# Open Issues & Confusions — For Jiani

Compiled 2026-07-29 after a full audit of our RAG chunk system (`data/chunks/*.md`) against
every source PDF in `data/documents/`, plus a cross-check of the 5 new reference documents
you uploaded to `policies/` (Angle, BFS, Metro, Resimac, Westpac/CFAL Exceptions Catalog).

Two kinds of items below:
- **A. Unresolved in our own chunks** — things we can't verify one way or the other because we
  don't have the source material. If you have access to the documents these would come from,
  this is exactly where we need help.
- **B. Issues found in your new reference documents** — real, cross-checked corrections for
  the files you uploaded to `policies/`. Your core policy facts (rates, thresholds, eligibility
  rules) were accurate everywhere we checked — these are specifically the interpretive/
  cross-reference layer, not the underlying numbers.

---

## A. Unresolved in our own chunks (need source material)

### CFAL — RESOLVED 2026-07-31, thanks to your `policies/rectification for chunking/Part A.md`

All four CFAL items previously listed here have been traced and fixed:

1. ~~"Repairable write-offs" exclusion~~ — confirmed as **Resimac** policy (Commercial Product Guide, p.7), not CFAL. Removed from `cfal_exclusions`.
2. ~~Geographic "Remote" / "Very Remote" rules~~ — confirmed as **BFS** policy (BFS Product Guide). Removed from `cfal_exclusions`; already correctly present in `bfs_chunks_v2.md` with the accurate "non-asset-backed" nuance (not "all Remote areas").
3. ~~"Standard settlement requirements" (QuickSell/biometrics/etc.)~~ — confirmed as **BFS** documentation requirements, mixed up with CFAL/Westpac's actual platform (DriveOnline). Removed from `cfal_settlement`; replaced with a short accurate note pointing to DriveOnline, since we still don't have a full CFAL/Westpac settlement checklist source.
4. **Rollover "Westpac / CFAL" attribution** — confirmed the source table only lists Westpac. `cfal_rollover_policy` now says Westpac-originated only, with a note that CFAL eligibility for the same cap is unconfirmed.

Re-ingested and live. Nice catch tracing all four back to their real source documents.

### Metro

5. **MetroEco EV loan cap conflict** — the MetroEco product booklet says **$91,387**; the newer Commercial Rate Sheet (effective 20/07/2026) says **$91,661**. Both are real, dated source documents; we don't know which is current. Flagged (not resolved) in both `metro_interest_rates` and `metro_eco` chunks. Your new Metro reference doc has both figures too, but doesn't flag them as conflicting — worth fixing there either way (see B.7 below).

---

## B. Issues found in your new reference documents

### Angle (`policies/Angle_Finance_Detailed_Reference.md`)

6. **EX120** — the accepted-lenders list for the $400K Low Doc credit reference is written as a closed list of 14 external lenders, but the source policy explicitly also accepts a reference from **Angle Finance itself** (an existing Angle loan). As written, this would wrongly reject an applicant using their own current Angle loan as the reference.
7. **Missing 12-month duration** — the $400K Low Doc program specifically requires a **12-month** asset finance credit reference; the document's only stated duration elsewhere is the generic 6-month rule, and the 12-month figure doesn't appear anywhere. Risk: applying 6 months where 12 is actually required.
8. **EX143** cites "EX134 (Non-Property Owners Require a 20% Deposit)" as a cross-reference, but EX134 in this same document is actually "Taxi and Uber Drivers Not Accepted" — a different topic entirely. The 20% deposit rule is real, it just doesn't have its own exception entry in this document.
9. **EX122** claims Westpac's EX002 and Metro's EX057 are both private-sale rate *loadings* (to contrast with Angle having none). Checked both — Westpac EX002 is an asset-category channel restriction, and Metro EX057 is about supplier eligibility, not a rate loading. Neither is actually a loading, so the comparison doesn't hold as written.

### BFS (`policies/BFS_Branded_Financial_Services_Detailed_Reference.md`)

10. **17.15% treated as a universal PRIME rate ceiling** — appears in Section 2, the worked example (`BFS-LOADING-001`), and EX087. It's actually **BFS Plus's own flat maximum rate**, not a cap that applies to Ultra Prime/Tier 1-4 pricing. Confirmed directly against the source PDF's rate table — 17.15% sits alone in the BFS Plus column. This is the same distinction we had to correct in our own chunk earlier this session, so it's an easy one to miss. Worth double-checking anywhere else in the document that references this figure.

### Metro (`policies/Metro_Commercial_Asset_Finance_Detailed_Reference-2.md`)

11. **Invented Luxury Car Tax rationale** — the document states the $91,387 EV cap "is the LCT threshold, adjusted annually" (appears twice). This isn't in either source document (the MetroEco booklet or the rate sheet) — it may well be true in the real world, but it's presented as sourced fact when it isn't.
12. **Same MetroEco conflict as A.5 above, but not flagged** — the document contains both $91,387 (six times, early on) and $91,661 (once, near the end, from the newer rate sheet) without ever connecting the two or noting they disagree.

### Westpac/CFAL Exceptions Catalog (`policies/Westpac_Equipment_Finance_Exceptions_Catalog.md`)

13. **EX005** conflates two different rows of the Medical channel limits table — states New Medical Equipment is capped at $500k (Specialist) / $250k (Allied Health), but those are actually the **cumulative approvals** caps; the real per-category medical-equipment caps are $350k / included-in-$150k. Its own worked example is self-contradictory as a result (an example marked "eligible" at $400k of equipment actually exceeds the real $350k cap).
14. **EX018** asserts that Matrix-policy deals get the full ≤$250k documentation tier "regardless of transaction size" — this is an interpretive leap beyond what the cited source text actually says, presented with more confidence than it's earned.

---

## What we're NOT flagging

Everything not listed above checked out — all core rates, thresholds, eligibility rules, fees,
and exclusion lists across all 5 of your documents matched our hand-verified chunks (which were
themselves checked line-by-line against the real source PDFs this session). The issues above are
concentrated in the interpretive/rationale/cross-reference layer, not the underlying policy facts.

Your documents also independently caught a few things we've now merged into our own chunks: Metro's
fuller Other Equipment eligible/non-eligible list, Metro's Agri "monthly payments only" rule, BFS's
learner-licence exception, and BFS Plus being fully excluded from remote lending (not just "Very
Remote"). Thanks for those — genuinely useful catches.
