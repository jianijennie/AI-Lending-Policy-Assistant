# LifeX Policy Assistant — Technical Documentation

**Current state of the system as at 2026-08-18.** This supersedes
`Week4_Technical_Documentation.md`, which stays in place as the historical record of
that week's work — this document describes how the system behaves *now*.

Written to be read before a Q&A, so it explains **why** each decision was made, not just
what the code does. Section 11 is a prepared answer bank for likely judge questions.

---

## 1. The system in one paragraph

A broker asks a question in plain English. The system works out which of the 7 lenders
the question concerns, pulls **every** policy chunk belonging to those lenders out of a
vector database, and hands that material to GPT-5.5 with instructions to answer only from
what it was given. Before generating anything it checks two stores of previous answers —
one of human-reviewed corrections, one of prior AI answers — and serves a stored answer if
one genuinely matches. Answers are grounded in 63 hand-curated policy chunks extracted
from 25 lender PDFs; the model is never asked to recall lending policy from its own
training.

**The one-sentence version for a judge:** *"It's retrieval-augmented generation over a
hand-curated policy corpus, with a two-layer answer cache and a human correction loop —
the model only ever reasons over policy text we put in front of it."*

---

## 2. Architecture at a glance

```
25 lender PDFs
      │  (manual, verified extraction — see §3)
      ▼
data/chunks/*.md ──ingest──► ChromaDB "lifex_policies" (63 chunks, bge-base embeddings)
                                        │
Broker question ────────────────────────┤
      │                                 │
      ├─ 1. Correction check   (only if mid-conversation)
      ├─ 2. Answer library     (only if a fresh question)   ── human-reviewed
      ├─ 3. Query cache        (only if a fresh question)   ── unreviewed
      └─ 4. Retrieve + generate  ── GPT-5.5, grounded in retrieved chunks
                                        │
                                        └──► answer + source chunk list
```

| Layer | File | Role |
|---|---|---|
| Data | `data/chunks/*.md` | 7 files, one per lender, 63 chunks total |
| Ingest | `src/ingest.py` | Parses chunks, embeds, rebuilds the vector DB |
| Retrieval + generation | `src/query.py` | Lender detection, retrieval, prompting, all classifiers |
| API | `src/api.py` | FastAPI endpoints, both caches, concurrency locks |
| Config | `src/config.py` | Every tunable, each with the reasoning behind its value |
| Frontend | `CMAP_PolicyAssistant_v7_2.html` | Single self-contained file, no build step |

**Models in use:**

| Model | Used for | Why this one |
|---|---|---|
| `BAAI/bge-base-en-v1.5` | embeddings | Runs locally, no API cost; upgraded from bge-small for better recall |
| `gpt-5.5` | writing the answer | Benchmarked head-to-head; see §10.3 |
| `gpt-4o-mini` | 5 narrow classifiers | Supports `temperature=0`, so its decisions are stable run to run |

---

## 3. Data layer — why chunks are hand-curated

Each lender has one markdown file. A chunk is an atomic policy unit with a stable
`chunk_id`, structured metadata (lender, intent, asset class, doc type, trigger words),
and the actual policy content as prose and tables.

**Why hand-curated rather than automated PDF extraction?** An automated extraction
pipeline was built, piloted, and **rolled back** in Week 4 — it silently corrupted figures
during extraction. For a system whose entire purpose is quoting exact financial figures, a
silent corruption is the worst possible failure, so extraction stayed manual and verified.
This is a deliberate trade of scalability for correctness.

**Chunks carry their own provenance and known conflicts.** Where two lender documents
disagree, the chunk records both figures and instructs that the conflict be surfaced rather
than silently resolved — e.g. Metro's EV price cap is $91,661 on the rate sheet and
$91,387 in the MetroEco booklet. The correct answer flags both.

`chunk_id` must never change once assigned — it is the key ChromaDB and every saved answer
references.

---

## 4. Retrieval — we deliberately do *not* use top-k

This is the single most counter-intuitive design decision and a likely judge question.

**Standard RAG** embeds the question, retrieves the top *k* most similar chunks (typically
5), and passes those to the model. **We don't do that.** Once the lenders are identified,
we retrieve **every chunk belonging to those lenders** (`ALL_LENDER_CHUNKS_K = 20` per
lender, above any lender's actual chunk count).

**Why:** each lender has only ~8–10 chunks (~5–6k tokens). The entire pool fits in the
prompt at negligible cost. Under top-k, a correct chunk ranked one position past the cutoff
is simply *never seen* by the model, and no amount of prompt engineering can recover it —
the failure is invisible and unfixable. By retrieving everything for the relevant lenders,
**a retrieval miss becomes structurally impossible**; embedding similarity now only decides
the *order* chunks appear in, never whether they appear at all.

This also let us delete the cross-encoder reranker entirely — its load time, ~1GB of RAM,
and its own known failure mode of demoting correct chunks. It existed only to fix ranking
near the top-k cutoff, and there is no cutoff any more.

**Lender detection** (`detect_lenders`) matches in tiers: canonical name → product/brand
variant (`premiumplus`, `flexicommercial`, `metroeco`) → single-typo fuzzy match as a last
resort. Results are **unioned**, not gated on first match — an earlier version returned as
soon as one lender matched, which silently dropped a second lender mentioned only by
product name. That was the single largest source of failures in the 111-question eval.

**If no lender is named**, the question fans out across all 7 lenders (~63 chunks). This is
the expensive path and is handled specially — see §7.

---

## 5. The four answer paths

Every request goes through `_query_impl` in `src/api.py`, which tries paths in a **fixed
order**. Understanding this order is essential.

```
1. CORRECTION      — only when mid-conversation. Is the broker correcting us?
2. ANSWER LIBRARY  — only for a fresh question. Human-reviewed answer on file?
3. QUERY CACHE     — only for a fresh question. Previous AI answer on file?
4. GENERATE        — retrieve chunks, ask GPT-5.5, then cache the result
```

Two rules explain most of the behaviour:

- **The correction check only runs when there IS conversation history.** A correction is
  a reply to something — it can't be the first message.
- **Both caches are skipped entirely when there IS history.** A follow-up like *"and for a
  used one?"* only means something inside its own conversation; matching it against a
  stranger's cached standalone question would return something that doesn't address it.
  For the same reason, a follow-up's answer is **never written to the cache** — it was
  written for a context the next asker won't have.

`answer_source` in the API response tells you which path produced the answer:
`generated`, `cache`, `library`, or `correction_saved`.

---

## 6. The two caches — how they differ and why there are two

This trips people up, so: **there are two server-side stores, and they are not the same
thing.** (The frontend also keeps its own small local list for its Review tab — that's a
third, separate thing and is not authoritative.)

| | **Query cache** | **Answer library** |
|---|---|---|
| File | `data/query_cache.json` | `data/answer_library.json` |
| Contains | Raw AI answers, unreviewed | Human-reviewed or human-corrected answers |
| Written by | Automatically, on every fresh answer | Broker correction in chat, or approval in the Review tab |
| Trust level | Same as any AI answer | Higher — a person signed off |
| Checked | **Second** | **First** |
| Purpose | Speed and cost | Correctness — a human fixed something |

**Why the library is checked first:** if a broker has explicitly corrected an answer, that
correction must beat an older unreviewed cached answer for the same question. If the order
were reversed, a correction could be silently shadowed by the very answer it was meant to
replace. This ordering is now covered by two regression scenarios (COMBO-1, COMBO-7).

### 6.1 How a cache match is decided — the two-stage gate

Both stores use the **same** two-stage matching, and the reason is a real measurement, not
a preference.

**Stage 1 — embedding similarity as a cheap pre-filter** (threshold 0.75). Narrows the
whole store to a handful of plausible candidates, best first.

**Stage 2 — a direct LLM comparison** (`questions_require_same_answer`) on up to 3
candidates. This is the actual yes/no decision.

**Why not just use a similarity threshold?** Because we measured it and it doesn't work for
this domain. Genuine paraphrases and dangerous near-misses **overlap in score**:

- *"BFS Tier 2's minimum credit score"* vs *"BFS **Tier 3's** minimum credit score"* →
  **0.93** similarity, but completely different correct answers
- Genuine paraphrases scored as low as **0.78**

No single threshold separates those. A value high enough to exclude the near-miss would
reject nearly every real paraphrase. So similarity is used only for the job it's reliable
at — excluding the obviously unrelated — and a model that can actually read both questions
makes the call.

The gate is deliberately **conservative**: a missed cache hit costs a few seconds and a
fraction of a cent; a wrongly-served cached answer hands a broker a confidently wrong
financial figure with nothing to flag it. It also returns "no match" on any internal error,
so a failure can never *open* the gate.

### 6.2 Deduplication

`_append_to_query_cache` now **purges any gate-equivalent entry before appending**, so
there is exactly one entry per distinct question — always the newest.

Without this, repeated evaluation runs accumulated several entries for the same question
with no recency signal, and ranking picked between them essentially at random. This was not
theoretical: three entries existed for one question, one of them a stale wrong answer from
before a rate update, and it was being served roughly a third of the time.

> **Known open issue:** the answer library does **not** yet have this dedup. Correcting the
> same question twice leaves two entries and serves the *first* correction, because
> `find_best_match` returns the highest-*similarity* entry rather than the newest. This is
> confirmed and reproducible (scenario COMBO-6, deliberately left failing). Fix is the same
> pattern already applied to the query cache.

### 6.3 Operational note

The cache was **cleared on 2026-08-18** because it held answers generated *before* that
day's reasoning fix — every pre-fix entry was stale by construction. It is safe to clear at
any time: it is purely regenerable, and the only cost is that the next ask of each question
pays full latency once. Consider pre-warming it from the question bank before a demo.

---

## 7. Reasoning-effort routing — the speed/accuracy dial

GPT-5 family models take a `reasoning_effort` parameter. We use two settings:

| Situation | Effort | Rationale |
|---|---|---|
| A lender was named | `low` | Raised from `minimal` after a reproducible bug: on rate build-ups the model stated a headline figure before working out the right table row, then derived a *different* number in its own shown working and never reconciled the two |
| No lender named (fan-out) | `none` **or** `low`, decided per question | `low` over ~63 chunks is materially slower, so a classifier decides whether this particular question actually needs it |

**The classifier was broadened on 2026-08-18 after it caused a wrong answer.** It
originally split on *"does this rank a number across lenders?"* versus *"is it a simple
yes/no eligibility scan?"* — and sent eligibility scans down the cheap path.

The failure: *"Carpenter registered ABN and GST last week, wants a ute, which lender can he
choose?"* reads as an eligibility scan → ran at `none` → recommended **Angle** (whose
Start-Up product requires 3 months' trading, which the client fails) while dismissing
**BFS** (whose New Business Ventures pathway explicitly covers *"less than 12 months ABN"*,
which the client meets). The answer even quoted BFS's requirement and then concluded the
opposite.

Diagnosed by elimination: retrieval was fine (the BFS chunk *was* retrieved), and scoped to
a single lender the model got **both** lenders right. A controlled A/B with identical
retrieval and effort as the only variable settled it — `none` answered Angle, `low`
answered BFS correctly.

**The axis was wrong.** It was never ranking-versus-eligibility; it's *whether a specific
customer figure has to be tested against each lender's own threshold*. Deciding which side
of a threshold "last week" falls on is as demanding as picking a cheapest rate. Pure
category lookups (*"which lenders finance trucks"*) still take the cheap path, preserving
the latency win.

---

## 8. Conversation handling

### 8.1 Follow-ups

`_resolve_followup` rewrites a follow-up into a standalone question using the last 3 turns,
and separately flags whether the broker is asking for *more detail* (as opposed to asking
something new). Everything downstream — lender detection, retrieval — then treats it like a
fresh question.

The detail flag matters because "keep it brief" and "give me more detail" are direct
opposites; with both in the prompt, brevity wins and the answer comes back as a reworded
copy. So the brevity instruction is switched **off in code** for that one turn.

### 8.2 Corrections

`detect_and_apply_correction` decides whether the broker is correcting us and, if so,
produces the corrected answer for immediate saving. Per project decision, chat corrections
go live **immediately** — unlike Review-tab answers, which wait for approval.

Two safeguards worth knowing:

- **It must quote a specific replacement value from the broker's own message.** Pure
  skepticism — *"are you sure?"*, *"that doesn't sound right"* — saves nothing. This is
  load-bearing: an earlier version that just asked for a true/false verdict **invented**
  replacement figures for skeptical messages. Requiring a quote suppressed that.
- **When correcting a follow-up, the previous turn is re-resolved first.** Otherwise
  correcting the answer to *"what about CFAL?"* would save the literal string *"what about
  CFAL?"* as the question and attach the *previous* lender's chunk ids — the correction
  would be unfindable and point at the wrong sources.

Verified 2026-08-18: a correction propagates into **later reasoning in the same
conversation**, not just into a repeat of the same question.

---

## 9. Other behaviours worth knowing

**Conversational messages skip retrieval.** *"Are you online?"*, *"hi"*, *"what can you
help with?"* previously fanned out across all 7 lenders, returning a meaningless 60+ source
list tagged with whichever lender happened to score highest. A narrow check now short-
circuits these with a direct reply and **zero sources**. It only runs when no lender was
detected, and deliberately fails toward "this is a real question" — a vague-but-genuine
question like *"best rate?"* still goes through the full pipeline.

**The source display collapses.** The frontend shows `N lenders · M sources` with a
per-lender expandable list, instead of every chunk id concatenated into one unreadable
string.

**Concurrency.** `/query` takes a read lock; `/chunks/promote` takes a write lock while
rebuilding the index, so a query can never read a half-rebuilt collection. Cache and
library writes are atomic (temp file + `os.replace`), so a concurrent reader never sees a
half-written file.

**Answer staleness — both stores, handled differently.** A chunk change has to reach every
answer already built on the old content, and the two stores get opposite treatment because
they're worth different amounts:

- **Answer library:** entries snapshot the chunk content they were based on, so
  `refresh_stale_entries` re-checks each affected one and either auto-updates it or flags it
  `needs_review`. Flagged entries are **never served automatically**. These are human
  corrections, so the effort to preserve them is justified.
- **Query cache:** entries citing a changed chunk are **deleted outright**
  (`_invalidate_query_cache_for_chunks`). Cache entries record their source chunk_ids, so
  this is precise rather than a blanket wipe. They're unreviewed LLM output, so there's
  nothing to salvage and regenerating costs one question's latency.

`/chunks/promote` does both and reports the counts. `/answer-library/refresh` (the manual
path, used after editing chunks by hand) refreshes the library the same way but **clears the
cache entirely** — nothing recorded which chunks moved, and cache entries don't snapshot
content, so there's no way to tell which are stale.

> **Operational note:** running `python src/ingest.py` while the backend is up deletes and
> recreates the Chroma collection out from under the running process, which then 500s until
> restarted. `/chunks/promote` avoids this by re-ingesting in-process and calling
> `reload_index()`. If you re-ingest by hand, restart the backend afterwards.

---

## 10. Evaluation

### 10.1 Test suites

| Suite | What it covers |
|---|---|
| `tests/run_quick_regression.py` | 14-question smoke test — every complexity type, every lender |
| `tests/run_complex_questions.py` | Full 125-question adversarial bank |
| `tests/run_full_eval.py` | 43 questions + follow-ups, corrections, cache, library |
| `tests/run_combination_eval.py` | 12 scenarios testing how those mechanisms **interact** |
| `tests/run_finals_practice.py` | 15 competition-style cases (see `Finals_Practice_Cases.md`) |

**Nothing is auto-scored on answer quality.** An earlier version scored by keyword overlap
against a gold answer, which gave false confidence — it marked a *wrong lender's* answer
correct because it shared enough words. Answers are graded by a human or an LLM judge with
the reference in front of it. The automated assertions only check mechanically verifiable
facts: which path served the answer, which lender's chunks were retrieved, whether a saved
answer was reproduced verbatim.

### 10.2 Current results

- **Finals practice cases: 15/15** correct (one with a minor caveat)
- **Combination eval: 8/12** — 1 real confirmed bug (the library dedup issue in §6.2),
  3 were flaws in the test assertions themselves, since corrected
- **Quick regression: 14/14**

### 10.3 Model selection

`gpt-5.5` was benchmarked against `gpt-5.6-terra` (cheaper, faster) on 11 questions drawn
from this project's own failure history. Terra was faster on **all 11** (avg 6.5s vs 8.7s,
−25%) — but on *"which lender is cheapest"* it quoted Flexi's **standard** rate instead of
the **flexipremium** rate and therefore named the wrong cheapest lender, on **2 of 4** runs.
gpt-5.5 got it right 4/4. It also added unverified qualifiers ("assuming brokerage is 5.5%
or less") that appear nowhere in the source.

**Decision: stay on gpt-5.5.** A coin-flip on the cheapest-rate question is disqualifying
regardless of speed, and rate accuracy is what the competition emphasises.

### 10.4 Reference data goes stale — a real lesson

The 111-question reference bank was frozen around 2026-07-22, but the policy chunks were
corrected three times afterwards. By 2026-08-18, **9 reference answers were wrong** while
the system was right — Flexi's rate dropped 7.30%→7.15%, Metro's rate sheet changed, and a
CFAL rule turned out to belong to a different lender entirely.

**Practical rule: when the system disagrees with a reference answer, check the chunk file
before assuming the system is wrong.**

---

## 11. Likely judge questions — prepared answers

**"How do you stop it hallucinating figures?"**
Three layers. The model only sees policy text we retrieved and is instructed to ground
every figure in it. Retrieval can't miss relevant chunks because we pass the lender's
entire chunk set, not a top-k slice. And every answer returns the exact chunk ids it drew
on, so any figure is traceable back to a source document. It's also explicitly instructed
that if the excerpts don't contain a figure, it should say so rather than produce one.

**"Why not fine-tune a model on the policies?"**
Policies change. A rate card update would need retraining, and a fine-tuned model gives no
way to tell whether an answer came from current policy or a memorised old version. With
retrieval, updating a policy is editing a markdown file and re-running ingest — and the
answer cites which chunk it used.

**"What happens when a lender changes a rate? Don't the old answers stick around?"**
Both stores are handled, and differently on purpose. Saved *corrections* are re-checked
one by one: each snapshotted the chunk text it was based on, so a narrow LLM call decides
whether it still holds, and it's either updated or flagged `needs_review` (flagged entries
are never served). *Cached* answers that cited a changed chunk are simply **dropped** —
they're unreviewed, so there's nothing worth preserving and regenerating costs one
question. Promoting through the UI does both automatically and reports the counts. The
Metro and Flexi rate changes in §10.4 went through exactly this path.

**"What if two source documents disagree?"**
It surfaces both and says to confirm, rather than silently picking one. Metro's EV cap
appears as $91,661 on the rate sheet and $91,387 in the booklet; Angle's Start-Up minimum
credit score is 550 on the flyer and 500 on the rate card. Both are handled this way, and
both are tested.

**"How accurate is it?"**
15/15 on competition-style practice cases, 14/14 on the regression suite. But the more
useful answer is that we track *specific failure modes* rather than a single accuracy
number — the test bank is built around traps this system has actually failed before.

**"How do you know it isn't just memorising the test set?"**
The reference answers were verified against source chunks independently of what the system
outputs — and when they disagreed, the *references* turned out wrong 9 times. We also
routinely find and fix errors the test bank didn't contain.

**"Why does it sometimes take 15–20 seconds?"**
Only when no lender is named, so it reads all 7 lenders' policies (~63 chunks) and does
careful step-by-step reasoning. Naming a lender takes it to ~3–7s. It's a deliberate
trade: that slow path is where the hardest questions live, and rushing it produced wrong
answers (§7).

**"What's the cost per question?"**
Roughly $0.01–$0.05 for a generated answer; cached and library answers are effectively
free. Embeddings run locally at no API cost.

**"What's the weakest part?"**
Chunk curation is manual, so adding a lender is real work — that's a deliberate trade after
the automated pipeline silently corrupted figures. The correction-matching gate is
deliberately conservative, so it sometimes misses a genuine paraphrase and answers fresh
instead. And there's a known duplicate-correction bug in the answer library (§6.2) that's
documented and reproducible rather than unknown.

---

## 12. Operating it live — see also

For driving the assistant in front of an audience (what to expect by question
shape, how to trigger follow-ups and corrections, what to do when something
breaks, and a Q&A answer bank), see **`Demo_Operator_Guide.md`**. It covers the
operational details this document deliberately leaves out.

Two mechanics from it are worth repeating here, because they surprise people:

- **A correction only saves when the message states the replacement value.**
  "That's wrong, it's actually 7.15%" saves; "are you sure?" deliberately does
  not, because the system will not invent a figure from vague doubt (§8.2).
- **The Reset cache control does not clear corrections.** It empties the query
  cache only. Corrections are human work that nothing else can reconstruct, so
  they are protected from an accidental wipe (§6).

---

## 13. Running it

```bash
python src/ingest.py                          # rebuild the vector DB after any chunk edit
uvicorn src.api:app --port 8000               # start the backend
python tests/run_quick_regression.py          # 14-question smoke test
python tests/run_finals_practice.py           # competition-style cases
python scripts/build_finals_report.py         # regenerate the shareable results page
```

Frontend: open `CMAP_PolicyAssistant_v7_2.html` — no build step. Point `API_BASE` at the
ngrok URL for a shared demo, or `127.0.0.1:8000` for local.

**Before a demo:** confirm `/health` returns 7 lenders and 63 chunks, and consider
pre-warming the query cache so the first questions aren't slow.
