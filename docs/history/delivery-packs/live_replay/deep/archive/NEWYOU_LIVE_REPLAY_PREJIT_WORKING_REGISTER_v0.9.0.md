# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.9.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PROPOSED REGISTER SUCCESSOR
- **Document version:** v0.9.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.8.1.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted predecessor commit:** `aaa9e97cb29a0f4499fcb5bf88691bb2863686d7`
- **Pass K discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.11.0.md`
- **Pass K discovery commit:** `68ce041d36d6ead8ffa54b6758ebbf070fd6d68c`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic rule:** Passes A–J remain `ACCEPTED_WORKING_LOCK`. Pass-K additions below remain `PROPOSED / AWAITING_USER_ACCEPTANCE` until explicitly accepted.

---

# 1. Cumulative state

Accepted working lock currently covers:

- Pass A / discovery v0.1.0;
- Pass B / discovery v0.2.0;
- Pass C / discovery v0.3.0;
- Pass D / discovery v0.4.0;
- Pass E / discovery v0.5.0;
- Pass F / discovery v0.6.0;
- Pass G / discovery v0.7.0;
- Pass H / discovery v0.8.0;
- Pass I / discovery v0.9.0;
- Pass J / discovery v0.10.0;
- `LIVE-PT-001...LIVE-PT-109`;
- `LIVE-UPD-001...LIVE-UPD-006`, with no `LIVE-UPD-007`;
- `LIVE-GAP-001...LIVE-GAP-014`, with no `LIVE-GAP-015`;
- no `LIVE-EV-*` entries.

Pass K adds proposed participant-communication findings only. It does not reopen accepted occurrence, registration, attendance, access, recording/consent, retention/deletion, replay-correction or promotional-clip semantics.

---

# 2. Pass register addition

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| K | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.11.0.md` | `68ce041d36d6ead8ffa54b6758ebbf070fd6d68c` | participant communications around live/replay lifecycle events | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

---

# 3. Proposed Pass-K working conclusions

1. **Communications remains delivery authority only.** It never becomes registration, occurrence, access, replay-publication, privacy or correction authority.
2. **FP-007 notification-failure visibility is obligation-scoped.** It requires governed notification obligations to expose failure; it does not silently create every conceivable lifecycle message.
3. **The future FP-007 Final Contract must enumerate included/promised participant communication roles.** UI copy and implementation may not invent them.
4. **Registration confirmation, reschedule/cancellation notice and replay-available notification are not identified by current authority as universal outbound FP-007 promises.** If included, OQ-036 applies.
5. **DEC-186 requires protected joining instructions, not email as authority.** A protected current application surface may satisfy the access requirement if the Final Contract permits it; promised outbound delivery remains separately governed.
6. **OQ-017 remains non-blocking until reminders are promised.** Once promised, OQ-017 owns reminder mechanics and OQ-036 the selected launch channel/provider proof.
7. **Any explicitly promised live notification journey routes through OQ-036.** The live capability cannot assume an unapproved provider/channel.
8. **Material correction notification is owner-conditional.** Product Law requires affected participants to be notified where appropriate; the governing source owner decides applicability/affected set, not Communications.
9. **Safety correction notification is mandatory Product consequence.** Unsafe replay use is withdrawn immediately; the notification proceeds as a must-not-lose Architecture Class-B consequence and failure remains visible.
10. **Legal/consent/withdrawal notice duties remain OQ-021/Privacy/legal dependent unless another current authority requires them.** Communications does not invent the duty.
11. **Mandatory/promised notification intent must be durable.** Crash/restart cannot lose the obligation, and best-effort PubSub is not a substitute for Class-B delivery semantics.
12. **Provider acceptance, delivery and unknown outcome remain evidence only.** They never freeze or recreate source state.
13. **Historical messages can become stale.** Current platform authority plus bounded capabilities prevent them from restoring obsolete schedule/access/publication state.
14. **Marketing preference is distinct from mandatory product/safety notice.** Marketing opt-out cannot suppress a correctly classified mandatory safety notice; optional reminder/marketing roles cannot misuse the mandatory class.
15. **Full Deletion/current privacy authority is revalidated before new provider I/O.** Queued messages are not self-authorising.
16. **No new Live-specific Communications Resource is justified.** Existing MessageIntent/DeliveryAttempt planning seams remain sufficient absent contrary JIT evidence.
17. **`LIVE-GAP-006` is refined and reused.** No `LIVE-GAP-015` is warranted.
18. **No `LIVE-UPD-007` is warranted.**
19. **No `LIVE-EV-*` is warranted yet.**

These are proposed working conclusions only until accepted.

---

# 4. Pressure-test additions

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-110` | Registration succeeds but registration-confirmation delivery fails | v0.11.0 | `PASS_WITH_REFINEMENT / JOURNEY_SCOPE_DEPENDENT` | `FP007_FINAL_CONTRACT → EVENTS_JIT → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → FAILURE/RECONCILIATION_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-111` | Protected joining instructions available in-app but outbound delivery fails | v0.11.0 | `PASS_WITH_REFINEMENT / ACCESS_SURFACE_NOT_DELIVERY_AUTHORITY` | `DEC-186 → EVENTS/ENTITLEMENTS_JIT → COMMUNICATIONS_JIT_IF_OUTBOUND_INCLUDED → OQ-036_IF_PROMISED → ACCESS/FAILURE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-112` | Pre-session reminder is never sent | v0.11.0 | `PASS / OQ-017_NON_BLOCKING_UNLESS_PROMISED` | `FP007_FINAL_CONTRACT → OQ-017_IF_REMINDER_PROMISED → OQ-036_CHANNEL_PROOF_IF_PROMISED` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-113` | Registered participant receives old schedule message, then occurrence is rescheduled | v0.11.0 | `PASS_WITH_REFINEMENT / SOURCE_FACT_DOMINATES` | `LIVE-UPD-001 / EVENTS_JIT → FP007_JOURNEY_SCOPE → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → REORDER/IDEMPOTENCY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-114` | Occurrence cancelled but cancellation delivery fails or is unknown | v0.11.0 | `PASS_WITH_REFINEMENT / JOURNEY_SCOPE_DEPENDENT` | `EVENTS_JIT → FP007_FINAL_CONTRACT → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → UNKNOWN/FAILURE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-115` | Previously delivered joining instructions become stale after source change | v0.11.0 | `PASS_WITH_REFINEMENT / CURRENT_AUTHORITY_ENFORCEMENT` | `EVENTS/ENTITLEMENTS_JIT → LIVE-UPD-001/004 → OQ-020 → CONTROLLED_LIVE_ACCESS_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-116` | Replay current but replay-available notification fails | v0.11.0 | `PASS_WITH_REFINEMENT / JOURNEY_SCOPE_DEPENDENT` | `CONTENT_MEDIA/ENTITLEMENTS_JIT → FP007_FINAL_CONTRACT → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → STALE-SOURCE/FAILURE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-117` | Material replay correction after participants consumed V1 | v0.11.0 | `PASS_WITH_REFINEMENT / AFFECTED_SET_AND_APPROPRIATENESS_OWNER_DEPENDENT` | `PRODUCT_CORRECTION_CLASS → CONTENT/SAFETY_JIT → AFFECTED_SET_RULE → COMMUNICATIONS_JIT → OQ-036 → CLASS-B_FAILURE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-118` | Safety correction withdraws replay and participant notification delivery fails | v0.11.0 | `PASS / MANDATORY_DURABLE_CONSEQUENCE` | `SAFETY/C&M_AUTHORITY → CLASS-B_DURABLE_HANDOFF → COMMUNICATIONS_JIT → OQ-036 → CRASH/RETRY/UNKNOWN/TERMINAL_FAILURE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-119` | Legal/consent correction or recording-purpose withdrawal may require participant notice | v0.11.0 | `BLOCKED / OQ-021_PRIVACY_LEGAL` | `PRIVACY/CURRENT_AUTHORITY → OQ-021 → CONTENT_MEDIA_JIT → COMMUNICATIONS_JIT_IF_NOTICE_REQUIRED → OQ-036_AS_APPLICABLE` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-120` | Full Deletion Request while live/replay message queued before provider submission | v0.11.0 | `PASS_WITH_REFINEMENT / CURRENT_OWNER_REVALIDATION` | `PRIVACY_JIT → COMMUNICATIONS_JIT → DELETION_RACE/RESTART_PROOF → OQ-030/032_AS_APPLICABLE` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-121` | Duplicate/reordered source lifecycle changes would create conflicting messages | v0.11.0 | `PASS / IDEMPOTENT_SOURCE_ROLE_INTENT` | `SOURCE_JIT → COMMUNICATIONS_JIT → DUPLICATE/REORDER/CONCURRENCY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-122` | Provider accepted old message, then source truth changes before delivery known | v0.11.0 | `PASS_WITH_REFINEMENT / EXTERNAL_IRREVERSIBILITY` | `COMMUNICATIONS_JIT → SOURCE_CURRENT_AUTHORITY → PROVIDER_UNKNOWN/REORDER_PROOF → STALE-CAPABILITY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-123` | Marketing opt-out but mandatory safety correction notice exists | v0.11.0 | `PASS_WITH_REFINEMENT / PURPOSE_CLASS_SEPARATION` | `SAFETY/C&M_SOURCE_ROLE → PRIVACY/PREFERENCE_POLICY → COMMUNICATIONS_JIT → OQ-036 → POLICY_MATRIX_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-124` | No outbound journey promised, so no MessageIntent exists | v0.11.0 | `PASS_WITH_REFINEMENT / OBLIGATION_EXISTENCE_MUST_BE_EXPLICIT` | `FP007_FINAL_CONTRACT → ACCEPTANCE_CRITERIA → COMMUNICATIONS_JIT_ONLY_FOR_INCLUDED_ROLES` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-125` | Mandatory notification exists but provider delivery terminally fails | v0.11.0 | `PASS / TERMINAL_FAILURE_VISIBILITY_REQUIRED` | `SOURCE_OBLIGATION → COMMUNICATIONS_JIT → OQ-036 → OUTAGE/BOUNCE/UNKNOWN/RETRY-EXHAUSTION/OPERATOR_RECOVERY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Detailed timelines, invariants, adversarial variants, questions and evidence needs remain in discovery v0.11.0.

---

# 5. Proposed refinement of `LIVE-GAP-006`

## `LIVE-GAP-006 — Promised live communications`

**Classification remains:** `COMMUNICATIONS_GATE`

Pass K proposes no new gap ID. Instead it refines the existing route:

1. **Ordinary lifecycle messages:** registration confirmation, reschedule/cancellation notice and replay-available notice are not universal outbound promises under current FP-007 authority. If included in the Final Contract, OQ-036 blocks that promised journey until approved.
2. **Protected joining instructions:** required under DEC-186 as protected access; outbound notification is separate and OQ-036 applies only if that outbound journey is promised.
3. **Reminders:** OQ-017 remains non-blocking until promised; once promised, OQ-017 governs reminder mechanics and OQ-036 the selected launch channel/provider proof.
4. **Material correction notices:** governing source owner determines `where appropriate` + affected set; once required, notification is a durable consequence and OQ-036 applies to execution.
5. **Safety correction notices:** explicit Product obligation; Class-B must-not-lose consequence with terminal-visible failure and OQ-036 release/provider proof.
6. **Legal/consent/withdrawal notices:** OQ-021/Privacy/legal authority first; Communications/OQ-036 follow only after obligation exists.
7. **Full Deletion:** queued execution revalidates current owner authority before provider admission; stale work is not self-authorising.

No governed sub-identifiers are created for these routes.

---

# 6. UPD register adjudication

## No `LIVE-UPD-007`

Pass K creates no new upstream-decision identifier.

Rationale:

- Domain Law already preserves source-owner/Communications separation;
- DEC-186 already defines protected joining-instruction requirement;
- Roadmap already defines conditional OQ-036 and optional-until-promised OQ-017 routing;
- Product correction law already defines material/safety notification consequence;
- OQ-021/Privacy already owns unresolved legal/consent notice duties;
- Architecture already defines Class-B mandatory durable consequences and terminal-visible execution;
- existing Communications working evidence already covers logical intent, provider attempt/evidence, ambiguity, retry and source-precondition revalidation.

Creating `LIVE-UPD-007` would duplicate existing authority/routing.

---

# 7. Gap-register adjudication

## No `LIVE-GAP-015`

Pass K creates no new gap identifier.

`LIVE-GAP-006` remains the correct communication gate and is refined above. Do not overload:

- `LIVE-GAP-001` with delivery mechanics;
- `LIVE-GAP-003` with ordinary message transport;
- `LIVE-GAP-005` with replay-available notification;
- `LIVE-GAP-014` with ordinary notification provider delivery.

The only legal/privacy overlap is routed to existing OQ-021/Privacy authority when that owner must first determine whether a notice duty exists.

---

# 8. Evidence register

No `LIVE-EV-*` item is added by Pass K.

Later proof should cover the relevant included/required roles:

- source→intent idempotency and crash safety;
- Class-B no-lost-intent behaviour for mandatory safety/material notices;
- duplicate/reordered source handoffs;
- current-source revalidation before provider I/O;
- provider accepted/delivered/unknown/terminal-failure distinctions;
- stale reschedule/cancellation message behaviour;
- stale join capability cannot restore access;
- replay correction/withdrawal invalidates future sends where applicable;
- marketing preference versus mandatory safety notice separation;
- terminal notification failure visibility and safe operator recovery.

Provider-specific claims remain deferred to OQ-036/provider validation.

---

# 9. Explicit non-decisions preserved

Pass K does **not** decide:

- which ordinary outbound lifecycle messages the FP-007 Final Contract will include;
- whether email, in-app or both fulfil a future message role;
- reminder timing/channel/quiet-hour policy;
- exact message wording/templates;
- exact Class-B cross-domain handoff topology;
- exact Communications schema/actions/jobs;
- provider selection, retry/failover mechanics or alert SLA;
- exact material-correction affected-set algorithm;
- OQ-021 legal/privacy notice duties;
- destination/change-of-email details;
- communication engagement analytics;
- event-commerce notices;
- promotional campaign messaging;
- retention durations.

---

# 10. Pass-K proposed outcome

**Outcome:** `PASS`

Current authority is semantically sufficient to plan the participant-communication seam without a new Product amendment or new gap identifier. Remaining work is correctly routed to Final Feature Pack scope selection, OQ-017, OQ-036, OQ-021/Privacy/legal where applicable, Communications JIT and executable/provider proof.

---

# 11. Acceptance transition rule

If Pass K is accepted without semantic changes, create non-semantic status successor `v0.9.1` that promotes:

- Pass K;
- `LIVE-PT-110...LIVE-PT-125`;
- the §3 Pass-K conclusions;
- the §5 refinement of `LIVE-GAP-006`;
- the decision that no `LIVE-UPD-007` is warranted;
- the decision that no `LIVE-GAP-015` is warranted;
- the decision that no `LIVE-EV-*` is warranted;

to `ACCEPTED_WORKING_LOCK`.

If semantic changes are requested, create a substantive successor instead and preserve this v0.9.0 unchanged.

---

# 12. Proposed next focused pass

Only after Pass K acceptance:

> **Cross-dimensional convergence and JIT-entry readiness — pressure-test simultaneous occurrence/access/privacy/media/communications changes under retries, reordering, restart and reconciliation, then perform a final contradiction/gap/proof-route sweep without adding new Product scope.**

This should be a bounded closure pass. Its purpose is to determine whether accepted A–K semantics compose under adversarial races and whether Live & Replay discovery can stop and hand off cleanly to governed Feature Pack/JIT planning.