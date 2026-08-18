# LifeX Policy Assistant — Technical Documentation (Week 4)

> **Historical record — superseded by [`Technical_Documentation.md`](Technical_Documentation.md).**
> This describes the system as it stood at the end of Week 4 and is kept for the design
> history it carries (notably §3, the automated chunk-extraction pipeline and why it was
> rolled back). For how the system behaves **now** — the two answer caches, correction
> handling, reasoning-effort routing, and current evaluation results — read the current
> document instead.

This document covers three things: (1) how the current RAG system works end to end, (2) the technical changes made this week, and (3) the automated chunk-extraction pipeline that was designed, built, piloted, and then rolled back this week.

---

## 1. How the current system works

### 1.1 Data layer

```
data/documents/*.pdf     25 source PDFs across 7 lenders (rate cards, credit matrices, checklists, fact sheets)
data/chunks/*.md         62 hand-curated policy chunks, one .md file per lender
```

Each lender has its own chunk file (`angle_chunks.md`, `bfs_chunks_v2.md`, `cfal_chunks_v2.md`, `flexi_chunks.md`, `metro_chunks.md`, `resimac_chunks_v2.md`, `westpac_chunks_v2.md`). A chunk file has a file-level header comment block (source docs, licence, effective date, update instructions) followed by chunks separated by `\n---\n`. Each chunk looks like:

```
## chunk_id: <stable_snake_case_id>
**source:** <lowercase lender code>
**topic:** <topic_slug>
**intent:** <ELIGIBILITY|PRICING|LOAN_LIMITS|DOCUMENTATION|FEES|SETTLEMENT|EXCLUSIONS|SPECIAL_PROGRAMS|ASSET_ELIGIBILITY|MEDICAL_PROGRAMS|ROLLOVER_REPLACEMENT>
**lenders:** <WESTPAC|BFS|RESIMAC|CFAL|ANGLE|FLEXI|METRO>   (exactly one)
**borrower_profile:** comma-separated tags (COMMERCIAL, CONSUMER, HIGH_CREDIT, PROPERTY_BACKED, ...)
**asset_class:** comma-separated tags (MV_NEW, MV_USED, PRIMARY, SECONDARY, TERTIARY, ...)
**doc_type:** comma-separated (LOW_DOC, FULL_DOC, NEW_BIZ, ALL)
**loan_size_band:** comma-separated (MICRO, SMALL, MEDIUM, LARGE, XLARGE, ALL)
**answerable_questions:** natural-language questions this chunk should match on retrieval
**confidence:** high | medium | low
**last_verified:** YYYY-MM-DD
**policy_fields:** comma-separated atomic field codes (BASE_RATE, ASSET_AGE_MAX, ...)
**trigger_words:** comma-separated retrieval keyword hints

**Content:**

<markdown prose + tables — the actual facts a broker-facing answer is synthesized from>
```

`chunk_id` is the stable key used by ChromaDB — it must never change once assigned, or retrieval references to it silently break.

### 1.2 Ingestion — `src/ingest.py`

`parse_chunk_file(filepath, warnings)` splits a chunk file on `\n---\n`, regex-extracts every `**field:**` value, and validates `lenders`/`intent` against two hardcoded sets:

```python
VALID_LENDERS = {"WESTPAC", "BFS", "RESIMAC", "CFAL", "ANGLE", "FLEXI", "METRO"}
VALID_INTENTS = {"PRICING", "ELIGIBILITY", "LOAN_LIMITS", "DOCUMENTATION", "FEES",
                 "SETTLEMENT", "EXCLUSIONS", "SPECIAL_PROGRAMS", "ASSET_ELIGIBILITY",
                 "MEDICAL_PROGRAMS", "ROLLOVER_REPLACEMENT"}
```

A typo in either field doesn't error — it just silently breaks metadata-filtered retrieval for that one chunk, so this validation is the only thing standing between a typo and a chunk quietly becoming unreachable. Warnings are collected and printed, not raised, but a duplicate `chunk_id` across files is flagged too (ChromaDB's `id_` would otherwise let one silently overwrite the other).

For embedding, `ingest.py` builds an **enriched text** per chunk — `answerable_questions` and `trigger_words` are prepended to the actual content before embedding, so the embedding model directly associates those phrases with the chunk (`enriched_text = f"Questions this chunk answers: {answerable_questions}\nKey terms: {trigger_words}\n\n{chunk_content}"`).

`ingest_chunks()` then: loads `HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")`, deletes and recreates the ChromaDB collection `lifex_policies` (persistent client at `chroma_db/`), and builds a `VectorStoreIndex` from all 62 `Document` objects with a `SentenceSplitter(chunk_size=4096, chunk_overlap=100)` as a safety-net transform (not an active splitter — chunks are already hand-sized atomic units; 4096 is set well above the longest real chunk so nothing actually gets split into fragments that share a `chunk_id`).

Run via `python src/ingest.py` — this is a full rebuild, not incremental. Every content or metadata edit to any chunk file requires re-running this before it's live.

### 1.3 Query pipeline — `src/query.py`

Module-level setup on import: loads the embedding model, opens the existing ChromaDB collection, and constructs an `OpenAI` client (`_openai_client`). This means importing `src.query` is not free — it pays the embedding-model + ChromaDB load cost immediately.

**`detect_lenders(question) -> list[str]`**
Returns *every* lender a question names, not just the first match — this matters because "Compare Metro and Flexi" needs both lenders' chunks retrieved, not just one. Matching runs in tiers per lender:
1. Canonical name, word-boundary match (`"westpac"`, `"cfal"`, `"angle"`, ...)
2. Product/brand variant, word-boundary match (`"premiumplus"`, `"metroeco"`, `"flexicommercial"`, `"bfs plus"`, ...)
3. Only if *nothing* matched on tiers 1–2: single-edit-distance fuzzy match on canonical names ≥ 5 characters (catches "westpak", "rezimac"; short codes like BFS/CFAL are excluded from fuzzy matching since at 3–4 letters, edit-distance-1 collides with real English words)

Results from tiers 1–2 are **unioned across lenders**, not gated on the first match — an earlier version returned as soon as any lender matched tier 1, which silently suppressed a tier-2-only mention of a *different* lender in the same question. This was a confirmed, measured bug (worst-scoring category in the 111-question eval was specifically two-lender comparisons where one lender was named only by product name).

Returns `[]` if no lender is named at all — this triggers the fan-out path (see below).

**`retrieve_nodes(question, lenders, log) -> list[NodeWithScore]`**
This is a deliberately non-standard retrieval design. For each lender in scope (or **all 7** if `lenders` is empty), it retrieves up to `ALL_LENDER_CHUNKS_K = 20` chunks filtered by `{"lenders": {"$eq": lender_code}}`. Since each lender only actually has 8–10 chunks total, this means: **every chunk for a scoped lender is always included**, with embedding scores only ever affecting *order*, never *inclusion*.

Why: an earlier design used a tight `TOP_K` cutoff plus a cross-encoder reranker to try to squeeze the right 5 chunks into the prompt. Its failure mode was a correct chunk ranking one place past the cutoff — unrecoverable no matter how good the answering prompt was. Since a lender's whole chunk pool is cheap (~5–6k tokens), "retrieve everything, let order be cosmetic" makes a retrieval *miss* for a scoped lender structurally impossible, and removes the reranker (its load time, ~1GB RAM, and its own demote-the-correct-chunk failure mode) entirely.

For a **single** detected lender, chunks are returned as one flat, score-ordered list. For **multiple** lenders (a named comparison, or the 0-lender fan-out across all 7), chunks are grouped under per-lender headings in the prompt — a flat mixed list caused the model to silently skip lenders buried in the middle of a large mixed pile.

**`_resolve_followup(question, history) -> (standalone_question, wants_more_detail)`**
Uses `RESOLVER_MODEL = "gpt-4o-mini"` (deliberately *not* GPT-5 — GPT-5 family ignores `temperature`, so the same follow-up would resolve to a differently-worded standalone question on every call; for the *answerer* that variance is tolerable, but the resolver's output feeds lender detection, where a differently-worded rewrite can change which lenders get retrieved at all — 4o-mini at `temperature=0` is stable). Detects three follow-up shapes: pure reformatting ("say it shorter"), a genuine request for more detail (triggers a higher output-token cap and an explicit "go deeper" instruction), and a topic switch (treated as a brand-new question, grounded only in newly-retrieved chunks, never carrying over a number from the prior answer).

**`_chat_completion(model, prompt, max_output_tokens, json_mode=False, reasoning_effort=None)`**
The single place every OpenAI call goes through. Handles the fact that GPT-5-family models use a different calling convention than everything else:
- GPT-5 family: `max_completion_tokens` (not `max_tokens`), `reasoning_effort`, `verbosity="low"`, no `temperature` parameter at all
- Everything else (gpt-4o-mini): `max_tokens`, `temperature=0`

For GPT-5 calls, `max_completion_tokens` is set to `max_output_tokens + 512` — reasoning tokens count against this same budget, so without headroom beyond the visible answer, the model's own internal reasoning can consume the whole cap and leave nothing for the actual response. If that happens anyway (`finish_reason == "length"` and empty content), the cap is doubled and retried **once** (not in a loop — a runaway generation shouldn't escalate into an essay). Rate-limit errors are retried up to 8 times using the server's suggested `retry-after` value.

**`query_policies(question, verbose=True, history=None)`** — the main entry point:
1. Resolve follow-up if `history` is non-empty
2. `detect_lenders()` on the resolved question
3. `retrieve_nodes()` for those lenders
4. Build context (flat or per-lender-grouped, per §above)
5. Build the full prompt — persona ("friendly, experienced finance broker"), brevity/calculation-order rules, a large "double-check these common mistakes" guardrail block (see §2.2), and the lender-enumeration checklist if this is a multi-lender/fan-out question
6. Choose reasoning effort: `REASONING_EFFORT` ("low") if any lender was detected, `FANOUT_REASONING_EFFORT` ("minimal") if none was — this split is the single biggest latency/cost lever in the system (see §2.1)
7. Call `_chat_completion` with `LLM_MODEL = "gpt-5"`, return `{answer, sources}`

### 1.4 API layer — `src/api.py`

FastAPI wrapper. `/query` calls `query_policies`, catches any unhandled exception and returns **HTTP 503** with a generic-but-distinct message — without this, an OpenAI outage or a ChromaDB hiccup would surface to the frontend as a plain connection failure, indistinguishable from "the backend process isn't running at all" (a previously-diagnosed confusing failure mode). `/health` is a trivial liveness check used by the test scripts before they start firing questions.

### 1.5 Config — `src/config.py`

Single source of truth for every path and constant, all derived from `PROJECT_ROOT = Path(__file__).resolve().parent.parent` so the project resolves correctly regardless of where it's cloned. Key constants: `LLM_MODEL`, `RESOLVER_MODEL`, `REASONING_EFFORT`, `FANOUT_REASONING_EFFORT`, `EMBEDDING_MODEL`, `TOP_K`/`ALL_LENDER_CHUNKS_K`, `CHUNK_SIZE`/`CHUNK_OVERLAP`, `QUERY_CACHE_ENABLED` (currently `False` — see comment in file on why the similarity threshold was never recalibrated after the embedding-model swap), and the three question-bank paths described next.

### 1.6 Test infrastructure

| File | What it is |
|---|---|
| `tests/test_queries.py` | 41-question scenario bank (`policy_question_bank.xlsx`), one lender at a time. No auto-scoring by design — an earlier keyword-overlap scorer gave false confidence (scored a wrong lender's answer as "correct" because it happened to share words with the reference). Read the output yourself or hand it to an LLM to grade. |
| `tests/run_complex_questions.py` | 111-question adversarial bank (`ComplexQuestions.xlsx`) — cross-lender comparisons, multi-filter, contradiction detection, negative/trap constraints, calculation questions, ambiguous-needs-clarification, etc. Same no-auto-score philosophy. |
| `tests/grade_complex_questions.py` | Optional LLM-based grading of the 111-question results via `gpt-4o` — largely superseded this week by having Claude grade directly (zero extra OpenAI cost); see §2.4. |
| `tests/run_quick_regression.py` | **New this week.** A curated 14-question subset of the 111-question bank for cheap fix-verification — see §2.4. |

---

## 2. Changes made this week

### 2.1 Model and reasoning-effort tuning

**`LLM_MODEL = "gpt-5"`** was chosen after head-to-head benchmarking on 5 known-ground-truth questions: `gpt-4o-mini` made 3 factual errors with the full-corpus context, `gpt-5-mini` was correct but slow and verbose (2–14s, up to 4k-char answers), `gpt-5` was correct on everything, fastest of the GPT-5 family tested (2.4–7.4s), and the only one that reliably followed the verdict-first/brevity prompt instructions.

**`REASONING_EFFORT`: `"minimal"` → `"low"`.** Root cause: at `"minimal"` effort, on multi-step rate-calculation questions the model would state a headline number *before* it had actually worked out the correct table row, then correctly derive a *different* number in its own shown breakdown two lines later, and never reconcile the two (e.g. headline "9.64% p.a." while the shown working computes "12.64% + 2.00% = 14.64%"). Verified 3/3 that `"low"` eliminates this. Cost: real latency increase (~2–3×, roughly 2–3s → 6–8s per query).

**`FANOUT_REASONING_EFFORT = "minimal"`** (new constant). Raising global effort to `"low"` fixed the calculation bug but had a much larger cost on the *other* extreme: when no lender is named, retrieval fans out across all 7 lenders (up to ~140 chunk-slots vs ~8–20 for a single named lender), and `"low"` effort over that much context measured **20–56 seconds per question** — 3–8× worse than the single-lender case — for a question type (broad eligibility scans: "which lenders can do X", "best-fit across the panel") that's mostly yes/no verdicts, not the numeric rate build-ups `"low"` was raised to fix. The effort selection in `query_policies()` is now:

```python
effort = REASONING_EFFORT if lenders else FANOUT_REASONING_EFFORT
```

This is a **deterministic** split (keyed off the already-computed `lenders` list from `detect_lenders`), not a new fuzzy classifier — consistent with this project's established aversion to keyword/fuzzy branching for behavior decisions (the same principle behind the follow-up detector's "more detail" flag being an explicit code path, not a heuristic).

### 2.2 Prompt-engineering fixes (`src/query.py`)

The "double-check these common mistakes" guardrail block in the main prompt was extended with several rules found via the 111-question complex eval and this week's chunk audit:

- **Cross-lender contamination**, broadened from "a number belonging to one lender" to also cover **category-membership claims**: e.g. if lender A's excerpt says an asset type is fundable under a category and lender B's excerpt never says that, don't write B's line as if B's excerpt said it too — even if B has a similarly-named category. This was driven by a real bug: the model borrowed Flexi's/Resimac's "Buses/coaches are Primary assets" phrasing and applied it to Angle, where Angle's *only* mention of buses anywhere is an exclusion, not a category statement.
- **Adjacent-attribute comparison**: when comparing one named attribute across lenders (e.g. "max age for a primary asset"), and the same excerpt also lists the equivalent figure for closely-related categories (secondary/tertiary) that weren't asked about, check those too before concluding the lenders "match."
- **Calculation-order guardrail**: for any question needing a build-up (a rate calc, a fee stack), work the breakdown out first and put the total *last* — a wrong headline followed by correct-looking working is judged worse than no headline at all.
- **Lender-enumeration checklist**: for "which lenders can do X" questions, the prompt now names the exact lenders present in the retrieved excerpts as an explicit checklist, rather than a generic "go through every lender" instruction — the generic version still let the model quietly stop after 3–5 of 7 lenders even with excerpts grouped by lender.

### 2.3 Chunk-content fixes (11 total, across 4 lenders)

A full audit dispatched 7 parallel agents (one per lender) to cross-verify all 62 chunks against their source PDFs directly — not against each other, against the actual PDF text/tables. Confirmed genuine transcription errors (not stylistic differences), fixed and re-verified against the source PDF a second time before trusting each fix:

| Lender | Fix |
|---|---|
| **Angle** | `angle_interest_rates` standard rate-card table was scrambled — mixed Property-Owner/Non-Property-Owner rates across the wrong asset-class rows. Root cause: `angle-finance-rate-card.pdf` is a multi-column design where naive linear text extraction reads cells out of order (confirmed via `pdftotext -layout` producing garbled output like "9 10. 5%"). Fixed via word-coordinate table reconstruction (cluster words into rows by y-position, columns by x-position) instead of trusting extraction order. |
| **Angle** | `angle_doc_types` Low Doc $100k–$250k credit score collapsed "Corporate 550+ / Individual 600+" into a single "600+" — fixed via word-coordinate positions on the source PDF page. |
| **Angle** | `angle_doc_types` Full Doc minimum-requirements checkmark grid had 4 wrong cells — checkmarks are vector-drawn shapes, not extractable text, so this required rendering the page to PNG and reading the grid visually. |
| **Angle** | `angle_start_up` bank-balance window stated "last 3 months"; source says "3–6 months". |
| **BFS** | `bfs_exclusions` falsely stated "BFS Plus: no commercial contracts" — contradicted by the source PDF's own table and by `bfs_commercial_rates` (which lists a BFS Plus commercial max rate in the same file). |
| **BFS** | `bfs_commercial_rates`/`bfs_consumer_rates`: Ultra Prime rate wrongly shown as "N/A" for "Used 2017–2021" — it's a merged cell continuing the same 7.60% (commercial) / 9.15% (consumer) rate from the rows above, confirmed via PDF word-coordinate + rendered-page cross-check. |
| **BFS** | `bfs_commercial_rates` "17.15% cap across all tiers" mischaracterized — 17.15% is BFS Plus's own flat maximum rate; PRIME-tier pricing with margin + loadings is not actually capped there. |
| **CFAL** | `cfal_replacement_policy` heavy-equipment Category B age limit wrongly stated as 7 years (source: 5 years general, 3 years for cranes specifically) — the real 7-year limit belongs to an entire agricultural-equipment list (tractors, headers, harvesters, ..., windrowers) that was missing from the chunk entirely. |
| **Westpac** | `westpac_medical`: motor vehicle + office equipment are one **merged cap per column** ($250k specialist / $150k allied health), not 4 separate figures as the chunk stated; the allied-health "medical equipment" figure the chunk invented doesn't exist as a separate line in the source. |
| **Westpac** | `westpac_settlement`/`westpac_exclusions`/`westpac_drivexpress`: several items had no basis in any of the 4 Westpac source PDFs at all — a "mid-term refinancing" exclusion, a "repairable write-offs" exclusion, an entire geographic Remote/Very-Remote exclusions section, a "90-day bank statements for Plus applications" requirement (Westpac has no "Plus" product in these docs — this was templated from BFS's own chunk), and an ASIC-search requirement added to DriveXpress where the source only requires it for Rollover/Replacement. All removed. |
| **Westpac** | `westpac_replacement`: Category B under Replacement actually differs from DriveXpress's Category B (adds tippers/dump trucks, folds in the agricultural list at a 7-year ceiling with windrowers, vs DriveXpress's own Category B/C split) — the chunk's "same as DriveXpress" framing undersold this and was rewritten to spell out the difference explicitly. |

**Technique used throughout**: since `pdftoppm`/poppler isn't installed on this machine (the standard PDF-page-rendering path fails), verification used PyMuPDF (`fitz`) directly via two methods — `page.get_text('words')` for coordinate-based table reconstruction where linear extraction order is unreliable, and `page.get_pixmap(...).save(path)` to render a page to PNG for visual inspection where content (like checkmarks) isn't text at all.

### 2.4 Cost investigation and the quick-regression script

Investigated why OpenAI spend had grown faster than expected. Findings, with real measured numbers:

- **Full-corpus retrieval is the dominant per-call cost multiplier.** A fan-out question (no lender named) sends effectively the *entire* 62-chunk corpus (~1.2M tokens measured across a real run of the 111-question bank, averaging ~11,000 tokens/call, with the worst single fan-out question at 32,705 tokens) — roughly 10× the cost of a single-lender question (~4,800–6,000 tokens).
- **The 111-question suite had been run in full at least 9 times** over the project's history (`complex_results.json` through `..._run9_final.json`), and 6 of those runs were graded with a second paid model (`gpt-4o`) before switching to Claude-based grading (zero additional OpenAI cost).
- Estimated cost of one full 111-question run: **~$2.30–$3.40** (measured input tokens × $1.25/M, plus estimated output/reasoning tokens at $10/M — the reasoning-token component is inherently an estimate, since it isn't directly observable without OpenAI's own usage dashboard).
- Built **`tests/run_quick_regression.py`**: a curated 14-question subset covering all 11 complexity types in the bank, all 7 lenders, 3 fan-out questions, and every question that has previously caught a real regression in this project (rate-table ambiguity, headline/breakdown calculation mismatch, cross-lender bus-coverage contamination, adjacent-attribute comparison, exact-cap edge case, fan-out latency). Supports `--lender <NAME>` (every question touching one lender) and `--ids CQ-x,CQ-y` (an explicit custom list). Cuts the cost of a routine fix-verification pass by roughly 85% relative to the full suite.
- Investigated **GPT-5.6 Luna** (OpenAI's newest, cheapest tier, released 2026-07-09 — after this assistant's knowledge cutoff, confirmed via live web search) as a potential cheaper replacement for `gpt-5`. Real pricing: Luna $1.00/$6.00 per M input/output vs `gpt-5`'s $1.25/$10.00 — genuinely cheaper, especially on output/reasoning tokens. **Not adopted** — Luna is explicitly OpenAI's least-capable tier in that family, and the specific bug that justified raising `REASONING_EFFORT` to `"low"` was a model-quality issue, not a pricing issue; switching model tiers without re-running the same empirical check that caught that bug in the first place would be reintroducing an already-fixed failure mode on faith.

---

## 3. Automated chunk-extraction pipeline — design, build, and rollback

### 3.1 The problem

All 62 chunks are hand-typed from PDFs — every one of the 11 bugs in §2.3 was a **transcription error**: a human (or, if automated the wrong way, an LLM) misread a PDF table or a checkmark grid and copied the wrong value. The rate-card bug in particular traces to a specific, fixable root cause: `angle-finance-rate-card.pdf`'s multi-column layout makes naive linear text extraction come out in the wrong order — the exact same extraction technique that produced the bug is also what a human would see if they ran `pdftotext` on it and typed up what they saw.

### 3.2 Design: "verified extraction"

The core constraint: **numbers must never pass through free-form transcription** — not by a human, and not by an LLM reading raw PDF text and writing a chunk about it. Two, and only two, roles for an LLM in the whole pipeline:

1. **Vision transcription** — narrowly scoped ("transcribe exactly what this image shows as JSON", never "read this and write a policy chunk") and reserved *only* for pages with no reliable text layer at all (checkmark grids drawn as vector shapes, fully scanned pages). Always flagged `confidence: "needs_review"`, blocked from promotion until a human checks it against the saved render.
2. **Chunk assembly** — takes ONLY already-verified fact records (never raw PDF text) and drafts the chunk `.md` format around them. Guarded twice: a prompt instruction forbidding invented/rounded numbers, and a **code-level** guardrail that regex-extracts every numeric token from the drafted content and rejects the draft outright if any number doesn't trace back to a supplied fact.

Everything else — deciding whether a PDF page needs table reconstruction at all, and doing that reconstruction — is deterministic code, zero LLM cost:

- **Page classifier** (`classify_page`): 3 signals computed from `fitz` primitives — `char_count` (near-zero ⇒ fully scanned), `char_count` low relative to visible graphic content (⇒ a checkmark-style visual grid; raw drawing *count* doesn't work as a signal on a heavily-styled PDF template, since even plain-text pages have hundreds of decorative vector shapes — text *density* is what actually discriminates), and **`order_disagreement`** — for each visually-clustered row, do the words' natural extraction order and left-to-right spatial order agree? Calibrated per-row rather than whole-page, because whole-page comparison picked up harmless cross-section stream-order jumps (a sidebar or footer stored out of visual sequence, which never confuses a reader) and scored *higher* on known-simple pages than on the actually-scrambled one.
- **Table reconstruction**: cluster words into rows by y-position, derive column boundaries from the *data* rows' x-positions (not the header — a wordy multi-word header phrase like "10 years (EOT)" has near-identical internal word-wrap spacing to genuine inter-column gaps, while single-token data cells have much cleaner, larger gaps), assign each row's words to nearest column. Sanity-checks column count and expected numeric shape per cell; failing either escalates the *table* to vision review rather than silently emitting a wrong grid.
- **Fact store**: every extraction method (reconstruction or vision) writes into one JSON schema with a page/coordinate citation and a `fact_id` — this is the audit trail the hand-written chunks never had ("why does this say 8.39%" becomes a citation, not "an analyst typed it").

### 3.3 What was built

| File | Role |
|---|---|
| `src/pdf_extract.py` | Deterministic layer — page classifier, table reconstruction, fact-store schema. Zero OpenAI cost, fully unit-testable offline. |
| `src/chunk_assembler.py` | LLM layer — vision transcription + chunk assembly, with the numeric-token cross-check guardrail. |
| `scripts/auto_chunk.py` | CLI: `extract` (run classifier + reconstruction for a lender's registered table specs) / `assemble` (LLM drafting step) / `diff` (fact-level comparison against the live chunk) / `promote` (merge into `data/chunks/`). |
| `tests/test_pdf_extract.py` | Golden-set regression tests, run before any LLM spend. |

### 3.4 Validation

Piloted on the exact table that had the known scrambled-table bug (Angle's standard rate card): **reproduced it cell-for-cell** against the hand-verified ground truth, including correctly flagging the one thing it genuinely can't recover from text — Property Owner vs Non-Property Owner is distinguished only by a house *icon* on this PDF, with no text label at all, so that distinction is applied from a stated convention and explicitly marked `confidence: "assumed_from_convention"` rather than presented as read off the page.

Expanded to cover the whole `angle_interest_rates` chunk (profile-based headline rates, Prime Movers rate, Start-Up rates, no-rate-loading conditions) by adding "prose region" extraction (a narrative/bulleted counterpart to table reconstruction, same reading-order guarantee). Result: **91% numeric overlap with the live chunk, zero invented or incorrect numbers.** The remaining 9% was fully explained — a document version string/date (not a policy fact) and one note living on a different PDF page that wasn't in scope for this pass.

### 3.5 The incident, and why it's rolled back

The first version of `promote` did a full-file `shutil.copyfile(draft, live)`. Run once for real, since the draft only ever covered 1 of Angle's 10 chunks, this **deleted the other 9 chunks** from `data/chunks/angle_chunks.md`.

Caught immediately. Recovered via `git show HEAD:data/chunks/angle_chunks.md` (the last commit, which predates every chunk fix made this session) plus the exact corrected content for the 5 already-fixed chunks, still present verbatim in conversation context from earlier reads this session. Reconstructed the full 10-chunk file, verified it parses cleanly with zero warnings, and confirmed via `diff` that the restored `angle_interest_rates` still matches the pipeline's validated output exactly. Then fixed the actual bug — `promote` now does exact/fuzzy chunk-id alignment (the same alignment `diff` uses) and splices in only the matched section(s), verified on temp copies (never against the real files again) to change exactly the intended chunk and leave every other chunk byte-identical.

**Decision: shelved, not because it doesn't work — because of the remaining scope.** Table/prose specs exist for 1 of Angle's 10 chunks; 0 of the other 6 lenders' 52 chunks have any registered at all. Turning "proven correct on one table" into "the whole corpus is automated" means repeating register-specs → extract → assemble → diff roughly 60 more times, each needing the same page-by-page verification discipline used here. Given that cost, the call was made to stop here for now.

**Everything was fully removed afterward**: `src/pdf_extract.py`, `src/chunk_assembler.py`, `scripts/auto_chunk.py`, `tests/test_pdf_extract.py`, the `data/extracted_facts/` and `data/chunks_draft/` directories, and the `EXTRACTED_FACTS_DIR`/`CHUNKS_DRAFT_DIR`/`VISION_MODEL` constants added to `src/config.py`. Verified afterward: all 7 lender chunk files show zero automation artifacts, all 62 chunks parse cleanly, and all 11 manual fixes from §2.3 remain intact.

### 3.6 If this gets picked back up

The design in §3.2 doesn't need to be rethought — it was validated, not disproven. What's missing is coverage: a `TABLE_SPECS` entry (which PDF, which page, which region, which extraction kind) has to be hand-registered per table, the same way this session's manual audit located each one by hand. The pragmatic rollout order, if resumed: finish the rest of `angle_interest_rates`'s own page (one more note, on page 3), then the other 9 Angle chunks, then CFAL/Flexi (simplest, single-page fact sheets — lowest new-bug surface), then Westpac/BFS (a second real test of table reconstruction on multi-column rate cards), then Metro (exercises the vision/scanned path, since it has the project's one fully-scanned PDF), then Resimac last.
