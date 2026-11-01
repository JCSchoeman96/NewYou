# P8-04 deterministic Phase-8 proof harness specification

- Version: v0.1.0.
- Status: CANDIDATE / INDEPENDENT CHATGPT PLANNING REVIEW REQUIRED.
- Implementation owner: WELL-5 / FP-001 P8-04, under WELL-1 and TB-001.
- Canonical baseline: live GitHub `main@5a6e574cd8bb2aabb99845247c57c8bb1862e3e8`, fetched and rechecked on 2026-10-22.
- Authority class: derived implementation specification. This document changes no governing law or frozen TB-001 design.
- Planning method: evidence-led Grill-Me, Q1–Q10 accepted by the user, followed by `to-spec` synthesis.
- Execution status: no P8-04 application or proof code has been implemented in this planning change.

## Problem statement

Later TB-001 slices need repeatable ways to interrupt execution, compete through real PostgreSQL transactions, simulate provider observations, and produce trustworthy machine-readable results. Without shared proof infrastructure, each slice would invent controls that could mask failures, claim sequential execution was concurrent, or confuse simulated observations with business authority.

WELL-5 is the next authorised execution unit. Current Open Work §12.35 records its prerequisites as complete and bounded Phase 8 execution as started. Proof result and certification remain unstarted. Phase 9 remains unauthorised. P8-04 must be executable before the later owning business actions exist, without implementing substitute business actions or claiming those actions have passed proof.

## Solution

Build test-only proof infrastructure using the existing NewYou application, Repo, Elixir/ExUnit, Ecto connection ownership and PostgreSQL. Use one explicit scenario handle for failure controls, barriers and provider scripts. Keep proof reporting outside the application supervision tree so a scenario can restart the relevant application processes without restoring business truth from test-process memory.

Provide a distinct infrastructure self-test mode. The complete TB-001 mode enumerates the frozen nine proof families and required browser spine, and fails closed while any required coverage is missing, unrun or failing. Infrastructure self-test success means the machinery passed its own contract. It never means TB-001 architectural PASS or certification.

No new dependency, business Resource, database table, Repo, service, ETS table, Redis use or GenServer is required. One short-lived scenario controller and monitored competing workers are justified by one-shot consumption and genuine concurrency. They own test instructions only.

## User stories

1. As a later TB-001 slice author, I want one reusable proof interface so I can test the owning production path without building competing machinery.
2. As a proof author, I want named one-shot cut-points so I can reproduce a precise failure boundary.
3. As a proof author, I want failures targeted to a particular worker so competing workers cannot consume each other's instructions.
4. As a reviewer, I want an expected but unreached cut-point to fail so a disconnected hook cannot produce PASS.
5. As an operator, I want proof controls absent from production so runtime configuration cannot enable injected failures.
6. As a concurrency-proof author, I want separate PostgreSQL transactions so the test exercises genuine competition.
7. As a reviewer, I want observed database contention so two tasks that ran sequentially cannot masquerade as a race.
8. As a proof author, I want bounded synchronization and cleanup so a crashed worker cannot leave a hanging run or pooled lock.
9. As a Communications slice author, I want scripted provider observations so I can test success, rejection, uncertainty and backlog deterministically.
10. As a Communications reviewer, I want no-invocation distinguished from rejection so local admission facts cannot become fabricated provider evidence.
11. As a reconciliation-proof author, I want authenticated, unauthenticated and mismatched fixtures so proof exercises the real verification boundary.
12. As a proof author, I want duplicate and reordered observations with stable identities so I can test idempotency and non-regression.
13. As a restart-proof author, I want the runner independent of restarted application processes so it can observe recovery without supplying business truth.
14. As an Identity reviewer, I want reconstruction through current owning interfaces so stale browser or process state cannot restore authority.
15. As an Audit reviewer, I want proof reporting separated from Audit evidence so test artifacts cannot materialise business assertions.
16. As a CI reviewer, I want exact source and dependency metadata so I can identify the executed build.
17. As a certifying reviewer, I want every mandatory family represented so missing proof cannot disappear from the report.
18. As a CI consumer, I want a non-zero exit on invariant, infrastructure or output failure so automation cannot treat a false PASS as success.
19. As a maintainer, I want deliberately broken fixtures to test the runner so exception swallowing and empty coverage cannot silently pass.
20. As a privacy reviewer, I want bounded redacted observations so proof artifacts contain no credentials, bearer material or unnecessary participant data.
21. As an implementation reviewer, I want executable acceptance criteria and explicit exclusions so P8-04 stays separate from later Domain implementation.

## Implementation decisions

### Authority and scope

Apply Product Law, Architecture Law, Domain Law, Roadmap, supporting contracts, current Open Work, approved FP-001 contracts, TB-001, proof evidence and implementation in that order. Refresh live authority before implementation. Plane tracks delivery and does not override GitHub authority.

P8-04 delivers the controller, registry, concurrency helper, deterministic provider scripts, result model, runner, self-tests and dedicated manually invoked proof workflow. Concrete business hook insertion, business scenario implementation and durable Domain reconstruction belong to the later owning slices. No minimum business seam is needed to make these infrastructure self-tests executable.

### Framework and mechanism evaluation

- Ash actions and code interfaces remain the business mutation boundary. Later scenarios invoke the owning interface with normal authorization. Pure proof orchestration uses ordinary Elixir under Architecture §4.3; creating an Ash Resource for a failure instruction or result would invent an unnecessary lifecycle.
- AshPostgres remains the existing business data layer. Later business scenarios exercise its real transaction and constraint behavior. P8-04 does not add a fixture Resource or schema to pretend those scenarios exist.
- Ecto SQL Sandbox ownership and the existing Repo provide independent test connections. Direct Repo transaction control, diagnostic SQL and transaction-level advisory locks are a bounded infrastructure-only use. They never write business records or wrap a later owning action in a replacement transaction.
- PostgreSQL is required. The infrastructure contention self-test uses transaction-level advisory locks, distinct backend identities and observed blocking. These locks are not a proposed business locking strategy.
- Ash Signals are evaluated and require no P8-04 implementation. TB-001 permits narrow coordination with receiving-owner interfaces. Inline delivery can participate in an emitting action's transaction, but a signal or notifier alone does not prove durable scheduling, E1/E2 or business success. No generic signal bus or proof controller built from Signals is introduced.
- Temporal Resources are evaluated and excluded. TB-001 preserves history in the lifecycle/evidence model and requires a capability-specific need before introducing temporal storage. Restart testing is not such a requirement. The pinned Ash guide labels temporal resources experimental.
- Ash Storage is evaluated and excluded. File/attachment management is unrelated to writing a local CI result artifact. No object storage, blob or attachment Resource is needed.
- Ash State Machine remains the frozen later Communications choice for MessageIntent dispatch disposition. It is not needed for runner status or one-shot instruction consumption. Account and DeliveryAttempt orthogonal dimensions remain outside that machine as required by TB-001 §5.
- Oban and AshOban remain required for the later real durable-execution path. They are absent from the baseline lockfile and are not installed for a simulated scheduling self-test. P8-04 provides named scheduling cuts and integration obligations; it does not claim durable enqueue or restart proof before the owning integration exists.
- AshAuthentication, AshAuthenticationPhoenix and AshCloak belong to later Identity proof. Reactor orchestration, Temporal Resources and extra extensions are not added for generic test plumbing. Existing transitive dependencies confer no new design requirement.
- No ETS, persistent-term controls, Redis, GenServer, production process, extra Repo, service, distributed lock manager or global application-environment mutation is justified. Tidewave remains DEV-only diagnostic tooling. Direct Sourceror remains deferred.

### Interfaces and ownership

These are proposed NewYou interfaces, not claims about third-party APIs:

- `NewYou.Proof.Scenario.start/1` returns a run-scoped handle containing a controller PID and unguessable reference. `stop/1` waits for cleanup and returns its verdict. A handle is never serialized into a business record or job argument.
- `NewYou.Proof.CutPoints.arm/4` takes the handle, registered name, worker label and failure mode. `hit/3` takes the handle, name and worker label. Only a matching worker consumes that instruction. `verify_consumed/1` rejects any expected instruction left unused.
- `NewYou.Proof.Barrier.arrive/3` and `release/3` coordinate named phases for an explicit participant set. Messages include the scenario reference. Unknown participants, duplicate arrival, missing acknowledgement and deadline expiry fail the scenario.
- `NewYou.Proof.Concurrent.run/3` takes the scenario handle, worker callbacks and finite options. It returns bounded connection, transaction, synchronization and outcome observations. It does not interpret a Domain winner.
- `NewYou.Proof.Provider.next/3` takes the handle, safe operation reference and script step. It returns the scripted external observation or ingress fixture. It cannot admit attempts, decide retry eligibility or mutate Domain state.
- `NewYou.Proof.Catalog.required/0` returns the fixed TB-001 coverage inventory, the required infrastructure check inventory and the compiled case manifests. Scenario registration names a family, case and invariant and provides a callback. Duplicates and unknown coverage/case identifiers fail registration. Registration cannot edit the required inventory or supply a replacement manifest.
- `NewYou.Proof.Result.expect!/5` takes the scenario handle, case ID, required check ID, observed value and expected value. It records a runner-owned assertion and raises on mismatch. Callbacks cannot supply their own assertion count or PASS. Actual observations still require source and code review; a test utility cannot prove that a malicious test author supplied truthful inputs.
- `NewYou.Proof.Runner.run/1` selects the full or infrastructure mode, executes the applicable catalog, checks semantic completeness, writes evidence and returns a verdict/exit-code pair. The CLI alone terminates the OS process. Controller and provider modules do not swallow runner failures.

Callbacks return bounded observations, never a trusted caller-supplied PASS. Assertions and scenario completion determine the verdict. The runner treats any callback exception, exit, throw, malformed return or absent expected observation as failure.

### Proof-only boundary

All control, simulator and runner modules compile through the existing test-only support path. The CLI checks the compiled environment before starting application work. A production or DEV build cannot enable these modules by setting an environment variable, request parameter or application flag. P8-04 adds no production hook module.

Later owning slices use the same production actions and boundaries while placing a compile-time-eliminated test hook at the exact required phase. They must prove that their production artifact has no callable proof branch or simulator selection. A live request cannot supply or reconstruct a scenario handle. Test-only compilation alone does not excuse an unsafe production adapter selector.

Self-tests inspect production-build module absence and rejection of attempted runtime enabling. Build artifacts and inherited environment must be isolated so an existing test BEAM cannot make that check pass falsely.

### Failure seam model

The fixed initial cut-point names are:

- `transaction.before_commit`
- `transaction.after_commit`
- `scheduling.before_enqueue`
- `scheduling.after_enqueue`
- `provider.before_invoke`
- `provider.after_invoke_before_persist`
- `evidence.before_materialize`
- `evidence.after_materialize_before_commit`

Each instruction selects one scenario, worker and cut-point, and either raises a tagged proof failure or terminates that worker. A hit without an armed matching instruction proceeds normally. An unknown cut-point or duplicate arming fails immediately. A consumed instruction cannot be rearmed in the same scenario. Repeated invocation after consumption does not fail again.

The controller serialises concurrent hits and records consumption before replying. For termination mode, it monitors the worker and confirms termination. For raise mode, it returns a tagged response that the hit function raises in the caller. A lost controller response invalidates the scenario rather than guessing whether the cut fired. Control state is local to this run and never durable business truth.

Later integration must document the exact hook binding. In particular, after-enqueue can still be inside the authoritative acceptance transaction; after-commit must actually follow commit. The provider-after-invoke cut is distinct from a conclusively rejected provider response. Evidence-after-materialize is before the transaction committing that evidence. A hook that changes an Ash action's atomicity or policy behavior is not acceptable merely to inject a failure. Stop if the required phase cannot be reached without weakening semantics.

Infrastructure self-tests exercise all names through bounded fixture callbacks. They are labelled infrastructure fixtures, not real durable scheduling or Audit materialisation proof.

### Genuine PostgreSQL concurrency

Use the existing Repo in manual Sandbox mode, in a dedicated non-async proof execution. Each competing process explicitly checks out its own connection with the Sandbox wrapper disabled. Shared owners, allowances and caller-inherited ownership are not substitutes for independent connections. Check distinct backend PIDs and transactions before releasing the race. Refuse a connection that is already owned or allowed elsewhere.

Infrastructure self-test sequence:

1. A checks out its connection, begins a real transaction and takes a transaction-level advisory lock on a run-scoped key. It reports its backend PID and transaction identity and waits at a barrier.
2. B independently checks out a connection, begins a transaction, reports a distinct backend PID/transaction identity and requests the same lock.
3. An independently owned observer connection polls within a finite deadline until PostgreSQL reports A blocking B. Polling observes database state; no sleep is accepted as proof of contention.
4. The coordinator releases A. A commits. B acquires the lock and commits. Record acquisition order, both transaction outcomes and absence of remaining run-owned locks.
5. Negative self-tests deliberately share a connection or remove overlap. The helper must reject them rather than report genuine competition.

The test needs three existing pool connections, not three Repos or databases. Reserve enough capacity before starting workers and fail clearly on pool exhaustion. Transaction-local statement/lock timeouts must not leak into the pool. Use transaction-scoped locks only, never session locks. Derive a bounded lock key from a run reference and reject unexpected contention from another run.

Later business races supply callbacks that call the owning Ash interface. Do not impose an outer Repo transaction or advisory lock on those actions. Their own action/constraint boundary chooses the winner. Barriers and hooks position the race, and fresh post-commit owner reads establish the winning and rejected outcomes. Each later slice owns its lawful fixture setup and cleanup. P8-04 adds no generic delete or raw business-table cleanup API.

### Provider outcome model

Scripts distinguish local no-invocation, external observations and reconciliation evidence. The following test vocabulary maps to the existing Communications concepts; it creates no new business states:

- `not_invoked`: the selected external call did not begin. It is not provider rejection. Later Communications may conclude closed-before-invocation only from sufficient proof through its own action.
- `rejected_before_submission`: a real request received a conclusive provider rejection before acceptance.
- `accepted`: provider acceptance with delivery unresolved. Acceptance does not permit blind retry or establish delivery.
- `delivered` and `bounced_or_failed`: conclusive scripted delivery observations for the identified operation.
- `unknown`: possibly submitted with unresolved outcome. Never collapse it into failure, no-operation or success.
- `backlog`: execution remains intentionally unreleased before invocation. A backlog script cannot manufacture an external observation or an attempt admission.
- Duplicate/reordered observations: a script supplies stable event and operation references plus explicit logical ordering. Preserve original evidence identity and generate repeated or permuted delivery deterministically, without wall-clock races.
- Reconciliation: fixtures describe authenticated conclusions such as confirmed no operation, rejection, acceptance, delivery or failure. Supply known test authentication material, invalid signatures and mismatched operation references. The real future ingress verifier must authenticate them; a trusted boolean cannot bypass it.

Scripts return only the requested external behavior. Communications decides observation persistence, conflicts, admission, reconciliation and retry through its own interfaces. The simulator has no production transport, live credentials or outbound network access. Unknown scripts, exhausted scripts and unmatched operation references fail explicitly. An explicit queued event is not a claimed durable backlog recovery result until real Oban integration is tested.

### Restart and reconnect

Runner and scenario controller remain outside the restarted NewYou application supervision tree. The controller retains consumed instructions for the lifetime of the scenario. A restarted worker receives its handle explicitly and cannot automatically rearm a consumed cut.

P8-04 demonstrates worker termination/replacement, controller isolation, dropped uncommitted PostgreSQL transactions, lock release and fresh connection ownership. These observations prove infrastructure behavior only.

Later slices terminate and restart their actual application/executor boundary, then reconstruct through fresh owning interfaces from PostgreSQL and durable executor state. They assert fresh process/connection identities and discard old business structs, browser state and caches. A callback that rehydrates business truth from the controller is forbidden. Fake restart flags, worker replacement alone and replaying the source mutation do not satisfy durable reconstruction proof.

A whole runner/BEAM crash loses instructions and invalidates the run. A new run gets a new identity and never resumes a prior PASS. No persistent failure-control state or automatic proof retry is introduced. Full BEAM replacement of the application is not claimed by P8-04; any later claim must name and terminate the actual tested boundary.

### Evidence runner and completeness

The result schema is version `1.0.0`, defined by the companion JSON Schema. It is a candidate wire contract until this planning package is approved. Schema-valid JSON alone cannot establish PASS; the runner also enforces the semantic rules below.

Modes are `harness_self_test`, `tb001` and `diagnostic`. Only `tb001` is eligible to report full architectural PASS. Diagnostic selection cannot acquire that eligibility by changing an output filename or mode label.

The fixed full inventory is `registration_pmr_reconciliation`, `proof_capability_scanner_replay_supersession`, `session_login_revocation_restart`, `communications_durability_backlog_ambiguity`, `audit_e2`, `audit_e1`, `recovery_primary_email_change`, `non_enumeration_current_privacy`, and `source_authority_bypass_negatives`, plus `browser_spine`.

Each full entry requires a compiled, reviewed case manifest covering every corresponding TB-001 §8 obligation. The browser spine manifest covers registration, PMR, explicit verification, credential login and Session reconstruction in §7. Each manifest fixes its source section, case/invariant IDs, required assertion IDs, version and digest. Cases cannot declare their own completeness. The runner compares registrations and observed assertions against that manifest, rejecting a missing case even when another case in the same family passes.

P8-04 deliberately supplies no approved business case manifest. A missing manifest produces `missing` and FAIL, even if an arbitrary passing callback registers under that family. Later owning slices introduce the complete case-to-obligation mapping through their independently reviewed ticket/PR. A partial mapping remains unavailable to full PASS. This spec defines no business action or schema to manufacture a complete mapping. Manifest completeness is a human review obligation against the frozen contract; the runner enforces the approved list once present and never treats registrations as that list.

The self-test manifest is fixed in P8-04. It expands `cut.raise.<name>` and `cut.terminate.<name>` for all eight registered names and also requires `cut.consume_once`, `cut.wrong_worker`, `cut.unknown_name`, `cut.duplicate_arm`, `cut.unreached`, `scenario.isolation`, `scenario.controller_death`, `scenario.lost_reply`, `scenario.parent_crash`, `db.contention`, `db.reject_shared`, `db.reject_sequential`, `db.timeout_cleanup`, `db.worker_crash_cleanup`, `provider.outcomes`, `provider.backlog`, `provider.duplicates_reorder`, `provider.authentication_fixtures`, `restart.consumption`, `restart.fresh_connection`, `result.missing_manifest`, `result.missing_family`, `result.missing_case`, `result.missing_assertion`, `result.empty_self_test`, `result.metadata`, `result.dirty_source`, `result.changed_source`, `result.callback_failures`, `result.broken_invariant_exit`, `result.output_failure`, `result.cleanup_failure`, `production.exclusion`, and `privacy.redaction`. Every manifest case has at least one explicit required assertion ID. Removing any required self-test registration or assertion fails self-test mode. A known-failure fixture must observe its precise expected failure before its outer self-test can pass.

Stop executing further business scenarios at the first invariant failure, as TB-001 §10 requires. Emit entries for remaining cases/families with `not_run` and FAIL. Missing registrations produce `missing` and FAIL. Both the failed invariant/cut-point and the skipped remainder remain visible. There is no weighted score, silent skip, automatic rerun or “partial PASS”.

Capture Git SHA with Git from the actual execution checkout, not a supplied environment string or the planning baseline. Capture tracked and untracked cleanliness before and after execution, excluding ignored build/output artifacts. Verify SHA and lock digest remain unchanged during execution. Read resolved versions from the lockfile and loaded application/runtime metadata, recording source-only dependencies separately. Read PostgreSQL server version from the actual TEST connection. Reject absent or conflicting required metadata.

Dependency metadata must contain exactly one entry for every package key in the executing lockfile, with no missing or duplicate entries. Hex entries record the resolved lock version. Git entries record their exact commit. Loaded runtime applications also record their actual version and must match the selected locked build; Git applications record both their loaded version and source commit. Non-application/source-only dependencies record `runtime_required=false` and null loaded version rather than a fabricated application version. Required runtime applications that are not loaded make metadata incomplete. A lock source without a reproducible identity fails metadata capture. A path dependency without a tracked, content-addressed identity cannot qualify for full proof. Record every lock entry even if its package is not active in TEST; classify it explicitly as source-only or inactive rather than omit it.

The runner uses Elixir/OTP runtime introspection and existing Jason for encoding. Do not shell out to print environment variables, dependency configuration or connection URLs. Full proof refuses a dirty checkout. Self-test/diagnostic runs report cleanliness accurately and cannot be used as full-proof evidence.

Write one bounded result to a new run-specific temporary file next to the requested artifact, then atomically publish the completed result. Never reuse a previous PASS artifact after failure. Reject an existing target rather than overwrite another run. Prefer an ignored directory or a path outside the checkout so output does not dirty source. Validate verdict, exit code and cleanup consistency before publication.

Exit codes are 0 for complete success within the selected mode, 1 for an invariant/coverage failure, and 2 for preflight, metadata, controller, timeout, cleanup, schema or output failure. Any non-zero invalidates full proof. If output cannot be written, emit a bounded redacted diagnostic to stderr and exit 2. Total OS failure can prevent an artifact; absence of a completed artifact is never PASS. A result artifact is proof evidence, not an Audit EvidenceRecord or a business authority.

### Timeout and cleanup behavior

Defaults are 5 seconds for a barrier, 15 seconds for a database statement, 30 seconds for an ordinary scenario and 120 seconds for a restart scenario. Overrides must be positive, finite and recorded with a reason. A scenario's overall deadline bounds its retries/polling; these limits are test mechanics, not launch policy or RPO/RTO targets.

Every exit path stops scenario workers, waits for monitored DOWN messages, rolls back any still-open owned transactions, releases/checks in owned connections and stops its controller. Cleanup gets a separate finite deadline of 5 seconds. If a worker is stuck, terminate that test-owned process and let its connection ownership unwind. Never stop PostgreSQL or terminate unrelated sessions. Verify the observer sees no remaining run-owned locks before returning success. An unconfirmed release or cleanup timeout yields FAIL and exit 2.

An ExUnit test owns its children and cleanup callbacks. The standalone runner applies the same rules in a `try/after` lifecycle and monitors its parent/worker relationships so an unexpected caller exit cannot orphan control workers. No reliance on process-memory instruction state is allowed for business crash recovery.

### Security and privacy

Use synthetic inputs only. Artifacts include safe scenario/event/operation labels and bounded diagnostic codes, not emails, Account data, password hashes, bearer tokens, signing secrets, raw SQL parameters, rendered messages or raw provider payloads. Record authentication result categories rather than fixture secret values. Redact exception diagnostics before serialization; do not dump changesets, connection config or process state.

The test runner obtains credentials through DevCore. It verifies TEST profile/database/role and refuses DEV/production configuration. No credentials enter arguments, artifact metadata or chat. Local environment activation never lifecycle-manages shared services. Test-generated authentication material is isolated from production keys. Proof output remains a restricted CI artifact with repository/platform access controls; this ticket defines no new legal retention period.

## Testing decisions

Tests attack externally observable failures. A controller map matching its implementation is insufficient; demonstrate one failure under competing hits and none leaking to a second scenario. Use current ExUnit support as prior art, while explicitly avoiding shared DataCase ownership for concurrency proofs.

Required tests:

1. Every registered cut-point works in raise and terminate modes. Concurrent hits consume once; the wrong worker does not consume; unknown names, duplicate arming and unreached expected cuts fail.
2. Scenario isolation, controller death, lost replies and caller/test crashes fail visibly and leave no live owned processes. No global state mutation is necessary.
3. Real PostgreSQL contention records different PIDs/transactions and observed blocking. Shared-connection and sequential fixtures fail. Timeout, rollback and worker death release connections and transaction locks.
4. Every provider observation, backlog release, duplicate/reordered script and valid/invalid/mismatched authentication fixture has deterministic behavior. Assert unknown remains unresolved and that the simulator has no Domain write API or production transport.
5. A consumed instruction remains consumed across worker replacement. Reconnection uses fresh ownership. Explicitly label this infrastructure test and refuse to count it as application durable-recovery proof.
6. Evidence validates against the companion schema and semantic completeness rules. Missing/empty/duplicate family, missing manifest/case/assertion, missing browser spine, missing/duplicate dependency metadata, dirty full proof, changed SHA/lock, malformed callback and invalid output destination fail. Removing one case from a nonempty family and removing one infrastructure self-test are separate negative tests.
7. Subprocess tests deliberately break an invariant and assert FAIL, family/case/invariant/cut identification and non-zero OS exit. Also test exception, exit, throw, timeout and cleanup/output failures. A fixture expected to fail passes its outer self-test only after observing the precise expected failure; never invert arbitrary failures into success.
8. Independent production-build checks prove proof modules absent and attempted runtime enabling ineffective. Check isolated build artifacts, not only a runtime flag.
9. Artifacts and stderr do not disclose synthetic canary secrets placed in rejected inputs or exception payloads.
10. Full mode at P8-04 completion exits non-zero and lists unavailable business families/browser coverage. Self-test mode passes only its complete infrastructure catalog. This expected full-mode failure is an acceptance assertion, not a requirement to implement later slices.

Use `mix check` for every implementation handoff and `mix check.deep` because implementation changes Elixir code. Keep full TB proof separate from routine checks. Run cheap harness regression tests in the normal suite; use a dedicated manual proof workflow for the full command and bounded infrastructure contention/restart probes. No Foundation gate is weakened, and no wait for non-blocking Foundation Full is required.

## Out of scope

No Identity, registration, authentication, PMR, Communications, Audit, recovery, primary-email-change, support, consent or Content implementation. No production business Resource, lifecycle, migration or table. No production provider/vendor selection, retry/backoff policy, OQ-035/OQ-036 resolution, release gate closure, Phase-8 proof certification or Phase-9 authorisation.

No new package or infrastructure, no direct Sourceror, no Temporal Resources, Ash Storage, generic event bus, process/cache authority, Redis, ETS table, GenServer, extra Repo, service or database. No test controller stored in durable business state. No replacement transaction or raw business write path. No business-proof claim from advisory locks or stub callbacks.

## Further notes

### Exact authority references

All paths below are relative to the repository root and were resolved at the canonical baseline. Manifest/current routing takes precedence over freeze-time lifecycle paragraphs in derived contracts.

- `docs/00_platform/README.md` and `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`, including the current Open Work route.
- `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` §§23–24, bounded executable entry.
- `docs/00_platform/00_PLATFORM_v1.8.0.md` §§21J and 21K.3/21K.7, Identity/security truth and concurrency/performance obligations.
- `docs/00_platform/01_DECISIONS_v1.8.0.md`, OQ-034 selection and OQ-035/OQ-036 unresolved boundaries; DEC-267 operational behavior.
- `docs/00_platform/03_ARCHITECTURE_v1.1.1.md` §§3–5, 7–8 and 15, authority, controlled infrastructure use, durability and engineering constraints. ARC-029 is enforced by the existing architecture checker.
- `docs/00_platform/04_DOMAIN_MAP_v1.2.0.md` §§6.1, 6.15, 6.18 and 8.1, sole Domain ownership.
- `docs/00_platform/05_ROADMAP_v1.2.3.md` Phase 8, §§15 and 17, proof sequencing and JIT mechanism detail.
- `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md` §§2–3, 8 and 25–26, projections, operating/implementation boundaries. Frontend Experience System is not applicable to this non-UI infrastructure unit; the later real browser spine retains its own experience obligations.
- `docs/00_platform/02_OPEN_WORK_v1.2.79.md` §§9 and 12.35, P8-04 NEXT and current execution authority.
- `docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md`, risk classification, error boundary, tests/review/proof and deferred choices. Treat implementation as HIGH for material concurrency and security/privacy proof correctness; reviewer must agree on applicable proof coverage.
- `docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md` §§G–M, P and W.
- `docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md` §§1, 3, 5–10, accepted implementation foundation and frozen nine-family proof obligations.
- `docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md` §§J, O, Q, R–V, sole Identity authority, concurrency and security.
- `docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` §§3, 6, 9, 11–14 and 19, invocation admission, ambiguity, authentication and proof.
- `docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` §§2, 6–8 and 14–15, E1/E2, evidence identity and source authority.
- Root `AGENTS.md`, the packaged `$ticket-implement` skill, `.agents/skills/code-change-verification/SKILL.md`, and `docs/development/foundation-integrity-merge-gate.md`.

No unresolved authority contradiction or unclear business owner was found. Frozen contracts' earlier NOT STARTED lifecycle snapshots do not override current Open Work §12.35. They are not silently rewritten here.

### Accepted Grill-Me record

- Q1 challenged harness scope before concrete business actions exist. Accepted infrastructure fixtures and later owner integration, with no substitute business implementation.
- Q2 challenged false architectural PASS. Accepted distinct self-tests and full fail-closed TB-001 coverage. Complete-family proof is already required by TB-001, not an optional relaxation.
- Q3 challenged production enabling. Accepted test-build-only machinery and no runtime switch.
- Q4 challenged shared one-shot consumption. Accepted one explicitly passed, monitored, short-lived test controller and no global mutable controls.
- Q5 challenged simulated concurrency. Accepted independent PostgreSQL transactions, observed contention and fixture-free advisory locks for infrastructure self-tests only.
- Q6 challenged provider authority and authentication bypass. Accepted deterministic observation scripts and real future authentication verification.
- Q7 challenged unbound and unreached seams. Accepted the fixed registry, targeted raise/termination and mandatory consumption checks.
- Q8 challenged restart scope and process-memory truth. Accepted controller survival outside restarted application processes, lost controls on whole-run crash and later PostgreSQL reconstruction through owners.
- Q9 challenged evidence completeness and provenance. Accepted a versioned result schema, exact metadata, every family visible and non-zero failures.
- Q10 challenged hangs, leaks and reruns concealing failure. Accepted bounded deadlines, owned cleanup and first-failure preservation.

The user's last acceptance settled Q7–Q10; the subsequent instruction invoked `to-spec` for synthesis. No further design choice is silently delegated to a package or later schema. User-specific output requirements override `to-spec` defaults that omit paths or immediately mark work ready.

### Expected file and module boundaries

This planning PR contains this specification and `docs/superpowers/specs/p8-04-proof-result-v1.schema.json` only. It does not amend governed authority, the manifest or frozen TB-001.

The future WELL-5 implementation is bounded to:

- `test/support/proof/scenario.ex`, `cut_points.ex`, `barrier.ex`, `concurrent.ex`, `provider.ex`, `catalog.ex`, `result.ex` and `runner.ex`, defining the corresponding `NewYou.Proof` modules. Result owns metadata capture, validation and JSON output.
- `test/proof/run.exs`, a thin test-environment CLI that calls the runner. Use existing `mix run` compilation/startup rather than depending on discovery of an uncompiled test-only Mix task.
- `test/new_you/proof/` for inexpensive ExUnit regressions, and `test/proof/` for explicit PostgreSQL contention/restart probes. A helper file under `test/proof/` must not accidentally enter the ordinary test glob.
- `test/proof/fixtures/` for deliberately broken runner fixtures and test-only provider authentication material. Fixture files are not business scenarios.
- `.github/workflows/phase8-proof.yml` for manually selected `harness_self_test` or `tb001` execution and artifact upload even after a failed command. The workflow uses the existing test database setup pattern, no new service type, and no DEV secrets. Its timeout also bounds a whole-run crash. Do not make a missing full TB result an ordinary PR merge requirement.
- `mix.exs` only if needed to declare explicit test CLI support. Existing test compilation paths and Jason already suffice; no dependency change is planned. Changes must preserve existing gates.
- `docs/development/phase8-proof.md` for operator commands and integration obligations, referencing this spec and TB-001 without redefining them.

No `lib/`, Domain Resource, migration, production configuration, architecture-rule exception or existing governance workflow change is expected. If needed, stop and explain the exact requirement before broadening scope. Use Igniter first where it safely supports a structural change; plain test/doc file authoring does not require inventing an Igniter operation.

### Result schema semantics

The companion schema defines types and required fields. Cross-field checks remain mandatory in `Result`:

1. Inventory equals the fixed list and contains no duplicates. Full mode emits every required family and browser entry exactly once, including missing/not-run results. Each entry identifies its compiled manifest digest and required case IDs. Missing manifest is represented by a null digest and empty required-case list, never completion. Self-test and diagnostic outputs still show the full coverage inventory separately from their selected checks. Self-test mode requires the exact expanded infrastructure manifest above. Diagnostic subsets never qualify as self-test or full completeness.
2. PASS requires all selected checks completed, nonempty and passing, successful cleanup and complete metadata. Full PASS additionally requires clean pre/post source, unchanged SHA/lock, every required business obligation and browser scenario demonstrated through the real path.
3. FAIL may contain completed passing checks, but cannot hide a failing/missing/not-run required check. Exit 0 is forbidden for overall FAIL. Non-zero is forbidden for overall PASS.
4. `cut_point` may be null only when no cut applies. Failing invariant and bounded reason codes are required on failed checks. Checks with no executed callback are never completed PASS. Per-case `assertion_ids` must match the manifest's required check IDs exactly, without duplicates, and their count must equal the runner-owned `assertions_executed` count. A caller-supplied count is rejected.
5. Metadata acquisition failure produces exit 2 and explicitly null unavailable fields with `metadata_complete=false`; it cannot masquerade as complete metadata. A failure envelope remains machine-readable where output is possible.
6. Evidence order follows fixed coverage and registration order. Timestamps, run identity, runtime metadata and durations may differ; deterministic means controlled scenario behavior and verdicts, not byte-identical files.

Schema validation cannot enforce equality with the executing catalog or lockfile. Any downstream consumer claiming full proof must verify the runner's complete result and exact-SHA evidence, including these semantic checks. A standalone schema validator is never a PASS authority.

### Package/API evidence and local feasibility

No new package or Oban/AshOban integration is selected. Latest package versions therefore are not pinned by this plan. Before a later unit adds or touches those packages, verify current stable HexDocs, Hex metadata and official releases, distinguishing prerelease and unreleased main. An unverifiable required API is a STOP, not permission to guess.

Baseline lockfile facts are Ash 3.37.0, AshPostgres 2.15.1, Ecto 3.14.2, Ecto SQL 3.14.0, Postgrex 0.22.4 and Jason 1.4.5. These are current repository pins, not a claim that they are ecosystem latest. The baseline has no Oban, AshOban, AshStateMachine or AshStorage dependency.

Primary documentation checked on 2026-10-22:

- [Ash 3.37.0 Signals](https://hexdocs.pm/ash/3.37.0/signals.html): inline nested listener actions, phases and no listener return contract.
- [Ash 3.37.0 Temporal Resources](https://hexdocs.pm/ash/3.37.0/temporal-resources.html): experimental application-time history; PostgreSQL requirements do not create a P8-04 need.
- [AshPostgres 2.15.1](https://hexdocs.pm/ash_postgres/2.15.1/readme.html): the existing PostgreSQL data layer.
- [Ecto SQL 3.14.0 Sandbox](https://hexdocs.pm/ecto_sql/3.14.0/Ecto.Adapters.SQL.Sandbox.html): explicit ownership, shared connections, `sandbox: false`, cleanup and ownership timeouts.
- [Mix 1.20.4 run](https://hexdocs.pm/mix/1.20.4/Mix.Tasks.Run.html): compiles and starts the application and passes arguments after the script to `System.argv/0`.
- [PostgreSQL 18 advisory locks](https://www.postgresql.org/docs/18/functions-admin.html#FUNCTIONS-ADVISORY-LOCKS) and [session information](https://www.postgresql.org/docs/18/functions-info.html#FUNCTIONS-INFO-SESSION): transaction-scoped locking, backend PID and blocker observations.
- [Official AshStorage repository](https://github.com/ash-project/ash_storage): attachment/file purpose only. Repository main is not treated as a verified stable release or an install recommendation.

DevCore doctor initially found missing ignored rendered environment files. Plan/activate repaired local rendering, and doctor then passed. A read-only TEST connection confirmed PostgreSQL 18.6, the expected TEST role/database and NOCREATEDB. The existing Repo pool size is 10; the infrastructure contention scenario needs three connections. No database role privilege or service lifecycle change was required.

### Executable acceptance and ticket decomposition

Retain WELL-5 as the single implementation ticket after this spec is complete. Controller, provider scripts, concurrency, runner and negative self-tests form one proof-infrastructure contract. Splitting them now would produce partially trustworthy machinery and duplicate review of the same false-PASS boundary. Use ordered implementation steps inside WELL-5, not artificial child tickets.

WELL-5 acceptance requires all Testing decisions above plus these reviewable deliverables:

- The named interfaces and test-only boundary are executable with no business writes or new dependency.
- The canonical runner supports distinct self-test/full modes and emits schema-valid, semantically complete results with truthful exit codes.
- All eight failure names and every provider outcome are self-tested, with no production authority.
- PostgreSQL observation proves overlap and contention; bounded failure paths leave no owned workers, locks or connections.
- A deliberately broken invariant subprocess identifies its case/invariant/cut and fails non-zero. Missing full coverage also fails non-zero.
- Production-build exclusion and secret-redaction tests pass.
- All required fast/deep/targeted gates pass on the exact implementation SHA. Full mode's expected missing-coverage failure is asserted separately, never advertised as architectural proof PASS.
- Plane reflects dependencies, review state and any discovered work; independent exact-head implementation review is required before merge recommendation.

Implementation order within WELL-5:

- [ ] Add failing behavior tests for registry/controller isolation and concurrent consumption, then implement the minimal test-only controls.
- [ ] Add separate-connection contention/timeout/crash tests, then implement bounded PostgreSQL coordination and cleanup.
- [ ] Add deterministic provider-script tests, including authentication ingress fixtures, then implement the observation-only simulator.
- [ ] Add result completeness/provenance/CLI subprocess tests, then implement catalog, schema checks, metadata and atomic output.
- [ ] Add production-exclusion, restart-isolation and canary-redaction checks; close all infrastructure false-PASS cases.
- [ ] Add the dedicated manual workflow/operator instructions and run the full acceptance commands before independent review.

Dependency order is completed WELL-38, completed WELL-3 and completed WELL-4, plus independent approval of this planning package, then WELL-5 implementation/review, then WELL-6 / P8-05 and later authorised slices. Existing WELL-5 blocked-by relations to WELL-3/WELL-4 and blocking relation to WELL-6 remain. WELL-1 is the parent. No new ticket is needed.

WELL-5 must remain in Planning with `ready-for-agent` removed until independent ChatGPT planning review approves the Grill-Me/spec/ticket set. This is a planning-review hold, not a newly invented authority blocker or proof execution start. Preserve its existing Outcome Contract and append the governing spec version/link and executable acceptance. Approval must identify the reviewed spec/PR SHA and any resolved objections before restoring implementation readiness.

### Verification commands

Planning artifacts:

```sh
git diff --check
python3 -m json.tool docs/superpowers/specs/p8-04-proof-result-v1.schema.json
python3 -m unittest discover -s tests -p 'test_foundation_smoke.py' -v
python3 -m unittest discover -s tests -p 'test_foundation_merge_gate.py' -v
python3 -m tools.foundation_integrity_smoke --manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json
devcore-project doctor
devcore-project run test -- mise exec -- mix check
git diff --stat origin/main...HEAD
git rev-parse HEAD
git status --short
```

Planning does not change application code, dependencies or architecture rules, so local `mix check.deep` is not required for this documentation diff. No Foundation Full dispatch or wait is part of this planning activity. Inspect the required Foundation Integrity status on the PR's exact head.

Future implementation commands, after planning approval and implementation only:

```sh
devcore-project doctor
devcore-project run test -- mise exec -- mix test test/new_you/proof
devcore-project run test -- mise exec -- mix run test/proof/run.exs --mode harness_self_test --output /tmp/new-you-p8-04-self-test.json
devcore-project run test -- mise exec -- mix run test/proof/run.exs --mode tb001 --output /tmp/new-you-tb001.json
devcore-project run test -- mise exec -- mix check
devcore-project run test -- mise exec -- mix check.deep
```

Use a fresh output path per invocation. At P8-04 completion the self-test command must exit 0, while full mode must exit 1 for missing later business coverage and identify that coverage. No command in this future list was executed as proof in this planning session. The implementation ticket also requires subprocess production-exclusion and negative-runner tests; it must not treat a manually observed failing command as sufficient self-test coverage.

### STOP and independent planning-review handoff

Current unresolved STOP items: none. Stop implementation and record the exact conflict in the existing Plane owner if higher authority contradicts TB-001, a Domain owner is unclear, proof creates business authority, later lifecycle decisions become prerequisites, a required API is unverifiable, genuine PostgreSQL proof needs weaker invariants, or speculative infrastructure becomes necessary. Propose the smallest upstream correction and preserve the failed proof evidence.

Independent ChatGPT planning review must examine live main, this spec/schema, accepted Q1–Q10, the updated WELL-5 Outcome Contract and exact PR diff. Challenge test-only exclusion, the eight cut bindings versus later owning actions, genuine contention, controller restart isolation, simulator authentication, coverage completeness and false-PASS subprocess tests. Confirm one-ticket decomposition and no new business schema/dependency. Return APPROVE or CHANGES REQUIRED with exact sources. Approval is planning approval only; it neither certifies TB-001 nor authorises a merge or Phase 9.
