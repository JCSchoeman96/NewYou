# NewYou Communications Pre-JIT Discovery — Working v0.9.0

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY
- **Stream:** FP-001 Communications JIT Domain Dossier preparation
- **Document version:** v0.9.0
- **Predecessor:** `NEWYOU_COMMUNICATIONS_PREJIT_DISCOVERY_WORKING_v0.8.0.md` — preserved unchanged
- **Earlier predecessors:** `NEWYOU_COMMUNICATIONS_PREJIT_DISCOVERY_WORKING_v0.1.0.md` through `NEWYOU_COMMUNICATIONS_PREJIT_DISCOVERY_WORKING_v0.7.0.md` — preserved unchanged
- **Live repository baseline:** `JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`
- **Baseline verified:** 2026-10-05
- **Intended repository placement:** `docs/00_platform/working/communications/NEWYOU_COMMUNICATIONS_PREJIT_DISCOVERY_WORKING_v0.9.0.md`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap amendment:** NONE
- **Phase 7C / proof classification / Phase 8 authority:** NONE
- **Provider selection / OQ-036 resolution:** NONE

This document is the cumulative working record for the FP-001 Communications Pre-JIT discovery / Grill-Me stream. It may preserve upstream-derived obligations, accepted working design conclusions, rejected models, open hypotheses, proof obligations and conditional-dossier findings. It may not silently amend Product Law, Architecture Law, Domain Law, Roadmap, supporting authority, Open Work, the FP-001 Skeleton or the certified Identity & Access JIT Domain Dossier.

If a later pressure test exposes an upstream contradiction or missing policy, this document must STOP at the owning authority level, record the smallest required amendment and avoid repairing that law inside Communications design.

---

# 1. Working-document governance

## 1.1 SemVer rule

This Pre-JIT stream uses working SemVer:

- `0.MINOR.0` — substantive new accepted working semantics, pressure-test classes, upstream-delta decisions or material register restructuring;
- `0.MINOR.PATCH` — non-semantic status, routing, provenance, wording or mechanical correction that preserves accepted working meaning;
- predecessor bytes are preserved when a successor is created; accepted working findings are not silently rewritten.

A working conclusion remains revisitable when new evidence, changed authority, contradiction or a later scenario exposes a flaw. A revision must state what changed and why.

## 1.2 Working classification

Each scenario conclusion is classified as exactly one of:

- `UPSTREAM_DERIVED` — current authority already determines the relevant semantic result; this stream only applies it to Communications;
- `WORKING_DESIGN_ACCEPTED` — authority leaves implementation-grade semantics open and this stream accepts a bounded working design for later governed JIT drafting;
- `OPEN_HYPOTHESIS` — insufficient evidence or intentionally deferred semantics remain.

These labels do not create governing authority.

---

# 2. Current live authority baseline

The live repository was independently rechecked before v0.1.0 creation. `main` remained:

`3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

Current relevant sources include:

- `docs/00_platform/README.md`;
- `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`;
- `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`;
- `docs/00_platform/00_PLATFORM_v1.6.0.md`;
- `docs/00_platform/01_DECISIONS_v1.6.0.md`;
- `docs/00_platform/02_OPEN_WORK_v1.2.56.md`;
- `docs/00_platform/03_ARCHITECTURE_v1.1.1.md`;
- `docs/00_platform/04_DOMAIN_MAP_v1.2.0.md`;
- `docs/00_platform/05_ROADMAP_v1.2.0.md`;
- `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md`;
- `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md`;
- `docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md`;
- `docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md`;
- `docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md`;
- `docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.0.md`;
- `docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.8.md`.

Relevant Pre-JIT methodology/provenance was also inspected from the current Privacy & Consent, Health/Safety/Plans, Commerce/Entitlements/Recurring and Content & Media working packs.

Current programme route:

```text
HARDEN-02 EXECUTION: COMPLETE / CERTIFIED
→ ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED
→ FP-001 PMR RECONCILIATION: COMPLETE / CERTIFIED
→ IDENTITY v0.1.3 PROMOTION: COMPLETE / CERTIFIED / CURRENT
→ COMMUNICATIONS JIT DOMAIN DOSSIER: REQUIRED / NEXT / NOT_STARTED
→ REMAINING REQUIRED / CONDITIONAL PHASE 7B
→ PHASE 7C
→ PROOF CLASSIFICATION
→ PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES
```

Communications finalisation remains `BLOCKED / STOP` until its governed work is complete. Privacy & Consent, Content & Media and Audit & Evidence remain conditional and require explicit adjudication. Analytics remains not required as an FP-001 dossier.

---

# 3. Frozen upstream boundaries consumed by this stream

## 3.1 Identity authority

Identity & Access remains sole authority for:

- Security Challenge purpose;
- validity;
- expiry;
- supersession;
- revocation;
- consumption;
- email verification truth;
- recovery completion;
- primary-email-change truth;
- canonical account email.

Communications owns communication intent, provider execution/status and provider evidence only.

The certified separation remains:

```text
provider accepted != provider delivered
provider delivered != proof consumed
proof consumed != provider delivery evidence
```

Provider evidence cannot establish Identity truth.

## 3.2 Certified protected-delivery seam

For FP-001 verification, password reset, recovery and new-address primary-email-change confirmation, crash-safe delivery may retain a bounded protected delivery capability only for the already-authorised delivery purpose.

The protected capability:

- is sensitive delivery machinery, not a second Security Challenge authority;
- is bound to one Communications message intent and the corresponding Identity-owned purpose/challenge;
- is recoverable only by the purpose-scoped delivery executor;
- cannot itself verify an Account, complete recovery or confirm an email change;
- must not outlive the governing proof validity/terminal boundary;
- must be cleared or rendered irrecoverable when no longer required.

Plaintext bearer material or rendered secret-bearing URLs must not appear in ordinary Identity/Communications fields, Oban arguments, logs, telemetry, Audit, Analytics or ordinary operational displays.

Source issuance, Communications durable intent and any required protected capability must commit atomically or leave no committed issuance whose must-not-lose delivery obligation was lost.

## 3.3 Durable asynchronous consequence rule

Architecture classifies must-not-lose delivery as a Class-B durable asynchronous consequence:

```text
authoritative transition
→ establish durable execution intent atomically
→ commit
→ durable executor
→ repeat-safe handler
→ re-read/revalidate current authority
→ success / retry / terminal-visible state
```

Oban is execution machinery, not business truth. Queue uniqueness may suppress work but is not business idempotency.

## 3.4 Engineering risk

The Communications path is `HIGH` engineering risk wherever it materially touches authoritative state, authentication/security, sensitive data, concurrency/idempotency, provider reconciliation or durable async/recovery. Exact proof execution remains downstream, but the later JIT contract must carry the applicable proof obligations rather than weakening them.

---

# 4. Starting resource hypothesis

Current starting hypothesis after live-authority reconstruction:

| Concept | v0.1.0 position |
|---|---|
| `MessageIntent` | REQUIRED candidate durable business concept |
| `DeliveryAttempt` | REQUIRED candidate durable business concept |
| Protected delivery capability | REQUIRED sensitive mechanism where applicable; not automatically a business Resource |
| `SubscriberContact` | NOT YET JUSTIFIED for FP-001 |
| `NotificationPreference` | NOT YET JUSTIFIED for FP-001 |
| `InAppNotification` | NOT YET JUSTIFIED; FES states participant notification centre is not an FP-001 prerequisite |
| `CommunicationJourney` | NOT YET JUSTIFIED for FP-001 |
| Generic `Channel` Resource | NOT JUSTIFIED merely because multiple channel types exist |
| Generic Outbox Resource | NOT JUSTIFIED merely because durable async exists |
| Campaign/fan-out Resource | OUT OF CURRENT FP-001 NEED unless later evidence proves otherwise |

This table is not final. Every row remains subject to pressure testing.

---

# 5. Accepted working-design register — v0.1.0

Identifiers in this section are local working identifiers only. They are not governed DEC/ARC/OQ/FP/TB/VS/HH identifiers.

## COMM-WD-001 — MessageIntent is the logical communication obligation

**Status:** `WORKING_DESIGN_ACCEPTED`

`MessageIntent` represents one platform-owned logical communication obligation requested by an authorised source Domain. Its business idempotency identity derives from the originating logical obligation and message role/purpose, not from an HTTP request UUID, Oban job ID, trace ID or provider request ID.

The exact idempotency-key composition remains intentionally unfrozen until the resend, destination-change and multiple-challenge scenarios are pressure-tested.

## COMM-WD-002 — DeliveryAttempt is provider execution/evidence, not the logical message

**Status:** `WORKING_DESIGN_ACCEPTED`

`DeliveryAttempt` represents a concrete provider/channel submission operation and its normalized provider evidence. One `MessageIntent` may have multiple `DeliveryAttempt`s when a new provider submission is lawfully authorised after a definitive retryable failure.

A safe replay/reconciliation of the same provider operation using a provider-supported stable idempotency identity remains the same logical attempt rather than manufacturing a new attempt.

## COMM-WD-003 — Atomic source-to-intent establishment is mandatory

**Status:** `UPSTREAM_DERIVED`

For the certified FP-001 Identity protected-delivery purposes, the Identity issuance/transition, Communications `MessageIntent` and required protected delivery capability must have one all-or-nothing durability boundary.

The source Domain may invoke the Communications owner interface inside that transaction; it may not bypass Communications ownership with direct foreign persistence. Same-database atomic participation does not create shared-write ownership when each Domain still owns and validates its own mutation.

## COMM-WD-004 — Durable execution must not have an unprotected enqueue gap

**Status:** `WORKING_DESIGN_ACCEPTED`

Preferred smallest shape:

```text
Identity authoritative transition/challenge issuance
+ Communications MessageIntent
+ required protected delivery capability
+ transactional durable job scheduling
→ one commit
```

If exact framework/proof constraints make transactional job scheduling unsuitable, a second lawful shape may be used only if the committed `MessageIntent` itself is sufficient durable obligation and deterministic restart/reconciliation discovers every actionable unscheduled intent.

Rejected is a best-effort `commit intent → later enqueue` seam with no durable reconciliation guarantee.

No generic Outbox Resource is justified by this conclusion alone.

## COMM-WD-005 — Only one new provider submission may be authorised at a time for one logical attempt path

**Status:** `WORKING_DESIGN_ACCEPTED`

Duplicate jobs, two BEAM nodes or retry races must not independently authorise concurrent new provider sends for the same attempt path. The send-authorisation/attempt-claim boundary must be protected by authoritative PostgreSQL state/constraints/atomic transition semantics rather than queue uniqueness or process-local coordination.

Exact lock/constraint/action mechanics remain later JIT/proof detail.

## COMM-WD-006 — Ambiguous provider outcome is an explicit unresolved condition

**Status:** `UPSTREAM_DERIVED` with Communications specialisation

A timeout, lost response, worker crash around provider I/O or otherwise ambiguous acknowledgement is not success and is not automatically retryable.

Once a provider submission may have occurred but its outcome is not definitive, Communications preserves an unresolved/reconciliation-required condition. It must not launch a fresh provider send blindly.

A replay is permitted only where the same provider operation can be repeated without creating another provider-side message/consequence, or where subsequent evidence proves that a new submission is lawful.

## COMM-WD-007 — Retry does not create a new MessageIntent

**Status:** `WORKING_DESIGN_ACCEPTED`

Infrastructure/provider retry of the same authorised logical communication remains under the same `MessageIntent`.

- safe replay of the same ambiguous provider operation → same `DeliveryAttempt`;
- a genuinely new provider submission after a definitive retryable failure → new `DeliveryAttempt`, same `MessageIntent`;
- new `MessageIntent` → only when a new logical communication obligation exists.

Participant-requested resend is deliberately not resolved here because the multiple-challenge/resend pressure-test cluster may prove that some resends are new obligations while others are additional attempts under an existing obligation.

## COMM-WD-008 — Provider submission state and delivery evidence are independent dimensions

**Status:** `WORKING_DESIGN_ACCEPTED`

Do not collapse `accepted`, `delivered`, `bounced/failed-delivery` and Identity proof consumption into one lifecycle state.

A `DeliveryAttempt` conceptually carries at least separate provider-submission and delivery-evidence dimensions. Exact enums/fields are not frozen in Pre-JIT.

Provider callbacks may refine provider evidence but cannot establish Identity business truth.

## COMM-WD-009 — Duplicate/reordered provider evidence reconciles monotonically

**Status:** `WORKING_DESIGN_ACCEPTED`

Duplicate callbacks are normal. Reordered callbacks must not regress a more authoritative/complete provider-evidence conclusion or reopen an already terminal business outcome. Reconciliation interprets external evidence against the attempt's current/historical state and the source Domain's current validity.

Exact provider-event deduplication fields remain OQ-036/provider/JIT detail.

## COMM-WD-010 — Definitive provider failure remains under the same intent until lawfully resolved

**Status:** `WORKING_DESIGN_ACCEPTED`

A definitive provider rejection/failure closes the affected attempt. If current source authority still permits delivery and the applicable bounded retry policy permits another submission, Communications creates another `DeliveryAttempt` under the same `MessageIntent`.

A non-retryable failure or exhausted bounded policy leads to terminal-visible message failure rather than silent disappearance or indefinite uncontrolled retry.

Exact retry classes, counts, delays, provider throttling and evidence requirements remain under `OQ-036`/later JIT where not already frozen.

## COMM-WD-011 — Oban uniqueness is optimisation, not correctness

**Status:** `UPSTREAM_DERIVED`

Oban uniqueness may reduce duplicate scheduled work. Correctness must still hold if duplicate jobs execute, a job is retried after restart, or two workers race.

The durable business invariant is enforced by Communications-owned state/constraints and current source-authority checks.

## COMM-WD-012 — Provider acceptance does not automatically discharge every delivery obligation

**Status:** `OPEN_HYPOTHESIS`

Current authority explicitly distinguishes provider acceptance from delivery. The exact channel-specific evidence that is sufficient to mark a `MessageIntent` satisfied is not frozen here because `OQ-036` remains unresolved.

The JIT contract may define provider-independent lifecycle states, but it must not fabricate `delivered` without evidence or silently equate `accepted` with Identity proof consumption.

---

# 6. Working lifecycle model — first cluster

The following is semantic working shape, not final enum/schema design.

## 6.1 MessageIntent lifecycle dimension

Conceptual states:

```text
PENDING
→ UNRESOLVED / RECONCILIATION_REQUIRED   (when safe continuation cannot yet be determined)
→ SATISFIED                              (under the applicable channel/delivery policy)
→ TERMINAL_FAILURE                       (no further lawful retry under bounded policy)
→ CANCELLED_OR_INVALIDATED               (source authority no longer permits delivery)
```

Terminal states:

- `SATISFIED`;
- `TERMINAL_FAILURE`;
- `CANCELLED_OR_INVALIDATED`.

`PENDING` and `UNRESOLVED` remain non-terminal obligations. They must survive worker/node restart and remain discoverable.

The exact satisfaction criterion is intentionally not frozen while `OQ-036` remains open.

## 6.2 DeliveryAttempt independent dimensions

Do not force all provider behaviour into one enum.

### Provider submission dimension

```text
PREPARED
→ DISPATCH_AUTHORISED
→ ACCEPTED | REJECTED | OUTCOME_UNKNOWN
```

### Provider delivery-evidence dimension

Conceptually:

```text
NO_DELIVERY_EVIDENCE
→ DELIVERED_EVIDENCE | DELIVERY_FAILURE_EVIDENCE | DELIVERY_EVIDENCE_UNKNOWN/UNAVAILABLE
```

A provider may acknowledge submission before later delivery/bounce evidence exists. Those states are not Identity states.

### Attempt guards

- only one worker/node may win a new dispatch authorisation for the same attempt path;
- a crash after dispatch may have begun yields ambiguity, not automatic retry authority;
- definitive retryable failure may authorise another `DeliveryAttempt` under the same `MessageIntent`;
- duplicate/reordered evidence cannot create a second logical message or regress authoritative source truth.

---

# 7. Pressure-test register — first cluster

## COMM-PT-001 — Identity issuance succeeds but Communications durable intent/capability fails

- **Scenario:** Identity challenge/transition would commit while Communications intent or required protected capability fails to persist.
- **Authority involved:** certified Identity v0.1.3 protected-delivery seam; Architecture Class-B durable consequence rule; Communications Domain ownership.
- **Durable truths and owner:** Identity owns challenge/transition truth; Communications owns `MessageIntent`; protected capability is delivery machinery.
- **Concurrency/retry/reordering/crash:** crash/failure at source-to-intent boundary.
- **Rejected models:** post-commit best-effort notification callback; committed challenge with no durable delivery obligation; foreign direct write bypassing Communications owner action.
- **Required invariant:** no committed must-not-lose issuance may exist without its durable Communications obligation and required protected capability.
- **Recommended JIT shape:** owner-mediated same-database atomic establishment; no provider I/O in the authoritative transaction.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** injected failure at each establishment step proves full rollback/no orphan challenge and no secret leakage.
- **Verdict:** PASS — starting two-concept model survives.

## COMM-PT-002 — Crash after intent commit but before ordinary worker execution/enqueue handoff

- **Scenario:** durable source transition and `MessageIntent` exist, process/node dies before a worker can execute.
- **Authority involved:** Architecture Class-B; Engineering Standards HIGH durable-async/recovery rules.
- **Durable truths and owner:** `MessageIntent` is Communications authority; queue/job is execution machinery.
- **Concurrency/retry/reordering/crash:** restart must not lose the obligation.
- **Rejected models:** volatile process message; PubSub; untracked post-commit enqueue; manual operator discovery as the only recovery path.
- **Required invariant:** every committed actionable intent is eventually rediscoverable for execution or remains explicitly unresolved/terminal-visible.
- **Recommended JIT shape:** prefer transactional durable scheduling with the same commit; otherwise prove deterministic intent-driven reconciliation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** deterministic crash at the post-commit/pre-execution boundary; restart; one logical intent continues without duplicate business effect.
- **Verdict:** PASS WITH WORKING RULE.

## COMM-PT-003 — Duplicate worker execution across nodes

- **Scenario:** two jobs/workers/nodes attempt the same communication concurrently.
- **Authority involved:** Architecture idempotency/concurrency doctrine; Engineering Standards HIGH concurrency/idempotency.
- **Durable truths and owner:** Communications owns intent and attempt authorisation.
- **Concurrency/retry/reordering/crash:** simultaneous execution is normal and must be safe.
- **Rejected models:** relying on Oban uniqueness alone; in-memory mutex; ETS/GenServer business lock; provider-side duplicate tolerance as the invariant.
- **Required invariant:** concurrent executors cannot independently authorise two new provider submissions for the same attempt path.
- **Recommended JIT shape:** PostgreSQL-backed atomic claim/transition/constraint semantics at the Communications boundary; exact mechanism deferred.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** deterministic two-worker interleaving using real PostgreSQL correctness semantics; prove one authorised provider submission path.
- **Verdict:** PASS.

## COMM-PT-004 — Provider accepted request but response is lost / timeout occurs

- **Scenario:** provider may have accepted a message, but Communications receives no definitive response.
- **Authority involved:** Architecture provider ambiguity; Engineering Standards error/reconciliation rules; Product no-duplicate-after-retry requirement.
- **Durable truths and owner:** `DeliveryAttempt` owns provider execution/evidence; `MessageIntent` remains unresolved; Identity truth unchanged.
- **Concurrency/retry/reordering/crash:** a retry may duplicate the externally visible message.
- **Rejected models:** timeout = failure; timeout = success; immediate blind resend; new `MessageIntent` per retry.
- **Required invariant:** ambiguous external outcome remains explicit and cannot fabricate certainty or authorise unsafe duplicate send.
- **Recommended JIT shape:** `OUTCOME_UNKNOWN` / reconciliation-required evidence state; safe replay only when the same provider operation is provably idempotent/reconcilable.
- **Conclusion:** `UPSTREAM_DERIVED` plus bounded Communications specialisation.
- **Upstream amendment:** NO; `OQ-036` remains the correct provider capability/policy gate.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** simulate provider acceptance with lost response; prove no blind second provider submission and later reconciliation convergence.
- **Verdict:** PASS.

## COMM-PT-005 — Worker crash after provider call may have started but before outcome persistence

- **Scenario:** process dies in the external-I/O ambiguity window.
- **Authority involved:** Architecture provider ambiguity and crash recovery.
- **Durable truths and owner:** existing attempt remains Communications-owned unresolved evidence.
- **Concurrency/retry/reordering/crash:** restart must not assume provider call did or did not happen.
- **Rejected models:** reset attempt to retryable merely because worker lease expired; create a replacement intent; mark terminal success.
- **Required invariant:** crash in the I/O ambiguity window preserves an unresolved obligation until evidence or a safe same-operation replay resolves it.
- **Recommended JIT shape:** restart/reconciliation treats the affected attempt as potentially externally executed.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** kill executor at controlled points immediately before/after provider invocation and before result persistence; verify safe recovery path.
- **Verdict:** PASS.

## COMM-PT-006 — Provider definitively rejects or fails before accepting

- **Scenario:** provider returns definitive retryable or non-retryable failure.
- **Authority involved:** Product/Domain bounded retry + terminal-visible failure; OQ-036 exact retry/provider policy.
- **Durable truths and owner:** failed `DeliveryAttempt`; `MessageIntent` remains pending if another lawful attempt is allowed.
- **Concurrency/retry/reordering/crash:** retry must not generate a second logical obligation.
- **Rejected models:** new `MessageIntent` for each infrastructure retry; indefinite retry; silently drop after queue exhaustion.
- **Required invariant:** bounded retries remain attached to one logical intent and terminal failure remains discoverable.
- **Recommended JIT shape:** definitive failed attempt closes; a fresh provider submission is a new `DeliveryAttempt` under the existing intent when current authority/policy allows it.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** retryable vs terminal failure; exhausted retries; restart after exhaustion; prove visible unresolved/terminal state.
- **Verdict:** PASS.

## COMM-PT-007 — Delayed acceptance/delivery evidence arrives after an ambiguous attempt

- **Scenario:** an attempt is unresolved; later provider evidence confirms acceptance/delivery/failure.
- **Authority involved:** Architecture provider reconciliation/reordering.
- **Durable truths and owner:** provider evidence belongs to Communications; source business truth remains with Identity.
- **Concurrency/retry/reordering/crash:** late evidence may arrive after restarts and duplicate callbacks.
- **Rejected models:** discard late callback because local worker timed out; create a new intent; let callback mutate Identity proof.
- **Required invariant:** legitimate late evidence reconciles against the same attempt and cannot multiply or rewrite source truth.
- **Recommended JIT shape:** normalized evidence update/reconciliation on the existing attempt; current source validity still governs any further delivery action.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** delayed acceptance after local timeout; delayed delivery after acceptance; duplicate callback; restart between events.
- **Verdict:** PASS.

## COMM-PT-008 — Duplicate and reordered provider callbacks

- **Scenario:** delivered/failed/accepted callbacks repeat or arrive out of order.
- **Authority involved:** Architecture duplicate/reordered external evidence rule; Domain provider-evidence ownership.
- **Durable truths and owner:** Communications delivery evidence only.
- **Concurrency/retry/reordering/crash:** concurrent callbacks may race with worker reconciliation.
- **Rejected models:** callback order = business order; last callback wins blindly; callback directly finalises Identity.
- **Required invariant:** repeated reconciliation converges to the same lawful Communications evidence conclusion for unchanged evidence/current authority.
- **Recommended JIT shape:** idempotent evidence receipt and monotonic reconciliation; exact provider event identity/precedence remains adapter/JIT detail.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** duplicate + reordered callback sequences, including concurrent worker reconciliation.
- **Verdict:** PASS.

## COMM-PT-009 — Infrastructure retry: same logical message or new logical intent?

- **Scenario:** retry after definitive technical/provider failure.
- **Authority involved:** Architecture business-idempotency identity; Product no-duplicate-after-retry requirement.
- **Durable truths and owner:** logical obligation = `MessageIntent`; provider submission = `DeliveryAttempt`.
- **Concurrency/retry/reordering/crash:** duplicate jobs/retries must converge.
- **Rejected models:** one MessageIntent per job; one MessageIntent per provider call; provider request UUID as business identity.
- **Required invariant:** infrastructure retry cannot manufacture a new logical communication obligation.
- **Recommended JIT shape:** same MessageIntent; new DeliveryAttempt only for a genuinely new provider submission after lawful retry authorisation; safe replay of same provider operation remains same attempt.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED` for infrastructure retry; participant-driven resend remains `OPEN_HYPOTHESIS` pending its dedicated cluster.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** repeated job execution and multiple retry paths converge on one intent and the lawful number of provider attempts.
- **Verdict:** PASS / PARTIAL OPEN EDGE.

## COMM-PT-010 — Oban uniqueness collision or duplicate jobs

- **Scenario:** queue uniqueness expires/is bypassed, or duplicate equivalent jobs exist.
- **Authority involved:** Architecture explicitly says queue uniqueness is not business idempotency.
- **Durable truths and owner:** Communications business state, not queue state.
- **Concurrency/retry/reordering/crash:** duplicate executors may still run.
- **Rejected models:** Oban uniqueness as the only duplicate-send safeguard.
- **Required invariant:** business state/constraints protect the logical consequence even when queue dedupe does not.
- **Recommended JIT shape:** queue uniqueness optional as load reduction only; all safety lives at Communications state/action boundary.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later proof:** deliberately insert/execute duplicate jobs and prove invariant remains true.
- **Verdict:** PASS.

---

# 8. Rejected-model register — v0.1.0

1. **Provider I/O inside the authoritative Identity transaction.** Rejected: slow/ambiguous network I/O cannot define the commit boundary.
2. **Identity commit followed by best-effort Communications callback/enqueue with no durable reconciliation.** Rejected: creates a must-not-lose crash gap.
3. **Plaintext bearer token or secret-bearing URL in Oban args, logs, telemetry, Audit, Analytics or ordinary Communications fields.** Rejected by certified protected-delivery seam.
4. **Oban uniqueness as business idempotency.** Rejected by Architecture.
5. **One new MessageIntent for every job execution/provider retry.** Rejected: transport execution identity is not logical business identity.
6. **Timeout/unknown provider result treated as retryable failure.** Rejected: can duplicate externally visible messages.
7. **Provider acceptance treated as delivery or Identity proof consumption.** Rejected.
8. **Provider callback order treated as business-authority order.** Rejected.
9. **ETS/GenServer/process-local locking as cross-node send correctness.** Rejected as business authority.
10. **Generic Outbox Resource introduced by pattern preference alone.** Rejected at current evidence level; MessageIntent already represents the durable obligation.

---

# 9. Upstream-delta register — v0.1.0

**NONE IDENTIFIED IN THIS CLUSTER.**

The current Product/Architecture/Domain/Identity/Engineering Standards authorities are sufficient to state the first-cluster invariants without amendment.

`OQ-036` remains deliberately unresolved. This cluster does not select a provider, channel adapter, retry count/backoff, callback contract or provider-specific idempotency mechanism.

---

# 10. Unresolved-gate register — v0.1.0

| Gate / open matter | Current effect on this stream |
|---|---|
| `OQ-036` notification providers/channel policy | Does not prevent provider-independent lifecycle/idempotency design. Still required before affected release/channel promise; provider-specific safe replay, callback evidence and exact retry rules remain unresolved. |
| `OQ-035` abuse thresholds | Not exercised by this first cluster; remains release-only and will be revisited during resend/enumeration/flooding pressure tests. |
| Exact MessageIntent business-idempotency key composition | Intentionally deferred to resend, destination-change and multiple-valid-challenge scenarios. |
| Exact channel-specific satisfaction criterion | Open while provider/channel evidence policy remains unresolved; `accepted` must not be mislabeled `delivered`. |
| Exact PostgreSQL/Ash transaction/claim mechanism | Later JIT/proof implementation detail; current semantic invariant is frozen at working level only. |

---

# 11. Cross-stream dependency register — v0.1.0

| Stream / Domain | First-cluster finding |
|---|---|
| Identity & Access | REQUIRED dependency. Certified v0.1.3 seam supplies source validity and protected-delivery constraints. No ownership conflict found. |
| Privacy & Consent | Dependency exists in mature Communications, but this cluster does not require new Privacy-owned semantics. Conditional dossier remains unpulled. |
| Content & Media | Message-template provenance exists upstream, but no first-cluster scenario requires new C&M lifecycle semantics. Conditional dossier remains unpulled. |
| Audit & Evidence | Provider/delivery evidence remains Communications truth; Audit remains separate restricted evidence where required. No new Audit-owned semantics required in this cluster. Conditional dossier remains unpulled. |
| Analytics | Consumer only. Provider/delivery evidence must not become business conversion truth. No dossier required. |
| Engineering Standards | Current supporting authority applies; first-cluster implementation will be HIGH and must later carry applicable concurrency/provider/recovery/leakage proof. |

---

# 12. Conditional-dossier adjudication — provisional v0.1.0

## Privacy & Consent

**Disposition:** `CONDITIONAL / NOT PULLED FORWARD YET`.

Reason: the first-cluster must-not-lose, retry and provider-ambiguity semantics can be specified entirely from current Identity, Communications and Architecture authority. No new Privacy-owned acceptance, withdrawal, deletion or purpose state must be invented here.

## Content & Media

**Disposition:** `CONDITIONAL / NOT PULLED FORWARD YET`.

Reason: this cluster needs no new template/content lifecycle rule. Later locale/render/template-provenance scenarios may change the result.

## Audit & Evidence

**Disposition:** `CONDITIONAL / NOT PULLED FORWARD YET`.

Reason: Communications can own delivery attempts/provider evidence without creating Audit authority. Later security-event retention/operator-retry scenarios may expose a need for exact Audit-owned semantics.

This adjudication is provisional until the full Communications Pre-JIT stabilisation review.

---

# 13. Later executable proof-obligation register — v0.1.0

The following are later proof obligations only; this document does not execute or classify Phase 8 proof.

1. Fail each source-to-intent/protected-capability establishment step and prove no committed must-not-lose Identity issuance is orphaned.
2. Crash after durable commit before ordinary worker execution and prove recovery without losing or multiplying the logical intent.
3. Execute duplicate equivalent jobs across nodes and prove one lawful provider-submission path per attempt authorisation.
4. Kill execution immediately before/after provider invocation and before result persistence; prove ambiguous outcome remains unresolved rather than blindly retried.
5. Simulate provider acceptance with lost response; prove no fabricated success and no unsafe fresh send.
6. Reconcile delayed provider acceptance/delivery/failure evidence after restart.
7. Replay duplicate and reordered callbacks; prove convergence and no regression of source business truth.
8. Prove bounded retry/terminal-visible failure for definitive retryable and non-retryable provider failures.
9. Prove Oban duplicate-job/uniqueness failure does not violate business idempotency.
10. Prove no bearer material/secret-bearing URL leaks into job arguments, logs, telemetry, Audit, Analytics or ordinary operational projections.

---

# 14. Completeness / stabilisation assessment — v0.1.0

**NOT STABLE FOR GOVERNED DOSSIER DRAFTING YET.**

The first cluster is internally coherent and has not exposed an upstream contradiction, but substantial materially distinct scenario classes remain, including:

- proof expiry, consumption, revocation and supersession racing retry;
- primary-email-change cancellation/supersession and old-address notice semantics;
- participant resend and deduplication identity;
- multiple simultaneously valid challenges for one purpose;
- destination change after intent creation and canonical-email versus snapshotted-destination semantics;
- account closure/deletion and duplicate-account merge while delivery remains outstanding;
- accountless contacts and marketing-purpose/preference ownership;
- mandatory security/transactional messages versus optional preferences, quiet hours and frequency caps;
- channel selection, email-first/in-app-first and whether any FP-001 in-app Resource is actually required;
- locale selection, template version ownership, render/send provenance and Content & Media boundary;
- sensitive-data minimisation and provider-metadata limits;
- Audit & Evidence and Analytics boundaries;
- observability, operator retry/reconciliation and terminal-failure recovery UX;
- delivery-attempt/provider-evidence retention and deletion implications;
- provider outage, backlog recovery, throttling, retry storms and bounded retry;
- batch/fan-out pressure without importing campaign architecture;
- abuse, enumeration and resend flooding;
- final provider-independent `OQ-036` boundary and later proof-stage obligations.

The Pre-JIT stream therefore continues. No final Communications JIT Domain Dossier should be drafted from v0.1.0 alone.

---

# 15. v0.2.0 semantic delta — source-authority races, resend and destination binding

This successor preserves every accepted v0.1.0 finding and adds the second substantive Communications pressure-test cluster.

The live repository was rechecked before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

The second cluster pressure-tests:

- retry racing proof expiry;
- retry racing proof consumption;
- retry racing revocation/supersession;
- dispatch authorisation racing source invalidation;
- participant-requested resend versus infrastructure retry;
- duplicate/concurrent resend;
- multiple valid challenges for the same broad purpose;
- canonical account email versus the delivery destination captured for a particular communication obligation;
- stale verification delivery after an email/address transition;
- primary-email-change cancellation and supersession;
- new-address confirmation versus old-address security notice;
- provider hard bounce / invalid-recipient evidence;
- resend after the underlying source obligation is already complete;
- resend flooding and public enumeration;
- whether any of these cases justify `SubscriberContact`, `NotificationPreference`, `CommunicationJourney` or `InAppNotification`.

The governing source facts used in this cluster include:

- Product Law requires expiring single-use recovery links, the ordered primary-email-change flow, layered abuse protection, mandatory security/transactional notices where necessary, durable notification intent, bounded retry and no duplicate message after retry;
- Architecture requires single-purpose bounded replay-controlled security capabilities, non-enumerating public recovery behaviour, current-authority revalidation for durable consequences and provider ambiguity handling;
- current Identity dossier v0.1.3 defines verification challenge states `issued / valid / consumed / expired / superseded / revoked`, makes verification resend supersede the prior active challenge for the same Account/purpose and create one durable communication intent, and defines primary-email-change operation cancellation/supersession separately from delivery;
- Identity remains owner of canonical Account email and source challenge validity;
- Communications remains owner of the logical message obligation, delivery attempts and provider evidence.

No provider is selected and no `OQ-036` item is resolved here.

---

# 16. Accepted working-design register additions — v0.2.0

## COMM-WD-013 — MessageIntent identity is anchored to the source logical obligation, not merely Account + purpose

**Status:** `WORKING_DESIGN_ACCEPTED`

The minimum semantic identity of an FP-001 `MessageIntent` includes:

1. the authoritative source Domain;
2. the source logical operation/challenge identity or equivalent durable causal identity; and
3. the communication role within that operation.

An Account id plus broad purpose such as `verification` or `email_change` is insufficient. Two different authorised source challenges must not be collapsed merely because they concern the same Account and purpose.

Exact database key/constraint representation remains JIT detail.

This refines `COMM-WD-001`.

## COMM-WD-014 — Participant resend is source re-issuance when Identity creates a new challenge; infrastructure retry is not resend

**Status:** `UPSTREAM_DERIVED` for FP-001 email verification, with general Communications specialisation

For email verification, current Identity authority states that an allowed resend:

```text
supersedes prior active challenge for the same Account/purpose
→ creates a new authorised challenge
→ creates one durable communication intent
```

Therefore:

- repeated execution of the same handoff/source issuance → same `MessageIntent`;
- infrastructure/provider retry → same `MessageIntent`;
- a participant resend that Identity accepts by issuing a new challenge → a new `MessageIntent`;
- the previous intent becomes source-invalid for future dispatch once its challenge is superseded.

Communications does not decide whether a participant action deserves new proof issuance. That remains Identity authority.

For reset/recovery purposes where Identity may use different issuance semantics, Communications follows the source-owned operation identity rather than imposing verification semantics globally.

## COMM-WD-015 — Source validity and delivery resolution are orthogonal MessageIntent dimensions

**Status:** `WORKING_DESIGN_ACCEPTED`

A single flattened state such as `sent`, `cancelled` or `delivered` cannot truthfully represent both:

- whether the source proof/operation still authorises a **new** dispatch; and
- what happened to an already-authorised provider submission.

The conceptual dimensions are therefore separate.

### Source-authorisation dimension

```text
VALID_FOR_NEW_DISPATCH
→ INVALID_FOR_NEW_DISPATCH
```

Invalidation reasons include, as applicable:

- proof consumed;
- expired;
- revoked;
- superseded;
- owning operation cancelled/rejected/terminal;
- source operation otherwise no longer authorises delivery.

### Delivery-obligation dimension

```text
UNRESOLVED
→ SATISFIED
→ terminal

UNRESOLVED
→ TERMINAL_FAILURE
→ terminal

UNRESOLVED
→ CANCELLED_BY_SOURCE
→ terminal
```

`RECONCILIATION_REQUIRED` is a non-terminal unresolved condition rather than fabricated success/failure.

A source can become invalid after a message was already accepted or delivered. That does not rewrite historical provider evidence. Likewise, provider delivery never restores source validity.

Exact enums remain JIT detail.

## COMM-WD-016 — Durable dispatch authorisation is the concurrency cutover against source invalidation

**Status:** `WORKING_DESIGN_ACCEPTED`

A new provider submission requires a durable authorisation/claim that is decided against current Identity source validity in a concurrency-safe boundary.

Required ordering semantics:

```text
source invalidation wins first
→ new dispatch authorisation is rejected

dispatch authorisation wins first
→ that one already-authorised attempt may continue
→ later source invalidation prevents every further attempt/retry
→ underlying proof remains invalid after invalidation
```

The exact same-database transaction/row-version/locking/interface mechanism is deferred. The semantic requirement is that source validity and the creation/authorisation of the new attempt cannot be decided from an unprotected stale read.

Provider network I/O still occurs outside the authoritative transaction/lock.

This avoids an impossible requirement to “unsend” a message already lawfully placed in flight.

## COMM-WD-017 — In-flight stale delivery is evidence, not renewed authority

**Status:** `WORKING_DESIGN_ACCEPTED`

If a `DeliveryAttempt` was lawfully dispatch-authorised before source invalidation and the provider later accepts/delivers it after expiry, consumption, revocation, supersession or cancellation:

- the provider evidence is retained against that historical attempt;
- the source proof remains invalid;
- no new retry/attempt is authorised;
- the protected capability is cleared/rendered irrecoverable as required;
- the late-delivered link cannot revive or recreate Identity authority.

The participant may therefore receive a physically late stale link under an unavoidable external race, but the link must fail safely at the Identity boundary.

## COMM-WD-018 — A security MessageIntent carries an immutable delivery-destination snapshot/provenance for that obligation

**Status:** `WORKING_DESIGN_ACCEPTED`

FP-001 security delivery cannot resolve “whatever the Account email is now” at worker execution time.

The authorised source operation supplies the destination applicable to the particular communication obligation. Communications retains the minimum durable destination snapshot/provenance needed to execute/retry that intent safely.

Examples:

- account-verification message → email address bound to that verification issuance;
- new-address primary-email-change confirmation → candidate **new** email;
- old-address primary-email-change notice → prior/current **old** email applicable to that security event.

The snapshot is delivery data, not canonical Account-email authority.

Exact field/encryption/retention representation remains JIT/privacy detail.

## COMM-WD-019 — Destination snapshot does not justify SubscriberContact for FP-001

**Status:** `WORKING_DESIGN_ACCEPTED`

A snapshotted Account-owned email destination inside a specific security `MessageIntent` does not create accountless subscriber/contact authority.

`SubscriberContact` remains unjustified for FP-001 unless a later scenario introduces independently durable contact truth not reducible to an Account-owned source destination.

Communications may retain delivery provenance without becoming owner of canonical Account email.

## COMM-WD-020 — Communications must not deduplicate distinct source challenges by recipient or purpose

**Status:** `WORKING_DESIGN_ACCEPTED`

If the source Domain lawfully permits more than one simultaneously valid challenge/operation, each distinct source obligation may require its own `MessageIntent`.

Communications must not collapse them merely because they share:

- Account;
- destination;
- purpose family;
- template;
- channel.

For current email verification, Identity already supplies a stronger rule: resend supersedes the previous active challenge, so only the current challenge remains source-valid for new delivery.

The generic Communications contract therefore follows source identity rather than inventing a universal one-active-challenge rule.

## COMM-WD-021 — New-address confirmation and old-address notice are distinct logical message obligations

**Status:** `UPSTREAM_DERIVED`

A primary-email-change operation has at least two materially distinct communications when applicable:

1. **new-address confirmation** — challenge-bearing, targets the candidate new address and exists to permit Identity proof of control;
2. **old-address security notice** — non-proof security consequence, targets the old address and informs the prior address holder of the security event.

They must not share one `MessageIntent`, one destination or one satisfaction state merely because they originate from the same email-change operation.

The communication role is therefore a necessary component of logical intent identity.

## COMM-WD-022 — Cancellation/supersession stops new delivery of obsolete challenge-bearing messages

**Status:** `UPSTREAM_DERIVED`

When Identity cancels, expires, revokes or supersedes the underlying verification/recovery/new-address challenge:

- the associated challenge-bearing `MessageIntent` becomes invalid for new dispatch;
- pending retries are ended;
- no provider evidence may reactivate it;
- any already-authorised in-flight attempt may complete physically under `COMM-WD-016/017`, but its proof is unusable.

Communications never “reopens” the old intent. A later new challenge produces a new logical intent.

## COMM-WD-023 — An already-established old-address security notice is not made false by later cancellation of the email-change operation

**Status:** `WORKING_DESIGN_ACCEPTED`

The old-address notice is evidence of an actual security-relevant change attempt/confirmation event, not proof that the canonical email ultimately changed.

If the notice obligation was lawfully established and the email-change operation is later cancelled or superseded, that later Identity transition does not retroactively erase the historical notification obligation or its delivery evidence.

The content/template must therefore avoid falsely claiming an unapplied final Account state.

Current Product/Identity authority does **not** require this Pre-JIT stream to invent a separate “cancellation notice”. A later Product requirement could add one, but FP-001 must not manufacture it speculatively.

## COMM-WD-024 — Provider bounce or invalid-recipient evidence never mutates canonical Account email

**Status:** `UPSTREAM_DERIVED`

A provider hard bounce, rejection or invalid-recipient result is Communications-owned delivery evidence.

It may:

- close or fail a `DeliveryAttempt`;
- contribute to terminal-visible delivery failure;
- inform operator/participant recovery UX through safe owner interfaces.

It may not by itself:

- clear or replace the Account email;
- mark it unverified;
- apply or cancel a primary-email change;
- prove that a person no longer controls the address.

Any Identity transition requires Identity-owned authority.

## COMM-WD-025 — Security/transactional preferences do not create an FP-001 NotificationPreference requirement

**Status:** `WORKING_DESIGN_ACCEPTED`

The FP-001 challenge-bearing verification/reset/recovery/email-change messages and required security notices are not optional marketing subscriptions.

Current Product Law already preserves essential security/transactional messages where necessary. Therefore a durable `NotificationPreference` Resource is not required merely to decide whether these messages can be sent.

Important distinction:

- optional preferences cannot suppress an upstream-required security consequence;
- exact urgency and whether a particular non-urgent security notice may be *scheduled* around quiet hours is not frozen by this conclusion;
- abuse/rate protection is separate from participant communication preference.

`NotificationPreference` remains outside the current FP-001 resource set.

## COMM-WD-026 — Resend abuse authority remains at the Identity/security boundary; Communications enforces delivery safety, not Account existence

**Status:** `UPSTREAM_DERIVED`

Public verification/reset/recovery/email-change requests remain non-enumerating and subject to layered cross-node abuse controls owned by the current Identity/security boundary and `OQ-035`.

Communications:

- executes only source-authorised durable intents;
- may enforce provider-safe throughput/retry/backlog constraints;
- does not expose provider acceptance, bounce, destination existence or intent creation as a public Account-existence oracle;
- does not create its own competing Account-abuse authority.

Provider throttling protects the delivery dependency. It does not replace the source Domain's request-abuse policy.

## COMM-WD-027 — Source-provided destination normalisation/identity wins over provider formatting

**Status:** `WORKING_DESIGN_ACCEPTED`

Communications must not create an independent canonical-email identity by renormalising addresses into business authority.

The source Domain supplies the authorised destination identity/snapshot. The provider adapter may perform provider-required transport encoding/canonicalisation, but provider formatting does not rewrite the Account destination or MessageIntent business identity.

Exact normalisation rules remain with the owning source/identity contract.

---

# 17. Lifecycle refinement — v0.2.0

## 17.1 MessageIntent lifecycle

The v0.1.0 single conceptual lifecycle is refined because source validity and delivery evidence are independent.

### Dimension A — source dispatch authority

```text
VALID_FOR_NEW_DISPATCH
→ INVALID_FOR_NEW_DISPATCH
```

**Transition guards:**

`VALID_FOR_NEW_DISPATCH` requires the source Domain to confirm that the exact referenced challenge/operation still permits a new provider submission.

`INVALID_FOR_NEW_DISPATCH` is reached when the source proof/operation is consumed, expired, revoked, superseded, cancelled, rejected or otherwise no longer authorises delivery.

**Terminal behaviour:**

This dimension never returns to valid for the same source challenge/operation. Correction/reissue creates a new source obligation and therefore a new `MessageIntent`.

### Dimension B — delivery obligation resolution

```text
UNRESOLVED
├─→ SATISFIED
├─→ TERMINAL_FAILURE
└─→ CANCELLED_BY_SOURCE
```

`RECONCILIATION_REQUIRED` is an unresolved condition inside `UNRESOLVED`.

**Guards:**

- `SATISFIED` requires the later applicable channel/provider evidence policy; provider acceptance alone is not automatically enough.
- `TERMINAL_FAILURE` requires no remaining lawful bounded retry under current source authority and provider policy.
- `CANCELLED_BY_SOURCE` applies when the source becomes invalid before the delivery obligation has been satisfied and no already-authorised attempt still needs reconciliation.

**Side effects:**

A terminal delivery resolution ends future retry scheduling for that intent and triggers protected-capability cleanup where applicable.

**Invariant:**

Historical delivery/provider evidence is never rewritten merely because Dimension A later becomes invalid.

## 17.2 DeliveryAttempt lifecycle

The conceptual dispatch boundary is now:

```text
PREPARED
→ DISPATCH_AUTHORISED
→ SUBMISSION_STARTED
→ ACCEPTED | REJECTED | OUTCOME_UNKNOWN
```

Delivery evidence remains independent:

```text
NO_DELIVERY_EVIDENCE
→ DELIVERED_EVIDENCE
  | DELIVERY_FAILURE_EVIDENCE
  | DELIVERY_EVIDENCE_UNAVAILABLE
```

**Critical transition guard:**

`PREPARED → DISPATCH_AUTHORISED` must be serialized against current source validity as described by `COMM-WD-016`.

Once `DISPATCH_AUTHORISED` commits, source invalidation may prevent all later attempts but need not pretend that the already-authorised external operation can be atomically withdrawn.

## 17.3 Primary-email-change communication lifecycle projection

The source-owned Identity operation remains:

```text
requested
→ reauthenticated
→ new_address_pending
→ confirmed
→ delayed/reviewed
→ applied
```

with Identity-owned terminals including:

```text
cancelled | expired | rejected | superseded | held
```

Communications projects only the consequences:

```text
new-address confirmation MessageIntent
    ↳ bound to candidate-new-email snapshot
    ↳ invalidated for new dispatch if source challenge expires/revokes/supersedes/cancels/consumes

old-address security-notice MessageIntent
    ↳ bound to old-email snapshot
    ↳ represents the security event, not final Account apply truth
```

No Communications state can apply the email change.

---

# 18. Pressure-test register — second cluster

## COMM-PT-011 — Retry races proof expiry before dispatch authorisation

- **Scenario:** a retry worker wakes while the source proof expires.
- **Authority involved:** Identity proof lifecycle; Architecture current-precondition revalidation.
- **Durable truths and owner:** Identity owns expiry; Communications owns pending intent/attempt.
- **Concurrency/retry/reordering/crash behaviour:** expiry and attempt authorisation may occur concurrently on separate nodes.
- **Rejected models:** read validity once when intent was created; treat queued job as permanent send authority; let provider call proceed from stale worker memory.
- **Required invariant:** if expiry wins the serialized dispatch-authorisation boundary, no new provider submission is authorised.
- **Recommended JIT shape:** current source validity participates in the durable attempt-authorisation decision; expired intent closes as source-cancelled/unresolved-cleanup rather than retryable failure.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** deterministic expiry-versus-dispatch interleaving in both orderings; no post-expiry new attempt when expiry wins.
- **Verdict:** PASS.

## COMM-PT-012 — Proof expires after dispatch authorisation but before provider acceptance/delivery

- **Scenario:** an attempt is lawfully authorised, then proof expiry commits while provider I/O is in flight or provider delivery is delayed.
- **Authority involved:** Identity expiry; Architecture no provider I/O in authoritative lock; certified protected-delivery seam.
- **Durable truths and owner:** provider attempt history remains Communications evidence; proof becomes invalid in Identity.
- **Concurrency/retry/reordering/crash behaviour:** physical message may arrive after proof expiry.
- **Rejected models:** keep proof valid merely because an email is in flight; roll back expiry; delete attempt evidence; retry again after expiry.
- **Required invariant:** expiry prevents every later attempt and the stale bearer link cannot be consumed even if the already-authorised message arrives.
- **Recommended JIT shape:** dispatch-authorisation commit is the cutover; late evidence is recorded historically; no new retry.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** authorise attempt, then expire source before provider completion; prove stale proof rejected and no subsequent attempt scheduled.
- **Verdict:** PASS.

## COMM-PT-013 — Retry races proof consumption

- **Scenario:** participant consumes a verification/reset/recovery/email-change proof while a retry worker is about to send it again.
- **Authority involved:** Identity consumption authority; certified rule that consumption ends remaining retry obligation.
- **Durable truths and owner:** Identity owns consumption; Communications owns attempt authorisation/evidence.
- **Concurrency/retry/reordering/crash behaviour:** consumption and dispatch authorisation race across nodes.
- **Rejected models:** always resend because job exists; consumption merely changes UI; Communications marks proof consumed from provider evidence.
- **Required invariant:** consumption winning first blocks new dispatch; dispatch winning first may complete only that authorised attempt, after which no further retry exists.
- **Recommended JIT shape:** same serialized cutover as `COMM-WD-016`.
- **Conclusion:** `UPSTREAM_DERIVED` plus working concurrency specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** controlled both-order interleavings and a provider-delay case.
- **Verdict:** PASS.

## COMM-PT-014 — Retry races revocation or supersession

- **Scenario:** security action or newer challenge revokes/supersedes the current source while a delivery retry is pending.
- **Authority involved:** Identity challenge states; primary-email-change/verification supersession rules.
- **Durable truths and owner:** Identity owns revocation/supersession; Communications owns historical intent/attempts.
- **Concurrency/retry/reordering/crash behaviour:** old and new intent jobs may both exist.
- **Rejected models:** queue order decides which proof is current; old provider delivery reactivates old challenge; delete prior intent history.
- **Required invariant:** only source-current challenge can authorise a new attempt; historical attempts remain evidence.
- **Recommended JIT shape:** old intent becomes invalid for dispatch; new source challenge has a distinct MessageIntent.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** old/new jobs reordered across nodes; only current challenge can receive new dispatch authorisation.
- **Verdict:** PASS.

## COMM-PT-015 — Participant requests verification resend before the original intent executes

- **Scenario:** original verification email is still queued; participant asks for resend.
- **Authority involved:** Identity F.2 resend semantics; abuse boundary.
- **Durable truths and owner:** Identity atomically supersedes prior active challenge and creates a new challenge/intent.
- **Concurrency/retry/reordering/crash behaviour:** old and new jobs may execute in reverse order.
- **Rejected models:** same MessageIntent with replaced token; mutate old intent to point at new challenge; allow stale queued job to send without revalidation.
- **Required invariant:** old intent cannot gain a new dispatch after supersession; new intent carries the new proof.
- **Recommended JIT shape:** new source challenge → new MessageIntent; stale job self-suppresses on current-validity check.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** enqueue old, create resend/new challenge, execute old job after new; old cannot newly dispatch.
- **Verdict:** PASS.

## COMM-PT-016 — Two concurrent/duplicate participant resend submissions

- **Scenario:** double-click, two tabs or two nodes submit resend nearly simultaneously.
- **Authority involved:** Identity one-active-challenge verification rule; OQ-035 abuse controls; Communications source-identity contract.
- **Durable truths and owner:** Identity decides resulting challenge sequence; Communications mirrors only committed source obligations.
- **Concurrency/retry/reordering/crash behaviour:** one or two valid source issuances may transiently be attempted depending on Identity serialization; earlier challenge becomes superseded.
- **Rejected models:** Communications guesses duplicates from recipient/time window; provider dedupe is treated as challenge correctness.
- **Required invariant:** Communications never has two source-current verification intents after Identity serialization; any older intent cannot newly dispatch after supersession.
- **Recommended JIT shape:** rely on Identity operation/version semantics; Communications dedupes duplicate handoff for the exact same committed source issuance only.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** simultaneous resend requests plus reordered job execution; at most the source-current challenge can obtain a post-race new dispatch.
- **Verdict:** PASS.

## COMM-PT-017 — Multiple valid challenges for the same broad purpose are allowed by a source flow

- **Scenario:** a future/source-specific Identity flow legitimately allows multiple distinct live challenges under one broad purpose family.
- **Authority involved:** Identity source authority; Communications deduplication ownership.
- **Durable truths and owner:** source owns challenge validity; Communications owns one logical intent per authorised source obligation.
- **Concurrency/retry/reordering/crash behaviour:** multiple jobs/attempts can coexist without being duplicates.
- **Rejected models:** universal uniqueness on `(account, purpose)`; collapse to latest merely because destination matches.
- **Required invariant:** Communications cannot destroy a legitimately distinct source obligation by over-broad dedupe.
- **Recommended JIT shape:** idempotency identity includes source challenge/operation identity + message role.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** two distinct source identities sharing Account/purpose/destination remain independently traceable; duplicate handoff of either still converges.
- **Verdict:** PASS.

## COMM-PT-018 — Canonical Account email changes after intent creation but before worker execution

- **Scenario:** an intent was created for address A; Account canonical email later becomes B before provider dispatch.
- **Authority involved:** Identity canonical email ownership; Communications delivery provenance.
- **Durable truths and owner:** Identity owns current canonical email; Communications owns destination snapshot for the already-created message.
- **Concurrency/retry/reordering/crash behaviour:** worker may execute after the Account change.
- **Rejected models:** query current Account email at send time and silently reroute the old message to B; treat destination snapshot as new canonical authority.
- **Required invariant:** delivery uses the source-authorised destination bound to that message, subject to source validity; it cannot silently retarget.
- **Recommended JIT shape:** immutable/minimised destination snapshot on intent; source validity decides whether it may still be sent.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** address transition between intent establishment and dispatch; no unintended retargeting.
- **Verdict:** PASS.

## COMM-PT-019 — Stale account-verification message after an email-change operation

- **Scenario:** verification for address A exists, then Identity lawfully changes/supersedes the email path.
- **Authority involved:** Identity verification/email-change authority.
- **Durable truths and owner:** old verification challenge becomes invalid under source rules; Communications retains historical attempt evidence.
- **Concurrency/retry/reordering/crash behaviour:** old verification job may run late.
- **Rejected models:** current-email lookup reroutes old challenge; provider delivery marks B verified; old intent rewritten to new proof.
- **Required invariant:** the old proof cannot verify the new canonical email and cannot receive a new dispatch once invalidated.
- **Recommended JIT shape:** source-bound challenge + destination snapshot; new email verification/confirmation creates its own source obligation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** old verification intent/job after email transition; stale link fails and no new dispatch is authorised.
- **Verdict:** PASS.

## COMM-PT-020 — Primary-email-change new-address confirmation is cancelled before delivery

- **Scenario:** new-address confirmation intent exists, then the owning email-change operation is cancelled before provider dispatch.
- **Authority involved:** Identity email-change lifecycle.
- **Durable truths and owner:** Identity owns cancellation; Communications owns unresolved delivery history.
- **Concurrency/retry/reordering/crash behaviour:** cancellation races dispatch.
- **Rejected models:** Communications independently decides cancellation; queued job remains permanent authority; cancel deletes intent history.
- **Required invariant:** cancellation winning the dispatch-authorisation race blocks new delivery; already-authorised attempt may finish but link cannot confirm/apply the cancelled change.
- **Recommended JIT shape:** source invalidation closes future dispatch and triggers protected-capability cleanup.
- **Conclusion:** `UPSTREAM_DERIVED` plus concurrency specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** both cancellation/dispatch orderings; stale link rejected.
- **Verdict:** PASS.

## COMM-PT-021 — A second primary-email-change request supersedes the first

- **Scenario:** operation A targets new address A2; later accepted operation B targets B2 while A remains pending.
- **Authority involved:** Identity newest-explicit-operation/supersession authority.
- **Durable truths and owner:** each operation/challenge is Identity-owned; each confirmation communication is separately Communications-owned.
- **Concurrency/retry/reordering/crash behaviour:** jobs for A and B may execute in either order.
- **Rejected models:** one mutable email-change MessageIntent whose destination/token is replaced; Account+purpose dedupe that destroys B or keeps A current.
- **Required invariant:** A cannot obtain new dispatch after supersession; B is independent; historical evidence for A remains.
- **Recommended JIT shape:** distinct MessageIntent per source operation/challenge + role.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** reordered A/B execution, callback evidence and restart.
- **Verdict:** PASS.

## COMM-PT-022 — Old-address security notice during primary-email change

- **Scenario:** the source reaches the Product-required point at which the old address must be notified.
- **Authority involved:** Product §21J.8; Identity F.7; Communications ownership.
- **Durable truths and owner:** Identity owns email-change operation/final apply; Communications owns old-address notice intent/delivery evidence.
- **Concurrency/retry/reordering/crash behaviour:** notice delivery may fail, retry or be delayed while Identity later changes state.
- **Rejected models:** send to whatever email is canonical when worker runs; treat old-address notice as proof; merge with new-address confirmation intent; suppress via optional marketing preference.
- **Required invariant:** the notice uses the old-address snapshot and cannot establish or reverse email-change truth.
- **Recommended JIT shape:** separate mandatory-security MessageIntent role bound to the old-address snapshot and source email-change operation.
- **Conclusion:** `UPSTREAM_DERIVED` for the separate consequence/destination; exact channel-satisfaction/urgency remains open.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** canonical email changes before worker execution; notice still addresses correct old destination; provider failure does not mutate Identity.
- **Verdict:** PASS WITH OQ-036 SCHEDULING EDGE OPEN.

## COMM-PT-023 — Email-change operation is cancelled/superseded after old-address notice intent already exists

- **Scenario:** old-address notice was lawfully established; later the email-change operation is cancelled or superseded.
- **Authority involved:** Product security-notice purpose; Identity operation history.
- **Durable truths and owner:** Identity retains event/cancellation truth; Communications retains notice/delivery history.
- **Concurrency/retry/reordering/crash behaviour:** notice may execute after cancellation.
- **Rejected models:** automatically erase/cancel historical security notice because final change did not apply; rewrite notice as proof of final Account state.
- **Required invariant:** a notice about the security event can remain lawful without implying that final change succeeded.
- **Recommended JIT shape:** event-scoped old-address intent; template/content semantics must describe the event truthfully.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO current amendment required.
- **Conditional dossier pulled forward:** NO; Content & Media becomes necessary only if exact template semantics cannot be specified from existing content authority.
- **Later executable proof:** cancellation after notice establishment; message provenance remains event-correct and no Identity mutation occurs.
- **Verdict:** PASS.

## COMM-PT-024 — Provider hard-bounces the new-address confirmation

- **Scenario:** provider definitively reports that the candidate new address cannot receive the challenge.
- **Authority involved:** Communications provider evidence; Identity email-change authority.
- **Durable truths and owner:** bounce belongs to DeliveryAttempt evidence; email-change remains Identity-owned pending/expiry/cancel/reissue according to its lifecycle.
- **Concurrency/retry/reordering/crash behaviour:** repeated/late bounce evidence may arrive after source cancellation or reissue.
- **Rejected models:** bounce automatically cancels/applies email change; provider says invalid therefore Account canonical email is changed; create SubscriberContact as canonical destination truth.
- **Required invariant:** provider evidence cannot mutate Identity; terminal delivery failure is visible and participant recovery stays source-controlled.
- **Recommended JIT shape:** normalized delivery failure evidence + terminal/unresolved intent semantics; safe participant path is owned through Identity.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** hard bounce before/after source cancellation, duplicated callback, safe frontend status without enumeration.
- **Verdict:** PASS.

## COMM-PT-025 — Provider hard-bounces the old-address security notice

- **Scenario:** the old address no longer accepts mail.
- **Authority involved:** Product old-address-notice consequence; Communications terminal failure; Identity final email authority.
- **Durable truths and owner:** delivery failure remains Communications truth; Identity operation remains independent.
- **Concurrency/retry/reordering/crash behaviour:** bounded retry may exhaust while email-change lifecycle continues.
- **Rejected models:** rollback/deny Identity truth solely because provider cannot deliver old-address notice; mark notice delivered; silently discard failure.
- **Required invariant:** failure is terminal-visible and does not fabricate source truth.
- **Recommended JIT shape:** normal mandatory-message terminal-failure visibility/operator recovery path; exact release/operational escalation belongs later.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`, consistent with certified Identity consequence separation.
- **Upstream amendment:** NO presently identified.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** terminal bounce/exhaustion remains discoverable; no Identity mutation.
- **Verdict:** PASS.

## COMM-PT-026 — Participant requests resend after the source obligation is already complete

- **Scenario:** verified Account asks to resend verification, or completed/consumed proof is targeted again.
- **Authority involved:** Identity source validity and non-enumerating action boundary.
- **Durable truths and owner:** source decides whether there is a new lawful issuance; Communications cannot revive old intent.
- **Concurrency/retry/reordering/crash behaviour:** stale UI may submit after completion.
- **Rejected models:** Communications requeues prior intent because user asked; reopen consumed proof; expose “already verified” in a way that violates source non-enumeration policy where applicable.
- **Required invariant:** no new Communications obligation exists without a new source-authorised issuance.
- **Recommended JIT shape:** public action routes through Identity; Communications receives only committed new source obligations.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale/double submission after completion creates no unauthorized provider send.
- **Verdict:** PASS.

## COMM-PT-027 — Resend flooding / enumeration attempt

- **Scenario:** attacker repeatedly requests verification/reset/recovery messages for known or guessed addresses.
- **Authority involved:** Product §21J.13, Architecture §6.4, `OQ-035`; Communications provider/backlog safety.
- **Durable truths and owner:** Identity/security owns request eligibility and abuse state; Communications owns only authorised delivery intents/provider execution.
- **Concurrency/retry/reordering/crash behaviour:** requests arrive cross-node and can create provider pressure/backlog.
- **Rejected models:** provider rate limit as Account-abuse authority; PostgreSQL MessageIntent counts as the only immediate high-velocity guard; public response varies based on provider/account existence.
- **Required invariant:** public behaviour remains non-enumerating; source abuse controls are cross-node; provider throttling cannot weaken source authority; stale superseded intents are suppressed before new dispatch.
- **Recommended JIT shape:** source-side distributed abuse boundary + Communications provider-safe bounded throughput/backoff; no new NotificationPreference Resource.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** burst across nodes, non-enumerating responses, superseded-intent suppression, provider throttle/backlog recovery.
- **Verdict:** PASS; exact thresholds remain `OQ-035`.

---

# 19. Rejected-model register additions — v0.2.0

11. **Deduplicate security messages by `(Account, purpose)` alone.** Rejected: distinct source operations/challenges can exist; email-change has multiple message roles.
12. **Participant resend is merely another provider retry of the same intent.** Rejected where Identity issues a new challenge.
13. **Mutate an existing MessageIntent to carry a newly issued challenge/token.** Rejected: corrupts provenance and stale-message reasoning.
14. **Resolve canonical Account email at worker-send time for every security message.** Rejected: silently retargets source-bound messages and breaks old/new-address semantics.
15. **Treat a destination snapshot as Communications-owned canonical contact truth.** Rejected: Identity remains canonical Account-email owner.
16. **Communications decides proof expiry/revocation/supersession.** Rejected: source authority belongs to Identity.
17. **Provider bounce mutates Account email or verification truth.** Rejected.
18. **Source invalidation deletes historical provider-attempt evidence.** Rejected: invalidation and delivery evidence are independent histories.
19. **Hold Identity/database locks open across provider network I/O to guarantee “no stale email ever arrives”.** Rejected by Architecture; the safe cutover is durable dispatch authorisation plus invalid proof at use.
20. **Optional preferences suppress required FP-001 security/transactional notices.** Rejected by Product boundary.
21. **Create `SubscriberContact` merely to persist the Account email used by a security intent.** Rejected at FP-001 scope.
22. **Create `NotificationPreference` merely to express “mandatory security messages bypass optional opt-out”.** Rejected; existing Product law already defines the rule.
23. **Automatically manufacture a separate cancellation/supersession notification for every email-change reversal.** Rejected as speculative Product scope; no current authority requires it.

---

# 20. Upstream-delta register — v0.2.0

**NO REQUIRED UPSTREAM AMENDMENT IDENTIFIED IN THIS CLUSTER.**

The second-cluster scenarios are currently resolvable beneath existing Product, Architecture, Domain and certified Identity authority.

One seam remains deliberately unresolved rather than silently decided:

- exact provider/channel evidence required for a message to count as `SATISFIED`;
- exact urgency/quiet-hour scheduling treatment of each security-notice subtype.

Those remain within `OQ-036` / later provider-channel policy unless future governed drafting proves that Product-level semantics, rather than provider policy, are missing.

No Product amendment is justified merely because provider delivery cannot be made physically retractable after a lawfully authorised external call has begun. Correctness is preserved by Identity proof invalidation and by preventing all *new* attempts after source invalidation.

---

# 21. Unresolved-gate register additions — v0.2.0

| Gate / open matter | v0.2.0 effect |
|---|---|
| `OQ-035` abuse-control thresholds | Exact resend/reset/recovery thresholds, escalation and false-positive recovery remain release/proof policy. Architecture already requires cross-node controls and non-enumeration. |
| `OQ-036` provider/channel policy | Exact channel evidence, provider idempotency/reconciliation API, retry classes/backoff, bounce semantics mapping and security-message urgency scheduling remain open. |
| MessageIntent exact DB idempotency constraint | Semantic identity is now narrowed to source obligation + communication role, but exact key/schema/index form remains JIT. |
| Destination storage protection/retention | A durable destination snapshot is required for FP-001 security intents; exact encryption/retention/deletion treatment remains later privacy/JIT detail. This has not yet justified the Privacy dossier. |
| Quiet hours for mandatory but non-emergency security notices | Optional preference cannot suppress them; exact delay/urgency policy is not frozen here. |
| Satisfaction criterion | Still `OPEN_HYPOTHESIS`; accepted provider submission is not automatically delivery. |

---

# 22. Cross-stream dependency register additions — v0.2.0

| Stream / Domain | v0.2.0 finding |
|---|---|
| Identity & Access | Stronger dependency boundary now explicit: source challenge/operation identity, validity and authorised destination role are inputs to Communications. Identity remains sole proof/email authority. |
| Privacy & Consent | Destination snapshots are personal data and later deletion/retention treatment must be lawful, but no new Privacy-owned lifecycle is needed to specify FP-001 dispatch semantics yet. Conditional dossier remains unpulled. |
| Content & Media | Old-address notice must describe the security event without falsely claiming final apply. Current governed template/version authority appears sufficient; no new C&M lifecycle semantic is yet required. |
| Audit & Evidence | Identity already owns/audits email-change requested/applied/cancelled/superseded history; Communications owns message/provider evidence. No extra Audit-owned contract is yet required. |
| Analytics | Must not infer Account-email validity or security outcome from bounce/delivery. Still consumer-only. |
| Abuse/security | `OQ-035` governs exact thresholds; Communications provider throttling is dependency protection rather than Account-abuse authority. |

---

# 23. Conditional-dossier adjudication — provisional v0.2.0

## Privacy & Consent

**Disposition:** `CONDITIONAL / NOT PULLED FORWARD`.

The second cluster proves that FP-001 needs a durable, minimised destination snapshot for source-bound security delivery. That creates a privacy obligation but not yet an unresolved Privacy-owned business semantic.

Existing authority is enough to state:

- Identity remains canonical email owner;
- Communications retains minimum delivery data for its own obligation;
- sensitive/personal data is minimised;
- full deletion/retention is owned by Privacy & Consent.

A Privacy dossier should be pulled forward only if the later closure/deletion/retention pressure tests show that Phase 7C cannot specify what happens to outstanding intents/delivery evidence without inventing Privacy-owned policy.

## Content & Media

**Disposition:** `CONDITIONAL / NOT PULLED FORWARD`.

This cluster requires exact template/version provenance eventually, and old-address copy must not overstate final Account state. Existing Architecture/Domain content authority already supports immutable version/locale provenance.

No new Content lifecycle or approval rule has yet been required.

## Audit & Evidence

**Disposition:** `CONDITIONAL / NOT PULLED FORWARD`.

Identity already specifies audit of the source email-change/recovery transitions. Communications owns delivery attempt/provider evidence. This cluster does not require an Audit-owned Resource or new central evidence lifecycle.

Later operator-retry/retention/security-investigation scenarios remain capable of changing this adjudication.

---

# 24. Later executable proof-obligation register additions — v0.2.0

11. Deterministically race source expiry against dispatch authorisation in both orderings.
12. Deterministically race proof consumption against dispatch authorisation in both orderings.
13. Deterministically race revocation/supersession against dispatch authorisation, including two BEAM nodes.
14. Prove that an already-authorised in-flight attempt may reconcile after source invalidation without restoring proof validity or permitting another attempt.
15. Verification resend: prove new source challenge → new MessageIntent, old challenge/intent loses new-dispatch authority, and late old job cannot send after supersession.
16. Concurrent duplicate resend: prove source serialization and Communications handoff idempotency do not create two current verification messages for one committed current challenge.
17. Prove distinct source challenges are not incorrectly collapsed by recipient/purpose deduplication.
18. Change canonical email after intent establishment and prove the worker neither silently retargets nor treats the destination snapshot as Account authority.
19. Primary-email-change: prove new-address confirmation uses the candidate address and old-address notice uses the prior address, as separate intents.
20. Cancel/supersede email change before new-address dispatch and prove no new stale attempt is authorised.
21. Cancel/supersede after an old-address notice was established and prove historical notice evidence remains truthful without applying Identity state.
22. Hard bounce candidate-new-email confirmation and old-address notice separately; prove neither provider outcome mutates canonical Account email or verification truth.
23. Submit stale resend after verification/recovery completion and prove no old MessageIntent is revived.
24. Execute cross-node resend flooding under the later approved OQ-035 boundary; prove public response remains non-enumerating and provider/backlog controls do not become Account authority.
25. Prove destination/bearer minimisation: no protected bearer appears in durable destination fields, logs, telemetry, audit or provider metadata beyond the minimum provider request.

---

# 25. Resource-discipline review — cumulative through v0.2.0

## `MessageIntent`

**Still required.**

Durable truth now proven to include:

- logical source communication obligation;
- source causal/challenge/operation reference;
- communication role;
- source-bound delivery destination snapshot/provenance;
- business deduplication identity;
- durable resolution/reconciliation/terminal visibility;
- link to protected delivery machinery where applicable.

This is not reducible to an Oban job or provider attempt.

## `DeliveryAttempt`

**Still required.**

Distinct durable truth includes:

- dispatch authorisation;
- provider submission operation identity;
- accepted/rejected/unknown submission evidence;
- later delivery/bounce evidence;
- reconciliation state;
- retry relationship to the parent logical intent.

This cannot safely be collapsed into MessageIntent without losing provider ambiguity and repeated-attempt history.

## Protected delivery capability

**Still required as sensitive machinery where applicable; still not justified as independent business Resource.**

It exists only to reproduce the already-authorised challenge-bearing delivery and carries no Identity authority.

## `SubscriberContact`

**Still rejected for FP-001.**

A source-bound snapshot of an Account-owned email address is not independently durable subscriber-contact truth.

## `NotificationPreference`

**Still rejected for FP-001.**

Current FP-001 messages under pressure are mandatory/security/transactional source consequences. Optional preference semantics are not required to decide their existence. Exact scheduling/urgency does not justify a participant-preference Resource.

## `InAppNotification`

**Still rejected for FP-001.**

No scenario in either cluster requires durable in-app inbox truth, and current FES explicitly says the participant notification centre is not an FP-001 prerequisite.

## `CommunicationJourney`

**Still rejected for FP-001.**

Verification/recovery/email-change obligations remain source-event-specific messages, not a campaign/journey lifecycle.

## Additional source-validity / cancellation Resource

**Rejected.**

Identity already owns proof/operation validity. Communications projects the source reference and current dispatch authority; it must not create a second source-validity owner.

## DeliveryDestination / Address Resource

**Rejected at current scope.**

The destination is an attribute/provenance of the `MessageIntent`, not independently governed FP-001 business truth.

**Cumulative resource verdict through v0.2.0: the two durable Communications business concepts remain `MessageIntent` and `DeliveryAttempt`.**

---

# 26. Completeness / stabilisation assessment — v0.2.0

**NOT YET STABLE FOR GOVERNED COMMUNICATIONS JIT DOSSIER DRAFTING.**

The source-authority/resend/destination cluster is now internally coherent. It produced no required upstream amendment and did not justify another FP-001 Communications Resource.

Several major materially distinct scenario classes remain and must still be pressure-tested before stabilisation:

1. **Account lifecycle / data lifecycle**
   - Account closure while message delivery is outstanding;
   - final deletion while intents/attempt/provider evidence remain;
   - duplicate-account merge/reconciliation while messages are outstanding;
   - destination/provider evidence retention and deletion implications;
   - restoration/non-resurrection after backup restore.

2. **Preferences / consent / accountless contacts**
   - accountless subscriber contact;
   - marketing purpose permission versus Communications channel/category preference;
   - mandatory security versus optional messaging;
   - quiet hours and frequency caps;
   - whether any of these finally require the conditional Privacy dossier.

3. **Content / locale / rendering**
   - locale selection at intent creation versus render/send time;
   - template version ownership and exact-content provenance;
   - correction/withdrawal after intent creation;
   - whether mutable/render-late content can make retries semantically inconsistent;
   - whether FP-001 genuinely requires the Content & Media conditional dossier.

4. **Operations / provider outage / recovery**
   - long provider outage and backlog recovery;
   - retry storms, throttling and fair bounded recovery;
   - bounded retry versus indefinite retry;
   - terminal-failure participant/operator recovery;
   - operator retry/reconciliation controls;
   - cross-node reconciliation;
   - no secret leakage through operational tooling;
   - graceful degradation.

5. **Audit / observability / retention**
   - exact boundary between Communications provider evidence and central Audit/security evidence;
   - retention/disposition of delivery attempts and provider metadata;
   - operator incident reconstruction;
   - Analytics minimisation and no business-conversion inference;
   - whether the conditional Audit & Evidence dossier becomes necessary.

6. **Channel / fan-out / mature-capability exclusion**
   - email-first versus in-app-first implications;
   - prove in-app remains unnecessary for FP-001;
   - future SMS/WhatsApp extension without premature abstraction;
   - batch/fan-out pressure without importing campaign architecture;
   - exact `OQ-036` boundary.

The next semantic pass should therefore attack **Account lifecycle + Privacy/data-lifecycle interactions** first. That cluster is the most likely remaining place where the current two-Resource Communications design could require a conditional Privacy dossier or expose an upstream retention/deletion gap.

---

# 27. v0.3.0 semantic delta — Account lifecycle, deletion, merge, retention and restore

This successor preserves all accepted v0.1.0 and v0.2.0 findings and adds the third substantive Communications pressure-test cluster.

The live repository was rechecked immediately before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

This pass deliberately respects the current FP-001 scope boundary:

- ordinary Account/Identity lifecycle and Communications consequences are material to FP-001;
- the reusable full data-rights / retention / deletion orchestration capability is **not** introduced by FP-001 and remains a later capability under the governed Roadmap;
- nevertheless, Communications must already expose a lawful owner boundary so later deletion/restore orchestration cannot resurrect, resend or reconstruct deleted participant data.

The cluster pressure-tests:

- Account closure racing queued or in-flight communication;
- required recovery/security communication during recoverable closure;
- closure reactivation;
- full-deletion request and 14-day cancellation window;
- full-deletion execution racing outstanding delivery;
- protected delivery capability disposition;
- late provider callbacks after deletion;
- provider-side deletion ambiguity;
- retained delivery/provider evidence;
- legal holds;
- duplicate deletion orchestration;
- deletion racing new MessageIntent establishment;
- backup restore from a pre-deletion snapshot;
- restored Oban work/provider egress;
- duplicate-account reconciliation/merge with outstanding delivery;
- rejected/conflicted merge;
- post-deletion re-registration with the same contact;
- operator retry after closure/deletion/merge;
- whether these cases require a Privacy & Consent or Audit & Evidence conditional FP-001 dossier.

No provider is selected. No retention duration is invented. `OQ-029...OQ-032` remain open at their governed stages.

---

# 28. Accepted working-design register additions — v0.3.0

## COMM-WD-028 — Source dispatch disposition is three-way, not binary

**Status:** `WORKING_DESIGN_ACCEPTED`

`COMM-WD-015` is refined.

For Communications execution, current source/privacy authority must be capable of yielding three conceptual dispositions:

```text
ALLOW_NEW_DISPATCH
SUSPEND_NEW_DISPATCH
STOP_NEW_DISPATCH
```

Meaning:

- `ALLOW_NEW_DISPATCH` — a new provider attempt may be authorised if all other guards pass;
- `SUSPEND_NEW_DISPATCH` — do not create a new provider attempt now, but the same logical obligation is not necessarily terminal; later current-authority revalidation may permit continuation;
- `STOP_NEW_DISPATCH` — this source obligation is terminal for new dispatch and can never be reopened merely by Communications.

Examples of why `SUSPEND` is necessary include recoverable Account closure and deletion-pending windows where the source/privacy owner may temporarily prohibit processing without yet establishing an irreversible terminal source state.

Communications does not decide which disposition applies. The owning source/privacy contract does.

A previously `STOP`ped source obligation requires a new source obligation and therefore a new `MessageIntent`; it is never reopened.

## COMM-WD-029 — Account closure and full deletion are different Communications events

**Status:** `UPSTREAM_DERIVED`

Current Product and Architecture authority already require:

```text
account closure != full deletion
```

Therefore Communications must not apply deletion semantics merely because an Account enters `closed_recoverable`.

Recoverable closure:

- stops optional processing and communication;
- disables ordinary login;
- preserves eligible records during the 30-day recovery window;
- may still require source-authorised recovery/security communication.

Full deletion:

- is cross-system, durable and irreversible after completion;
- eventually removes/anonymises eligible identifiable Communications representations;
- prevents future account recovery/reconstruction.

No single `account_inactive` flag may collapse these behaviours.

## COMM-WD-030 — Recoverable closure suppresses optional delivery but does not create a blanket ban on required recovery/security communication

**Status:** `UPSTREAM_DERIVED`

Product Law explicitly says closure stops **optional** processing and communication.

Therefore a closed-recoverable Account does not automatically prohibit every Communications action.

The source owner must distinguish:

- obsolete/optional messages that are suspended or stopped;
- required recovery/security messages that remain authorised for the governed recovery path.

Communications may not infer “mandatory” merely from template/category naming; the source obligation must carry or expose the applicable authoritative delivery role.

This does not create a `NotificationPreference` Resource.

## COMM-WD-031 — Closure does not autonomously replay old communications after reactivation

**Status:** `WORKING_DESIGN_ACCEPTED`

If an Account is reopened during the allowed recovery window, Communications must re-evaluate the exact source obligation before resuming a suspended intent.

Possible outcomes:

- same source challenge/operation remains valid and the same unresolved `MessageIntent` may continue;
- source challenge expired/superseded/revoked while closed → intent stops;
- source owner issues a fresh challenge/operation → new `MessageIntent`.

Account reactivation by itself is not send authority.

## COMM-WD-032 — Full deletion uses an owner-mediated Communications deletion contract; Privacy does not shared-write Communications rows

**Status:** `UPSTREAM_DERIVED`

Architecture already requires every capability holding eligible identifiable representations to participate in full deletion through its own deletion contract.

For Communications, the conceptual owner contract must be able to:

1. prevent new participant-linked dispatch under current deletion/suppression authority;
2. end or suspend outstanding eligible `MessageIntent` obligations according to the current deletion phase;
3. make protected delivery capabilities irrecoverable when the owning source/deletion authority requires it;
4. delete or irreversibly anonymise eligible identifiable destination/content/provenance fields;
5. apply approved disposition to `DeliveryAttempt` and provider evidence;
6. issue/reconcile required external messaging-processor deletion requests;
7. report unresolved versus completed Communications deletion work to Privacy & Consent;
8. remain idempotent under duplicate/retried orchestration.

Privacy & Consent orchestrates and owns deletion completion. It does not directly mutate Communications persistence.

## COMM-WD-033 — Business lifecycle and data lifecycle remain orthogonal for MessageIntent and DeliveryAttempt

**Status:** `UPSTREAM_DERIVED`

A Communication record can be business-terminal yet still have a later data-lifecycle disposition.

Examples:

```text
MessageIntent SATISFIED
+ data lifecycle eligible_for_deletion

DeliveryAttempt REJECTED
+ retained_by_obligation

MessageIntent TERMINAL_FAILURE
+ legal_hold

provider evidence historical
+ irreversibly anonymised later
```

Do not encode business delivery state and privacy/retention state into one enum.

This preserves Architecture §11's separation of business lifecycle from data lifecycle.

## COMM-WD-034 — Protected delivery capability has no independent retention right

**Status:** `UPSTREAM_DERIVED`

Protected delivery material exists only to satisfy the bounded delivery obligation accepted in certified Identity v0.1.3.

It has no historical, audit, analytics or provider-evidence retention purpose.

Therefore:

- once the underlying delivery obligation no longer lawfully requires retry, it is cleared/rendered irrecoverable;
- completed full deletion cannot leave recoverable bearer material;
- a legal hold over historical delivery evidence does not automatically justify holding live bearer capability;
- restoring an older backup must not reactivate protected material for a deleted/suppressed participant.

During a reversible deletion-pending or recoverable-closure period, exact challenge/capability invalidation remains source-owned; Communications never extends capability lifetime beyond the underlying proof.

## COMM-WD-035 — Retention of delivery/provider evidence requires independent category authority

**Status:** `UPSTREAM_DERIVED`

`MessageIntent` and `DeliveryAttempt` existence does not itself grant indefinite retention.

Any retained delivery/provider evidence must be:

- covered by an approved record category/purpose;
- minimised;
- restricted from ordinary participant/product use;
- non-reconstructive where the Account has been fully deleted;
- disposed when the approved retention basis ends.

Provider preference, troubleshooting convenience or “we may need it someday” is not retention authority.

Exact periods remain `OQ-029`.

## COMM-WD-036 — Retention policy metadata does not justify a new Communications Resource

**Status:** `WORKING_DESIGN_ACCEPTED`

Communications may need policy/version/classification references on its records or through the platform retention contract.

That does not justify a `CommunicationRetentionPolicy` business Resource inside Communications.

Privacy & Consent owns retention-policy authority. Communications owns the record being disposed and applies the effective owner-mediated disposition.

Exact representation remains later JIT detail.

## COMM-WD-037 — Late provider evidence after completed deletion cannot recreate participant linkage

**Status:** `WORKING_DESIGN_ACCEPTED`

A provider callback/event may arrive after the applicable Communications record or participant linkage has been deleted/anonymised.

The callback must not:

- recreate a deleted `MessageIntent`;
- restore a destination;
- reconnect evidence to a deleted Account;
- recreate canonical identity;
- restart delivery;
- defeat deletion completion.

If provider evidence can no longer be safely correlated under the approved retained/suppression contract, it is handled as unmatched/minimised external evidence or discarded according to provider/retention policy.

Exact provider-message tombstone/idempotency mechanism remains `OQ-030`/JIT and is not a new business Resource.

## COMM-WD-038 — External processor deletion acknowledgement is evidence, not deletion completion

**Status:** `UPSTREAM_DERIVED`

For any launch messaging processor:

```text
request accepted != processor deletion complete
```

Privacy Pre-JIT and Architecture already require unresolved processor paths to remain unresolved rather than fabricating deletion completion.

Communications owns the provider-facing execution/evidence for its processor boundary; Privacy & Consent owns aggregate full-deletion completion.

Exact provider API, retry limits, evidence and legal-retention behaviour remain `OQ-030` / `OQ-032`.

## COMM-WD-039 — Restore is provider-egress fail-closed until privacy/suppression reconciliation completes

**Status:** `WORKING_DESIGN_ACCEPTED`, derived from Architecture restore doctrine

A restored environment can contain historical:

- MessageIntents;
- DeliveryAttempts;
- protected capability bytes;
- Oban jobs;
- provider operation identifiers.

Therefore restored async execution must not regain provider egress merely because the database/queue has started.

Before normal Communications execution resumes:

```text
restore
→ recover current deletion/suppression/hold authority
→ reconcile Communications owner records
→ render forbidden protected material unusable
→ suppress/cancel stale restored jobs
→ verify no deleted participant can be contacted/reconstructed
→ enable normal provider egress
```

Exact operational control remains `OQ-031` / later proof.

## COMM-WD-040 — Duplicate-account merge does not re-parent old Communications history to the survivor as new authority

**Status:** `WORKING_DESIGN_ACCEPTED`

When Identity applies a duplicate-account reconciliation:

- historical Communications provenance remains tied to the source Account/operation that caused it;
- an outstanding intent from the non-surviving Account is not silently rewritten to the survivor Account or survivor email;
- current dispatch authority is re-evaluated through Identity's canonical/reconciliation state;
- if a new message is required for the surviving Account, the source owner creates a new source obligation and a new `MessageIntent`.

This prevents a stale proof/message from becoming valid merely because two Accounts were reconciled.

## COMM-WD-041 — Candidate or conflicted merge does not change Communications authority

**Status:** `UPSTREAM_DERIVED`

Identity explicitly distinguishes detected/candidate/review/conflict from an applied merge.

Therefore Communications must not:

- retarget;
- cancel;
- merge histories;
- move provider evidence;
- change destination authority

merely because two Accounts are suspected duplicates.

Only an applied authoritative reconciliation can change current source dispatch eligibility.

## COMM-WD-042 — Completed deletion permanently disables participant/operator resend of historical intents

**Status:** `UPSTREAM_DERIVED`

After completed full deletion:

- no historical `MessageIntent` may be reopened;
- no protected delivery capability may be reconstructed;
- no operator may “retry” a pre-deletion verification/recovery/security message;
- retained evidence, where lawful, is historical evidence only.

A later person registering the same email address creates a new Account relationship and new source obligations.

Contact equality is not continuity of deleted authority.

## COMM-WD-043 — Deletion versus new-intent creation must converge fail-closed

**Status:** `WORKING_DESIGN_ACCEPTED`

A full-deletion/suppression transition can race a source action attempting to establish a new Communication intent.

Required invariant:

```text
deletion/suppression authority wins first
→ new participant-linked intent is rejected/suppressed

new source transition wins first
→ deletion orchestration must discover and dispose/suppress the resulting Communications representation before deletion can complete
```

No cross-Domain global database transaction is required by this semantic statement.

Deletion completion may not be declared while an unresolved eligible Communications representation/provider path remains.

## COMM-WD-044 — Legal hold preserves only scoped evidence, not send authority

**Status:** `UPSTREAM_DERIVED`

If a lawful hold covers Communications evidence:

- the held historical record may remain restricted;
- optional/ordinary use stays prohibited;
- the hold does not restore the Account;
- the hold does not restore a destination as active contact authority;
- the hold does not preserve or reactivate a bearer capability;
- the hold does not authorise resend;
- unrelated eligible Communications data continues through deletion.

On hold release, deferred disposition resumes without a new participant request.

## COMM-WD-045 — Communications deletion completion is a reported sub-result, not global privacy completion

**Status:** `WORKING_DESIGN_ACCEPTED`

Communications can truthfully report only its own owner-contract state, conceptually:

```text
NOT_APPLICABLE
PENDING
BLOCKED_UNRESOLVED
COMPLETED
RETAINED_BY_APPROVED_OBLIGATION
```

This does not define one mandatory database enum.

Communications cannot mark the participant's full deletion complete. Privacy & Consent aggregates all owner and processor outcomes and owns final completion.

## COMM-WD-046 — Participant-visible terminal failure disappears as a recovery path once deletion is complete

**Status:** `WORKING_DESIGN_ACCEPTED`

Before deletion, terminal delivery failure may need participant/operator recovery.

After completed full deletion, that same historical failure cannot remain an actionable participant/account recovery item because there is no Account/product recovery path.

If evidence is retained, it is restricted historical evidence only.

This avoids retained operational queues becoming a backdoor reconstruction surface.

---

# 29. Lifecycle refinement — v0.3.0

## 29.1 Source dispatch-authority dimension

The v0.2.0 binary source-authorisation dimension is superseded by:

```text
ALLOW_NEW_DISPATCH
→ SUSPEND_NEW_DISPATCH
→ ALLOW_NEW_DISPATCH     # only after current owner revalidation

ALLOW_NEW_DISPATCH
→ STOP_NEW_DISPATCH

SUSPEND_NEW_DISPATCH
→ STOP_NEW_DISPATCH
```

`STOP_NEW_DISPATCH` is terminal for the same source obligation.

`SUSPEND_NEW_DISPATCH` is not proof validity. It means current platform authority does not permit a new provider submission at this moment.

A suspension may be caused by an orthogonal Account/privacy lifecycle while the source challenge itself remains historically present.

## 29.2 Communications data-lifecycle dimension

Separate from message delivery state:

```text
IDENTIFIABLE_ACTIVE
→ RESTRICTED
→ RETAINED_BY_APPROVED_OBLIGATION
→ disposed when authority ends

IDENTIFIABLE_ACTIVE
→ DELETION_PENDING
→ DELETED

IDENTIFIABLE_ACTIVE
→ DELETION_PENDING
→ IRREVERSIBLY_ANONYMISED

IDENTIFIABLE_ACTIVE
→ LEGAL_HOLD
→ prior/deferred disposition after release
```

Not every Communications record needs every conceptual state and this is not a demand for one universal enum.

The governing rule is that delivery state cannot grant retention, and retention cannot grant delivery authority.

## 29.3 Restore lifecycle projection

```text
RESTORED_BYTES
→ PROVIDER_EGRESS_DISABLED
→ CURRENT_PRIVACY_AUTHORITY_RECOVERED
→ COMMUNICATIONS_RECONCILED
→ DERIVED/JOB STATE_REBUILT_OR_SUPPRESSED
→ SEMANTIC_VERIFICATION
→ NORMAL_EXECUTION_ENABLED
```

Any failure to establish current deletion/suppression authority leaves Communications fail-closed for provider egress.

---

# 30. Pressure-test register — third cluster

## COMM-PT-028 — Account closes while verification message is queued

- **Scenario:** verification intent exists; Account becomes `closed_recoverable` before dispatch.
- **Authority involved:** Product account-closure law; Identity Account state; Communications source revalidation.
- **Durable truths and owner:** Identity owns closure and challenge; Communications owns unresolved intent.
- **Concurrency/retry/reordering/crash behaviour:** closure and dispatch authorisation may race across nodes.
- **Rejected models:** queue existence permanently authorises send; delete intent because closure equals deletion; Communications decides Account reopening.
- **Required invariant:** current closure/source policy determines `ALLOW/SUSPEND/STOP` before a new attempt; optional/obsolete dispatch cannot proceed merely because it was queued.
- **Recommended JIT shape:** closure participates in source dispatch-disposition revalidation; intent history remains separate from deletion.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** both closure/dispatch orderings; no post-closure unauthorised new attempt.
- **Verdict:** PASS.

## COMM-PT-029 — Closed-recoverable Account requires a governed recovery/security message

- **Scenario:** ordinary login is disabled but participant enters the authorised closure-recovery path.
- **Authority involved:** Product 30-day recoverable closure; Identity recovery authority.
- **Durable truths and owner:** Identity decides whether recovery message is required; Communications delivers it.
- **Concurrency/retry/reordering/crash behaviour:** recovery initiation may occur while other old intents are suspended.
- **Rejected models:** blanket “closed Account can never receive email”; reuse unrelated old verification intent; optional NotificationPreference controls required recovery.
- **Required invariant:** only the new/current source-authorised recovery obligation can dispatch.
- **Recommended JIT shape:** role-specific source disposition; fresh source obligation when Identity requires one.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** closed Account recovery path can receive required message while unrelated suspended intents cannot leak through.
- **Verdict:** PASS.

## COMM-PT-030 — Account reopens while a previously suspended MessageIntent is still unexpired

- **Scenario:** closure is reversed within 30 days.
- **Authority involved:** Identity reopening; source challenge validity.
- **Durable truths and owner:** Identity determines current source validity; Communications owns same unresolved logical intent.
- **Concurrency/retry/reordering/crash behaviour:** reopening and challenge expiry/supersession can race.
- **Rejected models:** automatic replay of every suspended message; always create a duplicate new intent; assume suspension is terminal.
- **Required invariant:** same intent may continue only if the exact same source obligation remains valid/current and reauthorises dispatch; otherwise stop or create a new source intent.
- **Recommended JIT shape:** `SUSPEND → ALLOW` only through current source revalidation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** reopen before/after proof expiry and supersession.
- **Verdict:** PASS.

## COMM-PT-031 — Closure races provider submission with unknown outcome

- **Scenario:** provider call may have happened, response is lost, then Account closes.
- **Authority involved:** provider ambiguity + Identity closure.
- **Durable truths and owner:** DeliveryAttempt remains Communications evidence; closure changes future dispatch eligibility.
- **Concurrency/retry/reordering/crash behaviour:** ambiguous attempt cannot be undone.
- **Rejected models:** closure marks ambiguous attempt “failed” and blindly retries; closure deletes evidence; provider acceptance reopens Account.
- **Required invariant:** unresolved attempt stays reconciliation-required; closure prevents any new attempt unless later current authority allows it.
- **Recommended JIT shape:** attempt reconciliation independent of dispatch disposition.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** timeout → closure → late provider evidence; no duplicate send.
- **Verdict:** PASS.

## COMM-PT-032 — Full-deletion request starts while queued FP-001 messages exist

- **Scenario:** deletion enters its 14-day cancellation window while verification/reset/recovery/security intents are pending.
- **Authority involved:** Privacy deletion orchestration; Identity source lifecycle; Product optional-processing stop.
- **Durable truths and owner:** Privacy owns deletion request; source owner owns challenge; Communications owns intents.
- **Concurrency/retry/reordering/crash behaviour:** stale jobs may wake during deletion pending.
- **Rejected models:** continue all sends until deletion execution; delete Communications rows immediately without owner result; treat deletion request as final completed deletion.
- **Required invariant:** current deletion authority can suspend/stop new participant-linked dispatch; stale workers recheck it.
- **Recommended JIT shape:** owner-mediated deletion/suppression consequence plus dispatch revalidation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO for FP-001; full orchestration remains later capability.
- **Later executable proof:** deletion request races queued job; no unauthorised dispatch.
- **Verdict:** PASS.

## COMM-PT-033 — Full-deletion request is cancelled within the 14-day window

- **Scenario:** participant lawfully cancels deletion after Communications work was suspended.
- **Authority involved:** Privacy deletion lifecycle plus Identity source validity.
- **Durable truths and owner:** Privacy decides cancellation; Communications has suspended/terminal records.
- **Concurrency/retry/reordering/crash behaviour:** cancellation may occur after proof expiry or source supersession.
- **Rejected models:** automatically replay all previously pending communications; reconstruct destroyed bearer capability; reopen a `STOP`ped intent.
- **Required invariant:** only `SUSPEND`ed intents whose exact source obligation remains current may resume; terminal/expired sources require new issuance.
- **Recommended JIT shape:** current source/privacy revalidation after deletion cancellation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** cancellation before and after challenge expiry; no bearer reconstruction.
- **Verdict:** PASS.

## COMM-PT-034 — Full deletion executes while a provider attempt is in flight

- **Scenario:** external send was lawfully authorised before deletion execution; deletion becomes irreversible before provider result returns.
- **Authority involved:** Privacy irreversible deletion; Communications provider evidence; Identity proof invalidation.
- **Durable truths and owner:** deletion cannot unsend external network work; it can eliminate future authority and participant linkage.
- **Concurrency/retry/reordering/crash behaviour:** provider may later accept/deliver.
- **Rejected models:** delay deletion forever until provider network settles; claim physical recall; late delivery recreates Account; delete all evidence before reconciliation when approved evidence retention is needed.
- **Required invariant:** no later attempt, no usable proof/account recovery, no reconstructed participant linkage; late evidence handled under approved deletion/retention policy.
- **Recommended JIT shape:** irreversible privacy cutover ends future dispatch and bearer authority; in-flight evidence reconciles separately.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** delete during in-flight attempt; late accept/deliver does not resurrect authority.
- **Verdict:** PASS.

## COMM-PT-035 — Completed deletion with pending protected delivery capability

- **Scenario:** a secret-bearing capability still exists when deletion is about to complete.
- **Authority involved:** certified Identity protected-delivery lifetime; Privacy completion/non-reconstruction.
- **Durable truths and owner:** capability is delivery machinery only.
- **Concurrency/retry/reordering/crash behaviour:** cleanup can race deletion completion/restart.
- **Rejected models:** retain encrypted bearer “for troubleshooting”; legal hold automatically keeps it; deletion completes while executor can still recover it.
- **Required invariant:** completed deletion cannot coexist with recoverable protected bearer material tied to the deleted participant.
- **Recommended JIT shape:** capability irrecoverability is a Communications/Identity owner-contract prerequisite to applicable deletion completion.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** deletion completion fails closed while capability recoverable; restart cannot restore it.
- **Verdict:** PASS.

## COMM-PT-036 — Completed deletion with historical MessageIntent / DeliveryAttempt rows

- **Scenario:** business-delivery history exists after participant deletion.
- **Authority involved:** Product category-specific retention; Architecture deletion; `OQ-029`.
- **Durable truths and owner:** Communications owns record semantics; Privacy owns disposition authority.
- **Concurrency/retry/reordering/crash behaviour:** retention job/deletion orchestration may retry.
- **Rejected models:** keep everything because delivery is “audit”; delete everything regardless approved legal/security basis; keep destination and Account linkage merely because attempt record survives.
- **Required invariant:** identifiable fields/evidence follow approved category policy; retained evidence is minimised/restricted/non-reconstructive.
- **Recommended JIT shape:** separate data-lifecycle/disposition from delivery lifecycle.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO; exact periods remain OQ-029.
- **Conditional dossier pulled forward:** NO at FP-001.
- **Later executable proof:** retained-by-obligation versus delete/anonymise paths.
- **Verdict:** PASS.

## COMM-PT-037 — Late provider callback after local participant linkage was deleted

- **Scenario:** bounce/delivery callback arrives using a provider message id after local deletion/anonymisation.
- **Authority involved:** Communications provider ingress; Privacy non-resurrection.
- **Durable truths and owner:** callback is external evidence only.
- **Concurrency/retry/reordering/crash behaviour:** duplicate/late/reordered callbacks normal.
- **Rejected models:** recreate intent/account mapping to attach callback; search deleted email address; retain unnecessary reverse lookup forever.
- **Required invariant:** late evidence cannot reconstruct deleted participant state.
- **Recommended JIT shape:** bounded provider-evidence handling under the approved processor/retention contract; unmatched evidence safe.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** callback after deletion cannot recreate participant linkage; duplicates harmless.
- **Verdict:** PASS; exact provider mechanism is OQ-030.

## COMM-PT-038 — Messaging provider accepts deletion request but completion is unknown

- **Scenario:** external processor returns acknowledgement but not verified final disposition.
- **Authority involved:** Privacy deletion completion; provider evidence.
- **Durable truths and owner:** Communications owns processor-request evidence; Privacy owns aggregate completion.
- **Concurrency/retry/reordering/crash behaviour:** request may have succeeded despite timeout or may require later provider evidence.
- **Rejected models:** HTTP 2xx/queued acknowledgement equals deletion completion; retry exhaustion equals complete; provider dashboard becomes Privacy authority.
- **Required invariant:** required unresolved processor path keeps deletion unresolved.
- **Recommended JIT shape:** provider request/reconciliation evidence with explicit unresolved state; exact provider API later.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO; OQ-030/OQ-032 remain named gates.
- **Later executable proof:** ack-only, timeout, duplicate request and late completion evidence.
- **Verdict:** PASS.

## COMM-PT-039 — Duplicate deletion orchestration invokes Communications twice

- **Scenario:** Privacy retries the owner deletion contract after timeout/crash.
- **Authority involved:** Architecture idempotent deletion.
- **Durable truths and owner:** one Communications disposition result for the same deletion operation.
- **Concurrency/retry/reordering/crash behaviour:** repeated calls may overlap.
- **Rejected models:** second call creates a new participant-linked message, duplicates processor erasure request unsafely, or changes a completed disposition back to pending.
- **Required invariant:** same deletion operation converges; destructive effects and processor operations are repeat-safe/reconciled.
- **Recommended JIT shape:** durable deletion operation identity/reference at owner interface; exact storage later.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate concurrent deletion calls and crash/retry.
- **Verdict:** PASS.

## COMM-PT-040 — New MessageIntent establishment races deletion/suppression

- **Scenario:** Identity attempts to create a security intent while Privacy deletion becomes effective.
- **Authority involved:** source transition + Privacy deletion authority + Architecture cross-domain consequence semantics.
- **Durable truths and owner:** source owns Identity transition; Communications owns intent; Privacy owns deletion suppression.
- **Concurrency/retry/reordering/crash behaviour:** neither Domain may assume event delivery order equals authority order.
- **Rejected models:** last event wins; deletion completes without scanning/reconciling new representation; global shared-write Privacy transaction.
- **Required invariant:** either new intent is blocked/suppressed, or deletion owner workflow detects and disposes it before aggregate completion.
- **Recommended JIT shape:** fail-closed owner reconciliation; exact coordination left to later JIT/proof.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO for FP-001.
- **Later executable proof:** deterministic both-order race plus crash after each commit.
- **Verdict:** PASS.

## COMM-PT-041 — Legal hold covers a DeliveryAttempt/provider evidence record during full deletion

- **Scenario:** approved hold applies to narrowly scoped security/provider evidence.
- **Authority involved:** Privacy legal-hold authority; Communications record ownership.
- **Durable truths and owner:** hold does not transfer business ownership.
- **Concurrency/retry/reordering/crash behaviour:** hold can race destructive disposition.
- **Rejected models:** hold preserves entire Account/intent destination; hold authorises resend; delete held record after destructive commit already began without revalidation.
- **Required invariant:** held evidence remains restricted/minimised; unrelated data deletion continues; send authority remains stopped.
- **Recommended JIT shape:** owner disposition respects current hold scope; bearer capability excluded unless independently and explicitly justified—which current authority does not justify.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** hold/delete race, release resumes deferred disposition.
- **Verdict:** PASS.

## COMM-PT-042 — Backup restore predates participant deletion

- **Scenario:** disaster restore recreates old Communications records/jobs for a participant deleted after the restore point.
- **Authority involved:** Architecture backup/restore; Privacy suppression replay.
- **Durable truths and owner:** historical backup bytes are not present authority.
- **Concurrency/retry/reordering/crash behaviour:** Oban/worker startup can race suppression replay.
- **Rejected models:** start workers/provider egress immediately after DB restore; trust restored queue schedule; manually delete rows later.
- **Required invariant:** no restored stale job can contact or reconstruct the deleted participant before current suppression authority is reapplied.
- **Recommended JIT shape:** provider egress/Communications execution recovery gate.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** restore pre-deletion snapshot with pending job/protected capability; prove zero external send before reconciliation and none after suppression.
- **Verdict:** PASS; exact runbook remains OQ-031.

## COMM-PT-043 — Restored backup contains protected bearer capability for a deleted Account

- **Scenario:** encrypted backup predates capability destruction/deletion.
- **Authority involved:** certified Identity protected-delivery boundary + backup replay doctrine.
- **Durable truths and owner:** backup byte existence is not current permission to decrypt/use.
- **Concurrency/retry/reordering/crash behaviour:** restored executor could otherwise recover the secret.
- **Rejected models:** encryption-at-rest makes restored use acceptable; restored job proves permission.
- **Required invariant:** current deletion/suppression authority prevents capability recovery/use and ensures irrecoverability before provider egress.
- **Recommended JIT shape:** execution checks present authority; recovery-gated restore invalidates/destroys stale capability.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale encrypted capability physically present but ordinary executor cannot use it.
- **Verdict:** PASS.

## COMM-PT-044 — Applied duplicate-account merge while losing Account has queued verification/recovery intent

- **Scenario:** Account B is merged into canonical Account A while B has outstanding source-bound messages.
- **Authority involved:** Identity reconciliation; Communications source provenance.
- **Durable truths and owner:** B's challenge/operation remains historical B provenance; canonical current Account is A.
- **Concurrency/retry/reordering/crash behaviour:** B job may execute after merge.
- **Rejected models:** rewrite B intent to A; send B proof to A's current email; old B proof becomes A proof.
- **Required invariant:** B intent obtains no new dispatch unless Identity's current canonical/source contract explicitly still authorises that exact obligation; no automatic re-parenting.
- **Recommended JIT shape:** source canonicality/reconciliation participates in dispatch disposition; new A obligation becomes new MessageIntent.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO presently required.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** applied merge before stale B worker, plus link consumption attempt.
- **Verdict:** PASS.

## COMM-PT-045 — Provider attempt for losing Account is already in flight when merge applies

- **Scenario:** B's message was lawfully dispatched; merge to A commits before provider result/delivery.
- **Authority involved:** Identity merge + Communications provider evidence.
- **Durable truths and owner:** attempt remains historical B evidence; merge does not rewrite it.
- **Concurrency/retry/reordering/crash behaviour:** late delivery/callback arrives after merge.
- **Rejected models:** relabel attempt as A delivery; use provider evidence to verify/authenticate A; erase original provenance.
- **Required invariant:** late B evidence cannot grant A authority; no further B attempt after source stop.
- **Recommended JIT shape:** immutable causal/source provenance plus current dispatch revalidation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** in-flight B attempt + merge + late callback.
- **Verdict:** PASS.

## COMM-PT-046 — Duplicate-account reconciliation is only candidate/conflicted, not applied

- **Scenario:** staff/system suspects duplicate Accounts but Identity has not committed merge.
- **Authority involved:** Identity reconciliation lifecycle.
- **Durable truths and owner:** both Accounts retain their own current authority until applied resolution.
- **Concurrency/retry/reordering/crash behaviour:** communications may continue independently.
- **Rejected models:** suppress/retarget based on candidate match; use same email/name as merge proof.
- **Required invariant:** Communications authority changes only from applied source truth.
- **Recommended JIT shape:** ignore candidate merge for business retargeting; preserve ordinary source checks.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** conflict/reject leaves each Account intent unchanged.
- **Verdict:** PASS.

## COMM-PT-047 — New Account later uses the same email after completed deletion

- **Scenario:** person re-registers with an email matching deleted historical Communications data/provider metadata.
- **Authority involved:** Product full-deletion non-reconstruction; Identity new relationship.
- **Durable truths and owner:** new Account is new authority; old retained evidence is non-reconstructive.
- **Concurrency/retry/reordering/crash behaviour:** historical provider callbacks or retained rows may still exist.
- **Rejected models:** reconnect by email equality; restore old intent history; reuse protected capability/provider message ids as new Account state.
- **Required invariant:** no automatic continuity from deleted Communications history to new Account.
- **Recommended JIT shape:** new source IDs and new MessageIntents; retained historical evidence remains isolated.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** same-email re-registration cannot access or resume old communication obligations.
- **Verdict:** PASS.

## COMM-PT-048 — Operator attempts retry of an intent after completed deletion

- **Scenario:** terminal-failure/admin queue retains a stale action.
- **Authority involved:** Privacy completed deletion; Communications operator interface.
- **Durable truths and owner:** old delivery record may be retained evidence but no active participant authority remains.
- **Concurrency/retry/reordering/crash behaviour:** stale UI/action can survive cache/reconnect.
- **Rejected models:** operator override bypasses deletion; support can recover destination from provider evidence; stale queue action is authority.
- **Required invariant:** authoritative action fails closed after deletion; UI projection cannot resurrect retry.
- **Recommended JIT shape:** operator retry action revalidates current dispatch/data authority; completed deletion is terminal denial.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale admin page/command after deletion receives safe denial without destination leakage.
- **Verdict:** PASS.

## COMM-PT-049 — Terminal delivery failure exists while full deletion completes

- **Scenario:** participant-visible recovery/escalation item exists because a mandatory security message failed; then deletion completes.
- **Authority involved:** Communications failure visibility; Privacy no-recovery rule.
- **Durable truths and owner:** historical failure may remain only under retention authority.
- **Concurrency/retry/reordering/crash behaviour:** operator queue projection may lag deletion.
- **Rejected models:** failure queue keeps Account actionable indefinitely; deletion blocks forever merely because participant delivery failed for an obsolete source.
- **Required invariant:** once underlying participant/source obligation is extinguished by completed deletion, delivery failure is no longer an actionable recovery path.
- **Recommended JIT shape:** source/deletion transition terminalises actionable retry while retaining only permitted evidence.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale failure queue cannot retry after deletion; evidence remains appropriately restricted.
- **Verdict:** PASS.

## COMM-PT-050 — Retained provider evidence contains identifiers that could reconstruct deleted Account linkage

- **Scenario:** provider message id, destination, correlation id and timestamps together permit practical relinking.
- **Authority involved:** Product minimised/non-reconstructive retention; Architecture anonymisation doctrine.
- **Durable truths and owner:** retained evidence must satisfy its approved purpose without becoming hidden Account reconstruction.
- **Concurrency/retry/reordering/crash behaviour:** historical exports/analytics/read models may carry copies.
- **Rejected models:** “remove account_id” automatically equals anonymised; reversible encryption/pseudonymisation called irreversible; keep raw destination as troubleshooting convenience.
- **Required invariant:** disposition is classified truthfully; if re-linkage remains practical, evidence is still identifiable/restricted rather than falsely anonymised.
- **Recommended JIT shape:** category-specific delete/minimise/pseudonymise/anonymise decision under Privacy authority.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO; exact matrix remains OQ-029.
- **Conditional dossier pulled forward:** NO at FP-001.
- **Later executable proof:** re-identification attack against intended anonymised representation and derived copies.
- **Verdict:** PASS.

## COMM-PT-051 — External processor deletion cannot be completed because provider is unavailable

- **Scenario:** provider deletion API/outcome unavailable through the deletion window.
- **Authority involved:** Privacy completion; OQ-030/OQ-032 provider operations.
- **Durable truths and owner:** unresolved provider path is not completion.
- **Concurrency/retry/reordering/crash behaviour:** long outage, retries, provider recovery.
- **Rejected models:** mark deletion complete after retry budget exhaustion; indefinitely spam provider; reconstruct ordinary Account access so support can investigate.
- **Required invariant:** local participant/product authority stays deleted/suppressed; aggregate deletion remains unresolved where processor completion is required; provider recovery is bounded/reconcilable.
- **Recommended JIT shape:** later provider-specific processor-deletion reconciliation under privacy orchestration.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO for FP-001 planning; this is a later release/provider gate.
- **Later executable proof:** prolonged outage/backlog and eventual reconciliation without participant resurrection.
- **Verdict:** PASS / RELEASE-GATED.

## COMM-PT-052 — Legal hold releases after Account deletion completed for all non-held Communications data

- **Scenario:** narrow provider/security evidence survives under hold; hold later releases.
- **Authority involved:** Privacy legal-hold release.
- **Durable truths and owner:** no Account authority survives merely because held evidence exists.
- **Concurrency/retry/reordering/crash behaviour:** release job may duplicate/reorder.
- **Rejected models:** require participant to request deletion again; reconnect held evidence to a new Account; release recreates delivery task.
- **Required invariant:** deferred disposition resumes idempotently; no send/recovery authority appears.
- **Recommended JIT shape:** hold release triggers owner disposition only.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate hold release and same-email re-registration remain isolated.
- **Verdict:** PASS.

---

# 31. Rejected-model register additions — v0.3.0

24. **Treat Account closure as full deletion.** Rejected: current Product/Architecture explicitly separate them.
25. **Treat closure as a blanket prohibition on required recovery/security communication.** Rejected: Product stops optional communication; governed recovery may still require delivery.
26. **Automatically replay every suspended message when an Account reopens.** Rejected: current source obligation must be revalidated.
27. **Keep binary `valid/invalid` dispatch state only.** Rejected: recoverable suspension is materially different from terminal source invalidation.
28. **Let Privacy directly update/delete Communications rows.** Rejected: shared-write ownership violates Domain doctrine.
29. **Let Communications declare full participant deletion complete.** Rejected: Privacy & Consent owns cross-system completion.
30. **Retain MessageIntent/DeliveryAttempt forever because they are “audit”.** Rejected: Audit and Communications evidence have category-specific retention authority.
31. **Legal hold preserves bearer capability or resend authority.** Rejected.
32. **Provider erasure acknowledgement automatically proves processor completion.** Rejected.
33. **Provider retry exhaustion equals privacy deletion completion.** Rejected.
34. **Start Oban/provider egress immediately after restoring a historical database.** Rejected: stale jobs can contact deleted participants.
35. **Rewrite losing-Account MessageIntents to the merge survivor.** Rejected: corrupts source provenance and can transfer stale proof authority.
36. **Act on candidate duplicate detection as if merge were applied.** Rejected.
37. **Reconnect a newly registered Account to deleted Communications history by matching email/phone.** Rejected.
38. **Allow support/operator tooling to retry historical messages after completed deletion.** Rejected.
39. **Call identifier removal “anonymous” while practical provider/correlation linkage remains.** Rejected.
40. **Keep raw destinations/provider metadata merely because troubleshooting may be useful later.** Rejected without independent retention authority.

---

# 32. Upstream-delta register — v0.3.0

## Required upstream amendments

**NONE identified for FP-001 Communications from this cluster.**

The current Product, Architecture, Domain, Roadmap and certified Identity authority are sufficient to establish the Communications owner boundary without inventing full deletion implementation.

## Deliberately deferred owner-specific semantics

The following are real but already governed as later gates rather than defects in the FP-001 Communications contract:

- exact retention duration and category disposition — `OQ-029`;
- exact messaging-processor deletion/export inventory and provider behaviour — `OQ-030`;
- exact restore/suppression replay/runbook and go-live evidence — `OQ-031`;
- exact deletion-operation deadlines, retries, notices, failure alerts and completion evidence — `OQ-032`.

## Identity seam noted but not currently blocking

Current Identity dossier does not enumerate a bespoke challenge transition for every Account closure/merge/deletion interleaving.

Communications does not need to invent those Identity transitions if the source-owner interface supplies current dispatch disposition for the exact source obligation.

If later governed Identity implementation cannot provide a deterministic `ALLOW / SUSPEND / STOP` answer without changing its certified lifecycle semantics, **STOP at Identity JIT and make the smallest Identity dossier amendment**. Do not resolve that contradiction inside Communications.

No such contradiction is proven by current authority.

---

# 33. Unresolved-gate register additions — v0.3.0

| Gate / open matter | v0.3.0 effect |
|---|---|
| `OQ-029` retention schedule matrix | Exact retention/anonymisation/deletion durations for MessageIntent, DeliveryAttempt, provider metadata and any restricted evidence remain open. Does not block this Pre-JIT/JIT contract shape; blocks applicable release as governed. |
| `OQ-030` external processor deletion inventory | Material to the chosen email provider. Roadmap explicitly makes processor inventory release-blocking when that processor is used. |
| `OQ-031` backup restore/deletion replay | Communications requires provider-egress fail-closed restore semantics; exact recovery runbook/evidence remains downstream. |
| `OQ-032` export/deletion operations | Exact deadlines, processor retries, participant notices, failure alerts and completion evidence remain downstream. |
| Protected capability during reversible deletion-pending | Exact source challenge/capability invalidation timing is owner/JIT detail. Completed deletion cannot retain recoverable capability. |
| Closure-specific challenge persistence | Communications needs only current source dispatch disposition. If Identity cannot supply this under its certified semantics, amend Identity rather than inventing Communications authority. |
| Provider callback after deletion | Exact safe correlation/tombstone mechanism depends on provider and retention policy; semantic non-resurrection invariant is fixed. |

---

# 34. Cross-stream dependency register additions — v0.3.0

| Stream / Domain | v0.3.0 finding |
|---|---|
| Identity & Access | Supplies current Account/reconciliation/challenge authority. Closure/merge never transfer proof authority to Communications. |
| Privacy & Consent | Owns deletion request/cancellation/completion, retention policies, legal holds and suppression/replay truth. Communications must expose an idempotent owner deletion contract. |
| Audit & Evidence | May retain minimum central security/audit linkage under its own approved class. Communications provider/delivery evidence does not become Audit-owned merely because it is historical. |
| Analytics | Identifiable delivery/engagement data follows deletion rules; retained aggregate analytics cannot reconstruct deleted participant identity. |
| Provider / OQ-030 | Messaging processor is part of deletion/export/reconciliation scope once selected; provider retention policy does not become NewYou retention authority. |
| Operations / OQ-031 | Restore ordering must prevent restored jobs/provider egress before current privacy authority is recovered. |
| Future accountless contact work | Accountless contacts remain a separate mature Communications truth; no SubscriberContact is introduced by this Account-deletion cluster. |

---

# 35. Conditional-dossier adjudication — v0.3.0

## Privacy & Consent

**Disposition: `CONDITIONAL / NOT PULLED FORWARD FOR FP-001`.**

This was the strongest cluster so far for potentially pulling Privacy forward, but current authority remains sufficient.

Why no FP-001 Privacy dossier is yet required:

1. Product Law already distinguishes closure from full deletion and freezes the 30-day / 14-day semantics.
2. Architecture already requires owner-specific deletion contracts, idempotent orchestration, non-reconstruction and restore suppression replay.
3. Domain Law already assigns Privacy the deletion/retention/hold authority and Communications its own records.
4. The FP-001 Skeleton explicitly excludes reusable full data-rights/retention/deletion orchestration, except for the identity-side distinctions needed to protect the entry boundary.
5. The existing Privacy Pre-JIT contract already captures the unresolved later proof/gate classes without making them FP-001 authority.

Therefore the Communications JIT can be implementation-grade for **its owner interface and invariants** without specifying the full Privacy orchestration engine.

**Pull-forward trigger:** if Phase 7C needs exact FP-001 Privacy-owned deletion/retention state transitions—not merely a Communications owner contract and later release gate—in order to state the FP-001 outcome, then Privacy becomes required. Current evidence has not reached that threshold.

## Audit & Evidence

**Disposition: `CONDITIONAL / NOT PULLED FORWARD`.**

Provider/delivery evidence remains Communications-owned. Central audit may link security/deletion actions under existing authority. Exact Audit retention durations remain OQ-029 and do not require a separate FP-001 dossier now.

**Pull-forward trigger:** if Phase 7C cannot define required central security/deletion evidence without inventing Audit-owned event/access/retention semantics.

## Content & Media

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD`.**

No new content lifecycle question was introduced by this cluster.

---

# 36. Later executable proof-obligation register additions — v0.3.0

26. Race recoverable Account closure against dispatch authorisation in both orderings.
27. Prove closed Account can receive only currently source-authorised recovery/security communication while obsolete/optional intents remain suppressed.
28. Reopen Account with suspended intent before/after source expiry and prove no automatic stale replay.
29. Provider unknown-outcome attempt followed by Account closure: reconcile evidence without duplicate new attempt.
30. Race deletion request against queued MessageIntent execution across nodes.
31. Cancel deletion window and prove only still-current suspended obligations may resume; no terminal bearer reconstruction.
32. Execute full deletion during in-flight provider attempt and prove late provider evidence cannot restore proof/Account/destination authority.
33. Prove completed deletion cannot coexist with executor-recoverable protected delivery capability.
34. Exercise delete/anonymise/retained-by-obligation disposition for Communications records without conflating delivery state.
35. Late callback after local deletion cannot recreate Account/intended destination linkage.
36. Messaging-processor deletion: request accepted, timeout, duplicate request, provider unavailable and late completion evidence.
37. Duplicate/concurrent Communications deletion-contract invocation converges idempotently.
38. Race new source MessageIntent establishment against effective deletion/suppression in both commit orders; deletion completion cannot miss the resulting representation.
39. Legal hold/delete race: held evidence remains restricted while unrelated Communications data is disposed.
40. Release hold after deletion and prove deferred disposition resumes without Account resurrection.
41. Restore a backup from before deletion containing MessageIntent, DeliveryAttempt, Oban job and protected capability; prove provider egress remains disabled until suppression replay/reconciliation completes.
42. Prove restored protected capability cannot be recovered/used after current deletion authority is replayed.
43. Apply duplicate-account merge with losing Account queued intent; no re-parenting/retargeting/stale proof transfer.
44. Apply merge while losing Account provider attempt is in flight; late evidence remains historical and cannot authorize survivor.
45. Candidate/conflicted/rejected merge causes no Communications retarget/suppression beyond ordinary source rules.
46. Re-register same email after completed deletion; new Account cannot access/resume historical Communications state.
47. Stale operator retry action after completed deletion fails closed even from cached/admin projection.
48. Terminal-failure queue item becomes non-actionable after completed deletion while permitted evidence remains restricted.
49. Re-identification proof for any intended anonymised Communications/provider evidence representation.
50. Verify no retained provider/delivery evidence can be used as a hidden subscriber-contact or Account reconstruction store.

---

# 37. Resource-discipline review — cumulative through v0.3.0

## `MessageIntent`

**Still required.**

The third cluster strengthens its need but does not broaden its ownership. It needs to participate in:

- closure/deletion suppression;
- owner-mediated deletion disposition;
- source/canonicality revalidation after merge;
- retention/anonymisation policy;
- restore reconciliation.

These are lifecycle obligations on an already-required Resource, not reasons for another Resource.

## `DeliveryAttempt`

**Still required.**

Deletion, legal hold, provider callback and restore scenarios independently prove the need for historical provider-operation/evidence lifecycle separate from MessageIntent.

## Protected delivery capability

**Still machinery, not business Resource.**

The deletion/restore scenarios strengthen the requirement that it be irrecoverable when current authority forbids use.

## `SubscriberContact`

**Still rejected for FP-001.**

Neither Account closure, deletion nor merge creates independent accountless contact truth. Destination provenance remains attached to the relevant MessageIntent.

## `NotificationPreference`

**Still rejected for FP-001.**

Closure/deletion suppression is Account/privacy authority, not a participant notification preference.

## `InAppNotification`

**Still rejected for FP-001.**

No data-lifecycle scenario creates a need for an FP-001 inbox.

## `CommunicationJourney`

**Still rejected for FP-001.**

Deletion orchestration is not a communication journey.

## `CommunicationDeletionCase`

**Rejected.**

Privacy & Consent owns the deletion orchestration/request. Communications applies its owner contract to existing Resources; creating a separate Communications deletion-case authority would compete with Privacy.

## `CommunicationRetentionPolicy`

**Rejected.**

Retention policy authority belongs to Privacy & Consent. Communications may reference/apply the effective policy to its records.

## `ProviderDeletionRequest`

**Not justified as an FP-001 business Resource at this stage.**

A future selected provider and `OQ-030/OQ-032` may prove that provider-deletion execution needs independent durable lifecycle/reconciliation state. Until then it is a provider-operation implementation concern under the Privacy deletion owner contract.

Do not pre-create it.

**Cumulative resource verdict through v0.3.0 remains unchanged: `MessageIntent` + `DeliveryAttempt` are the only justified durable FP-001 Communications business Resources.**

---

# 38. Completeness / stabilisation assessment — v0.3.0

**NOT YET STABLE FOR GOVERNED COMMUNICATIONS JIT DOSSIER DRAFTING.**

The Account/data-lifecycle cluster is now pressure-tested deeply enough to close this scenario class provisionally.

Material findings have begun to converge onto the existing model rather than creating new Resources:

- source dispatch disposition;
- MessageIntent;
- DeliveryAttempt;
- Privacy owner contract;
- current-authority revalidation;
- non-reconstructive retention;
- restore fail-closed.

No upstream Product/Architecture/Domain amendment is required by this cluster, and the Privacy conditional dossier still does not need to be pulled into FP-001.

The next materially distinct classes remain:

1. **Preferences / consent / accountless contacts**
   - accountless subscriber lifecycle;
   - account linkage/reconciliation;
   - marketing purpose permission versus channel/category preference;
   - mandatory security/transactional versus optional communication;
   - quiet hours, frequency caps and completion suppression;
   - consent/preference change racing queued delivery;
   - whether this forces the Privacy conditional dossier.

2. **Content / locale / rendering provenance**
   - locale at intent creation versus render versus send;
   - template version binding;
   - mutable template change after intent;
   - correction/withdrawal after intent creation;
   - retry consistency;
   - secret-bearing interpolation boundaries;
   - whether this forces Content & Media.

3. **Provider outage / backlog / operator recovery**
   - long outage;
   - bounded retries;
   - retry storm;
   - provider throttling;
   - fairness and backlog age;
   - operator retry/reconcile controls;
   - terminal escalation;
   - cross-node coordination;
   - graceful degradation.

4. **Audit / observability / evidence**
   - provider evidence versus Audit evidence;
   - security incident linkage;
   - operator actions;
   - leakage/cardinality;
   - evidence retention;
   - whether Audit & Evidence becomes required.

5. **Channel / mature-capability exclusion**
   - email-first versus in-app-first;
   - prove in-app is unnecessary for FP-001;
   - future SMS/WhatsApp without premature abstraction;
   - batch/fan-out without campaign architecture;
   - exact `OQ-036` boundary.

The recommended next pass is **Preferences / consent / accountless contacts**. It is the remaining cluster most likely to challenge `SubscriberContact` and `NotificationPreference` and therefore the current two-Resource hypothesis.

---

# 39. v0.4.0 semantic delta — preferences, consent, accountless contacts and optional acquisition

This successor preserves all accepted v0.1.0–v0.3.0 findings and adds the fourth substantive Communications pressure-test cluster.

The live repository was rechecked immediately before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

This pass pressure-tests:

- whether Product Law's public mailing-list allowance makes mailing-list signup part of FP-001;
- the Atlas `CAP-005` conditional subscriber-contact lifecycle;
- accountless mailing-list contact ownership;
- account creation using the same destination as an existing subscriber;
- accountless contact ↔ Account linkage/reconciliation;
- canonical Account email versus Communications-owned subscriber destination;
- purpose-level marketing permission versus channel/category preference;
- partial failure across Communications and Privacy-owned truths;
- duplicate/concurrent signup;
- scoped opt-out versus purpose withdrawal;
- provider unsubscribe evidence;
- ambiguous unsubscribe semantics;
- consent/preference changes racing queued delivery;
- regrant/re-enable after suppression;
- mandatory security/transactional communication versus optional marketing;
- quiet hours;
- frequency caps;
- timezone;
- future channel fallback;
- concurrency between preference edits;
- completion/obsolete-message suppression;
- whether the Privacy & Consent conditional FP-001 dossier must now be pulled forward;
- whether `SubscriberContact` or `NotificationPreference` becomes required for the current FP-001 outcome.

No legal-sufficiency rule, double-opt-in rule, provider, channel policy or `OQ-036` resolution is invented here.

---

# 40. Scope adjudication — public mailing list versus FP-001

Current authority contains all of the following simultaneously:

1. Product Law §7.3 / `DEC-017` permits a person to join the public mailing list without creating a full Account or making a purchase.
2. Frontend Experience §5.1 describes an **optional permissioned email or account relationship** and says email capture *may* be offered.
3. Delivery Atlas `CAP-005` says subscriber-contact lifecycle is `CONDITIONAL` — only where the active acquisition boundary includes a governed mailing-list relationship; its earliest possible full specification point is FP-001.
4. The governed FP-001 Roadmap outcome and exit condition require bilingual public entry, Account creation, verification, recovery and support. They do **not** promise mailing-list signup.
5. The current FP-001 Skeleton's in-scope list does not include a mailing-list signup outcome; its `CAP-005` detail indication is conditional on materially new acquisition surfaces.
6. The required Communications dossier is justified specifically by verification/recovery durable delivery.

These sources are reconcilable.

**Working adjudication:**

> Product Law permits an accountless mailing-list relationship at the platform level, and FP-001 is its earliest lawful specification point if that surface is selected. The current governed FP-001 outcome does not require that surface. Therefore accountless mailing-list signup is a **conditional FP-001 acquisition surface, not an implied Communications requirement**.

The governed Communications JIT must not silently include it merely because the mature Domain owns `SubscriberContact`.

If the later FP-001 Final Contract explicitly activates the mailing-list surface, the conditional branch in §48 applies.

This conclusion is `UPSTREAM_DERIVED` from the combination of Roadmap, Skeleton, Atlas, Product and FES scope.

No upstream amendment is required.

---

# 41. Accepted working-design register additions — v0.4.0

## COMM-WD-047 — The required FP-001 Communications contract excludes accountless mailing-list state unless the conditional acquisition surface is explicitly activated

**Status:** `UPSTREAM_DERIVED`

For the currently required FP-001 outcome:

```text
required Communications scope
= Account-originated verification / reset / recovery / email-change / required security delivery
```

The mere existence of Product Law's mailing-list allowance does not make accountless subscriber state part of the required outcome.

Therefore `SubscriberContact` remains outside the required FP-001 Resource set unless the final Feature Pack explicitly selects the optional permissioned-email acquisition surface.

## COMM-WD-048 — Activating the mailing-list surface conditionally requires a durable SubscriberContact concept

**Status:** `WORKING_DESIGN_ACCEPTED` for the conditional branch

If FP-001 explicitly includes public mailing-list signup, the contact/destination itself becomes independent durable Communications truth because it:

- may exist without an Account;
- survives independently of Account creation;
- has Communications-owned preference state;
- may later be linked/reconciled with an Account without becoming canonical Account email;
- has its own deletion/suppression/retention concerns;
- is not reducible to a security `MessageIntent`.

At that point `SubscriberContact` is materially justified as a concept.

Whether the exact physical Ash Resource name/shape matches the conceptual name remains JIT detail.

## COMM-WD-049 — Mailing-list activation would pull the Privacy & Consent conditional dossier forward before Phase 7C freeze

**Status:** `WORKING_DESIGN_ACCEPTED`

If accountless mailing-list signup is activated in FP-001, Phase 7C would need implementation-grade owner semantics for:

- creation of an explicit marketing-purpose grant for an accountless subject;
- withdrawal and regrant;
- binding the Privacy-owned grant to the accountless contact without transferring ownership;
- contact→Account linkage without creating/transferring/broadening/restoring permission;
- duplicate/reconciliation behaviour when contact and Account relationships converge;
- current-purpose revalidation before delivery.

Current Product/Domain law fixes the ownership and invariants, but does not fully specify the accountless Privacy subject/linkage implementation contract.

That situation exactly matches the current Skeleton's Privacy-dossier trigger: exact entry-purpose, acceptance or withdrawal semantics are needed.

Therefore:

```text
mailing-list not activated
→ Privacy dossier remains CONDITIONAL / not pulled forward

mailing-list activated in FP-001
→ Privacy & Consent JIT dossier becomes REQUIRED before Phase 7C freeze
```

This does not start that dossier now.

## COMM-WD-050 — Marketing permission and Communications preference are orthogonal durable truths

**Status:** `UPSTREAM_DERIVED`

For optional marketing:

```text
Privacy & Consent
    owns purpose-level marketing permission

Communications
    owns channel/category preference
```

Neither can replace the other.

A send is not lawful merely because one is positive.

Conceptually:

```text
current marketing purpose permission
AND applicable current Communications preference
AND current scheduling/delivery policy
→ optional marketing may become dispatch-eligible
```

Subject to all other source/provider guards.

## COMM-WD-051 — Account registration, terms acceptance and email verification do not grant marketing permission

**Status:** `UPSTREAM_DERIVED`

Registration establishes the required Account/service relationship.

It must not infer optional marketing permission from:

- Account creation;
- terms/privacy acceptance;
- verified email;
- preferred language;
- prior product use;
- presence of an email destination.

Marketing permission requires its own explicit Privacy & Consent-owned grant.

## COMM-WD-052 — SubscriberContact destination and canonical Account email remain separate even when textually equal

**Status:** `UPSTREAM_DERIVED`

If the mature/conditional mailing-list branch exists:

```text
Communications subscriber email
!=
Identity canonical Account email
```

even when both currently contain the same address string.

Consequences:

- Identity email change does not silently mutate subscriber-contact destination;
- SubscriberContact preference changes do not mutate Account email;
- marketing withdrawal does not make Account security delivery impossible;
- Account verification does not establish marketing permission;
- a provider bounce on one purpose does not automatically rewrite the other owner's state.

## COMM-WD-053 — Contact-to-Account linking is an association/reconciliation, not authority transfer

**Status:** `UPSTREAM_DERIVED`

Current Product Law explicitly fixes that linking an accountless contact to an Account does not create, transfer, broaden or restore purpose permission.

The same rule applies to Communications preferences.

The link may improve provenance, deduplication or participant management, but cannot make:

```text
Account exists
→ marketing permission exists
```

or:

```text
subscriber opted in
→ Account service/security destination becomes Communications-owned
```

The exact identity/verification guard for establishing the link is not frozen by current authority and remains conditional future JIT detail.

No automatic linking by weak demographic/name match is authorised.

## COMM-WD-054 — Current purpose permission and current preference are revalidated at dispatch authorisation for non-mandatory communication

**Status:** `UPSTREAM_DERIVED`

A MessageIntent may retain the purpose/category/channel provenance that caused its creation, but that historical snapshot is not current send authority.

Immediately before authorising a new provider attempt for optional communication:

```text
re-read current source authority
→ re-read current purpose permission
→ re-read current applicable Communications preference
→ evaluate scheduling policy
→ only then authorise provider attempt
```

Event/callback order does not substitute for current owner state.

## COMM-WD-055 — Optional-purpose withdrawal terminally suppresses pending old marketing intent; later regrant does not revive it automatically

**Status:** `WORKING_DESIGN_ACCEPTED`

If Privacy & Consent commits marketing-purpose withdrawal before a new provider dispatch is authorised:

- pending optional marketing MessageIntents for that withdrawn purpose cannot obtain new dispatch authority;
- queued jobs self-suppress;
- no retry survives the withdrawal;
- later explicit purpose regrant does not autonomously resurrect old suppressed marketing intents.

A new current marketing decision must establish a new intent if communication is still appropriate.

This prevents stale campaign work from becoming current merely because permission later changes again.

## COMM-WD-056 — Scoped preference opt-out suppresses the applicable pending optional intent without changing purpose permission

**Status:** `UPSTREAM_DERIVED` plus working stale-intent specialisation

If the participant opts out of a marketing channel/category before dispatch:

- the applicable pending optional intent cannot obtain a new attempt;
- other purpose permission remains unchanged;
- other unaffected channel/category preferences remain unchanged;
- a later opt-in does not automatically replay old suppressed intent.

This is Communications-owned state and must not write Privacy persistence.

## COMM-WD-057 — Preference re-enable and purpose regrant are prospective authority, not retroactive delivery instructions

**Status:** `WORKING_DESIGN_ACCEPTED`

A current positive permission/preference allows future eligible communications.

It is not an instruction to replay everything suppressed while the state was negative.

This prevents:

- stale campaign resurrection;
- post-withdrawal surprise delivery;
- old reminder delivery after its business context is obsolete.

A current source/journey decision must still justify a new MessageIntent.

## COMM-WD-058 — Provider unsubscribe/subscription state is evidence, not NewYou permission authority

**Status:** `UPSTREAM_DERIVED`

Provider callback/dashboard state cannot independently:

- grant marketing permission;
- withdraw Privacy purpose permission;
- change Communications channel/category preference;
- restore either truth.

Where a provider-hosted unsubscribe interaction is ever used, its participant-visible semantics and owner-routed platform action must be explicit.

The provider's own suppression list may constrain physical delivery, but it remains an external delivery condition, not NewYou business permission.

## COMM-WD-059 — Mandatory FP-001 security/account communication is not governed by optional marketing permission

**Status:** `UPSTREAM_DERIVED`

A participant who has:

- never granted marketing permission;
- withdrawn marketing permission;
- opted out of marketing email;
- paused optional marketing

may still receive a required verification/recovery/email-change/security message where Product/source authority requires it.

Conversely, marketing permission cannot create authority to send a security message whose Identity source obligation does not exist.

Purpose/category classification therefore precedes preference evaluation.

## COMM-WD-060 — Quiet hours and frequency caps are dispatch-policy controls, not source truth

**Status:** `WORKING_DESIGN_ACCEPTED`

Quiet hours and frequency caps can determine **when or whether an optional communication may be dispatched under current policy**.

They do not change:

- Identity proof validity;
- originating business facts;
- Privacy purpose permission;
- Account canonical email;
- provider delivery evidence.

Conceptually they add an orthogonal delivery-policy result:

```text
ELIGIBLE_NOW
DEFER_BY_POLICY
SUPPRESS_BY_POLICY
```

Exact policy enums, windows, timezone rules and cap values remain downstream.

## COMM-WD-061 — Security abuse throttles, participant frequency caps and provider throughput limits are three different mechanisms

**Status:** `WORKING_DESIGN_ACCEPTED`

Do not collapse:

1. `OQ-035` / Identity-security abuse controls on registration/recovery/resend requests;
2. Communications participant-facing quiet hours/frequency caps for message overload;
3. provider/backlog throughput/rate control protecting the delivery dependency.

One may cause another operation to wait, but none becomes authority for the others.

In particular, a marketing frequency cap cannot replace resend-abuse protection, and provider throttling cannot create a participant preference.

## COMM-WD-062 — Mandatory does not mean “ignore every scheduling/risk rule”

**Status:** `WORKING_DESIGN_ACCEPTED`

A required security/transactional communication cannot be suppressed by an optional marketing preference.

However, this does not pre-decide:

- which security notices are urgent;
- whether a non-urgent mandatory notice may be deferred by quiet hours;
- provider outage behaviour;
- abuse throttling;
- channel fallback.

Those remain governed by the message role plus `OQ-036` and applicable source/security policy.

This avoids the opposite overreach: treating every `security` label as unlimited immediate send authority.

## COMM-WD-063 — Cross-purpose deduplication is forbidden

**Status:** `WORKING_DESIGN_ACCEPTED`

Two messages to the same textual email address are not duplicates merely because destination and time overlap.

Examples:

- marketing newsletter;
- verification;
- password reset;
- old-address security notice.

Logical deduplication remains source obligation + communication role/purpose.

A marketing opt-out cannot suppress a security intent by accidental destination-level dedupe.

## COMM-WD-064 — Channel fallback cannot widen permission

**Status:** `UPSTREAM_DERIVED`

If an optional email marketing message cannot be delivered or email preference is disabled:

- do not silently fall back to SMS/WhatsApp;
- do not infer consent from phone presence;
- do not infer channel permission from broad marketing permission alone.

Future SMS/WhatsApp requires its applicable purpose/channel permission, preference and provider policy.

For required FP-001 security communication, exact alternate-channel policy remains `OQ-036`; no fallback is assumed.

## COMM-WD-065 — Preference updates require durable concurrency semantics but not necessarily a separate Resource

**Status:** `WORKING_DESIGN_ACCEPTED`

Where Communications preferences are introduced, simultaneous participant edits must converge under one authoritative current preference result.

A stale edit must not silently overwrite a newer scoped opt-out/opt-in.

The exact representation may be:

- fields/substructure on `SubscriberContact` for a narrow email-only acquisition slice; or
- a separate `NotificationPreference` Resource when independent channel/category lifecycle, query, indexing, versioning or reuse justifies it.

Therefore the **preference concept** can become required while a **separate Resource** remains unproven.

## COMM-WD-066 — Unsubscribe is not contact deletion

**Status:** `UPSTREAM_DERIVED`

These remain separate:

```text
channel/category opt-out
purpose-level marketing withdrawal
contact deletion/data lifecycle
Account closure
full deletion
```

A preference/purpose withdrawal may require retention of minimum suppression truth so the platform does not accidentally resume optional marketing.

It does not automatically erase every contact/provider evidence record.

Exact retention is governed by Privacy/data-lifecycle authority.

## COMM-WD-067 — Unknown/missing timezone does not justify inventing participant locale/timezone authority

**Status:** `WORKING_DESIGN_ACCEPTED`

FP-001 Account registration captures preferred language, not a required participant timezone.

South Africa/Africa-Johannesburg defaults exist at Product level, but Communications must not infer that a stored default is the participant's immutable personal timezone.

For the required FP-001 security path, time-sensitive user-initiated messages should not require a new timezone Resource merely to send.

If a future optional mailing-list/reminder surface depends materially on quiet hours, the exact timezone-source and update semantics must be explicitly specified with that preference capability.

---

# 42. Dispatch-admission refinement — v0.4.0

The cumulative model now has distinct gates.

For a new provider attempt:

```text
A. source obligation / Account / proof disposition
   → ALLOW | SUSPEND | STOP

B. purpose permission
   → REQUIRED_NON_OPTIONAL / CURRENTLY_ALLOWED / CURRENTLY_DENIED

C. Communications channel/category preference
   → NOT_APPLICABLE / CURRENTLY_ALLOWED / CURRENTLY_DENIED

D. scheduling / overload policy
   → ELIGIBLE_NOW / DEFER_BY_POLICY / SUPPRESS_BY_POLICY

E. provider/dependency admission
   → handled by later provider/backlog policy

A+B+C+D(+E)
→ new DeliveryAttempt may or may not be authorised
```

Important rules:

- a mandatory security message can use `B = REQUIRED_NON_OPTIONAL` and `C = NOT_APPLICABLE`;
- optional marketing requires current positive purpose permission **and** current applicable preference;
- `DEFER_BY_POLICY` creates no provider attempt yet;
- `STOP`, denied permission or denied applicable preference prevents a new attempt;
- no gate can manufacture the truth owned by another gate;
- an already-authorised in-flight provider operation retains the v0.2/v0.3 ambiguity/reconciliation rules.

This is conceptual JIT shape, not an exact enum/table/API prescription.

---

# 43. Pressure-test register — fourth cluster

## COMM-PT-053 — Product permits mailing-list signup but FP-001 outcome does not promise it

- **Scenario:** mature Product Law says a public visitor may join the mailing list without an Account.
- **Authority involved:** Product §7.3 / DEC-017; Roadmap FP-001; Skeleton; Atlas CAP-005; FES.
- **Durable truths and owner:** accountless contact would belong to Communications if activated.
- **Concurrency/retry/reordering/crash behaviour:** none needed to resolve scope.
- **Rejected models:** every Product-level capability mentioned by an authority anchor is automatically required in FP-001; omit the mailing-list seam from consideration entirely.
- **Required invariant:** Feature Pack scope follows its governed outcome/exit and explicit conditional capability routing.
- **Recommended JIT shape:** required dossier excludes SubscriberContact; retain explicit conditional activation seam.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO at current scope.
- **Later executable proof:** none until mailing-list surface is actually selected.
- **Verdict:** PASS.

## COMM-PT-054 — FP-001 Final Contract explicitly chooses to ship public mailing-list signup

- **Scenario:** later Phase 7C selects the optional permissioned-email acquisition surface already permitted by Product/CAP-005.
- **Authority involved:** Communications subscriber ownership; Privacy marketing permission; CAP-005 conditional lifecycle.
- **Durable truths and owner:** SubscriberContact/preference = Communications; marketing purpose grant = Privacy & Consent.
- **Concurrency/retry/reordering/crash behaviour:** signup changes two independently owned durable truths.
- **Rejected models:** use Account as prerequisite; store marketing consent on SubscriberContact; pretend MessageIntent is the subscriber relationship; silently add the surface without conditional-dossier review.
- **Required invariant:** contact and permission remain separate owners; optional delivery requires both current.
- **Recommended JIT shape:** conditionally introduce SubscriberContact + preference concept and pull Privacy JIT forward.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO Product amendment currently required; explicit Feature Pack activation required.
- **Conditional dossier pulled forward:** **YES — Privacy & Consent if this branch is selected.**
- **Later executable proof:** signup partial failure, duplicate signup, withdrawal, link-to-Account, current permission recheck.
- **Verdict:** CONDITIONAL PASS.

## COMM-PT-055 — Two concurrent accountless mailing-list signups use the same destination

- **Scenario:** double-click/two tabs/replayed HTTP request.
- **Authority involved:** Communications SubscriberContact; Privacy purpose grant if branch active.
- **Durable truths and owner:** one current contact relationship for the same governed contact identity; purpose history remains Privacy-owned.
- **Concurrency/retry/reordering/crash behaviour:** duplicate contact/grant operations may race.
- **Rejected models:** create duplicate SubscriberContacts and independently market both; provider dedupe is business uniqueness.
- **Required invariant:** equivalent contact creation converges and does not multiply optional delivery.
- **Recommended JIT shape:** durable contact identity/idempotency + owner-mediated Privacy grant; exact normalisation/constraint deferred.
- **Conclusion:** `OPEN_HYPOTHESIS` for exact contact identity; lifecycle requirement accepted conditionally.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy required only if branch selected.
- **Later executable proof:** concurrent same-destination signup and repeated grant request.
- **Verdict:** CONDITIONAL / EXACT CONTACT IDENTITY JIT DETAIL.

## COMM-PT-056 — Communications contact commits but Privacy marketing grant fails

- **Scenario:** cross-domain mailing-list signup partially succeeds.
- **Authority involved:** Communications contact ownership; Privacy permission ownership.
- **Durable truths and owner:** contact may exist without marketing send authority.
- **Concurrency/retry/reordering/crash behaviour:** crash/failure between owner transitions.
- **Rejected models:** contact existence implies permission; delete unrelated contact history to fabricate atomicity; send while grant is unknown.
- **Required invariant:** no optional marketing until current Privacy permission is positively established.
- **Recommended JIT shape:** durable partial/pending relationship is safe; retry/reconcile Privacy grant or surface failure.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy YES if branch active.
- **Later executable proof:** crash after contact commit, before grant; zero marketing dispatch.
- **Verdict:** PASS CONDITIONALLY.

## COMM-PT-057 — Privacy grant commits but Communications contact/preference creation fails

- **Scenario:** the opposite cross-domain partial failure.
- **Authority involved:** Privacy marketing purpose; Communications destination/preference.
- **Durable truths and owner:** permission alone has no deliverable contact/preference.
- **Concurrency/retry/reordering/crash behaviour:** retry may later create contact.
- **Rejected models:** Privacy grant contains destination/contact authority; provider list becomes SubscriberContact authority.
- **Required invariant:** no send until both independent truths are current and linked lawfully.
- **Recommended JIT shape:** reconcile/complete Communications side with stable operation provenance; no guessed destination.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy YES if branch active.
- **Later executable proof:** grant-only state remains non-deliverable; duplicate repair converges.
- **Verdict:** PASS CONDITIONALLY.

## COMM-PT-058 — Account registration uses the same email as an existing accountless subscriber

- **Scenario:** mailing-list contact later creates a full Account.
- **Authority involved:** Communications contact; Privacy permission; Identity Account.
- **Durable truths and owner:** three separate authorities.
- **Concurrency/retry/reordering/crash behaviour:** registration/linking may race preference/permission changes.
- **Rejected models:** registration creates marketing permission; subscriber contact becomes canonical Account email; automatically delete contact and copy its state onto Account.
- **Required invariant:** linking changes neither marketing purpose nor channel/category preference by itself.
- **Recommended JIT shape:** optional association/reconciliation only; each owner retains existing truth.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy YES only if mailing-list branch active.
- **Later executable proof:** registration while subscribed/unsubscribed/withdrawn.
- **Verdict:** PASS.

## COMM-PT-059 — New Account has verified email but no marketing permission

- **Scenario:** participant completes required registration and email verification without marketing opt-in.
- **Authority involved:** Identity versus Privacy/Communications.
- **Durable truths and owner:** verified email = Identity; marketing permission = Privacy; preference/contact if applicable = Communications.
- **Concurrency/retry/reordering/crash behaviour:** none material.
- **Rejected models:** verified email implies marketable email; terms/privacy acceptance implies optional marketing.
- **Required invariant:** no optional marketing send authority.
- **Recommended JIT shape:** required security delivery uses Account destination; optional marketing requires separate grant.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO for required FP-001.
- **Later executable proof:** verified Account with absent marketing grant receives security mail but no optional marketing.
- **Verdict:** PASS.

## COMM-PT-060 — Same email is opted out for marketing while a verification/reset message is required

- **Scenario:** accountless or Account-linked marketing preference denies email marketing.
- **Authority involved:** Communications preference + Identity source obligation.
- **Durable truths and owner:** marketing preference does not own security source.
- **Concurrency/retry/reordering/crash behaviour:** preference may change while security job is queued.
- **Rejected models:** destination-level global suppression blocks all email; one provider suppression flag becomes all-purpose authority.
- **Required invariant:** optional marketing remains suppressed while required security can proceed under its own source/channel policy.
- **Recommended JIT shape:** purpose/category-aware dispatch admission; no cross-purpose dedupe.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** marketing opt-out + verification/reset dispatch.
- **Verdict:** PASS.

## COMM-PT-061 — Marketing permission is active but email marketing preference is opted out

- **Scenario:** broad Privacy permission remains active; Communications email/category preference is negative.
- **Authority involved:** DEC-304 / §21S.
- **Durable truths and owner:** permission and preference independent.
- **Concurrency/retry/reordering/crash behaviour:** stale job may predate opt-out.
- **Rejected models:** broad purpose permission overrides channel opt-out.
- **Required invariant:** email marketing cannot obtain new dispatch authority.
- **Recommended JIT shape:** current preference recheck immediately before attempt authorisation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** only if mailing-list/marketing branch selected.
- **Later executable proof:** queued optional email after scoped opt-out self-suppresses.
- **Verdict:** PASS.

## COMM-PT-062 — Email marketing preference is active but purpose-level marketing permission was withdrawn

- **Scenario:** preference says yes; Privacy says no.
- **Authority involved:** Privacy purpose withdrawal.
- **Durable truths and owner:** withdrawal suppresses all optional marketing across channels.
- **Concurrency/retry/reordering/crash behaviour:** provider/channel jobs may still exist.
- **Rejected models:** preference overrides Privacy; provider list membership restores permission.
- **Required invariant:** no optional marketing across channels.
- **Recommended JIT shape:** purpose check precedes/combines with channel preference.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** only if branch selected.
- **Later executable proof:** preference positive + purpose withdrawn yields zero new provider attempts.
- **Verdict:** PASS.

## COMM-PT-063 — Purpose withdrawal races queued optional marketing dispatch

- **Scenario:** worker and Privacy withdrawal execute concurrently.
- **Authority involved:** Privacy current authority; Communications dispatch authorisation.
- **Durable truths and owner:** withdrawal = Privacy; attempt = Communications.
- **Concurrency/retry/reordering/crash behaviour:** same ordering class as Identity invalidation.
- **Rejected models:** job admission at creation is permanent permission; event order decides.
- **Required invariant:** withdrawal winning before dispatch authorisation blocks send; already-authorised in-flight attempt may complete physically but cannot be retried afterward.
- **Recommended JIT shape:** current Privacy authority participates in new-attempt authorisation.
- **Conclusion:** `UPSTREAM_DERIVED` plus working concurrency specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy if branch selected.
- **Later executable proof:** both interleavings and late provider response.
- **Verdict:** PASS.

## COMM-PT-064 — Scoped preference opt-out races queued optional marketing dispatch

- **Scenario:** participant opts out of email/category while worker is preparing send.
- **Authority involved:** Communications preference authority.
- **Durable truths and owner:** preference + intent/attempt all Communications-owned but independent concepts.
- **Concurrency/retry/reordering/crash behaviour:** same-node and cross-node updates.
- **Rejected models:** stale worker preference cache; provider send list as authoritative preference.
- **Required invariant:** opt-out winning before dispatch authorisation prevents new attempt; in-flight attempt is reconciled but not retried.
- **Recommended JIT shape:** version/current-state check in dispatch authorisation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** no additional dossier beyond branch's Privacy need.
- **Later executable proof:** deterministic both-order race.
- **Verdict:** PASS.

## COMM-PT-065 — Purpose is withdrawn, then explicitly regranted before an old queued job executes

- **Scenario:** old marketing MessageIntent survived technical queue delay.
- **Authority involved:** Privacy grant history + Communications intent provenance.
- **Durable truths and owner:** regrant is new current purpose authority; old intent was suppressed under prior authority.
- **Concurrency/retry/reordering/crash behaviour:** stale old job wakes after regrant.
- **Rejected models:** regrant revives every pre-withdrawal marketing intent.
- **Required invariant:** old suppressed intent stays terminal for new dispatch; future marketing requires a current new intent.
- **Recommended JIT shape:** suppression records causal authority/version; new grant is prospective.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy if branch selected.
- **Later executable proof:** withdrawal→regrant→late old job.
- **Verdict:** PASS.

## COMM-PT-066 — Scoped opt-out is later reversed before old queued message executes

- **Scenario:** participant re-enables marketing email.
- **Authority involved:** Communications preference lifecycle.
- **Durable truths and owner:** current preference positive; prior suppressed intent still stale.
- **Concurrency/retry/reordering/crash behaviour:** old job may wake after opt-in.
- **Rejected models:** preference re-enable is an instruction to replay stale mail.
- **Required invariant:** new/current source decision required for send.
- **Recommended JIT shape:** re-enable prospective only.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO additional.
- **Later executable proof:** opt-out→opt-in→old job produces no send.
- **Verdict:** PASS.

## COMM-PT-067 — Provider reports unsubscribe/suppression state

- **Scenario:** provider webhook/dashboard says destination unsubscribed.
- **Authority involved:** DEC-304; Communications provider evidence; Privacy permission.
- **Durable truths and owner:** provider state = external evidence only.
- **Concurrency/retry/reordering/crash behaviour:** callback may duplicate/reorder around platform changes.
- **Rejected models:** callback silently withdraws purpose permission; callback silently creates NewYou preference; provider re-subscribe restores permission.
- **Required invariant:** owner-routed platform action is required for platform-state change.
- **Recommended JIT shape:** record minimal provider evidence; reconcile provider delivery limitation without elevating it to permission authority.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO beyond optional branch.
- **Later executable proof:** duplicate/reordered provider unsubscribe evidence cannot rewrite platform permission.
- **Verdict:** PASS; exact provider UX/API remains OQ-036.

## COMM-PT-068 — UI exposes one ambiguous “unsubscribe” action

- **Scenario:** participant cannot tell whether it means email-category opt-out or all-marketing purpose withdrawal.
- **Authority involved:** Product §21S / DEC-304.
- **Durable truths and owner:** two different owners/states.
- **Concurrency/retry/reordering/crash behaviour:** not material.
- **Rejected models:** infer scope from backend route or whichever state is easiest to update.
- **Required invariant:** participant action clearly states which durable truth changes.
- **Recommended JIT shape:** distinct owner-routed actions and safe response semantics.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy if mailing-list marketing UI is selected.
- **Later executable proof:** UI/action contract tests mapping visible action to one owner mutation.
- **Verdict:** PASS / AMBIGUOUS UI MODEL REJECTED.

## COMM-PT-069 — Accountless contact is linked to an Account while still actively subscribed

- **Scenario:** same participant later registers/logs in and the system establishes an approved contact↔Account link.
- **Authority involved:** Communications contact; Identity Account; Privacy marketing grant.
- **Durable truths and owner:** link does not transfer any owner truth.
- **Concurrency/retry/reordering/crash behaviour:** linking can race permission/preference update.
- **Rejected models:** copy purpose permission onto Account; convert SubscriberContact into Account email; drop contact preference.
- **Required invariant:** current permission/preference remains unchanged; source references stay traceable.
- **Recommended JIT shape:** association only; exact guard/reconciliation future JIT.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy if branch selected.
- **Later executable proof:** linking under active/withdrawn/opted-out states.
- **Verdict:** PASS.

## COMM-PT-070 — Contact↔Account linking races purpose withdrawal

- **Scenario:** linkage and Privacy withdrawal happen concurrently.
- **Authority involved:** Privacy current permission; Communications association.
- **Durable truths and owner:** link cannot manufacture permission.
- **Concurrency/retry/reordering/crash behaviour:** event order may differ.
- **Rejected models:** link snapshots prior permission and keeps it active; copy-before-withdraw bypass.
- **Required invariant:** current Privacy withdrawal wins for optional future marketing regardless of link ordering.
- **Recommended JIT shape:** delivery always reads current purpose authority; link contains no grant.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy if branch selected.
- **Later executable proof:** both link/withdraw orderings.
- **Verdict:** PASS.

## COMM-PT-071 — Linked Account changes canonical email

- **Scenario:** Identity changes Account email from A to B; SubscriberContact still points at A.
- **Authority involved:** Identity canonical email; Communications subscriber contact.
- **Durable truths and owner:** independent destinations.
- **Concurrency/retry/reordering/crash behaviour:** marketing job may be queued to A; security message may target B/old A according to source role.
- **Rejected models:** silently mutate subscriber contact to B; silently copy marketing permission to B; make marketing destination follow canonical email automatically.
- **Required invariant:** contact destination changes only through an authorised Communications/contact action.
- **Recommended JIT shape:** explicit link remains but destinations independent.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** no extra beyond branch.
- **Later executable proof:** Identity email change leaves contact/preference/permission untouched.
- **Verdict:** PASS.

## COMM-PT-072 — Optional marketing intent becomes eligible during quiet hours

- **Scenario:** purpose and preference allow, but participant/timezone policy says do not send now.
- **Authority involved:** Communications quiet-hour policy.
- **Durable truths and owner:** intent remains unresolved; no provider attempt yet.
- **Concurrency/retry/reordering/crash behaviour:** worker can restart/reorder across quiet-hour boundary.
- **Rejected models:** create failed DeliveryAttempt; busy-loop retries; bypass quiet hours because intent is durable.
- **Required invariant:** defer without provider attempt and re-evaluate current permission/preference when eligible time arrives.
- **Recommended JIT shape:** policy-deferred MessageIntent scheduling; exact schedule mechanism later.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** only if such optional messaging is activated.
- **Later executable proof:** quiet-hour entry/exit, restart and withdrawal during deferral.
- **Verdict:** PASS.

## COMM-PT-073 — User requests password reset during configured quiet hours

- **Scenario:** time-sensitive required security action occurs at night.
- **Authority involved:** Identity source obligation; Product mandatory/non-urgent distinction; OQ-036.
- **Durable truths and owner:** reset proof lifecycle belongs to Identity; Communications delivery is required for that requested path.
- **Concurrency/retry/reordering/crash behaviour:** proof may expire before quiet hours end.
- **Rejected models:** blindly delay every message under quiet hours; participant preference makes reset impossible; silently extend proof lifetime.
- **Required invariant:** quiet-hour policy cannot make an explicitly requested time-bounded security path unusable.
- **Recommended JIT shape:** treat reset/verification role according to governed urgency/mandatory policy; do not alter proof expiry.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED` at invariant level; exact role policy remains `OPEN_HYPOTHESIS` / OQ-036.
- **Upstream amendment:** NO currently.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** time-bounded proof cannot be trapped behind optional quiet-hour policy.
- **Verdict:** PASS WITH OQ-036 DETAIL OPEN.

## COMM-PT-074 — Optional messages hit participant frequency cap

- **Scenario:** several permitted optional messages would exceed current cap.
- **Authority involved:** Communications frequency-cap policy.
- **Durable truths and owner:** source facts remain true; current message may defer/suppress according to policy.
- **Concurrency/retry/reordering/crash behaviour:** concurrent workers can race cap accounting.
- **Rejected models:** each worker checks stale count and all send; provider throttle is the cap; Redis counter becomes durable business authority without justification.
- **Required invariant:** cap enforcement is concurrency-correct for the promised policy.
- **Recommended JIT shape:** authoritative/durable policy accounting sufficient for correctness; exact storage/acceleration later.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED` for future optional branch.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO additional.
- **Later executable proof:** concurrent cap-bound sends across nodes.
- **Verdict:** PASS CONDITIONALLY.

## COMM-PT-075 — Required security messages occur after optional-message frequency cap is exhausted

- **Scenario:** participant has received the maximum optional communications but initiates recovery.
- **Authority involved:** Product mandatory notices versus frequency caps.
- **Durable truths and owner:** optional overload policy cannot manufacture/deny source security truth.
- **Concurrency/retry/reordering/crash behaviour:** cap accounting and security intent overlap.
- **Rejected models:** one universal send-count cap suppresses password reset/security notice.
- **Required invariant:** required security role follows its own governed policy and is not blocked merely by optional marketing/programme volume.
- **Recommended JIT shape:** category/purpose-aware caps; mandatory role explicitly classified.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** exhausted optional cap + required verification/recovery.
- **Verdict:** PASS.

## COMM-PT-076 — Optional email is disallowed; system has a phone number

- **Scenario:** email preference off or provider delivery fails; phone exists on Account/contact.
- **Authority involved:** Product channel/consent separation and OQ-036.
- **Durable truths and owner:** phone presence is not SMS/WhatsApp permission.
- **Concurrency/retry/reordering/crash behaviour:** fallback logic may run after email failure.
- **Rejected models:** opportunistic SMS/WhatsApp fallback; infer preference/consent from available destination.
- **Required invariant:** no channel widening without current applicable permission/preference and approved provider/channel policy.
- **Recommended JIT shape:** channel-specific admission; future adapters remain gated.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** possibly Privacy if optional multi-channel marketing is activated; not FP-001 required.
- **Later executable proof:** email failure cannot trigger unauthorised alternate channel.
- **Verdict:** PASS.

## COMM-PT-077 — Two devices edit the same scoped preference concurrently

- **Scenario:** one turns marketing email off while another submits an older preference form.
- **Authority involved:** Communications preference authority.
- **Durable truths and owner:** one current scoped preference.
- **Concurrency/retry/reordering/crash behaviour:** stale optimistic write/reordered HTTP completion.
- **Rejected models:** last network response blindly wins; provider list decides.
- **Required invariant:** current preference update uses version/conditional semantics or equivalent conflict-safe owner action.
- **Recommended JIT shape:** stale update rejected/rebased; exact UX and storage later.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** only if preferences activated.
- **Later executable proof:** concurrent preference mutations.
- **Verdict:** PASS.

## COMM-PT-078 — Participant withdraws all marketing but contact record is retained for suppression/provenance

- **Scenario:** platform needs minimum state to avoid accidental re-marketing.
- **Authority involved:** Privacy purpose withdrawal + Communications contact data lifecycle.
- **Durable truths and owner:** withdrawal != deletion; suppression truth may remain under approved policy.
- **Concurrency/retry/reordering/crash behaviour:** old provider callbacks/queued intents may arrive.
- **Rejected models:** delete all state and later treat same address as fresh permission; retain full contact forever.
- **Required invariant:** retained state is minimum/approved and cannot grant delivery.
- **Recommended JIT shape:** separate permission/preference/data-lifecycle states.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO; exact retention remains Privacy policy.
- **Conditional dossier pulled forward:** Privacy if mailing-list branch selected.
- **Later executable proof:** suppression survives stale job/provider callback and does not become marketing authority.
- **Verdict:** PASS.

## COMM-PT-079 — Same destination has accountless marketing relationship and Account security obligation simultaneously

- **Scenario:** newsletter and reset/verification target the same email.
- **Authority involved:** Privacy marketing purpose; Communications preference; Identity security source.
- **Durable truths and owner:** distinct purposes/logical obligations.
- **Concurrency/retry/reordering/crash behaviour:** jobs may run together.
- **Rejected models:** destination-only dedupe; marketing opt-out suppresses security; security delivery reactivates marketing.
- **Required invariant:** each intent evaluates its own purpose/source policy.
- **Recommended JIT shape:** communication role/purpose in MessageIntent identity/admission.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO for security path.
- **Later executable proof:** simultaneous optional + required intent to same destination.
- **Verdict:** PASS.

## COMM-PT-080 — Quiet-hour timezone is absent or changes while optional intent waits

- **Scenario:** accountless contact has no reliable personal timezone, or participant changes timezone/profile context.
- **Authority involved:** Communications preference policy; Product SA default.
- **Durable truths and owner:** a platform default is not necessarily participant-declared preference.
- **Concurrency/retry/reordering/crash behaviour:** scheduled eligibility may become stale.
- **Rejected models:** add required timezone to FP-001 Account solely for Communications; persist guessed timezone as immutable participant truth.
- **Required invariant:** policy uses an explicit known/default source and re-evaluates before delayed send; absence cannot silently violate the published quiet-hour contract.
- **Recommended JIT shape:** exact timezone-source rules only when quiet-hour-enabled optional communication is activated.
- **Conclusion:** `OPEN_HYPOTHESIS` outside required FP-001.
- **Upstream amendment:** NO now.
- **Conditional dossier pulled forward:** NO now.
- **Later executable proof:** depends on future preference implementation.
- **Verdict:** DEFER / NOT FP-001 REQUIRED.

## COMM-PT-081 — Business action completes while an optional reminder is deferred

- **Scenario:** quiet-hours/frequency policy delays a reminder, then the action being reminded about is completed.
- **Authority involved:** originating Domain current truth; Product “completed actions suppress obsolete reminders”.
- **Durable truths and owner:** completion belongs to source Domain; Communications owns pending reminder intent.
- **Concurrency/retry/reordering/crash behaviour:** completion can race delayed worker.
- **Rejected models:** scheduled time is permanent send authority; stale reminder sends because preference still allows.
- **Required invariant:** source-current completion invalidates/suppresses obsolete reminder before new dispatch.
- **Recommended JIT shape:** source precondition revalidation; no new Resource.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** complete action before/at deferred send.
- **Verdict:** PASS / FUTURE REMINDER CLASS.

## COMM-PT-082 — Mailing-list contact opts out while a required Account security message is provider-throttled

- **Scenario:** same email, two purposes; optional preference changes while provider backlog delays required mail.
- **Authority involved:** Communications preference + Identity required source + provider admission.
- **Durable truths and owner:** opt-out affects only optional scope.
- **Concurrency/retry/reordering/crash behaviour:** shared provider queue can reorder work.
- **Rejected models:** global destination suppression in application; security retry cancelled by marketing opt-out.
- **Required invariant:** category/purpose isolation survives shared provider/backlog infrastructure.
- **Recommended JIT shape:** policy-aware queue execution; provider physical suppression constraints reconciled separately.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO for required FP-001.
- **Later executable proof:** mixed-purpose backlog and preference mutation.
- **Verdict:** PASS.

## COMM-PT-083 — Contact is linked to Account A, then later evidence suggests Account B is the same human

- **Scenario:** duplicate/reconciliation ambiguity intersects SubscriberContact.
- **Authority involved:** Identity reconciliation; Communications contact association; Privacy permission.
- **Durable truths and owner:** contact association cannot resolve human identity or transfer permission.
- **Concurrency/retry/reordering/crash behaviour:** candidate merge can be unresolved for long period.
- **Rejected models:** move contact to likely survivor before Identity apply; duplicate permission across Accounts.
- **Required invariant:** candidate/conflicted Identity evidence does not rewrite Communications/Privacy ownership.
- **Recommended JIT shape:** wait for applied Identity reconciliation; exact post-merge association is future JIT.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** only if mailing-list branch active.
- **Later executable proof:** candidate/rejected/applied merge.
- **Verdict:** PASS.

## COMM-PT-084 — Mailing-list signup asks for one checkbox labelled “email updates” but product later wants categories

- **Scenario:** narrow capture UI precedes mature category preferences.
- **Authority involved:** DEC-262/304; Communications preference ownership; Privacy purpose permission.
- **Durable truths and owner:** permission scope and preference scope must be explicit enough to avoid retroactive broadening.
- **Concurrency/retry/reordering/crash behaviour:** later category expansion.
- **Rejected models:** old generic opt-in automatically authorises every future marketing category/channel; treat UI wording as unlimited grant.
- **Required invariant:** later category/channel expansion cannot silently broaden historic permission/preference scope.
- **Recommended JIT shape:** versioned/scoped grant and preference semantics if mailing-list branch is activated.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO; legal/expert sufficiency still separate.
- **Conditional dossier pulled forward:** Privacy YES if this branch is activated.
- **Later executable proof:** historic grant/preference under later category additions.
- **Verdict:** PASS CONDITIONALLY.

---

# 44. Rejected-model register additions — v0.4.0

41. **DEC-017 means FP-001 must implement mailing-list signup.** Rejected: Product permission is broader than the Roadmap outcome; Atlas makes subscriber lifecycle conditional.
42. **Ignore mailing-list semantics entirely because the current outcome does not require them.** Rejected: CAP-005 explicitly preserves the conditional seam and it must not be lost.
43. **Use Account as the mailing-list record.** Rejected: Product explicitly allows accountless contact.
44. **Use SubscriberContact as marketing-consent authority.** Rejected: Privacy & Consent solely owns purpose permission.
45. **Store marketing permission as a Communications preference flag.** Rejected.
46. **Account creation/verification implies marketing permission.** Rejected.
47. **Terms/privacy acceptance implies marketing permission.** Rejected.
48. **Linking contact to Account transfers/restores permission.** Rejected by Product Law.
49. **Identity email change silently updates subscriber contact destination.** Rejected.
50. **Provider unsubscribe callback directly mutates platform permission.** Rejected.
51. **Provider re-subscription restores platform marketing permission.** Rejected.
52. **One ambiguous “unsubscribe” action can mutate whichever owner is convenient.** Rejected.
53. **Preference/purpose state is checked only when MessageIntent is created.** Rejected for non-mandatory delivery.
54. **Purpose regrant or preference re-enable automatically replays previously suppressed marketing intents.** Rejected.
55. **Marketing opt-out globally suppresses required security/account communication.** Rejected.
56. **Every mandatory message bypasses quiet hours, provider limits and abuse controls by definition.** Rejected; exact urgency policy remains governed.
57. **One universal frequency cap covers marketing, reminders, verification and recovery alike.** Rejected.
58. **Frequency caps are equivalent to OQ-035 abuse throttling.** Rejected.
59. **Provider rate limiting is a participant preference.** Rejected.
60. **Fall back to SMS/WhatsApp merely because a phone number exists.** Rejected.
61. **Destination-only dedupe across marketing and security messages.** Rejected.
62. **A separate NotificationPreference Resource is mandatory merely because the mature Domain names the concept.** Rejected; concept may be represented more narrowly when/if activated.
63. **Retain full SubscriberContact forever after unsubscribe so suppression is easy.** Rejected without retention authority.
64. **Delete all suppression state on opt-out and later treat the address as brand-new permission.** Rejected.

---

# 45. Upstream-delta register — v0.4.0

## Required upstream amendments

**NONE for the currently required FP-001 Communications outcome.**

The apparent mailing-list tension is resolved by current authority:

```text
Product permits mailing-list relationship
+
Atlas marks subscriber lifecycle conditional
+
Roadmap/Skeleton do not require that acquisition surface
=
SubscriberContact is not required for current FP-001
```

## Conditional scope activation requiring extra Phase 7B work

If FP-001 later explicitly activates public mailing-list signup:

- this is not automatically a Product/Roadmap contradiction because Product Law and `CAP-005` already permit/anticipate it;
- the Final Contract must explicitly state that the conditional acquisition surface is active rather than silently broadening Communications;
- the Communications JIT must include SubscriberContact and preference semantics;
- **Privacy & Consent must be pulled forward as a required conditional dossier before Phase 7C freeze**.

## Unresolved future detail, not an upstream contradiction

- exact contact identity/normalisation and duplicate-contact rule;
- exact accountless-contact ↔ Account linking guard;
- exact initial preference semantics at mailing-list grant;
- exact legal sufficiency / double-opt-in requirements;
- exact timezone/quiet-hour semantics for accountless contacts;
- exact mature preference Resource decomposition.

These must not be invented inside the required security-delivery path.

---

# 46. Unresolved-gate register additions — v0.4.0

| Gate / open matter | v0.4.0 effect |
|---|---|
| Mailing-list acquisition activation | Not part of required FP-001 outcome today. Explicit activation would conditionally expand Communications + require Privacy JIT. |
| Existing legal/privacy expert review for marketing | Product semantics do not establish legal sufficiency. Public marketing activation must still satisfy applicable review. |
| `OQ-035` abuse controls | Verification/reset/recovery resend abuse remains separate from message frequency caps. |
| `OQ-036` provider/channel policy | Exact security-message urgency, provider suppression/list behaviour, provider-hosted unsubscribe integration and alternate-channel policy remain unresolved. |
| Accountless-contact identity | Exact destination normalisation, duplicate identity and link guards are conditional JIT details only if mailing list is activated. |
| Preference physical representation | Preference concept becomes material only with a surface that exposes mutable optional preferences. Separate Ash Resource is not yet justified. |
| Quiet-hour timezone source | Not required by current FP-001 security outcome; specify when a quiet-hour-governed optional surface is activated. |
| Regrant/re-enable source behaviour | Working rule is prospective-only; future campaign/journey JIT may refine source-specific intent creation without reviving stale intents. |

---

# 47. Cross-stream dependency register additions — v0.4.0

| Stream / Domain | v0.4.0 finding |
|---|---|
| Identity & Access | Account email and verification never grant marketing permission or mutate SubscriberContact preference. Security messages remain source-owned even when marketing for the same destination is opted out. |
| Privacy & Consent | Sole owner of marketing-purpose grant/withdrawal/regrant. Becomes a required FP-001 conditional dossier **only if** accountless mailing-list acquisition is activated. |
| Communications | Sole owner of SubscriberContact and channel/category preference where introduced; does not own purpose permission. |
| Content & Media | Marketing/public capture copy and templates still consume governed content; no new C&M lifecycle is required by this cluster alone. |
| Audit & Evidence | Preference/permission audit may be required under existing boundaries but no new Audit semantics were exposed. |
| Analytics | Acquisition evidence cannot establish permission, preference or contact authority. |
| Provider | Subscription/suppression/unsubscribe state is external evidence/physical delivery constraint only. |
| CAP-005 | Public discovery is required; subscriber-contact lifecycle is conditional on selecting the mailing-list relationship. |
| CAP-017 | Required now for security/account delivery even when subscriber/preference concepts remain absent from the FP-001 physical model. |

---

# 48. Conditional-dossier adjudication — v0.4.0

## Privacy & Consent

### Current required FP-001 path

**Disposition: `CONDITIONAL / NOT PULLED FORWARD`.**

Verification/recovery/email-change/security delivery can be fully specified using existing authority without a mutable marketing-purpose workflow.

No marketing permission is inferred or required for those messages.

### Conditional mailing-list branch

**Disposition if activated: `PULL FORWARD / REQUIRED BEFORE PHASE 7C`.**

Reason:

The active Feature Pack would then require implementation-grade Privacy-owned semantics for an accountless subject:

- explicit marketing-purpose grant;
- current permission evaluation;
- withdrawal;
- regrant;
- accountless contact linkage;
- Account-link reconciliation without permission transfer;
- concurrency/partial-failure recovery.

Those are not Communications implementation details and must not be invented by the Communications dossier.

This is the first Pre-JIT cluster to establish a **specific conditional trigger that would change the Privacy dossier disposition**.

It does not change the disposition today because the triggering surface is not currently selected.

## Content & Media

**Disposition: `CONDITIONAL / NOT PULLED FORWARD`.**

Clear unsubscribe/permission wording and marketing templates are content concerns, but existing content version/governance authority is sufficient at this stage.

Pull forward only if the active FP-001 surface requires implementation-grade Content-owned lifecycle semantics beyond existing law.

## Audit & Evidence

**Disposition: `CONDITIONAL / NOT PULLED FORWARD`.**

No new central audit lifecycle was required.

---

# 49. Later executable proof-obligation register additions — v0.4.0

51. Required FP-001 path: prove absence/withdrawal of marketing permission does not suppress verification/reset/recovery/email-change/security delivery.
52. Required FP-001 path: prove marketing email opt-out cannot become destination-global suppression of required security messages.
53. Required FP-001 path: prove security delivery does not grant/restore marketing purpose permission or preference.
54. Required FP-001 path: prove same-destination marketing/security MessageIntents are not cross-purpose deduplicated.
55. Required FP-001 path: verify time-bounded participant-requested security proof is not made unusable by optional quiet-hour policy.
56. If mailing-list branch activates: concurrent duplicate accountless signup converges on one governed contact relationship without duplicate optional sends.
57. If mailing-list branch activates: contact commit + Privacy grant failure yields no optional send.
58. If mailing-list branch activates: Privacy grant commit + contact failure yields no guessed destination/send.
59. If mailing-list branch activates: Account registration with matching subscriber destination creates no permission/preference transfer.
60. If mailing-list branch activates: linking and purpose withdrawal in both orderings yields current withdrawn authority.
61. If mailing-list branch activates: Account email change does not silently retarget subscriber contact.
62. Optional marketing queued before purpose withdrawal cannot obtain new attempt afterward.
63. Optional marketing queued before scoped opt-out cannot obtain new attempt afterward.
64. Purpose regrant cannot revive old pre-withdrawal suppressed MessageIntent.
65. Preference re-enable cannot revive old pre-opt-out suppressed MessageIntent.
66. Duplicate/reordered provider unsubscribe evidence cannot mutate platform permission/preference.
67. Participant-visible unsubscribe controls map unambiguously to the intended owner action.
68. Quiet-hour deferral survives restart and rechecks current purpose/preference/source before eventual attempt.
69. Withdrawal during quiet-hour deferral prevents later send.
70. Frequency-cap enforcement remains concurrency-correct across nodes for any activated optional category.
71. Exhausted optional frequency cap does not suppress required security/recovery.
72. Email channel denial/failure cannot trigger unauthorised SMS/WhatsApp fallback.
73. Concurrent preference edits use conflict-safe current-state semantics.
74. Withdrawn marketing purpose with retained suppression/contact evidence cannot become future permission after restore/relink.
75. Future category/channel expansion cannot silently broaden a historic narrow mailing-list grant/preference.

---

# 50. Resource-discipline review — cumulative through v0.4.0

## Required current FP-001 Resources

### `MessageIntent`

**REQUIRED.**

Nothing in the preference/contact cluster changes this.

For mandatory FP-001 security/account messages it stores/provides the logical communication obligation, source reference, role, destination provenance, durable deduplication and terminal/reconciliation visibility.

### `DeliveryAttempt`

**REQUIRED.**

Provider execution/evidence remains independently durable.

## Conditional mature/acquisition concepts

### `SubscriberContact`

**NOT REQUIRED for the current governed FP-001 outcome.**

**CONDITIONALLY REQUIRED if FP-001 explicitly activates public accountless mailing-list signup.**

Why it would then earn existence:

- independent of Account;
- independent destination/contact lifecycle;
- own Communications preference relationship;
- later Account association without ownership transfer;
- independent data lifecycle.

This is now a precise conditional rather than a blanket rejection.

### `NotificationPreference`

**NOT REQUIRED as a current FP-001 Resource.**

If the conditional mailing-list branch activates:

- a durable Communications-owned preference **concept** becomes required because scoped channel/category opt-out is Product Law;
- a separate Ash Resource is still not automatically justified.

For a narrowly scoped email-only mailing-list slice, the preference may potentially live safely on/under `SubscriberContact` if all lifecycle/concurrency/indexing requirements are preserved.

A separate Resource becomes justified only when independent multi-channel/category lifecycle, versioning, querying, reuse or scale makes that truth materially independent.

### `InAppNotification`

**Still not required.**

Nothing in this cluster changes the FES conclusion that a participant notification centre is not an FP-001 prerequisite.

### `CommunicationJourney`

**Still not required.**

Optional mailing-list contact existence does not itself create a campaign/journey lifecycle.

### `MarketingConsent`

**REJECTED as a Communications Resource.**

That would duplicate Privacy & Consent authority.

### `Unsubscribe`

**REJECTED as a standalone generic Resource/concept.**

An unsubscribe action must resolve to a specific owner transition:

- Communications scoped preference change; or
- Privacy purpose withdrawal.

An ambiguous generic lifecycle would conceal ownership.

### `QuietHour` / `FrequencyCap` standalone Resources

**NOT JUSTIFIED.**

They are Communications preference/policy semantics. A separate Resource requires independent durable lifecycle evidence not currently present.

**Cumulative required-resource verdict for the current FP-001 outcome remains:**

```text
MessageIntent
DeliveryAttempt
```

**Conditional branch verdict:**

```text
if public mailing-list acquisition is explicitly activated:
    + SubscriberContact durable concept
    + Communications preference concept
    + Privacy & Consent JIT dossier
```

---

# 51. Completeness / stabilisation assessment — v0.4.0

**NOT YET STABLE FOR GOVERNED COMMUNICATIONS JIT DOSSIER DRAFTING.**

The preferences/consent/accountless-contact scenario class is provisionally complete enough to stop broadening this branch.

The pressure tests produced one important conditional fork rather than forcing premature Resources into the required FP-001 model:

```text
CURRENT REQUIRED FP-001
→ MessageIntent + DeliveryAttempt
→ no SubscriberContact
→ no NotificationPreference Resource
→ Privacy dossier stays conditional

IF OPTIONAL MAILING-LIST SURFACE IS ACTIVATED
→ SubscriberContact becomes material
→ mutable Communications preference concept becomes material
→ Privacy dossier must be pulled forward
```

No upstream Product/Architecture/Domain/Roadmap amendment is required.

The remaining materially distinct scenario classes are now narrower:

1. **Content / locale / rendering provenance**
   - preferred language and locale capture;
   - locale at intent creation vs render vs send;
   - exact template/content version binding;
   - template correction/withdrawal after intent creation;
   - retries rendering the same logical content versus a later corrected version;
   - secret-bearing interpolation boundary;
   - personal/sensitive payload minimisation;
   - whether Content & Media becomes required.

2. **Provider outage / backlog / operational recovery**
   - long outage and backlog;
   - bounded retry versus indefinite retry;
   - provider-aware backoff;
   - retry storms;
   - provider throttling;
   - fairness / starvation;
   - delayed acceptance;
   - terminal escalation;
   - operator retry/reconciliation controls;
   - cross-node worker concurrency;
   - graceful degradation.

3. **Audit / observability / evidence**
   - provider evidence versus Audit evidence;
   - operator retry/reconciliation evidence;
   - security incident linkage;
   - logs/metrics/traces versus business evidence;
   - sensitive-data/cardinality limits;
   - retention boundaries;
   - whether Audit & Evidence becomes required.

4. **Channel / provider-independent architecture**
   - email-first versus in-app-first;
   - prove no FP-001 in-app inbox is needed;
   - future SMS/WhatsApp seams;
   - provider-independent adapter contract;
   - exact `OQ-036` STOP boundary;
   - batch/fan-out pressure without campaign architecture.

5. **Final cross-cluster adversarial/stabilisation sweep**
   - combine source invalidation + provider ambiguity + closure/deletion + preference change + template withdrawal + outage;
   - search deliberately for scenario classes not reducible to the accepted invariants;
   - only then decide whether broad Communications Pre-JIT discovery has stabilised.

The recommended next substantive pass is **Content / locale / rendering provenance** because it is the next conditional-dossier boundary most capable of forcing a change to the FP-001 dossier set.

---

# 52. v0.5.0 semantic delta — Content, locale, rendering and exact delivery provenance

This successor preserves all accepted v0.1.0–v0.4.0 findings and adds the fifth substantive Communications pressure-test cluster.

The live repository was rechecked immediately before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

This pass uses current authoritative Product / Architecture / Domain / FP-001 / FES material plus the already-stabilised **non-authoritative** Content & Media Pre-JIT compact pack. It does **not** reopen broad Content & Media discovery.

The cluster pressure-tests:

- Communications versus Content & Media ownership of message bodies/templates;
- the certified Identity dossier's current cross-domain wording;
- preferred interface language versus communication-delivery locale;
- content language versus interface language;
- exact governed content/locale version provenance;
- when content binding becomes fixed;
- missing or withdrawn Afrikaans/English variants;
- machine translation;
- content correction/supersession/withdrawal while queued;
- content correction after provider rejection, acceptance, unknown outcome or delivery;
- duplicate/cross-node content binding;
- retry consistency;
- message-role remapping;
- dynamic render inputs;
- destination/event snapshots;
- secret-bearing interpolation;
- rendering failures before provider I/O;
- untrusted dynamic input;
- provider-hosted template drift;
- current C&M eligibility revalidation;
- operator retry after correction;
- historical content provenance and retention;
- whether the FP-001 Content & Media conditional dossier must be pulled forward.

No provider is selected. No exact C&M Ash Resource topology is selected. `OQ-013` is not silently resolved.

---

# 53. Upstream ownership contradiction discovered — STOP on final certification until corrected

## COMM-UPD-001 — certified Identity dossier message-template ownership wording

**Classification:** LOCAL WORKING UPSTREAM-DELTA LABEL ONLY. Not a governed DEC/ARC/OQ/FP identifier.

**Conflict:**

Current certified Identity dossier v0.1.3 says:

> Communications owns subscriber/contact relationship, message body/template, provider and delivery evidence.

Current higher/current authority says the opposite for the governed content body/template:

- Domain Law §6.7: Content & Media owns **message/template content versions**; exact delivery belongs Communications.
- Domain Law §6.15: Communications explicitly does **not** own template/content body versions.
- Architecture §10.4: material mutable message templates are governed versioned content with exact locale/version delivery provenance.
- FP-001 Skeleton §14: Communications may consume governed templates but does not own content body truth.

The Identity dossier separately says Identity owns no content lifecycle, so the problematic phrase is localised to the Communications bullet rather than a broad Identity model.

## Required correction

The smallest safe upstream correction is a narrow Identity dossier PATCH successor that changes the cross-domain sentence to the equivalent of:

> Communications owns subscriber/contact relationship where applicable, MessageIntent, delivery execution/status and provider evidence. Content & Media owns governed message/template content versions. Communications retains exact content/locale delivery provenance and the minimum delivery-instance data needed to execute an authorised message, without acquiring content-template authority.

No Product, Architecture or Domain Law amendment is required.

## Stop effect

This defect does **not** require halting non-authoritative Communications discovery because the higher authority is clear.

It **does** require:

```text
COMMUNICATIONS GOVERNED JIT FINAL CERTIFICATION
→ BLOCKED / STOP on COMM-UPD-001

PHASE 7C FREEZE
→ BLOCKED / STOP on COMM-UPD-001
```

until the certified/current Identity dossier wording is superseded by the narrow correction or the governed process otherwise removes the contradiction.

This Communications working document does not silently repair the Identity artifact.

---

# 54. Accepted working-design register additions — v0.5.0

## COMM-WD-068 — Content authority and delivery authority are separate

**Status:** `UPSTREAM_DERIVED`

For material FP-001 messages:

```text
Content & Media
→ owns governed message-content/template identity, immutable versions,
  locale versions, approval, correction, supersession and withdrawal

Communications
→ owns MessageIntent, content binding/provenance used for that intent,
  delivery execution, DeliveryAttempt and provider evidence
```

Communications may hold a reference/snapshot needed for delivery. That does not make it the content owner.

The current Identity-dossier wording must be corrected under `COMM-UPD-001`.

## COMM-WD-069 — A MessageIntent carries semantic message role and explicit intended delivery locale independently of exact C&M version

**Status:** `WORKING_DESIGN_ACCEPTED`

The logical communication obligation exists before or independently of a particular mutable “latest template”.

The required conceptual inputs include:

- source Domain/source obligation reference;
- communication role;
- intended delivery locale;
- source/destination provenance;
- minimum authorised render-data snapshot;
- protected bearer capability where required.

The message role is stable business meaning such as verification, password reset, recovery, new-address confirmation or old-address security notice.

It is not a provider template id.

Exact physical fields remain JIT detail.

## COMM-WD-070 — Exact C&M content binding becomes durable before the first provider submission, not by dereferencing “latest” on every retry

**Status:** `WORKING_DESIGN_ACCEPTED`

A source transition may establish the durable `MessageIntent` without forcing Identity to own or resolve C&M lifecycle state inside its authoritative transaction.

Before the **first** provider submission for that intent:

```text
MessageIntent role + intended locale
→ C&M current delivery eligibility
→ exact governed shared/message-content version
→ exact approved locale version
→ durable binding
→ DeliveryAttempt authorisation
```

The binding may occur earlier if implementation convenience allows, but provider submission may not occur while it is unresolved.

This keeps the must-not-lose handoff durable while preventing worker-time “latest template” drift.

## COMM-WD-071 — Exact content binding is concurrency-safe and one current binding wins for the attempt sequence

**Status:** `WORKING_DESIGN_ACCEPTED`

If two workers/nodes race first dispatch:

- they must not independently bind different eligible content versions;
- one durable exact binding/current revision wins;
- losing work re-reads the committed binding;
- Oban uniqueness is not business correctness.

Exact PostgreSQL/Ash conditional-update mechanics remain downstream.

## COMM-WD-072 — Intended communication locale is explicit source input; Communications does not infer it from arbitrary content browsing state

**Status:** `WORKING_DESIGN_ACCEPTED`

Product Law distinguishes:

```text
preferred interface language
!=
content language
```

Therefore Communications must not infer a security message locale from:

- the last public article locale viewed;
- browser URL locale alone;
- provider default locale;
- C&M source-language metadata.

For FP-001 Account-originated security communication, the source owner supplies the intended communication locale according to the approved Account/experience rule.

The current Account preferred interface language is the obvious candidate input for that rule, but this Pre-JIT record does not silently redefine “preferred interface language” as a universal marketing/content-language preference.

## COMM-WD-073 — Intended locale is stable for one MessageIntent

**Status:** `WORKING_DESIGN_ACCEPTED`

Changing the Account's preferred interface language does not silently mutate a previously established logical message.

A later **new** source obligation may choose the then-current locale.

For verification specifically:

```text
participant changes language
→ participant requests allowed resend
→ Identity issues/supersedes according to its current resend lifecycle
→ new MessageIntent
→ new intended locale may be selected
```

This preserves deterministic logical-message provenance and avoids one intent changing language mid-retry.

## COMM-WD-074 — C&M delivery eligibility owns the bilingual prerequisite; Communications must not duplicate translation governance

**Status:** `UPSTREAM_DERIVED`

Product Law requires both Afrikaans and English before publication/delivery for registration/authentication, terms/consent, safety and core onboarding.

Therefore Communications should not implement a second translation-approval matrix.

For an FP-001 security message, C&M's exact-version eligibility contract must fail closed when the governing bilingual/approval requirement is not satisfied.

Consequences can include:

```text
CONTENT_BLOCKED / RECONCILIATION_REQUIRED
```

at the Communications intent level, with **no provider attempt**.

Exact status naming remains JIT detail.

## COMM-WD-075 — No silent or machine fallback for critical FP-001 message content

**Status:** `UPSTREAM_DERIVED`

If the intended critical locale is unavailable, unapproved, stale where current authority makes it ineligible, superseded into ineligibility or withdrawn:

- do not silently switch to the other language;
- do not use machine translation;
- do not ask the provider to translate;
- do not manufacture ad-hoc operator copy.

The intent remains blocked/terminal-visible until lawful content becomes available or the source obligation ends.

This is distinct from optional low-risk editorial fallback.

## COMM-WD-076 — Current C&M eligibility is revalidated before every new provider attempt

**Status:** `UPSTREAM_DERIVED`

The exact bound version provides reproducibility, but binding alone is not permanent delivery authority.

Before a **new** provider submission:

```text
exact bound C&M shared/message-content version
+ exact locale version
→ revalidate current C&M delivery eligibility
→ only then authorise DeliveryAttempt
```

A stale PubSub/event/cache saying “still published” cannot preserve authority after withdrawal.

## COMM-WD-077 — Ordinary retry uses the same exact content binding while that binding remains eligible

**Status:** `WORKING_DESIGN_ACCEPTED`

A technical retry of the same logical message does not re-resolve “latest”.

It uses:

- the same logical MessageIntent;
- the same intended locale;
- the same exact C&M content/locale binding;
- the same immutable non-secret render snapshot;
- the same protected bearer material where still valid;
- a new DeliveryAttempt only when a genuinely new provider submission begins.

This is the default retry path.

## COMM-WD-078 — Explicit successor rebinding is allowed only under narrow safe conditions

**Status:** `WORKING_DESIGN_ACCEPTED`

If the bound content becomes ineligible and C&M supplies an exact eligible successor for the same communication role/locale, the **same MessageIntent** may be rebound only when:

1. the underlying source obligation is still valid;
2. no provider outcome remains ambiguous;
3. no already-successful/delivered attempt means the original obligation has already been physically communicated;
4. any previous attempt is definitively non-delivered/failed for retry purposes;
5. the successor relationship/eligibility is explicit, not “latest” discovery;
6. the rebind is durable and preserves prior attempt provenance.

This avoids forcing a new proof/source obligation merely because wording was corrected before successful delivery.

Exact rebinding action/resource topology remains JIT detail.

## COMM-WD-079 — An ambiguous provider outcome blocks content rebinding plus new submission

**Status:** `WORKING_DESIGN_ACCEPTED`

If the previous attempt may already have reached the provider/recipient:

- do not change content version and send again merely because a corrected version now exists;
- reconcile the ambiguous provider operation first;
- preserve old exact attempt provenance.

Otherwise the platform could deliver both old and corrected content without knowing it.

## COMM-WD-080 — Correction after successful delivery creates a new remediation obligation where communication is required

**Status:** `UPSTREAM_DERIVED` plus Communications specialisation

C&M owns the correction/withdrawal declaration.

If old content was already delivered and Product/Safety/Privacy/source policy requires affected participants to be notified, that is a **new communication consequence**, not a rewrite/retry of the historical MessageIntent.

Conceptually:

```text
historical delivered MessageIntent
→ stays historical

C&M correction/withdrawal
→ affected owning Domain determines consequence
→ new authorised remediation MessageIntent where required
```

C&M must not directly mutate foreign business authority.

## COMM-WD-081 — Content withdrawal and source-proof validity are orthogonal

**Status:** `WORKING_DESIGN_ACCEPTED`

A still-valid Identity proof does not authorise delivery of withdrawn message content.

Likewise, valid content does not authorise delivery of an expired/revoked proof.

A new provider attempt requires both:

```text
current source dispatch authority
AND
current C&M content delivery eligibility
```

plus the other v0.4 admission gates where applicable.

## COMM-WD-082 — MessageIntent holds a bounded immutable non-secret render-data snapshot, not arbitrary live Domain reads

**Status:** `WORKING_DESIGN_ACCEPTED`

The message instance may need event-specific data such as:

- source-event timestamp;
- display/given name if actually used;
- old/new address labels where the message semantics require them;
- bounded non-sensitive reason/context identifiers;
- destination provenance.

Those values may be captured as a minimum immutable delivery snapshot where necessary for deterministic rendering.

They are **not** new business authority. They are immutable delivery provenance.

The render executor must not be allowed to fetch arbitrary data from any Domain merely because a template requests it.

## COMM-WD-083 — Protected bearer material is not ordinary render data or C&M content

**Status:** `UPSTREAM_DERIVED`

Verification/reset/recovery/email-change bearer material remains in the certified protected-delivery seam.

C&M templates contain only an approved placeholder/contract for the protected action.

The secret/link material is injected transiently by the purpose-scoped Communications executor for an authorised attempt.

It must not be persisted in:

- C&M content/version fields;
- ordinary MessageIntent render data;
- ordinary DeliveryAttempt fields;
- Oban arguments;
- logs;
- telemetry;
- Audit;
- Analytics;
- provider metadata beyond the minimum unavoidable request.

## COMM-WD-084 — A full rendered secret-bearing message body is not required as ordinary durable Communications truth

**Status:** `WORKING_DESIGN_ACCEPTED`

Exact delivery provenance can be established from:

- exact content version;
- exact locale version;
- exact safe render-data snapshot/provenance;
- exact source obligation;
- DeliveryAttempt/provider evidence;
- protected capability relationship where applicable.

Persisting the full secret-bearing body in ordinary Communications storage would duplicate sensitive material and undermine the protected-delivery boundary.

If a provider necessarily receives the rendered body, that is bounded external execution, not permission to retain another internal plaintext copy indefinitely.

## COMM-WD-085 — DeliveryAttempt records the exact content/locale binding actually used

**Status:** `WORKING_DESIGN_ACCEPTED`

Every provider submission operation must be traceable to the exact governed content/locale version rendered for that operation.

This matters because a MessageIntent can, under `COMM-WD-078`, be explicitly rebound after a definitive non-delivery.

Therefore historical attempt provenance must not rely only on the MessageIntent's **current** binding.

Exact schema remains JIT detail.

## COMM-WD-086 — Rendering failure before provider I/O is not a DeliveryAttempt

**Status:** `WORKING_DESIGN_ACCEPTED`

`DeliveryAttempt` represents a provider/channel submission operation.

If rendering/validation fails before provider I/O starts:

- no provider attempt occurred;
- no DeliveryAttempt should be fabricated merely to record an internal render error;
- MessageIntent remains blocked/retryable/terminal-visible according to the failure;
- operational evidence may record the rendering failure without becoming business authority.

This preserves the meaning of DeliveryAttempt.

## COMM-WD-087 — Message rendering uses closed, typed/allow-listed data contracts and safe encoding

**Status:** `WORKING_DESIGN_ACCEPTED`

A governed message template may not execute arbitrary code, arbitrary database queries or arbitrary cross-Domain field access.

The rendering contract is bounded by the communication role/template contract.

Dynamic participant-controlled strings are context-appropriately encoded/sanitised.

Unknown required placeholders or unsupported template schema fail closed before provider submission.

This is consistent with the stabilised C&M rejection of executable stored content/runtime authority.

## COMM-WD-088 — Provider-hosted template state cannot become C&M content authority

**Status:** `UPSTREAM_DERIVED`

If a future provider supports stored templates, its template id/version is external execution state only.

The platform still retains:

- exact governed NewYou content/locale authority in C&M;
- exact delivery provenance in Communications.

A provider-side edit must not silently change the body of a NewYou message without a corresponding governed platform version.

The exact adapter strategy remains `OQ-036`.

## COMM-WD-089 — C&M events/notifications accelerate invalidation but never replace current eligibility reads

**Status:** `UPSTREAM_DERIVED`

Publication/correction/withdrawal notifications may wake or cancel work promptly.

They may be:

- delayed;
- duplicated;
- missing;
- reordered.

A worker authorising a new provider attempt still evaluates current C&M authority.

## COMM-WD-090 — Communications does not need its own TemplateVersion/RenderedMessage business Resource

**Status:** `WORKING_DESIGN_ACCEPTED`

The existing two-Resource required model still holds.

C&M owns exact governed content versions.

Communications owns:

- MessageIntent;
- DeliveryAttempt;
- bounded immutable delivery snapshots/references.

A separate Communications `TemplateVersion`, `RenderedMessage`, `MessageBody` or `LocaleContent` Resource would duplicate C&M authority or sensitive payload without an independent durable business truth.

## COMM-WD-091 — The current Content & Media conditional FP-001 dossier remains unpulled after this cluster

**Status:** `WORKING_DESIGN_ACCEPTED`

The active Communications path consumes already-frozen semantics:

- C&M owns message content/template versions;
- locale branches are independent;
- exact delivery provenance is required;
- critical bilingual content cannot silently fallback;
- immutable versions are corrected/superseded/withdrawn rather than rewritten;
- current eligibility must be revalidated.

The stabilised C&M Pre-JIT pack already constrains those semantics without authorising implementation.

Communications does **not** need to decide:

- exact C&M Ash Resource topology;
- translation-work persistence;
- approval Resource topology;
- publication scheduler mechanics;
- public routing.

Therefore a separate FP-001 C&M JIT dossier is still not required **unless** the Final Contract introduces materially new message-content/publication semantics or implementation proves that the required exact C&M reference/eligibility contract cannot be expressed from current authority.

`COMM-UPD-001` is an Identity-artifact correction, not a reason to pull C&M forward.

---

# 55. Content-binding lifecycle refinement — v0.5.0

## 55.1 MessageIntent content-selection dimension

Conceptually:

```text
UNBOUND
→ BOUND_TO_EXACT_CONTENT

BOUND_TO_EXACT_CONTENT
→ CONTENT_BLOCKED
→ BOUND_TO_EXPLICIT_SUCCESSOR   # only under COMM-WD-078

BOUND_TO_EXACT_CONTENT
→ CONTENT_TERMINAL
```

This is not a required literal enum.

`UNBOUND` still has:

- source obligation;
- communication role;
- intended locale;
- destination;
- safe render-data snapshot;
- protected capability where applicable.

It simply has no provider-sendable exact C&M version yet.

## 55.2 Binding eligibility

Before first binding or an explicit safe rebind:

```text
role
+ intended locale
+ applicable risk/content contract
→ C&M exact current eligible shared/message-content version
→ C&M exact current eligible locale version
```

For FP-001 registration/authentication/core-onboarding messages, C&M eligibility incorporates the Product-Law bilingual prerequisite.

Communications should consume the owner result rather than duplicate C&M approval logic.

## 55.3 Attempt rendering

For each provider submission:

```text
current source dispatch authority
+ current privacy/preference policy where applicable
+ current C&M eligibility of exact binding
+ exact safe render snapshot
+ transient protected bearer material where applicable
→ render/validate
→ authorise provider submission
→ DeliveryAttempt with exact content/locale provenance
```

No provider submission occurs if rendering/validation fails.

## 55.4 Correction/withdrawal relationship

```text
bound version remains eligible
→ ordinary retry uses same binding

bound version becomes ineligible
+ prior provider outcome definitively non-delivered
+ exact eligible successor exists
→ explicit safe rebind may occur

bound version becomes ineligible
+ prior provider outcome unknown
→ reconciliation first; no corrected duplicate send

old version was delivered
+ remediation required
→ new source/affected-owner communication consequence
→ new MessageIntent
```

---

# 56. Pressure-test register — fifth cluster

## COMM-PT-085 — Certified Identity dossier says Communications owns message body/template

- **Scenario:** Communications JIT consumes the certified Identity cross-domain seam literally.
- **Authority involved:** Identity dossier v0.1.3 versus current Domain Law, Architecture and FP-001 Skeleton.
- **Durable truths and owner:** C&M owns governed template/content body versions; Communications owns delivery.
- **Concurrency/retry/reordering/crash behaviour:** not material.
- **Rejected models:** silently accept lower-level wording; create duplicate Communications template authority; silently reinterpret without governance record.
- **Required invariant:** one content owner only.
- **Recommended JIT shape:** follow higher authority and block final certification until the Identity wording is patched.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** **YES — narrow certified Identity dossier PATCH successor (`COMM-UPD-001`).**
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** cross-domain ownership tests/static governance checks once implementation exists.
- **Verdict:** **BLOCKED / STOP FOR FINAL CERTIFICATION; discovery may continue.**

## COMM-PT-086 — MessageIntent exists but no eligible C&M message content is currently available

- **Scenario:** Identity challenge + durable intent/capability committed, but content cannot be bound before first provider submission.
- **Authority involved:** must-not-lose delivery; C&M current eligibility.
- **Durable truths and owner:** intent remains Communications truth; content eligibility remains C&M truth.
- **Concurrency/retry/reordering/crash behaviour:** content may become available later; proof may expire first.
- **Rejected models:** send hard-coded emergency copy; use provider default template; drop intent silently.
- **Required invariant:** no provider send without exact eligible governed content; undeliverable obligation remains visible until source ends or content becomes eligible.
- **Recommended JIT shape:** `UNBOUND/CONTENT_BLOCKED` MessageIntent with reconciliation; protected capability remains bounded by proof lifetime.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** missing content → later content availability and missing content → proof expiry.
- **Verdict:** PASS.

## COMM-PT-087 — Afrikaans intended locale exists only as an English approved template

- **Scenario:** Account/source wants Afrikaans; English is available.
- **Authority involved:** Product §21E.1/§21E.7; C&M locale authority.
- **Durable truths and owner:** C&M decides eligible locale versions.
- **Concurrency/retry/reordering/crash behaviour:** none special.
- **Rejected models:** silently send English; provider translate; machine draft.
- **Required invariant:** no delivery until applicable approved Afrikaans content is eligible.
- **Recommended JIT shape:** content-blocked intent, visible failure/reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** selected critical locale unavailable produces zero provider call.
- **Verdict:** PASS.

## COMM-PT-088 — English recipient while required Afrikaans sibling translation is withdrawn

- **Scenario:** English version is still approved, but Product Law requires both languages before registration/authentication delivery.
- **Authority involved:** Product §21E.1 bilingual prerequisite; C&M publication eligibility.
- **Durable truths and owner:** C&M eligibility includes cross-locale prerequisite.
- **Concurrency/retry/reordering/crash behaviour:** withdrawal can occur after intent creation.
- **Rejected models:** “recipient only needs English so Afrikaans does not matter”; Communications independently checks only selected locale.
- **Required invariant:** if C&M deems the governed message ineligible because required bilingual coverage is broken, no new provider attempt occurs even for the still-present locale.
- **Recommended JIT shape:** consume a C&M delivery-eligibility result rather than recreating bilingual logic.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** withdraw required sibling locale and attempt English send.
- **Verdict:** PASS.

## COMM-PT-089 — Only a machine-generated translation is available

- **Scenario:** provider send is urgent but approved human-reviewed variant is missing.
- **Authority involved:** Product/C&M translation lifecycle.
- **Durable truths and owner:** machine draft is not delivery authority.
- **Concurrency/retry/reordering/crash behaviour:** machine draft may later be reviewed.
- **Rejected models:** urgent security use justifies machine translation; operator copies raw machine output.
- **Required invariant:** critical delivery waits for approved governed content.
- **Recommended JIT shape:** content-blocked intent with bounded source lifetime.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** machine-draft state rejected.
- **Verdict:** PASS.

## COMM-PT-090 — Preferred interface language changes after intent creation but before first dispatch

- **Scenario:** MessageIntent was created with Afrikaans intended locale; Account setting becomes English.
- **Authority involved:** Identity Account language + Communications intent provenance.
- **Durable truths and owner:** Account owns current preferred interface language; intent owns selected delivery-locale provenance.
- **Concurrency/retry/reordering/crash behaviour:** language update races content binding/worker.
- **Rejected models:** worker silently re-reads latest Account language and changes the intent; mutate historical intent.
- **Required invariant:** existing intent stays on its explicit locale.
- **Recommended JIT shape:** new source obligation/resend may choose new current language; existing intent unchanged.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** language change before dispatch cannot mutate existing intent.
- **Verdict:** PASS.

## COMM-PT-091 — Browser/content locale differs from Account preferred interface language

- **Scenario:** English-interface Account deliberately browses Afrikaans content, then requests password reset.
- **Authority involved:** Product distinction between interface and content language.
- **Durable truths and owner:** browsing content locale is not security-message preference authority.
- **Concurrency/retry/reordering/crash behaviour:** browser tab locale may be stale or unauthenticated.
- **Rejected models:** use current URL locale automatically for security mail.
- **Required invariant:** communication locale comes from the approved source rule, not unrelated content navigation.
- **Recommended JIT shape:** explicit locale input on MessageIntent.
- **Conclusion:** `UPSTREAM_DERIVED` plus working specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** content-page locale does not change reset email locale absent source rule.
- **Verdict:** PASS.

## COMM-PT-092 — Verification resend after participant changes preferred language

- **Scenario:** original challenge/intent Afrikaans; participant changes language to English and requests resend.
- **Authority involved:** Identity resend lifecycle; Communications new-intent semantics.
- **Durable truths and owner:** Identity issues/supersedes challenge; new MessageIntent has new locale.
- **Concurrency/retry/reordering/crash behaviour:** old Afrikaans job may wake after new English intent.
- **Rejected models:** mutate old MessageIntent locale; reuse old challenge solely to change language.
- **Required invariant:** old source-invalid intent cannot newly dispatch; new intent may use English.
- **Recommended JIT shape:** same v0.2 resend semantics with explicit locale per new intent.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** reordered old/new language jobs.
- **Verdict:** PASS.

## COMM-PT-093 — C&M publishes a corrected version while MessageIntent is still unbound

- **Scenario:** intent waits in queue; template v1 is superseded by eligible v2 before any provider attempt.
- **Authority involved:** C&M current eligibility + Communications first binding.
- **Durable truths and owner:** no exact delivery content had yet been used.
- **Concurrency/retry/reordering/crash behaviour:** first worker may see v1 while another sees v2.
- **Rejected models:** intent creation timestamp permanently selects whichever version existed then despite no binding; each worker picks “latest” independently.
- **Required invariant:** one exact current eligible version is durably bound before first provider submission.
- **Recommended JIT shape:** conditional exact binding; v2 may legitimately become the first binding.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** correction races two first-dispatch workers.
- **Verdict:** PASS.

## COMM-PT-094 — Two workers race initial content binding across nodes

- **Scenario:** both resolve an eligible version around the same time.
- **Authority involved:** Communications binding authority consuming C&M truth.
- **Durable truths and owner:** one current MessageIntent binding.
- **Concurrency/retry/reordering/crash behaviour:** v1 may be superseded between reads.
- **Rejected models:** each DeliveryAttempt chooses independently; Oban uniqueness assumed sufficient.
- **Required invariant:** one committed binding/revision wins and attempt authorisation revalidates it.
- **Recommended JIT shape:** version/conditional update around binding + dispatch preparation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** multi-node concurrent binding.
- **Verdict:** PASS.

## COMM-PT-095 — Bound content is withdrawn before provider I/O

- **Scenario:** exact v1 is bound; safety/legal operator withdraws it before submission starts.
- **Authority involved:** C&M withdrawal.
- **Durable truths and owner:** binding provenance remains, but delivery authority is gone.
- **Concurrency/retry/reordering/crash behaviour:** withdrawal races dispatch authorisation.
- **Rejected models:** immutable binding means forever-sendable; cached publish status.
- **Required invariant:** withdrawal winning before attempt authorisation blocks provider call.
- **Recommended JIT shape:** current C&M eligibility check in the dispatch-authorisation boundary.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** withdrawal/dispatch both interleavings.
- **Verdict:** PASS.

## COMM-PT-096 — Bound version is corrected after a definitive provider rejection

- **Scenario:** attempt 1 definitely did not deliver; C&M withdraws v1 and publishes eligible successor v2 while source proof remains valid.
- **Authority involved:** C&M successor truth; Communications retry.
- **Durable truths and owner:** attempt 1 stays v1 provenance; current intent may still require delivery.
- **Concurrency/retry/reordering/crash behaviour:** retry worker can race correction.
- **Rejected models:** retry v1 after withdrawal; new Identity proof automatically required; silently choose arbitrary latest.
- **Required invariant:** if explicit successor and all `COMM-WD-078` guards pass, same MessageIntent may rebind to v2; next DeliveryAttempt records v2.
- **Recommended JIT shape:** explicit durable content rebind preserving prior attempt.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** definitive rejection → correction → safe rebind → retry.
- **Verdict:** PASS.

## COMM-PT-097 — Content is corrected while prior provider outcome is unknown

- **Scenario:** attempt 1 timed out after possible provider acceptance; v1 is withdrawn and v2 exists.
- **Authority involved:** provider ambiguity + C&M correction.
- **Durable truths and owner:** old attempt may have delivered v1.
- **Concurrency/retry/reordering/crash behaviour:** provider evidence may arrive later.
- **Rejected models:** immediately send v2; mark v1 failed because it was withdrawn.
- **Required invariant:** reconcile the ambiguous old attempt before any new submission/rebind that could duplicate delivery.
- **Recommended JIT shape:** content correction blocks further send but does not resolve provider ambiguity.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** timeout + correction + late accept/deliver.
- **Verdict:** PASS.

## COMM-PT-098 — Content is withdrawn after provider acceptance but before delivery evidence

- **Scenario:** provider accepted v1, C&M withdraws it before delivery callback.
- **Authority involved:** C&M current delivery authority; provider physical operation.
- **Durable truths and owner:** already-submitted attempt remains historical external work.
- **Concurrency/retry/reordering/crash behaviour:** cannot physically recall unless provider independently supports it.
- **Rejected models:** erase acceptance; mark message undelivered; retry corrected content immediately.
- **Required invariant:** no further v1 submission; late delivery evidence retained; remediation is separate if required.
- **Recommended JIT shape:** same in-flight race doctrine as source invalidation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** accepted → withdrawal → late delivery.
- **Verdict:** PASS.

## COMM-PT-099 — Safety/legal correction after old version was delivered

- **Scenario:** participant already received v1; C&M declares material/safety/legal correction.
- **Authority involved:** Product §21E.10; C&M correction; affected source Domain.
- **Durable truths and owner:** original delivery remains historical fact.
- **Concurrency/retry/reordering/crash behaviour:** affected-participant discovery may be async/retried.
- **Rejected models:** rewrite historical attempt to v2; retry old MessageIntent; C&M directly writes Identity/other Domain state.
- **Required invariant:** any required correction notice is a new owner-authorised communication consequence.
- **Recommended JIT shape:** new remediation MessageIntent with exact corrected content.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** delivered v1 + correction → one bounded remediation intent where policy requires.
- **Verdict:** PASS.

## COMM-PT-100 — Content version is superseded but remains delivery-eligible

- **Scenario:** C&M has a newer current version, but old bound v1 is not withdrawn/ineligible.
- **Authority involved:** C&M eligibility, not “latest” ordering.
- **Durable truths and owner:** exact binding v1 remains valid for this intent.
- **Concurrency/retry/reordering/crash behaviour:** retry occurs after v2 publication.
- **Rejected models:** retry automatically jumps to v2 because it is newer.
- **Required invariant:** retry uses v1 while C&M still says that exact binding is eligible.
- **Recommended JIT shape:** exact-version eligibility check.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** v2 published while v1 remains eligible.
- **Verdict:** PASS.

## COMM-PT-101 — Duplicate/reordered C&M withdrawal events

- **Scenario:** Communications receives withdrawal notifications twice or after a later publication notification.
- **Authority involved:** C&M current state; Architecture event/realtime doctrine.
- **Durable truths and owner:** events are observations.
- **Concurrency/retry/reordering/crash behaviour:** duplicate/reordered/lost.
- **Rejected models:** last event wins; event payload becomes publication truth.
- **Required invariant:** attempt authorisation reads current C&M eligibility.
- **Recommended JIT shape:** notifications only accelerate recheck/reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** reorder notification sequence.
- **Verdict:** PASS.

## COMM-PT-102 — Template/content version is missing a required render placeholder

- **Scenario:** verification template lacks required protected-link slot or required event field.
- **Authority involved:** C&M version + Communications closed message-role contract.
- **Durable truths and owner:** C&M owns wording/version; Communications owns executable delivery contract.
- **Concurrency/retry/reordering/crash behaviour:** deterministic render failure.
- **Rejected models:** send incomplete message; let provider invent field; stringly ignore missing variable.
- **Required invariant:** fail closed before provider I/O.
- **Recommended JIT shape:** typed/allow-listed required render contract; content blocked/operationally visible.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** missing/extra/invalid placeholder cases.
- **Verdict:** PASS.

## COMM-PT-103 — Renderer crashes before provider submission

- **Scenario:** all authority checks pass, then render process fails.
- **Authority involved:** Communications execution.
- **Durable truths and owner:** no provider submission occurred.
- **Concurrency/retry/reordering/crash behaviour:** job retry/restart.
- **Rejected models:** create DeliveryAttempt and mark provider failed; discharge intent.
- **Required invariant:** no fabricated provider attempt; retry can re-render deterministically if guards still pass.
- **Recommended JIT shape:** MessageIntent execution failure evidence; DeliveryAttempt begins only at provider operation boundary.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** crash immediately before provider call.
- **Verdict:** PASS.

## COMM-PT-104 — Participant name changes between delivery attempts

- **Scenario:** v1 attempt definitively fails; Account name is edited before retry.
- **Authority involved:** Identity current profile versus Communications delivery snapshot.
- **Durable truths and owner:** Identity owns current name; prior intent may retain minimum immutable render value.
- **Concurrency/retry/reordering/crash behaviour:** profile edit races retry.
- **Rejected models:** arbitrary live reads mean retry body changes unpredictably; duplicate the full Account into Communications.
- **Required invariant:** message-specific render provenance is deterministic and minimal.
- **Recommended JIT shape:** if name is included and material to deterministic message rendering, snapshot the authorised display value on intent; do not re-fetch arbitrary current profile.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** profile edit does not alter old intent rendering.
- **Verdict:** PASS.

## COMM-PT-105 — Email-change message needs old/new address semantics

- **Scenario:** new-address confirmation and old-address notice render address context.
- **Authority involved:** Identity email-change truth; Communications destination snapshot; C&M wording.
- **Durable truths and owner:** Identity owns canonical/candidate addresses; Communications owns minimum immutable delivery snapshot.
- **Concurrency/retry/reordering/crash behaviour:** canonical address can change before retry.
- **Rejected models:** template queries “current Account email” dynamically; C&M stores Account address.
- **Required invariant:** render data describes the source event truth, not whatever Account fields happen to contain later.
- **Recommended JIT shape:** source-authorised old/new address snapshot only where participant-visible copy actually requires it.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** email change progresses while retry renders same historical event correctly.
- **Verdict:** PASS.

## COMM-PT-106 — Bearer token is supplied as an ordinary template variable

- **Scenario:** implementation proposes `render_data.reset_token`.
- **Authority involved:** certified protected-delivery seam.
- **Durable truths and owner:** bearer belongs protected capability machinery.
- **Concurrency/retry/reordering/crash behaviour:** ordinary persistence/log inspection can leak it.
- **Rejected models:** ordinary MessageIntent field; Oban arg; C&M variable default; Audit/telemetry copy.
- **Required invariant:** bearer appears only transiently inside the purpose-scoped executor/provider request.
- **Recommended JIT shape:** protected placeholder injected from protected capability.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** secret-scanning/log/DB/job/audit tests.
- **Verdict:** PASS.

## COMM-PT-107 — Template attempts arbitrary cross-Domain data access

- **Scenario:** editor adds a field like `{{health.conditions}}` or arbitrary query expression.
- **Authority involved:** C&M content ownership; owning Domain data authority; Communications render contract.
- **Durable truths and owner:** template text cannot grant data access.
- **Concurrency/retry/reordering/crash behaviour:** not material.
- **Rejected models:** executable templates; runtime query DSL; broad actor context exposed to renderer.
- **Required invariant:** only code-governed allow-listed render inputs for the message role are available.
- **Recommended JIT shape:** closed data contract with pre-authorised snapshot values.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** unsupported variable/query fails closed.
- **Verdict:** PASS.

## COMM-PT-108 — Participant-controlled string contains HTML/script/control content

- **Scenario:** first name or other permitted render value contains malicious markup.
- **Authority involved:** Communications safe rendering + C&M governed template.
- **Durable truths and owner:** participant input is not trusted markup.
- **Concurrency/retry/reordering/crash behaviour:** deterministic.
- **Rejected models:** raw interpolation into HTML email; provider-specific sanitisation assumed sufficient.
- **Required invariant:** context-appropriate escaping/sanitisation preserves template boundary.
- **Recommended JIT shape:** safe renderer with text/HTML context rules.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** injection corpus/render tests.
- **Verdict:** PASS.

## COMM-PT-109 — Provider-hosted template changes without NewYou content publication

- **Scenario:** provider operator edits template body directly.
- **Authority involved:** C&M content authority; provider external state.
- **Durable truths and owner:** provider edit is not governed NewYou content.
- **Concurrency/retry/reordering/crash behaviour:** subsequent sends differ despite same platform version.
- **Rejected models:** provider template id is the only provenance.
- **Required invariant:** provider cannot silently alter governed body.
- **Recommended JIT shape:** platform-rendered content or strictly version-bound/verified provider mapping; exact approach OQ-036.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider-side drift detection/adapter contract once provider selected.
- **Verdict:** PASS / OQ-036 DETAIL.

## COMM-PT-110 — Provider evidence stores only its template id

- **Scenario:** provider logs say “template 42”, but NewYou version mapping is lost.
- **Authority involved:** exact delivery provenance requirement.
- **Durable truths and owner:** Communications must know the exact C&M version it used.
- **Concurrency/retry/reordering/crash behaviour:** provider template may later change.
- **Rejected models:** reconstruct history from current provider configuration.
- **Required invariant:** platform DeliveryAttempt provenance independently records exact governed C&M binding.
- **Recommended JIT shape:** provider id is supplementary evidence only.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** historical attempt remains interpretable after provider config change.
- **Verdict:** PASS.

## COMM-PT-111 — C&M content lookup/read fails temporarily before first dispatch

- **Scenario:** PostgreSQL/read path error or transient internal failure prevents content resolution.
- **Authority involved:** C&M owner read + Communications durable intent.
- **Durable truths and owner:** MessageIntent remains durable; no content authority is guessed.
- **Concurrency/retry/reordering/crash behaviour:** job retries later; source may expire.
- **Rejected models:** use cached stale template without current eligibility; hard-coded fallback; mark message delivered.
- **Required invariant:** no provider call without exact current eligible binding.
- **Recommended JIT shape:** bounded retry/reconciliation at intent execution; source validity rechecked each time.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** content read outage and recovery.
- **Verdict:** PASS.

## COMM-PT-112 — Historical DeliveryAttempt references content later subject to retention/deletion

- **Scenario:** old exact C&M version is no longer ordinary-current content.
- **Authority involved:** C&M retention/deletion; Communications attempt evidence.
- **Durable truths and owner:** exact historical provenance must remain truthful while the attempt is retained, without forcing indefinite content retention.
- **Concurrency/retry/reordering/crash behaviour:** deletion/disposition may happen after attempt completion.
- **Rejected models:** retain every message template forever solely for Communications; let attempt silently point to an unrelated newer version.
- **Required invariant:** retention/disposition contracts preserve enough lawful provenance to interpret retained evidence without creating perpetual content authority.
- **Recommended JIT shape:** exact version reference while lawful; later disposition follows C&M/Privacy retention contract.
- **Conclusion:** `OPEN_HYPOTHESIS` for exact disposition mechanics; ownership invariant accepted.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO now.
- **Later executable proof:** retention matrix when OQ-029 applies.
- **Verdict:** DEFERRED DETAIL / NO FP-001 BLOCKER.

## COMM-PT-113 — Operator retries while C&M correction/rebind is committing

- **Scenario:** operator presses retry as v1 is being withdrawn and v2 successor binding is being applied.
- **Authority involved:** Communications current binding/version + C&M eligibility.
- **Durable truths and owner:** one current binding/revision wins.
- **Concurrency/retry/reordering/crash behaviour:** cross-node operator/worker race.
- **Rejected models:** operator command carries stale permanent send authority.
- **Required invariant:** retry action revalidates current intent binding + C&M eligibility and loses on stale revision.
- **Recommended JIT shape:** optimistic/conditional current-binding semantics.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale operator retry against rebind.
- **Verdict:** PASS.

## COMM-PT-114 — Corrected content rebind attempts to reuse the previous provider idempotency operation

- **Scenario:** attempt 1 definitively failed with v1; intent is rebound to v2.
- **Authority involved:** Communications DeliveryAttempt identity; provider idempotency semantics.
- **Durable truths and owner:** v2 submission is a genuinely new provider operation even though same MessageIntent.
- **Concurrency/retry/reordering/crash behaviour:** provider could return prior operation if key reused.
- **Rejected models:** reuse provider-operation identity across materially different rendered content.
- **Required invariant:** a new content binding that requires a new submission produces a new DeliveryAttempt/provider-operation identity.
- **Recommended JIT shape:** same business MessageIntent, new DeliveryAttempt.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider idempotency integration once selected.
- **Verdict:** PASS.

## COMM-PT-115 — Does message-template use itself require the FP-001 C&M conditional dossier?

- **Scenario:** Communications JIT needs exact template/locale version provenance.
- **Authority involved:** Skeleton dossier rule; current C&M Domain/Architecture/Product; stabilised C&M Pre-JIT.
- **Durable truths and owner:** no new C&M truth is being introduced.
- **Concurrency/retry/reordering/crash behaviour:** existing C&M correction/withdrawal semantics are already constrained.
- **Rejected models:** pull a dossier merely because another Domain depends on C&M; let Communications invent C&M resources.
- **Required invariant:** dependency alone does not imply dossier; implementation-grade owner semantics must actually be missing.
- **Recommended JIT shape:** reference opaque exact C&M version/locale ids + owner eligibility contract; exact C&M resource topology remains its JIT/OQ-013 concern.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** **NO.**
- **Later executable proof:** cross-domain reference/eligibility integration in the eventual slice.
- **Verdict:** PASS.

## COMM-PT-116 — Provider/adapter accidentally sends the wrong locale body

- **Scenario:** MessageIntent is Afrikaans-bound but adapter submits English payload.
- **Authority involved:** Communications exact delivery provenance and provider request.
- **Durable truths and owner:** requested/bound locale and actual provider payload must agree.
- **Concurrency/retry/reordering/crash behaviour:** adapter bug can recur.
- **Rejected models:** record intended locale and ignore actual rendered/request locale.
- **Required invariant:** attempt preparation validates that rendered artifact matches the exact bound locale/content identity before provider I/O.
- **Recommended JIT shape:** render result carries non-secret provenance metadata checked against attempt binding.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** swapped-locale adapter fault injection.
- **Verdict:** PASS.

## COMM-PT-117 — Test/preview rendering accidentally uses real bearer material

- **Scenario:** operator previews verification/reset template against a real participant intent.
- **Authority involved:** protected-delivery seam + C&M preview.
- **Durable truths and owner:** preview is not delivery authority.
- **Concurrency/retry/reordering/crash behaviour:** preview logs/screens can leak secrets.
- **Rejected models:** decrypt protected capability for preview; copy actual link into C&M preview.
- **Required invariant:** preview/test uses synthetic/non-secret placeholder data and cannot access production bearer capability.
- **Recommended JIT shape:** strict separation between C&M content preview and purpose-scoped delivery executor.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** preview path cannot recover bearer.
- **Verdict:** PASS.

## COMM-PT-118 — Multiple C&M versions appear “approved” but only one is current delivery target

- **Scenario:** immutable historical approvals coexist with current/superseded versions.
- **Authority involved:** C&M `latest != approved != published/current`.
- **Durable truths and owner:** historical approval alone is insufficient.
- **Concurrency/retry/reordering/crash behaviour:** content selection races publication.
- **Rejected models:** pick max version number; pick any approved row.
- **Required invariant:** exact binding comes from C&M's current delivery-eligibility contract.
- **Recommended JIT shape:** owner query/action, not Communications sorting/version heuristics.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** historical approved + superseded/current set.
- **Verdict:** PASS.

## COMM-PT-119 — Message-role mapping changes while an old intent is queued

- **Scenario:** C&M/configuration changes which governed content identity serves `email_verification`.
- **Authority involved:** Communications message-role contract + C&M content identity.
- **Durable truths and owner:** old unbound intent still has the same semantic role.
- **Concurrency/retry/reordering/crash behaviour:** role mapping can change before first binding.
- **Rejected models:** provider id is the role; already-bound intent silently changes content identity.
- **Required invariant:** unbound intent may resolve the currently eligible exact content for that role; once bound, ordinary retry remains pinned unless explicit safe successor rebind applies.
- **Recommended JIT shape:** role→C&M resolution is versioned/configured under governed code/content boundary; exact representation downstream.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** mapping change before/after binding.
- **Verdict:** PASS.

## COMM-PT-120 — Content is withdrawn while Identity proof remains valid for hours

- **Scenario:** proof itself is still valid but the message content is legally/safety ineligible.
- **Authority involved:** independent Identity and C&M authority.
- **Durable truths and owner:** proof validity and content eligibility are distinct.
- **Concurrency/retry/reordering/crash behaviour:** worker repeatedly retries while content remains withdrawn.
- **Rejected models:** valid proof forces delivery; extend retry indefinitely; silently send old content.
- **Required invariant:** content withdrawal blocks new attempts; source proof remains Identity truth and expires normally.
- **Recommended JIT shape:** content-blocked intent with bounded reconciliation; no proof-lifetime extension.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** long content outage until proof expiry.
- **Verdict:** PASS.

## COMM-PT-121 — Preferred language changes after provider acceptance but before physical delivery

- **Scenario:** attempt already accepted in Afrikaans; Account preference becomes English.
- **Authority involved:** Identity language preference + provider external operation.
- **Durable truths and owner:** accepted attempt has immutable exact locale provenance.
- **Concurrency/retry/reordering/crash behaviour:** provider delivery delayed.
- **Rejected models:** rewrite attempt locale; send English duplicate.
- **Required invariant:** in-flight attempt remains Afrikaans historical operation; future new intent may use English.
- **Recommended JIT shape:** no mutation/retry solely due preference change.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** delayed delivery after preference update.
- **Verdict:** PASS.

## COMM-PT-122 — Old-address notice and new-address confirmation accidentally share one content binding

- **Scenario:** implementation maps both email-change roles to one generic template with ambiguous wording.
- **Authority involved:** Identity source roles + C&M content semantics + Communications intent identity.
- **Durable truths and owner:** roles have different destinations and claims.
- **Concurrency/retry/reordering/crash behaviour:** both may be emitted close together.
- **Rejected models:** one generic “email changed” body that can falsely claim final apply; role inferred only from destination.
- **Required invariant:** each MessageIntent role resolves content that is semantically valid for that role.
- **Recommended JIT shape:** role-specific closed render/content contract; C&M may still reuse governed components internally without merging business roles.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** role/template mapping contract tests.
- **Verdict:** PASS.

## COMM-PT-123 — Accountless mailing-list branch later needs bilingual template handling

- **Scenario:** optional mailing-list surface from v0.4 is activated.
- **Authority involved:** conditional SubscriberContact/Privacy branch + C&M locale authority.
- **Durable truths and owner:** same C&M version/locale rules apply, but low-risk marketing fallback may differ from critical security rules according to Product.
- **Concurrency/retry/reordering/crash behaviour:** preference/withdrawal + content correction can race.
- **Rejected models:** reuse security criticality rules blindly for every newsletter; allow provider translation.
- **Required invariant:** message category/risk selects the applicable C&M fallback/approval policy.
- **Recommended JIT shape:** future branch composes the existing admission model with C&M risk/eligibility.
- **Conclusion:** `OPEN_HYPOTHESIS` because the branch is not active FP-001 scope.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** Privacy per v0.4 if branch selected; C&M only if new content semantics emerge.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-124 — Restore/restart resurrects an old bound content version after current withdrawal

- **Scenario:** a restored worker sees MessageIntent bound to v1 from a historical snapshot; current C&M authority has withdrawn v1.
- **Authority involved:** C&M current eligibility + v0.3 restore doctrine.
- **Durable truths and owner:** historical binding is provenance, not current delivery authority.
- **Concurrency/retry/reordering/crash behaviour:** restore precedes current C&M replay/reconciliation.
- **Rejected models:** bound version automatically sends after restore.
- **Required invariant:** provider egress remains gated until current C&M/privacy/source authority is re-established; v1 cannot send if currently withdrawn.
- **Recommended JIT shape:** content eligibility participates in restore semantic verification.
- **Conclusion:** `UPSTREAM_DERIVED` plus working integration.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** pre-withdrawal backup restore with queued intent.
- **Verdict:** PASS.

---

# 57. Rejected-model register additions — v0.5.0

65. **Communications owns governed message template/body versions.** Rejected by current Domain/Architecture law; certified Identity wording requires correction.
66. **Identity owns message content because it originates verification/recovery.** Rejected.
67. **Resolve the provider template id inside the Identity authoritative transition.** Rejected as unnecessary provider/content coupling.
68. **Dereference “latest template” on every retry.** Rejected: destroys exact provenance and allows logical-message drift.
69. **Choose any approved content version.** Rejected: approved, latest and current/delivery-eligible are distinct.
70. **Use browser/content-page locale as automatic security-email locale.** Rejected.
71. **Mutate an existing MessageIntent locale whenever Account preferred language changes.** Rejected.
72. **Silently fall back from Afrikaans to English for required authentication/core-onboarding content.** Rejected.
73. **Use machine translation for urgent security email.** Rejected.
74. **Duplicate C&M translation/approval logic inside Communications.** Rejected.
75. **Immutable content binding means forever-sendable.** Rejected: current C&M eligibility still governs new attempts.
76. **Automatically jump retries to the newest content version.** Rejected.
77. **Send corrected v2 immediately while v1 provider outcome is unknown.** Rejected.
78. **Rewrite historical delivered attempt provenance after correction.** Rejected.
79. **C&M directly creates/changes Identity truth when content is corrected.** Rejected.
80. **Permit arbitrary runtime database queries from message templates.** Rejected.
81. **Store bearer token/link in ordinary render_data.** Rejected.
82. **Persist full secret-bearing rendered body as ordinary MessageIntent truth.** Rejected.
83. **Create DeliveryAttempt for a render failure before provider I/O.** Rejected.
84. **Provider template version is sufficient delivery provenance.** Rejected.
85. **Provider-hosted template edits are governed NewYou publication.** Rejected.
86. **PubSub/correction event is current C&M authority.** Rejected.
87. **Create a Communications TemplateVersion Resource duplicating C&M.** Rejected.
88. **Create a RenderedMessage Resource merely to archive plaintext bodies.** Rejected absent independent requirement and sensitive-data justification.
89. **Pull the C&M dossier forward merely because Communications references C&M.** Rejected; dependency alone does not satisfy the conditional-dossier rule.
90. **Extend Identity proof lifetime because C&M content is unavailable.** Rejected.

---

# 58. Upstream-delta register — v0.5.0

## COMM-UPD-001 — REQUIRED

**Owner:** FP-001 Identity JIT dossier governance.

**Problem:** current certified v0.1.3 cross-domain seam assigns “message body/template” ownership to Communications, conflicting with current Domain Law, Architecture and FP-001 Skeleton.

**Required action:** narrow PATCH successor correcting only the ownership sentence and preserving the certified durable-delivery seam.

**Effect until resolved:**

```text
Pre-JIT discovery
→ MAY CONTINUE

Communications governed JIT final certification
→ BLOCKED / STOP

Phase 7C freeze
→ BLOCKED / STOP
```

## No Product / Architecture / Domain amendment

No higher authority change is required.

The higher authority is already internally coherent.

## C&M working pack staleness

The compact C&M Pre-JIT pack was stabilised against an older authority baseline and is non-authoritative. Its durable conclusions used here were independently checked against current Product v1.6.0, Architecture v1.1.1, Domain v1.2.0, FES v1.0.1 and FP-001 Skeleton v0.1.3.

No C&M broad-discovery reopening is justified.

---

# 59. Unresolved-gate register additions — v0.5.0

| Gate / open matter | v0.5.0 effect |
|---|---|
| `COMM-UPD-001` Identity ownership correction | **Blocks Communications final JIT certification / Phase 7C freeze.** Does not block continued discovery. |
| `OQ-013` exact translation Resource model | Exact C&M Ash topology/immutable-reference implementation remains open. Communications consumes opaque exact version/locale identity and current eligibility; this pass does not resolve OQ-013. |
| `OQ-036` provider/channel policy | Exact provider rendering mode, provider-hosted-template support, provider template drift checks and payload constraints remain open. |
| Message communication-locale selection rule | Explicit intent locale is required. Exact product rule mapping Account preferred interface language to security-message locale should be stated in Communications JIT/Final Contract without turning it into generic content-language preference. |
| Content successor rebinding mechanism | Semantic guard is accepted; exact C&M successor lookup and Communications action/field representation remain JIT. |
| C&M retention versus historical attempt provenance | Exact OQ-029/data-lifecycle disposition remains later policy; no indefinite-retention rule is invented. |
| Correction remediation vocabulary | C&M `CM-UPD-011` remains downstream: exact severity → participant-remediation contract belongs Product/C&M/Safety/Privacy/affected owner as applicable. |

---

# 60. Cross-stream dependency register additions — v0.5.0

| Stream / Domain | v0.5.0 finding |
|---|---|
| Identity & Access | Supplies source obligation, destination and intended communication locale under the approved Account/experience rule. Must not own C&M template content. Certified dossier wording needs narrow correction. |
| Content & Media | Sole owner of governed message-content/template versions, locale versions and correction/withdrawal eligibility. Communications consumes exact references and current eligibility. |
| Privacy & Consent | No new Privacy semantics exposed by required FP-001 content rendering. Secret-bearing/body retention remains minimised under existing boundaries. |
| Audit & Evidence | Should retain only bounded evidence/provenance, not secret-bearing message bodies. Exact Audit dossier still not required by this cluster. |
| Analytics | May consume approved delivery observations; must never receive secret-bearing rendered content or become content provenance authority. |
| Provider | Receives bounded rendered delivery request through adapter. Provider template/configuration never becomes content authority. |
| FES | Confirms bilingual critical-content and no-silent-fallback experience semantics; preview does not authorise use of real secrets. |
| C&M Pre-JIT | Existing stable non-authoritative semantics are reusable evidence; no broad discovery reopening justified. |

---

# 61. Conditional-dossier adjudication — v0.5.0

## Content & Media

**Disposition: `CONDITIONAL / NOT PULLED FORWARD`.**

This pass deliberately attempted to force the dossier forward and did not find a legitimate trigger.

The Communications JIT needs an implementation-grade **cross-domain contract**, but current authority is sufficient to state it:

```text
input:
  message role
  intended locale
  exact/current eligibility requirement

C&M supplies:
  exact governed content version identity
  exact locale-version identity
  current delivery eligibility
  explicit successor relation where applicable

Communications stores/uses:
  exact binding/provenance
  bounded render snapshot
  DeliveryAttempt provenance
```

The Communications dossier does not need to specify C&M's internal:

- ContentItem/ContentVersion physical topology;
- translation work;
- approval persistence;
- publication scheduler;
- public address model;
- editor workflow.

**Pull-forward trigger remains:**

- FP-001 introduces materially new message-content/publication semantics;
- the active slice needs an exact C&M owner lifecycle not already frozen;
- or implementation proves the opaque exact-version/current-eligibility contract cannot be supplied without resolving C&M-specific JIT semantics.

None is proven now.

## Privacy & Consent

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD` for the required FP-001 path.**

The v0.4 mailing-list conditional trigger still stands.

## Audit & Evidence

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD`.**

No new central evidence lifecycle is needed merely to retain exact content-version references.

---

# 62. Later executable proof-obligation register additions — v0.5.0

76. Static/governance proof that only C&M owns governed message-content/template versions; Communications code contains no competing template authority.
77. First-dispatch content binding races across two BEAM nodes and converges on one exact binding.
78. Intent created with no eligible content remains durable/visible and performs zero provider calls until content becomes eligible or source ends.
79. Required Afrikaans message with only English eligible performs zero provider calls.
80. Break required sibling-language eligibility and prove critical registration/authentication delivery fails closed according to C&M authority.
81. Machine-draft translation cannot be selected for required delivery.
82. Account preferred-language change after intent creation does not mutate existing intent locale.
83. Verification resend after language change creates new source intent with new locale while old intent self-suppresses.
84. Correction before first binding selects one exact current eligible successor, never worker-specific “latest”.
85. Withdrawal racing attempt authorisation in both orderings.
86. Definitive provider failure + C&M successor permits one safe explicit rebind and new DeliveryAttempt.
87. Provider unknown + content correction does not permit new corrected send until ambiguity is reconciled.
88. Provider accepted/delivered + later correction preserves historical attempt and uses new remediation intent only when owner policy requires.
89. Retry after unrelated newer version publication keeps old exact eligible binding.
90. Duplicate/reordered C&M invalidation notifications cannot override current C&M read.
91. Missing/invalid required render placeholder fails before provider I/O.
92. Renderer crash before provider call creates no fabricated DeliveryAttempt.
93. Render snapshot remains deterministic when participant name/profile fields change later.
94. Email-change rendering uses event-correct old/new address snapshots rather than current-field drift.
95. Bearer token/link cannot be found in C&M storage, ordinary MessageIntent/DeliveryAttempt fields, Oban args, logs, telemetry, Audit or Analytics.
96. Template cannot access arbitrary cross-Domain data outside its closed role contract.
97. Participant-controlled render data is safely encoded in text/HTML contexts.
98. Provider-hosted template/config drift cannot silently alter a platform-governed content version.
99. Historical DeliveryAttempt can still identify the exact NewYou C&M version after provider config changes.
100. Transient C&M lookup failure yields no stale/hard-coded fallback send.
101. Stale operator retry loses to content withdrawal/rebind revision.
102. Explicit content rebind creates a new provider-operation/DeliveryAttempt identity.
103. Adapter fault attempting to send the wrong locale fails before provider submission or is detected as proof failure.
104. Content preview/test paths cannot recover real protected bearer capability.
105. Restore from pre-withdrawal state cannot send a currently withdrawn bound content version.
106. Role/template mapping tests prove new-address confirmation and old-address security notice resolve semantically valid distinct roles.
107. Content-retention proof later demonstrates no indefinite template retention is introduced solely for Communications evidence.

---

# 63. Resource-discipline review — cumulative through v0.5.0

## `MessageIntent`

**REQUIRED.**

v0.5.0 adds only justified attributes/relationships:

- semantic message role;
- explicit intended locale;
- exact current C&M binding once selected;
- bounded immutable non-secret render-data snapshot;
- content-blocked/rebind status/provenance where applicable.

These are properties/lifecycle of the existing logical communication obligation.

## `DeliveryAttempt`

**REQUIRED.**

v0.5.0 strengthens the requirement that each provider operation preserve the exact content/locale binding used.

## Protected delivery capability

**Still machinery, not business Resource.**

It remains the only lawful place for crash-recoverable bearer material where required.

## Communications `TemplateVersion`

**REJECTED.**

Competes with C&M.

## `RenderedMessage`

**REJECTED at current scope.**

The platform does not need a durable plaintext-body Resource merely to prove what was sent. Exact content/locale provenance plus bounded render snapshot is sufficient unless later evidence proves otherwise.

## `RenderSnapshot`

**Not justified as a separate Resource.**

The bounded immutable non-secret render values belong to MessageIntent delivery provenance unless independent lifecycle/query/retention needs later prove otherwise.

## `LocalePreference`

**Not justified as a Communications Resource for required FP-001.**

The intended communication locale is a property of MessageIntent selected under the source/experience rule. The Account preferred interface language remains Identity-owned.

## `ContentBinding`

**Not justified as a standalone Resource.**

It is an exact relationship/provenance dimension of MessageIntent. A separate Resource would require independent lifecycle evidence beyond safe rebind history, which can currently be represented through the intent's own revision/provenance.

## `SubscriberContact`, `NotificationPreference`, `InAppNotification`, `CommunicationJourney`

No v0.5 content scenario changes the v0.4 adjudication.

**Cumulative required FP-001 Communications Resource verdict remains:**

```text
MessageIntent
DeliveryAttempt
```

---

# 64. Completeness / stabilisation assessment — v0.5.0

**NOT YET STABLE FOR GOVERNED COMMUNICATIONS JIT DOSSIER DRAFTING.**

The Content / locale / rendering scenario class is now provisionally stable enough to stop broadening it.

Two important outcomes emerged:

### 1. No C&M dossier expansion

The required Communications path can consume existing C&M authority through an opaque exact-version / locale / current-eligibility contract.

No new Content & Media lifecycle semantics were needed.

### 2. One real upstream blocker was exposed

`COMM-UPD-001` is now the first required upstream artifact correction found by Communications Pre-JIT:

```text
Identity dossier v0.1.3
"Communications owns ... message body/template"
        ↓ conflicts with
current Domain Law + Architecture + FP-001 Skeleton
```

This does not change higher authority. It requires a narrow Identity PATCH successor before Communications final certification / Phase 7C freeze.

The next materially distinct cluster should be:

## Provider outage / backlog / operational recovery

Pressure-test:

- hours/days-long email-provider outage;
- intent accumulation and proof expiry in backlog;
- bounded versus indefinite retry;
- provider-aware backoff;
- `Retry-After`;
- retry storms after recovery;
- thundering herd;
- fair recovery across message roles;
- security-message priority without starvation;
- provider throughput limits versus business priority;
- attempt unknown at scale;
- delayed provider acceptance;
- provider-wide partial failure;
- per-recipient hard failure;
- operator pause/resume;
- operator retry/reconcile;
- bulk terminal-failure handling;
- cross-node worker concurrency;
- Oban uniqueness versus business idempotency under backlog;
- graceful degradation;
- maintenance modes;
- queue depth/job age observability;
- protected capability/proof expiry while queued;
- participant-visible recovery after terminal delivery failure;
- whether Audit & Evidence becomes required;
- whether `OQ-036` prevents provider-independent JIT finalisation.

After that, perform the Audit/observability and channel/provider-independent passes, then a final combined adversarial stabilisation sweep.
---

# 65. v0.6.0 semantic delta — Provider outage, backlog, bounded retry and operational recovery

This successor preserves all accepted v0.1.0–v0.5.0 findings and adds the sixth substantive Communications pressure-test cluster.

The live repository was rechecked immediately before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

Current controlling authority is unusually explicit for this cluster:

- Product Law requires durable asynchronous notification delivery, idempotency, deduplication, exponential/provider-aware backoff, terminal-failure visibility, correlation, no duplicate message after retry, queue priority classes, backlog alerting, bounded retry and explicit degraded behaviour during provider outages.
- Architecture Class B requires durable intent, repeat-safe execution, current-precondition revalidation and success/retry/terminal-visible outcome. Oban is execution machinery, not business truth. Backlogs are bounded operational buffers; retry budgets are error-class-aware, bounded and jittered; shared dependency outages use coordinated degradation rather than worker herds.
- Architecture provider ingress treats duplicate/reordered callbacks as normal and requires ambiguous irreversible provider outcomes to remain pending/unresolved and reconcile before repeating the effect.
- Communications Domain Law makes provider outage a degradation of communication only, identifies provider rate limits/backlog recovery/retry storms as material scaling risks and keeps Redis/ETS/queue state non-authoritative.
- Engineering Standards require adapters to translate provider failures into application-understood `retryable`, `terminal`, `unknown/unresolved` or `reconciliation-required` semantics. A timeout or ambiguous acknowledgement cannot silently become success or blind retry.
- FP-001 Roadmap classifies `OQ-036` as **BLOCKS_RELEASE_ONLY**, not a Phase-7C planning blocker. Exact launch provider/channel policy, costs, provider-specific retries and delivery evidence remain unresolved.

This pass pressure-tests:

- provider operation identity before external I/O;
- known outage before submission;
- crash before provider call;
- crash after provider call with no response;
- timeout/ambiguous acknowledgement;
- definitive connection failure;
- provider `Retry-After`/rate limiting;
- provider credentials/configuration failure;
- provider-wide 5xx/outage;
- recipient-specific hard rejection;
- partial provider failure;
- delayed acceptance/callback;
- duplicate workers and Oban uniqueness expiry;
- job loss and intent-liveness reconciliation;
- proof/capability/content expiry while queued;
- proof consumption/revocation/supersession while backlogged;
- repeated participant resend during outage;
- retry-budget exhaustion;
- infrastructure-attempt count versus business retry budget;
- outage recovery thundering herd;
- priority/fairness under backlog;
- provider capacity versus business priority;
- operator pause/resume/retry/reconciliation;
- terminal failure and participant-visible recovery;
- maintenance modes;
- observability outage;
- provider failover temptation;
- bulk retry/fan-out without campaign architecture;
- whether `OQ-036` prevents a provider-independent Communications JIT;
- whether Audit & Evidence must be pulled forward.

No provider, queue name, exact retry count, timeout, backoff coefficient, circuit-breaker package, Redis key, worker concurrency, provider idempotency API or failover provider is selected.

---

# 66. Accepted working-design register additions — v0.6.0

## COMM-WD-092 — A DeliveryAttempt operation identity is durably established after all preflight validation and before external provider submission

**Status:** `WORKING_DESIGN_ACCEPTED`

`COMM-WD-086` is refined, not contradicted.

Rendering/validation failure before provider-operation preparation is **not** a DeliveryAttempt. Once all current guards pass and Communications is genuinely ready to perform one provider submission, the platform establishes one durable attempt/operation identity and exact provenance before crossing the external-I/O boundary.

Conceptually:

```text
revalidate current source/content/privacy/preference/policy
→ render + validate
→ establish durable DeliveryAttempt/provider-operation identity
→ external provider call
→ classify/reconcile provider outcome
```

This provides a durable correlation point for the crash window after a request may have left the process but before its result is durably recorded.

A crash after attempt preparation but before any external request is proven to have begun may resume/cancel that prepared operation according to the provider adapter contract. It must not be mistaken for provider acceptance.

Exact attempt-state vocabulary and transaction layout remain JIT/proof detail.

## COMM-WD-093 — Provider outcomes are normalised into platform semantics before they affect retry/reconciliation

**Status:** `UPSTREAM_DERIVED`

Provider SDK/HTTP/SMTP-specific errors are translated into application-understood semantics such as:

```text
DEFINITIVE_SUCCESS_OR_ACCEPTANCE_EVIDENCE
DEFINITIVE_RETRYABLE_FAILURE
DEFINITIVE_TERMINAL_FAILURE
OUTCOME_UNKNOWN_OR_UNRESOLVED
RECONCILIATION_REQUIRED
```

This is conceptual, not a required enum.

Raw provider codes do not become participant-facing contracts or Communications business authority.

## COMM-WD-094 — `unknown` is never synonymous with `retryable`

**Status:** `UPSTREAM_DERIVED`

A timeout, connection loss after submission, malformed acknowledgement or crash after external I/O may mean the provider accepted the operation even though NewYou does not know.

Therefore:

```text
unknown
!= failed
!= retryable
!= accepted
!= delivered
```

An unresolved attempt is reconciled before a new provider operation that could duplicate delivery.

## COMM-WD-095 — Known pre-provider deferral does not create a DeliveryAttempt

**Status:** `WORKING_DESIGN_ACCEPTED`

If Communications knows **before attempt preparation** that provider submission is not currently allowed or useful because of:

- provider-wide outage/dependency pause;
- provider admission throttle;
- maintenance mode;
- quiet/policy deferral;
- current proof/source invalidity;
- content ineligibility;

then no provider operation exists and no DeliveryAttempt is fabricated.

The MessageIntent remains deferred/suppressed/terminal-visible according to the owning reason.

## COMM-WD-096 — The effective retry horizon is bounded by the delivery obligation, not just a queue's retry configuration

**Status:** `WORKING_DESIGN_ACCEPTED`

For FP-001 bearer-bearing security messages, automated retry can continue only while **all** relevant current bounds still permit it.

Conceptually:

```text
effective retry horizon
= bounded delivery policy
  intersect source proof validity
  intersect protected-capability recoverability
  intersect current content eligibility
  intersect current Account/privacy/source dispatch authority
```

The exact provider retry count/backoff remains `OQ-036`, but no provider policy may extend a proof or protected capability beyond its authoritative lifetime.

## COMM-WD-097 — Business retry state is durable and independent of Oban's job-attempt counter

**Status:** `WORKING_DESIGN_ACCEPTED`

Oban attempt count is execution evidence, not the complete Communications retry contract.

Why:

- some job wakes create no provider attempt because current authority suppresses/defer them;
- renderer/internal failures may consume infrastructure executions but no provider operation;
- provider reconciliation may occur without a new send;
- a job can be recreated after loss/restart;
- provider-specific operation attempts need their own evidence.

Therefore a restart, job recreation or uniqueness expiry must not reset the business retry budget.

Exact durable representation may live in MessageIntent/DeliveryAttempt state and does not justify a separate `RetryBudget` Resource.

## COMM-WD-098 — Source/proof/capability expiry pre-empts queued retry

**Status:** `UPSTREAM_DERIVED`

When a queued verification/reset/recovery/email-change obligation is no longer valid:

- no new provider attempt is authorised;
- protected bearer material is cleared/rendered irrecoverable according to the certified Identity seam;
- remaining execution work self-suppresses/reconciles;
- provider outage is not blamed as the source business outcome.

A new participant resend/recovery action requires the source-owner lifecycle to create a new source obligation and MessageIntent where permitted.

## COMM-WD-099 — Queue position and job age are not delivery authority

**Status:** `UPSTREAM_DERIVED`

A MessageIntent becoming old, reaching the front of the queue or being retried many times never makes it sendable.

Every actual new provider submission still requires current:

- source dispatch authority;
- content eligibility;
- privacy/preference policy where applicable;
- delivery-policy/provider admission.

Queue age is operational evidence/alert input only.

## COMM-WD-100 — Durable MessageIntent liveness must not depend on one surviving Oban job

**Status:** `WORKING_DESIGN_ACCEPTED`

A committed must-not-lose MessageIntent cannot be permanently stranded because:

- a process dies;
- a job is lost/cancelled/corrupted;
- transactional enqueue was not the selected exact mechanism;
- job uniqueness behaves unexpectedly;
- an operator pauses/resumes queues.

The implementation must provide a durable liveness/reconciliation path that can identify an unresolved eligible MessageIntent with missing/stale execution work and safely restore execution.

A transactional Oban job may satisfy this when it fully represents intent; otherwise the MessageIntent itself is the durable reconciliation anchor.

Exact sweep/reconciler/query mechanism remains JIT/proof detail and is **not** a new Resource.

## COMM-WD-101 — Shared provider outage uses coordinated degradation, not per-intent exponential chaos

**Status:** `UPSTREAM_DERIVED`

A provider-wide outage is a shared dependency condition.

The desired execution shape is:

```text
provider degradation detected
→ reduce/pause new provider admissions coherently
→ preserve durable MessageIntents
→ avoid multiplying network calls/jobs
→ periodically/provably reassess dependency
→ resume gradually when safe
```

Each MessageIntent still owns its own business validity. Shared outage coordination is execution/admission machinery, not message authority.

## COMM-WD-102 — Provider `Retry-After` and similar hints are evidence/input to scheduling, not authority

**Status:** `WORKING_DESIGN_ACCEPTED`

Where a provider supplies a retry delay or rate-limit reset:

- the adapter may use it if trustworthy and applicable;
- it cannot override proof expiry, source invalidation, content withdrawal or platform safety bounds;
- a pathological/very long hint cannot silently extend the delivery obligation;
- exact parsing/mapping remains provider-specific `OQ-036` work.

## COMM-WD-103 — Outage recovery is revalidated and spread; it is not a blind FIFO drain

**Status:** `WORKING_DESIGN_ACCEPTED`

When a provider recovers after a backlog:

1. stale/expired/superseded/consumed intents self-suppress first;
2. unresolved provider attempts reconcile before duplicate submission;
3. eligible work resumes under bounded concurrency/provider capacity;
4. jitter/spreading prevents a thundering herd;
5. operational priority may order eligible work but never bypass source authority.

The oldest queued job is not automatically the most important or still valid message.

## COMM-WD-104 — Priority is a scheduling policy over eligible work, not a business-authority dimension

**Status:** `UPSTREAM_DERIVED` plus working specialisation

Current Product Law requires queue priority classes.

For Communications, priority may distinguish classes such as time-sensitive required security/recovery from optional future marketing/reminders, but:

- priority never makes invalid work valid;
- priority never changes proof expiry;
- priority never creates an alternate channel;
- priority never converts provider capacity into business truth.

Exact priority classes/weights/queue names are implementation/OQ-036 detail.

## COMM-WD-105 — Priority policy must prevent operational starvation of still-valid required work

**Status:** `WORKING_DESIGN_ACCEPTED`

It is acceptable for optional/low-urgency communication to degrade aggressively during provider pressure.

It is not acceptable for one high-volume class to indefinitely starve other still-valid required FP-001 security obligations merely because they share infrastructure.

Exact fairness algorithm is downstream proof/operations detail, but the required property is:

```text
bounded provider capacity
+ priority
+ fairness among still-valid required work
```

not universal FIFO and not unlimited priority bypass.

## COMM-WD-106 — Provider capacity/rate-control state is derived execution state, never Communications business authority

**Status:** `UPSTREAM_DERIVED`

Rate tokens, circuit state, concurrency counters or temporary provider-health summaries may use PostgreSQL/Redis/ETS or another approved mechanism if later justified.

They do not own:

- MessageIntent validity;
- DeliveryAttempt history;
- Identity proof state;
- consent/preferences;
- terminal business outcome.

Loss of an accelerator may reduce throughput or force explicit conservative degradation, but must not fabricate delivery success or permission.

## COMM-WD-107 — Provider idempotency capability strengthens safety but never replaces business idempotency

**Status:** `UPSTREAM_DERIVED`

If the selected provider supports idempotency keys/request identities, the adapter should use them where they materially reduce duplicate risk.

However:

- MessageIntent logical identity remains platform-owned;
- DeliveryAttempt/provider-operation identity remains platform-owned;
- provider idempotency-window expiry cannot redefine business duplicate semantics;
- provider lack of idempotency support must be handled by the selected `OQ-036` reconciliation strategy rather than assumed away.

## COMM-WD-108 — Provider-wide and recipient-specific failures remain separate

**Status:** `WORKING_DESIGN_ACCEPTED`

Examples:

```text
provider authentication/config failure
provider service outage
provider global throttle
```

are shared dependency conditions.

Examples such as:

```text
invalid destination
hard recipient rejection/bounce evidence
recipient/provider suppression
```

are destination/operation-specific evidence.

Do not globally pause healthy recipients because one address fails, and do not retry thousands of recipients independently against a known global outage.

## COMM-WD-109 — Automated terminal failure means no further automatic provider submission under the current policy

**Status:** `WORKING_DESIGN_ACCEPTED`

Terminal-visible delivery failure is a durable Communications outcome for the current logical obligation/policy.

It does **not** mean:

- Identity proof succeeded/failed;
- Account email became invalid;
- operator may never investigate;
- historical provider evidence disappears.

An explicit operator recovery action may permit a new attempt on the **same MessageIntent** only when:

- source obligation is still valid;
- prior provider outcomes are definitive/reconciled;
- current content/destination/policy still permits send;
- the operator action is authorised and evidence-bearing;
- it does not merely reset the old automated retry budget by accident.

If the source has expired/superseded, recovery requires a new source obligation/MessageIntent instead.

## COMM-WD-110 — Operator retry is a current-authority command, not a bypass

**Status:** `WORKING_DESIGN_ACCEPTED`

Operator retry must re-read exactly the same current authority dimensions as normal execution.

An operator cannot override:

- expired/consumed/revoked proof;
- completed deletion;
- content withdrawal;
- denied optional permission/preference;
- unresolved previous provider outcome;
- destination/source mismatch.

The action is safe even from a stale admin page because the server-side action revalidates current state.

## COMM-WD-111 — Reconciliation and retry are different operator actions

**Status:** `WORKING_DESIGN_ACCEPTED`

For an unknown provider outcome, the safe operator action is **reconcile**, not “retry anyway”.

Reconciliation may:

- query/provider-match an operation if supported;
- consume late callback/evidence;
- classify the attempt definitive success/failure;
- leave it unresolved if evidence remains insufficient.

Only after the ambiguity is resolved may normal retry policy decide whether a new provider operation is allowed.

Exact provider reconciliation capability remains `OQ-036`.

## COMM-WD-112 — Provider pause/resume is execution control, not MessageIntent lifecycle authority

**Status:** `WORKING_DESIGN_ACCEPTED`

An authorised operator/system may temporarily pause admissions to a provider/channel during an incident or maintenance window.

Pause does not:

- cancel valid source obligations;
- mark attempts failed;
- mark messages delivered;
- extend proof expiry.

Resume does not blindly submit the accumulated backlog; every intent is revalidated first.

## COMM-WD-113 — Terminal FP-001 delivery failure requires participant-visible recovery through the owning journey, not necessarily an in-app notification centre

**Status:** `UPSTREAM_DERIVED` plus working specialisation

Required work cannot exist only in email/toast/ephemeral state.

For verification/recovery/email-change, the participant-facing Identity/account journey already has the appropriate recovery surfaces such as:

- verification pending;
- resend where permitted;
- change-email recovery where permitted;
- support/recovery escalation.

Communications supplies accurate delivery failure/requires-attention state. This does **not** justify `InAppNotification` for FP-001.

## COMM-WD-114 — Provider outage never fabricates Identity success and does not roll back a correctly committed source transition merely because external delivery is delayed

**Status:** `UPSTREAM_DERIVED`

If Identity challenge issuance + MessageIntent + protected capability commit coherently, subsequent provider outage leaves:

- the Identity challenge/source truth intact until its own lifecycle changes;
- the Account unverified/unrecovered/unapplied as applicable;
- Communications pending/degraded/terminal-visible according to delivery state.

A participant may need to retry/resend/recover later, but provider failure cannot mark the Account verified or manufacture success.

## COMM-WD-115 — Participant resend during outage creates new source authority only through Identity; Communications does not coalesce proofs by convenience

**Status:** `UPSTREAM_DERIVED` plus working backlog specialisation

An accepted participant resend follows the certified Identity resend lifecycle and can create a new challenge + new MessageIntent.

Older superseded intents may still have stale Oban jobs/backlog entries, but current source revalidation suppresses them.

Communications must not merge multiple distinct Identity challenges into one intent merely to reduce backlog.

`OQ-035` owns abuse thresholds limiting resend flooding.

## COMM-WD-116 — Failure to establish the durable handoff still fails closed even during a provider incident

**Status:** `UPSTREAM_DERIVED`

A provider outage is safe **after** durable intent exists.

A database/transaction failure that prevents atomic source issuance + MessageIntent + required protected capability establishment is different:

```text
no durable Communications obligation
→ source issuance requiring it must not commit as if delivery were safely queued
```

Provider degradation cannot be used as an excuse to weaken the must-not-lose transaction boundary.

## COMM-WD-117 — Maintenance/degraded mode may queue valid communications, but cannot silently discard them or pretend they were sent

**Status:** `UPSTREAM_DERIVED`

Product Law explicitly permits notifications to queue safely during degradation.

Therefore maintenance may:

- stop provider admissions;
- preserve durable pending intents;
- surface degraded/pending state;
- resume after revalidation.

It may not convert queued → sent/delivered without evidence or drop must-not-lose obligations silently.

## COMM-WD-118 — Automatic cross-provider failover is not part of the FP-001 provider-independent contract

**Status:** `WORKING_DESIGN_ACCEPTED`

No second-provider architecture is justified by current FP-001 law.

Automatic failover is particularly dangerous after an unknown first-provider outcome because it can deliver the same logical message twice through two providers.

If `OQ-036` later selects multiple providers/failover, it must prove:

- provider-operation reconciliation;
- duplicate suppression across providers;
- content/destination consistency;
- credential/security operations;
- bounded failover policy.

Until then, no generic `ProviderRouter` or multi-provider failover Resource/service is introduced.

## COMM-WD-119 — Batch/backlog recovery does not create CommunicationJourney or campaign authority

**Status:** `WORKING_DESIGN_ACCEPTED`

Operationally processing many independent MessageIntents in bounded batches is not a campaign or communication journey.

FP-001 can use:

- bounded pagination;
- batch job claiming;
- concurrency limits;
- priority classes;

without introducing `CommunicationJourney`.

Each security MessageIntent retains its own source obligation and current-validity contract.

## COMM-WD-120 — Telemetry/dashboard state is derived; durable provider/attempt evidence stays in Communications

**Status:** `UPSTREAM_DERIVED`

Operational observability must show enough to find:

- backlog depth/age;
- retry/reconciliation failures;
- provider latency/outage;
- unresolved obligations;
- terminal failures.

But:

- a metrics exporter outage cannot change delivery truth;
- dashboards are not retry authority;
- raw logs/traces are not DeliveryAttempt history;
- sensitive destinations/bearer material are not metric labels/log payloads.

Material provider execution evidence needed to understand a MessageIntent belongs in Communications-owned durable state. Central Audit remains separate and minimal.

---

# 67. Provider-independent execution model — v0.6.0

The cumulative provider submission path is now:

```text
MessageIntent exists durably
        ↓
execution wakes / reconciliation finds it
        ↓
re-read source + content + privacy/preference + closure/deletion authority
        ↓
provider/channel admission check
        ↓
if known defer/pause/throttle
    → no DeliveryAttempt
    → schedule/reconcile later within bounded obligation
        ↓
render + validate
        ↓
establish durable DeliveryAttempt/provider-operation identity
        ↓
provider request
        ↓
classify evidence
    ├─ definitive accepted/success evidence
    ├─ definitive retryable failure
    ├─ definitive terminal failure
    └─ unknown/reconciliation-required
        ↓
update MessageIntent / retry schedule / terminal visibility
```

Important distinctions:

```text
job execution
!= provider attempt

provider accepted
!= delivered

provider failure
!= source failure

unknown
!= retryable

retry budget exhausted
!= permission to fabricate terminal business truth elsewhere
```

---

# 68. Retry-budget doctrine — v0.6.0

The exact numeric retry policy remains `OQ-036`, but the JIT semantic envelope can be frozen.

A retry policy must be:

- bounded;
- error-class-aware;
- jittered;
- provider-aware;
- source-validity-aware;
- protected-capability-aware;
- content/current-authority-aware;
- restart-safe;
- independent of telemetry availability;
- visible when exhausted.

It must **not** be:

- infinite;
- reset by process/node restart;
- reset by recreating an Oban job;
- driven only by HTTP status without adapter semantics;
- allowed beyond proof expiry;
- allowed while prior provider outcome remains ambiguous;
- a mechanism for silently sending stale/superseded content/proofs.

Exact retry count, interval sequence, provider `Retry-After` handling, timeout and circuit thresholds are provider/operations implementation details under `OQ-036`.

---

# 69. Pressure-test register — sixth cluster

## COMM-PT-125 — Provider is known unavailable before provider-operation preparation

- **Scenario:** provider incident/dependency pause is already active when worker wakes.
- **Authority involved:** Product graceful degradation; Architecture coordinated outage; Communications durable intent.
- **Durable truths and owner:** MessageIntent remains Communications truth; provider health is execution evidence.
- **Concurrency/retry/reordering/crash behaviour:** thousands of workers may wake on multiple nodes.
- **Rejected models:** each creates a DeliveryAttempt and calls provider anyway; mark failed/delivered; drop jobs.
- **Required invariant:** no provider attempt; durable intent remains deferred within its valid obligation.
- **Recommended JIT shape:** provider admission gate before attempt preparation + coordinated reschedule/reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED` plus working attempt-boundary specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider-down state + large worker population yields near-zero/controlled provider calls and no fabricated attempts.
- **Verdict:** PASS.

## COMM-PT-126 — Crash after DeliveryAttempt preparation but before network request begins

- **Scenario:** durable attempt identity committed; process dies before provider call.
- **Authority involved:** Communications attempt lifecycle.
- **Durable truths and owner:** prepared provider-operation identity exists; no external acceptance is proven.
- **Concurrency/retry/reordering/crash behaviour:** replacement worker sees prepared/incomplete attempt.
- **Rejected models:** assume sent; create a second unrelated attempt immediately; delete evidence.
- **Required invariant:** resume/reconcile the prepared operation safely without multiplying logical message.
- **Recommended JIT shape:** provider adapter defines safe pre-submit recovery using the existing attempt identity.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** deterministic crash at pre-network boundary.
- **Verdict:** PASS.

## COMM-PT-127 — Crash after provider request leaves the node but before response is durably recorded

- **Scenario:** provider may have accepted; local process dies.
- **Authority involved:** Architecture ambiguous irreversible outcomes; Communications attempt evidence.
- **Durable truths and owner:** durable attempt identity exists; outcome unknown.
- **Concurrency/retry/reordering/crash behaviour:** new worker may wake before callback/provider query.
- **Rejected models:** mark failed and retry; mark success; create a new attempt because Oban retried.
- **Required invariant:** attempt becomes/remains unresolved and reconciles before a second provider operation.
- **Recommended JIT shape:** durable operation identity + provider-specific reconciliation under OQ-036.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** process kill immediately after socket/request handoff.
- **Verdict:** PASS.

## COMM-PT-128 — Provider request times out after submission may have occurred

- **Scenario:** no definitive response before deadline.
- **Authority involved:** Engineering Standards unknown semantics.
- **Durable truths and owner:** attempt outcome unresolved.
- **Concurrency/retry/reordering/crash behaviour:** provider may later callback/deliver.
- **Rejected models:** HTTP timeout = failed; blindly exponential-retry.
- **Required invariant:** no new send until reconciliation strategy permits it.
- **Recommended JIT shape:** `unknown/reconciliation-required` provider outcome.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** timeout + late provider acceptance/delivery.
- **Verdict:** PASS.

## COMM-PT-129 — Connection fails definitively before request can reach provider

- **Scenario:** adapter can prove no provider operation was accepted/started.
- **Authority involved:** provider adapter failure classification.
- **Durable truths and owner:** prepared attempt has definitive non-submission/retryable result.
- **Concurrency/retry/reordering/crash behaviour:** safe bounded retry may occur.
- **Rejected models:** classify every transport error unknown forever; create duplicate logical intent.
- **Required invariant:** only adapter-proven definitive non-submission may enter retry path without provider reconciliation.
- **Recommended JIT shape:** provider-specific mapping beneath stable platform taxonomy.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** fault before connect/request body; prove no provider operation.
- **Verdict:** PASS / exact mapping OQ-036.

## COMM-PT-130 — Provider rate-limits with a Retry-After hint

- **Scenario:** provider returns a throttling response with a delay.
- **Authority involved:** Product provider-aware backoff; OQ-036.
- **Durable truths and owner:** provider hint is execution evidence; source proof lifetime remains Identity authority.
- **Concurrency/retry/reordering/crash behaviour:** many attempts can receive same reset time.
- **Rejected models:** all jobs wake exactly at reset; extend proof expiry to honour provider; ignore provider signal entirely.
- **Required invariant:** bounded/jittered provider-aware delay never outlives current delivery authority.
- **Recommended JIT shape:** adapter-normalised throttle + shared admission/backoff.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** common Retry-After across backlog without herd.
- **Verdict:** PASS / exact parsing OQ-036.

## COMM-PT-131 — Provider credentials/configuration are invalid

- **Scenario:** every request fails authentication/authorisation because configuration is broken.
- **Authority involved:** provider boundary + operations degradation.
- **Durable truths and owner:** systemic dependency fault, not per-recipient failure.
- **Concurrency/retry/reordering/crash behaviour:** naive workers can hammer provider indefinitely.
- **Rejected models:** retry each intent independently as transient; mark destination bad; expose raw provider error to participant.
- **Required invariant:** coordinated degradation stops herd, preserves intents and surfaces actionable operator failure.
- **Recommended JIT shape:** systemic provider fault classification + pause/circuit/degraded mode.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** credential revocation under active backlog.
- **Verdict:** PASS.

## COMM-PT-132 — Provider returns sustained 5xx/service outage

- **Scenario:** service is reachable but broadly failing.
- **Authority involved:** Architecture shared dependency outage.
- **Durable truths and owner:** provider-wide health evidence; each intent remains independent business truth.
- **Concurrency/retry/reordering/crash behaviour:** many workers observe same fault.
- **Rejected models:** thousands of independent exponential loops with no coordination.
- **Required invariant:** provider admissions degrade coherently; retry remains bounded/jittered.
- **Recommended JIT shape:** shared outage coordination + per-intent durable state.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** sustained 5xx at representative backlog volume.
- **Verdict:** PASS.

## COMM-PT-133 — Provider definitively rejects one recipient/destination

- **Scenario:** invalid address/hard rejection for one destination while provider is otherwise healthy.
- **Authority involved:** Communications provider evidence; Identity canonical email boundary.
- **Durable truths and owner:** recipient-specific DeliveryAttempt evidence; canonical Account email remains Identity-owned.
- **Concurrency/retry/reordering/crash behaviour:** another worker may retry same intent.
- **Rejected models:** pause global provider; clear canonical email; retry hard failure forever.
- **Required invariant:** destination-specific terminal/recovery path; no Identity mutation from provider evidence.
- **Recommended JIT shape:** terminal attempt/intent visibility + participant change-email/support path where source permits.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** one hard rejection among healthy sends.
- **Verdict:** PASS.

## COMM-PT-134 — Provider partially fails: some operations succeed, others throttle/fail

- **Scenario:** degraded provider behaves inconsistently.
- **Authority involved:** per-operation provider evidence + shared health projection.
- **Durable truths and owner:** each DeliveryAttempt result is independent; shared health is derived.
- **Concurrency/retry/reordering/crash behaviour:** classifications arrive concurrently.
- **Rejected models:** one global status rewrites all attempt results; successful operations retried because provider is “down”.
- **Required invariant:** definitive successful attempts stay definitive; only eligible unresolved/retryable work continues.
- **Recommended JIT shape:** per-attempt evidence plus conservative shared admission control.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** mixed provider outcomes under one outage window.
- **Verdict:** PASS.

## COMM-PT-135 — Provider accepts slowly and callback arrives after local retry timer would normally fire

- **Scenario:** delayed acceptance/evidence creates apparent timeout.
- **Authority involved:** unknown-outcome reconciliation.
- **Durable truths and owner:** original attempt remains unresolved until evidence.
- **Concurrency/retry/reordering/crash behaviour:** timer/job may wake first; callback later.
- **Rejected models:** retry timer itself proves failure.
- **Required invariant:** unresolved attempt blocks duplicate provider submission.
- **Recommended JIT shape:** reconciliation-first state; late evidence converges idempotently.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** timer wake before late callback.
- **Verdict:** PASS.

## COMM-PT-136 — Duplicate workers execute the same MessageIntent during outage

- **Scenario:** Oban duplicate/retry/concurrency creates two workers.
- **Authority involved:** business idempotency + attempt identity.
- **Durable truths and owner:** one logical MessageIntent.
- **Concurrency/retry/reordering/crash behaviour:** both nodes race provider admission/attempt preparation.
- **Rejected models:** rely only on Oban uniqueness; both create attempts.
- **Required invariant:** business concurrency control permits at most the policy-allowed provider operation for the current intent state.
- **Recommended JIT shape:** conditional current-state/attempt claim; exact DB mechanism later.
- **Conclusion:** `UPSTREAM_DERIVED` plus working specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** two-node simultaneous attempt preparation.
- **Verdict:** PASS.

## COMM-PT-137 — Worker receives provider acceptance, then crashes before committing the acceptance result

- **Scenario:** response definitely said accepted, but local durable update is lost.
- **Authority involved:** provider operation identity/reconciliation.
- **Durable truths and owner:** provider may later expose operation by id/callback; local state remains unresolved after crash.
- **Concurrency/retry/reordering/crash behaviour:** replacement worker lacks committed result.
- **Rejected models:** assume previous process succeeded locally; blindly resend.
- **Required invariant:** durable attempt identity permits later reconciliation; no duplicate send without resolving the original.
- **Recommended JIT shape:** provider operation id/idempotency key stored before/with request as provider permits; exact mechanics OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** kill after accepted response before state update.
- **Verdict:** PASS.

## COMM-PT-138 — Duplicate/reordered provider callbacks arrive during backlog recovery

- **Scenario:** callbacks for accepted/delivered/bounce evidence arrive multiple times/out of order.
- **Authority involved:** Architecture provider ingress.
- **Durable truths and owner:** callbacks = authenticated external evidence; DeliveryAttempt effective state = Communications.
- **Concurrency/retry/reordering/crash behaviour:** callbacks race worker/reconciliation.
- **Rejected models:** last callback blindly overwrites; callback spawns new intent.
- **Required invariant:** duplicate/reordered evidence converges without regressing impossible state or changing source authority.
- **Recommended JIT shape:** idempotent provider-evidence ingestion + reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** callback permutation/fuzz tests.
- **Verdict:** PASS.

## COMM-PT-139 — Provider recovers with a large multi-node backlog

- **Scenario:** thousands of jobs become runnable together.
- **Authority involved:** Product queue priority/backlog alerts; Architecture anti-herd doctrine.
- **Durable truths and owner:** intents remain individual durable obligations.
- **Concurrency/retry/reordering/crash behaviour:** every node sees provider healthy simultaneously.
- **Rejected models:** release all workers at once; FIFO blast; Redis counter as authority.
- **Required invariant:** bounded concurrency/jitter/admission control prevents provider/DB overload and revalidates each intent.
- **Recommended JIT shape:** shared provider capacity budget + queue/workload controls; exact mechanism later.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** outage recovery burst at representative scale.
- **Verdict:** PASS.

## COMM-PT-140 — Many queued proofs have expired before outage recovery

- **Scenario:** provider was down longer than verification/reset lifetimes.
- **Authority involved:** Identity proof lifecycle + Communications backlog.
- **Durable truths and owner:** Identity expiry is authoritative.
- **Concurrency/retry/reordering/crash behaviour:** expired and live work interleaved.
- **Rejected models:** drain queue before checking expiry; extend proof lifetime; send stale links “for completeness”.
- **Required invariant:** expired intents self-suppress/cleanup before provider attempt.
- **Recommended JIT shape:** cheap current-validity revalidation ahead of provider capacity consumption.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** majority-expired backlog recovery.
- **Verdict:** PASS.

## COMM-PT-141 — Proof expires while a retry is sleeping

- **Scenario:** next retry time is after proof expiry.
- **Authority involved:** Identity expiry + retry scheduler.
- **Durable truths and owner:** expiry wins.
- **Concurrency/retry/reordering/crash behaviour:** scheduled job still wakes.
- **Rejected models:** scheduled time reserves send authority; extend proof to next attempt.
- **Required invariant:** wake revalidates and creates no provider attempt.
- **Recommended JIT shape:** retry scheduling bounded by known proof horizon plus wake-time recheck.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** expiry just before wake.
- **Verdict:** PASS.

## COMM-PT-142 — Protected delivery capability becomes irrecoverable before proof expiry

- **Scenario:** early capability loss makes the still-valid proof impossible to reproduce for delivery.
- **Authority involved:** certified Identity protected-delivery correction.
- **Durable truths and owner:** proof remains Identity truth; capability loss is Communications delivery failure.
- **Concurrency/retry/reordering/crash behaviour:** workers may continue retrying without secret.
- **Rejected models:** reconstruct token from hashes; silently mark delivered; keep retrying impossible work.
- **Required invariant:** terminal/reconciliation-required delivery failure, participant/source recovery path, no secret reconstruction.
- **Recommended JIT shape:** explicit protected-material-unavailable terminal reason within existing intent lifecycle.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** destroy capability mid-backlog.
- **Verdict:** PASS.

## COMM-PT-143 — Proof is consumed while its email remains queued

- **Scenario:** participant consumed proof through another already-delivered path/device before stale queued retry.
- **Authority involved:** Identity challenge consumption.
- **Durable truths and owner:** consumed proof cannot be delivered again.
- **Concurrency/retry/reordering/crash behaviour:** consumption races worker wake.
- **Rejected models:** retry because intent still pending; provider backlog overrides consumption.
- **Required invariant:** no new provider attempt after consumption wins.
- **Recommended JIT shape:** source revalidation before provider attempt.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** consumption/worker both orderings.
- **Verdict:** PASS.

## COMM-PT-144 — Participant resend supersedes old proof while old job remains queued

- **Scenario:** new challenge/new intent created; old outage backlog still contains old work.
- **Authority involved:** Identity resend/supersession.
- **Durable truths and owner:** old intent is source-stopped; new intent is separate logical obligation.
- **Concurrency/retry/reordering/crash behaviour:** old job may execute before or after new.
- **Rejected models:** both send because provider is back; coalesce proofs in Communications.
- **Required invariant:** old source-invalid intent cannot dispatch; only current new intent may.
- **Recommended JIT shape:** same v0.2/v0.4 source-validity contract under backlog.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** reordered old/new jobs after recovery.
- **Verdict:** PASS.

## COMM-PT-145 — Participant repeatedly requests resend during prolonged provider outage

- **Scenario:** many new challenges/intents can be created before delivery resumes.
- **Authority involved:** OQ-035 abuse boundary; Identity resend lifecycle; Communications backlog.
- **Durable truths and owner:** Identity controls accepted resend issuance; Communications owns each resulting intent.
- **Concurrency/retry/reordering/crash behaviour:** stale jobs accumulate.
- **Rejected models:** Communications invents resend threshold; send every historical challenge after recovery; merge challenges by destination.
- **Required invariant:** OQ-035 limits abusive issuance; superseded old intents self-suppress; current challenge remains independently deliverable.
- **Recommended JIT shape:** no Communications resend policy invention; efficient stale-intent reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** burst resend + outage + recovery.
- **Verdict:** PASS / OQ-035 release detail remains.

## COMM-PT-146 — Provider throttling is confused with Identity resend-abuse control

- **Scenario:** provider 429s cause product to reject participant resend requests as “abuse”.
- **Authority involved:** OQ-035 versus OQ-036/Communications provider capacity.
- **Durable truths and owner:** provider capacity is not participant abuse evidence.
- **Concurrency/retry/reordering/crash behaviour:** provider pressure and legitimate resend can overlap.
- **Rejected models:** one global rate limiter governs both semantics.
- **Required invariant:** controls remain distinct, though both may contribute to degraded UX.
- **Recommended JIT shape:** separate source admission and provider delivery admission.
- **Conclusion:** `UPSTREAM_DERIVED` from separated policy layers.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider throttle does not fabricate abuse state.
- **Verdict:** PASS.

## COMM-PT-147 — Oban max-attempts is exhausted before the business delivery obligation is necessarily resolved

- **Scenario:** infrastructure job configuration reaches its execution cap.
- **Authority involved:** Architecture Oban-not-business-truth; Communications intent lifecycle.
- **Durable truths and owner:** unresolved MessageIntent remains Communications truth.
- **Concurrency/retry/reordering/crash behaviour:** job is discarded/dead but source may remain valid.
- **Rejected models:** Oban discarded = business terminal by definition; silently lose intent.
- **Required invariant:** business state decides terminality; unresolved eligible intent is reconciled/re-enqueued/terminalised explicitly according to business policy.
- **Recommended JIT shape:** business retry budget and intent-liveness reconciliation independent of raw Oban count.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** infrastructure-attempt exhaustion with still-valid source.
- **Verdict:** PASS.

## COMM-PT-148 — Business retry budget is exhausted while Oban could technically keep retrying

- **Scenario:** provider failures hit the approved Communications retry ceiling.
- **Authority involved:** Product bounded retry/terminal visibility.
- **Durable truths and owner:** MessageIntent becomes automated-terminal-visible.
- **Concurrency/retry/reordering/crash behaviour:** queued/recreated jobs may still exist.
- **Rejected models:** let Oban continue indefinitely; job config overrides business policy.
- **Required invariant:** no further automated provider attempt; stale execution self-suppresses.
- **Recommended JIT shape:** durable terminal automated state + participant/operator recovery path.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** business budget exhausted with runnable job present.
- **Verdict:** PASS.

## COMM-PT-149 — Oban job disappears but MessageIntent is still unresolved and eligible

- **Scenario:** operator/job cleanup/bug removes execution work.
- **Authority involved:** Class-B must-not-lose liveness.
- **Durable truths and owner:** MessageIntent still exists.
- **Concurrency/retry/reordering/crash behaviour:** no worker will wake naturally.
- **Rejected models:** queue absence means obligation gone; manual database repair only.
- **Required invariant:** durable reconciliation discovers and restores safe execution or surfaces unresolved terminal/requires-attention state.
- **Recommended JIT shape:** liveness reconciler/periodic owner query or transactionally guaranteed equivalent.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** delete/lose job after intent commit.
- **Verdict:** PASS.

## COMM-PT-150 — Oban uniqueness window expires and a duplicate job is inserted

- **Scenario:** duplicate execution work exists for one intent.
- **Authority involved:** Architecture queue uniqueness non-authority.
- **Durable truths and owner:** MessageIntent business idempotency wins.
- **Concurrency/retry/reordering/crash behaviour:** jobs race across nodes.
- **Rejected models:** uniqueness window is exactly-once guarantee.
- **Required invariant:** at most the policy-permitted provider operation is created.
- **Recommended JIT shape:** conditional attempt claim/business idempotency.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate jobs after uniqueness expiry.
- **Verdict:** PASS.

## COMM-PT-151 — Operator retries an automated-terminal MessageIntent while proof is still valid

- **Scenario:** provider recovered; source remains current; previous attempts were definitively failed.
- **Authority involved:** Communications operator action + Identity current validity.
- **Durable truths and owner:** same logical message may still satisfy same source obligation.
- **Concurrency/retry/reordering/crash behaviour:** operator and background reconciliation can race.
- **Rejected models:** terminal means impossible forever; operator resets all counters blindly; create new Identity proof unnecessarily.
- **Required invariant:** authorised explicit recovery can create one new DeliveryAttempt only after full revalidation and preserved history.
- **Recommended JIT shape:** controlled manual-retry action separate from automated retry budget.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** terminal → provider recovery → authorised manual retry.
- **Verdict:** PASS.

## COMM-PT-152 — Operator retries terminal MessageIntent after proof expiry/supersession

- **Scenario:** stale admin UI still exposes retry.
- **Authority involved:** Identity source authority.
- **Durable truths and owner:** source is terminal-invalid.
- **Concurrency/retry/reordering/crash behaviour:** stale command races expiry.
- **Rejected models:** staff override; admin UI state is authority.
- **Required invariant:** server-side retry fails closed and leaks no bearer/destination detail beyond authorised support need.
- **Recommended JIT shape:** current source revalidation inside operator action.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale retry command after expiry.
- **Verdict:** PASS.

## COMM-PT-153 — Operator presses retry while previous DeliveryAttempt outcome is unknown

- **Scenario:** support sees “not delivered” from stale projection, but attempt is unresolved.
- **Authority involved:** provider reconciliation doctrine.
- **Durable truths and owner:** unknown attempt blocks repeat.
- **Concurrency/retry/reordering/crash behaviour:** late callback may arrive simultaneously.
- **Rejected models:** operator override “send again anyway”.
- **Required invariant:** action routes to reconciliation or denies retry until ambiguity resolved.
- **Recommended JIT shape:** distinct reconcile/retry actions and states.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale admin action + late callback.
- **Verdict:** PASS.

## COMM-PT-154 — Operator attempts to manually mark a message delivered/successful

- **Scenario:** support wants to clear failure queue without provider evidence.
- **Authority involved:** Communications provider evidence/business state.
- **Durable truths and owner:** delivery evidence cannot be invented.
- **Concurrency/retry/reordering/crash behaviour:** not material.
- **Rejected models:** manual “mark delivered” closeout; change Identity truth.
- **Required invariant:** operator may classify/reconcile with real evidence or close a recovery task, but cannot fabricate provider delivery.
- **Recommended JIT shape:** no generic manual-success mutation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** authorisation/action surface lacks fabricated-success path.
- **Verdict:** PASS.

## COMM-PT-155 — Operator pauses provider/channel while jobs are queued

- **Scenario:** incident response intentionally stops outbound email.
- **Authority involved:** Product maintenance/degraded modes; Communications execution control.
- **Durable truths and owner:** MessageIntent validity unchanged.
- **Concurrency/retry/reordering/crash behaviour:** in-flight attempts may already exist.
- **Rejected models:** pause cancels intents; pause marks in-flight failure; kill jobs and lose obligations.
- **Required invariant:** new admissions stop; in-flight attempts reconcile; durable intents remain visible.
- **Recommended JIT shape:** provider admission pause separate from intent lifecycle.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** pause during active sends and backlog.
- **Verdict:** PASS.

## COMM-PT-156 — Provider resumes after operator pause

- **Scenario:** many old jobs/intents remain.
- **Authority involved:** current source/content/privacy/provider admission.
- **Durable truths and owner:** resume is not send authority.
- **Concurrency/retry/reordering/crash behaviour:** herd risk.
- **Rejected models:** unpause = release everything.
- **Required invariant:** gradual bounded recovery with per-intent revalidation.
- **Recommended JIT shape:** same outage recovery doctrine as COMM-WD-103.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** resume with mixed stale/live intents.
- **Verdict:** PASS.

## COMM-PT-157 — Platform enters `limited_capability` or `full_maintenance` while verification emails are pending

- **Scenario:** application intentionally limits external delivery.
- **Authority involved:** Product §21J.21.
- **Durable truths and owner:** committed intents survive.
- **Concurrency/retry/reordering/crash behaviour:** mode can change while workers execute.
- **Rejected models:** silently discard; mark sent; extend proof indefinitely.
- **Required invariant:** queue safely where permitted, fail/stop according to source horizon, expose honest degraded state.
- **Recommended JIT shape:** maintenance admission control + durable intent reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** maintenance mode transition around attempt boundary.
- **Verdict:** PASS.

## COMM-PT-158 — Database/transaction cannot establish MessageIntent during Identity issuance

- **Scenario:** provider may be healthy, but durable handoff fails.
- **Authority involved:** certified Identity atomic must-not-lose seam.
- **Durable truths and owner:** no safe delivery obligation exists.
- **Concurrency/retry/reordering/crash behaviour:** transaction error/crash.
- **Rejected models:** commit Identity proof and “send later somehow”; invoke provider synchronously as fallback.
- **Required invariant:** source issuance requiring delivery does not commit without durable intent/protected capability.
- **Recommended JIT shape:** fail closed at transaction-aware owner handoff.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** injected DB failure during handoff.
- **Verdict:** PASS.

## COMM-PT-159 — MessageIntent commits but Oban is temporarily unavailable/not executing

- **Scenario:** database contains durable obligation; executor is down.
- **Authority involved:** Architecture Oban execution machinery vs business truth.
- **Durable truths and owner:** MessageIntent is durable owner truth.
- **Concurrency/retry/reordering/crash behaviour:** executor restart later.
- **Rejected models:** intent lost because no active job process; mark failure immediately merely because queue executor restarted.
- **Required invariant:** execution resumes/reconciles after Oban recovery; current authority rechecked.
- **Recommended JIT shape:** transactionally durable job where sufficient and/or intent-liveness reconciler.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** Oban supervisor/node unavailable after commit then restored.
- **Verdict:** PASS.

## COMM-PT-160 — Provider is degraded while telemetry/exporter is also unavailable

- **Scenario:** operational visibility is poor during the incident.
- **Authority involved:** Engineering observability doctrine; Communications durable evidence.
- **Durable truths and owner:** MessageIntent/DeliveryAttempt remain authoritative despite telemetry failure.
- **Concurrency/retry/reordering/crash behaviour:** logs/metrics missing.
- **Rejected models:** telemetry outage blocks otherwise safe business writes; infer success from absence of errors.
- **Required invariant:** delivery state remains reconstructible from durable business/provider evidence; telemetry failure is failure-isolated.
- **Recommended JIT shape:** minimum durable correlation/provider evidence independent of exporter.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** disable telemetry while exercising provider failures/reconciliation.
- **Verdict:** PASS.

## COMM-PT-161 — Terminal verification-delivery failure must be visible to participant without an in-app inbox

- **Scenario:** provider hard-fails/exhausts retry while Account remains unverified.
- **Authority involved:** FES required-work rule + Identity verification-pending journey.
- **Durable truths and owner:** Communications failure state; Identity verification state.
- **Concurrency/retry/reordering/crash behaviour:** UI may reconnect later.
- **Rejected models:** email-only failure; toast-only error; add InAppNotification solely for this.
- **Required invariant:** Account/verification journey can read/project requires-attention and expose resend/change-email/support action as permitted.
- **Recommended JIT shape:** read/query seam or approved projection from Communications failure state.
- **Conclusion:** `UPSTREAM_DERIVED` plus working specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** terminal failure visible after page reload/reconnect.
- **Verdict:** PASS.

## COMM-PT-162 — UI says “email sent” while provider admission is paused and intent is only queued

- **Scenario:** frontend uses optimistic generic success text.
- **Authority involved:** FES honest pending/degraded state; Communications delivery evidence.
- **Durable truths and owner:** intent queued != provider accepted/sent.
- **Concurrency/retry/reordering/crash behaviour:** outage can last hours.
- **Rejected models:** queued = sent; hide degraded dependency.
- **Required invariant:** participant messaging truthfully distinguishes request accepted/queued from provider submission/delivery where the distinction matters.
- **Recommended JIT shape:** source journey reflects durable state without exposing provider internals unnecessarily.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** degraded provider state surface contract.
- **Verdict:** PASS.

## COMM-PT-163 — Verification and password-recovery messages compete for constrained provider capacity

- **Scenario:** both are required FP-001 security messages.
- **Authority involved:** Product queue priority; source proof expiry.
- **Durable truths and owner:** both remain independently valid obligations.
- **Concurrency/retry/reordering/crash behaviour:** one class could dominate.
- **Rejected models:** one class starves the other indefinitely; arbitrary domain FIFO.
- **Required invariant:** priority/fairness policy preserves bounded progress for still-valid required classes subject to provider capacity.
- **Recommended JIT shape:** workload/freshness/expiry-aware priority classes; exact weights deferred.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** mixed required backlog under constrained throughput.
- **Verdict:** PASS.

## COMM-PT-164 — Future optional marketing backlog is huge while FP-001 security mail arrives

- **Scenario:** mature capability shares provider/channel later.
- **Authority involved:** Product mandatory vs optional priority; Communications queue isolation.
- **Durable truths and owner:** optional work cannot redefine required security priority.
- **Concurrency/retry/reordering/crash behaviour:** large low-priority queue.
- **Rejected models:** universal FIFO across all categories.
- **Required invariant:** still-valid required security work can progress ahead of optional bulk traffic.
- **Recommended JIT shape:** queue/workload isolation by failure/freshness/priority semantics without campaign architecture in FP-001.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** future integration proof when optional traffic exists.
- **Verdict:** PASS / mature-pressure case.

## COMM-PT-165 — Security-message surge itself exceeds provider capacity

- **Scenario:** legitimate registration/recovery burst or attack creates many required intents.
- **Authority involved:** OQ-035 source abuse/admission; Communications provider capacity; Product graceful degradation.
- **Durable truths and owner:** provider capacity does not make every request safe/immediate.
- **Concurrency/retry/reordering/crash behaviour:** burst fan-out across nodes.
- **Rejected models:** unlimited high-priority bypass; provider throttle is the only abuse defence.
- **Required invariant:** source abuse controls and provider admission both apply; capacity pressure degrades/queues safely without fabricated success.
- **Recommended JIT shape:** layered admission + bounded queue recovery.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** legitimate + abusive burst against provider limit.
- **Verdict:** PASS / OQ-035 + OQ-036 release details.

## COMM-PT-166 — Provider-level suppression prevents delivery of a required security message

- **Scenario:** provider refuses an address because of provider-side suppression/bounce policy, while NewYou's source says security message is required.
- **Authority involved:** provider external constraint + Identity source truth.
- **Durable truths and owner:** provider suppression is external evidence/physical limitation, not marketing preference or Identity truth.
- **Concurrency/retry/reordering/crash behaviour:** repeated sends may hard-fail.
- **Rejected models:** reinterpret provider suppression as participant marketing opt-out; keep retrying same provider indefinitely; mark proof successful.
- **Required invariant:** required message reaches terminal/degraded recovery path; Account/source remains unchanged; alternate channel only if separately authorised by OQ-036.
- **Recommended JIT shape:** recipient/provider terminal classification + participant change-email/support recovery.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider suppression on verification destination.
- **Verdict:** PASS / channel fallback remains OQ-036.

## COMM-PT-167 — Automatic second-provider failover after first provider outcome is unknown

- **Scenario:** system considers sending through provider B because provider A timed out.
- **Authority involved:** provider ambiguity + OQ-036 provider selection.
- **Durable truths and owner:** provider A may already have accepted/delivered.
- **Concurrency/retry/reordering/crash behaviour:** failover can duplicate delivery.
- **Rejected models:** automatic failover on timeout; generic provider router now.
- **Required invariant:** reconcile A first or use a future explicitly proven cross-provider idempotency/failover contract.
- **Recommended JIT shape:** no FP-001 automatic multi-provider failover.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** only if OQ-036 later selects multi-provider failover.
- **Verdict:** PASS / REJECT PREMATURE FAILOVER.

## COMM-PT-168 — Provider is definitively unavailable before any attempt and operations want to switch vendors immediately

- **Scenario:** no ambiguous per-message attempt exists, but provider outage prompts operational switch.
- **Authority involved:** OQ-036 launch provider/channel policy; content/security configuration.
- **Durable truths and owner:** MessageIntent is provider-independent; exact adapter/provider is execution choice.
- **Concurrency/retry/reordering/crash behaviour:** backlog may contain no attempt or attempts on old provider.
- **Rejected models:** Communications dossier predefines hot-swappable failover; mutate provider evidence history.
- **Required invariant:** only an authorised OQ-036 operational/provider strategy may redirect eligible unsent work; old attempts retain provider provenance.
- **Recommended JIT shape:** thin provider-independent adapter seam without promising runtime multi-provider failover.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider switch only after provider selection/operations contract exists.
- **Verdict:** PASS / OQ-036.

## COMM-PT-169 — Backlog recovery implementation batches many independent MessageIntents

- **Scenario:** worker claims pages/chunks for efficient recovery.
- **Authority involved:** Communications per-intent truth; Domain scaling profile.
- **Durable truths and owner:** each intent remains independent.
- **Concurrency/retry/reordering/crash behaviour:** batch can partially complete/crash.
- **Rejected models:** batch is one campaign authority; all-or-nothing shared delivery truth; load entire backlog into memory.
- **Required invariant:** per-intent idempotency/revalidation survives partial batch failure.
- **Recommended JIT shape:** bounded pagination/batch claiming only.
- **Conclusion:** `UPSTREAM_DERIVED` plus working specialisation.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** crash mid-batch and restart.
- **Verdict:** PASS.

## COMM-PT-170 — Node restart loses in-memory circuit/rate-control state

- **Scenario:** provider remains degraded, but local execution-control memory is reset.
- **Authority involved:** non-authoritative acceleration/admission state.
- **Durable truths and owner:** provider/intent evidence remains durable.
- **Concurrency/retry/reordering/crash behaviour:** restarted node may briefly re-probe provider.
- **Rejected models:** node-local circuit is correctness authority; reset causes duplicate business effects.
- **Required invariant:** bounded provider probing cannot bypass durable attempt/idempotency/source guards; shared state is introduced only if measured need warrants it.
- **Recommended JIT shape:** execution-control recovery safe by construction; exact shared/Redis mechanism evidence-gated.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** rolling restart during provider outage.
- **Verdict:** PASS.

## COMM-PT-171 — Retry is scheduled just beyond source proof expiry because of provider backoff

- **Scenario:** provider delay says 20 minutes; proof expires in 5.
- **Authority involved:** source expiry versus provider scheduling hint.
- **Durable truths and owner:** proof lifetime wins.
- **Concurrency/retry/reordering/crash behaviour:** job may still be scheduled after expiry.
- **Rejected models:** extend proof; blindly honor provider schedule and later send.
- **Required invariant:** no provider attempt beyond proof lifetime; intent can terminalise/source-stop earlier.
- **Recommended JIT shape:** compute retry schedule within known obligation horizon and still recheck on wake.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** backoff > remaining proof lifetime.
- **Verdict:** PASS.

## COMM-PT-172 — Provider callback arrives after the underlying proof expired

- **Scenario:** old attempt eventually reports delivered after source expiry.
- **Authority involved:** provider evidence versus Identity proof authority.
- **Durable truths and owner:** Communications may record late delivery evidence; Identity expiry stays terminal.
- **Concurrency/retry/reordering/crash behaviour:** callback after terminal source transition.
- **Rejected models:** late delivery revives proof; discard truthful provider evidence because source ended.
- **Required invariant:** evidence remains historical only; no new attempt/source mutation.
- **Recommended JIT shape:** orthogonal attempt evidence and source validity.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** late delivered callback after expiry.
- **Verdict:** PASS.

## COMM-PT-173 — Terminal failure is followed by participant-requested resend

- **Scenario:** original MessageIntent exhausted retry; participant requests a valid resend.
- **Authority involved:** Identity resend lifecycle.
- **Durable truths and owner:** old intent remains terminal historical; new challenge/intent is new logical message.
- **Concurrency/retry/reordering/crash behaviour:** stale old jobs/operator actions may remain.
- **Rejected models:** reopen old source challenge; erase terminal history; merge intents.
- **Required invariant:** new source intent proceeds independently; old intent cannot send.
- **Recommended JIT shape:** existing resend/new-intent contract.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** old terminal + new resend + stale old worker.
- **Verdict:** PASS.

## COMM-PT-174 — Provider idempotency key/window expires while business intent remains retryable

- **Scenario:** selected provider deduplicates requests only for a bounded window.
- **Authority involved:** provider evidence versus platform business idempotency.
- **Durable truths and owner:** MessageIntent identity is durable; provider window is external capability.
- **Concurrency/retry/reordering/crash behaviour:** late retry may no longer be provider-deduped.
- **Rejected models:** provider window defines logical duplicate lifetime.
- **Required invariant:** platform retry/reconciliation strategy remains safe outside provider idempotency window or stops/fails visibly.
- **Recommended JIT shape:** OQ-036 validates provider idempotency/reconciliation capabilities against required retry horizon.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider-specific once selected.
- **Verdict:** PASS / RELEASE-GATED BY OQ-036.

## COMM-PT-175 — Provider returns syntactically successful but semantically incomplete acknowledgement

- **Scenario:** response is 2xx but lacks the evidence required to know whether operation is accepted/trackable.
- **Authority involved:** adapter semantic classification; Engineering Standards.
- **Durable truths and owner:** HTTP class alone is not business meaning.
- **Concurrency/retry/reordering/crash behaviour:** callback/query may later clarify.
- **Rejected models:** every 2xx = accepted; every malformed 2xx = failed.
- **Required invariant:** classify according to provider contract; unresolved if evidence insufficient.
- **Recommended JIT shape:** provider adapter conformance tests under OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** malformed/partial success payloads.
- **Verdict:** PASS / OQ-036.

## COMM-PT-176 — Provider introduces an undocumented/new error response

- **Scenario:** adapter receives status/payload not in its known mapping.
- **Authority involved:** fail-closed provider boundary.
- **Durable truths and owner:** unknown provider response is not safe success/retry by guess.
- **Concurrency/retry/reordering/crash behaviour:** can affect many sends after provider change.
- **Rejected models:** default all unknown codes to retry; default to success.
- **Required invariant:** conservative unresolved/terminal-degraded classification with operator visibility until adapter contract is updated.
- **Recommended JIT shape:** closed normalisation mapping + unknown-case handling.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider contract drift/fuzz test.
- **Verdict:** PASS.

## COMM-PT-177 — Optional Redis/shared rate-control mechanism is unavailable during provider outage

- **Scenario:** future implementation uses Redis only for temporary provider rate coordination and Redis fails.
- **Authority involved:** Domain/Architecture Redis non-authority doctrine.
- **Durable truths and owner:** MessageIntent/DeliveryAttempt remain PostgreSQL authority.
- **Concurrency/retry/reordering/crash behaviour:** rate coordination may degrade.
- **Rejected models:** lose intent/delivery truth; fabricate capacity tokens; Redis outage silently enables unlimited send.
- **Required invariant:** explicit conservative fallback/degraded behaviour; correctness remains in durable business guards.
- **Recommended JIT shape:** do not select Redis now; if later used, document failure mode/proof.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** only if Redis is later selected.
- **Verdict:** PASS / NO REDIS REQUIREMENT.

## COMM-PT-178 — Operator bulk-retries many failed MessageIntents

- **Scenario:** outage is resolved and support wants to retry all failures.
- **Authority involved:** operator authorisation + per-intent current authority + provider capacity.
- **Durable truths and owner:** bulk selection is convenience, not campaign truth.
- **Concurrency/retry/reordering/crash behaviour:** partial bulk execution/crash; some sources expire meanwhile.
- **Rejected models:** one bulk override bypasses per-intent guards; create CommunicationJourney.
- **Required invariant:** each selected intent independently revalidates and creates at most one allowed new attempt.
- **Recommended JIT shape:** bounded bulk command decomposes to owner-safe per-intent actions.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** mixed eligible/ineligible batch with mid-run crash.
- **Verdict:** PASS.

## COMM-PT-179 — Duplicate terminal-failure alerts/escalations are emitted

- **Scenario:** retries/restarts produce repeated operational alerts for one terminal intent.
- **Authority involved:** observability/work management versus Communications business state.
- **Durable truths and owner:** one terminal intent state; alerts are operational projections/work.
- **Concurrency/retry/reordering/crash behaviour:** duplicate events normal.
- **Rejected models:** each alert creates a new retry/message; alert store becomes business authority.
- **Required invariant:** duplicate alerting may be deduped operationally and never multiplies delivery effects.
- **Recommended JIT shape:** stable intent/correlation id for alert dedupe; exact alerting system downstream.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** repeated terminal transition/alert delivery.
- **Verdict:** PASS.

## COMM-PT-180 — Dashboard queue depth/job age is stale during incident

- **Scenario:** operator sees old metrics while actual intents have expired/reconciled.
- **Authority involved:** Product observability; Engineering dashboard non-authority.
- **Durable truths and owner:** dashboard is projection only.
- **Concurrency/retry/reordering/crash behaviour:** metric lag/missing exporter.
- **Rejected models:** operator retries based only on chart; dashboard count defines obligations.
- **Required invariant:** actions resolve current intent/attempt state at execution time.
- **Recommended JIT shape:** correlation from dashboard to authoritative views/actions, never direct authority.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale dashboard + safe operator action.
- **Verdict:** PASS.

## COMM-PT-181 — Provider latency grows sharply without explicit errors

- **Scenario:** requests approach timeout and worker capacity is consumed.
- **Authority involved:** bounded deadlines/bulkheads/provider admission.
- **Durable truths and owner:** high latency is dependency evidence, not message success/failure by itself.
- **Concurrency/retry/reordering/crash behaviour:** slow calls can exhaust worker/provider slots.
- **Rejected models:** unlimited concurrency to compensate; no deadlines; mark slow calls failed before outcome classification.
- **Required invariant:** bounded deadlines/concurrency protect platform; timed-out submissions follow unknown/definitive adapter semantics.
- **Recommended JIT shape:** provider-aware bulkhead/admission thresholds under OQ-036/proof.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** latency injection near deadline.
- **Verdict:** PASS.

## COMM-PT-182 — Account closure/deletion/content withdrawal occurs while an intent sleeps in provider backoff

- **Scenario:** orthogonal current authority changes during retry delay.
- **Authority involved:** cumulative v0.3/v0.5 state + retry scheduling.
- **Durable truths and owner:** scheduling never reserves future send authority.
- **Concurrency/retry/reordering/crash behaviour:** stale job wakes after authority change.
- **Rejected models:** retry schedule bypasses newer authority.
- **Required invariant:** wake revalidates all current authority and suppresses as required.
- **Recommended JIT shape:** one shared current-admission pipeline before every attempt.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** combined closure/deletion/content change while sleeping.
- **Verdict:** PASS.

## COMM-PT-183 — Does unresolved OQ-036 block the provider-independent Communications JIT contract?

- **Scenario:** provider not selected, so exact retry/evidence API is unknown.
- **Authority involved:** Roadmap gate classification + Skeleton dossier requirement.
- **Durable truths and owner:** provider-independent business semantics are already governed; provider-specific operational details remain release gate.
- **Concurrency/retry/reordering/crash behaviour:** semantic classes can be specified without exact numeric policy.
- **Rejected models:** choose provider in JIT to make semantics concrete; block Phase 7C merely because vendor is unresolved; omit retry semantics entirely.
- **Required invariant:** JIT fixes required provider-independent invariants while explicitly leaving vendor-specific mappings/numbers to OQ-036.
- **Recommended JIT shape:** thin adapter contract + stable platform outcome taxonomy + release gate.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider selected under OQ-036 must demonstrate it can satisfy the contract.
- **Verdict:** **PASS — OQ-036 DOES NOT BLOCK COMMUNICATIONS JIT/7C SEMANTICS; IT BLOCKS RELEASE.**

## COMM-PT-184 — Selected future provider cannot reconcile unknown outcomes or provide sufficient delivery evidence

- **Scenario:** OQ-036 vendor candidate lacks capability needed by accepted Communications invariants.
- **Authority involved:** OQ-036 vendor/operations review + Architecture provider reconciliation.
- **Durable truths and owner:** provider limitation cannot weaken NewYou correctness contract silently.
- **Concurrency/retry/reordering/crash behaviour:** timeout/unknown cases become unsafe.
- **Rejected models:** downgrade unknown to retryable because vendor is cheap/easy; rely on best effort.
- **Required invariant:** vendor/adapter strategy must satisfy the accepted contract or OQ-036 must reject/change the provider/operational approach; if no viable provider can satisfy law, STOP upstream for architecture/product review.
- **Recommended JIT shape:** provider capability acceptance checklist at OQ-036/Phase 8.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO now; possible future STOP only with concrete provider evidence.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** vendor-specific conformance.
- **Verdict:** PASS WITH FUTURE OQ-036 FAIL-CLOSED GATE.

## COMM-PT-185 — Does provider outage/operator recovery require the Audit & Evidence conditional dossier now?

- **Scenario:** terminal failures, operator retries, incident links and provider evidence exist.
- **Authority involved:** Audit Domain Law + Skeleton conditional rule.
- **Durable truths and owner:** DeliveryAttempt/provider evidence belongs Communications; central Audit owns only approved minimum security/privilege/incident evidence.
- **Concurrency/retry/reordering/crash behaviour:** audit/telemetry may be async but cannot become retry authority.
- **Rejected models:** move all provider history into Audit; require Audit dossier solely because support action exists; keep no evidence for privileged retry where existing Audit law requires it.
- **Required invariant:** Communications retains delivery evidence; operator/privileged/material security actions emit bounded Audit evidence under current authority where applicable.
- **Recommended JIT shape:** use existing Audit owner interface; pull Audit dossier only if exact new Audit-owned lifecycle/retention/access semantics become necessary.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** **NO.**
- **Later executable proof:** operator retry/reconcile emits required minimum audit evidence without secret/provider-payload leakage.
- **Verdict:** PASS.

---

# 70. Rejected-model register additions — v0.6.0

91. **A job execution is a DeliveryAttempt.** Rejected: policy/provider deferral and internal rendering can occur without provider operation.
92. **Create DeliveryAttempt only after provider returns.** Rejected: crash after external submission would lack durable provider-operation identity.
93. **HTTP/provider timeout means failure and is safe to retry.** Rejected.
94. **`unknown` is just another retryable error.** Rejected.
95. **Oban max-attempts is the Communications business retry budget.** Rejected.
96. **Recreating an Oban job resets retry policy.** Rejected.
97. **Retry forever while provider remains unavailable.** Rejected by Product/Architecture bounded retry.
98. **Extend verification/reset proof lifetime to accommodate provider outage.** Rejected.
99. **Drain backlog FIFO before checking source validity.** Rejected.
100. **Every worker independently discovers provider outage and runs its own retry loop.** Rejected; shared outage requires coordinated degradation.
101. **Provider Retry-After overrides proof/source expiry.** Rejected.
102. **Provider rate-limit counters are business delivery authority.** Rejected.
103. **Redis/circuit state may replace durable MessageIntent/DeliveryAttempt truth.** Rejected.
104. **Provider idempotency means platform business idempotency is unnecessary.** Rejected.
105. **One hard-bounced address means the whole provider is unhealthy.** Rejected.
106. **One provider outage means all previous successful sends are failed.** Rejected.
107. **Automated terminal failure can be cleared by simply resetting attempt counters.** Rejected.
108. **Operator retry bypasses source/content/privacy/proof checks.** Rejected.
109. **Operator can retry an unresolved/unknown attempt anyway.** Rejected.
110. **Operator can manually mark delivery success without evidence.** Rejected.
111. **Pause/resume provider mutates MessageIntent business authority.** Rejected.
112. **Resume means release the entire backlog immediately.** Rejected.
113. **Provider outage requires an FP-001 in-app inbox.** Rejected.
114. **Provider failure rolls back already-committed Identity challenge/source truth.** Rejected.
115. **Communications coalesces distinct Identity resend challenges to reduce backlog.** Rejected.
116. **During provider outage, commit Identity issuance even if durable MessageIntent/capability handoff failed.** Rejected.
117. **Maintenance may silently drop notification work because users can retry later.** Rejected.
118. **Automatic multi-provider failover on timeout is a generic safety improvement.** Rejected; can multiply delivery.
119. **Batch recovery implies CommunicationJourney/campaign authority.** Rejected.
120. **Dashboard/metrics state is safe retry authority.** Rejected.
121. **Telemetry failure means provider outcome is unknowable even when durable attempt evidence exists.** Rejected.
122. **Provider-side suppression is equivalent to participant marketing opt-out or canonical email invalidity.** Rejected.
123. **Unknown/undocumented provider response defaults to success or retry.** Rejected.
124. **OQ-036 must be resolved before Communications can define any retry/provider semantics.** Rejected by Roadmap `BLOCKS_RELEASE_ONLY` classification.

---

# 71. Upstream-delta register — v0.6.0

## Required upstream amendments

No new Product/Architecture/Domain/Roadmap amendment was discovered in this cluster.

`COMM-UPD-001` from v0.5.0 remains the only current required upstream artifact correction:

> narrow certified Identity dossier PATCH correcting message-body/template ownership before Communications final JIT certification / Phase 7C freeze.

## No OQ-036 escalation yet

`OQ-036` remains correctly classified as `VENDOR / OPERATIONS REVIEW` and `BLOCKS_RELEASE_ONLY` for FP-001.

This cluster found no evidence requiring it to be promoted into a Phase-7C blocker.

A future selected provider **would** force a STOP at `OQ-036` / Architecture if concrete evidence showed that no safe adapter/reconciliation strategy can satisfy the accepted provider-independent semantics.

That is a future evidence-triggered gate, not a current amendment.

---

# 72. Unresolved-gate register additions — v0.6.0

| Gate / open matter | v0.6.0 effect |
|---|---|
| `COMM-UPD-001` | Still blocks Communications final certification / Phase 7C freeze; unrelated to provider outage semantics. |
| `OQ-036` provider/channel policy | **Release-only** for FP-001. Must later select provider/channel implementation, exact retry/backoff/deadline policy, provider evidence/reconciliation capability and operational limits. |
| Exact retry count/backoff | Deliberately unresolved. Must remain bounded/error-class-aware/jittered and inside source/protected-capability horizon. |
| Provider timeout semantics | Stable platform rule is unknown/reconciliation where acceptance cannot be excluded; exact transport/status mapping is provider-specific. |
| Provider `Retry-After` interpretation | May inform scheduling; exact support/trust/cap remains provider-specific. |
| Provider idempotency support/window | Must be validated under OQ-036; never replaces platform idempotency. |
| Provider reconciliation API/callbacks | Must be validated under OQ-036. Provider without sufficient strategy may fail the launch gate. |
| Queue names/concurrency/Oban settings | JIT/Phase-8 mechanism/proof detail; no current authority requires exact values now. |
| Shared outage/circuit mechanism | Semantics required; Redis/ETS/PostgreSQL/library selection evidence-gated. |
| Operator alert/on-call ownership | Actionable visibility required; broad incident command remains governed separately and `OQ-038` is not pulled into FP-001. |
| OQ-035 | Resend/request abuse thresholds remain distinct from provider capacity/rate control. |

---

# 73. Cross-stream dependency register additions — v0.6.0

| Stream / Domain | v0.6.0 finding |
|---|---|
| Identity & Access | Owns challenge/proof validity, resend/supersession/consumption and destination truth. Provider outage cannot extend or complete Identity proof. |
| Content & Media | Exact bound content must remain eligible on every new provider attempt; outage/retry cannot preserve withdrawn content authority. |
| Privacy & Consent | Current permission/deletion/closure suppression still revalidated where applicable; provider retry state cannot restore withdrawn permission. |
| Audit & Evidence | Central evidence remains bounded/minimal; provider history stays Communications-owned. No conditional Audit dossier pull-forward. |
| Engineering Standards | Normalised provider errors, unknown-outcome discipline and bounded observability are supporting authority for implementation/proof. |
| OQ-035 | Owns source/action abuse thresholds, not provider throughput. |
| OQ-036 | Owns launch provider/channel choice and provider-specific operational policy; does not block provider-independent JIT semantics. |
| Operations | Needs actionable backlog/provider/terminal visibility and safe pause/reconcile/retry controls; dashboards remain projections. |
| Oban | Core executor, not business authority. Job uniqueness/max-attempts cannot define MessageIntent idempotency/terminality. |

---

# 74. Conditional-dossier adjudication — v0.6.0

## Audit & Evidence

**Disposition: `CONDITIONAL / NOT PULLED FORWARD`.**

This cluster was the strongest test so far for the Audit conditional and still did not justify a separate FP-001 Audit JIT dossier.

Current authority already answers the necessary ownership:

- Communications owns MessageIntent, DeliveryAttempt, provider evidence and terminal failure;
- generic operational logs/metrics/traces are not Audit authority;
- Audit owns only approved minimum append-only security/privilege/incident evidence;
- privileged/operator actions can emit bounded audit evidence through the existing owner boundary;
- Audit evidence cannot become retry/delivery authority.

**Pull-forward trigger:** Phase 7C would need a new implementation-grade Audit-owned lifecycle, retention class/access contract or incident-evidence semantic not already frozen. None was exposed here.

## Privacy & Consent

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD` for required FP-001.**

The v0.4 mailing-list trigger remains the only current conditional pull-forward case.

## Content & Media

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD`.**

Provider outage adds no new C&M lifecycle semantics.

---

# 75. OQ-036 provider-independent JIT boundary — v0.6.0

## Communications JIT may freeze now

- MessageIntent and DeliveryAttempt ownership/lifecycles;
- durable provider-operation identity before external submission;
- source/content/privacy/preference revalidation before new provider attempt;
- stable normalised provider outcome classes;
- `unknown != retryable`;
- no blind duplicate retry after ambiguous submission;
- bounded retry requirement;
- business retry state independent of Oban counters;
- proof/capability expiry pre-empts delivery retry;
- terminal failure visibility;
- operator retry/reconcile/pause semantic boundaries;
- coordinated shared-outage degradation;
- backlog recovery revalidation/jitter/priority/fairness requirements;
- no automatic multi-provider failover assumption;
- telemetry non-authority and sensitive-data minimisation;
- liveness/reconciliation requirement for stranded durable intents.

## OQ-036 must decide later

- launch email provider and exact in-app implementation/channel policy;
- provider API/SDK;
- exact connect/request/read deadlines;
- exact provider-specific response/error mappings;
- exact automated retry counts and delay sequence;
- `Retry-After` handling details;
- exact concurrency/provider throughput budgets;
- circuit/shared-rate-control implementation;
- provider idempotency capability/window/key format;
- provider message/query/callback reconciliation capability;
- provider suppression/bounce semantics and operational playbooks;
- any authorised alternate-channel/failover policy;
- provider costs/limits/credentials and release runbooks.

## Release acceptance condition

The eventual selected provider/adapter must prove that it can implement the frozen provider-independent contract.

If it cannot, the solution is **not** to weaken Communications semantics silently. Reject/change provider/operations strategy or STOP at the correct Architecture/Product authority if concrete evidence proves the requirement infeasible.

---

# 76. Later executable proof-obligation register additions — v0.6.0

108. Durable DeliveryAttempt/provider-operation identity exists before a submission can become ambiguous, but no attempt is created for render/policy/provider-admission deferral.
109. Crash after attempt preparation but before network I/O recovers without fabricated acceptance or duplicate logical message.
110. Crash after request handoff and before response/state commit yields unresolved/reconciliation state, never blind retry.
111. Provider timeout + late acceptance/delivery proves `unknown != retryable`.
112. Adapter-proven pre-submission connection failure can retry safely within bounded policy.
113. Provider 429/Retry-After across many intents does not produce a synchronized herd and never extends proof lifetime.
114. Provider credential/config failure triggers coordinated degradation rather than per-intent retry storm.
115. Sustained provider 5xx outage preserves durable intents and bounded/jittered recovery.
116. Recipient-specific hard rejection does not pause healthy recipients or mutate Identity canonical email.
117. Mixed provider partial failure preserves definitive successes while retrying/reconciling only eligible operations.
118. Duplicate workers on separate BEAM nodes cannot create multiple provider operations outside policy.
119. Kill process after provider accepted response but before local commit; reconcile without duplicate send.
120. Duplicate/reordered callbacks converge idempotently and never alter source proof truth.
121. Provider recovery with large backlog stays inside configured DB/CPU/provider budgets and does not thundering-herd.
122. Majority-expired backlog is suppressed before consuming provider capacity.
123. Proof expiry, consumption, supersession and revocation racing retry wake all prevent stale new provider attempts.
124. Protected capability early loss terminates/reconciles visibly without reconstructing bearer material.
125. Repeated participant resend during outage leaves only current source-authorised intent dispatchable; OQ-035 controls abuse separately.
126. Oban max-attempt exhaustion cannot silently lose an unresolved eligible MessageIntent.
127. Business retry-budget exhaustion prevents further automatic sends even if execution jobs remain runnable.
128. Lost/deleted Oban job for unresolved MessageIntent is detected by liveness reconciliation and safely restored/surfaced.
129. Duplicate job after Oban uniqueness-window expiry remains business-idempotent.
130. Authorised operator manual retry after automated terminal failure revalidates all current authority and preserves previous attempt history.
131. Operator retry after source expiry/deletion/content withdrawal fails closed.
132. Operator retry on unknown attempt is denied/routed to reconciliation.
133. No operator action can fabricate provider delivery success.
134. Provider pause stops new admissions without losing intents or rewriting in-flight evidence.
135. Provider resume gradually revalidates mixed stale/live backlog.
136. Limited/full maintenance preserves must-not-lose intent and honest participant state without extending proof lifetime.
137. Failure to establish MessageIntent/protected capability prevents committed source issuance requiring that delivery.
138. Oban executor outage after durable commit recovers/reconciles from durable intent.
139. Telemetry/exporter outage during provider failure does not change business truth and durable evidence remains enough to reconcile.
140. Terminal verification delivery failure remains visible after reload/reconnect through the Identity/account recovery journey without requiring in-app inbox.
141. Participant UX distinguishes queued/degraded from provider-submitted/delivered state accurately enough not to fabricate success.
142. Mixed verification/recovery required backlog demonstrates priority with bounded fairness under constrained provider capacity.
143. Future optional bulk traffic cannot starve still-valid required security work.
144. Security burst proves OQ-035 source abuse control and OQ-036 provider capacity control remain distinct.
145. Provider-side suppression of required security delivery yields terminal/recovery behaviour without becoming marketing preference or Account-email authority.
146. Unknown first-provider outcome cannot trigger automatic second-provider failover.
147. Bounded batch backlog recovery survives mid-batch crash with per-intent idempotency.
148. Rolling node restart during outage cannot reset business retry state or create duplicate delivery because circuit/rate state was local/derived.
149. Provider delay longer than remaining proof lifetime produces no post-expiry attempt.
150. Late provider callback after proof expiry records historical evidence only and cannot revive source authority.
151. Participant resend after terminal failure creates new source/MessageIntent while old terminal work stays inert.
152. Provider idempotency-window expiry does not redefine platform logical duplicate lifetime.
153. Syntactically successful but semantically incomplete provider response is not guessed into success/retry.
154. Unknown/new provider response mapping fails conservatively and becomes operator-visible.
155. If shared Redis/rate-control acceleration is later adopted, its outage cannot fabricate capacity/send authority and must have explicit degraded behaviour.
156. Bulk operator retry decomposes to independently revalidated per-intent actions and survives partial failure.
157. Duplicate terminal alerts do not multiply retries/messages.
158. Stale dashboards cannot authorise unsafe retry; server action resolves current intent/attempt state.
159. Provider latency/bulkhead fault injection demonstrates bounded worker/resource consumption and correct unknown classification at deadline.
160. Combined closure/deletion/content withdrawal during provider backoff prevents stale send on wake.
161. OQ-036 provider conformance proof validates timeout/error mapping, idempotency, reconciliation, callback authenticity/order handling, throughput limits and delivery-evidence sufficiency before release.
162. Operator retry/reconcile/pause actions emit the currently required minimum Audit evidence without secret/provider-payload leakage and without making Audit business authority.

---

# 77. Resource-discipline review — cumulative through v0.6.0

## `MessageIntent`

**REQUIRED.**

Provider outage/backlog strengthens its independent durable lifecycle:

- survives executor/provider outage;
- carries current automated-terminal/deferred/reconciliation visibility;
- anchors liveness when execution jobs disappear;
- retains business retry/idempotency state independent of Oban.

## `DeliveryAttempt`

**REQUIRED.**

v0.6.0 strengthens its meaning as the durable identity/evidence for one prepared/executed provider operation, including ambiguous outcomes requiring reconciliation.

## `ProviderOutage`

**NOT JUSTIFIED as a Communications business Resource.**

Shared provider-health/circuit/rate state is operational execution/admission state. A durable incident/work record may exist elsewhere when operational governance requires it, but provider health does not own message truth.

## `RetryBudget`

**NOT JUSTIFIED as a separate Resource.**

Retry policy/state is a lifecycle dimension of MessageIntent/DeliveryAttempt and provider execution policy unless future evidence proves an independently governed object.

## `DeliveryReconciliationCase`

**NOT JUSTIFIED for FP-001 at present.**

Unknown/reconciliation-required state can be represented on the affected DeliveryAttempt plus bounded operator work/projection. A separate case Resource requires evidence of independent long-lived workflow, assignment or multi-operation lifecycle.

## `OperatorRecoveryCase`

**NOT JUSTIFIED.**

Existing support/work patterns can project terminal Communications obligations and invoke owner actions. Do not create a Domain Resource merely because an operator may need to act.

## `Provider`

**NOT a new business Resource requirement from this pass.**

Provider/channel adapter configuration may need governed implementation/configuration later, but provider identity does not become Communications business authority merely because attempts reference it.

## `CommunicationJourney`

**Still not required.**

Backlog batches/bulk retries are operational grouping over independent MessageIntents, not journey truth.

## `InAppNotification`

**Still not required for FP-001.**

Terminal failure recovery is represented in the owning account/verification/recovery journey.

**Cumulative required FP-001 Communications Resource verdict remains:**

```text
MessageIntent
DeliveryAttempt
```

---

# 78. Completeness / stabilisation assessment — v0.6.0

**NOT YET STABLE FOR GOVERNED COMMUNICATIONS JIT DOSSIER DRAFTING.**

The provider-outage/backlog/retry scenario class is now provisionally stable enough to stop broadening it.

The major conclusions are converging rather than expanding the model:

```text
MessageIntent
+ DeliveryAttempt
+ protected capability machinery where required
+ thin provider adapter
+ provider-independent outcome taxonomy
+ bounded retry/reconciliation
+ execution admission/degradation controls
```

No new business Resource was justified.

`OQ-036` does **not** prevent an implementation-grade provider-independent Communications JIT contract. It remains the proper release gate for provider/channel selection and exact operational parameters.

No new upstream Product/Architecture/Domain/Roadmap amendment was discovered.

`COMM-UPD-001` remains the one existing blocker to **final Communications JIT certification / Phase 7C freeze**.

The next materially distinct pass should be:

## Audit / observability / evidence and operator-security boundary

Pressure-test:

- which Communications actions require central Audit evidence versus only Communications provider evidence;
- actor/system causation for create/retry/reconcile/pause/resume;
- privileged retry/bulk retry access boundaries;
- support visibility minimisation;
- correlation ids and high-cardinality leakage;
- raw provider payload retention;
- delivery/open/click evidence versus Analytics;
- logs/telemetry cardinality and destination leakage;
- terminal-failure work queues versus Audit;
- incident/security-event linkage;
- provider credential/secret leakage;
- evidence retention/deletion;
- operator action replay/idempotency;
- whether Audit & Evidence finally needs a conditional dossier.

After that, perform the channel/provider-independent architecture pass (`email` versus `in_app`, future SMS/WhatsApp, no premature abstractions, batch/fan-out) and then the final combined adversarial/stabilisation sweep.

---

# 79. v0.7.0 semantic delta — Audit, observability, operator security and evidence boundaries

This successor preserves all accepted v0.1.0–v0.6.0 findings and adds the seventh substantive Communications pressure-test cluster.

The live repository was rechecked immediately before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

This pass pressure-tests:

- Communications delivery/provider evidence versus central Audit evidence;
- automated execution versus privileged operator action evidence;
- operator retry, reconciliation, pause/resume, suppression and bulk work;
- stale operator screens and concurrent provider/source transitions;
- support visibility minimisation;
- destination masking/reveal;
- raw provider request/response/webhook payloads;
- provider credentials and adapter exceptions;
- message-body and protected-bearer leakage;
- correlation identifiers;
- metric cardinality;
- structured logs and traces;
- alert/dashboard authority;
- terminal-failure work projections;
- invalid provider callbacks and callback-authentication failures;
- provider dashboards/manual provider operations;
- delivery/open/click evidence versus Analytics;
- provider link rewriting and click tracking;
- corporate/link-security prefetch of protected action URLs;
- telemetry exporter failure;
- Audit evidence failure;
- evidence retention/deletion/legal hold;
- incident linkage;
- whether Audit & Evidence must be pulled forward.

This pass introduces no observability vendor, SIEM, APM backend, logging vendor, provider, provider dashboard workflow or exact Audit Resource/event schema.

---

# 80. Evidence-class matrix — v0.7.0

The following classes are intentionally distinct.

| Evidence class | Authority / owner | What it proves | What it does **not** prove |
|---|---|---|---|
| Communications business evidence | Communications | logical MessageIntent state; DeliveryAttempt/provider-operation history; normalized provider outcome; reconciliation status | Identity verification, provider physical truth beyond received evidence, consent, Account truth, conversion |
| Source business evidence | Identity & Access or other originating Domain | proof/operation/account/source truth | provider send/delivery truth |
| Central Audit/security evidence | Audit & Evidence | that a governed sensitive/privileged/security action/access/incident occurred with bounded actor/cause/linkage | underlying Communications/Identity business state |
| Operational telemetry | observability pipeline | operational behaviour, latency, counts, queue/backlog/provider health, diagnostics | business success, permission, delivery authority, audit completion |
| Analytics | Analytics | approved derived measurement facts | provider/business authority, permission, verification, source truth |
| Operator/support UI | projection over authorised reads/actions | current authorised operational view | durable truth merely because it is displayed |
| Provider dashboard/report | external evidence | provider-reported state under provider semantics | NewYou business authority, consent, Identity proof state, Audit truth |

A system may correlate these classes. It must not collapse them into one store or one authority.

---

# 81. Upstream security delta discovered — protected-link prefetch / scanner consumption

## COMM-UPD-002 — automated URL fetch must not be sufficient to complete a protected Identity transition

**Classification:** LOCAL WORKING UPSTREAM-DELTA LABEL ONLY. Not a governed DEC/ARC/OQ/FP identifier.

### Scenario

Email providers, corporate mail gateways, anti-phishing products, browser preview systems and security scanners may:

- rewrite links;
- perform `HEAD`/`GET` requests;
- follow redirects;
- prefetch destination pages;
- inspect query parameters;
- fetch links before the participant sees the message.

Current Identity dossier v0.1.3 correctly makes Identity the sole authority for proof consumption and states that email verification changes only through consuming a valid purpose-bound proof.

However, the current certified lifecycle does not explicitly state the HTTP/user-interaction boundary that prevents an automated mail/security scanner from becoming the effective proof consumer.

No current authority was found that permits an email/provider/security scanner to establish verification/recovery/email-change truth merely by fetching the bearer URL.

### Required invariant

For verification, password reset/recovery and primary-email-change protected links:

> automated provider/mail-security/browser-prefetch retrieval must not by itself complete the protected Identity transition.

The exact safe interaction may differ by purpose. This Pre-JIT record does **not** select:

- a GET-versus-POST design;
- confirmation-page UX;
- CSRF mechanics;
- AshAuthentication route details;
- exact token presentation scheme.

It only requires the Identity boundary to distinguish **link retrieval/prefetch** from the protected transition in a way that preserves current Identity proof authority.

For password reset/recovery/email change, a fetched link must not itself change credentials or canonical email.

For email verification, the selected interaction must prove that expected automated fetch behaviour cannot mark the Account verified without the intended participant interaction boundary.

### Routing

This is an **Identity & Access JIT semantic**, not a Communications workaround.

Disabling provider click rewriting helps but is insufficient because independent corporate/security scanners may still fetch links.

The smallest safe correction is an Identity dossier successor/clarification that preserves the existing proof lifecycle while adding scanner/prefetch-safe protected-link consumption semantics.

### Stop effect

```text
Communications Pre-JIT discovery
→ MAY CONTINUE

Communications final cross-domain certification / Phase 7C freeze
→ BLOCKED / STOP until COMM-UPD-002 is either
   (a) resolved by a narrow Identity successor, or
   (b) explicitly routed to a downstream Identity proof contract by the governed process
```

No Product, Architecture or Domain Law amendment is currently indicated.

---

# 82. Accepted working-design register additions — v0.7.0

## COMM-WD-121 — Communications business evidence is not central Audit evidence

**Status:** `UPSTREAM_DERIVED`

Communications remains authoritative for:

- MessageIntent lifecycle;
- DeliveryAttempt/provider-operation history;
- normalized provider evidence;
- unknown/reconciliation-required delivery state;
- terminal delivery failure.

Audit & Evidence does not become a second delivery ledger.

An Audit Event may link to a Communications intent/attempt, but cannot replace, correct or authorise it.

## COMM-WD-122 — Automated delivery events do not require one central Audit event per attempt/callback

**Status:** `WORKING_DESIGN_ACCEPTED`

Ordinary automated:

- queue execution;
- retry scheduling;
- provider submission;
- provider callback;
- bounce/delivery evidence;
- reconciliation progress

remain durably represented in Communications.

Central Audit duplication of every automatic event would create:

- competing historical stores;
- unnecessary sensitive/cardinality load;
- retention ambiguity;
- false pressure to reconstruct delivery state from Audit.

Audit evidence is added only where current policy requires sensitive/privileged/security/governance evidence.

## COMM-WD-123 — Privileged manual Communications mutations require bounded Audit evidence

**Status:** `UPSTREAM_DERIVED` plus Communications specialisation

Material manual actions such as an authorised operator:

- retrying after automated terminal closeout;
- initiating/confirming reconciliation;
- pausing/resuming provider execution where this changes live operation;
- suppressing/cancelling eligible work under a governed owner action;
- performing approved bulk recovery;
- invoking break-glass access/action

require minimum central Audit/security evidence.

The semantic evidence contract includes at least:

- named actor/system causation;
- current scoped grant/assurance context or safe reference;
- action class;
- safe target reference(s);
- reason where required;
- result/outcome;
- timestamp/provenance/correlation;
- no secret-bearing payload.

Exact Audit Resource/event names remain Audit implementation/JIT detail.

## COMM-WD-124 — Required Audit establishment is fail-closed for privileged provider-mutating action

**Status:** `WORKING_DESIGN_ACCEPTED`

Where current policy makes Audit evidence mandatory for a privileged operator action that may cause a provider mutation:

```text
authorise operator action
→ durably establish required audit evidence/intention
→ only then permit provider-mutating execution
```

If the required Audit evidence cannot be durably established, the privileged action fails closed.

The exact cross-Domain transaction/durable-consequence mechanism remains implementation detail.

This rule does **not** mean telemetry/exporter failure blocks valid business work.

## COMM-WD-125 — Telemetry failure is failure-isolated and never fabricates business failure/success

**Status:** `UPSTREAM_DERIVED`

Metrics, trace and log exporter failure may reduce visibility.

It must not:

- mark an intent failed;
- mark an attempt delivered;
- revoke retry authority;
- make a valid provider callback fail after Communications evidence was durably committed;
- create Identity proof state.

Durable business evidence remains independent of telemetry.

## COMM-WD-126 — Support/operator views are minimum-necessary projections, not action authority

**Status:** `UPSTREAM_DERIVED`

A support/communications workspace may show only the information needed for the current permitted task, such as:

- communication role;
- safe destination display/mask;
- current intent status;
- current source eligibility summary;
- attempt timestamps/outcome class;
- retry/reconciliation availability;
- bounded normalized terminal reason.

Merely seeing a button, row, queue item or stale status does not grant action authority.

Every material action revalidates current policy/state server-side.

## COMM-WD-127 — Destination is masked by default in operator projections

**Status:** `WORKING_DESIGN_ACCEPTED`

The full destination is personal contact data.

Operator/support projections default to a useful masked form.

Full destination reveal is permitted only where:

- the actor has a current scoped need;
- the action genuinely requires it;
- the reveal is policy-authorised;
- sensitive access evidence is recorded where current Audit policy requires it.

No operator view exposes protected bearer material.

## COMM-WD-128 — Operator retry and operator reconciliation are separate owner actions

**Status:** `WORKING_DESIGN_ACCEPTED`

```text
RECONCILE
→ resolve/refresh evidence about an existing ambiguous provider operation

RETRY
→ authorise a genuinely new provider operation
```

An operator cannot use `retry` to bypass unresolved ambiguity.

A `reconcile` action does not itself send another message.

The UI/command contract must make the distinction explicit.

## COMM-WD-129 — Operator actions are idempotent, concurrency-safe and stale-command-safe

**Status:** `WORKING_DESIGN_ACCEPTED`

Duplicate button clicks, browser retries, two staff members and concurrent automated work must converge.

A privileged action command uses:

- operation identity/idempotency;
- current intent/attempt revision;
- current source/privacy/content authority;
- current provider ambiguity state.

A stale action fails/rebases safely rather than replaying an old decision.

## COMM-WD-130 — Operator may not edit historical DeliveryAttempt/provider evidence in place

**Status:** `WORKING_DESIGN_ACCEPTED`

Historical provider evidence is append/reconciliation-oriented.

An operator must not simply change:

```text
unknown → delivered
failed → delivered
```

because a dashboard or participant report suggests it.

New evidence/reconciliation outcome is added with provenance.

Corrections do not falsify the original external observation.

## COMM-WD-131 — Routine provider-dashboard/manual send bypass is prohibited

**Status:** `WORKING_DESIGN_ACCEPTED`

Normal operator recovery must run through NewYou's Communications owner actions.

Directly clicking “send” or “resend” inside a provider dashboard would bypass:

- source validity revalidation;
- privacy/preference checks;
- content binding;
- protected-capability rules;
- business idempotency;
- DeliveryAttempt creation;
- platform Audit.

Therefore it is not an approved routine FP-001 recovery path.

Any later true emergency provider-side action would require explicit break-glass governance, reconciliation and evidence; this Pre-JIT does not create such a path.

## COMM-WD-132 — Provider dashboard status is external evidence only

**Status:** `UPSTREAM_DERIVED`

An operator may consult provider state during reconciliation.

The provider dashboard cannot directly establish NewYou delivery truth.

A governed reconciliation action must ingest/normalize the relevant evidence into Communications before platform state changes.

Screenshots/manual notes alone are not delivery authority.

## COMM-WD-133 — Raw provider payload retention is opt-in, not default

**Status:** `WORKING_DESIGN_ACCEPTED`

The adapter should normally persist only the minimum normalized evidence needed for:

- idempotency;
- reconciliation;
- provider operation identity;
- delivery/failure classification;
- approved troubleshooting.

Full provider request/response/webhook bodies are not retained merely because they are available.

If a selected provider later requires some raw artifact for dispute/reconciliation/security proof, `OQ-036`/retention policy must justify:

- exact fields;
- purpose;
- access;
- protection;
- retention;
- deletion.

## COMM-WD-134 — Provider credentials and signing secrets never enter business evidence, Audit, logs or telemetry

**Status:** `UPSTREAM_DERIVED`

API keys, webhook secrets, signing material and authentication headers belong only to the protected integration configuration boundary.

They are excluded from:

- MessageIntent;
- DeliveryAttempt ordinary fields;
- Audit events;
- job args;
- structured logs;
- traces;
- metrics;
- Analytics;
- operator UI;
- error messages.

Credential rotation changes integration configuration, not delivery business history.

## COMM-WD-135 — Protected bearer material and secret-bearing rendered bodies are excluded from observability and Audit

**Status:** `UPSTREAM_DERIVED`

No protected verification/reset/recovery/email-change bearer may appear in:

- log message;
- trace attribute;
- metric label;
- span event;
- error exception payload;
- central Audit event;
- Analytics event;
- support note;
- operator export.

Full rendered security-message bodies are likewise not required in those surfaces.

## COMM-WD-136 — Correlation uses opaque safe identifiers and is not business authority

**Status:** `WORKING_DESIGN_ACCEPTED`

A workflow may carry safe opaque correlation across:

```text
source transition
→ MessageIntent
→ execution job
→ DeliveryAttempt
→ provider operation
→ callback/reconciliation
→ privileged operator action
→ Audit linkage
```

Rules:

- correlation identifiers contain no email/phone/name/token/PMR/business meaning;
- they are not authentication, authorisation or idempotency authority;
- collision/reuse cannot merge business records;
- high-cardinality correlation is not used as a metric label;
- provider exposure is only where useful and safe.

The durable source/intent/attempt ids remain their own business identities.

## COMM-WD-137 — Provider operation IDs are scoped evidence, not global business keys

**Status:** `WORKING_DESIGN_ACCEPTED`

A provider message/event id is interpreted within the selected provider/account/channel boundary.

It must not become the sole NewYou MessageIntent identity.

If a provider duplicates/reuses identifiers unexpectedly, internal attempt identity and causal provenance preserve correctness.

## COMM-WD-138 — Metrics use bounded dimensions, never participant identifiers

**Status:** `UPSTREAM_DERIVED`

Useful Communications metric dimensions may include bounded values such as:

- message role/category;
- channel;
- normalized outcome class;
- queue/execution class;
- provider adapter name where approved;
- environment;
- retry/reconciliation class.

Metrics must not use as labels:

- full email/phone;
- Account id;
- PMR;
- MessageIntent id;
- DeliveryAttempt id;
- provider message id;
- token fingerprint;
- correlation id.

Per-operation drill-down belongs restricted logs/traces/business evidence, not cardinality-exploding metrics.

## COMM-WD-139 — Structured logs/traces are diagnostics, not Audit or delivery history

**Status:** `UPSTREAM_DERIVED`

Logs/traces may contain safe opaque references and normalized operational context.

They do not replace:

- MessageIntent;
- DeliveryAttempt;
- Audit Event;
- incident record.

Log retention, loss or sampling cannot rewrite business history.

## COMM-WD-140 — Dashboards are projections and cannot drive state without owner actions

**Status:** `UPSTREAM_DERIVED`

Queue depth, oldest age, provider latency, terminal counts and reconciliation counts may appear on dashboards.

If a dashboard disagrees with authoritative Communications state, authoritative state wins.

A dashboard action invokes an owner command that revalidates current authority; it does not mutate a chart/read model directly.

## COMM-WD-141 — Alerts require a meaningful owner action/decision

**Status:** `UPSTREAM_DERIVED`

Alerting should focus on actionable conditions such as:

- prolonged required-message backlog;
- oldest-job/intent age beyond expected bound;
- growing reconciliation-required population;
- terminal-failure spike;
- provider-wide outage/degradation;
- repeated invalid provider callback authentication;
- evidence of duplicate-send invariant breach;
- protected-data leakage/security incident.

Do not create one alert per participant/message merely because a failure exists.

## COMM-WD-142 — Terminal-failure work queues are projections, not Audit Resources or new business Resources

**Status:** `UPSTREAM_DERIVED`

A queue can project Communications-owned terminal/unresolved obligations for operator attention.

The queue item is not:

- a second MessageIntent;
- an Audit Event;
- a SupportCase;
- delivery authority.

Queue disappearance/rebuild does not lose Communications business truth.

## COMM-WD-143 — Public participant error/status never exposes raw provider semantics

**Status:** `UPSTREAM_DERIVED`

Participant-facing verification/recovery status may safely communicate:

- pending;
- delayed;
- failed to send;
- resend available;
- change-address/recovery route where permitted;
- contact support.

It does not expose:

- raw SMTP/provider codes;
- provider message ids;
- mailbox-existence hints;
- internal account existence;
- provider payload;
- security diagnostic detail.

Public recovery remains non-enumerating.

## COMM-WD-144 — Raw provider evidence access is exceptional and separately privileged

**Status:** `WORKING_DESIGN_ACCEPTED`

If selected-provider operations later justify raw evidence access, it is not shown by default.

Access requires:

- a scoped operational/security purpose;
- current privileged policy;
- minimum necessary reveal;
- restricted retention;
- access evidence where required.

Routine support should use normalized evidence.

## COMM-WD-145 — Invalid provider callbacks cannot create DeliveryAttempt/business state

**Status:** `UPSTREAM_DERIVED`

Provider ingress follows:

```text
authenticate/verify callback
→ only then durably receive Communications evidence
```

An invalid/unverifiable callback:

- does not mutate intent/attempt truth;
- does not mark delivery;
- does not create Identity effects;
- may create bounded security telemetry/evidence according to materiality.

Raw hostile payload is not logged wholesale.

## COMM-WD-146 — Security-event escalation is materiality-driven, not one Audit event per invalid request

**Status:** `WORKING_DESIGN_ACCEPTED`

A single rejected invalid callback may be ordinary security telemetry.

Repeated, patterned or material callback-authentication failure may cross into:

- security evidence;
- incident linkage;
- operational alerting.

Current security/incident policy owns that escalation.

Communications does not create an Audit/security flood by appending every hostile packet centrally.

## COMM-WD-147 — Delivery/open/click observations remain distinct and do not create business conversion

**Status:** `UPSTREAM_DERIVED`

Provider states such as:

- accepted;
- delivered;
- bounced;
- opened;
- clicked

are distinct observations.

They never prove:

- email verification;
- proof consumption;
- password reset completion;
- email-change apply;
- Account control;
- business conversion.

Analytics may consume only explicitly approved minimum observations.

## COMM-WD-148 — FP-001 protected security emails do not require open/click tracking

**Status:** `WORKING_DESIGN_ACCEPTED`

The FP-001 outcome needs reliable security/account delivery, not marketing engagement measurement.

Therefore security messages do not need:

- tracking pixels;
- open tracking;
- click analytics;
- URL click rewriting

to satisfy the Feature Pack.

Absent an explicit approved purpose, those features should be disabled/not persisted for protected FP-001 communication.

This reduces privacy exposure and protected-link risk.

## COMM-WD-149 — Protected action URLs must not be rewritten through provider click-tracking redirects

**Status:** `WORKING_DESIGN_ACCEPTED`

A verification/reset/recovery/email-change protected action URL is bearer-sensitive.

Provider URL rewriting/click-tracking may:

- copy the bearer into provider tracking systems;
- add redirect hops;
- expose query/path data;
- trigger scanner fetches;
- complicate exact provenance.

Therefore the provider-independent contract requires a non-tracking protected-link path.

Exact provider configuration is `OQ-036`.

This does not by itself solve `COMM-UPD-002` because independent mail-security scanners may still fetch the direct URL.

## COMM-WD-150 — Analytics receives minimum derived observations, not security-message payload/contact truth

**Status:** `UPSTREAM_DERIVED`

For FP-001, Analytics does not need:

- raw email/phone destination;
- rendered message body;
- bearer URL/token;
- provider raw payload;
- source proof secret;
- support notes.

Where an approved measurement exists, it consumes a bounded derived observation with the minimum safe identity/provenance required by Analytics policy.

Analytics failure never changes delivery or Identity truth.

## COMM-WD-151 — Observability sampling may reduce diagnostic detail but business evidence remains complete

**Status:** `UPSTREAM_DERIVED`

Risk-sensitive telemetry sampling is acceptable.

Critical business correctness does not depend on every log/span being retained.

Durable Communications and required Audit evidence provide the non-sampled business/governance history.

## COMM-WD-152 — Communications, Audit, telemetry and Analytics have independent retention/data-lifecycle policies

**Status:** `UPSTREAM_DERIVED`

Do not retain logs forever merely because Audit needs history.

Do not retain full provider evidence forever because an incident once occurred.

Each evidence class follows its own approved:

- purpose;
- access;
- retention;
- legal hold;
- deletion/anonymisation.

`OQ-029` owns exact duration where unresolved.

## COMM-WD-153 — Deletion/legal hold cannot turn retained evidence into active Communications authority

**Status:** `UPSTREAM_DERIVED`

After participant deletion:

- retained Audit evidence remains restricted evidence;
- retained Communications provider evidence remains historical only where lawful;
- telemetry/Analytics follow their own disposition;
- no retained identifier may authorise resend/recovery;
- no correlation link may reconstruct an active Account/contact relationship.

A legal hold preserves scoped evidence, not provider-send authority.

## COMM-WD-154 — Provider callback processing does not wait on central Audit

**Status:** `WORKING_DESIGN_ACCEPTED`

A valid provider callback should:

```text
verify authenticity
→ durably commit Communications evidence
→ acknowledge provider
→ reconcile asynchronously
```

If the callback itself later requires central security/incident evidence, that consequence is durably emitted/reconciled separately.

Central Audit availability must not force the provider to redeliver a callback whose Communications evidence is already safely committed.

## COMM-WD-155 — Causation is explicit: participant, system, provider and operator are different

**Status:** `WORKING_DESIGN_ACCEPTED`

Evidence records distinguish at least conceptual causation classes:

- participant/source request;
- automatic system executor;
- provider callback/evidence;
- named operator;
- break-glass operator where applicable.

Do not record an automated retry as if a human sent the message.

Do not record provider evidence as if NewYou asserted the provider outcome independently.

Exact actor enum/schema remains downstream.

## COMM-WD-156 — Privileged evidence review/export is itself governed access

**Status:** `UPSTREAM_DERIVED`

Audit and raw-provider-evidence access is highly restricted.

A bulk export of operational evidence cannot be treated as ordinary dashboard access.

If a governed export is needed it uses:

- scoped authorisation;
- bounded selection;
- minimum fields;
- appropriate access evidence;
- safe file handling/expiry;
- retention/deletion rules.

No unrestricted CSV dump of destinations/provider payloads is introduced.

## COMM-WD-157 — Audit & Evidence remains conditional / not pulled forward

**Status:** `WORKING_DESIGN_ACCEPTED`

The current Skeleton says Audit becomes required only if exact FP-001 evidence event, minimisation, access or retention contracts cannot be stated without invention.

This pass can state the necessary cross-Domain contract from existing authority:

- automated delivery evidence stays Communications-owned;
- minimum privileged/security action evidence is appended centrally;
- central Audit never owns delivery/Identity truth;
- actor/cause/action/reason/result/target linkage is bounded;
- bearer/body/provider secrets are excluded;
- evidence access is restricted;
- retention remains category-specific under existing OQ-029 governance.

No new Audit lifecycle, Resource or policy has been invented.

Therefore the Audit conditional dossier remains unpulled.

---

# 83. Operator/evidence lifecycle refinement — v0.7.0

## 83.1 Automated execution

```text
authoritative MessageIntent
→ automated executor
→ DeliveryAttempt
→ provider evidence
→ normalized Communications state
```

Central Audit is not required for every step.

Operational telemetry may observe the path but is non-authoritative.

## 83.2 Privileged operator command

Conceptually:

```text
operator request
→ authenticate current actor
→ current scoped grant / assurance / separation-of-duties checks
→ current MessageIntent / DeliveryAttempt / source / privacy / content checks
→ validate reason where required
→ durably establish required Audit evidence/intention
→ commit owner command admission
→ execute or schedule bounded Communications action
→ append result/reconciliation evidence
```

No provider call occurs merely because an operator UI loaded an old state.

## 83.3 Reconciliation

```text
existing ambiguous DeliveryAttempt
→ obtain provider evidence through adapter / approved operator evidence path
→ normalize
→ append reconciliation evidence
→ update current effective Communications resolution
```

Historical evidence is not overwritten.

## 83.4 Audit versus telemetry failure

```text
telemetry unavailable
→ business action may continue if otherwise valid
→ visibility degrades

required privileged Audit establishment unavailable
→ privileged action fails closed
```

Exact mechanism remains JIT/implementation.

---

# 84. Pressure-test register — seventh cluster

## COMM-PT-186 — Automated provider acceptance is recorded

- **Scenario:** ordinary executor receives definitive provider acceptance.
- **Authority involved:** Communications DeliveryAttempt; provider external evidence.
- **Durable truths and owner:** normalized acceptance belongs to Communications.
- **Concurrency/retry/reordering/crash behaviour:** worker may crash after provider response or after durable commit.
- **Rejected models:** append a central Audit Event as the only durable acceptance history; rely on logs.
- **Required invariant:** Communications retains durable attempt evidence independent of Audit/telemetry.
- **Recommended JIT shape:** DeliveryAttempt update/append; ordinary telemetry optional.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider success + telemetry/Audit outage.
- **Verdict:** PASS.

## COMM-PT-187 — Automated retry occurs after definitive retryable failure

- **Scenario:** system schedules another provider attempt.
- **Authority involved:** Communications retry policy.
- **Durable truths and owner:** MessageIntent/DeliveryAttempt history.
- **Concurrency/retry/reordering/crash behaviour:** retry worker duplicates/restarts.
- **Rejected models:** one Audit Event per automatic retry as delivery truth.
- **Required invariant:** business retry provenance remains complete in Communications even if telemetry is sampled.
- **Recommended JIT shape:** ordinary delivery history + bounded operational signal.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** sampled/no logs still leaves full business history.
- **Verdict:** PASS.

## COMM-PT-188 — Valid provider callback arrives

- **Scenario:** authenticated webhook reports a delivery/bounce state.
- **Authority involved:** Architecture provider-ingress contract; Communications evidence.
- **Durable truths and owner:** callback evidence belongs to Communications.
- **Concurrency/retry/reordering/crash behaviour:** duplicate/redelivery if acknowledgment fails.
- **Rejected models:** wait for central Audit write before committing/acknowledging provider callback.
- **Required invariant:** Communications evidence commits durably before provider acknowledgement; optional Audit linkage is separate.
- **Recommended JIT shape:** verify → commit Communications evidence → ack → reconcile.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** Audit unavailable during callback.
- **Verdict:** PASS.

## COMM-PT-189 — Duplicate/reordered provider callback

- **Scenario:** delivery evidence repeats or arrives after a later observation.
- **Authority involved:** Communications provider evidence.
- **Durable truths and owner:** normalized evidence/current resolution.
- **Concurrency/retry/reordering/crash behaviour:** normal duplicate/reorder.
- **Rejected models:** duplicate central Audit events become effective state; last callback/log line wins.
- **Required invariant:** Communications reconciliation is idempotent/order-safe; Audit not used as ordering authority.
- **Recommended JIT shape:** provider event identity/evidence append plus current effective resolution.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate/reordered callbacks.
- **Verdict:** PASS.

## COMM-PT-190 — Operator manually retries a terminal eligible intent

- **Scenario:** bounded automated retry ended; current source remains valid and manual recovery is permitted.
- **Authority involved:** Communications owner action; Identity/scoped operator policy; Audit.
- **Durable truths and owner:** intent/attempt = Communications; privileged-action evidence = Audit.
- **Concurrency/retry/reordering/crash behaviour:** action may duplicate or race source expiry.
- **Rejected models:** click directly in provider portal; no reason/audit because send already existed.
- **Required invariant:** current authority revalidated; required Audit evidence established; one new DeliveryAttempt at most.
- **Recommended JIT shape:** idempotent operator command with actor/reason/revision.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate click + source race.
- **Verdict:** PASS.

## COMM-PT-191 — Operator reconciles an unknown attempt

- **Scenario:** provider result was ambiguous.
- **Authority involved:** Communications reconciliation.
- **Durable truths and owner:** existing DeliveryAttempt remains the provider-operation identity.
- **Concurrency/retry/reordering/crash behaviour:** provider callback may arrive simultaneously.
- **Rejected models:** “reconcile” sends another message; operator manually selects delivered.
- **Required invariant:** reconciliation can only add/normalize evidence about the existing operation; no new provider send.
- **Recommended JIT shape:** distinct reconcile action; stale reconciliation loses to newer committed evidence.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** callback/operator race.
- **Verdict:** PASS.

## COMM-PT-192 — Operator pauses/resumes/suppresses provider execution

- **Scenario:** authorised operations response changes execution admission.
- **Authority involved:** Communications operational control + Identity grant/Audit.
- **Durable truths and owner:** pause state is execution admission, not source truth.
- **Concurrency/retry/reordering/crash behaviour:** workers already running; resume duplicates.
- **Rejected models:** pause marks intents failed/cancelled; no Audit because “operations only”.
- **Required invariant:** business state preserved; privileged control is attributable/audited; current source checks still run after resume.
- **Recommended JIT shape:** bounded operational command, no new business Resource.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** pause during execution/restart.
- **Verdict:** PASS.

## COMM-PT-193 — Operator double-clicks retry

- **Scenario:** UI submits same privileged command twice.
- **Authority involved:** Communications idempotency + Audit.
- **Durable truths and owner:** one logical privileged command/result.
- **Concurrency/retry/reordering/crash behaviour:** requests overlap.
- **Rejected models:** two DeliveryAttempts because operator clicked twice; two conflicting audit histories.
- **Required invariant:** duplicate command converges; Audit may record one accepted action plus duplicate/refused evidence according to policy, not two provider sends.
- **Recommended JIT shape:** operator operation id.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** concurrent same command.
- **Verdict:** PASS.

## COMM-PT-194 — Stale operator page offers retry after state changed

- **Scenario:** page shows terminal failure; meanwhile source proof expired/deletion completed/provider callback resolved it.
- **Authority involved:** current owner state.
- **Durable truths and owner:** UI is projection only.
- **Concurrency/retry/reordering/crash behaviour:** common stale-view race.
- **Rejected models:** button presence carries authority.
- **Required invariant:** command revalidates server-side and safely refuses stale action.
- **Recommended JIT shape:** revision/current-state guard.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale UI across all terminal transitions.
- **Verdict:** PASS.

## COMM-PT-195 — Operator retry races proof expiry/revocation

- **Scenario:** privileged command is admitted while Identity invalidates proof.
- **Authority involved:** v0.2 dispatch cutover + operator action.
- **Durable truths and owner:** Identity source validity; Communications attempt.
- **Concurrency/retry/reordering/crash behaviour:** cross-node race.
- **Rejected models:** operator privilege bypasses source validity.
- **Required invariant:** same dispatch-authorisation ordering applies to manual and automatic sends.
- **Recommended JIT shape:** no privileged bypass.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** both race orderings.
- **Verdict:** PASS.

## COMM-PT-196 — Operator reconciliation races late provider callback

- **Scenario:** manual lookup and webhook resolve same unknown attempt differently/near-simultaneously.
- **Authority involved:** Communications provider evidence.
- **Durable truths and owner:** evidence provenance matters.
- **Concurrency/retry/reordering/crash behaviour:** concurrent updates.
- **Rejected models:** whichever UI request commits last rewrites history.
- **Required invariant:** append/reconcile evidence deterministically; stale operator conclusion cannot overwrite stronger/newer provider evidence.
- **Recommended JIT shape:** evidence provenance + revision.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** interleavings.
- **Verdict:** PASS.

## COMM-PT-197 — Central Audit is unavailable when operator requests manual retry

- **Scenario:** privileged action requires Audit.
- **Authority involved:** Audit mandatory privileged-action evidence.
- **Durable truths and owner:** action cannot become unaudited side effect.
- **Concurrency/retry/reordering/crash behaviour:** Audit outage may recover later.
- **Rejected models:** “send now and log later best effort”; provider call then failed Audit.
- **Required invariant:** privileged provider-mutating action fails closed unless required Audit evidence/intention is durably established.
- **Recommended JIT shape:** durable audit-before-effect admission.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** Audit outage/recovery.
- **Verdict:** PASS.

## COMM-PT-198 — Telemetry exporter is unavailable during valid automated send

- **Scenario:** metrics/traces cannot be exported.
- **Authority involved:** Engineering Standards observability failure isolation.
- **Durable truths and owner:** Communications business action remains valid.
- **Concurrency/retry/reordering/crash behaviour:** exporter recovers later.
- **Rejected models:** fail provider send because APM is down; mark attempt failed.
- **Required invariant:** business evidence remains correct; visibility may degrade.
- **Recommended JIT shape:** bounded local instrumentation failure isolation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** exporter fault injection.
- **Verdict:** PASS.

## COMM-PT-199 — Metrics label contains raw email destination

- **Scenario:** engineer proposes `delivery_failure{email="..."}`.
- **Authority involved:** privacy/minimisation + Engineering Standards bounded-cardinality rules.
- **Durable truths and owner:** email belongs protected business data, not metric dimension.
- **Concurrency/retry/reordering/crash behaviour:** high-cardinality leak at scale.
- **Rejected models:** hash email and use as metric label as a loophole.
- **Required invariant:** participant identifiers never metric labels.
- **Recommended JIT shape:** bounded outcome/category/provider dimensions only.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** telemetry field/label audit.
- **Verdict:** PASS.

## COMM-PT-200 — Metrics label uses MessageIntent/DeliveryAttempt/correlation id

- **Scenario:** per-message metric labels enable convenient drill-down.
- **Authority involved:** cardinality/privacy/observability rules.
- **Durable truths and owner:** identifiers are not bounded metric dimensions.
- **Concurrency/retry/reordering/crash behaviour:** cardinality explosion.
- **Rejected models:** every durable id becomes a metric label.
- **Required invariant:** per-operation correlation belongs logs/traces/restricted evidence, not metrics labels.
- **Recommended JIT shape:** aggregate metrics + safe diagnostic correlation elsewhere.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** metric schema/cardinality checks.
- **Verdict:** PASS.

## COMM-PT-201 — Structured log includes full destination

- **Scenario:** worker logs `sending to user@example...`.
- **Authority involved:** privacy minimisation.
- **Durable truths and owner:** destination already exists in restricted business storage.
- **Concurrency/retry/reordering/crash behaviour:** logs replicate to external backend.
- **Rejected models:** duplicate raw contact info in logs for convenience.
- **Required invariant:** logs use safe opaque refs/masked data only where necessary.
- **Recommended JIT shape:** structured normalized context, no full destination.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** log capture tests.
- **Verdict:** PASS.

## COMM-PT-202 — Log/trace contains bearer URL/token

- **Scenario:** rendered body/URL or exception query string is logged.
- **Authority involved:** certified protected-delivery seam.
- **Durable truths and owner:** bearer must remain purpose-scoped protected material.
- **Concurrency/retry/reordering/crash behaviour:** log replication makes exposure durable.
- **Rejected models:** redact later at exporter; “debug only”.
- **Required invariant:** bearer never enters ordinary logs/traces.
- **Recommended JIT shape:** structured redaction at source + tests.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** secret scanning.
- **Verdict:** PASS.

## COMM-PT-203 — Provider exception echoes request body/headers

- **Scenario:** SDK exception includes destination, body, Authorization header or bearer URL.
- **Authority involved:** adapter boundary + minimisation.
- **Durable truths and owner:** raw provider exception is not safe application error.
- **Concurrency/retry/reordering/crash behaviour:** exception can hit logs/APM.
- **Rejected models:** log `inspect(exception)` indiscriminately.
- **Required invariant:** adapter converts to sanitized bounded error semantics before external observability.
- **Recommended JIT shape:** error normalization/redaction boundary.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** hostile exception fixtures.
- **Verdict:** PASS.

## COMM-PT-204 — Provider credential leaks into log/trace

- **Scenario:** request instrumentation captures auth headers or webhook secret.
- **Authority involved:** integration-secret policy.
- **Durable truths and owner:** credentials are configuration secrets.
- **Concurrency/retry/reordering/crash behaviour:** broad compromise.
- **Rejected models:** rely solely on vendor-side secret masking.
- **Required invariant:** secret headers/keys are never captured by ordinary instrumentation.
- **Recommended JIT shape:** allow-list telemetry fields, credential redaction, incident path.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** credential canary tests.
- **Verdict:** PASS.

## COMM-PT-205 — Routine support views a terminal verification delivery failure

- **Scenario:** support needs to help participant.
- **Authority involved:** FES minimum-necessary support workspace; Communications projection.
- **Durable truths and owner:** support needs state, not full provider internals.
- **Concurrency/retry/reordering/crash behaviour:** view may stale.
- **Rejected models:** expose raw webhook/provider JSON by default.
- **Required invariant:** show role/status/masked destination/safe recovery action only.
- **Recommended JIT shape:** scoped projection.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** role-based projection tests.
- **Verdict:** PASS.

## COMM-PT-206 — Operator needs full destination for an authorised recovery task

- **Scenario:** masked value is insufficient for a specific permitted task.
- **Authority involved:** Identity grant + minimum disclosure + Audit.
- **Durable truths and owner:** canonical destination remains source-owned; reveal is access, not mutation.
- **Concurrency/retry/reordering/crash behaviour:** grant may expire/revoke during view.
- **Rejected models:** full contact details always visible to all support.
- **Required invariant:** scoped reveal rechecks current authority; no bearer/body reveal.
- **Recommended JIT shape:** explicit privileged reveal action where justified.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** grant revoke/reveal race.
- **Verdict:** PASS.

## COMM-PT-207 — Support asks to see full rendered security email

- **Scenario:** support wants to verify wording/link.
- **Authority involved:** C&M provenance + protected-delivery secrecy.
- **Durable truths and owner:** full bearer-bearing body is not ordinary support evidence.
- **Concurrency/retry/reordering/crash behaviour:** copy/paste/screenshots can leak.
- **Rejected models:** expose exact historical plaintext body.
- **Required invariant:** support uses template/version/locale provenance and safe preview with synthetic placeholders.
- **Recommended JIT shape:** no production bearer/body reveal.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** preview path cannot recover secret.
- **Verdict:** PASS.

## COMM-PT-208 — Raw webhook payload retained indefinitely

- **Scenario:** provider sends JSON with destination/provider metadata and event details.
- **Authority involved:** Communications evidence minimisation + OQ-029.
- **Durable truths and owner:** normalized evidence normally sufficient.
- **Concurrency/retry/reordering/crash behaviour:** high-volume retention.
- **Rejected models:** keep every raw webhook “just in case”.
- **Required invariant:** raw persistence requires explicit need/retention; otherwise normalize and discard.
- **Recommended JIT shape:** selected-provider evidence contract.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** retention/data-field audit.
- **Verdict:** PASS.

## COMM-PT-209 — Raw provider response body contains participant/message data

- **Scenario:** synchronous send response echoes destination/body metadata.
- **Authority involved:** same minimisation boundary.
- **Durable truths and owner:** provider operation id/outcome may be required; rest may not.
- **Concurrency/retry/reordering/crash behaviour:** repeated attempts multiply copies.
- **Rejected models:** store entire SDK response on DeliveryAttempt.
- **Required invariant:** persist only approved normalized/minimum fields.
- **Recommended JIT shape:** adapter DTO/error taxonomy.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider fixture minimisation.
- **Verdict:** PASS.

## COMM-PT-210 — Provider dashboard says delivered but platform has unknown outcome

- **Scenario:** operator inspects provider portal.
- **Authority involved:** provider external evidence + Communications reconciliation.
- **Durable truths and owner:** platform needs durable ingested evidence before resolution.
- **Concurrency/retry/reordering/crash behaviour:** callback may arrive later.
- **Rejected models:** operator toggles database field manually.
- **Required invariant:** reconcile through owner action with provider evidence/provenance.
- **Recommended JIT shape:** provider lookup adapter/reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** portal/API reconciliation.
- **Verdict:** PASS.

## COMM-PT-211 — Operator tries “mark delivered”

- **Scenario:** no provider evidence is available but operator believes participant received message.
- **Authority involved:** Communications delivery evidence.
- **Durable truths and owner:** belief is not provider evidence.
- **Concurrency/retry/reordering/crash behaviour:** could discharge obligation incorrectly.
- **Rejected models:** arbitrary manual state override.
- **Required invariant:** operator cannot fabricate provider-delivery fact; may record a note/escalation without changing evidence semantics.
- **Recommended JIT shape:** no generic `mark_delivered` owner action.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** authorisation model excludes it.
- **Verdict:** PASS.

## COMM-PT-212 — Operator sends message directly from provider portal

- **Scenario:** support clicks provider resend outside NewYou.
- **Authority involved:** Communications owner boundary, Identity source validity, Audit.
- **Durable truths and owner:** NewYou would have no authoritative MessageIntent/DeliveryAttempt admission.
- **Concurrency/retry/reordering/crash behaviour:** duplicate send likely.
- **Rejected models:** provider dashboard is acceptable manual fallback.
- **Required invariant:** routine provider-side manual send is prohibited.
- **Recommended JIT shape:** all normal sends through platform owner action.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** operational runbook/provider permissions.
- **Verdict:** PASS.

## COMM-PT-213 — Callback signature/authentication fails

- **Scenario:** unauthenticated/forged webhook.
- **Authority involved:** provider ingress security.
- **Durable truths and owner:** no valid external evidence exists.
- **Concurrency/retry/reordering/crash behaviour:** attacker retries.
- **Rejected models:** create DeliveryAttempt/event then mark invalid.
- **Required invariant:** zero business mutation before authenticity passes.
- **Recommended JIT shape:** reject + bounded security telemetry.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** invalid signatures/replay.
- **Verdict:** PASS.

## COMM-PT-214 — Invalid callback flood

- **Scenario:** attacker/provider misconfiguration generates high-volume invalid webhooks.
- **Authority involved:** security/operations.
- **Durable truths and owner:** hostile packets are not business facts.
- **Concurrency/retry/reordering/crash behaviour:** log/Audit flood risk.
- **Rejected models:** append one central Audit Event per rejected request.
- **Required invariant:** bounded telemetry/rate controls; escalate material pattern/incident, not every packet.
- **Recommended JIT shape:** aggregation/alert threshold under existing security policy.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** flood load/cardinality.
- **Verdict:** PASS.

## COMM-PT-215 — Callback secret rotates and legitimate callback temporarily fails verification

- **Scenario:** configuration transition overlaps provider retries.
- **Authority involved:** integration configuration + provider evidence.
- **Durable truths and owner:** failed verification is not delivery state.
- **Concurrency/retry/reordering/crash behaviour:** callback may be redelivered after fix.
- **Rejected models:** accept unsigned callback because provider is known; mutate delivery to failed.
- **Required invariant:** fail closed on evidence authenticity; provider business attempt remains unresolved until valid evidence/reconciliation.
- **Recommended JIT shape:** operational alert + safe secret-rotation procedure.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** key rotation overlap.
- **Verdict:** PASS.

## COMM-PT-216 — Provider event/message id is duplicated or unexpectedly reused

- **Scenario:** external provider identifier assumptions fail.
- **Authority involved:** internal attempt identity + provider evidence.
- **Durable truths and owner:** provider id is scoped evidence only.
- **Concurrency/retry/reordering/crash behaviour:** callbacks could collide.
- **Rejected models:** global unique provider id is MessageIntent key.
- **Required invariant:** internal attempt/provenance prevents cross-message state corruption.
- **Recommended JIT shape:** provider/account/channel-scoped external key plus internal ids.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate provider id fixture.
- **Verdict:** PASS.

## COMM-PT-217 — Correlation id is accidentally reused

- **Scenario:** instrumentation bug emits same correlation id for two workflows.
- **Authority involved:** observability correlation only.
- **Durable truths and owner:** business ids remain distinct.
- **Concurrency/retry/reordering/crash behaviour:** traces intermix.
- **Rejected models:** correlation id doubles as dedupe/idempotency key.
- **Required invariant:** correlation collision can degrade diagnostics only; cannot merge MessageIntents/attempts.
- **Recommended JIT shape:** separate business identities.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** forced collision.
- **Verdict:** PASS.

## COMM-PT-218 — Correlation id encodes email/Account/PMR

- **Scenario:** developer uses `account_id-email-purpose` as trace id.
- **Authority involved:** privacy/cardinality.
- **Durable truths and owner:** correlation should be opaque.
- **Concurrency/retry/reordering/crash behaviour:** propagates across providers/logs.
- **Rejected models:** meaningful correlation strings.
- **Required invariant:** no participant/business semantics embedded.
- **Recommended JIT shape:** random opaque correlation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** format/field scan.
- **Verdict:** PASS.

## COMM-PT-219 — Correlation id is sent in provider metadata

- **Scenario:** adapter wants end-to-end reconciliation.
- **Authority involved:** provider metadata minimisation.
- **Durable truths and owner:** safe opaque value may be useful but not necessary authority.
- **Concurrency/retry/reordering/crash behaviour:** provider retains it under external policy.
- **Rejected models:** send Account id/email/PMR instead.
- **Required invariant:** any provider-exposed correlation is opaque, non-secret, minimum and not the only reconciliation key.
- **Recommended JIT shape:** provider-specific decision under OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider metadata mapping.
- **Verdict:** PASS.

## COMM-PT-220 — Provider sends “opened” before “delivered”

- **Scenario:** provider event semantics/order are surprising.
- **Authority involved:** provider evidence.
- **Durable truths and owner:** observations remain independent.
- **Concurrency/retry/reordering/crash behaviour:** events reorder.
- **Rejected models:** linear `accepted→delivered→opened` enum required.
- **Required invariant:** engagement evidence does not advance delivery/source truth incorrectly.
- **Recommended JIT shape:** independent evidence dimensions.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** reordered engagement events.
- **Verdict:** PASS.

## COMM-PT-221 — Click event arrives after proof expired/consumed

- **Scenario:** recipient/security software follows old link.
- **Authority involved:** Identity proof state + provider click evidence.
- **Durable truths and owner:** click observation cannot revive proof.
- **Concurrency/retry/reordering/crash behaviour:** long-delayed events.
- **Rejected models:** clicked means verified/reset/recovered.
- **Required invariant:** provider engagement never creates Identity state.
- **Recommended JIT shape:** ignore for source truth; optional approved Analytics only.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** click after consumption/expiry.
- **Verdict:** PASS.

## COMM-PT-222 — Security email open/click tracking is enabled “because provider supports it”

- **Scenario:** provider adds tracking pixel and link analytics by default.
- **Authority involved:** privacy/minimisation; FP-001 outcome.
- **Durable truths and owner:** engagement is not required for security outcome.
- **Concurrency/retry/reordering/crash behaviour:** extra callbacks/data.
- **Rejected models:** provider defaults define platform tracking scope.
- **Required invariant:** no unnecessary security-email engagement tracking.
- **Recommended JIT shape:** disable/not persist absent explicit approved purpose.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider configuration test.
- **Verdict:** PASS.

## COMM-PT-223 — Provider rewrites protected URL through tracking redirect

- **Scenario:** bearer link becomes provider-hosted tracking URL.
- **Authority involved:** protected-delivery seam + OQ-036.
- **Durable truths and owner:** provider already transports content but must not become extra bearer-routing authority.
- **Concurrency/retry/reordering/crash behaviour:** scanner/redirect/prefetch.
- **Rejected models:** accept click rewriting for convenience.
- **Required invariant:** protected action URL is not rewritten through provider tracking.
- **Recommended JIT shape:** provider config/adapter capability check.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** inspect actual provider payload/link.
- **Verdict:** PASS / OQ-036 DETAIL.

## COMM-PT-224 — Corporate mail scanner prefetches direct verification/reset URL

- **Scenario:** no provider tracking is enabled, but recipient's security gateway fetches URL.
- **Authority involved:** Identity proof-consumption boundary.
- **Durable truths and owner:** URL possession/fetch is not provider delivery truth.
- **Concurrency/retry/reordering/crash behaviour:** scanner fetch can precede participant by seconds/minutes.
- **Rejected models:** solve solely by disabling provider click tracking.
- **Required invariant:** automated fetch cannot complete protected Identity transition.
- **Recommended JIT shape:** route to Identity scanner-safe proof-use contract.
- **Conclusion:** `OPEN_HYPOTHESIS` resolved into `COMM-UPD-002` upstream requirement.
- **Upstream amendment:** **YES — Identity JIT clarification/successor required unless governed process explicitly routes to proof.**
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** scanner `HEAD/GET` and redirect fetch.
- **Verdict:** BLOCKED UPSTREAM FOR FINAL FREEZE.

## COMM-PT-225 — Automated scanner actually presents a valid bearer before participant

- **Scenario:** scanner fetch reaches the current consumption endpoint with the genuine token.
- **Authority involved:** Identity sole proof-consumption authority.
- **Durable truths and owner:** verification/reset/email change must remain participant/security-bound.
- **Concurrency/retry/reordering/crash behaviour:** participant later gets replay result.
- **Rejected models:** treat scanner consumption as successful participant verification because token was valid.
- **Required invariant:** the chosen Identity interaction boundary prevents non-human fetch alone from completing the protected transition.
- **Recommended JIT shape:** Identity contract/proof test, not Communications inference.
- **Conclusion:** `OPEN_HYPOTHESIS / UPSTREAM GAP`.
- **Upstream amendment:** **YES — COMM-UPD-002.**
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** scanner-first/user-second interleaving.
- **Verdict:** BLOCKED UPSTREAM FOR FINAL FREEZE.

## COMM-PT-226 — Analytics asks for per-Account verification-email opens/clicks

- **Scenario:** product analyst wants funnel detail.
- **Authority involved:** Analytics derived measurement; Privacy; Communications evidence.
- **Durable truths and owner:** current FP-001 Analytics dossier is `NO`.
- **Concurrency/retry/reordering/crash behaviour:** tracking can be incomplete/bot-driven.
- **Rejected models:** engagement tracking becomes verification funnel authority.
- **Required invariant:** no new security-message tracking/personal-data purpose is introduced silently.
- **Recommended JIT shape:** not required for FP-001; separate governed measurement/privacy decision if later needed.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** Analytics absence does not affect product flow.
- **Verdict:** PASS.

## COMM-PT-227 — Analytics requests raw destination/message content/provider payload

- **Scenario:** convenient enrichment proposal.
- **Authority involved:** minimum data boundary.
- **Durable truths and owner:** not required for derived measurement.
- **Concurrency/retry/reordering/crash behaviour:** creates duplicate sensitive store.
- **Rejected models:** copy operational provider record into Analytics.
- **Required invariant:** Analytics consumes minimum derived observations only.
- **Recommended JIT shape:** bounded event contract.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** Analytics event schema review.
- **Verdict:** PASS.

## COMM-PT-228 — Analytics pipeline is unavailable

- **Scenario:** delivery succeeds while Analytics consumer fails.
- **Authority involved:** Analytics non-authority.
- **Durable truths and owner:** delivery remains Communications truth.
- **Concurrency/retry/reordering/crash behaviour:** Analytics may backfill later.
- **Rejected models:** retry security email to recover missing analytics.
- **Required invariant:** no business effect.
- **Recommended JIT shape:** failure-isolated derived pipeline.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** consumer outage.
- **Verdict:** PASS.

## COMM-PT-229 — Dashboard says backlog is clear while DB has unresolved intents

- **Scenario:** cached aggregate stale.
- **Authority involved:** Communications authority versus operational projection.
- **Durable truths and owner:** DB/current owner state wins.
- **Concurrency/retry/reordering/crash behaviour:** cache lag.
- **Rejected models:** operator closes incident because chart says zero without authoritative check.
- **Required invariant:** dashboard is diagnostic only; material operator action rechecks owner state.
- **Recommended JIT shape:** freshness markers/drill-down to authoritative query where needed.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale aggregate.
- **Verdict:** PASS.

## COMM-PT-230 — Provider outage causes alert storm

- **Scenario:** thousands of intents individually fail/defer.
- **Authority involved:** operational observability.
- **Durable truths and owner:** one shared dependency condition drives many business records.
- **Concurrency/retry/reordering/crash behaviour:** high fan-out.
- **Rejected models:** one alert/page per intent.
- **Required invariant:** alerts aggregate dependency/material condition while business records remain individually correct.
- **Recommended JIT shape:** provider/outage alert aggregation with actionable owner.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** simulated outage alert volume.
- **Verdict:** PASS.

## COMM-PT-231 — Terminal-failure work queue contains duplicates/stale entries

- **Scenario:** projection rebuild or event duplication shows repeated item.
- **Authority involved:** Communications business truth.
- **Durable truths and owner:** queue is non-authoritative.
- **Concurrency/retry/reordering/crash behaviour:** duplicate projection rows.
- **Rejected models:** queue item identity becomes retry idempotency.
- **Required invariant:** owner command targets MessageIntent/current revision; duplicates cannot multiply action.
- **Recommended JIT shape:** rebuildable queue projection.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate/stale projection.
- **Verdict:** PASS.

## COMM-PT-232 — Operator exports failure queue to CSV

- **Scenario:** troubleshooting request wants bulk email/provider fields.
- **Authority involved:** data minimisation + privileged export.
- **Durable truths and owner:** operational export creates another sensitive representation.
- **Concurrency/retry/reordering/crash behaviour:** file persists/downloads.
- **Rejected models:** unrestricted raw CSV.
- **Required invariant:** export only if governed need; bounded fields/access/expiry/evidence.
- **Recommended JIT shape:** no default raw export in FP-001.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** access/export controls if introduced.
- **Verdict:** PASS.

## COMM-PT-233 — Support note contains full destination/token/provider body

- **Scenario:** operator pastes debugging data into free text.
- **Authority involved:** minimisation/support evidence.
- **Durable truths and owner:** support note must not become secret dumping ground.
- **Concurrency/retry/reordering/crash behaviour:** note retention may exceed provider evidence.
- **Rejected models:** “staff-only” means safe for bearer secrets.
- **Required invariant:** protected bearer forbidden; sensitive provider/raw destination minimised; UI discourages unsafe copy.
- **Recommended JIT shape:** structured reason codes/context where possible; secret detection/redaction controls later if justified.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** note input secret leakage tests if free text exists.
- **Verdict:** PASS.

## COMM-PT-234 — Required Audit event is duplicated/reordered

- **Scenario:** cross-Domain audit consequence retries.
- **Authority involved:** Audit append-only evidence.
- **Durable truths and owner:** duplicate audit delivery must not create conflicting business effects.
- **Concurrency/retry/reordering/crash behaviour:** event retry/reorder.
- **Rejected models:** Audit event order is Communications state order.
- **Required invariant:** audit append is duplicate-safe/causally linked; business truth remains Communications.
- **Recommended JIT shape:** stable action/operation reference in bounded audit contract.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** duplicate/reordered audit consequence.
- **Verdict:** PASS.

## COMM-PT-235 — Break-glass operator wants to retry protected security email

- **Scenario:** ordinary grant insufficient; emergency access is invoked.
- **Authority involved:** Identity break-glass + Communications action + Audit.
- **Durable truths and owner:** break-glass grants scoped identity-side authority only.
- **Concurrency/retry/reordering/crash behaviour:** grant can expire/revoke during action.
- **Rejected models:** break-glass bypasses source validity/protected capability/content/deletion.
- **Required invariant:** break-glass is named, narrow, MFA-protected, reasoned, time-bounded, alerted/reviewed and still subject to owning-Domain invariants.
- **Recommended JIT shape:** same owner action with stronger policy/evidence; no provider dashboard bypass.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** grant expiry/action race.
- **Verdict:** PASS.

## COMM-PT-236 — Material duplicate-send incident occurs

- **Scenario:** defect causes widespread duplicate verification/security mail.
- **Authority involved:** Communications evidence + security/incident governance.
- **Durable truths and owner:** individual attempts remain Communications evidence; incident linkage belongs Audit/Operations.
- **Concurrency/retry/reordering/crash behaviour:** broad incident.
- **Rejected models:** convert incident record into delivery authority; duplicate every attempt payload into Audit.
- **Required invariant:** central incident evidence links to bounded affected operations; underlying business state stays with owners.
- **Recommended JIT shape:** incident correlation/reference only; OQ-038 owns later named incident command.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** later incident process.
- **Verdict:** PASS / OQ-038 LATER.

## COMM-PT-237 — Provider API key compromise is suspected

- **Scenario:** integration credential may be exposed.
- **Authority involved:** security/secret rotation; provider adapter.
- **Durable truths and owner:** rotating credential does not mutate delivery history.
- **Concurrency/retry/reordering/crash behaviour:** old/new key overlap, callbacks continue.
- **Rejected models:** erase attempts/provider ids; log old key for diagnosis.
- **Required invariant:** secret rotation and incident evidence stay separate from business truth; pending work revalidates integration availability.
- **Recommended JIT shape:** protected secret management + incident linkage.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** credential rotation during backlog/callback flow.
- **Verdict:** PASS.

## COMM-PT-238 — Observability restore/replay contains old logs for deleted participant

- **Scenario:** log backend/backup restores historical diagnostic records.
- **Authority involved:** Privacy/data lifecycle + telemetry non-authority.
- **Durable truths and owner:** old log presence cannot restore Account/contact/send authority.
- **Concurrency/retry/reordering/crash behaviour:** restore after deletion.
- **Rejected models:** use log email/provider id to reconstruct deleted relationship.
- **Required invariant:** telemetry restoration is subject to its retention/deletion contract and never becomes business authority.
- **Recommended JIT shape:** independent telemetry data lifecycle.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** OQ-029/restore regime later.
- **Verdict:** PASS.

## COMM-PT-239 — Communications records deleted but lawful Audit evidence remains

- **Scenario:** category-specific retention differs.
- **Authority involved:** Privacy retention + Audit evidence.
- **Durable truths and owner:** retained Audit is minimum/non-reconstructive evidence, not resend state.
- **Concurrency/retry/reordering/crash behaviour:** later same-email registration possible.
- **Rejected models:** use audit target link to recreate MessageIntent/contact.
- **Required invariant:** no active relationship reconstruction.
- **Recommended JIT shape:** restricted minimal retained linkage.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** retention/delete integration.
- **Verdict:** PASS.

## COMM-PT-240 — Legal hold preserves privileged-action Audit evidence after Communications deletion

- **Scenario:** narrow security investigation holds operator evidence.
- **Authority involved:** Audit/Privacy legal hold.
- **Durable truths and owner:** hold preserves evidence only.
- **Concurrency/retry/reordering/crash behaviour:** hold later releases.
- **Rejected models:** preserve bearer/full destination because related Audit exists.
- **Required invariant:** scoped evidence survives without Communications send/recovery authority.
- **Recommended JIT shape:** existing legal-hold contract.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** hold/release.
- **Verdict:** PASS.

## COMM-PT-241 — Unauthorised staff member attempts raw provider-evidence access

- **Scenario:** staff can see general support but lacks operations/security scope.
- **Authority involved:** current Identity grant + Communications/Audit access policy.
- **Durable truths and owner:** navigation visibility grants nothing.
- **Concurrency/retry/reordering/crash behaviour:** role revoke during access.
- **Rejected models:** “staff” generic role; hidden URL security.
- **Required invariant:** access denied from current server policy; no data leakage.
- **Recommended JIT shape:** scoped read action.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** role matrix/revocation.
- **Verdict:** PASS.

## COMM-PT-242 — Central Audit is unavailable during ordinary automated provider callback

- **Scenario:** webhook evidence is valid; Audit backend/path fails.
- **Authority involved:** Communications provider ingress versus central Audit.
- **Durable truths and owner:** callback evidence is Communications truth.
- **Concurrency/retry/reordering/crash behaviour:** provider expects timely acknowledgement.
- **Rejected models:** reject/500 callback solely because central Audit is unavailable.
- **Required invariant:** Communications commits/acks valid evidence; any required Audit consequence remains separately durable/reconcilable.
- **Recommended JIT shape:** no synchronous Audit dependency for ordinary callbacks.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** Audit outage.
- **Verdict:** PASS.

## COMM-PT-243 — Audit viewer/exporter fails

- **Scenario:** restricted Audit review UI/export is unavailable.
- **Authority involved:** Audit read availability.
- **Durable truths and owner:** existing Audit evidence remains; Communications truth unaffected.
- **Concurrency/retry/reordering/crash behaviour:** read service recovers.
- **Rejected models:** regenerate audit history from logs/provider dashboard.
- **Required invariant:** no business mutation; recovery reads durable Audit evidence.
- **Recommended JIT shape:** ordinary degraded read behaviour.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** later Audit availability.
- **Verdict:** PASS.

## COMM-PT-244 — Does FP-001 Communications require an Audit & Evidence dossier after all?

- **Scenario:** Phase 7C needs privileged Communications retry/reconcile/support evidence.
- **Authority involved:** FP-001 Skeleton conditional rule; Audit Domain law.
- **Durable truths and owner:** current law already defines restricted append-only minimal evidence for sensitive/privileged actions and explicitly separates provider reconciliation evidence.
- **Concurrency/retry/reordering/crash behaviour:** duplicate/reordered audit consequence handled by existing append/idempotent evidence doctrine.
- **Rejected models:** pull dossier merely because Audit receives a link/event; let Communications invent Audit internals.
- **Required invariant:** Communications can state the bounded audit contract without choosing Audit schema/event names/retention duration.
- **Recommended JIT shape:** owner interface for minimum privileged/security evidence; exact Audit implementation remains outside Communications.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** **NO.**
- **Later executable proof:** eventual cross-domain Audit integration in slice/proof.
- **Verdict:** PASS.

---

# 85. Rejected-model register additions — v0.7.0

91. **Central Audit is the delivery-attempt ledger.** Rejected: duplicates Communications authority.
92. **Append one Audit Event for every automated provider callback/retry.** Rejected absent material security/privileged need.
93. **Logs/traces are sufficient delivery history.** Rejected.
94. **Logs/traces are sufficient Audit evidence.** Rejected.
95. **Provider dashboard is Communications authority.** Rejected.
96. **Operator can manually mark delivered/failed.** Rejected without governed evidence/reconciliation.
97. **Routine operator may resend directly from provider portal.** Rejected.
98. **“Retry” and “reconcile” are the same operator command.** Rejected.
99. **UI button presence is action authority.** Rejected.
100. **Privileged send may proceed while required Audit is unavailable and be logged later best-effort.** Rejected.
101. **Telemetry exporter failure should fail a valid automated send/callback.** Rejected.
102. **Full email/phone destination in metric labels.** Rejected.
103. **Account/PMR/MessageIntent/DeliveryAttempt/correlation ids in metric labels.** Rejected.
104. **Raw destination/body in ordinary structured logs.** Rejected.
105. **Log/trace protected bearer URLs/tokens for debugging.** Rejected.
106. **Log raw provider SDK exception/request/headers without adapter sanitisation.** Rejected.
107. **Store provider credentials/signing secrets in business/Audit/telemetry state.** Rejected.
108. **Support can view production bearer/rendered body to debug.** Rejected.
109. **Retain every raw provider payload indefinitely.** Rejected.
110. **Provider event id is global NewYou message identity.** Rejected.
111. **Correlation id is a business idempotency/dedup key.** Rejected.
112. **Meaningful correlation strings containing participant/business identifiers.** Rejected.
113. **Provider `opened/clicked` implies delivered/verified/converted.** Rejected.
114. **Enable security-message engagement tracking merely because provider supports it.** Rejected.
115. **Rewrite protected bearer URLs through provider click tracking.** Rejected.
116. **Disabling provider tracking alone solves automated mail-scanner proof consumption.** Rejected.
117. **A valid token fetched by any automated scanner may complete verification.** Rejected pending Identity upstream correction.
118. **Copy raw security-message engagement/destination/content to Analytics.** Rejected.
119. **One alert per failed message during provider outage.** Rejected.
120. **Terminal-failure queue is a durable business/Audit Resource.** Rejected.
121. **Unrestricted CSV export of Communications failures/provider evidence.** Rejected.
122. **Support free text is an acceptable place for bearer/provider payload dumps.** Rejected.
123. **Break-glass bypasses source/content/privacy/protected-delivery invariants.** Rejected.
124. **Audit retention can recreate deleted Communications authority.** Rejected.

---

# 86. Upstream-delta register — v0.7.0

## COMM-UPD-001 — REQUIRED / unchanged

The certified Identity v0.1.3 Communications ownership sentence still requires narrow correction because current higher authority assigns governed message/template body versions to Content & Media, not Communications.

**Effect:** blocks Communications final JIT certification / Phase 7C freeze until corrected.

## COMM-UPD-002 — REQUIRED IDENTITY REVIEW / new

The certified Identity proof lifecycle does not explicitly close the automated email/security-link scanner prefetch boundary.

The current safe invariant is clear from existing authority:

- Identity alone owns proof consumption;
- provider delivery/status does not establish verification;
- security proofs are purpose-bound and replay-controlled.

But the implementation-grade interaction boundary that prevents an automated URL fetch from becoming the proof consumer is not frozen.

**Smallest safe route:** narrow Identity JIT successor/clarification or an explicitly governed downstream Identity proof contract before Phase 7C final freeze/implementation.

This Communications artifact does not select the mechanism.

## No higher-law amendment identified

Neither `COMM-UPD-001` nor `COMM-UPD-002` requires a Product/Architecture/Domain ownership amendment based on current evidence.

---

# 87. Unresolved-gate register additions — v0.7.0

| Gate / open matter | v0.7.0 effect |
|---|---|
| `COMM-UPD-001` content ownership wording | Continues to block Communications final certification / Phase 7C freeze. |
| `COMM-UPD-002` scanner/prefetch-safe Identity proof use | New cross-domain Identity blocker/clarification before final freeze or implementation. |
| `OQ-029` retention | Exact Communications/Audit/log/trace/Analytics/provider-evidence durations remain unresolved. |
| `OQ-036` provider/channel policy | Must prove provider can disable/avoid protected-link click rewriting/tracking and support safe callback authentication/reconciliation. |
| `OQ-038` incident ownership | Remains later/future-only for FP-001 planning; material incidents can still preserve evidence without selecting the future incident command structure here. |
| Raw provider artifact retention | Provider-specific. Default is normalize/minimise; exact exception requires OQ-036 + retention justification. |
| Support full-destination reveal | Semantic minimum-disclosure rule accepted; exact support-role/grant mapping remains Identity/FES implementation detail. |
| Central Audit event names/schema | Intentionally not frozen. Bounded semantic evidence contract is sufficient for Communications. |
| Security-message engagement analytics | Not required by FP-001. Any later activation requires explicit purpose/privacy/measurement governance. |

---

# 88. Cross-stream dependency register additions — v0.7.0

| Stream / Domain | v0.7.0 finding |
|---|---|
| Identity & Access | Owns operator authentication/grants/break-glass and protected proof consumption. `COMM-UPD-002` routes scanner-safe link consumption here. |
| Audit & Evidence | Owns minimum append-only privileged/security/incident evidence. Does not own delivery/provider reconciliation truth. |
| Communications | Owns MessageIntent, DeliveryAttempt, normalized provider evidence, reconciliation and terminal failure. |
| Privacy & Consent | Governs retention/deletion and any later additional tracking purpose. No new Privacy dossier trigger from required FP-001 observability. |
| Analytics | Remains consumer-only; no raw security-message payload/contact/engagement authority. |
| Content & Media | Exact message version/locale provenance remains available without storing full rendered body in Audit/telemetry. |
| FES / Operating Model | Operator/support UI is policy-aware minimum-necessary projection; routine impersonation/provider-side bypass remains disallowed. |
| Engineering Standards | Backend-neutral bounded observability, cardinality/minimisation and provider error-normalisation rules apply. |
| OQ-036 | Selected provider must satisfy callback-auth, no-protected-link-rewrite, minimised evidence and reconciliation requirements. |
| OQ-038 | Material incident ownership remains later; current FP-001 does not need to invent incident-command topology. |

---

# 89. Conditional-dossier adjudication — v0.7.0

## Audit & Evidence

**Disposition: `CONDITIONAL / NOT PULLED FORWARD`.**

This pass directly tested the Skeleton's condition:

> a dossier is needed if exact FP-001 evidence event, minimisation, access or retention contracts cannot be stated without invention.

The required Communications/Audit contract **can** be stated from current authority without inventing a new Audit lifecycle:

### What Communications owns

- MessageIntent;
- DeliveryAttempt;
- provider operation/evidence;
- current reconciliation/terminal delivery state;
- operator command business result.

### What central Audit receives where applicable

- minimum privileged/security action/access evidence;
- actor/system causation;
- safe target linkage;
- action class;
- reason where required;
- result/outcome;
- bounded incident/security linkage.

### What Audit explicitly does not receive as normal evidence

- protected bearer;
- full rendered message body;
- provider credentials;
- full raw provider payload;
- raw destination by default;
- delivery business authority.

### Access/retention

Existing law already requires restricted access and category-specific retention; exact durations remain OQ-029 and need not be invented in Phase 7B Communications.

No independent Audit Resource/lifecycle is needed to make the Communications contract implementation-grade.

**Pull-forward trigger remains:** if later Phase 7C cannot specify a materially required central evidence action/access/retention rule without creating new Audit-owned semantics.

Current evidence does not meet that trigger.

## Privacy & Consent

**Disposition unchanged.**

Required FP-001 security delivery/observability introduces no new purpose/tracking requirement.

If security open/click analytics is later activated, that is a new governance question and must not be inferred from this contract.

## Content & Media

**Disposition unchanged.**

No new content lifecycle semantics exposed in this pass.

---

# 90. Later executable proof-obligation register additions — v0.7.0

108. Automated send/retry/callback correctness survives total telemetry-export failure.
109. Communications provider evidence remains complete when no central Audit event exists for ordinary automated delivery.
110. Privileged manual retry fails closed if required Audit evidence/intention cannot be durably established.
111. Duplicate/concurrent operator retry produces at most one new DeliveryAttempt.
112. Reconcile action cannot create a new provider submission.
113. Stale operator retry loses to proof expiry/revocation/consumption/deletion/content withdrawal.
114. Late provider callback racing operator reconciliation converges without history rewrite.
115. Operator cannot directly set `delivered`/`failed` provider facts without governed evidence.
116. Provider-dashboard direct manual send is absent/blocked from normal operating procedure.
117. Routine support projection reveals only minimum role/status/masked destination.
118. Full-destination reveal requires current scoped access and remains bearer-free.
119. Support/preview path cannot display/decrypt protected bearer or production secret-bearing rendered body.
120. No email/phone/Account/PMR/MessageIntent/DeliveryAttempt/correlation/provider-message id appears as a metric label.
121. Structured logs/traces contain no raw destination, rendered security body, bearer token/link, provider credential or raw auth header.
122. Provider SDK exceptions are sanitized before logging/tracing.
123. Provider request/response/webhook persistence contains only the approved normalized/minimum fields.
124. Invalid callback authentication produces zero Communications business mutation.
125. Invalid-callback flood does not create unbounded Audit/log/cardinality amplification.
126. Callback-secret rotation preserves fail-closed authenticity and later reconciliation.
127. Duplicate/reused provider ids cannot merge independent internal attempts.
128. Forced correlation-id collision degrades diagnostics only; business identity/idempotency remains correct.
129. Provider-exposed correlation metadata contains no participant/business secret/identity semantics.
130. Reordered `opened/clicked/delivered` evidence cannot advance Identity or business conversion truth.
131. Security-message tracking pixels/click analytics are absent unless a future explicit approved purpose enables them.
132. Selected launch provider proves protected verification/reset/recovery/email-change links are not rewritten through click-tracking redirects.
133. Automated `HEAD`/`GET`/prefetch/security-scanner access cannot alone complete email verification/reset/recovery/email-change transition under the corrected Identity contract.
134. Scanner-first then participant-use interleaving remains safe and replay-controlled.
135. Analytics can be completely unavailable without altering delivery/verification/recovery.
136. Analytics events contain no raw security-message destination/body/bearer/provider payload.
137. Stale dashboard/read model cannot authorize operator action.
138. Provider-wide outage produces bounded actionable alerts rather than per-message alert storm.
139. Duplicate/stale terminal-failure queue entries cannot multiply retries.
140. Any privileged evidence export is bounded/scoped/minimised and cannot include bearer/credentials by default.
141. Free-text support/operator surfaces cannot become a bearer/provider-payload leakage route.
142. Duplicate/reordered central Audit consequence is idempotent/append-safe and never becomes business ordering authority.
143. Break-glass operator action remains MFA-protected, narrow, reasoned, time-bounded, reviewed and subject to Communications source/content/privacy invariants.
144. Material duplicate-send/security incident can be reconstructed through bounded links without duplicating full provider/message payloads into Audit.
145. Provider credential rotation/compromise handling does not mutate historical delivery state or leak old/new secrets.
146. Deletion/legal hold retains only lawful minimum evidence and cannot recreate send/recovery authority.
147. Unauthorised staff cannot access raw provider evidence or full destination through hidden routes/API calls.
148. Audit read/export outage does not lead to reconstruction from non-authoritative logs/provider dashboards.

---

# 91. Resource-discipline review — cumulative through v0.7.0

## `MessageIntent`

**REQUIRED.**

No Audit/observability scenario creates a replacement for the logical communication obligation.

## `DeliveryAttempt`

**REQUIRED.**

It remains the correct durable home for provider-operation/evidence/reconciliation provenance.

## `AuditEvent`

**NOT a Communications Resource.**

Audit & Evidence owns central Audit Event semantics. Communications emits/links minimum evidence where current policy requires it.

## `ProviderWebhookEvent`

**NOT JUSTIFIED as a new FP-001 business Resource.**

Provider ingress evidence can be represented as bounded DeliveryAttempt/provider-evidence history unless a selected provider later proves an independently durable multi-attempt ingress lifecycle. Do not pre-create one.

## `ProviderRawPayload`

**REJECTED as a general Resource.**

Raw artifacts are provider-specific evidence exceptions, not a platform business concept.

## `OperatorAction`

**NOT JUSTIFIED as a new Communications Resource.**

Privileged actions are owner commands with operation identity and Audit evidence. A separate Resource becomes justified only if later evidence proves an independent durable workflow beyond existing intent/attempt + work projection.

## `DeliveryReconciliationCase`

**Still not justified.**

v0.7.0 confirms reconciliation can remain an explicit lifecycle/action on DeliveryAttempt with operator projection and Audit linkage.

## `SupportCase`

**Still rejected.**

Support uses source-owned actions and projections.

## `Incident`

**Not a Communications Resource.**

Material incident evidence/coordination belongs the existing Audit/Operations boundary and later OQ-038 route.

## `TelemetryEvent` / `Metric` / `Trace`

**Not business Resources.**

They are observability signals.

## `EngagementEvent`

**Not required for FP-001 security delivery.**

Open/click measurement is deliberately not pulled into required scope.

**Cumulative required FP-001 Communications Resource verdict remains:**

```text
MessageIntent
DeliveryAttempt
```

---

# 92. Completeness / stabilisation assessment — v0.7.0

**NOT YET STABLE FOR GOVERNED COMMUNICATIONS JIT DOSSIER DRAFTING.**

The Audit/observability/operator-security scenario class is provisionally stable enough to stop broadening it.

The evidence model has now converged to:

```text
Communications business evidence
    MessageIntent + DeliveryAttempt
        ↓ bounded linkage

Audit/security evidence
    minimum privileged/security/governance proof
        ↓

Operational observability
    metrics / logs / traces / alerts / dashboards
    non-authoritative, bounded, failure-isolated
        ↓

Analytics
    optional approved derived measurement only
```

No new Communications Resource was justified.

The Audit & Evidence conditional dossier remains **NOT PULLED FORWARD**.

Two upstream blockers/clarifications now remain before final Phase 7C freeze:

1. `COMM-UPD-001` — correct certified Identity dossier message-template ownership wording.
2. `COMM-UPD-002` — freeze scanner/prefetch-safe protected-link proof-consumption semantics at the Identity boundary or explicitly route them into the governed Identity proof contract.

The next materially distinct pass should be:

## Channel / provider-independent architecture and mature-capability exclusion

Pressure-test:

- email-first versus Product's “email + in-app first” direction;
- whether FP-001 actually needs an in-app inbox/notification Resource;
- verification/recovery when participant is not signed in;
- in-app notification versus required-work/status surfaces;
- future SMS/WhatsApp addition without generic Channel abstraction sprawl;
- channel adapter contract;
- channel selection authority;
- mandatory security fallback;
- provider/channel failover;
- one provider versus multiple providers;
- provider-independent destination/idempotency semantics;
- per-channel provider evidence;
- cross-channel duplicate suppression;
- channel switch during retry;
- security proof sent on multiple channels;
- channel consent/preferences;
- channel-specific content/locale constraints;
- `OQ-036` exact boundary;
- batch/fan-out pressure without importing campaign/journey architecture;
- graceful degradation when one channel is down;
- whether `Channel`, `InAppNotification`, `SubscriberContact`, `NotificationPreference` or `CommunicationJourney` becomes required by the actual FP-001 outcome.

After that, perform the final combined adversarial/stabilisation sweep across all accepted invariants before deciding whether broad Pre-JIT discovery is stable enough to draft the governed Communications JIT dossier.

---

# 93. v0.8.0 semantic delta — channel architecture, provider independence and mature-capability exclusion

This successor preserves all accepted v0.1.0–v0.7.0 findings and adds the eighth substantive Communications pressure-test cluster.

The live repository was rechecked immediately before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

Current higher authority provides the following channel constraints:

- Product Law supports `email`, `in_app`, `sms`, `whatsapp`, `push_future`;
- the Product launch direction is email and in-app first;
- SMS/WhatsApp activate later only after provider/cost/consent validation;
- native push is deferred;
- Communications Domain Law says email provider initially, future SMS/WhatsApp behind channel adapters;
- Architecture requires platform-owned notification intent behind thin channel adapters;
- FES explicitly says an in-app participant notification centre is an approved eventual capability, **not an FP-001 prerequisite**;
- Roadmap FP-001 classifies `OQ-036` as `BLOCKS_RELEASE_ONLY` because email verification and mandatory notices need a valid launch channel, while future reminder/SMS/WhatsApp choices do not block the pack;
- the FP-001 Skeleton allows the Communications JIT to define its delivery contract without choosing a provider/channel policy.

This pass pressure-tests:

- whether Product's “email + in-app first” means both channels are mandatory in FP-001;
- external proof delivery versus in-app account state;
- email verification and proof-of-inbox-control semantics;
- password reset/recovery when signed out;
- old-address security notice during possible compromise;
- participant-visible pending/failure status without an inbox;
- when `InAppNotification` would become a real Resource;
- channel requirement versus provider selection;
- provider replacement versus runtime failover;
- multiple providers on the same channel;
- provider ambiguity during failover;
- provider migration while old attempts are unresolved;
- provider suppression lists versus platform preferences;
- bounce/complaint consequences;
- future SMS versus WhatsApp permission;
- cross-channel fallback;
- multi-channel simultaneous delivery;
- channel-specific content binding;
- batch provider APIs;
- outage-recovery fan-out;
- whether `Channel`, `InAppNotification`, `SubscriberContact`, `NotificationPreference` or `CommunicationJourney` earns FP-001 existence;
- whether `OQ-036` blocks Communications JIT finalisation.

No provider is selected. No email service, SMS service, WhatsApp service, in-app implementation, provider router or runtime failover mechanism is chosen.

---

# 94. Channel-scope adjudication — “email + in-app first” does not mean “both for every FP-001 communication”

There is no current contradiction between Product Law and FES.

The combined authority means:

```text
platform channel direction
→ support email + in-app as the first channel family

FP-001 required outcome
→ requires an externally valid launch channel for verification / mandatory notices

FES
→ in-app participant notification centre is not an FP-001 prerequisite
```

Therefore:

> FP-001 must preserve a channel-capable Communications architecture, but it does not need to ship a durable participant inbox or duplicate every required security message into an in-app notification channel.

For the required FP-001 Identity consequences, email has semantic significance rather than being an arbitrary provider choice:

- `email_verification` must prove access to the target email address;
- `password_reset` / normal recovery may need a verified external route when the participant is not signed in;
- `new_address_confirmation` must reach the proposed new email address;
- `old_address_notice` must reach the previous address independently of the new Account destination;
- compromise/security notices often need an external route precisely because account access may be impaired.

An Identity/account page may still show authoritative pending work/status and Communications delivery status. That is **not** the same thing as introducing a durable `InAppNotification` business Resource.

No Product/Architecture/Domain/Roadmap amendment is required.

---

# 95. Accepted working-design register additions — v0.8.0

## COMM-WD-158 — Product's email + in-app launch direction is capability direction, not mandatory dual delivery

**Status:** `UPSTREAM_DERIVED`

`DEC-261` and Product §21J.18 establish the first channel family.

FES explicitly removes the inference that an in-app participant notification centre must exist in FP-001.

Therefore:

```text
email + in-app first
!=
every FP-001 MessageIntent must create email + in-app delivery
```

Channel use remains message-role/policy specific.

## COMM-WD-159 — Required FP-001 protected Identity communication is email-semantic, not merely “any available channel”

**Status:** `UPSTREAM_DERIVED`

For current FP-001:

- email verification targets the email being proved;
- new-address confirmation targets the proposed email;
- old-address notice targets the old email;
- ordinary reset/recovery uses the approved external verified route.

Communications may choose an email provider under `OQ-036`, but it may not replace the meaning of “verify this email address” with an unrelated channel.

## COMM-WD-160 — In-app account/work status is not an InAppNotification

**Status:** `UPSTREAM_DERIVED`

The participant can be shown:

- `verification pending`;
- resend availability;
- change-email route;
- delayed delivery;
- terminal delivery failure/recovery action

through the owning Identity/account journey plus Communications status projection.

That satisfies the Operating Model rule that required work is not present only in email/ephemeral UI.

It does not require a durable inbox item, read/unread lifecycle or `InAppNotification` Resource.

## COMM-WD-161 — `InAppNotification` remains outside required FP-001 Resources

**Status:** `UPSTREAM_DERIVED`

A future in-app notification centre may have independent:

- unread/read state;
- archival/dismissal;
- participant notification history;
- inbox pagination;
- retention/deletion;
- PubSub freshness.

Those would justify an `InAppNotification` concept when introduced.

FP-001 does not need that lifecycle.

## COMM-WD-162 — Required-work visibility remains source-owned even when Communications delivers the message

**Status:** `UPSTREAM_DERIVED`

Verification/recovery work does not become Communications authority merely because Communications sends the email.

Example:

```text
Identity: verification required / challenge current
Communications: message pending / attempted / terminal
UI: combines current owner truth
```

Deleting/rebuilding a UI notification/read model cannot remove the underlying required work.

## COMM-WD-163 — Channel requirement and provider selection are separate decisions

**Status:** `WORKING_DESIGN_ACCEPTED`

A logical message can carry a **channel requirement/constraint** without knowing the provider.

Conceptually:

```text
source obligation
→ communication role
→ channel requirement / allowed-channel policy
→ Communications provider selection
→ DeliveryAttempt
```

For FP-001 protected Identity messages the requirement is currently email-specific.

The source Domain never selects an email vendor.

## COMM-WD-164 — Source semantics may constrain channel; Communications owns execution inside that constraint

**Status:** `WORKING_DESIGN_ACCEPTED`

Examples:

- email verification constrains delivery to the target email channel;
- future optional reminders may permit a preference-selected channel;
- future safety communication may have separately governed override rules.

Communications cannot choose a channel that changes the proof/business meaning owned by the source Domain.

## COMM-WD-165 — There is no generic automatic cross-channel fallback in FP-001

**Status:** `WORKING_DESIGN_ACCEPTED`

Failure of email does not mean:

```text
email failed
→ try in_app
→ then SMS
→ then WhatsApp
```

without explicit policy.

Cross-channel fallback can change:

- proof meaning;
- privacy/consent;
- destination;
- content constraints;
- participant expectation;
- duplication risk.

It must be explicitly governed per message role.

## COMM-WD-166 — Email-verification proof must not be delivered through another channel as a substitute for inbox control

**Status:** `UPSTREAM_DERIVED`

Sending the email-verification bearer in-app, by SMS or by WhatsApp would allow possession of another channel/session to stand in for access to the email inbox being verified.

That would weaken the meaning of Identity's `email_verified` truth.

Future alternate identity-verification mechanisms require Identity/Product authority; they are not Communications fallback.

## COMM-WD-167 — Future phone/WhatsApp recovery requires source-level Identity semantics before Communications can use it

**Status:** `WORKING_DESIGN_ACCEPTED`

A phone number's presence does not make it an approved recovery channel.

Future SMS/WhatsApp recovery requires:

- Identity definition of what the channel proves;
- verified destination/control semantics;
- applicable Privacy/consent rules;
- current Communications preference/mandatory policy;
- provider validation.

Communications cannot introduce phone recovery by adapter configuration alone.

## COMM-WD-168 — MessageIntent remains one logical communication obligation across same-channel provider attempts

**Status:** `WORKING_DESIGN_ACCEPTED`

Switching/retrying email provider does not create a new logical message merely because infrastructure changed.

```text
one MessageIntent
→ DeliveryAttempt(email, provider A)
→ DeliveryAttempt(email, provider B)  # only when safe/authorised
```

Business deduplication remains at MessageIntent/source-obligation level.

## COMM-WD-169 — Same-channel provider failover creates a new DeliveryAttempt only after safe admission

**Status:** `WORKING_DESIGN_ACCEPTED`

Provider B may be used for the same intent only if:

- current source/content/privacy/channel authority still permits delivery;
- the previous provider operation is definitively non-delivered/non-ambiguous, **or**
- no provider operation actually began;
- retry budget still permits another submission;
- selected launch policy allows provider failover.

A new provider submission gets a new DeliveryAttempt/provider-operation identity.

## COMM-WD-170 — Unknown provider outcome blocks failover to another provider

**Status:** `UPSTREAM_DERIVED` from provider-ambiguity doctrine

If provider A may already have accepted the message:

```text
A outcome = UNKNOWN
→ do not send same logical message through B merely to be safe
→ reconcile A first
```

Changing vendor does not solve ambiguity.

Business idempotency cannot make two unrelated provider networks exactly-once.

## COMM-WD-171 — Provider acceptance/delay is not a failover trigger

**Status:** `WORKING_DESIGN_ACCEPTED`

`accepted != delivered`, but accepted is evidence that an external operation exists.

Slow delivery or delayed callback does not justify sending the same security message through a second provider.

Failover requires a policy-supported, safe new-attempt condition.

## COMM-WD-172 — Provider configuration changes never rewrite historical DeliveryAttempt identity

**Status:** `WORKING_DESIGN_ACCEPTED`

Each DeliveryAttempt retains the actual:

- channel;
- provider/adapter identity;
- provider operation identity;
- exact content/locale provenance;
- normalized outcome evidence.

Changing the configured default provider affects later admitted attempts only.

## COMM-WD-173 — Outstanding ambiguity remains reconcilable against the provider that created it

**Status:** `WORKING_DESIGN_ACCEPTED`

A migration from provider A to B cannot discard the ability to reconcile still-open A attempts.

The platform must retain the minimum adapter/configuration/evidence capability needed for bounded old-provider reconciliation until those attempts terminalise or are otherwise lawfully closed.

This does not require retaining old credentials forever; migration planning must safely close or transfer the reconciliation obligation.

## COMM-WD-174 — Replaceable provider boundary does not imply a runtime multi-provider router

**Status:** `WORKING_DESIGN_ACCEPTED`

FP-001 needs:

- an email capability boundary;
- a replaceable provider adapter;
- normalized outcomes;
- callback/reconciliation contract.

It does **not** currently justify:

- weighted provider routing;
- automatic health-based routing;
- provider marketplace/registry;
- active-active delivery vendors;
- generic failover engine.

`OQ-036` may select one launch email provider and still satisfy the architecture.

## COMM-WD-175 — Channel adapters are thin and typed, not one universal `send(map)` abstraction

**Status:** `WORKING_DESIGN_ACCEPTED`

Future email, SMS, WhatsApp and in-app channels have different:

- destinations;
- consent/preference rules;
- content constraints;
- provider evidence;
- callback semantics;
- size/template requirements.

They may share a normalized execution outcome algebra such as:

```text
definitive_success_or_acceptance
definitive_retryable_failure
definitive_terminal_failure
unknown_requires_reconciliation
```

but should preserve channel-specific typed inputs rather than flattening every channel into an untyped generic payload.

## COMM-WD-176 — `Channel` is a required bounded concept, not a required database Resource

**Status:** `WORKING_DESIGN_ACCEPTED`

Product already supplies the channel vocabulary:

```text
email
in_app
sms
whatsapp
push_future
```

The actual channel used is material DeliveryAttempt provenance.

That does not justify a mutable `Channel` business Resource for FP-001.

Configuration/adapter availability may remain code/configuration until independent durable business lifecycle proves otherwise.

## COMM-WD-177 — SMS and WhatsApp remain separate channels even if both use the same phone number

**Status:** `UPSTREAM_DERIVED`

One phone destination does not collapse:

```text
sms preference/permission
whatsapp preference/permission
```

They may have different provider, consent, cost, template and delivery semantics.

Future implementation must not create a generic `phone_message` permission that silently broadens channel scope.

## COMM-WD-178 — `push_future` remains a vocabulary seam only

**Status:** `UPSTREAM_DERIVED`

Native push is explicitly deferred.

FP-001 does not create:

- device-push registrations;
- push-token Resources;
- push adapters;
- push preference UI;
- push retry rules.

The architecture simply must not make later addition impossible.

## COMM-WD-179 — Cross-channel delivery requires an explicit fulfillment policy

**Status:** `WORKING_DESIGN_ACCEPTED`

If a future message may lawfully use multiple channels, the intent needs an explicit rule such as conceptually:

```text
EMAIL_REQUIRED
ANY_ONE_ALLOWED_CHANNEL
ALL_REQUIRED_CHANNELS
PRIMARY_THEN_EXPLICIT_FALLBACK
```

This is illustrative, not a frozen enum.

No implicit “try everything” policy exists.

## COMM-WD-180 — Explicit multi-channel delivery is not the same thing as accidental duplicate delivery

**Status:** `WORKING_DESIGN_ACCEPTED`

If future policy intentionally requires both email and in-app, two channel deliveries can satisfy one logical communication policy.

That is different from accidentally retrying the same email twice.

Current FP-001 does not need this multi-channel fulfillment model.

## COMM-WD-181 — Provider suppression state is a physical delivery constraint, not Communications preference or Privacy permission

**Status:** `UPSTREAM_DERIVED`

A provider may suppress a destination because of:

- bounce;
- complaint;
- provider policy;
- reputation controls;
- prior provider-side unsubscribe.

That can prevent physical delivery.

It does not automatically mutate:

- Identity canonical email;
- Privacy marketing permission;
- Communications preference;
- source business truth.

NewYou must record/reconcile the delivery constraint separately.

## COMM-WD-182 — Marketing suppression must not become mandatory-security preference authority

**Status:** `UPSTREAM_DERIVED` plus `OQ-036` provider requirement

The selected email implementation must preserve the Product distinction between:

- optional marketing;
- mandatory/necessary security or transactional communication.

A marketing unsubscribe cannot silently become the platform rule “never send password reset/security email”.

If the selected provider has global suppression semantics that make this impossible, that is a launch-provider suitability problem under `OQ-036`, not a reason to collapse platform permissions.

## COMM-WD-183 — Hard bounce/invalid mailbox evidence does not mutate Identity canonical email

**Status:** `UPSTREAM_DERIVED`

A definitive email delivery failure can:

- terminalise/suppress the current delivery attempt according to policy;
- make failure visible;
- enable participant change-email/recovery flows where permitted.

It cannot directly change Account.email or verification truth.

## COMM-WD-184 — Content binding is channel-specific when different channels are introduced

**Status:** `WORKING_DESIGN_ACCEPTED`

v0.5's exact content/locale provenance remains valid.

For current FP-001 email:

```text
role + locale + email
→ exact eligible C&M binding
```

A future SMS/WhatsApp/in-app attempt must not assume the email body is valid for that channel.

If a lawful channel switch occurs, exact new channel-appropriate content must be bound before the new attempt.

Historical attempts retain their own exact binding.

## COMM-WD-185 — Provider batch APIs are execution optimisations only if per-recipient truth remains independently reconstructible

**Status:** `WORKING_DESIGN_ACCEPTED`

A future provider bulk API may be used only if the platform can still determine per MessageIntent/recipient:

- whether an operation actually began;
- provider operation identity/evidence;
- success/failure/unknown outcome;
- retry eligibility;
- exact content/channel provenance.

One opaque batch status cannot replace individual Communications truth.

FP-001 does not require provider batching.

## COMM-WD-186 — Outage backlog recovery is not a CommunicationJourney

**Status:** `UPSTREAM_DERIVED`

Selecting/paginating thousands of pending MessageIntents after provider recovery is operational recovery of existing obligations.

It does not create:

- campaign membership;
- scheduled marketing sequence;
- journey state;
- new communication business intent.

No `CommunicationJourney` is justified by batch recovery.

## COMM-WD-187 — `OQ-036` remains release-blocking, not Communications-JIT-blocking

**Status:** `UPSTREAM_DERIVED`

The Communications JIT can freeze:

- channel/source ownership;
- email-semantic FP-001 roles;
- adapter boundary;
- normalized provider outcome algebra;
- attempt/idempotency/reconciliation semantics;
- provider-independent operator/retry rules;
- privacy/content/evidence boundaries.

`OQ-036` later chooses/proves:

- launch email implementation/provider;
- any launch in-app implementation/policy;
- exact provider capabilities;
- provider callback/authentication behaviour;
- delivery/reconciliation support;
- exact retry/backoff/rate/operational values;
- provider suppression configuration;
- later SMS/WhatsApp activation.

The selected provider must satisfy the contract.

The contract is not weakened to fit the provider.

---

# 96. Channel / provider execution model — v0.8.0

## 96.1 Required FP-001 logical path

For the current protected Identity roles:

```text
Identity source obligation
→ email-semantic MessageIntent
→ current source/content/privacy checks
→ selected launch email adapter/provider
→ DeliveryAttempt(channel=email, provider=<selected>)
→ provider evidence / bounded retry / reconciliation / terminal failure
```

No in-app inbox object is required.

## 96.2 Participant experience in parallel

```text
Identity source state
+ Communications delivery projection
→ verification/recovery/account status UI
```

Examples:

- `Check your email`;
- `Still waiting`;
- `Resend`;
- `Change email`;
- `Delivery problem`;
- `Use recovery/support`.

This UI is not the business delivery authority and not an `InAppNotification`.

## 96.3 Same-channel provider switch

```text
attempt A never started
→ provider B may be selected if policy allows

attempt A definitive non-delivery
→ provider B may be new DeliveryAttempt if policy allows

attempt A unknown
→ NO provider B submission
→ reconcile A

attempt A accepted / may deliver
→ NO speculative B duplicate
```

## 96.4 Future cross-channel seam

A future message may have:

```text
source role
+ channel constraints
+ purpose permission
+ channel preference
+ explicit fulfillment/fallback policy
+ channel-specific content eligibility
```

Only then can Communications choose among multiple channels.

Current FP-001 does not need to implement that mature policy engine.

---

# 97. Pressure-test register — eighth cluster

## COMM-PT-245 — Product says email + in-app first while FES says notification centre is not FP-001 prerequisite

- **Scenario:** literal reading appears to require an FP-001 inbox.
- **Authority involved:** Product §21J.18 / DEC-261; FES; Roadmap FP-001.
- **Durable truths and owner:** Communications owns in-app notification state only where introduced.
- **Concurrency/retry/reordering/crash behaviour:** none needed for scope adjudication.
- **Rejected models:** create `InAppNotification` solely to satisfy the phrase “in-app first”; ignore channel-capable architecture entirely.
- **Required invariant:** platform direction and Feature-Pack outcome remain distinct.
- **Recommended JIT shape:** email execution now; preserve typed future in-app seam; no inbox Resource.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** FP-001 flow succeeds without inbox.
- **Verdict:** PASS.

## COMM-PT-246 — Newly registered unverified participant is viewing the verification-pending page

- **Scenario:** participant is signed in enough for limited onboarding but not email-verified.
- **Authority involved:** Identity verification gate + FES.
- **Durable truths and owner:** verification work is Identity; delivery status Communications.
- **Concurrency/retry/reordering/crash behaviour:** email may be delayed/retried while page reconnects.
- **Rejected models:** create durable in-app notification just to display `check your email`.
- **Required invariant:** page reconstructs required work/status from durable owner state.
- **Recommended JIT shape:** Identity source projection + Communications status.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** reconnect/restart retains correct pending UI without inbox.
- **Verdict:** PASS.

## COMM-PT-247 — Participant requests password reset while signed out

- **Scenario:** no authenticated in-app context exists.
- **Authority involved:** Identity recovery + Communications external delivery.
- **Durable truths and owner:** proof source Identity; delivery Communications.
- **Concurrency/retry/reordering/crash behaviour:** email outage/backlog.
- **Rejected models:** in-app is a mandatory co-channel for reset.
- **Required invariant:** recovery remains usable from the external/email route selected by Identity policy.
- **Recommended JIT shape:** email-semantic intent.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** signed-out reset flow.
- **Verdict:** PASS.

## COMM-PT-248 — Email-verification token is displayed inside in-app notification

- **Scenario:** implementation tries to provide a convenient fallback.
- **Authority involved:** Identity meaning of `email_verified`.
- **Durable truths and owner:** proof of target inbox control remains Identity authority.
- **Concurrency/retry/reordering/crash behaviour:** session holder could consume without inbox.
- **Rejected models:** in-app session possession is equivalent to email inbox possession.
- **Required invariant:** verification bearer is delivered to the email being verified.
- **Recommended JIT shape:** in-app may say `check your email` but not substitute proof.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO beyond existing COMM-UPD-002 scanner-safe consumption.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** no alternate-channel verification path.
- **Verdict:** PASS.

## COMM-PT-249 — Old-address email-change notice during possible account compromise

- **Scenario:** attacker controls current session/new address; old address owner needs notice.
- **Authority involved:** DEC-251 Identity email-change security boundary.
- **Durable truths and owner:** old-address notice is Communications consequence to old email snapshot.
- **Concurrency/retry/reordering/crash behaviour:** canonical email may already change after apply.
- **Rejected models:** replace old-address notice with in-app notification accessible to attacker.
- **Required invariant:** old external destination provenance remains independently deliverable.
- **Recommended JIT shape:** email-specific old-address MessageIntent.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** attacker/session context cannot suppress old-address routing.
- **Verdict:** PASS.

## COMM-PT-250 — Security notice is delivered only in-app after participant loses Account access

- **Scenario:** compromise/recovery locks the participant out.
- **Authority involved:** Identity recovery/compromise + Communications.
- **Durable truths and owner:** participant may not see in-app channel.
- **Concurrency/retry/reordering/crash behaviour:** session revoked.
- **Rejected models:** in-app is universal mandatory fallback.
- **Required invariant:** required security route is usable under the source scenario.
- **Recommended JIT shape:** external verified route where source policy requires it.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** revoked sessions do not make notice invisible-only.
- **Verdict:** PASS.

## COMM-PT-251 — Verification delivery enters terminal failure while participant remains on account page

- **Scenario:** provider cannot deliver email.
- **Authority involved:** Communications terminal failure + Identity required work.
- **Durable truths and owner:** verification remains pending; failure remains Communications.
- **Concurrency/retry/reordering/crash behaviour:** support/resend/change-email action may occur.
- **Rejected models:** terminal failure exists only in admin queue/email; in-app inbox required.
- **Required invariant:** participant-visible recovery route exists on owning journey.
- **Recommended JIT shape:** account status projection + resend/change-email/support.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** terminal failure participant recovery.
- **Verdict:** PASS.

## COMM-PT-252 — Future in-app notification centre is introduced in a later Feature Pack

- **Scenario:** durable inbox/read state becomes real product capability.
- **Authority involved:** Communications Domain + FES.
- **Durable truths and owner:** in-app notification/read lifecycle Communications.
- **Concurrency/retry/reordering/crash behaviour:** multi-device read/unread and deletion.
- **Rejected models:** force lifecycle onto MessageIntent only; pre-build it in FP-001.
- **Required invariant:** later Resource justified by independent lifecycle, not by current noun list.
- **Recommended JIT shape:** later JIT may introduce `InAppNotification`.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO now.
- **Later executable proof:** future.
- **Verdict:** DEFER / NOT FP-001.

## COMM-PT-253 — Identity requests `send_with_provider_X`

- **Scenario:** source Domain knows a vendor name.
- **Authority involved:** Architecture thin adapter boundary + Domain ownership.
- **Durable truths and owner:** provider selection belongs Communications execution.
- **Concurrency/retry/reordering/crash behaviour:** provider changes/migration.
- **Rejected models:** source provider coupling.
- **Required invariant:** source requests semantic communication/channel constraint, never vendor.
- **Recommended JIT shape:** provider-opaque owner interface.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** source API contains no provider enum/vendor id.
- **Verdict:** PASS.

## COMM-PT-254 — Default email provider changes after MessageIntent creation but before first attempt

- **Scenario:** operational config switches A→B.
- **Authority involved:** Communications execution.
- **Durable truths and owner:** no provider operation yet exists.
- **Concurrency/retry/reordering/crash behaviour:** workers on different nodes may read config around change.
- **Rejected models:** MessageIntent must snapshot provider at source transaction; two workers independently create A/B attempts.
- **Required invariant:** first admitted DeliveryAttempt durably binds one provider; no duplicate provider operations.
- **Recommended JIT shape:** provider selected inside concurrency-safe attempt admission.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** config switch + two workers.
- **Verdict:** PASS.

## COMM-PT-255 — Provider A outage is known before any provider call begins

- **Scenario:** launch policy later has an approved provider B.
- **Authority involved:** OQ-036 execution policy.
- **Durable truths and owner:** no A DeliveryAttempt operation has begun.
- **Concurrency/retry/reordering/crash behaviour:** dependency-health state may race.
- **Rejected models:** fabricate failed A attempt; always wait for A merely because it is default.
- **Required invariant:** if policy permits B and current guards pass, B may become the first provider attempt.
- **Recommended JIT shape:** provider selection at attempt admission; exact failover policy OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** only if multi-provider launch policy selected.
- **Verdict:** PASS CONDITIONALLY.

## COMM-PT-256 — Provider A times out after request may have been accepted; provider B is healthy

- **Scenario:** classic cross-provider failover temptation.
- **Authority involved:** provider ambiguity doctrine.
- **Durable truths and owner:** A DeliveryAttempt = unknown/reconciliation required.
- **Concurrency/retry/reordering/crash behaviour:** late A acceptance/delivery possible.
- **Rejected models:** send through B immediately; new provider means new idempotency namespace so duplicate is safe.
- **Required invariant:** no B submission while A outcome is ambiguous.
- **Recommended JIT shape:** reconcile A first.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** timeout A + healthy B.
- **Verdict:** PASS.

## COMM-PT-257 — Provider A definitively reports operation was not accepted/submitted

- **Scenario:** provider-specific failure occurs before delivery operation exists.
- **Authority involved:** normalized adapter evidence + retry policy.
- **Durable truths and owner:** first attempt definitive non-delivery.
- **Concurrency/retry/reordering/crash behaviour:** failover can race source expiry.
- **Rejected models:** create a new MessageIntent.
- **Required invariant:** same intent may create B DeliveryAttempt only after all current guards are revalidated.
- **Recommended JIT shape:** same-channel failover as retry.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** selected-provider failover if applicable.
- **Verdict:** PASS.

## COMM-PT-258 — Provider A accepted message but provider delivery callback is slow

- **Scenario:** operations sees delay and wants B.
- **Authority involved:** provider evidence + no-duplicate policy.
- **Durable truths and owner:** accepted A external operation exists.
- **Concurrency/retry/reordering/crash behaviour:** late delivery/callback.
- **Rejected models:** accepted-but-not-delivered means safe to fail over.
- **Required invariant:** do not create speculative B duplicate.
- **Recommended JIT shape:** wait/reconcile/terminal policy under OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider latency.
- **Verdict:** PASS.

## COMM-PT-259 — Provider A returns hard invalid-recipient bounce; provider B is healthy

- **Scenario:** address itself appears invalid.
- **Authority involved:** Communications provider evidence + Identity destination ownership.
- **Durable truths and owner:** bounce is delivery evidence, not Account mutation.
- **Concurrency/retry/reordering/crash behaviour:** participant may change email concurrently.
- **Rejected models:** try providers B/C indefinitely; mark Identity email invalid automatically.
- **Required invariant:** destination-class terminal failure does not become vendor failover storm.
- **Recommended JIT shape:** terminal/current failure + participant change-email/recovery route.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** hard-bounce classification.
- **Verdict:** PASS.

## COMM-PT-260 — Provider A returns a retryable provider-side 5xx

- **Scenario:** provider error is definite but temporary.
- **Authority involved:** normalized failure taxonomy; OQ-036 retry policy.
- **Durable truths and owner:** attempt definitively failed/retryable.
- **Concurrency/retry/reordering/crash behaviour:** retry could use A or approved B.
- **Rejected models:** hard-code all 5xx as B failover; indefinite A retries.
- **Required invariant:** provider-specific retry/failover choice remains bounded and current-authority-checked.
- **Recommended JIT shape:** normalized retryable class; exact route OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider-selected policy.
- **Verdict:** PASS / OQ-036 DETAIL.

## COMM-PT-261 — Provider A account/service is suspended globally

- **Scenario:** no sends can proceed through A.
- **Authority involved:** graceful degradation + OQ-036.
- **Durable truths and owner:** existing intents remain Communications truth.
- **Concurrency/retry/reordering/crash behaviour:** many workers discover outage.
- **Rejected models:** mark all intents terminal immediately; auto-route to unknown unapproved provider.
- **Required invariant:** coordinated degradation; approved B only if configured/policy-valid; otherwise queue/surface failure.
- **Recommended JIT shape:** provider-independent backlog + bounded operational failover.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider outage.
- **Verdict:** PASS.

## COMM-PT-262 — Late callback from provider A arrives after a safe provider-B failover

- **Scenario:** A was believed definitively non-delivered but later emits evidence.
- **Authority involved:** Communications reconciliation.
- **Durable truths and owner:** both DeliveryAttempts remain historical evidence.
- **Concurrency/retry/reordering/crash behaviour:** callback may contradict adapter classification.
- **Rejected models:** discard old-provider callback; overwrite B attempt.
- **Required invariant:** reconcile evidence, detect duplicate-delivery/invariant breach if applicable, never rewrite source truth.
- **Recommended JIT shape:** per-attempt provider provenance + incident signal if contract violation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** multi-provider only if selected.
- **Verdict:** PASS.

## COMM-PT-263 — Provider A late evidence says delivered after B also delivered

- **Scenario:** failover produced physical duplicate.
- **Authority involved:** Communications attempt evidence; incident/quality.
- **Durable truths and owner:** one logical intent, two actual deliveries.
- **Concurrency/retry/reordering/crash behaviour:** evidence arrives in either order.
- **Rejected models:** hide one attempt to preserve “no duplicate” appearance.
- **Required invariant:** preserve truthful evidence; mark duplicate-delivery invariant breach; source business truth still unchanged.
- **Recommended JIT shape:** bounded incident/operational evidence.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** failover contract if multi-provider.
- **Verdict:** PASS / INCIDENT CONDITION.

## COMM-PT-264 — Provider A and B callbacks arrive reordered for same intent

- **Scenario:** multi-provider history exists.
- **Authority involved:** per-attempt evidence.
- **Durable truths and owner:** each callback belongs to one provider operation.
- **Concurrency/retry/reordering/crash behaviour:** arbitrary order.
- **Rejected models:** one intent-level provider status field with last-callback-wins.
- **Required invariant:** attempt-specific evidence first; intent aggregate derives safely.
- **Recommended JIT shape:** DeliveryAttempt remains independent evidence owner.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** callback reorder.
- **Verdict:** PASS.

## COMM-PT-265 — Two providers use the same external message-id string

- **Scenario:** provider id namespaces collide.
- **Authority involved:** internal attempt identity.
- **Durable truths and owner:** external id is scoped by provider/account.
- **Concurrency/retry/reordering/crash behaviour:** callbacks.
- **Rejected models:** global unique provider_message_id constraint without provider scope.
- **Required invariant:** no cross-provider evidence collision.
- **Recommended JIT shape:** internal DeliveryAttempt id + provider-scoped external identity.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** fixture collision.
- **Verdict:** PASS.

## COMM-PT-266 — Platform migrates new sends from provider A to B while A has unknown attempts

- **Scenario:** planned vendor migration.
- **Authority involved:** provider reconciliation + operational config.
- **Durable truths and owner:** old A attempts retain A provenance.
- **Concurrency/retry/reordering/crash behaviour:** new B attempts run while A callbacks continue.
- **Rejected models:** migrate all unresolved A attempts by re-sending through B.
- **Required invariant:** new intents/eligible future attempts may use B; unresolved A operations remain A reconciliation obligations.
- **Recommended JIT shape:** provider version/provenance on attempt.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider migration runbook.
- **Verdict:** PASS.

## COMM-PT-267 — Provider A credentials are revoked before unknown A attempts are reconciled

- **Scenario:** migration/security rotation removes lookup access.
- **Authority involved:** Communications reconciliation + provider operations.
- **Durable truths and owner:** unknown cannot be guessed complete/failed.
- **Concurrency/retry/reordering/crash behaviour:** callbacks may still arrive or never arrive.
- **Rejected models:** credential revocation converts unknown to failed; blindly send via B.
- **Required invariant:** unresolved status remains honest; migration/credential-rotation planning must close or govern outstanding ambiguity.
- **Recommended JIT shape:** OQ-036 runbook/capability requirement.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** operational migration.
- **Verdict:** PASS / RELEASE OPERATIONS DETAIL.

## COMM-PT-268 — Default provider switches to B but queued work was created while A was default

- **Scenario:** provider is not part of source business identity.
- **Authority involved:** Communications attempt admission.
- **Durable truths and owner:** MessageIntent persists independently.
- **Concurrency/retry/reordering/crash behaviour:** worker restart after config switch.
- **Rejected models:** queued job payload hard-codes A forever.
- **Required invariant:** provider chosen from current approved policy when a new attempt is admitted, unless a prior attempt already binds/requires reconciliation.
- **Recommended JIT shape:** jobs carry intent/attempt ids, not provider secret/config blobs.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** config change/restart.
- **Verdict:** PASS.

## COMM-PT-269 — Provider marketing unsubscribe list globally suppresses the same email used for password reset

- **Scenario:** provider has coarse suppression behaviour.
- **Authority involved:** Product mandatory-vs-marketing separation; OQ-036.
- **Durable truths and owner:** marketing opt-out != security suppression.
- **Concurrency/retry/reordering/crash behaviour:** provider may reject security attempt.
- **Rejected models:** platform changes password-reset policy to honor marketing unsubscribe; silently clear participant marketing opt-out to send reset.
- **Required invariant:** provider setup must support lawful mandatory-security delivery independently or surface a launch-blocking provider limitation.
- **Recommended JIT shape:** provider suitability test under OQ-036.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** selected provider suppression semantics.
- **Verdict:** PASS / RELEASE GATE.

## COMM-PT-270 — Provider unsubscribe callback arrives from a marketing stream

- **Scenario:** destination also has FP-001 security intents.
- **Authority involved:** provider evidence + platform permission owners.
- **Durable truths and owner:** provider callback does not globally alter NewYou permissions.
- **Concurrency/retry/reordering/crash behaviour:** callback may precede security attempt.
- **Rejected models:** set global email-disabled flag.
- **Required invariant:** scope provider evidence correctly; mandatory security remains source/policy governed.
- **Recommended JIT shape:** normalized provider suppression evidence by stream/purpose where supported.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider-specific.
- **Verdict:** PASS.

## COMM-PT-271 — Verification email hard-bounces

- **Scenario:** participant entered inaccessible/invalid address.
- **Authority involved:** Identity canonical/candidate email + Communications evidence.
- **Durable truths and owner:** bounce does not change Identity.
- **Concurrency/retry/reordering/crash behaviour:** participant may request address change while callbacks arrive.
- **Rejected models:** automatically correct Account email from provider guess; repeated vendor failover.
- **Required invariant:** verification remains unverified; participant gets safe change-email/recovery path.
- **Recommended JIT shape:** terminal failure projection to Identity journey.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** bounce + change-email race.
- **Verdict:** PASS.

## COMM-PT-272 — Recipient marks a security email as spam / provider records complaint

- **Scenario:** provider suppresses future mail.
- **Authority involved:** provider evidence; Identity required source.
- **Durable truths and owner:** complaint does not revoke Account email or source proof.
- **Concurrency/retry/reordering/crash behaviour:** future recovery attempt may be physically blocked.
- **Rejected models:** convert complaint into marketing-consent withdrawal or Account-email mutation.
- **Required invariant:** provider delivery constraint is visible/reconcilable; participant recovery path remains.
- **Recommended JIT shape:** provider-specific terminal/suppression evidence under OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** selected provider.
- **Verdict:** PASS.

## COMM-PT-273 — Participant opts out of marketing email, then requests password reset

- **Scenario:** same channel, different purpose.
- **Authority involved:** v0.4 preference boundary + Identity reset.
- **Durable truths and owner:** marketing preference remains negative; reset is mandatory/source-authorised.
- **Concurrency/retry/reordering/crash behaviour:** preference callback may race reset.
- **Rejected models:** channel-wide application suppression.
- **Required invariant:** reset may use email under security policy.
- **Recommended JIT shape:** role-aware channel admission.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** required vs optional channel isolation.
- **Verdict:** PASS.

## COMM-PT-274 — Email attempt fails and a phone number exists; system tries SMS automatically

- **Scenario:** future channel is technically available.
- **Authority involved:** channel/permission policy.
- **Durable truths and owner:** phone existence != SMS permission/recovery authority.
- **Concurrency/retry/reordering/crash behaviour:** email result may be ambiguous.
- **Rejected models:** generic cross-channel fallback.
- **Required invariant:** no SMS without explicit source/channel authority and current permission/policy.
- **Recommended JIT shape:** no FP-001 fallback.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** possible Privacy future, not now.
- **Later executable proof:** later SMS activation.
- **Verdict:** PASS.

## COMM-PT-275 — Same phone number could receive both SMS and WhatsApp

- **Scenario:** mature platform adds both.
- **Authority involved:** DEC-261/262 and Privacy.
- **Durable truths and owner:** channels remain independent.
- **Concurrency/retry/reordering/crash behaviour:** preferences may diverge.
- **Rejected models:** one `phone_enabled` flag.
- **Required invariant:** one channel's permission/preference cannot authorize the other.
- **Recommended JIT shape:** separate channel vocabulary/adapters/preferences when introduced.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** not for FP-001.
- **Later executable proof:** future.
- **Verdict:** DEFER / PASS PRINCIPLE.

## COMM-PT-276 — Participant changes phone number while future SMS message is queued

- **Scenario:** mature channel destination changes.
- **Authority involved:** source/contact owner + Communications snapshot rules.
- **Durable truths and owner:** current/source-approved destination semantics matter.
- **Concurrency/retry/reordering/crash behaviour:** old job wakes after change.
- **Rejected models:** silently substitute new number on existing intent without source policy; always send stale old number.
- **Required invariant:** future channel JIT must define destination snapshot/current-authority rules per role.
- **Recommended JIT shape:** analogous to email destination provenance, not prebuilt now.
- **Conclusion:** `OPEN_HYPOTHESIS` future-only.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-277 — Email-verification proof is sent by SMS as fallback

- **Scenario:** email provider is down but SMS works.
- **Authority involved:** Identity email-verification truth.
- **Durable truths and owner:** SMS possession does not prove email inbox possession.
- **Concurrency/retry/reordering/crash behaviour:** proof remains valid.
- **Rejected models:** multi-channel availability weakens proof semantics.
- **Required invariant:** no SMS substitute for email verification.
- **Recommended JIT shape:** queue email / participant change-email route.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** channel policy tests.
- **Verdict:** PASS.

## COMM-PT-278 — Future recovery uses SMS

- **Scenario:** product later wants verified-phone recovery.
- **Authority involved:** Identity recovery authority + Privacy/channel policy.
- **Durable truths and owner:** Communications cannot define what phone proof means.
- **Concurrency/retry/reordering/crash behaviour:** SIM change/number recycle risks outside current contract.
- **Rejected models:** simply reuse email recovery token over SMS.
- **Required invariant:** Identity must first govern phone recovery semantics.
- **Recommended JIT shape:** future upstream Identity/Product work before channel adapter activation.
- **Conclusion:** `OPEN_HYPOTHESIS`.
- **Upstream amendment:** NO for current FP-001.
- **Conditional dossier pulled forward:** future Privacy likely if activated.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-279 — Future policy permits email→SMS fallback after definitive email non-delivery

- **Scenario:** same source obligation may use alternate channel.
- **Authority involved:** future source/channel fulfillment policy.
- **Durable truths and owner:** one logical obligation could remain MessageIntent.
- **Concurrency/retry/reordering/crash behaviour:** channel change races source invalidation.
- **Rejected models:** automatically create new logical intent solely because provider/channel changed; assume same content/proof is valid.
- **Required invariant:** fallback requires explicit source semantics, destination authority, permission and channel-specific content.
- **Recommended JIT shape:** same intent may support explicit fallback only if future contract proves equivalence.
- **Conclusion:** `OPEN_HYPOTHESIS`.
- **Upstream amendment:** NO now.
- **Conditional dossier pulled forward:** not now.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-280 — Email result is unknown and future SMS fallback is permitted generally

- **Scenario:** policy says SMS is fallback, but email may have delivered.
- **Authority involved:** ambiguity + cross-channel policy.
- **Durable truths and owner:** email attempt unresolved.
- **Concurrency/retry/reordering/crash behaviour:** late email delivery.
- **Rejected models:** cross-channel fallback bypasses unknown-outcome guard.
- **Required invariant:** unknown blocks fallback unless the policy intentionally permits duplicate multi-channel delivery from the outset.
- **Recommended JIT shape:** reconciliation first for fallback policy.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** future multi-channel.
- **Verdict:** PASS PRINCIPLE.

## COMM-PT-281 — Future policy intentionally sends email + in-app for one security notice

- **Scenario:** both channels are intended, not failover.
- **Authority involved:** Communications fulfillment policy.
- **Durable truths and owner:** one logical notice can have two intended channel deliveries.
- **Concurrency/retry/reordering/crash behaviour:** either channel can deliver first/fail.
- **Rejected models:** cross-channel dedupe suppresses the second intended channel.
- **Required invariant:** policy distinguishes intentional multi-channel fulfillment from accidental duplicate.
- **Recommended JIT shape:** future multi-channel fulfillment semantics.
- **Conclusion:** `OPEN_HYPOTHESIS` mature capability.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO now.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-282 — Email delivered but future in-app notification has not yet been created

- **Scenario:** policy requires both channels.
- **Authority involved:** future fulfillment semantics.
- **Durable truths and owner:** email success does not necessarily satisfy `ALL_REQUIRED_CHANNELS`.
- **Concurrency/retry/reordering/crash behaviour:** in-app creation retries.
- **Rejected models:** one intent-level scalar `delivered` cannot express multi-channel policy.
- **Required invariant:** mature design must evaluate fulfillment policy without overwriting per-channel evidence.
- **Recommended JIT shape:** derive intent fulfillment from per-channel operations.
- **Conclusion:** `OPEN_HYPOTHESIS`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO now.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-283 — Future in-app notification is read on one device while another remains open

- **Scenario:** independent read/unread lifecycle appears.
- **Authority involved:** Communications in-app state.
- **Durable truths and owner:** read state cannot live only in LiveView.
- **Concurrency/retry/reordering/crash behaviour:** multi-device writes.
- **Rejected models:** use MessageIntent provider-delivered status as read state.
- **Required invariant:** read lifecycle is independently durable if capability exists.
- **Recommended JIT shape:** later `InAppNotification` concept likely justified.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO now.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-284 — Future inbox unread count cache disagrees with durable state

- **Scenario:** PubSub/cache lag.
- **Authority involved:** Communications in-app authority.
- **Durable truths and owner:** unread durable state wins.
- **Concurrency/retry/reordering/crash behaviour:** cache rebuild.
- **Rejected models:** unread cache is business authority.
- **Required invariant:** cache/projection rebuildable.
- **Recommended JIT shape:** later in-app JIT.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-285 — Future inbox item outlives the source action it referred to

- **Scenario:** verification completed but notification remains unread.
- **Authority involved:** source truth vs notification history.
- **Durable truths and owner:** inbox item cannot make obsolete action current.
- **Concurrency/retry/reordering/crash behaviour:** completion/read reorder.
- **Rejected models:** clicking old inbox item revives old proof.
- **Required invariant:** current source truth rechecked before action.
- **Recommended JIT shape:** notification is informational/navigation only.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO now.
- **Later executable proof:** future.
- **Verdict:** DEFER.

## COMM-PT-286 — Proposal adds InAppNotification to FP-001 “for architecture completeness”

- **Scenario:** mature Domain noun is copied into initial schema.
- **Authority involved:** FES + resource discipline.
- **Durable truths and owner:** no FP-001 independent inbox lifecycle is required.
- **Concurrency/retry/reordering/crash behaviour:** speculative only.
- **Rejected models:** prebuild unused Resource.
- **Required invariant:** Resources require current durable truth.
- **Recommended JIT shape:** reject.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** N/A.
- **Verdict:** PASS / REJECT RESOURCE.

## COMM-PT-287 — Requirement says “required work must never exist only in email”

- **Scenario:** someone concludes an in-app notification Resource is mandatory.
- **Authority involved:** Operating Model/FES work-vs-notification distinction.
- **Durable truths and owner:** required work lives with source Domain; email is delivery consequence.
- **Concurrency/retry/reordering/crash behaviour:** source state survives email failure.
- **Rejected models:** required work must be duplicated as inbox notification.
- **Required invariant:** source-owned durable work/status exists independently.
- **Recommended JIT shape:** Identity verification/recovery state + status UI.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** email outage while work remains recoverable.
- **Verdict:** PASS.

## COMM-PT-288 — Email queue is down but participant refreshes verification page

- **Scenario:** delivery executor unavailable.
- **Authority involved:** Identity source state + Communications projection.
- **Durable truths and owner:** verification remains pending; intent durable.
- **Concurrency/retry/reordering/crash behaviour:** queue/restart.
- **Rejected models:** UI claims “sent successfully” from stale toast; inbox item substitutes for actual delivery.
- **Required invariant:** honest pending/delayed status with resend/support path.
- **Recommended JIT shape:** durable intent/read projection.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** queue outage.
- **Verdict:** PASS.

## COMM-PT-289 — Participant repeatedly presses resend while provider is down

- **Scenario:** source resend semantics and provider backlog interact.
- **Authority involved:** Identity resend + Communications dedup.
- **Durable truths and owner:** Identity challenge supersession remains source authority.
- **Concurrency/retry/reordering/crash behaviour:** old/new intents in backlog.
- **Rejected models:** create multi-channel fallback automatically; provider outage changes resend semantics.
- **Required invariant:** newest source-valid intent survives; old intents stop; abuse limits remain separate.
- **Recommended JIT shape:** existing resend/source revalidation; no inbox requirement.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider outage + repeated resend.
- **Verdict:** PASS.

## COMM-PT-290 — Safe provider failover sends same protected bearer through provider B after A definitive non-delivery

- **Scenario:** same email proof may be retried through another trusted processor.
- **Authority involved:** protected delivery + OQ-036.
- **Durable truths and owner:** same MessageIntent/source proof remains valid.
- **Concurrency/retry/reordering/crash behaviour:** source may expire between attempts.
- **Rejected models:** provider switch automatically requires new Identity challenge; unlimited provider hopping.
- **Required invariant:** bounded retry, current source validity, minimal processor exposure, no ambiguity.
- **Recommended JIT shape:** same protected capability may serve bounded authorised retry; exact provider policy OQ-036.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** only if multi-provider selected.
- **Verdict:** PASS CONDITIONALLY.

## COMM-PT-291 — Same MessageIntent has provider-A then provider-B external ids

- **Scenario:** same-channel failover.
- **Authority involved:** DeliveryAttempt evidence.
- **Durable truths and owner:** each operation identity belongs to its attempt.
- **Concurrency/retry/reordering/crash behaviour:** callbacks may arrive later.
- **Rejected models:** one provider_id field on MessageIntent overwritten.
- **Required invariant:** historical attempt provenance retained.
- **Recommended JIT shape:** provider identity on DeliveryAttempt.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** failover if selected.
- **Verdict:** PASS.

## COMM-PT-292 — Provider offers batch API for 100 verification emails

- **Scenario:** throughput optimisation proposal.
- **Authority involved:** individual MessageIntent/DeliveryAttempt authority.
- **Durable truths and owner:** each recipient remains independent.
- **Concurrency/retry/reordering/crash behaviour:** batch response may be partial.
- **Rejected models:** one DeliveryAttempt for the whole batch; one status for 100 proofs.
- **Required invariant:** each participant operation independently attributable/reconcilable.
- **Recommended JIT shape:** do not use batching unless adapter maps per-recipient operation evidence.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** only if batching adopted later.
- **Verdict:** PASS.

## COMM-PT-293 — Provider batch partially accepts 70/100 and returns mixed outcomes

- **Scenario:** bulk API result.
- **Authority involved:** per-intent provider evidence.
- **Durable truths and owner:** outcomes differ.
- **Concurrency/retry/reordering/crash behaviour:** response loss may affect subset.
- **Rejected models:** batch success/failure scalar.
- **Required invariant:** per-recipient definitive/unknown classification.
- **Recommended JIT shape:** batch execution only if this evidence exists.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** future.
- **Verdict:** PASS PRINCIPLE.

## COMM-PT-294 — Batch response is lost after provider may have accepted all/part of batch

- **Scenario:** bulk ambiguity.
- **Authority involved:** provider ambiguity.
- **Durable truths and owner:** each included DeliveryAttempt may be unknown.
- **Concurrency/retry/reordering/crash behaviour:** callback/reconciliation later.
- **Rejected models:** resend full batch; mark all failed.
- **Required invariant:** no blind batch retry that multiplies messages.
- **Recommended JIT shape:** batching rejected unless per-operation idempotency/reconciliation supports safe handling.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** future.
- **Verdict:** PASS PRINCIPLE.

## COMM-PT-295 — Provider recovers from outage and thousands of pending verification intents are processed in pages

- **Scenario:** operational backlog fan-out.
- **Authority involved:** Communications delivery/recovery.
- **Durable truths and owner:** each intent already exists independently.
- **Concurrency/retry/reordering/crash behaviour:** batch selection/restarts.
- **Rejected models:** create CommunicationJourney/campaign to model recovery.
- **Required invariant:** pagination/bulk scheduling cannot change logical ownership/idempotency.
- **Recommended JIT shape:** bounded query/execution over MessageIntents.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** backlog recovery.
- **Verdict:** PASS.

## COMM-PT-296 — Proposal creates `Channel` table with rows email/SMS/WhatsApp/etc.

- **Scenario:** mature concept becomes mutable Resource.
- **Authority involved:** Product fixed vocabulary + resource discipline.
- **Durable truths and owner:** no independent FP-001 channel business lifecycle.
- **Concurrency/retry/reordering/crash behaviour:** N/A.
- **Rejected models:** database rows just to enumerate code-known channels.
- **Required invariant:** Resource existence requires durable business truth/lifecycle.
- **Recommended JIT shape:** closed type/config/adapter registry in code as needed.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** N/A.
- **Verdict:** PASS / REJECT RESOURCE.

## COMM-PT-297 — Proposal creates one universal provider adapter `send(channel, map)`

- **Scenario:** premature abstraction hides channel semantics.
- **Authority involved:** Architecture thin adapters + channel-specific rules.
- **Durable truths and owner:** email/SMS/WhatsApp semantics differ.
- **Concurrency/retry/reordering/crash behaviour:** error/callback normalization becomes ambiguous.
- **Rejected models:** untyped map/payload is lowest-common-denominator API.
- **Required invariant:** shared outcome semantics must not erase channel-specific constraints.
- **Recommended JIT shape:** typed channel ports/adapters with common normalized result concepts.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** implementation review.
- **Verdict:** PASS.

## COMM-PT-298 — Email adapter needs provider-specific callback/reconciliation capability not shared by future SMS adapter

- **Scenario:** adapters have asymmetric capabilities.
- **Authority involved:** provider-independent architecture.
- **Durable truths and owner:** business contract requires normalized evidence but not identical provider features.
- **Concurrency/retry/reordering/crash behaviour:** unknown outcomes.
- **Rejected models:** force every adapter to fake unsupported features; weaken email contract to future lowest common denominator.
- **Required invariant:** channel/provider capability is explicit; selected launch provider must meet required email contract.
- **Recommended JIT shape:** capability-specific adapter implementation behind stable business semantics.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider selected under OQ-036.
- **Verdict:** PASS.

## COMM-PT-299 — Future channel has different content constraints from email

- **Scenario:** SMS length or WhatsApp provider-approved template constraints differ.
- **Authority involved:** C&M + Communications channel provenance.
- **Durable truths and owner:** email template version is not automatically valid.
- **Concurrency/retry/reordering/crash behaviour:** channel fallback/change.
- **Rejected models:** render the same email HTML into every channel.
- **Required invariant:** exact content eligibility/binding is channel-aware.
- **Recommended JIT shape:** future channel-specific C&M binding; attempt records exact content/channel.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** not now.
- **Later executable proof:** future.
- **Verdict:** PASS PRINCIPLE.

## COMM-PT-300 — `OQ-036` remains unresolved when Communications JIT is otherwise ready to freeze

- **Scenario:** no email vendor/provider/channel operations policy has been selected yet.
- **Authority involved:** Roadmap gate classification + FP-001 Skeleton.
- **Durable truths and owner:** provider-independent Communications semantics are already frozen.
- **Concurrency/retry/reordering/crash behaviour:** covered by provider-independent contract.
- **Rejected models:** block Phase 7B/7C until vendor selection; select provider inside dossier to make it concrete; leave failure semantics undefined until provider appears.
- **Required invariant:** JIT freezes what provider must satisfy; release remains blocked until OQ-036 evidence proves a valid launch channel.
- **Recommended JIT shape:** final dossier explicitly lists OQ-036 as release-only implementation/operations gate.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** selected provider/channel proof before release.
- **Verdict:** PASS.

---

# 98. Rejected-model register additions — v0.8.0

125. **“Email + in-app first” means every FP-001 message must be delivered by both channels.** Rejected.
126. **FP-001 needs a durable in-app inbox because required work must not exist only in email.** Rejected; required work remains source-owned.
127. **Display verification bearer inside the app to bypass email delivery problems.** Rejected: breaks email-control meaning.
128. **Use in-app as the primary password-reset channel for signed-out participants.** Rejected.
129. **Replace old-address security notice with in-app notice.** Rejected.
130. **Source Domains choose provider/vendor names.** Rejected.
131. **MessageIntent snapshots provider at source-transition time.** Rejected unless a later provider-specific requirement proves it.
132. **Provider replacement requires a new MessageIntent.** Rejected.
133. **Unknown provider A outcome can be solved by sending through provider B.** Rejected.
134. **Provider acceptance delay justifies duplicate failover.** Rejected.
135. **Hard invalid-recipient bounce should trigger retries through multiple vendors.** Rejected.
136. **Provider dashboard/default config rewrites historical attempts.** Rejected.
137. **Dropping old-provider reconciliation when migrating vendors.** Rejected.
138. **Replaceable adapter means build active-active multi-provider routing now.** Rejected.
139. **One universal untyped `send(map)` API across email/SMS/WhatsApp/in-app.** Rejected.
140. **Create a `Channel` database Resource only to enumerate fixed channel names.** Rejected.
141. **Treat SMS and WhatsApp as one generic phone permission.** Rejected.
142. **Build native-push registrations/preferences in FP-001 for future-proofing.** Rejected.
143. **Any available channel may substitute for an email-verification proof.** Rejected.
144. **Phone number presence authorises SMS/WhatsApp recovery.** Rejected.
145. **Automatic “try all channels” fallback.** Rejected.
146. **Cross-channel unknown-outcome fallback bypasses reconciliation.** Rejected.
147. **One scalar intent `delivered` state is sufficient for future explicit multi-channel fulfillment.** Rejected as mature design assumption.
148. **Marketing provider suppression is equivalent to NewYou channel preference.** Rejected.
149. **Marketing unsubscribe may globally disable mandatory password-reset/security mail.** Rejected at platform authority level.
150. **Hard bounce automatically mutates canonical Account email.** Rejected.
151. **Same email content body is automatically valid for SMS/WhatsApp/in-app.** Rejected.
152. **One DeliveryAttempt for a provider batch of many recipients.** Rejected.
153. **Retry an ambiguous batch wholesale.** Rejected.
154. **Create CommunicationJourney to drain a provider-outage backlog.** Rejected.
155. **OQ-036 must be solved before the provider-independent Communications dossier can freeze.** Rejected by Roadmap/Skeleton classification.
156. **Choose the provider inside Communications JIT merely to make the contract concrete.** Rejected.

---

# 99. Upstream-delta register — v0.8.0

## Existing blockers remain

### `COMM-UPD-001`

**REQUIRED / unchanged.**

Correct certified Identity v0.1.3 wording that currently assigns message body/template ownership to Communications.

### `COMM-UPD-002`

**REQUIRED IDENTITY REVIEW / unchanged.**

Freeze scanner/prefetch-safe proof-consumption semantics or explicitly route them into the governed Identity proof contract.

## New upstream amendments from this channel cluster

**NONE.**

The apparent tension between:

- Product `email + in-app first`;
- Domain in-app capability;
- FES `in-app notification centre is not an FP-001 prerequisite`;
- Roadmap `OQ-036 BLOCKS_RELEASE_ONLY`

is reconcilable without amendment.

No Product, Architecture, Domain or Roadmap law needs changing.

---

# 100. Unresolved-gate register additions — v0.8.0

| Gate / open matter | v0.8.0 effect |
|---|---|
| `COMM-UPD-001` | Still blocks final Communications certification / Phase 7C freeze. |
| `COMM-UPD-002` | Still blocks final cross-domain freeze unless explicitly routed into governed Identity proof. |
| `OQ-036` launch email implementation | **Release-only gate.** Must select/prove a valid launch email implementation for verification/mandatory notices. |
| `OQ-036` in-app implementation | Product direction supports it, but FES means participant notification centre is not an FP-001 prerequisite. Exact launch/later in-app policy remains vendor/operations scope. |
| Provider count | One launch email provider is sufficient unless OQ-036 evidence justifies more. |
| Provider failover | Semantics frozen; actual provider-B availability/routing policy remains OQ-036. |
| Provider suppression model | Selected provider must prove mandatory-security delivery does not silently collapse into marketing unsubscribe semantics. |
| Protected-link rewriting/tracking | Selected provider must support the v0.7 non-tracking protected-link requirement; scanner-safe proof consumption remains Identity-owned. |
| Future SMS/WhatsApp | Not FP-001 blockers. Activation requires future provider/cost/consent/source semantics. |
| Future in-app inbox | Explicitly not FP-001 prerequisite. Independent lifecycle remains future JIT. |
| Multi-channel fulfillment | Not required now; exact semantics deferred until an active Product outcome needs them. |
| Provider batching | Not required. Any future use must preserve per-recipient attempt/reconciliation truth. |

---

# 101. Cross-stream dependency register additions — v0.8.0

| Stream / Domain | v0.8.0 finding |
|---|---|
| Identity & Access | Owns proof/channel meaning. Email verification cannot be replaced by unrelated channel possession. Future phone recovery needs Identity authority first. |
| Communications | Owns channel execution, provider selection, MessageIntent, DeliveryAttempt and provider evidence within source constraints. |
| Privacy & Consent | Future optional/multi-channel SMS/WhatsApp activation may require purpose/channel consent semantics. Required FP-001 security email does not pull Privacy forward. |
| Content & Media | Exact content binding is channel-aware; future channel bodies/templates may differ. No C&M dossier trigger now. |
| Audit & Evidence | Provider/channel operator controls remain under existing v0.7 bounded privileged evidence contract. |
| FES | In-app participant notification centre is eventual, not FP-001 prerequisite. Source/account status UI can expose required verification/recovery work. |
| Operating Model | Required work belongs in durable source state, not only email/toast/inbox projection. |
| OQ-036 | Owns selected launch provider/channel operations policy and later SMS/WhatsApp provider activation. |
| Provider adapters | Thin typed execution boundaries. Provider state/evidence never becomes source truth. |

---

# 102. Conditional-dossier adjudication — v0.8.0

## Privacy & Consent

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD` for current required FP-001.**

The required FP-001 path is mandatory/source-authorised security/account email.

This channel pass does not introduce optional SMS/WhatsApp marketing or accountless contact state.

**Future trigger:** activating optional SMS/WhatsApp or the v0.4 mailing-list branch may require Privacy JIT because channel/purpose permission semantics become implementation-grade.

## Content & Media

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD`.**

Current FP-001 needs email-specific exact governed content, already covered by v0.5.

Future SMS/WhatsApp/in-app channel variants do not force a dossier until one of those channels is actually selected for an active Feature Pack outcome with missing C&M semantics.

## Audit & Evidence

**Disposition unchanged: `CONDITIONAL / NOT PULLED FORWARD`.**

Provider failover/operator actions compose with the v0.7 minimum privileged-action evidence contract.

No new Audit-owned lifecycle appeared.

---

# 103. Later executable proof-obligation register additions — v0.8.0

149. Complete FP-001 registration/verification/recovery without an `InAppNotification` Resource or participant inbox.
150. Verification-pending UI reconstructs correctly after reconnect/restart from Identity + Communications state.
151. Signed-out password reset remains usable without in-app channel.
152. No endpoint/UI can use an in-app/session channel to satisfy email inbox verification.
153. Old-address email-change notice remains routed to the old-address snapshot even after canonical-email apply/session compromise.
154. Terminal email-delivery failure is participant-visible through source/account journey without requiring an inbox.
155. Source-domain APIs cannot select a provider/vendor.
156. Provider selection racing two workers creates one provider-bound DeliveryAttempt.
157. Switching default provider before first attempt changes only new attempt admission, not MessageIntent identity.
158. Known pre-call outage can select approved alternate provider without fabricating an attempt for the skipped provider.
159. Unknown provider-A outcome prevents provider-B failover.
160. Accepted/delayed provider-A operation prevents speculative duplicate through B.
161. Definitive provider-A non-submission can safely produce one B DeliveryAttempt when policy permits.
162. Hard invalid-recipient failure does not trigger provider-hop storm or mutate Identity email.
163. Provider-wide outage produces coordinated queue/degradation behaviour and uses alternate provider only if OQ-036 explicitly configured it.
164. Late old-provider callback after failover remains attributable to old DeliveryAttempt.
165. Physical duplicate across providers is detected/preserved truthfully rather than hidden.
166. Provider-A/B callback reordering cannot corrupt intent aggregate.
167. Identical external provider ids from different providers/accounts cannot collide internally.
168. Vendor migration preserves reconciliation for outstanding old-provider ambiguous attempts.
169. Credential/provider retirement cannot silently convert unknown old attempts into failed/successful.
170. Queued pre-migration MessageIntent can use newly approved provider if no old provider operation exists.
171. Selected provider's marketing unsubscribe/suppression configuration cannot silently suppress required password-reset/security delivery at platform-policy level.
172. Marketing unsubscribe provider callback cannot set a global application email-disabled state.
173. Verification hard bounce preserves `unverified` Identity truth and exposes safe change-email/recovery.
174. Provider complaint/suppression remains delivery evidence rather than Account/consent mutation.
175. Marketing email opt-out does not suppress password reset/security email.
176. No automatic SMS fallback occurs merely because a phone destination exists.
177. Future SMS and WhatsApp preferences/permissions remain distinct even for the same phone number.
178. No email-verification bearer is sent via SMS/WhatsApp/in-app as substitute proof.
179. Future cross-channel fallback, if introduced, is blocked while the previous channel outcome is unknown.
180. Explicit future dual-channel policy can distinguish intended second delivery from accidental duplicate.
181. Future in-app read/unread state, if introduced, remains independent of MessageIntent provider-delivery state.
182. Unread/inbox caches cannot become durable notification authority.
183. Stale future inbox item cannot resurrect completed/expired source work.
184. Required work survives email/queue failure independently of any in-app notification.
185. Repeated resend during provider outage supersedes/stops stale source intents correctly.
186. Same protected bearer across an approved same-channel provider retry remains bounded by source validity/retry lifetime.
187. Multiple provider operation ids remain attached to independent DeliveryAttempts under one MessageIntent.
188. Any provider batch implementation preserves independent per-recipient operation/outcome/unknown semantics.
189. Partial batch response maps independently to each included DeliveryAttempt.
190. Lost/ambiguous batch response cannot trigger blind whole-batch resend.
191. Outage backlog recovery uses bounded pagination/concurrency without creating campaign/journey authority.
192. No mutable `Channel` database Resource exists unless a later independent lifecycle proves it necessary.
193. Adapter interface remains typed enough that email/SMS/WhatsApp-specific constraints cannot be silently ignored.
194. Launch provider capability proof verifies callback/reconciliation/idempotency/suppression/link-tracking requirements under OQ-036.
195. Communications JIT remains executable/provider-independent when OQ-036 is still open; public/pilot release remains correctly blocked until OQ-036 closes.

---

# 104. Resource-discipline review — cumulative through v0.8.0

## `MessageIntent`

**REQUIRED.**

Channel pressure strengthens rather than weakens its role as the logical communication obligation independent of provider.

For current FP-001 it may carry/derive the required email channel constraint plus the existing role/locale/source/destination/content/protected-delivery provenance.

## `DeliveryAttempt`

**REQUIRED.**

v0.8.0 further proves that provider/channel execution belongs here:

- actual channel;
- actual provider/adapter identity;
- external operation id;
- exact content/locale provenance;
- provider evidence/reconciliation.

## `Channel`

**REQUIRED CONCEPT / NOT A RESOURCE.**

Product supplies a bounded channel vocabulary.

No independent durable FP-001 business lifecycle justifies a table/Resource.

## `InAppNotification`

**NOT REQUIRED for FP-001.**

FES is explicit.

A future inbox/read lifecycle is sufficient justification to introduce it later, not now.

## `SubscriberContact`

**Still not required for current FP-001.**

The v0.4 conditional mailing-list trigger remains the only current branch that justifies it.

## `NotificationPreference`

**Still not required as a current FP-001 Resource.**

Required security/account email is not optional preference-driven marketing.

Future multi-channel/optional messaging may justify the preference concept.

## `CommunicationJourney`

**Still not required.**

Provider outage recovery, retry batches and pagination do not create a campaign/journey lifecycle.

## `Provider`

**NOT a Communications business Resource at FP-001.**

Provider identity/configuration is execution/integration configuration plus DeliveryAttempt provenance.

A mutable provider catalogue/router Resource would be speculative.

## `ProviderRoute` / `ProviderFailoverPolicy`

**NOT justified as Resources.**

`OQ-036` may choose operational/configured policy.

Durable business truth remains MessageIntent/DeliveryAttempt.

## `ChannelDelivery`

**NOT justified as a third Resource.**

For the current single required email channel, DeliveryAttempt already owns physical channel/provider operations.

A future explicit multi-channel fulfillment model may revisit representation only if independent durable lifecycle demands it.

**Cumulative required FP-001 Communications Resource verdict remains:**

```text
MessageIntent
DeliveryAttempt
```

The model has now survived **300 cumulative pressure tests** without a third required FP-001 Communications business Resource.

---

# 105. Completeness / stabilisation assessment — v0.8.0

The broad channel/provider-independent scenario class is provisionally stable enough to stop expanding.

Major conclusions now converge:

```text
logical obligation
→ MessageIntent

physical provider/channel operation
→ DeliveryAttempt

channel vocabulary
→ bounded concept/config, not Resource

provider
→ replaceable thin adapter/config, not business authority

in-app inbox
→ future capability, explicitly not FP-001 prerequisite

SMS / WhatsApp / push
→ future activation seams, not current Resources

batch/backlog
→ execution shape, not CommunicationJourney
```

The two-Resource hypothesis has now survived **300 materially distinct pressure tests** across:

- atomic handoff;
- retries/ambiguity;
- proof invalidation;
- destination/email change;
- deletion/restore/merge;
- accountless contacts/preferences;
- consent;
- content/locale/rendering;
- provider outage/backlog;
- Audit/observability/operator security;
- channel/provider independence.

No new upstream law amendment emerged from v0.8.0.

Two known upstream corrections/clarifications remain:

1. `COMM-UPD-001` — correct Identity v0.1.3 content/template ownership wording.
2. `COMM-UPD-002` — scanner/prefetch-safe protected-link proof-consumption semantics.

## Stabilisation verdict

**BROAD DISCOVERY IS NOW NEAR STABILISATION, BUT NOT YET READY FOR GOVERNED DOSSIER DRAFTING.**

The next pass should no longer be another broad thematic expansion.

It should be a **combined adversarial stabilisation sweep** designed to falsify the accepted model by composing previously separate hazards:

- proof expiry + provider unknown + content withdrawal;
- resend + provider outage + language change;
- email change + old/new address + provider failover;
- Account closure/deletion + operator retry + late callback;
- duplicate-account merge + stale intent + content correction;
- preference/consent withdrawal + multi-channel future assumptions;
- restore + stale provider config + deleted participant;
- provider migration + old ambiguous attempts + credential rotation;
- Audit outage + operator recovery;
- callback flood + outage + backlog recovery;
- concurrent source invalidation + content invalidation + provider admission;
- terminal failure + participant resend + operator retry;
- protected capability lifetime + long outage + provider migration;
- scanner prefetch + resend/supersession;
- channel/provider failover + exact content provenance.

The stabilisation pass must ask one question repeatedly:

> Does this composed scenario require a new durable business truth, expose an unresolved upstream contradiction, invalidate an accepted invariant, or pull a conditional dossier forward?

If the answer continues to be no and cases reduce to the existing contracts, broad Communications Pre-JIT discovery should be declared stable and the working pack can be compressed into the requested final registers before drafting the governed JIT dossier.

---

# 106. v0.9.0 semantic delta — combined adversarial stabilisation sweep

This successor preserves all accepted v0.1.0–v0.8.0 findings and performs the first **cross-cluster falsification sweep**.

The live repository was rechecked immediately before this pass and remained pinned to:

`JCSchoeman96/NewYou@3f899e00ecfdfb9abc0794cffcb19eaff2726d58`

This is intentionally **not** another broad thematic expansion.

Every scenario combines multiple previously pressure-tested hazards and asks:

> Does the composition require a new durable business truth, expose an unresolved upstream contradiction, invalidate an accepted invariant, pull a conditional dossier forward, or materially change the required FP-001 Resource model?

The tested compositions include:

- source expiry + provider ambiguity + content withdrawal;
- source supersession + old ambiguous provider operation;
- resend + outage + language change;
- email-change cancellation/supersession + delayed provider evidence;
- deletion/closure + operator retry + late callback;
- duplicate-account merge + stale communication work;
- restore + stale provider configuration + current deletion;
- provider migration + unresolved old-provider operations;
- content correction + provider failover;
- preference/consent changes + future channel assumptions;
- callback flood + provider outage + backlog recovery;
- Audit outage + operator recovery;
- simultaneous source/content/provider cutovers;
- terminal failure + participant resend + operator retry;
- protected-capability expiry + long outage;
- scanner prefetch + resend/supersession;
- queue uniqueness/idempotency + new logical intent;
- batch recovery with mixed source/content validity.

No new provider, channel, package, schema, queue, backoff value or Phase-8 proof classification is selected.

---

# 107. Cross-cluster admission theorem — v0.9.0

A **new provider submission** for an existing logical `MessageIntent` is authorised only if all currently applicable owner predicates are true.

Conceptually:

```text
CURRENT SOURCE AUTHORITY
AND CURRENT PROTECTED-CAPABILITY AUTHORITY where required
AND CURRENT DESTINATION / SOURCE-SNAPSHOT AUTHORITY
AND CURRENT PURPOSE / PREFERENCE / MANDATORY POLICY
AND CURRENT C&M CONTENT ELIGIBILITY
AND NO UNRESOLVED PREVIOUS OPERATION THAT FORBIDS A NEW SUBMISSION
AND CURRENT RETRY / MANUAL-RECOVERY BUDGET
AND CURRENT CHANNEL / PROVIDER EXECUTION ADMISSION
→ MAY CREATE / EXECUTE NEXT DeliveryAttempt
```

Important properties:

1. these predicates remain independently owned;
2. no one scalar status becomes the authority for all of them;
3. worker/job/provider state cannot substitute for an owner predicate;
4. a failed predicate suppresses **new provider egress**, not necessarily historical reconciliation;
5. source invalidation can end future retry while an already-started provider operation remains unresolved historical evidence;
6. a **new superseding source obligation** is a new logical `MessageIntent` and is not the same as retry/failover of the old intent.

This theorem is a synthesis of existing accepted invariants. It does not create a new Domain or shared-write authority.

---

# 108. Accepted working-design register additions — v0.9.0

## COMM-WD-188 — Provider-attempt admission is conjunctive across independent authorities

**Status:** `WORKING_DESIGN_ACCEPTED`

A worker/operator does not ask “is MessageIntent sendable?” from one cached scalar.

It composes the currently applicable owner predicates in §107.

This avoids a state-explosion anti-pattern where source proof, content publication, permission, destination, provider ambiguity and retry budget are collapsed into one pseudo-authoritative status enum.

## COMM-WD-189 — Unknown outcome blocks retry/failover of the same logical intent, not a genuinely new superseding source obligation

**Status:** `WORKING_DESIGN_ACCEPTED`

Example:

```text
old verification challenge / old MessageIntent
→ provider outcome UNKNOWN

participant requests allowed resend
→ Identity supersedes old challenge
→ new challenge
→ new MessageIntent
```

The old unknown operation remains reconcilable, but it cannot prevent the new source-owned obligation from proceeding merely because both target the same mailbox.

If the old email later arrives, its old proof is invalid.

This is not blind duplicate retry of one logical message.

## COMM-WD-190 — Source terminalisation ends future protected delivery even when an old provider operation remains unresolved

**Status:** `WORKING_DESIGN_ACCEPTED`

If the underlying proof becomes:

- expired;
- consumed;
- revoked;
- superseded;
- otherwise source-terminal,

then:

- no further DeliveryAttempt may begin for that intent;
- protected bearer capability is no longer retained for future delivery;
- existing unknown/in-flight provider operation may still be reconciled as historical evidence;
- late physical delivery cannot revive the proof.

Provider ambiguity does not extend proof lifetime.

## COMM-WD-191 — Historical reconciliation survives source invalidation without restoring send authority

**Status:** `WORKING_DESIGN_ACCEPTED`

A source-invalid intent may still receive:

- a late authenticated provider callback;
- provider lookup evidence;
- operator reconciliation evidence.

That can improve historical delivery truth.

It cannot:

- authorise retry;
- restore protected capability;
- reopen Identity proof;
- recreate deleted Account/contact authority.

## COMM-WD-192 — Supersession creates a new logical communication; old intent is never morphed into the successor

**Status:** `UPSTREAM_DERIVED` plus cumulative specialisation

Resend/new email-change request/new proof issuance remains a source lifecycle event.

The old Communications record stays bound to:

- old source proof;
- old destination snapshot;
- old intended locale;
- old content/attempt history.

The successor gets a new `MessageIntent`.

No in-place rewrite turns old evidence into the new obligation.

## COMM-WD-193 — Composed failure does not justify a workflow/orchestration Resource

**Status:** `WORKING_DESIGN_ACCEPTED`

A case involving:

```text
source invalidation
+ content withdrawal
+ provider unknown
+ operator reconciliation
```

still consists of owner states plus `MessageIntent` / `DeliveryAttempt`.

It does not by itself create durable independent truth called:

- DeliveryCase;
- RecoveryWorkflow;
- CommunicationIncident;
- ProviderReconciliationCase;
- OrchestrationState.

A new Resource still requires its own durable business lifecycle.

## COMM-WD-194 — Reconciliation may continue after deletion/closure only under the lawful historical-evidence boundary

**Status:** `WORKING_DESIGN_ACCEPTED`

When deletion/closure ends active communication authority:

- no new provider operation begins;
- no protected bearer is retained for future send;
- late provider evidence may be consumed only to the extent allowed by the current data-lifecycle contract;
- retained evidence cannot reconstruct an active participant/contact relationship.

Exact retention duration remains `OQ-029`.

## COMM-WD-195 — Automatic and privileged manual sends use the same business admission predicates

**Status:** `WORKING_DESIGN_ACCEPTED`

Operator privilege changes:

- who may request the action;
- required assurance/grant;
- required reason/audit evidence.

It does not bypass:

- source validity;
- protected-capability validity;
- content eligibility;
- purpose/channel rules;
- previous-operation ambiguity;
- destination semantics;
- deletion/closure;
- retry/manual-recovery budget.

## COMM-WD-196 — Restore/restart suppresses provider egress until current owner truth and current integration admission are re-established

**Status:** `UPSTREAM_DERIVED` plus cumulative integration

A restored/stale record is never assumed sendable because it was sendable at backup time.

Before new provider egress, current:

- source state;
- deletion/merge state;
- content eligibility;
- permission/preference;
- provider/channel configuration;
- previous attempt ambiguity

must be re-established.

## COMM-WD-197 — Provider migration never transfers an unresolved external operation to the new provider

**Status:** `WORKING_DESIGN_ACCEPTED`

Provider A's unknown operation remains provider A evidence.

Migrating defaults to provider B affects:

- new intents;
- or later safely admitted new attempts.

It does not reinterpret A's unknown operation as a B operation or silently close it.

## COMM-WD-198 — Simultaneous owner invalidations require executable cutover proof, not a new coordinating authority

**Status:** `WORKING_DESIGN_ACCEPTED`

Races such as:

```text
Identity proof invalidates
C&M content withdraws
Communications worker admits provider attempt
```

must be proven safe at the attempt-admission cutover.

The required property is:

- if invalidation wins before admission, no provider call;
- if a provider operation lawfully begins first, later invalidation prevents future attempts and makes late delivery harmless to source truth.

The exact PostgreSQL/Ash transaction/locking/conditional-write mechanism is downstream JIT/proof detail.

## COMM-WD-199 — The three conditional FP-001 dossiers remain unpulled after composed-case testing

**Status:** `WORKING_DESIGN_ACCEPTED`

The combined scenarios did not expose missing implementation-grade owner semantics for the **required current FP-001 path** that force:

- Privacy & Consent;
- Content & Media;
- Audit & Evidence

into separate dossiers.

Previously identified conditional triggers remain conditional:

- public/accountless mailing-list activation can pull Privacy forward;
- materially new message-content lifecycle can pull C&M forward;
- materially new central evidence/access/retention lifecycle can pull Audit forward.

None is activated by the composed FP-001 security/account flow.

## COMM-WD-200 — Broad Communications Pre-JIT discovery is stable enough to stop ordinary scenario expansion

**Status:** `WORKING_DESIGN_ACCEPTED`

After this falsification sweep:

- no third required Communications business Resource emerged;
- no accepted core invariant was overturned;
- no additional higher-authority contradiction was found;
- no conditional dossier became mandatory;
- unresolved exact mechanisms cleanly route to JIT/proof/OQ gates;
- new scenarios increasingly reduce to existing owner predicates rather than producing new design law.

Therefore ordinary broad Grill-Me expansion should now stop unless there is:

- new repository authority;
- changed FP-001 scope;
- a contradiction discovered during consolidation/JIT drafting;
- implementation evidence that falsifies a working assumption;
- or resolution of an upstream blocker that materially changes the seam.

---

# 109. Combined adversarial pressure-test register

## COMM-PT-301 — Proof expires while provider outcome is unknown and bound content is withdrawn

- **Scenario:** provider may have accepted v1; before resolution, Identity proof expires and C&M withdraws v1.
- **Authority involved:** Identity proof; C&M eligibility; Communications provider ambiguity.
- **Durable truths and owner:** old DeliveryAttempt remains Communications historical evidence; proof terminal = Identity; content ineligible = C&M.
- **Concurrency/retry/reordering/crash behaviour:** late provider callback may report accepted/delivered after both invalidations.
- **Rejected models:** retry corrected content; extend proof until reconciliation; keep bearer solely because provider status is unknown.
- **Required invariant:** no new send; protected capability ends with proof authority; reconcile old operation historically.
- **Recommended JIT shape:** source-terminal intent + unresolved/historical attempt evidence.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** expiry + withdrawal + timeout + late delivery.
- **Verdict:** PASS.

## COMM-PT-302 — Proof is consumed from the first delivery while provider status remains unknown and content is later corrected

- **Scenario:** participant successfully verifies using the message even though provider callback never resolved.
- **Authority involved:** Identity proof consumption; Communications evidence; C&M correction.
- **Durable truths and owner:** Identity consumed truth wins; provider status stays historically unresolved/reconcilable.
- **Concurrency/retry/reordering/crash behaviour:** correction/reconciliation arrive later.
- **Rejected models:** resend because Communications still says unknown; mutate verification from provider evidence.
- **Required invariant:** consumed proof terminates delivery obligation; content correction cannot cause retry of completed source obligation.
- **Recommended JIT shape:** stop egress, reconcile evidence only.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** proof consume precedes late callback/correction.
- **Verdict:** PASS.

## COMM-PT-303 — Provider outage + participant language change + allowed resend

- **Scenario:** Afrikaans verification intent is queued during outage; participant changes preference to English and requests resend.
- **Authority involved:** Identity resend/supersession; Communications locale; provider outage.
- **Durable truths and owner:** old challenge/intent remains Afrikaans and is superseded; new challenge/intent may be English.
- **Concurrency/retry/reordering/crash behaviour:** outage recovery sees both records.
- **Rejected models:** mutate old intent locale; send both because both are queued; make outage freeze resend semantics.
- **Required invariant:** old source-invalid intent self-suppresses; new intent is independently eligible.
- **Recommended JIT shape:** source-validity-first backlog recovery.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** outage recovery with old/new locale intents.
- **Verdict:** PASS.

## COMM-PT-304 — Old verification provider operation is unknown when participant requests resend

- **Scenario:** old token may be physically delivered later; Identity issues/supersedes a new challenge.
- **Authority involved:** Identity resend; Communications ambiguity.
- **Durable truths and owner:** old attempt stays unknown; old proof becomes invalid; new MessageIntent is a new logical obligation.
- **Concurrency/retry/reordering/crash behaviour:** old and new provider operations may physically arrive out of order.
- **Rejected models:** old unknown blocks new resend forever; resend is treated as same-intent retry.
- **Required invariant:** old proof cannot succeed after supersession; new intent may proceed under current guards.
- **Recommended JIT shape:** implement `COMM-WD-189`.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** old unknown + new resend + old-late delivery.
- **Verdict:** PASS.

## COMM-PT-305 — New-address email-change confirmation is unknown when participant cancels/supersedes the change

- **Scenario:** provider operation may still deliver the confirmation email after cancellation.
- **Authority involved:** Identity email-change source state; Communications attempt.
- **Durable truths and owner:** Identity cancellation/supersession invalidates old challenge/change; attempt remains evidence.
- **Concurrency/retry/reordering/crash behaviour:** late old email/callback after cancellation.
- **Rejected models:** cancel provider evidence by rewriting attempt; confirmation click can still apply old change.
- **Required invariant:** late old proof cannot change Identity; no retry of cancelled source obligation.
- **Recommended JIT shape:** source terminal + historical reconciliation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** cancellation before/after provider acceptance.
- **Verdict:** PASS.

## COMM-PT-306 — Email change applies while old-address notice is still backlogged during provider outage

- **Scenario:** canonical new email is already active; old-address notice has not sent.
- **Authority involved:** Identity email-change truth; Communications old-address destination snapshot.
- **Durable truths and owner:** notice obligation remains bound to old-address event provenance where source policy requires it.
- **Concurrency/retry/reordering/crash behaviour:** outage recovers after sessions/canonical address change.
- **Rejected models:** re-resolve destination to new canonical email; drop notice because change already applied.
- **Required invariant:** event-correct old-address notice remains independently deliverable.
- **Recommended JIT shape:** durable source/destination snapshot + current source consequence state.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** apply → outage → later old-address send.
- **Verdict:** PASS.

## COMM-PT-307 — Account deletion begins while a protected DeliveryAttempt is unknown

- **Scenario:** provider may have message; deletion removes active Account communication authority.
- **Authority involved:** Identity/deletion owner; Communications historical evidence; Privacy retention.
- **Durable truths and owner:** no new send; old operation may be reconciled only as lawfully retained evidence.
- **Concurrency/retry/reordering/crash behaviour:** late callback after deletion.
- **Rejected models:** keep bearer to retry after deletion; provider callback recreates Account/contact; blind delete attempt evidence before required reconciliation/retention rules.
- **Required invariant:** active authority ends; retained evidence stays non-authoritative.
- **Recommended JIT shape:** deletion suppression + bounded historical reconciliation.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** deletion + timeout + late callback.
- **Verdict:** PASS.

## COMM-PT-308 — Operator manual retry races Account deletion while central Audit is unavailable

- **Scenario:** staff tries to recover a terminal message as deletion closes the Account and Audit evidence cannot be established.
- **Authority involved:** deletion; Communications operator action; Audit.
- **Durable truths and owner:** deletion/source authority and required Audit both gate the action.
- **Concurrency/retry/reordering/crash behaviour:** race across nodes/services.
- **Rejected models:** privileged override; send first then audit later; deletion waits on operator UI.
- **Required invariant:** retry fails closed and produces no provider operation.
- **Recommended JIT shape:** same business admission + required privileged Audit establishment.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** deletion/Audit outage/operator race.
- **Verdict:** PASS.

## COMM-PT-309 — Duplicate-account merge occurs while both accounts have stale/pending security MessageIntents

- **Scenario:** Identity merges/reconciles Accounts with independent prior communication history.
- **Authority involved:** Identity merge authority; Communications source references.
- **Durable truths and owner:** merge semantics decide which source obligations remain valid.
- **Concurrency/retry/reordering/crash behaviour:** workers wake against pre-merge ids.
- **Rejected models:** Communications moves/rewrites all intents to surviving Account; merge itself authorises resend.
- **Required invariant:** every future attempt revalidates source obligation; historical records retain original provenance.
- **Recommended JIT shape:** nonsecret source ref + current owner validation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** merge + stale queued work.
- **Verdict:** PASS.

## COMM-PT-310 — Merge completes while an old-account provider operation is unknown

- **Scenario:** provider callback arrives after Identity merge.
- **Authority involved:** Identity merge; Communications evidence.
- **Durable truths and owner:** old attempt remains tied to original source provenance.
- **Concurrency/retry/reordering/crash behaviour:** callback after merge/restart.
- **Rejected models:** rewrite old attempt to surviving Account; discard callback as orphan.
- **Required invariant:** reconcile historical attempt without creating surviving-Account send/source authority.
- **Recommended JIT shape:** immutable causal provenance + owner resolution.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** late callback after merge.
- **Verdict:** PASS.

## COMM-PT-311 — Restore from old backup resurrects queued intent after current deletion and provider migration

- **Scenario:** backup predates deletion and still references provider A while live policy uses B.
- **Authority involved:** restore doctrine; deletion; Communications/provider config.
- **Durable truths and owner:** restored record is stale evidence, not current send authority.
- **Concurrency/retry/reordering/crash behaviour:** workers may start before reconciliation if not suppressed.
- **Rejected models:** immediately drain restored queue; use stale provider A config; recreated Account/contact authority.
- **Required invariant:** restore suppression prevents egress until current owner truth/config reconciles.
- **Recommended JIT shape:** restart/restore gate from `COMM-WD-196`.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** pre-deletion backup restore.
- **Verdict:** PASS.

## COMM-PT-312 — Long provider outage outlives protected capability/proof lifetime

- **Scenario:** queue survives longer than token/protected retry window.
- **Authority involved:** Identity proof lifetime; protected-delivery seam; Communications outage recovery.
- **Durable truths and owner:** source expires; intent cannot deliver protected proof afterward.
- **Concurrency/retry/reordering/crash behaviour:** provider recovers after expiry.
- **Rejected models:** extend proof/capability because outage was external; reconstruct token; send stale link.
- **Required invariant:** no provider egress after source/capability terminal; participant must obtain new source obligation.
- **Recommended JIT shape:** source-first backlog eligibility.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** outage > proof TTL.
- **Verdict:** PASS.

## COMM-PT-313 — Provider migration during outage: some intents never attempted, some provider-A attempts unknown

- **Scenario:** system switches default to B during recovery.
- **Authority involved:** provider migration; ambiguity; Communications.
- **Durable truths and owner:** no-attempt intents may use current approved B; unknown A attempts remain A reconciliation obligations.
- **Concurrency/retry/reordering/crash behaviour:** mixed backlog processed together.
- **Rejected models:** resend all through B; freeze all new work because some A operations are unknown.
- **Required invariant:** admission is per intent/attempt state, not provider-wide scalar.
- **Recommended JIT shape:** bounded per-record recovery.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** mixed backlog migration.
- **Verdict:** PASS.

## COMM-PT-314 — Provider-A credential rotation removes lookup access while unknown A attempts remain

- **Scenario:** A callbacks may still arrive but active API lookup is unavailable.
- **Authority involved:** OQ-036 operational migration; Communications ambiguity.
- **Durable truths and owner:** unknown remains unknown until valid evidence or bounded closeout policy.
- **Concurrency/retry/reordering/crash behaviour:** callbacks delayed/lost.
- **Rejected models:** credential loss means failed; resend via B automatically.
- **Required invariant:** provider retirement cannot fabricate certainty.
- **Recommended JIT shape:** migration/runbook must account for outstanding ambiguity.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** provider retirement procedure.
- **Verdict:** PASS / OQ-036 OPERATIONS.

## COMM-PT-315 — Content v1 withdrawn after provider-A definitive non-delivery; v2 successor exists and provider B is now default

- **Scenario:** retry requires both content correction and provider switch.
- **Authority involved:** C&M successor; Communications retry/provider policy; source validity.
- **Durable truths and owner:** original attempt remains v1/A; new attempt may be v2/B.
- **Concurrency/retry/reordering/crash behaviour:** source may invalidate during rebind/failover.
- **Rejected models:** one mutable attempt rewritten A/v1→B/v2; new MessageIntent solely for implementation change.
- **Required invariant:** explicit safe rebind then new DeliveryAttempt after current guards.
- **Recommended JIT shape:** same MessageIntent, preserved attempt provenance.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** rebind + provider switch race.
- **Verdict:** PASS.

## COMM-PT-316 — Content v1 withdrawn while provider-A attempt is unknown and provider B is healthy

- **Scenario:** corrected v2 exists.
- **Authority involved:** C&M + provider ambiguity.
- **Durable truths and owner:** old A operation may deliver v1.
- **Concurrency/retry/reordering/crash behaviour:** late A evidence.
- **Rejected models:** rebind to v2 and send B immediately.
- **Required invariant:** ambiguity wins against same-intent rebind/failover; reconcile A first.
- **Recommended JIT shape:** content blocked + reconciliation required.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** v1 withdrawal + A timeout + B availability.
- **Verdict:** PASS.

## COMM-PT-317 — Language changes after a definitive failed attempt and before same-intent provider failover

- **Scenario:** old intent was Afrikaans; Account preference is now English.
- **Authority involved:** intent locale stability; provider failover.
- **Durable truths and owner:** same intent remains Afrikaans.
- **Concurrency/retry/reordering/crash behaviour:** participant may separately request resend.
- **Rejected models:** provider switch re-resolves locale from current Account.
- **Required invariant:** infrastructure retry/failover does not change logical intent locale.
- **Recommended JIT shape:** failover uses original locale/content binding or explicit safe successor in same locale.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** language change + provider retry.
- **Verdict:** PASS.

## COMM-PT-318 — Canonical email changes while an older password-recovery intent is queued

- **Scenario:** destination/business state changed after intent creation.
- **Authority involved:** Identity source challenge/destination authority.
- **Durable truths and owner:** Communications cannot decide whether old recovery proof remains valid merely from current Account.email.
- **Concurrency/retry/reordering/crash behaviour:** old worker wakes after email change.
- **Rejected models:** silently retarget old intent to new canonical email; always send old destination without source revalidation.
- **Required invariant:** source-owner validity contract determines whether old recovery obligation survives; destination never silently substitutes.
- **Recommended JIT shape:** re-read Identity source validity before send.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO; current Identity source lifecycle remains owner.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** email-change/recovery race.
- **Verdict:** PASS.

## COMM-PT-319 — Optional communication loses permission while future multi-channel fallback is being considered

- **Scenario:** email failed definitively; before SMS fallback, purpose/channel permission is withdrawn.
- **Authority involved:** Privacy purpose + Communications preference + future fallback.
- **Durable truths and owner:** withdrawn current permission blocks new optional attempt.
- **Concurrency/retry/reordering/crash behaviour:** fallback worker already queued.
- **Rejected models:** original intent creation permanently authorises fallback.
- **Required invariant:** current optional permission re-evaluated before each new channel/provider operation.
- **Recommended JIT shape:** future admission theorem.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO for current FP-001; future optional channel activation may.
- **Later executable proof:** future.
- **Verdict:** PASS PRINCIPLE.

## COMM-PT-320 — Accountless marketing contact links to Account while permission is withdrawn and message remains queued

- **Scenario:** conditional v0.4 branch combined with linkage and retry.
- **Authority involved:** Privacy purpose; Communications SubscriberContact/preference; Account linkage.
- **Durable truths and owner:** linking cannot restore/broaden permission.
- **Concurrency/retry/reordering/crash behaviour:** worker sees changed linkage.
- **Rejected models:** Account's settings replace old permission automatically; queue admission predates withdrawal so send anyway.
- **Required invariant:** current purpose permission suppresses optional send.
- **Recommended JIT shape:** same v0.4 conditional branch.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** **Privacy only if this branch is actually activated.**
- **Later executable proof:** future branch.
- **Verdict:** PASS / CONDITIONAL UNCHANGED.

## COMM-PT-321 — Invalid-callback flood occurs during provider outage while backlog is recovering

- **Scenario:** dependency recovery and hostile/misconfigured ingress coincide.
- **Authority involved:** provider authentication; Communications backlog; security observability.
- **Durable truths and owner:** invalid callbacks are not business facts; backlog intents remain independent.
- **Concurrency/retry/reordering/crash behaviour:** load amplification risk.
- **Rejected models:** central Audit event per invalid callback; callback flood pauses/terminalises every intent as business truth.
- **Required invariant:** authenticate before mutation, rate/aggregate hostile telemetry, bounded provider recovery.
- **Recommended JIT shape:** failure-isolated ingress and executor controls.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** combined callback flood + backlog.
- **Verdict:** PASS.

## COMM-PT-322 — Valid late callback reports delivery after proof has expired

- **Scenario:** physical delivery occurred but source proof is no longer usable.
- **Authority involved:** provider evidence vs Identity proof.
- **Durable truths and owner:** DeliveryAttempt may become delivered historically; proof stays expired.
- **Concurrency/retry/reordering/crash behaviour:** callback after cleanup.
- **Rejected models:** delivered restores proof/retry; ignore truthful callback because source ended.
- **Required invariant:** evidence updates only its own dimension.
- **Recommended JIT shape:** historical reconciliation without source mutation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** expiry then delivered callback.
- **Verdict:** PASS.

## COMM-PT-323 — Valid late callback arrives after participant deletion

- **Scenario:** provider reports delivered/bounced for an old operation.
- **Authority involved:** Privacy deletion/retention + Communications evidence.
- **Durable truths and owner:** callback processing must respect current lawful retention/minimisation.
- **Concurrency/retry/reordering/crash behaviour:** deleted business references may be unavailable.
- **Rejected models:** recreate participant/contact solely to attach callback; drop authenticated material evidence without retention rule.
- **Required invariant:** consume only bounded lawful historical evidence; never resurrect active authority.
- **Recommended JIT shape:** tombstone/minimal-reference capable evidence path as required by data-lifecycle JIT.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** deletion + late callback under OQ-029 policy.
- **Verdict:** PASS.

## COMM-PT-324 — Audit outage overlaps automatic callback processing and manual retry request

- **Scenario:** valid provider callback and privileged operator command happen concurrently.
- **Authority involved:** Communications callback; Audit privileged evidence.
- **Durable truths and owner:** automatic callback need not wait for Audit; manual provider-mutating action does.
- **Concurrency/retry/reordering/crash behaviour:** callback may resolve state that operator viewed as terminal.
- **Rejected models:** block callback on Audit; allow manual retry unaudited.
- **Required invariant:** callback commits; manual action fails/revalidates.
- **Recommended JIT shape:** separate consequence paths.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** combined outage/race.
- **Verdict:** PASS.

## COMM-PT-325 — Operator manual retry races participant resend/supersession

- **Scenario:** staff acts on old terminal intent just as participant requests new proof.
- **Authority involved:** Identity supersession; Communications operator retry; Audit.
- **Durable truths and owner:** new source invalidates old source obligation.
- **Concurrency/retry/reordering/crash behaviour:** operator command may have been authorised against stale UI.
- **Rejected models:** staff privilege lets old intent send; both operations use same logical key.
- **Required invariant:** current source revalidation makes old operator retry lose if supersession wins.
- **Recommended JIT shape:** revision/source guard immediately before attempt admission.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** resend/manual retry interleavings.
- **Verdict:** PASS.

## COMM-PT-326 — Operator reconciliation of old unknown attempt occurs after participant resend

- **Scenario:** old source has been superseded but historical ambiguity remains.
- **Authority involved:** Communications reconciliation; Identity source.
- **Durable truths and owner:** reconciliation is still allowed; new send is not.
- **Concurrency/retry/reordering/crash behaviour:** old callback/new attempt may overlap.
- **Rejected models:** source supersession deletes old evidence; reconciliation result can revive old delivery obligation.
- **Required invariant:** old attempt may resolve historically while old intent stays non-sendable.
- **Recommended JIT shape:** `COMM-WD-191`.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** old reconcile + new intent.
- **Verdict:** PASS.

## COMM-PT-327 — Automated terminal failure + participant resend + stale operator manual-recovery command

- **Scenario:** three recovery paths overlap.
- **Authority involved:** Communications terminal state; Identity resend; operator policy.
- **Durable truths and owner:** participant resend creates new source obligation; old manual command must not send stale proof.
- **Concurrency/retry/reordering/crash behaviour:** duplicate UI/actions.
- **Rejected models:** terminal failure creates a permanent manual-send right.
- **Required invariant:** old operator action revalidates source and loses after supersession.
- **Recommended JIT shape:** current owner checks on all recovery paths.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** three-way race.
- **Verdict:** PASS.

## COMM-PT-328 — Provider batch recovery includes mixed expired proofs, valid proofs and withdrawn content versions

- **Scenario:** outage recovery selects many intents at once.
- **Authority involved:** Identity, C&M, Communications batching.
- **Durable truths and owner:** eligibility differs per intent.
- **Concurrency/retry/reordering/crash behaviour:** batch list becomes stale while processing.
- **Rejected models:** batch-level “eligible” flag; create campaign/journey to own recovery.
- **Required invariant:** per-intent current admission before provider operation.
- **Recommended JIT shape:** bounded pagination + individual attempt admission.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** mixed-validity backlog batch.
- **Verdict:** PASS.

## COMM-PT-329 — Oban uniqueness accidentally coalesces old superseded intent and new resend intent

- **Scenario:** both share destination/purpose but have different source challenges.
- **Authority involved:** business idempotency vs infrastructure uniqueness.
- **Durable truths and owner:** they are distinct logical obligations because source challenge changed.
- **Concurrency/retry/reordering/crash behaviour:** new job may be discarded by coarse uniqueness.
- **Rejected models:** uniqueness key = email + purpose; Oban uniqueness defines logical message identity.
- **Required invariant:** infrastructure dedupe cannot suppress a new valid source obligation.
- **Recommended JIT shape:** business MessageIntent established first; queue uniqueness scoped only as safe optimisation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** coarse uniqueness regression test.
- **Verdict:** PASS.

## COMM-PT-330 — Business idempotency key is reused across a new challenge because destination/purpose are unchanged

- **Scenario:** resend generates new challenge but implementation key does not include source logical identity.
- **Authority involved:** MessageIntent dedup identity; Identity source.
- **Durable truths and owner:** new challenge = new logical intent.
- **Concurrency/retry/reordering/crash behaviour:** new row/action may dedupe to stale one.
- **Rejected models:** idempotency key based only on `account/email + purpose`.
- **Required invariant:** business idempotency identifies the source obligation, not just channel/destination/category.
- **Recommended JIT shape:** stable source-obligation identity participates in logical-key contract.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** new challenge cannot collapse into old intent.
- **Verdict:** PASS.

## COMM-PT-331 — Two workers race content successor rebind and provider failover

- **Scenario:** v1/A definitively failed; v2/B is allowed; two nodes recover simultaneously.
- **Authority involved:** Communications binding/retry concurrency; C&M.
- **Durable truths and owner:** one current binding and one next provider operation may win.
- **Concurrency/retry/reordering/crash behaviour:** double B attempt risk.
- **Rejected models:** content rebind and provider attempt are independent uncontrolled writes; Oban uniqueness alone.
- **Required invariant:** concurrency-safe current intent revision/attempt admission yields at most one new operation.
- **Recommended JIT shape:** conditional write/transaction boundary in JIT.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** two-node recovery race.
- **Verdict:** PASS.

## COMM-PT-332 — Identity invalidation, C&M withdrawal and provider-attempt admission happen concurrently

- **Scenario:** three independent owners change around the cutover.
- **Authority involved:** Identity, C&M, Communications.
- **Durable truths and owner:** no shared-write owner is introduced.
- **Concurrency/retry/reordering/crash behaviour:** all interleavings matter.
- **Rejected models:** central orchestrator Resource owns combined state; stale pre-check with provider call much later.
- **Required invariant:** attempt admission proves a safe current-authority cutover; losing invalidation blocks call, winning call becomes historical external effect only.
- **Recommended JIT shape:** executable concurrency proof; exact DB mechanism downstream.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** exhaustive interleavings around provider-call boundary.
- **Verdict:** PASS / HIGH-PRIORITY PROOF.

## COMM-PT-333 — Content correction arrives after provider acceptance while proof is consumed before delivery callback

- **Scenario:** external operation exists; participant used it; message content later corrected.
- **Authority involved:** C&M correction; Identity consumption; Communications evidence.
- **Durable truths and owner:** source obligation is complete; historical attempt remains old content version.
- **Concurrency/retry/reordering/crash behaviour:** late delivery/correction evidence.
- **Rejected models:** send corrected version as retry of consumed proof; rewrite historical content version.
- **Required invariant:** no same-intent resend; remediation only if separately required by correction policy.
- **Recommended JIT shape:** historical provenance + optional new remediation obligation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** accepted → consumed → correction → callback.
- **Verdict:** PASS.

## COMM-PT-334 — Mail scanner prefetches old verification URL, then participant requests resend/supersession

- **Scenario:** scanner touches old bearer before new challenge exists.
- **Authority involved:** `COMM-UPD-002` Identity proof-consumption boundary; resend.
- **Durable truths and owner:** automated fetch must not verify; resend supersedes old proof.
- **Concurrency/retry/reordering/crash behaviour:** scanner/user/new challenge interleave.
- **Rejected models:** scanner prefetch becomes successful verification; resend reuses old proof.
- **Required invariant:** old automated fetch has no protected transition effect; old proof cannot succeed after supersession.
- **Recommended JIT shape:** Identity scanner-safe proof boundary + standard resend.
- **Conclusion:** `OPEN_HYPOTHESIS / UPSTREAM GAP CONFIRMED`.
- **Upstream amendment:** **YES — existing `COMM-UPD-002`, no new delta.**
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** scanner-old → resend → user-new.
- **Verdict:** BLOCKED UPSTREAM FOR FINAL FREEZE.

## COMM-PT-335 — Scanner fetch and participant protected action race on the same valid proof

- **Scenario:** scanner and real participant hit the link almost simultaneously.
- **Authority involved:** `COMM-UPD-002`; Identity replay/consumption.
- **Durable truths and owner:** automated retrieval must not consume; participant transition remains atomic/replay-safe.
- **Concurrency/retry/reordering/crash behaviour:** simultaneous requests.
- **Rejected models:** first HTTP GET wins regardless actor/interaction semantics.
- **Required invariant:** scanner-safe interaction boundary plus one atomic protected transition.
- **Recommended JIT shape:** upstream Identity proof contract/proof case.
- **Conclusion:** `OPEN_HYPOTHESIS / UPSTREAM GAP CONFIRMED`.
- **Upstream amendment:** **YES — existing `COMM-UPD-002`.**
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** concurrent scanner/user requests.
- **Verdict:** BLOCKED UPSTREAM FOR FINAL FREEZE.

## COMM-PT-336 — Provider click tracking is accidentally re-enabled while scanner prefetch also occurs

- **Scenario:** both provider redirect tracking and independent scanner fetch expose/touch protected URL.
- **Authority involved:** v0.7 provider configuration + `COMM-UPD-002`.
- **Durable truths and owner:** Communications/provider config must not add tracking; Identity still must tolerate independent automated fetch.
- **Concurrency/retry/reordering/crash behaviour:** redirect chain may be prefetched.
- **Rejected models:** solve scanner risk only in provider config; solve provider tracking leak only by making scanner consume harmless but still allow bearer copying.
- **Required invariant:** both defenses hold independently.
- **Recommended JIT shape:** OQ-036 provider proof + Identity scanner-safe consumption.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED` plus existing upstream blocker.
- **Upstream amendment:** no new amendment; `COMM-UPD-002` remains.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** selected-provider redirect inspection + scanner simulation.
- **Verdict:** PASS AT COMMUNICATIONS / BLOCKED AT IDENTITY SEAM.

## COMM-PT-337 — Provider global suppression blocks required security email while participant repeatedly resends

- **Scenario:** every new intent is valid but provider refuses due coarse global suppression.
- **Authority involved:** Product mandatory-vs-marketing distinction; Communications provider evidence; OQ-036.
- **Durable truths and owner:** new source intents may exist; provider limitation is physical delivery constraint.
- **Concurrency/retry/reordering/crash behaviour:** resend could create storm.
- **Rejected models:** clear marketing opt-out; mutate Account email; infinite resend/provider retry.
- **Required invariant:** bounded abuse/retry, participant-visible recovery/change-email path, provider suitability gate.
- **Recommended JIT shape:** terminal delivery constraint + OQ-036 launch validation.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** selected provider suppression behaviour.
- **Verdict:** PASS / RELEASE GATE.

## COMM-PT-338 — Long outage exhausts automated retry budget while proof remains valid and participant requests resend

- **Scenario:** old intent is terminal-auto; source proof may still be valid; participant creates allowed new source challenge.
- **Authority involved:** Communications retry budget; Identity resend.
- **Durable truths and owner:** automated retry terminality is not permanent ban on a new source obligation.
- **Concurrency/retry/reordering/crash behaviour:** old manual recovery may still be visible.
- **Rejected models:** retry-budget exhaustion blocks all future communication for purpose; silently reopen old attempt.
- **Required invariant:** source may create new intent according to Identity policy; old intent stays historical/terminal.
- **Recommended JIT shape:** old terminal + new logical intent.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** retry exhaustion + new resend.
- **Verdict:** PASS.

## COMM-PT-339 — Account closure completes after terminal failure but before participant's delayed resend request arrives

- **Scenario:** client submits resend from stale page.
- **Authority involved:** Identity closure/deletion; Communications.
- **Durable truths and owner:** closure prevents new source challenge/intent.
- **Concurrency/retry/reordering/crash behaviour:** stale browser request.
- **Rejected models:** Communications creates new intent because old terminal record existed; stale UI grants resend.
- **Required invariant:** source owner refuses new obligation; no MessageIntent created.
- **Recommended JIT shape:** source action first, Communications consequence only after authorised issuance.
- **Conclusion:** `UPSTREAM_DERIVED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** stale resend after closure.
- **Verdict:** PASS.

## COMM-PT-340 — Crash/restart occurs after source issuance + durable intent but before queue execution, followed by content withdrawal and provider migration

- **Scenario:** classic must-not-lose window composed with later owner changes.
- **Authority involved:** Class-B durable consequence; C&M; Communications provider policy.
- **Durable truths and owner:** intent survives crash; later execution must use current content/provider authority.
- **Concurrency/retry/reordering/crash behaviour:** restart discovers intent after v1 withdrawal and provider A→B migration.
- **Rejected models:** lost intent; replay source issuance; send stale v1/A because that was state at creation.
- **Required invariant:** durable intent resumes exactly once as a logical obligation, but new provider attempt uses current admissible content/provider state and current source validity.
- **Recommended JIT shape:** durable recovery/reconciler + current attempt-admission theorem.
- **Conclusion:** `WORKING_DESIGN_ACCEPTED`.
- **Upstream amendment:** NO.
- **Conditional dossier pulled forward:** NO.
- **Later executable proof:** crash → authority changes → restart.
- **Verdict:** PASS.

---

# 110. Falsification summary

Across `COMM-PT-301...340`:

- **0** new Communications business Resources were justified;
- **0** accepted core ownership boundaries were overturned;
- **0** new Product/Architecture/Domain/Roadmap amendments were discovered;
- **0** conditional FP-001 dossiers were newly pulled forward;
- **0** cases required provider choice to state the business invariant;
- **2** previously known upstream Identity corrections/clarifications remained active (`COMM-UPD-001`, `COMM-UPD-002`);
- **1** particularly important refinement was added: old provider ambiguity does not block a genuinely new superseding source obligation (`COMM-WD-189`);
- composed cases repeatedly reduced to the owner predicates in §107.

The two-Resource model therefore survived **340 materially distinct pressure tests**.

---

# 111. Conditional-dossier adjudication after adversarial composition

## Privacy & Consent

**`CONDITIONAL / NOT PULLED FORWARD`.**

No required current FP-001 security/account flow needed new Privacy-owned implementation semantics.

The prior trigger remains:

```text
IF public/accountless mailing-list capability is activated
→ Privacy subject/grant/withdrawal/linkage semantics become implementation-grade
→ pull Privacy dossier forward
```

Future optional SMS/WhatsApp/marketing activation may similarly require Privacy work.

Those branches are not current required FP-001.

## Content & Media

**`CONDITIONAL / NOT PULLED FORWARD`.**

Combined cases involving:

- withdrawal;
- successor rebind;
- locale stability;
- provider failover;
- restore

still fit the existing exact-version/current-eligibility/successor contract.

No new C&M Resource/lifecycle must be invented in Communications.

## Audit & Evidence

**`CONDITIONAL / NOT PULLED FORWARD`.**

Combined operator/Audit/callback/deletion cases still fit:

- Communications-owned delivery evidence;
- central minimum privileged/security evidence;
- fail-closed privileged mutation when required Audit cannot be established;
- automated callback/business evidence independent of central Audit availability.

No new central Audit lifecycle became necessary.

## Analytics

**`NO DOSSIER` remains unchanged.**

Nothing in combined delivery correctness depends on Analytics.

---

# 112. Resource-discipline verdict — cumulative through v0.9.0

## Required Resources

### `MessageIntent`

**REQUIRED.**

It remains the durable logical communication obligation.

The adversarial sweep confirms it is the correct anchor for:

- source obligation;
- role;
- destination provenance;
- intended locale;
- channel constraint;
- exact content binding/rebind provenance;
- logical dedup identity;
- terminal/recovery state.

### `DeliveryAttempt`

**REQUIRED.**

It remains the durable external operation/evidence boundary for:

- actual channel;
- actual provider;
- provider operation identity;
- exact content/locale used;
- provider result/evidence;
- ambiguity/reconciliation;
- retry provenance.

## Still not required

The combined cases did **not** justify any of the following as current FP-001 Resources:

- SubscriberContact;
- NotificationPreference;
- InAppNotification;
- CommunicationJourney;
- Channel;
- Provider;
- ProviderRoute;
- ProviderFailoverPolicy;
- ChannelDelivery;
- ContentBinding;
- RenderedMessage;
- RenderSnapshot;
- DeliveryReconciliationCase;
- OperatorAction;
- SupportCase;
- Incident;
- ProviderWebhookEvent;
- ProviderRawPayload;
- RetryBudget;
- ProviderOutage;
- RecoveryWorkflow / DeliveryCase / orchestration Resource.

The fact that several of these are useful **concepts, projections, commands or configuration** does not make them durable business Resources.

---

# 113. Upstream-delta register — stabilised

## COMM-UPD-001 — REQUIRED BEFORE FINAL COMMUNICATIONS CERTIFICATION

**Owner:** certified FP-001 Identity & Access JIT dossier governance.

**Issue:** current Identity v0.1.3 sentence says Communications owns “message body/template”, conflicting with higher current Domain/Architecture/FP-001 authority that assigns governed content/template versions to Content & Media.

**Required action:** narrow Identity PATCH successor/explicit correction preserving the protected-delivery seam.

**Higher-law amendment required:** NO.

## COMM-UPD-002 — REQUIRED BEFORE FINAL CROSS-DOMAIN FREEZE / IMPLEMENTATION

**Owner:** Identity & Access proof-consumption semantics.

**Issue:** current certified Identity lifecycle does not explicitly freeze scanner/prefetch-safe protected-link use.

**Required invariant:** automated provider/security/browser retrieval must not by itself complete verification/reset/recovery/email-change protected transition.

**Required action:** narrow Identity successor/clarification or explicitly governed Identity executable proof contract before Phase 7C final freeze/implementation.

**Higher-law amendment required:** NO.

## No other upstream delta

The adversarial composition sweep discovered no third upstream correction.

---

# 114. Unresolved-gate register — stabilised Pre-JIT view

| Matter | Stabilised disposition |
|---|---|
| `COMM-UPD-001` | **BLOCKS Communications final JIT certification / Phase 7C freeze.** |
| `COMM-UPD-002` | **BLOCKS final cross-domain freeze/implementation unless explicitly resolved/routed.** |
| `OQ-035` | Release-only abuse thresholds/recovery; does not block provider-independent dossier semantics. |
| `OQ-036` | Release-only launch email/in-app provider/channel implementation and operations proof. Communications dossier must remain provider-independent. |
| `OQ-029` | Exact category-specific retention/deletion durations remain later policy/expert gate. |
| `OQ-038` | Future incident ownership; does not require an Incident Resource in FP-001 Communications. |
| Exact Ash Resources/attributes/actions/indexes | Communications JIT detail, not Pre-JIT authority. |
| Exact PostgreSQL uniqueness/locking/conditional-write mechanism | JIT/proof detail. |
| Exact Oban queue/uniqueness/backoff/budget numbers | JIT/OQ-036/proof detail. |
| Exact provider adapter/API/callback fields | OQ-036 + implementation proof. |
| Exact protected-capability storage/encryption package | Identity/Communications JIT/proof; no package selected here. |
| Exact C&M Resource topology | C&M JIT/OQ-013; opaque exact-version/current-eligibility contract is sufficient here. |
| Exact central Audit event schema | Audit implementation detail; semantic minimum contract is sufficient here. |

---

# 115. Later executable proof-obligation additions — v0.9.0

196. Proof expiry + provider unknown + content withdrawal yields zero new provider calls and safe protected-capability cleanup.
197. Proof consumption while provider status is unknown terminates further delivery without waiting for provider callback.
198. Provider outage + language change + resend suppresses old-language superseded intent and delivers only current source-valid intent.
199. Old unknown provider operation does not block a new superseding source obligation; old late delivery contains unusable proof.
200. Email-change cancellation/supersession makes late old confirmation harmless.
201. Applied email change + provider outage preserves event-correct old-address notice routing.
202. Deletion + unknown provider operation permits bounded historical reconciliation without recreating active Account/contact/send authority.
203. Deletion + Audit outage + operator retry produces no provider mutation.
204. Duplicate-account merge suppresses stale source-invalid queued work without rewriting historical Communications provenance.
205. Late provider callback after merge remains attributable to original source/attempt.
206. Restore from pre-deletion/pre-migration backup produces zero egress until current owner/configuration reconciliation completes.
207. Provider outage exceeding proof/capability lifetime cannot result in stale protected delivery.
208. Mixed migration backlog treats no-attempt intents and old-provider unknown attempts differently and correctly.
209. Retiring provider credentials cannot fabricate resolution of old unknown attempts.
210. Safe content-successor rebind + provider failover preserves old attempt provenance and produces at most one new operation.
211. Content withdrawal + unknown old provider attempt prevents corrected-provider failover until reconciliation.
212. Provider failover does not mutate the MessageIntent locale after Account language changes.
213. Recovery intent queued across Account-email change rechecks source validity and never silently retargets destination.
214. Optional future fallback loses admission immediately when current purpose/channel permission is withdrawn.
215. Accountless-linkage conditional branch cannot restore withdrawn marketing permission.
216. Invalid callback flood + provider outage/backlog does not create business mutation or unbounded Audit/cardinality amplification.
217. Late delivered callback after proof expiry updates provider evidence only.
218. Late callback after deletion obeys current retention/minimisation and cannot restore active authority.
219. Audit outage allows valid automated callback commit but blocks required privileged provider-mutating action.
220. Participant resend racing operator old-intent retry yields at most the new source-valid operation.
221. Old-intent reconciliation remains possible after resend without permitting old-intent delivery.
222. Automated terminal failure + participant resend + stale manual recovery cannot produce stale proof send.
223. Mixed-validity provider batch recovery performs per-intent current admission.
224. Oban uniqueness cannot coalesce a new resend MessageIntent with the superseded old intent.
225. Business idempotency cannot dedupe a new source challenge into an old MessageIntent merely because destination/purpose match.
226. Two-node content-rebind/provider-failover race creates at most one new DeliveryAttempt.
227. Source invalidation + C&M withdrawal + provider-attempt admission interleavings satisfy the cutover theorem.
228. Content correction after provider acceptance + source proof consumption cannot cause same-intent resend.
229. Scanner prefetch + resend/supersession is harmless after `COMM-UPD-002` correction.
230. Scanner/user concurrency on one valid proof cannot let automated fetch complete the protected transition.
231. Provider click-tracking remains disabled for protected links and Identity remains independently scanner-safe.
232. Provider global suppression + repeated resend stays bounded and participant-recoverable without mutating marketing preference/Account email.
233. Automated retry exhaustion does not prevent a newly authorised source resend.
234. Stale resend request after Account closure creates no source challenge or Communications intent.
235. Crash after durable intent + later content/provider changes resumes the original obligation using current admissible execution truth without replaying source issuance.

---

# 116. Stabilisation closure record

## 116.1 Broad-discovery outcome

**PASS — PARK BROAD COMMUNICATIONS PRE-JIT DISCOVERY.**

This verdict applies to the **discovery process**, not to governed Communications JIT certification.

The adversarial sweep did what it was intended to do:

- composed multiple previously independent hazards;
- searched for hidden shared-write ownership;
- searched for state-machine collapse;
- searched for resource proliferation;
- searched for conditional-dossier triggers;
- searched for provider-dependent holes;
- searched for new upstream contradictions.

It did not falsify the core model.

## 116.2 Governed-dossier readiness

**BLOCKED / STOP BEFORE FINAL GOVERNED COMMUNICATIONS JIT CERTIFICATION.**

Reason:

```text
COMM-UPD-001
COMM-UPD-002
```

remain unresolved upstream Identity items.

This does **not** justify more broad Communications scenario invention.

The correct next work is governance/consolidation, not additional random pressure tests.

## 116.3 Stable working conclusion

For the required current FP-001 Communications path:

```text
REQUIRED DURABLE BUSINESS RESOURCES
→ MessageIntent
→ DeliveryAttempt

REQUIRED NON-RESOURCE MECHANISMS / CONCEPTS
→ protected delivery capability where applicable
→ bounded channel vocabulary
→ typed thin provider/channel adapter
→ current owner revalidation
→ retry/reconciliation machinery
→ operator/support projections
→ bounded Audit linkage
→ observability

NOT REQUIRED CURRENT FP-001 RESOURCES
→ SubscriberContact
→ NotificationPreference
→ InAppNotification
→ CommunicationJourney
→ Channel
→ Provider
→ orchestration/reconciliation/support/incident wrapper Resources
```

## 116.4 Conditional-dossier conclusion

```text
Privacy & Consent
→ CONDITIONAL / NOT PULLED FORWARD

Content & Media
→ CONDITIONAL / NOT PULLED FORWARD

Audit & Evidence
→ CONDITIONAL / NOT PULLED FORWARD

Analytics
→ NO DOSSIER
```

These dispositions should be preserved into the eventual Phase-7B consolidation / Phase-7C handoff unless new evidence changes them.

## 116.5 Stop rule for further discovery

Do **not** add another ordinary broad Communications pressure-test round merely to increase count.

Reopen discovery only for:

1. changed live authority;
2. changed FP-001 scope;
3. resolution of `COMM-UPD-001` / `COMM-UPD-002` that changes the seam;
4. contradiction encountered during consolidation/dossier drafting;
5. implementation/proof evidence that falsifies an accepted working design;
6. activation of a previously conditional branch such as accountless marketing or SMS/WhatsApp.

## 116.6 Recommended next artifact step

The next successor should be a **compression / consolidation pass**, not new broad discovery.

It should produce the requested final Pre-JIT registers in compact, reviewer-oriented form:

1. accepted working-design register;
2. pressure-test coverage register;
3. upstream-delta register;
4. unresolved-gate register;
5. cross-stream dependency register;
6. conditional-dossier adjudication;
7. rejected-model register;
8. later proof-obligation register;
9. completeness/stabilisation assessment.

That consolidation should remove repetition without discarding semantic conclusions, preserve traceability back to the local `COMM-WD-*` / `COMM-PT-*` labels, and explicitly state that governed dossier drafting remains blocked on the two upstream Identity items.
