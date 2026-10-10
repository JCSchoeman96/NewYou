# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.5.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.5.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Working branch predecessor head:** `2603076a0a7f68222f758416ddf1cc456ee7869e`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_CONTROL_REGISTER_WORKING_v0.4.0.md`
- **Discovery source through:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.12.0.md`
- **Purpose:** compact current-state projection over the append-only Operations / Support / Pilot Pre-JIT discovery ledger.
- **v0.5.0 bounded change:** records `OPS-PT-175...186` and narrows `OPS-UPD-005` / `OPS-GAP-015`; no new upstream delta or gap class.
- **Non-goals:** no Product/Architecture/Domain/Roadmap amendment, no implementation authority, no PR.

---

# 1. Register semantics

`WORKING_LOCKED` means a conclusion is fixed **inside this Pre-JIT working stream** unless:
1. live authority changes materially;
2. new authoritative text contradicts/refines it;
3. a later pressure test finds a genuine contradiction/new semantic class;
4. empirical/provider/expert evidence falsifies an assumption;
5. independent review identifies a blocking defect; or
6. the user explicitly reopens it.

It does not mean frozen Product Law or implementation authority.

Current register states:

- `WORKING_LOCKED`
- `OPEN_UPSTREAM`
- `CONFLICT_STOP`
- `JIT_DOWNSTREAM`
- `PROOF_DOWNSTREAM`
- `PROVIDER_OR_EXPERT_GATE`
- `DEFERRED_OUT_OF_SCOPE`
- `CLOSED_BY_LATER_AUTHORITY`

Read order:

```text
current NewYou authority
→ this control register
→ exact discovery ledger / OPS-PT / OPS-UPD / OPS-GAP for reasoning detail
```

Authority wins over this register. Deep ledger evidence wins over an erroneous summary.

---

# 2. Discovery lineage and pressure-test coverage

The pressure-test ID space is contiguous through `OPS-PT-186`.

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

The deep discovery versions remain the full scenario/reasoning record. This register indexes current state rather than duplicating all 186 scenarios.

---

# 3. Current upstream-delta register

The unique current delta set remains exactly `OPS-UPD-001...007`.

| ID | Current meaning | State | Route |
|---|---|---|---|
| `OPS-UPD-001` | pilot admission commitment / review boundaries / maximum / in-flight / historical cohort | `OPEN_UPSTREAM` | Product/release policy before JIT mechanism |
| `OPS-UPD-002` | duplicate genuine collection / full-excess make-whole / no-manufactured partial attribution | `OPEN_UPSTREAM`, focused | Product promotion; provider proof separate |
| `OPS-UPD-003` | minimum FP-006 consequential human command authority matrix | `OPEN_UPSTREAM`, principally operations-policy | ops policy → JIT/proof; Product/clinical/privacy/security only where powers change |
| `OPS-UPD-004` | assessment credit held/claimed vs consumed; `DEC-055` conflict with later successful-delivery rule | `CONFLICT_STOP` | explicit Product/Decision supersession/refinement required |
| `OPS-UPD-005` | material participant Plan change-of-intent before first fulfilment; stale Request invalidation vs same-right rebinding/new purchase | `OPEN_UPSTREAM`, narrowed | Product / Commerce / Entitlements; reuse `HSP-UPD-008` |
| `OPS-UPD-006` | valid export followed by Full Deletion | `OPEN_UPSTREAM` | Product/Privacy; reuse `PRIV-UPD-001` |
| `OPS-UPD-007` | General Wellness 14-day choice-window clock-start event | `OPEN_UPSTREAM` | Product/customer-communication decision |

Do not create duplicate upstream IDs for the same semantic questions.

---

# 4. Normalized `OPS-GAP-001...025` inventory

`OPS-GAP-*` is a discovery index, not another authority layer. A gap may be upstream, JIT-only, proof/provider/expert, future-only, or closed.

| Gap | Working title | Classification / current state | Route |
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
| `020` | General Wellness 14-day clock start | Product gap / OPEN | `OPS-UPD-007` |
| `021` | Communications provider/channel operational policy | provider gate / OPEN | `OQ-036` / `OQ-017` |
| `022` | FP-006 support-interaction measurement unit | JIT-only / OPEN downstream | prospective metric definition |
| `023` | per-product Day-7/30/90 clock anchors | JIT-only / OPEN downstream | prospective metric definition |
| `024` | capability-specific degradation runbooks | Phase-8 proof / deferred | JIT/proof/controlled-live |
| `025` | pilot admission/cap lifecycle | Product gap / OPEN | `OPS-UPD-001` |

The 25 gap records still collapse to seven unique upstream deltas.

---

# 5. Current working-locked doctrine

The following are locked for this working stream unless a reopen condition in §1 occurs.

1. No Operations / Support / Administration Domain is justified merely by coordinated operator work.
2. Consequential business mutation goes through the owning Domain; operator UI/work queues are not a second write API.
3. Queue/work assignment is attention/responsibility, not business authority.
4. Dashboard, Analytics, cache, provider state, PubSub and UI state are not business authority.
5. Manual correction means an authorised human invokes an owner-Domain operation under current guards; direct DB editing is not normal correction.
6. Correction and compensation are different; later true refund/revocation/replacement does not make an earlier legitimate event false.
7. Unknown consequential outcomes reconcile authoritative evidence; do not blindly retry or guess.
8. Work state, command-attempt state, source-Domain state, provider state and participant-communication state remain separate.
9. Role labels are not blanket permissions; current scoped authority and source guards are checked at execution.
10. `request`, `approve`, `execute`, `retry`, `reconcile`, `correct`, `compensate`, `restrict`, `restore`, `override`, `bulk` are distinct.
11. Stale UI/approval/role state cannot authorize a current transition.
12. Bulk convenience preserves per-target policy/invariants.
13. Super Admin is not a universal bypass; break-glass is scoped exceptional access, not unrelated business authority.
14. Commerce owns money truth; Entitlements owns current right/access truth.
15. Support role alone is not refund/grant/reset/assessment/safety/Plan authority.
16. Paid-demand pilot evidence requires verified actual payment; free/staff/complimentary/sponsored/100%-discount/manual-grant access does not count.
17. Genuine discounted positive payment may count when list/promotion/amount paid remain distinct.
18. Pilot progression counts human participants, not orders/attempts/collections.
19. First paid pilot maximum is 50.
20. 10 and 25 are review/progression points; exact concurrent closure semantics remain upstream-open.
21. Ambiguous payment outcome is not known failure and cannot release scarce capacity by timeout assumption.
22. Replayed provider evidence for one collection is not another payment.
23. One accepted one-off purchase yields one lawful purchase/right consequence even with duplicate genuine collections.
24. Provider refund execution state is distinct from whether money is owed.
25. Partial provider loss amount does not itself identify a NewYou component/right.
26. Full-reversal semantics already governed by `DEC-300` are not reopened by `OPS-UPD-002`.
27. Assessment attempt state, credit claim/availability and credit consumption are distinct.
28. Refundability and assessment-credit consumption are distinct.
29. Immutable assessment result existence alone is not successful participant delivery.
30. Notification/open analytics do not become entitlement authority by convention.
31. Operators cannot resolve `OPS-UPD-004` by manually selecting consumed/restored.
32. Participant-owned material Plan-input change applying to the current in-flight Request cannot silently mutate immutable Plan history; stale work cannot become first fulfilment merely because it completes later.
33. Plan Request invalidation/supersession and Plan entitlement treatment are distinct dimensions.
34. Under `DEC-299`, generation start/completion does not itself consume the paid Plan right; successful governed delivery remains the current consumption boundary.
35. `DEC-045` refundability does not automatically answer pre-first-fulfilment replacement-right treatment.
36. `DEC-038` must not be silently projected backward to decide the pre-first-fulfilment gap.
37. `DEC-036` is a narrow explicit complimentary-regeneration exception, not a general free regeneration right.
38. Future-only/unrelated or immaterial edits do not automatically invalidate current Plan work.
39. Safety-relevant new information routes through Health/Safety authority rather than ordinary change-of-intent policy.
40. Technical sunk cost, operator convenience or stale delivery cannot manufacture the commercial answer to `OPS-UPD-005`.

---

# 6. Focused state: `OPS-UPD-005` after discovery v0.12.0

## 6.1 Already governed / do not reopen

- `DEC-299`: successful governed Plan delivery is the Plan-entitlement consumption boundary; technical generation failure preserves the right.
- `DEC-107`: generation/adjustment produces immutable reproducible linked Plan history.
- `DEC-045`: ordinary Plan refund boundary is generation.
- `DEC-038`: ordinary post-fulfilment preference/progress re-personalisation requires a new purchase or qualifying membership/add-on.
- `DEC-036`: one narrow complimentary regeneration is allowed for the materially different included digital-assessment-result case.
- safety-relevant changes remain a Health/Safety path, not an ordinary preference shortcut.
- working HSP evidence supports explicit current-Request applicability and stale-basis invalidation without rewriting history.

## 6.2 Still open

Product / Commerce / Entitlements must decide:

1. whether the same still-unconsumed Plan right may authorize a replacement Request after a material participant current-Request change before first fulfilment;
2. whether treatment differs before generation, during generation, or generated-but-not-delivered;
3. if a new purchase/right is required, what becomes of the original still-unconsumed right and how that is consistent with `DEC-299`;
4. whether repeated participant-driven pre-fulfilment replacements have an allowance/cap or other commercial consequence;
5. whether genuine correction of an earlier wrong input is commercially different from discretionary change-of-intent;
6. how the rule composes with `DEC-045` without collapsing refundability, generation, fulfilment and consumption.

## 6.3 Recommended promotion shape — not authority

> A participant-owned material Plan-input change explicitly intended for the current paid Request before first successful fulfilment supersedes the stale Request for fulfilment and never rewrites immutable generation history. The paid Plan entitlement remains unconsumed until successful governed Plan delivery. Product authority must state whether that existing unconsumed right may authorize the replacement Request and whether the rule changes after qualifying generation has begun. Refundability remains governed separately by `DEC-045`. If a new purchase/right is required before first fulfilment, the disposition of the original still-unconsumed right must be stated explicitly rather than inferred as consumed, forfeited, expired or silently reusable. After first successful fulfilment, ordinary preference/progress re-personalisation follows `DEC-038`, subject only to explicit governed exceptions such as `DEC-036`.

For the once-off MVP, the least contradictory candidate is:

```text
one paid Plan right
→ one successful first Plan fulfilment
```

with pre-fulfilment participant supersession treated separately from successful consumption. Exact replacement allowance/cap remains Product policy.

---

# 7. Focused v0.12.0 pressure-test index

| ID | Scenario | Disposition |
|---|---|---|
| `OPS-PT-175` | material current-Request intent change before generation begins | `NEEDS_WORKING_DELTA` |
| `OPS-PT-176` | material change after basis capture but before generation execution | `NEEDS_WORKING_DELTA` |
| `OPS-PT-177` | material change while generation is in progress | `NEEDS_WORKING_DELTA` |
| `OPS-PT-178` | generation completes, delivery has not happened, then intent changes | `NEEDS_WORKING_DELTA` |
| `OPS-PT-179` | accepted intent change races stale generation/delivery completion | `PASS_WITH_REFINEMENT` |
| `OPS-PT-180` | successful delivery wins before participant changes intent | `PASS` |
| `OPS-PT-181` | edit is future-only or unrelated to current Request | `PASS_WITH_REFINEMENT` |
| `OPS-PT-182` | participant changes a non-material field | `PASS_WITH_REFINEMENT` |
| `OPS-PT-183` | safety-relevant new information presented as preference change | `PASS / OUTSIDE OPS-UPD-005` |
| `OPS-PT-184` | correction of earlier wrong Plan input, not changed intent | `PASS_WITH_REFINEMENT` |
| `OPS-PT-185` | successive material changes while replacement work is in flight | `NEEDS_WORKING_DELTA` |
| `OPS-PT-186` | operator edits old basis or deliberately delivers stale Plan | `PASS / NEGATIVE AUTHORITY PROOF` |

Exact reasoning remains in discovery `v0.12.0`.

---

# 8. Current STOP / non-inference rules

- `OPS-UPD-004` remains a Product-authority `CONFLICT_STOP`; downstream may not choose the assessment-credit consumption rule.
- Do not infer universal Super Admin/business override.
- Do not infer 10/25 are identical hard caps to 50.
- Do not infer historical pilot membership disappears after refund/withdrawal (`OPS-UPD-001`).
- Do not infer General Wellness clock start from provider convention (`OPS-UPD-007`).
- Do not infer export-versus-Full-Deletion ordering (`OPS-UPD-006`).
- Do not resurrect closed old terminal-unfulfillable Plan remedy (`OPS-GAP-014`).
- Do not turn JIT/proof/provider/expert gaps into Product Law.
- Do not infer provider refund failure erases customer-money obligation (`OPS-UPD-002`).
- Do not infer partial reversal component identity from amount coincidence/current price/callback order/proportional allocation.
- Do not silently reinterpret `DEC-055`; explicit supersession/refinement is required.
- Do not treat assessment attempt expiry as automatic consumption or automatic reissue/reuse.
- Do not infer `DEC-038` automatically makes pre-first-fulfilment Plan intent change a new-purchase event.
- Do not infer `DEC-045` generation refund closure consumes the still-unfulfilled Plan right or answers replacement-right treatment.
- Do not infer an unconsumed Plan right is automatically freely reusable/rebindable.
- Do not silently consume/forfeit/expire/strand/convert the original Plan right to make a new-fee policy balance.
- Do not generalize `DEC-036`.
- Do not let operator edits, stale delivery or technical sunk cost decide `OPS-UPD-005`.

---

# 9. Pass discipline

Each future semantic pass must:

1. reverify live `main`, branch head and relevant authority;
2. pressure-test one bounded semantic area only;
3. add only genuinely new `OPS-PT` IDs;
4. refine existing `OPS-UPD` / `OPS-GAP` IDs rather than duplicate them;
5. create one SemVer discovery successor for that pass;
6. update this register in a successor;
7. update the downloadable chat snapshot from the same normalized state;
8. stop and report changed / unresolved / convergence.

Register-only normalization may version this register without a discovery successor only when it adds no semantic conclusion.

---

# 10. v0.5.0 disposition

```text
SEMANTIC PRESSURE TESTS ADDED: OPS-PT-175...186
CUMULATIVE PRESSURE TESTS: 186
NEW OPS-UPD: 0
NEW OPS-GAP: 0
NORMALIZED GAP INVENTORY: OPS-GAP-001...025 PRESERVED
UNIQUE CURRENT UPSTREAM DELTAS: OPS-UPD-001...007
OPS-UPD-005: CONFIRMED + NARROWED
OPS-GAP-015: OPEN / SAME SEMANTIC CLASS
HSP-UPD-008: REUSED, NOT DUPLICATED
STALE CURRENT-REQUEST / IMMUTABLE-HISTORY SEMANTICS: WORKING_LOCKED
PLAN ENTITLEMENT CONSUMPTION: SUCCESSFUL GOVERNED DELIVERY REMAINS CONTROLLING CURRENT RULE
REFUNDABILITY VS REPLACEMENT-RIGHT TREATMENT: SEPARATED
PRE-FIRST-FULFILMENT SAME-RIGHT REBINDING / NEW-PURCHASE RULE: OPEN PRODUCT DECISION
REPEATED PARTICIPANT-DRIVEN CHANGE ALLOWANCE: PART OF OPS-UPD-005
POST-FULFILMENT DEC-038: NOT REOPENED
DEC-036 NARROW REGENERATION EXCEPTION: NOT GENERALIZED
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED BY EXISTING UPSTREAM DELTAS + REQUIRED REVIEW/PROMOTION
```
