# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.7.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.7.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Working branch predecessor head:** `452a71f49224e94890cf6a0a3bc59ddcefaf0660`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_CONTROL_REGISTER_WORKING_v0.6.0.md`
- **Discovery source through:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.14.0.md`
- **Purpose:** compact current-state projection over the Operations / Support / Pilot Pre-JIT discovery stream.
- **v0.7.0 bounded change:** records `OPS-PT-199...210` and narrows `OPS-UPD-007` / `OPS-GAP-020`; no new upstream delta or gap class. It separates General Wellness outcome finalisation, internal communication intent, provider evidence, qualifying participant-facing communication, open/read telemetry, one-window idempotency, and no-choice deadline/refund-execution semantics while preserving `OQ-017` and `OQ-036` downstream.
- **Compression note:** unchanged v0.6.0 working locks and detailed focused-state sections remain inherited and authoritative only as working evidence through the predecessor. This successor restates all current upstream/gap routing and the new v0.14.0 locks without duplicating prior deep reasoning.
- **Non-goals:** no Product/Architecture/Domain/Roadmap amendment, no implementation authority, no PR.

---

# 1. Register semantics

`WORKING_LOCKED` means a conclusion is fixed inside this Pre-JIT working stream unless:

1. live authority changes materially;
2. new authoritative text contradicts/refines it;
3. a later pressure test finds a genuine contradiction/new semantic class;
4. empirical/provider/expert evidence falsifies an assumption;
5. independent review identifies a blocking defect; or
6. the user explicitly reopens it.

It does not mean Product Law, a frozen DEC/ARC/ARQ, implementation authority or a JIT contract.

Read order:

```text
current NewYou authority
→ this control register
→ predecessor control register where unchanged inherited locks are needed
→ exact discovery ledger / OPS-PT / OPS-UPD / OPS-GAP for reasoning detail
```

Authority wins over this register. Exact deep-ledger evidence wins over an erroneous summary.

---

# 2. Discovery lineage and pressure-test coverage

The pressure-test ID space is contiguous through `OPS-PT-210`.

| Discovery version | PTs added | Focus |
|---|---:|---|
| `v0.1.0` | `001...013` | authority/ownership + normal operator journeys |
| `v0.2.0` | `014...027` | correction + Commerce / Entitlements |
| `v0.3.0` | `028...051` | Assessment + Health / Safety / Plans |
| `v0.4.0` | `052...078` | Privacy / Identity + Audit + Communications |
| `v0.5.0` | `079...111` | concurrency + pilot admission/measurement/pause/degradation |
| `v0.6.0` | `112...127` | privilege/abuse + adversarial convergence |
| `v0.7.0` | none | false-positive audit of seven upstream deltas |
| `v0.8.0` | `128...139` | operator authority + consequential correction |
| `v0.9.0` | `140...150` | pilot admission/cap commitment |
| `v0.10.0` | `151...162` | duplicate collection / make-whole / partial attribution |
| `v0.11.0` | `163...174` | assessment-credit claim vs consumption conflict |
| `v0.12.0` | `175...186` | pre-first-fulfilment Plan change-of-intent |
| `v0.13.0` | `187...198` | predating participant export across Full Deletion |
| `v0.14.0` | `199...210` | General Wellness single 14-day choice-window qualifying communication start |

Deep discovery remains the full reasoning record; the control register indexes current state.

---

# 3. Current upstream-delta register

The unique current delta set remains exactly `OPS-UPD-001...007`.

| ID | Current meaning | State | Route |
|---|---|---|---|
| `OPS-UPD-001` | pilot admission commitment / review boundaries / maximum / in-flight / historical cohort | `OPEN_UPSTREAM` | Product/release policy before JIT mechanism |
| `OPS-UPD-002` | duplicate genuine collection / full-excess make-whole / no-manufactured partial attribution | `OPEN_UPSTREAM`, focused | Product promotion; provider proof separate |
| `OPS-UPD-003` | minimum FP-006 consequential human command authority matrix | `OPEN_UPSTREAM`, principally operations-policy | ops policy → JIT/proof; escalate only where powers change |
| `OPS-UPD-004` | assessment credit held/claimed vs consumed; `DEC-055` conflicts with later successful-delivery rule | `CONFLICT_STOP` | explicit Product/Decision supersession/refinement required |
| `OPS-UPD-005` | material participant Plan change-of-intent before first fulfilment; stale Request invalidation vs same-right rebinding/new purchase | `OPEN_UPSTREAM`, narrowed | Product / Commerce / Entitlements; reuse `HSP-UPD-008` |
| `OPS-UPD-006` | valid predating export across effective Full Deletion: narrow continuation, successful-handoff boundary, irreversible-execution termination, participant-held copy vs platform-controlled capability | `OPEN_UPSTREAM`, narrowed; Product/Privacy + legal/privacy validation | reuse `PRIV-UPD-001` / `PRIV-WD-001`; `OQ-032` downstream |
| `OPS-UPD-007` | General Wellness single 14-day choice-window start: qualifying participant-facing communication boundary, first-qualifying-channel semantics, non-controlling open/read telemetry, no-reset retries/reminders, deadline vs refund execution | `OPEN_UPSTREAM`, narrowed | Product/customer-communication promotion; `OQ-017` reminder design and `OQ-036` provider/channel policy downstream |

Do not create parallel upstream IDs for the same semantic classes.

---

# 4. Normalized `OPS-GAP-001...025` inventory

`OPS-GAP-*` is a discovery index, not another authority layer.

| Gap | Working title | Classification/current state | Route |
|---|---|---|---|
| `001` | pilot admission/count concurrency boundary | Product gap / OPEN | `OPS-UPD-001` |
| `002` | consequential operator permission/approval matrix | operations-policy gap / CONFIRMED | `OPS-UPD-003` |
| `003` | exact support/work representation | JIT-only / deferred | FP-006 JIT |
| `004` | Paystack one-off empirical proof | provider gap / OPEN | `OQ-004` / FP-002 proof |
| `005` | retention/deletion/restore release gates | expert gate / OPEN | `OQ-009`, `OQ-029...032` |
| `006` | notification provider/channel release policy | provider gap / OPEN | `OQ-036` |
| `007` | duplicate collection make-whole rule | Product gap / OPEN | `OPS-UPD-002` |
| `008` | exact multi-source Entitlement convergence | JIT-only / deferred | Entitlements JIT |
| `009` | partial reversal component attribution | Product gap / OPEN | `OPS-UPD-002` |
| `010` | assessment-credit consumption conflict | Product conflict / STOP | `OPS-UPD-004` |
| `011` | exact clinical eligibility / urgent-support rules | expert gate / OPEN | `OQ-005`, `OQ-008` |
| `012` | in-flight fulfilment across time-scoped entitlement expiry | future-only | later recurring FP |
| `013` | dependency withdrawal → affected Plan consequence | JIT-only by default | Plans/Safety/Content governance |
| `014` | old final-unfulfillable Plan remedy | CLOSED BY LATER AUTHORITY | current Product law |
| `015` | participant Plan change-of-intent before first fulfilment | Product gap / OPEN | `OPS-UPD-005`, `HSP-UPD-008` |
| `016` | export → subsequent Full Deletion ordering | Product/Privacy gap / OPEN | `OPS-UPD-006` |
| `017` | recurring membership + Full Deletion | future-only for FP-006 core | later membership FP |
| `018` | duplicate-account merge/delete concurrency | JIT-only by default | Identity + Privacy JIT |
| `019` | Audit degraded-mode classification for FP-006 commands | JIT-only / OPEN downstream | Audit JIT/proof |
| `020` | General Wellness 14-day clock start | Product/customer-communication gap / OPEN, narrowed | `OPS-UPD-007`; `OQ-017` / `OQ-036` downstream |
| `021` | Communications provider/channel operational policy | provider gate / OPEN | `OQ-036` / `OQ-017` |
| `022` | FP-006 support-interaction measurement unit | JIT-only / OPEN downstream | prospective metric definition |
| `023` | per-product Day-7/30/90 clock anchors | JIT-only / OPEN downstream | prospective metric definition |
| `024` | capability-specific degradation runbooks | Phase-8 proof / deferred | JIT/proof/controlled-live |
| `025` | pilot admission/cap lifecycle | Product gap / OPEN | `OPS-UPD-001` |

The 25 gap records still collapse to seven unique upstream deltas.

---

# 5. Inherited working-lock baseline

All v0.6.0 working locks `1...51` remain unchanged unless a normal reopen condition occurs. They include, in compact form:

- one-owner Domain authority and no Operations/Admin authority by convenience;
- correction vs compensation and unknown-outcome reconciliation;
- current-state revalidation, no universal Super Admin bypass, and no Support/Finance authority leakage;
- pilot paid-demand/headcount/max-50 and unresolved 10/25 boundary semantics;
- duplicate collection make-whole and no manufactured partial attribution;
- assessment attempt/claim/consumption/refundability separation and the unresolved `DEC-055` conflict;
- Plan Request invalidation vs entitlement treatment and pre-first-fulfilment change-of-intent separation;
- export request/generation/delivery-capability/successful-handoff separation across Full Deletion;
- provider/JIT/expert gates remaining downstream rather than becoming Product Law.

For exact inherited wording use v0.6.0; this successor does not silently alter it.

---

# 6. Working locks added by v0.14.0

52. Authoritative `general_wellness_only` outcome finalisation and the 14-day choice-window start are distinct events.
53. Internal communication obligation creation, outbox/job creation or queue insertion is not participant communication.
54. Raw provider acceptance is not automatically the Product-level General Wellness clock-start event.
55. Known failed/bounced communication does not start the choice window.
56. Open/read/view telemetry is not automatically Product authority and must not be required by implementation convention.
57. A qualifying communication must carry the current governed decision and retain-or-refund choice; materially incomplete/wrong communication cannot start the no-response clock.
58. A governed way to record either retain or refund must exist when the communication qualifies.
59. The single 14-day window starts once; later channels, retries and reminders do not reset or extend it.
60. A valid explicit participant choice terminates the no-response window; stale communications cannot reopen it.
61. Reminder failure does not reset the Product clock.
62. No-choice expiry creates the refund/close obligation independently of later provider refund execution/reconciliation timing.
63. `OQ-017` and `OQ-036` remain downstream; reminder/provider/channel mechanics must not be promoted accidentally into Product Law.

---

# 7. Focused state: `OPS-UPD-007` after discovery v0.14.0

## 7.1 Already governed / do not reopen

- `DEC-308` and Product §21T.4: General Wellness does not fulfil the personalised Plan.
- Plan-component entitlement remains `held_unconsumed` while participant chooses.
- Governed choices are retain or refund the original snapshotted plan-component allocation.
- Exactly one 14-day choice window exists.
- Reminders occur within that same window.
- No choice by deadline produces automatic refund and component closeout.
- Explicit retention leaves the entitlement held/unconsumed.
- Safety & Eligibility owns eligibility truth; Commerce owns payment/refund truth; Entitlements owns current right/access truth; Communications owns communication/delivery truth only.
- `OQ-017` and `OQ-036` remain downstream.

## 7.2 Still open

Product/customer-communication authority must define:

1. the exact participant-facing event that means NewYou has communicated the governed decision and choice;
2. whether qualification requires correct decision/choice content plus a governed path to record either choice;
3. the Product-level handoff/delivery class without using intent creation, queue insertion or raw provider acceptance by convenience;
4. first-qualifying-channel semantics for multi-channel delivery;
5. explicit non-control by open/read/view telemetry;
6. that no-choice expiry fixes the refund/close obligation even if provider execution occurs later.

## 7.3 Recommended promotion shape — not authority

> The single 14-day General Wellness retain-or-refund window starts exactly once when the current governed `general_wellness_only` decision and the correct retain-or-refund choice first cross a qualifying participant-facing communication boundary. A communication qualifies only when the decision/choice are correct for that participant, directed through an authorised participant-facing channel or surface, and a governed path exists to record either choice. Internal eligibility finalisation, communication-intent/outbox/job creation, queue insertion, raw provider acceptance, known failed/bounced attempts, and open/read/view telemetry do not by themselves start the Product clock. For multiple channels, the first qualifying communication starts the single window; later channels, retries and reminders do not reset or extend it. Channel-specific evidence satisfying the qualifying handoff boundary is defined downstream under Communications JIT / `OQ-036`; reminder execution remains `OQ-017`. A valid participant choice terminates the window. If no choice is recorded by the deadline, the automatic refund and component-entitlement-close obligation becomes due at that deadline; later provider refund execution/reconciliation does not reopen the choice window.

---

# 8. Focused v0.14.0 pressure-test index

| ID | Scenario | Disposition |
|---|---|---|
| `OPS-PT-199` | General Wellness authoritative; initial communication delayed | `NEEDS_WORKING_DELTA` |
| `OPS-PT-200` | durable communication obligation exists; no dispatch | `PASS_WITH_REFINEMENT` |
| `OPS-PT-201` | provider accepts initial message; final delivery unknown/bounced | `NEEDS_WORKING_DELTA` |
| `OPS-PT-202` | one channel qualifies; second channel later | `NEEDS_WORKING_DELTA` |
| `OPS-PT-203` | delivered notice lacks correct/actionable governed retain-or-refund choice | `NEEDS_WORKING_DELTA` |
| `OPS-PT-204` | qualifying communication; participant never opens/reads | `PASS_WITH_REFINEMENT` |
| `OPS-PT-205` | first attempt fails; later attempt qualifies | `PASS_WITH_REFINEMENT` |
| `OPS-PT-206` | crash/retry replays initial communication after start | `PASS` |
| `OPS-PT-207` | wrong destination/participant/materially wrong governed content | `PASS_WITH_REFINEMENT` |
| `OPS-PT-208` | valid participant choice precedes later duplicate/secondary communication | `PASS` |
| `OPS-PT-209` | reminder fails or occurs near deadline | `PASS` |
| `OPS-PT-210` | no choice at deadline; refund execution delayed/ambiguous | `PASS_WITH_REFINEMENT` |

Exact reasoning is in discovery v0.14.0.

---

# 9. Current STOP / non-inference rules

- `OPS-UPD-004` remains `CONFLICT_STOP`; downstream may not choose the assessment-credit consumption rule.
- Do not infer 10/25 are identical hard caps to 50.
- Do not infer historical pilot membership disappears after refund/withdrawal.
- Do not infer General Wellness clock start from eligibility finalisation, internal intent/queue creation, raw provider acceptance or open/read telemetry.
- Do not infer second channel/retry/reminder creates a second General Wellness window or resets the first.
- Do not let materially incomplete/wrong General Wellness communication start the no-response clock merely because a provider reports delivery.
- Do not infer the exact export successful-handoff event under `OPS-UPD-006`.
- Do not infer a new export may be requested after effective Full Deletion merely because a predating-export exception may be approved.
- Do not resurrect `OPS-GAP-014`.
- Do not turn JIT/proof/provider/expert gaps into Product Law.
- Do not infer provider refund failure erases customer-money obligation.
- Do not infer partial reversal component identity from amount coincidence.
- Do not silently reinterpret `DEC-055`.
- Do not infer `DEC-038` or `DEC-045` answers pre-first-fulfilment Plan replacement-right treatment.
- Do not silently consume/forfeit/expire/strand/convert an unconsumed Plan right to make a new-fee policy balance.
- Do not generalise `DEC-036`.

---

# 10. Pass discipline and next route

Each semantic pass must reverify live authority, pressure-test one bounded area, add only genuine new PT IDs, refine existing UPD/GAP IDs, version the discovery successor, version this register, update the downloadable snapshot, then stop.

After v0.14.0, **all seven current `OPS-UPD-001...007` classes have received at least one dedicated focused semantic pass**.

Therefore further scenario expansion should require new evidence, contradiction or scope change. Do not automatically create `OPS-UPD-008`.

The next recommended step is a **separate convergence/upstream-promotion review** over `OPS-UPD-001...007` to determine:

- which deltas require Product/Decision amendments;
- which require operations policy only;
- which remain JIT/proof/provider/expert gates;
- the smallest safe amendment package;
- the correct order for resolving `OPS-UPD-004` `CONFLICT_STOP` relative to the other promotions.

---

# 11. v0.7.0 disposition

```text
SEMANTIC PRESSURE TESTS ADDED: OPS-PT-199...210
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
NORMALIZED GAP INVENTORY: OPS-GAP-001...025 PRESERVED
UNIQUE CURRENT UPSTREAM DELTAS: OPS-UPD-001...007
OPS-UPD-007: CONFIRMED + NARROWED
OPS-GAP-020: OPEN / SAME SEMANTIC CLASS
DEC-308 / PRODUCT §21T.4: REUSED, NOT REWRITTEN
OUTCOME FINALISATION VS WINDOW START: SEPARATED
INTERNAL INTENT / QUEUE / PROVIDER ACCEPTANCE VS QUALIFYING COMMUNICATION: SEPARATED
OPEN/READ TELEMETRY: NON-CONTROLLING BY DEFAULT
MULTI-CHANNEL / RETRY / REMINDER: ONE WINDOW / NO RESET
NO-CHOICE DEADLINE VS REFUND EXECUTION: SEPARATED
OQ-017: PRESERVED AS DOWNSTREAM REMINDER DESIGN
OQ-036: PRESERVED AS DOWNSTREAM PROVIDER/CHANNEL POLICY
ALL SEVEN CURRENT OPS-UPD CLASSES HAVE RECEIVED FOCUSED SEMANTIC PASSES
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED BY EXISTING UPSTREAM DELTAS + REQUIRED REVIEW/PROMOTION
NEXT RECOMMENDED STEP: CONVERGENCE / UPSTREAM-PROMOTION REVIEW
```