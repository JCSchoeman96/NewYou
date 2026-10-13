# NewYou OPS-UPD-004 — Assessment-Credit Authority Promotion Candidate Working v0.1.0

> **WORKING / NON-AUTHORITATIVE**  
> **PRODUCT / DECISION AMENDMENT CANDIDATE — NOT CURRENT LAW**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.1.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch before this candidate:** `129515d9641a6a78967a422c88fb86546707e194`
- **Working branch:** `prejit/operations-support-pilot`
- **Source delta:** `OPS-UPD-004`
- **Source gap:** `OPS-GAP-010`
- **Source discovery:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.11.0.md`, `OPS-PT-163...174`
- **Promotion-planning source:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_UPSTREAM_PROMOTION_REVIEW_WORKING_v0.1.0.md`
- **Purpose:** define the smallest explicit Product/Decision successor that removes the `DEC-055` assessment-credit consumption contradiction without inventing implementation representation or reopening unrelated assessment policy.
- **Non-goals:** no methodology/scoring/tie/mask change; no annual-retake change; no Domain/Architecture change; no Resource/schema/action design; no provider/channel selection; no PR; no current-authority mutation in this artifact.

---

# 1. Authority evidence reverified

Current governed sources still say both of the following:

```text
DEC-055:
Do not consume the entitlement until the first answer is saved.
Mark it used once the attempt begins.
```

and:

```text
Product Law / FP-003:
assessment credit remains unused until successful digital assessment delivery
```

Current surrounding law also establishes:

- `DEC-045`: ordinary assessment refundability ends after the first answer except technical failure;
- `DEC-054`: one active attempt, save/resume and controlled recovery for genuine technical failure;
- `DEC-056`: unfinished attempts expire after 30 days with advance warning;
- `DEC-061`: submitted answers, calculated scores and assessment version are immutable;
- `DEC-066`: preserve the original delivered report;
- `DEC-067`: completed results remain immutable and active short-lived attempts may finish on their original version;
- `DEC-303`: at most one active unused ordinary paid assessment credit; a second sale is blocked while it remains unused;
- Product Law §21R.5: a second standalone purchase is rejected until the existing credit is **used or closed**;
- Product Law §21R.4: a digitally assessed participant receives the exact digital result/report and the included credit is consumed only after successful assessment delivery;
- FP-003: included credit remains unused until successful digital assessment delivery.

The conflict therefore cannot be repaired by redefining `used` in JIT code. It requires explicit Product/Decision supersession.

---

# 2. Promotion decision

This candidate chooses the smallest coherent rule that satisfies the current higher-level Product promise and all `OPS-PT-163...174` cases:

```text
credit available + unused
→ first answer saved
→ credit claimed/held + unconsumed
→ successful governed digital result + paid report availability
→ credit consumed exactly once
```

with distinct terminal branches:

```text
attempt expires before first answer
→ credit remains available + unused

attempt expires after first answer, no successful delivery,
nontechnical / no governed technical-recovery case remains
→ credit closes unconsumed

 genuine technical failure
→ same paid obligation is recovered OR technical-failure refund closes it
```

This deliberately separates:

- attempt state;
- credit availability/claim;
- credit consumption;
- credit closure;
- refundability;
- result creation;
- participant delivery;
- notification/open telemetry.

## 2.1 Explicit Product choice introduced by this candidate

The **post-first-answer nontechnical expiry → `close_unconsumed`** branch is not derivable from `DEC-056` alone. It is a new customer-right/commercial policy choice proposed by this candidate to resolve the otherwise stranded-credit branch while preserving all three existing constraints: successful-delivery-only consumption, ordinary refund closure after the first answer, and the one-active-unused-credit purchase cap.

Its consequence is material: a participant who voluntarily abandons a post-first-answer attempt until it expires receives neither successful assessment delivery nor an ordinary refund and the credit no longer remains an active unused right. Therefore this branch must receive explicit Product approval in the formal authority-successor review; it must not be treated as a mechanical consequence of the existing 30-day attempt expiry. This candidate establishes no legal sufficiency for that policy.

If formal Product review rejects that customer-right choice, the authority build must STOP and choose another explicit terminal rule rather than silently returning the credit to availability or treating expiry as consumption.

---

# 3. Proposed Decision Register addition

## Proposed `DEC-313 — Assessment-credit claim, closure and consumption`

> **CANDIDATE STATUS:** proposed `LOCKED` decision for the formal authority successor. `DEC-313` is not current law until the successor is approved and made current.

**Proposed normative text:**

An ordinary paid digital-assessment credit is **not consumed** when an assessment attempt is admitted or when the first answer is saved. Saving the first answer **claims/holds the existing credit** for the active or recoverable attempt. A claimed credit remains commercially unconsumed but is unavailable for another ordinary assessment purchase or independent attempt.

Successful digital assessment delivery occurs when the participant's **immutable governed digital result** and the **paid digital report permitted by current Product Law** have both been durably made available to that participant through an approved participant-access path under current Identity and Entitlement authority. Participant open/read/view behaviour is not required. Notification-provider acceptance, notification delivery, result creation alone and report generation alone do not independently establish this consumption event.

The ordinary paid assessment credit is consumed **exactly once** at successful digital assessment delivery.

If an attempt expires under `DEC-056` **before the first answer has been saved**, the attempt ends and the credit remains available and unused. If an attempt expires after the first answer has been saved **without successful delivery** and the case is not still governed as a genuine technical-failure recovery, the attempt ends and the credit **closes unconsumed**. That closure is neither successful delivery nor consumption; ordinary refundability remains governed separately by `DEC-045`.

A genuine technical failure must resolve through controlled recovery of the **same paid obligation/result lineage** or through the existing technical-failure refund path. Technical recovery must not mint a duplicate credit, result, report or consumption. A valid technical-failure refund closes the affected credit/right.

Duplicate or retried submission, recovery, report-availability, delivery or consumption signals must converge on the one logical paid credit/result lineage and consume at most once.

This decision **supersedes `DEC-055` only** on the timing and meaning of assessment-credit consumption and the associated terminal credit consequence. It does not rewrite `DEC-055` historical text. `DEC-045`, `DEC-054`, `DEC-056`, `DEC-057`, `DEC-061`, `DEC-066`, `DEC-067`, `DEC-303` and the existing assessment-retake interval remain otherwise unchanged.

---

# 4. Proposed Product Law addition

## Proposed `00_PLATFORM` §21R.6 — Assessment-credit claim, delivery, closure and consumption

The formal Product Law successor should add a compact machine-testable lifecycle immediately after current §21R.5.

| Assessment-credit situation | Product consequence |
|---|---|
| valid ordinary paid credit; no first answer saved | `available_unused` |
| first answer saved; attempt active/recoverable; no successful delivery | `held_unconsumed` |
| immutable result exists but paid report is not yet durably participant-available | `held_unconsumed` |
| governed immutable result **and** paid report durably available through approved participant-access path | `consume_exactly_once` |
| attempt expires before first answer | `release_to_available_unused` |
| attempt expires after first answer without successful delivery and no live genuine technical-recovery case | `close_unconsumed` |
| genuine technical failure under controlled recovery | `preserve_same_credit_obligation; no_duplicate_credit_or_result` |
| valid technical-failure refund | `close_credit_after_refund; do_not_consume_as_delivery` |
| notification/provider attempt fails after in-product delivery already qualifies | `no_change_to_consumption_truth` |
| participant never opens/views an otherwise qualifying delivered result/report | `no_change_to_consumption_truth` |

Normative clarifications:

1. **Availability/claim is not consumption.** A first answer can make a credit unavailable for another sale/attempt without consuming it.
2. **Delivery is product availability, not telemetry.** The qualifying event is durable availability of the governed result + paid report to the authorised participant, not email/provider acceptance and not open/read analytics.
3. **Closure is not consumption.** A post-answer nontechnical expired attempt may close an unconsumed credit without fabricating successful delivery.
4. **Refundability remains separate.** `DEC-045` continues to govern ordinary versus technical-failure refunds.
5. **Source ownership remains unchanged.** Temperament owns attempt/result/report truth; Entitlements owns current credit/right truth; Communications/provider state remains evidence only.
6. **Representation remains JIT.** The lifecycle labels above are semantic values, not mandated database enums, tables or Ash Resources.

---

# 5. Proposed Roadmap synchronization

The formal Roadmap successor should refine **FP-003 only**. It should not legislate new Product policy independently.

Recommended FP-003 exit-condition synchronization:

- first saved answer claims/holds the existing ordinary paid credit without consuming it;
- a held credit blocks a second ordinary assessment purchase/independent attempt under current Product Law;
- successful digital assessment delivery requires one immutable governed result plus its paid report to be durably participant-available through the approved access path;
- result creation alone, report generation alone, notification delivery and open/read telemetry do not consume the credit;
- pre-first-answer expiry returns the credit to available unused;
- post-first-answer nontechnical expiry closes the credit unconsumed;
- genuine technical failure recovers the same obligation/result lineage or uses the technical-failure refund path;
- duplicate/retried completion and delivery consume at most once.

No Roadmap change to assessment methodology, annual retake interval, score semantics or Domain ownership is justified.

---

# 6. Existing decisions explicitly preserved

| Existing authority | Candidate effect |
|---|---|
| `DEC-045` refund boundaries | preserved; refundability remains separate from consumption |
| `DEC-054` one active attempt / technical recovery | preserved and composed with same-credit recovery |
| `DEC-055` historical wording | preserved historically but explicitly superseded on consumption timing/consequence |
| `DEC-056` 30-day attempt expiry | preserved; this candidate supplies the associated credit consequence |
| `DEC-057` annual retake limit | preserved; no interval change |
| `DEC-061` immutable raw result | preserved |
| `DEC-066` historical delivered report | preserved |
| `DEC-067` version immutability | preserved |
| `DEC-303` unused-credit purchase limits | preserved; `held_unconsumed` remains unavailable and `closed_unconsumed` is no longer active unused credit |

No new Domain is created and no current owner changes.

---

# 7. Validation against `OPS-PT-163...174`

| PT | Candidate result |
|---|---|
| `OPS-PT-163` first answer saved | claim/hold credit; do not consume; second sale remains blocked |
| `OPS-PT-164` abandon after answers before delivery | remain held while active; at nontechnical expiry close unconsumed |
| `OPS-PT-165` genuine technical failure before final result | preserve same obligation for controlled recovery or technical-failure refund; no duplicate credit |
| `OPS-PT-166` immutable result exists but report/delivery incomplete | result retained; credit remains held/unconsumed until result + paid report qualify as delivered |
| `OPS-PT-167` in-product assessment available but notification fails | delivery/consumption remains valid; notification does not control credit truth |
| `OPS-PT-168` participant never opens otherwise qualifying report | consumption remains valid; open/read telemetry is non-authoritative |
| `OPS-PT-169` second purchase while attempt holds credit | reject under current unused-credit cap; claim and consumption remain distinct |
| `OPS-PT-170` active attempt expires after 30 days without delivery | pre-answer expiry releases unused; post-answer nontechnical expiry closes unconsumed; technical failure follows recovery/refund branch |
| `OPS-PT-171` controlled recovery after interruption | same credit/result lineage; consume at most once on eventual qualifying delivery |
| `OPS-PT-172` ordinary refund requested after first answer before delivery | ordinary refund remains unavailable under `DEC-045`; credit remains held until delivery, expiry closure or genuine technical-failure remedy |
| `OPS-PT-173` duplicate submit/delivery/recovery | one result/right; consumption exactly once |
| `OPS-PT-174` operator manually marks consumed | prohibited; operator cannot substitute for the governed delivery event |

**Result:** all twelve focused cases have a deterministic Product-level answer under this candidate without requiring implementation representation.

---

# 8. Proposed authority-successor footprint

This candidate recommends the following **formal promotion package** in the next execution/review pass:

| Authority/artifact | Proposed successor/action | Reason |
|---|---|---|
| `01_DECISIONS_v1.6.0.md` | `v1.7.0` candidate; append `DEC-313` | explicit supersession/refinement of `DEC-055` |
| `00_PLATFORM_v1.6.0.md` | `v1.7.0` candidate; add §21R.6 | make Product lifecycle machine-readable and participant promise explicit |
| `05_ROADMAP_v1.2.0.md` | `v1.3.0` candidate; synchronize FP-003 exit condition only | keep Roadmap acceptance aligned with Product Law |
| `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` | no semantic successor expected | current participant journey is compatible |
| `03_ARCHITECTURE_v1.1.1.md` | no amendment expected | current durable/current-authority/idempotency doctrine is sufficient |
| `04_DOMAIN_MAP_v1.2.0.md` | no amendment expected | owner split already sufficient |
| `02_OPEN_WORK_v1.2.59.md` | patch successor after candidate approval/current-status promotion | route status and record conflict closure |
| `README.md` | route to new current authority only when promoted | routing only |
| `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` | update paths/versions/hashes and archive predecessors | inventory integrity; not new authority |
| current predecessor authority files | archive byte-identically | preserve history / explicit supersession |

The proposed SemVer changes are semantic candidates, not current repository state.

---

# 9. Required integrity and review proof for the formal promotion

Before the candidate may become current authority, the promotion should prove at minimum:

1. current `DEC-055` bytes are preserved in the archived predecessor;
2. `DEC-313` explicitly says it supersedes `DEC-055` **only** for assessment-credit consumption timing/consequence;
3. Product §21R.6 and `DEC-313` agree on first-answer claim, qualifying delivery, expiry closure and technical-failure branches;
4. FP-003 repeats the Product rule rather than inventing a competing one;
5. no North Star, Architecture or Domain ownership semantics change accidentally;
6. Foundation Integrity tests assert the new rule and still assert the existing Product matrices/ownership;
7. a negative test prevents reintroduction of attempt-start consumption as current authoritative semantics without an explicit later supersession;
8. README/manifest route only one current Platform/Decision/Roadmap successor each;
9. predecessor hashes/archive routing are correct;
10. exact-head CI passes on the candidate;
11. fresh independent semantic review passes the exact candidate head;
12. after merge, resulting-main tree/current-routing and Foundation Integrity are reverified before current-status certification is claimed.

No application code, Ash Resource, database migration or provider integration belongs in this authority-promotion package.

---

# 10. Current state after this candidate

This working artifact does **not** remove the live conflict.

Until a formal Product/Decision successor is approved and made current:

```text
OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
DEC-055 current wording = still current
Product/Roadmap successful-delivery wording = still current
implementation = NOT AUTHORISED to choose between them
```

What changes in this working stream is readiness:

```text
PROMOTION CANDIDATE = READY FOR FORMAL AUTHORITY-SUCCESSOR BUILD / INDEPENDENT REVIEW
NEW PRESSURE TESTS = NONE
NEW OPS-UPD = NONE
NEW OPS-GAP = NONE
NEW DOMAIN = NONE
ARCHITECTURE AMENDMENT = NOT JUSTIFIED
DOMAIN MAP AMENDMENT = NOT JUSTIFIED
PR = NONE
```

**Pass outcome:** `PASS / OPS-UPD-004 AUTHORITY-PROMOTION CANDIDATE CONVERGED`.
