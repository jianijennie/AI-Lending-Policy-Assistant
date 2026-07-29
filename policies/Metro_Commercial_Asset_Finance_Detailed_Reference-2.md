# Metro Commercial Asset Finance — Detailed Policy Reference & Glossary

> Source: Metro Commercial Asset Finance rate card (20/07/2026) and MetroEco / Streamlined Product brochures
> (Passenger Vehicle, Trucks/Trailers/Wheeled Equipment, Other Equipment, Agri, Replacement Policy,
> Balloon/Residual Refinance, MetroEco Solar/Batteries/Chargers, MetroEco Electric Trucks, MetroEco Electric
> Vehicles & Chargers).
> Purpose: A standalone deep-dive reference (parallel to the Resimac reference) covering rate loading mechanics,
> asset category definitions, the shared "Streamlined Product" framework, fees, and full inclusion/exclusion lists,
> structured for RAG retrieval. Section 10 lists all Metro-specific exception clauses separately, using the same
> `exception_id` / `keywords` / `synonyms` / `intent_examples` / `decision` / `related_policy` schema as the
> multi-lender Exceptions Catalog (Westpac / CFAL / Resimac), numbered EX039 onward to allow future merging.

---

## 1. Product Suite Overview

Metro's commercial asset finance offering has three layers:

| Layer | Products | Purpose |
|---|---|---|
| **Core rate card** | Commercial Asset Finance (main rate card) | Standard tiered pricing by asset type/GVM/amount, with rate loadings for risk factors |
| **Streamlined Products** | Passenger Vehicle, Trucks/Trailers/Wheeled Equipment, Other Equipment, Agri, Replacement Policy, Balloon/Residual Refinance | Pre-approved, fast-track policies with fixed loan-size/exposure matrices by property ownership tier |
| **MetroEco** | Electric Vehicles & Chargers, Electric Trucks, Solar/Batteries/Chargers | Green-asset finance with dedicated discounts, terms, and eligibility rules |

---

## 2. The Shared "Streamlined Product" Framework

Five of the six Streamlined Products (Passenger Vehicle, Trucks/Trailers/Wheeled Equipment, Replacement Policy,
Balloon/Residual Refinance, Agri) use the **same table structure**. Understanding this shared structure once
avoids re-explaining it for every product.

```yaml
term: Streamlined Product Framework — Property Ownership Tiers
definition: >
  Every Streamlined Product scales the maximum loan size and maximum
  Metro exposure by WHO owns the property backing the deal, not by the
  applicant's business profile alone.
tiers:
  - name: "In the borrower or guarantor's name"
    meaning: >
      The applicant or their guarantor directly owns qualifying real
      property. This is the strongest tier, unlocking the highest loan
      sizes and exposure limits, which further scale up based on repayment
      history with Metro (12 months -> higher tier, 24 months -> highest
      tier).
  - name: "In spouse's name"
    meaning: >
      Property is owned by the applicant's spouse, not the applicant/
      guarantor directly. This unlocks a fixed, lower loan size/exposure
      (typically $150,000 flat) regardless of repayment history — it does
      not scale up with a good repayment track record the way borrower-
      owned property does.
  - name: "Non-property backed"
    meaning: >
      No qualifying property backing at all. This is the most restricted
      tier: lowest loan size (typically $100,000–$150,000), dealer sale
      only (private sale excluded in most products), and — for motor
      vehicles specifically — a mandatory 30% deposit.
trigger_keywords:
  - property ownership
  - property backed
  - spouse's name
  - non-property backed
rationale: >
  Property ownership is Metro's primary security signal across all
  Streamlined Products. Direct borrower/guarantor ownership gives the
  strongest legal recourse; spousal ownership is weaker (similar
  reasoning to Resimac's spouse-property rule); no property at all is
  the weakest, hence the deposit requirement to compensate.
```

```yaml
term: Maximum Metro Exposure (Streamlined Products)
definition: >
  The total combined balance of ALL Metro facilities the customer holds
  (including the new deal), not just the size of the single new loan.
  This is separate from "Maximum Loan Size," which caps the individual
  transaction.
scaling_rule: >
  Exposure limits step up based on repayment history with Metro:
  - New customers: base exposure limit (typically $250,000–$300,000)
  - 12 months good repayment history: mid-tier exposure (typically $500,000)
  - 24 months good repayment history: top-tier exposure (typically $750,000)
trigger_keywords:
  - Metro exposure
  - aggregate exposure
  - repayment history
rationale: >
  Rewards proven, low-risk repeat customers with higher aggregate credit
  lines, similar in spirit to Resimac's Low Doc aggregate exposure
  carve-out (EX025 in the Resimac/Westpac Exceptions Catalog).
```

```yaml
term: Comparable Credit Reference
definition: >
  Evidence that the applicant has held a similar asset finance facility
  (or, in some products, a mortgage) with satisfactory conduct, generally
  running at least 12 months, checked within the last 12 months on a
  similar asset.
variants_by_product:
  - Most Streamlined Products: "current or previous asset finance,
    within the last 12 months on similar assets"
  - Passenger Vehicle (fallback): "12 months mortgage statements
    acceptable if no asset finance reference is available, for amounts
    up to $100,000"
  - Replacement Policy: reference must be on the SPECIFIC account being
    refinanced, AND that contract must have run for a minimum of 36 months
  - Balloon/Residual Refinance: reference must be on the account being
    refinanced (no minimum running period stated, but "no inspection
    required")
trigger_keywords:
  - comparable credit reference
  - asset finance reference
  - mortgage statement fallback
rationale: >
  Demonstrated repayment conduct on a similar facility is used as a
  proxy for future repayment behaviour, reducing the need for full
  financial statements under the streamlined (fast-track) pathway.
```

```yaml
term: Age of Asset at End of Term (EOT)
definition: >
  The asset's projected age when the loan matures (current age + loan
  term), NOT its age today — same forward-looking concept as Resimac's
  EOT rule.
typical_limits_by_product:
  - Passenger vehicles / light commercials: no older than 12 years at EOT
  - Trucks/Trailers/Wheeled Equipment, Agri, Other Equipment (general):
    no older than 15 years at EOT, with "no balloons or residuals for
    lends out to 15 years at end of term"
  - Other Equipment (Primary Equipment specifically): no older than 3
    years — much tighter than the general 15-year rule
trigger_keywords:
  - EOT
  - end of term
  - asset age at term
  - no balloon
rationale: >
  Same rationale as Resimac's EOT rule (Resimac reference, Section 1):
  the lender's exposure to residual/mechanical risk is highest near loan
  maturity, so the maximum permitted term is set by the asset's
  projected age at that point, not its age today. Where a deal is
  stretched out to the full 15-year EOT limit, Metro disallows balloon/
  residual payments entirely, since a confident residual value cannot be
  set that far out.
```

---

## 3. Risk / Rate Loading Trigger Definitions (Main Commercial Asset Finance Rate Card)

These loadings apply to the main Commercial Asset Finance rate card (Image 1), not the Streamlined Products
(which use fixed criteria instead of loadings).

```yaml
term: Private Sale Loading (Metro)
definition: >
  A 0.25% rate loading applied when the asset is purchased from a
  private seller rather than a licensed dealer.
trigger_keywords: [private sale, non-dealer purchase]
rationale: >
  Same underlying logic as other lenders in this catalog (see Resimac
  reference, Section 1.1) — private sales lack dealer warranty/
  accountability and are harder to verify, but Metro's loading (0.25%)
  is notably smaller than Resimac's equivalent (2%), reflecting a
  different risk appetite/pricing philosophy between the two lenders.
```

```yaml
term: Sale / Hire Back Loading (Metro)
definition: >
  A 0.75% rate loading applied to sale-and-hireback transactions (where
  the customer already owns the asset and sells it to Metro to lease/
  hire it back).
trigger_keywords: [sale and hireback, sale and leaseback]
rationale: >
  Sale and hireback carries elevated risk of cash-out schemes or
  inflated valuations (consistent with why other lenders restrict or
  exclude it entirely — see Westpac Exceptions Catalog EX013, Resimac
  reference EX024). Metro prices this risk in via a loading on the main
  rate card rather than an outright exclusion, but note: several
  Streamlined Products (Trucks/Trailers/Wheeled Equipment, Agri) state
  "no sale/hire back" as a flat exclusion — the loading applies only
  under the main rate card, not under those Streamlined pathways.
```

```yaml
term: Asset Age Loading — Start of Term (Metro)
definition: >
  A 0.25% rate loading applied when the asset is already older than 5
  years AT THE START of the loan term (i.e. based on current age, not
  projected EOT age).
trigger_keywords: [asset age, start of term, used asset loading]
rationale: >
  Complements the separate EOT-based loading below — this loading
  captures risk from the asset already being used/aged today,
  independent of how long the loan runs.
```

```yaml
term: Asset Age Loading — End of Term (Metro)
definition: >
  A 1.00% rate loading applied when the asset will be older than 10
  years AT THE END of the loan term (i.e. current age + loan term > 10).
  This is Metro's equivalent of the EOT concept, but on the main rate
  card it is expressed as a rate loading rather than a hard maximum-age
  cutoff (contrast with the Streamlined Products, which use hard EOT
  caps of 12/15/3 years instead of a loading).
trigger_keywords: [EOT, end of term, projected asset age, aged asset loading]
rationale: >
  Prices in the higher residual/mechanical risk of an asset that will be
  significantly aged by loan maturity, consistent with the EOT logic
  used across every lender in this catalog.
```

```yaml
term: Other Equipment Loading (Metro)
definition: >
  "Other equipment" (equipment outside the core Passenger/Commercial
  Vehicle and Heavy Commercial Vehicle & Trailers categories) is priced
  by adding 1% to the Wheeled Plant & Equipment base rate — it does not
  have its own independent base rate on the main card.
trigger_keywords: [other equipment, wheeled equipment rate, +1% loading]
rationale: >
  Rather than publish a fully separate rate table for every possible
  equipment type, Metro anchors "other equipment" pricing to the
  Wheeled Plant & Equipment rate plus a flat margin, reflecting
  similarly elevated (but not extreme) resale/valuation uncertainty.
```

```yaml
term: Vehicle Streamlined Non-Property Product Loading (Metro)
definition: >
  A flat 1% rate loading applied specifically to vehicle deals financed
  under the Streamlined pathway where the applicant is NOT property
  backed.
trigger_keywords: [non-property backed, streamlined loading, vehicle loading]
rationale: >
  Directly parallels the "Non property-backed deposit differential"
  concept seen at other lenders (Resimac reference EX028) — lacking
  property security increases risk, so Metro compensates with a rate
  loading (on top of the 30% deposit already required for non-property-
  backed motor vehicle deals under the Streamlined Products).
```

```yaml
term: Brokerage Escalation (Metro)
definition: >
  Advertised rates already assume brokerage up to 4%. Any brokerage
  above 4% triggers a rate loading of 0.5% for every additional 1% of
  brokerage.
trigger_keywords: [brokerage, broker commission, brokerage loading]
rationale: >
  Same purpose as Resimac's brokerage escalation (reference, Section
  3.3) and Westpac's equivalent (Exceptions Catalog EX036) — recovers
  the cost of above-standard broker commission via a proportional rate
  increase, and is calculated independently of (i.e. stacks on top of)
  the risk loadings above.
```

### 3.1 Worked Case Example — Combined Loadings (for retrieval)

```yaml
case_example_id: METRO-LOADING-001
scenario: >
  A customer wants to finance a Wheeled Plant & Equipment asset (a
  telehandler), purchased privately (not from a dealer), currently 7
  years old, over a 6-year (72-month) loan term, with brokerage set at
  6%.
step_1_identify_base_rate: >
  Wheeled Plant & Equipment falls under "Heavy Commercial Vehicles &
  Wheeled Plant & Equipment" -> base rate 8.45% (amount >$20K, 24-60
  month term).
step_2_identify_triggers:
  - Private sale -> +0.25%
  - Asset already 7 years old at start of term (>5 years) -> +0.25%
  - Projected age at EOT = 7 + 6 = 13 years, which is >10 -> +1.00%
  - (Not a sale/hireback, no "other equipment" loading since it IS
    Wheeled Plant & Equipment already, not "other")
step_3_sum_risk_loadings: 0.25% + 0.25% + 1.00% = 1.50%
  # Note: unlike Resimac's 4% cap on combined risk loadings, the Metro
  # rate card as shown does NOT state an explicit cap on these specific
  # loadings — they appear to be additive without a stated ceiling.
  # Always confirm with Metro BDMs for deals with multiple stacked
  # loadings, especially above $250,000 (which requires a BDM quote
  # regardless).
step_4_rate_before_brokerage: 8.45% + 1.50% = 9.95%
step_5_brokerage_loading: >
  Brokerage is 6%, which is 2% above the 4% threshold built into
  advertised rates -> 2 * 0.5% = 1.00% additional loading.
step_6_final_rate: 9.95% + 1.00% = 10.95% p.a.
key_takeaway: >
  Risk-factor loadings (private sale, asset age at start/end of term)
  and the brokerage loading are calculated as independent, additive
  components — consistent with the same "risk loading vs brokerage
  loading are separate mechanisms" principle documented for Resimac and
  Westpac, even though Metro does not publish an explicit 4% cap on the
  combined risk-factor loadings the way Resimac does.
```

---

## 4. Asset Category Definitions (Main Rate Card)

```yaml
term: Passenger & Commercial Vehicles (<12t GVM)
definition: >
  Standard road vehicles under 12 tonnes Gross Vehicle Mass, financeable
  for up to 5 years, and the basis of Metro's "8.20% Prime Rate"
  streamline product for dealer-sold vehicles under 5 years old.
trigger_keywords: [passenger vehicle, commercial vehicle, <12t GVM, prime rate]
base_rate: 8.20% (>$20K) / 9.00% (>$10K<$20K), for 24-60 month terms
```

```yaml
term: Heavy Commercial Vehicles (above 12t GVM) & Trailers / Wheeled Plant & Equipment
definition: >
  Vehicles above 12 tonnes GVM, trailers, and wheeled plant/equipment,
  priced on a single shared rate line (higher than the <12t GVM category).
trigger_keywords: [heavy commercial vehicle, >12t GVM, trailer, wheeled plant, wheeled equipment]
base_rate: 8.45% (>$20K) / 10.15% (>$10K<$20K), for 24-60 month terms
```

```yaml
term: Prime Movers (Metro — Exclusion from Trucks/Trailers/Wheeled Equipment Streamlined)
definition: >
  The Trucks, Trailers & Wheeled Equipment Streamlined Product explicitly
  states "excluding prime movers" in its subtitle — prime movers are NOT
  eligible under that Streamlined pathway. They only reappear as an
  eligible asset under the Balloon/Residual Refinance Streamlined
  Product ("Prime movers included").
trigger_keywords: [prime mover, excluded, road train head]
rationale: >
  Consistent with the elevated risk profile of prime movers seen at
  other lenders in this catalog (Resimac reference, Section 1.4) —
  Metro routes new prime mover finance away from the standard streamlined
  fast-track and only permits them under the narrower Balloon/Residual
  Refinance product, likely reflecting a preference for assessing new
  prime mover deals individually via the main rate card rather than a
  fast-track policy.
```

---

## 5. MetroEco Suite (Green Asset Finance)

### 5.1 Electric Vehicles & Chargers

```yaml
term: MetroEco Electric Vehicles & Chargers
definition: >
  A dedicated EV finance line with three channels — Commercial,
  Consumer, and Novated — each with the SAME loan amount cap but
  different maximum terms.
loan_amount_cap: Up to $91,387.00 on vehicles (all three channels — this
  figure is the LCT — Luxury Car Tax — threshold, adjusted annually)
loan_term_by_channel:
  Commercial: 60 months, max EOT 5 years
  Consumer: 84 months, max EOT 7 years
  Novated: 60 months, max EOT 5 years
age_of_asset: New or Demo* (all channels)
eligibility:
  - Vehicle solely powered by electricity, charged via an external plug
  - Demonstrator vehicles must be no more than 12 months old with no
    more than 5,000km on the odometer
special_notes:
  - Bundling an EV charger on the same application unlocks "the vehicle
    carded rate" for the charger too
  - FBT (Fringe Benefits Tax) exemptions may apply to novated leasing —
    applicants should confirm with their salary packager
  - Approvals valid for 90 days
trigger_keywords: [MetroEco, electric vehicle, EV, novated lease, FBT exemption]
rationale: >
  The $91,387 cap tracks the Luxury Car Tax threshold for fuel-efficient
  vehicles — financing above this amount falls outside the dedicated EV
  product and would need to be assessed under the standard vehicle rate
  card instead.
```

### 5.2 Electric Trucks

```yaml
term: MetroEco Electric Trucks
definition: >
  A streamlined product specifically for battery electric trucks 3.5t
  GVM and above, with a 1% MetroEco rate discount.
eligibility:
  - Brand new assets only (no used electric trucks)
  - Dealer sale only (no private sale)
  - ABN & GST registered for a minimum of 2 years continuously
  - Comparable credit reference on a current/previous asset finance
    facility, within the last 12 months, on similar assets
  - Battery Electric Trucks only, 3.5t GVM and above
  - Property owners only (non-property-backed applicants not eligible)
loan_amounts:
  - Up to $250,000 for new customers
  - Up to $300,000 for customers with 12 months good repayment history with Metro
transaction_caps:
  - $600,000 maximum transaction size with full financials
  - $700,000 maximum (Electric Truck) exposure
exclusions:
  - Excludes biofuel powered or hybrid trucks (battery electric only)
trigger_keywords: [electric truck, battery electric truck, MetroEco discount, biofuel exclusion]
rationale: >
  Excluding biofuel/hybrid trucks keeps the discount targeted at the
  cleanest technology tier, and the property-owner-only requirement
  reflects the higher asset value/risk of trucks compared with passenger
  EVs.
```

### 5.3 Solar, Batteries & Chargers

```yaml
term: MetroEco Solar, Batteries & Chargers
definition: >
  A streamlined product for new-only solar/battery/charger installations,
  with a longer maximum term for solar than for batteries alone.
specification:
  age_of_asset: New only
  min_loan_amount: $10,000
  max_loan_amount_other_equipment: $100,000
  min_loan_term: 12 months (fully amortised)
  max_loan_term: 84 months (fully amortised) for solar; batteries on
    their own are capped at a 60-month max term
  property_ownership: Borrower or guarantor must own the property where
    the installation is installed
  credit_reference: Comparable reference running at least 12 months with
    satisfactory conduct (active or paid out within the last 6 months),
    OR 12 months of mortgage statements
  min_abn_gst_registration: ABN & GST registered for 2 years continuously
  supplier: Must be a verified supplier
  credit_file: Satisfactory Equifax on applicant and guarantors
solar_upfront_requirements:
  property_ownership:
    - Borrower or guarantor must own the property where installation is
      installed — leasehold properties are NEVER considered
    - Owner-occupied property considered with a business use letter
    - Residential investment property considered with a copy of the
      current lease agreement confirming the property is tenanted
    - The applicant or guarantor must hold at least 50% ownership
  supplier_installer_accreditations:
    - NETCC accredited seller
    - SAA accredited installer
    - Asset must be listed on the register of CEC-approved products
  other_conditions:
    - Maximum purchase price $500,000
    - Maximum exposure limit $700,000
    - STC (Small-scale Technology Certificate) assignment form with
      photos required prior to settlement
trigger_keywords: [solar, battery, EV charger, MetroEco, NETCC, SAA, CEC approved, STC assignment]
rationale: >
  The hard exclusion of leasehold properties (with no exceptions) and
  the accreditation requirements (NETCC/SAA/CEC) exist because solar
  installations are physically fixed to a property and only reliably
  valuable/recoverable if the installer and equipment meet recognised
  industry standards — an unaccredited installation may not be safely
  repossessable or resaleable, and could expose Metro to compliance risk
  under Australian solar/STC regulations.
```

---

## 6. Streamlined Products — Detail Tables

### 6.1 Passenger Vehicle Streamlined Product (<3.5t GVM)

| Property Ownership | Max Loan Size | Max Metro Exposure | GST Registration | Credit Reference | Age at EOT |
|---|---|---|---|---|---|
| Borrower/guarantor's name | $150,000 (dealer & private); $200,000 (12mo good history, dealer & private) | $250,000 new / $500,000 (12mo history) / $750,000 (24mo history) | Registered 2 years continuously | Comparable asset finance ref (12mo) OR 12mo mortgage statements if no reference available, for amounts up to $100,000 | No older than 12 years |
| Spouse's name | $150,000 (dealer & private) | $150,000 | — | — | — |
| Non-property backed (motor vehicles only) | $100,000, dealer sale only, 30% deposit required | $100,000 | — | — | — |

**Special note:** Taxi/Uber/Rideshare applications — maximum customer exposure $250,000 and **must be property
backed** (no non-property-backed rideshare deals permitted).

### 6.2 Trucks, Trailers & Wheeled Equipment Streamlined Product (>3.5t GVM, excluding prime movers)

| Property Ownership | Max Loan Size | Max Metro Exposure | GST Registration | Credit Reference | Age at EOT | Eligible Assets |
|---|---|---|---|---|---|---|
| Borrower/guarantor's name | $250,000 (dealer & private, new); $300,000 (12mo history); max $250,000 for private sales specifically | $250,000 new / $500,000 (12mo) / $750,000 (24mo) | Registered 2 years continuously | Comparable asset finance ref (12mo) | No older than 15 years, no balloon/residual at 15yr EOT | 3.5t GVM+, vehicles, trailers, earthmoving equipment, yellow goods, material handling equipment |
| Spouse's name | $150,000 (dealer & private) | $150,000 | — | — | — | — |
| Non-property backed (motor vehicles only) | $100,000, dealer sale only, 30% deposit | $100,000 | — | — | — | — |

### 6.3 Replacement Policy Streamlined Product

| Property Ownership | Max Loan Size | Max Metro Exposure | GST Registration | Credit Reference | Age at EOT | Replacement Criteria |
|---|---|---|---|---|---|---|
| Borrower/guarantor's name | $150,000 (passenger/light commercial); $300,000 (medium/heavy commercial excl. prime movers, trailers, wheeled equipment); max $250,000 for private sales | $300,000 new / $500,000 (12mo) / $750,000 (24mo) | Must have ABN with current GST registration (no 24-month minimum required) | Satisfactory reference on account being refinanced; contract being replaced must have run ≥36 months | Passenger/light commercial: ≤12 years; all other equipment: ≤15 years, no balloon at 15yr EOT | New loan amount ≤125% of original loan being replaced, OR new monthly repayment ≤125% of the monthly repayment being replaced |
| Spouse's name | $150,000 | $150,000 | — | — | — | — |
| Non-property backed | $100,000 (dealer & private) | $100,000 | — | — | — | — |

```yaml
term: Replacement Criteria (125% Rule)
definition: >
  Under the Replacement Policy, the new facility must satisfy EITHER of
  two independent tests: the new loan amount does not exceed 125% of the
  original loan amount being replaced, OR the new monthly repayment does
  not exceed 125% of the monthly repayment being replaced. Only one test
  needs to pass, not both.
trigger_keywords: [replacement policy, 125%, loan amount test, repayment test]
rationale: >
  Prevents a "replacement" from being used to substantially increase a
  customer's debt load under the guise of refinancing, while still
  allowing reasonable step-ups (e.g. for genuinely upgraded equipment)
  as long as one of the two proportional caps is respected.
```

### 6.4 Balloon/Residual Refinance Streamlined Product

| Property Ownership | Max Loan Size | Max Metro Exposure | GST Registration | Credit Reference | Age at EOT | Eligible Assets | Account Being Replaced |
|---|---|---|---|---|---|---|---|
| Borrower/guarantor's name | $150,000 | $300,000 new / $500,000 (12mo) / $750,000 (24mo) | Registered 2 years continuously | Satisfactory reference on account being refinanced (no inspection required) | Passenger/light commercial: ≤12 years; all other equipment: ≤15 years, no balloon at 15yr EOT | Motor vehicles & wheeled equipment only (**prime movers included**) | Must be in final 12 months |
| Spouse's name | $150,000 | $150,000 | — | — | — | — | — |
| Non-property backed | $150,000 | $150,000 | — | — | — | — | — |

```yaml
term: Balloon/Residual Refinance — "Account Being Replaced Must Be in Final 12 Months"
definition: >
  This product only applies when the existing contract with a balloon/
  residual payment due is within its LAST 12 months of term — it cannot
  be used to refinance a balloon that is still several years away from
  maturity.
trigger_keywords: [balloon payment, residual value, final 12 months, refinance]
rationale: >
  Restricts this product to its intended purpose — helping customers
  manage an imminent balloon/residual payment — rather than being used
  as a general-purpose early refinance tool years ahead of the actual
  balloon due date.
```

### 6.5 Other Equipment Streamlined Product

| Property Ownership | Age of Asset | Max Loan Size | Max Metro Exposure | Credit Reference | Eligible Assets | Non-Eligible Assets |
|---|---|---|---|---|---|---|
| Borrower/guarantor's name (Primary Equipment) | No older than 3 years; asset must be serial numbered | $10,000 min / $100,000 max | $100,000 including current Metro exposure | Registered 2 years continuously; comparable reference (12mo, similar assets) | Tools of trade; earthmoving & construction equipment; manufacturing & workshop equipment; agricultural and forestry equipment | Fixtures & fittings; IT, AV, telephony & printing; retail, health/beauty & fitness; mining; intangible assets |

**Additional notes:** Must be from a recognised supplier (no private sale or sale/hire back); maximum term 60
months, nil balloon.

**Eligible Equipment Guide** (illustrative, not exhaustive) includes: attachments, surveying equipment, large
engineering equipment, manufacturing lines, packing/robotic packaging/wrapping/weighing equipment, workshop
equipment, vacuum excavators, CNC, dust extractors, dustless sandblasters, edge banders, lasers, lathes, machining
centres, ATVs, augers, pumps and power equipment, direction drills, farming implements & machinery, feeding
equipment, grain handling, portable dipping/testing, GPS equipment, generators/welders/pumps/plumbing equipment,
dynamometers, radios (UHF/VF/HF), routers, tools of trade, medical and dental equipment, panel saws.

**Non-Eligible Assets** (illustrative, not exhaustive) includes: air conditioning units & ducting, audio visual
equipment, blinds, carpets, catering, coffee machines, desks, display units, drones, fixture/fitting, furniture,
gym equipment, health/beauty equipment/fitness, IT equipment, kitchen, LED lighting, mining, partitions, printers,
racking (fixed and freestanding), safes and strong rooms, scaffolding, solar (has its own MetroEco product — see
Section 5.3), spray booths, telephone systems.

### 6.6 Agri Streamlined Product

| Category | Max Loan Size | Max Metro Exposure | GST Registration | Credit Reference | Age of Asset | Eligible Assets |
|---|---|---|---|---|---|---|
| Primary Equipment | $10,000 min / $250,000 max (dealer/private); $300,000 max (12mo good history) | $250,000 new / $500,000 (12mo) / $750,000 (24mo) | GST registered >5 years | Comparable reference (12mo, similar asset) | No older than 15 years at EOT, no balloon/residual out to 15yrs; max term 60 months | Tractors, harvesters, wheeled handling equipment, self-propelled mower conditioners, self-propelled sprayers |
| Implements/Tertiary Equipment | $10,000 min / $150,000 max (dealer/private) | $150,000 (new and existing customers) | GST registered >5 years | Comparable reference (12mo, similar asset) | No older than 15 years at EOT; max term 60 months/nil balloon | Tillage seeding, spraying, grain handling hay & silage |

**Additional criteria:** Must be a genuine primary producer; minimum farm size 40 hectares; maximum $500,000 in a
12-month period under streamlined; no sale/hire back; satisfactory Equifax; goods must be serial numbered and
"cannot be fixed" (i.e. not permanently affixed structures); monthly payments only.

**Non-Eligible Assets:** Sheds, silos, yards; testing and measurement equipment (note: can be financed under
"Other Equipment" Streamlined Policy if under $100k); dairy equipment; irrigation equipment; bikes & ATVs (note:
ATVs can be financed under "Other Equipment" Streamlined Policy if under $100k); excludes the forestry industry
and its assets entirely.

```yaml
term: Agri Streamlined — Cross-Referral to "Other Equipment" Policy
definition: >
  Certain items that are technically excluded from the Agri Streamlined
  Product (testing/measurement equipment, and ATVs/bikes) are not
  entirely unfinanceable — they can instead be routed through the
  "Other Equipment" Streamlined Product, but only if the amount is under
  $100,000.
trigger_keywords: [testing equipment, ATV, cross-referral, Other Equipment policy]
rationale: >
  Keeps the Agri policy focused on core farm production assets while
  still giving brokers a valid pathway for smaller peripheral equipment
  purchases via a different, more general-purpose streamlined product.
```

---

## 7. Why Some Categories Face More Restrictions

Metro's pattern mirrors the same underlying logic seen at Resimac and Westpac: **restrictions tighten as resale
market depth and valuation predictability decrease.**

| Factor | Passenger/Commercial Vehicles | Trucks/Trailers/Wheeled Equipment | Other Equipment (Primary) | Agri Implements/Tertiary |
|---|---|---|---|---|
| Max age at EOT | 12 years | 15 years | 3 years | 15 years |
| Balloon available | Yes (main rate card) | No, if lent to 15yr EOT | No (nil balloon stated) | No (nil balloon on Implements) |
| Supplier restriction | Dealer & private sale allowed | Dealer & private sale allowed | Recognised supplier only (no private sale) | Dealer/private sale allowed, but "cannot be fixed" |
| Max loan size (borrower-owned) | $150k–$200k | $250k–$300k | $100k | $150k–$300k |

**Other Equipment's 3-year age cap** is the tightest in the entire Metro suite — far shorter than every other
Streamlined Product's 12–15 year allowance. This reflects that "Other Equipment" spans a very broad, heterogeneous
set of tools/machinery (from CNC machines to augers to dynamometers) with no single standardised depreciation
curve, so Metro compensates with the shortest permissible asset age rather than a rate loading.

**Agri Implements/Tertiary equipment** (tillage, seeding, spraying, grain handling attachments) is capped at a much
lower loan size ($150k vs $300k for Primary Agri Equipment like tractors/harvesters) because implements have far
less standalone resale value than the core machinery they attach to — directly parallel to the "attachment
bundling" logic seen at Westpac (Exceptions Catalog EX008).

---

## 8. Fees Explained (Main Commercial Asset Finance Rate Card)

```yaml
fee_name: Metro Establishment Fee (Minimum/Maximum)
amount: Minimum $275; Maximum $450, excluding a 50/50 split arrangement
when_charged: At loan establishment
purpose: Covers Metro's cost of originating and documenting the finance contract
trigger_keywords: [Metro fee, establishment fee, minimum fee, maximum fee]
notes: >
  The "excluding split 50/50" note suggests that where a fee is split
  between two parties (e.g. broker and Metro, or two co-borrowers), the
  $450 maximum does not apply to each split portion individually —
  confirm the exact mechanics with Metro's BDM team if structuring a
  split-fee deal.
```

```yaml
fee_name: Loan Size Caps (Main Rate Card)
amount: Single assets capped at $1,000,000; total customer exposure capped at $2,000,000
when_charged: Structural limit, not a fee, but included here for completeness
purpose: Caps Metro's maximum exposure to any single asset or single customer under the main rate card
trigger_keywords: [loan size, single asset cap, customer exposure cap]
```

---

## 9. Cross-Lender Comparison Notes

For quick reference when comparing Metro against Resimac/Westpac/CFAL (see the multi-lender Exceptions Catalog):

- **Private sale loading**: Metro (+0.25%) is materially lower than Resimac's risk loading (+2%) for the same
  trigger — reflects different lender risk appetites, not a discrepancy to "correct."
- **EOT concept**: Used by both Metro and Resimac, but Metro mostly applies it as a hard maximum-term cutoff within
  Streamlined Products (12/15/3 years), while also using it as a rate loading trigger (+1% for >10yr EOT) on the
  main rate card — Resimac uses it purely as a risk-loading trigger (+2%) with no separate hard cutoff.
- **Spouse-owned property**: Metro gives spouse-owned property a fixed reduced loan size ($150,000), whereas
  Resimac does not count it as property-backed at all (only a deposit waiver) and Westpac may accept it as full
  property backing at credit discretion — three different treatments of the same concept across three lenders.
- **Non-property-backed deposit**: Metro requires a flat 30% deposit for non-property-backed motor vehicle deals;
  Resimac's equivalent is 10% for motor vehicles (non-property-backed) — again, different risk pricing philosophies.

---

## 10. Exceptions Catalog (Metro)

The following are the specific "exception" clauses in the Metro suite — rules that deviate from the general
pattern established elsewhere in this document. Each uses the same schema as the multi-lender Exceptions Catalog
(Westpac / CFAL / Resimac, EX001–EX038) so all four lenders' exceptions can eventually be merged into one
retrieval set. IDs continue that numbering from EX039.

```yaml
exception_id: EX039
title: Prime Movers Excluded from Trucks/Trailers/Wheeled Equipment Streamlined, Eligible Only Under Balloon/Residual Refinance
source_document: Metro — Trucks, Trailers & Wheeled Equipment Streamlined Product / Balloon/Residual Refinance Streamlined Product
policy_statement: >
  "Medium & Heavy Commercial Vehicles >3.5t GVM (excluding prime movers)"
  [Trucks/Trailers/Wheeled Equipment]; "Eligible Assets: For motor
  vehicles & wheeled equipment only (Prime movers included)"
  [Balloon/Residual Refinance].
interpretation: >
  New prime mover finance cannot be arranged through the Trucks/
  Trailers/Wheeled Equipment Streamlined fast-track product at all. The
  ONLY Streamlined pathway that accepts prime movers is Balloon/Residual
  Refinance — and only for an existing contract nearing its balloon due
  date, not a brand-new prime mover purchase.
business_rationale: >
  Reflects the elevated risk profile of prime movers (heavy usage
  intensity, specialised resale market) — Metro prefers to assess new
  prime mover deals individually via the main rate card (with its
  loading structure) rather than fast-track them, but still allows
  existing prime mover customers to refinance an imminent balloon
  through the narrower, already-known-risk Balloon/Residual product.
examples:
  eligible:
    - Existing Metro prime mover contract with a balloon due in 8 months
      -> eligible for Balloon/Residual Refinance Streamlined
  ineligible:
    - New customer wanting to finance a brand-new prime mover via the
      Trucks/Trailers/Wheeled Equipment Streamlined Product -> not
      eligible; must go through the main Commercial Asset Finance rate
      card instead
business_logic: |
  IF asset_type == "prime_mover":
    IF streamlined_product == "Trucks/Trailers/Wheeled Equipment":
      not_eligible
    ELSE IF streamlined_product == "Balloon/Residual Refinance"
         AND existing_balloon_due_within_12_months:
      eligible
    ELSE:
      route_to_main_rate_card
keywords:
  - prime mover
  - excluded
  - balloon refinance
synonyms:
  prime mover:
    - truck tractor
    - road train head
intent_examples:
  - "Can I finance a new prime mover through the streamlined truck policy?"
  - "Is a prime mover eligible for balloon refinance?"
decision: Conditional — Excluded from Trucks/Trailers/Wheeled Equipment; eligible only under Balloon/Residual Refinance for imminent balloons
related_policy:
  - Section 4 (Prime Movers definition)
  - Section 6.2 / 6.4 (Streamlined product tables)
```

```yaml
exception_id: EX040
title: Taxi/Uber/Rideshare Must Be Property Backed (Passenger Vehicle Streamlined)
source_document: Metro — Passenger Vehicle Streamlined Product
policy_statement: >
  "Taxi/Uber/Ride share applications - maximum customer exposure
  $250,000 and must be property backed."
interpretation: >
  Ride-share/taxi vehicle finance cannot use the Non-Property-Backed tier
  at all, even though that tier is otherwise available for standard
  passenger vehicles. Property backing is mandatory, and total exposure
  for this specific use-case is capped at $250,000 regardless of
  repayment history tier.
business_rationale: >
  Ride-share/taxi vehicles are used far more intensively (higher
  mileage, commercial wear) than a standard passenger vehicle, and carry
  higher usage/liability risk, so Metro removes the weakest security
  tier (non-property-backed) entirely for this use-case and caps total
  exposure independent of the usual repayment-history-based scaling.
examples:
  eligible:
    - Uber driver, property-backed guarantor, $200,000 vehicle finance
      request -> eligible (within the $250k cap)
  ineligible:
    - Uber driver with no property backing -> not eligible regardless of
      deposit offered (non-property-backed tier is not available for
      this use-case)
    - Property-backed Uber driver requesting $280,000 -> exceeds the
      $250k use-case-specific cap even though standard property-backed
      limits might otherwise be higher
business_logic: |
  IF vehicle_use == "taxi/uber/rideshare":
    require(property_backed == True)
    max_exposure = MIN(requested_exposure, $250,000)
  ELSE:
    apply_standard_passenger_vehicle_tiers
keywords:
  - taxi
  - Uber
  - rideshare
  - property backed
synonyms:
  rideshare:
    - taxi
    - Uber
    - Ola
    - DiDi
intent_examples:
  - "Can I finance an Uber vehicle without property backing?"
  - "What is the exposure limit for a taxi driver?"
decision: Not Eligible without property backing; capped at $250,000 exposure even if property backed
related_policy:
  - Section 6.1 (Passenger Vehicle Streamlined Product table)
```

```yaml
exception_id: EX041
title: Replacement Policy 125% Dual-Test Rule
source_document: Metro — Replacement Policy Streamlined Product
policy_statement: >
  "New loan amount not to exceed 125% of the original loan amount of the
  contract being replaced OR Proposed monthly repayment does not exceed
  125% of the monthly repayment of the contract being replaced."
interpretation: >
  The new facility only needs to pass ONE of two independent tests — the
  loan amount test or the monthly repayment test — not both. This gives
  flexibility for deals where, e.g., a longer term keeps repayments low
  even if the loan amount itself grows by more than 25%.
business_rationale: >
  Prevents "replacement" finance from being used to substantially
  increase a customer's debt burden under the guise of refinancing,
  while still allowing reasonable step-ups in either loan size or term
  structure as long as one of the two proportional caps is respected.
examples:
  eligible:
    - Original loan $100,000; new loan $145,000 (145% — FAILS the loan
      amount test), but new monthly repayment is only 110% of the
      original repayment (due to a longer term) -> PASSES via the
      repayment test, so still eligible
  ineligible:
    - New loan amount 140% of original AND new monthly repayment 140% of
      original -> fails both tests, not eligible under Replacement Policy
business_logic: |
  eligible = (new_loan_amount <= 1.25 * original_loan_amount)
             OR (new_monthly_repayment <= 1.25 * original_monthly_repayment)
keywords:
  - replacement policy
  - 125% rule
  - loan amount test
  - repayment test
synonyms:
  replacement policy:
    - refinance policy
intent_examples:
  - "Does my replacement loan need to pass both the amount and repayment tests?"
  - "What happens if the new loan amount exceeds 125% but repayments don't?"
decision: Conditional — Eligible if EITHER of the two 125% tests is satisfied
related_policy:
  - Section 6.3 (Replacement Policy Streamlined Product table)
```

```yaml
exception_id: EX042
title: Balloon/Residual Refinance Restricted to Final 12 Months of Existing Contract
source_document: Metro — Balloon/Residual Refinance Streamlined Product
policy_statement: >
  "Account Being Replaced: Must be in final 12 months."
interpretation: >
  This product can only be used when the existing contract's balloon/
  residual payment is due within the next 12 months — it cannot be used
  to refinance a balloon that is still years away from maturity.
business_rationale: >
  Keeps this Streamlined product targeted at its intended purpose
  (helping customers manage an imminent balloon payment) rather than
  functioning as a general early-refinance tool for any active contract.
examples:
  eligible:
    - Existing contract with a balloon due in 6 months -> eligible
  ineligible:
    - Existing contract with a balloon due in 30 months -> not eligible
      under this Streamlined product (too far from maturity)
business_logic: |
  IF (balloon_due_date - today) <= 12 months:
    eligible_for_balloon_residual_refinance
  ELSE:
    not_eligible  # consider standard refinance assessment instead
keywords:
  - balloon payment
  - residual value
  - final 12 months
  - refinance timing
synonyms:
  balloon:
    - residual payment
    - end-of-term payment
intent_examples:
  - "Can I refinance a balloon that's due in 2 years?"
  - "How close to the balloon due date do I need to be to qualify?"
decision: Not Eligible unless the existing balloon is due within 12 months
related_policy:
  - Section 6.4 (Balloon/Residual Refinance Streamlined Product table)
```

```yaml
exception_id: EX043
title: Non-Property-Backed Motor Vehicles Require 30% Deposit + Dealer Sale Only
source_document: Metro — Passenger Vehicle / Trucks, Trailers & Wheeled Equipment Streamlined Products
policy_statement: >
  "Non-property backed (motor vehicles only): $100,000, Dealer sale
  only, (30% deposit required)."
interpretation: >
  Applicants with no property backing at all can still finance a motor
  vehicle, but only up to $100,000, only via a dealer (private sale not
  permitted), and only with a 30% deposit — stacking three separate
  restrictions simultaneously.
business_rationale: >
  With no property security at all, Metro compensates via multiple
  layers: capping the loan size, requiring dealer-verified provenance
  (removing private-sale risk), and requiring a substantial deposit to
  reduce the loan-to-value ratio and the lender's exposure.
examples:
  eligible:
    - Non-property-backed applicant, dealer-sourced $70,000 vehicle, 30%
      deposit ($21,000) provided, financed amount $49,000 -> within the
      $100k cap and meets the deposit requirement
  ineligible:
    - Non-property-backed applicant wanting to buy privately -> not
      eligible; dealer sale is mandatory for this tier
    - Non-property-backed applicant offering only a 15% deposit -> does
      not meet the 30% requirement
business_logic: |
  IF property_backed == False AND asset_type == "motor_vehicle":
    require(supplier_type == "dealer")
    require(deposit_pct >= 30%)
    max_loan_size = $100,000
keywords:
  - non-property backed
  - 30% deposit
  - dealer sale only
synonyms:
  non-property backed:
    - no property security
    - unsecured applicant
intent_examples:
  - "Can I buy a car privately if I don't own property?"
  - "What deposit do I need without property backing?"
decision: Conditional — Eligible only with dealer sale, 30% deposit, capped at $100,000
related_policy:
  - Section 2 (Streamlined Product Framework — Property Ownership Tiers)
  - EX049 (Vehicle Streamlined Non-Property Product +1% Loading)
```

```yaml
exception_id: EX044
title: Spouse-Owned Property Fixed at $150,000 (Does Not Scale with Repayment History)
source_document: Metro — All Streamlined Products (repeating pattern)
policy_statement: >
  "In spouse's name: $150,000 / $150,000" — appears identically across
  Passenger Vehicle, Trucks/Trailers/Wheeled Equipment, Replacement
  Policy, and Balloon/Residual Refinance Streamlined Products.
interpretation: >
  Unlike the borrower/guarantor-owned property tier (which scales up to
  $300k+ loan size and $750k exposure based on 12/24 months of good
  repayment history), the spouse-owned property tier is a FIXED
  $150,000 regardless of how long or how well the customer has repaid
  previous Metro facilities.
business_rationale: >
  Spousal property ownership is treated as a materially weaker security
  position than direct borrower/guarantor ownership (the borrower has no
  direct legal claim on the asset), so Metro does not extend the same
  repayment-history-based scaling benefits to this tier — good repayment
  history increases exposure only for the strongest (borrower-owned)
  security tier.
examples:
  eligible:
    - Applicant with 3 years of perfect Metro repayment history, but
      property is in spouse's name -> still capped at $150,000, the same
      as a brand-new customer with spouse-owned property
  ineligible:
    - Applicant tries to claim the $500,000 (12-month history) or
      $750,000 (24-month history) exposure tier based on spouse-owned
      property -> not available; those scaled tiers apply only to
      borrower/guarantor-owned property
business_logic: |
  IF property_ownership == "spouse":
    max_loan_size = $150,000  # fixed, does not scale with repayment history
  ELSE IF property_ownership == "borrower_or_guarantor":
    max_loan_size = scale_by_repayment_history(12mo -> higher tier, 24mo -> highest tier)
keywords:
  - spouse-owned property
  - fixed limit
  - repayment history
synonyms:
  spouse-owned property:
    - spousal property
intent_examples:
  - "Does good repayment history increase my limit if the property is in my spouse's name?"
  - "Why is spouse-owned property capped lower than my own property?"
decision: Fixed at $150,000 — does not scale with repayment history, unlike borrower-owned property
related_policy:
  - Section 2 (Streamlined Product Framework — Property Ownership Tiers)
```

```yaml
exception_id: EX045
title: MetroEco Electric Trucks Excludes Biofuel or Hybrid
source_document: Metro — MetroEco Electric Trucks
policy_statement: >
  "*Excludes biofuel powered or hybrid."
interpretation: >
  The MetroEco Electric Trucks product (with its 1% rate discount and
  streamlined criteria) applies ONLY to battery electric trucks — biofuel
  and hybrid trucks are explicitly excluded, even though they might be
  considered "green" or lower-emission by some standards.
business_rationale: >
  Keeps the MetroEco discount targeted specifically at the cleanest
  (zero tailpipe emission) technology tier, avoiding discount "creep"
  toward partially fossil-fuel-dependent vehicles.
examples:
  eligible:
    - Brand new battery electric truck, 3.5t GVM -> eligible for the 1%
      MetroEco discount
  ineligible:
    - Hybrid diesel-electric truck -> not eligible for MetroEco Electric
      Trucks discount (would need to be assessed under the standard
      Heavy Commercial Vehicle rate card instead)
    - Biofuel-powered truck -> excluded regardless of emissions profile
business_logic: |
  IF asset_type == "truck" AND powertrain == "battery_electric":
    eligible_for_metroeco_electric_truck_discount = True
  ELSE IF powertrain IN {"hybrid", "biofuel"}:
    eligible_for_metroeco_electric_truck_discount = False
    # route to standard Heavy Commercial Vehicle rate card instead
keywords:
  - electric truck
  - biofuel exclusion
  - hybrid exclusion
  - MetroEco discount
synonyms:
  battery electric:
    - BEV
    - fully electric
intent_examples:
  - "Does a hybrid truck qualify for the MetroEco discount?"
  - "Is a biofuel truck eligible for the electric truck product?"
decision: Not Eligible for biofuel or hybrid trucks — battery electric only
related_policy:
  - Section 5.2 (MetroEco Electric Trucks)
```

```yaml
exception_id: EX046
title: MetroEco Solar — Leasehold Properties Never Considered
source_document: Metro — MetroEco Solar, Batteries & Chargers (Solar Upfront Requirements)
policy_statement: >
  "Borrower or guarantor must own the property where installation is
  installed – will NOT consider for leasehold properties under any
  circumstances."
interpretation: >
  This is an absolute, no-exceptions exclusion — unlike most other rules
  in this document that allow case-by-case discretion, leasehold
  properties are categorically ineligible for MetroEco solar finance,
  with no pathway to override this even at Metro's discretion.
business_rationale: >
  Solar installations are physically fixed to the property. On a
  leasehold property, the installer/lender's ability to secure, recover,
  or even guarantee continued access to the asset is legally
  complicated by the underlying lease terms and landlord's rights, making
  the security position too weak to accept under any circumstances.
examples:
  eligible:
    - Owner-occupied property (owned outright or with a business use
      letter) -> eligible
    - Residential investment property, tenanted, with a copy of the
      current lease agreement -> eligible
  ineligible:
    - Leasehold property (regardless of the strength of the applicant's
      financials, guarantor support, or deposit offered) -> not eligible,
      no exceptions
business_logic: |
  IF property_tenure == "leasehold":
    application_not_eligible = True  # absolute exclusion, no discretion override
  ELSE IF property_tenure IN {"owner_occupied_with_business_use_letter",
                                "residential_investment_tenanted_with_lease_copy"}:
    eligible_subject_to_other_criteria = True
keywords:
  - leasehold
  - solar
  - property ownership
synonyms:
  leasehold:
    - leased property
    - rented commercial premises
intent_examples:
  - "Can I get solar finance for a leasehold property?"
  - "Is there any exception for leasehold properties under MetroEco Solar?"
decision: Not Eligible — leasehold properties are excluded absolutely, with no discretionary override
related_policy:
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX047
title: Agri Cross-Referral to "Other Equipment" Policy for Testing Equipment/ATVs Under $100k
source_document: Metro — Agri Streamlined Product (Non-Eligible Assets notes)
policy_statement: >
  "Testing and measurement equipment (note can be done under 'Other
  Equipment' streamlined policy <$100k)... Bikes & ATV's (note that
  ATV's can be done under 'Other Equipment' streamlined policy <$100k)."
interpretation: >
  Testing/measurement equipment and ATVs are excluded from the Agri
  Streamlined Product itself, but are not entirely unfinanceable — they
  can be routed through the separate "Other Equipment" Streamlined
  Product instead, provided the amount is under $100,000.
business_rationale: >
  Keeps the Agri policy focused on core production assets (tractors,
  harvesters, implements) while still giving brokers a valid, simple
  alternative pathway for smaller peripheral equipment that doesn't fit
  the Agri policy's specific asset list.
examples:
  eligible:
    - $60,000 ATV purchase for a farm business -> not eligible under Agri
      Streamlined, but IS eligible under Other Equipment Streamlined
      (since it's under $100k)
  ineligible:
    - $150,000 testing/measurement equipment purchase -> exceeds the
      $100k threshold for the Other Equipment cross-referral pathway;
      not eligible under either Streamlined product (would need standard
      assessment)
business_logic: |
  IF asset_type IN {"testing/measurement equipment", "ATV", "bike"}:
    not_eligible_under_agri_streamlined = True
    IF amount < $100,000:
      route_to_other_equipment_streamlined_product
    ELSE:
      route_to_standard_assessment
keywords:
  - ATV
  - testing equipment
  - cross-referral
  - Other Equipment policy
synonyms:
  ATV:
    - all-terrain vehicle
    - quad bike
intent_examples:
  - "Can I finance an ATV under the Agri policy?"
  - "What policy covers testing equipment for a farm business?"
decision: Not Eligible under Agri Streamlined; conditionally eligible under Other Equipment Streamlined if under $100,000
related_policy:
  - Section 6.5 (Other Equipment Streamlined Product)
  - Section 6.6 (Agri Streamlined Product)
```

```yaml
exception_id: EX048
title: Other Equipment (Primary Equipment) 3-Year Age Cap
source_document: Metro — Other Equipment Streamlined Product
policy_statement: >
  "Age of Asset: No older than 3 years; Asset must be serial numbered."
interpretation: >
  While most other Metro Streamlined Products allow assets up to 12–15
  years old at end of term, the Other Equipment Streamlined Product caps
  eligible asset age at just 3 years — the tightest limit anywhere in
  the Metro suite.
business_rationale: >
  "Other Equipment" spans an extremely broad and heterogeneous range of
  tools/machinery (from CNC machines to augers to dynamometers) with no
  single standardised depreciation curve or resale market comparable to
  vehicles or core agricultural machinery, so Metro compensates for this
  valuation uncertainty with the shortest permissible asset age rather
  than a rate loading.
examples:
  eligible:
    - Brand new CNC machine (0 years old) -> eligible
    - 2-year-old workshop equipment -> eligible
  ineligible:
    - 5-year-old manufacturing line equipment -> exceeds the 3-year cap;
      not eligible under this Streamlined product (may require standard
      assessment via the main rate card instead)
business_logic: |
  IF product == "Other Equipment Streamlined" AND asset_category == "Primary Equipment":
    require(asset_age_years <= 3)
    require(asset_is_serial_numbered == True)
keywords:
  - Other Equipment
  - 3-year age cap
  - serial numbered
synonyms:
  Other Equipment:
    - tools of trade
    - workshop equipment
intent_examples:
  - "Can I finance a 5-year-old CNC machine under Other Equipment Streamlined?"
  - "Why is the age limit so much shorter for Other Equipment than for trucks?"
decision: Not Eligible if asset is older than 3 years — the tightest age cap in the Metro suite
related_policy:
  - Section 6.5 (Other Equipment Streamlined Product)
  - Section 7 (Why Some Categories Face More Restrictions)
```

```yaml
exception_id: EX049
title: Vehicle Streamlined Non-Property Product +1% Loading
source_document: Metro — Commercial Asset Finance rate card (Loadings)
policy_statement: >
  "1% loading on vehicle streamlined non-property product."
interpretation: >
  On top of the 30% deposit and dealer-sale-only restriction already
  required for non-property-backed vehicle deals (EX043), a further flat
  1% rate loading applies specifically to non-property-backed vehicle
  deals processed under the Streamlined pathway.
business_rationale: >
  Stacks an additional pricing compensation on top of the structural
  restrictions (deposit, dealer-only) to further offset the weaker
  security position of a non-property-backed applicant.
examples:
  eligible:
    - Non-property-backed applicant, dealer-sourced vehicle, 30% deposit
      provided, financed under the Streamlined pathway -> base rate + 1%
      loading applies
  ineligible (i.e., loading does not apply):
    - Property-backed applicant financing the same vehicle -> no 1%
      non-property loading applies
business_logic: |
  IF property_backed == False AND product_pathway == "Vehicle Streamlined":
    applicable_rate = base_rate + 1%
keywords:
  - non-property backed
  - streamlined loading
  - vehicle finance
synonyms:
  non-property backed:
    - no property security
intent_examples:
  - "Is there an extra rate loading for non-property-backed streamlined vehicle deals?"
decision: Conditional — +1% loading applies in addition to the 30% deposit/dealer-only restrictions
related_policy:
  - EX043 (Non-Property-Backed Motor Vehicles Require 30% Deposit + Dealer Sale Only)
  - Section 3 (Risk / Rate Loading Trigger Definitions)
```

```yaml
exception_id: EX050
title: MetroEco EV Loan Cap Tied to the Luxury Car Tax (LCT) Threshold ($91,387)
source_document: Metro — MetroEco Electric Vehicles & Chargers
policy_statement: >
  "Loan Amount: Up to $91,387.00 on vehicles" (Commercial, Consumer, and
  Novated channels).
interpretation: >
  The MetroEco EV product's loan cap is not an arbitrary round number —
  it aligns with the Luxury Car Tax (LCT) threshold for fuel-efficient
  vehicles, which is set by the Australian Government and adjusted
  annually (and will therefore change year to year, unlike a fixed
  internal policy limit).
business_rationale: >
  Financing above the LCT threshold would typically trigger Luxury Car
  Tax implications and push the vehicle outside the profile MetroEco is
  designed for (mainstream EV adoption); above this amount, the vehicle
  would need to be assessed under the standard vehicle rate card instead
  of the dedicated MetroEco product.
examples:
  eligible:
    - New EV priced at $85,000 -> eligible for MetroEco EV financing
  ineligible:
    - New EV priced at $110,000 -> exceeds the $91,387 cap; must be
      financed under the standard Commercial Asset Finance rate card
      instead of MetroEco
business_logic: |
  IF vehicle_price <= $91,387 (or the current LCT fuel-efficient threshold):
    eligible_for_metroeco_ev_product = True
  ELSE:
    route_to_standard_vehicle_rate_card
keywords:
  - MetroEco
  - electric vehicle
  - Luxury Car Tax
  - LCT threshold
synonyms:
  LCT threshold:
    - Luxury Car Tax threshold
    - fuel-efficient vehicle threshold
intent_examples:
  - "Why is the MetroEco EV loan capped at exactly $91,387?"
  - "Can I finance a $110,000 EV under MetroEco?"
decision: Not Eligible above the LCT threshold — must use the standard vehicle rate card instead; note this figure changes annually
related_policy:
  - Section 5.1 (MetroEco Electric Vehicles & Chargers)
```

```yaml
exception_id: EX051
title: Increased Streamline Exposure Requires a Current or Recently Paid-Out Metro Contract
source_document: Metro — All Streamlined Products (repeating note)
policy_statement: >
  "For increased streamline exposure, applicant required to have a
  current Metro Contract or have a contract paid out within the past 6
  months."
interpretation: >
  The scaled-up exposure tiers (e.g. $500,000 for 12 months good
  history, $750,000 for 24 months good history) are only available to
  applicants who EITHER currently hold an active Metro contract OR had
  one paid out within the last 6 months — a lapsed relationship older
  than 6 months does not qualify for the increased tiers, even if the
  applicant's historical repayment conduct was good.
business_rationale: >
  Ensures the "good repayment history" being relied upon is recent and
  verifiable, rather than allowing an applicant to claim a scaled-up
  exposure limit based on a Metro relationship that ended long ago and
  may no longer reflect their current risk profile.
examples:
  eligible:
    - Applicant with a Metro contract paid out 3 months ago, with 18
      months of prior good repayment history -> eligible for increased
      streamline exposure
  ineligible:
    - Applicant whose last Metro contract was paid out 14 months ago
      (exceeds the 6-month recency window) -> not eligible for the
      increased exposure tiers, even with a historically good repayment
      record; reverts to the "new customer" exposure tier
business_logic: |
  IF has_active_metro_contract == True:
    eligible_for_increased_exposure_tiers = True
  ELSE IF (today - last_contract_payout_date) <= 6 months:
    eligible_for_increased_exposure_tiers = True
  ELSE:
    eligible_for_increased_exposure_tiers = False  # treated as new customer
keywords:
  - increased exposure
  - current contract
  - paid out within 6 months
synonyms:
  increased streamline exposure:
    - scaled exposure tier
    - repayment history tier
intent_examples:
  - "Do I still qualify for the higher exposure tier if my last Metro loan ended a year ago?"
  - "How recent does my Metro contract need to be for increased exposure?"
decision: Conditional — Requires an active contract, or one paid out within the last 6 months
related_policy:
  - Section 2 (Maximum Metro Exposure — scaling rule)
```

```yaml
exception_id: EX052
title: Maximum $500,000 per 12-Month Period Under Streamlined (Aggregate Cap Across Deals)
source_document: Metro — All Streamlined Products (repeating note)
policy_statement: >
  "Maximum $500,000 in a 12 month period under streamlined."
interpretation: >
  This is a rolling 12-month aggregate cap across ALL Streamlined
  product deals for a given customer — separate from, and in addition
  to, the per-product Maximum Loan Size and Maximum Metro Exposure
  figures already listed in each product's table.
business_rationale: >
  Prevents a customer from using the fast-track Streamlined pathway
  repeatedly within a short period to accumulate an unusually large
  total exposure without ever going through a full/standard credit
  assessment.
examples:
  eligible:
    - Customer takes a $200,000 Streamlined truck deal in March and a
      $250,000 Streamlined Other Equipment deal in September (same
      12-month window) -> total $450,000, within the $500k cap
  ineligible:
    - Same customer attempts a further $150,000 Streamlined deal in
      November (same 12-month window) -> would bring the rolling total
      to $600,000, exceeding the $500k cap; this deal would need
      standard (non-Streamlined) assessment instead
business_logic: |
  rolling_12_month_streamlined_total = SUM(all streamlined deals in
                                            the trailing 12 months)
  IF rolling_12_month_streamlined_total + new_deal_amount > $500,000:
    new_deal_not_eligible_under_streamlined  # route to standard assessment
keywords:
  - streamlined cap
  - 12-month aggregate
  - $500,000 limit
synonyms:
  streamlined cap:
    - rolling exposure cap
    - aggregate streamlined limit
intent_examples:
  - "Can I do multiple streamlined deals in the same year?"
  - "What happens if my combined streamlined deals exceed $500,000?"
decision: Not Eligible under Streamlined once the rolling 12-month total across all Streamlined deals would exceed $500,000
related_policy:
  - Section 6 (all Streamlined Product tables — this cap applies across all of them)
```

```yaml
exception_id: EX053
title: Private Sale Transaction Size Cap for Trucks/Trailers/Wheeled Equipment ($250k Regardless of Tier)
source_document: Metro — Trucks, Trailers & Wheeled Equipment Streamlined Product
policy_statement: >
  "Maximum transaction size of $250,000 for private sales."
interpretation: >
  Even though the borrower/guarantor-owned property tier can otherwise
  reach $300,000 for customers with 12 months of good repayment history,
  private sale transactions specifically are capped at $250,000 —
  overriding the higher dealer-sale limit for this asset category.
business_rationale: >
  Private sales lack dealer verification/warranty, so Metro caps the
  transaction size lower for private sales regardless of how favourable
  the customer's repayment history tier would otherwise allow, limiting
  the lender's exposure to the harder-to-verify transaction type.
examples:
  eligible:
    - Customer with 12 months good repayment history, private sale
      transaction of $240,000 -> within the $250k private sale cap
  ineligible:
    - Same customer, private sale transaction of $290,000 -> exceeds the
      $250k private sale cap, even though their repayment history tier
      would otherwise permit up to $300,000 for a DEALER sale
business_logic: |
  IF transaction_type == "private_sale" AND product == "Trucks/Trailers/Wheeled Equipment Streamlined":
    max_transaction_size = MIN(tier_based_limit, $250,000)
  ELSE:
    max_transaction_size = tier_based_limit
keywords:
  - private sale
  - transaction size cap
  - trucks and trailers
synonyms:
  private sale:
    - non-dealer sale
intent_examples:
  - "Is the private sale limit the same as the dealer sale limit for trucks?"
  - "Can I do a $290,000 private sale truck deal with good repayment history?"
decision: Not Eligible above $250,000 for private sales, regardless of the customer's repayment history tier
related_policy:
  - Section 6.2 (Trucks, Trailers & Wheeled Equipment Streamlined Product table)
```

```yaml
exception_id: EX054
title: Demonstrator EV Vehicle Age/Odometer Limit (12 Months / 5,000km)
source_document: Metro — MetroEco Electric Vehicles & Chargers
policy_statement: >
  "Demonstrator electric motor vehicle not more than 12 months old, and
  odometer is not more than 5000km."
interpretation: >
  "Age of Asset: New or Demo" allows demonstrator vehicles under this
  product, but only within a narrow window — the demo vehicle must be
  both under 12 months old AND under 5,000km on the odometer. Both
  conditions must be met simultaneously.
business_rationale: >
  A demonstrator vehicle that is too old or has too many kilometres
  starts to resemble a used vehicle rather than an effectively "new"
  one, undermining the residual value assumptions built into the
  MetroEco New/Demo pricing and terms.
examples:
  eligible:
    - Demo EV, 8 months old, 3,200km on the odometer -> eligible
  ineligible:
    - Demo EV, 10 months old, but 7,000km on the odometer -> not
      eligible (fails the odometer condition even though age is within
      limit)
    - Demo EV, 14 months old, 2,000km on the odometer -> not eligible
      (fails the age condition even though odometer is low)
business_logic: |
  IF vehicle_status == "demonstrator":
    eligible = (age_months <= 12) AND (odometer_km <= 5000)
  ELSE IF vehicle_status == "new":
    eligible = True  # no age/odometer test needed
keywords:
  - demonstrator vehicle
  - demo EV
  - odometer limit
synonyms:
  demonstrator vehicle:
    - demo vehicle
    - dealer demo
intent_examples:
  - "Can I finance a demo EV with 7,000km on it?"
  - "What's the age limit for a demonstrator electric vehicle?"
decision: Not Eligible unless BOTH the 12-month age limit AND the 5,000km odometer limit are satisfied
related_policy:
  - Section 5.1 (MetroEco Electric Vehicles & Chargers)
```

```yaml
exception_id: EX055
title: Consumer EV Channel Gets a Longer Term Than Commercial/Novated (84 vs 60 Months)
source_document: Metro — MetroEco Electric Vehicles & Chargers
policy_statement: >
  Loan Term — Commercial: 60 months (max EOT 5 years); Consumer: 84
  months (max EOT 7 years); Novated: 60 months (max EOT 5 years).
interpretation: >
  Despite sharing the same loan amount cap ($91,387) and the same New/
  Demo eligibility rules, the Consumer channel is uniquely permitted a
  longer maximum term (84 months / 7-year EOT) than both the Commercial
  and Novated channels (60 months / 5-year EOT each).
business_rationale: >
  Consumer (personal, non-business) borrowers are typically financing
  their only/primary vehicle for long-term personal use, which aligns
  with a longer amortisation profile; Commercial deals are priced/termed
  around business asset turnover cycles, and Novated leases are
  typically tied to an employee's employment term, both of which favour
  a shorter, more standard term.
examples:
  eligible:
    - Individual consumer financing a personal EV over 84 months -> eligible
  ineligible:
    - Business financing a Commercial EV over 84 months -> not eligible;
      Commercial channel is capped at 60 months
    - Employee arranging a Novated EV lease over 84 months -> not
      eligible; Novated channel is capped at 60 months
business_logic: |
  IF channel == "Consumer":
    max_term_months = 84  # max EOT 7 years
  ELSE IF channel IN {"Commercial", "Novated"}:
    max_term_months = 60  # max EOT 5 years
keywords:
  - Consumer channel
  - Commercial channel
  - Novated lease
  - loan term
synonyms:
  Consumer channel:
    - personal finance channel
  Novated:
    - novated lease
    - salary packaged vehicle
intent_examples:
  - "Can a business get an 84-month term on a MetroEco EV loan?"
  - "Why is the Consumer EV term longer than Commercial?"
decision: Conditional — 84-month max term only for the Consumer channel; 60 months for Commercial and Novated
related_policy:
  - Section 5.1 (MetroEco Electric Vehicles & Chargers)
```

```yaml
exception_id: EX056
title: Mortgage Statement Substitution for Credit Reference, Capped at $100k (Passenger Vehicle Streamlined)
source_document: Metro — Passenger Vehicle Streamlined Product
policy_statement: >
  "Comparable credit reference on a current or previous asset finance
  (within the last 12 months). 12 months mortgage statements acceptable
  (if no reference available) for amounts up to $100,000."
interpretation: >
  The standard requirement is a comparable ASSET FINANCE credit
  reference. However, if the applicant has no such reference available,
  12 months of mortgage statements can be substituted instead — but only
  as a fallback, and only for loan amounts up to $100,000. Above $100,000,
  this substitution is not available; a genuine asset finance reference
  is required.
business_rationale: >
  A mortgage statement demonstrates repayment discipline but is a weaker
  proxy for asset finance repayment behaviour than an actual asset
  finance track record, so Metro only accepts it as a fallback (not a
  first choice) and only up to a capped amount, limiting the lender's
  reliance on a less-directly-comparable form of evidence for larger
  facilities.
examples:
  eligible:
    - Applicant has no asset finance history, but provides 12 months of
      clean mortgage statements, requesting $85,000 -> acceptable (under
      the $100k cap)
  ineligible:
    - Applicant has no asset finance history, provides mortgage
      statements, but requests $150,000 -> not acceptable; exceeds the
      $100k cap for this substitution, a genuine asset finance reference
      is required instead
    - Applicant has an asset finance reference available but tries to
      submit mortgage statements instead for convenience -> not
      applicable; mortgage statements are only a fallback when NO asset
      finance reference is available, not an alternative of choice
business_logic: |
  IF asset_finance_reference_available == True:
    require(asset_finance_reference)
  ELSE IF asset_finance_reference_available == False AND requested_amount <= $100,000:
    accept(12_months_mortgage_statements)
  ELSE:  # no asset finance reference AND amount > $100,000
    not_eligible_under_streamlined  # requires standard assessment
keywords:
  - mortgage statement
  - asset finance reference
  - credit reference substitution
synonyms:
  mortgage statement:
    - home loan statement
  asset finance credit reference:
    - asset finance reference
    - comparable credit reference
intent_examples:
  - "Can I use my mortgage statements instead of an asset finance reference?"
  - "Is there an amount limit for using mortgage statements as a credit reference?"
  - "Do mortgage statements work for a $150,000 vehicle loan?"
decision: Conditional — Mortgage statements accepted only as a fallback (no asset finance reference available) AND only for amounts ≤$100,000
related_policy:
  - Section 2 (Comparable Credit Reference — Passenger Vehicle variant)
  - Multi-lender Exceptions Catalog, EX032 (Resimac — Credit Reference Requirements Scale by NAF Threshold, same underlying concept at a different lender)
```

```yaml
exception_id: EX057
title: Metro Allows Private Sale Where Other Lenders Restrict to Dealer Only
source_document: Metro — Passenger Vehicle / Trucks, Trailers & Wheeled Equipment / Replacement Policy Streamlined Products (cross-lender comparison)
policy_statement: >
  Metro's Streamlined Products repeatedly state "Dealer and Private Sale"
  as an accepted supplier type for the borrower/guarantor-owned and
  spouse-owned property tiers — in contrast to other lenders in this
  catalog that restrict certain products to dealer/recognised-supplier
  sales only (e.g. CFAL's Other Equipment policy requires "recognized
  supplier, no private sale"; Resimac restricts Sale and Buyback to
  dealership purchases only).
interpretation: >
  Private sale is a routinely accepted supplier channel across most
  Metro Streamlined Products (Passenger Vehicle, Trucks/Trailers/Wheeled
  Equipment, Replacement Policy), subject only to product-specific caps
  (see EX053) — it is NOT a special exception requiring extra
  justification the way it is treated at some other lenders. The one
  place Metro itself restricts to dealer-only is the Non-Property-Backed
  tier (EX043) and the Other Equipment / Agri Streamlined Products
  ("must be from recognised supplier, no private sale").
business_rationale: >
  This reflects a genuine difference in risk appetite/product design
  between lenders rather than an error to reconcile: Metro is willing to
  accept private-sale provenance for property-backed vehicle and
  wheeled-equipment deals (compensating via lower transaction caps
  instead — EX053), whereas other lenders in this catalog either exclude
  private sale entirely for certain asset classes or require heavier
  additional fees/loadings (e.g. Resimac's introducer documentation fee
  variance for private sale, or Westpac's private sale scope restriction
  to Category A assets only).
examples:
  eligible:
    - Property-backed applicant financing a privately-sourced passenger
      vehicle through Metro's Passenger Vehicle Streamlined Product ->
      accepted (no dealer requirement for this tier)
  ineligible:
    - Same private-sale scenario submitted under Metro's Other Equipment
      or Agri Streamlined Product -> not accepted; those specific
      products require a recognised supplier (no private sale), unlike
      the vehicle-focused Streamlined products
    - Same private-sale scenario submitted to a lender/product that
      restricts private sale entirely (e.g. Resimac Sale and Buyback,
      or Westpac's private sale scope limited to Category A only) ->
      treatment differs by lender; always check the specific lender's
      rule rather than assuming Metro's private-sale-friendly approach
      applies elsewhere
business_logic: |
  IF lender == "Metro" AND product IN {"Passenger Vehicle Streamlined",
                                         "Trucks/Trailers/Wheeled Equipment Streamlined",
                                         "Replacement Policy Streamlined"}
     AND property_ownership_tier IN {"borrower/guarantor", "spouse"}:
    private_sale_accepted = True  # subject to product-specific transaction caps, see EX053
  ELSE IF lender == "Metro" AND product IN {"Other Equipment Streamlined", "Agri Streamlined"}:
    private_sale_accepted = False  # recognised supplier only
  ELSE IF lender == "Metro" AND property_ownership_tier == "non-property-backed":
    private_sale_accepted = False  # dealer sale only, see EX043
  # For other lenders, consult their specific policy (e.g. Resimac EX024, Westpac EX002)
keywords:
  - private sale
  - dealer only
  - recognised supplier
  - cross-lender comparison
synonyms:
  private sale:
    - non-dealer sale
    - individual seller sale
  dealer only:
    - recognised supplier only
    - licensed dealer requirement
intent_examples:
  - "Does Metro require a dealer for private sale vehicle finance?"
  - "Why does one lender allow private sale but another requires a dealer?"
  - "Is private sale accepted for Metro's Other Equipment policy?"
decision: >
  Conditional — Metro accepts private sale for Passenger Vehicle,
  Trucks/Trailers/Wheeled Equipment, and Replacement Policy (borrower/
  guarantor and spouse tiers only), subject to transaction caps (EX053);
  Metro excludes private sale for Other Equipment, Agri, and the
  Non-Property-Backed tier (EX043); other lenders in this catalog vary —
  always confirm the specific product and lender.
related_policy:
  - EX043 (Non-Property-Backed Motor Vehicles Require 30% Deposit + Dealer Sale Only)
  - EX053 (Private Sale Transaction Size Cap for Trucks/Trailers/Wheeled Equipment)
  - Section 9 (Cross-Lender Comparison Notes)
  - Multi-lender Exceptions Catalog, EX002 (Westpac — Private Sale Eligibility Scope Restriction)
  - Multi-lender Exceptions Catalog, EX024 (Resimac — Sale and Buyback Restricted to Dealership)
```

```yaml
exception_id: EX058
title: Other Equipment Streamlined Requires Recognised Supplier — No Private Sale
source_document: Metro — Other Equipment Streamlined Product
policy_statement: >
  "Must be from recognized supplier (no private sale or sale/hire back)."
interpretation: >
  Unlike the vehicle-focused Streamlined Products (Passenger Vehicle,
  Trucks/Trailers/Wheeled Equipment, Replacement Policy), which accept
  private sale (see EX057), the Other Equipment Streamlined Product
  requires the asset to come from a recognised supplier. Private sale is
  not an accepted channel for this product under any circumstances —
  this is the single largest structural difference between Other
  Equipment and the vehicle Streamlined products.
business_rationale: >
  "Other Equipment" spans a very broad, non-standardised range of
  tools/machinery with no dealer-network equivalent to the used-vehicle
  market. A recognised-supplier requirement is the main verification
  mechanism available to confirm genuine invoice pricing and legitimate
  ownership, since there is no VIN-style registry or dealer accreditation
  system as consistent as the motor vehicle industry's.
examples:
  eligible:
    - CNC machine purchased from a recognised industrial equipment
      supplier -> eligible
  ineligible:
    - Same CNC machine purchased from a private individual seller -> not
      eligible under Other Equipment Streamlined, regardless of price or
      applicant's tier
business_logic: |
  IF product == "Other Equipment Streamlined" AND supplier_type == "private_sale":
    not_eligible = True  # hard exclusion, no exceptions
keywords:
  - recognised supplier
  - no private sale
  - Other Equipment
synonyms:
  recognised supplier:
    - approved supplier
    - verified supplier
intent_examples:
  - "Can I buy workshop equipment privately under Other Equipment Streamlined?"
  - "Is private sale ever accepted for Other Equipment?"
decision: Not Eligible — private sale is excluded entirely for Other Equipment Streamlined, no exceptions
related_policy:
  - EX057 (Metro Allows Private Sale Where Other Lenders Restrict to Dealer Only — cross-reference for contrast with vehicle products)
  - Section 6.5 (Other Equipment Streamlined Product)
```

```yaml
exception_id: EX059
title: Other Equipment Streamlined Prohibits Sale & Hire Back
source_document: Metro — Other Equipment Streamlined Product
policy_statement: >
  "Must be from recognized supplier (no private sale or sale/hire
  back)."
interpretation: >
  In addition to excluding private sale (EX058), the Other Equipment
  Streamlined Product also prohibits sale-and-hireback transactions
  outright — there is no loading or workaround; it is a flat exclusion,
  unlike the main Commercial Asset Finance rate card, which prices
  sale/hireback via a 0.75% loading rather than banning it (see Section
  3, Sale/Hire Back Loading).
business_rationale: >
  Sale and hireback on unverified, non-standardised equipment carries
  compounded risk (valuation risk from Other Equipment's broad asset
  range, plus the cash-out/inflated-valuation risk inherent to sale and
  hireback structures), so Metro removes it entirely from this
  particular fast-track product rather than pricing it in.
examples:
  eligible:
    - New equipment purchase from a recognised supplier, standard
      finance (not sale/hireback) -> eligible
  ineligible:
    - Business already owns a piece of equipment and wants to sell it to
      Metro and hire it back -> not eligible under Other Equipment
      Streamlined under any circumstances
business_logic: |
  IF product == "Other Equipment Streamlined" AND transaction_type == "sale_and_hireback":
    not_eligible = True  # hard exclusion, contrast with the 0.75% loading on the main rate card
keywords:
  - sale and hireback
  - prohibited
  - Other Equipment
synonyms:
  sale and hireback:
    - sale and leaseback
intent_examples:
  - "Can I do a sale and hireback under Other Equipment Streamlined?"
  - "Is there a loading for sale/hireback under this product, like the main rate card?"
decision: Not Eligible — sale/hireback is a hard exclusion for Other Equipment Streamlined (contrast with the 0.75% loading available on the main rate card)
related_policy:
  - Section 3 (Sale / Hire Back Loading — main rate card, for contrast)
  - Section 6.5 (Other Equipment Streamlined Product)
```

```yaml
exception_id: EX060
title: Other Equipment Streamlined Maximum Term 60 Months (Nil Balloon)
source_document: Metro — Other Equipment Streamlined Product
policy_statement: >
  "Maximum term 60 months nil [balloon]."
interpretation: >
  The Other Equipment Streamlined Product caps the loan term at 60
  months with no balloon/residual payment option at all — this is a
  hard structural limit, separate from (and in addition to) the 3-year
  maximum asset age at EOT already noted in EX048.
business_rationale: >
  Given the already-tight 3-year age cap (EX048) and the broad, hard-
  to-value nature of "Other Equipment," Metro further removes balloon
  flexibility to avoid relying on an uncertain residual value for this
  asset category, and caps the term itself at a conservative 60 months.
examples:
  eligible:
    - New workshop equipment financed over 48 months, fully amortised
      (no balloon) -> eligible
  ineligible:
    - Same equipment financed over 72 months -> exceeds the 60-month cap;
      not eligible under Other Equipment Streamlined
    - Same equipment financed over 60 months WITH a 20% balloon payment
      -> not eligible; balloons are not available at all under this
      product ("nil")
business_logic: |
  IF product == "Other Equipment Streamlined":
    require(loan_term_months <= 60)
    require(balloon_payment == 0)  # "nil" — no balloon option
keywords:
  - Other Equipment
  - 60 months
  - nil balloon
synonyms:
  nil balloon:
    - no balloon
    - fully amortised
intent_examples:
  - "Can I get a 72-month term for Other Equipment Streamlined?"
  - "Is a balloon payment available under Other Equipment Streamlined?"
decision: Not Eligible above 60 months, and no balloon/residual option available at all
related_policy:
  - EX048 (Other Equipment Primary Equipment 3-Year Age Cap)
  - Section 6.5 (Other Equipment Streamlined Product)
```

```yaml
exception_id: EX061
title: Agri Streamlined Requires a Genuine Primary Producer (Not Agricultural Investment)
source_document: Metro — Agri Streamlined Product
policy_statement: >
  "Must be genuine primary producer."
interpretation: >
  The applicant must be an actual, operating primary producer (someone
  who genuinely farms/produces agricultural output as their business),
  not merely an investor who owns agricultural land or assets without
  actively operating a farming business.
business_rationale: >
  The favourable Agri Streamlined terms (12-month/24-month exposure
  scaling, comparable credit reference pathway) are designed to support
  working farm operations, not passive agricultural property investment,
  which carries a different risk/return profile and is not the product's
  intended use case.
examples:
  eligible:
    - Applicant actively operates a cropping/livestock farm and applies
      for a tractor -> eligible
  ineligible:
    - Applicant owns farmland purely as a passive investment (e.g.
      leased out to a third-party farmer) and applies for farm equipment
      -> not eligible; does not meet the "genuine primary producer" test
business_logic: |
  IF product == "Agri Streamlined" AND applicant_status != "genuine_primary_producer":
    not_eligible = True
keywords:
  - primary producer
  - agricultural investment
  - genuine farming operation
synonyms:
  primary producer:
    - working farmer
    - farming operator
intent_examples:
  - "Do I qualify for Agri Streamlined if I just own farmland but don't farm it myself?"
  - "What counts as a genuine primary producer?"
decision: Not Eligible for passive agricultural investors — must be an operating primary producer
related_policy:
  - Section 6.6 (Agri Streamlined Product)
```

```yaml
exception_id: EX062
title: Agri Streamlined Minimum Farm Size — 40 Hectares
source_document: Metro — Agri Streamlined Product
policy_statement: >
  "Minimum farm size 40 ha."
interpretation: >
  In addition to being a genuine primary producer (EX061), the
  applicant's farm must be at least 40 hectares in size. A smaller
  operation — even if genuinely farming — does not meet this threshold.
business_rationale: >
  Sets a practical scale threshold to distinguish a genuine commercial
  farming operation from a hobby farm or small-acreage lifestyle
  property, aligning the product with operations large enough to justify
  the equipment being financed.
examples:
  eligible:
    - Genuine primary producer operating a 120-hectare farm -> eligible
  ineligible:
    - Genuine primary producer operating a 15-hectare hobby farm -> not
      eligible; below the 40-hectare minimum
business_logic: |
  IF product == "Agri Streamlined" AND farm_size_hectares < 40:
    not_eligible = True
keywords:
  - farm size
  - 40 hectares
  - hobby farm
synonyms:
  farm size:
    - property size
    - land area
intent_examples:
  - "Is there a minimum farm size for Agri Streamlined?"
  - "Does a 20-hectare hobby farm qualify for Agri Streamlined?"
decision: Not Eligible below 40 hectares, regardless of primary producer status
related_policy:
  - EX061 (Agri Streamlined Requires a Genuine Primary Producer)
  - Section 6.6 (Agri Streamlined Product)
```

```yaml
exception_id: EX063
title: Agri Streamlined Prohibits Sale & Hire Back
source_document: Metro — Agri Streamlined Product
policy_statement: >
  "No sale/hire back."
interpretation: >
  Like Other Equipment Streamlined (EX059), Agri Streamlined excludes
  sale-and-hireback transactions entirely — a flat prohibition, not a
  loading.
business_rationale: >
  Same underlying logic as EX059 — combined valuation uncertainty
  (agricultural equipment resale markets) and cash-out/inflated-
  valuation risk inherent to sale/hireback structures make this
  unsuitable for a fast-track streamlined product.
examples:
  eligible:
    - New tractor purchase (standard finance, not sale/hireback) -> eligible
  ineligible:
    - Farmer already owns a harvester and wants to sell it to Metro and
      hire it back -> not eligible under Agri Streamlined
business_logic: |
  IF product == "Agri Streamlined" AND transaction_type == "sale_and_hireback":
    not_eligible = True
keywords:
  - sale and hireback
  - prohibited
  - Agri Streamlined
synonyms:
  sale and hireback:
    - sale and leaseback
intent_examples:
  - "Can I do a sale and hireback on farm equipment under Agri Streamlined?"
decision: Not Eligible — sale/hireback is a hard exclusion under Agri Streamlined
related_policy:
  - EX059 (Other Equipment Streamlined Prohibits Sale & Hire Back — same pattern, different product)
  - Section 6.6 (Agri Streamlined Product)
```

```yaml
exception_id: EX064
title: Agri Streamlined — Monthly Payments Only (No Quarterly)
source_document: Metro — Agri Streamlined Product
policy_statement: >
  "Monthly payments only."
interpretation: >
  Repayments under Agri Streamlined must be structured monthly. Other
  repayment frequencies sometimes used in agricultural finance
  elsewhere in the industry (e.g. quarterly or seasonal repayment
  structures, common where farm income is seasonal) are NOT available
  under this Streamlined product.
business_rationale: >
  Monthly repayments give Metro more frequent, granular visibility into
  the account's conduct and reduce the risk of a large missed payment
  accumulating over a longer quarterly cycle — a trade-off against the
  seasonal cash flow flexibility that quarterly structures are usually
  designed to provide.
examples:
  eligible:
    - Standard monthly repayment schedule for a new tractor -> eligible
  ineligible:
    - Applicant requests a quarterly repayment structure to align with
      harvest-season cash flow -> not eligible under Agri Streamlined;
      would need to be assessed outside this fast-track product if a
      non-monthly structure is genuinely required
business_logic: |
  IF product == "Agri Streamlined" AND repayment_frequency != "monthly":
    not_eligible = True
keywords:
  - monthly payments
  - quarterly repayment
  - repayment frequency
synonyms:
  monthly payments:
    - monthly repayment schedule
intent_examples:
  - "Can I set up quarterly repayments for a harvester loan?"
  - "Does Agri Streamlined support seasonal repayment structures?"
decision: Not Eligible for quarterly or other non-monthly repayment structures — monthly only
related_policy:
  - Section 6.6 (Agri Streamlined Product)
```

```yaml
exception_id: EX065
title: Agri Streamlined — Goods Must Be Movable (Cannot Be Fixed)
source_document: Metro — Agri Streamlined Product
policy_statement: >
  "Goods are required to be serial numbered and cannot be fixed."
interpretation: >
  Eligible Agri assets must be movable/serial-numbered equipment (e.g.
  tractors, implements) — they cannot be permanently affixed structures.
  This is also why sheds, silos, and yards appear on the Non-Eligible
  Assets list (Section 6.6) — those are fixed structures, not movable
  serialised equipment.
business_rationale: >
  A movable, serial-numbered asset can be repossessed and resold
  independently of the underlying land if the loan defaults. A fixed
  structure is effectively part of the real property and cannot be
  recovered separately, making it unsuitable as security for an asset
  finance (as opposed to a property/construction finance) product.
examples:
  eligible:
    - Tractor, harvester, or self-propelled sprayer (movable, serial
      numbered) -> eligible
  ineligible:
    - Farm shed or grain silo (a fixed structure, not movable) -> not
      eligible under Agri Streamlined, consistent with the Non-Eligible
      Assets list explicitly excluding sheds, silos, and yards
business_logic: |
  IF product == "Agri Streamlined" AND (asset_is_fixed_structure == True OR asset_has_no_serial_number):
    not_eligible = True
keywords:
  - movable equipment
  - fixed structure
  - serial numbered
  - sheds silos yards
synonyms:
  fixed structure:
    - permanent installation
    - built structure
intent_examples:
  - "Can I finance a grain silo under Agri Streamlined?"
  - "Why are sheds excluded from Agri Streamlined?"
decision: Not Eligible for fixed/non-serial-numbered structures (e.g. sheds, silos, yards) — movable serialised equipment only
related_policy:
  - Section 6.6 (Agri Streamlined Product — Non-Eligible Assets list)
```

```yaml
exception_id: EX066
title: Sale/Hire Back Prohibited Under Vehicle-Focused Streamlined Products
source_document: Metro — Passenger Vehicle / Trucks, Trailers & Wheeled Equipment / Replacement Policy Streamlined Products
policy_statement: >
  "Supplier can be a licensed dealer or private sale (no sale/hire
  back)." — repeated identically across the Passenger Vehicle, Trucks/
  Trailers & Wheeled Equipment, and Replacement Policy tables.
interpretation: >
  While these three products accept both dealer and private-sale supply
  channels (see EX057), sale-and-hireback is flatly excluded from all
  three, with no loading-based alternative — the same hard-exclusion
  pattern already documented for Other Equipment (EX059) and Agri
  (EX063), just not previously listed as its own entry for the
  vehicle-focused products.
business_rationale: >
  Same rationale as EX059/EX063 — sale/hireback carries cash-out and
  inflated-valuation risk that Metro is unwilling to accept under any of
  its fast-track Streamlined pathways, reserving sale/hireback pricing
  (via the 0.75% loading) for the main Commercial Asset Finance rate
  card assessment only.
examples:
  eligible:
    - Dealer or private-sale purchase of a passenger vehicle, standard
      finance -> eligible
  ineligible:
    - Applicant already owns the vehicle and wants to sell it to Metro
      and hire it back -> not eligible under any of the three Streamlined
      products listed above
business_logic: |
  IF product IN {"Passenger Vehicle Streamlined", "Trucks/Trailers/Wheeled Equipment Streamlined",
                  "Replacement Policy Streamlined"} AND transaction_type == "sale_and_hireback":
    not_eligible = True  # route to main rate card instead, where a 0.75% loading applies
keywords:
  - sale and hireback
  - prohibited
  - vehicle streamlined
synonyms:
  sale and hireback:
    - sale and leaseback
intent_examples:
  - "Can I do a sale and hireback under the Trucks and Trailers Streamlined Product?"
  - "Is sale/hireback ever allowed under a Metro Streamlined vehicle product?"
decision: Not Eligible — hard exclusion across all three vehicle-focused Streamlined products; use the main rate card instead (0.75% loading applies there)
related_policy:
  - EX059 (Other Equipment Streamlined Prohibits Sale & Hire Back)
  - EX063 (Agri Streamlined Prohibits Sale & Hire Back)
  - Section 3 (Sale / Hire Back Loading — main rate card, for contrast)
```

```yaml
exception_id: EX067
title: No Balloon/Residual at 15-Year EOT (Wheeled/Heavy Equipment Streamlined Products)
source_document: Metro — Trucks, Trailers & Wheeled Equipment / Replacement Policy / Balloon-Residual Refinance Streamlined Products
policy_statement: >
  "No older than 15 years at end of term – no balloons or residuals for
  lends out to 15 years at end of term."
interpretation: >
  Where a deal is structured to run all the way out to the maximum
  15-year EOT limit, no balloon or residual payment is permitted at all
  — the closer a deal pushes to the maximum allowable asset age, the
  less confident Metro is in setting a residual value, so it removes the
  balloon option entirely rather than adjusting the balloon percentage.
business_rationale: >
  A confident residual value estimate becomes unreliable the further out
  the projected EOT age extends; rather than publish a shrinking balloon
  percentage schedule, Metro sets a binary cutoff — balloons are simply
  unavailable once a deal is stretched to the full 15-year limit.
examples:
  eligible:
    - Wheeled equipment financed over a term that reaches 10 years EOT,
      with a balloon payment structured -> eligible (within the range
      where balloons are still permitted)
  ineligible:
    - Wheeled equipment financed over a term that reaches the full
      15-year EOT limit, WITH a balloon payment requested -> not
      eligible; balloon must be removed (fully amortised structure
      required) if the deal is lent out to the 15-year maximum
business_logic: |
  IF projected_asset_age_at_EOT == 15 (i.e. at the maximum allowed):
    require(balloon_payment == 0)  # fully amortised only
  ELSE IF projected_asset_age_at_EOT < 15:
    balloon_payment_may_be_available  # subject to other product criteria
keywords:
  - EOT
  - balloon payment
  - 15 years
  - residual value
synonyms:
  EOT:
    - end of term
    - projected asset age
intent_examples:
  - "Can I have a balloon payment if my equipment loan runs to the full 15-year limit?"
  - "Why can't I get a residual on a long-term wheeled equipment loan?"
decision: Not Eligible for balloon/residual structuring once the deal reaches the 15-year EOT maximum
related_policy:
  - Section 2 (Age of Asset at End of Term — EOT definition)
  - Section 6.2 / 6.3 / 6.4 (Streamlined product tables)
```

```yaml
exception_id: EX068
title: MetroEco EV & Chargers — Dealer Supplier Only
source_document: Metro — MetroEco Electric Vehicles & Chargers
policy_statement: >
  "Supplier: Dealer" (stated identically across the Commercial, Consumer,
  and Novated channels).
interpretation: >
  Unlike several of Metro's mainstream vehicle Streamlined Products,
  which accept private sale (EX057), the MetroEco EV & Chargers product
  requires a dealer supplier across all three channels — private sale
  EVs are not eligible for this dedicated green-finance product.
business_rationale: >
  New/demo EV pricing, warranty status, and charger bundling are more
  reliably verified through a dealer channel; private-sale EVs would
  introduce the same provenance/valuation uncertainty that Metro avoids
  elsewhere by excluding private sale from its most standardised,
  discount-bearing products.
examples:
  eligible:
    - New EV purchased from a licensed EV dealer -> eligible for MetroEco pricing
  ineligible:
    - Privately purchased used EV -> not eligible for MetroEco EV & Chargers;
      would need to be assessed under the standard vehicle rate card
      (private sale loading would apply there instead)
business_logic: |
  IF product == "MetroEco EV & Chargers" AND supplier_type == "private_sale":
    not_eligible = True
keywords:
  - MetroEco
  - electric vehicle
  - dealer only
synonyms:
  dealer only:
    - licensed dealer requirement
intent_examples:
  - "Can I buy a used EV privately and still get the MetroEco rate?"
decision: Not Eligible for private-sale EVs under MetroEco — dealer supply required across all channels
related_policy:
  - Section 5.1 (MetroEco Electric Vehicles & Chargers)
  - EX057 (Metro Allows Private Sale Where Other Lenders Restrict to Dealer Only — contrast)
```

```yaml
exception_id: EX069
title: MetroEco EV & Chargers — New or Demo Only
source_document: Metro — MetroEco Electric Vehicles & Chargers
policy_statement: >
  "Age of Asset: New or Demo*" — with the demo-specific age/odometer
  conditions detailed separately in EX054.
interpretation: >
  MetroEco EV & Chargers financing is restricted to brand-new vehicles or
  demonstrator vehicles meeting the EX054 conditions (≤12 months old,
  ≤5,000km). Used, non-demonstrator EVs of any age are not eligible
  under this product regardless of condition or mileage.
business_rationale: >
  The MetroEco discount and streamlined terms are designed around new-
  vehicle residual value assumptions; a genuinely used EV (beyond demo
  status) falls outside that pricing model and would need standard
  used-vehicle assessment instead.
examples:
  eligible:
    - Brand-new EV from a dealer -> eligible
    - Qualifying demonstrator EV (per EX054 conditions) -> eligible
  ineligible:
    - 2-year-old used EV (not a demonstrator) -> not eligible under
      MetroEco EV & Chargers, regardless of low kilometres
business_logic: |
  IF product == "MetroEco EV & Chargers":
    eligible = (asset_status == "new") OR (asset_status == "demo" AND meets_EX054_conditions)
  ELSE:
    not_eligible = True
keywords:
  - MetroEco
  - new vehicle
  - demonstrator
  - used EV exclusion
synonyms:
  demo:
    - demonstrator vehicle
intent_examples:
  - "Can I finance a 2-year-old used EV under MetroEco?"
decision: Not Eligible for used (non-demo) EVs — new or qualifying demo only
related_policy:
  - EX054 (Demonstrator EV Vehicle Age/Odometer Limit)
  - Section 5.1 (MetroEco Electric Vehicles & Chargers)
```

```yaml
exception_id: EX070
title: MetroEco Approval Validity — 90 Days
source_document: Metro — MetroEco Electric Vehicles & Chargers / MetroEco Solar, Batteries & Chargers
policy_statement: >
  "Approvals valid for 90 days" — stated for both MetroEco EV & Chargers
  and MetroEco Solar/Batteries/Chargers.
interpretation: >
  A MetroEco approval expires if settlement does not occur within 90
  days of approval — the customer/broker must complete the transaction
  within this window or will need to re-apply/re-assess.
business_rationale: >
  Time-limits the validity of an approval to ensure the applicant's
  financial position, the asset's pricing, and MetroEco program terms
  (which may change) remain current and accurate at the point of
  settlement, rather than relying on a stale approval indefinitely.
examples:
  eligible:
    - MetroEco EV approval settled 60 days after approval -> valid,
      within the 90-day window
  ineligible:
    - MetroEco Solar approval where settlement is attempted 120 days
      after approval -> approval has lapsed; reassessment required
business_logic: |
  IF (settlement_date - approval_date) > 90 days:
    approval_expired = True  # reassessment/reapplication required
keywords:
  - MetroEco
  - approval validity
  - 90 days
synonyms:
  approval validity:
    - approval expiry
intent_examples:
  - "How long is a MetroEco approval valid for?"
  - "Does my MetroEco Solar approval expire if I don't settle quickly?"
decision: Not Valid for settlement beyond 90 days from approval — reassessment required
related_policy:
  - Section 5.1 (MetroEco Electric Vehicles & Chargers)
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX071
title: MetroEco Electric Trucks — Dealer Sale Only
source_document: Metro — MetroEco Electric Trucks
policy_statement: >
  "Dealer sale" (listed as a Product Feature).
interpretation: >
  Consistent with the EV & Chargers product (EX068), Electric Trucks
  under MetroEco must be sourced from a dealer — private sale electric
  trucks are not eligible for this product.
business_rationale: >
  Same rationale as EX068 — dealer channels provide more reliable
  provenance/pricing verification for a product carrying a dedicated
  rate discount and streamlined criteria.
examples:
  eligible:
    - New battery electric truck from a dealer -> eligible
  ineligible:
    - Privately purchased battery electric truck -> not eligible under
      MetroEco Electric Trucks
business_logic: |
  IF product == "MetroEco Electric Trucks" AND supplier_type == "private_sale":
    not_eligible = True
keywords:
  - MetroEco
  - electric truck
  - dealer only
synonyms:
  dealer sale:
    - licensed dealer purchase
intent_examples:
  - "Can I buy an electric truck privately and still get the MetroEco discount?"
decision: Not Eligible for private-sale electric trucks — dealer supply required
related_policy:
  - Section 5.2 (MetroEco Electric Trucks)
  - EX045 (MetroEco Electric Trucks Excludes Biofuel or Hybrid)
```

```yaml
exception_id: EX072
title: MetroEco Electric Trucks — Property Owners Only
source_document: Metro — MetroEco Electric Trucks
policy_statement: >
  "Property owners only" (listed as a Product Feature).
interpretation: >
  Unlike the mainstream vehicle Streamlined Products, which offer a
  Non-Property-Backed tier (albeit with a 30% deposit — EX043), MetroEco
  Electric Trucks has NO non-property-backed pathway at all — property
  ownership (by the applicant or guarantor) is mandatory.
business_rationale: >
  Reflects the higher asset value and risk profile of trucks (3.5t GVM+)
  compared with passenger vehicles, combined with the newer/less-proven
  resale market for battery electric trucks specifically — Metro removes
  the weakest security tier entirely for this product rather than
  pricing it via a deposit/loading.
examples:
  eligible:
    - Property-backed applicant (borrower or guarantor owns qualifying
      property) -> eligible
  ineligible:
    - Applicant with no property backing, even offering a 30%+ deposit
      -> not eligible under MetroEco Electric Trucks (contrast with
      EX043, where a deposit is an accepted substitute for standard
      vehicles)
business_logic: |
  IF product == "MetroEco Electric Trucks" AND property_backed == False:
    not_eligible = True  # no deposit-based substitute available, unlike EX043
keywords:
  - MetroEco
  - electric truck
  - property owners only
synonyms:
  property owner:
    - property-backed applicant
intent_examples:
  - "Can I get an electric truck loan without owning property, with a large deposit instead?"
decision: Not Eligible without property backing — no deposit-based alternative exists for this product
related_policy:
  - EX043 (Non-Property-Backed Motor Vehicles — contrast, deposit accepted there)
  - Section 5.2 (MetroEco Electric Trucks)
```

```yaml
exception_id: EX073
title: MetroEco Electric Trucks — Full Financials Required Above $600,000
source_document: Metro — MetroEco Electric Trucks
policy_statement: >
  "$600,000 Maximum Transaction Size with full financials."
interpretation: >
  The streamlined MetroEco Electric Truck criteria (dealer sale, ABN/GST
  2 years, comparable reference, property owner) support transactions up
  to $300,000 (12 months good history) or $250,000 (new customers)
  without full financials. To reach transaction sizes up to $600,000,
  full financial statements are required in addition to the standard
  streamlined criteria.
business_rationale: >
  Larger transaction sizes warrant deeper due diligence beyond the
  streamlined criteria alone, consistent with the general principle
  (seen across all lenders in this catalog) that documentation
  requirements escalate with transaction size.
examples:
  eligible:
    - $450,000 electric truck transaction, full financials provided ->
      eligible (within the $600k cap, with full financials)
  ineligible:
    - $450,000 electric truck transaction WITHOUT full financials, relying
      only on the standard streamlined criteria -> not eligible above the
      $300,000 (12-month history) or $250,000 (new customer) streamlined
      thresholds; full financials are required to access the higher band
    - $650,000 transaction -> exceeds the $600,000 maximum transaction
      size entirely, regardless of financials provided
business_logic: |
  IF product == "MetroEco Electric Trucks":
    IF transaction_size <= (250000 if new_customer else 300000):
      eligible_under_standard_streamlined_criteria = True
    ELSE IF transaction_size <= 600000 AND full_financials_provided == True:
      eligible = True
    ELSE:
      not_eligible = True  # exceeds $600k cap, or missing required financials
keywords:
  - full financials
  - $600,000
  - transaction size
synonyms:
  full financials:
    - full financial statements
intent_examples:
  - "Do I need full financials for a $450,000 electric truck loan?"
  - "What is the absolute maximum electric truck transaction size?"
decision: Conditional — Full financials required for transactions between the streamlined threshold and $600,000; not eligible at all above $600,000
related_policy:
  - Section 5.2 (MetroEco Electric Trucks)
```

```yaml
exception_id: EX074
title: MetroEco Solar vs Battery — Differentiated Maximum Term (84 vs 60 Months)
source_document: Metro — MetroEco Solar, Batteries & Chargers
policy_statement: >
  "Max loan term: 84 months (fully amortized) batteries on their own—max
  term 60 months."
interpretation: >
  Solar installations can be financed over a term of up to 84 months
  (7 years), but if a battery is financed ON ITS OWN (not bundled with a
  solar installation), the maximum term drops to 60 months (5 years).
business_rationale: >
  Solar panel systems generally have a longer useful/warranted life than
  standalone batteries, which degrade faster and have a shorter
  practical service life — Metro aligns the maximum term with the
  asset's realistic useful life, similar in spirit to the EOT concept
  used elsewhere.
examples:
  eligible:
    - Solar panel installation financed over 84 months -> eligible
    - Standalone battery (no solar bundled) financed over 60 months -> eligible
  ineligible:
    - Standalone battery financed over 84 months -> not eligible; battery-
      only deals are capped at 60 months regardless of the 84-month solar
      allowance
business_logic: |
  IF asset_bundle == "solar" (with or without battery/charger):
    max_term_months = 84
  ELSE IF asset_bundle == "battery_only":
    max_term_months = 60
keywords:
  - solar
  - battery
  - maximum term
synonyms:
  battery only:
    - standalone battery
intent_examples:
  - "Can I get an 84-month term for a battery with no solar panels?"
  - "Why is the battery-only term shorter than the solar term?"
decision: Conditional — 84 months for solar; 60 months maximum if battery is financed standalone
related_policy:
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX075
title: MetroEco Solar — Mortgage Statement Substitution for Credit Reference (No Stated Cap)
source_document: Metro — MetroEco Solar, Batteries & Chargers
policy_statement: >
  "Credit reference: Comparable reference running at least 12 months
  with satisfactory conduct (loan must be active or paid out within the
  last 6 months) or 12 months mortgage statements."
interpretation: >
  Similar to EX056 (Passenger Vehicle), MetroEco Solar accepts 12 months
  of mortgage statements as an alternative to a comparable asset finance
  reference. However, UNLIKE EX056, the Solar brochure does not state an
  amount cap (e.g. no "$100,000" limit is mentioned) — always confirm
  with Metro whether an implicit cap applies, since the absence of a
  stated limit in the brochure does not necessarily mean there is none in
  practice.
business_rationale: >
  Same underlying logic as EX056 — a mortgage statement is accepted as a
  reasonable proxy for repayment discipline when a direct asset finance
  reference isn't available — but the Solar product's documentation does
  not appear to gate this substitution by loan size the way the
  Passenger Vehicle product does.
examples:
  eligible:
    - Applicant has no comparable asset finance reference, but provides
      12 months of clean mortgage statements for a $90,000 solar
      installation -> acceptable per the stated criteria
  ineligible (needs confirmation):
    - Applicant attempts to use mortgage statements for a $400,000 solar
      installation -> the brochure does not explicitly cap this, but
      given EX056's precedent at a different product, confirm with Metro
      before assuming this is unrestricted at high amounts
business_logic: |
  IF product == "MetroEco Solar" AND asset_finance_reference_available == False:
    accept(12_months_mortgage_statements)  # no stated cap in the source brochure — confirm operationally
keywords:
  - mortgage statement
  - solar credit reference
  - no stated cap
synonyms:
  mortgage statement:
    - home loan statement
intent_examples:
  - "Can I use mortgage statements for a large solar installation loan?"
  - "Is there a cap on using mortgage statements for MetroEco Solar, like there is for vehicles?"
decision: Conditional — Mortgage statements accepted as a fallback; no explicit cap stated in this product's documentation (contrast with EX056's $100k cap for Passenger Vehicle) — confirm with Metro before relying on this for large amounts
related_policy:
  - EX056 (Mortgage Statement Substitution — Passenger Vehicle, capped at $100k, for contrast)
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX076
title: MetroEco Solar — Verified Supplier Only
source_document: Metro — MetroEco Solar, Batteries & Chargers
policy_statement: >
  "Supplier: Verified supplier."
interpretation: >
  The solar/battery/charger supplier must be a "verified supplier" —
  this is distinct from (and in addition to) the separate installer/
  product accreditation requirements (NETCC, SAA, CEC — see EX080).
business_rationale: >
  Ensures the commercial entity selling the equipment (as opposed to the
  installer physically fitting it) meets Metro's own verification
  standards, adding a supplier-level check on top of the
  installer/product-level accreditations.
examples:
  eligible:
    - Solar system purchased from a Metro-verified supplier, installed by
      an SAA-accredited installer -> eligible (both checks satisfied)
  ineligible:
    - Solar system purchased from a non-verified/unknown supplier, even
      if installed by an SAA-accredited installer -> not eligible;
      supplier verification is a separate, additional requirement
business_logic: |
  IF product == "MetroEco Solar" AND supplier_verified == False:
    not_eligible = True  # separate check from installer/product accreditation (EX080)
keywords:
  - verified supplier
  - solar supplier
synonyms:
  verified supplier:
    - approved supplier
intent_examples:
  - "Does the solar supplier need separate verification from the installer?"
decision: Not Eligible if the supplier is not verified, independent of installer/product accreditation
related_policy:
  - EX080 (Triple Supplier/Installer/Product Accreditation Required)
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX077
title: MetroEco Solar — Owner-Occupied Property Requires a Business Use Letter
source_document: Metro — MetroEco Solar, Batteries & Chargers (Solar Upfront Requirements)
policy_statement: >
  "Considered on owner occupied property with a business use letter."
interpretation: >
  An owner-occupied property (as opposed to a dedicated commercial
  premises) can still be used to satisfy the property-ownership
  requirement, but only if accompanied by a business use letter
  confirming the property is used for business purposes.
business_rationale: >
  Since this is a COMMERCIAL asset finance product, Metro needs evidence
  that the property/installation genuinely relates to business use, even
  when the property is technically the applicant's residence, to keep
  the facility within the intended commercial-use scope.
examples:
  eligible:
    - Owner-occupied home with a home-based business, business use letter
      provided -> eligible
  ineligible:
    - Owner-occupied home with no business use letter provided -> not
      eligible; the letter is a mandatory supporting document for this
      property type
business_logic: |
  IF property_type == "owner_occupied":
    require(business_use_letter_provided == True)
keywords:
  - owner occupied
  - business use letter
synonyms:
  business use letter:
    - business use declaration
intent_examples:
  - "Can I use my home as the solar installation site if I run a business from it?"
decision: Conditional — Eligible only with a business use letter for owner-occupied property
related_policy:
  - EX046 (MetroEco Solar Leasehold Properties Never Considered)
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX078
title: MetroEco Solar — Investment Property Requires a Current Lease Agreement
source_document: Metro — MetroEco Solar, Batteries & Chargers (Solar Upfront Requirements)
policy_statement: >
  "Considered on residential investment property with copy of the
  current lease agreement confirming the property is tenanted."
interpretation: >
  A residential investment property can also satisfy the property
  requirement, but only with a copy of the current lease agreement
  proving the property is actually tenanted at the time of application.
business_rationale: >
  Confirms the property is a genuine, actively-used investment (not
  vacant or in an ambiguous ownership/use state), supporting the
  underlying property-backing assumption behind the facility.
examples:
  eligible:
    - Investment property with a current, valid lease agreement provided,
      confirming an active tenancy -> eligible
  ineligible:
    - Investment property with no current lease agreement, or a lapsed/
      expired lease -> not eligible; the tenancy must be confirmed as
      current
business_logic: |
  IF property_type == "residential_investment":
    require(current_lease_agreement_provided == True)
keywords:
  - investment property
  - lease agreement
  - tenanted
synonyms:
  investment property:
    - rental property
intent_examples:
  - "Can I use a rental property I own as the solar installation site?"
decision: Conditional — Eligible only with a copy of the current lease agreement confirming tenancy
related_policy:
  - EX046 (MetroEco Solar Leasehold Properties Never Considered)
  - EX077 (Owner-Occupied Property Requires Business Use Letter)
```

```yaml
exception_id: EX079
title: MetroEco Solar — Minimum 50% Ownership Requirement
source_document: Metro — MetroEco Solar, Batteries & Chargers (Solar Upfront Requirements)
policy_statement: >
  "The applicant or guarantor must hold at least 50% ownership."
interpretation: >
  Whichever property-ownership pathway is used (owner-occupied or
  investment property), the applicant or guarantor must hold at least
  50% ownership of that property — a minority stake below 50% does not
  qualify.
business_rationale: >
  A sub-50% ownership stake gives the applicant/guarantor insufficient
  legal control/equity in the property to reliably support the facility
  as security, so Metro sets a majority-ownership floor.
examples:
  eligible:
    - Applicant holds 60% ownership of the property (co-owned with a
      family member) -> eligible
  ineligible:
    - Applicant holds only 30% ownership of the property -> not eligible;
      below the 50% minimum
business_logic: |
  IF ownership_pct(applicant_or_guarantor) < 50%:
    not_eligible = True
keywords:
  - ownership percentage
  - 50% minimum
  - co-owned property
synonyms:
  ownership:
    - equity stake
intent_examples:
  - "Do I qualify if I only own 30% of the property with my sibling?"
decision: Not Eligible below 50% ownership
related_policy:
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX080
title: MetroEco Solar — Triple Supplier/Installer/Product Accreditation Required
source_document: Metro — MetroEco Solar, Batteries & Chargers (Solar Upfront Requirements)
policy_statement: >
  "NETCC accredited seller; SAA accredited installer; The asset must be
  listed under the register of CEC approved products."
interpretation: >
  Three SEPARATE accreditation checks must all be satisfied
  simultaneously: the seller must be NETCC-accredited, the installer must
  be SAA-accredited, and the specific product/asset must appear on the
  Clean Energy Council (CEC) approved products register. All three,
  not just one or two, are required.
business_rationale: >
  Each accreditation covers a different part of the transaction chain
  (who sold it, who installed it, what the product itself is), and
  Australian solar/STC regulatory compliance depends on all three being
  correctly certified — a gap in any one undermines the legitimacy and
  recoverability of the installation as security.
examples:
  eligible:
    - NETCC-accredited seller + SAA-accredited installer + CEC-approved
      panel/inverter model -> eligible (all three satisfied)
  ineligible:
    - NETCC-accredited seller and CEC-approved product, but a
      non-SAA-accredited installer -> not eligible; all three checks are
      required, not just two
business_logic: |
  eligible = (seller_is_NETCC_accredited == True)
             AND (installer_is_SAA_accredited == True)
             AND (product_is_CEC_approved == True)
keywords:
  - NETCC
  - SAA
  - CEC approved
  - solar accreditation
synonyms:
  CEC approved:
    - Clean Energy Council approved
intent_examples:
  - "Do I need all three accreditations, or just one, for solar finance?"
  - "What happens if my installer isn't SAA accredited?"
decision: Not Eligible unless all three accreditation checks (NETCC seller, SAA installer, CEC-approved product) are satisfied
related_policy:
  - EX076 (MetroEco Solar Verified Supplier Only)
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX081
title: MetroEco Solar — Maximum Purchase Price $500,000
source_document: Metro — MetroEco Solar, Batteries & Chargers (Other Conditions)
policy_statement: >
  "Maximum purchase price $500k."
interpretation: >
  The solar/battery/charger installation's total purchase price cannot
  exceed $500,000 — this is a hard cap on the transaction itself,
  separate from the maximum exposure limit (EX082).
business_rationale: >
  Caps the size of any single solar installation Metro will finance under
  this product, keeping individual transaction risk within a defined
  ceiling.
examples:
  eligible:
    - $350,000 solar installation -> eligible
  ineligible:
    - $600,000 solar installation -> exceeds the $500,000 maximum
      purchase price; not eligible under this product
business_logic: |
  IF product == "MetroEco Solar" AND purchase_price > 500000:
    not_eligible = True
keywords:
  - maximum purchase price
  - $500,000
  - solar cap
synonyms:
  purchase price:
    - installation cost
intent_examples:
  - "Is there a maximum size for a solar installation Metro will finance?"
decision: Not Eligible above $500,000 purchase price
related_policy:
  - EX082 (MetroEco Solar Maximum Exposure $700,000)
```

```yaml
exception_id: EX082
title: MetroEco Solar — Maximum Exposure $700,000
source_document: Metro — MetroEco Solar, Batteries & Chargers (Other Conditions)
policy_statement: >
  "Maximum exposure limit $700k."
interpretation: >
  Total Metro exposure across all of a customer's MetroEco Solar
  facilities combined cannot exceed $700,000 — this is an aggregate
  exposure cap, distinct from the $500,000 per-transaction purchase
  price cap (EX081). A customer could, for example, have two smaller
  solar facilities that together approach this $700k ceiling.
business_rationale: >
  Limits Metro's total aggregate risk to any single customer across
  multiple MetroEco Solar facilities, consistent with the "maximum
  exposure" concept used throughout the Streamlined Products (Section 2).
examples:
  eligible:
    - Customer with one existing $400,000 MetroEco Solar facility applies
      for a further $250,000 facility -> total $650,000, within the $700k
      cap
  ineligible:
    - Same customer applies for a further $150,000 facility on top of the
      above -> total would reach $800,000, exceeding the $700k cap; not
      eligible
business_logic: |
  total_exposure = SUM(all existing MetroEco Solar facility balances) + new_facility_amount
  IF total_exposure > 700000:
    not_eligible = True
keywords:
  - maximum exposure
  - $700,000
  - aggregate solar exposure
synonyms:
  exposure:
    - aggregate facility balance
intent_examples:
  - "What is the total exposure limit across multiple solar facilities?"
decision: Not Eligible if the customer's total MetroEco Solar exposure would exceed $700,000
related_policy:
  - EX081 (MetroEco Solar Maximum Purchase Price $500,000)
```

```yaml
exception_id: EX083
title: MetroEco Solar — STC Assignment Form with Photos Required at Settlement
source_document: Metro — MetroEco Solar, Batteries & Chargers (Other Conditions)
policy_statement: >
  "STC assignment form with photos required prior to settlement."
interpretation: >
  Before settlement can occur, the applicant must provide a completed STC
  (Small-scale Technology Certificate) assignment form, together with
  photos — this is a mandatory settlement-condition document, not
  optional or something that can be provided after settlement.
business_rationale: >
  STCs are a government rebate mechanism for solar installations, and the
  assignment form (with photographic evidence of the completed
  installation) confirms the installation is genuinely complete and
  eligible for the rebate — protecting both the customer's rebate
  entitlement and Metro's confirmation that the asset has actually been
  installed as described before releasing funds.
examples:
  eligible:
    - Completed STC assignment form with installation photos submitted
      before settlement -> settlement can proceed
  ineligible:
    - Settlement requested without the STC assignment form or photos ->
      not eligible; settlement cannot proceed until this document is
      provided
business_logic: |
  IF product == "MetroEco Solar":
    require(STC_assignment_form_with_photos_provided == True) # before settlement
keywords:
  - STC
  - Small-scale Technology Certificate
  - settlement condition
synonyms:
  STC:
    - Small-scale Technology Certificate
intent_examples:
  - "What documents are needed before a solar loan can settle?"
  - "Can settlement happen before the STC form is submitted?"
decision: Not Eligible for settlement without the STC assignment form and photos
related_policy:
  - Section 5.3 (MetroEco Solar, Batteries & Chargers)
```

```yaml
exception_id: EX116
title: MetroEco 1% Rate Discount Applies Across All Qualifying Green Products
source_document: Metro — Commercial Asset Finance rate card (MetroEco box) / MetroEco Electric Trucks / MetroEco Solar
policy_statement: >
  ">1% discount applies for new electric vehicles up to $91,661. >1%
  discount applies for eligible wheeled equipment. >1% discount applies
  for batteries, chargers and solar (wheeled equipment rate +2%
  loading)." Also stated separately for Electric Trucks: "1% MetroEco
  rate discount applies."
interpretation: >
  A 1% rate discount is not a single product-specific feature — it is a
  consistent MetroEco-wide benefit applied across every qualifying green
  asset category: new EVs (up to the $91,661 cap), electric trucks,
  eligible wheeled equipment, and batteries/chargers/solar. The one
  variant is that eligible "wheeled equipment" under MetroEco is priced
  off the Wheeled Plant & Equipment rate PLUS a 2% loading before the 1%
  MetroEco discount is applied — i.e. the discount does not fully offset
  the wheeled-equipment loading.
business_rationale: >
  Provides a consistent, predictable green-finance incentive across
  Metro's entire eco product range, while still pricing in the higher
  underlying risk of "other" wheeled equipment (the +2% loading) even
  when that equipment happens to qualify for the MetroEco discount.
examples:
  eligible:
    - New EV priced at $85,000 -> 1% discount applies to the standard EV rate
    - Eligible wheeled equipment under MetroEco -> priced at Wheeled
      Plant & Equipment rate + 2% loading, THEN the 1% MetroEco discount
      is applied on top of that loaded rate (net effect: still higher
      than the standard Wheeled Plant & Equipment rate, just partially
      offset)
  ineligible:
    - Non-qualifying (e.g. hybrid/biofuel) vehicle or equipment -> no
      MetroEco discount applies at all; standard rate card applies instead
business_logic: |
  IF asset IN {"new EV (<=$91,661)", "electric truck", "eligible wheeled equipment", "battery", "charger", "solar"}:
    IF asset_category == "wheeled_equipment":
      applicable_rate = wheeled_plant_equipment_base_rate + 2% - 1%  # net +1% vs standard wheeled equipment rate
    ELSE:
      applicable_rate = product_specific_rate - 1%
  ELSE:
    no_metroeco_discount_applies
keywords:
  - MetroEco
  - 1% discount
  - green finance
synonyms:
  MetroEco discount:
    - green rate discount
    - eco discount
intent_examples:
  - "Does the MetroEco discount apply to wheeled equipment the same way as EVs?"
  - "Is the 1% discount enough to offset the wheeled equipment loading?"
decision: Conditional — 1% discount applies across all qualifying MetroEco assets, but wheeled equipment nets to a net +1% versus the standard rate (2% loading minus 1% discount), not a true discount
related_policy:
  - Section 1 (Commercial Asset Finance rate card — MetroEco box)
  - Section 5.2 (MetroEco Electric Trucks)
  - EX045 (MetroEco Electric Trucks Excludes Biofuel or Hybrid)
```

```yaml
exception_id: EX117
title: MetroEco EV & Chargers Eligibility Implicitly Excludes Hybrid and Biofuel Vehicles
source_document: Metro — MetroEco Electric Vehicles & Chargers (Eligibility)
policy_statement: >
  "Electric Vehicle, where the vehicle is solely powered by electricity
  and uses an external electrical plug to charge the battery."
interpretation: >
  Unlike MetroEco Electric Trucks, which states its hybrid/biofuel
  exclusion explicitly (EX045: "*Excludes biofuel powered or hybrid"),
  the EV & Chargers product does not use the word "excludes" — instead,
  the exclusion is IMPLICIT in the eligibility definition itself: a
  vehicle must be "solely" powered by electricity via an external plug.
  A hybrid (which also has a combustion engine) or a biofuel vehicle by
  definition fails this "solely powered by electricity" test, so both
  are excluded, just via a positive-definition mechanism rather than a
  named exclusion.
business_rationale: >
  Same underlying rationale as EX045 (targeting the MetroEco discount at
  genuinely zero-tailpipe-emission vehicles), but expressed through the
  eligibility criterion's wording rather than a standalone exclusion
  clause — worth flagging separately because a keyword search for
  "excludes hybrid" would miss this product's eligibility rule, even
  though the practical effect is identical to Electric Trucks.
examples:
  eligible:
    - Fully battery-electric passenger vehicle, charged via an external
      plug -> meets the "solely powered by electricity" test
  ineligible:
    - Plug-in hybrid vehicle (has both a plug AND a combustion engine) ->
      fails the "solely powered by electricity" test, even though it can
      be charged via an external plug
    - Biofuel-powered vehicle -> fails the "solely powered by
      electricity" test entirely
business_logic: |
  IF product == "MetroEco EV & Chargers":
    eligible = (power_source == "electricity_only") AND (charging_method == "external_plug")
    # a hybrid or biofuel vehicle fails this test even without an explicit "excludes hybrid/biofuel" clause
keywords:
  - electric vehicle
  - hybrid exclusion
  - biofuel exclusion
  - solely powered
synonyms:
  solely powered by electricity:
    - fully electric
    - battery electric only
intent_examples:
  - "Is a plug-in hybrid eligible for MetroEco EV & Chargers?"
  - "Does the EV product exclude hybrids the same way the Electric Truck product does?"
decision: Not Eligible for hybrid or biofuel vehicles — excluded implicitly via the "solely powered by electricity" eligibility test, not a named exclusion clause
related_policy:
  - EX045 (MetroEco Electric Trucks Excludes Biofuel or Hybrid — explicit version of the same exclusion)
  - EX069 (MetroEco EV & Chargers — New or Demo Only)
```

---

*Compiled from the Metro Commercial Asset Finance rate card (20/07/2026) and associated MetroEco/Streamlined
Product brochures. This document is a standalone deep-dive reference intended to sit alongside, and be
cross-referenced with, the Resimac Detailed Reference and the multi-lender Exceptions Catalog (Westpac / CFAL /
Resimac). Verify all figures against Metro's live platform before operational use.*
