# Enhanced Policy Chunks — v2.0 (structured metadata)

These are the four lender policy chunk files with **structured taxonomy metadata added**
to every chunk, per the Week 2 "Enhance all policy chunks with structured metadata" task.

## What changed vs v1.0
For each chunk, the following fields were inserted into the header (after `intent`,
before `policy_fields`). **All chunk content is byte-for-byte unchanged.**

| Field | Purpose |
|-------|---------|
| `lenders` | Canonical lender code (RESIMAC / BFS / WESTPAC / CFAL) |
| `borrower_profile` | Borrower tags (e.g. COMMERCIAL, PROPERTY_BACKED, MEDICAL_PROFESSIONAL) |
| `asset_class` | Asset codes (MV_NEW, EV, PRIMARY, SECONDARY, TERTIARY, LCV, …) |
| `doc_type` | Documentation pathway (LOW_DOC / LITE_DOC / FULL_DOC / NEW_BIZ) |
| `loan_size_band` | MICRO / SMALL / MEDIUM / LARGE / XLARGE / ALL |
| `answerable_questions` | Natural-language retrieval hints this chunk can answer |
| `confidence` | Analyst confidence in the chunk's accuracy |
| `last_verified` | Date the chunk was last verified against source |

The controlled vocabulary matches `docs/policy_chunks_v2.md` (v3 unified taxonomy),
so these fields can be used directly as **ChromaDB metadata filters** during retrieval.

## Files
- `resimac_chunks.md`  (8 chunks)
- `bfs_chunks.md`      (10 chunks)
- `westpac_chunks.md`  (9 chunks)
- `cfal_chunks.md`     (8 chunks)

File headers bumped to `version: 2.0`, `last_updated: 2026-07-01`.
`chunk_id` values are unchanged (stable vector-DB keys).

---

## Understanding `Metadata.csv` — the logic in plain words

### The core idea
Our RAG system stores every policy chunk as an **embedding** (a set of numbers that
captures the chunk's meaning). When a broker asks a question, the question is turned
into an embedding too, and the system finds the chunks whose embeddings are *closest*.
That is "semantic search".

The catch: embeddings alone are **fuzzy**. Ask *"What rate does Westpac charge for a
used truck?"* and pure semantic search might return a **Resimac** truck-rate chunk, or a
Westpac *eligibility* chunk — because they all "sound" related to trucks and Westpac.
That is exactly how a model produces a confident but **wrong** answer.

**Metadata is the fix.** It is a set of plain labels attached to each chunk (like tags on
a file). Instead of searching all 35 chunks by meaning alone, the system first **filters**
down to the chunks that match the *facts* of the question, then runs semantic search
inside that smaller, cleaner set.

> One-line analogy: **the embedding is *how* the system searches; the metadata is the set
> of guardrails that stop it searching in the wrong aisle.**

### What each column is for
Each column answers a different "which box does this chunk belong in?" question:

| Column | Plain-English job | Example filter |
|--------|-------------------|----------------|
| `lenders` | Which company the chunk belongs to. Kills most cross-lender mistakes on its own. | Question says "Westpac" → keep `WESTPAC` chunks only |
| `topic_intent` | What *kind* of question it answers (PRICING, ELIGIBILITY, EXCLUSIONS…). | "What's the rate?" → keep PRICING, drop SETTLEMENT |
| `borrower_profile` | Who is asking (a doctor, a renter, a new business). | Doctor → prefer `MEDICAL_PROFESSIONAL` chunks |
| `asset_class` | What is being financed. | "forklift" → keep `PRIMARY`; "EV" → keep `EV` |
| `doc_type` | Which paperwork tier applies. | "Low Doc" → keep `LOW_DOC` chunks |
| `loan_size_band` | Roughly how big the loan is. | "$300k" → keep `LARGE` chunks |
| `policy_fields` | The atomic facts inside (MAX_LOAN, BASE_RATE, PPSR…). | rate question → expect `BASE_RATE` |
| `answerable_questions` | Natural-language hints of what the chunk can answer — *improves* the semantic match. | boosts recall for paraphrased questions |
| `confidence` | How much to trust the chunk. | low confidence → flag for human review |
| `last_verified` | When it was last checked against the source PDF. | old date → may be stale, re-verify |

### How this helps the model do its two jobs

**1. Find the right answer faster (better retrieval).**
Filter first, search second. "Westpac + PRICING + a truck" narrows 35 chunks down to
maybe 2 *before* the fuzzy matching even runs. Result: faster, cheaper (fewer tokens),
and far more likely to surface the correct chunk instead of a look-alike.

**2. Double-check an answer (grounding / self-audit).**
After the model drafts an answer, we can compare it to the metadata of the chunk it
actually used:
- If the answer quotes a **rate** but the source chunk is **not** tagged `PRICING` /
  `BASE_RATE`, that is a red flag the answer was not truly grounded — likely a
  hallucination.
- If the answer mentions **Westpac** but the retrieved chunk is tagged `RESIMAC`, we
  caught cross-lender contamination automatically.
- `confidence` and `last_verified` tell us whether the *source itself* is trustworthy or
  possibly out of date, before we even trust the answer.

So the same tags that speed up retrieval also act as a cheap, automatic sanity check on
whether an answer is real.

### How the file is structured
`Metadata.csv` has **one row per chunk** (35 rows). Every column above is a filterable
field. The `chunk_id` is the stable key that links each row back to:
- the chunk in the enhanced `*_chunks.md` files, and
- the embedding record in ChromaDB.

Practically, Sameep loads each chunk into ChromaDB with these columns passed as the
`metadata` argument, then retrieval calls use `where={...}` filters (e.g.
`where={"lenders": "WESTPAC", "topic_intent": "PRICING"}`) *before* the vector search.

### Worked example — one question, start to finish

**Broker asks:** *"What's Westpac's Xpress rate for a used truck bought from a dealer?"*

**Step 1 — Read the question into filters.**
A light parsing/classifier step pulls the facts out of the question:

| Signal in the question | Metadata filter it sets |
|------------------------|-------------------------|
| "Westpac" | `lenders = WESTPAC` |
| "rate" | `topic_intent = PRICING` |
| "truck bought from a dealer" | `asset_class ∈ {PRIMARY}` |

**Step 2 — Filter first (the guardrail).**
ChromaDB applies the filter *before* any fuzzy matching:
`where={"lenders": "WESTPAC", "topic_intent": "PRICING"}`.
Of all 35 chunks, only **2** survive — `westpac_xpress_rates` and
`westpac_standard_rates`. Every Resimac/BFS/CFAL chunk, and every Westpac
eligibility/settlement chunk, is gone before the search even starts. This is what stops
the classic mistake of returning a Resimac truck rate to a Westpac question.

**Step 3 — Semantic search inside the survivors.**
Now the embedding match runs on just those 2 chunks. The word "Xpress" and the
`answerable_questions` hint on `westpac_xpress_rates` ("*What is the Xpress rate for a
car by term… What is the heavy-equipment Xpress rate?*") pull it to the top over the
"standard rates" chunk. **Retrieved chunk: `westpac_xpress_rates`.**

**Step 4 — Answer from that chunk only.**
The model reads the chunk and answers, citing the source:
> *"A used truck (>4.5T, up to 5 years old) from a licensed dealer is priced at 8.17% p.a.
> for a 24/36/48-month term, or 8.37% for 60 months. (Source: `westpac_xpress_rates`.)"*

**Step 5 — Double-check the answer against metadata (the audit).**
Before showing it to the broker, run cheap automatic checks:

| Check | Result |
|-------|--------|
| Answer mentions a rate → source chunk tagged `PRICING` / `BASE_RATE`? | ✅ yes → grounded |
| Answer says "Westpac" → source chunk `lenders = WESTPAC`? | ✅ yes → no cross-lender leak |
| Source `confidence`? | `high` → safe to auto-serve |
| Source `last_verified`? | `2026-06-15` (rate card date) → current |

All green, so the answer is served. If, say, the model had instead grabbed a chunk
tagged `RESIMAC`, or a chunk with no `PRICING` tag, the audit would fail and we'd route
the answer to human review (the bonus "human review interface" in the brief) instead of
trusting it.

> **This is the whole payoff in one example:** the metadata makes retrieval land on the
> right chunk in step 2, *and* gives us a way to prove the answer came from the right
> place in step 5 — the same tags do both jobs.

---

## Companion deliverables
- `Metadata.csv`       — one row per chunk, all taxonomy fields flattened (35 rows)
- `QuestionBank.xlsx`  — 100 gold-standard questions (25/lender) with 4/4 reference answers
- `GroundTruth.xlsx`   — 100 scored candidate answers (1–4) with rationales + per-level tabs
