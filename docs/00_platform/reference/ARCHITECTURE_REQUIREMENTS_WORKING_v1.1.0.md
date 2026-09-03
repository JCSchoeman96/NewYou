# ARCHITECTURE_REQUIREMENTS_WORKING.md

- **Document status:** CURRENT / COMPLETE AR-000 REQUIREMENTS REGISTER
- **Document version:** v1.1.0
- **Last updated:** 2026-09-03
- **Previous version:** v1.0.0 (preserved at `docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`)
- **Change type:** MINOR — post-freeze Product Law v1.3.0 source propagation and append-only additive requirements
- **Governance mode:** CUMULATIVE / APPEND-ONLY HISTORY
- **Started:** 2026-08-16
- **Current scope captured:** Complete v1.0.0 AR-000 history plus the governed Stage 3A.2 amendment for Product Law v1.3.0 §§21M–21Q; Performance and Analytics remain closed
- **Next planned scope:** Stage 3B — Independent Architecture/Engineering Classification; Architecture Law remains unamended
- **Purpose:** Preserve every accepted architecture requirement and its historical reasoning while appending the accepted Product-Law delta as ARQ requirements.
- **Authority boundary:** This document records accepted AR-000 requirements — what architecture must make true. It does **not** itself choose final implementation mechanisms or replace `03_ARCHITECTURE.md`, `04_DOMAIN_MAP.md`, Domain Dossiers, Feature Pack contracts, or `ARC-nnn` decisions.

## Governing source pack

This current successor retains the complete v1.0.0 history and appends the Stage 3A.2 amendment derived from the current Product Law source set:

- `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
- `00_PLATFORM_v1.3.0.md`
- `01_DECISIONS_v1.3.0.md`
- `02_OPEN_WORK_v1.2.32.md`
- `docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` — preserved v1.0.0 historical evidence
- `docs/00_platform/archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md` — non-authoritative Stage 3A.1 evidence

The v1.0.0 freeze narrative below remains historical content. It is not rewritten as though Product Law v1.3.0 existed on 2026-08-16. The post-freeze amendment is explicitly appended under `# 10`.

Where this document appears to conflict with upstream Product Law or an approved later Architecture Law decision, work must STOP and the conflict must be routed to the correct authority rather than silently reconciled.

---

# 1. Permanent Maintenance Rule

This document is a **living cumulative record** and must always be kept up to date as additional AR-000 requirements and Grill-Me decisions are accepted.

## 1.1 Never remove locked history

Once an accepted requirement is added:

- do **not** delete it;
- do **not** silently weaken it;
- do **not** renumber it merely for neatness;
- do **not** overwrite its historical meaning without an explicit amendment record.

If a later finding changes an earlier requirement:

1. retain the original entry;
2. mark the original `SUPERSEDED`, `AMENDED`, or `INVALIDATED` as appropriate;
3. append a new requirement or amendment entry;
4. link the old and new entries explicitly;
5. record the reason, evidence, date, and affected downstream artifacts.

This preserves the reasoning trail.

## 1.2 Working-status vocabulary

- `ACCEPTED`: selected and locked for AR-000.
- `ACCEPTED_WITH_REFINEMENT`: recommendation accepted with an explicit user refinement.
- `AMENDED`: still active, but later clarification modifies its interpretation.
- `SUPERSEDED`: replaced by a later requirement; retained for history.
- `INVALIDATED`: later evidence proves the requirement should no longer govern; retained for history.
- `PENDING`: not yet decided.
- `ESCALATED`: requires Product Law, expert, vendor, or other authority before closure.

## 1.3 Requirement strength

Each accepted item may be classified as one or more of:

- `MANDATORY_INVARIANT`
- `MANDATORY_REQUIREMENT`
- `PERFORMANCE_FLOOR`
- `PERFORMANCE_TARGET`
- `ARCHITECTURAL_PRINCIPLE`
- `EVIDENCE_GATED`
- `DEFERRED_TO_ARCHITECTURE`
- `DEFERRED_TO_DOMAIN_DOSSIER`
- `RELEASE_GATE_INPUT`

## 1.4 AR-000 versus Architecture Law

The chain remains:

```text
Frozen Product Law
        ↓
AR-000 source extraction + clustering; focused Grill-Me only when a material ambiguity remains
        ↓
ARQ requirements — what must be true
        ↓
AR-001 ... AR-009 architecture workstreams
        ↓
ARC-nnn decisions — how the platform will make it true
        ↓
03_ARCHITECTURE.md
        ↓
Domain Law / Feature Packs / JIT Domain Dossiers
        ↓
Architectural Proof / Vertical Slices / Hardening
```

No accepted AR-000 requirement automatically means a specific technology is mandatory unless the requirement itself explicitly makes that technology part of the required product/platform contract.

---

# 2. Grill-Me Operating Rule

All focused Grill-Me rounds must use:

1. a multiple-choice question;
2. a recommended option;
3. rationale based on the governing project requirements, current primary technical documentation, and recognised engineering best practice;
4. explicit trade-offs or consequences;
5. user acceptance or an alternative selection;
6. conversion of the accepted choice into one or more durable ARQ requirements.

Accepted choices must be added to this document before or alongside subsequent rounds so that no decision depends only on chat history.

## 2.1 Effective AR-000 operating-mode amendment — v0.16.0

The multiple-choice format above remains the required format **when a focused Grill-Me is actually justified**, but focused Grill-Me is no longer the default method for the remaining AR-000 surface.

Default AR-000 processing is now:

```text
Product Law source coverage
→ extract architecture-relevant obligations
→ cluster related obligations at meaningful architecture level
→ record concise ARQ clusters with exact source trace
→ route unresolved material ambiguity only
```

A focused Grill-Me may be opened only when the source pack leaves a genuine unresolved choice that would materially change architecture, correctness, privacy/security, failure semantics, scale behaviour, or an approved product capability. Engineering best practice that can be decided properly in AR-001…AR-009 is **not** by itself a reason to create another AR-000 Grill round.

Do not measure AR-000 completeness by ARQ count. Prefer one coherent clustered requirement over many micro-ARQs when the source obligations share one architectural meaning. Performance and Analytics remain closed and are not reopened absent a genuine contradiction or upstream change.

## 2.2 AR-000 completion test

The remaining AR-000 work is complete when:

> AR-001…AR-009 can proceed without inventing Product Law and without missing a material architecture constraint.

AR-000 must not pre-decide final domain ownership, library choice, exact adapter/module structure, table/index/key/TTL/queue/topic design, or other HOW/WHO decisions that belong to Architecture Law, `04_DOMAIN_MAP.md`, or JIT Domain Dossiers.

---

# 3. AR-000-P — Performance, Concurrency, Scaling & Resilience

## 3.1 Round P1 — Workload Envelope, Traffic Shape & Acceptable Degradation

### ARQ-PERF-001 — Relevant meaning of 100,000 concurrent users
- **Grill source:** P1.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Requirement:** The platform architecture must have a credible path to supporting approximately 100,000 simultaneously active or connected users where relevant, while each business flow receives its own realistic concurrency envelope. The platform must not impose a fictional 100,000-simultaneous-request requirement on every action.
- **Primary downstream workstreams:** AR-001, AR-005, AR-008, AR-009

### ARQ-PERF-002 — Scale-ready architecture from the beginning
- **Grill source:** P1.2
- **Accepted option:** B
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Requirement:** Architecture and implementation must be performance-aware and scale-ready from first delivery. Known structural bottlenecks, knowingly throwaway authority models, and designs that predictably require fundamental rewrites at growth are not acceptable merely because initial traffic is small. Infrastructure capacity may scale progressively with measured demand, but the platform should be optimised as far as reasonably possible from the beginning so later growth requires as little fundamental change as possible.
- **User refinement:** “We must make sure to optimize everything as much as we can, so that not much needs to be changed when the platform grows and scales.”
- **Guardrail:** This does not justify speculative complexity with no known or locked future requirement. Optimise fundamentals first; acceleration still requires justification.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-003 — Multiple workload profiles, not one generic benchmark
- **Grill source:** P1.3
- **Accepted option:** C
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Architecture and performance validation must model materially different workload shapes separately, including at minimum ordinary sustained authenticated use, campaign/login bursts, scheduled programme/content releases, scarce-inventory flash sales, and abusive/bot/accidental retry traffic where relevant.
- **User refinement:** The project must build explicit load tests and pressure tests for these workload classes.
- **Evidence requirement:** Relevant capabilities must receive repeatable load, stress, spike, breakpoint/pressure, soak, and failure/recovery tests as appropriate rather than relying on theoretical concurrency assumptions alone.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-004 — Graceful degradation priority hierarchy
- **Grill source:** P1.4
- **Accepted option:** A
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / ARCHITECTURAL_PRINCIPLE
- **Requirement:** Under extreme load, degrade lower-criticality freshness and convenience before authoritative correctness. A default degradation order is: analytics freshness → non-essential recommendation/personalisation freshness → non-critical notifications → non-essential realtime updates → ordinary convenience features. Security/authentication correctness, privacy, clinical/safety truth, payment truth, entitlement truth, and confirmed inventory/capacity truth must not be weakened to preserve convenience or latency.
- **Primary downstream workstreams:** AR-004, AR-005, AR-007, AR-008, AR-009

### ARQ-PERF-005 — Bounded waiting and controlled admission
- **Grill source:** P1.5
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** When a workload approaches unsafe saturation, the platform must use bounded waiting and an explicit action-appropriate response such as throttling, controlled queueing, rejection, or fail-fast behaviour rather than allowing unbounded work accumulation and latency growth.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-006 — Failure-domain isolation for optional dependencies
- **Grill source:** P1.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Optional acceleration, analytics, notification, presentation, or similar dependencies should fail independently wherever technically possible. Failure of an optional component must not unnecessarily remove unrelated authoritative capability. Degraded behaviour must not invent successful authoritative outcomes.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008, AR-009

### ARQ-PERF-007 — Business-effective time versus fan-out execution time
- **Grill source:** P1.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Requirement:** For mass scheduled releases, authoritative eligibility/access should become logically correct at the promised business-effective time, while non-authoritative downstream consequences such as notifications, analytics projections, and secondary fan-out may execute over a defined bounded window. Exact-second mass mutations must not be required without a real business need.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008, AR-009

### ARQ-PERF-008 — Multi-node correctness from the beginning
- **Grill source:** P1.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** The application architecture must be correct under multi-node operation from the beginning even if an initial deployment temporarily runs a single application node. No critical invariant may depend on permanent single-node locality.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-009 — International-safe architecture without premature active-active multi-region
- **Grill source:** P1.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Design for timezone-safe, localisation-safe, and future regional deployment while not requiring active-active multi-region infrastructure for MVP. Avoid choices that unnecessarily prevent future regionalisation.
- **Primary downstream workstreams:** AR-001, AR-005, AR-006, AR-008, AR-009

### ARQ-PERF-010 — Overload principle: correct refusal over unsafe acceptance
- **Grill source:** P1.10
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Under overload, shed optional work before compromising authoritative correctness. Reject, throttle, or explicitly defer work before accepting an operation that the platform cannot safely honour. Correct refusal is preferable to false success.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

---

## 3.2 Round P2 — Latency, SLOs & User-Perceived Performance

### ARQ-PERF-011 — Percentile-based latency measurement
- **Grill source:** P2.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Important/common latency SLIs must primarily use percentiles such as p50/p90/p95/p99. A mean/average must never be the sole performance measure.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-012 — Latency classes instead of universal sub-100ms
- **Grill source:** P2.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** PERFORMANCE_TARGET / DEFERRED_TO_ARCHITECTURE
- **Requirement:** Use explicit latency classes based on action semantics rather than applying a universal sub-100ms requirement. Suitable hot/common paths should target the existing sub-100ms objective; normal durable interactions, complex synchronous flows, provider-bound flows, and asynchronous work receive fit-for-purpose targets.
- **Provisional architecture starting points:** Fast interactive actions may aim for ≥90% under 100ms and ≥99% under 400ms server-side; normal durable interactions may aim for p95 under 500ms and p99 under 1s; checkout retains p99 under 5s where provider latency permits. Exact class boundaries remain an architecture/SLO decision.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-013 — Measure both system and user-perceived performance
- **Grill source:** P2.3
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Measure backend/component latency for diagnosis and end-to-end/user-perceived latency for product quality. The observability model must allow attribution across server processing, database work, queues, external providers, network/client effects, and frontend/LiveView behaviour where applicable.
- **Primary downstream workstreams:** AR-002, AR-005, AR-008, AR-009

### ARQ-PERF-014 — Core Web Vitals floor
- **Grill source:** P2.4
- **Accepted option:** A
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Strength:** PERFORMANCE_FLOOR / RELEASE_GATE_INPUT
- **Requirement:** The current “good” Core Web Vitals thresholds are the bare minimum acceptable user-experience floor wherever the metric applies. The platform must aim to outperform the current “good” thresholds wherever reasonably achievable. Falling below the “good” range is a performance regression, not an acceptable steady-state target.
- **User refinement:** “Current ‘good’ Core Web Vitals must be the bare minimum, nothing worse than that and we aim for better than.”
- **Current baseline captured when locked:** LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 at the 75th percentile, evaluated appropriately across mobile and desktop.
- **Future-proofing rule:** Because external CWV definitions can evolve, architecture/release checks must use the then-current official “good” thresholds and may only tighten the project target, not silently weaken this floor.
- **Primary downstream workstreams:** AR-002, AR-008, AR-009

### ARQ-PERF-015 — LiveView performance decomposition
- **Grill source:** P2.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** LiveView performance must be observable at meaningful stages rather than collapsed into one generic HTTP metric, including mount, parameter handling, event handling, render duration, relevant component work, connection behaviour, and user-visible interaction timing where applicable.
- **Primary downstream workstreams:** AR-002, AR-008, AR-009

### ARQ-PERF-016 — Separate internal and provider latency
- **Grill source:** P2.6
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Measure both the end-to-end latency experienced by the user and the internal-versus-external dependency contribution. Provider latency must not be ignored, but it must be separable from platform processing for diagnosis and SLO interpretation.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008, AR-009

### ARQ-PERF-017 — Async boundary determined by semantics
- **Grill source:** P2.7
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Work becomes asynchronous based on semantics and failure behaviour, not an arbitrary duration threshold. Expensive, unbounded, retryable, fan-out-heavy, provider-dependent, or non-immediately-required work should generally use durable async execution with a fast authoritative acknowledgement when appropriate.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-018 — Cold-cache, restart and recovery performance testing
- **Grill source:** P2.8
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Test applicable paths under warm state, cold-cache state, node restart, rolling deployment, and dependency recovery. Warm-cache benchmark performance alone is insufficient evidence.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-019 — No intentional performance debt; no speculative complexity
- **Grill source:** P2.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Build performance-aware from day one. Eliminate known structural inefficiencies, use appropriate data/query shapes, prevent N+1 and unbounded work, keep transactions bounded, and manage payload/memory/concurrency deliberately. Additional architectural complexity such as caching, denormalisation, or special coordination is introduced only where a current or locked future requirement or measurement justifies it.
- **Doctrine:** No intentional performance debt on known critical/common paths. No speculative complexity without evidence.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-020 — Material performance regressions can block delivery
- **Grill source:** P2.10
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** RELEASE_GATE_INPUT / MANDATORY_REQUIREMENT
- **Requirement:** Relevant slices and Feature Packs must carry measurable performance budgets and evidence. Material unexplained regressions are failed acceptance criteria. Deterministic checks should be used where possible, with benchmark/load-test evidence used for actual latency and throughput.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-021 — Progressive performance-test regime
- **Grill source:** P2.11
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Performance-sensitive capabilities must receive the applicable progressive test classes: smoke, normal load, stress, spike, breakpoint/limit discovery, soak, and relevant failure/recovery pressure testing. Not every capability requires every class, but exclusions must be justified by workload semantics.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-022 — Layered performance-test cadence
- **Grill source:** P2.12
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Use layered cadence: cheap deterministic performance checks in normal CI; smoke/small-load tests frequently; workload-level load/stress tests during affected Feature Packs; major spike/breakpoint/soak tests during Architectural Proof, hardening, and release gates where applicable.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-023 — Performance-path observability
- **Grill source:** P2.13
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Important performance paths require sufficient structured metrics/traces to identify request/action latency, database/query and pool/queue time, async queue behaviour, external-provider latency, relevant LiveView execution, backlog, errors, and other material bottleneck dimensions.
- **Primary downstream workstreams:** AR-002, AR-005, AR-008, AR-009

### ARQ-PERF-024 — Error budgets versus hard invariants
- **Grill source:** P2.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Requirement:** Availability, latency, and freshness SLOs may use error budgets where appropriate. Correctness invariants such as zero confirmed overselling or zero duplicate entitlement grants are not consumable error budgets and retain zero tolerated committed violation.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

---

## 3.3 Round P3 — Concurrency, Race Conditions & Authoritative Invariants

### ARQ-PERF-025 — Durable enforcement of critical invariants
- **Grill source:** P3.1
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Critical durable invariants must remain correct when multiple processes/nodes race. Where an invariant can be expressed at the durable data layer, durable enforcement must complement application-level validation rather than relying only on prior reads or cooperative application timing.
- **Primary downstream workstreams:** AR-003, AR-005, AR-009

### ARQ-PERF-026 — Idempotent important external mutations
- **Grill source:** P3.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Important externally initiated mutations must be designed for idempotency so legitimate retries, double submissions, connectivity retries, and equivalent repeated requests cannot create duplicate committed business effects.
- **Primary downstream workstreams:** AR-004, AR-005

### ARQ-PERF-027 — Business-scoped idempotency semantics
- **Grill source:** P3.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_DOMAIN_DOSSIER
- **Requirement:** Idempotency must be scoped to the intended business operation/actor/context with a defined lifecycle and deterministic replay behaviour. Exact key format/retention is deferred to architecture/domain implementation planning.
- **Primary downstream workstreams:** AR-004, AR-005

### ARQ-PERF-028 — Duplicate payment-provider delivery is normal
- **Grill source:** P3.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Duplicate equivalent payment-provider events must be safely recognised/reconciled. Only one valid business transition/effect may occur regardless of duplicate webhook delivery.
- **Primary downstream workstreams:** AR-005, AR-006

### ARQ-PERF-029 — Explicit pending/unknown payment state
- **Grill source:** P3.5
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Ambiguous provider outcomes must enter an explicit pending/unknown state and reconcile authoritative evidence before irreversible successful outcomes are granted. A timeout proves neither success nor failure.
- **Primary downstream workstreams:** AR-005, AR-006

### ARQ-PERF-030 — At-most-one valid entitlement grant
- **Grill source:** P3.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Multiple legitimate processing paths may request the same entitlement transition, but the authoritative model must guarantee at most one valid entitlement grant for the applicable entitlement identity.
- **Primary downstream workstreams:** AR-003, AR-005

### ARQ-PERF-031 — Atomic scarce-inventory reservation/confirmation
- **Grill source:** P3.7
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Scarce inventory/capacity requires an atomic authoritative reservation/confirmation protocol such that competing requests cannot produce more confirmed allocations than available capacity. The mechanism remains an architecture/domain decision.
- **Primary downstream workstreams:** AR-003, AR-005, AR-009

### ARQ-PERF-032 — Concurrency control selected by invariant
- **Grill source:** P3.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Do not mandate optimistic locking universally. Select the concurrency mechanism according to the invariant and access pattern, using appropriate combinations of atomic mutation, durable uniqueness, optimistic version checks, row locks, stronger transaction isolation, reservation protocols, or other justified mechanisms.
- **Primary downstream workstreams:** AR-003, AR-005

### ARQ-PERF-033 — Risk-sensitive stale edit/conflict handling
- **Grill source:** P3.9
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_DOMAIN_DOSSIER
- **Requirement:** Where silent overwrite could cause meaningful information loss, stale edits/conflicts must be detected and explicitly resolved or retried. Trivial/non-conflicting data may use domain-appropriate merge or last-write policy. Health/safety-sensitive data should receive stronger conflict protection than cosmetic preferences.
- **Primary downstream workstreams:** AR-004, AR-005

### ARQ-PERF-034 — No lost updates in concurrent arithmetic
- **Grill source:** P3.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Where concurrent arithmetic or counter mutation matters, perform the mutation atomically at the authoritative layer rather than relying on unsafe read-modify-write timing.
- **Primary downstream workstreams:** AR-003, AR-005

### ARQ-PERF-035 — Bounded safe concurrency retries
- **Grill source:** P3.11
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Retryable concurrency failures may be retried only with bounded, idempotent, safe, and observable behaviour. If the retry budget is exhausted, surface an explicit recoverable failure rather than hiding uncertainty or retrying indefinitely.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-036 — Deadlock minimisation and recovery
- **Grill source:** P3.12
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Design consistent lock ordering and short transactions to minimise deadlocks; detect/observe deadlocks and treat them as retryable failures where safe rather than assuming they can never occur.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008

### ARQ-PERF-037 — Short bounded authoritative transactions
- **Grill source:** P3.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Requirement:** Keep authoritative database transactions as short and bounded as practical. Avoid holding locks while waiting on slow external systems unless architecture proves the behaviour unavoidable and safe.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-009

### ARQ-PERF-038 — Durable truth before non-transactional consequences
- **Grill source:** P3.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Durable business truth must commit before non-transactional external consequences are treated as authoritative. Required consequences need a durable mechanism so they cannot be silently lost or duplicated across commit boundaries.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008

### ARQ-PERF-039 — PubSub is observation, not durable truth
- **Grill source:** P3.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** PubSub communicates observations/coordination that something changed; it is not authoritative durable business truth. Correctness-sensitive consumers must ultimately derive truth from approved authoritative state or a durable event/consequence mechanism.
- **Primary downstream workstreams:** AR-002, AR-005, AR-008

### ARQ-PERF-040 — Crash-recoverable operation state
- **Grill source:** P3.16
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** After process/node crash, retry, or restart, critical workflows must be able to determine from durable evidence whether an operation committed, did not commit, or remains legitimately unresolved, and reconcile safely from that state.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008

### ARQ-PERF-041 — Overarching concurrency doctrine
- **Grill source:** P3.17
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Every critical invariant must remain correct under duplicate, simultaneous, reordered, retried, and partially failed execution across multiple processes and nodes.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-008, AR-009

---

## 3.4 Round P4 — State Authority, Caching, ETS, Redis, GenServers & `:persistent_term`

### ARQ-PERF-042 — PostgreSQL default durable authority
- **Grill source:** P4.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** PostgreSQL is the default durable authority for durable business state. Any alternative authority requires explicit architectural justification and a defined correctness, lifecycle, reconciliation, crash/recovery, and multi-node contract.
- **Primary downstream workstreams:** AR-003, AR-005

### ARQ-PERF-043 — Cache only with a justified workload and safe freshness model
- **Grill source:** P4.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Requirement:** Introduce caching when a known access pattern, benchmark, or scalability requirement demonstrates meaningful benefit and the cached representation has an explicit safe staleness/invalidation model. Design for future cacheability where sensible without preloading the architecture with unnecessary caches.
- **Primary downstream workstreams:** AR-003, AR-009

### ARQ-PERF-044 — Ordinary cache data must be rebuildable
- **Grill source:** P4.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Ordinary cached data must be derivable/rebuildable from authoritative state and safe to lose without corrupting business truth.
- **Primary downstream workstreams:** AR-003, AR-008

### ARQ-PERF-045 — Invalidation/versioning plus bounded TTL
- **Grill source:** P4.4
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_DOMAIN_DOSSIER
- **Requirement:** Cache freshness should use a domain-appropriate combination of explicit invalidation/versioning and bounded TTL where useful. TTL may not be the sole correctness mechanism where stale data creates material safety, security, entitlement, payment, or capacity risk.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007

### ARQ-PERF-046 — Immediate invalidation/bypass for material revocation
- **Grill source:** P4.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Material safety/security/access/entitlement revocation or withdrawal requires an explicit immediate invalidation or authoritative bypass path. Ordinary TTL is at most a secondary safety mechanism.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007

### ARQ-PERF-047 — ETS is node-local acceleration, not distributed durable truth
- **Grill source:** P4.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** ETS may be used as extremely fast node-local acceleration/lookup state where justified. Unless a stronger explicit contract exists, ETS contents are local to one BEAM node and must be reconstructable; ETS must not silently become distributed or durable business authority.
- **Primary downstream workstreams:** AR-003, AR-009

### ARQ-PERF-048 — Do not lock Cachex/raw ETS prematurely
- **Grill source:** P4.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** DEFERRED_TO_ARCHITECTURE
- **Requirement:** Lock the required node-local caching semantics first. Choose raw ETS, Cachex, or another abstraction later according to the required TTL, eviction, observability, concurrency, and operational behaviour.
- **Primary downstream workstreams:** AR-003

### ARQ-PERF-049 — Redis only for justified distributed/velocity requirements
- **Grill source:** P4.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Requirement:** Redis is justified where the platform needs distributed acceleration, high-velocity temporary coordination, counters/rate limits, or another explicit cross-node access pattern that PostgreSQL and/or node-local state do not satisfy efficiently enough. Redis is not mandatory for every domain.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-050 — Separate cache semantics from correctness-sensitive coordination semantics
- **Grill source:** P4.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Freely evictable cache data and correctness-sensitive temporary coordination state must have explicit and potentially isolated memory, eviction, persistence, recovery, and failure policies. They must not share semantics merely because both use Redis.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008

### ARQ-PERF-051 — Explicit Redis failure mode per use
- **Grill source:** P4.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Every Redis-backed capability must declare its failure mode: safe authoritative fallback where possible, deliberate degraded/queued behaviour where appropriate, or fail-closed behaviour when Redis participates in a correctness-sensitive temporary protocol. No implicit fallback may invent truth.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008

### ARQ-PERF-052 — Eviction is acceptable only for genuine caches
- **Grill source:** P4.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** For genuine rebuildable cache data, appropriate eviction under memory pressure is acceptable. Memory limits and eviction policy must fit the access pattern and be observable. If losing a value is catastrophic, it must not be treated as an ordinary disposable cache without a stronger contract.
- **Primary downstream workstreams:** AR-003, AR-008

### ARQ-PERF-053 — GenServers only for genuine process ownership/behaviour
- **Grill source:** P4.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Requirement:** Use GenServers where the problem genuinely benefits from process lifecycle, message handling, coordination, serialised ownership, or stateful behaviour. Do not introduce a GenServer merely as an in-memory map or universal hot-path wrapper.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-009

### ARQ-PERF-054 — Process ownership must scale beyond one mailbox
- **Grill source:** P4.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Where process ownership is justified for a high-scale workload, the ownership model must be partitionable/shardable or otherwise prove that a single process/mailbox will not become a systemic bottleneck.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-009

### ARQ-PERF-055 — `:persistent_term` only for read-heavy, rarely-changing VM-wide values
- **Grill source:** P4.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Requirement:** `:persistent_term` may be used only for very frequently read VM-wide values that are never or very infrequently updated, where its specialised update cost is understood and justified. It is not a general ETS replacement and should not casually hold frequently changing pricing, eligibility, permissions, health rules, or similar governed runtime state.
- **Primary downstream workstreams:** AR-003, AR-009

### ARQ-PERF-056 — Version-aware cache identity
- **Grill source:** P4.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / DEFERRED_TO_DOMAIN_DOSSIER
- **Requirement:** Where practical, derived-cache identity should incorporate authoritative version/dependency identity so new governed source versions naturally produce distinct cached representations and stale cross-version confusion is reduced.
- **Primary downstream workstreams:** AR-003, AR-006

### ARQ-PERF-057 — Explicit anti-stampede strategy
- **Grill source:** P4.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** High-fan-out cached values must have an appropriate anti-stampede strategy such as request coalescing/single-flight regeneration, jittered expiry, deliberate prewarming, stale-while-revalidate where safe, or another bounded regeneration mechanism. A single expiry must not create an uncontrolled database stampede.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-058 — TTL derived from domain semantics
- **Grill source:** P4.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** DEFERRED_TO_DOMAIN_DOSSIER / MANDATORY_REQUIREMENT
- **Requirement:** TTL is derived from data volatility, staleness tolerance, regeneration cost, invalidation reliability, and load pattern. No universal TTL applies to all caches, and some versioned/explicitly-invalidated representations may not need a conventional TTL.
- **Primary downstream workstreams:** AR-003

### ARQ-PERF-059 — Local-cache consistency contract in multi-node operation
- **Grill source:** P4.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Every material node-local cache must define its stale-data envelope and refresh/invalidation/version strategy. Correctness must remain safe if another node temporarily has a different local cached representation.
- **Primary downstream workstreams:** AR-003, AR-005, AR-009

### ARQ-PERF-060 — PubSub may accelerate invalidation but cannot be the sole correctness guarantee
- **Grill source:** P4.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** PubSub may accelerate cache invalidation/refresh notifications, but correctness cannot depend solely on every subscriber receiving every transient broadcast. Versioning, authoritative reads, or another reconciliation mechanism must protect material correctness.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005

### ARQ-PERF-061 — Correctness with empty caches
- **Grill source:** P4.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / RELEASE_GATE_INPUT
- **Requirement:** The platform must remain correct with empty caches. Startup/recovery must avoid uncontrolled simultaneous regeneration, and important cache warming may be deliberate only where evidence justifies it.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-062 — Cache observability
- **Grill source:** P4.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Every material cache requires enough observability to understand hit/miss behaviour, load/regeneration latency, expiry/eviction where applicable, errors/fallback behaviour, and whether the cache materially improves the targeted workload.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-063 — Overarching acceleration doctrine
- **Grill source:** P4.22
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Requirement:** Authoritative state first; efficient authoritative queries second; derived/read models and acceleration third. Add acceleration only where justified, make its consistency/failure contract explicit, and ensure losing an acceleration layer does not silently corrupt durable truth.
- **Preferred optimisation order:**
  1. sound data model;
  2. correct authority and transaction boundaries;
  3. appropriate algorithms;
  4. efficient queries;
  5. appropriate indexes;
  6. bounded work;
  7. pagination/batching/streaming where appropriate;
  8. derived read models where justified;
  9. caching / ETS / Redis where justified;
  10. specialised process coordination where justified.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-008, AR-009


## 3.5 Round P5 — PostgreSQL, Queries, Indexes, Connection Pools & Database Scaling

### ARQ-PERF-064 — Optimise authoritative database access before secondary acceleration
- **Grill source:** P5.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Requirement:** First make authoritative database access intrinsically efficient through sound schema design, bounded query shapes, appropriate indexes, short transactions, and sensible connection use. Secondary acceleration such as caches or Redis must not be used to conceal avoidable PostgreSQL inefficiency.
- **Primary downstream workstreams:** AR-003, AR-005, AR-009

### ARQ-PERF-065 — Avoidable N+1 behaviour is performance debt
- **Grill source:** P5.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Avoidable N+1 query behaviour on known application paths must be treated as performance debt and eliminated in the slice that introduces or materially changes the path rather than deferred until production traffic exposes it.
- **Primary downstream workstreams:** AR-002, AR-003, AR-009

### ARQ-PERF-066 — Potentially growing interactive collections must be bounded
- **Grill source:** P5.3
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Every potentially growing interactive collection must have an explicit bound, pagination strategy, aggregate, stream, or other controlled retrieval shape. Unbounded database-to-BEAM materialisation is not acceptable merely because current tables are small.
- **Primary downstream workstreams:** AR-002, AR-003, AR-009

### ARQ-PERF-067 — Indexes derive from constraints and real access patterns
- **Grill source:** P5.4
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_DOMAIN_DOSSIER
- **Requirement:** Indexes must be derived from authoritative constraints, filters, joins, ordering, and critical access patterns, then validated against representative query plans. The project must neither index every column nor rely only on primary-key indexes.
- **Primary downstream workstreams:** AR-003, AR-009

### ARQ-PERF-068 — Specialised indexes are allowed when justified
- **Grill source:** P5.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / DEFERRED_TO_DOMAIN_DOSSIER
- **Requirement:** Multicolumn, partial, expression, covering/index-only, and other specialised index designs may be used where actual query or invariant patterns justify them. They must not be introduced speculatively as blanket defaults.
- **Primary downstream workstreams:** AR-003, AR-009

### ARQ-PERF-069 — Index lifecycle and cost must be observable
- **Grill source:** P5.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Index usage and operational cost must be measured over time. Redundant or genuinely unused non-constraint indexes may be removed when evidence justifies it, while indexes that enforce integrity constraints remain governed by correctness requirements rather than usage frequency alone.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-070 — Critical and suspicious queries require plan evidence
- **Grill source:** P5.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Critical, slow, or suspicious queries must be inspected with PostgreSQL query-plan evidence such as `EXPLAIN` / `EXPLAIN ANALYZE` where appropriate, using representative data cardinality and distribution rather than relying only on small local fixtures or ORM-level timing.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-071 — Pagination must match access depth and ordering semantics
- **Grill source:** P5.8
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_DOMAIN_DOSSIER
- **Requirement:** Paginated queries require deterministic ordering. Offset pagination is acceptable for bounded/shallow use cases; cursor/keyset-style pagination should be preferred where deep or high-volume traversal would make large offsets inefficient or unstable.
- **Primary downstream workstreams:** AR-002, AR-003, AR-009

### ARQ-PERF-072 — Large data traversal uses bounded batches or streams
- **Grill source:** P5.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Large exports, transformations, and processing jobs must traverse data in bounded batches or streams where semantics permit rather than loading complete datasets into one BEAM process.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-073 — Database connections are a system-wide capacity budget
- **Grill source:** P5.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Database pool sizing must be treated as a system-wide capacity budget based on PostgreSQL capacity, application-node count, pool count, workload characteristics, and measured queue pressure. One connection per user and arbitrarily large per-node pools are prohibited design assumptions.
- **Primary downstream workstreams:** AR-001, AR-003, AR-008, AR-009

### ARQ-PERF-074 — Pool saturation requires bounded queueing and backpressure
- **Grill source:** P5.11
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Database-pool saturation must use bounded queueing/timeouts/backpressure, be observable, and prevent one workload from silently exhausting all database capacity. Unlimited waiting and unlimited emergency connection growth are not acceptable.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-075 — Preserve transaction-pooling compatibility where practical
- **Grill source:** P5.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / EVIDENCE_GATED
- **Requirement:** Application/database usage should remain compatible with transaction-pooling connection proxies such as PgBouncer where practical, avoiding unnecessary dependence on session-local PostgreSQL semantics that would force redesign later. PgBouncer itself is introduced when production/multi-node connection pressure justifies it.
- **Primary downstream workstreams:** AR-001, AR-003, AR-008, AR-009

### ARQ-PERF-076 — Read replicas are for explicitly stale-tolerant workloads
- **Grill source:** P5.13
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / EVIDENCE_GATED
- **Requirement:** Read replicas may serve explicitly stale-tolerant, read-heavy workloads such as suitable analytics/reporting when justified. Correctness-sensitive read-after-write paths must use an authority path that provides the required consistency; replicas must never be assumed perfectly current.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-077 — Expensive analytics must be isolated from critical OLTP work
- **Grill source:** P5.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Expensive stale-tolerant analytics/reporting work must be isolated from critical transactional workloads using justified derived models, materialised views, replicas, caches, or other approved architecture. Large peak-time scans against the primary OLTP path are prohibited.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-078 — Materialised views/read models serve expensive repeatable stale-tolerant reads
- **Grill source:** P5.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Requirement:** Materialised views or other derived read models may be used for expensive, repeatable, stale-tolerant aggregation/reporting where precomputation provides meaningful benefit. They must not replace transactional authority and require explicit refresh/freshness semantics.
- **Primary downstream workstreams:** AR-003, AR-005, AR-009

### ARQ-PERF-079 — Partitioning is planned for but not imposed before evidence
- **Grill source:** P5.16
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Requirement:** Domains expected to become genuinely very large should remain compatible with future partitioning, but table partitioning is implemented only where expected volume, retention, maintenance, or query patterns justify its cost and complexity.
- **Primary downstream workstreams:** AR-003, AR-009

### ARQ-PERF-080 — Preserve sound authoritative structure; denormalise projections deliberately
- **Grill source:** P5.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Durable authoritative business truth should remain structurally sound and sufficiently normalised to preserve integrity. Denormalised projections/read models may be introduced for concrete read workloads only with explicit derivation, update/rebuild, freshness, and failure semantics.
- **Primary downstream workstreams:** AR-003, AR-005, AR-009

### ARQ-PERF-081 — Vacuum, statistics and planner health are first-class operations
- **Grill source:** P5.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** PostgreSQL routine maintenance and planner statistics are first-class operational performance requirements. Autovacuum should remain enabled and be observed/tuned according to workload; statistics freshness and table/index maintenance must be part of database health monitoring.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-082 — Production schema/index changes require lock/runtime safety planning
- **Grill source:** P5.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Production migrations affecting large or hot tables must be designed and tested for lock duration, runtime, failure/rollback behaviour, and deployment impact. Online/concurrent PostgreSQL techniques should be used where supported and appropriate rather than accepting avoidable blocking downtime.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-083 — Database observability must expose contention and capacity
- **Grill source:** P5.20
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Database observability must cover connection/pool queueing, query latency, slow/top queries, execution statistics, table/index usage, locks/contention, replication lag where relevant, vacuum/analyze health, storage/resource pressure, and other evidence needed to distinguish query, lock, pool, replica, and resource bottlenecks.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-084 — Interactive database operations require bounded timeouts
- **Grill source:** P5.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_ARCHITECTURE
- **Requirement:** Interactive database operations require bounded, workload-appropriate timeouts. Genuinely long-running operations belong in explicitly controlled background/reporting paths rather than consuming interactive database resources indefinitely. Exact timeout classes are deferred to architecture/action-level planning.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009

### ARQ-PERF-085 — Performance evidence uses representative cardinality and distribution
- **Grill source:** P5.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Critical query/load tests must include representative data cardinalities and distributions because planner choices and resource behaviour can change materially as data grows. Tiny fixture databases alone are insufficient proof for scale-sensitive paths.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009

### ARQ-PERF-086 — Database scaling proceeds from efficient authority to justified distribution
- **Grill source:** P5.23
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Database scaling proceeds by first optimising authoritative schema, query, index, transaction, maintenance, and pool behaviour; then introducing justified read models, replicas, partitioning, or related measures; and moving to more distributed write topology only when proven workload requires it. Redis or sharding must not be used to bypass avoidable primary-database inefficiency.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-008, AR-009

---

---

## 3.6 Round P6 — Async Work, Queues, Backpressure, Scheduling & Worker Saturation

### ARQ-PERF-087 — Durable intent for required background work
- **Grill source:** P6.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** If business-required work must survive request termination, application restart, or node loss, the intent to perform that work must itself become durable. Required consequences may not rely on unsupervised or ephemeral fire-and-forget execution.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-088 — Durable async capability first; tool selection later
- **Grill source:** P6.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** DEFERRED_TO_ARCHITECTURE
- **Requirement:** Architecture must provide a durable, transactional, observable background-job mechanism. Oban is a strong architectural candidate, but AR-000 does not make a package selection before AR-005 evaluates the required semantics and operational model.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-089 — Queue isolation by workload characteristics
- **Grill source:** P6.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Workloads with materially different criticality, resource profiles, latency/freshness SLOs, failure behaviour, or downstream dependencies must be isolatable into separate queues or capacity pools so one workload cannot silently starve unrelated work.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-090 — Queue priority is not a substitute for isolation
- **Grill source:** P6.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Priorities may order work within an appropriate queue, but priority alone must not substitute for resource/failure isolation between fundamentally different workloads.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-091 — Worker concurrency derived from bottlenecks
- **Grill source:** P6.5
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Worker concurrency must be sized from the limiting downstream resource envelope, including PostgreSQL connections, external-provider limits, CPU, RAM, I/O, contention, and workload behaviour—not merely from the number of BEAM schedulers or processes available.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-092 — Explicit backlog/backpressure control
- **Grill source:** P6.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Durable queues must have explicit backlog SLIs/limits and use backpressure, admission control, coalescing, pausing, throttling, or deliberate degradation before work accumulation becomes uncontrolled or threatens authoritative OLTP capacity.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-093 — Bounded backoff with jitter for transient failures
- **Grill source:** P6.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Transient/retryable failures must use bounded retry with error-appropriate backoff and jitter so simultaneous failures do not form synchronized retry storms.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-094 — Error-class-aware async failure handling
- **Grill source:** P6.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Async execution must distinguish at minimum transient/retryable failure, provider rate-limit/unavailability, permanent invalid input/business state, superseded/cancelled work, and unexpected system defects. These classes may not share one blind retry policy.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008

### ARQ-PERF-095 — Coordinated response to prolonged dependency outage
- **Grill source:** P6.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Shared provider/dependency outages must cause coordinated slowdown, snoozing, pausing, circuit/degraded behaviour, or equivalent governance so independent workers do not hammer a failing dependency or create a secondary database storm.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008

### ARQ-PERF-096 — Exhausted retries do not erase business obligations
- **Grill source:** P6.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Critical work must never disappear silently after retry exhaustion. Exhausted execution must transition into an explicit unresolved/quarantined/discarded operational state with alerting and controlled reconciliation/replay where safe. Retry exhaustion must not imply business success or that the obligation ceased to exist.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-097 — Assume re-execution, not exactly-once worker execution
- **Grill source:** P6.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Architecture must not depend on exactly-once worker-process execution. Worker effects must tolerate re-execution through idempotency, durable invariants, and reconciliation.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-098 — Queue uniqueness does not replace business idempotency
- **Grill source:** P6.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Queue/job uniqueness may reduce redundant enqueueing but must not replace worker-side business idempotency where repeated execution could create harmful duplicate effects.
- **Primary downstream workstreams:** AR-005

### ARQ-PERF-099 — Mandatory consequences require atomic durable intent
- **Grill source:** P6.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Where an async consequence is mandatory, its durable execution intent must be established atomically with the originating authoritative transaction or through an equivalently robust durable outbox/commit-bridge pattern.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-100 — Bounded large fan-out
- **Grill source:** P6.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Large fan-out must be implemented as a deliberately bounded pipeline with controlled production/batching, bounded consumer concurrency, and measurable backlog rather than synchronous per-recipient spawning or unbounded task creation.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-101 — Business-effective time differs from worker execution time
- **Grill source:** P6.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Scheduled business-effective time and actual background execution time are distinct. Authoritative product logic must satisfy the promised effective time, while scheduled consequences execute within an explicit freshness/SLO window unless exact execution timing is a genuine requirement.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-102 — Cluster-safe periodic issuance
- **Grill source:** P6.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Periodic/cron work in a multi-node deployment must have single logical issuance or equivalent deduplication so additional nodes do not multiply scheduled business work.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-103 — Revalidate queued work against current authority
- **Grill source:** P6.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Queued work must revalidate material current preconditions at execution time where newer authoritative state can invalidate, cancel, supersede, or render the original intent a safe no-op. Historic enqueueing is not permission to violate current authority.
- **Primary downstream workstreams:** AR-004, AR-005, AR-007

### ARQ-PERF-104 — Minimise sensitive data in durable queue payloads
- **Grill source:** P6.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Prefer stable identifiers and minimal routing metadata in durable job payloads, re-reading authorised current state where appropriate. Sensitive, personal, clinical, or health data placed in durable queue storage requires explicit privacy, encryption, retention, deletion, and access rules.
- **Primary downstream workstreams:** AR-004, AR-005, AR-007

### ARQ-PERF-105 — Graceful worker shutdown and orphan recovery
- **Grill source:** P6.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Deployment/shutdown must stop fetching new work, allow bounded graceful completion, and ensure unfinished/orphaned jobs remain discoverable and recoverable after restart. Running work may not be marked complete merely to permit deployment.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-106 — Worker topology must remain separable
- **Grill source:** P6.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Architecture must permit heavy/background queue execution to be separated onto worker-focused nodes without changing domain/application semantics when CPU, RAM, I/O, reliability, or workload evidence justifies separation.
- **Primary downstream workstreams:** AR-001, AR-005, AR-008, AR-009

### ARQ-PERF-107 — Queue observability
- **Grill source:** P6.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Material queues must expose enough observability to understand queue depth, oldest-job/wait age, execution duration, throughput, success/failure/retry/discard/cancel states, memory/resource behaviour, and relevant downstream dependency saturation.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-108 — Queue freshness/completion SLOs
- **Grill source:** P6.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** PERFORMANCE_TARGET / RELEASE_GATE_INPUT
- **Requirement:** Define workload-specific queue wait, completion, and freshness SLOs where applicable. These SLOs may use error budgets where appropriate, while correctness obligations remain hard invariants.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-109 — Poison-job quarantine and controlled replay
- **Grill source:** P6.23
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Repeatedly failing jobs that exhaust approved retry policy must move into an explicit inspectable failed/discarded/quarantined operational state, retain enough diagnostic evidence, alert according to criticality, and support controlled replay where safe.
- **Primary downstream workstreams:** AR-005, AR-008

### ARQ-PERF-110 — Low-value backlog may not starve critical work
- **Grill source:** P6.24
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Low-value, bulk, analytics, or convenience work must be throttleable, pausable, deferred, or shed before it starves higher-criticality queues or threatens OLTP capacity.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-111 — Async work shares the PostgreSQL resource budget
- **Grill source:** P6.25
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Worker concurrency and job query patterns must be included in the same system-wide PostgreSQL connection/query/load budget as interactive traffic. A PostgreSQL-backed job system does not receive unlimited database capacity merely because it is asynchronous.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-112 — System-level queue pressure testing
- **Grill source:** P6.26
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Test worker correctness individually and queue/system behaviour under burst production, sustained backlog, dependency slowdown/outage, retries, node restart, deployment shutdown, recovery, and other relevant failure/load envelopes.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009

### ARQ-PERF-113 — Overarching asynchronous-work doctrine
- **Grill source:** P6.27
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Requirement:** Durable async work is a controlled continuation of business intent: required consequences are enqueued durably, processed with bounded and isolated capacity, assumed to be retryable/re-executable, protected by idempotency and current-authority checks, observable under backlog/failure, and prevented from starving or corrupting authoritative operations.
- **Primary downstream workstreams:** AR-005, AR-008, AR-009


---

## 3.7 Round P7 — Realtime, PubSub, LiveView, WebSockets & Fan-out

### ARQ-PERF-114 — Realtime is projection/interaction, not durable authority
- **Grill source:** P7.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Realtime mechanisms primarily distribute observations, projections, and user-interface updates of authoritative state. LiveView, WebSocket, process, Presence, or PubSub state must not silently become durable business authority.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005

### ARQ-PERF-115 — Realtime is requirement-driven, not universal
- **Grill source:** P7.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Requirement:** Use realtime where freshness materially improves product behaviour or removes harmful polling. Ordinary data that does not require immediate updates may use normal request/navigation semantics. Realtime subscriptions and broadcasts are not mandatory merely because Phoenix supports them well.
- **Primary downstream workstreams:** AR-002, AR-005, AR-009

### ARQ-PERF-116 — Reconstructable UI after disconnect/reconnect
- **Grill source:** P7.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** LiveView/WebSocket UI state must be reconstructable after disconnect, remount, process loss, or node loss from durable authority or explicitly safe reconstructable state. Correctness may not depend on the previous process still existing.
- **Primary downstream workstreams:** AR-002, AR-003, AR-008, AR-009

### ARQ-PERF-117 — Reconnect/remount lifecycle must be repeat-safe
- **Grill source:** P7.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Reconnect, remount, and subscription setup must be safe to repeat and must not accidentally recreate durable business effects. UI/process lifecycle setup must remain distinct from one-time authoritative mutations.
- **Primary downstream workstreams:** AR-002, AR-005

### ARQ-PERF-118 — Connectivity uncertainty must be visible where material
- **Grill source:** P7.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Where connectivity materially affects correctness or freshness, the UI must clearly indicate disconnected/reconnecting or equivalent degraded state and must not imply that unconfirmed server actions succeeded.
- **Primary downstream workstreams:** AR-002, AR-005, AR-008

### ARQ-PERF-119 — PubSub topics scoped to sensible audience/business boundaries
- **Grill source:** P7.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / DEFERRED_TO_ARCHITECTURE
- **Requirement:** PubSub topics must be scoped to the smallest sensible business/audience boundary—such as actor, resource, cohort, event, tenant, or other justified scope—to reduce unnecessary fan-out and exposure. Exact topic naming is deferred to architecture/domain design.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005, AR-009

### ARQ-PERF-120 — Topic knowledge is not authorization
- **Grill source:** P7.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Topic names and routing information are not authorization boundaries. Subscription/connect access and all authoritative actions must remain explicitly authorised; obscurity of a topic identifier must never grant access.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005

### ARQ-PERF-121 — Minimise realtime payloads
- **Grill source:** P7.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Realtime payloads should contain the minimum information required for the realtime effect—often identifiers, versions/change types, or safe projections—rather than indiscriminately broadcasting large or sensitive records. Payload design must account for privacy, serialization, bandwidth, memory, fan-out, and staleness risk.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005, AR-009

### ARQ-PERF-122 — Presence is ephemeral connection truth only
- **Grill source:** P7.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Presence may represent ephemeral connection/process facts such as “currently online,” but must not become durable authentication, attendance, entitlement, consent, or other business truth.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005

### ARQ-PERF-123 — Bounded per-connection LiveView state
- **Grill source:** P7.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Keep per-connection state bounded. Large or growing collections must use suitable paging, streaming, keyed/efficient rendering, or other bounded mechanisms rather than retaining unbounded lists in every connected process.
- **Primary downstream workstreams:** AR-002, AR-009

### ARQ-PERF-124 — Control state/work per LiveView rather than rejecting process-per-connection
- **Grill source:** P7.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** The process-per-connection model is acceptable, but architecture must control per-connection state, subscription count, render work, mailbox pressure, and fan-out so lightweight processes do not become heavyweight sessions at scale.
- **Primary downstream workstreams:** AR-002, AR-008, AR-009

### ARQ-PERF-125 — Slow clients may not create unbounded server backlog
- **Grill source:** P7.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Realtime design must prevent slow clients, stale sockets, or large process mailboxes from creating unbounded server memory/work. Expendable UI updates may be coalesced, refreshed, or reconstructed from current state rather than buffered indefinitely.
- **Primary downstream workstreams:** AR-002, AR-008, AR-009

### ARQ-PERF-126 — Coalesce obsolete intermediate UI observations
- **Grill source:** P7.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Where intermediate realtime observations have no business/audit value, the platform may coalesce or refresh toward the current authoritative projection instead of forcing every client to process every obsolete intermediate visual state.
- **Primary downstream workstreams:** AR-002, AR-005, AR-009

### ARQ-PERF-127 — Business correctness may not depend on global PubSub ordering
- **Grill source:** P7.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Realtime consumers must tolerate appropriate delay, missing observations, duplication, and reordering. Where ordering materially matters, use authoritative versions/sequences or re-read current state rather than relying on global PubSub delivery order or wall-clock timing.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005

### ARQ-PERF-128 — Duplicate realtime observations may not create duplicate durable effects
- **Grill source:** P7.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Realtime observation consumers must tolerate duplicate notifications and must never create duplicate durable effects solely because the same change was observed more than once.
- **Primary downstream workstreams:** AR-002, AR-005

### ARQ-PERF-129 — Prompt live-session revocation for material access changes
- **Grill source:** P7.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Material revocation—such as logout, account disablement, consent/access withdrawal, or security action—must be capable of promptly invalidating/disconnecting affected live sessions and may not wait indefinitely for old socket/process state to disappear naturally.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005, AR-007

### ARQ-PERF-130 — Re-authorise authoritative actions at the action boundary
- **Grill source:** P7.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** Authoritative business actions invoked through LiveView/WebSocket must perform current actor/policy authorization at the action boundary. Authorization established at mount/connect time does not permanently authorise future actions.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005

### ARQ-PERF-131 — Controlled degraded behaviour when WebSockets are unavailable
- **Grill source:** P7.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Where appropriate, use supported transport/degraded behaviour when WebSockets are unavailable while preserving correctness and preventing polling storms. Genuinely realtime functions may expose degraded freshness rather than pretending realtime remains available.
- **Primary downstream workstreams:** AR-002, AR-008, AR-009

### ARQ-PERF-132 — Realtime refresh must not amplify one broadcast into uncontrolled database work
- **Grill source:** P7.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Realtime refresh paths must retrieve only the authoritative projection needed for the changed UI, coalesce/batch where appropriate, and avoid turning one broadcast into uncontrolled N×M database queries across large subscriber populations.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-009

### ARQ-PERF-133 — High-fan-out broadcasts require deliberate amplification control
- **Grill source:** P7.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** High-fan-out realtime events must be measured and deliberately designed using suitable topic scoping, coalescing, derived projections, batching, or other approved mechanisms so one logical change does not create uncontrolled cross-node CPU, network, memory, render, or database amplification.
- **Primary downstream workstreams:** AR-002, AR-005, AR-008, AR-009

### ARQ-PERF-134 — Multi-node PubSub semantics first; adapter/topology later
- **Grill source:** P7.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** DEFERRED_TO_ARCHITECTURE
- **Requirement:** Lock reliable multi-node PubSub semantics and failure behaviour as requirements first. Select the concrete PubSub topology/adapter later according to deployment architecture and measured scale rather than preselecting Redis or another backend during AR-000.
- **Primary downstream workstreams:** AR-001, AR-002, AR-005, AR-009

### ARQ-PERF-135 — Realtime observability
- **Grill source:** P7.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Realtime observability must cover relevant connection counts/churn, mount/reconnect behaviour, LiveView event/render durations, material process/mailbox pressure, subscription/fan-out behaviour, broadcast rates, payload sizes, errors, and resource impact.
- **Primary downstream workstreams:** AR-002, AR-008, AR-009

### ARQ-PERF-136 — Realtime-specific capacity and failure testing
- **Grill source:** P7.23
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Realtime capacity testing must include large concurrent connection populations plus connect/reconnect storms, subscription fan-out, broadcast bursts, slow-client conditions, node loss, rolling deploys, and recovery—not merely HTTP request throughput.
- **Primary downstream workstreams:** AR-002, AR-008, AR-009

### ARQ-PERF-137 — Node loss may interrupt freshness, not durable truth
- **Grill source:** P7.24
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** If a node hosting many LiveViews fails, clients may reconnect to surviving/replacement nodes and reconstruct UI state from authority. Node loss may temporarily affect realtime experience/freshness but must not corrupt durable business truth.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-008, AR-009

### ARQ-PERF-138 — Overarching realtime doctrine
- **Grill source:** P7.25
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Requirement:** Realtime is a bounded, observable projection/interaction layer over authoritative state: use it where product freshness warrants it; keep per-connection state and fan-out controlled; tolerate reconnect, reordering, and duplicate observations; re-authorise business actions; and ensure node/socket/PubSub failure affects freshness before it affects truth.
- **Primary downstream workstreams:** AR-001, AR-002, AR-004, AR-005, AR-008, AR-009


---

## 3.8 Round P8 — Reliability, Uptime, Failure Isolation, Deployment & Recovery

### ARQ-PERF-139 — Availability classes by business criticality
- **Grill source:** P8.1
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / PERFORMANCE_TARGET
- **Requirement:** Define measurable availability classes according to business criticality rather than one universal uptime number. Suitable capabilities may use SLOs/error budgets, while hard correctness invariants remain separately governed and are not relaxed by availability targets.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-140 — High availability without fictitious 100% promise
- **Grill source:** P8.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Design for very high availability and rapid recovery, but do not create a fictitious literal 100% availability promise. Availability objectives may have explicit error budgets where appropriate; correctness, safety, privacy, entitlement, payment and capacity invariants remain stricter.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-141 — Application-node failure containment
- **Grill source:** P8.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** In the intended scaled production topology, loss of one application node must not corrupt durable truth and should not materially remove the whole platform. Traffic and realtime clients must be able to recover through surviving or replacement capacity.
- **Primary downstream workstreams:** AR-001, AR-002, AR-008, AR-009

### ARQ-PERF-142 — Bounded supervision restart behaviour
- **Grill source:** P8.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Recoverable process failures may restart according to intentional OTP supervision policy, but repeated crash loops must escalate through supervision/operations rather than restart indefinitely and consume resources without resolution.
- **Primary downstream workstreams:** AR-001, AR-008

### ARQ-PERF-143 — Supervision boundaries follow failure dependencies
- **Grill source:** P8.5
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Structure supervision according to genuine runtime/failure dependencies so unrelated capabilities do not restart together unnecessarily, while tightly coupled components may share an appropriate failure boundary. Supervision topology must model fault containment rather than simply source-code organisation.
- **Primary downstream workstreams:** AR-001, AR-008

### ARQ-PERF-144 — Distinct startup, liveness and readiness semantics
- **Grill source:** P8.6
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Distinguish startup completion, process liveness and readiness to accept intended traffic/work, regardless of the eventual deployment/orchestration platform. A single undifferentiated health signal is insufficient for production reliability.
- **Primary downstream workstreams:** AR-001, AR-008

### ARQ-PERF-145 — Dependency outages do not automatically imply process death
- **Grill source:** P8.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Temporary external dependency failure should affect readiness or capability-specific degraded behaviour only where necessary. Liveness should represent a fault that restarting the current process/node can reasonably fix; dependency failure must not trigger destructive restart cascades by default.
- **Primary downstream workstreams:** AR-006, AR-008, AR-009

### ARQ-PERF-146 — Single fenced PostgreSQL write authority during failover
- **Grill source:** P8.8
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Requirement:** PostgreSQL failover must preserve one accepted writable authority and use fencing or equivalent protection so an old primary cannot rejoin and continue accepting conflicting writes. Split-brain writable authority is prohibited.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008

### ARQ-PERF-147 — High availability and backups are separate controls
- **Grill source:** P8.9
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Standby/failover capacity does not replace recoverable historical backup/PITR. Availability/failover and backup/recovery must be designed as distinct controls for the data classes that require them.
- **Primary downstream workstreams:** AR-007, AR-008

### ARQ-PERF-148 — Recovery objectives by state/business class
- **Grill source:** P8.10
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Define RPO and RTO by state/business class, with the strictest objectives for authoritative financial, entitlement, safety, identity and other critical durable state. Positively acknowledged durable commits must not silently disappear after ordinary application/node failure.
- **Primary downstream workstreams:** AR-003, AR-005, AR-007, AR-008

### ARQ-PERF-149 — Bounded dependency deadlines
- **Grill source:** P8.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** External/dependency calls must use workload-appropriate bounded deadlines/timeouts, and downstream work should stop or cancel where possible once the originating operation is no longer useful or valid. Infinite dependency waiting is prohibited on production paths.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008, AR-009

### ARQ-PERF-150 — Deliberate retry ownership and budgets
- **Grill source:** P8.12
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Establish explicit retry ownership and budgets across call chains so nested layers cannot multiply retries exponentially. Only eligible failures may retry, with bounded backoff/jitter and observable exhaustion behaviour.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008

### ARQ-PERF-151 — Failure isolation / bulkhead doctrine
- **Grill source:** P8.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_ARCHITECTURE
- **Requirement:** Material integrations and resource classes require failure-isolation boundaries so one saturated/failing dependency cannot consume all request, connection, worker or other shared capacity. Circuit-style controls or equivalent mechanisms may be used where justified by AR-005/AR-008.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008, AR-009

### ARQ-PERF-152 — Do not restart healthy-but-overloaded capacity as first response
- **Grill source:** P8.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Requirement:** Overload should first trigger backpressure, admission control, load shedding or deliberate degradation. Restarting otherwise healthy but overloaded capacity must not be the default response because it can redistribute load and amplify cascading failure.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-153 — Degraded modes require recurrent proof
- **Grill source:** P8.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Important degraded/load-shedding paths must be exercised often enough to prove they remain functional. Rarely used degradation code may not exist only as an untested incident theory.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-154 — Readiness only after safe mandatory startup
- **Grill source:** P8.16
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** A node may declare readiness only after mandatory initialization required for safe traffic/work has completed. Optional cache warming or other startup work must remain bounded so concurrent node starts do not stampede databases/dependencies; full cache warmth is not a correctness prerequisite.
- **Primary downstream workstreams:** AR-001, AR-003, AR-008, AR-009

### ARQ-PERF-155 — Adjacent-version coexistence during rolling deployment
- **Grill source:** P8.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Where rolling deployment is used, adjacent application versions must have an explicitly safe interoperability window across shared database schema, durable jobs/messages, distributed behaviour and other shared contracts.
- **Primary downstream workstreams:** AR-001, AR-005, AR-008

### ARQ-PERF-156 — Expand/transition/contract migration safety
- **Grill source:** P8.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Destructive/high-risk schema changes should use expand → compatible application transition → contract patterns or an equivalently safe approach so adjacent application versions can overlap without interpreting shared state incompatibly.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008

### ARQ-PERF-157 — Drain before termination
- **Grill source:** P8.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Before terminating a node for deployment/maintenance, remove or drain it from new traffic/work, allow bounded in-flight work to finish where safe, and rely on idempotent durable recovery for unfinished obligations rather than inventing completion.
- **Primary downstream workstreams:** AR-001, AR-002, AR-005, AR-008

### ARQ-PERF-158 — Every release needs rollback or explicit forward-recovery
- **Grill source:** P8.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Every production release needs an understood rollback/recovery path. Irreversible migrations or data transformations require an explicit forward-recovery plan before deployment; rollback assumptions may not depend on impossible restoration of already-destroyed state.
- **Primary downstream workstreams:** AR-007, AR-008

### ARQ-PERF-159 — Risk-based progressive/canary rollout
- **Grill source:** P8.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / RELEASE_GATE_INPUT
- **Requirement:** High-risk changes should support progressive/canary exposure when their blast radius justifies it, with defined health/performance comparison and rollback criteria. Canarying supplements rather than replaces testing and is applied proportionally to risk.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-160 — Evidence-based production capacity headroom
- **Grill source:** P8.22
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / PERFORMANCE_TARGET
- **Requirement:** Maintain evidence-based capacity headroom appropriate to workload and failure topology so expected loss of capacity or normal traffic redistribution does not immediately create cascading failure. Autoscaling does not eliminate capacity planning or headroom requirements.
- **Primary downstream workstreams:** AR-008, AR-009

### ARQ-PERF-161 — Single-primary-region initially; resilient disaster recovery boundary
- **Grill source:** P8.23
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Requirement:** South-Africa-first/single-primary-region operation is acceptable initially, but disaster-recovery and backup controls must not share every meaningful failure domain, and architecture must avoid unnecessary choices that prevent future regionalisation.
- **Primary downstream workstreams:** AR-001, AR-007, AR-008, AR-009

### ARQ-PERF-162 — Controlled failure-injection testing
- **Grill source:** P8.24
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Deliberately test expected failure modes in representative environments, including node death, dependency loss, queue backlog, Redis loss where used, database failover, slow providers, reconnect storms and recovery. Progress to controlled production game days only when the platform and operational maturity justify them.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008, AR-009

### ARQ-PERF-163 — Recovery runbooks require exercised evidence
- **Grill source:** P8.25
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Requirement:** Runbooks are required but insufficient alone. Important failover, backup restoration, reconciliation and recovery procedures must be exercised periodically and produce evidence that the procedures and restored state actually work.
- **Primary downstream workstreams:** AR-007, AR-008

### ARQ-PERF-164 — Auditable emergency controls for optional work
- **Grill source:** P8.26
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Requirement:** Approved, authorised and auditable operational controls must be capable of pausing/throttling selected low-priority queues, integrations, fan-out or optional features during incidents without weakening critical correctness. Emergency controls themselves require RBAC and audit governance.
- **Primary downstream workstreams:** AR-004, AR-005, AR-008

### ARQ-PERF-165 — Incidents feed explicit upstream amendment/re-proof
- **Grill source:** P8.27
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / GOVERNANCE_REQUIREMENT
- **Requirement:** Significant reliability incidents must feed evidence back into architecture, tests, capacity assumptions, runbooks and monitoring. If evidence contradicts an ARQ, ARC, Domain Law assumption or Feature Pack premise, STOP, classify the root cause, amend the correct upstream layer explicitly, re-prove affected flows, and only then resume execution.
- **Primary downstream workstreams:** AR-008, AR-009; governance-wide

### ARQ-PERF-166 — Overarching reliability doctrine
- **Grill source:** P8.28
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Requirement:** Reliability comes from explicit failure boundaries, durable authority, bounded retries/load, safe supervision, redundancy where justified, graceful degradation, health/readiness semantics, reversible deployment, tested failover/recovery and evidence-driven capacity. Assume components will fail; engineer failure so it is bounded, observable, recoverable and cannot silently corrupt truth.
- **Primary downstream workstreams:** AR-001, AR-003, AR-005, AR-007, AR-008, AR-009

# 4. Consolidated P1–P8 Principles

The accepted P1–P8 requirements currently establish the following architectural doctrine:

1. **Scale-ready, not scale-wasteful.** Design the core authority, concurrency, data, transaction, and multi-node model so growth does not demand fundamental redesign; scale purchased capacity progressively with evidence.
2. **Optimise fundamentals first.** Prevent known bottlenecks and performance debt from the beginning, while rejecting speculative mechanisms that add complexity without a requirement.
3. **Correctness outranks latency.** Security, privacy, clinical/safety truth, payment truth, entitlement truth, and confirmed capacity may not be weakened to preserve apparent availability or speed.
4. **Correct refusal beats false success.** Under saturation, queue, throttle, reject, or explicitly defer before accepting work that cannot safely be honoured.
5. **Evidence replaces intuition.** Use percentile SLIs, user-perceived metrics, component-level telemetry, and progressive workload/failure testing.
6. **Current good Core Web Vitals are the floor.** The project aims better than the current official “good” range, never worse as an accepted steady state.
7. **Concurrency is assumed hostile.** Critical invariants must survive duplicate, simultaneous, reordered, retried, and partially failed execution across processes and nodes.
8. **Durable invariants need durable protection.** Application checks alone are insufficient where the durable layer can enforce the invariant.
9. **Async boundaries follow semantics.** Do not make work synchronous or asynchronous solely because of a duration threshold.
10. **Acceleration is optional infrastructure, not truth.** PostgreSQL remains the default durable authority; cache/ETS/Redis/GenServer/`:persistent_term` are introduced only where their semantics justify them.
11. **Caches are disposable unless explicitly governed otherwise.** Ordinary caches must be rebuildable and safe to lose.
12. **Every acceleration mechanism carries a failure contract.** Staleness, invalidation, restart, reconstruction, multi-node behaviour, memory pressure, and dependency outage behaviour must be explicit.
13. **Performance testing is continuous and layered.** CI checks, regular load tests, workload pressure tests, Architectural Proof, hardening, and release gates all contribute evidence.
14. **Multi-node correctness is a day-one architecture requirement.** Initial single-node deployment, if used, is only a capacity/deployment choice.
15. **PostgreSQL performance is application architecture.** Query shape, indexes, transaction length, pool economics, maintenance, and planner health are designed deliberately rather than postponed as database tuning.
16. **All growing reads are bounded.** Interactive collections, exports, and large processing paths must paginate, stream, aggregate, or batch rather than materialise unbounded sets.
17. **Connection capacity is finite shared infrastructure.** Pool sizing and queue pressure must be reasoned about across all application nodes and workloads.
18. **Analytics must not compete blindly with OLTP.** Heavy stale-tolerant reporting is isolated through justified projections, materialised views, replicas, or other approved read architecture.
19. **Scale topology follows evidence.** Preserve compatibility with future PgBouncer, replicas, partitioning, and more distributed topology without imposing them before the workload justifies them.
20. **Durable async work is controlled business continuation.** Queueing must preserve durable intent, bounded capacity, idempotency, backlog observability, current-authority checks, and safe recovery.
21. **Realtime is projection, not authority.** LiveView/PubSub/Presence/socket state may optimise freshness and interaction but may not silently become durable business truth.
22. **Per-connection and fan-out cost must remain bounded.** Realtime scale depends on controlling state, subscriptions, renders, payloads, mailboxes, and amplification—not merely connection count.
23. **Disconnect/reconnect is normal operation.** UI state must reconstruct safely; remount/reconnect may never recreate one-time durable effects.
24. **Freshness may degrade before truth.** Realtime transport, node, or PubSub failure may interrupt UX freshness, but authoritative correctness remains intact.
25. **Failure is expected and contained.** Process, node, dependency and hosting failures must have explicit containment, health, recovery and escalation semantics rather than relying on restart optimism.
26. **Availability SLOs and correctness invariants are different.** Availability may use evidence-based error budgets; committed correctness violations do not become acceptable because uptime is high.
27. **High availability is not backup.** Failover preserves service continuity; backup/PITR preserves recoverability from deletion, corruption, bad migration and other historical failures.
28. **Deployments are compatibility events.** Adjacent versions, schema changes, draining, rollback/forward-recovery and progressive rollout must be designed as part of runtime reliability.
29. **Recovery must be exercised.** Degraded modes, failover, restoration, reconciliation and failure injection require repeatable evidence rather than documentation alone.
30. **Incidents may amend architecture, never silently drift it.** Production evidence routes through STOP → classification → explicit upstream amendment → affected re-proof before execution resumes.


---

# 5. Requirement Coverage Snapshot

Current AR-000-P accepted requirement count:

```text
P1  ARQ-PERF-001 ... ARQ-PERF-010   = 10
P2  ARQ-PERF-011 ... ARQ-PERF-024   = 14
P3  ARQ-PERF-025 ... ARQ-PERF-041   = 17
P4  ARQ-PERF-042 ... ARQ-PERF-063   = 22
P5  ARQ-PERF-064 ... ARQ-PERF-086   = 23
P6  ARQ-PERF-087 ... ARQ-PERF-113   = 27
P7  ARQ-PERF-114 ... ARQ-PERF-138   = 25
P8  ARQ-PERF-139 ... ARQ-PERF-166   = 28
-----------------------------------------
TOTAL                                = 166
```

Current status:

```text
P1 COMPLETE / ACCEPTED
P2 COMPLETE / ACCEPTED
P3 COMPLETE / ACCEPTED
P4 COMPLETE / ACCEPTED
P5 COMPLETE / ACCEPTED
P6 COMPLETE / ACCEPTED
P7 COMPLETE / ACCEPTED
P8 COMPLETE / ACCEPTED
AR-000-P PERFORMANCE REQUIREMENTS EXTRACTION CLOSED
ARQ-PERF-001 ... ARQ-PERF-166 LOCKED / APPEND-ONLY
AR-000-A ANALYTICS GRILL NEXT
```

---

# 6. Research / Best-Practice Basis Used During P1–P8

The recommendations were informed by the governing project requirements and primary/current technical guidance including, where relevant:

- PostgreSQL documentation — concurrency control, MVCC, transaction isolation, locking, uniqueness, `INSERT ... ON CONFLICT`
- PostgreSQL documentation — indexes, `EXPLAIN`, pagination/`LIMIT`/`OFFSET`, materialised views, partitioning, monitoring statistics, routine vacuuming, hot standby, concurrent index builds
- Ecto / Ecto SQL documentation — Repo pools, query timing/queue telemetry, query timeouts, streaming and query-plan inspection
- PgBouncer documentation — pooling modes and transaction-pooling compatibility constraints
- Oban documentation — durable jobs, queue isolation, retries/backoff, uniqueness, scheduling, shutdown/recovery and telemetry
- Elixir documentation — ETS, GenServer
- Erlang/OTP documentation — `:persistent_term`
- Phoenix / Phoenix LiveView / Phoenix PubSub / Phoenix Presence / Phoenix Socket documentation
- Ash Framework documentation — actions, transactions, optimistic locking, notifiers, atomic operations
- Redis documentation — caching, expiration, eviction and memory policies
- Google SRE guidance — SLOs, percentile latency, overload/cascading-failure handling, reliability/stress testing
- Web.dev / Google guidance — current Core Web Vitals
- Grafana k6 guidance — smoke, load, stress, spike, breakpoint and soak testing concepts
- Erlang/OTP supervision documentation — supervision strategies and bounded restart intensity
- PostgreSQL high-availability/failover/backup documentation — standby, failover authority, fencing implications, WAL/PITR recovery
- Google SRE guidance — deadlines, retry budgets, cascading failure, canary releases and capacity/failure testing
- Kubernetes documentation used only as deployment-neutral reference semantics for startup/liveness/readiness and draining concepts; no Kubernetes commitment is implied

Exact package/tool selection is not locked by this list unless a later `ARC-nnn` decision explicitly does so.

---

# 7. Open / Escalated Findings

At formal AR-000-P closure:

- no accepted P1–P8 requirement requires reopening Product Law;
- `ARQ-PERF-001` through `ARQ-PERF-166` are closed as the current Performance requirements surface and remain append-only;
- Redis, ETS, Cachex, GenServer, `:persistent_term`, replicas, table partitioning, and specific load-testing/observability packages are not universal requirements merely because they are available;
- Oban is a specific upstream Platform-Law choice for the heavy/durable async and notification scopes already named by Product Law; exact queue/worker topology remains Architecture work;
- PgBouncer transaction mode is an upstream Platform-Law requirement once the measurable production-scale gate is reached; compatibility is preserved before that gate;
- Phoenix/LiveView remain part of the locked platform stack; PubSub is the approved cross-node realtime broadcast mechanism where that capability is required, while per-domain applicability still follows the `NONE`-is-valid rule where no such behaviour is needed;
- exact concurrency mechanisms, concrete indexes, cache structures, TTLs, Redis structures, pool sizes, timeouts, replica routing, partition keys, worker names, process topology, SLO class thresholds, and deployment sizing remain downstream Architecture/Domain Dossier decisions unless explicitly locked later;
- future evidence may amend or supersede a Performance ARQ only through an explicit append-only amendment trail; the broad Performance Grill does not reopen automatically.

---

# 8. Next Planned Step

## AR-000-P — Formal Performance Grill Closure

The substantive Performance Grill rounds P1–P8 are complete. Before moving to the Analytics Grill, perform a formal closure pass that:

1. verifies every P1–P8 question has an accepted answer;
2. verifies `ARQ-PERF-001` through `ARQ-PERF-166` are contiguous and represented exactly once;
3. checks duplicate/overlapping ARQs and records intentional overlap without deleting history;
4. checks contradictions between P1–P8 requirements;
5. checks contradictions against the governing Product Law pack;
6. classifies any item that unexpectedly requires Product Law escalation;
7. verifies each ARQ has downstream AR-001–AR-009 routing;
8. identifies Architecture decisions that AR-003, AR-005, AR-008 or AR-009 must explicitly resolve;
9. confirms no technology was accidentally made mandatory without an accepted requirement;
10. records a Performance Grill closure verdict and any open gates in this append-only document.

After the closure passes, begin **AR-000-A — Analytics, Reporting, Funnels & Financial Intelligence Grill**.

The closure result must be appended to this document with the next SemVer increment; no prior requirement may be deleted or silently rewritten.

---

---

# 8A. AR-000-P Formal Performance Closure — ACCEPTED

- **Closure date:** 2026-08-16
- **Closure decision source:** Performance Closure Grill PC.1–PC.5 — all recommendations accepted
- **Closed requirement range:** `ARQ-PERF-001` through `ARQ-PERF-166`
- **Closure verdict:** **PASS WITH EXPLICIT PRECEDENCE AMENDMENTS RECORDED BELOW**

## 8A.1 Closure audit results

1. All substantive Performance Grill rounds P1–P8 are complete and accepted.
2. `ARQ-PERF-001` through `ARQ-PERF-166` are contiguous, unique and represented exactly once.
3. Intentional overlaps exist across authority, idempotency, backlog/backpressure, observability, recovery and multi-node requirements. They are reinforcing constraints at different failure boundaries, not contradictory duplicate law, and are retained.
4. No unresolved contradiction exists between the accepted Performance ARQs after applying PC.2–PC.4 below.
5. No Performance closure finding requires reopening Product Law.
6. No Product-Law escalation remains open from AR-000-P.
7. Every ARQ has downstream architecture-workstream routing; the permanent keyed trace addendum in §8B supplies the complete source/status/blocking metadata required by AR-000.
8. AR-003, AR-005, AR-008 and AR-009 carry the largest Performance disposition burden, with AR-001, AR-002, AR-004, AR-006 and AR-007 receiving the cross-cutting items routed to them.
9. Technology-lock review passes subject to the explicit precedence interpretations below.
10. The broad Performance Grill is now **CLOSED**. Future evidence may amend/supersede a requirement explicitly, but does not silently reopen or erase this closed requirement surface.

## 8A.2 AMEND-PERF-001 — ARQ-PERF-088 / Oban precedence

- **Status:** ACCEPTED AMENDMENT
- **Amends:** `ARQ-PERF-088`
- **Original entry:** retained unchanged for history.
- **Upstream authority:** `00_PLATFORM_v1.1 §21J.20`, `§21J.24`, `§21K.4`, interpreted together with `§21K.7`.

**Governing interpretation:**

Oban is already a locked Platform-Law mechanism for the heavy/durable asynchronous and notification-delivery scopes explicitly named by Product Law. AR-005 does **not** reopen whether to replace Oban for those scopes. AR-005 must instead decide/prove queue topology, concurrency, worker boundaries, priorities, scheduling, transaction integration, failure/retry behaviour, observability and related operating semantics.

`NONE` remains valid for a domain/action that genuinely requires no Oban behaviour. The generic `NONE` rule does not nullify a specific upstream mandate for an action that does require the already-locked heavy/durable async or notification mechanism.

## 8A.3 AMEND-PERF-002 — ARQ-PERF-075 / PgBouncer production-scale gate

- **Status:** ACCEPTED AMENDMENT
- **Amends:** `ARQ-PERF-075`
- **Original entry:** retained unchanged for history.
- **Upstream authority:** `00_PLATFORM_v1.1 §21K.3` and `§21K.7`.

**Governing interpretation:**

Transaction-pooling compatibility must be preserved from the beginning. PgBouncer in transaction mode becomes required once the Architecture-defined measurable **production-scale gate** is reached. AR-009 must define objective evidence/criteria for that gate. The first small paid pilot does not automatically trigger PgBouncer merely because it is technically a production environment; the requirement is tied to the scale/connection-pressure gate intended by Product Law.

## 8A.4 INTERP-PERF-001 — Generic acceleration-tool precedence

- **Status:** ACCEPTED INTERPRETATION
- **Applies to:** Redis, ETS, Cachex, GenServer, PubSub, Oban and related generic performance-tool lists.
- **Upstream authority:** `00_PLATFORM_v1.1 §21K.1–§21K.7`.

**Governing interpretation:**

The generic data-temperature and realtime lists define the approved platform toolbox/direction. Actual domain/action applicability is governed by `§21K.7`: acceleration must be earned and `NONE` is valid where the access pattern does not require a mechanism.

Specific upstream mandates remain specific exceptions and are not weakened by the generic `NONE` rule. In particular:

- Phoenix/LiveView remain part of the locked platform stack;
- Phoenix PubSub is the approved cross-node broadcast mechanism where realtime cross-node broadcasting is actually required;
- Oban is locked for the Product-Law-named heavy/durable async and notification scopes;
- PgBouncer transaction mode is required at the Architecture-defined production-scale gate;
- Redis, ETS, Cachex, GenServer and `:persistent_term` are not mandatory in every domain merely because they are approved capabilities.

## 8A.5 Performance closure routing

```text
AR-000-P PERFORMANCE REQUIREMENTS
CLOSED

ARQ-PERF-001 ... ARQ-PERF-166
        ↓
AR-001 ... AR-009 disposition / ARC decisions
        ↓
reference-flow pressure tests
        ↓
03_ARCHITECTURE review/freeze
```

The next AR-000 focused Grill is **AR-000-A — Analytics, Reporting, Funnels & Financial Intelligence**.

# 8B. Permanent ARQ-PERF Source Trace and Architecture Routing Addendum

This table implements the AR-000 traceability requirement accepted at Performance Closure PC.1. It is keyed to every currently closed Performance ARQ.

**Interpretation rules**

- `EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL` means the governing Platform Law contains the material obligation and the Grill clarified/strengthened its architecture-facing meaning.
- `DERIVED_ACCEPTED_GRILL_REQUIREMENT` means the exact detail is not stated verbatim in Product Law; it is an accepted AR-000 requirement derived from the cited performance/reliability mandate plus researched best practice. It must not later be misrepresented as an original Product-Law DEC.
- `ARQ_LOCKED / ARC_PENDING` means the requirement is closed for AR-000, but the relevant AR-001…AR-009 workstream still has to decide/prove the architecture mechanism.
- The cited sections are the exact upstream Platform-Law anchors for AR-000 traceability; the accepted Grill ID is the additional direct source for the refined/derived requirement.

| ARQ | Grill | Exact Product Law source(s) | Source classification | Architecture workstream(s) | Blocking classification | Architecture status |
|---|---|---|---|---|---|---|
| ARQ-PERF-001 | P1.1 | 00_PLATFORM_v1.1 §21K.7; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-001, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-002 | P1.2 | 00_PLATFORM_v1.1 §21L.22; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-001, AR-003, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-003 | P1.3 | 00_PLATFORM_v1.1 §21K.5; §21L.22 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-004 | P1.4 | 00_PLATFORM_v1.1 §21J.21; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-004, AR-005, AR-007, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-005 | P1.5 | 00_PLATFORM_v1.1 §21K.5; §21J.21 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-006 | P1.6 | 00_PLATFORM_v1.1 §21J.21; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-006, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-007 | P1.7 | 00_PLATFORM_v1.1 §21K.5; §21J.20 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-006, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-008 | P1.8 | 00_PLATFORM_v1.1 §21K.8; §21L.22 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-001, AR-003, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-009 | P1.9 | 00_PLATFORM_v1.1 §21L.3; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-005, AR-006, AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-010 | P1.10 | 00_PLATFORM_v1.1 §21J.21; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-011 | P2.1 | 00_PLATFORM_v1.1 §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-012 | P2.2 | 00_PLATFORM_v1.1 §21K.8; §21L.22 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-013 | P2.3 | 00_PLATFORM_v1.1 §21J.24; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-014 | P2.4 | 00_PLATFORM_v1.1 §21K.8; §21L.22 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-008, AR-009 | EVIDENCE_GATE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-015 | P2.5 | 00_PLATFORM_v1.1 §21J.24; §21K.4 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-016 | P2.6 | 00_PLATFORM_v1.1 §21J.24; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-006, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-017 | P2.7 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-018 | P2.8 | 00_PLATFORM_v1.1 §21J.21; §21L.22 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-019 | P2.9 | 00_PLATFORM_v1.1 §21K.7; §21L.22 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-003, AR-005, AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-020 | P2.10 | 00_PLATFORM_v1.1 §21L.22; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-021 | P2.11 | 00_PLATFORM_v1.1 §21L.22 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-022 | P2.12 | 00_PLATFORM_v1.1 §21L.22 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-023 | P2.13 | 00_PLATFORM_v1.1 §21J.24; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-024 | P2.14 | 00_PLATFORM_v1.1 §21K.8; §21J.21 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-025 | P3.1 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-026 | P3.2 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-004, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-027 | P3.3 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-004, AR-005 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-028 | P3.4 | 00_PLATFORM_v1.1 §21J.15; §21K.3; §21K.5 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-006 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-029 | P3.5 | 00_PLATFORM_v1.1 §21J.15; §21K.3; §21K.5 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-006 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-030 | P3.6 | 00_PLATFORM_v1.1 §21J.15; §21K.3; §21K.5 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-031 | P3.7 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-032 | P3.8 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-033 | P3.9 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-004, AR-005 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-034 | P3.10 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-035 | P3.11 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-036 | P3.12 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-037 | P3.13 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-006, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-038 | P3.14 | 00_PLATFORM_v1.1 §21J.20; §21J.21; §21J.24; §21K.4 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-006, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-039 | P3.15 | 00_PLATFORM_v1.1 §21J.20; §21J.21; §21J.24; §21K.4 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-005, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-040 | P3.16 | 00_PLATFORM_v1.1 §21J.20; §21J.21; §21J.24; §21K.4 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-041 | P3.17 | 00_PLATFORM_v1.1 §21K.3; §21K.5; §21K.8 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-003, AR-005, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-042 | P4.1 | 00_PLATFORM_v1.1 §21K.4 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-043 | P4.2 | 00_PLATFORM_v1.1 §21K.1; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-044 | P4.3 | 00_PLATFORM_v1.1 §21K.1; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-045 | P4.4 | 00_PLATFORM_v1.1 §21K.1; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-004, AR-005, AR-007 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-046 | P4.5 | 00_PLATFORM_v1.1 §21K.1; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-004, AR-005, AR-007 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-047 | P4.6 | 00_PLATFORM_v1.1 §21K.1; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-048 | P4.7 | 00_PLATFORM_v1.1 §21K.1; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-049 | P4.8 | 00_PLATFORM_v1.1 §21K.2; §21K.4; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-008, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-050 | P4.9 | 00_PLATFORM_v1.1 §21K.2; §21K.4; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-051 | P4.10 | 00_PLATFORM_v1.1 §21K.2; §21K.4; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-052 | P4.11 | 00_PLATFORM_v1.1 §21K.2; §21K.4; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-008 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-053 | P4.12 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-001, AR-003, AR-005, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-054 | P4.13 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-003, AR-005, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-055 | P4.14 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-056 | P4.15 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-006 | DOWNSTREAM_GATE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-057 | P4.16 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-058 | P4.17 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-059 | P4.18 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-060 | P4.19 | 00_PLATFORM_v1.1 §21K.1; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-003, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-061 | P4.20 | 00_PLATFORM_v1.1 §21K.4; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-062 | P4.21 | 00_PLATFORM_v1.1 §21K.4; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-063 | P4.22 | 00_PLATFORM_v1.1 §21K.4; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-001, AR-003, AR-005, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-064 | P5.1 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-065 | P5.2 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-003, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-066 | P5.3 | 00_PLATFORM_v1.1 §21K.6; §21K.7; §21L.22 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-003, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-067 | P5.4 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-068 | P5.5 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-009 | DOWNSTREAM_GATE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-069 | P5.6 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-070 | P5.7 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-071 | P5.8 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-003, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-072 | P5.9 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-073 | P5.10 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-074 | P5.11 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-075 | P5.12 | 00_PLATFORM_v1.1 §21K.3; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-001, AR-003, AR-008, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / AMENDED_BY_PC-03 / ARC_PENDING |
| ARQ-PERF-076 | P5.13 | 00_PLATFORM_v1.1 §21K.6; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-077 | P5.14 | 00_PLATFORM_v1.1 §21K.6; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-078 | P5.15 | 00_PLATFORM_v1.1 §21K.6; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-079 | P5.16 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-080 | P5.17 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-081 | P5.18 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-082 | P5.19 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-083 | P5.20 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-084 | P5.21 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-085 | P5.22 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-086 | P5.23 | 00_PLATFORM_v1.1 §21K.3; §21K.7; §21L.22; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-003, AR-005, AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-087 | P6.1 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-088 | P6.2 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / AMENDED_BY_PC-02 / ARC_PENDING |
| ARQ-PERF-089 | P6.3 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-090 | P6.4 | 00_PLATFORM_v1.1 §21J.24; §21K.4; §21K.7; §21L.22 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-091 | P6.5 | 00_PLATFORM_v1.1 §21J.24; §21K.4; §21K.7; §21L.22 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-092 | P6.6 | 00_PLATFORM_v1.1 §21J.24; §21K.4; §21K.7; §21L.22 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-093 | P6.7 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-094 | P6.8 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-006, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-095 | P6.9 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-006, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-096 | P6.10 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-097 | P6.11 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-098 | P6.12 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-099 | P6.13 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-100 | P6.14 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-101 | P6.15 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-102 | P6.16 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-103 | P6.17 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-004, AR-005, AR-007 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-104 | P6.18 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-004, AR-005, AR-007 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-105 | P6.19 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-106 | P6.20 | 00_PLATFORM_v1.1 §21J.24; §21K.4; §21K.7; §21L.22 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-005, AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-107 | P6.21 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-108 | P6.22 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | EVIDENCE_GATE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-109 | P6.23 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-110 | P6.24 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-111 | P6.25 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-112 | P6.26 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-113 | P6.27 | 00_PLATFORM_v1.1 §21J.20; §21J.24; §21K.4; §21K.5; §21K.7 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-114 | P7.1 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-003, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-115 | P7.2 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-005, AR-009 | EVIDENCE_GATED_DESIGN | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-116 | P7.3 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-117 | P7.4 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-118 | P7.5 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-119 | P7.6 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-004, AR-005, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-120 | P7.7 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-004, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-121 | P7.8 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-004, AR-005, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-122 | P7.9 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-004, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-123 | P7.10 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-124 | P7.11 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-125 | P7.12 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-126 | P7.13 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-005, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-127 | P7.14 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-003, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-128 | P7.15 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-129 | P7.16 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-004, AR-005, AR-007 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-130 | P7.17 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-002, AR-004, AR-005 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-131 | P7.18 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-132 | P7.19 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-003, AR-005, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-133 | P7.20 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-005, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-134 | P7.21 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-002, AR-005, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-135 | P7.22 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-136 | P7.23 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-002, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-137 | P7.24 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-002, AR-003, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-138 | P7.25 | 00_PLATFORM_v1.1 §21K.4; §21K.7; §21K.8; §21J.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-002, AR-004, AR-005, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-139 | P8.1 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-140 | P8.2 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-141 | P8.3 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-002, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-142 | P8.4 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-143 | P8.5 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-008 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-144 | P8.6 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-145 | P8.7 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-006, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-146 | P8.8 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-008 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-147 | P8.9 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-007, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-148 | P8.10 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-003, AR-005, AR-007, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-149 | P8.11 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-005, AR-006, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-150 | P8.12 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-006, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-151 | P8.13 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-005, AR-006, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-152 | P8.14 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009 | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-153 | P8.15 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-154 | P8.16 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-003, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-155 | P8.17 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-156 | P8.18 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-157 | P8.19 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-002, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-158 | P8.20 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-007, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-159 | P8.21 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009 | EVIDENCE_GATE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-160 | P8.22 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-161 | P8.23 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-001, AR-007, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-162 | P8.24 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-003, AR-005, AR-006, AR-008, AR-009 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-163 | P8.25 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-007, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-164 | P8.26 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-004, AR-005, AR-008 | BLOCKING_ARCHITECTURE | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-165 | P8.27 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | DERIVED_ACCEPTED_GRILL_REQUIREMENT | AR-008, AR-009; governance-wide | ARCHITECTURE_DESIGN_INPUT | ARQ_LOCKED / ARC_PENDING |
| ARQ-PERF-166 | P8.28 | 00_PLATFORM_v1.1 §21J.21–§21J.24; §21K.5; §21K.7; §21K.8; §21L.22; §21L.24 | EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL | AR-001, AR-003, AR-005, AR-007, AR-008, AR-009 | BLOCKING_INVARIANT | ARQ_LOCKED / ARC_PENDING |

# 8C. Next Planned Step — AR-000-A Analytics Grill

Performance requirements extraction is closed. The next focused AR-000 requirements session is:

**AR-000-A — Analytics, Reporting, Funnels & Financial Intelligence Grill**

This Grill must use the same permanent rules:

- multiple-choice questions only;
- a recommended answer for every question;
- recommendations grounded in Product Law plus current primary/best-practice research;
- accepted answers converted into stable `ARQ-AN-*` requirements;
- append accepted requirements to this same cumulative document;
- bump SemVer on every accepted addition;
- never delete earlier requirements; amendments/supersessions preserve history explicitly.



# 8D. AR-000-A — Analytics, Reporting, Funnels & Financial Intelligence

## 8D.1 Round A1 — Analytics Truth, Metric Definitions & Event Governance

A1 was accepted in full on 2026-08-16. The requirements below are therefore locked AR-000 requirements. They define what Architecture must make true; they do not yet choose the final analytics storage engine, warehouse, event collector, semantic-layer product, BI tool, or dashboard implementation.

### ARQ-AN-001 — Analytics is projection, not operational business authority
- **Grill source:** A1.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6 Analytics`; supported by `§21H.22 Operational dashboards`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Analytics consumes and projects authoritative domain facts. It must never become the authority for payment, entitlement, safety, consent, inventory/capacity, identity, or other operational business truth. A dashboard/projection may describe a business fact but may not create or redefine it.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-002 — Governed semantic definitions for important metrics
- **Grill source:** A1.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Every important governed metric/KPI must have one controlled semantic definition including at minimum business meaning/formula, population/scope, grain, time basis/window, inclusions/exclusions, accountable owner, and definition version. Dashboard-local redefinitions of the same governed metric are not permitted.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-003 — Distinct governed user/population identities
- **Grill source:** A1.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Analytics must distinguish materially different populations rather than expose one ambiguous universal `user_count`. Definitions must support relevant distinctions such as anonymous visitor, registered account, verified account, purchaser, recipient, participant, enrolled participant, active participant, member, practitioner, and staff/admin. Every governed metric must identify which population it measures.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-004 — Session is an analytical construct, not business authority
- **Grill source:** A1.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`; `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** A session may be defined and used as an analytical interaction construct, but session counts/state must not determine authoritative enrolment, entitlement, attendance, participation completion, payment, or other business truth. Those facts use their own governed domain definitions.
- **Primary downstream workstreams:** AR-003, AR-005
- **Blocking classification:** ARCHITECTURE_DESIGN_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-005 — Governed analytics event contracts
- **Grill source:** A1.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`; `§21I.16 Analytics after deletion`; `§21K.6 Analytics`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Important analytics events require a governed event contract/schema containing at minimum stable event identity/name, business meaning, event version, required/optional properties, actor/subject identity rules, authoritative source, timestamp semantics, privacy classification, and retention/deletion class. Arbitrary undocumented event payloads may not become governed analytics contracts.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007
- **Blocking classification:** BLOCKING_ARCHITECTURE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-006 — Versioned analytics event-schema evolution
- **Grill source:** A1.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`; `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Material changes to event meaning or schema require explicit compatible evolution/versioning so historical data remains interpretable. Analytics event semantics may not be silently changed in place in a way that makes old and new observations indistinguishable.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006
- **Blocking classification:** BLOCKING_ARCHITECTURE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-007 — Distinct event-time semantics
- **Grill source:** A1.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`; `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where relevant, analytics must preserve distinct semantics for when the business event actually occurred, when the platform authoritatively recorded/committed it, and when analytics received/processed it. Late, retried, offline-synchronised, or provider-delayed facts must remain temporally interpretable.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_ARCHITECTURE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-008 — Governed conversion is tied to authoritative business outcomes
- **Grill source:** A1.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`; `§21K.6 Analytics`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** A governed successful conversion must be tied to the authoritative business transition appropriate to that metric, not merely a browser page view, button click, or third-party analytics event. Intermediate funnel events such as checkout-started, payment-initiated, payment-verified, redemption, or entitlement-granted remain distinct measurable facts.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-009 — Governed funnel contracts
- **Grill source:** A1.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Every governed funnel must define its population, entry criteria, ordered steps, open/closed behaviour, allowable time window, repeat-step behaviour, cross-session behaviour, success event, exclusions, and version. Funnel conversion rates may not be treated as stable KPIs without these semantics.
- **Primary downstream workstreams:** AR-003, AR-005; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-010 — Cross-session/device journey semantics must be explicit
- **Grill source:** A1.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Funnel and lifecycle definitions must explicitly state whether steps may span sessions, devices, enrolments, and time windows according to the business question. The platform must not silently assume all meaningful journeys occur in one browser session or merge activity indefinitely without a governed rule.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-011 — Analytics events are not financial truth
- **Grill source:** A1.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.12 Commercial records`; `§21K.6 Analytics`; supported by `§21H.22 Operational dashboards`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Monetary/financial/commercial truth must derive from the authoritative commercial, payment, accounting, refund, chargeback, tax, or other approved financial records appropriate to the metric. Behavioural analytics events may explain user behaviour but may not become the source of financial truth.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-012 — Distinct governed commercial/financial measures
- **Grill source:** A1.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.12 Commercial records`; `§21H.22 Operational dashboards`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Commercial/financial reporting must define distinct governed measures where applicable, including gross sales, discounts, refunds, chargebacks, taxes, gateway fees, net sales, recognised/accounting revenue if later applicable, recurring/member revenue, and complimentary/sponsored value. An unlabeled or semantically ambiguous generic `revenue` figure is not a governed KPI.
- **Primary downstream workstreams:** AR-003, AR-005; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-013 — Marketing attribution is interpretation, not transaction truth
- **Grill source:** A1.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.12 Commercial records`; `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Marketing attribution models may assign analytical credit to an authoritative transaction, but may not alter whether the transaction occurred, its authoritative value, refund/chargeback state, or accounting treatment. Multiple attribution models may coexist only when clearly identified as interpretations.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-014 — Metric definitions are versioned and historically interpretable
- **Grill source:** A1.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** A material change to a governed metric definition must create an explicit version/amendment. The definition must state whether historical periods are recalculated under the new version or preserved under their original version. Different semantic versions may not be silently mixed into one trend as though they were identical.
- **Primary downstream workstreams:** AR-003, AR-005; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-015 — Deterministic reconciliation of late/corrected analytical facts
- **Grill source:** A1.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6 Analytics`; supported by `§21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Analytics projections must support deterministic reconciliation/backfill when authoritative source facts arrive late, are retried, or are legitimately corrected. Corrections must remain auditable; authoritative business records may not be rewritten merely to make a dashboard match an earlier projection.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_ARCHITECTURE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-016 — Realtime analytics counters are reconcilable projections
- **Grill source:** A1.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / PERFORMANCE_TARGET
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6 Analytics`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Realtime counters may provide fast approximate/current operational views where justified, but their freshness/precision semantics must be explicit and they must reconcile to durable authoritative/analytical facts. A Redis or other realtime counter is not final business or financial truth merely because it is fast.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-017 — Analytics data-quality controls
- **Grill source:** A1.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`; `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed analytics requires data-quality controls appropriate to criticality, including schema validity, duplicate detection, required-property completeness, freshness/lag, unexpected volume changes, impossible-state detection, and reconciliation against authoritative totals where applicable.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-018 — Analytics deletion/anonymisation follows Product Law
- **Grill source:** A1.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.16 Analytics after deletion`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Full participant deletion must remove identifiable event-level analytics, stop future collection, delete/anonymise participant identifiers, issue required deletion instructions to external processors, and apply small-group suppression where appropriate. Only irreversibly aggregated statistics may remain where re-identification is not reasonably possible.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-019 — Detailed health/journal data stays out of general analytics
- **Grill source:** A1.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.16 Analytics after deletion`; `§21H.22 Operational dashboards`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Journals and detailed health/clinical records must not enter general analytics. General analytical surfaces may receive only specifically approved, minimised dimensions/aggregates; any separately governed legitimate clinical/professional analytical purpose requires its own controlled authority, access, privacy, retention, and small-group/re-identification safeguards.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-020 — Identity stitching is governed processing
- **Grill source:** A1.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.16 Analytics after deletion`; `§21I.12 Commercial records`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Analytics identity stitching may use only explicitly approved identifiers and must obey purpose, consent, privacy, retention, and deletion rules. It may not reconstruct a deleted identity, repurpose finance/security records to rebuild analytics identity, or combine identities across purposes merely because technical linkage is possible.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-021 — Governed KPI ownership and promotion
- **Grill source:** A1.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** A top-level governed business KPI requires an accountable business owner and controlled technical implementation/review. Exploratory metrics may exist for investigation but must be clearly labelled non-governed until formally promoted, defined, versioned, and approved.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** GOVERNANCE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-022 — Overarching Analytics truth doctrine
- **Grill source:** A1.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6 Analytics`; `§21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`; `§21I.16 Analytics after deletion`; `§21I.12 Commercial records`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Analytics is a governed, versioned, privacy-constrained projection of authoritative business events and records. Metrics, cohorts, funnels, attribution models, and KPIs require explicit semantics. Behavioural data may explain what users did but may not redefine payment, entitlement, safety, consent, inventory/capacity, identity, or financial truth.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007, AR-008, AR-009
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

## 8D.2 Round A2 — Users, Cohorts, Engagement, Retention, Churn & Product Behaviour

A2 was accepted in full on 2026-08-16. The requirements below are locked AR-000 requirements. They govern lifecycle semantics and analytical interpretation; they do not create a second lifecycle authority separate from the relevant business domains.

### ARQ-AN-023 — Platform-specific active-user semantics
- **Grill source:** A2.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3 Five-year non-financial success`; `§21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed platform `active_*` metrics must use platform-specific qualifying activity appropriate to the measured product/context. Third-party vendor definitions such as GA4 Active Users may remain vendor metrics but must not redefine governed platform activity semantics.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-024 — Distinct active-state concepts
- **Grill source:** A2.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.22`; `§21H.23`; `§21I.17 Inactive accounts`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Analytics must distinguish materially different concepts such as active account, active membership, active programme enrolment, active programme participant, active community participant, and recently engaged user. A single ambiguous universal `active=true/false` metric may not collapse these states.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-025 — Meaningful engagement uses governed value actions
- **Grill source:** A2.3
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.22`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Meaningful product engagement must be defined through governed product-relevant value actions. Passive page views, dwell time, sessions, or vendor engagement metrics may support analysis but must not automatically equal meaningful product engagement.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-026 — Product-specific activation milestones
- **Grill source:** A2.4
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.22`; `§21H.23`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Each important product or programme must define an explicit activation milestone that represents first meaningful receipt/use of core value. Registration, first login, or first email open may be useful events but do not automatically constitute product activation.
- **Primary downstream workstreams:** AR-003, AR-005; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-027 — Business cohorts and analytical cohorts are distinct
- **Grill source:** A2.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.2 Delivery model`; `§21H.23 Analytics and repeat participation`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** A business/programme Cohort is an authoritative programme concept under a ChallengeEdition and must remain distinct from an analytical cohort, which is a governed grouping used for analysis. Analytics may project business cohort membership but may not replace or redefine it.
- **Primary downstream workstreams:** AR-003, AR-005; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-028 — Historical enrolment/cohort membership is preserved
- **Grill source:** A2.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.2`; `§21H.23`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Original enrolment and cohort association must remain historical truth. Later repeat participation creates new governed enrolment/history rather than moving, merging, or overwriting earlier participation.
- **Primary downstream workstreams:** AR-003, AR-005
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-029 — Analytical cohort snapshot/dynamic semantics are explicit
- **Grill source:** A2.7
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`; supported by `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Every governed analytical cohort must state whether membership is a fixed historical snapshot or dynamically recalculated. The BI/analytics implementation may not silently choose or change that semantic.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_ARCHITECTURE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-030 — Temporal property semantics for historical analysis
- **Grill source:** A2.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`; `§21H.2`; `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Analyses involving mutable properties must explicitly choose the relevant temporal semantic, such as property at event/cohort-entry time versus current property. Historical analyses must not silently change merely because a participant's current profile or membership later changes.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_ARCHITECTURE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-031 — Governed retention start/return semantics
- **Grill source:** A2.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.23`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Every governed retention metric must define its eligible starting population/start event, qualifying return/value event, and time interval. Account existence or generic login alone does not automatically equal retention.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-032 — Retention cadence follows product usage lifecycle
- **Grill source:** A2.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.3 Meaning of 60 days`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Retention cadence must reflect expected product usage frequency and lifecycle. Daily, weekly, programme-relative, membership-period, or other windows may differ by product; universal D1/D7/D30 semantics are not automatically authoritative.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-033 — Retention time model must be explicit
- **Grill source:** A2.11
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.3`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Every governed retention metric must state its time model, including whether intervals are rolling elapsed periods, calendar periods, cohort-relative periods, or another explicit model. Analytics tools may not silently choose this semantic.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-034 — Stable retention denominator and unique-count rules
- **Grill source:** A2.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Each governed retention metric must define a stable eligible entry population/cohort and unique-count rules so its numerator and denominator remain reproducible and interpretable over time.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-035 — DAU/WAU/MAU only when product cadence warrants them
- **Grill source:** A2.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Daily/weekly/monthly active measures may be used only where they meaningfully correspond to the product's expected value cadence, with qualifying activity explicitly defined. DAU/WAU/MAU are not automatic platform North-Star metrics.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-036 — Churn is not generic inactivity
- **Grill source:** A2.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.2 Five-year scale target`; `§19.3`; `§21H.20 Completion and certificate`; `§21I.17 Inactive accounts`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Analytics must distinguish subscription/member churn from inactivity/dormancy, programme abandonment, entitlement expiry, community inactivity, safety withdrawal, and account deletion. These states may be related analytically but are not interchangeable definitions.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-037 — Voluntary and involuntary membership churn are distinct
- **Grill source:** A2.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.2`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where recurring membership exists, deliberate cancellation/non-renewal must remain analytically distinct from failed-payment or other involuntary loss. Failed payments may contribute to involuntary churn but may not be silently reclassified as voluntary cancellation.
- **Primary downstream workstreams:** AR-003, AR-005; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-038 — Churn effective time follows authoritative lifecycle state
- **Grill source:** A2.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.2`; supported by general entitlement/membership authority rules
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed membership churn becomes effective at the authoritative business-state transition where membership/entitlement actually ceases or enters the approved churned state. Cancellation-request time may be measured separately but may not silently replace the authoritative effective state.
- **Primary downstream workstreams:** AR-003, AR-005; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-039 — Reactivation preserves prior churn history
- **Grill source:** A2.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.2`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** A returning churned member must create an explicit reactivation/new lifecycle transition while prior churn history remains preserved. Reactivation may not rewrite history so it appears the churn episode never occurred.
- **Primary downstream workstreams:** AR-003, AR-005
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-040 — Dormancy and commercial churn remain distinct
- **Grill source:** A2.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.17 Inactive accounts`; `§19.2`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Account dormancy/inactivity lifecycle states and commercial/member churn are distinct governed concepts. Analytics must project the authoritative account lifecycle rather than infer commercial churn solely from inactivity.
- **Primary downstream workstreams:** AR-003, AR-005, AR-007
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-041 — Programme completion is projected from authoritative versioned criteria
- **Grill source:** A2.19
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.20 Completion and certificate`; `§21H.22`; `§21H.23`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Programme completion analytics must project the authoritative versioned programme-completion criteria/status. Analytics may not create a parallel completion engine based on logins, elapsed days, arbitrary engagement scores, or dashboard-local formulas.
- **Primary downstream workstreams:** AR-003, AR-005
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-042 — Safety withdrawal remains a distinct outcome
- **Grill source:** A2.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.20 Completion and certificate`; `§21H.22`; `§21H.23`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** `withdrawn_for_safety` must remain a distinct governed programme outcome and may not be silently reclassified as ordinary disengagement, abandonment, failure, or commercial churn. Reporting must preserve this distinction while respecting safety/privacy access boundaries.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-043 — Preserve Day-60 and later catch-up completion states
- **Grill source:** A2.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.3 Meaning of 60 days`; `§21H.20 Completion and certificate`; `§21H.23`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Analytics must preserve the participant's status at the formal cohort conclusion and separately measure later approved catch-up completion. Later completion must not retroactively rewrite the Day-60 historical snapshot.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-044 — Repeat participation remains enrolment-level truth plus lifetime analytics
- **Grill source:** A2.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`; supported by `§21H.2 Delivery model`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Each repeat programme participation creates and preserves its own enrolment/edition/cohort history. Analytics may derive participant-level lifetime measures across enrolments but may not merge those enrolments into a single rewritten authoritative participation record.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-045 — Adoption denominators use eligible/opportunity populations
- **Grill source:** A2.23
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards`; `§21H.23 Analytics and repeat participation`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed feature/product adoption rates must use a denominator representing the population that actually had eligibility/opportunity to use the feature. All accounts may not be used as a default denominator where many accounts could not access the capability.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-046 — Overarching lifecycle/retention doctrine
- **Grill source:** A2.24
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.3`; `§21H.2`; `§21H.3`; `§21H.20`; `§21H.22`; `§21H.23`; `§21I.17`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** User lifecycle analytics must be built from explicit product-relevant states and value events. Activation, engagement, retention, dormancy, churn, abandonment, completion, safety withdrawal, repeat enrolment, and reactivation are distinct concepts. Historical lifecycle states must remain interpretable and may not be retroactively rewritten merely to simplify current reporting.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING


## 8D.3 Round A3 — Acquisition, Funnels, Attribution & Campaign Measurement

All A3 recommendations were accepted on 2026-08-16. These requirements preserve acquisition evidence separately from attribution interpretation, keep authoritative conversions anchored to business truth, and make marketing measurement explicitly privacy/consent constrained.

### ARQ-AN-047 — Acquisition source has distinct temporal meanings
- **Grill source:** A3.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`; `§21C.19 Consent and processing permissions`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Analytics must distinguish first-known acquisition, later session/visit acquisition, event/conversion touchpoints, and governed attribution results. One generic `source` value may not silently stand for all of these temporal meanings.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-006, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-048 — Preserve first-known acquisition separately from later touches
- **Grill source:** A3.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`; `§21C.19`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** First-known acquisition history must be preserved independently from later campaign/session/event touches. A later interaction may not overwrite how the participant was first known to have been acquired.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-049 — Govern campaign taxonomy and naming
- **Grill source:** A3.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.18 Complimentary and sponsored access`; `§21H.23`
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Campaign source, medium, campaign, and related acquisition classifications must follow a governed taxonomy/naming convention and should map to stable internal campaign identity where practical. Equivalent labels may not fragment reporting merely because operators used inconsistent spelling/casing.
- **Primary downstream workstreams:** AR-003, AR-006, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-050 — Preserve raw acquisition evidence separately from normalised classification
- **Grill source:** A3.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21C.19`; `§21I.13`; `§21I.16`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Preserve only the privacy-approved raw acquisition evidence necessary to support later reclassification, separately from governed normalised channel/campaign classifications. Raw URL/query data may not be retained indiscriminately and remains subject to purpose, retention, deletion, and minimisation rules.
- **Primary downstream workstreams:** AR-003, AR-004, AR-007, AR-008
- **Blocking classification:** PRIVACY_AND_DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-051 — Stable campaign identity outranks mutable campaign name
- **Grill source:** A3.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.18`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Campaigns should use stable identifiers where practical. Human-readable campaign names are mutable descriptive metadata and may not be the sole identity used to preserve longitudinal campaign reporting.
- **Primary downstream workstreams:** AR-003, AR-006, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-052 — Attribution models are versioned analytical interpretations
- **Grill source:** A3.6
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`; supported by `§19 Revenue and Growth Targets`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** No attribution model is universal business truth. Attribution results must identify the governed model and applicable lookback/window semantics, and material model changes require explicit versioning rather than silent reinterpretation.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-053 — Attribution models may be compared without multiplying conversions
- **Grill source:** A3.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`; `§19.1`; `§19.2`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Multiple attribution models may allocate analytical credit differently over the same authoritative conversion set. Model comparison must never create additional commercial transactions or add attributed totals from different models as though they represented separate conversions.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-054 — Direct/unknown acquisition is evidence absence, not behavioural proof
- **Grill source:** A3.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** A direct/unknown/no-referrer classification means usable referral/campaign evidence was unavailable to that measurement path. It may not be presented as proof that a person manually typed a URL or followed any other specific human acquisition behaviour.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-055 — Later direct visits do not overwrite first acquisition
- **Grill source:** A3.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Later direct/unknown visits must remain session/event-level observations and may not overwrite previously known first-acquisition history.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-056 — Governed cross-domain journey continuity
- **Grill source:** A3.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21C.19`; `§21H.23`; `§21I.13`; `§21I.16`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where a legitimate owned user journey crosses domains, analytics may preserve approved measurement continuity without fragmenting the journey, but cross-domain identity/measurement must retain security, consent, purpose, and privacy boundaries. It may not become blanket cross-domain tracking authority.
- **Primary downstream workstreams:** AR-001, AR-004, AR-006, AR-007, AR-008
- **Blocking classification:** PRIVACY_AND_ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-057 — Anonymous-to-known identity transitions must be explicit and approved
- **Grill source:** A3.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21C.19`; `§21I.13`; `§21I.16`
- **Source classification:** EXPLICIT_PRIVACY_LAW_REFINED_BY_GRILL
- **Requirement:** Association of pre-authentication analytics activity with an authenticated participant requires an explicit approved identity transition and must obey applicable purpose, consent, deletion, and privacy rules. Technical correlatability alone is insufficient authority to merge identities.
- **Primary downstream workstreams:** AR-004, AR-005, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-058 — No covert fingerprinting for attribution completeness
- **Grill source:** A3.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21C.19 Consent and processing permissions`; `§21I.13`; `§21I.16`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT_FROM_PRIVACY_LAW
- **Requirement:** The platform must not introduce covert/probabilistic browser or device fingerprinting merely to increase marketing attribution completeness. Cross-device identity must use explicitly approved identity mechanisms and lawful purpose/consent rules.
- **Primary downstream workstreams:** AR-004, AR-006, AR-007
- **Blocking classification:** BLOCKING_PRIVACY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-059 — Measurement collection/use is purpose- and consent-aware
- **Grill source:** A3.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21C.19 Consent and processing permissions`; `§21I.13 Consent withdrawal`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Analytics/marketing measurement must honour the applicable lawful-purpose/permission state at collection and use time. Required product processing, anonymised/aggregated analytics, marketing communications, advertising-related processing, and personalisation may not be collapsed into one perpetual consent flag.
- **Primary downstream workstreams:** AR-004, AR-006, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-060 — Marketing withdrawal stops affected future marketing measurement/processing
- **Grill source:** A3.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.13 Consent withdrawal`; `§21C.19`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Marketing withdrawal must stop the affected future marketing processing/collection and invalidate dependent active permissions/state. Historically lawful records may remain only where Product Law permits them; withdrawal does not erase authoritative commercial records or rewrite prior lawful processing.
- **Primary downstream workstreams:** AR-004, AR-006, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-061 — Successful conversion originates from authoritative business transition
- **Grill source:** A3.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Commercial dashboards`; `§21H.23`; `§19.1`; `§19.2`
- **Source classification:** EXPLICIT_PLATFORM_AUTHORITY_PRINCIPLE_REFINED_BY_GRILL
- **Requirement:** Successful commercial conversion truth must originate from the governed authoritative business transition appropriate to the metric, not from a browser page/event or advertising-platform report. Client/server analytics signals project the conversion but do not create it.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-062 — Multiple conversion-delivery paths require deterministic deduplication
- **Grill source:** A3.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21H.23`; supported by platform idempotency/deduplication rules`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** When the same conversion may be emitted through browser, server, queue, webhook, or other measurement paths, use a stable business/conversion identity and deterministic deduplication so one authoritative conversion cannot be multiplied by duplicate analytical delivery.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-063 — Modelled conversions remain estimates and cannot create business truth
- **Grill source:** A3.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21H.23`; `§21K.6 Analytics`
- **Source classification:** EXPLICIT_ANALYTICS_NON_AUTHORITY_PRINCIPLE_REFINED_BY_GRILL
- **Requirement:** Statistical/modelled conversion estimates may exist as clearly labelled analytical estimates but may never create authoritative payments, purchases, entitlements, inventory effects, or commercial records.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-064 — Attribution/conversion windows are explicit and versioned
- **Grill source:** A3.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Every governed attribution/funnel metric must declare the applicable conversion/lookback window. Material window changes require metric/model versioning so historical reports do not silently mix incompatible definitions.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-065 — Refunds/chargebacks preserve original conversion chronology
- **Grill source:** A3.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Commercial dashboards`; `§19 Revenue and Growth Targets`; `§21I.12 Commercial records`
- **Source classification:** EXPLICIT_COMMERCIAL_RECORD_PRINCIPLE_REFINED_BY_GRILL
- **Requirement:** A later refund, chargeback, or reversal must not delete/rewrite the historical fact that an original conversion occurred. Analytics must project the later commercial reversal separately so gross conversion and current/net commercial outcome remain distinguishable.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-066 — Sensitive health/safety/journal profiling is excluded from advertising measurement by default
- **Grill source:** A3.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.16 Analytics after deletion`; `§21H.22`; `§21C.19`; journal privacy boundaries in `§21F`
- **Source classification:** EXPLICIT_PRIVACY_PRODUCT_LAW_REFINED_BY_GRILL
- **Requirement:** Detailed health, safety, journal, and similarly sensitive participant-profile data must not enter advertising/marketing measurement or targeting merely because it could improve attribution or performance. Any exceptional future use requires explicit upstream lawful-purpose/privacy approval and a separately governed surface.
- **Primary downstream workstreams:** AR-004, AR-006, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-067 — Vendor conversion reports are labelled/reconciled, not financial truth
- **Grill source:** A3.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21H.23`; `§21K.6 Analytics`; `§19.1`; `§19.2`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT_FROM_ANALYTICS_NON_AUTHORITY
- **Requirement:** Vendor-reported or modelled conversion/revenue figures must be clearly distinguished from authoritative platform conversions and commercial values. Material discrepancies require reconciliation/explanation rather than silent equivalence.
- **Primary downstream workstreams:** AR-003, AR-006, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-068 — Overarching acquisition and attribution doctrine
- **Grill source:** A3.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21C.19`; `§21H.22`; `§21H.23`; `§21I.13`; `§21I.16`; `§21K.6`; `§21L.18`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENTS_SYNTHESISED_BY_GRILL
- **Requirement:** Preserve acquisition evidence, governed campaign identities, and chronological touchpoints separately from attribution interpretation. Authoritative conversions come from business truth; attribution models allocate analytical credit but never create/alter transactions. Identity stitching and measurement remain purpose-, consent-, privacy-, deletion-, and minimisation-constrained.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-006, AR-007, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING


## 8D.4 Round A4 — Revenue, Finance, Refunds, Subscriptions, MRR/ARR, LTV & Commercial Reporting
All A4 recommendations were accepted on 2026-08-16. Two explicit user refinements were locked at the same time: Paystack is the first/launch payment gateway, and management/commercial revenue reporting must include all income in scope and then separate it by governed income type. The Paystack lock is recorded separately as a cross-cutting requirement because it is a payment-platform decision, not merely an analytics metric.

### ARQ-AN-069 — Authoritative monetary facts originate outside analytics
- **Grill source:** A4.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21J.15`; `§21I.12`; `§21H.22`; `§19`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Authoritative commercial, payment, refund, dispute, tax, settlement, and accounting facts must come from their approved business/finance sources. Analytics may project and aggregate those facts but may not create financial truth.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-070 — Money-looking concepts require explicit governed semantics
- **Grill source:** A4.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.1–§19.2`; `§21H.22`; `§21I.12`
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Financial/commercial reporting must govern materially different concepts separately, including sale/order value, amount due, cash collected, gross sales, discounts, refunds, disputes/chargebacks, taxes, payment fees, net commercial proceeds, recurring run-rate measures, and formally recognised accounting revenue where applicable. A generic field named `revenue` may not silently stand for all of them.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-071 — Payment success does not automatically equal accounting revenue recognition
- **Grill source:** A4.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21J.15`; `§21I.12`; `§19`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Verified payment establishes a payment fact. Formal accounting revenue recognition follows approved accounting policy and may occur on a different date or basis. Analytics may not equate successful collection with recognised accounting revenue unless finance/accounting law explicitly permits that treatment.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Finance/accounting authority later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-072 — Executive finance labels must not invent accounting policy
- **Grill source:** A4.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21H.22`; `§21I.12`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Until formal accounting policy is locked, executive dashboards must use explicitly named commercial measures such as gross sales, payments collected, refunds, and recurring run-rate rather than labelling a derived figure `recognised revenue` without governed accounting support.
- **Primary downstream workstreams:** AR-003, AR-008; Finance/accounting authority later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-073 — Existing Product Law MRR target is a gross recurring commercial run-rate
- **Grill source:** A4.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.1`; `§19.2`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** The existing paying-members × monthly-price MRR milestones are governed gross recurring commercial run-rate targets. They are distinct from VAT, payment fees, discounts, failed-payment effects, refunds, collected cash, profit, and formal accounting revenue recognition.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-074 — Platform MRR requires its own governed contract
- **Grill source:** A4.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.1–§19.2`; `§21A.5`; `§21A.8`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** The platform must define and version its own MRR semantics, including included subscription states, recurring discounts, trials/free periods, taxes, usage-based components if ever added, pauses, failed-payment/grace states, cancellations, and reactivations. Payment-provider MRR definitions are evidence/reference only.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-075 — Recurring revenue may expose multiple governed views
- **Grill source:** A4.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21A.5`; `§21A.8`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where decision-useful, reporting may distinguish gross contractual/run-rate MRR, good-standing recurring MRR, at-risk/past-due MRR, lost/churned MRR, and collected recurring cash. Different economic states must not be collapsed merely to produce one favourable headline value.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-076 — One-time income is excluded from MRR
- **Grill source:** A4.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21A.5`; commercial product rules throughout `§21A` and `§21L`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** MRR measures governed recurring subscription/member value only. One-time assessments, plans, programmes, events, bundles, and other non-recurring sales remain separate income/revenue categories and may not be annualised into MRR merely to increase the metric.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-077 — Complimentary/sponsored access does not silently inflate paid MRR
- **Grill source:** A4.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.18`; `§19`
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Complimentary or sponsored access grants do not count as paying-member MRR merely because the entitlement has a list price. Actual sponsor payments, where they exist, are recorded as their own governed income type; imputed promotional value may be shown only when clearly labelled as non-cash/non-paid value.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-078 — Recurring discounts require explicit MRR treatment
- **Grill source:** A4.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21A.13`; `§21L.17`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Reporting may distinguish list-price recurring value from actual contracted recurring run-rate after applicable recurring discounts. The primary operational MRR definition must state which basis it uses and may not ignore discount effects silently.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-079 — Tax/VAT must be explicitly separable
- **Grill source:** A4.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.1–§19.2`; `§21I.12`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Tax amounts must remain explicitly separable from commercial income metrics. Every governed finance KPI must state whether values are tax-inclusive or tax-exclusive. The current Product Law recurring target remains a gross commercial target before VAT.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Finance/tax authority later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-080 — Payment fees remain separate from gross commercial value
- **Grill source:** A4.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.1–§19.2`; `§21I.12`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Preserve gross commercial value and payment-processing fees as separate measures. Net proceeds/cash/contribution measures must be explicitly derived rather than silently redefining gross income by subtracting gateway fees.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-081 — Refunds are linked subsequent financial events
- **Grill source:** A4.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21A.10`; `§21I.12`; `§21I correction rules`; `§21H.22`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** The original sale/payment remains historical truth. A full or partial refund is a linked later financial event/adjustment and may not erase or rewrite the original commercial event.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-082 — Refunds and disputes/chargebacks remain distinct
- **Grill source:** A4.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.12`; `§21J.15`
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Refunds and disputes/chargebacks may produce similar monetary effects but remain distinct governed event/state types and reporting dimensions. They may not be merged into one generic reversal category when the distinction matters operationally or financially.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-083 — Recoveries/resolutions preserve chronology
- **Grill source:** A4.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.12`; correction rules around financial adjustments
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** If a dispute is won, a reversal is reversed, or other funds are recovered, retain the earlier event and append the later recovery/resolution. Reporting must reconstruct both chronology and current financial outcome without rewriting history.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-084 — Failed recurring payment is not immediate subscription churn
- **Grill source:** A4.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21A.8 Failed payments`; `§19`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Payment failure/dunning, grace-period or past-due state, effective cancellation/unpaid termination, entitlement suspension, and commercial churn are distinct lifecycle concepts. A failed recurring charge may not immediately be reported as churn unless the governed lifecycle reaches the churn-effective state.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-085 — Subscription churn uses the effective business transition
- **Grill source:** A4.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21A.8`; `§21A.11`; subscription cancellation rules
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Commercial subscription churn becomes effective at the governed subscription/entitlement cessation transition. Cancellation request time and effective churn time may both be measured, but they may not be silently conflated.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-086 — ARR is an annualised recurring run-rate, not accounting revenue
- **Grill source:** A4.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.1–§19.2`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** ARR must be a governed annualised recurring run-rate derived from the approved recurring-revenue definition, commonly 12 × normalised MRR where valid. It is not a guaranteed forecast, trailing-twelve-month revenue, cash balance, or formal accounting revenue statement.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-087 — Recurring-revenue movement must be decomposable
- **Grill source:** A4.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; membership/subscription lifecycle in `§21A`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where decision-useful, recurring revenue movement should be decomposable into governed categories such as new recurring revenue, expansion, contraction, reactivation, voluntary churn, involuntary loss, and ending run-rate. Ending MRR alone is insufficient to explain change.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-088 — LTV requires a governed, versioned model contract
- **Grill source:** A4.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19 Revenue and Growth Targets`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Every governed LTV metric must state population/cohort, value basis, observation horizon, refund/churn/reactivation treatment, whether the result is observed or modelled, material assumptions, and model version. LTV is derived decision-support information rather than transaction truth.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-089 — Observed and modelled LTV remain distinct
- **Grill source:** A4.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Historical realised/observed customer value and forecast/modelled lifetime value must remain explicitly distinguishable. Forecast value may not be presented as though the underlying income has already occurred.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-090 — CAC requires explicit numerator, denominator and attribution semantics
- **Grill source:** A4.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21H.23`; campaign concepts in `§21L.18`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Every governed CAC metric must specify included acquisition costs, authoritative new-customer/conversion population, attribution model/window, period, and whether it is blended or channel/campaign-specific. External ad-platform CAC is an analytical source, not authoritative platform truth.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-091 — LTV:CAC is derived decision support
- **Grill source:** A4.23
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** LTV:CAC is a derived decision-support ratio and must remain traceable to the exact governed LTV and CAC definitions/versions used. It is not financial truth and no universal benchmark may silently replace platform-specific economics.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-092 — Acquisition-cohort economics preserve stable historical membership
- **Grill source:** A4.24
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.23`; `§19`; campaign concepts in `§21L.18`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Commercial analytics may compare acquisition month, campaign, product, membership, programme, or other governed cohorts, but cohort membership must preserve the applicable historical semantics rather than being reassigned to later acquisition/campaign state.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-093 — Revenue, proceeds, margin and profit are distinct measures
- **Grill source:** A4.25
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19.1–§19.2`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Revenue/income, collected cash or net proceeds, gross/contribution margin, and profit are distinct governed measures with explicit cost-inclusion rules. Product Law gross recurring targets may not be presented as profit.
- **Primary downstream workstreams:** AR-003, AR-008; Finance/accounting authority later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-094 — Future multi-currency reporting must preserve original currency and conversion semantics
- **Grill source:** A4.26
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21A.12 Payment provider, market and currency`
- **Source classification:** EXPLICIT_FUTURE_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** If/when true multi-currency commerce is introduced, preserve authoritative transaction currency/amount. Consolidated currency conversion must record the governed exchange-rate source, date/time basis, and method so historic reporting is reproducible. This requirement does not accelerate multi-currency into MVP.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008
- **Blocking classification:** FUTURE_ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-095 — Finance dashboards expose freshness and reconciliation state
- **Grill source:** A4.27
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21I.12`; `§21K.6 Analytics`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where material, commercial/finance dashboards must state freshness and reconciliation state, such as realtime/provisional versus reconciled/closed. Payment, settlement, refund, dispute, and accounting data may resolve on different timelines.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-096 — Provider reports are reconciliation evidence, not internal financial authority
- **Grill source:** A4.28
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21J.15`; `§21I.12`; `§21A.12`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Payment-provider reports are external evidence sources. Material payment, refund, dispute, and settlement figures must reconcile against authoritative platform commercial records and, where applicable, bank/accounting records. Successful webhooks do not eliminate reconciliation obligations.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-097 — Late finance corrections remain explainable
- **Grill source:** A4.29
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.12`; financial correction rules; audit rules in `§21I.14`
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Late corrections/reconciliation may update derived financial views, but linked event/audit history must remain sufficient to explain what changed and why. Formally closed accounting periods follow the later approved finance/accounting correction policy rather than silent dashboard rewriting.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Finance/accounting authority later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-098 — Overarching commercial and finance analytics doctrine
- **Grill source:** A4.30
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21A`; `§21H.22`; `§21I.12`; `§21J.15`; `§21K.6`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENTS_CONSOLIDATED_BY_GRILL
- **Requirement:** Monetary reporting must preserve distinctions between authoritative commercial transactions, verified payment/cash state, recurring run-rate measures, refunds/disputes, tax/fees, derived unit economics, and formal accounting revenue. Important KPIs require governed definitions and reconciliation paths. Analytics explains and aggregates financial facts but is not the ledger and may not invent accounting policy.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008; Domain Law and finance/accounting authority later
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-099 — Total income completeness with mandatory income-type classification
- **Grill source:** A4 USER REFINEMENT after acceptance
- **Accepted option:** USER-LOCKED
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Strength:** MANDATORY_REQUIREMENT / EXECUTIVE_REPORTING_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19 Revenue and Growth Targets`; `§21H.22 Operational dashboards`; `§21I.12 Commercial records`; product/pricing rules throughout `§21A` and `§21L`
- **Source classification:** USER_LOCKED_REFINEMENT_TO_A4
- **Requirement:** Management/commercial reporting must provide a complete `total_income` view for the selected reporting scope that includes **all authoritative platform income**, not only subscription or membership income. Every included amount must also be classifiable by a governed `income_type` so management can see both the total and its composition. The income taxonomy must be extensible and must cover every actual revenue-bearing product/source (for example recurring membership/subscription income, assessments, plans, programmes/challenges, events/tickets, bundles/add-ons, sponsor income where a sponsor actually pays, and future approved commercial sources). Unclassified income may not be silently omitted; it must surface as a data-quality/governance exception until classified. This management `total_income` measure remains distinct from formal accounting `recognised_revenue` unless approved accounting policy defines them as equivalent for a particular reporting purpose.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008; Domain Law and finance/accounting authority later
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT / EXECUTIVE_REPORTING_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING


## 8D.5 Round A5 — Dashboards, Roles, Drill-down, Alerts, Exports & Decision-Support UX

### ARQ-AN-100 — Role-scoped dashboard classes
- **Grill source:** A5.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards`; privacy/role boundaries throughout `§21C`, `§21I`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Dashboards must be purpose- and role-scoped rather than one universal surface. The architecture must support distinct decision surfaces such as executive/commercial, programme operations, support/operations, marketing/analytics, and tightly controlled professional/safety views according to approved roles and purposes.
- **Primary downstream workstreams:** AR-004, AR-008; Domain Law later
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-101 — Dashboard UI hiding is not authorisation
- **Grill source:** A5.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; actor/policy/privacy requirements throughout Product Law
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Hiding a dashboard tile, route, menu item, or drill-down control is presentation only. Authorisation must be enforced at the underlying query/action/data boundary so bypassing the UI cannot expose unauthorised records or fields.
- **Primary downstream workstreams:** AR-002, AR-004, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-102 — Row- and field-level dashboard restrictions
- **Grill source:** A5.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21I`; role/privacy boundaries
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where sensitivity or role scope requires it, dashboard/report access must constrain both which records a viewer can access and which fields/dimensions are exposed. Dashboard-level permission alone is insufficient.
- **Primary downstream workstreams:** AR-003, AR-004, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-103 — Drill-down inherits or tightens access controls
- **Grill source:** A5.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21I`
- **Source classification:** EXPLICIT_PLATFORM_BOUNDARY_REFINED_BY_GRILL
- **Requirement:** Drill-down from an aggregate must apply the same or stricter current authorisation, purpose, row, field, privacy, and small-group rules as the underlying data. Visibility of an aggregate never implies permission to inspect contributing individual records.
- **Primary downstream workstreams:** AR-003, AR-004, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-104 — General programme dashboards exclude journals and full clinical records
- **Grill source:** A5.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21I.16`; journal boundaries in `§21F`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT
- **Requirement:** General programme dashboards may not expose journals or full clinical/health records through ordinary drill-down. Authorised professional case workflows are separate controlled surfaces with their own access and audit contracts.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-105 — Governed KPI definition metadata is accessible
- **Grill source:** A5.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `ARCHITECTURE_REQUIREMENTS_WORKING.md ARQ-AN-002, ARQ-AN-014`; `00_PLATFORM_v1.1.md §21H.22–§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed KPI/dashboard elements must expose or link to sufficient metric metadata to understand the current definition/version, scope, time basis, and important exclusions. A bare label is not sufficient for trusted decision support.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-106 — Dashboard freshness and reconciliation state are visible
- **Grill source:** A5.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; `§21H.22`; finance freshness requirement already derived in ARQ-AN-095
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Where freshness matters, dashboards must display an appropriate as-of time, last-refresh time, reconciliation state, or equivalent indicator so viewers can distinguish realtime/provisional, cached/materialised, delayed, and reconciled data.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-107 — Refresh frequency follows decision need
- **Grill source:** A5.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6 Analytics`; `§21H.22`
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Dashboard refresh frequency must be selected by decision criticality and freshness need. Safety/operations may require high freshness while executive, cohort, and historical reporting may use delayed/materialised views. No blanket realtime requirement applies.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-108 — Explicit report date/time/timezone semantics
- **Grill source:** A5.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md` timezone requirements; `§21H` cohort-day semantics; analytics event timing requirements derived in A1
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Every governed report must define the relevant date/time and timezone semantics. Business day, cohort day, event occurrence time, transaction time, and processing/ingestion time must not be silently conflated.
- **Primary downstream workstreams:** AR-003, AR-006, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-109 — Period comparisons require an explicit baseline
- **Grill source:** A5.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21H.22–§21H.23`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Comparative KPI values must state their baseline, such as previous equivalent period, prior year, prior cohort, target, or budget. Unequal periods may not be compared without explicit labelling/normalisation.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-110 — Dashboard filters are visible, permission-aware and semantically safe
- **Grill source:** A5.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; role/privacy law
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Dashboard/report filters must be visible or inspectable, permission-aware, and applied consistently to intended metrics. Semantic filters that define a governed KPI may be locked or constrained so users cannot silently change the metric definition.
- **Primary downstream workstreams:** AR-003, AR-004, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-111 — Personal saved views do not redefine canonical metrics
- **Grill source:** A5.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; governed-metric requirements from A1
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where personal saved dashboard views are supported, they may persist presentation and permitted filter state but must not rewrite canonical KPI definitions or promote themselves automatically to governed company metrics.
- **Primary downstream workstreams:** AR-002, AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-112 — Governed/certified content is distinguishable from exploratory analysis
- **Grill source:** A5.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22–§21H.23`; ARQ-AN-021 metric governance
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** The analytics experience must distinguish governed/certified dashboards and KPIs from exploratory analysis. Exploratory work is permitted but must not be presented as canonical until promoted through the approved metric/dashboard governance process.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** GOVERNANCE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-113 — Material business events may annotate reporting timelines
- **Grill source:** A5.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19`; `§21H.23`; version/change governance throughout Product Law
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Relevant reporting timelines should support governed contextual annotations for material events such as product/price changes, campaigns, outages, launches, or metric-definition changes so movement can be interpreted without rewriting historical values.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DOMAIN_SEMANTICS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-114 — Alerts require governed conditions, ownership and action semantics
- **Grill source:** A5.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; operational alert/backlog requirements in `§21J`, `§21K`
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Analytics/business alerts must define a condition/model, window, threshold or trigger, owner, severity, routing, cooldown/re-notification semantics, and expected action. A changing chart alone is not an alert contract.
- **Primary downstream workstreams:** AR-008, AR-009
- **Blocking classification:** OPERATIONS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-115 — Alerting prioritises actionability and noise control
- **Grill source:** A5.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21J`; `§21K`; operational degradation/backlog rules
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Alerts should normally be actionable. Repeated/noisy signals must be suppressible or coalescible with governed thresholds/windows so alert fatigue is reduced without hiding material conditions.
- **Primary downstream workstreams:** AR-008, AR-009
- **Blocking classification:** OPERATIONS_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-116 — Anomaly/model alerts remain analytical signals
- **Grill source:** A5.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; analytics-not-truth doctrine
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Anomaly detection, forecasting, or other model-derived alerts are analytical signals with explicit methodology/version/confidence where relevant. They do not by themselves prove that a business-state transition or safety/financial fact has occurred.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-117 — Sensitive alert payloads are minimised
- **Grill source:** A5.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I`; `§21H.22`; journal/health boundaries
- **Source classification:** EXPLICIT_PLATFORM_PRIVACY_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Alert payloads must be minimised according to recipient, channel, and purpose. Prefer stable identifiers and deep links into authorised workflows rather than transmitting sensitive health, journal, payment, or participant data in the alert itself where not required.
- **Primary downstream workstreams:** AR-004, AR-006, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-118 — Export is a separately governed capability
- **Grill source:** A5.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I`; export/access rights; role-scoped dashboard law
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Ability to view a dashboard does not automatically grant bulk export permission. Export capability may be more restrictive based on role, sensitivity, volume, purpose, and downstream data-release risk.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-119 — Exports enforce row, field, purpose and privacy restrictions
- **Grill source:** A5.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I`; `§21H.22`
- **Source classification:** EXPLICIT_PLATFORM_PRIVACY_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Exported, scheduled, or delivered datasets must enforce at least the same applicable row-level, field-level, purpose, retention, and privacy restrictions as the interactive source. Export must never become a bypass around dashboard/data authorisation.
- **Primary downstream workstreams:** AR-003, AR-004, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-120 — Large exports use bounded durable execution
- **Grill source:** A5.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; async requirements; ARQ-PERF-087–113
- **Source classification:** EXPLICIT_PLATFORM_PERFORMANCE_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Large exports must use bounded processing and, where synchronous execution would be unsafe or expensive, a durable asynchronous generation workflow with explicit limits, status, expiry, and secure retrieval rather than unbounded LiveView/HTTP work.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-121 — Generated exports have explicit retention and secure lifecycle
- **Grill source:** A5.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I`; deletion and file lifecycle rules
- **Source classification:** EXPLICIT_PLATFORM_PRIVACY_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Generated sensitive export artifacts require explicit access control, retention/expiry, storage, delivery, and deletion semantics. Temporary exports must not become uncontrolled long-lived shadow copies of governed data.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-122 — Spreadsheet-compatible exports defend against formula injection
- **Grill source:** A5.23
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21J` security posture; export requirements
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** User-controlled text written to CSV or spreadsheet-compatible exports must be encoded/sanitised so supported spreadsheet software cannot interpret malicious cell content as executable formulas or dangerous links/commands.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** SECURITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-123 — Material/sensitive exports are auditable
- **Grill source:** A5.24
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.14 Audit logs`; export/data-access rights
- **Source classification:** EXPLICIT_PLATFORM_AUDIT_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Material or sensitive exports must record appropriate audit metadata such as actor, report/data scope, timestamp, purpose where required, delivery destination where relevant, and outcome, while avoiding duplication of full sensitive payloads inside audit logs.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** BLOCKING_AUDIT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-124 — Scheduled report delivery remains permission- and purpose-aware
- **Grill source:** A5.25
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I`; `§21H.22`; communication/access boundaries
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Scheduled dashboard/report delivery must remain subject to current permission, purpose, recipient, and filter constraints. A schedule created earlier may not continue exposing data after permissions or valid scope change, and broken/stale filters may not broaden disclosure.
- **Primary downstream workstreams:** AR-004, AR-005, AR-006, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-125 — Authorised financial totals drill toward reconciliation evidence
- **Grill source:** A5.26
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21I.12`; `§21J.15`; ARQ-AN-095–099
- **Source classification:** EXPLICIT_PLATFORM_FINANCE_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Where authorised, important commercial totals must support traceable drill-down through governed reporting layers toward contributing platform transactions, refunds, disputes, settlements, or reconciliation evidence. Analytics may expose evidence but may not mutate authoritative financial records.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-008
- **Blocking classification:** FINANCE_RECONCILIATION_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-126 — Total Income always exposes income-type composition
- **Grill source:** A5.27
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / EXECUTIVE_REPORTING_INVARIANT
- **Exact Product Law source:** `ARCHITECTURE_REQUIREMENTS_WORKING.md ARQ-AN-099`; `00_PLATFORM_v1.1.md §19`; `§21H.22`
- **Source classification:** USER_LOCKED_REFINEMENT_OPERATIONALISED_BY_A5
- **Requirement:** The executive/management Total Income surface must show the governed all-income total for the selected scope and provide an immediately accessible breakdown/filter/drill-down by governed `income_type`. Filtering by type changes the selected slice, not the definition of the all-income total.
- **Primary downstream workstreams:** AR-003, AR-008; Domain Law later
- **Blocking classification:** EXECUTIVE_REPORTING_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-127 — Overarching dashboard decision-surface doctrine
- **Grill source:** A5.28
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22`; `§21I`; `§21K.6`; ARQ-AN-001–126
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENTS_CONSOLIDATED_BY_GRILL
- **Requirement:** Dashboards are role-scoped decision surfaces over governed metrics. Access is enforced beneath the UI; freshness, definition, and context remain visible; drill-down cannot bypass privacy or purpose boundaries; alerts are actionable; exports are controlled data releases; and executive totals remain traceable to authoritative facts.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING



## 8D.8 Round A6 — Data Warehouse, Read Models, Event Pipeline, Data Quality, Reconciliation & Analytics Architecture

### ARQ-AN-128 — PostgreSQL/read-model first; warehouse-ready, not warehouse-first
- **Grill source:** A6.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6 Analytics`; ARQ-PERF-078–080; ARQ-AN-001
- **Source classification:** EXPLICIT_PLATFORM_ANALYTICS_DIRECTION_REFINED_BY_GRILL
- **Requirement:** Begin with efficient PostgreSQL analytical read models, materialised views, precomputed/cached aggregates, and justified replicas where they satisfy the workload. The architecture must remain warehouse-ready, but a dedicated analytical store is introduced only when evidence justifies it rather than as an MVP default.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-129 — Evidence-based warehouse trigger
- **Grill source:** A6.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; performance/scaling ARQs
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Introduce a dedicated analytical store only when evidence such as OLTP contention, large historical scans, materially increasing data volume, high BI concurrency, cross-domain analytical complexity, independent-compute needs, large external-data integration, or similar proven workload pressure makes PostgreSQL read models insufficient or uneconomic.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-130 — OLTP isolation from analytics
- **Grill source:** A6.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENT
- **Requirement:** Protect authoritative OLTP capacity from large analytical scans, exports, transformations, and BI concurrency through suitable query design, materialisation, scheduling, replicas, or later analytical isolation.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** BLOCKING_PERFORMANCE_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-131 — Logical analytical boundary inside PostgreSQL
- **Grill source:** A6.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-AN-001
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Even while analytics uses PostgreSQL, analytical projections/read models must have an explicit logical/module/schema boundary from authoritative transactional structures, with access appropriate to downstream read use.
- **Primary downstream workstreams:** AR-003, AR-004, AR-008
- **Blocking classification:** ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-132 — Freshness-driven projection refresh
- **Grill source:** A6.5
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-AN-029, ARQ-AN-106
- **Source classification:** EXPLICIT_PLATFORM_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Materialised-view/read-model refresh behaviour must match the governed freshness SLO, regeneration cost, source-change frequency, and database impact; different projections may use different refresh strategies.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-133 — Incremental plus rebuildable
- **Grill source:** A6.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-AN-015
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Where scale or freshness warrants it, analytical aggregates may be maintained incrementally, but important projections must retain a deterministic full rebuild/reconciliation path so incremental state is never unrecoverable truth.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-134 — Streaming capability before streaming infrastructure
- **Grill source:** A6.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / DEFERRED_TO_ARCHITECTURE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-PERF-063
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Do not mandate Kafka or any dedicated streaming platform in AR-000. Lock event durability, schema, replay, ordering tolerance, observability, and scale requirements first; introduce dedicated streaming infrastructure only when volume, topology, or freshness needs justify it.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-135 — Server/domain authority for business analytics facts
- **Grill source:** A6.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; `§21J.15`; ARQ-AN-001, ARQ-AN-008
- **Source classification:** EXPLICIT_PLATFORM_AUTHORITY_RULE_REFINED_BY_GRILL
- **Requirement:** Important business analytical facts must originate from or reconcile to authoritative server/domain state. Client instrumentation is appropriate for genuinely client-observable interactions, but may not become the source of truth for payment, entitlement, refund, completion, safety, or similar governed business transitions.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-136 — Analytics failure does not undo committed business truth
- **Grill source:** A6.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-PERF-006, ARQ-PERF-038
- **Source classification:** EXPLICIT_PLATFORM_DEGRADATION_RULE_REFINED_BY_GRILL
- **Requirement:** Ordinary analytics collection/projection failure must not turn a successfully committed authoritative business operation into a false user-visible failure. Required analytical consequences need durable recovery/reconciliation rather than making analytics availability part of business commit success.
- **Primary downstream workstreams:** AR-005, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-137 — Durable analytics commit bridge
- **Grill source:** A6.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** ARQ-PERF-038; ARQ-PERF-099; `00_PLATFORM_v1.1.md §21K.6`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Required server-side analytical event/projection intent must be derived from committed authoritative state or established through an atomic durable transaction/outbox-equivalent bridge so the business commit boundary cannot silently lose the required analytical consequence.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_CONSISTENCY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-138 — Stable event identity and deduplication
- **Grill source:** A6.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-005–006; ARQ-PERF-026–027
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Events whose duplicate delivery matters require stable logical identity and deterministic deduplication/idempotent projection semantics so retries, replay, and recovery do not multiply one business event.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_DATA_QUALITY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-139 — Schema validation and quarantine
- **Grill source:** A6.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-005–006, ARQ-AN-017
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed analytical events must be validated against their event contract. Invalid events must be rejected or quarantined into an inspectable failure path and must not silently contaminate trusted analytical datasets.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DATA_QUALITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-140 — Sensitive failed-event handling
- **Grill source:** A6.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I`; ARQ-AN-018–020
- **Source classification:** EXPLICIT_PLATFORM_PRIVACY_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Failed-event/quarantine storage must be treated as potentially sensitive because malformed payloads may contain PII or health information in unexpected fields. It requires restricted access, retention, deletion, and observability controls appropriate to that risk.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-141 — Versioned event-schema evolution
- **Grill source:** A6.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-005–006; Product Law versioning doctrine
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Analytical event schemas require explicit compatible evolution/versioning. Semantic breaking changes create a new version and historical events remain interpretable under the schema/meaning applicable when they occurred.
- **Primary downstream workstreams:** AR-003, AR-006, AR-008
- **Blocking classification:** ARCHITECTURE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-142 — Fact versus interpretation in analytics history
- **Grill source:** A6.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I`; ARQ-AN-014–015
- **Source classification:** EXPLICIT_PLATFORM_HISTORY_AND_PRIVACY_RULE_REFINED_BY_GRILL
- **Requirement:** Where lawfully retained, preserve original analytical/source evidence separately from corrected normalisation or downstream interpretation. Do not silently rewrite raw history for convenience; deletion/anonymisation/retention obligations remain higher authority and may require removal.
- **Primary downstream workstreams:** AR-003, AR-007, AR-008
- **Blocking classification:** BLOCKING_HISTORY_INTEGRITY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-143 — Late/out-of-order convergence
- **Grill source:** A6.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-007, ARQ-AN-015; ARQ-PERF-041
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Analytics pipelines and read models must tolerate valid late and out-of-order inputs and converge deterministically using governed business/event timestamps, stable identities, authoritative versions, and reconciliation semantics appropriate to the source.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** DATA_QUALITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-144 — Replayable/rebuildable analytics
- **Grill source:** A6.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-015, ARQ-AN-017; recovery requirements
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Important derived analytical models must support safe replay, rebuild, or backfill from approved retained source evidence where feasible so derived analytics can be repaired without manual fabrication.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** RECOVERY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-145 — Idempotent backfill
- **Grill source:** A6.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** ARQ-AN-144; ARQ-PERF-026–027
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Replay/backfill transformations must be idempotent or deterministically replace the intended derived state/range so rebuilding cannot multiply users, events, income, conversions, or other metrics.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_DATA_INTEGRITY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-146 — Backfill auditability
- **Grill source:** A6.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.14 Audit logs`; ARQ-AN-014–015
- **Source classification:** EXPLICIT_PLATFORM_AUDIT_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Material analytical rebuilds/backfills must record sufficient provenance such as affected source/range, transformation or model version, initiator/automation identity, execution time, outcome, and material failures.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** BLOCKING_AUDIT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-147 — Governed data-quality test suite
- **Grill source:** A6.20
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-017; `00_PLATFORM_v1.1.md §21K.6`
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Trusted analytical models require risk-appropriate data-quality checks including, where relevant, required values, uniqueness, accepted values/ranges, referential relationships, duplicate detection, freshness, volume anomalies, and reconciliation against authoritative totals.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DATA_QUALITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-148 — Risk-classified data-quality response
- **Grill source:** A6.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-017; ARQ-PERF-004
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Data-quality failures must be classified by business risk. Critical trusted-model violations may block publication or mark the model unhealthy, while lower-severity anomalies may warn and continue under explicit degraded status rather than forcing one universal pipeline-stop rule.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** DATA_QUALITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-149 — Analytics freshness SLOs
- **Grill source:** A6.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** PERFORMANCE_TARGET / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-AN-016, ARQ-AN-106
- **Source classification:** EXPLICIT_PLATFORM_FRESHNESS_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Analytical sources and projections whose business usefulness depends on freshness must have explicit freshness/lag SLOs and alert when critical data exceeds the allowed window. Not every analytical surface must be realtime.
- **Primary downstream workstreams:** AR-008, AR-009
- **Blocking classification:** SLO_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-150 — Dataset/model/metric lineage
- **Grill source:** A6.23
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-002, ARQ-AN-014; AR-000 traceability doctrine
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed KPIs/read models must be traceable through transformation provenance to their material source events/datasets and transformation/model versions so impact analysis, audit, and incident diagnosis do not rely on undocumented institutional memory.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** GOVERNANCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-151 — Pragmatic lineage depth
- **Grill source:** A6.24
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** ARQ-AN-150
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Require practical dataset/model/job/metric provenance from the beginning, but do not require maximal automated column-level lineage for every field. Add finer-grained lineage where sensitivity, complexity, regulation, or scale makes it valuable.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-152 — Deletion propagation across analytical copies
- **Grill source:** A6.25
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.16 Analytics after deletion`; external processor/deletion rules
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Approved deletion/anonymisation/consent withdrawal must propagate to every applicable analytical projection, warehouse/lake copy, identifiable event store, cache/index, export, and external processor. Only legally permitted irreversible aggregates may remain.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_DELETION
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-153 — Deletion-safe replay/restore
- **Grill source:** A6.26
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21I.16`; restore/deletion rules
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT_REFINED_BY_GRILL
- **Requirement:** Replay, backfill, restoration, or disaster recovery must honour deletion/suppression/tombstone state so analytics cannot reconstruct an identity Product Law has deleted. Retained finance, security, or other restricted records may not be used to rebuild the deleted analytics identity.
- **Primary downstream workstreams:** AR-003, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_DELETION
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-154 — CDC-compatible, not CDC-first
- **Grill source:** A6.27
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED / DEFERRED_TO_ARCHITECTURE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; PostgreSQL platform direction
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Do not require PostgreSQL logical replication/CDC in MVP. Keep authoritative schemas and deployment choices compatible with a future CDC/logical-replication path where practical, and introduce it only when independent analytical replication or streaming is justified.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-155 — CDC resource/lag observability
- **Grill source:** A6.28
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** ARQ-AN-154; reliability/observability requirements
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** If CDC/logical replication is introduced, monitor consumer lag, replication-slot state, retained WAL/storage growth, failures, and recovery. A stalled analytics consumer must not silently exhaust or endanger production PostgreSQL.
- **Primary downstream workstreams:** AR-003, AR-008, AR-009
- **Blocking classification:** OPERATIONS_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-156 — Warehouse remains downstream
- **Grill source:** A6.29
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Any future warehouse or analytical store remains downstream analytical/read authority only; it never becomes operational authority for payments, entitlements, safety, consent, capacity, or other transactional business truth.
- **Primary downstream workstreams:** AR-003, AR-005, AR-008
- **Blocking classification:** BLOCKING_AUTHORITY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-157 — No silent BI-to-OLTP mutation
- **Grill source:** A6.30
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** ARQ-AN-001; Product Law action/authority model
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Analytical transformations must not silently write derived results back into authoritative business state. Any analytics-to-product feedback loop must enter through a separately authorised domain action with explicit semantics, validation, privacy, and audit rules.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-008
- **Blocking classification:** BLOCKING_AUTHORITY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-158 — Semantic portability across analytical storage
- **Grill source:** A6.31
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** ARQ-AN-002, ARQ-AN-014; ARQ-AN-128–157
- **Source classification:** DERIVED_ACCEPTED_GRILL_REQUIREMENT
- **Requirement:** Governed metric, funnel, cohort, and income semantics must remain stable above the physical analytics storage/compute technology so moving from PostgreSQL projections to another analytical store does not itself redefine KPI meaning.
- **Primary downstream workstreams:** AR-003, AR-008
- **Blocking classification:** GOVERNANCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-159 — Analytics pipeline observability
- **Grill source:** A6.32
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-AN-017; ARQ-PERF-023
- **Source classification:** EXPLICIT_PLATFORM_OBSERVABILITY_CONCEPT_REFINED_BY_GRILL
- **Requirement:** Material analytics ingestion/transformation pipelines must expose sufficient observability for throughput, lag/freshness, failures/quarantine, duplicate indicators where measurable, retries, processing duration, backlog, source-to-model reconciliation, and CDC/replication health where used.
- **Primary downstream workstreams:** AR-008, AR-009
- **Blocking classification:** OBSERVABILITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-160 — Representative analytics performance testing
- **Grill source:** A6.33
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Exact Product Law source:** ARQ-PERF-003, ARQ-PERF-021–022; `00_PLATFORM_v1.1.md §21K.6`
- **Source classification:** EXPLICIT_PLATFORM_PERFORMANCE_RULE_REFINED_BY_GRILL
- **Requirement:** Analytics architecture must be tested with representative data volumes/cardinalities, refresh/rebuild workloads, concurrent dashboard usage, large date ranges, exports, backfills, pipeline lag, recovery, and measurable OLTP impact where applicable.
- **Primary downstream workstreams:** AR-008, AR-009
- **Blocking classification:** RELEASE_GATE_INPUT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-161 — Overarching analytics architecture doctrine
- **Grill source:** A6.34
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21K.6`; ARQ-AN-001–160
- **Source classification:** EXPLICIT_PLATFORM_REQUIREMENTS_CONSOLIDATED_BY_GRILL
- **Requirement:** Analytics is a rebuildable downstream projection system. Begin with efficient PostgreSQL read models/materialised views where sufficient; isolate analytics from OLTP; use governed, deduplicable, replayable events and deterministic projections; test quality, freshness and reconciliation; maintain provenance; propagate privacy/deletion; and introduce CDC, dedicated streaming, or an independent warehouse only when evidence justifies them without changing business metric semantics.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007, AR-008, AR-009
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING



## 8D.9 Round A7 — Targets, Surveys, Outcome Measurement, Outlooks & Decision Thresholds

### ARQ-AN-162 — Targets bind to governed metric semantics
- **Grill source:** A7.1
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23 Pilot success criteria` and `§21L.24 Go/No-Go and rollback authority`
- **Source classification:** EXPLICIT_PRODUCT_TARGETS_HARDENED_BY_GRILL
- **Requirement:** Every governed target must reference a governed metric/version and define threshold, population, period/window, comparison operator, and effective version. A target may not float independently from the metric semantics it evaluates.
- **Primary downstream workstreams:** AR-002, AR-004, AR-008
- **Blocking classification:** DECISION_EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-163 — Target denominators are explicit
- **Grill source:** A7.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23`
- **Source classification:** EXPLICIT_PRODUCT_TARGET_DENOMINATORS_HARDENED_BY_GRILL
- **Requirement:** Every target must state the eligible denominator/population and exclusions. Terms such as starters, eligible purchasers, delivered plans, surveyed participants, or exposed experiment units may not be silently substituted for one another.
- **Primary downstream workstreams:** AR-002, AR-004
- **Blocking classification:** METRIC_SEMANTICS_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-164 — Target definitions are versioned
- **Grill source:** A7.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23 Pilot success criteria` and `§21L.24 Go/No-Go and rollback authority`
- **Source classification:** DERIVED_GOVERNANCE_REQUIREMENT
- **Requirement:** Material target-definition changes require a new governed version. Historic reporting must state whether it is evaluated against the target effective at the time or recalculated under a later version; versions may not be silently mixed.
- **Primary downstream workstreams:** AR-002, AR-008
- **Blocking classification:** METRIC_VERSIONING_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-165 — Integrity gates are distinct from ordinary targets
- **Grill source:** A7.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23`
- **Source classification:** EXPLICIT_PRODUCT_INTEGRITY_GATES_HARDENED_BY_GRILL
- **Requirement:** Hard integrity, safety, security, privacy, payment, entitlement, and reproducibility gates are not ordinary performance targets and do not receive discretionary tolerance merely because non-integrity targets use percentages or error budgets.
- **Primary downstream workstreams:** AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-166 — Missed non-integrity targets trigger governed decisions
- **Grill source:** A7.5
- **Accepted option:** C
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23`
- **Source classification:** EXPLICIT_PRODUCT_DECISION_FLOW
- **Requirement:** Missing a non-integrity pilot target triggers a governed `proceed`, `iterate`, `repeat_pilot`, or `pause` decision supported by evidence and accountable ownership; it does not automatically terminate or expand the product and the target may not be retrospectively changed to manufacture success.
- **Primary downstream workstreams:** AR-002, AR-008
- **Blocking classification:** RELEASE_DECISION_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-167 — Authority-separated Go/No-Go decisions
- **Grill source:** A7.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.24`
- **Source classification:** EXPLICIT_PRODUCT_AUTHORITY_BOUNDARY
- **Requirement:** Commercial, product, technical, clinical/safety, security/privacy, and other blocker authorities remain separated according to Product Law. A strong result in one dimension cannot waive a blocker owned by another authority.
- **Primary downstream workstreams:** AR-002, AR-004, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-168 — Target status is interpretable in decision surfaces
- **Grill source:** A7.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23 Pilot success criteria` and `§21L.24 Go/No-Go and rollback authority`
- **Source classification:** DERIVED_DECISION_SUPPORT_REQUIREMENT
- **Requirement:** Where target status is decision-relevant, the surface must expose enough context to interpret it, including actual value, target, metric version, denominator/scope, period, freshness, and target/gate class as applicable.
- **Primary downstream workstreams:** AR-002, AR-004
- **Blocking classification:** DECISION_SUPPORT_REQUIREMENT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-169 — Survey KPI tracks invitation and response populations
- **Grill source:** A7.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23 Value target`
- **Source classification:** EXPLICIT_SURVEY_TARGET_HARDENED_BY_GRILL
- **Requirement:** For a survey-derived KPI, retain the applicable eligible, invited, responded, and completed populations so the reported denominator and response rate remain interpretable.
- **Primary downstream workstreams:** AR-002, AR-004, AR-007
- **Blocking classification:** SURVEY_EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-170 — KPI-driving survey questions are versioned
- **Grill source:** A7.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23 Value target`; multilingual/content versioning requirements elsewhere in Platform Law
- **Source classification:** DERIVED_SURVEY_GOVERNANCE_REQUIREMENT
- **Requirement:** Survey questions that drive governed KPIs require stable identity/version, exact wording, response scale, language/version, and applicable population. Material wording or scale changes create a new version rather than silently redefining historic responses.
- **Primary downstream workstreams:** AR-002, AR-004, AR-006
- **Blocking classification:** SURVEY_VERSIONING_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-171 — Survey results preserve methodology context
- **Grill source:** A7.10
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23 Value target`
- **Source classification:** DERIVED_SURVEY_EVIDENCE_REQUIREMENT
- **Requirement:** Where material, governed survey results preserve/report the question/version, population, respondent count, field period, mode, response rate, exclusions, and weighting methodology if any.
- **Primary downstream workstreams:** AR-002, AR-004, AR-008
- **Blocking classification:** SURVEY_EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-172 — Respondent results are not silently generalized
- **Grill source:** A7.11
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23 Value target`
- **Source classification:** DERIVED_SURVEY_VALIDITY_REQUIREMENT
- **Requirement:** A percentage measured among survey respondents must be reported as such and may not silently be represented as the percentage of all participants. Any broader inference requires explicit methodological support and suitable caveats.
- **Primary downstream workstreams:** AR-002, AR-004
- **Blocking classification:** ANALYTICS_TRUTH_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-173 — Participant-value surveys are not medical efficacy claims
- **Grill source:** A7.12
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23` explicitly states pilot thresholds are not medical efficacy claims
- **Source classification:** EXPLICIT_PRODUCT_SAFETY_BOUNDARY
- **Requirement:** Participant-reported usefulness, clarity, relevance, satisfaction, or similar value outcomes remain decision-support/product measures and must not be represented as evidence of medical or clinical efficacy.
- **Primary downstream workstreams:** AR-002, AR-004, AR-006
- **Blocking classification:** SAFETY_CLAIM_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-174 — Completion outlook is a derived estimate
- **Grill source:** A7.13
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22 Operational dashboards` and `§21H.20 Completion and certificate`
- **Source classification:** EXPLICIT_DASHBOARD_CAPABILITY_BOUND_BY_PRODUCT_TRUTH
- **Requirement:** `completion_outlook` is a derived decision-support estimate of future completion/recovery risk. It is not an authoritative programme status and does not replace versioned completion criteria or authoritative completion outcomes.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004
- **Blocking classification:** ANALYTICS_NON_AUTHORITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-175 — Completion outlook uses the simplest adequate model
- **Grill source:** A7.14
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22` plus AR-000 no-speculative-complexity doctrine
- **Source classification:** DERIVED_EVIDENCE_GATED_REQUIREMENT
- **Requirement:** Begin completion-outlook capability with the simplest transparent governed rule/heuristic/statistical model that satisfies the decision need. More complex statistical or machine-learning approaches require evidence that their added complexity provides material value.
- **Primary downstream workstreams:** AR-002, AR-009
- **Blocking classification:** EVIDENCE_GATED
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-176 — Predictive models require explicit governance
- **Grill source:** A7.15
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22` completion outlook plus privacy/safety/versioning law
- **Source classification:** DERIVED_MODEL_GOVERNANCE_REQUIREMENT
- **Requirement:** A predictive/outlook model requires an explicit purpose, model/rule version, approved input features, evaluation/calibration method where applicable, performance measures, limitations, owner, deployment/effective date, and monitoring/review process.
- **Primary downstream workstreams:** AR-002, AR-004, AR-007, AR-008
- **Blocking classification:** MODEL_GOVERNANCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-177 — Predictive quality uses problem-appropriate validation
- **Grill source:** A7.16
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22` completion outlook
- **Source classification:** DERIVED_MODEL_VALIDITY_REQUIREMENT
- **Requirement:** Predictive quality must use metrics appropriate to the actual decision problem and prevalence. Validation must use suitable holdout/out-of-sample evidence where applicable; no single generic accuracy percentage is universally sufficient.
- **Primary downstream workstreams:** AR-002, AR-008
- **Blocking classification:** MODEL_VALIDITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-178 — Predictive uncertainty is not hidden
- **Grill source:** A7.17
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22` completion outlook
- **Source classification:** DERIVED_MODEL_TRANSPARENCY_REQUIREMENT
- **Requirement:** Where predictive outputs are probabilistic or materially uncertain, preserve and present suitable uncertainty/confidence semantics and do not present estimates as certain observed facts.
- **Primary downstream workstreams:** AR-002, AR-004
- **Blocking classification:** DECISION_SUPPORT_REQUIREMENT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-179 — Outlook cannot independently alter protected business truth
- **Grill source:** A7.18
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.20`, `§21C` safety rules, and `§21K.6` analytics non-authority
- **Source classification:** EXPLICIT_AUTHORITY_BOUNDARIES_CONSOLIDATED_BY_GRILL
- **Requirement:** A completion outlook or other predictive analytical signal may support programme operations/recovery outreach but may not independently alter entitlement, safety, clinical status, authoritative completion, payment, or other protected business state unless a separately governed authorised domain action explicitly permits it.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-180 — Modelled estimates and observed facts stay distinct
- **Grill source:** A7.19
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21H.22` and accepted A4 observed-versus-modelled doctrine
- **Source classification:** DERIVED_ANALYTICS_TRUTH_REQUIREMENT
- **Requirement:** Forecasts, outlooks, and other modelled estimates must be visibly and semantically distinguishable from observed/reconciled facts, including model/version where material.
- **Primary downstream workstreams:** AR-002, AR-004
- **Blocking classification:** ANALYTICS_TRUTH_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-181 — Built-in A/B/n experimentation is a required platform capability
- **Grill source:** A7.20 — USER AMENDMENT TO PRIOR RECOMMENDATION
- **Accepted option:** USER_OVERRIDE: BUILT_IN_REQUIRED
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** LOCKED_PRODUCT_CAPABILITY_REQUIREMENT
- **Exact Product Law source:** No existing Product Law section currently mandates a general experimentation platform; explicit user decision on 2026-08-16 adds this capability
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** The platform must include a first-party experimentation capability for controlled A/B/n testing of two or more variants, including web/page experiences and email/message variants. Experimentation is a built-in product/platform requirement, not merely a future optional capability.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-006, AR-008, AR-009
- **Blocking classification:** UPSTREAM_PRODUCT_LAW_AMENDMENT_REQUIRED / ARCHITECTURE_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING
- **Required governance follow-up:** Amend Product Law/DEC explicitly before AR-000-A closure/freeze to add first-party experimentation as a governed platform capability and preserve this user decision as the source of the amendment.

### ARQ-AN-182 — External benchmarks remain contextual rather than automatic targets
- **Grill source:** A7.21
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §19` and `§21L.23` define internal targets; no external-benchmark mandate exists
- **Source classification:** DERIVED_TARGET_GOVERNANCE_REQUIREMENT
- **Requirement:** External industry/vendor benchmarks may provide context but do not silently become platform targets. Internal governed targets remain explicit business/Product Law decisions.
- **Primary downstream workstreams:** AR-002, AR-008
- **Blocking classification:** TARGET_GOVERNANCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-183 — Overarching target/outcome decision doctrine
- **Grill source:** A7.22
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21L.23–24`; `§21H.22`; ARQ-AN-162–182
- **Source classification:** EXPLICIT_PRODUCT_DECISION_MODEL_CONSOLIDATED_BY_GRILL
- **Requirement:** Decision-support analytics preserves the chain `governed metric → governed target/model/experiment → trustworthy evidence → authorised decision`. Hard integrity gates remain non-waivable outside their authority; non-integrity targets support deliberate decisions; survey outcomes retain methodological context; predictive outlooks remain versioned estimates rather than business truth; experimentation evidence remains decision support rather than automatic Product Law.
- **Primary downstream workstreams:** AR-002, AR-004, AR-008, AR-009
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING


## 8D.10 Built-in Experimentation Capability — User Amendment / Expansion

> **Governance note:** The earlier proposed A7.20 recommendation (“do not make experimentation an AR-000 requirement today”) was **not accepted as written**. On 2026-08-16 the user explicitly required first-party A/B/n testing for pages and emails. Because A7 had not yet been appended to this register, ARQ-AN-181 records the accepted amended position directly. This capability also requires explicit upstream Product Law/DEC propagation before AR-000-A closes.

### ARQ-AN-184 — Experiment object supports control plus one or more treatment variants
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** The experimentation model must support a control plus at least one treatment and must be extensible to A/B/n tests with more than two variants. Each experiment has a stable identity, explicit owner, hypothesis/purpose, lifecycle state, eligible audience, traffic allocation, primary decision metric(s), guardrail metric(s), start/end/readout semantics, and immutable versioned configuration evidence.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-185 — Page experiment duplicate-and-edit authoring workflow
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_PRODUCT_UX_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** For page experiments, an authorised editor must be able to choose an eligible published page/experience, create an experiment, duplicate the control into one or more variant drafts, and manually change approved content/design elements such as copy, colour, layout, images, hero treatment, CTA, or section composition before review/activation. The experiment system must preserve which exact page/variant version each participant saw.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-186 — Public URLs remain clean, semantic and canonically stable
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Experiment assignment must not require user-visible experiment IDs, variant IDs, random query strings, or duplicate public URLs. The normal clean semantic URL remains the canonical user-facing URL wherever technically feasible; if temporary alternate URLs are ever required, SEO/canonical handling must follow current search-engine testing guidance so variants do not become competing canonical pages.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** SEO_AND_ROUTING_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-187 — Experiment assignment is deterministic and sticky for the selected randomization unit
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Each experiment must declare its randomization unit (normally stable user/account identity where available, otherwise an approved anonymous stable identifier or another justified unit). Assignment must be pseudo-random, deterministic/sticky for that unit for the experiment lifetime, and reproducible enough to audit allocation without re-randomising users on every request/session.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-188 — Anonymous-to-known identity transitions preserve experimental validity
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** The architecture must define how anonymous visitors who later authenticate map to experiment assignment so identity stitching does not cause silent treatment crossover, double-counting, or biased results. The chosen rule must be explicit per experiment/use case and remain privacy/consent compliant.
- **Primary downstream workstreams:** AR-002, AR-004, AR-007, AR-008
- **Blocking classification:** EXPERIMENT_VALIDITY_AND_PRIVACY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-189 — Eligibility and traffic allocation are explicit and versioned
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Each experiment must define who is eligible, what percentage of eligible traffic enters the experiment, and the intended variant allocation. Allocation changes during a running experiment require governed semantics and audit history because they can affect interpretation.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-190 — Exposure is logged when the intervention is actually experienced
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Experiment analysis must be based on governed exposure records representing that the randomization unit actually received/saw the applicable treatment where practical, not merely that it was theoretically eligible. Exposure records require stable experiment/variant identity, unit identity according to privacy rules, and exposure time.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-191 — Experiment metrics are governed before activation
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Before activation, an experiment must bind to governed primary outcome metric(s), optional secondary diagnostics, and guardrail metrics. Primary metrics answer the hypothesis; guardrails protect against material regressions. Post-hoc exploratory cuts may generate future hypotheses but cannot be silently promoted to the original success criterion.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-192 — Sales, conversion and time-to-conversion use authoritative business facts
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Experiments may compare sales/conversion rate, revenue/income by governed type, funnel progression, and time-to-conversion, but business conversions and monetary values must reconcile to authoritative platform payment/commercial facts rather than browser-only events. The experiment layer assigns analytical credit; it does not create sales, payments, entitlements, or income.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008
- **Blocking classification:** ANALYTICS_AND_FINANCIAL_TRUTH_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-193 — Experiment timing metrics preserve exposure-to-outcome semantics
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Where conversion speed matters, preserve the relevant first-exposure timestamp and authoritative outcome timestamp so time-to-conversion can be compared across variants using an explicit window and censoring/eligibility rule rather than arbitrary session duration.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-194 — Experiments require predeclared statistical design and power expectations
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Before a decision-bearing experiment starts, define an approved statistical methodology and, where applicable, target significance/error level, statistical power, baseline estimate, minimum detectable effect, expected sample/exposure requirement, target duration/readout rule, and practical minimum duration needed to cover relevant usage cycles. Underpowered/inconclusive experiments may not be represented as evidence of no effect.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** STATISTICAL_VALIDITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-195 — Naive repeated peeking is prohibited
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** The experiment engine must not allow ordinary fixed-horizon significance tests to be repeatedly checked and stopped opportunistically as if each peek were independent. If continuous/early decision monitoring is supported, use an approved sequential-testing or equivalent methodology that controls the relevant false-positive risk and records the method/version.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** STATISTICAL_VALIDITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-196 — Multiple variants and multiple decision metrics require false-positive control
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** When an experiment evaluates multiple treatment variants and/or multiple decision metrics, the statistical method must explicitly address the increased false-positive risk through an approved correction/control strategy or an experiment design that otherwise accounts for multiplicity.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** STATISTICAL_VALIDITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-197 — Sample-ratio mismatch is a first-class experiment health check
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** The platform must compare observed experiment allocation with expected allocation and flag material sample-ratio mismatch or equivalent assignment/exposure anomalies. A material unexplained SRM blocks a conclusive winner decision until investigated/resolved or explicitly classified under a governed statistical exception.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** STATISTICAL_VALIDITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-198 — Experiment results include effect size and uncertainty, not winner labels alone
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Results must expose the underlying variant sample/exposure counts, primary metric values, absolute/relative effect where applicable, uncertainty/confidence or posterior semantics according to the approved method, statistical status, and guardrail outcomes. `winner`/`loser` labels alone are insufficient evidence.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-199 — Experiments have governed lifecycle, pause, stop and invalidation states
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Experiments require explicit lifecycle states such as draft/review/ready/running/paused/stopped/concluded/invalidated/archived (exact names later). Operators must be able to halt harmful or broken experiments promptly; stopping or invalidating an experiment must preserve accumulated evidence and the reason rather than deleting history.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENT_OPERATION_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-200 — Email/message A/B/n testing is built in
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_PRODUCT_CAPABILITY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** The first-party experimentation capability must support governed A/B/n testing of eligible email/message campaigns, including manually authored variants of appropriate elements such as subject line, content/body, CTA/layout, sender presentation, and send timing where the communication channel and consent/quiet-hour rules permit. Recipient assignment must be random/sticky for the campaign experiment and messaging consent, suppression, idempotency, and delivery rules remain authoritative.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005, AR-006, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_AND_MESSAGING_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-201 — Email experiment outcomes distinguish delivery and downstream conversion
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Email experiments must distinguish send/accepted/delivered/bounced/open/click/reply or other channel signals from authoritative downstream business outcomes such as verified purchase. Where privacy/platform restrictions make some engagement signals unreliable or unavailable, the dashboard must disclose that limitation rather than manufacture precision.
- **Primary downstream workstreams:** AR-002, AR-004, AR-006, AR-008
- **Blocking classification:** MESSAGING_ANALYTICS_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-202 — Experiment configuration and final result record are immutable evidence
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Once an experiment starts, preserve an immutable/auditable record of the activated experiment version, variants, assignment rules, metric definitions/versions, statistical method/settings, exposures, data-quality/health warnings, stop/readout conditions, final computed result snapshot, conclusion/decision, decision owner, and timestamps. Corrections or re-analysis create additive/superseding result versions rather than rewriting the original evidence. PostgreSQL remains durable authority for this experiment-history record.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007, AR-008
- **Blocking classification:** EXPERIMENT_EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-203 — Experiment archive supports future design and funnel decisions
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_PRODUCT_UX_REQUIREMENT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Authorised users must be able to search and compare historical experiments by page/flow/campaign, tested hypothesis, variants, metrics, outcome, date, and decision so future design/flow/content work can use accumulated evidence. Historic experiments remain read-only evidence after conclusion except through explicit additive annotations/re-analysis versions.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENTATION_CAPABILITY_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-204 — Experimentation remains privacy- and consent-constrained
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** Experiment assignment, exposure logging, analysis, and message variants must obey current consent/purpose/privacy/deletion rules. Experimentation is not permission to fingerprint users, reconstruct deleted identities, reuse sensitive health/journal data for marketing experiments, or retain identifiable experiment data beyond approved lifecycle rules.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** PRIVACY_AND_CONSENT_GATE
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING

### ARQ-AN-205 — Experiments may not weaken protected safety, legal, payment or entitlement guarantees
- **Decision source:** Explicit user experimentation requirement on 2026-08-16 following A7 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** No current explicit Product Law mandate; new user-locked capability requiring Product Law/DEC propagation. Related existing sources: `00_PLATFORM_v1.1.md §21H.23 Analytics and repeat participation`, `§21K.6 Analytics`, `§21I` privacy/deletion, and `§21L.23–24` decision thresholds/authority.
- **Source classification:** NEW_PRODUCT_CAPABILITY_LOCKED_DURING_AR_000
- **Requirement:** The experimentation system may test presentation, content, layout, funnel and other approved product choices, but may not randomly weaken mandatory safety messages, consent/legal notices, accessibility obligations, security controls, payment verification, entitlement correctness, clinical/safety rules, or other hard Product Law invariants. Any experiment touching a protected boundary requires the same upstream authority that owns that rule and may not waive it.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005, AR-006, AR-008
- **Blocking classification:** BLOCKING_INVARIANT
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING


### ARQ-AN-206 — Experiment assignment uses a reusable deterministic assignment primitive behind the Experiment domain
- **Decision source:** Explicit user acceptance on 2026-08-16 of the FunWithFlags/Bandera experimentation-boundary recommendation
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** No current explicit implementation-mechanism mandate; derives from the user-locked first-party experimentation capability in `ARQ-AN-181` and `ARQ-AN-184`–`ARQ-AN-205`. Product Law propagation for the experimentation capability remains pending.
- **Source classification:** DERIVED_ACCEPTED_ARCHITECTURE_REQUIREMENT / EXPERIMENTATION_ASSIGNMENT_BOUNDARY
- **Requirement:** The first-party Experiment domain must use a reusable deterministic feature-flag/variant-assignment primitive for treatment allocation rather than scattering ad-hoc experiment-routing logic through product code. The assignment primitive is subordinate to the Experiment domain and must not become the authority for experiment hypothesis, eligibility, exposure evidence, metrics, statistical analysis, immutable results, or decisions.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** ARCHITECTURE_MECHANISM_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-207 — Experiment assignment is isolated behind a platform-owned adapter/behaviour boundary
- **Decision source:** Explicit user acceptance on 2026-08-16 of the FunWithFlags/Bandera experimentation-boundary recommendation
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit implementation-mechanism mandate; derives from the user-locked first-party experimentation capability in `ARQ-AN-181` and the maintainable/rebuildable architecture doctrine in A6.
- **Source classification:** DERIVED_ACCEPTED_ARCHITECTURE_REQUIREMENT / PORTABILITY_AND_DRIFT_CONTROL
- **Requirement:** Product/application code must depend on a platform-owned Experiment assignment interface/behaviour rather than directly coupling business flows to a third-party feature-flag library API. The concrete assignment implementation must therefore be replaceable without redefining experiment identity, exposure records, metric semantics, historical evidence, or dashboard/reporting contracts.
- **Primary downstream workstreams:** AR-002, AR-005, AR-008
- **Blocking classification:** ARCHITECTURE_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-208 — Assignment must support stable mutually exclusive weighted A/B/n allocation
- **Decision source:** Explicit user acceptance on 2026-08-16 of the FunWithFlags/Bandera experimentation-boundary recommendation
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** No current explicit implementation-mechanism mandate; derives from `ARQ-AN-181`, `ARQ-AN-184`, `ARQ-AN-187`, and `ARQ-AN-189`.
- **Source classification:** DERIVED_ACCEPTED_ARCHITECTURE_REQUIREMENT / EXPERIMENT_VALIDITY
- **Requirement:** The assignment mechanism must support deterministic, sticky, mutually exclusive weighted allocation across a control and one or more treatment variants (A/B/n). Independent boolean flags are insufficient by themselves unless the platform adapter adds a deterministic mutually-exclusive bucketing layer. Time/random-per-request percentage gates must not be used for experiment treatment assignment because the same experimental unit must not flip variants across requests merely due to repeated evaluation.
- **Primary downstream workstreams:** AR-002, AR-005, AR-009
- **Blocking classification:** EXPERIMENT_VALIDITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-209 — FunWithFlags, Bandera and equivalent mechanisms are architecture candidates, not Product Law
- **Decision source:** Explicit user acceptance on 2026-08-16 of the FunWithFlags/Bandera experimentation-boundary recommendation
- **Status:** ACCEPTED
- **Strength:** EVIDENCE_GATED
- **Exact Product Law source:** No current Product Law library mandate; the experimentation capability itself is user-locked and awaits upstream propagation.
- **Source classification:** ARCHITECTURE_CANDIDATE_EVALUATION / NO_PREMATURE_LIBRARY_LOCK
- **Requirement:** Architecture must evaluate an Elixir-native assignment mechanism against the locked experimentation requirements before selecting the concrete implementation. At minimum, FunWithFlags and Bandera (or a documented equivalent/custom deterministic bucketing adapter if those fail the proof) must be assessed for stable A/B/n assignment, persistence/reconstruction, multi-node behaviour, cache/failure semantics, operational maturity, observability, privacy/identity handling, and dependency risk. The chosen library is an implementation mechanism beneath the platform-owned assignment boundary and may be replaced without changing Experiment-domain law.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** ARCHITECTURE_PROOF_GATE
- **Architecture status:** ARQ_LOCKED / CANDIDATE_EVALUATION_PENDING / ARC_PENDING


## 8D.11 Formal Analytics Closure Audit — AC.1–AC.10 accepted

### ARQ-AN-210 — Immutable experiment knowledge is compatible with participant deletion
- **Closure source:** AC.2
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.md §21K.6A`; `§21I.16`; DEC-293
- **Source classification:** PRODUCT_LAW_AND_PRIVACY_BOUNDARY_HARDENED_BY_CLOSURE
- **Requirement:** Preserve the experiment definition, activated variant versions, methodology, aggregate result snapshot, conclusion, decision and appropriately de-identified institutional evidence as durable experiment history. Identifiable participant-level assignment/exposure evidence remains subject to consent, retention, deletion and anonymisation law. “Immutable experiment history” must never be interpreted as permission to retain a deleted participant identity indefinitely.
- **Primary downstream workstreams:** AR-003, AR-004, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AND_HISTORY_INTEGRITY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-211 — Allocation changes cannot silently rebucket already exposed units
- **Closure source:** AC.3
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.md §21K.6A`; DEC-293; ARQ-AN-187, ARQ-AN-189
- **Source classification:** EXPERIMENT_VALIDITY_HARDENING
- **Requirement:** Changing traffic allocation during an experiment must preserve the historical treatment of already exposed experimental units wherever technically possible. A material change that would rebucket already exposed units requires an explicit experiment version/reset/invalidation decision; participants may not silently flip treatment because allocation percentages changed.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENT_VALIDITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-212 — Concurrent experiments require interaction and mutual-exclusion governance
- **Closure source:** AC.4
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.md §21K.6A`; DEC-293
- **Source classification:** EXPERIMENT_VALIDITY_HARDENING
- **Requirement:** Every experiment must declare an interaction/isolation policy. Experiments that can materially contaminate one another on the same surface, audience or funnel must support explicit mutual exclusion/layering or another justified isolation design. Clearly orthogonal experiments may run concurrently, but relevant cross-exposure must be recorded sufficiently to detect or analyse material interaction.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENT_INTERACTION_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-213 — Experiment delivery uses a variant-safe cache contract
- **Closure source:** AC.5
- **Accepted option:** B
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.md §21K.6A`; DEC-293; ARQ-AN-186, ARQ-AN-187, ARQ-AN-208
- **Source classification:** SEO_CACHE_AND_EXPERIMENT_VALIDITY_HARDENING
- **Requirement:** When multiple experiment variants share one canonical public URL, shared/browser/CDN/application caching must not serve one unit's treatment as another unit's treatment. Architecture must either bypass shared full-page caching for experiment-sensitive HTML or partition cache entries by a safe internal variant/assignment dimension. Cache loss, purge, deployment or invalidation must not silently switch an already exposed unit's treatment. Static/public assets may remain normally cacheable.
- **User refinement:** SEO and clean URLs remain a priority; cache segmentation must not require exposing treatment identity in the normal public URL.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** CACHE_CORRECTNESS_AND_SEO_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-214 — Public URL parameters are not the normal experiment-assignment or cache-partition contract
- **Closure source:** AC.5 + explicit user URL/cache refinement on 2026-08-16
- **Accepted option:** REFINED_B
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Strength:** MANDATORY_REQUIREMENT / SEO_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.md §21K.6A`; DEC-293
- **Source classification:** USER_REFINEMENT / SEO_CACHE_ARCHITECTURE_REQUIREMENT
- **Requirement:** Normal participant treatment assignment must keep the base URL clean, semantic and canonical and must not rely on user-visible `experiment`, `variant`, random-bucket or equivalent query parameters. The delivery/cache layer may derive an internal cache-key dimension from the sticky assignment (for example through a controlled cookie, server-side assignment identity, internal header, edge metadata or synthetic internal cache-key rewrite) without changing the browser URL. Legitimate campaign-attribution parameters such as governed UTM values, authenticated/signed preview/debug controls, or temporary alternate test URLs may exist under separate rules; they do not define normal treatment identity. If alternate test URLs are ever necessary, canonical/temporary-redirect handling must preserve the base page as the preferred canonical.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** SEO_ROUTING_AND_CACHE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-215 — Experiment decision populations exclude or classify invalid/non-human traffic before analysis
- **Closure source:** AC.6
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.md §21K.6A`; DEC-293; ARQ-AN-189
- **Source classification:** EXPERIMENT_DATA_QUALITY_HARDENING
- **Requirement:** Each experiment defines its decision population and traffic-quality rules. Known internal QA/test users, monitoring/synthetic traffic, bots or other invalid experimental units must be excluded or separately classified where appropriate before decision analysis. Exclusion rules are governed/auditable and may not be selectively changed post hoc to manufacture a winner.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-008
- **Blocking classification:** EXPERIMENT_DATA_QUALITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-AN-216 — Assignment-mechanism failure degrades safely without false exposure or treatment switching
- **Closure source:** AC.7
- **Accepted option:** B
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.md §21K.6A`; DEC-293; ARQ-AN-187, ARQ-AN-206–209
- **Source classification:** EXPERIMENT_FAILURE_RECOVERY_HARDENING
- **Requirement:** Experiment assignment must be safely reconstructable/deterministic. Cache, node, adapter or assignment-library failure may not silently flip a known experimental unit. If a safe treatment cannot be established, serve the governed safe/default experience, do not record a fabricated exposure, expose degraded experiment health, and recover/reconcile without weakening authoritative business flows. Experiment-assignment availability must not unnecessarily block unrelated payment, entitlement, authentication or safety operations.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** EXPERIMENT_FAILURE_RECOVERY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### PROP-AN-001 — Product Law v1.2 propagation completed for first-party experimentation
- **Closure source:** AC.1
- **Accepted option:** B
- **Status:** COMPLETE
- **Propagation:** `00_PLATFORM_v1.2.md §21K.6A` + `01_DECISIONS_v1.2.md DEC-293` + `02_OPEN_WORK_v1.2.md OQ-040/FLOW-12`.
- **Effect:** The user-locked experimentation capability previously marked `PRODUCT_LAW_PROPAGATION_PENDING` now has an authoritative upstream home. Original ARQ entries are retained unchanged as historical evidence of the pre-propagation state.

### PROP-PAY-001 — Product Law v1.2 propagation completed for Paystack launch gateway
- **Closure source:** AC.1
- **Accepted option:** B
- **Status:** COMPLETE
- **Propagation:** `00_PLATFORM_v1.2.md §21A.12` + `01_DECISIONS_v1.2.md DEC-292`; `DEC-047` retained and marked superseded in v1.2.
- **Effect:** Paystack is authoritative Product Law as the first/launch gateway while OQ-004 remains the provider-behaviour validation gate.

### ROUTE-AN-001 — Analytics topology-sensitive ARQs also route into AR-001
- **Closure source:** AC.8
- **Accepted option:** B
- **Status:** ACCEPTED
- **Requirement:** AR-001 System Shape & Runtime Topology is an additional downstream consumer for Analytics requirements that materially affect deployment/runtime topology, especially ARQ-AN-128–134, ARQ-AN-137, ARQ-AN-144, ARQ-AN-149, ARQ-AN-154–161, ARQ-AN-184, ARQ-AN-187–190, ARQ-AN-199, ARQ-AN-202, and ARQ-AN-206–216. This routing addendum supplements original workstream metadata without rewriting or renumbering prior ARQs.

### INTERP-AN-001 — Concrete experiment-assignment library selection remains Architecture work
- **Closure source:** AC.9
- **Accepted option:** B
- **Status:** ACCEPTED
- **Interpretation:** AR-000-A is allowed to close without selecting FunWithFlags, Bandera or another candidate. ARQ-AN-206–209 define the required boundary/proof. Architecture selects the concrete mechanism only after the candidate proof; the mechanism is not Product Law.

### AR-000-A Formal Closure Verdict
- **Closure source:** AC.10
- **Accepted option:** B
- **Status:** CLOSED
- **Coverage:** ARQ-AN-001 through ARQ-AN-216 plus the above propagation/routing/interpretation addenda.
- **Verdict:** Analytics requirements are complete enough for Architecture to proceed without inventing Analytics product policy. No broad Analytics Grill remains open. Future new Analytics capability requires explicit upstream Product Law/business change, or is handled in Domain Law/Feature Pack/JIT Dossier/Architecture according to the global STOP routing.
- **Non-blocking downstream proof:** FunWithFlags/Bandera/equivalent selection remains an Architecture proof item and does not keep AR-000-A open.


## 8D.12 AR-000 scope-discipline amendments — v0.16.0

These entries preserve the accepted experimentation history while correcting AR-000 boundary leakage identified in the post-Analytics process review. They do **not** reopen Analytics.

### AMEND-AN-001 — ARQ-AN-206 does not pre-name the final owning domain
- **Amends:** `ARQ-AN-206`
- **Status:** AMENDED
- **Reason:** The original wording used “Experiment domain”, which can be read as prematurely assigning concrete domain ownership before `04_DOMAIN_MAP.md`.
- **Effective interpretation:** Experiment hypothesis/configuration, exposure evidence, metric binding, statistical result and decision semantics must have **one coherent authoritative business-ownership boundary** that is separate from the lower-level treatment-assignment mechanism. AR-000 does not name the final owning domain. Final business/domain ownership is `DEFERRED_TO_04_DOMAIN_MAP`.
- **Preserved history:** The original `ARQ-AN-206` text remains unchanged above.
- **Downstream:** AR-002 may establish platform interaction boundaries; `04_DOMAIN_MAP.md` decides final domain ownership.

### AMEND-AN-002 — ARQ-AN-207 requires decoupling, not a preselected adapter/Behaviour implementation
- **Amends:** `ARQ-AN-207`
- **Status:** AMENDED
- **Reason:** “platform-owned adapter/behaviour” is a plausible implementation pattern but is a HOW decision.
- **Effective interpretation:** Business-facing experimentation semantics must not be coupled directly to a concrete third-party assignment-library API, and the concrete assignment mechanism must be replaceable without redefining experiment truth/history. The exact abstraction mechanism — Elixir Behaviour, adapter module, protocol, façade or another structure — is `DEFERRED_TO_ARCHITECTURE` and decided through ARC work.
- **Preserved history:** The original `ARQ-AN-207` text remains unchanged above.

### INTERP-AN-002 — ARQ-AN-209 candidate names are Architecture evidence inputs, not AR-000 mechanism law
- **Interprets:** `ARQ-AN-209` and OQ-040
- **Status:** ACCEPTED
- **Effective interpretation:** FunWithFlags and Bandera remain useful named candidates because the user explicitly accepted their evaluation, but AR-000 does not choose either and does not require experimentation mechanism work before the relevant Architecture/Feature Pack proof needs it. Architecture may select an equivalent or small custom deterministic bucketer if the proof supports that decision.
- **Domain/mechanism boundary:** library selection and exact assignment infrastructure are `DEFERRED_TO_ARCHITECTURE`; final experiment business ownership is `DEFERRED_TO_04_DOMAIN_MAP`.

### PROCESS-AR000-001 — Remaining AR-000 uses extraction and clustering by default
- **Status:** ACCEPTED
- **Requirement:** For remaining AR-000 surfaces, source extraction and clustering is the default. Create focused multiple-choice Grill-Me only when an unresolved ambiguity materially changes the required architecture. Do not generate micro-ARQs merely to enumerate generic engineering best practice.
- **Success criterion:** AR-001…AR-009 can proceed without inventing Product Law and without missing a material constraint.

### PROCESS-AR000-002 — Closed focused surfaces stay closed
- **Status:** ACCEPTED
- **Requirement:** AR-000-P Performance and AR-000-A Analytics are not revisited merely for further optimisation ideas, implementation preferences or additional best-practice enumeration. Reopen only for a genuine contradiction, upstream Product Law amendment, expert invalidation or materially new approved business direction.

## 8E. Cross-cutting accepted decisions surfaced during Analytics Grill

### ARQ-PAY-001 — Paystack is the first / launch payment gateway
- **Decision source:** Explicit user lock on 2026-08-16 during A4 acceptance
- **Status:** ACCEPTED_WITH_UPSTREAM_PROPAGATION_REQUIRED
- **Strength:** LOCKED_PLATFORM_INTEGRATION_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.1.md §21A.12 Payment provider, market and currency` currently states that Paystack is the **provisional** launch payment provider, South Africa is the launch market, ZAR is the launch billing currency, and automatic subscriptions initially use supported card billing. `§21J.15` states that durable payment truth remains in PostgreSQL and provider webhooks are verified/idempotent.
- **Source classification:** EXPLICIT_PLATFORM_PROVISIONAL_REQUIREMENT_PROMOTED_TO_USER_LOCKED_DECISION
- **Requirement:** Paystack is the **first and launch payment gateway**. The payment integration must use Paystack for the initial South African/ZAR launch, including the supported initial recurring-card path. Durable platform payment truth remains provider-independent and authoritative in PostgreSQL; Paystack transaction/reference/status/settlement/refund/dispute data is external-provider evidence mapped into governed platform payment states. The architecture must retain a provider boundary so a future additional gateway can be introduced without redefining core payment, entitlement, refund, reconciliation, or analytics semantics.
- **Primary downstream workstreams:** AR-003, AR-005, AR-006, AR-008, AR-009; Payments Domain Law later
- **Blocking classification:** PLATFORM_INTEGRATION_GATE / UPSTREAM_PRODUCT_LAW_AMENDMENT_REQUIRED
- **Architecture status:** ARQ_LOCKED / PRODUCT_LAW_PROPAGATION_PENDING / ARC_PENDING
- **Required governance follow-up:** Amend the upstream Product Law wording from **provisional launch payment provider** to the newly locked launch decision before Architecture freeze. Preserve the historical provisional wording through the normal amendment/supersession trail rather than silently rewriting history.


## 8D.6 Analytics Requirement Coverage Snapshot

```text
AR-000-P Performance    ARQ-PERF-001 ... ARQ-PERF-166 = 166  CLOSED
AR-000-A Analytics A1   ARQ-AN-001   ... ARQ-AN-022   =  22  ACCEPTED
AR-000-A Analytics A2   ARQ-AN-023   ... ARQ-AN-046   =  24  ACCEPTED
AR-000-A Analytics A3   ARQ-AN-047   ... ARQ-AN-068   =  22  ACCEPTED
AR-000-A Analytics A4   ARQ-AN-069   ... ARQ-AN-098   =  30  ACCEPTED
A4 user refinement      ARQ-AN-099                    =   1  ACCEPTED_WITH_REFINEMENT
AR-000-A Analytics A5   ARQ-AN-100   ... ARQ-AN-127   =  28  ACCEPTED
AR-000-A Analytics A6   ARQ-AN-128   ... ARQ-AN-161   =  34  ACCEPTED
AR-000-A Analytics A7   ARQ-AN-162   ... ARQ-AN-183   =  22  ACCEPTED_WITH_A7.20_USER_AMENDMENT
Built-in experimentation ARQ-AN-184  ... ARQ-AN-205   =  22  ACCEPTED / PRODUCT_LAW_PROPAGATED_v1.2
Experiment assignment layer ARQ-AN-206 ... ARQ-AN-209   =   4  ACCEPTED / ARCHITECTURE_PROOF_PENDING
Analytics closure hardening ARQ-AN-210 ... ARQ-AN-216   =   7  ACCEPTED
Cross-cutting Payments  ARQ-PAY-001                   =   1  ACCEPTED / PRODUCT_LAW_PROPAGATED_v1.2
----------------------------------------------------------------
TOTAL ACCEPTED ARQs                                       = 383
```

Current Analytics status:

```text
A1 COMPLETE / ACCEPTED
A2 COMPLETE / ACCEPTED
A3 COMPLETE / ACCEPTED
A4 COMPLETE / ACCEPTED + USER REFINEMENTS LOCKED
A5 COMPLETE / ACCEPTED
A6 COMPLETE / ACCEPTED
A7 COMPLETE / ACCEPTED WITH A7.20 USER AMENDMENT
BUILT-IN EXPERIMENTATION CAPABILITY LOCKED / PRODUCT LAW v1.2 PROPAGATION COMPLETE
EXPERIMENT ASSIGNMENT-LAYER CONTRACT LOCKED / FUNWITHFLAGS-BANDERA-EQUIVALENT ARCHITECTURE PROOF PENDING (DOWNSTREAM, NON-BLOCKING TO AR-000-A CLOSURE)
ANALYTICS CLOSURE HARDENING ARQ-AN-210 ... ARQ-AN-216 ACCEPTED
AR-000-A ANALYTICS CLOSED
```

## 8D.7 Analytics Closure Status

**AR-000-A — CLOSED at v0.15.0.**

The formal closure audit accepted AC.1–AC.10, propagated the two new business/platform decisions into Product Law v1.2, added ARQ-AN-210 through ARQ-AN-216 for experiment deletion/history compatibility, allocation stability, interaction isolation, variant-safe caching, clean-URL/internal-cache segmentation, traffic quality and safe assignment failure, added AR-001 topology routing, and confirmed that concrete assignment-library choice remains downstream Architecture proof.

No broad Analytics Grill remains open. Continue with the remaining AR-000 architecture-requirement extraction outside the completed Performance and Analytics focused surfaces.


# 8F. Remaining AR-000 Clustered Extraction

## 8F.1 R1 — System & Application Boundaries

> **Operating mode:** Source extraction + clustering under `PROCESS-AR000-001`. No focused Grill-Me was required for R1 because the governing Product Law resolves the material system-shape obligations without an architecture-changing ambiguity. Performance and Analytics remain closed.

### ARQ-SYS-001 — One operating platform with controlled product spaces
- **Extraction source:** R1 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21L.1`; `01_DECISIONS_v1.2.1.md DEC-268`; `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md §19 Long-Term Expansion`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** The system must be shaped as one operating platform capable of controlled product spaces. It must not hard-wire the platform into a permanent women-only application, split approved product spaces into independently reinvented applications by default, or introduce unrestricted generic SaaS tenancy. Sponsors, churches, employers, practitioners, event partners, or similar actors do not become tenants merely by participating. Tenant-style isolation is introduced only if a later approved product requirement genuinely requires it.
- **Architectural implication:** AR-001 must define a runtime/system shape that can host controlled product experiences without assuming generic tenancy or duplicating shared platform foundations. Final business/domain ownership remains deferred to `04_DOMAIN_MAP.md`.
- **Primary downstream workstreams:** AR-001, AR-002, AR-004
- **Blocking classification:** SYSTEM_SHAPE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-SYS-002 — Shared platform capability and product-experience separation
- **Extraction source:** R1 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21L.1`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Architecture must permit approved product spaces to reuse shared platform capabilities such as identity/authentication, payments, entitlements, temperament methodology, content infrastructure, notifications, live/event infrastructure, analytics, audit, and operations while allowing a product space to define its own approved brand, audience, onboarding, navigation, products, programmes, content, eligibility, and participant journeys. Shared infrastructure must not force all product experiences to become one undifferentiated interface or policy surface.
- **Architectural implication:** AR-001/AR-002 must establish platform-versus-experience boundaries and extension points without pre-naming final domains, resources, modules, or implementation structure.
- **Primary downstream workstreams:** AR-001, AR-002, AR-004, AR-006
- **Blocking classification:** PLATFORM_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING / DOMAIN_OWNERSHIP_DEFERRED

### ARQ-SYS-003 — Future product spaces are explicitly activated, not accidentally exposed
- **Extraction source:** R1 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21L.2`; `01_DECISIONS_v1.2.1.md DEC-269`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Only deliberately approved and activated product spaces may become customer-facing. At first public launch, only the women’s health and lifestyle space is exposed; unfinished men’s, professional, corporate, partner, or specialist spaces must remain absent from customer-facing navigation and journeys until separately activated. Nuwe Jy remains a product within the women’s ecosystem rather than redefining the whole platform identity.
- **Architectural implication:** The system must support explicit product-space activation/visibility boundaries without requiring placeholder navigation or premature implementation of future spaces. Exact configuration and routing mechanics are Architecture work.
- **Primary downstream workstreams:** AR-001, AR-002, AR-004, AR-006
- **Blocking classification:** PRODUCT_SPACE_ACTIVATION_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-SYS-004 — South-Africa-first defaults without reusable-platform hard-coding
- **Extraction source:** R1 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21L.3`; `01_DECISIONS_v1.2.1.md DEC-270`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** The first activated market is South Africa with ZAR, Africa/Johannesburg, Afrikaans and English, and South-Africa-first payment configuration. Reusable platform logic must avoid unnecessary South-Africa-specific hard-coding that would make a later approved market require fundamental redesign. A future market is activated only through explicit review/configuration of currency, payments, tax, legal/consumer requirements, privacy, health/safety rules, urgent-support resources, language, and support capability; foreign-card acceptance alone does not activate a market.
- **Architectural implication:** AR-001/AR-002/AR-006/AR-007 must distinguish launch configuration from reusable platform semantics while not building premature multi-market infrastructure.
- **Primary downstream workstreams:** AR-001, AR-002, AR-006, AR-007
- **Blocking classification:** MARKET_PORTABILITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-SYS-005 — Mature-platform compatibility with deliberate MVP restraint
- **Extraction source:** R1 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** ARCHITECTURAL_PRINCIPLE / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md §§3, 14, 18A, 19`; `00_PLATFORM_v1.2.1.md §21L`; `01_DECISIONS_v1.2.1.md DEC-271–280`
- **Source classification:** EXPLICIT_NORTH_STAR_AND_RELEASE_SEQUENCE_REQUIREMENT
- **Requirement:** Architecture must treat the approved MVP as the smallest viable slice of the coherent mature platform rather than a throwaway standalone application. Approved near-future capabilities—especially the first native Nuwe Jy edition—must not require fundamental redesign of shared platform foundations that Product Law already identifies as reusable. This compatibility requirement does **not** authorise premature implementation of capabilities explicitly excluded from the MVP; delivery remains incremental and Roadmap/Feature Packs decide when approved capabilities are built.
- **Architectural implication:** AR-001/AR-002 must preserve known extension paths while resisting speculative infrastructure or feature implementation not required by the selected release.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-006
- **Blocking classification:** EVOLUTIONARY_ARCHITECTURE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-SYS-006 — Legacy LearnDash structures do not become new-platform authority
- **Extraction source:** R1 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21H.11, 21H.24`; `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md §18A`; `01_DECISIONS_v1.2.1.md DEC-207, DEC-219`
- **Source classification:** EXPLICIT_PRODUCT_LAW_LEGACY_BOUNDARY
- **Requirement:** The new platform must not adopt LearnDash identifiers, course hierarchy, completion states, shortcodes, drip implementation, quiz assumptions, plugin architecture, or equivalent legacy implementation structures as new authoritative business truth. Do not create a general LearnDash importer, converter, or compatibility subsystem. Existing obligations may be completed and source content/media reviewed, but a future named Nuwe Jy edition runs natively on the new platform; exceptional legacy recognition remains a bounded business process rather than a reusable migration architecture.
- **Architectural implication:** AR-001/AR-002/AR-003 must establish a clean legacy boundary and native application model; exact data-entry/cutover operations remain later planning/operations work.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-006
- **Blocking classification:** LEGACY_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### R1 Coverage / Deferral Note

R1 deliberately does **not** create separate requirements for provider-specific live/media ownership, translation-resource design, notification/provider boundaries, cache implementation, or exact Phoenix/LiveView/Ash structure. Those sources are retained for R4/R5 or the relevant AR-001…AR-009 HOW decisions. R1 also does not re-extract Performance/Analytics requirements already closed.

Current clustered coverage after R1:

```text
AR-000-P Performance              166  CLOSED
AR-000-A Analytics                216  CLOSED
Cross-cutting Payments              1  ACCEPTED / PRODUCT LAW PROPAGATED
R1 System & Application Boundaries  6  COMPLETE
------------------------------------------------
TOTAL ACCEPTED ARQs                389
```

**Next:** R2 — Identity, Authentication, Authorisation, Consent & Audit clustered extraction.



## 8F.2 R2 — Identity, Authentication, Authorisation, Consent & Audit

> **Operating mode:** Source extraction + clustering under `PROCESS-AR000-001`. No focused Grill-Me was required: Product Law already fixes the material identity/access/consent obligations while leaving package choice, policy implementation, exact resource shape and authentication mechanics to Architecture.

### ARQ-IAM-001 — One human identity may hold multiple explicit scoped roles without collapsing actor concepts
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§15.1–15.6`; `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md §8 Absolute Non-Negotiables`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** One human identity may hold multiple explicit roles, but roles must remain assignable, removable, scoped and auditable. Purchaser, recipient, participant and account holder remain distinct concepts. A role or broad technical/admin capability must not automatically grant unrelated health, assessment, journal, methodology, professional or clinical authority, and paying for another person never grants access to that person's private health journey.
- **Architectural implication:** AR-004 must support actor context and composable scoped roles/policies without conflating identity, commercial relationship, participation, professional authority or administrative capability. Final role/domain ownership remains Domain Map work.
- **Primary downstream workstreams:** AR-002, AR-004
- **Blocking classification:** BLOCKING_AUTHZ_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-002 — Launch authentication and verified-email capability gates are explicit
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§7.3, 21J.1–21J.2`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Launch authentication supports email/password with secure password reset and may support optional email magic-link sign-in; future passkeys remain allowed when justified, while social login is deferred until a proven need exists. Email verification is a real capability boundary: unverified users may perform only permitted low-risk setup/public actions, while verified email is required before paid purchase/redemption, assessment, health-data entry, personalised plans, member community, sensitive export and account deletion.
- **Architectural implication:** AR-004 must define an authentication/verification state model that can enforce capability gates consistently across UI and application actions without hard-coding a third-party auth package into Product Law.
- **Primary downstream workstreams:** AR-002, AR-004
- **Blocking classification:** AUTHENTICATION_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-003 — Authentication strength, sessions, trusted devices and recovery are role/risk based
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21J.3–21J.8`; `§21I.4 risk-based verification`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Participant MFA remains optional, but high-risk actions require step-up authentication. MFA is mandatory for staff and practitioners and privileged access is prohibited without it. Session lifetime and reauthentication are role/risk based; users can inspect/revoke sessions and sign out all devices. Trusted-device status is expiring/revocable and never bypasses required step-up. Recovery is graduated and auditable, with security holds, sensitive-change restrictions and second-person approval for privileged recovery where ordinary recovery fails. Informal support overrides are not an authentication mechanism.
- **Architectural implication:** AR-004/AR-008 must define coherent authentication assurance, session, device and recovery state transitions plus revocation behaviour; exact package, token/session representation and MFA providers remain Architecture decisions.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** BLOCKING_AUTHENTICATION_SECURITY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-004 — Privileged and break-glass access is named, least-privilege, time-bounded and fully auditable
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§15.4, 21J.4, 21J.11–21J.12`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Privileged-role grants require named subjects, explicit role/scope/reason, approver, start and expiry/review semantics, relationship context where applicable and revocation history. Sensitive roles cannot be self-approved; least privilege and time-limited elevation are preferred; termination triggers prompt revocation. Break-glass/production access requires named identity, strong MFA, reason, narrow scope where possible, short expiry, immediate audit, owner alert and post-access review. Shared privileged credentials are prohibited; direct database access is exceptional; production participant data must not be copied into local development.
- **Architectural implication:** AR-004/AR-008 must establish privileged-access control and evidence mechanisms without treating Super Admin or technical administration as universal business/clinical authority.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** PRIVILEGED_ACCESS_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-005 — Practitioner and sensitive-record access requires a live scoped relationship, not merely a role name
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §16 Practitioner Access to Participant Data`; `§21C.19`; `§21F.19`; `§21H.16`; `§21I.13`
- **Source classification:** EXPLICIT_PRODUCT_LAW_PRIVACY_AND_AUTHZ_REQUIREMENT
- **Requirement:** Practitioner access to participant information requires explicit participant permission, an active care/review relationship, defined scope and expiry, complete audit and revocable future access. Clinical access is a separate consented authority; ordinary support/content/moderator/admin roles cannot browse private journals or unrelated clinical data. Revocation ends future platform access even where a professional copy must remain under separate retention law.
- **Architectural implication:** AR-004 must support relationship-, purpose-, field/record- and time-scoped authorisation rather than role-only access checks; AR-007 later governs retained professional copies.
- **Primary downstream workstreams:** AR-004, AR-007
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-006 — Consent is purpose-specific, versioned and dynamically effective
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21C.19`; `§21I.13`; `§17 Data Ownership and Control`
- **Source classification:** EXPLICIT_PRODUCT_LAW_CONSENT_REQUIREMENT
- **Requirement:** Consent/lawful-basis state must be purpose-specific rather than one universal flag. Required service processing, health storage, health personalisation, automated recommendations, laboratory uploads, practitioner sharing, anonymised/aggregated analytics, marketing communications and community participation remain separately governable; required and optional processing are distinguishable and marketing is separate. Consent, withdrawal and applicable policy version are timestamped/retained. Withdrawal stops affected future processing and invalidates dependent active permissions/caches/flags while preserving only records that lawfully remain; prior lawful processing is not rewritten.
- **Architectural implication:** AR-004/AR-007 must define a reusable permission/consent evaluation boundary and dependency invalidation path; exact consent resources/schema belong to Architecture/Domain Law.
- **Primary downstream workstreams:** AR-004, AR-005, AR-007, AR-008
- **Blocking classification:** BLOCKING_CONSENT_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-007 — Audit and security evidence is immutable, minimised, reasoned and separated from business payloads
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21I.14–21I.15`; sensitive-access rules throughout §§15–16 and 21J
- **Source classification:** EXPLICIT_PRODUCT_LAW_AUDIT_REQUIREMENT
- **Requirement:** Material sensitive access, privileged actions, policy decisions, consent/withdrawal, recovery/security changes and similar governed actions require immutable, category-appropriate audit/security evidence. Entries capture enough provenance such as actor, action, target category, time, access reason, outcome/policy result, correlation identifier and limited change summary without duplicating full sensitive health payloads. Ordinary administrators cannot rewrite audit history. Security evidence is minimised, retained under its own approved rule and must not be repurposed for marketing/personalisation.
- **Architectural implication:** AR-004/AR-008 must establish an auditable action/access evidence path that is tamper-resistant at the application authority level while keeping sensitive payloads out of generic logs. Exact storage/retention mechanism is deferred.
- **Primary downstream workstreams:** AR-004, AR-008
- **Blocking classification:** BLOCKING_AUDIT_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-008 — Identity recovery, merge and compromise handling preserves provenance and does not manufacture authority
- **Extraction source:** R2 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21J.7–21J.10`
- **Source classification:** EXPLICIT_PRODUCT_LAW_IDENTITY_LIFECYCLE_REQUIREMENT
- **Requirement:** Identity changes and exceptional recovery must preserve security and domain provenance. Duplicate accounts are never merged by name/demographics alone; control of identities is verified where practical, affected business records are reconciled deliberately, immutable histories and finance/professional provenance are preserved, and conflicting current-state choices are resolved explicitly. Compromise containment may revoke sessions/devices, suspend sensitive actions and freeze high-risk changes until verified recovery; privileged compromise escalates immediately.
- **Architectural implication:** AR-004/AR-005/AR-008 must support revocable identity/session state and domain-safe merge/recovery workflows without allowing identity tooling to overwrite authoritative domain histories.
- **Primary downstream workstreams:** AR-004, AR-005, AR-008
- **Blocking classification:** IDENTITY_INTEGRITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### R2 Coverage / Deferral Note

R2 deliberately does **not** choose an authentication library/package, Ash policy implementation, session/token representation, MFA provider, exact consent schema, audit table/log technology or final role ownership. Abuse/rate-limit mechanisms remain R6/Architecture where not already covered by closed Performance. Deletion/retention mechanics and backup interaction remain R3.

Current clustered coverage after R2:

```text
AR-000-P Performance               166  CLOSED
AR-000-A Analytics                 216  CLOSED
Cross-cutting Payments               1  ACCEPTED / PRODUCT LAW PROPAGATED
R1 System & Application Boundaries   6  COMPLETE
R2 Identity / Access / Consent        8  COMPLETE
-------------------------------------------------
TOTAL ACCEPTED ARQs                 397
```

**Next:** R3 — State Authority, Storage & Records Lifecycle clustered extraction.



## 8F.3 R3 — State Authority, Storage & Records Lifecycle

> **Operating mode:** Source extraction + clustering. The closed Performance surface already governs PostgreSQL durable authority, rebuildable cache/acceleration state and failure semantics; R3 does not duplicate those requirements. No focused Grill-Me was required.

### ARQ-STATE-001 — Storage location and delivery path follow data sensitivity and authority
- **Extraction source:** R3 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21E.15, 21K.1`; closed Performance authority/cache requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT_PLUS_CLOSED_PERFORMANCE_DOCTRINE
- **Requirement:** Browser-local storage is permitted only for explicitly safe client-side state. Public static/media may use object storage and CDN delivery. Private health, plan, entitlement, security, paid or practitioner-shared data must not be exposed through public cache paths. Private/protected assets require governed access and short-lived signed delivery where applicable; upload safety gates must prevent unsafe/unscanned content from publishing. Storage/delivery acceleration never changes the authoritative business record.
- **Architectural implication:** AR-003/AR-006 must classify client, object, CDN and protected-delivery state by sensitivity/access contract while preserving the existing PostgreSQL/caching authority law.
- **Primary downstream workstreams:** AR-003, AR-004, AR-006, AR-007
- **Blocking classification:** STORAGE_PRIVACY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-002 — Material business records use immutable or superseding history rather than destructive rewriting
- **Extraction source:** R3 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md §8`; `00_PLATFORM_v1.2.1.md §§21B.2–21B.14, 21D.6, 21D.11–21D.13, 21E.8–21E.10, 21I.22`
- **Source classification:** EXPLICIT_CROSS_PRODUCT_VERSIONING_REQUIREMENT
- **Requirement:** Where Product Law requires reproducibility/history, submitted assessment answers/results, generated plans, material content versions, professional corrections and financial corrections must preserve original historical truth. Material changes use new versions, reviewed interpretations, addenda, credits/refunds/adjustments or other record-appropriate superseding constructs; current-state selection may change without erasing the original fact. Updating reusable content or methodology must not silently rewrite previously delivered immutable records.
- **Architectural implication:** AR-003/AR-005 must establish a cross-cutting immutability/versioning doctrine while final record-specific state machines and resource ownership remain Domain Law.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008
- **Blocking classification:** HISTORY_INTEGRITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-003 — Record lifecycle state is explicit, category-aware and separate from business state
- **Extraction source:** R3 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21I.1–21I.3, 21I.17–21I.18`
- **Source classification:** EXPLICIT_PRODUCT_LAW_LIFECYCLE_REQUIREMENT
- **Requirement:** Record/account lifecycle concepts such as active, archived, access-restricted, deletion-requested/pending, anonymised, deleted, retained-by-obligation and legal-hold state are distinct from a record's business lifecycle. Applicable transitions record reason, authority, timestamp and policy version and destructive workflows are idempotent. Account closure remains distinct from full deletion; dormancy, deceased-participant handling and later re-registration must not silently resurrect a fully deleted identity relationship.
- **Architectural implication:** AR-003/AR-007 must define reusable lifecycle/deletion orchestration semantics without forcing one identical lifecycle table/state machine onto every domain.
- **Primary downstream workstreams:** AR-003, AR-004, AR-007, AR-008
- **Blocking classification:** DATA_LIFECYCLE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-004 — Full deletion is irreversible and propagates across every eligible representation
- **Extraction source:** R3 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21I.3, 21I.5–21I.16`; Analytics deletion ARQs remain additionally applicable
- **Source classification:** EXPLICIT_PRODUCT_LAW_DELETION_REQUIREMENT
- **Requirement:** Completed full deletion is irreversible for the deleted account relationship. Eligible identifiable data must be deleted or irreversibly anonymised across authoritative records and applicable derived representations, including health/check-in state, journals, uploads, object derivatives/thumbnails, extracted values, indexes, caches, signed-link capability, superseded eligible files, temporary worker files and external processors. Deleting only a database row is insufficient. Retained transactions, security evidence, professional records or backups must never be used to reconstruct the deleted account, health profile, plan history or analytics identity.
- **Architectural implication:** AR-003/AR-007/AR-008 must define deletion discovery/orchestration, idempotency, processor propagation and proof without assuming all categories share the same retention outcome.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007, AR-008
- **Blocking classification:** BLOCKING_DELETION_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-005 — Retained-by-obligation records and legal holds are isolated and minimal
- **Extraction source:** R3 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21I.8, 21I.12, 21I.15, 21I.19`; exact durations remain expert-owned
- **Source classification:** EXPLICIT_PRODUCT_LAW_RETENTION_REQUIREMENT
- **Requirement:** Where professional, tax/accounting/payment/dispute, fraud/security or legal obligations require retention, retain only the necessary records/identity fields, isolate them from ordinary participant use, restrict access and exclude them from marketing/personalisation/ordinary analytics as applicable. Legal holds are scoped to exact records/purpose/authority/owner/time/release condition, must not block unrelated deletion unnecessarily, and deletion resumes when the hold ends. Exact statutory/professional durations remain expert-owned and must not be invented by Architecture.
- **Architectural implication:** AR-007/AR-004 must support category-specific restricted retention/hold semantics and explicit expert-owned policy inputs.
- **Primary downstream workstreams:** AR-004, AR-007, AR-008
- **Blocking classification:** RETENTION_LEGAL_HOLD_GATE
- **Architecture status:** ARQ_LOCKED / EXPERT_DURATION_INPUT_PENDING_WHERE_APPLICABLE / ARC_PENDING

### ARQ-STATE-006 — Backup and restore must preserve deletion/withdrawal truth
- **Extraction source:** R3 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / RELEASE_GATE_INPUT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21I.20`; closed Performance recovery requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_BACKUP_REQUIREMENT
- **Requirement:** Backups exist for disaster recovery rather than participant-level recovery. Deleted data may survive only within encrypted backup retention until normal expiry; ordinary retrieval of deleted accounts is prohibited. Restore occurs through a controlled recovery process that replays completed deletion and consent-withdrawal events before normal service resumes and verifies deleted identities do not reappear. A backup may not be used to restore one deleted participant on request.
- **Architectural implication:** AR-007/AR-008 must integrate backup/restore with deletion suppression/replay and proof; exact RPO/RTO remains governed separately by reliability classification.
- **Primary downstream workstreams:** AR-007, AR-008
- **Blocking classification:** BACKUP_DELETION_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-007 — Participant export is a secure governed data-release workflow
- **Extraction source:** R3 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21I.21`; `§21I.4`; applicable Analytics export-hardening ARQs
- **Source classification:** EXPLICIT_PRODUCT_LAW_EXPORT_REQUIREMENT
- **Requirement:** Participants must be able to receive an approved human-readable plus structured export of eligible records, potentially including original uploaded files, subject to category-specific redaction/retention restrictions. Sensitive exports require strong verification, audit, secure short-lived delivery and bounded/asynchronous generation where size warrants it. Export capability must not expose records the participant is not entitled or legally permitted to receive.
- **Architectural implication:** AR-004/AR-005/AR-007/AR-008 must define a secure export orchestration boundary while reusing closed Analytics export controls rather than creating a separate weaker path.
- **Primary downstream workstreams:** AR-004, AR-005, AR-007, AR-008
- **Blocking classification:** DATA_EXPORT_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### R3 Coverage / Deferral Note

R3 reuses rather than duplicates the closed Performance authority/cache/read-model/recovery requirements and closed Analytics deletion/export requirements. It does not choose object-storage vendor, bucket layout, browser key format, signed-URL implementation, deletion job topology, retention duration, backup product, schema, table or index. Detailed media/content governance remains R5.

Current clustered coverage after R3:

```text
AR-000-P Performance                166  CLOSED
AR-000-A Analytics                  216  CLOSED
Cross-cutting Payments                1  ACCEPTED / PRODUCT LAW PROPAGATED
R1 System & Application Boundaries    6  COMPLETE
R2 Identity / Access / Consent         8  COMPLETE
R3 State / Storage / Lifecycle         7  COMPLETE
--------------------------------------------------
TOTAL ACCEPTED ARQs                  404
```

**Next:** R4 — Transactions, Async, Realtime & Notifications clustered extraction.



## 8F.4 R4 — Transactions, Async, Realtime & Notifications

> **Operating mode:** Source extraction + clustering. Transaction boundaries, atomic durable intent/outbox-equivalent semantics, async queueing/backpressure, idempotency/retry, PubSub/LiveView observation and multi-node realtime behaviour are already covered by the closed Performance surface and are not duplicated here. No focused Grill-Me was required.

### ARQ-ASYNC-001 — Notification intent, preference and delivery are governed separately from business truth
- **Extraction source:** R4 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21J.18–21J.20`; consent requirements in `§21C.19`; closed Performance async requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_NOTIFICATION_REQUIREMENT
- **Requirement:** The platform must support category-, purpose- and channel-aware notification policy. Launch is email and in-app first; SMS/WhatsApp activate only after provider/cost/consent validation and native push remains deferred until justified. Essential security/transactional messages may remain mandatory where necessary; marketing consent is separate; non-urgent communication respects timezone/quiet hours/frequency caps; completed actions suppress obsolete reminders; safety overrides are separately governed. Delivery is a durable asynchronous consequence with idempotency/deduplication, bounded/provider-aware retry, template/version and correlation evidence, terminal-failure visibility and no duplicate message after retry. Notification delivery status does not create or replace the underlying authoritative business event.
- **Architectural implication:** AR-005/AR-006/AR-008 must separate authoritative domain outcome, durable notification intent, channel/provider delivery and observable delivery status while reusing the closed queue/outbox law. Exact provider, queue names and template resource ownership are deferred.
- **Primary downstream workstreams:** AR-004, AR-005, AR-006, AR-008
- **Blocking classification:** NOTIFICATION_CONSEQUENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-ASYNC-002 — Scheduled publication and programme release are preconditioned, idempotent and recoverable business-effective transitions
- **Extraction source:** R4 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21E.9, 21H.5`; closed Performance scheduling/business-effective-time requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_SCHEDULING_REQUIREMENT
- **Requirement:** Scheduled publication and programme/day release must be timezone-aware where applicable, idempotent, observable, recoverable and protected against duplicate release. Required approvals, translations, access/product state, safety-withdrawal state and relevant dependencies are revalidated at execution. Preconfigured programme releases must not depend on daily administrator action. A failed attempt creates visible recoverable operational state rather than silently skipping or double-publishing the business transition.
- **Architectural implication:** AR-005/AR-006/AR-008 must define how business-effective schedules become durable/recoverable consequences using the existing cluster-safe scheduling and retry doctrine; exact scheduler/job implementation is deferred.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008
- **Blocking classification:** SCHEDULED_TRANSITION_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-ASYNC-003 — External callback/provider evidence is verified and repeat-safe but never becomes unqualified platform authority
- **Extraction source:** R4 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21A.12, 21J.15, 21J.20`; `ARQ-PAY-001`; closed Performance provider/idempotency requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_PROVIDER_BOUNDARY_CONSOLIDATED_WITH_EXISTING_ARQS
- **Requirement:** Provider callbacks and delivery evidence must be authenticated/verified as appropriate, idempotently/repeat-safely processed and mapped into governed platform state. A replay, retry or duplicate callback may not multiply entitlements, notifications, refunds or other consequences. Paystack/provider status remains external evidence behind the provider boundary; durable platform payment/business truth remains governed by the platform's authoritative state and reconciliation rules. Exact Paystack retry/subscription/webhook/proration/refund/dispute semantics remain OQ-004/vendor-validation work rather than being invented in AR-000.
- **Architectural implication:** AR-005/AR-006/AR-008 must expose a consistent provider-ingress/reconciliation boundary while provider-specific details remain Architecture/vendor proof.
- **Primary downstream workstreams:** AR-005, AR-006, AR-008
- **Blocking classification:** PROVIDER_CALLBACK_INTEGRITY_GATE
- **Architecture status:** ARQ_LOCKED / VENDOR_DETAILS_PENDING_WHERE_APPLICABLE / ARC_PENDING

### R4 Coverage / Deferral Note

R4 adds no new generic transaction, outbox, Oban, PubSub, LiveView, retry, queue or realtime mechanics beyond closed Performance. Those ARQs remain the authoritative requirements surface. Exact queue names, worker topology, scheduler implementation, PubSub topics, notification providers, callback endpoints and retry constants are Architecture/JIT concerns.

Current clustered coverage after R4:

```text
AR-000-P Performance                 166  CLOSED
AR-000-A Analytics                   216  CLOSED
Cross-cutting Payments                 1  ACCEPTED / PRODUCT LAW PROPAGATED
R1 System & Application Boundaries     6  COMPLETE
R2 Identity / Access / Consent          8  COMPLETE
R3 State / Storage / Lifecycle          7  COMPLETE
R4 Transactions / Async / Realtime      3  COMPLETE
---------------------------------------------------
TOTAL ACCEPTED ARQs                   407
```

**Next:** R5 — Content, Translation, Media & External Integrations clustered extraction.



## 8F.5 R5 — Content, Translation, Media & External Integrations

> **Operating mode:** Source extraction + clustering. Content/version immutability already has a cross-cutting R3 requirement; caching/performance is already covered; notification and Paystack provider consequences were handled in R4/`ARQ-PAY-001`. R5 records only the remaining content/media/integration boundaries. No focused Grill-Me was required.

### ARQ-CONTENT-001 — Bilingual governed content uses linked, independently approved language versions
- **Extraction source:** R5 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21D.12, 21E.1–21E.3, 21E.7–21E.8`; `01_DECISIONS_v1.2.1.md DEC-118–119, DEC-123–127, DEC-134–135`
- **Source classification:** EXPLICIT_PRODUCT_LAW_TRANSLATION_REQUIREMENT
- **Requirement:** Afrikaans and English variants remain linked to one conceptual governed item but are independently versioned/reviewed. Both approved languages are mandatory before delivery/publication of registration/authentication, checkout/subscription, terms/consent/privacy, assessments, paid reports, personalised plans, safety/clinical warnings, cancellation/refund communication and core onboarding. Optional low-risk public editorial content may be temporarily single-language only with explicit availability/fallback handling. Machine translation may create drafts only and never silently publishes or serves as an unapproved fallback for governed paid/health/safety content.
- **Architectural implication:** AR-002/AR-006 must support conceptual content identity plus independently governed locale versions and delivery-version provenance without treating translations as unrelated content or one mutable global blob.
- **Primary downstream workstreams:** AR-002, AR-006
- **Blocking classification:** BILINGUAL_CONTENT_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-CONTENT-002 — Product Law requires a layered translation boundary, while exact resource design remains Architecture work
- **Extraction source:** R5 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** LOCKED_PLATFORM_MECHANISM_REQUIREMENT / DEFERRED_TO_ARCHITECTURE_FOR_DETAIL
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21D.12`; `01_DECISIONS_v1.2.1.md DEC-119`; `OQ-013 Translation resource design`
- **Source classification:** EXPLICIT_PRODUCT_LAW_TECHNOLOGY_BOUNDARY_WITH_OPEN_DETAIL
- **Requirement:** Preserve the Product-Law-mandated layered translation model: Gettext handles fixed interface/system strings, governed runtime content is represented through Ash-backed managed translation data rather than compiled strings alone, and delivered personalised/paid outputs retain immutable references to the exact language-content versions shown. Complex governed editorial content must not live only in compiled Gettext files.
- **Architectural implication:** AR-002/AR-006 must decide exact Ash resource/module relationships, approval relationships, locale/version indexes and delivery references under OQ-013; AR-000 does not design those resources.
- **Primary downstream workstreams:** AR-002, AR-003, AR-006
- **Blocking classification:** TRANSLATION_ARCHITECTURE_GATE
- **Architecture status:** ARQ_LOCKED / OQ-013_ARCHITECTURE_DETAIL_PENDING / ARC_PENDING

### ARQ-CONTENT-003 — Content risk class governs approval, publication, correction and withdrawal authority
- **Extraction source:** R5 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21E.4, 21E.8–21E.10`; `01_DECISIONS_v1.2.1.md DEC-129–130, DEC-135–137`
- **Source classification:** EXPLICIT_PRODUCT_LAW_CONTENT_GOVERNANCE_REQUIREMENT
- **Requirement:** Governed content has an explicit risk class that controls the required review/approval authority, language approval, publication authority, correction severity and withdrawal urgency. Separate approvals remain separately evidenced even when one human holds several roles. Scheduled publication revalidates required approvals/translations/access/safety state. Material, safety and legal/consent corrections use governed superseding/withdrawal handling rather than silent edits; safety withdrawal must be able to remove affected future use promptly.
- **Architectural implication:** AR-002/AR-004/AR-005/AR-006 must support approval/policy state and authoritative publication/withdrawal decisions without predefining exact resources or editorial UI.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005, AR-006, AR-008
- **Blocking classification:** CONTENT_APPROVAL_SAFETY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-CONTENT-004 — Discovery and personalised content use access-first, minimum-signal, explainable rules
- **Extraction source:** R5 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21E.5–21E.6, 21E.12`; `01_DECISIONS_v1.2.1.md DEC-131–133, DEC-139–140`
- **Source classification:** EXPLICIT_PRODUCT_LAW_DISCOVERY_AND_PERSONALISATION_REQUIREMENT
- **Requirement:** Search/feed/discovery must apply access/publication policy before returning content and use deterministic/explainable governed ranking. Health-derived personalisation receives minimum approved relevance flags rather than full diagnoses or clinical records; source/permission expiry removes dependent flags. Participants can understand/control optional ranking while applicable safety-required content cannot be permanently hidden. Semantic ranking may later be a controlled secondary signal, not sole authority.
- **Architectural implication:** AR-004/AR-006 must keep discovery/feed infrastructure separated from detailed clinical records and preserve policy-first access plus explainability. Exact search engine/index/ranking implementation remains Architecture work.
- **Primary downstream workstreams:** AR-004, AR-006, AR-007, AR-008
- **Blocking classification:** CONTENT_PRIVACY_AND_ACCESS_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-CONTENT-005 — Public multilingual SEO and private indexing boundaries are deliberate
- **Extraction source:** R5 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21E.13`; `01_DECISIONS_v1.2.1.md DEC-141`; experimentation clean-URL ARQs remain additionally applicable
- **Source classification:** EXPLICIT_PRODUCT_LAW_SEO_REQUIREMENT
- **Requirement:** Public translated content uses deliberate locale-specific URLs with approved per-language slugs/canonical URLs and appropriate alternate-language relationships; slug changes create permanent redirects. Language alternates are emitted only for real translations. Private/paid content is excluded from ordinary indexing. Experimentation must preserve these canonical/SEO rules rather than creating normal public variant URLs as cache/assignment infrastructure.
- **Architectural implication:** AR-001/AR-002/AR-006 must define routing/publication metadata boundaries that preserve multilingual canonical semantics without leaking private or experimental internal identity into search indexing.
- **Primary downstream workstreams:** AR-001, AR-002, AR-006
- **Blocking classification:** SEO_ROUTING_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-CONTENT-006 — Media providers may deliver/transcode, but platform business access/policy metadata remains platform-controlled
- **Extraction source:** R5 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21E.15, 21G.15–21G.16`; `01_DECISIONS_v1.2.1.md DEC-143–144`; OQ-020/OQ-021 provider/recording validation where applicable
- **Source classification:** EXPLICIT_PRODUCT_LAW_MEDIA_AND_PROVIDER_BOUNDARY
- **Requirement:** Media is governed with version/ownership/licence/creator/accessibility/risk/publication/checksum/storage/replacement metadata and protected assets remain entitlement-controlled. For live/replay delivery, external production/streaming/transcoding services may perform media transport, but the platform retains governed session metadata, registrations, entitlements, policy/replay-publication decisions, consent/audit and analytics. A live session/recording is not public merely because the provider produced it. Do not build a self-hosted RTMP/transcoding service for the first release.
- **Architectural implication:** AR-001/AR-006 must establish provider boundaries and platform-owned business metadata/policy while exact Restream/Cloudflare validation and recording-retention implementation remain vendor/operations gates.
- **Primary downstream workstreams:** AR-001, AR-003, AR-004, AR-006, AR-008
- **Blocking classification:** MEDIA_PROVIDER_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / PROVIDER_VALIDATION_PENDING_WHERE_APPLICABLE / ARC_PENDING

### R5 Coverage / Deferral Note

R5 does not choose exact Ash translation resources, content tables, search engine/index structure, Cloudflare cache rules, object-storage layout, media provider plans, notification providers, or processor inventory. Paystack is already governed separately; external processor deletion belongs to R3/AR-007. Detailed content types and programme ownership remain Domain Map/Dossiers.

Current clustered coverage after R5:

```text
AR-000-P Performance                  166  CLOSED
AR-000-A Analytics                    216  CLOSED
Cross-cutting Payments                  1  ACCEPTED / PRODUCT LAW PROPAGATED
R1 System & Application Boundaries      6  COMPLETE
R2 Identity / Access / Consent           8  COMPLETE
R3 State / Storage / Lifecycle           7  COMPLETE
R4 Transactions / Async / Realtime       3  COMPLETE
R5 Content / Translation / Media          6  COMPLETE
----------------------------------------------------
TOTAL ACCEPTED ARQs                    413
```

**Next:** R6 — Security, Operations, Deployment & Cross-Cutting Closure Coverage.



## 8F.6 R6 — Security, Operations, Deployment & Cross-Cutting Closure Coverage

> **Operating mode:** Source extraction + clustering. Closed Performance already governs deployment safety, graceful degradation, multi-node behaviour, reliability, observability, recovery testing and incident-driven correction. R2/R3 already govern privileged access, audit and deletion-safe restore. R6 therefore adds only the remaining explicit Product-Law security/operations obligations. No focused Grill-Me was required.

### ARQ-SEC-001 — Abuse protection is layered, distributed and non-enumerating across sensitive entry points
- **Extraction source:** R6 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21J.13–21J.15, 21J.17`; closed Performance distributed-rate/overload requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_SECURITY_REQUIREMENT
- **Requirement:** Registration, login, reset/magic-link/MFA, email-change/recovery, redemption, checkout/payment and protected download/search surfaces require layered abuse controls appropriate to risk, combining edge/application/distributed velocity and account/device/network signals where justified. High-velocity counters/limits must work across nodes; temporary lockout/challenge behaviour remains recoverable; privileged accounts receive stricter handling. Redemption/auth failure responses must not leak whether a guessed secret/code/account state was otherwise valid. Bot/scraping controls must preserve intended public SEO while preventing ordinary endpoints from becoming bulk extraction paths for private, paid, health or plan data.
- **Architectural implication:** AR-004/AR-008/AR-009 must establish reusable abuse/rate/risk-control boundaries while exact thresholds, Redis structures, Cloudflare rules and challenge mechanisms remain Architecture/JIT evidence decisions.
- **Primary downstream workstreams:** AR-004, AR-008, AR-009
- **Blocking classification:** SECURITY_ABUSE_GATE
- **Architecture status:** ARQ_LOCKED / EXACT_THRESHOLDS_DEFERRED / ARC_PENDING

### ARQ-SEC-002 — Uploads remain restricted until type/content/malware safety gates pass
- **Extraction source:** R6 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21J.16`; `§21E.15`; `ARQ-STATE-001`
- **Source classification:** EXPLICIT_PRODUCT_LAW_UPLOAD_SECURITY_REQUIREMENT
- **Requirement:** Every upload begins in a restricted/unpublished state and must pass appropriate size/type validation, MIME/content inspection, malware scanning and metadata sanitisation before durable governed access/publication. Unsafe/failed-scan formats never publish; private files are not public by default; signed protected access expires; heavy processing may execute asynchronously under the existing durable-work law.
- **Architectural implication:** AR-003/AR-006/AR-008 must define quarantine-to-governed-storage state and failure handling without choosing storage vendor, scanner product, bucket/key structure or worker implementation in AR-000.
- **Primary downstream workstreams:** AR-003, AR-006, AR-008
- **Blocking classification:** FILE_SECURITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-OPS-001 — Material incidents and release stages require named cross-functional ownership and explicit no-go evidence
- **Extraction source:** R6 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** RELEASE_GATE_INPUT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §§21J.23–21J.24, 21L.21–21L.24`; `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md MVP Safety Release Gates`; closed Performance incident/release requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_OPERATIONS_AND_RELEASE_REQUIREMENT
- **Requirement:** Material incidents use governed severity/ownership with a named owner, timeline, containment, communication, remediation and post-incident review. Release/pilot progression is cross-functional: applicable clinical, content, commerce, legal/privacy, security and operations prerequisites are evidence-bearing gates, and an unresolved required item is a no-go for the affected stage. Technical/commercial success cannot waive a blocker owned by another authority. Operational visibility must include relevant infrastructure/application/domain outcomes rather than infrastructure health alone.
- **Architectural implication:** AR-008 must define incident/release evidence, ownership and observability integration while Product/Clinical/Legal gate values remain with their proper authorities.
- **Primary downstream workstreams:** AR-004, AR-008, AR-009
- **Blocking classification:** RELEASE_AND_INCIDENT_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-OPS-002 — Disaster recovery covers configuration/secrets and object state as well as databases
- **Extraction source:** R6 clustered source extraction
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / RELEASE_GATE_INPUT
- **Exact Product Law source:** `00_PLATFORM_v1.2.1.md §21J.22`; `ARQ-STATE-006`; closed Performance recovery/RPO/RTO requirements
- **Source classification:** EXPLICIT_PRODUCT_LAW_RECOVERY_REQUIREMENT
- **Requirement:** Recovery capability must cover the platform components needed to reconstitute service, including PostgreSQL backup/PITR where supported, encrypted off-site copies, object-storage durability and recoverable configuration/secrets, with backup expiry and regularly exercised restore. Restored service must still apply R3 deletion/consent replay rules. Exact RPO/RTO values, backup products and secret-management mechanisms remain Architecture/evidence decisions.
- **Architectural implication:** AR-001/AR-007/AR-008 must define the recoverable runtime/configuration boundary and prove restore of required dependencies, not only database bytes.
- **Primary downstream workstreams:** AR-001, AR-007, AR-008
- **Blocking classification:** DISASTER_RECOVERY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### R6 Coverage / Deferral Note

R6 does not re-create the extensive closed Performance reliability/deployment/observability requirements. Exact Cloudflare rules, rate thresholds, security tooling, malware scanner, secret manager, backup product, incident roster and deployment topology are AR-001…AR-009 or operations/JIT decisions.

Current clustered coverage after R6:

```text
AR-000-P Performance                  166  CLOSED
AR-000-A Analytics                    216  CLOSED
Cross-cutting Payments                  1  ACCEPTED / PRODUCT LAW PROPAGATED
R1 System & Application Boundaries      6  COMPLETE
R2 Identity / Access / Consent           8  COMPLETE
R3 State / Storage / Lifecycle           7  COMPLETE
R4 Transactions / Async / Realtime       3  COMPLETE
R5 Content / Translation / Media          6  COMPLETE
R6 Security / Operations                  4  COMPLETE
----------------------------------------------------
TOTAL ACCEPTED ARQs                    417
```

**Next:** one global AR-000 closure audit. No additional focused concern round is planned.



# 8G. AR-000 Global Closure Audit

- **Audit date:** 2026-08-16
- **Verdict:** **PASS — AR-000 COMPLETE / FROZEN**
- **Stable requirement version:** `v1.0.0`
- **Requirement count:** **417 accepted/locked ARQs**
- **Next phase:** `AR-001 System Shape & Runtime Topology`

## 8G.1 Mechanical integrity proof

The frozen register was mechanically verified before freeze:

```text
ARQ-PERF-001    ... ARQ-PERF-166       166 contiguous
ARQ-AN-001      ... ARQ-AN-216         216 contiguous
ARQ-PAY-001                                1
ARQ-SYS-001     ... ARQ-SYS-006           6 contiguous
ARQ-IAM-001     ... ARQ-IAM-008           8 contiguous
ARQ-STATE-001   ... ARQ-STATE-007         7 contiguous
ARQ-ASYNC-001   ... ARQ-ASYNC-003         3 contiguous
ARQ-CONTENT-001 ... ARQ-CONTENT-006       6 contiguous
ARQ-SEC-001     ... ARQ-SEC-002           2 contiguous
ARQ-OPS-001     ... ARQ-OPS-002           2 contiguous
-------------------------------------------------------
TOTAL                                      417
```

All R1–R6 clustered ARQs contain the required requirement/source/strength/architectural-implication/workstream/blocking/status metadata. Existing Performance and Analytics ARQ history was not rewritten during R1–R6.

## 8G.2 Required Product Law surface coverage

The `02_OPEN_WORK` AR-000 exit checklist is covered as follows:

| Required surface | Frozen requirement home | Closure status |
|---|---|---|
| System/runtime shape and product-space evolution | `ARQ-SYS-*`, `ARQ-PERF-*`, `ARQ-OPS-*` | COVERED |
| Phoenix/LiveView/Ash/application boundaries | closed realtime Performance ARQs + `ARQ-SYS-*` + Product-Law-specific `ARQ-CONTENT-002/006` | COVERED; exact HOW deferred to AR-001/002 |
| Identity/authentication/authorisation/actor/field privacy | `ARQ-IAM-*`, applicable Analytics privacy ARQs | COVERED |
| Consent and audit | `ARQ-IAM-006/007`, applicable Analytics/State ARQs | COVERED |
| Versioning/immutability | `ARQ-STATE-002`, closed Analytics/Performance history rules, Product-Law-specific content requirements | COVERED |
| PostgreSQL authority and acceleration distinction | closed `ARQ-PERF-*` authority/cache/database requirements | COVERED |
| Transactions/concurrency/idempotency | closed `ARQ-PERF-*` + `ARQ-ASYNC-*` + `ARQ-PAY-001` | COVERED |
| Browser/object/CDN/protected storage | `ARQ-STATE-001`, `ARQ-CONTENT-005/006`, closed Performance caching law | COVERED |
| Durable async/scheduling | closed `ARQ-PERF-*` + `ARQ-ASYNC-001/002` | COVERED |
| PubSub/realtime/LiveView observation | closed `ARQ-PERF-*` realtime surface | COVERED |
| Notifications | `ARQ-ASYNC-001` | COVERED |
| Content/translation/media | `ARQ-CONTENT-*` | COVERED |
| External integrations/provider boundaries | `ARQ-PAY-001`, `ARQ-ASYNC-003`, `ARQ-CONTENT-006` | COVERED |
| Privacy/deletion/retention/legal hold | `ARQ-IAM-*`, `ARQ-STATE-003..007`, applicable Analytics privacy ARQs | COVERED |
| Backup/restore | `ARQ-STATE-006`, `ARQ-OPS-002`, closed Performance recovery requirements | COVERED |
| Analytics/reporting/experimentation | `ARQ-AN-001..216` | CLOSED / COVERED |
| Deployment/degradation/reliability/observability | closed `ARQ-PERF-*` + `ARQ-OPS-*` | COVERED |
| Security/abuse/upload protections | `ARQ-IAM-*`, `ARQ-SEC-*` | COVERED |
| Multi-node/performance/scaling | closed `ARQ-PERF-001..166` | CLOSED / COVERED |

## 8G.3 Authority and boundary audit

**PASS.** The frozen AR-000 surface preserves the required separation:

```text
AR-000 = WHAT must be true
AR-001…AR-009 = HOW architecture makes it true
04_DOMAIN_MAP = WHO owns concrete business truth
JIT dossiers = implementation-grade domain/action detail
```

- No new R1–R6 requirement assigns final concrete domain ownership.
- The earlier experimentation ownership/mechanism leakage remains historically preserved but is explicitly corrected by `AMEND-AN-001`, `AMEND-AN-002` and `INTERP-AN-002`.
- Exact libraries, adapters/Behaviours, Ash Resources, tables, migrations, indexes, Redis keys, TTLs, worker names, PubSub topics, endpoint shape and deployment topology remain downstream unless Product Law itself explicitly mandates a technology boundary.
- Product-Law-named mechanisms such as Paystack launch gateway, Oban for named durable work, Gettext plus Ash-backed runtime translation data, Phoenix PubSub/LiveView direction and Cloudflare direction remain requirements only to the extent already made authoritative upstream; exact implementation detail remains Architecture work.

## 8G.4 Contradiction and unresolved-gate audit

**PASS.** No unresolved contradiction was found that prevents Architecture workstreams from beginning. Remaining open questions are correctly retained as downstream expert/vendor/Architecture gates rather than guessed inside AR-000. Representative examples include Paystack provider behaviour (`OQ-004`), translation resource detail (`OQ-013`), Cloudflare edge/cache design (`OQ-014`), live/recording/provider validation, retention-duration expert decisions, external processor behaviour, exact auth package, abuse thresholds, RPO/RTO values and OQ-039 implementation-grade per-action performance mapping.

These gates may block the affected later capability/Feature Pack, but they do not represent missing AR-000 Product Law.

## 8G.5 AR-000 completion test

The v0.16.0 process correction defined the completion test as:

> **Can AR-001…AR-009 proceed without inventing Product Law and without missing a material architecture constraint?**

**Answer: YES.**

The nine Architecture workstreams all have routed requirement inputs. Additional engineering best practice can now be decided as `ARC-nnn` Architecture Law rather than expanding AR-000.

## 8G.6 Formal closure verdict

`AR-000 Architecture Requirement Extraction` is **CLOSED and FROZEN at v1.0.0**.

Rules after freeze:

1. Do not reopen Performance or Analytics for optimisation ideas or implementation preferences.
2. Do not add new ARQs merely because Architecture discovers a preferred pattern.
3. Reopen/amend AR-000 only for a genuine upstream Product Law change, contradiction, expert invalidation or material newly approved business direction.
4. Compatible post-freeze requirement additions/amendments use the normal append-only SemVer/history process; incompatible changes require explicit supersession and appropriate major-version treatment.
5. Begin `AR-001 System Shape & Runtime Topology` immediately.


# 9. Change Log


## v1.0.0 — 2026-08-16 — AR-000 stable freeze / global closure PASS
- SemVer transition: `v0.22.0 → v1.0.0`.
- Completed the one global AR-000 closure/coverage/boundary audit.
- Mechanical proof confirmed **417** accepted ARQs with every numbered family contiguous and all R1–R6 clustered ARQs carrying required trace/routing metadata.
- Confirmed full coverage of the AR-000 source checklist in `02_OPEN_WORK`: system/runtime shape; Phoenix/LiveView/Ash/application boundaries; IAM/consent/audit; versioning/immutability; PostgreSQL authority/acceleration; transactions/idempotency; storage/CDN/browser state; async/realtime/notifications; content/translation/media/integrations; privacy/deletion/backup; analytics; deployment/degradation/observability; security; multi-node/performance/scaling.
- Confirmed no remaining Product-Law contradiction blocks Architecture. Open expert/vendor/Architecture gates remain downstream and were not guessed.
- Confirmed final domain ownership and exact implementation mechanisms remain deferred correctly; historical experimentation leakage remains corrected through prior amendment entries.
- Froze `ARCHITECTURE_REQUIREMENTS_WORKING.md` as the stable AR-000 handoff.
- Advanced the planning tracker to `02_OPEN_WORK_v1.2.2.md`, marking Phase 1 COMPLETE and `AR-001 System Shape & Runtime Topology` NEXT without changing Product Law v1.2.1.
- **Next:** begin AR-001 and create `ARC-nnn` decisions for HOW the platform satisfies the frozen ARQs.



## v0.22.0 — 2026-08-16 — R6 Security, Operations, Deployment & Cross-Cutting Closure Coverage
- SemVer transition: `v0.21.0 → v0.22.0`.
- Completed the final remaining extraction cluster under the extraction-first AR-000 operating mode; no focused Grill-Me was required.
- Added `ARQ-SEC-001`, `ARQ-SEC-002`, `ARQ-OPS-001` and `ARQ-OPS-002`.
- Captured layered distributed abuse/non-enumeration controls, secure upload quarantine/inspection, named cross-functional incident/release no-go evidence and full-runtime recoverability including configuration/secrets/object state.
- Reused closed Performance reliability/deployment/observability/recovery law and R2/R3 access/deletion law instead of duplicating it.
- Preserved all prior 413 ARQs unchanged.
- Requirement total is now **417 accepted/locked ARQs**.
- All planned remaining clusters R1–R6 are complete; one global AR-000 closure audit is next.



## v0.21.0 — 2026-08-16 — R5 Content, Translation, Media & External Integrations clustered extraction
- SemVer transition: `v0.20.0 → v0.21.0`.
- Completed R5 under extraction-first AR-000 mode; no focused Grill-Me was required.
- Added `ARQ-CONTENT-001` through `ARQ-CONTENT-006` (6 clustered requirements).
- Captured governed bilingual content/version parity; the Product-Law-mandated Gettext + Ash-backed-runtime-content + immutable-delivery-reference translation boundary while leaving OQ-013 details open; risk-based approval/publication/withdrawal; minimum-signal access-first discovery/personalisation; multilingual SEO/private-indexing boundaries; and platform-owned media access/policy metadata behind external live/streaming providers.
- Did not design exact resources, content tables, search/index engines, CDN/cache rules, object layout or provider plans.
- Preserved all prior 407 ARQs unchanged.
- Requirement total is now **413 accepted/locked ARQs**.
- R6 — Security, Operations, Deployment & Cross-Cutting Closure Coverage — is next.



## v0.20.0 — 2026-08-16 — R4 Transactions, Async, Realtime & Notifications clustered extraction
- SemVer transition: `v0.19.0 → v0.20.0`.
- Completed R4 under extraction-first AR-000 mode; no focused Grill-Me was required.
- Reused closed Performance transaction/outbox/queue/realtime/idempotency law rather than duplicating it.
- Added only `ARQ-ASYNC-001` through `ARQ-ASYNC-003`: governed notification policy/durable delivery, recoverable scheduled publication/programme release, and verified repeat-safe provider callback/reconciliation boundaries.
- Preserved OQ-004 as the unresolved Paystack provider-behaviour gate and did not invent provider retry/webhook/proration/refund details.
- Preserved all prior 404 ARQs unchanged.
- Requirement total is now **407 accepted/locked ARQs**.
- R5 — Content, Translation, Media & External Integrations — is next.



## v0.19.0 — 2026-08-16 — R3 State Authority, Storage & Records Lifecycle clustered extraction
- SemVer transition: `v0.18.0 → v0.19.0`.
- Completed R3 under extraction-first AR-000 mode; no focused Grill-Me was required.
- Added `ARQ-STATE-001` through `ARQ-STATE-007` (7 clustered requirements).
- Reused the closed Performance durable-authority/cache/recovery doctrine instead of duplicating it.
- Added sensitivity-based client/object/CDN/protected-storage boundaries; cross-product immutable/superseding history; explicit lifecycle-state semantics; irreversible distributed full deletion; isolated obligation/legal-hold retention; deletion-safe backup/restore; and secure participant export.
- Did not choose storage vendor, cache key, signed-URL implementation, deletion worker topology, retention durations, backup product, schemas/tables/indexes or record-owning domains.
- Preserved all prior 397 ARQs unchanged.
- Requirement totals: 166 Performance + 216 Analytics + 1 Payments + 6 System + 8 IAM + 7 State = **404 accepted/locked ARQs**.
- R4 — Transactions, Async, Realtime & Notifications — is next.



## v0.18.0 — 2026-08-16 — R2 Identity, Authentication, Authorisation, Consent & Audit clustered extraction
- SemVer transition: `v0.17.0 → v0.18.0`.
- Completed R2 under extraction-first AR-000 mode; no focused Grill-Me was required.
- Added `ARQ-IAM-001` through `ARQ-IAM-008` (8 clustered requirements).
- Captured explicit scoped multi-role actor semantics; purchaser/recipient/participant separation; launch authentication and verified-email gates; risk-based MFA/session/device/recovery; privileged/break-glass controls; practitioner relationship-scoped access; purpose-specific consent and withdrawal; immutable/minimised audit/security evidence; and provenance-preserving identity merge/compromise handling.
- Did not choose an auth package, MFA provider, Ash policy implementation, exact role/domain ownership, consent schema, audit storage or token/session representation.
- Preserved all prior 389 ARQs unchanged.
- Requirement totals: 166 Performance + 216 Analytics + 1 Payments + 6 System + 8 IAM = **397 accepted/locked ARQs**.
- R3 — State Authority, Storage & Records Lifecycle — is next.



## v0.17.0 — 2026-08-16 — R1 System & Application Boundaries clustered extraction
- SemVer transition: `v0.16.0 → v0.17.0`.
- Completed R1 under the corrected extraction-first AR-000 operating mode; no focused Grill-Me was required.
- Added six clustered requirements: `ARQ-SYS-001` through `ARQ-SYS-006`.
- Locked one operating platform with controlled product spaces; shared platform capability versus product-experience separation; explicit future-space activation/visibility; South-Africa-first defaults without reusable-platform hard-coding; mature-platform compatibility with MVP restraint; and a strict LearnDash legacy/non-authority clean-cutover boundary.
- Did not pre-name final domains, Ash Resources, modules, tables, routes, adapters, tenancy mechanisms, or other HOW/WHO decisions.
- Explicitly deferred provider-specific live/media, translation-resource, notification/provider, cache implementation, and exact Phoenix/LiveView/Ash structure to later clusters or Architecture Law.
- Preserved all previous 383 ARQs and all Performance/Analytics closure history unchanged.
- Requirement totals: 166 Performance + 216 Analytics + 1 Payments + 6 System = **389 accepted/locked ARQs**.
- R2 — Identity, Authentication, Authorisation, Consent & Audit — is next.




## v0.16.0 — 2026-08-16 — AR-000 scope-discipline corrective pass
- SemVer transition: `v0.15.0 → v0.16.0`.
- Adopted the post-Analytics process review warning that AR-000 was beginning to overgrow its intended WHAT-only role.
- Changed the remaining AR-000 default from repeated focused Grill-Me to **Product Law extraction + meaningful requirement clustering**, with focused Grill-Me reserved for unresolved material ambiguities.
- Added an explicit AR-000 completion test: AR-001…AR-009 can proceed without inventing Product Law and without missing a material constraint.
- Preserved all 383 existing ARQs and all Performance/Analytics closure history; no ARQ was deleted or renumbered.
- Added `AMEND-AN-001` so `ARQ-AN-206` no longer pre-names a final Experiment domain; final ownership is deferred to `04_DOMAIN_MAP.md`.
- Added `AMEND-AN-002` so `ARQ-AN-207` requires library decoupling/replaceability but does not preselect an Elixir Behaviour/adapter implementation; exact abstraction is deferred to ARC work.
- Added `INTERP-AN-002` clarifying FunWithFlags/Bandera are Architecture evidence candidates, not AR-000 or Product Law mechanism choices.
- Added `PROCESS-AR000-001` and `PROCESS-AR000-002` to constrain future AR-000 granularity and keep closed Performance/Analytics surfaces closed absent a real reopening trigger.
- Updated the current governing source-pack metadata to the non-semantic v1.2.1 hygiene pack while preserving historical v1.1/v1.2 source citations inside earlier ARQs.

## v0.15.0 — 2026-08-16 — Formal Analytics closure + Product Law v1.2 propagation
- SemVer transition: `v0.14.0 → v0.15.0`.
- Accepted Analytics Closure recommendations AC.1–AC.10 in full.
- Propagated Paystack launch-gateway and first-party experimentation decisions into the authoritative Product Law v1.2 pack while preserving v1.1 unchanged.
- Added `ARQ-AN-210` through `ARQ-AN-216` for experiment-history/privacy compatibility, allocation stability, concurrent-experiment interaction isolation, variant-safe caching, clean semantic URLs with internal cache segmentation, decision-population/traffic-quality governance, and safe assignment failure/recovery.
- Locked that normal experiment treatment assignment/cache partitioning does **not** use visible variant query parameters; campaign attribution and controlled preview/debug parameters remain separate allowed concerns.
- Added `PROP-AN-001`, `PROP-PAY-001`, `ROUTE-AN-001`, and `INTERP-AN-001`.
- Added AR-001 as a downstream consumer for topology-sensitive Analytics requirements.
- Formally closed `AR-000-A` with `ARQ-AN-001` through `ARQ-AN-216`.
- FunWithFlags/Bandera/equivalent selection remains a downstream Architecture proof and does not block Analytics closure.
- Requirement totals: 166 Performance + 216 Analytics + 1 cross-cutting Payments = **383 accepted/locked ARQs**.

## v0.14.0 — 2026-08-16 — Experiment assignment-layer boundary and candidate proof
- SemVer transition: `v0.13.0 → v0.14.0`.
- Recorded the user's acceptance of the FunWithFlags/Bandera experimentation architecture recommendation without prematurely locking either library as Product Law.
- Added `ARQ-AN-206` through `ARQ-AN-209` (4 requirements).
- Locked the Experiment domain as the authority for experiment semantics/evidence while a reusable deterministic flag/variant primitive performs assignment beneath it.
- Locked a platform-owned assignment adapter/behaviour boundary so product code does not couple directly to FunWithFlags, Bandera, or another implementation library.
- Locked deterministic sticky mutually-exclusive weighted A/B/n assignment; independent boolean flags alone are insufficient unless augmented by deterministic exclusive bucketing, and random-per-request/time percentage gates are prohibited for treatment assignment.
- Required Architecture to prove FunWithFlags, Bandera, or a documented equivalent/custom bucketing adapter against multivariate assignment, persistence/reconstruction, multi-node behaviour, failure/cache semantics, maturity, observability, privacy/identity handling, and dependency risk before selecting the mechanism.
- Preserved all prior Performance, Analytics A1–A7, built-in experimentation, Paystack, and Total Income requirements unchanged.
- Requirement totals: 166 Performance + 209 Analytics + 1 cross-cutting Payments = **376 accepted/locked ARQs**.
- Formal Analytics Closure Audit remains next; Product Law propagation for built-in experimentation and Paystack remains mandatory before AR-000-A closure.

## v0.13.0 — 2026-08-16 — A7 decision governance + first-party A/B/n experimentation
- SemVer transition: `v0.12.0 → v0.13.0`.
- Accepted A7 recommendations with an explicit user amendment to A7.20: experimentation is **required and first-party**, not deferred/future-only.
- Added `ARQ-AN-162` through `ARQ-AN-183` for targets, survey evidence, completion outlook/model governance, authority-separated decision gates, and the amended built-in experimentation requirement.
- Added `ARQ-AN-184` through `ARQ-AN-205` for the first-party experimentation capability: page duplicate-and-edit authoring; clean/canonical URLs; deterministic sticky random assignment; anonymous-to-known handling; eligible traffic/allocation; exposure logging; primary/guardrail metrics; authoritative sales/revenue and time-to-conversion; predeclared power/MDE/statistical design; sequential-testing/peeking controls; multiplicity control; SRM health checks; effect-size/uncertainty reporting; lifecycle/stop/invalid states; email/message A/B/n testing; immutable PostgreSQL experiment evidence; searchable historical experiment learning; privacy/consent; and protected-invariant exclusions.
- Recorded that Product Law currently has no general experimentation mandate, so the user-locked capability requires an explicit upstream Product Law/DEC amendment before AR-000-A closure.
- Preserved all prior Performance, Analytics A1–A6, Paystack, and Total Income requirements unchanged.
- Requirement totals: 166 Performance + 205 Analytics + 1 cross-cutting Payments = **372 accepted/locked ARQs**.
- Marked the formal Analytics Closure Audit as next, with Product Law propagation for experimentation and Paystack as explicit prerequisites.


## v0.12.0 — 2026-08-16 — A6 analytics architecture / data-pipeline governance
- SemVer transition: `v0.11.0 → v0.12.0`.
- Accepted A6 recommendations in full.
- Added stable `ARQ-AN-128` through `ARQ-AN-161` (34 requirements).
- Locked PostgreSQL/read-model-first and warehouse-ready evolution, OLTP protection, analytical logical boundaries, freshness-driven projections, incremental-plus-rebuild semantics, evidence-gated streaming/CDC/warehouse introduction, authoritative event origins, durable commit bridges, event identity/schema/quarantine, privacy-aware failed-event handling, late/out-of-order convergence, replay/backfill/audit, data-quality and freshness gates, provenance/lineage, deletion-safe analytical copies and restore, CDC operations, no warehouse authority, no silent BI-to-OLTP feedback, semantic portability, pipeline observability, representative analytics performance testing, and the overarching rebuildable-downstream-projection doctrine.
- Preserved all prior Performance, Analytics A1–A5, Paystack, and Total Income requirements unchanged.
- Requirement totals: 166 Performance ARQs + 161 Analytics ARQs + 1 cross-cutting Payments ARQ = 328 accepted/locked requirements.
- Marked the Analytics completeness / closure audit as next rather than assuming another round is necessary.


## v0.11.0 — 2026-08-16 — A5 dashboard/decision-support governance
- SemVer transition: `v0.10.0 → v0.11.0`.
- Accepted A5 recommendations in full.
- Added stable `ARQ-AN-100` through `ARQ-AN-127` (28 requirements).
- Locked role-scoped dashboard classes; data-boundary authorisation; row/field restrictions; safe drill-down; freshness/date/filter semantics; governed versus exploratory content; alert governance; export authorisation, lifecycle, audit and CSV-injection protection; scheduled-delivery controls; finance reconciliation drill-down; and Total Income breakdown by `income_type`.
- Preserved all prior Performance, Analytics A1–A4, Paystack, and Total Income requirements unchanged.
- Marked A6 — Data Warehouse/Read Models, Event Pipeline, Data Quality, Reconciliation & Analytics Architecture — as next.

## v0.10.0 — 2026-08-16 — A4 finance/commercial analytics + Paystack + total-income refinements
- SemVer transition: `v0.9.0 → v0.10.0`.
- Accepted A4 recommendations in full.
- Added stable `ARQ-AN-069` through `ARQ-AN-098` (30 requirements).
- Added `ARQ-AN-099` to lock the user refinement that management/commercial revenue reporting includes **all income** in the selected scope and separates every included amount by governed income type.
- Added cross-cutting `ARQ-PAY-001`: Paystack is now user-locked as the first/launch payment gateway, promoting the existing Product Law wording from provisional to locked; upstream Product Law amendment remains explicitly pending.
- Preserved the distinction between commercial income, verified payments/cash, MRR/ARR run-rate, refunds/disputes, tax/fees, unit economics, profit/margin, and formal accounting recognised revenue.
- Requirement totals: 166 Performance ARQs + 99 Analytics ARQs + 1 cross-cutting Payments ARQ = 266 accepted/locked requirements.
- Preserved every v0.1.0 through v0.9.0 requirement and change-history entry unchanged.
- Marked A5 — Dashboards, Roles, Drill-down, Alerts, Exports & Decision-Support UX — as next.



## v0.9.0 — 2026-08-16 — A3 acquisition, funnels, attribution and campaign measurement requirements
- SemVer transition: `v0.8.0 → v0.9.0`.
- Preserved the formally closed AR-000-P Performance surface (`ARQ-PERF-001` through `ARQ-PERF-166`) and all A1–A2 Analytics requirements (`ARQ-AN-001` through `ARQ-AN-046`) unchanged.
- Accepted A3 recommendations in full.
- Added stable `ARQ-AN-047` through `ARQ-AN-068` (22 requirements).
- Locked distinct acquisition-time semantics, first-acquisition preservation, campaign taxonomy/identity, raw-evidence versus normalised classification, attribution-model/version semantics, model comparison without conversion multiplication, direct/unknown interpretation, cross-domain continuity constraints, explicit anonymous-to-known transitions, anti-fingerprinting privacy rule, purpose/consent-aware measurement, marketing-withdrawal behaviour, authoritative conversion origin, deterministic conversion deduplication, modelled-conversion non-authority, versioned attribution windows, refund/chargeback chronology, sensitive-data exclusion from advertising measurement, vendor-report reconciliation, and the overarching acquisition/attribution doctrine.
- Added exact Product Law source, source classification, workstream routing, blocking classification, and `ARC_PENDING` status directly to every A3 ARQ.
- Requirement total increased from 212 to 234.
- Marked A4 — Revenue, Finance, Refunds, Subscriptions, MRR/ARR, LTV & Commercial Reporting — as next.


## v0.8.0 — 2026-08-16 — A2 user lifecycle, cohort, engagement, retention and churn requirements
- SemVer transition: `v0.7.0 → v0.8.0`.
- Preserved the formally closed AR-000-P Performance surface (`ARQ-PERF-001` through `ARQ-PERF-166`) and all A1 Analytics requirements (`ARQ-AN-001` through `ARQ-AN-022`) unchanged.
- Accepted A2 recommendations in full.
- Added stable `ARQ-AN-023` through `ARQ-AN-046` (24 requirements).
- Locked platform-specific activity semantics, distinct active-state concepts, governed value engagement, product-specific activation, business-versus-analytical cohort semantics, historical enrolment preservation, static/dynamic cohort semantics, temporal property semantics, retention definitions/cadence/time models/denominators, governed DAU/WAU/MAU use, churn distinctions, voluntary/involuntary churn, authoritative churn timing, reactivation history, dormancy separation, authoritative completion, safety-withdrawal distinction, Day-60 versus late catch-up state, repeat-enrolment history, adoption denominators, and overarching lifecycle doctrine.
- Added exact Product Law source, source classification, workstream routing, blocking classification, and `ARC_PENDING` status directly to every A2 ARQ.
- Requirement total increased from 188 to 212.
- Marked A3 — Acquisition, Funnels, Attribution & Campaign Measurement — as next.



## v0.7.0 — 2026-08-16 — A1 Analytics truth/metric/event-governance requirements
- SemVer transition: `v0.6.1 → v0.7.0`.
- Preserved the formally closed AR-000-P Performance surface (`ARQ-PERF-001` through `ARQ-PERF-166`) and all prior SemVer/change history.
- Accepted A1 recommendations in full.
- Added stable `ARQ-AN-001` through `ARQ-AN-022` (22 requirements).
- Locked Analytics-as-projection/non-authority, governed metric semantics, explicit user populations, session non-authority, governed/versioned event contracts, distinct event-time semantics, authoritative conversion definitions, governed funnels/cross-session journeys, financial-truth separation, distinct commercial measures, attribution-as-interpretation, metric versioning, deterministic reconciliation, reconcilable realtime counters, analytics data-quality controls, Product-Law deletion/anonymisation, exclusion of detailed health/journal data from general analytics, governed identity stitching, KPI ownership/promotion, and the overarching Analytics truth doctrine.
- Added exact Product Law source, source classification, workstream routing, blocking classification, and `ARC_PENDING` status directly to every new Analytics ARQ.
- Requirement total increased from 166 to 188.
- Marked A2 — Users, Cohorts, Engagement, Retention, Churn & Product Behaviour — as next.


## v0.6.1 — 2026-08-16 — Formatting-only patch
- SemVer transition: `v0.6.0 → v0.6.1`.
- Repaired literal newline escape characters in the newly appended v0.6.0 closure, next-step and change-log blocks.
- No ARQ, amendment, interpretation, source trace, closure verdict or governance meaning changed.
- `ARQ-PERF-001` through `ARQ-PERF-166` remain identical in meaning and numbering.

## v0.6.0 — 2026-08-16 — AR-000-P formal Performance closure and traceability
- Preserved all v0.1.0 through v0.5.0 requirements and history.
- Accepted Performance Closure recommendations PC.1–PC.5 in full.
- Formally closed AR-000-P with `ARQ-PERF-001` through `ARQ-PERF-166` retained as the append-only Performance requirement surface.
- Added a permanent keyed source-trace/classification/routing addendum for every Performance ARQ.
- Added `AMEND-PERF-001` clarifying that Oban is already the locked mechanism for the Product-Law-named heavy/durable async and notification scopes, while queue/worker design remains Architecture work.
- Added `AMEND-PERF-002` clarifying transaction-pooling compatibility from the beginning and PgBouncer transaction mode at an Architecture-defined measurable production-scale gate.
- Added `INTERP-PERF-001` clarifying approved acceleration-toolbox versus per-domain `NONE` applicability and specific upstream technology mandates.
- Closure audit found no unresolved Product-Law contradiction or escalation.
- Marked AR-000-A — Analytics, Reporting, Funnels & Financial Intelligence Grill — as next.

## v0.5.0 — 2026-08-16 — P8 reliability/uptime/recovery requirements
- Preserved all v0.1.0 through v0.4.0 requirements and history.
- Accepted P8 recommendations in full.
- Added stable `ARQ-PERF-139` through `ARQ-PERF-166` (28 requirements).
- Locked availability classes, realistic high-availability doctrine, application-node fault containment, bounded OTP supervision, dependency-aware supervision boundaries, startup/liveness/readiness semantics, dependency-outage handling, fenced PostgreSQL failover, backup-versus-HA separation, RPO/RTO classification, bounded deadlines/retry budgets, failure isolation/bulkheads, overload-without-restart doctrine, degraded-mode proof, safe startup, rolling-version compatibility, expand/transition/contract migrations, draining, rollback/forward-recovery, risk-based canary rollout, evidence-based capacity headroom, disaster-recovery failure-domain separation, controlled failure injection, exercised recovery runbooks, auditable emergency controls, incident-driven upstream amendment, and the overarching reliability doctrine.
- Requirement total increased from 138 to 166.
- Completed the eight substantive Performance Grill rounds and marked the formal AR-000-P closure/contradiction/coverage audit as next.

## v0.4.0 — 2026-08-16 — P7 realtime/PubSub/LiveView requirements
- Preserved all v0.1.0 through v0.3.0 requirements and history.
- Accepted P7 recommendations in full.
- Added stable `ARQ-PERF-114` through `ARQ-PERF-138` (25 requirements).
- Locked realtime-as-projection authority boundaries, reconnect/remount repeat safety, visible connectivity uncertainty, scoped/authorised PubSub use, minimal payloads, Presence ephemerality, bounded LiveView state/work, slow-client/backlog control, observation coalescing, ordering/duplication tolerance, prompt access revocation, action-boundary re-authorisation, controlled WebSocket degradation, database/fan-out amplification protection, topology deferral, realtime observability, realtime pressure testing, and node-loss reconstruction.
- Requirement total increased from 113 to 138.
- Marked P8 — Reliability, Uptime, Failure Isolation, Deployment & Recovery — as next.

## v0.3.0 — 2026-08-16 — P6 async/queue/backpressure requirements
- Preserved all v0.1.0 and v0.2.0 requirements and history.
- Accepted P6 recommendations in full.
- Added stable `ARQ-PERF-087` through `ARQ-PERF-113` (27 requirements).
- Locked durable intent, queue isolation, priority/isolation separation, bottleneck-derived concurrency, explicit backlog/backpressure, bounded jittered retry, failure classification, provider-outage coordination, retry-exhaustion governance, re-execution/idempotency, atomic durable enqueue/outbox semantics, bounded fan-out, business-effective scheduling, cluster-safe periodic work, precondition revalidation, sensitive-payload minimisation, graceful shutdown/orphan recovery, worker-topology flexibility, queue observability/SLOs, poison-job quarantine, critical-work protection, PostgreSQL resource budgeting, and async pressure testing.
- Requirement total increased from 86 to 113.
- Marked P7 — Realtime, PubSub, LiveView, WebSockets & Fan-out — as next.

## v0.2.0 — 2026-08-16 — P5 database/query/PostgreSQL scaling requirements
- Preserved all v0.1.0 requirements and history.
- Accepted P5 recommendations in full.
- Added stable `ARQ-PERF-064` through `ARQ-PERF-086` (23 requirements).
- Locked authoritative-database-first optimisation, N+1 prevention, bounded reads, evidence-driven index design, query-plan proof, deterministic pagination, streaming/batching, finite connection budgets, pool backpressure, future transaction-pooling compatibility, stale-tolerant replica rules, analytics/OLTP isolation, justified materialised views, evidence-gated partitioning, projection-only denormalisation, autovacuum/statistics health, production migration safety, database observability, bounded query timeouts, representative-cardinality testing, and evidence-led scaling topology.
- Requirement total increased from 63 to 86.
- Marked P6 — Async Work, Queueing, Backpressure, Scheduling & Worker Saturation — as next.

## v0.1.0 — 2026-08-16 — Initial creation
- Created the cumulative `ARCHITECTURE_REQUIREMENTS_WORKING.md`.
- Locked the append-only historical maintenance rule.
- Captured all accepted AR-000-P decisions from P1, P2, P3, and P4.
- Captured the explicit P1.2 scale-optimisation refinement.
- Captured the explicit P1.3 load/pressure-testing refinement.
- Captured the strengthened P2.4 Core Web Vitals floor.
- Created stable `ARQ-PERF-001` through `ARQ-PERF-063`.
- Marked P5 as the next planned Performance Grill-Me round.

# 10. Post-freeze governed amendment — Product Law v1.3.0 / Stage 3A.2

## 10.1 Amendment control and authority boundary

- **Amendment version:** v1.1.0
- **Amendment date:** 2026-09-03
- **Amendment authority:** Product Law v1.3.0 §§21M–21Q and `DEC-294`–`DEC-298`
- **Stage:** Stage 3A.2 — Governed AR-000 Amendment
- **Stage 3A.1 evidence:** [`TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md`](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md), especially its consolidated treatment register and provenance audit
- **Historical preservation:** all 417 v1.0.0 ARQs and their original wording/status remain in this cumulative document; the byte-preserved v1.0.0 artifact is also retained in `docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`.
- **Semantic amendment targets:** none. The Stage 3A.1 conclusion that no exact historical ARQ requires semantic mutation is retained.
- **Architecture decision boundary:** no `ARC-nnn` decision, final domain owner, implementation mechanism, schema, package, queue, provider, threshold or identifier encoding is selected here.

This section is a post-freeze supplement. It does not rewrite the historical v1.0.0 freeze closure, source fields or change-log entries. The new Product source is attached through the governed provenance table below, and the new requirements are appended after that table.

## 10.2 POST-FREEZE PRODUCT-SOURCE PROPAGATION SUPPLEMENT

The records below add valid v1.3.0 provenance to existing ARQs without duplicating or rewriting the old entries. Every record is dated 2026-09-03 and points to the Stage 3A.1 provenance audit. `SOURCE_REFRESH_ONLY` corresponds to the five complete source-refresh rows. `PARTIAL_SOURCE_REFRESH_PLUS_ADDITIVE` corresponds to the three reclassified amendment rows that retain only the valid `ARQ-STATE-002` provenance component.

There are **17 source-to-ARQ records** and **10 distinct existing ARQs** receiving post-freeze provenance. The historical wording and historical status of every target remain unchanged.

### Valid source-propagation mappings

| Mapping class | Stage 3A.1 evidence row | Existing ARQ | New Product source | Date | Why the source applies | Historical wording/status | Downstream workstreams affected | Stage 3A.1 provenance reference |
|---|---|---|---|---|---|---|---|
| `SOURCE_REFRESH_ONLY` | Vote limits and retried/concurrent submissions | `ARQ-PERF-025` | `00_PLATFORM_v1.3.0.md §21N.3`; `DEC-295` | 2026-09-03 | Vote-limit correctness under simultaneous submissions is a durable critical-invariant requirement. | Unchanged; historical text and status remain intact. | AR-003, AR-005, AR-008, AR-009 receive the new voting-invariant trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Vote limits and retried/concurrent submissions | `ARQ-PERF-026` | `00_PLATFORM_v1.3.0.md §21N.3`; `DEC-295` | 2026-09-03 | Retried and duplicate vote submissions directly exercise the existing idempotent externally initiated mutation invariant. | Unchanged; historical text and status remain intact. | AR-003, AR-005, AR-008, AR-009 receive the new voting-invariant trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Vote limits and retried/concurrent submissions | `ARQ-PERF-027` | `00_PLATFORM_v1.3.0.md §21N.3`; `DEC-295` | 2026-09-03 | Retried and duplicate vote handling requires idempotency scoped to the intended voting operation and context. | Unchanged; historical text and status remain intact. | AR-003, AR-005, AR-008, AR-009 receive the new voting-invariant trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Vote limits and retried/concurrent submissions | `ARQ-PERF-041` | `00_PLATFORM_v1.3.0.md §21N.3`; `DEC-295` | 2026-09-03 | Duplicate, simultaneous and retried submissions directly match the existing overarching concurrency invariant. | Unchanged; historical text and status remain intact. | AR-003, AR-005, AR-008, AR-009 receive the new voting-invariant trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Proportionate voting anti-abuse controls | `ARQ-SEC-001` | `00_PLATFORM_v1.3.0.md §21N.3`; `DEC-295` | 2026-09-03 | Proportionate controls against repeated voting at abusive volume directly support layered abuse protection at a sensitive entry point. | Unchanged; historical text and status remain intact. | AR-004, AR-008, AR-009 receive the new voting-abuse trace only; exact mechanisms remain deferred. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `PARTIAL_SOURCE_REFRESH_PLUS_ADDITIVE` | Governed research publication and lifecycle | `ARQ-STATE-002` | `00_PLATFORM_v1.3.0.md §21M.4`; `DEC-294` | 2026-09-03 | Immutable published Research meaning directly supports the existing immutable-or-superseding history doctrine, while Research-specific lifecycle coverage is appended as `ARQ-STATE-008`. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-005, AR-006, AR-008 receive the Research provenance trace and new linked coverage. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Material calculation changes create governed versions | `ARQ-STATE-002` | `00_PLATFORM_v1.3.0.md §21O.3`; `DEC-296` | 2026-09-03 | A material calculation meaning change must create a governed version and preserve historical interpretation. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-005, AR-006, AR-008 receive the tool-version trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `PARTIAL_SOURCE_REFRESH_PLUS_ADDITIVE` | Persisted interactive-result version provenance | `ARQ-STATE-002` | `00_PLATFORM_v1.3.0.md §21O.3`; `DEC-296` | 2026-09-03 | Persisted or materially consequential tool output must retain producing-version provenance, with detailed tool coverage appended as `ARQ-STATE-013`. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-006, AR-008 receive the tool provenance trace and new linked coverage. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `PARTIAL_SOURCE_REFRESH_PLUS_ADDITIVE` | Interactive correction and recalculation preserve history | `ARQ-STATE-002` | `00_PLATFORM_v1.3.0.md §21O.5`; `DEC-296` | 2026-09-03 | Tool correction and recalculation must preserve historical meaning, with tool-specific coverage appended as `ARQ-STATE-013`. | Unchanged; historical text and status remain intact. | AR-003, AR-005, AR-007, AR-008 receive the correction trace and new linked coverage. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Dashboards and visualisations remain derived | `ARQ-AN-001` | `00_PLATFORM_v1.3.0.md §21O.5`; `DEC-296` | 2026-09-03 | Dashboards and visualisations present owning-capability truth without becoming authoritative, directly supporting the existing derived-presentation doctrine. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008 receive the tool-derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Dashboards and visualisations remain derived | `ARQ-AN-022` | `00_PLATFORM_v1.3.0.md §21O.5`; `DEC-296` | 2026-09-03 | The source directly supports governed, derived and non-authoritative dashboard/presentation behavior. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008 receive the tool-derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Dashboards and visualisations remain derived | `ARQ-AN-127` | `00_PLATFORM_v1.3.0.md §21O.5`; `DEC-296` | 2026-09-03 | The source names dashboards as derived decision surfaces that may combine owning-capability truth without owning it. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008 receive the tool-derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Dashboards and visualisations remain derived | `ARQ-AN-161` | `00_PLATFORM_v1.3.0.md §21O.5`; `DEC-296` | 2026-09-03 | The source directly supports the downstream-projection and ownership-boundary portion of the Analytics doctrine. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008 receive the tool-derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Analytics, dashboards, leaderboards and reports remain derived | `ARQ-AN-001` | `00_PLATFORM_v1.3.0.md §21Q.8`; `DEC-298` | 2026-09-03 | Analytics, dashboards, leaderboards and reports remain derived presentation rather than underlying business authority. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008, AR-009 receive the cross-capability derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Analytics, dashboards, leaderboards and reports remain derived | `ARQ-AN-022` | `00_PLATFORM_v1.3.0.md §21Q.8`; `DEC-298` | 2026-09-03 | The source directly supports the existing governed derived-presentation doctrine. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008, AR-009 receive the cross-capability derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Analytics, dashboards, leaderboards and reports remain derived | `ARQ-AN-127` | `00_PLATFORM_v1.3.0.md §21Q.8`; `DEC-298` | 2026-09-03 | The source directly supports derived dashboards and other presentation surfaces that do not own the underlying truth. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008, AR-009 receive the cross-capability derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |
| `SOURCE_REFRESH_ONLY` | Analytics, dashboards, leaderboards and reports remain derived | `ARQ-AN-161` | `00_PLATFORM_v1.3.0.md §21Q.8`; `DEC-298` | 2026-09-03 | The source directly supports downstream projection and ownership separation for cross-capability reports and leaderboards. | Unchanged; historical text and status remain intact. | AR-002, AR-003, AR-004, AR-008, AR-009 receive the cross-capability derived-presentation trace only. | [Exact provenance audit](../archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md#exact-provenance-audit-of-former-source-refresh-rows) |

The table has 17 rows: 14 mappings from the five complete source-refresh rows plus three partial source associations attached to additive coverage. The distinct-target count remains 10: `ARQ-PERF-025`, `ARQ-PERF-026`, `ARQ-PERF-027`, `ARQ-PERF-041`, `ARQ-SEC-001`, `ARQ-STATE-002`, `ARQ-AN-001`, `ARQ-AN-022`, `ARQ-AN-127` and `ARQ-AN-161`.

### Source-propagation exclusions and related evidence only

The following mappings are deliberately absent from the valid mapping table. Their ARQs remain related evidence only; no new v1.3.0 provenance is attached to them for the stated source:

| Product source scenario | Related-evidence-only ARQs — no source propagation |
|---|---|
| Voting retry/concurrency, `§21N.3`; `DEC-295` | `ARQ-PERF-032`, `ARQ-PERF-037` |
| Voting anti-abuse, `§21N.3`; `DEC-295` | `ARQ-PERF-025`, `ARQ-PERF-049` |
| Material interactive calculation versions, `§21O.3`; `DEC-296` | `ARQ-AN-014`, `ARQ-AN-141` |
| Persisted interactive-result provenance, `§21O.3`; `DEC-296` | `ARQ-AN-014`, `ARQ-AN-141`, `ARQ-CONTENT-003` |
| Derived interactive dashboards/visualisations, `§21O.5`; `DEC-296` | `ARQ-PERF-114` |
| Cross-capability derived reporting, `§21Q.8`; `DEC-298` | `ARQ-AN-180` |
| Interactive correction/recalculation, `§21O.5`; `DEC-296` | `ARQ-AN-015`, `ARQ-AN-142`, `ARQ-AN-144`, `ARQ-PERF-033` |
| Research publication/lifecycle, `§21M.4`; `DEC-294` | `ARQ-CONTENT-003`, `ARQ-ASYNC-002` |

The exclusions do not weaken the related historical ARQs. They preserve the exact Stage 3A.1 semantic distinction between direct provenance and downstream implementation evidence.

## 10.3 Additive coverage register

The 44 amendment-classified rows and 15 `NEW_ARQ_REQUIRED` rows receive additive governed coverage below. The 12 cluster rows and 18 linked-theme rows are descriptive coverage labels, not additional governed identifier types. Each row maps to at least one resulting ARQ; existing ARQs named in the tables are unchanged unless they appear in the provenance supplement above.

### 12 new descriptive cluster coverage

| Stage 3A.1 descriptive cluster | Resulting governed ARQ(s) | Consolidation / invariant retained |
|---|---|---|
| Bounded Research and Feedback capability modes | `ARQ-SYS-007` | Bounded lightweight and governed modes, explicit capability boundary and no generic survey-builder promise remain one platform-boundary invariant. |
| Research identity, uniqueness and anonymous-linkage truth | `ARQ-IAM-009` | Identity mode, uniqueness promise, truthful anonymity, public participation and no hidden Account linkage share one privacy/identity invariant. |
| Research response lifecycle, including anonymous withdrawal limits | `ARQ-STATE-008` | Versioned instrument meaning, immutable publication, correction/withdrawal/retention/closure and anonymous-withdrawal limits share one Research-record lifecycle. |
| Research follow-up and monitoring-promise boundary | `ARQ-ASYNC-004` | Explicit follow-up/escalation is separated from an accidental universal monitoring or intervention promise. |
| Bounded voting modes and purpose classification | `ARQ-SYS-008` | Lightweight polls, Research polls and governed voting are classified by purpose/consequence rather than a shared widget. |
| Vote lifecycle and integrity-evidence states | `ARQ-STATE-009` | Vote rules, acceptance states, visibility of provisional evidence and integrity treatment share one durable submission contract. |
| Tally, official result and reward boundary | `ARQ-STATE-010` | Accepted tally, governed official result and owner-mediated reward/entitlement fulfilment remain separate authorities in one outcome chain. |
| Voting finalisation and exception outcomes | `ARQ-STATE-011` | Finalisation, adjudication, exception outcomes, ballot privacy and existing safety restrictions share one governed outcome-transition invariant. |
| Bounded interactive-tool capability and administrator configuration | `ARQ-SYS-009` | Approved tool types and bounded administrator configuration are governed together; arbitrary formulas/scripts/code are not a Product promise. |
| Platform Member Reference assignment and identity meaning | `ARQ-IAM-011` | Account assignment, human-facing meaning, non-authority, privacy class, uniqueness and lifecycle continuity form one identifier contract. |
| Platform Member Reference human-usable representation | `ARQ-IAM-013` | Human usability, non-semantic representation, error detection and namespace constraints are one representation invariant; exact encoding remains deferred. |
| Historical Research and Voting truth after Account deletion | `ARQ-STATE-012` | Deletion of an Account relationship is separated from silent rewriting of legitimate response, vote, tally or result history. |

### 18 linked additive theme coverage

| Stage 3A.1 linked additive theme | Resulting governed ARQ(s) | Additive invariant retained and consolidation reason |
|---|---|---|
| Research authority and downstream handoff | `ARQ-SYS-010` | Research responses may initiate/request an owner-mediated action but cannot mutate another capability's durable truth; this is the cross-capability authority invariant. |
| Governed research instrument provenance and lifecycle | `ARQ-STATE-008`, `ARQ-STATE-002` | Research-specific version/lifecycle meaning is appended in `ARQ-STATE-008`; `ARQ-STATE-002` receives only the directly valid provenance supplement. |
| Sensitive Research visibility, targeting and publication | `ARQ-IAM-010` | Purpose-scoped sensitive access, participant visibility, cohort targeting, longitudinal limits and approved publication share one privacy/access boundary. |
| Research incentives and annotation provenance | `ARQ-SYS-010`, `ARQ-STATE-008` | Owner-mediated reward authority belongs to the cross-capability boundary; participant truth versus staff annotation belongs to the Research record lifecycle. |
| Voting participation identity and eligibility | `ARQ-IAM-009` | Voting identity/eligibility, public unauthenticated participation and truthful uniqueness share the participation identity promise. |
| Voting visibility and integrity | `ARQ-STATE-009`, `ARQ-STATE-011` | Provisional/aggregate/final exposure belongs to the submission/outcome state contract; individual voter and ballot-choice privacy belongs to governed finalisation. |
| Voting integrity, status and anti-abuse | `ARQ-STATE-009`, `ARQ-SEC-001` | Durable status/invalidation evidence is new state coverage; the valid anti-abuse source is propagated only to `ARQ-SEC-001`. |
| Voting visibility, adjudication and safety | `ARQ-STATE-011` | Privacy-by-default, scoped operator adjudication and unchanged wellness/competition safety restrictions share one finalisation and exception boundary. |
| Non-authoritative tool result and downstream handoff | `ARQ-STATE-013`, `ARQ-SYS-010` | Tool result authority/version history belongs to the result contract; owner-mediated mutation belongs to the cross-capability boundary. |
| Tool persistence, version and history | `ARQ-STATE-013`, `ARQ-STATE-002` | Tool-specific persistence/version/correction is appended in `ARQ-STATE-013`; `ARQ-STATE-002` receives only direct version provenance. |
| Tool health, safety, access and minimisation | `ARQ-IAM-010` | Sensitive inputs, public/Account/entitlement access distinctions and non-weakened public safety share one purpose/access invariant. |
| Tool explainability, configuration and correction | `ARQ-SYS-009`, `ARQ-STATE-013` | Configuration bounds are system capability; consequence-proportional explanation and history-preserving correction are result lifecycle. |
| Derived presentation and ownership boundary | `ARQ-AN-001`, `ARQ-AN-022`, `ARQ-AN-127`, `ARQ-AN-161` | Existing Analytics ARQs receive exact source propagation; no new Analytics ARQ is needed and no `ARQ-AN-180` propagation occurs. |
| Platform Member Reference security and non-authority | `ARQ-IAM-011` | Non-secret/private-by-default handling and no authentication/authorisation/entitlement power are part of the reference identity contract. |
| Platform Member Reference security and lifecycle | `ARQ-IAM-011` | Uniqueness, immutability, non-reuse, reactivation, deletion, merge and exceptional replacement are one identity lifecycle invariant. |
| Platform Member Reference lookup and beneficiary boundaries | `ARQ-IAM-012` | Minimum-disclosure lookup and beneficiary association are separated from purchaser control, consent, payment and entitlement authority. |
| Cross-capability purpose and authority boundary | `ARQ-SYS-010` | Purpose/consequence determines the capability boundary; Research, Tool, Voting, Member Reference and commercial truth do not silently acquire one another's authority. |
| Shared interaction and ownership boundary | `ARQ-SYS-010` | Shared forms, polls, calculators and dashboards remain reusable interaction primitives, not a shared-write or universal Engagement authority. |

### Product-source coverage check — §§21M–21Q / DEC-294–DEC-298

| Product Law surface | Decision | Governed additive ARQ destination(s) | Existing source-propagation destination(s) | Result |
|---|---|---|---|---|
| `§§21M.1–21M.8` Research and Feedback | `DEC-294` | `ARQ-SYS-007`, `ARQ-IAM-009`, `ARQ-IAM-010`, `ARQ-STATE-008`, `ARQ-ASYNC-004`, `ARQ-SYS-010` | `ARQ-STATE-002` for the exact valid §21M.4 historical-meaning component | COVERED |
| `§§21N.1–21N.6` Voting, Balloting and Competitions | `DEC-295` | `ARQ-SYS-008`, `ARQ-IAM-009`, `ARQ-STATE-009`, `ARQ-STATE-010`, `ARQ-STATE-011`, `ARQ-SYS-010` | `ARQ-PERF-025`, `ARQ-PERF-026`, `ARQ-PERF-027`, `ARQ-PERF-041`, `ARQ-SEC-001` | COVERED |
| `§§21O.1–21O.5` Interactive Tools, Calculators and Decision Aids | `DEC-296` | `ARQ-SYS-009`, `ARQ-IAM-010`, `ARQ-STATE-013`, `ARQ-SYS-010` | `ARQ-STATE-002`, `ARQ-AN-001`, `ARQ-AN-022`, `ARQ-AN-127`, `ARQ-AN-161` | COVERED |
| `§§21P.1–21P.4` Platform Member Reference | `DEC-297` | `ARQ-IAM-011`, `ARQ-IAM-012`, `ARQ-IAM-013` | None | COVERED |
| `§§21Q.1–21Q.10` Cross-capability interaction rules | `DEC-298` | `ARQ-SYS-008`, `ARQ-SYS-010`, `ARQ-IAM-009`, `ARQ-IAM-012`, `ARQ-STATE-010`, `ARQ-STATE-012` | `ARQ-AN-001`, `ARQ-AN-022`, `ARQ-AN-127`, `ARQ-AN-161` | COVERED |

The source check records the Product Law surface, its governing decision, at least one additive destination, and any exact source-propagation destination. No additive ARQ is sourced from an unapproved Product paragraph, and no source-propagation target is used to hide a semantic amendment.

## 10.4 New governed ARQs

The following 16 ARQs are appended in monotonic family order. Each requirement is Product-derived and remains `ARQ_LOCKED / ARC_PENDING`; exact Architecture Law decisions and final ownership remain downstream.

### ARQ-SYS-007 — Research and Feedback capability remains bounded and mode-explicit
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Bounded Research and Feedback capability modes` cluster
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_ARCHITECTURE
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §21M.1`; `01_DECISIONS_v1.3.0.md DEC-294`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** The platform supports two bounded Research/Feedback modes: lightweight interaction/feedback and governed structured research campaigns. Each mode has an explicit purpose, capability boundary, lifecycle and authority path. The platform does not thereby become a general-purpose SurveyMonkey/Typeform-style survey-building platform or an unrestricted instrument authoring/execution surface.
- **Architectural implication:** AR-001/AR-002/AR-003/AR-004/AR-006 must preserve bounded capability classes and their separate authority/lifecycle pressure points without selecting final resources, modules or domain ownership.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-004, AR-006
- **Blocking classification:** PLATFORM_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-SYS-008 — Voting participation modes are bounded by purpose and consequence
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Bounded voting modes and purpose classification` cluster and cross-capability purpose theme
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_ARCHITECTURE
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §21N.1, §21Q.1`; `01_DECISIONS_v1.3.0.md DEC-295`, `DEC-298`
- **Source classification:** EXPLICIT_PRODUCT_DECISION_FLOW
- **Requirement:** The platform distinguishes bounded lightweight opinion polls, Research polls and governed voting/balloting. Competition voting is a governed-voting use case rather than a commitment to a generic civic-election platform. The approved purpose and consequence determine the participation mode, authority, eligibility, lifecycle and finality; a reusable poll or voting widget must not decide those meanings or create shared business authority.
- **Architectural implication:** AR-001/AR-002/AR-003/AR-004/AR-006/AR-008/AR-009 must preserve mode-specific authority and consequence boundaries while leaving exact flow, ownership and implementation to downstream Architecture and Domain work.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-004, AR-006, AR-008, AR-009
- **Blocking classification:** PLATFORM_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-SYS-009 — Interactive tools are bounded approved capabilities with bounded administrator configuration
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Bounded interactive-tool capability and administrator configuration` cluster
- **Status:** ACCEPTED
- **Strength:** LOCKED_PRODUCT_CAPABILITY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21O.1, 21O.5`; `01_DECISIONS_v1.3.0.md DEC-296`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Approved educational tools, calculators, visualisations, quizzes/self-assessments, decision aids, progress views, planning tools, personalised tools and dashboards remain bounded Product capabilities. Authorised staff may configure approved tool types, governed content and bounded parameters, but the platform does not promise arbitrary executable formulas, unrestricted scripts, arbitrary code or a general-purpose no-code/user-programmable execution environment through a CMS or administrator experience.
- **Architectural implication:** AR-001/AR-002/AR-003/AR-004/AR-006/AR-008 must enforce a bounded capability/configuration boundary while leaving validation, authoring representation, exact execution limits and ownership to downstream Architecture, Domain and security work.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-004, AR-006, AR-008
- **Blocking classification:** PLATFORM_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-SYS-010 — Cross-capability purpose and shared interaction do not transfer business authority
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Research authority and downstream handoff`, `Research incentives and annotation provenance`, `Non-authoritative tool result and downstream handoff`, `Cross-capability purpose and authority boundary` and `Shared interaction and ownership boundary` themes
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21M.3, 21M.8, 21O.2, 21O.4, 21Q.1–21Q.6, 21Q.9–21Q.10`; `01_DECISIONS_v1.3.0.md DEC-294`, `DEC-296`, `DEC-298`
- **Source classification:** EXPLICIT_PRODUCT_AUTHORITY_BOUNDARY
- **Requirement:** Purpose and consequence determine which capability owns durable truth. Research/Feedback responses and interactive-tool results may initiate, offer or request an action in another capability, but the owning capability must independently establish authority before changing its truth. Research responses do not become Health Records, Safety & Eligibility, Plans, Temperament, Commerce or Entitlements truth merely because their subject matter overlaps; tool source data remains owned by its source; participation or result evidence does not manufacture payment, discount, voucher, entitlement or prize truth. Participant submissions remain distinguishable from staff annotations and classifications. Shared forms, questions, polls, voting components, calculators and dashboards are reusable interaction or presentation primitives and do not create shared-write ownership or a universal Engagement authority.
- **Architectural implication:** AR-001/AR-002/AR-003/AR-004/AR-005/AR-006/AR-008 must preserve causal handoff, source ownership, annotation provenance, commercial separation and reusable-interface boundaries without choosing cross-capability APIs, resources, modules or final Domain ownership.
- **Primary downstream workstreams:** AR-001, AR-002, AR-003, AR-004, AR-005, AR-006, AR-008
- **Blocking classification:** BLOCKING_AUTHORITY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-009 — Research and voting participation identity, uniqueness and linkage promises remain truthful
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Research identity, uniqueness and anonymous-linkage truth` cluster and `Voting participation identity and eligibility` linked theme
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21M.2, 21N.2, 21Q.2, 21Q.5`; `01_DECISIONS_v1.3.0.md DEC-294`, `DEC-295`, `DEC-298`
- **Source classification:** EXPLICIT_PRODUCT_LAW_PRIVACY_AND_AUTHZ_REQUIREMENT
- **Requirement:** Each Research instrument and governed vote declares its participation identity mode, including Account-linked, pseudonymous or anonymous/public modes where appropriate. Identity mode and any uniqueness promise are separate Product claims. A genuinely anonymous participant must not be secretly Account-linked merely to enforce deduplication, and an anonymous/public vote must not be represented as a verified one-human-one-vote result when that assurance is not provided. No Account or Platform Member Reference is required merely for approved anonymous/public participation. Duplicate suppression, rate limiting or other integrity treatment must not be represented as stronger identity assurance than the Product provides; longitudinal linkage is permitted only where the declared identity mode and approved purpose support it.
- **Architectural implication:** AR-002/AR-003/AR-004/AR-007/AR-008/AR-009 must carry declared participation identity, linkage and uniqueness semantics through access, evidence, deletion and derived-read paths without selecting an identifier, fingerprinting method or verification mechanism.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-007, AR-008, AR-009
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-010 — Sensitive Research and interactive-tool data uses purpose-scoped access, targeting and minimisation
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Sensitive Research visibility, targeting and publication` and `Tool health, safety, access and minimisation` linked themes
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21M.6–21M.7, 21O.3–21O.5`; `01_DECISIONS_v1.3.0.md DEC-294`, `DEC-296`
- **Source classification:** EXPLICIT_PRODUCT_LAW_PRIVACY_AND_AUTHZ_REQUIREMENT
- **Requirement:** Sensitive Research questions and health/safety-sensitive tools require an explicitly approved purpose with stronger privacy and safety governance. Account-linked Research responses should normally be visible to the participant where appropriate, subject to approved research, safety, legal and integrity constraints. Cohort targeting and personalised-tool source-data use are purpose-scoped, minimised and do not transfer ownership of the source attribute or record. Longitudinal linkage and publication use only the identity, aggregation and approval basis the purpose permits; publication or attribution to internal, participant or public audiences must use an approved aggregate or otherwise authorised form. Interactive tools may be public, Account-gated or entitlement-gated, but access mode is separate from entitlement authority; public availability must not weaken privacy, safety or minimisation, and the tool does not establish entitlement by being commercially accessible.
- **Architectural implication:** AR-002/AR-003/AR-004/AR-006/AR-007/AR-008/AR-009 must support purpose-, relationship-, sensitivity- and access-scoped reads and derived outputs while leaving clinical/privacy policy, source ownership and exact access mechanisms to their proper authorities.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-006, AR-007, AR-008, AR-009
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-011 — Platform Member Reference is assigned per Account and is non-authoritative across its lifecycle
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Platform Member Reference assignment and identity meaning`, `Platform Member Reference security and non-authority` and `Platform Member Reference security and lifecycle` clusters/themes
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21P.1–21P.2`; `01_DECISIONS_v1.3.0.md DEC-297`
- **Source classification:** EXPLICIT_PRODUCT_LAW_IDENTITY_LIFECYCLE_REQUIREMENT
- **Requirement:** Every successfully created individual Account receives one Platform Member Reference; an anonymous visitor, anonymous voter, anonymous Research respondent, mailing-list contact without an Account or uncreated recipient does not receive one automatically. The reference is a stable human-facing Account identifier, not database identity, authentication, authorisation, identity-verification assurance, paid membership, subscription or entitlement. Possession of it confers no Account rights. It is non-secret but private-by-default, unique and normally immutable for the Account, never reassigned to another Account, and retained when that same Account is legitimately reactivated. If an Account undergoes genuine final deletion and the person later creates a genuinely new Account, that new Account receives a new Platform Member Reference and the old reference remains permanently non-reusable. A governed duplicate-account merge leaves exactly one canonical active Account/reference and retires the other reference permanently. Governed exceptional retirement/replacement is permitted only for security, privacy, integrity, reconciliation or equivalent operational-correctness reasons; routine vanity changes are not a Product requirement. Exact representation is governed separately by `ARQ-IAM-013` and remains implementation-detail work.
- **Architectural implication:** AR-003/AR-004/AR-005/AR-007/AR-008 must preserve assignment, privacy, uniqueness, continuity, merge and deletion semantics without making the reference a credential, commercial authority or premature domain ownership decision.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007, AR-008
- **Blocking classification:** IDENTITY_INTEGRITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-012 — Platform Member Reference lookup and beneficiary association are minimum-disclosure, non-authoritative flows
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Platform Member Reference lookup and beneficiary boundaries` linked theme
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / PRIVACY_CONSTRAINED
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §21P.3, §21Q.6`; `01_DECISIONS_v1.3.0.md DEC-297`, `DEC-298`
- **Source classification:** EXPLICIT_PRODUCT_AUTHORITY_BOUNDARY
- **Requirement:** A Platform Member Reference may support purpose-driven human-facing identification in approved support, communication, event, checkout, gifting and beneficiary workflows. Lookup reveals only the minimum information needed to confirm the intended person and prevent material selection error; it is not authentication, authorisation or permission bypass. A purchaser's use of another person's reference does not prove control, beneficiary consent, subscription state, discount validity or entitlement eligibility. Commerce/Entitlements or the applicable owning capability remains authoritative for benefits, discounts, vouchers and fulfilment; the reference is never a pseudo-coupon, credential or entitlement token. Staff lookup remains subject to the same scoped access and audit rules as other participant information.
- **Architectural implication:** AR-002/AR-003/AR-004/AR-005/AR-008 must provide purpose-scoped, minimum-disclosure lookup and association evidence while keeping consent, payment, benefit and entitlement decisions with their owning authorities.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AUTHZ
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-IAM-013 — Platform Member Reference representation is human-usable without encoding a Product format
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Platform Member Reference human-usable representation` cluster
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / DEFERRED_TO_ARCHITECTURE
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §21P.4`; `01_DECISIONS_v1.3.0.md DEC-297`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** The Platform Member Reference must be human-readable, reasonably short and practical to type, dictate, copy and display; resistant to common transcription mistakes and unambiguous for ordinary human entry; non-semantic; non-secret; not obviously sequential in a way that unnecessarily exposes Account growth or materially simplifies enumeration; compatible with an error-detection/check mechanism; stable across ordinary Account changes; and supported by a realistically adequate namespace. This ARQ does not freeze a prefix, alphabet, payload length, grouping, check algorithm, generation algorithm, collision strategy or database representation; a brand-specific prefix such as `VG` is not Product Law.
- **Architectural implication:** AR-002/AR-003/AR-004/AR-008 must prove the Product-level usability, privacy and collision constraints before selecting an exact representation or generator.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-008
- **Blocking classification:** ARCHITECTURE_PROOF_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-008 — Research instruments and responses preserve versioned meaning through an explicit lifecycle
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Governed research instrument provenance and lifecycle` and `Research response lifecycle, including anonymous withdrawal limits` clusters
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21M.4–21M.5, 21M.8`; `01_DECISIONS_v1.3.0.md DEC-294`
- **Source classification:** EXPLICIT_PRODUCT_LAW_LIFECYCLE_REQUIREMENT
- **Requirement:** Every persisted Research/Feedback response preserves the exact question or instrument version against which it was submitted. Governed campaigns use immutable published versions and explicit publication, correction, withdrawal, retention and closure semantics; a published version must not be edited in place to change the meaning of responses already collected against it. Account-linked or appropriately pseudonymous responses may be corrected, withdrawn or deleted only where purpose, applicable law/policy and retention obligations permit, with history preserved when historical integrity matters. For a genuinely anonymous response, the Product must not promise later individual withdrawal or deletion when it cannot reliably identify the response, and the limitation must be clear before submission where relevant. Participant-submitted truth, staff annotations/classifications and later interpretations remain distinguishable; incentives or downstream actions do not turn an annotation into participant truth.
- **Architectural implication:** AR-002/AR-003/AR-005/AR-006/AR-007/AR-008 must preserve Research instrument/result provenance and category-aware lifecycle transitions while leaving exact retention durations, record ownership and implementation mechanisms downstream.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-006, AR-007, AR-008
- **Blocking classification:** HISTORY_INTEGRITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-009 — Vote rules, accepted evidence and submission states remain durable and distinct
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Vote lifecycle and integrity-evidence states`, `Voting visibility and integrity` and `Voting integrity, status and anti-abuse` clusters/themes
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21N.2–21N.3`; `01_DECISIONS_v1.3.0.md DEC-295`
- **Source classification:** EXPLICIT_PRODUCT_LAW_REQUIREMENT
- **Requirement:** Each governed vote carries durable rules for allowed selections, maximum votes/selections, whether a submitted vote may change, open/close timing and finality. Submission evidence distinguishes submitted, accepted, rejected/invalidated and held/requires-review states where applicable, and material invalidation is explainable and auditable. Configured visibility may expose no live tally, an approximate indicator, exact provisional counts/percentages or final results only, but a provisional view must not be treated as an official result and private voter identity/choice must not be exposed by the presentation path. Integrity controls may suppress duplicates, classify abuse or invalidate evidence without upgrading identity assurance; legitimate campaigning remains a Product-policy permission where approved.
- **Architectural implication:** AR-002/AR-003/AR-004/AR-005/AR-008/AR-009 must preserve the separation between vote rules, evidence state, visibility policy, accepted tally input and identity assurance without choosing anti-abuse thresholds or mechanisms.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-008, AR-009
- **Blocking classification:** BLOCKING_DATA_INTEGRITY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-010 — Voting tally, official result and reward fulfilment remain separate authorities
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Tally, official result and reward boundary` cluster and linked cross-capability authority theme
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §21N.4, §21Q.9`; `01_DECISIONS_v1.3.0.md DEC-295`, `DEC-298`
- **Source classification:** EXPLICIT_PRODUCT_AUTHORITY_BOUNDARY
- **Requirement:** Governed voting distinguishes submitted evidence, integrity/eligibility treatment, accepted tally, governed finalisation, official result or winner, and separately governed prize, reward, discount or entitlement fulfilment. A raw count, cache, analytics projection or provider count does not become the official result merely by being largest or current. A participation or result condition may initiate or request fulfilment, but the owning commercial/entitlement or other applicable capability independently establishes its own authority and records the consequence.
- **Architectural implication:** AR-002/AR-003/AR-005/AR-008/AR-009 must maintain separate result and consequence boundaries with auditable causation, without choosing a result resource, tally mechanism, provider or fulfilment workflow.
- **Primary downstream workstreams:** AR-002, AR-003, AR-005, AR-008, AR-009
- **Blocking classification:** BLOCKING_AUTHORITY_INVARIANT
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-011 — Voting finalisation governs exceptions, adjudication, privacy and safety
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Voting finalisation and exception outcomes` and `Voting visibility, adjudication and safety` clusters/themes
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / EVIDENCE_GATED
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21N.5–21N.6`; `01_DECISIONS_v1.3.0.md DEC-295`
- **Source classification:** EXPLICIT_PRODUCT_LAW_INTEGRITY_GATES_HARDENED_BY_GRILL
- **Requirement:** Every governed competition or material ballot has an approved finalisation policy covering ties, contestant/option disqualification, material integrity failure, outage or disruption, cancellation, re-run or extension and adjudication. Rules must not be invented after the outcome to favour a preferred result. Authorised operators may perform only governed adjudication actions and may not arbitrarily alter counts or choose a preferred winner. Individual voter identity and ballot choice are private by default; aggregate indicators or leaderboards must not expose them through drill-down or enumeration. Voting mechanics do not supersede or weaken existing wellness and competition safety restrictions.
- **Architectural implication:** AR-002/AR-003/AR-004/AR-006/AR-008/AR-009 must support evidence-bearing finalisation, scoped adjudication and privacy/safety-preserving exception paths while leaving competition policy, clinical review and exact state transitions downstream.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-006, AR-008, AR-009
- **Blocking classification:** DECISION_EVIDENCE_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-012 — Account deletion does not rewrite legitimate historical Research or Voting truth
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Historical Research and Voting truth after Account deletion` cluster
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / MANDATORY_REQUIREMENT
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §21Q.7`; `01_DECISIONS_v1.3.0.md DEC-298`
- **Source classification:** EXPLICIT_PRODUCT_LAW_DELETION_REQUIREMENT
- **Requirement:** Account closure or deletion must not automatically invalidate a historically legitimate Research/Feedback response, vote, accepted tally, adjudicated outcome or official competition result. The eligible identity and personal data lifecycle still follows the applicable deletion, anonymisation, retention and legal-hold rules, but deleting an Account relationship must not silently recalculate or falsify an established Research or Voting fact. Historical evidence that lawfully remains must preserve its legitimate meaning without reconstructing the deleted identity beyond the approved basis.
- **Architectural implication:** AR-003/AR-004/AR-005/AR-007/AR-008 must separate identity deletion from historical Research/Voting truth and prove category-aware de-identification or retention without selecting retention duration, schema or deletion orchestration.
- **Primary downstream workstreams:** AR-003, AR-004, AR-005, AR-007, AR-008
- **Blocking classification:** BLOCKING_PRIVACY_AND_HISTORY_INTEGRITY
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-STATE-013 — Interactive results preserve purpose, version provenance and historical interpretation
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Non-authoritative tool result and downstream handoff`, `Tool persistence, version and history` and `Tool explainability, configuration and correction` themes
- **Status:** ACCEPTED
- **Strength:** MANDATORY_INVARIANT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §§21O.2–21O.5`; `01_DECISIONS_v1.3.0.md DEC-296`
- **Source classification:** EXPLICIT_CROSS_PRODUCT_VERSIONING_REQUIREMENT
- **Requirement:** Interactive-tool output is educational or advisory by default; calculation is not authority for Health Records, Safety & Eligibility, Plans, Temperament, Commerce or Entitlements. Public or anonymous inputs/results are non-persistent by default, while Account-linked persistence requires clear Product value, participant expectation and purpose. Every persisted or materially consequential result remains associated with the approved tool/calculation version that produced it; a material change in calculation meaning creates a new governed version rather than silently changing historical interpretation. Correction and recalculation may produce a new interpretation or result without falsifying historical meaning, and explanation is proportional to consequence. A result may initiate, offer or request an owner-mediated action but cannot itself perform the authoritative transition.
- **Architectural implication:** AR-002/AR-003/AR-004/AR-005/AR-006/AR-007/AR-008 must preserve tool-result purpose, persistence, version, explanation and correction boundaries while leaving exact version records, storage, recalculation workflow and downstream owner unresolved for Architecture/Domain work.
- **Primary downstream workstreams:** AR-002, AR-003, AR-004, AR-005, AR-006, AR-007, AR-008
- **Blocking classification:** HISTORY_INTEGRITY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

### ARQ-ASYNC-004 — Research follow-up and escalation do not create a universal monitoring promise
- **Extraction source:** Stage 3A.2 governed amendment from the Stage 3A.1 `Research follow-up and monitoring-promise boundary` cluster
- **Status:** ACCEPTED
- **Strength:** MANDATORY_REQUIREMENT / ARCHITECTURAL_PRINCIPLE
- **Exact Product Law source:** `00_PLATFORM_v1.3.0.md §21M.7`; `01_DECISIONS_v1.3.0.md DEC-294`
- **Source classification:** EXPLICIT_PRODUCT_AUTHORITY_BOUNDARY
- **Requirement:** A Research/Feedback instrument may explicitly support participant-requested follow-up, a defined escalation path or another approved downstream action. The response remains Research/Feedback evidence until the owning capability independently establishes its own authority. Free text or a research submission must not imply a universal promise that every response is continuously monitored for safety, intervention or clinical follow-up. Follow-up intent, routing and outcome remain distinguishable from the participant response.
- **Architectural implication:** AR-002/AR-004/AR-005/AR-006/AR-008 must preserve an explicit, separately governed follow-up/consequence boundary without selecting a notification mechanism, monitoring service or domain owner.
- **Primary downstream workstreams:** AR-002, AR-004, AR-005, AR-006, AR-008
- **Blocking classification:** ARCHITECTURE_BOUNDARY_GATE
- **Architecture status:** ARQ_LOCKED / ARC_PENDING

## 10.5 Identifier allocation proof

No new ARQ family was required. The selected existing families already represent the invariants without implying Research, Voting, Tool, Engagement or Member Reference Domain ownership:

- `SYS` owns platform-space, capability-boundary and shared-interaction constraints.
- `IAM` owns participation identity, privacy/access, Account-reference meaning and lookup boundaries.
- `STATE` owns versioned meaning, submission/result state and deletion/history invariants.
- `ASYNC` owns explicit follow-up/escalation consequence boundaries.

All existing family ranges were mechanically enumerated before allocation. They were complete and collision-free at v1.0.0. New identifiers begin at the prior family maximum plus one; no historical identifier was renumbered.

| Existing family | v1.0.0 count | v1.0.0 range / maximum | New allocation | New family maximum | Allocation rationale |
|---|---:|---|---|---:|---|
| `ARQ-PERF` | 166 | `ARQ-PERF-001`–`ARQ-PERF-166` / 166 | none | 166 | Closed Performance family; no new Product obligation is genuinely a Performance requirement. |
| `ARQ-AN` | 216 | `ARQ-AN-001`–`ARQ-AN-216` / 216 | none | 216 | Closed Analytics family; derived-presentation obligations use exact source propagation only. |
| `ARQ-PAY` | 1 | `ARQ-PAY-001` / 001 | none | 1 | Commercial ownership remains an existing authority boundary. |
| `ARQ-SYS` | 6 | `ARQ-SYS-001`–`ARQ-SYS-006` / 006 | `ARQ-SYS-007`–`ARQ-SYS-010` (4) | 10 | Capability/platform-space and shared-primitive boundaries. |
| `ARQ-IAM` | 8 | `ARQ-IAM-001`–`ARQ-IAM-008` / 008 | `ARQ-IAM-009`–`ARQ-IAM-013` (5) | 13 | Participation identity, privacy/access and Member Reference semantics. |
| `ARQ-STATE` | 7 | `ARQ-STATE-001`–`ARQ-STATE-007` / 007 | `ARQ-STATE-008`–`ARQ-STATE-013` (6) | 13 | Research, voting, tool and deletion/history lifecycle invariants. |
| `ARQ-ASYNC` | 3 | `ARQ-ASYNC-001`–`ARQ-ASYNC-003` / 003 | `ARQ-ASYNC-004` (1) | 4 | Explicit Research follow-up and escalation consequence boundary. |
| `ARQ-CONTENT` | 6 | `ARQ-CONTENT-001`–`ARQ-CONTENT-006` / 006 | none | 6 | Research/tool source does not establish Content risk-class or publication authority. |
| `ARQ-SEC` | 2 | `ARQ-SEC-001`–`ARQ-SEC-002` / 002 | none | 2 | Voting anti-abuse source directly propagates to existing `ARQ-SEC-001`. |
| `ARQ-OPS` | 2 | `ARQ-OPS-001`–`ARQ-OPS-002` / 002 | none | 2 | No new Product obligation changes Operations-family semantics. |
| **Total** | **417** |  | **16 new ARQs** | **433** | `417 + 16 = 433`; Performance and Analytics remain closed. |

The proposed new family sets are contiguous by construction: `SYS 007–010`, `IAM 009–013`, `STATE 008–013` and `ASYNC 004`. The v1.0.0 sets are also contiguous; therefore the cumulative identifier set has no gaps, duplicates or collisions introduced by this amendment.

## 10.6 Two NO_ARQ_REQUIRED rules deliberately retained outside AR-000

The two Product rules classified `NO_ARQ_REQUIRED` in Stage 3A.1 are explicitly accounted for and do not receive new ARQ identifiers:

1. **Ordinary campaigning and legitimate supporter invitations remain permitted where competition rules allow** (`§§21N.1–21N.6`; `DEC-295`). The permission is competition/Product policy, not an independent durable architecture invariant at this stage. The new `ARQ-STATE-009` preserves the separate prohibition on deliberate manipulation and the integrity-state boundary, but no ARQ is created merely to encode permission to campaign.
2. **The exact Platform Member Reference representation remains an implementation decision** (`§21P.4`; `DEC-297`). Prefix, alphabet, payload length, grouping, check algorithm, generation, collision strategy and database representation are deliberately deferred; `ARQ-IAM-013` governs the Product-level usability/privacy/error-detection constraints without freezing the format, and no `VG` identifier is frozen. No separate ARQ is created for those implementation details.

These rules count as deliberately covered Product Law, not as omissions. The closure arithmetic records exactly two `NO_ARQ_REQUIRED` rows.

## 10.7 Stage 3B exclusion and downstream decision boundary

No new Product-derived ARQ imports the independent Stage 3B inputs: Errors & Diagnostics, Observability refinement, Native Compute / Rustler or Engineering Quality. Where a Product requirement has an ordinary implication for audit, logging, performance, failure handling or reliability, this amendment records only the Product-derived invariant and leaves the mechanism downstream.

This amendment does not decide exact Ash Resources, schemas/tables/columns, packages, queue/worker topology, Redis, ETS/Cachex, GenServers, exact PubSub, API shapes, anti-abuse mechanisms, CAPTCHA/device/IP strategy, identifier format/check algorithm, Research/Voting/Tool Domain ownership, provider selection, retention duration or Roadmap Feature Pack placement. Those remain Architecture Law, Domain, expert/vendor, Roadmap or later programme work.

Architecture Law, `03_ARCHITECTURE_v1.0.0.md`, Domain Map, Roadmap, Delivery Atlas, HARDEN-02, FP-001 artifacts and application implementation are not amended by this document.

## 10.8 Stage 3A.2 closure audit

### Stage 3A.1 shorthand normalization note

The archived Stage 3A.1 analysis uses the shorthand **“error-detectable”** when describing the §21P.4 representation constraint. The governed `ARQ-IAM-013` uses the exact current Product Law meaning: **“compatible with an error-detection/check mechanism.”** This normalises non-authoritative Stage 3A.1 shorthand without changing Product Law or historical evidence; it is not an upstream Product contradiction, and it does not require a check digit, checksum or particular algorithm in AR-000.

| Closure item | Result |
|---|---|
| Previous accepted ARQ total | 417 |
| New ARQs added | 16 |
| New cumulative accepted ARQ total | 433 (`417 + 16`) |
| Existing ARQs receiving post-freeze source propagation | 10 distinct ARQs across 17 source-to-ARQ records |
| Complete source-refresh rows | 5 |
| Reclassified source-refresh-plus-additive rows | 3, each retaining only valid `ARQ-STATE-002` provenance |
| Historical ARQ deletions | 0 |
| Historical ARQ renumberings | 0 |
| Historical ARQ semantic rewrites | 0 |
| Stage 3A.1 `EXISTING_ARQ_SUFFICIENT` rows | 0 |
| Stage 3A.1 `EXISTING_ARQ_SOURCE_REFRESH_REQUIRED` rows | 5 |
| Stage 3A.1 `EXISTING_ARQ_AMENDMENT_REQUIRED` rows | 44 (`41` preserve-plus-additive and `3` source-refresh-plus-additive) |
| Stage 3A.1 `NEW_ARQ_REQUIRED` rows | 15 consolidated into 12 new descriptive clusters and 16 governed ARQs |
| Stage 3A.1 `NO_ARQ_REQUIRED` rows | 2, explicitly listed in §10.6 |
| Stage 3A.1 `UPSTREAM_PRODUCT_CONTRADICTION` rows | 0 |
| Stage 3A.1 descriptive themes mapped | 30 (`12` clusters + `18` linked themes), all mapped in §10.3 |
| Product Law source coverage | §§21M–21Q and `DEC-294`–`DEC-298` covered in §10.3 |
| Stage 3B inputs | Excluded |
| Architecture Law amendment | 0; still not amended by Stage 3A.2 |
| Downstream Architecture/Domain/Roadmap/FP-001/implementation changes | 0 |

The complete Product-obligation arithmetic is `5 + 44 + 15 + 2 + 0 = 66`; the ARQ arithmetic is `417 + 16 = 433`. All 30 descriptive themes have governed destinations, every new ARQ has an exact Product Law source, and no contradiction or historical mutation was discovered.

## 10.9 v1.1.0 amendment record

- SemVer transition: `v1.0.0 → v1.1.0`.
- Preserved the complete v1.0.0 AR-000 register and freeze/closure history; the exact v1.0.0 artifact is archived as historical evidence.
- Added the five complete post-freeze source-refresh rows and the three valid partial `ARQ-STATE-002` provenance components without changing historical ARQ wording or status.
- Added 16 accepted Product-Law ARQs in existing `SYS`, `IAM`, `STATE` and `ASYNC` families; no `PERF` or `AN` ARQs were added.
- Mapped all 12 new descriptive clusters and 18 linked additive themes, explicitly accounted for both `NO_ARQ_REQUIRED` rules and excluded Stage 3B.
- Advanced the planning tracker to `02_OPEN_WORK_v1.2.32.md`; Stage 3B is next and executable development remains blocked.
- **Next:** independent Stage 3B Architecture/Engineering classification, followed by separately authorised downstream Architecture/Domain/Roadmap/FP-001 reconciliation. No implementation is authorised by this amendment.
