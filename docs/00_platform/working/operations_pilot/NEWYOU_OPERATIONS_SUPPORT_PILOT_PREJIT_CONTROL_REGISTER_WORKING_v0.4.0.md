# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.4.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.4.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Working branch predecessor head:** `a310a108c6f5dbd6198ded97a98760cdd2a658b5`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_CONTROL_REGISTER_WORKING_v0.3.0.md`
- **Discovery source through:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.11.0.md`
- **Purpose:** provide one compact working control surface for current decisions, working locks, pressure-test coverage, upstream deltas, exact historical gap classification/state, known conflicts and reopen conditions.
- **v0.4.0 bounded scope:** incorporate the completed `OPS-UPD-004` assessment-credit consumption-conflict pass. This successor adds no new upstream delta or gap class; it records `OPS-PT-163...174`, narrows the conflict to credit claim/availability versus commercial consumption plus successful-delivery/terminal-non-delivery semantics, and preserves the normalized `OPS-GAP-001...025` inventory.
- **Non-goals:** this register does not amend Product Law, Architecture Law, Domain Law, Roadmap, Operating Model or any JIT dossier; it does not replace the deep discovery ledgers; it does not authorise implementation or a PR.

---

# 1. How to use this register

The deep discovery files remain the reasoning/evidence record. This register is the **current working-state projection** over that evidence.

Read order:

```text
current NewYou authority
→ this working control register for current Pre-JIT state
→ exact discovery ledger version / OPS-PT / OPS-UPD / OPS-GAP when reasoning detail is needed
```

If this register conflicts with current NewYou authority, **current NewYou authority wins**.

If this register conflicts with the exact deep ledger evidence it claims to summarise, stop and correct/version this register. Do not silently choose the summary.

---

# 2. Meaning of working locks and register states

`WORKING_LOCKED` means:

> Within this Pre-JIT stream, the conclusion is sufficiently supported that later passes must treat it as a constraint and may not casually re-debate or contradict it.

It does **not** mean frozen Product Law, a new DEC/ARC/ARQ, implementation authority, a Domain/JIT contract, or permission to override later upstream authority.

A working lock reopens only when at least one of these occurs:

1. live `main` or the authority route changes materially;
2. new authoritative text contradicts/refines it;
3. a later pressure test finds a genuine contradiction or new semantic class;
4. empirical/provider/expert evidence materially falsifies an assumption;
5. an independent reviewer identifies a blocking semantic defect;
6. the user explicitly reopens the decision.

Register states:

- `WORKING_LOCKED`
- `OPEN_UPSTREAM`
- `CONFLICT_STOP`
- `JIT_DOWNSTREAM`
- `PROOF_DOWNSTREAM`
- `PROVIDER_OR_EXPERT_GATE`
- `DEFERRED_OUT_OF_SCOPE`
- `CLOSED_BY_LATER_AUTHORITY`

---

# 3. Current discovery lineage and pressure-test coverage

The pressure-test ID space is contiguous through `OPS-PT-174`.

| Discovery version | Pressure tests added | Bounded focus | Current role |
|---|---:|---|---|
| `v0.1.0` | `OPS-PT-001...013` | authority/ownership + normal operator journeys | historical reasoning evidence |
| `v0.2.0` | `OPS-PT-014...027` | correction taxonomy + Commerce / Entitlements | historical reasoning evidence |
| `v0.3.0` | `OPS-PT-028...051` | Assessment + Health / Safety / Plans | historical reasoning evidence |
| `v0.4.0` | `OPS-PT-052...078` | Privacy / Identity + Audit / Evidence + Communications | historical reasoning evidence |
| `v0.5.0` | `OPS-PT-079...111` | operator concurrency + pilot admission/counting + measurement + pause/degradation | historical reasoning evidence |
| `v0.6.0` | `OPS-PT-112...127` | privilege/abuse + second adversarial pass | historical reasoning evidence |
| `v0.7.0` | none | false-positive/convergence audit | confirmed `OPS-UPD-001...007`; did not reopen closed/deferred gap classes |
| `v0.8.0` | `OPS-PT-128...139` | operator authority + consequential correction | narrowed `OPS-UPD-003` |
| `v0.9.0` | `OPS-PT-140...150` | pilot admission/cap commitment | narrowed `OPS-UPD-001` |
| `v0.10.0` | `OPS-PT-151...162` | duplicate genuine collection / make-whole / partial loss attribution | narrowed `OPS-UPD-002` |
| `v0.11.0` | `OPS-PT-163...174` | assessment-credit claim/availability versus consumption conflict | narrowed `OPS-UPD-004`; STOP remains |

The detailed scenario, variants, disposition and proof route remain in the named discovery version. This register does not duplicate 174 full scenarios because duplication would create a stale second reasoning corpus.

---

# 4. Current upstream-delta register

The current delta set remains exactly `OPS-UPD-001...007`.

| ID | Current meaning | Classification / state | Current routing |
|---|---|---|---|
| `OPS-UPD-001` | Pilot admission commitment / review-boundary / hard-cap / in-flight / historical-cohort semantics | `OPEN_UPSTREAM` — Product/release policy gap | Product decision/amendment before FP-006 JIT chooses mechanism |
| `OPS-UPD-002` | Duplicate genuine collection / full-excess make-whole persistence / no-manufactured partial component attribution | `OPEN_UPSTREAM` — Product gap, now focused and ready for governed promotion; reuse existing Paystack working clarification | Product promotion; `OQ-004` provider proof remains separate |
| `OPS-UPD-003` | Consequential FP-006 human command authority matrix | `OPEN_UPSTREAM` but narrowed principally to bounded FP-006 operations policy; escalate only where a command creates/changes Product, clinical, privacy or security authority | operations policy → JIT/proof; upstream promotion only when authority meaning changes |
| `OPS-UPD-004` | Assessment-credit claim/availability versus consumption contradiction (`DEC-055` attempt-begins consumption versus later successful-delivery consumption), including successful-delivery terminal definition and terminal non-delivery/expiry consequence | `CONFLICT_STOP` — narrowed; minimal repair is explicit `DEC-055` supersession/refinement, not downstream interpretation | Product/Decision authority must separate held/claimed-unconsumed from consumed and define the unresolved terminal branches before JIT chooses mechanism |
| `OPS-UPD-005` | Material participant Plan change-of-intent before first fulfilment | `OPEN_UPSTREAM` — Product / Commerce / Entitlements rule; reuse `HSP-UPD-008` | Product decision/promotion |
| `OPS-UPD-006` | Valid export followed by Full Deletion | `OPEN_UPSTREAM` — Product / Privacy ordering rule; reuse `PRIV-UPD-001` | Product/Privacy policy promotion |
| `OPS-UPD-007` | Exact start event for General Wellness 14-day choice window | `OPEN_UPSTREAM` — Product/customer-communication rule | Product decision/promotion before JIT/provider convention |

**Working lock:** do not create parallel duplicate upstream deltas for these same semantic questions. Refine the existing ID.

---

# 5. Exact normalized `OPS-GAP-001...025` inventory

This section is the bounded change introduced by v0.2.0.

Important interpretation:

- `OPS-GAP-*` is a discovery classification/index, not an independent authority layer.
- A gap entry may be upstream, JIT-only, proof-only, empirical/expert, future-only or already closed.
- Multiple `OPS-GAP-*` records may route to the **same** `OPS-UPD-*`; therefore 25 gap records do **not** mean 25 upstream blockers.
- `v0.7.0` re-audited the semantic classes and found no basis to reopen the deliberately closed/deferred classifications.

| Gap | Exact working title | Classification | Current state | Route / controlling relation |
|---|---|---|---|---|
| `OPS-GAP-001` | Pilot admission/count concurrency boundary | `PRODUCT_AUTHORITY_GAP` | OPEN | `OPS-UPD-001` |
| `OPS-GAP-002` | Consequential operator permission/approval matrix | `OPERATIONS_POLICY_GAP` | CONFIRMED | `OPS-UPD-003` |
| `OPS-GAP-003` | Exact support/work representation | `JIT_ONLY` | DEFERRED CORRECTLY | FP-006 JIT only if concrete workflow requires it |
| `OPS-GAP-004` | Paystack one-off operational empirical proof | `PROVIDER_EMPIRICAL_GAP` | OPEN / REUSED EXISTING GATE | existing Paystack empirical plan / `OQ-004` / FP-002 proof |
| `OPS-GAP-005` | Retention/deletion/restore release gates | `EXPERT_GATE` | OPEN / REUSED EXISTING GATES | `OQ-009`, `OQ-029...OQ-032` |
| `OPS-GAP-006` | Notification provider/channel release policy | `PROVIDER_EMPIRICAL_GAP` | OPEN / REUSED EXISTING GATE | `OQ-036` |
| `OPS-GAP-007` | Duplicate collection / make-whole clarification not yet governed | `PRODUCT_AUTHORITY_GAP` | OPEN | `OPS-UPD-002` |
| `OPS-GAP-008` | Exact multi-source Entitlement convergence | `JIT_ONLY` | DEFERRED CORRECTLY | Entitlements JIT unless concrete Product benefit semantics are missing |
| `OPS-GAP-009` | Partial reversal component attribution | `PRODUCT_AUTHORITY_GAP` | OPEN | included in `OPS-UPD-002`; no parallel delta |
| `OPS-GAP-010` | Assessment-credit consumption conflict | `PRODUCT_AUTHORITY_GAP` | OPEN / **CONFLICT / STOP affected seam** | `OPS-UPD-004` |
| `OPS-GAP-011` | Exact clinical eligibility / urgent-support rules | `EXPERT_GATE` | OPEN / REUSED EXISTING GATES | `OQ-005`, `OQ-008` |
| `OPS-GAP-012` | In-flight fulfilment across time-scoped entitlement expiry | `FUTURE_ONLY` | DEFERRED CORRECTLY | later recurring/membership Feature Pack |
| `OPS-GAP-013` | Dependency withdrawal → affected Plan consequence mapping | `JIT_ONLY` | DEFERRED CORRECTLY unless a concrete case exposes a new Product/clinical promise | dependency/reason-specific Content + Plans + Safety JIT/governance |
| `OPS-GAP-014` | Old `HSP-UPD-005` final-unfulfillable remedy | `NOT_A_REAL_GAP` at current baseline | **CLOSED BY LATER GOVERNED AUTHORITY** | current Product Law now governs terminal unfulfillable paid-Plan closeout |
| `OPS-GAP-015` | Material participant change-of-intent before first Plan fulfilment | `PRODUCT_AUTHORITY_GAP` | OPEN | `OPS-UPD-005`; reuse `HSP-UPD-008` |
| `OPS-GAP-016` | Export → subsequent Full Deletion ordering | `PRODUCT_AUTHORITY_GAP` | OPEN | `OPS-UPD-006` / `PRIV-UPD-001` |
| `OPS-GAP-017` | Recurring membership + Full Deletion | `FUTURE_ONLY` for FP-006 core / Product gap for later recurring capability | DEFERRED CORRECTLY | later membership Feature Pack / existing `PRIV-UPD-002` |
| `OPS-GAP-018` | Duplicate-account merge/delete concurrency | `JIT_ONLY` by default | DEFERRED CORRECTLY | Identity + Privacy JIT/proof; Product escalation only if participant rights change |
| `OPS-GAP-019` | Audit degraded-mode classification for FP-006 commands | `JIT_ONLY` | OPEN DOWNSTREAM, NOT AN UPSTREAM GAP | Audit JIT / Final Contract / proof |
| `OPS-GAP-020` | General Wellness 14-day choice-window clock start | `PRODUCT_AUTHORITY_GAP` | OPEN | `OPS-UPD-007` |
| `OPS-GAP-021` | Communications provider/channel operational policy | `PROVIDER_EMPIRICAL_GAP` | OPEN / REUSED EXISTING GATES | `OQ-036` plus `OQ-017` where reminder design applies |
| `OPS-GAP-022` | FP-006 support-interaction measurement unit | `JIT_ONLY` | OPEN DOWNSTREAM | version exact support interaction/episode + handling-time definition before first paid participant; invent no threshold |
| `OPS-GAP-023` | Per-product Day-7/30/90 clock anchors | `JIT_ONLY` | OPEN DOWNSTREAM, NOT PRODUCT GAP | freeze prospective product/pathway anchors under current metric-versioning law |
| `OPS-GAP-024` | Capability-specific degradation runbooks | `PHASE8_PROOF` | DEFERRED CORRECTLY | JIT/proof/controlled-live exercises |
| `OPS-GAP-025` | Pilot admission/cap lifecycle | `PRODUCT_AUTHORITY_GAP` | OPEN | `OPS-UPD-001`, narrowed by discovery `v0.5.0` and `v0.9.0` |

## 5.1 Gap-state normalization

For planning purposes, the 25 gap records collapse into these semantic routes:

**Upstream/Product/operations-policy work represented by existing `OPS-UPD-*`:**
`001`, `002`, `007`, `009`, `010`, `015`, `016`, `020`, `025`, with `002` being operations-policy rather than Product law and several entries sharing one upstream delta.

**JIT/downstream definition rather than upstream policy:**
`003`, `008`, `013`, `018`, `019`, `022`, `023`.

**Proof / empirical / expert gates:**
`004`, `005`, `006`, `011`, `021`, `024`.

**Future-only for the current once-off FP-006 core:**
`012`, `017`.

**Closed at current authority baseline:**
`014`.

This is the key normalization: the ledger carries 25 gap records, but the unique current upstream-delta set remains seven.

---

# 6. Current working-locked doctrine

The following conclusions are `WORKING_LOCKED` unless a reopen condition in §2 occurs.

1. There is no justified Operations / Support / Administration Domain merely because operators need coordinated work.
2. Every consequential business mutation goes through the owning Domain; operator UI/work queues are not a second write API.
3. Work/queue assignment is attention/responsibility, not business authority.
4. Dashboard, Analytics, cache, provider state, PubSub and UI state do not become business authority.
5. “Manual correction” means an authorised human invokes an explicit owner-Domain operation under current guards; direct database editing is not normal correction.
6. Correction and compensation are different: a later true refund/revocation/replacement does not make the earlier legitimate event false.
7. Unknown/ambiguous consequential outcomes are first-class: reconcile authoritative evidence; do not blindly retry or guess success/failure.
8. Operator work-state, command-attempt state, source-Domain state, provider-attempt state and participant-communication state are independent dimensions.
9. Role labels are not blanket permissions. Consequential authority composes current capability/scope/purpose/relationship/assurance plus owner-Domain transition guards.
10. `request`, `approve`, `execute`, `retry`, `reconcile`, `correct`, `compensate`, `restrict`, `restore`, `override` and `bulk` must not collapse into one generic “admin action”.
11. Stale page state, old approval or previous role membership cannot authorise a current business transition; current actor and source state are revalidated at execution.
12. Bulk action is convenience over individually lawful commands; every target still passes policy/invariants.
13. Super Admin is not a universal bypass. Break-glass is exceptional scoped access/elevation and does not manufacture unrelated business authority.
14. Commerce owns payment/refund/dispute truth; Entitlements owns current access/right truth; Finance cannot directly grant entitlement merely because money appears paid.
15. Support role alone is not refund/grant/reset/assessment/safety/plan authority.
16. Paid-demand pilot evidence requires verified actual payment; free/staff/complimentary/sponsored/100%-discount/manual-grant access does not count.
17. A genuine discounted purchase may count when list price, promotion and amount paid remain distinct.
18. Pilot progression counts human participants, not orders, payment attempts or collections. Multiple qualifying purchases/duplicate collections for one known participant do not create extra participant headcount.
19. The first paid pilot has an explicit maximum of 50 participants.
20. The 10 and 25 boundaries are review/progression points whose exact concurrent closure semantics are upstream-open; do not silently implement them as hard caps identical to 50.
21. A provider timeout/ambiguous result is not a known failure and cannot safely release/reuse strict scarce capacity merely by timeout assumption.
22. Replayed/reordered provider evidence for one genuine collection is not a second customer payment.
23. One accepted one-off purchase may produce only one lawful purchase/right consequence even if multiple genuine collections occur.
24. A later correction preserves the truthful history of the original collection(s); correction is not retroactive deletion.
25. Provider refund execution state is distinct from whether NewYou owes the customer money.
26. A provider partial-loss amount does not itself identify a NewYou component/right.
27. Entitlements may permanently alter a component/right for partial financial loss only when governed NewYou commercial evidence deterministically identifies that component/right.
28. Full-reversal semantics already governed by `DEC-300` are not part of `OPS-UPD-002` and must not be reopened in this stream.
29. Assessment attempt state and assessment-credit consumption are independent dimensions; an active/recoverable attempt cannot be represented safely by a single consumed boolean.
30. Credit availability/claim and commercial consumption are independent semantic dimensions; `DEC-303` proves an unused credit may still be unavailable for another sale.
31. Refundability and credit consumption are independent; `DEC-045` may close ordinary refundability after the first answer while later Product/Roadmap text still calls the credit unconsumed until successful delivery.
32. Result creation and successful participant delivery are independent; immutable result existence alone must not silently trigger the disputed consumption consequence.
33. Notification/provider state and participant open/read analytics do not become assessment-entitlement authority by implementation convention.
34. Operators may not resolve `OPS-UPD-004` by manually marking a credit consumed/restored; the upstream rule must be governed first.

---

# 7. Pilot-admission working state after v0.9.0

## 7.1 Locked current facts

- first cohort qualification is already governed;
- paid-demand admission cannot be inferred from checkout start or provider/browser success;
- the first paid pilot maximum is 50;
- participant count and purchase count are separate;
- provider callback order and Analytics/dashboard counts are not admission authority;
- unknown payment outcome requires reconciliation;
- duplicate Account/payment correction may not erase truthful Commerce history.

## 7.2 Still open under `OPS-UPD-001`

Product/release policy must still decide:

1. exact first-10 review closure semantics;
2. exact “toward 25” review closure semantics;
3. whether/how a provisional place is committed before a charge-capable payment flow;
4. the exact paid-admission commitment event;
5. treatment of a valid in-flight claim when admissions pause/close;
6. treatment of late verified success after stage closure;
7. whether later legitimate refund/withdrawal preserves historical pilot membership and consumes the historical place;
8. correction/backfill semantics when an admission was invalid from inception or duplicate-human counting is discovered later.

## 7.3 Recommended shape, not locked authority

`v0.9.0` recommends:

```text
provisional capacity claim
→ payment in flight
→ admitted on Commerce-authoritative verified actual payment
```

with `unknown → reconcile`, and later refund/withdrawal modelled separately from historical admission.

This is a recommended upstream shape only. It must not be implemented as policy until `OPS-UPD-001` is resolved by the correct authority.

---

# 8. Duplicate-collection / make-whole working state after v0.10.0

## 8.1 Already governed

- Commerce owns payment/refund/dispute/reversal truth.
- Entitlements owns current access/right truth.
- Provider callbacks/browser/dashboard state are evidence only.
- Duplicate-payment correction leaves one valid right.
- Commercial history and current access remain distinct.
- Full final reversal and post-delivery full reversal consequences are already governed by `DEC-300`.
- Technical/payment corrections remain separate from dissatisfaction evidence.
- Component refunds use the accepted-order allocation snapshot where a governed Product rule authorises a component refund.
- Unknown consequential outcomes are reconciled rather than blindly retried.

## 8.2 Still open under `OPS-UPD-002`

The smallest safe Product promotion must state that:

1. one accepted one-off order is satisfied only once;
2. additional genuine successful customer collections create no additional right;
3. the **full excess genuinely collected amount remains owed** for make-whole correction;
4. ambiguous/unavailable/failed provider refund execution does **not** extinguish the owed customer-money obligation;
5. the exact remaining owed amount/source remains open until lawfully reconciled or satisfied;
6. the same economic correction cannot be applied twice through competing refund/dispute/other paths;
7. a partial provider financial loss amount does not itself identify a NewYou product component/right;
8. only governed NewYou commercial evidence that deterministically identifies a component may drive a component-level permanent access consequence;
9. amount coincidence, provider aggregate state, callback order, current prices, arbitrary ordering or proportional allocation cannot manufacture component identity;
10. an unattributable partial loss remains Commerce/Finance adjudication work rather than arbitrary Entitlement mutation.

## 8.3 Recommended governed wording

> For one accepted Purchase Intent/order in the current one-off launch path, the purchase may be satisfied only once. Any additional genuine successful customer collection remains truthful financial history but creates no second entitlement, credit, paid period or other right. The full excess amount genuinely collected from the customer remains owed for make-whole correction. Ambiguous, unavailable or failed provider execution does not extinguish that obligation; the exact remaining owed amount/source stays open until lawfully reconciled or satisfied. Financial correction paths must not apply the same economic correction twice. A partial provider dispute/chargeback/final reversal establishes financial loss only; its amount does not by itself identify a NewYou product component/right. Entitlements may permanently alter only a component/right deterministically identified by governed NewYou commercial evidence. Amount coincidence, provider aggregate status, callback ordering, current prices, arbitrary ordering or proportional allocation do not manufacture component identity. An unattributable partial loss remains visible Commerce/Finance adjudication work without arbitrary entitlement mutation. Historical payment, delivery, refund and reversal truth remains preserved.

This wording is a **working promotion candidate**, not current Product Law.

## 8.4 Provider/JIT work remains separate

Even after promotion, `OPS-GAP-004` / `OQ-004` remains open for provider empirical proof. Exact Paystack refund/dispute status behaviour, timeout reconciliation, insufficient-balance handling, rate limits/retries, concrete Commerce Resources/actions and executable restart/idempotency proof remain downstream.

---

# 9. Assessment-credit conflict working state after v0.11.0

## 9.1 Direct authority conflict

Current authority remains contradictory:

```text
DEC-055
first answer / attempt begins
→ consume / mark used

versus

00_PLATFORM_v1.6.0 + FP-003 Roadmap
successful digital assessment delivery
→ consume
```

No explicit supersession of `DEC-055` exists. The seam therefore remains `CONFLICT_STOP`.

## 9.2 Working-locked analytical distinctions

The focused pass established these distinctions as constraints for later work:

- assessment attempt state is not entitlement consumption;
- credit availability/claim is not entitlement consumption;
- ordinary refundability is not entitlement consumption;
- immutable result creation is not automatically successful delivery;
- notification delivery/open tracking is not source entitlement authority;
- operator correction cannot select between conflicting Product rules.

A minimal conceptual shape is therefore:

```text
available + unconsumed
→ first answer / governed attempt claim
→ held-or-claimed + unconsumed
→ successful governed digital assessment delivery
→ consumed exactly once
```

This is a **working recommendation**, not current Product Law.

## 9.3 Still open under `OPS-UPD-004`

Product/Decision authority must explicitly decide:

1. whether the later successful-delivery rule supersedes `DEC-055`'s attempt-begins consumption wording;
2. whether first answer/attempt start only holds/claims the credit and blocks another sale/independent attempt while leaving it unconsumed;
3. the minimum customer-facing event that constitutes `successful digital assessment delivery` for consumption;
4. whether notification failure matters to that delivery event or is merely Communications state;
5. the entitlement consequence of a non-delivered attempt that expires or becomes terminally unrecoverable;
6. how technical-failure recovery/refund resolves the held credit without duplicate right, duplicate result or double consumption.

The first two remove the direct contradiction. The remaining questions prevent the repair from merely moving ambiguity into JIT.

## 9.4 Recommended promotion shape

A candidate governed refinement is:

> An ordinary paid assessment credit remains commercially unconsumed until successful governed digital assessment delivery. Saving the first answer / beginning the governed attempt claims or holds that credit for the active/recoverable attempt and makes it unavailable for another ordinary assessment purchase or independent attempt, but does not itself consume it. Successful governed delivery consumes the credit exactly once. Technical interruption, retry, reconciliation or recovery must not manufacture a second credit, result or consumption. Product authority must define the terminal treatment of a non-delivered expired/unrecoverable attempt and the minimum event that constitutes successful digital delivery; notification/open analytics do not become entitlement authority merely by implementation convention.

This is a promotion candidate only. Concrete Resources/state names/transactions remain JIT.

---

# 10. Current explicit STOPs and non-inference rules

1. `OPS-UPD-004` / `OPS-GAP-010` is a current Product-authority contradiction. Assessment-credit consumption must not be chosen downstream.
2. Do not infer a universal Super Admin/business override capability.
3. Do not infer that Finance owns Entitlements or that Support owns any source business truth.
4. Do not infer that 10/25 are hard caps identical to 50.
5. Do not infer that a refunded participant automatically stops counting historically; that remains `OPS-UPD-001`.
6. Do not infer a 14-day General Wellness clock-start event from provider delivery conventions; that remains `OPS-UPD-007`.
7. Do not infer pending-export versus Full-Deletion ordering; reuse `OPS-UPD-006` / `PRIV-UPD-001`.
8. Do not resurrect `OPS-GAP-014` / old terminal-unfulfillable Plan remedy; current Product authority already resolved it.
9. Do not convert JIT-only, proof-only, empirical or expert gaps into Product Law merely because they appear in the gap register.
10. Do not treat duplicate/replayed provider evidence as proof of a second genuine collection.
11. Do not invent that provider refund failure cancels a customer-money obligation; this remains `OPS-UPD-002` until governed.
12. Do not infer component identity for a partial reversal from amount coincidence, current price, callback order or proportional allocation.
13. Do not reopen full-reversal semantics already governed by `DEC-300` merely because `OPS-UPD-002` covers partial attribution.
14. Do not silently reinterpret `DEC-055` “used” as merely “held”; that distinction requires explicit governed supersession/refinement.
15. Do not move or rewrite `DEC-045` refund boundaries merely to resolve the consumption conflict; refundability and consumption are separate.
16. Do not let email delivery, provider status, or participant-open analytics become the credit-consumption event by implementation convention.
17. Do not treat attempt expiry as automatic consumption or automatic reissue/reuse; terminal non-delivery consequence remains part of `OPS-UPD-004`.

---

# 11. Focused pressure-test indexes

## 11.1 Focused v0.9.0 `OPS-UPD-001` pressure-test index

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

## 11.2 Focused v0.10.0 `OPS-UPD-002` pressure-test index

| ID | Scenario | Disposition |
|---|---|---|
| `OPS-PT-151` | replayed provider evidence for one genuine collection | `PASS` |
| `OPS-PT-152` | two distinct genuine successful collections for one accepted order | `NEEDS_WORKING_DELTA` |
| `OPS-PT-153` | second genuine collection discovered after fulfilment already delivered | `NEEDS_WORKING_DELTA` |
| `OPS-PT-154` | excess correction completes successfully | `PASS_WITH_REFINEMENT` |
| `OPS-PT-155` | refund/correction mutation times out and outcome is ambiguous | `PASS_WITH_REFINEMENT` |
| `OPS-PT-156` | provider cannot execute an owed correction | `NEEDS_WORKING_DELTA` |
| `OPS-PT-157` | refund and another correction channel race for the same excess | `PASS_WITH_REFINEMENT` |
| `OPS-PT-158` | provider says refund processed but source/amount does not match obligation | `PASS` |
| `OPS-PT-159` | partial final reversal amount happens to equal one component allocation | `NEEDS_WORKING_DELTA` |
| `OPS-PT-160` | partial final reversal cannot be mapped to any specific component | `NEEDS_WORKING_DELTA` |
| `OPS-PT-161` | partial final loss is deterministically attributable to a governed component | `PASS_WITH_REFINEMENT` |
| `OPS-PT-162` | full final reversal after delivery | `PASS` |

Exact reasoning remains in discovery `v0.10.0`.

## 11.3 Focused v0.11.0 `OPS-UPD-004` pressure-test index

| ID | Scenario | Disposition |
|---|---|---|
| `OPS-PT-163` | first answer is saved | `CONFLICT` |
| `OPS-PT-164` | participant abandons after answering but before delivery | `CONFLICT / NEEDS_UPSTREAM_REFINEMENT` |
| `OPS-PT-165` | genuine technical failure after first answer, before final result | `CONFLICT` |
| `OPS-PT-166` | immutable result exists but governed report/delivery is incomplete | `CONFLICT_WITH_DOWNSTREAM_REFINEMENT` |
| `OPS-PT-167` | assessment available in-product but notification email fails | `NEEDS_UPSTREAM_REFINEMENT` |
| `OPS-PT-168` | participant never opens otherwise available report | `NEEDS_UPSTREAM_REFINEMENT` |
| `OPS-PT-169` | participant tries to buy another assessment while active attempt holds credit | `PASS` |
| `OPS-PT-170` | active attempt expires after 30 days without successful delivery | `NEEDS_UPSTREAM_REFINEMENT` |
| `OPS-PT-171` | controlled recovery after technical interruption | `PASS_WITH_REFINEMENT` |
| `OPS-PT-172` | ordinary refund requested after first answer but before successful delivery | `PASS_WITH_REFINEMENT` |
| `OPS-PT-173` | duplicate/retried completion races credit consumption | `PASS_WITH_REFINEMENT` |
| `OPS-PT-174` | operator manually marks credit consumed because attempt started | `PASS / NEGATIVE AUTHORITY PROOF` |

Exact reasoning remains in discovery `v0.11.0`.

---

# 12. Pass discipline from here

For each future semantic pass:

1. reverify live `main`, branch head and authority route relevant to the pass;
2. pressure-test exactly one bounded semantic area;
3. add only genuinely new `OPS-PT` IDs;
4. refine an existing `OPS-UPD`/`OPS-GAP` where the semantic class already exists instead of creating duplicates;
5. create exactly one SemVer successor for that semantic pass;
6. update this control register in a successor after the bounded result is known;
7. update the downloadable chat working document from the same normalized state;
8. stop and report what changed, what remains unresolved and whether the bounded area converged.

Register-only normalization/QA passes may version this register without creating a discovery successor, provided they add **no semantic conclusion**.

---

# 13. v0.4.0 focused-pass disposition

```text
SEMANTIC PRESSURE TESTS ADDED: OPS-PT-163...174
CUMULATIVE PRESSURE TESTS: 174
NEW OPS-UPD: 0
NEW OPS-GAP: 0
NORMALIZED GAP INVENTORY: OPS-GAP-001...025 PRESERVED
UNIQUE CURRENT UPSTREAM DELTAS: OPS-UPD-001...007
OPS-UPD-004: CONFLICT CONFIRMED + NARROWED
OPS-GAP-010: OPEN / CONFLICT STOP
DIRECT CONFLICT: DEC-055 ATTEMPT-BEGIN CONSUMPTION VS LATER SUCCESSFUL-DELIVERY CONSUMPTION
MINIMAL SAFE PROMOTION TARGET: EXPLICIT DEC-055 SUPERSESSION/REFINEMENT + CLAIM VS CONSUMPTION SEPARATION
TERMINAL NON-DELIVERY / SUCCESSFUL-DELIVERY EVENT: STILL REQUIRES GOVERNED REFINEMENT
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED BY EXISTING UPSTREAM DELTAS + REQUIRED REVIEW/PROMOTION
```
