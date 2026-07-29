# BFS (Branded Financial Services) — Detailed Policy Reference & Exceptions Catalog

> Source: Branded Financial Services — Product Guide (Broker), effective 1 July 2026.
> Purpose: A standalone deep-dive reference (parallel to the Resimac and Metro references) covering BFS's
> tier structure (Ultra Prime → Tier 1–4 → BFS Plus), rate loading mechanics, documentation tiers, fees, and
> commission/clawback terms — with all exception clauses listed separately in Section 5, using the same
> `exception_id` / `keywords` / `synonyms` / `intent_examples` / `decision` / `related_policy` schema as the
> Westpac/CFAL/Resimac Exceptions Catalog and the Metro Exceptions Catalog. IDs continue from EX084 onward.

---

## 1. Tier Structure Overview

BFS prices risk through six tiers, driven primarily by the applicant's/guarantor's Experian CCR (Comprehensive
Credit Reporting) score:

| Tier | Min. CCR Score | Notes |
|---|---|---|
| Ultra Prime | 960 | Strongest tier; exempt from the non-asset-backed loading |
| Tier 1 | 800 | |
| Tier 2 | 600 | |
| Tier 3 | 550 | + mandatory 20% deposit |
| Tier 4 | 400 | + mandatory 20% deposit; New/Demo commercial only (no Used) |
| BFS Plus | 400 (550 for commercial Used contracts) | Separate product line with its own criteria (see Section 5) |

BFS Plus sits alongside (not strictly "above" or "below") the Prime tiers — it has a different eligibility and
documentation framework rather than simply being a lower-score version of Prime.

---

## 2. Rate & Loading Mechanics

**Base rates** are set by tier + vehicle age/condition (New/Demo, Used 2022–2026, Used 2017–2021, Used 2016 and
older), separately for Commercial and Consumer pricing. On top of the base rate:

- **Maximum margin above base**: capped at 6% — brokers cannot price more than 6 percentage points above the
  published base rate for the tier/asset combination.
- **Non-asset-backed loading**: +1.85% (Commercial) or +1.25% (Consumer), Tier 1–4 only — **does not apply to
  Ultra Prime** (see EX085).
- **Private sale loading**: +0.50%, applies across both Commercial and Consumer pricing, all tiers (see EX086).
- **Maximum rate**: 17.15% (both Commercial and Consumer), with a discretionary discount of up to 2% available
  off the maximum rate.

### Worked Case Example

```yaml
case_example_id: BFS-LOADING-001
scenario: >
  A Tier 3 commercial applicant wants to finance a used (2019) vehicle
  privately, with no asset backing (renting, no property).
step_1_base_rate: >
  Tier 3, Used 2017–2021, Commercial -> base rate 12.90%.
step_2_apply_loadings:
  - Non-asset-backed (Tier 1-4 applies) -> +1.85%
  - Private sale -> +0.50%
step_3_sum: 12.90% + 1.85% + 0.50% = 15.25%
step_4_check_against_cap: >
  15.25% is below the 17.15% maximum rate, so no further capping is
  needed. Also check: margin above base = 15.25% - 12.90% = 2.35%,
  well within the 6% maximum margin allowance.
step_5_final_rate: 15.25% p.a. (subject to any discretionary discount up to 2% off the maximum rate, at BFS's discretion)
key_takeaway: >
  Loadings are additive on top of the tier's base rate, but the deal must
  still respect BOTH the 6%-above-base margin cap AND the 17.15% absolute
  maximum rate — whichever constrains the rate first applies.
```

---

## 3. Documentation Tiers (Commercial)

| | Low Doc | Full Doc | New Business Ventures |
|---|---|---|---|
| Tier | Ultra Prime–Tier 2 only | Ultra Prime–Tier 4, BFS Plus | Ultra Prime–Tier 4 only |
| Loan Size | Up to $150,000 (total exposure) | Up to $250,000 (standard); up to $400,000 (high value) | Up to $100,000 (total exposure) |
| Trading History | 2+ years (ABN + GST) | 12+ months (ABN) | Less than 12 months (ABN) |
| Minimum Deposit | 0% | 20% for Tiers 3 & 4 | 20% for Tiers 3 & 4 |

## 4. Fees & Commission Summary

| Fee | Amount |
|---|---|
| Establishment fee | $525 Consumer / $625 Consumer Private Sale / $575 Commercial / $675 Commercial Private Sale |
| Origination fee | Up to $1,650, added to the loan and paid to the introducer |
| PPSR registration fee | $6 |
| Account maintenance fee | $10/month, $4.62/fortnight, or $2.31/week depending on repayment frequency |
| Variation fee | $60 per variation |
| Statement fee | $15 per paper statement |
| Early termination admin fee | $70 Consumer / $85 Commercial |

| Commission Term | Rule |
|---|---|
| Payment in full or termination | 100% of commission/incentives refundable to BFS if terminated or paid in full within the first 12 months |
| Brokerage | 75% overs, net of GST |
| Repossession or loan write-off | 100% of commission refundable to BFS if this occurs within 24 months |

---

## 5. Exceptions Catalog (BFS)

```yaml
exception_id: EX084
title: Tier 3/4 Lower CCR Score Compensated by Mandatory 20% Deposit
source_document: BFS Product Guide — Minimum Experian CCR Score table
policy_statement: >
  "Tier 3: 550 +20% deposit. Tier 4: 400 +20% deposit."
interpretation: >
  Tiers 3 and 4 accept lower credit scores than Tier 1/2/Ultra Prime, but
  ONLY if the applicant provides a 20% deposit — the deposit is not
  optional for these tiers, it is the trade-off that makes the lower
  score acceptable at all.
business_rationale: >
  A lower credit score increases default risk; the 20% deposit reduces
  BFS's loan-to-value exposure to compensate, keeping the effective risk
  in a similar range to the higher-score tiers.
examples:
  eligible:
    - Applicant with CCR 560, 20% deposit provided -> eligible for Tier 3
  ineligible:
    - Applicant with CCR 560, no deposit or less than 20% -> not eligible
      for Tier 3 at all (does not default to a lower tier without deposit)
business_logic: |
  IF ccr_score >= 550 AND ccr_score < 600 AND deposit_pct >= 20%:
    tier = "Tier 3"
  ELSE IF ccr_score >= 400 AND ccr_score < 550 AND deposit_pct >= 20%:
    tier = "Tier 4"
  ELSE IF ccr_score < 550 (or <400) AND deposit_pct < 20%:
    not_eligible = True
keywords:
  - CCR score
  - Tier 3
  - Tier 4
  - 20% deposit
synonyms:
  CCR score:
    - Experian score
    - credit score
intent_examples:
  - "Can I qualify for Tier 3 without a deposit?"
  - "What deposit is required for a 560 credit score applicant?"
decision: Not Eligible for Tier 3/4 without the mandatory 20% deposit
related_policy:
  - Section 1 (Tier Structure Overview)
```

```yaml
exception_id: EX085
title: Non-Asset-Backed Loading Does Not Apply to Ultra Prime
source_document: BFS Product Guide — Commercial/Consumer Pricing Adjustments
policy_statement: >
  "Non-asset backed subject to a loading of 1.85% [Commercial] / 1.25%
  [Consumer] (Tier 1-4 only, does not apply to Ultra Prime)."
interpretation: >
  The non-asset-backed loading applies to Tier 1 through Tier 4
  applicants who lack property/asset backing, but Ultra Prime applicants
  are exempt from this loading entirely, regardless of their asset-backed
  status.
business_rationale: >
  Ultra Prime's very high CCR threshold (960) already reflects an
  exceptionally low-risk applicant profile, so BFS does not consider
  asset backing a material additional risk factor at that tier — the
  credit score alone is considered sufficient.
examples:
  eligible:
    - Ultra Prime applicant with no asset backing -> no 1.85%/1.25%
      loading applied
  ineligible (i.e., loading DOES apply):
    - Tier 2 applicant with no asset backing -> 1.85% (Commercial) or
      1.25% (Consumer) loading applies
business_logic: |
  IF tier == "Ultra Prime":
    non_asset_backed_loading = 0%  # exempt regardless of asset backing
  ELSE IF tier IN {"Tier 1", "Tier 2", "Tier 3", "Tier 4"} AND asset_backed == False:
    non_asset_backed_loading = 1.85% (Commercial) OR 1.25% (Consumer)
keywords:
  - non-asset backed
  - Ultra Prime
  - loading exemption
synonyms:
  non-asset backed:
    - unsecured applicant
    - no property backing
intent_examples:
  - "Does Ultra Prime get charged extra for having no asset backing?"
decision: Not Applicable to Ultra Prime — loading applies only to Tier 1–4
related_policy:
  - Section 2 (Rate & Loading Mechanics)
```

```yaml
exception_id: EX086
title: Private Sale Loading (+0.50%) Stacks With Non-Asset-Backed Loading
source_document: BFS Product Guide — Commercial/Consumer Pricing Adjustments
policy_statement: >
  "Private sale subject to an additional loading of 0.50%" — listed as a
  separate adjustment line from the non-asset-backed loading.
interpretation: >
  The 0.50% private sale loading is independent of, and stacks with, the
  non-asset-backed loading (EX085) and applies across all tiers
  (including Ultra Prime, unlike the non-asset-backed loading) whenever
  the transaction is a private sale.
business_rationale: >
  Private sale risk (provenance/valuation uncertainty) is treated as a
  universal pricing factor across every tier, unlike asset-backing risk,
  which BFS considers immaterial once an applicant reaches Ultra Prime
  status.
examples:
  eligible:
    - Ultra Prime applicant, private sale vehicle -> +0.50% loading
      applies (even though Ultra Prime is exempt from the non-asset-
      backed loading)
  ineligible (i.e., no loading):
    - Any tier, dealer-sourced vehicle -> no private sale loading applies
business_logic: |
  IF transaction_type == "private_sale":
    rate_loading += 0.50%  # applies regardless of tier, including Ultra Prime
keywords:
  - private sale
  - loading
  - stacking
synonyms:
  private sale:
    - non-dealer purchase
intent_examples:
  - "Does the private sale loading apply even to Ultra Prime?"
  - "Can the private sale loading and non-asset-backed loading both apply to the same deal?"
decision: Applicable to all tiers including Ultra Prime; stacks additively with other loadings
related_policy:
  - EX085 (Non-Asset-Backed Loading Does Not Apply to Ultra Prime — contrast)
  - Section 2 (Rate & Loading Mechanics)
```

```yaml
exception_id: EX087
title: Maximum Margin Above Base Rate Capped at 6%
source_document: BFS Product Guide — Commercial Pricing Adjustments
policy_statement: >
  "Maximum margin above base 6%."
interpretation: >
  Regardless of how many loadings apply or how much discretionary margin
  a broker wants to add, the total rate cannot exceed the tier/asset
  base rate by more than 6 percentage points.
business_rationale: >
  Protects against excessive cumulative pricing (loadings + broker
  margin) that could otherwise push a rate unreasonably high even before
  hitting the absolute 17.15% ceiling, and supports Best Interest Rate
  Duty (BID) compliance by keeping broker-added margin within a defined
  band.
examples:
  eligible:
    - Base rate 8.50%, combined loadings + margin bring the rate to
      14.00% (5.50% above base) -> within the 6% margin cap
  ineligible:
    - Base rate 8.50%, broker attempts to price at 15.50% (7% above base)
      -> exceeds the 6% margin cap, not permitted even if still under the
      17.15% absolute maximum
business_logic: |
  IF (proposed_rate - base_rate) > 6%:
    not_permitted = True  # even if proposed_rate < 17.15% absolute max
keywords:
  - maximum margin
  - 6% cap
  - Best Interest Duty
synonyms:
  margin:
    - broker margin
    - rate margin
intent_examples:
  - "Can I set a rate 7% above the base rate if it's still under the maximum rate?"
decision: Not Permitted above 6% margin over base, independent of the 17.15% absolute maximum
related_policy:
  - Section 2 (Rate & Loading Mechanics — worked example)
```

```yaml
exception_id: EX088
title: Tier 4 Excludes Commercial Contracts for Used Vehicles (New/Demo Only)
source_document: BFS Product Guide — Commercial Pricing table / Vehicle Types table
policy_statement: >
  Tier 4 commercial pricing shows rates only for "New and Demo" (11.50%);
  all "Used" rows are marked "Not available" for Tier 4. The Vehicle
  Types table confirms: "No commercial contracts for Used."
interpretation: >
  Tier 4 commercial applicants can only finance new or demonstrator
  vehicles — used vehicles of any age are not financeable under Tier 4
  commercial pricing at all, even though Tier 4 is otherwise the most
  accessible Prime tier (lowest CCR threshold).
business_rationale: >
  Tier 4 already represents the highest-risk Prime tier (lowest CCR
  score, mandatory deposit); combining this with a used vehicle (which
  itself carries higher depreciation/valuation risk) is considered an
  unacceptable compounded risk, so BFS restricts Tier 4 commercial to
  New/Demo only.
examples:
  eligible:
    - Tier 4 applicant, brand-new commercial vehicle -> eligible
  ineligible:
    - Tier 4 applicant, 2020 used commercial vehicle -> not eligible
      under Tier 4 at all; may need to be reassessed under a different
      tier if the applicant's profile changes, or the deal does not
      proceed
business_logic: |
  IF tier == "Tier 4" AND product == "Commercial" AND vehicle_condition == "used":
    not_eligible = True
keywords:
  - Tier 4
  - commercial
  - used vehicle exclusion
synonyms:
  Tier 4:
    - lowest Prime tier
intent_examples:
  - "Can a Tier 4 applicant finance a used commercial vehicle?"
decision: Not Eligible — Tier 4 commercial is New/Demo only, no used vehicles
related_policy:
  - Section 1 (Tier Structure Overview)
```

```yaml
exception_id: EX089
title: Tier 4 and BFS Plus Restricted to Passenger & Light Commercial Only
source_document: BFS Product Guide — Vehicle Types table
policy_statement: >
  Tier 4: "Passenger vehicles and light commercial only." BFS Plus:
  "Passenger vehicles and light commercial vehicles only."
interpretation: >
  Unlike Ultra Prime through Tier 3 (which also accept motorcycles,
  motorhomes, campervans, caravans, and camper trailers, plus limited
  ride-share/hire/rental appetite), Tier 4 and BFS Plus are restricted to
  standard passenger and light commercial vehicles only.
business_rationale: >
  Motorcycles, motorhomes, and caravans carry more specialised
  valuation/resale characteristics; BFS reserves this broader asset
  appetite for its stronger credit tiers (Ultra Prime–Tier 3) and keeps
  the higher-risk/lower-score tiers (Tier 4, BFS Plus) focused on the
  most standardised, liquid asset types.
examples:
  eligible:
    - Tier 4 applicant financing a passenger car -> eligible
  ineligible:
    - Tier 4 applicant financing a motorhome -> not eligible; motorhomes
      are only available Ultra Prime–Tier 3
    - BFS Plus applicant financing a caravan -> not eligible
business_logic: |
  IF tier IN {"Tier 4", "BFS Plus"} AND asset_type IN {"motorcycle", "motorhome", "campervan", "caravan", "camper trailer"}:
    not_eligible = True
keywords:
  - Tier 4
  - BFS Plus
  - motorcycle exclusion
  - motorhome exclusion
synonyms:
  light commercial:
    - light commercial vehicle
intent_examples:
  - "Can a BFS Plus applicant finance a caravan?"
  - "Are motorcycles available under Tier 4?"
decision: Not Eligible for motorcycles/motorhomes/campervans/caravans/camper trailers under Tier 4 or BFS Plus
related_policy:
  - Section 1 (Tier Structure Overview)
  - EX107 (Motorcycle-specific requirements, for the tiers where motorcycles ARE eligible)
```

```yaml
exception_id: EX090
title: BFS Plus Requires a Higher CCR Score (550) Specifically for Commercial Used Contracts
source_document: BFS Product Guide — Minimum Experian CCR Score table
policy_statement: >
  "BFS Plus: 400. 550 – commercial contracts for Used."
interpretation: >
  BFS Plus's standard minimum CCR score is 400, but this rises to 550
  specifically for commercial contracts financing a USED vehicle — new/
  demo commercial and all consumer BFS Plus contracts remain at the
  400 threshold.
business_rationale: >
  Combines the general BFS Plus risk profile (already a lower-score
  product) with the added depreciation/valuation risk of a used
  commercial asset, requiring a stronger credit profile to accept that
  compounded risk.
examples:
  eligible:
    - BFS Plus applicant, CCR 570, financing a used commercial vehicle ->
      eligible (meets the 550 threshold for this specific scenario)
  ineligible:
    - BFS Plus applicant, CCR 450, financing a used commercial vehicle ->
      not eligible (below the 550 threshold required for commercial used,
      even though 450 would be sufficient for consumer or new/demo
      commercial BFS Plus deals)
business_logic: |
  IF product == "BFS Plus":
    IF contract_type == "commercial" AND vehicle_condition == "used":
      require(ccr_score >= 550)
    ELSE:
      require(ccr_score >= 400)
keywords:
  - BFS Plus
  - commercial used
  - CCR threshold
synonyms:
  BFS Plus:
    - Plus tier
intent_examples:
  - "What CCR score do I need for a BFS Plus used commercial vehicle loan?"
decision: Conditional — 550 minimum CCR specifically for BFS Plus commercial used contracts; 400 otherwise
related_policy:
  - Section 1 (Tier Structure Overview)
```

```yaml
exception_id: EX091
title: Maximum Vehicle Age Tightens for Terms Over 60 Months (7 Years vs 15 Years)
source_document: BFS Product Guide — Maximum Vehicle Age (Prime)
policy_statement: >
  "15 years at the start of the term (terms up to 60 months) or 7 years
  at start of term (terms over 60 months)."
interpretation: >
  Prime allows a vehicle up to 15 years old at the START of the loan if
  the term is 60 months or less, but if the term extends beyond 60
  months (up to the 84-month maximum), the vehicle must be no older than
  7 years at the start of the term — a much tighter limit.
business_rationale: >
  Longer loan terms project further into the future, compounding
  residual/mechanical risk for an already-older vehicle; BFS halves the
  acceptable starting age (roughly) when the term extends past 60 months
  to keep the projected end-of-term age within a reasonable range.
examples:
  eligible:
    - 12-year-old vehicle financed over a 48-month term -> eligible
      (within the 15-year limit for terms up to 60 months)
    - 5-year-old vehicle financed over a 72-month term -> eligible
      (within the 7-year limit for terms over 60 months)
  ineligible:
    - 12-year-old vehicle financed over a 72-month term -> not eligible;
      exceeds the 7-year starting-age limit that applies once the term
      goes over 60 months
business_logic: |
  IF loan_term_months <= 60:
    max_vehicle_age_at_start = 15 years
  ELSE:  # loan_term_months > 60, up to 84
    max_vehicle_age_at_start = 7 years
keywords:
  - vehicle age
  - loan term
  - 60 months
  - 84 months
synonyms:
  vehicle age:
    - asset age at start of term
intent_examples:
  - "Can I finance a 12-year-old car over a 7-year term?"
  - "Why is the vehicle age limit different for longer loan terms?"
decision: Not Eligible for vehicles older than 7 years if the term exceeds 60 months, even though 15 years is allowed for shorter terms
related_policy:
  - Section 1 (Tier Structure Overview)
```

```yaml
exception_id: EX092
title: Private Sale Loan Size Capped Lower Than Standard ($150k vs $250k)
source_document: BFS Product Guide — Loan Size (Prime)
policy_statement: >
  "$5,000 – $250,000 standard loans. $5,000 – $150,000 private sales."
interpretation: >
  While standard (dealer-sourced) Prime loans can reach $250,000, private
  sale transactions are capped $100,000 lower, at $150,000 — regardless
  of the applicant's tier or credit strength.
business_rationale: >
  Consistent with the broader pattern across every lender in this
  catalog — private sale provenance/valuation risk is compensated by a
  lower maximum transaction size rather than (or in addition to) a rate
  loading (EX086).
examples:
  eligible:
    - Ultra Prime applicant, private sale vehicle, $140,000 -> eligible
  ineligible:
    - Ultra Prime applicant, private sale vehicle, $200,000 -> not
      eligible; exceeds the $150,000 private sale cap even though the
      standard cap ($250,000) would otherwise allow it
business_logic: |
  IF transaction_type == "private_sale":
    max_loan_size = MIN(tier_based_limit, $150,000)
  ELSE:
    max_loan_size = MIN(tier_based_limit, $250,000)
keywords:
  - private sale
  - loan size cap
  - $150,000
synonyms:
  private sale:
    - non-dealer purchase
intent_examples:
  - "What is the maximum loan size for a private sale vehicle?"
decision: Not Eligible above $150,000 for private sales, regardless of tier
related_policy:
  - EX086 (Private Sale Loading — stacks with this cap)
```

```yaml
exception_id: EX093
title: Loan Term May Be Reduced for Courier, Rideshare, or Rental Vehicles
source_document: BFS Product Guide — Loan Term (Prime)
policy_statement: >
  "12 – 84 months. May be reduced for courier, ride share or rental
  vehicles."
interpretation: >
  While the standard maximum term is 84 months, BFS reserves discretion
  to shorten the available term specifically for vehicles used for
  courier, rideshare, or rental purposes — the exact reduced term is not
  fixed in the guide and is assessed case-by-case.
business_rationale: >
  These use-cases involve much higher usage intensity (higher mileage,
  more wear) than standard personal/business use, accelerating
  depreciation and increasing mechanical risk — a shorter term reduces
  BFS's exposure to an asset that will age/wear faster than the standard
  84-month assumption would suggest.
examples:
  eligible:
    - Standard personal-use vehicle financed over 84 months -> eligible
  ineligible (i.e., term reduced):
    - Rideshare vehicle requesting an 84-month term -> may be reduced by
      BFS at its discretion; the full 84 months is not guaranteed for
      this use-case
business_logic: |
  IF vehicle_use IN {"courier", "rideshare", "rental"}:
    max_term_months = discretionary_reduced_term  # less than the standard 84-month maximum, case-by-case
  ELSE:
    max_term_months = 84
keywords:
  - courier
  - rideshare
  - rental vehicle
  - reduced term
synonyms:
  rideshare:
    - Uber
    - Ola
    - DiDi
intent_examples:
  - "Can I get an 84-month term for a rideshare vehicle?"
decision: Conditional — Term may be reduced below 84 months at BFS's discretion for courier/rideshare/rental use
related_policy:
  - Section 1 (Tier Structure Overview)
  - EX100 (Balloon Payments Excluded for Couriers/Rideshare)
```

```yaml
exception_id: EX094
title: High Value Loans ($250k–$400k) Restricted to Ultra Prime–Tier 2, Asset-Backed Only, 20% Minimum Deposit
source_document: BFS Product Guide — High Value Loans (Prime)
policy_statement: >
  "$250,000 – $400,000. Minimum deposit 20%. Asset-backed applicants
  only." Assessed on a case-by-case basis, with an acceptable vehicle.
  Not available for Tier 3, Tier 4, or BFS Plus.
interpretation: >
  Transactions above the standard $250,000 cap (up to $400,000) are only
  available to Ultra Prime, Tier 1, or Tier 2 applicants, and require
  BOTH a minimum 20% deposit AND asset-backed status — this is not
  available under any circumstances for Tier 3, Tier 4, or BFS Plus.
business_rationale: >
  Larger transaction sizes require the strongest available credit tiers
  and additional security (deposit + asset backing) to justify the
  increased exposure, and are explicitly excluded from the weaker tiers
  regardless of any compensating deposit they might offer.
examples:
  eligible:
    - Tier 1 applicant, asset-backed, 25% deposit, $350,000 vehicle ->
      eligible for case-by-case High Value Loan assessment
  ineligible:
    - Tier 3 applicant, asset-backed, 30% deposit, $300,000 vehicle -> not
      eligible; High Value Loans are not available for Tier 3 at all,
      regardless of deposit or asset-backed status
business_logic: |
  IF loan_amount > 250000 AND loan_amount <= 400000:
    IF tier IN {"Ultra Prime", "Tier 1", "Tier 2"} AND asset_backed == True AND deposit_pct >= 20%:
      eligible_for_case_by_case_review = True
    ELSE:
      not_eligible = True  # includes all Tier 3/4/BFS Plus applicants, regardless of deposit
keywords:
  - High Value Loans
  - $400,000
  - asset-backed
  - 20% deposit
synonyms:
  High Value Loans:
    - high value finance
intent_examples:
  - "Can a Tier 3 applicant access a $350,000 High Value Loan with a large deposit?"
decision: Not Eligible for Tier 3/4/BFS Plus under any circumstances; Ultra Prime–Tier 2 only, case-by-case
related_policy:
  - Section 1 (Tier Structure Overview)
```

```yaml
exception_id: EX095
title: Low Doc Restricted to Ultra Prime–Tier 2 (Commercial Only)
source_document: BFS Product Guide — Commercial Loans Supporting Documentation
policy_statement: >
  "Tier: Ultra Prime to Tier 2 only" [Low Doc]. Loan Size: up to $150,000
  (total exposure). Trading History: 2+ years (ABN + GST). Minimum
  Deposit: 0%.
interpretation: >
  Low Doc is available ONLY to Ultra Prime, Tier 1, or Tier 2 commercial
  applicants — Tier 3, Tier 4, and BFS Plus cannot access Low Doc under
  any circumstances, regardless of trading history or deposit offered.
business_rationale: >
  Reduced documentation relies on the applicant's strong credit profile
  as the primary risk mitigant in place of full financial verification;
  BFS reserves this pathway for its strongest tiers only.
examples:
  eligible:
    - Tier 2 applicant, 3 years trading history, ABN+GST registered ->
      eligible for Low Doc
  ineligible:
    - Tier 3 applicant, otherwise meeting all Low Doc criteria -> not
      eligible; Low Doc is not available below Tier 2 under any
      circumstances
business_logic: |
  IF product == "Low Doc" AND tier NOT IN {"Ultra Prime", "Tier 1", "Tier 2"}:
    not_eligible = True
keywords:
  - Low Doc
  - Tier 2
  - commercial only
synonyms:
  Low Doc:
    - low documentation
intent_examples:
  - "Can a Tier 3 applicant use Low Doc?"
decision: Not Eligible for Low Doc below Tier 2, and not available for consumer loans at all (commercial only)
related_policy:
  - Section 3 (Documentation Tiers)
```

```yaml
exception_id: EX096
title: New Business Ventures Not Available Under BFS Plus
source_document: BFS Product Guide — New Business Ventures / Commercial Loans Supporting Documentation
policy_statement: >
  "New Business Ventures: Available [Ultra Prime–Tier 2], Available
  [Tier 3/4], Not available" [BFS Plus]. Confirmed on page 4: "Tier:
  Ultra Prime to Tier 4 only" [New Business Ventures].
interpretation: >
  New Business Ventures (businesses trading less than 12 months) are
  supported across the entire Prime tier range (Ultra Prime through
  Tier 4), but this pathway is not available at all under BFS Plus.
business_rationale: >
  BFS Plus is likely designed around a different (potentially more
  standardised/simplified) risk assessment model than the Prime tiers,
  and does not extend to the higher-risk profile of a business trading
  less than 12 months.
examples:
  eligible:
    - Business trading 8 months, Tier 4 profile -> eligible for New
      Business Ventures assessment
  ineligible:
    - Business trading 8 months, applying under BFS Plus -> not eligible;
      New Business Ventures is not available under BFS Plus at all
business_logic: |
  IF trading_history_months < 12 AND product == "BFS Plus":
    not_eligible = True
  ELSE IF trading_history_months < 12 AND tier IN {"Ultra Prime", "Tier 1", "Tier 2", "Tier 3", "Tier 4"}:
    eligible_for_new_business_ventures_assessment = True
keywords:
  - New Business Ventures
  - BFS Plus
  - trading history
synonyms:
  New Business Ventures:
    - new business
    - startup finance
intent_examples:
  - "Can a new business apply under BFS Plus?"
decision: Not Eligible under BFS Plus regardless of trading history; available across all Prime tiers
related_policy:
  - Section 3 (Documentation Tiers)
```

```yaml
exception_id: EX097
title: BFS Plus Discharged Bankrupt/Insolvent Pathway (12+ Months Since Discharge, 20% Deposit)
source_document: BFS Product Guide — CCR History (BFS Plus)
policy_statement: >
  "Discharged bankrupt or insolvent: 20% deposit required, more than 12
  months since discharge, with no adverse history since."
interpretation: >
  Unlike the Prime tiers (where the Auto Decline Criteria — EX110 —
  automatically and irreversibly declines any currently bankrupt
  individual, with no mention of a discharged-bankrupt pathway), BFS Plus
  explicitly provides a pathway for PREVIOUSLY (discharged) bankrupt or
  insolvent applicants, provided discharge occurred more than 12 months
  ago, a 20% deposit is provided, and there has been no adverse credit
  history since discharge.
business_rationale: >
  Distinguishes between a CURRENT bankruptcy (an absolute decline trigger
  across the whole guide) and a DISCHARGED bankruptcy with a clean
  post-discharge track record, which BFS Plus is willing to accept with
  additional security (deposit) and a demonstrated recency/cleanliness
  requirement.
examples:
  eligible:
    - Applicant discharged from bankruptcy 18 months ago, no adverse
      history since, 20% deposit provided, applying under BFS Plus ->
      eligible
  ineligible:
    - Applicant discharged from bankruptcy 6 months ago -> not eligible;
      does not meet the 12-month recency requirement
    - Applicant currently bankrupt (not discharged) -> not eligible under
      any BFS product; this is an absolute auto-decline trigger (EX110)
business_logic: |
  IF bankruptcy_status == "currently_bankrupt":
    auto_decline = True  # applies across all BFS products, see EX110
  ELSE IF bankruptcy_status == "discharged":
    IF (months_since_discharge > 12) AND (deposit_pct >= 20%) AND (no_adverse_history_since_discharge == True):
      eligible_under_bfs_plus = True
    ELSE:
      not_eligible = True
keywords:
  - discharged bankrupt
  - insolvent
  - BFS Plus
  - 20% deposit
synonyms:
  discharged bankrupt:
    - former bankrupt
    - post-bankruptcy applicant
intent_examples:
  - "Can I apply for finance if I was discharged from bankruptcy 18 months ago?"
  - "Is there a difference between current and discharged bankruptcy for BFS Plus?"
decision: Conditional — Eligible under BFS Plus only if discharged >12 months ago, 20% deposit, no adverse history since
related_policy:
  - EX110 (Auto Decline Criteria — Currently Bankrupt, absolute exclusion)
```

```yaml
exception_id: EX098
title: 90-Day Bank Statements Mandatory for BFS Plus vs Conditional for Prime
source_document: BFS Product Guide — 90 Days Bank Statements
policy_statement: >
  Prime: "Consumer – On request only or where required for income
  evidence. Commercial – Full Doc/New Business Ventures loans under
  $100,000 for income evidence." BFS Plus: "Mandatory."
interpretation: >
  Under Prime, 90-day bank statements are only required conditionally
  (on request, or for specific commercial scenarios under $100,000).
  Under BFS Plus, providing 90 days of bank statements is mandatory for
  EVERY application, with no conditional exceptions.
business_rationale: >
  BFS Plus likely relies more heavily on transactional bank data as a
  core verification input (given it sits outside the standard Prime
  credit-tier assessment model), making this document non-negotiable
  rather than a conditional/on-request item.
examples:
  eligible:
    - BFS Plus application submitted without 90-day bank statements ->
      not eligible; application incomplete until provided
    - Prime consumer application where income is already well-evidenced
      by other means -> bank statements may not be requested at all
business_logic: |
  IF product == "BFS Plus":
    require(90_day_bank_statements_provided == True)  # always mandatory
  ELSE IF product == "Prime":
    require_bank_statements_conditionally  # on request, or specific Full Doc/NBV scenarios under $100k
keywords:
  - 90 days bank statements
  - BFS Plus
  - mandatory
synonyms:
  bank statements:
    - bank transaction information
intent_examples:
  - "Are bank statements always required for BFS Plus?"
decision: Mandatory for all BFS Plus applications; conditional (on request or specific scenarios) for Prime
related_policy:
  - Section 3 (Documentation Tiers)
```

```yaml
exception_id: EX099
title: Non-Resident Visa Holders — Lower Minimum Income for BFS Plus, But Low Doc Never Available
source_document: BFS Product Guide — Non-Resident Visa Holders
policy_statement: >
  Prime: "Minimum income $100,000. Loan term must end one month before
  visa expiry. Low doc not available." BFS Plus: "Minimum income
  $50,000. Loan term must end one month before visa expiry."
interpretation: >
  Non-resident visa holders face a LOWER minimum income requirement under
  BFS Plus ($50,000) than under Prime ($100,000) — but Prime explicitly
  states Low Doc is never available for visa holders regardless of
  income (BFS Plus doesn't offer Low Doc at all, so this restriction is
  moot for that product — see EX095).
business_rationale: >
  The lower BFS Plus income threshold likely reflects a different
  underlying risk model for that product, but the shared "loan term must
  end one month before visa expiry" rule across both products reflects a
  consistent underlying concern: BFS wants certainty that the loan
  concludes before the applicant's legal right to remain (and work, and
  service the loan) in Australia expires.
examples:
  eligible:
    - Non-resident visa holder, income $60,000, applying under BFS Plus,
      loan term ending 2 months before visa expiry -> eligible (meets the
      $50k threshold and the 1-month buffer requirement)
  ineligible:
    - Non-resident visa holder, income $60,000, applying under Prime ->
      not eligible; below the $100,000 Prime threshold (would need to
      apply under BFS Plus instead)
    - Non-resident visa holder, any income level, loan term ending after
      visa expiry -> not eligible under either product
business_logic: |
  IF applicant_status == "non_resident_visa_holder":
    require(loan_term_end_date <= visa_expiry_date - 1_month)  # applies to both products
    IF product == "Prime":
      require(income >= $100,000)
      not_eligible_for_low_doc = True  # regardless of income
    ELSE IF product == "BFS Plus":
      require(income >= $50,000)
keywords:
  - non-resident visa
  - minimum income
  - visa expiry
synonyms:
  non-resident visa holder:
    - temporary visa holder
    - overseas visa holder
intent_examples:
  - "What income do I need as a visa holder applying under BFS Plus vs Prime?"
  - "Can a visa holder use Low Doc?"
decision: Conditional — $50k minimum income under BFS Plus vs $100k under Prime; Low Doc never available to visa holders under Prime
related_policy:
  - EX095 (Low Doc Restricted to Ultra Prime–Tier 2 — BFS Plus doesn't offer Low Doc regardless)
```

```yaml
exception_id: EX100
title: Balloon Payments Not Available for Tier 3/4/BFS Plus, and Excludes Couriers/Rideshare
source_document: BFS Product Guide — Balloons
policy_statement: >
  "Balloons (Commercial only, excluding couriers and ride-share)" — table
  shows balloon percentages only for Ultra Prime/Tier 1/Tier 2; Tier 3/4
  and BFS Plus are marked "Not available."
interpretation: >
  Balloon payments are available only for commercial deals under Ultra
  Prime, Tier 1, or Tier 2 — never for Tier 3, Tier 4, or BFS Plus — and
  even within the eligible tiers, courier and rideshare vehicles are
  excluded from balloon structuring regardless of tier.
business_rationale: >
  Balloon payments rely on confident residual value forecasting, which
  BFS reserves for its strongest credit tiers; courier/rideshare vehicles
  are excluded due to their accelerated wear/depreciation (consistent
  with EX093's term-reduction rule for the same use-cases), making a
  residual value forecast unreliable regardless of the applicant's tier.
examples:
  eligible:
    - Tier 1 applicant, standard commercial (non-rideshare) vehicle,
      36-month term, 0-3 years old -> eligible for a 50% balloon
  ineligible:
    - Tier 3 applicant, otherwise identical scenario -> not eligible;
      balloons are not available for Tier 3 regardless of vehicle age/term
    - Tier 1 applicant, rideshare vehicle -> not eligible for a balloon,
      even though Tier 1 is otherwise balloon-eligible
business_logic: |
  IF tier IN {"Tier 3", "Tier 4", "BFS Plus"}:
    balloon_available = False
  ELSE IF vehicle_use IN {"courier", "rideshare"}:
    balloon_available = False  # regardless of tier
  ELSE IF tier IN {"Ultra Prime", "Tier 1", "Tier 2"} AND product == "Commercial":
    balloon_available = True  # percentage depends on vehicle age and term
keywords:
  - balloon payment
  - Tier 3
  - Tier 4
  - BFS Plus
  - rideshare exclusion
synonyms:
  balloon:
    - residual payment
intent_examples:
  - "Can a Tier 3 commercial loan have a balloon payment?"
  - "Is a balloon available for a rideshare vehicle under Tier 1?"
decision: Not Eligible for Tier 3/4/BFS Plus under any circumstances, and not eligible for courier/rideshare vehicles regardless of tier
related_policy:
  - EX093 (Loan Term May Be Reduced for Courier/Rideshare/Rental Vehicles)
```

```yaml
exception_id: EX101
title: Remote Area Lending Excluded Entirely for BFS Plus; Non-Asset-Backed Requires 20% Deposit in Remote Areas
source_document: BFS Product Guide — Remote Areas
policy_statement: >
  "Non-asset backed requires a 20% deposit" [Prime, remote areas]. BFS
  Plus: "Not available" [for remote areas generally].
interpretation: >
  Under Prime, remote-area lending (per the ABS 2021 Remoteness Area
  classification) is permitted, but non-asset-backed applicants in
  remote areas must provide a 20% deposit. Under BFS Plus, remote area
  lending is not available at all — no deposit-based workaround exists
  for BFS Plus in remote areas.
business_rationale: >
  Remote-area assets/security are generally harder to value, insure, and
  (if needed) repossess/resell, so Prime compensates via a deposit
  requirement for the weaker (non-asset-backed) security position, while
  BFS Plus — likely a more standardised, lower-touch product — excludes
  remote lending altogether rather than adding conditional deposit rules.
examples:
  eligible:
    - Prime applicant, non-asset-backed, remote area (not "Very Remote"),
      20% deposit provided -> eligible
  ineligible:
    - BFS Plus applicant in a remote area, any deposit level -> not
      eligible; remote area lending is unavailable under BFS Plus
    - Prime applicant, non-asset-backed, remote area, no deposit -> not
      eligible; the 20% deposit is mandatory for this scenario
business_logic: |
  IF area_classification == "remote" (per ABS 2021):
    IF product == "BFS Plus":
      not_eligible = True
    ELSE IF product == "Prime" AND asset_backed == False:
      require(deposit_pct >= 20%)
keywords:
  - remote area
  - BFS Plus
  - 20% deposit
synonyms:
  remote area:
    - ABS remoteness classification
intent_examples:
  - "Can BFS Plus lend in a remote area?"
  - "What deposit is needed for a non-asset-backed applicant in a remote area?"
decision: Not Eligible for BFS Plus in remote areas under any circumstances; Prime requires 20% deposit if non-asset-backed
related_policy:
  - EX102 (Very Remote Areas Excluded Entirely — all tiers)
```

```yaml
exception_id: EX102
title: Very Remote Areas Excluded Entirely (All Tiers)
source_document: BFS Product Guide — Remote Areas
policy_statement: >
  "Not available in 'Very Remote' areas."
interpretation: >
  Unlike standard "Remote" areas (which are financeable, subject to
  EX101's deposit conditions), properties/locations classified as "Very
  Remote" under the ABS 2021 Remoteness Area classification are excluded
  entirely — this applies across ALL tiers and products, with no
  deposit-based or discretionary override mentioned.
business_rationale: >
  "Very Remote" locations present the most extreme version of the
  valuation/insurability/repossession difficulties that justify the
  standard "Remote" deposit requirement — sufficiently extreme that BFS
  does not offer any pathway to accept these deals at all.
examples:
  eligible:
    - Standard "Remote" area (not "Very Remote"), Prime, 20% deposit if
      non-asset-backed -> eligible (per EX101)
  ineligible:
    - "Very Remote" area classification, any tier, any deposit level ->
      not eligible under any circumstances
business_logic: |
  IF area_classification == "very_remote" (per ABS 2021 Remoteness Area):
    not_eligible = True  # absolute exclusion, all tiers, no deposit override
keywords:
  - very remote
  - ABS remoteness area
  - absolute exclusion
synonyms:
  very remote:
    - extremely remote location
intent_examples:
  - "Is there any way to get finance approved in a Very Remote area?"
decision: Not Eligible — absolute exclusion for Very Remote areas, no override available at any tier
related_policy:
  - EX101 (Remote Area Lending — contrast with standard Remote areas, which ARE financeable)
```

```yaml
exception_id: EX103
title: Private Sale Requires DoxAI/Redbook Vehicle Inspection Report and Arm's-Length Transaction
source_document: BFS Product Guide — Private Sales
policy_statement: >
  "Vehicle inspection report required – DoxAI Asset Verification via
  DoxAI Portal (preferred) or Redbook. Must be an arm's length
  transaction."
interpretation: >
  Every private sale requires BOTH a formal vehicle inspection report
  (via the DoxAI Portal, BFS's preferred method, or Redbook as an
  alternative) AND confirmation that the transaction is at arm's length
  (i.e. not between related parties who might manipulate the sale price).
business_rationale: >
  Directly addresses the two core private-sale risks also seen at other
  lenders in this catalog: verifying the asset's actual condition/value
  (via the inspection report) and preventing related-party transactions
  that could disguise an inflated or artificial sale price.
examples:
  eligible:
    - Private sale between unrelated parties, DoxAI inspection report
      provided -> meets the baseline requirement (additional Private Sale
      requirements document conditions may also apply)
  ineligible:
    - Private sale between family members (not arm's length) -> not
      eligible, regardless of inspection report
    - Private sale with no inspection report via DoxAI or Redbook -> not
      eligible; this is a mandatory document, not optional
business_logic: |
  IF transaction_type == "private_sale":
    require(inspection_report_via_DoxAI_or_Redbook == True)
    require(arms_length_transaction == True)
keywords:
  - private sale
  - DoxAI
  - Redbook
  - arm's length
synonyms:
  DoxAI:
    - DoxAI Asset Verification
    - DoxAI Portal
intent_examples:
  - "Can I buy a car privately from a family member?"
  - "Is a Redbook valuation acceptable instead of DoxAI?"
decision: Not Eligible without both a DoxAI/Redbook inspection report and confirmed arm's-length status
related_policy:
  - EX086 (Private Sale Loading)
  - EX092 (Private Sale Loan Size Cap)
```

```yaml
exception_id: EX104
title: Interlock-Condition Licences Not Accepted (Hard Exclusion)
source_document: BFS Product Guide — Driver Licence Types
policy_statement: >
  "Licences with interlock conditions are not accepted."
interpretation: >
  Applicants/guarantors/borrowers holding a driver's licence with an
  alcohol interlock condition (typically imposed following a drink-
  driving offence) are excluded outright — this is a flat exclusion, not
  a risk factor to be priced via a loading.
business_rationale: >
  An interlock condition indicates a relatively recent serious driving
  offence and an ongoing legal restriction on driving, which BFS treats
  as an unacceptable risk factor for vehicle finance regardless of the
  applicant's other credit strength.
examples:
  eligible:
    - Standard, unrestricted driver's licence -> meets this requirement
  ineligible:
    - Applicant holds a licence with an interlock condition, even with an
      otherwise excellent CCR score -> not eligible under this criterion,
      regardless of tier
business_logic: |
  IF any_borrower_or_guarantor_licence_has_interlock_condition == True:
    not_eligible = True  # hard exclusion, applies across all tiers/products
keywords:
  - interlock condition
  - driver licence
  - exclusion
synonyms:
  interlock condition:
    - alcohol interlock
    - drink driving restriction
intent_examples:
  - "Can I get finance if my licence has an interlock condition?"
decision: Not Eligible — hard exclusion, no exceptions across any tier
related_policy:
  - Section 5 (Driver Licence Types requirements generally)
```

```yaml
exception_id: EX105
title: Australian Learner Licence Accepted Only With a Co-Borrower, Passenger Vehicles Only
source_document: BFS Product Guide — Driver Licence Types
policy_statement: >
  "Australian learner licence accepted with co-borrower (passenger
  vehicles only)."
interpretation: >
  A learner's licence is only acceptable if the application includes a
  co-borrower (i.e. the learner cannot be the sole applicant), AND only
  for passenger vehicles — not commercial vehicles, motorcycles, or any
  other asset category.
business_rationale: >
  A learner driver represents materially higher risk (both financially
  and in terms of asset condition/accident risk); requiring a co-borrower
  provides a secondary responsible party, and restricting to passenger
  vehicles keeps the exposure to the most standardised, lowest-risk asset
  category.
examples:
  eligible:
    - Learner licence holder, passenger vehicle, co-borrower with a full
      licence included on the application -> eligible
  ineligible:
    - Learner licence holder applying alone (no co-borrower) -> not
      eligible, regardless of vehicle type
    - Learner licence holder with a co-borrower, applying for a
      commercial vehicle or motorcycle -> not eligible; restricted to
      passenger vehicles only
business_logic: |
  IF primary_applicant_licence_type == "learner":
    require(co_borrower_present == True)
    require(asset_type == "passenger_vehicle")
keywords:
  - learner licence
  - co-borrower
  - passenger vehicles
synonyms:
  learner licence:
    - provisional learner permit
intent_examples:
  - "Can a learner driver apply for vehicle finance alone?"
  - "Is a learner licence accepted for a commercial vehicle loan?"
decision: Not Eligible without a co-borrower, and not eligible at all outside passenger vehicles
related_policy:
  - EX104 (Interlock-Condition Licences Not Accepted)
```

```yaml
exception_id: EX106
title: Loan Exclusions — Debt Consolidation, Cash Raising, Sale & Buyback, Sale & Leaseback, Mid-Term Refinancing All Prohibited
source_document: BFS Product Guide — Loan Exclusions
policy_statement: >
  "Debt consolidation, cash raising, top-up loans, sale and buyback, sale
  and leaseback, and mid-term refinancing."
interpretation: >
  BFS excludes six specific loan purposes/structures entirely — this is a
  purpose-based exclusion list, separate from the asset-type exclusions
  seen elsewhere. None of these six can be financed under any BFS
  product, at any tier.
business_rationale: >
  Each of these purposes represents a use of vehicle finance for
  something other than acquiring a vehicle asset (raising cash, paying
  off other debts, or restructuring an existing facility mid-term),
  which falls outside BFS's core vehicle-asset-finance product design and
  carries different (often higher) risk characteristics than a
  straightforward vehicle purchase.
examples:
  eligible:
    - Standard new vehicle purchase, dealer or private sale -> eligible
  ineligible:
    - Applicant wants to consolidate credit card debt into a new vehicle
      loan -> not eligible (debt consolidation excluded)
    - Applicant wants "extra cash" beyond the vehicle price added to the
      loan -> not eligible (cash raising / top-up excluded)
    - Applicant wants to refinance an existing BFS loan partway through
      its term for a better rate -> not eligible (mid-term refinancing
      excluded)
business_logic: |
  IF loan_purpose IN {"debt_consolidation", "cash_raising", "top_up_loan",
                        "sale_and_buyback", "sale_and_leaseback", "mid_term_refinancing"}:
    not_eligible = True  # applies across all tiers and products
keywords:
  - debt consolidation
  - cash raising
  - top-up loan
  - sale and buyback
  - sale and leaseback
  - mid-term refinancing
synonyms:
  cash raising:
    - equity release
    - extra cash
  top-up loan:
    - loan increase
intent_examples:
  - "Can I add extra cash to my vehicle loan for other expenses?"
  - "Can I refinance my current BFS loan halfway through the term for a better rate?"
decision: Not Eligible for any of the six listed purposes/structures, across all tiers
related_policy:
  - None specific — this is a standalone, universal exclusion list
```

```yaml
exception_id: EX107
title: Motorcycles Capped at 60 Months With No Balloon (Overriding the Standard 84-Month/Balloon-Eligible Norm)
source_document: BFS Product Guide — Additional Requirements (Motorcycles)
policy_statement: >
  "Maximum term 60 months, no balloons" [Motorcycles].
interpretation: >
  While the standard Prime loan term can reach 84 months (with balloons
  available for eligible tiers — EX100), motorcycles are specifically
  capped at a maximum 60-month term with no balloon option at all,
  overriding both the general term and balloon rules for this asset
  category.
business_rationale: >
  Motorcycles have a different depreciation/risk profile (and generally
  shorter practical lending horizons) than cars, so BFS applies a
  tighter, motorcycle-specific term cap and removes balloon flexibility
  entirely for this asset type.
examples:
  eligible:
    - Motorcycle financed over 48 months, fully amortised -> eligible
  ineligible:
    - Motorcycle financed over 72 months -> exceeds the 60-month
      motorcycle-specific cap, even though 72 months would be within the
      general 84-month maximum for other vehicle types
    - Motorcycle financed over 60 months WITH a balloon payment -> not
      eligible; balloons are not available for motorcycles at all
business_logic: |
  IF asset_type == "motorcycle":
    require(loan_term_months <= 60)
    require(balloon_payment == 0)
keywords:
  - motorcycle
  - 60 months
  - no balloon
synonyms:
  motorcycle:
    - motorbike
intent_examples:
  - "Can I get a 72-month term for a motorcycle?"
  - "Is a balloon available on a motorcycle loan?"
decision: Not Eligible above 60 months, and no balloon option available at all, for motorcycles
related_policy:
  - EX100 (Balloon Payments Not Available for Tier 3/4/BFS Plus, and Excludes Couriers/Rideshare)
  - EX108 (Electric Motorcycles Must Exceed 80km/h Top Speed)
```

```yaml
exception_id: EX108
title: Electric Motorcycles Must Exceed 80km/h Top Speed
source_document: BFS Product Guide — Additional Requirements (Motorcycles)
policy_statement: >
  "Electric motorcycles acceptable, maximum speed must be over 80km/hr."
interpretation: >
  Electric motorcycles are eligible, but ONLY if their maximum speed
  exceeds 80km/h — this excludes lower-powered electric mopeds/scooters
  that top out at or below that speed, even though they are technically
  "electric motorcycles."
business_rationale: >
  Sets a minimum performance threshold to distinguish genuine
  motorcycles (comparable to petrol-powered equivalents in capability and
  use-case) from lower-powered electric mopeds/scooters, which may have a
  different resale market, regulatory classification, or use-case profile
  that BFS does not intend to include under this policy.
examples:
  eligible:
    - Electric motorcycle with a top speed of 110km/h -> eligible
  ineligible:
    - Electric moped/scooter with a top speed of 60km/h -> not eligible;
      does not exceed the 80km/h threshold, even though it may be
      marketed as an "electric motorcycle"
business_logic: |
  IF asset_type == "electric_motorcycle":
    require(max_speed_kmh > 80)
keywords:
  - electric motorcycle
  - top speed
  - 80km/h
synonyms:
  electric motorcycle:
    - e-motorcycle
    - electric moped (if speed qualifies)
intent_examples:
  - "Can I finance an electric scooter that only goes 60km/h?"
  - "Is there a minimum speed requirement for electric motorcycles?"
decision: Not Eligible for electric motorcycles with a top speed at or below 80km/h
related_policy:
  - EX107 (Motorcycles Capped at 60 Months With No Balloon)
```

```yaml
exception_id: EX109
title: Caravans/Campervans/Camper Trailers Restricted to Leisure Use Unless Accountant Letter Confirms Business Use
source_document: BFS Product Guide — Additional Requirements (Caravans, Campervans, Camper Trailers)
policy_statement: >
  "Leisure use only (not to be used as a residence). Commercial requires
  a letter from an accountant confirming business use."
interpretation: >
  The default assumption for caravans/campervans/camper trailers is
  leisure use, and they explicitly cannot be used as a residence. If the
  applicant wants to finance one for commercial/business use instead, an
  accountant's letter confirming genuine business use is required as a
  condition of eligibility.
business_rationale: >
  Prevents these asset types from being financed as a disguised
  residential/accommodation solution (which would carry very different
  risk and regulatory characteristics than vehicle finance), while still
  allowing a legitimate commercial-use pathway with independent
  (accountant-verified) confirmation.
examples:
  eligible:
    - Caravan financed for standard leisure/holiday use -> eligible, no
      accountant letter needed
    - Camper trailer financed for a mobile business (e.g. a mobile
      catering trailer), with an accountant's letter confirming business
      use -> eligible
  ineligible:
    - Caravan intended to be used as the applicant's primary residence ->
      not eligible under any circumstances (this is an absolute
      exclusion, not resolved by an accountant's letter)
    - Camper trailer for commercial use, but no accountant's letter
      provided -> not eligible; the letter is a mandatory condition for
      commercial use of this asset type
business_logic: |
  IF asset_type IN {"caravan", "campervan", "camper_trailer"}:
    IF intended_use == "residence":
      not_eligible = True  # absolute exclusion, no override
    ELSE IF intended_use == "commercial":
      require(accountant_letter_confirming_business_use == True)
    # else (leisure use) -> eligible by default, no extra letter needed
keywords:
  - caravan
  - campervan
  - camper trailer
  - leisure use
  - residence exclusion
synonyms:
  camper trailer:
    - travel trailer
intent_examples:
  - "Can I use a financed caravan as my permanent home?"
  - "What do I need to provide to finance a camper trailer for business use?"
decision: Not Eligible for residential use under any circumstances; commercial use requires an accountant's letter
related_policy:
  - EX089 (Tier 4/BFS Plus Restricted to Passenger & Light Commercial Only — caravans not available at those tiers regardless)
```

```yaml
exception_id: EX110
title: Auto Decline Criteria — No Resubmission Available
source_document: BFS Product Guide — Auto Decline Criteria
policy_statement: >
  "Applications will be automatically declined (with no resubmission
  available) where: All individuals and guarantors have a CCR score of
  less than 400 (consumer + commercial new/demo), or 550 (commercial
  used); Any individual who is currently bankrupt; Consumer applications
  where the net monthly income is less than $2,318 per month."
interpretation: >
  These three triggers cause an AUTOMATIC decline with explicitly NO
  resubmission pathway — unlike most other exceptions in this catalog
  (which route to a different tier/product or require additional
  documents), meeting any one of these three conditions ends the
  application entirely, with no way to reapply or restructure around it.
business_rationale: >
  Sets an absolute floor below which BFS considers an application
  fundamentally unviable (either a credit score too low even for the most
  accessible tier, an active bankruptcy that represents unmanaged
  insolvency, or income too low to service even a modest facility) —
  distinguishing this from the "discharged bankrupt" pathway (EX097),
  which explicitly IS resubmittable/eligible under BFS Plus given time and
  conditions.
examples:
  eligible:
    - All individuals/guarantors CCR >= 400 (or >=550 for commercial
      used), none currently bankrupt, consumer net monthly income >=
      $2,318 -> proceeds to normal tiered assessment
  ineligible:
    - Any individual or guarantor with CCR 380 -> automatic decline, no
      resubmission
    - Any individual currently (not discharged) bankrupt -> automatic
      decline, no resubmission (contrast with EX097's discharged-bankrupt
      pathway, which IS available)
    - Consumer applicant with net monthly income of $2,000 -> automatic
      decline, no resubmission
business_logic: |
  IF ANY(individual_or_guarantor_ccr < 400 for consumer/commercial_new_demo)
     OR ANY(individual_or_guarantor_ccr < 550 for commercial_used)
     OR ANY(individual_currently_bankrupt)
     OR (product == "Consumer" AND net_monthly_income < 2318):
    auto_decline = True
    resubmission_available = False  # final, no workaround
keywords:
  - auto decline
  - no resubmission
  - minimum income
  - CCR floor
synonyms:
  auto decline:
    - automatic decline
    - hard decline
intent_examples:
  - "Can I resubmit if my application was automatically declined?"
  - "What is the absolute minimum credit score BFS will consider?"
decision: Not Eligible, final — no resubmission pathway exists once any auto-decline trigger is met
related_policy:
  - EX097 (BFS Plus Discharged Bankrupt/Insolvent Pathway — contrast, this IS available for discharged bankrupts)
```

```yaml
exception_id: EX111
title: Low Doc Requires Guarantor to Be Australian Citizen/PR Only (No Visa Holders)
source_document: BFS Product Guide — Commercial Loans Supporting Documentation (Residency)
policy_statement: >
  "Guarantor must be an Australian citizen or permanent resident only"
  [Low Doc]. Contrast with Full Doc/New Business Ventures: "Loan term
  must end one month before visa expiry" (implying visa holders ARE
  accepted under those pathways, subject to term conditions).
interpretation: >
  Non-resident visa holders cannot act as guarantors under Low Doc at
  all — this is a stricter residency requirement than Full Doc or New
  Business Ventures, which accommodate visa holders (with the term-end
  condition per EX099) rather than excluding them entirely.
business_rationale: >
  Low Doc already relies on reduced documentation as its core risk
  mitigant; adding the uncertainty of a non-permanent residency status
  would compound risk beyond what BFS is willing to accept without full
  supporting documentation, hence Low Doc restricts to citizens/PRs only.
examples:
  eligible:
    - Australian citizen or permanent resident guarantor, applying under
      Low Doc -> eligible
  ineligible:
    - Non-resident visa holder guarantor, applying under Low Doc -> not
      eligible under Low Doc; the applicant would need to apply under
      Full Doc instead (subject to EX099's visa-related conditions)
business_logic: |
  IF product == "Low Doc" AND guarantor_residency_status NOT IN {"citizen", "permanent_resident"}:
    not_eligible = True  # must use Full Doc or New Business Ventures instead
keywords:
  - Low Doc
  - guarantor residency
  - visa holder exclusion
synonyms:
  permanent resident:
    - PR
    - Australian PR
intent_examples:
  - "Can a visa holder be a guarantor under Low Doc?"
decision: Not Eligible for Low Doc if the guarantor is a non-resident visa holder — must use Full Doc instead
related_policy:
  - EX095 (Low Doc Restricted to Ultra Prime–Tier 2)
  - EX099 (Non-Resident Visa Holders — Full Doc pathway)
```

```yaml
exception_id: EX112
title: Commercial Loans to Individuals (ABN Holders) Require Business-Use Confirmation
source_document: BFS Product Guide — Commercial Loans to Individuals (ABN holders only)
policy_statement: >
  "Vehicle must be for business use, confirmed by letter from an
  accountant or tax returns."
interpretation: >
  Where a commercial loan is made to an individual (rather than a
  company/trust entity) who holds an ABN, the vehicle must genuinely be
  for business use — and this must be independently confirmed via either
  an accountant's letter or the applicant's tax returns, not simply
  self-declared.
business_rationale: >
  Individuals with an ABN could otherwise use commercial (potentially
  more favourable or differently structured) pricing for what is really a
  personal-use vehicle; requiring third-party confirmation (accountant
  or tax returns) reduces the risk of commercial finance being accessed
  under false pretences.
examples:
  eligible:
    - Sole trader with an ABN, accountant's letter confirming the vehicle
      is used for business deliveries -> eligible for commercial pricing
  ineligible:
    - Individual with an ABN, no accountant letter or supporting tax
      return evidence of business use -> not eligible for commercial
      pricing; would need to apply as a standard consumer loan instead
business_logic: |
  IF applicant_type == "individual_with_ABN" AND loan_type == "commercial":
    require(business_use_confirmed_by_accountant_letter OR tax_returns_showing_business_use)
keywords:
  - ABN holder
  - business use
  - accountant letter
synonyms:
  ABN holder:
    - sole trader
intent_examples:
  - "Do I need to prove business use if I have an ABN but want commercial pricing?"
decision: Not Eligible for commercial pricing without accountant/tax-return confirmation of business use
related_policy:
  - Section 3 (Documentation Tiers)
```

```yaml
exception_id: EX113
title: Early Termination Fee (Commercial) Reduced to 15% If Refinancing With BFS
source_document: BFS Product Guide — Fees and Charges (Early termination fee – Commercial)
policy_statement: >
  "35% of the amount of interest payable for the remainder of the term,
  or 15% of the amount of interest payable for the remainder of the term
  if repayment is due to you refinancing with us."
interpretation: >
  The standard commercial early termination fee is 35% of remaining
  interest, but this is reduced to just 15% if the reason for early
  repayment is that the customer is REFINANCING WITH BFS itself (as
  opposed to paying out the loan for any other reason, e.g. selling the
  vehicle, refinancing elsewhere, or simply repaying early from cash
  flow).
business_rationale: >
  Rewards customer retention — if the customer is staying with BFS (just
  restructuring into a new facility), BFS loses less future revenue than
  if the customer leaves entirely, so the exit penalty is reduced
  accordingly, functioning as a loyalty/retention incentive.
examples:
  eligible:
    - Commercial customer pays out their loan early specifically to
      refinance into a new BFS facility -> 15% early termination fee
      applies
  ineligible (i.e., the higher 35% applies):
    - Commercial customer pays out their loan early to refinance with a
      different lender -> 35% early termination fee applies (the reduced
      15% rate does not apply)
business_logic: |
  IF early_repayment_reason == "refinancing_with_BFS":
    early_termination_fee_pct = 15%  # of remaining interest
  ELSE:
    early_termination_fee_pct = 35%  # of remaining interest
keywords:
  - early termination fee
  - refinancing
  - commercial
synonyms:
  early termination:
    - early payout
    - loan payout
intent_examples:
  - "Is the early termination fee lower if I refinance with BFS instead of leaving?"
decision: Conditional — 15% fee only if refinancing with BFS itself; 35% otherwise
related_policy:
  - Section 4 (Fees & Commission Summary)
```

```yaml
exception_id: EX114
title: Commission Clawback — 100% Refundable on Repossession/Write-Off Within 24 Months (Longer Window Than the Standard 12-Month Clawback)
source_document: BFS Product Guide — Commission and Clawback Terms
policy_statement: >
  "All commissions and incentives on all consumer and commercial
  contracts are fully refundable to Branded Financial Services if the
  contract is terminated or paid in full within the first 12 months...
  Where a repossession occurs or a loan is written off within 24 months,
  100% of the commission is refundable to Branded Financial Services."
interpretation: >
  The GENERAL commission clawback window is 12 months (for early
  termination or payout in full). However, for the SPECIFIC triggers of
  repossession or loan write-off, the clawback window is extended to 24
  months — twice as long as the standard window.
business_rationale: >
  Repossession/write-off events reflect a materially worse outcome for
  BFS than a simple early payout (representing an actual credit loss
  rather than just lost future interest), so BFS extends the window
  during which it can reclaim commission for these more severe outcomes,
  holding brokers accountable for a longer period on the loans they
  originate.
examples:
  eligible (broker keeps commission):
    - Loan performs normally, no repossession/write-off, and isn't paid
      out/terminated within 12 months -> commission is retained by the
      broker permanently
  ineligible (commission clawed back):
    - Loan is written off in month 18 -> since this falls within the
      24-month repossession/write-off window (even though it's beyond
      the standard 12-month general clawback window), 100% of the
      commission is still refundable to BFS
    - Loan is paid out in full in month 10 (no repossession/write-off
      involved) -> falls within the standard 12-month clawback window;
      100% refundable
business_logic: |
  IF (loan_terminated_or_paid_in_full == True) AND (months_since_origination <= 12):
    commission_clawback_pct = 100%
  ELSE IF (repossession_occurred OR loan_written_off) AND (months_since_origination <= 24):
    commission_clawback_pct = 100%  # extended window for these specific triggers
  ELSE:
    commission_clawback_pct = 0%  # commission retained
keywords:
  - commission clawback
  - repossession
  - loan write-off
  - 24 months
synonyms:
  clawback:
    - commission refund
    - commission recovery
intent_examples:
  - "How long is the commission clawback period if a loan is repossessed?"
  - "Is the clawback window the same for early payout as for repossession?"
decision: Conditional — 12-month clawback window for general termination/payout; extended to 24 months specifically for repossession/write-off
related_policy:
  - Section 4 (Fees & Commission Summary)
```

```yaml
exception_id: EX115
title: Origination Fee Added to the Loan and Paid to the Introducer
source_document: BFS Product Guide — Fees and Charges (Origination fee)
policy_statement: >
  "$1,650 (maximum). Added to the loan and paid to the introducer."
interpretation: >
  Unlike a typical lender-retained fee, the origination fee (up to
  $1,650) is added to the customer's loan balance and then paid OUT to
  the introducer (broker) — it is a broker-facing fee mechanism financed
  through the loan itself, not a fee BFS keeps or a separate upfront
  out-of-pocket cost to the customer.
business_rationale: >
  Allows the introducer to be compensated for origination work without
  requiring the customer to pay this amount upfront in cash — it is
  capitalised into the loan, spreading the cost over the loan term
  alongside the principal and interest.
examples:
  eligible:
    - $1,500 origination fee added to the loan balance, paid to the
      introducer at settlement -> standard mechanism, within the $1,650 cap
  ineligible:
    - Origination fee of $2,000 -> exceeds the $1,650 maximum
business_logic: |
  IF origination_fee_requested <= 1650:
    origination_fee = capitalised_into_loan_balance
    origination_fee_recipient = "introducer"
  ELSE:
    not_eligible = True  # exceeds the $1,650 cap
keywords:
  - origination fee
  - introducer payment
  - capitalised fee
synonyms:
  origination fee:
    - broker origination fee
intent_examples:
  - "Does the origination fee get paid upfront or added to my loan?"
  - "Who receives the origination fee?"
decision: Capped at $1,650; capitalised into the loan and paid to the introducer, not retained by BFS or paid upfront by the customer
related_policy:
  - Section 4 (Fees & Commission Summary)
```

---

*Compiled from the Branded Financial Services (BFS) Product Guide (Broker), effective 1 July 2026. This document
is a standalone deep-dive reference intended to sit alongside, and be cross-referenced with, the Resimac and Metro
Detailed References and the multi-lender Exceptions Catalog (Westpac / CFAL / Resimac / Metro). Verify all figures
against BFS's live QuickSell platform before operational use, and consult your BDM for scenarios outside these
criteria.*
