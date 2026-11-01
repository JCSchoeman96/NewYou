# 02_OPEN_WORK_v1.2.25.md

- **Document status:** POST-GRILL OPEN-WORK BASELINE v1.2.25
- **Authoritative for:** Remaining unresolved planning questions, expert/vendor/architecture/operations gates, post-grilling deliverables, planning and delivery sequencing, and planning/development stop conditions
- **Not authoritative for:** Locked product decisions, platform truth, implementation details, Ash Resources, schemas, or legal and clinical conclusions
- **Related documents:**
  - `00_PLATFORM_v1.2.1.md`
  - `01_DECISIONS_v1.2.1.md`
  - `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
  - `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`
  - `ARCHITECTURE_LAW_WORKING_v0.35.0.md`
  - `REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`
  - `03_ARCHITECTURE_v1.0.0.md`
  - `04_DOMAIN_MAP_v1.0.0.md`
- **Last updated:** 2026-08-17
- **Current planning position:** PRODUCT GRILL COMPLETE; Product Law remains at v1.2.1; `AR-000` is COMPLETE/FROZEN at `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`; **Phase 2 Architecture Decision Workstreams are COMPLETE** through AR-009 closure at `ARC-326`, with post-closure `ARC-327` preserving staged proof timing; **Phase 3 Reference Flow Pressure Tests are COMPLETE** in `REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`; **Phase 4 Architecture is FROZEN** at `03_ARCHITECTURE_v1.0.0.md`; **Phase 5 Domain Map + lightweight Domain Architecture Profile baseline is COMPLETE/FROZEN** at `04_DOMAIN_MAP_v1.0.0.md` with 18 approved ownership domains, 48 major durable-truth ownership rows, 18/18 profiles, zero shared-write ambiguities and zero circular authoritative control dependencies. **Immediate next action: Phase 6 — create `05_ROADMAP.md` using the frozen Architecture and Domain Law.** Implementation remains stopped pending Roadmap/Feature Pack and JIT dossier/gate requirements.

---



## v1.2.25 — 2026-08-17 — Domain Map/Profile freeze / Phase 6 advancement

- Planning-state SemVer transition: `v1.2.24 → v1.2.25`.
- Completed Phase 5 and froze `04_DOMAIN_MAP_v1.0.0.md` as the authoritative Domain Map + lightweight Domain Architecture Profile baseline.
- Approved **18** coherent platform ownership domains after challenging the 22-name hypothesis; no standalone Memberships, Recommendations, Administration, Nuwe Jy or Challenges domain was created.
- Platform-wide ownership matrix records **48 major durable business truths**, each with exactly one authoritative platform domain.
- Completed **18/18** lightweight Domain Architecture Profiles required by OQ-039; exact indexes, Redis keys/structures, TTLs, queues, topics, schemas and source code remain downstream JIT/Feature Pack work.
- Consolidated Phase 5 review PASSED ownership completeness, boundary coherence, shared-write/circular-control safety, Product Law coverage, Architecture compliance, privacy/security, performance/scaling proportionality and anti-fragmentation.
- Closure audit: **0 shared-write ambiguities; 0 circular authoritative control dependencies; 0 new platform mechanisms; 0 owner questions requiring Grill-Me; 0 Product Law/Architecture amendments.**
- OQ-033 remains the legal/professional record-authority gate; Domain Law assigns Professional Care the platform care-case/workflow boundary without pretending the platform is automatically the ultimate professional recordkeeper.
- Advanced immediate planning work to **Phase 6 — `05_ROADMAP.md`**.
- Executable development remains stopped under the Development Entry Hard Stop.

## v1.2.24 — 2026-08-17 — Architecture freeze / Phase 5 advancement

- Planning-state SemVer transition: `v1.2.23 → v1.2.24`.
- Completed Phase 4 synthesis/review/freeze and created `03_ARCHITECTURE_v1.0.0.md`.
- Consolidated Phase 4 review PASSED across architecture consistency, security/privacy, failure/recovery, performance/scaling and anti-overengineering/development-friction lenses.
- Mechanical closure: 327/327 active ARCs represented with no gaps/duplicates; all 417 frozen ARQs remain preserved through the accepted Architecture Law and all 10 ARQ families are represented in the synthesis.
- Lightweight FLOW-01...FLOW-12 traceability PASSED 12/12; no flow was materially changed by synthesis and therefore no full flow rerun was required.
- Domain Map readiness PASSED: concrete business ownership can now be assigned without inventing a new platform transaction, persistence, async, realtime, provider, privacy, security or scaling mechanism.
- No Product Law, DEC, OQ, ARQ, ARC or Reference Flow finding changed during Phase 4.
- Advanced immediate work to Phase 5 — `04_DOMAIN_MAP.md` plus the required lightweight Domain Architecture Profiles.
- Implementation remains stopped under the Development Entry Hard Stop.

## v1.2.23 — 2026-08-17 — Phase 4 immediate-next-action hygiene correction

- Planning-state-only SemVer transition: `v1.2.22 → v1.2.23`.
- Corrected only the active Section 9 `Immediate Next Action`, which still carried stale AR-009 V3 / FLOW-01...FLOW-12 sequencing despite the current-state header already recording Phase 3 COMPLETE.
- Phase 2 remains COMPLETE; Phase 3 remains COMPLETE; immediate substantive work is Phase 4 `03_ARCHITECTURE.md` synthesis/review/freeze, followed by `04_DOMAIN_MAP.md` only after Architecture freeze.
- No Product Law, DEC, OQ, ARQ, ARC or Reference Flow finding changed.

## v1.2.22 — 2026-08-17 — Phase 3 efficiency correction + Reference Flow closure

- Planning-state SemVer transition: `v1.2.21 → v1.2.22`.
- Accepted the Phase 3 efficiency correction: Reference Flow Pressure Tests remain required, but are lean architecture-coherence proofs rather than pre-implementation benchmark/specification packs.
- Added post-closure Architecture Law `ARC-327` in `ARCHITECTURE_LAW_WORKING_v0.35.0.md` as a narrow timing/depth amendment to `ARC-326`.
- `ARC-327` preserves the full Performance & Capacity Proof Matrix for executable evidence while allowing Phase 3 to record only performance sensitivity, material scale concern, hard invariant, later executable proof requirement and applicable future proof stage.
- AR-009 remains COMPLETE through `ARC-326`; no V4/general AR-009 reopening occurred.
- Compacted FLOW-01 without changing its `PASS_WITH_DOWNSTREAM_GATES` verdict.
- Completed FLOW-02 through FLOW-12 in `REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`.
- Phase 3 closure audit: **12/12 flows complete; 1 PASS; 11 PASS_WITH_DOWNSTREAM_GATES; 0 FAIL_ARCHITECTURE_GAP; 0 BLOCKED_CONTRADICTION; 0 Product Law amendments; 0 ARQ amendments; 0 flow-mechanism ARCs required.**
- Replaced the Phase 4 instruction to formally rerun all twelve flows with a lightweight synthesis traceability check. Only materially affected flows are rerun after a synthesis correction or later Architecture amendment.
- Advanced immediate work to `03_ARCHITECTURE.md` synthesis/review/freeze.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.21 — 2026-08-17 — Hammer candidate acceptance + Reference Flow Pressure Tests start

- Planning-state-only SemVer transition: `v1.2.20 → v1.2.21`.
- Recorded the accepted conclusion for the unresolved rate-limiting package question: **Hammer is the preferred application-layer proof/JIT candidate, while the Architecture boundary remains package-replaceable**.
- This acceptance **does not create ARC-327**, does not change `ARCHITECTURE_LAW_WORKING_v0.34.0.md`, and does not weaken `ARC-144`, `ARC-145`, `ARC-322` or `ARC-326`. Concrete Hammer version/backend/algorithm selection remains proof/JIT work.
- Preserved `OQ-035` as the owner of exact Cloudflare/application/distributed-rate thresholds, escalation rules and false-positive recovery. Hammer does not resolve those thresholds.
- Preferred proof direction: platform-owned rate/abuse boundary; Hammer behind that boundary; Redis-backed distributed semantics where the affected control requires a shared multi-node view; node-local counters only where locality is explicitly acceptable; risk-class-specific fail-open/fail-closed behaviour; platform telemetry around allow/deny/backend-error/degraded outcomes.
- Opened `REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.1.0.md` and completed `FLOW-01 Registration → verification → login` with verdict **PASS_WITH_DOWNSTREAM_GATES**. No undocumented architecture mechanism or contradiction was found.
- `FLOW-01` preserves `OQ-034` authentication implementation proof and `OQ-035` exact abuse-control thresholds as downstream gates; it does not treat unresolved package/threshold detail as an Architecture-law gap.
- Corrected the active Phase 2 current-state line below to show `AR-009` COMPLETE through `ARC-326`; historical version entries remain unchanged.
- Immediate next action: `FLOW-02 Checkout → provider verification → payment → entitlement`.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ, ARQ or ARC changed.

## v1.2.20 — 2026-08-17 — AR-009 V3 + final closure / Reference Flow Pressure Tests advancement

- Planning-state-only SemVer transition: `v1.2.19 → v1.2.20`.
- Recorded accepted AR-009 V3 Architecture Law `ARC-315...ARC-326` in `ARCHITECTURE_LAW_WORKING_v0.34.0.md`.
- Locked adversarial contention/race proof, zero-oversell flash-sale verification, duplicate/retry storm testing, database contention evidence, anti-stampede cold/recovery proof, controlled backlog catch-up, realtime storm/node-loss proof, distributed abuse-control pressure, migration/maintenance pressure testing, representative synthetic scale data, analytics/experiment composite pressure and the canonical Performance & Capacity Proof Matrix contract.
- Re-ran the complete AR-009 closure audit across **155 frozen ARQs routed through AR-009**: Performance 105; Analytics 47; Payments 1; Security 1; Operations 1. Result: **PASS**.
- Confirmed no V4 is required; remaining routed realtime, dashboard/alert, analytics/warehouse/CDC and experiment-governance requirements are already semantically closed by prior Architecture Law plus V1–V3.
- Marked `AR-009 — Performance, Scaling & Multi-Node Behaviour` COMPLETE through `ARC-326`; **AR-001...AR-009 Architecture Decision workstreams are now COMPLETE**.
- Advanced immediate planning work to **Reference Flow Pressure Tests**, followed by `03_ARCHITECTURE.md` freeze if no genuine contradiction/gap is exposed.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.19 — 2026-08-17 — AR-009 V2 capacity/multi-node scaling progress

- Planning-state-only SemVer transition: `v1.2.18 → v1.2.19`.
- Recorded accepted AR-009 V2 Architecture Law `ARC-303...ARC-314` in `ARCHITECTURE_LAW_WORKING_v0.33.0.md`.
- Locked system-wide PostgreSQL connection budgets/reserve, evidence-gated transaction pooling, query/index/plan budgets, evidence-driven read scaling, bounded LiveView connection envelopes, realtime amplification proof, shared worker/resource budgets, node-count multipliers, evidence-based headroom, bottleneck-driven scaling triggers and composite topology pressure proof.
- AR-009 remains IN PROGRESS; immediate next action is `AR-009 V3 — contention/race proofs, flash-sale zero-oversell, backlog recovery, abuse pressure, migration/maintenance pressure, realistic test data and final proof matrix`.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.18 — 2026-08-17 — AR-009 V1 workload/performance verification progress

- Planning-state-only SemVer transition: `v1.2.17 → v1.2.18`.
- Recorded accepted AR-009 V1 Architecture Law `ARC-291...ARC-302` in `ARCHITECTURE_LAW_WORKING_v0.32.0.md`.
- Locked workload-specific scale interpretation, distinct load profiles, percentile-based budgets, initial semantic latency classes, current-official Core Web Vitals floor, internal/provider latency decomposition, regression-blocking performance budgets, progressive test classes/cadence, cold/recovery-state proof, versioned pass/fail thresholds and load-generator validity.
- AR-009 remains IN PROGRESS; immediate next action is `AR-009 V3 — contention/race proofs, flash-sale zero-oversell, backlog recovery, abuse pressure, migration/maintenance pressure, realistic test data and final proof matrix`.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.17 — 2026-08-17 — AR-008 O3 + final closure / AR-009 advancement

- Planning-state-only SemVer transition: `v1.2.16 → v1.2.17`.
- Recorded accepted AR-008 O3 Architecture Law `ARC-279...ARC-290` in `ARCHITECTURE_LAW_WORKING_v0.31.0.md`.
- Locked impact/risk-based incident severity; named incident command; safe containment; owned/versioned/exercised runbooks; post-incident amendment/re-proof; cross-functional release no-go gates; failure-injection maturity; full-service recovery exercises; validated runtime configuration; secret handling; governed material configuration releases; and telemetry retention/access governance.
- Re-ran the complete AR-008 closure audit across **321 frozen ARQs routed through AR-008**: Performance 115; Analytics 184; Payments 1; IAM 5; State 6; Async 3; Content 3; Security 2; Operations 2. Result: **PASS**.
- Confirmed no O4 is required; abuse/upload-security operational residuals are already semantically covered by prior AR-003/004/006 Architecture Law plus AR-008 operational controls, with exact thresholds/products remaining AR-009/JIT evidence decisions.
- Marked `AR-008 — Reliability, Deployment, Operations & Observability` COMPLETE through `ARC-290`.
- Advanced immediate Architecture Decision work to `AR-009 — Performance, Scaling & Multi-Node Behaviour`.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.16 — 2026-08-17 — AR-008 O2 observability/telemetry progress

- Planning-state-only SemVer transition: `v1.2.15 → v1.2.16`.
- Recorded accepted AR-008 O2 Architecture Law `ARC-267...ARC-278` in `ARCHITECTURE_LAW_WORKING_v0.30.0.md`.
- AR-008 remains IN PROGRESS; accepted AR-008 law is now `ARC-255...ARC-278`.
- Advanced immediate next action to `AR-008 O3 — Incident severity/command, runbooks, cross-functional release gates, recovery/failure exercises, secrets/config operations and observability retention/access`.
- No Product Law, DEC, OQ or ARQ changed.


## v1.2.15 — 2026-08-17 — AR-008 O1 runtime failure/health/deployment progress

- Planning-state-only SemVer transition: `v1.2.14 → v1.2.15`.
- Recorded accepted AR-008 O1 Architecture Law `ARC-255...ARC-266` in `ARCHITECTURE_LAW_WORKING_v0.29.0.md`.
- Locked capability-specific availability classes; separate startup/liveness/readiness/degraded semantics; dependency-aware health; bounded supervision/crash-loop escalation; overload backpressure/shedding; explicit dependency deadlines/retry budgets/bulkheads; fenced PostgreSQL failover authority; mixed-version-safe rolling deployment; drain-before-terminate; rollback/forward-recovery; risk-proportional canaries; and auditable emergency controls.
- Marked AR-008 IN PROGRESS and advanced immediate next action to `AR-008 O2 — Observability, SLO/error-budget evidence, logs/metrics/traces, incident correlation, alert ownership and telemetry privacy`.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.

## v1.2.14 — 2026-08-17 — AR-007 P2 + final closure / AR-008 advancement

- Planning-state SemVer transition: `v1.2.13 → v1.2.14`.
- Recorded accepted AR-007 P2 Architecture Law `ARC-243...ARC-254` in `ARCHITECTURE_LAW_WORKING_v0.28.0.md`.
- Locked complete recovery-authority scope, HA-versus-backup separation, encrypted-backup ageing with deletion-safe restore, independently recoverable deletion/withdrawal suppression, recovery-gated service promotion, semantic restore verification, deletion-safe derived-model rebuild, class-specific RPO/RTO, governed participant export composition/reauthorisation, temporary protected export artifacts and sensitive-export assurance/audit/output safety.
- Re-ran the complete AR-007 closure audit against **51 frozen ARQs routed through AR-007**: Performance 12; Analytics 28; System 1; IAM 2; State 6; Content 1; Operations 1. Result: **PASS**.
- Marked `AR-007 — Privacy, Deletion, Backup & Restore` COMPLETE through `ARC-254`.
- Advanced immediate Architecture Decision work to `AR-008 — Reliability, Deployment, Operations & Observability`.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.

## v1.2.13 — 2026-08-17 — AR-007 P1 privacy lifecycle/retention/deletion progress

- Planning-state-only SemVer transition: `v1.2.12 → v1.2.13`.
- Recorded accepted AR-007 P1 Architecture Law `ARC-233...ARC-242` in `ARCHITECTURE_LAW_WORKING_v0.28.0.md`.
- Locked separate business/data lifecycle semantics; category/purpose-specific retention with expert-owned durations; durable idempotent deletion orchestration; representation-complete deletion verification; strict anonymisation rules; isolated retained-by-obligation evidence; scoped legal holds; capability-owned deletion contracts; minimal suppression evidence; and separation of closure, consent withdrawal and full deletion.
- Marked AR-007 IN PROGRESS and advanced immediate next action to `AR-007 P2 — Backup/Restore Deletion Replay, Recovery Suppression, Export Lifecycle & Deletion-Safe Restore Testing`, followed by the AR-007 closure audit.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.12 — 2026-08-17 — AR-006 C4 closure / AR-007 advancement

- Planning-state SemVer transition: `v1.2.11 → v1.2.12`.
- Recorded accepted AR-006 C4 Architecture Law `ARC-223...ARC-232` in `ARCHITECTURE_LAW_WORKING_v0.26.0.md`.
- Re-ran the full AR-006 closure audit across **66 routed frozen ARQs**: Performance 16; Analytics 33; Payments 1; System 5; State 1; Async 3; Content 6; Security 1. Result: **PASS**.
- Marked `AR-006 — Content, Translation, Media & External Integrations` COMPLETE through `ARC-232`.
- Advanced immediate Architecture Decision work to `AR-007 — Privacy, Deletion, Backup & Restore`.
- Implementation remains stopped under the Development Entry Hard Stop.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.11 — 2026-08-17 — AR-006 C1–C3 progress / preliminary closure audit

- Planning-state SemVer transition: `v1.2.10 → v1.2.11`.
- Recorded accepted AR-006 C1–C3 Architecture Law through `ARC-222` in `ARCHITECTURE_LAW_WORKING_v0.25.0.md`.
- Mechanically audited all **66 frozen ARQs routed through AR-006**: Performance 16; Analytics 33; Payments 1; System 5; State 1; Async 3; Content 6; Security 1.
- Preliminary audit result: **AR-006 is not yet complete**. C1–C3 close content/translation/publication, search/personalisation/SEO/experiment-safe public delivery, and media/live/replay/provider boundaries, but one surgical residual cluster remains for governed notification/message-template delivery, email/message A/B/n treatment semantics, sensitive scheduled/alert delivery, acquisition/marketing measurement boundaries and outbound vendor-integration privacy/deduplication/reconciliation.
- Immediate next action is `AR-006 C4 — Messaging, Measurement & External Integration Boundary`, followed by the final AR-006 closure audit.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.10 — 2026-08-17 — AR-005 TC4 closure / AR-006 advancement

- Planning-state SemVer transition: `v1.2.9 → v1.2.10`.
- Recorded accepted AR-005 TC4 Architecture Law `ARC-179...ARC-188` in `ARCHITECTURE_LAW_WORKING_v0.22.0.md`.
- Re-ran the full AR-005 closure audit across **234** routed frozen ARQs (Performance 106; Analytics 118; Payments 1; IAM 2; State 3; Async 3; Content 1). Result: **PASS**.
- Marked `AR-005 — Transactions, Consistency, Async & Realtime` COMPLETE through `ARC-188`.
- Advanced immediate Architecture Decision work to `AR-006 — Content, Translation, Media & External Integrations`, beginning with content authority/versioning/translation/publication boundaries.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.9 — 2026-08-17 — AR-005 TC1–TC3 progress / preliminary closure audit

- Updated planning state to reflect accepted AR-005 TC1–TC3 Architecture Law through `ARC-178` in `ARCHITECTURE_LAW_WORKING_v0.21.0.md`.
- Recorded the preliminary AR-005 closure audit over **234** routed frozen ARQs.
- Audit result: AR-005 is **not yet complete**; one surgical TC4 is required for `Analytics Commit/Replay & Experiment Assignment/Exposure Consistency`.
- Preserved all Product Law and ARQ authority unchanged; no contradiction or upstream amendment was identified.
- Immediate next action is AR-005 TC4, followed by the final AR-005 closure audit.

## v1.2.8 — 2026-08-17 — AR-004 closure / AR-005 advancement

- Planning-state-only SemVer transition: `v1.2.7 → v1.2.8`.
- Marked `AR-004 — Identity, Authentication, Authorisation & Field Privacy` COMPLETE after Architecture Law `ARC-110...ARC-145` and the 119-ARQ closure audit PASS.
- Advanced the immediate next Architecture workstream to `AR-005 — Transactions, Consistency, Async & Realtime`.
- Updated the current Architecture Law pointer to `ARCHITECTURE_LAW_WORKING_v0.18.0.md` through `ARC-145`.
- No Product Law, DEC, OQ or ARQ changed.

## v1.2.7 Patch Scope

This is a **planning-state-only tracker patch**. It does not change Product Law, any DEC, OQ, ARQ, ARC meaning, delivery methodology, MVP scope, or implementation rule.

It only records that:

- `AR-003 — State Authority, Persistence, Caching & Storage` is COMPLETE after accepted `ARC-059...ARC-109` and the AR-003 closure audit;
- the AR-003 closure audit covered all **240 frozen ARQs** routed through AR-003 and PASSED without Product Law/ARQ amendment or an S6 round;
- `ARCHITECTURE_LAW_WORKING_v0.14.0.md` is the current cumulative Architecture Law register;
- the immediate next workstream is `AR-005 — Transactions, Consistency, Async & Realtime`;
- Phase 2 Architecture Decision Workstreams remain IN PROGRESS;
- implementation remains stopped under the existing Development Entry Hard Stop.

The Product Law source documents remain v1.2.1 because no Product Law meaning changed.

---

## v1.2.6 Patch Scope

This is a **planning-state-only filename/current-state hygiene patch**. It does not change Product Law, any DEC, OQ, ARQ, ARC meaning, delivery methodology, MVP scope, or implementation rule.

It only records that:

- cumulative architecture/planning artifacts now carry their SemVer in the filename as well as document metadata;
- the frozen AR-000 handoff is referenced as `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`;
- the current Architecture Law register is `ARCHITECTURE_LAW_WORKING_v0.13.0.md`;
- AR-003 is IN PROGRESS through `ARC-099`;
- historical patch-scope text is preserved as history even where it quoted the earlier unversioned working filename;
- implementation remains stopped under the existing Development Entry Hard Stop.

The Product Law source documents remain v1.2.1 because no Product Law meaning changed.

---


## v1.2.5 Patch Scope

This is a **planning-state-only tracker patch**. It does not change Product Law, any DEC, OQ, ARQ, delivery methodology, architecture requirement, MVP scope, or implementation rule.

It only records that:

- `AR-002 — Phoenix / LiveView / Ash / Code Boundaries` is COMPLETE after accepted `ARC-027...ARC-058` and the AR-002 closure audit;
- `ARCHITECTURE_LAW_WORKING.md v0.8.0` is the current cumulative Architecture Law register;
- the immediate next workstream is `AR-003 — State Authority, Persistence, Caching & Storage`;
- Phase 2 Architecture Decision Workstreams remain IN PROGRESS;
- implementation remains stopped under the existing Development Entry Hard Stop.

The Product Law source documents remain v1.2.1 because no Product Law meaning changed.

---


## v1.2.4 Patch Scope

This is a **planning-state-only tracker patch**. It does not change Product Law, any DEC, OQ, ARQ, delivery methodology, architecture requirement, MVP scope, or implementation rule.

It only records that:

- `AR-001 — System Shape & Runtime Topology` is COMPLETE after accepted `ARC-001...ARC-026` and the AR-001 closure audit;
- `ARCHITECTURE_LAW_WORKING.md v0.4.0` is the current cumulative Architecture Law register;
- the immediate next workstream is `AR-002 — Phoenix / LiveView / Ash / Code Boundaries`;
- Phase 2 Architecture Decision Workstreams are now IN PROGRESS;
- implementation remains stopped under the existing Development Entry Hard Stop.

The Product Law source documents remain v1.2.1 because no Product Law meaning changed.

---


## v1.2.3 Patch Scope

This is a **planning-state-only hygiene patch**. It does not change Product Law, any DEC, OQ, ARQ, delivery methodology, architecture requirement, MVP scope, or implementation rule.

It only:

- corrects Section 9 so the immediate next action is `AR-001 — System Shape & Runtime Topology`;
- corrects the later reference-flow pressure-test sequence to `FLOW-01...FLOW-12`;
- removes stale wording that could imply AR-000 remains pending or could routinely reopen Grill-Me;
- leaves AR-000 COMPLETE/FROZEN at `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`.

The Product Law source documents remain v1.2.1 because no Product Law meaning changed.

---


## v1.2.2 Patch Scope

This is a **planning-state-only tracker patch**. It does not change Product Law, DEC-001 through DEC-293, the North Star, Platform semantics, MVP scope, or any expert/vendor gate.

It records only that:

- all planned AR-000 requirement extraction is complete;
- `ARCHITECTURE_REQUIREMENTS_WORKING.md` passed the global closure audit and froze at v1.0.0;
- Performance and Analytics remain closed;
- R1–R6 clustered remaining coverage is complete;
- Phase 1 is complete;
- Phase 2 begins with `AR-001 System Shape & Runtime Topology`;
- implementation remains stopped.

The Product Law source documents remain v1.2.1 because no Product Law meaning changed.

---

## v1.2.1 Patch Scope

This is a **non-semantic current-state reference hygiene patch**. It does not add, remove, reopen, weaken or supersede any Product Law decision. The v1.2 amendments remain authoritative and the v1.2 text is preserved as the immediately preceding version.

The patch only corrects stale current-state version/provider wording and related-document metadata so the active pack describes its own v1.2.1 state consistently. Historical v1.0/v1.1/v1.2 amendment text remains intentionally preserved where it describes earlier states.

## v1.2 Amendment Scope

This v1.2 amendment preserves the post-freeze planning method and records the approved upstream propagation from AR-000:

- Paystack is promoted from provisional provider choice to locked first/launch gateway via DEC-292; provider behaviour validation remains open under OQ-004.
- first-party A/B/n experimentation is added as a locked platform capability via DEC-293; exact assignment, caching, statistical engine and architecture mechanism remain downstream Architecture/Feature Pack work.
- the Architecture reference-flow suite gains FLOW-12 for experimentation so the new capability is pressure-tested before architecture freeze.

The remaining v1.1 planning sequence and JIT dossier method remain unchanged.

## v1.1 Amendment Scope (preserved historical text)

This amendment changes **planning sequence and planning granularity only**.

It does not reopen Product Grill-Me and does not alter DEC-001 through DEC-291.

The v1.1 correction:

- inserts derived architecture-requirement extraction before architecture decisions;
- requires architecture reference-flow pressure testing before architecture freeze;
- separates complete platform-wide **Domain Architecture Profiles** from **JIT implementation-grade Domain Dossiers**;
- moves `05_ROADMAP.md` after the complete Domain Map and the lightweight profile baseline, rather than after speculative implementation-grade dossiers for every future domain;
- introduces Feature Packs as the delivery-planning container between Roadmap and implementation;
- clarifies that implementation-grade OQ-039 mapping is required for affected domain/actions before the slices that depend on them are issued;
- makes Architectural Proof the first authorised executable development stage;
- keeps TOON as a just-in-time execution projection, never an authority.

Implementation remains stopped until the Development Entry Hard Stop in this document is satisfied.

# 1. Purpose

This document is the single living tracker for work that still needs to be:

- answered;
- reviewed;
- approved;
- designed;
- documented;
- or built later.

It prevents unresolved work from being hidden inside the Platform document or Decision Register.

Use the three core documents as follows:

```text
00_PLATFORM
→ current platform truth

01_DECISIONS
→ locked decisions and formal open gates

02_OPEN_WORK
→ what remains, in what order, and what blocks progress
```

When an item is resolved:

1. record the final decision in `01_DECISIONS`;
2. update `00_PLATFORM` when platform-level wording changes;
3. mark the item complete here;
4. do not leave duplicate competing rules in this document.

---

# 2. Status Values

Use only these statuses:

```text
NOT_STARTED
IN_PROGRESS
BLOCKED
EXPERT_REVIEW
READY_TO_CLOSE
COMPLETE
DEFERRED
```

Definitions:

- `NOT_STARTED`: no formal decision work has begun;
- `IN_PROGRESS`: currently being answered;
- `BLOCKED`: cannot continue until another decision or dependency is resolved;
- `EXPERT_REVIEW`: requires legal, clinical, commercial, methodology, payment-provider, or other specialist approval;
- `READY_TO_CLOSE`: answers exist but documents still need updating;
- `COMPLETE`: decisions are locked and recorded;
- `DEFERRED`: intentionally excluded until a named future trigger occurs.

---

# 3. Completed Grill-Me Rounds

| Round | Scope | Status |
|---|---|---|
| GQ-001 | Ultimate goal and commercial foundation | COMPLETE |
| GQ-002 | Users, actors, roles, registration and data ownership | COMPLETE |
| GQ-003 | Products, purchases, memberships and entitlements | COMPLETE |
| GQ-004 | Temperament assessment, scoring and reports | COMPLETE |
| GQ-005 | Health onboarding, eligibility and safety | COMPLETE |
| GQ-006 | Plan generation, lifecycle and adjustments | COMPLETE |
| GQ-007 | Content, translation and personalised feeds | COMPLETE |
| GQ-008 | Programmes, habits, journals and progress | COMPLETE |
| GQ-009 | Community, challenges, live sessions and events | COMPLETE |
| GQ-NY-001 | Nuwe Jy flagship product | COMPLETE |
| GQ-010 | Privacy, records and data lifecycle | COMPLETE |
| GQ-011 | Identity, security, notifications and operations | COMPLETE |
| GQ-012 | Launch scope, product spaces, pilot, pricing and go/no-go | COMPLETE |

Completed rounds must not be reopened casually.

Reopen a completed round only when:

- a contradiction is discovered;
- expert review invalidates a locked assumption;
- a later decision materially changes the domain model;
- or the commercial model changes significantly.

A reopened decision must be marked `SUPERSEDED` or amended explicitly in `01_DECISIONS`.
# 4. Product Grill-Me Status

## GQ-012 — COMPLETE

GQ-012A locked:

- one operating platform with controlled product spaces;
- women’s health/lifestyle as the only launch-facing space;
- South Africa-first market activation;
- exact core MVP loop;
- all approved temperament provenance paths;
- three-product launch catalogue;
- Nuwe Jy as first flagship expansion;
- Basic Membership readiness gate;
- adjustment capability before Premium;
- controlled practitioner pilot;
- Facebook-first community sequence;
- live integration before full event commerce.

GQ-012B locked:

- staged paid rollout;
- first paid pilot max 50 with 10 → 25 → 50 review points;
- MVP list prices R249 / R399 / R549;
- future Basic Membership planning anchor R199/month and R1,990/year;
- small explicit bundle model;
- governed complimentary/sponsored grants;
- Nuwe Jy activation gate;
- practitioner saleable-capacity gate;
- cross-functional paid-pilot readiness;
- progressive load/performance gates;
- pilot success criteria;
- release/rollback authority.

## Product Grill-Me Stop Condition — MET

All product Grill-Me rounds are complete.

Do not schedule further product Grill-Me rounds unless:

- an expert decision contradicts a locked product assumption;
- a genuine new business direction appears;
- architecture discovers a real product contradiction that cannot be resolved from the current approved Product Law pack.

Ordinary architecture detail is not grounds to reopen product Grill-Me.
# 5. Expert, Vendor and Architecture Gates

These gates may permit planning to continue, but each blocks the affected production capability.

## 5.1 Legal, ownership and commercial

- **OQ-001:** final operating entity;
- IP/licence/model/book/translation/contributor rights;
- terms/privacy/consumer wording;
- practitioner/sponsor agreements;
- **OQ-028:** LearnDash obligations and retirement;
- **OQ-029:** full retention schedule matrix.

## 5.2 Pricing and payments

- **OQ-003 / OQ-012:** monthly review contract/timing;
- **OQ-004:** Paystack recurring, webhook, retry, proration, refund and chargeback behaviour;
- international-card and future multi-currency activation;
- EFT reconciliation.

## 5.3 Clinical and methodology

- **OQ-005:** exact eligibility matrix;
- **OQ-006:** temperament score-distance thresholds;
- **OQ-007:** laboratory validity;
- **OQ-008:** urgent-help wording;
- **OQ-010:** calculation values;
- **OQ-011:** adjustment thresholds;
- **OQ-019:** programme-specific completion metrics;
- **OQ-025:** Nuwe Jy safety/completion thresholds;
- **OQ-033:** professional record authority.

## 5.4 Content, translation, media and search

- **OQ-013:** translation resource model;
- **OQ-014:** Cloudflare/edge cache design;
- **OQ-015:** search configuration;
- **OQ-016:** scheduled publication operations;
- **OQ-020:** Restream/Cloudflare live validation;
- **OQ-021:** recording/video consent/retention;
- **OQ-024:** Nuwe Jy source-content/media inventory.

## 5.5 Community, events and Nuwe Jy operations

- **OQ-022:** event reservation/performance architecture;
- **OQ-023:** Facebook moderation/privacy operating policy;
- **OQ-026:** Nuwe Jy operational capacity;
- **OQ-027:** Nuwe Jy communication configuration.

## 5.6 Privacy, security and continuity

- **OQ-009:** health/professional retention umbrella;
- **OQ-017:** reminder delivery design;
- **OQ-018:** journal encryption/retention;
- **OQ-030:** external processor deletion/export inventory;
- **OQ-031:** backup restore/deletion replay;
- **OQ-032:** export/deletion operations;
- **OQ-034:** authentication implementation architecture;
- **OQ-035:** abuse-control thresholds; **accepted implementation/proof candidate note:** Hammer is the preferred application-layer candidate behind a platform-owned replaceable boundary; Redis-backed/shared semantics are preferred where cross-node velocity coherence is required, but concrete package version/backend/algorithm and all thresholds remain proof/JIT decisions;
- **OQ-036:** notification providers/channel policy;
- **OQ-037:** RPO/RTO;
- **OQ-038:** incident ownership.

## 5.7 Performance and scaling

- **OQ-039 — two-level performance/scaling mapping:**
  1. before Roadmap, every approved domain receives a lightweight Domain Architecture Profile covering authoritative state ownership, broad hot/warm/cold classification, concurrency sensitivity, major scaling risks, and whether Redis, ETS/Cachex, GenServer, PubSub, Oban, replicas and streaming/pagination are potentially applicable or explicitly `NONE` / not justified;
  2. before an affected implementation slice is issued, every domain/action touched by that Feature Pack or slice receives implementation-grade mapping for indexes, Redis structure or `NONE`, TTL/invalidation or `NONE`, GenServer ownership or `NONE`, PubSub or `NONE`, Oban or `NONE`, replica use, streaming/pagination, concurrency/idempotency behaviour and relevant 100k-concurrency characteristics;
- future domains/actions outside the current delivery scope do not require speculative implementation-grade mapping before development begins;
- validate high-demand checkout/event paths for queueing, rate limits, expiring holds, thundering-herd and cache-stampede protection when those paths enter delivery scope;
- confirm target behaviour under horizontal multi-node operation and 100k-concurrent-user assumptions where relevant;
- this changes timing/granularity only and does **not** weaken correctness, privacy, clinical-safety, financial-integrity, performance or horizontal-scaling requirements.

## 5.8 First-party experimentation architecture proof

- **OQ-040:** prove the first-party experimentation architecture against DEC-293 and the closed AR-000 Analytics requirements, including page/email authoring boundaries, deterministic A/B/n assignment, anonymous-to-known continuity, concurrent-experiment isolation, exposure logging, authoritative conversion attribution, statistical methodology, immutable aggregate result evidence, privacy/deletion handling, variant-safe caching and failure/recovery;
- FunWithFlags, Bandera or an equivalent implementation remains an Architecture candidate only until the assignment primitive passes the required proof;
- experiment-sensitive HTML must preserve clean/canonical public URLs and prevent cache cross-contamination between assigned treatments.

# 6. Work Explicitly Deferred Until After Grill-Me

Do not decide these inside product Q&A:

- exact Ash Resource names;
- table and column names;
- migrations;
- indexes;
- cache keys;
- Redis key formats;
- TTL values;
- Oban worker names;
- PubSub topics;
- GenServer modules;
- API endpoints;
- folder paths;
- package selection;
- UI component structure;
- exact implementation sequence;
- exact browser-storage use;
- exact PubSub broadcast rules;
- exact PgBouncer/read-replica sizing.

These belong, at the appropriate level of granularity, to architecture, Domain Architecture Profiles, JIT Domain Dossiers, Feature Pack planning and authorised implementation tasks.

---

# 7. Architecture and Delivery Documentation Sequence

The v1.0 product freeze remains the historical baseline. v1.1 changed downstream planning governance. v1.2 preserves that method and appends DEC-292–DEC-293 as explicit post-freeze Product Law amendments.

The canonical forward sequence is:

```text
PHASE 0   Frozen Product Law
PHASE 1   AR-000 Architecture Requirement Extraction
PHASE 2   Architecture Decision Workstreams
PHASE 3   Reference-Flow Pressure Testing
PHASE 4   03_ARCHITECTURE synthesis/review/freeze
PHASE 5   04_DOMAIN_MAP + Domain Architecture Profiles
PHASE 6   05_ROADMAP
PHASE 7   Feature Pack preparation + JIT Domain Dossiers
PHASE 8   Architectural Proof
PHASE 9   Vertical Slices
PHASE 10  Horizontal Hardening
PHASE 11  Release / Readiness Gate
```

TOON is not a separate planning phase. It is generated just in time for an already approved TB, VS or HH task.

## Phase 0 — COMPLETE: Frozen Product Law

Historical freeze pack:

```text
PROJECT_NORTH_STAR_AND_MVP_v1.0.md
00_PLATFORM_v1.0.md
01_DECISIONS_v1.0.md
02_OPEN_WORK_v1.0.md
```

The preservation audit proved the historical freeze. The v1.2 amendment preserves DEC-001 through DEC-291 as history and explicitly appends DEC-292–DEC-293 rather than silently rewriting them.

Do not reopen routine Product Grill-Me. Reopen Product Law only for a genuine contradiction, an expert finding that invalidates an assumption, or a deliberately approved new business direction.

## Phase 1 — COMPLETE: AR-000 Architecture Requirement Extraction

Create:

```text
ARCHITECTURE_REQUIREMENTS_WORKING.md
```

Mark it prominently:

```text
DERIVED WORKING ARTIFACT
NON-AUTHORITATIVE
DOES NOT MODIFY PRODUCT LAW
```

AR-000 exists to prove that architecture is derived from Product Law rather than from preferred implementation patterns.

Each architecture-relevant requirement should receive an `ARQ-nnn` entry containing at minimum:

- requirement;
- exact Product Law source;
- source status / normative strength;
- architectural implication;
- architecture workstream;
- blocking classification;
- architecture status;
- notes where needed.

AR-000 must cover the full architecture-relevant Product Law surface, including system/runtime shape, Phoenix/LiveView, Ash/application boundaries, identity/authentication/authorisation, actor propagation, field policies, consent, audit, versioning/immutability, PostgreSQL authority, transactions, concurrency, idempotency, state acceleration, object storage/CDN/browser-local state, async work, PubSub/realtime, notifications, content/translation/media, integrations, privacy/deletion, backup/restore, analytics, deployment, degradation, observability, multi-node behaviour and performance/scaling.

AR-000 must distinguish:

```text
authority
≠
acceleration
```

PostgreSQL-only is valid where it safely satisfies the required correctness and performance envelope. Redis, ETS/Cachex and GenServer are not mandatory merely because they are available.

AR-000 must not decide final domain ownership, exact Ash Resources, tables, migrations, indexes, Redis keys, TTLs, worker names, PubSub topics or implementation source code.

Exit condition:

- every architecture-relevant Product Law obligation is represented;
- source coverage is auditable;
- contradictions/missing policy are surfaced;
- architecture workstreams can begin without guessing.

**Phase 1 completion:** MET on 2026-08-16. `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` is the frozen AR-000 requirement handoff. No further AR-000 concern round is planned unless a genuine Product Law amendment, contradiction or expert invalidation requires reopening.

## Phase 2 — COMPLETE: Architecture Decision Workstreams

AR-000 defines what architecture must make true. Phase 2 decides how.

**Current Phase 2 state:** `AR-001` COMPLETE (`ARC-001...ARC-026`); `AR-002` COMPLETE (`ARC-027...ARC-058`); `AR-003` COMPLETE (`ARC-059...ARC-109`); `AR-004` COMPLETE (`ARC-110...ARC-145`); `AR-005` COMPLETE (`ARC-146...ARC-188`); `AR-006` COMPLETE (`ARC-189...ARC-232`, final 66-ARQ closure audit PASS); `AR-007` COMPLETE (`ARC-233...ARC-254`, final 51-ARQ closure audit PASS); `AR-008` COMPLETE (`ARC-255...ARC-290`, final 321-ARQ closure audit PASS); `AR-009` COMPLETE (`ARC-291...ARC-326`, final 155-ARQ closure audit PASS). `ARC-327` is a post-closure Phase 3 proof-governance amendment to ARC-326 timing only. **Phase 2 remains COMPLETE.**

The starting workstreams are:

```text
AR-001  System Shape & Runtime Topology
AR-002  Phoenix / LiveView / Ash / Code Boundaries
AR-003  State Authority, Persistence, Caching & Storage
AR-004  Identity, Authentication, Authorisation & Field Privacy
AR-005  Transactions, Consistency, Async & Realtime
AR-006  Content, Translation, Media & External Integrations
AR-007  Privacy, Deletion, Backup & Restore
AR-008  Reliability, Deployment, Operations & Observability
AR-009  Performance, Scaling & Multi-Node Behaviour
```

These workstream labels may be split or combined after AR-000 if the coverage remains complete.

Actual architectural law is recorded as `ARC-nnn` decisions. Every ARC must identify its source ARQs, decision, rationale, rules, failure behaviour, security/privacy implications, performance/scaling implications, enforcement and downstream gates.

Architecture may establish platform mechanisms and interaction doctrine. It must not prematurely assign final concrete business ownership that belongs to Domain Law.

## Phase 3 — Reference-Flow Pressure Testing — COMPLETE

Before architecture synthesis/freeze, pressure-test representative cross-cutting flows to answer:

> Can this flow traverse accepted Architecture Law coherently without an undocumented mechanism or governing contradiction?

Required flows:

```text
FLOW-01  Registration → verification → login
FLOW-02  Checkout → provider verification → payment → entitlement
FLOW-03  Assessment → submission → scoring → immutable result → report
FLOW-04  Health intake → safety evaluation → eligibility
FLOW-05  Eligibility → deterministic plan generation → immutable plan
FLOW-06  New health risk → safety effect → dependent plan behaviour
FLOW-07  Nuwe Jy scheduled release → durable work → notification → LiveView
FLOW-08  Full deletion → storage/processors → backup boundary
FLOW-09  Future event hold → payment → ticket / expiry
FLOW-10  Consent → practitioner relationship → scoped access → audit → expiry/revocation
FLOW-11  Safety-critical correction/withdrawal → dependency discovery → invalidation → operational/participant response → audit
FLOW-12  Experiment draft/version → eligibility → stable assignment → variant-safe delivery/cache → exposure → authoritative outcome → statistical readout → immutable result/decision → archive/deletion boundary
```

Each flow uses the lean Phase 3 contract:

```text
purpose
→ governing DEC / ARC / OQ references
→ concise architecture trace
→ hard invariants
→ meaningful failure pressure
→ later executable proof obligations
→ gap / contradiction / premature-design review
→ verdict
```

Per `ARC-327`, Phase 3 records only the **proof-obligation projection** of the Performance & Capacity Proof Matrix:

- performance-sensitive: YES / NO;
- material scale/resource concern;
- hard performance/correctness invariant;
- later executable proof required: YES / NO;
- applicable future proof stage.

Runtime-only workload/topology/cardinality/concurrency/latency/resource/tool/result/safe-envelope/breakpoint fields are instantiated under the full `ARC-326` matrix when executable evidence exists in Architectural Proof, affected Feature Packs/slices, Horizontal Hardening or Release Gates.

Do not repeat Product Law/Architecture Law prose when stable IDs suffice. Do not invent Domain ownership, Resources, schema, indexes, cache keys, thresholds, package choices or test sizes.

**Phase 3 completion evidence:** `REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`.

**Closure result:**

```text
12/12 flows complete
1 PASS
11 PASS_WITH_DOWNSTREAM_GATES
0 FAIL_ARCHITECTURE_GAP
0 BLOCKED_CONTRADICTION
0 Product Law amendments
0 ARQ amendments
0 flow-mechanism ARC additions
```

Exit condition — **MET**:

- no required flow depends on an undocumented architectural mechanism;
- no flow creates contradictory architecture rules;
- downstream expert/provider/JIT/proof gates are explicit and remain in their correct authority layer.

## Phase 4 — COMPLETE: `03_ARCHITECTURE_v1.0.0.md`

Synthesize the approved architecture work into:

```text
03_ARCHITECTURE.md
```

It must define at minimum:

- system context and architectural style;
- runtime/deployment topology;
- Phoenix/LiveView/Ash responsibilities;
- application and infrastructure boundaries;
- domain-interaction rules;
- identity/authentication/authorisation/field-policy mechanisms;
- PostgreSQL and other state authority;
- immutability/versioning/audit doctrine;
- data temperature and justified acceleration;
- transactions, consistency and idempotency;
- durable async work and realtime observation;
- content/translation/media/integrations;
- privacy/deletion/backup/restore;
- graceful degradation;
- operations/deployment/observability;
- performance/scaling/multi-node behaviour;
- architecture enforcement;
- ARC register;
- downstream gates;
- Domain Map handoff.

Before freeze, perform:

1. ARQ → ARC/downstream-gate traceability audit;
2. architecture consistency review;
3. security/privacy review;
4. failure/recovery review;
5. performance/scaling review;
6. perform a lightweight traceability check that `03_ARCHITECTURE.md` still represents the already-passed FLOW-01 through FLOW-12 paths; rerun only the specific flow(s) materially affected by a synthesis correction or later Architecture amendment.

Freeze only when Domain Map can proceed without inventing architecture.

**Phase 4 completion evidence:** `03_ARCHITECTURE_v1.0.0.md`.

**Closure result:** PASS — 327/327 ARC thematic coverage; 10/10 ARQ families represented; FLOW-01...FLOW-12 traceability 12/12; 0 real ARC conflicts; Domain Map readiness PASS.

## Phase 5 — COMPLETE: `04_DOMAIN_MAP_v1.0.0.md` + Domain Architecture Profiles

### 5A — Complete Domain Map

Create:

```text
04_DOMAIN_MAP.md
```

It must define all known approved mature-platform domains and, for each:

- purpose;
- authoritative ownership;
- major entities/resources/concepts;
- major relationships;
- major states/state machines;
- core capabilities/actions at domain level;
- important policies;
- external dependencies;
- cross-domain dependencies;
- key invariants;
- data-integrity rules;
- sensitive-data classification where relevant;
- important commands/events/contracts where useful.

Historical pre-Phase-5 domain hypotheses were:

```text
Accounts
IdentityAndAccess
Consent
Temperaments
HealthProfiles
Safety
Content
Programmes
Habits
Journals
Plans
Recommendations
Commerce
Entitlements
Memberships
Community
Challenges
Events
Practitioners
Notifications
Analytics
Administration
Audit
```

This hypothesis list was not preserved blindly. Phase 5 approved the following 18 ownership domains: `Identity & Access`, `Privacy & Consent`, `Temperament`, `Health Records`, `Safety & Eligibility`, `Plans & Nutrition`, `Content & Media`, `Programmes & Challenges`, `Habits, Journals & Progress`, `Commerce`, `Entitlements`, `Community`, `Events & Live`, `Professional Care`, `Communications`, `Experimentation`, `Analytics`, and `Audit & Evidence`.

The Domain Map must eliminate shared-write ambiguity and establish one authoritative owner for every major durable business truth.

### 5B — Complete one lightweight Domain Architecture Profile per approved domain

A **Domain Architecture Profile** is a pre-Roadmap architecture/domain baseline. It is deliberately less detailed than an implementation-grade Domain Dossier.

Every profile must contain enough to make delivery sequencing safe, including:

- domain purpose and authoritative ownership;
- major resources/concepts and lifecycle/state-machine summary;
- major cross-domain dependencies;
- key invariants and privacy/sensitivity classification;
- transaction/concurrency sensitivity;
- authoritative storage layer;
- broad hot/warm/cold classification;
- major scaling risks;
- whether Redis is potentially applicable or `NONE` / not justified;
- whether ETS/Cachex is potentially applicable or `NONE` / not justified;
- whether GenServer ownership is potentially applicable or `NONE` / not justified;
- whether PubSub is potentially applicable or `NONE` / not justified;
- whether Oban is potentially applicable or `NONE` / not justified;
- replica/streaming/pagination relevance at architecture level;
- major unresolved gates affecting future implementation.

A Domain Architecture Profile must **not** speculatively fix:

- exact table/column design;
- exact indexes;
- exact Redis keys/structures where the access pattern is not yet known;
- exact TTLs;
- exact worker names/queue names;
- exact PubSub topics;
- exact API endpoints;
- detailed implementation actions;
- source code.

Phase 5 exit condition:

- every known approved mature-platform capability has a domain home;
- every major durable truth has one owner;
- cross-domain interaction is coherent;
- all approved domains have a lightweight architecture profile;
- the MVP can be sequenced without creating a dead-end for approved future capabilities;
- Roadmap can proceed without requiring speculative implementation-grade dossiers.

**Phase 5 completion evidence:** `04_DOMAIN_MAP_v1.0.0.md`.

**Closure result:** PASS — 18 approved domains; 48/48 ownership-matrix truths have one listed owner; 18/18 lightweight profiles complete; 0 shared-write ambiguities; 0 circular authoritative control dependencies; no new Architecture mechanism required.

## Phase 6 — NEXT: `05_ROADMAP.md`

Create:

```text
05_ROADMAP.md
```

The Roadmap works backward from the mature platform and then identifies the smallest safe commercial path through it.

It must define:

- delivery phases and sub-phases;
- outcome-oriented Feature Packs (`FP-nnn`);
- Feature Pack dependencies;
- validation objective/hypothesis for each Feature Pack;
- MVP path;
- pilot progression;
- Nuwe Jy path;
- membership/adjustment/Premium path;
- practitioner path;
- major gates;
- anticipated architectural-proof dependencies;
- deferred capabilities;
- release/readiness sequence;
- completion criteria.

A **Feature Pack** is an outcome-oriented delivery container representing a coherent participant, operator or platform capability.

The Roadmap must not require implementation-grade Domain Dossiers for every future domain before it can be approved.

## Phase 7 — Feature Pack Preparation + JIT Domain Dossiers

Prepare one Feature Pack at a time.

### 7A — FP Skeleton

Each `FP-nnn` starts with enough definition to discover what detailed domain law is required:

- outcome;
- validation objective/hypothesis;
- type;
- in scope / out of scope;
- entry dependencies;
- affected domains;
- applicable DEC/ARC references;
- preliminary Gate Manifest;
- preliminary performance/safety/privacy concerns.

The Gate Manifest classifies at minimum:

```text
AUTHORITATIVE PRODUCT DECISIONS
APPLICABLE ARCHITECTURE DECISIONS
AFFECTED DOMAINS
REQUIRED JIT DOSSIERS
BLOCKING OQs
NON-BLOCKING FUTURE OQs
WHY NON-BLOCKING
ENTRY STOP CONDITION
```

Resolve gates at the earliest point required to prevent downstream guessing, but do not resolve unrelated future gates merely for completeness.

### 7B — JIT implementation-grade Domain Dossiers

Complete only the detailed dossiers required by the selected Feature Pack.

A dossier covers, where applicable:

- purpose;
- resources and relationships;
- actions and validations;
- policies and field policies;
- calculations and aggregates;
- detailed state machines/invariants;
- concrete indexes;
- concurrency/idempotency behaviour;
- audit;
- data temperature;
- cache/TTL/invalidation;
- Redis representation or explicit `NONE`;
- ETS/Cachex/GenServer use or explicit `NONE`;
- PubSub or explicit `NONE`;
- Oban or explicit `NONE`;
- integrations;
- privacy/security;
- implementation-grade OQ-039 performance/scaling mapping for affected actions;
- tests;
- STOP conditions.

This is still planning law. Exact implementation source code is not written here.

### 7C — Final Feature Pack Contract

After required dossiers and blocking gates are resolved, finalise:

- outcome and validation objective;
- in/out scope;
- entry conditions;
- affected domains;
- applicable Product Law and ARCs;
- final Gate Manifest;
- architectural-proof requirement;
- Vertical Slice map;
- horizontal-hardening requirements;
- performance envelope;
- security/privacy envelope;
- failure/recovery expectations;
- future extension hooks;
- exit criteria;
- release/readiness implications;
- STOP conditions.

The final Feature Pack Contract is the development-entry authority for that Feature Pack.

## Phase 8 — Architectural Proof

Phase 8 is the **first authorised executable development stage**.

Every Feature Pack must state whether its architectural proof is:

```text
REUSE_EXISTING_PROOF
or
NEW_TRACER_BULLET
```

Do not create ceremonial tracer bullets.

A new `TB-nnn` exists only to prove a materially unproven architectural claim/path. A real tracer bullet uses the real architecture: authentication where relevant, Ash policy path, persistence, domain boundaries, transaction mechanism, required idempotency, async boundary and audit path.

It may reduce breadth. It may not bypass architectural correctness.

If the proof fails, correct architecture/domain law before vertical expansion.

## Phase 9 — Vertical Slices

A `VS-nnn` delivers one useful production-quality behaviour through every required layer.

A slice must include, where applicable:

- interface/LiveView behaviour;
- authorised Ash/application action;
- actor/policy/field-policy enforcement;
- domain invariants;
- durable state;
- async consequences;
- PubSub observation;
- audit;
- observability;
- correctness/concurrency/idempotency;
- required database constraints/indexes;
- safe cache/invalidation behaviour;
- automated tests;
- acceptance criteria.

Do not defer correctness, privacy or security to hardening.

Every TB/VS receives one self-contained implementation task containing one outcome, exact scope, authoritative references, files/resources/actions, data changes, security/privacy, concurrency, indexes, cache/TTL, Redis/GenServer/PubSub/Oban rule or `NONE`, performance, observability, tests, acceptance criteria, minimal tools and STOP conditions.

## Phase 10 — Horizontal Hardening

`HH-nnn` work strengthens capabilities that are already correct.

Use evidence from measurements, failure tests, security review, pilot operation or explicit release gates.

Examples may include:

- load/stress testing;
- cache/Redis optimisation;
- queue saturation testing;
- provider-failure exercises;
- failover/restore exercises;
- security/penetration testing;
- accessibility sweeps;
- telemetry/dashboard strengthening;
- multi-node stress;
- cache-stampede/thundering-herd protection;
- deletion/restore exercises.

Do not create hardening work merely because a technology exists.

## Phase 11 — Release / Readiness Gate

A Feature Pack may unlock a public release or only another dependency.

Its gate therefore produces one of:

```text
PROCEED
ITERATE
REPEAT PILOT
PAUSE
ROLL BACK
```

using evidence.

Release/readiness evidence must answer, where applicable:

- whether the Feature Pack achieved its objective;
- whether acceptance criteria passed;
- whether blocking OQs are resolved;
- whether architectural proof remains valid;
- whether security/privacy requirements pass;
- whether performance envelopes pass;
- whether runbooks/support ownership are sufficient;
- whether rollback criteria are defined;
- which downstream dependencies are now unblocked.

## TOON Execution Rule

TOON is an ephemeral just-in-time execution projection generated only after a TB, VS or HH task is approved.

```text
approved TB / VS / HH contract
→ generate one JIT TOON
→ coding agent executes exactly that task
→ verify acceptance criteria/evidence
→ STOP
```

A TOON prompt may not redesign Product Law, architecture, domain ownership, Feature Pack scope or slice boundaries. If it would need to invent missing planning, STOP and repair the upstream artifact.

# 8. Product Planning Stop Condition

**Status: MET.**

The Product Grill-Me phase remains complete because:

1. GQ-001 through GQ-012 and GQ-NY-001 are complete.
2. Remaining unknowns are expert/vendor/architecture/operations gates.
3. No known unresolved product question requires routine Product Grill-Me to continue.
4. DEC-001 through DEC-291 remain preserved; DEC-292 and DEC-293 are the explicit v1.2 post-freeze amendments.
5. Architecture can begin without inventing product policy.

Product Law may reopen only for a genuine contradiction, an expert finding that invalidates an assumption, or an approved new business direction.

## Development Entry Hard Stop

**Executable development remains stopped through Phase 7. Phase 8 Architectural Proof is the first authorised executable development stage.**

No TB/VS/HH implementation may begin until, for the selected Feature Pack:

1. `03_ARCHITECTURE` is approved;
2. `04_DOMAIN_MAP` is approved;
3. all approved domains have their Domain Architecture Profiles;
4. `05_ROADMAP` is approved and the Feature Pack is selected from it;
5. the Feature Pack Skeleton and Gate Manifest identify the affected domains and gates;
6. every required JIT Domain Dossier is approved;
7. every blocking expert/vendor/architecture/operations gate is resolved or the Feature Pack explicitly excludes the blocked capability;
8. the Final Feature Pack Contract is approved;
9. the Architectural Proof Requirement is explicitly `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`;
10. the implementation task can prove acceptance criteria without inventing upstream law.

Implementation remains stopped unless every Development Entry Hard Stop condition above is satisfied.

# 9. Immediate Next Action

```text
PHASE 2 — COMPLETE
PHASE 3 — COMPLETE
PHASE 4 — COMPLETE / ARCHITECTURE FROZEN v1.0.0
PHASE 5 — COMPLETE / DOMAIN MAP + PROFILES FROZEN v1.0.0

Immediate next substantive action:

PHASE 6
→ create 05_ROADMAP.md
→ work backward from the mature platform
→ define outcome-oriented Feature Packs and dependencies
→ identify the smallest safe commercial/MVP path
→ preserve Nuwe Jy, membership/Premium and practitioner expansion paths
→ sequence expert/vendor/Architectural-Proof gates without speculative implementation dossiers
→ freeze Roadmap only after Phase 6 PASS
```

Do not begin implementation. Do not redesign frozen Architecture or Domain ownership inside Roadmap; route any genuine contradiction to the governing upstream artifact.

# 10. Minimal Tools

For architecture/domain/delivery planning, use the least tools needed:

- read access to the frozen/current core Markdown documents;
- Markdown editing;
- approved source material when a domain term/methodology depends on the book;
- current official technical documentation when actual current framework/provider behaviour must be verified;
- expert/vendor evidence when a named gate requires it.

Do not use executable implementation tooling before the selected Feature Pack reaches Phase 8:

- Ash generators;
- migrations;
- package installation for product implementation;
- repository scaffolding;
- deployment tooling;
- implementation agents.

During Phase 8 onward, the exact allowed tools must be stated in the approved TB/VS/HH task.

# 11. Global STOP Routing

A planner or coding agent must STOP and route the blocker to the correct authority rather than making a plausible assumption.

```text
missing/conflicting product policy
→ Product Law / DEC amendment

missing/conflicting platform mechanism
→ Architecture / ARC

missing/conflicting domain ownership or invariant
→ Domain Map / Domain Law

missing implementation semantics for an affected domain/action
→ JIT Domain Dossier

scope/dependency/gate problem
→ Feature Pack / Roadmap

execution ambiguity
→ TB / VS / HH contract
```

Additional STOP conditions include:

- clinical policy is required but unresolved;
- legal/commercial policy is required but unresolved;
- required provider behaviour has not been validated;
- sensitive data would be exposed beyond approved policy;
- a lower-level artifact conflicts with upstream authority;
- a slice crosses its Feature Pack boundary;
- complexity is introduced without a current or locked future requirement;
- a TOON prompt would need to invent missing planning;
- acceptance criteria cannot be proven.

STOP means surface the blocker at the correct level. It does not mean silently reconcile, guess or redesign upstream law.
