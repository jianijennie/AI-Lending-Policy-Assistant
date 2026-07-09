import os
import re
import sys
import time
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import chromadb
# from groq import Groq as GroqClient
from openai import OpenAI
from src.config import LLM_MODEL, TOP_K

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ── Initialise once at module load ──────────────────────────────────────────
print("Initialising embedding model and ChromaDB...")
_embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.embed_model = _embed_model
Settings.llm = None

_chroma_client = chromadb.PersistentClient(path="C:/Projects/chroma_db")
_chroma_collection = _chroma_client.get_collection("lifex_policies")
_vector_store = ChromaVectorStore(chroma_collection=_chroma_collection)
_storage_context = StorageContext.from_defaults(vector_store=_vector_store)
_index = VectorStoreIndex.from_vector_store(
    _vector_store,
    storage_context=_storage_context
)
_openai_client = OpenAI(api_key=OPENAI_API_KEY)
print("Ready.\n")
# ────────────────────────────────────────────────────────────────────────────

LENDER_KEYWORDS = {
    "WESTPAC": ["westpac", "wef", "xpress"],
    "BFS": ["bfs", "branded financial", "bfs plus", "bfs prime"],
    "RESIMAC": ["resimac", "premiumplus", "premium plus"],
    "CFAL": ["cfal", "capital finance", "capital finance australia"],
    "ANGLE": ["angle", "angle finance"],
    "FLEXI": ["flexi", "flexicommercial", "flexipremium", "flexireplacement"],
    "METRO": ["metro", "metro finance", "metroeco"]
}

INTENT_KEYWORDS = {
    "PRICING": ["rate", "rates", "interest", "pricing", "%", "per annum",
                "how much does it cost", "what rate", "base rate",
                "headline rate", "under flexipremium", "flexipremium deal"],
    "ELIGIBILITY": ["eligible", "qualify", "eligibility", "abn", "gst",
                    "credit score", "minimum", "criteria", "who can",
                    "can i apply", "do i qualify", "deposit required",
                    "which tiers", "auto-decline", "auto decline"],
    "LOAN_LIMITS": ["maximum loan", "how much can i borrow", "borrow",
                    "loan limit", "max loan", "loan amount", "lvr", "naf",
                    "net amount financed", "exposure limit", "high-value loan",
                    "high value loan", "loan range", "loan term", "maximum term",
                    "exposure", "total exposure"],
    "DOCUMENTATION": ["documents", "documentation", "what do i need",
                      "financials", "tax return", "bank statements",
                      "low doc", "full doc", "lite doc", "paperwork",
                      "mid doc"],
    "FEES": ["fee", "fees", "establishment fee", "brokerage", "commission",
             "clawback", "above 5.5", "introducer", "setup fee",
             "monthly fee", "account keeping", "origination", "cost",
             "paid out within", "early termination", "loading for brokerage"],
    "SETTLEMENT": ["settle", "settlement", "ppsr", "insurance",
                   "certificate of currency", "coc", "biometrics",
                   "payout", "signed documents", "what is required to settle",
                   "before settlement"],
    "EXCLUSIONS": ["excluded", "not allowed", "cannot", "restriction",
                   "decline", "not eligible", "used for debt",
                   "used for cash", "interlock", "very remote"],
    "SPECIAL_PROGRAMS": ["medical", "rollover", "replacement", "specialist",
                         "physiotherapist", "pharmacist", "doctor", "dental",
                         "vet", "allied health", "replace contract",
                         "roll over", "refinance existing", "existing contract",
                         "medical channel", "medical equipment",
                         "low doc program", "$400k low doc", "400k low doc",
                         "abn under 2 years", "under 2 years"],
    "ASSET_ELIGIBILITY": ["asset type", "asset class", "what assets",
                          "can i finance", "can bfs finance",
                          "can westpac finance", "can resimac finance",
                          "can cfal finance", "classification", "classify",
                          "category", "asset age", "maximum age", "how old",
                          "vehicle type", "caravan", "motorbike",
                          "eligible asset", "what vehicles", "heavy equipment",
                          "private sale", "plant", "motorcycle",
                          "bfs private sale", "medical and dental equipment",
                          "dental equipment"]
}


def _parse_retry_after(message: str, default: float = 5.0) -> float:
    m = re.search(r"try again in ([\d.]+)(ms|s)", message)
    if not m:
        return default
    value, unit = float(m.group(1)), m.group(2)
    seconds = value / 1000 if unit == "ms" else value
    return seconds + 0.5


def detect_lender(question: str):
    q = question.lower()
    for lender, keywords in LENDER_KEYWORDS.items():
        if any(kw in q for kw in keywords):
            return lender
    return None


def detect_intent(question: str):
    q = question.lower()
    scores = {}
    for intent, keywords in INTENT_KEYWORDS.items():
        scores[intent] = sum(1 for kw in keywords if kw in q)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None


def get_retriever(where_filter=None):
    if where_filter:
        return _index.as_retriever(
            similarity_top_k=TOP_K,
            vector_store_kwargs={"where": where_filter}
        )
    return _index.as_retriever(similarity_top_k=TOP_K)


def query_policies(question: str, verbose: bool = True):
    def log(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    log(f"\nQuestion: {question}")
    log("-" * 60)

    lender = detect_lender(question)
    intent = detect_intent(question)

    log(f"Detected lender: {lender or 'None (searching all)'}")
    log(f"Detected intent: {intent or 'None (searching all)'}")

    where_filter = None
    if lender and intent:
        where_filter = {
            "$and": [
                {"lenders": {"$eq": lender}},
                {"topic_intent": {"$eq": intent}}
            ]
        }
    elif lender:
        where_filter = {"lenders": {"$eq": lender}}
    elif intent:
        where_filter = {"topic_intent": {"$eq": intent}}

    log(f"Filter applied: {where_filter}")

    retriever = get_retriever(where_filter)
    nodes = retriever.retrieve(question)

    if not nodes:
        log("No results with filter — falling back to unfiltered search")
        nodes = get_retriever().retrieve(question)

    log(f"\nRetrieved {len(nodes)} chunks:")
    context = ""
    for i, node in enumerate(nodes):
        chunk_id = node.metadata.get('chunk_id', 'unknown')
        lender_tag = node.metadata.get('lenders', 'unknown')
        intent_tag = node.metadata.get('topic_intent', 'unknown')
        score = node.score
        log(f"  [{i+1}] {chunk_id} | {lender_tag} | {intent_tag} | score: {score:.3f}")
        context += f"\n[Source: {chunk_id} | Lender: {lender_tag}]\n{node.text}\n"

    prompt = f"""You are a finance policy assistant for LifeX Asset Finance.
Answer the broker's question using ONLY the policy excerpts provided below.
For every fact in your answer, state which chunk_id it comes from.
If the information is not in the excerpts, say "This information is not available in the provided policy documents."

Policy excerpts:
{context}

Broker's question: {question}

Answer:"""
    max_retries = 8
    for attempt in range(max_retries):
        try:
            response = _openai_client.chat.completions.create(
                model=LLM_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            break
        except Exception as e:
            is_rate_limit = "rate_limit" in str(e).lower() or "429" in str(e)
            if attempt < max_retries - 1 and is_rate_limit:
                time.sleep(_parse_retry_after(str(e)))
                continue
            raise
    answer = response.choices[0].message.content
    log(f"\nAnswer:\n{answer}")

    return answer, nodes


if __name__ == "__main__":
    print("LifeX Policy Assistant - type 'quit' to exit\n")
    while True:
        question = input("Your question: ")
        if question.lower() == "quit":
            break
        if question.strip():
            query_policies(question)
            print()