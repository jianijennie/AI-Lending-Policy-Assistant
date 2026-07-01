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

## How `Metadata.csv`, `QuestionBank.xlsx` and `GroundTruth.xlsx` work together

These three files are not separate islands — they are **linked by one shared key: the
`chunk_id`** (called `Source Chunk ID` in the Excel files). That key is what lets us tie a
test question back to the exact policy chunk it should be answered from.

Think of it as three layers of the same system:

| File | What it holds | Its job |
|------|---------------|---------|
| `Metadata.csv` | The **labels** on each policy chunk (35 rows) | Helps the model *find* the right chunk |
| `QuestionBank.xlsx` | 100 **questions** + the correct (4/4) answer + `Source Chunk ID` | Says *what the model should be asked* and *where the answer lives* |
| `GroundTruth.xlsx` | The same 100 questions with **scored answers (1–4)** + why | Says *how to grade the model's answers* |

### How they interact, step by step

1. **A question in `QuestionBank.xlsx` points to a chunk.**
   Every question carries a `Source Chunk ID` — the chunk that contains its answer. That
   ID is the *same* `chunk_id` used in `Metadata.csv` and in ChromaDB.

2. **`Metadata.csv` helps the model retrieve that chunk.**
   When we test the model with a question, the metadata filters (lender, topic, asset…)
   narrow the search so the model lands on the correct chunk — ideally the very one listed
   in the question's `Source Chunk ID`. If it retrieves a *different* chunk, that's an
   early sign retrieval is going wrong, before we even look at the answer.

3. **`GroundTruth.xlsx` grades the result.**
   The model's answer is compared against the scored examples. The 4/4 answer is the
   target; the 3/4, 2/4 and 1/4 examples teach the grader *what different kinds of wrong
   look like* — so it can score the model's live answers consistently.

4. **The metadata closes the loop (auto-audit).**
   Because the question, the chunk, and the chunk's labels all share the `chunk_id`, we
   can automatically check: *did the model answer a PRICING question using a chunk tagged
   `PRICING`?* If not, the answer is flagged — the same guardrail described earlier, now
   measured across the whole test set.

### Short example

Take question **`WBC-03`** in `QuestionBank.xlsx`:

> *"What is Westpac's Xpress rate for a dealer-sourced car on a 36-month term…?"*
> `Source Chunk ID = westpac_xpress_rates`

- **QuestionBank** says: the correct answer is 7.75% (24/36/48mo), and it should come from
  `westpac_xpress_rates`.
- **Metadata.csv** row for `westpac_xpress_rates` says: `lenders = WESTPAC`,
  `topic_intent = PRICING`, `confidence = high`, `last_verified = 2026-06-15`. → These
  filters make the model retrieve exactly this chunk.
- **GroundTruth.xlsx** row `WBC-03` says: an answer of "7.75%" scores **4/4**; an answer of
  "8.8% max brokerage" scores **2/4** (right lender, wrong number); an answer quoting a
  Resimac rate scores **1/4**.
- **Auto-audit:** the question is PRICING and the retrieved chunk is tagged PRICING, from
  WESTPAC, verified 2026-06-15 → the answer is trustworthy. ✅

One `chunk_id` (`westpac_xpress_rates`) ties all three files together for that question.

### Keeping the Q&A database up to date over time

Policies change — rate cards get repriced, limits move, new assets get added. When that
happens, the three files must stay in sync. The rule is simple: **the `chunk_id` is the
anchor; everything else follows it.**

When a **policy changes**:
1. Update the affected chunk in `policies/*_chunks.md` and bump its `last_verified` date
   (and the file `version`).
2. Update that chunk's row in `Metadata.csv` if any label changed (e.g. a new asset class).
3. Find every QuestionBank/GroundTruth row whose `Source Chunk ID` matches that chunk, and
   **re-check the answer** — if a rate moved from 7.75% to 7.90%, the 4/4 answer (and the
   wrong-answer variants built off it) must be corrected too.
4. Re-embed only the changed chunk in ChromaDB.

When **adding new questions**:
- Give each a new `ID` (e.g. `WBC-26`) and a valid `Source Chunk ID` that already exists in
  `Metadata.csv`. This guarantees every question is answerable from a real, labelled chunk.

When **adding a new lender or chunk**:
- Add the chunk to `policies/`, add its row to `Metadata.csv` (using the shared vocabulary
  in `policy_chunks_v2.md`), then write its QuestionBank/GroundTruth questions.

> **Golden rule:** never let a QuestionBank/GroundTruth row point to a `Source Chunk ID`
> that doesn't exist in `Metadata.csv`. As long as that link holds, the whole evaluation
> set stays consistent with the live knowledge base. A quick check — confirming every
> `Source Chunk ID` in the Excel files appears in `Metadata.csv` — catches breakages early
> and can be run automatically before each update is merged.

---

## The dynamic Answer Library (where this is heading)

Everything above describes the **starter set** of 100 questions. The bigger goal is for the
question list to be **dynamic** — it grows every time a real broker (or anyone) asks
something new. This turns the Q&A files into a living **Answer Library** (the "Persistent
Answer Library" in the CMAP brief).

### The idea in simple words

When a new question comes in:
1. It is **stored** in the library with its own `ID`, its answer, a `score`, a
   `Source Chunk ID`, and the same **metadata tags** (lender, topic, asset, etc.).
2. Next time someone asks the **same or a very similar** question, the system finds the
   stored answer and **serves it directly** — no need to run the full retrieval + LLM
   pipeline again.

Why this matters: it **saves time and tokens**. A cached answer is basically free compared
to re-embedding, re-retrieving, and re-generating from scratch. The more the library grows,
the more questions get answered instantly and consistently.

### How a new question flows in

```
Broker asks a question
        │
        ▼
Is a very similar question already in the library?   ── yes ──►  Serve the stored answer
        │                                                        (fast, ~0 tokens)
        │ no
        ▼
Run the normal pipeline (metadata filter → retrieve chunk → LLM answer)
        │
        ▼
Auto-score the answer against GroundTruth examples + tag it with metadata
        │
        ▼
Confident (high score, tags match)? ── yes ──►  Add to library automatically
        │
        │ no / borderline
        ▼
Send to a human reviewer to confirm or fix, then add to library
```

This is the **hybrid** model: the system auto-scores first, and only the low-confidence
answers go to a human. That keeps it fast while stopping wrong answers from poisoning the
library — and the human-review step is the **bonus deliverable** the brief rewards.

### "Similar question" — how the metadata helps twice

The same metadata tags do two jobs here:

- **Matching:** to decide if a new question is "already answered", we compare its meaning
  (embedding) **and** its tags. Two questions that are both `WESTPAC` + `PRICING` + a truck
  are far more likely to be true duplicates than two questions that just share a few words.
  Tags stop the cache from returning a Resimac answer to a Westpac question.
- **Re-checking:** because each stored answer carries its `Source Chunk ID`, we can
  periodically re-verify the library against the live chunks. If a chunk's
  `last_verified` date changes (a policy update), every cached answer built on that
  `chunk_id` is automatically flagged for re-scoring. The library never silently goes stale.

### Short example

- A broker asks: *"Westpac Xpress rate for a dealer car, 3-year term?"*
- The system sees this is `WESTPAC` + `PRICING`, embedding-close to stored question
  `WBC-03`. → It serves the cached 4/4 answer ("7.75%") instantly. **No LLM call.**
- Later, Westpac reprices and `westpac_xpress_rates` gets a new `last_verified` date. →
  Every library entry with `Source Chunk ID = westpac_xpress_rates` (including this one) is
  flagged, re-scored, and — if the rate changed — updated. The next broker still gets a
  correct, fast answer.

> In short: **QuestionBank + GroundTruth are the seed; the Answer Library is what they grow
> into.** Metadata is what makes both the fast-match and the stay-accurate parts work.

---

## Week 3 handoff — who does what next

This is where the closely-linked work between the Finance/Policy side and the RAG/data side
comes together.

### Maksim (Finance & Policy Analyst) — next tasks
- **Define the "similarity threshold"** for what counts as a duplicate question (with
  Sameep) — how close is "close enough" to reuse a cached answer.
- **Grow the question set** beyond the seed 100: add cross-lender **COMPARE / RECOMMEND /
  DIFFERENCE** questions (the taxonomy already supports these intents), since brokers often
  ask "which lender is best for X".
- **Own the human-review step** of the hybrid flow: review low-confidence auto-scored
  answers, correct them, and set the final score before they enter the library.
- **Keep the golden rule enforced:** every new library entry must have a valid
  `Source Chunk ID` that exists in `Metadata.csv`.

### Sameep (AI / RAG & Data Engineer) — next tasks
- **Load the enhanced chunks into ChromaDB** with the `Metadata.csv` fields passed as the
  `metadata` argument, so `where={...}` filtering works.
- **Wire up metadata-filtered retrieval:** parse the incoming question into tags
  (lender, intent, asset…) and apply them as filters *before* the vector search.
- **Build the Answer Library as a second collection** (or table): store each answered
  question as an embedding + its `ID`, `score`, `Source Chunk ID`, and tags. On a new
  question, check this library first (semantic + tag match) before hitting the main
  pipeline — this is the token/time saver.
- **Implement the auto-score + flag step:** compare a generated answer to the GroundTruth
  examples, attach a score, and route borderline ones to Maksim's review queue.
- **Add the staleness check:** when a chunk's `last_verified` changes, flag every library
  entry sharing that `chunk_id` for re-scoring.

> The two roles meet at the `chunk_id` and the metadata tags: Maksim keeps the questions,
> answers and labels correct; Sameep makes the retrieval, caching and auto-scoring run on
> them. As long as both sides respect the shared `chunk_id` key, the system stays in sync.

---

## Companion deliverables
- `Metadata.csv`       — one row per chunk, all taxonomy fields flattened (35 rows)
- `QuestionBank.xlsx`  — 100 gold-standard questions (25/lender) with 4/4 reference answers
- `GroundTruth.xlsx`   — 100 scored candidate answers (1–4) with rationales + per-level tabs
