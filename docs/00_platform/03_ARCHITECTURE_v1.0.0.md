# 03_ARCHITECTURE_v1.0.0.md

- **Document status:** FROZEN / COMPLETE ARCHITECTURE SYNTHESIS
- **Document version:** v1.0.0
- **Previous working version:** `archive/03_ARCHITECTURE_WORKING_v0.1.0.md`
- **Last updated:** 2026-08-17
- **Purpose:** Synthesize accepted Product/Requirement/Architecture Law into a concise engineering architecture that can govern Domain Map and later delivery planning.
- **Derived from:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`, `00_PLATFORM_v1.2.1.md`, `01_DECISIONS_v1.2.1.md`, `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`, `reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md`, `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`, `02_OPEN_WORK_v1.2.27.md`
- **Architecture Law coverage:** `ARC-001...ARC-327` — 327/327 contiguous and represented
- **Frozen ARQ coverage:** 417/417 requirements preserved through the accepted Architecture Law; all 10 requirement families represented in this synthesis
- **Reference Flow coverage:** `FLOW-01...FLOW-12` — 12/12 traceability PASS; no flow rerun required
- **Authority rule:** This document is the authoritative **synthesis** of accepted Architecture Law for normal engineering consumption. If this synthesis conflicts with an active `ARC-*` decision, the active Architecture Law register wins and this frozen synthesis must be explicitly corrected/versioned. This document does not silently amend Architecture Law.
- **Phase 4 closure:** PASS — consistency, security/privacy, failure/recovery, performance/scaling, anti-overengineering, ARC/ARQ-family coverage, flow traceability and Domain Map readiness checks complete
- **Implementation status:** STOPPED. Architecture freeze advances planning to Phase 5; this document does not authorise production implementation.

---

# 1. Document Authority & Purpose

`03_ARCHITECTURE` is the platform's operating architecture constitution. It turns the detailed legislative record in `reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md` into a usable set of doctrines and boundaries.

The governing chain remains:

```text
Frozen Product Law
        ↓
AR-000 requirements — WHAT must be true
        ↓
ARC-001...ARC-327 — HOW architecture makes it true
        ↓
03_ARCHITECTURE — coherent engineering synthesis
        ↓
04_DOMAIN_MAP — WHO owns concrete business truth
        ↓
Domain Profiles / Roadmap / Feature Packs / JIT Dossiers
        ↓
Architectural Proof / Vertical Slices / Hardening / Release
```

This document **does** define platform mechanisms, authority boundaries, interaction rules, failure semantics, security/privacy doctrine, scaling doctrine and architectural enforcement expectations already accepted in Architecture Law.

This document **does not** define final Domains, Ash Resource names, database tables/columns, concrete indexes, Redis key formats, TTL values, PubSub topics, Oban queue names, GenServer modules, UI components, exact provider configuration, implementation code or delivery sequencing beyond the already-governed phase handoff.

---

# 2. Architecture Executive Summary

The platform begins as one modular Elixir/Phoenix/Ash application and one release family. Product spaces are logical experience/activation boundaries inside the common platform, not independent tenants or deployments by default.

Launch topology is deliberately simple:

- one application instance / one BEAM node;
- Phoenix + LiveView for delivery and interaction;
- Ash 3.x actions/code interfaces as the normal authoritative application-operation boundary;
- PostgreSQL as the default durable structured business authority;
- Oban as the default durable asynchronous executor;
- Phoenix PubSub for realtime observation/freshness, never durable truth;
- S3-compatible object storage for durable binary objects, with PostgreSQL governing business metadata/control;
- Cloudflare as the intended public edge;
- Redis and ETS only where a justified workload needs distributed or node-local acceleration/coordination;
- web and worker responsibilities combined initially, separable later from the same release;
- external providers behind platform-owned capability boundaries.

The architecture is horizontally correct from the beginning even though launch infrastructure is not horizontally replicated. No hard business invariant may depend on permanent single-node locality, sticky load-balancer affinity, LiveView process memory, ETS, PubSub delivery or provider dashboards.

The scaling doctrine is evidence-driven:

```text
correct bounded design
→ optimise query/transaction/data shapes
→ vertical capacity
→ justified local/shared acceleration
→ additional application replicas
→ web/worker separation where needed
→ read scaling / transaction pooling where evidence requires
→ specialist infrastructure or service extraction only when demonstrated
```

The durability doctrine is:

> **Authority before projection. Durability before convenience. Current policy before delivery.**

The degradation doctrine is:

> Correct refusal, bounded waiting or reduced freshness is preferable to fabricated success or weakened correctness.

Correctness, clinical/safety truth, privacy/security, payment/entitlement/accounting truth and confirmed capacity/inventory truth outrank latency, freshness, convenience, analytics and UI polish.

**Supporting Architecture Law:** `ARC-001...ARC-327`.

---

# 3. System Context & Runtime Topology

## 3.1 Logical context

```text
                         PUBLIC INTERNET
                               │
                          Cloudflare
                 DNS / edge / approved controls
                               │
                    approved public ingress
                               │
              ┌──────────────────────────────┐
              │ Elixir / Phoenix / Ash app   │
              │                              │
              │ Phoenix / LiveView           │
              │ Ash application operations   │
              │ Oban execution               │
              │ PubSub observations          │
              └──────────────┬───────────────┘
                             │
          ┌──────────────────┼───────────────────┐
          │                  │                   │
     PostgreSQL        optional Redis      object storage
 durable structured     acceleration /     durable binary
     authority          coordination         objects
          │                                      │
          └──────────────────┬───────────────────┘
                             │
                    external providers
              payment / email / media / etc.
               behind capability adapters
```

## 3.2 Launch topology

Launch uses one active application instance in one primary location. That explicitly accepts one active runtime failure domain; it is not presented as high availability. PostgreSQL is logically independent from application compute even when physical co-location is temporarily economical. Durable object storage is external to the application filesystem.

Application compute is replaceable. Process-local memory, LiveView/socket state, ETS/cache state and temporary local disk are not durable business authority. Restart or node replacement may reduce availability/freshness but cannot fabricate, erase or redefine committed truth.

Only approved ingress is public. PostgreSQL, Redis and other internal state services remain private/restricted. Production, non-production and local development are separate runtime/data/security boundaries.

## 3.3 Deployment and evolution

The production artifact is one portable OCI-compatible image containing an Elixir/Phoenix release. Environment-specific configuration and secrets are injected and validated at runtime. Production deployments may use temporary adjacent-version overlap to prove readiness and drain the previous instance; steady-state launch remains one application instance.

Adjacent releases must remain compatible with state/schema/job contracts during the approved deployment window. Every production change requires either a rollback path or explicit forward-recovery path.

When evidence requires additional capacity or availability, the same release may add application replicas and later separate web/worker runtime roles. Same-region BEAM clustering may then support distributed Phoenix capabilities where justified. Session affinity is never a correctness dependency. Adding nodes requires proof that shared-resource pressure remains safe.

Independent service extraction is a later explicit architecture amendment and requires demonstrated independent scaling, failure-isolation, deployment-cadence, security or technology need. Domain/team boundaries alone do not justify microservices.

**Supporting Architecture Law:** `ARC-001...ARC-026`, `ARC-255...ARC-266`, `ARC-303...ARC-314`.

**Material downstream gates:** hosting/provider selection; `OQ-037` class-specific RPO/RTO; deployment/secret implementation details remain downstream.

---

# 4. Application & Framework Boundaries

The application call flow is deliberately layered:

```text
browser / caller intent
        ↓
Phoenix / LiveView interaction boundary
        ↓
Ash code interface / authoritative Ash action
        ↓
policy + validation + application orchestration
        ↓
authoritative state / durable consequence
        ↓
response / projection / observation
```

## 4.1 Phoenix and LiveView

Phoenix and LiveView own delivery, interaction and presentation workflow. LiveView assigns are reconstructible projections, not durable business truth. Browser and LiveView event parameters are untrusted intent. Long-lived LiveViews re-evaluate current authority for authoritative operations rather than treating mount-time access as permanent permission.

LiveView-native async work is suitable for bounded UI work only. Durable or critical obligations must leave the LiveView process and use the governed application/async boundary.

Phoenix components compose presentation and interaction; they do not become independent business-authority layers.

## 4.2 Ash application authority

Ash actions are the normal authoritative business/application-operation boundary. Callers prefer code interfaces rather than scattered low-level action construction. Authorisation is default-on. Actor and application context are explicit through the call chain.

Ash resources model coherent application/business resources, not database tables or screens. The final set of Resources and Domains is not defined here; `04_DOMAIN_MAP` owns concrete business ownership and later JIT dossiers own implementation-grade resource design.

AshPhoenix.Form is preferred where forms directly represent Ash-backed application operations. UI-only forms may remain ordinary Phoenix forms.

## 4.3 Ordinary Elixir and controlled escape hatches

Pure deterministic calculations/rules remain ordinary Elixir when Ash semantics are unnecessary. Substantial behaviour should not be buried inside oversized validations/changes/preparations/calculations merely to keep everything inside one framework hook.

Direct Ecto/SQL is a controlled read/infrastructure escape hatch, never a second ordinary business-write API. Supported Ash extension/manual-action mechanisms are preferred before dropping below the application contract. Any escape hatch must be explicit, bounded and preserve the same invariants/policies.

Do not build speculative REST/GraphQL surfaces merely for architectural appearance. External adapters may be added later around the same application contracts.

**Supporting Architecture Law:** `ARC-027...ARC-058`.

---

# 5. Domain Interaction Doctrine

`03_ARCHITECTURE` defines interaction law but deliberately does not assign concrete business ownership.

The rules inherited by `04_DOMAIN_MAP` are:

1. Each durable business truth has one authoritative owner.
2. Cross-boundary writes call the owning application/domain interface; they do not directly mutate another boundary's persistence.
3. Relationships permit governed navigation/read composition but do not transfer mutation authority.
4. Shared technical primitives are acceptable; shared business-semantic dumping grounds are not.
5. Circular business authority/control dependencies are architectural defects and must be resolved explicitly.
6. Synchronous multi-step operations stay behind an authoritative application boundary when one atomic operation is required.
7. Cross-boundary consequences that may occur after commit use durable intent/execution semantics rather than hidden synchronous coupling.
8. Read projections may combine data for usability/performance without becoming write authority.
9. Domain boundaries remain internal module/application boundaries by default; they do not imply network services.

`04_DOMAIN_MAP` may decide **WHO owns** concrete identity, payment, entitlement, health, plan, programme, experiment or other truth. It may not invent a competing transaction model, cache authority model, async mechanism, provider-authority model or privacy model.

**Supporting Architecture Law:** principally `ARC-030`, `ARC-043...ARC-050`, with transaction/async reinforcement in `ARC-146...ARC-188`.

---

# 6. Identity, Authentication, Authorisation & Field Privacy

## 6.1 Canonical identity and authentication

The platform has one canonical platform identity distinct from roles and business relationships. Launch authentication is email/password first with optional magic-link capability where appropriate; these are authentication methods around one identity model, not separate identities.

Email verification is a capability gate rather than a blanket inability to authenticate. Sessions are individually identifiable, revocable, server-governed security objects with bounded lifetime. First-party web session credentials use secure opaque cookie transport by default.

Authentication assurance is contextual. The platform supports MFA and step-up for higher-risk actions; exact package configuration remains proof/JIT work. Argon2id is the preferred password-hashing direction with benchmarked cost parameters. Anonymous, participant and system execution contexts are deliberate; executing system authority is kept distinct from the human/business causation that initiated an operation.

## 6.2 Authorisation

Authorisation composes role/capability with relationship, purpose, scope, expiry and current authoritative state. Roles classify people; they do not grant unrelated blanket permissions.

Material authority grants are explicit, durable, scoped assignments with governed lifecycle. Practitioner/private-record access depends on an explicit governed relationship, not practitioner role alone.

Ash policies are the normal action/record authorisation boundary. Purpose-specific actions restrict writable inputs and protected transitions. Sensitive field visibility uses explicit field policies plus minimum-data loading and safe redaction.

Session identity/assurance context may be stable, but revocable permission is resolved from current server state when authoritative action occurs.

## 6.3 Consent, privileged access and revocation

Consent/lawful-basis authority is purpose-specific. Consent history is append-only evidence with an efficient current-effective-state representation. Material revocation is an authoritative transition and triggers dependent invalidation obligations.

Privileged authority is named, least-privilege, scoped and preferably time-bounded. There is no universal Super Admin bypass. Break-glass is a distinct exceptional elevation path requiring strong assurance, reason/scope/expiry/evidence/alert/review semantics.

Audit/security evidence is governed separately from generic operational logs.

## 6.4 Recovery, compromise and abuse

Account recovery is risk-proportional and restores identity control; it never manufactures unrelated business authority. Sensitive credential/identity changes are high-risk transitions. Duplicate-identity merge is governed reconciliation, not destructive row collapse. Compromise handling includes explicit containment and session/revocation powers.

Reset, confirmation, magic-link and recovery capabilities are single-purpose, bounded and replay-controlled.

Abuse protection is layered, risk-aware and recoverable. Public responses on sensitive auth/recovery/redemption surfaces remain non-enumerating while internal evidence remains precise. Platform-wide velocity controls require distributed-capable state before multi-node traffic depends on them. Edge and application controls complement one another; exact thresholds, challenge rules and package/backend choices remain downstream.

**Supporting Architecture Law:** `ARC-035...ARC-042`, `ARC-110...ARC-145`.

**Material downstream gates:** `OQ-034` authentication implementation architecture; `OQ-035` abuse thresholds/recovery; expert/legal/privacy gates where applicable.

---

# 7. State Authority, Storage & Acceleration

## 7.1 Authority matrix

| State/representation | Authoritative boundary | Optional acceleration / projection |
|---|---|---|
| Durable structured business state | PostgreSQL by default | bounded read projections, ETS/Redis where justified |
| Sensitive health/private records | PostgreSQL under current policy | minimum safe derived state only |
| Durable binary objects | S3-compatible object storage; PostgreSQL governs metadata/control | approved CDN/browser delivery where safe |
| Durable async execution intent/jobs | authoritative transaction + PostgreSQL-backed durable intent/Oban | queue runtime state is operational only |
| LiveView UI/workflow state | no durable authority | LiveView process assigns |
| Realtime freshness | authoritative state elsewhere | Phoenix PubSub |
| Rebuildable node-local lookup/cache | authoritative state elsewhere | ETS / cache abstraction where justified |
| Shared velocity/temporary coordination | explicitly declared mechanism/contract | Redis where justified; never silent business authority |
| Search/discovery | governed content/business authority elsewhere | PostgreSQL-backed search/read projection first |
| Analytics/experimentation readouts | authoritative facts + governed derived models | materialised/cached aggregates, later isolation if evidenced |

Core rule:

> **Authority ≠ acceleration.**

## 7.2 PostgreSQL

PostgreSQL is the default durable authority for structured business state. Business validation and database-enforceable invariants use defence in depth. Material historical truth is preserved through immutable/versioned or superseding records where required rather than destructive overwrite; authoritative write state remains distinct from derived/read state. Concurrency control is selected by the invariant: atomic mutation, uniqueness, optimistic checks, row locking, transaction isolation or another proven PostgreSQL mechanism as appropriate.

Transactions cover the smallest coherent authoritative transition and remain short. Critical operation/idempotency evidence is durable when crash recovery/reconciliation depends on it.

Application queries are bounded and deliberate from introduction. Indexes derive from integrity constraints and real access patterns, not generic indexing folklore. PostgreSQL connections are a finite platform-wide capacity budget.

Migrations are production code and must remain safe under adjacent-version deployment. Read scaling begins with correct bounded queries/projections and only later introduces replicas for explicitly stale-tolerant reads when evidence justifies them. UUIDv7 is the default internal opaque identifier type; it is an identifier, not a bearer secret or access-control mechanism.

## 7.3 Caching, ETS and Redis

Caching is evidence-gated. Empty-cache correctness is mandatory.

Node-local cache semantics are decided before selecting raw ETS, Cachex or another library. ETS is appropriate for reconstructible node-local acceleration. `:persistent_term` is restricted to near-immutable, very read-heavy VM-wide values whose update cost is acceptable.

Redis is optional shared acceleration/coordination infrastructure. Each Redis use declares purpose, authority boundary, lifecycle, eviction/persistence assumptions, and failure mode: authoritative fallback, explicit degraded/queued behaviour, or fail-closed behaviour where a correctness-sensitive temporary protocol requires it.

Cache freshness uses authoritative identity/version, explicit invalidation and bounded TTL where semantics justify it. TTL is not the sole correctness mechanism for material safety, security, entitlement, payment or capacity truth. PubSub can accelerate invalidation/freshness but cannot establish correctness. High-fanout regeneration requires anti-stampede protection.

## 7.4 Object storage, browser and CDN

PostgreSQL owns governed file metadata/control; S3-compatible storage owns durable bytes. Durable uploads do not depend on application local disk. Suitable browser-to-object-storage uploads may be direct/presigned but land restricted/untrusted until validation/safety gates pass.

Protected downloads/playback authorise current access first and then issue bounded delivery capability. Object keys are opaque and non-sensitive. Derivatives retain source lineage and lifecycle. Physical deletion is durable, retryable, observable and reconcilable.

Browser-local persistence is restricted to explicitly safe non-authoritative convenience state. Public immutable assets may be aggressively cached. Shared caching of dynamic/authenticated/personalised responses is opt-in by response class. Experiment-sensitive HTML bypasses shared full-page caching unless variant-safe partitioning is explicitly proven.

**Supporting Architecture Law:** `ARC-059...ARC-109`.

**Material downstream gates:** `OQ-014` exact edge/cache design; `OQ-039` domain/action performance mapping; exact object-store/attachment stack remains proof/JIT where not already accepted as candidate direction.

---

# 8. Transactions, Consistency, Idempotency & Durable Async

The platform uses three distinct consequence classes.

## 8.1 Class A — authoritative synchronous work

An authoritative action performs the smallest coherent durable transition and returns from authoritative state. Slow provider/network I/O is not performed while holding authoritative database locks/transactions.

Critical invariants must survive duplicate, simultaneous, reordered, retried and partially failed execution. Important external mutations have business-scoped durable idempotency where repeated delivery could multiply durable effects.

## 8.2 Class B — mandatory durable asynchronous consequence

For a must-not-lose consequence:

```text
authoritative transaction
→ establish durable execution intent atomically
→ commit
→ Oban executes consequence
→ repeat-safe/idempotent handler
→ current preconditions re-read/revalidated
→ success / retry / terminal-visible state
```

A transactional Oban job is sufficient where it fully represents the durable intent. A separate outbox/consequence resource is used only when independent lifecycle, audit, fan-out or reconciliation semantics require it; there is no generic outbox by fashion.

Oban is execution machinery, not business truth. Queue uniqueness suppresses duplicate work but does not replace business idempotency. Payloads remain small/stable/minimised. Causal provenance is preserved separately from the current execution authority.

Queues are isolated by workload/dependency/resource/failure/freshness semantics rather than by arbitrary domain names. Worker concurrency is budgeted against the tightest DB/CPU/RAM/I/O/provider limit. Backlogs are bounded operational buffers; retry budgets are error-class-aware, bounded and jittered. Shared dependency outages trigger coordinated degradation rather than worker herds.

Scheduling semantics are explicit: one-off execution, static periodic platform work and dynamic business-effective schedules are different concepts. Static periodic schedules may use the durable job scheduler; dynamic business schedules remain governed business state. Time-self-effective state is distinguished from transitions that require an execution action at the effective time.

## 8.3 Provider ingress and reconciliation

Provider callbacks follow:

```text
verify authenticity
→ durably receive evidence
→ commit
→ acknowledge provider
→ reconcile asynchronously
```

Provider callbacks/status are authenticated external evidence, not platform payment/entitlement/business authority. Duplicate or reordered delivery is normal. Ambiguous irreversible provider outcomes remain pending/unresolved and reconcile before repeating the irreversible effect.

## 8.4 Class C — ephemeral observation

Realtime notifications of already-committed change are best-effort observations. They may be delayed, missing, duplicated or reordered. Mandatory delivery is Class B, not PubSub.

**Supporting Architecture Law:** `ARC-068...ARC-071`, `ARC-146...ARC-178`; analytics/experiment consistency `ARC-179...ARC-188`.

---

# 9. Realtime Architecture

Realtime is an observation/freshness layer over authoritative state.

```text
authoritative Ash action commits
        ↓
optional post-commit PubSub observation
        ↓
LiveView receives narrow scoped signal
        ↓
refresh / reconcile from authoritative or approved projection state
        ↓
render current authorised UI
```

A user receives confirmation from the authoritative action/returned state, not from waiting for a PubSub echo.

PubSub topics are narrow routing boundaries; knowing a topic never grants access. Realtime consumers assume missing, duplicate, late and reordered observations. Refresh strategy is selected to bound fan-out and database/render amplification.

Loss of a socket, PubSub message or node may reduce freshness or require reconnect/rebuild. It cannot lose committed business truth. Reconnects re-authorise relevant state/action access.

At scale, realtime proof covers connection populations, connect/reconnect storms, broadcast bursts, slow clients, node loss, rolling deployment, mailbox/process memory, CPU, DB amplification and network/render cost. Freshness may degrade before durable correctness.

**Supporting Architecture Law:** `ARC-004...ARC-005`, `ARC-051...ARC-054`, `ARC-174...ARC-178`, `ARC-308...ARC-309`, `ARC-321`.

---

# 10. Content, Translation, Search, Media, Messaging & External Integrations

## 10.1 Governed content and translation

Governed runtime content has one conceptual identity with independently versioned locale branches. Gettext owns relatively static interface/system strings; editorial/legal/clinical/business runtime content is Ash-backed governed content.

Published/activated governed versions are immutable evidence. Material edits create new versions; corrections use explicit supersession/withdrawal. Delivery of paid, personalised or governed output retains exact content/locale provenance.

Locale approval is independent. Critical paid/safety/legal content does not silently fall back to an unapproved translation or machine translation. Publication activates a specific approved locale/version; latest, approved and published are distinct states. Risk classification determines approval/correction/withdrawal requirements.

## 10.2 Search, discovery, personalisation and SEO

Search/discovery is a derived navigation capability, never publication/access authority. Start with PostgreSQL-backed search/read projections where sufficient. Dedicated search infrastructure is evidence-gated.

Search indexes/projections contain the minimum safe discovery fields plus explicit access/publication metadata. Ranking is deterministic/explainable and access-first; semantic/vector ranking may later be a secondary governed signal.

Health-related personalisation crosses a minimum-signal relevance boundary; raw detailed clinical records are not copied into feed/search infrastructure by default.

Public multilingual content uses explicit locale routes, canonicals and alternate-language relationships. Private/paid content is not ordinarily publicly indexed.

Experiment treatment uses one clean canonical public URL. Experiment-sensitive HTML initially bypasses shared full-page caching unless internal variant-safe partitioning is proven.

## 10.3 Media and live/replay

Media has a platform-owned identity independent of provider/object IDs. Masters, recordings and derivatives retain lineage. Protected playback checks current platform authority before bounded delivery capability is issued.

Live-session participation, registration, entitlement and publication truth stay platform-authoritative. Provider capture is not automatic replay publication. Full recording, approved replay and promotional clips have separate governed publication/rights states. Captions/transcripts are governed derivatives.

External production/streaming/transcoding remains the first-release direction behind replaceable platform adapters. Provider callbacks/status are evidence and provider failure does not rewrite entitlement/publication truth.

## 10.4 Messaging, measurement and provider boundaries

Material mutable message templates are governed versioned content with exact locale/version delivery provenance. Notification intent is platform-owned and delivered through thin channel adapters. Delivery/engagement observations are not authoritative business conversion.

Message experiments reuse the common governed Experiment authority; assignment, delivery, engagement and downstream authoritative outcome are separate evidence classes.

Acquisition touchpoint evidence remains separate from attribution interpretation. Vendor analytics/payment/communication reports are labelled external evidence and reconciled rather than becoming platform financial/entitlement truth.

All optional/required integrations reuse bounded deadline/retry/bulkhead and durable-consequence semantics. Provider SDK details do not leak throughout business code.

## 10.5 Experiment governance

Experiment governance is platform-owned even when assignment mechanics are implemented behind a replaceable deterministic adapter. Assignment is deterministic, sticky, mutually exclusive within the governed experiment and version-bound. Assignment and exposure are separate facts: exposure records that the participant actually experienced a treatment.

Concurrent experiments require explicit interaction/isolation governance. Activated experiment configuration is immutable/versioned evidence rather than mutable history. Experiment or analytics failure may degrade measurement/freshness but cannot block unrelated authoritative business operations or fabricate evidence. Material unexplained Sample Ratio Mismatch is a validity blocker at the relevant proof/readout gate.

**Supporting Architecture Law:** `ARC-189...ARC-232`.

**Material downstream gates:** `OQ-013...OQ-016`, `OQ-020...OQ-021`, `OQ-024`, `OQ-036`, `OQ-040` as applicable.

---

# 11. Privacy, Records, Deletion, Export & Recovery

Business lifecycle and data lifecycle are separate dimensions.

```text
account closure
≠ consent withdrawal
≠ full deletion
≠ legal hold
≠ ordinary business retention
```

Retention is category-, purpose- and authority-specific. Architecture does not invent statutory, clinical or professional retention durations.

## 11.1 Full deletion

Full deletion is a durable, idempotent cross-system orchestration. Deleting an account row is not completion. Every capability that holds eligible identifiable representations participates through a deletion contract while retaining its own business semantics.

Deletion completes only when eligible identifiable representations are deleted or irreversibly anonymised and verified across authoritative state, object/derivative storage, caches, search/read models and relevant external processors. Pseudonymisation is not automatically irreversible anonymisation.

Retained-by-obligation data is minimised and isolated from ordinary participant use. Legal holds are narrowly scoped and pause only the deletion they govern. Minimal non-reconstructive suppression/deletion evidence may survive when necessary and lawful to prove deletion or prevent resurrection.

## 11.2 Backup and restore

High availability/failover and historical backup/PITR are distinct protections. Disaster recovery restores the complete minimum authority set, not PostgreSQL bytes alone.

Historical encrypted backups age out under their normal lifecycle; the platform does not mutate every old backup for each deletion. Instead, deletion/consent-withdrawal suppression must survive beyond the selected restore point and be replayed/reconciled before a restored environment returns to normal service.

Restored environments remain recovery-gated until privacy suppression, critical reconciliation and semantic authority checks pass. Recovery restores valid **present** authority; it does not blindly resurrect the historical world captured by the backup.

Derived analytics/search/read models rebuild only through current privacy/deletion rules.

## 11.3 Participant export

Export is a governed data-release product assembled from eligible domain-owned records. Authority/scope is revalidated through request, generation and delivery. Large/sensitive exports use bounded durable generation, short-lived protected delivery, expiry/deletion, strong verification where appropriate, minimised audit evidence and safe output encoding.

**Supporting Architecture Law:** `ARC-233...ARC-254`.

**Material downstream gates:** `OQ-009`, `OQ-018`, `OQ-029...OQ-033`, `OQ-037`.

---

# 12. Reliability, Deployment, Observability & Incident Operations

## 12.1 Health and failure isolation

Availability objectives are capability/business-class specific. Hard correctness invariants are not consumable error budgets.

Startup, liveness, readiness and capability degradation are distinct contracts. A remote dependency failure changes only the capability/readiness semantics that actually depend on it; it does not automatically imply local process death.

OTP supervision follows real failure dependencies. Restart intensity is bounded and crash loops escalate rather than restart forever. Under overload, use backpressure, admission control, shedding and degradation before restarting healthy capacity. Dependency calls have bounded deadlines, one deliberate retry owner/budget and failure-isolation bulkheads.

PostgreSQL failover preserves one fenced accepted write authority; split-brain writes are forbidden.

## 12.2 Deployment and operational change

Rolling deployment requires adjacent-version interoperability and compatible state evolution. Planned termination drains new traffic/work first and relies on durable recovery for unfinished obligations. Every change has rollback or explicit forward recovery. Progressive/canary release is risk-proportional and uses explicit comparison/stop criteria.

Emergency controls are named, least-privilege and auditable; they isolate optional work without weakening core correctness.

Runtime configuration is centralised, validated and readiness-gated. Secrets are a distinct sensitive configuration class with least-privilege access, rotation/revocation support and recoverability. Material configuration changes are code-adjacent governed releases.

## 12.3 Observability

Observability combines metrics, distributed traces, structured operational logs and governed domain outcome signals. Audit/security evidence remains a separate governed class.

Correlation propagates across synchronous, durable-async and provider boundaries without using raw sensitive identity as the tracing key. Metrics use bounded cardinality. Logs minimise/redact sensitive payloads. Vendor-neutral tracing is preferred where material and never substitutes for authoritative evidence.

Database observability distinguishes query, pool, lock, planner/index, maintenance, replication and resource pressure. Queues and realtime surfaces expose freshness, saturation, retry and amplification evidence. Material alerts are actionable, severity-governed and owned.

Telemetry failure normally degrades visibility rather than business correctness; telemetry handlers/exporters remain bounded/non-blocking. Observability classes have purpose- and sensitivity-specific retention/access, and collection is minimised before relying on redaction as a safety mechanism.

## 12.4 Incidents and operational proof

Incident severity follows impact/risk. One named incident commander/owner coordinates material incidents while specialist authorities retain non-waivable decisions. Safe containment may precede perfect diagnosis.

Runbooks are owned, versioned, exercised and include entry/stop/success/escalation conditions. Post-incident reviews are evidence-based and trigger explicit amendment/re-proof when governing assumptions fail.

Release/pilot progression uses a cross-functional evidence-bearing gate manifest. Failure injection matures from deterministic tests to controlled game days. Recovery exercises prove the complete service and semantic promotion criteria, not merely restored bytes.

**Supporting Architecture Law:** `ARC-255...ARC-290`, with deployment foundation `ARC-010...ARC-026`.

**Material downstream gates:** `OQ-037` RPO/RTO; `OQ-038` incident ownership; exact secret/deployment/observability products remain downstream.

---

# 13. Performance, Capacity & Scaling Doctrine

## 13.1 Scale intent without premature infrastructure

The platform must have a credible path to approximately 100,000 simultaneously active/connected users where relevant, but this is workload-specific. It is **not** a requirement for 100,000 simultaneous requests on every endpoint and it is not a reason to provision 100,000-user infrastructure at launch.

Performance architecture follows measured bottlenecks and the simplest lawful response. Adding nodes is not automatically adding capacity; it also multiplies pressure on PostgreSQL connections, Redis, providers, queues, network and realtime fan-out.

## 13.2 Initial performance budgets

Important latency gates use percentile distributions, not averages alone.

Initial server-side architecture budgets are:

- suitable hot/common interactive actions: `p90 <= 100 ms`, `p99 <= 400 ms`;
- normal durable interactions: `p95 <= 500 ms`, `p99 <= 1 s`;
- provider-bound checkout/payment: end-to-end `p99 <= 5 s` where provider latency permits, with internal platform contribution measured separately.

Applicable public/participant web experiences must meet at least the then-current official "good" Core Web Vitals floor and aim better. The baseline captured when the law was locked was LCP <= 2.5 s, INP <= 200 ms and CLS <= 0.1 at the 75th percentile; release gates revalidate the then-current official definitions rather than silently weakening the floor.

Correctness/security/privacy/safety is never skipped to meet latency.

## 13.3 PostgreSQL and shared-resource capacity

PostgreSQL connections are one finite platform-wide budget with explicit operational/failure reserve. Pool sizes, worker concurrency and topology changes must be evaluated together.

Transaction-pooling compatibility is preserved, but PgBouncer/equivalent is introduced only when measured need justifies it. Query/index/plan budgets are path-specific and evidence-derived. Read replicas are for explicitly stale-tolerant reads only and are introduced after simpler query/projection approaches are insufficient.

LiveView scale is measured through per-connection resource envelopes. Realtime proof measures the whole amplification path. Worker concurrency shares database/CPU/RAM/I/O/provider budgets with interactive traffic.

Headroom is workload/resource specific; autoscaling does not replace capacity planning. Vertical versus horizontal scaling follows the measured bottleneck.

## 13.4 Adversarial proof obligations

Performance proof includes correctness under contention, not clean-load speed only. Applicable executable tests deliberately attack:

- simultaneous/repeated/reordered/retried execution;
- zero confirmed oversell for scarce capacity;
- duplicate/retry storms and ambiguous outcomes;
- DB pool/lock/transaction/plan contention;
- cache expiry/cold-start stampedes;
- backlog catch-up after provider/node/deployment disruption;
- realtime connect/reconnect/broadcast storms;
- layered abuse controls under load;
- large/hot-table migration and maintenance pressure;
- representative synthetic cardinality, skew, selectivity and hot spots;
- analytics/experimentation composite load without starving critical OLTP.

## 13.5 Staged proof model

Architecture defines what must eventually be proven; it does not fabricate runtime evidence before software exists.

```text
Phase 3 Architecture Pressure Test
→ Is the path architecturally coherent?
→ What hard invariant / scale concern must later be proved?

Phase 8 Architectural Proof / affected Feature Pack
→ Does the implemented architectural mechanism actually work?
→ Instantiate applicable executable ARC-326 evidence.

Horizontal Hardening / Release Gate
→ What safe operating envelope does the release sustain?
→ Prove adverse load/failure/recovery behaviour and breakpoint/headroom.
```

`ARC-326` remains the canonical Performance & Capacity Proof Matrix for executable evidence. `ARC-327` stages its depth: pre-implementation pressure tests record proof obligations; runtime-only topology, workload, tooling, measured result, safe envelope and breakpoint fields become mandatory when executable evidence exists. Major load tests must also prove the load generator itself is not the limiting factor; generation is distributed only when evidence requires it.

**Supporting Architecture Law:** `ARC-291...ARC-327` plus the performance-related mechanisms in earlier workstreams.

**Material downstream gates:** `OQ-022`, `OQ-035`, `OQ-039`, `OQ-040` and affected Feature Pack/Architectural Proof gates.

---

# 14. Cross-Cutting Security Doctrine

Security is enforced through platform/application authority rather than browser, cache, provider or operational convenience.

Core rules:

1. Server-side authoritative actions decide protected state transitions.
2. Browser/client parameters, URLs and LiveView assigns are untrusted intent/projection.
3. Least privilege applies to participant, practitioner, staff, system and provider access.
4. No universal privileged-policy bypass exists.
5. Sensitive fields are minimum-loaded and field-policy protected.
6. Private state services are not publicly exposed.
7. External providers receive the minimum capability/data needed and remain evidence/delivery systems rather than domain authority.
8. Uploads remain quarantined/restricted until governed validation/scanning/sanitisation appropriate to risk.
9. Protected downloads/media are authorised from current policy before bounded delivery capability is issued.
10. Sessions, recovery tokens and one-purpose secrets are bounded and revocable/replay-controlled.
11. Rate/abuse protection is layered across edge/application/shared velocity state where required, with non-enumerating public behaviour and recoverable handling.
12. Audit/security evidence is separated from ordinary logs and is purpose/minimisation governed.
13. Secrets are separate from ordinary runtime configuration and never baked into source/images.
14. Production participant data is not treated as development/test convenience data.
15. Security/privacy controls remain active during load/performance testing.

**Supporting Architecture Law:** `ARC-020...ARC-022`, `ARC-035...ARC-042`, `ARC-089...ARC-109`, `ARC-110...ARC-145`, `ARC-223...ARC-232`, `ARC-233...ARC-254`, `ARC-267...ARC-290`, `ARC-322`, `ARC-324`.

---

# 15. Architecture Enforcement

The architecture is enforceable through a combination of code structure, policies, tests, review and proof evidence.

| Rule | Primary enforcement expectation |
|---|---|
| No durable business authority in LiveView/process state | architecture/code review; restart/reconnect tests; application-action boundaries |
| Business writes go through authoritative application interfaces | Ash code-interface conventions; review; dependency tests/static checks where useful |
| No ordinary cross-boundary direct persistence | module/dependency rules; code review; owning-interface tests |
| No Repo/SQL second business-write API | code review/static checks; bounded documented exceptions |
| Browser/client values are not authority | action validation/policies; security tests |
| Authorisation is default-on/current | Ash policies; actor/context tests; long-lived LiveView reauthorisation tests |
| Protected fields are minimum-loaded | field policies; query/projection review; privacy tests |
| Redis/ETS/cache is not silent business authority | Domain/JIT cache contract; empty-cache/restart/failure tests |
| Material revocation bypasses stale caches | authority-first checks; invalidation/revocation tests |
| Mandatory post-commit consequence is durable | transactional intent/Oban tests; crash-window/idempotency tests |
| Queue uniqueness is not business idempotency | explicit operation identity/invariant tests |
| Provider response/callback is evidence, not domain truth | adapter/reconciliation tests; duplicate/reorder/ambiguity tests |
| PubSub is not durable delivery | architecture review; missing/duplicate/reorder observation tests |
| Protected files/media are current-policy authorised | entitlement/policy tests; bounded capability tests |
| Public/private cache classes do not cross | cache classification; headers/integration tests; experiment variant-isolation proof |
| Deletion is representation-complete and non-resurrecting | deletion contracts; processor/object/cache/search tests; restore replay exercises |
| Deployment remains adjacent-version compatible | migration/release tests; rollback/forward-recovery gate |
| Performance proof attacks hard invariants | ARC-326 evidence matrix at executable proof stages |
| New infrastructure/package does not become permanent law by convenience | Architectural Proof / JIT decision record; replaceable platform boundary |

Architecture enforcement should prefer deterministic/cheap checks early and reserve expensive runtime proof for the stage where evidence is meaningful.

---

# 16. Deliberately Deferred Decisions

The following omissions are intentional. A future agent must not treat them as Architecture defects merely because `03_ARCHITECTURE` does not specify them.

| Deferred decision | Owning downstream stage / gate |
|---|---|
| Final business Domains and ownership | `04_DOMAIN_MAP.md` |
| Broad hot/warm/cold and concurrency profile per Domain | Domain Architecture Profiles / `OQ-039` |
| Ash Domains/Resources/actions/module names | JIT Domain Dossier / Feature Pack |
| Tables, columns, constraints, exact indexes | JIT Domain Dossier / Feature Pack / migration proof |
| Redis data structures, keys, TTLs, invalidation triggers | JIT Domain Dossier / `OQ-039` / affected proof |
| ETS/Cachex exact library use | JIT/proof where node-local caching is justified |
| GenServer ownership/modules | JIT/proof only where genuine process ownership exists |
| PubSub topics and broadcast payloads | JIT Domain Dossier / Feature Pack |
| Oban queue names/counts/concurrency/worker modules | JIT Domain Dossier / capacity proof |
| PgBouncer sizing/activation | evidence under AR-009 / ops proof |
| Read-replica topology | evidence under AR-009 / affected read model |
| Exact authentication package configuration | `OQ-034` / Architectural Proof |
| Exact rate-limit thresholds/backend/algorithms | `OQ-035` / Architectural Proof / affected JIT dossier |
| Exact Paystack retry/webhook/subscription/refund/dispute behaviour | `OQ-004` provider validation |
| Exact Cloudflare WAF/cache/rate rules | `OQ-014`, `OQ-035` |
| Exact notification providers/channel rules | `OQ-036` |
| Exact content translation resource model | `OQ-013` / Domain Map/JIT |
| Exact search configuration/extensions/engine | `OQ-015` / evidence-gated proof |
| Live/video provider operational plan | `OQ-020...OQ-021` |
| Clinical thresholds/formulas/eligibility/adjustment rules | `OQ-005...OQ-011`, `OQ-019`, `OQ-025` |
| Retention periods and professional record obligations | `OQ-009`, `OQ-029`, `OQ-033` / expert review |
| External processor deletion/export inventory | `OQ-030...OQ-032` |
| Exact RPO/RTO values | `OQ-037` |
| Event hold/locking/rate/expiry implementation | `OQ-022` + Domain/JIT/Architectural Proof |
| Experiment hash/library/statistical engine/cache partition | `OQ-040` + Architectural Proof/Feature Pack |
| Exact hosting, secret manager, backup product, malware scanner | operations/vendor proof/JIT |

The governing principle is: **capability law first; replaceable mechanism/package choice at the first stage where evidence can distinguish candidates.**

---

# 17. Domain Map Handoff

Architecture is ready to hand concrete ownership to `04_DOMAIN_MAP.md`.

`04_DOMAIN_MAP` may now answer questions such as which Domain owns a particular durable fact, relationship or state machine. It inherits these non-negotiable rules:

- one authoritative owner per durable business truth;
- no shared-write ambiguity;
- cross-boundary writes invoke the owner;
- relationships do not transfer mutation authority;
- projections/search/cache/analytics do not become hidden write authority;
- provider evidence remains external evidence;
- async/realtime/privacy/security/storage/performance mechanisms come from this Architecture rather than being reinvented per Domain;
- circular authority dependencies are defects;
- final resource/schema/index/key/topic/queue design remains later JIT work;
- every mapped Domain receives the required lightweight Domain Architecture Profile before Roadmap sequencing under `OQ-039`.

**Domain Map readiness test:** a Domain must be able to choose ownership and dependencies without inventing a new transaction, state-authority, async, realtime, provider, privacy, security or scaling mechanism. If it cannot, route the missing mechanism back to Architecture rather than silently solving it in Domain Law.

---

# 18. Appendices

## Appendix A — Architecture Law thematic index

| Theme | Architecture Law |
|---|---|
| Runtime topology / deployment shape | `ARC-001...ARC-026` |
| Phoenix / LiveView / Ash / code boundaries | `ARC-027...ARC-058` |
| State authority / PostgreSQL / caching / storage | `ARC-059...ARC-109` |
| Identity / authentication / authorisation / field privacy | `ARC-110...ARC-145` |
| Transactions / durable async / realtime / analytics consistency | `ARC-146...ARC-188` |
| Content / translation / search / media / messaging / integrations | `ARC-189...ARC-232` |
| Privacy / deletion / backup / restore / export | `ARC-233...ARC-254` |
| Reliability / deployment / observability / incident operations | `ARC-255...ARC-290` |
| Performance / capacity / multi-node proof | `ARC-291...ARC-326` |
| Staged performance-proof timing | `ARC-327` |

## Appendix B — Downstream gate index

| Architecture area | Principal remaining gates |
|---|---|
| Legal/entity/IP/consumer authority | `OQ-001`, `OQ-028`, `OQ-029` |
| Payments/commercial execution | `OQ-003`, `OQ-004`, `OQ-012` |
| Clinical/methodology | `OQ-005...OQ-008`, `OQ-010...OQ-011`, `OQ-019`, `OQ-025`, `OQ-033` |
| Content/search/media | `OQ-013...OQ-016`, `OQ-020...OQ-021`, `OQ-024` |
| Community/events/Nuwe Jy operations | `OQ-022...OQ-023`, `OQ-026...OQ-027` |
| Privacy/security/continuity | `OQ-009`, `OQ-017...OQ-018`, `OQ-030...OQ-038` |
| Performance/scaling mapping | `OQ-039` |
| Experiment implementation proof | `OQ-040` |

## Appendix C — Reference Flow traceability

| Flow | Primary architecture sections |
|---|---|
| FLOW-01 Registration → verification → login | §§4, 6, 8, 9, 14 |
| FLOW-02 Checkout → provider verification → payment → entitlement | §§5, 7, 8, 10, 13, 14 |
| FLOW-03 Assessment → scoring → immutable result → report | §§4, 5, 7, 8, 10 |
| FLOW-04 Health intake → safety evaluation → eligibility | §§4, 5, 6, 7, 8, 14 |
| FLOW-05 Eligibility → deterministic plan → immutable plan | §§4, 5, 7, 8, 10, 13 |
| FLOW-06 New health risk → safety effect → dependent plan behaviour | §§5, 6, 7, 8, 9, 14 |
| FLOW-07 Scheduled programme release → durable work → notification → LiveView | §§8, 9, 10, 12, 13 |
| FLOW-08 Full deletion → storage/processors → backup boundary | §§7, 10, 11, 12, 14 |
| FLOW-09 Event hold → payment → ticket / expiry | §§5, 7, 8, 9, 13, 14 |
| FLOW-10 Consent → practitioner relationship → scoped access → audit/revocation | §§5, 6, 7, 11, 14 |
| FLOW-11 Safety-critical correction/withdrawal → invalidation/response/audit | §§6, 7, 8, 9, 10, 11, 12, 14 |
| FLOW-12 Experiment lifecycle → assignment → exposure → outcome → learning | §§7, 8, 9, 10, 11, 13, 14 |

---

# 19. Architecture Freeze Record

## 19.1 Consolidated review

The one-pass Phase 4 review used five lenses simultaneously.

| Review lens | Result | Finding |
|---|---|---|
| Architecture consistency | PASS | No active ARC conflict found |
| Security / privacy | PASS | Current-policy, least-privilege, private-state, provider-minimisation, deletion and evidence boundaries remain coherent |
| Failure / recovery | PASS | Commit/consequence, provider ambiguity, dependency degradation, restore suppression and rollout recovery mechanisms remain coherent |
| Performance / scaling | PASS | Workload-specific budgets, finite shared-resource capacity and staged `ARC-326`/`ARC-327` proof model are represented without pre-provisioning scale |
| Anti-overengineering / development friction | PASS | Redis, replicas, PgBouncer, specialist search, service extraction and package choices remain evidence/JIT-gated |

Review findings were classified under the governed Phase 4 taxonomy:

- `EDITORIAL`: minor wording/organisation corrections only; resolved in synthesis.
- `MISSING_SYNTHESIS`: accepted-law omissions identified for scheduling semantics, system-authority/causation separation, UUIDv7 identifier doctrine, experiment governance and observability/performance proof details; all were added from existing ARC law without changing it.
- `REAL_ARC_CONFLICT`: **0**.
- `DOWNSTREAM_DETAIL`: remains explicitly deferred in Section 16 and Appendix B.

No Product Law, ARQ or ARC amendment was required by Phase 4.

## 19.2 Mechanical coverage audit

```text
Frozen ARQs:            417 unique
Requirement families:   10 / 10 represented
  Performance           166
  Analytics             216
  Payments                1
  System                  6
  IAM                     8
  State                   7
  Async                   3
  Content                 6
  Security                2
  Operations              2

Active ARCs:            327 unique
ARC range:               ARC-001...ARC-327
ARC gaps:                0
ARC duplicates:          0
Thematic-index coverage: 327 / 327
```

This audit does not duplicate 417 ARQ rows inside the synthesis. The frozen ARQ register and detailed Architecture Law remain the legislative traceability records.

## 19.3 Reference Flow traceability

All twelve already-passed Phase 3 flows still have the architecture mechanisms that produced their verdicts. Appendix C maps each flow to the relevant synthesis sections.

```text
FLOW-01...FLOW-12:          12 / 12 represented
PASS:                        1
PASS_WITH_DOWNSTREAM_GATES: 11
Architecture gaps:           0
Governing contradictions:    0
Flows materially changed:    0
Flows rerun:                 0
```

No flow was rerun because synthesis did not change Architecture Law or a material flow mechanism.

## 19.4 Domain Map readiness

**PASS.** `04_DOMAIN_MAP.md` can now decide concrete business ownership using existing platform mechanisms without inventing a transaction, persistence, cache-authority, async, realtime, provider, privacy, security or scaling model. No concrete Domain ownership was assigned during Architecture synthesis.

## 19.5 Freeze verdict

**PASS — PHASE 4 COMPLETE / ARCHITECTURE FROZEN v1.0.0.**

The detailed supporting records remain preserved:

- `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`;
- `reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md`;
- `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`.

Normal downstream work should consume this frozen synthesis first and consult exact `ARC-*` entries when deeper legislative rationale/evidence is required.

The next governed planning stage is Phase 5 — `04_DOMAIN_MAP.md` plus Domain Architecture Profiles. Implementation remains stopped.
