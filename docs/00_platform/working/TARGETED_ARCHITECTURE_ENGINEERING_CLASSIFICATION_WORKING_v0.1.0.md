# Targeted Architecture / Engineering classification

**NON-AUTHORITATIVE / STAGE 3B CLASSIFICATION**

> **DOES NOT AMEND PRODUCT LAW**
> **DOES NOT AMEND AR-000**
> **DOES NOT AMEND ARCHITECTURE LAW**
> **DOES NOT CREATE ENGINEERING STANDARDS**
> **NO GOVERNED IDENTIFIERS CREATED**
> **LIVE GITHUB AUTHORITY IS CANONICAL**

- **Artifact version:** v0.1.0
- **Date:** 2026-09-04
- **Programme:** Targeted Product Amendment → FP-001 Development Entry Readiness
- **Stage:** Stage 3B, Independent Architecture / Engineering Input Classification
- **Status:** Classification complete, pending independent review
- **Baseline:** `main` at `e0e9680f2f121512a6bd582299755d06e5094aff`
- **Authority:** Current GitHub `main`, routed by `docs/00_platform/README.md` and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`

## Scope and stop boundary

This file classifies four independent Architecture/Engineering inputs:

1. Errors & Diagnostics
2. Observability refinement
3. Native Compute / Rustler
4. Engineering Quality

The inputs are independent technical proposals. They are not Product-derived, even though Stage 3B sits inside the same amendment programme. This artifact does not reopen Stage 3A.2 or add technical material to Product Law or the current ARQ register.

The artifact records classification, evidence and questions for later human Grills. It does not answer an Architecture Grill, write an Engineering Standard, select packages, create a Domain, create a Feature Pack, or authorise implementation.

### Primary classification enum

Every local proposition key below has exactly one primary classification:

- `ALREADY_GOVERNED_NO_CHANGE`
- `ARCHITECTURE_GRILL_REQUIRED`
- `ENGINEERING_POLICY_GRILL_REQUIRED`
- `SPLIT_ARCHITECTURE_AND_ENGINEERING_POLICY`
- `DEFER_NO_CURRENT_EVIDENCE`
- `REJECT_UNNECESSARY_COMPLEXITY`
- `UPSTREAM_CONTRADICTION_STOP`

The keys such as `A-01` and `C-04` are local labels for this working artifact. They are not ARQ, ARC, DEC, OQ, CAP, FP, TB, VS or HH identifiers.

## Authority and evidence baseline

### Resolved current paths

The README and current manifest resolve the authority set as follows:

| Class | Current path | Use in this artifact |
|---|---|---|
| Product north star | `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` | Product boundary and stop conditions |
| Platform Product Law | `docs/00_platform/00_PLATFORM_v1.3.0.md` | Product authority and cross-capability boundaries |
| Decision Register | `docs/00_platform/01_DECISIONS_v1.3.0.md` | Locked decisions and explicit gates |
| Open Work | `docs/00_platform/02_OPEN_WORK_v1.2.32.md` at baseline | Programme sequence and development stop |
| Architecture synthesis | `docs/00_platform/03_ARCHITECTURE_v1.0.0.md` | Current architecture law as consumed by engineering |
| Domain Map | `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md` | Durable business-truth ownership and domain boundary |
| Roadmap | `docs/00_platform/05_ROADMAP_v1.0.0.md` | Sequencing and anti-speculation constraints |
| Operating model | `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md` | Operational evidence, dashboards and traceability boundaries |
| ARQ evidence | `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` | Product-derived architecture requirement tracing |
| Architecture-law evidence | `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md` | Exact ARC reasoning for the frozen synthesis |
| Flow evidence | `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md` | Cross-boundary failure and recovery pressure |

The current manifest records the following baseline SHA-256 values for the protected authority and deep-evidence files:

| Path | SHA-256 |
|---|---|
| `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` | `5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20` |
| `00_PLATFORM_v1.3.0.md` | `4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445` |
| `01_DECISIONS_v1.3.0.md` | `43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96` |
| `02_OPEN_WORK_v1.2.32.md` | `ed68c4c5264f07226de3844801402e97e4acd9ed4bbeda086fad284559ddbf63` |
| `03_ARCHITECTURE_v1.0.0.md` | `87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b` |
| `04_DOMAIN_MAP_v1.0.0.md` | `f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a` |
| `05_ROADMAP_v1.0.0.md` | `b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20` |
| `PLATFORM_OPERATING_MODEL_v1.0.0.md` | `884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811` |
| `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` | `971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91` |
| `reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md` | `a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639` |
| `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md` | `f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20` |

These values are evidence of the reviewed baseline. The Stage 3B change set must leave those files and hashes unchanged.

### Existing architecture coverage used for classification

The relevant current law is already broad:

- `03_ARCHITECTURE` §§4.1–4.3, 7, 8, 10.4, 12.1, 12.3–12.4, 13, 14 and 15 cover application authority, controlled escape hatches, provider boundaries, bounded retries, degradation, observability, performance evidence and architecture enforcement.
- The exact evidence includes `ARC-027`, `ARC-028`, `ARC-031`, `ARC-033`, `ARC-044`–`ARC-049`, `ARC-052`, `ARC-057`–`ARC-058`, `ARC-070`, `ARC-076`, `ARC-131`–`ARC-132`, `ARC-147`, `ARC-151`, `ARC-154`, `ARC-161`, `ARC-232`, `ARC-267`–`ARC-290` and `ARC-291`–`ARC-327`.
- Relevant current ARQ evidence includes `ARQ-SYS-002`, `ARQ-SYS-005`, `ARQ-SYS-006`, `ARQ-PERF-002`, `ARQ-PERF-016`, `ARQ-PERF-018`–`ARQ-PERF-024`, `ARQ-PERF-094`, `ARQ-PERF-107`, `ARQ-PERF-112`, `ARQ-PERF-135`, `ARQ-PERF-136`, `ARQ-PERF-150`, `ARQ-PERF-156` and `ARQ-IAM-007` / `ARQ-OPS-001`.
- `04_DOMAIN_MAP` assigns durable business truth to business Domains and assigns incident/release evidence to Audit & Evidence. It does not create technical ownership Domains.
- `PLATFORM_OPERATING_MODEL` separates operational work and evidence from participant/business truth, requires traceability for material operational changes, and rejects a general dashboard builder.
- `05_ROADMAP` rejects speculative Redis, replicas, GenServers, specialist search and microservices before evidence. It treats operational capability as part of the product without turning every tool into an upfront requirement.

The review therefore classifies semantic gaps, not missing section names.

### Provenance rule

The source of the four proposals is the independent Stage 3B input brief supplied for this task. Current Product, ARQ, Architecture, Domain, Roadmap and Operating Model documents are evidence and constraint checks, not retroactive provenance for the proposals. Stage 1 and Stage 3A.1 archive artifacts remain historical programme context only.

## Classification method

For each proposition:

1. state the concrete concern;
2. locate current Product, ARQ, Architecture, Domain, Roadmap or operating evidence;
3. identify the remaining semantic gap, if any;
4. assign one primary classification;
5. route secondary work without allowing it to override the primary classification;
6. name the evidence that would justify a deferred revisit.

The Architecture-versus-Policy test was applied explicitly:

> If two correct implementations can choose different mechanisms while preserving current platform invariants, the mechanism belongs in Engineering Policy or JIT work, not Architecture Law.

The reverse test was also applied:

> If violating a practice could break a durable cross-platform invariant, separate that invariant from the practice and route the invariant to Architecture.

No proposition exposed a Product Law, AR-000 or current Architecture contradiction. The `UPSTREAM_CONTRADICTION_STOP` count is zero.

## Structured evidence register

### Track A: Errors & Diagnostics

| Key | Proposition and requirement | Proposal provenance | Current evidence | Gap analysis and rationale | Primary classification | Routing, rejected mechanism, revisit and STOP |
|---|---|---|---|---|---|---|
| A-01 | An authoritative application operation owns the result and error semantics consumed by HTTP, LiveView, workers and other callers. Delivery code must not recreate business outcomes. | Independent Stage 3B Errors & Diagnostics brief. | `03_ARCHITECTURE` §§4.1–4.3, 8; `ARC-027`, `ARC-028`, `ARC-031`, `ARC-033`, `ARC-046`, `ARC-048`; `FLOW-01`–`FLOW-12`. | The boundary already exists. A new global error framework would duplicate it. | `ALREADY_GOVERNED_NO_CHANGE` | No further action. Later implementation may choose surface adapters inside the existing boundary. STOP: none. |
| A-02 | HTTP/provider transport status, browser return state, callback state and queue execution state must not become application or business authority. Pending, retryable, terminal and unknown outcomes remain distinguishable. | Independent brief, including transport/protocol versus application semantics. | `03_ARCHITECTURE` §§7, 8.3, 10.4, 12.1; `ARC-052`, `ARC-147`, `ARC-154`, `ARC-161`, `ARC-232`; `ARQ-PERF-028`, `ARQ-PERF-039`, `ARQ-PERF-094`; `FLOW-02`. | Current law already separates evidence, authority, pending state and retry/terminal behaviour. | `ALREADY_GOVERNED_NO_CHANGE` | No new status taxonomy or provider authority. Surface-specific presentation remains downstream. STOP: none. |
| A-03 | Decide whether a minimum cross-boundary error/result contract is required for application, HTTP/API, LiveView, background-worker and provider boundaries. It would need to preserve authority, pending/unknown state, retry/terminal semantics and safe/public versus internal separation without choosing a package or envelope here. | Independent brief. The question is architectural only if the invariant changes the platform boundary. | `03_ARCHITECTURE` §§4, 8, 10.4, 12.1; `ARC-027`, `ARC-028`, `ARC-046`, `ARC-048`, `ARC-161`, `ARC-232`; `ARQ-PERF-094`, `ARQ-PERF-150`. | Current Architecture already establishes this durable cross-surface invariant through the authoritative application operation, thin delivery layers and approved application contracts. The lack of one consolidated sentence is not a semantic gap, and RFC Problem Details is only a possible later representation. | `ALREADY_GOVERNED_NO_CHANGE` | No further Architecture work. Existing law governs the invariant. Ash/Splode mapping, HTTP representation, LiveView presentation, localisation, redaction and labels belong under A-08 or a real approved API/JIT contract. Future evidence: none is needed for Architecture; a concrete implementation may still trigger A-08. STOP: no upstream contradiction. |
| A-04 | Participant-safe or public messages must be separate from internal diagnostic detail, provider payloads, stack traces and sensitive data. | Independent brief. | `03_ARCHITECTURE` §§10.4, 12.3, 14; `ARC-131`, `ARC-132`, `ARC-232`, `ARC-267`, `ARC-270`, `ARC-290`; `ARQ-IAM-007`; `04_DOMAIN_MAP` §§2, 4. | The separation, minimisation and access boundaries already exist. | `ALREADY_GOVERNED_NO_CHANGE` | No public exposure of internal diagnostics. Redaction and message-writing conventions can be considered later as Engineering Policy. STOP: none. |
| A-05 | Trace ID, correlation context, diagnostic occurrence/reference value, business/resource identity and actor identity remain distinct. Diagnostic IDs do not grant authority or replace causation, subject or durable business identifiers. | Independent brief. | `03_ARCHITECTURE` §§4, 7, 8, 12.3; `ARC-046`, `ARC-151`, `ARC-154`, `ARC-268`, `ARC-270`; `ARQ-IAM-007`; `FLOW-01`, `FLOW-02`. | The durable distinction and non-authority rule already exist. A participant-facing occurrence ID is a separate product/support decision and is not silently assumed. | `ALREADY_GOVERNED_NO_CHANGE` | No shared identity abstraction or business error ID is created. Naming and field conventions may be policy work only if a real implementation requires them. STOP: none. |
| A-06 | Expose a stable occurrence/reference ID to participants or support on every surface. | Independent brief, supportability question. | Current law requires diagnostic evidence, correlation and supportable operations, but no current Product Law requirement requires a participant-facing occurrence ID on every surface. | A global reference contract could be useful later, but no current incident, API, support workflow or participant need establishes it. | `DEFER_NO_CURRENT_EVIDENCE` | Do not add a public identifier contract now. Revisit after a real support workflow, incident pattern or API contract demonstrates that correlation alone is insufficient. STOP: none. |
| A-07 | Error classes must support safe retry, terminal failure, unresolved state, reconciliation and recovery without one blind retry rule. | Independent brief, including validation/domain/application/infrastructure/provider classes. | `03_ARCHITECTURE` §§8.2–8.3, 12.1; `ARC-147`, `ARC-154`, `ARC-161`, `ARC-232`; `ARQ-PERF-039`, `ARQ-PERF-094`, `ARQ-PERF-150`, `ARQ-PERF-156`; `FLOW-02`, `FLOW-07`, `FLOW-11`. | The durable semantic requirement and failure pressure are already governed. | `ALREADY_GOVERNED_NO_CHANGE` | No giant universal taxonomy is needed. Affected actions later map their concrete errors to the existing classes. STOP: none. |
| A-08 | Establish implementation conventions for Ash/Splode errors, application error modules, public-message mapping, redaction, localisation and retry classification without creating a parallel custom error framework. | Independent brief plus current Ash/Splode ecosystem question. | `03_ARCHITECTURE` §§4.2–4.3, 10.4, 12.3; `ARC-027`, `ARC-046`, `ARC-048`, `ARC-057`–`ARC-058`; current Ash/Splode documentation confirms a framework-native error model with extensible error types. | The architecture boundary is present. The repository-wide mapping and review rules are implementation practice, and the repository has no current executable application requiring a settled convention. | `ENGINEERING_POLICY_GRILL_REQUIRED` | Engineering-Policy Grill question: which risk-proportional Ash/Splode mapping and redaction conventions should teams use while keeping business semantics behind the application boundary? Do not build a parallel framework. Future evidence: first affected application slice, repeated mapping defects or a reviewed public API contract. STOP: none. |
| A-09 | Mandate RFC 9457 Problem Details as the external representation for every API error. | Independent brief, RFC representation question. | North Star/MVP excludes implementation-grade API commitments; `03_ARCHITECTURE` leaves exact API endpoints and surface details downstream; `05_ROADMAP` and `FLOW` evidence do not require an API. RFC 9457 defines a useful HTTP representation but does not require universal adoption. | No current API boundary or interoperability requirement justifies a platform-wide mandate. | `DEFER_NO_CURRENT_EVIDENCE` | Do not mandate Problem Details now. Revisit when a real HTTP/API boundary, client interoperability need, or external contract is approved. A later policy may choose it at that boundary. STOP: none. |
| A-10 | Create one giant global error-code registry spanning validation, domain, application, infrastructure, provider and UI failures. | Independent brief, explicitly pressure-tested as an anti-pattern. | `03_ARCHITECTURE` §§4.2–4.3, 8, 10.4; `ARC-048`, `ARC-049`, `ARC-161`, `ARC-232`; `05_ROADMAP` anti-speculation rules. | A registry would duplicate Ash/Splode and application boundaries, turn implementation detail into a false public authority and create maintenance ceremony without a current contract. | `REJECT_UNNECESSARY_COMPLEXITY` | Reject now. Reopen only if an approved external contract proves that a bounded, versioned code set is needed for a named interoperability purpose. STOP: none. |
| A-11 | Provider exceptions, raw responses and diagnostic evidence stay behind provider adapters and do not rewrite business state or become public diagnostic detail. | Independent brief, provider failure/evidence question. | `03_ARCHITECTURE` §§8.3, 10.4, 12.1, 12.3; `ARC-147`, `ARC-232`, `ARC-267`, `ARC-270`; `ARQ-PERF-028`, `ARQ-PERF-039`; `FLOW-02`, `FLOW-07`, `FLOW-09`. | Current provider evidence, adapter, retry, redaction and authority rules already cover the requirement. | `ALREADY_GOVERNED_NO_CHANGE` | No provider-specific error layer is added. Concrete adapter conventions remain JIT/policy work. STOP: none. |

### Track B: Observability refinement

| Key | Proposition and requirement | Proposal provenance | Current evidence | Gap analysis and rationale | Primary classification | Routing, rejected mechanism, revisit and STOP |
|---|---|---|---|---|---|---|
| B-01 | The platform needs metrics, distributed traces, structured operational logs and governed domain-outcome signals, with Audit & Evidence and security evidence kept separate. | Independent Stage 3B Observability brief. | `03_ARCHITECTURE` §12.3; `ARC-267`, `ARC-270`, `ARC-271`, `ARC-275`; `04_DOMAIN_MAP` ownership row for incident/release evidence; `PLATFORM_OPERATING_MODEL` §§3, 9. | This is already an explicit architecture invariant. | `ALREADY_GOVERNED_NO_CHANGE` | No observability law or technical plane is added. STOP: none. |
| B-02 | Runtime/platform telemetry and capability/application operational telemetry must be distinguishable without creating a technical Observability Domain. | Independent brief, proposed plane distinction. | `03_ARCHITECTURE` §12.3; `ARC-267`, `ARC-273`–`ARC-275`; `ARQ-PERF-023`, `ARQ-PERF-083`, `ARQ-PERF-107`, `ARQ-PERF-135`; `04_DOMAIN_MAP` §§2, 4. | Current law already distinguishes platform resource evidence from capability outcome signals. The distinction is semantic, not a missing domain. | `ALREADY_GOVERNED_NO_CHANGE` | Keep the distinction in instrumentation and operational views. Do not create an Observability Domain. STOP: none. |
| B-03 | Business/reporting/derived measurement must remain distinct from operational telemetry and must not become business authority. | Independent brief, measurement-plane question. | `03_ARCHITECTURE` §§10.4, 12.3; `ARC-267`, `ARC-270`, `ARC-275`; `00_PLATFORM` analytics rules; `04_DOMAIN_MAP` Analytics and Experimentation rows; `PLATFORM_OPERATING_MODEL` §9. | Existing law states the separation. Dashboard and report definitions are downstream conventions. | `ALREADY_GOVERNED_NO_CHANGE` | Preserve `Audit ≠ operational logs ≠ Analytics ≠ business authority`. No second telemetry authority store. STOP: none. |
| B-04 | Audit & Evidence, security evidence and incident diagnostic evidence need separate purpose, sensitivity, retention and access handling from ordinary logs. | Independent brief, evidence-class question. | `03_ARCHITECTURE` §§12.3–12.4, 14; `ARC-131`, `ARC-132`, `ARC-267`, `ARC-270`, `ARC-277`, `ARC-290`; `04_DOMAIN_MAP` §§2, 4; `ARQ-IAM-007`. | Purpose and access distinctions are already governed. | `ALREADY_GOVERNED_NO_CHANGE` | No technical evidence domain is created. Exact retention and operational products remain current downstream gates. STOP: none. |
| B-05 | Correlation across synchronous, durable-async and provider boundaries must avoid sensitive identity in tracing keys; metrics need bounded cardinality; logs need minimisation; tracing needs controlled sampling. | Independent brief, refinement of existing telemetry law. | `03_ARCHITECTURE` §12.3; `ARC-268`–`ARC-271`, `ARC-278`, `ARC-290`; `ARQ-IAM-007`, `ARQ-PERF-023`; `FLOW-01`, `FLOW-02`, `FLOW-07`. | The exact proposed refinements are current law, including privacy, cardinality, sampling and failure isolation. | `ALREADY_GOVERNED_NO_CHANGE` | No universal trace vendor or raw-identity labels. Implementation field names and sampling values are JIT/policy work. STOP: none. |
| B-06 | Database, queue and realtime telemetry must expose the evidence needed to distinguish latency, pool/lock/resource pressure, freshness, saturation, retries, fan-out and amplification, with actionable owned alerts. | Independent brief, operational coverage question. | `03_ARCHITECTURE` §§12.3–12.4, 13; `ARC-273`–`ARC-277`; `ARQ-PERF-083`, `ARQ-PERF-107`, `ARQ-PERF-135`, `ARQ-PERF-136`; `FLOW-07`, `FLOW-09`. | Current architecture names the relevant evidence and alert ownership. | `ALREADY_GOVERNED_NO_CHANGE` | No new telemetry authority or universal dashboard is needed. Exact dashboards are downstream. STOP: none. |
| B-07 | Telemetry handlers and exporters must remain bounded, non-blocking and failure-isolated. Exporter outage may reduce diagnosis but must not corrupt business correctness or create unbounded backpressure. | Independent brief, telemetry reliability question. | `03_ARCHITECTURE` §§12.1, 12.3; `ARC-278`; `ARQ-PERF-145`, `ARQ-PERF-151`, `ARQ-PERF-166`; current Telemetry documentation. | Already governed as a platform failure-isolation rule. | `ALREADY_GOVERNED_NO_CHANGE` | No synchronous telemetry dependency in authoritative transactions. Concrete handler/testing conventions can be policy work. STOP: none. |
| B-08 | Add a new three-plane model, technical Observability Domain or second authority store merely to rename operational, analytical and audit distinctions. | Independent brief, proposed model pressure-tested against current law. | `03_ARCHITECTURE` §12.3; `ARC-267`, `ARC-270`, `ARC-275`, `ARC-290`; `04_DOMAIN_MAP` §§2, 4; `05_ROADMAP` anti-speculation rules. | The model adds names and ownership ambiguity without a semantic gap. It risks confusing Audit, Analytics, operational evidence and business authority. | `REJECT_UNNECESSARY_COMPLEXITY` | Reject the new plane/domain/store. Reopen only if an actual cross-capability authority or retention conflict survives the existing distinctions. STOP: none. |
| B-09 | Establish concrete conventions for telemetry naming, required context, ownership, dashboards, signal quality, retention/access and incident evidence capture, proportionate to risk. | Independent brief, implementation refinement question. | `03_ARCHITECTURE` §§12.3–12.4, 15; `ARC-276`–`ARC-282`, `ARC-290`; `PLATFORM_OPERATING_MODEL` §§3, 9; `05_ROADMAP` operational evidence rules. | Architecture states what evidence must exist, but not every event name, dashboard layout or team workflow. Those choices can vary while preserving law. | `ENGINEERING_POLICY_GRILL_REQUIRED` | Engineering-Policy Grill question: which risk-class conventions prove current observability law without mandating a vendor or a universal dashboard? Do not write the standard here. Future evidence: first production capability, incident review, cardinality/privacy failure or repeated signal disagreement. STOP: none. |
| B-10 | Require OpenTelemetry or a named telemetry vendor/backend as an Architecture condition before a real workload or integration need exists. | Independent brief, technology-choice pressure test. | `03_ARCHITECTURE` §12.3 prefers vendor-neutral tracing and leaves products downstream; `ARC-271`, `ARC-278`; current Telemetry and OpenTelemetry documentation. | A vendor-neutral architecture does not imply one implementation vendor. The mandate would add speculative infrastructure. | `REJECT_UNNECESSARY_COMPLEXITY` | Reject the upfront mandate. Revisit a backend/instrumentation choice when an approved capability has a measured interoperability, export or support requirement. STOP: none. |

### Track C: Native Compute / Rustler

| Key | Proposition and requirement | Proposal provenance | Current evidence | Gap analysis and rationale | Primary classification | Routing, rejected mechanism, revisit and STOP |
|---|---|---|---|---|---|---|
| C-01 | Ordinary Elixir/BEAM code is the default for pure deterministic logic and ordinary application work. | Independent Stage 3B Native Compute brief. | `03_ARCHITECTURE` §§4.2–4.3; `ARC-033`, `ARC-044`, `ARC-045`; `ARQ-SYS-005`, `ARQ-PERF-002`; `05_ROADMAP` §3.2. | The default is already explicit. | `ALREADY_GOVERNED_NO_CHANGE` | No native component is introduced. STOP: none. |
| C-02 | Optimisation must follow a measured bottleneck and the simplest lawful response. Native compute is an escape hatch, not a hypothetical performance feature. | Independent brief, evidence-gated optimisation question. | `03_ARCHITECTURE` §§4.3, 13; `ARC-057`, `ARC-058`, `ARC-291`–`ARC-327`; `ARQ-PERF-002`, `ARQ-PERF-019`, `ARQ-PERF-021`–`ARQ-PERF-024`; `REFERENCE_FLOW_PRESSURE_TESTS` Phase 3 contract. | Evidence-gated optimisation and staged proof are already governed. No current executable workload proves a native need. | `ALREADY_GOVERNED_NO_CHANGE` | No benchmark, NIF or Rustler work is started in Stage 3B. STOP: none. |
| C-03 | If measured workload evidence shows ordinary BEAM cannot meet a required CPU/resource envelope safely or economically, Architecture must decide whether a bounded native seam is permitted and what boundary it preserves. The question includes CPU-bound versus blocking/native-I/O work and NIF versus port/external worker options, without selecting one here. | Independent brief. This is architectural only because it may change an execution-model boundary. | `03_ARCHITECTURE` §§4.3, 8, 12.1, 13; `ARC-033`, `ARC-057`–`ARC-058`, `ARC-291`–`ARC-327`; `ARQ-PERF-019`, `ARQ-PERF-021`–`ARQ-PERF-024`; no current executable workload evidence. | Existing evidence-first escape-hatch law is sufficient until a real workload exists. `ARC-057` and `ARC-058` already require justification, bounded scope and invariant preservation; there is no current native seam to decide. | `DEFER_NO_CURRENT_EVIDENCE` | Defer all native-seam decisions. Reopen only when representative profiling demonstrates a material unmet requirement after ordinary BEAM, query/data-shape, async and topology alternatives are tested safely and economically. If reopened, Architecture may then decide whether a native seam is permitted, which workload classes remain outside a NIF and which boundary must be preserved. Do not answer those questions now. STOP: no upstream contradiction. |
| C-04 | A native component, if later admitted, needs scheduler/resource/failure/timeout/cancellation/deployment/observability/test/fallback/security constraints. The durable invariant and the implementation proof must be separated. | Independent brief, including dirty schedulers, memory ownership, panic/crash containment and portability. | Architecture already requires bounded resources, failure isolation, recovery, observability, security and evidence: `03_ARCHITECTURE` §§12–15; `ARC-058`, `ARC-131`, `ARC-267`–`ARC-290`, `ARC-291`–`ARC-327`; Erlang NIF and Rustler primary documentation. | C-04 is wholly contingent on a native seam that has not been admitted and no current workload triggers that decision. Its checklist is valuable future reopening/proof evidence, not present Architecture or Engineering-Policy scope. | `DEFER_NO_CURRENT_EVIDENCE` | Defer the native safety checklist as current Grill work. Retain it as future reopening criteria: if C-03 is later triggered and Architecture admits a native seam, reclassify/split as appropriate between the minimum native failure/resource/authority boundary and the engineering proof of scheduler safety, memory bounds, panic/crash containment, timeout/cancellation, portability, observability, testing, fallback/recovery and security. Do not select Rustler, add Rust or create a native standard now. Future trigger: an approved, measured C-03 workload. STOP: none. |
| C-05 | Native code may not contain business rules, durable business authority, authoritative state mutation or a second business-law layer. | Independent brief, explicit anti-authority rule. | `03_ARCHITECTURE` §§4.2–4.3, 7, 8; `ARC-033`, `ARC-044`–`ARC-049`, `ARC-057`–`ARC-058`; `04_DOMAIN_MAP` §§2, 4. | Current application/domain authority and controlled escape-hatch law already prohibit this. | `ALREADY_GOVERNED_NO_CHANGE` | A native component, if ever approved, remains subordinate computation/infrastructure. STOP: none. |
| C-06 | Make Rustler/NIFs the standard native-compute path for the platform or add a Rust toolchain before a measured need exists. | Independent brief, Rustler selection pressure test. | `03_ARCHITECTURE` §§4.3, 13; `ARC-057`–`ARC-058`, `ARC-291`–`ARC-327`; `05_ROADMAP` §3.2; no current workload or native component. | The proposal confuses one implementation option with an architecture requirement and creates build, deployment and security burden without value. | `REJECT_UNNECESSARY_COMPLEXITY` | Reject the platform-wide baseline. Reopen only after C-03 evidence and an approved Architecture decision. STOP: none. |
| C-07 | Evaluate and select Rustler for a real workload now, before profiling ordinary BEAM and other lawful options. | Independent brief, actual Rustler-selection question. | `03_ARCHITECTURE` §§4.3, 13; `ARC-057`, `ARC-058`, `ARC-291`–`ARC-327`; `ARQ-PERF-019`; no current executable workload, `mix.exs`, `Cargo.toml` or native component in the reviewed baseline. | The selection may become legitimate, but current evidence does not identify a workload, envelope, safety case or portability need. | `DEFER_NO_CURRENT_EVIDENCE` | Do not add Rustler or Rust dependencies. Revisit with representative profiles, BEAM/query/async comparisons, failure evidence, deployment constraints and a security review. STOP: none. |
| C-08 | Use a NIF or dirty scheduler as a generic replacement for durable async execution, worker isolation or long-running/blocking I/O handling. | Independent brief, CPU-bound versus blocking/native-I/O pressure test. | `03_ARCHITECTURE` §§4.1, 8, 12.1; `ARC-033`, `ARC-147`, `ARC-154`, `ARC-161`; `ARQ-PERF-017`, `ARQ-PERF-094`, `ARQ-PERF-109`; Erlang NIF guidance distinguishes scheduler execution and does not turn arbitrary blocking work into a durable workflow. | This creates a second execution model for work already governed by LiveView, application, queue and provider boundaries. It also does not supply durable retry, cancellation or recovery semantics. | `REJECT_UNNECESSARY_COMPLEXITY` | Reject the generic substitution. Reopen only for a measured workload whose execution model is explicitly decided by Architecture and whose durable orchestration remains outside the native call. STOP: none. |

### Track D: Engineering Quality

| Key | Proposition and requirement | Proposal provenance | Current evidence | Gap analysis and rationale | Primary classification | Routing, rejected mechanism, revisit and STOP |
|---|---|---|---|---|---|---|
| D-01 | The platform needs proportionate code structure, tests, review, proof, security/privacy, failure/recovery, performance and release evidence. | Independent Stage 3B Engineering Quality brief. | `03_ARCHITECTURE` §§12–15; architecture enforcement matrix in §15; `ARC-070`, `ARC-076`, `ARC-131`, `ARC-284`–`ARC-286`, `ARC-291`–`ARC-327`; `ARQ-PERF-021`–`ARQ-PERF-024`, `ARQ-PERF-112`, `ARQ-PERF-156`. | The durable expectations and proportionality rule already exist. | `ALREADY_GOVERNED_NO_CHANGE` | No second Architecture quality law is needed. Engineering Policy may define proof formats and team practice. STOP: none. |
| D-02 | Documentation and `@spec`/typespec usage should be risk- and value-proportional: strong at public, authoritative, security/privacy, concurrency and complex boundary code; not mandatory on every trivial private helper. | Independent brief, documentation/typespec question. | `03_ARCHITECTURE` §§4.2–4.3, 15; `ARC-027`, `ARC-031`, `ARC-048`, `ARC-058`; current Elixir typespec documentation. | This is a coding and maintainability practice. Two implementations can meet current invariants with different documentation depth. | `ENGINEERING_POLICY_GRILL_REQUIRED` | Engineering-Policy Grill question: what risk classes require docs, typespecs and named rationale, and what evidence is enough without burdening trivial code? Do not turn style preference into Architecture Law. Future evidence: defects caused by undocumented contracts or a real public/authoritative boundary. STOP: none. |
| D-03 | Formatting, linting, static analysis, typespec checking, dependency hygiene and reproducible build checks should be part of proportionate engineering practice. | Independent brief, tooling and hygiene question. | `03_ARCHITECTURE` §15; `ARC-284`–`ARC-285`, `ARC-291`–`ARC-327`; `05_ROADMAP` anti-ceremony rules; current Credo, Dialyzer and Mix documentation. | Tools and thresholds are implementation choices. The architecture requires evidence and safe boundaries, not one toolchain or universal severity policy. | `ENGINEERING_POLICY_GRILL_REQUIRED` | Engineering-Policy Grill question: which checks, scope and failure rules produce useful evidence for each risk class without making a named tool an authority? Do not pin versions or add tools in Stage 3B. Future evidence: a real repository baseline or repeated defect class. STOP: none. |
| D-04 | Testing should rise with consequence and complexity, including unit/integration/acceptance, property/invariant, concurrency, failure/recovery and boundary tests where the risk warrants it. | Independent brief, test proportionality question. | `03_ARCHITECTURE` §§8, 12–15; `ARC-070`, `ARC-076`, `ARC-161`, `ARC-284`–`ARC-286`, `ARC-291`–`ARC-327`; `ARQ-PERF-021`–`ARQ-PERF-024`, `ARQ-PERF-112`, `ARQ-PERF-156`; current ExUnit and StreamData documentation. | The architecture names proof obligations, but test selection and depth are engineering practice. | `ENGINEERING_POLICY_GRILL_REQUIRED` | Engineering-Policy Grill question: how should teams choose test depth for pure helpers, authoritative transitions, privacy/security code, financial/entitlement flows, concurrent workflows, migrations, provider adapters and UI helpers? No universal test matrix is written here. Future evidence: first affected Feature Pack and its risk classification. STOP: none. |
| D-05 | Code review, CI evidence, security/privacy checks, maintainability checks and proof records should demonstrate that implementation preserves current law. | Independent brief, review and CI evidence question. | `03_ARCHITECTURE` §§12.3–12.4, 14–15; `ARC-131`, `ARC-267`–`ARC-290`, `ARC-284`–`ARC-286`; `PLATFORM_OPERATING_MODEL` §§3, 9; `05_ROADMAP` release gates. | The cross-platform invariants are already Architecture. The review checklist, CI evidence shape, security scan choice and maintainability practice are policy. | `ENGINEERING_POLICY_GRILL_REQUIRED` | Engineering-Policy Grill question: what minimum evidence must a change carry, by risk class, for review, CI, security/privacy and operational proof? Do not manufacture CI stages or make CI a second authority. Future evidence: selected implementation slice, release gate or incident finding. STOP: none. |
| D-06 | Production migrations are reviewed code, safe across rolling deployment, tested for lock/runtime/failure/rollback impact and observable. | Independent brief, migration-safety question. | `03_ARCHITECTURE` §§7.2, 12.1, 13, 15; `ARC-070`, `ARC-076`, `ARC-284`–`ARC-286`; `ARQ-PERF-081`, `ARQ-PERF-156`; `FLOW-08`. | The durable migration-safety requirement already exists. | `ALREADY_GOVERNED_NO_CHANGE` | Do not create a new migration law. Exact migration checklists are later policy/JIT work. STOP: none. |
| D-07 | Architecture-boundary tests or dependency checks should catch direct cross-boundary persistence, authority bypass, unsafe cache use and other violations. The durable boundary and the test/check practice must be separated. | Independent brief, architecture-boundary test question. | `03_ARCHITECTURE` §15 enforcement matrix; `ARC-027`, `ARC-046`, `ARC-048`, `ARC-052`, `ARC-058`, `ARC-154`; `04_DOMAIN_MAP` §§2, 4. | Existing Architecture and Domain authority/no-bypass rules already define the durable invariant. Whether every boundary is checked by static analysis, tests, review or another mechanism is policy and may vary by risk. | `ENGINEERING_POLICY_GRILL_REQUIRED` | Engineering-Policy Grill question: which static checks, dependency checks, architecture-boundary tests, review checks or CI evidence are valuable, maintainable and proportionate for proving the already-governed boundary? Existing Architecture is the mandatory constraint; there is no remaining Architecture decision. Do not create a universal checker. Future evidence: an approved codebase and a demonstrated boundary-bypass risk. STOP: none. |
| D-08 | Apply maximum documentation, typespec, test, review and CI ceremony uniformly to every function and change. | Independent brief, explicit proportionality pressure test. | `03_ARCHITECTURE` §§13, 15; `ARC-291`–`ARC-327`; `05_ROADMAP` anti-overengineering and development-friction rules. | Uniform maximum ceremony conflicts with risk-proportional proof and adds friction without protecting a durable invariant. | `REJECT_UNNECESSARY_COMPLEXITY` | Reject. Reopen only if a named failure class shows that the proportional model cannot protect a particular risk class. STOP: none. |
| D-09 | Manufacture CI stages, coverage thresholds or tool adoption solely to make the repository look mature before implementation risk or delivery scope exists. | Independent brief, anti-ceremony/tooling pressure test. | `03_ARCHITECTURE` §§13, 15; `ARC-284`–`ARC-286`, `ARC-291`–`ARC-327`; `05_ROADMAP` §§3.2, 4; no application implementation baseline. | The proposal creates ceremony before there is a repository, capability or evidence need. | `REJECT_UNNECESSARY_COMPLEXITY` | Reject. Reopen when an approved implementation slice, release gate or incident requires a specific check with a named failure mode. STOP: none. |

## Track pressure tests

The following tests were run against the candidate concerns. They validate the classifications above; they do not create new law.

### Errors & Diagnostics

| Pressure case | Result |
|---|---|
| HTTP status versus application/business error | Transport evidence cannot establish business authority under A-02. Existing ARC-027, ARC-028 and ARC-048 already govern the cross-surface authority invariant; A-08 routes representation and mapping conventions to Engineering Policy. |
| Safe participant message versus internal diagnostic detail | Existing minimisation, access and redaction law covers the split under A-04. |
| Occurrence/reference ID versus trace/correlation ID | Existing correlation and non-authority rules cover the identity separation under A-05. A participant-facing occurrence contract is unsupported and deferred under A-06. |
| Validation/domain/application failure versus system/provider failure | Existing error-class-aware retry and terminal/reconciliation law covers the durable behaviour under A-07. Ash/Splode mapping is a policy question under A-08. |
| Provider failure versus platform business state | Provider evidence stays behind adapters and cannot rewrite originating truth under A-02 and A-11. |
| Retryable, unresolved and terminal failure | Existing bounded, owned retry and pending/reconciliation rules cover the distinction under A-02 and A-07. |
| Privacy, redaction and supportability | Public detail is minimised and diagnostic evidence is restricted under A-04 and A-11. Support-facing occurrence IDs remain deferred until a support need is evidenced. |
| Stable public contract versus implementation detail | Existing Architecture governs the shared authority invariant. A-09 defers choosing RFC Problem Details until an actual HTTP/API boundary exists, while A-08 routes implementation mapping later. |
| HTTP/API, LiveView and background-worker differences | Surface differences do not permit business-rule duplication under existing Architecture. A-08 covers the later implementation mapping. |

### Observability

| Pressure case | Result |
|---|---|
| Telemetry runtime failure | Visibility may degrade without changing business correctness under B-07. |
| Exporter outage or telemetry backpressure | Bounded, non-blocking, failure-isolated handling is already governed. |
| High-cardinality accident | Bounded dimensions and opaque correlation are already governed under B-05. |
| Sensitive data leakage | Minimisation before redaction, purpose-specific access and separate evidence classes are already governed under B-04 and B-05. |
| Trace sampling | Controlled sampling is already part of the current trace law; no vendor mandate follows. |
| Missing business-outcome signal | `ARC-275` already requires important capabilities to expose operational domain outcome signals without moving authority into telemetry. |
| Dashboard/report disagreement | Business/reporting measurement remains distinct from operational signals and authoritative state under B-03. Definitions and ownership route to B-09. |
| Audit/log/Analytics confusion | The existing separation is explicit. B-08 rejects a new plane or store to rename it. |
| Incident evidence reconstruction | Release/configuration/incident correlation, owned runbooks and post-incident evidence are already covered by B-04 and current incident law. |

### Native Compute

| Pressure case | Result |
|---|---|
| CPU-bound hotspot | Profile first. A measured unmet envelope can trigger C-03; hypothetical speed is covered by C-02 and C-07. |
| Long-running native call | It cannot become a generic substitute for durable async or worker isolation under C-08. |
| NIF crash or Rust panic | The future native invariant and engineering proof checklist are retained under deferred C-04. No native code is admitted now. |
| Scheduler starvation | C-03 and C-04 remain deferred; execution-class and safety questions reopen only after native-workload evidence. |
| Native memory growth or ownership bug | C-04 retains bounded resource/failure and ownership proof as future reopening criteria. |
| Malformed input | Native code remains subordinate computation; validation and authority stay in the application boundary under C-05. |
| Node restart | Durable authority and recovery remain outside native execution under C-05 and C-08. |
| Deployment portability or toolchain failure | No Rustler baseline is adopted. If C-03 reopens, portability becomes part of the C-04 proof checklist. |
| Concurrency | Current transaction/idempotency law remains in the application and database boundary; native computation cannot become authority. |
| Timeout/cancellation | A native call does not supply durable cancellation or reconciliation by itself. If native work is later admitted, C-04 retains this as a proof criterion. |
| Telemetry | Any later native work would need bounded diagnostic signals without making telemetry authoritative; this remains a C-04 reopening criterion. |
| Fallback/recovery | A fallback is a later implementation proof, not a reason to introduce a native seam now. |
| Authoritative business-state mutation | Explicitly excluded by C-05. |

### Engineering Quality

| Pressure case | Result |
|---|---|
| Simple pure helper | Low ceremony can be correct. D-02, D-04 and D-08 reject universal maximum requirements. |
| Authoritative business transition | Strong contract documentation, policy tests, concurrency/idempotency proof and review are proportionate under D-02 through D-05. |
| Privacy/security code | Security/privacy evidence rises with consequence under D-05; the invariant remains current Architecture. |
| Financial/entitlement code | Durable transition and duplicate/retry proof are already Architecture; policy chooses the concrete test/review evidence. |
| Concurrent/idempotent workflow | Property, concurrency, failure/recovery and boundary tests may be warranted under D-04. |
| Migration | Existing migration safety law covers the durable requirement under D-06; later policy can provide a checklist. |
| Provider adapter | Provider isolation, retry, redaction and reconciliation are already governed; adapter tests and review route to D-04/D-05. |
| UI-only presentation helper | Low-risk documentation and test depth may be lower, provided it does not bypass authority or privacy law. |

## Architecture versus Engineering Policy routing

The queue boundary is intentionally narrow:

| Concern | Durable WHAT | Implementation HOW | Result |
|---|---|---|---|
| Cross-surface errors | Existing authority/status/public-diagnostic invariant governed by `ARC-027`, `ARC-028` and `ARC-048` | Ash/Splode mappings, envelopes, labels, messages and surface adapters | A-03 already governed; A-08 Engineering-Policy Grill |
| Native compute | Existing evidence-gated escape-hatch constraints; no native seam is admitted without a real workload | Dirty-scheduler or equivalent choice, memory ownership, build, tests, panic handling, timeout/cancellation, fallback and security evidence if later triggered | C-03 and C-04 deferred |
| Boundary enforcement | Existing application/domain authority and no-bypass invariant | Static checks, dependency checks, tests, review and CI evidence selected by risk | D-07 Engineering-Policy Grill |
| Observability | Existing separation of operational, domain-outcome, audit/security and business/reporting evidence | Event names, fields, dashboards, ownership, retention workflows and backend integration | B-01–B-07 already governed; B-09 policy |
| General quality | Existing proof and hard-invariant requirements | Documentation, typespecs, linting, tests, CI, review and dependency hygiene | D-01/D-06 already governed; D-02–D-05 policy |

The test result is not a claim that every current concern is fully implemented. It is a routing result. Later policy work must preserve the current invariants, and later Architecture work must not absorb choices that can vary between correct implementations.

## Classification summary

### Counts

| Primary classification | Count |
|---|---:|
| `ALREADY_GOVERNED_NO_CHANGE` | 19 |
| `ARCHITECTURE_GRILL_REQUIRED` | 0 |
| `ENGINEERING_POLICY_GRILL_REQUIRED` | 7 |
| `SPLIT_ARCHITECTURE_AND_ENGINEERING_POLICY` | 0 |
| `DEFER_NO_CURRENT_EVIDENCE` | 5 |
| `REJECT_UNNECESSARY_COMPLEXITY` | 7 |
| `UPSTREAM_CONTRADICTION_STOP` | 0 |
| **Total propositions** | **38** |

### Queue A: Already governed

No new law or policy is required for these propositions:

- **A-01** — authoritative application operation owns result/error semantics. Evidence: `03_ARCHITECTURE` §§4.1–4.3, 8; `ARC-027`, `ARC-028`, `ARC-031`, `ARC-033`, `ARC-046`, `ARC-048`.
- **A-02** — transport, provider and queue state cannot become business authority; pending/retry/terminal/unknown states remain distinct. Evidence: `03_ARCHITECTURE` §§7, 8.3, 12.1; `ARC-052`, `ARC-147`, `ARC-154`, `ARC-161`, `ARC-232`.
- **A-03** — the cross-surface authority/result invariant is already governed by the authoritative application operation, thin delivery layers and approved application contracts. Evidence: `03_ARCHITECTURE` §§4, 8, 10.4, 12.1; `ARC-027`, `ARC-028`, `ARC-046`, `ARC-048`, `ARC-161`, `ARC-232`.
- **A-04** — safe public messages and internal diagnostics remain separate. Evidence: `03_ARCHITECTURE` §§10.4, 12.3, 14; `ARC-131`, `ARC-132`, `ARC-232`, `ARC-267`, `ARC-270`, `ARC-290`.
- **A-05** — diagnostic identity does not replace trace, actor, subject, resource or business authority. Evidence: `03_ARCHITECTURE` §§4, 7, 8, 12.3; `ARC-046`, `ARC-151`, `ARC-154`, `ARC-268`, `ARC-270`.
- **A-07** — error classes drive bounded retry, terminal handling, reconciliation and recovery. Evidence: `03_ARCHITECTURE` §§8.2–8.3, 12.1; `ARC-147`, `ARC-154`, `ARC-161`, `ARC-232`.
- **A-11** — provider exceptions/evidence stay behind adapters and cannot rewrite business truth. Evidence: `03_ARCHITECTURE` §§8.3, 10.4, 12.1, 12.3; `ARC-147`, `ARC-232`, `ARC-267`, `ARC-270`.
- **B-01** — metrics, traces, structured logs and domain signals are coherent, with audit/security separate. Evidence: `03_ARCHITECTURE` §12.3; `ARC-267`, `ARC-270`, `ARC-271`, `ARC-275`.
- **B-02** — platform/runtime and capability operational telemetry are semantically distinguishable without a technical Domain. Evidence: `03_ARCHITECTURE` §12.3; `ARC-267`, `ARC-273`–`ARC-275`.
- **B-03** — reporting/derived measurement is not operational telemetry or business authority. Evidence: `03_ARCHITECTURE` §§10.4, 12.3; `ARC-267`, `ARC-270`, `ARC-275`; `04_DOMAIN_MAP` Analytics/Experimentation ownership.
- **B-04** — audit, security and incident evidence have separate purpose/access/retention handling. Evidence: `03_ARCHITECTURE` §§12.3–12.4, 14; `ARC-131`, `ARC-132`, `ARC-267`, `ARC-270`, `ARC-277`, `ARC-290`.
- **B-05** — correlation, cardinality, privacy, minimisation and sampling are already governed. Evidence: `03_ARCHITECTURE` §12.3; `ARC-268`–`ARC-271`, `ARC-278`, `ARC-290`.
- **B-06** — database, queue, realtime and alert signals cover operational diagnosis. Evidence: `03_ARCHITECTURE` §§12.3–12.4, 13; `ARC-273`–`ARC-277`.
- **B-07** — telemetry remains bounded, non-blocking and failure-isolated. Evidence: `03_ARCHITECTURE` §§12.1, 12.3; `ARC-278`.
- **C-01** — ordinary BEAM/Elixir is the default. Evidence: `03_ARCHITECTURE` §§4.2–4.3; `ARC-033`, `ARC-044`, `ARC-045`.
- **C-02** — optimisation follows measured bottlenecks and staged proof. Evidence: `03_ARCHITECTURE` §§4.3, 13; `ARC-057`, `ARC-058`, `ARC-291`–`ARC-327`; `ARQ-PERF-019`.
- **C-05** — native code cannot contain business rules or durable authority. Evidence: `03_ARCHITECTURE` §§4.2–4.3, 7, 8; `ARC-033`, `ARC-044`–`ARC-049`, `ARC-057`–`ARC-058`.
- **D-01** — current Architecture already requires proportionate tests, review, proof, security/privacy, failure/recovery and performance evidence. Evidence: `03_ARCHITECTURE` §§12–15; `ARC-284`–`ARC-286`, `ARC-291`–`ARC-327`.
- **D-06** — migration safety is already governed. Evidence: `03_ARCHITECTURE` §§7.2, 12.1, 13, 15; `ARC-070`, `ARC-076`; `ARQ-PERF-156`.

### Queue B: Architecture Grill

No independent Stage 3B proposition currently requires an Architecture-level decision. A-03 and D-07 are constrained by existing Architecture Law, while C-03 and C-04 are deferred until native-workload evidence exists.

### Architecture Grill provenance

This zero-count independent queue does not cancel or skip the programme's Architecture Grill. The Architecture Grill remains `NOT_STARTED / NEXT` because the governed Product-derived AR-000 v1.1.0 amendment from Stage 3A.2 is a separate input stream.

Architecture Grill input stream A — Product-derived:

- Stage 3A.2's governed AR-000 v1.1.0 additions and their downstream Architecture closure.

Architecture Grill input stream B — independent Stage 3B:

- Zero current propositions.

### Queue C: Engineering-Policy Grill

These are the only unsplit Engineering-Policy Grill inputs:

- **A-08** — Which risk-proportional Ash/Splode mapping, public-message, redaction, localisation and retry-class conventions should teams use without a parallel error framework?
- **B-09** — Which risk-class conventions prove telemetry naming, context, ownership, dashboards, signal quality, access and incident evidence without mandating a vendor?
- **D-02** — Which risk classes require documentation and typespecs, and what is enough for public, authoritative, security-sensitive and complex code?
- **D-03** — Which formatting, lint, static analysis, typespec, dependency and reproducible-build checks provide value, with what scope and failure policy?
- **D-04** — How should teams choose test depth for pure helpers, authoritative transitions, privacy/security code, financial/entitlement flows, concurrency, migrations, provider adapters and UI helpers?
- **D-05** — What review, CI, security/privacy and proof evidence must accompany a change by risk class, without making CI a second authority?
- **D-07** — Which static checks, dependency checks, architecture-boundary tests, review checks or CI evidence are valuable, maintainable and proportionate for proving the already-governed boundary?

### Queue D: Deferred / rejected

Deferred until evidence exists:

- **A-06** — Participant/support occurrence ID on every surface. Reopen for a real support workflow, incident pattern, API contract or demonstrated need beyond correlation.
- **A-09** — RFC 9457 as a universal API representation. Reopen when a real HTTP/API boundary and interoperability requirement are approved.
- **C-03** — Native execution seam. Reopen only when representative profiling demonstrates a material unmet requirement after ordinary BEAM, query/data-shape, async and topology alternatives are tested safely and economically; Architecture may then decide the seam and workload boundary.
- **C-04** — Native scheduler/resource/failure/timeout/cancellation/deployment/observability/test/fallback/security checklist. Reopen only with an approved, measured C-03 workload; then split the minimum durable boundary from the engineering proof as appropriate.
- **C-07** — Rustler selection for an actual workload now. Reopen with representative profiling, ordinary BEAM/query/async comparison, deployment constraints, failure evidence and security review.

Rejected for the current programme:

- **A-10** — giant global error-code registry. Reopen only for a bounded, versioned external interoperability contract.
- **B-08** — three-plane rename, Observability Domain or second telemetry authority store. Reopen only if an actual authority, retention or access conflict survives current law.
- **B-10** — mandatory OpenTelemetry/vendor/backend. Reopen for a measured interoperability, export or support requirement in an approved capability.
- **C-06** — Rustler/NIF platform standard or Rust toolchain baseline. Reopen after C-03 evidence and an Architecture decision.
- **C-08** — NIF/dirty scheduler as generic durable async or blocking-I/O substitute. Reopen only for a measured workload with a separately governed durable orchestration boundary.
- **D-08** — maximum ceremony for every change. Reopen only if a named failure class defeats risk-proportional practice.
- **D-09** — manufactured CI stages, coverage thresholds or tool adoption. Reopen when an approved slice, release gate or incident names a concrete failure mode requiring the check.

## Contradiction and authority result

- **Upstream contradictions:** none found.
- **Product Law changes:** none required.
- **AR-000 changes:** none required.
- **Architecture Law changes:** none made or answered.
- **Engineering Standards:** none created.
- **New Domains:** none created. The four tracks remain technical concerns, not business ownership domains.
- **Governed identifiers:** none created. Existing identifiers are cited only as evidence.
- **Implementation:** none performed.

The Architecture Grill remains `NOT_STARTED / NEXT` after this classification because the governed Product-derived AR-000 v1.1.0 input stream remains downstream work. The independent Stage 3B Architecture queue contributes zero current propositions. The Engineering-Policy Grill remains `NOT_STARTED`.

## External primary sources consulted

Access date for all sources below: 2026-09-04. HexDocs links refer to the stable release documentation available at access time; no prerelease or `main` documentation was used. No package version or dependency constraint is adopted by this artifact.

| Source | Status at access time | Use |
|---|---|---|
| [Ash error handling](https://hexdocs.pm/ash/error-handling.html) | Stable release HexDocs | Current Ash error/result conventions and framework-native extension points |
| [Splode HexDocs](https://hexdocs.pm/splode/Splode.html) | Stable release HexDocs | Current structured error framework model used by Ash |
| [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) | IETF Proposed Standard | Problem Details scope and HTTP representation semantics |
| [Erlang NIF User's Guide](https://www.erlang.org/doc/apps/erts/erl_nif.html) | Current stable OTP documentation | NIF execution, scheduler, resource and failure-safety considerations |
| [Rustler HexDocs](https://hexdocs.pm/rustler/Rustler.html) | Stable release HexDocs | Current Rustler/NIF integration surface; no selection or version decision made |
| [Telemetry HexDocs](https://hexdocs.pm/telemetry/Telemetry.html) | Stable release HexDocs | Event/handler model and bounded handler implications |
| [OpenTelemetry Erlang documentation](https://opentelemetry.io/docs/languages/erlang/) | Official documentation; tracing stable, metrics/logs development | Interoperability context; does not justify a vendor mandate |
| [Elixir typespecs](https://hexdocs.pm/elixir/typespecs.html) | Stable release HexDocs | Typespec purpose and implementation-level usage |
| [Credo HexDocs](https://hexdocs.pm/credo/overview.html) | Stable release HexDocs | Static-analysis tooling context |
| [Dialyzer documentation](https://www.erlang.org/doc/apps/dialyzer/dialyzer.html) | Current stable OTP documentation | Success-typing analysis context |
| [ExUnit HexDocs](https://hexdocs.pm/ex_unit/ExUnit.html) | Stable release HexDocs | Test tooling context |
| [StreamData HexDocs](https://hexdocs.pm/stream_data/StreamData.html) | Stable release HexDocs | Property-testing tooling context |

These sources inform classification only. They do not override the live repository authority and do not authorize dependency installation, implementation or package selection.

## Stage 3B handoff boundary

This artifact is ready for independent review as one bounded Stage 3B input. After review of the exact PR head:

1. Architecture Grill may consume the separate Product-derived Stage 3A.2 / AR-000 v1.1.0 input stream; Stage 3B contributes no current independent Architecture proposition.
2. Engineering-Policy Grill may consume Queue C.
3. No later stage may treat Queue A as new law.
4. Deferred/rejected items require their named evidence trigger before reconsideration.
5. A changed PR head requires a fresh exact-head review.

No merge, Architecture Grill, Engineering-Policy Grill, Architecture amendment, Engineering Standard, Domain Map amendment, Roadmap reconciliation, Atlas reconciliation, HARDEN-02 execution, FP-001 modification or implementation is authorised by this artifact.
