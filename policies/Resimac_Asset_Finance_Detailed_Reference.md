# Resimac Asset Finance — Detailed Policy Reference & Glossary

> Source: Resimac Asset Finance — Commercial Product Guide, Auto and Equipment, effective 27 March 2026.
> Purpose: This document expands every term, trigger condition, and mechanic in the Resimac guide into a
> retrieval-friendly reference, separate from the multi-lender Exceptions Catalog. Each glossary entry includes
> `term`, `definition`, `includes`, `trigger_keywords`, and `rationale` so it can be chunked directly for RAG lookup.

---

## 1. Risk Loading Trigger Definitions

These four conditions each add a 2% risk loading (see Section 3 for the mechanics and cap).

```yaml
term: Private Sale
definition: >
  A transaction where the asset is purchased from a private individual or
  business that is not a licensed dealer — i.e. there is no dealership
  invoice, dealer warranty, or dealer accountability behind the sale.
includes:
  - Buying a vehicle/equipment directly from its current private owner
  - Buying via a private online marketplace listing (e.g. Facebook
    Marketplace, Gumtree) where the seller is not a registered dealer
excludes:
  - Any purchase from a licensed dealership (even if the dealer is
    small or independent)
trigger_keywords:
  - private sale
  - private seller
  - non-dealer purchase
  - individual seller
  - person-to-person sale
rationale: >
  Private sales lack a dealer's warranty, standardised invoice pricing,
  and accountability if the asset's condition or ownership is
  misrepresented. Verifying title, roadworthiness, and fair value is
  harder and slower, so the lender prices in a 2% loading to compensate
  for this added uncertainty.
```

```yaml
term: Classic Cars
definition: >
  Vehicles that are collectible/vintage rather than standard daily-use
  commercial vehicles — valued primarily for rarity, provenance, and
  collector demand rather than conventional utility-based depreciation.
includes:
  - Vintage or heritage vehicles sought by collectors
  - Restored or limited-production vehicles with values driven by
    condition/originality rather than mileage/age alone
excludes:
  - Standard passenger vehicles, even if older than average
trigger_keywords:
  - classic car
  - vintage vehicle
  - collector car
  - heritage vehicle
  - restored vehicle
rationale: >
  Classic car values are set by a niche, sentiment-driven collector
  market rather than a standard depreciation curve, making resale value
  volatile and harder to predict confidently. This is also why classic
  cars are excluded from balloon payment options (see Section 2.6) and
  do not benefit from the standard 25-year motor vehicle age-at-term
  allowance in the same predictable way.
```

```yaml
term: Assets Age ≥16 Years EOT (End of Term)
definition: >
  "EOT" = End of Term. This condition is triggered when the asset's age
  AT THE END of the proposed loan term (not its age today) reaches or
  exceeds 16 years. It is a forward-looking calculation:
  current_asset_age + loan_term_years >= 16.
includes:
  - A 10-year-old asset financed over a 6-year term (10 + 6 = 16 -> triggers)
  - A 14-year-old asset financed over a 3-year term (14 + 3 = 17 -> triggers)
excludes:
  - A 5-year-old asset financed over a 5-year term (5 + 5 = 10 -> does not trigger)
trigger_keywords:
  - EOT
  - end of term
  - asset age at term
  - projected asset age
rationale: >
  A lender's real exposure to mechanical/residual-value risk is highest
  near the end of the loan, when the asset is oldest. Pricing off the
  asset's PROJECTED age at maturity (rather than its current age) more
  accurately reflects the risk the lender is carrying for the full term,
  even if the asset seems young today.
```

```yaml
term: Prime Movers
definition: >
  The tractor/head unit of an articulated truck combination — the
  powered unit that pulls one or more semi-trailers (also called a
  truck tractor or road train head unit).
includes:
  - Semi-trailer tractor units
  - Road train head units (single/double/triple trailer configurations)
excludes:
  - The trailers themselves (trailers are a separate Primary asset line item)
  - Rigid trucks that are not designed to pull separate trailers
trigger_keywords:
  - prime mover
  - truck tractor
  - road train head
  - semi truck cab
  - articulated truck head unit
rationale: >
  Prime movers are used at high intensity (long-haul freight), face
  significant wear, and sit in a specialised resale market with a
  narrower buyer pool than passenger/light commercial vehicles. This is
  also why prime movers always require a property-backed guarantor
  (see the Exceptions Catalog, EX026) in addition to this rate loading.
```

---

## 2. Asset Category Definitions

Resimac splits every financeable asset into five categories. Categorisation drives the interest rate, maximum loan amount, maximum asset age at term, and balloon payment eligibility.

```yaml
term: Motor Vehicles
definition: >
  Standard road vehicles used for personal/light business transport,
  priced and depreciated in large, liquid, well-documented resale
  markets.
includes:
  - Passenger vehicles
  - Light trucks
  - Light commercial vehicles (vans, utes)
  - Classic cars (loadings apply — see Section 1)
  - Motorbikes
trigger_keywords:
  - car
  - sedan
  - SUV
  - ute
  - van
  - hatchback
  - motorbike
  - light truck
rationale: >
  High-volume, standardised resale market with abundant comparable
  sales data, giving the lender strong confidence in residual value —
  hence the longest age-at-term allowance (25 years) and full balloon
  eligibility (except classic cars).
```

```yaml
term: Electric Vehicles
definition: >
  Fully electric (battery electric) vehicles, priced as their own rate
  line separate from standard motor vehicles, reflecting a distinct
  (currently favourable) residual value trend.
includes:
  - Fully electric passenger/light commercial vehicles
excludes:
  - Hybrid vehicles (not explicitly listed; treat as standard Motor
    Vehicle unless confirmed otherwise with Resimac)
trigger_keywords:
  - EV
  - electric vehicle
  - battery electric vehicle
  - BEV
rationale: >
  EVs currently show more stable/favourable resale value trends than
  average, and Resimac (like other lenders in this catalog) prices this
  in as a distinct, lower base rate rather than a discount off the Motor
  Vehicle rate.
```

```yaml
term: Primary Assets
definition: >
  Heavy-duty commercial/industrial vehicles and equipment with GVM
  above the light-vehicle threshold, or specialised heavy machinery with
  an established, moderately liquid resale market.
includes:
  - Heavy trucks >4.5T GVM
  - Trailers
  - Buses and coaches
  - Small yellow goods and excavators
  - Construction and earth moving equipment
  - Farming and agriculture equipment
  - Materials handling and access equipment
  - Prime movers (loadings apply — see Section 1)
  - Caravans
trigger_keywords:
  - excavator
  - forklift
  - tractor
  - harvester
  - bus
  - coach
  - heavy truck
  - dump truck
  - trailer
  - caravan
rationale: >
  These assets have an active dealer/auction resale market (heavy
  equipment auctions, truck dealerships), but less liquidity than
  passenger vehicles — hence a slightly higher base rate than Motor
  Vehicles, but still a long 25-year age-at-term allowance and full
  loan-amount-table access.
```

```yaml
term: Secondary Assets
definition: >
  Mid-tier specialised industrial/commercial equipment with a
  narrower, more fragmented resale market than Primary assets —
  typically only valuable to buyers within the same trade/industry.
includes:
  - Generators and compressors
  - Engineering and toolmaking equipment
  - Medical equipment
  - Woodworking and metalworking equipment
  - CNC machines and edge benders
  - Landscaping and groundskeeping equipment (motorised only)
  - Attachments for earthmoving machinery
trigger_keywords:
  - generator
  - compressor
  - CNC machine
  - medical equipment
  - woodworking machine
  - metalworking equipment
  - motorised lawn equipment
  - earthmoving attachment
rationale: >
  Buyer pools for this equipment are industry-specific and thinner than
  for vehicles, and valuation/technology relevance can shift faster.
  This is reflected in: a noticeably higher base rate (12%+ p.a.), a
  shorter maximum age-at-term (10 years vs 25 for Motor/Primary), and
  exclusion from balloon payment structures.
```

```yaml
term: Tertiary Assets
definition: >
  The most specialised, lowest-liquidity asset category — equipment
  with the narrowest resale market, fastest technological obsolescence,
  or industry-specific value that does not transfer well outside its
  original use case.
includes:
  - Audio visual equipment
  - Conveyors
  - Wine and beer industry and processing equipment
  - Skip bins
  - Medical lasers
  - Testing and calibration equipment
  - GPS units (must be detachable)
trigger_keywords:
  - AV equipment
  - conveyor belt
  - brewery equipment
  - winery equipment
  - skip bin
  - medical laser
  - calibration equipment
  - GPS tracker
rationale: >
  These assets have the thinnest resale markets and highest
  obsolescence/specialisation risk, resulting in the highest base rate
  (14%+ p.a.), the shortest age-at-term allowance (5 years), no
  availability at all under Low Doc (see the loan amount table — Low
  Doc column shows "–" for Tertiary), and no balloon payment option.
```

### 2.6 Why Secondary, Tertiary, and Classic Cars Face More Restrictions

All four "more restricted" categories (Secondary, Tertiary, Classic Cars, and to a lesser extent Prime Movers)
share the same underlying driver: **the lender's confidence in predicting residual/resale value at the end of the
loan term.** This confidence is a function of:

| Factor | Motor Vehicles / Primary | Secondary | Tertiary | Classic Cars |
|---|---|---|---|---|
| Resale market depth | Large, standardised, high transaction volume | Niche, industry-specific buyer pool | Very niche, sometimes single-industry buyer pool | Collector-driven, sentiment-based |
| Valuation predictability | High — established depreciation curves, comparable sales data | Moderate — depends on trade demand | Low — technology/industry shifts can devalue quickly | Low — driven by rarity/condition, not standard depreciation |
| Max age at term | 25 years | 10 years | 5 years | Standard Motor Vehicle limit, but with loading |
| Balloon payment available | Yes | No | No | No |
| Base interest rate | Lowest tier | Mid-high tier (12%+) | Highest tier (14%+) | Standard tier + 2% loading |
| Low Doc availability | Yes | Yes | No (Lite/Full Doc only) | Yes (loading still applies) |

In short: **the further an asset category sits from a large, liquid, well-documented resale market, the shorter
the lender is willing to lend against its expected future value, the less willing it is to defer part of the loan
to a balloon payment, and the higher the rate it charges to compensate for that uncertainty.**

---

## 3. Risk Loading Mechanics (Deep Dive)

### 3.1 What Is Risk Loading

Risk loading is a rate add-on applied when a deal carries one or more of the four elevated-risk characteristics in
Section 1. It is separate from, and stacks independently of, the underlying tier/asset-category base rate.

### 3.2 Why the Multiple-Loading Cap Is 4%

Each triggered condition individually adds 2%, but if a deal triggers three or four conditions at once (e.g. a
private sale of a classic prime mover aged 17 years at EOT), the raw sum could reach 6–8%. Resimac caps the
**combined risk loading at 4% per deal** for two main reasons:

1. **Commercial viability** — Beyond a certain point, stacking loadings without limit would price the deal out of
   the market entirely (the customer would simply decline or the repayment burden would become unserviceable),
   causing the lender to lose the deal rather than price it appropriately.
2. **Predictable, quotable pricing** — A hard ceiling means brokers and credit assessors can always quote a
   maximum possible rate for a multi-risk deal upfront, rather than needing case-by-case escalation for
   increasingly rare combinations of risk factors.

### 3.3 Why Brokerage Loading Is Excluded From the 4% Cap

Risk loading and brokerage loading compensate for two **entirely different things**:

- **Risk loading** compensates the lender for **credit/asset risk** — the chance the loan underperforms because of
  the asset's resale uncertainty or the transaction's verification difficulty.
- **Brokerage loading** (see the Exceptions Catalog, EX036) compensates for a **distribution cost** — when a
  broker charges commission above the standard 5.5% threshold, the lender passes a proportional rate increase back
  to the customer to recover that higher acquisition cost.

Because these are independent pricing components serving independent purposes, the 4% cap on risk loading has no
bearing on the (separate) brokerage-driven rate loading — the two can and do stack on top of each other.

### 3.4 Worked Case Example (for retrieval)

```yaml
case_example_id: RISK-LOADING-001
scenario: >
  A customer wants to finance a classic car, purchased from a private
  seller, currently 12 years old, over a 5-year loan term.
step_1_identify_triggers:
  - Private sale -> +2%
  - Classic car -> +2%
  - Asset age at EOT = 12 + 5 = 17 years, which is >= 16 -> +2%
  - (Not a prime mover -> no additional trigger)
step_2_sum_raw_loading: 6%  # (2% + 2% + 2%)
step_3_apply_cap: >
  Raw loading of 6% exceeds the 4% per-deal cap, so the APPLIED risk
  loading is capped at 4%, not 6%.
step_4_base_rate: >
  Assume this falls under "Primary assets >3 years" at Premium tier =
  9.54% p.a. (classic cars are priced within the Motor Vehicle line in
  the published table, but this example illustrates the mechanic; use
  the correct base line for the actual asset category in practice).
step_5_rate_after_risk_loading: 9.54% + 4% = 13.54% p.a.
step_6_brokerage_scenario: >
  The broker separately charges 7% brokerage (1.5% above the 5.5%
  threshold, rounding up to 2 full percentage points of "part
  thereof").
step_7_brokerage_loading: 2 * 0.5% = 1.0%
step_8_final_rate: 13.54% + 1.0% = 14.54% p.a.
key_takeaway: >
  The risk loading cap (4%) and the brokerage loading (1.0% in this
  example) are calculated independently and both apply — the 4% cap
  does NOT limit or absorb the brokerage-driven increase.
```

---

## 4. Application Requirements Explained

### 4.1 What Is "12 Months Running ATO Portals"

```yaml
term: 12 Months Running ATO Portals
definition: >
  A document (typically a PDF export or screenshot series) from the
  Australian Taxation Office's online business portal ("Online services
  for business", accessed via myGovID) showing the applicant's
  Integrated Client Account running balance and lodgement/payment
  history over the trailing 12 months.
what_it_shows:
  - Real-time running balance of tax liabilities (GST, PAYG, income tax)
  - History of lodgements and payments over the period
  - Whether any payment arrangement/debt is currently in place
required_for:
  - Lite Doc and Full Doc applications (NOT required for Low Doc)
trigger_keywords:
  - ATO portal
  - integrated client account
  - running balance export
  - tax portal screenshot
  - Online services for business
why_it_matters: >
  This document is the primary evidence used to verify the Lite Doc ATO
  debt threshold (ATO debt must be <10% of turnover and under an
  established payment arrangement in place >3 months — see the
  Exceptions Catalog, EX029). Without it, the lender cannot confirm the
  applicant meets this threshold.
```

### 4.2 Full Doc Checklist Walkthrough

| Requirement | Low Doc | Lite Doc | Full Doc | What it verifies |
|---|---|---|---|---|
| Application and privacy consent | ✔ | ✔ | ✔ | Basic identity/consent to process the application |
| Asset and liability statement | ✔ | ✔ | ✔ | Applicant/guarantor's personal net worth position |
| 12 months running ATO portals | – | ✔ | ✔ | Tax debt/compliance status (see 4.1) |
| Two most recent BAS portals | – | ✔ | ✔ | Recent turnover figures, used for the 2.5x asset-price turnover test (EX029) |
| 90-day bank statements | – | On request | ✔ | Cash flow / trading activity verification |
| Financial accounts / tax returns | – | – | ✔ | Full financial position for deeper credit assessment |

---

## 5. Fee Schedule Explained

```yaml
fee_name: Monthly Account Keeping Fee
amount: $4.95 per month
when_charged: Ongoing, for the life of the loan
purpose: Covers the administrative cost of maintaining the loan account
trigger_keywords: [account keeping fee, monthly fee, ongoing fee]
```

```yaml
fee_name: Setup Fee
amount: $495 (one-off)
when_charged: At loan establishment/settlement
purpose: Covers the cost of originating and documenting the finance contract
trigger_keywords: [setup fee, establishment fee, origination fee]
```

```yaml
fee_name: Private Sale / Sale and Buyback Fee
amount: $695 (one-off, in addition to the setup fee)
when_charged: Only on private sale or sale-and-buyback transactions
purpose: >
  Covers the additional verification work required for non-dealer
  transactions — ownership/title checks, condition verification, and
  (for sale and buyback) confirming the recent purchase invoice and
  30-day purchase window (see the Exceptions Catalog, EX024).
trigger_keywords: [private sale fee, sale and buyback fee]
```

```yaml
fee_name: PPSR Fee(s)
amount: At cost (variable, pass-through)
when_charged: When registering the lender's security interest on the
  Personal Property Securities Register
purpose: >
  Recovers the actual government registration fee for securing the
  asset against the loan; not a fixed markup, charged at whatever the
  PPSR registration actually costs.
trigger_keywords: [PPSR fee, security registration fee]
```

```yaml
fee_name: Introducer Documentation Fee
amount: Up to $990 (standard) / up to $880 (private sale or sale and buyback)
when_charged: At settlement, payable to the broker/introducer
purpose: >
  Compensates the broker for documentation/administration work;
  capped lower for private sale/buyback deals (see the Exceptions
  Catalog, EX037), likely to avoid stacking excessive total fees on an
  already higher-risk transaction type.
trigger_keywords: [introducer fee, documentation fee, broker fee]
```

```yaml
fee_name: Brokerage (incl. GST)
amount: Standard up to 5.5%; maximum 8.8% (with rate loading above 5.5% — see the Exceptions Catalog, EX036)
when_charged: Built into the finance rate/structure, set by the broker
purpose: Broker commission for originating the deal
trigger_keywords: [brokerage, broker commission]
```

---

## 6. Key Point Guidelines — Full Walkthrough

**General**
- **NAF (Net Amount Financed)** excludes fees and brokerage — it is the "clean" financed principal only.
- Existing property-backed clients with 12 months of perfect repayment history can access a **$400k Low Doc
  aggregate exposure** cap (see Exceptions Catalog, EX025) — this is specifically an existing-customer benefit,
  not available to new clients.
- Privacy consent must be signed **within 90 days** of the application date and must explicitly reference
  "Resimac Asset Finance (resimacassetfinance.com.au)" — an outdated or generic consent form is not valid.
- **Sale and buyback** is restricted to dealership-sourced assets purchased within 30 days, for PremiumPLUS/Premium
  tiers only, case-by-case (see Exceptions Catalog, EX024).
- References may be obtained "where available," at Resimac's sole discretion — not a mandatory document for every
  deal.
- Standard loan terms run 12–60 months; **Green Goods** assets can extend to 84 months (Exceptions Catalog, EX031).
- Insurance is mandatory on every deal; **CoC (Certificate of Currency) proof** is only required above $100k NAF
  (Exceptions Catalog, EX035).
- Applicants with current bankruptcy, or discharged bankruptcy within the last 10 years, are not eligible.

**Asset**
- The asset must be used in the business's normal trading activities (not purely personal/investment use).
- All assets must be serialised, identifiable, and registered prior to settlement where applicable (i.e. must have
  a VIN/serial number that can be checked/registered, similar in spirit to the Westpac VIN-based PPSR rules in the
  Exceptions Catalog, EX010).
- Valuations are done in-house where possible; otherwise an external valuation may be required at the customer's
  cost.
- Luxury assets or motor vehicles will require additional information (unspecified — likely case-by-case).
- Hard per-asset caps: motorbike $75k, passenger vehicle $250k (Exceptions Catalog, EX027).

**Property Backing**
- An applicant is considered property-backed only if: (a) at least 25% of a relevant property resides in a
  guarantor's name, AND (b) equity in that property is at least 1x the NAF, AND (c) there are no multiple or
  adverse encumbrances on the property. All three conditions must hold simultaneously.

**Spouse-Owned Property**
- Does NOT count toward property-backed status, but can be used to waive a deposit requirement — and only for
  legally married couples, not de facto relationships (Exceptions Catalog, EX023).

**Lite Doc**
- ATO debt must be under 10% of turnover, with an established payment arrangement in place for more than 3 months.
- BAS-reported annualised turnover must exceed 2.5x the asset purchase price (Exceptions Catalog, EX029).

**Directors and Shareholders**
- All directors and all shareholders holding >40% must be Australian citizens or permanent residents residing in
  Australia, and must personally guarantee the loan.
- All shareholders holding >25% must complete Resimac's AML (Anti-Money Laundering) procedures.
- Large corporates, clubs, private schools, charities, and associations may be exempted from the personal
  guarantee requirement (Exceptions Catalog, EX030).

**Definitions Table**
- **Equifax scores**: The assessment uses the HIGHEST of the company score or any guarantor score, but any single
  score below 450 can independently trigger a referral or decline (Exceptions Catalog, EX038).
- **Cash flow lenders**: Any enquiry from a cash-flow (short-term working capital) lender within the last 6 months
  may escalate the required documentation level to Lite Doc, or trigger a bank statement sweep review, subject to
  overall profile (Exceptions Catalog, EX033).
- **Credit references**: Requirements scale by NAF size at the $100k threshold, with a "50% of requested NAF"
  coverage rule for Low Doc applications above $100k (Exceptions Catalog, EX032).
- **Active credit file**: Applicants must be an established business with regular, ongoing industry-related credit
  enquiries visible on file — a business with no credit history at all does not meet this bar.
- **Prime movers**: Always require a property-backed guarantor, regardless of tier (Exceptions Catalog, EX026).

---

## 7. Asset Categories — Full Detail with Trigger Keywords

See Section 2 above for the five financeable categories. The following is the **complete exclusion list** — none
of these can be financed under this product regardless of tier, documentation level, or deposit (cross-referenced
in the Exceptions Catalog as EX034):

```yaml
term: Resimac Excluded Asset Categories
definition: >
  A hard negative list — these asset types cannot be financed under
  this Resimac product at all.
includes:
  - Fixtures and fittings
  - Cool rooms and spray booths
  - Intangible assets
  - Refrigeration
  - Gym equipment
  - Hospitality equipment
  - Software
  - Scaffolding, racking and temporary fencing
  - Food trucks
  - Artwork
  - Vending and gaming machines
  - Livestock
  - Ride share, taxis and repairable writeoffs
  - Demountables and shipping containers
  - Racking
  - Office furniture
  - Electric or motor vehicle used for hire/rental purposes
  - IT hardware
trigger_keywords:
  - fixtures and fittings
  - office furniture
  - IT hardware
  - software
  - livestock
  - artwork
  - gaming machine
  - food truck
  - ride share vehicle
  - repairable writeoff
rationale: >
  These items share risk traits that make them unsuitable for this
  product: illiquid/non-standardised resale markets, intangibility or
  difficulty of repossession, regulatory complexity (gaming, livestock),
  or high fraud/valuation risk (artwork, repairable writeoffs).
related_policy:
  - Exceptions Catalog EX034 (Excluded Asset Categories — Resimac)
  - Exceptions Catalog EX006 (Computers, Fixtures & Fittings Excluded — Westpac, for comparison)
```

---

*Compiled from the Resimac Asset Finance Commercial Product Guide (effective 27 March 2026). This document is a
standalone deep-dive reference intended to sit alongside, and be cross-referenced with, the multi-lender
Exceptions Catalog (Westpac / CFAL / Resimac). Verify all figures against Resimac's live platform before
operational use.*
