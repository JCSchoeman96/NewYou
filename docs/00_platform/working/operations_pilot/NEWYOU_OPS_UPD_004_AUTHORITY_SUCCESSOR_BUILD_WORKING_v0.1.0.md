# NewYou OPS-UPD-004 — Formal Authority Successor Build Working v0.1.0

> **WORKING / NON-AUTHORITATIVE BUILD CONTRACT**  
> **DETERMINISTIC SUCCESSOR PATCHSET — DOES NOT CHANGE CURRENT ROUTING**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.1.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact `main` baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch before build:** `b22edeb06ce409acbdf518e6686a772b8a058bf1`
- **Source Product blob:** `00_PLATFORM_v1.6.0.md` = `bb98081841b432a5a3d5e961929acf494ac9c8ba`
- **Source Decisions blob:** `01_DECISIONS_v1.6.0.md` = `85402cb169e095771f03482981d0691e08efb021`
- **Corrected semantic candidate:** `NEWYOU_OPS_UPD_004_AUTHORITY_PROMOTION_CANDIDATE_WORKING_v0.2.0.md`
- **Purpose:** define an exact, minimal, mechanically reviewable transformation from current Product/Decision authority to the proposed `v1.7.0` successors without changing current README/manifest routing in this pass.

---

# 1. Build doctrine

This build is deliberately expressed as a deterministic patch contract against exact source blob SHAs.

Why:

- current `v1.6.0` authority must remain current until successor review/promotion;
- historical predecessor bytes must be preserved rather than edited in place;
- the semantic repair is small and should be reviewable as a small diff rather than by re-legislating unrelated Product Law;
- no Roadmap, Architecture or Domain semantic successor is justified by this conflict repair.

A future materialisation/promotion step must generate the cumulative successor files from these exact source blobs and prove the resulting diff matches this contract exactly before routing them as current.

---

# 2. Target Product successor

**Target filename:** `docs/00_platform/00_PLATFORM_v1.7.0.md`  
**Source:** exact bytes of `00_PLATFORM_v1.6.0.md` blob `bb98081841b432a5a3d5e961929acf494ac9c8ba`  
**SemVer:** substantive MINOR successor `v1.6.0 → v1.7.0`

Only the following Product changes are authorised by this build.

## P-01 — Header/version metadata

Set:

```text
# 00_PLATFORM_v1.7.0.md
Document status = FROZEN PRODUCT BASELINE v1.7.0
Document version = v1.7.0
Predecessor = archive/00_PLATFORM_v1.6.0.md
SemVer transition = v1.6.0 → v1.7.0
Last updated = 2026-10-10
Decision coverage = existing coverage plus approved post-freeze DEC-313 amendment
Related Decisions document = 01_DECISIONS_v1.7.0.md
```

The related Open Work path may remain the current source-at-build `02_OPEN_WORK_v1.2.59.md`; a later status/routing successor may update it during promotion. No Product semantics depend on that metadata field.

## P-02 — Add v1.7.0 Amendment Scope before preserved v1.6.0 history

Exact intended scope text:

```text
## v1.7.0 Amendment Scope

This substantive Product successor repairs the assessment-credit consumption contradiction exposed by OPS-UPD-004. It preserves prior Product Law except for the explicit assessment-credit claim/closure/consumption refinement: first-answer save claims/holds the existing ordinary paid assessment credit without consuming it; successful digital assessment delivery consumes exactly once when the immutable governed result and paid report are durably available to the authorised participant; pre-first-answer expiry leaves the credit available unused; post-first-answer nontechnical expiry closes the credit unconsumed; and genuine technical failure preserves the same paid obligation for controlled recovery or the existing technical-failure refund path. DEC-313 records the decision. The amendment changes no methodology, scoring, annual retake interval, Domain ownership, Architecture, provider/channel policy or legal-sufficiency finding.
```

## P-03 — Replace only the two conflicting §21B.3 bullets

Find exact current text:

```text
- The entitlement is not consumed until the first answer is saved.
- Once the first answer is saved, the entitlement is marked used.
```

Replace with:

```text
- Saving the first answer claims/holds the existing ordinary paid assessment credit for that active or recoverable attempt; it does not consume the credit.
- Assessment-credit availability, closure and consumption follow §21R.6 and DEC-313.
```

No other §21B.3 bullet changes.

## P-04 — Add §21R.6 immediately after current §21R.5

Exact intended normative section:

```text
## 21R.6 Assessment-credit claim, delivery, closure and consumption

Assessment attempt/result/report state and commercial credit state are separate. An ordinary paid assessment credit may be unavailable for another attempt or sale while still commercially unconsumed.

| Assessment-credit situation | Product consequence |
|---|---|
| valid ordinary paid credit; no first answer saved | `available_unused` |
| first answer saved; attempt active/recoverable; no successful delivery | `held_unconsumed` |
| immutable governed result exists but paid report is not yet durably participant-available | `held_unconsumed` |
| immutable governed result and paid report are both durably available to the authorised participant through the approved access path | `consume_exactly_once` |
| attempt expires before first answer | `release_to_available_unused` |
| attempt expires after first answer; no successful delivery; no live genuine technical-recovery case | `close_unconsumed` |
| genuine technical failure under controlled recovery | `preserve_same_paid_obligation; recover_existing_lineage_where_present` |
| valid technical-failure refund | `close_credit_after_refund; not_delivery_or_consumption` |
| notification/provider failure after qualifying in-product delivery | `no_change_to_consumption_truth` |
| participant never opens/views an otherwise qualifying result/report | `no_change_to_consumption_truth` |

Saving the first answer claims/holds the existing ordinary paid credit; it does not consume it. Successful digital assessment delivery is the durable availability of both the immutable governed digital result and the paid digital report to the authorised participant through the approved participant-access path. Temperament owns attempt, result and report truth; Entitlements owns current assessment-credit/right truth; Identity & Access governs access assurance. Notification/provider acceptance or delivery, result creation alone, report generation alone, and participant open/read/view telemetry do not independently establish consumption.

A qualifying delivery consumes the ordinary paid assessment credit exactly once. If the attempt expires before the first answer, the attempt ends and the credit remains available unused. If it expires after the first answer without successful delivery and no genuine technical-recovery case remains live, the attempt ends and the credit closes unconsumed. Closure is not delivery or consumption. Genuine technical failure preserves one paid obligation for controlled recovery of the same lineage where one exists, or follows the existing technical-failure refund path. A valid technical-failure refund closes the affected right and is not recorded as delivery or consumption.

Refundability remains governed separately by DEC-045. The annual retake interval in DEC-034 remains separate and unchanged; this amendment does not redefine its clock. The assessment-completion metric remains separate from commercial credit consumption and cannot become Entitlements authority. Duplicate/retried submission, recovery, report availability, delivery processing or consumption signals must converge on one logical credit/result/report lineage and may not create duplicate rights, immutable results/reports or consumption.

The lifecycle labels in this section are Product semantics, not mandated database enums, tables, Ash Resources or action names.
```

## P-05 — Internal current-version consistency

In §24, replace only the sentence:

```text
Current Product Law is v1.6.0.
```

with:

```text
Current Product Law is v1.7.0.
```

No Development Entry condition is weakened or otherwise changed.

---

# 3. Target Decision Register successor

**Target filename:** `docs/00_platform/01_DECISIONS_v1.7.0.md`  
**Source:** exact bytes of `01_DECISIONS_v1.6.0.md` blob `85402cb169e095771f03482981d0691e08efb021`  
**SemVer:** substantive MINOR successor `v1.6.0 → v1.7.0`

Only the following Decision Register changes are authorised.

## D-01 — Header/version metadata

Set:

```text
# 01_DECISIONS_v1.7.0.md
Document status = FROZEN PRODUCT DECISION REGISTER v1.7.0
Document version = v1.7.0
Predecessor = archive/01_DECISIONS_v1.6.0.md
SemVer transition = v1.6.0 → v1.7.0
Decision coverage = existing coverage plus DEC-313
Last updated = 2026-10-10
Related Product document = 00_PLATFORM_v1.7.0.md
```

## D-02 — Add v1.7.0 Amendment Scope before preserved v1.6.0 history

Exact intended scope text:

```text
## v1.7.0 Amendment Scope

This substantive successor preserves prior decision history, explicitly supersedes DEC-055 with DEC-313 for ordinary paid assessment-credit claim, closure and consumption semantics, and appends DEC-313. It changes no assessment methodology, scoring, annual retake interval, Architecture, Domain ownership, provider/channel policy or legal-sufficiency conclusion.
```

## D-03 — Preserve DEC-055 historically but mark current supersession

Replace current DEC-055 block:

```text
## DEC-055 — Entitlement consumption
**Status:** LOCKED
Do not consume the entitlement until the first answer is saved. Mark it used once the attempt begins.
```

with:

```text
## DEC-055 — Entitlement consumption
**Status:** SUPERSEDED BY DEC-313
Historical DEC-055 wording: “Do not consume the entitlement until the first answer is saved. Mark it used once the attempt begins.” Current assessment-credit claim, closure and consumption semantics follow DEC-313 and Product Law §21R.6.
```

## D-04 — Append DEC-313 after DEC-312 and before Open Gates

Exact intended decision:

```text
## DEC-313 — Assessment-credit claim, closure and consumption
**Status:** LOCKED
An ordinary paid digital-assessment credit is not consumed when an assessment attempt is admitted or when the first answer is saved. Saving the first answer claims/holds the existing credit for the active or recoverable attempt. A claimed credit remains commercially unconsumed but is unavailable for another ordinary assessment purchase or independent attempt.

Successful digital assessment delivery occurs when the participant's immutable governed digital result and the paid digital report permitted by current Product Law have both been durably made available to the authorised participant through an approved participant-access path. Temperament owns attempt, result and report truth; Entitlements owns the assessment-credit/right state; Identity & Access governs access assurance. Participant open/read/view behaviour is not required. Notification-provider acceptance, notification delivery, result creation alone and report generation alone do not independently establish this consumption event.

The ordinary paid assessment credit is consumed exactly once at successful digital assessment delivery. If an attempt expires under DEC-056 before the first answer has been saved, the attempt ends and the credit remains available and unused. If an attempt expires after the first answer has been saved without successful delivery and the case is not still governed as a genuine technical-failure recovery, the attempt ends and the credit closes unconsumed. Closure is neither successful delivery nor consumption; ordinary refundability remains governed separately by DEC-045.

A genuine technical failure resolves through controlled recovery of the same paid obligation and existing result/report lineage where one exists, or through the existing technical-failure refund path. Recovery must not mint a duplicate credit, immutable result, report or consumption. A valid technical-failure refund closes the affected credit/right and is not recorded as delivery or consumption. Duplicate or retried submission, result/report recovery, delivery processing and consumption signals must converge on one logical paid credit/result/report lineage and may consume at most once.

DEC-034, DEC-045, DEC-054, DEC-056, DEC-057, DEC-061, DEC-066, DEC-067 and DEC-303 otherwise remain unchanged. DEC-313 supersedes DEC-055 for assessment-credit claim, closure and consumption semantics only.
```

---

# 4. Explicit non-changes

This build does **not** authorise or require semantic changes to:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`;
- `03_ARCHITECTURE_v1.1.1.md`;
- `04_DOMAIN_MAP_v1.2.0.md`;
- FP-003 Roadmap semantics in `05_ROADMAP_v1.2.0.md`;
- methodology/scoring/tie/mask rules;
- `DEC-034` retake interval or its clock;
- refund rules beyond composing with existing `DEC-045`;
- provider/channel selection;
- operator permission policy;
- implementation representation.

When/if the Product/Decision successors are promoted, downstream routing/reference documents may need non-semantic PATCH successors so they no longer identify `v1.6.0` as current.

---

# 5. Materialisation acceptance checks

A future materialisation of this build must fail closed unless all checks pass:

1. source Product blob is exactly `bb98081841b432a5a3d5e961929acf494ac9c8ba`;
2. source Decisions blob is exactly `85402cb169e095771f03482981d0691e08efb021`;
3. cumulative target files are named exactly `00_PLATFORM_v1.7.0.md` and `01_DECISIONS_v1.7.0.md`;
4. Product diff contains only P-01...P-05 plus mechanically necessary line-context changes;
5. Decisions diff contains only D-01...D-04 plus mechanically necessary line-context changes;
6. current predecessor bytes are archived byte-identically before routing changes;
7. README and authority manifest are not changed to current `v1.7.0` until independent exact-head review passes;
8. no Roadmap semantic rule is added for this conflict;
9. Foundation Integrity asserts DEC-055 supersession, DEC-313 presence, §21B.3 corrected wording and §21R.6 lifecycle;
10. negative integrity proof rejects current authoritative first-answer consumption wording;
11. exact-head CI and independent semantic review pass before promotion;
12. resulting-main routing/tree is reverified after any eventual merge.

---

# 6. Build disposition

```text
SOURCE AUTHORITY: EXACT LIVE MAIN BLOBS PINNED
TARGET PRODUCT VERSION: v1.7.0
TARGET DECISIONS VERSION: v1.7.0
NEW DEC: DEC-313 ONLY
PRODUCT SEMANTIC SURFACES: §21B.3 + NEW §21R.6 ONLY
DECISION SEMANTIC SURFACES: DEC-055 SUPERSESSION + DEC-313 ONLY
ROADMAP SEMANTIC CHANGE: NONE
NORTH STAR SEMANTIC CHANGE: NONE
ARCHITECTURE CHANGE: NONE
DOMAIN CHANGE: NONE
CURRENT ROUTING CHANGE IN THIS BUILD: NONE
LIVE OPS-UPD-004 / OPS-GAP-010: CONFLICT_STOP REMAINS UNTIL MATERIALISED SUCCESSORS ARE APPROVED AND ROUTED CURRENT
IMPLEMENTATION: NOT AUTHORISED
STATUS: DETERMINISTIC AUTHORITY-SUCCESSOR BUILD CONTRACT READY FOR INDEPENDENT REVIEW
```
