# NewYou OPS-UPD-004 — Assessment-Credit Authority Promotion Candidate Working v0.2.0

> **WORKING / NON-AUTHORITATIVE**  
> **PRODUCT / DECISION AMENDMENT CANDIDATE — NOT CURRENT LAW**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.2.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch before this successor:** `b22edeb06ce409acbdf518e6686a772b8a058bf1`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPS_UPD_004_AUTHORITY_PROMOTION_CANDIDATE_WORKING_v0.1.0.md`
- **Source delta / gap:** `OPS-UPD-004` / `OPS-GAP-010`
- **Source discovery:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.11.0.md`, `OPS-PT-163...174`
- **Purpose:** correct the v0.1.0 candidate after independent authority review and define the smallest coherent Product/Decision repair for formal successor materialisation.
- **Non-goals:** no methodology/scoring/tie/mask change; no retake-interval change; no Domain/Architecture change; no Resource/schema/action design; no provider/channel selection; no current-authority routing change; no PR.

---

# 1. Why v0.2.0 exists

Independent review found four defects or omissions in v0.1.0 that must be corrected before promotion:

1. **Wrong decision reference:** v0.1.0 incorrectly described `DEC-057` as the annual retake rule. The actual retake interval is `DEC-034`; `DEC-057` is launch scoring.
2. **Blurred ownership wording:** v0.1.0 described successful delivery as occurring through a path "under current Identity and Entitlement authority". The corrected rule preserves ownership explicitly: Temperament owns attempt/result/report truth; Entitlements owns credit/right truth; Identity & Access governs access assurance.
3. **Incomplete conflict removal footprint:** adding §21R.6 alone is insufficient because current Product §21B.3 still says the entitlement is consumed/marked used at first-answer start. A formal Product successor must replace those conflicting §21B.3 bullets as well as add §21R.6.
4. **Roadmap over-versioning:** current FP-003 already says the included credit remains unused until successful digital assessment delivery. No new Roadmap semantic rule is needed. Any later Roadmap change should be routing/reference hygiene only unless independent review finds a real semantic mismatch.

v0.1.0 remains historical reasoning evidence; it is not silently rewritten.

---

# 2. Exact live contradiction

Current governed authority still says both:

```text
DEC-055 / Product §21B.3:
first answer / attempt begins
→ consume / mark used
```

and:

```text
Product §21R.4 + FP-003:
successful digital assessment delivery
→ consume
```

No explicit current supersession exists. Therefore:

```text
OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
```

The repair must be explicit at Product/Decision authority. JIT, operators and implementation may not choose between the current texts.

---

# 3. Approved candidate semantic model

The corrected candidate keeps independent lifecycle dimensions:

```text
Temperament attempt/result/report truth
≠
Entitlements credit availability/claim/closure/consumption truth
≠
refundability
≠
notification/open telemetry
```

Candidate lifecycle:

```text
valid ordinary paid credit
+ no first answer
→ available_unused

first answer saved
→ same credit claimed/held
→ held_unconsumed

successful digital assessment delivery
→ consume_exactly_once
```

Terminal branches:

```text
attempt expires before first answer
→ attempt ends
→ credit available_unused

attempt expires after first answer
+ no successful delivery
+ nontechnical / no live governed technical-recovery case
→ attempt ends
→ credit close_unconsumed

genuine technical failure
→ preserve same paid obligation for controlled recovery
   OR valid technical-failure refund closes affected right
```

The semantic labels above are Product concepts, not mandated database enums, Ash Resources or action names.

---

# 4. Explicit new Product choice

The branch:

```text
post-first-answer nontechnical expiry
→ close_unconsumed
```

is a deliberate Product/customer-right choice. It is **not** implied by `DEC-056` alone.

Material consequence:

- the participant saved at least one answer;
- she did not receive successful digital assessment delivery;
- ordinary refundability has already ended under `DEC-045` unless genuine technical failure applies;
- if she voluntarily abandons the attempt until its governed expiry, the credit ceases to be an active unused right without being recorded as consumed or delivered.

This candidate makes no legal-sufficiency finding. Formal Product review must accept this consequence explicitly. The user's approval to continue authorises this candidate build/review stream; it does not replace any required legal/expert review if later authority identifies one.

---

# 5. Corrected proposed DEC-313

## Proposed `DEC-313 — Assessment-credit claim, closure and consumption`

> **CANDIDATE STATUS:** proposed `LOCKED` decision for a future formal Decision Register successor. It is not current law until that successor is approved and routed as current.

**Proposed normative text:**

An ordinary paid digital-assessment credit is **not consumed** when an assessment attempt is admitted or when the first answer is saved. Saving the first answer **claims/holds the existing credit** for the active or recoverable attempt. A claimed credit remains commercially unconsumed but is unavailable for another ordinary assessment purchase or independent attempt.

Successful digital assessment delivery occurs when the participant's **immutable governed digital result** and the **paid digital report permitted by current Product Law** have both been durably made available to the authorised participant through an approved participant-access path. **Temperament owns attempt, result and report truth; Entitlements owns the assessment-credit/right state; Identity & Access governs access assurance.** Participant open/read/view behaviour is not required. Notification-provider acceptance, notification delivery, result creation alone and report generation alone do not independently establish this consumption event.

The ordinary paid assessment credit is consumed **exactly once** at successful digital assessment delivery.

If an attempt expires under `DEC-056` **before the first answer has been saved**, the attempt ends and the credit remains available and unused. If an attempt expires after the first answer has been saved **without successful delivery** and the case is not still governed as a genuine technical-failure recovery, the attempt ends and the credit **closes unconsumed**. Closure is neither successful delivery nor consumption; ordinary refundability remains governed separately by `DEC-045`.

A genuine technical failure resolves through controlled recovery of the **same paid obligation and existing result/report lineage where one exists**, or through the existing technical-failure refund path. Recovery must not mint a duplicate credit, immutable result, report or consumption. A valid technical-failure refund closes the affected credit/right and is not recorded as delivery or consumption.

Duplicate or retried submission, result/report recovery, delivery processing and consumption signals must converge on one logical paid credit/result/report lineage and may consume at most once.

This decision **supersedes `DEC-055`** for assessment-credit claim, closure and consumption semantics. The historical DEC-055 wording remains preserved in the predecessor register. `DEC-034`, `DEC-045`, `DEC-054`, `DEC-056`, `DEC-057`, `DEC-061`, `DEC-066`, `DEC-067` and `DEC-303` otherwise remain unchanged.

---

# 6. Corrected Product Law successor footprint

A formal Product successor must make **both** changes below. Doing only one would leave a same-document contradiction.

## 6.1 Replace conflicting §21B.3 bullets

Current conflicting bullets:

```text
- The entitlement is not consumed until the first answer is saved.
- Once the first answer is saved, the entitlement is marked used.
```

Candidate replacement:

```text
- Saving the first answer claims/holds the existing ordinary paid assessment credit for that active or recoverable attempt; it does not consume the credit.
- Assessment-credit availability, closure and consumption follow §21R.6 and DEC-313.
```

All other §21B.3 attempt rules remain unchanged.

## 6.2 Add §21R.6

### Proposed §21R.6 — Assessment-credit claim, delivery, closure and consumption

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

Normative clarifications:

1. First-answer claim/hold is not consumption.
2. Successful delivery is durable participant availability of the governed result **and** paid report, not result production alone, report generation alone, notification/provider telemetry or participant open/read/view telemetry.
3. Temperament owns attempt/result/report truth; Entitlements owns current assessment-credit/right truth; Identity & Access governs access assurance; Communications/provider state is non-authoritative evidence for this commercial boundary.
4. Closure is not consumption. Post-first-answer nontechnical expiry may close an unconsumed credit without fabricating successful delivery.
5. `DEC-045` refundability remains separate from credit consumption/closure.
6. `DEC-034` retake interval remains separate and unchanged. This amendment does not redefine its clock or eligibility semantics.
7. The assessment-completion **metric** remains separate from commercial consumption: a metric may classify completion under its governed result-production contract without becoming Entitlements authority.
8. Duplicate/retried submission, recovery, report availability, delivery processing or consumption signals converge on one logical credit/result/report lineage and may not create duplicate rights or consumption.
9. Physical representation, exact state names, transactions, locks, Resources and actions remain downstream JIT/implementation choices.

---

# 7. Decision Register supersession treatment

A formal Decision Register successor must not rewrite the historical rule as though it never existed.

Candidate current-entry treatment:

```text
## DEC-055 — Entitlement consumption
**Status:** SUPERSEDED BY DEC-313
Historical DEC-055 wording: “Do not consume the entitlement until the first answer is saved. Mark it used once the attempt begins.”
Current assessment-credit claim, closure and consumption semantics follow DEC-313 and Product Law §21R.6.
```

`DEC-313` is then appended after `DEC-312` as the new locked decision.

---

# 8. Roadmap disposition

No semantic Roadmap successor is required for `OPS-UPD-004` because current FP-003 already requires:

```text
included credit remains unused until successful digital assessment delivery
```

That statement is compatible with the corrected Product/Decision rule.

When the new Product/Decision versions are eventually promoted, Roadmap metadata/current-authority references may require a **routing/reference PATCH** so it does not continue naming superseded Product/Decision versions. Such a patch must not restate or enlarge the Product rule unless an actual Roadmap contradiction is found.

---

# 9. Validation against OPS-PT-163...174

| PT | Corrected candidate answer |
|---|---|
| `OPS-PT-163` | first answer claims/holds; no consumption; second sale/independent attempt remains blocked |
| `OPS-PT-164` | held while active; nontechnical post-answer expiry closes unconsumed |
| `OPS-PT-165` | genuine technical failure preserves same obligation for controlled recovery or technical-failure refund |
| `OPS-PT-166` | result alone is insufficient; held until paid report also becomes durably participant-available |
| `OPS-PT-167` | in-product qualifying delivery can consume even if notification fails; provider state is non-controlling |
| `OPS-PT-168` | participant open/read is not required; analytics cannot become Entitlements authority |
| `OPS-PT-169` | active claimed credit blocks another ordinary purchase/independent attempt without needing consumption |
| `OPS-PT-170` | pre-answer expiry releases; post-answer nontechnical expiry closes; technical case follows recovery/refund |
| `OPS-PT-171` | recovery continues the same credit/result/report lineage and consumes at most once |
| `OPS-PT-172` | ordinary refund remains unavailable after first answer under DEC-045; credit remains held until delivery, expiry closure or technical remedy |
| `OPS-PT-173` | duplicate submit/delivery/recovery converges on one immutable result/report lineage and one consumption |
| `OPS-PT-174` | operator cannot manually substitute “attempt started” for the governed delivery event |

No new PT, UPD or GAP is required by these corrections.

---

# 10. Corrected formal promotion footprint

| Artifact | Correct next action |
|---|---|
| `00_PLATFORM_v1.6.0.md` | substantive `v1.7.0` successor: header/version scope, §21B.3 replacement, new §21R.6, internal current-version consistency |
| `01_DECISIONS_v1.6.0.md` | substantive `v1.7.0` successor: header/version scope, DEC-055 supersession treatment, append DEC-313 |
| `05_ROADMAP_v1.2.0.md` | no semantic change; routing/reference PATCH only when promotion requires it |
| `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` | no semantic successor; metric remains distinct from consumption |
| `03_ARCHITECTURE_v1.1.1.md` | no amendment justified |
| `04_DOMAIN_MAP_v1.2.0.md` | no amendment justified |
| `02_OPEN_WORK_v1.2.59.md` | status/routing successor only after formal promotion |
| `README.md` | route new current versions only after formal approval/promotion |
| authority manifest | update inventory/hashes/archive predecessors only after formal approval/promotion |

No application code or executable proof belongs in this authority repair.

---

# 11. Current disposition

```text
V0.1.0 CANDIDATE: SUPERSEDED FOR PROMOTION PURPOSES BY THIS CORRECTED V0.2.0
NEW PT: 0
NEW OPS-UPD: 0
NEW OPS-GAP: 0
PROPOSED DEC-313: CORRECTED CANDIDATE
PROPOSED PRODUCT §21R.6: CORRECTED CANDIDATE
PRODUCT §21B.3 REPLACEMENT: REQUIRED
ROADMAP SEMANTIC SUCCESSOR: NOT REQUIRED
ARCHITECTURE AMENDMENT: NOT JUSTIFIED
DOMAIN MAP AMENDMENT: NOT JUSTIFIED
LIVE DEC-055 CONFLICT: STILL CURRENT
OPS-UPD-004 / OPS-GAP-010: CONFLICT_STOP UNTIL FORMAL PROMOTION
IMPLEMENTATION: NOT AUTHORISED
PR: NONE
OUTCOME: CORRECTED PROMOTION CANDIDATE READY FOR DETERMINISTIC AUTHORITY-SUCCESSOR BUILD + INDEPENDENT REVIEW
```
