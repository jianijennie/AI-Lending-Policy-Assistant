import json
import math
import os
import sys
import threading
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_index.core import Settings

from src.query import query_policies
from src.config import (
    ANSWER_LIBRARY_PATH, QUERY_CACHE_PATH, QUERY_CACHE_SIMILARITY_THRESHOLD,
    QUERY_CACHE_ENABLED,
)

app = FastAPI(title="LifeX Policy Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_answer_library_lock = threading.Lock()
_query_cache_lock = threading.Lock()

LENDERS = ["BFS", "Resimac", "Westpac", "CFAL", "Angle", "Flexi", "Metro"]


def _embed(text: str):
    # Same embedding model used for retrieval — comparing question meaning,
    # not just word overlap, so e.g. "primary assets" vs "secondary assets"
    # (same words otherwise, different correct answer) doesn't false-match.
    return Settings.embed_model.get_query_embedding(text)


def _cosine_similarity(a, b) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def _load_query_cache():
    if os.path.exists(QUERY_CACHE_PATH):
        with open(QUERY_CACHE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _find_cached(question: str):
    q_embedding = _embed(question)
    best, best_score = None, 0.0
    for entry in _load_query_cache():
        score = _cosine_similarity(q_embedding, entry["embedding"])
        if score > best_score:
            best, best_score = entry, score
    if best and best_score >= QUERY_CACHE_SIMILARITY_THRESHOLD:
        return best
    return None


def _append_to_query_cache(question: str, answer: str, sources: list):
    with _query_cache_lock:
        cache = _load_query_cache()
        cache.append({
            "question": question,
            "answer": answer,
            "sources": sources,
            "embedding": _embed(question),
        })
        os.makedirs(os.path.dirname(QUERY_CACHE_PATH), exist_ok=True)
        # Write to a temp file then atomically replace, rather than
        # truncating QUERY_CACHE_PATH in place. FastAPI's sync endpoints run
        # in a thread pool, so a concurrent request's unlocked _load_query_cache
        # read could otherwise land mid-write and hit a half-written/invalid
        # JSON file. os.replace is atomic on both Windows and POSIX, so any
        # concurrent reader always sees either the old or the new file whole.
        tmp_path = QUERY_CACHE_PATH + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2)
        os.replace(tmp_path, QUERY_CACHE_PATH)


class HistoryTurn(BaseModel):
    question: str
    answer: str


class QueryRequest(BaseModel):
    question: str
    history: list[HistoryTurn] = []


class Source(BaseModel):
    chunk_id: str
    lender: str
    intent: str
    score: float


class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]
    response_time: float
    from_cache: bool


class HealthResponse(BaseModel):
    status: str
    lenders: list[str]
    chunks: int


class SaveAnswerRequest(BaseModel):
    question: str
    answer: str
    chunk_ids: list[str]


class SaveAnswerResponse(BaseModel):
    status: str
    entry_id: int


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    start = time.time()

    # Follow-ups are only meaningful in the context of their own
    # conversation, so they neither read from nor write to the general
    # question cache — caching one could later return it as a generic
    # answer to an unrelated standalone question.
    if QUERY_CACHE_ENABLED and not request.history:
        cached = _find_cached(request.question)
        if cached:
            return QueryResponse(
                answer=cached["answer"],
                sources=[Source(**s) for s in cached["sources"]],
                response_time=time.time() - start,
                from_cache=True,
            )

    history = [h.model_dump() for h in request.history]
    try:
        answer, nodes = query_policies(request.question, verbose=False, history=history)
    except Exception as e:
        # Without this, an unhandled exception here (OpenAI down after all
        # retries, a ChromaDB hiccup, etc.) surfaces to the frontend as a
        # generic connection failure indistinguishable from "the backend
        # isn't running at all" — the exact confusing failure mode already
        # diagnosed once before in this project for an unrelated bug. A
        # distinct 503 at least tells the frontend/broker the backend is up
        # but the question itself failed, so they know to just retry.
        raise HTTPException(status_code=503, detail=f"Couldn't process that question — please try again. ({type(e).__name__})")
    elapsed = time.time() - start

    sources = [
        Source(
            chunk_id=node.metadata.get("chunk_id", "unknown"),
            lender=node.metadata.get("lenders", "unknown"),
            intent=node.metadata.get("topic_intent", "unknown"),
            score=node.score,
        )
        for node in nodes
    ]

    if QUERY_CACHE_ENABLED and not request.history:
        _append_to_query_cache(request.question, answer, [s.model_dump() for s in sources])

    return QueryResponse(
        answer=answer,
        sources=sources,
        response_time=elapsed,
        from_cache=False,
    )


@app.get("/health", response_model=HealthResponse)
def health():
    from src.query import _chroma_collection

    return HealthResponse(status="ok", lenders=LENDERS, chunks=_chroma_collection.count())


@app.post("/answer-library/save", response_model=SaveAnswerResponse)
def save_answer(request: SaveAnswerRequest):
    with _answer_library_lock:
        if os.path.exists(ANSWER_LIBRARY_PATH):
            with open(ANSWER_LIBRARY_PATH, "r", encoding="utf-8") as f:
                library = json.load(f)
        else:
            library = []

        entry_id = len(library) + 1
        library.append({
            "id": entry_id,
            "question": request.question,
            "answer": request.answer,
            "chunk_ids": request.chunk_ids,
        })

        os.makedirs(os.path.dirname(ANSWER_LIBRARY_PATH), exist_ok=True)
        with open(ANSWER_LIBRARY_PATH, "w", encoding="utf-8") as f:
            json.dump(library, f, indent=2)

    return SaveAnswerResponse(status="saved", entry_id=entry_id)
