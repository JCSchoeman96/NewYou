# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.1.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.1.0`
- **Date:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Discovery source through:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.9.0.md`
- **Purpose:** provide one compact working control surface for the current decisions, working locks, pressure-test coverage, upstream deltas, known conflicts and reopen conditions discovered by the Operations / Support / Pilot Pre-JIT stream.
- **Non-goals:** this register does not amend Product Law, Architecture Law, Domain Law, Roadmap, Operating Model or any JIT dossier; it does not replace the deep discovery ledgers; it does not authorise implementation or a PR.

---

# 1. How to use this register

The deep discovery files remain the reasoning/evidence record. This register is the **current working-state projection** over that evidence.

Read order for this stream:

```text
current NewYou authority
→ this working control register for current Pre-JIT state
→ exact discovery ledger version / OPS-PT / OPS-UPD / OPS-GAP when reasoning detail is needed
```

If this register conflicts with current NewYou authority, **current NewYou authority wins**.

If this register conflicts with the exact deep ledger evidence it claims to summarise, stop and correct/version this register; do not silently choose the summary.

---

# 2. Meaning of “working locked”

`WORKING_LOCKED` means:

> Within this Pre-JIT stream, the conclusion is sufficiently supported that later passes must treat it as a constraint and may not casually re-debate or contradict it.

It does **not** mean:

- frozen Product Law;
- a new DEC/ARC/ARQ;
- implementation authority;
- a Domain/JIT contract;
- permission to override later upstream authority.

A `WORKING_LOCKED` conclusion is reopened only when at least one of these is true:

1. live `main` or the authority route changed materially;
2. new authoritative text contradicts/refines it;
3. a later pressure test finds a genuine contradiction/new semantic class;
4. empirical/provider/expert evidence materially falsifies an assumption;
5. an independent reviewer identifies a blocking semantic defect;
6. the user explicitly reopens the decision.

Working statuses used here:

- `WORKING_LOCKED`
- `OPEN_UPSTREAM`
- `CONFLICT_STOP`
- `JIT_DOWNSTREAM`
- `PROOF_DOWNSTREAM`
- `DEFERRED_OUT_OF_SCOPE`

---

# 3. Current discovery lineage and pressure-test coverage

The pressure-test ID space is contiguous through `OPS-PT-150`.

| Discovery version | Pressure tests added | Bounded focus | Current role |
|---|---:|---|---|
| `v0.1.0` | `OPS-PT-001...013` | authority/ownership + normal operator journeys | historical reasoning evidence |
| `v0.2.0` | `OPS-PT-014...027` | correction taxonomy + Commerce / Entitlements | historical reasoning evidence |
| `v0.3.0` | `OPS-PT-028...051` | Assessment + Health / Safety / Plans | historical reasoning evidence |
| `v0.4.0` | `OPS-PT-052...078` | Privacy / Identity + Audit / Evidence + Communications | historical reasoning evidence |
| `v0.5.0` | `OPS-PT-079...111` | operator concurrency + pilot admission/counting + measurement + pause/degradation | historical reasoning evidence |
| `v0.6.0` | `OPS-PT-112...127` | privilege/abuse + second adversarial pass | historical reasoning evidence |
| `v0.7.0` | none | upstream-delta false-positive/convergence audit | confirmed `OPS-UPD-001...007` remain real |
| `v0.8.0` | `OPS-PT-128...139` | operator authority + consequential correction | `OPS-UPD-003` narrowed |
| `v0.9.0` | `OPS-PT-140...150` | pilot admission/cap commitment | `OPS-UPD-001` narrowed |

This table tracks **all current pressure-test IDs by exact source range**. The detailed scenario, variants, disposition and proof route remain in the named discovery version; this register does not duplicate 150 full scenarios because duplication would create a stale second reasoning corpus.

---

# 4. Current upstream-delta register

The current delta set remains exactly `OPS-UPD-001...007`. No later pass has created an eighth delta.

| ID | Current meaning | Classification / state | Current routing |
|---|---|---|---|
| `OPS-UPD-001` | Pilot admission commitment / review-boundary / hard-cap / in-flight / historical-cohort semantics | `OPEN_UPSTREAM` — Product/release policy gap | Product decision/amendment before FP-006 JIT chooses mechanism |
| `OPS-UPD-002` | Duplicate genuine collection / full-excess make-whole / partial attribution clarification | `OPEN_UPSTREAM` — Product gap; existing Paystack working clarification should be reused rather than reworded here | Product promotion + provider proof |
| `OPS-UPD-003` | Consequential FP-006 human command authority matrix | `OPEN_UPSTREAM` but narrowed principally to bounded FP-006 operations policy; escalate Product/clinical/privacy/security only where a command would create new authority | operations policy → JIT/proof; upstream promotion only when authority meaning changes |
| `OPS-UPD-004` | Assessment-credit consumption contradiction (`DEC-055` attempt-begins wording versus successful-delivery consumption rule) | `CONFLICT_STOP` | Product/Decision authority must explicitly amend/supersede; downstream must not repair it |
| `OPS-UPD-005` | Material participant Plan change-of-intent before first fulfilment | `OPEN_UPSTREAM` — Product / Commerce / Entitlements rule; reuse existing HSP working gap rather than parallel wording | Product decision/promotion |
| `OPS-UPD-006` | Valid export followed by Full Deletion | `OPEN_UPSTREAM` — Product / Privacy ordering rule; reuse `PRIV-UPD-001` | Product/Privacy policy promotion |
| `OPS-UPD-007` | Exact start event for General Wellness 14-day choice window | `OPEN_UPSTREAM` — Product/customer-communication rule | Product decision/promotion before JIT/provider convention |

**Working lock:** do not create parallel duplicate upstream deltas for these same semantic questions. Refine the existing ID instead.

---

# 5. Current working-locked doctrine

The following conclusions are `WORKING_LOCKED` for this stream unless a reopen condition in §2 occurs.

| Working conclusion | Status | Primary discovery source |
|---|---|---|
| There is no justified Operations / Support / Administration Domain merely because operators need coordinated work. | `WORKING_LOCKED` | `v0.1.0` ownership doctrine; reinforced throughout |
| Every consequential business mutation goes through the owning Domain; operator UI/work queues are not a second write API. | `WORKING_LOCKED` | `v0.1.0`, `v0.8.0` |
| Work/queue assignment is attention/responsibility, not business authority. | `WORKING_LOCKED` | `v0.1.0`, `v0.5.0`, `v0.8.0` |
| Dashboard, Analytics, cache, provider state, PubSub and UI state do not become business authority. | `WORKING_LOCKED` | `v0.1.0`, `v0.5.0`, `v0.9.0` |
| “Manual correction” means an authorised human invokes an explicit owner-Domain operation under current guards; direct database editing is not normal correction. | `WORKING_LOCKED` | `v0.2.0`, `v0.8.0` |
| Correction and compensation are different: a later true refund/revocation/replacement does not make the earlier legitimate event false. | `WORKING_LOCKED` | `v0.2.0` |
| Unknown/ambiguous consequential outcomes are first-class: reconcile authoritative evidence; do not blindly retry or guess success/failure. | `WORKING_LOCKED` | `v0.2.0`, `v0.5.0`, `v0.9.0` |
| Operator work-state, command-attempt state, source-Domain state, provider-attempt state and participant-communication state are independent dimensions. | `WORKING_LOCKED` | `v0.2.0`, `v0.8.0` |
| Role labels are not blanket permissions. Consequential authority composes current capability/scope/purpose/relationship/assurance plus owner-Domain transition guards. | `WORKING_LOCKED` | `v0.8.0` |
| `request`, `approve`, `execute`, `retry`, `reconcile`, `correct`, `compensate`, `restrict`, `restore`, `override` and `bulk` must not be collapsed into one generic “admin action”. | `WORKING_LOCKED` | `v0.8.0` |
| Stale page state, old approval or previous role membership cannot authorise a current business transition; current actor and source state are revalidated at execution. | `WORKING_LOCKED` | `v0.5.0`, `v0.8.0` |
| Bulk action is convenience over individually lawful commands; every target still passes policy/invariants. | `WORKING_LOCKED` | `v0.6.0`, `v0.8.0` |
| Super Admin is not a universal bypass. Break-glass is exceptional scoped access/elevation and does not manufacture unrelated business authority. | `WORKING_LOCKED` | `v0.6.0`, `v0.8.0` |
| Commerce owns payment/refund/dispute truth; Entitlements owns current access/right truth; Finance cannot directly grant entitlement merely because money appears paid. | `WORKING_LOCKED` | `v0.2.0`, `v0.8.0` |
| Support role alone is not refund/grant/reset/assessment/safety/plan authority. | `WORKING_LOCKED` | `v0.1.0`, `v0.6.0`, `v0.8.0` |
| Paid-demand pilot evidence requires verified actual payment; free/staff/complimentary/sponsored/100%-discount/manual-grant access does not count. | `WORKING_LOCKED` | `v0.5.0`, `v0.7.0`, `v0.9.0` |
| A genuine discounted purchase may count when list price, promotion and amount paid remain distinct. | `WORKING_LOCKED` | `v0.5.0`, `v0.9.0` |
| Pilot progression counts human participants, not orders, payment attempts or collections. Multiple qualifying purchases/duplicate collections for one known participant do not create extra participant headcount. | `WORKING_LOCKED` | `OPS-PT-092`, `OPS-PT-096`, `OPS-PT-149` |
| The first paid pilot has an explicit maximum of 50 participants. | `WORKING_LOCKED` | `DEC-281` rechecked in `v0.9.0` |
| The 10 and 25 boundaries are review/progression points whose exact concurrent closure semantics are still upstream-open; do not silently implement them as identical hard caps to 50. | `WORKING_LOCKED` as a constraint on inference; exact rule `OPEN_UPSTREAM` | `v0.5.0`, `v0.7.0`, `v0.9.0` |
| A provider timeout/ambiguous result is not a known failure and cannot safely release/reuse strict scarce capacity merely by timeout assumption. | `WORKING_LOCKED` | `OPS-PT-089`, `OPS-PT-145` |

---

# 6. Pilot-admission working state after v0.9.0

## 6.1 Locked current facts

- first cohort qualification is already governed;
- paid-demand admission cannot be inferred from checkout start or provider/browser success;
- the first paid pilot maximum is 50;
- participant count and purchase count are separate;
- provider callback order and Analytics/dashboard counts are not admission authority;
- unknown payment outcome requires reconciliation;
- duplicate Account/payment correction may not erase truthful Commerce history.

## 6.2 Still open under `OPS-UPD-001`

Product/release policy must still decide:

1. exact first-10 review closure semantics;
2. exact “toward 25” review closure semantics;
3. whether/how a provisional place is committed before a charge-capable payment flow;
4. the exact paid-admission commitment event;
5. treatment of a valid in-flight claim when admissions pause/close;
6. treatment of late verified success after stage closure;
7. whether later legitimate refund/withdrawal preserves historical pilot membership and consumes the historical place;
8. correction/backfill semantics when an admission was invalid from inception or duplicate-human counting is discovered later.

## 6.3 Recommended shape, not locked authority

`v0.9.0` recommends a two-stage semantic model:

```text
provisional capacity claim
→ payment in flight
→ admitted on Commerce-authoritative verified actual payment
```

with `unknown → reconcile`, and with later refund/withdrawal modelled separately from historical admission.

This is a recommended upstream shape only. It must not be implemented as policy until `OPS-UPD-001` is resolved by the correct authority.

---

# 7. Current explicit STOPs and non-inference rules

1. `OPS-UPD-004` is a current Product-authority contradiction. Assessment-credit consumption must not be chosen downstream.
2. Do not infer a universal Super Admin/business override capability.
3. Do not infer that Finance owns Entitlements or that Support owns any source business truth.
4. Do not infer that 10/25 are hard caps identical to 50.
5. Do not infer that a refunded participant automatically stops counting historically; that remains `OPS-UPD-001`.
6. Do not infer a 14-day General Wellness clock-start event from provider delivery conventions; that remains `OPS-UPD-007`.
7. Do not infer pending-export versus Full-Deletion ordering; reuse `OPS-UPD-006` / `PRIV-UPD-001`.
8. Do not resurrect the old terminal-unfulfillable Plan remedy gap: current Product authority already resolved it.

---

# 8. Known gap tracking

The exact deep ledgers remain the source for the historical `OPS-GAP-*` inventory. This initial control-register version deliberately does **not** transcribe every historical gap title without re-verifying each source record; omission from this compact table does not mean a historical gap is closed.

The currently material gap for the just-completed pass is:

| Gap | Classification | State | Route |
|---|---|---|---|
| `OPS-GAP-025` — Pilot admission/cap lifecycle | `PRODUCT_AUTHORITY_GAP` | OPEN | `OPS-UPD-001` |

Future control-register successors should import additional `OPS-GAP-*` rows only when their exact predecessor wording/state has been rechecked. This avoids turning an incomplete transcription into false authority.

---

# 9. Focused v0.9.0 pressure-test index

| ID | Scenario | Disposition |
|---|---|---|
| `OPS-PT-140` | charge-capable checkout begins before governed capacity commitment | `NEEDS_WORKING_DELTA` |
| `OPS-PT-141` | participant 10/11 overlap at first review point | `NEEDS_WORKING_DELTA` |
| `OPS-PT-142` | participant 25/26 overlap at second review point | `NEEDS_WORKING_DELTA` |
| `OPS-PT-143` | participant 50/51 overlap at hard first-pilot maximum | `NEEDS_WORKING_DELTA` |
| `OPS-PT-144` | known payment failure after provisional place claim | `PASS_WITH_REFINEMENT` |
| `OPS-PT-145` | ambiguous payment while place is claimed | `PASS_WITH_REFINEMENT` |
| `OPS-PT-146` | late verified success after stage closes/pauses | `NEEDS_WORKING_DELTA` |
| `OPS-PT-147` | stage pauses after place claim but before payment verification | `NEEDS_WORKING_DELTA` |
| `OPS-PT-148` | admitted participant later refunded/withdraws | `NEEDS_WORKING_DELTA` |
| `OPS-PT-149` | same participant makes multiple purchases / duplicate collections | `PASS` |
| `OPS-PT-150` | duplicate Accounts later proven same human participant | `NEEDS_WORKING_DELTA` |

Exact reasoning remains in discovery `v0.9.0`.

---

# 10. Pass discipline from here

This register must support the user's required **separate-pass** method rather than become an excuse to reopen everything at once.

For each future semantic pass:

1. reverify live `main` and only the relevant authority;
2. read this register for current working locks;
3. read only the exact predecessor ledger sections/IDs relevant to the pass;
4. pressure-test one bounded semantic area;
5. add only genuinely new `OPS-PT` / `OPS-UPD` / `OPS-GAP` IDs;
6. explicitly mark any working lock that is reaffirmed, refined or reopened;
7. create one discovery-ledger MINOR successor for semantic work;
8. version this control register only when its current-state projection materially changes;
9. stop and report before moving to the next semantic area.

No broad freeze is claimed by this register.

---

# 11. Current overall status

```text
DISCOVERY LEDGER: v0.9.0
PRESSURE TEST COVERAGE: OPS-PT-001...150
CURRENT UPSTREAM DELTAS: OPS-UPD-001...007
CURRENT PRODUCT CONFLICT: OPS-UPD-004
CURRENT FOCUSED GAP: OPS-GAP-025 / OPS-UPD-001
LATEST CONVERGED PASS: pilot admission/cap commitment
INDEPENDENT FINAL REVIEW: still required before broad freeze
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY AMENDMENT: NONE
PR: NONE
```

This control register is now the compact working index for the stream. The detailed ledgers remain the source of reasoning evidence.
