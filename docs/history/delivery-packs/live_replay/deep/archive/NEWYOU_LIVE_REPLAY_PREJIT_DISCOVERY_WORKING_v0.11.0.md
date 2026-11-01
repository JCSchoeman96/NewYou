# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.11.0.md

- **Status:** WORKING / NON-AUTHORITATIVE DISCOVERY
- **Document version:** v0.11.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.10.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted register predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.8.1.md`
- **Accepted register commit:** `aaa9e97cb29a0f4499fcb5bf88691bb2863686d7`
- **Pass:** K
- **Focused semantic class:** participant communications around live/replay lifecycle events
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE

---

# 1. Pass-K bounded question

This pass asks only:

> **Which participant-facing communications around live/replay lifecycle events are actual governed obligations, which are optional/promised journeys, and how must source truth, message intent, delivery evidence and failure visibility remain separated across registration/join, reschedule/cancellation, replay availability, correction/withdrawal and deletion?**

This pass does **not** design:

- generic Communications architecture;
- a marketing campaign or journey engine;
- exact email/SMS/WhatsApp/push provider selection;
- message wording, branding or templates;
- exact quiet-hour/frequency-cap policy;
- reminder schedules;
- exact operator UI/dashboard layout;
- exact Ash Resource/action/schema/job topology;
- exact destination-resolution implementation;
- social/promotional campaign distribution;
- event-commerce/ticket notices;
- generic account/security communications;
- a new Product notification taxonomy;
- a new Roadmap Feature Pack.

The pass must reuse the existing Communications ownership and durable-delivery doctrine rather than rebuilding it inside Live & Replay.

---

# 2. Authority baseline

## 2.1 Communications never becomes live/replay source authority

Accepted Pass-A discovery already separated Communications from occurrence truth, and current Domain Law preserves that boundary.

Events & Live owns live-session/event scheduling, registration/capacity, occurrence/policy and attendance truth. Communications is integrated for reminders/changes but does not gain write ownership over those facts.

Therefore:

```text
message says registered       != registration truth
message says rescheduled      != reschedule truth
message says cancelled        != cancellation truth
message says replay available != replay publication/access truth
message says withdrawn        != withdrawal truth
```

A late, duplicate, bounced, delayed or failed message cannot create, undo or repair the source lifecycle fact.

## 2.2 Roadmap makes promised notification journeys conditional

Current FP-007 Roadmap routing states:

- `OQ-036 — BLOCKS_THIS_FP` **for any promised live notification journey**;
- the live capability itself cannot assume an unapproved provider/channel;
- `OQ-017 — NON_BLOCKING_FOR_THIS_FP` until reminder delivery is an actual governed promise.

The Roadmap exit also requires **notification failure to be visible**.

The coherent reading is not “every imaginable participant message is mandatory.” Instead:

> the future FP-007 Final Contract must enumerate any included/promised outbound journeys; where a governed communication obligation exists, failure must be visible and the applicable delivery/provider gate must be satisfied.

The exit-condition wording does not itself enumerate registration confirmation, reschedule, cancellation, reminder or replay-available messages.

## 2.3 Protected joining instructions are required, outbound email is not inherently required

`DEC-186 — Live-session access` is LOCKED and requires:

- entitlement-aware registration;
- capacity/waitlists where applicable;
- **protected joining instructions**;
- privacy-preserving attendance.

This is a secure-access requirement, not by itself a mandate that an email must carry the instructions.

The instructions may be surfaced through a currently authorised protected application path if the Final Contract allows that participant experience. If an outbound communication carrying or pointing to joining instructions is explicitly promised, its communication path becomes subject to `OQ-036` and the normal Communications delivery contract.

A delivered join link/instruction never becomes durable entitlement authority.

## 2.4 Reminder mechanics remain separately gated

`OQ-017 — Reminder delivery design` remains ARCHITECTURE / OPERATIONS REVIEW and owns reminder-specific channel/scheduling/retry/quiet-hour details.

Because the Roadmap explicitly keeps it non-blocking until reminders are promised, this pass must not turn a desirable pre-session reminder into a required FP-007 outcome.

## 2.5 Product correction law creates stronger notification obligations

The generic correction vocabulary accepted in Pass I matters here because current Product Law already says:

- material corrections create an approved superseding version and **notify affected participants where appropriate**;
- safety corrections withdraw affected use immediately, identify impacted uses, **notify participants**, replace content where possible and create an incident record.

Therefore replay-correction communications are not all optional:

```text
minor editorial correction
→ no blanket participant-notification requirement identified here

material content correction
→ notification required where the governing owner determines it is appropriate for affected participants

safety correction
→ participant notification is an explicit Product consequence

legal_or_consent_correction / full withdrawal
→ exact participant-notice duty remains purpose/legal/privacy/OQ-021 dependent unless another current authority requires it
```

Communications does not decide whether a material correction is notification-worthy or who is affected. That decision belongs with the governing source authority/JIT contract.

## 2.6 Mandatory product/safety notices are not marketing

Current Domain Law separates marketing permission/preferences from product/safety mandatory notices.

A marketing opt-out therefore cannot silently suppress a source-authorised mandatory safety notice. Conversely, an optional reminder cannot masquerade as a mandatory notice to bypass applicable preference/quiet-hour policy.

Purpose class must be explicit.

## 2.7 Architecture supplies the must-not-lose consequence contract

Architecture §8.2 defines a Class-B mandatory durable asynchronous consequence:

```text
authoritative transaction
→ establish durable execution intent atomically
→ commit
→ execute consequence
→ repeat-safe/idempotent handler
→ re-read/revalidate current preconditions
→ success / retry / terminal-visible state
```

Provider/network I/O is not performed while holding the authoritative source transaction.

Architecture §8.4 also states that best-effort realtime/PubSub observations cannot substitute for mandatory delivery.

Accordingly:

> once Product Law or the Final Feature Pack Contract creates a must-not-lose participant communication obligation, that obligation requires durable consequence semantics; a fire-and-forget PubSub event or ephemeral queue side effect is insufficient.

The exact cross-domain handoff representation remains JIT/proof detail. This pass does not require the source Domain to shared-write Communications persistence.

## 2.8 Existing Communications working model is reusable supporting evidence

The current non-authoritative Communications Pre-JIT consolidation is stable and broad discovery is parked. Its relevant working conclusions are:

- `MessageIntent` = one logical communication obligation anchored to a source operation + communication role;
- `DeliveryAttempt` = one real provider/channel submission operation and its evidence;
- source validity and delivery state are orthogonal;
- provider acceptance/delivery never establishes the source business outcome;
- unknown provider outcome is first-class and not equal to retryable failure;
- destination provenance is exact/minimised/event-correct;
- current owner predicates are revalidated before a new provider operation;
- content/locale binding is exact and governed;
- OQ-036 may remain a later provider/release gate after provider-independent semantics are frozen.

Pass K reuses this evidence but does not make the working Communications pack authoritative for FP-007.

---

# 3. Semantic dimensions kept separate

Pass K keeps at least these dimensions independent:

1. source occurrence/registration fact;
2. source schedule/cancellation version;
3. current entitlement/access fact;
4. replay publication/current-version fact;
5. correction/withdrawal fact;
6. Privacy/Full-Deletion authority;
7. whether a communication obligation exists;
8. logical `MessageIntent` truth;
9. destination/content/locale delivery provenance;
10. provider/channel `DeliveryAttempt` evidence;
11. terminal delivery outcome/failure visibility;
12. participant engagement/open/click evidence;
13. operator/audit evidence.

Forbidden collapses include:

```text
message delivered => source transition happened        [false]
message failed    => source transition rolled back      [false]
provider accepted => participant received message       [false]
provider delivered=> participant saw/understood message [false]
marketing opt-out => suppress every mandatory notice    [false]
registration      => reminder automatically required    [false]
replay published  => replay-available email required    [not established]
old join link     => old access remains authorised       [false]
PubSub event      => mandatory notice durably exists     [false]
```

---

# 4. Working communication-obligation classes

This is a planning classification, not a new governed enum.

## 4.1 Source-access surface

Example: protected joining instructions required by DEC-186.

The Product requirement is that the participant has a protected, currently authorised way to obtain/use the joining instructions. Outbound notification is a separate question.

## 4.2 Optional operational communication

Examples may include registration confirmation, pre-session reminder, reschedule/cancellation notice or replay-available notification when the Final Contract does not promise them.

These do not become must-not-lose obligations merely because they are good UX ideas.

## 4.3 Explicitly promised participant journey

Once the Final Feature Pack Contract promises a live lifecycle message, `OQ-036` applies to the chosen launch channel/provider path, and the obligation must have durable/visible failure semantics appropriate to its class.

Reminder-specific mechanics additionally route through OQ-017.

## 4.4 Product-mandated correction/safety consequence

Where current Product Law says affected participants must be notified, the notification is a mandatory downstream consequence. Safety withdrawal must not wait for message delivery; the unsafe/current-ineligible media state changes immediately, while the must-not-lose notification consequence proceeds durably and failure remains visible.

Material correction becomes this class once the governing owner determines that notification is appropriate for the identified affected set.

## 4.5 Legal/privacy-determined notice

For legal/consent correction, purpose withdrawal, recording/privacy remediation or deletion-related notice, the duty to notify is not invented by Communications. OQ-021/Privacy/legal authority decides the requirement; once required, Communications executes it under the appropriate durable-delivery policy.

---

# 5. Pressure tests — Pass K

## LIVE-PT-110 — Registration succeeds but registration-confirmation delivery fails

**Scenario class**  
Source truth versus optional/promised communication.

**Why it matters**  
A common implementation error is to make registration success depend on an email provider or, conversely, to hide a promised communication failure because registration itself committed.

**Authority**  
DEC-186; FP-007 Roadmap OQ-036 conditional notification gate; Events & Live ownership; Communications ownership; Architecture Class B where a must-not-lose consequence exists.

**Owning domains**  
Events & Live owns registration. Communications owns any resulting message intent/attempt/delivery evidence.

**Preconditions**  
Participant is eligible to register; occurrence exists; registration succeeds; outbound confirmation is either excluded or explicitly included by future FP-007 scope.

**Timeline**

1. Events validates registration rules.
2. Events commits registration.
3. If confirmation is a governed promised journey, a durable communication consequence is established.
4. Communications attempts delivery.
5. Provider rejects/bounces/times out or later reports failure.

**Expected invariants**

- registration remains true despite message failure;
- message delivery cannot manufacture or cancel registration;
- if no confirmation journey was promised, absence of a MessageIntent is not a delivery failure;
- if promised, terminal failure is visible/reconcilable and OQ-036 applies;
- retry remains the same logical obligation unless source semantics create a genuinely new obligation.

**Questions**

- Is registration confirmation in the future Final Contract?
- Is the participant able to reconstruct current registration state in-app even when delivery fails?

**Adversarial variants**

- duplicate registration request;
- provider accepts then callback is lost;
- participant changes email after registration;
- provider delivers after occurrence has been cancelled.

**Analysis**  
No current FP-007 Product/Roadmap wording found makes registration-confirmation messaging universally mandatory. Events truth must not be coupled to provider delivery. If the Final Contract promises confirmation, that promise activates the Communications gate and must-not-lose/terminal-visible semantics.

**Disposition**  
`PASS_WITH_REFINEMENT / JOURNEY_SCOPE_DEPENDENT`

**Proof route**  
`FP007_FINAL_CONTRACT → EVENTS_JIT → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → FAILURE/RECONCILIATION_PROOF`

**UPD**  
None.

**Evidence needed**  
Source→intent idempotency; terminal delivery failure visibility; registration remains independently queryable/current.

---

## LIVE-PT-111 — Protected joining instructions are available in-app but outbound delivery fails

**Scenario class**  
Required access surface versus communication channel.

**Why it matters**  
DEC-186 requires protected joining instructions, but conflating that requirement with email delivery would create unnecessary provider authority and availability coupling.

**Authority**  
DEC-186; Architecture protected delivery/current-authority rules; FP-007 OQ-036 conditional gate.

**Owning domains**  
Events & Live / Entitlements own the source access requirements; Communications owns any outbound delivery; provider remains evidence/execution only.

**Preconditions**  
Participant has current join access; protected application surface can reveal bounded/current instructions; optional/promised outbound message also exists.

**Timeline**

1. participant registers or otherwise qualifies;
2. current entitlement/admission permits join;
3. protected application surface exposes current joining instructions;
4. outbound message attempt fails.

**Expected invariants**

- required joining-instruction availability is not automatically defeated by email failure if a valid protected participant surface remains;
- a delivered old link cannot preserve access after revocation;
- provider message state is not admission authority;
- if outbound delivery is itself promised, its failure is still visible even though the participant can join another way.

**Questions**

- Does the Final Contract promise outbound join delivery or only protected availability?
- Are joining capabilities short-lived/current-authority checked rather than durable bearer entitlement?

**Adversarial variants**

- message arrives after entitlement revocation;
- participant opens an old message after provider replacement;
- app surface is temporarily unavailable but email succeeds;
- both channels fail.

**Analysis**  
The Product requirement is protected joining instructions, not email-as-authority. Channel choice is a delivery concern. Final Contract/JIT must define the participant experience without creating dual authority.

**Disposition**  
`PASS_WITH_REFINEMENT / ACCESS_SURFACE_NOT_DELIVERY_AUTHORITY`

**Proof route**  
`DEC-186 → EVENTS/ENTITLEMENTS_JIT → COMMUNICATIONS_JIT_IF_OUTBOUND_INCLUDED → OQ-036_IF_PROMISED → ACCESS/FAILURE_PROOF`

**UPD**  
None.

**Evidence needed**  
Current-authority join retrieval; stale-link denial; independent outbound failure visibility.

---

## LIVE-PT-112 — Pre-session reminder is never sent

**Scenario class**  
Optional reminder scope.

**Why it matters**  
Reminder UX is attractive enough that implementation teams may accidentally make OQ-017 a hidden FP-007 prerequisite.

**Authority**  
FP-007 Roadmap; OQ-017; OQ-036.

**Owning domains**  
Events & Live supplies current event fact; Communications owns reminder intent/delivery if the reminder is included.

**Preconditions**  
Occurrence is scheduled; participant is registered/eligible; no governed reminder promise has been added.

**Timeline**

1. session remains scheduled;
2. no reminder intent is created;
3. participant may still discover current session state and join through governed platform paths.

**Expected invariants**

- absence of an unpromised reminder is not an FP-007 delivery failure;
- OQ-017 remains non-blocking;
- no synthetic failure row/message intent is created for an obligation that does not exist;
- current schedule/access remains source-authoritative.

**Questions**

- Does a later Product/Final Contract add a reminder promise?
- If added, what exact reminder role and timing apply?

**Adversarial variants**

- participant assumes reminders based on previous product behaviour;
- operator manually sends an ad-hoc message;
- multiple reminder windows are proposed.

**Analysis**  
Roadmap is explicit: reminder delivery is non-blocking until promised. This pass must preserve that scope discipline.

**Disposition**  
`PASS / OQ-017_NON_BLOCKING_UNLESS_PROMISED`

**Proof route**  
`FP007_FINAL_CONTRACT → OQ-017_IF_REMINDER_PROMISED → OQ-036_CHANNEL_PROOF_IF_PROMISED`

**UPD**  
None.

**Evidence needed**  
Final Contract scope declaration only; executable reminder proof is unnecessary if excluded.

---

## LIVE-PT-113 — Registered participant receives an old schedule message, then occurrence is rescheduled

**Scenario class**  
Source-version change after historical delivery.

**Why it matters**  
Previously delivered communication is immutable historical evidence but can become stale. It must not remain current schedule authority.

**Authority**  
Events & Live ownership; accepted LIVE-UPD-001 occurrence/provider replacement seam; Domain communication-for-changes integration; Communications provenance doctrine.

**Owning domains**  
Events & Live owns reschedule/version truth. Communications owns any resulting change-message obligation/delivery history.

**Preconditions**  
Occurrence is scheduled; participant received prior schedule information; Events lawfully applies a reschedule preserving or superseding occurrence identity per current/UPD-001 authority.

**Timeline**

1. old schedule is current;
2. a message containing old schedule is delivered;
3. Events commits new schedule/version;
4. if a change notification is promised, a new logical communication obligation is created against the new source fact;
5. old delivered message remains historical evidence.

**Expected invariants**

- reschedule exists before/independently of message delivery;
- old message is not edited into new history;
- new communication binds to the exact new schedule/version/role;
- delayed old delivery cannot revert platform UI or occurrence truth;
- duplicate source event processing cannot create unlimited duplicate intents.

**Questions**

- Is reschedule notification part of the Final Contract?
- Which occurrence/version identifier anchors the message role?

**Adversarial variants**

- reschedule twice before first change notice is attempted;
- new notice provider outcome unknown;
- old provider-delayed message arrives after new notice;
- participant changes timezone between versions.

**Analysis**  
Communication is a projection/delivery of source meaning at a point in time. Source versioning and message provenance must stay explicit. No generic “latest schedule” rewrite of historical attempts is acceptable.

**Disposition**  
`PASS_WITH_REFINEMENT / SOURCE_FACT_DOMINATES`

**Proof route**  
`LIVE-UPD-001 / EVENTS_JIT → FP007_JOURNEY_SCOPE → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → REORDER/IDEMPOTENCY_PROOF`

**UPD**  
None.

**Evidence needed**  
Exact source-version provenance; duplicate/reorder handling; late-old-message test.

---

## LIVE-PT-114 — Occurrence is cancelled but cancellation delivery fails or is unknown

**Scenario class**  
Terminal source transition with communication failure.

**Why it matters**  
Cancellation must not remain contingent on provider email success, while a promised cancellation notice cannot disappear silently.

**Authority**  
Events & Live authority; FP-007 OQ-036 conditional journey gate; Architecture provider ambiguity/terminal-visible failure.

**Owning domains**  
Events & Live owns cancellation. Communications owns the cancellation-message intent/attempt/evidence if such a journey exists.

**Preconditions**  
Occurrence is cancellable; participant may have registered; future Final Contract either includes or excludes participant cancellation notice.

**Timeline**

1. Events commits occurrence cancellation;
2. future join/admission path becomes ineligible per owner rules;
3. if cancellation notice is promised, durable communication consequence exists;
4. provider outcome becomes failure or unknown.

**Expected invariants**

- occurrence remains cancelled;
- unknown delivery is not treated as delivered or safe-to-retry without reconciliation;
- failure/unknown is operationally visible when obligation exists;
- participant querying current platform state sees cancellation even if message failed;
- old joining capabilities cannot override cancellation/current access policy.

**Questions**

- Is a cancellation notice explicitly promised/required by the Final Contract or later legal/operations authority?
- What operator escalation is required for terminal failure?

**Adversarial variants**

- provider accepts before cancellation commit due a race;
- cancellation is reversed by a separate legitimate owner transition;
- message reaches participant after a replacement occurrence is created.

**Analysis**  
No current universal Product wording was found making every cancellation an outbound message promise. If included, it becomes a governed obligation; source terminality still remains Events truth.

**Disposition**  
`PASS_WITH_REFINEMENT / JOURNEY_SCOPE_DEPENDENT`

**Proof route**  
`EVENTS_JIT → FP007_FINAL_CONTRACT → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → UNKNOWN/FAILURE_PROOF`

**UPD**  
None.

**Evidence needed**  
Cancellation source truth independent of delivery; unknown outcome reconciliation; stale-link denial.

---

## LIVE-PT-115 — Previously delivered joining instructions become stale after reschedule, provider replacement or access revocation

**Scenario class**  
Stale bearer/instruction after source authority change.

**Why it matters**  
Messages are durable outside the platform. They cannot be relied upon as revocable entitlement state.

**Authority**  
DEC-186; Architecture current protected-delivery authority; accepted LIVE-UPD-001 and LIVE-UPD-004; OQ-020 as applicable.

**Owning domains**  
Events & Live / Entitlements own current access/admission; Communications owns historical delivery only.

**Preconditions**  
A participant received valid instructions while access/schedule/provider binding was current; source authority later changes.

**Timeline**

1. valid join message is delivered;
2. schedule/provider/access changes;
3. participant later uses old message/link;
4. platform/provider adapter rechecks or enforces current authority.

**Expected invariants**

- old message does not preserve revoked/obsolete access;
- provider replacement does not change occurrence identity by itself;
- protected delivery capabilities are bounded and/or current-authority checked;
- Communications is not responsible for entitlement revocation;
- historical message evidence remains truthful.

**Questions**

- Which join capability layer enforces current authority at use time?
- What provider proof is required for stale room/link invalidation?

**Adversarial variants**

- copied link shared to another participant;
- participant keeps old browser tab open;
- provider allows a stale room despite NewYou revocation;
- old message is forwarded externally.

**Analysis**  
No communication system can retract arbitrary historical email. Correctness therefore depends on source-authoritative admission and bounded provider capabilities, not on message recall.

**Disposition**  
`PASS_WITH_REFINEMENT / CURRENT_AUTHORITY_ENFORCEMENT`

**Proof route**  
`EVENTS/ENTITLEMENTS_JIT → LIVE-UPD-001/004 → OQ-020 → CONTROLLED_LIVE_ACCESS_PROOF`

**UPD**  
None.

**Evidence needed**  
Revoked/stale capability tests; provider replacement test; forwarded-link rejection/minimisation evidence.

---

## LIVE-PT-116 — Replay becomes current but replay-available notification fails

**Scenario class**  
Media publication versus optional/promised communication.

**Why it matters**  
Replay publication and replay entitlement must not be coupled to a message provider.

**Authority**  
DEC-188; Content & Media ownership; Entitlements ownership; FP-007 OQ-036 conditional gate.

**Owning domains**  
Content & Media owns current replay publication; Entitlements owns replay access; Communications owns any replay-available message.

**Preconditions**  
Governed replay is approved/published; participant has current replay entitlement where required; Final Contract may or may not promise replay-availability notification.

**Timeline**

1. replay becomes current under C&M authority;
2. participant can discover it through authorised platform state;
3. optional/promised outbound notification is attempted;
4. provider fails/unknown/bounces.

**Expected invariants**

- replay remains published/current independently of message outcome;
- entitlement remains independently evaluated;
- a failed message cannot make replay “unavailable” in source truth;
- if notification is promised, failure is visible and reconcilable;
- no replay notification obligation is inferred merely from publication unless scope/authority says so.

**Questions**

- Is replay-available notification an FP-007 promise?
- Is there an in-app current replay surface independent of outbound delivery?

**Adversarial variants**

- message queues while replay is corrected/withdrawn;
- entitlement expires before attempt;
- replay is superseded between render and provider admission.

**Analysis**  
Current authority requires governed replay, not a universal replay-available email. If promised, Communications must revalidate current source/content/access predicates before a new provider operation as applicable.

**Disposition**  
`PASS_WITH_REFINEMENT / JOURNEY_SCOPE_DEPENDENT`

**Proof route**  
`CONTENT_MEDIA/ENTITLEMENTS_JIT → FP007_FINAL_CONTRACT → COMMUNICATIONS_JIT → OQ-036_IF_PROMISED → STALE-SOURCE/FAILURE_PROOF`

**UPD**  
None.

**Evidence needed**  
Replay source state independent of delivery; queued-message invalidation/revalidation; terminal failure visibility.

---

## LIVE-PT-117 — Material replay correction after participants consumed V1

**Scenario class**  
Conditional Product-mandated correction notice.

**Why it matters**  
Product Law requires material corrections to notify affected participants where appropriate, but Communications must not decide “affected” or “appropriate.”

**Authority**  
Product correction law; accepted Pass I; Content & Media correction/version authority; Communications ownership; OQ-036 for actual launch delivery path.

**Owning domains**  
Content & Media/source governance determines correction and affected-use evidence; applicable Product/Safety owner determines notification applicability; Communications executes the resulting obligation.

**Preconditions**  
V1 was published; material correction creates approved V2; there is evidence about who was affected/eligible/consumed V1 to the extent governed and necessary.

**Timeline**

1. material correction is approved;
2. V2 supersedes V1 under C&M authority;
3. governing owner decides whether notification is appropriate and identifies the bounded affected set;
4. each required logical notification obligation is durably established;
5. Communications attempts delivery;
6. some deliveries may fail/unknown.

**Expected invariants**

- correction truth does not depend on message success;
- Communications does not infer affected participants from raw provider opens/views alone;
- once notification is required, it is not best-effort PubSub;
- source/version provenance of notification is exact;
- duplicate correction processing does not duplicate the logical obligation;
- terminal failures are visible for operator remediation.

**Questions**

- Which owner decides “where appropriate” for an FP-007 replay?
- What minimum lawful evidence defines the affected set?

**Adversarial variants**

- participant watched only the unaffected section;
- participant entitlement expired after V1 view;
- V2 is corrected again before notification send;
- provider outcome for the first notification is unknown.

**Analysis**  
The Product obligation exists conditionally. JIT must not shift that decision into Communications. Once the owner says notification is required, the consequence becomes durable Class B and OQ-036/provider proof applies to its execution path.

**Disposition**  
`PASS_WITH_REFINEMENT / AFFECTED_SET_AND_APPROPRIATENESS_OWNER_DEPENDENT`

**Proof route**  
`PRODUCT_CORRECTION_CLASS → CONTENT/SAFETY_JIT → AFFECTED_SET_RULE → COMMUNICATIONS_JIT → OQ-036 → CLASS-B_FAILURE_PROOF`

**UPD**  
None.

**Evidence needed**  
Affected-set derivation/provenance; source→intent idempotency; correction-of-correction handling; terminal-visible delivery failure.

---

## LIVE-PT-118 — Safety correction withdraws replay and participant notification delivery fails

**Scenario class**  
Mandatory safety consequence.

**Why it matters**  
This is the strongest communication case in the pass: Product Law explicitly requires participant notification, but unsafe use must stop immediately rather than waiting for provider delivery.

**Authority**  
Product safety-correction law; accepted Pass I; Architecture Class B; Content & Media/Safety ownership; OQ-036 delivery gate.

**Owning domains**  
Content & Media / Safety authority owns withdrawal/correction impact; Communications owns the resulting message intent/attempt/delivery evidence.

**Preconditions**  
Current replay is found unsafe for affected use; participants are within the governed affected scope.

**Timeline**

1. safety authority triggers correction;
2. affected replay use is withdrawn immediately;
3. source transaction establishes a durable must-not-lose notification consequence without performing provider I/O inside the source transaction;
4. Communications executes each logical notification obligation;
5. provider delivery may fail/unknown;
6. operator visibility/escalation remains.

**Expected invariants**

- unsafe replay stays withdrawn regardless of message outcome;
- notification obligation is not lossy/best-effort;
- exact cross-domain handoff does not create shared-write ownership;
- provider acceptance does not prove participant receipt;
- terminal delivery failure is visible/actionable;
- marketing opt-out cannot suppress the mandatory safety notice;
- duplicate workers do not duplicate the logical obligation.

**Questions**

- What exact source-side durable handoff representation satisfies Class B without shared writes?
- What operator escalation/recovery policy is required after terminal failure?

**Adversarial variants**

- database commits withdrawal then process crashes before async execution;
- provider accepts but never delivers;
- participant changed destination after consuming V1;
- participant requested Full Deletion concurrently;
- a second safety correction supersedes the first.

**Analysis**  
Current authority is sufficient to classify this as a mandatory durable consequence. The exact handoff representation and provider mechanics remain Communications/C&M/Safety JIT/proof details. This is not a reason to delay withdrawal until notification succeeds.

**Disposition**  
`PASS / MANDATORY_DURABLE_CONSEQUENCE`

**Proof route**  
`SAFETY/C&M_AUTHORITY → CLASS-B_DURABLE_HANDOFF → COMMUNICATIONS_JIT → OQ-036 → CRASH/RETRY/UNKNOWN/TERMINAL_FAILURE_PROOF`

**UPD**  
None.

**Evidence needed**  
Crash-after-withdrawal proof; no-lost-intent proof; duplicate/retry idempotency; terminal failure dashboard/escalation; marketing-preference bypass only for correct mandatory class.

---

## LIVE-PT-119 — Legal/consent correction or recording-purpose withdrawal may require participant notice

**Scenario class**  
Legal/privacy-determined obligation.

**Why it matters**  
Communications must not invent a legal notification duty or suppress one that the governing privacy/legal authority requires.

**Authority**  
OQ-021; Privacy & Consent ownership; accepted LIVE-UPD-006; accepted Passes F/I; Communications ownership after obligation exists.

**Owning domains**  
Privacy & Consent / applicable legal authority determines purpose consequence and any notice duty; C&M applies publication consequence; Communications executes required notice.

**Preconditions**  
A participant/speaker withdraws a relevant purpose or a legal/consent correction is raised after capture/publication.

**Timeline**

1. Privacy/current authority changes;
2. C&M re-evaluates current replay/derivative eligibility;
3. OQ-021/legal policy determines whether participant-facing notice is required and to whom;
4. only then is a Communications obligation created;
5. delivery is executed/reconciled.

**Expected invariants**

- Communications does not determine legal sufficiency;
- absence/presence of message cannot define consent state;
- source privacy/media consequence occurs according to owner authority, not provider delivery;
- if notice is required, it receives durable/visible delivery semantics appropriate to its class;
- unrelated marketing preferences do not redefine legal/privacy duty.

**Questions**

- Which legal/consent correction classes require notice?
- Who is the affected audience when one person’s recorded contribution is removed from shared media?

**Adversarial variants**

- one participant withdraws promotion only but replay remains valid;
- replay already fully withdrawn;
- recipient’s Account is closed/deletion pending;
- provider has an unresolved prior attempt.

**Analysis**  
Current authority deliberately leaves the exact duty open under OQ-021. This pass can route, not invent, the answer.

**Disposition**  
`BLOCKED / OQ-021_PRIVACY_LEGAL`

**Proof route**  
`PRIVACY/CURRENT_AUTHORITY → OQ-021 → CONTENT_MEDIA_JIT → COMMUNICATIONS_JIT_IF_NOTICE_REQUIRED → OQ-036_AS_APPLICABLE`

**UPD**  
None.

**Evidence needed**  
Approved OQ-021 notice rules; current-purpose transition evidence; delivery proof only after obligation is defined.

---

## LIVE-PT-120 — Full Deletion Request occurs while a live/replay message is queued but not yet submitted

**Scenario class**  
Privacy invalidation race before provider I/O.

**Why it matters**  
A stale worker must not keep sending merely because the message was admitted earlier, while historical source facts remain independently governed.

**Authority**  
Product Full Deletion lifecycle; Architecture deletion/non-resurrection; accepted Pass H; Communications current-precondition revalidation supporting contract.

**Owning domains**  
Privacy & Consent owns Full Deletion orchestration/suppression; source domains retain their own business semantics; Communications owns message lifecycle.

**Preconditions**  
A MessageIntent exists for a live/replay communication; no provider operation has yet begun; participant starts Full Deletion and normal access is revoked.

**Timeline**

1. message obligation exists;
2. message waits in durable execution state;
3. Full Deletion Request changes current privacy/access authority;
4. worker wakes;
5. current owner predicates are re-read before provider admission;
6. message is stopped/suspended/disposed if current policy requires.

**Expected invariants**

- queued work does not self-authorise stale processing;
- Privacy does not shared-write Communications records;
- source occurrence/attendance history is not rewritten by message suppression;
- a provider operation already lawfully begun may leave historical delivery evidence and is handled under processor/deletion policy;
- cancellation of Full Deletion does not automatically replay suppressed old messages unless current owner policy creates a valid obligation.

**Questions**

- Which communication classes may still be lawfully required during deletion/cancellation windows?
- What exact owner predicate stops each live/replay message role?

**Adversarial variants**

- provider admission races the deletion request;
- deletion is cancelled within 14 days;
- message is a mandatory safety notice;
- account email changes before deletion.

**Analysis**  
Pass H already prevents self-resurrection and stale processing. Pass K reuses that doctrine: execution authority is current, historical intent/evidence is not resend authority.

**Disposition**  
`PASS_WITH_REFINEMENT / CURRENT_OWNER_REVALIDATION`

**Proof route**  
`PRIVACY_JIT → COMMUNICATIONS_JIT → DELETION_RACE/RESTART_PROOF → OQ-030/032_AS_APPLICABLE`

**UPD**  
None.

**Evidence needed**  
Pre-attempt invalidation race; deletion cancellation behaviour; mandatory-notice exception policy if any.

---

## LIVE-PT-121 — Duplicate/reordered source lifecycle changes would create conflicting messages

**Scenario class**  
Idempotency/reordering across domains.

**Why it matters**  
Reschedule/cancel/replay/correction events may be retried or observed out of order. Communications must not create a contradictory journey ledger that becomes hidden source authority.

**Authority**  
Architecture idempotency/provider-reorder doctrine; Communications MessageIntent working contract; Domain ownership.

**Owning domains**  
Source owner owns lifecycle transition/version; Communications owns each logical obligation and its attempts.

**Preconditions**  
One occurrence or replay experiences multiple legitimate source versions/transitions; async handoffs may duplicate/reorder.

**Timeline**

1. source version A creates/permits obligation role R;
2. source changes to B;
3. duplicate A handoff and B handoff arrive in varying order;
4. Communications deduplicates by logical source operation/version + role and revalidates current predicates before a new provider operation.

**Expected invariants**

- one logical source obligation does not multiply under retry;
- a genuinely new source version/role may create a distinct intent;
- historical attempts are not rewritten;
- current source authority controls whether a later provider operation is still admissible;
- no generic `CommunicationJourney` becomes source lifecycle authority.

**Questions**

- What exact source idempotency/provenance key will FP-007 JIT expose?
- When is a new reschedule/correction a new logical communication obligation rather than a retry?

**Adversarial variants**

- cancel then legitimate reinstatement;
- V2 correction then V3 before V2 notice;
- two workers race admission;
- old provider callback arrives after successor intent.

**Analysis**  
Existing idempotency and MessageIntent doctrine is sufficient. Exact keys/relations remain JIT design.

**Disposition**  
`PASS / IDEMPOTENT_SOURCE_ROLE_INTENT`

**Proof route**  
`SOURCE_JIT → COMMUNICATIONS_JIT → DUPLICATE/REORDER/CONCURRENCY_PROOF`

**UPD**  
None.

**Evidence needed**  
Duplicate handoff test; source-version successor test; current-predicate admission test.

---

## LIVE-PT-122 — Provider accepted an old message, then source truth changes before delivery is known

**Scenario class**  
External irreversible/ambiguous delivery versus current source truth.

**Why it matters**  
Email/SMS providers may already have accepted an operation that cannot be recalled. Source state can change afterward.

**Authority**  
Architecture provider evidence/ambiguity; Communications unknown-outcome doctrine; source Domain ownership.

**Owning domains**  
Source owner retains current truth; Communications owns provider operation/evidence.

**Preconditions**  
A valid message is submitted; provider accepts or outcome is ambiguous; occurrence/replay/access changes before final delivery evidence.

**Timeline**

1. provider operation begins lawfully;
2. source truth changes;
3. provider may still deliver the old message;
4. platform current state rejects stale authority and renders current truth.

**Expected invariants**

- provider acceptance cannot freeze source state;
- already-begun operation remains historical evidence even if later stale;
- unknown old outcome blocks speculative duplicate retry/failover of the same intent where duplicate delivery matters;
- stale message cannot restore access/publication;
- operator/support history can explain the discrepancy.

**Questions**

- Which message roles require stronger late-staleness mitigation in content/link design?
- Can the channel support recall, and if so is that evidence only rather than correctness authority?

**Adversarial variants**

- safety withdrawal immediately after provider acceptance;
- cancelled event message arrives after replacement event notice;
- provider callback is reordered.

**Analysis**  
Some stale-message arrival is physically unavoidable. Correctness must therefore live in current platform authority and bounded capabilities, not a guarantee that all external messages can be recalled.

**Disposition**  
`PASS_WITH_REFINEMENT / EXTERNAL_IRREVERSIBILITY`

**Proof route**  
`COMMUNICATIONS_JIT → SOURCE_CURRENT_AUTHORITY → PROVIDER_UNKNOWN/REORDER_PROOF → STALE-CAPABILITY_PROOF`

**UPD**  
None.

**Evidence needed**  
Accepted-then-source-change test; unknown outcome reconciliation; support traceability.

---

## LIVE-PT-123 — Participant opted out of marketing but must receive a safety correction notice

**Scenario class**  
Purpose/preference separation.

**Why it matters**  
Treating every notification as marketing can suppress required safety notices; treating every reminder as mandatory can bypass participant controls.

**Authority**  
Domain Communications policy; Product safety-correction law; Privacy purpose ownership; OQ-017/OQ-036 as applicable.

**Owning domains**  
Privacy owns purpose-level withdrawal; Communications owns category/channel preference and delivery; Safety/C&M owns safety-notice source obligation.

**Preconditions**  
Participant has opted out of marketing/category messages; a governed safety correction affects them.

**Timeline**

1. marketing preference is off;
2. safety correction creates mandatory notice obligation;
3. Communications classifies the source-authorised role correctly;
4. mandatory notice proceeds under approved product/safety policy;
5. marketing remains suppressed.

**Expected invariants**

- marketing opt-out does not erase mandatory safety notice duty;
- safety notice does not re-enable marketing;
- purpose/category semantics are explicit, not inferred from channel;
- optional reminders remain subject to their own policy/controls;
- Privacy purpose withdrawal, if relevant to the notice itself, remains separate authority.

**Questions**

- Which live lifecycle message roles are mandatory product/safety versus optional reminder/operational?
- What quiet-hour exception policy, if any, applies to mandatory safety notices?

**Adversarial variants**

- participant disabled email category but in-app remains available;
- participant withdrew a purpose that affects the lawful notice basis;
- same template is mistakenly reused for marketing and safety.

**Analysis**  
Current Domain Law already requires this separation. Pass K does not define the exact preference schema or emergency quiet-hour policy.

**Disposition**  
`PASS_WITH_REFINEMENT / PURPOSE_CLASS_SEPARATION`

**Proof route**  
`SAFETY/C&M_SOURCE_ROLE → PRIVACY/PREFERENCE_POLICY → COMMUNICATIONS_JIT → OQ-036 → POLICY_MATRIX_PROOF`

**UPD**  
None.

**Evidence needed**  
Marketing-off/safety-on test; optional-reminder suppression test; role/content provenance.

---

## LIVE-PT-124 — No outbound journey was promised, so no MessageIntent exists

**Scenario class**  
Absence of obligation versus delivery failure.

**Why it matters**  
Roadmap requires notification-failure visibility, but a system must not create artificial “failures” for messages that were never part of the governed participant contract.

**Authority**  
FP-007 Roadmap conditional OQ-036 wording and exit condition; Architecture Class B versus Class C; Communications ownership.

**Owning domains**  
Final Feature Pack scope/source owner determines whether an obligation exists; Communications owns delivery only after a valid obligation exists.

**Preconditions**  
A lifecycle event occurs for which no Product/Final Contract/legal rule requires an outbound message.

**Timeline**

1. source transition commits;
2. no communication obligation is created;
3. no MessageIntent/DeliveryAttempt exists;
4. current participant/app state reflects the source fact.

**Expected invariants**

- absence of unpromised communication is not labelled provider/delivery failure;
- operator metrics distinguish `no obligation` from `intent pending/failed`;
- Roadmap failure visibility applies where a governed notification obligation/path exists;
- optional future journeys remain explicit scope choices, not accidental hidden requirements.

**Questions**

- Does the Final Contract require at least one ordinary outbound live journey, or only the Product-mandated correction/safety cases plus protected in-app access?
- How will acceptance criteria enumerate included roles?

**Adversarial variants**

- product team assumes confirmation email without contract text;
- operator dashboard counts no-intent as failure;
- UI copy promises a reminder that the governed contract did not include.

**Analysis**  
The Roadmap does not enumerate every message and explicitly makes OQ-036 conditional on a promised journey. The Final Contract must eliminate UX/contract ambiguity by listing included roles rather than inferring them from implementation screens.

**Disposition**  
`PASS_WITH_REFINEMENT / OBLIGATION_EXISTENCE_MUST_BE_EXPLICIT`

**Proof route**  
`FP007_FINAL_CONTRACT → ACCEPTANCE_CRITERIA → COMMUNICATIONS_JIT_ONLY_FOR_INCLUDED_ROLES`

**UPD**  
None.

**Evidence needed**  
Final Contract role inventory; dashboard distinction between no-obligation and failed obligation.

---

## LIVE-PT-125 — Mandatory notification exists but provider delivery terminally fails

**Scenario class**  
Roadmap failure-visibility acceptance test.

**Why it matters**  
A mandatory notice can fail physically even when platform correctness is intact. FP-007 explicitly requires notification failure visibility.

**Authority**  
FP-007 exit condition; Architecture Class B; Communications ownership; OQ-036.

**Owning domains**  
Source owner establishes the mandatory obligation; Communications owns intent, attempts, reconciliation and terminal delivery failure; operator/audit surfaces consume evidence without becoming source authority.

**Preconditions**  
A mandatory/promised communication obligation exists; durable intent was established correctly; all approved attempts exhaust or reach terminal failure.

**Timeline**

1. source transition establishes/causes durable obligation;
2. Communications admits provider attempts under current predicates;
3. retries/reconciliation proceed within bounded policy;
4. obligation reaches terminal-visible failure or unresolved state requiring operator action;
5. source business truth remains what its owner committed.

**Expected invariants**

- failure is not silently dropped;
- provider failure does not rewrite source truth;
- failure state is operationally visible with enough provenance to act safely;
- operator recovery cannot bypass source/privacy/content/current-authority guards;
- retry exhaustion is not falsely reported as provider delivery;
- duplicate manual action cannot multiply the logical obligation.

**Questions**

- Which terminal states/escalations does Communications JIT/OQ-036 require for the selected provider?
- Which mandatory notice failures block release readiness or require manual outreach?

**Adversarial variants**

- provider outage affects all participants;
- destination hard-bounces;
- provider outcome remains unknown rather than terminal failure;
- manual operator retry races automatic reconciliation.

**Analysis**  
This is the direct executable meaning of “notification failure is visible.” Exact provider/retry/alert mechanics remain OQ-036/Communications JIT, but silent loss is not acceptable once the obligation exists.

**Disposition**  
`PASS / TERMINAL_FAILURE_VISIBILITY_REQUIRED`

**Proof route**  
`SOURCE_OBLIGATION → COMMUNICATIONS_JIT → OQ-036 → OUTAGE/BOUNCE/UNKNOWN/RETRY-EXHAUSTION/OPERATOR_RECOVERY_PROOF`

**UPD**  
None.

**Evidence needed**  
Terminal-failure dashboard/evidence; unknown-versus-failure distinction; bounded operator recovery; source-state independence.

---

# 6. Pass-K synthesis

## 6.1 Source truth and communication obligation are separate transitions

The stable working model is:

```text
source authoritative fact
→ determine whether a communication obligation exists
→ if required/promised, establish durable logical intent
→ bind exact governed delivery content/provenance
→ provider/channel attempt(s)
→ delivery evidence / unknown / terminal-visible failure
```

The arrow sequence does **not** imply that provider success is required to make the source fact true.

## 6.2 Failure visibility is not blanket message creation

FP-007’s “notification failure is visible” requirement means included/required notification obligations cannot disappear silently. It does not authorise discovery to invent a registration confirmation, reminder, cancellation email or replay-available message where Product/Final Contract authority has not promised one.

The Final Feature Pack Contract must enumerate included participant communication roles so UI copy, acceptance tests and implementation do not silently expand scope.

## 6.3 Protected joining instructions are a source-access requirement

DEC-186 requires protected joining instructions. A protected current in-app/application surface may satisfy that access need if the Final Contract permits it. Outbound message delivery is a separate promise and must not become admission authority.

## 6.4 Reminder scope remains optional until promised

OQ-017 remains non-blocking for FP-007 unless reminders enter the governed participant contract. Once promised, reminder-specific mechanics route through OQ-017 and selected delivery/provider proof through OQ-036.

## 6.5 Correction notifications have different authority strength

- `minor_editorial_correction`: no blanket participant-notification duty identified by this pass;
- `material_content_correction`: source owner must govern whether notification is appropriate and identify affected participants;
- `safety_correction`: participant notification is explicit and mandatory, while withdrawal happens immediately;
- `legal_or_consent_correction` / `full_withdrawal`: any notice requirement routes through OQ-021/Privacy/legal unless another current authority already requires it.

Communications executes; it does not decide these source obligations.

## 6.6 Mandatory notification is Class B

Once a communication is a must-not-lose Product/Final-Contract consequence, Architecture §8.2 applies. Durable execution intent must survive crash/restart and handlers must revalidate current preconditions before provider I/O.

Exact cross-domain transaction/outbox/job representation remains JIT/proof detail. No shared-write ownership is created.

## 6.7 Stale messages are unavoidable external history, not authority

After provider admission, an old message may be physically impossible to recall. Therefore all consequential access/publication decisions continue to read current platform authority. Messages should contain bounded capabilities and exact provenance, not durable authority.

## 6.8 Mandatory product/safety notice versus marketing remains purpose-separated

Marketing consent/preferences do not suppress mandatory safety/product notices. Optional reminders/marketing-like journeys cannot claim “mandatory” merely to bypass participant controls. Exact policy matrix remains Communications/Privacy/JIT work.

## 6.9 No new Communications Resource is justified

Nothing in Pass K proves independent durable business truth requiring a new Live-specific `CommunicationJourney`, notification resource, provider resource or shared lifecycle resource.

The existing MessageIntent/DeliveryAttempt working seam remains sufficient as planning evidence unless future governed Communications JIT demonstrates otherwise.

---

# 7. Gap-register adjudication

## Refine and reuse `LIVE-GAP-006 — Promised live communications`

**Classification remains:** `COMMUNICATIONS_GATE`

Pass K does not create `LIVE-GAP-015`.

Accepted/proposed refinement for later acceptance:

1. **Ordinary lifecycle messages** — registration confirmation, reschedule/cancellation notice, replay-available notice are not established by current FP-007 authority as universal outbound promises. If the Final Contract includes one, `OQ-036` becomes blocking for that promised journey.
2. **Protected joining instructions** — required by DEC-186 as protected participant access; outbound notification is separate. If outbound delivery is promised, OQ-036 applies.
3. **Reminders** — remain OQ-017 non-blocking until promised; once promised, OQ-017 governs reminder mechanics and OQ-036 the selected launch channel/provider proof.
4. **Material correction notices** — Product law requires notification where appropriate; the governing source owner defines applicability/affected set. Once required, durable Communications semantics + OQ-036 apply.
5. **Safety correction notices** — explicit Product requirement; mandatory Class-B consequence with terminal-visible failure; OQ-036 applies to the selected release delivery path.
6. **Legal/consent/withdrawal notices** — OQ-021/Privacy/legal authority first determines whether notice is required; Communications/OQ-036 follow only after that obligation exists.
7. **Full Deletion interaction** — current owner predicates govern whether queued messages may proceed; stale workers do not self-authorise.

No new governed sub-identifiers are created for these routes.

---

# 8. UPD adjudication

## No `LIVE-UPD-007`

Pass K creates no new upstream decision package.

Rationale:

- current Domain Law already separates source authority from Communications;
- DEC-186 already requires protected joining instructions;
- Roadmap already makes OQ-036 conditional on promised live notification journeys;
- Roadmap already makes OQ-017 non-blocking until reminder promise exists;
- Product correction law already distinguishes material/safety notification consequence;
- Privacy/OQ-021 already owns unresolved legal/consent notice semantics;
- Architecture already defines Class-B mandatory durable consequence behaviour;
- existing Communications working evidence already covers intent/attempt, provider ambiguity, retry, content/locale provenance and current-precondition revalidation.

A new Product amendment would duplicate existing authority/routing rather than resolve a genuine contradiction.

---

# 9. Evidence-register adjudication

No `LIVE-EV-*` item is added by Pass K.

Later proof should cover, where the Final Contract includes the relevant journeys:

- source fact remains authoritative despite message failure;
- source→logical-intent idempotency;
- durable must-not-lose handoff for mandatory safety/material-notice obligations;
- crash after source transition before provider execution;
- duplicate/reordered source handoffs;
- current-precondition revalidation before provider I/O;
- provider acceptance versus delivery versus unknown versus terminal failure;
- reschedule/cancellation stale-message races;
- stale joining capability cannot restore current access;
- replay withdrawal/correction invalidates future send where required;
- marketing opt-out does not suppress mandatory safety notice;
- optional reminder remains suppressible/controlled under its approved policy;
- terminal notification failure is visible and operator recovery remains source-authority safe.

Provider-specific testing remains deferred to OQ-036/provider selection rather than guessed here.

---

# 10. Explicit non-decisions preserved

Pass K does **not** decide:

- whether FP-007 must include registration-confirmation messaging;
- whether every reschedule/cancellation must generate an outbound message;
- whether replay publication always triggers a replay-available message;
- exact reminder timing/channel/quiet-hour policy;
- exact source-side durable handoff representation for Class B;
- exact Communications Resource/action/table/job design;
- exact provider/retry/failover implementation;
- exact destination-resolution/change-of-email rules for FP-007;
- exact operator escalation SLA;
- exact material-correction “where appropriate” threshold/affected-set algorithm;
- legal/privacy notice duties under OQ-021;
- exact wording or channel of mandatory safety notices;
- whether email, in-app or both fulfil any one future message role;
- notification analytics/engagement tracking;
- event-commerce/ticket messages;
- promotional-clip campaign messaging;
- retention periods.

---

# 11. Pass-K proposed conclusions

1. Communications never becomes registration, occurrence, access, replay-publication, privacy or correction authority.
2. FP-007 notification-failure visibility applies to governed notification obligations; it does not silently create every conceivable lifecycle message.
3. The Final FP-007 Contract must enumerate included/promised participant communication roles.
4. Registration confirmation, reschedule/cancellation notice and replay-available notification are not identified by current authority as universal outbound FP-007 promises.
5. DEC-186 protected joining instructions are required, but outbound email delivery is not inherently the authority; a protected current application surface may satisfy the access requirement if the Final Contract permits it.
6. OQ-017 remains non-blocking until reminders are promised.
7. Any explicitly promised live notification journey routes through OQ-036 for launch channel/provider proof.
8. Material correction notification is conditional on the governing owner determining it is appropriate for an affected set; Communications does not make that decision.
9. Safety correction notification is an explicit mandatory Product consequence; replay withdrawal happens immediately and the notice proceeds as a must-not-lose Class-B consequence.
10. Legal/consent/withdrawal notice duties are not invented by Communications; OQ-021/Privacy/legal authority decides them first.
11. Once a message is a must-not-lose obligation, durable intent must survive crash/restart and terminal failure must remain visible; PubSub/best-effort observation is insufficient.
12. Provider acceptance/delivery/unknown remains evidence only and never freezes current source truth.
13. Historical messages may become stale; current platform authority and bounded capabilities prevent them from restoring obsolete schedule/access/publication state.
14. Marketing opt-out does not suppress a correctly classified mandatory safety/product notice; optional reminder/marketing roles cannot misuse the mandatory class.
15. Full Deletion/current privacy authority is revalidated before new provider work; queued work is not self-authorising.
16. No new Live-specific Communications Resource is justified.
17. `LIVE-GAP-006` is refined/reused; no `LIVE-GAP-015` is warranted.
18. No `LIVE-UPD-007` is warranted.
19. No `LIVE-EV-*` is warranted yet.

---

# 12. Pass-K outcome

**Outcome:** `PASS`

Current authority is sufficient to separate source live/replay truth from participant communication obligations and to route the remaining message/provider details correctly. The material uncertainty is scope selection and existing gates, not missing Product capability.

Pass K therefore proposes:

- `LIVE-PT-110...LIVE-PT-125`;
- refinement/reuse of `LIVE-GAP-006` only;
- no `LIVE-UPD-007`;
- no `LIVE-GAP-015`;
- no `LIVE-EV-*`.

---

# 13. Proposed next focused pass after acceptance

Only after Pass K acceptance:

> **Cross-dimensional convergence and JIT-entry readiness — pressure-test simultaneous occurrence/access/privacy/media/communications changes under retries, reordering, restart and reconciliation, then perform a final contradiction/gap/proof-route sweep without adding new Product scope.**

That pass should be a closure sweep rather than another broad feature expansion. It should test whether accepted A–K conclusions compose under races such as cancellation + entitlement revocation + provider ambiguity + replay withdrawal + queued mandatory notice, and determine whether Live & Replay discovery is ready to stop and hand off to governed Feature Pack/JIT planning.
