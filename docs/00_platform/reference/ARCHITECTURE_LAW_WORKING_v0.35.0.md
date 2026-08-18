# ARCHITECTURE_LAW_WORKING_v0.35.0.md

- **Document status:** ACTIVE WORKING ARCHITECTURE LAW REGISTER
- **Document version:** v0.35.0
- **Started:** 2026-08-16
- **Last updated:** 2026-08-17
- **Current workstream:** Phase 3 Reference Flow Pressure Tests COMPLETE; AR-009 remains COMPLETE
- **Current scope:** AR-001 through AR-009 COMPLETE; cumulative accepted Architecture Law is ARC-001 through ARC-327; ARC-327 amends ARC-326 proof timing only
- **Next planned scope:** Phase 4 — synthesize/review/freeze `03_ARCHITECTURE.md`; lightweight traceability-check the already-passed FLOW-01...FLOW-12 and rerun only materially affected flows
- **Governance mode:** CUMULATIVE / APPEND-ONLY ARCHITECTURE DECISIONS
- **Filename governance:** Every emitted version of this cumulative artifact includes its SemVer in the filename (for example `ARCHITECTURE_LAW_WORKING_v0.34.0.md`); later versions are emitted as new versioned files rather than relying on an unversioned filename.
- **Authority boundary:** This document records `ARC-nnn` decisions — HOW the platform will satisfy frozen `ARQ-*` requirements. It does not modify Product Law and does not assign final concrete business-domain ownership reserved for `04_DOMAIN_MAP.md`.

## Governing source set

- `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
- `00_PLATFORM_v1.2.1.md`
- `01_DECISIONS_v1.2.1.md`
- `../02_OPEN_WORK_v1.2.27.md`
- `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` — frozen AR-000 handoff

Architecture decisions must remain traceable to the frozen requirement set. A later change to an accepted ARC must preserve history through explicit amendment/supersession rather than silent rewriting.

---

# 1. AR-001 — System Shape & Runtime Topology

## 1.1 Round T1 — Core Runtime Shape

**Accepted answer set:** `T1.1 B, T1.2 B, T1.3 B, T1.4 B, T1.5 B, T1.6 B, T1.7 B, T1.8 B, T1.9 B`

**User deployment refinement:** Initial production starts with **one application instance** on either a South-African VPS or Railway. The launch does **not** require multiple application nodes, replicas, a BEAM cluster, or dedicated worker nodes. Architecture must nevertheless avoid single-node-only correctness assumptions so horizontal replication/clustering and worker separation can be introduced later without redefining business truth or application semantics.

**Provider evidence note — revalidate at provider-selection time:** As of 2026-08-16 Railway's official region list contains US West (California), US East (Virginia), EU West (Amsterdam), and Southeast Asia (Singapore); it does not list a South African deployment region. Railway's documentation states that services deploy as a single instance by default and can later add replicas. Therefore `Railway` must not be interpreted as `Railway South Africa`; if in-country compute is required, a South-African VPS/provider is the currently compatible path unless Railway's region catalogue changes.

---

## ARC-001 — Modular monolith is the default application/deployment shape

- **Decision source:** AR-001 T1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-001`, `ARQ-SYS-002`, `ARQ-SYS-005`, `ARQ-PERF-002`
- **Decision:** Build the platform as one deployable modular Elixir/Phoenix/Ash application with strong internal architectural boundaries. Do not create independent microservices merely because a future Domain Map contains multiple domains. Independent deployed services are introduced only through a later explicit ARC when evidence shows a durable independent scaling, failure-isolation, deployment-cadence, security, or technology boundary that cannot be handled cleanly inside the modular application.
- **Rationale:** Product Law requires one operating platform with shared capabilities and controlled product experiences while also requiring evolutionary scale-readiness without speculative complexity.
- **Rules:**
  1. Logical/module/domain boundaries do not automatically imply network/deployment boundaries.
  2. Cross-boundary interaction must still be explicit and policy-safe inside the application.
  3. The modular-monolith decision does not pre-name final business domains or Ash Resource boundaries.
  4. Service extraction requires evidence and an architecture amendment, not preference.
- **Failure behaviour:** OTP/process supervision may isolate runtime failures inside the application; independent process failure does not imply an independent network service is required.
- **Security/privacy:** Internal calls do not bypass authentication/authorisation/field-policy requirements merely because they are in one deployable application.
- **Performance/scaling:** Prefer vertical capacity, query/transaction correctness, bounded work, concurrency-safe design and horizontal-replica compatibility before service decomposition.
- **Enforcement/downstream:** AR-002 defines Phoenix/LiveView/Ash/code boundaries. `04_DOMAIN_MAP.md` decides final business ownership. AR-008 governs deployment mechanics.

## ARC-002 — Product spaces are logical activation/experience boundaries inside the common platform

- **Decision source:** AR-001 T1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-001`, `ARQ-SYS-002`, `ARQ-SYS-003`, `ARQ-SYS-004`
- **Decision:** A product space is a controlled logical experience and activation boundary inside the common platform, not a separate application, database, or generic tenant by default. Product spaces may vary approved brand, routes/navigation, onboarding, catalogue, programmes, content, eligibility and participant journeys while reusing shared platform capabilities.
- **Rationale:** This satisfies the locked one-platform/controlled-product-space model without turning every future audience or partner into a tenant or duplicate application.
- **Rules:**
  1. Only explicitly activated product spaces become customer-facing.
  2. Shared capabilities must not force all product experiences into one undifferentiated UI/policy surface.
  3. No `tenant_id` or tenant isolation model is introduced merely to represent a product space.
  4. Exact product-space data/configuration representation is deferred to AR-002/AR-004 and Domain Law.
- **Failure behaviour:** Failure or deactivation of one product experience must not redefine shared business truth for unrelated approved experiences.
- **Security/privacy:** Product-space visibility is not itself an authorisation mechanism; data/action policy remains independently enforced.
- **Performance/scaling:** Product-space separation must not require duplicated infrastructure merely for organisational convenience.
- **Enforcement/downstream:** AR-002 defines routing/application boundaries; AR-004 defines policy context; `04_DOMAIN_MAP.md` establishes concrete ownership.

## ARC-003 — Launch with one application instance; preserve later horizontal-replica compatibility

- **Decision source:** AR-001 T1.3 + explicit user refinement on 2026-08-16
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Source ARQs:** `ARQ-PERF-008`, `ARQ-PERF-141`, `ARQ-SYS-005`, `ARQ-PERF-161`
- **Decision:** The initial production topology uses **one running application instance / one BEAM node**. It may run on a South-African VPS or on Railway. Multiple application replicas/nodes are not a launch requirement. However, application correctness must not depend on permanent single-node locality; the same application must be capable of later horizontal replication behind a traffic layer without changing authoritative business semantics.
- **Rationale:** This minimises launch infrastructure and operating cost while preserving the frozen requirement that the platform be multi-node-correct when growth or availability eventually requires multiple nodes.
- **Rules:**
  1. Launch may be single-instance.
  2. No critical invariant may rely on process-local memory surviving restart or on there forever being exactly one node.
  3. Node-count-dependent optimisations are evidence-gated.
  4. Adding a second replica must not require redesign of payment, entitlement, safety, consent, capacity, plan, or other durable truth.
- **Failure behaviour:** At launch, loss of the sole instance can cause temporary service unavailability, but must not fabricate or corrupt committed durable truth. Recovery/restart must reconstruct operational state from durable authority and approved temporary-state contracts.
- **Security/privacy:** Restart/replacement must not weaken authentication, session, policy, consent, or audit boundaries.
- **Performance/scaling:** Vertical scaling is the initial capacity path. Horizontal application replicas are introduced when capacity or availability evidence justifies them.
- **Enforcement/downstream:** AR-003/005 define state/consistency contracts; AR-008 defines deployment/restart/health behaviour; AR-009 defines measurable scale triggers.

## ARC-004 — Load-balancer/session affinity is never a correctness dependency

- **Decision source:** AR-001 T1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-137`, `ARQ-PERF-138`, `ARQ-PERF-141`
- **Decision:** Sticky load-balancer affinity is not required for business correctness. A LiveView/socket process naturally lives on one node while connected, but reconnect after restart/node loss must be able to land on the same or another healthy node and reconstruct authorised UI state from authoritative/rebuildable sources.
- **Rationale:** This prevents ephemeral LiveView/process locality from becoming hidden business authority and preserves later replica mobility.
- **Rules:**
  1. Do not store irreplaceable business state only in a LiveView/socket/process.
  2. Reconnect paths re-authorise relevant actions/state.
  3. Affinity may be used later as a performance optimisation only if correctness remains affinity-independent.
- **Failure behaviour:** Socket/process/node loss may affect realtime freshness/session continuity, but cannot turn uncommitted state into committed truth or lose committed truth.
- **Security/privacy:** Reconnection must not inherit unauthorised state merely because a prior socket had access.
- **Performance/scaling:** Future replicas can receive reconnects without permanent user-to-node pinning.
- **Enforcement/downstream:** AR-002 defines LiveView state boundaries; AR-004 auth/policy; AR-005 PubSub/realtime semantics.

## ARC-005 — No BEAM cluster at launch; use same-region BEAM clustering when multi-node application topology is introduced

- **Decision source:** AR-001 T1.5 + explicit user refinement on 2026-08-16
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Source ARQs:** `ARQ-PERF-008`, `ARQ-PERF-134`, `ARQ-PERF-137`, `ARQ-PERF-138`, `ARQ-PERF-141`
- **Decision:** The single-instance launch does not run an application cluster because there is only one application node. When horizontal application replicas are introduced in the primary region, the preferred normal Elixir topology is a same-region distributed BEAM cluster for Phoenix distributed capabilities where justified. Phoenix PubSub remains the application-level realtime broadcast abstraction. Exact node discovery, topology strategy, and PubSub adapter are later Architecture/deployment decisions.
- **Rationale:** This preserves an idiomatic Elixir scale path without paying distributed-system complexity before a second application instance exists.
- **Rules:**
  1. No clustering dependency is required for initial launch.
  2. Code must not assume clustering is absent forever.
  3. Redis is not automatically required merely to provide PubSub between future nodes.
  4. Exact discovery library/provider integration is not locked here.
- **Failure behaviour:** Cluster partition/node disconnect must affect distributed observation/coordination before it affects durable business truth; authoritative operations require their own correctness contracts.
- **Security/privacy:** Future Erlang distribution must use appropriately protected private networking/authentication; no public distribution ports.
- **Performance/scaling:** Cluster introduction is tied to actual multi-node deployment. High-fan-out behaviour remains bounded/observable.
- **Enforcement/downstream:** AR-005 selects PubSub semantics/adapter details; AR-008 selects deployment/discovery/network implementation; AR-009 validates scale behaviour.

## ARC-006 — One release/codebase with combined launch role and separable web/worker roles later

- **Decision source:** AR-001 T1.6 + explicit user refinement on 2026-08-16
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Source ARQs:** `ARQ-PERF-106`, closed Performance async/queue requirements, `ARQ-ASYNC-001`
- **Decision:** Maintain one application codebase/release capable of web-facing and background-worker execution. The launch instance runs the required web and worker responsibilities together unless a specific workload proves otherwise. Later deployments may run dedicated web-focused and worker-focused instances from the same application release/configuration model without changing domain/application semantics.
- **Rationale:** This avoids premature service/process-fleet complexity while preserving a clean path for CPU/I/O/queue isolation when needed.
- **Rules:**
  1. Background work does not execute as unbounded request/LiveView work merely because roles are combined initially.
  2. Durable work remains durable/idempotent according to AR-005 law.
  3. Runtime role separation is an operational deployment choice, not a domain rewrite.
- **Failure behaviour:** Worker failure/backlog is observable and recoverable; web availability must not create false job completion, and later worker isolation must not alter business semantics.
- **Security/privacy:** Dedicated worker roles later receive only the secrets/network/data access needed for their approved work.
- **Performance/scaling:** Separate workers when queue latency, CPU, RAM, I/O or reliability evidence warrants it; do not require separation for the first pilot without evidence.
- **Enforcement/downstream:** AR-005 defines durable async mechanics; AR-008 defines runtime role/deployment configuration; AR-009 defines separation triggers.

## ARC-007 — Application compute is logically replaceable; durable authority is external to ephemeral process state

- **Decision source:** AR-001 T1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-042`, `ARQ-PERF-008`, `ARQ-PERF-137`, `ARQ-PERF-141`, `ARQ-STATE-001`
- **Decision:** Application process memory, LiveView state, ETS/cache state and ephemeral filesystem state are not durable business authority. Durable business state is committed through the approved shared persistence/storage boundary, with PostgreSQL as the default durable authority under the frozen ARQs. This is a **logical authority boundary**; AR-003/AR-008 may still decide whether some durable services are physically co-located on the initial VPS or managed separately, provided backup/recovery and correctness requirements are met.
- **Rationale:** The launch may be physically simple, but process/node restart must not redefine what is committed.
- **Rules:**
  1. Ephemeral state must be reconstructible, disposable, or governed temporary state with explicit lifecycle/reconciliation.
  2. Application restart cannot erase committed business truth.
  3. Redis/cache/local disk cannot silently become authority merely because it is faster or co-located.
- **Failure behaviour:** Loss of process-local state causes reconstruction/degradation, not silent durable-data loss or false success.
- **Security/privacy:** Sensitive durable data must follow approved storage/access boundaries regardless of physical co-location.
- **Performance/scaling:** Physical separation of state services may evolve with scale; semantic authority must remain stable.
- **Enforcement/downstream:** AR-003 decides persistence/cache/object-storage placement and contracts; AR-007 backup/deletion; AR-008 recovery/deployment.

## ARC-008 — One primary launch location; provider remains selectable between Railway and a South-African VPS

- **Decision source:** AR-001 T1.8 + explicit user hosting refinement on 2026-08-16
- **Status:** ACCEPTED_WITH_REFINEMENT
- **Source ARQs:** `ARQ-PERF-009`, `ARQ-PERF-161`, `ARQ-SYS-004`, `ARQ-OPS-002`
- **Decision:** Launch in one primary deployment location/region. Do not build active-active multi-region application infrastructure for MVP. The eligible launch hosting direction is Railway or a South-African VPS/provider; exact provider remains a downstream vendor/operations decision. If physical in-country compute/data locality is required, current Railway region availability does not satisfy that requirement and a South-African hosting option is required unless Railway later adds an appropriate region.
- **Rationale:** One-region operation matches the South-Africa-first launch and avoids premature multi-region complexity while preserving regionalisation and disaster-recovery paths.
- **Rules:**
  1. Region/provider choice must consider latency, data-location/legal requirements, managed-service availability, backup/DR, networking and operational support.
  2. Future market support must not require rewriting reusable application semantics.
  3. Disaster-recovery copies/controls must not share every meaningful failure domain with primary production.
  4. Railway region availability is evidence, not permanent Product Law, and must be rechecked when provider selection is made.
- **Failure behaviour:** Primary-location outage may cause launch service unavailability until recovery/failover; it may not justify unsafe split-brain or fabricated business state.
- **Security/privacy:** Provider/region selection must satisfy applicable privacy, encryption, secret-management and access-control requirements.
- **Performance/scaling:** Prefer proximity to primary users/state services; avoid cross-region chatty database topology before justified.
- **Enforcement/downstream:** AR-007 defines DR/backup; AR-008 selects provider/deployment/health/secret mechanisms; AR-009 validates latency/capacity.

## ARC-009 — Independent service extraction is evidence-gated and amendment-controlled

- **Decision source:** AR-001 T1.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-005`, `ARQ-PERF-002`, `ARQ-PERF-054`, `ARQ-PERF-106`
- **Decision:** A capability may become an independently deployed service only after measurable or structurally unavoidable evidence demonstrates a durable benefit such as independent scaling, fault isolation, deployment cadence, security boundary or technology/runtime requirement. An Ash/domain boundary, team boundary, or anticipated future scale is not sufficient by itself.
- **Rationale:** Preserve optionality without creating microservice operational cost or distributed-consistency problems before they are justified.
- **Rules:**
  1. Extraction requires an explicit ARC amendment/addition with evidence.
  2. Extracted services must preserve authoritative ownership, idempotency, audit and privacy semantics.
  3. Network boundaries are introduced deliberately with failure/retry/consistency contracts.
- **Failure behaviour:** Service extraction may not create silent partial-success or unowned cross-service truth.
- **Security/privacy:** New network boundaries require explicit authentication, authorisation, encryption and least-privilege review.
- **Performance/scaling:** Extraction must solve a demonstrated bottleneck/isolation requirement, not merely redistribute complexity.
- **Enforcement/downstream:** AR-002/003/005/008/009 provide evidence and mechanics; `04_DOMAIN_MAP.md` business ownership remains authoritative regardless of deployment boundary.

---

# 2. AR-001 T1 Consolidated Runtime Doctrine

The accepted AR-001 T1 architecture is:

```text
ONE MODULAR ELIXIR / PHOENIX / ASH PLATFORM
                    │
                    ├── controlled logical product spaces
                    │
                    ├── ONE application instance at launch
                    │      ├── web responsibilities
                    │      └── worker responsibilities
                    │
                    ├── durable authority outside ephemeral process state
                    │
                    └── scale path when evidence requires it
                           ├── vertical capacity first
                           ├── additional app replicas
                           ├── same-region BEAM cluster where justified
                           ├── optional web/worker pool separation
                           └── independent services only by explicit evidence
```

### Explicitly NOT required at launch

- multiple application nodes;
- a BEAM cluster;
- Kubernetes;
- microservices;
- dedicated worker servers;
- active-active multi-region;
- one deployment/database per product space;
- generic SaaS tenancy;
- sticky-load-balancer correctness;
- a specific node-discovery library;
- a specific orchestration platform.

### Explicitly required from the beginning

- no critical invariant depends on permanent single-node locality;
- ephemeral process/LiveView/cache state is not durable business truth;
- future replicas can be added without changing authoritative business semantics;
- future web/worker separation does not change domain semantics;
- one-platform/product-space separation remains clean;
- one-primary-location deployment does not block later regionalisation;
- provider choice remains reviewable and evidence-based.

---


## 1.2 Round T2 — Deployment & Infrastructure Topology

**Accepted answer set:** `T2.1 B, T2.2 B, T2.3 B, T2.4 B, T2.5 B, T2.6 B, T2.7 B, T2.8 B, T2.9 B`

**Launch-hosting context carried forward:** steady-state launch remains one application instance. Railway and a South-African VPS remain eligible hosting directions; exact provider selection remains downstream vendor/operations work. Current Railway region availability is evidence only and must be revalidated at provider-selection time.

---

## ARC-010 — One portable OCI image containing a production Elixir/Phoenix release is the deployment artifact

- **Decision source:** AR-001 T2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-005`, `ARQ-PERF-155`, `ARQ-PERF-158`, `ARQ-OPS-002`
- **Decision:** Build the production application as an Elixir/Phoenix Release packaged in an OCI-compatible container image. The same application artifact must be deployable to Railway or a suitable VPS/container runtime without provider-specific business logic or a separately maintained application packaging model.
- **Rationale:** A portable immutable artifact reduces provider lock-in, keeps launch simple, and preserves later movement between providers/hosts without redefining application semantics.
- **Rules:**
  1. Provider-specific deployment metadata may wrap the common image but may not become application/domain authority.
  2. Production dependencies required inside the application image are built deterministically; environment-specific configuration is injected at runtime under ARC-017.
  3. Do not maintain divergent Railway and VPS application builds unless later evidence proves a real need.
  4. Image/release construction must remain compatible with safe adjacent-version deployment and rollback/forward-recovery requirements.
- **Failure behaviour:** A failed image build/deploy does not mutate durable business truth; unsuccessful releases must be rejectable before traffic cutover or handled by governed recovery.
- **Security/privacy:** Images must not contain production secrets or participant data. Dependency/image provenance and patching become AR-008 enforcement concerns.
- **Performance/scaling:** The image must support the combined launch role and later web/worker or multi-replica roles without recompiling domain semantics.
- **Enforcement/downstream:** AR-008 defines CI/CD, image registry, host/runtime and rollout mechanics. AR-002 keeps code boundaries provider-neutral.

## ARC-011 — Cloudflare is the common public edge; origin hosting remains replaceable

- **Decision source:** AR-001 T2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-SEC-001`, `ARQ-AN-213`, `ARQ-AN-214`, `ARQ-CONTENT-005`
- **Decision:** Use Cloudflare as the common public DNS/edge boundary for the customer-facing platform where supported, routing to the selected Railway or VPS origin. Cloudflare may provide approved edge security, rate/bot controls, TLS termination/origin protection and caching/CDN behaviour, but Phoenix/Ash/platform state remains authoritative for application/business decisions.
- **Rationale:** One public-edge model gives consistent routing/security/cache posture across hosting providers while preserving origin portability and the already locked Cloudflare direction.
- **Rules:**
  1. Cloudflare edge decisions may reject/throttle/cache only within approved security/cache contracts.
  2. Edge caching must never expose private/personalised/paid data or violate experiment variant isolation/canonical-URL rules.
  3. Exact Cloudflare rules, cache keys, WAF/bot settings and origin configuration remain AR-006/008/JIT implementation detail.
  4. Internal service-to-service traffic does not need to traverse Cloudflare unless explicitly justified.
- **Failure behaviour:** Edge degradation may affect reachability/cache/security convenience, but may not fabricate payment, entitlement, safety, consent or other business truth. Origin-bypass/emergency behaviour must be separately governed if ever required.
- **Security/privacy:** Origin exposure should be minimised; sensitive data must not be placed in public cache keys, logs or edge-readable payloads without an approved purpose.
- **Performance/scaling:** Public static/cacheable content may benefit from edge delivery; dynamic authenticated business flows remain origin-governed.
- **Enforcement/downstream:** AR-006 defines content/media/cache eligibility; AR-008 defines ingress/origin/network controls; AR-009 validates edge/origin load behaviour.

## ARC-012 — PostgreSQL is a logically independent state service even when physically co-located at launch

- **Decision source:** AR-001 T2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-042`, `ARQ-PERF-075`, `ARQ-STATE-001`, `ARQ-OPS-002`
- **Decision:** PostgreSQL is a logically independent durable state service from the application runtime. On Railway it may be a separate managed/service deployment. On a single VPS it may initially run on the same physical host as the application when operationally acceptable, but it remains separately configured, backed up, monitored and replaceable/movable without redefining business authority.
- **Rationale:** This preserves a low-cost single-VPS launch option without making database lifecycle subordinate to the application container or preventing later database separation/managed hosting.
- **Rules:**
  1. Never embed PostgreSQL inside the application container/image.
  2. Application restarts/deploys do not imply database lifecycle/reinitialisation.
  3. Co-location is a physical deployment optimisation, not a semantic coupling.
  4. Backup/restore, storage durability, connection limits and upgrade policy remain independently governed.
- **Failure behaviour:** Application failure must not corrupt/recreate the database; database unavailability causes explicit degraded/refused business behaviour rather than guessed truth.
- **Security/privacy:** Database exposure is private/restricted; credentials are runtime secrets; local co-location does not justify broad host/user access.
- **Performance/scaling:** Co-location can minimise latency initially; PostgreSQL may later move to dedicated/managed capacity without changing domain semantics.
- **Enforcement/downstream:** AR-003 defines database authority/pooling/storage contracts; AR-007 backup/restore; AR-008 host/service lifecycle.

## ARC-013 — Redis is optional shared acceleration/coordination infrastructure, never general business authority

- **Decision source:** AR-001 T2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-042`, `ARQ-PERF-043`, `ARQ-SEC-001`, closed Performance cache/velocity requirements
- **Decision:** Redis is an approved but optional infrastructure capability for explicitly justified cache, velocity/rate-control, temporary coordination or similar workloads. It may be deployed on the launch VPS or as a provider service when an approved requirement needs it. It is not mandatory merely because it is available and may not become default durable business authority.
- **Rationale:** Some frozen requirements anticipate distributed/high-velocity controls, while the authority doctrine requires evidence before secondary acceleration.
- **Rules:**
  1. Each Redis use has an explicit purpose, authority/freshness/lifecycle/failure contract.
  2. PostgreSQL-only remains valid where it safely meets the workload.
  3. Redis loss/flush/restart must be survivable according to the workload's declared contract.
  4. Exact key formats, structures, TTLs and topology remain AR-003/004/005/009/JIT decisions.
- **Failure behaviour:** Redis failure degrades/refuses the dependent acceleration/coordination path according to its contract; it cannot silently convert stale/absent cache state into authoritative truth.
- **Security/privacy:** Redis remains privately networked/authenticated; sensitive payload duplication is minimised and purpose-bound.
- **Performance/scaling:** Redis may later move from co-located to dedicated/managed topology without changing domain truth.
- **Enforcement/downstream:** AR-003 decides data-temperature/cache contracts; AR-004 abuse/security usage; AR-005 temporary coordination; AR-009 scale triggers.

## ARC-014 — Durable uploads/media use external object storage; application filesystem is temporary only

- **Decision source:** AR-001 T2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-SEC-002`, `ARQ-CONTENT-006`, `ARQ-OPS-002`
- **Decision:** Durable user uploads, protected files and governed media are stored in approved external object storage from the beginning rather than relying on the application host/container filesystem as permanent storage. Local/container disk may be used only for bounded temporary processing under explicit cleanup/security rules.
- **Rationale:** This preserves provider/instance replaceability, supports CDN/protected delivery, and avoids hidden persistence tied to one Railway container or VPS disk layout.
- **Rules:**
  1. Uploads remain restricted/quarantined until required validation/scanning gates pass.
  2. Protected delivery remains entitlement/access checked with short-lived mechanisms where required.
  3. Temporary local files are bounded, cleaned and never assumed durable.
  4. Exact object-storage vendor, bucket/key layout and lifecycle policy remain AR-003/006/007 decisions.
- **Failure behaviour:** Object-storage/provider failure causes explicit upload/download/media degradation; application local disk is not an undocumented fallback durable store.
- **Security/privacy:** Private objects are non-public by default; access, encryption, retention and deletion propagate across derivatives/copies.
- **Performance/scaling:** Object delivery can scale independently from application compute and can use approved CDN paths for public media.
- **Enforcement/downstream:** AR-003 defines storage authority/layout classes; AR-006 media delivery; AR-007 deletion/retention; AR-008 provider operations.

## ARC-015 — One steady-state app instance may use temporary adjacent-version overlap for safe deployment

- **Decision source:** AR-001 T2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-155`, `ARQ-PERF-157`, `ARQ-PERF-158`, `ARQ-PERF-154`
- **Decision:** Steady-state launch production remains one application instance, but a deployment may temporarily run old and new application versions concurrently or sequentially behind a controlled cutover so the candidate version can complete startup/readiness checks before receiving intended traffic. The prior version is drained/stopped after safe cutover. Permanent two-node operation is not required merely for deployment.
- **Rationale:** This enables safer replacement/zero-or-low-downtime deployment while preserving the user's single-instance operating preference.
- **Rules:**
  1. Adjacent versions must honour the frozen interoperability window across schema/jobs/shared contracts.
  2. The outgoing instance is removed from new traffic/work and drains bounded in-flight work where safe.
  3. Unfinished durable obligations rely on idempotent recovery rather than invented completion.
  4. Exact provider/VPS rollout mechanism is AR-008 work.
- **Failure behaviour:** If the candidate fails readiness, traffic remains/returns to the safe version where possible. Irreversible schema/data changes require forward-recovery planning rather than unsafe binary rollback.
- **Security/privacy:** Both temporary versions must enforce equivalent active security/privacy law during overlap.
- **Performance/scaling:** Deployment overlap is temporary capacity, not the launch scaling topology.
- **Enforcement/downstream:** AR-008 defines blue/green/rolling/replacement mechanics and migration ordering; AR-005 durable-job/version compatibility.

## ARC-016 — Runtime health distinguishes startup, liveness and readiness

- **Decision source:** AR-001 T2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-144`, `ARQ-PERF-145`, `ARQ-PERF-154`
- **Decision:** The runtime exposes distinct startup-complete, liveness and readiness semantics. Readiness means the instance can safely accept its intended traffic/work; liveness means the process is healthy enough that restart is appropriate/not appropriate; startup gates initial safe activation. Optional provider/cache outages do not automatically make the whole application dead.
- **Rationale:** Safe deployment/recovery requires a meaningful distinction between process health, mandatory initialization and capability/dependency degradation.
- **Rules:**
  1. Mandatory initialization must complete before readiness.
  2. Optional cache warming is bounded and not a correctness prerequisite.
  3. Dependency-specific degradation may disable only affected capability where safe.
  4. Exact endpoints/check implementations remain AR-008.
- **Failure behaviour:** A failed mandatory dependency can remove readiness for affected intended work; optional dependency outage should not cause endless restart loops of an otherwise healthy application.
- **Security/privacy:** Health output must not leak credentials, sensitive configuration or participant data.
- **Performance/scaling:** Health checks must remain cheap/bounded and suitable for future replica traffic management.
- **Enforcement/downstream:** AR-008 defines checks, orchestration/provider integration and degradation matrix.

## ARC-017 — Build once; inject environment-specific runtime configuration and secrets at deployment

- **Decision source:** AR-001 T2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-002`, `ARQ-SYS-005`, `ARQ-PERF-155`
- **Decision:** Application images/releases are immutable across staging/production/provider targets; environment-specific configuration and secrets are supplied at runtime through approved provider/VPS configuration and secret-management boundaries. Do not bake production credentials or participant data into images or source control.
- **Rationale:** Runtime configuration preserves artifact portability and enables safe credential/configuration changes without maintaining divergent code builds.
- **Rules:**
  1. Secrets never live in committed source or production image layers.
  2. Configuration that changes Product/Architecture Law remains governed even if technically represented as environment/runtime data.
  3. Required configuration is validated before readiness.
  4. Recoverability of required configuration/secrets is included in disaster-recovery planning.
- **Failure behaviour:** Missing/invalid mandatory configuration fails startup/readiness safely rather than silently defaulting to unsafe values.
- **Security/privacy:** Least-privilege secret access, rotation and audit are downstream requirements; logs/error output must not expose secret values.
- **Performance/scaling:** Runtime configuration supports the same image in combined/web/worker/future-replica roles.
- **Enforcement/downstream:** AR-008 selects secret/config mechanism and deployment validation; AR-004/006 may define provider credential scopes.

## ARC-018 — Primary application and latency-sensitive state services stay co-located by region/location where practical

- **Decision source:** AR-001 T2.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-002`, `ARQ-PERF-073`, `ARQ-PERF-161`, `ARQ-OPS-002`
- **Decision:** Keep the primary application runtime, authoritative PostgreSQL service and other latency-sensitive shared services in the same primary region/location or low-latency network boundary wherever practical. Disaster-recovery/backup copies deliberately cross appropriate failure boundaries. Do not create chatty cross-continent database/cache topology merely for provider convenience.
- **Rationale:** Most Phoenix/Ash business interactions are latency-sensitive to PostgreSQL; unnecessary geographic separation increases request latency, connection cost and failure complexity without improving launch correctness.
- **Rules:**
  1. Provider choice evaluates application-to-database/network latency as one topology.
  2. Redis, when used on latency-sensitive paths, normally resides near the application/authority it accelerates.
  3. Backup/DR separation is distinct from active request-path placement.
  4. Future multi-region operation requires a later explicit architecture decision.
- **Failure behaviour:** Regional dependency failure follows governed degradation/recovery rather than attempting unsafe ad-hoc cross-region writes.
- **Security/privacy:** Private service networking/encryption and data-location requirements remain applicable.
- **Performance/scaling:** Avoid cross-region round trips on ordinary OLTP/request paths; later read replicas/regionalisation remain evidence-gated.
- **Enforcement/downstream:** AR-003 decides DB/cache topology; AR-007 DR/backup; AR-008 provider/network placement; AR-009 latency/capacity proof.

---

# 2A. AR-001 T2 Consolidated Deployment Doctrine

```text
PUBLIC INTERNET
      │
  Cloudflare
      │
SELECTED ORIGIN
Railway OR South-African VPS
      │
      ├── ONE application instance at launch
      │      ├── Phoenix/LiveView web
      │      └── durable/background workers
      │
      ├── PostgreSQL
      │      └── logically independent authority service
      │          (may be physically co-located on launch VPS)
      │
      ├── Redis only where explicitly justified
      │
      └── external object storage for durable files/media

DEPLOYMENT ARTIFACT
OCI image containing production Elixir/Phoenix Release
      │
      └── runtime configuration/secrets injected at deployment

SAFE DEPLOYMENT
one steady-state app instance
      +
optional temporary old/new overlap for readiness/cutover

FUTURE SCALE
vertical capacity → extra replicas → web/worker separation → other topology only by evidence
```

### T2 explicitly does not lock

- Railway versus a specific South-African VPS provider;
- Docker runtime/orchestrator product on the VPS;
- exact PostgreSQL hosting/managed product;
- exact Redis hosting/product/key design;
- exact object-storage vendor/bucket layout;
- exact Cloudflare WAF/cache/routing rules;
- exact secret manager;
- CI/CD vendor;
- permanent two-node deployment;
- Kubernetes;
- active-active multi-region.

# 2B. AR-001 Round T3 — Failure Boundaries, Private Networking & Growth Transition

**Accepted answer set:** `T3.1 B, T3.2 B, T3.3 B, T3.4 B, T3.5 B, T3.6 B, T3.7 B, T3.8 B`

**Launch-topology interpretation:** The first production deployment deliberately has one active application/runtime failure domain. This is an accepted availability trade-off, not a claim of high availability. Durable authority, backup/recovery and provider portability must be arranged so later capacity/redundancy can be introduced without redefining business truth.

---

## ARC-019 — The launch deployment explicitly accepts one active runtime failure domain

- **Decision source:** AR-001 T3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-141`, `ARQ-PERF-161`, `ARQ-PERF-166`, `ARQ-OPS-002`
- **Decision:** Initial production may operate with one active application/runtime host or provider instance. Containers, process separation or logically separate services on the same underlying host do not constitute independent high-availability failure domains. A host/location failure may therefore cause temporary service unavailability at launch. Recovery durability must cross the active-host failure boundary even though permanent redundant application capacity is not required initially.
- **Rationale:** This preserves the user's deliberately simple single-instance launch while accurately modelling availability risk and satisfying the frozen DR/recovery requirements.
- **Rules:**
  1. Do not advertise or design-assume high availability merely because components are containerised or separately supervised.
  2. Backups/recovery evidence required for service reconstruction must not depend solely on the failed active host.
  3. Availability redundancy is introduced when evidence or release requirements justify it, not to cosmetically eliminate the single-instance label.
  4. Correctness and recoverability requirements remain stricter than initial uptime topology.
- **Failure behaviour:** Loss of the active host may cause an outage, but must not silently convert uncommitted state into committed truth or eliminate the approved recovery path.
- **Security/privacy:** Recovery copies and credentials remain protected and independently access-controlled.
- **Performance/scaling:** The accepted single failure domain does not remove capacity-headroom, load-test or future-replica requirements.
- **Enforcement/downstream:** AR-007 defines backup/restore and deletion-safe replay; AR-008 defines provider recovery, availability objectives and operational failover; AR-009 validates capacity/failure behaviour.

## ARC-020 — Only the approved application ingress is public; state and internal services remain private

- **Decision source:** AR-001 T3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-IAM-004`, `ARQ-PERF-166`, `ARQ-SEC-001`
- **Decision:** The public network surface is limited to approved application/edge ingress. PostgreSQL, Redis and other internal infrastructure are not ordinary public Internet endpoints. On a VPS they use localhost/private interfaces/firewall boundaries as appropriate; on a managed platform they use provider-private networking where available. Administrative access is separate, restricted and auditable.
- **Rationale:** Password-protected public database/cache ports unnecessarily enlarge the attack surface and are not required by the target topology.
- **Rules:**
  1. Public application traffic enters through the approved ingress path.
  2. State services are private by default.
  3. Direct database administration is exceptional rather than an application access path.
  4. Private networking is a capability requirement; exact provider/VPS mechanics remain AR-008 work.
- **Failure behaviour:** Loss of private connectivity causes explicit dependency degradation/unreadiness rather than insecure public fallback.
- **Security/privacy:** No automatic exposure of database/cache/storage administration ports to the public Internet.
- **Performance/scaling:** Private low-latency paths should be used for chatty authority/acceleration traffic.
- **Enforcement/downstream:** AR-003 defines state-service connections; AR-004 privileged access; AR-008 firewall/private-network/provider configuration.

## ARC-021 — Cloudflare is the intended public edge and direct-origin exposure is minimised

- **Decision source:** AR-001 T3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SEC-001`, `ARQ-AN-213`, `ARQ-AN-214`, `ARQ-SYS-005`
- **Decision:** Cloudflare remains the intended common public edge. The selected origin should minimise direct public bypass of that edge as far as the hosting provider reasonably permits. AR-001 does not lock Cloudflare Tunnel, Authenticated Origin Pulls, fixed Cloudflare-IP allowlists or another specific mechanism; the mechanism is selected and proven in AR-008/provider work.
- **Rationale:** The architecture needs one coherent ingress/security/cache boundary without prematurely coupling the application to one origin-protection technique.
- **Rules:**
  1. Public DNS/routing should normally lead users through the approved edge.
  2. Origin-bypass exposure is treated as something to minimise, not a required feature.
  3. Provider limitations must be documented rather than hidden.
  4. Edge failure or bypass protection may not become payment/entitlement/safety authority.
- **Failure behaviour:** If the edge/origin path is unavailable, the application follows explicit degraded/maintenance behaviour; it does not silently open normally private services.
- **Security/privacy:** Origin protection complements, never replaces, application authentication/authorisation and data policy.
- **Performance/scaling:** Edge caching/rate protection may reduce origin load where safe; personalised/private correctness remains authoritative at the application/state layers.
- **Enforcement/downstream:** AR-003 handles cache/storage interaction; AR-008 locks origin-protection mechanics; AR-009 validates edge/origin load behaviour.

## ARC-022 — Production, staging/test and local development are separate runtime/data/security boundaries

- **Decision source:** AR-001 T3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-004`, `ARQ-OPS-001`, `ARQ-PERF-166`
- **Decision:** Production, staging/test and local development operate as distinct environments with separate runtime configuration, secrets and data boundaries. Production participant data is not copied into ordinary local development. Lower environments use synthetic, anonymised or separately governed test data appropriate to the proof being performed.
- **Rationale:** Environment isolation reduces accidental production-data exposure and prevents testing/deployment activity from becoming a production integrity dependency.
- **Rules:**
  1. Production credentials/secrets are not reused as ordinary development credentials.
  2. Lower-environment data does not create production business authority.
  3. Any exceptional production-derived test dataset requires explicit governance rather than convenience copying.
  4. The same portable application artifact may be configured differently at runtime without merging environment trust boundaries.
- **Failure behaviour:** Lower-environment failure cannot directly corrupt production authority.
- **Security/privacy:** Production participant data is excluded from ordinary local-development workflows.
- **Performance/scaling:** Performance tests requiring production-like volume should use safe representative data rather than weakening privacy boundaries.
- **Enforcement/downstream:** AR-004/AR-007 define data-access/privacy controls; AR-008 defines environment provisioning/secrets/deployment; Architectural Proof defines representative test fixtures.

## ARC-023 — Horizontal scaling is evidence-triggered and preceded by replica-safety proof

- **Decision source:** AR-001 T3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-001`, `ARQ-PERF-002`, `ARQ-PERF-008`, `ARQ-PERF-073`, `ARQ-PERF-086`, `ARQ-PERF-106`, `ARQ-PERF-134`, `ARQ-PERF-137`, `ARQ-PERF-141`
- **Decision:** Do not use account count as the trigger for multiple application instances. Scale the initial deployment vertically where sensible, then add replicas when measured CPU/RAM/latency/queue/connection/headroom evidence, deployment needs or availability objectives show that one instance is no longer sufficient. Before adding replicas, prove the relevant application/state paths are replica-safe.
- **Rationale:** User count is a poor proxy for workload, while premature clustering creates operational cost. The frozen ARQs nevertheless require multi-node-correct semantics before multi-node production is introduced.
- **Replica-safety gate before horizontal expansion:**
  1. shared durable authority remains correct;
  2. database connection/pool budget tolerates additional instances;
  3. temporary/node-local state is non-authoritative or reconstructible;
  4. PubSub/realtime semantics are appropriate for multiple nodes;
  5. distributed rate/velocity controls are used where cross-node correctness requires them;
  6. durable jobs remain idempotent and safe under concurrent workers;
  7. LiveView reconnect/re-authorisation works across replacement nodes;
  8. load/failure tests validate the target replica topology.
- **Failure behaviour:** A scaling event may never manufacture duplicate work, entitlements, payment truth or safety decisions.
- **Security/privacy:** Additional replicas inherit the same actor/policy/secret/private-network controls; scaling is not an authorisation bypass.
- **Performance/scaling:** Horizontal scale is introduced from measured need and validated as a system, including database and shared-infrastructure pressure.
- **Enforcement/downstream:** AR-003/005/008/009 define the exact shared-state, PubSub, queue, connection and scaling proof mechanisms.

## ARC-024 — PostgreSQL may be physically co-located initially but can move independently when evidence justifies it

- **Decision source:** AR-001 T3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-073`, `ARQ-PERF-075`, `ARQ-PERF-086`, `ARQ-STATE-001`, `ARQ-PERF-161`
- **Decision:** If the VPS path is chosen, the launch application and PostgreSQL may share the same physical VPS while remaining logically separate services. PostgreSQL moves to dedicated/managed infrastructure when resource contention, I/O/storage pressure, maintenance independence, availability/recovery needs, connection capacity or measured scale justify separation. The move is an infrastructure/topology change, not a redefinition of domain/business authority.
- **Rationale:** Dedicated database infrastructure from day one is not required to preserve sound authority boundaries, but the application must not be architecturally fused to local database co-location.
- **Rules:**
  1. PostgreSQL remains the same durable authority before and after physical separation.
  2. Connection configuration is runtime/provider configuration, not domain semantics.
  3. Co-location must not prevent independent backup/recovery planning.
  4. A later managed/dedicated move requires latency, security, pool and migration proof.
- **Failure behaviour:** Database movement/cutover must fail safely and preserve authoritative consistency; no hidden local-file fallback.
- **Security/privacy:** Database networking remains private and encrypted/protected as required by the selected topology.
- **Performance/scaling:** Separation is evidence-driven and considers latency as well as contention/availability gains.
- **Enforcement/downstream:** AR-003 defines connection/persistence topology; AR-008 migration/operations; AR-009 capacity evidence.

## ARC-025 — Railway ↔ VPS movement should be infrastructure migration, not business-architecture migration

- **Decision source:** AR-001 T3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-004`, `ARQ-SYS-005`, `ARQ-PERF-161`, `ARQ-OPS-002`, `ARQ-CONTENT-006`
- **Decision:** Hosting-provider portability is an architectural property. Moving the approved application between Railway and a South-African VPS/provider should normally change infrastructure/configuration/operations rather than business semantics. Provider-native features may be used when useful, but application correctness and durable business authority must not become unnecessarily dependent on an irreplaceable hosting primitive.
- **Rationale:** The launch provider remains intentionally undecided, and future cost, region, capacity or availability evidence may justify a move.
- **Rules:**
  1. The portable OCI/Phoenix release remains the primary application artifact.
  2. Runtime configuration/secrets remain external to the image.
  3. PostgreSQL, optional Redis and S3-compatible object storage are capability boundaries rather than provider identity in domain logic.
  4. Provider-specific features require an explicit boundary when loss/replacement would affect application semantics.
  5. Portability does not mean refusing all valuable provider-native services; it means keeping authority and contracts explicit.
- **Failure behaviour:** Provider migration is planned/cut over with rollback or forward-recovery; it is not an ad-hoc emergency rewrite.
- **Security/privacy:** Provider changes must re-prove data location, private networking, secrets, backup and access controls.
- **Performance/scaling:** Migration must revalidate latency, connection budgets, storage performance and workload envelopes.
- **Enforcement/downstream:** AR-003/006/007/008/009 own provider-specific proof and migration mechanics.

## ARC-026 — AR-001 stops at topology law; deployment-tool implementation belongs downstream

- **Decision source:** AR-001 T3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-005`, `ARQ-PERF-166`, `ARQ-OPS-001`, `ARQ-OPS-002`; process authority `02_OPEN_WORK_v1.2.3.md` Phase 2 workstream separation
- **Decision:** AR-001 defines runtime/deployment topology, public/private/failure boundaries and growth transitions but does not select or configure the exact VPS container manager, Docker Compose/systemd/Coolify-style tooling, firewall commands, secret manager, backup product, Cloudflare origin-protection configuration, CI/CD provider, Railway project settings or health-endpoint implementation. Those choices belong primarily to AR-008 and later Architectural Proof/JIT work unless another architecture workstream legitimately owns part of the mechanism.
- **Rationale:** This preserves workstream discipline and prevents AR-001 from becoming an implementation programme.
- **Rules:**
  1. AR-001 must leave enough topology law for downstream choices to be coherent.
  2. Downstream tooling may not contradict ARC-001–026.
  3. Tool/provider selection uses current evidence at the time it is needed.
  4. A future tool choice that changes architecture semantics requires an ARC amendment rather than silent implementation drift.
- **Failure behaviour:** Operational tooling failure is handled under AR-008; it may not redefine authoritative business state.
- **Security/privacy:** Downstream tools must satisfy existing secret/private-access/data-location requirements.
- **Performance/scaling:** Tooling must support the accepted single-instance launch and evidence-gated growth path without forcing unnecessary permanent clustering.
- **Enforcement/downstream:** AR-008 is the primary owner; Architectural Proof validates deployment/recovery mechanics.

---

# 2C. AR-001 Consolidated Runtime Topology

```text
                         PUBLIC INTERNET
                               │
                          CLOUDFLARE
                     intended public edge
                               │
                    minimise origin bypass
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
        SOUTH-AFRICAN VPS                 RAILWAY
            candidate                     candidate
                 │                           │
                 └─────────────┬─────────────┘
                               │
                     ONE APP INSTANCE
                         at launch
                 Phoenix / LiveView / Ash
                    web + worker roles
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
        PostgreSQL        Redis if justified   S3-compatible
      durable authority    acceleration /       object storage
                           coordination only     durable files
             │                 │                 │
             └──────── private/internal ─────────┘

INITIAL REALITY
- one active runtime failure domain
- not falsely described as HA
- backup/recovery crosses the active-host failure boundary

GROWTH PATH
vertical capacity
      ↓ evidence
additional app replicas
      ↓ proof
same-region BEAM/PubSub multi-node operation
      ↓ evidence
web/worker pool separation
      ↓ only if durable need exists
independent service extraction / further regionalisation
```

This topology does **not** assign final business domains, Ash Resources, database tables, Redis keys, PubSub topics, worker names, provider products or deployment commands.

---

# 2D. AR-001 Closure Audit — PASSED

**Audit date:** 2026-08-16  
**Result:** `AR-001 — System Shape & Runtime Topology` is **COMPLETE**. No additional AR-001 Grill round is required.

The 37 frozen ARQs routed to AR-001 were checked against ARC-001–ARC-026 and downstream ownership. AR-001 has made the topology decisions necessary for later workstreams without consuming their implementation/detail authority.

| AR-001 requirement surface | Architecture-law coverage | Result / downstream boundary |
|---|---|---|
| One platform / controlled product spaces / future-space activation | `ARC-001`, `ARC-002` | COVERED; concrete business ownership remains `04_DOMAIN_MAP.md` |
| Scale-ready but simple launch shape | `ARC-003`, `ARC-006`, `ARC-019`, `ARC-023` | COVERED; one instance now, replicas only by evidence |
| Multi-node correctness / node-loss / LiveView reconstruction | `ARC-003`–`ARC-005`, `ARC-007`, `ARC-023` | COVERED; exact PubSub/session mechanisms go to AR-002/005/009 |
| Process ownership / supervision / fault containment | `ARC-001`, `ARC-006`, launch failure-boundary law in `ARC-019` | COVERED at topology level; exact supervision tree belongs AR-002/008 |
| PostgreSQL/connection/distribution growth | `ARC-007`, `ARC-012`, `ARC-018`, `ARC-023`, `ARC-024` | COVERED; exact persistence/pool/proxy design belongs AR-003/009 |
| Worker separation | `ARC-006`, `ARC-023` | COVERED; exact queues/concurrency belong AR-005/008/009 |
| PubSub/realtime topology | `ARC-004`, `ARC-005`, `ARC-023` | COVERED; no cluster at launch, multi-node adapter/discovery deferred appropriately |
| Startup/readiness/deploy coexistence/drain | `ARC-015`–`ARC-017`, `ARC-026` | COVERED; exact health endpoints/deploy tooling AR-008 |
| Public/private ingress and provider portability | `ARC-010`, `ARC-011`, `ARC-020`, `ARC-021`, `ARC-025` | COVERED |
| Object/media topology | `ARC-014` + accepted AR-003/006 proof inputs | COVERED at topology level; package/provider/lifecycle detail deferred |
| Single-primary-location / DR boundary | `ARC-008`, `ARC-018`, `ARC-019`, `ARC-025` | COVERED; restore/RPO/RTO/provider mechanics AR-007/008/009 |
| Cross-domain analytics/experiment delivery topology | `ARC-001`, `ARC-011`, `ARC-020`, `ARC-021` | COVERED at topology boundary; variant cache/assignment semantics remain AR-003/005/008/009 |
| Clean multilingual/public routing | `ARC-002`, `ARC-011`, `ARC-021` | COVERED at system-shape level; concrete Phoenix routes/content metadata AR-002/006 |
| Media provider boundary / no self-hosted first-release transcoder | `ARC-014` plus external-provider boundary carried to AR-006 | COVERED; exact Restream/Cloudflare Stream validation remains provider gate |
| LearnDash clean-cutover/non-authority | `ARC-001` native modular-platform boundary + explicit ARQ handoff to AR-002/003/006 | COVERED for AR-001: no LearnDash runtime/deployment subsystem becomes part of target topology |
| Recovery includes config/secrets/object state | `ARC-017`, `ARC-019`, `ARC-025` | COVERED at topology boundary; execution belongs AR-007/008 |

### AR-001 closure invariants

1. **Launch simplicity is explicit:** one app instance; combined web/worker runtime; no mandatory BEAM cluster, Kubernetes or permanent replica set.
2. **Future scale does not require business-model redesign:** application correctness, shared authority and portable boundaries are replica/provider compatible.
3. **One-host launch is not misrepresented as HA:** availability risk is accepted and recovery crosses failure domains.
4. **Public exposure is narrow:** the approved application ingress is public; state/internal services remain private.
5. **Authority remains external to replaceable compute:** application/container/node loss affects service/freshness before it affects durable truth.
6. **Provider choice remains open:** Railway and South-African VPS remain deployment candidates; current provider capabilities are evidence, not Product Law.
7. **AR-001 stops before implementation tooling:** exact deploy, firewall, secret, backup, cluster-discovery and provider configuration moves downstream.
8. **No final business-domain ownership was assigned.**

**Immediate next workstream:** `AR-002 — Phoenix / LiveView / Ash / Code Boundaries`.

---

# 3. External Evidence Snapshot — 2026-08-16

These are **architecture evidence inputs, not permanent Product Law** and must be revalidated when provider/deployment selection is finalised.

1. Railway official Regions documentation currently lists four deployment regions: US West (California), US East (Virginia), EU West (Amsterdam), and Southeast Asia (Singapore). No South African Railway deployment region is listed.
2. Railway official Advanced Concepts documentation states deployments use a single instance by default and replicas may be added later.
3. Railway official Scaling documentation supports adding/removing replicas without requiring a new application architecture.
4. Phoenix/Elixir documentation supports distributed Erlang clustering for multiple instances, but clustering is unnecessary when only one application instance exists.

---

# 3A. Deferred AR-003 / AR-006 Proof Inputs — Object Storage, Attachments & Uploads

> **Status:** ACCEPTED AS DOWNSTREAM ARCHITECTURE/PROOF INPUTS — not AR-001 topology law and not package/provider locks.
> **Acceptance source:** User acceptance on 2026-08-16 after architectural review of Wasabi, `ash_storage`, `req_s3`, Waffle and ExAws options.
> **Routing:** Primarily AR-003 State Authority, Persistence, Caching & Storage and AR-006 Content, Translation, Media & External Integrations, with AR-007 privacy/deletion and AR-008 operations/security implications.

The following constraints/candidates must be carried into downstream architecture and Architectural Proof:

1. **S3-compatible durable-object boundary.** Durable uploads/media/files should use an S3-compatible object-storage capability rather than provider-specific domain code.
2. **Wasabi is a preferred initial provider candidate, not business authority.** Provider selection remains replaceable and must pass data-location, privacy, latency, retention/economic and operational proof.
3. **`ash_storage` is the preferred Ash-native attachment candidate to prove**, not yet a locked dependency.
4. **`req_s3` is the preferred S3 transport candidate if `ash_storage` is selected**, subject to proof against the chosen S3-compatible provider.
5. **Do not adopt parallel S3 client stacks without demonstrated need.** `ReqS3` and `ExAws.S3` should not both become default infrastructure merely for convenience.
6. **Waffle remains a fallback candidate**, not a parallel default attachment architecture, unless proof shows a material capability/maturity advantage that justifies it.
7. **Direct-to-object-storage upload should be supported for appropriate participant files.** Phoenix/LiveView should authorise and presign where suitable so large uploads need not proxy through the application process.
8. **Direct upload enters a restricted/quarantine state, not trusted/public state.** Successful transfer does not equal approval; actual object validation, MIME/content inspection, malware/security processing, metadata sanitisation where required, policy checks and governed promotion/publication still apply.
9. **File lifecycle is broader than one database row/object.** Architecture must account for the authoritative object plus derivatives, previews/thumbnails, extracted values, indexes, cached/signed access capability, superseded objects and temporary processing artefacts where applicable.
10. **Object deletion must be durable, retryable, observable and reconcilable.** Database lifecycle/destruction alone may not be treated as proof that external object bytes and eligible derivatives are gone. Deletion completion requires a governed confirmation/reconciliation path consistent with ARQ-STATE deletion law.
11. **Separate ephemeral-file economics from durable-object storage.** Wasabi or another long-retention durable store is not automatically the scratch/temp-file tier. Bounded local temporary filesystem or a separately justified ephemeral object tier may be used where safe; Redis/PostgreSQL are not general-purpose scratch-file stores.
12. **Object-storage HTTP concurrency must be bounded and observable.** Exact HTTP client, connection pool, timeout and concurrency settings are deferred; object-store workloads may not create uncontrolled socket, memory or worker pressure.

### Proof questions carried forward

Before locking the attachment/storage package/provider combination, downstream proof must establish at minimum:

- Wasabi/S3 endpoint compatibility and signing behaviour;
- direct-upload/presign flow and post-upload verification;
- private/protected signed delivery;
- attachment metadata/version relationships;
- derivative processing lifecycle;
- deletion failure/retry/reconciliation;
- quarantine/security scanning path;
- provider/data-location/privacy suitability for each data class;
- provider minimum-retention/egress economics for durable versus ephemeral objects;
- bounded concurrent upload/download/worker behaviour;
- provider portability without changing business/domain semantics.

These inputs do **not** lock Wasabi, `ash_storage`, `req_s3`, Waffle, ExAws, bucket layout, object keys, presign TTLs, scanning vendor, lifecycle policy or CDN delivery mechanics.

---


# 3B. AR-002 — Phoenix / LiveView / Ash / Code Boundaries

## 3B.1 Round C1 — Application Authority & Call Flow

**Accepted answer set:** `C1.1 B, C1.2 B, C1.3 B, C1.4 B, C1.5 B, C1.6 B, C1.7 B, C1.8 B`

**Architecture intent:** Phoenix/LiveView owns first-party interaction and presentation; authoritative application/business operations are exposed through Ash actions and coherent application APIs. The framework boundary must prevent UI, jobs or future adapters from becoming alternative business-rule implementations. Final concrete business-domain ownership remains deferred to `04_DOMAIN_MAP.md`.

## ARC-027 — Ash actions are the normal authoritative application/business-operation boundary

- **Decision source:** AR-002 C1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-PERF-166`, plus ARQ families requiring one authoritative rule path for payment, entitlement, safety, plans, content and lifecycle state
- **Decision:** For business state governed by the Ash application model, Ash actions are the normal authoritative application/business-operation boundary. Phoenix/LiveView, Oban workers, internal callers and future adapters invoke those operations rather than recreating their validations, policies, state transitions or persistence semantics independently.
- **Rationale:** The platform needs one enforceable application-operation path so correctness, authorisation, validation, audit and transaction semantics do not vary by caller. Ash actions are explicitly designed to describe allowed operations on resources and to carry actor/context through the action lifecycle.
- **Rules:**
  1. Business mutations are not implemented as ad-hoc persistence from UI or worker code.
  2. Read operations that carry policy/business semantics also use the approved Ash action/interface path.
  3. Pure computation may remain ordinary Elixir when no Ash operation semantics are required.
  4. Exceptional low-level data/infrastructure access must be explicit and may not become a parallel business API.
- **Failure behaviour:** A caller failure or alternate delivery surface cannot bypass the same authoritative validation/policy/state-transition contract.
- **Security/privacy:** Actor and authorisation context must be available to protected actions; callers cannot weaken policy by choosing a different interface.
- **Performance/scaling:** Actions must remain suitable for efficient bounded execution; the boundary does not require unnecessary resource/action hops for pure logic.
- **Enforcement/downstream:** AR-002 further defines actor/policy/code structure; AR-004 defines identity/auth policy semantics; AR-005 transaction/async consequences; Domain Map later assigns concrete business ownership.

## ARC-028 — Phoenix and LiveView remain a thin delivery/interaction layer over application authority

- **Decision source:** AR-002 C1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-137`, `ARQ-PERF-138`, `ARQ-IAM-001`–`ARQ-IAM-006`, `ARQ-SYS-002`
- **Decision:** Phoenix controllers/components and LiveViews own transport, routing/navigation, presentation state, UI event handling and rendering. They may coordinate user interaction but do not become the authoritative location for durable business rules, entitlement/safety decisions, policy semantics or state-transition law.
- **Rationale:** UI processes are transient and delivery-specific. Keeping business authority behind the application boundary prevents LiveView lifecycle/reconnect or future API changes from changing business meaning.
- **Rules:**
  1. `handle_event`/controller code translates UI intent into approved application calls.
  2. UI-level validation may improve feedback but never replaces authoritative action validation.
  3. LiveView assigns/socket state is interaction state, not durable business truth.
  4. Reconnect or alternate delivery surfaces must re-establish the required actor/context rather than inherit implicit trust.
- **Failure behaviour:** LiveView/process loss may lose transient presentation state but not committed business truth; callers reconstruct from authority.
- **Security/privacy:** UI visibility is not authorisation. Server-side action/policy enforcement remains mandatory.
- **Performance/scaling:** Thin delivery code reduces duplicate queries/rules and keeps LiveView process state bounded.
- **Enforcement/downstream:** AR-002 defines LiveView/Ash interaction patterns; AR-004 actor/policy propagation; AR-009 realtime scale proof.

## ARC-029 — Ordinary business code does not use Ecto.Repo as a second business API

- **Decision source:** AR-002 C1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-042`, `ARQ-PERF-064`, `ARQ-IAM-005`–`ARQ-IAM-007`, `ARQ-STATE-002`
- **Decision:** Business state governed by Ash is normally accessed through Ash actions/interfaces rather than direct `Ecto.Repo` calls from Web, workers or ordinary application modules. Direct Ecto/Repo usage remains allowed for explicit infrastructure, migration, data-layer or exceptional architectural needs, but it may not silently bypass action/policy/audit/business invariants.
- **Rationale:** Uncontrolled direct Repo access would create a parallel business path that can bypass Ash policies, validations, notifications and action semantics.
- **Rules:**
  1. Direct Repo access requires an explicit architectural reason.
  2. Reads are not automatically exempt merely because they do not mutate state; protected read semantics still go through policy-aware paths.
  3. Migrations/data repair/ops tooling follow separate controlled authority and audit rules.
  4. AshPostgres/Ecto remain valid implementation layers underneath Ash; this rule concerns caller boundaries, not banning Ecto.
- **Failure behaviour:** Exceptional low-level operations must fail closed with respect to protected invariants and must not become routine fallback paths.
- **Security/privacy:** Direct data access cannot be used to bypass record/field policy.
- **Performance/scaling:** Low-level optimisation may be considered later when proven necessary, but must preserve equivalent correctness/policy semantics.
- **Enforcement/downstream:** Code review/lint/tests should detect inappropriate Repo use; AR-003 owns persistence mechanics; AR-008 owns privileged repair/ops access.

## ARC-030 — Ash.Domain expresses approved application API/resource boundaries; Domain Map owns final business boundaries

- **Decision source:** AR-002 C1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-001`, `ARQ-SYS-002`, `ARQ-IAM-001`; AR-000 amendment deferring final domain ownership to `04_DOMAIN_MAP.md`
- **Decision:** `Ash.Domain` is the preferred framework construct for grouping approved related resources and exposing coherent application APIs, but AR-002 does not name/freeze the final domain catalogue. `04_DOMAIN_MAP.md` determines final concrete business ownership; Ash Domains then express those approved boundaries in code.
- **Rationale:** This uses Ash's native organisational/API boundary without repeating the earlier mistake of pre-naming business domains before modelling.
- **Rules:**
  1. Do not create one giant catch-all Domain merely for convenience unless later modelling proves that boundary.
  2. Do not create one Domain per Resource mechanically.
  3. Domain relationships/interfaces follow approved Domain Law, not folder aesthetics.
  4. Cross-domain application calls must remain explicit.
- **Failure behaviour:** A framework grouping decision may not silently redefine business authority; conflicts route back to Domain Law/Architecture amendment.
- **Security/privacy:** Domain grouping does not replace action/resource/field policies.
- **Performance/scaling:** Domain boundaries are logical/API boundaries, not automatic network-service boundaries.
- **Enforcement/downstream:** `04_DOMAIN_MAP.md` is authoritative for final ownership; implementation maps approved domains/resources accordingly.

## ARC-031 — Normal internal call sites prefer Ash code interfaces over scattered low-level action construction

- **Decision source:** AR-002 C1.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-002`, `ARQ-IAM-001`, `ARQ-PERF-166`
- **Decision:** Normal application callers should prefer well-defined Ash code interfaces for approved actions so business operations appear as discoverable typed function APIs. Direct construction of `Ash.Query`, `Ash.Changeset` or `Ash.ActionInput` remains available where genuinely useful, but must not be scattered as the default call style.
- **Rationale:** Code interfaces expose Ash actions cleanly while preserving the action as authority and avoiding repetitive caller-specific construction logic.
- **Rules:**
  1. Prefer named application-facing functions for common operations.
  2. Do not add a redundant custom wrapper layer around every generated interface by default.
  3. Low-level construction is acceptable for specialised composition/testing where clearer.
  4. Internal code does not call its own HTTP/REST endpoints to reach business operations.
- **Failure behaviour:** Callers receive the same authoritative action result/error model regardless of delivery surface.
- **Security/privacy:** Actor/scope/context must still be passed correctly through code interfaces.
- **Performance/scaling:** Interfaces should not introduce extra network or persistence round-trips.
- **Enforcement/downstream:** AR-002 establishes naming/call conventions; Domain Map later determines the concrete public APIs.

## ARC-032 — AshPhoenix.Form is preferred for Ash-backed forms; UI-only forms may remain ordinary Phoenix forms

- **Decision source:** AR-002 C1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`, `ARQ-IAM-006`, validation/safety invariants across Product Law
- **Decision:** For forms that invoke Ash-backed create/read/update/destroy/generic action workflows, `AshPhoenix.Form` is the preferred Phoenix/LiveView integration where it fits. Ordinary Phoenix forms remain appropriate for interaction-only/non-resource UI state. Client-side validation is UX assistance only; authoritative validation remains server-side in the application/action contract.
- **Rationale:** AshPhoenix.Form is designed to build, validate and submit forms against Ash actions while carrying actor/scope into the underlying action.
- **Rules:**
  1. Avoid duplicating authoritative validation into a separate Ecto changeset solely for the UI.
  2. Complex UI composition may use normal Phoenix form structures where AshPhoenix.Form is not the right abstraction.
  3. Form errors should be translated into user-safe presentation without leaking sensitive policy internals.
  4. Actor/scope must be present before building action-aware forms when policy/changes/hooks depend on them.
- **Failure behaviour:** Invalid/stale/unauthorised form submission fails through the authoritative action contract, not by trusting prior UI validation.
- **Security/privacy:** Form visibility/input controls do not grant permission; policy remains server-side.
- **Performance/scaling:** Live validation must be bounded/debounced where necessary and must not create unbounded DB/work amplification.
- **Enforcement/downstream:** AR-002/004 define actor-aware form construction; Feature Packs select exact form implementation per workflow.

## ARC-033 — Multi-step/multi-resource business orchestration stays behind the application boundary; pure logic stays ordinary Elixir where appropriate

- **Decision source:** AR-002 C1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-166`, `ARQ-IAM-006`, `ARQ-ASYNC-001`–`ARQ-ASYNC-003`; cross-domain Product Law flows
- **Decision:** Authoritative multi-step or multi-resource business orchestration is implemented behind the application boundary. Use Ash actions when the operation benefits from Ash policy, validation, typing, transaction or API semantics; use ordinary Elixir modules/functions for pure deterministic logic where those semantics add no value. LiveView/controller code is not the authoritative workflow engine, and GenServer is not the default orchestration abstraction.
- **Rationale:** This preserves one business-operation boundary while keeping framework use proportional and avoiding both UI orchestration and "everything must be an Ash action" over-engineering.
- **Rules:**
  1. Pure calculations/rules may be normal testable Elixir modules/functions and be called by actions.
  2. Operations that change protected durable state or require actor/policy semantics enter through an approved application action.
  3. Durable asynchronous consequences are handled under AR-005 rather than hidden in transient UI processes.
  4. Cross-domain orchestration must respect final Domain Law ownership once defined.
- **Failure behaviour:** Partial workflow failure follows action/transaction/async law rather than leaving UI-owned half-state.
- **Security/privacy:** Orchestration cannot invent or broaden actor authority.
- **Performance/scaling:** Pure compute is not forced through unnecessary persistence/framework layers; hot paths remain optimisable behind stable contracts.
- **Enforcement/downstream:** AR-005 defines transaction/saga/async boundaries; Domain Map defines ownership and permitted cross-domain interactions.

## ARC-034 — Do not build speculative REST/GraphQL surfaces; preserve adapter-ready application actions

- **Decision source:** AR-002 C1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-005`, `ARQ-PERF-002`, `ARQ-PERF-166`
- **Decision:** Phoenix LiveView is the initial first-party interactive delivery surface. The architecture does not require parallel REST or GraphQL exposure for every action at launch. Ash application actions/interfaces must remain reusable by future API adapters when a real product/integration requirement exists.
- **Rationale:** This preserves API optionality without building unused network contracts or multiplying security/versioning work before a consumer exists.
- **Rules:**
  1. No internal self-HTTP calls are required for application operations.
  2. Future REST/GraphQL adapters consume existing authoritative actions rather than reimplementing business logic.
  3. API exposure is explicit and separately secured/versioned; action existence does not automatically imply public API exposure.
  4. A later API requirement may trigger a dedicated ARC/Feature Pack without changing the underlying business authority model.
- **Failure behaviour:** Absence/failure of an optional API adapter cannot alter LiveView/application business truth.
- **Security/privacy:** New API surfaces require explicit auth/authz/field-policy/export-abuse review.
- **Performance/scaling:** Avoids unnecessary duplicate ingress/fan-out at launch while preserving future adapter scale paths.
- **Enforcement/downstream:** AR-004 policy, AR-008 rate/security operations and future API-specific planning govern exposed adapters.

### AR-002 C1 interim invariants

1. Phoenix/LiveView is a delivery/interaction layer; it does not own durable business law.
2. Ash actions are the normal authoritative application-operation boundary.
3. Ash code interfaces are the preferred normal internal application API.
4. Direct Repo/Ecto usage does not become a parallel business path.
5. Ash Domain expresses later-approved business/API boundaries but does not decide them before Domain Map.
6. AshPhoenix.Form is preferred for Ash-backed form workflows where appropriate.
7. Pure deterministic logic may remain ordinary Elixir; framework use is proportional.
8. REST/GraphQL remain future adapters, not speculative launch requirements.

**Next AR-002 scope:** C2 — Actor propagation, policy enforcement and field-level privacy.


# 3C. AR-002 C2 — Actor Propagation, Policy Enforcement & Field-Level Privacy

## ARC-035 — Actor/application context is explicit through the full application call chain

- **Decision source:** AR-002 C2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-002`, `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-PERF-138`
- **Decision:** Authenticated identity plus the applicable application actor/scope/context is passed explicitly from Phoenix/LiveView entry points into Ash code interfaces, forms, queries and actions. Hidden global/process-state lookup is not the normal authorisation mechanism, and authorising only in the Web layer is insufficient.
- **Rationale:** Ash action hooks, policies and field visibility may depend on the actor/context while the action/query/form is being constructed. Explicit propagation makes the authority available at the point where protected application semantics are evaluated and prevents caller-specific hidden trust.
- **Rules:**
  1. Authenticated requests establish an explicit application actor/context before protected application calls.
  2. Ash-backed forms/queries/actions receive that actor/context at construction/evaluation time where required.
  3. Callers do not rely on process dictionary/global mutable state to manufacture authorisation context.
  4. Web-layer route/socket visibility never substitutes for application-policy enforcement.
- **Failure behaviour:** Missing or invalid required actor/context fails closed for protected operations rather than silently acquiring broader authority.
- **Security/privacy:** Explicit propagation preserves subject, role/scope and purpose context for policy and audit decisions.
- **Performance/scaling:** Actor propagation is in-process metadata and must remain bounded; protected state is not copied wholesale into every caller.
- **Enforcement/downstream:** AR-004 defines exact actor/authentication/session models; Domain Law later assigns concrete role/relationship ownership.

## ARC-036 — Governed Ash authorisation is default-on; bypass is exceptional and explicit

- **Decision source:** AR-002 C2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-004`, `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-IAM-007`
- **Decision:** Governed application operations run with Ash authorisation enabled by default at the appropriate Domain/resource/action boundary. Call sites must not depend on remembering an opt-in flag. Any `authorize?: false` or equivalent bypass is an exceptional, separately governed infrastructure/maintenance path and may not become routine application behaviour.
- **Rationale:** The platform has privacy, clinical, practitioner, role and consent constraints that cannot safely depend on each caller remembering to enable enforcement. Default-on policy preserves one authoritative access path.
- **Rules:**
  1. Protected reads and writes are policy-authorised by default.
  2. Read operations are not exempt merely because they do not mutate state.
  3. Explicit bypass requires a defined operational authority/use case and corresponding audit/guardrails.
  4. Tests must cover failure-closed behaviour when actor/policy requirements are absent or denied.
- **Failure behaviour:** Policy uncertainty/denial does not degrade into permissive access.
- **Security/privacy:** Prevents caller-level policy bypass and supports least-privilege access.
- **Performance/scaling:** Policies should use efficient checks/filtering and avoid unnecessary protected-data loading; performance tuning may not remove required authorisation.
- **Enforcement/downstream:** AR-004 selects exact policy/auth mechanisms and bypass governance; AR-008 governs privileged maintenance/break-glass execution.

## ARC-037 — Anonymous, participant and system execution contexts are deliberate; causation is separate from executing authority

- **Decision source:** AR-002 C2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-004`, `ARQ-IAM-007`, `ARQ-IAM-008`, `ARQ-ASYNC-001`–`ARQ-ASYNC-003`
- **Decision:** Actor state is explicit for anonymous/public, authenticated human and governed system/service execution. Missing actor context never means privileged access. Durable/background work records the relevant causation/provenance separately from the authority under which the eventual worker executes; a job does not implicitly become administrator and does not trust an indefinitely stale user-authorisation snapshot.
- **Rationale:** Async work frequently executes later than the initiating request. Separating executor authority from causation preserves auditability while allowing current authoritative policy/state to be re-evaluated where required.
- **Rules:**
  1. Anonymous means deliberately unauthenticated, not accidentally missing context.
  2. System/service authority is named/scoped and separately governable.
  3. Background jobs carry only the identity/provenance/context necessary for safe execution and reconciliation.
  4. When an action depends on current consent/relationship/entitlement/security state, delayed execution re-checks applicable authority rather than trusting stale snapshots.
- **Failure behaviour:** Missing/expired/invalid authority causes the protected consequence to fail/reconcile safely rather than elevate access.
- **Security/privacy:** Prevents accidental worker superuser semantics and preserves initiator/audit provenance without over-copying sensitive state into job payloads.
- **Performance/scaling:** Job payloads remain bounded; current-state checks are targeted to authoritative facts.
- **Enforcement/downstream:** AR-004 defines actor/service authority; AR-005 defines durable job/causation/idempotency semantics; AR-008 covers privileged operational actors.

## ARC-038 — Authorisation composes role/capability with relationship, purpose, scope, expiry and authoritative state

- **Decision source:** AR-002 C2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-005`, `ARQ-IAM-006`, relevant field/privacy Analytics ARQs
- **Decision:** Ash policies do not treat a coarse role name as sufficient access authority. Governed access composes the relevant role/capability with authoritative facts such as record ownership/relationship, participant consent/purpose, scope, expiry, verification/assurance state and other Product-Law conditions.
- **Rationale:** Product Law explicitly separates role identity from sensitive authority and requires practitioner access to depend on a live consented relationship, scope and expiry.
- **Rules:**
  1. A broad staff/admin/practitioner role never implies blanket private-record access.
  2. Relationship/purpose/time constraints are evaluated where applicable.
  3. Policies reference authoritative application facts rather than presentation state.
  4. Final concrete policy ownership follows Domain Map rather than being preassigned here.
- **Failure behaviour:** Missing/expired/revoked relationship or permission denies future protected access.
- **Security/privacy:** Establishes least privilege and purpose limitation at the application boundary.
- **Performance/scaling:** Relationship/policy checks must be designed for bounded indexed evaluation and may use safe derived facts only when freshness/invalidation preserves authority.
- **Enforcement/downstream:** AR-004 defines the reusable policy model; AR-003 may define safe policy projections/acceleration; Domain Map defines authoritative owners.

## ARC-039 — Field-level privacy uses Ash field policies plus minimum-data loading; `sensitive?` is not authorisation

- **Decision source:** AR-002 C2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-005`, `ARQ-IAM-007`, privacy/minimisation ARQs across Analytics and State
- **Decision:** Genuinely protected Ash attributes/calculations/aggregates use field-policy enforcement where appropriate, together with resource/action policies and minimum-data loading. `sensitive?`/inspection redaction is a logging/display safeguard and must not be treated as permission enforcement. Sensitive related records remain protected by their own resource/action policy and loading boundaries.
- **Rationale:** Hiding a field in a template or redacting inspected values does not prevent a caller from receiving it. Privacy must be enforced before presentation and combined with data minimisation.
- **Rules:**
  1. Callers request only fields/relationships needed for the workflow.
  2. Field policies govern protected field visibility where the framework supports them.
  3. `sensitive?` is used for accidental-inspection/log protection, not as a substitute for policy.
  4. Sensitive relationships are loaded only through policy-aware resource boundaries.
- **Failure behaviour:** Forbidden protected fields/records do not leak through alternate callers or presentation paths.
- **Security/privacy:** Implements defence-in-depth field privacy and minimises sensitive data residency in transient processes.
- **Performance/scaling:** Smaller projections/loads reduce memory and query costs, especially in long-lived LiveViews.
- **Enforcement/downstream:** AR-004 defines field/policy classifications; Domain Dossiers identify exact protected fields/relationships.

## ARC-040 — Long-lived LiveViews never freeze business authorisation at mount time

- **Decision source:** AR-002 C2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-IAM-008`, `ARQ-PERF-137`, `ARQ-PERF-138`
- **Decision:** A LiveView may retain authenticated session/identity context, but every authoritative protected action remains subject to current applicable application policy. Consent withdrawal, relationship expiry, role revocation, account/security restriction or other authoritative change must be capable of denying a later action on an already-connected socket.
- **Rationale:** Product Law makes permission and consent dynamically effective. Mount-time checks alone would create stale access windows in long-lived stateful processes.
- **Rules:**
  1. Protected actions re-enter the policy-aware application boundary.
  2. Socket assigns do not store a permanent permission verdict as authority.
  3. Proactive socket notification/disconnect may be added for high-risk revocations, but is not the sole correctness mechanism.
  4. Reconnect reconstructs allowed state from current authority.
- **Failure behaviour:** Stale socket state may affect presentation freshness briefly but cannot authorise a denied business action.
- **Security/privacy:** Revocation becomes effective for future protected actions without waiting for logout/socket expiry.
- **Performance/scaling:** Current-policy checks should be targeted/bounded; broad repeated private-state loading is prohibited.
- **Enforcement/downstream:** AR-004 defines revocation/session state; AR-005 defines PubSub/proactive invalidation where useful; AR-009 proves realtime scaling.

## ARC-041 — There is no universal Super Admin policy bypass; break-glass is a separate exceptional authority path

- **Decision source:** AR-002 C2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-004`, `ARQ-IAM-005`, `ARQ-IAM-007`
- **Decision:** `Super Admin`, technical administration or production shell access does not automatically bypass all Ash policy or confer clinical/methodology/private-record authority. Ordinary privileged operations remain explicit scoped policy paths. Genuine break-glass access is a distinct exceptional path requiring the Product-Law controls for identity, strong authentication, reason, narrow scope, expiry, audit/alert and review.
- **Rationale:** Product Law explicitly separates technical breadth from methodology/clinical/data authority and prohibits routine unrestricted working roles.
- **Rules:**
  1. No ordinary actor gets a blanket `allow all` solely because of an admin label.
  2. Sensitive business authorities remain separately granted and policy checked.
  3. Break-glass operations are explicit and auditable rather than hidden `authorize?: false` convenience.
  4. Direct DB/ops paths remain exceptional and separately controlled.
- **Failure behaviour:** Failure of ordinary privileged policy does not automatically fall back to universal bypass.
- **Security/privacy:** Preserves least privilege, separation of duties and auditability for highly sensitive records/actions.
- **Performance/scaling:** No material topology effect; privileged audit/evidence must remain bounded and reliable.
- **Enforcement/downstream:** AR-004 and AR-008 define concrete grant, step-up, break-glass and operational-access mechanisms.

## ARC-042 — Data minimisation and policy enforcement are complementary; long-lived callers do not preload sensitive records for convenience

- **Decision source:** AR-002 C2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-IAM-007`, `ARQ-PERF-138`, privacy minimisation requirements across Product Law
- **Decision:** Policy enforcement is not permission to load entire protected records indiscriminately. Application/Web callers request the minimum fields/relationships required for the workflow while policy remains the authoritative defence if a caller asks for more. Long-lived LiveViews/processes do not retain broad sensitive datasets merely for future convenience.
- **Rationale:** Data minimisation reduces accidental disclosure, process-memory exposure and query/memory cost while policy supplies the non-bypassable security boundary.
- **Rules:**
  1. Prefer explicit projections/loads appropriate to the user journey.
  2. Avoid `load everything` patterns for health, journal, professional and other sensitive records.
  3. Long-lived socket/process state contains only necessary presentation/workflow data.
  4. Additional data is fetched policy-aware when the workflow actually needs it.
- **Failure behaviour:** Lost/restarted UI processes reconstruct minimum permitted state rather than relying on hidden broad caches.
- **Security/privacy:** Reduces blast radius of UI/process/logging defects and supports purpose limitation.
- **Performance/scaling:** Reduces DB transfer, BEAM heap size and LiveView memory pressure.
- **Enforcement/downstream:** AR-004 classifies sensitive access; implementation conventions/tests enforce bounded loads.

### AR-002 C2 interim invariants

1. Actor/application context is explicit through every protected Ash call path.
2. Governed authorisation is default-on; bypass is exceptional and separately controlled.
3. Anonymous and system execution are deliberate contexts; missing actor never means privileged.
4. Execution authority and causation/provenance remain distinguishable for delayed work.
5. Access policies compose role with relationship/purpose/scope/expiry/current authority rather than role alone.
6. Field policies enforce protected field visibility; `sensitive?` is only redaction assistance.
7. LiveViews do not freeze permissions at mount time; authoritative actions evaluate current policy.
8. Super Admin is not universal authority; break-glass is a separate exceptional path.
9. Minimum-data loading and policy enforcement are both required.

**Next AR-002 scope:** C3 — Resource/module boundaries, pure logic placement, dependency direction and cross-domain calls.


## 2.3 Round C3 — Resource Boundaries & Dependency Direction

**Accepted answer set:** `C3.1 B, C3.2 B, C3.3 B, C3.4 B, C3.5 B, C3.6 B, C3.7 B, C3.8 B`

## ARC-043 — Ash Resources model coherent application/business resources, not database tables or screens

- **Decision source:** AR-002 C3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-001`, `ARQ-SYS-002`, `ARQ-SYS-005`; governed by `ARC-027`, `ARC-030`
- **Decision:** An Ash Resource represents a coherent application/business resource whose identity, state, actions, relationships, policies and lifecycle belong together. Resource boundaries are not mechanically derived from PostgreSQL tables, UI screens or CRUD pages. Persistence structure may inform implementation, but it does not define business ownership.
- **Rationale:** The platform must derive application structure from approved business semantics while preserving final concrete business ownership for `04_DOMAIN_MAP.md`. Treating Resources as table wrappers would create persistence-led domain design and make later boundary changes unnecessarily invasive.
- **Rules:**
  1. Do not create a Resource merely because a table exists.
  2. Do not create a Resource merely because a screen needs a form.
  3. Supporting persistence structures may exist without becoming public application Resources.
  4. One Resource must not become a dumping ground for unrelated state merely to reduce module count.
  5. Final Resource inventory and ownership are produced after Domain Map/Profiles, not pre-decided by AR-002.
- **Failure behaviour:** If persistence/UI convenience conflicts with coherent business semantics, the application boundary wins and the persistence/presentation design is adapted.
- **Security/privacy:** Resource boundaries must not widen sensitive-data access merely to simplify joins or screens.
- **Performance/scaling:** Resource semantics do not prohibit specialised read models/projections later; performance optimisation must not silently transfer business authority.
- **Enforcement/downstream:** Domain Map establishes final owners; Domain Profiles/Dossiers define concrete Resource candidates and lifecycle; AR-003 defines persistence/read-model mechanisms.

## ARC-044 — Pure deterministic logic uses ordinary Elixir unless Ash semantics are materially required

- **Decision source:** AR-002 C3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-005`, `ARQ-PERF-002`; governed by `ARC-027`, `ARC-033`
- **Decision:** Pure deterministic rules/calculations may and should live in ordinary focused Elixir modules/functions when they do not require Ash authorization, persistence, typed action input, transaction semantics, lifecycle hooks or API exposure. Ash calculations/actions are used when the behaviour is part of the Resource/application contract or materially benefits from those Ash semantics.
- **Rationale:** Business logic should remain testable and composable without forcing every calculation through framework machinery, while authoritative operations remain governed by Ash actions.
- **Rules:**
  1. Pure functions have no hidden persistence/provider/UI side effects.
  2. Authoritative state transitions remain behind Ash actions/interfaces.
  3. Pure modules may be called from Ash changes/actions/calculations and from other approved application logic.
  4. Do not create generic actions solely to wrap trivial pure arithmetic.
- **Failure behaviour:** Pure-function failure returns explicit values/errors to the governing action; it does not partially commit business state.
- **Security/privacy:** Pure logic receives only the data it requires; it does not bypass action/policy boundaries to fetch protected data itself.
- **Performance/scaling:** Pure logic can be profiled/optimised independently; CPU-heavy exceptions may later be routed through the approved RUST-1-style boundary only if separately justified.
- **Enforcement/downstream:** Domain Dossiers decide which rules are pure modules versus Ash calculations/actions.

## ARC-045 — Ash changes, preparations, validations and calculations stay focused; substantial behaviour is extracted deliberately

- **Decision source:** AR-002 C3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-005`, `ARQ-PERF-002`; governed by `ARC-027`, `ARC-044`
- **Decision:** Simple local Ash behaviour may remain inline where it is clearer, but substantial, reusable or independently testable behaviour is extracted into focused modules and may delegate to pure application logic. Resource modules must not accumulate giant opaque callback chains or unrelated orchestration.
- **Rationale:** The Ash DSL should express the Resource contract clearly rather than hide a second application architecture inside oversized callbacks.
- **Rules:**
  1. Inline behaviour is appropriate when short, local and obvious.
  2. Reusable/complex changes, preparations, validations and calculations use named focused modules.
  3. Side effects and cross-boundary consequences are not hidden inside incidental validation/calculation callbacks.
  4. Multi-step authoritative orchestration uses the explicit action/orchestration patterns established by Architecture Law rather than nested callback surprises.
- **Failure behaviour:** Failures surface through the owning action contract with no hidden partial-success path.
- **Security/privacy:** Extracted modules do not gain independent data-access authority; actor/policy decisions stay at governed boundaries.
- **Performance/scaling:** Focused modules make expensive behaviour measurable and prevent repeated hidden queries/side effects.
- **Enforcement/downstream:** Code conventions, tests and later implementation tasks enforce module-size/dependency discipline without imposing one-module-per-rule ceremony.

## ARC-046 — Cross-boundary business interaction uses the owning Domain/application interface

- **Decision source:** AR-002 C3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-002`, `ARQ-SYS-005`, `ARQ-IAM-001`; governed by `ARC-030`, `ARC-031`
- **Decision:** Once Domain Law establishes an authoritative owner, another Domain/caller invokes that owner's approved Ash code interface/action (or other explicitly approved application contract) for business interaction. Callers do not reach through the boundary to construct arbitrary owner-internal changesets/queries, mutate its persistence directly or recreate its rules.
- **Rationale:** Ownership is meaningful only if the owner controls its mutation/application API. A modular monolith does not permit shared-write ambiguity.
- **Rules:**
  1. Cross-boundary writes always enter the owning application contract.
  2. Cross-boundary reads use approved interfaces/projections appropriate to the use case.
  3. No internal HTTP/network hop is introduced merely to respect a logical boundary.
  4. Direct Repo/table mutation across an ownership boundary is prohibited for ordinary application code.
  5. Final owners and exact interfaces remain Domain Map/Dossier work.
- **Failure behaviour:** An unavailable/failed owning operation returns an explicit failure; callers do not bypass the owner to force state.
- **Security/privacy:** The owning boundary remains responsible for authorization/minimum disclosure.
- **Performance/scaling:** In-process interfaces keep modular boundaries without microservice latency; derived read models may later remove expensive synchronous cross-boundary reads without transferring write authority.
- **Enforcement/downstream:** Domain Map eliminates shared-write ambiguity; code dependency checks/tests enforce approved interface paths.

## ARC-047 — Relationships enable governed navigation/read composition but never transfer ownership or mutation authority

- **Decision source:** AR-002 C3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-002`, `ARQ-IAM-001`, `ARQ-IAM-005`; governed by `ARC-036`, `ARC-038`, `ARC-046`
- **Decision:** Legitimate Ash relationships may cross later-approved Domain boundaries for governed loading/query/navigation where appropriate. The existence of a relationship does not transfer business ownership, authorization, policy scope or write authority; mutations still enter the authoritative owner's application interface.
- **Rationale:** Prohibiting all cross-boundary relationships would create unnecessary duplication, while treating relationships as ownership would dissolve Domain Law.
- **Rules:**
  1. Relationship traversal remains actor/policy aware.
  2. Related data is loaded only when needed and permitted.
  3. A caller may not mutate a related Resource merely because it can navigate to it.
  4. Sensitive relationship loading follows minimum-data law from `ARC-042`.
- **Failure behaviour:** Missing/forbidden related data is handled as an explicit unavailable/forbidden result rather than encouraging bypass queries.
- **Security/privacy:** Relationship convenience never expands consent, practitioner or private-record scope.
- **Performance/scaling:** Cross-boundary loads must remain bounded/preloaded deliberately; high-cost joins/read paths may use later-approved projections.
- **Enforcement/downstream:** AR-004 defines detailed field/record authorization; Domain Dossiers identify permitted cross-boundary relationships.

## ARC-048 — Application/business semantics point inward; Phoenix and provider infrastructure depend on application contracts

- **Decision source:** AR-002 C3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-002`, `ARQ-SYS-005`, `ARQ-SYS-006`, `ARQ-CONTENT-006`, `ARQ-STATE-001`; governed by `ARC-001`, `ARC-020`, `ARC-026`, `ARC-028`
- **Decision:** Core application/business logic must not require Phoenix/LiveView or concrete external-provider SDKs to define its semantics. Delivery layers and provider/infrastructure adapters depend on approved application contracts. Provider-specific code is kept at replaceable boundaries unless Product Law explicitly makes the provider itself part of the contract.
- **Rationale:** This preserves the modular-monolith benefits, testability and Railway↔VPS/S3/provider portability without imposing abstraction theatre around every trivial dependency.
- **Rules:**
  1. Business rules do not import UI framework concepts as authority.
  2. Concrete Paystack/media/object-storage/email provider details do not leak throughout Resources/actions.
  3. Provider adapters may translate between external protocols and application contracts.
  4. Introduce ports/behaviours/adapters where replaceability/testing/failure boundaries justify them, not mechanically for every module.
  5. Legacy LearnDash implementation concepts remain outside new-platform authority.
- **Failure behaviour:** Provider failure is translated into explicit application failure/degraded semantics; it does not mutate business law.
- **Security/privacy:** Provider boundaries receive the minimum permitted data and remain subject to consent/retention/deletion law.
- **Performance/scaling:** Provider abstraction must not add unnecessary network hops; in-process adapters remain appropriate in the modular monolith.
- **Enforcement/downstream:** AR-006 defines concrete external-integration boundaries; AR-003 handles storage adapters; AR-008 handles provider operations.

## ARC-049 — Shared technical primitives are allowed; shared business-semantics dumping grounds are not

- **Decision source:** AR-002 C3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-002`, `ARQ-SYS-005`; governed by `ARC-046`, `ARC-048`
- **Decision:** Genuinely generic, dependency-neutral technical primitives may be shared across the application. Business semantics, decisions and mutable truth have one authoritative owner and are accessed through that owner rather than moved into a broad `Common`, `Shared`, `Utils` or equivalent namespace merely because multiple callers use them.
- **Rationale:** Shared dumping grounds create undeclared Domains, circular dependencies and business-law duplication while appearing convenient locally.
- **Rules:**
  1. Technical helpers are stateless/generic and do not become hidden business authorities.
  2. Reuse of a business decision means calling/reusing the owner's contract or pure owned rule, not creating another copy in `Utils`.
  3. A broadly shared business concept discovered during modelling is a Domain Map question, not automatically a global library.
  4. Duplication may temporarily be preferable to premature shared abstraction where ownership is not yet established.
- **Failure behaviour:** If a shared module begins accumulating business policy/state, architecture review must assign/refine ownership rather than letting it become implicit authority.
- **Security/privacy:** Shared helpers must not become generic access paths around policy/minimum-data controls.
- **Performance/scaling:** Shared primitives remain lightweight; global mutable shared state is governed separately by AR-003/AR-005.
- **Enforcement/downstream:** Domain Map/Dossiers and architecture lint/review govern ownership and dependency structure.

## ARC-050 — Circular business authority/control dependencies are architecture defects requiring explicit resolution

- **Decision source:** AR-002 C3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-002`, `ARQ-SYS-005`, `ARQ-PERF-166`; governed by `ARC-046`, `ARC-049`
- **Decision:** Application/Domain dependencies should be clear and preferably acyclic. A circular write/control dependency is treated as an architecture smell/defect requiring explicit resolution through clearer ownership, a coordinating application operation, durable consequence/event semantics where appropriate, or Domain Map refinement. A cycle does not automatically justify a microservice.
- **Rationale:** Circular authority makes transactions, policies, failures, testing and future scaling ambiguous and often exposes unresolved ownership.
- **Rules:**
  1. Distinguish harmless compile/read references from circular business control/ownership.
  2. Do not resolve cycles through service-locator/global-access modules.
  3. Do not split into network services solely to hide a logical cycle.
  4. Cross-domain durable event/consequence patterns may break synchronous coupling only where AR-005 semantics justify them.
  5. Persistent cycles that reveal shared truth are routed to Domain Map rather than normalised.
- **Failure behaviour:** No business operation may require mutually recursive authority calls with undefined partial-failure semantics.
- **Security/privacy:** Clear ownership prevents accidental cross-policy bypass and confused-deputy paths.
- **Performance/scaling:** Acyclic/explicit coordination avoids recursive query/action amplification and makes later extraction/async decoupling safer.
- **Enforcement/downstream:** Domain Map plus AR-005 transaction/async decisions settle concrete coordination patterns; architecture tests/lint may enforce forbidden dependency directions.

### AR-002 C3 interim invariants

1. Ash Resources model coherent application/business resources rather than tables/screens.
2. Pure deterministic rules may remain ordinary Elixir; authoritative operations remain Ash-governed.
3. Resource DSL/callbacks stay focused; substantial/reusable behaviour is extracted deliberately.
4. Cross-boundary business writes enter the authoritative owner's application interface.
5. Relationships do not transfer ownership, policy or write authority.
6. Business/application semantics do not depend on Phoenix or concrete provider SDKs as authority.
7. Generic shared primitives are allowed; shared business-law dumping grounds are not.
8. Circular authority/control dependencies require explicit resolution rather than normalisation.

**Next AR-002 scope:** C4 — LiveView/realtime code boundaries and controlled framework escape hatches; then AR-002 closure audit.



## 2.4 Round C4 — LiveView Boundaries & Controlled Escape Hatches

**Accepted answer set:** `C4.1 B, C4.2 B, C4.3 B, C4.4 B, C4.5 B, C4.6 B, C4.7 B, C4.8 B`

## ARC-051 — LiveView state is reconstructible presentation/workflow state, never durable business authority

- **Decision source:** AR-002 C4.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-114`, `ARQ-PERF-116`, `ARQ-PERF-117`, `ARQ-PERF-123`, `ARQ-PERF-137`; governed by `ARC-007`, `ARC-028`
- **Decision:** LiveView socket assigns and process-local state are presentation/workflow projections and may hold bounded reconstructible state, but they never become durable business authority. After disconnect, remount, process loss, node loss, stale state, or concurrent change, correctness-sensitive state is reconstructed from authoritative application state or another explicitly approved reconstructible projection.
- **Rationale:** LiveView processes are excellent interaction processes but are intentionally ephemeral. Durable payment, entitlement, consent, health/safety, plans, inventory/capacity and other business truth must survive process loss independently.
- **Rules:**
  1. Do not persist durable business truth only in socket assigns/process memory.
  2. Remount/reconnect setup is repeat-safe and does not recreate one-time durable effects.
  3. Long-lived sockets keep bounded state; growing collections use controlled paging/streaming/projections.
  4. Socket state may optimise rendering but cannot override newer authoritative state.
- **Failure behaviour:** LiveView/process/node loss may interrupt freshness or interaction; recovery reconstructs state and never fabricates a committed business outcome.
- **Security/privacy:** Sensitive state retained in sockets is minimised and remains subject to current policy; disconnect/reconnect does not extend access.
- **Performance/scaling:** Bounded per-connection state prevents process-per-connection from becoming heavyweight session storage.
- **Enforcement/downstream:** AR-003 defines authoritative/reconstructible state classes; AR-005 defines realtime/reconciliation mechanics; AR-009 proves connection/state scale envelopes.

## ARC-052 — Browser and LiveView event parameters are untrusted intent, not authoritative facts

- **Decision source:** AR-002 C4.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-130`, `ARQ-IAM-001`, `ARQ-IAM-002`; governed by `ARC-027`, `ARC-035`, `ARC-036`
- **Decision:** All client-supplied request, form, LiveView event, hook, query-string and hidden-field values are treated as untrusted intent. IDs, prices, roles, ownership, entitlement, consent, safety, eligibility and other authoritative facts are resolved/revalidated through approved application actions and current policy before durable effects occur.
- **Rationale:** Server-rendered UI does not make round-tripped browser values authoritative. Treating the browser as a fact source would bypass the Ash action/policy boundary.
- **Rules:**
  1. Client values may identify a requested target/action but do not establish permission or business state.
  2. Current actor/policy and authoritative values are checked at the action boundary.
  3. Optimistic/UI convenience state never weakens server-side validation.
  4. Signed/opaque client tokens, where later used, remain scoped capabilities rather than universal trust.
- **Failure behaviour:** Stale/tampered input produces an explicit validation/authorization/conflict outcome and no invented success.
- **Security/privacy:** Prevents confused-deputy, IDOR and client-side privilege/price/ownership manipulation paths.
- **Performance/scaling:** Revalidation is designed as bounded authoritative work; hot-path optimisation may use safe projections but not client trust.
- **Enforcement/downstream:** AR-004 defines authentication/authorization detail; Domain Dossiers define action-specific validation; security tests include tampered/stale event inputs.

## ARC-053 — PubSub and realtime messages are observations/invalidation signals, not authoritative commits

- **Decision source:** AR-002 C4.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-039`, `ARQ-PERF-060`, `ARQ-PERF-114`, `ARQ-PERF-127`, `ARQ-PERF-128`, `ARQ-PERF-134`, `ARQ-PERF-138`; governed by `ARC-007`, `ARC-051`
- **Decision:** PubSub/realtime messages distribute observations, invalidation hints or explicitly safe projections. Receiving a message does not itself establish a durable business commit. Correctness-sensitive consumers re-read or reconcile against authoritative/versioned state where required and tolerate missing, duplicate, delayed and reordered observations.
- **Rationale:** Transient messaging is valuable for freshness but cannot provide the durable delivery/ordering guarantees required for business authority.
- **Rules:**
  1. Topic knowledge is never authorization.
  2. Payloads are minimal and privacy-appropriate.
  3. Duplicate/reordered observations do not create duplicate durable effects.
  4. Ordering-sensitive UI uses authoritative versions/sequences or refreshes current state.
  5. Exact PubSub adapter/topic design remains AR-005/AR-009 work.
- **Failure behaviour:** Lost/delayed broadcasts degrade freshness; consumers recover from authority/reconciliation rather than assuming delivery.
- **Security/privacy:** Subscription and payload disclosure remain separately authorized and minimised.
- **Performance/scaling:** Fan-out, topic scope, coalescing and refresh amplification are bounded/proved downstream rather than solved by broadcasting full records.
- **Enforcement/downstream:** AR-005 locks concrete PubSub/realtime semantics; AR-008/009 govern observability, capacity and adapter/topology proof.

## ARC-054 — LiveView async is for bounded UI work; durable/critical obligations leave the LiveView process

- **Decision source:** AR-002 C4.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-117`, `ARQ-PERF-138`, `ARQ-ASYNC-001`, `ARQ-ASYNC-002`, `ARQ-ASYNC-003`; governed by `ARC-028`, `ARC-033`, `ARC-051`
- **Decision:** LiveView async facilities may be used for bounded, reconstructible UI-oriented work where loss/retry semantics are harmless. Durable, retryable, expensive, externally consequential or business-critical background obligations leave the LiveView process and use the durable async mechanism defined by AR-005.
- **Rationale:** Process-local async improves UX but does not provide durable delivery, idempotency, reconciliation or restart semantics.
- **Rules:**
  1. A user disconnect/process crash may cancel UI-only work without violating business obligations.
  2. Payment reconciliation, governed notifications, deletion, file scanning, scheduled release and similar durable work cannot rely solely on LiveView tasks.
  3. Do not spawn arbitrary unmanaged processes as a substitute for durable async.
  4. Exact Oban worker/queue topology remains AR-005/008 work.
- **Failure behaviour:** Lost UI-only tasks are safely reconstructible; durable obligations survive caller/process loss through downstream durable mechanisms.
- **Security/privacy:** Background execution receives explicit authority/causation context under `ARC-037`; sensitive work is not smuggled into unmanaged tasks.
- **Performance/scaling:** Long/expensive work does not tie up LiveView event handling or create unbounded per-socket work.
- **Enforcement/downstream:** AR-005 decides transactions/outbox/jobs/idempotency; AR-008/009 set worker capacity/observability gates.

## ARC-055 — Phoenix components are presentation/interaction composition, not independent business-authority layers

- **Decision source:** AR-002 C4.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-002`, `ARQ-PERF-114`, `ARQ-IAM-001`; governed by `ARC-027`, `ARC-028`, `ARC-046`
- **Decision:** Function components are presentation-oriented and side-effect free. Stateful LiveComponents may own bounded UI interaction state, but authoritative operations still enter approved application/Ash interfaces. Component structure never creates an alternative Domain Map or write authority.
- **Rationale:** UI composition should remain freely evolvable without fragmenting business ownership across component trees.
- **Rules:**
  1. Components may format/render and coordinate bounded UI interaction.
  2. Components do not use Repo/direct persistence as a convenience write path.
  3. Business rules reused across components live in the owning application/pure logic boundary, not copied into UI helpers.
  4. Sensitive data passed into components follows minimum-data rules.
- **Failure behaviour:** Component/process failure affects UI state only; durable business state is preserved/reloaded.
- **Security/privacy:** Components inherit current actor/policy results and do not become bypass paths.
- **Performance/scaling:** Component boundaries are chosen for UI behaviour/performance, not treated as service/domain boundaries.
- **Enforcement/downstream:** UI implementation conventions/tests enforce no direct business persistence from components.

## ARC-056 — Direct Ecto/SQL is a controlled read/infrastructure escape hatch, not a second business-write API

- **Decision source:** AR-002 C4.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-019`, `ARQ-PERF-065`, `ARQ-PERF-066`, `ARQ-PERF-071`, `ARQ-SYS-005`; governed by `ARC-029`, `ARC-046`, `ARC-048`
- **Decision:** Where Ash cannot express a legitimate query sufficiently or a proven performance/operational need justifies a lower-level path, focused Ecto/SQL may be used behind a clearly owned application/read/infrastructure boundary. It must preserve authorization/privacy/authority/transaction/audit invariants and may not become an ordinary alternate business-write API.
- **Rationale:** Prohibiting all lower-level access would create framework dogma; allowing casual Repo access would destroy the Ash action/policy boundary.
- **Rules:**
  1. Each material escape hatch states why Ash is insufficient or materially inferior for the use case.
  2. Business writes continue through approved owner actions unless a separately approved ARC explicitly changes the authority mechanism.
  3. Read escape hatches return bounded approved projections and enforce equivalent actor/privacy rules.
  4. SQL/query design remains deterministic, bounded and performance-tested.
  5. Migrations/maintenance/infrastructure operations are separately governed and do not establish application precedent.
- **Failure behaviour:** Escape-hatch failure returns explicit application failure and cannot partially invent business state.
- **Security/privacy:** Equivalent policy/minimum-data controls are mandatory; raw SQL never implies raw data entitlement.
- **Performance/scaling:** Escape hatches are acceptable for specialised efficient queries but require evidence and must not hide N+1/unbounded retrieval.
- **Enforcement/downstream:** Architecture review/lint may maintain an escape-hatch register; AR-003/009 define data/performance specifics.

## ARC-057 — Prefer supported Ash extension/manual-action mechanisms before dropping below the application contract

- **Decision source:** AR-002 C4.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SYS-005`, `ARQ-PERF-019`; governed by `ARC-027`, `ARC-033`, `ARC-056`
- **Decision:** When ordinary Ash CRUD/action patterns do not fit, first use supported Ash custom/generic/manual action extension mechanisms where they preserve the application contract. Lower-level Elixir/Ecto/provider code may implement the operation only when justified, while the public application operation, policy, failure and authority semantics remain stable.
- **Rationale:** Framework extension should change implementation HOW, not silently relocate business authority into controllers, workers or ad-hoc persistence code.
- **Rules:**
  1. Do not force unnatural CRUD just to remain inside a default action type.
  2. Do not bypass Ash merely because an operation is unusual.
  3. Custom/manual implementations still honour actor, policy, validation and lifecycle contracts where applicable.
  4. Repeated custom patterns may justify a reusable internal abstraction only after evidence.
- **Failure behaviour:** Custom implementation errors surface through the owning action/application contract.
- **Security/privacy:** Extension points do not bypass current policy or broaden provider/data access.
- **Performance/scaling:** Specialised implementation may optimise bottlenecks while preserving measurable bounded behaviour.
- **Enforcement/downstream:** Domain Dossiers document material manual/custom action paths and their proof obligations.

## ARC-058 — Framework escape hatches are explicit, bounded and invariant-preserving

- **Decision source:** AR-002 C4.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-019`, `ARQ-SYS-005`, `ARQ-SYS-006`; governed by `ARC-048`, `ARC-056`, `ARC-057`
- **Decision:** Any material escape from the normal Phoenix/Ash/application path requires an explicit reason and bounded scope and must preserve the upstream invariants the normal framework path supplies. Repeated escape hatches around the same limitation trigger architecture review rather than silently becoming the default architecture.
- **Rationale:** Escape hatches are necessary in mature systems, but undocumented exceptions become architectural drift and can bypass authorization, audit, transactions and failure semantics.
- **Rules:**
  1. State the reason: framework expressiveness, proven performance, provider integration, specialised query/compute or another approved constraint.
  2. Preserve authority, authorization, validation, transaction, audit, privacy and failure behaviour applicable to the operation.
  3. Keep exception surface as small as practical.
  4. If invariants cannot be preserved, STOP and route an architecture conflict rather than implement the bypass.
  5. Repeated exceptions trigger reconsideration of the platform abstraction/framework boundary.
- **Failure behaviour:** Exception failure remains bounded to its declared operation and cannot silently corrupt authoritative state.
- **Security/privacy:** Escape paths receive explicit security/privacy review proportional to what framework protections they bypass.
- **Performance/scaling:** A performance-motivated escape hatch requires measurement before/after and remains removable/reviewable.
- **Enforcement/downstream:** Architectural Proof/JIT tasks identify material escape hatches; implementation review rejects undocumented bypasses.

### AR-002 C4 invariants

1. LiveView/process state is reconstructible UI/workflow state, not durable authority.
2. Browser events/params are untrusted intent; current authoritative facts/policy are resolved server-side.
3. PubSub/realtime messages are observations, not commits.
4. Durable/critical async obligations leave the LiveView process.
5. Phoenix components do not become business-authority layers.
6. Ecto/SQL remains a bounded escape hatch, never a casual second write API.
7. Supported Ash extension/manual patterns are preferred where they preserve the application contract.
8. Every material framework escape hatch is explicit, scoped and invariant-preserving.

---

# 3. AR-002 Closure Audit — Phoenix / LiveView / Ash / Code Boundaries

**Verdict:** **PASS — AR-002 COMPLETE**

## 3.1 Mechanical traceability result

The frozen ARQ register contains **103 requirements whose `Primary downstream workstreams` include AR-002**:

```text
PERF      37
AN        53
SYS        6
IAM        2
STATE      1
CONTENT    4
TOTAL     103
```

AR-002 does not need to fully implement the database/cache/realtime/authentication/analytics/content mechanisms belonging to later workstreams. Closure requires that the **Phoenix / LiveView / Ash / code-boundary part** of each requirement is decided here and that remaining mechanism work is explicitly handed downstream rather than guessed.

## 3.2 Coverage by frozen requirement surface

| Frozen ARQ surface routed to AR-002 | AR-002 Architecture Law coverage | Remaining downstream mechanism |
|---|---|---|
| Phoenix/LiveView action boundary, performance-safe code path, no hidden second business API | `ARC-027–029`, `ARC-031–034`, `ARC-044–045`, `ARC-051–058` | AR-005/008/009 prove transaction/realtime/observability/performance envelopes |
| Realtime as projection, reconstructible UI, repeat-safe remount, current action authorization, bounded socket state | `ARC-036`, `ARC-040`, `ARC-042`, `ARC-051–055` | AR-004 revocation/session mechanics; AR-005 PubSub/realtime semantics; AR-009 fan-out/capacity |
| PubSub observation, duplicate/reorder tolerance, topic not authorization, minimal payload | `ARC-036`, `ARC-039`, `ARC-053` | AR-005 topic/event/reconciliation doctrine; AR-009 topology/fan-out proof |
| N+1/unbounded collection/query escape-hatch discipline | `ARC-029`, `ARC-042`, `ARC-043`, `ARC-045`, `ARC-047`, `ARC-056`, `ARC-058` | AR-003 read models/persistence; AR-009 query/load proof |
| Controlled product spaces, shared platform versus experience, future activation, reusable platform boundaries | `ARC-030`, `ARC-043`, `ARC-046`, `ARC-048–050` plus AR-001 topology law | Domain Map assigns final owners; AR-006 handles routing/content/locale mechanisms |
| Multiple scoped roles and verified-email capability gates at the application boundary | `ARC-035–040`, `ARC-052` | AR-004 chooses authentication/session/verification mechanisms and concrete policies |
| Immutable/superseding records may not be bypassed by UI/Repo shortcuts | `ARC-027`, `ARC-029`, `ARC-046`, `ARC-056–058` | AR-003/005 define persistence/transaction/version mechanics |
| Bilingual/governed content, translation layering, risk-class publication/withdrawal, multilingual SEO | `ARC-027`, `ARC-030–031`, `ARC-043`, `ARC-046`, `ARC-048`, `ARC-052` | AR-006 defines content/translation/routing/provider mechanics |
| Analytics dashboards/targets/surveys/prediction must not gain authority through UI/code paths | `ARC-027–031`, `ARC-035–042`, `ARC-046`, `ARC-048`, `ARC-051–058` | Analytics semantics already frozen; AR-003/005/008/009 handle read models, async, observability and scale |
| Experimentation: clean UI delivery, deterministic assignment boundary, no safety/payment/auth weakening, platform-owned adapter | `ARC-027–031`, `ARC-035–040`, `ARC-048`, `ARC-051–053`, `ARC-058` | AR-003 cache/state; AR-005 assignment/exposure sequencing; AR-006 routing/content; AR-009 cache/fan-out/performance proof |

## 3.3 Boundary audit

**PASS.** AR-002 does not:

- name or freeze final business Domains/owners;
- enumerate final Ash Resources;
- define PostgreSQL tables/indexes/read models;
- choose Redis keys/TTLs or cache topology;
- choose authentication/MFA/session packages;
- define Oban queues/workers/outbox details;
- choose PubSub adapter/topic names;
- choose final content/translation resources;
- lock experiment assignment/cache implementation;
- turn Ecto/Repo into a parallel business API;
- create implementation folder/module inventories.

Those remain with `04_DOMAIN_MAP.md`, AR-003...AR-009, Domain Profiles/Dossiers and JIT implementation planning.

## 3.4 Contradiction / unresolved-choice audit

**PASS.** No Product Law contradiction or unresolved AR-002-specific material architecture choice remains.

The following are intentionally downstream, not missing AR-002 decisions:

- authentication/session/MFA/step-up/revocation implementation → AR-004;
- PostgreSQL authority/read models/cache/object storage → AR-003;
- transactions/idempotency/Oban/PubSub/realtime consequence semantics → AR-005;
- content/translation/media/provider/routing details → AR-006;
- deletion/retention/backup interaction → AR-007;
- deploy/incident/health/observability implementation → AR-008;
- query/LiveView/fan-out/multi-node capacity evidence → AR-009;
- final business ownership → `04_DOMAIN_MAP.md`.

## 3.5 AR-002 completion statement

AR-002 has established the framework/application law required for later workstreams:

```text
Phoenix / LiveView
    = delivery + interaction + reconstructible UI state

Ash code interfaces / actions
    = normal authoritative application-operation boundary

Ash policies / actor context
    = default-on current authorization boundary

ordinary Elixir
    = pure deterministic logic where framework semantics are unnecessary

Ash Domains / Resources
    = expression of later-approved Domain Law, not pre-emptive domain ownership

Ecto / SQL / manual paths
    = explicit bounded escape hatches, not parallel business authority

PubSub / realtime
    = observation and UI freshness, never durable truth
```

**AR-002 is COMPLETE.** The next Architecture Decision Workstream is:

```text
AR-003 — State Authority, Persistence, Caching & Storage
```



# 3D. AR-003 — State Authority, Persistence, Caching & Storage

## 3D.1 Round S1 — Authority & State Placement Doctrine

**Accepted answer set:** `S1.1 B, S1.2 B, S1.3 B, S1.4 B, S1.5 B, S1.6 B, S1.7 B, S1.8 B, S1.9 B`

**Scope guardrail:** S1 locks state classes, authority boundaries and storage semantics. It does **not** choose concrete table names, Resource inventory, Redis keys, TTLs, Cachex versus raw ETS, Wasabi bucket structure, AshStorage/ReqS3 dependency versions, object-storage region, exact database constraints or record-specific state machines. Those remain with later AR-003/AR-006 decisions, Domain Law, JIT Dossiers and implementation proof.

## ARC-059 — State classes have explicit authority boundaries

- **Decision source:** AR-003 S1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-042`, `ARQ-PERF-044`, `ARQ-PERF-047`, `ARQ-PERF-049`, `ARQ-PERF-063`, `ARQ-STATE-001`
- **Decision:** Use an explicit state-class authority model. PostgreSQL is the default authority for structured durable business state. Durable binary bytes live in governed object storage while PostgreSQL retains the authoritative business metadata, lifecycle and access meaning. Derived read models/projections are rebuildable from authority. Redis, ETS, CDN and browser-local state are acceleration/temporary layers only where justified. Ephemeral processing state is bounded and safe to lose/retry.
- **Rationale:** The platform must distinguish durable truth from delivery, binary storage, projection and acceleration so failure of a cache, node or object-delivery layer cannot silently redefine business state.
- **Rules:**
  1. An object existing in storage does not by itself prove entitlement, publication, approval or current lifecycle state.
  2. Cache/projection presence never substitutes for authoritative facts.
  3. Any non-PostgreSQL durable authority requires a later explicit ARC with correctness/lifecycle/recovery contract.
  4. State classification follows semantics/sensitivity, not implementation convenience.
- **Failure behaviour:** Loss of reconstructible acceleration may reduce performance/freshness but must not corrupt business truth. Loss/unavailability of durable object bytes follows the governed storage/recovery contract and may degrade file delivery without inventing metadata truth.
- **Security/privacy:** Protected/private data cannot become public merely because its bytes are stored in an object service or CDN-capable platform.
- **Performance/scaling:** Optimise authoritative access first; introduce specialised state layers only where their workload justifies them.
- **Enforcement/downstream:** AR-003 S2+ defines transactions/read models/cache mechanics; AR-006 defines upload/media/provider details; AR-007 defines deletion/retention across representations.

## ARC-060 — Business validation and database-enforceable invariants use defence in depth

- **Decision source:** AR-003 S1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-042`, `ARQ-PERF-063`, `ARQ-STATE-002`
- **Decision:** Express business validation and policy through approved Ash actions while also enforcing invariants in PostgreSQL where the database can reliably enforce them through suitable constraints or equivalent database mechanisms.
- **Rationale:** Application validation provides business semantics and useful errors; database constraints protect integrity against races, exceptional code paths and concurrent writers. Neither layer alone should be assumed sufficient for every invariant.
- **Rules:**
  1. Do not rely on check-then-write application logic for uniqueness/referential invariants that PostgreSQL can enforce atomically.
  2. Do not move all nuanced business policy into database constraints merely because constraints exist.
  3. Exact constraints/indexes belong to Domain Dossiers/schema work and require migration-safe deployment.
- **Failure behaviour:** Constraint conflicts return controlled application errors/retry outcomes; they are not treated as impossible programmer states.
- **Security/privacy:** Database integrity does not replace Ash authorisation/field privacy.
- **Performance/scaling:** Prefer database-enforced integrity over race-prone extra round trips where appropriate.
- **Enforcement/downstream:** AR-003 S2 defines concurrency/transaction rules; Domain Dossiers define concrete constraints.

## ARC-061 — Authoritative write state and derived/read state remain explicitly distinct

- **Decision source:** AR-003 S1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-043`, `ARQ-PERF-044`, `ARQ-PERF-063`, applicable frozen Analytics projection requirements
- **Decision:** Read models, materialised views, projections, search representations and analytics/dashboard structures may be shaped for efficient consumption but do not become authoritative business state merely because they are faster or easier to query.
- **Rationale:** This preserves one coherent source of durable truth while allowing high-performance read paths.
- **Rules:**
  1. Derived state must identify its authoritative dependencies and rebuild/reconciliation path.
  2. Writes to authoritative business state do not occur through a derived projection unless a later ARC explicitly defines that structure as authority.
  3. Staleness tolerance must be explicit per read model.
- **Failure behaviour:** Projection loss/staleness degrades the affected read experience; it does not erase or rewrite authoritative facts.
- **Security/privacy:** Derived stores remain subject to the same purpose/access/deletion constraints applicable to their source data.
- **Performance/scaling:** Derived read models are preferred before introducing unrelated distributed authority where they solve the measured read bottleneck.
- **Enforcement/downstream:** AR-003 S2/S3 define read-model/query/cache mechanics; Analytics Law governs analytics projections.

## ARC-062 — Caching is evidence-gated, not a default Resource layer

- **Decision source:** AR-003 S1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-043`, `ARQ-PERF-057`, `ARQ-PERF-062`, `ARQ-PERF-063`
- **Decision:** Begin with correct, efficient authoritative queries. Introduce a cache only for a known workload where measurement or a locked scale requirement demonstrates meaningful benefit and where freshness, invalidation, failure and observability contracts are explicit.
- **Rationale:** Caching can hide poor query/data design and introduces consistency/failure complexity. It is an optimisation, not the default data-access architecture.
- **Rules:**
  1. No blanket Redis/ETS cache around every Ash Resource.
  2. Optimise model/query/index/bounded retrieval before adding secondary acceleration.
  3. Cache adoption requires measurable target and later proof that it improves that target.
- **Failure behaviour:** Cache absence/failure falls back or degrades according to the specific cache contract without inventing truth.
- **Security/privacy:** Sensitive data is not cached merely because technically possible; location/access/retention must be appropriate.
- **Performance/scaling:** Cache strategy must include anti-stampede and observability where fan-out/regeneration could be material.
- **Enforcement/downstream:** AR-003 later rounds decide concrete cache patterns only where justified; AR-009 proves performance benefit.

## ARC-063 — Acceleration technology is chosen by scope and semantics

- **Decision source:** AR-003 S1.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-047` through `ARQ-PERF-052`, `ARQ-STATE-001`
- **Decision:** Choose browser-local storage, CDN, ETS/local cache or Redis according to required scope, sensitivity, consistency and failure semantics. Browser state is limited to explicitly safe convenience state; CDN is for cache-safe representations; ETS/local caches are node-local reconstructible acceleration; Redis is reserved for justified distributed acceleration/velocity/temporary coordination use.
- **Rationale:** A single universal cache technology would blur important differences between node-local, distributed, public-edge and client-side state.
- **Rules:**
  1. Redis is not mandatory merely because it is available.
  2. ETS is never assumed distributed/durable.
  3. CDN/browser caching may not expose protected/private authority.
  4. Correctness-sensitive temporary coordination is not treated as freely evictable cache.
- **Failure behaviour:** Each adopted acceleration use declares safe fallback, degradation or fail-closed semantics.
- **Security/privacy:** Placement follows sensitivity and purpose constraints.
- **Performance/scaling:** Use the narrowest/simplest layer that satisfies the measured workload and future multi-node semantics.
- **Enforcement/downstream:** AR-003 S3 will refine cache/Redis/ETS semantics; AR-006 covers CDN/object delivery.

## ARC-064 — Empty-cache correctness is mandatory

- **Decision source:** AR-003 S1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-044`, `ARQ-PERF-057`, `ARQ-PERF-061`, `ARQ-PERF-063`
- **Decision:** The platform must remain correct when ordinary caches are completely empty. Cache warm-up may affect latency/throughput but may not be a prerequisite for payment, entitlement, access, safety, identity or other authoritative correctness.
- **Rationale:** Rebuildable acceleration must be safe to lose, including after restart, deployment, purge or failure.
- **Rules:**
  1. Empty-cache behaviour is a standard architecture/performance proof case.
  2. Regeneration must be bounded/anti-stampede where high fan-out exists.
  3. Cache snapshots are not required to establish truth at startup.
- **Failure behaviour:** The system falls back to authority or deliberately degrades non-critical functionality; it must not fabricate or omit authoritative facts.
- **Security/privacy:** Revoked/withdrawn access cannot survive merely because a stale cache exists.
- **Performance/scaling:** Capacity planning must account for cold-start/empty-cache load where applicable.
- **Enforcement/downstream:** AR-008/AR-009 proof includes recovery/cold-cache cases; Domain Dossiers define material-cache invalidation.

## ARC-065 — Material historical truth is preserved through version/supersession rather than destructive overwrite

- **Decision source:** AR-003 S1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-002` and applicable immutable history requirements across finance, assessment, plan, content and professional records
- **Decision:** Where Product Law marks a record as historically material or reproducible, preserve the original fact and represent correction/change through an appropriate new version, superseding record, addendum, adjustment, reversal or similar record-specific construct. A separate current-selection/projection may identify the currently governing version.
- **Rationale:** Reproducibility, auditability and lawful correction require retaining what was originally submitted/delivered/posted rather than silently mutating history.
- **Rules:**
  1. Audit logs alone are not a substitute for the required immutable business record.
  2. Reusable methodology/content changes do not rewrite historical delivered outcomes.
  3. Exact version identifiers/state machines are Domain Law/Dossier decisions.
- **Failure behaviour:** Failed correction/version creation leaves the prior authoritative record intact.
- **Security/privacy:** Historical preservation remains subject to retention/deletion law; immutability does not mean retain everything forever.
- **Performance/scaling:** Current-state projections may optimise reads without destroying historical provenance.
- **Enforcement/downstream:** AR-003 S2/AR-005 define transactional version creation; Domain Dossiers define category-specific version semantics.

## ARC-066 — Business lifecycle and data/record lifecycle are separate dimensions

- **Decision source:** AR-003 S1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-STATE-005`
- **Decision:** Model business lifecycle separately from applicable record/data lifecycle. A record may have a business state while simultaneously being active, access-restricted, archived, deletion-pending, anonymised, deleted, retained-by-obligation or held under a legal/regulated retention state where Product Law permits.
- **Rationale:** Commercial/clinical/content state and privacy/retention state answer different questions and must not be collapsed into one generic status.
- **Rules:**
  1. Do not require one universal status enum/state machine across all Resources.
  2. Lifecycle transitions carry required authority/reason/time/policy evidence where applicable.
  3. Account closure is not synonymous with full deletion.
- **Failure behaviour:** Destructive/lifecycle workflows must be repeat-safe and may pause/retry without falsely reporting completed deletion.
- **Security/privacy:** Retained-by-obligation data is restricted from ordinary participant/marketing/personalisation use as later AR-007 law defines.
- **Performance/scaling:** Lifecycle filtering/indexing is designed per Domain workload rather than by global status convention.
- **Enforcement/downstream:** AR-007 owns deletion/retention orchestration; Domain Dossiers own concrete lifecycle state machines.

## ARC-067 — Durable files use an S3-compatible capability boundary; provider and attachment stack remain proof-gated

- **Decision source:** AR-003 S1.9 + accepted AR-003/AR-006 object-storage proof inputs
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-STATE-004`, `ARQ-CONTENT-006`, applicable upload-security requirements
- **Decision:** Durable file bytes live behind an S3-compatible object-storage capability boundary. PostgreSQL owns authoritative file business metadata, lifecycle and access state. Wasabi is a preferred provider candidate, while AshStorage + ReqS3 is the preferred Ash-native proof path; none is yet locked as irreversible provider/dependency law.
- **Rationale:** S3 compatibility and provider abstraction preserve portability while keeping file bytes outside application-local durable storage. Ash-native attachment semantics are promising but require proof against the platform's deletion, upload-security, privacy and operational requirements.
- **Rules:**
  1. Application/VPS local disk is not the durable participant/media library.
  2. Direct uploads land in restricted/quarantine state and do not become trusted/published merely because upload succeeded.
  3. DB deletion alone does not prove object/derivative deletion; deletion must be durable, retryable, reconcilable and verifiable.
  4. Ephemeral processing artefacts are not automatically stored in Wasabi/S3 durable storage.
  5. Do not introduce Waffle/ExAws as a parallel default stack unless proof identifies a requirement AshStorage/ReqS3 cannot satisfy.
  6. Provider region/data-location, retention economics, direct-upload compatibility and object-store concurrency remain explicit proof items.
- **Failure behaviour:** Object-store unavailability may delay upload/download/processing; it cannot create entitlement/publication truth. Failed deletion remains an outstanding governed obligation until reconciled.
- **Security/privacy:** Private/protected objects use governed access and short-lived delivery where applicable; upload verification/scanning gates precede publication.
- **Performance/scaling:** Prefer direct-to-object-store transfer for appropriate uploads; object-store HTTP concurrency is bounded/observable and exact client/pool tuning is deferred.
- **Enforcement/downstream:** AR-003 later rounds define storage references/lifecycle semantics; AR-006 performs provider/upload/media proof; AR-007 proves deletion propagation.

## 3D.2 S1 Consolidated State Doctrine

```text
PostgreSQL
    = default structured durable business authority

Object storage
    = durable governed binary bytes
    + never business access/publication authority by itself

Derived/read models
    = optimised projections with explicit rebuild/reconciliation

Redis / ETS / CDN / browser state
    = scoped acceleration/temporary state only where justified

Historical material records
    = immutable/superseding/versioned as required

Lifecycle
    = business state separated from privacy/retention/deletion state

Correctness
    = survives empty ordinary caches
```

**AR-003 remains IN PROGRESS.** Next: `S2 — PostgreSQL concurrency, transaction-safe persistence, query/index/read-model doctrine & migration compatibility`.


## 3.3 Round S2 — PostgreSQL Concurrency, Transactions, Queries & Migrations

**Accepted answer set:** `S2.1 B, S2.2 B, S2.3 B, S2.4 B, S2.5 B, S2.6 B, S2.7 B, S2.8 B, S2.9 B`

## ARC-068 — Concurrency control is selected by invariant, not imposed globally

- **Decision source:** AR-003 S2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-025`, `ARQ-PERF-030`, `ARQ-PERF-031`, `ARQ-PERF-032`, `ARQ-PERF-034`, `ARQ-PERF-036`, `ARQ-PERF-041`
- **Decision:** Use the narrowest PostgreSQL/application concurrency mechanism that proves the specific invariant. Prefer durable constraints or atomic mutation where sufficient; escalate through optimistic conflict/version checks, targeted row locking, stronger isolation or a specialised reservation/coordination protocol only where the access pattern and invariant require it. Do not mandate `SERIALIZABLE`, Redis locks, optimistic locking or GenServer serialisation universally.
- **Rationale:** Different invariants have different contention, latency and failure characteristics. A single universal mechanism would either under-protect critical state or impose unnecessary blocking/retry cost.
- **Rules:**
  1. Concurrency mechanism is documented with the invariant it protects.
  2. Critical correctness may not depend on cooperative application timing alone.
  3. Redis/distributed locking is not the default substitute for durable PostgreSQL enforcement.
  4. Any retryable concurrency failure follows bounded/idempotent retry rules defined in AR-005/AR-008.
- **Failure behaviour:** Contention, serialization failure or deadlock produces an explicit retryable/recoverable outcome where safe; exhaustion never invents success.
- **Security/privacy:** Concurrency controls may not bypass actor/policy checks or expose another actor's protected state while resolving conflicts.
- **Performance/scaling:** Choose the least expensive mechanism that remains correct; minimise hot locks and single serial bottlenecks.
- **Enforcement/downstream:** Domain Dossiers define concrete invariant/mechanism pairs; AR-005 defines retry/idempotency orchestration; AR-009 proves contention behaviour.

## ARC-069 — Transactions cover the smallest coherent authoritative atomic transition

- **Decision source:** AR-003 S2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-036`, `ARQ-PERF-037`, `ARQ-PERF-038`, `ARQ-PERF-040`, `ARQ-PERF-041`
- **Decision:** A database transaction encloses the smallest coherent authoritative state transition that must commit or fail atomically. Keep transactions short and bounded; do not hold database locks while waiting on Paystack, email, object storage or other slow/non-transactional providers unless a later ARC proves an exceptional safe protocol.
- **Rationale:** Short authority-focused transactions reduce lock contention/deadlocks and make provider ambiguity/crash recovery tractable.
- **Rules:**
  1. HTTP/LiveView request scope does not define transaction scope.
  2. Authoritative mutation and any required durable consequence intent that must be atomic are committed together where applicable.
  3. Non-transactional side effects are handled after durable truth through AR-005 consequence semantics.
- **Failure behaviour:** Transaction failure leaves no partial authoritative success; provider failure after commit is reconciled from durable state/intent.
- **Security/privacy:** Policy/validation context applies before/inside the authoritative mutation; transactions do not become policy-bypass zones.
- **Performance/scaling:** Avoid long-held locks, provider waits and unbounded multi-resource work inside OLTP transactions.
- **Enforcement/downstream:** AR-005 defines outbox/job/consequence boundaries; Domain Dossiers define exact transaction composition.

## ARC-070 — Race-proof invariants use durable PostgreSQL enforcement where expressible

- **Decision source:** AR-003 S2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-025`, `ARQ-PERF-030`, `ARQ-PERF-031`, `ARQ-PERF-034`, `ARQ-PERF-041`, `ARQ-PERF-064`
- **Decision:** Where a critical invariant can be represented in PostgreSQL, enforce it durably with the appropriate constraint/atomic mutation/lock/isolation mechanism in addition to Ash-facing validation and error semantics. Prior reads, disabled UI controls or cooperative process timing are not concurrency guarantees.
- **Rationale:** Database enforcement remains correct when multiple processes or future nodes race.
- **Rules:**
  1. Exact constraints and SQL mechanisms remain record/domain-specific.
  2. Ash translates/enriches durable violations into controlled application outcomes where appropriate.
  3. A cache or UI check may improve UX/performance but never replaces durable enforcement.
- **Failure behaviour:** Competing requests deterministically produce at most the permitted durable effect; losing requests fail/retry explicitly.
- **Security/privacy:** Error handling must avoid leaking protected existence/details through raw constraint errors.
- **Performance/scaling:** Prefer local durable constraints/atomic mutations over global coordination where they prove the invariant efficiently.
- **Enforcement/downstream:** JIT Domain Dossiers map critical invariants to PostgreSQL enforcement and tests.

## ARC-071 — Critical operation/idempotency evidence is durable when recovery depends on it

- **Decision source:** AR-003 S2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-026`, `ARQ-PERF-027`, `ARQ-PERF-028`, `ARQ-PERF-029`, `ARQ-PERF-040`, `ARQ-PERF-041`
- **Decision:** When retry/reconciliation correctness depends on knowing whether a critical operation already committed or remains unresolved, preserve the necessary operation/idempotency evidence in PostgreSQL or another explicitly approved durable authority. Redis/ETS/process memory may accelerate duplicate detection but cannot be the sole proof of a committed effect.
- **Rationale:** BEAM restart, cache eviction or Redis loss must not erase knowledge of payment/entitlement/other critical mutation outcomes.
- **Rules:**
  1. Business scope, key lifecycle and replay semantics remain AR-005/Domain Dossier decisions.
  2. Durable evidence distinguishes committed, not committed and legitimately unresolved states where required.
  3. Acceleration never upgrades an uncertain outcome to success.
- **Failure behaviour:** After crash/retry, the workflow reconciles against durable evidence rather than repeating blindly.
- **Security/privacy:** Idempotency evidence is minimised to the operation identity/provenance required; do not duplicate sensitive payloads unnecessarily.
- **Performance/scaling:** Index/query design must keep duplicate lookup bounded on high-volume paths.
- **Enforcement/downstream:** AR-005 defines idempotency/outbox/reconciliation contracts; Domain Dossiers define exact evidence models/retention.

## ARC-072 — Application queries are bounded and deliberate from introduction

- **Decision source:** AR-003 S2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-064`, `ARQ-PERF-065`, `ARQ-PERF-066`, `ARQ-PERF-071`, `ARQ-PERF-072`, `ARQ-PERF-084`, `ARQ-PERF-085`
- **Decision:** Known application paths must use bounded deliberate query shapes from the slice that introduces them: eliminate avoidable N+1 access, load only required data, bound growing collections, paginate deterministically, use keyset/cursor approaches where deep traversal warrants them, and batch/stream large processing rather than materialising unbounded datasets into a BEAM process.
- **Rationale:** Efficient authority is the first optimisation layer and is cheaper/safer than hiding poor query behaviour behind cache or more infrastructure.
- **Rules:**
  1. Interactive and large/reporting query classes remain distinct.
  2. Potentially unbounded collections require an explicit bound/traversal strategy.
  3. Sensitive data loading follows ARC-042 minimum-data rules in addition to performance bounds.
- **Failure behaviour:** Oversized/unbounded requests are rejected, paginated, streamed or moved to controlled async/reporting paths rather than exhausting memory/database resources.
- **Security/privacy:** Query minimisation reduces unnecessary sensitive-data exposure; pagination/filtering remains policy-authorised.
- **Performance/scaling:** Representative cardinality/distribution is required for scale-sensitive proof.
- **Enforcement/downstream:** AR-009 defines performance gates; Feature Packs/JIT Dossiers prove critical query shapes.

## ARC-073 — Indexes derive from integrity and real access-pattern evidence

- **Decision source:** AR-003 S2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-067`, `ARQ-PERF-068`, `ARQ-PERF-069`, `ARQ-PERF-070`, `ARQ-PERF-085`
- **Decision:** Design indexes from durable constraints plus actual filters, joins, ordering and critical access patterns. Use specialised multicolumn/partial/expression/covering or other indexes only where justified and validate critical/suspicious queries with representative PostgreSQL plan evidence. Do not index every column or defer all indexing until production pain.
- **Rationale:** Indexes are both correctness/performance tools and write/storage/maintenance costs; evidence must govern the trade-off.
- **Rules:**
  1. Integrity-enforcing indexes are governed by correctness, not usage frequency alone.
  2. Non-constraint indexes may be added/removed as evidence evolves.
  3. Tiny fixture performance is insufficient for scale-sensitive index decisions.
- **Failure behaviour:** A bad/unused index does not become permanent architecture; removal/change follows safe migration rules.
- **Security/privacy:** Plan/log evidence must not expose protected values unnecessarily.
- **Performance/scaling:** Query plans and index usage/cost are measured over representative distributions.
- **Enforcement/downstream:** AR-008/009 own ongoing DB observability; Domain Dossiers own concrete index contracts.

## ARC-074 — Heavy stale-tolerant reads evolve through derived projections before distributed authority

- **Decision source:** AR-003 S2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-076`, `ARQ-PERF-077`, `ARQ-PERF-078`, `ARQ-PERF-079`, `ARQ-PERF-080`, `ARQ-PERF-086`, applicable `ARQ-AN-*`
- **Decision:** Start with efficient authoritative PostgreSQL reads. When repeatable expensive stale-tolerant workloads justify it, introduce derived read models/materialised views and later read replicas or larger analytics infrastructure only as evidence requires. Correctness-sensitive read-after-write paths remain on an authority path with the required consistency.
- **Rationale:** Reporting/analytics scale must not damage OLTP correctness or force premature distributed write architecture.
- **Rules:**
  1. Derived/read models have explicit derivation, freshness, refresh/rebuild and failure semantics.
  2. Read replicas are never assumed perfectly current.
  3. Authoritative normalized state is not denormalised merely to suit one read surface.
- **Failure behaviour:** Derived projection/replica lag affects freshness of eligible workloads, not authoritative truth.
- **Security/privacy:** Read models/replicas inherit purpose/access/deletion constraints and may not become broader data copies by convenience.
- **Performance/scaling:** Progress from efficient authority to projections/replicas/partitioning only with measured need.
- **Enforcement/downstream:** Analytics architecture remains governed by ARQ-AN law; AR-009 proves OLTP isolation/freshness envelopes.

## ARC-075 — PostgreSQL connections are a finite platform-wide capacity budget

- **Decision source:** AR-003 S2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-073`, `ARQ-PERF-074`, `ARQ-PERF-075`, `ARQ-PERF-084`, `ARQ-PERF-086`
- **Decision:** Treat PostgreSQL connections as a finite system-wide capacity budget across web/application instances, worker roles and other consumers. Pool saturation uses bounded queueing/timeouts/backpressure; do not assume one connection per user or unlimited emergency pool growth. Preserve transaction-pooling compatibility where practical so PgBouncer/equivalent can be introduced later when evidence warrants it.
- **Rationale:** Horizontal application/worker scale multiplies pool demand and can overload PostgreSQL even when application CPU is healthy.
- **Rules:**
  1. Pool sizing accounts for total instance/role count and database capacity.
  2. Long-running work must not monopolise interactive connection capacity without explicit isolation.
  3. Avoid unnecessary session-local database assumptions that prevent later transaction pooling.
- **Failure behaviour:** Saturation degrades through bounded queueing/timeout/refusal rather than cascading connection exhaustion.
- **Security/privacy:** Connection/proxy architecture must preserve database authentication/TLS/secrets controls.
- **Performance/scaling:** PgBouncer is evidence-gated, not a launch requirement; pool pressure is measured before scaling.
- **Enforcement/downstream:** AR-008 defines runtime pool/proxy operations; AR-009 defines capacity tests/headroom.

## ARC-076 — Database migrations are reviewed production code and remain rolling-deployment safe

- **Decision source:** AR-003 S2.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-082`, `ARQ-PERF-155`, `ARQ-PERF-156`, `ARQ-PERF-157`, `ARQ-PERF-158`, `ARQ-PERF-085`
- **Decision:** AshPostgres-generated migrations are a useful starting mechanism, not automatic authority. Every migration is reviewed as production code. Production schema/index changes must preserve the required adjacent-version compatibility window, use expand/transition/contract evolution where needed, and receive lock/runtime/failure/deployment analysis for large or hot tables. Use appropriate online/concurrent PostgreSQL techniques where supported and safe.
- **Rationale:** Generated schema changes can be ambiguous or operationally dangerous even when semantically correct; rollout safety is part of architecture correctness.
- **Rules:**
  1. Never run an unreviewed generated migration merely because the framework emitted it.
  2. Destructive contract steps occur only after supported application versions no longer depend on old structure.
  3. Backfills are bounded/observable and separated from interactive deployment when their workload warrants it.
  4. Exact migration executor/CI/deploy tooling belongs to AR-008.
- **Failure behaviour:** Every material migration has rollback or explicit forward-recovery strategy and may block release if lock/runtime risk is unproven.
- **Security/privacy:** Migration/backfill tooling retains production access controls and must not export sensitive data casually.
- **Performance/scaling:** Hot/large-table migrations are load/lock tested against representative scale where applicable.
- **Enforcement/downstream:** AR-008 defines deployment execution/gates; JIT Dossiers/Feature Packs define migration-specific evidence.

## 3D.3 S2 Consolidated PostgreSQL Doctrine

```text
Concurrency
    = mechanism chosen by invariant

Transactions
    = smallest coherent atomic authoritative transition

Race safety
    = durable PostgreSQL enforcement where expressible

Critical replay/idempotency evidence
    = durable when crash/retry correctness depends on it

Queries
    = bounded, deliberate and minimum-data from introduction

Indexes
    = integrity + real access pattern + query-plan evidence

Heavy stale-tolerant reads
    = derived projections/read models before distributed authority

Connections
    = finite system-wide capacity budget

Migrations
    = generated where useful, always reviewed,
      expand/transition/contract safe and production-lock-aware
```

**AR-003 remains IN PROGRESS.** Next: `S3 — Cache consistency, Redis/ETS semantics, invalidation, stampede protection & distributed-state failure behaviour`.


## 3E. Round S3 — Cache Consistency, Redis/ETS & Failure Semantics

**Accepted answer set:** `S3.1 B, S3.2 B, S3.3 B, S3.4 B, S3.5 B, S3.6 B, S3.7 B, S3.8 B, S3.9 B, S3.10 B`

## ARC-077 — Node-local cache semantics are chosen before the cache library

- **Decision source:** AR-003 S3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-047`, `ARQ-PERF-048`, `ARQ-PERF-052`, `ARQ-PERF-062`
- **Decision:** Define the required node-local acceleration semantics first, then choose raw ETS, Cachex, or another abstraction only when the workload requires its specific TTL, eviction, warming, fallback, observability, or concurrency behaviour. No local-cache library is a platform-wide default merely because it is available.
- **Rationale:** Node-local cache requirements vary materially; choosing a library before semantics creates accidental coupling and unnecessary runtime machinery.
- **Rules:**
  1. Local cache contents are rebuildable and non-authoritative unless a later explicit ARC establishes a stronger contract.
  2. Raw ETS is acceptable for simple high-speed node-local lookup where its semantics are sufficient.
  3. Higher-level cache abstractions require workload justification.
- **Failure behaviour:** Local-cache loss/restart may affect latency/freshness within its declared envelope but cannot corrupt durable business truth.
- **Security/privacy:** Sensitive cache use requires explicit minimisation, scope, eviction/lifecycle, and access review; caching does not bypass policy.
- **Performance/scaling:** Measure hit/miss/regeneration behaviour before and after introducing the cache abstraction.
- **Enforcement/downstream:** Domain Dossiers/JIT work choose concrete cache libraries and limits; AR-008/009 define observability/performance proof.

## ARC-078 — Redis is optional and introduced only for justified distributed/velocity workloads

- **Decision source:** AR-003 S3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-049`, `ARQ-PERF-050`, `ARQ-PERF-051`, `ARQ-PERF-063`
- **Decision:** Redis is not a mandatory platform dependency. Introduce it only where the platform needs genuinely distributed acceleration, high-velocity shared counters/rate limits, temporary cross-process/node coordination, or another explicit access pattern that PostgreSQL and node-local state do not satisfy efficiently enough.
- **Rationale:** The launch topology is single-instance and PostgreSQL is durable authority; Redis must solve a real workload rather than becoming ritual infrastructure.
- **Rules:**
  1. A valid distributed/security/velocity requirement may justify Redis even before multiple application replicas exist.
  2. Do not move durable business truth into Redis merely to reduce database reads.
  3. Each Redis use is separately classified and justified.
- **Failure behaviour:** Every Redis use follows ARC-083 explicit fallback/degraded/fail-closed semantics.
- **Security/privacy:** Redis exposure is private; sensitive values require minimisation and purpose-specific retention/expiry.
- **Performance/scaling:** Redis introduction requires evidence that it improves the targeted workload without hiding avoidable PostgreSQL/query inefficiency.
- **Enforcement/downstream:** AR-005/008/009 and capability Dossiers define concrete Redis uses/topology when justified.

## ARC-079 — Cache freshness combines authoritative identity, explicit invalidation and bounded TTL as semantics require

- **Decision source:** AR-003 S3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-045`, `ARQ-PERF-046`, `ARQ-PERF-056`, `ARQ-PERF-058`, `ARQ-PERF-059`
- **Decision:** Cache consistency is domain-specific. Prefer authoritative version/dependency identity plus explicit invalidation where useful, with bounded TTL as an additional freshness mechanism where appropriate. Material safety, entitlement, permission, security, payment, or capacity correctness must have an immediate authoritative bypass/invalidation path and may not wait solely for TTL expiry.
- **Rationale:** TTL is a freshness aid, not a universal correctness protocol.
- **Rules:**
  1. Version-aware cache identity is preferred where governed source versions naturally define representation identity.
  2. Revocation/withdrawal paths explicitly bypass or invalidate stale material state.
  3. TTL values remain domain/evidence decisions under ARC-084.
- **Failure behaviour:** Missed invalidation may create only the declared bounded staleness; material actions re-check authoritative state where required.
- **Security/privacy:** Permission/consent revocation takes effect through an authoritative path immediately, independent of cached presentation state.
- **Performance/scaling:** Avoid global invalidation where narrower versioned/invalidation scopes suffice.
- **Enforcement/downstream:** AR-004/005/007 define revocation dependencies; Domain Dossiers define cache-specific freshness contracts.

## ARC-080 — PubSub accelerates cache freshness but is never the sole correctness mechanism

- **Decision source:** AR-003 S3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-039`, `ARQ-PERF-060`, `ARQ-PERF-134`, `ARQ-PERF-138`
- **Decision:** Phoenix PubSub may notify processes/nodes that cached or projected state changed and may trigger fast invalidation/refresh, but correctness cannot depend on every subscriber receiving every transient broadcast. Material state remains protected by authoritative reads, version identity, bounded expiry, reconciliation, or another durable mechanism.
- **Rationale:** PubSub is an observation/freshness channel, not durable delivery or storage authority.
- **Rules:**
  1. A missed PubSub message must not permanently preserve incorrect material state.
  2. Broadcast payloads should be minimal signals/projections rather than universal replicas of sensitive business records.
  3. Multi-node adapter/topology remains AR-005/009 work.
- **Failure behaviour:** PubSub outage reduces freshness/realtime convenience before it affects truth.
- **Security/privacy:** Topic/payload design must not broaden access or leak protected data.
- **Performance/scaling:** High-fan-out invalidation is scoped/coalesced to avoid broadcast amplification.
- **Enforcement/downstream:** AR-005 finalises PubSub semantics; AR-009 pressure-tests fan-out and node-loss behaviour.

## ARC-081 — Expensive/high-fan-out cache regeneration requires explicit anti-stampede control

- **Decision source:** AR-003 S3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-057`, `ARQ-PERF-061`, `ARQ-PERF-063`, `ARQ-PERF-154`
- **Decision:** Every high-fan-out or expensive-to-regenerate cached value requires a workload-appropriate anti-stampede strategy such as request coalescing/single-flight regeneration, jittered expiry, bounded regeneration, deliberate warming, or stale-while-revalidate only where the allowed staleness is safe.
- **Rationale:** Cache expiry/loss must not convert one logical miss into an uncontrolled database/dependency burst.
- **Rules:**
  1. Do not route all cache misses through one unpartitionable global GenServer/mailbox.
  2. Strategy is proportional to regeneration cost, fan-out and staleness tolerance.
  3. Cache warming is evidence-gated and bounded under ARC-086.
- **Failure behaviour:** Under regeneration pressure, bounded waiting/fallback/degraded behaviour applies rather than unlimited concurrent regeneration.
- **Security/privacy:** Stale-while-revalidate is prohibited where stale state could violate access/safety/security/payment/entitlement truth.
- **Performance/scaling:** Stampede controls are tested under cold-cache/restart/spike workloads.
- **Enforcement/downstream:** AR-009 defines load proof; Dossiers select exact coalescing/warming mechanisms.

## ARC-082 — Evictable cache and correctness-sensitive Redis coordination are separate semantic classes

- **Decision source:** AR-003 S3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-049`, `ARQ-PERF-050`, `ARQ-PERF-051`, `ARQ-PERF-052`
- **Decision:** Freely evictable cache state and correctness-sensitive temporary coordination state are distinct semantic classes even if one Redis deployment initially hosts both. Cache loss is acceptable by design; coordination state requires an explicit persistence, eviction, recovery, expiry and failure contract and may later require stronger isolation/topology.
- **Rationale:** Sharing a product/engine does not make the semantics or safe failure modes equivalent.
- **Rules:**
  1. Coordination state may not inherit a cache eviction policy by accident.
  2. If losing a value is catastrophic, it is not an ordinary cache.
  3. Separate Redis instances/services are introduced only when workload/risk evidence warrants them.
- **Failure behaviour:** Cache eviction causes a miss/rebuild; coordination loss follows its declared protocol rather than silently inventing success.
- **Security/privacy:** Sensitive coordination state is minimised and separately access/expiry-governed.
- **Performance/scaling:** Memory budgets/eviction pressure are observable by semantic class.
- **Enforcement/downstream:** AR-005 owns correctness-sensitive coordination protocols; AR-008 owns operational isolation when introduced.

## ARC-083 — Every Redis-backed capability declares fallback, degraded, or fail-closed behaviour

- **Decision source:** AR-003 S3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-050`, `ARQ-PERF-051`, `ARQ-PERF-052`, `ARQ-PERF-063`
- **Decision:** Each Redis-backed capability explicitly declares what happens when Redis is unavailable: (1) safe authoritative fallback, (2) deliberate degraded/queued/lower-freshness behaviour, or (3) fail closed where continuing would violate a correctness/security invariant. There is no universal fallback policy.
- **Rationale:** Redis outage semantics depend on why Redis is present; a blind fallback can be as unsafe as a blind outage.
- **Rules:**
  1. Fallback may not infer business truth from caller/browser data.
  2. A capability that fails closed must expose observable degraded health and recover/reconcile deliberately.
  3. Unrelated platform capabilities should continue when safe.
- **Failure behaviour:** Behaviour is deterministic and capability-specific rather than accidental timeout cascades.
- **Security/privacy:** Security/rate/permission controls cannot silently become fail-open merely because Redis is unavailable.
- **Performance/scaling:** Fallback paths are load-tested so a Redis outage does not create an uncontrolled PostgreSQL stampede.
- **Enforcement/downstream:** AR-005/008/009 and relevant Dossiers record the concrete mode and proof.

## ARC-084 — Cache TTL is domain-derived, not a platform-wide constant

- **Decision source:** AR-003 S3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-045`, `ARQ-PERF-056`, `ARQ-PERF-058`, `ARQ-PERF-059`
- **Decision:** TTL is derived per cache from source volatility, tolerated staleness, regeneration cost, invalidation reliability, access/privacy risk and load behaviour. No universal platform TTL exists, and some version-keyed/explicitly-invalidated caches may not need a conventional TTL.
- **Rationale:** A single time value cannot correctly represent materially different business semantics.
- **Rules:**
  1. TTL never substitutes for immediate material revocation under ARC-079.
  2. Long TTL requires stronger version/invalidation reasoning where source may change.
  3. Exact numbers remain Domain Dossier/evidence decisions.
- **Failure behaviour:** Expiry causes bounded miss/regeneration rather than authority loss.
- **Security/privacy:** Private access-sensitive representations receive stricter freshness/revocation treatment than ordinary public content.
- **Performance/scaling:** TTL/jitter choices are evaluated against stampede and regeneration load.
- **Enforcement/downstream:** Dossiers/gates record TTL rationale and tests for material caches.

## ARC-085 — `:persistent_term` is restricted to very read-heavy, near-immutable VM-wide values

- **Decision source:** AR-003 S3.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-055`, `ARQ-PERF-063`
- **Decision:** Permit `:persistent_term` only for values that are read extremely frequently, are VM-wide, and never or very rarely change, where its specialised update cost is understood. It is not a general cache and must not hold frequently changing prices, permissions, eligibility, health/safety rules, entitlements, experiment assignments, or equivalent governed runtime state.
- **Rationale:** `:persistent_term` is a specialised VM primitive whose strengths and update costs do not suit ordinary changing business state.
- **Rules:**
  1. Candidate use requires an explicit reason beyond micro-optimisation preference.
  2. Values remain reconstructible/config-derived unless another approved authority exists.
  3. Avoid large/frequently replaced terms that create disruptive update behaviour.
- **Failure behaviour:** BEAM restart reconstructs the values from approved source/configuration.
- **Security/privacy:** Do not place sensitive per-user state in VM-wide persistent terms.
- **Performance/scaling:** Use only after profiling/clear hot-read need where ordinary module constants/config/ETS are insufficient.
- **Enforcement/downstream:** Code review/static architecture checks may flag inappropriate uses.

## ARC-086 — Cache warmth is not a readiness or correctness prerequisite

- **Decision source:** AR-003 S3.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-061`, `ARQ-PERF-154`, `ARQ-PERF-144`, `ARQ-PERF-063`
- **Decision:** The platform must start and operate correctly with empty caches. Full cache warmth is not part of readiness. Only caches with evidence-backed warming needs may be warmed, and warming must be bounded/staggered/coordinated so simultaneous starts or cache loss do not stampede PostgreSQL or external dependencies.
- **Rationale:** Rebuildable acceleration cannot become a hidden startup authority requirement.
- **Rules:**
  1. Readiness requires safe mandatory initialization, not a target cache hit rate.
  2. Cold-cache behaviour is a standard test condition.
  3. Multi-replica startup must avoid duplicate full regeneration.
- **Failure behaviour:** Cold starts may be slower within protected capacity but remain correct; overload is bounded rather than unsafe.
- **Security/privacy:** Warming must not bulk-load sensitive data beyond legitimate need or bypass normal policy boundaries.
- **Performance/scaling:** Cold-start, cache-loss and multi-node-start scenarios are included in performance/recovery proof.
- **Enforcement/downstream:** AR-008 readiness design and AR-009 load/failure testing prove this invariant.

## 3E.1 S3 Consolidated Cache Doctrine

```text
Cache library
    = semantics first, library second

Redis
    = optional / justified, never universal authority

Freshness
    = version/dependency identity + invalidation + TTL as appropriate

Material revocation
    = immediate authoritative path

PubSub
    = freshness accelerator, not correctness authority

Stampedes
    = deliberately bounded

Redis semantic classes
    = evictable cache != correctness-sensitive coordination

Redis outage
    = explicit fallback / degraded / fail-closed per capability

TTL
    = domain-derived, never universal

:persistent_term
    = rare, read-heavy, near-immutable VM state only

Cold start
    = correct with empty caches
```

**AR-003 remains IN PROGRESS.** S4 is accepted below. Two user-raised refinements remain to be locked separately: default opaque identifier type (UUIDv7 candidate) and independent binary-redundancy/failsafe topology.

## 3F. AR-003 S4 — Object Storage, Upload Security & File Lifecycle

**Accepted answer set:** `S4.1 B, S4.2 B, S4.3 B, S4.4 B, S4.5 B, S4.6 B, S4.7 B, S4.8 B, S4.9 B, S4.10 B, S4.11 B`

## ARC-087 — PostgreSQL owns file business metadata; S3-compatible storage owns durable binary bytes

- **Decision source:** AR-003 S4.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-CONTENT-006`, `ARQ-PERF-042`
- **Decision:** PostgreSQL remains authoritative for file ownership/reference, access classification, lifecycle, content metadata, checksum/integrity evidence, scan/approval state, version/provenance, object identity, derivative relationships and deletion state. S3-compatible object storage holds the durable binary bytes. Object existence alone does not establish approval, publication, entitlement or active business state.
- **Rationale:** Separating structured business authority from blob storage preserves policy correctness, provider portability and efficient durable binary handling.
- **Failure behaviour:** Missing/unavailable bytes create an explicit storage/recovery condition; the platform must not fabricate availability from metadata.
- **Security/privacy:** Private/protected classification remains application-authoritative.
- **Performance/scaling:** Large blobs do not burden ordinary OLTP row/query paths.
- **Enforcement/downstream:** AR-006/007/008 and Dossiers define file classes, retention and operational recovery.

## ARC-088 — Suitable user uploads prefer direct presigned browser-to-object-storage transfer

- **Decision source:** AR-003 S4.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-SEC-002`, `ARQ-PERF-063`
- **Decision:** Suitable user files should normally transfer directly from the browser to S3-compatible storage under short-lived, narrowly scoped presigned authority created only after platform authorisation. Server-mediated uploads remain valid for workflows that genuinely require server custody or are simpler/smaller.
- **Rationale:** Avoid unnecessary double handling of large binaries by Phoenix while retaining platform control of upload authority.
- **Failure behaviour:** Failed/expired uploads remain incomplete and do not create approved attachments.
- **Security/privacy:** Permanent object credentials are never exposed to browsers.
- **Performance/scaling:** Protects application bandwidth/memory and supports future horizontal scale.
- **Enforcement/downstream:** Architectural Proof validates presigning, limits, cancellation/retry and provider compatibility.

## ARC-089 — Direct uploads land untrusted/restricted until governed approval

- **Decision source:** AR-003 S4.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SEC-002`, `ARQ-STATE-001`
- **Decision:** Direct uploads enter a restricted/quarantine state. Successful byte transfer proves only arrival. Files may become approved/published/protected-deliverable only after the required verification pipeline succeeds.
- **Rationale:** Transport success is not safety or publication approval.
- **Failure behaviour:** Failed or unresolved verification remains quarantined/rejected; no unsafe fallback to publication.
- **Security/privacy:** Quarantine is private/non-public by default.
- **Performance/scaling:** Heavy verification may be durable async work.
- **Enforcement/downstream:** AR-006/008 define exact state transitions/scanner integration.

## ARC-090 — Upload approval uses risk-appropriate content/safety verification

- **Decision source:** AR-003 S4.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SEC-002`, `ARQ-STATE-001`
- **Decision:** Before an untrusted upload becomes governed/approved, apply applicable size limits, actual type/MIME/signature checks, checksum/integrity verification, malware/security scanning, metadata sanitisation, media/document validation, derivatives/transformation and policy/publication approval.
- **Rationale:** Filename extensions and provider acceptance cannot establish safety.
- **Failure behaviour:** Verification failure is explicit and retry/review behaviour is bounded; unsafe content never silently publishes.
- **Security/privacy:** Minimise metadata leakage and prevent malicious content serving.
- **Performance/scaling:** Expensive processing moves to bounded durable async execution.
- **Enforcement/downstream:** Exact scanners/analyzers/libraries remain proof/JIT choices.

## ARC-091 — Object identities are opaque, collision-safe and non-sensitive

- **Decision source:** AR-003 S4.5
- **Status:** ACCEPTED — AMENDED BY `ARC-098`
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-SEC-002`
- **Decision:** Object storage identities/keys use opaque, collision-safe, non-sensitive internal identifiers. Human filenames and business/PII semantics remain governed metadata and are not embedded unnecessarily in object keys.
- **Rationale:** Storage keys should not leak participant identity, clinical meaning or mutable naming semantics.
- **Rules:** Browser/user input does not choose authoritative final keys; public-facing identifiers need not equal internal object identity.
- **Failure behaviour:** Key collision must be safely rejected/regenerated rather than overwrite another logical object.
- **Security/privacy:** Avoid email/name/health/document semantics in keys.
- **Performance/scaling:** Key layout may later include non-sensitive distribution prefixes if evidence warrants it.
- **Enforcement/downstream:** Identifier-type refinement was resolved explicitly by `ARC-098`; this ARC remains the governing opacity/non-sensitivity rule.

## ARC-092 — Protected downloads authorise first, then use short-lived delivery capability

- **Decision source:** AR-003 S4.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-CONTENT-006`, applicable IAM requirements
- **Decision:** Protected download requests are authorised by the platform against current policy/entitlement before issuing a short-lived signed/redirected object-delivery capability. Public assets are a separate deliberately published class.
- **Rationale:** Avoid proxying every large byte while keeping access authority in the application.
- **Failure behaviour:** Signing/provider failure surfaces explicit temporary unavailability; it never grants broader access.
- **Security/privacy:** Signed URLs are temporary capabilities, not entitlement truth.
- **Performance/scaling:** Object storage/CDN may serve bytes after authorisation.
- **Enforcement/downstream:** AR-006/007 define expiry/logging/revocation classes.

## ARC-093 — Physical file deletion is durable, retryable, observable and reconcilable

- **Decision source:** AR-003 S4.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-STATE-006`
- **Decision:** Database lifecycle change alone does not prove physical deletion. Governed deletion tracks durable obligations across originals, variants, previews, superseded objects, temporary derivatives, extracted/indexed values, cache/signed-link capability and applicable processors until required consequences are verified/reconciled.
- **Rationale:** Object operations can fail independently of database transactions.
- **Failure behaviour:** Incomplete deletion remains explicit/pending and is retried/reconciled idempotently rather than falsely marked complete.
- **Security/privacy:** Access is removed as required while deletion completes; retained-by-law classes remain separately governed.
- **Performance/scaling:** Deletion fan-out is bounded/durable async where needed.
- **Enforcement/downstream:** AR-007 owns full deletion/retention/backup interaction.

## ARC-094 — AshStorage + ReqS3 is the preferred attachment-stack Architectural Proof candidate

- **Decision source:** AR-003 S4.8
- **Status:** ACCEPTED / PROOF_GATED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-STATE-004`, `ARQ-SEC-002`
- **Decision:** Promote AshStorage + ReqS3 to the preferred Ash-native attachment implementation candidate, but do not lock the dependency until proof covers custom S3 endpoints/Wasabi, direct uploads, quarantine, protected delivery, checksums, variants, deletion failure/reconciliation, orphan detection, tests, bounded large-file concurrency and provider portability.
- **Rationale:** It aligns with the Ash-first architecture while documented non-transactional physical deletion/orphan concerns require explicit hardening proof.
- **Failure behaviour:** Failure of proof preserves the S3 capability contract and permits another implementation without changing domain semantics.
- **Security/privacy:** Proof includes protected delivery and upload security boundaries.
- **Performance/scaling:** Proof includes direct-upload and concurrency behaviour.
- **Enforcement/downstream:** Waffle/ExAws remain fallback candidates, not parallel defaults.

## ARC-095 — Wasabi is a preferred initial S3-compatible provider candidate, not platform law

- **Decision source:** AR-003 S4.9
- **Status:** ACCEPTED / PROVIDER_PROOF_GATED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-CONTENT-006`, `ARQ-PERF-161`
- **Decision:** Wasabi remains the preferred initial durable-object provider candidate behind the S3-compatible capability boundary, subject to privacy/data-location, performance, contract, operations, recovery and cost proof. Application/domain semantics must not unnecessarily depend on Wasabi-specific behaviour.
- **Rationale:** S3 compatibility provides portability while provider economics/location are operational facts.
- **Failure behaviour:** Provider outage/degradation follows explicit storage-class availability/recovery semantics.
- **Security/privacy:** Data-location and processor obligations must pass AR-006/007 review.
- **Performance/scaling:** Durable object workloads and temporary/scratch workloads may use different storage classes/providers.
- **Enforcement/downstream:** Revalidate region, pricing, durability and contractual evidence at provider lock.

## ARC-096 — Object Lock/immutability is retention-class-specific, never universal

- **Decision source:** AR-003 S4.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-004`, `ARQ-STATE-005`, `ARQ-STATE-006`
- **Decision:** Do not universally enable immutable retention/Object Lock for ordinary participant-deletable objects. Apply immutable storage only where an approved backup/evidence/legal retention class requires it and where deletion law is compatible.
- **Rationale:** Universal immutability could make legitimately deletable participant data technically undeletable for the retention interval.
- **Failure behaviour:** Retention conflicts are blocking architecture/compliance issues, not silently ignored deletion failures.
- **Security/privacy:** Legal hold/retention remains scoped and expert-governed.
- **Performance/scaling:** Storage-cost implications are assessed per class.
- **Enforcement/downstream:** AR-007/008 define retention/backup buckets and controls.

## ARC-097 — Derivatives have explicit source lineage and lifecycle

- **Decision source:** AR-003 S4.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-004`, `ARQ-SEC-002`, `ARQ-CONTENT-006`
- **Decision:** Every thumbnail, preview, resized/transcoded output, extracted metadata/index artefact or other derivative is either explicitly rebuildable or itself governed durable state and has discoverable lineage to its source. Supersession/deletion must handle all applicable derivatives.
- **Rationale:** Invisible derivative residue breaks deletion, provenance and correction guarantees.
- **Failure behaviour:** Missing derivative can be regenerated only where declared rebuildable; orphaned/unknown derivatives become reconciliation defects.
- **Security/privacy:** Derivatives inherit appropriate sensitivity/access constraints and cannot become public accidentally.
- **Performance/scaling:** Regeneration strategies are bounded and may use async processing/caching.
- **Enforcement/downstream:** AshStorage variant support is proof input, not sole lifecycle authority.

## ARC-098 — UUIDv7 is the default internal opaque identifier type

- **Decision source:** AR-003 S4-R1 user refinement accepted 2026-08-17; explicit amendment to `ARC-091`.
- **Status:** ACCEPTED / AMENDS `ARC-091`
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-SEC-002`
- **Decision:** Use UUIDv7 as the default platform-generated internal opaque identifier where no stronger domain-specific, externally mandated, or protocol-specific identifier is required, including logical object/file identities. UUIDv7 identifies an object/record; it is not an access secret, bearer capability, authorisation token, or proof of entitlement. Public/signed access capabilities use separately generated bounded credentials/tokens.
- **Rationale:** UUIDv7 preserves globally unique opaque identity while providing time-ordered identifiers that are operationally and index-friendly compared with purely random identifiers, without embedding human/business/PII semantics.
- **Rules:** Do not infer authorisation or confidentiality from identifier obscurity. Do not expose UUID timestamp ordering where a workflow requires stronger unlinkability; such cases may use a different external/public identifier while retaining an internal UUIDv7.
- **Failure behaviour:** Identifier collision or malformed identity is rejected safely; no existing logical object may be overwritten by identifier reuse.
- **Security/privacy:** UUIDv7 timestamp information is not secret and must not encode participant names, email addresses, clinical meaning, filenames, roles or other sensitive semantics.
- **Performance/scaling:** Time ordering supports index locality and operational sorting while remaining compatible with distributed generation.
- **Enforcement/downstream:** Domain Dossiers may justify another identifier for a specific business/protocol requirement; storage key/prefix layout remains implementation work.

## ARC-099 — File recovery uses storage-class replicas, not routine PostgreSQL byte duplication

- **Decision source:** AR-003 S4-R2 user refinement accepted 2026-08-17.
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-STATE-004`, `ARQ-STATE-006`, `ARQ-OPS-002`
- **Decision:** Do not routinely duplicate durable object bytes into PostgreSQL as an object-storage outage fallback. PostgreSQL remains the authoritative file manifest and records the logical file identity, integrity/checksum evidence, governed lifecycle/access state, primary object reference and replica/recovery status. Storage classes whose recovery requirements justify it receive an independent secondary object copy/replica in an appropriate separate storage failure domain.
- **Rationale:** Duplicating large binary payloads into PostgreSQL would enlarge and couple the critical OLTP/recovery surface without providing the cleanest independent object-storage failure boundary. File durability is better expressed as independently recoverable object copies while PostgreSQL records what must exist and its verified state.
- **Rules:** Rebuildable derivatives need not receive independent replicas when their source is recoverable. Irreplaceable participant/professional/legal artefacts may require stronger replica classes. Same-provider cross-region replication may be useful but does not automatically satisfy every provider-level disaster requirement; higher-criticality classes may require a different account/provider/failure domain. Small specialised binary-in-PostgreSQL cases require explicit Domain/Architecture justification rather than becoming the default file model.
- **Failure behaviour:** Primary object-store failure follows the storage class's explicit recovery/failover behaviour. If no approved replica is available, the file is explicitly unavailable/recovering; the platform must not fabricate bytes or treat stale/unchecked data as verified. Replica drift/missing copies become reconciliation defects.
- **Security/privacy:** Replicas inherit the source sensitivity, encryption/access and deletion/retention obligations. Deletion/supersession must discover and handle every eligible replica; lawful retained copies remain separately governed.
- **Performance/scaling:** Keeps large binary throughput/storage out of the OLTP database and permits independent object-store scaling/recovery.
- **Enforcement/downstream:** AR-007/AR-008 define storage classes, replica topology, backup/restore/failover verification and provider independence; exact table/resource names and replication products remain deferred.

## 3F.1 S4 Consolidated Storage Doctrine

```text
PostgreSQL
    = authoritative file metadata / policy / lifecycle

S3-compatible object storage
    = durable binary bytes

Direct uploads
    = short-lived presigned capability where suitable

Arrival
    != approval

Quarantine
    -> inspect / scan / sanitise / verify
    -> governed attachment

Protected delivery
    = authorise first, short-lived signed/redirected bytes second

Deletion
    = durable obligation + reconciliation, not DB-row deletion alone

AshStorage + ReqS3
    = preferred proof candidate, not dependency law yet

Wasabi
    = preferred provider candidate behind S3 boundary

Object Lock
    = retention-class-specific only

Derivatives
    = explicit lineage + lifecycle

Internal opaque identifiers
    = UUIDv7 by default; identity is not an access secret

File recovery
    = PostgreSQL manifest + storage-class object replicas where justified;
      no routine PostgreSQL byte duplication
```

**Resolved S4 refinements accepted on 2026-08-17:**
1. `ARC-098` makes UUIDv7 the default platform-generated internal opaque identifier type, while keeping access capabilities/secrets separate and allowing explicit domain/protocol exceptions.
2. `ARC-099` rejects routine PostgreSQL duplication of object bytes and instead uses PostgreSQL as the authoritative file manifest plus storage-class-specific independent object replicas where recovery requirements justify them.

**AR-003 remains IN PROGRESS.** Proceed to the compact S5 client/CDN/storage-class boundary round and then AR-003 closure audit.


## 3G. AR-003 S5 — Browser State, CDN/Public Caching & Storage-Class Boundaries

**Accepted answer set:** `S5.1 B, S5.2 B, S5.3 B, S5.4 B, S5.5 B, S5.6 B, S5.7 B, S5.8 B, S5.9 B, S5.10 B`

## ARC-100 — Browser-local persistence is limited to explicitly safe non-authoritative convenience state

- **Decision source:** AR-003 S5.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, applicable IAM/privacy requirements, `ARQ-PERF-063`
- **Decision:** Browser-local persistence may hold only explicitly safe, non-authoritative client convenience state. Sensitive business truth, health information, permissions, entitlements, privileged state, payment state, durable operation truth and other governed authoritative facts remain server-authoritative and are not stored in ordinary browser-local persistence merely for convenience.
- **Rationale:** Client storage persists independently of server authority and is exposed to the browser execution environment; it must not become an undeclared authority or sensitive offline-data store.
- **Rules:**
  1. Safe UI preferences may be stored locally where useful.
  2. Browser-local presence never proves current permission, entitlement, payment, consent or workflow completion.
  3. Authentication-session/token representation remains AR-004 work.
  4. A future requirement for offline protected data requires a separate explicit architecture decision covering device trust, encryption/key custody, expiry, revocation, deletion and synchronisation.
- **Failure behaviour:** Loss/eviction/corruption of ordinary client-local state may affect convenience only; authoritative state is re-derived from approved server sources.
- **Security/privacy:** Sensitive/protected records are not copied into ordinary local persistence by default.
- **Performance/scaling:** Client-side persistence may reduce harmless UI repetition without creating correctness coupling.
- **Enforcement/downstream:** AR-004 governs auth/session state; AR-006 governs content delivery; AR-007 governs deletion implications.

## ARC-101 — Browser/service-worker caching is restricted to public or explicitly safe responses by default

- **Decision source:** AR-003 S5.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-STATE-004`, `ARQ-PERF-063`
- **Decision:** Browser and service-worker caches may persist public/static application resources and other explicitly safe responses. Participant-specific sensitive/protected responses are not persistently cached client-side by default. Offline protected-data support, if later required, is a separate architecture problem rather than an accidental consequence of generic web caching.
- **Rationale:** Persistent browser caches are not a trustworthy durable authority and can create difficult revocation/deletion residue for sensitive data.
- **Failure behaviour:** Cache eviction or absence must not remove authoritative capability; public/safe resources are re-fetched.
- **Security/privacy:** Private health, plan, entitlement, security, paid or practitioner-shared responses are excluded from ordinary persistent client caches.
- **Performance/scaling:** Public/static client caching remains available for latency/bandwidth savings.
- **Enforcement/downstream:** AR-006/007 define response/cache headers and any future offline-sensitive-data contract.

## ARC-102 — Immutable/versioned public assets may use aggressive browser/CDN caching

- **Decision source:** AR-003 S5.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-056`, `ARQ-PERF-058`, `ARQ-STATE-001`, `ARQ-CONTENT-005`
- **Decision:** Approved public static assets should prefer immutable/versioned/content-addressed identity where practical so browsers/CDNs can cache aggressively without making expiry the correctness mechanism. Changed immutable content receives a new identity/version. Mutable public representations use their own explicit freshness/invalidation contract.
- **Rationale:** Version-aware identity makes stale immutable assets harmless and reduces reliance on global purges or short universal TTLs.
- **Failure behaviour:** CDN/cache loss affects performance only; origin/authoritative publication metadata remains governing.
- **Security/privacy:** Only deliberately public assets use this public-cache class.
- **Performance/scaling:** Supports high cache hit rates and efficient global delivery without authority ambiguity.
- **Enforcement/downstream:** AR-006/008 define exact publication headers/CDN rules; TTL values remain evidence/domain-derived.

## ARC-103 — Shared CDN caching of dynamic/personalised responses is opt-in by response class

- **Decision source:** AR-003 S5.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-PERF-045`, `ARQ-AN-213`
- **Decision:** Dynamic authenticated, personalised or protected responses are not shared-CDN-cache eligible by default. Shared caching is opt-in only when the response class has an explicitly proven cache key, privacy boundary, staleness envelope and invalidation/version contract. Public responses may deliberately opt into shared caching.
- **Rationale:** A shared edge cache is a cross-user distribution surface; privacy must not depend on incidental provider defaults.
- **Failure behaviour:** Uncertain cache classification fails toward origin/non-shared delivery rather than risking cross-user leakage.
- **Security/privacy:** Edge/provider configuration may not silently convert protected/personalised content into public/shared cache entries.
- **Performance/scaling:** Public cache-safe responses may still gain CDN scale; sensitive dynamic traffic remains origin/application-governed unless explicitly proven safe.
- **Enforcement/downstream:** AR-006/008 define concrete Cloudflare/cache-rule implementation and tests.

## ARC-104 — Experiment-sensitive HTML bypasses shared full-page caching unless variant-safe partitioning is explicitly proven

- **Decision source:** AR-003 S5.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-213`, `ARQ-AN-214`, `ARQ-AN-187`, `ARQ-CONTENT-005`
- **Decision:** Initial architecture bypasses shared full-page caching for experiment-sensitive HTML. A later optimisation may partition shared cache entries by a stable safe internal assignment dimension only after proving that one experimental unit's treatment cannot be served to another and without exposing treatment identity in canonical public URLs. Static/public assets remain normally cacheable.
- **Rationale:** The simplest correct launch contract is to avoid a shared full-page treatment cache until its partition semantics are worth the complexity.
- **Failure behaviour:** Cache purge/loss/deployment must not rebucket an already governed exposed unit or fabricate exposure.
- **Security/privacy:** Internal experiment identity is not leaked into normal public URLs/cache keys exposed to users/search engines.
- **Performance/scaling:** Full-page caching may be added later through evidence-backed variant-safe partitioning if needed.
- **Enforcement/downstream:** AR-005/009 govern assignment/exposure correctness and performance proof.

## ARC-105 — Protected media is authorised first; delivery capability is short-lived and non-authoritative

- **Decision source:** AR-003 S5.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-CONTENT-006`, applicable IAM requirements
- **Decision:** Protected media delivery begins with a current application policy/entitlement check. On success, the platform may issue a short-lived signed/redirected delivery capability so object storage/CDN can serve bytes efficiently. A CDN may accelerate protected bytes only when its private-delivery/cache contract proves that one user's authorisation cannot expose content to another unauthorised user. Signed delivery capability never becomes entitlement authority.
- **Rationale:** Delivery infrastructure may move bytes; the platform retains access/policy authority.
- **Failure behaviour:** Provider/signing failure produces explicit temporary unavailability, not an unauthorised fallback.
- **Security/privacy:** Public/unguessable URLs are not a substitute for authorisation; protected assets remain private by class.
- **Performance/scaling:** Large protected bytes can bypass Phoenix after authorisation while preserving policy boundaries.
- **Enforcement/downstream:** AR-004/006 define access policy and delivery implementation; AR-008 validates provider/CDN configuration.

## ARC-106 — Storage security/lifecycle classes are explicit and independent of business-domain boundaries

- **Decision source:** AR-003 S5.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-STATE-004`, `ARQ-SEC-002`, `ARQ-CONTENT-006`
- **Decision:** Define explicit storage security/lifecycle classes independent of business-domain ownership. At minimum the architecture recognises conceptual classes for `PUBLIC_APPROVED`, `PROTECTED`, `QUARANTINE`, `EPHEMERAL_PROCESSING`, `DURABLE_SOURCE`, and `RETAINED/RECOVERY`. Classes may use different buckets, namespaces, accounts, providers or lifecycle controls when security, deletion, recovery or cost semantics justify separation.
- **Rationale:** Public/protected/quarantine/recovery semantics must not collapse merely because all objects use an S3-compatible API.
- **Rules:** One physical bucket is not one semantic class; one business Domain is not automatically one storage class.
- **Failure behaviour:** Misclassified or unknown objects fail toward restricted handling/reconciliation rather than public exposure.
- **Security/privacy:** Class controls inherit appropriate access, encryption, retention and deletion obligations.
- **Performance/scaling:** Physical topology may evolve by class without rewriting business semantics.
- **Enforcement/downstream:** AR-006/007/008 and Domain Dossiers define exact mappings, bucket topology and provider choices.

## ARC-107 — Cache purge/invalidation accelerates freshness but never establishes authoritative state

- **Decision source:** AR-003 S5.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-045`, `ARQ-PERF-056`, `ARQ-PERF-060`, `ARQ-STATE-001`
- **Decision:** Browser/CDN/application cache purge is a freshness mechanism, not an authoritative state transition. Prefer immutable/version-aware identity where possible; use targeted invalidation/purge for mutable representations where useful; preserve authoritative state/policy as the correctness source.
- **Rationale:** A successful purge cannot prove that business state changed, and a missed purge must not create durable corruption.
- **Failure behaviour:** Failed/missed invalidation may temporarily reduce freshness only within the declared safe envelope; correctness-sensitive paths use authoritative bypass/version checks.
- **Security/privacy:** Revocation-sensitive/private state cannot rely only on eventual edge expiry.
- **Performance/scaling:** Targeted invalidation avoids unnecessary global purge load while preserving cache efficiency.
- **Enforcement/downstream:** AR-006/008 define provider-specific purge/cache-key mechanisms and observability.

## ARC-108 — Protected delivery capabilities have an explicit residual-access/revocation envelope

- **Decision source:** AR-003 S5.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-001`, `ARQ-STATE-004`, `ARQ-PERF-046`, applicable IAM consent/revocation requirements
- **Decision:** Every protected delivery class defines the residual-access envelope of already-issued signed/bearer delivery capabilities. New capabilities always require current authority. Where a capability cannot be individually revoked, its lifetime must be short enough for the risk class; higher-risk classes may require an actively revocable delivery mechanism.
- **Rationale:** Revoking application permission does not necessarily invalidate a bearer URL already issued to a client until the delivery mechanism expires or revokes it.
- **Failure behaviour:** Revocation immediately blocks new capability issuance; already-issued capability behaviour follows its declared bounded contract rather than an implicit assumption.
- **Security/privacy:** Expiry/revocation strength is risk-class-specific; no indefinite protected bearer links.
- **Performance/scaling:** The simplest low-risk class may use short-lived direct delivery; stronger revocation infrastructure is introduced where justified.
- **Enforcement/downstream:** AR-004/006 and Domain Dossiers set expiry/revocation classes; AR-007 incorporates deletion implications.

## ARC-109 — Client/CDN/storage residue participates in governed deletion where platform-controlled

- **Decision source:** AR-003 S5.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-004`, `ARQ-STATE-003`, `ARQ-SEC-002`
- **Decision:** Governed deletion discovery covers every eligible platform-controlled representation, including original objects, variants/previews, extracted/indexed derivatives, platform caches, applicable CDN/cache capabilities, temporary processing files and recovery replicas. Because arbitrary client/browser copies cannot reliably be recalled after delivery, architecture minimises persistent sensitive client copies rather than treating recall as a deletion guarantee.
- **Rationale:** Full deletion is a distributed lifecycle obligation, not a single-row or single-object operation.
- **Failure behaviour:** Undeleted eligible residue remains an explicit pending/reconciliation defect until completion or lawful retention classification.
- **Security/privacy:** Deleted/withdrawn participant data is not repopulated from caches/replicas/client-side convenience stores.
- **Performance/scaling:** Deletion fan-out is handled through bounded/durable lifecycle processing where needed.
- **Enforcement/downstream:** AR-007 owns full deletion/retention/backup orchestration; AR-008 owns verification/operational evidence.

## 3G.1 S5 Consolidated Client/CDN/Storage-Class Doctrine

```text
Browser-local state
    = safe convenience only; never durable authority

Browser/service-worker cache
    = public/explicitly safe responses by default

Public immutable assets
    = versioned identity + aggressive cache allowed

Shared CDN
    = opt-in by proven response class

Experiment-sensitive HTML
    = bypass shared full-page cache initially

Protected media
    = current authorisation -> short-lived delivery capability

Storage classes
    = public / protected / quarantine / ephemeral /
      durable-source / retained-recovery semantics kept explicit

Purge/invalidation
    = freshness acceleration, not business truth

Protected bearer capabilities
    = explicit residual-access/revocation envelope

Deletion
    = discovers platform-controlled client/CDN/object/derivative residue
```

## 3H. AR-003 Closure Audit — PASS

**Audit scope:** all frozen ARQs whose `Primary downstream workstreams` include `AR-003`.

**Mechanical routing count:** **240 ARQs**, comprising:
- `68` Performance ARQs;
- `162` Analytics ARQs;
- `1` Payments ARQ;
- `2` System ARQs;
- `4` State/Storage/Lifecycle ARQs;
- `2` Content/Media ARQs;
- `1` Security ARQ.

**Closure result:** PASS. No unresolved AR-003-specific architecture contradiction or missing state/persistence/cache/storage mechanism remains.

### Closure coverage map

1. **Authority and state placement** — `ARC-059...ARC-067` establish PostgreSQL structured authority, durable-binary object storage, derived/read-model separation, evidence-gated acceleration, immutable/superseding history and distinct business/data lifecycle.
2. **PostgreSQL concurrency, transactions, queries and migrations** — `ARC-068...ARC-076` establish invariant-specific concurrency control, short atomic authoritative transactions, durable invariant enforcement, durable critical-operation evidence, bounded queries, evidence-derived indexes, finite connection budgets, stale-tolerant read-model evolution and rolling-compatible migration law.
3. **Cache/distributed temporary state** — `ARC-077...ARC-086` establish semantics-first ETS/Cachex selection, evidence-gated Redis, version/invalidation/TTL freshness, PubSub-as-acceleration, anti-stampede control, separate cache/coordination semantics, explicit outage behaviour, restricted `:persistent_term` and empty-cache correctness.
4. **Object storage and upload lifecycle** — `ARC-087...ARC-099` establish PostgreSQL file-manifest authority, S3-compatible durable bytes, direct presigned uploads, quarantine/scan approval, UUIDv7 opaque internal identity, protected delivery, deletion reconciliation, proof-gated AshStorage+ReqS3/Wasabi candidates, derivative lineage and storage-class-specific replica recovery without routine PostgreSQL blob duplication.
5. **Browser/CDN/protected delivery/storage classes** — `ARC-100...ARC-109` establish safe-only browser persistence, public/safe client caching, immutable public asset caching, opt-in shared CDN caching, variant-safe experiment delivery, protected-media delivery capabilities, explicit storage security classes, non-authoritative purge, residual-access envelopes and deletion residue discovery.
6. **Analytics ARQs routed through AR-003** — the 162 routed Analytics requirements do not make analytics a competing operational authority. AR-003 provides their required durable/projection/storage mechanics: PostgreSQL/read-model first, rebuildable downstream projections, OLTP isolation, stable versioned state and cache/experiment-delivery boundaries. Metric semantics, assignment/exposure workflow, durable async bridges, privacy/deletion, operational observability and scaling remain governed by their existing Analytics law and later `AR-004`, `AR-005`, `AR-007`, `AR-008`, `AR-009`/Domain work as already routed; no additional AR-003 state authority is required.
7. **Cross-cutting routed requirements** — `ARQ-PAY-001`, `ARQ-SYS-*`, `ARQ-CONTENT-*`, `ARQ-SEC-002` are satisfied at the AR-003 layer without inventing provider/domain ownership: payment remains provider-integrated but PostgreSQL-authoritative where applicable; legacy LearnDash does not become authority; governed runtime translations/media retain platform state/policy boundaries; uploads remain restricted until safety approval.

### Explicit downstream handoff — not unresolved AR-003 work

AR-003 deliberately does **not** freeze:
- exact Ash Resources/tables/columns/constraints/indexes or final Domain ownership;
- exact transaction/isolation/lock choice for each Domain invariant;
- idempotency key schema/retention;
- Redis topology, key layout, eviction policy or universal TTL values;
- Cachex versus raw ETS before a workload justifies it;
- Cloudflare Cache Rules, exact cache headers, purge tags or protected-CDN implementation;
- exact browser authentication/session representation;
- object bucket/prefix layout, exact provider/region/account topology or storage-class bucket mapping;
- scanner/analyser/transcoder products;
- AshStorage/ReqS3 dependency version lock before Architectural Proof;
- exact Wasabi/provider lock before privacy/location/contract/performance/recovery proof;
- retention durations, legal-hold rules, deletion orchestration topology or backup/restore implementation;
- exact object-replica topology/provider independence by storage class;
- exact analytics projection/resource schema, refresh schedules or warehouse trigger;
- exact experiment assignment primitive implementation or statistics engine.

Those matters remain intentionally routed to AR-004...AR-009, `04_DOMAIN_MAP.md`, Domain Architecture Profiles, JIT Domain Dossiers, Architectural Proof and expert/vendor gates as applicable.

### AR-003 closure determination

- Product Law change required: **NO**
- ARQ amendment required: **NO**
- New S6 decision round required: **NO**
- Contradiction discovered: **NO**
- AR-003 status: **COMPLETE**
- Accepted AR-003 Architecture Law: `ARC-059...ARC-109`
- Next workstream: **AR-004 — Identity, Authentication, Authorisation & Field Privacy**


# 4. AR-004 — Identity, Authentication, Authorisation & Field Privacy

## 4.1 Round I1 — Identity, Authentication & Session Authority

**Accepted answer set:** `I1.1 B, I1.2 B, I1.3 B, I1.4 B, I1.5 B, I1.6 B, I1.7 B, I1.8 B`

## ARC-110 — One canonical platform identity is distinct from roles and business relationships

- **Decision source:** AR-004 I1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-008`
- **Decision:** Use one canonical platform identity for the human/account authentication subject. Participant, purchaser, recipient, practitioner, staff, moderator, administrator and similar business/authority concepts remain explicit roles, relationships or capabilities attached to that identity rather than becoming separate login identities by default.
- **Rationale:** Authentication identity answers who is acting; it must not collapse the distinct commercial, participation, professional, administrative or consent relationships required by Product Law.
- **Rules:**
  1. Multiple scoped roles may coexist on one identity.
  2. A role never manufactures unrelated authority.
  3. Duplicate identities are an exceptional recovery/merge condition, not a normal authority model.
  4. Identity merge/recovery must preserve provenance and must not silently combine conflicting business histories.
- **Security/privacy:** Paying for, inviting or administering another person does not grant access to that person's private journey merely because identities are related commercially or operationally.
- **Enforcement/downstream:** AR-004 later defines roles/relationships/consent evaluation. Domain Law owns concrete role/resource names and ownership.

## ARC-111 — AshAuthentication + AshAuthenticationPhoenix are preferred proof candidates, not permanent package law

- **Decision source:** AR-004 I1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`, `ARQ-IAM-003`, `ARQ-IAM-008`
- **Decision:** Treat AshAuthentication and AshAuthenticationPhoenix as the preferred Architectural Proof path for the Ash-first authentication boundary, subject to proof that the selected stable versions can satisfy password authentication, confirmation/verification, session/token revocation, LiveView integration, recovery, audit and the platform's stronger MFA/step-up/session-management requirements.
- **Rationale:** They align naturally with the accepted Ash action/domain architecture while preserving the rule that package capability never weakens frozen security requirements.
- **Rules:**
  1. Package selection is subordinate to the platform authentication contract.
  2. Proof failure changes implementation, not Product Law.
  3. Exact dependency versions remain JIT/proof decisions.
  4. Package-specific resource/table shapes are not architecture authority.
- **Enforcement/downstream:** Architectural Proof must explicitly test revocation, LiveView session reconstruction, MFA/step-up extensibility, recovery, audit and rolling-deployment compatibility.

## ARC-112 — Launch authentication is email/password first; optional magic-link sign-in does not create a second identity model

- **Decision source:** AR-004 I1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`, `ARQ-IAM-008`
- **Decision:** Launch authentication uses email/password as the baseline. Optional email magic-link sign-in may authenticate an existing canonical identity, but it must not silently create an alternate identity model or auto-register unknown addresses unless a later explicit Product/Architecture decision approves that behaviour. Social login remains deferred and future passkeys remain allowed.
- **Rationale:** A deliberate registration/verification path reduces accidental duplicate identities and keeps all authentication methods attached to one governed identity.
- **Rules:**
  1. Authentication method is not identity ownership.
  2. Magic-link use must respect existing verification/recovery rules.
  3. Unknown-address registration via magic link is disabled by default.
  4. Future authentication strategies must link to the canonical identity through an explicit verified process.
- **Security/privacy:** Account enumeration and magic-link abuse protections remain mandatory under AR-004/AR-008 security design.

## ARC-113 — Email verification is a capability gate, not a blanket inability to authenticate

- **Decision source:** AR-004 I1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`
- **Decision:** Store and evaluate email-verification state as an explicit application capability condition. Unverified users may authenticate and perform Product-Law-permitted low-risk setup/public actions, while actions requiring verified email are rejected at the authoritative application/policy boundary.
- **Rationale:** Product Law deliberately distinguishes identity authentication from verification-sensitive capability access.
- **Rules:**
  1. Verification state is authoritative server-side state.
  2. UI hiding alone is insufficient enforcement.
  3. Paid purchase/redemption, assessment, health-data entry, personalised plans, member community, sensitive export and account deletion require verified email where frozen Product Law says so.
  4. Verification changes must affect current policy evaluation rather than relying on stale socket/client state.
- **Enforcement/downstream:** Exact confirmation token lifecycle and delivery mechanics remain implementation/proof work.

## ARC-114 — First-party sessions are individually identifiable, revocable and backed by durable server authority

- **Decision source:** AR-004 I1.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`, `ARQ-IAM-008`
- **Decision:** Meaningful first-party login sessions must be individually identifiable and revocable through durable server-side authority or an equivalent durable token/session record. The platform must be able to inspect/revoke one session, revoke all sessions, and reconstruct current authority after application restart or node loss.
- **Rationale:** Purely self-contained long-lived client tokens cannot by themselves satisfy the frozen session inspection, revocation and compromise-containment requirements.
- **Rules:**
  1. The browser holds a credential/reference, not independent authority.
  2. Session validity is checked against current identity/security state where required.
  3. Revocation must survive process/node restart.
  4. Session records capture only the minimum metadata needed for security, user inspection and audit.
- **Security/privacy:** Session metadata must not become unnecessary fingerprinting/analytics payload.
- **Enforcement/downstream:** Exact cookie/token/session resource representation is deferred to implementation proof; AR-008 governs secure deployment/secret handling.

## ARC-115 — Authentication assurance is contextual and supports explicit MFA/step-up elevation

- **Decision source:** AR-004 I1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`
- **Decision:** Treat authentication assurance as contextual state rather than a binary logged-in flag. Participant MFA may remain optional, staff and practitioners require MFA, and designated high-risk actions require fresh step-up authentication according to current risk/policy. Trusted-device status is expiring/revocable and never permanently bypasses required step-up.
- **Rationale:** Product Law explicitly requires stronger assurance for privileged roles and high-risk actions.
- **Rules:**
  1. Identity, session, current assurance and current policy jointly determine whether an action may proceed.
  2. Step-up state has bounded freshness appropriate to the action risk.
  3. Trusted-device state is not universal MFA bypass.
  4. Security changes or compromise may invalidate assurance and force reauthentication.
- **Enforcement/downstream:** Exact MFA factors, assurance levels and reauthentication windows are AR-004/JIT proof decisions.

## ARC-116 — Mandatory MFA/step-up is a platform capability boundary, not delegated to an unstable package feature

- **Decision source:** AR-004 I1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`
- **Decision:** Lock a framework-independent MFA/step-up capability contract. Do not make a release-candidate or otherwise unproven AshAuthentication feature the sole authority for mandatory staff/practitioner MFA. Architectural Proof selects a stable implementation path that can later accommodate approved passkey/WebAuthn capability without redefining authentication law.
- **Rationale:** Mandatory security invariants must outlive package maturity/version changes.
- **Rules:**
  1. Stable production capability is required before a mechanism becomes launch security authority.
  2. MFA implementation must integrate with explicit assurance/session/revocation/audit semantics.
  3. Recovery paths must not become an MFA bypass.
  4. Future passkey support is evolutionary, not a reason to weaken launch controls.
- **Enforcement/downstream:** Vendor/library proof and exact factor UX remain downstream.

## ARC-117 — Argon2id is the preferred password-hashing default with benchmarked cost parameters

- **Decision source:** AR-004 I1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`, `ARQ-IAM-003`
- **Decision:** Prefer Argon2id for password hashing. Memory/time/parallelism parameters are selected through security/performance proof against actual production hardware and abuse controls rather than frozen as a universal architecture constant.
- **Rationale:** Password hashing must be deliberately expensive for attackers while remaining operationally safe for the launch and scaled authentication workload.
- **Rules:**
  1. Passwords are never stored recoverably or logged.
  2. Hash parameters are versioned/upgradeable so stronger settings can be adopted over time.
  3. Authentication load/abuse testing includes password-hash resource pressure.
  4. Exact parameters remain operational/security configuration, not Product Law.
- **Security/privacy:** Password hash material remains highly protected credential data even though it is one-way.
- **Enforcement/downstream:** AR-008/AR-009 cover abuse/load evidence and resource budgets.

### I1 deferrals preserved

I1 deliberately does **not** freeze final role/resource names, permission schema, consent schema, MFA provider/factor set, session table schema, cookie/token representation, exact Argon2 parameters, recovery workflow, trusted-device implementation or package versions. Those remain for later AR-004 rounds, AR-008/009, Domain Law, JIT Dossiers and Architectural Proof.


## 4.2 Round I2 — Roles, Capabilities, Relationships & Field Privacy

**Accepted answer set:** `I2.1 B, I2.2 B, I2.3 B, I2.4 B, I2.5 B, I2.6 B, I2.7 B, I2.8 B`

## ARC-118 — Authorisation is composable and contextual rather than role-only RBAC

- **Decision source:** AR-004 I2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-003`, `ARQ-IAM-005`, `ARQ-IAM-006`
- **Decision:** Governed authorisation evaluates the relevant combination of canonical identity, current role/capability, requested action, target/resource relationship, scope, purpose/consent, time/expiry, authentication assurance and current resource/security state. Role membership is one policy fact, not a universal access grant.
- **Rationale:** Product Law requires multiple scoped roles while explicitly separating commercial, participant, professional, clinical and administrative authority. A pure role-name check cannot represent those constraints safely.
- **Rules:**
  1. Policies evaluate only facts material to the requested action rather than constructing one universal permission snapshot.
  2. Relationship-, purpose-, time- and assurance-sensitive actions must include those facts where applicable.
  3. A broad technical role must not imply unrelated business/clinical authority.
  4. Final concrete role/capability vocabulary remains Domain Law.
- **Security/privacy:** Sensitive access must fail closed when required contextual authority cannot be established.
- **Enforcement/downstream:** Ash policies are the normal enforcement mechanism under ARC-036/ARC-122; AR-005/AR-008 later define revocation/event/audit operational mechanics.

## ARC-119 — Roles are governed contextual classifications, not blanket permission keys

- **Decision source:** AR-004 I2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-004`, `ARQ-IAM-005`
- **Decision:** Treat roles as understandable governed classifications/bundles from which relevant capabilities and policy facts may be derived. The authoritative question remains whether this actor may perform this action on this target in the current context.
- **Rationale:** This retains useful concepts such as participant, practitioner, moderator, support, finance and administrator without making those labels universal authority tokens.
- **Rules:**
  1. One identity may hold multiple roles simultaneously.
  2. Roles are scoped where applicable and may be granted/revoked independently.
  3. `administrator` or equivalent technical role never automatically grants clinical, methodology, finance or private-journal authority.
  4. Role labels do not replace explicit relationship/consent checks.
- **Security/privacy:** Role display or membership alone is insufficient proof for sensitive data disclosure.
- **Enforcement/downstream:** `04_DOMAIN_MAP.md` and Domain Dossiers define final role ownership/vocabulary; AR-004 defines policy semantics.

## ARC-120 — Material authority grants are explicit durable scoped assignments with governed lifecycle

- **Decision source:** AR-004 I2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-004`, `ARQ-IAM-005`
- **Decision:** Material role/capability/authority grants are represented as explicit durable assignments carrying the scope and lifecycle evidence appropriate to their risk, including subject, authority, scope/context, effective period, grant/revocation provenance and approval/reason metadata where required.
- **Rationale:** Durable scoped assignments support revocation, audit, expiry and multiple simultaneous authorities without reducing the user record to one mutable role enum or stale token claim.
- **Rules:**
  1. Ordinary low-risk roles need only the metadata justified by their lifecycle.
  2. Privileged/sensitive grants require named subject, explicit scope, reason/approver where required, expiry/review semantics and revocation history.
  3. Material grants are not stored only in sessions/JWTs/client state.
  4. Exact resource/table schema remains Domain/JIT design.
- **Failure behaviour:** Loss of cache/session state must not erase or invent durable authority grants.
- **Security/privacy:** Grant metadata itself is governed security/identity data and should be minimised.

## ARC-121 — Practitioner/private-record access is an explicit governed relationship distinct from practitioner role

- **Decision source:** AR-004 I2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-005`, `ARQ-IAM-006`
- **Decision:** Practitioner access to participant/private records requires explicit governed relationship state in addition to practitioner role. Applicable policy facts include participant permission/consent, active relationship, purpose, record/field scope, effective/expiry period and revocation state.
- **Rationale:** Product Law explicitly rejects role-only browsing of private participant information and requires a live, scoped, revocable relationship.
- **Rules:**
  1. Practitioner status never implies access to all participants.
  2. The relationship itself is durable, auditable and revocable.
  3. Scope/purpose/expiry are enforced during current policy evaluation.
  4. Revocation ends future platform access even if separately retained professional records remain under retention law.
- **Security/privacy:** Support/content/moderation/technical-admin roles cannot reuse practitioner relationship semantics to obtain health/private access.
- **Enforcement/downstream:** Final owning Resource/domain is deferred to Domain Law; AR-007 governs retained professional copies.

## ARC-122 — Ash policies are the normal authoritative action/record authorisation boundary

- **Decision source:** AR-004 I2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-IAM-007`
- **Decision:** Governed Ash Resources/actions use Ash policies as the normal authoritative authorisation boundary, with authorisation forced at the approved Domain boundary under ARC-036. Read policies filter unauthorised records before they enter ordinary application/UI results rather than loading broad sensitive datasets and hiding rows afterward.
- **Rationale:** Enforcement at the application authority boundary keeps authorization consistent across LiveView, jobs and future API callers and avoids presentation-layer filtering becoming security law.
- **Rules:**
  1. Route/UI guards are UX/navigation controls, not sufficient authorisation.
  2. Direct low-level escape hatches must preserve equivalent authorisation under ARC-056/058.
  3. Missing required authority facts fail closed.
  4. Exceptional internal/break-glass paths remain separately governed rather than globally disabling policy.
- **Security/privacy:** Unauthorised records should not be unnecessarily loaded into application/socket memory.

## ARC-123 — Field privacy uses explicit field policies plus redaction and minimum-data loading

- **Decision source:** AR-004 I2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-IAM-007`, `ARQ-STATE-001`
- **Decision:** Protected field disclosure uses layered controls: public/private field exposure declarations, `sensitive?` inspection redaction, Ash field policies for actual field visibility, and minimum-data loading. Protected related records remain governed by policies on the related Resource because relationship traversal is not implicitly authorised by a field policy.
- **Rationale:** Redaction, public API exposure and runtime authorisation solve different problems and must not be conflated.
- **Rules:**
  1. `sensitive?: true` is not authorisation.
  2. `public?: false` is not a complete runtime access policy.
  3. Callers request only the fields/relationships needed by the workflow.
  4. Field policies apply where field-level disclosure differs by actor/context.
- **Security/privacy:** Detailed health/private data must not leak through broad loads, calculations, aggregates or related resources merely because the parent record is visible.

## ARC-124 — Purpose-specific Ash actions explicitly control writable inputs and protected state transitions

- **Decision source:** AR-004 I2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-002`, `ARQ-IAM-004`, `ARQ-IAM-006`
- **Decision:** Prefer purpose-specific authoritative actions with explicitly accepted inputs. Sensitive/system-owned attributes such as privileged authority, verification, consent or protected workflow state are changed through governed action logic rather than exposed through generic mass-update inputs.
- **Rationale:** Purpose-specific actions make authorization, validation, audit and invariants reviewable and materially reduce accidental mass-assignment authority.
- **Rules:**
  1. A database column existing does not imply callers may set it.
  2. Generic update actions may be used only where their accepted surface is intentionally narrow and safe.
  3. Protected state transitions are named application operations.
  4. Browser params are untrusted intent under ARC-052.
- **Security/privacy:** Privileged/verification/consent fields must not be caller-controlled through broad form payloads.

## ARC-125 — Sessions carry stable identity/assurance context; revocable authority is resolved from current server state

- **Decision source:** AR-004 I2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`, `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-IAM-008`, `ARQ-PERF-046`
- **Decision:** Sessions/actor context carry relatively stable identity and authentication/assurance context, while revocable roles, grants, relationships, consent and other dynamic authority are resolved from current authoritative state during governed operations. Safe caches may accelerate evaluation but cannot freeze authority for the life of a session.
- **Rationale:** Consent withdrawal, role removal, relationship expiry and compromise containment must affect already-connected users without requiring logout or token expiry.
- **Rules:**
  1. Do not embed a permanent complete permission snapshot in session/JWT state.
  2. Current governed actions re-evaluate material revocable facts.
  3. Material revocation has immediate invalidation/authoritative-bypass semantics under ARC-079/081.
  4. Long-lived LiveViews remain subject to current policy under ARC-040.
- **Failure behaviour:** Stale cache/session claims cannot preserve revoked authority; the authoritative check wins.
- **Security/privacy:** Session contents are minimised and must not contain unnecessary sensitive relationship/consent payloads.

### I2 deferrals preserved

I2 deliberately does **not** freeze final role/capability names, permission table/resource schema, practitioner-relationship owner, consent-resource schema, exact Ash policy modules, privileged approval workflow, audit storage, break-glass implementation, revocation broadcast mechanism or Domain ownership. Those remain for I3/later AR-004, AR-005/007/008, Domain Law, JIT Dossiers and Architectural Proof.


## 4.3 Round I3 — Consent, Privileged Authority, Audit & Revocation

**Accepted answer set:** `I3.1 B, I3.2 B, I3.3 B, I3.4 B, I3.5 B, I3.6 B, I3.7 B, I3.8 B, I3.9 B, I3.10 B`

## ARC-126 — Consent/lawful-basis authority is purpose-specific rather than one universal flag

- **Decision source:** AR-004 I3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-006`, applicable privacy/analytics consent ARQs
- **Decision:** Govern consent/lawful-basis state per processing purpose. Required service/lawful processing and optional consent remain distinguishable; health storage/personalisation, automated recommendations, laboratory uploads, practitioner sharing, anonymised/aggregated analytics, marketing and community participation remain independently governable where Product Law requires them.
- **Rationale:** One master consent Boolean cannot express withdrawal, purpose limitation, optional-vs-required processing or independent marketing/community decisions safely.
- **Rules:**
  1. No unrelated purpose inherits permission merely because another purpose is allowed.
  2. Required service/legal processing is not mislabeled as optional consent.
  3. Policy evaluation uses the current effective purpose state relevant to the action.
  4. Exact purpose vocabulary/resource ownership remains Domain Law/JIT design.
- **Security/privacy:** Purpose limitation is an authorisation/privacy boundary, not presentation metadata.

## ARC-127 — Consent history is append-only evidence with a separate efficient current-effective-state projection

- **Decision source:** AR-004 I3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-006`, `ARQ-IAM-007`, `ARQ-STATE-002`
- **Decision:** Material consent grants, withdrawals and applicable policy/version evidence are preserved as immutable/superseding history while an efficient current-effective-state projection may identify what presently governs each purpose.
- **Rationale:** Withdrawal changes future authority without rewriting whether prior processing was lawful under the then-effective consent/policy state.
- **Rules:**
  1. Material transitions preserve subject, purpose, decision, effective time, applicable policy/version and provenance appropriate to the workflow.
  2. Current projections are derived convenience/authority views, not a reason to destroy historical evidence.
  3. Corrections/supersession preserve prior evidence rather than destructive rewriting.
  4. Exact schema/table/resource shape is deferred.
- **Security/privacy:** Consent evidence is sensitive governance data and must be minimised to what is needed for proof and operation.

## ARC-128 — Material revocation is an authoritative transition with explicit dependency invalidation obligations

- **Decision source:** AR-004 I3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-006`, `ARQ-IAM-008`, `ARQ-PERF-046`, `ARQ-PERF-129`, `ARQ-PERF-130`
- **Decision:** Consent/access/session/security revocation becomes effective through its durable authoritative transition. New governed actions must immediately observe the revoked authority; dependent caches/flags/session capability and future processing receive explicit invalidation/reconciliation obligations. PubSub/signals may accelerate propagation but are not the source of truth.
- **Rationale:** Waiting for TTL, logout or socket death would preserve revoked authority beyond the Product-Law boundary.
- **Rules:**
  1. Current action-boundary policy evaluation wins over stale cache/session state.
  2. Material live-session revocation must be capable of prompt disconnect/invalidation.
  3. Durable downstream propagation semantics are defined in AR-005 where required.
  4. Missed transient notifications cannot restore authority.
- **Failure behaviour:** If propagation is delayed, authoritative operations still fail closed against current revoked state.

## ARC-129 — Privileged authority uses named, least-privilege, scoped and preferably time-bounded elevation

- **Decision source:** AR-004 I3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-004`, `ARQ-IAM-007`
- **Decision:** Sensitive/privileged authority is granted to named subjects with the narrowest practical scope and lifecycle evidence, preferring time-bounded elevation. Material grants support reason, approver where required, effective/expiry/review semantics, MFA requirements and revocation history; sensitive grants cannot be self-approved.
- **Rationale:** Permanent broad administrator authority creates unnecessary blast radius and conflicts with Product Law's separation of technical, business and clinical authority.
- **Rules:**
  1. Shared privileged identities/credentials are prohibited.
  2. Privileged role does not bypass unrelated business/clinical policies.
  3. Termination/authority loss triggers prompt revocation.
  4. Exact approval UX/workflow remains AR-008/JIT design.
- **Security/privacy:** Elevation metadata and usage are auditable security evidence.

## ARC-130 — Break-glass is a separate exceptional governed elevation path, never a universal authorisation-off switch

- **Decision source:** AR-004 I3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-004`, `ARQ-IAM-007`
- **Decision:** Break-glass/production access is a distinct exceptional path requiring named identity, strong MFA, explicit reason, narrow scope where possible, short expiry, immediate audit evidence, owner/security notification and post-access review.
- **Rationale:** Emergency access must preserve accountability and minimum authority precisely when ordinary controls are being exceptionally overridden.
- **Rules:**
  1. No shared emergency account/password.
  2. Break-glass elevation is explicit and expires automatically.
  3. Direct database access remains exceptional and separately evidenced.
  4. Break glass does not imply unrestricted clinical/business authority unrelated to the emergency.
- **Security/privacy:** Access reason/scope and affected target categories are recorded without copying sensitive payloads unnecessarily.

## ARC-131 — Material audit/security evidence uses a separate immutable, minimised and reasoned evidence path

- **Decision source:** AR-004 I3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-007`, `ARQ-IAM-004`, `ARQ-IAM-006`
- **Decision:** Material sensitive access, privileged actions, consent transitions, security/recovery changes and similar governed events write category-appropriate tamper-resistant audit/security evidence separate from ordinary debug logs, analytics and business payload copies.
- **Rationale:** Operational logs are not sufficient durable governance evidence and can create privacy risk if full sensitive payloads are duplicated indiscriminately.
- **Rules:**
  1. Evidence includes appropriate actor/executing authority, action, target category/identity, time, reason/purpose where required, outcome/policy result, correlation identifier and limited change summary.
  2. Passwords, bearer tokens and unnecessary health/private payloads are excluded.
  3. Ordinary administrators cannot rewrite audit history.
  4. Exact storage/retention technology remains AR-008/AR-007/JIT work.
- **Security/privacy:** Audit evidence has its own access/retention purpose and cannot be repurposed for marketing/personalisation.

## ARC-132 — Audit capture is risk/category based rather than an unbounded permanent record of every low-risk denial

- **Decision source:** AR-004 I3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-007`, `ARQ-SEC-001`
- **Decision:** Governed immutable audit evidence is mandatory for material categories, while routine low-risk probes/denials may use security telemetry rather than creating an expensive permanent audit record. Exact category matrices and retention are risk/Domain/operations decisions.
- **Rationale:** Capturing every trivial denial as permanent immutable evidence would add cost, privacy exposure and abuse amplification without improving material accountability.
- **Rules:**
  1. Sensitive-record access, privileged/break-glass use, consent/security/recovery/elevation changes and high-risk abuse/security outcomes are explicit evidence candidates.
  2. Denial telemetry may be aggregated/rate-controlled where safe.
  3. The absence of permanent audit for a low-risk event does not disable required security monitoring.
  4. Materiality thresholds are documented rather than caller discretion.
- **Security/privacy:** Audit minimisation reduces secondary sensitive-data accumulation.

## ARC-133 — Sensitive authentication/recovery/redemption surfaces use non-enumerating public responses with precise internal diagnosis

- **Decision source:** AR-004 I3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SEC-001`, `ARQ-IAM-003`, `ARQ-IAM-008`
- **Decision:** Public responses on registration/login/reset/magic-link/MFA/recovery/redemption and comparable sensitive entry points must not reveal whether a guessed identity, secret, code or protected state was otherwise valid. Internally, authorised security/audit paths retain the precise outcome needed for diagnosis and response.
- **Rationale:** Differentiated public errors and materially different processing can become account/secret enumeration or abuse oracles.
- **Rules:**
  1. Generic public responses are used where existence/state disclosure is unsafe.
  2. Timing/work factors should avoid avoidable enumeration signals where practical.
  3. Already-authorised contexts may return more specific errors where disclosure is safe and useful.
  4. Internal diagnostic detail never becomes browser-visible by default.
- **Security/privacy:** Non-enumeration applies consistently across equivalent sensitive channels, not only password login.

## ARC-134 — Authorisation failures separate exact internal policy reasoning from minimum-safe external responses

- **Decision source:** AR-004 I3.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-005`, `ARQ-IAM-007`, `ARQ-SEC-001`
- **Decision:** Internal policy evaluation may retain precise forbidden reasons/correlation evidence, while external responses disclose only the minimum information appropriate to the caller/context. Protected record existence, hidden relationship state, privileged rules and sensitive policy internals must not leak through response differences unnecessarily.
- **Rationale:** Correct denial can still violate privacy if the error itself reveals protected facts.
- **Rules:**
  1. Do not expose raw Ash policy traces/debug internals to untrusted clients.
  2. No universal HTTP status is mandated; response semantics remain context-appropriate and non-enumerating.
  3. Authorised support/security diagnostics may access richer evidence under policy.
  4. UI messaging must not become an alternate authority oracle.
- **Security/privacy:** Privacy-safe denial is part of authorisation correctness.

## ARC-135 — Revocation broadcasts accelerate propagation; durable authority makes revocation effective

- **Decision source:** AR-004 I3.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-046`, `ARQ-PERF-060`, `ARQ-PERF-129`, `ARQ-PERF-130`, `ARQ-IAM-006`, `ARQ-IAM-008`
- **Decision:** Durable authoritative revocation is effective immediately at governed action boundaries. PubSub/realtime signals may promptly disconnect LiveViews, invalidate node-local caches, refresh actor state and stop stale UI interaction, but missed broadcasts cannot preserve or restore revoked authority.
- **Rationale:** Multi-node correctness cannot depend on every transient subscriber receiving every revocation event.
- **Rules:**
  1. Realtime consumers treat revocation signals as freshness/invalidation instructions, not authority creation.
  2. Subsequent actions re-evaluate current authority even after missed messages.
  3. Prompt live-session revocation is required for material access/security changes.
  4. Durable cross-boundary consequence delivery, when required, is designed in AR-005.
- **Failure behaviour:** A node that misses a revocation message may show stale UI briefly but cannot successfully commit a newly forbidden authoritative action.

### I3 deferrals preserved

I3 deliberately does **not** freeze exact consent resources/tables, legal-basis taxonomy beyond Product Law, audit storage technology/retention, privileged approval UI, break-glass implementation, revocation event/outbox topology, live-session disconnect implementation, exact public error strings, rate-limit thresholds or final Domain ownership. Those remain for I4, AR-005/007/008/009, Domain Law, JIT Dossiers and Architectural Proof.


## 4.4 Round I4 — Recovery, Compromise, Sessions, Devices & Abuse Controls

**Accepted answer set:** `I4.1 B, I4.2 B, I4.3 B, I4.4 B, I4.5 B, I4.6 B, I4.7 B, I4.8 B, I4.9 B, I4.10 B`

## ARC-136 — Account recovery is a graduated risk-proportional security state machine

- **Decision source:** AR-004 I4.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`, `ARQ-IAM-008`, `ARQ-SEC-001`
- **Decision:** Account recovery is an explicit governed workflow whose evidence, friction, temporary restrictions and approvals scale with risk. Ordinary recovery may use an approved verified channel; exceptional or privileged recovery requires stronger evidence and may impose security holds, restricted sensitive actions and second-person approval. Successful recovery restores controlled access to the canonical identity; it does not automatically restore every prior session, device trust, elevated role or revoked authority.
- **Rationale:** Product Law requires graduated, auditable recovery and prohibits informal support override as an authentication mechanism.
- **Rules:**
  1. Recovery establishes control of the identity through an approved process; it does not manufacture business/domain authority.
  2. Privileged recovery is stricter than ordinary participant recovery and cannot silently bypass MFA/approval requirements.
  3. Recovery may trigger credential/session rotation, revocation and temporary security restrictions according to risk.
  4. Exact proof/evidence steps, holds and time windows remain security/JIT configuration.
- **Failure behaviour:** Ambiguous or insufficient recovery evidence fails safely into a controlled unresolved/restricted state rather than granting full authority.
- **Security/privacy:** Recovery responses remain non-enumerating and minimised under `ARC-133` and `ARQ-SEC-001`.
- **Enforcement/downstream:** AR-008 owns operational recovery evidence/incident handling; Domain Dossiers define domain-specific post-recovery restrictions where required.

## ARC-137 — Sensitive identity and credential changes are high-risk security transitions

- **Decision source:** AR-004 I4.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`, `ARQ-IAM-003`, `ARQ-IAM-008`, `ARQ-SEC-001`
- **Decision:** Changes to login identifiers, credentials, MFA/trusted-device state and equivalent sensitive identity controls use purpose-specific high-risk actions. Depending on risk, they require current/recent step-up authentication, confirmation of newly introduced control channels, notification to prior verified channels where feasible, and session/token rotation or selective revocation.
- **Rationale:** Treating email/credential changes as ordinary profile edits would allow an already-compromised session to convert temporary access into durable account takeover.
- **Rules:**
  1. Identity-security fields are never generic mass-assignment inputs.
  2. New contact/authentication channels are not trusted merely because the requester supplied them.
  3. Material security transitions may invalidate prior sessions, trusted-device grants or recovery capabilities.
  4. Exact hold/notification windows are evidence-gated rather than universal constants.
- **Security/privacy:** Failure messages do not disclose protected account state to unauthorised callers.
- **Enforcement/downstream:** Preferred authentication packages may implement parts of this flow, but package semantics remain subordinate to the platform contract.

## ARC-138 — Duplicate-identity merge is governed reconciliation, not destructive row collapse

- **Decision source:** AR-004 I4.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-001`, `ARQ-IAM-008`, applicable `ARQ-STATE-*` history requirements
- **Decision:** Reconciling duplicate identities requires verified control/evidence for the identities involved, deliberate discovery of affected domain records, preservation of immutable provenance/history and explicit resolution of conflicting current-state choices. A merge may establish one canonical future authentication identity without rewriting the historical origin of finance, professional, audit, consent or other immutable records.
- **Rationale:** Identity consolidation is not equivalent to domain-history consolidation; naïvely repointing all foreign keys and deleting one identity can manufacture authority and destroy provenance.
- **Rules:**
  1. Name, demographics or similarity alone are never sufficient merge proof.
  2. Each affected domain owns its reconciliation semantics through Domain Law/JIT dossiers.
  3. Historical records retain original actor/subject provenance where required even after canonical identity resolution.
  4. Conflicting active preferences/consents/relationships are resolved explicitly rather than last-write-wins by accident.
- **Failure behaviour:** Unresolved conflicts leave the merge pending/partial under governed state rather than silently selecting one side.
- **Security/privacy:** Merge tooling cannot be used as an access-elevation shortcut.

## ARC-139 — Account compromise has explicit containment state and revocation powers

- **Decision source:** AR-004 I4.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`, `ARQ-IAM-008`, `ARQ-PERF-046`, `ARQ-PERF-129`, `ARQ-SEC-001`
- **Decision:** The identity/security model supports explicit suspected/confirmed compromise containment capable of revoking active sessions/tokens and trusted-device status, disconnecting/restricting live sessions, freezing high-risk changes/actions, requiring verified recovery and preserving security evidence. Privileged-account compromise escalates immediately through the operational security path.
- **Rationale:** Password change alone is not enough if stolen sessions, trusted-device grants or high-risk actions remain usable.
- **Rules:**
  1. Containment scope is proportional to the incident but can become account-wide where needed.
  2. Current authoritative compromise/revocation state overrides stale session/cache claims.
  3. Security holds are distinct from permanent business/domain deletion or cancellation.
  4. Recovery from compromise deliberately re-establishes trust rather than resurrecting old trust state.
- **Failure behaviour:** If the platform cannot establish that a sensitive action is safe during compromise containment, it fails closed for that action.
- **Enforcement/downstream:** AR-005 defines durable propagation where required; AR-008 defines incident operations/observability.

## ARC-140 — Sessions are individually addressable server-governed security objects with bounded lifetime

- **Decision source:** AR-004 I4.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`, `ARQ-IAM-008`, `ARQ-PERF-129`, `ARQ-PERF-130`
- **Decision:** First-party authenticated sessions are individually identifiable and server-governed with risk-appropriate idle and absolute expiry, explicit revocation and sufficient durable/current state to inspect/revoke one session or all sessions. Material authentication, recovery, credential or privilege transitions can rotate session credentials or revoke prior sessions. The session carries identity/authentication assurance context, not a frozen universal permission snapshot.
- **Rationale:** Product Law requires user-visible/revocable sessions and role/risk-based lifetime; purely long-lived stateless bearer authority cannot satisfy those controls reliably.
- **Rules:**
  1. Session lifetime classes differ by risk/role; exact numbers remain security configuration.
  2. Server-side revocation must be authoritative for governed first-party sessions.
  3. `logout all devices`/security containment can revoke all relevant active sessions.
  4. Permission/consent/relationship changes remain dynamically evaluated under `ARC-125`.
- **Failure behaviour:** Expired/revoked sessions cannot regain authority from client-held stale state.
- **Performance/scaling:** Session validation must remain compatible with future multi-node application operation without requiring sticky routing.

## ARC-141 — First-party web session credentials use secure opaque cookie transport by default

- **Decision source:** AR-004 I4.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`, `ARQ-IAM-003`, `ARQ-SEC-001`, applicable browser/storage ARQs
- **Decision:** Ordinary first-party browser sessions use an opaque credential/reference transported through appropriately scoped secure cookies rather than storing bearer session authority in `localStorage` or URLs. Production cookies use HTTPS-only transport, `Secure`, `HttpOnly`, deliberate `SameSite` behaviour and appropriately narrow host/path scope. Client credentials contain no unnecessary business/sensitive payload.
- **Rationale:** This minimises script-readable credential exposure and keeps session meaning/revocation under server control.
- **Rules:**
  1. Session identifiers/tokens are secrets, distinct from UUIDv7 resource identifiers under `ARC-098`.
  2. URLs must not carry durable session secrets.
  3. Cross-site flows requiring different cookie behaviour must be explicitly justified and protected.
  4. Native/mobile/API credential models, if later introduced, receive their own approved contract rather than inheriting browser assumptions blindly.
- **Security/privacy:** Cookie/session values are excluded from ordinary logs/analytics.
- **Enforcement/downstream:** Exact cookie names, signing/encryption implementation and token representation remain Architectural Proof/JIT work.

## ARC-142 — Trusted-device state is separate, expiring and revocable convenience authority

- **Decision source:** AR-004 I4.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-003`, `ARQ-IAM-008`
- **Decision:** Trusted-device/remembered-device state is an explicit expiring and revocable security record established only after an approved verified authentication event. It may reduce authentication friction only where policy permits and never bypasses mandatory practitioner/staff MFA, explicit high-risk step-up, compromise containment or current security revocation.
- **Rationale:** Device trust is a bounded convenience signal, not durable identity proof or universal MFA exemption.
- **Rules:**
  1. Device trust is revocable independently of the account/session.
  2. Device trust expires/revalidates according to risk.
  3. Invasive fingerprinting is not treated as identity proof merely for convenience.
  4. Account compromise/recovery may revoke trusted-device state globally.
- **Security/privacy:** Device metadata is minimised and purpose-limited security data, not advertising/profile infrastructure.

## ARC-143 — Reset, confirmation, magic-link and recovery capabilities are single-purpose bounded replay-controlled secrets

- **Decision source:** AR-004 I4.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-002`, `ARQ-IAM-003`, `ARQ-IAM-008`, `ARQ-SEC-001`
- **Decision:** Authentication/security capabilities such as reset, confirmation, magic-link, recovery and equivalent tokens are purpose-specific cryptographically unpredictable or cryptographically signed secrets with bounded lifetime and explicit replay/revocation semantics. Successful use or relevant security-state change invalidates them where required. Server persistence stores only the information necessary to validate, revoke and audit them rather than preserving reusable plaintext bearer secrets.
- **Rationale:** Resource identifiers such as UUIDv7 are not secret capabilities, and reusable multi-purpose tokens magnify replay/account-takeover risk.
- **Rules:**
  1. One token purpose cannot silently authorize another security action.
  2. Tokens are not logged in plaintext or sent to analytics.
  3. Expiry/use/revocation behaviour is explicit and testable.
  4. Security state changes may invalidate outstanding capabilities according to their purpose.
- **Failure behaviour:** Replay/expired/revoked capability use fails safely with non-enumerating external responses.

## ARC-144 — Abuse protection is layered, risk-aware and recoverable rather than one universal threshold

- **Decision source:** AR-004 I4.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SEC-001`, `ARQ-PERF-004`, `ARQ-IAM-003`, `ARQ-IAM-008`
- **Decision:** Sensitive identity/payment/redemption/download/search entry points use layered abuse controls appropriate to their risk, combining edge and application controls and relevant account/network/device/session/operation/velocity/security-state signals. Responses may progressively throttle, delay, challenge, require stronger authentication, temporarily lock or enter security containment. Exact thresholds and challenge providers are evidence/JIT decisions.
- **Rationale:** One IP limit or one permanent fixed-attempt lock cannot safely represent credential stuffing, distributed abuse, shared networks, recovery flows or privileged-account risk.
- **Rules:**
  1. Temporary lockouts/challenges remain recoverable and do not become accidental permanent denial of service.
  2. Privileged accounts may receive stricter handling.
  3. Public SEO/discovery must remain available while private/paid/health/plan bulk extraction is constrained.
  4. Public responses remain non-enumerating under `ARC-133`.
- **Failure behaviour:** Abuse-control degradation follows an explicit risk posture; it must not silently disable critical protection.
- **Performance/scaling:** Controls must avoid unbounded per-request work and remain observable under attack/peak load.

## ARC-145 — Platform-wide velocity/security controls require distributed-capable state before multi-node traffic depends on them

- **Decision source:** AR-004 I4.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SEC-001`, `ARQ-PERF-049`, `ARQ-PERF-050`, `ARQ-PERF-051`, applicable multi-node ARQs
- **Decision:** A security/abuse control whose correctness depends on platform-wide velocity uses a state/coordination mechanism that provides the required shared view across every application node processing that surface. Single-instance launch does not mandate Redis merely for diagrammatic symmetry; before traffic is distributed across multiple nodes, the chosen mechanism must prove cross-node behaviour. PostgreSQL, Redis or another approved mechanism may satisfy the boundary according to latency, contention, failure and scale requirements.
- **Rationale:** Node-local counters become bypassable when traffic spreads across nodes, while prematurely requiring Redis would violate the evidence-gated infrastructure doctrine.
- **Rules:**
  1. Local-only counters are allowed only where the control contract explicitly tolerates locality.
  2. Distributed security coordination has explicit outage/failure semantics.
  3. Redis remains optional/evidence-gated under `ARC-078`; using it for security coordination does not make it durable business authority.
  4. Horizontal application scaling cannot precede proof of required shared security-state semantics.
- **Failure behaviour:** If loss of shared coordination would make a high-risk operation unsafe, that operation degrades/fails closed according to its declared contract rather than silently reverting to ineffective local protection.
- **Enforcement/downstream:** AR-008/009 own topology, observability, thresholds and pressure testing.

## 4.5 I4 Consolidated Identity-Security Lifecycle Doctrine

```text
Canonical identity
    |
    +-- normal authentication
    +-- graduated recovery
    |
    v
Server-governed revocable session
    |
    +-- authentication assurance
    +-- expiring/revocable trusted-device context
    +-- bounded security capabilities/tokens
    |
    v
Current Ash policy + current authority
    |
    +-- ordinary operation
    +-- step-up / privileged elevation
    +-- compromise containment
    |
    v
Governed audit/security evidence

Recovery restores controlled identity access;
it does not manufacture domain authority or resurrect old trust.
```

## 4H. AR-004 Closure Audit — PASS

**Audit scope:** all frozen ARQs whose `Primary downstream workstreams` include `AR-004`.

**Mechanical routing count:** **119 ARQs**, comprising:
- `16` Performance ARQs;
- `81` Analytics ARQs;
- `3` System ARQs;
- `8` Identity/Authentication/Authorisation ARQs;
- `5` State/Storage/Lifecycle ARQs;
- `1` Async/Notification ARQ;
- `3` Content/Media ARQs;
- `1` Security ARQ;
- `1` Operations/Release ARQ.

**Closure result:** PASS. No unresolved AR-004-specific architecture contradiction or missing identity/authentication/authorisation/field-privacy mechanism remains.

### Closure coverage map

1. **Canonical identity, authentication and assurance** — `ARC-110...ARC-117`, `ARC-136...ARC-143` establish one canonical identity, proof-gated AshAuthentication integration, launch email/password + optional magic-link posture, capability-gated email verification, revocable server-governed sessions, contextual assurance/MFA boundaries, Argon2id preference, graduated recovery, sensitive identity-change handling, compromise containment, secure cookie transport, trusted-device lifecycle and bounded security capabilities.
2. **Role/capability/relationship authority and field privacy** — `ARC-118...ARC-125` establish contextual composable policy rather than role-only RBAC, explicit durable authority grants, relationship-scoped practitioner/private access, Ash policy enforcement, field policies + minimum-data loading, purpose-specific actions and current-state authority evaluation rather than stale session permission snapshots.
3. **Consent, privileged access, audit and revocation** — `ARC-126...ARC-135` establish purpose-specific consent/lawful-basis state, immutable grant/withdrawal evidence plus current-effective projection, immediate authority change with downstream invalidation, scoped/time-bounded privileged elevation, separate break-glass path, governed minimised immutable audit/security evidence, proportional denial logging, non-enumerating external failures and broadcast-as-acceleration-only revocation semantics.
4. **Recovery/merge/compromise/abuse lifecycle** — `ARC-136...ARC-145` establish deliberate identity reconciliation preserving provenance, compromise containment, individually revocable sessions/devices, single-purpose security tokens and layered distributed-capable abuse controls without prematurely mandating Redis at single-node launch.
5. **Performance/realtime/async ARQs routed through AR-004** — current authority is re-evaluated at the action boundary; material revocation has authoritative bypass plus prompt session effects; PubSub topic knowledge is not authorization; realtime/queue payloads remain minimised; queued work must revalidate current authority where required. Exact durable consequence/queue/PubSub topology remains AR-005/AR-008 work rather than AR-004 identity law.
6. **Analytics ARQs routed through AR-004** — analytics identity stitching, consent/purpose, sensitive-data exclusion, role-scoped dashboards, row/field restrictions, exports, scheduled reports, experiment privacy and governance all consume the same canonical identity/policy/consent/field-privacy model. Analytics does not receive a parallel authorization system. Metric/statistical semantics remain governed by frozen Analytics law and later AR-005/007/008/009 mechanics as already routed.
7. **State/content/media/export cross-cutting ARQs** — protected assets, participant exports, retained/held records, personalised/discovery content and provider-delivered media remain policy-first and minimum-data. AR-004 defines who may act/receive; AR-003 defines storage/delivery authority; AR-006/007 define provider/content/deletion/retention mechanics.
8. **System/product-space ARQs** — product-space activation and experience differences may contribute policy context, but product-space membership/visibility never becomes a substitute for canonical identity, explicit authority or field/privacy controls.
9. **Security/operations ARQs** — layered non-enumerating abuse control is established by `ARC-133`, `ARC-144`, `ARC-145`; named operational incident/release ownership, thresholds, provider rules and evidence pipelines remain AR-008/009 responsibility rather than an unresolved AR-004 authorization mechanism.

### Explicit downstream handoff — not unresolved AR-004 work

AR-004 deliberately does **not** freeze:
- final concrete business role/capability vocabulary or owning Domains;
- exact identity/session/role/relationship/consent/audit Resources, tables, columns or indexes;
- exact Ash policy modules/check implementations or field-policy code;
- exact MFA factor/provider, WebAuthn/passkey implementation or step-up windows;
- exact idle/absolute session timeouts, cookie names, token formats or trusted-device expiry values;
- exact account-recovery evidence, security-hold durations or support workflow UI;
- exact duplicate-identity merge rules for each affected business Domain;
- exact abuse/rate thresholds, Redis/PostgreSQL coordination structures, Cloudflare rules or challenge/CAPTCHA provider;
- exact audit storage technology, retention durations or security-event pipeline;
- durable revocation/notification/outbox/job/PubSub propagation mechanics;
- deletion/retention/legal-hold/backup interactions after authority changes;
- provider/content/media-specific policy adapters;
- operational incident/release processes, observability and security pressure-test thresholds.

Those matters remain intentionally routed to AR-005...AR-009, `04_DOMAIN_MAP.md`, Domain Architecture Profiles, JIT Domain Dossiers, Architectural Proof and expert/vendor gates as applicable.

### AR-004 closure determination

- Product Law change required: **NO**
- ARQ amendment required: **NO**
- New I5 decision round required: **NO**
- Contradiction discovered: **NO**
- AR-004 status: **COMPLETE**
- Accepted AR-004 Architecture Law: `ARC-110...ARC-145`
- Next workstream: **AR-005 — Transactions, Consistency, Async & Realtime**



# 4I. AR-005 — Transactions, Consistency, Async & Realtime

## 4I.1 Round TC1 — Transaction Commit & Durable Consequence Boundary

**Accepted answer set:** `TC1.1 B, TC1.2 B, TC1.3 B, TC1.4 B, TC1.5 B, TC1.6 B, TC1.7 B, TC1.8 B, TC1.9 B, TC1.10 B`

## ARC-146 — Mandatory asynchronous consequences establish durable intent atomically with authoritative state

- **Decision source:** AR-005 TC1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-087`, `ARQ-PERF-099`, `ARQ-PERF-038`, `ARQ-ASYNC-001`, `ARQ-ASYNC-002`
- **Decision:** When a business transition requires follow-on asynchronous work that must not be lost, the originating authoritative transaction must establish durable execution intent atomically with the business transition, or use an equivalently robust durable commit-bridge. A transactionally inserted Oban job is sufficient when the job record itself fully represents the required execution intent; a distinct durable consequence/domain-intent record is used where the intent has independent lifecycle, reconciliation, audit, fan-out or downstream-consumer meaning.
- **Rationale:** A successful business commit followed by an ephemeral enqueue/network step creates a crash window in which mandatory work may disappear. Conversely, requiring a separate outbox row for every trivial task creates redundant ceremony where PostgreSQL-backed transactional job insertion already supplies the needed durability.
- **Rules:**
  1. Mandatory consequences may not depend on fire-and-forget Tasks, process mailboxes, PubSub delivery or post-response callbacks.
  2. The durable intent is committed in the same transaction as the state transition when those semantics are required.
  3. Distinct consequence/domain records are introduced by semantic need, not universally.
  4. Consequence creation failure causes the authoritative transaction to fail when the consequence is mandatory to that transition.
- **Failure behaviour:** After commit, process/node loss cannot erase the recorded obligation; recovery can rediscover pending work from durable state.
- **Enforcement/downstream:** AR-008/JIT work owns exact Oban configuration, job schemas and operational reconciliation tooling.

## ARC-147 — Slow or non-transactional external calls stay outside authoritative database transactions

- **Decision source:** AR-005 TC1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-037`, `ARQ-PERF-038`, `ARQ-PERF-099`, applicable provider ARQs
- **Decision:** Authoritative PostgreSQL transactions contain the smallest coherent durable state transition and required durable consequence intent; slow or non-transactional calls to payment, email, object-storage, messaging or other providers execute after commit through the approved consequence path. Holding database locks while waiting on remote systems is prohibited unless a later proof demonstrates an unavoidable and safe exception.
- **Rationale:** Remote latency and ambiguity must not extend database lock duration, consume scarce connections or make local transaction success depend on an external system that cannot participate in the same atomic commit.
- **Rules:**
  1. An Ash `after_transaction` callback may coordinate non-critical post-commit work but is not by itself sufficient durability for a mandatory consequence.
  2. Provider calls execute from durable work or another explicit post-commit mechanism.
  3. Ambiguous external outcomes are reconciled through authoritative evidence rather than by holding the transaction open.
- **Performance/scaling:** Protects OLTP connection/lock budgets and prevents provider slowness from directly serialising authoritative writes.

## ARC-148 — Oban is the preferred durable asynchronous executor; AshOban is the preferred Ash-native integration candidate

- **Decision source:** AR-005 TC1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-087`, `ARQ-PERF-088`, `ARQ-PERF-106`, `ARQ-PERF-113`
- **Decision:** Oban is selected as the platform's default durable PostgreSQL-backed asynchronous execution engine, subject to normal dependency proof/version governance. AshOban is the preferred integration candidate where resource actions naturally map to background triggers/scheduled actions. Neither Oban nor AshOban owns business truth; they execute durable business/consequence intent governed by application/domain state.
- **Rationale:** The required durability, transactional insertion, retry/recovery and PostgreSQL alignment fit the locked stack without introducing an independent queue authority. AshOban can reduce glue code where Ash actions already express the operation.
- **Rules:**
  1. Ordinary durable background work uses Oban unless a concrete capability requires another mechanism.
  2. Queue/job state is operational state, not a substitute for domain state.
  3. Worker topology may later separate from web nodes without changing application semantics.
  4. Exact queue names, plugins, limits and worker deployment remain later architecture/JIT decisions.
- **Amendment relationship:** This resolves the package-selection question deferred by `ARQ-PERF-088`; it does not make every possible future async workload permanently dependent on one package if a later explicit supersession is justified.

## ARC-149 — Important asynchronous effects assume re-execution and are repeat-safe/idempotent

- **Decision source:** AR-005 TC1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-026`, `ARQ-PERF-028`, `ARQ-PERF-035`, `ARQ-PERF-097`, `ARQ-PERF-113`, `ARQ-ASYNC-003`
- **Decision:** The platform never assumes exactly-once worker-process execution. Important workers and provider-facing consequences must tolerate retry, duplicate execution, crash after external effect, reordered delivery and equivalent replay through business idempotency, durable invariants and reconciliation.
- **Rationale:** A worker can complete an external side effect and fail before recording local completion; retries are therefore normal rather than exceptional.
- **Rules:**
  1. Retryability is designed at the effect boundary, not merely configured in Oban.
  2. External provider idempotency facilities are used where appropriate but do not replace local authoritative invariants/reconciliation.
  3. Retry exhaustion never retroactively proves that the business obligation disappeared or failed safely.
- **Failure behaviour:** Ambiguous outcomes remain explicit and reconciled rather than blindly reissued or declared successful.

## ARC-150 — Queue uniqueness is duplicate-work suppression, not business idempotency

- **Decision source:** AR-005 TC1.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-098`, `ARQ-PERF-027`, `ARQ-PERF-030`, `ARQ-PERF-097`
- **Decision:** Oban uniqueness may suppress redundant enqueueing or concurrent duplicate work according to a bounded queue-level key/window, but it cannot establish the authoritative at-most-once business effect. Business idempotency remains defined by operation/actor/context identity and durable domain constraints/evidence.
- **Rationale:** Job uniqueness cannot prove whether a provider effect already occurred before a crash, nor can a queue retention window represent permanent business uniqueness such as one entitlement grant.
- **Rules:**
  1. Unique-job keys/windows are operational optimisations.
  2. Domain idempotency survives pruning, queue reconfiguration and job deletion.
  3. Worker execution still validates authoritative business state even when a job was uniquely enqueued.

## ARC-151 — Durable job payloads contain stable identifiers and minimal routing/provenance metadata

- **Decision source:** AR-005 TC1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-104`, `ARQ-IAM-007`, applicable privacy/deletion ARQs
- **Decision:** Durable job arguments preferentially contain stable identifiers, authoritative version/reference identity where relevant, operation/correlation identity and minimal routing metadata. Workers re-read current authorised state at execution. Persisting sensitive personal, clinical, health or other protected payload data in queue storage requires an explicit privacy, encryption, retention, deletion and access justification.
- **Rationale:** Durable queues persist and are operationally inspectable; copying full business records into jobs increases privacy residue, stale-state risk and deletion complexity.
- **Rules:**
  1. Do not serialize entire Ash resources, sessions or broad actor snapshots into jobs by default.
  2. Secrets/tokens are excluded from ordinary args unless a narrowly governed capability explicitly requires them.
  3. Job payload deletion/retention remains compatible with privacy/deletion law.
- **Security/privacy:** Queue storage is treated as durable application data with least-data access controls rather than an invisible implementation detail.

## ARC-152 — Causal provenance is separate from current execution authority

- **Decision source:** AR-005 TC1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-103`, `ARQ-IAM-007`, `ARQ-IAM-008`, `ARQ-ASYNC-003`
- **Decision:** Durable work preserves enough causal provenance to identify the initiating actor/system/operation where required, but execution authority is evaluated separately at run time. A delayed job uses the appropriate current system/service authority or explicitly reconstructed actor context and revalidates material current permissions/preconditions rather than permanently impersonating a stale historical user session.
- **Rationale:** Audit needs to know who caused work, while authorization needs to know whether the work remains permitted now; collapsing those concepts either destroys provenance or freezes stale authority.
- **Rules:**
  1. `caused_by`/correlation provenance does not itself grant permission.
  2. System/service execution authority is explicit and least-privileged.
  3. Where a user's current authority is essential to execution, it is re-evaluated against current authoritative state.

## ARC-153 — Queued work revalidates current preconditions and may no-op, cancel, supersede or defer safely

- **Decision source:** AR-005 TC1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-103`, `ARQ-ASYNC-002`, `ARQ-IAM-006`, applicable lifecycle/revocation ARQs
- **Decision:** Important queued work re-reads material current state at execution and follows its contract when the original intent has become invalid, withdrawn, superseded, already satisfied or temporarily unsafe. Valid outcomes include execution, idempotent no-op, explicit cancellation, supersession or controlled defer/snooze; historical enqueueing never overrides current authority.
- **Rationale:** Consent, access, publication approval, payment state, safety state and business dependencies can legitimately change between enqueue and execution.
- **Rules:**
  1. Precondition checks are domain-specific and not replaced by queue age/uniqueness.
  2. Permanent invalidity is not blindly retried as a transient error.
  3. A no-op/cancel/supersede outcome remains observable where operationally material.
- **Failure behaviour:** Stale work fails safe rather than resurrecting revoked/superseded effects.

## ARC-154 — Queue execution state is operational evidence, never authoritative business status

- **Decision source:** AR-005 TC1.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-040`, `ARQ-PERF-096`, `ARQ-PERF-109`, `ARQ-ASYNC-001`, `ARQ-ASYNC-002`
- **Decision:** Oban job states such as available, scheduled, executing, retryable, completed, discarded or cancelled describe operational execution state only. Authoritative domain/consequence records determine whether the business obligation is pending, effective, complete, failed, cancelled, superseded or unresolved. Job terminal failure is surfaced and reconciled without rewriting an already-valid authoritative commit.
- **Rationale:** A completed worker may still have produced an ambiguous provider outcome, while a discarded worker may leave a valid business obligation outstanding.
- **Rules:**
  1. Business UI/API state is not inferred solely from Oban row state.
  2. Critical exhausted work retains enough durable domain/consequence identity for controlled reconciliation.
  3. Job pruning cannot erase required business/audit evidence.

## ARC-155 — Separate outbox/consequence records are semantic tools, not a universal mandatory layer

- **Decision source:** AR-005 TC1.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-038`, `ARQ-PERF-099`, `ARQ-ASYNC-001`, `ARQ-ASYNC-002`, `ARQ-ASYNC-003`
- **Decision:** The architecture does not mandate a generic outbox/event row for every state change. A transactionally inserted Oban job may be the durable post-commit execution intent when that is sufficient. A distinct outbox/consequence/domain-intent record is required when the intent has independent business/operational lifecycle, reconciliation, audit, multi-consumer fan-out or retention meaning beyond one queue execution record.
- **Rationale:** This preserves the transactional-outbox reliability property without duplicating durable records or creating an event architecture before there is semantic need.
- **Rules:**
  1. The choice is made per consequence class, not per developer preference at each call site.
  2. Distinct intent records have explicit ownership and lifecycle.
  3. PubSub/transient messages cannot substitute for durable intent when the consequence is mandatory.
  4. Future external event-stream integration may consume governed durable consequence/domain events without forcing every internal job to become an integration event today.

## 4I.2 TC1 Consolidated Commit-to-Consequence Doctrine

```text
Authoritative Ash action
        |
        v
PostgreSQL transaction
   +-- commit authoritative business state
   +-- commit mandatory durable consequence intent
        |        (Oban job OR first-class consequence record + job)
        v
      COMMIT
        |
        v
Durable Oban executor
   +-- reload current state
   +-- revalidate authority/preconditions
   +-- execute repeat-safely
   +-- retry / snooze / cancel / supersede as governed
   +-- record operational execution evidence
        |
        v
Authoritative domain/consequence state remains business truth
```

**AR-005 status:** IN PROGRESS. TC1 resolves the transaction-to-durable-async handoff and selects Oban as the default durable executor. Queue isolation/capacity/backpressure, scheduling, retry classification, terminal-failure operations and multi-node worker topology remain TC2/downstream work.


## 4I.3 Round TC2 — Queue Isolation, Backpressure, Scheduling & Worker Topology

**Accepted answer set:** `TC2.1 B, TC2.2 B, TC2.3 B, TC2.4 B, TC2.5 B, TC2.6 B, TC2.7 B, TC2.8 B, TC2.9 B, TC2.10 B, TC2.11 B`

## ARC-156 — Queue and capacity isolation follows workload characteristics rather than resource/domain names

- **Decision source:** AR-005 TC2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-089`, `ARQ-PERF-090`, `ARQ-PERF-110`, `ARQ-PERF-113`
- **Decision:** Durable work with materially different criticality, latency/freshness SLO, CPU/memory/I/O profile, PostgreSQL pressure, external-provider dependency, failure behaviour or bulk/fan-out characteristics must be isolatable into separate Oban queues or equivalent capacity pools. Final queue names/counts are not Architecture Law and are defined by evidence/JIT configuration.
- **Rationale:** Queue isolation is a failure/resource boundary. Mapping queues mechanically to Resources or Domains would ignore the actual bottleneck and allow one expensive workload to starve unrelated obligations.
- **Rules:**
  1. Queue placement is derived from workload behaviour and criticality.
  2. Low-value/bulk work must remain independently throttleable, pausable or deferrable.
  3. Queue structure may evolve without changing domain/application semantics.
- **Enforcement/downstream:** AR-008/AR-009/JIT owns concrete queue inventory, capacity values and pressure tests.

## ARC-157 — Job priority orders work within an appropriate isolation boundary; it does not create isolation

- **Decision source:** AR-005 TC2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-089`, `ARQ-PERF-090`
- **Decision:** Job priority may order work within a queue whose workload characteristics already belong together, but priority alone must never substitute for separate resource/failure isolation between fundamentally different workload classes.
- **Rationale:** A high-priority job still competes for the same worker, database and downstream capacity if it shares a queue with heavy or failure-prone work.
- **Rules:** Priority is a local ordering tool; queue/capacity separation is the architectural isolation tool.

## ARC-158 — Worker concurrency is budgeted from the tightest downstream resource envelope

- **Decision source:** AR-005 TC2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-091`, `ARQ-PERF-111`, `ARQ-PERF-073`, `ARQ-PERF-074`, `ARQ-PERF-113`
- **Decision:** Queue concurrency is derived from the limiting system/downstream envelope—PostgreSQL connections/query budget, CPU, RAM, I/O, provider rate/concurrency limits, external process capacity, contention and job duration—rather than from BEAM scheduler/process capacity alone. Interactive OLTP headroom is explicitly reserved.
- **Rationale:** BEAM processes are cheap; database connections, external APIs and CPU-heavy transforms are not. Async work shares the same finite platform resources as interactive operations.
- **Rules:**
  1. No queue receives unlimited PostgreSQL capacity because it is asynchronous.
  2. Provider-specific concurrency is bounded to the provider contract/evidence.
  3. Capacity values are tuned from representative load evidence rather than globally hard-coded in Architecture Law.

## ARC-159 — Ordinary queue concurrency is treated as node-local; strict global limits require explicit cluster-wide control

- **Decision source:** AR-005 TC2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-091`, `ARQ-PERF-102`, `ARQ-PERF-106`, `ARQ-PERF-111`, `ARQ-PERF-113`
- **Decision:** Core Oban queue concurrency is treated as local to each node running that queue; effective ordinary concurrency therefore scales with worker-node count. Before a workload depends on a strict platform-wide cap, architecture must provide deliberate bounded worker placement, shared/global coordination, a proof-gated global-limits capability such as an appropriate Oban Pro engine, or another proven mechanism. Oban Pro is not required at launch merely to satisfy this future boundary.
- **Rationale:** Scaling worker nodes must not accidentally multiply payment/provider/database concurrency beyond safe limits.
- **Failure/scaling behaviour:** Single-node launch may use local limits directly; scale-out triggers aggregate-capacity recalculation before additional nodes run constrained queues.

## ARC-160 — Durable queues are bounded operational buffers with explicit backpressure and degradation behaviour

- **Decision source:** AR-005 TC2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-092`, `ARQ-PERF-100`, `ARQ-PERF-107`, `ARQ-PERF-108`, `ARQ-PERF-110`, `ARQ-PERF-111`, `ARQ-PERF-112`
- **Decision:** Material queues require observable backlog/freshness state and controlled pressure responses before accumulation threatens authoritative OLTP capacity. Permitted mechanisms include producer throttling/admission control, coalescing, batching, pausing/deferment, reduced consumer concurrency and explicit shedding of disposable low-value work. Autoscaling is one possible response, not the default or sole control.
- **Rationale:** PostgreSQL durability does not make backlog capacity infinite; uncontrolled queues can convert a downstream slowdown into database and recovery failure.
- **Rules:** Critical correctness obligations may be delayed/degraded according to their contract but may not silently disappear merely to relieve pressure.

## ARC-161 — Retry behaviour is error-class-aware, bounded and jittered rather than one universal policy

- **Decision source:** AR-005 TC2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-093`, `ARQ-PERF-094`, `ARQ-PERF-095`, `ARQ-PERF-096`, `ARQ-PERF-097`, `ARQ-PERF-109`, `ARQ-ASYNC-003`
- **Decision:** Async failures are classified at minimum as transient/retryable, provider rate-limit/outage, permanently invalid business input/state, superseded/revoked, unexpected system defect, or ambiguous external outcome. Retryable failures use bounded error-appropriate backoff with jitter; permanent/superseded work does not blind-retry; ambiguous irreversible external outcomes reconcile before repeat execution.
- **Rationale:** One retry policy can amplify provider outages, repeat irreversible effects, or waste capacity on permanently invalid work.
- **Failure behaviour:** Exhausted retries never imply business success or erase an outstanding authoritative obligation.

## ARC-162 — Shared dependency outages trigger coordinated degradation rather than independent worker hammering

- **Decision source:** AR-005 TC2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-095`, `ARQ-PERF-092`, `ARQ-PERF-110`, `ARQ-PERF-113`
- **Decision:** A prolonged shared provider/dependency outage must support coordinated slowdown, snoozing/deferment, pausing, concurrency reduction, circuit/degraded behaviour or equivalent control across affected workload classes while unrelated work remains operational. Node-local queue pause alone is not assumed to be a future cluster-wide circuit.
- **Rationale:** Independent retries across many workers/nodes can hammer the failed dependency and create a secondary PostgreSQL/retry storm.
- **Enforcement/downstream:** AR-008/JIT chooses the shared degradation-state mechanism, thresholds and operator controls.

## ARC-163 — Exhausted work requires dead-letter semantics without mandating a separate physical DLQ

- **Decision source:** AR-005 TC2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-096`, `ARQ-PERF-109`, `ARQ-PERF-107`, `ARQ-PERF-113`
- **Decision:** After approved retry exhaustion, work moves into an explicit inspectable terminal operational state such as discarded/quarantined/cancelled as appropriate, with diagnostic evidence, criticality-based alerting and controlled reconciliation/replay. A separate physical `dead_letter` queue/table is not mandated when Oban terminal states plus authoritative consequence/domain state provide the required semantics.
- **Rationale:** The invariant is inspectable unresolved work, not imitation of another queue ecosystem's storage terminology.
- **Rules:** Job pruning may not erase an unresolved business obligation or required audit/reconciliation evidence.

## ARC-164 — One-off scheduling, periodic platform work and dynamic business-effective schedules are distinct concepts

- **Decision source:** AR-005 TC2.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-101`, `ARQ-PERF-102`, `ARQ-PERF-103`, `ARQ-ASYNC-002`
- **Decision:** One-off future consequences may use durable scheduled Oban jobs; static platform periodic work may use core Oban Cron or an equivalent cluster-safe scheduler; dynamic business schedules remain authoritative application/domain state whose promised effective-time semantics are separate from worker execution time and whose execution is durable, idempotent, recoverable and revalidated at run time. Oban Pro DynamicCron is optional/proof-gated rather than required by Product/Architecture Law.
- **Rationale:** A user's/programme's schedule is business truth; cron configuration and worker wake-up time are execution mechanisms.
- **Rules:** Multi-node periodic issuance must produce one logical business issuance or equivalent deduplication.

## ARC-165 — Large fan-out is a bounded, observable producer/batcher/consumer pipeline

- **Decision source:** AR-005 TC2.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-100`, `ARQ-PERF-092`, `ARQ-PERF-110`, `ARQ-PERF-111`, `ARQ-PERF-112`
- **Decision:** Large fan-out may not synchronously spawn unbounded tasks/jobs/requests per recipient. It is implemented as a controlled pipeline with bounded production/batching, isolated bounded consumer concurrency, provider-aware throughput and measurable remaining backlog. Exact batch sizes are evidence/JIT values.
- **Rationale:** Fan-out must preserve OLTP and downstream-provider stability under hundreds of thousands of recipients/objects, not merely work for small test sets.

## ARC-166 — Worker execution remains runtime-separable without becoming a new domain/service boundary

- **Decision source:** AR-005 TC2.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-105`, `ARQ-PERF-106`, `ARQ-PERF-111`, `ARQ-PERF-112`; cross-reference `ARC-006`, `ARC-015`
- **Decision:** Launch may run web and Oban workers together in one application instance. Runtime configuration must nevertheless allow selected queues to move onto worker-focused nodes/pools when measured contention, reliability or resource evidence justifies it, without changing business/domain semantics or requiring a new codebase/service boundary. Deployment/shutdown stops fetching new work, allows bounded graceful completion and leaves unfinished/orphaned jobs recoverable.
- **Rationale:** Worker separation is an operational topology decision, not a business architecture rewrite.
- **Failure/deployment behaviour:** In-flight work is never marked complete merely to permit deployment; interrupted work remains recoverable under Oban/authoritative consequence semantics.

## 4I.4 TC2 Consolidated Queue/Capacity Doctrine

```text
Durable work
     |
     +--> queue/capacity class chosen by workload characteristics
     |       +-- criticality / freshness
     |       +-- DB / CPU / RAM / I/O profile
     |       +-- provider dependency
     |       +-- bulk/fan-out / failure behaviour
     |
     +--> bounded concurrency from tightest resource budget
     |       +-- ordinary core queue limits are per node
     |       +-- strict global limits need explicit cluster-wide control
     |
     +--> observable backlog/freshness
     |       +-- throttle / coalesce / batch / pause / defer / shed where safe
     |
     +--> error-class-aware bounded retry + jitter
     |       +-- shared outage => coordinated degradation
     |       +-- exhausted => inspectable terminal state + reconciliation
     |
     +--> schedule semantics
     |       +-- one-off durable schedule
     |       +-- cluster-safe static periodic work
     |       +-- dynamic business schedule remains authoritative domain state
     |
     +--> bounded fan-out
     |
     `--> launch combined web+worker; later separate worker pools by evidence
```

**AR-005 status:** IN PROGRESS. TC1 and TC2 now resolve the transaction-to-durable-work handoff and the durable queue/capacity/failure/scheduling topology. Provider callback/reconciliation semantics, notification consequences, business-effective scheduling application semantics and realtime/PubSub consistency remain TC3/downstream work.
## 4I.5 AR-005 TC3 — Provider Evidence, Notifications, Scheduling & Realtime Consistency

> **Accepted answer set:** `TC3.1 B, TC3.2 B, TC3.3 B, TC3.4 B, TC3.5 B, TC3.6 B, TC3.7 B, TC3.8 B, TC3.9 B, TC3.10 B, TC3.11 B, TC3.12 B`.
>
> **Scope guardrail:** TC3 resolves cross-boundary consistency semantics for external provider evidence, governed notification consequences, business-effective scheduling and realtime observation. It does not freeze provider-specific Paystack status semantics, notification vendors/templates, final queue names, PubSub topic strings, exact retry/timing constants, or Domain ownership reserved for vendor proof, AR-006/008/009, Domain Law and JIT dossiers.

## ARC-167 — Provider callbacks use verify → durable receipt → acknowledge → asynchronous reconciliation

- **Decision source:** AR-005 TC3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-026`, `ARQ-PERF-028`, `ARQ-PERF-038`, `ARQ-PERF-087`, `ARQ-PERF-099`, `ARQ-ASYNC-003`, `ARQ-PAY-001`
- **Decision:** External provider callbacks/webhooks first pass provider-appropriate authentication/signature/origin verification and basic envelope validation, then establish durable canonical receipt/evidence plus any mandatory processing intent before the platform returns successful acknowledgement. Material provider processing/reconciliation proceeds behind the authoritative application boundary asynchronously where appropriate. The platform must not acknowledge durable receipt if the receipt/intent transaction failed.
- **Rationale:** A provider may retry, duplicate or reorder delivery, and synchronous downstream processing may be slow or fail after the provider request arrives. Durable receipt before acknowledgement prevents silent loss while keeping provider ingress bounded.
- **Security/failure behaviour:** Secret callback URLs are not authentication by themselves. Invalid/unverified requests do not enter governed provider state; transient persistence failure yields a retryable provider response rather than false success.

## ARC-168 — Verified provider callbacks are authenticated external evidence, not unqualified platform authority

- **Decision source:** AR-005 TC3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-025`, `ARQ-PERF-026`, `ARQ-PERF-028`, `ARQ-PERF-029`, `ARQ-PERF-030`, `ARQ-PERF-040`, `ARQ-ASYNC-003`, `ARQ-PAY-001`
- **Decision:** A verified provider callback is reconciled through the owning application/domain action against the matching platform operation/reference, expected relationships and relevant current authoritative state before it changes payment, entitlement or other business truth. Provider status remains external evidence behind the provider boundary; platform durable state plus approved reconciliation rules determine the authoritative transition.
- **Rationale:** Verification proves who sent the message, not that every implied business consequence is currently valid or has not already occurred through another path.
- **Downstream:** Exact Paystack event/status/refund/subscription/dispute semantics remain OQ-004/vendor-validation/JIT work.

## ARC-169 — Provider ingress and reconciliation are duplicate-safe and arrival-order independent

- **Decision source:** AR-005 TC3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-026`, `ARQ-PERF-027`, `ARQ-PERF-028`, `ARQ-PERF-029`, `ARQ-PERF-041`, `ARQ-ASYNC-003`
- **Decision:** Provider evidence has stable identity/deduplication and repeat-safe processing so replay/retry cannot multiply business consequences. Network arrival order, callback timestamps or “last callback wins” are not authoritative ordering rules. Older/duplicate evidence may no-op, while ambiguous ordering or outcome triggers governed reconciliation against current provider and platform state.
- **Rationale:** External delivery is an at-least-once, delay/reordering-prone observation channel; business state machines must not regress merely because an older callback arrived later.

## ARC-170 — Notification business truth, durable intent and provider delivery evidence are separate state classes

- **Decision source:** AR-005 TC3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-ASYNC-001`, `ARQ-PERF-087`, `ARQ-PERF-099`, `ARQ-PERF-104`, `ARQ-PERF-113`
- **Decision:** Notification delivery is modelled as a durable consequence of authoritative business truth. Where lifecycle/audit/reconciliation semantics warrant it, a governed notification intent records the semantic purpose, recipient identity/reference, eligible channel/policy context, template/version/correlation provenance and delivery lifecycle without duplicating unnecessary sensitive business payload. Provider delivery identifiers/status remain delivery evidence and never create/replace the originating business event.
- **Rationale:** Separating meaning from transport permits retry, provider substitution, preference changes, audit and reconciliation without confusing “email sent” with “business event happened.”

## ARC-171 — Material notification policy/preconditions are revalidated before delivery when they can legitimately change

- **Decision source:** AR-005 TC3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-ASYNC-001`, `ARQ-PERF-103`, `ARQ-IAM-006`
- **Decision:** Notification intent creation evaluates applicable category/purpose/channel policy, and delayed delivery revalidates material current conditions that may legitimately suppress, alter or invalidate the message. Completed actions suppress obsolete reminders; consent withdrawal affects future optional/marketing delivery; mandatory security/transactional communication follows its separately governed lawful/product basis.
- **Rationale:** Historic enqueueing is not perpetual permission to deliver a now-obsolete or no-longer-authorised message.

## ARC-172 — Material notifications have semantic durable deduplication independent of queue uniqueness

- **Decision source:** AR-005 TC3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-ASYNC-001`, `ARQ-PERF-027`, `ARQ-PERF-097`, `ARQ-PERF-098`
- **Decision:** Notification deduplication is defined by the semantic notification purpose and originating business identity/version for the recipient rather than by subject text, provider ID or Oban uniqueness alone. Worker retries, duplicate observations and provider retries may not generate an extra message unless the approved product rule actually calls for another notification.
- **Rationale:** Queue uniqueness suppresses redundant execution; it does not define whether two messages are the same business communication.

## ARC-173 — Time-self-effective state and execution-gated scheduled transitions are distinct scheduling semantics

- **Decision source:** AR-005 TC3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-007`, `ARQ-PERF-101`, `ARQ-PERF-102`, `ARQ-PERF-103`, `ARQ-ASYNC-002`
- **Decision:** Scheduled business semantics are classified explicitly. **Time-self-effective state** already contains the approved authoritative `effective_from`/`effective_until`-style conditions so reads/actions derive effect from authoritative time and a delayed worker does not shift the promised effective instant. **Execution-gated transitions** require a governed action at execution, revalidate approvals/safety/access/dependencies/current authority and become effective only when that transition succeeds within its approved freshness/SLO. Cron/job wake-up configuration is never itself business authority.
- **Rationale:** Product promises such as an already-approved effective window and safety-sensitive publication/release workflows have different correctness semantics and must not be forced through one scheduler model.
- **Failure behaviour:** Cluster-safe issuance/deduplication still applies; failed execution-gated transitions remain visible/recoverable rather than silently skipping or double-publishing.

## ARC-174 — Best-effort realtime observations are emitted only after authoritative commit; mandatory consequences use durable paths

- **Decision source:** AR-005 TC3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-038`, `ARQ-PERF-039`, `ARQ-PERF-114`, `ARQ-PERF-128`, `ARQ-PERF-138`
- **Decision:** Ordinary realtime UI freshness uses an after-commit notifier/observation boundary such as Phoenix PubSub and may carry a small safe projection, identity/version or change type. PubSub is appropriate only where loss is acceptable because clients can reconstruct/re-read authority. A consequence that must survive process/node failure uses the durable TC1/Oban/consequence path instead of relying on notifier/PubSub delivery.
- **Rationale:** Broadcasting pre-commit or treating best-effort notification as a durable business handoff can expose state that rolls back or silently lose required work.

## ARC-175 — PubSub topics are narrowly scoped routing boundaries; topic knowledge never grants authorization

- **Decision source:** AR-005 TC3.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-119`, `ARQ-PERF-120`, `ARQ-PERF-121`
- **Decision:** PubSub topics/subscriptions use the smallest sensible audience/business scope such as actor/resource/event/cohort or another approved boundary, and realtime payloads are minimised for privacy/fan-out. Topic names, identifiers or obscurity are routing only; subscription/connect access and authoritative actions remain explicitly authorized through current policy.
- **Rationale:** Broad topics amplify CPU/network/privacy exposure, while secret-looking topic names are not an access-control mechanism.
- **Downstream:** Exact topic naming and subscription topology belong to Domain/JIT design.

## ARC-176 — Realtime consumers assume delayed, missing, duplicate and reordered observations

- **Decision source:** AR-005 TC3.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-117`, `ARQ-PERF-127`, `ARQ-PERF-128`, `ARQ-PERF-138`
- **Decision:** Business correctness may not depend on global PubSub ordering or exactly-once observation. When ordering/freshness matters, observations carry/use an authoritative version/sequence or trigger a current-state read. Duplicate observations are repeat-safe and may not create duplicate durable effects.
- **Rationale:** Realtime distribution is an observation layer across reconnects/nodes and must tolerate normal distributed delivery uncertainty.

## ARC-177 — Realtime refresh shape is selected to bound fan-out, database amplification and stale intermediate work

- **Decision source:** AR-005 TC3.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-121`, `ARQ-PERF-126`, `ARQ-PERF-132`, `ARQ-PERF-133`, `ARQ-PERF-138`
- **Decision:** Low/moderate-fan-out realtime may broadcast a small invalidation/version signal followed by a bounded authoritative projection reload. Where that creates N×M database amplification, the platform may use prepared safe projections, coalescing, batching or equivalent fan-out controls. Obsolete visual intermediate states may be skipped when only current state matters.
- **Rationale:** “Broadcast ID then every subscriber queries PostgreSQL” is not a universal scaling strategy; realtime freshness must share the same finite database/CPU/network budget as the rest of the platform.

## ARC-178 — UI confirmation comes from the authoritative action/state, not a PubSub echo

- **Decision source:** AR-005 TC3.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-117`, `ARQ-PERF-118`, `ARQ-PERF-130`; cross-reference `ARC-052`, `ARC-053`
- **Decision:** The result of the authoritative application action/state confirms a mutation. Absence or receipt of a realtime broadcast does not prove success/failure. If connectivity drops during an ambiguous operation, the UI exposes unconfirmed/reconnecting state where material and reconstructs/re-reads authority after reconnect rather than blindly replaying the action or assuming failure/success.
- **Rationale:** PubSub is best-effort freshness. Conflating it with command acknowledgement creates duplicate writes and false-success UX during ordinary disconnects/reconnects.

## 4I.6 TC3 Consolidated Cross-Boundary Consistency Doctrine

```text
External provider callback
        |
        +--> verify + durable receipt/intent --> acknowledge
        |                                  |
        |                                  `--> governed reconciliation --> authority
        |
Authoritative business state
        |
        +--> mandatory consequence --> durable intent / Oban --> provider delivery/reconciliation
        |
        +--> governed notification intent --> current policy revalidation --> provider evidence
        |
        +--> scheduled semantics
        |       +-- time-self-effective state
        |       `-- execution-gated transition + revalidation
        |
        `--> after-commit realtime observation --> PubSub --> bounded/reconstructable UI projection

Provider evidence != platform authority
Provider/network arrival order != business ordering
Job/provider delivery state != business truth
PubSub freshness != command acknowledgement
```

**AR-005 status:** TC1–TC3 accepted through `ARC-178`; closure audit follows before any TC4 is created.

## 4I.7 AR-005 Preliminary Closure Audit — TC4 REQUIRED

- **Audit date:** 2026-08-17
- **Frozen ARQ surface audited:** **234** requirements whose primary downstream workstreams include `AR-005`.
- **Family counts:** Performance 106; Analytics 118; Payments 1; IAM 2; State 3; Async 3; Content 1.
- **Result:** **NOT YET CLOSED — one surgical TC4 required.** TC1–TC3 cover transaction/commit semantics, durable work, queue/backpressure/retry/topology, provider reconciliation, notification consequences, scheduling and realtime/PubSub consistency. The audit found two residual AR-005 mechanism clusters that are still architecture-significant rather than merely Domain/JIT detail:
  1. **Analytics commit/replay consistency** — required server-side analytics facts/events need an explicit durable commit bridge, stable event identity/schema/time semantics, idempotent replay/backfill and deterministic late/out-of-order convergence while ordinary analytics failure remains non-blocking to committed business truth (`ARQ-AN-133`–`ARQ-AN-145` relevant subset, especially `AN-135`–`AN-145`).
  2. **Experiment assignment/exposure consistency** — the first-party experiment capability needs an explicit platform-owned deterministic A/B/n assignment boundary, sticky/versioned allocation, exposure-as-experienced evidence, interaction/mutual-exclusion semantics and safe failure/default behaviour (`ARQ-AN-181`, `AN-184`–`AN-216` relevant subset).
- **Correct deferrals confirmed:** exact analytics warehouse/streaming infrastructure, statistical implementation, experiment authoring UI, content/email template ownership, provider packages, queue/topic names, operational thresholds and Domain ownership remain downstream AR-006/008/009, Domain Law, OQ-040/proof and JIT work.
- **Governance conclusion:** Do not close AR-005 or advance the tracker to AR-006 until TC4 is decided. No Product Law/ARQ contradiction was found; this is an architecture coverage gap only.


## 4I.8 AR-005 TC4 — Analytics Commit/Replay & Experiment Assignment/Exposure Consistency

> **Accepted answer set:** `TC4.1 B, TC4.2 B, TC4.3 B, TC4.4 B, TC4.5 B, TC4.6 B, TC4.7 B, TC4.8 B, TC4.9 B, TC4.10 B`.
>
> **Scope guardrail:** TC4 closes the two mechanism gaps identified by the preliminary AR-005 audit: durable/replayable analytics consistency and deterministic experiment assignment/exposure consistency. It does not select an analytics warehouse, streaming platform, statistical package, experiment-authoring UI, exact hashing library, third-party flag package, data-retention values, final Domain ownership, or email/page content implementation reserved for AR-006/007/008/009, Domain Law, OQ-040/proof and JIT dossiers.

## ARC-179 — Important business analytics facts originate from or reconcile to authoritative server/domain state

- **Decision source:** AR-005 TC4.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-135`, `ARQ-AN-136`; cross-reference `ARQ-PERF-038`
- **Decision:** Important business analytical facts such as payment, entitlement, refund, completion, safety or other governed transitions originate from or reconcile to authoritative server/domain state. Client instrumentation is reserved for genuinely client-observable interaction/experience facts and may not manufacture authoritative business outcomes.
- **Rationale:** Analytics must describe governed business truth rather than create a second, less reliable business authority from browser observations.
- **Rules:**
  1. Server/domain state is the source or reconciliation anchor for governed business facts.
  2. Client-observable facts may originate client-side only when the fact is inherently a client observation.
  3. Analytics availability is not a precondition for an otherwise valid business transaction to commit unless Product Law explicitly says otherwise.
- **Failure behaviour:** Loss of optional client telemetry degrades analytics completeness only. Loss/failure of a required server-side analytical consequence enters durable recovery/reconciliation under ARC-180 rather than undoing committed business truth.
- **Security/privacy:** Analytics facts remain minimised and governed by the applicable consent, purpose, retention and deletion law; server authority does not license indiscriminate sensitive-data copying into analytics.
- **Performance/scaling:** Avoid synchronous external analytics dependencies on hot business commit paths. Derived analytics may scale independently while preserving authoritative provenance.
- **Enforcement/downstream:** Analytics event contracts and Domain Dossiers must classify each fact as authoritative-derived or genuinely client-observable. AR-007/008 govern deletion, retention, operational recovery and observability.

## ARC-180 — Required analytics consequences use committed derivation or an atomic durable commit bridge

- **Decision source:** AR-005 TC4.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-136`, `ARQ-AN-137`, `ARQ-PERF-038`, `ARQ-PERF-099`; cross-reference `ARC-146`, `ARC-155`
- **Decision:** A required server-side analytics event/projection consequence must either be deterministically reconstructable from committed authoritative state or have its durable processing intent established atomically with the originating authoritative transaction through the approved transactional job/outbox-equivalent boundary. Optional telemetry may remain best-effort where loss is explicitly acceptable.
- **Rationale:** Required analytics must not silently disappear in the commit-to-async gap, while analytics infrastructure must not become part of ordinary business transaction availability.
- **Rules:**
  1. No required analytical consequence relies solely on after-commit fire-and-forget execution.
  2. Prefer reconstructability when the authoritative source already contains enough evidence; do not duplicate durable event state merely ceremonially.
  3. When reconstructability is insufficient, establish durable intent atomically using the same consequence doctrine as TC1.
  4. Downstream projection failure does not retroactively invalidate a committed business transition.
- **Failure behaviour:** Failed required analytics processing remains discoverable/replayable and is reconciled later; optional telemetry may be dropped only according to its declared lower-criticality contract.
- **Security/privacy:** The durable bridge stores only the minimum approved identifiers/routing data needed for replay and processing.
- **Performance/scaling:** Business hot paths perform bounded transactional persistence only; projection/warehouse work remains asynchronous and backpressure-controlled.
- **Enforcement/downstream:** Event/Dossier design must state whether each required analytical consequence is reconstructable or atomically bridged. AR-008/009 prove backlog/recovery/load behaviour.

## ARC-181 — Governed analytics events have stable identity, versioned semantics and explicit time/provenance fields

- **Decision source:** AR-005 TC4.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-138`, `ARQ-AN-143`; cross-reference `ARQ-AN-141`, `ARC-098`
- **Decision:** Governed analytical event contracts include stable logical identity, event type, schema/semantic version, authoritative source identity/version where applicable, business/event time, observation/ingestion time when materially distinct, causation/correlation identity, an approved subject/randomization-unit identity where applicable, and only the minimum payload required for the analytical purpose.
- **Rationale:** Stable identity and explicit semantic/time provenance make retries, deduplication, late arrival and replay deterministic rather than timestamp-guess driven.
- **Rules:**
  1. Platform-generated event records may normally use the platform UUIDv7 identity doctrine.
  2. Replay-derived facts may use a deterministic source-derived logical identity where that better guarantees idempotent reconstruction.
  3. Event time and ingestion/observation time are distinct when that distinction matters.
  4. Breaking semantic changes create explicit event/schema versions; historical meaning is not silently rewritten.
- **Failure behaviour:** An event whose contract cannot be validated or whose source identity is insufficient for required deduplication may not silently enter a trusted derived dataset; exact quarantine mechanics remain AR-008/analytics implementation work.
- **Security/privacy:** Full Resource snapshots and unnecessary sensitive payloads are prohibited by default; identity representation must obey consent/privacy/deletion rules.
- **Performance/scaling:** Compact stable contracts reduce queue/storage/fan-out cost and permit efficient indexed deduplication/replay.
- **Enforcement/downstream:** AR-006 may define content-generated analytical event version relationships; AR-007 governs participant-level deletion/anonymisation; AR-008 governs contract-validation/quarantine operations.

## ARC-182 — Analytics projection, replay and backfill are idempotent and converge under late/reordered inputs

- **Decision source:** AR-005 TC4.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-133`, `ARQ-AN-134`, `ARQ-AN-143`, `ARQ-AN-144`, `ARQ-AN-145`, `ARQ-PERF-041`
- **Decision:** Important analytical projections are incremental where justified but retain a deterministic reconciliation/rebuild path. Consumers tolerate duplicate, late and reordered input, and replay/backfill is idempotent or deterministically replaces the intended derived state/range so recovery cannot multiply users, events, money, conversions or other metrics.
- **Rationale:** Derived analytical state must remain repairable rather than become an unrecoverable second source of truth.
- **Rules:**
  1. Do not assume exactly-once or globally ordered analytics delivery.
  2. Convergence uses stable identity, governed event/business time, authoritative versions and source-appropriate reconciliation.
  3. Dedicated streaming infrastructure such as Kafka is evidence-gated; semantics are locked before infrastructure.
  4. Rebuild/backfill preserves original governed evidence and does not fabricate missing authoritative source facts.
- **Failure behaviour:** Projection corruption or failed backfill results in an explicit recoverable analytics state; authoritative business operations remain unaffected.
- **Security/privacy:** Replay may use only source evidence still lawfully retained and must obey current deletion/anonymisation boundaries.
- **Performance/scaling:** Full rebuilds may be batch/bounded and isolated from OLTP; dedicated streaming is introduced only on measured volume/topology/freshness evidence.
- **Enforcement/downstream:** AR-008/009 define operational replay controls, load isolation, observability and proof; Domain/analytics dossiers define source-specific convergence rules.

## ARC-183 — Experiment governance remains platform-owned while assignment mechanics sit behind a replaceable deterministic adapter

- **Decision source:** AR-005 TC4.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-181`, `ARQ-AN-184`, `ARQ-AN-206`, `ARQ-AN-207`, `ARQ-AN-209`; Product Law propagation `DEC-293`
- **Decision:** The platform owns governed experiment identity/version, purpose/hypothesis, eligibility, variants, allocation, lifecycle, metrics, exposures, health, result evidence and decisions. Treatment allocation is provided through a platform-owned deterministic assignment interface/behaviour beneath that governance. FunWithFlags, Bandera or another library/custom primitive may be evaluated as replaceable implementation candidates but never become experiment authority.
- **Rationale:** Library replacement or cache/runtime failure must not redefine experiment semantics, history or analysis contracts.
- **Rules:**
  1. Product/application code calls the platform-owned assignment boundary rather than scattering third-party flag APIs.
  2. Assignment mechanics do not own hypotheses, exposure evidence, metrics, results or decision authority.
  3. Concrete assignment package selection remains proof-gated.
  4. AR-005 does not assign final concrete Domain ownership despite the frozen ARQ shorthand referring to an Experiment domain.
- **Failure behaviour:** Adapter/library failure follows ARC-188 safe degradation and cannot fabricate or rewrite experiment truth.
- **Security/privacy:** Assignment-unit identity and exposure evidence remain governed by consent/privacy/deletion law.
- **Performance/scaling:** The adapter must support efficient reconstructable multi-node assignment without requiring a remote service call for every evaluation unless later evidence justifies it.
- **Enforcement/downstream:** OQ-040/proof evaluates candidates; AR-006 integrates experiments into content/message delivery; AR-008/009 cover health/scale/observability.

## ARC-184 — A/B/n assignment is deterministic, sticky, mutually exclusive and version-bound

- **Decision source:** AR-005 TC4.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-187`, `ARQ-AN-188`, `ARQ-AN-189`, `ARQ-AN-208`, `ARQ-AN-211`
- **Decision:** Treatment assignment uses an immutable activated experiment version plus the approved stable randomization unit and a versioned deterministic bucketing contract to produce mutually exclusive weighted control/treatment allocation. Random-per-request/time percentage gates and independent overlapping Boolean flags are not sufficient A/B/n assignment semantics.
- **Rationale:** The same experimental unit must not flip treatment because of request repetition, process/node changes, cache loss or ordinary allocation maintenance.
- **Rules:**
  1. Every experiment declares its randomization unit.
  2. Assignment is reproducible for that unit and activated experiment version.
  3. Anonymous-to-known identity transitions follow the experiment's governed identity/reconciliation rule rather than silently rebucketing.
  4. Allocation changes preserve already exposed units wherever technically possible; changes that would invalidate that property require explicit new-version/reset/invalidation semantics.
  5. The exact hash/bucketing implementation is proof/JIT detail but its algorithm/version is part of experiment evidence when needed for reproducibility.
- **Failure behaviour:** If the known treatment can be reconstructed, preserve it; if not, use ARC-188 safe/default behaviour rather than random reassignment.
- **Security/privacy:** Stable units must minimise unnecessary identity disclosure and obey anonymous/known participant privacy boundaries.
- **Performance/scaling:** Deterministic local/reconstructable evaluation is preferred to per-request remote coordination; multi-node behaviour must produce the same result for the same governed inputs.
- **Enforcement/downstream:** AR-006 applies assignment to page/message delivery; AR-009 pressure-tests allocation stability at scale.

## ARC-185 — Assignment and exposure are separate governed facts; exposure records actual treatment experience

- **Decision source:** AR-005 TC4.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-185`, `ARQ-AN-190`, `ARQ-AN-198`, `ARQ-AN-203`; cross-reference `ARQ-AN-138`
- **Decision:** Assignment establishes the treatment selected for an eligible randomization unit; exposure is recorded separately when the treatment is actually experienced/delivered where practical. Exposure evidence uses stable experiment/version, variant, privacy-approved unit identity and exposure time, and is deduplicated/idempotent according to the experiment contract.
- **Rationale:** Analysing eligibility or theoretical assignment as if it were treatment exposure biases experiment evidence and makes retries/rerenders inflate samples.
- **Rules:**
  1. No fabricated exposure merely because assignment exists.
  2. Server-controlled treatment delivery should establish exposure reliably/idempotently at the point the treatment is actually delivered where practical.
  3. Genuinely client-observable exposure may require a deduplicated client signal.
  4. Re-render/reconnect/retry does not automatically create another logical exposure when the contract says it is the same experience.
- **Failure behaviour:** If safe assignment exists but exposure evidence cannot be established, do not invent exposure; surface analytics/experiment health for reconciliation as appropriate.
- **Security/privacy:** Exposure evidence is participant-level analytical data and remains subject to consent, retention, deletion/anonymisation and minimum-data rules.
- **Performance/scaling:** Exposure capture uses the analytics durable/replay doctrine where required and avoids synchronous remote analytical dependencies on rendering hot paths.
- **Enforcement/downstream:** AR-006 defines page/email/message delivery hook points; AR-007 governs identifiable exposure lifecycle; AR-008/009 cover operational quality and load.

## ARC-186 — Concurrent experiments require explicit interaction/isolation governance

- **Decision source:** AR-005 TC4.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-196`, `ARQ-AN-212`
- **Decision:** Every active experiment declares an interaction/isolation policy. Experiments that may materially contaminate one another on the same audience, surface, funnel or outcome use explicit mutual exclusion/layering or another justified isolation design; clearly orthogonal experiments may coexist, with relevant cross-exposure retained sufficiently for analysis.
- **Rationale:** Independent randomisation does not guarantee independent causal interpretation when treatments interact.
- **Rules:**
  1. Experiment activation validates its declared interaction/isolation policy.
  2. Mutual exclusion/layering semantics are governed experiment configuration, not ad-hoc UI logic.
  3. Orthogonality is a deliberate design assertion and may be revisited when evidence shows interaction.
- **Failure behaviour:** When required isolation cannot be safely established, affected treatment assignment degrades/blocks according to experiment policy rather than silently contaminating the experiment.
- **Security/privacy:** Cross-exposure evidence remains minimised and purpose-limited.
- **Performance/scaling:** Interaction checks must remain bounded; architecture must not require enumerating every active experiment on every hot-path request without an indexed/cached plan.
- **Enforcement/downstream:** Domain/Experiment dossier defines layering/isolation vocabulary; AR-006 integrates surface-level delivery; AR-009 proves hot-path cost.

## ARC-187 — Activated experiment configuration is immutable/versioned evidence rather than mutable in-place history

- **Decision source:** AR-005 TC4.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-184`, `ARQ-AN-185`, `ARQ-AN-189`, `ARQ-AN-191`, `ARQ-AN-192`, `ARQ-AN-211`; cross-reference `ARC-065`
- **Decision:** Activated experiment configuration that affects experimental validity is immutable/versioned evidence. Material changes to variants, eligibility, allocation, randomization unit, assignment algorithm/version, metric definitions or statistical design create explicit version/supersession/reset semantics rather than silently rewriting the configuration under historical exposures.
- **Rationale:** Historical exposure and result evidence must remain interpretable under the exact design that generated it.
- **Rules:**
  1. Exposure records identify the experiment/version under which they occurred.
  2. Draft configuration may evolve under its approved lifecycle; activation freezes the validity-relevant version.
  3. Material post-activation changes use explicit version/reset/invalidation decisions.
  4. Result/readout evidence remains linked to the applicable configuration/version.
- **Failure behaviour:** Configuration drift/mismatch is an experiment-health failure; do not silently continue with ambiguous treatment semantics.
- **Security/privacy:** Immutable experiment-methodology evidence never overrides participant-level deletion/anonymisation obligations for identifiable assignment/exposure data.
- **Performance/scaling:** Versioned immutable config is suitable for safe cache acceleration because old semantics remain addressable/reconstructable.
- **Enforcement/downstream:** AR-006 publication/content versioning must preserve variant-version relationships; AR-007 deletion boundary; AR-008 audit/operational controls.

## ARC-188 — Analytics and experiment failures degrade safely without blocking unrelated authoritative flows or fabricating evidence

- **Decision source:** AR-005 TC4.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-136`, `ARQ-AN-216`; cross-reference `ARQ-AN-213`, `ARC-084`, `ARC-180`, `ARC-184`, `ARC-185`
- **Decision:** Analytics/experiment availability is isolated from unrelated authoritative business correctness. If a treatment assignment can be safely reconstructed, preserve it; if safe assignment cannot be established, serve the governed safe/default experience, record no fabricated exposure, expose degraded experiment health and recover/reconcile later. Analytics projection failure preserves committed business truth and uses durable replay/recovery where required.
- **Rationale:** Experimentation and analytics are decision-support capabilities, not permission to block or corrupt payment, entitlement, authentication, consent or safety flows.
- **Rules:**
  1. Cache/node/adapter/library failure may not silently flip a known unit's treatment.
  2. Safe/default experience is preferred to random reassignment when treatment cannot be established.
  3. No exposure is recorded for a treatment that was not safely established/experienced.
  4. Required analytics recovery uses the durable bridge/replay law; optional telemetry may degrade according to its declared contract.
  5. Experiment/analytics degradation must not bypass product safety or authorization law.
- **Failure behaviour:** Degraded experiment/analytics health is observable and recoverable; unrelated authoritative workflows continue when their own dependencies are healthy.
- **Security/privacy:** Safe degradation must not expose hidden variants, participant identity or sensitive analytical payloads.
- **Performance/scaling:** Failure handling avoids synchronous retries/stampedes on hot paths and isolates analytical/assignment dependency incidents from OLTP capacity.
- **Enforcement/downstream:** AR-008/009 define health signals, alerting, failure tests and capacity envelopes; OQ-040/proof validates assignment candidate behaviour.

## 4I.9 AR-005 Final Closure Audit — PASS

- **Audit date:** 2026-08-17
- **Frozen ARQ surface audited:** **234** requirements whose primary downstream workstreams include `AR-005`.
- **Family counts:** Performance 106; Analytics 118; Payments 1; IAM 2; State 3; Async 3; Content 1.
- **Mechanical routing proof:** Re-parsed the frozen `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` `Primary downstream workstreams` metadata and independently reproduced the 234-count/family split above.
- **Result:** **PASS — AR-005 COMPLETE.** `ARC-146` through `ARC-188`, together with inherited AR-001...AR-004 Architecture Law, now cover the AR-005 transaction/consistency/async/realtime mechanism surface: atomic commit/durable consequences; Oban execution and business-idempotency separation; queue isolation/concurrency/backpressure/retry/dead-letter semantics; scheduling and worker topology; provider receipt/reconciliation; governed notification intent/delivery; time-effective transitions; after-commit realtime/PubSub projection semantics; durable/replayable analytics commit/recovery; and deterministic/versioned experiment assignment/exposure/failure behaviour.
- **Residuals correctly deferred rather than omitted:** provider-specific Paystack transition details remain OQ-004/vendor proof; exact analytics warehouse/streaming/statistical implementation remains evidence-gated; concrete Experiment/analytics Domain ownership and schemas remain Domain Law/Dossiers; page/email variant delivery and content-template ownership continue in AR-006; privacy/deletion/retention in AR-007; queue/worker/provider/observability/recovery operations in AR-008; capacity/performance/multi-node proof in AR-009; experiment candidate implementation proof remains OQ-040/Architectural Proof.
- **Contradiction check:** no Product Law, DEC, OQ or frozen ARQ contradiction was found. No upstream amendment is required.
- **Governance conclusion:** close `AR-005 — Transactions, Consistency, Async & Realtime`; advance Architecture Decision work to `AR-006 — Content, Translation, Media & External Integrations`.

## 4I.10 AR-005 Consolidated Consistency Doctrine

```text
AUTHORITATIVE ASH ACTION / DOMAIN TRANSITION
        |
        +--> PostgreSQL commit
        |       +-- business truth
        |       +-- mandatory durable consequence intent when required
        |       `-- required analytics intent when not reconstructable
        |
        +--> Oban / durable executor
        |       +-- reload + revalidate current authority
        |       +-- repeat-safe provider/notification/scheduled consequence
        |       +-- bounded queue/backpressure/retry semantics
        |       `-- unresolved obligation remains visible after execution exhaustion
        |
        +--> provider evidence
        |       `-- verify + durable receipt + reconcile; evidence != authority
        |
        +--> realtime observation
        |       `-- after-commit PubSub / LiveView projection; freshness != truth
        |
        +--> analytics
        |       `-- stable identity/version/time + idempotent replay/rebuild
        |
        `--> experimentation
                `-- governed immutable version -> deterministic sticky assignment
                    -> actual experienced exposure -> governed evidence/results

Required consequence != fire-and-forget
Job/provider/PubSub/analytics state != business authority
Assignment != exposure
Worker execution time != automatically business-effective time
Retry/replay/reconnect != permission to multiply durable effects
```

**AR-005 status:** COMPLETE through `ARC-188`; final 234-ARQ closure audit PASS.


# 4J. AR-006 — Content, Translation, Media & External Integrations

## 4J.1 AR-006 C1 — Content Authority, Versioning, Translation & Publication

> **Accepted answer set:** `C1.1 B, C1.2 B, C1.3 B, C1.4 B, C1.5 B, C1.6 B, C1.7 B, C1.8 B, C1.9 B, C1.10 B`.
>
> **Scope guardrail:** C1 locks the semantic content-governance boundary: conceptual identity, locale/version independence, Gettext versus governed runtime content, immutable published versions, delivery provenance, language approval/readiness, fallback, publication, risk classification and correction/withdrawal. It deliberately does not freeze final Ash Resource/table ownership, exact editorial UI, approval-role taxonomy, content-type catalogue, search engine, media provider, bucket layout, notification-template ownership or OQ-013 implementation-grade resource design.

## ARC-189 — Governed bilingual content uses one conceptual identity with independently versioned locale branches

- **Decision source:** AR-006 C1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-001`; cross-reference `ARC-043`, `ARC-065`
- **Decision:** A governed content concept has one stable conceptual identity, while each supported locale/language is represented through its own independently versioned, reviewed and publishable branch. Afrikaans and English versions belong to the same conceptual item but do not share one mutable body, one version number or one approval state.
- **Rationale:** Independent locale governance preserves translation provenance, review independence and historical delivery accuracy without turning translations into unrelated content objects.
- **Rules:**
  1. Conceptual identity and locale/version identity are distinct.
  2. Locale versions may advance asynchronously.
  3. Relationships across locales are explicit and stable.
  4. Complex governed bilingual content is not represented merely as paired `*_af`/`*_en` mutable fields on one current row where that would defeat independent version/review lifecycle.
- **Failure behaviour:** Missing or invalid locale linkage blocks only the governed operations that require that linkage; it may not silently substitute unrelated content.
- **Security/privacy:** Locale/version records inherit the conceptual item's access and sensitivity policy; translation relationships never bypass authorization.
- **Performance/scaling:** Stable conceptual/locale identifiers permit indexed lookup and cache-safe version addressing without duplicating business semantics.
- **Enforcement/downstream:** Domain Map/OQ-013/JIT dossier defines exact Resource/table structure; AR-006 C2 uses the locale/version identity for routing/search/SEO; AR-007 applies retention/deletion rules.

## ARC-190 — Gettext owns fixed interface/system strings; governed mutable runtime content lives in Ash-backed managed content

- **Decision source:** AR-006 C1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-002`; Product Law `DEC-119`
- **Decision:** Preserve the layered translation boundary: Gettext is the normal mechanism for relatively static application-owned interface/system strings, while business/editorial content requiring runtime governance, versioning, approval, audit or non-developer management is represented through Ash-backed governed runtime content. Complex governed content may not exist only in compiled Gettext catalogues.
- **Rationale:** Code-local UI translation and governed business content have different lifecycle, authority and audit requirements and should not be conflated.
- **Rules:**
  1. Fixed UI labels/messages belong in Gettext unless a governed runtime use case justifies otherwise.
  2. Content requiring editorial/legal/clinical/business lifecycle belongs in managed runtime content.
  3. Machine-generated/compiled translation files do not replace governed content-version evidence.
  4. Moving a string across this boundary requires preserving its governance semantics, not merely changing storage technology.
- **Failure behaviour:** Missing runtime content follows ARC-194 fallback law; missing Gettext strings follow ordinary application localization fallback without being mistaken for governed content approval.
- **Security/privacy:** Managed runtime content remains subject to access/publishing policy; Gettext catalogues may not become a backdoor for protected runtime content.
- **Performance/scaling:** Static strings remain deployment-efficient; managed content may use deliberate caching/read models under AR-003 without changing authority.
- **Enforcement/downstream:** OQ-013/Domain Law defines exact Ash-backed translation resources and indexes; implementation lint/review should reject large governed editorial blobs hidden in compiled locale files.

## ARC-191 — Published/activated governed content versions are immutable evidence; changes create new draft versions

- **Decision source:** AR-006 C1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-003`; cross-reference `ARQ-STATE-002`, `ARC-065`
- **Decision:** Once a governed locale/version becomes published/activated, its material content is immutable historical evidence. Corrections or improvements create a new version progressing through the required draft/review/approval/publication lifecycle rather than mutating the published version in place.
- **Rationale:** Historical deliveries, approvals and audit evidence must remain interpretable against the exact content that existed at the time.
- **Rules:**
  1. Published version bytes/semantics are not destructively edited.
  2. Draft versions may evolve according to workflow until approval/activation freezes them.
  3. Superseded or withdrawn versions remain historically addressable according to retention law.
  4. Audit logs supplement but do not replace preserved version evidence.
- **Failure behaviour:** An attempted in-place material mutation of published content fails closed and must proceed through a new version/supersession workflow.
- **Security/privacy:** Historical retention remains subject to lawful deletion/anonymisation requirements where applicable; immutability is not permission for indefinite retention.
- **Performance/scaling:** Immutable versions are cache-friendly and reduce invalidation ambiguity; current-published pointers/read models may optimize retrieval.
- **Enforcement/downstream:** Database/resource constraints/actions must prevent ordinary destructive edits; AR-007 governs retention/deletion tension; AR-008 provides audit/operational controls.

## ARC-192 — Material delivered outputs retain immutable provenance to the exact governed content/language versions used

- **Decision source:** AR-006 C1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-002`; cross-reference `ARQ-STATE-002`, `ARC-181`, `ARC-191`
- **Decision:** Personalised, paid, assessment, safety, legal/consent or otherwise governed delivered outputs retain immutable references to the exact content identity, locale and version(s) used to construct the delivery. Rendering may additionally preserve an approved snapshot when product semantics require it, but a mutable pointer to “current content” is insufficient provenance.
- **Rationale:** A historical output must remain explainable even after source content changes.
- **Rules:**
  1. Delivery provenance identifies exact source versions.
  2. Later source supersession does not silently rewrite prior delivery history.
  3. Re-rendering a historical delivery must declare whether it reproduces original-version content or intentionally creates a new delivery under current content.
  4. Composite outputs preserve provenance for all material governed components where required.
- **Failure behaviour:** If exact provenance cannot be established for a delivery class that requires it, the delivery must not be represented as fully governed/traceable.
- **Security/privacy:** Provenance references must not leak protected content or participant information beyond authorized contexts.
- **Performance/scaling:** Store stable references rather than duplicating full content unless snapshot semantics require duplication; indexes support reverse impact analysis.
- **Enforcement/downstream:** Domain Dossiers define which outputs require exact provenance/snapshots; AR-007 governs participant-related lifecycle; AR-008 audit/recovery; AR-009 performance proof.

## ARC-193 — Locale versions have independent approval evidence and derived bilingual delivery-readiness

- **Decision source:** AR-006 C1.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-001`, `ARQ-CONTENT-003`; cross-reference `ARC-189`
- **Decision:** Each governed locale/version carries its own review/approval evidence. Where a content class requires both approved languages, bilingual delivery readiness is a derived state from the required locale/version approvals plus any risk-specific approvals; approval of one locale or one authority does not imply approval of another.
- **Rationale:** Translation, clinical/legal/content and publication approvals answer different governance questions and must remain separately evidenced.
- **Rules:**
  1. A single ambiguous `approved=true` flag may not collapse distinct approvals.
  2. The same human may hold multiple roles, but each required approval remains a separately recorded decision.
  3. Required-language readiness is evaluated from current applicable approved versions.
  4. Optional low-risk single-language content follows explicit availability policy rather than pretending bilingual readiness.
- **Failure behaviour:** Missing required approval prevents the applicable publication/delivery transition but does not erase already-valid historical versions.
- **Security/privacy:** Approval authority uses AR-004 policy/role/relationship law and captures only necessary evidence.
- **Performance/scaling:** Derived readiness may be cached/read-modelled but is reconstructable from authoritative approval/version state.
- **Enforcement/downstream:** Domain Law defines approval authorities/risk taxonomy; AR-008 audit; editorial UI must expose distinct approval states clearly.

## ARC-194 — Missing-language fallback is governed by content class; critical governed content never silently uses unapproved fallback

- **Decision source:** AR-006 C1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-001`
- **Decision:** Locale fallback is content-class governed. Critical paid, health, safety, assessment, consent/legal/privacy, checkout/subscription, core-onboarding and personalised-plan content may not silently substitute an unapproved language version or machine translation. Explicitly permitted low-risk public/editorial content may use a declared fallback/availability rule with clear language handling.
- **Rationale:** Convenience fallback must not weaken language approval, informed-consent or safety guarantees.
- **Rules:**
  1. Machine translation may generate drafts but is never self-approving.
  2. Critical delivery checks requested-locale readiness before use.
  3. Low-risk fallback policy is explicit, not accidental framework behaviour.
  4. Fallback does not fabricate `hreflang`/translation availability or bilingual readiness.
- **Failure behaviour:** Critical missing/unapproved locale produces a governed unavailable/blocking outcome rather than silent substitution; low-risk content follows its approved fallback policy.
- **Security/privacy:** Fallback never crosses access/public/private boundaries.
- **Performance/scaling:** Fallback lookup is deterministic and bounded; no real-time machine translation on hot governed delivery paths.
- **Enforcement/downstream:** C2 integrates fallback with routing/SEO; OQ-013/Domain dossiers define locale availability fields and exact UX.

## ARC-195 — Publication activates a specific approved locale/version; latest, approved and published are distinct states

- **Decision source:** AR-006 C1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-003`; cross-reference `ARQ-ASYNC-002`, `ARC-172`, `ARC-191`
- **Decision:** Publication is an authoritative transition that activates a specific approved locale/version for its governed audience/use. “Latest version”, “approved version” and “currently published version” are distinct concepts. Draft/newer versions do not replace the published version until the required publication transition succeeds.
- **Rationale:** Publication must be explicit, reversible/superseding and schedule-safe rather than inferred from record recency.
- **Rules:**
  1. Current-published identity is explicit per relevant locale/audience/use.
  2. Scheduled publication revalidates approvals, translation readiness, access and safety state before activation when execution-gated.
  3. Publication does not mutate the immutable version body.
  4. Withdrawal can remove future eligibility without deleting historical evidence.
- **Failure behaviour:** Failed publication leaves the prior valid published state in force unless safety law requires withdrawal/no-content; failed jobs do not create half-published truth.
- **Security/privacy:** Publication policy enforces audience/access boundaries; private/paid content cannot become public by toggling a generic visibility flag outside policy.
- **Performance/scaling:** Explicit published pointers/read models provide cheap hot-path reads while preserving version history.
- **Enforcement/downstream:** AR-005 scheduling law executes transitions; C2 uses published identities for search/SEO; Domain Law defines exact publication owner/resource.

## ARC-196 — Governed content risk classification drives approval, publication, correction and withdrawal requirements

- **Decision source:** AR-006 C1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-003`; cross-reference `ARC-038`, `ARC-193`
- **Decision:** Governed content carries an explicit risk classification or equivalent governed policy input that determines required review/approval authority, language readiness, publication authority, correction severity and withdrawal urgency. Workflow is policy/data-driven rather than scattered page-specific conditionals.
- **Rationale:** Low-risk editorial copy and safety/legal/clinical content do not justify identical governance, yet both require deterministic rules.
- **Rules:**
  1. Risk classification is authoritative governed data, not inferred from URL/file location.
  2. Higher-risk classes may require stronger approvals and faster withdrawal capability.
  3. The exact risk vocabulary and responsible authorities belong to Domain Law.
  4. Risk changes that affect governance are themselves governed/audited transitions.
- **Failure behaviour:** Unknown/invalid risk classification fails closed for publication of content requiring governed classification; it may not default silently to low risk.
- **Security/privacy:** Risk classification does not expose underlying sensitive content unnecessarily.
- **Performance/scaling:** Policy evaluation must be bounded/indexable; high-risk governance is not implemented through expensive ad-hoc scans.
- **Enforcement/downstream:** Domain Map/Dossier locks risk classes/owners; AR-004 authorizes approvals; AR-008 audits; C2/Media rounds consume the classification.

## ARC-197 — Material corrections use explicit supersession/withdrawal semantics; historical immutability never implies continued future eligibility

- **Decision source:** AR-006 C1.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-003`; cross-reference `ARQ-STATE-002`, `ARC-065`, `ARC-191`
- **Decision:** Corrections are severity-governed. Ordinary corrections create new superseding versions; material/legal/consent corrections preserve provenance and evaluate dependent impact; safety-critical errors can immediately withdraw an affected version from future use while retaining historical evidence according to law. Historical immutability and future eligibility are separate dimensions.
- **Rationale:** Correctness requires both explainable history and the ability to stop unsafe/outdated content immediately.
- **Rules:**
  1. Destructive editing/deletion is not the normal correction mechanism.
  2. Withdrawal blocks future delivery/use according to scope without pretending the version never existed.
  3. Dependency/impact analysis is required where material downstream outputs may rely on the corrected/withdrawn version.
  4. Replacement approval need not delay an urgent safety withdrawal.
- **Failure behaviour:** If safe replacement is unavailable, affected future delivery may become unavailable/degraded rather than continue serving a withdrawn unsafe version.
- **Security/privacy:** Impact analysis follows minimum-access policy and does not expose unrelated participant data.
- **Performance/scaling:** Reverse dependency/version indexes/read models may support bounded impact discovery; large remediation fan-out uses AR-005 durable bounded async law.
- **Enforcement/downstream:** AR-007 handles retained/deleted dependent data, AR-008 incident/audit, Domain dossiers define severity/remediation contracts.

## ARC-198 — AR-006 locks content-governance semantics now; exact Ash Resource/schema ownership remains Domain Law/OQ-013/JIT work

- **Decision source:** AR-006 C1.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-001`, `ARQ-CONTENT-002`, `ARQ-CONTENT-003`; governance cross-reference `ARC-030`, `ARC-043`
- **Decision:** Architecture requires stable conceptual content identity, locale/version identity, approval evidence, risk classification, publication state, supersession/withdrawal semantics and delivery-version provenance, but does not prematurely freeze exact Ash Resources/tables/modules, ownership boundaries, indexes or editorial UI. Those are derived through Domain Map/OQ-013/JIT dossiers under these contracts.
- **Rationale:** Freezing semantics prevents drift while preserving the planned architecture→domain→delivery derivation sequence and avoiding schema design from feature names.
- **Rules:**
  1. Later Resource/schema designs must prove all C1 invariants.
  2. No implementation may collapse required semantic distinctions merely to reduce table count.
  3. Conversely, no design may introduce unnecessary Resource proliferation where simpler structure preserves law.
  4. Exact approval/resource/index relationships remain OQ-013/Domain/JIT evidence decisions.
- **Failure behaviour:** If a proposed implementation cannot express independent locale/version governance, immutable delivery provenance or withdrawal, it fails architecture review rather than weakening the law.
- **Security/privacy:** Final schema must preserve AR-004 policy and AR-007 privacy/deletion boundaries.
- **Performance/scaling:** Resource/schema selection must later prove representative read/write/index behaviour under AR-009 rather than optimize abstractly now.
- **Enforcement/downstream:** `04_DOMAIN_MAP.md`, lightweight Domain Architecture Profiles, Feature-Pack JIT Dossiers and OQ-013 are the next implementation-detail authorities.

**AR-006 status:** IN PROGRESS — C1 accepted through `ARC-198`.



## 4J.2 AR-006 C2 — Discovery, Search, Personalisation, SEO & Experiment-Safe Delivery

> **Accepted answer set:** `C2.1 B, C2.2 B, C2.3 B, C2.4 B, C2.5 B, C2.6 B, C2.7 B, C2.8 B, C2.9 B, C2.10 B, C2.11 B, C2.12 B`.
>
> **Scope guardrail:** C2 locks access-first discovery, evidence-gated search infrastructure, minimum-data search projections, explainable ranking, minimum-signal health personalisation, participant control/safety prominence, multilingual public routing/SEO, private-indexing separation and experiment-safe public delivery. It deliberately does not select a dedicated search product, vector engine, exact PostgreSQL indexes/extensions, final route shapes, CDN rules, personalisation flag schema or experiment content Resource design.

## ARC-199 — Search/discovery is a derived navigation capability over governed content authority, never publication or access authority

- **Decision source:** AR-006 C2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-004`, `ARQ-CONTENT-005`; cross-reference `ARC-061`, `ARC-195`
- **Decision:** Search, feed and discovery mechanisms operate over governed published/eligible content and current access policy. Search/index/ranking state is derived navigation state and may accelerate candidate discovery, but it cannot publish content, authorize access, resurrect withdrawn versions or override current locale/access/safety state.
- **Rationale:** Derived discovery infrastructure can be stale, rebuilt or replaced; protected content authority must remain with the governing application/domain state.
- **Rules:**
  1. Publication/withdrawal/access decisions are resolved from authoritative policy/state, not index presence.
  2. Candidate generation may use derived indexes, but final result eligibility remains policy-safe.
  3. Missing/stale index entries may affect discoverability, not authoritative existence or entitlement.
  4. Withdrawn/ineligible content must be removable from discovery promptly without erasing historical evidence.
- **Failure behaviour:** Search/index outage degrades discovery; it must not grant access, publish stale unsafe content or corrupt authoritative state.
- **Security/privacy:** Access/publication policy applies before protected content is returned; UI-side filtering is not the security boundary.
- **Performance/scaling:** Derived indexes/read projections may be introduced for latency/fan-out without changing authority.
- **Enforcement/downstream:** Domain Law defines content/search ownership; AR-008 governs operational recovery; AR-009 proves query/search performance.

## ARC-200 — Start with PostgreSQL-backed search/read projections where sufficient; dedicated search infrastructure is evidence-gated

- **Decision source:** AR-006 C2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-004`; cross-reference `ARC-074`, `ARC-199`
- **Decision:** The initial search implementation should use efficient PostgreSQL-backed authoritative/derived search projections where they satisfy relevance, latency and scale requirements. Maintain a clean application search boundary so a dedicated search engine can be introduced later when measured needs justify it; do not preselect Elasticsearch/OpenSearch/vector infrastructure merely because search exists.
- **Rationale:** PostgreSQL is already the default durable authority and can cover substantial search needs without adding an independent operational system prematurely.
- **Rules:**
  1. Exact full-text indexes, extensions and query shape remain JIT/evidence decisions.
  2. Search implementation stays behind platform/domain interfaces rather than leaking engine-specific calls across product code.
  3. Dedicated search infrastructure requires explicit evidence such as relevance, latency, scaling, language or operational requirements unmet by PostgreSQL.
  4. Plain unbounded wildcard scans are not a long-term substitute for designed search indexes.
- **Failure behaviour:** Search degradation must not compromise authoritative writes/access; fallback may provide reduced discovery where safe.
- **Security/privacy:** Any external search engine later introduced inherits data-minimization/access/deletion requirements.
- **Performance/scaling:** Progression is PostgreSQL-efficient search -> derived projections/indexes -> specialised engine only on evidence.
- **Enforcement/downstream:** AR-009/JIT proof determines indexes/engine thresholds; Domain Dossiers define query/relevance needs.

## ARC-201 — Search projections contain only minimum discovery data and explicit governed access/publication metadata

- **Decision source:** AR-006 C2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-004`, `ARQ-CONTENT-005`; cross-reference `ARC-042`, `ARC-199`
- **Decision:** Search/read projections contain only fields necessary for discovery/ranking and enough governed metadata to preserve publication/access boundaries. Detailed clinical records, private journals, payment payloads, practitioner notes and other unrelated sensitive data are not copied into a universal search index merely for convenience.
- **Rationale:** Search infrastructure is high-fan-out and often replicated; minimization reduces privacy exposure and deletion/recovery complexity.
- **Rules:**
  1. Prefer approved title/excerpt/locale/version/category/ranking/access metadata over full source payloads.
  2. Protected/paid content may have searchable internal representations only under explicit access-safe design.
  3. Index fields are classified and lifecycle-governed.
  4. Source withdrawal/deletion/permission expiry propagates to derived search representations under AR-007/008 rules.
- **Failure behaviour:** If access metadata is missing/ambiguous, protected result delivery fails closed rather than exposing content.
- **Security/privacy:** Minimum-data principle applies to both indexed fields and search logs/queries.
- **Performance/scaling:** Smaller projections improve index size, serialization and fan-out efficiency.
- **Enforcement/downstream:** Domain/JIT design defines exact projection fields; AR-007 deletion propagation; AR-008 security/operations.

## ARC-202 — Discovery ranking is governed, deterministic/explainable and access-first; semantic ranking is secondary/evidence-gated

- **Decision source:** AR-006 C2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-004`
- **Decision:** Search/feed ranking applies access/publication eligibility first and then uses governed explainable factors such as query relevance, locale/content fit, editorial/business signals and approved minimum personalisation signals. Semantic/vector/AI ranking may later augment ranking as a controlled secondary signal but may not become sole publication/access/safety authority.
- **Rationale:** Explainable ranking supports user trust, debugging, governance and safe degradation while preserving room for later relevance improvements.
- **Rules:**
  1. Ranking inputs and precedence are governed/versionable where material.
  2. Access filters precede ranking output.
  3. Safety-required content may receive explicit governed prominence independent of optional personalisation.
  4. AI/semantic relevance does not manufacture eligibility or override withdrawal.
- **Failure behaviour:** Ranking-engine failure degrades to a governed deterministic/default ordering where possible; it must not expose inaccessible content.
- **Security/privacy:** Ranking receives only approved signals appropriate to its purpose.
- **Performance/scaling:** Expensive semantic features are evidence-gated and must fit bounded query/fan-out budgets.
- **Enforcement/downstream:** Domain Dossiers define ranking rules; AR-009 tests search/recommendation performance and degradation.

## ARC-203 — Health-derived content personalisation crosses a minimum-signal relevance boundary, not detailed clinical records

- **Decision source:** AR-006 C2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-004`; cross-reference `ARC-039`, `ARC-042`
- **Decision:** Health/assessment capabilities expose only minimum approved derived relevance flags or equivalent scoped signals to content/discovery personalisation. Full diagnoses, raw assessments, laboratory values, private journals and detailed clinical records are not duplicated into the discovery/content layer merely to rank content.
- **Rationale:** Personalisation needs relevance signals, not broad clinical authority; minimization reduces privacy coupling and supports revocation.
- **Rules:**
  1. Derived signals carry enough source/purpose/version/expiry provenance to support invalidation.
  2. Source withdrawal, consent expiry or supersession removes dependent personalisation influence.
  3. Discovery cannot infer or persist richer clinical state from a minimal signal beyond its approved purpose.
  4. Exact signal vocabulary belongs to Domain Law/Dossiers.
- **Failure behaviour:** Missing/expired personalisation signals yield non-personalised/default discovery rather than blocking ordinary content access.
- **Security/privacy:** Signals are subject to purpose/consent/minimum-data policy and are not public/profile labels.
- **Performance/scaling:** Small stable signals support cheap ranking/cache keys while avoiding cross-domain joins on detailed health tables.
- **Enforcement/downstream:** AR-007 governs consent/deletion propagation; Domain Law owns source signals; AR-009 tests ranking cost.

## ARC-204 — Optional personalisation is understandable/controllable; safety-required content remains independently enforceable

- **Decision source:** AR-006 C2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-004`
- **Decision:** Where Product Law permits optional personalised ranking, participants can understand and control that personalisation. Safety-required or otherwise mandatory governed content remains independently eligible/prominent and cannot be permanently hidden merely because optional personalisation is disabled.
- **Rationale:** User agency over optional ranking must not weaken safety obligations.
- **Rules:**
  1. Optional ranking controls do not revoke underlying safety/legal duties.
  2. Recommendation rationale is explainable at the level appropriate to the user without exposing sensitive internals.
  3. Disabling personalisation produces a governed non-personalised experience rather than an empty/unsafe surface.
  4. Exact UX/control granularity remains product/domain design.
- **Failure behaviour:** Personalisation-service failure falls back to governed non-personalised ordering while preserving mandatory content.
- **Security/privacy:** Explanations must not reveal protected health inference beyond approved user-visible context.
- **Performance/scaling:** User controls are bounded state/policy inputs rather than per-request ad-hoc recomputation of entire histories.
- **Enforcement/downstream:** Domain/Product dossiers define user-facing controls and safety prominence; AR-009 tests high-fan-out recommendation paths.

## ARC-205 — Public translated content uses explicit locale-specific semantic routing and approved canonical/alternate metadata

- **Decision source:** AR-006 C2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-005`; cross-reference `ARC-189`, `ARC-195`
- **Decision:** Public translated content uses deliberate deterministic locale-specific public URLs tied to approved locale content, with per-locale canonical identity, appropriate alternate-language relationships only for real approved translations and governed permanent redirects after slug changes. Exact prefix/path convention remains routing design.
- **Rationale:** Explicit locale routing preserves SEO, shareability, canonical identity and content-version governance better than cookie-only or ad-hoc query-language selection.
- **Rules:**
  1. Locale slugs are approved governed metadata.
  2. Alternate-language metadata is emitted only when the corresponding approved public translation exists.
  3. Slug changes preserve canonical history through permanent redirects where applicable.
  4. Machine-generated transient slugs are not authoritative public identity.
- **Failure behaviour:** Missing translation produces the governed C1 fallback/availability behaviour; it does not emit a false alternate URL.
- **Security/privacy:** Public routing metadata may not leak private/paid content identities beyond deliberate public representations.
- **Performance/scaling:** Stable locale routes support CDN/browser caching and indexed route lookup.
- **Enforcement/downstream:** Phoenix routing/SEO implementation is JIT; AR-008 handles redirect/SEO operational migration; AR-009 performance.

## ARC-206 — Private/paid/protected content is excluded from ordinary public indexing; public teasers are separate deliberate representations

- **Decision source:** AR-006 C2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-005`; cross-reference `ARC-092`, `ARC-205`
- **Decision:** Private, paid, participant-specific or entitlement-protected content is not ordinarily exposed to public search-engine indexing. If marketing/discovery requires a public teaser or landing representation, that representation is a separately governed public surface rather than the protected content itself.
- **Rationale:** Index visibility and content authorization are distinct; exposing protected content to crawlers and hiding it only after click leaks information and weakens access boundaries.
- **Rules:**
  1. Obscure URLs are not an indexing/access control.
  2. Public teaser metadata/body contains only deliberately public information.
  3. Protected canonical content routes emit appropriate non-indexing behaviour where applicable.
  4. SEO systems may not receive protected body content merely for ranking.
- **Failure behaviour:** SEO/index configuration uncertainty defaults to non-public indexing for protected content.
- **Security/privacy:** Public crawlers receive no protected payload or entitlement information.
- **Performance/scaling:** Separate public teaser pages may use normal public caching without coupling to protected delivery.
- **Enforcement/downstream:** AR-008 defines crawler/header/sitemap operational controls; Domain Dossiers define which catalogue/teaser surfaces are public.

## ARC-207 — Normal experiment treatment uses one clean canonical public URL; assignment plumbing remains internal

- **Decision source:** AR-006 C2.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-213`, `ARQ-AN-214`, `ARQ-CONTENT-005`; cross-reference `ARC-184`, `ARC-205`
- **Decision:** Normal participant experiment treatment does not use public `experiment`, `variant`, `bucket` or equivalent parameters as treatment identity. One clean canonical URL represents the public content route; the platform derives current experiment/version and deterministic sticky assignment internally. Controlled authenticated preview/debug/test routes may exist under separate non-canonical rules.
- **Rationale:** Experiment mechanics should not fragment SEO identity, leak assignment semantics or make user-visible URLs unstable.
- **Rules:**
  1. Legitimate campaign attribution parameters remain separately governed and do not define assignment.
  2. Alternate testing URLs, if needed, preserve canonical preference and do not become normal participant assignment.
  3. Assignment identity stays behind the platform-owned experimentation boundary.
  4. Public URL history is content/locale governance, not experiment history.
- **Failure behaviour:** Experiment assignment failure uses ARC-210 safe/default delivery rather than changing the URL.
- **Security/privacy:** Internal treatment/assignment identifiers are not exposed as ordinary public routing requirements.
- **Performance/scaling:** Internal assignment/cache dimensions may optimise delivery without changing canonical URLs.
- **Enforcement/downstream:** AR-008 implements cache/edge/routing controls; AR-009 proves variant delivery under load.

## ARC-208 — Experiment-sensitive public HTML initially bypasses shared full-page caching; any later shared cache must be variant-safe internally

- **Decision source:** AR-006 C2.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-213`, `ARQ-AN-214`; cross-reference `ARC-103`, `ARC-104`, `ARC-207`
- **Decision:** The initial delivery architecture bypasses shared full-page caching for experiment-sensitive HTML. A future optimisation may use shared caching only after proving an internal variant/assignment cache-key dimension that cannot leak one unit's treatment to another, does not alter the canonical URL and preserves sticky treatment through cache purge/loss/deployment. Static/public assets remain normally cacheable.
- **Rationale:** Conservative cache admission is simpler and safer than prematurely engineering treatment-aware edge caching.
- **Rules:**
  1. Shared full-page cache admission is explicit for experiment-sensitive HTML.
  2. Cache loss/invalidation may not rebucket known units.
  3. Treatment cache identity remains internal and non-canonical.
  4. Static versioned assets may remain aggressively cacheable.
- **Failure behaviour:** Unsafe/unknown cache partitioning disables shared HTML caching rather than risking cross-user treatment leakage.
- **Security/privacy:** Cache keys must not expose sensitive actor data or cause protected/personalised response leakage.
- **Performance/scaling:** Revisit shared experiment-aware caching only on measured origin-load need.
- **Enforcement/downstream:** AR-008/009 prove Cloudflare/cache implementation, load and purge behaviour.

## ARC-209 — Experiment treatments reference governed immutable content/version identities or deterministic governed compositions

- **Decision source:** AR-006 C2.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-187`, `ARQ-AN-190`, `ARQ-AN-211`; cross-reference `ARC-187`, `ARC-191`, `ARC-192`
- **Decision:** An activated experiment treatment references specific governed content/version identity or another deterministic governed composition whose semantics are frozen for that experiment version. Materially changing treatment content after activation requires the applicable experiment-version/reset/supersession transition rather than silently redefining what the treatment meant.
- **Rationale:** Exposure and outcome analysis are invalid if a treatment label silently points to changing content over time.
- **Rules:**
  1. Exposure evidence remains interpretable against exact treatment/version semantics.
  2. Content supersession does not silently rewrite past experiment treatment history.
  3. Safety withdrawal may override continued treatment eligibility and trigger governed experiment degradation/version change.
  4. Exact treatment-content relation structure remains Domain/JIT design.
- **Failure behaviour:** Missing/withdrawn treatment content follows governed default/degraded behaviour and does not fabricate an exposure.
- **Security/privacy:** Treatment references do not bypass protected-content access policy.
- **Performance/scaling:** Stable version references are cache/replay friendly and support deterministic experiment analysis.
- **Enforcement/downstream:** Experiment/content Domain Dossiers define ownership/relations; AR-008 incident/safety handling; AR-009 experiment load/proof.

## ARC-210 — Experiment delivery failure preserves reconstructable treatment or serves governed default without fabricated exposure

- **Decision source:** AR-006 C2.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-216`; cross-reference `ARC-188`, `ARC-207`, `ARC-208`
- **Decision:** Delivery-layer failure of assignment/cache/adapter state preserves a known treatment when deterministic reconstruction is safe. If a safe treatment cannot be established, serve the governed default experience, do not record a fabricated exposure, surface degraded experiment health and continue unrelated authoritative payment/authentication/entitlement/safety flows normally.
- **Rationale:** Experiment infrastructure is subordinate to product correctness and must fail safely without silently switching participants or blocking unrelated critical capabilities.
- **Rules:**
  1. Process-local stale treatment is not authoritative if it cannot be verified/reconstructed safely.
  2. Default delivery under degraded assignment is explicitly observable and not counted as false treatment exposure.
  3. Experiment health degradation is operationally visible.
  4. Recovery/reconciliation preserves prior exposure/treatment evidence.
- **Failure behaviour:** Safe default rather than random treatment or broad platform outage.
- **Security/privacy:** Degraded fallback must preserve access/publication policy.
- **Performance/scaling:** Assignment failure isolation prevents experimentation infrastructure from becoming a shared critical-path availability dependency.
- **Enforcement/downstream:** AR-008 operational health/failure controls; AR-009 capacity/failure testing; Domain Dossiers define default experience.


## 4J.3 AR-006 C3 — Media, Live/Replay Delivery & Provider Boundaries

> **Accepted answer set:** `C3.1 B, C3.2 B, C3.3 B, C3.4 B, C3.5 B, C3.6 B, C3.7 B, C3.8 B, C3.9 B, C3.10 B, C3.11 B, C3.12 B`.
>
> **Scope guardrail:** C3 locks platform-owned governed media identity/lineage, recovery-class handling, entitlement-checked protected playback, live-session access authority, capture-versus-publication separation, replay/clip approval separation, governed accessibility derivatives, proof-gated external production/streaming providers, provider-evidence reconciliation, provider-failure semantics and a thin replaceable media-provider adapter. It does not select final provider plans, retention durations, bucket layout, recording pipeline, caption/transcript tooling, exact playback-token shape or a self-hosted RTMP/transcoding implementation.

## ARC-211 — Governed media uses a platform-owned business identity independent of provider/object identifiers

- **Decision source:** AR-006 C3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-STATE-001`; cross-reference `ARC-087`, `ARC-098`
- **Decision:** Every governed media asset has a stable platform-owned identity and platform-governed metadata for ownership/creator, rights/licence, accessibility, risk, publication, checksum/integrity, storage/provider references and replacement/supersession. Provider IDs, playback IDs and object keys are external/storage references rather than the media business identity.
- **Rationale:** Provider/storage identifiers are implementation details that may change during migration, transcoding, replacement or provider failover; business governance must remain stable.
- **Rules:**
  1. Provider/object identifiers may be replaced without changing the platform media identity unless business semantics require a new governed version/asset.
  2. Platform identity does not itself confer public access or entitlement.
  3. Provider metadata may augment but not replace platform rights/publication/access metadata.
  4. Exact Resource/table ownership remains Domain Law/JIT design.
- **Failure behaviour:** Missing/stale provider references degrade delivery/processing and enter reconciliation; they do not erase governed media history or fabricate availability.
- **Security/privacy:** Public knowledge of a media identifier is never sufficient access authority.
- **Performance/scaling:** Stable internal identity permits provider/storage migration and caching without rewriting business relationships.
- **Enforcement/downstream:** AR-007 governs retention/deletion; AR-008 provider/secret/operations proof; Domain Dossiers define media ownership.

## ARC-212 — Media masters, recordings and derived renditions retain explicit lineage and lifecycle relationships

- **Decision source:** AR-006 C3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-STATE-001`; cross-reference `ARC-097`, `ARC-193`
- **Decision:** Source/master media and derived representations such as streaming renditions, compressed downloads, thumbnails/posters, captions, transcripts and approved clips retain explicit lineage to the governed source/version and have lifecycle/rebuildability semantics appropriate to their role.
- **Rationale:** Treating transcodes and derivatives as unrelated files loses provenance, correction/withdrawal coverage and deletion/recovery accountability.
- **Rules:**
  1. Material edited replay versions may create new governed version relationships rather than silently replacing the source.
  2. Rebuildable derivatives may be regenerated from an approved source; governed/non-rebuildable derivatives retain appropriate durable status.
  3. Supersession/withdrawal/deletion evaluation includes affected derivatives.
  4. Provider-generated renditions do not silently become the governed source/master.
- **Failure behaviour:** Missing derivative may be rebuilt or marked unavailable; source/master authority remains explicit.
- **Security/privacy:** Derivatives inherit applicable sensitivity/access/retention obligations from source plus their own publication class.
- **Performance/scaling:** Lineage allows selective regeneration/caching rather than duplicating all representations as independent truth.
- **Enforcement/downstream:** AR-007 deletion/retention; AR-008 processing/recovery; Domain/JIT defines version/derivative schema.

## ARC-213 — Irreplaceable media uses recovery-class durability; routine derived renditions are not universally duplicated

- **Decision source:** AR-006 C3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-STATE-001`; cross-reference `ARC-095`, `ARC-099`, `ARC-106`
- **Decision:** Important or irreplaceable approved masters/recordings receive an appropriate durable source/recovery class, normally including a platform-controlled source/master or independent approved replica/export in a suitable failure domain. Rebuildable provider transcodes, thumbnails and ordinary derivatives do not automatically require identical independent duplication.
- **Rationale:** Sole reliance on a streaming/transcoding provider for irreplaceable originals creates avoidable loss risk, while universal duplication of every rendition creates needless cost/complexity.
- **Rules:**
  1. Durability/replica strength follows media value, replaceability, rights and retention obligations.
  2. A provider's playback rendition is not presumed to be the only archival copy of an irreplaceable asset.
  3. PostgreSQL is not the routine byte-backup store for large media.
  4. Exact provider/replica/retention topology remains AR-007/008/OQ-021 proof.
- **Failure behaviour:** Loss of a rebuildable rendition triggers regeneration/reconciliation; loss of a required source/replica is a material operational incident.
- **Security/privacy:** Recovery copies inherit access/encryption/deletion/retention obligations.
- **Performance/scaling:** Tiered durability avoids multiplying high-volume derived media unnecessarily.
- **Enforcement/downstream:** AR-007/008 define storage/retention/recovery classes and exercises.

## ARC-214 — Protected media playback is authorised from current platform entitlement/policy before issuing bounded delivery authority

- **Decision source:** AR-006 C3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-STATE-001`; cross-reference `ARC-092`, `ARC-105`, `ARC-108`
- **Decision:** Protected video/replay access performs a current platform entitlement/access-policy evaluation before issuing a short-lived/bounded provider/CDN playback or delivery capability. Provider playback tokens/URLs are consequences of platform authority, not permanent entitlements.
- **Rationale:** Permanent provider URLs or obscure IDs cannot enforce revocation, subscription expiry, participant-specific access or current policy.
- **Rules:**
  1. Protected media is not publicly deliverable merely because the provider can serve it.
  2. Capability lifetime/scope matches the residual-access risk envelope.
  3. New capabilities always consult current authority.
  4. Phoenix need not proxy every byte when a safe signed/provider delivery path exists.
- **Failure behaviour:** Unable-to-authorise or unable-to-issue capability fails closed for protected delivery while preserving entitlement/business state.
- **Security/privacy:** Delivery capabilities contain minimum authority, expire and are not logged/exposed unnecessarily.
- **Performance/scaling:** Direct provider/CDN delivery avoids application byte-proxy bottlenecks while preserving policy checks.
- **Enforcement/downstream:** AR-008 proves provider token/CDN rules; Domain Dossiers define entitlement semantics.

## ARC-215 — Live-session participation/access remains platform-authoritative; provider join/playback references are delivery details

- **Decision source:** AR-006 C3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-SYS-002`; cross-reference `ARC-214`
- **Decision:** The platform owns live-session occurrence metadata, registration/capacity state where applicable, entitlement and joining eligibility. External production/streaming attendee lists or join URLs do not become business access authority; eligible participants receive bounded provider joining/playback information after current policy evaluation.
- **Rationale:** Session cancellation, refund, expiry, waitlist movement or access revocation must remain enforceable independent of provider internals.
- **Rules:**
  1. Provider attendee state is evidence/operational delivery state, not authoritative registration/entitlement.
  2. Permanent universal join URLs are avoided for protected sessions where provider capability permits bounded access.
  3. Live occurrence and replay entitlement are separately governable.
  4. Exact capacity/waitlist business ownership remains Domain Law.
- **Failure behaviour:** Provider inability to join is recorded as delivery degradation/failure; entitlement is not silently removed.
- **Security/privacy:** Joining data is scoped/minimised and distributed only to currently eligible actors.
- **Performance/scaling:** Provider transport absorbs media fan-out while the app handles bounded auth/session metadata.
- **Enforcement/downstream:** Domain Map owns live/event semantics; AR-008 provider operations; AR-009 load/failure proof.

## ARC-216 — Captured recording is not replay publication; replay requires a governed approval/policy transition

- **Decision source:** AR-006 C3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-003`, `ARQ-CONTENT-006`; cross-reference `ARC-195`, `ARC-197`
- **Decision:** A provider-created/captured live recording initially becomes an unpublished/restricted governed recording candidate. Capture alone does not create an approved replay. Replay publication occurs only after applicable consent/privacy, editing, accessibility, risk/content, entitlement/expiry and publication requirements are satisfied.
- **Rationale:** Live capture can include participant data, accidental material, rights restrictions, safety errors or content requiring editing/review; automatic replay publication would bypass governance.
- **Rules:**
  1. Recording availability from a provider is external evidence, not publication authority.
  2. Replay policy may differ from live attendance/access policy.
  3. Safety/privacy/legal withdrawal can prevent or revoke future replay publication while historical evidence remains governed.
  4. Exact approval checklist depends on content/risk class.
- **Failure behaviour:** If approval cannot be established, recording remains restricted/unpublished rather than silently public/member-visible.
- **Security/privacy:** Consent/privacy review precedes replay exposure where applicable.
- **Performance/scaling:** Review is metadata/workflow state; large media stays in object/provider storage.
- **Enforcement/downstream:** AR-007 retention/consent; AR-008 operational review; Domain Dossiers define replay workflow.

## ARC-217 — Full recording, approved replay and public promotional clips have separable publication/rights authority

- **Decision source:** AR-006 C3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-003`, `ARQ-CONTENT-006`; cross-reference `ARC-192`, `ARC-196`, `ARC-216`
- **Decision:** Retention of a full recording, publication of an edited/protected replay and publication of promotional clips are distinct governed uses with separable rights/consent/risk/publication evidence. Approval for one use does not automatically approve another.
- **Rationale:** Audience, purpose and exposure differ materially between archival retention, member replay and public marketing reuse.
- **Rules:**
  1. Provider-generated clips are drafts/assets until separately governed.
  2. Public promotional reuse requires its own approved rights/purpose/publication state.
  3. Withdrawal/correction may target one representation/use without necessarily deleting every historical record immediately.
  4. Rights/licence constraints remain first-class metadata.
- **Failure behaviour:** Ambiguous rights/approval defaults to non-public use.
- **Security/privacy:** Public marketing is never inferred from private/member replay consent.
- **Performance/scaling:** Separate publication metadata allows shared bytes/derivatives without conflating access classes.
- **Enforcement/downstream:** AR-007 privacy/retention; Domain/JIT defines approval/use relationships.

## ARC-218 — Captions, transcripts and accessibility outputs are governed/versioned media derivatives, not unreviewed provider truth

- **Decision source:** AR-006 C3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-001`, `ARQ-CONTENT-003`, `ARQ-CONTENT-006`; cross-reference `ARC-191`, `ARC-212`
- **Decision:** Material captions, transcripts and accessibility artefacts retain media/version lineage and applicable locale/governance state. Automated transcription/translation may create drafts, but safety/health/meaning-sensitive outputs must satisfy applicable review/approval rules before being presented as governed authoritative content.
- **Rationale:** Automated captions/transcripts can materially alter meaning and must remain correctable/versioned alongside the media they represent.
- **Rules:**
  1. Locale-specific caption/transcript versions may evolve independently while staying linked to the media version.
  2. Machine output is draft unless the risk class explicitly permits direct publication.
  3. Corrected accessibility artefacts supersede prior published versions without erasing delivery history.
  4. Missing accessibility output is visible governance/quality state rather than fabricated completion.
- **Failure behaviour:** Failed generation/review degrades accessibility availability according to release/content gates; it never invents approved output.
- **Security/privacy:** Transcripts may increase discoverability/sensitivity and inherit the media's access class unless explicitly governed otherwise.
- **Performance/scaling:** Generation may be durable async and derived; delivery may use cached/versioned assets.
- **Enforcement/downstream:** AR-005 async law; AR-008 processor/provider operations; Domain Dossiers define accessibility requirements.

## ARC-219 — External production/streaming/transcoding is the first-release path; Restream/Cloudflare remain proof-gated replaceable candidates

- **Decision source:** AR-006 C3.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`; cross-reference `ARC-009`, `ARC-026`
- **Decision:** The first release uses external production/streaming/transcoding infrastructure rather than building a self-hosted RTMP/transcoding service. Restream-like production/multistreaming and Cloudflare-Stream-like delivery/recording remain preferred launch proof candidates where upstream Product Law points that direction, but OQ-020/OQ-021/vendor proof must validate plans, custom RTMPS, recording limits, failure behaviour, retention/export and required integration capabilities before implementation locks assumptions.
- **Rationale:** Video infrastructure is specialised, operationally expensive and already identified as an external-provider boundary; proof preserves portability without needless custom media infrastructure.
- **Rules:**
  1. Provider selection is not domain/business law.
  2. Do not build self-hosted RTMP/transcoding merely to avoid a vendor dependency in v1.
  3. Vendor capabilities used by Feature Packs require current proof before release.
  4. Provider-specific code stays behind the platform media/live boundary.
- **Failure behaviour:** If a preferred candidate fails proof, select another compliant provider rather than redefining media/session business semantics.
- **Security/privacy:** Provider contracts/data flows/access controls must satisfy privacy/security/rights requirements before production use.
- **Performance/scaling:** Provider scale/cost/latency/concurrency are evidence inputs; the platform avoids owning media transport scaling initially.
- **Enforcement/downstream:** OQ-020/OQ-021/vendor validation; AR-008 contracts/secrets/incident ops; AR-009 performance/cost proof.

## ARC-220 — Media-provider callbacks/status are verified external evidence reconciled through governed platform transitions

- **Decision source:** AR-006 C3.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-ASYNC-003`, `ARQ-PERF-028`; cross-reference `ARC-167`, `ARC-168`, `ARC-169`
- **Decision:** Media-provider callbacks/status such as stream readiness/start/stop, recording availability, transcode completion/failure or deletion/export completion are authenticated/verified as appropriate, durably received where required, repeat-safely processed and reconciled into platform state through governed application actions. Provider evidence cannot bypass publication, entitlement, consent or rights rules.
- **Rationale:** Provider callbacks can be duplicated, delayed, reordered or wrong for current platform context; reuse of the AR-005 provider boundary prevents a second inconsistent integration model.
- **Rules:**
  1. Duplicate/reordered callbacks may not create duplicate recordings/publications or regress valid platform state.
  2. Provider status does not automatically publish or grant entitlement.
  3. Ambiguous external outcomes enter reconciliation rather than blind repeat or last-message-wins behaviour.
  4. Exact callback schema/endpoints remain provider proof/JIT design.
- **Failure behaviour:** Verification/persistence failure does not falsely acknowledge successful reconciliation where provider retry semantics matter.
- **Security/privacy:** Reject unauthenticated/forged provider evidence; payloads are minimised/retained appropriately.
- **Performance/scaling:** Callback requests stay bounded; heavy work proceeds through durable async mechanisms.
- **Enforcement/downstream:** AR-008 ingress security/ops; Domain Dossiers define media state transitions.

## ARC-221 — Media/provider delivery failure is explicit degraded operational state and never rewrites entitlement or fabricates delivery success

- **Decision source:** AR-006 C3.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-PERF-006`, `ARQ-PERF-095`, `ARQ-PERF-145`, `ARQ-PERF-151`; cross-reference `ARC-165`, `ARC-170`
- **Decision:** Live/video provider failure separates authoritative session/entitlement state from transport/delivery state. Provider unavailability may mark delivery degraded/failed and trigger governed retry, alternate delivery, reschedule, later replay or business remedy where Product Law requires, but it does not silently revoke entitlement, fabricate attendance/recording/replay availability or report success.
- **Rationale:** Optional/external dependency outages must fail in their own boundary rather than corrupting unrelated business state.
- **Rules:**
  1. Provider health/delivery status is explicit and observable.
  2. Unrelated platform capabilities continue where safe.
  3. Recovery/remedy decisions are governed business/operations actions, not automatic provider-state inference.
  4. Exact alternate-provider/reschedule/refund policy remains Domain/Product/operations work.
- **Failure behaviour:** Clear degraded/failed state with bounded retries/reconciliation; never indefinite false `live`/`available` status.
- **Security/privacy:** Degraded modes preserve access policy and do not fall back to insecure public links.
- **Performance/scaling:** Dependency bulkheads/backpressure protect app/DB during provider outage.
- **Enforcement/downstream:** AR-008 incident/dependency controls; AR-009 failure injection; Domain Dossiers define remedies.

## ARC-222 — Media/live provider integration uses a thin platform-owned capability adapter, not provider SDK semantics throughout business code

- **Decision source:** AR-006 C3.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-CONTENT-006`, `ARQ-SYS-005`; cross-reference `ARC-048`, `ARC-058`, `ARC-219`
- **Decision:** Provider-specific media/live operations are isolated behind a thin platform-owned capability boundary covering the needed operations such as live input/session setup, playback capability, recording discovery, transcode state, provider asset identity, callbacks, export/delete and health/status. Core application/domain logic speaks in platform concepts (live session, recording, approved replay, protected media, publication, entitlement) rather than vendor SDK objects.
- **Rationale:** A provisional provider is expected but replaceable; direct provider calls scattered through Resources/LiveViews would make vendor mechanics de facto domain law.
- **Rules:**
  1. Adapter surface stays no broader than actual required provider capabilities.
  2. Avoid a speculative universal streaming abstraction supporting hypothetical providers/features.
  3. Business/policy decisions remain above the adapter.
  4. Provider-specific error/status translation is explicit at the boundary.
- **Failure behaviour:** Provider replacement/failure changes adapter implementation/operational state, not core business semantics.
- **Security/privacy:** Secrets/tokens remain in infrastructure/provider layer and do not leak into domain/UI state.
- **Performance/scaling:** Adapter supports provider-specific efficient APIs while protecting callers from implementation churn.
- **Enforcement/downstream:** AR-008 provider config/secrets/health; Domain/JIT owns exact interface and provider modules.



## 4J.4 AR-006 C4 — Messaging, Measurement & External Integration Boundary

> **Accepted answer set:** `C4.1 B, C4.2 B, C4.3 B, C4.4 B, C4.5 B, C4.6 B, C4.7 B, C4.8 B, C4.9 B, C4.10 B`.
>
> **Scope guardrail:** C4 closes the residual AR-006 boundary found by the preliminary 66-ARQ audit: governed message/template versioning, channel-provider adapters, email/message experimentation, delivery-versus-conversion evidence, privacy-safe scheduled/sensitive delivery, acquisition/attribution separation, consent-constrained measurement, deduplicated outbound conversion signals, vendor-report reconciliation and external-integration failure isolation. It does not select notification vendors, marketing/analytics vendors, exact campaign schemas, consent UI, provider SDKs, retry constants or final Domain ownership.

## ARC-223 — Material mutable message templates are governed versioned runtime content with exact locale/version delivery provenance

- **Decision source:** AR-006 C4.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-ASYNC-001`, `ARQ-CONTENT-002`, `ARQ-AN-200`; cross-reference `ARC-190`, `ARC-192`, `ARC-173`
- **Decision:** Material notification/email/message copy that is mutable, approved, experimented on or otherwise governed is represented as managed runtime content under the AR-006 content-version/locale doctrine. A durable notification intent references the semantic purpose plus the exact governed template/content locale and version used for delivery, rather than relying on a mutable provider template name or current-content pointer.
- **Rationale:** Historical communication must remain interpretable after copy changes, and provider-side templates must not become hidden content authority.
- **Rules:**
  1. Fixed low-risk application UI strings may remain Gettext-owned under ARC-190; governed message bodies/templates do not move there merely for convenience.
  2. Notification intent records the exact material template/version identity needed for provenance.
  3. Provider template identifiers are delivery references, not authoritative content identity.
  4. Message-template changes follow the applicable draft/review/approval/version lifecycle and experimentation law.
- **Failure behaviour:** If required governed template/version provenance is missing or no longer delivery-eligible, delivery fails closed or enters governed unresolved state; it does not silently fall back to unapproved copy.
- **Security/privacy:** Templates/payload assembly must avoid embedding unnecessary sensitive data; access to protected template/content remains governed.
- **Performance/scaling:** Resolve immutable/versioned template content efficiently through cache/read-model mechanisms without replacing authority.
- **Enforcement/downstream:** Domain Map/JIT defines exact template/content ownership and Resource shape; AR-007 governs message evidence/retention/deletion; AR-008 provider configuration/audit; AR-009 delivery scale testing.

## ARC-224 — Governed notification intent delivers through thin platform-owned channel adapters; providers do not own notification truth

- **Decision source:** AR-006 C4.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-ASYNC-001`, `ARQ-SYS-005`, `ARQ-PERF-006`, `ARQ-PERF-145`; cross-reference `ARC-172`, `ARC-173`, `ARC-174`
- **Decision:** Notification intent remains platform-governed and is delivered through thin channel-specific adapters (email and in-app at launch; SMS/WhatsApp only after provider/cost/consent proof; native push deferred until justified). Provider campaign/message objects and SDK semantics remain subordinate delivery mechanisms.
- **Rationale:** Communication providers differ in capability and failure modes, while message policy, consent, suppression and business causation belong to the platform.
- **Rules:**
  1. Business actions do not directly call provider SDKs for mandatory notifications.
  2. Channel eligibility, consent/purpose, suppression, quiet hours and required-vs-marketing semantics are decided above the provider adapter.
  3. Adapter surfaces remain narrow and channel-aware rather than pretending all channels are identical.
  4. Provider delivery identifiers/statuses map back to platform notification intent/evidence.
- **Failure behaviour:** Provider failure degrades the affected channel and follows durable retry/reconciliation law without changing the originating business truth.
- **Security/privacy:** Credentials stay in the provider/infrastructure layer; adapters minimise transmitted personal/sensitive data.
- **Performance/scaling:** Queue/provider concurrency is isolated and bounded under AR-005; channel outages cannot starve unrelated work.
- **Enforcement/downstream:** AR-008 selects/configures providers and secrets; Domain/JIT defines adapter interfaces; provider activation gates must prove cost, consent and reliability semantics.

## ARC-225 — Email/message A/B/n experiments reuse governed experiment authority and sticky assignment; treatment references immutable governed message versions

- **Decision source:** AR-006 C4.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-181`, `ARQ-AN-200`, `ARQ-AN-205`; cross-reference `ARC-183`, `ARC-184`, `ARC-185`, `ARC-187`, `ARC-210`, `ARC-223`
- **Decision:** Eligible email/message experiments use the platform-owned Experiment capability and deterministic sticky assignment contract already locked in AR-005. Each experiment treatment references immutable governed message/template content and may vary approved dimensions such as subject, body/content, CTA/layout, sender presentation or send timing only within the applicable consent, suppression, quiet-hour, safety/legal and delivery rules.
- **Rationale:** Provider-side random splitting or retry-time randomization would fragment experiment authority and can switch a recipient's treatment across attempts.
- **Rules:**
  1. Assignment is stable for the declared campaign experiment/randomization unit.
  2. Retries preserve the assigned treatment unless an explicit governed experiment reset/version transition says otherwise.
  3. Treatment content/version is immutable for the activated experiment version.
  4. Experimentation never weakens mandatory security, legal, payment, entitlement, safety or consent controls.
- **Failure behaviour:** If assignment cannot be safely reconstructed, use the governed default/no-exposure behaviour from ARC-188 rather than randomizing or fabricating treatment.
- **Security/privacy:** Experiment payloads and assignment evidence follow privacy/minimisation law; message experimentation is not a bypass around marketing consent.
- **Performance/scaling:** Assignment remains deterministic/reconstructable and provider delivery remains queued/bounded; no provider-specific randomization dependency is required.
- **Enforcement/downstream:** Domain/JIT defines campaign/experiment/template relationships; AR-008 proves provider observability and experiment health; AR-009 tests bulk/variant delivery scale.

## ARC-226 — Messaging experiment evidence separates assignment, delivery lifecycle, engagement observations and authoritative downstream conversion

- **Decision source:** AR-006 C4.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-008`, `ARQ-AN-061`, `ARQ-AN-201`; cross-reference `ARC-176`, `ARC-185`
- **Decision:** Messaging analytics keeps distinct evidence for assignment, notification intent, send attempt, provider acceptance, delivery/bounce, observable engagement signals such as open/click/reply where available, and authoritative downstream business outcomes such as verified purchase. Provider/channel engagement metrics are observational evidence and never substitute for the owning domain's conversion truth.
- **Rationale:** Delivery and engagement signals have different reliability and semantics from a completed business conversion; collapsing them produces misleading experiment results.
- **Rules:**
  1. A send/open/click does not equal a purchase or entitlement.
  2. Downstream conversion joins to authoritative business identity/event evidence.
  3. Dashboards disclose material limitations where privacy/client/platform behavior makes engagement signals unreliable or unavailable.
  4. Provider-reported conversion remains external attribution evidence under ARC-231.
- **Failure behaviour:** Missing engagement telemetry lowers measurement completeness/confidence; it does not fabricate engagement or conversion.
- **Security/privacy:** Engagement measurement is purpose/consent constrained and minimised; no hidden sensitive profiling is introduced for experiment convenience.
- **Performance/scaling:** Event identities permit deduplicated async ingestion and replay without coupling message send latency to analytics processing.
- **Enforcement/downstream:** AR-008 observability/data-quality evidence; Domain/analytics dossiers define metric joins and caveats.

## ARC-227 — Sensitive alerts and scheduled report delivery are minimum-data and execution-time permission/purpose scoped

- **Decision source:** AR-006 C4.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-117`, `ARQ-AN-124`, `ARQ-ASYNC-001`; cross-reference `ARC-123`, `ARC-151`, `ARC-174`
- **Decision:** Sensitive alerts and scheduled reports prefer minimum-data notifications plus authorised deep links/workflows where practical. At execution, scheduled disclosure revalidates the current recipient, permission, purpose, scope/filter and data eligibility; schedule creation is not permanent future disclosure authority.
- **Rationale:** Long-lived schedules and external message channels can outlast grants, relationships or scope, making creation-time authorization insufficient.
- **Rules:**
  1. Prefer stable identifiers/deep links over embedding sensitive health, journal, payment or participant payloads unless the delivery use case explicitly requires and governs them.
  2. Current authorization/purpose is checked at execution.
  3. Broken/stale filters fail narrow/closed; they may not broaden disclosure.
  4. Revocation/consent withdrawal affects future scheduled disclosure according to current authority.
- **Failure behaviour:** If permission/purpose/filter validity cannot be established, suppress/fail the delivery and expose recoverable operational state rather than sending broadly.
- **Security/privacy:** Minimum disclosure, current authorization and channel-appropriate controls are mandatory.
- **Performance/scaling:** Revalidation is bounded and query-efficient; large scheduled reports use durable async generation/delivery rather than synchronous request work.
- **Enforcement/downstream:** AR-007 governs retained generated reports/copies; AR-008 auditing/security; Domain Dossiers define permitted attachment/deep-link patterns.

## ARC-228 — Acquisition touchpoint evidence and stable campaign identity are preserved separately from attribution interpretation

- **Decision source:** AR-006 C4.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-013`, `ARQ-AN-047`, `ARQ-AN-049`, `ARQ-AN-051`, `ARQ-AN-068`; cross-reference `ARC-179`, `ARC-181`
- **Decision:** The platform preserves governed acquisition/touchpoint evidence and stable internal campaign identity independently from mutable human-readable campaign names and attribution models. Attribution is a downstream analytical interpretation allocating credit over preserved evidence; it never rewrites historical transactions or raw acquisition chronology.
- **Rationale:** First-touch, session-touch, conversion-touch and model-specific attribution answer different questions and must not collapse into one mutable `source` field.
- **Rules:**
  1. Campaign taxonomy/naming is governed metadata over stable identity.
  2. Chronological acquisition/touchpoint evidence is retained according to its approved purpose/lifecycle.
  3. Attribution models are versioned/identifiable analytical interpretations.
  4. Changing attribution logic may recompute credit but not authoritative commercial facts.
- **Failure behaviour:** Missing/ambiguous evidence is represented as unknown/incomplete rather than guessed into a preferred source.
- **Security/privacy:** Acquisition evidence is purpose/minimisation/deletion constrained and does not justify covert identity collection.
- **Performance/scaling:** Analytical projections may rebuild attribution from retained approved evidence; OLTP does not depend on attribution computation.
- **Enforcement/downstream:** AR-007 handles privacy/deletion; AR-008 vendor/integration governance; Domain Map defines campaign/acquisition ownership.

## ARC-229 — Measurement and marketing integrations use approved identity/consent mechanisms; no covert fingerprinting or blanket cross-domain tracking authority

- **Decision source:** AR-006 C4.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-056`, `ARQ-AN-058`, `ARQ-AN-059`, `ARQ-AN-060`, `ARQ-AN-066`; cross-reference `ARC-118`, `ARC-126`, `ARC-128`
- **Decision:** Measurement, attribution and marketing integrations use only approved identity continuity and current purpose/consent authority. Covert/probabilistic fingerprinting is not introduced to maximize attribution completeness; owned-domain continuity or identity stitching must remain governed, purpose-specific and revocable where applicable.
- **Rationale:** Measurement completeness is subordinate to privacy, consent and minimisation obligations.
- **Rules:**
  1. No one universal perpetual analytics/marketing consent flag.
  2. Marketing withdrawal stops affected future marketing measurement/processing and invalidates dependent active integration state.
  3. Historically lawful evidence remains only under its approved retention/legal basis; withdrawal does not fabricate historical deletion beyond applicable law.
  4. Sensitive health/safety/journal profiling is excluded from advertising measurement by default.
- **Failure behaviour:** If required consent/purpose identity cannot be established, omit/suppress the affected measurement/integration rather than infer hidden authority.
- **Security/privacy:** Purpose limitation, minimisation and deletion propagation are first-class; vendor payloads must not become a shadow participant profile.
- **Performance/scaling:** Consent/identity checks use current authoritative state with bounded caching only where revocation-safe.
- **Enforcement/downstream:** AR-007 defines processor deletion/retention propagation; AR-008 vendor inventory/configuration; Domain/JIT defines exact approved signals.

## ARC-230 — Outbound conversion measurement derives from authoritative business outcomes and uses stable deduplication identity across delivery paths

- **Decision source:** AR-006 C4.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-006`, `ARQ-AN-008`, `ARQ-AN-061`, `ARQ-AN-062`, `ARQ-AN-141`; cross-reference `ARC-179`, `ARC-181`, `ARC-182`
- **Decision:** Browser, server-side and vendor conversion signals are downstream representations of one authoritative business conversion and carry a stable event/conversion identity sufficient for deterministic deduplication/reconciliation across approved delivery paths. Provider or thank-you-page observations never independently manufacture another conversion.
- **Rationale:** Multiple transport paths improve measurement robustness but otherwise create duplicate revenue/conversion counts.
- **Rules:**
  1. Authoritative conversion originates in the owning business transition.
  2. Event/schema version is explicit and evolvable without semantic ambiguity.
  3. Multiple approved delivery paths share/reconcile stable conversion identity.
  4. Advertising payloads exclude detailed clinical/health/safety/journal data by default.
- **Failure behaviour:** Failed optional delivery affects measurement completeness and may be replayed/backfilled where allowed; it does not roll back the authoritative conversion.
- **Security/privacy:** Payload fields are purpose-approved/minimised and processor-specific; no sensitive business record dump is sent externally.
- **Performance/scaling:** Use durable/bounded async delivery for server-side integrations; browser delivery remains supplementary and deduplicable.
- **Enforcement/downstream:** AR-008 provider schemas/observability; AR-007 consent/deletion; analytics dossiers define dedup/reconciliation contracts.

## ARC-231 — Vendor analytics/payment/communication reports are labelled external evidence and reconciled, never internal financial or entitlement authority

- **Decision source:** AR-006 C4.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-067`, `ARQ-AN-069`, `ARQ-AN-080`, `ARQ-AN-081`, `ARQ-AN-082`, `ARQ-AN-084`, `ARQ-AN-094`, `ARQ-AN-096`, `ARQ-AN-098`, `ARQ-PAY-001`; cross-reference `ARC-168`, `ARC-170`, `ARC-176`
- **Decision:** External provider dashboards/reports/status taxonomies are preserved as labelled external evidence/interpretation and reconciled against platform authority. They may legitimately differ from platform totals because attribution, fees, refunds, disputes, recurring-payment state, currency conversion and provider reporting semantics answer different questions; they do not overwrite platform financial, subscription, entitlement or business truth.
- **Rationale:** Treating provider dashboards as canonical creates irreconcilable authority conflicts and can corrupt financial/product state.
- **Rules:**
  1. Gross commercial value, fees, refunds, disputes and subscription/payment status retain their distinct governed semantics.
  2. Original currency and approved conversion semantics remain explicit where multi-currency applies.
  3. Provider schema/status meaning is translated/versioned at the integration boundary when materially changed.
  4. Material discrepancies trigger reconciliation/operational review rather than silent overwrite.
- **Failure behaviour:** Unknown/disputed provider evidence remains explicit pending reconciliation; no last-report-wins state regression.
- **Security/privacy:** Provider reports are accessed/minimised according to role/purpose and not repurposed as participant profiling datasets.
- **Performance/scaling:** Reconciliation may be asynchronous/batched and must not block ordinary read flows.
- **Enforcement/downstream:** AR-007 retention; AR-008 provider reconciliation/incident operations; payment/commercial Domain Dossiers own exact status transitions.

## ARC-232 — Optional/required external integrations reuse the durable-consequence, bounded-retry and bulkhead model; provider failure cannot corrupt originating business truth

- **Decision source:** AR-006 C4.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-006`, `ARQ-PERF-016`, `ARQ-PERF-037`, `ARQ-PERF-038`, `ARQ-PERF-094`, `ARQ-PERF-095`, `ARQ-PERF-145`, `ARQ-PERF-149`, `ARQ-PERF-150`, `ARQ-PERF-151`, `ARQ-PERF-162`, `ARQ-ASYNC-003`; cross-reference `ARC-146`, `ARC-147`, `ARC-165`, `ARC-168`, `ARC-170`, `ARC-221`
- **Decision:** External analytics, communication and integration consequences reuse AR-005's short-authoritative-transaction, durable-intent, provider-adapter, retry/reconciliation and failure-isolation doctrine. Required consequences are durably captured; optional measurement may degrade and recover/backfill where permitted. Provider unavailability may affect delivery/freshness/completeness, but it cannot retroactively fail or rewrite a successful payment, entitlement, consent, content publication or safety decision.
- **Rationale:** A single integration reliability model reduces split-brain semantics and prevents optional providers from becoming hidden availability dependencies for core business flows.
- **Rules:**
  1. Do not hold authoritative transactions open across slow provider calls.
  2. Retry ownership/budgets are deliberate and provider-aware; no stacked unbounded retry loops.
  3. Provider/internal latency and failures are separately observable.
  4. Bulkheads/degraded modes prevent dependency outages from exhausting PostgreSQL/worker capacity.
  5. Failure-injection/pressure testing proves the affected integration can degrade without corrupting authority.
- **Failure behaviour:** Explicit degraded/unresolved state with bounded retry/reconciliation/alerting as appropriate; never silent loss for mandatory consequences or fabricated success for optional ones.
- **Security/privacy:** Provider boundaries verify ingress, protect secrets and minimise payloads; degraded mode never falls back to insecure/unapproved disclosure.
- **Performance/scaling:** Provider queues/concurrency/deadlines are isolated and evidence-sized; optional integrations can be paused/shed before OLTP is threatened.
- **Enforcement/downstream:** AR-008 owns concrete provider health/observability/secret/configuration/incident controls; AR-009 owns load/failure proof; Domain Dossiers define business-specific remediation.

## 4J.5 AR-006 Closure Audit — PASS

**Audit scope:** every frozen ARQ whose **Primary downstream workstreams** includes `AR-006`.

**Mechanical routed count:** **66 ARQs**.

```text
Performance     16
Analytics       33
Payments         1
System           5
State             1
Async             3
Content           6
Security          1
-------------------
TOTAL            66
```

**Closure result: PASS.** The accepted AR-006 law now covers the complete routed requirement surface without reopening Product Law:

1. **Content, translation, publication and historical delivery provenance** — `ARC-189...ARC-198` cover conceptual/locale identity, Gettext versus managed runtime content, immutable versions, exact delivery provenance, approval/readiness, fallback, publication, risk classification and correction/withdrawal.
2. **Discovery, search, personalisation, SEO and experiment-safe public delivery** — `ARC-199...ARC-210` cover access-first derived search, PostgreSQL-first/evidence-gated search infrastructure, minimum-data projections, explainable ranking, minimum health-derived relevance signals, participant controls, locale-specific canonical routing, private/paid indexing, clean experiment URLs, variant-safe caching, governed experiment content/version references and safe delivery degradation.
3. **Media, live/replay and streaming/transcoding provider boundaries** — `ARC-211...ARC-222` cover platform-owned media identity/lineage, recovery-class durability, protected playback, live-session access, recording-versus-publication separation, replay/promotional approval, accessibility derivatives, proof-gated external provider direction, provider-evidence reconciliation, explicit delivery degradation and replaceable media adapters.
4. **Messaging, measurement and outbound external integrations** — `ARC-223...ARC-232` cover governed message-template versions, channel adapters, email/message A/B/n treatment semantics, delivery-versus-conversion evidence, sensitive scheduled/alert disclosure, acquisition/attribution separation, consent-constrained measurement, deduplicated authoritative conversion export, vendor-report reconciliation and provider failure isolation.
5. **Cross-workstream requirements routed through AR-006** — the 16 Performance ARQs reuse AR-005 bounded transactions/durable consequence/backpressure/provider-failure law plus `ARC-232`; the Payments ARQ remains governed by Paystack evidence/reconciliation rather than provider authority (`ARC-168`, `ARC-231`); the five System ARQs remain compatible with one platform/controlled product-space, SA-first international-safe and mature-platform/MVP restraint law from AR-001/AR-002 while AR-006 keeps providers/content portable; `ARQ-STATE-001` is satisfied by AR-003 storage/access classifications plus protected media/message delivery rules; the three Async ARQs are covered by AR-005 scheduling/provider/notification law and AR-006 delivery semantics; `ARQ-SEC-002` remains enforced by AR-003 quarantine/inspection before publication and AR-006 media/content publication authority.

**Deferrals remain valid and do not block AR-006 closure:** exact Ash content/template Resources and schemas; final Domain ownership; search indexes/extensions; notification/analytics/ad/media provider selection and plan capabilities; object-storage layout; exact locale route syntax; consent UI; provider SDK modules; retry/timeout constants; recording-retention durations; Cloudflare/Restream proof; and implementation-grade OQ-013/OQ-020/OQ-021 details remain assigned to Domain Law, AR-007/008/009, expert/vendor gates, Feature Pack dossiers or Architectural Proof as already governed.

**No Product Law, DEC, OQ, ARQ or prior ARC amendment was required. No unresolved contradiction remains inside AR-006.**

**AR-006 status:** COMPLETE through `ARC-232`; final 66-ARQ closure audit PASS.

# 4K. AR-007 — Privacy, Deletion, Backup & Restore

## 4K.1 Round P1 — Privacy Lifecycle, Retention & Irreversible Deletion

**Accepted answer set:** `P1.1 B, P1.2 B, P1.3 B, P1.4 B, P1.5 B, P1.6 B, P1.7 B, P1.8 B, P1.9 B, P1.10 B`

## ARC-233 — Business lifecycle and data lifecycle are separate governed dimensions

- **Decision source:** AR-007 P1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-IAM-006`; cross-reference `ARC-060`, `ARC-063`, `ARC-125`, `ARC-128`
- **Decision:** Business state and data-lifecycle state are modelled as separate governed concerns. A business record may remain completed, cancelled, refunded or otherwise historically valid while its data lifecycle independently becomes archived, access-restricted, deletion-requested/pending, anonymised, retained-by-obligation, legal-hold or deleted according to category-specific law. AR-007 does not force one identical state machine/table onto all domains.
- **Rationale:** Conflating business meaning with retention/deletion state creates false semantics such as treating account closure as deletion or destroying historically valid financial/professional state merely because participant access ends.
- **Rules:**
  1. Lifecycle transitions record applicable reason, authority, timestamp and policy/version provenance.
  2. Account closure, archival, deletion request, anonymisation, restricted retention, hold and completed deletion remain distinct states/operations.
  3. Domain-specific lifecycle vocabulary may vary, but the cross-cutting meanings remain interoperable.
  4. Re-registration or identity recovery may not silently resurrect a fully deleted identity relationship.
- **Failure behaviour:** Ambiguous lifecycle state fails closed for destructive or disclosure-sensitive operations and is surfaced for governed reconciliation.
- **Security/privacy:** Lifecycle state is an authorization/privacy input and may further restrict otherwise-valid business access.
- **Performance/scaling:** Lifecycle checks must remain indexable/queryable without requiring reconstruction from audit logs for ordinary enforcement.
- **Enforcement/downstream:** Domain Map/Dossiers define domain-owned lifecycle states; AR-008 audits/operates lifecycle transitions; AR-009 proves lifecycle enforcement under load/recovery.

## ARC-234 — Retention is category-, purpose- and authority-specific; Architecture does not invent statutory/professional durations

- **Decision source:** AR-007 P1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-005`, `ARQ-IAM-006`, `ARQ-IAM-007`
- **Decision:** Retention is governed by explicit policy inputs such as data category, purpose, legal/professional/business obligation, jurisdiction where applicable, record state, lawful basis/consent context and legal-hold state. Exact statutory/professional retention durations remain expert-owned inputs rather than Architecture constants.
- **Rationale:** One global retention period is legally and semantically wrong for mixed participant, health, payment, professional, security and audit records.
- **Rules:**
  1. Retention policies are versioned/governed inputs rather than scattered hard-coded literals.
  2. The narrowest applicable lawful retention purpose wins over convenience reuse.
  3. Policy changes do not silently rewrite historical evidence; they govern current/future lifecycle decisions according to applicable law.
  4. Unknown required duration is an explicit expert gate, not a guessed default.
- **Failure behaviour:** If a required retention rule is unresolved, the affected destructive operation stops at the governed gate rather than guessing deletion or indefinite retention.
- **Security/privacy:** Retained data remains purpose-limited and access-restricted; retention does not create marketing/personalisation authority.
- **Performance/scaling:** Retention eligibility may be computed/batched by indexed policy/state fields rather than full-record scans where practical.
- **Enforcement/downstream:** Expert/legal/professional gates supply durations; Domain Dossiers map categories; AR-008 operates retention jobs/alerts; AR-009 tests bulk lifecycle processing.

## ARC-235 — Full deletion is a durable, idempotent, cross-system orchestration rather than a synchronous row cascade

- **Decision source:** AR-007 P1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-PERF-087`, `ARQ-PERF-097`, `ARQ-PERF-099`, `ARQ-PERF-103`, `ARQ-ASYNC-003`; cross-reference `ARC-146`, `ARC-149`, `ARC-151`, `ARC-165`
- **Decision:** Approved full deletion transitions into a durable deletion workflow that discovers the applicable scope, executes category-specific deletion/anonymisation/processor actions idempotently, reconciles partial failures and reaches completion only after governed verification. It must survive request termination, process/node loss, retry and deployment.
- **Rationale:** Full deletion spans authoritative records, derived state, files, indexes, caches, workers and external processors; it cannot safely depend on one HTTP/LiveView process or one all-or-nothing database cascade.
- **Rules:**
  1. Deletion orchestration has durable operation identity and explicit state/progress.
  2. Each destructive step is repeat-safe or protected by durable invariants.
  3. Partial processor/system failure produces unresolved/retryable state, not false completion.
  4. New eligible writes/processing are blocked or governed appropriately while deletion is pending.
  5. Deletion completion is verified against the declared scope.
- **Failure behaviour:** Remain `DELETION_PENDING`/unresolved with visible retry/reconciliation requirements until all mandatory scope is satisfied or an explicit retained-by-obligation exception applies.
- **Security/privacy:** Workflow payloads contain minimum identifiers/routing data; sensitive copies are not replicated into job payloads unnecessarily.
- **Performance/scaling:** Large deletions use bounded async/batched execution and must not starve OLTP; processor-specific concurrency is isolated.
- **Enforcement/downstream:** AR-008 owns monitoring/reconciliation/incident tooling; Domain Dossiers define category operations; AR-009 proves retry, restart and partial-failure correctness.

## ARC-236 — Deletion completes only when every eligible identifiable representation is deleted or irreversibly anonymised and verified

- **Decision source:** AR-007 P1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-004`; related Analytics deletion requirements and `ARQ-STATE-001`; cross-reference `ARC-105`, `ARC-106`, `ARC-108`, `ARC-235`
- **Decision:** A primary-row delete is insufficient. Full-deletion completion requires every eligible identifiable representation to be deleted or irreversibly anonymised according to category law, including authoritative records, health/check-in state, journals, uploads, object derivatives/thumbnails, extracted values, search/analytics/read projections, caches, signed-link capability, superseded eligible files, temporary worker material and applicable external processors.
- **Rationale:** Privacy obligations attach to the person's identifiable data footprint, not merely to one canonical table.
- **Rules:**
  1. Deletion scope explicitly enumerates representation classes/capabilities.
  2. Derived/index/cache copies are governed as deletion targets, not assumed to vanish eventually without proof.
  3. Outstanding bearer/signed delivery capability is revoked/invalidated as part of deletion.
  4. External processor deletion is tracked to a verifiable terminal state where applicable.
  5. Completion evidence is sufficient to detect skipped representation classes.
- **Failure behaviour:** Any mandatory unverified class keeps deletion incomplete/unresolved.
- **Security/privacy:** Verification must not retain reconstructive copies merely to prove deletion.
- **Performance/scaling:** Verification uses bounded inventories/contracts rather than uncontrolled global scans where possible.
- **Enforcement/downstream:** AR-008 defines processor evidence/operational dashboards; AR-009 exercises representative deletion scope under realistic data volume.

## ARC-237 — Anonymisation may substitute for deletion only where policy permits and the result is irreversibly non-identifiable for the governed purpose

- **Decision source:** AR-007 P1.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-004`, `ARQ-STATE-005`; Analytics deletion/privacy requirements
- **Decision:** Irreversible anonymisation is a permitted deletion outcome only where the governing category/policy allows it and the remaining data cannot reasonably reconstruct or relink the deleted identity for the governed purpose. Pseudonymisation, masking, renaming or hiding direct identifiers is not automatically anonymisation.
- **Rationale:** A row labelled “Deleted User” while preserving stable linkage keys can still retain the participant relationship and therefore does not satisfy irreversible deletion semantics.
- **Rules:**
  1. Anonymisation design must identify direct and indirect/linkage identifiers relevant to the dataset.
  2. Retained analytical/statistical data must not permit re-identification through platform-controlled linkage.
  3. Pseudonymised data remains personal/identifiable data and stays under applicable lifecycle law.
  4. Anonymisation methods are versioned/proofable for affected categories.
- **Failure behaviour:** If irreversibility cannot be demonstrated, treat the data as still identifiable and continue deletion/retention governance accordingly.
- **Security/privacy:** No hidden mapping/key may be retained merely for convenience if it defeats the claimed anonymisation outcome.
- **Performance/scaling:** Anonymisation transformations must be batchable/idempotent and preserve only approved aggregate utility.
- **Enforcement/downstream:** Privacy/security proof in AR-008/JIT; Domain Dossiers classify eligible data and permitted anonymisation outcomes.

## ARC-238 — Retained-by-obligation data is minimised and isolated from ordinary participant use after deletion

- **Decision source:** AR-007 P1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-005`, `ARQ-IAM-004`, `ARQ-IAM-007`; payment/professional/security retention requirements
- **Decision:** Where tax/accounting/payment/dispute, professional, fraud/security or legal obligations require retention, only the necessary evidence/identity fields are retained in a restricted retention class. Such retained records do not preserve an ordinary participant account/profile relationship and are excluded from marketing, personalisation, recommendations, ordinary analytics and new entitlement use unless an independent lawful basis explicitly requires otherwise.
- **Rationale:** Lawful retention of evidence is not permission to keep the user functionally alive in the product.
- **Rules:**
  1. Retained records have explicit purpose/category/access restrictions.
  2. Ordinary product-facing lookups exclude retained-only identity by default.
  3. Staff access is least-privilege and auditable according to retention purpose.
  4. When the obligation expires and no hold remains, deletion resumes according to policy.
- **Failure behaviour:** Unclassified retained data is quarantined from ordinary use pending governance rather than silently remaining active.
- **Security/privacy:** Retention stores/views minimise identifiers and block secondary use.
- **Performance/scaling:** Restricted retention may use separate projections/access paths where justified but need not imply a separate service/database.
- **Enforcement/downstream:** Domain Dossiers define retained evidence; AR-004 authorization law governs access; AR-008 monitors retention expiry and access.

## ARC-239 — Legal holds are record/purpose-scoped and pause only the deletion they actually govern

- **Decision source:** AR-007 P1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-005`, `ARQ-IAM-004`, `ARQ-IAM-007`
- **Decision:** Legal/professional holds are explicit governed records/evidence with affected record/category scope, purpose, authority, owner, activation time and release condition. A hold blocks deletion only for the records/purpose it legitimately covers; unrelated eligible data continues through deletion.
- **Rationale:** A single account-wide hold flag creates excessive retention and violates minimisation.
- **Rules:**
  1. Holds require named authority/provenance and review/release semantics.
  2. Scope must be narrow enough to identify which deletion operations are suspended.
  3. Hold state does not expose retained records to ordinary product use.
  4. When the hold is released, suspended deletion resumes automatically/durably where applicable.
- **Failure behaviour:** Expired/invalid hold metadata cannot silently extend retention; ambiguous holds require governed review.
- **Security/privacy:** Hold details and held records are access-controlled and auditable.
- **Performance/scaling:** Hold evaluation is indexed/scoped so deletion orchestration need not globally scan legal data.
- **Enforcement/downstream:** AR-008 owns review/expiry/operational evidence; expert/legal policy determines valid hold authority.

## ARC-240 — Each data-owning capability implements a platform deletion contract; orchestration coordinates but does not steal domain semantics

- **Decision source:** AR-007 P1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-STATE-005`; cross-reference `ARC-049`, `ARC-050`, `ARC-235`
- **Decision:** A platform deletion orchestration boundary coordinates deletion, but every data-owning capability declares how its eligible data is discovered, deleted/anonymised, externally propagated, reconciled and verified. The orchestrator does not hard-code every domain table/provider forever or become the owner of domain record meaning.
- **Rationale:** Cross-cutting privacy requires one coherent completion contract while domain ownership must remain with the capability that understands the record's lawful/business semantics.
- **Rules:**
  1. Capability deletion contracts are versioned/testable and declare scope/classes handled.
  2. Contracts distinguish delete, anonymise, retain-by-obligation and hold outcomes.
  3. New data-bearing capabilities cannot ship without registering their deletion/export/retention responsibilities.
  4. Central orchestration aggregates status/evidence and coordinates dependencies only.
- **Failure behaviour:** Missing/unregistered deletion capability is a release/blocking defect, not silently ignored scope.
- **Security/privacy:** Contracts expose minimum orchestration metadata and keep sensitive payload handling in the owner.
- **Performance/scaling:** Capability-local batching prevents one global deletion routine from becoming a monolithic bottleneck.
- **Enforcement/downstream:** Domain Map/Dossiers assign owners; AR-008 verifies registry/compliance; Feature Pack gate manifests require lifecycle contract coverage.

## ARC-241 — Minimal non-reconstructive deletion/suppression evidence may survive to prove deletion and prevent resurrection

- **Decision source:** AR-007 P1.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-STATE-006`, `ARQ-IAM-007`; cross-reference `ARC-064`, `ARC-235`
- **Decision:** Completed deletion may retain only the minimum lawful non-reconstructive evidence required to prove the operation, coordinate processor completion and prevent resurrection after restore/re-registration. Such evidence may include deletion-operation identity, completion time, policy/version, completed scope classes and verification state, plus only the minimum former-identity suppression reference demonstrably required. It must not become a hidden participant profile.
- **Rationale:** Zero surviving suppression evidence can allow backups/imports to recreate deleted identities, while excessive tombstones defeat deletion itself.
- **Rules:**
  1. Suppression evidence has a narrow purpose and restricted access.
  2. It cannot contain health/profile/history payloads beyond what is strictly necessary.
  3. The exact former-identity token/hash/tombstone design requires privacy/security proof; no reversible convenient mapping is assumed.
  4. Re-registration creates a new governed identity relationship and may not automatically reconnect deleted history.
- **Failure behaviour:** If suppression matching cannot be performed safely, restoration/re-import remains blocked for affected records until reconciliation.
- **Security/privacy:** Suppression evidence is excluded from marketing, personalisation and ordinary analytics and receives its own retention policy.
- **Performance/scaling:** Matching/indexing mechanisms must resist enumeration and remain bounded for restore/import checks.
- **Enforcement/downstream:** AR-008 chooses/proves suppression representation and access; P2 governs restore replay; Domain/IAM dossiers govern re-registration semantics.

## ARC-242 — Account closure, consent withdrawal and full deletion are independent governed operations

- **Decision source:** AR-007 P1.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-IAM-006`; cross-reference `ARC-126`, `ARC-127`, `ARC-128`, `ARC-233`
- **Decision:** Account closure/deactivation, consent withdrawal and full deletion remain distinct operations with different scope and effects. Closure stops ordinary account use without claiming data erasure; consent withdrawal stops future consent-dependent processing and invalidates dependent authority without rewriting prior lawful history; full deletion irreversibly deletes/anonymises every eligible representation subject only to explicit retention/hold exceptions.
- **Rationale:** One `inactive` flag cannot accurately represent these materially different legal/product/security consequences.
- **Rules:**
  1. User/admin messaging names the actual lifecycle operation accurately.
  2. Consent withdrawal triggers the dependency invalidation law from AR-004.
  3. Closure may precede later deletion but does not imply deletion completion.
  4. Full deletion completion cannot be reversed by reopening the account.
- **Failure behaviour:** Ambiguous user intent routes to the explicit lifecycle workflow rather than silently selecting a more destructive or less protective operation.
- **Security/privacy:** Each operation has its own authorization, audit and evidence requirements proportional to risk.
- **Performance/scaling:** Operations may share infrastructure but keep separate semantic state and reconciliation.
- **Enforcement/downstream:** UI/Domain Dossiers expose distinct actions; AR-008 audit/operations; P2 backup/restore handling respects all three transitions.

**P1 deferrals:** exact retention durations/statutes/professional rules; final lifecycle Resource/table ownership; legal-hold UI; exact anonymisation algorithms; processor deletion APIs; deletion-registry representation; suppression/tombstone encoding; detailed re-registration merge rules; exact batching/concurrency/retry constants; proof/monitoring implementation. These remain assigned to expert/legal/privacy inputs, Domain Map/Dossiers, AR-008/009, JIT Feature Pack work and Architectural Proof.


## 4K.2 Round P2 — Backup/Restore Deletion Replay, Recovery Suppression, Export Lifecycle & Deletion-Safe Restore Testing

**Accepted answer set:** `P2.1 B, P2.2 B, P2.3 B, P2.4 B, P2.5 B, P2.6 B, P2.7 B, P2.8 B, P2.9 B, P2.10 B, P2.11 B, P2.12 B`

## ARC-243 — Disaster recovery restores the minimum complete authority set, not PostgreSQL bytes alone

- **Decision source:** AR-007 P2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-002`, `ARQ-STATE-006`, `ARQ-PERF-147`, `ARQ-PERF-161`; cross-reference `ARC-009`, `ARC-019`, `ARC-077`, `ARC-099`
- **Decision:** Disaster recovery must recover the minimum complete set of authoritative/recovery-critical state needed to reconstitute correct service, including PostgreSQL/PITR where applicable, durable object state, required configuration, recoverable secrets/key material, deletion/withdrawal suppression authority, and other non-rebuildable state whose loss would corrupt business truth. Caches, process state and rebuildable derivatives are not restored as authority merely because they existed before failure.
- **Rationale:** Restoring only database bytes can leave object references, credentials, deletion evidence or required configuration inconsistent and produce an apparently running but semantically invalid platform.
- **Rules:**
  1. Recoverable components are classified by whether they are authoritative, recovery-critical, independently durable or rebuildable.
  2. Recovery dependencies and restoration order are documented/proved rather than inferred during an incident.
  3. Object/media durability follows its governed storage/recovery class; rebuilding is allowed only where the source remains valid.
  4. Secrets/configuration recovery uses approved secure mechanisms and may require rotation/reconciliation after restore.
- **Failure behaviour:** Missing recovery-critical state keeps the platform recovery-gated rather than declaring normal readiness.
- **Security/privacy:** Recovery copies remain encrypted/restricted and may not become alternate ordinary-access stores.
- **Performance/scaling:** Recovery planning separates essential authority from rebuildable state so restoration is bounded by critical dependencies rather than every cache/derivative.
- **Enforcement/downstream:** AR-008 selects/operates backup and secret/config recovery mechanisms; AR-009 proves representative full-service reconstruction.

## ARC-244 — High availability/failover and historical backup/PITR are separate protections

- **Decision source:** AR-007 P2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-147`, `ARQ-PERF-166`, `ARQ-OPS-002`
- **Decision:** High availability/failover protects service continuity, while backup/PITR protects recoverability from corruption, destructive operator action, bad migration, historical data loss and disaster. Neither control substitutes for the other for data classes requiring both.
- **Rationale:** A healthy standby can faithfully replicate corruption or a destructive write; conversely a backup does not provide immediate service continuity.
- **Rules:**
  1. HA and backup have separate objectives, evidence and failure scenarios.
  2. Replicas/standbys are not counted as historical backup merely because they contain another copy.
  3. Recovery design addresses common-mode failure domains rather than assuming colocated copies are independent.
- **Failure behaviour:** Failure of one protection class invokes its governed degraded/recovery path without falsely claiming the other control has covered it.
- **Security/privacy:** Backup retention/access and standby access are governed separately.
- **Performance/scaling:** Capacity and retention for HA and backup are sized from their distinct objectives.
- **Enforcement/downstream:** AR-008 operational topology/runbooks; AR-009 failover and restore exercises.

## ARC-245 — Historical encrypted backups age out normally; participant deletion is enforced through recovery-time suppression rather than unsafe backup mutation

- **Decision source:** AR-007 P2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-004`, `ARQ-STATE-006`, `ARQ-AN-153`
- **Decision:** Completed deletion does not normally require surgically rewriting every immutable historical backup/PITR chain. Deleted data may remain only inside encrypted recovery-only backup retention until normal expiry, with no ordinary participant-level retrieval. Any restore must apply current deletion/withdrawal suppression before service returns.
- **Rationale:** Mutating historical backup chains can destroy recovery integrity, while treating backup copies as exempt forever would allow deleted identities to re-enter service. Recovery-time suppression reconciles both obligations.
- **Rules:**
  1. Backup retention is bounded/governed and not indefinite by convenience.
  2. Backups are not ordinary archives or participant-access stores.
  3. A request to restore one deleted participant from backup is prohibited.
  4. Backup expiry/deletion is itself operationally verifiable.
- **Failure behaviour:** If suppression cannot be proved for a candidate restore, that restore cannot become normal production authority.
- **Security/privacy:** Backup access is exceptional, audited and restricted; deleted records may not be mined from backups for marketing, support or analytics.
- **Performance/scaling:** Avoids per-subject mutation of backup chains while preserving deletion correctness at recovery boundaries.
- **Enforcement/downstream:** AR-008 backup retention/access controls and restore tooling; AR-009 restore/deletion-resurrection tests.

## ARC-246 — Deletion and consent-withdrawal suppression must be recoverable beyond the selected restore point

- **Decision source:** AR-007 P2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-004`, `ARQ-STATE-006`, `ARQ-AN-153`, `ARQ-IAM-006`, `ARQ-PERF-148`; cross-reference `ARC-128`, `ARC-241`
- **Decision:** Recovery semantics must preserve enough independently recoverable deletion/withdrawal suppression truth to reapply privacy-effective transitions that occurred after the backup/PITR point selected for restoration. Exact storage/replication/tombstone implementation is deferred, but an older restore point may not semantically undo a completed deletion or material consent withdrawal.
- **Rationale:** Restoring Monday after a Tuesday deletion cannot be allowed to recreate Tuesday's deleted participant merely because the database RPO selected an older point.
- **Rules:**
  1. Recovery identifies the restored data point and the later deletion/withdrawal transitions that must be re-applied.
  2. Suppression evidence remains minimal/non-reconstructive per `ARC-241`.
  3. Suppression authority has recovery protection appropriate to its correctness role and does not depend solely on the same older restore point it must correct.
  4. Reapplication is idempotent and covers affected authoritative/derived/external representations as required.
- **Failure behaviour:** Missing or ambiguous suppression authority blocks normal-service promotion until reconciled; privacy-effective transitions are not guessed away.
- **Security/privacy:** Suppression data has narrowly scoped purpose/access and cannot become a shadow identity history.
- **Performance/scaling:** Replay is bounded/indexable by operation/time/scope rather than scanning all historical participants.
- **Enforcement/downstream:** AR-008 proves the concrete suppression-recovery mechanism; AR-009 exercises restore points older than known deletion/withdrawal events.

## ARC-247 — Restored environments remain recovery-gated until deletion/withdrawal replay and critical reconciliation complete

- **Decision source:** AR-007 P2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-006`, `ARQ-AN-153`, `ARQ-PERF-163`, `ARQ-OPS-002`; cross-reference `ARC-246`
- **Decision:** A restored environment does not become normal service authority merely because PostgreSQL starts. It enters an explicit recovery state in which required objects/configuration/secrets are restored, deletion and consent-withdrawal consequences are replayed, critical derived state is reconciled, and recovery verification passes before ordinary traffic resumes.
- **Rationale:** Serving traffic while stale deleted/revoked state still exists turns temporary recovery inconsistency into a privacy/security incident.
- **Rules:**
  1. Recovery readiness is distinct from process liveness and infrastructure readiness.
  2. Normal user traffic and external side effects remain gated until mandatory recovery invariants pass.
  3. Recovery steps are repeatable/idempotent where feasible and leave evidence.
  4. Controlled operator access during recovery follows privileged/audit law.
- **Failure behaviour:** Any failed mandatory recovery stage leaves service recovery-gated with explicit unresolved state.
- **Security/privacy:** Deleted/revoked identities are never briefly exposed under a "fix later" policy.
- **Performance/scaling:** Recovery can rebuild non-critical projections after authority is safe where their absence merely degrades freshness, but correctness gates finish first.
- **Enforcement/downstream:** AR-008 readiness/runbooks; AR-009 disaster-recovery exercises and release gates.

## ARC-248 — Recovery verification proves semantic authority, including non-resurrection and critical cross-store consistency

- **Decision source:** AR-007 P2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-163`, `ARQ-STATE-006`, `ARQ-OPS-002`, `ARQ-AN-153`; related critical-state requirements
- **Decision:** Restore proof must verify semantic validity, not merely application startup. Applicable verification covers database authority/integrity, required object references, recoverable configuration/secrets, deletion/withdrawal suppression, absence of deleted-identity resurrection, critical financial/entitlement consistency, and required derived-state reconstruction or safe degradation.
- **Rationale:** A technically successful restore can still be business-invalid or privacy-invalid.
- **Rules:**
  1. Verification checks are automated where practical and produce inspectable evidence.
  2. Critical discrepancies have explicit reconciliation/STOP behaviour.
  3. Verification includes representative negative checks for data that must remain absent.
  4. Recovery exercises periodically prove the procedure, not merely the backup artifact.
- **Failure behaviour:** Failed semantic verification blocks readiness and triggers controlled reconciliation/escalation.
- **Security/privacy:** Verification queries/results are minimised and protected; proof does not create new sensitive shadow datasets.
- **Performance/scaling:** Verification is designed to scale with data volume using inventories/sampling only where sampling cannot weaken hard invariants; mandatory non-resurrection checks remain deterministic for governed suppression scope.
- **Enforcement/downstream:** AR-008 observability/runbooks/evidence; AR-009 release and disaster-recovery testing.

## ARC-249 — Derived analytics/search/read models rebuild only through current privacy suppression and deletion rules

- **Decision source:** AR-007 P2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-AN-018`, `ARQ-AN-020`, `ARQ-AN-152`, `ARQ-AN-153`, `ARQ-AN-161`, `ARQ-STATE-004`; cross-reference `ARC-060`, `ARC-108`, `ARC-181`
- **Decision:** Replay/backfill/restore of analytics, search indexes, caches and other derived read models must filter through current deletion/anonymisation/suppression authority. Retained finance/security/professional evidence may not be repurposed to reconstruct a deleted participant analytics identity, health profile, recommendation history or searchable participant relationship.
- **Rationale:** A rebuildable projection is only safe if its rebuild pipeline preserves the higher-authority privacy state.
- **Rules:**
  1. Rebuild sources and joins honour current permitted identity/linkage state.
  2. Deleted participant-level event/exposure identities are excluded/anonymised as governed before projection.
  3. Old projection snapshots are not blindly promoted over cleaned authority.
  4. External analytical processors receive required deletion/suppression propagation.
- **Failure behaviour:** If suppression cannot be applied safely, affected projections remain unavailable/degraded rather than rebuilding forbidden identity.
- **Security/privacy:** Detailed health/journal data remains outside ordinary analytics under existing law; restore does not loosen that boundary.
- **Performance/scaling:** Rebuilds use bounded, idempotent pipelines and may trade freshness for correctness during recovery.
- **Enforcement/downstream:** AR-008 analytics/search recovery procedures; AR-009 replay/backfill/privacy tests.

## ARC-250 — RPO/RTO are class-specific recovery objectives; completed privacy revocation/deletion remains a hard non-resurrection invariant

- **Decision source:** AR-007 P2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-148`, `ARQ-STATE-006`, `ARQ-AN-153`, `ARQ-OPS-002`
- **Decision:** Recovery objectives are defined by business/state class, with stricter objectives for financial, entitlement, safety, identity and other critical durable authority and looser/rebuild semantics permitted for suitable derivatives. Exact values are deferred. Regardless of RPO/RTO, a completed deletion or materially effective withdrawal may not be treated as reversibly lost merely because the selected backup point predates it.
- **Rationale:** Availability/recovery targets are operational objectives; privacy-effective deletion/withdrawal is a correctness boundary.
- **Rules:**
  1. State classes declare recovery priority, RPO/RTO target and restoration/rebuild mechanism.
  2. Positively acknowledged durable critical commits follow their approved durability class.
  3. Deletion/withdrawal replay is a required recovery overlay, not ordinary best-effort recent data.
  4. Exact numerical targets require AR-008/evidence approval.
- **Failure behaviour:** Missed RPO/RTO triggers incident/evidence handling; it does not authorise privacy resurrection or fabricated state.
- **Security/privacy:** Recovery classification cannot downgrade sensitive deletion/retention rules for convenience.
- **Performance/scaling:** Enables staged recovery by criticality without restoring every derivative before service.
- **Enforcement/downstream:** AR-008 defines values/runbooks; AR-009 validates class-specific objectives under exercises.

## ARC-251 — Participant export is a governed data-release product assembled from domain-owned eligible records

- **Decision source:** AR-007 P2.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-007`, `ARQ-AN-118`, `ARQ-AN-119`; cross-reference `ARC-040`, `ARC-043`, `ARC-123`
- **Decision:** A participant export is not a database dump or a mirror of one UI. It is a governed release assembled from each owning capability's eligible records into approved human-readable and structured representations, with eligible original uploads where appropriate, subject to redaction, third-party privacy, retention, legal/hold and entitlement constraints.
- **Rationale:** Data portability/access rights require meaningful release while preserving restrictions that still lawfully apply.
- **Rules:**
  1. Export eligibility is declared by data-owning capabilities.
  2. Viewing a record/dashboard does not automatically grant bulk export of every related field.
  3. Third-party and restricted evidence is redacted/excluded according to policy.
  4. Export formats retain sufficient semantics/provenance to be useful without exposing implementation-only secrets.
- **Failure behaviour:** Unresolved eligibility/redaction scope fails closed for the affected category rather than over-disclosing.
- **Security/privacy:** Export is a high-value disclosure surface with explicit authorization and data minimisation.
- **Performance/scaling:** Export contracts support bounded streaming/batching for large datasets.
- **Enforcement/downstream:** Domain Dossiers define export fields/categories; AR-008 security/audit; AR-009 volume/security tests.

## ARC-252 — Export authority and disclosure scope are revalidated through request, generation and delivery

- **Decision source:** AR-007 P2.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-007`, `ARQ-AN-119`, `ARQ-PERF-103`, `ARQ-IAM-005`, `ARQ-IAM-006`; cross-reference `ARC-151`, `ARC-154`
- **Decision:** Sensitive export workflows strongly verify/authorise the request and revalidate material current recipient, scope, row/field access, purpose, privacy/redaction, retention/hold and delivery eligibility at generation/delivery where later state can invalidate the original request. Historic queueing is not permanent disclosure authority.
- **Rationale:** Large exports may finish long after request time; permission/relationship/consent state can change before disclosure.
- **Rules:**
  1. Export operation records the requested scope and governing policy context.
  2. Practitioner/relationship-derived access must still be live where required at release time.
  3. A changed filter or broken scope cannot broaden disclosure.
  4. Superseded/revoked requests cancel/no-op or regenerate under governed policy.
- **Failure behaviour:** Failed reauthorization prevents artifact release and records an appropriate safe outcome.
- **Security/privacy:** Minimum-data job payloads and non-enumerating delivery links apply.
- **Performance/scaling:** Revalidation queries remain bounded/indexed and do not require materialising full export content before authorization.
- **Enforcement/downstream:** AR-008 export security/audit; Domain Dossiers define eligibility; AR-009 race/revocation tests.

## ARC-253 — Large or sensitive exports use bounded durable generation and short-lived protected delivery with mandatory artifact expiry/deletion

- **Decision source:** AR-007 P2.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-007`, `ARQ-AN-120`, `ARQ-AN-121`, `ARQ-PERF-072`, `ARQ-PERF-087`; cross-reference `ARC-146`, `ARC-168`, `ARC-169`
- **Decision:** Where synchronous generation would be unsafe or expensive, exports run as bounded durable work that produces a protected temporary artifact. Delivery uses current authorization and a short-lived capability; artifacts have explicit retention/expiry and are deleted after expiry or earlier lifecycle triggers. Generated exports never become uncontrolled permanent shadow copies.
- **Rationale:** Large exports combine high resource cost with concentrated privacy risk.
- **Rules:**
  1. Generation uses bounded batching/streaming and isolated capacity appropriate to workload.
  2. Temporary artifacts use protected storage, never public random URLs.
  3. Artifact access is revocable/current-policy aware where material.
  4. Expiry/deletion is durable, retryable and reconcilable.
  5. Export artifacts participate in participant deletion where applicable.
- **Failure behaviour:** Generation/delivery failure leaves explicit recoverable operational state; stale artifacts are not silently retained.
- **Security/privacy:** Encryption/access controls and short-lived delivery capabilities apply according to sensitivity.
- **Performance/scaling:** Large exports do not execute as unbounded LiveView/HTTP memory work and may be throttled below critical OLTP.
- **Enforcement/downstream:** AR-008 storage/expiry/monitoring; AR-009 large-export and cleanup tests.

## ARC-254 — Sensitive/material exports require strong verification, minimised audit evidence, safe file encoding and governed delivery

- **Decision source:** AR-007 P2.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-STATE-007`, `ARQ-AN-122`, `ARQ-AN-123`, `ARQ-IAM-003`, `ARQ-IAM-007`; cross-reference `ARC-115`, `ARC-131`, `ARC-132`
- **Decision:** Material/sensitive exports require authentication assurance/step-up proportional to risk, audit of actor/scope/purpose/outcome/destination metadata where relevant, secure short-lived delivery, and format-specific output safety. Spreadsheet-compatible output must neutralise formula/link/command injection from user-controlled cells. Audit evidence must not duplicate the full sensitive export payload.
- **Rationale:** A participant-requested export remains a high-value exfiltration surface and generated files can introduce secondary execution risk.
- **Rules:**
  1. High-risk exports require recent/step-up authentication where policy demands.
  2. Export audit retains minimum sufficient metadata rather than the exported dataset.
  3. CSV/spreadsheet output applies governed injection-safe encoding/sanitisation.
  4. Delivery destinations/channels are restricted to approved secure mechanisms.
  5. Export audit/temporary artifacts have independent governed retention.
- **Failure behaviour:** Insufficient assurance, unsafe output generation or delivery-policy failure blocks release without leaking sensitive details.
- **Security/privacy:** Export access and audit are least-privilege; audit cannot become an uncontrolled replica.
- **Performance/scaling:** Safety transformations are streamed/bounded where possible and included in workload sizing.
- **Enforcement/downstream:** AR-008 defines assurance/audit/storage controls; AR-009 security tests formula injection, link expiry, replay and unauthorized access.

**P2 deferrals:** exact backup/PITR vendor/product, backup retention periods, RPO/RTO numerical values, concrete deletion/suppression ledger/tombstone representation, encryption/key-management product, off-site/failure-domain topology, restore automation/runbook tooling, exact verification query suite, export formats/schemas, step-up thresholds, artifact expiry durations and object layout remain assigned to AR-008/009, expert/legal/privacy gates, Domain Dossiers, JIT Feature Pack work and Architectural Proof.


## 4K.3 AR-007 Closure Audit — PASS

The final AR-007 closure audit mechanically re-parsed `ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` and found exactly **51 frozen ARQs whose Primary downstream workstreams include AR-007**:

- **Performance:** 12 — `ARQ-PERF-004`, `ARQ-PERF-045`, `ARQ-PERF-046`, `ARQ-PERF-103`, `ARQ-PERF-104`, `ARQ-PERF-129`, `ARQ-PERF-147`, `ARQ-PERF-148`, `ARQ-PERF-158`, `ARQ-PERF-161`, `ARQ-PERF-163`, `ARQ-PERF-166`
- **Analytics:** 28 — `ARQ-AN-005`, `ARQ-AN-018`, `ARQ-AN-019`, `ARQ-AN-020`, `ARQ-AN-022`, `ARQ-AN-040`, `ARQ-AN-042`, `ARQ-AN-046`, `ARQ-AN-050`, `ARQ-AN-056`, `ARQ-AN-057`, `ARQ-AN-058`, `ARQ-AN-059`, `ARQ-AN-060`, `ARQ-AN-066`, `ARQ-AN-068`, `ARQ-AN-121`, `ARQ-AN-140`, `ARQ-AN-142`, `ARQ-AN-152`, `ARQ-AN-153`, `ARQ-AN-161`, `ARQ-AN-169`, `ARQ-AN-176`, `ARQ-AN-188`, `ARQ-AN-202`, `ARQ-AN-204`, `ARQ-AN-210`
- **System:** 1 — `ARQ-SYS-004`
- **IAM:** 2 — `ARQ-IAM-005`, `ARQ-IAM-006`
- **State:** 6 — `ARQ-STATE-001`, `ARQ-STATE-003`, `ARQ-STATE-004`, `ARQ-STATE-005`, `ARQ-STATE-006`, `ARQ-STATE-007`
- **Content:** 1 — `ARQ-CONTENT-004`
- **Operations:** 1 — `ARQ-OPS-002`

**Closure result: PASS.** P1/P2 plus earlier accepted Architecture Law cover every routed ARQ without requiring a new P3 or reopening Product Law.

Coverage findings:

1. **Lifecycle, deletion, retention and holds** — `ARC-233...ARC-242` establish separate data-lifecycle semantics, expert-owned retention inputs, durable/idempotent full-deletion orchestration, representation-complete verification, irreversible anonymisation rules, isolated retained-by-obligation state, narrowly scoped legal holds, capability-owned deletion contracts, minimal non-reconstructive suppression evidence, and separation of closure/withdrawal/deletion. This directly closes the `ARQ-STATE-003...006` lifecycle/privacy core and the lifecycle/privacy implications of routed IAM/Analytics requirements.
2. **Backup, restore and disaster recovery privacy** — `ARC-243...ARC-250` establish recovery of the full minimum authority set, HA/backup separation, bounded encrypted backup ageing, independently recoverable deletion/withdrawal suppression, recovery-gated restore promotion, semantic restore verification, deletion-safe analytical/search replay, and class-specific RPO/RTO with hard non-resurrection. This closes `ARQ-PERF-147`, `ARQ-PERF-148`, `ARQ-PERF-161`, `ARQ-PERF-163`, `ARQ-STATE-006`, `ARQ-AN-153` and `ARQ-OPS-002` while preserving AR-008 ownership of concrete operational mechanisms/values.
3. **Participant export lifecycle** — `ARC-251...ARC-254` establish domain-owned export eligibility, repeated/current authorization, bounded durable generation, protected temporary artifacts, expiry/deletion, strong assurance, minimised audit and safe spreadsheet output. This closes `ARQ-STATE-007` and the AR-007 portion of `ARQ-AN-118...123`/related export requirements without weakening AR-004/005/008 controls.
4. **Analytics/privacy inheritance** — routed Analytics requirements whose core HOW law was already locked in AR-003/005/006 remain authoritative and are privacy-completed by AR-007 rather than duplicated. Specifically: governed analytical event identity/contracts (`ARQ-AN-005`) are implemented by `ARC-180...181`; detailed health/journal exclusion and authoritative analytics truth (`ARQ-AN-019`, `ARQ-AN-022`) are preserved by `ARC-179...182`, `ARC-201...205` and `ARC-249`; lifecycle distinctions (`ARQ-AN-040`, `ARQ-AN-042`, `ARQ-AN-046`) remain domain-semantic truth while `ARC-233...242` govern their retention/deletion lifecycle; acquisition/identity/privacy constraints (`ARQ-AN-050`, `ARQ-AN-057`) remain governed by `ARC-184...188`, `ARC-228...229`, with deletion consequences supplied by P1/P2; sensitive failed-event/quarantine retention (`ARQ-AN-140`) remains governed by analytical event quarantine plus `ARC-234...240`; fact-versus-interpretation history (`ARQ-AN-142`) remains immutable/superseding evidence under prior law plus category-specific AR-007 retention; survey/predictive evidence (`ARQ-AN-169`, `ARQ-AN-176`) gains no new AR-007 mechanism beyond current privacy/retention/deletion contracts; and experiment immutability/privacy/deletion compatibility (`ARQ-AN-202`, `ARQ-AN-204`, `ARQ-AN-210`) remains governed by `ARC-187...188` plus P1/P2 deletion/suppression.
5. **Revocation, queued work and storage/access interactions** — `ARQ-PERF-045`, `ARQ-PERF-046`, `ARQ-PERF-103`, `ARQ-PERF-104`, `ARQ-PERF-129`, `ARQ-IAM-005`, `ARQ-IAM-006`, `ARQ-STATE-001` and `ARQ-CONTENT-004` are already enforced by AR-003/004/005/006 current-authority, protected-storage, consent/revocation and minimum-signal law; AR-007 adds lifecycle/deletion/export semantics without duplicating those action-boundary mechanisms.
6. **No extra infrastructure is legislated here.** Exact backup product, PITR mechanics, off-site topology, secret manager, suppression-ledger representation, retention durations, processor APIs, RPO/RTO values, recovery automation, monitoring and operational test schedules remain correctly assigned to AR-008/009, expert/privacy/legal gates, Domain Dossiers, JIT Feature Packs and Architectural Proof.

**No Product Law, DEC, OQ, ARQ or prior ARC amendment is required. No unresolved contradiction remains inside AR-007.**

**AR-007 status:** COMPLETE through `ARC-254`; final 51-ARQ closure audit PASS.

# 4L. AR-008 — Reliability, Deployment, Operations & Observability

## 4L.1 Round O1 — Runtime Failure, Health, Dependency Isolation & Safe Deployment

**Accepted answer set:** `O1.1 B, O1.2 B, O1.3 B, O1.4 B, O1.5 B, O1.6 B, O1.7 B, O1.8 B, O1.9 B, O1.10 B, O1.11 B, O1.12 B`

## ARC-255 — Availability objectives are capability/business-class specific; correctness invariants are not error-budgeted

- **Decision source:** AR-008 O1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-139`, `ARQ-PERF-140`, `ARQ-PERF-166`
- **Decision:** Define measurable availability/SLO classes according to business criticality rather than one platform-wide uptime promise. Availability may use explicit error budgets where appropriate, but correctness, safety, privacy, payment, entitlement, identity and other hard invariants are not relaxed by availability targets.
- **Rationale:** Different capabilities tolerate different interruption/freshness envelopes, while a high uptime percentage cannot legitimise corrupted authority or unsafe outcomes.
- **Rules:**
  1. Capability classes and their availability objectives are explicit and evidence-backed.
  2. High-criticality authority paths receive stricter availability/recovery treatment than convenience or stale-tolerant projections where justified.
  3. Literal 100% availability is not promised as an architectural assumption.
  4. Error budgets govern availability/product reliability trade-offs only where applicable; they never budget correctness violations.
- **Failure behaviour:** Capability degradation is surfaced according to its class and may consume availability budget, while correctness violations trigger incident/STOP handling rather than being accepted as budget spend.
- **Security/privacy:** Security/privacy invariants remain hard constraints regardless of SLO attainment.
- **Performance/scaling:** Capacity/headroom and scaling targets are derived from capability class and measured demand rather than one universal service target.
- **Enforcement/downstream:** O2 defines observable SLI evidence; AR-009 assigns/measures numerical performance and capacity objectives; release gates prove the applicable class.

## ARC-256 — Startup, liveness, readiness and capability degradation are distinct operational contracts

- **Decision source:** AR-008 O1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-144`, `ARQ-PERF-154`, `ARQ-PERF-166`; cross-reference `ARC-018`
- **Decision:** Model startup completion, process/node liveness, readiness for intended traffic/work and capability-specific degraded state as distinct signals. A single undifferentiated health Boolean is insufficient.
- **Rationale:** Operators/orchestrators need to distinguish “still booting”, “restart may repair this process”, “alive but unsafe for traffic” and “partially degraded” to avoid destructive restart or traffic-routing behaviour.
- **Rules:**
  1. Startup completes only after mandatory safe initialisation needed to evaluate/use the instance.
  2. Liveness indicates a condition where restarting the current process/node can reasonably repair the failure.
  3. Readiness indicates whether the instance may safely receive the traffic/work assigned to it.
  4. Optional dependency/capability degradation may be represented without making the whole process unready or dead when safe operation remains possible.
  5. Full cache warmth is not a correctness prerequisite for readiness.
- **Failure behaviour:** Failed startup prevents promotion; liveness failure invokes restart/recovery; readiness failure drains/withholds traffic/work without fabricating process death.
- **Security/privacy:** Health endpoints/signals expose minimum safe operational information and do not leak secrets, internal topology or sensitive participant state.
- **Performance/scaling:** Readiness/startup checks are bounded and may not create dependency/database stampedes during concurrent node starts.
- **Enforcement/downstream:** Runtime/deployment adapters implement separate probes/signals; O2 monitors them; AR-009 pressure-tests startup/recovery behaviour.

## ARC-257 — Dependency failure changes only the readiness/capability semantics that truly depend on it; remote outages do not imply local process death

- **Decision source:** AR-008 O1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-145`, `ARQ-PERF-149`, `ARQ-PERF-151`, `ARQ-PERF-166`; cross-reference `ARC-163`, `ARC-164`, `ARC-221`, `ARC-232`
- **Decision:** Temporary external/dependency outage must produce capability-specific bounded degradation or readiness impact only where required. Liveness fails only where the current process/node is itself unhealthy and restart is a plausible remedy. Loss of mandatory authority such as safe PostgreSQL write access may remove the affected readiness without falsely declaring the BEAM process dead.
- **Rationale:** Restarting healthy application nodes because a remote service is down amplifies outages and can create cascades without repairing the dependency.
- **Rules:**
  1. Each material dependency declares whether it is mandatory, capability-scoped or optional for each traffic/work class.
  2. Optional providers normally degrade only their dependent capability.
  3. Mandatory authority unavailability blocks only the operations that cannot remain correct without it.
  4. Health evaluation uses bounded dependency checks and avoids turning the health system itself into a load source.
- **Failure behaviour:** Dependency loss selects the governed degraded/bulkhead/readiness path; dependency recovery restores capability after current-state validation rather than process restart optimism.
- **Security/privacy:** Degraded modes cannot bypass authorization, consent, privacy or entitlement controls merely to maintain availability.
- **Performance/scaling:** Dependency checks, timeouts and health fan-out are bounded and account for shared provider capacity.
- **Enforcement/downstream:** O2 defines dependency-health telemetry/alerts; AR-009 tests provider loss and recovery under load.

## ARC-258 — OTP supervision follows real failure dependencies and bounded restart intensity; crash loops escalate instead of restarting forever

- **Decision source:** AR-008 O1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-142`, `ARQ-PERF-143`, `ARQ-PERF-166`
- **Decision:** Structure supervision according to genuine runtime/failure dependency relationships. Recoverable failures may restart under intentional OTP policy, while repeated restart intensity/exhaustion becomes an explicit operational failure/escalation. Unrelated capabilities must not restart together solely because their source modules are nearby.
- **Rationale:** OTP supervision is a fault-containment mechanism; unbounded restart loops or oversized supervision blast radii can turn local defects into platform incidents.
- **Rules:**
  1. Supervisor boundaries document which failures should restart which children/components.
  2. Restart type/intensity are deliberate for long-lived runtime processes.
  3. Repeated crash loops are observable and escalate after bounded policy limits.
  4. Ephemeral request/task failures do not automatically restart unrelated long-lived runtime state.
- **Failure behaviour:** Recoverable child failure restarts inside its approved boundary; exhausted restart policy degrades/fails the affected capability/node and triggers operational response.
- **Security/privacy:** Restart/recovery may not reset security state into a weaker mode or bypass current authority.
- **Performance/scaling:** Restart storms are bounded; supervision design avoids simultaneous expensive reinitialisation where unnecessary.
- **Enforcement/downstream:** OTP supervision-tree review and failure-injection evidence are AR-008/009 gates; O2 monitors restart intensity/crash loops.

## ARC-259 — Overload is handled with backpressure, admission control, shedding and degradation before restarting healthy capacity

- **Decision source:** AR-008 O1.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-152`, `ARQ-PERF-153`, `ARQ-PERF-160`, `ARQ-PERF-166`; cross-reference `ARC-160`, `ARC-164`, `ARC-165`
- **Decision:** Treat overload primarily as a capacity/admission problem. Use bounded waiting, backpressure, throttling, queue isolation, admission control, load shedding or explicit degraded modes before restarting otherwise healthy nodes. Restart is reserved for state that restart can actually repair.
- **Rationale:** Restarting overloaded nodes redistributes outstanding demand and can amplify cascading failure while destroying useful warm capacity.
- **Rules:**
  1. Critical/authoritative traffic is protected ahead of optional/bulk work according to governed priority/isolation.
  2. Load shedding is explicit and never fabricates successful completion.
  3. Degraded paths are recurrently tested rather than incident-only theory.
  4. Autoscaling, where used, supplements rather than replaces admission/headroom planning.
- **Failure behaviour:** Overload triggers bounded degradation and recovery thresholds; inability to preserve critical correctness escalates rather than silently accepting work the system cannot safely complete.
- **Security/privacy:** Shedding/degradation cannot disable security/privacy enforcement.
- **Performance/scaling:** Headroom and overload thresholds are evidence-based and become AR-009 capacity gates.
- **Enforcement/downstream:** O2 exposes saturation/backpressure/degradation evidence; AR-009 stress/spike/failure tests prove behaviour.

## ARC-260 — Material dependency calls have bounded deadlines, one deliberate retry owner/budget and failure-isolation bulkheads

- **Decision source:** AR-008 O1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-149`, `ARQ-PERF-150`, `ARQ-PERF-151`, `ARQ-PERF-166`; cross-reference `ARC-151`, `ARC-161`, `ARC-162`, `ARC-163`
- **Decision:** Every material outbound dependency/workload class uses workload-appropriate bounded deadlines and explicit retry ownership/budgets. Nested layers may not independently multiply retries. Material dependencies/resource classes receive sufficient isolation so one slow/failing provider cannot consume all request, worker, database or other shared capacity.
- **Rationale:** Infinite waits, layered retries and shared unbounded capacity are common causes of retry storms and cascading failure.
- **Rules:**
  1. Deadline/timeout values are explicit per operation/dependency class and evidence-tuned.
  2. One layer owns automatic retry for a given failure path unless a deliberately bounded composed policy proves otherwise.
  3. Only classified retryable failures retry; backoff/jitter and exhaustion behaviour remain bounded.
  4. Bulkheads may use queue/capacity separation, concurrency limits, circuit/degraded controls or equivalent mechanisms.
  5. Cancellation/abandonment propagates where practical when the originating operation is no longer useful/valid.
- **Failure behaviour:** Timeout/retry exhaustion produces explicit failure/degraded/reconciliation state; it never blocks forever or multiplies irreversible effects.
- **Security/privacy:** Retries/logging carry minimum sensitive data and revalidate current authority when execution is delayed.
- **Performance/scaling:** Retry budgets are part of capacity modelling; bulkheads preserve critical headroom during dependency incidents.
- **Enforcement/downstream:** O2 observes latency/timeouts/retries/circuit state; AR-009 tests nested failure, provider slowdown and saturation.

## ARC-261 — PostgreSQL failover preserves one fenced accepted write authority; split-brain writes are forbidden

- **Decision source:** AR-008 O1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-146`, `ARQ-PERF-166`; cross-reference `ARC-060`, `ARC-077`, `ARC-244`
- **Decision:** PostgreSQL failover/recovery must preserve exactly one accepted writable authority using fencing or an equivalently proven mechanism. A former primary that lost authority may not rejoin as writable until safely reconciled. Application conflict handling is not a substitute for preventing split-brain write authority.
- **Rationale:** Two concurrent writable authorities can irreversibly violate financial, entitlement, identity and lifecycle invariants beyond safe application-level reconciliation.
- **Rules:**
  1. Failover tooling/topology must have an explicit promotion/fencing authority.
  2. Stale/former primaries cannot accept writes after authority loss.
  3. Application nodes discover/use the accepted authority through a controlled connection/failover mechanism.
  4. Failover procedures include reconciliation/readiness before the promoted authority serves normal writes.
- **Failure behaviour:** Ambiguous database authority fails closed for writes rather than accepting conflicting primaries.
- **Security/privacy:** Failover access/control is privileged and auditable; restored authority retains deletion/consent/privacy law.
- **Performance/scaling:** Failover objectives and connection recovery are capacity-tested without assuming zero interruption.
- **Enforcement/downstream:** Concrete HA/failover product/topology is proof-gated in AR-008/009; failover drills are mandatory evidence.

## ARC-262 — Rolling deployments require an adjacent-version interoperability window and compatible state evolution

- **Decision source:** AR-008 O1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-155`, `ARQ-PERF-156`; cross-reference `ARC-077`, `ARC-152`, `ARC-166`
- **Decision:** Where rolling deployment is used, adjacent application versions must safely coexist across shared database schema, durable jobs/messages, provider/event contracts and relevant distributed/runtime semantics. Risky/destructive database evolution uses expand → compatible transition → contract or an equivalently proven compatibility strategy.
- **Rationale:** During rollout, old and new nodes may execute simultaneously; a release that is only correct after instant global replacement is not safely rollable.
- **Rules:**
  1. Schema changes are deployed in a compatibility order that preserves both adjacent versions during overlap.
  2. Durable queued payloads/events remain consumable by permitted adjacent versions or are version-gated/migrated safely.
  3. Contract/removal phases occur only after old consumers/writers are proven absent.
  4. Distributed coordination/protocol changes declare mixed-version semantics.
- **Failure behaviour:** Incompatible rollout is blocked/paused; operators use rollback or governed forward recovery rather than allowing mixed-version corruption.
- **Security/privacy:** Compatibility phases may not temporarily weaken policy/field/privacy enforcement.
- **Performance/scaling:** Migration/backfill/dual-write or compatibility work is bounded and monitored to avoid OLTP degradation.
- **Enforcement/downstream:** Release/migration checklists and CI/proof gates enforce compatibility; O2 monitors rollout health; AR-009 exercises representative overlaps.

## ARC-263 — Planned node termination drains new traffic/work first and relies on durable recovery for unfinished obligations

- **Decision source:** AR-008 O1.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-157`, `ARQ-PERF-105`; cross-reference `ARC-165`, `ARC-018`
- **Decision:** Before planned termination for deploy/maintenance, remove or drain the node from new traffic/work, stop acquiring new durable jobs, allow bounded in-flight work to finish where safe, then terminate. Unfinished obligations remain recoverable through their durable/idempotent mechanisms; shutdown never invents completion.
- **Rationale:** Immediate termination increases avoidable failures, while indefinite shutdown blocks deployments and can create operational deadlock.
- **Rules:**
  1. Traffic readiness/draining changes precede process termination.
  2. Worker queue acquisition stops before the grace period where supported.
  3. In-flight grace is bounded and workload-aware.
  4. Work that cannot finish safely is retried/reconciled from durable state after restart/replacement.
- **Failure behaviour:** Grace expiry terminates without marking unfinished work successful; orphan/rescue mechanisms recover durable obligations.
- **Security/privacy:** Draining does not bypass current authorization or expose partial sensitive output.
- **Performance/scaling:** Deployments account for temporary reduced capacity/headroom during drain/replacement.
- **Enforcement/downstream:** Deployment runtime config and runbooks encode drain/grace semantics; O2 monitors drains; AR-009 tests rolling termination under load.

## ARC-264 — Every production change has a pre-deployment rollback path or explicit forward-recovery strategy

- **Decision source:** AR-008 O1.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-158`, `ARQ-PERF-156`; cross-reference `ARC-250`
- **Decision:** Every production release/change must declare an understood recovery path before deployment. Reversible changes may use rollback; irreversible migrations/data transformations require an explicit forward-recovery plan. Recovery assumptions may not depend on restoring state that the release intentionally and irreversibly destroyed.
- **Rationale:** “We can always roll back” is false once schema/data semantics cross an irreversible boundary and can turn an incident into improvisation.
- **Rules:**
  1. Release risk review identifies reversible versus irreversible changes.
  2. Rollback compatibility includes database/job/message/provider state, not only application image version.
  3. Irreversible steps cannot proceed without tested/documented forward-recovery handling proportional to risk.
  4. Historical backup remains disaster recovery, not a substitute for safe release planning.
- **Failure behaviour:** If the planned recovery path becomes invalid during rollout, deployment stops/escalates rather than proceeding on hope.
- **Security/privacy:** Recovery/rollback may not resurrect deleted data or weaken current security/privacy state.
- **Performance/scaling:** Recovery steps are capacity-aware and avoid unbounded repair jobs during incidents.
- **Enforcement/downstream:** Release gate records rollback/forward-recovery evidence; O2 exposes deployment markers/health; AR-009 tests high-risk recovery scenarios.

## ARC-265 — Progressive/canary rollout is a risk-proportional blast-radius control with explicit comparison and stop criteria

- **Decision source:** AR-008 O1.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-159`, `ARQ-PERF-165`
- **Decision:** High-risk production changes should support progressive/canary exposure where it meaningfully reduces blast radius. Rollout stages use defined health/performance/correctness comparison signals and stop/no-go/rollback-or-recovery criteria. Low-risk changes need not incur ceremonial canary complexity without benefit.
- **Rationale:** Progressive exposure can bound unknown production risk, but only when coupled to meaningful evidence and clear action thresholds.
- **Rules:**
  1. Rollout strategy is proportional to change risk and architecture topology.
  2. Canary cohorts/nodes are representative enough for the risk being tested.
  3. Comparison criteria are defined before exposure, not selected after observing results.
  4. Canarying supplements tests/proofs and never authorises known invariant violations.
- **Failure behaviour:** Breached stop criteria pause/reverse/forward-recover according to the release plan; traffic is not expanded while critical signals are ambiguous.
- **Security/privacy:** Progressive rollout may not create inconsistent authorization/privacy semantics between cohorts.
- **Performance/scaling:** Canary evidence includes relevant latency/error/saturation/capacity effects where applicable.
- **Enforcement/downstream:** O2 defines deployment correlation/signals; AR-009 sets workload comparison gates and release proof expectations.

## ARC-266 — Operational emergency controls are named, least-privilege, auditable mechanisms for isolating optional work without weakening core correctness

- **Decision source:** AR-008 O1.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-164`, `ARQ-IAM-004`, `ARQ-IAM-007`; cross-reference `ARC-129`, `ARC-130`, `ARC-131`, `ARC-164`
- **Decision:** Provide explicit authorised/auditable operational controls capable of pausing, throttling or disabling selected low-priority queues, integrations, fan-out or optional capabilities during incidents. These controls are privileged operations governed by AR-004 assurance/least-privilege/audit law and may not weaken authoritative correctness.
- **Rationale:** Operators need fast containment mechanisms during incidents, but ad-hoc SSH/manual database mutation creates unbounded authority and poor evidence.
- **Rules:**
  1. Emergency controls are named operations with known scope/effect/reversal semantics.
  2. Access is role/capability scoped, strongly authenticated where risk requires, and fully auditable.
  3. Controls prefer reducing optional load/dependency pressure before touching critical authority paths.
  4. Activation/deactivation state is visible to operations and relevant health surfaces.
  5. Break-glass remains a separate exceptional path and is not the default incident mechanism.
- **Failure behaviour:** Control failure or ambiguous state is surfaced explicitly; the platform does not assume a queue/provider was paused when it was not.
- **Security/privacy:** Least privilege, strong MFA/step-up, reason capture and audit apply according to AR-004; controls cannot disable required security/privacy checks.
- **Performance/scaling:** Controls are designed to release capacity/bulkhead pressure predictably and are themselves lightweight/available under stress.
- **Enforcement/downstream:** O2 observes control state/effect; incident runbooks name approved controls; AR-009 failure/game-day tests exercise them safely.

**O1 deferrals:** exact availability/SLO percentages and error budgets; health endpoint paths/payloads; concrete supervisor-tree/restart-intensity values; dependency timeout/retry-budget constants; circuit/bulkhead implementation; PostgreSQL HA/failover/fencing product; drain/grace durations; deployment/canary tooling; rollback automation; emergency-control UI/API and exact operator roles remain assigned to O2/AR-009, Operations/JIT configuration, Domain Dossiers where business-specific, and Architectural Proof/release gates.

## 4L.2 Round O2 — Observability, SLO Evidence, Telemetry, Alerting & Incident Correlation

**Accepted answer set:** `O2.1 B, O2.2 B, O2.3 B, O2.4 B, O2.5 B, O2.6 B, O2.7 B, O2.8 B, O2.9 B, O2.10 B, O2.11 B, O2.12 B`

## ARC-267 — Observability is a coherent metrics, traces, structured-logs and domain-signal system; audit/security evidence remains a separate governed class

- **Decision source:** AR-008 O2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-013`, `ARQ-PERF-023`, `ARQ-OPS-001`, `ARQ-IAM-007`
- **Decision:** Operate one coherent observability model composed of metrics, distributed/causal traces, structured diagnostic logs and governed domain/business outcome signals. Audit/security evidence remains a separate immutable/minimised evidence path and is not collapsed into generic observability logs.
- **Rationale:** Infrastructure-only monitoring cannot show whether business outcomes remain correct, while logs alone cannot efficiently represent health, saturation, latency distributions or cross-boundary causality.
- **Rules:**
  1. Metrics answer health/rate/latency/saturation/freshness questions.
  2. Traces diagnose causal path and time distribution across important boundaries.
  3. Structured logs provide bounded contextual diagnostic evidence.
  4. Domain outcome signals expose governed operational state without becoming business authority.
  5. Audit/security evidence follows ARC-131 and its own retention/access rules.
- **Failure behaviour:** Loss of one observability signal class degrades diagnosis/visibility but does not silently redefine business success or audit evidence.
- **Security/privacy:** All observability classes are minimised and access-controlled according to sensitivity; generic telemetry does not duplicate protected payloads.
- **Performance/scaling:** Instrumentation volume and backend cost are bounded through signal design, aggregation and sampling rather than uncontrolled event dumping.
- **Enforcement/downstream:** O3 governs ownership/retention/access; AR-009 defines numerical SLI/SLO and proof thresholds; JIT implementation chooses compatible backends.

## ARC-268 — Platform correlation context propagates across synchronous, durable-async and provider boundaries without using sensitive identity as the tracing key

- **Decision source:** AR-008 O2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-013`, `ARQ-IAM-007`, `ARQ-ASYNC-001`, `ARQ-ASYNC-003`; cross-reference `ARC-149`, `ARC-153`, `ARC-167`
- **Decision:** Propagate a safe platform correlation/causation context across important HTTP/LiveView interactions, Ash actions, database operations, durable jobs, provider calls and callbacks where practical. Correlation identity is distinct from participant identity, business-resource identity and causal actor provenance.
- **Rationale:** Incidents spanning request, job and provider boundaries are otherwise difficult to reconstruct, but using email/user IDs or complete payloads as tracing context leaks sensitive data and couples diagnostics to business identity.
- **Rules:**
  1. Correlation/trace IDs are opaque operational identifiers, not authorization credentials.
  2. Causal initiator and execution actor remain separately represented where material.
  3. Release/environment/node/runtime-role and safe operation/job/provider identities may accompany correlation where useful.
  4. Trace baggage/context excludes secrets, cookies, tokens and unnecessary protected data.
- **Failure behaviour:** Missing correlation weakens diagnostics but cannot block an otherwise valid business action unless the correlation itself is part of separately governed audit evidence.
- **Security/privacy:** Correlation metadata is intentionally non-secret and minimised; protected identity is accessed through governed drill-down rather than embedded broadly in telemetry.
- **Performance/scaling:** Context propagation is bounded and compact.
- **Enforcement/downstream:** Shared observability helpers/adapters implement propagation; O3 defines access/retention; Domain Dossiers may add safe domain operation IDs.

## ARC-269 — Metrics use controlled low-cardinality dimensions; high-cardinality entity identity stays out of metric labels

- **Decision source:** AR-008 O2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-023`, `ARQ-PERF-083`, `ARQ-PERF-107`, `ARQ-IAM-007`
- **Decision:** Metric dimensions/labels are governed for bounded cardinality and privacy. Suitable dimensions include controlled operation class, queue, provider, outcome/error class, runtime role and release/environment; participant IDs, emails, order/payment identifiers, arbitrary URLs and other unbounded identities are not ordinary metric labels.
- **Rationale:** Unbounded cardinality creates telemetry cost/memory/index pressure and leaks sensitive/business identifiers into systems designed for aggregation.
- **Rules:**
  1. Every metric dimension must have a bounded/understood cardinality envelope.
  2. High-cardinality drill-down identity belongs in appropriate trace/log/audit evidence with access controls.
  3. Error labels use governed categories rather than raw exception strings when aggregating.
  4. New labels are reviewed for both scale and privacy.
- **Failure behaviour:** When a useful dimension cannot be represented safely as a metric label, retain aggregate metrics and rely on sampled/contextual trace/log evidence for drill-down.
- **Security/privacy:** Direct identifiers and secrets are prohibited from general metric labels.
- **Performance/scaling:** Cardinality budgets protect telemetry pipelines and queryability at scale.
- **Enforcement/downstream:** Metric-schema conventions and lint/review checks are JIT/AR-009 work.

## ARC-270 — Structured operational logs are diagnostic evidence, not the audit ledger; sensitive payloads are redacted/minimised by design

- **Decision source:** AR-008 O2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-007`, `ARQ-PERF-023`; cross-reference `ARC-131`
- **Decision:** Use structured operational logs for diagnostics and correlation, while material audit/security evidence remains the separate immutable/minimised path defined by AR-004. Generic logs do not serve as authoritative audit history.
- **Rationale:** Operational logs need flexibility and lifecycle controls that differ from governed evidence; mixing them encourages sensitive payload dumping and weakens audit tamper/retention semantics.
- **Rules:**
  1. Logs prefer structured safe fields over interpolated dumps.
  2. Passwords, session/bearer tokens, secrets, payment credentials, cookies and full protected records are never general log content.
  3. Exceptions are normalised/redacted before exporting where necessary.
  4. Audit events are emitted through the dedicated governed evidence path even if a diagnostic log also exists.
- **Failure behaviour:** Logging backend/export failure degrades diagnostics; required audit evidence must still follow its durable policy.
- **Security/privacy:** Log access and retention are sensitivity-aware; logs are not a shadow participant database.
- **Performance/scaling:** Log volume is bounded with levels/sampling/aggregation rather than disabling diagnostic value globally.
- **Enforcement/downstream:** O3 sets retention/access/incident handling; implementation establishes redaction helpers and safe logger metadata.

## ARC-271 — Important boundaries support vendor-neutral distributed tracing with controlled sampling; traces never substitute for zero-tolerance evidence

- **Decision source:** AR-008 O2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-013`, `ARQ-PERF-023`, `ARQ-PERF-024`
- **Decision:** Instrument important application, database, queue and provider boundaries consistently for distributed tracing and use controlled sampling according to traffic, criticality and diagnostic need. OpenTelemetry-compatible propagation/export is the preferred proof direction, while no proprietary APM backend is architecture authority.
- **Rationale:** Cross-boundary traces materially improve latency/failure diagnosis, but retaining every trace indefinitely is costly and traces are observational rather than canonical business evidence.
- **Rules:**
  1. Sampling policy may vary by environment, traffic class, error/anomaly state and diagnostic campaign.
  2. Important low-volume/error traces may be sampled more strongly than routine high-volume success traffic.
  3. Trace absence may not erase a required audit/business invariant.
  4. Instrumentation APIs remain backend-neutral where practical.
- **Failure behaviour:** Tracing/exporter failure degrades diagnosis only and remains isolated under ARC-278.
- **Security/privacy:** Span attributes/baggage follow minimisation/cardinality rules and exclude protected payloads.
- **Performance/scaling:** Sampling and span design bound telemetry overhead.
- **Enforcement/downstream:** JIT selects exporter/collector/backend; AR-009 measures instrumentation overhead and trace completeness on key paths.

## ARC-272 — SLOs use user/business-facing SLIs by capability class while hard correctness invariants remain outside consumable error budgets

- **Decision source:** AR-008 O2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-012`, `ARQ-PERF-013`, `ARQ-PERF-024`, `ARQ-PERF-139`, `ARQ-PERF-140`; cross-reference `ARC-255`
- **Decision:** Each availability/performance class has explicit user/business-facing SLIs and supporting component metrics. Percentiles/distributions are used where appropriate instead of relying on averages alone. Error budgets apply only to approved availability, latency or freshness objectives; zero-tolerance business/security/privacy invariants are separate incident gates.
- **Rationale:** Component uptime can be green while users cannot complete the intended business operation, and average latency hides tail failure.
- **Rules:**
  1. SLI definitions describe the successful user/business outcome and observation window.
  2. Diagnostic metrics explain SLI degradation but do not replace the SLI.
  3. Exact targets/error-budget policies are evidence-gated AR-009 decisions.
  4. Hard invariant breach is not reclassified as acceptable because an SLO remains within budget.
- **Failure behaviour:** SLO breach drives operational/release response according to severity; invariant breach invokes correctness incident/STOP semantics.
- **Security/privacy:** SLI calculation uses minimised aggregated data.
- **Performance/scaling:** SLI computation is efficient and does not create per-user high-cardinality monitoring state by default.
- **Enforcement/downstream:** AR-009 locks numerical targets, tests and release thresholds; O3 governs alert/error-budget ownership.

## ARC-273 — PostgreSQL observability must distinguish query, pool, lock, planner/index, maintenance, replication and resource bottlenecks

- **Decision source:** AR-008 O2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-083`, `ARQ-PERF-073`, `ARQ-PERF-081`, `ARQ-PERF-082`
- **Decision:** PostgreSQL and application DB telemetry must expose enough evidence to distinguish query execution latency from connection/pool queueing, locks/contention, index/planner issues, replication lag where applicable, vacuum/analyze/statistics health, storage/resource pressure and migration impact.
- **Rationale:** A generic “database slow” signal cannot identify whether to fix query shape, indexing, pool economics, lock scope, maintenance or infrastructure.
- **Rules:**
  1. Pool wait/checkout time is observable separately from SQL execution time.
  2. Slow/top query evidence is available without indiscriminately logging sensitive bind values.
  3. Lock/transaction contention and long-running transactions are diagnosable.
  4. Maintenance/replica/storage indicators are captured where the topology uses them.
- **Failure behaviour:** DB telemetry gaps trigger monitoring degradation; they do not alter database authority.
- **Security/privacy:** SQL telemetry avoids exposing sensitive parameters/query payloads unnecessarily.
- **Performance/scaling:** Database observability itself is sampled/aggregated to avoid materially worsening DB load.
- **Enforcement/downstream:** AR-009 defines thresholds/load evidence; operations choose PostgreSQL/hosting telemetry integrations.

## ARC-274 — Material queues and realtime surfaces expose freshness, saturation, retry and amplification evidence sufficient for diagnosis

- **Decision source:** AR-008 O2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-107`, `ARQ-PERF-135`; cross-reference `ARC-160`, `ARC-161`, `ARC-166`
- **Decision:** Material queue observability includes depth, oldest wait age, execution duration, throughput, retries/failures/discards/cancels and downstream resource/dependency saturation. Realtime/LiveView observability includes connection/churn/reconnect behaviour, relevant mount/event/render timing, process/mailbox pressure, subscription/fan-out, broadcast rates/payload sizes and errors.
- **Rationale:** Job counts or websocket connection totals alone do not expose freshness collapse, retry storms, slow clients or fan-out amplification.
- **Rules:**
  1. Freshness/wait age is first-class for time-sensitive queues.
  2. Queue state is correlated with dependency/DB/resource pressure where possible.
  3. Realtime metrics remain bounded and avoid per-connection cardinality explosion.
  4. High-fan-out changes expose enough evidence to identify amplification.
- **Failure behaviour:** Queue/realtime monitoring loss degrades diagnosis while durable queue/business/realtime semantics remain unchanged.
- **Security/privacy:** Payload-size and routing metrics avoid exposing message contents/topic secrets.
- **Performance/scaling:** Collection is aggregation-oriented and compatible with worker-node separation/multi-node LiveView.
- **Enforcement/downstream:** AR-009 load/failure tests validate thresholds; O3 alert/runbook ownership.

## ARC-275 — Important business capabilities expose operational domain outcome signals without moving domain authority into observability queries

- **Decision source:** AR-008 O2.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-001`, `ARQ-PERF-024`; cross-reference `ARC-154`, `ARC-168`, `ARC-221`, `ARC-240`
- **Decision:** Important domains/capabilities expose bounded operational signals representing material unresolved/failing business outcomes (for example reconciliation backlog, unresolved required consequence, deletion workflow backlog, scheduled transition failure or critical provider reconciliation failure). Monitoring reads these governed states; dashboards/alerts do not become authority or encode hidden business law.
- **Rationale:** Green infrastructure can coexist with failed business obligations, while implementing business semantics only in monitoring queries creates unreviewed shadow law.
- **Rules:**
  1. Domain signal semantics originate from owning application/domain contracts.
  2. Signals are aggregated/minimised enough for operations.
  3. Monitoring may drill into governed records through authorised workflows rather than copy protected payloads.
  4. Domain signal absence/failure is itself observable where material.
- **Failure behaviour:** Monitoring failure does not resolve or mutate the underlying domain obligation.
- **Security/privacy:** Domain metrics avoid protected detail; authorised diagnostic drill-down is separate.
- **Performance/scaling:** Prefer derived counts/age/state-class signals over expensive ad-hoc full-domain scans.
- **Enforcement/downstream:** Domain Map/Dossiers define concrete signals; O3 owns response; AR-009 defines thresholds/proof.

## ARC-276 — Material alerts are actionable, severity-governed and explicitly owned; noisy correlated symptoms are grouped instead of paging everyone

- **Decision source:** AR-008 O2.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-001`, `ARQ-PERF-163`, `ARQ-PERF-165`
- **Decision:** Material alerts/pages have an explicit severity, owning role/team, affected capability/SLO/invariant, useful evidence/context and response/runbook/escalation path. Prefer alerts tied to user/business impact, saturation or invariant threat over indiscriminate low-level exceptions, and group/deduplicate correlated failures where possible.
- **Rationale:** Alert volume without ownership/actionability produces fatigue and slows incident response; one provider outage should not become hundreds of independent pages.
- **Rules:**
  1. Paging alerts require a defined human action or escalation.
  2. Informational diagnostics may remain dashboards/logs instead of paging.
  3. Alert thresholds and severity map are reviewed with SLO/error-budget/invariant semantics.
  4. Correlation/suppression never hides a distinct critical invariant breach.
- **Failure behaviour:** Alert-delivery failure is itself operationally visible through an independent path appropriate to risk.
- **Security/privacy:** Alert payloads are minimised; sensitive diagnostics require authorised drill-down rather than broad message disclosure.
- **Performance/scaling:** Alert aggregation/dedup protects operators and downstream notification systems during storms.
- **Enforcement/downstream:** O3 defines incident ownership/severity/runbooks and alert-channel resilience; AR-009 locks numerical criteria.

## ARC-277 — Release, configuration and incident timelines are correlated with runtime evidence, and significant incidents feed explicit amendment/re-proof

- **Decision source:** AR-008 O2.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-159`, `ARQ-PERF-165`, `ARQ-OPS-001`; cross-reference `ARC-265`
- **Decision:** Operational evidence includes safe release/deployment-stage, environment, node/runtime-role and relevant configuration-generation/experiment-feature version markers so behaviour changes can be correlated with rollout/configuration events. Material incidents retain an evidence-backed timeline and feed explicit Architecture/test/capacity/runbook amendment when evidence contradicts existing assumptions.
- **Rationale:** Without change correlation, operators waste time discovering what changed, and incident lessons disappear into prose instead of correcting governing assumptions.
- **Rules:**
  1. Deployment/canary markers are queryable alongside relevant SLIs/diagnostics.
  2. Secret values are never recorded as configuration correlation data.
  3. Incident timelines distinguish observation, hypothesis, containment and confirmed cause.
  4. Contradicted Product/ARQ/ARC/Domain/Feature-Pack assumptions trigger STOP and explicit upstream amendment/re-proof.
- **Failure behaviour:** Missing rollout marker is an observability defect, not permission to continue an ambiguous high-risk rollout.
- **Security/privacy:** Correlation metadata stores versions/generations/hashes where safe, never secret material.
- **Performance/scaling:** Release markers are low-volume metadata correlated by backend, not per-request large payloads.
- **Enforcement/downstream:** O3 establishes incident/release evidence workflow; governance-wide amendment discipline applies.

## ARC-278 — Observability is failure-isolated from business authority; telemetry handlers/exporters remain lightweight, bounded and non-blocking

- **Decision source:** AR-008 O2.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-145`, `ARQ-PERF-151`, `ARQ-PERF-166`, `ARQ-IAM-007`; cross-reference `ARC-267`
- **Decision:** Ordinary metrics/log/trace exporter or observability-backend failure degrades visibility rather than blocking valid payment, entitlement, authentication, consent, safety or other authoritative operations. Local instrumentation/handlers are lightweight and bounded; expensive exporting/processing occurs off the emitting critical path. Durable audit/security/business-required evidence remains separately governed and cannot be silently downgraded to best-effort telemetry.
- **Rationale:** Observability should help detect incidents, not become a new synchronous dependency capable of causing them.
- **Rules:**
  1. Telemetry handlers do no slow external I/O on emitting processes.
  2. Export buffering is bounded and may drop ordinary telemetry according to policy under overload rather than exhausting business capacity.
  3. Observability backend health is itself monitored where practical but not a universal readiness dependency.
  4. Required audit/security evidence follows its own durable path.
- **Failure behaviour:** Exporter/backend outage produces explicit monitoring degradation/backlog/drop evidence while business flows remain operational where otherwise safe.
- **Security/privacy:** Local buffering/export honours retention/redaction/access controls.
- **Performance/scaling:** Instrumentation overhead is measured and constrained; telemetry cannot consume unbounded memory/CPU/network.
- **Enforcement/downstream:** O3 defines telemetry retention/access/degraded operations; AR-009 performance tests include instrumentation overhead/failure.

**O2 deferrals:** exact observability backend/vendor, OpenTelemetry exporter/collector deployment, metric/tracing libraries beyond preferred proof direction, SLI/SLO numerical values, alert thresholds/channels/on-call schedule, telemetry sampling rates, metric-cardinality budgets, log/trace/metric retention, dashboard layout, incident-severity vocabulary and ownership roster remain assigned to O3/AR-009, Operations/JIT configuration and release evidence.


## 4L.3 Round O3 — Incident Command, Operational Proof, Release Gates, Configuration & Telemetry Governance

**Accepted answer set:** `O3.1 B, O3.2 B, O3.3 B, O3.4 B, O3.5 B, O3.6 B, O3.7 B, O3.8 B, O3.9 B, O3.10 B, O3.11 B, O3.12 B`

## ARC-279 — Material incident severity is governed by impact and risk, not technical novelty or exception volume

- **Decision source:** AR-008 O3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-001`, `ARQ-PERF-165`, `ARQ-PERF-166`
- **Decision:** Define a governed material-incident severity model whose primary inputs are user/business impact, affected criticality class, financial/entitlement impact, safety/privacy/security implications, data-integrity uncertainty, duration, scope/blast radius and recovery difficulty. Exact labels and thresholds remain Operations/AR-009 evidence inputs.
- **Rationale:** A technically dramatic infrastructure event may be low business impact, while a subtle privacy, safety, entitlement or accounting correctness failure may require immediate high-severity response.
- **Rules:**
  1. Severity is based on impact/risk evidence rather than number of logs/exceptions alone.
  2. Hard-invariant uncertainty may elevate severity even before final root cause is known.
  3. Severity may change as evidence develops, with the change recorded in the incident timeline.
  4. Exact `SEV-*` names and numerical thresholds are not frozen by this ARC.
- **Failure behaviour:** When impact is uncertain on a hard-invariant path, response errs toward containment/escalation until evidence establishes a lower-risk state.
- **Security/privacy:** Security/privacy incidents are classified on exposure/risk and integrity impact, not merely application availability.
- **Performance/scaling:** Large traffic volume is relevant only insofar as it changes blast radius, saturation or user/business impact.
- **Enforcement/downstream:** Operations/JIT defines the severity vocabulary and contact roster; AR-009 defines measurable thresholds where appropriate.

## ARC-280 — Every material incident has one named coordination owner while specialist authorities retain their own non-waivable decision rights

- **Decision source:** AR-008 O3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-001`, `ARQ-IAM-004`, `ARQ-IAM-008`
- **Decision:** Assign a single named incident commander/owner for coordination of each material incident. Specialist authorities such as security, privacy/legal, clinical/safety, finance/commerce or product retain their governed decision rights; incident command coordinates but does not manufacture authority or waive another authority's blocker.
- **Rationale:** Collective ownership produces ambiguity during time pressure, while a technically senior responder should not become an unlimited cross-functional authority.
- **Rules:**
  1. Incident command owns coordination, priorities, timeline and communication cadence.
  2. Technical lead, communications/scribe and specialist-authority roles may be distinct people.
  3. Break-glass or privileged actions still follow ARC-130/AR-004 governance.
  4. A required authority's no-go/containment requirement cannot be overruled by convenience.
- **Failure behaviour:** If the incident owner becomes unavailable, ownership is explicitly transferred rather than silently becoming collective.
- **Security/privacy:** Privileged incident actions remain named, scoped, auditable and least-privilege.
- **Performance/scaling:** Clear command reduces duplicated or conflicting remediation during large incidents.
- **Enforcement/downstream:** Operations runbooks define role assignment/transfer and contact paths; final organisational roster remains outside Architecture Law.

## ARC-281 — Safe containment precedes perfect diagnosis when material impact is ongoing, using authorised controls that preserve evidence and authority

- **Decision source:** AR-008 O3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-164`, `ARQ-PERF-166`, `ARQ-OPS-001`, `ARQ-IAM-008`; cross-reference `ARC-266`
- **Decision:** When material impact is active, prefer safe bounded containment before waiting for complete root-cause certainty. Approved containment may pause optional queues/integrations, stop a rollout, isolate a provider, disable an affected non-critical capability, revoke compromised authority or enter a governed degraded mode, while preserving evidence and authoritative state.
- **Rationale:** Continuing damage while pursuing perfect diagnosis is unsafe, but arbitrary destructive intervention can worsen incidents or destroy evidence.
- **Rules:**
  1. Containment controls are named, authorised and auditable.
  2. Containment never fabricates successful business outcomes.
  3. Hard correctness/security/privacy policy remains enforced in degraded modes.
  4. Destructive/manual data mutation requires separately governed authority and evidence.
- **Failure behaviour:** If safe containment is unavailable, escalate severity/ownership and stop affected operations rather than improvise unbounded state changes.
- **Security/privacy:** Compromise containment may revoke sessions/devices and freeze sensitive actions under ARC-139.
- **Performance/scaling:** Containment may deliberately sacrifice optional freshness/throughput to protect critical capacity and truth.
- **Enforcement/downstream:** Emergency-control inventory/runbooks are Operations/JIT artifacts and are exercised under ARC-285.

## ARC-282 — Material runbooks are owned, versioned, evidence-bearing procedures with explicit entry, stop, success and escalation conditions

- **Decision source:** AR-008 O3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-163`, `ARQ-OPS-001`
- **Decision:** Treat material runbooks as governed operational procedures, not passive documentation. Each runbook identifies ownership, applicability/entry conditions, authority prerequisites, steps, stop/escalation conditions, success verification and recovery/fallback. Confidence requires exercised or incident-derived evidence.
- **Rationale:** A stale wiki page that has never been exercised is not reliable recovery capability.
- **Rules:**
  1. Runbooks are versioned and linked to the capability/failure they govern.
  2. Material changes to architecture/provider/configuration trigger runbook review where applicable.
  3. Exercises/incidents record runbook version and outcome.
  4. A failed runbook exercise creates remediation work rather than being silently accepted.
- **Failure behaviour:** If the documented path proves unsafe or invalid, stop, contain, escalate and amend before relying on it again.
- **Security/privacy:** Runbooks do not embed secrets; privileged steps identify the authority required.
- **Performance/scaling:** Procedures consider load, timeouts, concurrency and recovery pressure where material.
- **Enforcement/downstream:** AR-009/release gates require exercised evidence for applicable critical paths.

## ARC-283 — Material post-incident review is factual, evidence-based and feeds explicit upstream amendment/re-proof when governing assumptions fail

- **Decision source:** AR-008 O3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-165`, `ARQ-OPS-001`
- **Decision:** Material incidents produce a post-incident record covering impact, timeline, detection, containment, contributing/root causes, recovery, what succeeded/failed and assigned follow-up actions. Where evidence contradicts Product Law, an ARQ/ARC, Domain Law, a Feature Pack premise, capacity assumption, test, alert or runbook, apply STOP → classify → explicitly amend the correct upstream layer → re-prove affected flows before normal execution resumes.
- **Rationale:** Restoring service without correcting failed assumptions creates repeat incidents and silent architectural drift.
- **Rules:**
  1. Separate observed facts, hypotheses and confirmed causes.
  2. Follow-ups have owners and completion criteria.
  3. Human/process accountability may be addressed where relevant, but technical analysis focuses on system/process correction rather than blame.
  4. Architecture amendments preserve prior history through explicit supersession/amendment.
- **Failure behaviour:** Unresolved material correctness uncertainty remains an open incident/release blocker.
- **Security/privacy:** Post-incident artifacts are access-controlled/minimised when they contain sensitive security/privacy detail.
- **Performance/scaling:** Capacity and latency incidents update workload assumptions and AR-009 proof plans.
- **Enforcement/downstream:** Governance-wide; closure evidence feeds Architecture Law, Domain/Dossier, test and release artifacts as appropriate.

## ARC-284 — Release/pilot progression uses an evidence-bearing cross-functional gate manifest; any applicable unresolved mandatory gate is a no-go

- **Decision source:** AR-008 O3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-001`, `ARQ-PERF-153`, `ARQ-PERF-156`, `ARQ-PERF-158`, `ARQ-PERF-159`
- **Decision:** Every material release/pilot stage has an explicit gate manifest identifying applicable authorities, required evidence and pass/no-go state. Depending on scope, gates may include engineering/operations, clinical/safety, content, commerce/finance, privacy/legal, security and product. A mandatory unresolved gate is a no-go for the affected stage and cannot be waived by success in another discipline.
- **Rationale:** Production readiness is cross-functional; a technically green build is not releasable if a required privacy, safety or commercial control remains unproved.
- **Rules:**
  1. Gates are explicit and evidence-linked.
  2. `Not applicable` requires justified classification rather than omission.
  3. Gate ownership remains with the competent authority.
  4. Progressive rollout/canary does not waive preconditions; it limits blast radius after prerequisites pass.
- **Failure behaviour:** Missing/failed mandatory evidence stops progression until resolved or the governing requirement is explicitly amended by the proper authority.
- **Security/privacy:** Security/privacy gates remain independent no-go authorities where applicable.
- **Performance/scaling:** AR-009 supplies load/capacity/performance evidence into the manifest.
- **Enforcement/downstream:** Feature Pack skeleton/gate manifest and release workflow consume this ARC.

## ARC-285 — Failure injection follows a maturity ladder from deterministic tests to controlled production game days, with blast radius proportional to operational maturity

- **Decision source:** AR-008 O3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-162`, `ARQ-PERF-153`, `ARQ-PERF-163`
- **Decision:** Exercise expected failure modes progressively: deterministic/local tests → representative integration/staging failures → Architectural Proof/pre-release scenarios → carefully controlled production game days only when maturity, containment and observability justify them.
- **Rationale:** Untested failure paths are speculation, while premature production chaos testing can create avoidable harm.
- **Rules:**
  1. Test scenarios derive from actual architecture and risk, including node death, dependency loss/slowness, queue backlog, Redis loss where used, database failover, reconnect storms, object/provider loss and recovery.
  2. Exercises define expected safe/degraded behaviour and pass/fail criteria in advance.
  3. Production exercises require explicit authority, containment and rollback/recovery.
  4. Exercise findings amend tests/runbooks/architecture where evidence demands.
- **Failure behaviour:** An exercise that breaches a hard invariant fails regardless of availability metrics.
- **Security/privacy:** Synthetic/test data is preferred; production exercises avoid unnecessary sensitive-data exposure.
- **Performance/scaling:** AR-009 combines failure injection with load/stress scenarios where required.
- **Enforcement/downstream:** Architectural Proof, hardening and release gates schedule/record applicable exercises.

## ARC-286 — Recovery exercises must prove the complete recoverable service boundary and semantic promotion criteria, not merely database-byte restoration

- **Decision source:** AR-008 O3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-002`, `ARQ-PERF-147`, `ARQ-PERF-148`, `ARQ-PERF-163`, `ARQ-STATE-006`; cross-reference `ARC-243` through `ARC-250`
- **Decision:** Recovery exercises prove restoration of the complete minimum service-authority set required by AR-007, including database/PITR, required object state, runtime configuration, recoverable secrets/key material, deletion/withdrawal suppression and other critical configuration/provider references, followed by replay/reconciliation and semantic verification before service promotion.
- **Rationale:** A backup job or database restore is not disaster-recovery proof if the resulting platform cannot safely resume service.
- **Rules:**
  1. Recovery remains gated until semantic verification passes.
  2. Restore evidence records source point, recovered classes, replay/reconciliation and verification outcome.
  3. Deletion/withdrawal truth is replayed before normal service resumes.
  4. Exact RPO/RTO values remain class-specific AR-009/operations evidence inputs.
- **Failure behaviour:** Failed restore/reconciliation/verification leaves the environment non-ready and triggers remediation/escalation.
- **Security/privacy:** Recovery secrets and restored sensitive state retain production-grade access controls; deleted identities may not reappear.
- **Performance/scaling:** Exercises measure recovery duration/resource demands against approved objectives.
- **Enforcement/downstream:** Release/DR gates require periodic exercised evidence appropriate to criticality.

## ARC-287 — Runtime configuration is centralised, validated and readiness-gated rather than interpreted ad hoc throughout business code

- **Decision source:** AR-008 O3.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-144`, `ARQ-PERF-154`, `ARQ-OPS-002`; cross-reference `ARC-017`
- **Decision:** Environment-specific runtime values enter through a controlled application/configuration boundary, are parsed/validated into explicit configuration and are consumed by application/business code through that governed boundary. Missing/invalid mandatory configuration prevents safe readiness; immutable release artifacts remain environment-neutral.
- **Rationale:** Scattered raw environment reads create inconsistent validation, hidden runtime dependencies and deployment drift.
- **Rules:**
  1. Mandatory configuration is validated before readiness.
  2. Optional/capability configuration has explicit degraded/disabled semantics.
  3. Release images do not bake environment-specific secrets/credentials.
  4. Health/config diagnostics expose safe metadata only.
- **Failure behaviour:** Invalid mandatory configuration fails startup/readiness clearly rather than causing delayed undefined behaviour.
- **Security/privacy:** Sensitive values use the secret-class controls in ARC-288.
- **Performance/scaling:** Configuration access is bounded/local after validation and not dependent on per-request remote lookups by default.
- **Enforcement/downstream:** Exact ConfigProvider/secret-manager/hosting integration remains JIT/provider proof.

## ARC-288 — Secrets are a distinct sensitive configuration class with least-privilege access, non-disclosure, rotation/revocation support and recoverability

- **Decision source:** AR-008 O3.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-OPS-002`, `ARQ-IAM-004`, `ARQ-IAM-007`; cross-reference `ARC-017`, `ARC-137`
- **Decision:** Treat secrets/credentials/key material separately from ordinary configuration. They are never committed to source, baked into OCI/release images, emitted in logs/traces/health endpoints or duplicated into general configuration evidence. Access is environment-specific and least-privilege; recovery, rotation and revocation are operationally supported. Architecture does not require a specific secret-manager vendor or universal live reload.
- **Rationale:** Secret sprawl turns operational convenience into a security and disaster-recovery weakness.
- **Rules:**
  1. Secret references/versions may be observable where safe; secret values are not.
  2. Controlled rolling restart/deployment is acceptable for rotation where service correctness/availability is preserved.
  3. Higher-risk compromise may require accelerated rotation/revocation.
  4. Recoverability is proved without storing secret plaintext in runbooks/backups outside the approved secret path.
- **Failure behaviour:** Missing/revoked mandatory secrets prevent the affected capability/readiness rather than falling back to insecure defaults.
- **Security/privacy:** Secret access/change is privileged and appropriately auditable without logging the value.
- **Performance/scaling:** Secret resolution strategy avoids high-frequency remote secret-manager calls on hot paths unless specifically justified.
- **Enforcement/downstream:** Secret manager/product, rotation cadence and access implementation remain Operations/JIT evidence decisions.

## ARC-289 — Material configuration changes are code-adjacent governed releases with validation, provenance and rollback/forward-recovery semantics

- **Decision source:** AR-008 O3.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-155`, `ARQ-PERF-158`, `ARQ-PERF-159`, `ARQ-OPS-001`; cross-reference `ARC-277`, `ARC-287`
- **Decision:** Treat material configuration/provider/infrastructure policy changes as governed release events. Validate them before activation, restrict mutation authority, correlate a safe configuration generation/version with telemetry, retain appropriate change evidence and define rollback or forward recovery. Risk-appropriate progressive rollout may apply to high-risk configuration changes.
- **Rationale:** “No code changed” is not a valid exemption from change control when configuration can alter security, routing, capacity or business availability.
- **Rules:**
  1. Material configuration has explicit ownership and review/activation path.
  2. Configuration correlation records version/generation, not secret values.
  3. Emergency controls are named mechanisms, not arbitrary undocumented config edits.
  4. Irreversible changes require explicit forward recovery.
- **Failure behaviour:** Invalid/regressive configuration is rolled back or forward-recovered according to the predeclared plan; ambiguous high-risk state stops progression.
- **Security/privacy:** Mutation rights are least-privilege and auditable.
- **Performance/scaling:** Capacity/routing/concurrency config changes are validated against AR-009 evidence where applicable.
- **Enforcement/downstream:** Release gate manifest and observability timelines include material configuration changes.

## ARC-290 — Observability classes have purpose/sensitivity-specific retention and access; minimise collection before relying on redaction

- **Decision source:** AR-008 O3.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-IAM-007`, `ARQ-PERF-023`, `ARQ-OPS-001`; cross-reference `ARC-270`, `ARC-271`, `ARC-278`
- **Decision:** Define separate retention/access policy classes for metrics, traces, diagnostic logs and audit/security evidence according to purpose, sensitivity and operational value. Prefer not collecting sensitive telemetry in the first place; redaction/filtering is defence in depth. Exact durations are privacy/security/operations inputs, not Architecture-invented constants.
- **Rationale:** Keeping every diagnostic forever expands privacy/security exposure and cost, while deleting all operational evidence destroys incident/reliability learning.
- **Rules:**
  1. Aggregated metrics may have different retention from detailed trace/log data.
  2. Potentially sensitive diagnostic telemetry receives stricter access and justified retention.
  3. Audit/security evidence remains under its separate immutable/minimised retention law.
  4. Telemetry access is least-privilege and appropriate access itself may be auditable.
  5. Retention/deletion propagates to buffers/exporters/backends under the applicable policy where controllable.
- **Failure behaviour:** Retention/export backend failure is visible and does not silently expand retention or block authoritative flows.
- **Security/privacy:** Secrets, credentials and full sensitive payloads are prohibited from generic telemetry.
- **Performance/scaling:** Sampling/aggregation/retention control telemetry volume without losing required SLI or incident evidence.
- **Enforcement/downstream:** Operations/JIT assigns exact periods, roles and backend controls; AR-009 proves observability overhead/retention-scale assumptions.

**O3 deferrals:** exact incident-severity labels/thresholds, on-call roster, alert channels, runbook inventory/tooling, release-gate workflow tool, secret manager/provider, rotation cadence, configuration-management implementation, backup product, recovery schedule, game-day schedule, telemetry backend/exporter/collector, telemetry access roles and retention durations remain Operations/JIT/AR-009 evidence decisions.

## 4L.4 AR-008 Closure Audit — Reliability, Deployment, Operations & Observability

**Audit status:** PASS — AR-008 COMPLETE.

The final routing audit mechanically reproduced **321 frozen ARQs whose `Primary downstream workstreams` include AR-008**:

- Performance: **115**
- Analytics: **184**
- Payments: **1**
- IAM: **5**
- State: **6**
- Async: **3**
- Content: **3**
- Security: **2**
- Operations: **2**
- **TOTAL: 321**

### Closure coverage findings

1. **Failure containment, availability classes and overload:** AR-001/AR-003/AR-005 foundations plus `ARC-255`–`ARC-266` establish capability-specific availability, readiness/liveness, dependency isolation, bounded supervision, backpressure/load shedding, retry ownership, fenced write authority, mixed-version deployment, draining, rollback/forward recovery, progressive rollout and governed emergency controls.
2. **Observability and operational diagnosis:** `ARC-267`–`ARC-278` establish metrics/traces/structured diagnostics/domain-outcome signals, safe correlation, telemetry privacy/cardinality, SLI/SLO evidence, PostgreSQL/queue/realtime observability, owned alerting, deployment correlation and failure-isolated telemetry.
3. **Incident/release/recovery governance:** `ARC-279`–`ARC-290` establish impact-based severity, named incident command, containment, exercised runbooks, post-incident amendment/re-proof, cross-functional no-go gates, failure-injection maturity, full-service recovery proof, validated runtime configuration/secrets, governed configuration change and telemetry retention/access.
4. **Analytics-heavy AR-008 routing:** The 184 Analytics ARQs do not require a second analytics architecture inside AR-008. Their authoritative event/replay/privacy/experiment semantics are already closed by AR-003/004/005/006/007; AR-008 supplies their operational observability, failure, recovery, release and incident mechanisms.
5. **Security/abuse/upload operations:** `ARQ-SEC-001` is already semantically closed by AR-004 abuse/recovery law (`ARC-144`–`ARC-145`) plus AR-008 distributed readiness/bulkhead/emergency/incident controls; exact thresholds remain AR-009/JIT evidence. `ARQ-SEC-002` is already semantically closed by AR-003 quarantine/storage law and AR-006 governed media/provider law, with AR-008 supplying operational failure/recovery/release controls; scanner product and exact limits remain JIT/provider evidence, not an Architecture-law gap.
6. **Deletion/backup/recovery:** AR-007 (`ARC-233`–`ARC-254`) owns privacy lifecycle and deletion-safe restore semantics; AR-008 adds exercised full-runtime recovery, incident ownership and release proof without duplicating that authority.
7. **No new Product Law needed:** The audit found no contradiction requiring Product Law, DEC, OQ or ARQ amendment and no residual AR-008 mechanism requiring an O4 round.

### AR-008 closure result

- Product Law change: **NO**
- ARQ amendment: **NO**
- New O4 round: **NO**
- Contradiction discovered: **NO**
- AR-008 status: **COMPLETE**
- Accepted AR-008 Architecture Law: `ARC-255` through `ARC-290`
- Next Architecture Decision workstream: **AR-009 — Performance, Scaling & Multi-Node Behaviour**

**AR-008 closure boundary:** Numerical SLOs/latency targets, concrete capacity limits, workload envelopes, performance/load/failure acceptance thresholds, exact distributed-rate limits, telemetry-overhead budgets and proof matrices remain AR-009/evidence work. Exact vendors/products/operational rosters/retention durations remain provider/JIT/Operations decisions unless later evidence requires an explicit Architecture amendment.



# 4M. AR-009 — Performance, Scaling & Multi-Node Behaviour

## 4M.1 Round V1 — Workload Model, Performance Budgets & Verification Regime

**Accepted answer set:** `V1.1 B, V1.2 B, V1.3 B, V1.4 B, V1.5 B, V1.6 B, V1.7 B, V1.8 B, V1.9 B, V1.10 B, V1.11 B, V1.12 B`

## ARC-291 — Scale verification is reference-flow and workload specific; the 100,000-user objective is not a fictional per-endpoint simultaneous-request requirement

- **Decision source:** AR-009 V1.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-001`, `ARQ-PERF-003`, `ARQ-PERF-008`
- **Decision:** Performance/capacity verification models concurrency per reference flow and workload class. The architecture must retain a credible path to approximately 100,000 simultaneously active/connected users where relevant, while each operation receives its own realistic arrival rate, concurrent-operation count, connection count and burst shape rather than inheriting a universal 100,000-simultaneous-request assumption.
- **Rationale:** Active users, connected sessions and simultaneous authoritative mutations are different load dimensions. Collapsing them into one number creates meaningless tests and encourages the wrong scaling work.
- **Rules:**
  1. Every material reference flow declares the relevant concurrency dimensions before major proof.
  2. Connected-user scale, request rate, authoritative-write rate, provider-bound concurrency and background work are modelled separately where material.
  3. Multi-node correctness remains mandatory even when a particular load test runs on one application node.
  4. Workload assumptions are versioned evidence and may be tightened when production evidence justifies it.
- **Failure behaviour:** A test that cannot state what its virtual users/connections/arrival rate represent is not accepted as scale proof.
- **Security/privacy:** Load generation uses synthetic/minimised data and may not weaken security or privacy invariants for throughput.
- **Performance/scaling:** Capacity conclusions are attached to the tested reference flow and workload, not extrapolated blindly to the whole platform.
- **Enforcement/downstream:** FLOW pressure tests, Feature Pack gate manifests and Architectural Proof consume this model.

## ARC-292 — The platform maintains distinct governed workload profiles rather than one generic benchmark

- **Decision source:** AR-009 V1.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-003`, `ARQ-PERF-004`, `ARQ-PERF-005`, `ARQ-PERF-010`
- **Decision:** Performance validation maintains at least the frozen workload families where relevant: ordinary sustained authenticated use; campaign/login bursts; scheduled programme/content releases; scarce-inventory flash sales; and abusive/bot/accidental-retry pressure. Feature Packs may add specialised workload profiles but may not erase platform workload classes that materially affect them.
- **Rationale:** Different traffic shapes stress different bottlenecks: connection lifetime, write contention, provider concurrency, queue fan-out, database pools, cache behaviour and admission controls.
- **Rules:**
  1. Each workload profile defines traffic shape, ramp/burst pattern, relevant read/write mix and expected degraded behaviour.
  2. Flash-sale/scarce-inventory tests assert correctness under contention, not merely response time.
  3. Abuse/retry profiles verify bounded admission and idempotency rather than benchmarking unsafe acceptance.
  4. Scheduled-release profiles distinguish business-effective time from downstream fan-out completion.
- **Failure behaviour:** Unsupported overload must fail safely through the governed throttling/degradation/refusal hierarchy.
- **Security/privacy:** Abuse tests do not disable security controls merely to reach higher throughput.
- **Performance/scaling:** Results are reported per workload profile with no claim that one scenario represents all platform traffic.
- **Enforcement/downstream:** AR-009 V2/V3 and FLOW tests refine exact envelopes and thresholds.

## ARC-293 — Important latency budgets are percentile-based; averages are diagnostic only

- **Decision source:** AR-009 V1.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-011`, `ARQ-PERF-024`
- **Decision:** Important/common latency SLIs and performance gates use percentile distributions such as p50 plus appropriate p90/p95/p99 tail measures. Mean/average latency may be retained for diagnostics but is never the sole acceptance measure.
- **Rationale:** Tail latency is operationally and experientially significant and is hidden by averages.
- **Rules:**
  1. Percentile selection is appropriate to traffic volume and criticality.
  2. Tail regressions can fail a gate even when the mean remains stable.
  3. Percentiles are evaluated over representative windows/workloads rather than tiny samples.
- **Failure behaviour:** Insufficient sample quality or invalid percentile computation invalidates the proof rather than yielding a pass.
- **Security/privacy:** No sensitive participant identifiers are required as metric dimensions.
- **Performance/scaling:** Percentile evidence is correlated with throughput/concurrency/saturation so latency cannot be interpreted in isolation.
- **Enforcement/downstream:** Performance budgets and gate manifests identify the percentile thresholds they enforce.

## ARC-294 — Initial server-side latency classes are semantic, explicit and tighten-with-evidence rather than universal sub-100ms promises

- **Decision source:** AR-009 V1.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-012`, `ARQ-PERF-016`, `ARQ-PERF-017`, `ARQ-PERF-020`
- **Decision:** Adopt the frozen provisional latency classes as initial Architecture budgets: suitable hot/common interactive actions aim for at least p90 <= 100 ms and p99 <= 400 ms server-side; normal durable interactions aim for p95 <= 500 ms and p99 <= 1 s; provider-bound checkout/payment retains end-to-end p99 <= 5 s where provider latency permits while internal platform contribution is measured separately. Async/fan-out work uses freshness/completion budgets rather than pretending to be synchronous HTTP latency.
- **Rationale:** Action semantics and external dependencies determine meaningful latency budgets; a universal sub-100ms target would either be fictitious or distort architecture.
- **Rules:**
  1. These are initial governing ceilings/targets, not entitlements to consume the whole budget.
  2. Faster proven baselines should not quietly regress merely because they remain under the ceiling.
  3. Weakening a governing budget requires explicit evidence and Architecture amendment, not local threshold drift.
  4. Domain/Feature Pack proof may define stricter path-specific budgets.
- **Failure behaviour:** Material unexplained regression beyond an approved budget is a failed gate.
- **Security/privacy:** Correctness/security/privacy work is not skipped to meet latency.
- **Performance/scaling:** Internal platform and provider contributions are decomposed so capacity tuning targets the correct layer.
- **Enforcement/downstream:** FLOW/Feature Pack proofs bind concrete actions to these or stricter classes.

## ARC-295 — Current official “good” Core Web Vitals are the minimum frontend/user-experience floor where applicable, with an aim to outperform them

- **Decision source:** AR-009 V1.5
- **Status:** ACCEPTED_WITH_FUTURE-PROOFING
- **Source ARQs:** `ARQ-PERF-014`, `ARQ-PERF-015`, `ARQ-PERF-020`
- **Decision:** Applicable public/participant-facing web experiences must meet at least the then-current official “good” Core Web Vitals thresholds using the appropriate user-centric/field methodology, and the project aims to outperform that floor wherever reasonably achievable. The frozen baseline when this law was locked is LCP <= 2.5 s, INP <= 200 ms and CLS <= 0.1 at the 75th percentile, evaluated appropriately across mobile and desktop.
- **Rationale:** Server latency alone does not capture user-perceived responsiveness/layout stability, especially for LiveView/browser/network paths.
- **Rules:**
  1. Current official definitions are revalidated when release gates are executed.
  2. External definitions may only tighten or update the project floor; they do not justify silent weakening.
  3. Lab/synthetic measurements help diagnose and gate regressions but do not substitute for appropriate field evidence once available.
  4. LiveView interaction timing remains decomposed alongside browser UX metrics.
- **Failure behaviour:** Sustained performance below the applicable “good” range is treated as a regression requiring remediation or explicit upstream exception, not accepted steady state.
- **Security/privacy:** Field telemetry uses privacy-safe aggregation and collection rules.
- **Performance/scaling:** Mobile/desktop/network/device distributions are considered where material.
- **Enforcement/downstream:** AR-009 proof matrices and release gates incorporate the then-current official threshold evidence.

## ARC-296 — Performance evidence separates user end-to-end latency from internal platform and external-provider contribution

- **Decision source:** AR-009 V1.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-013`, `ARQ-PERF-016`, `ARQ-PERF-023`; cross-reference `ARC-268`, `ARC-273`
- **Decision:** Measure both end-to-end/user-perceived latency and the internal-versus-external contribution for provider-bound or distributed flows. Provider delay remains part of the experience, while platform processing, database/pool time, queue time, network/client effects and external provider time remain separable for diagnosis and SLO interpretation.
- **Rationale:** A single end-to-end number cannot identify which authority or dependency requires remediation.
- **Rules:**
  1. Correlation/tracing context is reused where practical.
  2. Provider latency is never erased from product-quality reporting simply because it is external.
  3. Internal budget compliance does not automatically imply acceptable end-to-end experience.
- **Failure behaviour:** Missing decomposition on a material provider-bound proof yields incomplete diagnostic evidence rather than a false platform pass/fail conclusion.
- **Security/privacy:** Correlation uses safe identifiers/metadata rather than raw sensitive payloads.
- **Performance/scaling:** Provider saturation and platform saturation are measured independently where possible.
- **Enforcement/downstream:** Provider-bound FLOW tests declare both internal and end-to-end budgets.

## ARC-297 — Material unexplained performance regressions are failed acceptance criteria for affected slices and Feature Packs

- **Decision source:** AR-009 V1.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-019`, `ARQ-PERF-020`, `ARQ-PERF-023`
- **Decision:** Relevant slices and Feature Packs carry explicit performance budgets/baselines for paths they materially affect. A statistically/materially meaningful unexplained regression against the approved budget or representative baseline fails acceptance even when functional tests pass.
- **Rationale:** Deferring known performance debt until the end contradicts the scale-ready/no-intentional-performance-debt doctrine.
- **Rules:**
  1. Deterministic structural checks catch known anti-patterns where practical.
  2. Real latency/throughput claims require representative benchmark/load evidence.
  3. A baseline may tighten after proven improvement; it may not quietly deteriorate.
  4. Regression exceptions require explicit rationale/authority and must not weaken hard invariants.
- **Failure behaviour:** Failed material budget halts the affected delivery gate until corrected or explicitly amended at the right authority layer.
- **Security/privacy:** Performance fixes cannot bypass access/privacy controls.
- **Performance/scaling:** Regression tests preserve future scaling headroom rather than validating only current tiny load.
- **Enforcement/downstream:** Feature Pack/VS acceptance evidence references concrete performance checks.

## ARC-298 — Performance-sensitive capabilities use a progressive proof ladder from smoke through failure/recovery pressure, with workload-based justified exclusions

- **Decision source:** AR-009 V1.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-003`, `ARQ-PERF-021`, `ARQ-PERF-022`, `ARQ-PERF-162`
- **Decision:** Applicable performance verification uses progressive classes: smoke, normal load, stress, spike, breakpoint/limit discovery, soak and relevant failure/recovery pressure. Not every capability must execute every class, but exclusions require explicit workload/risk rationale.
- **Rationale:** Different tests reveal different failure modes; a single steady load test cannot prove burst tolerance, leak-free endurance, breakpoint behaviour or recovery safety.
- **Rules:**
  1. Test class selection derives from workload semantics and criticality.
  2. Hard correctness assertions remain active during stress/spike/failure tests.
  3. Breakpoint testing is controlled and need not endanger production.
  4. Soak duration/scale is evidence-driven and proportionate.
- **Failure behaviour:** Breach of a hard invariant fails the scenario regardless of throughput/latency success.
- **Security/privacy:** Use safe synthetic identities/data and representative controls.
- **Performance/scaling:** Major tests capture saturation/resource evidence to explain the limit, not merely the first observed failure count.
- **Enforcement/downstream:** Architectural Proof/hardening/release stages choose and document applicable classes.

## ARC-299 — Performance proof uses layered cadence across CI, Feature Packs, Architectural Proof, hardening and release gates

- **Decision source:** AR-009 V1.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-020`, `ARQ-PERF-021`, `ARQ-PERF-022`
- **Decision:** Distribute performance verification by cost and purpose: cheap deterministic checks in normal CI; smoke/small-load tests frequently; workload-specific load/stress tests during affected Feature Packs; and major spike/breakpoint/soak/failure-recovery tests during Architectural Proof, hardening or release gates where applicable.
- **Rationale:** Running every expensive scenario on every commit is wasteful, while reserving all performance testing for release discovers structural problems too late.
- **Rules:**
  1. Fast regression evidence is available close to the change.
  2. Expensive proofs run when the architecture/scope is stable enough to make them meaningful.
  3. Critical-flow changes can trigger earlier/larger proof regardless of cadence.
- **Failure behaviour:** Required proof omitted without justified classification is a release/gate failure.
- **Security/privacy:** Test environments/data remain appropriately isolated and minimised.
- **Performance/scaling:** Cadence preserves both fast feedback and credible large-scale evidence.
- **Enforcement/downstream:** CI/gate manifests name the proof class and execution stage.

## ARC-300 — Representative performance evidence includes cold-cache, restart, deployment-overlap and dependency-recovery states where applicable

- **Decision source:** AR-009 V1.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-018`, `ARQ-PERF-154`, `ARQ-PERF-155`, `ARQ-PERF-162`
- **Decision:** Important applicable paths are tested under warm state and relevant non-ideal states including cold cache, node restart, rolling-deployment overlap and dependency recovery. Warm-cache steady-state benchmarks alone are insufficient architecture/release proof.
- **Rationale:** Real incidents/deployments occur outside ideal warmed steady state and can reveal stampedes, startup pressure, stale-version incompatibility and recovery thundering herds.
- **Rules:**
  1. Cold-state tests preserve empty-cache correctness.
  2. Restart tests include readiness/startup semantics rather than merely process boot.
  3. Rolling-overlap tests exercise adjacent-version shared contracts where used.
  4. Dependency-recovery tests observe retry/backlog catch-up pressure.
- **Failure behaviour:** Stampede or recovery overload that threatens correctness/availability is a failed proof.
- **Security/privacy:** Recovery/deployment tests preserve normal security controls.
- **Performance/scaling:** Resource spikes during warming/recovery count toward headroom/capacity planning.
- **Enforcement/downstream:** V2 capacity/headroom decisions consume this evidence.

## ARC-301 — Formal performance scenarios have versioned pass/fail thresholds plus independent hard-invariant assertions

- **Decision source:** AR-009 V1.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-010`, `ARQ-PERF-020`, `ARQ-PERF-021`, `ARQ-PERF-024`, `ARQ-PERF-025`
- **Decision:** Every formal verification scenario defines versioned pass/fail thresholds and invariant assertions before execution. Thresholds may cover latency percentiles, error/failure rate, throughput/freshness, backlog/wait age and saturation; zero-tolerance correctness/privacy/safety/payment/entitlement/capacity invariants are asserted independently and are never converted into consumable performance error budgets.
- **Rationale:** Charts without acceptance criteria do not constitute evidence-bearing release gates.
- **Rules:**
  1. Threshold provenance identifies workload, environment, release and test version.
  2. A scenario can fail for performance or invariant breach independently.
  3. Threshold changes are reviewed/versioned and cannot silently redefine historical results.
  4. False success under unsafe overload is prohibited.
- **Failure behaviour:** Any hard-invariant violation is immediate failure regardless of achieved throughput.
- **Security/privacy:** Performance assertions include relevant security/privacy invariants where the workload can threaten them.
- **Performance/scaling:** Thresholds are linked to saturation evidence so passes remain interpretable.
- **Enforcement/downstream:** Gate manifests reference the exact threshold/test artifact version.

## ARC-302 — Major scale proofs validate load-generator capacity and distribute generation only when evidence requires it

- **Decision source:** AR-009 V1.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-001`, `ARQ-PERF-003`, `ARQ-PERF-021`, `ARQ-PERF-160`
- **Decision:** Major high-scale proofs verify that the load generator itself has sufficient CPU, memory, network and scheduling capacity to produce the declared traffic faithfully. Begin with the simplest generator topology that satisfies the proof; distribute load generation when one generator becomes a bottleneck, multiple network origins are genuinely required, or target scale cannot otherwise be generated reliably.
- **Rationale:** A saturated test client can make an application appear slower, faster or lower-throughput than reality and invalidates capacity conclusions.
- **Rules:**
  1. Generator-side utilisation/limitations are captured for major proofs.
  2. Generated arrival rate/concurrency is validated against the declared scenario.
  3. Distributed generation is a proof mechanism, not mandatory infrastructure from day one.
  4. Test-network/provider limits are separated from application bottlenecks where practical.
- **Failure behaviour:** A generator-limited test is marked invalid/inconclusive rather than accepted as the platform breakpoint.
- **Security/privacy:** Distributed generators use controlled credentials/data and approved source networks.
- **Performance/scaling:** Generator topology scales only as required to produce trustworthy evidence.
- **Enforcement/downstream:** Architectural Proof/release evidence records generator validity for major load tests.

**V1 consolidated doctrine:** Performance proof is workload-specific, percentile-driven, user-and-system aware, progressively tested, gate-bearing and generator-valid. Hard correctness invariants remain outside consumable error budgets. Performance budgets are initial ceilings/floors that can tighten with evidence but may not silently weaken.

**V1 deferrals:** Exact per-flow concurrency/arrival envelopes; exact RPO/RTO values; final CWV official thresholds at future gate time; concrete k6/test-runner topology; test data generators; CI provider; test-environment sizing; path-specific stricter latency budgets; workload-specific soak durations; exact error-rate/freshness thresholds; and final capacity triggers remain V2/V3/FLOW/Feature Pack/JIT evidence decisions.

## 4M.2 Round V2 — Capacity Budgets, Multi-Node Multipliers & Scaling Triggers

**Accepted answer set:** `V2.1 B, V2.2 B, V2.3 B, V2.4 B, V2.5 B, V2.6 B, V2.7 B, V2.8 B, V2.9 B, V2.10 B, V2.11 B, V2.12 B`

## ARC-303 — PostgreSQL connections are one platform-wide finite capacity budget, not independent per-node entitlements

- **Decision source:** AR-009 V2.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-073`, `ARQ-PERF-074`, `ARQ-PERF-008`; cross-reference `ARC-073`, `ARC-156`, `ARC-257`
- **Decision:** PostgreSQL connection capacity is budgeted across the entire production topology, including interactive application pools, durable workers, migrations/maintenance, monitoring/operations and future nodes/pools. Per-node pool size is derived from the total safe PostgreSQL envelope and measured workload rather than chosen independently.
- **Rationale:** Horizontal application scaling can otherwise multiply connection demand faster than database capacity and move the bottleneck into pool/database saturation.
- **Rules:**
  1. Capacity models state application-node count, pool count, worker count and reserved operational connection requirements.
  2. Adding a node triggers recalculation of total possible PostgreSQL concurrency.
  3. Pool saturation uses bounded queueing/timeouts/backpressure rather than emergency unbounded connection growth.
  4. One connection per user is prohibited as a design assumption.
- **Failure behaviour:** When the safe database envelope is reached, governed admission/backpressure/degradation applies before connection-capacity correctness is compromised.
- **Security/privacy:** Operational reserve does not become a general privileged bypass to normal application authority.
- **Performance/scaling:** Pool queue time and database saturation are first-class evidence for topology changes.
- **Enforcement/downstream:** FLOW proofs and deployment sizing must show the whole-topology connection budget.

## ARC-304 — Production database capacity retains an explicit operational/failure reserve rather than planning steady state at the hard ceiling

- **Decision source:** AR-009 V2.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-073`, `ARQ-PERF-074`, `ARQ-PERF-146`, `ARQ-PERF-160`
- **Decision:** The steady-state connection/load plan must preserve evidence-based reserve for operations, maintenance, failover/recovery and unexpected pressure. Exact counts/percentages are configuration/proof decisions and are not hard-coded in Architecture Law.
- **Rationale:** A topology that consumes every available connection during ordinary load has no safe room for recovery, maintenance or incident response.
- **Rules:**
  1. Reserve is sized from PostgreSQL capability and expected failure topology.
  2. Operational reserve is monitored and not silently consumed by ordinary pools.
  3. Capacity alerts/scaling triggers fire before the hard ceiling becomes the operating target.
- **Failure behaviour:** Exhaustion of planned reserve is a capacity-risk condition requiring admission/scaling/remediation, not a reason to loosen correctness controls.
- **Security/privacy:** Reserved operational access remains least-privilege and auditable.
- **Performance/scaling:** Headroom evidence includes connection capacity, not CPU/RAM alone.
- **Enforcement/downstream:** Production sizing/runbooks and recovery exercises include reserve validation.

## ARC-305 — Transaction-pooling compatibility is preserved now; PgBouncer-equivalent topology is introduced only on measured need

- **Decision source:** AR-009 V2.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-075`, `ARQ-PERF-073`, `ARQ-PERF-160`
- **Decision:** Application/database usage should avoid unnecessary session-local PostgreSQL assumptions that would force redesign for transaction pooling later. PgBouncer or equivalent external pooling remains evidence-gated and is introduced when multi-node connection pressure, connection churn or topology justifies its operational cost.
- **Rationale:** Scale-readiness requires avoiding preventable incompatibility without installing infrastructure before it solves a measured problem.
- **Rules:**
  1. New database features that require sticky/session-local semantics identify the compatibility cost explicitly.
  2. Pooling introduction requires representative proof of benefit and compatibility.
  3. External pooling does not change business authority or transaction semantics.
- **Failure behaviour:** Connection pressure is first diagnosed and pool budgets corrected; a proxy is not used to hide unsafe query/load behaviour.
- **Security/privacy:** Pooling topology preserves authentication/networking/least-privilege controls.
- **Performance/scaling:** Pooling is a capacity tool, not an authority layer.
- **Enforcement/downstream:** JIT deployment/database proof records whether external pooling is required.

## ARC-306 — Critical/common database paths use semantic query-shape and representative query-plan budgets, not universal query-count folklore

- **Decision source:** AR-009 V2.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-067`, `ARQ-PERF-068`, `ARQ-PERF-071`, `ARQ-PERF-072`, `ARQ-PERF-083`
- **Decision:** Important access paths receive bounded query/retrieval shapes, indexes derived from real constraints/filters/joins/orderings and representative PostgreSQL query-plan evidence. Universal rules such as “every action <= N queries” are not Architecture Law, although path-specific query counts may be regression signals.
- **Rationale:** Query count alone does not capture cardinality, lock behaviour, planner choices, row width or I/O cost.
- **Rules:**
  1. Growing reads are bounded by pagination, streaming, aggregation or equivalent controlled traversal.
  2. Deep/high-volume traversal prefers access patterns that avoid pathological offset cost where semantics allow.
  3. Critical/slow/suspicious queries use representative data cardinality/distribution for plan evidence.
  4. Specialised indexes are justified by actual paths/invariants and carry observable maintenance cost.
- **Failure behaviour:** A path with unbounded materialisation or unstable/unsafe query-plan behaviour fails proof even if small fixtures are fast.
- **Security/privacy:** Query optimisations may not bypass row/field/purpose authorization.
- **Performance/scaling:** Query/index changes are assessed against latency, write amplification, storage and maintenance effects.
- **Enforcement/downstream:** Domain Dossiers/Feature Packs define exact access-path budgets and indexes.

## ARC-307 — Read scaling follows an evidence-driven ladder while correctness-sensitive reads remain on an authority-consistent path

- **Decision source:** AR-009 V2.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-076`, `ARQ-PERF-077`, `ARQ-PERF-078`, `ARQ-PERF-079`, `ARQ-PERF-080`
- **Decision:** Read scaling progresses from sound authoritative query/model design and indexes, to bounded derived/read models or caches where justified, then to stale-tolerant replicas/partitioning only when workload evidence warrants them. Correctness-sensitive read-after-write paths use an authority path that provides the required consistency.
- **Rationale:** Premature replicas/partitioning/denormalisation add operational and consistency complexity while often failing to address the real bottleneck.
- **Rules:**
  1. Large peak-time analytics scans may not compete blindly with critical OLTP.
  2. Read replicas are explicitly stale-tolerant and never assumed perfectly current.
  3. Derived models declare freshness/rebuild semantics and never become transactional authority.
  4. Partitioning is introduced only for demonstrated volume/retention/maintenance/query benefit.
- **Failure behaviour:** Replica lag or derived-model staleness degrades only workloads that permit it and must not corrupt correctness-sensitive decisions.
- **Security/privacy:** Derived/replica access retains the same privacy/deletion/authorization constraints applicable to the data class.
- **Performance/scaling:** Each added read-acceleration layer must show measurable benefit and known freshness cost.
- **Enforcement/downstream:** FLOW/Dossier proof chooses the lowest-complexity layer that meets the workload.

## ARC-308 — LiveView scale is proven through bounded per-connection resource envelopes rather than assumed from lightweight BEAM processes

- **Decision source:** AR-009 V2.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-123`, `ARQ-PERF-124`, `ARQ-PERF-125`, `ARQ-PERF-135`
- **Decision:** Representative LiveView experiences are empirically budgeted for server-side connection/process cost including assigns/state, subscriptions, mailbox pressure, event/render work, query behaviour and fan-out. The process-per-connection model remains accepted; unbounded per-connection growth does not.
- **Rationale:** BEAM process overhead is only one component of connection cost; retained state, subscriptions, renders and downstream amplification can dominate at scale.
- **Rules:**
  1. Large/growing collections use streams/pagination/keyed bounded representations rather than indefinite socket assigns.
  2. Slow/stale clients may not accumulate unbounded mailboxes or server work.
  3. Expendable intermediate UI observations may be coalesced/reconstructed from current authority.
  4. Representative connection-cost evidence is captured at meaningful connection counts and workloads.
- **Failure behaviour:** Mailbox/memory/render/query amplification beyond the approved envelope triggers coalescing, degradation, admission or redesign rather than unlimited accumulation.
- **Security/privacy:** Connection-state minimisation also limits unnecessary sensitive-data residence.
- **Performance/scaling:** Connection-count claims include per-connection resource evidence, not process counts alone.
- **Enforcement/downstream:** V3/FLOW pressure tests include representative LiveView populations where applicable.

## ARC-309 — Realtime capacity proof measures end-to-end amplification from one logical change through subscribers, refresh, render and network

- **Decision source:** AR-009 V2.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-132`, `ARQ-PERF-133`, `ARQ-PERF-135`; cross-reference `ARC-175`, `ARC-176`
- **Decision:** High-fan-out realtime proofs measure the full amplification chain rather than PubSub broadcast throughput alone: topic/broadcast, subscriber process work, authoritative refresh where required, render/diff, payload/network and cross-node effects.
- **Rationale:** A fast broadcast primitive can still trigger catastrophic N×M database, render, memory or network work downstream.
- **Rules:**
  1. Topic scoping, coalescing, batching and derived projections are used where they materially reduce amplification.
  2. Realtime refresh retrieves only the projection needed for the changed UI where practical.
  3. Obsolete intermediate states need not be faithfully buffered.
  4. Fan-out tests include representative subscriber distributions and multi-node topology where applicable.
- **Failure behaviour:** Realtime may degrade in freshness before authoritative correctness; uncontrolled amplification is a failed proof.
- **Security/privacy:** PubSub/topic knowledge never becomes authorization; refreshed data is re-read through proper authority.
- **Performance/scaling:** CPU, DB, mailbox, render, network and payload dimensions are correlated in the proof.
- **Enforcement/downstream:** FLOW tests define high-fan-out scenarios for affected features.

## ARC-310 — Durable worker capacity shares database/CPU/RAM/I/O/provider budgets with interactive traffic and is constrained by the tightest bottleneck

- **Decision source:** AR-009 V2.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-106`, `ARQ-PERF-108`, `ARQ-PERF-110`, `ARQ-PERF-111`, `ARQ-PERF-112`; cross-reference `ARC-157`, `ARC-158`
- **Decision:** Oban/worker concurrency is sized against the same finite PostgreSQL, CPU, memory, I/O and provider budgets as interactive work, with critical interactive/authoritative headroom protected. Queue concurrency follows the tightest relevant bottleneck rather than available BEAM schedulers alone.
- **Rationale:** Asynchronous execution moves work in time; it does not make the underlying resources unlimited.
- **Rules:**
  1. Low-value bulk/convenience work is throttleable/pausable/deferable before starving critical work.
  2. Provider-limited or CPU/I/O-heavy workloads receive queue isolation and suitable lower concurrency where needed.
  3. Queue wait/completion/freshness SLOs are workload-specific.
  4. Worker topology may later separate onto worker-focused nodes without changing domain semantics.
- **Failure behaviour:** Backlog growth triggers controlled throttling/admission/concurrency adjustment rather than blindly increasing workers.
- **Security/privacy:** Worker separation does not create broader execution authority; handlers retain current-policy/revalidation rules.
- **Performance/scaling:** Queue depth/oldest age/throughput/resource saturation and OLTP impact are evaluated together.
- **Enforcement/downstream:** Composite pressure tests include worker traffic alongside interactive load.

## ARC-311 — Horizontal node count is both a capacity multiplier and a shared-resource pressure multiplier that requires explicit recalculation

- **Decision source:** AR-009 V2.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-008`, `ARQ-PERF-073`, `ARQ-PERF-106`, `ARQ-PERF-133`, `ARQ-PERF-160`; cross-reference `ARC-004`, `ARC-159`
- **Decision:** Adding application/worker nodes requires recalculation of aggregate DB pools, local queue concurrency, provider/API concurrency, PubSub/fan-out, cache/rebuild pressure, scheduled work, socket distribution and telemetry volume. Node replication must not silently multiply a strict global constraint.
- **Rationale:** Horizontal scale can increase pressure on shared state/services even while increasing application CPU/RAM capacity.
- **Rules:**
  1. Per-node concurrency values are not assumed to be global unless enforced/proven as such.
  2. Periodic/scheduled work preserves one-logical-issuance semantics where required.
  3. Provider limits and database capacity are modelled across all nodes.
  4. Multi-node pressure proof precedes reliance on the scaled topology for production capacity.
- **Failure behaviour:** If added nodes push a shared dependency beyond its safe envelope, scaling is rejected/reconfigured rather than treated as success.
- **Security/privacy:** Node replication preserves the same authority/privacy semantics and secrets/config isolation.
- **Performance/scaling:** Capacity gains are measured net of new shared-resource demand.
- **Enforcement/downstream:** Deployment/topology changes include a multiplier impact review.

## ARC-312 — Production headroom is resource/workload specific and maintained before measured saturation knees; autoscaling does not replace capacity planning

- **Decision source:** AR-009 V2.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-005`, `ARQ-PERF-152`, `ARQ-PERF-160`, `ARQ-PERF-161`
- **Decision:** Safe operating envelopes and headroom are defined per constrained resource/workload from measured saturation behaviour and expected failure topology. There is no universal Architecture percentage for CPU, memory, database connections, provider quota, network or queue backlog.
- **Rationale:** Different resources fail non-linearly at different saturation points; universal utilisation percentages create false confidence.
- **Rules:**
  1. Scaling/shedding triggers occur before the demonstrated saturation knee.
  2. Headroom accounts for expected burst, recovery catch-up and traffic redistribution after capacity loss.
  3. Once production relies on multiple capacity units, expected loss of one relevant unit must not immediately cause cascading failure.
  4. Autoscaling is a response mechanism, not permission to run permanently at unsafe saturation.
- **Failure behaviour:** When headroom is exhausted, governed admission/degradation activates before correctness is compromised.
- **Security/privacy:** Capacity shedding preserves security/privacy/safety/payment/entitlement invariants.
- **Performance/scaling:** Headroom targets are evidence-bearing and revisited with workload/topology changes.
- **Enforcement/downstream:** Release/readiness capacity evidence records the active safe operating envelope.

## ARC-313 — Vertical versus horizontal scaling is triggered by the measured bottleneck and uses the simplest lawful mechanism that resolves it

- **Decision source:** AR-009 V2.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-002`, `ARQ-PERF-073`, `ARQ-PERF-075`, `ARQ-PERF-076`, `ARQ-PERF-079`, `ARQ-PERF-106`, `ARQ-PERF-160`
- **Decision:** Scaling decisions follow sustained SLI/resource/headroom evidence and forecasted workload rather than registered-user counts or a fixed vertical/horizontal ideology. Query/index correction precedes adding database complexity where it addresses the bottleneck; application/worker nodes, DB capacity, pooling, replicas/read models and partitioning are introduced only where each solves the demonstrated constraint.
- **Rationale:** Scaling the wrong layer increases cost/complexity while preserving the actual bottleneck.
- **Rules:**
  1. Optimisation of known structural inefficiency precedes infrastructure multiplication where practical.
  2. Vertical scaling remains valid when it is the simplest sufficient capacity step.
  3. Horizontal scaling is used for availability/parallel capacity only when shared-resource envelopes remain safe.
  4. Specialised infrastructure is evidence-gated and must preserve existing domain semantics.
- **Failure behaviour:** A scaling change that fails to improve the constrained SLI/resource or creates a worse shared bottleneck is rolled back/revised.
- **Security/privacy:** Scaling may not weaken isolation/authorization to obtain throughput.
- **Performance/scaling:** Trigger evidence is versioned and tied to workload/topology.
- **Enforcement/downstream:** Capacity plans state bottleneck, chosen intervention and proof outcome.

## ARC-314 — Final topology capacity proof uses realistic composite competing workloads and expected failure/recovery conditions, not isolated component maxima

- **Decision source:** AR-009 V2.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-003`, `ARQ-PERF-018`, `ARQ-PERF-112`, `ARQ-PERF-160`, `ARQ-PERF-162`
- **Decision:** Major topology proofs combine the material competing workloads for the reference scenario—HTTP/Ash, connected LiveViews, PostgreSQL pool/query contention, durable worker backlog, provider delay/retries, realtime fan-out, cold/recovery activity and expected capacity loss where applicable. They do not simply add independent component maxima or require impossible simultaneous worst cases unrelated to the workload model.
- **Rationale:** Shared-resource contention and recovery catch-up emerge only when subsystems operate together.
- **Rules:**
  1. Composite scenarios are derived from V1 workload profiles and expected failure topology.
  2. Component tests remain useful diagnostics but do not replace end-to-end pressure proof.
  3. Correctness/invariant assertions run under the same composite pressure.
  4. Generator validity from ARC-302 remains required.
- **Failure behaviour:** Saturation, false success, unbounded backlog/amplification or hard-invariant breach under the declared envelope fails the topology proof.
- **Security/privacy:** Representative pressure tests preserve normal security/privacy controls and use synthetic/minimised data.
- **Performance/scaling:** Results define the proven safe envelope for that topology/release/workload version.
- **Enforcement/downstream:** V3 and FLOW proof matrices use composite topology scenarios as release evidence.

**V2 consolidated doctrine:** Capacity is a set of shared finite resource envelopes. Horizontal scale can add application capacity while simultaneously multiplying database, worker, provider, fan-out and telemetry pressure. Scale the measured bottleneck using the simplest mechanism that preserves authority, maintain evidence-based headroom, and prove the whole topology under realistic competing load.

**V2 deferrals:** Exact PostgreSQL `max_connections`/pool sizes; exact operational reserve; PgBouncer introduction point/configuration; exact indexes/query-count budgets; read-replica/partition thresholds; per-LiveView byte/process limits; queue concurrency values; node counts; provider quotas; headroom percentages; autoscaling rules; and exact composite workload numbers remain V3/FLOW/Feature Pack/JIT/performance evidence decisions.


## 4M.3 Round V3 — Contention, Recovery & Final Performance-Proof Matrix

**Accepted answer set:** `V3.1 B, V3.2 B, V3.3 B, V3.4 B, V3.5 B, V3.6 B, V3.7 B, V3.8 B, V3.9 B, V3.10 B, V3.11 B, V3.12 B`

## ARC-315 — Contention and race proofs attack declared hard invariants and inspect authoritative post-state, not merely throughput

- **Decision source:** AR-009 V3.1
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-025`, `ARQ-PERF-031`, `ARQ-PERF-041`; cross-reference `ARC-068`, `ARC-070`, `ARC-301`
- **Decision:** Every material contention-sensitive reference flow declares the hard invariant being attacked and proves it under deliberately simultaneous, duplicate, reordered, retried and partially failed execution. Proof evaluates authoritative durable post-state and reconciliation evidence rather than inferring correctness from HTTP success/error counts or throughput alone.
- **Rationale:** High throughput can coexist with duplicate grants, illegal transitions or oversell; performance evidence is invalid if correctness is not asserted under the same pressure.
- **Rules:**
  1. The invariant under test is named before execution.
  2. Test concurrency is designed to maximise realistic collision/overlap for the governed operation.
  3. Durable post-state and relevant operation/idempotency evidence are verified after the run.
  4. Hard-invariant violations are zero-tolerance failures independent of latency/error-budget thresholds.
- **Failure behaviour:** Any committed invariant breach fails the proof immediately; transient/refused work is evaluated according to the workload contract rather than counted as corruption.
- **Security/privacy:** Pressure tests use synthetic/minimised identities and do not weaken normal authorisation/security controls.
- **Performance/scaling:** Safe throughput is the highest envelope that preserves both performance budgets and hard invariants.
- **Enforcement/downstream:** Reference Flow Pressure Tests and later Feature Pack proof matrices include explicit invariant assertions.

## ARC-316 — Scarce-inventory and flash-sale proofs require zero confirmed oversell under adversarial concurrency

- **Decision source:** AR-009 V3.2
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-003`, `ARQ-PERF-010`, `ARQ-PERF-031`, `ARQ-PERF-041`; cross-reference `ARC-069`, `ARC-301`, `ARC-315`
- **Decision:** Scarce-inventory/capacity proofs drive competing reservations/confirmations against the same constrained authority under relevant burst, retry, duplicate and multi-node conditions and assert that confirmed allocations never exceed authoritative capacity. Latency may degrade and excess demand may be throttled, queued, deferred or rejected according to law; confirmed oversell is never an acceptable trade-off.
- **Rationale:** Flash-sale scale is a correctness problem first and a throughput problem second.
- **Rules:**
  1. The test includes intentional contention on the same inventory/capacity keys rather than evenly distributed low-contention demand only.
  2. Duplicate/retry cases are included where the real client/provider path can create them.
  3. Final confirmed allocation count is reconciled to authoritative capacity.
  4. Failed/refused demand must not fabricate success or hidden allocation.
- **Failure behaviour:** One committed oversell is a hard failure regardless of achieved requests/second.
- **Security/privacy:** Synthetic purchase/participant data is used for large-scale proof unless a separately approved environment requires otherwise.
- **Performance/scaling:** Proof records the highest safe contention envelope, tail latency, refusal behaviour and saturation point.
- **Enforcement/downstream:** Ticketing/inventory Feature Packs inherit this zero-oversell gate where scarcity applies.

## ARC-317 — Retry and duplicate storms are explicit performance/correctness scenarios for idempotency and reconciliation

- **Decision source:** AR-009 V3.3
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-026`, `ARQ-PERF-027`, `ARQ-PERF-041`, `ARQ-PERF-112`; cross-reference `ARC-071`, `ARC-146`, `ARC-170`
- **Decision:** Applicable proofs deliberately inject duplicate submissions, client/connectivity retries, durable-job retries, duplicated/reordered provider callbacks and ambiguous timeout/recovery cases. The expected result is one valid durable effect per governed operation identity, or a deliberately unresolved/reconcilable state, never multiplied committed effects.
- **Rationale:** Clean one-request-per-user load hides the failure modes most likely to create duplicate payments, entitlements or side effects in production.
- **Rules:**
  1. Duplicate/retry patterns are derived from realistic protocol/client/provider behaviour.
  2. Business idempotency remains distinct from Oban uniqueness or transport duplicate suppression.
  3. Ambiguous irreversible provider outcomes reconcile before unsafe repetition.
  4. Test assertions inspect authoritative effects and reconciliation state.
- **Failure behaviour:** Duplicate durable effects or unrecoverable ambiguous state fail the scenario.
- **Security/privacy:** Retry simulations do not bypass authentication or disclose sensitive response differences.
- **Performance/scaling:** Retry amplification and its effect on shared resources are captured explicitly.
- **Enforcement/downstream:** Reference flows identify which duplicate/retry classes are mandatory for their proof matrix.

## ARC-318 — Database contention proof measures lock, pool, transaction and query-plan behaviour alongside business outcomes

- **Decision source:** AR-009 V3.4
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-073`, `ARQ-PERF-074`, `ARQ-PERF-083`, `ARQ-PERF-084`, `ARQ-PERF-085`; cross-reference `ARC-072`, `ARC-073`, `ARC-273`, `ARC-306`
- **Decision:** Contention-sensitive performance proofs collect sufficient database evidence to distinguish pool queueing, lock waits/contention, transaction duration, deadlock/timeout behaviour, query-plan cost and database resource saturation while verifying the governed business result. Passing latency alone is insufficient if the workload creates unsafe lock amplification or starves unrelated OLTP work.
- **Rationale:** Database saturation often presents as application latency while the real limiting mechanism is shared connection, lock or I/O contention.
- **Rules:**
  1. Relevant scenarios capture pool and database-side pressure dimensions.
  2. Long/interactive queries remain bounded according to workload class.
  3. Unrelated critical traffic is included where required to detect starvation/blast radius.
  4. Representative cardinality/distribution is required for scale-sensitive query plans.
- **Failure behaviour:** Dangerous lock amplification, unbounded waiting, starvation or hard-invariant breach fails the proof even when some latency percentiles remain within target.
- **Security/privacy:** Query diagnostics are captured without exporting sensitive row payloads unnecessarily.
- **Performance/scaling:** Evidence identifies whether the bottleneck is query, pool, lock, I/O, CPU, plan or other database resource.
- **Enforcement/downstream:** Query/load evidence feeds index/query/topology decisions rather than generic database scaling assumptions.

## ARC-319 — Cold-cache, expiry and recovery proofs must demonstrate bounded anti-stampede regeneration

- **Decision source:** AR-009 V3.5
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-018`, `ARQ-PERF-057`, `ARQ-PERF-154`; cross-reference `ARC-081`, `ARC-086`, `ARC-300`, `ARC-314`
- **Decision:** Material cached/high-fan-out paths are tested under cold cache, coordinated/near-coordinated expiry, node startup and dependency recovery so simultaneous misses cannot create uncontrolled regeneration/database/provider pressure. Proof validates the applicable coalescing, jitter, prewarming, stale-safe serving or other bounded anti-stampede mechanism while preserving empty-cache correctness.
- **Rationale:** Warm-state benchmarks hide a common cascading-failure mechanism: many consumers regenerating the same derived value simultaneously.
- **Rules:**
  1. Cache absence may worsen latency but may not break authority/correctness.
  2. Regeneration amplification is measured at database/provider/resource boundaries.
  3. Stale-while-revalidate or stale serving is used only where the data class permits it.
  4. Prewarming remains bounded and may not itself stampede dependencies.
- **Failure behaviour:** Unbounded regeneration amplification or correctness dependence on cache presence fails the proof.
- **Security/privacy:** Protected/sensitive cache paths preserve their access contract during recovery/stale handling.
- **Performance/scaling:** The proof records cold/recovery cost and time to return to stable operating envelopes.
- **Enforcement/downstream:** High-fan-out cache use requires an anti-stampede proof case in the relevant matrix.

## ARC-320 — Backlog recovery is proven as controlled catch-up inside shared OLTP/provider budgets, not merely eventual queue drain

- **Decision source:** AR-009 V3.6
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-108`, `ARQ-PERF-110`, `ARQ-PERF-111`, `ARQ-PERF-112`; cross-reference `ARC-156`, `ARC-157`, `ARC-164`, `ARC-309`, `ARC-314`
- **Decision:** Queue/system proofs include burst creation, sustained backlog, dependency slowdown/outage, retry pressure, node restart, deployment interruption and recovery. Catch-up must remain within approved PostgreSQL, CPU/RAM/I/O and provider budgets, protect newly arriving higher-criticality work and meet workload-specific queue wait/completion/freshness objectives without weakening hard correctness obligations.
- **Rationale:** Maximum worker concurrency after an outage can turn recovery into a second outage by crushing shared dependencies.
- **Rules:**
  1. Recovery scenarios include new foreground/critical arrivals while backlog drains where relevant.
  2. Low-value work is throttleable/deferable before critical queues or OLTP are starved.
  3. Queue freshness/completion SLOs are evaluated separately from must-happen correctness.
  4. Provider-specific concurrency/rate constraints remain part of the recovery budget.
- **Failure behaviour:** Catch-up that causes cascading saturation, starvation, false completion or missed hard obligation fails the proof.
- **Security/privacy:** Backlog controls do not skip privacy/security/consent revalidation where current policy is required.
- **Performance/scaling:** Proof captures drain rate, oldest-job age, resource use and stable-recovery envelope.
- **Enforcement/downstream:** Worker/queue topology changes require representative backlog-recovery evidence.

## ARC-321 — Realtime capacity proof includes connection/reconnect storms, fan-out bursts, slow clients, node loss and rolling recovery

- **Decision source:** AR-009 V3.7
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-123`, `ARQ-PERF-124`, `ARQ-PERF-125`, `ARQ-PERF-132`, `ARQ-PERF-133`, `ARQ-PERF-136`; cross-reference `ARC-054`, `ARC-055`, `ARC-308`
- **Decision:** Realtime performance validation includes large concurrent connection populations and the adverse behaviours that matter operationally: connection/reconnect storms, subscription fan-out, broadcast bursts, slow clients, rolling deployment, node loss and recovery. Proof verifies bounded process/mailbox/memory/database/render/network amplification while permitting governed freshness degradation instead of durable corruption.
- **Rationale:** Idle WebSocket counts or ordinary HTTP load do not prove LiveView/PubSub behaviour under reconnect/fan-out pressure.
- **Rules:**
  1. Representative LiveView state and subscriptions are used rather than empty sockets only.
  2. Slow/stale clients may not create unbounded mailbox or server work.
  3. Broadcast refresh remains scoped/coalesced and avoids N×M database amplification.
  4. Node loss may interrupt freshness but not durable truth.
- **Failure behaviour:** Unbounded mailbox/memory/fan-out/database amplification or durable-effect duplication fails the proof.
- **Security/privacy:** Reconnect/failover preserves current authorisation/revocation semantics.
- **Performance/scaling:** The proof establishes connection/process/fan-out envelopes for the tested topology.
- **Enforcement/downstream:** Realtime-heavy reference flows receive explicit realtime pressure scenarios.

## ARC-322 — Abuse and velocity controls are pressure-tested with normal layered protections enabled and must work across nodes without enumeration leakage

- **Decision source:** AR-009 V3.8
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-SEC-001`, `ARQ-PERF-003`, `ARQ-PERF-005`, `ARQ-PERF-010`; cross-reference `ARC-141`, `ARC-142`, `ARC-258`
- **Decision:** Applicable authentication, recovery, redemption, checkout/payment, protected-download/search and similar sensitive entry points are pressure-tested with their normal layered edge/application/distributed abuse controls enabled. Proof verifies cross-node effectiveness, bounded legitimate recovery/challenge semantics, stricter privileged handling where required and non-enumerating external responses. Exact thresholds and concrete counter/backing technology remain evidence/JIT decisions.
- **Rationale:** Disabling abuse controls during performance testing can produce an impressive benchmark for a topology that is not the topology actually exposed to hostile traffic.
- **Rules:**
  1. Test profiles distinguish ordinary users, bursts, accidental retry and malicious/automated pressure where relevant.
  2. Distributed limits must remain effective when traffic is spread across application nodes.
  3. Rate-control failure/degradation semantics are explicit and may not silently grant unlimited access to high-risk operations.
  4. Thresholds are tuned from risk and measured legitimate traffic rather than one universal constant.
- **Failure behaviour:** Cross-node bypass, enumeration leakage, runaway counter dependency pressure or unsafe fail-open behaviour fails the relevant security/performance gate.
- **Security/privacy:** Rate-limit identifiers/payloads are minimised and may not become a tracking/marketing identity store.
- **Performance/scaling:** Counter/backend latency and saturation are included in the safe operating envelope.
- **Enforcement/downstream:** Exact library/backend/threshold selection is proof-gated before implementation of the affected Feature Pack.

## ARC-323 — Large/hot-table migrations and database maintenance are pressure-tested as part of the production performance envelope

- **Decision source:** AR-009 V3.9
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-081`, `ARQ-PERF-082`, `ARQ-PERF-083`, `ARQ-PERF-085`; cross-reference `ARC-076`, `ARC-262`, `ARC-318`
- **Decision:** Production schema/index changes affecting large or hot tables are tested with representative cardinality and concurrent workload for lock duration, runtime, resource impact, failure/rollback or forward-recovery behaviour and adjacent-version compatibility. Routine PostgreSQL maintenance, planner statistics and vacuum/analyze health are included in the operating performance model rather than treated as unrelated DBA detail.
- **Rationale:** A migration that succeeds on a small/idle database may create unacceptable lock or I/O pressure in a realistic production workload.
- **Rules:**
  1. Representative data volume/distribution is used for scale-sensitive migration proof.
  2. Online/concurrent PostgreSQL techniques are preferred where supported and justified.
  3. Deployment compatibility and rollback/forward-recovery evidence accompany risky changes.
  4. Maintenance pressure is observed under representative load when it can materially affect critical paths.
- **Failure behaviour:** Avoidable blocking downtime, unsafe lock duration, resource starvation or unrecoverable migration failure blocks release.
- **Security/privacy:** Performance fixtures avoid copying sensitive production identities solely for migration realism.
- **Performance/scaling:** Migration/maintenance evidence forms part of headroom and deployment-capacity planning.
- **Enforcement/downstream:** High-risk migration gate manifests reference representative pressure evidence.

## ARC-324 — Scale-sensitive proof data reproduces cardinality, skew, selectivity, relationship density and hot spots without requiring production identities

- **Decision source:** AR-009 V3.10
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-003`, `ARQ-PERF-071`, `ARQ-PERF-085`, `ARQ-AN-160`; cross-reference `ARC-306`, `ARC-314`
- **Decision:** Major query/load/performance proofs use synthetic, generated or otherwise safely prepared datasets that reproduce the material scale characteristics of the target workload, including cardinality, skew/distribution, selectivity, relationship density, historical depth and contention hot spots where relevant. Tiny fixtures alone are insufficient; sensitive production data is not copied merely for realism.
- **Rationale:** PostgreSQL planner choices, memory/I/O behaviour and contention can change materially as data size and distribution evolve.
- **Rules:**
  1. Data-generation assumptions and seed/version are captured with proof evidence.
  2. Referential/business-shape realism is preserved where it affects access patterns.
  3. Hot-key/skew scenarios are included where uniform distributions would hide contention.
  4. Production-derived data requires an independently approved privacy/security basis if ever used.
- **Failure behaviour:** A proof using materially unrealistic cardinality/distribution is inconclusive rather than accepted as scale evidence.
- **Security/privacy:** Synthetic/minimised datasets are the default for performance environments.
- **Performance/scaling:** Dataset version is part of benchmark reproducibility.
- **Enforcement/downstream:** Performance & Capacity Proof Matrix records dataset cardinality/distribution/version.

## ARC-325 — Analytics and experimentation participate in composite pressure proof without competing blindly with OLTP or bypassing validity gates

- **Decision source:** AR-009 V3.11
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-077`, `ARQ-AN-149`, `ARQ-AN-160`, `ARQ-AN-197`; cross-reference `ARC-179...ARC-188`, `ARC-277`, `ARC-307`, `ARC-314`
- **Decision:** Where material to the workload, composite proof includes representative analytical refresh/rebuild work, concurrent dashboard usage, large ranges, exports, backfills, pipeline lag/recovery and experiment-measurement health while measuring impact on OLTP. Analytical freshness may degrade within its governed SLO before critical transactional capacity is threatened. Statistical/experiment-validity blockers such as material unexplained sample-ratio mismatch remain blockers regardless of pipeline speed.
- **Rationale:** Analytics and experimentation are real production workloads, but they are downstream decision-support systems and may not steal capacity from authoritative critical work or manufacture valid conclusions from broken measurement.
- **Rules:**
  1. Analytical workloads use representative volume/cardinality and concurrency.
  2. OLTP impact is measured explicitly for heavy refresh/export/backfill scenarios.
  3. Freshness SLOs and hard integrity/statistical-validity gates remain distinct.
  4. Warehouse/CDC introduction remains evidence-gated rather than assumed by the test model.
- **Failure behaviour:** Unbounded analytical impact on critical OLTP, unreconciled pipeline corruption or invalid experiment-health state fails the relevant proof/gate.
- **Security/privacy:** Performance proof preserves analytics deletion/privacy/minimisation constraints.
- **Performance/scaling:** Results identify when PostgreSQL/read-model architecture remains sufficient versus when later isolation evidence is triggered.
- **Enforcement/downstream:** Analytics/experiment-heavy Feature Packs instantiate these composite pressure cases where applicable.

## ARC-326 — Architecture establishes a versioned Performance & Capacity Proof Matrix contract for all later reference-flow and Feature-Pack evidence

- **Decision source:** AR-009 V3.12
- **Status:** ACCEPTED
- **Source ARQs:** `ARQ-PERF-003`, `ARQ-PERF-020`, `ARQ-PERF-021`, `ARQ-PERF-022`, `ARQ-PERF-041`, `ARQ-PERF-160`; cross-reference `ARC-291...ARC-325`
- **Decision:** Every later governed Reference Flow Pressure Test, Architectural Proof and performance-sensitive Feature Pack instantiates a versioned Performance & Capacity Proof Matrix that records at least: reference flow/operation; workload profile/version; topology/node roles/counts; data cardinality/distribution; concurrency/arrival/connection envelope; latency/freshness/throughput budgets; hard invariants; resource budgets/headroom; dependency/failure conditions; required test classes; evidence/tool versions; pass/fail result; proven safe envelope/breakpoint; and known exclusions/unresolved gates.
- **Rationale:** A repeatable proof contract prevents each team/Feature Pack from redefining what “performance tested” means and preserves comparability across architectural evolution.
- **Rules:**
  1. The matrix is evidence metadata plus results, not one universal benchmark number.
  2. Scenario and dataset versions are immutable historical evidence once used for a decision; later changes create new versions.
  3. Exclusions require explicit workload-based rationale.
  4. Hard-invariant assertions and performance thresholds are reported separately.
  5. The proven safe envelope/breakpoint is tied to the tested topology/release, not treated as timeless capacity.
- **Failure behaviour:** Missing mandatory proof fields, invalid generator/data conditions or unresolved hard-invariant failures prevent a PASS conclusion.
- **Security/privacy:** Proof artifacts minimise sensitive data and preserve access/retention controls appropriate to operational evidence.
- **Performance/scaling:** This matrix is the canonical downstream vehicle for capacity/scaling evidence.
- **Enforcement/downstream:** Reference Flow Pressure Tests consume this contract before `03_ARCHITECTURE.md` is frozen; later Feature Pack gate manifests reference the applicable matrix version.

**V3 consolidated doctrine:** A topology is not proven because it is fast under clean load. It is proven only when it remains correct, bounded and recoverable under the adverse workload conditions the platform is designed to survive. Concurrency, duplicates, retries, scarcity, database contention, cache regeneration, backlog recovery, realtime storms, abuse controls, migration pressure and representative data are first-class proof dimensions.

**V3 deferrals:** Exact per-flow concurrency/arrival envelopes; concrete rate-limit library/backend and thresholds; exact migration timing thresholds; dataset generators/seeds; k6/distributed-generator topology; environment sizing; final load durations; and Feature-Pack-specific hard-invariant/test matrices remain Reference Flow/Domain/JIT/Feature Pack proof decisions. Architecture requires the proof contract and semantics, not speculative universal constants.

## ARC-327 — ARC-326 proof depth is staged: Phase 3 records proof obligations; executable stages record runtime evidence

- **Decision source:** Phase 3 Reference Flow efficiency correction accepted 2026-08-17; explicit timing/depth amendment to `ARC-326`
- **Status:** ACCEPTED_AMENDMENT
- **Amends:** `ARC-326` timing/depth only; the full Performance & Capacity Proof Matrix contract remains in force
- **Source ARQs:** `ARQ-PERF-003`, `ARQ-PERF-020`, `ARQ-PERF-021`, `ARQ-PERF-022`, `ARQ-PERF-041`, `ARQ-PERF-160`; cross-reference `ARC-291...ARC-326`
- **Decision:** The canonical Performance & Capacity Proof Matrix remains the required contract for executable performance/capacity evidence. Pre-implementation Reference Flow Pressure Tests use a **proof-obligation projection** rather than fabricating runtime evidence. At Phase 3 each flow records, at minimum: whether the flow is performance-sensitive; its material scale/resource concern; the hard performance/correctness invariant that later proof must attack; whether executable proof is required; and the downstream proof stage(s) that must instantiate the full matrix. Runtime-only fields such as measured topology capacity, representative cardinality, concurrency envelope, latency/throughput result, tool version, safe envelope and breakpoint are deferred until executable evidence can actually exist.
- **Rationale:** Phase 3 exists to prove architectural coherence across end-to-end flows, not to simulate Architectural Proof, Horizontal Hardening or Release testing before software exists. Requiring placeholder `NOT_YET_MEASURED` values creates ceremony without evidence while obscuring the genuinely useful question: whether the architecture can support the proof later.
- **Rules:**
  1. A Phase 3 flow does **not** need placeholder values for runtime-only matrix fields.
  2. A Phase 3 PASS means the required future proof is identifiable, architecturally possible and not contradicted by accepted law; it is not a measured production-capacity claim.
  3. The first applicable executable proof point — Architectural Proof, a performance-sensitive Feature Pack/slice, Horizontal Hardening or Release Gate — instantiates the full `ARC-326` matrix fields relevant to that path.
  4. Hard correctness invariants remain explicit in Phase 3 even when their executable concurrency/failure proof is deferred.
  5. If a pre-implementation architectural choice genuinely cannot be judged without targeted executable evidence, Phase 3 may mark that flow blocked for Architectural Proof rather than inventing a benchmark result.
  6. Later executable evidence remains versioned, topology/release-specific and governed by `ARC-326`; this amendment does not weaken any V1–V3 performance, contention, recovery or validity requirement.
- **Failure behaviour:** Phase 3 cannot PASS a flow if the required later proof cannot be identified, the architecture makes the required proof impossible, or a hard invariant lacks an architectural enforcement path. At executable proof stages, missing mandatory `ARC-326` evidence fields or failed hard invariants still prevent PASS.
- **Security/privacy:** Deferred runtime evidence does not defer security/privacy invariants. Phase 3 must still identify security-sensitive pressure concerns and later proof obligations without copying production participant data merely for realism.
- **Performance/scaling:** This amendment changes **when** evidence fields become mandatory, not **what** must eventually be proven. The full matrix remains the canonical downstream capacity/scaling evidence vehicle.
- **Enforcement/downstream:** `REFERENCE_FLOW_PRESSURE_TESTS_WORKING` uses the lean proof-obligation projection. Architectural Proof, affected Feature Packs/slices, Horizontal Hardening and Release Gates instantiate the full executable matrix when software and representative environments exist.
- **Amendment effect:** `ARC-326` remains preserved as accepted history. Where `ARC-326` can be read as requiring runtime-only evidence during pre-implementation Phase 3, `ARC-327` governs that timing interpretation. AR-009 remains COMPLETE through `ARC-326`; this is a post-closure proof-governance amendment, not an AR-009 reopening.

---

# 5. Change Log

## v0.35.0 — 2026-08-17 — Phase 3 proof-depth correction / ARC-326 timing amendment

- SemVer transition: `v0.34.0 → v0.35.0`.
- Added `ARC-327` as one narrow post-closure amendment to `ARC-326`.
- Preserved the full Performance & Capacity Proof Matrix as the canonical executable evidence contract while removing the requirement to populate runtime-only placeholder fields during pre-implementation Reference Flow Pressure Tests.
- Phase 3 now records a lean proof-obligation projection: performance sensitivity, material scale concern, hard invariant, need for later executable proof and applicable proof stage.
- Full workload/topology/cardinality/concurrency/latency/resource/tool/result/safe-envelope/breakpoint evidence remains mandatory when executable Architectural Proof, affected Feature Pack/slice, Horizontal Hardening or Release testing actually occurs.
- AR-009 remains COMPLETE through `ARC-326`; it was not reopened and no V4 was created.
- Phase 3 then completed in `REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`: FLOW-01...FLOW-12 all passed architecture pressure testing with 0 architecture gaps and 0 contradictions; the next stage is `03_ARCHITECTURE.md` synthesis/review/freeze.
- No Product Law, DEC, OQ, ARQ or prior ARC was changed.



## v0.34.0 — 2026-08-17 — AR-009 V3 Adversarial Proof Hardening + Final Closure

- SemVer transition: `v0.33.0 → v0.34.0`.
- Accepted all AR-009 V3.1–V3.12 recommendations and added `ARC-315` through `ARC-326`.
- Locked invariant-attacking contention proofs; zero-confirmed-oversell flash-sale proof; duplicate/retry storm testing; database lock/pool/query contention evidence; cold-cache anti-stampede proof; controlled backlog recovery; realtime reconnect/fan-out/node-loss pressure; distributed abuse-control pressure with non-enumeration; representative migration/maintenance pressure; synthetic representative scale data; analytics/experiment composite pressure without OLTP starvation; and the versioned Performance & Capacity Proof Matrix contract.
- Re-ran the complete AR-009 closure audit against **155 frozen ARQs routed through AR-009**: Performance 105; Analytics 47; Payments 1; Security 1; Operations 1. Result: **PASS**.
- Confirmed the remaining AR-009-routed requirements not newly named in V3 are already semantically closed by prior AR-001...AR-008 decisions plus V1/V2/V3, including realtime/degraded semantics, dashboard freshness/alerts, PostgreSQL/read-model-first analytics, warehouse/CDC evidence gates, experiment statistical governance/lifecycle and public experiment URL/cache rules. No V4 is required.
- Marked `AR-009 — Performance, Scaling & Multi-Node Behaviour` COMPLETE through `ARC-326`.
- **Architecture Decision workstreams AR-001 through AR-009 are now COMPLETE.** Advanced the governed next stage to **Reference Flow Pressure Tests**, which must instantiate the proof matrix against end-to-end flows before `03_ARCHITECTURE.md` is frozen.
- Updated current document/tracker pointers to `ARCHITECTURE_LAW_WORKING_v0.34.0.md` and `02_OPEN_WORK_v1.2.20.md`.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.

## v0.33.0 — 2026-08-17 — AR-009 V2 Capacity Budgets, Multi-Node Multipliers & Scaling Triggers

- SemVer transition: `v0.32.0 → v0.33.0`.
- Accepted all AR-009 V2.1–V2.12 recommendations and added `ARC-303` through `ARC-314`.
- Locked platform-wide PostgreSQL connection budgeting with operational reserve; evidence-gated transaction pooling; semantic query/index/plan budgets; evidence-driven read-scaling progression; empirical bounded LiveView connection envelopes; end-to-end realtime amplification proof; worker capacity inside shared DB/CPU/RAM/I/O/provider budgets; explicit multi-node pressure multipliers; resource-specific headroom; bottleneck-driven vertical/horizontal scaling; and composite topology pressure proof.
- Marked AR-009 IN PROGRESS through `ARC-314`; next round is `AR-009 V3 — contention/race proofs, flash-sale zero-oversell, backlog recovery, abuse pressure, migration/maintenance pressure, realistic test data and final proof matrix`.
- Updated current document/tracker pointers to `ARCHITECTURE_LAW_WORKING_v0.33.0.md` and `02_OPEN_WORK_v1.2.19.md`.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.

## v0.32.0 — 2026-08-17 — AR-009 V1 Workload Model, Performance Budgets & Verification Regime

- SemVer transition: `v0.31.0 → v0.32.0`.
- Accepted all AR-009 V1.1–V1.12 recommendations and added `ARC-291` through `ARC-302`.
- Locked reference-flow/workload-specific interpretation of the 100,000-user scale objective; distinct sustained/burst/scheduled/flash/abusive workload profiles; percentile latency evidence; initial semantic latency classes; current-official Core Web Vitals as the minimum frontend floor; end-to-end versus internal/provider latency decomposition; regression-blocking performance budgets; progressive smoke/load/stress/spike/breakpoint/soak/failure proof; layered test cadence; cold/restart/deployment/recovery-state testing; versioned pass/fail thresholds plus hard-invariant assertions; and load-generator validity/distribution rules.
- Marked AR-009 IN PROGRESS through `ARC-302`; next round is `AR-009 V2 — PostgreSQL/connection capacity, LiveView/process cost, worker/resource headroom, scaling triggers and multi-node pressure proof`.
- Updated current document/tracker pointers to `ARCHITECTURE_LAW_WORKING_v0.32.0.md` and `02_OPEN_WORK_v1.2.18.md`.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.

## v0.31.0 — 2026-08-17 — AR-008 O3 Operations Governance + Final Closure

- SemVer transition: `v0.30.0 → v0.31.0`.
- Accepted all AR-008 O3.1–O3.12 recommendations and added `ARC-279` through `ARC-290`.
- Locked impact/risk-based incident severity; named incident command with preserved specialist authority; containment-before-perfect-diagnosis; owned/versioned/exercised runbooks; evidence-based post-incident amendment/re-proof; cross-functional release no-go manifests; failure-injection maturity; complete service-boundary recovery proof; validated central runtime configuration; separate least-privilege secret handling; governed material configuration releases; and purpose/sensitivity-specific telemetry retention/access.
- Re-ran the complete AR-008 closure audit across **321 frozen ARQs routed through AR-008**: Performance 115; Analytics 184; Payments 1; IAM 5; State 6; Async 3; Content 3; Security 2; Operations 2. Result: **PASS**.
- Confirmed the abuse/upload-security residuals are already semantically covered by prior AR-003/004/006 law plus AR-008 operational controls; no O4 is required.
- Marked `AR-008 — Reliability, Deployment, Operations & Observability` COMPLETE through `ARC-290`.
- Advanced immediate Architecture Decision work to `AR-009 — Performance, Scaling & Multi-Node Behaviour`.
- Corrected current-document metadata pointers in this new version so the document version/filename and governing open-work source identify `v0.31.0` / `02_OPEN_WORK_v1.2.17.md`; no prior ARC semantics or historical changelog entries were modified.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.


## v0.30.0 — 2026-08-17 — AR-008 O2 Observability, SLO Evidence, Telemetry, Alerting & Incident Correlation

- SemVer transition: `v0.29.0 → v0.30.0`.
- Accepted all AR-008 O2.1–O2.12 recommendations and added `ARC-267` through `ARC-278`.
- Locked a coherent metrics/traces/structured-logs/domain-signal observability model; safe cross-boundary correlation context; bounded metric-cardinality governance; diagnostic logs separate from immutable audit evidence; vendor-neutral distributed tracing with controlled sampling; business-facing SLI/SLO evidence with non-budgetable correctness invariants; PostgreSQL/queue/realtime diagnostic coverage; domain outcome signals; actionable owned alerting; release/config/incident correlation; and failure-isolated lightweight telemetry/export.
- Marked AR-008 IN PROGRESS through `ARC-278`; next round is O3 incident severity/command, runbooks, cross-functional release gates, recovery/failure exercises, secrets/config operations and observability retention/access.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.


## v0.29.0 — 2026-08-17 — AR-008 O1 Runtime Failure, Health, Dependency Isolation & Safe Deployment

- SemVer transition: `v0.28.0 → v0.29.0`.
- Accepted all AR-008 O1.1–O1.12 recommendations and added `ARC-255` through `ARC-266`.
- Locked capability-specific availability/SLO classes; distinct startup/liveness/readiness/degraded semantics; dependency-aware health; bounded OTP supervision; overload-first backpressure/shedding; explicit deadline/retry/bulkhead ownership; fenced single PostgreSQL write authority; rolling adjacent-version compatibility; drain-before-terminate; rollback-or-forward-recovery; risk-proportional canary rollout; and privileged auditable emergency controls.
- Marked AR-008 IN PROGRESS through `ARC-266`; next round is O2 observability/SLO evidence/logs/metrics/traces/incident correlation/alert ownership/telemetry privacy.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.


## v0.28.0 — 2026-08-17 — AR-007 P2 Backup/Restore, Deletion Replay & Export Lifecycle

- SemVer transition: `v0.27.0 → v0.28.0`.
- Accepted all AR-007 P2.1–P2.12 recommendations and added `ARC-243` through `ARC-254`.
- Locked full recovery-authority scope beyond PostgreSQL; HA versus backup separation; encrypted-backup ageing with restore-time deletion suppression; independently recoverable deletion/withdrawal replay semantics; recovery-gated restore promotion; semantic restore verification; deletion-safe derived-model rebuild; class-specific RPO/RTO with hard non-resurrection; governed participant-export composition; execution-time export reauthorization; bounded temporary export artifacts with expiry/deletion; and strong assurance/audit/CSV-safety controls for sensitive exports.
- Re-ran the complete AR-007 closure audit against **51 frozen ARQs routed through AR-007**: Performance 12; Analytics 28; System 1; IAM 2; State 6; Content 1; Operations 1. Result: **PASS**.
- Marked `AR-007 — Privacy, Deletion, Backup & Restore` COMPLETE through `ARC-254` and advanced the next Architecture Decision workstream to `AR-008 — Reliability, Deployment, Operations & Observability`.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.

## v0.27.0 — 2026-08-17 — AR-007 P1 Privacy Lifecycle, Retention & Irreversible Deletion

- SemVer transition: `v0.26.0 → v0.27.0`.
- Accepted all AR-007 P1.1–P1.10 recommendations and added `ARC-233` through `ARC-242`.
- Locked separate business/data lifecycle dimensions; category/purpose-specific retention with expert-owned durations; durable idempotent cross-system deletion orchestration; representation-complete deletion verification; strict anonymisation versus pseudonymisation; isolated retained-by-obligation evidence; narrowly scoped legal holds; capability-owned deletion contracts; minimal non-reconstructive deletion/suppression evidence; and semantic separation of account closure, consent withdrawal and full deletion.
- Marked AR-007 IN PROGRESS and advanced immediate scope to P2 backup/restore deletion replay, recovery suppression, export lifecycle and deletion-safe restore testing.
- No Product Law, DEC, OQ, ARQ or prior ARC changed.

\n## v0.26.0 — 2026-08-17 — AR-006 C4 Messaging/Measurement/Integration + AR-006 Closure PASS\n\n- SemVer transition: `v0.25.0 → v0.26.0`.\n- Accepted all AR-006 C4.1–C4.10 recommendations and added `ARC-223` through `ARC-232`.\n- Locked governed versioned message templates with exact locale/version provenance; thin platform-owned channel adapters; sticky governed email/message A/B/n treatments; separation of delivery/engagement evidence from authoritative downstream conversion; minimum-data/current-permission scheduled and sensitive disclosure; acquisition evidence separate from attribution interpretation; consent-constrained measurement without covert fingerprinting; stable deduplicated outbound conversion identity; vendor reports as reconcilable external evidence rather than platform financial truth; and shared durable-consequence/bulkhead semantics for external integrations.\n- Re-ran the complete AR-006 closure audit against **66 frozen ARQs routed through AR-006**: Performance 16; Analytics 33; Payments 1; System 5; State 1; Async 3; Content 6; Security 1. Result: **PASS**.\n- Marked `AR-006 — Content, Translation, Media & External Integrations` COMPLETE through `ARC-232` and advanced the next Architecture Decision workstream to `AR-007 — Privacy, Deletion, Backup & Restore`.\n- Preserved exact content/template Resources, search implementation, provider selections/plans, consent UI, object layout, retention durations, retry/timeout constants, OQ-013/OQ-020/OQ-021 proof details and final Domain ownership for their proper downstream gates.\n- No Product Law, DEC, OQ, ARQ or prior ARC was modified.\n\n
## v0.25.0 — 2026-08-17 — AR-006 C3 Media, Live/Replay Delivery & Provider Boundaries

- SemVer transition: `v0.24.0 → v0.25.0`.
- Accepted all AR-006 C3.1–C3.12 recommendations and added `ARC-211` through `ARC-222`.
- Locked platform-owned media identity; source/derivative lineage; recovery-class durability for irreplaceable media; entitlement-checked bounded protected playback; platform-authoritative live-session access; capture-versus-replay-publication separation; separable recording/replay/promotional-use approval; governed caption/transcript/accessibility derivatives; external first-release production/streaming/transcoding with Restream/Cloudflare remaining proof-gated candidates; provider-evidence reconciliation; explicit provider delivery-degradation semantics; and a thin replaceable media/live provider adapter.
- Preserved exact provider plans, RTMPS/recording capabilities, object/bucket layout, retention durations, playback-token format, caption/transcript toolchain, recording workflow and adapter module/resource structure for OQ-020/OQ-021/AR-007/AR-008/AR-009/Domain Dossiers/JIT proof.
- Reaffirmed that provider output is not publication, media transport is not entitlement authority, captured recording/approved replay/public promotional clip are distinct governed states, and v1 does not build self-hosted RTMP/transcoding infrastructure.
- AR-006 remains IN PROGRESS pending the routed-ARQ closure audit; add a C4 only if that audit exposes a genuine uncovered mechanism.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.24.0 — 2026-08-17 — AR-006 C2 Discovery, Search, Personalisation, SEO & Experiment-Safe Delivery

- SemVer transition: `v0.23.0 → v0.24.0`.
- Accepted all AR-006 C2.1–C2.12 recommendations and added `ARC-199` through `ARC-210`.
- Locked search/discovery as derived navigation rather than authority; PostgreSQL-first/evidence-gated search infrastructure; minimum-data search projections; deterministic/explainable access-first ranking; minimum-signal health-derived personalisation; participant control with independent safety prominence; locale-specific canonical public routing; private/paid indexing separation; clean canonical experiment URLs; conservative variant-safe HTML caching; governed immutable content-version treatment references; and safe/default experiment delivery degradation.
- Preserved exact search engine/index/extension selection, route-prefix syntax, SEO header/sitemap implementation, personalisation signal schema, CDN/cache-key implementation and experiment-content Resource design for Domain Law/AR-008/AR-009/JIT proof.
- Corrected the top document-title filename metadata from a stale historical `v0.22.0` label to the actual emitted `ARCHITECTURE_LAW_WORKING_v0.24.0.md`; no prior ARC semantics or change-history entry was altered.
- AR-006 remains IN PROGRESS. Next planned round: `AR-006 C3 — Media Metadata, Live/Replay Delivery, Streaming/Transcoding Providers, Protected Playback & Provider Failure Boundaries`.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.23.0 — 2026-08-17 — AR-006 C1 Content Authority, Versioning, Translation & Publication

- SemVer transition: `v0.22.0 → v0.23.0`.
- Accepted all AR-006 C1.1–C1.10 recommendations and added `ARC-189` through `ARC-198`.
- Locked conceptual content identity with independently governed locale/version branches; Gettext-versus-managed-runtime-content boundary; immutable published versions; exact delivered-version provenance; independent language/authority approvals and derived readiness; content-class-governed locale fallback; explicit version-targeted publication; risk-driven governance; correction/supersession/withdrawal semantics; and semantic-contract-first deferral of exact Ash Resource/schema ownership to Domain Law/OQ-013/JIT design.
- Preserved the distinction between historical immutability and future eligibility: withdrawn versions may remain historical evidence while being prohibited from future use.
- Did not select exact content Resources/tables, approval role taxonomy, search engine, media/live provider, bucket layout, editorial UI or OQ-013 implementation-grade resource design.
- AR-006 remains IN PROGRESS. Next planned round: `AR-006 C2 — Discovery/Search/Feed, Personalisation, Multilingual SEO/Routing & Experiment-Safe Delivery`.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.22.0 — 2026-08-17 — AR-005 TC4 Analytics/Experiment Consistency + AR-005 Closure PASS

- SemVer transition: `v0.21.0 → v0.22.0`.
- Accepted all AR-005 TC4.1–TC4.10 recommendations and added `ARC-179` through `ARC-188`.
- Locked authoritative-origin business analytics facts; atomic/reconstructable analytics commit bridge; stable/versioned analytical event identity/time/provenance; idempotent late/reordered replay/backfill; platform-owned experiment governance behind a replaceable deterministic assignment adapter; sticky mutually-exclusive A/B/n allocation; assignment/exposure separation; concurrent-experiment isolation; immutable activated experiment versions; and safe analytics/experiment degradation.
- Re-ran the full AR-005 closure audit against **234** frozen ARQs routed through AR-005: Performance 106; Analytics 118; Payments 1; IAM 2; State 3; Async 3; Content 1. Result: **PASS**.
- Closed `AR-005 — Transactions, Consistency, Async & Realtime` and advanced the current Architecture Decision workstream to `AR-006 — Content, Translation, Media & External Integrations`.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.


## v0.21.0 — 2026-08-17 — AR-005 TC3 Provider Evidence, Notifications, Scheduling & Realtime Consistency

- SemVer transition: `v0.20.0 → v0.21.0`.
- Accepted all AR-005 TC3.1–TC3.12 recommendations and added `ARC-167` through `ARC-178`.
- Locked verify/durable-receipt/acknowledge/reconcile provider ingress; external-evidence-not-authority semantics; duplicate/order-independent provider reconciliation; notification truth/intent/delivery separation with policy revalidation and semantic deduplication; time-self-effective versus execution-gated scheduling; after-commit best-effort realtime observation; scoped/minimal PubSub routing; delay/missing/duplicate/reorder tolerance; amplification-aware refresh; and authoritative action/state as UI confirmation.
- Preserved Paystack-specific state-machine details, provider retry constants, final notification vendors/templates, exact PubSub topics, queue/timing values and Domain ownership for OQ-004/vendor proof, AR-006/008/009, Domain Law and JIT dossiers.
- Preliminary AR-005 closure audit checked 234 routed ARQs and found two residual mechanism clusters—analytics commit/replay and experiment assignment/exposure consistency—so one surgical TC4 is required before closure.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.




## v0.20.0 — 2026-08-17 — AR-005 TC2 Queue Isolation, Backpressure, Scheduling & Worker Topology

- SemVer transition: `v0.19.0 → v0.20.0`.
- Accepted all AR-005 TC2.1–TC2.11 recommendations and added `ARC-156` through `ARC-166`.
- Locked workload-characteristic queue isolation; priority-within-isolation; bottleneck-derived concurrency; explicit per-node versus strict-global concurrency semantics; bounded backlog/backpressure; error-class-aware bounded retry; coordinated dependency-outage degradation; dead-letter semantics without mandatory physical DLQ; separation of one-off/static-periodic/dynamic-business scheduling; bounded fan-out; and runtime-separable worker topology with graceful recovery-safe shutdown.
- Preserved final queue names/counts, concurrency numbers, SLOs, thresholds, batch sizes, retry constants, Oban Pro licensing/feature choices, global-limit mechanism, circuit-state implementation and worker host count for AR-008/009/JIT/proof work.
- AR-005 remains IN PROGRESS; next round is TC3 provider callbacks/reconciliation, notification consequences, scheduled business transitions and realtime/PubSub consistency.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.


## v0.19.0 — 2026-08-17 — AR-005 TC1 Transaction Commit & Durable Consequence Boundary

- SemVer transition: `v0.18.0 → v0.19.0`.
- Accepted all AR-005 TC1.1–TC1.10 recommendations and added `ARC-146` through `ARC-155`.
- Selected Oban as the default durable PostgreSQL-backed asynchronous executor, with AshOban as the preferred Ash-native integration candidate where resource actions fit naturally.
- Locked atomic durable consequence intent with authoritative commits; remote calls outside authoritative transactions; re-execution/idempotency doctrine; queue-uniqueness separation from business idempotency; minimal durable job payloads; causal provenance separate from execution authority; current-precondition revalidation; job-state/business-state separation; and semantic rather than universal use of separate outbox/consequence records.
- Preserved exact queue names, limits, retry schedules, plugins, worker topology, scheduler configuration, consequence schemas, provider-specific idempotency details and operational reconciliation tooling for TC2/AR-006/008/009/Domain Dossiers/JIT/proof work.
- AR-005 remains IN PROGRESS; next round is TC2 queue classes, concurrency/backpressure, scheduling, retry/dead-letter behaviour and multi-node worker topology.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.


## v0.18.0 — 2026-08-17 — AR-004 I4 Recovery/Compromise/Sessions/Abuse + AR-004 Closure PASS

- SemVer transition: `v0.17.0 → v0.18.0`.
- Accepted all AR-004 I4.1–I4.10 recommendations and added `ARC-136` through `ARC-145`.
- Locked graduated account recovery, high-risk identity changes, provenance-preserving duplicate-identity reconciliation, explicit compromise containment, individually revocable bounded sessions, secure opaque cookie transport, expiring/revocable trusted-device state, single-purpose bounded security capabilities, layered abuse controls and distributed-capable velocity state before multi-node traffic depends on it.
- Ran the AR-004 closure audit against all **119 frozen ARQs** whose downstream workstreams include AR-004: 16 Performance, 81 Analytics, 3 System, 8 IAM, 5 State, 1 Async, 3 Content, 1 Security and 1 Operations.
- Closure audit PASSED with no Product Law amendment, ARQ amendment, contradiction or I5 round required.
- Marked AR-004 COMPLETE with accepted AR-004 law `ARC-110...ARC-145`.
- Advanced the current workstream to `AR-005 — Transactions, Consistency, Async & Realtime`.
- Preserved exact schemas, MFA/session/token values, audit technology, rate thresholds, distributed coordination mechanism, recovery evidence and Domain-specific merge semantics for later work.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.


## v0.17.0 — 2026-08-17 — AR-004 I3 Consent, Privileged Authority, Audit & Revocation

- SemVer transition: `v0.16.0 → v0.17.0`.
- Accepted all AR-004 I3.1–I3.10 recommendations and added `ARC-126` through `ARC-135`.
- Locked purpose-specific consent/lawful-basis authority; append-only consent history plus current-effective projection; revocation dependency invalidation; least-privilege/time-bounded privileged elevation; governed break-glass; separate minimised immutable audit/security evidence; risk-based audit capture; non-enumerating sensitive public responses; minimum-safe external authorisation errors; and durable-revocation-first realtime propagation.
- Preserved exact consent/audit schemas, retention, privileged approval/break-glass implementation, revocation/outbox/session-disconnect mechanism, public error copy and rate-limit thresholds for I4/AR-005/007/008/009/Domain Law/JIT/proof work.
- AR-004 remains IN PROGRESS; next round is I4 identity recovery/merge, account compromise, device/session lifecycle and layered abuse controls.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.16.0 — 2026-08-17 — AR-004 I2 Roles, Capabilities, Relationships & Field Privacy

- SemVer transition: `v0.15.0 → v0.16.0`.
- Accepted all AR-004 I2.1–I2.8 recommendations and added `ARC-118` through `ARC-125`.
- Locked composable contextual authorisation rather than role-only RBAC; roles as contextual classifications rather than blanket keys; explicit durable scoped authority grants; practitioner/private-record relationship authority; Ash policy enforcement for actions/records; layered field privacy; purpose-specific writable action surfaces; and current-authority evaluation rather than session-frozen permissions.
- Preserved final role/capability vocabulary, permission/relationship/consent schemas, exact Ash policy modules, privileged approval/break-glass mechanics, audit storage and revocation propagation for I3/Domain Law/AR-005/007/008/JIT/proof work.
- AR-004 remains IN PROGRESS; next round is I3 consent modelling, privileged/break-glass authority, audit evidence, non-enumeration and revocation propagation.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.15.0 — 2026-08-17 — AR-004 I1 Identity, Authentication & Session Authority

- SemVer transition: `v0.14.0 → v0.15.0`.
- Accepted all AR-004 I1.1–I1.8 recommendations and added `ARC-110` through `ARC-117`.
- Locked canonical identity separate from roles/relationships; proof-gated AshAuthentication/AshAuthenticationPhoenix preference; email/password-first launch with non-auto-registering optional magic links; verified-email capability gating; individually revocable durable session authority; contextual MFA/step-up assurance; framework-independent mandatory MFA capability; and Argon2id password-hashing preference with benchmarked parameters.
- Preserved exact role/resource ownership, permission/consent schemas, MFA provider/factors, session/token/cookie representation, password-hash parameters, recovery UX and dependency versions for later AR-004/JIT/proof work.
- AR-004 remains IN PROGRESS; next round is I2 roles, capabilities, relationship-scoped authority and field-level privacy.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.14.0 — 2026-08-17 — AR-003 S5 accepted and State Authority, Persistence, Caching & Storage closed

- SemVer transition: `v0.13.0 → v0.14.0`.
- Accepted all AR-003 S5.1–S5.10 recommendations and added `ARC-100` through `ARC-109`.
- Locked safe-only browser-local persistence; public/safe browser caching; immutable/versioned public asset caching; opt-in shared CDN caching; initial bypass of shared full-page caching for experiment-sensitive HTML; policy-first protected-media delivery; explicit storage security/lifecycle classes; purge-as-freshness-only; residual-access contracts for issued protected delivery capabilities; and deletion discovery across client/CDN/object/derivative residue.
- Ran the AR-003 closure audit against all **240 frozen ARQs** whose downstream workstreams include AR-003: 68 Performance, 162 Analytics, 1 Payments, 2 System, 4 State, 2 Content and 1 Security.
- Closure audit PASSED with no Product Law amendment, ARQ amendment, contradiction or S6 round required.
- Marked AR-003 COMPLETE with accepted AR-003 law `ARC-059...ARC-109`.
- Advanced the current workstream to `AR-004 — Identity, Authentication, Authorisation & Field Privacy`.
- Preserved exact schemas, resource ownership, cache/provider configuration, retention durations, object topology and other properly downstream implementation/domain/proof decisions.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.13.0 — 2026-08-17 — S4 Identifier & Object-Recovery Refinements + Versioned Filename Governance

- SemVer transition: `v0.12.0 → v0.13.0`.
- Accepted the two explicit S4 refinements and added `ARC-098` through `ARC-099`.
- `ARC-098` explicitly amends `ARC-091`: UUIDv7 is now the default platform-generated internal opaque identifier type where no domain/protocol exception is justified; identifier identity remains separate from access secrets/capabilities.
- `ARC-099` locks PostgreSQL as the authoritative file manifest rather than a routine duplicate binary store, with storage-class-specific independent object replicas/recovery copies where justified.
- Resolved the S4 refinement-pending state; AR-003 now proceeds to S5 client/CDN/storage-class boundaries before closure audit.
- Added filename governance: every emitted cumulative architecture artifact carries its SemVer in the filename so versions do not collide and the latest version is unambiguous.
- No Product Law, DEC, OQ, ARQ or prior ARC meaning was silently changed; `ARC-091` is explicitly cross-marked as amended by `ARC-098`.

## v0.12.0 — 2026-08-17 — AR-003 S4 Object Storage, Upload Security & File Lifecycle

- SemVer transition: `v0.11.0 → v0.12.0`.
- Accepted all AR-003 S4.1–S4.11 recommendations and added `ARC-087` through `ARC-097`.
- Locked PostgreSQL file-metadata authority with S3-compatible binary storage; direct presigned uploads; quarantine/verification; risk-appropriate scanning/sanitisation; opaque non-sensitive object identities; protected short-lived signed delivery; durable deletion reconciliation; AshStorage+ReqS3 proof-gated preference; Wasabi provider-candidate status; retention-class-specific Object Lock; and explicit derivative lineage/lifecycle.
- Preserved exact bucket/prefix/key format, scanner packages, presign details, provider/region, dependency versions, retention values and derivative implementation for proof/AR-006/007/008/Domain Dossiers.
- Recorded two user-raised S4 refinements for explicit follow-up rather than silently changing the accepted ARC set: UUIDv7 as default internal opaque identifier, and independent binary replica/backup topology for selected storage classes.
- AR-003 remains IN PROGRESS.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.

## v0.11.0 — 2026-08-17 — AR-003 S3 Cache Consistency, Redis/ETS & Failure Semantics

- SemVer transition: `v0.10.0 → v0.11.0`.
- Accepted all AR-003 S3.1–S3.10 recommendations and added `ARC-077` through `ARC-086`.
- Locked semantics-first node-local caching; optional/evidence-gated Redis; version/invalidation/TTL cache consistency; PubSub as freshness acceleration only; anti-stampede requirements; semantic separation of evictable cache from correctness-sensitive coordination; explicit Redis outage modes; domain-derived TTLs; restricted `:persistent_term`; and empty-cache/cold-start correctness.
- Preserved exact cache library choice, Redis topology/database/key layout, eviction policy, TTL numbers, PubSub topics/adapter, anti-stampede implementation, warming plan and per-capability fallback details for AR-005/AR-008/AR-009/Domain Dossiers/JIT work.
- AR-003 remains IN PROGRESS; next round is S4 object storage, direct uploads, quarantine/scanning, signed delivery, deletion reconciliation and Wasabi/AshStorage/ReqS3 proof boundary.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.




## v0.10.0 — 2026-08-17 — AR-003 S2 PostgreSQL Concurrency, Transactions, Queries & Migrations

- SemVer transition: `v0.9.0 → v0.10.0`.
- Accepted all AR-003 S2.1–S2.9 recommendations and added `ARC-068` through `ARC-076`.
- Locked invariant-specific concurrency control; smallest coherent authoritative transaction boundaries; durable PostgreSQL enforcement for race-proof invariants; durable critical operation/idempotency evidence; bounded query doctrine; evidence-derived indexes; read-model/materialised-view/replica progression for stale-tolerant heavy reads; finite system-wide PostgreSQL connection budgeting; and reviewed expand/transition/contract-safe migration law.
- Preserved exact constraints, lock/isolation choices, idempotency schema/key retention, query implementations, index definitions, pool sizes/timeouts, PgBouncer introduction, materialised-view refresh design, migration executor and CI/CD details for AR-005/AR-008/AR-009/Domain Dossiers/JIT work.
- AR-003 remains IN PROGRESS; next round is S3 cache consistency, Redis/ETS semantics, invalidation, stampede protection and distributed-state failure behaviour.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.


## v0.9.0 — 2026-08-17 — AR-003 S1 Authority & State Placement Doctrine

- SemVer transition: `v0.8.0 → v0.9.0`.
- Accepted all AR-003 S1.1–S1.9 recommendations and added `ARC-059` through `ARC-067`.
- Locked explicit state classes; PostgreSQL structured authority; database + Ash defence-in-depth invariants; authoritative-vs-derived separation; evidence-gated caching; scope-based browser/CDN/ETS/Redis acceleration; empty-cache correctness; immutable/superseding historical records; separate business/data lifecycle; and an S3-compatible durable-file boundary with Wasabi/AshStorage/ReqS3 remaining proof-gated candidates.
- Preserved exact Resource/table/index/constraint names, cache keys/TTLs, cache library, Redis topology, object buckets/regions, dependency versions and record-specific lifecycle/version state machines for later Architecture/Domain/JIT work.
- AR-003 remains IN PROGRESS; next round is S2 PostgreSQL concurrency, transaction-safe persistence, query/index/read-model doctrine and migration compatibility.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.


## v0.8.0 — 2026-08-16 — AR-002 C4 accepted and Phoenix / LiveView / Ash / Code Boundaries closed

- SemVer transition: `v0.7.0 → v0.8.0`.
- Accepted all AR-002 C4.1–C4.8 recommendations and added `ARC-051` through `ARC-058`.
- Locked reconstructible LiveView authority boundaries, untrusted browser intent, PubSub-as-observation, durable-async separation, presentation-only component authority, controlled Ecto/SQL/manual Ash escape hatches and explicit invariant-preserving exception governance.
- Ran the AR-002 closure audit against all **103 frozen ARQs** whose downstream workstreams include AR-002. Audit PASSED.
- Marked AR-002 COMPLETE and advanced the Architecture Law working scope to `AR-003 — State Authority, Persistence, Caching & Storage`.
- Activated the previously preserved AR-003/AR-006 S3-compatible object-storage proof inputs for downstream consideration without locking Wasabi/AshStorage/ReqS3 as final dependencies.
- No Product Law, DEC, OQ, ARQ or prior ARC was modified.


## v0.7.0 — 2026-08-16 — AR-002 C3 Resource Boundaries & Dependency Direction

- SemVer transition: `v0.6.0 → v0.7.0`.
- Accepted all AR-002 C3.1–C3.8 recommendations and added `ARC-043` through `ARC-050`.
- Locked business-semantic Ash Resource boundaries, proportional use of pure Elixir, focused Ash DSL/callback modules, owner-interface cross-boundary interaction, relationship-without-ownership-transfer, inward application dependency direction, no shared business-law dumping ground, and explicit resolution of circular authority/control dependencies.
- Preserved final concrete Domain names/owners, Resource inventory, persistence schema, exact module/folder structure, cross-domain event topology and provider adapters for Domain Law/AR-003/AR-005/AR-006/JIT Dossiers.
- No Product Law, DEC, OQ, ARQ or existing ARC was modified.


## v0.6.0 — 2026-08-16 — AR-002 C2 Actor Propagation, Policy Enforcement & Field Privacy

- SemVer transition: `v0.5.0 → v0.6.0`.
- Accepted all AR-002 C2.1–C2.8 recommendations and added `ARC-035` through `ARC-042`.
- Locked explicit actor/context propagation, default-on governed Ash authorisation, deliberate anonymous/system actors with separate causation, composable relationship/purpose/scope/time policy facts, field-policy + minimum-data defence in depth, current-policy re-evaluation for long-lived LiveViews, no universal Super Admin bypass, and bounded sensitive-data loading.
- Preserved exact authentication packages, actor structs, policy code, session representation, MFA/revocation mechanisms, audit storage and final role/domain ownership for AR-004/AR-005/AR-008/Domain Law.
- No Product Law, DEC, OQ, ARQ or existing ARC was modified.



## v0.5.0 — 2026-08-16 — AR-002 C1 Application Authority & Call Flow

- SemVer transition: `v0.4.0 → v0.5.0`.
- Accepted all AR-002 C1.1–C1.8 recommendations and added `ARC-027` through `ARC-034`.
- Locked Ash actions as the normal authoritative application-operation boundary; thin Phoenix/LiveView delivery semantics; no ordinary direct Repo second business API; Ash.Domain as the framework expression of later-approved Domain Law; code-interface-first internal calls; AshPhoenix.Form preference for Ash-backed forms; proportional ordinary-Elixir vs Ash orchestration; and no speculative REST/GraphQL launch surface.
- Preserved final concrete business-domain ownership for `04_DOMAIN_MAP.md`.
- Did not select authentication packages, concrete policies, final Ash Domains/Resources, tables, APIs, worker/transaction mechanisms or implementation folders.
- No Product Law, DEC, OQ, ARQ or AR-001 ARC was modified.


## v0.4.0 — 2026-08-16 — AR-001 T3 accepted and System Shape & Runtime Topology closed

- SemVer transition: `v0.3.0 → v0.4.0`.
- Accepted all AR-001 T3.1–T3.8 recommendations and added `ARC-019` through `ARC-026`.
- Locked the honest single-active-failure-domain launch model, private internal/state networking, Cloudflare-origin minimisation principle, environment isolation, evidence-gated horizontal scaling, independently movable PostgreSQL topology, Railway↔VPS infrastructure portability and the AR-001 topology-law stop boundary.
- Ran the AR-001 closure audit against all 37 frozen ARQs routed to AR-001. Audit PASSED.
- Marked AR-001 COMPLETE and advanced the Architecture Law working scope to `AR-002 — Phoenix / LiveView / Ash / Code Boundaries`.
- Preserved the accepted AR-003/AR-006 object-storage proof inputs unchanged.
- No Product Law, DEC, OQ or ARQ was modified.


## v0.3.0 — 2026-08-16 — Deferred object-storage architecture/proof inputs

- SemVer transition: `v0.2.0 → v0.3.0`.
- Recorded the user's accepted Wasabi/S3/AshStorage/ReqS3 architectural recommendations as downstream AR-003/AR-006 proof inputs, not AR-001 topology decisions or dependency/provider locks.
- Added the S3-compatible storage boundary, Wasabi candidate status, AshStorage/ReqS3 preferred proof path, no-unnecessary-parallel-S3-stack rule, Waffle fallback status, direct-to-quarantine upload principle, complete file-lifecycle/deletion reconciliation, ephemeral-vs-durable storage separation and bounded object-store HTTP concurrency.
- Added explicit proof questions for provider compatibility, privacy/location, upload security, deletion reconciliation, economics, concurrency and portability.
- No Product Law, DEC, OQ, ARQ or existing ARC was modified.


## v0.2.0 — 2026-08-16 — AR-001 T2 Deployment & Infrastructure Topology

- SemVer transition: `v0.1.0 → v0.2.0`.
- Accepted all AR-001 T2.1–T2.9 recommendations.
- Added `ARC-010` through `ARC-018`.
- Locked a portable OCI/Phoenix Release artifact, Cloudflare common edge, logically independent PostgreSQL service, optional/evidence-gated Redis, external object storage for durable media/uploads, single-steady-instance safe deployment with temporary version overlap, startup/liveness/readiness separation, runtime-injected configuration/secrets, and same-primary-location placement for latency-sensitive state services.
- Preserved the single-instance Railway-or-South-African-VPS launch posture; no cluster or permanent second application instance is introduced by T2.
- Did not lock provider, orchestrator, exact Cloudflare rules, database product, Redis topology, object-storage vendor, secret manager, CI/CD vendor, or Kubernetes.
- No Product Law, DEC, OQ or ARQ was modified.

## v0.1.0 — 2026-08-16 — AR-001 T1 Core Runtime Shape

- Started the cumulative Architecture Law working register after AR-000 v1.0.0 freeze.
- Accepted AR-001 T1.1–T1.9 recommendations.
- Applied the user's explicit deployment refinement: launch with one Railway or South-African-VPS application instance, not a cluster/multi-node topology from day one.
- Locked modular-monolith-first architecture, logical controlled product spaces, single-instance launch with future replica compatibility, affinity-independent correctness, cluster-on-scale rather than cluster-at-launch, combined web/worker launch role with later separation, ephemeral-compute/durable-authority separation, one-primary-location launch, and evidence-gated service extraction.
- Recorded current Railway region limitations as temporary vendor evidence, not Architecture/Product Law permanence.
- No Product Law, DEC, OQ or ARQ was modified.
