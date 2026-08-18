# REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md

- **Document status:** PHASE 3 COMPLETE — REFERENCE-FLOW CLOSURE AUDIT PASS
- **Document version:** v0.2.0
- **Started:** 2026-08-17
- **Last updated:** 2026-08-17
- **Current stage:** Phase 3 — Reference Flow Pressure Tests — COMPLETE
- **Completed suite:** FLOW-01 through FLOW-12
- **Closure verdict:** PASS — 0 architecture gaps; 0 governing contradictions; downstream gates preserved
- **Next stage:** Phase 4 — synthesize/review/freeze `03_ARCHITECTURE.md`
- **Architecture authority:** `ARCHITECTURE_LAW_WORKING_v0.35.0.md`, cumulative `ARC-001...ARC-327`
- **Requirements authority:** `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`, 417 frozen ARQs
- **Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`, `00_PLATFORM_v1.2.1.md`, `01_DECISIONS_v1.2.1.md`
- **Planning tracker:** `../02_OPEN_WORK_v1.2.27.md`
- **Governance mode:** CUMULATIVE / APPEND-ONLY PRESSURE-TEST EVIDENCE
- **Authority boundary:** This register pressure-tests accepted Architecture Law across representative end-to-end flows. It does not assign final Domain ownership, invent Resources/tables/modules/packages/thresholds, or authorise executable development.

---

# 1. Purpose

Phase 3 asks one question:

> Can each representative end-to-end journey traverse the completed architecture without an undocumented mechanism or governing contradiction?

It is an **architecture pressure test**, not an implementation specification, benchmark, security penetration test, Feature Pack contract or release proof.

The Phase 3 distinction is:

```text
PHASE 3 — ARCHITECTURE PRESSURE TEST
Can the flow work coherently using accepted law?

PHASE 8 — ARCHITECTURAL / TRACER PROOF
Does the implemented architectural path actually work?

HORIZONTAL HARDENING / RELEASE
How much load does it safely handle and how does it behave under failure?
```

`ARC-327` amends the timing interpretation of `ARC-326`: Phase 3 records the future performance/capacity **proof obligation projection** only. Runtime-only evidence is captured when executable proof exists.

## 1.1 Verdicts

- `PASS`: accepted Architecture Law covers the flow and no unresolved downstream gate is material to the core path.
- `PASS_WITH_DOWNSTREAM_GATES`: Architecture is coherent and complete, while named expert/provider/JIT/proof gates remain intentionally unresolved.
- `FAIL_ARCHITECTURE_GAP`: a material mechanism required by the flow has no accepted Architecture Law.
- `BLOCKED_CONTRADICTION`: governing authorities conflict materially and the correct upstream authority must be amended before continuing.

Unknown table names, indexes, packages, thresholds, Redis keys, load-test sizes, provider settings or Domain ownership are **not** Phase 3 failures when accepted law already defines the enduring contract and intentionally defers the concrete mechanism.

## 1.2 Lean flow contract

Each flow records only:

1. purpose;
2. governing DEC/ARC/OQ references;
3. concise architecture trace;
4. hard invariants;
5. meaningful failure pressure;
6. later executable proof obligations;
7. architecture-gap / contradiction / premature-design review;
8. verdict.

The full `ARC-326` Performance & Capacity Proof Matrix is deferred to the first applicable executable proof stage. No `NOT_YET_MEASURED` placeholder matrix is required here.

---

# 2. Required flow suite

| Flow | Scope | Verdict |
|---|---|---|
| FLOW-01 | Registration → verification → login | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-02 | Checkout → provider verification → payment → entitlement | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-03 | Assessment → submission → scoring → immutable result → report | PASS |
| FLOW-04 | Health intake → safety evaluation → eligibility | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-05 | Eligibility → deterministic plan generation → immutable plan | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-06 | New health risk → safety effect → dependent plan behaviour | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-07 | Nuwe Jy scheduled release → durable work → notification → LiveView | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-08 | Full deletion → storage/processors → backup boundary | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-09 | Future event hold → payment → ticket / expiry | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-10 | Consent → practitioner relationship → scoped access → audit → expiry/revocation | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-11 | Safety-critical correction/withdrawal → dependency discovery → invalidation → operational/participant response → audit | PASS_WITH_DOWNSTREAM_GATES |
| FLOW-12 | Experiment draft/version → eligibility → stable assignment → variant-safe delivery/cache → exposure → authoritative outcome → statistical readout → immutable result/decision → archive/deletion boundary | PASS_WITH_DOWNSTREAM_GATES |

---

# 3. FLOW-01 — Registration → verification → login

## 3.1 Purpose

Pressure-test the identity path from anonymous registration through verified capability and authenticated session establishment.

## 3.2 Governing References

**Product:** `DEC-017`, `DEC-018`, `DEC-027`, `DEC-244...DEC-256`, `DEC-263`  
**Architecture:** `ARC-027`, `ARC-028`, `ARC-110...ARC-117`, `ARC-122...ARC-125`, `ARC-133...ARC-145`, `ARC-146...ARC-153`, `ARC-170...ARC-178`, `ARC-322`, `ARC-327`  
**Open gates:** `OQ-034`, `OQ-035`

## 3.3 Architecture Trace

```text
anonymous browser
→ thin Phoenix/LiveView boundary
→ authoritative Ash registration action
→ durable canonical identity
→ durable verification-delivery intent
→ provider delivery
→ bounded verification capability
→ authoritative verified transition
→ login action
→ layered abuse control + credential verification
→ durable revocable session
→ authorised application capability
```

## 3.4 Hard Invariants

1. Registration cannot create a second identity model for later magic-link or session flows.
2. Browser parameters and verification links cannot directly manufacture verified state.
3. Verification delivery retry cannot create multiple authoritative verification effects.
4. Login/session authority remains server-governed and revocable.
5. Abuse protection may degrade according to risk policy, but may not silently become unlimited on sensitive surfaces.

## 3.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Duplicate registration submission | durable identity/idempotency/uniqueness handling; no duplicate business identity effect | YES |
| Verification email delayed/duplicated | delivery evidence is separate; bounded verification capability remains authoritative | YES |
| Verification link replay | one-purpose replay-controlled capability | YES |
| Login retry storm | layered edge/application/distributed velocity contract | YES |
| Node/process loss after commit | reconstruct from durable identity/session authority | YES |

## 3.6 Later Proof Obligations

**Performance-sensitive:** YES  
**Critical scale concern:** password hashing cost, login bursts, abuse controls, verification delivery backlog.  
**Hard later proof:** retries/abuse must not multiply identity/session effects or bypass limits.  
**Executable proof required:** YES — Authentication/Security Feature Pack, Architectural Proof where needed, Horizontal Hardening.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 3.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — exact auth package details and rate thresholds remain `OQ-034` / `OQ-035`.

## 3.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

The original FLOW-01 substantive verdict is preserved. The only change from v0.1.0 is removal of pre-implementation runtime-evidence ceremony.

---

# 4. FLOW-02 — Checkout → provider verification → payment → entitlement

## 4.1 Purpose

Pressure-test commerce authority across an external payment provider without allowing provider/browser state to become payment or entitlement truth.

## 4.2 Governing References

**Product:** `DEC-039`, `DEC-043`, `DEC-045...DEC-050`, `DEC-258`, `DEC-292`  
**Architecture:** `ARC-027`, `ARC-052`, `ARC-059...ARC-071`, `ARC-146...ARC-169`, `ARC-178...ARC-182`, `ARC-231`, `ARC-232`, `ARC-317`, `ARC-322`, `ARC-327`  
**Open gates:** `OQ-004`, `OQ-035`

## 4.3 Architecture Trace

```text
participant checkout intent
→ authorised application action
→ durable purchase/payment intent
→ Paystack interaction outside authoritative DB transaction
→ browser return and/or verified provider callback/query as external evidence
→ durable reconciliation
→ authoritative payment transition
→ durable idempotent entitlement consequence
→ entitlement authority
→ optional PubSub/UI refresh
```

## 4.4 Hard Invariants

1. Browser-supplied or unverified provider state cannot invent successful payment.
2. Duplicate/reordered Paystack evidence cannot create duplicate payment effects.
3. Duplicate/retried consequence execution cannot create duplicate entitlement grants.
4. Provider timeout means unknown/pending until reconciled; it is neither success nor failure by assumption.
5. App/process failure after provider success must remain reconcilable from durable evidence.

## 4.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Provider timeout | explicit unresolved state + reconciliation | YES |
| Duplicate/reordered webhook | verify, durably receive, dedupe/reconcile independent of arrival order | YES |
| Browser never returns | callback/query reconciliation does not depend on browser | YES |
| Crash after payment evidence before entitlement | durable intent/state permits idempotent continuation | YES |
| Entitlement worker exhausts retries | visible terminal work state; business truth remains reconcilable | YES |

## 4.6 Later Proof Obligations

**Performance-sensitive:** YES  
**Critical scale concern:** provider-bound checkout latency, duplicate storms, DB/worker contention, payment abuse.  
**Hard later proof:** one payment transition / one valid entitlement effect per governed operation identity.  
**Executable proof required:** YES — Commerce Architectural Proof/Feature Pack, provider validation, Horizontal Hardening/Release.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 4.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — exact Paystack retry/refund/subscription/webhook behaviour remains `OQ-004`; exact abuse thresholds remain `OQ-035`.

## 4.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 5. FLOW-03 — Assessment → submission → scoring → immutable result → report

## 5.1 Purpose

Pressure-test a versioned assessment from resumable answers through deterministic submission/scoring and immutable historical output.

## 5.2 Governing References

**Product:** `DEC-051...DEC-070`, especially `DEC-053`, `DEC-054`, `DEC-057...DEC-061`, `DEC-065...DEC-070`  
**Architecture:** `ARC-027`, `ARC-052`, `ARC-059...ARC-071`, `ARC-124`, `ARC-146...ARC-153`, `ARC-189...ARC-194`, `ARC-327`  
**Open gates:** `OQ-006` only if optional score-distance labels are enabled; core launch scoring does not depend on those labels.

## 5.3 Architecture Trace

```text
authorised participant
→ active durable assessment attempt
→ resumable answer writes
→ authoritative final-submit action validates completeness
→ fixed methodology/version inputs
→ deterministic scoring
→ immutable answers + scores + assessment version
→ governed report referencing exact result/content versions
→ protected participant delivery
```

## 5.4 Hard Invariants

1. Final submission cannot succeed with missing required scored answers.
2. Submitted answers, calculated scores and assessment version are not overwritten.
3. Scoring is reproducible from the exact methodology/version used.
4. Duplicate submit/retry cannot create multiple authoritative completed results or double-consume the same attempt entitlement.
5. The delivered report remains traceable to the immutable result and governed content/language versions.

## 5.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Save/reconnect retry | durable resumable attempt; repeat-safe write semantics | YES |
| Duplicate final submit | authoritative idempotency/uniqueness around completion | YES |
| Assessment version retires mid-attempt | active attempt may finish under its captured version; new starts use current allowed version | YES |
| Report rendering/delivery fails after result commit | result remains authoritative; delivery can retry without rescoring | YES |
| Required locale content missing | critical paid output fails closed rather than silently using unapproved fallback | YES |

## 5.6 Later Proof Obligations

**Performance-sensitive:** YES, but not a high-concurrency authority hotspot by default.  
**Critical scale concern:** burst completion/report generation and bounded deterministic scoring.  
**Hard later proof:** duplicate/retry submission must produce one immutable result.  
**Executable proof required:** YES in the Assessment Feature Pack; dedicated Architectural Proof only if implementation introduces material complexity.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 5.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — question/Resource/schema/index design remains Domain/JIT work. `OQ-006` is not needed unless the gated labels are activated.

## 5.8 Verdict

**PASS**

---

# 6. FLOW-04 — Health intake → safety evaluation → eligibility

## 6.1 Purpose

Pressure-test clinically sensitive intake and deterministic routing without allowing incomplete/stale participant data or presentation logic to bypass safety authority.

## 6.2 Governing References

**Product:** `DEC-073...DEC-095`, especially `DEC-074`, `DEC-077...DEC-080`, `DEC-089...DEC-095`  
**Architecture:** `ARC-027`, `ARC-038...ARC-042`, `ARC-052`, `ARC-059...ARC-071`, `ARC-118...ARC-128`, `ARC-131`, `ARC-203`, `ARC-255`, `ARC-327`  
**Open gates:** `OQ-005`, `OQ-007`, `OQ-008`, applicable retention gate `OQ-009`

## 6.3 Architecture Trace

```text
participant
→ purpose-scoped health-intake actions
→ durable provenance-bearing health facts
→ authoritative safety/eligibility action
→ approved rule/protocol version + current inputs
→ deterministic eligibility outcome
→ durable outcome/evidence
→ permitted downstream capability
   OR General Wellness
   OR professional review
   OR insufficient information
```

## 6.4 Hard Invariants

1. Missing safety-critical information cannot silently become automated eligibility.
2. Approved high-risk state blocks automated personalised-plan authority.
3. Temperament/presentation preferences cannot override clinical safety.
4. A later clinical override is scoped/audited and does not erase the original automated outcome.
5. Sensitive fields are loaded/disclosed only for the purpose and action that requires them.

## 6.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Incomplete/withheld safety answer | explicit insufficient-information or governed safe route | YES |
| Concurrent intake edits during evaluation | authoritative action uses coherent current state/versioning/conflict control | YES |
| Rule/protocol changes | governed/versioned policy; historical outcome remains reproducible | YES |
| High-risk fact conflicts with requested plan | safety authority wins; request is refused/rerouted | YES |
| Reviewer/override race | scoped authoritative transition with audit; no destructive rewrite | YES |

## 6.6 Later Proof Obligations

**Performance-sensitive:** YES.  
**Critical scale concern:** bounded safety evaluation under onboarding bursts without unsafe caching or broad health-data loading.  
**Hard later proof:** no concurrency/retry path may produce automated eligibility from incomplete/high-risk authoritative state.  
**Executable proof required:** YES — Safety/Health Feature Pack and release safety gate.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 6.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — exact clinical matrices and validity/urgent wording remain expert gates.

## 6.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 7. FLOW-05 — Eligibility → deterministic plan generation → immutable plan

## 7.1 Purpose

Pressure-test the transition from current eligibility into a complete, reproducible, immutable plan without partial delivery or unsafe stale inputs.

## 7.2 Governing References

**Product:** `DEC-096...DEC-121`, especially `DEC-096`, `DEC-099`, `DEC-102...DEC-110`, `DEC-118...DEC-121`  
**Architecture:** `ARC-027`, `ARC-052`, `ARC-059...ARC-071`, `ARC-124`, `ARC-146...ARC-153`, `ARC-189...ARC-198`, `ARC-327`  
**Open gates:** `OQ-010`, `OQ-011`, `OQ-013`

## 7.3 Architecture Trace

```text
eligible participant
→ authorised plan-generation action
→ current eligibility/entitlement revalidation
→ approved calculation/content/version inputs
→ deterministic generation
→ commit complete immutable plan snapshot + provenance
   OR commit no plan / explicit failure
→ protected delivery
→ later activation revalidates material current safety where required
```

The implementation may be synchronous or durably asynchronous according to bounded-work semantics; Phase 3 does not select that detail.

## 7.4 Hard Invariants

1. Ineligible/high-risk state cannot produce an automated personalised plan.
2. Generation either produces one complete governed plan snapshot or fails closed; partial plans are not authoritative.
3. Retries cannot create duplicate charged/generation effects for the same governed operation.
4. Delivered plans remain reproducible from captured inputs, rule/calculation versions and content versions.
5. Historical plan snapshots are preserved when later corrections, replacements or practitioner-derived versions occur.

## 7.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Generator/process crashes mid-work | no partial authoritative delivery; durable recovery where async | YES |
| Duplicate generation request | durable operation identity/idempotency | YES |
| Health eligibility changes during generation | current preconditions revalidated at authoritative boundary; unsafe result not activated | YES |
| Required governed content/translation absent | fail closed for required paid/safety content | YES |
| Worker retry after commit | repeat-safe/idempotent consequence | YES |

## 7.6 Later Proof Obligations

**Performance-sensitive:** YES.  
**Critical scale concern:** generation cost, content/query fan-in, concurrency, queue/backlog if async.  
**Hard later proof:** no partial/duplicate plan; deterministic/reproducible result under retries and failure.  
**Executable proof required:** YES — Plan Feature Pack; Architectural Proof if generation path is materially complex; Horizontal Hardening for burst generation.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 7.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — formulas/limits (`OQ-010`), adjustment thresholds (`OQ-011`) and exact translation Resources (`OQ-013`) remain downstream.

## 7.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 8. FLOW-06 — New health risk → safety effect → dependent plan behaviour

## 8.1 Purpose

Pressure-test propagation of a newly authoritative safety risk into dependent plan behaviour without relying on cache/PubSub freshness for correctness.

## 8.2 Governing References

**Product:** `DEC-089...DEC-095`, `DEC-110`, `DEC-114`, `DEC-121`  
**Architecture:** `ARC-059...ARC-066`, `ARC-079`, `ARC-080`, `ARC-118...ARC-128`, `ARC-135`, `ARC-146...ARC-153`, `ARC-174...ARC-178`, `ARC-327`  
**Open gates:** `OQ-005`, `OQ-008`, and `OQ-011` where adjustment behaviour is affected

## 8.3 Architecture Trace

```text
new authoritative health fact
→ safety re-evaluation
→ authoritative safety transition / safety case
→ dependent authority invalidation obligation
→ current plan becomes safety-paused/restricted as Product Law requires
→ durable downstream consequences where required
→ cache invalidation + PubSub freshness
→ participant/professional operational response
```

## 8.4 Hard Invariants

1. Safety effect is authoritative even if PubSub/cache invalidation is delayed or lost.
2. A stale cache cannot authorise a new adjustment or unsafe continuation.
3. Existing historical plan evidence is preserved; safety pause does not rewrite history.
4. Repeated risk detection cannot multiply dependent transitions/notifications incorrectly.
5. Returning from high-risk state requires the approved clinical authority/protocol; it cannot self-clear through convenience state.

## 8.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| PubSub missed | current authoritative state still blocks unsafe action | YES |
| Cache stale | material safety path bypasses/invalidates stale acceleration | YES |
| Dependent consequence job fails | durable intent remains visible/retryable; authority already changed | YES |
| Concurrent plan adjustment | revalidation/current-policy check prevents stale unsafe commit | YES |
| Duplicate health-risk event | idempotent/repeat-safe safety transition | YES |

## 8.6 Later Proof Obligations

**Performance-sensitive:** YES.  
**Critical scale concern:** rapid dependency invalidation/fan-out without DB/cache stampede.  
**Hard later proof:** material risk becomes effective despite lost/reordered observations and concurrent plan actions.  
**Executable proof required:** YES — Safety + Plan Feature Packs; failure/recovery hardening.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 8.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — exact safety matrices, participant wording and dependency/index representation remain downstream.

## 8.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 9. FLOW-07 — Nuwe Jy scheduled release → durable work → notification → LiveView

## 9.1 Purpose

Pressure-test scheduled programme delivery across business-effective access, durable execution, notification and realtime UI freshness.

## 9.2 Governing References

**Product:** `DEC-196...DEC-219`, especially `DEC-199...DEC-202`, `DEC-211`, `DEC-218`; `DEC-261...DEC-264`, `DEC-286`  
**Architecture:** `ARC-040`, `ARC-054`, `ARC-146...ARC-165`, `ARC-170...ARC-178`, `ARC-189...ARC-195`, `ARC-223...ARC-227`, `ARC-259`, `ARC-292`, `ARC-320`, `ARC-321`, `ARC-327`  
**Open gates:** `OQ-017`, `OQ-024`, `OQ-026`, `OQ-027`, `OQ-036`

## 9.3 Architecture Trace

```text
approved edition/version + durable schedule
→ business-effective release rule
→ durable scheduled execution where a transition/consequence is required
→ bounded Oban work
→ authoritative programme/content access becomes correct
→ governed notification intent
→ provider delivery
→ PubSub observation
→ LiveView refresh/re-authorises from current authority
```

## 9.4 Hard Invariants

1. Notification delivery is not programme-release authority.
2. PubSub echo is not confirmation of release.
3. Scheduled/retried work is idempotent and cannot duplicate participant consequences.
4. Node restart/deployment cannot permanently lose a required release consequence.
5. Backlog catch-up may degrade notification/realtime freshness before crushing newly arriving critical OLTP work.

## 9.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Scheduler/node down at release time | durable schedule/work recovery; business-effective semantics remain explicit | YES |
| Notification provider outage | programme truth remains; delivery retries/degrades independently | YES |
| Duplicate scheduled execution | semantic idempotency/deduplication | YES |
| Reconnect storm at release | bounded realtime/fan-out; clients reconstruct from authority | YES |
| Large backlog after recovery | controlled catch-up within shared resource/provider budgets | YES |

## 9.6 Later Proof Obligations

**Performance-sensitive:** YES.  
**Critical scale concern:** simultaneous release populations, notification fan-out, queue catch-up, LiveView reconnect/fan-out amplification.  
**Hard later proof:** scheduled access remains correct while notification/realtime may lag; recovery cannot duplicate release effects.  
**Executable proof required:** YES — Nuwe Jy/Notifications Feature Packs, Architectural Proof for scheduling/fan-out where needed, HH/Release.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 9.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — source inventory, operational capacity, channels/provider, quiet hours and exact schedules remain named downstream gates.

## 9.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 10. FLOW-08 — Full deletion → storage/processors → backup boundary

## 10.1 Purpose

Pressure-test full deletion as a durable cross-system privacy lifecycle, including object storage, processors, derived models and disaster recovery.

## 10.2 Governing References

**Product:** `DEC-221...DEC-243`, especially `DEC-221`, `DEC-224...DEC-239`, `DEC-243`  
**Architecture:** `ARC-093`, `ARC-109`, `ARC-233...ARC-250`, `ARC-286`, `ARC-327`  
**Open gates:** `OQ-029`, `OQ-030`, `OQ-031`, `OQ-032`, `OQ-037`

## 10.3 Architecture Trace

```text
strongly verified deletion request
→ immediate normal-access revocation
→ governed cancellation window where applicable
→ durable idempotent deletion orchestration
→ each data-owning capability executes its deletion contract
→ object/derivative/external-processor deletion or lawful isolation
→ derived search/analytics/read-model suppression
→ minimal non-reconstructive completion/suppression evidence
→ backups age out normally
→ any restore replays later deletion/withdrawal truth before service promotion
```

## 10.4 Hard Invariants

1. Deleting the account row alone never means deletion complete.
2. Eligible identifiable representations must be deleted/anonymised across governed stores/processors.
3. Retained-by-obligation records are isolated/minimised and cannot recreate product authority.
4. Older backup restore cannot resurrect a completed deletion into normal service.
5. Repeated deletion execution is idempotent and safely resumable.

## 10.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| External processor unavailable | durable pending/retry state; deletion not falsely marked complete | YES |
| Object/derivative delete fails | durable retry/reconciliation | YES |
| Orchestrator restarts | resume from durable completion evidence | YES |
| Legal hold affects subset | narrow scoped hold; unrelated eligible deletion continues | YES |
| Old backup restored | recovery-gated environment + suppression/deletion replay before service | YES |

## 10.6 Later Proof Obligations

**Performance-sensitive:** YES, mainly bounded orchestration/recovery rather than synchronous latency.  
**Critical scale concern:** large representation fan-out, processor retries, restore-time replay and derived-model rebuild.  
**Hard later proof:** no deleted participant becomes recoverable/servable after retries or older restore.  
**Executable proof required:** YES — Privacy Feature Pack, deletion/restore Architectural Proof, recovery exercises/HH.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 10.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — retention durations, processor inventory, backup product/expiry and exact operational deadlines remain explicit gates.

## 10.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 11. FLOW-09 — Future event hold → payment → ticket / expiry

## 11.1 Purpose

Pressure-test scarce-capacity commerce under concurrent holds, external payment latency, expiry and eventual ticket confirmation.

## 11.2 Governing References

**Product:** `DEC-191...DEC-195`, especially `DEC-192`, `DEC-193`; `DEC-279`  
**Architecture:** `ARC-068...ARC-071`, `ARC-146...ARC-169`, `ARC-259`, `ARC-260`, `ARC-315...ARC-317`, `ARC-322`, `ARC-327`  
**Open gates:** `OQ-004`, `OQ-022`

## 11.3 Architecture Trace

```text
attendee purchase request
→ authorised reservation action
→ atomic authoritative short-lived capacity hold
→ external payment interaction outside held DB lock/transaction
→ verified provider evidence + reconciliation
→ confirm allocation only through authoritative capacity protocol
→ durable ticket/entitlement consequence
OR
→ hold expires/releases capacity
→ later payment evidence enters governed reconciliation, not oversell
```

## 11.4 Hard Invariants

1. Confirmed allocations may never exceed authoritative capacity.
2. A hold is not a confirmed ticket/entitlement.
3. Duplicate provider evidence or retries cannot issue duplicate tickets.
4. Hold expiry/payment-confirmation races have one deterministic authoritative outcome.
5. Slow provider calls do not hold authoritative DB locks open.

## 11.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Many simultaneous holds | invariant-specific atomic reservation protocol | YES |
| Provider timeout | pending/reconciliation; hold lifecycle remains governed | YES |
| Payment evidence arrives after hold expiry | reconcile under event/payment policy; never fabricate capacity | YES |
| Crash during confirm/ticket consequence | durable state/idempotency permits safe continuation | YES |
| Bot/flash-sale surge | admission/rate/queue protection may reject/throttle before unsafe acceptance | YES |

## 11.6 Later Proof Obligations

**Performance-sensitive:** YES — highest class.  
**Critical scale concern:** flash-sale contention, hold expiry, DB pool/locks, queueing/rate controls, provider latency.  
**Hard later proof:** **zero confirmed oversell** under concurrency, retries, duplicates, multi-node execution and relevant failures.  
**Executable proof required:** YES — mandatory event reservation Architectural Proof plus HH/Release proof.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 11.7 Gap Review

Architecture gap: **NONE** — Architecture defines the required invariant and mechanism class without prematurely choosing the exact reservation schema/Redis layout.  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — exact locking, expiry, Redis acceleration, waitlist and flash-sale implementation remain `OQ-022`; Paystack specifics remain `OQ-004`.

## 11.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 12. FLOW-10 — Consent → practitioner relationship → scoped access → audit → expiry/revocation

## 12.1 Purpose

Pressure-test sensitive practitioner access as contextual, purpose-bound authority rather than role-based blanket access.

## 12.2 Governing References

**Product:** `DEC-024...DEC-026`, `DEC-094`, `DEC-229`, `DEC-232`, `DEC-247`  
**Architecture:** `ARC-037...ARC-042`, `ARC-110`, `ARC-115...ARC-131`, `ARC-135`, `ARC-140`, `ARC-327`  
**Open gates:** `OQ-009`, `OQ-033` plus legal/practitioner agreement gates

## 12.3 Architecture Trace

```text
participant gives purpose-specific consent
→ explicit practitioner relationship/grant with scope + expiry
→ practitioner authenticates with required assurance
→ authoritative action policy evaluates role + relationship + purpose + consent + scope + expiry
→ minimum necessary fields loaded
→ material access evidence recorded
→ expiry/revocation changes durable authority
→ later access re-evaluates current state and is denied
```

## 12.4 Hard Invariants

1. Practitioner role alone never grants participant private-record access.
2. Consent alone without the required active relationship/scope does not grant access.
3. Revocation/expiry becomes effective from durable authority even if realtime invalidation is missed.
4. Long-lived LiveViews/actions re-authorise against current state.
5. Material sensitive access remains auditable without exposing excessive health content in generic logs.

## 12.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Consent revoked while practitioner UI is open | next authoritative action re-authorises; broadcasts only accelerate freshness | YES |
| Stale cache of relationship | material authority read/bypass prevents stale grant | YES |
| Practitioner session loses required assurance | step-up/current assurance policy blocks sensitive action | YES |
| Relationship expires mid-workflow | current state checked at action boundary | YES |
| Audit/telemetry subsystem degraded | audit evidence remains separate from generic telemetry; exact risk-class capture is governed | YES |

## 12.6 Later Proof Obligations

**Performance-sensitive:** YES, but security/privacy correctness dominates latency.  
**Critical scale concern:** policy lookup/field privacy without N+1 or broad health-data loads.  
**Hard later proof:** revoked/expired relationship cannot regain access through cache, reconnect or stale session context.  
**Executable proof required:** YES — Practitioner/IAM Feature Packs and security hardening.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 12.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — final professional record authority/retention and concrete relationship Resources belong to expert/Domain/JIT work.

## 12.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 13. FLOW-11 — Safety-critical correction/withdrawal → dependency discovery → invalidation → operational/participant response → audit

## 13.1 Purpose

Pressure-test a material correction/withdrawal across immutable history, dependent representations and freshness mechanisms.

## 13.2 Governing References

**Product:** `DEC-121`, `DEC-129`, `DEC-137`, `DEC-188`, `DEC-241`  
**Architecture:** `ARC-065`, `ARC-079`, `ARC-080`, `ARC-109`, `ARC-128`, `ARC-135`, `ARC-146...ARC-153`, `ARC-189...ARC-197`, `ARC-212...ARC-221`, `ARC-327`  
**Open gates:** `OQ-014`, `OQ-016`; `OQ-021` where affected representation is recorded/live media

## 13.3 Architecture Trace

```text
authorised safety correction/withdrawal
→ new governed version / explicit withdrawal state
→ historical delivered evidence preserved
→ dependent references/eligibility discovered through governed relationships
→ authoritative future eligibility/access invalidated
→ durable consequences for search/cache/media/message/participant operations where required
→ cache purge/invalidation + PubSub freshness
→ operational/participant response
→ immutable audit/evidence
```

## 13.4 Hard Invariants

1. Correction/withdrawal does not destructively rewrite historical evidence.
2. Withdrawn material cannot remain eligible for new governed delivery merely because a cache/index is stale.
3. PubSub is not the sole withdrawal mechanism.
4. Dependent invalidation/consequence execution is idempotent and resumable.
5. Participant/operational response is based on the authoritative correction class, not provider delivery status.

## 13.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Cache purge misses/fails | authoritative access/publication state blocks unsafe new delivery | YES |
| Search/read model lags | projection is derived; current authority governs access | YES |
| Downstream media/message provider unavailable | durable consequence retries/degrades; withdrawal truth remains | YES |
| Dependency fan-out partially completes | durable bounded orchestration can resume/reconcile | YES |
| Concurrent user requests old content | current policy/publication/access is checked before governed delivery | YES |

## 13.6 Later Proof Obligations

**Performance-sensitive:** YES for high-fan-out withdrawals.  
**Critical scale concern:** dependency discovery, invalidation fan-out, cache/search regeneration and notification backlog.  
**Hard later proof:** safety-critical withdrawal becomes effective even with stale/missing derived state and partial consequence failure.  
**Executable proof required:** YES — Content/Safety Feature Packs; Architectural Proof for broad invalidation paths; HH/failure recovery.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 13.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — exact dependency indexes, purge APIs, scheduler mechanics and media-specific retention remain downstream gates/JIT.

## 13.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 14. FLOW-12 — Experiment lifecycle → stable assignment → safe delivery → exposure → authoritative outcome → immutable learning

## 14.1 Purpose

Pressure-test first-party A/B/n experimentation without allowing experiments or analytics to become business authority or contaminate public caching/privacy.

## 14.2 Governing References

**Product:** `DEC-293`  
**Architecture:** `ARC-179...ARC-188`, `ARC-207...ARC-210`, `ARC-225`, `ARC-226`, `ARC-230`, `ARC-249`, `ARC-325`, `ARC-327`  
**Open gates:** `OQ-040`, and `OQ-014` for any future experiment-sensitive shared edge cache

## 14.3 Architecture Trace

```text
draft/versioned experiment
→ governed activation freezes configuration
→ eligibility
→ deterministic sticky assignment
→ clean canonical URL
→ variant-safe delivery / shared HTML cache bypass unless proven safe
→ exposure only when treatment is actually experienced
→ authoritative business outcome occurs independently
→ deduplicated analytics attribution/reconciliation
→ governed statistical readout
→ immutable aggregate result/decision
→ archive
→ privacy/deletion suppression applied to participant-linked evidence
```

## 14.4 Hard Invariants

1. Assignment is not exposure.
2. Experiment treatment cannot alter protected payment, entitlement, clinical/safety or accounting truth.
3. Public assignment does not create variant URLs/canonical fragmentation.
4. Shared cache cannot cross-contaminate treatments.
5. Conversion/outcome facts originate from authoritative business state, not analytics-provider claims.
6. Activated experiment configuration and historical result/decision are immutable/versioned evidence.

## 14.5 Failure Pressure

| Failure | Architecture response | Covered? |
|---|---|---|
| Assignment adapter unavailable | governed default/reconstructable behaviour; no fabricated exposure | YES |
| Exposure duplicated/missing | stable event identity/deduplication; assignment remains separate | YES |
| Analytics pipeline lags | experiment readout freshness degrades; business operation continues | YES |
| Concurrent experiments interact | explicit interaction/isolation governance | YES |
| Cache threatens treatment leakage | initial shared full-page cache bypass; later partitioning must be proven | YES |
| Participant deletion | analytics/derived models rebuild/suppress under privacy law | YES |

## 14.6 Later Proof Obligations

**Performance-sensitive:** YES.  
**Critical scale concern:** assignment/delivery overhead, exposure event volume, analytics lag/rebuild and composite load against OLTP.  
**Hard later proof:** no variant leakage; stable assignment; valid exposure/outcome dedupe; unexplained material SRM remains a validity blocker.  
**Executable proof required:** YES — `OQ-040` Architectural Proof, Experiment Feature Pack, HH/Release where material.  
**Full executable Performance & Capacity Matrix:** DEFERRED.

## 14.7 Gap Review

Architecture gap: **NONE**  
Contradiction: **NONE**  
Premature implementation decision required: **NO** — exact assignment hash/library, statistical engine, cache partitioning and event schema remain proof/JIT decisions.

## 14.8 Verdict

**PASS_WITH_DOWNSTREAM_GATES**

---

# 15. Consolidated Phase 3 Closure Audit

## 15.1 Results

```text
Required flows:                 12
Completed flows:                12

PASS:                            1
PASS_WITH_DOWNSTREAM_GATES:     11
FAIL_ARCHITECTURE_GAP:           0
BLOCKED_CONTRADICTION:           0

Product Law amendments required: 0
ARQ amendments required:         0
Flow mechanism ARCs required:    0
Post-closure governance ARC:      1  (ARC-327, timing/depth amendment to ARC-326)
Premature Domain ownership:       0
Implementation authorised:       NO
```

## 15.2 Closure findings

1. **The architecture is coherent across all twelve representative journeys.** No flow requires an undocumented authority, persistence, async, provider, realtime, privacy, security or recovery mechanism.
2. **The only Phase 3 correction was proof timing, not product/system mechanism.** `ARC-327` narrows `ARC-326` so Phase 3 records future proof obligations while executable stages retain the full Performance & Capacity Proof Matrix.
3. **Downstream gates remain in their proper authority layer.** Paystack behaviour, clinical thresholds, notification providers, event reservation detail, processor inventories, RPO/RTO, practitioner-record authority and experiment implementation proof remain explicit gates rather than Architecture gaps.
4. **No final Domain ownership was invented.** The flows speak in authoritative capability/state terms; `04_DOMAIN_MAP.md` still decides WHO owns concrete business truth.
5. **No implementation design was legislated.** Exact tables, indexes, Redis structures, TTLs, queue names, PubSub topics, provider settings, package choices and test sizes remain downstream.
6. **Executable proof remains mandatory.** Phase 3 PASS is not a benchmark or release claim. Each flow's listed obligations must be instantiated through the full `ARC-326` matrix at the first applicable executable proof stage.

## 15.3 Phase 3 verdict

**PASS — PHASE 3 COMPLETE**

The project may advance to Phase 4:

```text
03_ARCHITECTURE.md synthesis
→ ARQ/ARC/downstream-gate traceability
→ consistency/security/privacy/failure/performance review
→ lightweight traceability check against FLOW-01...FLOW-12
→ rerun only a flow materially affected by a synthesis correction or later Architecture amendment
→ freeze if no contradiction/gap is introduced
```

Do **not** rewrite or formally rerun all twelve pressure tests merely because `03_ARCHITECTURE.md` restates the already-accepted law.

---

# 16. Phase 3 STOP Conditions

Phase 3 is now closed. If a later synthesis review reopens a flow, stop that affected flow only when one of these occurs:

- genuine Product Law ↔ Architecture contradiction;
- required architecture mechanism does not exist;
- accepted ARC cannot satisfy a hard invariant;
- a flow cannot be reasoned about without prematurely assigning Domain ownership;
- a real Architecture amendment is required.

Do **not** stop because a table name, index, package, threshold, provider setting, Redis key, load-test size or other JIT detail is unknown.

---

# 17. Change Log

## v0.2.0 — 2026-08-17 — Lean Phase 3 correction + FLOW-01...FLOW-12 closure

- SemVer transition: `v0.1.0 → v0.2.0`.
- Preserved FLOW-01's `PASS_WITH_DOWNSTREAM_GATES` verdict and substantive architecture findings while compacting it into the lean Phase 3 format.
- Adopted `ARC-327` staged proof depth: Phase 3 records proof obligations; executable stages instantiate the full `ARC-326` matrix.
- Removed runtime-only `NOT_YET_MEASURED` placeholder matrix ceremony from Phase 3.
- Completed FLOW-02 through FLOW-12 using the lean architecture-pressure-test template.
- Consolidated closure result: 12/12 complete; 0 Architecture gaps; 0 contradictions; no Product Law/ARQ amendment; no final Domain ownership or implementation design invented.
- Advanced the next governed stage to `03_ARCHITECTURE.md` synthesis/review/freeze.
- Implementation remains stopped.
