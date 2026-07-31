import os
from pathlib import Path
from dotenv import load_dotenv

# Single source of truth for "where is the project" — every path below is
# derived from this, so the project can be cloned/copied anywhere (a
# teammate's machine, a different drive letter) and still resolve correctly.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATA_DIR = str(PROJECT_ROOT / "data" / "documents")
# Lives inside the project (not a sibling folder) because it's fully
# regenerable from data/chunks/*.md via `python src/ingest.py` — nothing
# here is hand-authored, so there's no migration cost to keeping it local.
CHROMA_DIR = str(PROJECT_ROOT / "chroma_db")

# bge-small (33M params) is what the "0.90-0.96 band" recall problem above
# was calibrated against — it's the reason a cross-encoder reranker had to
# exist at all: the reranker can only re-score chunks bge-small's first pass
# already found, so a chunk missed entirely at that stage is unrecoverable.
# bge-base (109M params) is the same BAAI family (drop-in via
# HuggingFaceEmbedding, no new network dependency, no API cost) and scores
# meaningfully higher on retrieval benchmarks. Chosen over bge-large
# (335M) given this machine's prior history of memory-pressure issues
# (see chat history) — base is a safer size increase, not the largest one.
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
# Answering model. Originally benchmarked head-to-head on 5 known-ground-truth
# questions (2026-07-22): gpt-4o-mini made 3 factual errors with the
# full-corpus context, gpt-5-mini was correct but verbose and slow
# (2-14s, up to 4k-char answers), gpt-5 was correct on everything,
# fastest of the GPT-5 family here (2.4-7.4s), and the only one that
# reliably followed the verdict-first/brevity instructions.
#
# Switched gpt-5 -> gpt-5.5 on 2026-07-31 after a second head-to-head, this
# time across 11 questions (one per complexity type in the 111-question
# stress bank): identical correctness on 10/11, and gpt-5.5 caught a real
# gap gpt-5 missed on the 11th (CQ-102, "cheapest lender for a $200k primary
# asset") — gpt-5 quoted Flexi's standard-tier rate (7.85%) and missed the
# cheaper flexipremium tier entirely (7.15%, this project's own corrected
# rate), while gpt-5.5 correctly identified flexipremium as the applicable
# tier. gpt-5.5 was also faster on every single question tested, often by
# 2x+. ~$0.01-0.05 per question at gpt-5 input pricing — irrelevant against
# the budget, and gpt-5.5 is the same non-mini/non-pro tier so priced
# similarly.
LLM_MODEL = "gpt-5.5"
# Small utility model for the follow-up resolver — rewrites "details" /
# "what about westpac?" into standalone questions. Kept on gpt-4o-mini
# deliberately: GPT-5 family models ignore temperature, so the same
# follow-up resolves to a different standalone question run to run — for
# the answerer that variance is tolerable, but the resolver feeds lender
# detection, where a differently-worded rewrite can change which lenders
# get retrieved at all. 4o-mini at temperature=0 is stable and was already
# proven at this job.
RESOLVER_MODEL = "gpt-4o-mini"
# For GPT-5 family models only: how much internal reasoning to spend.
# Raised from "minimal" to "low" on 2026-07-25 after finding a reproducible
# bug at "minimal": on multi-step rate calculations, the model would state a
# headline number before it had actually worked out the right table row,
# then correctly derive a DIFFERENT number in its own shown breakdown and
# never reconcile the two (e.g. answering "9.64% p.a." as the headline while
# the working two lines later computes "12.64% + 2.00% = 14.64%"). Verified
# 3/3 that "low" eliminates this; latency cost is real (~2-3x slower per
# query, 2-3s -> 6-8s) but was judged worth it over silently wrong headline
# numbers on calculation questions.
REASONING_EFFORT = "low"
# Scoped back down for the one case where "low" cost far more than 2-3x:
# when NO lender is named, retrieval fans out across all 7 lenders (up to
# ~140 chunks vs ~8-20 for a single named lender), and "low" effort over
# that much context measured 20-56s per question — 3-8x worse than the
# single-lender case, for a question type (broad eligibility scans: "which
# lenders can do X", "best-fit across the panel") that's mostly yes/no
# verdicts, not the numeric rate build-ups "low" was raised to fix. Falls
# back to the cheapest tier specifically for that no-lender-detected
# fan-out path.
#
# Was "minimal" under gpt-5 -- gpt-5.5 doesn't support that value at all
# (hard 400 error; its scale is none/low/medium/high/xhigh, no "minimal").
# Re-benchmarked "none" vs "low" head-to-head on 6 genuine fan-out questions
# before picking "none": both gave equivalent-quality answers with no
# regressions vs the old gpt-5/minimal baseline, but "none" was faster in
# 4/6 cases and never worse -- "none" is the correct like-for-like mapping
# of "minimal"'s original intent (cheapest/fastest tier for this
# mostly-yes/no question type), not an arbitrary substitute.
FANOUT_REASONING_EFFORT = "none"

CHUNKS_DIR = str(PROJECT_ROOT / "data" / "chunks")
METADATA_PATH = str(PROJECT_ROOT / "data" / "Metadata" / "Metadata.csv")
QUESTION_BANK_PATH = str(PROJECT_ROOT / "data" / "Metadata" / "QuestionBank.xlsx")
# The current scenario-based bank (41 questions, no exact chunk_id column —
# graded by reading the answer against reference_answer, not auto-scored).
SCENARIO_QUESTION_BANK_PATH = str(PROJECT_ROOT / "policy_question_bank.xlsx")
# 111-question stress-test set (2026-07-22): cross-lender comparisons,
# multi-filter, contradiction detection, negative/trap constraints, etc. —
# harder and more adversarial than the 41-question scenario bank above.
COMPLEX_QUESTION_BANK_PATH = str(PROJECT_ROOT / "ComplexQuestions.xlsx")
GROUND_TRUTH_PATH = str(PROJECT_ROOT / "data" / "Metadata" / "GroundTruth.xlsx")
ANSWER_LIBRARY_PATH = str(PROJECT_ROOT / "data" / "answer_library.json")
QUERY_CACHE_PATH = str(PROJECT_ROOT / "data" / "query_cache.json")
# Deliberately conservative: bge-small embeddings don't reliably separate
# genuine paraphrases from same-wording-different-detail questions (e.g.
# "Tier 2" vs "Tier 3") in the 0.90-0.96 band for this domain's short,
# structurally similar questions. A wrong cached financial figure is a much
# worse failure than a missed cache hit, so this trades cache recall for
# guaranteed precision — see chat history for the calibration data.
QUERY_CACHE_SIMILARITY_THRESHOLD = 0.97
# The 0.97 threshold above was calibrated against bge-small embeddings and
# never recalibrated after the swap to bge-base — an uncalibrated
# similarity cache can return a *wrong but confident* old answer for a
# similar-wording-different-detail question, which in a competition is a
# far worse failure than the few seconds a cache hit saves. Off until/unless
# it's recalibrated.
QUERY_CACHE_ENABLED = False

# Unlike the raw semantic query cache above, every answer_library.json entry
# has already been through a human review/approval step in the frontend's
# Review tab (and may have been hand-corrected there) before it's ever
# saved -- that's a fundamentally different trust level than caching every
# unreviewed LLM output, so it's safe to actually serve these back at query
# time. Still uses the same conservative threshold as QUERY_CACHE (same
# uncalibrated-embedding caveat applies), since a wrongly-matched *human
# correction* served to an unrelated question is just as bad a failure mode.
ANSWER_LIBRARY_SIMILARITY_THRESHOLD = 0.97
ANSWER_LIBRARY_ENABLED = True

# Each chunk in data/chunks/*.md is already a hand-curated atomic unit with
# its own chunk_id, lender/intent/trigger-word metadata — SentenceSplitter's
# job here is only to be a safety net, never to actually re-split one.
# 1024 was too tight for that: it silently fragmented longer chunks (e.g.
# angle_doc_types at ~3800 chars) into multiple pieces that share a
# chunk_id but each hold only part of the content, so retrieval could
# return one half without the other. Sized well above the longest current
# chunk (~3800 chars) with real headroom for future edits.
CHUNK_SIZE = 4096
CHUNK_OVERLAP = 100
TOP_K = 5
