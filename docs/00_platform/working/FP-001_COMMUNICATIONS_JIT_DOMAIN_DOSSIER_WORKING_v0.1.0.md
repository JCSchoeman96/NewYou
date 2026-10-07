# FP-001 Communications JIT Domain Dossier

~~~text
PROPOSED PATH: docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md
PROPOSED VERSION: v0.1.0
PHASE: 7B implementation-grade planning
FEATURE PACK: FP-001
DOMAIN: COMMUNICATIONS
STATUS: CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT
NON-EXECUTABLE
NOT PHASE 7C DEVELOPMENT-ENTRY AUTHORITY
DOES NOT AMEND PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW
~~~

This path and version are proposed for review. This file is a working candidate, not a governed identifier, current authority, certification record or implementation approval.

The authority baseline is live GitHub main at 0473cd69416f72fd94f2cee24a4d02c7f4fe0992, verified against git ls-remote and the checked out main commit. The live main SHA has not moved from the supplied baseline.

## 1. Authority, baseline and post-Identity delta

### 1.1 Authority order

Apply the repository authority hierarchy in this order:

1. Product Law.
2. Architecture Law.
3. Domain Law.
4. Roadmap.
5. Platform Operating Model and Frontend Experience System where applicable.
6. Current Open Work.
7. Certified FP-001 Skeleton.
8. Certified Identity & Access JIT Domain Dossier.
9. Communications Pre-JIT material as non-authoritative evidence only.

The README and manifest route readers to current sources. The Delivery Atlas is derived navigation and creates no law.

### 1.2 Current authority baseline

The live README and manifest identify these current sources and versions:

| Authority | Current source | Material use in this dossier |
|---|---|---|
| Product direction | docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md | §§5.1, 8, 10-13 for bilingual entry, account scope and first-launch boundaries |
| Product Law | docs/00_platform/00_PLATFORM_v1.6.0.md | §21I.24; §§21E.1-21E.10; §§21J.1-21J.2, 21J.7-21J.8, 21J.10, 21J.18-21J.20, 21J.24 |
| Decision Register | docs/00_platform/01_DECISIONS_v1.6.0.md | DEC-017-028; DEC-244-267; DEC-297-298; OQ-034-036 |
| Open Work | docs/00_platform/02_OPEN_WORK_v1.2.57.md | §§7B, 7C, 9, 12.14; Communications next-stage status and conditional-dossier status |
| Architecture | docs/00_platform/03_ARCHITECTURE_v1.1.1.md | §§4-8, 10.1, 10.4, 11.1-11.2, 12.1-12.4, 13, 14-16 |
| Domain Law | docs/00_platform/04_DOMAIN_MAP_v1.2.0.md | §§4-5; §§6.1, 6.2, 6.7, 6.15, 6.18 |
| Roadmap | docs/00_platform/05_ROADMAP_v1.2.0.md | §6 FP-001 |
| Operating Model | docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md | §§2-6, 8, 12-13 |
| Frontend contract | docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md | §§3.2-3.3, 4, 5.2, 5.7, 6, 10.2-10.4 |

docs/00_platform/README.md identifies these as current. docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json records current authority paths, versions and integrity metadata. The manifest is an inventory, not a new authority layer.

### 1.3 Certified FP-001 working contracts

| Contract | Current source | Material use |
|---|---|---|
| Phase 7A Skeleton | docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md | §§5-8, 10, 12-17; FP-001 scope, required Communications dossier, conditional candidates and Phase 7C stop |
| Identity & Access dossier | docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md | §§I-J, J.1, J.1a, R-U, X-AA; ownership, atomic handoff, protected capability and proof consumption |

Open Work v1.2.57 §12.14 and the current Identity dossier record Identity v0.1.4 as CERTIFIED / CURRENT under the separate PR #77 status successor. The dossier preserves the completed PR #76 candidate certification and post-merge evidence. Identity remains the sole authority for proof and primary-email-change truth.

### 1.4 Post-Identity-correction delta revalidation

The Communications Pre-JIT README and v0.10.0 consolidation are WORKING / NON-AUTHORITATIVE. Their authority pin, 3f899e00ecfdfb9abc0794cffcb19eaff2726d58, predates current main. The COMM-UPD-001 and COMM-UPD-002 labels are used here only to locate old seam questions. They do not create authority.

| Old working label | Earlier issue in Pre-JIT §3 | Current authority check | Revalidation |
|---|---|---|---|
| COMM-UPD-001 | Pre-JIT described governed message/template content ownership as an unresolved correction. | Domain Map §6.7 assigns governed message/template versions to Content & Media. Architecture §§10.1 and 10.4 require immutable locale/version provenance. Identity v0.1.4 §§I and J.1 assigns content ownership to Content & Media and delivery binding/provenance and execution to Communications. Its final state and Open Work §12.14 record the correction as certified/current. | Resolved by current authority. No upstream amendment is needed. |
| COMM-UPD-002 | Pre-JIT required an explicit rule against scanners, previews, HEAD, GET and prefetch consuming proof. | Identity v0.1.4 §J.1a requires passive retrieval to be non-consuming, followed by explicit participant action, fresh Identity checks and a single-use guarded mutation. Its final state and Open Work §12.14 record the correction as certified/current. | Resolved by current authority. No upstream amendment is needed. |

The current Identity contract and Open Work independently preserve the two-Resource FP-001 Communications model. Domain Map §6.15 describes broader mature Communications concepts, but it does not require each concept to become a Resource in FP-001.

I found no Product, Architecture, Domain or Roadmap contradiction in this revalidation. The old Pre-JIT BLOCKED / STOP wording describes its earlier baseline. Current Open Work still says Communications is REQUIRED / NEXT / NOT_STARTED and Communications finalisation is BLOCKED / STOP because this dossier and applicable dispositions remain outstanding. This candidate does not change that status.

## 2. Purpose and scope

Communications supplies implementation-grade delivery semantics for the Identity-related communication consequences in FP-001. Its purpose is to preserve each source-authorised communication obligation, deliver it to the destination authorised for that obligation, retain delivery evidence, and stop safely when source validity or provider outcome is uncertain.

The in-scope roles are:

| Communication role | Source identity and destination meaning |
|---|---|
| Account/email verification | One Identity verification challenge and its issuing operation. Use the exact destination Identity authorised when that challenge was issued. |
| Password reset | One Identity reset challenge and request operation. Use the exact destination Identity authorised when that challenge was issued. |
| Account recovery | One recovery operation/challenge. Use the destination Identity authorised for that recovery step. |
| New-address primary-email-change confirmation | One primary-email-change operation and its new-address confirmation challenge. Use the pending new address captured for that operation. This is the proof-bearing message. |
| Old-address primary-email-change notice | The relevant primary-email-change operation/event. Use the old canonical address captured before the change. This is a security notice, not proof. |
| Required security/account notice | Only a message required by a named current Identity transition. Its source event, semantic role and authorised destination must be explicit. No generic notice catalogue is introduced. |

These obligations are not marketing. No marketing purpose permission, marketing preference, newsletter, campaign, journey, generic notification centre, or mandatory email-plus-in-app duplication is introduced. A participant resend that causes Identity to issue or supersede a challenge creates a new source obligation and a new MessageIntent.

Accountless mailing-list acquisition and optional marketing are outside this FP-001 contract. A later proposal for those flows requires its own current-authority and conditional-dossier review. This candidate does not create SubscriberContact or NotificationPreference and does not authorise that work.

The dossier does not add SMS/WhatsApp delivery, native push, accountless mailing-list acquisition, generic support workflow, or unrelated product notifications. "Email and in-app first" remains a channel-capable launch direction. It does not require every Identity message to use both channels. OQ-036 remains unresolved.

## 3. Ownership and authority

| Truth or operation | Sole owner | Communications contract |
|---|---|---|
| Account truth and canonical account email | Identity & Access | Read the current non-secret source contract. Never mutate or infer account identity. |
| Security Challenge purpose, validity, expiry, supersession, revocation and consumption | Identity & Access | Check source eligibility before an attempt. Never issue, consume, revive or reinterpret proof. |
| Verification, recovery completion and primary-email-change truth | Identity & Access | Delivery status is an observation only. It cannot establish a source transition. |
| Logical communication obligation and dispatch disposition | Communications | Own MessageIntent and the fact that a delivery obligation exists, is held, is ambiguous or has ended. |
| Destination provenance for an obligation | Communications, from Identity-authorised source data | Retain the minimum exact destination needed to retry and explain the recipient. Never silently resolve the current Account email on retry. |
| Governed message/template content and locale versions, publication and eligibility | Content & Media | Resolve and publish exact eligible versions. Communications stores a version reference and delivery provenance, not content authority. |
| Delivery execution, DeliveryAttempt, provider observations and delivery reconciliation | Communications | Own normalised delivery evidence and terminal delivery-side status. |
| Purpose-level consent and withdrawal truth | Privacy & Consent | Not used as a marketing gate for required FP-001 Identity messages. Any later optional purpose must be checked through Privacy’s owner contract. |
| Restricted cross-domain audit/security evidence | Audit & Evidence | Receive only minimum evidence explicitly required by current authority. Communications retains its own delivery ledger. |
| Provider state, telemetry, analytics, PubSub, jobs, UI and support projections | None of these are originating business authority | They may carry evidence or freshness signals only. |

No shared writes are permitted. Cross-domain reads or commands use the owning Domain boundary. Communications never writes Identity, Content & Media, Privacy & Consent or Audit persistence directly.

## 4. Required Resources and excluded concepts

Exactly two durable FP-001 Communications Resources are required:

1. **MessageIntent**
2. **DeliveryAttempt**

The bounded protected capability described in §8 is sensitive delivery machinery. It is not a third business Resource.

The following are not FP-001 Communications Resources on current evidence: SubscriberContact, NotificationPreference, InAppNotification, CommunicationJourney, Channel, Provider, ProviderRoute, ProviderFailoverPolicy, ChannelDelivery, ContentBinding, RenderedMessage, RenderSnapshot, DeliveryReconciliationCase, OperatorAction, SupportCase, Incident, ProviderWebhookEvent, ProviderRawPayload, RetryBudget, ProviderOutage, RecoveryWorkflow and DeliveryCase.

A field, reference, bounded value, immutable fact or operational projection does not become a Resource merely because it has a name. A new Resource would require a distinct durable business truth, an authoritative requirement and a current FP-001 need.

## 5. MessageIntent contract

### 5.1 Purpose, ownership and identity

A MessageIntent is one logical communication obligation caused by one authoritative source operation/challenge plus its semantic communication role. Communications owns its lifecycle.

Its stable causal identity is based on the source owner, source operation/challenge or source event identifier, and semantic role. Where one source operation can produce distinct required notices, the specific source event/obligation reference distinguishes them. It is not keyed by Account + purpose + destination. A resend with a newly issued or superseding Identity challenge has a new causal identity and therefore a new MessageIntent.

The intent has an opaque durable identifier. The source reference and role provide business idempotency. Duplicate source handoff returns or recognises the same logical intent; it must not create another one. A provider retry remains execution of the same MessageIntent.

### 5.2 Required concepts

The durable intent records only what its invariants require:

- opaque intent identifier;
- originating owner and non-secret source operation, event and challenge references;
- closed semantic communication role and source purpose reference;
- the exact destination value authorised by Identity, its source/provenance and the point at which it was authorised; a reference is sufficient only if it always resolves to that same historical value and never to the current Account email;
- intended locale fixed for this obligation;
- exact Content & Media content and locale version once bound;
- independent dispatch disposition and terminal reason;
- safe correlation and idempotency references;
- creation, binding, attempt-admission and terminal timestamps needed for recovery and explanation;
- minimal, non-secret pre-provider failure and reconciliation facts.

Do not persist the bearer token, a rendered secret-bearing URL, a complete rendered body, provider credentials, or a high-detail raw provider payload in MessageIntent. A provider or channel label is bounded routing metadata, not a Provider or Channel Resource.

The intent's side effect is to establish one durable communication obligation and make it discoverable for execution. It does not itself make a provider call or change Identity truth.

The exact recipient must remain stable for any authorised retry. The exact value is restricted personal contact data and is not copied into ordinary logs, telemetry, Audit payloads, Analytics or routine operator displays. Retain it only while delivery or an authorised reconciliation requires it, subject to Privacy retention authority.

### 5.3 Independent lifecycle dimensions

A single MessageIntent status must not collapse independent facts. Preserve these dimensions:

| Dimension | Owner and values |
|---|---|
| Dispatch disposition | Communications: open, held, reconciliation_required, or closed. A separate terminal reason records delivery evidence, terminal failure, source invalidation, cancellation or other governed closure. |
| Source eligibility | Identity supplies a fresh, non-secret, role-specific allow/stop result for the exact source reference. Communications does not own or cache it as current proof truth. |
| Attempt admission | Communications records whether a concrete provider operation has crossed the durable attempt-admission boundary. Admission is not provider evidence. |
| Provider outcome | Derived from DeliveryAttempts: no provider observation yet, rejected before submission, accepted, delivered where established, bounced/failed, or unknown. |
| Content binding | unbound, bound to one exact eligible content/locale version, or held because the binding became ineligible. |
| Protected capability | Not required, recoverable for this intent, or irrecoverable/cleared. It is governed separately from the intent’s send status. |

Accepted does not mean delivered. Delivered does not mean proof consumed or Identity success. A source becoming invalid ends future send authority but does not rewrite already-recorded attempt evidence.

### 5.4 Transitions and guards

- Identity’s authorised source transition creates the MessageIntent in the same must-not-lose handoff as any required protected capability.
- An open intent can remain open while awaiting execution, content binding or a transient dependency. A pre-provider validation, rendering, admission or queue failure is recorded against the intent and does not create a DeliveryAttempt.
- A missing or ineligible source/content prerequisite holds the intent. Resolve it only through the owning Domain’s current contract.
- Any possibly submitted provider operation with unknown outcome moves the intent to reconciliation_required. No new provider submission is admitted while ambiguity remains.
- A conclusive provider rejection or failure may permit a new attempt under the same intent only if current Identity eligibility, destination, content and the future channel/provider policy allow it.
- A source invalidation, expiry, revocation, supersession or consumption ends send authority for a protected proof obligation. Communications closes or holds the intent according to its evidence, clears the protected capability and does not revive the obligation.
- Delivery evidence or a governed terminal delivery decision closes the dispatch obligation. It does not change the originating Identity state.
- A participant resend that creates new Identity proof is not a transition back to open. It creates a new MessageIntent.

The dispatch disposition never substitutes for the Identity source dimension, protected-capability validity, content eligibility or provider-attempt outcome.

### 5.5 Invariants, side effects and terminal behaviour

- One source obligation plus role produces at most one logical intent.
- Each intent preserves its authorised destination and intended locale.
- One intent can have multiple DeliveryAttempts only when prior external ambiguity is resolved and a new attempt is safe.
- Provider execution cannot change source truth, content eligibility, consent or canonical email.
- Closing an intent prevents future submissions. It does not erase delivery history or authorise a new source operation.
- Terminal reasons remain distinguishable: delivery observed; source invalid/expired/revoked/superseded/consumed; explicit source cancellation; or terminal delivery failure.
- A terminal failure remains visible for permitted support/reconciliation. It does not create a generic support case or operator workflow.
- When no send or reconciliation need remains, Communications clears the recipient and other personal details that no longer have a retention basis. Applicable Privacy retention/hold authority controls retained ledger evidence.

## 6. DeliveryAttempt contract

### 6.1 Purpose, ownership and identity

A DeliveryAttempt is one concrete provider/channel submission operation and its evidence. Communications owns the record. Durable attempt admission and the provider's outcome are separate facts; admission alone does not establish that a provider accepted or delivered anything.

It has an opaque durable identifier tied to exactly one MessageIntent, one selected channel/provider operation and the exact content/locale binding used. A replay of the identical provider operation may use the same attempt identity only where the selected provider contract proves it is the same operation. Every new external submission operation is a new DeliveryAttempt. Provider retries are never new MessageIntents.

No DeliveryAttempt is created for local validation, rendering, queueing, rate/policy rejection or any other failure before the final durable attempt-admission cutover. At that cutover, create the attempt for one concrete provider call with its safe operation identity, then make the call. This is the last durable step before external I/O and serialises concurrent executors. Do not hold an authoritative database transaction open across provider I/O. If a crash leaves it unclear whether the call began, treat the attempt outcome as unknown. If the system can prove the provider invocation did not begin, close that admission as not submitted and allow safe same-intent admission later.

The attempt's side effect is one external provider/channel submission operation. It never changes Identity, Content & Media or Privacy truth. A provider observation may later update only this attempt's delivery evidence.

### 6.2 Required concepts and outcome states

An attempt carries the minimum information needed to identify and reconcile its operation:

- attempt and MessageIntent identifiers;
- bounded channel/provider route value selected under the later OQ-036 policy;
- exact content/locale version reference used;
- safe provider operation/idempotency reference where supported;
- admission and submission timing;
- one normalised outcome plus minimal authenticated evidence identifiers and observation times;
- conflict/reconciliation facts where observations disagree.

The provider outcome is separate from MessageIntent dispatch, attempt admission, source validity, content eligibility and capability validity:

| Outcome | Meaning and retry effect |
|---|---|
| rejected_before_submission | The provider conclusively confirms the concrete submission request was rejected before message acceptance or delivery. This attempt is terminal. A same-intent attempt is possible only after all other guards pass. |
| accepted | Provider accepted the operation. This does not prove delivery. Do not submit again while it may still deliver. |
| delivered | Provider establishes this delivery observation. It is delivery evidence only. |
| bounced_or_failed | Provider establishes non-delivery/failure for this attempt. Any retry still needs fresh source and content checks and a safe policy decision. |
| unknown | The operation may have occurred but its outcome is unresolved. This is not retryable failure. No new attempt or failover is admitted. |

Before any provider observation, the attempt remains admitted with outcome pending. An accepted attempt remains accepted and pending if later delivery evidence is absent; it does not regress to unknown and cannot be resubmitted. It may later receive delivered or bounced_or_failed evidence. An unknown outcome may be resolved only through reconciliation evidence. These transitions update the same attempt. A callback does not create another attempt.

~~~text
admitted / pending → rejected_before_submission | accepted | unknown
accepted → delivered | bounced_or_failed
unknown → reconciled rejected_before_submission | accepted | delivered | bounced_or_failed
rejected_before_submission / delivered / bounced_or_failed → terminal for this attempt
~~~

### 6.3 Guards, terminal states and evidence handling

- Create an attempt only after source eligibility, destination, content/locale eligibility and provider admission checks pass.
- Only one executor may hold an active attempt admission for an intent at a time. The concurrency guard ends before network I/O.
- A definitive no-submission/no-delivery outcome is required before another external operation is safe. Unknown and accepted-but-unresolved outcomes block retry and failover.
- An attempt becomes terminal when its final outcome is known. Unknown remains unresolved, not terminal.
- Reconciliation attaches minimal normalised evidence to the existing attempt. It does not create a DeliveryReconciliationCase, provider-event Resource or new MessageIntent.
- Reconciliation uses authenticated provider callbacks or a provider status/evidence path selected under OQ-036, matched to the safe operation reference. An authorised operator may record verified provider-side evidence through the same Communications boundary. If no authoritative evidence can resolve the operation, the attempt remains unknown and requires attention.
- Authenticated duplicate callbacks are idempotent. Reordered callbacks may add evidence but may not regress stronger known evidence. A contradiction is preserved and surfaced for attention rather than resolved by arrival order.
- Stale evidence is attached to its original attempt and cannot overwrite a newer attempt’s details. If late evidence contradicts a prior retry admission, stop further attempts and flag the intent for reconciliation.
- Raw provider payloads, bearer material and secret-bearing URLs are not retained in ordinary Communications evidence.

## 7. Source roles and destination provenance

canonical account email != Communications delivery provenance.

For each intent, the destination provenance is the exact address Identity authorised for that source role and operation. Communications preserves that value for the delivery lifetime; it does not re-resolve "current Account email" on retry.

- Verification, reset and recovery use the destination authorised when their specific challenge/operation was issued.
- New-address confirmation uses the pending new address for that email-change operation.
- Old-address notice uses the old canonical address captured before the change.
- A security notice uses the destination authorised for its exact Identity transition.

New-address confirmation and old-address notice are different obligations. They have different purposes, source-event meaning, recipients and message roles. They never merge because they belong to one email-change workflow.

Identity remains authoritative for whether the exact role/source is eligible to send. Destination provenance does not transfer canonical-email authority to Communications. If the source changes, is superseded, revoked, expires or is consumed, Communications must not silently retarget the existing intent. Any new recipient or proof requires a new Identity-authorised source obligation.

## 8. Protected delivery capability

The protected delivery capability is sensitive delivery machinery that exists only to reproduce an already-authorised proof-bearing communication. It is not an Identity proof or a business Resource.

It must:

- be protected/encrypted at rest using an already approved protected-secret mechanism;
- be inaccessible through ordinary Resource reads and recoverable only by the purpose-scoped delivery executor;
- bind to exactly one MessageIntent and the corresponding Identity proof/source purpose;
- expire no later than the underlying Identity proof;
- remain recoverable only while a permitted retry/reconciliation obligation needs it;
- become immediately inaccessible when send authority ends, then be cleared or rendered irrecoverable; and
- remain out of jobs, logs, telemetry, Audit, Analytics and ordinary operator displays.

It cannot verify an Account, complete recovery, confirm/apply an email change, or change canonical email. Do not choose an encryption package, key manager or exact persistence representation here.

## 9. Must-not-lose handoff and durable execution

For every in-scope Identity-caused obligation that current authority requires, including verification, password reset, recovery, new-address confirmation, old-address notice and bounded security/account notices, the handoff is:

~~~text
authoritative Identity transition / challenge issuance
→ durable Communications MessageIntent
→ bounded protected delivery capability for bearer-bearing roles, where required
→ commit
→ discoverable durable Communications execution
→ DeliveryAttempt
→ retry, reconciliation or terminal delivery result
~~~

The authoritative Identity transition/source event and its MessageIntent must commit atomically or fail closed. Any required protected capability also commits atomically for bearer-bearing roles only. A committed source obligation must not silently lose its delivery obligation. The Identity owner invokes the Communications-owned intent boundary; no Domain directly writes another Domain’s persistence. A post-commit callback or Sender return value alone is not sufficient evidence of the handoff.

Provider I/O occurs after the authoritative transaction commits. Durable job/executor arguments contain only non-secret identifiers and bounded routing metadata. They never contain bearer tokens, protected capability values or rendered secret-bearing URLs.

PostgreSQL is the default durable structured authority. Oban may be the default durable executor under current Architecture and Operating Model. An Oban job, job uniqueness, PubSub message or LiveView process is not the MessageIntent or business idempotency authority. A committed intent remains discoverable and recoverable if a job is lost, duplicated, delayed or recreated. PubSub and LiveView may improve freshness only.

If a future implementation cannot establish the atomic handoff or recover a committed intent independently of one job, stop and return to the owning authority. Do not weaken the invariant by adding an ungoverned third Resource or generic event bus.

## 10. Content and locale binding

Content & Media owns governed message/template body versions, locale versions, approval, publication, correction and withdrawal. Communications owns the exact binding used for one delivery operation.

Before the first external submission, bind the MessageIntent to the exact currently eligible Content & Media content version and locale version. Capture the intended locale from the authorised source context. Core registration, authentication, onboarding, terms/privacy and applicable safety communication retain the approved Afrikaans and English obligations in Product Law. Send the intended eligible locale; do not send duplicate copies in both languages or silently fall back to an unapproved translation.

Retry never dereferences "latest". The intent and each attempt retain the exact version reference used. A content correction or withdrawal does not rewrite a prior binding or attempt:

| Timing of correction/withdrawal | Required handling |
|---|---|
| Before any external submission | Hold the intent if its binding is no longer eligible. Bind an explicitly eligible successor version before submission and preserve the prior binding fact. |
| After a confirmed non-delivery attempt | A successor may be bound and retried under the same intent only if source eligibility remains current and the provider outcome is conclusive. Preserve the old attempt and its content reference. |
| During an unknown/ambiguous outcome | Do not rebind and do not submit again. Reconcile the prior provider operation first. |
| After an accepted or delivered operation | Do not rewrite the submitted content provenance. Any required correction communication comes from a new source-authorised obligation. |

A change to the semantic role is not a content rebind. It requires a new source-authorised obligation. Content withdrawal/correction decisions remain with Content & Media. A provider’s inability to cancel an already accepted operation does not change Content or Identity authority.

## 11. Admission, retry and reconciliation rules

Before every new provider submission capable of sending protected material, Communications must freshly re-read Identity’s non-secret, role-specific source eligibility contract. The check covers the exact source operation/challenge and current proof/source state. No cached source-validity result grants retry authority.

A new attempt is admissible only when all applicable conditions hold:

1. The MessageIntent remains open and no prior provider operation is accepted-but-unresolved or unknown.
2. Identity currently permits this exact source and semantic role.
3. The original destination remains the authorised destination for that obligation.
4. The exact content/locale version is currently eligible, or a safe explicit successor binding has been recorded.
5. The protected capability remains available and within its own expiry, where required.
6. The later governed channel/provider policy permits this submission.
7. Attempt admission is concurrency-safe and durable before provider I/O.

A retry after known non-delivery is the same MessageIntent and creates a new DeliveryAttempt for a new provider operation. A repeated transmission of an already identified operation remains the same attempt only when the provider’s selected contract proves that identity. A participant resend with a new Identity challenge is a new MessageIntent.

Provider ambiguity is a correctness problem:

- timeout after possible submission, crash across the submission/result boundary, or an unclassified provider response yields unknown;
- no blind retry, alternate provider or failover is allowed while an attempt is unknown or accepted but unresolved;
- reconciliation must establish either that no provider operation/delivery occurred, or that the existing operation was accepted/delivered/failed;
- only conclusive non-delivery can make a later submission eligible, subject to all other current guards;
- accepted-only evidence remains accepted and pending. It continues to block retry and failover until conclusive non-delivery is established; accepted evidence alone never makes another submission safe;
- if authoritative reconciliation is unavailable, keep the intent ambiguous and require attention; do not manufacture success or duplicate the message.

The exact retry count, delay/backoff, launch channel/provider policy, failover product, provider callback schema and vendor are reserved to OQ-036. A release provider must satisfy these frozen semantics.

## 12. Concurrency and crash behaviour

| Race or failure | Required result and recovery path |
|---|---|
| Duplicate Identity source handoff | Source-operation/role idempotency recognises one MessageIntent. Required intent/capability failure aborts the must-not-lose commit. |
| Concurrent executor runs | Durable attempt admission serialises one external operation per intent. Losers re-read the intent and current guards. Job uniqueness is not the invariant. |
| Retry races Identity expiry, revocation, supersession or consumption | Identity eligibility is checked at admission. If invalidation wins first, no attempt. If admission wins first, an already-started external call cannot be recalled; later Identity use still fails current Identity validation. Clear capability when authority ends. |
| Retry races destination/source change | Existing intent keeps its authorised destination and source reference. It never retargets. A changed source requires a new Identity operation and intent. |
| Participant resend races old provider attempt | New challenge creates a new intent. Old intent cannot retry after supersession. An already-submitted old message may arrive, but its proof cannot be consumed. Old ambiguity or acceptance blocks only the old intent; the new intent is independently admitted against its own current Identity source. No account- or destination-wide lock or dedupe key may merge or block the two obligations. |
| Provider timeout or response lost | Mark the admitted attempt unknown; reconcile that operation before any new submission. |
| Crash before first provider attempt | The committed intent remains discoverable. Rebuild/recreate durable execution from the intent; no DeliveryAttempt exists unless provider submission admission began. |
| Crash after durable attempt admission but before provider invocation is known to have begun | If recovery can prove invocation never began, close the admission as not submitted and allow a fresh admission after all guards pass. Otherwise treat it as unknown and reconcile before any new submission. |
| Crash after provider submission but before local result persistence | Recover the existing attempt as ambiguous and reconcile by its safe operation reference/evidence. Do not submit again. |
| Duplicate or reordered provider callbacks | Authenticate, deduplicate and attach minimal evidence to the same attempt. Preserve stronger evidence and never use arrival order to regress it. |
| Late evidence from an older attempt after a newer attempt exists | Attach to the older attempt. If it conflicts with the reason a newer attempt was admitted, freeze further sends and require reconciliation. |
| Content correction/withdrawal races with delivery | Revalidate eligibility before attempt admission. If correction wins, hold/rebind before submission; if admission wins, preserve that attempt’s exact version and handle any correction as a new authorised obligation. |
| Restart while protected capability remains required | Reconstruct the intent and attempt from PostgreSQL; re-read Identity and Content authority before submission; recover capability only through the restricted executor. |
| Terminal source or delivery boundary | Disable capability access immediately, clear/render it irrecoverable, stop retries and retain only the minimal ledger evidence still required by retention authority. |
| Account closure, full deletion or later reactivation | Apply Identity's current role/source disposition and Privacy's current deletion, suppression and retention contract. Closure is not inferred to be full deletion. Reactivation alone never reopens a closed intent or restores an old proof/capability. Eligible pending sends stay suppressed until their owner disposition permits them. |
| Backup/PITR restore | Keep provider egress and restored jobs gated. Replay current privacy/deletion/withdrawal suppression, reconcile Communications and critical source state, and pass semantic authority checks before service resumes. Recreate execution only for still-open intents after fresh Identity and Content checks; do not replay historical jobs or blindly retry ambiguous attempts. |

The attempt-admission check is the send-authority linearization point. A later source invalidation cannot turn an already admitted external operation into proof authority. The explicit participant action still revalidates current Identity state and consumes proof exactly once.

## 13. Scanner-safe proof consumption

Communications may deliver a participant-facing link. Communications, the provider, a browser, a scanner, a gateway or a preview does not consume the proof.

For all four protected bearer purposes: verification, password reset, recovery and new-address email-change confirmation:

~~~text
passive retrieval / HEAD / GET / scanner / preview / unfurl / prefetch
→ no Identity mutation and no proof consumption

explicit participant action
→ fresh Identity proof and source-state validation
→ guarded Identity state-changing action
→ proof consumed exactly once
~~~

The confirmation action is the existing Identity-owned state-changing boundary. This dossier creates no second proof-consumption endpoint and no success inference from provider delivery, successful token parsing, page load or UI state.

## 14. Security, privacy, audit and observation

Required FP-001 Identity communications are security/account communications, not marketing. Minimise payloads. Do not require open/click tracking. Do not allow provider click-tracking rewrites of protected URLs. Use only the protected capability path for bearer material.

Communications owns the delivery facts needed for its own retry, status and reconciliation authority. Audit & Evidence receives only the minimum restricted evidence explicitly required by current authority, such as an authorised source/role reference, result class, actor/reason for privileged delivery-side action and a safe correlation reference. Do not copy bearer material, rendered secret URLs, full rendered bodies or raw provider payloads into Audit.

Logs, traces, metrics, Analytics, PubSub and dashboards remain non-authoritative and secret-safe. Use bounded, minimised outcomes and safe correlation. Do not use raw destination, bearer data, message body or high-cardinality participant identifiers in normal telemetry.

## 15. Operator and participant presentation boundary

Operators may observe the Communications ledger and perform only explicitly authorised delivery-side retry or reconcile actions through Communications-owned operations. Every action rechecks current source, content, destination, capability and ambiguity guards, and emits only the restricted evidence required by current authority.

Operators cannot revive Identity proof, change canonical email, override Content eligibility, restore Privacy permission, bypass provider ambiguity, manufacture provider success or create a second business authority. No generic OperatorAction, SupportCase, Incident or work/task Resource is created.

Required operational presentation distinguishes:

- **Pending:** durable intent exists, but no provider completion is established; may be queued, held for a current prerequisite, or accepted and awaiting outcome.
- **Failed:** delivery cannot continue under the bounded current policy, and no unresolved provider ambiguity remains.
- **Ambiguous:** an external operation may have occurred and cannot yet be resolved. No retry or failover is available.
- **Requires attention:** safe automatic delivery/reconciliation is unavailable, evidence conflicts, a required capability was lost early, or a governed owner decision is needed.

Participant-facing status uses honest pending, complete, invalid/expired, temporarily unavailable or safe next-action outcomes from the owning Identity contract. It never exposes provider internals or turns a delivery receipt into identity success. Frontend state remains presentation state, not proof authority.

## 16. Retention, cleanup and data temperature

Active MessageIntents and DeliveryAttempts remain in PostgreSQL while needed for execution, retry, reconciliation and terminal visibility. Querying and recovery are bounded by the active intent/attempt state.

The ledger retains the minimum causal and delivery evidence required by Communications. Retain attempt evidence while an intent can retry or needs reconciliation. Do not delete an ambiguous attempt. Once no retry, reconciliation or terminal-visibility need remains, keep only minimal normalised evidence under the applicable Privacy retention/disposition contract and remove any unnecessary recipient detail. Exact retention periods, deletion schedules, legal holds and deletion orchestration remain Privacy & Consent authority and applicable existing gates. Privacy does not shared-write Communications records.

The protected capability has the shorter, strict boundary: clear or make irrecoverable as soon as retry authority ends and never later than Identity proof expiry, revocation, supersession or consumption. Cleanup must be idempotent and safe after restart. Cleanup failure cannot restore send authority.

On backup/PITR restore, Communications outbound delivery remains recovery-gated until the current privacy/deletion/withdrawal suppressions, critical Communications/Identity reconciliation and semantic authority checks have completed. Restored jobs and capabilities cannot resume from the historical snapshot alone. Rebuild execution only from current, still-open MessageIntents after checking current Identity and Content eligibility. An unknown or accepted-but-unresolved attempt stays blocked pending reconciliation.

Account closure follows Identity's closure disposition and does not itself mean full deletion. Full deletion and any applicable suppression, retention, legal-hold or external-processor requirements follow Privacy & Consent's current owner contract. Communications applies that disposition to pending delivery and protected capability, preserves only evidence that remains authorised, and does not infer permission to send from later Account reactivation. Exact deletion periods, policy and orchestration remain with Privacy & Consent and the current deletion/restore gates.

PostgreSQL is the structured authority. Oban is an optional/default execution mechanism under current Architecture and Operating Model, not authority. PubSub may update operational freshness only. No Redis, ETS, Cachex, custom GenServer, separate queue, vendor-specific data store or cache is required by this contract. Exact resource/action performance mapping remains subject to the current Phase 7B/OQ-039 process; this dossier selects no performance number or infrastructure topology.

## 17. Conditional-dossier impact

This is an explicit impact assessment for the Communications seam only. It does not complete the programme-wide Open Work adjudication.

| Conditional dossier | Communications finding | Why this narrow contract does not newly force it |
|---|---|---|
| Privacy & Consent | No new JIT dossier is forced by required FP-001 Identity messages. | They are mandatory security/account obligations, not marketing. Privacy remains owner of purpose permission, withdrawal, retention and deletion. The dossier delegates those existing truths and creates no optional campaign or accountless-contact flow. |
| Content & Media | No new JIT dossier is forced by this delivery contract. | Current Product Law and Domain Law already require Content ownership, bilingual eligible versions, correction/withdrawal lifecycle and exact version provenance. Communications consumes the owner’s exact eligible version. It does not invent Content Resource topology. |
| Audit & Evidence | No new JIT dossier is forced by this delivery contract. | Existing authority already separates Communications delivery ledger from minimum restricted central evidence and bars Audit from becoming business truth. No new Audit-owned lifecycle is introduced. |
| Analytics | Not required. | Analytics is unnecessary for delivery correctness, proof consumption, provider reconciliation or FP-001 completion. |

Open Work v1.2.57 still records Privacy & Consent, Content & Media and Audit & Evidence as CONDITIONAL / PENDING EXPLICIT ADJUDICATION, with Analytics NOT REQUIRED. This dossier does not close, change or imply completion of that programme-wide gate. Its impact findings are evidence for the separately governed adjudication.

## 18. OQ-036 and downstream boundary

OQ-036 remains unresolved and release-only. This dossier freezes provider-independent business semantics. It selects no:

- email vendor or provider;
- in-app implementation;
- SMS/WhatsApp provider;
- provider failover product or launch channel/provider policy;
- retry count, delay or backoff;
- provider-specific idempotency API or webhook schema;
- encryption package, key-management product or protected-storage representation;
- queue/worker names, database migration or infrastructure topology.

No Phase 7C Final Feature Pack Contract is created or approved. Proof classification is not finalised. No TB, VS, HH, TOON, Phase 8 or application implementation is authorised. OQ-035 and other release/security/operations gates keep their current authority and status.

## 19. Proof pressure for future executable evidence

No proof is performed or classified here. Future evidence must demonstrate:

1. Atomic source transition/event and MessageIntent creation for every required in-scope Identity communication role, plus protected-capability persistence for bearer-bearing roles. Failure must leave no committed source without its durable obligation.
2. No bearer token or secret-bearing URL in durable jobs, logs, telemetry, Audit, Analytics or ordinary operational views.
3. Restart-safe discovery and retry after a committed intent, including when an execution job is lost or duplicated.
4. Expiry, revocation, supersession and consumption block stale delivery for every protected purpose.
5. Duplicate source handoff and duplicate executor runs preserve one logical obligation and do not multiply provider operations.
6. Unknown provider outcome blocks blind retry and failover until reconciled.
7. Provider acceptance, delivery, bounce or failure never establishes Identity verification, recovery completion, email-change confirmation or proof consumption.
8. Passive HEAD, GET, scanner, gateway, preview, unfurl and prefetch retrieval remains non-consuming for verification, reset, recovery and new-address email-change confirmation.
9. New-address confirmation and old-address email-change notice preserve separate source roles and destination snapshots.
10. Protected material becomes inaccessible and is cleared/irrecoverable when retry authority ends, no later than the source proof boundary.
11. Duplicate, stale, contradictory and reordered callbacks remain idempotent and cannot regress stronger evidence or overwrite a newer attempt.
12. Each attempt retains exact Content & Media content/locale provenance; correction and withdrawal races do not rewrite prior attempt history.
13. Crash recovery is bounded at intent commit, execution scheduling, attempt admission, provider submission, outcome persistence and callback processing.
14. A late callback from an older attempt cannot silently change the outcome of a newer attempt or infer Identity success.
15. Source change and resend races produce a new intent for a new Identity challenge; the old intent cannot revive superseded proof.
16. Operator retry/reconcile actions cannot bypass Identity, Content, Privacy or ambiguity guards.
17. Backup/PITR restore blocks provider egress and restored job replay until current suppression, critical reconciliation and semantic authority checks pass.
18. Account closure, full deletion and reactivation apply current owner disposition without replaying stale or deleted obligations.

## 20. STOP conditions and review handoff

Stop and return to the named upstream owner if review or later implementation reveals:

- Product, Architecture, Domain or Roadmap contradiction;
- shared-write ownership or a required mutation outside the owning Domain contract;
- need to change Identity proof purpose, validity, expiry, revocation, supersession, consumption or email-change semantics;
- need to change Content & Media ownership or publication eligibility;
- need to resolve OQ-036 to state the provider-independent business contract;
- a third durable Communications Resource is unavoidable without current authority and FP-001 need;
- a conditional-dossier requirement cannot be answered by current upstream law;
- accountless mailing-list acquisition, optional marketing or another out-of-scope communication purpose is proposed under this FP-001 contract;
- atomic must-not-lose delivery cannot be preserved with the approved authority boundary; or
- completion would require silently advancing Phase 7C, proof classification, Phase 8 or application implementation.

### Review handoff

This candidate freezes the narrow FP-001 Communications contract for two durable Resources, source-operation/role idempotency, immutable destination provenance, exact eligible content/locale binding, real provider-attempt evidence, unknown-outcome reconciliation, atomic must-not-lose handoff, protected bearer handling, scanner-safe Identity consumption, operator limits and restart/concurrency behaviour.

It leaves programme-wide conditional-dossier adjudication pending, preserves OQ-036 as unresolved/release-only, and does not authorise Phase 7C, proof classification, Phase 8 or application implementation. Reviewers should check the ownership seams, the separate source/provider/capability/content dimensions, the crash and race outcomes, and the exact source trail below.

### Provenance trail

#### Current authoritative sources

The current authority files and exact versions are listed in §1.2. Their material sections are named there. The current Open Work and manifest, not the Delivery Atlas, control lifecycle and source routing.

#### Certified FP-001 working contracts

- docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md, §§5-8, 10, 12-17.
- docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md, §§I-J, J.1, J.1a, R-U, X-AA.
- Current lifecycle and certification route: docs/00_platform/02_OPEN_WORK_v1.2.57.md, §12.14.

#### Non-authoritative Communications evidence

- docs/00_platform/working/communications/README.md, read order and scope warning.
- docs/00_platform/working/communications/NEWYOU_COMMUNICATIONS_PREJIT_DISCOVERY_WORKING_v0.10.0.md, §§1-3 and 6-9, used only to locate and revalidate old blocker claims and compare the compact model.
- The Pre-JIT register, scenario labels and conclusions are not cited as authority and are not promoted into this dossier as governing identifiers.

#### Historical evidence

- Current Open Work v1.2.57 §12.14 records PR #76 candidate certification/post-merge evidence and PR #77 current-status promotion.
- docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md and docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md are historical Identity artifacts only. They do not override v0.1.4.
- The Pre-JIT v0.10.0 authority pin is historical baseline context, not current repository authority.

#### External technical research

None was required. This candidate chooses no current provider, vendor, package, encryption product, callback schema or implementation technology.

### Candidate final state

~~~text
PROPOSED PATH / VERSION: docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md / v0.1.0
CANDIDATE: REVIEW-READY / NOT CERTIFIED / NOT CURRENT
COMMUNICATIONS RESOURCES: MessageIntent + DeliveryAttempt
COMM-UPD-001 / COMM-UPD-002: REVALIDATED AGAINST CURRENT IDENTITY v0.1.4; RESOLVED / CERTIFIED / CURRENT THERE
CONDITIONAL DOSSIERS: IMPACT ASSESSED HERE; PROGRAMME GATE STILL PENDING EXPLICIT ADJUDICATION
OQ-036: UNRESOLVED / RELEASE-ONLY
PHASE 7C: NOT CREATED OR AUTHORISED
PROOF CLASSIFICATION: NOT FINALISED
PHASE 8 / APPLICATION IMPLEMENTATION: NOT AUTHORISED
~~~
