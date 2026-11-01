# Targeted Engineering-Policy Grill

**NON-AUTHORITATIVE / STAGE 4B ENGINEERING-POLICY GRILL EVIDENCE**

> **DOES NOT AMEND PRODUCT LAW**
> **DOES NOT AMEND AR-000**
> **DOES NOT AMEND ARCHITECTURE LAW**
> **DOES NOT CREATE ENGINEERING STANDARDS**
> **DOES NOT INSTALL OR SELECT DEPENDENCIES**
> **NO GOVERNED IDENTIFIERS CREATED**
> **NO IMPLEMENTATION AUTHORISED**
> **LIVE GITHUB AUTHORITY IS CANONICAL**

- **Artifact version:** v0.1.0
- **Date:** 2026-09-04
- **Programme:** Targeted Product Amendment → FP-001 Development Entry Readiness
- **Stage:** Stage 4B — Engineering-Policy Grill
- **Status:** Grill complete with explicit human acceptance; pending independent review of exact PR head
- **Baseline:** `main` at `d2477e2d3d49187610fdee6b5aedb799df8bfe02`
- **Authority:** Current GitHub `main`, routed by `docs/00_platform/README.md` and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`
- **Input stream:** Stage 3B independent Engineering-Policy queue only (`ENGINEERING_POLICY_GRILL_REQUIRED`)

## Scope and stop boundary

This file records the Engineering-Policy HOW conventions required to satisfy the seven Stage 3B policy propositions classified `ENGINEERING_POLICY_GRILL_REQUIRED`.

It does not:

- amend Product Law, Decision Register, AR-000, Architecture Law or `03_ARCHITECTURE`;
- create `ARC-*`, `ARQ-*`, DEC, OQ, Domain, Feature Pack, Engineering Standard or implementation artifacts;
- install packages, edit `mix.exs`, add Elixir/tool configuration or modify `.github/workflows`;
- begin Architecture amendment.

Engineering Standards remain downstream. They are a later separately authorised stage after Architecture amendment. This artifact is active working input for that later standards work and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.

## Provenance streams (must remain separate)

### Stream A — Stage 3B Engineering-Policy input

Direct provenance for this Grill. Exact keys:

`A-08`, `B-09`, `D-02`, `D-03`, `D-04`, `D-05`, `D-07`.

### Stream B — Stage 4A Architecture Grill constraint

Stage 4A (`working/TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md`) is an Architecture constraint, not Engineering-Policy provenance. This Grill does not reopen Product-derived Architecture HOW decisions and does not allocate ARC identifiers.

## Clustering

Five human questions covered the seven propositions plus the shared risk model.

| Question | Covers | Decision |
|---|---|---|
| `EP-Q1` | Shared Engineering-Policy risk model | Accepted with refinement |
| `EP-Q2` | `A-08` | Accepted with refinement |
| `EP-Q3` | `B-09` | Accepted with refinement |
| `EP-Q4` | `D-02`, `D-03`, `D-07` | Accepted with refinement |
| `EP-Q5` | `D-04`, `D-05` | Accepted with refinement |

`EP-Q1` is not a Stage 3B key. It is the classification used by the other four questions.

## Accepted risk model

Three Engineering-Policy risk levels:

- `LOW`
- `STANDARD`
- `HIGH`

Do not introduce a fourth `CRITICAL` tier at current scope.

### LOW

Presentation-only helpers, simple pure utilities and mechanically obvious transformations that have no authoritative, sensitive, concurrent, provider or consequential boundary.

### STANDARD

Ordinary application/domain code where failure is bounded and recoverable and the code does not itself establish high-consequence truth.

### HIGH

A change is `HIGH` whenever it materially involves one or more of:

- authoritative state transitions;
- authentication or authorisation;
- privacy, consent or sensitive data;
- concurrency or idempotency;
- provider reconciliation;
- durable async/recovery;
- migrations affecting authoritative data;
- participant-facing consequential calculations.

The HIGH classification is not optional if one of these triggers genuinely applies.

Named consequence tags, where applicable:

- `financial`
- `entitlement`
- `safety`
- `privacy_deletion`
- `privileged_security`
- `irreversible`

These tags select or strengthen relevant proof obligations. They are not a fourth risk class, Domain ownership, Product classification or Architecture authority.

Authors may propose the risk classification and consequence tags, but consequential classification must be reviewable. A developer may not downgrade a change from HIGH merely to avoid proof requirements. Where classification is reasonably ambiguous, reviewer agreement is required. The later Engineering Standard may define examples and declaration mechanics, but must not create an elaborate scoring system.

This model is Engineering-Policy classification only.

## Human Grill decisions

All five material questions received explicit human acceptance on 2026-09-04.

### EP-Q1 — Shared engineering-policy risk model

- **Stage 3B keys:** none (shared classification)
- **Recommendation:** Option A, three levels with HIGH consequence tags
- **Human decision:** `ACCEPTED WITH REFINEMENT`
- **Accepted policy:** The three-level model and tag list above, including reviewable HIGH classification and no elaborate scoring system.

### EP-Q2 — Error-handling engineering policy

- **Stage 3B keys:** `A-08`
- **Recommendation:** Option A, framework-native Ash/Splode mapping
- **Human decision:** `ACCEPTED WITH REFINEMENT`
- **Accepted policy:** Use the current Ash/Splode error model rather than a parallel NewYou-wide error framework. Business/application meaning remains owned by the authoritative application/action boundary. Use built-in Ash/Splode errors where they express the required meaning. Create custom `Splode.Error` types only when a stable, meaningful application distinction is required and the built-in model is insufficient. Do not create custom error types merely to hold different wording.
- **Participant/public messages:** safe; localisable through the approved Gettext path; no sensitive/internal diagnostic information; no authorisation policy detail; no unsafe existence disclosure where privacy/security requires it.
- **Diagnostics:** richer technical context is allowed internally subject to minimisation, access and redaction.
- **Providers:** adapters translate provider failures into application-understood failure semantics. Raw provider payloads, exception detail and provider SDK semantics do not become participant-facing contracts or business authority.
- **Not created:** a global numeric error-code registry; universal RFC 9457; a universal participant-facing occurrence-ID contract.
- **Retry refinement:** Do not infer retryability solely from the Splode class. Where operationally relevant, the responsible application/provider boundary must distinguish retryable, terminal, and unresolved/unknown/reconciliation-required according to existing Architecture failure semantics. `unknown` does not automatically mean retryable. A provider timeout or ambiguous acknowledgement must not silently become success or trigger blind duplicate retries.
- **Risk proportionality:** `LOW` uses ordinary result/exception handling and no custom application error type unless genuinely needed. `STANDARD` uses framework-native handling, participant-safe/localised copy where user-facing, and diagnostics separated from public output. `HIGH` requires explicit failure/retry/reconciliation semantics where applicable, redaction/leakage proof where privacy/security applies, provider-error translation at the adapter boundary, and non-enumerating behaviour where identity/security requires it.

### EP-Q3 — Operational observability practice

- **Stage 3B keys:** `B-09`
- **Recommendation:** Option A, backend-neutral conventions
- **Human decision:** `ACCEPTED WITH REFINEMENT`
- **Accepted policy:** Adopt backend-neutral operational observability conventions. Do not mandate OpenTelemetry, a telemetry vendor, an APM backend, a dashboard platform, an Observability Domain or a second telemetry authority store.
- **Preserve Architecture:** metrics, traces, structured logs, domain-outcome operational signals and separate Audit/security evidence remain as currently required.
- **Material signals:** stable naming; defined measurements versus contextual metadata; bounded cardinality; opaque correlation; minimum necessary context; explicit owner and purpose.
- **Sensitive data:** minimise before logging/telemetry. Account IDs, participant identifiers, health content and other high-cardinality/sensitive values must not be used casually as metric labels. Correlation identifiers must not become authentication, Account identity or business authority.
- **Alerts and dashboards:** a material alert requires an identified owner, a meaningful operator action or decision, and a clear reason for existing. Do not manufacture alerts simply because a metric exists. Dashboards are projections for operational understanding, never business authority. If a dashboard disagrees with authoritative state, authoritative state wins and the diagnostic discrepancy is investigated.
- **Failure isolation:** telemetry/exporter failure may reduce visibility but must not make an otherwise valid business transaction fail. Telemetry must remain bounded and failure-isolated.
- **HIGH:** where applicable, enough operational evidence to correlate request/job/provider activity, see unresolved obligations or important outcomes, reconstruct consequential incidents, and diagnose provider/reconciliation failures. Sampling may be risk-sensitive. Do not require zero sampling globally.

### EP-Q4 — Code contract and automated-quality policy

- **Stage 3B keys:** `D-02`, `D-03`, `D-07`
- **Recommendation:** Option A, risk-proportional contract plus staged automation
- **Human decision:** `ACCEPTED WITH REFINEMENT`
- **Accepted policy:** Adopt risk-proportional contract evidence plus staged automation. Do not install an Elixir quality toolchain during Stage 4B. Once an authorised Elixir application baseline exists, cheap, deterministic, high-signal checks should become normal blocking evidence. Noisy/style-oriented checks should not automatically block until an approved clean baseline and failure policy exist. Automation should enforce only repeatable, valuable rules whose false-positive burden is acceptably low. Human review remains appropriate for novel Architecture/Domain boundary reasoning and approved escape hatches.
- **Documentation:** `LOW` has no documentation requirement for trivial private helpers; document only where understanding genuinely benefits. `STANDARD` documents meaningful public/application contracts and externally consumed interfaces. `HIGH` documents the relevant contract and short rationale for consequential actions, policies, adapters, escape hatches and other material boundaries. Do not require comments that merely restate the code.
- **Typespecs / equivalent contract evidence:** Do not adopt a rule that every Elixir `def` requires `@spec`. Require useful typespec/equivalent contract evidence for meaningful externally consumed/public interfaces, behaviours/callback boundaries, cross-domain/application interfaces, complex HIGH-risk boundaries, and dense logic where a type contract materially improves understanding or analysis. Trivial mechanically obvious helpers do not need ceremonial typespecs solely because they are public functions. The policy must remain adaptable if Elixir's future type-system capabilities supersede current typespec practice.
- **Automated checks once an application exists:** formatting blocking; compiler warnings under approved policy blocking; reproducible dependency state required; new unexplained static-analysis regressions blocking once a clean approved baseline exists; noisy/style findings advisory or policy-scoped rather than automatically fatal; architecture-boundary automation used where the rule is repeatable and high-signal.
- **Boundary enforcement:** Do not create a universal Architecture checker. Existing Architecture and Domain Law remain authority; automated checks merely provide evidence. Examples worth automating later may include forbidden ordinary Repo writes around an owning boundary, forbidden dependency direction, and UI/delivery code bypassing the application boundary. Approved exceptions/escape hatches must remain possible through explicit governed review rather than hacking around the checker.
- **Tool independence:** this decision does not select Credo, Dialyzer, `mix xref`, Hex `boundary`, a dependency-audit package or exact warning flags.

### EP-Q5 — Test, review and proof policy

- **Stage 3B keys:** `D-04`, `D-05`
- **Recommendation:** Option A, risk-proportional tests plus a justified HIGH proof menu
- **Human decision:** `ACCEPTED WITH REFINEMENT`
- **Accepted policy:** Adopt risk-proportional testing and review, with a justified HIGH proof menu. Do not require universal 100% coverage, property tests everywhere, concurrency tests on non-concurrent code, every expensive proof in permanent CI, or security tooling merely as a maturity badge. CI is evidence. CI is not Product, Architecture or business authority.
- **LOW:** testing may be minimal where logic is mechanically obvious. Non-obvious pure logic should have focused examples. Ordinary engineering review is sufficient.
- **STANDARD:** require appropriate positive behaviour plus important rejection/edge cases. Ordinary application changes should carry enough tests to make their intended contract repeatable.
- **HIGH:** every HIGH change must explicitly evaluate the applicable proof menu. The author must mark applicable/not-applicable with a meaningful reason. The reviewer must agree with the applicability assessment. For HIGH consequence tags such as financial, safety, privacy/deletion, privileged security and material concurrency, weak or unjustified `N/A` classifications must block approval.
- **Possible HIGH proof, where applicable:** positive and negative tests; invariant/state-transition tests; policy/authorisation tests; concurrency/idempotency tests; duplicate/reorder/retry tests; failure/recovery/reconciliation tests; migration safety evidence; sensitive-data leakage/redaction tests; provider reconciliation tests; security/privacy review evidence; reviewer acknowledgement of authority boundaries. Not every HIGH change requires every proof. The proof must follow the actual failure modes.
- **Property testing:** use property/generative testing when a generator can meaningfully attack an invariant or state space. Do not require it by default.
- **Concurrency testing:** required where correctness materially depends on concurrent execution, duplicate requests, ordering or idempotency. Do not require it for code without a concurrency surface.
- **Review expertise:** HIGH changes should receive review appropriate to the applicable consequence tag. This does not manufacture permanent specialist review for LOW/STANDARD work.
- **CI versus JIT:** permanent CI should contain cheap repeatable checks appropriate to the application. Load testing, game days, restore testing, penetration testing and large-scale concurrency proof remain JIT/stage-specific unless repeated evidence shows permanent automation is justified. Do not move later Architecture Proof/Release Readiness work into every PR.
- **Coverage:** do not establish a universal numeric coverage target as proof of correctness. Coverage may be used diagnostically later, but the important question is whether applicable invariants and failure paths have been proven.

## Seven-proposition coverage matrix

| Stage 3B key | Cluster | Human question | Recommendation | Accepted human answer | Accepted policy direction |
|---|---|---|---|---|---|
| `A-08` | Error-handling engineering policy | `EP-Q2` | Framework-native Ash/Splode mapping without a parallel error framework | Accepted with refinement | Ash/Splode remains the error model; public copy is safe/localisable; diagnostics stay internal; retryability is mapped from application/provider semantics, not inferred from Splode class alone |
| `B-09` | Operational observability practice | `EP-Q3` | Backend-neutral conventions without vendor, Domain or dashboard mandate | Accepted with refinement | Stable naming, bounded cardinality, opaque correlation, owned alerts/dashboards, minimisation, failure-isolated telemetry; no OpenTelemetry/vendor/backend selection |
| `D-02` | Code contract and automated quality | `EP-Q4` | Risk-proportional docs/typespecs, not every function | Accepted with refinement | Document and type meaningful public/HIGH contracts; no ceremonial docs or `@spec` on trivial helpers; remain adaptable if Elixir typespecs are later superseded |
| `D-03` | Code contract and automated quality | `EP-Q4` | Staged automation with cheap high-signal checks blocking | Accepted with refinement | No toolchain in Stage 4B; once an app exists, format/warnings/reproducible deps block; noisy style stays advisory until a clean baseline exists |
| `D-04` | Test, review and proof | `EP-Q5` | Risk-proportional test depth plus HIGH proof menu | Accepted with refinement | LOW/STANDARD have small defaults; HIGH authors justify applicable proofs; property and concurrency tests only where they attack a real failure mode |
| `D-05` | Test, review and proof | `EP-Q5` | CI as evidence, review expertise by tag, expensive proof JIT | Accepted with refinement | CI is not business authority; HIGH review matches consequence tags; load/game-day/restore/pen-test stay stage-specific |
| `D-07` | Code contract and automated quality | `EP-Q4` | Automate repeatable no-bypass rules; no universal Architecture checker | Accepted with refinement | Existing Architecture/Domain Law remain authority; later cheap checks may prove Repo/dependency/UI-bypass rules; escape hatches stay review-governed |

## Deferred and rejected Stage 3B items remain closed

A Stage 4B preference is not evidence sufficient to reopen a deferred or rejected Stage 3B item.

Deferred until named evidence exists:

- `A-06` participant/support occurrence ID on every surface
- `A-09` RFC 9457 as a universal API representation
- `C-03` native execution seam
- `C-04` native safety checklist
- `C-07` Rustler selection for an actual workload now

Rejected for the current programme:

- `A-10` giant global error-code registry
- `B-08` three-plane rename, Observability Domain or second telemetry authority store
- `B-10` mandatory OpenTelemetry/vendor/backend
- `C-06` Rustler/NIF platform standard or Rust toolchain baseline
- `C-08` NIF/dirty scheduler as generic durable async or blocking-I/O substitute
- `D-08` maximum ceremony for every change
- `D-09` manufactured CI stages, coverage thresholds or tool adoption

## Downstream tool and package choices explicitly deferred

None of the following is selected, installed or configured by Stage 4B:

- Ash/Splode/Gettext package versions
- `:telemetry` exporter, OpenTelemetry API/SDK, collector, APM or log shipper
- dashboard product
- Credo, Dialyzer, `mix xref`, Hex `boundary`, mix audit tools
- StreamData, Sobelow, coverage reporters
- exact formatter/warning flags
- HTTP error envelopes, Oban backoff numbers, sampling rates, retention periods

Exact strings, worker mapping tables, event grammar and CI job lists belong to later Engineering Standards or JIT work after Architecture amendment.

## Likely later Engineering Standard sections

Engineering Standards remain downstream. If later authorised, they will likely encode:

1. Risk-class declaration mechanics and examples, without a scoring system.
2. Ash/Splode mapping, Gettext public-copy, redaction and retry/terminal/unknown conventions.
3. Telemetry naming, context, ownership, alert/dashboard and minimisation conventions.
4. Documentation/typespec expectations and staged automated-quality failure policy.
5. Architecture-boundary check catalogue for repeatable no-bypass rules.
6. HIGH proof-menu recording, review-expertise routing, and CI versus JIT split.

No Engineering Standard is created here.

## Architecture and Domain result

- Architecture changes: **0**
- Domain changes: **0**
- Independent Stage 3B Architecture Grill propositions reintroduced: **0**
- Architecture amendment begun: **no**
- Engineering Standards created: **none**
- Packages/dependencies/config/CI standards installed: **none**
- Governed identifiers created: **none**
- Implementation authorised: **no**

Current Architecture invariants remain constraints, not restated as new Engineering-Policy law: application actions stay the authoritative operation boundary; delivery layers stay thin; provider/queue/transport state is not business authority; internal diagnostics remain distinct from safe public output; Audit, operational telemetry, Analytics and business truth remain distinct; telemetry remains bounded/non-blocking/failure-isolated; durable business truth retains one owner; cross-domain writes enter the owning boundary; business correctness does not depend on dashboards, CI, logs or static-analysis tools.

## Current ecosystem primary sources consulted

Access date for all sources below: 2026-09-04. HexDocs links refer to the stable release documentation available at access time. No prerelease or `main` documentation was used as policy input. No package version or dependency constraint is adopted by this artifact.

| Source | Status at access time | Use |
|---|---|---|
| [Ash 3.32.3 error handling](https://hexdocs.pm/ash/3.32.3/error-handling.html) | Stable HexDocs | Four Splode classes; custom `Splode.Error`; translation `vars`; `error_handler` reshapes rather than recovers |
| [Splode 0.3.2](https://hexdocs.pm/splode/0.3.2/Splode.html) | Stable HexDocs | Class aggregator already used by Ash |
| [Telemetry 1.4.2](https://hexdocs.pm/telemetry/1.4.2/telemetry.html) | Stable HexDocs | Event names, measurements versus metadata, spans, handler-failure isolation |
| [OpenTelemetry Erlang](https://opentelemetry.io/docs/languages/erlang/) | Official; traces stable, metrics/logs development | Interoperability context only; does not select a vendor |
| [Elixir typespecs (1.20.2)](https://hexdocs.pm/elixir/typespecs.html) | Stable HexDocs | Documentation and Dialyzer input; compiler does not enforce; may later yield to set-theoretic signatures |
| [Dialyzer OTP 29.0.6 / 6.0.2](https://www.erlang.org/doc/apps/dialyzer/dialyzer.html) | Current OTP | Success-typing analysis context |
| [Credo 1.7.19](https://hexdocs.pm/credo/1.7.19/overview.html) | Stable HexDocs | Optional static-analysis context |
| [ExUnit](https://hexdocs.pm/ex_unit/ExUnit.html) | Stable HexDocs | Default test runner once an application exists |
| [StreamData 1.4.0](https://hexdocs.pm/stream_data/1.4.0/StreamData.html) | Stable HexDocs | Property-testing context where a generator attacks an invariant |
| [mix format](https://hexdocs.pm/mix/Mix.Tasks.Format.html) | Mix 1.19/1.20 stable | Built-in formatter as a cheap blocking-check candidate later |

These sources inform the accepted conventions. They do not override live repository authority and do not authorise dependency installation.

## Programme routing after Stage 4B

```text
Stage 4A Architecture Grill: COMPLETE
Engineering-Policy Grill: COMPLETE
Architecture amendment: NOT_STARTED / NEXT
Engineering Standards: DOWNSTREAM / NOT CURRENT
Domain/Roadmap/Atlas/HARDEN-02/FP-001 reconciliation: DOWNSTREAM / NOT CURRENT
Executable development: BLOCKED
```

Engineering-Policy Grill completion does not authorise writing Engineering Standards immediately. Programme sequencing requires the Architecture amendment/closure stage first.

## Mandatory STOP

After the Stage 4B PR opens, work must **STOP** pending independent review of the exact PR head.

Do not merge this PR, start Architecture amendment, create ARC identifiers, write Engineering Standards, modify CI/tooling, install dependencies, amend Architecture Law, modify `03_ARCHITECTURE`, amend Domain Map or Roadmap, reconcile Delivery Atlas, execute HARDEN-02, modify FP-001, or implement any capability.
