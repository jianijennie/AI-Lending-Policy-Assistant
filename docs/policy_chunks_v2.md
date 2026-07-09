# Lender Policy Knowledge Base — v3 (Unified Taxonomy)
#
# DESIGN PRINCIPLES
# ─────────────────────────────────────────────────────────────────
# Layer 0 │ TAXONOMY REGISTRY   — canonical field definitions &
# │                               controlled vocabulary
# Layer 1 │ INTENT CHUNKS       — borrower query driven (from v2)
# │                               each chunk now carries full
# │                               taxonomy metadata
# Layer 2 │ COMPARISON MATRIX   — cross-lender tables per dimension
# Layer 3 │ RECOMMENDATION ENGINE— scored matching logic +
# │                               decision trees
# Layer 4 │ DIFFERENCE ANALYSIS  — delta tables highlighting where
#                                  lenders diverge most
#
# HOW RAG SHOULD USE THIS FILE
# ─────────────────────────────────────────────────────────────────
# 1. Parse taxonomy fields as metadata filters (lender, intent,
#    dimension, borrower_profile tags)
# 2. Use trigger_words for dense retrieval / semantic matching
# 3. Layer 2–4 chunks answer "compare", "recommend", "difference"
#    queries directly — do NOT try to synthesise from Layer 1 chunks
# 4. chunk_id is the stable retrieval key; never embed chunk_id
#    text into the vector — use it as a metadata field only
#
# Last updated : 2026-06-27
# Version      : 3.0

═══════════════════════════════════════════════════════════════════
# LAYER 0 — UNIFIED TAXONOMY REGISTRY
═══════════════════════════════════════════════════════════════════

## chunk_id: taxonomy_registry
**layer:** 0
**type:** registry
**description:** Canonical controlled vocabulary for all chunks in this knowledge base. Every field value used in any chunk must appear here first. RAG systems should load this chunk as a system-level context.

---

### DIMENSION: lender
Canonical lender identifiers used in all metadata fields.

| Code | Full Name | Licence |
|------|-----------|---------|
| RESIMAC | Resimac Asset Finance Pty Ltd | ACL 393031 |
| BFS | Branded Financial Services | ACL 392188 |
| WESTPAC | Westpac Equipment Finance (WEF) | ACL 233714 |
| CFAL | Capital Finance Australia Ltd | ACL 393031 |

---

### DIMENSION: intent
Primary borrower query intent. Every chunk maps to exactly one intent.

| Code | Plain English | Typical trigger question |
|------|--------------|--------------------------|
| ELIGIBILITY | Can I qualify? | "Can I get approved with X months ABN?" |
| PRICING | What rate will I get? | "What is the interest rate for a used truck?" |
| LOAN_LIMITS | How much can I borrow? | "Can I borrow $300k?" |
| DOCUMENTATION | What do I need to prepare? | "What documents are required?" |
| ASSET_ELIGIBILITY | Can I finance this asset? | "Can I finance a forklift?" |
| EXCLUSIONS | Is this excluded? | "Can I use this loan for debt consolidation?" |
| SETTLEMENT | What happens at settlement? | "What do I need to settle the loan?" |
| SPECIAL_PROGRAMS | Are there programs for my situation? | "Do you have programs for doctors?" |
| FEES | What will it cost me? | "What fees apply?" |
| COMPARE | Which lender is better for me? | "Compare Resimac vs BFS for used trucks" |
| RECOMMEND | Who should I go with? | "Which lender suits my situation?" |
| DIFFERENCE | How do these lenders differ? | "What is different between Westpac and BFS?" |

---

### DIMENSION: borrower_profile
Tags used to describe the borrower's situation. Multiple tags may apply to one chunk.

| Tag | Meaning |
|-----|---------|
| ABN_UNDER_1YR | Business registered less than 1 year |
| ABN_1_2YR | ABN 1–2 years |
| ABN_2_4YR | ABN 2–4 years |
| ABN_4_6YR | ABN 4–6 years |
| ABN_OVER_6YR | ABN over 6 years |
| PROPERTY_BACKED | Borrower or guarantor owns residential/commercial property |
| NO_PROPERTY | Borrower does not own property |
| RENTER | Borrower is renting |
| HIGH_CREDIT | Credit score ≥ 800 |
| MID_CREDIT | Credit score 550–799 |
| LOW_CREDIT | Credit score 400–549 |
| SUBPRIME | Credit score < 400 |
| DISCHARGED_BANKRUPT | Previously bankrupt, now discharged |
| VISA_HOLDER | Non-citizen / non-PR visa holder |
| CONSUMER | Individual borrowing for personal vehicle use |
| COMMERCIAL | Business / ABN holder borrowing for business use |
| SELF_EMPLOYED | Sole trader or director without PAYG income |
| NEW_BUSINESS | Business < 12 months trading |
| MEDICAL_PROFESSIONAL | Doctor, dentist, vet, allied health practitioner |
| EXISTING_CLIENT | Has existing loan with the lender |
| NEW_CLIENT | No prior relationship with the lender |

---

### DIMENSION: asset_class
Controlled vocabulary for asset types.

| Code | Description | Resimac | BFS | Westpac | CFAL |
|------|-------------|---------|-----|---------|------|
| MV_NEW | Motor vehicle new/demo (≤ 3 yrs) | Motor vehicles | New & Demo | Category A | ✓ |
| MV_USED | Motor vehicle used (> 3 yrs) | Motor vehicles | Used by year | Category A | ✓ |
| EV | Electric vehicle | Electric vehicles | EV (same tiers) | EV (–1%) | — |
| LCV | Light commercial vehicle < 4.5T | Motor vehicles | ✓ | Category A | ✓ |
| PRIMARY | Heavy trucks, trailers, construction, agriculture | Primary assets | — | Category B/C | ✓ |
| SECONDARY | Engineering, medical, CNC, landscape equipment | Secondary assets | — | — | ✓ |
| TERTIARY | AV, conveyors, processing, medical lasers | Tertiary assets | — | — | ✓ |
| CARAVAN | Caravans, campervans, camper trailers | Primary assets | ✓ | Limited | — |
| MOTORBIKE | Motorcycles | Motor vehicles | ✓ (max $75k) | Limited | — |
| MEDICAL_EQUIP | New medical equipment | — | — | Medical channel | ✓ |
| OFFICE_EQUIP | New office equipment and fittings | — | — | Medical channel | ✓ |

---

### DIMENSION: doc_type
Documentation tier used by each lender.

| Code | Resimac | BFS | Westpac | CFAL |
|------|---------|-----|---------|------|
| LOW_DOC | Low Doc | Commercial Low Doc | DriveXpress (fast-track) | N/A |
| LITE_DOC | Lite Doc | — | — | N/A |
| FULL_DOC | Full Doc | Full Doc | Standard WEF | All transactions |
| NEW_BIZ | — | New Business Ventures | — | — |

---

### DIMENSION: loan_size_band
Standard size bands used across all comparison tables.

| Code | Range |
|------|-------|
| MICRO | < $20,000 |
| SMALL | $20,000–$100,000 |
| MEDIUM | $100,000–$250,000 |
| LARGE | $250,000–$500,000 |
| XLARGE | > $500,000 |

---

### DIMENSION: policy_field
Atomic policy attributes. Used in difference analysis chunks.

| Code | Description |
|------|-------------|
| MIN_ABN | Minimum ABN registration duration |
| MIN_GST | Minimum GST registration duration |
| MIN_CREDIT_SCORE | Minimum credit score |
| PROPERTY_REQUIRED | Whether property ownership is required |
| DEPOSIT_REQUIRED | Minimum deposit percentage |
| MAX_LOAN | Maximum loan amount |
| MAX_TERM | Maximum loan term |
| BASE_RATE | Base / headline interest rate |
| RISK_LOADING | Risk-based rate loadings |
| EV_DISCOUNT | Electric vehicle rate benefit |
| BROKERAGE_MAX | Maximum allowable brokerage |
| PRIVATE_SALE_LOADING | Rate loading for private sales |
| ASSET_AGE_MAX | Maximum asset age at start or end of term |

═══════════════════════════════════════════════════════════════════
# LAYER 1 — INTENT CHUNKS (v2 enhanced with taxonomy metadata)
# Note: full content retained from v2; taxonomy fields added to header
═══════════════════════════════════════════════════════════════════

---

## chunk_id: eligibility_abn_gst_duration
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_ABN, MIN_GST
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** ABN_UNDER_1YR, ABN_1_2YR, ABN_2_4YR, ABN_4_6YR, ABN_OVER_6YR, COMMERCIAL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "how long do I need my ABN", "new business ABN", "just registered ABN", "ABN less than 2 years", "GST registered recently", "how long in business"

**Content:**

A borrower's ABN and GST registration duration is one of the primary eligibility gates. Here is what each lender requires:

| Lender | Minimum ABN | Minimum GST | Notes |
|--------|------------|------------|-------|
| Resimac PremiumPLUS | > 6 years | > 3 years | Highest tier; lowest rates |
| Resimac Premium | > 4 years | > 2 years | Property-backed only |
| Resimac Standard | > 2 years | > 1 year | Accepts renters |
| Resimac Basic | > 1 year | > 1 year | Widest property type acceptance |
| BFS Low Doc (commercial) | 2+ years ABN + GST | — | Max $150k |
| BFS Full Doc (commercial) | 12+ months ABN | — | Max $250k standard |
| BFS New Business Ventures | < 12 months ABN | — | Max $100k; Ultra Prime–Tier 4 |
| Westpac WEF (all channels) | > 2 years | Currently registered | Verbal confirmation if financials not obtained |
| CFAL | ≥ 2 years | Currently registered | All transaction sizes |

**Matching logic:**
- ABN < 12 months → BFS New Business Ventures only (max $100k)
- ABN 12 months–2 years → BFS Full Doc; Westpac new-to-bank with property + $75k income
- ABN 2–4 years → Resimac Standard/Basic; BFS; Westpac; CFAL
- ABN 4–6 years → Resimac Premium+; all lenders
- ABN > 6 years → all lenders including Resimac PremiumPLUS (best rates)

---

## chunk_id: eligibility_credit_score
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_CREDIT_SCORE
**lenders:** RESIMAC, BFS
**borrower_profile:** HIGH_CREDIT, MID_CREDIT, LOW_CREDIT, SUBPRIME, COMMERCIAL, CONSUMER
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "credit score", "Equifax score", "Experian score", "bad credit", "low credit score", "credit history", "CCR score", "what score do I need"

**Content:**

| Lender | Score System | Minimum Score | Key Conditions |
|--------|-------------|--------------|---------------|
| Resimac Low Doc | Equifax | Sole Trader ≥ 650 / Company ≥ 600 | Score < 450 → referral or decline |
| Resimac Lite/Full Doc | Equifax | Sole Trader ≥ 600 / Company ≥ 550 | Highest score of company or any guarantor used |
| BFS Ultra Prime | Experian CCR | 960 | Best rates; all products |
| BFS Tier 1 | Experian CCR | 800 | — |
| BFS Tier 2 | Experian CCR | 600 | — |
| BFS Tier 3 | Experian CCR | 550 | + 20% deposit |
| BFS Tier 4 | Experian CCR | 400 | + 20% deposit; no commercial used |
| BFS Plus | Experian CCR | 400 (consumer) / 550 (commercial used) | Passenger & LCV only |
| Westpac WEF | Not published | Satisfactory | Credit bureau + ASIC search |
| CFAL | Not published | Satisfactory | Credit bureau at credit discretion |

**Auto-decline triggers (BFS — no resubmission):**
- All individuals/guarantors CCR < 400 (consumer + commercial new/demo)
- All individuals/guarantors CCR < 550 (commercial used)
- Currently bankrupt

**Score band matching:**
- ≥ 960: BFS Ultra Prime; Westpac (satisfactory); Resimac PremiumPLUS (if ABN/property criteria met)
- 800–959: BFS Tier 1; Westpac; Resimac
- 600–799: BFS Tier 2; Westpac; Resimac Standard/Basic
- 550–599: BFS Tier 3 (+20% deposit); Resimac Lite/Full Doc (Company/Guarantor)
- 400–549: BFS Tier 4 (+20% deposit); Resimac at credit discretion
- < 400: BFS auto-decline; Westpac/CFAL at heavy credit discretion only

---

## chunk_id: eligibility_property_backing
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** PROPERTY_REQUIRED, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** PROPERTY_BACKED, NO_PROPERTY, RENTER, COMMERCIAL, CONSUMER
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "do I need to own property", "property owner", "renting", "no property", "property backed", "home owner", "residential property", "guarantor property"

**Content:**

| Lender | Property required? | Renter eligible? | Conditions if no property |
|--------|------------------|-----------------|--------------------------|
| Resimac PremiumPLUS | ✓ Mandatory | ✗ | Cannot access this tier |
| Resimac Premium | ✓ Mandatory | ✗ | Cannot access this tier |
| Resimac Standard | Optional | ✓ | Non-property-backed deposit: MV 10%, other 20% |
| Resimac Basic | Optional | ✓ | Non-property-backed deposit: MV 10%, other 20% |
| BFS (all tiers) | ✗ Not required | ✓ | No deposit impact from property status |
| Westpac (new client) | ✓ Required | ✗ | Cannot access DriveXpress, Replacement, Medical |
| Westpac (existing client) | ✗ Not required | ✓ | Relationship replaces property requirement |
| CFAL | Not specified | At discretion | Assessed case-by-case |

**Property-backed definition (Resimac):**
- ≥ 25% of property in guarantor's name
- Equity ≥ 1× NAF
- No multiple or adverse encumbrances on property
- Spouse-owned property: waives deposit but does not count as property backing; marriage (not de facto) required

**Key matching rule:**
- Renter, no property → BFS is the only clearly accessible lender across all tiers
- Renter approaching Westpac → existing client only
- Renter approaching Resimac → Standard or Basic tier only

---

## chunk_id: eligibility_residency_visa
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** VISA_HOLDER, COMMERCIAL, CONSUMER
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "visa holder", "non-resident", "permanent resident", "citizen", "temporary visa", "work visa", "overseas", "international borrower"

**Content:**

| Lender | Citizens/PR | Visa Holders | Conditions |
|--------|-----------|-------------|-----------|
| Resimac | ✓ Required (directors + >40% shareholders) | ✗ Not accepted | Must be AU Citizen or PR residing in Australia |
| BFS PRIME | ✓ | ✓ | Min income $100k p.a.; loan ends ≥ 1 month before visa expiry; Low Doc not available |
| BFS Plus | ✓ | ✓ | Min income $50k p.a.; loan ends ≥ 1 month before visa expiry |
| Westpac (Full Doc) | ✓ | ✓ | Loan term must end 1 month before visa expiry |
| Westpac Low Doc | ✓ | Not specified | — |
| CFAL | ✓ (implied) | At discretion | AML requirements apply |

**Driver licence (BFS):**
- Must be legally able to drive in Australia
- International licence: insurance evidence required at settlement
- Learner licence: accepted with co-borrower (passenger vehicles only)
- Interlock conditions: NOT accepted

---

## chunk_id: eligibility_discharged_bankrupt
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_CREDIT_SCORE
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** DISCHARGED_BANKRUPT, LOW_CREDIT
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "bankrupt", "discharged bankrupt", "bankruptcy", "Part IX", "debt agreement", "adverse credit", "default"

**Content:**

| Lender | Current Bankrupt | Discharged Bankrupt | Conditions |
|--------|-----------------|-------------------|-----------|
| Resimac | ✗ Excluded | ✗ Excluded | If discharged within last 10 years |
| BFS | ✗ Auto-decline | ✓ Accepted | 20% deposit; > 12 months post-discharge; no adverse history since; BFS Plus tier |
| Westpac | ✗ Excluded | At discretion | Not explicitly addressed |
| CFAL | ✗ Excluded (implied) | At discretion | Not explicitly addressed |

**RHI standards (BFS):**

| Tier | Last 3 months | Last 12 months |
|------|--------------|---------------|
| PRIME (Ultra–Tier 2) | No arrears | ≤ 30 days in arrears; no financial defaults |
| BFS Plus | ≤ 30 days in arrears | ≤ 60 days in arrears; no financial defaults |

---

## chunk_id: eligibility_tax_obligations
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_ABN
**lenders:** RESIMAC, WESTPAC, CFAL
**borrower_profile:** COMMERCIAL, SELF_EMPLOYED
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "ATO debt", "tax debt", "BAS arrears", "outstanding tax", "payment plan ATO", "tax compliance", "GST lodgements overdue"

**Content:**

| Lender | ATO Debt Policy | Payment Arrangement |
|--------|----------------|-------------------|
| Resimac Low Doc | Not assessed | — |
| Resimac Lite Doc | Debt must be < 10% of turnover | Must be in place > 3 months |
| Resimac Full Doc | ATO compliance assumed | — |
| Westpac (all) | Must be fully up to date | No arrangements permitted |
| CFAL (all) | Must be fully up to date | No arrangements permitted |
| BFS | Not explicitly stated | Assessed in income evaluation |

**Key rule:** If borrower has ATO debt with no arrangement → unlikely any lender will approve.
If debt < 10% turnover with active arrangement > 3 months → Resimac Lite Doc may be accessible.

---

## chunk_id: pricing_motor_vehicles_new
**layer:** 1
**intent:** PRICING
**policy_field:** BASE_RATE
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** COMMERCIAL, CONSUMER, NEW_CLIENT, EXISTING_CLIENT
**asset_class:** MV_NEW
**doc_type:** ALL
**trigger_words:** "rate for new car", "interest rate new vehicle", "new car finance rate", "demo car rate", "what rate new motor vehicle"

**Content:**

| Lender / Tier | Rate | Notes |
|--------------|------|-------|
| Resimac PremiumPLUS | 7.64% p.a. | Motor vehicles < 3 years |
| Resimac Premium/Standard/Basic | 7.89% p.a. | Motor vehicles < 3 years |
| BFS Commercial Ultra Prime | 7.60% base | + up to 6% broker margin |
| BFS Commercial Tier 1 | 8.25% base | Max rate 17.15% |
| BFS Commercial Tier 2 | 8.50% base | Max rate 17.15% |
| BFS Commercial Tier 3 | 10.15% base | Max rate 17.15% |
| BFS Commercial Tier 4 | 11.50% base | Max rate 17.15% |
| BFS Consumer Ultra Prime | 9.15% max | — |
| BFS Consumer Tier 1 | 9.29% max | — |
| BFS Consumer Tier 2 | 10.15% max | — |
| BFS Consumer Tier 3 | 11.50% max | — |
| BFS Consumer Tier 4 | 12.50% max | — |
| Westpac Xpress (dealer, ≤ 5 yrs) 24–48m | 7.75% | Fixed; brokerage up to 3% |
| Westpac Xpress (dealer, ≤ 5 yrs) 60m | 7.85% | — |
| Westpac Standard $20k–$50k 24–36m | 8.42% | Monthly repayments only |
| Westpac Standard $50k–$150k 24–36m | 8.32% | — |

**Lowest available rate (new car, dealer):** Westpac Xpress **7.75%** or Resimac PremiumPLUS **7.64%** (subject to full eligibility).

---

## chunk_id: pricing_motor_vehicles_used
**layer:** 1
**intent:** PRICING
**policy_field:** BASE_RATE, RISK_LOADING
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** MV_USED
**doc_type:** ALL
**trigger_words:** "rate for used car", "second hand car rate", "used vehicle interest rate", "2019 car rate", "2015 car rate", "used motor vehicle"

**Content:**

**Resimac (> 3 years old):**

| Tier | Rate |
|------|------|
| PremiumPLUS | 8.24% p.a. |
| Premium / Standard / Basic | 8.49% p.a. |

+2% risk loading if asset age > 16 years at end of term.

**BFS Commercial — Used (base rates):**

| Year Band | Ultra Prime | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|-----------|------------|--------|--------|--------|--------|
| 2022–2026 | 7.60% | 8.95% | 10.45% | 12.50% | N/A |
| 2017–2021 | N/A | 10.30% | 11.35% | 12.90% | N/A |
| 2016 & older | 9.55% | 11.05% | 11.80% | 13.40% | N/A |

**BFS Consumer — Used (max rates):**

| Year Band | Ultra Prime | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|-----------|------------|--------|--------|--------|--------|
| 2022–2026 | 9.15% | 9.75% | 10.55% | 12.00% | 13.20% |
| 2017–2021 | — | 10.35% | 11.35% | 12.25% | 13.70% |
| 2016 & older | 10.15% | 11.35% | 11.65% | 13.00% | 13.90% |

**Westpac Xpress (≤ 5 years old, dealer or private sale):**

| Channel | 24–48m | 60m |
|---------|--------|-----|
| Dealer | 7.75% | 7.85% |
| Private Sale | 8.17% | 8.37% |

Westpac Standard: used 4–10 years → add 0.75% to applicable new vehicle rate.

---

## chunk_id: pricing_electric_vehicles
**layer:** 1
**intent:** PRICING
**policy_field:** BASE_RATE, EV_DISCOUNT
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** EV
**doc_type:** ALL
**trigger_words:** "electric vehicle rate", "EV loan", "electric car finance", "Tesla finance rate", "EV interest rate", "green vehicle", "hybrid rate"

**Content:**

| Lender | EV Rate | Benefit vs ICE | Extra EV benefit |
|--------|--------|----------------|-----------------|
| Resimac PremiumPLUS | **7.54% p.a.** | –0.10% vs MV < 3 yrs | Loan term up to 84 months |
| Resimac Premium/Standard/Basic | **7.79% p.a.** | –0.10% vs MV < 3 yrs | Loan term up to 84 months |
| BFS | Same tiers as ICE | No separate discount published | Electric motorbikes accepted if > 80 km/h |
| Westpac Xpress dealer 24–48m | **6.75%** (7.75% – 1%) | –1.00% | — |
| Westpac Xpress dealer 60m | **6.85%** (7.85% – 1%) | –1.00% | — |
| Westpac Xpress private sale 24–48m | **7.17%** (8.17% – 1%) | –1.00% | — |
| Westpac Standard $50k–$150k 24–36m | **7.32%** (8.32% – 1%) | –1.00% | — |

**Lowest available EV rate:** Westpac Xpress dealer 24–48m **6.75%**
**Best EV loan term:** Resimac up to **84 months** (only lender with EV-specific term extension)

---

## chunk_id: pricing_heavy_equipment_primary
**layer:** 1
**intent:** PRICING
**policy_field:** BASE_RATE, RISK_LOADING
**lenders:** RESIMAC, WESTPAC
**borrower_profile:** COMMERCIAL
**asset_class:** PRIMARY, SECONDARY, TERTIARY
**doc_type:** ALL
**trigger_words:** "truck finance rate", "excavator loan rate", "heavy equipment interest rate", "primary asset rate", "forklift rate", "tractor rate", "agricultural equipment rate"

**Content:**

**Resimac:**

| Category | Age | PremiumPLUS | Premium/Standard/Basic |
|----------|-----|------------|----------------------|
| Primary | < 3 yrs | 8.39% | 8.64% |
| Primary | > 3 yrs | 9.29% | 9.54% |
| Secondary | Any | 12.39% | 12.64% |
| Tertiary | Any | 14.09% | 14.34% |

Prime movers: +2% risk loading; property-backed guarantor always required.

**Westpac Xpress (Category B heavy equipment):**

| Term | Rate |
|------|------|
| 24/36/48 months | 8.17% |
| 60 months | 8.37% |

**Westpac Standard (New Plant & Equipment):**

| Amount | 24–36m | 48m | 60m |
|--------|--------|-----|-----|
| $15k–$20k | 10.22% | 10.36% | 10.56% |
| $20k–$50k | 8.72% | 8.86% | 9.06% |
| $50k–$150k | 8.52% | 8.62% | 8.82% |
| $150k+ | By negotiation | — | — |

EV equipment: –1% on all above rates.

---

## chunk_id: pricing_private_sale_loading
**layer:** 1
**intent:** PRICING
**policy_field:** PRIVATE_SALE_LOADING
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** MV_USED, MV_NEW
**doc_type:** ALL
**trigger_words:** "private sale rate", "buying from private seller", "private seller loan", "buying from individual", "not from dealer", "private purchase finance"

**Content:**

| Lender | Rate Impact | Extra Requirements | Asset Restriction |
|--------|------------|-------------------|------------------|
| Resimac | +2% risk loading | — | — |
| BFS | +0.50% | DoxAI or Redbook inspection; arm's length transaction | — |
| Westpac Xpress | Separate rate tier (e.g. 8.17% vs 7.75%) | Inspection may apply | Category A only (MV/LCV) |
| Westpac Standard | Unchanged | Inspection may apply | — |
| CFAL | Not specified | — | MV/LCV only |

---

## chunk_id: loan_limits_overview
**layer:** 1
**intent:** LOAN_LIMITS
**policy_field:** MAX_LOAN
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "how much can I borrow", "maximum loan", "loan limit", "borrow $300k", "borrow $500k", "maximum finance amount", "loan cap"

**Content:**

| Lender | Doc Type | Standard Max | Extended Max | Notes |
|--------|---------|-------------|-------------|-------|
| Resimac PremiumPLUS | Full Doc | $450k NAF | — | Per asset |
| Resimac Standard | Full Doc | $400k NAF | — | — |
| Resimac Basic | Full Doc | $200k NAF | — | — |
| BFS PRIME | Standard | $250k | $400k (high value, 20% deposit, Tier 1–2) | — |
| BFS PRIME | Private sale | $150k | — | — |
| BFS Plus | Any | $100k | — | — |
| Westpac New-to-Bank | DriveXpress | $150k | — | Property + $75k income |
| Westpac Existing Client | DriveXpress | $500k (Cat C) | — | 12m WEF history |
| CFAL | Full Doc | Case-by-case | $1m+ possible | Size drives docs |

Individual asset caps (Resimac): passenger vehicle $250k; motorbike $75k.
Westpac LVR: maximum 120% for no-deposit applications; Glass's Retail Value for used.

---

## chunk_id: loan_limits_new_business
**layer:** 1
**intent:** LOAN_LIMITS
**policy_field:** MAX_LOAN, MIN_ABN
**lenders:** BFS, WESTPAC, RESIMAC
**borrower_profile:** NEW_BUSINESS, ABN_UNDER_1YR, ABN_1_2YR, COMMERCIAL
**asset_class:** ALL
**doc_type:** NEW_BIZ, FULL_DOC
**trigger_words:** "new business loan", "just started business", "startup loan", "new ABN loan", "less than 2 years business"

**Content:**

| Lender | ABN Requirement | Max Loan | Conditions |
|--------|----------------|---------|-----------|
| BFS New Business Ventures | < 12 months | $100k total exposure | 90-day bank statements; 20% deposit for Tier 3–4 |
| BFS Full Doc | 12+ months | $250k | — |
| Westpac New-to-Bank | > 2 years | $150k (DriveXpress) | Own residential property + $75k income |
| Resimac Basic | > 1 year | $100k–$200k | ABN + GST; all standard criteria |

---

## chunk_id: loan_limits_high_value
**layer:** 1
**intent:** LOAN_LIMITS
**policy_field:** MAX_LOAN, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** HIGH_CREDIT, PROPERTY_BACKED, COMMERCIAL, EXISTING_CLIENT
**asset_class:** ALL
**doc_type:** FULL_DOC
**trigger_words:** "borrow more than $250k", "large loan equipment", "$300k loan", "$400k loan", "$500k finance", "high value loan"

**Content:**

| Lender | Range | Requirements |
|--------|-------|-------------|
| Resimac PremiumPLUS/Premium | Up to $450k NAF | ABN > 4–6 yrs; property-backed; Full Doc |
| Resimac (SME exposure) | Up to $500k total | All standard criteria |
| BFS High Value | $250k–$400k | Ultra Prime–Tier 2; 20% deposit; asset-backed; case-by-case |
| Westpac Existing (Cat C) | Up to $500k | 12m WEF history; DriveXpress |
| Westpac Replacement Existing | Up to $650k (B&C) | 12m history; replacement criteria |
| CFAL | $500k–$1m+ | 3 years financials; ATO portal; full documentation |

---

## chunk_id: documentation_low_doc
**layer:** 1
**intent:** DOCUMENTATION
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** SELF_EMPLOYED, COMMERCIAL, NEW_CLIENT
**asset_class:** ALL
**doc_type:** LOW_DOC, LITE_DOC
**trigger_words:** "low doc", "no financials", "without tax return", "minimal paperwork", "self-employed no financials", "lite doc", "reduced documentation"

**Content:**

| Lender | Product | Min Documents | Max Loan | Eligibility Gate |
|--------|---------|--------------|---------|-----------------|
| Resimac Low Doc | Low Doc | Application + A&L Statement | $300k (PremiumPLUS) | All tiers; not Tertiary |
| Resimac Lite Doc | Lite Doc | + ATO portals + BAS | $300k (PremiumPLUS) | ATO debt < 10% turnover; payment plan > 3m |
| BFS | Commercial Low Doc | Business Financial Declaration | $150k total exposure | 2+ yrs ABN+GST; Ultra Prime–Tier 2; Guarantor = AU citizen/PR |
| Westpac | DriveXpress | Affordability Declaration + credit check | $150k new client / $500k existing | > 2 yrs ABN+GST; statutory obligations current |
| CFAL | None | 2 yrs financials minimum | — | Not available |

---

## chunk_id: documentation_full_doc
**layer:** 1
**intent:** DOCUMENTATION
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** FULL_DOC
**trigger_words:** "what documents do I need", "full application", "financials required", "tax return loan", "financial statements", "what paperwork", "bank statements loan"

**Content:**

**By loan size — minimum financial documentation:**

| Size Band | Resimac | BFS Commercial | Westpac Standard | CFAL |
|-----------|---------|---------------|-----------------|------|
| < $100k | Full Doc: BAS + ATO portal + financials | 90-day bank statements | 90-day bank statements | 2 yrs financials + 2 yrs ITR |
| $100k–$250k | 2 yrs financials (P&L + balance sheet) ≤ 18m | 2 yrs signed externally prepared financials | Evidence of income | 2 yrs financials + 2 yrs ITR + ATO portal |
| $250k–$500k | 2 yrs financials + ATO portal + commitment schedule | 2 yrs signed financials | By negotiation | 3 yrs financials + ATO portal + aged debtor list |
| $500k–$1m | 3 yrs financials + commentary on movements ≥ 10% | — | — | + Interim accounts if year-end > 6m old |
| > $1m | 3 yrs financials + cash flow projections | — | — | + Cash flow projections + succession plan + competitor list |

---

## chunk_id: asset_motor_vehicles_eligibility
**layer:** 1
**intent:** ASSET_ELIGIBILITY
**policy_field:** ASSET_AGE_MAX
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** MV_NEW, MV_USED, EV, LCV, MOTORBIKE, CARAVAN
**doc_type:** ALL
**trigger_words:** "can I finance a car", "vehicle finance eligibility", "what cars can I finance", "ute loan", "van finance", "light commercial vehicle loan", "motorbike loan", "caravan finance"

**Content:**

| Vehicle Type | Resimac | BFS PRIME | BFS Plus | Westpac | CFAL |
|-------------|---------|----------|---------|---------|------|
| Passenger cars | ✓ | ✓ | ✓ | ✓ Cat A | ✓ |
| Vans/utes < 4.5T | ✓ | ✓ | ✓ | ✓ Cat A | ✓ |
| Electric vehicles | ✓ (best rate) | ✓ | ✓ | ✓ (–1%) | — |
| Motorbikes | ✓ max $75k | ✓ | — | Limited | — |
| Caravans | ✓ Primary | ✓ | — | Limited | — |
| Campervans | — | ✓ | — | Limited | — |
| Classic cars | ✓ +2% | — | — | — | — |
| Ride-share/hire | ✗ Excluded | ⚠ Limited | ⚠ Limited | ⚠ Limited | — |

**Maximum vehicle age:**

| Lender | Max at Start of Term | Max at End of Term |
|--------|--------------------|--------------------|
| Resimac | Not specified | 25 years (motor vehicles) |
| BFS PRIME | 15 yrs (≤ 60m term); 7 yrs (> 60m term) | — |
| BFS Plus | 15 years | — |
| Westpac | 15 years (Xpress Cat A) | — |

---

## chunk_id: asset_heavy_equipment_eligibility
**layer:** 1
**intent:** ASSET_ELIGIBILITY
**policy_field:** ASSET_AGE_MAX
**lenders:** RESIMAC, WESTPAC, CFAL
**borrower_profile:** COMMERCIAL
**asset_class:** PRIMARY, SECONDARY, TERTIARY
**doc_type:** ALL
**trigger_words:** "truck finance", "excavator loan", "forklift finance", "crane loan", "heavy machinery loan", "construction equipment finance", "tractor loan", "agricultural machinery"

**Content:**

| Asset Type | Resimac | Westpac | CFAL | BFS |
|-----------|---------|---------|------|-----|
| Heavy trucks > 4.5T | ✓ Primary | ✓ Cat B (≤ 5 yrs, dealer) | ✓ | ✗ |
| Trailers | ✓ Primary | ✓ Cat B | ✓ | ✗ |
| Forklifts / telehandlers | ✓ Primary | ✓ Cat B | ✓ | ✗ |
| Excavators / skid steers | ✓ Primary | ✓ Cat B | ✓ | ✗ |
| Cranes (mobile/tight access) | ✓ Primary | ✓ Cat B (≤ **3 yrs**) | ✓ | ✗ |
| Prime movers | ✓ +2% loading | — | — | ✗ |
| Tractors / harvesters | ✓ Primary | ✓ Cat C (≤ 7 yrs, dealer) | ✓ | ✗ |
| Medical equipment | — | ✓ Medical channel | ✓ | ✗ |
| Generators/compressors | ✓ Secondary | — | ✓ | ✗ |
| AV / conveyors | ✓ Tertiary | — | — | ✗ |

**Maximum asset age by category (start of term):**

| Lender | Category | Max Age |
|--------|---------|--------|
| Resimac | Primary (end of term) | 25 years |
| Resimac | Secondary (end of term) | 10 years |
| Resimac | Tertiary (end of term) | 5 years |
| Westpac | Cat B heavy equipment | 5 years |
| Westpac | Cranes | 3 years |
| Westpac | Cat C agriculture | 7 years |

---

## chunk_id: asset_excluded_items
**layer:** 1
**intent:** EXCLUSIONS
**policy_field:** ASSET_AGE_MAX
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "can I finance gym equipment", "software loan", "office furniture loan", "food truck finance", "livestock loan", "what can't be financed", "excluded assets"

**Content:**

**Excluded across multiple lenders:**

| Asset | Resimac | BFS | Westpac | CFAL |
|-------|---------|-----|---------|------|
| Ride-share / taxis | ✗ | ⚠ Limited | ⚠ Limited | — |
| IT hardware / computers | ✗ | — | ✗ (excl. from plant rates) | — |
| Office furniture | ✗ | — | — | — |
| Livestock | ✗ | — | — | — |
| Software / intangibles | ✗ | — | — | — |
| Gym equipment | ✗ | — | — | — |
| Hospitality equipment | ✗ | — | — | — |
| Food trucks | ✗ | — | — | — |
| Artwork | ✗ | — | — | — |
| Fixtures and fittings | ✗ | — | ✗ | — |
| Novated leases | — | — | ✗ | — |
| Sale and leaseback | — | ✗ | ✗ | — |
| Debt consolidation | — | ✗ | — | — |
| Cash raising / top-up | — | ✗ | — | — |

---

## chunk_id: settlement_universal
**layer:** 1
**intent:** SETTLEMENT
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "settlement documents", "what do I need to settle", "finalise loan", "PPSR", "insurance settlement", "sign loan documents", "Certificate of Currency"

**Content:**

**Universal settlement checklist:**

| Requirement | Resimac | BFS | Westpac |
|------------|---------|-----|---------|
| Signed loan documents | ✓ | ✓ (QuickSell) | ✓ (DriveOnline) |
| Asset insurance (lender as interested party) | ✓ | ✓ (loaded in QuickSell) | ✓ |
| PPSR registration | ✓ (at cost) | ✓ ($6) | ✓ |
| Tax invoice or private sale agreement | ✓ | ✓ | ✓ |
| Biometric verification | — | ✓ | ✓ |
| Certificate of Currency (CoC) | ✓ ($100k+ assets) | — | ✓ ($150k+ assets) |

**Westpac settlement updates (effective 24 February 2025):**
- PPSR: motor vehicles with VIN in buyback/private sale no longer need PPSR company search over seller. VIN search day-of must show no other registration.
- CoC: fleet policies no longer need to list specific VIN/serial number (motor vehicles only).

---

## chunk_id: special_programs_rollover_replacement
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** MAX_LOAN, MIN_ABN
**lenders:** WESTPAC, RESIMAC
**borrower_profile:** EXISTING_CLIENT, COMMERCIAL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "refinance equipment loan", "roll over contract", "extend loan", "replace existing finance", "refinance truck loan", "switch lender"

**Content:**

**Westpac Rollover:**
- Existing clients only (12m+ WEF history)
- Westpac original: max $500k, all assets; Other financier: max $250k, Cat A&B (inspection required)
- Contract must have been operating > 12 months; borrower/security same as original

**Westpac Replacement:**
- New client: max $150k (A&B), must own property
- Existing client: max $650k (B&C)
- Monthly repayment ≤ 125% (new) or 150% (existing) of payment being replaced
- Contract being replaced: operating ≥ 12 months; finalised within 6 months / on settlement

**Resimac Sale and Buyback:**
- PremiumPLUS or Premium only; dealership sales; asset purchased within 30 days; case-by-case

**BFS — excluded refinance types:** Mid-term refinancing, sale and leaseback, top-up loans, cash raising.

---

## chunk_id: special_programs_medical
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** MAX_LOAN
**lenders:** WESTPAC
**borrower_profile:** MEDICAL_PROFESSIONAL, COMMERCIAL
**asset_class:** MEDICAL_EQUIP, OFFICE_EQUIP, MV_NEW
**doc_type:** ALL
**trigger_words:** "doctor loan", "medical professional finance", "GP equipment loan", "dental equipment finance", "vet loan", "allied health loan", "medical equipment finance"

**Content:**

**Eligible professions:**
- Medical Specialist, GP, Dental, Vet (higher limits)
- Allied Health: OT, Optometrist, Osteopath, Physiotherapist, Chiropractor, Audiologist, Pathology, Podiatrist, Psychologist, Speech Pathologist
- Excluded: Pharmacists

**Limits:**

| Asset | Specialist/GP/Dental/Vet | Allied Health |
|-------|------------------------|--------------|
| Motor vehicle (≤ 5 yrs) | < $250k | < $150k |
| New office equipment | < $150k | < $150k |
| New medical equipment | < $350k | < $150k |
| Max cumulative | < $500k | < $250k |

**Conditions:** > 2 yrs in business + GST; new clients must own property + $75k income; sale & hire back within 30 days permitted; Affordability Declaration required.

---

## chunk_id: special_programs_ev_extended
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** MAX_TERM, EV_DISCOUNT
**lenders:** RESIMAC
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** EV
**doc_type:** ALL
**trigger_words:** "84 month loan", "7 year EV loan", "longer term electric vehicle", "green goods loan", "extended term EV"

**Content:**

- Resimac only lender offering 84-month terms specifically for Green Goods (EV/sustainable assets)
- Standard max term: 60 months; Green Goods: up to 84 months
- Combined benefits: 7.54% rate (PremiumPLUS) + 84-month term = lowest rate + longest term in the group
- BFS PRIME standard max term: 84 months (not EV-specific)
- Westpac standard max: 84 months; Medical buses Cat C: up to 10 years

---

## chunk_id: fees_comparison
**layer:** 1
**intent:** FEES
**policy_field:** BROKERAGE_MAX
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "fees", "setup fee", "establishment fee", "monthly fee", "early repayment fee", "break cost", "what does it cost", "brokerage fee"

**Content:**

**Establishment fees:**

| Lender | Consumer | Commercial | Private Sale Premium |
|--------|---------|-----------|---------------------|
| Resimac | — | $495 | +$200 ($695 total) |
| BFS | $525 | $575 | +$100 |
| Westpac | Not published | Not published | — |
| CFAL | Not published | Not published | — |

**Ongoing fees:**

| Lender | Monthly | Fortnightly | Weekly |
|--------|---------|------------|--------|
| Resimac | $4.95 | — | — |
| BFS | $10.00 | $4.62 | $2.31 |

**Early termination:**

| Lender | Admin Fee | Additional |
|--------|----------|-----------|
| BFS Consumer | $70 | Up to $750 (reduces by $12/month paid) |
| BFS Commercial | $85 | 35% of remaining interest (15% if refinancing with BFS) |

**Brokerage:**

| Lender | Standard | Cap | Above cap |
|--------|---------|-----|----------|
| Resimac | Up to 5.5% no rate impact | 8.8% | +0.5% rate per 1% extra brokerage |
| BFS | Origination fee max $1,650 | — | 75% overs net of GST |
| Westpac Xpress | Up to 3% | 3% | — |
| Westpac Standard | Up to 3% | 4% (by negotiation) | — |

═══════════════════════════════════════════════════════════════════
# LAYER 2 — CROSS-LENDER COMPARISON MATRIX
# Purpose: answer "compare X vs Y" queries directly
# Each chunk = one policy dimension, all lenders side by side
═══════════════════════════════════════════════════════════════════

---

## chunk_id: compare_tier_logic
**layer:** 2
**intent:** COMPARE
**policy_field:** MIN_ABN, MIN_CREDIT_SCORE, PROPERTY_REQUIRED
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** ALL
**trigger_words:** "compare lenders", "which lender is better", "difference between lenders", "how do lenders compare", "compare Resimac BFS Westpac"

**Content:**

The four lenders use fundamentally different logic to tier and assess borrowers.

| Dimension | Resimac | BFS | Westpac WEF | CFAL |
|-----------|---------|-----|-------------|------|
| **Primary tier driver** | Property-backing type × ABN duration | Experian CCR credit score | Relationship history with bank | Transaction size |
| **Serves consumers?** | ✗ Commercial only | ✓ Commercial + individual | ✗ Commercial only | ✗ Commercial only |
| **Serves new businesses?** | ✓ Basic tier (ABN > 1 yr) | ✓ New Business Ventures (< 12m) | ✓ New-to-Bank (with property) | ✓ With full docs |
| **Sub-prime tolerance** | Medium — Basic tier accessible | Highest — CCR 400 accepted | Low-medium — relationship or property required | Low — no sub-prime channel |
| **Discharged bankrupt** | ✗ Excluded (10 yr rule) | ✓ Accepted (conditions) | At discretion | At discretion |
| **Consumer accessible?** | ✗ | ✓ | ✗ | ✗ |
| **Simplified Doc option** | ✓ Low / Lite Doc | ✓ Commercial Low Doc | ✓ DriveXpress | ✗ |
| **Asset breadth** | Widest (4 asset categories) | Narrowest (MV only) | Broad (A/B/C + Medical) | Broad (equipment) |
| **EV incentive** | ✓ Lowest rate + 84m term | ✓ Same rate tiers | ✓ –1% rate reduction | Not specified |
| **Max standard loan** | $450k NAF | $250k | $500k+ (existing) | Case-by-case |
| **Private sale allowed?** | ✓ (+2% loading) | ✓ (+0.50%) | ✓ Cat A only (+rate tier) | ✓ MV only |
| **Ride-share vehicles** | ✗ Excluded | ⚠ Limited | ⚠ Limited | — |

---

## chunk_id: compare_interest_rates
**layer:** 2
**intent:** COMPARE
**policy_field:** BASE_RATE, EV_DISCOUNT, RISK_LOADING
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** ALL
**trigger_words:** "compare rates", "which lender has the lowest rate", "best rate", "rate comparison", "who is cheapest", "lowest interest rate"

**Content:**

**Rate comparison — best available rate per asset type:**

| Asset Type | Lowest Available Rate | Lender | Conditions |
|-----------|----------------------|--------|-----------|
| New car (dealer) | **7.64%** | Resimac PremiumPLUS | ABN > 6 yrs; property-backed |
| New car (dealer, fast) | **7.75%** | Westpac Xpress | > 2 yrs ABN; satisfactory credit |
| New car (consumer) | **9.15%** | BFS Ultra Prime | CCR ≥ 960 |
| Used car 2022–2026 (dealer) | **7.75%** | Westpac Xpress | ≤ 5 yrs old |
| Used car 2017–2021 | **8.49%** | Resimac Premium/Standard/Basic | — |
| Used car 2016 & older | **9.55%** | Resimac PremiumPLUS | — |
| Electric vehicle (dealer) | **6.75%** | Westpac Xpress (–1%) | ≤ 5 yrs old |
| Electric vehicle (Resimac) | **7.54%** | Resimac PremiumPLUS | + 84-month term |
| Heavy equipment (dealer) | **8.17%** | Westpac Xpress Cat B | ≤ 5 yrs old |
| Heavy equipment (Resimac primary) | **8.39%** | Resimac PremiumPLUS | < 3 yrs old |
| Secondary assets | **12.39%** | Resimac PremiumPLUS | — |
| Tertiary assets | **14.09%** | Resimac PremiumPLUS | — |

**Rate structure differences:**
- Resimac: flat rates by tier and asset category — borrower sees exact rate upfront
- BFS commercial: base rate + broker margin (up to +6%) — borrower may not see actual rate until offer
- BFS consumer: published maximum rates — actual rate can be lower
- Westpac: fixed rates by channel — transparent but less flexible

---

## chunk_id: compare_documentation_effort
**layer:** 2
**intent:** COMPARE
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** SELF_EMPLOYED, COMMERCIAL
**trigger_words:** "easiest application", "least paperwork", "simplest lender", "compare document requirements", "which lender asks for less"

**Content:**

**Documentation burden ranking (least to most):**

| Rank | Lender / Channel | What's required | Suitable for |
|------|-----------------|----------------|-------------|
| 1 (easiest) | Westpac DriveXpress | Affordability Declaration + credit check only | Existing clients or new clients with property, 2+ yr ABN |
| 2 | Resimac Low Doc | Application + Asset & Liability Statement | All tiers; up to $300k |
| 3 | BFS Commercial Low Doc | Business Customer Financial Declaration | 2+ yr ABN+GST; up to $150k; Ultra Prime–Tier 2 |
| 4 | Resimac Lite Doc | Low Doc + ATO portal + 2 BAS statements | ATO debt < 10% turnover |
| 5 | BFS Full Doc (≤ $100k) | 90-day bank statements | Standard commercial |
| 6 | BFS New Business Ventures | 90-day bank statements + (run contract for couriers) | < 12 months ABN |
| 7 | Resimac Full Doc | Full financials + ATO + bank statements | Standard |
| 8 | BFS Full Doc (> $100k) | 2 years externally prepared financials | Larger loans |
| 9 | CFAL (all sizes) | 2 years financials minimum; scales to 3 yrs + projections for > $500k | All commercial |
| 10 (hardest) | CFAL > $1m | Full package including cash flow projections, succession plan, competitor list | Large transactions |

---

## chunk_id: compare_loan_amounts
**layer:** 2
**intent:** COMPARE
**policy_field:** MAX_LOAN, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** ALL
**trigger_words:** "compare loan amounts", "who lends more", "highest loan limit", "maximum borrowing comparison", "which lender has higher limits"

**Content:**

| Borrower Profile | Best Lender | Max Available | Notes |
|----------------|------------|--------------|-------|
| New business < 12m ABN | BFS | $100k | New Business Ventures |
| ABN 1–2 yrs, renting | BFS Full Doc | $250k | — |
| ABN 2+ yrs, no property | BFS / Westpac existing | $250k / $500k | Westpac if existing client |
| ABN 2+ yrs, property owned | Westpac / Resimac | $500k / $450k | Westpac existing client |
| ABN 4–6 yrs, property | Resimac Premium | $450k NAF | Full Doc |
| ABN 6+ yrs, property | Resimac PremiumPLUS | $450k NAF per asset / $500k total | — |
| Large corporate / equipment > $500k | CFAL | $1m+ | Full documentation required |
| High-value vehicle ≥ $250k, high credit | BFS High Value | $400k | Ultra Prime–Tier 2; 20% deposit |

═══════════════════════════════════════════════════════════════════
# LAYER 3 — RECOMMENDATION ENGINE
# Purpose: answer "which lender suits me?" queries
# Each chunk = a borrower scenario with scored lender recommendations
═══════════════════════════════════════════════════════════════════

---

## chunk_id: recommend_new_business_car
**layer:** 3
**intent:** RECOMMEND
**policy_field:** MIN_ABN, BASE_RATE, MAX_LOAN
**lenders:** BFS, WESTPAC, RESIMAC
**borrower_profile:** NEW_BUSINESS, ABN_UNDER_1YR, ABN_1_2YR, COMMERCIAL
**asset_class:** MV_NEW, MV_USED, LCV
**trigger_words:** "new business car loan", "just started business vehicle", "startup car finance", "new ABN car loan", "which lender for new business"

**Content:**

**Scenario:** Borrower has < 2 years ABN and needs a vehicle for business use.

**Recommendation matrix:**

| ABN Duration | Recommended Lender | Product | Max Loan | Key Condition |
|-------------|-------------------|---------|---------|--------------|
| < 12 months | **BFS** | New Business Ventures | $100k | 90-day bank statements; CCR ≥ 400; 20% deposit if Tier 3–4 |
| 12–24 months | **BFS** | Full Doc | $250k | CCR ≥ 400; standard documentation |
| 12–24 months (property owner) | **Westpac** | DriveXpress New-to-Bank | $150k | Own residential property; income ≥ $75k; > 2 yrs ABN needed |
| 1–2 years | **Resimac Basic** | Low Doc | $100k–$200k | ABN > 1 yr; GST > 1 yr; credit score ≥ 600 (company) |

**Why not CFAL?** CFAL requires ABN ≥ 2 years and full financial documentation for all sizes.
**Why not Westpac (< 2 yrs ABN)?** Westpac requires > 2 years ABN for all channels.

---

## chunk_id: recommend_renter_no_property
**layer:** 3
**intent:** RECOMMEND
**policy_field:** PROPERTY_REQUIRED, BASE_RATE, MAX_LOAN
**lenders:** BFS, RESIMAC, WESTPAC
**borrower_profile:** NO_PROPERTY, RENTER, COMMERCIAL, CONSUMER
**asset_class:** ALL
**trigger_words:** "renting no property loan", "no property vehicle finance", "renter equipment loan", "don't own home equipment finance", "tenant business loan"

**Content:**

**Scenario:** Borrower is renting, does not own property, needs business or personal vehicle/equipment finance.

| Lender | Accessible? | Tier / Product | Notes |
|--------|-----------|---------------|-------|
| **BFS** | ✓ Best option | Any tier based on CCR score | No property requirement at any tier |
| Resimac | ✓ Limited | Standard or Basic only | Non-property-backed deposit: MV 10%, other 20% |
| Westpac (new client) | ✗ | Not accessible | Requires residential property for new-to-bank |
| Westpac (existing client) | ✓ | All channels | Relationship replaces property requirement |
| CFAL | ✓ At discretion | All sizes | Property not explicitly required; case-by-case |

**Recommendation:** BFS is the primary lender for borrowers with no property. CCR score determines tier and rate.

---

## chunk_id: recommend_low_credit_score
**layer:** 3
**intent:** RECOMMEND
**policy_field:** MIN_CREDIT_SCORE, DEPOSIT_REQUIRED
**lenders:** BFS, RESIMAC, WESTPAC
**borrower_profile:** LOW_CREDIT, MID_CREDIT, DISCHARGED_BANKRUPT
**asset_class:** MV_NEW, MV_USED, LCV
**trigger_words:** "bad credit car loan", "low credit score vehicle finance", "poor credit history equipment loan", "credit issues finance", "impaired credit"

**Content:**

**Scenario:** Borrower has a low credit score or adverse credit history.

| Score Range | Best Lender | Product | Rate Range | Conditions |
|------------|------------|---------|-----------|-----------|
| 960+ | BFS Ultra Prime / Resimac PremiumPLUS | Standard | 7.54–7.60% | Full eligibility required |
| 800–959 | BFS Tier 1 / Resimac Premium | Standard | 7.64–8.95% | — |
| 600–799 | BFS Tier 2 / Resimac Standard | Standard | 7.89–11.35% | — |
| 550–599 | **BFS Tier 3** | Standard + 20% deposit | 10.15–12.90% (commercial) | 20% deposit required |
| 400–549 | **BFS Tier 4** | Standard + 20% deposit | 11.50%+ (commercial new) | No commercial used contracts |
| < 400 | — | Auto-declined by BFS | — | Westpac/CFAL at heavy credit discretion only |
| Discharged bankrupt | **BFS Plus** | Restricted products | Up to 17.15% | 20% deposit; > 12m post-discharge; no adverse history since |

**Note:** Resimac minimum Equifax score: Sole Trader 650 (Low Doc), 600 (Full Doc); Company 600 (Low Doc), 550 (Full Doc). Scores below these thresholds require referral.

---

## chunk_id: recommend_high_value_loan
**layer:** 3
**intent:** RECOMMEND
**policy_field:** MAX_LOAN, DEPOSIT_REQUIRED, MIN_ABN
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**borrower_profile:** HIGH_CREDIT, PROPERTY_BACKED, COMMERCIAL, EXISTING_CLIENT
**asset_class:** ALL
**trigger_words:** "large loan recommendation", "which lender for $300k", "who lends $500k", "large equipment finance lender", "high value loan lender"

**Content:**

**Scenario:** Borrower needs finance above $250k.

| Amount | Best Lender | Conditions |
|--------|------------|-----------|
| $250k–$400k (vehicle) | **BFS High Value** or **Resimac PremiumPLUS** | BFS: CCR ≥ 800, 20% deposit; Resimac: ABN > 6 yrs, property-backed |
| $250k–$450k (equipment) | **Resimac Premium/PremiumPLUS** | Full Doc; property-backed; ABN > 4–6 yrs |
| $400k–$500k | **Westpac existing client** | 12m+ WEF history; DriveXpress Cat C |
| $500k–$1m | **CFAL** or **Westpac by negotiation** | CFAL: 3 years financials; Westpac: case-by-case |
| > $1m | **CFAL** | Full financial package including projections and succession plan |

---

## chunk_id: recommend_best_ev_lender
**layer:** 3
**intent:** RECOMMEND
**policy_field:** BASE_RATE, EV_DISCOUNT, MAX_TERM
**lenders:** RESIMAC, BFS, WESTPAC
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** EV
**trigger_words:** "best lender for electric vehicle", "EV loan recommendation", "which lender for Tesla", "electric vehicle finance comparison", "green vehicle loan"

**Content:**

**Scenario:** Borrower wants to finance an electric vehicle and wants the best overall deal.

| Priority | Best Lender | Rate | Term | Why |
|---------|------------|------|------|-----|
| Lowest rate | **Westpac Xpress** | 6.75% (dealer, 24–48m) | Up to 60m | –1% EV discount; fast approval via DriveXpress |
| Lowest rate + longest term | **Resimac PremiumPLUS** | 7.54% | Up to **84 months** | Only lender with extended 84m term for green goods |
| Consumer borrower | **BFS Consumer** | From 9.15% (Ultra Prime) | Up to 84m | Only lender accepting personal (non-ABN) borrowers |
| Low credit score | **BFS Tier 3–4** | 10.15–12.50% | Up to 84m | No property required; CCR 400 accepted |
| Flexible eligibility | **BFS** | Varies by tier | Up to 84m | No property; accepts sub-prime; commercial + consumer |

**Combined recommendation:** If borrower qualifies for Westpac (> 2 yrs ABN, existing client or property owner), Westpac Xpress is cheapest. If borrower wants longest term or has no property, Resimac (PremiumPLUS) or BFS is preferred.

═══════════════════════════════════════════════════════════════════
# LAYER 4 — POLICY DIFFERENCE ANALYSIS
# Purpose: answer "how do these lenders differ on X?" queries
# Each chunk = one policy dimension, delta-focused
═══════════════════════════════════════════════════════════════════

---

## chunk_id: diff_tier_logic
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** MIN_ABN, MIN_CREDIT_SCORE, PROPERTY_REQUIRED
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**trigger_words:** "how do lenders tier customers differently", "what makes each lender different", "tier comparison", "eligibility differences between lenders"

**Content:**

**Core difference: what each lender uses as its primary filter**

| Lender | Primary Filter | Why it matters |
|--------|--------------|---------------|
| Resimac | Property-backing type + ABN duration | Borrowers without property are locked out of top 2 tiers regardless of credit score or income |
| BFS | Experian CCR score alone | Most meritocratic; a borrower with CCR 960 and 6 months ABN can access better rates than a 10-year business with CCR 550 at Resimac |
| Westpac WEF | Relationship history with Westpac bank | Rewards loyalty; new clients with no Westpac relationship face strict eligibility even with good credit |
| CFAL | Transaction size | No customer tiering; documentation scales with deal size; all commercial borrowers treated the same until proven otherwise |

**The single biggest eligibility difference:**
Resimac and Westpac (new client) both require property ownership at their top tiers. BFS does not require property at any tier. This is the most important differentiator for borrowers who rent or do not own property.

---

## chunk_id: diff_private_sale_policy
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** PRIVATE_SALE_LOADING, ASSET_AGE_MAX
**lenders:** RESIMAC, BFS, WESTPAC
**trigger_words:** "private sale differences", "buying privately lender comparison", "which lender is better for private sale", "private seller policy differences"

**Content:**

| Aspect | Resimac | BFS | Westpac |
|--------|---------|-----|---------|
| Rate loading | **+2.00%** | **+0.50%** | Separate (higher) rate tier |
| Asset types allowed | All asset classes | All vehicle types | Category A only (passenger car / LCV < 4.5T) |
| Inspection required? | No | ✓ DoxAI or Redbook | ✓ May be required |
| Max loan (private sale) | Per standard limits | $150k | Category A standard limits |
| Fee premium | $200 extra ($695 total) | $100 extra ($675 total) | — |

**Delta summary:**
- BFS has the smallest private sale rate loading (+0.50%) and allows all vehicle types
- Westpac has the narrowest private sale scope (Category A only) but competitive Xpress rate tier
- Resimac carries the highest private sale loading (+2%) but no inspection requirement

---

## chunk_id: diff_ev_policy
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** EV_DISCOUNT, MAX_TERM, BASE_RATE
**lenders:** RESIMAC, BFS, WESTPAC
**trigger_words:** "EV policy differences", "electric vehicle lender comparison", "which lender is better for EV", "compare EV rates", "electric car loan differences"

**Content:**

| Aspect | Resimac | BFS | Westpac |
|--------|---------|-----|---------|
| EV rate mechanism | Separate lower rate category | Same rate table as ICE (no explicit EV discount published) | –1% applied to all standard rates |
| Best EV rate | 7.54% (PremiumPLUS) | 7.60% (Ultra Prime commercial) | **6.75%** (Xpress dealer 24–48m) |
| EV extended term | ✓ **84 months** (Green Goods) | 84 months (standard, not EV-specific) | 84 months (standard) |
| Electric motorbikes | Accepted (Motor Vehicles) | ✓ Accepted if speed > 80 km/h | Limited |
| Consumer EV | ✗ Commercial only | ✓ Consumer + commercial | ✗ Commercial only |

**Delta summary:**
- Westpac offers the lowest EV rate in absolute terms (6.75%)
- Resimac is the only lender to extend the loan term specifically for EV/green goods (84 months)
- BFS is the only lender allowing individual consumers to finance EVs

---

## chunk_id: diff_documentation_by_lender
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**trigger_words:** "document requirements difference", "which lender needs less paperwork", "documentation comparison lenders", "easiest lender to apply", "most paperwork required"

**Content:**

**What each lender uniquely requires vs the others:**

| Lender | Unique requirement | Not required by others |
|--------|-------------------|----------------------|
| Resimac | Privacy consent must note specific URL (resimacassetfinance.com.au); signed < 90 days | BFS/Westpac/CFAL do not specify URL |
| Resimac Lite Doc | BAS annualised turnover > 2.5× asset price | No other lender has this specific turnover test |
| BFS | Biometric verification via QuickSell link | Resimac and CFAL do not require biometrics |
| BFS Low Doc | Business Customer Financial Declaration (BFS-specific form) | Other lenders use generic financial statements |
| Westpac | Affordability Declaration (signed by borrower) | Other lenders assess affordability internally |
| Westpac | DriveXpress: verbal confirmation of tax compliance accepted | CFAL requires written confirmation or documents |
| CFAL > $500k | Commentary on financial movements ≥ 10% | No other lender requires this specific commentary |
| CFAL > $1m | Succession planning details + major competitor/client list | No other lender requests these |

---

## chunk_id: diff_sub_prime_and_adverse_credit
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** MIN_CREDIT_SCORE, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, WESTPAC, CFAL
**trigger_words:** "bad credit lender differences", "which lender accepts poor credit", "adverse history lender comparison", "sub-prime lender comparison", "bankrupt lender differences"

**Content:**

**Sub-prime and adverse credit: how lenders differ**

| Scenario | Resimac | BFS | Westpac | CFAL |
|---------|---------|-----|---------|------|
| CCR / Equifax score 400–549 | ⚠ At discretion (< 450 may decline) | ✓ Tier 4 (+ 20% deposit) | ⚠ At credit discretion | ⚠ At discretion |
| CCR / Equifax score < 400 | ✗ Likely decline | ✗ Auto-decline | ⚠ At heavy discretion | ⚠ At discretion |
| Discharged bankrupt (< 10 yrs) | ✗ Excluded | ✓ BFS Plus (+ 20% deposit; 12m+ post-discharge; no adverse since) | ⚠ At discretion | ⚠ At discretion |
| Current bankrupt | ✗ Excluded | ✗ Auto-decline | ✗ Excluded | ✗ Excluded |
| 30–60 days arrears in last 12m | ⚠ Assessed | ✓ BFS Plus eligible | ⚠ At discretion | ⚠ At discretion |
| ATO debt / payment plan | ✓ Resimac Lite Doc (< 10% turnover, plan > 3m) | ⚠ At discretion | ✗ Not permitted | ✗ Not permitted |

**Delta summary:**
BFS has the highest tolerance for sub-prime and adverse credit. It is the only lender with a published pathway for discharged bankrupts and the only lender with explicit score thresholds (CCR 400) for near-prime borrowers. Resimac offers the ATO debt pathway via Lite Doc. Westpac and CFAL have no published sub-prime channels.

