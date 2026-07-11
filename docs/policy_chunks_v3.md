# Lender Policy Knowledge Base — v4 (Unified Taxonomy, 6-Lender Edition)
#
# DESIGN PRINCIPLES
# ─────────────────────────────────────────────────────────────────
# Layer 0 │ TAXONOMY REGISTRY   — canonical field definitions &
# │                               controlled vocabulary
# Layer 1 │ INTENT CHUNKS       — borrower query driven, cross-lender
# │                               tables per intent; each chunk now
# │                               carries full taxonomy metadata
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
# 2. Use trigger_words / answerable_questions for dense retrieval
# 3. Layer 2–4 chunks answer "compare", "recommend", "difference"
#    queries directly — do NOT try to synthesise from Layer 1 chunks
# 4. chunk_id is the stable retrieval key; never embed chunk_id
#    text into the vector — use it as a metadata field only
#
# ═══════════════════════════════════════════════════════════════════
# CHANGELOG — v3 → v4
# ═══════════════════════════════════════════════════════════════════
# LENDER ROSTER CHANGED:
#   Removed : WESTPAC (Westpac Equipment Finance / WEF) as a
#             standalone lender code. Source review of the new CFAL
#             chunk set (cfal_drivexpress_policy) confirms DriveXpress
#             is run "shared with Westpac Group" under the CFAL ACL
#             (393031) — i.e. what v3 modelled as a separate "Westpac"
#             lender is the same Westpac Group product surfaced through
#             CFAL. All DriveXpress / Rollover / Replacement / Medical
#             content that lived under WESTPAC in v3 now lives under
#             CFAL. No standalone Westpac source file was supplied for
#             this rebuild — if Westpac Consumer/WEF re-emerges as a
#             distinct channel, re-add it as its own lender code rather
#             than merging into CFAL again.
#   Added   : ANGLE (Angle Finance), FLEXI (flexicommercial, a humm
#             Group subsidiary), METRO (Metro Finance)
#   Kept    : RESIMAC, BFS, CFAL (all refreshed against v2 source
#             chunks dated 2026-06-28 to 2026-07-01)
#
# NEW DIMENSIONS / VALUES:
#   borrower_profile : + SPOUSE_OWNED, NON_PROPERTY_BACKED,
#                       TRANSPORT_OPERATOR, TAXI_RIDESHARE
#   asset_class       : + PRIME_MOVER, SOLAR
#   doc_type          : + MID_DOC (Angle), STREAMLINED (Metro)
#   policy_field      : + EXPOSURE_LIMIT, REPLACEMENT_LOADING,
#                        STREAMLINED_ANNUAL_CAP, MIN_FARM_SIZE
#
# STRUCTURAL NOTE: flexicommercial (FLEXI) does not fund SUVs or
# passenger cars at all — it has no MV_NEW/MV_USED presence. Any
# chunk comparing "which lender for a car" should show FLEXI as N/A,
# not as a missing data point.
#
# Last updated : 2026-07-11
# Version      : 4.0

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

| Code | Full Name | Licence | Notes |
|------|-----------|---------|-------|
| RESIMAC | Resimac Asset Finance Pty Ltd | ACL 393031 | Commercial only; 4 customer tiers |
| BFS | Branded Financial Services | ACL 392188 | Only lender in this set with a consumer product |
| CFAL | Capital Finance Australia Ltd | ACL 393031 | Westpac Group; runs DriveXpress fast-track (formerly modelled separately as "Westpac" in v3) |
| ANGLE | Angle Finance | Not stated in source docs | 3 doc tiers (Low/Mid/Full); strong primary-asset/agri focus |
| FLEXI | flexicommercial Pty Ltd (humm Group) | ABN 17 644 644 860 | No passenger vehicles / SUVs funded at all |
| METRO | Metro Finance Ltd | ABN 85 650 102 891 | Rate-sheet + "streamlined" fast-track product suite; MetroEco green channel |

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
| DIFFERENCE | How do these lenders differ? | "What is different between Angle and Metro?" |

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
| NON_PROPERTY_BACKED | Angle/flexi/Metro house style for "no property"; treat as equivalent to NO_PROPERTY |
| RENTER | Borrower is renting |
| SPOUSE_OWNED | Property backing comes from a spouse's name only (accepted by Angle, Resimac, Metro; not by BFS as a distinct category since BFS does not require property at all) |
| HIGH_CREDIT | Credit score ≥ 800 (Experian/Veda) or ≥ 650 (Equifax, Resimac/Angle scale) |
| MID_CREDIT | Credit score 550–799 (Experian) or 550–649 (Equifax) |
| LOW_CREDIT | Credit score 400–549 (Experian) or 500–549 (Equifax/Veda) |
| SUBPRIME | Credit score < 400 (Experian) or < 500 (Equifax/Veda) |
| DISCHARGED_BANKRUPT | Previously bankrupt, now discharged |
| VISA_HOLDER | Non-citizen / non-PR visa holder |
| CONSUMER | Individual borrowing for personal vehicle use |
| COMMERCIAL | Business / ABN holder borrowing for business use |
| SELF_EMPLOYED | Sole trader or director without PAYG income |
| NEW_BUSINESS | Business < 12–24 months trading (exact threshold varies by lender) |
| MEDICAL_PROFESSIONAL | Doctor, dentist, vet, allied health practitioner |
| EXISTING_CLIENT | Has existing loan with the lender |
| NEW_CLIENT | No prior relationship with the lender |
| TRANSPORT_OPERATOR | Transport/logistics subcontractor — triggers mandatory asset-backing at flexi and Metro |
| TAXI_RIDESHARE | Taxi, Uber or ride-share driver — excluded or capped at most lenders |

---

### DIMENSION: asset_class
Controlled vocabulary for asset types.

| Code | Description | Resimac | BFS | CFAL | Angle | Flexi | Metro |
|------|-------------|---------|-----|------|-------|-------|-------|
| MV_NEW | Motor vehicle new/demo (≤ 3 yrs) | Motor vehicles | New & Demo | Category A | ✓ (up to $250k asset price) | ✗ Not funded | ✓ (Passenger Vehicle Streamlined) |
| MV_USED | Motor vehicle used (> 3 yrs) | Motor vehicles | Used by year | Category A | ✓ | ✗ Not funded | ✓ |
| EV | Electric vehicle | Electric vehicles | EV (same tiers) | — | — | — | ✓ MetroEco (up to $91,387) |
| LCV | Light commercial vehicle < 4.5T | Motor vehicles | ✓ | Category A | ✓ (within MV) | — | ✓ |
| PRIMARY | Heavy trucks, trailers, construction, agriculture | Primary assets | — | Category B/C | Primary assets | Primary assets | Trucks/Trailers, Agri, Wheeled Plant streamlined |
| SECONDARY | Engineering, medical, CNC, landscape equipment | Secondary assets | — | — | Secondary assets | Secondary assets | Other Equipment streamlined |
| TERTIARY | AV, conveyors, processing, medical lasers | Tertiary assets | — | — | Tertiary assets | Tertiary assets | Other Equipment (implements) |
| PRIME_MOVER | Prime mover trucks | Primary (+2% loading) | — | — | Dedicated Prime Mover product (from 9.39%) | Primary + 1.0% add-on | Included in Balloon/Residual Refinance; excluded from Trucks/Trailers streamlined |
| CARAVAN | Caravans, campervans, camper trailers | Primary assets | ✓ | — | — | — | — |
| MOTORBIKE | Motorcycles | Motor vehicles | ✓ (max $75k) | — | — | — | — |
| MEDICAL_EQUIP | New medical equipment | — | — | Medical channel | — | Secondary (medical/dental/lab) | — |
| OFFICE_EQUIP | New office equipment and fittings | — | — | Medical channel | — | — | — |
| SOLAR | Solar / batteries / chargers | — | — | — | — | — | MetroEco (up to 7-yr term) |

---

### DIMENSION: doc_type
Documentation tier used by each lender.

| Code | Resimac | BFS | CFAL | Angle | Flexi | Metro |
|------|---------|-----|------|-------|-------|-------|
| LOW_DOC | Low Doc | Commercial Low Doc | DriveXpress (fast-track) | Low Doc (incl. $400k Low Doc) | N/A (Credit Matrix scales with size, no formal "Low Doc" label) | Streamlined products (functionally low-doc) |
| LITE_DOC | Lite Doc | — | — | — | — | — |
| MID_DOC | — | — | — | Mid Doc (< $500k) | — | — |
| FULL_DOC | Full Doc | Full Doc | Standard application | Full Doc | All transactions run on the Credit Matrix / flexipremium criteria | Non-streamlined (rate-sheet) deals |
| NEW_BIZ | — | New Business Ventures | — | Start-Up (< 2 yr ABN) | — | — |
| STREAMLINED | — | — | — | — | — | Passenger Vehicle / Trucks & Trailers / Agri / Other Equipment / Replacement / Balloon-Residual streamlined products |

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
| EXPOSURE_LIMIT | Maximum aggregate exposure to one borrower (across all contracts) |
| REPLACEMENT_LOADING | Maximum repayment/loan increase allowed under a replacement/rollover policy |
| STREAMLINED_ANNUAL_CAP | Maximum volume a borrower can access under a fast-track/streamlined channel in 12 months |
| MIN_FARM_SIZE | Minimum farm size for agricultural finance eligibility |

═══════════════════════════════════════════════════════════════════
# LAYER 1 — INTENT CHUNKS (cross-lender, 6-lender edition)
═══════════════════════════════════════════════════════════════════

---

## chunk_id: eligibility_abn_gst_duration
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_ABN, MIN_GST
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** ABN_UNDER_1YR, ABN_1_2YR, ABN_2_4YR, ABN_4_6YR, ABN_OVER_6YR, COMMERCIAL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "how long do I need my ABN", "new business ABN", "just registered ABN", "ABN less than 2 years", "GST registered recently", "how long in business"

**Content:**

A borrower's ABN and GST registration duration is one of the primary eligibility gates across every lender in this set.

| Lender | Minimum ABN | Minimum GST | Notes |
|--------|------------|------------|-------|
| Resimac PremiumPLUS | > 6 years | > 3 years | Highest tier; lowest rates |
| Resimac Premium | > 4 years | > 2 years | Property-backed only |
| Resimac Standard | > 2 years | > 1 year | Accepts renters |
| Resimac Basic | > 1 year | > 1 year | Widest property type acceptance |
| BFS Low Doc (commercial) | 2+ years ABN + GST | — | Max $150k |
| BFS Full Doc (commercial) | 12+ months ABN | — | Max $250k standard |
| BFS New Business Ventures | < 12 months ABN | — | Max $100k; Ultra Prime–Tier 4 |
| CFAL (all channels) | ≥ 2 years | Currently registered | No lower tier available |
| Angle Low/Mid Doc | 2+ years | Not essential (Low Doc < $100k) / 1+ yr (Low Doc > $100k, Mid Doc) | — |
| Angle $400k Low Doc | 3+ years ABN & GST | 3+ years | Sole traders excluded |
| Angle Prime Movers | 5+ years ABN & GST | 5+ years | Company/Trust only |
| Angle Start-Up | < 2 years ABN | Not required | Max $150k; 20% deposit |
| flexicommercial Credit Matrix | > 2 years | > 2 years | Requirements scale with exposure band |
| flexipremium (asset backed) | 4+ years | 4+ years | Companies/Trusts/Partnerships only (no sole traders) |
| flexipremium (non-asset backed) | 8+ years | 8+ years | — |
| Metro (streamlined products) | Not separately stated | 2+ years continuously (Agri: 5+ years) | GST duration is the binding gate, not ABN age |

**Matching logic:**
- ABN < 12 months → BFS New Business Ventures only (max $100k)
- ABN 12 months–2 years → BFS Full Doc; Angle Start-Up (< $150k, 20% deposit)
- ABN 2–4 years → Resimac Standard/Basic; BFS; CFAL; Angle Low/Mid Doc; Metro streamlined; flexicommercial Credit Matrix
- ABN 4–6 years → Resimac Premium+; all lenders; flexipremium (asset backed) becomes available
- ABN > 6 years → all lenders including Resimac PremiumPLUS, Angle $400k Low Doc, Angle Prime Movers, flexipremium (non-asset backed)

---

## chunk_id: eligibility_credit_score
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_CREDIT_SCORE
**lenders:** RESIMAC, BFS, ANGLE
**borrower_profile:** HIGH_CREDIT, MID_CREDIT, LOW_CREDIT, SUBPRIME, COMMERCIAL, CONSUMER
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "credit score", "Equifax score", "Experian score", "bad credit", "low credit score", "credit history", "CCR score", "Veda score", "what score do I need"

**Content:**

Only three of the six lenders publish explicit numeric credit-score thresholds; CFAL, flexicommercial and Metro require "satisfactory" / "clear and acceptable" credit reports without publishing a number.

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
| Angle Low Doc (< $100k) | Veda 1:1 | 550+ | Corporate & Individual |
| Angle Low Doc ($100k–$250k) | Veda 1:1 | 600+ | Corporate & Individual |
| Angle Mid Doc (< $500k) | Veda 1:1 | 650+ | Individual & Corporate |
| Angle $400k Low Doc | Veda 1:1 | 600+ | + 12-months asset finance credit reference |
| Angle Prime Movers | Veda 1:1 | 600+ | Company/Trust only |
| Angle Start-Up | Veda 1:1 | 550+ (flyer) / 500+ (rate card — confirm current threshold) | 20% deposit on all deals |
| Angle exposure gate | Veda 1:1 | 500 → < $150k; 550 → < $250k; 650 → > $250k | Large tickets ($500k+) have score flexibility with financial assessment |
| CFAL | Not published | "Satisfactory" | Credit bureau + ASIC search at credit discretion |
| flexicommercial | Not published | "Clear and acceptable" | Equifax on all borrowers/guarantors |
| Metro | Not published | "Satisfactory Equifax" | On applicant and guarantors |

**Auto-decline triggers (BFS — no resubmission):**
- All individuals/guarantors CCR < 400 (consumer + commercial new/demo)
- All individuals/guarantors CCR < 550 (commercial used)
- Currently bankrupt

**Angle auto-exclusion:** credit score below 500; financial defaults on file (except telco/utilities paid up to $2,500).

**Score band matching (where numeric thresholds exist):**
- ≥ 960: BFS Ultra Prime; Resimac PremiumPLUS (if ABN/property criteria met)
- 800–959: BFS Tier 1; Resimac Premium
- 650–799: BFS Tier 2; Resimac Standard/Basic; Angle Mid Doc
- 600–649: Angle Low Doc/$400k Low Doc/Prime Movers threshold
- 550–599: BFS Tier 3 (+20% deposit); Resimac Lite/Full Doc; Angle Low Doc (< $100k) / Start-Up
- 500–549: BFS Tier 4 (+20% deposit); Angle exposure capped < $150k
- < 500: BFS auto-decline below 400; Angle auto-decline below 500; CFAL/flexi/Metro at heavy discretion only (no published floor)

---

## chunk_id: eligibility_property_backing
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** PROPERTY_REQUIRED, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** PROPERTY_BACKED, NO_PROPERTY, NON_PROPERTY_BACKED, RENTER, SPOUSE_OWNED, COMMERCIAL, CONSUMER
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "do I need to own property", "property owner", "renting", "no property", "property backed", "home owner", "residential property", "guarantor property", "spousal property"

**Content:**

| Lender | Property required? | Renter/non-property eligible? | Spousal property accepted? | Conditions if no property |
|--------|------------------|-----------------|------------------------------|--------------------------|
| Resimac PremiumPLUS/Premium | ✓ Mandatory | ✗ | ✓ (waives deposit only, does not count as backing; marriage required, not de facto) | Cannot access these tiers |
| Resimac Standard/Basic | Optional | ✓ | ✓ | Non-property-backed deposit: MV 10%, other 20% |
| BFS (all tiers) | ✗ Not required | ✓ | N/A — not needed | No deposit impact from property status |
| CFAL DriveXpress (new-to-bank) | ✓ Required | ✗ | Not specified | Cannot access new-to-bank fast track |
| CFAL DriveXpress (existing client) | ✗ Not required | ✓ | — | 12m WEF/business lending history substitutes |
| Angle (all doc tiers) | Property backed OR non-property owner accepted at Low Doc (< $100k) | ✓ (Low Doc only) | ✓ (marriage cert, Medicare card or joint utility bill as evidence) | 20% deposit required for non-property owners |
| flexicommercial | Asset backed with sufficient equity, or 20% deposit | ✓ (with 20% deposit) | Not specified | Deposit assessed on aggregate proposed exposure |
| Metro (streamlined products) | Optional | ✓ (motor vehicles only) | ✓ ($150,000 cap in spouse's name) | Non-property backed: $100,000 cap, 30% deposit, dealer sale only |

**Property-backed definition (Resimac / broadly consistent across Angle & Metro):**
- ≥ 25% of property in guarantor's name
- Equity ≥ 1× NAF (Net Amount Financed)
- No multiple or adverse encumbrances on property
- Property equity must scale to exceed NAF (Metro's phrasing of the same principle)

**Key matching rule:**
- Renter, no property → BFS is the only lender across the whole set with zero property requirement at any tier
- Angle Low Doc (< $100k) is the next most accessible for non-property owners, but caps loan size and typically nudges toward a deposit
- Metro allows non-property-backed motor vehicle deals but caps at $100,000 with a steep 30% deposit
- flexicommercial and CFAL DriveXpress (new-to-bank) both push non-property borrowers toward a 20%+ deposit or exclude them from the fast-track channel entirely

---

## chunk_id: eligibility_residency_visa_bankrupt
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_ABN, MIN_CREDIT_SCORE
**lenders:** RESIMAC, BFS, CFAL
**borrower_profile:** VISA_HOLDER, DISCHARGED_BANKRUPT, LOW_CREDIT, COMMERCIAL, CONSUMER
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "visa holder", "non-resident", "permanent resident", "bankrupt", "discharged bankrupt", "bankruptcy", "temporary visa", "international borrower"

**Content:**

Only Resimac, BFS and CFAL publish explicit residency and bankruptcy policy in the source documents; Angle, flexicommercial and Metro do not address either topic directly (assessed case-by-case via standard credit checks).

**Residency / visa:**

| Lender | Citizens/PR | Visa Holders | Conditions |
|--------|-----------|-------------|-----------|
| Resimac | ✓ Required (directors + >40% shareholders) | ✗ Not accepted | Must be AU Citizen or PR residing in Australia |
| BFS PRIME | ✓ | ✓ | Min income $100k p.a.; loan ends ≥ 1 month before visa expiry; Low Doc not available |
| BFS Plus | ✓ | ✓ | Min income $50k p.a.; loan ends ≥ 1 month before visa expiry |
| CFAL | ✓ (implied) | At discretion | AML requirements apply to all >25% shareholders |

**Bankruptcy:**

| Lender | Current Bankrupt | Discharged Bankrupt | Conditions |
|--------|-----------------|-------------------|-----------|
| Resimac | ✗ Excluded | ✗ Excluded | If discharged within last 10 years |
| BFS | ✗ Auto-decline | ✓ Accepted | 20% deposit; > 12 months post-discharge; no adverse history since; BFS Plus tier |
| CFAL | ✗ Excluded (implied) | At discretion | Not explicitly addressed |

**RHI standards (BFS):**

| Tier | Last 3 months | Last 12 months |
|------|--------------|---------------|
| PRIME (Ultra–Tier 2) | No arrears | ≤ 30 days in arrears; no financial defaults |
| BFS Plus | ≤ 30 days in arrears | ≤ 60 days in arrears; no financial defaults |

**Practical note:** for borrowers with a discharged bankruptcy, BFS is the only lender in the group with a *published* pathway. For visa holders, BFS and CFAL are viable; Resimac requires citizenship/PR.

---

## chunk_id: eligibility_tax_obligations
**layer:** 1
**intent:** ELIGIBILITY
**policy_field:** MIN_ABN
**lenders:** RESIMAC, CFAL, ANGLE, METRO
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
| CFAL (all) | Must be fully up to date | No arrangements permitted |
| Angle | ATO Portals required for deals ≥ $250,000 (all doc tiers) | Portal shows last 12 months' good payment history — implies arrangements are visible but not explicitly barred |
| Metro | Not explicitly addressed in streamlined products | — |

**Key rule:** If a borrower has ATO debt with no arrangement, CFAL will decline outright. If debt is under 10% of turnover with an active arrangement running over 3 months, Resimac Lite Doc may still be accessible — this is the most forgiving published pathway in the group.

---

## chunk_id: pricing_motor_vehicles
**layer:** 1
**intent:** PRICING
**policy_field:** BASE_RATE, RISK_LOADING
**lenders:** RESIMAC, BFS, CFAL, ANGLE, METRO
**borrower_profile:** COMMERCIAL, CONSUMER, NEW_CLIENT, EXISTING_CLIENT
**asset_class:** MV_NEW, MV_USED, LCV
**doc_type:** ALL
**trigger_words:** "rate for new car", "interest rate new vehicle", "new car finance rate", "demo car rate", "used car rate", "what rate motor vehicle"

**Content:**

flexicommercial does not fund passenger vehicles/SUVs and has no rate to compare here.

| Lender / Tier | New/Demo Rate | Used Rate | Notes |
|--------------|---------------|-----------|-------|
| Resimac PremiumPLUS | 7.64% p.a. | 8.24% p.a. (> 3 yrs) | Motor vehicles |
| Resimac Premium/Standard/Basic | 7.89% p.a. | 8.49% p.a. (> 3 yrs) | Motor vehicles |
| BFS Commercial Ultra Prime | 7.60% base | 7.60% (2022–26) / 9.55% (2016 & older) | + up to 6% broker margin; cap 17.15% |
| BFS Commercial Tier 1 | 8.25% base | 8.95%–11.05% by age | — |
| BFS Commercial Tier 2 | 8.50% base | 10.45%–11.80% by age | — |
| BFS Commercial Tier 3 | 10.15% base | 12.50%–13.40% by age | — |
| BFS Commercial Tier 4 | 11.50% base | N/A (no used commercial) | — |
| BFS Consumer Ultra Prime | 9.15% max | 9.15%–10.15% by age | — |
| BFS Consumer Tier 4 | 12.50% max | 13.20%–13.90% by age | — |
| CFAL | Not published | Not published | Category A (≤ 5 yrs) — contact Credit Manager for indicative pricing |
| Angle (standard rate card, 2+ yr ABN) | — | — | Angle prices vehicles as part of its general asset-class rate card, not a dedicated MV line; motor vehicle max asset price $250k |
| Metro Passenger & Commercial (<12t GVM, ≤ 5 yrs) | 8.35% (> $20k) / 9.15% ($10k–$20k) | Add 0.75% if > 5 yrs at start of term; +1.50% if > 10 yrs at end of term | 8.35% "Prime Rate" — dealer sale, brokerage ≤ 4% |
| Metro Heavy Commercial (>12t GVM) | 8.60% (> $20k) / 10.30% ($10k–$20k) | Same age loadings apply | Trailers included |

**Lowest available rate (new car, dealer):** Resimac PremiumPLUS **7.64%**, closely followed by Metro's 8.35% Prime Rate and BFS Ultra Prime 7.60% base (before broker margin, which can push the effective rate higher).

**Rate structure differences:**
- Resimac: flat published rate by tier and asset age — most transparent for a borrower comparing lenders
- BFS commercial: base rate + broker margin (up to +6%) — actual rate to the borrower may be materially above the published base
- BFS consumer: published *maximum* rates — actual rate can be lower with a discount of up to 2%
- Metro: rate sheet + loadings (age, private sale, brokerage above 4%) stacked on top of a base figure
- CFAL and Angle do not publish a fixed MV rate card in the source documents supplied — pricing is quoted case-by-case

---

## chunk_id: pricing_electric_vehicles
**layer:** 1
**intent:** PRICING
**policy_field:** BASE_RATE, EV_DISCOUNT
**lenders:** RESIMAC, BFS, METRO
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** EV
**doc_type:** ALL
**trigger_words:** "electric vehicle rate", "EV loan", "electric car finance", "Tesla finance rate", "EV interest rate", "green vehicle", "MetroEco"

**Content:**

Only three of the six lenders publish a distinct EV product or discount. CFAL, Angle and flexicommercial do not have a published EV line (Angle and flexi's asset-class rate cards would apply to an EV as a standard motor vehicle / primary asset, with no specific discount noted).

| Lender | EV Rate / Benefit | Loan Amount / Term | Notes |
|--------|--------------------|--------------------|-------|
| Resimac PremiumPLUS | **7.54% p.a.** | Up to **84 months** (Green Goods) | –0.10% vs MV < 3 yrs; only lender extending term specifically for EVs |
| Resimac Premium/Standard/Basic | **7.79% p.a.** | Up to 84 months | — |
| BFS | Same rate tiers as ICE vehicles | Up to 84 months (standard, not EV-specific) | No separate EV discount published; electric motorcycles accepted if > 80 km/h |
| Metro MetroEco (Commercial/Consumer) | MetroEco rate discount applied to the vehicle's carded rate | Up to $91,387; 60m commercial / 84m consumer | FBT exemption on novated leasing; approvals valid 90 days |
| Metro MetroEco Electric Trucks | 1% MetroEco discount off standard rate | Up to $250k (new customer) / $300k (12m history) | Battery electric only (excludes hybrid/biofuel); property owners only; 3.5t GVM+ |
| Metro MetroEco Solar/Batteries/Chargers | MetroEco discount; no loadings on 6–7 yr terms | Up to 7-year term | Bundled with other assets on one application |

**Best EV rate (vehicle):** Resimac PremiumPLUS **7.54%**, combined with the longest available term (84 months) makes it the strongest overall EV offer in this group.
**Best EV loan term for consumers:** Metro MetroEco consumer channel — 84 months, max EOT 7 years.
**Only lender financing EV/solar bundles on one application:** Metro (MetroEco).

---

## chunk_id: pricing_primary_and_heavy_equipment
**layer:** 1
**intent:** PRICING
**policy_field:** BASE_RATE, RISK_LOADING
**lenders:** RESIMAC, ANGLE, FLEXI, METRO
**borrower_profile:** COMMERCIAL, PROPERTY_BACKED, NON_PROPERTY_BACKED
**asset_class:** PRIMARY, SECONDARY, TERTIARY, PRIME_MOVER
**doc_type:** ALL
**trigger_words:** "truck finance rate", "excavator loan rate", "heavy equipment interest rate", "primary asset rate", "forklift rate", "tractor rate", "agricultural equipment rate", "prime mover rate"

**Content:**

BFS does not finance heavy/primary equipment at all (motor vehicles only); CFAL does not publish a rate card (quoted case-by-case).

| Lender | Primary (new/short EOT) | Primary (older/longer EOT) | Secondary | Tertiary | Prime Mover |
|--------|------------------------|----------------------------|-----------|----------|-------------|
| Resimac | 8.39% (PremiumPLUS, < 3 yrs) / 8.64% (other tiers) | 9.29% / 9.54% (> 3 yrs) | 12.39% / 12.64% | 14.09% / 14.34% | Primary rate + 2% risk loading |
| Angle | 7.79%–8.79% (top profile: 8+ yr ABN, new assets) / 8.29%–9.29% (4+ yr ABN, EOT 10 yrs) | 8.39%–12.65% by EOT band (10/15/20/25 yrs, 2+ yr ABN) | 10.95%–17.15% by EOT band | 11.85%–17.85% by EOT band | From 9.39% (1% loading on standard primary rate) |
| flexicommercial | $150,001+: 8.10% (base, ex brokerage) | Add 1.0%–2.0% for asset age at EOT (11–15 yrs: +1%; 15–20 yrs: +2%) | $150,001+: 8.35% | $150,001+: 11.35% | Add 1.0% to base primary rate |
| flexicommercial flexipremium (established business) | 7.30% ($50k–$500k) | — | 8.19%–8.69% | N/A (Primary/Secondary only) | Standard add-ons apply |
| Metro Wheeled Plant & Equipment | 8.65% (> $20k) / 10.40% ($10k–$20k) | +0.75% if > 5 yrs at start; +1.50% if > 10 yrs at EOT | Metro "Other Equipment" +2% on wheeled equipment rate | — | Included under Trucks/Trailers rate sheet line (8.60%), but **excluded** from the Trucks & Trailers streamlined product |

**Cheapest new primary asset (property-backed, top profile):** Angle **7.79%** (8+ yr ABN, new asset, property backed) narrowly beats Resimac PremiumPLUS **8.39%**.
**Cheapest for an established business without top-tier ABN:** flexicommercial flexipremium **7.30%** ($50k–$500k, 4+ yr asset-backed, primary asset).
**Prime movers specifically:** Angle offers the lowest headline starting rate (**from 9.39%**, a 1% loading on its primary rate), but requires Company/Trust structure, 5+ year ABN and 600+ credit score. Resimac and flexicommercial both apply a flat loading (+2% and +1% respectively) on top of their standard primary rate rather than a dedicated product line.

---

## chunk_id: pricing_private_sale_loading
**layer:** 1
**intent:** PRICING
**policy_field:** PRIVATE_SALE_LOADING
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** MV_USED, MV_NEW, PRIMARY
**doc_type:** ALL
**trigger_words:** "private sale rate", "buying from private seller", "private seller loan", "buying from individual", "not from dealer", "private purchase finance"

**Content:**

| Lender | Rate Impact | Extra Requirements | Asset Restriction |
|--------|------------|-------------------|------------------|
| Resimac | +2.00% risk loading | — | — |
| BFS | +0.50% | DoxAI or Redbook inspection; arm's length transaction | Loan capped at $150k for private sales |
| CFAL | Not specified (no separate loading published) | — | Motor vehicles / LCV < 4.5T only — not available for heavy equipment (Cat B) or agriculture (Cat C) |
| Angle | **No rate loading applies** to private sales | Inspection via Verimoto/Redbook/Olasio/Broker Inspection; current & active registration required | — |
| flexicommercial | +1.0% add-on | $745 establishment fee (vs $495 standard) | Primary assets standard; Secondary/Tertiary private sale on exception basis only |
| Metro | +0.25% loading | — | Non-property backed: dealer sale only (private sale not available without property backing) |

**Delta summary:** Angle is the only lender in the group that charges **zero** rate loading for private sales, making it the cheapest option for a private-sale purchase by a meaningful margin once compared against Resimac's +2.00%. BFS and Metro sit in the middle with small (+0.25–0.50%) loadings; flexicommercial's +1.0% add-on is paired with a higher establishment fee.

---

## chunk_id: loan_limits_overview
**layer:** 1
**intent:** LOAN_LIMITS
**policy_field:** MAX_LOAN, EXPOSURE_LIMIT
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "how much can I borrow", "maximum loan", "loan limit", "borrow $300k", "borrow $500k", "maximum finance amount", "loan cap"

**Content:**

| Lender | Doc Type | Standard Max | Extended Max | Notes |
|--------|---------|-------------|-------------|-------|
| Resimac PremiumPLUS | Full Doc | $450k NAF | SME exposure $500k / large corporate $750k / A-rated or Govt $2m | Per asset |
| Resimac Basic | Full Doc | $200k NAF | — | — |
| BFS PRIME | Standard | $250k | $400k (high value, 20% deposit, Tier 1–2) | — |
| BFS Plus | Any | $100k | — | — |
| CFAL DriveXpress (new to bank) | Fast track | $150k | — | Property + $75k income |
| CFAL DriveXpress (existing client) | Fast track | $200k–$500k by asset category | Rollover to $500k (Westpac/CFAL original) | 12m WEF history |
| CFAL standard | Full Doc | Case-by-case | $1m+ possible | Size drives documentation |
| Angle Low Doc | Low Doc | $100k–$500k by asset class | $400k (dedicated Low Doc program, 3+ yr ABN) | Motor vehicle asset price capped $250k |
| Angle credit-score exposure gate | All | $150k (score 500) / $250k (score 550) / unlimited-ish (score 650+) | $500k+ tickets have score flexibility with assessment | Applies on top of doc-tier limits |
| flexicommercial Credit Matrix | All | Primary $750k (individual txn $500k) / Secondary $500k ($300k) / Tertiary $300k ($300k) | Increases unlocked after 9–18 perfect payments on an approved-lender contract | — |
| Metro streamlined (per product) | Streamlined | $100k–$300k individual transaction depending on product & property status | Aggregate exposure up to $750k with 24m repayment history | $500k cap per 12-month period across all streamlined products |

**Individual asset caps:** Resimac passenger vehicle $250k, motorbike $75k. Angle motor vehicle asset price $250k. flexicommercial individual primary-asset transaction $500k, secondary $300k, tertiary $300k. Metro single asset $1m, customer exposure $2m (non-streamlined rate-sheet deals).

---

## chunk_id: loan_limits_new_business
**layer:** 1
**intent:** LOAN_LIMITS
**policy_field:** MAX_LOAN, MIN_ABN
**lenders:** BFS, RESIMAC, ANGLE
**borrower_profile:** NEW_BUSINESS, ABN_UNDER_1YR, ABN_1_2YR, COMMERCIAL
**asset_class:** ALL
**doc_type:** NEW_BIZ, FULL_DOC
**trigger_words:** "new business loan", "just started business", "startup loan", "new ABN loan", "less than 2 years business"

**Content:**

| Lender | ABN Requirement | Max Loan | Conditions |
|--------|----------------|---------|-----------|
| BFS New Business Ventures | < 12 months | $100k total exposure | 90-day bank statements; 20% deposit for Tier 3–4 |
| BFS Full Doc | 12+ months | $250k | — |
| Angle Start-Up | < 2 years (business trading min. 3 months) | $150k incl. brokerage | 550+ credit score (flyer)/500+ (rate card); 20% deposit on all deals; previous industry experience required; primary assets only |
| Resimac Basic | > 1 year | $100k–$200k | ABN + GST > 1 yr; all standard criteria |

CFAL, flexicommercial and Metro have no published sub-2-year-ABN product — CFAL and flexicommercial's floor is 2 years ABN/GST, and Metro's streamlined products require 2+ years continuous GST registration (Agri: 5+ years). A borrower under 2 years ABN is effectively limited to BFS, Angle Start-Up, or Resimac Basic (once past the 1-year mark).

---

## chunk_id: loan_limits_high_value
**layer:** 1
**intent:** LOAN_LIMITS
**policy_field:** MAX_LOAN, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** HIGH_CREDIT, PROPERTY_BACKED, COMMERCIAL, EXISTING_CLIENT
**asset_class:** ALL
**doc_type:** FULL_DOC
**trigger_words:** "borrow more than $250k", "large loan equipment", "$300k loan", "$400k loan", "$500k finance", "high value loan"

**Content:**

| Lender | Range | Requirements |
|--------|-------|-------------|
| Resimac PremiumPLUS/Premium | Up to $450k NAF | ABN > 4–6 yrs; property-backed; Full Doc |
| BFS High Value | $250k–$400k | Ultra Prime–Tier 2; 20% deposit; asset-backed; case-by-case |
| CFAL | $500k–$1m+ | 3 years financials; ATO portal; full documentation; succession plan + competitor list above $1m |
| CFAL DriveXpress (existing client, Cat C) | Up to $500k | 12m WEF history |
| Angle Full Doc | $500k–$1m+ | FY2024+FY2023 financials only (no bank statement alternative); aged debtor/creditor listing and cashflow projections above $500k |
| flexicommercial Credit Matrix | Up to $750k aggregate (Primary) | 18 payments perfect conduct on a $250k+ contract to unlock the top band |
| Metro streamlined (12–24m history) | $500k–$750k aggregate exposure | 12/24 months of good repayment history with Metro required to unlock each step |

---

## chunk_id: documentation_low_doc
**layer:** 1
**intent:** DOCUMENTATION
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, CFAL, ANGLE, METRO
**borrower_profile:** SELF_EMPLOYED, COMMERCIAL, NEW_CLIENT
**asset_class:** ALL
**doc_type:** LOW_DOC, LITE_DOC, MID_DOC, STREAMLINED
**trigger_words:** "low doc", "no financials", "without tax return", "minimal paperwork", "self-employed no financials", "lite doc", "reduced documentation", "streamlined"

**Content:**

flexicommercial has no formally named "Low Doc" product — its Credit Matrix scales requirements continuously with exposure band rather than offering a discrete low-doc tier.

| Lender | Product | Min Documents | Max Loan | Eligibility Gate |
|--------|---------|--------------|---------|-----------------|
| Resimac Low Doc | Low Doc | Application + A&L Statement | $300k (PremiumPLUS) | All tiers; not Tertiary assets |
| Resimac Lite Doc | Lite Doc | + ATO portals + BAS | $300k (PremiumPLUS) | ATO debt < 10% turnover; payment plan > 3m |
| BFS | Commercial Low Doc | Business Financial Declaration | $150k total exposure | 2+ yrs ABN+GST; Ultra Prime–Tier 2; Guarantor = AU citizen/PR |
| CFAL | DriveXpress | Affordability Declaration + credit check | $150k new client / up to $500k existing | > 2 yrs ABN+GST; statutory obligations current |
| Angle | Low Doc | 1 ID + A&L statement (+ credit reference above $100k) | $100k–$250k by asset class; $400k dedicated program | 2+ yrs ABN (3+ yrs for $400k program) |
| Angle | Mid Doc | 6 months bank statements (clean conduct test) | $500k | 2+ yrs ABN, 1+ yr GST |
| Metro | Streamlined (per product) | Comparable credit reference (12m) + Equifax check | $100k–$300k individual transaction | 2+ yrs GST (Agri: 5+ yrs); no financials required if streamlined criteria met |

**Easiest access (least paperwork) ranking:** CFAL DriveXpress (existing client) and Metro streamlined products both require essentially just a credit reference and declaration with no financials — these are the two "fastest" channels in the group when the borrower already has a qualifying credit history with that lender or an approved lender.

---

## chunk_id: documentation_full_doc
**layer:** 1
**intent:** DOCUMENTATION
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** FULL_DOC
**trigger_words:** "what documents do I need", "full application", "financials required", "tax return loan", "financial statements", "what paperwork", "bank statements loan"

**Content:**

**By loan size — minimum financial documentation:**

| Size Band | Resimac | BFS Commercial | CFAL | Angle | flexicommercial |
|-----------|---------|---------------|------|-------|-----------------|
| < $100k | Full Doc: BAS + ATO portal + financials | 90-day bank statements | 2 yrs financials + 2 yrs ITR | 6m bank statements OR FY24+FY23 financials | Scales with exposure band on Credit Matrix |
| $100k–$250k | 2 yrs financials (P&L + balance sheet) ≤ 18m | 2 yrs signed externally prepared financials | 2 yrs financials + 2 yrs ITR + ATO portal | Same as above + Commitment Schedule + ATO portal | Same |
| $250k–$500k | 2 yrs financials + ATO portal + commitment schedule | 2 yrs signed financials | 3 yrs financials + ATO portal + aged debtor list | + business background + major client list | Higher band on Credit Matrix; repayment history may substitute |
| $500k–$1m | 3 yrs financials + commentary on movements ≥ 10% | — | + Interim accounts if year-end > 6m old | FY24+FY23 financials only (bank statement alternative no longer accepted); aged debtor/creditor + cashflow projections | — |
| > $1m | 3 yrs financials + cash flow projections | — | + Cash flow projections + succession plan + competitor list | Same as $500k–$1m band | — |

Metro's non-streamlined (rate-sheet) deals are not itemised as a size-banded documentation table in the source material; streamlined products substitute a credit reference for financials entirely (see documentation_low_doc chunk above).

---

## chunk_id: asset_motor_vehicles_eligibility
**layer:** 1
**intent:** ASSET_ELIGIBILITY
**policy_field:** ASSET_AGE_MAX
**lenders:** RESIMAC, BFS, CFAL, ANGLE, METRO
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** MV_NEW, MV_USED, EV, LCV, MOTORBIKE, CARAVAN
**doc_type:** ALL
**trigger_words:** "can I finance a car", "vehicle finance eligibility", "what cars can I finance", "ute loan", "van finance", "light commercial vehicle loan", "motorbike loan", "caravan finance"

**Content:**

**flexicommercial does not fund SUVs or passenger cars under any circumstances (including rental car businesses) — it is excluded from this table entirely for vehicle rows.**

| Vehicle Type | Resimac | BFS PRIME | BFS Plus | CFAL | Angle | Metro |
|-------------|---------|----------|---------|------|-------|-------|
| Passenger cars | ✓ | ✓ | ✓ | ✓ Cat A | ✓ | ✓ Passenger Vehicle streamlined |
| Vans/utes < 4.5T | ✓ | ✓ | ✓ | ✓ Cat A | ✓ | ✓ |
| Electric vehicles | ✓ (best rate) | ✓ | ✓ | — | — | ✓ MetroEco |
| Motorbikes | ✓ max $75k | ✓ | — | — | — | — |
| Caravans | ✓ Primary | ✓ | — | — | — | — |
| Campervans | — | ✓ | — | — | — | — |
| Classic cars | ✓ +2% | — | — | — | — | — |
| Taxi / Uber / ride-share | ✗ Excluded | ⚠ Limited | ⚠ Limited | ✗ Excluded | ✗ Excluded | ⚠ Capped $250k, property backed |

**Maximum vehicle age:**

| Lender | Max at Start of Term | Max at End of Term |
|--------|--------------------|--------------------|
| Resimac | Not specified | 25 years (motor vehicles) |
| BFS PRIME | 15 yrs (≤ 60m term); 7 yrs (> 60m term) | — |
| BFS Plus | 15 years | — |
| CFAL Category A | Up to 5 years old | — |
| Angle | Not separately specified for MV | Motor vehicle asset price capped $250k regardless of age |
| Metro Passenger/Commercial streamlined | — | 12 years |
| Metro Replacement (passenger/light commercial) | — | 12 years |

---

## chunk_id: asset_heavy_equipment_eligibility
**layer:** 1
**intent:** ASSET_ELIGIBILITY
**policy_field:** ASSET_AGE_MAX
**lenders:** RESIMAC, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** COMMERCIAL
**asset_class:** PRIMARY, SECONDARY, TERTIARY, PRIME_MOVER
**doc_type:** ALL
**trigger_words:** "truck finance", "excavator loan", "forklift finance", "crane loan", "heavy machinery loan", "construction equipment finance", "tractor loan", "agricultural machinery"

**Content:**

BFS does not finance any heavy/primary equipment (motor vehicles only).

| Asset Type | Resimac | CFAL | Angle | flexicommercial | Metro |
|-----------|---------|------|-------|------------------|-------|
| Heavy trucks > 4.5T | ✓ Primary | ✓ Cat B (≤ 5 yrs, dealer) | ✓ Primary | ✓ Primary | ✓ Trucks/Trailers streamlined |
| Trailers | ✓ Primary | ✓ Cat B | ✓ Primary | ✓ Primary (30 yr EOT) | ✓ |
| Forklifts / telehandlers | ✓ Primary | ✓ Cat B | ✓ Primary | ✓ Primary | ✓ (capped $250k for on-hire businesses) |
| Excavators / skid steers | ✓ Primary | ✓ Cat B | ✓ Primary | ✓ Primary | ✓ |
| Cranes (mobile/tight access) | ✓ Primary | ✓ Cat B (≤ 3 yrs) | Not separately listed | — | — |
| Prime movers | ✓ +2% loading | — | ✓ Dedicated product, from 9.39% | ✓ +1.0% add-on | ✓ Balloon/Residual only; **excluded from Trucks & Trailers streamlined** |
| Tractors / harvesters | ✓ Primary | ✓ Cat C (≤ 7 yrs, dealer) | ✓ Primary | Not primary category focus | ✓ Agri streamlined |
| Agricultural implements | ✓ Primary | ✓ Cat C | ✓ Primary | — | ✓ Agri (Tertiary/Implements line) |
| Medical equipment | — | ✓ Medical channel (< $350k specialist) | — | ✓ Secondary | — |
| Generators/compressors | ✓ Secondary | — | — | ✓ Secondary (plant services) | — |
| AV / conveyors / drones | ✓ Tertiary | — | — | ✓ Tertiary | — |

**Maximum asset age by category (end of term unless noted):**

| Lender | Category | Max Age |
|--------|---------|--------|
| Resimac | Primary | 25 years |
| Resimac | Secondary | 10 years |
| Resimac | Tertiary | 5 years |
| CFAL | Cat B heavy equipment | 5 years (cranes: 3 years) |
| CFAL | Cat C agriculture | 7 years |
| Angle | Primary | 25 years |
| Angle | Secondary | 15 years |
| Angle | Tertiary | 10 years |
| flexicommercial | Primary | 20 years (trailers: 30 years) |
| flexicommercial | Secondary | 7 years |
| Metro | Trucks/Trailers/Wheeled Equipment streamlined | 15 years |
| Metro | Agri streamlined | 15 years |
| Metro | Other Equipment streamlined | 3 years |

**Widest asset breadth:** Resimac and Angle both cover all three heavy-equipment tiers (Primary/Secondary/Tertiary) plus a dedicated or loaded prime-mover pathway; flexicommercial matches this breadth but with zero motor-vehicle presence. Metro is the most fragmented — coverage exists but is split across five separate streamlined products, each with its own cap and criteria.

---

## chunk_id: asset_excluded_items
**layer:** 1
**intent:** EXCLUSIONS
**policy_field:** ASSET_AGE_MAX
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "can I finance gym equipment", "software loan", "office furniture loan", "food truck finance", "livestock loan", "what can't be financed", "excluded assets", "photocopier", "SUV excluded"

**Content:**

**Excluded across multiple lenders:**

| Asset | Resimac | BFS | CFAL | Angle | flexicommercial | Metro |
|-------|---------|-----|------|-------|------------------|-------|
| SUVs / passenger cars | ✓ Funded | ✓ Funded | ✓ Funded | ✓ Funded | ✗ Excluded (all circumstances) | ✓ Funded |
| Taxis / ride-share | ✗ | ⚠ Limited | ✗ | ✗ | — (not a vehicle lender) | ⚠ Capped $250k |
| IT hardware / computers | ✗ | — | — | — | ✓ Funded (Tertiary, capped $50k) | ✗ Non-eligible |
| Office furniture / fixtures & fittings | ✗ | — | — | — | — | ✗ Non-eligible |
| Livestock | ✗ | — | — | — | — | — |
| Software / intangibles | ✗ | — | — | — | ✓ Funded (Tertiary) | ✗ Non-eligible |
| Gym / fitness equipment | ✗ | — | — | — | ✓ Funded (Tertiary) | ✗ Non-eligible |
| Photocopiers / MFDs | — | — | — | — | ✗ Excluded | — |
| Scaffolding | ✗ | — | — | — | ✗ Excluded | — |
| Food trucks | ✗ | — | — | — | — | — |
| Artwork | ✗ | — | — | — | — | — |
| Novated leases | — | — | ✗ | — | — | — |
| Sale and leaseback | — | ✗ | ⚠ Medical only (< 30 days) | — | — | ✗ (loading applies to non-streamlined) |
| Debt consolidation / cash raising / top-up | — | ✗ | — | — | — | — |
| Imported / exotic cars | — | — | ✗ | — | — | — |
| Repairable write-offs | ✗ | — | ✗ | — | — | — |
| Charter buses | — | — | ⚠ Replacement Cat C: govt/school/local route only | — | — | — |
| Dairy / irrigation equipment | — | — | — | ✗ (not addressed) | — | ✗ Excluded (Agri streamlined) |
| Pharmacists (as a profession, for medical channel) | — | — | ✗ Excluded from CFAL Medical | — | — | — |

**Widest exclusion list:** Resimac publishes the longest explicit exclusion list of any single lender (18+ named categories) — useful as a first filter when a borrower asks about an unusual asset type.

---

## chunk_id: settlement_universal
**layer:** 1
**intent:** SETTLEMENT
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, CFAL, ANGLE
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "settlement documents", "what do I need to settle", "finalise loan", "PPSR", "insurance settlement", "sign loan documents", "Certificate of Currency"

**Content:**

**Universal settlement checklist (source documents did not detail Metro or flexicommercial settlement procedures separately — assumed broadly standard: signed documents, insurance, PPSR):**

| Requirement | Resimac | BFS | CFAL | Angle |
|------------|---------|-----|------|-------|
| Signed loan documents | ✓ | ✓ (QuickSell) | ✓ (QuickSell/DriveOnline) | ✓ (DocuSign) |
| Asset insurance (lender as interested party) | ✓ | ✓ (loaded in QuickSell) | ✓ | ✓ |
| PPSR registration | ✓ (at cost) | ✓ ($6) | ✓ | ✓ (conducted by Angle) |
| Tax invoice or private sale agreement | ✓ | ✓ | ✓ | ✓ (must note year/make/model/VIN/odometer) |
| Biometric verification | — | ✓ | ✓ | — |
| Certificate of Currency (CoC) | ✓ ($100k+ assets) | — | ✓ ($150k+ assets) | ✓ ($100k+ assets) |
| Private sale inspection | DoxAI/Redbook not specified | DoxAI or Redbook | — | Verimoto / Redbook / Olasio / Broker Inspection |

**CFAL settlement updates (effective 24 February 2025):**
- PPSR: motor vehicles with VIN in buyback/private sale no longer need PPSR company search over seller. VIN search day-of must show no other registration.
- CoC: fleet policies no longer need to list specific VIN/serial number (motor vehicles only).

**Angle-specific note:** all existing PPSR encumbrances on a used car must be cleared before settlement, and unaccredited suppliers must provide a current bank statement for accreditation before Angle will settle.

---

## chunk_id: special_programs_replacement_rollover
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** MAX_LOAN, MIN_ABN, REPLACEMENT_LOADING
**lenders:** CFAL, FLEXI, METRO, RESIMAC
**borrower_profile:** EXISTING_CLIENT, COMMERCIAL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "refinance equipment loan", "roll over contract", "extend loan", "replace existing finance", "refinance truck loan", "switch lender", "balloon refinance"

**Content:**

Four of the six lenders offer a dedicated replacement/rollover/refinance channel; BFS explicitly excludes mid-term refinancing, sale and leaseback, top-up loans and cash raising as loan purposes.

| Lender | Product | Max Loan | Repayment/Loan Increase Cap | Contract Age Requirement |
|--------|---------|---------|------------------------------|---------------------------|
| CFAL Rollover | Existing clients only | $500k (Westpac/CFAL original) / $250k (other financier) | — | 12+ months current WEF/CFAL history |
| CFAL Replacement | New or existing | $150k (new, Cat A&B) / $650k (existing, Cat B&C) | 125% (new-to-bank) / 150% (existing) of payment being replaced | Contract operating ≥ 12 months; finalised within 6 months / on settlement |
| flexicommercial flexireplacement | Primary assets only | $500k aggregate | 125% of repayment being replaced | Old facility 18+ months old, current or paid out within last 3 months |
| flexicommercial Mid-term Refinancing | Existing flexi contract | Up to 5-year new term | Refinanced at net book value (no early termination cost) | At least 12 months into current contract |
| Metro Replacement | New/existing/spouse/non-property | $150k–$300k depending on category & property status | 125% of original loan amount or monthly repayment | Contract being replaced must have run ≥ 36 months |
| Metro Balloon/Residual Refinance | New/existing/spouse/non-property | $150k | — | Account must be in its final 12 months; no inspection required |
| Resimac Sale and Buyback | PremiumPLUS/Premium only | Standard limits | — | Dealership sales only; asset purchased within last 30 days |

**Fastest / lowest-friction replacement:** Metro's Balloon/Residual Refinance requires **no inspection** and accepts prime movers, making it the quickest path for a borrower refinancing a balloon in its final year. flexicommercial's Mid-term Refinancing is notable for capping brokerage at just 1.0% and guaranteeing no early-termination cost.

---

## chunk_id: special_programs_medical
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** MAX_LOAN
**lenders:** CFAL
**borrower_profile:** MEDICAL_PROFESSIONAL, COMMERCIAL, NEW_CLIENT, PROPERTY_BACKED
**asset_class:** MEDICAL_EQUIP, OFFICE_EQUIP, MV_NEW
**doc_type:** LOW_DOC
**trigger_words:** "doctor loan", "medical professional finance", "GP equipment loan", "dental equipment finance", "vet loan", "allied health loan", "medical equipment finance"

**Content:**

CFAL is the only lender in this six-lender set with a named Medical specialist channel. (flexicommercial finances medical/dental/lab equipment as part of its general Secondary asset category, but has no dedicated medical program or professional-specific limits.)

**Eligible professions:**
- Medical Specialist, GP, Dental, Vet (higher limits)
- Allied Health: OT, Optometrist, Osteopath, Physiotherapist, Chiropractor, Audiologist, Pathology, Podiatrist, Psychologist, Speech Pathologist
- **Excluded:** Pharmacists

**Limits:**

| Asset | Specialist/GP/Dental/Vet | Allied Health |
|-------|------------------------|--------------|
| Motor vehicle (≤ 5 yrs) | < $250k | < $150k |
| New office equipment | < $150k | < $150k |
| New medical equipment | < $350k | < $150k |
| Max cumulative | < $500k | < $250k |

**Conditions:** > 2 yrs in business + GST; new clients must own property + $75k income; sale & hire back within 30 days permitted; Affordability Declaration required.

---

## chunk_id: special_programs_ev_green
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** MAX_TERM, EV_DISCOUNT
**lenders:** RESIMAC, METRO
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** EV, SOLAR, PRIME_MOVER
**doc_type:** ALL
**trigger_words:** "84 month loan", "7 year EV loan", "longer term electric vehicle", "green goods loan", "extended term EV", "MetroEco", "solar finance", "electric truck finance"

**Content:**

- Resimac's Green Goods program: 84-month terms specifically for EVs/sustainable assets (standard max term is 60 months elsewhere in the Resimac range)
- Resimac combined benefit: 7.54% rate (PremiumPLUS) + 84-month term = lowest rate + longest term for a straight EV purchase in this group
- Metro's MetroEco suite is the broadest green program in the group — it bundles electric vehicles, electric trucks (3.5t GVM+, battery only) and solar/batteries/chargers under one discount mechanism, with consumer EV terms up to 84 months (max EOT 7 years) and solar terms up to 7 years
- Metro Electric Trucks require property ownership and exclude hybrid/biofuel vehicles — a narrower gate than Resimac's EV product, which has no property requirement baked into the EV rate itself (Resimac's general tier rules on property still apply)
- BFS has no EV-specific discount or term extension — EVs are priced on the same tier table as internal-combustion vehicles
- Angle and flexicommercial have no published green/EV product

---

## chunk_id: special_programs_new_business_startup
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** MIN_ABN, MAX_LOAN
**lenders:** ANGLE, BFS
**borrower_profile:** NEW_BUSINESS, ABN_UNDER_1YR, ABN_1_2YR, NON_PROPERTY_BACKED
**asset_class:** PRIMARY
**doc_type:** NEW_BIZ
**trigger_words:** "Angle Start-Up", "BFS New Business Ventures", "new business finance program", "under 2 years business loan program"

**Content:**

| Feature | Angle Start-Up | BFS New Business Ventures |
|---------|----------------|----------------------------|
| ABN age | Under 2 years (business operating min. 3 months) | Under 12 months |
| Asset scope | Primary assets only (wood chippers, tippers, excavators, ride-on mowers, caravans, etc.) | Motor vehicles only |
| Max loan | $150,000 incl. brokerage | $100,000 total exposure |
| Deposit | 20% on all applications | 20% for Tier 3–4 only |
| Credit score | 550+ (flyer) / 500+ (rate card — confirm) | Any BFS tier, CCR ≥ 400 |
| Extra requirement | Previous industry experience required (PAYG history, prior contracts, or qualifications); clean bank statements (no overdraws/dishonours/ATO arrangements) | 90-day bank statements; run contract required for couriers |

**Key distinction:** Angle's Start-Up product is asset-restricted (primary equipment only, no vehicles) and explicitly demands proof of relevant industry experience — it is built for tradespeople starting their own business with familiar equipment, not for a new business buying its first car. BFS New Business Ventures is the mirror image: vehicle finance only, with a shorter (12-month) ABN threshold.

---

## chunk_id: special_programs_streamlined_and_fast_track
**layer:** 1
**intent:** SPECIAL_PROGRAMS
**policy_field:** STREAMLINED_ANNUAL_CAP, MAX_LOAN
**lenders:** ANGLE, METRO, CFAL
**borrower_profile:** COMMERCIAL, PROPERTY_BACKED, NON_PROPERTY_BACKED
**asset_class:** ALL
**doc_type:** LOW_DOC, STREAMLINED
**trigger_words:** "fast track finance", "quick approval loan", "streamlined product", "Angle $400k Low Doc", "DriveXpress", "Metro streamlined"

**Content:**

Three lenders operate a named fast-track / streamlined channel that substitutes a credit reference for full financials.

| Lender | Channel | Annual/Aggregate Cap | Turnaround |
|--------|---------|----------------------|------------|
| CFAL DriveXpress | New-to-bank $150k / existing client up to $500k exposure | DriveXpress exposure = aggregate loan balances under the policy | Not stated |
| Angle A+ deals | Priority assessment (any product meeting top-tier criteria) | — | Average 2 hours |
| Angle $400k Low Doc | Dedicated big-ticket low-doc program | $400k max transaction | Requires 12m+ credit reference from Angle or a Tier 1/2 asset finance provider |
| Metro (all streamlined products combined) | Passenger Vehicle / Trucks & Trailers / Agri / Other Equipment / Replacement / Balloon-Residual | **$500,000 maximum in any 12-month period** across all streamlined products combined | Fast (credit-reference based, no financials) |

**Key distinction:** Metro's $500k cap is a genuine rolling 12-month ceiling shared across *all* its streamlined products — a borrower who has already drawn $450k streamlined this year has only $50k of streamlined capacity left, regardless of which product they use next. CFAL and Angle's caps are structured per-product/per-program rather than as one shared pool.

---

## chunk_id: fees_comparison
**layer:** 1
**intent:** FEES
**policy_field:** BROKERAGE_MAX
**lenders:** RESIMAC, BFS, ANGLE, FLEXI, METRO
**borrower_profile:** ALL
**asset_class:** ALL
**doc_type:** ALL
**trigger_words:** "fees", "setup fee", "establishment fee", "monthly fee", "early repayment fee", "break cost", "what does it cost", "brokerage fee"

**Content:**

CFAL does not publish a public fee schedule (indicative pricing obtained from the CFAL Credit Manager on a deal-by-deal basis).

**Establishment fees:**

| Lender | Standard | Private Sale / Refinance Premium |
|--------|---------|------------------------------------|
| Resimac | $495 | +$200 ($695 total) |
| BFS Consumer | $525 | +$100 ($625 total) |
| BFS Commercial | $575 | +$100 ($675 total) |
| Angle | $649 | Same fee applies to dealer or private sale |
| flexicommercial | $495 | $745 for private sales and refinances |
| Metro | $275 min / $450 max (excl. 50/50 split deals) | Not separately stated |

**Ongoing fees:**

| Lender | Monthly | Fortnightly | Weekly |
|--------|---------|------------|--------|
| Resimac | $4.95 | — | — |
| BFS | $10.00 | $4.62 | $2.31 |
| Angle | $4.95 | — | $1.00 |

**Early termination:**

| Lender | Admin Fee | Additional |
|--------|----------|-----------|
| BFS Consumer | $70 | Up to $750 (reduces by $12/month paid) |
| BFS Commercial | $85 | 35% of remaining interest (15% if refinancing with BFS) |

**Brokerage caps:**

| Lender | Standard cap (no rate impact) | Absolute max | Above cap |
|--------|-------------------------------|-------------|----------|
| Resimac | Up to 5.5% | 8.8% | +0.5% rate per 1% extra brokerage |
| BFS | Origination fee max $1,650 | — | 75% overs net of GST |
| Angle | Up to 8% (incl. GST) | 8% | No rate loading applies up to 8% |
| Angle flexipremium-equivalent (n/a — Angle has no separate premium tier) | — | — | — |
| flexicommercial (< $50k deals) | Up to 5% | 8% | +0.5% rate per 1% brokerage above 5% |
| flexicommercial (≥ $50k deals) | Up to 4% | 6% | +0.5% rate per 1% brokerage above 4% |
| flexicommercial flexipremium | — | **3% max** | Product-specific cap, lower than standard Credit Matrix |
| flexicommercial Mid-term Refinancing | — | **1.0% max** | Higher brokerage only by BDM exception |
| Metro | Up to 4% | — | +0.5% rate for every 1% brokerage above 4% |

**Cheapest establishment fee in the group:** Metro ($275 minimum). **Most generous brokerage cap without a rate penalty:** Angle (up to 8% with zero rate loading, versus Resimac and flexicommercial which both start adding rate loadings above 4–5.5%).

═══════════════════════════════════════════════════════════════════
# LAYER 2 — CROSS-LENDER COMPARISON MATRIX
# Purpose: answer "compare X vs Y" queries directly
# Each chunk = one policy dimension, all lenders side by side
═══════════════════════════════════════════════════════════════════

## chunk_id: compare_tier_logic
**layer:** 2
**intent:** COMPARE
**policy_field:** MIN_ABN, MIN_CREDIT_SCORE, PROPERTY_REQUIRED
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** ALL
**trigger_words:** "compare lenders", "which lender is better", "difference between lenders", "how do lenders compare", "compare Resimac BFS Angle Flexi Metro CFAL"

**Content:**

The six lenders use fundamentally different logic to tier and assess borrowers.

| Dimension | Resimac | BFS | CFAL | Angle | flexicommercial | Metro |
|-----------|---------|-----|------|-------|------------------|-------|
| **Primary tier driver** | Property-backing type × ABN duration | Experian CCR credit score | Transaction size + relationship history (Westpac Group) | Credit score × ABN duration × exposure size | Exposure band on the Credit Matrix | Property status × repayment history with Metro |
| **Serves consumers?** | ✗ Commercial only | ✓ Commercial + individual | ✗ Commercial only | ✗ Commercial only | ✗ Commercial only | ⚠ Consumer only via MetroEco EV |
| **Serves new businesses?** | ✓ Basic tier (ABN > 1 yr) | ✓ New Business Ventures (< 12m) | ✗ 2-year ABN floor | ✓ Start-Up (< 2 yrs, primary assets only) | ✗ 2-year ABN floor | ✗ 2-year GST floor (Agri: 5 yrs) |
| **Finances vehicles?** | ✓ | ✓ (only vehicles) | ✓ Cat A | ✓ | ✗ Never | ✓ + MetroEco |
| **Finances heavy/primary equipment?** | ✓ Widest | ✗ | ✓ Cat B/C | ✓ Wide | ✓ Wide, no vehicles | ✓ Via 5 separate streamlined products |
| **Sub-prime tolerance** | Medium — Basic tier accessible | Highest — CCR 400 accepted | Low — no sub-prime channel | Medium — score 500 floor, capped exposure | Low — no published floor | Low — no published floor |
| **Discharged bankrupt** | ✗ Excluded (10 yr rule) | ✓ Accepted (conditions) | At discretion | Not addressed | Not addressed | Not addressed |
| **Simplified/fast-track option** | ✓ Low / Lite Doc | ✓ Commercial Low Doc | ✓ DriveXpress | ✓ Low Doc / $400k Low Doc | ✗ No discrete low-doc tier | ✓ 6 streamlined products |
| **Dedicated green/EV product** | ✓ Green Goods (84m) | ✗ | ✗ | ✗ | ✗ | ✓ MetroEco (EV+trucks+solar) |
| **Prime mover product** | ✓ +2% loading | ✗ Not financed | ✗ Not financed | ✓ Dedicated product | ✓ +1% loading | ⚠ Only via Balloon/Residual Refinance; excluded from main streamlined truck product |
| **Max standard loan** | $450k NAF | $250k | Case-by-case, $1m+ possible | $500k+ (Full Doc) | $750k aggregate (Primary) | $750k aggregate (24m history) |
| **Private sale rate loading** | +2.00% | +0.50% | Not specified | **0% — no loading** | +1.0% | +0.25% |
| **Replacement/rollover channel** | ⚠ Sale & Buyback only | ✗ Explicitly excluded | ✓ Rollover + Replacement | ✗ Not published | ✓ flexireplacement + Mid-term Refinancing | ✓ Replacement + Balloon/Residual Refinance |

---

## chunk_id: compare_interest_rates
**layer:** 2
**intent:** COMPARE
**policy_field:** BASE_RATE, EV_DISCOUNT, RISK_LOADING
**lenders:** RESIMAC, BFS, ANGLE, FLEXI, METRO
**borrower_profile:** ALL
**trigger_words:** "compare rates", "which lender has the lowest rate", "best rate", "rate comparison", "who is cheapest", "lowest interest rate"

**Content:**

**Rate comparison — best available rate per asset type (CFAL excluded; no public rate card):**

| Asset Type | Lowest Available Rate | Lender | Conditions |
|-----------|----------------------|--------|-----------|
| New car (dealer) | **7.60%** base | BFS Ultra Prime commercial | Before broker margin (up to +6%); or Resimac PremiumPLUS 7.64% flat |
| New car (Metro Prime Rate) | **8.35%** | Metro | Vehicle < 5 yrs, dealer, > $20k |
| Used car 2022–2026 (dealer) | **7.60%** | BFS Ultra Prime | Same tier as new/demo |
| Used car 2016 & older | **9.55%** | BFS Ultra Prime / Resimac PremiumPLUS 8.24%+ | Resimac's flat used-vehicle rate (8.24–8.49%) beats BFS at lower tiers |
| Electric vehicle | **7.54%** | Resimac PremiumPLUS | + 84-month term |
| Electric vehicle (Metro discount) | MetroEco discount off carded rate | Metro | Bundled EV + charger on one application |
| Primary asset, top profile | **7.79%** | Angle | 8+ yr ABN, new asset, property backed |
| Primary asset, established business | **7.30%** | flexicommercial flexipremium | $50k–$500k, 4+ yr asset-backed |
| Prime mover | **from 9.39%** | Angle | Company/Trust, 5+ yr ABN, 600+ credit score |
| Secondary assets | **8.19%** (flexipremium) or **12.39%** (Resimac PremiumPLUS) | flexicommercial (if eligible) / Resimac | flexipremium requires 4+ yr asset-backed business, up to 2-yr-old secondary assets only |
| Tertiary assets | **11.35%** (flexi, $150k+) | flexicommercial | Resimac's tertiary rate (14.09%) is notably higher |

**Rate structure differences:**
- Resimac: flat rates by tier and asset category — borrower sees the exact rate upfront
- BFS commercial: base rate + broker margin (up to +6%) — actual rate to borrower may sit well above the published base
- BFS consumer: published maximum rates — actual rate can be lower
- Angle: profile-based headline rates for top-tier borrowers, falling back to an EOT-age-banded standard rate card for everyone else
- flexicommercial: base rate by amount funded, with a long list of stackable add-ons (asset age, non-asset-backed, private sale, term length)
- Metro: rate-sheet base + loadings; brokerage above 4% adds 0.5% per 1%, same structural pattern as flexicommercial and Resimac's brokerage-linked pricing

---

## chunk_id: compare_documentation_effort
**layer:** 2
**intent:** COMPARE
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, CFAL, ANGLE, METRO
**borrower_profile:** SELF_EMPLOYED, COMMERCIAL
**trigger_words:** "easiest application", "least paperwork", "simplest lender", "compare document requirements", "which lender asks for less"

**Content:**

**Documentation burden ranking (least to most, six-lender set; flexicommercial omitted as it has no discrete low-doc tier — see documentation_low_doc chunk):**

| Rank | Lender / Channel | What's required | Suitable for |
|------|-----------------|----------------|-------------|
| 1 (easiest) | CFAL DriveXpress (existing client) | Affordability Declaration + credit check only | 12m WEF/CFAL history or existing Westpac business lending |
| 2 | Metro streamlined (with 6–24m Metro history) | Comparable credit reference + Equifax check | Existing Metro customers wanting a fast repeat deal |
| 3 | Angle Low Doc (< $100k) | 1 ID + Asset & Liabilities statement | 2+ yr ABN, property backed or non-property owner |
| 4 | Resimac Low Doc | Application + Asset & Liability Statement | All tiers; up to $300k |
| 5 | BFS Commercial Low Doc | Business Customer Financial Declaration | 2+ yr ABN+GST; up to $150k; Ultra Prime–Tier 2 |
| 6 | Angle Mid Doc | 6 months bank statements (clean conduct test) | Up to $500k |
| 7 | Resimac Lite Doc | Low Doc + ATO portal + 2 BAS statements | ATO debt < 10% turnover |
| 8 | BFS Full Doc (≤ $100k) | 90-day bank statements | Standard commercial |
| 9 | Resimac Full Doc | Full financials + ATO + bank statements | Standard |
| 10 | Angle Full Doc (< $250k) | 6m bank statements OR FY24+FY23 financials + commitment schedule | Standard |
| 11 | BFS Full Doc (> $100k) | 2 years externally prepared financials | Larger loans |
| 12 | CFAL (standard, all sizes) | 2 years financials minimum; scales to 3 yrs + projections for > $500k | All commercial |
| 13 (hardest) | CFAL / Angle > $1m | Full package: cash flow projections, succession plan, competitor list | Large transactions |

---

## chunk_id: compare_loan_amounts
**layer:** 2
**intent:** COMPARE
**policy_field:** MAX_LOAN, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**borrower_profile:** ALL
**trigger_words:** "compare loan amounts", "who lends more", "highest loan limit", "maximum borrowing comparison", "which lender has higher limits"

**Content:**

| Borrower Profile | Best Lender | Max Available | Notes |
|----------------|------------|--------------|-------|
| New business < 12m ABN | BFS | $100k | New Business Ventures |
| New business < 2 yrs, primary asset only | Angle Start-Up | $150k | 20% deposit; industry experience required |
| ABN 1–2 yrs, renting | BFS Full Doc | $250k | — |
| ABN 2+ yrs, no property, vehicle | BFS or Metro (non-property, dealer) | $250k / $100k | BFS has no cap penalty for no-property; Metro caps at $100k with 30% deposit |
| ABN 2+ yrs, property owned, equipment | flexicommercial Credit Matrix | $750k aggregate (Primary) | Individual transaction still capped $500k |
| ABN 4–6 yrs, property, vehicle/EV | Resimac Premium/PremiumPLUS | $450k NAF | Full Doc |
| ABN 6+ yrs, property, primary asset | Angle Full Doc | $500k–$1m+ | Detailed business background required above $250k |
| Large corporate / equipment > $500k | CFAL | $1m+ | Full documentation required |
| High-value vehicle ≥ $250k, high credit | BFS High Value | $400k | Ultra Prime–Tier 2; 20% deposit |
| Existing customer, repeat streamlined deals | Metro | $750k aggregate exposure | Requires 24 months good repayment history; $500k/12-month rolling cap across all streamlined products |

═══════════════════════════════════════════════════════════════════
# LAYER 3 — RECOMMENDATION ENGINE
# Purpose: answer "which lender suits me?" queries
# Each chunk = a borrower scenario with scored lender recommendations
═══════════════════════════════════════════════════════════════════

## chunk_id: recommend_new_business_car
**layer:** 3
**intent:** RECOMMEND
**policy_field:** MIN_ABN, BASE_RATE, MAX_LOAN
**lenders:** BFS, RESIMAC, ANGLE
**borrower_profile:** NEW_BUSINESS, ABN_UNDER_1YR, ABN_1_2YR, COMMERCIAL
**asset_class:** MV_NEW, MV_USED, LCV
**trigger_words:** "new business car loan", "just started business vehicle", "startup car finance", "new ABN car loan", "which lender for new business"

**Content:**

**Scenario:** Borrower has < 2 years ABN and needs a vehicle for business use.

| ABN Duration | Recommended Lender | Product | Max Loan | Key Condition |
|-------------|-------------------|---------|---------|--------------|
| < 12 months | **BFS** | New Business Ventures | $100k | 90-day bank statements; CCR ≥ 400; 20% deposit if Tier 3–4 |
| 12–24 months | **BFS** | Full Doc | $250k | CCR ≥ 400; standard documentation |
| 1–2 years | **Resimac Basic** | Low Doc | $100k–$200k | ABN > 1 yr; GST > 1 yr; credit score ≥ 600 (company) |

**Why not Angle?** Angle's Start-Up product only funds primary assets (equipment), not motor vehicles — it is not a fit for a straight vehicle purchase.
**Why not CFAL, flexicommercial or Metro?** All three require ≥ 2 years ABN/GST as a hard floor before any channel opens up.

---

## chunk_id: recommend_renter_no_property
**layer:** 3
**intent:** RECOMMEND
**policy_field:** PROPERTY_REQUIRED, BASE_RATE, MAX_LOAN
**lenders:** BFS, RESIMAC, ANGLE, METRO, CFAL
**borrower_profile:** NO_PROPERTY, NON_PROPERTY_BACKED, RENTER, COMMERCIAL, CONSUMER
**asset_class:** ALL
**trigger_words:** "renting no property loan", "no property vehicle finance", "renter equipment loan", "don't own home equipment finance", "tenant business loan"

**Content:**

**Scenario:** Borrower is renting, does not own property, needs business or personal vehicle/equipment finance.

| Lender | Accessible? | Tier / Product | Notes |
|--------|-----------|---------------|-------|
| **BFS** | ✓ Best option | Any tier based on CCR score | No property requirement at any tier |
| Resimac | ✓ Limited | Standard or Basic only | Non-property-backed deposit: MV 10%, other 20% |
| Angle | ✓ Limited | Low Doc (< $100k) only | Non-property owners accepted here specifically; other tiers require property or spousal property |
| Metro | ✓ Capped | Streamlined (motor vehicles only) | $100,000 cap, 30% deposit, dealer sale only |
| CFAL (new to bank) | ✗ | Not accessible | Requires residential property for new-to-bank DriveXpress |
| CFAL (existing client) | ✓ | DriveXpress | Relationship history substitutes for property |
| flexicommercial | ⚠ With deposit | Credit Matrix | 20% deposit (or asset-backing) required for any non-property-backed deal |

**Recommendation:** BFS remains the primary lender for borrowers with no property at all — it is the only lender with zero property requirement across its entire tier structure. Angle's Low Doc and Metro's streamlined vehicle product are workable secondary options but both come with tighter caps or a steep deposit.

---

## chunk_id: recommend_low_credit_score
**layer:** 3
**intent:** RECOMMEND
**policy_field:** MIN_CREDIT_SCORE, DEPOSIT_REQUIRED
**lenders:** BFS, RESIMAC, ANGLE
**borrower_profile:** LOW_CREDIT, MID_CREDIT, DISCHARGED_BANKRUPT
**asset_class:** MV_NEW, MV_USED, LCV, PRIMARY
**trigger_words:** "bad credit car loan", "low credit score vehicle finance", "poor credit history equipment loan", "credit issues finance", "impaired credit"

**Content:**

**Scenario:** Borrower has a low credit score or adverse credit history.

| Score Range | Best Lender | Product | Rate Range | Conditions |
|------------|------------|---------|-----------|-----------|
| 960+ (Experian) / 650+ (Equifax/Veda) | BFS Ultra Prime / Resimac PremiumPLUS / Angle Mid Doc | Standard | 7.54–7.79% | Full eligibility required |
| 800–959 / 600–649 | BFS Tier 1 / Resimac Premium / Angle $400k Low Doc | Standard | 7.64–8.95% | — |
| 600–799 | BFS Tier 2 / Resimac Standard / Angle Low Doc (> $100k) | Standard | 7.89–11.35% | — |
| 550–599 | **BFS Tier 3** / Angle Low Doc (< $100k) / Angle Start-Up | Standard + 20% deposit | 10.15–12.90% (commercial) | 20% deposit required |
| 500–549 | **BFS Tier 4** | Standard + 20% deposit | 11.50%+ (commercial new) | No commercial used contracts; Angle auto-excludes below 500 |
| 400–499 | BFS only (Tier 4 floor is 400) | Restricted | 11.50%+ | Angle, Resimac auto-decline/referral in this band |
| < 400 | — | Auto-declined by BFS and Angle | — | CFAL/flexi/Metro at heavy credit discretion only (no published floor) |
| Discharged bankrupt | **BFS Plus** | Restricted products | Up to 17.15% | 20% deposit; > 12m post-discharge; no adverse history since |

**Note:** Resimac minimum Equifax score: Sole Trader 650 (Low Doc), 600 (Full Doc); Company 600 (Low Doc), 550 (Full Doc). Scores below these thresholds require referral. BFS remains the strongest published pathway across the full sub-prime range, including the only clear route for a discharged bankrupt.

---

## chunk_id: recommend_high_value_loan
**layer:** 3
**intent:** RECOMMEND
**policy_field:** MAX_LOAN, DEPOSIT_REQUIRED, MIN_ABN
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI
**borrower_profile:** HIGH_CREDIT, PROPERTY_BACKED, COMMERCIAL, EXISTING_CLIENT
**asset_class:** ALL
**trigger_words:** "large loan recommendation", "which lender for $300k", "who lends $500k", "large equipment finance lender", "high value loan lender"

**Content:**

**Scenario:** Borrower needs finance above $250k.

| Amount | Best Lender | Conditions |
|--------|------------|-----------|
| $250k–$400k (vehicle) | **BFS High Value** | CCR ≥ 800, 20% deposit, asset-backed |
| $250k–$450k (equipment, top tier) | **Resimac PremiumPLUS/Premium** | Full Doc; property-backed; ABN > 4–6 yrs |
| $250k–$500k (primary asset, established business) | **flexicommercial** (Credit Matrix / flexipremium) | Individual transaction up to $500k; asset-backed; 4+ yr ABN for flexipremium |
| $400k–$500k (existing lender relationship) | **CFAL DriveXpress (existing client)** or **Metro** (12–24m history) | Relationship/repayment history substitutes for fresh financials |
| $500k–$750k | **Angle Full Doc** or **flexicommercial** (18-payment unlock) | Angle: detailed business background, aged debtor/creditor listing; flexi: perfect conduct on a prior $250k+ contract |
| $500k–$1m | **CFAL** | 3 years financials; ATO portal |
| > $1m | **CFAL** or **Angle** | Full financial package including projections and (for CFAL) succession plan |

---

## chunk_id: recommend_best_ev_lender
**layer:** 3
**intent:** RECOMMEND
**policy_field:** BASE_RATE, EV_DISCOUNT, MAX_TERM
**lenders:** RESIMAC, BFS, METRO
**borrower_profile:** COMMERCIAL, CONSUMER
**asset_class:** EV, SOLAR
**trigger_words:** "best lender for electric vehicle", "EV loan recommendation", "which lender for Tesla", "electric vehicle finance comparison", "green vehicle loan", "solar finance recommendation"

**Content:**

**Scenario:** Borrower wants to finance an electric vehicle (or a green bundle) and wants the best overall deal.

| Priority | Best Lender | Rate | Term | Why |
|---------|------------|------|------|-----|
| Lowest rate, commercial | **Resimac PremiumPLUS** | 7.54% | Up to **84 months** | Only lender combining lowest EV rate with extended Green Goods term |
| Consumer borrower | **BFS Consumer** | From 9.15% (Ultra Prime) | Up to 84m | BFS and Metro are the only lenders in the group accepting personal (non-ABN) EV borrowers |
| Consumer, longest term | **Metro MetroEco** | MetroEco discount off carded rate | Up to **84m, max EOT 7 years** | Longest published consumer EV term |
| Bundling EV + charger, or EV + solar | **Metro MetroEco** | MetroEco discount | Up to 7-yr term (solar) | Only lender that bundles EV/charger/solar on one application |
| Electric truck (3.5t+) | **Metro MetroEco Electric Trucks** | 1% MetroEco discount off standard rate | Up to $250k–$300k | Property owners only; excludes hybrid/biofuel |
| Low credit score | **BFS Tier 3–4** | 10.15–12.50% | Up to 84m | No property required; CCR 400 accepted |
| Flexible eligibility, no property | **BFS** | Varies by tier | Up to 84m | No property; accepts sub-prime; commercial + consumer |

**Combined recommendation:** For a straightforward commercial EV purchase with strong ABN/property, Resimac PremiumPLUS is cheapest overall. For a consumer buyer, or for a borrower wanting to bundle an EV with a home charger or solar system, Metro's MetroEco suite is the strongest single-application option. Angle and flexicommercial have no EV-specific offer and should not be recommended for this scenario.

---

## chunk_id: recommend_prime_mover_and_heavy_transport
**layer:** 3
**intent:** RECOMMEND
**policy_field:** BASE_RATE, MIN_ABN, MIN_CREDIT_SCORE
**lenders:** ANGLE, RESIMAC, FLEXI, METRO
**borrower_profile:** COMMERCIAL, PROPERTY_BACKED, TRANSPORT_OPERATOR
**asset_class:** PRIME_MOVER, PRIMARY
**trigger_words:** "prime mover finance", "truck fleet loan", "which lender for a prime mover", "transport business loan", "road transport finance"

**Content:**

**Scenario:** Borrower runs a transport/logistics business and wants to finance a prime mover.

| Priority | Best Lender | Rate/Terms | Conditions |
|---------|------------|-----------|-----------|
| Lowest headline rate | **Angle Prime Movers** | From 9.39% (1% loading on primary rate) | Company/Trust only (no sole traders); 5+ yr ABN & GST; 600+ credit score; property backed; fleet credit limit available |
| Established Road Transport/Logistics operator (5+ trucks) | **flexicommercial flexipremium** | 7.30%–8.19% base + 1.0% prime mover add-on | Road Transport/Logistics businesses operating 5+ trucks can access flexipremium's primary-asset pricing even on newer used trucks (up to 5 yrs old) |
| Standard / smaller operator | **Resimac** | Primary rate + 2% risk loading | Property-backed guarantor always required for prime movers at Resimac |
| Refinancing a balloon on an existing prime mover | **Metro Balloon/Residual Refinance** | Standard rates | Only Metro product that explicitly includes prime movers; no inspection required |

**Why not BFS or CFAL?** Neither lender finances prime movers — BFS is vehicles-only (< 4.5T GVM) and CFAL's Category B (trucks > 4.5T) explicitly does not extend to prime movers in the source documentation supplied.
**Why not Metro's Trucks & Trailers streamlined product?** It explicitly excludes prime movers — a borrower must use Metro's Balloon/Residual Refinance (existing contracts only) or the general rate-sheet product instead.

---

## chunk_id: recommend_medical_professional
**layer:** 3
**intent:** RECOMMEND
**policy_field:** MAX_LOAN, PROPERTY_REQUIRED
**lenders:** CFAL, FLEXI
**borrower_profile:** MEDICAL_PROFESSIONAL, COMMERCIAL, NEW_CLIENT
**asset_class:** MEDICAL_EQUIP, MV_NEW
**trigger_words:** "doctor finance recommendation", "which lender for medical equipment", "dentist equipment loan", "GP practice finance"

**Content:**

**Scenario:** A GP, dentist, vet or allied health practitioner wants to finance new medical equipment or a practice vehicle.

| Profession | Best Lender | Max Loan | Why |
|-----------|------------|---------|-----|
| Medical Specialist / GP / Dental / Vet | **CFAL Medical channel** | < $350k (medical equipment) / < $500k cumulative | Purpose-built professional channel with the highest published limits in the group; new clients need property + $75k income |
| Allied Health Practitioner | **CFAL Medical channel** | < $150k per asset / < $250k cumulative | Still the only dedicated medical channel, though limits are lower than for specialists |
| Pharmacist | **Not CFAL** — use standard commercial channels | — | CFAL explicitly excludes pharmacists from its Medical channel; fall back to Resimac Full Doc, Angle Full Doc, or flexicommercial's Secondary asset category (medical/dental/lab equipment) with no professional-specific limit |

**Why not other lenders?** None of Resimac, BFS, Angle, flexicommercial or Metro publish a profession-specific medical program — a medical professional outside CFAL's channel is simply assessed under each lender's general commercial criteria (flexicommercial does list "medical/dental/laboratory equipment" as an eligible Secondary asset, but with no special pricing or limits tied to the borrower's profession).

---

═══════════════════════════════════════════════════════════════════
# LAYER 4 — POLICY DIFFERENCE ANALYSIS
# Purpose: answer "how do these lenders differ on X?" queries
# Each chunk = one policy dimension, delta-focused
═══════════════════════════════════════════════════════════════════

## chunk_id: diff_tier_logic
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** MIN_ABN, MIN_CREDIT_SCORE, PROPERTY_REQUIRED
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**trigger_words:** "how do lenders tier customers differently", "what makes each lender different", "tier comparison", "eligibility differences between lenders"

**Content:**

**Core difference: what each lender uses as its primary filter**

| Lender | Primary Filter | Why it matters |
|--------|--------------|---------------|
| Resimac | Property-backing type + ABN duration | Borrowers without property are locked out of the top two tiers regardless of credit score or income |
| BFS | Experian CCR score alone | Most meritocratic; a borrower with CCR 960 and 6 months ABN can access better rates than a 10-year business with CCR 550 at Resimac |
| CFAL | Relationship history + transaction size | Rewards loyalty; new-to-bank clients face strict eligibility (property + income) even with good credit |
| Angle | Credit score × ABN duration × requested exposure, layered together | The most multi-dimensional gate in the group — a strong score alone does not unlock higher exposure without matching ABN age, and vice versa |
| flexicommercial | Exposure band on the Credit Matrix | No discrete "tiers" as such — requirements (ABN/GST duration, deposit, repayment history) scale continuously as the requested amount rises through defined bands |
| Metro | Property status × prior repayment history with Metro specifically | The only lender whose best pricing/exposure is earned mainly through *repeat business with Metro itself* (12m and 24m history unlocks), rather than external credit history |

**The single biggest eligibility difference across all six lenders:**
BFS is the only lender that never requires property ownership at any tier. Every other lender either mandates it outright at the top tier (Resimac, CFAL new-to-bank) or uses it to unlock materially better pricing/exposure (Angle, flexicommercial, Metro). This is the most important differentiator for borrowers who rent or do not own property.

---

## chunk_id: diff_asset_class_coverage
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** ASSET_AGE_MAX
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**trigger_words:** "which lender covers the most asset types", "asset class differences", "who finances what", "widest range of equipment lender"

**Content:**

**The starkest structural difference in the group is asset-class coverage, not pricing:**

| Lender | Vehicles | Heavy/Primary Equipment | Secondary/Tertiary | Prime Movers | Medical | Green/EV |
|--------|:--------:|:------------------------:|:-------------------:|:-------------:|:-------:|:--------:|
| Resimac | ✓ | ✓ | ✓ | ✓ (+2%) | — | ✓ Best rate + 84m |
| BFS | ✓ **only** | ✗ | ✗ | ✗ | — | ⚠ Same tiers, no discount |
| CFAL | ✓ Cat A | ✓ Cat B/C | — | ✗ | ✓ Dedicated channel | — |
| Angle | ✓ | ✓ | ✓ | ✓ Dedicated product | — | — |
| flexicommercial | ✗ **never** | ✓ | ✓ | ✓ (+1%) | ⚠ Secondary only, no dedicated program | — |
| Metro | ✓ | ✓ (5 streamlined products) | ⚠ Other Equipment only | ⚠ Refinance only | — | ✓ MetroEco (EV+trucks+solar) |

**Delta summary:** BFS and flexicommercial sit at opposite extremes — BFS finances *only* vehicles, while flexicommercial finances *everything except* vehicles. A broker choosing between the two based on asset type alone will almost never have both as valid options for the same deal. Resimac and Angle are the two genuine "full-range" lenders, covering vehicles through to prime movers with no major asset-class gap.

---

## chunk_id: diff_private_sale_policy
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** PRIVATE_SALE_LOADING, ASSET_AGE_MAX
**lenders:** RESIMAC, BFS, ANGLE, FLEXI, METRO
**trigger_words:** "private sale differences", "buying privately lender comparison", "which lender is better for private sale", "private seller policy differences"

**Content:**

| Aspect | Resimac | BFS | Angle | flexicommercial | Metro |
|--------|---------|-----|-------|------------------|-------|
| Rate loading | **+2.00%** | **+0.50%** | **0% — none** | +1.0% | +0.25% |
| Asset types allowed | All asset classes | All vehicle types | All (motor vehicles + primary/secondary on exception) | Primary standard; Secondary/Tertiary exception basis only | Motor vehicles (property-backed only — non-property backed is dealer sale only) |
| Inspection required? | No | ✓ DoxAI or Redbook | ✓ Verimoto/Redbook/Olasio/Broker Inspection | Not separately specified | Not separately specified |
| Max loan (private sale) | Per standard limits | $150k | Per standard limits | Per Credit Matrix, with $745 fee | Not available without property backing |
| Fee premium | $200 extra ($695 total) | $100 extra ($675 total) | None — same $649 fee as dealer sale | $250 extra ($745 vs $495) | Not separately stated |

**Delta summary:**
- Angle has both the smallest private sale rate loading (**zero**) and no separate fee premium — the clear standout for a private-sale purchase
- Metro has the narrowest private sale scope (property-backed only) but the smallest of the four published non-zero loadings (+0.25%)
- Resimac carries the highest private sale loading (+2%) of any lender in the group, though it requires no formal inspection
- flexicommercial pairs a moderate rate loading (+1.0%) with the largest fee premium ($250 extra)

---

## chunk_id: diff_ev_policy
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** EV_DISCOUNT, MAX_TERM, BASE_RATE
**lenders:** RESIMAC, BFS, METRO
**trigger_words:** "EV policy differences", "electric vehicle lender comparison", "which lender is better for EV", "compare EV rates", "electric car loan differences"

**Content:**

| Aspect | Resimac | BFS | Metro |
|--------|---------|-----|-------|
| EV rate mechanism | Separate lower rate category (–0.10% vs ICE) | Same rate table as ICE (no explicit EV discount published) | MetroEco discount applied to the vehicle's carded rate |
| Best EV rate | 7.54% (PremiumPLUS) | 7.60% (Ultra Prime commercial) | Discount off carded rate — exact figure varies by vehicle |
| EV extended term | ✓ **84 months** (Green Goods) | 84 months (standard, not EV-specific) | Consumer: 84 months, max EOT **7 years** (longest published EOT of the three) |
| Electric motorbikes | Not addressed | ✓ Accepted if speed > 80 km/h | Not addressed |
| Consumer EV | ✗ Commercial only | ✓ Consumer + commercial | ✓ Consumer + commercial + novated (FBT exemption applies) |
| Bundling (EV + charger/solar) | ✗ | ✗ | ✓ **Only lender offering this** |
| Electric trucks | Not a separate category | Not addressed | ✓ Dedicated product (3.5t+, battery only, property owners only) |

**Delta summary:**
- Metro is the only lender offering a genuinely broad green-finance ecosystem (EV, electric truck, solar/battery/charger, novated leasing with FBT exemption) rather than a single discounted vehicle line
- Resimac is the only lender to extend the loan term specifically for EV/green goods on a straight commercial purchase (84 months)
- BFS is the only lender allowing individual consumers to finance EVs without any green-specific discount at all — its EV appeal rests entirely on its no-property, sub-prime-friendly tier structure, not on pricing

---

## chunk_id: diff_documentation_by_lender
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** MIN_ABN
**lenders:** RESIMAC, BFS, CFAL, ANGLE, FLEXI, METRO
**trigger_words:** "document requirements difference", "which lender needs less paperwork", "documentation comparison lenders", "easiest lender to apply", "most paperwork required"

**Content:**

**What each lender uniquely requires vs the others:**

| Lender | Unique requirement | Not required by others |
|--------|-------------------|----------------------|
| Resimac | Privacy consent must note specific URL (resimacassetfinance.com.au); signed < 90 days | No other lender specifies a URL requirement |
| Resimac Lite Doc | BAS annualised turnover > 2.5× asset price | No other lender has this specific turnover multiple test |
| BFS | Biometric verification via QuickSell link | Resimac, Angle and CFAL's standard channel do not require biometrics (CFAL DriveXpress does) |
| BFS Low Doc | Business Customer Financial Declaration (BFS-specific form) | Other lenders use generic financial statements |
| CFAL | Affordability Declaration (DriveXpress) | Other lenders assess affordability internally without a signed declaration, except Metro (implicit via Equifax) |
| CFAL > $500k | Commentary on financial movements ≥ 10% | No other lender requires this specific commentary |
| CFAL > $1m | Succession planning details + major competitor/client list | No other lender requests these |
| Angle | Rates notice (within last 3 months) as proof of property, alongside a marriage certificate/Medicare card/joint utility bill for spousal property | Most granular published spousal-property evidence list of any lender |
| Angle Mid Doc | Explicit bank-statement "pre-qualification" test: no dishonours, ≤1 non-financial dishonour, $20,000+ average monthly revenue, running balance ≥ 10% of revenue | No other lender publishes this specific pass/fail bank-statement formula |
| flexicommercial | Explicit exclusion of specific asset brands/types by name (SUVs, photocopiers, MFDs, scaffolding) rather than a positive-only asset list | Other lenders describe eligible assets positively; flexi is unusually explicit about what it will *never* fund |
| Metro | "Comparable credit reference" from a reputable finance company running ≥ 12 months, used as a direct substitute for financials across all six streamlined products | No other lender operationalises credit-reference substitution this consistently across its entire product suite |

---

## chunk_id: diff_sub_prime_and_adverse_credit
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** MIN_CREDIT_SCORE, DEPOSIT_REQUIRED
**lenders:** RESIMAC, BFS, CFAL, ANGLE
**trigger_words:** "bad credit lender differences", "which lender accepts poor credit", "adverse history lender comparison", "sub-prime lender comparison", "bankrupt lender differences"

**Content:**

**Sub-prime and adverse credit: how lenders differ**

| Scenario | Resimac | BFS | CFAL | Angle |
|---------|---------|-----|------|-------|
| Score 550–649 (mid-band) | ⚠ Company/guarantor ≥ 550 (Full/Lite Doc) | ✓ Tier 3 (+ 20% deposit) | ⚠ At discretion | ✓ Low Doc (< $100k) / Start-Up |
| Score 500–549 | ⚠ At discretion (< 450 may decline) | ✓ Tier 4 (+ 20% deposit) | ⚠ At discretion | ⚠ Exposure capped < $150k |
| Score < 500 | ✗ Likely decline below 450 | ✗ Auto-decline below 400 | ⚠ At heavy discretion | ✗ Auto-decline below 500 |
| Discharged bankrupt (< 10 yrs) | ✗ Excluded | ✓ BFS Plus (+ 20% deposit; 12m+ post-discharge; no adverse since) | ⚠ At discretion | Not addressed in source docs |
| Current bankrupt | ✗ Excluded | ✗ Auto-decline | ✗ Excluded | Not addressed (implied excluded via credit file test) |
| Financial default on file | ⚠ Assessed | ✓ BFS Plus eligible depending on RHI | ⚠ At discretion | ✗ Excluded (except telco/utilities paid up to $2,500) |
| ATO debt / payment plan | ✓ Resimac Lite Doc (< 10% turnover, plan > 3m) | ⚠ At discretion | ✗ Not permitted | Not explicitly addressed (ATO portal required ≥ $250k) |

**Delta summary:** BFS has the highest published tolerance for sub-prime and adverse credit, and remains the only lender with an explicit discharged-bankrupt pathway. Angle has the second clearest published sub-prime floor (score 500) but pairs it with the strictest default policy of the four — any financial default beyond a small telco/utility threshold is an automatic exclusion, regardless of score. Resimac offers the ATO-debt pathway via Lite Doc that none of the others match. CFAL has no published sub-prime channel at all.

---

## chunk_id: diff_replacement_and_fast_track_products
**layer:** 4
**intent:** DIFFERENCE
**policy_field:** REPLACEMENT_LOADING, STREAMLINED_ANNUAL_CAP
**lenders:** CFAL, FLEXI, METRO
**trigger_words:** "replacement policy differences", "rollover vs replacement", "streamlined product comparison", "fast track finance differences"

**Content:**

The three lenders with the richest fast-track/replacement product suites differ significantly in structure:

| Aspect | CFAL | flexicommercial | Metro |
|--------|------|------------------|-------|
| Number of distinct fast-track/replacement products | 3 (DriveXpress, Rollover, Replacement) | 3 (flexireplacement, Mid-term Refinancing, Low Start Loans / Old Finance Meets New) | 6 (Passenger Vehicle, Trucks & Trailers, Agri, Other Equipment, Replacement, Balloon/Residual Refinance — all "streamlined") |
| Repayment increase cap | 125% (new-to-bank) / 150% (existing) | 125% of repayment being replaced | 125% of original loan amount **or** monthly repayment |
| Minimum age of contract being replaced | 12 months (Rollover) | 18 months (flexireplacement) | 36 months (Replacement) / final 12 months only (Balloon/Residual) |
| Aggregate annual cap | Not published as a shared pool | Not published as a shared pool | **$500,000 shared across all six streamlined products in any 12-month period** |
| New-to-bank eligible? | ✓ Replacement only (Rollover is existing-clients-only) | ✗ Not addressed — flexireplacement implies an existing facility with an "approved lender", not necessarily flexi itself | ✓ Replacement and Balloon/Residual both accept new customers, at lower caps than existing-customer tiers |
| Inspection requirement | Not specified | Required if balloon > $300K | **Not required** for Balloon/Residual Refinance specifically |

**Delta summary:** Metro's suite is the broadest by product count but is the only one of the three capped by a single shared annual ceiling — a borrower who is heavy-streamlined-product user with Metro will hit that $500k wall faster than an equivalent CFAL or flexicommercial borrower spreading similar volume across those lenders' uncapped-aggregate channels. flexicommercial's 18-month minimum contract age is the strictest "how long ago" gate of the three.

---
