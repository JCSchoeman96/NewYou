# 02_OPEN_WORK_v1.2.42.md

- **Document status:** HARDEN-02 CONTRACT CERTIFICATION BLOCKER / EXECUTION PREPARATION SUCCESSOR v1.2.42
- **Authoritative for:** Remaining unresolved planning questions, expert/vendor/architecture/operations gates, post-grilling deliverables, planning and delivery sequencing, and planning/development stop conditions
- **Not authoritative for:** Locked product decisions, platform truth, implementation details, Ash Resources, schemas, or legal and clinical conclusions
- **Related documents:**
  - `00_PLATFORM_v1.3.0.md`
  - `01_DECISIONS_v1.3.0.md`
  - `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
  - `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`
  - `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`
  - `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`
  - `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md`
  - `working/TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md`
  - `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md`
  - `working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md`
  - `working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md`
  - `working/DELIVERY_ATLAS_WORKING_v0.2.1.md`
  - `working/HARDEN-02_CONTRACT_WORKING_v0.2.0.md`
  - `03_ARCHITECTURE_v1.1.0.md`
  - `04_DOMAIN_MAP_v1.1.0.md`
  - `05_ROADMAP_v1.1.0.md`
  - `archive/05_ROADMAP_WORKING_v0.1.0.md`
  - `reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md`
  - `archive/FOUNDATION_READINESS_AUDIT_v1.0.0.md`
- **Last updated:** 2026-09-23
- **Current planning position:** The **Targeted Product Amendment Programme** through Domain amendment, Roadmap amendment and Atlas reconciliation remains **COMPLETE**. Domain count is **20**. Feature Pack count remains **17**. Current Roadmap remains `05_ROADMAP_v1.1.0.md`. Current Delivery Atlas is the routing-only successor `working/DELIVERY_ATLAS_WORKING_v0.2.1.md`. PR #37 head `b1b0431152481006bbc1eff33cc9844a1b8c1ad5` was merged unchanged into `main` `2599638334b761ddef8e5568d0a38c3207eef722`, and post-merge Foundation Integrity run `35875423226` passed. However, the contract requires independent pre-merge review plus independent post-merge certification before execution becomes authorised, and no such certification is repository-verifiable from PR #37 reviews/comments. Therefore the contract remains **OPEN / PENDING INDEPENDENT CERTIFICATION** and HARDEN-02 execution remains **NOT STARTED / NOT AUTHORISED**. This PR may prepare deterministic proof tooling and correct stale routing, but it must not claim execution completion or advance Engineering Standards. `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`, `FP001_RECONCILIATION_REQUIRED`, Communications, Phase 7C, proof classification and executable development remain downstream / blocked. **PLANNING FOUNDATION: READY**. **EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS.** FP-001 artifacts are not amended here.

---


## Historical changelog

- Planning-state SemVer transition: `v1.2.41 → v1.2.42`.
- Records verified merge/CI facts for PR #37 but also the unresolved certification blocker: the required independent pre-merge review and independent post-merge certification are not repository-verifiable, so execution entry remains closed.
- Records that the predecessor routing expected `HARDEN-02_EXECUTION_REQUIRED` only after contract certification; this successor now fails closed because that independent certification evidence is not repository-verifiable.
- Adds machine-checkable HARDEN-02 execution evidence for I-01…I-13, including the full H02-3R downstream route through remaining Phase 7B/7C, proof classification and Phase 8 entry gates.
- Advances the derived Delivery Atlas `v0.2.0 → v0.2.1` only to correct stale current Open Work routing; Atlas remains derived/non-authoritative and does not become `ATLAS-12`.
- Engineering Standards Authority Promotion remains downstream / not started; no Engineering Standards authority module is created or frozen.
- Preserves the predecessor at `archive/02_OPEN_WORK_v1.2.41.md`.
- Does not amend North Star/MVP, Product Law, Decision Register, AR-000, Architecture Law, Architecture synthesis, Reference Flows, Domain Map, Roadmap, Operating Model, Frontend Experience System or FP-001, and does not authorise application implementation.
- Planning-state SemVer transition: `v1.2.40 → v1.2.41`.
- Records the accepted 2026-09-23 HARDEN-02 routing refinement in `working/HARDEN-02_CONTRACT_WORKING_v0.2.0.md`; preserves `v0.1.0` as historical working evidence.
- Preserves the historical v1.2.41 contingent route in which `HARDEN-02_EXECUTION_REQUIRED` could become NEXT only after the certified contract head was merged unchanged and resulting `main` independently post-merge certified; that prerequisite is not currently evidenced.
- Records `H02-3R`: certified HARDEN-02 execution routes NEXT to `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`; H02-3 remains historical evidence of the earlier immediate FP-001 route and is superseded only on that routing point.
- Routes narrow `FP001_RECONCILIATION_REQUIRED` only after Engineering Standards Authority Promotion is complete / certified; Communications remains after FP-001 reconciliation.
- Engineering Standards authority promotion is routed but **NOT STARTED** here; this successor creates no Engineering Standards authority module and does not freeze or execute standards.
- Preserves `FP001_RECONCILIATION_REQUIRED` without amending FP-001 Skeleton, Gate Manifest, Identity dossier, Communications dossier, Final Contract or proof classification.
- Preserves the predecessor at `archive/02_OPEN_WORK_v1.2.40.md`.
- Does not amend North Star/MVP, Product Law, Decision Register, AR-000, Architecture Law, Architecture synthesis, Reference Flows, Domain Map, Roadmap, Operating Model, Frontend Experience System or FP-001, and does not authorise implementation.

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

**Phase 3 completion evidence:** predecessor preserved in `archive/` and recorded by the authority manifest; current targeted Architecture-amendment successor `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`.

**Closure result:**

```text
12/12 flows complete
1 PASS
11 PASS_WITH_DOWNSTREAM_GATES
0 FAIL_ARCHITECTURE_GAP
0 BLOCKED_CONTRADICTION
0 Product Law amendments
0 ARQ amendments
7 mandatory targeted flow reviews incorporated in the Architecture-amendment successor
FLOW-09 conditional review not triggered
```

Exit condition — **MET**:

- no required flow depends on an undocumented architectural mechanism;
- no flow creates contradictory architecture rules;
- downstream expert/provider/JIT/proof gates are explicit and remain in their correct authority layer.

## Phase 4 — COMPLETE: `03_ARCHITECTURE_v1.1.0.md` Architecture-amendment successor

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

**Phase 4 completion evidence:** predecessor `archive/03_ARCHITECTURE_v1.0.0.md`; current frozen successor `03_ARCHITECTURE_v1.1.0.md`, supported by `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`.

**Closure result:** PASS — 332/332 ARC thematic coverage; 433/433 ARQ coverage; 16/16 Stage 4A Product-derived ARQs closed; five new ARC decisions; mandatory targeted FLOW-01/02/03/06/08/10/11 review complete; FLOW-09 conditional and not triggered; 0 real ARC conflicts; no Domain ownership assigned; implementation remains blocked.

## Phase 5 — COMPLETE: Domain Map + Domain Architecture Profiles

Historical Phase-5 freeze: `archive/04_DOMAIN_MAP_v1.0.0.md` (18 Domains). Current Domain Law successor: `04_DOMAIN_MAP_v1.1.0.md` (20 Domains).

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

**Phase 5 completion evidence:** historical freeze `archive/04_DOMAIN_MAP_v1.0.0.md`; current successor `04_DOMAIN_MAP_v1.1.0.md`.

**Historical Phase-5 closure:** PASS — 18 approved domains; 48/48 ownership-matrix truths; 18/18 lightweight profiles.

**Current Domain Law closure:** PASS — 20 approved domains; Domain 19 Research & Feedback; Domain 20 Voting & Balloting; PMR owned by Identity & Access; Interactive Tools are not a Domain; 0 shared-write ambiguities; 0 circular authoritative control dependencies; no new Architecture mechanism required.

## Phase 6 — COMPLETE: `05_ROADMAP_v1.1.0.md` Roadmap-amendment successor

Historical Phase-6 freeze:

```text
archive/05_ROADMAP_WORKING_v0.1.0.md  — preserved historical planning evidence
archive/05_ROADMAP_v1.0.0.md          — preserved frozen Roadmap predecessor
05_ROADMAP_v1.1.0.md                  — FROZEN / AMENDED ROADMAP (current)
```

The Roadmap works backward from the approved mature platform, defines the smallest safe commercial path, sequences outcome-oriented Feature Packs, preserves all approved expansion paths, schedules gates at the first point required, exposes anticipated proof needs and defers implementation-grade detail to Phase 7.

**Historical Phase 6 completion:** PASS on the v1.0.0 freeze.

**Current Roadmap amendment:** PASS — additive v1.1.0 successor after accepted Roadmap Sequencing Grill decisions; Feature Pack count remains 17; PMR REQUIRED in FP-001; Research/Voting FUTURE-GATED / FEATURE-PACK-UNASSIGNED; Interactive Tools purpose-distributed; no upstream contradiction.

**Current programme blocker:** HARDEN-02 contract certification remains OPEN / PENDING INDEPENDENT CERTIFICATION. PR #37 merge and CI are verified, but the required independent certification evidence is not repository-verifiable, so execution remains NOT STARTED / NOT AUTHORISED. Only after that contract gate is genuinely closed may HARDEN-02 execution become current. The conditional downstream route after later certified execution remains Engineering Standards Authority Promotion → narrow `FP001_RECONCILIATION_REQUIRED` → Communications JIT Domain Dossier → remaining required/conditional Phase 7B → Phase 7C → proof classification → Phase 8 only when Development Entry Hard Stop conditions pass.

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
6. Stage 3B independently classified Architecture/Engineering inputs before Architecture Grill; Stage 4A Architecture Grill, Stage 4B Engineering-Policy Grill and the governed Architecture amendment are complete for the Product-derived AR-000 stream; downstream work must not invent product policy.

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
CURRENT AUTHORITY-STAGE PROGRAMME: TARGETED PRODUCT AMENDMENT → ROADMAP AMENDMENT → ATLAS RECONCILIATION COMPLETE; HARDEN-02 CONTRACT OPEN / PENDING INDEPENDENT CERTIFICATION; HARDEN-02 EXECUTION NOT STARTED
STAGE 1 — TARGETED PRODUCT AMENDMENT GRILL: COMPLETE
STAGE 2 — GOVERNED PRODUCT LAW AMENDMENT: COMPLETE
STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE
STAGE 3A.2 — GOVERNED AR-000 AMENDMENT: COMPLETE
STAGE 3B — INDEPENDENT ARCHITECTURE/ENGINEERING CLASSIFICATION: COMPLETE
ARCHITECTURE GRILL: COMPLETE
ENGINEERING-POLICY GRILL: COMPLETE
ARCHITECTURE AMENDMENT: COMPLETE — Architecture Law v0.36.0 / synthesis v1.1.0 / targeted flows v0.3.0
DOMAIN PRESSURE TEST: COMPLETE
DOMAIN AMENDMENT: COMPLETE — Domain Map v1.1.0 / 20 Domains / Domain 19 Research & Feedback / Domain 20 Voting & Balloting
ROADMAP SEQUENCING GRILL: COMPLETE
ROADMAP AMENDMENT: COMPLETE — current Roadmap `05_ROADMAP_v1.1.0.md`; predecessor `archive/05_ROADMAP_v1.0.0.md`; Feature Packs 17
ATLAS RECONCILIATION: COMPLETE — current routing-only Atlas successor `working/DELIVERY_ATLAS_WORKING_v0.2.1.md`; predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`; original reconciliation baseline `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`; DERIVED / NON-AUTHORITATIVE; not ATLAS-12
ENGINEERING STANDARDS AUTHORITY PROMOTION: DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED
HARDEN-02 CONTRACT: OPEN / PENDING INDEPENDENT CERTIFICATION — `working/HARDEN-02_CONTRACT_WORKING_v0.2.0.md`; PR #37 head `b1b0431152481006bbc1eff33cc9844a1b8c1ad5` merged unchanged into `main` `2599638334b761ddef8e5568d0a38c3207eef722`; run `35875423226` PASS; required independent certification evidence is not repository-verifiable
HARDEN-02 EXECUTION: NOT STARTED / NOT AUTHORISED — contract certification evidence must close first
FP001_RECONCILIATION_REQUIRED — DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION
COMMUNICATIONS JIT DOMAIN DOSSIER — DOWNSTREAM AFTER NARROW FP-001 RECONCILIATION

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

ORDINARY PHASE 7B CONTINUATION REMAINS SUSPENDED / DOWNSTREAM. HARDEN-02 contract v0.2.0 remains OPEN / PENDING INDEPENDENT CERTIFICATION because the required independent certification evidence is not repository-verifiable. HARDEN-02 execution is NOT STARTED / NOT AUTHORISED. This draft branch may prepare proof tooling, but only a genuinely certified contract state may make execution current. Engineering Standards Authority Promotion remains after certified HARDEN-02 execution; narrow FP-001 PMR reconciliation remains after certified standards promotion, followed by Communications.

DELIVERY ATLAS WORKING BASELINE: ATLAS-01 THROUGH ATLAS-11 COMPLETE AT CURRENT SCOPE; ATLAS RECONCILIATION COMPLETE AT `working/DELIVERY_ATLAS_WORKING_v0.2.1.md`; ATLAS-12 NOT_STARTED (undefined view-population contract; reconciliation is not ATLAS-12). Atlas remains derived, non-authoritative navigation.
HARDEN-02 ACCEPTED SCOPE: H02-1 governance/structural only; H02-2 Store/CER excluded; H02-3 remains historical for FP-001 reconciliation before Communications; H02-3R inserts Engineering Standards Authority Promotion immediately after certified HARDEN-02 execution.
```

The Foundation Readiness Audit remains complete with no upstream blocker reopened. The targeted Product amendment programme has completed Product → AR-000 → Architecture → Domain → Roadmap → warranted Atlas reconciliation. HARDEN-02 contract merge and CI are verified, but the contract's required independent certification evidence is not repository-verifiable. HARDEN-02 execution therefore remains NOT STARTED / NOT AUTHORISED. Do not promote Engineering Standards, reconcile FP-001, start Communications or implement until that contract certification gate is genuinely closed and then HARDEN-02 execution is separately completed/certified.

FOUNDATION INTEGRITY PATCH COMPLETE. NO FURTHER FOUNDATION EXPANSION WITHOUT AN UPSTREAM CONTRADICTION.

This tracker successor prepares bounded HARDEN-02 proof tooling and machine-checkable governance checks while execution remains NOT STARTED / NOT AUTHORISED. It does not self-certify the contract, execute HARDEN-02, execute or freeze Engineering Standards Authority Promotion, create the Communications JIT Domain Dossier, perform FP-001 reconciliation, start Phase 7C, generate TOON prompts, perform Architectural Proof, create Vertical Slices or implement application behaviour. The Identity & Access JIT Domain Dossier remains complete / merged and FP-001 artifacts remain unreconciled for PMR. Executable development remains stopped until the applicable Phase 7 and Development Entry Hard Stop requirements are satisfied.

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
| Stage 3B | Independent Architecture/Engineering classification | **COMPLETE** — non-authoritative classification artifact recorded |
| Architecture Grill | Product-derived Architecture Grill for AR-000 v1.1.0 | **COMPLETE** — non-authoritative Grill evidence recorded |
| Engineering-Policy Grill | Independent downstream Engineering-policy classification | **COMPLETE** — non-authoritative Grill evidence recorded; exact PR head requires independent review |
| Architecture amendment | Product-derived Stage 4A Architecture Law/synthesis/targeted-flow amendment | **COMPLETE** — current successors are `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`, `03_ARCHITECTURE_v1.1.0.md` and `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`; predecessors are preserved in `archive/` |
| Domain pressure test | Targeted Domain ownership pressure test after Architecture amendment | **COMPLETE** — non-authoritative evidence in `working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md` |
| Domain amendment | Additive Domain Law successor implementing accepted human Domain decisions | **COMPLETE** — current successor is `04_DOMAIN_MAP_v1.1.0.md`; predecessor is `archive/04_DOMAIN_MAP_v1.0.0.md`; 20 Domains |
| Roadmap Sequencing Grill | Sequencing decisions for PMR / Research / Voting / Interactive Tools | **COMPLETE** — non-authoritative evidence in `working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md` |
| Roadmap amendment | Additive Roadmap successor implementing accepted human Roadmap decisions | **COMPLETE** — current successor is `05_ROADMAP_v1.1.0.md`; predecessor is `archive/05_ROADMAP_v1.0.0.md`; Feature Packs remain 17 |
| Current / later | HARDEN-02 contract certification / execution / Engineering Standards Authority Promotion / FP-001 reconciliation | **CURRENT BLOCKER:** contract remains OPEN / PENDING INDEPENDENT CERTIFICATION because independent certification evidence is not repository-verifiable; HARDEN-02 execution is NOT STARTED / NOT AUTHORISED. **DOWNSTREAM:** after genuine contract certification, HARDEN-02 execution; after certified execution, Engineering Standards Authority Promotion; after certified standards promotion, FP-001 reconciliation; then Communications. FP-001 remains unamended. |

**Baseline reviewed for Stage 1:** `main` at `ad71191b17b297ac9dc683c18141e1c546fa9850`.
**Stage 3A.1 analysis baseline:** `main` at `0aa6b5990e333988c3617a43db495d6fc6c85cd4`.
**Stage 3A.2 amendment baseline:** `main` at `c1a66ee5a8a3cd27cd66e2d698267810ac0330c0`.
**Stage 3B classification baseline:** `main` at `e0e9680f2f121512a6bd582299755d06e5094aff` (merged as `a7cd4279cfddc67bb816f512231c3f7bfc8482c2`).
**Stage 4A Architecture Grill baseline:** `main` at `a7cd4279cfddc67bb816f512231c3f7bfc8482c2`.
**Stage 4B Engineering-Policy Grill baseline:** `main` at `ccf94a7d78174f01e56bae1ba7f2bb19ccb216ae`.
**Architecture-amendment baseline:** `main` at `ccf94a7d78174f01e56bae1ba7f2bb19ccb216ae`.
**Domain-amendment baseline:** `main` at `f5170caeb09dcffe80c20fbc7d251c854a422a66`.
**Roadmap-amendment baseline:** `main` at `522eab3d5efd367044f2bb0459730b200523071f`.

## 12.2 Stage 2 amendment scope (current)

The Stage 2 Product amendment encodes exactly four Product-level areas plus cross-capability rules:

1. Research & Feedback (`DEC-294`, `00_PLATFORM_v1.3.0.md` §21M);
2. Voting / Balloting / Competitions (`DEC-295`, §21N);
3. Interactive Tools / Calculators / Decision Aids (`DEC-296`, §21O);
4. Platform Member Reference (`DEC-297`, §21P);
5. Cross-capability interaction rules (`DEC-298`, §21Q).

Explicitly **not** in Stage 2 scope: ARQ/ARC creation, Architecture amendment, Domain Map amendment, Roadmap amendment, new Domains, new Feature Packs, FP-001 contract/dossier changes, HARDEN-02 execution, or implementation.

## 12.3 Stage 4B completion and Architecture amendment handoff

Stage 3A.2 remains complete in `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`. Stage 3B remains complete as classification only in `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md`; its independent Architecture queue remains zero. Stage 4A remains complete as non-authoritative Architecture Grill evidence in `working/TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md`.

Stage 4B is complete as non-authoritative Engineering-Policy Grill evidence in `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md`. It records explicit human decisions for the seven Stage 3B Engineering-Policy propositions, creates no Product Law, ARQ, ARC, Engineering Standard, Domain, Roadmap, Feature Pack, dependency, CI or implementation artifact, and remains active working input for later Engineering Standards. The governed Architecture amendment is complete in the cumulative law successor `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`, frozen synthesis successor `03_ARCHITECTURE_v1.1.0.md`, targeted flow successor `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md` and this Open Work successor. It closes exactly the 16 Product-derived ARQs, adds `ARC-328` through `ARC-332`, assigns no Domain owner and does not amend Product Law, the Decision Register or AR-000.

After the exact Architecture-amendment PR head is reported, work must **STOP** pending independent review of that head. Do not merge it, write Engineering Standards, begin Domain pressure testing/amendment, amend the Domain Map or Roadmap, create Domains or Feature Packs, reconcile the Delivery Atlas, execute HARDEN-02, modify FP-001 artifacts, or implement any capability before the next separately authorised stage.
## 12.4 North Star / MVP note

`PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` is **unchanged**. The approved capabilities are mature-platform additions and cross-cutting Product rules; they do not alter MVP launch scope, launch catalogue, core loop or Phase 7/8 entry conditions. Platform Member Reference is now REQUIRED in Roadmap FP-001 sequencing meaning and still affects later FP-001 artifact reconciliation, but that does not by itself require North Star/MVP amendment. Research, Voting and generic Interactive Tools remain outside MVP unless a later Product amendment says otherwise.

## 12.5 Domain pressure test and Domain amendment completion

The targeted Domain pressure test is complete as non-authoritative evidence in `working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md`. It does not itself create Domain Law.

The governed Domain amendment is complete in `04_DOMAIN_MAP_v1.1.0.md`. Predecessor `archive/04_DOMAIN_MAP_v1.0.0.md` is preserved byte-identically. Human decisions implemented:

- `DQ-1` ACCEPT — Domain 19 **Research & Feedback** owns the Research/feedback campaign, instrument/version, participant response, correction/withdrawal/de-link and staff-annotation lifecycle.
- `DQ-2` ACCEPT WITH NAMING REFINEMENT — Domain 20 **Voting & Balloting** owns governed vote rules, submission/integrity evidence, accepted tally, finalisation, official result and adjudication. Competitions are not a Domain.

Platform Member Reference is Identity & Access Account truth. Interactive Tools do not create a Domain. Content is not generic tool-calculation authority. Habits is not a generic persisted-tool-result bucket. Reward/entitlement remains Commerce/Entitlements. Analytics and Audit remain non-source authority.

`ROADMAP_REVIEW_REQUIRED`. `FP001_RECONCILIATION_REQUIRED`. Roadmap, Atlas, HARDEN-02, FP-001, Engineering Standards, JIT dossiers for Domains 19 and 20, Resource/schema design and implementation are not started here.

Domain amendment remains complete. Roadmap Sequencing Grill and Roadmap amendment are recorded in §12.6.


## 12.6 Roadmap Sequencing Grill and Roadmap amendment completion

The Roadmap Sequencing Grill is complete as non-authoritative evidence in `working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md`. It does not itself create Roadmap Law.

The governed Roadmap amendment is complete in `05_ROADMAP_v1.1.0.md`. Predecessor `archive/05_ROADMAP_v1.0.0.md` is preserved byte-identically. Human decisions implemented:

- `RQ-1` ACCEPT — Platform Member Reference is **REQUIRED within FP-001**; no PMR Feature Pack; encoding remains unfrozen; `FP001_RECONCILIATION_REQUIRED` remains for later narrow artifact reconciliation.
- `RQ-2` ACCEPT WITH REFINEMENT — Research & Feedback is mature **FUTURE-GATED / FEATURE-PACK-UNASSIGNED**; not MVP; not FP-005; not automatically FP-006/008/009; no Research Feature Pack now.
- `RQ-3` ACCEPT WITH REFINEMENT — Voting & Balloting is mature **FUTURE-GATED / FEATURE-PACK-UNASSIGNED**; not required by FP-008 or FP-013; no Voting/Competitions Feature Pack now.
- `RQ-4` ACCEPT WITH REFINEMENT — Interactive Tools have no Feature Pack and no generic activation point; purpose-distributed only.

Feature Pack count remains **17**. Atlas reconciliation remains **COMPLETE**; routing-only Atlas successor v0.2.1 corrects stale current-source navigation without changing authority. HARDEN-02 contract v0.2.0 remains OPEN / PENDING INDEPENDENT CERTIFICATION: merge/CI facts are verified, but independent certification evidence is not repository-verifiable. HARDEN-02 execution remains NOT STARTED / NOT AUTHORISED. Engineering Standards Authority Promotion, FP-001 reconciliation, Communications, JIT dossiers for Domains 19 and 20, Resource/schema design and application implementation remain downstream / not started here.

The HARDEN-02 contract entry gate is **not evidenced as satisfied**. Work must **STOP** at contract certification. Do not treat this draft execution preparation as authorisation. Obtain a genuinely independent certification record for the contract lifecycle, then re-baseline execution from the certified repository state. Do not begin Engineering Standards Authority Promotion, modify FP-001 artifacts, create the Communications dossier, create JIT dossiers for Research & Feedback or Voting & Balloting, or implement any capability from this stage.

## 12.7 — Delivery Atlas reconciliation

**Status:** COMPLETE as derived / non-authoritative navigation; current routing-only successor `working/DELIVERY_ATLAS_WORKING_v0.2.1.md` preserves `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md` unchanged. Original reconciliation baseline remains `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`.

Atlas reconciliation remains complete as derived navigation. Atlas v0.2.1 is a routing-only HARDEN-02 execution patch correcting stale references that described archived Open Work as current. It creates no Product, Architecture, Domain or Roadmap law, does not amend FP-001 artifacts, does not execute Engineering Standards Authority Promotion and does not authorise application implementation.

**Current:** HARDEN-02 contract remains `OPEN / PENDING INDEPENDENT CERTIFICATION`; execution is `NOT STARTED / NOT AUTHORISED`. **Conditional downstream route only after genuine contract certification and later certified execution:** `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED` → certified standards promotion → narrow `FP001_RECONCILIATION_REQUIRED` → Communications → remaining Phase 7B/7C → proof classification → Phase 8 only when Development Entry Hard Stop conditions pass.

## 12.8 — HARDEN-02 contract and execution

**Status:** CONTRACT OPEN / PENDING INDEPENDENT CERTIFICATION; HARDEN-02 EXECUTION NOT STARTED / NOT AUTHORISED. Contract: `working/HARDEN-02_CONTRACT_WORKING_v0.2.0.md`. PR #37 head `b1b0431152481006bbc1eff33cc9844a1b8c1ad5` and merge baseline `main` `2599638334b761ddef8e5568d0a38c3207eef722` are verified; post-merge Foundation Integrity run `35875423226` is PASS. The contract-required independent pre-merge review and independent post-merge certification are not repository-verifiable, so those facts do not authorise execution.

Accepted human decisions:

- `H02-1` — HARDEN-02 is bounded Phase-7 delivery-pipeline governance / structural hardening only; not Product/Roadmap/OQ/FP/HH/Store/Commerce hardening.
- `H02-2` — Store Blueprint / CER is explicitly out of scope and remains a parallel non-authoritative Pre-JIT/reuse stream.
- `H02-3` — Historical accepted route: certified HARDEN-02 execution completion routed NEXT to narrow `FP001_RECONCILIATION_REQUIRED`, then Communications. **SUPERSEDED IN PART** on 2026-09-23 only for the immediate post-HARDEN-02 NEXT stage.
- `H02-3R` — ACCEPTED 2026-09-23: certified HARDEN-02 execution completion routes NEXT to `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`; after that supporting-authority promotion is complete / certified, narrow `FP001_RECONCILIATION_REQUIRED` becomes NEXT, then Communications and remaining Phase-7B/7C work under ordinary gates.

This draft successor prepares HARDEN-02 proof tooling and routing corrections but does **not** execute HARDEN-02 because the contract certification gate is not repository-verifiably closed. It does not self-certify the contract, execute or freeze Engineering Standards Authority Promotion, reconcile FP-001, start Communications, or authorise application implementation.
