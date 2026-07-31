# CFAL Policy Verification Findings
**Date:** 31 July 2026

This document records the verification results for several issues raised during the audit of the CFAL RAG chunks. Each finding has been cross-checked against the official policy documents currently available.

---

# 1. Repairable Write-offs

## Audit Finding

The audit suggested that the following exclusion recorded in the CFAL chunk could not be verified:

> Repairable write-offs

After checking every CFAL source document currently available, **there is no evidence that this exclusion belongs to CFAL policy.**

The only CFAL document currently available is:

> **Your CFAL Equipment Finance Credit Team – Checklist – Minimum Documentation Requirements**

This document is purely a documentation checklist organised by transaction size (Matrix / ≤$250k / >$250k–$500k / >$500k–$1m / >$1m).

It contains:

- Client Information
- ABN requirements
- Financial Statements
- Tax Returns
- Supporting documentation

There is **no Asset Categories section**, **no Exclusions section**, and the phrase **"Repairable write-offs" never appears anywhere**.

### Actual Source

The phrase actually comes from **Resimac Asset Finance – Commercial Product Guide (Effective 27 March 2026)**.

Page 7 lists:

> Excludes  
> Ride share, taxis and repairable writeoffs

Therefore:

- ❌ Not supported by any CFAL source currently available.
- ✅ Explicitly supported by the Resimac Product Guide.

### Recommendation

Unless another official CFAL policy document is located, this exclusion should be removed from the CFAL chunk and remain only within the Resimac policy.

### Evidence

![Resimac Asset Categories](images/resimac_asset_categories.png)

---

# 2. Geographic Exclusions (Remote / Very Remote)

## Audit Finding

The audit questioned whether the following rules belong to CFAL:

- Remote (ABS 2021 classification)
- Very Remote not available
- 20% deposit requirement

After verification:

These rules are **not CFAL policy**.

They originate from:

> **BFS Product Guide – Broker (Effective 1 July 2026)**

Original wording:

- "Remote" as per ABS classification (2021 Remoteness Area)
- Not available in "Very Remote" areas
- Non-asset backed requires a 20% deposit

This wording matches our chunk almost exactly.

### Important Clarification

One important detail should be retained:

The original policy states:

> **Non-asset backed requires a 20% deposit**

It **does not** state that **all** Remote Area applications require a 20% deposit.

If the chunk has simplified this into:

> Remote Areas require a 20% deposit

then that statement is inaccurate and should be corrected.

### Recommendation

Remove this section from the CFAL chunk.

Keep it only under BFS policy.

### Evidence

![BFS Remote Areas](images/bfs_remote_areas.png)

---

# 3. Standard Settlement Requirements

## Audit Finding

The settlement section currently contains items such as:

- QuickSell
- Biometrics
- Tax Invoice
- Fully Signed Loan Documents

After verification, these are **not CFAL settlement requirements**.

They are copied directly from:

> **BFS Product Guide – Standard Documentation Requirements**

Original wording includes:

- All payout documents submitted via QuickSell
- Completion of biometrics
- Vehicle tax invoice
- Loan documents fully signed

These statements match the BFS policy almost word-for-word.

### Source Confusion

The current chunk appears to mix together two completely different organisations.

**BFS**

- QuickSell
- Biometrics
- Settlement checklist

**Westpac / CFAL**

- DriveOnline
- Separate documentation process

Additionally,

The official CFAL update document

> UPDATEDEquipmentFinanceSettlementRequirements.pdf

contains only two policy changes effective 24 February 2025:

- PPSR Search exemption
- CoC Fleet Policy exemption

There is **no settlement checklist** anywhere in that document.

### Recommendation

This section appears to be a multi-source mix-up.

It should be removed from CFAL and remain under BFS documentation only.

### Evidence

#### BFS Standard Documentation Requirements

![BFS Settlement](images/bfs_standard_documentation.png)

#### Westpac Key Policies

![Westpac Exclusions Notes](images/westpac_exclusions_notes.png)

---

# 4. Rollover Original Funder ($500k Limit)

## Audit Finding

The audit questioned whether the $500k rollover limit applies to both:

- Westpac
- CFAL

After checking the original table in:

> **Westpac Equipment Finance Key Policies**

the wording is unambiguous.

| Customer Type | Maximum Loan | Original Funder | Eligible Goods |
|---------------|-------------|-----------------|----------------|
| Existing Clients | $500k | **Westpac** | All |
| Existing Clients | $250k | Other Financier | A & B |

The table **only mentions Westpac**.

CFAL is **never referenced**.

Therefore there is currently **no evidence** that CFAL-originated contracts qualify for the same $500k rollover policy.

### Recommendation

Until an official CFAL rollover policy is found,

the chunk should state:

> Applicable to Westpac-originated contracts only.

rather than

> Westpac / CFAL originated contracts.

### Evidence

![Westpac Rollover Table](images/westpac_rollover.png)

---

# Overall Conclusion

The verification confirms that several disputed statements currently labelled as CFAL policy are actually sourced from other lenders.

| Issue | Verification Result |
|---------|---------------------|
| Repairable write-offs | Resimac policy, not CFAL |
| Remote / Very Remote | BFS policy, not CFAL |
| QuickSell Settlement | BFS policy, not CFAL |
| DriveOnline | Westpac platform |
| $500k Rollover | Westpac only (CFAL unsupported) |

At present, none of these statements can be verified using the official CFAL documentation currently available.

Unless additional CFAL source documents become available, these items should either be removed from the CFAL chunks or reassigned to their correct lender policy.
