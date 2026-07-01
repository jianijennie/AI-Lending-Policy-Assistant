# `policies/` — Lender Policy Chunks

This folder holds the **knowledge base** for the RAG system: the actual lender policy
text, cut into small labelled pieces called **chunks**. These are the files the AI reads
from when answering a broker's question.

## What's in here

| File | Lender | Chunks |
|------|--------|:------:|
| `resimac_chunks.md` | Resimac Asset Finance | 8 |
| `bfs_chunks.md` | Branded Financial Services (BFS) | 10 |
| `westpac_chunks.md` | Westpac Equipment Finance | 9 |
| `cfal_chunks.md` | Capital Finance Australia (CFAL) | 8 |

**35 chunks total, across 4 lenders.**

## What a "chunk" is (in simple words)

Instead of feeding the AI a whole 100-page PDF, we split each lender's policy into small,
self-contained pieces — one per topic (e.g. eligibility, interest rates, exclusions).
Each chunk has:

- a **`chunk_id`** — a stable name (e.g. `westpac_drivexpress`). This is the key the
  vector database uses; **never rename it.**
- a **header of metadata** — plain labels describing the chunk (which lender, what topic,
  which assets, etc.). These are used as *filters* so the AI searches the right chunks.
- the **`Content`** — the actual policy text, taken word-for-word from the source PDFs.

The AI turns each chunk into an "embedding" (numbers that capture its meaning) and stores
it in ChromaDB. When a broker asks a question, the system finds the closest chunks and
answers from them — quoting the `chunk_id` as the source.

## What changed in v2.0 (July 2026)

**v1.0** had the basic header (`source`, `topic`, `intent`, `policy_fields`,
`trigger_words`).

**v2.0** adds **structured taxonomy metadata** to every chunk header — extra labels that
let the system filter to the right chunks *before* it searches, and double-check that an
answer really came from the right place:

| New field | What it says |
|-----------|--------------|
| `lenders` | Which company (RESIMAC / BFS / WESTPAC / CFAL) |
| `borrower_profile` | Who it applies to (e.g. COMMERCIAL, PROPERTY_BACKED, MEDICAL_PROFESSIONAL) |
| `asset_class` | What's being financed (MV_NEW, EV, PRIMARY, SECONDARY, TERTIARY, LCV…) |
| `doc_type` | Paperwork tier (LOW_DOC / LITE_DOC / FULL_DOC / NEW_BIZ) |
| `loan_size_band` | Rough loan size (MICRO / SMALL / MEDIUM / LARGE / XLARGE) |
| `answerable_questions` | Plain-English hints of what the chunk can answer |
| `confidence` | How much to trust the chunk |
| `last_verified` | When it was last checked against the source PDF |

> **Important:** v2.0 only **added header labels**. The policy `Content` and all
> `chunk_id` values are **unchanged** — so the diff is clean and Sameep's ingest script
> needs no path or key changes.

The label values follow the shared vocabulary in
[`../docs/policy_chunks_v2.md`](../docs/policy_chunks_v2.md), so they plug straight into
ChromaDB as metadata filters.

## Why the metadata matters (one-line version)

The embedding is *how* the system searches; the metadata is the **guardrails** that stop
it searching in the wrong aisle — e.g. returning a Resimac rate to a Westpac question.
A full explanation, with a worked example, is in
[`../docs/README_ENHANCED.md`](../docs/README_ENHANCED.md).

## How to update these files

1. Edit only the affected chunk(s).
2. Bump `last_updated` and `version` in the file header.
3. Re-embed only the changed chunks.
4. **Never change `chunk_id` values** — they are the stable keys the vector DB relies on.

## Related files (in `../docs/`)

- `Metadata.csv` — every chunk's labels in one flat table (35 rows)
- `QuestionBank.xlsx` — 100 gold-standard test questions (25 per lender)
- `GroundTruth.xlsx` — 100 scored answers (1–4) with rationales, for evaluating the model
- `README_ENHANCED.md` — full explanation of the metadata logic + worked example
