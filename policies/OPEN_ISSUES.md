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

### CFAL

1. **"Repairable write-offs" exclusion** (`data/chunks/cfal_chunks_v2.md`, `cfal_exclusions` chunk) — listed as an excluded vehicle/asset type, but this phrase doesn't appear anywhere in any of our 5 CFAL/Westpac source PDFs. Might be a real CFAL policy from a document we don't have, or might be an unsupported addition — we can't tell which.
2. **Geographic exclusions — "Remote" / "Very Remote" areas** (same chunk) — a rule requiring 20% deposit in "Remote" areas (ABS 2021 classification) and unavailability in "Very Remote" areas. Same situation: not found in any source PDF we have. (Your Exceptions Catalog doesn't have this either — we checked.)
3. **"Standard settlement requirements" bullets** (`cfal_settlement` chunk) — QuickSell/DriveOnline payout docs, biometrics, tax invoice, fully-signed loan documents. `UPDATEDEquipmentFinanceSettlementRequirements.pdf` only covers two specific 2025 changes (PPSR simplification, CoC fleet exemption) — none of these bullets are in it or anywhere else we have.
4. **Rollover "Original Funder" attribution** (`cfal_rollover_policy` chunk) — our chunk lists the $500k/all-goods rollover cap as available to "Westpac / CFAL" originated contracts, but the actual source table (Key Financial Policies) only shows "Westpac" in that cell. We don't know whether CFAL-originated rollovers actually get the same cap, or whether this was an assumption by whoever wrote the chunk originally.

### Metro

5. **MetroEco EV loan cap conflict** — the MetroEco product booklet says **$91,387**; the newer Commercial Rate Sheet (effective 20/07/2026) says **$91,661**. Both are real, dated source documents; we don't know which is current. Flagged (not resolved) in both `metro_interest_rates` and `metro_eco` chunks. Your new Metro reference doc has both figures too, but doesn't flag them as conflicting — worth fixing there either way (see B.7 below).

If any of these five turn out to be genuinely unsupported (not just missing from our document set), the right fix is probably to just remove the claim rather than keep it — but we didn't want to delete something that might be true just because we personally couldn't verify it.

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
