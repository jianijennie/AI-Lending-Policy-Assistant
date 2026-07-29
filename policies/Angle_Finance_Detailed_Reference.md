# Angle Finance — Detailed Policy Reference & Exceptions Catalog

> Source: Angle Finance Rate Card (April 2026, Version 02.04.26), Start-Up Product Flyer (Jan 2026), Full Doc —
> Minimum Requirements Product Update, and Prime Movers Product Flyer (May 2026).
> Purpose: A standalone deep-dive reference (parallel to the Resimac, Metro, and BFS references) covering Angle's
> A/A+ profile structure, Low/Mid/Full Doc tiers, Prime Movers, Start-Up product, rate mechanics, and fees — with
> all exception clauses listed separately in Section 5, using the same `exception_id` / `keywords` / `synonyms` /
> `intent_examples` / `decision` / `related_policy` schema as the other lenders' catalogs. IDs continue from
> EX118 onward.

---

## 1. Structure Overview

Angle prices commercial asset finance through two overlapping frameworks:

| Framework | What it drives |
|---|---|
| **A / A+ Profile** | A quick-reference rate summary for two headline customer profiles (see Section 2) |
| **Rate Card (by EOT × Property Status)** | The actual base rate table, driven by asset category (Primary/Secondary/Tertiary/Prime Movers/Start-Up) and End of Term (EOT) |
| **Documentation Tier (Low Doc / Mid Doc / Full Doc)** | Which supporting documents are required, scaled by applicant exposure/loan size |

Angle also runs two dedicated product lines with their own eligibility rules: **Start-Up** (ABN <2 years) and
**Prime Movers** (heavy vehicle finance for established fleet operators).

## 2. A / A+ Profile Comparison

| | A Profile | A+ Profile |
|---|---|---|
| ABN / GST | 8+ years ABN, 4+ years GST | 4+ years ABN, 2+ years GST |
| Asset types | Primary assets only | Primary & Secondary assets |
| Asset age | New assets (YOM 2023) | — |
| Max EOT | (follows standard Primary rate card, up to 25 years) | **10 years** (see EX121) |
| Entity types | Sole traders, Company, Trust, Partnership | Sole traders, Company, Trust, Partnership |
| Property backed rate | 7.79% | 8.29% |
| Non-property backed rate | 8.79% | 9.29% |

## 3. Documentation Tiers

| | Low Doc <$100k | Low Doc $100k–$250k | Mid Doc <$500k | Full Doc |
|---|---|---|---|---|
| ABN | 2+ years | 2+ years | 2+ years | (varies) |
| GST | Not essential | 1+ years | 1+ years | (varies) |
| Credit Score (Veda 1:1) | 550+ (Corp & Individual) | 550+ Corp / 600+ Individual | 650+ (Individual & Corp) | (per financial assessment) |
| Property Status | Property backed OR **Non-Property Owner** | Property backed only | Property backed only | Property backed only |
| Credit References | Not essential | Asset Finance Credit Reference or Mortgage Statements | Asset Finance Credit Reference or Mortgage Statements | Full financials |
| Max EOT | Primary 25yrs / Secondary 15yrs / Tertiary 10yrs | Primary 25yrs / Secondary 15yrs / Tertiary N/A | Primary 25yrs / Secondary 15yrs / Tertiary 10yrs | Per asset category |

## 4. Fees Summary

| Fee | Amount |
|---|---|
| Establishment Fee (Dealer or Private Sale) | $649, financed into the loan or direct debit at settlement |
| Account Keeping Fee | $4.95 monthly or $1 weekly |
| Brokerage | Up to 8% (incl. GST) |
| Origination fee | Up to $1,400 (incl. GST), capitalised within the loan |

---

## 5. Exceptions Catalog (Angle Finance)

```yaml
exception_id: EX118
title: $400K Low Doc Excludes Sole Traders (Unlike Standard Low Doc Tiers)
source_document: Angle Finance Rate Card — $400K Low Doc Checklist
policy_statement: >
  "Exclusions: Sole traders" (listed under the $400K Low Doc Checklist).
interpretation: >
  The new $400K Low Doc product does not accept sole traders as
  applicants — this is a product-specific exclusion; sole traders remain
  eligible under the standard Low Doc <$100k, Low Doc $100k–$250k, and
  Mid Doc tiers (Section 3), which list "Sole traders, Company, Trust,
  Partnership" as accepted entity types generally.
business_rationale: >
  The $400K threshold represents a much larger exposure than standard
  Low Doc tiers; Angle likely considers a sole trader structure (with no
  separation between personal and business liability/assets) an
  unacceptable risk profile at this transaction size under reduced
  documentation.
examples:
  eligible:
    - Company entity, otherwise meeting all $400K Low Doc criteria -> eligible
  ineligible:
    - Sole trader entity applying for $400K Low Doc, otherwise meeting all
      other criteria -> not eligible; sole traders are excluded from this
      specific product regardless of credit score or trading history
business_logic: |
  IF product == "$400K Low Doc" AND entity_type == "sole_trader":
    not_eligible = True
keywords:
  - $400K Low Doc
  - sole trader
  - exclusion
synonyms:
  sole trader:
    - individual trader
    - unincorporated business
intent_examples:
  - "Can a sole trader apply for the $400K Low Doc product?"
decision: Not Eligible — sole traders excluded from $400K Low Doc specifically
related_policy:
  - Section 3 (Documentation Tiers)
  - EX138 (Prime Movers Excludes Both Sole Traders and Individual Partnerships)
```

```yaml
exception_id: EX119
title: $400K Low Doc Excludes Tertiary Assets, Prime Movers, and Buses
source_document: Angle Finance Rate Card — $400K Low Doc Checklist
policy_statement: >
  "Exclusions: ... Tertiary assets. Prime Movers. Buses."
interpretation: >
  Even though the $400K Low Doc product accepts "Primary & Secondary"
  asset types generally, three specific categories are carved out
  entirely: Tertiary assets, Prime Movers, and Buses — none of these can
  be financed under this product, regardless of the applicant's
  strength.
business_rationale: >
  Prime Movers and Buses each carry elevated risk/valuation profiles that
  Angle addresses through dedicated products with their own tailored
  criteria (see EX124/EX138/EX139 for Prime Movers) rather than the
  general-purpose $400K Low Doc pathway; Tertiary assets are already the
  lowest-liquidity category across Angle's asset hierarchy (10-year EOT
  cap even under other Low Doc/Mid Doc tiers).
examples:
  eligible:
    - Excavator (Primary asset) financed under $400K Low Doc -> eligible
  ineligible:
    - Prime Mover financed under $400K Low Doc -> not eligible; must use
      the dedicated Prime Movers product (Mid Doc or Full Doc only, see
      EX139) instead
    - Bus financed under $400K Low Doc -> not eligible
business_logic: |
  IF product == "$400K Low Doc" AND asset_category IN {"Tertiary", "Prime Mover", "Bus"}:
    not_eligible = True
keywords:
  - $400K Low Doc
  - Tertiary assets
  - Prime Movers
  - Buses
synonyms:
  Tertiary assets:
    - lowest liquidity asset tier
intent_examples:
  - "Can I finance a bus under the $400K Low Doc product?"
  - "Are Prime Movers eligible for $400K Low Doc?"
decision: Not Eligible for Tertiary assets, Prime Movers, or Buses under $400K Low Doc
related_policy:
  - EX124 (Prime Movers Carry a 1% Rate Loading)
  - EX139 (Prime Movers Not Available Under Low Doc)
```

```yaml
exception_id: EX120
title: $400K Low Doc Credit Reference Must Be From a Named List of Angle-Accepted Lenders
source_document: Angle Finance Rate Card — Credit Reference Definitions
policy_statement: >
  "To qualify for $400K Low Doc your credit reference must be from an
  Angle accepted lender: Westpac / Capital Finance, NAB, ANZ, CBA, BOQ,
  Judo, DLL, Suncorp, Bendigo / Adelaide Bank, Macquarie Bank, Flexi
  Commercial, Metro Finance, Pepper Money, Toyota Finance."
interpretation: >
  Unlike the general "Tier 1 / Tier 2 Asset Finance Provider" wording
  used elsewhere in the $400K Low Doc checklist, this is a closed,
  NAMED list of specific lenders — a credit reference from any other
  asset finance provider not on this list does not satisfy the $400K Low
  Doc credit reference requirement, even if that provider would
  otherwise be considered reputable.
business_rationale: >
  Ensures the credit reference comes from lenders whose reporting/
  conduct standards Angle has already vetted and trusts, reducing the
  risk of relying on a reference from an unfamiliar or less rigorous
  credit provider for a reduced-documentation, high-value ($400K)
  transaction.
examples:
  eligible:
    - 12-month clean asset finance reference from Macquarie Bank -> meets
      the $400K Low Doc credit reference requirement
  ineligible:
    - 12-month clean asset finance reference from a lender not on the
      named list -> does not satisfy the $400K Low Doc requirement, even
      if the reference itself is otherwise strong
business_logic: |
  IF product == "$400K Low Doc":
    require(credit_reference_lender IN {"Westpac", "Capital Finance", "NAB", "ANZ", "CBA",
                                          "BOQ", "Judo", "DLL", "Suncorp", "Bendigo/Adelaide Bank",
                                          "Macquarie Bank", "Flexi Commercial", "Metro Finance",
                                          "Pepper Money", "Toyota Finance"})
keywords:
  - $400K Low Doc
  - credit reference
  - accepted lender list
synonyms:
  Angle accepted lender:
    - approved credit reference lender
intent_examples:
  - "Does my client's credit reference from [lender] count for $400K Low Doc?"
decision: Not Eligible for $400K Low Doc unless the credit reference comes from the named lender list
related_policy:
  - EX129 (Asset Finance Credit Reference Must Cover at Least 50% of the New Finance Amount)
```

```yaml
exception_id: EX121
title: A+ Profile Caps End of Term at 10 Years (Shorter Than the Standard 25-Year Primary Asset Allowance)
source_document: Angle Finance Rate Card — A+ Profile
policy_statement: >
  "End of term 10 years" [A+ Profile], compared with the standard Rate
  Card, which allows Primary assets up to 25 years EOT.
interpretation: >
  The A+ Profile — despite unlocking Secondary assets on top of Primary
  (which A Profile does not offer) — caps the maximum End of Term at
  just 10 years, far shorter than the 25-year EOT otherwise available
  for Primary assets under the general Rate Card.
business_rationale: >
  The A+ Profile trades a lower ABN/GST tenure requirement (4+/2+ years
  vs A Profile's 8+/4+ years) and broader asset-type access (Primary &
  Secondary) for a shorter maximum term — Angle compensates for the
  slightly weaker business-tenure profile and broader asset scope by
  limiting how far into the future the loan (and its residual risk)
  extends.
examples:
  eligible:
    - A+ Profile applicant, Primary asset, 8-year EOT -> eligible
  ineligible:
    - A+ Profile applicant, Primary asset, 20-year EOT -> not eligible
      under the A+ Profile terms; would need to qualify under the A
      Profile (or the general Rate Card) instead, which allows up to 25
      years
business_logic: |
  IF customer_profile == "A+":
    max_EOT_years = 10
  ELSE IF customer_profile == "A" OR general_rate_card_assessment:
    max_EOT_years = 25 (Primary) / 15 (Secondary) / 10 (Tertiary)
keywords:
  - A+ Profile
  - End of Term
  - 10 years
synonyms:
  A+ Profile:
    - A-plus profile
intent_examples:
  - "Can an A+ Profile deal have a 20-year EOT?"
  - "Why is the A+ Profile term shorter than the standard Primary asset rate card?"
decision: Not Eligible above 10 years EOT under the A+ Profile, even though standard Primary assets allow up to 25 years
related_policy:
  - Section 2 (A / A+ Profile Comparison)
```

```yaml
exception_id: EX122
title: No Rate Loading for Private Sales, Business Continuity, Commission up to 8%, or Spousal Property (Angle-Wide Policy)
source_document: Angle Finance Rate Card — "Here's the best angle!"
policy_statement: >
  "Here's the best angle! No rate loading for: Private sales; Business
  continuity; Commission up to 8%; Property in spouse's name."
interpretation: >
  Angle explicitly does NOT apply a rate loading for four factors that
  attract loadings at essentially every other lender in this catalog —
  private sale transactions, business continuity concerns, broker
  commission up to the full 8% cap, and property backing held in a
  spouse's name. This is a genuine point of differentiation worth
  flagging clearly, since assuming a private-sale loading (as would be
  correct for Westpac, Resimac, Metro, or BFS) would be an ERROR when
  applied to Angle.
business_rationale: >
  Positioned as a competitive differentiator ("the best angle") — Angle
  chooses to absorb these risk factors within its standard pricing
  rather than pricing them individually via loadings, likely as a market
  positioning/broker-attraction strategy.
examples:
  eligible:
    - Private sale transaction, Angle base rate applies with NO
      additional loading -> correct treatment
    - Broker commission set at 8% (the maximum), no rate impact -> correct
      treatment
  ineligible (i.e., incorrect assumption):
    - Assuming a private sale loading applies at Angle (as it would at
      other lenders in this catalog) -> INCORRECT; Angle's policy is the
      opposite of the private-sale-loading norm seen elsewhere
business_logic: |
  IF lender == "Angle Finance":
    IF trigger IN {"private_sale", "business_continuity", "commission_up_to_8pct", "spousal_property"}:
      rate_loading = 0%  # explicitly no loading, unlike most other lenders in this catalog
keywords:
  - no rate loading
  - private sale
  - business continuity
  - spousal property
  - commission
synonyms:
  no rate loading:
    - loading-free
    - no surcharge
intent_examples:
  - "Does Angle charge extra for private sales like other lenders do?"
  - "Is there a loading for property in my spouse's name at Angle?"
decision: Not Applicable — no loading for these four factors at Angle, in contrast to standard industry practice at other lenders in this catalog
related_policy:
  - Section 2 (A / A+ Profile Comparison)
  - Cross-lender note: contrast with Westpac EX002, Resimac Section 1.1, Metro EX057, BFS EX086 (all of which DO apply private sale loadings)
```

```yaml
exception_id: EX123
title: A+ Deals Receive Priority Assessment (2-Hour Average Turnaround)
source_document: Angle Finance Rate Card — A+ Profile box
policy_statement: >
  "A+ deals receive priority assessment with an average turnaround time
  of 2 hours."
interpretation: >
  This is a service-level commitment tied specifically to the A+
  Profile — deals structured to meet A+ criteria are assessed faster
  (2-hour average) than standard submissions, which is a genuine
  operational benefit of structuring a deal to qualify as A+ rather than
  A or a standard Rate Card submission.
business_rationale: >
  Rewards brokers/customers who meet the more specific A+ profile
  criteria with faster processing, incentivising well-packaged, complete
  applications that fit this profile.
examples:
  eligible:
    - Deal meeting A+ Profile criteria (4+ year ABN, 2+ year GST, Primary
      & Secondary assets, strong credit score) -> eligible for the 2-hour
      priority assessment turnaround
  ineligible:
    - Standard Rate Card submission not meeting A+ Profile criteria -> not
      eligible for the priority 2-hour turnaround; standard assessment
      timeframes apply
business_logic: |
  IF customer_profile == "A+":
    assessment_priority = "priority"  # average 2-hour turnaround
  ELSE:
    assessment_priority = "standard"
keywords:
  - A+ Profile
  - priority assessment
  - turnaround time
synonyms:
  priority assessment:
    - fast-track assessment
intent_examples:
  - "How fast is assessment for an A+ deal compared to a standard deal?"
decision: Applicable only to deals meeting A+ Profile criteria
related_policy:
  - Section 2 (A / A+ Profile Comparison)
```

```yaml
exception_id: EX124
title: Prime Movers Carry a 1% Rate Loading Over Standard Primary Asset Rates
source_document: Angle Finance Rate Card / Prime Movers Product Flyer
policy_statement: >
  "*1% rate loading applies to standard primary asset rates. See Pg. 4
  for qualifying criteria" [Rate Card]; "A 1% rate loading will apply to
  standard primary asset rates" [Prime Movers flyer and Qualifying
  Criteria].
interpretation: >
  Prime Mover pricing (starting from 9.39%/8.99% depending on the
  document) is not an independently set rate — it is the standard
  Primary asset rate PLUS a 1% loading. This is confirmed consistently
  across both the Rate Card and the dedicated Prime Movers flyer.
business_rationale: >
  Reflects the elevated risk/specialised resale market for prime movers
  (consistent with the same asset category at Resimac and Metro in this
  catalog), priced as a margin add-on to the existing Primary asset
  curve rather than a fully separate rate table.
examples:
  eligible:
    - Standard Primary asset rate 8.39% (10yr EOT, property owner) -> Prime
      Mover equivalent = 9.39%
  ineligible (i.e., miscalculation):
    - Assuming Prime Mover rates are set independently of the Primary
      asset table -> incorrect; always calculate as Primary rate + 1%
business_logic: |
  IF asset_type == "Prime Mover":
    applicable_rate = corresponding_primary_asset_rate + 1%
keywords:
  - Prime Movers
  - 1% loading
  - Primary asset rate
synonyms:
  Prime Movers:
    - prime mover trucks
    - truck tractors
intent_examples:
  - "How is the Prime Mover rate calculated?"
decision: Conditional — Prime Mover rate = standard Primary asset rate + 1% loading
related_policy:
  - EX138 (Prime Movers Excludes Both Sole Traders and Individual Partnerships)
  - EX139 (Prime Movers Not Available Under Low Doc)
```

```yaml
exception_id: EX125
title: Tertiary Assets Capped at 10-Year Maximum EOT (No 15/20/25-Year Options)
source_document: Angle Finance Rate Card — Rate Card table
policy_statement: >
  Rate Card shows Tertiary assets priced only at the "10 years (EOT)"
  column (11.85%/17.85%); the 15/20/25-year EOT columns show "–" (not
  available) for Tertiary assets.
interpretation: >
  Tertiary assets are the most term-restricted category in Angle's asset
  hierarchy — no EOT beyond 10 years is available at all, compared with
  Secondary assets (up to 15 years) and Primary assets (up to 25 years,
  or 20 years with a NEW pricing point).
business_rationale: >
  Consistent with the broader industry pattern in this catalog (Metro,
  Resimac) — the least liquid, most specialised asset category gets the
  shortest permissible term, reflecting the least confidence in
  long-term residual value.
examples:
  eligible:
    - Tertiary asset financed with a 10-year EOT -> eligible, priced at
      11.85% (property owner) or 17.85% (non-property owner)
  ineligible:
    - Tertiary asset financed with a 15-year EOT -> not eligible; no rate
      is published for Tertiary beyond 10 years
business_logic: |
  IF asset_category == "Tertiary" AND EOT_years > 10:
    not_eligible = True  # no rate available beyond 10 years
keywords:
  - Tertiary assets
  - EOT
  - 10 years
synonyms:
  Tertiary assets:
    - lowest liquidity asset category
intent_examples:
  - "Can I get a 15-year EOT on a Tertiary asset?"
decision: Not Eligible for Tertiary assets beyond a 10-year EOT
related_policy:
  - Section 1 (Structure Overview)
```

```yaml
exception_id: EX126
title: Total Exposure Capped by Credit Score Band (500/550/650 Thresholds)
source_document: Angle Finance Rate Card — Total Exposure
policy_statement: >
  "Credit score determines total exposure: 500 = <$150,000; 550 =
  <$250,000; 650 = >$250,000."
interpretation: >
  A customer's total exposure ceiling with Angle is directly gated by
  their credit score band, independent of any other factor (asset type,
  property backing, documentation tier) — a 500-score customer cannot
  exceed $150,000 in total exposure no matter how strong their other
  credentials are, and so on up the bands.
business_rationale: >
  Provides a simple, credit-score-driven ceiling on aggregate risk per
  customer, ensuring exposure scales with the most fundamental risk
  indicator (credit score) as a backstop across all other product-
  specific rules.
examples:
  eligible:
    - Customer with a 560 credit score, total exposure request of
      $220,000 -> eligible (within the <$250,000 band for 550+)
  ineligible:
    - Customer with a 510 credit score, total exposure request of
      $200,000 -> not eligible; capped at <$150,000 for the 500 band,
      regardless of asset type or property backing
business_logic: |
  IF credit_score >= 650:
    max_total_exposure = "unlimited (>$250,000, subject to other criteria)"
  ELSE IF credit_score >= 550:
    max_total_exposure = $250,000
  ELSE IF credit_score >= 500:
    max_total_exposure = $150,000
  ELSE:
    not_eligible = True  # see EX132, credit scores <500 not accepted at all
keywords:
  - total exposure
  - credit score band
  - exposure cap
synonyms:
  total exposure:
    - aggregate exposure
intent_examples:
  - "What is the maximum exposure for a 550 credit score customer?"
decision: Conditional — Total exposure capped strictly by credit score band, independent of other factors
related_policy:
  - EX127 (Large Ticket Deals Over $500,000 Get Credit Score Flexibility)
  - EX133 (Credit Scores Below 500 Not Accepted)
```

```yaml
exception_id: EX127
title: Large Ticket Deals Over $500,000 Get Credit Score Flexibility With Financial Assessment
source_document: Angle Finance Rate Card — Total Exposure
policy_statement: >
  "Large ticket deals over $500,000+ have credit score flexibility.
  Credit scores <650 can be considered with financial assessment. Speak
  to your BDM to determine if your customer profile qualifies."
interpretation: >
  While the standard exposure bands (EX126) would otherwise require a
  650+ score for any exposure above $250,000, deals specifically over
  $500,000 introduce a discretionary override — scores below 650 CAN
  still be considered, but only with additional financial assessment and
  BDM sign-off, not as an automatic entitlement.
business_rationale: >
  Recognises that very large transactions often come with additional
  supporting evidence/strength (e.g. substantial assets, established
  operations) that a credit score alone doesn't capture, so Angle
  provides a manual override pathway rather than a hard score-based
  decline for this specific size band.
examples:
  eligible:
    - $600,000 deal, customer credit score 610, additional financial
      assessment completed and BDM approval obtained -> may be eligible
      despite being below the standard 650 threshold
  ineligible:
    - $300,000 deal, customer credit score 610 -> does NOT qualify for
      this flexibility; the deal falls below the $500,000 threshold
      where this override applies, so the standard 550-band cap
      ($250,000 max) applies instead
business_logic: |
  IF total_exposure > 500000 AND credit_score < 650:
    eligible_subject_to_financial_assessment_and_bdm_approval = True  # discretionary, not automatic
  ELSE IF total_exposure <= 500000:
    apply_standard_credit_score_exposure_bands  # see EX126
keywords:
  - large ticket deals
  - credit score flexibility
  - BDM approval
synonyms:
  large ticket deals:
    - large transactions
intent_examples:
  - "Can a 600 credit score customer get a $600,000 deal approved?"
decision: Conditional — Discretionary BDM-approved pathway for scores <650 only above $500,000; not available below that threshold
related_policy:
  - EX126 (Total Exposure Capped by Credit Score Band)
```

```yaml
exception_id: EX128
title: Second Low Doc Loan Requires First Loan to Have Run 6 Months With Good Conduct
source_document: Angle Finance Rate Card — Account Conduct With Angle
policy_statement: >
  "For multiple low doc deals, please ensure your applicants first loan
  has been running with Angle for 6 months with good account conduct. If
  your applicant's loan has been running for less then <6 months & they
  would like to be considered for a second low doc loan, please speak to
  your BDM."
interpretation: >
  A customer cannot automatically stack a second Low Doc facility on top
  of a first — the first Low Doc loan must have been running for at
  least 6 months with good conduct before a second Low Doc application is
  processed normally. If the first loan is younger than 6 months, the
  second application requires BDM discretion rather than standard
  processing.
business_rationale: >
  Prevents a customer from rapidly accumulating multiple reduced-
  documentation facilities before Angle has any track record of their
  repayment conduct, ensuring at least one demonstrated period of good
  conduct before extending further Low Doc credit.
examples:
  eligible:
    - First Low Doc loan running 8 months with good conduct, applicant
      applies for a second Low Doc loan -> eligible for standard
      processing
  ineligible (requires BDM):
    - First Low Doc loan running 3 months, applicant applies for a second
      Low Doc loan -> not eligible for standard processing; must speak
      to BDM for discretionary consideration
business_logic: |
  IF applicant_has_existing_low_doc_loan == True:
    IF months_running(existing_loan) >= 6 AND conduct == "good":
      second_low_doc_application_standard_processing = True
    ELSE:
      require(bdm_discretionary_approval)
keywords:
  - multiple Low Doc
  - account conduct
  - second loan
synonyms:
  Low Doc:
    - low documentation
intent_examples:
  - "Can a customer get a second Low Doc loan after only 2 months?"
decision: Conditional — Standard processing only if the first Low Doc loan has run 6+ months with good conduct; otherwise requires BDM approval
related_policy:
  - Section 3 (Documentation Tiers)
```

```yaml
exception_id: EX129
title: Asset Finance Credit Reference Must Cover at Least 50% of the New Finance Amount
source_document: Angle Finance Rate Card — Credit Reference Definitions
policy_statement: >
  "Asset finance Credit Reference: Loan running 6 months+, 50%+ of
  finance amount & no missed repayments."
interpretation: >
  A qualifying asset finance credit reference must satisfy three
  conditions simultaneously: the referenced loan must have been running
  for 6+ months, the referenced loan amount must be at least 50% of the
  NEW finance amount being applied for, and there must be no missed
  repayments on it.
business_rationale: >
  Ensures the credit reference is genuinely comparable in scale to the
  new facility — a small prior loan (e.g. $10,000) would not be a
  meaningful reference for a much larger new facility (e.g. $200,000),
  so the 50% threshold keeps the reference proportionate.
examples:
  eligible:
    - Prior asset finance loan of $120,000, running 8 months, no missed
      repayments, applied toward a new $200,000 facility -> eligible (60%
      of new amount, exceeds the 50% threshold)
  ineligible:
    - Prior asset finance loan of $50,000, running 8 months, no missed
      repayments, applied toward a new $200,000 facility -> not eligible;
      only 25% of the new finance amount, below the 50% threshold
business_logic: |
  IF credit_reference_type == "asset_finance":
    require(loan_running_months >= 6)
    require(referenced_loan_amount >= 0.5 * new_finance_amount)
    require(missed_repayments == 0)
keywords:
  - asset finance credit reference
  - 50% threshold
  - comparable reference
synonyms:
  asset finance credit reference:
    - comparable credit reference
intent_examples:
  - "Does a $50,000 prior loan count as a reference for a $200,000 new facility?"
decision: Not Eligible as a valid reference unless it covers at least 50% of the new finance amount, in addition to the 6-month/no-missed-repayments conditions
related_policy:
  - EX120 (Credit Reference Must Be From a Named Lender List — $400K Low Doc specific)
  - EX130 (Spouse's Mortgage Statements Not Accepted)
```

```yaml
exception_id: EX130
title: Spouse's Mortgage Statements Not Accepted as Credit Reference (Despite Spousal Property Being Accepted as Security)
source_document: Angle Finance Rate Card — Credit Reference Definitions / Property Ownership
policy_statement: >
  "Mortgage Statements: Loan running 6+ months & no missed repayments.
  Must be in applicants name, spouses mortgage statements not accepted."
interpretation: >
  There is an important internal distinction: spousal PROPERTY is
  explicitly accepted as asset-backed security (with marriage
  certificate/Medicare card/joint utility bill as evidence — see EX135),
  but spousal MORTGAGE STATEMENTS specifically are NOT accepted as a
  credit reference — the mortgage statement must be in the applicant's
  own name.
business_rationale: >
  Property backing and credit reference serve different purposes:
  property backing is about the SECURITY behind the loan (where
  ownership/equity is what matters), while a mortgage statement as a
  credit reference is about DEMONSTRATED REPAYMENT CONDUCT — Angle wants
  that conduct evidence to be the applicant's own repayment history, not
  a family member's, even if the underlying property can be shared.
examples:
  eligible:
    - Applicant provides their own 8-month mortgage statement with no
      missed repayments -> valid credit reference
  ineligible:
    - Applicant has no mortgage in their own name, submits their spouse's
      mortgage statement instead -> not eligible as a credit reference,
      even though spousal property itself could separately be used as
      security
business_logic: |
  IF credit_reference_type == "mortgage_statement":
    require(mortgage_is_in_applicants_own_name == True)  # spouse's mortgage statement explicitly rejected
    require(loan_running_months >= 6)
    require(missed_repayments == 0)
keywords:
  - mortgage statement
  - spouse
  - credit reference
synonyms:
  mortgage statement:
    - home loan statement
intent_examples:
  - "Can I use my spouse's mortgage statement as a credit reference?"
  - "Is spousal property treated the same as a spousal mortgage statement?"
decision: Not Eligible — spouse's mortgage statements are rejected as a credit reference, even though spousal property is accepted as security (contrast with EX135)
related_policy:
  - EX135 (Spousal Property Requires Specific Relationship Evidence)
  - EX129 (Asset Finance Credit Reference Must Cover at Least 50%)
```

```yaml
exception_id: EX131
title: Credit Files Younger Than 12 Months Cannot Be Considered
source_document: Angle Finance Rate Card — Credit File
policy_statement: >
  "Credit files <12 months can not be considered."
interpretation: >
  If an applicant's credit file is younger than 12 months old (i.e. they
  have a very limited/recent credit history), the application cannot be
  considered at all — this is an absolute exclusion, not a factor to be
  weighed alongside other strengths.
business_rationale: >
  A credit file under 12 months provides insufficient history to assess
  genuine repayment behaviour and risk, so Angle sets a hard floor on
  credit file age rather than relying on a thin/recent file even if other
  aspects of the application are strong.
examples:
  eligible:
    - Applicant with a credit file 18 months old -> meets this requirement
  ineligible:
    - Applicant with a credit file only 8 months old, otherwise strong
      application -> not eligible; cannot be considered under any Angle
      product
business_logic: |
  IF credit_file_age_months < 12:
    not_eligible = True  # absolute exclusion across all products
keywords:
  - credit file age
  - 12 months
  - not accepted
synonyms:
  credit file:
    - credit history
intent_examples:
  - "Can an applicant with an 8-month credit file be considered?"
decision: Not Eligible — absolute exclusion for credit files under 12 months old
related_policy:
  - EX133 (Credit Scores Below 500 Not Accepted)
```

```yaml
exception_id: EX132
title: Financial Defaults Excluded Except Telco/Utilities Up to $2,500
source_document: Angle Finance Rate Card — Not Accepted Applicants / Assets
policy_statement: >
  "Financial defaults on credit files (paid/unpaid), except telco or
  utilities (paid up to $2,500)."
interpretation: >
  Financial defaults on a credit file are generally an exclusion trigger
  regardless of whether they have since been paid or remain unpaid.
  However, there is a specific carve-out: telco or utility defaults ARE
  tolerated, provided they have been PAID and do not exceed $2,500.
business_rationale: >
  Telco/utility defaults are considered a materially lower-risk signal
  than a financial (credit/loan) default — often reflecting minor
  billing disputes or oversights rather than genuine credit
  unreliability — so Angle carves out a specific tolerance for these,
  provided they're both paid and below a modest dollar threshold.
examples:
  eligible:
    - Applicant has a paid $800 telco default on file, no other defaults
      -> eligible (within the $2,500 telco/utility carve-out)
  ineligible:
    - Applicant has a paid $3,000 telco default -> not eligible; exceeds
      the $2,500 carve-out threshold
    - Applicant has any financial (loan/credit) default, paid or unpaid
      -> not eligible; this carve-out applies ONLY to telco/utilities, not
      financial defaults generally
business_logic: |
  IF default_type == "financial" (loan/credit):
    not_eligible = True  # regardless of paid/unpaid status
  ELSE IF default_type IN {"telco", "utilities"}:
    IF default_status == "paid" AND default_amount <= 2500:
      eligible = True
    ELSE:
      not_eligible = True
keywords:
  - financial default
  - telco default
  - utilities default
  - $2,500 carve-out
synonyms:
  financial default:
    - credit default
    - loan default
intent_examples:
  - "Does a paid telco default disqualify an applicant?"
  - "What's the threshold for an acceptable utility default?"
decision: Not Eligible for any financial default; conditionally eligible for telco/utility defaults only if paid and ≤$2,500
related_policy:
  - EX131 (Credit Files Younger Than 12 Months Cannot Be Considered)
```

```yaml
exception_id: EX133
title: Credit Scores Below 500 Not Accepted
source_document: Angle Finance Rate Card — Not Accepted Applicants / Assets
policy_statement: >
  "Applicants with credit scores <500."
interpretation: >
  A credit score below 500 is an absolute floor across Angle's entire
  product suite — no product or discretionary pathway accommodates a
  score below this threshold (contrast with EX127, which allows
  discretion for scores as low as, implicitly, whatever floor the
  financial assessment supports above $500,000 exposure — but nothing in
  the guide overrides this absolute <500 floor).
business_rationale: >
  Sets the fundamental credit floor below which Angle considers an
  applicant simply not viable, regardless of transaction size,
  documentation tier, or other compensating factors.
examples:
  eligible:
    - Applicant with a credit score of 510 -> may be viable under Low Doc
      <$100k (which has a 550 threshold, so still needs to check tier-
      specific minimums) or other tiers, subject to their specific
      thresholds
  ineligible:
    - Applicant with a credit score of 480 -> not accepted under any
      Angle product
business_logic: |
  IF credit_score < 500:
    not_eligible = True  # absolute floor across all products
keywords:
  - credit score
  - 500 floor
  - not accepted
synonyms:
  credit score:
    - Veda score
intent_examples:
  - "Is there any Angle product that accepts a credit score below 500?"
decision: Not Eligible — absolute floor of 500, no exceptions across any product
related_policy:
  - EX126 (Total Exposure Capped by Credit Score Band)
  - EX131 (Credit Files Younger Than 12 Months Cannot Be Considered)
```

```yaml
exception_id: EX134
title: Taxi and Uber Drivers Not Accepted
source_document: Angle Finance Rate Card — Not Accepted Applicants / Assets
policy_statement: >
  "Taxi & Uber drivers."
interpretation: >
  Unlike some other lenders in this catalog (e.g. Metro, which accepts
  rideshare/taxi applicants subject to property-backing and exposure
  caps — EX040), Angle excludes taxi and Uber drivers entirely, with no
  conditional pathway mentioned.
business_rationale: >
  Reflects Angle's risk appetite choice to avoid the high-usage-
  intensity, higher-wear risk profile associated with rideshare/taxi use
  altogether, rather than pricing it in via a loading or restricting it
  to a specific tier (as Metro does).
examples:
  eligible:
    - Standard business-use or personal-use applicant -> eligible
      (subject to other criteria)
  ineligible:
    - Uber driver applicant, even with strong credit score and property
      backing -> not eligible under any Angle product
business_logic: |
  IF applicant_occupation IN {"taxi_driver", "uber_driver", "rideshare_driver"}:
    not_eligible = True  # absolute exclusion, no conditional pathway
keywords:
  - taxi driver
  - Uber driver
  - rideshare exclusion
synonyms:
  rideshare driver:
    - Uber driver
    - taxi driver
intent_examples:
  - "Can an Uber driver get vehicle finance from Angle?"
decision: Not Eligible — absolute exclusion, no conditional pathway (contrast with Metro's conditional rideshare acceptance, EX040)
related_policy:
  - Cross-lender note: contrast with Metro EX040 (Taxi/Uber/Rideshare Must Be Property Backed — a conditional pathway, not an absolute exclusion)
```

```yaml
exception_id: EX135
title: Spousal Property Requires Specific Relationship Evidence (Marriage Certificate, Medicare Card, or Joint Utility Bill)
source_document: Angle Finance Rate Card — Property Ownership
policy_statement: >
  "Spousal property is accepted as asset backed. Marriage certificate,
  Medicare card or joint utility bill required to support evidence of
  relationship."
interpretation: >
  Spousal property IS accepted as security (unlike Resimac's approach,
  which only allows it to waive a deposit — see the Resimac reference),
  but this acceptance is conditional on providing ONE of three specific
  documents to evidence the marital/relationship status: a marriage
  certificate, a Medicare card (showing both names), or a joint utility
  bill.
business_rationale: >
  Requires independent verification of the relationship before relying
  on a third party's (spouse's) property as security, to prevent
  misrepresentation of an unrelated third party's property as
  "spousal."
examples:
  eligible:
    - Applicant provides a marriage certificate confirming the
      relationship to the property owner -> spousal property accepted as
      security
  ineligible:
    - Applicant claims spousal property backing but provides none of the
      three accepted evidence documents -> not eligible; spousal property
      cannot be relied upon without this evidence
business_logic: |
  IF security_type == "spousal_property":
    require(evidence_document IN {"marriage_certificate", "Medicare_card", "joint_utility_bill"})
keywords:
  - spousal property
  - marriage certificate
  - relationship evidence
synonyms:
  spousal property:
    - spouse-owned property
intent_examples:
  - "What documents prove a spousal relationship for property backing?"
decision: Not Eligible as security without one of the three specified evidence documents
related_policy:
  - EX130 (Spouse's Mortgage Statements Not Accepted — contrast, property vs credit reference treatment)
```

```yaml
exception_id: EX136
title: Boarders and Mid-Term Refinance Require Mid Doc or Full Doc (Low Doc Not Available)
source_document: Angle Finance Rate Card — Property Ownership
policy_statement: >
  "Boarders & mid-term refinance require mid doc or full doc
  assessment."
interpretation: >
  Two specific scenarios — applicants who are boarders (renting a room
  rather than the whole property, or living in someone else's home
  without formal tenancy) and mid-term refinance transactions — are
  excluded from Low Doc processing entirely, regardless of credit score
  or other Low Doc-qualifying factors.
business_rationale: >
  Boarders lack the clearer property/tenancy relationship that supports
  reduced-documentation assessment, and mid-term refinances (restructuring
  an existing facility partway through its term) introduce complexity
  that warrants fuller financial verification than Low Doc provides.
examples:
  eligible:
    - Boarder applicant assessed under Mid Doc or Full Doc -> eligible
      (subject to those tiers' specific criteria)
  ineligible:
    - Boarder applicant attempting to apply under Low Doc <$100k, even
      with a 600+ credit score -> not eligible under Low Doc; must be
      assessed under Mid Doc or Full Doc instead
business_logic: |
  IF applicant_status == "boarder" OR transaction_type == "mid_term_refinance":
    not_eligible_for_low_doc = True
    require(documentation_tier IN {"Mid Doc", "Full Doc"})
keywords:
  - boarder
  - mid-term refinance
  - Low Doc exclusion
synonyms:
  boarder:
    - lodger
    - room renter
intent_examples:
  - "Can a boarder apply under Low Doc?"
  - "Is mid-term refinancing available under Low Doc?"
decision: Not Eligible for Low Doc — boarders and mid-term refinance require Mid Doc or Full Doc assessment
related_policy:
  - Section 3 (Documentation Tiers)
```

```yaml
exception_id: EX137
title: Start-Up Loan Cap of $150,000 Is Inclusive of Brokerage
source_document: Angle Finance Start-Up Flyer — Quick Qualifying Checklist
policy_statement: >
  "Loans to a maximum of $150,000, including brokerage."
interpretation: >
  The $150,000 Start-Up loan cap is not just the financed asset amount —
  brokerage is counted WITHIN that $150,000 ceiling, not added on top of
  it. This means the effective maximum asset finance amount is somewhat
  less than $150,000 once brokerage is factored in.
business_rationale: >
  Keeps the total customer obligation (asset finance + brokerage)
  strictly capped at $150,000 for this higher-risk (ABN <2 years)
  product, rather than allowing brokerage to push total exposure beyond
  the intended ceiling.
examples:
  eligible:
    - $140,000 asset finance + $8,000 brokerage = $148,000 total -> within
      the $150,000 cap
  ineligible:
    - $148,000 asset finance + $8,000 brokerage = $156,000 total -> exceeds
      the $150,000 cap; brokerage must be factored into the total, not
      added separately
business_logic: |
  IF product == "Start-Up":
    require((asset_finance_amount + brokerage_amount) <= 150000)
keywords:
  - Start-Up
  - $150,000 cap
  - brokerage inclusive
synonyms:
  Start-Up:
    - new business product
intent_examples:
  - "Is brokerage included in the $150,000 Start-Up cap, or added on top?"
decision: Not Eligible if total (asset finance + brokerage) exceeds $150,000 — brokerage is inclusive, not additional
related_policy:
  - Section 4 (Fees Summary)
  - EX146 (Start-Up Credit Score Discrepancy Between Rate Card and Flyer)
```

```yaml
exception_id: EX138
title: Prime Movers Excludes Both Sole Traders and Individual Partnerships (Broader Than the $400K Low Doc Exclusion)
source_document: Angle Finance Prime Movers Flyer — Exclusions
policy_statement: >
  "No Sole traders or Individual Partnerships" [Prime Movers exclusions],
  compared with the Qualifying Criteria: "Company & Trust only."
interpretation: >
  Prime Movers is restricted to Company or Trust entity types only —
  this is a BROADER exclusion than the $400K Low Doc product (EX118),
  which excludes sole traders but does not mention Individual
  Partnerships. For Prime Movers, neither sole traders NOR individual
  partnerships (as distinct from company/trust structures) are accepted
  under any circumstances.
business_rationale: >
  Prime Movers targets well-established fleet operators; Company and
  Trust structures typically reflect more established, formalised
  businesses with clearer succession/continuity and asset ownership
  structures than sole trader or individual partnership arrangements,
  aligning with the product's "well-established business" positioning
  (reinforced by the 5+ year ABN/GST requirement).
examples:
  eligible:
    - Company entity, 6 years ABN & GST, applying for Prime Movers ->
      eligible (entity type criterion met)
  ineligible:
    - Individual partnership (not a company or trust), even with 6+ years
      ABN & GST and strong credit -> not eligible for Prime Movers under
      any circumstances
    - Sole trader -> not eligible for Prime Movers (also excluded from
      $400K Low Doc per EX118, but Prime Movers additionally excludes
      individual partnerships, which $400K Low Doc does not mention)
business_logic: |
  IF product == "Prime Movers" AND entity_type NOT IN {"Company", "Trust"}:
    not_eligible = True  # excludes sole traders AND individual partnerships
keywords:
  - Prime Movers
  - sole trader exclusion
  - individual partnership exclusion
  - Company and Trust only
synonyms:
  individual partnership:
    - partnership (non-corporate)
intent_examples:
  - "Can an individual partnership apply for Prime Movers finance?"
decision: Not Eligible for Prime Movers unless the entity type is Company or Trust — sole traders and individual partnerships both excluded
related_policy:
  - EX118 ($400K Low Doc Excludes Sole Traders — narrower exclusion, doesn't mention partnerships)
```

```yaml
exception_id: EX139
title: Prime Movers Not Available Under Low Doc — Mid Doc or Full Doc Only
source_document: Angle Finance Prime Movers Flyer — FAQ
policy_statement: >
  "Prime Movers can be done under Mid Doc or Full Doc. Low Doc is not an
  option as bank statements or financials, plus ATO portals, are
  required."
interpretation: >
  Regardless of the applicant's credit score or property backing, Prime
  Movers can NEVER be processed under Low Doc — only Mid Doc or Full Doc
  are available, because the product's underlying requirements (bank
  statements/financials, ATO portals) are inherently incompatible with
  Low Doc's reduced documentation model.
business_rationale: >
  Prime Movers already requires bank statements or a full financial
  assessment as a qualifying criterion (see the Prime Movers Qualifying
  Criteria), which is structurally beyond what Low Doc provides — so Low
  Doc is not merely discouraged but categorically incompatible with this
  product's requirements.
examples:
  eligible:
    - Prime Mover deal assessed under Mid Doc, applicant provides 6
      months bank statements -> eligible
    - Prime Mover deal assessed under Full Doc with full financials ->
      eligible
  ineligible:
    - Prime Mover deal submitted under Low Doc, even with a 650+ credit
      score -> not eligible; Low Doc is structurally unavailable for this
      product regardless of credit strength
business_logic: |
  IF product == "Prime Movers":
    require(documentation_tier IN {"Mid Doc", "Full Doc"})
    IF documentation_tier == "Low Doc":
      not_eligible = True  # categorically excluded, not just discouraged
keywords:
  - Prime Movers
  - Low Doc exclusion
  - Mid Doc
  - Full Doc
synonyms:
  Low Doc:
    - low documentation
intent_examples:
  - "Can a high-credit-score customer use Low Doc for a Prime Mover deal?"
decision: Not Eligible under Low Doc — Prime Movers requires Mid Doc or Full Doc only, with no exception
related_policy:
  - EX124 (Prime Movers Carry a 1% Rate Loading)
  - EX138 (Prime Movers Excludes Both Sole Traders and Individual Partnerships)
```

```yaml
exception_id: EX140
title: Terms Over 60 Months Require Property-Backed Status Plus a 1% Rate Loading
source_document: Angle Finance Rate Card — Loan Structure
policy_statement: >
  "* 1% rate loading applicable for terms over 60 months. Customer must
  be property backed to qualify."
interpretation: >
  Extending a term beyond the standard 60-month maximum (up to 72 months
  for Primary Assets, or 84 months for Primary MV) is only available if
  the customer is property-backed — non-property-backed customers cannot
  access these extended terms at all — AND even for property-backed
  customers, a 1% rate loading applies once the term exceeds 60 months.
business_rationale: >
  Longer terms compound residual/mechanical risk and extend the lender's
  exposure horizon; requiring property backing ensures a stronger
  security position is in place before extending beyond the standard
  term, and the 1% loading additionally compensates for the extra time-
  based risk.
examples:
  eligible:
    - Property-backed customer, Primary Asset, 72-month term -> eligible,
      with a 1% rate loading applied
  ineligible:
    - Non-property-backed customer requesting a 72-month term -> not
      eligible; extended terms beyond 60 months are only available to
      property-backed customers
business_logic: |
  IF loan_term_months > 60:
    require(property_backed == True)
    applicable_rate = base_rate + 1%
  ELSE:
    no_additional_loading_or_property_requirement_for_term_alone
keywords:
  - loan term
  - 60 months
  - property backed
  - 1% loading
synonyms:
  extended term:
    - long-term loan
intent_examples:
  - "Can a non-property-backed customer get a 72-month term?"
  - "Is there a rate loading for terms over 60 months?"
decision: Not Eligible for terms over 60 months unless property-backed; 1% loading applies even when eligible
related_policy:
  - EX141 (Zero Balloon Only at Maximum EOT)
```

```yaml
exception_id: EX141
title: Zero Balloon Only at Maximum EOT (25 Years Primary / 15 Years Secondary)
source_document: Angle Finance Rate Card — Loan Structure footnote
policy_statement: >
  "* EOT 25 Years Primary Assets & EOT 15 Years Secondary Assets 0%
  Balloon Only."
interpretation: >
  Where a deal is structured to reach the maximum EOT allowed for its
  asset category (25 years for Primary, 15 years for Secondary), no
  balloon payment is available at all — a fully amortised (0% balloon)
  structure is mandatory at these maximum EOT points, consistent with
  the pattern seen at Metro (EX067) where balloons become unavailable at
  the maximum permitted asset age.
business_rationale: >
  A confident residual value estimate becomes unreliable as the
  projected asset age approaches the absolute maximum the lender is
  willing to accept, so Angle removes the balloon option entirely at
  that ceiling rather than offering a reduced balloon percentage.
examples:
  eligible:
    - Primary asset financed to a 20-year EOT, with a balloon structured
      -> eligible (below the 25-year maximum, balloon still available per
      the standard Loan Structure table)
  ineligible:
    - Primary asset financed to the full 25-year EOT, WITH a balloon
      requested -> not eligible; must be fully amortised (0% balloon) at
      this maximum EOT
business_logic: |
  IF asset_category == "Primary" AND EOT_years == 25:
    require(balloon_pct == 0%)
  ELSE IF asset_category == "Secondary" AND EOT_years == 15:
    require(balloon_pct == 0%)
keywords:
  - balloon payment
  - maximum EOT
  - 0% balloon
synonyms:
  0% balloon:
    - fully amortised
    - no balloon
intent_examples:
  - "Can I get a balloon payment if the loan runs to the maximum 25-year EOT?"
decision: Not Eligible for any balloon percentage once EOT reaches the maximum (25 years Primary / 15 years Secondary) — fully amortised only
related_policy:
  - EX140 (Terms Over 60 Months Require Property-Backed Status)
```

```yaml
exception_id: EX142
title: Full Doc Documentation Requirement Escalates Above $250,000 (Bank Statements Alone No Longer Accepted)
source_document: Angle Finance Full Doc — Minimum Requirements Product Update
policy_statement: >
  "6 Months+ Bank Statements OR FY2024 + FY2023 Accountant prepared
  financials" [Under $250,000 only]; "FY2024 + FY2023 Accountant
  prepared financials only" [$250,000 and above].
interpretation: >
  Below $250,000, an applicant has a CHOICE between providing 6+ months
  of bank statements OR 2 years of accountant-prepared financials —
  either satisfies the requirement. At $250,000 and above, this choice
  disappears entirely — only the 2 years of accountant-prepared
  financials is accepted; bank statements alone are no longer sufficient
  at any amount from $250,000 upward.
business_rationale: >
  Reflects escalating due-diligence requirements with transaction size —
  bank statements alone are considered adequate income/serviceability
  evidence only for smaller transactions, while larger transactions
  require the more rigorous, externally-verified view that accountant-
  prepared financials provide.
examples:
  eligible:
    - $180,000 transaction, applicant provides only 6 months of bank
      statements (no financials) -> eligible (under the $250,000
      threshold, bank statements alone are sufficient)
  ineligible:
    - $300,000 transaction, applicant provides only 6 months of bank
      statements (no financials) -> not eligible; at this size, only
      accountant-prepared financials (FY2024+FY2023) are accepted, bank
      statements alone do not suffice
business_logic: |
  IF transaction_size < 250000:
    require(bank_statements_6mo_plus OR accountant_prepared_financials_FY2024_FY2023)
  ELSE:  # transaction_size >= 250000
    require(accountant_prepared_financials_FY2024_FY2023)  # bank statements alone insufficient
keywords:
  - Full Doc
  - bank statements
  - accountant prepared financials
  - $250,000 threshold
synonyms:
  accountant prepared financials:
    - externally prepared financial statements
intent_examples:
  - "Can I use bank statements instead of financials for a $300,000 Full Doc deal?"
decision: Not Eligible with bank statements alone at $250,000 or above — accountant-prepared financials required from that threshold upward
related_policy:
  - Section 3 (Documentation Tiers)
```

```yaml
exception_id: EX143
title: Low Doc Under $100k Uniquely Allows Non-Property-Backed Applicants
source_document: Angle Finance Rate Card — Low Doc & Mid Doc guidelines
policy_statement: >
  Property Status: "Property backed (We accept spousal property!) /
  Non-Property Owner" [Low Doc <$100k], compared with "Property backed
  (We accept spousal property!)" only [Low Doc $100k–$250k and Mid Doc
  <$500k — no non-property-backed option listed].
interpretation: >
  Among Angle's three documentation-tier products, ONLY the smallest Low
  Doc bracket (<$100k) offers a genuine non-property-backed pathway. Both
  the larger Low Doc bracket ($100k–$250k) and Mid Doc (<$500k) require
  property backing — there is no non-property-owner option at all once
  exposure exceeds $100,000.
business_rationale: >
  Reflects a straightforward risk-scaling principle: the smallest,
  lowest-exposure transactions can be supported without property
  security, but any larger exposure requires the stronger security
  position that property backing provides.
examples:
  eligible:
    - Non-property-backed applicant, $80,000 exposure -> eligible under
      Low Doc <$100k
  ineligible:
    - Non-property-backed applicant, $150,000 exposure -> not eligible
      under Low Doc $100k–$250k (property backing is mandatory at this
      tier); would need to reduce exposure below $100,000, or provide
      property backing
business_logic: |
  IF total_exposure < 100000:
    property_backed_required = False  # non-property-backed pathway available
  ELSE IF total_exposure >= 100000:
    property_backed_required = True  # mandatory from this threshold upward, all tiers
keywords:
  - non-property owner
  - Low Doc
  - $100,000 threshold
synonyms:
  non-property-backed:
    - unsecured applicant
intent_examples:
  - "Can a non-property-backed applicant get a $150,000 Low Doc facility?"
decision: Not Eligible for non-property-backed applicants above $100,000 exposure, under any documentation tier
related_policy:
  - Section 3 (Documentation Tiers)
  - EX134 (Non-Property Owners Require a 20% Deposit — general property ownership rule)
```

```yaml
exception_id: EX144
title: Unaccredited Suppliers Require a Current Bank Statement for Accreditation
source_document: Angle Finance Rate Card — Settlement Details
policy_statement: >
  "Unaccredited suppliers – please supply a current bank statement for
  accreditation."
interpretation: >
  If the vehicle/asset supplier is not already an Angle-accredited
  supplier, the transaction is not automatically rejected — instead,
  providing the supplier's current bank statement allows Angle to
  accredit them as part of the settlement process.
business_rationale: >
  Provides a practical pathway to work with new or lesser-known
  suppliers (rather than restricting brokers only to a pre-existing
  accredited list), while still requiring a basic verification step
  (bank statement) before funds are released to an unfamiliar supplier.
examples:
  eligible:
    - Supplier not on Angle's accredited list, current bank statement
      provided at settlement -> supplier can be accredited, settlement
      can proceed
  ineligible:
    - Unaccredited supplier, no bank statement provided -> settlement
      cannot proceed until this is supplied
business_logic: |
  IF supplier_status == "unaccredited":
    require(current_bank_statement_provided == True)  # enables accreditation and settlement
keywords:
  - unaccredited supplier
  - bank statement
  - accreditation
synonyms:
  unaccredited supplier:
    - non-approved supplier
intent_examples:
  - "Can I settle a deal with a supplier that isn't on Angle's accredited list?"
decision: Conditional — Settlement possible for unaccredited suppliers only with a current bank statement provided
related_policy:
  - Section (Settlement Details)
```

```yaml
exception_id: EX145
title: Existing PPSR Encumbrances on Used Cars Must Be Removed Prior to Settlement
source_document: Angle Finance Rate Card — Settlement Details
policy_statement: >
  "All existing PPSR encumbrances on used cars, must be removed prior to
  settlement."
interpretation: >
  For used cars specifically, any existing PPSR (Personal Property
  Securities Register) encumbrance (i.e. another party's registered
  security interest) must be cleared BEFORE settlement can occur — this
  is a precondition, not something that can be resolved after funding.
business_rationale: >
  An existing PPSR encumbrance means another financier has a registered
  claim over the asset; Angle cannot safely register its own interest
  (or safely take security) while a competing encumbrance remains,
  making removal a mandatory precondition specifically for used cars
  (where prior encumbrances are more likely than on new vehicles).
examples:
  eligible:
    - Used car with a prior PPSR encumbrance, encumbrance cleared/
      released before the settlement date -> eligible to proceed
  ineligible:
    - Used car with an active, unresolved PPSR encumbrance at the
      scheduled settlement date -> settlement cannot proceed until the
      encumbrance is removed
business_logic: |
  IF asset_condition == "used" AND asset_type == "car":
    require(all_existing_ppsr_encumbrances_removed_before(settlement_date))
keywords:
  - PPSR encumbrance
  - used cars
  - settlement precondition
synonyms:
  PPSR encumbrance:
    - existing security interest
    - registered charge
intent_examples:
  - "Can settlement proceed if the used car still has a PPSR encumbrance?"
decision: Not Eligible for settlement until existing PPSR encumbrances on used cars are fully removed
related_policy:
  - Section (Settlement Details — Satisfactory PPSR, Certificate of Currency for assets >$100K)
```

```yaml
exception_id: EX146
title: Start-Up Product Minimum Credit Score — Discrepancy Between Rate Card (500+) and Start-Up Flyer (550+)
source_document: Angle Finance Rate Card (Start Up Product Qualifying criteria) vs. Angle Finance Start-Up Flyer (Quick Qualifying Checklist)
policy_statement: >
  Rate Card: "500+ Credit Score" [Start Up Product Qualifying criteria].
  Start-Up Flyer: "Minimum credit score (Veda 1:1): 550+" [Quick
  Qualifying Checklist].
interpretation: >
  These two Angle source documents state DIFFERENT minimum credit score
  thresholds for the same Start-Up product — the Rate Card says 500+,
  while the dedicated Start-Up Flyer says 550+. This is flagged as a
  documentation discrepancy requiring verification rather than treated
  as a confirmed policy rule, since the two source documents conflict.
business_rationale: >
  Not a business rationale in the usual sense — this entry exists to
  flag an inconsistency for operational safety. Applying the wrong
  (lower) threshold could result in submitting applications that don't
  actually meet Angle's true current requirement, or unnecessarily
  declining applicants who would qualify at the lower stated threshold.
examples:
  eligible:
    - Applicant with a 560 credit score -> meets either stated threshold
      (500+ or 550+), no ambiguity
  ineligible (ambiguous — requires verification):
    - Applicant with a 520 credit score -> would meet the Rate Card's
      500+ threshold but NOT the Start-Up Flyer's 550+ threshold; the
      correct outcome cannot be determined from these documents alone
business_logic: |
  IF credit_score >= 550:
    eligible_under_both_stated_thresholds = True  # no ambiguity
  ELSE IF credit_score >= 500 AND credit_score < 550:
    outcome = "AMBIGUOUS — verify current requirement with Angle before proceeding"
  ELSE:
    not_eligible = True  # below both thresholds
keywords:
  - Start-Up
  - credit score discrepancy
  - documentation conflict
synonyms:
  Start-Up:
    - new business product
intent_examples:
  - "What is the actual minimum credit score for Start-Up — 500 or 550?"
decision: Ambiguous for scores between 500–549 — verify current requirement with Angle Finance directly before relying on either source document
related_policy:
  - EX137 (Start-Up Loan Cap of $150,000 Is Inclusive of Brokerage)
```

---

*Compiled from the Angle Finance Rate Card (April 2026), Start-Up Product Flyer (Jan 2026), Full Doc — Minimum
Requirements Product Update, and Prime Movers Product Flyer (May 2026). This document is a standalone deep-dive
reference intended to sit alongside, and be cross-referenced with, the Resimac, Metro, and BFS Detailed References.
Verify all figures against Angle's live MyHub platform before operational use, and consult your BDM for scenarios
outside these criteria.*
