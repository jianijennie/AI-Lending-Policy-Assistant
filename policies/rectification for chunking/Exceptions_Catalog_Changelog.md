# Exceptions Catalog — Correction Changelog

> This document tracks every correction made across the multi-lender Exceptions Catalogs (Westpac/CFAL, Metro,
> BFS, Angle, flexicommercial) following review of the reference documents. Each entry shows what was wrong,
> what was changed, and the original-source evidence used to verify the correction. Use this as an audit trail —
> the source-of-truth content itself lives in each lender's own document, not here.

---

## 1. Angle Finance (`Angle_Finance_Detailed_Reference.md`)

### EX120 — $400K Low Doc Credit Reference
**Problem:** The entry only listed the 14 named external lenders as acceptable credit reference sources, and
omitted the product-specific 12-month minimum (incorrectly leaving the general 6-month rule as the only stated
duration).

**Original source text (Angle Rate Card, $400K Low Doc Checklist, page 1):**
> "Minimum 12-months Asset Finance Credit Reference (Angle Finance or a Tier 1 / Tier 2 Asset Finance Provider)"

**Fix applied:**
- Retitled to "$400K Low Doc Credit Reference — Angle Finance Itself OR a Named List of Accepted External
  Lenders, 12 Months Minimum"
- `policy_statement` now quotes both the checklist line (which includes "Angle Finance") and the named-lender
  definitions line
- `interpretation`, `business_logic`, `examples`, and `decision` all updated to state a reference from Angle's own
  existing loan book satisfies the requirement, and that 12 months (not 6) is the minimum for this specific
  product
- `related_policy` updated to explicitly contrast with EX129 (the general 6-month rule)

### EX143 — Low Doc Under $100k Non-Property-Backed Pathway
**Problem:** `related_policy` cited "EX134 (Non-Property Owners Require a 20% Deposit...)" — but EX134 is actually
titled "Taxi and Uber Drivers Not Accepted." No exception entry for the 20% deposit rule existed at all.

**Original source text (Angle Rate Card, Property Ownership):**
> "Non property owners require a 20% deposit."

**Fix applied:**
- EX143's `related_policy` corrected to point to the new **EX183** instead of the mislabeled EX134
- Created **EX183 — Non-Property Owners Require a 20% Deposit** as a standalone entry (previously this rule
  existed only as unlinked prose, never as its own catalog entry)

### EX122 — No Rate Loading for Private Sales (Angle-wide policy)
**Problem:** The cross-lender comparison note cited "Westpac EX002" and "Metro EX057" as examples of lenders
that DO apply a private-sale rate loading. Neither is actually a rate-loading exception.

**Verification:**
- Westpac EX002 = "Private Sale Eligibility Scope Restriction (DriveXpress)" — this is an **asset-category
  eligibility restriction** (private sale limited to Category A), not a rate loading.
- Metro EX057 = "Metro Allows Private Sale Where Other Lenders Restrict to Dealer Only" — this is a **supplier
  eligibility comparison**, not a rate loading.

**Fix applied:**
- `related_policy` corrected to cite only the two genuinely-comparable rate-loading examples (Resimac Section 1.1
  — Private Sale +2% risk loading; BFS EX086 — Private Sale Loading +0.50%), with an explicit note that Westpac
  EX002 and Metro EX057 were removed because they are not loading examples.

---

## 2. BFS (`BFS_Branded_Financial_Services_Detailed_Reference.md`)

### 17.15% "Maximum Rate" — scope ambiguity
**Problem:** The document treated 17.15% as a universal ceiling applying across ALL Prime tiers (Ultra Prime
through Tier 4), including using it as the cap-check in the Section 2 worked example for a Tier 3 deal.

**Original source layout (BFS Product Guide, page 1):** The "Maximum Rate: 17.15%" box is positioned to the
right of the main Commercial/Consumer Pricing tables, in a position structurally aligned with the separate
"PLUS / BFS Plus" column (which has no tiered rate table of its own) — not clearly spanning the Ultra Prime–Tier
4 tier table. The plain-text extraction cannot conclusively resolve which reading is correct.

**Fix applied:**
- Section 2 rate-mechanics summary now flags this as "UNCERTAIN SCOPE" with an explicit warning not to treat
  17.15% as a confirmed universal Prime ceiling
- The Section 2 worked example (`case_example_id: BFS-LOADING-001`) updated to note the ambiguity at
  `step_4_check_against_cap` and in `key_takeaway`, clarifying it demonstrates the calculation MECHANIC, not a
  confirmed Tier 3 ceiling
- EX087's `decision` and `related_policy` updated to reference the new EX184
- Created **EX184 — 17.15% Maximum Rate — Ambiguous Whether It Is a Prime-Wide Ceiling or a BFS Plus-Specific
  Figure**, documenting the ambiguity and recommending direct verification with BFS

---

## 3. Metro (`Metro_Commercial_Asset_Finance_Detailed_Reference.md`)

*(Corrected in the prior session, included here for completeness of the audit trail.)*

### $91,387 vs $91,661 — MetroEco EV loan cap conflict
**Problem:** EX050/EX055 cited $91,387 (from the MetroEco Electric Vehicles & Chargers brochure) and EX116 cited
$91,661 (from the Commercial Asset Finance Rate Card, 20/07/2026) — six references to one figure, one reference
to the other — with no cross-note that the two figures conflict.

**Original source text:**
- MetroEco Electric Vehicles & Chargers brochure: "Loan Amount: Up to $91,387.00 on vehicles"
- Commercial Asset Finance Rate Card (20/07/2026), MetroEco box: "1% discount applies for new electric vehicles
  up to $91,661"

**Fix applied:**
- Created **EX182 — MetroEco EV Loan Cap Discrepancy ($91,387 vs $91,661)**, explicitly stating both figures are
  genuine verbatim quotes from two different Metro documents and that neither should be treated as authoritative
  without verification
- Added ⚠️ cross-reference warnings to EX050's and EX116's `related_policy` fields pointing to EX182

### Luxury Car Tax (LCT) explanation
**Problem:** EX050 and Section 5.1 presented "this cap tracks the Luxury Car Tax threshold for fuel-efficient
vehicles" as if it were Metro's own stated reasoning, when it is actually Claude's own inference — Metro's source
documents never mention "Luxury Car Tax" at all.

**Status:** Confirmed as a valid concern. **Not yet corrected in the live document** — recommended next step is
to reword the `business_rationale` language in EX050 and the Section 5.1 note to explicitly attribute the LCT
explanation as an inference (e.g. "this figure numerically aligns with the LCT threshold for fuel-efficient
vehicles, though Metro's source documents do not state this connection explicitly") rather than presenting it as
confirmed official reasoning.

---

## 4. Westpac / CFAL (`Westpac_Equipment_Finance_Exceptions_Catalog.md`)

### EX005 — Medical Specialist vs Allied Health Practitioner Limits
**Problem:** The entry labelled the $500,000 / $250,000 figures as a "New Medical Equipment" per-item limit. The
original source table has no such row — those figures belong to a row labelled "Max. Cumulative Approvals" (an
aggregate ceiling across a customer's total Medical facilities, not a single-item equipment cap). The worked
example ("GP applying for $400,000 of new medical equipment... within the $500k limit") was built on this
mislabeling.

**Original source table (Westpac Equipment Finance Key Policies, Medical, as originally transcribed):**
> Motor Vehicle up to 5 yrs old: <$250,000 / <$150,000
> New Office equipment and fittings: <$350,000 / <$150,000
> Max. Cumulative Approvals: <$500,000 / <$250,000

**Fix applied:**
- `policy_statement`, `interpretation`, `examples`, and `business_logic` corrected to label $500k/$250k as
  "Max. Cumulative Approvals" (an aggregate ceiling), not a "New Medical Equipment" item limit
- Added an explicit note that a reviewer suggested alternative figures ($350k Specialist single-item cap; Allied
  Health "included within" $150k) — but these specific numbers do **not** appear in any source material available
  to us and are flagged as **UNCONFIRMED**, requiring verification against the original Westpac table image or
  current DriveOnline policy before being treated as fact
- The old example (GP at $400,000 "within the $500k limit") is retained but annotated as having previously
  conflated a cumulative ceiling with a single-item purchase, with a warning that if the true per-item limit is
  lower (e.g. the unconfirmed $350k figure), that $400,000 example would NOT actually be eligible

### EX018 — Matrix Policy Reduced Documentation (CFAL)
**Problem:** The entry stated as confirmed fact that Matrix-policy deals "follow the same reduced documentation
checklist as the ≤$250k tier, regardless of the actual transaction size." This is not an explicit sentence in the
CFAL source document — it was inferred from the Matrix column's checkmarks visually matching the ≤$250k column's
checkmarks in the checklist table.

**Fix applied:**
- Retitled to "Matrix Policy Reduced Documentation Requirement (CFAL) — INFERRED, Not Explicitly Stated"
- `interpretation`, `business_rationale`, `business_logic`, and `decision` all reworded to explicitly flag this as
  an inference drawn from checkbox correlation, not a confirmed CFAL statement, with an explicit recommendation
  to verify directly with CFAL — especially for transactions materially above $250,000
- Removed an orphaned duplicate text fragment left over from the original version during editing (structural
  cleanup; verified the file's YAML code-fence count remains balanced after the fix)

---

## 5. flexicommercial (`Flexicommercial_Detailed_Reference.md`)

### EX148 — flexireplacement Repayment Cap (125% rule)
**Addition (not a correction — a clarifying note requested directly):** Added an explicit note distinguishing
flexicommercial's single repayment-only test from Metro's dual (loan amount OR repayment) test under its own
Replacement Policy (EX041), and flagging that any additional loan-amount test is not documented in the current
flyer.

**Note added verbatim:**
> "Note: The current FlexiReplacement flyer explicitly limits only the proposed repayment to 125% of the facility
> being replaced. It does not mention an equivalent loan amount or finance amount test. Unlike Metro's replacement
> policy, no 'Loan Amount OR Repayment' alternative is provided. If Flexicommercial applies an additional loan
> amount test internally, this is not documented in the current flyer and should be confirmed directly with
> Flexicommercial before being treated as policy."

---

## Outstanding / Not Yet Actioned

| Item | Status |
|---|---|
| Metro — Luxury Car Tax explanation reworded to mark it as inference, not stated fact | **Not yet corrected** — flagged in this changelog, pending edit |
| CFAL "Repairable Write-offs" chunk attribution | Previously assessed as likely a Resimac→CFAL mislabeling; recommend checking the chunk pipeline's source field directly |
| CFAL "Geographic Exclusions" (Remote/Very Remote) chunk attribution | Previously assessed as a BFS→CFAL mislabeling (matches BFS EX101/EX102 verbatim) |
| CFAL "Standard Settlement Requirements" (QuickSell/Biometrics) chunk attribution | Previously assessed as a BFS→CFAL mislabeling (QuickSell is a BFS platform, not CFAL/Westpac) |
| CFAL "Rollover Original Funder" $500K All Goods claim | Previously assessed as an unsupported inference — the Westpac Rollover table names only "Westpac" and "Other Financier," never "CFAL" |

---

*This changelog reflects corrections made during this review session. It is a working audit document, not a
policy source — always defer to the corrected lender-specific Exceptions Catalog files for the current, accurate
content.*
