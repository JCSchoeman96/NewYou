# Engineering Standards v1.0.0

- **Document version:** v1.0.0
- **Status:** PROMOTION CANDIDATE / NOT CERTIFIED
- **Authority class:** SUPPORTING AUTHORITY / ENGINEERING STANDARDS CANDIDATE
- **Promotion baseline main SHA:** `73eca9d9148a82cab8ae988c5950539bfee0d7f9`
- **Source Grill:** `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md`
- **Source Grill SHA-256:** `27bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017`
- **HARDEN-02 authority basis:** `working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md`, H02-3R and I-12
- **Candidate classification:** reference document for the separately authorised supporting-authority promotion stage

## Boundary

This document is the minimum Engineering Standards content that can be promoted from the accepted Stage 4B Engineering-Policy Grill. It records engineering HOW rules. It does not create Product Law, Architecture Law, Domain Law, Roadmap Law, a Feature Pack, an OQ, a governed identifier or an implementation permission.

The source Grill remains preserved, working and non-authoritative. This candidate does not replace it. The candidate is not certified, and it does not advance `FP001_RECONCILIATION_REQUIRED` or any later stage. Certification requires the separate exact-head and post-merge lifecycle described by the current HARDEN-02 route.

Higher authority wins. A conflict with Product Law, Architecture Law, Domain Law, Roadmap Law, the Platform Operating Model or an approved Feature Pack is a STOP condition. This document must not restate or mutate those authorities as Engineering Standards.

## Promotion provenance

The promoted material comes only from the accepted policy decisions in the source Grill:

| Standards section | Grill decision | Stage 3B provenance |
|---|---|---|
| Risk classification | `EP-Q1` | shared classification for the accepted policy questions |
| Error handling | `EP-Q2` | `A-08` |
| Operational observability | `EP-Q3` | `B-09` |
| Code contracts and automated quality | `EP-Q4` | `D-02`, `D-03`, `D-07` |
| Tests, review and proof | `EP-Q5` | `D-04`, `D-05` |

The Stage 4A Architecture Grill is a constraint, not Engineering-Policy provenance. No Architecture, Product or Domain rule is copied into this document as a new authority.

## Risk classification

Use three engineering-policy risk levels:

- `LOW`
- `STANDARD`
- `HIGH`

Do not add a `CRITICAL` tier at this scope.

`LOW` covers presentation-only helpers, simple pure utilities and mechanically obvious transformations with no authoritative, sensitive, concurrent, provider or consequential boundary.

`STANDARD` covers ordinary application or domain code where failure is bounded and recoverable and the code does not itself establish high-consequence truth.

Classify a change as `HIGH` when it materially involves one or more of:

- authoritative state transitions;
- authentication or authorisation;
- privacy, consent or sensitive data;
- concurrency or idempotency;
- provider reconciliation;
- durable asynchronous execution or recovery;
- migrations affecting authoritative data; or
- participant-facing consequential calculations.

The HIGH classification is mandatory when a trigger applies. Use consequence tags when relevant: `financial`, `entitlement`, `safety`, `privacy_deletion`, `privileged_security` and `irreversible`. Tags select or strengthen proof obligations. They do not create a risk class, Domain owner, Product classification or Architecture authority.

Authors may propose a classification and tags. A consequential classification must be reviewable, and a developer may not downgrade a HIGH change to avoid proof. If classification is reasonably ambiguous, the reviewer must agree. Do not use an elaborate scoring system.

## Error handling

Use the current Ash/Splode error model. Do not create a parallel NewYou-wide error framework. The authoritative application or action boundary owns business meaning.

- Use built-in Ash/Splode errors when they express the required meaning.
- Create a custom `Splode.Error` only for a stable, meaningful application distinction that the built-in model cannot express. Do not create one for different wording alone.
- Participant-facing messages must be safe and localisable through the approved Gettext path. They must not expose sensitive or internal diagnostics, authorisation policy detail or unsafe existence information.
- Keep richer technical diagnostics internal, access-controlled and redacted as needed.
- Adapters translate provider failures into application-understood semantics. Raw provider payloads and SDK details are not participant contracts or business authority.
- The responsible application or provider boundary classifies retryable, terminal, unresolved or unknown outcomes where that distinction matters. Do not infer retryability only from a Splode class. An ambiguous provider acknowledgement is not success and must not trigger blind duplicate retries.

Apply the risk model proportionally. LOW uses ordinary result or exception handling. STANDARD uses framework-native handling and separates public copy from diagnostics. HIGH adds explicit failure, retry and reconciliation semantics where applicable, plus leakage and non-enumeration proof where privacy or security requires it.

## Operational observability

Use backend-neutral operational observability conventions. Do not mandate OpenTelemetry, a telemetry vendor, an APM backend, a dashboard product, an Observability Domain or a second telemetry authority store.

Preserve the existing Architecture separation between metrics, traces, structured logs, domain-outcome operational signals and Audit/security evidence. Material signals need stable names, a defined measurement or contextual field, bounded cardinality, opaque correlation, minimum necessary context, an owner and a purpose.

Minimise sensitive data before logging or telemetry. Account IDs, participant identifiers, health content and other sensitive or high-cardinality values must not be used casually as metric labels. Correlation identifiers must not become authentication, Account identity or business authority.

A material alert needs an identified owner, a meaningful operator action or decision and a clear reason to exist. Do not manufacture alerts simply because a metric exists. Dashboards are projections for operational understanding, never business authority. When a dashboard disagrees with authoritative state, authoritative state wins and the discrepancy is investigated.

Telemetry and exporter failure may reduce visibility but must not fail an otherwise valid business transaction. Telemetry remains bounded and failure-isolated. For HIGH changes, provide enough evidence where applicable to correlate request, job and provider activity, find unresolved obligations or important outcomes, reconstruct consequential incidents and diagnose provider or reconciliation failures. Risk-sensitive sampling is allowed. Do not require zero sampling globally.

## Code contracts and automated quality

Use risk-proportional contract evidence and staged automation. Do not install an Elixir quality toolchain as part of this promotion. Once an authorised Elixir application baseline exists, cheap, deterministic and high-signal checks should become normal blocking evidence. Noisy or style-oriented findings stay advisory or policy-scoped until a clean baseline and failure policy exist. Automation must enforce repeatable, valuable rules with an acceptable false-positive burden. Human review remains necessary for novel Architecture or Domain boundary reasoning and approved escape hatches.

- LOW needs no documentation for a trivial private helper. Document where understanding benefits.
- STANDARD documents meaningful public or application contracts and externally consumed interfaces.
- HIGH documents the relevant contract and a short rationale for consequential actions, policies, adapters, escape hatches and other material boundaries.
- Do not require comments that only restate code.
- Do not require `@spec` on every Elixir `def`. Require useful typespec or equivalent contract evidence for meaningful public interfaces, behaviours and callbacks, cross-domain or application interfaces, complex HIGH boundaries and dense logic where it improves understanding or analysis. Keep this policy adaptable if Elixir's type-system capabilities supersede current typespec practice.
- Once an application exists, formatting, approved compiler-warning policy and reproducible dependency state are blocking evidence. New unexplained static-analysis regressions block after a clean approved baseline. Noisy style findings do not become automatically fatal without that policy.
- Automate Architecture-boundary rules only when they are repeatable and high-signal. Examples include forbidden ordinary Repo writes around an owning boundary, forbidden dependency direction and delivery code bypassing the application boundary. Existing Architecture and Domain Law remain authority. Approved exceptions require governed review.

This policy does not select Credo, Dialyzer, `mix xref`, Hex `boundary`, an audit package, warning flags or a dependency version.

## Tests, review and proof

Use risk-proportional tests and a justified HIGH proof menu. Do not require universal 100% coverage, property tests everywhere, concurrency tests for non-concurrent code, every expensive proof in permanent CI or security tooling as a maturity badge. CI is evidence, not Product, Architecture or business authority.

- LOW may use minimal testing for mechanically obvious logic. Non-obvious pure logic gets focused examples. Ordinary review is sufficient.
- STANDARD includes positive behaviour plus important rejection and edge cases. Application changes carry enough tests to make their intended contract repeatable.
- Every HIGH change evaluates the applicable proof menu. The author marks each item applicable or not applicable with a meaningful reason, and the reviewer agrees. For HIGH consequence tags such as financial, safety, privacy/deletion, privileged security and material concurrency, a weak or unjustified `N/A` blocks approval.

The proof menu may include positive and negative tests, invariant or state-transition tests, policy or authorisation tests, concurrency or idempotency tests, duplicate/reorder/retry tests, failure/recovery/reconciliation tests, migration-safety evidence, sensitive-data leakage or redaction tests, provider-reconciliation tests, security/privacy review evidence and reviewer acknowledgement of authority boundaries. Apply only the proofs that attack the actual failure modes.

Use property or generative testing when a generator meaningfully attacks an invariant or state space. Require concurrency testing when correctness materially depends on concurrent execution, duplicate requests, ordering or idempotency. Do not require it for code without a concurrency surface.

HIGH changes should receive review appropriate to the applicable consequence tag. Permanent CI contains cheap repeatable checks appropriate to the application. Load testing, game days, restore testing, penetration testing and large-scale concurrency proof remain JIT or stage-specific unless repeated evidence justifies permanent automation. Do not move later Architecture Proof or Release Readiness work into every PR. Coverage is diagnostic; no universal numeric coverage target is authority for correctness.

## Deferred choices and closed alternatives

This candidate does not select or install any package, framework, tool, version, flag, provider or vendor. That includes Ash, Splode, Gettext, Telemetry exporters, OpenTelemetry, APM or log backends, dashboards, Credo, Dialyzer, `mix xref`, Hex `boundary`, audit tools, StreamData, Sobelow, coverage reporters, exact formatter or warning flags, HTTP error envelopes, Oban backoff numbers, sampling rates and retention periods.

The following Grill items remain deferred or rejected at their recorded scope: a universal participant/support occurrence ID, universal RFC 9457, a native execution seam, a native safety checklist, Rustler selection for an actual workload, a global error-code registry, an Observability Domain or second telemetry store, mandatory OpenTelemetry or vendor choice, a Rust/NIF platform standard, NIFs as a generic async or blocking-I/O substitute, maximum ceremony for every change and manufactured CI stages or coverage thresholds.

Exact strings, worker mapping tables, event grammar, CI job lists and implementation-grade package/API choices require later authorised JIT work. Current stable ecosystem facts must be rechecked against primary sources before any such choice is frozen.

## Candidate lifecycle and preserved downstream state

The candidate is registered as a reference supporting-authority candidate. It is not a governing-root document and is not certified. The source Grill remains at its working path and its bytes are preserved.

The current route remains:

```text
CERTIFIED HARDEN-02 EXECUTION
→ ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED
→ CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION
→ FP001_RECONCILIATION_REQUIRED
→ COMMUNICATIONS JIT DOMAIN DOSSIER
→ REMAINING REQUIRED / CONDITIONAL PHASE 7B
→ PHASE 7C
→ PROOF CLASSIFICATION
→ PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES
```

This candidate does not mark Standards certified. It does not perform FP-001 reconciliation, start Communications, resolve conditional dossiers, unblock Phase 7C, finalise proof classification, authorise implementation or add Store/CER to HARDEN-02.

## Primary-source verification note

On 2026-10-01, the candidate preparation checked the official HexDocs and Hex.pm entries for the ecosystem references named by the Grill. Those checks confirmed current stable documentation and releases, but this document adopts no version or dependency constraint. The Grill's original source table remains historical provenance for the accepted policy decisions.

No package, framework, tool, version, flag, provider or vendor is selected by this candidate.
