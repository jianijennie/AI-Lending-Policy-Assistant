# Open Issues & Confusions — For Jiani

Compiled 2026-07-29 after a full audit of our RAG chunk system (`data/chunks/*.md`) against
every source PDF in `data/documents/`, plus a cross-check of the reference documents you've
uploaded to `policies/` (Angle, BFS, Metro, Resimac, Westpac/CFAL Exceptions Catalog, and —
added 2026-08-03 — Flexicommercial). Updated 2026-08-03 after your
`Exceptions_Catalog_Changelog.md` resolved most of section B below.

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

### Angle (`policies/Angle_Finance_Detailed_Reference.md`) — RESOLVED 2026-08-03

6. ~~EX120 accepted-lenders list~~ — fixed: now includes Angle Finance itself as an accepted reference, per `Exceptions_Catalog_Changelog.md`.
7. ~~Missing 12-month duration~~ — fixed: retitled and reworded to state the 12-month minimum for the $400K Low Doc product specifically.
8. ~~EX143 wrong cross-reference~~ — fixed: now points to a new standalone **EX183** (Non-Property Owners Require a 20% Deposit) instead of the mislabeled EX134.
9. ~~EX122 Westpac/Metro loading mischaracterization~~ — fixed: `related_policy` now cites only genuinely-comparable loading examples (Resimac, BFS), with an explicit note on why Westpac EX002/Metro EX057 were removed.

Nice, precise fixes — all four match exactly what we flagged, down to the specific field changed.

### BFS (`policies/BFS_Branded_Financial_Services_Detailed_Reference.md`) — partially resolved, one correction needed

10. **17.15% scope** — your changelog flags this as genuinely ambiguous ("UNCERTAIN SCOPE... plain-text extraction cannot conclusively resolve which reading is correct") and recommends confirming with BFS directly. We went back and rendered the actual source page as an image to check: it's **not actually ambiguous**. The page layout has two clearly separate, side-by-side panels — "PRIME" (Ultra Prime–Tier 4, with its own detailed rate grid) on the left, and "PLUS" (BFS Plus, a single column) on the right. The "Maximum Rate: 17.15%" box sits directly under the BFS Plus column header, appearing twice (once for Commercial pricing, once for Consumer) — never inside or adjacent to the Prime tier grid. This was a text-extraction limitation, not a real ambiguity in the source. Recommend updating EX184 to state this with confidence (BFS Plus only) rather than flagging it as needing BFS confirmation — happy to send the rendered page image if useful.

### Metro (`policies/Metro_Commercial_Asset_Finance_Detailed_Reference-2.md`)

11. **Invented Luxury Car Tax rationale** — per your own changelog, confirmed as a valid concern but **not yet corrected** in the live document. Still worth doing — reword to attribute the LCT connection as an inference, not stated Metro policy.
12. ~~MetroEco $91,387/$91,661 conflict not flagged~~ — fixed: new **EX182** explicitly documents both figures as genuine verbatim quotes from two different Metro documents, with a warning not to treat either as authoritative without verification. Matches our own chunks' handling of the same conflict.

### Westpac/CFAL Exceptions Catalog (`policies/Westpac_Equipment_Finance_Exceptions_Catalog.md`) — partially resolved, one correction needed

13. **EX005 medical limits** — your fix correctly identifies that $500k/$250k are "Max. Cumulative Approvals" (aggregate), not per-item caps — that part's right and matches our own `cfal_medical_policy` chunk. But the changelog goes on to flag the *alternative* figures ($350k Specialist / $150k Allied Health) as **UNCONFIRMED, not in any source material available to us** — we checked, and that's not right either: we rendered the actual Key Financial Policies page as an image, and the $350k/$150k figures are clearly visible in the same Medical table, in their own dedicated row ("New Medical equipment"), distinct from the Cumulative Approvals row. They also already match our own independently-verified chunk exactly. Recommend updating EX005 to state $350k/$150k as confirmed (not unconfirmed) — again, happy to send the page image.
14. ~~EX018 Matrix policy overconfidence~~ — fixed: retitled to flag it explicitly as an inference from checkbox correlation, not a confirmed CFAL statement, with a recommendation to verify directly for large transactions.

### Flexicommercial (`policies/Flexicommercial_Detailed_Reference-2.md`) — new document, audited 2026-08-03

Good news first: **all Section 3 rates match the current 13 July 2026 rate card exactly** — flexipremium 7.15%, the merged $20,001–$150,000 standard band, and the new 1.50% non-asset-backed loading (correctly kept separate from the 1.25% >60-month loading) all check out. The full Credit Matrix exposure ceilings, flexireplacement policy (125% cap, 90-day settlement window, 23-lender list), and the cross-check against Metro's replacement policy (EX148) were all verified verbatim against the source PDFs — no numeric errors found there.

Two things worth fixing:

15. **Dangling "Section 4" references** — three exceptions (around the Credit Matrix increased-exposure rules) cite "Section 4 (Credit Matrix — ...)" as a cross-reference, but there is no Section 4 anywhere in the document — the headings jump straight from Section 3 to Section 5. The Credit Matrix's core numbers only appear scattered inside individual exception examples, never as its own narrative section. Not a factual error, but a structural gap — a reader following that cross-reference finds nothing.
16. **Unsupported "19 May 2026" date** — both the intro and closing note date the flexipremium Low Start Loans, Old Finance Meets New, and Mid-Term Refinancing fact sheets to "19 May 2026." We read all three source PDFs directly — none of them displays a date anywhere, unlike the Rate Card/Credit Matrix/flexireplacement Policy, which are all clearly dated on their face. This looks like an invented date; worth removing or verifying where it actually came from.

Minor/optional: the worked-example numbers from the three fact sheets (e.g. the Low Start Loan's $8,400 vs $4,200 vs $9,196/month figures) are in the source PDFs and in our own chunks, but aren't reproduced in this document — not wrong, just thinner than it could be.

---

## What we're NOT flagging

Everything not listed above checked out — all core rates, thresholds, eligibility rules, fees,
and exclusion lists across all 6 of your documents (Angle, BFS, Metro, Resimac, Westpac/CFAL,
Flexicommercial) matched our hand-verified chunks and/or the source PDFs directly. The issues
above are concentrated in the interpretive/rationale/cross-reference layer and a couple of
document-structure gaps, not the underlying policy facts.

Your documents also independently caught a few things we've now merged into our own chunks: Metro's
fuller Other Equipment eligible/non-eligible list, Metro's Agri "monthly payments only" rule, BFS's
learner-licence exception, and BFS Plus being fully excluded from remote lending (not just "Very
Remote"). Thanks for those — genuinely useful catches.

**Status as of 2026-08-03:** of the 14 original items in section B, 10 are now fully resolved via
your `Exceptions_Catalog_Changelog.md`, 1 remains open on your end (Metro's LCT wording), and 2
resolutions need a small follow-up correction (BFS 17.15% and Westpac EX005 — both flagged
"unconfirmed" when they're actually directly confirmable from the source page images, details
above). Plus 2 new items from auditing the new Flexicommercial document, which was otherwise clean
and fully current against the 13 July 2026 rate card.
