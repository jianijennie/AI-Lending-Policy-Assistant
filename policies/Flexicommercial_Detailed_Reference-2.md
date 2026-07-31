# flexicommercial (Flexi) — Detailed Policy Reference & Exceptions Catalog

> Source: flexicommercial Rate Card (13 July 2026), Credit Matrix — All Entities (effective 8 December 2025),
> flexireplacement Policy (current as at 1 August 2024), flexipremium Low Start Loans Fact Sheet, Old Finance
> Meets New Fact Sheet, and Mid-Term Refinancing Fact Sheet (all dated 19 May 2026).
> Purpose: A standalone deep-dive reference (parallel to the Resimac, Metro, BFS, and Angle references) covering
> flexicommercial's standard/flexipremium rate structure, Credit Matrix exposure rules, asset categories, and its
> suite of specialty products (flexireplacement, Low Start Loans, Mid-Term Refinancing, bundled refinancing) —
> with all exception clauses listed separately in Section 5, using the same `exception_id` / `keywords` /
> `synonyms` / `intent_examples` / `decision` / `related_policy` schema as the other lenders' catalogs. IDs
> continue from EX147 onward.

---

## 1. Structure Overview

Flexi runs two parallel rate tracks plus several specialty overlay products:

| Track/Product | Purpose |
|---|---|
| **flexipremium** | Lower rates for more established businesses buying newer assets (Primary ≤5yrs, Secondary ≤2yrs) |
| **flexicommercial standard rates** | The general-purpose rate table across Primary/Secondary/Tertiary, by funded amount |
| **Credit Matrix** | Governs maximum loan size, exposure, and required conditions (ABN/GST tenure, asset backing, repayment history) by asset category and transaction size band |
| **flexireplacement** | A dedicated policy for replacing an existing (possibly non-Flexi) facility with a new Flexi facility |
| **flexipremium Low Start Loans** | 50% repayments for the first 3 months on new flexipremium facilities |
| **Mid-Term Refinancing** | Refinancing an existing Flexi facility mid-term, at net book value |
| **Old Finance Meets New (bundled refinance)** | Bundling payout of an existing facility into a new, larger facility with additional equipment |

## 2. Asset Categories

| | Primary | Secondary | Tertiary |
|---|---|---|---|
| Examples | Agricultural machinery, materials handling/forklifts, access equipment, light/heavy trucks, trailers, buses/coaches, commercial motor vehicles, construction/earthmoving | Medical/dental/lab equipment, mining equipment, earthmoving attachments, plant services, printing/packaging, forestry, engineering/toolmaking, woodworking/metalworking, mechanical workshop, agricultural spraying drones, Tier II trucks/buses/earthmoving/utes | Drones, fitness equipment, POS systems, AV/video conferencing, IT assets, renewable energy, pallet racking, security hardware, fit-outs, temporary fencing, GPS attachments, software, air conditioning, cool rooms, spray booths, catering/hospitality equipment, food manufacturing equipment, portable buildings |
| Max age at EOT | 20 years (trailers – 30 years) | 7 years | (per Tertiary sub-limits, see EX164/EX165) |
| Excluded | SUVs, passenger cars (incl. rental car businesses) | — | Photocopiers, MFDs, scaffolding |

## 3. Rate Tables

**flexipremium** (ex brokerage): $50k–$100k: Primary 7.15% / Secondary 8.69%; $100,001–$500k: Primary 7.15% /
Secondary 8.19%; $500,001+: contact BDM. Max 3% brokerage.

**flexicommercial standard** (ex brokerage): $10k–$20k: 12.60%/13.50%/14.10% (Primary/Secondary/Tertiary);
$20,001–$150k: 8.35%/8.85%/12.10%; $150,001+: 7.85%/8.35%/11.10%.

Loadings on standard rates: +1.0% (Prime Movers excl. Tippers/Agitators/Rigid Bodies; assets 11–15yrs at EOT;
term <24 months; private sales and refinances) / +1.25% (term >60 months) / +1.50% (non-asset-backed) / +2.0%
(assets >15–20yrs at EOT).

---

## 5. Exceptions Catalog (flexicommercial)

```yaml
exception_id: EX147
title: flexireplacement Aggregated Exposure Cap Includes Existing Matrix Exposure ($500K Combined)
source_document: flexicommercial flexireplacement Policy — Conditions
policy_statement: >
  "Maximum transaction size/aggregated exposure (includes existing
  matrix exposure) $500K."
interpretation: >
  The $500K ceiling for flexireplacement is not just the new
  transaction — it is a COMBINED total that includes whatever exposure
  the customer already has under the standard Credit Matrix. A customer
  already carrying $300K of Matrix exposure could only add up to
  $200K more via flexireplacement, not a fresh $500K.
business_rationale: >
  Prevents a customer from using flexireplacement as a way to bypass the
  aggregate exposure limits that would otherwise apply under the Credit
  Matrix, keeping total risk to any one customer capped consistently
  across products.
examples:
  eligible:
    - Customer with $200K existing Matrix exposure applies for a $250K
      flexireplacement facility -> total $450K, within the $500K
      combined cap
  ineligible:
    - Customer with $400K existing Matrix exposure applies for a $200K
      flexireplacement facility -> total would be $600K, exceeding the
      $500K combined cap; not eligible at the requested size
business_logic: |
  combined_exposure = existing_matrix_exposure + new_flexireplacement_amount
  IF combined_exposure > 500000:
    not_eligible_at_requested_size = True
keywords:
  - flexireplacement
  - aggregated exposure
  - $500K cap
synonyms:
  aggregated exposure:
    - combined exposure
    - total exposure
intent_examples:
  - "Does my client's existing Matrix exposure count toward the flexireplacement $500K cap?"
decision: Not Eligible at the requested size if combined (existing Matrix + new flexireplacement) exposure exceeds $500K
related_policy:
  - Section 4 (Credit Matrix — Increased Exposure)
```

```yaml
exception_id: EX148
title: flexireplacement Repayment Cap — 125% of Facility Being Replaced
source_document: flexicommercial flexireplacement Policy — Conditions
policy_statement: >
  "Proposed repayment not to exceed 125% of that being replaced."
interpretation: >
  The new facility's repayment cannot exceed 125% of the repayment on
  the facility it replaces — a single test based on repayment amount
  (not loan amount), consistent with the same "125% rule" concept seen
  at Metro (EX041), though Metro offers a dual test (loan amount OR
  repayment) while flexireplacement appears to test repayment only.
business_rationale: >
  Prevents a "replacement" from being used to substantially increase a
  customer's repayment burden under the guise of asset replacement.
examples:
  eligible:
    - Facility being replaced has a $2,000/month repayment; new facility
      proposed at $2,400/month (120%) -> eligible
  ineligible:
    - Facility being replaced has a $2,000/month repayment; new facility
      proposed at $2,600/month (130%) -> not eligible; exceeds the 125%
      repayment cap
business_logic: |
  IF new_facility_repayment > 1.25 * replaced_facility_repayment:
    not_eligible = True
keywords:
  - flexireplacement
  - 125% cap
  - repayment test
synonyms:
  repayment cap:
    - repayment ceiling
intent_examples:
  - "Can the new repayment be 130% of the old repayment under flexireplacement?"
decision: Not Eligible if proposed repayment exceeds 125% of the repayment being replaced
related_policy:
  - Cross-lender note: compare with Metro EX041 (Replacement Policy 125% Dual-Test Rule, which offers a loan-amount OR repayment test)

Note: The current FlexiReplacement flyer explicitly limits only the proposed repayment to 125% of the facility being replaced. It does not mention an equivalent loan amount or finance amount test. Unlike Metro's replacement policy, no "Loan Amount OR Repayment" alternative is provided. If Flexicommercial applies an additional loan amount test internally, this is not documented in the current flyer and should be confirmed directly with Flexicommercial before being treated as policy.
```

```yaml
exception_id: EX149
title: flexireplacement Asset Need Not Be Like-for-Like With Replaced Asset
source_document: flexicommercial flexireplacement Policy — Conditions
policy_statement: >
  "Asset to be financed must be core business equipment. Asset does not
  necessarily need to be like-for-like with the replaced asset."
interpretation: >
  While the new asset must still qualify as "core business equipment,"
  it does NOT need to be the same type of asset as the one being
  replaced — e.g. a customer could replace an ageing forklift with a new
  excavator, provided both are legitimate core business equipment for
  that customer.
business_rationale: >
  Gives customers flexibility to use the replacement pathway to actually
  upgrade or change their equipment mix (not just swap like-for-like),
  while still requiring the new asset to serve a genuine core business
  purpose rather than an unrelated purchase.
examples:
  eligible:
    - Replacing an old forklift with a new excavator, both used as core
      business equipment -> eligible
  ineligible:
    - Replacing an old forklift with an asset unrelated to the core
      business (e.g. office fit-out furniture) -> not eligible; fails
      the "core business equipment" test even though like-for-like isn't
      required
business_logic: |
  IF new_asset_is_core_business_equipment == True:
    like_for_like_not_required = True
  ELSE:
    not_eligible = True
keywords:
  - flexireplacement
  - like-for-like
  - core business equipment
synonyms:
  core business equipment:
    - primary business asset
intent_examples:
  - "Does the replacement asset need to be the same type as the old one?"
decision: Not Required to be like-for-like, but must still be genuine core business equipment
related_policy:
  - Section 1 (Structure Overview)
```

```yaml
exception_id: EX150
title: flexireplacement Uses a Different "Approved Lender" List Than the Credit Matrix/Rate Card Documents
source_document: flexicommercial flexireplacement Policy vs. Credit Matrix / Low Start Loans Fact Sheet
policy_statement: >
  flexireplacement approved lenders: "ANZ, CBA, NAB, Westpac, BOQ,
  Suncorp, Bendigo Adelaide, Macquarie Bank, Judo Bank, and also Angle
  Finance, Caterpillar Finance Australia, DLL, Dynamoney, Earlypay, John
  Deere Financial, Kubota Australia Finance, Mercedes Benz Financial
  Services, Moneytech, Morris Finance, Nissan Financial Services, Pepper
  Money, Scotpac, Shift, Toyota Finance, Volvo Finance, Westlawn
  Finance." Credit Matrix / Low Start Loans approved lenders: "The big
  four banks (and their subsidiaries), BoQ, Judo Bank, Rabobank (and
  DLL), Suncorp, Bendigo Adelaide or Macquarie Bank as well as large
  asset finance institutions limited to Metro Finance, Caterpillar
  Financial, CNH Capital, John Deere Financial, Paccar Financial and
  Toyota Finance."
interpretation: >
  These two lists overlap substantially (big four banks, BOQ, Suncorp,
  Bendigo Adelaide/Macquarie, Judo Bank, Caterpillar, John Deere, Toyota
  Finance appear in both) but are NOT identical. The flexireplacement
  list additionally includes Angle Finance, Dynamoney, Earlypay, Kubota,
  Mercedes-Benz Financial Services, Moneytech, Morris Finance, Nissan
  Financial Services, Pepper Money, Scotpac, Shift, Volvo Finance, and
  Westlawn Finance — none of which appear in the Credit Matrix/Low Start
  Loans list. Conversely, the Credit Matrix/Low Start Loans list includes
  Metro Finance, CNH Capital, and Paccar Financial, which do not appear
  by name in the flexireplacement list (though Rabobank/DLL are named
  there too). This is flagged as a discrepancy requiring verification —
  do not assume a lender approved for one product is automatically
  approved for the other.
business_rationale: >
  Different flexicommercial products may reasonably have different
  approved-lender lists depending on the product's specific risk
  profile and purpose, but the discrepancy is significant enough
  (13+ lenders differ) that it should not be assumed to be a simple
  oversight — always check the CORRECT list for the SPECIFIC product
  being used.
examples:
  eligible:
    - Customer's existing facility is with Pepper Money, applying for
      flexireplacement -> Pepper Money appears on the flexireplacement
      list, so this may be eligible (subject to other flexireplacement
      conditions)
  ineligible (i.e., requires verification):
    - Customer's existing facility is with Pepper Money, applying for a
      Low Start Loan (which requires "an existing commercial asset
      finance facility with an approved lender") -> Pepper Money does
      NOT appear on the Credit Matrix/Low Start Loans approved lender
      list, so this specific product's eligibility is uncertain and
      needs verification
business_logic: |
  IF product == "flexireplacement":
    approved_lender_list = flexireplacement_list  # includes Angle Finance, Dynamoney, Earlypay, Kubota, etc.
  ELSE IF product IN {"Credit Matrix Increased Exposure", "Low Start Loans"}:
    approved_lender_list = credit_matrix_list  # includes Metro Finance, CNH Capital, Paccar Financial
  # Do not use one list to validate eligibility for the other product
keywords:
  - approved lender
  - flexireplacement
  - Low Start Loans
  - discrepancy
synonyms:
  approved lender:
    - approved financier
intent_examples:
  - "Is Pepper Money an approved lender for a Low Start Loan?"
  - "Does the flexireplacement approved lender list match the Credit Matrix list?"
decision: Ambiguous/Product-Specific — verify the correct approved lender list for the specific product being used; the two lists are not interchangeable
related_policy:
  - EX173 (Low Start Loan Requires an Existing Commercial Asset Finance Facility With an Approved Lender)
```

```yaml
exception_id: EX151
title: flexireplacement Requires Old and New Facility to Have Identical Borrowing/Guarantee Parties
source_document: flexicommercial flexireplacement Policy — New facility requirements
policy_statement: >
  "Borrowing and Guarantee parties on the old and new facility to be
  identical."
interpretation: >
  The exact same borrower(s) and guarantor(s) on the facility being
  replaced must also be the borrower(s)/guarantor(s) on the new
  flexireplacement facility — no substitution, addition, or removal of
  parties is permitted as part of this process.
business_rationale: >
  Keeps the replacement transaction a genuine like-for-like continuation
  of the same credit relationship (just moving to a new asset/facility),
  rather than allowing the replacement process to be used to
  restructure the borrowing entity or guarantor pool, which would
  require a fresh full credit assessment rather than the streamlined
  replacement pathway.
examples:
  eligible:
    - Same company borrower and same individual guarantor on both the
      old and new facility -> eligible
  ineligible:
    - New facility proposes adding an additional guarantor not on the
      original facility -> not eligible under flexireplacement; would
      require a standard (non-replacement) application instead
business_logic: |
  IF new_facility_borrowers_and_guarantors != old_facility_borrowers_and_guarantors:
    not_eligible_under_flexireplacement = True
keywords:
  - flexireplacement
  - identical parties
  - borrower
  - guarantor
synonyms:
  identical parties:
    - same borrowing entity
intent_examples:
  - "Can I add a new guarantor when using flexireplacement?"
decision: Not Eligible if the borrowing/guarantee parties differ between the old and new facility
related_policy:
  - Section 1 (Structure Overview)
```

```yaml
exception_id: EX152
title: flexireplacement Settlement Must Occur Within 90 Days of Old Facility Expiry
source_document: flexicommercial flexireplacement Policy — New facility requirements
policy_statement: >
  "Settlement of the new facility must be made within 90 days of the
  expiry of the old facility."
interpretation: >
  There is a hard 90-day window from when the old facility expires
  (or is paid out) to when the new flexireplacement facility must settle
  — this is not an indefinite pathway; if settlement doesn't occur
  within this window, the replacement structure is no longer available.
business_rationale: >
  Keeps the replacement transaction genuinely connected in time to the
  facility it is replacing, preventing the pathway from being used for
  an unrelated, much-later transaction that happens to reference an old,
  already-closed facility.
examples:
  eligible:
    - Old facility expires 15 March; new facility settles 20 May (within
      90 days) -> eligible
  ineligible:
    - Old facility expires 15 March; new facility settlement attempted
      in September (well beyond 90 days) -> not eligible under
      flexireplacement
business_logic: |
  IF (new_facility_settlement_date - old_facility_expiry_date) > 90 days:
    not_eligible_under_flexireplacement = True
keywords:
  - flexireplacement
  - settlement window
  - 90 days
synonyms:
  settlement window:
    - settlement deadline
intent_examples:
  - "How long after the old facility expires can I settle the new flexireplacement facility?"
decision: Not Eligible if settlement occurs more than 90 days after the old facility's expiry
related_policy:
  - Section 1 (Structure Overview)
```

```yaml
exception_id: EX153
title: flexireplacement Balloon Refinances Require Inspection/Valuation Above $300K
source_document: flexicommercial flexireplacement Policy — Conditions
policy_statement: >
  "Can be used for balloon refinances up to $500K (inspection and
  valuation required if >$300K)."
interpretation: >
  Balloon refinances up to $500K are permitted under flexireplacement,
  but a physical inspection and valuation becomes mandatory once the
  transaction exceeds $300K — below that threshold, no inspection/
  valuation is explicitly required.
business_rationale: >
  Larger balloon refinance amounts warrant independent verification of
  the asset's actual condition and value before Flexi commits to
  refinancing the balloon, reducing the risk of relying solely on
  paperwork for higher-value transactions.
examples:
  eligible:
    - $250K balloon refinance, no inspection/valuation provided -> eligible
      (below the $300K threshold)
    - $400K balloon refinance, inspection and valuation provided -> eligible
  ineligible:
    - $400K balloon refinance, no inspection/valuation provided -> not
      eligible; mandatory above $300K
business_logic: |
  IF transaction_type == "balloon_refinance" AND amount > 300000:
    require(inspection_and_valuation_provided == True)
  IF amount > 500000:
    not_eligible_under_flexireplacement  # exceeds the $500K cap entirely
keywords:
  - flexireplacement
  - balloon refinance
  - inspection
  - valuation
synonyms:
  balloon refinance:
    - residual refinance
intent_examples:
  - "Is an inspection required for a $250K balloon refinance?"
decision: Not Eligible above $300K without an inspection and valuation; not eligible at all above $500K
related_policy:
  - Section 1 (Structure Overview)
```

```yaml
exception_id: EX154
title: Credit Matrix — Tertiary Assets Require ABN/GST From the Smallest Transaction Band (Stricter Than Primary/Secondary)
source_document: flexicommercial Credit Matrix — Tertiary Assets table
policy_statement: >
  Tertiary Assets table shows both "ABN >2 years" AND "GST Registered >2
  years" ticked from the smallest ($10K–$20K) band upward. Primary and
  Secondary Assets tables only require GST Registered >2 years from the
  $20K–$50K band upward (not required at $10K–$20K).
interpretation: >
  Tertiary assets are held to a stricter documentation standard from the
  very smallest transaction size — both ABN and GST tenure are required
  immediately, whereas Primary and Secondary assets get a concession at
  the smallest ($10K–$20K) band where GST registration is not required.
business_rationale: >
  Consistent with Tertiary being the lowest-liquidity, most specialised
  asset category across this catalog (see the general "least liquid =
  most restricted" pattern) — Flexi does not extend even the smallest-
  transaction documentation concession to Tertiary assets that it does
  to Primary/Secondary.
examples:
  eligible:
    - $15,000 Primary asset transaction, ABN >2 years but GST registered
      only 6 months -> eligible (GST not required at this band for
      Primary)
  ineligible:
    - $15,000 Tertiary asset transaction, ABN >2 years but GST registered
      only 6 months -> not eligible; GST >2 years IS required for
      Tertiary even at this smallest band
business_logic: |
  IF asset_category == "Tertiary":
    require(ABN_years > 2 AND GST_years > 2)  # required from the smallest ($10K-$20K) band
  ELSE IF asset_category IN {"Primary", "Secondary"} AND transaction_band == "$10K-$20K":
    require(ABN_years > 2)  # GST not required at this smallest band
keywords:
  - Credit Matrix
  - Tertiary assets
  - GST registration
  - ABN
synonyms:
  Tertiary assets:
    - lowest liquidity category
intent_examples:
  - "Is GST registration required for a small Tertiary asset transaction?"
decision: Not Eligible for Tertiary assets without both ABN >2 years and GST >2 years, even at the smallest transaction band
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX155
title: Credit Matrix — Asset Backing Is Mandatory for All Transport Operator/Subcontractor Transactions
source_document: flexicommercial Credit Matrix — footnote / Conditions page
policy_statement: >
  "Asset backing is a requirement for all transport operator/
  subcontractor transactions." Also: "Borrowers/Guarantors for transport
  operators/subcontractors must be asset backed with sufficient equity."
interpretation: >
  Regardless of transaction size or which band of the Credit Matrix
  table would otherwise apply, transport operator and subcontractor
  customers are ALWAYS required to be asset backed with sufficient
  equity — this overrides the standard table's size-based asset-backing
  thresholds (which normally only kick in at larger transaction bands).
business_rationale: >
  Transport operators/subcontractors are considered a higher-risk
  industry segment (consistent with the road transport/logistics
  distinctions seen elsewhere in the Flexi documents — EX169), so Flexi
  removes the smaller-transaction concession (where asset backing isn't
  otherwise required) for this specific customer segment.
examples:
  eligible:
    - Transport operator, $15,000 transaction (would normally not require
      asset backing at this size for a standard customer), asset-backed
      applicant -> eligible
  ineligible:
    - Transport operator, $15,000 transaction, non-asset-backed
      applicant -> not eligible; asset backing is mandatory for this
      industry segment regardless of transaction size
business_logic: |
  IF customer_industry IN {"transport_operator", "subcontractor"}:
    require(asset_backed_with_sufficient_equity == True)  # overrides standard size-based table
keywords:
  - transport operator
  - subcontractor
  - asset backing
  - mandatory
synonyms:
  transport operator:
    - logistics operator
    - freight operator
intent_examples:
  - "Does a small transport operator transaction still require asset backing?"
decision: Not Eligible for transport operator/subcontractor customers without asset backing, regardless of transaction size
related_policy:
  - EX168 / EX169 (flexipremium Road Transport/Logistics Definitions)
```

```yaml
exception_id: EX156
title: Credit Matrix — Director's Guarantees Waived for ASIC-Reporting Public/Private Companies
source_document: flexicommercial Credit Matrix — Conditions
policy_statement: >
  "Director's Guarantees.*" with footnote: "*Not required for Public
  companies or Private companies that are required to lodge annual
  financial statements with ASIC."
interpretation: >
  While director's guarantees are a standard condition generally,
  Public companies and Private companies that must lodge annual
  financial statements with ASIC are exempt from this requirement
  entirely — no director's guarantee is needed for these entity types.
business_rationale: >
  Companies required to lodge audited/reviewed financial statements with
  ASIC are subject to a higher level of external financial transparency
  and regulatory scrutiny already, reducing the incremental value of a
  personal director's guarantee as a risk mitigant.
examples:
  eligible:
    - Public company required to lodge annual financial statements with
      ASIC -> no director's guarantee required
  ineligible (i.e., guarantee still required):
    - Small private company NOT required to lodge financial statements
      with ASIC -> director's guarantee still required
business_logic: |
  IF entity_type == "public_company" OR (entity_type == "private_company" AND required_to_lodge_ASIC_financials == True):
    directors_guarantee_required = False
  ELSE:
    directors_guarantee_required = True
keywords:
  - director's guarantee
  - ASIC
  - public company
  - private company
synonyms:
  director's guarantee:
    - personal guarantee
intent_examples:
  - "Does a public company still need a director's guarantee?"
decision: Not Required for Public companies or ASIC-reporting Private companies; required otherwise
related_policy:
  - Section 4 (Credit Matrix — Conditions)
```

```yaml
exception_id: EX157
title: Credit Matrix — Used Assets and Private Sale Restricted to "Exception Basis" for Secondary/Tertiary
source_document: flexicommercial Credit Matrix — Conditions
policy_statement: >
  "Used assets and Private Sale acceptable for Primary. Secondary and
  Tertiary assets on exception basis."
interpretation: >
  Used assets and private sale transactions are standard/routinely
  accepted for Primary assets, but for Secondary and Tertiary assets,
  these are only considered on an EXCEPTION basis — not a standard,
  routinely available option. This means Secondary/Tertiary used/private
  sale deals require additional justification/discretionary approval
  rather than automatic processing.
business_rationale: >
  Secondary and Tertiary assets already carry more valuation/liquidity
  uncertainty than Primary assets (consistent with the broader industry
  pattern in this catalog); adding used condition and/or private sale
  provenance on top of that uncertainty is considered acceptable only in
  exceptional, individually-justified circumstances.
examples:
  eligible:
    - Used Primary asset (e.g. a used excavator) purchased privately ->
      standard acceptable transaction
  ineligible (requires exception approval):
    - Used Secondary asset (e.g. used medical equipment) purchased
      privately -> not automatically accepted; requires exception-basis
      approval, not standard processing
business_logic: |
  IF asset_category == "Primary" AND (asset_condition == "used" OR transaction_type == "private_sale"):
    standard_processing_available = True
  ELSE IF asset_category IN {"Secondary", "Tertiary"} AND (asset_condition == "used" OR transaction_type == "private_sale"):
    require(exception_basis_approval)  # not standard/automatic
keywords:
  - used assets
  - private sale
  - exception basis
  - Secondary assets
  - Tertiary assets
synonyms:
  exception basis:
    - discretionary approval
    - case-by-case approval
intent_examples:
  - "Can a used Secondary asset be purchased privately as a standard deal?"
decision: Not Standard/Automatic for used or private-sale Secondary/Tertiary assets — requires exception-basis approval
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX158
title: Credit Matrix — Trailers Get a 30-Year EOT vs 20 Years for Other Primary Assets
source_document: flexicommercial Credit Matrix / Rate Card — Asset Categories
policy_statement: >
  "Can be up to 20 years old at end of term (trailers – 30 years)."
interpretation: >
  Within the Primary asset category, trailers are singled out for a
  materially longer maximum EOT (30 years) than every other Primary
  asset type (20 years) — this is a sub-category exception within
  Primary, not a blanket rule.
business_rationale: >
  Trailers (unlike powered vehicles/equipment) have no engine or complex
  drivetrain to wear out, giving them a genuinely longer realistic
  useful life, which Flexi reflects in a longer permitted EOT
  specifically for this asset type.
examples:
  eligible:
    - Trailer financed to a 28-year EOT -> eligible (within the 30-year
      trailer-specific limit)
  ineligible:
    - Heavy truck (not a trailer) financed to a 25-year EOT -> not
      eligible; exceeds the standard 20-year Primary asset limit that
      applies to trucks
business_logic: |
  IF asset_type == "trailer":
    max_EOT_years = 30
  ELSE IF asset_category == "Primary":
    max_EOT_years = 20
keywords:
  - trailer
  - EOT
  - 30 years
synonyms:
  trailer:
    - towed asset
intent_examples:
  - "Can a trailer be financed to a 28-year EOT?"
decision: Eligible for trailers up to 30 years EOT; all other Primary assets capped at 20 years
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX159
title: Credit Matrix — Increased Exposure to $500K Keeps Secondary's Individual Transaction Cap Unchanged at $300K
source_document: flexicommercial Credit Matrix — Increased Exposure
policy_statement: >
  "Primary and Secondary Assets: after 9 payments... Applications can be
  considered to take the combined exposure to a maximum of $500K
  (individual transactions to be a maximum of $500K). NOTE: Individual
  transactions for secondary assets remains unchanged at $300K."
interpretation: >
  While the COMBINED exposure limit rises to $500K for both Primary and
  Secondary assets under this Increased Exposure pathway, the INDIVIDUAL
  transaction cap for Secondary assets specifically does NOT rise to
  match — it stays at its standard $300K limit, even though the combined
  ceiling implies $500K might be available. Only Primary assets can have
  an individual transaction reaching the full $500K under this pathway.
business_rationale: >
  Secondary assets are inherently less liquid than Primary, so even
  though the customer's overall relationship (combined exposure) can
  expand with good repayment history, Flexi does not extend this
  increased ceiling to a single Secondary transaction — the individual
  transaction risk cap for Secondary remains fixed regardless of the
  customer's improved standing.
examples:
  eligible:
    - Customer with $150K minimum qualifying contract and 9 payments made,
      applies for a $450K Primary asset transaction -> eligible (within
      the $500K individual transaction cap for Primary)
  ineligible:
    - Same customer applies for a $400K Secondary asset transaction -> not
      eligible; Secondary's individual transaction cap remains fixed at
      $300K even under the Increased Exposure pathway
business_logic: |
  IF pathway == "Increased Exposure (Primary and Secondary)":
    combined_exposure_limit = 500000
    IF asset_category == "Primary":
      individual_transaction_limit = 500000
    ELSE IF asset_category == "Secondary":
      individual_transaction_limit = 300000  # unchanged, does not scale with combined limit
keywords:
  - Increased Exposure
  - Secondary assets
  - individual transaction cap
  - $300K
synonyms:
  individual transaction:
    - single transaction
intent_examples:
  - "Can a single Secondary asset transaction reach $500K under Increased Exposure?"
decision: Not Eligible for a Secondary asset individual transaction above $300K, even under the Increased Exposure pathway
related_policy:
  - Section 4 (Credit Matrix — Increased Exposure)
  - EX147 (flexireplacement Aggregated Exposure Cap)
```

```yaml
exception_id: EX160
title: Credit Matrix — New Policy: Primary-Only Exposure to $750K Requires 18 Payments on a $250K+ Minimum Contract
source_document: flexicommercial Credit Matrix — New Policies
policy_statement: >
  "Primary Assets Only: after 18 payments have been made on either the
  flexicommercial contract or an asset finance contract with an approved
  lender.** (Minimum contract amount to be $250K. Statement to be
  provided showing perfect conduct.) Applications can be considered to
  take the combined exposure to a maximum of $750K (individual
  transactions to be a maximum of $500K)."
interpretation: >
  This is a SEPARATE, higher-tier exposure pathway from EX159's 9-payment
  pathway — it requires MORE payments (18 vs 9), a LARGER minimum
  qualifying contract ($250K vs $150K), and is Primary-assets-only (not
  available for Secondary), but in exchange unlocks a HIGHER combined
  exposure ceiling ($750K vs $500K) — though the individual transaction
  cap remains $500K either way.
business_rationale: >
  Rewards an even longer, larger demonstrated track record (18 payments
  on a $250K+ contract, "perfect conduct") with a higher aggregate
  exposure ceiling, reflecting Flexi's tiered approach to expanding
  credit based on progressively stronger evidence of reliability.
examples:
  eligible:
    - Customer with an existing $280,000 contract, 18 payments made with
      perfect conduct, applies to take combined exposure to $700,000
      (Primary assets only) -> eligible
  ineligible:
    - Customer with only 12 payments made on their existing contract ->
      not eligible for this $750K pathway; would need to wait until 18
      payments are reached, or use the 9-payment/$500K pathway (EX159) if
      it separately qualifies
business_logic: |
  IF payments_made_on_qualifying_contract >= 18 AND qualifying_contract_amount >= 250000
     AND perfect_conduct_statement_provided == True AND asset_category == "Primary":
    combined_exposure_limit = 750000
    individual_transaction_limit = 500000
  ELSE:
    apply_standard_or_9_payment_pathway_limits  # see EX159
keywords:
  - Increased Exposure
  - New Policy
  - $750K
  - 18 payments
synonyms:
  perfect conduct:
    - clean repayment history
intent_examples:
  - "What's required to reach the $750K combined exposure tier?"
decision: Conditional — Eligible for $750K combined exposure only with 18 payments on a $250K+ contract with perfect conduct, Primary assets only
related_policy:
  - EX159 (Increased Exposure to $500K — the lower, 9-payment tier)
```

```yaml
exception_id: EX161
title: Credit Matrix — New Policy: Tertiary-Only Exposure to $300K Requires Asset-Backed Status
source_document: flexicommercial Credit Matrix — New Policies
policy_statement: >
  "Tertiary Assets Only: after 18 payments have been made... Applications
  from asset backed customers can be considered to take the combined
  exposure to a maximum of $300K (individual transactions to be a
  maximum of $300K)."
interpretation: >
  Unlike the Primary-only pathway (EX160), which doesn't explicitly
  restrict to asset-backed customers, the Tertiary-only increased
  exposure pathway is EXPLICITLY limited to asset-backed customers only —
  non-asset-backed customers cannot access this increased Tertiary
  exposure pathway at all, regardless of payment history.
business_rationale: >
  Tertiary assets already carry the least liquidity/valuation confidence
  in Flexi's asset hierarchy; extending increased exposure for this
  category is only considered acceptable when the customer additionally
  provides property/asset security, not on payment history alone.
examples:
  eligible:
    - Asset-backed customer, 18 payments made on a $150K+ qualifying
      contract with perfect conduct -> eligible for increased Tertiary
      exposure up to $300K
  ineligible:
    - Non-asset-backed customer, otherwise identical payment history ->
      not eligible for this increased exposure pathway; asset backing is
      a mandatory precondition specifically for Tertiary
business_logic: |
  IF asset_category == "Tertiary" AND payments_made >= 18 AND qualifying_contract_amount >= 150000:
    IF asset_backed == True:
      combined_exposure_limit = 300000
      individual_transaction_limit = 300000
    ELSE:
      not_eligible_for_increased_exposure = True  # asset backing mandatory for this pathway
keywords:
  - Increased Exposure
  - Tertiary assets
  - asset backed
  - $300K
synonyms:
  asset backed:
    - property backed
    - secured applicant
intent_examples:
  - "Can a non-asset-backed customer get increased Tertiary exposure?"
decision: Not Eligible for the increased Tertiary exposure pathway without asset-backed status
related_policy:
  - EX160 (New Policy: Primary-Only Exposure to $750K)
```

```yaml
exception_id: EX162
title: Primary Assets Exclude SUVs and Passenger Cars (Including Rental Car Businesses)
source_document: flexicommercial Rate Card / Credit Matrix — Asset Categories
policy_statement: >
  "NB: We do not fund SUVs or passenger cars (this includes rental car
  businesses)."
interpretation: >
  Despite Primary assets including "commercial motor vehicles (utes,
  vans and 4WDs)," SUVs and passenger cars are explicitly excluded —
  and this exclusion extends even to businesses whose core operation IS
  renting out passenger cars/SUVs (rental car businesses), which might
  otherwise be assumed to qualify given the asset is core to their
  trading activity.
business_rationale: >
  Flexi positions itself around commercial/trade-purpose vehicles and
  equipment rather than passenger vehicle finance generally; explicitly
  naming rental car businesses closes an otherwise-plausible loophole
  where a business could argue passenger cars are their "core business
  equipment."
examples:
  eligible:
    - Ute or van (light commercial vehicle) -> eligible under Primary
  ineligible:
    - SUV purchased for a rental car business's fleet -> not eligible,
      even though it is core equipment for that specific business
    - Passenger sedan for any business use -> not eligible
business_logic: |
  IF asset_type IN {"SUV", "passenger_car"}:
    not_eligible = True  # applies even to rental car businesses
keywords:
  - SUV exclusion
  - passenger car exclusion
  - rental car business
synonyms:
  passenger car:
    - sedan
    - passenger vehicle
intent_examples:
  - "Can a rental car business finance SUVs through flexicommercial?"
decision: Not Eligible for SUVs or passenger cars under any circumstances, including rental car businesses
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX163
title: Tertiary Assets Exclude Photocopiers, MFDs, and Scaffolding
source_document: flexicommercial Rate Card / Credit Matrix — Asset Categories
policy_statement: >
  "NB: We do not fund photocopiers, MFDs and scaffolding."
interpretation: >
  Despite falling within the broad Tertiary asset category description
  (office/IT-adjacent equipment), photocopiers, multi-function devices
  (MFDs), and scaffolding are explicitly excluded from financing under
  any circumstances.
business_rationale: >
  These asset types likely carry poor resale/security value (photocopiers/
  MFDs depreciate to near-zero quickly and have thin secondary markets;
  scaffolding is often rented/hired rather than owned in a way that
  suits asset finance security), making them unsuitable even within the
  already-lowest-tier Tertiary category.
examples:
  eligible:
    - POS system or AV equipment (Tertiary category items not on the
      exclusion list) -> eligible
  ineligible:
    - Office photocopier or MFD -> not eligible under any circumstances
    - Scaffolding -> not eligible under any circumstances
business_logic: |
  IF asset_type IN {"photocopier", "MFD", "scaffolding"}:
    not_eligible = True  # hard exclusion, no exceptions
keywords:
  - photocopier
  - MFD
  - scaffolding
  - exclusion
synonyms:
  MFD:
    - multi-function device
    - multi-function printer
intent_examples:
  - "Can I finance an office photocopier under Tertiary assets?"
decision: Not Eligible — hard exclusion for photocopiers, MFDs, and scaffolding
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX164
title: IT/Renewable Energy/Temporary Fencing Capped at $50K Unless Full Doc Provided
source_document: flexicommercial Rate Card / Credit Matrix — Asset Categories footnote ##
policy_statement: >
  "## Maximum exposure $50K. Full doc acceptable for >$50K."
interpretation: >
  IT assets, renewable energy assets, and temporary fencing (all marked
  with the ## footnote) are capped at $50K exposure under standard
  documentation, BUT this cap can be exceeded if Full Doc is provided —
  it is a documentation-conditional cap, not an absolute one.
business_rationale: >
  These asset categories may carry higher technology-obsolescence or
  valuation uncertainty at smaller documentation levels, but Flexi is
  willing to extend beyond $50K when the applicant provides the deeper
  verification that Full Doc requires.
examples:
  eligible:
    - $80,000 renewable energy asset, Full Doc provided -> eligible
      (exceeds $50K, but Full Doc unlocks this)
  ineligible:
    - $80,000 renewable energy asset, standard (non-Full Doc)
      documentation only -> not eligible; exceeds the $50K cap without
      Full Doc
business_logic: |
  IF asset_type IN {"IT_asset", "renewable_energy", "temporary_fencing"}:
    IF exposure_amount > 50000:
      require(documentation_tier == "Full Doc")
    # <=$50K available under standard documentation
keywords:
  - IT assets
  - renewable energy
  - temporary fencing
  - $50K cap
  - Full Doc
synonyms:
  Full Doc:
    - full documentation
intent_examples:
  - "Can I finance $80,000 of IT equipment without Full Doc?"
decision: Not Eligible above $50K without Full Doc for IT assets, renewable energy, and temporary fencing
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX165
title: GPS Attachments — Fixed Devices Require Host Asset Security Unless Capped at $50K/$20K
source_document: flexicommercial Rate Card / Credit Matrix — Asset Categories footnote ###
policy_statement: >
  "### Limited to $100K for portable devices. For applications for fixed
  devices will require security over the host asset, unless the lend is
  limited to $50K for asset backed customers, $20K for non-asset backed
  customers."
interpretation: >
  GPS attachments have THREE distinct rules depending on device type and
  customer profile: (1) portable devices are capped at $100K generally;
  (2) fixed devices normally require security over the "host" asset
  (i.e. the vehicle/equipment the GPS unit is attached to) UNLESS (3)
  the fixed-device lend is kept under a lower cap — $50K for asset-
  backed customers, or just $20K for non-asset-backed customers — in
  which case the host-asset-security requirement is waived.
business_rationale: >
  A GPS unit has little independent security value on its own (it's a
  small, embedded device); requiring security over the host asset
  addresses this for larger fixed-device lends, but Flexi waives this
  extra complexity for smaller transactions where the exposure itself is
  already modest enough to accept without additional security — though
  that smaller threshold is itself lower for non-asset-backed customers.
examples:
  eligible:
    - Fixed GPS device, $18,000 lend, non-asset-backed customer -> eligible
      without host-asset security (below the $20K threshold for this
      customer type)
    - Fixed GPS device, $70,000 lend, asset-backed customer -> requires
      security over the host asset (exceeds the $50K threshold for
      asset-backed customers)
  ineligible:
    - Fixed GPS device, $60,000 lend, non-asset-backed customer, no host-
      asset security offered -> not eligible; exceeds the $20K threshold
      for this customer type, so host-asset security is mandatory
business_logic: |
  IF gps_device_type == "portable":
    max_exposure = 100000
  ELSE IF gps_device_type == "fixed":
    IF asset_backed == True AND exposure <= 50000:
      host_asset_security_required = False
    ELSE IF asset_backed == False AND exposure <= 20000:
      host_asset_security_required = False
    ELSE:
      require(host_asset_security_provided == True)
keywords:
  - GPS attachments
  - fixed device
  - host asset security
  - portable device
synonyms:
  host asset:
    - underlying vehicle
    - attached equipment
intent_examples:
  - "Do I need host asset security for a $15,000 fixed GPS unit?"
decision: Conditional — Host asset security required for fixed GPS devices above the $50K (asset-backed) or $20K (non-asset-backed) thresholds
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX166
title: Forklift On-Hire Businesses Capped at $250K Exposure
source_document: flexicommercial Rate Card / Credit Matrix — Asset Categories footnote ####
policy_statement: >
  "#### Exposures for forklift on-hire businesses are capped at $250K."
interpretation: >
  While materials handling/forklifts generally fall under Primary assets
  (with correspondingly higher exposure limits available under the
  Credit Matrix), businesses whose MODEL is specifically forklift
  ON-HIRE (i.e. renting forklifts out to others) face a dedicated,
  lower $250K exposure cap — overriding the standard Primary asset
  exposure limits that would otherwise apply.
business_rationale: >
  On-hire businesses have a different risk profile than businesses using
  forklifts for their own internal operations — the assets are exposed
  to a wider range of end-users/operators and usage intensity, and the
  underlying business model (equipment rental) carries its own
  commercial risk beyond just the asset's value, justifying a more
  conservative exposure ceiling.
examples:
  eligible:
    - Forklift on-hire business, total exposure request of $220K -> eligible
      (within the $250K on-hire-specific cap)
  ineligible:
    - Forklift on-hire business, total exposure request of $400K -> not
      eligible; capped at $250K regardless of what the standard Primary
      asset Credit Matrix table might otherwise allow for that
      transaction size
business_logic: |
  IF business_model == "forklift_on_hire":
    max_total_exposure = 250000  # overrides standard Primary asset Credit Matrix limits
keywords:
  - forklift
  - on-hire
  - $250K cap
synonyms:
  on-hire business:
    - equipment rental business
intent_examples:
  - "What is the exposure cap for a forklift rental business?"
decision: Not Eligible above $250K total exposure for forklift on-hire businesses, regardless of standard Primary asset limits
related_policy:
  - Section 2 (Asset Categories)
```

```yaml
exception_id: EX167
title: flexipremium Excludes Sole Traders
source_document: flexicommercial Rate Card — flexipremium Eligibility Criteria
policy_statement: >
  "Companies, Trusts, Partnerships (Sole Traders are excluded) trading
  continuously for required time in business."
interpretation: >
  Unlike the standard flexicommercial rates (and the Credit Matrix, whose
  heading explicitly lists "Companies • Trusts • Partnerships • Sole
  Traders" as accepted entity types), the flexipremium product line
  specifically excludes sole traders — this is a flexipremium-specific
  restriction, not a Flexi-wide rule.
business_rationale: >
  flexipremium targets more established businesses with newer assets and
  offers materially better rates; Flexi likely considers sole trader
  structures (lacking the separation of personal/business liability)
  incompatible with the lower-risk profile this premium product is
  designed around.
examples:
  eligible:
    - Company entity, meeting flexipremium's time-in-business and asset-
      age criteria -> eligible
  ineligible:
    - Sole trader entity, otherwise meeting all flexipremium criteria ->
      not eligible for flexipremium; would need to apply under the
      standard flexicommercial rates instead (which do accept sole
      traders per the Credit Matrix heading)
business_logic: |
  IF product == "flexipremium" AND entity_type == "sole_trader":
    not_eligible = True
  ELSE IF product == "flexicommercial standard":
    sole_traders_generally_accepted = True  # per Credit Matrix entity types
keywords:
  - flexipremium
  - sole trader
  - exclusion
synonyms:
  sole trader:
    - individual trader
intent_examples:
  - "Can a sole trader apply for flexipremium rates?"
decision: Not Eligible for flexipremium if the entity type is sole trader — standard flexicommercial rates remain available instead
related_policy:
  - Section 3 (Rate Tables)
```

```yaml
exception_id: EX168
title: flexipremium 5-Year Primary Asset Age Cap Extended for Qualifying Road Transport/Logistics Operators (5+ Trucks)
source_document: flexicommercial Rate Card — flexipremium Eligible Assets
policy_statement: >
  "Primary: up to 5 years old (Contract Road Transport/Logistic
  businesses who operate 5 or more trucks can be considered^)."
interpretation: >
  The standard flexipremium Primary asset age limit is 5 years, but this
  can be extended (considered, not automatic) for businesses in the
  Contract Road Transport/Logistics industry that operate a fleet of 5
  or more trucks — a fleet-size-based carve-out for a specific industry
  segment.
business_rationale: >
  Larger, established transport/logistics fleet operators represent a
  more predictable, lower-risk profile within an industry that Flexi
  otherwise treats cautiously (see EX155, EX169), so Flexi is willing to
  consider relaxing the standard age cap for this specific, larger-scale
  operator profile.
examples:
  eligible:
    - Contract Road Transport business operating 7 trucks, applying for a
      flexipremium facility on an 8-year-old Primary asset -> may be
      considered (subject to the ^ definition in EX169 confirming the
      business genuinely fits "Road Transport/Logistics")
  ineligible:
    - Same business operating only 3 trucks -> does not meet the 5+
      truck threshold; the standard 5-year age cap applies, no extension
      considered
business_logic: |
  IF product == "flexipremium" AND industry == "Contract Road Transport/Logistics" AND fleet_size_trucks >= 5:
    asset_age_may_be_considered_beyond_5_years = True  # discretionary, not automatic
  ELSE:
    max_asset_age_years = 5
keywords:
  - flexipremium
  - Road Transport
  - fleet size
  - asset age extension
synonyms:
  Road Transport/Logistics:
    - freight and logistics industry
intent_examples:
  - "Can a transport business with 6 trucks get an older asset approved under flexipremium?"
decision: Conditional — Age extension only considered for Road Transport/Logistics operators with 5+ trucks; standard 5-year cap otherwise
related_policy:
  - EX169 (flexipremium's Road Transport/Logistics Definition Excludes Construction, Engineering, Agriculture, and Civil Work)
```

```yaml
exception_id: EX169
title: flexipremium's Road Transport/Logistics Definition Excludes Construction, Engineering, Agriculture, and Civil Work
source_document: flexicommercial Rate Card — footnote ^
policy_statement: >
  "^The industry of Road Transport/Logistics includes contract road
  freight, transport services, road vehicle towing, log haulage service
  (road), furniture removal services and truck hire service. It does not
  include: Transport assets required to be used directly in a business
  such as construction services, heavy and civil engineering
  construction, building construction, agriculture; and Civil work (i.e.
  tippers, dogs, agitators, and cranes)."
interpretation: >
  This footnote precisely defines which businesses qualify for the
  5+-truck age extension in EX168 — a business must be genuinely in
  contract road freight, transport services, road vehicle towing, log
  haulage (road), furniture removal, or truck hire. Critically, a
  business that merely USES trucks to support a construction,
  engineering, building, or agricultural operation does NOT qualify,
  even if it owns 5+ trucks — because those trucks are considered
  incidental equipment to a different core industry, not the business
  of "Road Transport/Logistics" itself. Civil work vehicles (tippers,
  dogs, agitators, cranes) are explicitly named as excluded examples.
business_rationale: >
  Prevents businesses in higher-risk or differently-classified
  industries (construction, civil engineering, agriculture) from
  accessing the Road Transport/Logistics fleet-size concession simply by
  owning a qualifying number of trucks — the concession is intended
  specifically for businesses whose core commercial activity IS
  transport/logistics.
examples:
  eligible:
    - Business operating 6 trucks, core activity is contract road
      freight -> qualifies as Road Transport/Logistics
  ineligible:
    - Construction business operating 6 tipper trucks used to support its
      construction projects -> does NOT qualify, even with 6+ trucks;
      tippers are explicitly named as excluded "Civil work" vehicles, and
      the core business (construction) is explicitly excluded from the
      Road Transport/Logistics definition
    - Agricultural business operating 5+ trucks to move produce -> does
      NOT qualify; agriculture is explicitly excluded
business_logic: |
  IF core_business_activity IN {"contract road freight", "transport services",
                                  "road vehicle towing", "log haulage (road)",
                                  "furniture removal services", "truck hire service"}:
    qualifies_as_road_transport_logistics = True
  ELSE IF core_business_activity IN {"construction", "civil engineering",
                                       "building construction", "agriculture"}:
    qualifies_as_road_transport_logistics = False  # explicitly excluded, regardless of truck count
  IF vehicle_type IN {"tipper", "dog trailer", "agitator", "crane"}:
    vehicle_classified_as_civil_work = True  # excluded from the Road Transport/Logistics concession
keywords:
  - Road Transport/Logistics
  - civil work
  - construction exclusion
  - agriculture exclusion
synonyms:
  civil work:
    - tippers
    - agitators
    - dog trailers
intent_examples:
  - "Does a construction company with 6 tipper trucks qualify as Road Transport/Logistics?"
  - "Is agriculture included in the Road Transport/Logistics definition?"
decision: Not Eligible for the Road Transport/Logistics concession if the core business is construction, civil engineering, building, or agriculture, regardless of truck count
related_policy:
  - EX168 (flexipremium 5-Year Age Cap Extension for 5+ Truck Operators)
  - EX174 (Prime Mover 1% Loading Excludes Tippers, Agitators, and Rigid Bodies)
```

```yaml
exception_id: EX170
title: flexipremium Non-Asset-Backed Applicants Require Double the Time in Business (8 Years vs 4 Years)
source_document: flexicommercial Rate Card — flexipremium Time in Business
policy_statement: >
  "Asset backed: ABN and GST registered – minimum of 4 years. Non-asset
  backed: ABN and GST registered – minimum of 8 years."
interpretation: >
  Asset-backed flexipremium applicants need only 4 years of ABN/GST
  tenure, while non-asset-backed applicants need DOUBLE that — 8 years —
  to qualify for flexipremium at all. This is a much larger gap than the
  loading-based approach other lenders in this catalog typically use for
  non-asset-backed risk (e.g. a rate loading); here, it's an eligibility
  threshold difference instead.
business_rationale: >
  Without asset backing as security, Flexi requires a much longer
  demonstrated trading history to compensate, reflecting the higher
  reliance on business longevity/stability as the primary risk mitigant
  in the absence of property security.
examples:
  eligible:
    - Non-asset-backed applicant, 9 years ABN & GST registered -> eligible
      for flexipremium (exceeds the 8-year non-asset-backed minimum)
  ineligible:
    - Non-asset-backed applicant, 5 years ABN & GST registered -> not
      eligible for flexipremium; meets the asset-backed threshold (4
      years) but not the non-asset-backed threshold (8 years) required
      given their lack of security
business_logic: |
  IF product == "flexipremium":
    IF asset_backed == True:
      require(ABN_GST_years >= 4)
    ELSE:
      require(ABN_GST_years >= 8)
keywords:
  - flexipremium
  - time in business
  - non-asset backed
  - 8 years
synonyms:
  time in business:
    - ABN/GST tenure
intent_examples:
  - "How many years in business does a non-asset-backed applicant need for flexipremium?"
decision: Not Eligible for flexipremium with less than 8 years ABN/GST tenure if non-asset-backed (vs 4 years if asset-backed)
related_policy:
  - Section 3 (Rate Tables)
```

```yaml
exception_id: EX171
title: flexipremium Brokerage Capped at 3% (Lower Than Standard Rates)
source_document: flexicommercial Rate Card — flexipremium Note 01
policy_statement: >
  "Note 01: Maximum 3% brokerage applies to flexipremium deals."
interpretation: >
  flexipremium deals cap brokerage at just 3% — significantly lower than
  the standard flexicommercial rates' brokerage caps (8% for deals under
  $50,000, 6% for deals $50,000+, per EX177).
business_rationale: >
  flexipremium already offers more competitive base rates for stronger
  customers; capping brokerage lower keeps the overall cost of finance
  aligned with this product's "competitive rate" positioning, rather
  than allowing broker commission to erode the rate advantage.
examples:
  eligible:
    - flexipremium deal with 3% brokerage -> eligible, no rate impact
  ineligible:
    - flexipremium deal with 5% brokerage requested -> not eligible;
      exceeds the 3% flexipremium-specific cap, even though 5% would be
      within the standard rates' brokerage allowance
business_logic: |
  IF product == "flexipremium":
    max_brokerage_pct = 3%
  ELSE IF product == "flexicommercial standard":
    max_brokerage_pct = 8% (if amount < $50,000) OR 6% (if amount >= $50,000)  # see EX177
keywords:
  - flexipremium
  - brokerage cap
  - 3%
synonyms:
  brokerage:
    - broker commission
intent_examples:
  - "What is the maximum brokerage for a flexipremium deal?"
decision: Not Eligible above 3% brokerage for flexipremium deals, even though standard rates allow more
related_policy:
  - EX177 (Brokerage Cap and Loading Trigger Differ Below vs At/Above $50,000 — standard rates)
```

```yaml
exception_id: EX172
title: Low Start Loan Requires No Cashflow Lenders on File
source_document: flexicommercial flexipremium Low Start Loans Fact Sheet — Conditions
policy_statement: >
  "No cashflow lenders on file (e.g. Prospa, Moula)."
interpretation: >
  If the applicant's credit file shows any cashflow (short-term working
  capital) lender enquiries or facilities — with Prospa and Moula given
  as named examples — the Low Start Loan is not available at all, even
  if the applicant otherwise qualifies for flexipremium.
business_rationale: >
  Cashflow lender activity signals potential short-term liquidity
  stress, which is precisely the kind of risk the Low Start Loan's
  reduced initial repayments are designed to help manage — but Flexi
  considers a customer ALREADY showing cashflow lender reliance too
  risky for this specific product, wanting to see clean serviceability
  fundamentals rather than an existing sign of financial strain.
examples:
  eligible:
    - flexipremium-qualifying applicant, no cashflow lender enquiries on
      file -> eligible for a Low Start Loan
  ineligible:
    - flexipremium-qualifying applicant, with a recent Prospa facility on
      file -> not eligible for a Low Start Loan, even though they
      otherwise qualify for flexipremium itself
business_logic: |
  IF product == "Low Start Loan" AND credit_file_shows_cashflow_lender_activity == True:
    not_eligible = True
keywords:
  - Low Start Loan
  - cashflow lender
  - Prospa
  - Moula
synonyms:
  cashflow lender:
    - short-term working capital lender
intent_examples:
  - "Can a customer with a Prospa loan get a flexipremium Low Start Loan?"
decision: Not Eligible for a Low Start Loan if any cashflow lender activity appears on the credit file
related_policy:
  - Section 1 (Structure Overview)
```

```yaml
exception_id: EX173
title: Low Start Loan Requires an Existing Commercial Asset Finance Facility With an Approved Lender
source_document: flexicommercial flexipremium Low Start Loans Fact Sheet — Conditions
policy_statement: >
  "Must have an existing commercial asset finance facility with an
  approved lender.*"
interpretation: >
  The Low Start Loan is not available to a first-time asset finance
  customer — the applicant must already hold an existing commercial
  asset finance facility with one of the approved lenders (see EX150 for
  the specific list relevant to this product).
business_rationale: >
  Demonstrates that this product is designed to support established
  customers through a temporary cash flow dip (per the fact sheet's
  framing: "ride out economic dips"), not to onboard brand-new asset
  finance customers who have no track record at all.
examples:
  eligible:
    - Applicant with an existing facility with Toyota Finance (an
      approved lender per the Credit Matrix/Low Start Loans list),
      otherwise qualifying for flexipremium -> eligible for a Low Start
      Loan
  ineligible:
    - First-time asset finance customer with no existing facility -> not
      eligible for a Low Start Loan, even if they otherwise qualify for
      standard flexipremium
business_logic: |
  IF product == "Low Start Loan" AND applicant_has_no_existing_commercial_asset_finance_facility:
    not_eligible = True
  ELSE IF existing_facility_lender NOT IN credit_matrix_approved_lender_list:
    not_eligible = True  # must be with an approved lender specifically, see EX150
keywords:
  - Low Start Loan
  - existing facility
  - approved lender
synonyms:
  existing facility:
    - current asset finance facility
intent_examples:
  - "Can a first-time customer get a Low Start Loan?"
decision: Not Eligible without an existing commercial asset finance facility with an approved lender
related_policy:
  - EX150 (flexireplacement Uses a Different Approved Lender List — clarifies which list applies to this product)
  - EX172 (Low Start Loan Requires No Cashflow Lenders on File)
```

```yaml
exception_id: EX174
title: Prime Mover 1% Loading Excludes Tippers, Agitators, and Rigid Bodies
source_document: flexicommercial Rate Card — Standard Rates Loadings
policy_statement: >
  "1.0% >> Prime Movers (excludes Tippers, Agitators, Rigid Bodies,
  etc)."
interpretation: >
  The +1.0% Prime Mover loading applies to genuine prime mover
  (articulated truck tractor) assets, but explicitly does NOT apply to
  Tippers, Agitators, Rigid Bodies, or similar vehicle configurations —
  these are treated differently (likely as standard Primary assets, or
  under the Civil Work classification referenced in EX169) rather than
  attracting the Prime Mover-specific loading.
business_rationale: >
  Tippers, agitators, and rigid-body trucks are structurally and
  functionally different from articulated prime movers (they don't pull
  separate trailers in the same way), and are already separately
  classified as "Civil work" vehicles in the Road Transport/Logistics
  exclusion (EX169) — so it would be inconsistent to also apply the
  Prime Mover loading to them.
examples:
  eligible:
    - Genuine articulated prime mover (truck tractor) -> +1.0% Prime
      Mover loading applies
  ineligible (i.e., the Prime Mover loading does NOT apply):
    - Tipper truck -> does not attract the +1.0% Prime Mover loading
      (though it may still be classified/priced differently as a Civil
      Work vehicle per EX169)
    - Concrete agitator truck -> does not attract the +1.0% Prime Mover
      loading
business_logic: |
  IF asset_type == "prime_mover" AND asset_configuration NOT IN {"tipper", "agitator", "rigid_body"}:
    rate_loading += 1.0%
  ELSE IF asset_configuration IN {"tipper", "agitator", "rigid_body"}:
    prime_mover_loading_does_not_apply = True  # priced under standard/civil work classification instead
keywords:
  - Prime Movers
  - tippers
  - agitators
  - rigid bodies
synonyms:
  Prime Mover:
    - truck tractor
    - articulated truck
intent_examples:
  - "Does the Prime Mover loading apply to a tipper truck?"
decision: Not Applicable to Tippers, Agitators, or Rigid Bodies — the 1% Prime Mover loading applies only to genuine prime movers
related_policy:
  - EX169 (flexipremium's Road Transport/Logistics Definition Excludes Civil Work — tippers, agitators, cranes)
```

```yaml
exception_id: EX175
title: 7-Year Maximum Term Only for Primary Assets Up to 3 Years Old
source_document: flexicommercial Rate Card — Standard Rates
policy_statement: >
  "Maximum term of 7 years on Primary assets up to 3 years old, for all
  other assets the maximum term is 5 years."
interpretation: >
  The longer 7-year maximum term is a narrow exception, available only
  for Primary assets that are themselves no older than 3 years — every
  other combination (older Primary assets, or any Secondary/Tertiary
  asset regardless of age) is capped at a 5-year maximum term.
business_rationale: >
  A newer Primary asset (≤3 years old) has the longest remaining useful
  life and most predictable residual value, justifying the longest
  available term; anything older or in a less liquid asset category
  reverts to the more conservative 5-year standard maximum.
examples:
  eligible:
    - Primary asset, 2 years old, financed over a 7-year term -> eligible
  ineligible:
    - Primary asset, 5 years old, financed over a 7-year term -> not
      eligible; exceeds the 5-year standard maximum term since the asset
      is older than 3 years
    - Secondary asset, 1 year old, financed over a 7-year term -> not
      eligible; the 7-year term is only available for Primary assets,
      regardless of the Secondary asset's age
business_logic: |
  IF asset_category == "Primary" AND asset_age_years <= 3:
    max_term_years = 7
  ELSE:
    max_term_years = 5
keywords:
  - maximum term
  - 7 years
  - Primary assets
synonyms:
  maximum term:
    - loan term cap
intent_examples:
  - "Can a 5-year-old Primary asset get a 7-year term?"
decision: Not Eligible for a 7-year term unless the asset is Primary AND no older than 3 years — 5 years otherwise
related_policy:
  - Section 3 (Rate Tables)
```

```yaml
exception_id: EX176
title: Establishment Fee Increases to $745 for Private Sales and Refinances
source_document: flexicommercial Rate Card — Standard Rates
policy_statement: >
  "Establishment fee of $495 applies to all products; $745 for private
  sales and refinances."
interpretation: >
  The standard establishment fee is $495, but this rises to $745
  specifically for private sale transactions and refinances — an
  additional $250 fee premium for these two transaction types.
business_rationale: >
  Private sales and refinances typically require additional verification
  work (asset inspection/valuation, reviewing existing facility terms,
  confirming payout figures) compared with a standard new dealer-sourced
  purchase, justifying the higher establishment fee to cover this extra
  administrative effort.
examples:
  eligible:
    - Standard new asset purchase from a dealer -> $495 establishment fee
  ineligible (i.e., the higher fee applies instead):
    - Private sale transaction -> $745 establishment fee applies, not $495
    - Refinance transaction -> $745 establishment fee applies, not $495
business_logic: |
  IF transaction_type IN {"private_sale", "refinance"}:
    establishment_fee = 745
  ELSE:
    establishment_fee = 495
keywords:
  - establishment fee
  - private sale
  - refinance
synonyms:
  establishment fee:
    - setup fee
intent_examples:
  - "Is the establishment fee higher for a private sale transaction?"
decision: $745 for private sales and refinances; $495 for all other transactions
related_policy:
  - Section 3 (Rate Tables)
```

```yaml
exception_id: EX177
title: Brokerage Cap and Loading Trigger Differ Below vs At/Above $50,000
source_document: flexicommercial Rate Card — Brokerage
policy_statement: >
  "<$50,000: Max Brokerage 8%. Add 0.5% to above rates for every 1%
  brokerage charged above 5% (up to 8%). ≥$50,000: Max Brokerage 6%. Add
  0.5% to above rates for every 1% brokerage charged above 4% (up to
  6%)."
interpretation: >
  Both the maximum brokerage allowed AND the threshold at which
  additional brokerage starts triggering a rate loading are different
  depending on whether the deal is below or at/above $50,000. Smaller
  deals get a higher brokerage ceiling (8% vs 6%) and a higher loading-
  free threshold (5% vs 4%) than larger deals.
business_rationale: >
  Smaller transactions generate less absolute broker revenue at any
  given percentage, so Flexi allows a higher percentage ceiling and
  loading-free threshold to keep smaller deals commercially viable for
  brokers, while capping both figures more tightly for larger
  transactions where the same percentage represents materially more
  dollar revenue.
examples:
  eligible:
    - $40,000 deal, 7% brokerage (2% above the 5% loading-free threshold
      for this size band) -> +1.0% rate loading applies (2 x 0.5%),
      within the 8% max for this size band
  ineligible:
    - $40,000 deal, 9% brokerage requested -> not eligible; exceeds the
      8% maximum for deals under $50,000
    - $80,000 deal, 7% brokerage (3% above the 4% loading-free threshold
      for this size band) -> +1.5% rate loading applies (3 x 0.5%),
      within the 6% max for this size band; note the SAME 7% brokerage
      triggers a bigger loading here than in the <$50,000 example, and a
      lower cap applies
business_logic: |
  IF deal_amount < 50000:
    max_brokerage_pct = 8%
    loading_free_threshold_pct = 5%
  ELSE:  # deal_amount >= 50000
    max_brokerage_pct = 6%
    loading_free_threshold_pct = 4%
  IF brokerage_pct > loading_free_threshold_pct:
    rate_loading = CEILING(brokerage_pct - loading_free_threshold_pct) * 0.5%
keywords:
  - brokerage
  - $50,000 threshold
  - rate loading
synonyms:
  brokerage:
    - broker commission
intent_examples:
  - "Is the brokerage cap the same for a $40,000 deal as an $80,000 deal?"
decision: Conditional — Brokerage cap and loading trigger threshold both differ based on whether the deal is below or at/above $50,000
related_policy:
  - EX171 (flexipremium Brokerage Capped at 3% — separate, lower cap for that product)
```

```yaml
exception_id: EX178
title: Mid-Term Refinancing Requires 12+ Months Into Current Contract Term
source_document: flexicommercial Mid-Term Refinancing Fact Sheet — Refinancing Framework
policy_statement: >
  "At least 12 months into the term of the current contract."
interpretation: >
  Mid-Term Refinancing is only available once the customer's existing
  contract has been running for at least 12 months — a very early-term
  contract (e.g. 3 months in) cannot be refinanced under this pathway.
business_rationale: >
  Ensures the customer has an established track record on the current
  facility before Flexi considers restructuring it, and that the
  "mid-term" framing is genuinely accurate (not an immediate refinance of
  a brand-new facility).
examples:
  eligible:
    - Contract running for 15 months -> eligible for Mid-Term Refinancing
  ineligible:
    - Contract running for 6 months -> not eligible; has not yet reached
      the 12-month minimum
business_logic: |
  IF months_into_current_contract >= 12:
    eligible_for_mid_term_refinancing = True
  ELSE:
    not_eligible = True
keywords:
  - Mid-Term Refinancing
  - 12 months
  - contract term
synonyms:
  mid-term refinancing:
    - mid-contract refinance
intent_examples:
  - "Can a 6-month-old contract be refinanced under Mid-Term Refinancing?"
decision: Not Eligible before 12 months into the current contract term
related_policy:
  - Section 1 (Structure Overview)
```

```yaml
exception_id: EX179
title: Mid-Term Refinancing Uses Net Book Value — No Early Termination Costs Apply
source_document: flexicommercial Mid-Term Refinancing Fact Sheet — Refinancing Framework
policy_statement: >
  "Deal to be refinanced at the net book value. That is, no early
  termination costs to apply."
interpretation: >
  Unlike a standard early payout (which might typically attract early
  termination costs), Mid-Term Refinancing is explicitly structured so
  that the existing facility is refinanced at its NET BOOK VALUE, with
  NO early termination costs charged — this is a deliberate fee waiver
  built into this specific refinancing pathway.
business_rationale: >
  Positions Mid-Term Refinancing as a genuinely supportive,
  relationship-preserving option for customers facing a cash flow
  crunch (per the fact sheet's framing), rather than penalising them
  with early termination costs on top of the refinance itself.
examples:
  eligible:
    - Existing facility refinanced at net book value, no early
      termination cost charged -> standard, correct treatment under this
      product
  ineligible (i.e., incorrect assumption):
    - Assuming standard early termination costs apply when using Mid-Term
      Refinancing -> incorrect; this product explicitly waives them
business_logic: |
  IF product == "Mid-Term Refinancing":
    refinance_basis = "net_book_value"
    early_termination_costs = 0  # explicitly waived for this product
keywords:
  - Mid-Term Refinancing
  - net book value
  - early termination costs
synonyms:
  net book value:
    - payout at book value
intent_examples:
  - "Are early termination costs charged when refinancing mid-term?"
decision: Not Applicable — early termination costs are explicitly waived under Mid-Term Refinancing
related_policy:
  - EX178 (Mid-Term Refinancing Requires 12+ Months Into Current Contract Term)
```

```yaml
exception_id: EX180
title: Mid-Term Refinancing Brokerage Capped at 1.0% (Far Lower Than Standard)
source_document: flexicommercial Mid-Term Refinancing Fact Sheet — Refinancing Framework
policy_statement: >
  "Brokerage limited to 1.0%. Speak to your flexi BDM if you believe the
  complexity of the deal warrants a higher brokerage."
interpretation: >
  Mid-Term Refinancing caps brokerage at just 1.0% — far below both the
  standard flexicommercial rates' brokerage (6–8%, per EX177) and even
  flexipremium's already-reduced 3% cap (EX171). However, unlike some
  other hard caps in this catalog, there IS an explicit discretionary
  pathway: brokers can request a higher brokerage via their BDM if the
  deal's complexity warrants it.
business_rationale: >
  Reflects that Mid-Term Refinancing is a relatively lower-complexity,
  supportive product (refinancing an existing, already-known facility)
  compared with originating new finance, so standard brokerage is much
  lower by default — but the BDM escalation path acknowledges that some
  refinances may genuinely involve more complexity than the norm.
examples:
  eligible:
    - Standard Mid-Term Refinance, 1.0% brokerage -> eligible, no BDM
      escalation needed
    - Complex Mid-Term Refinance, broker requests 2.5% brokerage with
      BDM approval obtained -> may be eligible with sign-off
  ineligible:
    - Broker charges 2.5% brokerage on a standard Mid-Term Refinance
      without BDM approval -> not eligible; exceeds the 1.0% default cap
      without the required discretionary approval
business_logic: |
  IF product == "Mid-Term Refinancing":
    default_max_brokerage_pct = 1.0%
    IF brokerage_pct > 1.0%:
      require(bdm_approval_for_complexity == True)
keywords:
  - Mid-Term Refinancing
  - brokerage
  - 1.0% cap
  - BDM approval
synonyms:
  brokerage:
    - broker commission
intent_examples:
  - "Can I charge more than 1% brokerage on a Mid-Term Refinance?"
decision: Conditional — 1.0% cap by default; higher brokerage possible only with BDM approval for deal complexity
related_policy:
  - EX171 (flexipremium Brokerage Capped at 3%)
  - EX177 (Brokerage Cap and Loading Trigger Differ Below vs At/Above $50,000 — standard rates)
```

```yaml
exception_id: EX181
title: Mid-Term Refinancing Tolerates a Small Number of Non-Systemic Dishonours
source_document: flexicommercial Mid-Term Refinancing Fact Sheet — Refinancing Framework
policy_statement: >
  "Satisfactory repayment history with no material arrears. A small
  number of non-systemic dishonours may be acceptable."
interpretation: >
  While "no material arrears" is required, Mid-Term Refinancing builds in
  explicit tolerance for a SMALL NUMBER of non-systemic dishonours (i.e.
  occasional, non-pattern dishonours) — this is not a zero-tolerance
  policy on dishonours, unlike some other conduct-based exclusions in
  this catalog.
business_rationale: >
  Recognises that occasional, isolated payment dishonours (e.g. a single
  banking error or timing issue) don't necessarily indicate genuine
  credit risk the way a systemic pattern of dishonours would, allowing
  some flexibility for customers with an otherwise satisfactory
  repayment history.
examples:
  eligible:
    - Customer with satisfactory repayment history and one isolated,
      non-systemic dishonour over the contract's life -> may be
      acceptable
  ineligible:
    - Customer with a systemic/recurring pattern of dishonours -> not
      eligible; this exceeds the "small number of non-systemic" tolerance
      and would likely also fail the "no material arrears" requirement
business_logic: |
  IF product == "Mid-Term Refinancing":
    require(no_material_arrears == True)
    IF dishonour_count > 0:
      IF dishonour_pattern == "non_systemic" AND dishonour_count == "small":
        may_be_acceptable = True  # subject to overall assessment
      ELSE:
        not_eligible = True
keywords:
  - Mid-Term Refinancing
  - dishonours
  - repayment history
synonyms:
  non-systemic dishonour:
    - isolated dishonour
    - one-off dishonour
intent_examples:
  - "Does a single dishonour disqualify a customer from Mid-Term Refinancing?"
decision: Conditional — A small number of non-systemic dishonours may be tolerated; systemic/recurring dishonours are not
related_policy:
  - EX178 (Mid-Term Refinancing Requires 12+ Months Into Current Contract Term)
```

---

*Compiled from the flexicommercial Rate Card (13 July 2026), Credit Matrix — All Entities (effective 8 December
2025), flexireplacement Policy (current as at 1 August 2024), flexipremium Low Start Loans Fact Sheet, Old Finance
Meets New Fact Sheet, and Mid-Term Refinancing Fact Sheet (19 May 2026). This document is a standalone deep-dive
reference intended to sit alongside, and be cross-referenced with, the Resimac, Metro, BFS, and Angle Detailed
References. Verify all figures against flexicommercial's live Broker Portal before operational use, and consult
your BDM for scenarios outside these criteria.*
