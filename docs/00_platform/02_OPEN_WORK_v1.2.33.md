# 02_OPEN_WORK_v1.2.33.md

- **Document status:** POST-STAGE-3B OPEN-WORK SUCCESSOR v1.2.33
- **Authoritative for:** Remaining unresolved planning questions, expert/vendor/architecture/operations gates, post-grilling deliverables, planning and delivery sequencing, and planning/development stop conditions
- **Not authoritative for:** Locked product decisions, platform truth, implementation details, Ash Resources, schemas, or legal and clinical conclusions
- **Related documents:**
  - `00_PLATFORM_v1.3.0.md`
  - `01_DECISIONS_v1.3.0.md`
  - `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
  - `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`
  - `reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md`
  - `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`
  - `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md`
  - `03_ARCHITECTURE_v1.0.0.md`
  - `04_DOMAIN_MAP_v1.0.0.md`
  - `05_ROADMAP_v1.0.0.md`
  - `archive/05_ROADMAP_WORKING_v0.1.0.md`
  - `reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md`
  - `archive/FOUNDATION_READINESS_AUDIT_v1.0.0.md`
- **Last updated:** 2026-09-04
- **Current planning position:** The **Targeted Product Amendment Programme** is the current authority-stage workstream. Stage 1 (Targeted Product Amendment Grill), Stage 2 (governed Product Law amendment), Stage 3A.1 (Product-Law AR-000 delta analysis) and Stage 3A.2 (governed AR-000 amendment) are **COMPLETE**. **NEXT AUTHORISED AUTHORITY-STAGE WORK: Architecture Grill** (`NOT_STARTED / NEXT`). Stage 3B Independent Architecture/Engineering Classification is **COMPLETE**. Engineering-Policy Grill and Architecture amendment remain **NOT_STARTED**; later Architecture/Domain/Roadmap/Atlas/HARDEN-02/FP-001 reconciliation remains **downstream / not current**. **PLANNING FOUNDATION: READY**. **EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS.** FP-001 Phase 7A, the Identity & Access JIT Domain Dossier and OQ-034 resolution remain factual completed milestones, but ordinary Phase 7B continuation and HARDEN-02 remain suspended until the targeted amendment programme reaches its approved downstream reconciliation point.

---


## Historical changelog

- Planning-state SemVer transition: `v1.2.32 → v1.2.33`.
- Records Stage 3B Independent Architecture/Engineering Classification complete in `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md`; the artifact is non-authoritative and pending exact-head independent review.
- Stage 3B classified 38 independent propositions: 0 Architecture Grill inputs, 7 Engineering-Policy Grill inputs, 0 split inputs, 5 deferred inputs, 7 rejected inputs and 19 already governed inputs; no upstream contradiction was found. The independent Stage 3B input stream contributes zero current Architecture decisions; Architecture Grill remains next because the separate governed Product-derived AR-000 v1.1.0 input stream from Stage 3A.2 still requires downstream closure.
- Keeps Architecture Grill as the next authorised stage and leaves Engineering-Policy Grill, Architecture amendment and later reconciliation downstream.
- Preserves the non-authoritative Stage 3A.1 analysis at `archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md`; it is historical evidence, not active working authority.
- Routes current AR-000 to `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` and preserves v1.0.0 in the archive.
- Does not amend North Star/MVP, Architecture, Domain Map, Roadmap, FP-001 or authorise implementation.

Historical planning-state entries are preserved in `archive/02_OPEN_WORK_CHANGELOG_v1.0.0.md`. That archive artifact is evidence only; this file's numbered sections are the current Open Work authority.

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

**Phase 1 completion:** MET on 2026-08-16. The v1.0.0 AR-000 requirement handoff was frozen at that date and is preserved as `archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`. The approved v1.3.0 Product Law amendment then triggered Stage 3A.1 delta analysis and the governed Stage 3A.2 append-only amendment, now complete in `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`.

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

**Phase 3 completion evidence:** `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`.

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

## Phase 6 — COMPLETE: `05_ROADMAP_v1.0.0.md`

Create and freeze:

```text
archive/05_ROADMAP_WORKING_v0.1.0.md  — preserved historical planning evidence
05_ROADMAP_v1.0.0.md          — FROZEN / COMPLETE ROADMAP
```

The Roadmap works backward from the approved mature platform, defines the smallest safe commercial path, sequences outcome-oriented Feature Packs, preserves all approved expansion paths, schedules gates at the first point required, exposes anticipated proof needs and defers implementation-grade detail to Phase 7.

**Phase 6 completion:** PASS. The closure audit confirmed no unresolved circular Feature Pack dependency, no new Product/Architecture/Domain law, no implementation-grade dossier work and sufficient information to select FP-001 after the Foundation Readiness Audit.

**Next:** Foundation Readiness Audit. This audit is deliberately not started by Phase 6 closure.

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
4. DEC-001 through DEC-291 remain preserved; DEC-292 and DEC-293 are the explicit v1.2 post-freeze amendments; DEC-294 through DEC-298 are the explicit v1.3.0 Targeted Product Amendment additions.
5. Stage 3A.1 classified the Product-derived AR-000 delta without amending the frozen register; Stage 3A.2 has now incorporated that approved delta into the cumulative v1.1.0 successor.
6. Stage 3B must independently classify Architecture/Engineering inputs before any Architecture Grill or Architecture amendment; downstream work must not invent product policy.

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
CURRENT AUTHORITY-STAGE PROGRAMME: TARGETED PRODUCT AMENDMENT → FP-001 DEVELOPMENT ENTRY READINESS
STAGE 1 — TARGETED PRODUCT AMENDMENT GRILL: COMPLETE
STAGE 2 — GOVERNED PRODUCT LAW AMENDMENT: COMPLETE
STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE
STAGE 3A.2 — GOVERNED AR-000 AMENDMENT: COMPLETE
STAGE 3B — INDEPENDENT ARCHITECTURE/ENGINEERING CLASSIFICATION: COMPLETE
ARCHITECTURE GRILL: NOT_STARTED / NEXT
ENGINEERING-POLICY GRILL: NOT_STARTED
ARCHITECTURE AMENDMENT: NOT_STARTED
LATER ARCHITECTURE / ENGINEERING STANDARDS / DOMAIN PRESSURE TEST / ROADMAP / ATLAS / HARDEN-02 / FP-001 RECONCILIATION: DOWNSTREAM / NOT CURRENT

CURRENT FEATURE PACK (FACTUAL, NOT CURRENT TASK): FP-001
LAST APPROVED FP-001 MILESTONE: PHASE 7A COMPLETE; IDENTITY & ACCESS JIT DOMAIN DOSSIER COMPLETE / MERGED; OQ-034 ARCHITECTURE SELECTION RESOLVED

REQUIRED DOSSIERS (FACTUAL STATE):
- IDENTITY & ACCESS: COMPLETE / MERGED
- COMMUNICATIONS: REQUIRED / NOT_STARTED

CONDITIONAL DOSSIER DISPOSITIONS:
- PRIVACY & CONSENT: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- CONTENT & MEDIA: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- AUDIT & EVIDENCE: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- ANALYTICS: NOT REQUIRED

OPEN GATES:
- OQ-035: SECURITY / OPERATIONS REVIEW; UNRESOLVED; RELEASE-ONLY SCOPE
- OQ-036: VENDOR / OPERATIONS REVIEW; UNRESOLVED; RELEASE-ONLY SCOPE

PHASE 7C: BLOCKED / NOT_STARTED pending the required Communications dossier and explicit conditional-dossier dispositions.
PROOF CLASSIFICATION: NOT FINALISED.
EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS.

ORDINARY PHASE 7B CONTINUATION AND HARDEN-02: SUSPENDED / DOWNSTREAM until Product → AR-000 → Architecture → Domain → Roadmap → warranted Atlas reconciliation reaches the approved HARDEN-02 point. HARDEN-02 remains in the approved overall programme but is not the immediate next task while the targeted amendment programme is active.

DELIVERY ATLAS WORKING BASELINE: ATLAS-01 THROUGH ATLAS-11 COMPLETE AT CURRENT SCOPE; ATLAS-12 NOT_STARTED. Atlas remains derived, non-authoritative navigation.
```

The Foundation Readiness Audit is complete and passed with no blockers, material contradictions, unowned durable truths or unrouted blocking gates. The targeted Product amendment programme remains the current authority-stage routing surface; Stage 3A.1, Stage 3A.2 and Stage 3B classification are complete. Architecture Grill is next, pending independent review of the exact Stage 3B PR head.

FOUNDATION INTEGRITY PATCH COMPLETE. NO FURTHER FOUNDATION EXPANSION WITHOUT AN UPSTREAM CONTRADICTION.

This tracker update does not create the Communications JIT Domain Dossier, start Phase 7C, generate TOON prompts, perform Architectural Proof, create Vertical Slices or implement anything. The Identity & Access JIT Domain Dossier is complete / merged. Executable development remains stopped until the applicable Phase 7 and Development Entry Hard Stop requirements are satisfied.

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
# 12. Targeted Product Amendment Programme

This section tracks the governed Targeted Amendment → FP-001 Development Entry Readiness programme. Stage 1 working input: `archive/TARGETED_PRODUCT_AMENDMENT_GRILL_WORKING_v0.5.0.md` (non-authoritative historical evidence only).

## 12.1 Programme state

| Stage | Scope | Status |
|---|---|---|
| Stage 1 | Targeted Product Amendment Grill (four capability areas + cross-capability pressure test) | **COMPLETE** |
| Stage 2 | Governed Product Law amendment encoding approved Grill decisions | **COMPLETE** |
| Stage 3A.1 | Product-Law AR-000 delta analysis | **COMPLETE** — preserved as non-authoritative historical evidence in `archive/`; no longer active working analysis |
| Stage 3A.2 | Governed cumulative, append-only AR-000 amendment | **COMPLETE** — current successor is `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`; v1.0.0 is preserved in `archive/` |
| Stage 3B | Independent Architecture/Engineering classification | **COMPLETE** — non-authoritative classification artifact recorded; exact PR head requires independent review |
| Architecture Grill | Independent downstream Architecture classification | **NOT_STARTED / NEXT** |
| Engineering-Policy Grill | Independent downstream Engineering-policy classification | **NOT_STARTED** |
| Architecture amendment | Any later Architecture Law amendment | **NOT_STARTED** |
| Later | Architecture/Engineering Standards/Domain/Roadmap/Atlas/HARDEN-02/FP-001 reconciliation | **DOWNSTREAM / NOT CURRENT** — resumes only after the approved Product → AR-000 → Architecture → Domain → Roadmap → warranted Atlas sequence reaches the HARDEN-02 point |

**Baseline reviewed for Stage 1:** `main` at `ad71191b17b297ac9dc683c18141e1c546fa9850`.
**Stage 3A.1 analysis baseline:** `main` at `0aa6b5990e333988c3617a43db495d6fc6c85cd4`.
**Stage 3A.2 amendment baseline:** `main` at `c1a66ee5a8a3cd27cd66e2d698267810ac0330c0`.

## 12.2 Stage 2 amendment scope (current)

The Stage 2 Product amendment encodes exactly four Product-level areas plus cross-capability rules:

1. Research & Feedback (`DEC-294`, `00_PLATFORM_v1.3.0.md` §21M);
2. Voting / Balloting / Competitions (`DEC-295`, §21N);
3. Interactive Tools / Calculators / Decision Aids (`DEC-296`, §21O);
4. Platform Member Reference (`DEC-297`, §21P);
5. Cross-capability interaction rules (`DEC-298`, §21Q).

Explicitly **not** in Stage 2 scope: ARQ/ARC creation, Architecture amendment, Domain Map amendment, Roadmap amendment, new Domains, new Feature Packs, FP-001 contract/dossier changes, HARDEN-02 execution, or implementation.

## 12.3 Stage 3A.2 completion and Stage 3B handoff

Stage 3A.2 is complete in `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`. The successor preserves all 417 v1.0.0 ARQs, appends the approved v1.3.0 Product-Law provenance and additive coverage, creates no Architecture decisions, and records the complete Stage 3A.1 analysis as historical evidence at `archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md`.

Stage 3B is complete as classification only in `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md`. It creates no Product Law, ARQ, Architecture Law, Engineering Standard, Domain, Roadmap, Feature Pack or implementation artifact. Its independent input stream contributes zero current Architecture Grill propositions after authority-placement correction. Architecture Grill remains `NOT_STARTED / NEXT` because the separate governed Product-derived AR-000 v1.1.0 input stream from Stage 3A.2 still requires downstream Architecture closure. Its exact PR head requires independent human/reviewer certification before the next stage is treated as approved.

After the exact Stage 3B PR head is reported, work must **STOP** pending independent review of that head. Do not merge it, begin the Architecture Grill, begin the Engineering-Policy Grill, amend Architecture Law, create ARC identifiers, amend the Domain Map or Roadmap, create Domains or Feature Packs, reconcile the Delivery Atlas, execute HARDEN-02, modify FP-001 artifacts, or implement any capability before the next separately authorised stage.

## 12.4 North Star / MVP note

`PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` is **unchanged**. The approved capabilities are mature-platform additions and cross-cutting Product rules; they do not alter MVP launch scope, launch catalogue, core loop or Phase 7/8 entry conditions. Platform Member Reference affects later FP-001 reconciliation because individual Account creation is already in FP-001, but that does not by itself require North Star/MVP amendment at Stage 2.
