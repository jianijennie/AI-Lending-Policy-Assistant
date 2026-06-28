# Lender Policy Knowledge Base — v2 (Query-Intent Driven)
> Structure: Query Intent → Topic Chunk (cross-lender) + Lender as metadata filter
> Lenders covered: Resimac | BFS | Westpac WEF | CFAL
> Last updated: 2026-06-27
> Version: 2.0 — optimised for borrower-facing RAG retrieval

---

## CHUNK SCHEMA
```
chunk_id       : {intent}_{subtopic}
intent         : eligibility | pricing | loan_limits | documentation |
                 asset_eligibility | exclusions | settlement | special_programs
subtopic       : describes the specific scenario or question this chunk answers
lenders        : which lenders this chunk covers
trigger_words  : sample borrower questions that should retrieve this chunk
content        : cross-lender answer, structured for comparison
```

---
---

# INTENT 1 — ELIGIBILITY
> "Can I get approved?" — covers ABN duration, credit score, property, residency, business type

---

## chunk_id: eligibility_abn_gst_duration
**intent:** eligibility
**subtopic:** Minimum ABN and GST registration duration by lender
**lenders:** Resimac, BFS, Westpac WEF, CFAL
**trigger_words:** "how long do I need my ABN", "new business ABN", "just registered ABN", "ABN less than 2 years", "GST registered recently", "how long in business"

**Content:**

A borrower's ABN and GST registration duration is one of the primary eligibility gates. Here is what each lender requires:

| Lender | Minimum ABN | Minimum GST | Notes |
|--------|------------|------------|-------|
| Resimac PremiumPLUS | > 6 years | > 3 years | Highest tier; lowest rates |
| Resimac Premium | > 4 years | > 2 years | Property-backed only |
| Resimac Standard | > 2 years | > 1 year | Accepts renters |
| Resimac Basic | > 1 year | > 1 year | Widest property type acceptance |
| BFS (Low Doc commercial) | 2+ years (ABN + GST) | — | Max loan $150k |
| BFS (Full Doc commercial) | 12+ months ABN | — | Max loan $250k standard |
| BFS (New Business Ventures) | < 12 months ABN | — | Max loan $100k; Ultra Prime–Tier 4 only |
| Westpac WEF (all channels) | > 2 years | Currently registered | Verbal confirmation accepted if financials not obtained |
| CFAL | ≥ 2 years | Currently registered | All transaction sizes |

**Key takeaway for borrowers:**
- Under 12 months ABN: only BFS New Business Ventures is available (max $100k)
- 12 months–2 years: BFS Full Doc and limited Westpac (new-to-bank with property)
- Over 2 years: all lenders accessible, with tier/rate varying by other factors

---

## chunk_id: eligibility_credit_score
**intent:** eligibility
**subtopic:** Minimum credit score requirements by lender and tier
**lenders:** Resimac, BFS
**trigger_words:** "credit score", "Equifax score", "Experian score", "bad credit", "low credit score", "credit history", "CCR score", "what score do I need"

**Content:**

Credit score requirements differ significantly between lenders. Only Resimac (Equifax) and BFS (Experian CCR) publish explicit score thresholds. Westpac and CFAL use "satisfactory credit bureau" as a qualitative standard.

**Resimac — Equifax scores:**

| Doc Type | Sole Trader | Company / Guarantor | Lower threshold |
|---------|------------|-------------------|----------------|
| Low Doc | ≥ 650 | ≥ 600 | Score < 450: referral or decline |
| Lite Doc | ≥ 600 | ≥ 550 | Score < 450: referral or decline |
| Full Doc | ≥ 600 | ≥ 550 | Score < 450: referral or decline |

Assessment uses the **highest** score among the company or any guarantor.

**BFS — Experian CCR scores:**

| Tier | Minimum Score | Additional conditions |
|------|--------------|----------------------|
| Ultra Prime | 960 | — |
| Tier 1 | 800 | — |
| Tier 2 | 600 | — |
| Tier 3 | 550 | + 20% deposit required |
| Tier 4 | 400 | + 20% deposit required |
| BFS Plus | 400 (consumer) / 550 (commercial used) | Passenger & light commercial only |

**BFS auto-decline (no resubmission):**
- All individuals and guarantors < 400 (consumer + commercial new/demo)
- All individuals and guarantors < 550 (commercial used)

**Westpac WEF & CFAL:** No published score threshold. Require "satisfactory credit bureau and ASIC search". Applications with adverse history are assessed at credit discretion.

**Key takeaway for borrowers:**
- Score ≥ 960: access to all lenders at best rates (BFS Ultra Prime)
- Score 600–799: BFS Tier 1–2, Resimac PremiumPLUS–Standard (with other criteria met)
- Score 400–599: BFS Tier 3–4 (with 20% deposit); Resimac Basic possible
- Score < 400: no pathway with BFS; Westpac/Resimac at credit discretion only

---

## chunk_id: eligibility_property_backing
**intent:** eligibility
**subtopic:** Property ownership and backing requirements
**lenders:** Resimac, Westpac WEF, BFS, CFAL
**trigger_words:** "do I need to own property", "property owner", "renting", "no property", "property backed", "home owner", "residential property", "guarantor property"

**Content:**

Property ownership affects eligibility and available tiers differently across lenders.

**Resimac — property type determines tier:**

| Tier | Accepted property situation |
|------|---------------------------|
| PremiumPLUS | Property-backed only |
| Premium | Property-backed only |
| Standard | Property-backed, Spouse-owned, Renter |
| Basic | Property-backed, Spouse-owned, Renter, LWP/other (no boarders) |

*Property-backed definition:* ≥ 25% of property in guarantor's name; equity ≥ 1× NAF; no multiple or adverse encumbrances.
*Spouse-owned property:* Cannot be used as property backing, but can waive deposit requirement. Must be legally married (not de facto).

**Non property-backed deposits (Resimac):**
- Motor vehicles: 10% deposit required
- All other assets: 20% deposit required

**Westpac WEF — property required for new clients only:**
- New-to-bank borrowers must own residential property AND have minimum annual income of $75k
- Existing clients (12+ months WEF history) do not need to demonstrate property ownership
- Medical channel (new clients): same rule — must own residential property + income ≥ $75k p.a.

**BFS:** No property ownership requirement at any tier. Property is not used as a qualifying criterion.

**CFAL:** No explicit property requirement published. Assessed case-by-case.

**Key takeaway for borrowers:**
- Renting with no property: BFS is the most accessible lender (no property requirement at any tier)
- Renting and approaching Resimac: Standard or Basic tier only
- New to Westpac and renting: ineligible for DriveXpress, Replacement and Medical channels

---

## chunk_id: eligibility_residency_visa
**intent:** eligibility
**subtopic:** Residency, citizenship and visa holder requirements
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "visa holder", "non-resident", "permanent resident", "citizen", "temporary visa", "work visa", "457 visa", "international", "overseas"

**Content:**

All lenders require directors and guarantors to meet residency standards. Visa holders face additional restrictions.

**Resimac:**
- All directors and all > 40% shareholders must be Australian Citizens or Permanent Residents residing in Australia
- All must be guarantors to the loan
- No provision for visa holders or non-residents

**BFS — PRIME tiers:**
- Non-resident visa holders accepted with conditions:
  - Minimum income: $100,000 p.a.
  - Loan term must end at least one month before visa expiry
  - Low Doc not available for non-residents

**BFS — BFS Plus:**
- Non-resident visa holders accepted with reduced conditions:
  - Minimum income: $50,000 p.a.
  - Loan term must end at least one month before visa expiry

**BFS — Driver licence (additional):**
- Visa holders must be legally able to drive in Australia (may need to convert to local licence)
- Evidence of insurance required at settlement for international licence holders
- Australian learner licence accepted with co-borrower (passenger vehicles only)
- Licences with interlock conditions: NOT accepted

**Westpac WEF:**
- Commercial loans (Full Doc): loan term must end one month before visa expiry
- No specific income floor published for non-residents (assessed at credit discretion)

**CFAL:** No published visa/residency policy. All guarantors implied to be Australian residents based on AML requirements.

---

## chunk_id: eligibility_discharged_bankrupt
**intent:** eligibility
**subtopic:** Eligibility for discharged bankrupts and adverse credit history
**lenders:** Resimac, BFS, Westpac WEF, CFAL
**trigger_words:** "bankrupt", "discharged bankrupt", "bankruptcy", "Part IX", "debt agreement", "adverse credit", "default", "bad history"

**Content:**

Current bankrupts are universally excluded across all lenders. Discharged bankrupts vary significantly.

| Lender | Current Bankrupt | Discharged Bankrupt |
|--------|-----------------|-------------------|
| Resimac | ✗ Excluded (no exceptions) | ✗ Excluded if discharged within last 10 years |
| BFS | ✗ Auto-declined (no resubmission) | ✓ Accepted with conditions (see below) |
| Westpac WEF | ✗ Excluded | Not explicitly addressed; assessed at credit discretion |
| CFAL | ✗ Excluded (implied) | Not explicitly addressed; assessed at credit discretion |

**BFS discharged bankrupt conditions:**
- 20% deposit required
- More than 12 months must have passed since discharge
- No adverse credit history since discharge
- Available at BFS Plus tier

**RHI (Repayment History Information) standards:**

| Lender / Tier | Last 3 months | Last 12 months |
|--------------|--------------|---------------|
| BFS PRIME (Ultra Prime–Tier 2) | No arrears at all | No more than 30 days in arrears; no financial defaults |
| BFS Plus | No more than 30 days in arrears | No more than 60 days in arrears; no financial defaults |

---

## chunk_id: eligibility_tax_obligations
**intent:** eligibility
**subtopic:** ATO tax compliance and outstanding tax debt requirements
**lenders:** Resimac, Westpac WEF, CFAL
**trigger_words:** "ATO debt", "tax debt", "BAS arrears", "outstanding tax", "payment plan ATO", "tax compliance", "GST lodgements", "BAS overdue"

**Content:**

All lenders require tax obligations to be current. The specific rules vary.

**Resimac — Lite Doc specific:**
- ATO debt must be < 10% of annual turnover
- Must be under an established payment arrangement that has been in place for > 3 months
- Low Doc and Full Doc: ATO compliance assumed; no specific tolerance published

**Westpac WEF (all channels):**
- Statutory lodgements and payments (tax, GST, employee entitlements) must be up to date
- No payment arrangements in place permitted
- Where financial data is not obtained: verbal confirmation of compliance is required

**CFAL (all transaction sizes):**
- Same standard as Westpac: all statutory obligations up to date, no payment arrangements
- Verbal confirmation accepted where financial data is not provided

**BFS:** No specific ATO debt policy published. Tax compliance is assessed as part of income evidence and credit evaluation.

**Key takeaway for borrowers:**
- ATO payment plan in place: only Resimac Lite Doc may be accessible (if < 10% turnover and plan > 3 months old)
- ATO debt with no arrangement: very unlikely to be approved by any lender
- All current and up to date: no restrictions from any lender on this basis

---
---

# INTENT 2 — PRICING
> "What rate will I get?" — covers interest rates, loadings, EV discounts, brokerage

---

## chunk_id: pricing_motor_vehicles_new
**intent:** pricing
**subtopic:** Interest rates for new and near-new motor vehicles (dealer sales)
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "rate for new car", "interest rate new vehicle", "new car finance rate", "demo car rate", "what rate new motor vehicle", "new car loan rate"

**Content:**

For new and near-new motor vehicles purchased from licensed dealers.

**Resimac (new/demo and < 3 years):**

| Tier | Rate |
|------|------|
| PremiumPLUS | 7.64% p.a. |
| Premium / Standard / Basic | 7.89% p.a. |

**BFS Commercial — New & Demo (base rates, before broker margin):**

| Tier | Base Rate | Max Rate |
|------|----------|---------|
| Ultra Prime | 7.60% | 17.15% |
| Tier 1 | 8.25% | 17.15% |
| Tier 2 | 8.50% | 17.15% |
| Tier 3 | 10.15% | 17.15% |
| Tier 4 | 11.50% | 17.15% |

**BFS Consumer — New & Demo (maximum rates):**

| Tier | Max Rate |
|------|---------|
| Ultra Prime | 9.15% |
| Tier 1 | 9.29% |
| Tier 2 | 10.15% |
| Tier 3 | 11.50% |
| Tier 4 | 12.50% |
| BFS Plus | 17.15% |

**Westpac WEF Xpress (new cars, dealer, up to 5 years old):**

| Term | Rate |
|------|------|
| 24 / 36 / 48 months | 7.75% |
| 60 months | 7.85% |

**Westpac WEF Standard — New Motor Vehicles (up to 4 years old, monthly repayments):**

| Amount Financed | 24–36 months | 48 months | 60 months |
|----------------|-------------|----------|----------|
| $15,000–$20,000 | 9.97% | 9.97% | 10.17% |
| $20,000–$50,000 | 8.42% | 8.52% | 8.67% |
| $50,000–$150,000 | 8.32% | 8.42% | 8.62% |
| $150,000+ | By negotiation | — | — |

**Key takeaway for borrowers:**
- Lowest available rate for a new car: Resimac PremiumPLUS at **7.64%** or Westpac Xpress at **7.75%**
- BFS commercial Ultra Prime base rate **7.60%** is competitive but subject to broker margin loading
- Westpac Standard rates for small loans (< $20k) are notably higher (9.97%)

---

## chunk_id: pricing_motor_vehicles_used
**intent:** pricing
**subtopic:** Interest rates for used motor vehicles by age band
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "rate for used car", "second hand car rate", "used vehicle interest rate", "old car finance rate", "2019 car rate", "2015 car rate", "used motor vehicle"

**Content:**

Used vehicle rates depend on the age of the vehicle at the time of financing.

**Resimac (> 3 years old motor vehicles):**

| Tier | Rate |
|------|------|
| PremiumPLUS | 8.24% p.a. |
| Premium / Standard / Basic | 8.49% p.a. |

Risk loading of +2% applies if the asset will be > 16 years old at end of term.

**BFS Commercial — Used vehicles (base rates):**

| Vehicle Age | Ultra Prime | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|-------------|------------|--------|--------|--------|--------|
| 2022–2026 | 7.60% | 8.95% | 10.45% | 12.50% | N/A |
| 2017–2021 | N/A | 10.30% | 11.35% | 12.90% | N/A |
| 2016 & older | 9.55% | 11.05% | 11.80% | 13.40% | N/A |

Note: Tier 4 does not accept commercial used vehicle contracts.

**BFS Consumer — Used vehicles (maximum rates):**

| Vehicle Age | Ultra Prime | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|-------------|------------|--------|--------|--------|--------|
| 2022–2026 | 9.15% | 9.75% | 10.55% | 12.00% | 13.20% |
| 2017–2021 | — | 10.35% | 11.35% | 12.25% | 13.70% |
| 2016 & older | 10.15% | 11.35% | 11.65% | 13.00% | 13.90% |

**Westpac WEF Xpress (used cars, dealer & private sale, up to 5 years old):**

| Channel | Term | Rate |
|---------|------|------|
| Licensed Dealer | 24/36/48 months | 7.75% |
| Licensed Dealer | 60 months | 7.85% |
| Private Sale | 24/36/48 months | 8.17% |
| Private Sale | 60 months | 8.37% |

**Westpac WEF Standard (used motor vehicles 4–10 years old):** add 0.75% to applicable new vehicle rate.

**Key takeaway for borrowers:**
- Vehicles 2022 onwards: rates are close to new vehicle rates
- Vehicles 2016 and older: rates increase significantly; Tier 4 BFS not available for commercial
- Very old vehicles (> 16 years at end of term): Resimac adds a 2% risk loading

---

## chunk_id: pricing_electric_vehicles
**intent:** pricing
**subtopic:** Interest rates and incentives for electric vehicles
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "electric vehicle rate", "EV loan", "electric car finance", "Tesla loan rate", "EV interest rate", "green vehicle", "hybrid car rate"

**Content:**

All three motor vehicle lenders offer preferential rates for electric vehicles.

**Resimac — Electric Vehicles:**

| Tier | Rate | vs. equivalent ICE motor vehicle |
|------|------|----------------------------------|
| PremiumPLUS | **7.54% p.a.** | –0.10% vs motor vehicle < 3 yrs |
| Premium / Standard / Basic | **7.79% p.a.** | –0.10% vs motor vehicle < 3 yrs |

Additional benefit: EV / green goods assets eligible for loan terms up to **84 months** (vs. 60 months standard).

**BFS — Electric Vehicles:**
- Same rate tier table as equivalent ICE motor vehicle (new/demo or used by year)
- No separate published EV rate discount in rate table
- Electric motorcycles accepted if maximum speed > 80 km/h

**Westpac WEF — Electric Vehicles:**
- Reduce applicable rate by **–1%** across all Xpress and Standard WEF rates
- Examples: Xpress dealer 24–48 months: 7.75% → **6.75%**; 60 months: 7.85% → **6.85%**
- Applies to both cars & light commercial and heavy equipment categories

**CFAL:** No EV-specific policy published in reviewed documents.

**Key takeaway for borrowers:**
- Best EV rate currently: Westpac Xpress after –1% discount (**6.75%** for 24–48 months, dealer)
- Resimac PremiumPLUS EV at 7.54% is also very competitive
- Resimac is the only lender to offer extended 84-month terms specifically for green/EV assets

---

## chunk_id: pricing_heavy_equipment_primary
**intent:** pricing
**subtopic:** Interest rates for heavy equipment and primary assets (trucks, excavators, agriculture)
**lenders:** Resimac, Westpac WEF
**trigger_words:** "truck finance rate", "excavator loan rate", "heavy equipment interest rate", "primary asset rate", "forklift rate", "tractor rate", "agricultural equipment rate", "construction equipment rate"

**Content:**

**Resimac — Primary Assets (heavy trucks > 4.5T, trailers, buses, construction, farming, materials handling):**

| Asset Age | PremiumPLUS | Premium / Standard / Basic |
|-----------|------------|---------------------------|
| < 3 years | 8.39% p.a. | 8.64% p.a. |
| > 3 years | 9.29% p.a. | 9.54% p.a. |

Risk loading +2% applies to prime movers (large semi-trailer heads). Prime movers always require a property-backed guarantor.

**Resimac — Secondary Assets (generators, compressors, medical equipment, CNC, engineering):**
- PremiumPLUS: 12.39% p.a.
- Premium / Standard / Basic: 12.64% p.a.

**Resimac — Tertiary Assets (AV equipment, conveyors, wine/beer processing, skip bins, medical lasers):**
- PremiumPLUS: 14.09% p.a.
- Premium / Standard / Basic: 14.34% p.a.

**Westpac WEF Xpress — Heavy Equipment (Category B: trucks, forklifts, excavators, telehandlers, cranes, rollers):**

| Term | Rate |
|------|------|
| 24 / 36 / 48 months | **8.17%** |
| 60 months | **8.37%** |

**Westpac WEF Standard — New Plant & Equipment (excl. computers, fixtures & fittings):**

| Amount Financed | 24–36 months | 48 months | 60 months |
|----------------|-------------|----------|----------|
| $15,000–$20,000 | 10.22% | 10.36% | 10.56% |
| $20,000–$50,000 | 8.72% | 8.86% | 9.06% |
| $50,000–$150,000 | 8.52% | 8.62% | 8.82% |
| $150,000+ | By negotiation | — | — |

**Electric vehicles (equipment category):** Westpac applies –1% to all equipment rates as well.

**Key takeaway for borrowers:**
- Westpac Xpress offers flat competitive rates for heavy equipment regardless of amount (8.17%/8.37%)
- Resimac rates for primary assets under 3 years (8.39–8.64%) are comparable
- Secondary and tertiary assets at Resimac carry significantly higher rates (12–14%) — very different risk tier

---

## chunk_id: pricing_private_sale_loading
**intent:** pricing
**subtopic:** Rate loadings for private sales vs dealer purchases
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "private sale rate", "buying from private seller", "private seller loan", "buying from individual", "not from dealer", "private purchase finance"

**Content:**

Buying from a private seller (rather than a licensed dealer) typically attracts higher rates and additional requirements.

| Lender | Private Sale Rate Impact | Additional Requirements |
|--------|------------------------|------------------------|
| Resimac | +2% risk loading on top of standard rate | — |
| BFS | +0.50% loading on both commercial and consumer rates | Vehicle inspection report required: DoxAI Asset Verification (preferred) or Redbook; must be arm's length transaction |
| Westpac Xpress | Separate (higher) rate tier — e.g. 8.17% vs 7.75% for dealer | Applies to Category A (motor vehicles / light commercial) only |
| Westpac Standard | Rate unchanged; additional inspection may apply | — |
| CFAL | Not explicitly specified | — |

**Westpac private sale restrictions:**
- Private sales only available for Category A assets (passenger cars and light commercial < 4.5T)
- Not available for Category B (heavy equipment) or Category C (agriculture)

**BFS private sale note:**
- Available across PRIME and BFS Plus tiers
- Additional requirements listed in QuickSell documents library (Private Sale Requirements document)

**Key takeaway for borrowers:**
- Buying privately always costs more in rate vs dealer purchase
- Resimac has the largest loading (+2%); BFS the smallest (+0.50%)
- Westpac limits private sales to motor vehicles only

---
---

# INTENT 3 — LOAN LIMITS
> "How much can I borrow?" — covers maximum amounts, exposure caps, high-value loans

---

## chunk_id: loan_limits_by_lender_overview
**intent:** loan_limits
**subtopic:** Maximum loan amounts across all lenders — quick comparison
**lenders:** Resimac, BFS, Westpac WEF, CFAL
**trigger_words:** "how much can I borrow", "maximum loan", "loan limit", "borrow $300k", "borrow $500k", "maximum finance amount", "loan cap"

**Content:**

| Lender | Standard Maximum | High Value / Extended | Notes |
|--------|----------------|----------------------|-------|
| Resimac PremiumPLUS/Premium Full Doc | **$450k NAF** | — | Per asset type |
| Resimac Standard Full Doc | $400k NAF | — | — |
| Resimac Basic Full Doc | $200k NAF | — | — |
| BFS PRIME (standard) | **$250k** | $250k–$400k (case-by-case, 20% deposit, asset-backed) | Ultra Prime–Tier 2 only for high value |
| BFS PRIME (private sale) | $150k | — | — |
| BFS Plus | $100k | — | — |
| Westpac WEF New-to-Bank | $150k (A), $150k (B&C) | — | Must own property + $75k income |
| Westpac WEF Existing Client | Up to $500k (C) | $500k+ by negotiation | 12 months WEF history required |
| CFAL | Case-by-case | $1m+ possible | Documentation increases with size |

**Individual asset caps (Resimac):**
- Passenger vehicle (per asset): max $250k NAF
- Motorbike (per asset): max $75k NAF

**Exposure limits (Resimac):**
- SME: $500k total
- Large corporate: $750k total
- Government / Sovereign rated entities: $2m total

---

## chunk_id: loan_limits_small_business_new
**intent:** loan_limits
**subtopic:** Loan limits for new or recently established businesses
**lenders:** BFS, Westpac WEF, Resimac
**trigger_words:** "new business loan", "just started business", "startup loan", "new ABN loan", "less than 2 years business", "new business vehicle finance"

**Content:**

New businesses face reduced limits and more limited lender options.

**BFS New Business Ventures (< 12 months ABN):**
- Maximum: $100k total exposure
- Available tiers: Ultra Prime to Tier 4
- Income evidence: 90-day bank statements (+ copy of run contract for couriers)
- Minimum deposit: 20% for Tier 3 and 4
- Not available via BFS Plus

**BFS Full Doc (12+ months ABN):**
- Maximum: $250k standard / $400k high value
- Wider tier access: Ultra Prime to Tier 4 and BFS Plus

**Westpac WEF New-to-Bank:**
- Maximum: $150k per asset (DriveXpress); eligible goods A, B & C
- Maximum total DriveXpress exposure: $250k
- Requirements: owns residential property + annual income ≥ $75k
- Must have > 2 years ABN + current GST

**Resimac Basic (> 1 year ABN):**
- Maximum: $100k–$200k depending on doc type
- All asset categories except tertiary on Low Doc

**Key takeaway for borrowers:**
- Under 12 months: BFS New Business Ventures is the primary option ($100k max)
- 1–2 years: Resimac Basic or BFS Full Doc; Westpac possible with property ownership
- Over 2 years: full access to all lenders

---

## chunk_id: loan_limits_high_value
**intent:** loan_limits
**subtopic:** High-value loan options above $250k
**lenders:** Resimac, BFS, Westpac WEF, CFAL
**trigger_words:** "borrow more than $250k", "large loan equipment", "$300k loan", "$400k loan", "$500k finance", "high value loan", "large asset finance"

**Content:**

Options for borrowers seeking finance above $250k.

**Resimac:**
- Up to $450k NAF: PremiumPLUS or Premium, Full Doc
- Up to $400k NAF: Standard, Full Doc
- Up to $750k total exposure: Large corporate clients
- Conditions: ABN > 4–6 years, property-backed, Full Doc financials

**BFS High Value Loans ($250k–$400k):**
- Available to Ultra Prime and Tier 1–2 only
- Minimum 20% deposit
- Asset-backed applicants only
- Assessed case-by-case with acceptable vehicle
- Not available to Tier 3, Tier 4 or BFS Plus

**Westpac WEF Existing Clients:**
- Up to $500k: Category C assets (DriveXpress existing client)
- Up to $650k: Category B & C (Replacement channel, existing client)
- Above $150k (Standard WEF): by negotiation

**CFAL:**
- No published cap; loan size $500k–$1m and $1m+ are documented transaction tiers
- Full financial package required: 3 years financials, ATO portal, aged debtor/creditor listing
- > $1m: additionally requires cash flow projections, succession plan, competitor/client list

**Key takeaway for borrowers:**
- $250k–$400k: BFS (with 20% deposit, Tier 1–2) or Resimac (Full Doc, Premium/PremiumPLUS)
- $400k–$750k: Westpac existing clients or Resimac large corporate
- Over $750k: CFAL or Westpac by negotiation with comprehensive financials

---
---

# INTENT 4 — DOCUMENTATION
> "What do I need to prepare?" — covers income evidence, bank statements, financials

---

## chunk_id: documentation_low_doc_options
**intent:** documentation
**subtopic:** Which lenders offer simplified / low doc options and their conditions
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "low doc", "no financials", "without tax return", "minimal paperwork", "self-employed no financials", "lite doc", "reduced documentation", "simple application"

**Content:**

Three of the four lenders offer simplified documentation pathways. CFAL requires full financials for all transactions.

**Resimac — Low Doc:**
- Available: PremiumPLUS through to Basic tier
- Documents needed: Application + privacy consent, Asset & Liability Statement only
- NOT available for: Tertiary asset category
- Maximum: varies by tier (Basic: up to $100k; PremiumPLUS: up to $300k)

**Resimac — Lite Doc:**
- Additional: 12 months running ATO portals + two most recent BAS portals
- 90-day bank statements on request
- Condition: ATO debt < 10% of turnover + payment arrangement > 3 months
- BAS annualised minimum turnover must be > 2.5× asset purchase price

**BFS — Commercial Low Doc:**
- Available: Ultra Prime through Tier 2 only (not Tier 3, 4 or BFS Plus)
- Documents: Business Customer Financial Declaration (signed)
- Maximum total exposure: $150k
- Trading history: 2+ years ABN + GST registered
- Minimum deposit: 0% (Tier 1–2); 20% (Tier 3–4, but Tier 3–4 not eligible for Low Doc)
- Guarantor must be Australian citizen or permanent resident

**Westpac WEF — DriveXpress (fast-track, no financials):**
- No financial statements required if all fast-track criteria met
- Documents needed: Signed Affordability Declaration; satisfactory credit bureau and ASIC search; 90-day bank statements
- If criteria not met: last 2 years financials + 2 years directors' ITRs required → standard application

**CFAL:** No Low Doc option. Minimum documentation for ≤ $250k includes 2 years financial statements and 2 years individual tax returns.

**Key takeaway for borrowers:**
- Simplest option: Westpac DriveXpress (no financials if criteria met) or Resimac Low Doc (A&L statement only)
- Self-employed with limited records: Resimac Lite Doc (BAS + ATO portal) or BFS Low Doc (Financial Declaration)
- CFAL always requires full 2-year financials regardless of deal size

---

## chunk_id: documentation_full_doc_requirements
**intent:** documentation
**subtopic:** Full documentation requirements for larger or standard loans
**lenders:** Resimac, BFS, Westpac WEF, CFAL
**trigger_words:** "what documents do I need", "full application documents", "financials required", "tax return loan", "financial statements required", "what paperwork", "bank statements loan"

**Content:**

Full documentation requirements by lender and loan size.

**Resimac — Full Doc:**

| Document | Required |
|---------|---------|
| Application + privacy consent | ✓ |
| Asset & Liability Statement (all directors/guarantors) | ✓ |
| 12 months ATO portal (TFN redacted) | ✓ |
| Two most recent BAS portals | ✓ |
| 90-day bank statements | ✓ |
| Financial accounts / tax returns | ✓ |

**BFS — Commercial Full Doc:**

| Loan Size | Required |
|----------|---------|
| Up to $100k | 90-day bank statements |
| Over $100k | 2 years signed externally prepared financial statements (≤ 18 months old) + management accounts if financials > 18 months old |

**Westpac WEF — Standard Full Doc:**
- Evidence of income
- 90-day bank statements (mandatory for BFS Plus; consumer: on request)
- Motorcycles and caravans: invoice upfront before asset loaded

**CFAL — Documentation by transaction size:**

| Size | Key additions |
|------|--------------|
| ≤ $250k | 2 years financials (P&L + balance sheet) + 2 years individual tax returns |
| $250k–$500k | + Detailed background of business/directors + ATO portal (TFN redacted) |
| $500k–$1m | + 3 years financials + interim accounts (if year-end > 6 months old) + aged debtor/creditor listing + commentary on movements ≥ 10% |
| > $1m | + Cash flow projections + succession planning + list of major competitors and clients |

**BFS — Consumer loan income evidence:**

| Income type | Documents required |
|------------|-------------------|
| PAYG | Most recent payslip with YTD (Jul/Aug: also June payslip or annual statement) |
| Rental | Rental statement or bank statements (shaded to 80%) |
| Super | Super statement or bank statements with regular credits |
| Pension/Benefits | Must be ongoing; Centrelink statement or body statement |
| Self-employed ≤ $100k | Most recent tax return or Notice of Assessment |
| Self-employed > $100k | 2 years externally prepared financials ≤ 18 months + tax return + management accounts |

---
---

# INTENT 5 — ASSET ELIGIBILITY
> "Can I finance this specific asset?" — covers asset types, age, condition, special categories

---

## chunk_id: asset_motor_vehicles_eligibility
**intent:** asset_eligibility
**subtopic:** Motor vehicle types accepted and age limits
**lenders:** Resimac, BFS, Westpac WEF, CFAL
**trigger_words:** "can I finance a car", "vehicle finance eligibility", "what cars can I finance", "ute loan", "van finance", "light commercial vehicle loan", "motorbike loan", "caravan finance"

**Content:**

**Accepted vehicle types by lender:**

| Vehicle Type | Resimac | BFS PRIME | BFS Plus | Westpac WEF | CFAL |
|-------------|---------|----------|---------|------------|------|
| Passenger cars | ✓ | ✓ | ✓ | ✓ (Cat A) | ✓ |
| Vans / utes (< 4.5T) | ✓ | ✓ | ✓ | ✓ (Cat A) | ✓ |
| Motorbikes | ✓ (max $75k) | ✓ | — | Limited | — |
| Caravans | ✓ (Primary) | ✓ | — | Limited | — |
| Motorhomes / campervans | — | ✓ | — | Limited | — |
| Classic cars | ✓ (+2% loading) | — | — | — | — |

**Maximum vehicle age:**

| Lender | Maximum Age at Start of Term | Maximum Age at End of Term |
|--------|---------------------------|--------------------------|
| Resimac | Not specified at start | **25 years** (motor vehicles excl. classic) |
| BFS PRIME | **15 years** at start (terms ≤ 60m); **7 years** at start (terms > 60m) | — |
| BFS Plus | **15 years** at start | — |
| Westpac WEF | **15 years** at start (Xpress category A) | — |
| CFAL | Per Matrix policy | — |

**Special vehicle conditions:**

*Motorbikes (BFS):*
- Maximum term 60 months; no balloon payments
- Must be registered, on-road 2/3/4 wheels
- Electric motorbikes: accepted if max speed > 80 km/h

*Caravans & campervans (BFS):*
- Leisure use only (not primary residence)
- Commercial use requires accountant's letter confirming business use

*Classic cars (Resimac):*
- 2% risk loading applies
- Balloon payments not available for classic cars

*Ride-share / hire / rental vehicles:*
- Resimac: explicitly excluded
- BFS: "limited appetite" — may be accepted but term may be reduced
- Westpac: limited appetite; term may be reduced for courier/ride-share

---

## chunk_id: asset_heavy_equipment_eligibility
**intent:** asset_eligibility
**subtopic:** Heavy equipment and plant — what is accepted and by which lender
**lenders:** Resimac, Westpac WEF, CFAL
**trigger_words:** "truck finance", "excavator loan", "forklift finance", "crane loan", "yellow goods", "heavy machinery loan", "construction equipment finance", "tractor loan", "agricultural machinery"

**Content:**

**Heavy equipment eligibility by lender:**

| Asset Type | Resimac (Primary) | Westpac (Cat B) | CFAL |
|-----------|------------------|----------------|------|
| Heavy trucks > 4.5T GVM | ✓ | ✓ (≤ 5 yrs, dealer) | ✓ |
| Trailers | ✓ | ✓ | ✓ |
| Buses / coaches | ✓ | ✓ (route only, ≤ 5 yrs) | ✓ |
| Forklifts / telehandlers | ✓ | ✓ | ✓ |
| Boom / scissor / spider lifts | ✓ | ✓ | ✓ |
| Excavators / skid steers | ✓ | ✓ | ✓ |
| Graders / scrapers / dozers / rollers | ✓ | ✓ | ✓ |
| Mobile / tight-access cranes | ✓ | ✓ (≤ **3 yrs**, dealer) | ✓ |
| Prime movers (semi-trailer heads) | ✓ (+2% loading; property-backed guarantor required) | — | — |

**Agricultural equipment:**

| Asset Type | Resimac (Primary) | Westpac (Cat C) | CFAL |
|-----------|------------------|----------------|------|
| Tractors / headers / harvesters | ✓ | ✓ (≤ 7 yrs, dealer) | ✓ |
| Cotton pickers / balers | ✓ | ✓ | ✓ |
| Ploughs / seeders / sprayers | ✓ | ✓ | ✓ |
| All-terrain vehicles / feed wagons | ✓ | ✓ | ✓ |

**Maximum asset age for heavy equipment:**

| Lender | Category | Max Age |
|--------|---------|--------|
| Resimac | Primary assets | 25 years at end of term |
| Resimac | Secondary assets | 10 years at end of term |
| Resimac | Tertiary assets | 5 years at end of term |
| Westpac | Category B (heavy equipment) | 5 years at start of term |
| Westpac | Category B (cranes only) | 3 years at start of term |
| Westpac | Category C (agriculture) | 7 years at start of term |

**BFS:** Does not finance heavy equipment or agriculture. Motor vehicles (< 4.5T GVM) only.

**Attachment / accessory rules (Westpac):**
- Modifications / aftermarket accessories: max 10% of dealer invoice price
- Tractor / yellow goods attachments must be funded together with the primary asset — cannot be financed separately

---

## chunk_id: asset_excluded_items
**intent:** asset_eligibility
**subtopic:** Assets that cannot be financed by any lender
**lenders:** Resimac, BFS, Westpac WEF, CFAL
**trigger_words:** "can I finance gym equipment", "software loan", "office furniture loan", "food truck finance", "livestock loan", "what can't be financed", "excluded assets", "not eligible for finance"

**Content:**

The following asset types are explicitly excluded by at least one or more lenders.

**Resimac — explicitly excluded:**
Fixtures and fittings, cool rooms and spray booths, intangible assets, refrigeration equipment, gym equipment, hospitality equipment, software, scaffolding, racking and temporary fencing, food trucks, artwork, vending and gaming machines, livestock, ride-share / taxis / repairable write-offs, demountables and shipping containers, office furniture, electric or motor vehicles used for hire/rental purposes, IT hardware.

**BFS — excluded loan purposes (not assets per se):**
Debt consolidation, cash raising, top-up loans, sale and buyback, sale and leaseback, mid-term refinancing.

**Westpac WEF — excluded assets/structures:**
Novated leases, sale and hirebacks (except Medical channel ≤ 30 days from acquisition), taxis and hire cars, imported/exotic cars (Category A), repairable write-offs, computers and IT hardware (excluded from Standard Plant & Equipment rates), fixtures and fittings.

**Commonly excluded across multiple lenders:**
- Livestock
- Software and intangible assets
- Gym and hospitality equipment
- IT hardware and computers
- Artwork
- Office furniture
- Ride-share, taxi and hire/rental vehicles

---
---

# INTENT 6 — SETTLEMENT & PROCESS
> "What happens after approval?" — covers settlement docs, PPSR, insurance, process steps

---

## chunk_id: settlement_universal_requirements
**intent:** settlement
**subtopic:** Documents and steps required at settlement — all lenders
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "settlement documents", "what do I need to settle", "finalise loan", "settlement process", "PPSR", "insurance settlement", "sign loan documents"

**Content:**

The following requirements apply at settlement across all reviewed lenders:

**Universal settlement checklist:**

| Requirement | Resimac | BFS | Westpac WEF |
|------------|---------|-----|------------|
| Signed loan documents (ink or e-sign) | ✓ | ✓ | ✓ |
| Asset insurance (lender as interested party) | ✓ | ✓ | ✓ |
| PPSR registration | ✓ (at cost) | ✓ ($6 fee) | ✓ |
| Vehicle tax invoice or private sale agreement | ✓ | ✓ | ✓ |
| Biometric identity verification | — | ✓ (link in approval) | ✓ |
| Payout documents via platform | — | QuickSell | DriveOnline / QuickSell |

**Insurance requirements:**
- All lenders: asset must be insured before settlement
- Lender must be noted as an interested party on the policy
- BFS: insurance details must be loaded into QuickSell
- Westpac: for assets > $150k, a Certificate of Currency (CoC) is required

**Westpac CoC update (effective 24 February 2025):**
- Fleet policies: no longer need to list specific VIN/serial on the CoC (motor vehicles only)
- Non-fleet and non-motor vehicle assets: VIN/serial must still be listed

**Westpac PPSR update (effective 24 February 2025):**
- Motor vehicles with a VIN (buybacks and private sales): PPSR company search over private seller no longer required
- Condition: day-of or day-before search must show no other registration on that VIN
- All other serial types (PIN, HIN, VH number): original process still applies

---
---

# INTENT 7 — SPECIAL PROGRAMS
> "Are there programs for my situation?" — covers rollover, replacement, medical, green goods

---

## chunk_id: special_programs_refinance_rollover
**intent:** special_programs
**subtopic:** Refinancing, rollover and contract replacement options
**lenders:** Westpac WEF, Resimac
**trigger_words:** "refinance equipment loan", "roll over contract", "extend loan", "replace existing finance", "refinance truck loan", "switch lender", "mid-term refinance"

**Content:**

**Westpac WEF — Rollover (contract extension):**
- Existing clients only (12 months current WEF history or finalised WEF contract within last 12 months)
- Original funder Westpac: max $500k, all asset categories
- Original funder other financier: max $250k, Category A & B only; inspection required
- Conditions: ABN > 2 years + GST registered; statutory obligations up to date; satisfactory credit bureau and ASIC search; contract being rolled has been operating > 12 months; borrower/guarantor and security position must be the same; St.George Group EF residual values accepted

**Westpac WEF — Replacement (asset swap):**
- New client: max $150k (Category A & B); must own residential property
- Existing client: max $200k (A), $650k (B & C)
- Conditions: monthly repayments ≤ 125% of payment being replaced (new clients) or ≤ 150% (existing clients); contract being replaced must have been operating ≥ 12 months and conducted within arrangements; finalised within last 6 months or on settlement; borrower/guarantors same as or additional to original contract

**BFS — Excluded refinance types:**
- Mid-term refinancing: explicitly excluded
- Sale and leaseback: excluded
- Top-up loans: excluded

**Resimac:**
- Sale and buyback: only for PremiumPLUS or Premium; dealership sales only; asset purchased within 30 days of receiving the application; assessed case-by-case

---

## chunk_id: special_programs_medical_professionals
**intent:** special_programs
**subtopic:** Specialist finance programs for medical and allied health professionals
**lenders:** Westpac WEF
**trigger_words:** "doctor loan", "medical professional finance", "GP equipment loan", "dental equipment finance", "vet loan", "allied health loan", "medical equipment finance", "physiotherapist loan"

**Content:**

Westpac WEF operates a dedicated Medical channel for healthcare professionals.

**Eligible professions:**

| Category | Included |
|---------|---------|
| Medical Specialist, GP, Dental and Vet | Doctors (GPs and specialists), dentists, veterinarians |
| Allied Health Practitioners | Occupational Therapists, Optometrists, Osteopaths, Physiotherapists, Chiropractors, Audiologists, Pathology services, Podiatrists, Psychologists, Speech Pathologists |
| Excluded | Pharmacists |

**Loan limits:**

| Asset Type | Medical Specialist / GP / Dental / Vet | Allied Health |
|-----------|--------------------------------------|--------------|
| Motor vehicle (≤ 5 years) | < $250,000 | < $150,000 |
| New office equipment and fittings | < $150,000 | < $150,000 |
| New medical equipment | < $350,000 | < $150,000 |
| **Max cumulative approvals** | **< $500,000** | **< $250,000** |

**Conditions:**
- Must be in business > 2 years and registered for GST
- Credit bureau satisfactory
- Statutory obligations up to date
- New clients: must own residential property + minimum annual income $75k
- Sale and hire back permitted if < 30 days past acquisition date
- Private sale permitted for motor vehicles
- Signed Affordability Declaration required

---

## chunk_id: special_programs_green_ev_extended_terms
**intent:** special_programs
**subtopic:** Extended loan terms and benefits for electric / green assets
**lenders:** Resimac
**trigger_words:** "84 month loan", "7 year loan equipment", "longer term EV loan", "green goods loan", "extended term electric vehicle", "sustainable asset finance"

**Content:**

**Resimac — Green Goods extended term:**
- Standard loan terms: 12–60 months
- Green Goods (EV and sustainable assets): eligible for terms up to **84 months**
- This is the only lender in the group to offer extended terms specifically for green/EV assets

**Combined EV benefits at Resimac:**
1. Lowest interest rate in product range: 7.54% (PremiumPLUS) / 7.79% (other tiers)
2. Extended loan term up to 84 months (vs 60 months standard)
3. Lower deposit requirement compared to equivalent non-EV assets in some tiers

**Other lenders — term limits:**
- BFS PRIME: up to 84 months (standard — not EV specific)
- BFS Plus: up to 60 months
- Westpac WEF: up to 84 months (standard); Medical Category C buses up to 10 years

---
---

# INTENT 8 — FEES & COSTS
> "What fees will I pay?" — covers setup, ongoing, early exit costs and brokerage

---

## chunk_id: fees_all_lenders_comparison
**intent:** fees
**subtopic:** Fee structures across all lenders
**lenders:** Resimac, BFS, Westpac WEF
**trigger_words:** "fees", "setup fee", "establishment fee", "monthly fee", "account fee", "early repayment fee", "break cost", "what does it cost", "brokerage fee"

**Content:**

**Establishment / setup fees:**

| Lender | Fee | Private Sale Premium |
|--------|-----|---------------------|
| Resimac | $495 setup fee | +$200 (private sale / sale and buyback: $695) |
| BFS Consumer | $525 | +$100 (private sale: $625) |
| BFS Commercial | $575 | +$100 (private sale: $675) |
| Westpac WEF | Not published in rate sheet | — |
| CFAL | Not published in checklist | — |

**Ongoing fees:**

| Lender | Monthly Fee |
|--------|------------|
| Resimac | $4.95/month |
| BFS | $10.00/month (monthly repayments) / $4.62/fortnight / $2.31/week |
| Westpac / CFAL | Not published |

**Early termination:**

| Lender | Consumer | Commercial |
|--------|---------|-----------|
| Resimac | Not specified | Not specified |
| BFS | Admin fee $70 + up to $750 (reducing by $12/month of repayments made) | Admin fee $85 + 35% of remaining interest (15% if refinancing with BFS) |

**Brokerage / origination:**

| Lender | Broker Commission | Cap |
|--------|-----------------|-----|
| Resimac | Up to 5.5% without rate impact; above 5.5% incurs 0.5% rate increase per 1% extra brokerage | Max brokerage 8.8% |
| BFS | Origination fee max $1,650 (added to loan, paid to introducer); 75% overs net of GST | — |
| Westpac Xpress | Up to 3% | — |
| Westpac Standard | Up to 3%; above 3% (up to 4%) by negotiation | Max 4% |

**BFS commission clawback:**
- Contract terminated or paid in full within 12 months: 100% commission refunded to BFS
- Repossession or loan write-off within 24 months: 100% commission refunded to BFS

**PPSR registration fees:**
- Resimac: at cost (pass-through)
- BFS: flat $6
- Westpac: included in process (no published fee)

