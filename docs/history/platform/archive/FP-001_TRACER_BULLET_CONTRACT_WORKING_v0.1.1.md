# FP-001 Phase 8 NEW_TRACER_BULLET Proof Contract

- **Artifact:** FP-001 Phase 8 proof contract and self-contained task definition
- **Tracer Bullet:** `TB-001`
- **Artifact version:** `v0.1.1`
- **Candidate base main SHA:** `0972864ef7f4638c96198e19a13977e0151e9726`
- **Lifecycle:** `CANDIDATE / REVIEW PENDING / NOT CERTIFIED`
- **Proof design:** FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS
- **Proof execution:** NOT STARTED
- **Proof certification:** NOT STARTED
- **Phase 9 / Vertical Slices:** NOT STARTED / NOT AUTHORISED
- **Authority class:** active working proof contract; derived under current authority; not Product, Architecture, Domain or Roadmap law
- **Candidate predecessor:** `archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.0.md` (preserved byte-identically)

This contract records the already-approved Phase 8 proof design for the materially unproven FP-001 authentication and durable-consequence path. `TB-001` is assigned at this routed task-definition stage: the route entering WELL-2, preserved at `archive/02_OPEN_WORK_v1.2.74.md`, uses `TB-nnn` for Phase 8 proof of materially unproven paths, places proof contract/task definition next, and records in §12.30 that no identifier was allocated in that prior promotion. WELL-2 performs that next definition action, and current Open Work v1.2.76 routes the successor candidate for TB-001 contract review. Atlas's Tracer Bullet lifecycle defines the proof boundary but explicitly does not create a contract, task or identifier; this separate routed task definition does. This is the first governed TB task in the repository. WELL-1's accepted Grill comments establish the source decisions; they did not allocate this identifier. The identifier and contract remain a candidate until independent review and the repository's approval gate complete. This v0.1.1 successor makes the omitted Q61/Q66 lifecycle mechanism, Q28–Q56 implementation foundation and Q79 machine-readable evidence requirements explicit; its v0.1.0 predecessor remains unchanged in the archive.

No application, proof harness, database, migration, dependency, provider integration, Phase 9 work or additional Plane ticket is created by this contract-authoring change.

## 1. Authority and provenance

Apply the live authority hierarchy in this order:

1. Product Law: `00_PLATFORM_v1.8.0.md` and `01_DECISIONS_v1.8.0.md`.
2. Architecture Law and current synthesis: `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` and `03_ARCHITECTURE_v1.1.1.md`.
3. Domain Law: `04_DOMAIN_MAP_v1.2.0.md`.
4. Roadmap: `05_ROADMAP_v1.2.3.md`.
5. Supporting operating, frontend and engineering contracts: `PLATFORM_OPERATING_MODEL_v1.0.1.md`, `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md`, and `reference/ENGINEERING_STANDARDS_v1.0.1.md`.
6. Current Open Work and the approved FP-001 planning contracts listed below.
7. This proof contract, then proof evidence produced under it.

The accepted WELL-1 INTERNAL Q1–Q90 Grill comments are design provenance, not an authority layer. They are preserved here only within the limits of the live source hierarchy. The Delivery Atlas is navigation only. Archive files are historical evidence only. If this task exposes a contradiction with higher authority, stop at that authority and recommend the smallest safe amendment; do not amend upstream law from this contract.

Current FP-001 source contracts:

- `working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md`
- `working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md`
- `working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md`
- `working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md`
- `working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md`

## Decision traceability

The following WELL-1 INTERNAL comments identify the accepted Q1–Q90 source batches and map each batch to this contract's treatment. Their UUIDs are Plane retrieval keys for provenance, not authority references. Locked implementation-environment and verification decisions are encoded in §§7.2–7.3; Plane records provenance only and does not govern implementation.

| Accepted decisions | WELL-1 INTERNAL source comment | Contract treatment |
|---|---|---|
| Q1–Q6 | `e8215515-4a76-4dde-b809-ab4f17932dd9` | §§3, 4, 7, 8: application path, authentication breadth, browser spine, deterministic provider, PMR and bounded privileged step-up. |
| Q7–Q11 | `e84a1ae5-8517-46c1-bb33-01d3fcc8b950` | §§4, 8: password established at registration, passive magic-link retrieval, supersession and one Identity Session model. |
| Q12–Q16 | `60fba648-e589-4e67-a6e4-4dd3818e8115` | §§3–8: PMR allocation, idempotency, transactional consequence boundary, E1/E2, and deterministic seams over real PostgreSQL/Ash/Oban boundaries. |
| Q17–Q21 | `b24f0a08-8493-4dc3-9885-b47be44eda0d` | §§3, 7, 10: `:new_you` / `NewYou` / `NewYouWeb`, one repo/database and root application shape. Version snapshots remain unpinned here and must be reverified before implementation. |
| Q22 | `cc6d56dd-344f-41ff-8b2f-64246d7f1c5b` | §§3, 5, 7–9: AshOban durable execution, MessageIntent authority, atomic first scheduling proof, and STOP if the real PostgreSQL proof fails. |
| Q23 | `446a4cc7-d1b3-4a06-a0ea-3e25d8d3149f` | §§3, 7.1, 8–10: owning Ash mutation boundaries and only narrow, justified infrastructure escape hatches. |
| Q24 | `e26ca691-0980-42de-80d0-3eec3d221d67` | §§3, 5, 7, 8: Ash Signals coordinate narrowly; receiving Domains use their owning interfaces; no universal event bus or signal-based authority. |
| Q25 | `b468c38e-662a-43c0-a6a5-b3abbca72499` | §§3, 6, 10: historical reconstruction stays in the lifecycle/evidence model; Ash Temporal Resources are not introduced without a later capability-specific requirement. |
| Q26–Q27 | `4464891a-f1ad-44c2-8b80-1601e3f991b1` | §§3, 7.1, 8–10: no Ash Storage absent a file/blob requirement; targeted enforcement and executable proof of the Ash business-write boundary. |
| Q28–Q38 | `82ba53ea-b6ca-4906-a024-c6ebfb6054b3` | §7.2: deterministic ports and project key, shared dev-core PostgreSQL ownership, DEV/TEST isolation and privileges, Redis exclusion, and repository non-lifecycle-management. |
| Q39–Q47 | `ca2db611-f846-4d84-83ba-fbdfa3d8c102` | §7.2: root AGENTS.md and required project skills, UsageRules skills-only, Igniter-first changes, DEV-only Tidewave and deferred MCP/Sourceror choices with recheck-before-install version handling. |
| Q48–Q56 | `20f6110e-582e-4498-bcac-c8cdbd54d7d8` | §7.3: canonical fast/deep checks, curated analysis roles, architecture-check limits, fast-before-deep CI, optional hooks, and the separate Tracer Bullet proof workflow. |
| Q57–Q62 | `7e8dc117-7ea5-4a0b-acf9-c7fc0cd2c39b` | §§3–6, 10: Domain-owned Resource sets, Audit boundaries and relationship/state dimensions are frozen here; precise schema constraints, provenance keys and internal ID representation remain JIT implementation detail. |
| Q63–Q70 | `f75834d8-1908-4661-9b8f-be1b81fb8b0a` | §§3–8: registration acceptance, purpose-specific consume, Session authority, DeliveryAttempt cutover, EvidenceObligation/EvidenceRecord and named owning-Ash writes. |
| Q71–Q80 | `d55613cf-8026-44e3-8f90-0d7bf687231d` | §§7–10: real browser spine plus fault probes, production business path, deterministic cuts, genuine concurrency, restart/reconnect and proof separated from production completeness. |
| Q81–Q90 | `b45e180f-180a-4126-b043-3f7d555517aa` | §§8–12: nine mandatory families, all-or-nothing exit, BLOCKED / STOP, no weighted pass, and the separate human review gate before proof execution. |

At the declared base main SHA, the route entering WELL-2 was Open Work v1.2.74, Delivery Atlas v0.4.16, FP-001 Skeleton v0.1.18 and HARDEN-02 v0.5.18. Those direct predecessors are preserved byte-identically at `archive/02_OPEN_WORK_v1.2.74.md`, `archive/DELIVERY_ATLAS_WORKING_v0.4.16.md`, `archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md` and `archive/HARDEN-02_CONTRACT_WORKING_v0.5.18.md`. The first candidate route versions v1.2.75 / v0.4.17 / v0.1.19 / v0.5.19 are now preserved as the direct predecessor archives for this correction. The current successor route is Open Work v1.2.76, Delivery Atlas v0.4.18, FP-001 Skeleton v0.1.20 and HARDEN-02 v0.5.20. This candidate changes no frozen Phase 7C contract or higher authority.

## 2. Outcome and proof claim

Prove that one minimal real browser journey and focused fault probes traverse the same production Phoenix/Ash business path and preserve FP-001's locked authority, transaction, idempotency, durable-async, Communications, Audit, privacy and security invariants against real PostgreSQL.

The proof may reduce breadth to the selected path. It may not substitute a mock architecture for the real architecture, weaken a required invariant, or claim production completeness. Every mandatory invariant is binary. There is no weighted score or partial architectural pass.

## 3. Locked application and consequence architecture

The proof implementation, after this contract is approved, shall use:

- **One modular Phoenix/Ash application**, with OTP app `:new_you`, application modules `NewYou` and `NewYouWeb`, and one `NewYou.Repo`.
- PostgreSQL as durable business authority by default. Ash Domains, actions and code interfaces are ordinary business mutation boundaries. There is no ordinary direct Repo/Ecto/raw-SQL alternate business-write API. Infrastructure-only escape hatches are explicit, narrow, reviewed and preserve the same invariants.
- Privileged MFA/step-up is limited to privileged paths; participant self-service MFA is deferred. Internal durable Resource keys default to server-generated UUIDv7; PMR remains a separate public reference.
- Oban as the durable executor and `ash_oban` for the Phase 8 durable async integration. Ash Signals are narrow coordination only; they are never a universal event bus or business authority. Cross-Domain listeners call the receiving Domain's owning Ash interface.
- MessageIntent as Communications authority and Oban/job state as executor state. A job's presence, absence, retry count or completion cannot establish business success.
- Deterministic proof seams for controlled failures and provider outcomes, while the transaction, Resource, Domain, action, policy and async boundaries remain the production path.

This contract pins no package versions, provider, deployment topology, production launch policy or implementation that current authority leaves open.
No Temporal Resources or Ash Storage is introduced without a later capability-specific requirement. Redis remains part of the accepted shared dev-core environment decision, but no Phase 8 application/proof component will use it absent a concrete requirement. Cross-Domain persistence uses explicit provenance references by default; stronger PostgreSQL constraints are Domain-local, with selective cross-Domain constraints only where they preserve lawful disposition and evidence history.

## 4. Locked Identity and PMR direction

- Password and magic-link authentication are both in Phase 8. Registration establishes a password.
- Magic-link GET, HEAD, link preview, scanner and prefetch are passive. Only an explicit participant action reaches the purpose-bound consume action.
- There is one current magic-login proof per Account and purpose; a newer proof supersedes the older proof. Identity owns one Session model. Verification does not implicitly log in.
- Proof capabilities are purpose-specific, single-use, expiry-, revocation- and supersession-aware. Scanner/prefetch safety covers email verification, password reset, recovery and primary-email-change confirmation.
- Identity rechecks current Account, proof, Session, grant, security and Privacy authority at the protected mutation boundary. Stale browser state is not authority.
- PMR is Account-owned durable truth. It is not a Resource, login identifier, secret, bearer credential or authorization. Allocation is concurrency-safe and externally opaque; a retired PMR is permanently non-reusable.

Identity physical Resources are exactly:

| Resource | Proof boundary |
|---|---|
| Account | Canonical account and registration state |
| Identity-owned Token | The approved AshAuthentication token mechanism |
| Session | Identity-owned session, assurance and revocation truth |
| DeviceAssurance | Device assurance state, never a bypass for current authority |
| IdentityGrant | Scoped, current identity-side grant truth |
| RecoveryCase | Durable recovery authority and lifecycle |
| ReconciliationCase | Duplicate-identity and PMR reconciliation authority |

Do not add a separate PMR Resource or manufacture a Resource for a page, worker, provider object, status, helper or projection.

## 5. Locked Communications cutover

- A DeliveryAttempt admission is durably committed before any provider I/O. The authoritative PostgreSQL transaction is never held open across provider I/O.
- An ambiguous possibly-submitted provider operation enters reconciliation and blocks blind retry. Only proof of a safe no-operation outcome permits the contract's next action.
- Communications owns MessageIntent, DeliveryAttempt, provider observations and delivery reconciliation. A provider response cannot verify an Account, complete recovery, apply a primary-email change or create Session authority.
- Identity supplies fresh source eligibility through its owning interface. Communications never issues, consumes, revives or reinterprets Identity proof.

Communications physical Resources are exactly `MessageIntent` and `DeliveryAttempt`.
`ash_state_machine` is used selectively for genuine single-dimension lifecycles only. `MessageIntent.dispatch_disposition` uses `ash_state_machine` for `open`, `held`, `reconciliation_required` and `closed`; source eligibility, content, capability and provider outcome remain separate. Account's orthogonal state dimensions remain outside this machine. `DeliveryAttempt` admission, invocation, provider observation and reconciliation conclusion remain separate dimensions outside that machine.

## 6. Locked Audit acceptance

- **E1:** Required evidence admission is accepted before the protected effect. Failure to accept required E1 evidence blocks that effect. A successful admission followed by a failed source effect remains truthful evidence of the admitted attempt; a later source result is linked and does not rewrite the admission.
- **E2:** The source transition, `EvidenceObligation` and initial durable scheduling share the required acceptance boundary. Failure to commit that shared boundary leaves none of those three changes committed. `EvidenceRecord` may materialise later. Retry materialises the same obligation instead of multiplying assertions. Audit cannot replay the source transition.
- `EvidenceRecord` is append-only at the business layer. Audit records source-owned results and cannot become Identity, Communications or another source Domain's authority.
- `EvidenceObligation` has a deliberately small open-to-fulfilled lifecycle with integrity/reconciliation condition separate. Correction, retraction or supersession creates linked new evidence; ordinary update/delete is not a business interface.

Audit physical Resources are exactly `EvidenceObligation` and `EvidenceRecord`.

## 7. Proof topology and allowed proof surface

The proof consists of one real minimal browser spine plus focused architectural fault probes, all through the same production business path. It uses real PostgreSQL, deterministic failure injection, genuine concurrent transactions wherever concurrency is the claim, restart/reconnect proof, deterministic provider ambiguity/reconciliation, both E1 and E2 proof, and explicit authority-negative proof.

Registration uses one authoritative PostgreSQL acceptance boundary: Account, PMR, verification Token, required Communications MessageIntent, selected Audit EvidenceObligation and initial durable scheduling commit together or are absent together.

The later execution task must name one deterministic proof entrypoint that runs the complete required proof set, exits non-zero on invariant failure and emits concise machine-readable evidence suitable for CI/certification. It records the exact Git SHA, relevant runtime and dependency versions, PASS/FAIL for every mandatory proof family, and the failing invariant/cut-point where applicable. The exact Mix command name remains unfrozen until the scaffold establishes the supported entrypoint. Focused probes may run directly during diagnosis, but the governed result must include every required scenario; a green subset does not replace the proof.

The minimal browser spine exercises registration, canonical PMR assignment, explicit verification, a credential login and current Session reconstruction through the same application. Focused probes exercise other authentication methods and failure boundaries below. Browser state, local storage and LiveView assigns remain presentation state, never authority.

The implementation task may touch only the smallest app, configuration, migration, test, deterministic adapter and browser surfaces required to prove this contract. It may create the future Phoenix application and dependencies only after this contract is approved and execution is separately started. It may not start Phase 9 Vertical Slices or broad FP-001 implementation.

### 7.1 File and command boundary

No implementation paths or proof command are assigned in this candidate because the repository has no Phoenix/Ash scaffold or Mix task to inspect. This prevents this task definition from choosing a layout or entrypoint by convention alone. The later execution task must derive exact paths and its deterministic proof entrypoint from the scaffold selected under the approved application shape before it creates application or harness files. If that mapping expands the Resources, changes an authority boundary, or cannot preserve a locked invariant, stop and review a successor contract before implementation. This candidate authorises no implementation files.

## 7.2 Locked Phase-8 implementation foundation

- Reserve DEV host ports `4220–4239`; the primary Phoenix port is `4220`. Worktrees use deterministic ports `4221–4239`, not arbitrary free-port selection, and startup fails closed if an assigned port is occupied. Set `PROJECT_KEY=new_you`.
- The shared workstation `dev-core` owns `SHARED_LOCAL` PostgreSQL. The repository connects to `dev-core` but never starts, stops, recreates, deletes or otherwise lifecycle-manages it.
- DEV uses PostgreSQL role/database `new_you_dev` / `new_you_dev` with `NOCREATEDB`. TEST uses role/base database `new_you_test` / `new_you_test`; DEV and TEST use isolated databases. TEST `CREATEDB` is disabled initially; enable it only if executable partitioned-database creation proves it is required.
- Redis is not used for FP-001 Phase 8 absent a demonstrated concrete requirement.
- Keep root `AGENTS.md` NewYou-controlled and follow it with mandatory `.agents/skills/project-implementation/SKILL.md` and `.agents/skills/code-change-verification/SKILL.md`. Use UsageRules in skills-only mode; load generated Ash, Phoenix and Elixir/OTP framework skills progressively when relevant.
- Supported framework/package installation and structural changes are Igniter-first. Manual changes are allowed when Igniter cannot safely express the required change.
- Tidewave is mandatory DEV-only agent tooling at the direct deterministic endpoint `http://127.0.0.1:4220/tidewave/mcp`; worktrees use their assigned `4221–4239` port. `mix tidewave.proxy` may be a client-side convenience, not a replacement for direct deterministic endpoints.
- HexDocs MCP is deferred initially and added only on demonstrated need. Ash AI dev MCP is deferred; do not add `ash_ai` solely for another MCP endpoint. Direct Sourceror is deferred unless a genuine low-level AST/source-transformation requirement appears; transitive use through Igniter is acceptable.
- Package versions belong in `mix.exs` / `mix.lock`, not permanent agent-governance text. Recheck current stable versions immediately before installation or pinning.

## 7.3 Locked verification foundation

- `mix check` is the canonical fast check: cheap, repeatable, blocking checks and the ordinary test suite run fail-fast.
- `mix check.deep` is the separate slower deep check. Credo uses a curated high-signal configuration; selected correctness/maintainability findings become blocking after a clean baseline, while subjective/noisy style remains advisory unless promoted. Sobelow begins from the Phoenix application baseline; materially applicable findings block unless explicitly reviewed or suppressed with rationale. Dialyxir/Dialyzer belongs in the slower deep gate, not the tight edit/test loop, and becomes required in PR CI after a clean approved baseline.
- Add project-owned architecture checks only for locked, mechanically enforceable invariants. The first required checker enforces the prohibition on ordinary business Repo/raw-SQL write bypasses; each checker maps to a precise locked invariant.
- Required CI runs the fast `mix check` gate before `mix check.deep`, so cheap failures report first. Local hooks are optional convenience only, never correctness authority; CI remains binding.
- The Tracer Bullet has a dedicated deterministic proof command/workflow separate from routine CI. Stage-specific expensive proof becomes permanent only where ongoing regression value justifies it.

## 8. Required scenario families and acceptance evidence

All nine families are mandatory. Each result records the invariant, real boundary exercised, deterministic cut or race, expected durable state, and evidence needed to distinguish pass from stop.

| # | Scenario family | Required proof |
|---|---|---|
| 1 | Registration / PMR / reconciliation | Account, password and PMR commit as one authoritative operation; verification Token, required Communications MessageIntent, selected Audit EvidenceObligation and initial durable scheduling commit together at the registration boundary or are absent together; idempotent retry converges; genuine same-email transactions and PMR collision pressure preserve one canonical result; duplicate-account reconciliation is Identity-owned; retired PMR never reuses. |
| 2 | Proof capability / scanner / replay / supersession | Verify, reset, recovery and new-address confirmation retrieval through HEAD/GET/preview/scanner/prefetch consumes nothing; explicit purpose-specific consume is single-use; replay, expiry, revocation and supersession fail closed; newer magic-login proof replaces the prior current proof. |
| 3 | Session / login / revocation / restart | Password and magic-link login share the Identity Session model; verification does not log in; current Session, credential and security checks govern; revocation survives restart/reconnect; stale UI cannot restore authority. |
| 4 | Communications durability / backlog / provider ambiguity | Must-not-lose source handoff is durable before execution; `ash_oban`/Oban recover after restart and backlog; DeliveryAttempt commits before provider I/O; no transaction spans provider I/O; ambiguous outcome blocks retry and is reconciled deterministically; provider evidence never grants Identity authority. |
| 5 | Audit E2 | Source transition, EvidenceObligation and initial scheduling share one acceptance boundary; failure rolls back the required boundary; replay materialises the same EvidenceRecord once; restart repairs materialisation without replaying the source transition. EvidenceRecord records only the restricted accepted source consequence, without secrets, excess payload or a second business truth. |
| 6 | Audit E1 | Using security-hold release as the representative privileged effect: required admission commits before the effect; admission failure blocks it; source failure after accepted admission preserves the truthful attempt; a distinct attempt has distinct admission evidence. EvidenceRecord records only bounded admission evidence, without secrets, excess payload or a second business truth. |
| 7 | Recovery / primary-email change | Identity owns cases, confirmation, canonical email and Session/credential consequences; Communications notices do not complete the change; duplicate, replay, expiry, restart and supersession cuts preserve old authority until an Identity apply transition commits. |
| 8 | Non-enumeration / current Privacy re-read | Responses remain non-enumerating under registration, login, recovery and support pressure; protected actions observe consent changes by re-reading current Privacy and Identity authority; stale purpose/consent state cannot pass; no generic consent platform is introduced. |
| 9 | Source-authority / bypass negatives | Direct ordinary Repo/Ecto/raw-SQL business writes are rejected by architecture enforcement; browser, Communications, Audit, Analytics, Oban, provider and Signals cannot impersonate source truth or bypass the owning Ash interface; executor state cannot satisfy a business invariant. |

Where a scenario claims concurrency, use separate genuine PostgreSQL transactions and observe the committed winner and loser. Where a scenario claims restart, terminate/reconnect the runtime boundary and reconstruct from PostgreSQL and durable executor state. Fake in-memory repositories, mocked transaction results, skipped restart probes and simulated concurrency do not satisfy those claims.

## 9. Failure, stop and evidence rules

The required architecture is all-or-nothing for its invariants. A failure to preserve required PostgreSQL atomicity, identity ownership, must-not-lose consequences, E1/E2 acceptance, safe provider ambiguity or current authority is `BLOCKED / STOP`. It is not technical debt, a weighted pass, permission to weaken an invariant or a reason to start Phase 9.

The proof result must report each required scenario as pass or fail with its durable evidence. Unrun, flaky, mocked in place of a required real boundary, or otherwise unproven evidence is not a pass. Proof execution and proof certification remain separate lifecycle gates. This contract candidate records neither a proof result nor a proof certification.

If evidence reveals an upstream contradiction, stop at the authority that owns it. Recommend the smallest safe amendment and re-proof consequence. Do not revise the locked design here to make a failing implementation pass.

## 10. Task boundary and completion gate

This candidate defines one outcome, exact scope, current authoritative references, Resources, actions, data/transaction boundaries, security/privacy constraints, concurrency, async, tests, acceptance criteria, allowed tools and STOP conditions required by the Phase 8 task route.

After independent review and approval, a separate execution start may implement only the bounded proof. The coding task must use the `NewYou`/`NewYouWeb` modular Phoenix/Ash application, one repo and the Resources listed in §§4–6; it must follow the foundation and verification decisions in §§7.2–7.3, and provide the deterministic proof entrypoint and nine scenario families above, plus the minimal browser spine. Proof execution must stop at the first unsatisfied invariant. Only a later evidence review may certify proof. Only a separate governed transition after certified proof can consider Phase 9.

The authoring tools for this documentation task are Git, the Foundation Integrity test suite and repository review. The future approved proof task is limited to the repository's Phoenix/Ash/Mix/PostgreSQL test toolchain and deterministic local provider adapter. It specifies no live provider credential, production endpoint or vendor account. It uses the accepted shared workstation dev-core environment without lifecycle-managing its services; the environment's Redis service is not an application/proof dependency absent a concrete Phase 8 requirement.

## 11. Version, history and lifecycle

`v0.1.0` is the initial proof-contract candidate. This `v0.1.1` PATCH successor makes previously accepted proof-design and implementation-foundation decisions explicit, preserves the exact v0.1.0 predecessor byte-identically under `docs/00_platform/archive/`, and updates the active manifest navigation and Open Work route. On later substantive change, create another explicit successor and preserve its exact predecessor. Do not rewrite an approved or historical contract in place. Current-status promotion and proof certification are separate from the contract design version, follow the repository's review/evidence and status-successor practice, and preserve the exact reviewed candidate.

The governing Open Work, Atlas, Skeleton and HARDEN-02 documents use their established patch successors for this routing-only transition; their direct predecessors are archived byte-identically. This derived contract is listed by the manifest for navigation/integrity only and is not promoted to `governing_documents` or `reference_documents`.

## 12. Lifecycle state

```text
PROOF CLASSIFICATION: COMPLETE / FINALISED — NEW_TRACER_BULLET
TRACER BULLET: REQUIRED / DEFINED AS REVIEW CANDIDATE
TRACER BULLET ID: TB-001
CONTRACT: CANDIDATE / REVIEW PENDING / NOT CERTIFIED
PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS
PROOF EXECUTION: NOT STARTED
PROOF RESULT: NOT STARTED
PROOF CERTIFICATION: NOT STARTED
PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY); EXECUTION WAITS FOR CONTRACT APPROVAL
PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED
```
