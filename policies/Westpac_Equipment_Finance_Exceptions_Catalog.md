# Equipment Finance — Policy Exceptions Catalog

> Consolidated from the following source documents:
> 1. Westpac Rate Special — Xpress (DriveXpress) — 13 July 2026
> 2. Westpac Equipment Finance Key Policies (DriveXpress / Rollover / Replacement / Medical)
> 3. Westpac Equipment Finance Update — PPSR & CoC Settlement Simplification (24 Feb 2025)
> 4. Westpac Rate Special — Hire Purchase, Commercial Loan and Finance Lease — 13 July 2026
> 5. Capital Finance Australia Limited (CFAL) — Equipment Finance Credit Team, Minimum Documentation Checklist
> 6. Resimac Asset Finance — Commercial Product Guide, Auto and Equipment, effective 27 March 2026
>
> Each exception entry uses one unified schema so it can be chunked directly into a RAG knowledge base. Fields:
> `exception_id`, `title`, `source_document`, `policy_statement`, `interpretation`, `business_rationale`, `examples` (eligible/ineligible), `business_logic` (IF–THEN), `keywords`, `synonyms`, `intent_examples`, `decision`, `related_policy`.

---

```yaml
exception_id: EX001
title: Electric Vehicle Rate Discount (DriveXpress)
source_document: Westpac Rate Special — Xpress, 13 July 2026
policy_statement: >
  "For Electric Vehicles, reduce rate by 1%."
interpretation: >
  Any Xpress deal (Licensed Dealer or Private Sale, cars or light commercial
  vehicles) receives a flat 1% reduction off the standard published rate
  when the financed asset is a fully electric vehicle.
business_rationale: >
  Supports the bank's sustainable finance / ESG objectives and reflects
  the historically stable resale value of EVs compared with the broader
  used-vehicle market.
examples:
  eligible:
    - Dealer-sourced EV, up to 5 years old, base rate 7.75% -> 6.75%
    - Privately sourced EV, base rate 8.17% -> 7.17%
  ineligible:
    - Hybrid vehicle (not fully electric) — discount does not apply
    - Plant and equipment (this discount is scoped to the Cars & Light
      Commercial Vehicle category only)
business_logic: |
  IF asset_type == "Electric Vehicle"
  THEN applicable_rate = category_base_rate - 1%
keywords:
  - electric vehicle
  - EV
  - EV discount
  - electric car
synonyms:
  electric vehicle:
    - EV
    - battery electric vehicle
    - BEV
    - new energy vehicle
    - full electric
intent_examples:
  - "Do electric cars get a better rate?"
  - "Is there a discount for financing an EV?"
  - "What rate applies to a Tesla under DriveXpress?"
  - "Does the EV discount apply to hybrids?"
decision: Conditional — Eligible if asset is fully electric
related_policy:
  - EX014 (Electric Vehicle Discount — HP/Commercial Loan/Finance Lease)
  - DriveXpress Rate Table (Category A)
```

---

```yaml
exception_id: EX002
title: Private Sale Eligibility Scope Restriction (DriveXpress)
source_document: Westpac Equipment Finance Key Policies / Rate Special — Xpress
policy_statement: >
  "*Xpress Private Sales applicable for Cars/Light Commercial only."
  "Private Sale only on Motor Vehicles or Light Commercial Vehicles
  <4.5 tonnes GVM."
interpretation: >
  The Xpress private-sale fast-track channel is restricted to Category A
  assets (passenger cars and light commercial vehicles under 4.5T GVM).
  Trucks, plant, agricultural equipment and other Category B/C assets
  cannot be financed via a private-sale Xpress deal.
business_rationale: >
  Verifying ownership, condition and value from a private (non-dealer)
  seller carries materially higher risk. The bank limits private-sale
  eligibility to standardised, liquid asset types with mature second-hand
  markets.
examples:
  eligible:
    - Private purchase of a 3-year-old passenger car
  ineligible:
    - Private purchase of an excavator (Category B — requires standard
      application, not Xpress private sale)
business_logic: |
  IF transaction_type == "Private Sale" AND asset_category != "A"
  THEN reject_from_xpress_channel -> route_to_standard_application
keywords:
  - private sale
  - non-dealer sale
  - private seller
synonyms:
  private sale:
    - private purchase
    - non-dealer transaction
    - individual seller
intent_examples:
  - "Can I buy machinery from a private seller through Xpress?"
  - "Is a private sale truck eligible for fast-track finance?"
  - "What vehicle types qualify for private sale finance?"
decision: Conditional — Eligible only for Category A assets
related_policy:
  - DriveXpress Customer Type Table
  - Asset Category A/B/C Definitions
```

---

```yaml
exception_id: EX003
title: Mobile / Tight Access Crane Age Limit Reduction
source_document: Westpac Equipment Finance Key Policies (Category B)
policy_statement: >
  "Category B: Up to 5 Years Old (*cranes up to 3 years only)."
interpretation: >
  While Category B assets (trucks, forklifts, excavators, etc.) are
  generally eligible up to 5 years old, mobile and tight-access cranes
  are restricted to a maximum age of 3 years — overriding the default
  Category B age limit.
business_rationale: >
  Cranes carry higher structural/safety compliance risk and depreciate
  faster than other heavy equipment, so the bank tightens the acceptable
  asset age to control residual/security risk.
examples:
  eligible:
    - 4-year-old excavator (within the standard 5-year Category B limit)
  ineligible:
    - 4-year-old mobile crane (exceeds the 3-year sub-limit; requires
      credit exception or decline)
business_logic: |
  IF asset_category == "B" AND asset_subtype == "Mobile/tight access crane"
  THEN max_age_years = 3
  ELSE IF asset_category == "B"
  THEN max_age_years = 5
keywords:
  - crane
  - mobile crane
  - tight access crane
synonyms:
  crane:
    - mobile crane
    - tight access crane
    - lifting equipment
intent_examples:
  - "How old can a crane be to qualify for finance?"
  - "Is a 4-year-old mobile crane eligible under Category B?"
  - "Do cranes follow the same age rule as trucks and excavators?"
decision: Conditional — Max age 3 years (not the standard 5 years)
related_policy:
  - Category B Asset List
  - DriveXpress / Replacement Age Tables
```

---

```yaml
exception_id: EX004
title: Government / School / Local Route Bus Extended Loan Term (Replacement)
source_document: Westpac Equipment Finance Key Policies (Replacement — Category C)
policy_statement: >
  "Category C (Replacement only): Up to 5 years old, up to 10-year loan
  term (Dealer only) — Govt/school/local route buses (excludes charter)."
interpretation: >
  Under the Replacement product only, government, school, and local
  public-route buses can be financed with a loan term of up to 10 years
  — well beyond the standard 3–7-year terms — but charter buses are
  explicitly excluded.
business_rationale: >
  Public-sector and public-transport assets have long service lives and
  are backed by stable government/institutional cash flow, justifying a
  longer amortisation period. Charter operations carry more commercial
  volatility and do not receive this extension.
examples:
  eligible:
    - Municipal government bus fleet, 9-year loan term requested
  ineligible:
    - Tourism charter bus operator requesting a 10-year term (excluded
      by definition)
business_logic: |
  IF customer_type IN {government, school, local_route_operator}
     AND asset_type == "bus" AND usage != "charter"
  THEN max_loan_term_years = 10   # Replacement product only
  ELSE max_loan_term_years = standard_term (typically 5-7 years)
keywords:
  - school bus
  - government bus
  - route bus
  - public transport
  - charter bus
synonyms:
  bus:
    - coach
    - route bus
    - school bus
    - government fleet vehicle
  charter bus:
    - tour bus
    - private hire bus
intent_examples:
  - "Can a school bus be financed over 10 years?"
  - "Is a charter bus eligible for the extended loan term?"
  - "What loan term applies to government bus fleets?"
decision: Conditional — 10-year term only for non-charter public buses under Replacement
related_policy:
  - Replacement Product Policy
  - Category C Asset List
```

---

```yaml
exception_id: EX005
title: Medical Specialist vs Allied Health Practitioner Differentiated Limits
source_document: Westpac Equipment Finance Key Policies (Medical)
policy_statement: >
  Medical Specialists/GPs/Dentists/Vets and Allied Health Practitioners
  receive different maximum loan amounts under the same Medical product
  (e.g. Motor Vehicle <$250,000 vs <$150,000; New Medical Equipment
  <$500,000 vs <$250,000).
interpretation: >
  Within the single Medical finance policy, the borrower's specific
  profession determines which limit table applies. Core medical
  professionals are given materially higher ceilings than allied health
  professionals.
business_rationale: >
  Core medical professionals typically have higher income stability,
  stricter licensing barriers to entry, and lower historical default
  rates, warranting higher credit limits.
examples:
  eligible:
    - GP applying for $400,000 of new medical equipment (within the
      $500k GP/Specialist limit)
  ineligible:
    - Physiotherapist (Allied Health) applying for $400,000 of the same
      equipment (exceeds the $250k Allied Health limit; requires
      downsizing or standard application)
business_logic: |
  IF profession IN {Medical Specialist, GP, Dentist, Vet}
  THEN limit_tier = "high"
  ELSE IF profession IN {Occupational Therapist, Optometrist, Osteopath,
       Physiotherapist, Chiropractor, Audiologist, Pathology Services,
       Podiatrist, Psychologist, Speech Pathologist}
  THEN limit_tier = "low"
  # Note: Pharmacists are NOT included in the Allied Health definition
keywords:
  - medical finance
  - allied health
  - medical specialist
  - GP
  - vet
  - dentist
synonyms:
  allied health practitioner:
    - physiotherapist
    - podiatrist
    - psychologist
    - optometrist
    - chiropractor
    - occupational therapist
  medical specialist:
    - GP
    - general practitioner
    - dentist
    - veterinarian
intent_examples:
  - "How much can a GP borrow for medical equipment?"
  - "Is a physiotherapist eligible for the same limits as a specialist?"
  - "Does a pharmacist count as allied health?"
decision: Conditional — Limit tier depends on borrower's exact profession
related_policy:
  - Medical Product Limit Table
  - Allied Health Practitioner Definition List
```

---

```yaml
exception_id: EX006
title: Computers, Fixtures & Fittings Excluded (New Plant and Equipment)
source_document: Westpac Rate Special — Hire Purchase, Commercial Loan and Finance Lease, 13 July 2026
policy_statement: >
  "New Plant and Equipment — Excluding Computers, Fixtures & Fittings."
interpretation: >
  The published tiered rate table for New Plant and Equipment does not
  apply to computers, fixtures, or fittings. These asset types fall
  outside the standard rate card and must be priced separately
  ("call us for a quote").
business_rationale: >
  Computers, fixtures, and fittings depreciate differently from core
  plant/equipment (faster obsolescence for IT hardware; low resale
  liquidity for fit-out items), so they do not fit the standard
  plant-and-equipment risk/pricing curve and require individual
  assessment.
examples:
  eligible:
    - Standard construction excavator, $80,000 — priced from the
      published Plant & Equipment table
  ineligible:
    - Office laptops/desktops — must be quoted individually, not from
      the standard table
    - Office fit-out (built-in cabinetry, partitions) — must be quoted
      individually
    - POS terminal / air-conditioning system as part of a fit-out — must
      be quoted individually
business_logic: |
  IF asset_type IN {computer, laptop, desktop, server, fixture, fitting}
  THEN standard_plant_equipment_rate_table = NOT_APPLICABLE
       -> require_bespoke_quote (call WEF Deal Build / Broker Support)
keywords:
  - computer
  - laptop
  - desktop
  - server
  - furniture
  - office furniture
  - cabinetry
  - workstation
  - POS terminal
synonyms:
  computer:
    - PC
    - notebook
    - IT equipment
  fixture:
    - permanent installation
    - built-in cabinet
    - HVAC
    - commercial kitchen
  fitting:
    - office furniture
    - desk
    - chair
    - workstation
    - filing cabinet
intent_examples:
  - "Can I finance office furniture?"
  - "Is a POS terminal eligible?"
  - "Are desks and chairs covered?"
  - "Can I finance air-conditioning?"
  - "Is a commercial kitchen considered plant and equipment?"
decision: Not Eligible (under standard rate table) — requires bespoke quote
related_policy:
  - HP / Commercial Loan / Finance Lease Rate Table
  - Asset Finance Policy
```

---

```yaml
exception_id: EX007
title: Modification / Aftermarket Accessory Funding Cap
source_document: Westpac Equipment Finance Key Policies (DriveXpress Note 1)
policy_statement: >
  "Note 1: Funding of any additional modifications or aftermarket
  accessories to be no more than 10% of the dealer invoice / purchase
  price."
interpretation: >
  Modifications and aftermarket accessories can be bundled into the
  finance contract, but the funded value of those additions cannot
  exceed 10% of the primary asset's invoice/purchase price.
business_rationale: >
  Limits exposure to non-standardised, hard-to-value additions that have
  little resale/security value if the loan needs to be recovered.
examples:
  eligible:
    - Truck invoice $100,000; $8,000 tray modification funded (8% <= 10%)
  ineligible:
    - Truck invoice $100,000; $15,000 modification requested (15% > 10%;
      excess must be self-funded or declined)
business_logic: |
  IF modification_value > (primary_asset_invoice_price * 0.10)
  THEN excess_amount_not_fundable
keywords:
  - modification
  - aftermarket accessories
  - customisation
synonyms:
  modification:
    - aftermarket accessory
    - customisation
    - fit-out addition
intent_examples:
  - "Can I finance a custom tray on top of the truck price?"
  - "Is there a limit on aftermarket accessories I can add to the loan?"
  - "How much modification cost can be bundled into DriveXpress?"
decision: Conditional — Capped at 10% of primary asset invoice price
related_policy:
  - DriveXpress Notes
  - Category A/B/C Definitions
```

---

```yaml
exception_id: EX008
title: Tractor / Yellow Goods Attachment Bundling Requirement
source_document: Westpac Equipment Finance Key Policies (DriveXpress Note 2)
policy_statement: >
  "Note 2: Tractor/yellow good attachments must be funded together with
  the tractor/primary asset."
interpretation: >
  Attachments for tractors and "yellow goods" (e.g. ploughs, buckets,
  implements) cannot be financed as a standalone item — they must be
  included in the same contract as the primary machine.
business_rationale: >
  Attachments have negligible standalone security value and cannot be
  recovered/resold independently at meaningful value, so they are only
  fundable when tied to the primary asset that gives them utility.
examples:
  eligible:
    - Tractor + matching plough financed together in one contract
  ineligible:
    - Standalone plough finance request where the tractor is not part of
      the same (or an existing Westpac) contract
business_logic: |
  IF financed_item == "attachment" AND primary_machine_not_in_same_contract
  THEN reject_application -> require_resubmission_with_primary_asset
keywords:
  - attachment
  - yellow goods
  - implement
  - plough
synonyms:
  attachment:
    - implement
    - yellow goods accessory
    - farm equipment attachment
intent_examples:
  - "Can I finance a plough on its own?"
  - "Do tractor attachments need to be bundled with the tractor?"
  - "Is a standalone bucket attachment eligible for finance?"
decision: Not Eligible as a standalone item — must be bundled with primary asset
related_policy:
  - DriveXpress Notes
  - Category C Asset List
```

---

```yaml
exception_id: EX009
title: No Minus Equity on Trade-Ins
source_document: Westpac Equipment Finance Key Policies (DriveXpress Note 3)
policy_statement: >
  "Note 3: No minus equity on trade-ins."
interpretation: >
  If an outgoing asset's outstanding loan balance exceeds its trade-in
  valuation (i.e. negative equity), that shortfall cannot be rolled into
  the new finance contract.
business_rationale: >
  Prevents an existing bad-debt/loss position from being disguised as
  part of a new loan, which would artificially inflate the new
  contract's leverage and risk.
examples:
  eligible:
    - Old asset loan balance $20,000; trade-in valuation $25,000
      (positive equity $5,000, can offset new purchase)
  ineligible:
    - Old asset loan balance $30,000; trade-in valuation $22,000
      (negative equity $8,000 — shortfall must be paid in cash, cannot
      be rolled into the new loan)
business_logic: |
  IF (outgoing_asset_loan_balance - trade_in_valuation) > 0
  THEN shortfall_not_fundable -> require_cash_settlement_or_decline
keywords:
  - trade-in
  - negative equity
  - minus equity
synonyms:
  negative equity:
    - minus equity
    - trade-in shortfall
    - upside-down loan
intent_examples:
  - "Can I roll negative equity from my old vehicle into a new loan?"
  - "What happens if my trade-in is worth less than what I owe?"
  - "Is a trade-in shortfall allowed to be financed?"
decision: Not Eligible — shortfall must be settled in cash
related_policy:
  - DriveXpress Notes
  - Replacement Product Policy
```

---

```yaml
exception_id: EX010
title: PPSR Company Search Waiver (VIN Motor Vehicles, Private Sale/Buyback)
source_document: Westpac Equipment Finance Update, effective 24 Feb 2025
policy_statement: >
  "Where the financed asset is a motor vehicle with a VIN, and the sale
  is a buyback or private sale, a PPSR company search over a private
  seller or customer will no longer be required."
interpretation: >
  For buyback or private-sale transactions involving a motor vehicle
  identified by a VIN, the pre-settlement PPSR company search on the
  seller is waived, provided a VIN-level search on the day of/before
  settlement shows no other registration.
business_rationale: >
  A VIN is uniquely identifying, so a VIN-specific search already
  provides sufficient ownership/encumbrance assurance without the added
  administrative step of a full company PPSR search, reducing
  settlement delays.
examples:
  eligible:
    - Private sale of a VIN-identified car; VIN search the day before
      settlement shows no other registration -> company search waived
  ineligible:
    - Asset identified by PIN/HIN/VH (not VIN, e.g. boats, trailers) —
      standard company PPSR search process still applies
    - VIN search reveals an existing registration -> waiver does not
      apply; standard process (including Deed of Release) required
business_logic: |
  IF transaction_type IN {buyback, private_sale}
     AND asset_serial_type == "VIN"
     AND vin_search_result(day_of_or_before_settlement) == "no other registration"
  THEN waive_ppsr_company_search
  ELSE follow_standard_ppsr_process
keywords:
  - PPSR
  - VIN
  - buyback
  - private sale
  - Deed of Release
synonyms:
  PPSR:
    - Personal Property Securities Register
    - company search
  buyback:
    - trade-in repurchase
intent_examples:
  - "Do I still need a PPSR search for a private sale car?"
  - "Is a company PPSR search required for a VIN vehicle buyback?"
  - "What happens if the VIN search shows another registration?"
decision: Conditional — Waived only for VIN motor vehicles with a clean pre-settlement search
related_policy:
  - Equipment Finance Update (Change 1)
  - Exclusions & Notes — Private Sale Scope
```

---

```yaml
exception_id: EX011
title: Fleet Policy CoC Asset Detail Waiver
source_document: Westpac Equipment Finance Update, effective 24 Feb 2025
policy_statement: >
  "Where the CoC confirms that the policy is a 'fleet policy', there will
  no longer be a requirement to include the asset detail on the CoC.
  This applies only for all motor vehicles and does not apply to any
  other asset types."
interpretation: >
  For financed assets above $150k, a Certificate of Currency (CoC) is
  required to confirm insurance. If the CoC confirms the policy is a
  fleet policy AND the asset is a motor vehicle, the CoC no longer needs
  to list the specific asset detail (VIN/Serial No) — it only needs to
  note Westpac's interest.
business_rationale: >
  A fleet policy already covers all vehicles under the customer's name,
  making per-asset listing redundant for large fleet customers and
  simplifying settlement paperwork. Non-vehicle assets are not covered
  by this simplification because they fall outside standard fleet policy
  structures.
examples:
  eligible:
    - Customer with a 50-vehicle fleet policy; CoC states "fleet policy"
      and notes Westpac's interest — no VIN listing required
  ineligible:
    - $200,000 excavator under a "fleet policy" — waiver does not apply
      (non-motor-vehicle asset); CoC must still list the serial number
    - Asset valued at $100,000 (below the $150k CoC threshold) — CoC not
      required at all, so this waiver is not triggered
business_logic: |
  IF asset_value > 150000 AND asset_type == "Motor Vehicle"
     AND coc_notes == "fleet policy"
  THEN waive_asset_detail_on_coc  # still require Westpac's interest noted
  ELSE IF asset_value > 150000
  THEN require_coc_with_westpac_interest_and_asset_detail
keywords:
  - CoC
  - Certificate of Currency
  - fleet policy
  - insurance
synonyms:
  CoC:
    - Certificate of Currency
    - insurance certificate
  fleet policy:
    - fleet insurance
    - blanket vehicle policy
intent_examples:
  - "Does a fleet insurance policy need to list the VIN on the CoC?"
  - "Is the CoC waiver available for plant and equipment?"
  - "Do I need a CoC for a $100,000 asset?"
decision: Conditional — Waived only for motor vehicles under a confirmed fleet policy above $150k
related_policy:
  - Equipment Finance Update (Change 2)
```

---

```yaml
exception_id: EX012
title: Spouse-Owned Residential Property Accepted at Credit Discretion
source_document: Westpac Equipment Finance Key Policies (Exclusions & Notes)
policy_statement: >
  "Residential property in spouses name may be accepted at credit
  discretion."
interpretation: >
  Several product lines (e.g. DriveXpress "New to Business Bank",
  Replacement "New Clients") require the borrower to own residential
  property. Property registered in a spouse's name may still satisfy
  this requirement, but only at the discretion of the credit assessor —
  it is not an automatic pass.
business_rationale: >
  Household finances are often shared, so spousal property ownership can
  still indicate financial stability, but because the borrower does not
  hold the asset directly, legal recourse differs — hence manual
  judgement is retained rather than automatic approval.
examples:
  eligible:
    - Married applicant; residential property registered to spouse;
      other financials strong -> may be approved at credit discretion
  ineligible:
    - Single applicant with no property, or property registered to a
      non-spouse third party (e.g. parent) -> this exception does not
      apply; standard "no property" pathway applies
business_logic: |
  IF borrower_does_not_own_residential_property
     AND spouse_owns_residential_property
     AND marital_relationship_verifiable
  THEN refer_to_credit_discretion  # not auto-approved
  ELSE treat_as_no_residential_property
keywords:
  - spouse property
  - residential property
  - credit discretion
synonyms:
  spouse property:
    - spousal property
    - partner-owned property
intent_examples:
  - "Can I use my spouse's house to meet the property-owner requirement?"
  - "Does property in my partner's name count for New to Business Bank?"
  - "Is spousal property automatically accepted?"
decision: Conditional — Subject to credit assessor discretion, not automatic
related_policy:
  - DriveXpress / Replacement "Owns Residential Property" Criteria
```

---

```yaml
exception_id: EX013
title: Medical Sale & Hireback 30-Day Window Exception
source_document: Westpac Equipment Finance Key Policies (Exclusions & Notes; Medical Criteria)
policy_statement: >
  General exclusion: "Excludes Sale and Hire back and Novated Lease."
  Medical criteria: "Sale and hire back where asset was purchased less
  than 30 days prior."
interpretation: >
  Sale & Hireback is excluded as a general rule across products. However,
  under the Medical product line specifically, a narrow exception allows
  Sale & Hireback where the asset was purchased within the last 30 days.
business_rationale: >
  Sale & Hireback is generally higher risk (potential for cash-out
  schemes or inflated valuations). For assets purchased very recently,
  invoice pricing and asset authenticity are still highly verifiable, so
  the risk is manageable — allowing medical practices to quickly recoup
  cash flow after equipment purchases.
examples:
  eligible:
    - Dental practice purchased $80,000 of equipment 15 days ago and now
      applies for Sale & Hireback
  ineligible:
    - Same practice applying for Sale & Hireback on equipment purchased
      8 months ago (exceeds the 30-day window)
    - Non-medical customer (e.g. retail business) applying for Sale &
      Hireback (exception is scoped to the Medical product only)
business_logic: |
  IF product_line == "Medical" AND transaction_type == "Sale & Hireback"
     AND (today - asset_purchase_date) <= 30 days
  THEN allow_application  # exception applies
  ELSE apply_general_exclusion  # Sale & Hireback not permitted
keywords:
  - sale and hireback
  - sale leaseback
  - medical equipment finance
synonyms:
  sale and hireback:
    - sale and leaseback
    - cash-out finance
intent_examples:
  - "Can I sell and lease back medical equipment I just bought?"
  - "Is Sale & Hireback allowed for a dental practice?"
  - "What's the time limit for Sale & Hireback eligibility?"
decision: Conditional — Eligible only within 30 days of original purchase, Medical product only
related_policy:
  - Exclusions & Notes — General Rule
  - Medical Product Policy
```

---

```yaml
exception_id: EX014
title: Used Motor Vehicle Age Rate Loading (4–10 Years, +0.75%)
source_document: Westpac Rate Special — Hire Purchase, Commercial Loan and Finance Lease, 13 July 2026
policy_statement: >
  "Used Motor Vehicles between 4 to 10 years old ADD 0.75%."
interpretation: >
  The published rate table applies to new motor vehicles up to 4 years
  old. For used vehicles aged between 4 and 10 years, a flat 0.75% rate
  loading is added on top of the base rate.
business_rationale: >
  Older vehicles carry higher depreciation and mechanical risk, so the
  bank prices in additional margin to compensate for the increased
  security/residual risk.
examples:
  eligible:
    - 6-year-old ute financed at $30,000; base rate 8.42% + 0.75% = 9.17%
  ineligible:
    - Vehicle older than 10 years — falls outside this loading rule and
      requires a bespoke quote ("call us for a quote")
business_logic: |
  IF vehicle_age_years > 4 AND vehicle_age_years <= 10
  THEN applicable_rate = base_rate + 0.75%
  ELSE IF vehicle_age_years > 10
  THEN require_bespoke_quote
keywords:
  - used vehicle
  - vehicle age loading
  - rate loading
synonyms:
  used vehicle:
    - second-hand vehicle
    - pre-owned vehicle
intent_examples:
  - "What rate applies to a 6-year-old used truck?"
  - "Is there a surcharge for older vehicles?"
  - "Can I finance a vehicle older than 10 years?"
decision: Conditional — +0.75% loading for 4–10 year old vehicles; bespoke quote beyond 10 years
related_policy:
  - HP / Commercial Loan / Finance Lease Rate Table
  - EX006 (Computers, Fixtures & Fittings Excluded)
```

---

```yaml
exception_id: EX015
title: Electric Vehicle Discount — HP / Commercial Loan / Finance Lease
source_document: Westpac Rate Special — Hire Purchase, Commercial Loan and Finance Lease, 13 July 2026
policy_statement: >
  "For Electric Vehicles, reduce rate by 1%."
interpretation: >
  Under the HP/Commercial Loan/Finance Lease rate card (a separate
  product line from DriveXpress/Xpress), electric vehicles also receive
  a 1% rate reduction against the applicable New Motor Vehicle tier rate.
business_rationale: >
  Consistent with the bank-wide EV incentive strategy applied across
  product lines, encouraging green asset finance regardless of which
  finance structure the customer chooses.
examples:
  eligible:
    - New EV financed at $40,000 (tier $20,000<$50,000), base rate 8.42%
      -> 7.42%
  ineligible:
    - EV financed under the New Plant and Equipment table where the
      asset itself is a computer/fixture/fitting (EX006 exclusion takes
      precedence)
business_logic: |
  IF asset_type == "Electric Vehicle" AND product IN {HP, Commercial Loan, Finance Lease}
  THEN applicable_rate = tier_base_rate - 1%
keywords:
  - electric vehicle
  - EV discount
  - HP
  - Commercial Loan
  - Finance Lease
synonyms:
  electric vehicle:
    - EV
    - battery electric vehicle
    - BEV
intent_examples:
  - "Does the EV discount apply under a Commercial Loan?"
  - "Is Finance Lease pricing different for electric vehicles?"
decision: Conditional — Eligible if asset is fully electric, under HP/Commercial Loan/Finance Lease
related_policy:
  - EX001 (Electric Vehicle Rate Discount — DriveXpress)
  - HP / Commercial Loan / Finance Lease Rate Table
```

---

```yaml
exception_id: EX016
title: Rates by Negotiation Above $150,000 (HP/Commercial Loan/Finance Lease)
source_document: Westpac Rate Special — Hire Purchase, Commercial Loan and Finance Lease, 13 July 2026
policy_statement: >
  "Amount Financed $150,000+ — By negotiation." Applies to both New
  Motor Vehicles and New Plant and Equipment tables.
interpretation: >
  The published fixed-rate tiers only cover financed amounts up to
  $150,000. Above that threshold, no standard rate is quoted — pricing
  must be individually negotiated.
business_rationale: >
  Larger transactions carry customer-specific risk profiles and
  competitive dynamics that a flat published rate cannot adequately
  price; individual negotiation allows risk-based and relationship-based
  pricing.
examples:
  eligible:
    - $200,000 truck finance request — routed to negotiated pricing, not
      the standard table
  ineligible:
    - $120,000 request — still falls within the standard published tier
      ($50,000<$150,000) and does not require negotiation
business_logic: |
  IF amount_financed >= 150000
  THEN rate = "by negotiation"  # not available on the standard table
  ELSE rate = standard_tier_rate(amount_financed)
keywords:
  - by negotiation
  - large transaction
  - rate tier
synonyms:
  by negotiation:
    - bespoke pricing
    - individually priced
intent_examples:
  - "What rate applies to a $200,000 equipment loan?"
  - "Is there a standard rate for large finance amounts?"
decision: Not Standard — Requires individual negotiation above $150,000
related_policy:
  - HP / Commercial Loan / Finance Lease Rate Table
  - EX019 (Escalated Documentation Requirements >$500k, CFAL)
```

---

```yaml
exception_id: EX017
title: HP/Commercial Loan/Finance Lease Rates Mutually Exclusive with Xpress Deals
source_document: Westpac Rate Special — Hire Purchase, Commercial Loan and Finance Lease, 13 July 2026
policy_statement: >
  "Rates exclude Xpress Deals." Brokerage on this rate card is built in
  up to 3%, with additional brokerage up to 4% available by negotiation.
interpretation: >
  This rate card only applies to standard Hire Purchase, Commercial
  Loan, and Finance Lease transactions. Deals processed under the
  Xpress/DriveXpress channel use a separate, dedicated rate card (see
  EX001/EX002) and cannot use these rates.
business_rationale: >
  Xpress deals follow a distinct fast-track credit and pricing model;
  keeping the two rate cards separate avoids pricing conflicts and
  ensures brokers apply the correct rate structure for the correct
  channel.
examples:
  eligible:
    - Standard commercial loan application (non-Xpress) — uses this
      rate card
  ineligible:
    - Deal processed through DriveXpress — must use the Xpress-specific
      rate card, not this one
business_logic: |
  IF deal_channel == "Xpress"
  THEN use_xpress_rate_card  # this HP/CL/FL rate card does not apply
  ELSE use_hp_cl_fl_rate_card
keywords:
  - Xpress deal
  - brokerage
  - rate card
synonyms:
  Xpress deal:
    - DriveXpress transaction
    - fast-track deal
intent_examples:
  - "Can I use the HP rate card for a DriveXpress deal?"
  - "How much brokerage is included in the standard rate?"
  - "Is additional brokerage above 3% possible?"
decision: Not Eligible — this rate card excludes Xpress deals (separate rate card applies)
related_policy:
  - EX001 (Electric Vehicle Discount — DriveXpress)
  - HP / Commercial Loan / Finance Lease Rate Table
```

---

```yaml
exception_id: EX018
title: Matrix Policy Reduced Documentation Requirement (CFAL)
source_document: Capital Finance Australia Limited (CFAL) — Minimum Documentation Checklist
policy_statement: >
  "Matrix refers to Motor Vehicle Policy, Small Ticket Policy,
  Replacement Policy & Roll-Over Policy." Deals under these four Matrix
  policies follow the same reduced documentation checklist as the
  "<=$250k" tier, regardless of the actual transaction size.
interpretation: >
  Instead of scaling documentation strictly by transaction size, deals
  that fall under one of the four Matrix policies (Motor Vehicle, Small
  Ticket, Replacement, Roll-Over) are entitled to the lighter,
  <=$250k-equivalent documentation set even if the transaction size
  would otherwise sit in a higher tier.
business_rationale: >
  These four policy types are considered lower-risk/standardised
  transaction categories, so CFAL streamlines documentation regardless
  of ticket size to speed up approvals for well-understood asset/deal
  structures.
examples:
  eligible:
    - $400,000 transaction structured under the Roll-Over Policy — only
      requires the reduced Matrix-tier document set (brief background,
      no full financial statements)
  ineligible:
    - $400,000 transaction NOT structured under one of the four Matrix
      policies — must follow the standard >$250k-$500k documentation
      tier (detailed background, 2 years financials, tax returns, etc.)
business_logic: |
  IF policy_type IN {Motor Vehicle Policy, Small Ticket Policy,
                      Replacement Policy, Roll-Over Policy}
  THEN documentation_tier = "Matrix"  # equivalent to <=$250k tier
  ELSE documentation_tier = size_based_tier(transaction_size)
keywords:
  - Matrix policy
  - Motor Vehicle Policy
  - Small Ticket Policy
  - Replacement Policy
  - Roll-Over Policy
synonyms:
  Matrix policy:
    - fast-track policy
    - standardised policy
intent_examples:
  - "Does a Roll-Over deal need full financial statements?"
  - "What documentation is required for a Small Ticket transaction over $250k?"
  - "Which policies qualify for reduced documentation regardless of size?"
decision: Conditional — Reduced documentation applies regardless of transaction size, for the four listed Matrix policies only
related_policy:
  - CFAL Documentation Checklist
  - EX019 (Documentation Threshold Waiver <=$250k)
```

---

```yaml
exception_id: EX019
title: Documentation Threshold Waiver for Transactions ≤$250k (CFAL)
source_document: Capital Finance Australia Limited (CFAL) — Minimum Documentation Checklist
policy_statement: >
  Financial Statements (last 2 years), tax returns, Current Tax Portal,
  and several other financial information items are only required for
  transactions above $250,000. Deals at or below $250,000 (and Matrix
  policy deals) are exempt from these financial-statement requirements.
interpretation: >
  Small-ticket transactions (<=$250k) do not require submission of full
  financial statements or tax returns — only lighter application-level
  information (client info, ABN/GST status, goods description, reason
  for purchase, signed privacy form) is required.
business_rationale: >
  For smaller transactions, the cost/time of collecting full financials
  outweighs the incremental risk benefit; CFAL instead relies on credit
  bureau checks and basic application data to keep approvals fast for
  low-risk, low-value deals.
examples:
  eligible:
    - $180,000 equipment purchase — only application/customer details
      required, no financial statements needed
  ineligible:
    - $300,000 equipment purchase (non-Matrix policy) — falls into the
      >$250k-$500k tier and requires 2 years of financial statements and
      tax returns
business_logic: |
  IF transaction_size <= 250000 OR policy_type == "Matrix"
  THEN financial_statements_required = False
       tax_returns_required = False
  ELSE
  THEN financial_statements_required = True (2 years, <=18 months old)
       tax_returns_required = True
keywords:
  - financial statements
  - tax returns
  - documentation threshold
  - small ticket
synonyms:
  financial statements:
    - profit and loss statement
    - balance sheet
    - P&L
intent_examples:
  - "Do I need financial statements for a $200,000 deal?"
  - "What is the documentation cut-off for requiring tax returns?"
  - "Is a small equipment purchase exempt from financials?"
decision: Not Required — financial statements/tax returns waived at or below $250k (or under Matrix policy)
related_policy:
  - CFAL Documentation Checklist
  - EX018 (Matrix Policy Reduced Documentation)
```

---

```yaml
exception_id: EX020
title: Escalated Documentation Requirements for Large Transactions (>$500k, CFAL)
source_document: Capital Finance Australia Limited (CFAL) — Minimum Documentation Checklist
policy_statement: >
  Transactions above $500,000 require additional items not needed at
  lower tiers: Details of Succession Planning, List of Major Competitors
  & Major Clients, Last 3 Years Financial Statements, Interim/Management
  Accounts (if year-end financials are >6 months old), Commentary on
  Major Movements (>=10%), Cash Flow Projections, and Current Aged
  Debtor & Creditor Listing.
interpretation: >
  Above the $500k threshold, CFAL escalates due-diligence requirements
  beyond the standard 2-year financials package to include forward-
  looking (cash flow projections), governance (succession planning), and
  market-position (competitors/clients) information.
business_rationale: >
  Larger exposures warrant a deeper credit assessment, including
  business continuity risk (succession), competitive positioning, and
  liquidity/working-capital visibility, to properly evaluate repayment
  capacity at scale.
examples:
  eligible:
    - $700,000 transaction — full escalated document set required
      (3-year financials, succession plan, cash flow projections, aged
      debtor listing, etc.)
  ineligible:
    - $300,000 transaction — does not trigger these escalated
      requirements (falls in the >$250k-$500k tier instead)
business_logic: |
  IF transaction_size > 500000
  THEN require({
    "3-year financial statements",
    "succession planning details",
    "major competitors & clients list",
    "interim/management accounts (if FS > 6 months old)",
    "commentary on movements >= 10%",
    "cash flow projections",
    "aged debtor & creditor listing"
  })
keywords:
  - succession planning
  - cash flow projections
  - aged debtor listing
  - large transaction documentation
synonyms:
  succession planning:
    - business continuity plan
    - ownership transition plan
  cash flow projections:
    - cash flow forecast
intent_examples:
  - "What extra documents are needed for a $700,000 deal?"
  - "Do I need to provide cash flow projections for large transactions?"
  - "Is succession planning required for a $400,000 loan?"
decision: Required — full escalated document set applies above $500,000
related_policy:
  - CFAL Documentation Checklist
  - EX016 (Rates by Negotiation Above $150,000)
```

---

```yaml
exception_id: EX021
title: PremiumPLUS 25bps Rate Discount (Resimac)
source_document: Resimac Asset Finance — Commercial Product Guide, 27 March 2026
policy_statement: >
  "25bps discount for PremiumPLUS."
interpretation: >
  Customers who qualify for the PremiumPLUS tier (the strictest customer
  tier: ABN registration >6 years, GST registration >3 years, property-
  backed only) receive a flat 25 basis point (0.25%) rate discount
  compared to the Premium/Standard/Basic rate on every asset category.
business_rationale: >
  Rewards the lowest-risk, longest-established, fully property-backed
  customer segment with preferential pricing to reflect their lower
  default probability.
examples:
  eligible:
    - Business with ABN registered 8 years, GST registered 5 years,
      property-backed guarantor -> qualifies for PremiumPLUS pricing
      (e.g. Motor vehicles <3yrs: 7.64% instead of 7.89%)
  ineligible:
    - Business with ABN registered 3 years (does not meet the >6 year
      PremiumPLUS duration requirement) -> falls to Premium/Standard/
      Basic tier instead, no 25bps discount
business_logic: |
  IF customer_tier == "PremiumPLUS"
  THEN applicable_rate = standard_tier_rate - 0.25%
keywords:
  - PremiumPLUS
  - rate discount
  - customer tier
synonyms:
  PremiumPLUS:
    - top tier
    - premium plus tier
intent_examples:
  - "What rate discount applies to PremiumPLUS customers?"
  - "Do I qualify for PremiumPLUS pricing with a 3-year-old ABN?"
decision: Conditional — 25bps discount applies only if customer tier == PremiumPLUS
related_policy:
  - Customer Tiers Table
  - Interest Rates Table
```

---

```yaml
exception_id: EX022
title: Risk Loading of 2% (Private Sales, Classic Cars, Assets ≥16yrs EOT, Prime Movers)
source_document: Resimac Asset Finance — Commercial Product Guide, 27 March 2026
policy_statement: >
  "Risk loading of 2% applies to: private sales, classic cars, assets age
  ≥16 yrs EOT, and prime movers. Multiple loadings may apply with a
  maximum per deal capped at 4%. Excludes brokerage loading."
interpretation: >
  Four specific risk factors each trigger a 2% rate loading on top of the
  standard published rate. If a deal has more than one risk factor
  (e.g. a private sale of a classic car), the loadings can stack, but the
  total loading on any single deal is capped at 4% — and this cap does
  not include any separate brokerage loading.
business_rationale: >
  These four categories represent elevated risk profiles (unverified
  private-seller provenance, volatile classic car valuations, high asset
  age at end of term, and prime movers' higher usage intensity/wear), so
  pricing is adjusted upward to compensate, while the 4% cap prevents
  loadings from compounding into an unreasonable rate.
examples:
  eligible:
    - Private sale of a standard (non-classic) 2-year-old vehicle -> +2%
      loading only
    - Private sale of a classic car -> two loadings apply (private sale +
      classic car) but capped at +4% total, not +4%+ stacked further
  ineligible:
    - Dealer-sourced, non-classic, <16yr EOT, non-prime-mover asset ->
      no risk loading applies
business_logic: |
  loading = 0
  IF transaction_type == "private_sale": loading += 2%
  IF asset_type == "classic_car": loading += 2%
  IF asset_age_at_EOT >= 16: loading += 2%
  IF asset_type == "prime_mover": loading += 2%
  applicable_loading = MIN(loading, 4%)   # excludes brokerage loading
keywords:
  - risk loading
  - private sale
  - classic car
  - prime mover
  - end of term
synonyms:
  risk loading:
    - rate loading
    - risk margin
  EOT:
    - end of term
    - asset age at term
intent_examples:
  - "Does a private sale of a classic car get double the loading?"
  - "What is the maximum risk loading that can apply to one deal?"
  - "Is there a loading for prime movers?"
decision: Conditional — +2% per triggered factor, capped at 4% total (excl. brokerage)
related_policy:
  - Interest Rates Table
  - EX026 (Prime Movers Always Require Property-Backed Guarantor)
```

---

```yaml
exception_id: EX023
title: Spouse-Owned Property Deposit Waiver (Resimac)
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "Spouse-owned property: Does not constitute property backing, but can
  be used to waive a deposit requirement. Must be married (not de
  facto)."
interpretation: >
  Property owned by a borrower's spouse cannot be used to classify the
  borrower as "property-backed" for tier purposes, but it can still be
  used specifically to waive a deposit requirement — and only applies to
  legally married couples, not de facto relationships.
business_rationale: >
  Legal marriage carries clearer property/asset rights and legal
  recourse than a de facto relationship, so Resimac allows a narrower
  benefit (deposit waiver only, not full property-backed status) based
  on the marriage certificate rather than cohabitation status.
examples:
  eligible:
    - Legally married applicant, spouse owns residential property ->
      deposit requirement waived, but applicant is still assessed as
      Standard/Basic tier (non property-backed) for other purposes
  ineligible:
    - De facto partner owns residential property -> cannot be used to
      waive deposit and does not count as property backing
    - Spouse's property used to try to qualify applicant as
      "property-backed" tier -> not permitted (only deposit waiver
      applies, not tier upgrade)
business_logic: |
  IF relationship_status == "married" (not de facto)
     AND spouse_owns_residential_property
  THEN waive_deposit_requirement
       # does NOT change property-backed tier classification
keywords:
  - spouse-owned property
  - deposit waiver
  - married
  - de facto
synonyms:
  spouse-owned property:
    - spousal property
    - partner's property
intent_examples:
  - "Can my spouse's house waive my deposit requirement?"
  - "Does a de facto partner's property count the same as a spouse's?"
  - "Does spouse property make me property-backed?"
decision: Conditional — Deposit waiver only, married couples only; does not confer property-backed status
related_policy:
  - Customer Tiers — Property Backing Definitions
  - EX028 (Non Property-Backed Deposit Differential)
```

---

```yaml
exception_id: EX024
title: Sale and Buyback Restricted to Dealership, 30-Day Window, PremiumPLUS/Premium Only
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "Sale and buyback can only be considered on Dealership sales, where the
  asset was purchased within the last 30-days of receiving the
  application. Sale and buybacks can only be considered for PremiumPLUS
  or Premium applications, on a case-by-case basis."
interpretation: >
  Sale and buyback transactions face three simultaneous restrictions:
  (1) the original purchase must have been from a dealership, not a
  private seller; (2) the purchase must have occurred within 30 days of
  the finance application; and (3) only PremiumPLUS or Premium tier
  applicants are eligible, assessed case-by-case (not automatic).
business_rationale: >
  Combining all three restrictions minimises the risk of cash-out
  schemes or inflated asset valuations, while reserving this higher-risk
  product structure for the bank's most creditworthy, longest-
  established customer tiers.
examples:
  eligible:
    - PremiumPLUS applicant purchased equipment from a dealership 10 days
      ago, now applies for sale and buyback -> may be considered
      case-by-case
  ineligible:
    - Standard tier applicant applying for sale and buyback (tier not
      eligible regardless of purchase timing/source)
    - PremiumPLUS applicant whose asset was purchased 45 days ago
      (exceeds 30-day window)
    - PremiumPLUS applicant whose asset was purchased privately, not
      from a dealership
business_logic: |
  IF customer_tier IN {PremiumPLUS, Premium}
     AND purchase_source == "dealership"
     AND (application_date - purchase_date) <= 30 days
  THEN eligible_for_case_by_case_review
  ELSE reject_sale_and_buyback_request
keywords:
  - sale and buyback
  - dealership sale
  - 30-day window
synonyms:
  sale and buyback:
    - sale and hireback
    - cash-out finance
intent_examples:
  - "Can a Basic tier customer apply for sale and buyback?"
  - "Is a private-sale asset eligible for sale and buyback?"
  - "How recent must the purchase be for sale and buyback?"
decision: Conditional — Eligible only for PremiumPLUS/Premium, dealership purchase, within 30 days, case-by-case
related_policy:
  - EX013 (Medical Sale & Hireback 30-Day Window Exception — Westpac, for comparison)
  - Customer Tiers Table
```

---

```yaml
exception_id: EX025
title: Low Doc Aggregate Exposure Cap of $400k for Existing Perfect-Repayment Clients
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "Low Doc aggregate exposure for any existing property backed client
  with 12 months perfect repayment history on a Resimac Asset Finance
  contract is $400k."
interpretation: >
  An existing, property-backed Resimac customer with a clean 12-month
  repayment record on a prior contract can access up to $400,000 in
  total Low Doc exposure — this is a specific carve-out for repeat
  customers rather than the general Low Doc limits shown in the loan
  amount table.
business_rationale: >
  A demonstrated clean repayment history is a strong positive credit
  signal, allowing Resimac to extend Low Doc (reduced documentation)
  treatment further than it would for a new customer with no track
  record.
examples:
  eligible:
    - Existing property-backed client, 14 months of on-time repayments
      on a current Resimac contract, applying for a further $350,000 Low
      Doc facility -> within the $400k aggregate cap
  ineligible:
    - New client with no prior Resimac contract applying for $350,000 Low
      Doc -> does not qualify for this exception; standard Low Doc limits
      by tier apply instead
    - Existing client with a missed repayment in the last 12 months ->
      "perfect repayment history" condition not met
business_logic: |
  IF client_status == "existing" AND property_backed == True
     AND repayment_history_months >= 12 AND missed_repayments == 0
  THEN low_doc_aggregate_exposure_limit = $400,000
  ELSE apply_standard_low_doc_limits_by_tier
keywords:
  - Low Doc
  - aggregate exposure
  - repayment history
synonyms:
  Low Doc:
    - low documentation
    - reduced documentation
intent_examples:
  - "What is the Low Doc limit for an existing customer with a good track record?"
  - "Does perfect repayment history increase my Low Doc exposure limit?"
decision: Conditional — $400k aggregate cap, only for existing property-backed clients with 12mo clean history
related_policy:
  - Maximum Loan Amounts Table
  - Application Requirements (Low/Lite/Full Doc)
```

---

```yaml
exception_id: EX026
title: Prime Movers Always Require a Property-Backed Guarantor
source_document: Resimac Asset Finance — Commercial Product Guide, Definitions
policy_statement: >
  "Prime movers: Always requires a property-backed guarantor."
interpretation: >
  Regardless of the applicant's customer tier or documentation level,
  financing a prime mover (truck tractor/road train head unit) always
  requires a property-backed guarantor — this overrides the tier-based
  flexibility (e.g. Basic tier normally allows renter/LWP applicants
  without property backing).
business_rationale: >
  Prime movers are high-value, high-usage-intensity assets with
  significant depreciation and operational risk; the bank mitigates this
  by mandating the strongest form of security (property-backed
  guarantee) irrespective of the deal's other characteristics.
examples:
  eligible:
    - Basic tier applicant financing a prime mover, but provides a
      property-backed guarantor -> requirement satisfied
  ineligible:
    - Basic tier applicant financing a prime mover using only a renter/
      LWP guarantor (normally acceptable for Basic tier) -> not
      acceptable for prime movers specifically; property-backed
      guarantor mandatory
business_logic: |
  IF asset_type == "Prime Mover"
  THEN require(guarantor_type == "property_backed")  # overrides tier default
keywords:
  - prime mover
  - guarantor
  - property-backed
synonyms:
  prime mover:
    - truck tractor
    - road train head unit
intent_examples:
  - "Can a Basic tier applicant finance a prime mover without property backing?"
  - "Is a property-backed guarantor mandatory for prime movers?"
decision: Required — Property-backed guarantor mandatory for all prime mover deals
related_policy:
  - EX022 (Risk Loading — Prime Movers)
  - Customer Tiers — Property Backing Definitions
```

---

```yaml
exception_id: EX027
title: Maximum NAF Per Asset — Motorbike $75k / Passenger Vehicle $250k
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "Maximum NAF per motorbike $75k. Maximum NAF per passenger vehicle
  $250k."
interpretation: >
  Independent of the customer tier and documentation-level loan amount
  tables, two specific asset types have hard per-asset Net Amount
  Financed (NAF) caps: motorbikes cannot exceed $75,000 and passenger
  vehicles cannot exceed $250,000, even if the customer's tier would
  otherwise permit a higher amount.
business_rationale: >
  Caps the bank's exposure to asset categories with faster depreciation
  curves or narrower resale markets (very high-end motorbikes or luxury
  passenger cars), independent of the customer's overall creditworthiness
  tier.
examples:
  eligible:
    - PremiumPLUS Full Doc customer (tier limit up to $450k) financing a
      $220,000 passenger vehicle -> within the $250k passenger vehicle
      cap
  ineligible:
    - Same customer financing a $300,000 passenger vehicle -> exceeds the
      $250k per-asset cap even though the tier's general limit ($450k)
      would otherwise allow it
    - $90,000 motorbike -> exceeds the $75k motorbike cap
business_logic: |
  IF asset_type == "motorbike"
  THEN max_NAF = MIN(tier_loan_amount_limit, $75,000)
  ELSE IF asset_type == "passenger_vehicle"
  THEN max_NAF = MIN(tier_loan_amount_limit, $250,000)
keywords:
  - NAF
  - motorbike
  - passenger vehicle
  - per-asset cap
synonyms:
  NAF:
    - Net Amount Financed
intent_examples:
  - "What is the maximum loan amount for a motorbike?"
  - "Can I finance a $300,000 passenger vehicle under PremiumPLUS?"
decision: Not Eligible above the per-asset cap, regardless of tier limits
related_policy:
  - Maximum Loan Amounts Table
  - Asset Categories — Motor Vehicles
```

---

```yaml
exception_id: EX028
title: Non Property-Backed Deposit Differential (10% Motor Vehicles vs 20% All Other)
source_document: Resimac Asset Finance — Commercial Product Guide, Customer Tiers
policy_statement: >
  "Non property-backed deposits: 10% Motor vehicles | 20% All other."
interpretation: >
  For applicants who are not property-backed, the required deposit
  differs by asset type — motor vehicles require only a 10% deposit,
  while every other asset category (Primary/Secondary/Tertiary) requires
  a 20% deposit.
business_rationale: >
  Motor vehicles have deeper, more liquid resale markets and more
  standardised valuations than industrial/specialised equipment, so the
  bank accepts a lower deposit buffer for them when the applicant lacks
  property backing.
examples:
  eligible:
    - Non property-backed applicant financing a passenger vehicle -> 10%
      deposit required
  ineligible (higher deposit required, not "ineligible"):
    - Non property-backed applicant financing a Secondary asset (e.g.
      generator) -> 20% deposit required, not 10%
business_logic: |
  IF property_backed == False:
    IF asset_type == "Motor Vehicle": deposit_required = 10%
    ELSE: deposit_required = 20%
  ELSE: deposit_required = standard_or_nil (per tier policy)
keywords:
  - deposit
  - non property-backed
  - motor vehicles
synonyms:
  deposit:
    - down payment
intent_examples:
  - "What deposit is required if I don't own property?"
  - "Is the deposit the same for a truck as for a car?"
decision: Conditional — 10% for motor vehicles, 20% for all other assets, non property-backed applicants only
related_policy:
  - Customer Tiers Table
  - EX023 (Spouse-Owned Property Deposit Waiver)
```

---

```yaml
exception_id: EX029
title: Lite Doc ATO Debt and Turnover Thresholds
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "Lite Doc: Any ATO Debt must be <10% of turnover and be under an
  established payment arrangement (in place >3 months). BAS requires
  annualised minimum turnover >2.5 x asset purchase price."
interpretation: >
  To qualify for Lite Doc treatment, an applicant with existing ATO
  (Australian Taxation Office) debt must keep that debt under 10% of
  turnover and have had a payment arrangement in place for more than 3
  months; separately, the applicant's annualised turnover (from BAS
  lodgements) must be more than 2.5 times the asset purchase price.
business_rationale: >
  These thresholds screen out businesses under material tax-debt stress
  or businesses whose revenue base is too small relative to the asset
  being financed, ensuring Lite Doc (reduced documentation) is only
  extended to financially stable applicants.
examples:
  eligible:
    - ATO debt = 6% of turnover, payment arrangement in place for 5
      months; annualised turnover $500,000 for a $150,000 asset purchase
      (turnover is 3.3x purchase price) -> Lite Doc eligible
  ineligible:
    - ATO debt = 15% of turnover -> exceeds 10% threshold, Lite Doc not
      available (may require Full Doc instead)
    - Annualised turnover $300,000 for a $150,000 asset (only 2x) -> below
      the 2.5x turnover requirement
business_logic: |
  IF (ato_debt / turnover) < 10%
     AND ato_payment_arrangement_duration_months > 3
     AND (annualised_turnover / asset_purchase_price) > 2.5
  THEN lite_doc_eligible = True
  ELSE lite_doc_eligible = False  # may require Full Doc
keywords:
  - Lite Doc
  - ATO debt
  - turnover
  - BAS
synonyms:
  ATO debt:
    - tax debt
    - Australian Taxation Office debt
intent_examples:
  - "What ATO debt level disqualifies me from Lite Doc?"
  - "How much turnover do I need relative to the asset price for Lite Doc?"
decision: Conditional — Both thresholds must be met simultaneously for Lite Doc eligibility
related_policy:
  - Application Requirements (Low/Lite/Full Doc)
  - Definitions — Cash Flow Lenders
```

---

```yaml
exception_id: EX030
title: Director/Shareholder Guarantee Waiver for Large Corporate, Clubs, Schools, Charities
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "May not be required to guarantee for large corporate, clubs, private
  schools, charities and associations."
interpretation: >
  The general rule requires all directors and all >40% shareholders to
  personally guarantee the loan. However, applicants that are large
  corporates, clubs, private schools, charities, or associations may be
  exempted from this personal guarantee requirement.
business_rationale: >
  These entity types typically have institutional governance, ongoing
  operations independent of any single individual, and/or public-benefit
  status, making personal guarantees from directors less necessary (and
  sometimes impractical to obtain) compared with small owner-operated
  businesses.
examples:
  eligible:
    - Private school applying for equipment finance -> may proceed
      without individual director guarantees, at Resimac's discretion
  ineligible:
    - Small owner-operated pty ltd company (not large corporate/club/
      school/charity/association) -> standard rule applies; all
      directors and >40% shareholders must guarantee
business_logic: |
  IF entity_type IN {large_corporate, club, private_school, charity,
                      association}
  THEN director_guarantee_requirement = "may be waived"  # discretionary
  ELSE director_guarantee_requirement = "mandatory for all directors and >40% shareholders"
keywords:
  - director guarantee
  - shareholder guarantee
  - large corporate
  - charity
  - private school
synonyms:
  guarantee waiver:
    - guarantor exemption
intent_examples:
  - "Does a charity need director guarantees for equipment finance?"
  - "Are all shareholders required to guarantee for a private school?"
decision: Conditional — Guarantee may be waived for specified entity types, at Resimac's discretion
related_policy:
  - Key Point Guidelines — Directors and Shareholders
```

---

```yaml
exception_id: EX031
title: Green Goods Extended Loan Term (up to 84 Months)
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "Loan terms are available between 12 and 60 months or up to 84 months
  for Green Goods."
interpretation: >
  Standard loan terms are capped at 60 months. "Green Goods" (assets
  meeting Resimac's environmental/sustainability criteria) qualify for an
  extended maximum term of up to 84 months.
business_rationale: >
  Encourages financing of environmentally beneficial assets by offering
  more affordable monthly repayments through a longer amortisation
  period, consistent with sustainable finance incentives seen across the
  industry (compare EX001/EX015 EV discounts).
examples:
  eligible:
    - Solar/EV-related "Green Goods" asset financed over a 72-month term
      -> permitted (within the 84-month Green Goods maximum)
  ineligible:
    - Standard (non-Green Goods) asset requesting a 72-month term ->
      exceeds the standard 60-month cap; not permitted
business_logic: |
  IF asset_classification == "Green Goods"
  THEN max_loan_term_months = 84
  ELSE max_loan_term_months = 60
keywords:
  - Green Goods
  - loan term
  - sustainable finance
synonyms:
  Green Goods:
    - environmentally certified assets
    - sustainable assets
intent_examples:
  - "Can I get a longer loan term for eco-friendly equipment?"
  - "What is the maximum term for a Green Goods asset?"
decision: Conditional — 84-month maximum term only for Green Goods; 60 months otherwise
related_policy:
  - EX001 / EX015 (Electric Vehicle Rate Discounts)
```

---

```yaml
exception_id: EX032
title: Credit Reference Requirements Scale by NAF Threshold ($100k)
source_document: Resimac Asset Finance — Commercial Product Guide, Definitions
policy_statement: >
  "Credit references: <100k (must be available) — asset finance
  statements (loan running six months plus with no missed repayments) or
  mortgage statements (same, spouse's mortgage statement not accepted
  for sole traders excluded); >100k (must be available) — asset finance
  statements only, must be for 50% of requested NAF if Low Doc."
interpretation: >
  The required type and strength of credit references changes at the
  $100,000 NAF threshold. Below $100k, either asset finance or mortgage
  statements are acceptable (with conditions). Above $100k, only asset
  finance statements are accepted, and for Low Doc applications the
  reference must cover at least 50% of the requested NAF.
business_rationale: >
  Larger financing amounts warrant stronger, more comparable credit
  evidence (an existing asset finance track record is a closer proxy for
  repayment behaviour on a new asset facility than a mortgage), and the
  50%-of-NAF rule ensures the reference is proportionate to the new
  facility size for the least-documented (Low Doc) pathway.
examples:
  eligible:
    - $80,000 NAF request; applicant provides a 8-month mortgage
      statement with no missed payments (not sole trader) -> acceptable
    - $150,000 Low Doc NAF request; applicant's existing asset finance
      facility is $80,000 (>=50% of $150k) with 6+ months clean history
      -> acceptable
  ineligible:
    - $150,000 Low Doc NAF request; existing asset finance reference is
      only $40,000 (<50% of $150k) -> insufficient, does not meet the
      50%-of-NAF requirement
    - Sole trader submitting spouse's mortgage statement -> not accepted
business_logic: |
  IF requested_NAF < 100000:
    reference_required = "asset finance statement (6mo+, no misses)"
                          OR "mortgage statement (6mo+, no misses,
                              applicant/guarantor name, spouse's
                              statement not accepted for non-sole-traders)"
  ELSE:  # requested_NAF >= 100000
    reference_required = "asset finance statement only"
    IF doc_level == "Low Doc":
      reference_amount_must_be >= 0.5 * requested_NAF
keywords:
  - credit reference
  - asset finance statement
  - mortgage statement
synonyms:
  credit reference:
    - reference check
    - repayment history evidence
intent_examples:
  - "What credit reference is needed for a $60,000 Low Doc application?"
  - "Can I use a mortgage statement for a $200,000 asset finance request?"
  - "Does my existing facility need to cover 50% of the new NAF?"
decision: Conditional — Reference type and coverage requirement scale with NAF and doc level
related_policy:
  - Application Requirements (Low/Lite/Full Doc)
  - Definitions — Active Credit File
```

---

```yaml
exception_id: EX033
title: Cash Flow Lender Enquiries Trigger Lite Doc / Bank Sweep Requirement
source_document: Resimac Asset Finance — Commercial Product Guide, Definitions
policy_statement: >
  "Cash flow lenders: Any enquiries from cashflow lenders within the last
  6 months may require Lite Doc or bank sweep, subject to profile."
interpretation: >
  If a credit file shows enquiries from cash flow (short-term working
  capital) lenders within the past 6 months, the application may be
  escalated to require Lite Doc-level documentation or a bank account
  sweep review, even if it would otherwise have qualified for Low Doc.
business_rationale: >
  Recent cash flow lender enquiries can signal short-term liquidity
  stress, so Resimac uses this as a trigger for closer financial
  scrutiny before extending reduced-documentation credit.
examples:
  eligible (no escalation):
    - No cash flow lender enquiries in the credit file -> standard doc
      level requirement applies (e.g. Low Doc if otherwise qualified)
  ineligible (escalation triggered):
    - Two cash flow lender enquiries in the last 4 months -> may be
      escalated to Lite Doc or require a bank statement sweep review,
      regardless of the applicant's otherwise-qualifying profile
business_logic: |
  IF cash_flow_lender_enquiries_last_6_months > 0
  THEN may_require(doc_level >= "Lite Doc" OR bank_sweep_review = True)
       # subject to overall profile assessment
keywords:
  - cash flow lender
  - bank sweep
  - credit enquiry
synonyms:
  cash flow lender:
    - short-term lender
    - working capital lender
intent_examples:
  - "Does a cash flow loan enquiry affect my Low Doc eligibility?"
  - "What is a bank sweep review and when is it required?"
decision: Conditional — May escalate documentation requirement; subject to broader profile review
related_policy:
  - Application Requirements (Low/Lite/Full Doc)
  - Definitions — Active Credit File
```

---

```yaml
exception_id: EX034
title: Excluded Asset Categories (Resimac)
source_document: Resimac Asset Finance — Commercial Product Guide, Asset Categories
policy_statement: >
  "Excludes: Fixtures and fittings; Cool rooms and spray booths;
  Intangible assets; Refrigeration; Gym equipment; Hospitality equipment;
  Software; Scaffolding, racking and temporary fencing; Food trucks;
  Artwork; Vending and gaming machines; Livestock; Ride share, taxis and
  repairable writeoffs; Demountables and shipping containers; Racking;
  Office furniture; Electric or motor vehicle used for hire/rental
  purposes; IT hardware."
interpretation: >
  This is a comprehensive negative list — none of these asset types can
  be financed under this Resimac product at all, regardless of customer
  tier, documentation level, or deposit offered. This is broader than
  Westpac's "Computers, Fixtures & Fittings" exclusion (EX006) and
  includes several categories Westpac does not explicitly exclude (e.g.
  livestock, artwork, gaming machines, ride-share vehicles).
business_rationale: >
  These categories share common risk traits: illiquid/non-standardised
  resale markets, intangible or hard-to-repossess nature, regulatory
  complexity (gaming, livestock), or high fraud/valuation risk (artwork,
  repairable writeoffs) — making them unsuitable for this asset finance
  product regardless of the applicant's creditworthiness.
examples:
  eligible:
    - Excavator (falls under Primary assets, not on the exclusion list)
  ineligible:
    - Office furniture, IT hardware, gym equipment, artwork, food trucks,
      livestock, gaming machines, or any other item on the exclusion list
      -> not financeable under this product, regardless of applicant tier
business_logic: |
  IF asset_type IN excluded_asset_list
  THEN application_not_eligible  # no tier, doc-level, or deposit can override this
keywords:
  - excluded assets
  - fixtures and fittings
  - IT hardware
  - office furniture
  - livestock
  - artwork
  - gaming machines
synonyms:
  excluded assets:
    - ineligible assets
    - non-financeable categories
intent_examples:
  - "Can I finance office furniture through Resimac?"
  - "Is IT hardware eligible for asset finance?"
  - "Can gym equipment or gaming machines be financed?"
  - "Is a food truck eligible?"
decision: Not Eligible — hard exclusion, no exceptions regardless of tier or documentation
related_policy:
  - EX006 (Computers, Fixtures & Fittings Excluded — Westpac, for comparison)
  - Asset Categories — Motor/Primary/Secondary/Tertiary
```

---

```yaml
exception_id: EX035
title: Certificate of Currency (CoC) Insurance Proof Required Only Above $100k NAF
source_document: Resimac Asset Finance — Commercial Product Guide, Key Point Guidelines
policy_statement: >
  "Insurance is required on all deals (with Certificate of Currency proof
  required on NAF amounts >$100k)."
interpretation: >
  Insurance itself is mandatory on every deal, but documentary proof via
  a Certificate of Currency (CoC) is only required to be provided when
  the Net Amount Financed exceeds $100,000. Below that threshold,
  insurance is still required but CoC proof is not enforced as a
  document.
business_rationale: >
  Balances administrative efficiency for smaller transactions against
  the need for verified insurance evidence on larger, higher-exposure
  deals.
examples:
  eligible:
    - $70,000 NAF deal — insurance required, but no CoC document needed
      to be submitted
  ineligible:
    - $150,000 NAF deal without a CoC provided -> incomplete application;
      CoC proof is mandatory above $100k
business_logic: |
  insurance_required = True  # always, on every deal
  IF NAF > 100000
  THEN coc_proof_required = True
  ELSE coc_proof_required = False
keywords:
  - Certificate of Currency
  - CoC
  - insurance
synonyms:
  CoC:
    - Certificate of Currency
    - insurance proof
intent_examples:
  - "Do I need to provide a Certificate of Currency for a $60,000 deal?"
  - "Is insurance required even if CoC proof isn't needed?"
decision: Conditional — CoC document required only when NAF > $100,000; insurance itself always required
related_policy:
  - EX011 (Fleet Policy CoC Asset Detail Waiver — Westpac, for comparison)
```

---

```yaml
exception_id: EX036
title: Brokerage Escalation Above 5.5% (Capped at 8.8%)
source_document: Resimac Asset Finance — Commercial Product Guide, Application Requirements
policy_statement: >
  "Rates applicable up to 5.5%. Any increase above 5.5% inc GST will
  incur equivalent of 0.5% for every 1% increase in brokerage (or part
  thereof). Maximum brokerage 8.8%."
interpretation: >
  Standard brokerage up to 5.5% (incl. GST) does not affect the
  customer's rate. Brokerage above 5.5% triggers a rate loading: for
  every additional 1% of brokerage (or part thereof), the customer's
  interest rate increases by 0.5%, up to a maximum brokerage of 8.8%.
business_rationale: >
  Higher broker commissions increase the total cost of the deal; passing
  a proportional rate increase back to the customer keeps the economics
  transparent and discourages excessive brokerage loading beyond the
  standard range.
examples:
  eligible:
    - Broker charges 5.5% brokerage -> no additional rate loading
    - Broker charges 7% brokerage (1.5% above 5.5%, rounds up to 2 full
      percentage points of "part thereof") -> +1.0% rate loading applied
  ineligible:
    - Broker requests 9% brokerage -> exceeds the 8.8% maximum; not
      permitted
business_logic: |
  IF brokerage_pct <= 5.5%:
    rate_loading_from_brokerage = 0
  ELSE IF brokerage_pct <= 8.8%:
    excess = CEILING(brokerage_pct - 5.5%)  # rounded up per 1% or part thereof
    rate_loading_from_brokerage = excess * 0.5%
  ELSE:
    brokerage_not_permitted  # exceeds 8.8% cap
keywords:
  - brokerage
  - rate loading
  - commission
synonyms:
  brokerage:
    - broker commission
    - introducer commission
intent_examples:
  - "What happens to my rate if brokerage is set above 5.5%?"
  - "What is the maximum brokerage percentage allowed?"
decision: Conditional — Rate loading applies above 5.5% brokerage, hard cap at 8.8%
related_policy:
  - Fees — Application Requirements
  - EX022 (Risk Loading — excludes brokerage loading)
```

---

```yaml
exception_id: EX037
title: Introducer Documentation Fee Variance (Private Sale / Buyback Reduced Fee)
source_document: Resimac Asset Finance — Commercial Product Guide, Application Requirements
policy_statement: >
  "Introducer documentation fee up to $990 (if private sale / sale and
  buyback $880)."
interpretation: >
  The standard introducer documentation fee cap is $990. For private
  sale or sale-and-buyback transactions specifically, the cap is lower,
  at $880.
business_rationale: >
  Likely reflects a difference in the documentation/verification effort
  or a deliberate pricing distinction to avoid stacking excessive fees on
  already higher-risk private sale/buyback transaction types (which also
  attract the 2% risk loading under EX022).
examples:
  eligible:
    - Standard dealer-sourced transaction — introducer documentation fee
      up to $990
  ineligible (i.e., the lower cap applies instead):
    - Private sale transaction charged a $990 introducer documentation
      fee -> exceeds the $880 cap applicable to private sale/buyback
      deals
business_logic: |
  IF transaction_type IN {private_sale, sale_and_buyback}
  THEN max_introducer_documentation_fee = $880
  ELSE max_introducer_documentation_fee = $990
keywords:
  - introducer documentation fee
  - private sale fee
  - sale and buyback fee
synonyms:
  introducer documentation fee:
    - broker documentation fee
intent_examples:
  - "What is the documentation fee cap for a private sale deal?"
  - "Is the introducer fee different for sale and buyback transactions?"
decision: Conditional — $880 cap for private sale/buyback; $990 cap for all other deals
related_policy:
  - Fees — Application Requirements
  - EX024 (Sale and Buyback Restrictions)
```

---

```yaml
exception_id: EX038
title: Equifax Score Referral/Decline Threshold (<450)
source_document: Resimac Asset Finance — Commercial Product Guide, Definitions
policy_statement: >
  "Equifax scores — Assessment score: using highest of company or any
  guarantor score. Lower limit: any company or guarantor score <450 can
  lead to deal being referred or declined."
interpretation: >
  The assessment score used for a deal is the highest score among the
  company and all guarantors (i.e. the best available score is used for
  the primary assessment). However, if any single company or guarantor
  score falls below 450, that alone can trigger a referral or decline —
  even if the "best" score used for assessment is otherwise strong.
business_rationale: >
  Using the highest score allows a strong guarantor to support a weaker
  company profile, but the 450 floor acts as an absolute backstop so
  that no individual party in the deal can have an extremely poor credit
  history hidden behind a stronger co-applicant's score.
examples:
  eligible:
    - Company score 520, guarantor score 680 -> assessment uses 680
      (highest); no party is below 450, so no automatic referral
  ineligible:
    - Company score 520, guarantor score 400 -> assessment would use 520
      (highest), BUT the guarantor's 400 score is below the 450 floor,
      triggering referral or decline despite the higher company score
business_logic: |
  assessment_score = MAX(company_score, guarantor_scores...)
  IF MIN(company_score, guarantor_scores...) < 450
  THEN deal_status = "referred_or_declined"  # overrides the assessment score result
keywords:
  - Equifax score
  - credit score
  - referral
  - decline
synonyms:
  Equifax score:
    - credit bureau score
    - credit score
intent_examples:
  - "Does a low guarantor score affect the deal if the company score is high?"
  - "What credit score triggers an automatic referral or decline?"
decision: Conditional — Any single score <450 triggers referral/decline, regardless of assessment score
related_policy:
  - Definitions — Active Credit File
  - Customer Tiers — Scores Table
```

---

## Non-Exception Baseline Criteria (for cross-reference only)

The following are **standard eligibility criteria**, not exceptions — included here only to prevent confusion with the entries above:

- Business trading >2 years, valid ABN, currently GST registered
- Statutory lodgements (tax/GST/employee entitlements) up to date, no payment arrangements in place
- All directors must guarantee the loan and pass satisfactory credit bureau checks
- Signed Affordability Declaration required from borrower(s)
- Where financial data cannot be obtained, verbal confirmation is an accepted substitute

**Resimac Asset Finance baseline criteria** (not exceptions, included for reference):
- Asset must be used by the business as part of its normal trading activities
- All assets must be serialised, identifiable and registered prior to settlement (where applicable)
- No current bankrupts or discharged bankrupts within the last 10 years
- Applicants must have an active credit file with regular industry-related enquiries
- All Directors and all >40% shareholders must be Australian Citizens or Permanent Residents residing in Australia and act as guarantor (subject to EX030 waiver)
- All shareholders >25% must complete Resimac Asset Finance AML procedures

---

*Compiled from user-supplied screenshots and PDF documents (Westpac, Capital Finance Australia Limited, and Resimac Asset Finance). Verify exact figures against each provider's live platform/current policy documents before operational use. This file is intended for internal knowledge-base / RAG ingestion purposes only.*
