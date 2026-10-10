# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.17.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.17.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 16 — communications orchestration / delivery-consequence semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.16.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused Programmes / Communications orchestration-and-consequence pass while preserving Passes 1–15 and their accepted working-lock boundaries.

> This is an append-only semantic successor. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work, approved Feature Pack/JIT contracts, Communications authority, Content & Media authority, Privacy & Consent authority, Identity authority, Entitlements authority, Safety authority or Programmes & Challenges authority.

> A Programme may be the authoritative source of a release, due date, recovery transition, Edition change or other participant-facing event that warrants communication. It does not thereby own durable communication intent, channel/category preference, quiet-hours/caps, delivery-attempt/provider evidence, marketing-purpose permission or message/template content version.

---

# 126. Accepted working-lock status entering Pass 16

The user explicitly accepted Pass 15 and instructed the stream to continue with the next pass.

Therefore Passes 1–15 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, named authority gates, deferred items and later explicit refinements.

Pass 16 inherits without reopening:

- ProgrammeVersion owns programme/activity structure, requirement/progression/completion meaning and references governed content rather than owning content bodies;
- Edition/Cohort/Enrolment/release/recovery timing remains Programmes-owned source truth;
- Content & Media owns governed message/template content, locale/version, approval, publication, correction and withdrawal;
- Communications owns communication intent, channel/category preferences, quiet-hours/caps and durable delivery lifecycle;
- Privacy & Consent owns purpose-level permission; Communications preferences do not grant or restore that permission;
- HJP owns habit occurrences and private progress; reminder delivery is not adherence evidence;
- Entitlements owns current access; a communication or deep link cannot grant access;
- source evidence and Programme satisfaction remain distinct owner truths;
- Pass 15 established exact delivered locale/version provenance and prohibited silent unapproved language fallback;
- generic operator source-correction/override authority remains narrowed under `PRG-GAP-009` and is reserved for Pass 17;
- exact reminder/provider/channel/cap/retry/failure mechanics remain behind `OQ-017`, `OQ-027` and `OQ-036`; and
- broad discovery remains unfrozen.

---

# 127. Pass 16 — communications orchestration / delivery-consequence semantics

## 127.1 Scope hard stop

This pass answers only:

1. how a Programme/Edition/HJP source event composes with Communications-owned durable message intent and delivery attempts;
2. why message dispatch/delivery/open/click evidence is not Programme progress/completion or HJP occurrence truth;
3. how Content-owned template/version/locale binding composes with Communications delivery;
4. how channel/category preferences, quiet hours, caps and reminder pause remain distinct from Enrolment/Habit lifecycles;
5. how Privacy & Consent purpose permission differs from Communications channel/category preference for Programme-originated messages;
6. how governed mandatory notices differ from optional reminders without letting Programmes self-declare bypass authority;
7. how deduplication/retry semantics prevent duplicate participant effects without defining implementation keys/queues;
8. how duplicate/reordered source/provider observations are reconciled without arrival order becoming authority;
9. how timezone/language/contact changes affect future delivery while preserving historical delivery provenance;
10. how Edition postponement/reschedule/recovery/source invalidation constrains stale queued messages without moving schedule authority into Communications;
11. how late enrolment and compassionate recovery affect future communication relevance without blanket reminder backfill;
12. how terminal delivery failure remains visible operational evidence without becoming participant failure;
13. how purchaser/participant separation constrains Programme-message recipients;
14. how role-scoped operational views avoid giving facilitators/support universal delivery/admin access;
15. how Programme communications minimise sensitive Health/HJP/Safety data;
16. how Analytics observes delivery/engagement without becoming Programme or Communications authority;
17. how current access remains enforced independently of messages/deep links;
18. how FP-008 and later FP-014 reuse the shared Communications capability rather than building programme-specific messaging engines;
19. whether existing `OQ-017`, `OQ-027`, `OQ-036` and existing PRG gaps are sufficient for later JIT; and
20. whether any new Product, Architecture or Domain amendment is actually required.

This pass deliberately does **not** decide:

- exact launch channel/provider selection, pricing, quotas or credentials — `OQ-036`;
- exact Nuwe Jy channel set, delivery caps, templates, retry counts, quiet-hour algorithm, deduplication key or failure owner — `OQ-027`;
- exact generic reminder scheduling/retry/rate-limit mechanics — `OQ-017`;
- exact Oban queue/worker names, job args, uniqueness options, backoff or retention;
- exact MessageIntent/DeliveryAttempt Ash Resource representation for FP-008/FP-014;
- a universal communication-journey/campaign DSL;
- operator/manual correction of delivery/source state — Pass 17;
- Edition cancellation/transfer commercial policy — later dedicated pass / existing `PRG-GAP-003` where applicable;
- broader cross-domain concurrency/retry proof beyond this communication seam — later dedicated pass;
- exact analytics denominator/reporting contracts — later analytics pass;
- legal classification of every message as marketing/service/mandatory;
- urgent-help wording/routing beyond preserving Safety/OQ-008 authority;
- translation architecture already bounded by Pass 15/OQ-013;
- generic support-case or incident-management architecture; or
- SMS/WhatsApp/native-push activation beyond current Product sequencing.

---

## 127.2 Pass-16 authority evidence

### PRG-EV-231 — Live authority baseline reconfirmed

Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413`. README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` continue to route Product Law v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and Platform Operating Model v1.0.1 as current authority. The Programmes/Learning ledgers remain working/non-authoritative.

### PRG-EV-232 — Communications owns communication intent, preferences and durable delivery lifecycle

Current Domain Law §6.15 defines Communications as the owner of outbound/in-app communication intent, subscriber contacts, channel/category preferences and durable delivery lifecycle while purpose permission and originating business events remain with their respective owners.

### PRG-EV-233 — The ownership matrix separates contact, preferences and delivery evidence

Domain Law assigns Communications the notification/subscriber communication contact, notification/marketing channel-category preferences plus quiet-hours/caps, and message-intent/delivery-attempt/provider evidence. Identity remains canonical identity/contact authority where applicable; Privacy & Consent remains purpose permission authority; originating domains only read delivery observations.

### PRG-EV-234 — Content & Media owns governed message/template content

Domain Law §6.7 owns governed message/template content versions and their locale/publication lifecycle. Communications may bind and deliver an approved content version but does not become wording, translation, publication or correction authority.

### PRG-EV-235 — Programmes owns source participation truth, not notification delivery

Domain Law §6.8 owns ProgrammeVersion structure, Edition/Cohort schedule, Enrolment, release/progression and completion while explicitly depending on Communications for scheduled messages. Notification delivery attempts are not Programme truth.

### PRG-EV-236 — Nuwe Jy communication operations are preconfigured, language/timezone aware and deduplicated

`DEC-218` requires preconfigured language- and timezone-aware deduplicated communications and role-scoped operational dashboards for Nuwe Jy. This is an explicit composition requirement, not permission for Programmes to own delivery state.

### PRG-EV-237 — Habit/programme reminders are participant-controlled

`DEC-162` requires participant-controlled, timezone-aware reminders with quiet hours, caps, pause and supportive language. Reminder control is therefore not equivalent to Enrolment, habit or activity lifecycle.

### PRG-EV-238 — Channel capability is broader than any one Programme

`DEC-261` locks a channel-capable architecture with email and in-app first, SMS/WhatsApp later and native push deferred. A Programme should request a governed communication role/category rather than encode provider/channel infrastructure as Programme truth.

### PRG-EV-239 — Notification preferences and mandatory notices are distinct governed semantics

`DEC-262` requires category/channel preferences, quiet hours, frequency caps, marketing-consent separation and governed mandatory notices. A Programme reminder cannot simply label itself mandatory to bypass preference rules.

### PRG-EV-240 — Delivery must be durable, idempotent, deduplicated, retryable and observable

`DEC-263` requires durable Oban-backed idempotent, deduplicated, retryable and observable notification delivery. Exact queue/worker/provider/retry representation remains implementation/JIT detail.

### PRG-EV-241 — Marketing preference and marketing-purpose permission have different owners

`DEC-304` makes a scoped channel/category opt-out a Communications-owned preference change while purpose-level marketing withdrawal is committed only by Privacy & Consent. Preference changes cannot grant or restore withdrawn purpose permission.

### PRG-EV-242 — Reminder delivery design is already an explicit architecture/operations gate

`OQ-017` owns exact reminder channels, scheduling, retries, quiet-hour behaviour, observability and rate limits. Pass 16 may define semantic ownership/consequences but must not choose these implementation values.

### PRG-EV-243 — Nuwe Jy communication policy is already an explicit operations/architecture gate

`OQ-027` owns Nuwe Jy launch channels, delivery caps, templates, retries, quiet hours, deduplication and failure ownership. These details therefore do not justify a new Programme gap or a Programme-owned delivery subsystem.

### PRG-EV-244 — Provider and launch-channel selection remains gated

`OQ-036` remains VENDOR / OPERATIONS REVIEW for launch email/in-app implementation, later SMS/WhatsApp providers, costs, consent rules, retries and delivery evidence.

### PRG-EV-245 — Roadmap treats Nuwe Jy communication readiness as a real activation/release concern

Roadmap FP-008 lists `OQ-027` among the major gates and classifies the required Nuwe Jy communication channels/caps/templates/retries/quiet-hours/deduplication/failure ownership as part of edition readiness, while the applicable notification/provider path also remains gated before activation.

### PRG-EV-246 — Foundation-programme reminders reuse existing Communications capability

Roadmap FP-014 keeps reminders/publication as release gates rather than creating a Programme-specific messaging platform. The broader programme/habits outcome can be modelled while exact scheduled-reminder operations remain gated.

### PRG-EV-247 — Current certified FP-001 Communications dossier confirms the owner pattern without generalising its narrow Resource set

The current certified/current FP-001 Communications JIT dossier is supporting lower-level evidence only. Within its narrow Identity scope it preserves the invariant that source-domain truth remains with the source owner, delivery status is observation only, and Communications owns MessageIntent/DeliveryAttempt. Pass 16 may reuse that owner pattern but must not copy FP-001-specific Resource or destination rules into Programme law.

### PRG-EV-248 — Communications lifecycle includes terminal-visible failure

Current Domain Law describes durable communication intent, delivery attempts/status/provider evidence and terminal-visible failure. Therefore failed delivery must remain visible operational evidence rather than disappear or be rewritten as participant behaviour.

### PRG-EV-249 — Analytics is downstream of communication and programme authority

Domain Law gives Analytics only derived observation/projection authority. Delivery rates, opens/clicks and programme outcomes may be analysed, but Analytics cannot convert delivery telemetry into Programme completion, adherence or Safety truth.

### PRG-EV-250 — Pass-15 locale/version provenance remains applicable to messages

Pass 15 working-lock established that exact delivered locale/content-version provenance must remain explainable and that machine/sibling-language fallback cannot silently bypass Content authority. Programme communications consume the same Content-owned locale/version rules.

### PRG-EV-251 — Current preference/permission must remain distinct from historical delivery evidence

A historical delivery attempt can remain true after a preference, purpose permission or Programme state changes. Current sending authority and past delivery evidence are separate dimensions; history must not restore permission or source validity.

### PRG-EV-252 — Programme schedule changes cannot be hidden inside Communications state

Edition/release/enrolment schedule truth remains Programmes-owned. A queued or previously sent message cannot change the authoritative release calendar, create availability, extend a deadline or prove that a release occurred.

### PRG-EV-253 — Communication delivery is not participant action evidence

Because Programme completion/progression and HJP occurrences have their own owners, send/accept/deliver/open/click observations cannot become lesson completion, habit occurrence, attendance or check-in evidence unless a separately approved source action in the owning Domain actually occurred.

### PRG-EV-254 — Compassionate recovery is not conditional on successful reminders

Existing Programme/HJP law preserves catch-up and compassionate recovery without punitive failure for ordinary delay, and Pass 14 already established reminder delivery is not adherence evidence. Communications failure therefore cannot manufacture a participant miss/failure or erase recovery eligibility.

### PRG-EV-255 — Existing authority and gates are sufficient for this semantic seam

`DEC-162`, `DEC-218`, `DEC-261...DEC-263`, `DEC-304`, Domain Law §§6.7/6.8/6.15 and `OQ-017`/`OQ-027`/`OQ-036` already place the durable truths and remaining operational questions. No new Product, Architecture or Domain authority is required merely to compose Programme events with Communications.

---

# 128. Pass-16 semantic model

## 128.1 Keep four truths separate

| Dimension | Owner | Answers |
|---|---|---|
| Originating business event/state | Programmes / HJP / Events / Safety / other source owner | What happened in the participant journey that may justify communication? |
| Communication obligation / preference | Communications (purpose permission remains Privacy & Consent) | What logical message obligation exists and which channels/categories are allowed? |
| Delivery execution/evidence | Communications | What attempts occurred and what provider/terminal delivery evidence exists? |
| Participant progress/consequence | Programmes / HJP / Events / other owning Domain | What did the participant actually do and what Programme consequence follows? |

No dimension silently rewrites another.

## 128.2 Programme orchestration requests communication; it does not deliver as business authority

The safe semantic shape is:

```text
authoritative Programme/Edition event
        ↓
request / create one logical communication obligation
        ↓
Communications applies allowed category/channel/preference/permission rules
        ↓
Communications attempts delivery and records evidence
        ↓
Programme remains authoritative for release/progress/completion
```

A provider callback never becomes an alternate Programme command.

## 128.3 Message content and message delivery are separate owner truths

Content & Media owns the approved message/template content version, locale and publication state. Communications owns the intent and execution that binds/uses an eligible version. Programmes may supply bounded source facts needed for approved rendering, but it does not copy or mutate message content authority.

## 128.4 Preference, purpose permission and mandatory-notice rules remain distinct

A Programme-originated message needs an approved communication category/semantic role. Communications owns channel/category preferences, quiet hours and caps. Privacy & Consent owns purpose permission. Mandatory-notice exceptions must come from governed Product/Privacy/Communications policy, not from a Programme flag invented for convenience.

## 128.5 Reminder pause is not Programme pause

```text
reminder preference paused  ≠  Enrolment paused
reminder preference paused  ≠  Habit paused
Enrolment paused            ≠  marketing permission withdrawn
```

Explicit cross-domain consequences may exist, but lifecycle states remain independent.

## 128.6 Delivery telemetry is never participation truth by itself

The following Communications observations do not by themselves satisfy a Programme requirement:

- queued;
- provider accepted;
- sent;
- delivered;
- bounced/failed;
- notification opened/read;
- message link clicked.

Only the owning activity/source Domain can record the qualifying participant action.

## 128.7 Deduplication protects participant effects, not just provider calls

The semantic invariant is one logical communication obligation for one authoritative source obligation/role. Duplicate source observations, job retries or provider retries must not multiply participant-facing logical messages or Programme consequences. Exact idempotency keys, uniqueness windows and queue mechanics remain JIT.

## 128.8 Stale queued work cannot outrank current source authority

When an authoritative source change makes a future message contradictory — for example an Edition postponement, recovery-path change, withdrawn content or superseded schedule — an old queued observation cannot force delivery merely because it exists. The system must reconcile at the appropriate boundary from current owner authority while preserving historical attempts. Exact cancellation/revalidation timing remains JIT.

## 128.9 Terminal failure stays visible without blaming the participant

Terminal delivery failure is Communications operational evidence. It may trigger an operator/support workflow under approved policy, but it does not mark the participant missed, failed, abandoned, non-adherent or incomplete.

## 128.10 Timezone, language and contact changes affect future delivery, not history

Future eligible communication uses governed current policy and authorised destination/locale selection. Historical attempts retain the actual destination, locale/content version and relevant timing provenance. A later profile change must not rewrite what was sent.

## 128.11 Late enrolment and recovery do not imply blanket backfill

Late enrolment/catch-up/recovery may create new relevant communication obligations under Programme policy. It does not imply sending every historical reminder, nor does recovery permit stale punitive nudges to continue after the Programme path changes.

## 128.12 Messages cannot grant access

A reminder or deep link is not Entitlement authority. Protected destinations enforce current Entitlements/Identity/Safety policy. A stale message must never resurrect access merely because it was previously valid to send.

## 128.13 Operational dashboards are scoped views, not shared-write authority

Role-scoped Communications dashboards may expose minimum delivery state needed for operations. They do not give facilitators, cohort managers or support generic authority to mutate Programme completion, provider evidence, preferences, Privacy permission or source events.

## 128.14 Communication payloads remain minimum necessary

Programme reminders should prefer opaque identifiers, approved render inputs and minimal participant context. Health facts, Safety cases, private journal prose or other sensitive source payloads are not copied into Communications merely because they could personalise a message.

## 128.15 Analytics remains downstream

Delivery/open/click rates can be analysed as derived facts. They cannot define Programme completion, HJP adherence, Safety eligibility, Entitlement validity or purpose permission.

---

# 129. Pass-16 focused pressure tests

## PRG-PT-627 — Programme stores provider delivery status as activity completion

**Scenario:** A Programme reminder is accepted/delivered by an email provider and the activity is marked complete.

**Expected invariants / analysis:** Provider/delivery evidence remains Communications truth. Programme completion requires approved Programme/source evidence and cannot be manufactured from delivery telemetry.

**Disposition:** `REJECT`.

## PRG-PT-628 — Delivered email is treated as participant action

**Scenario:** A reminder email is delivered successfully but the participant does nothing.

**Expected invariants / analysis:** Delivery proves only the delivery-side observation. It does not prove lesson view, reflection, habit occurrence, attendance or any other participant action.

**Disposition:** `REJECT`.

## PRG-PT-629 — Failed reminder marks the participant missed or failed

**Scenario:** A scheduled reminder reaches terminal delivery failure.

**Expected invariants / analysis:** Terminal failure must remain visible Communications evidence. The participant is not marked missed/failed/abandoned solely because delivery failed.

**Disposition:** `REJECT`.

## PRG-PT-630 — Reminder opt-out is treated as non-adherence

**Scenario:** The participant pauses or disables an optional reminder category.

**Expected invariants / analysis:** Participant-controlled reminder preference is not Programme adherence truth. Progress/completion remains determined from source participation evidence.

**Disposition:** `REJECT`.

## PRG-PT-631 — Duplicate Programme source observations create duplicate reminders

**Scenario:** The same release/due-event is observed twice because of retry/reconnect.

**Expected invariants / analysis:** One logical communication obligation must not produce duplicate durable participant effects. Exact idempotency key mechanics remain JIT/OQ-027.

**Disposition:** `PASS / JIT PROOF`.

## PRG-PT-632 — Provider retry creates a new Programme event

**Scenario:** A provider delivery attempt fails and Communications retries.

**Expected invariants / analysis:** Retry stays delivery execution for the same logical communication obligation; it does not create a new Programme release/activity/due event.

**Disposition:** `REJECT`.

## PRG-PT-633 — Every Programme notification must be duplicated across email and in-app

**Scenario:** The system sends both channels for every reminder merely because launch architecture supports both.

**Expected invariants / analysis:** DEC-261 is channel-capable, not a universal dual-send rule. Approved category/channel policy and preferences decide allowed delivery.

**Disposition:** `REJECT / OQ-027`.

## PRG-PT-634 — Programme admin mutates notification preference inside Programme state

**Scenario:** A cohort manager disables a participant email category by editing an Enrolment/Programme record.

**Expected invariants / analysis:** Communications owns channel/category preferences. Programme operators may invoke authorised Communications actions only under their scoped role.

**Disposition:** `REJECT`.

## PRG-PT-635 — Reminder pause automatically pauses Enrolment

**Scenario:** A participant pauses programme reminders.

**Expected invariants / analysis:** Reminder pause and Enrolment pause are independent lifecycles. No Enrolment transition is inferred.

**Disposition:** `REJECT`.

## PRG-PT-636 — Enrolment pause withdraws marketing permission

**Scenario:** A participant pauses an Enrolment and the platform removes purpose-level marketing permission.

**Expected invariants / analysis:** Programme lifecycle cannot mutate Privacy & Consent purpose permission by implication.

**Disposition:** `REJECT`.

## PRG-PT-637 — Marketing withdrawal automatically suppresses every operational Programme notice

**Scenario:** A participant withdraws marketing purpose permission while enrolled.

**Expected invariants / analysis:** Optional marketing must be suppressed, but whether a concrete Programme notice is operational/mandatory/another permitted category must come from approved communication classification. Pass 16 does not relabel all Programme messages as marketing or mandatory.

**Disposition:** `PASS WITH CLASSIFICATION GATE`.

## PRG-PT-638 — Channel opt-out is treated as purpose-level marketing withdrawal

**Scenario:** A participant disables marketing email but not other marketing channels.

**Expected invariants / analysis:** A scoped channel/category preference change remains Communications truth and does not itself withdraw Privacy & Consent-owned purpose permission.

**Disposition:** `REJECT`.

## PRG-PT-639 — Re-enabling an email preference restores withdrawn marketing permission

**Scenario:** Purpose-level marketing permission was withdrawn; later the participant re-enables a Communications email preference.

**Expected invariants / analysis:** Preference cannot grant/restore purpose-level permission. A new valid Privacy & Consent grant is required.

**Disposition:** `REJECT`.

## PRG-PT-640 — Programme labels an ordinary reminder mandatory to bypass preferences

**Scenario:** A Programme configuration marks routine motivation as mandatory solely to ignore quiet hours/opt-outs.

**Expected invariants / analysis:** Mandatory-notice treatment requires a governed Product/communication basis; Programmes cannot manufacture bypass authority.

**Disposition:** `REJECT`.

## PRG-PT-641 — Optional reminder preference suppresses a separately governed mandatory notice

**Scenario:** A participant has disabled an optional reminder category and a genuinely mandatory notice arises.

**Expected invariants / analysis:** Optional preference does not automatically suppress a separately governed mandatory notice; exact channel/exception rules remain OQ-027/OQ-036 and applicable legal/privacy authority.

**Disposition:** `PASS WITH GOVERNED RULE`.

## PRG-PT-642 — Quiet hours are ignored for an ordinary habit reminder

**Scenario:** A routine reminder is scheduled inside the participant quiet-hours window.

**Expected invariants / analysis:** DEC-162/DEC-262 require timezone-aware quiet-hour handling for ordinary reminders. Exact deferral mechanics remain OQ-017/OQ-027.

**Disposition:** `REJECT`.

## PRG-PT-643 — Urgent-help content is improvised as a Programme notification exception

**Scenario:** A Programme detects distress and invents a new urgent push/SMS bypass.

**Expected invariants / analysis:** Urgent-help wording/routing remains governed by Safety/OQ-008 and approved mandatory-channel policy. Programmes cannot improvise clinical urgency semantics or channels.

**Disposition:** `REJECT / EXISTING GATE`.

## PRG-PT-644 — Timezone change duplicates the same reminder

**Scenario:** The participant changes timezone after one reminder has been scheduled.

**Expected invariants / analysis:** Future scheduling should reconcile from current applicable timezone/policy without duplicating the same logical obligation. Historical attempts remain historical. Exact scheduler mechanics remain OQ-017.

**Disposition:** `PASS / JIT PROOF`.

## PRG-PT-645 — Language change creates a second communication obligation

**Scenario:** The participant switches preferred/content language before a future reminder.

**Expected invariants / analysis:** Language choice may affect the eligible message variant but must not create duplicate Programme truth or duplicate obligations by itself. Delivered locale/version remains explainable.

**Disposition:** `REJECT DUPLICATION`.

## PRG-PT-646 — Missing message translation silently falls back to machine draft

**Scenario:** A required Programme notice has no approved selected-language template.

**Expected invariants / analysis:** Pass-15 Content rules still apply. Do not silently deliver an unapproved machine/sibling variant; exact required-notice fallback belongs to Content/OQ-013/OQ-027.

**Disposition:** `REJECT`.

## PRG-PT-647 — Withdrawn template remains deliverable from a queued job

**Scenario:** A message content version is withdrawn after intent creation but before send.

**Expected invariants / analysis:** A stale queued execution must not use withdrawn content as if current authority remained valid. Exact revalidation/cancellation mechanics belong to Content/Communications JIT.

**Disposition:** `REJECT / JIT PROOF`.

## PRG-PT-648 — Late provider callback revives a cancelled Programme obligation

**Scenario:** A source obligation is no longer valid, then a delayed provider callback reports delivered.

**Expected invariants / analysis:** Provider evidence may update historical delivery observation but cannot recreate Programme source validity or future delivery authority.

**Disposition:** `REJECT`.

## PRG-PT-649 — Edition postponement is ignored by already queued reminders

**Scenario:** An Edition is postponed after future reminders were prepared.

**Expected invariants / analysis:** Programmes remains schedule authority. Future contradictory sends must be suppressed/reconciled from current source authority; exact cancellation mechanics remain OQ-027/JIT.

**Disposition:** `PASS / JIT PROOF`.

## PRG-PT-650 — Late enrolment backfills every historical daily reminder

**Scenario:** A participant enrols late in a shared scheduled Edition.

**Expected invariants / analysis:** Late enrolment/catch-up does not imply replaying every old communication. Programme recovery policy defines relevant future obligations; no blanket backfill is inferred.

**Disposition:** `REJECT DEFAULT`.

## PRG-PT-651 — Recovery mode leaves contradictory old missed-day reminders active

**Scenario:** A participant enters an approved catch-up/recovery path while old scheduled nudges remain queued.

**Expected invariants / analysis:** Communications should not continue stale messages that contradict the current Programme recovery path. Exact suppression/rescheduling mechanics remain OQ-027/JIT.

**Disposition:** `PASS / JIT PROOF`.

## PRG-PT-652 — Frequency cap causes Programme requirement failure

**Scenario:** Several valid reminders reach the Communications frequency cap.

**Expected invariants / analysis:** Caps are delivery-governance controls, not Programme completion rules. Suppressed/deferred optional messages do not become participant failure.

**Disposition:** `REJECT`.

## PRG-PT-653 — Reminder cap reached marks HJP habit occurrence missed

**Scenario:** A habit reminder is not sent because the cap is reached.

**Expected invariants / analysis:** HJP occurrence truth is independent of reminder delivery. No missed occurrence is created from cap suppression.

**Disposition:** `REJECT`.

## PRG-PT-654 — Message delivery receipt is used as habit evidence

**Scenario:** Provider says a habit reminder was delivered.

**Expected invariants / analysis:** Delivery receipt is not HJP occurrence evidence.

**Disposition:** `REJECT`.

## PRG-PT-655 — In-app notification read state completes a lesson

**Scenario:** Participant opens an in-app reminder but never opens/completes the lesson activity.

**Expected invariants / analysis:** Notification read state remains Communications truth and cannot substitute for Programme activity evidence.

**Disposition:** `REJECT`.

## PRG-PT-656 — Reminder-link click completes the target activity

**Scenario:** Participant clicks a link in a communication.

**Expected invariants / analysis:** A click may be Analytics/communication interaction evidence only. It does not complete the target Programme activity unless the owning activity contract explicitly defines and records a qualifying source action.

**Disposition:** `REJECT DEFAULT`.

## PRG-PT-657 — Offline/retry reconnect creates two communication intents for one obligation

**Scenario:** The originating programme event is delivered to Communications twice after a retry.

**Expected invariants / analysis:** Semantic deduplication must preserve one logical obligation; exact causal/idempotency key is JIT.

**Disposition:** `PASS / JIT PROOF`.

## PRG-PT-658 — Provider webhooks arriving out of order define delivery truth by arrival order

**Scenario:** A bounce/failure observation arrives before an earlier provider-accepted callback.

**Expected invariants / analysis:** Communications reconciles its delivery lifecycle from governed evidence/current state; arrival order alone is not business authority.

**Disposition:** `REJECT ARRIVAL ORDER`.

## PRG-PT-659 — Provider acceptance is treated as confirmed participant receipt

**Scenario:** Provider API accepts the message for delivery.

**Expected invariants / analysis:** Acceptance is an execution observation, not proof the participant saw or acted on the message. Delivery lifecycle must preserve the distinction.

**Disposition:** `REJECT`.

## PRG-PT-660 — Terminal delivery failure is hidden because Programme still works

**Scenario:** A reminder fails terminally but the participant can access the Today view directly.

**Expected invariants / analysis:** Programme capability may remain intact, but terminal-visible Communications failure must remain observable for operations.

**Disposition:** `REJECT HIDDEN FAILURE`.

## PRG-PT-661 — Manual resend creates duplicate Programme consequence

**Scenario:** Support resends the same reminder after a delivery issue.

**Expected invariants / analysis:** Resend must not create extra Programme progress/release/completion effects. Whether it is a new attempt or new intent depends on the approved communication obligation contract; exact mechanics remain JIT.

**Disposition:** `PASS WITH JIT BOUNDARY`.

## PRG-PT-662 — Operator manually marks a provider message delivered without evidence

**Scenario:** A staff member changes delivery status solely to clear an operational queue.

**Expected invariants / analysis:** Provider/delivery evidence must remain truthful and auditable. Generic operator override of historical delivery is not authorised; operator-correction semantics are deferred to Pass 17.

**Disposition:** `REJECT / PASS-17`.

## PRG-PT-663 — Operator marks Programme complete because all reminders were sent

**Scenario:** An admin sees every scheduled communication sent and marks participant complete.

**Expected invariants / analysis:** Message dispatch is not participation/completion evidence. Generic mark-complete authority remains prohibited/narrowed under PRG-GAP-009.

**Disposition:** `REJECT`.

## PRG-PT-664 — Canonical email change rewrites historical delivery provenance

**Scenario:** Participant changes their Account email after earlier Programme messages.

**Expected invariants / analysis:** Historical Communications evidence retains the destination/provenance actually used. Current contact authority governs future eligible sends; history is not rewritten.

**Disposition:** `REJECT REWRITE`.

## PRG-PT-665 — Purchaser receives participant Programme reminders by default

**Scenario:** A gift purchaser paid for the Programme and receives the participant daily reminders.

**Expected invariants / analysis:** Purchaser and participant remain separate. Programme-participant communications target the authorised participant context unless an explicit different recipient role exists.

**Disposition:** `REJECT`.

## PRG-PT-666 — Facilitator can inspect all participant delivery details by default

**Scenario:** A facilitator dashboard exposes all delivery attempts, email addresses and provider evidence.

**Expected invariants / analysis:** DEC-218 requires role-scoped operational dashboards and minimum necessary data. Facilitator role does not automatically grant Communications operations access.

**Disposition:** `REJECT DEFAULT`.

## PRG-PT-667 — Analytics delivery score changes Programme completion

**Scenario:** Analytics computes a high engagement score from opens/clicks.

**Expected invariants / analysis:** Analytics remains derived and cannot mutate Programme completion/adherence truth.

**Disposition:** `REJECT`.

## PRG-PT-668 — Experiment variant suppresses a governed mandatory Programme notice

**Scenario:** An experiment changes messaging and removes an applicable mandatory notice.

**Expected invariants / analysis:** Experimentation cannot override protected Product/communication invariants. Mandatory notice requirements remain controlling.

**Disposition:** `REJECT`.

## PRG-PT-669 — Communications outage changes Programme release state

**Scenario:** The notification provider is unavailable when Day 12 releases.

**Expected invariants / analysis:** Programme release state remains Programmes-owned. Communications failure is a delivery problem and does not itself roll back or erase the release.

**Disposition:** `REJECT LIFECYCLE COLLAPSE`.

## PRG-PT-670 — No notification means released content is considered unreleased

**Scenario:** A participant receives no reminder but the Today content was authoritatively released.

**Expected invariants / analysis:** Notification is not release authority. The content remains released according to Programme state; failure must be visible separately.

**Disposition:** `REJECT`.

## PRG-PT-671 — Reminder is sent before the authoritative release boundary

**Scenario:** A scheduler race causes the Day 13 reminder to send before Day 13 is available.

**Expected invariants / analysis:** Communications must not invent availability. The send path must be constrained by the authoritative source obligation/release policy; exact synchronization is JIT proof.

**Disposition:** `REJECT / JIT PROOF`.

## PRG-PT-672 — Rescheduled live session leaves original reminder authoritative

**Scenario:** A linked live session time changes after a reminder was created.

**Expected invariants / analysis:** Events/Programme source state remains authority. Future communications must reconcile; old delivery history remains historical and cannot define the session time.

**Disposition:** `PASS / JIT PROOF`.

## PRG-PT-673 — Duplicate Edition activation causes duplicate launch messages

**Scenario:** Edition activation is observed more than once.

**Expected invariants / analysis:** One logical activation communication obligation must deduplicate; no duplicate participant effects from duplicate observations.

**Disposition:** `PASS / JIT PROOF`.

## PRG-PT-674 — Queued reminder grants access after entitlement revocation

**Scenario:** A participant loses current access but an old reminder with a deep link is still delivered.

**Expected invariants / analysis:** The message itself cannot grant or restore access; protected destinations must enforce current Entitlements authority. Whether the reminder should also be suppressed is source/category policy under OQ-027/JIT.

**Disposition:** `PASS WITH ACCESS INVARIANT`.

## PRG-PT-675 — Programme reminder contains copied health or private journal details

**Scenario:** A reminder includes diagnosis, medication detail or private journal text to personalise the nudge.

**Expected invariants / analysis:** Communications must use minimum necessary approved render data. Programme/HJP/Health ownership and privacy boundaries prohibit copying sensitive source payloads merely for convenience.

**Disposition:** `REJECT`.

## PRG-PT-676 — Communications unavailable at release time is treated as participant/programme failure

**Scenario:** A release occurs but Communications is temporarily unavailable.

**Expected invariants / analysis:** The Programme release remains authoritative and delivery failure/retry remains Communications truth. No participant failure/completion consequence is inferred; operational visibility/recovery is required.

**Disposition:** `REJECT LIFECYCLE COLLAPSE`.

---

# 130. Pass-16 gap adjudication

## `PRG-GAP-009` — operator correction remains deferred; delivery ownership is now sharper

Pass 16 confirms that generic staff/facilitator/support authority cannot edit provider evidence, participant preferences, source Programme truth or completion merely because an operational dashboard displays them. The exact governed operator-correction/source-authority semantics remain reserved for Pass 17 rather than being solved inside Communications.

## `PRG-GAP-003` — Edition cancellation/postponement policy remains separate from communication suppression

Communications must respect authoritative Edition/source invalidation and avoid stale contradictory sends, but it cannot define the business cancellation/postponement/transfer policy itself. The existing narrowed Edition lifecycle gap therefore remains separate; no communications-specific duplicate gap is created.

## `PRG-GAP-004` — entitlement/access remains independent of reminder delivery

A queued/sent message cannot restore access, and a delivered reminder does not prove current access. Protected destinations still consult current Entitlements authority. This does not reopen the already-resolved generic access/Enrolment boundary.

## `PRG-GAP-005` / `PRG-GAP-011` — message content follows existing Content rules

Message/template versions remain Content-owned. Withdrawn/unavailable required content cannot be bypassed by an old queued message, machine translation or stale template. Existing Content/translation gates remain sufficient.

## No new Product / Architecture / Domain gap promoted

The Programmes ↔ Communications seam has explicit owners and named unresolved operational gates. The remaining unknowns are implementation/operations questions already routed to `OQ-017`, `OQ-027`, `OQ-036` and later JIT/proof. Creating a new Programme notification Domain or gap would duplicate authority rather than resolve ambiguity.

---

# 131. Pass-16 refinements to the working synthesis

## PRG-REF-183 — Separate source event, communication intent, delivery attempt and participant consequence

Programme/Edition/HJP/Events owners create the business truth; Communications owns the logical communication obligation and delivery lifecycle; participant action/progress stays with its owning Domain.

## PRG-REF-184 — Programmes never owns provider delivery truth

Programme records may reference communication outcomes where needed for explanation/operations, but durable communication-intent/delivery-attempt/provider evidence remains Communications authority.

## PRG-REF-185 — Communications never owns Programme lifecycle truth

Sending, delivering, failing, opening or retrying a message cannot release content, pause/complete/abandon an Enrolment, create a habit occurrence or rewrite an Edition schedule.

## PRG-REF-186 — Message/template wording remains Content & Media authority

Communications binds approved content/version/locale provenance and delivers it; it does not become editorial/translation/publication authority.

## PRG-REF-187 — Preference and purpose permission remain separate owners

Communications owns channel/category preferences, quiet-hours/caps; Privacy & Consent owns purpose-level permission. Programme configuration cannot collapse them.

## PRG-REF-188 — Reminder pause and Enrolment/Habit pause remain independent lifecycle dimensions

Coordination may be an explicit consequence, but one pause state never silently mutates the other.

## PRG-REF-189 — Mandatory-notice classification requires explicit governed authority

A Programme cannot evade optional preferences/quiet-hours/caps by self-labelling messages mandatory. Exact categories/exceptions remain Product/Privacy/Communications policy.

## PRG-REF-190 — Delivery/open/click observations are not Programme completion evidence

Communications interaction may feed Analytics, but only owning-domain source actions can satisfy Programme requirements.

## PRG-REF-191 — Delivery failure is not participant failure

Terminal failure remains visible Communications evidence and never by itself marks missed, failed, abandoned or incomplete.

## PRG-REF-192 — Quiet-hours/caps suppression has no automatic progress consequence

Delivery governance cannot manufacture HJP occurrence or Programme completion/failure.

## PRG-REF-193 — Timezone/language changes affect future eligible delivery without rewriting history

Future scheduling/variant selection uses governed current policy; prior attempts retain the actual timezone/locale/destination provenance needed for explanation.

## PRG-REF-194 — Duplicate source observations must not duplicate participant communication effects

Semantic deduplication applies to the logical business obligation; exact idempotency key/index/job mechanics remain JIT.

## PRG-REF-195 — Provider retries remain delivery execution, not new Programme obligations

Retry policy belongs Communications/OQ-017/OQ-027/OQ-036 and cannot duplicate release/progress effects.

## PRG-REF-196 — Stale queued work reconciles against current source/content authority where invalidation matters

Postponement, withdrawal, recovery-path changes and other authoritative invalidations must not be overridden by an old queue observation. Exact cancellation/revalidation mechanics remain JIT.

## PRG-REF-197 — Terminal-visible failure is part of the operational contract

Failures must be observable to appropriately scoped operators rather than silently discarded or converted into participant state.

## PRG-REF-198 — Late-enrolment and recovery communications need explicit Programme policy

Do not backfill all historical reminders or continue contradictory old nudges by default. Programme recovery meaning determines which future communication obligations are relevant.

## PRG-REF-199 — Purchaser and participant communication contexts remain separate

Payment does not grant purchaser access to the participant journey or make the purchaser the default recipient of participant reminders.

## PRG-REF-200 — Operational communication views remain role-scoped

DEC-218 operational dashboards expose only the minimum communication evidence appropriate to each role; facilitator/support roles are not universal delivery-admin roles.

## PRG-REF-201 — Programme communications use minimum necessary source data

Do not copy health records, private journals or other sensitive payloads into message state when bounded references/approved render inputs suffice.

## PRG-REF-202 — Communication analytics remains derived

Delivery/open/click aggregates can inform operations/product learning but cannot become Programme, HJP, Entitlement, Safety or Privacy authority.

## PRG-REF-203 — OQ-017, OQ-027 and OQ-036 remain the implementation/operations boundary

Pass 16 does not choose channels/providers, retry budgets, exact caps, quiet-hour algorithms, templates, idempotency keys, queue/worker names or provider-evidence representation.

## PRG-REF-204 — No new Communications-in-Programme Domain or gap is justified

Existing Communications plus Programmes/Content/Privacy owner contracts and named gates cover the seam; a Programme-owned notification engine would create competing authority.

---

# 132. Pass-16 anti-notification-engine / YAGNI outcome

Pass 16 explicitly rejects:

- a Programme-owned notification/reminder delivery table as business authority;
- provider delivery status stored as Programme completion/adherence truth;
- a separate Nuwe Jy messaging engine;
- a separate Foundation Programme messaging engine;
- a generic Programme campaign builder merely to send scheduled reminders;
- a universal communication-journey DSL before concrete OQ-027/JIT need;
- mandatory email-plus-in-app duplication for every Programme message;
- pulling SMS/WhatsApp or native push into FP-008 merely because Communications can support channels later;
- a Programme-owned copy of notification preferences, quiet hours or frequency caps;
- a Programme-owned copy of marketing consent/purpose permission;
- using marketing unsubscribe as an Enrolment or habit state change;
- using reminder pause as Programme pause;
- using notification read/open/click as completion evidence;
- using provider acceptance as participant receipt or action proof;
- using notification failure as participant miss/failure/abandonment;
- backfilling every historical daily reminder for late enrolment by default;
- keeping stale reminders alive after authoritative postponement/recovery/withdrawal merely because a job exists;
- raw health facts or private journal text embedded into reminder persistence;
- facilitator-wide access to provider/destination evidence by default;
- Analytics engagement scores as Programme completion authority;
- a generic provider abstraction/resource catalogue inside Programmes;
- a second deduplication truth separate from Communications;
- Redis/Kafka/GenServer/event-bus infrastructure solely for Programme reminders without evidence;
- a new Notification Domain or Feature Pack;
- pulling Pass-17 operator-correction semantics into message status editing;

The simplest correct model remains source-domain business truth → Communications-owned logical intent/delivery → source-domain participant consequence, with Content/Privacy/Entitlements/Safety authority preserved and exact provider/scheduler mechanics left to existing gates/JIT.

---

# 133. Pass-16 disposition

**Outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Passes 1–15 remain accepted/working-locked and Pass 16 does not reopen them.
2. Programmes owns the Programme/Edition/Enrolment/release/recovery source event; Communications owns durable communication intent, channel/category preference and delivery lifecycle.
3. Content & Media owns message/template content version, locale, publication, correction and withdrawal; Communications binds/delivers approved content rather than owning it.
4. Privacy & Consent owns purpose-level permission; Communications owns channel/category preferences, quiet hours and caps. Programme configuration cannot collapse or restore either authority.
5. A Programme-originated message must have an approved semantic category/role; Programmes cannot self-label ordinary reminders mandatory to bypass preferences or quiet hours.
6. Reminder pause, Enrolment pause, Habit pause and marketing-purpose withdrawal remain independent lifecycle dimensions.
7. Queued/sent/provider-accepted/delivered/failed/opened/read/clicked communication observations are not Programme completion, HJP occurrence or attendance evidence by themselves.
8. Delivery failure is operational Communications evidence and never by itself participant failure, missed activity, abandonment or incomplete status.
9. Semantic deduplication must prevent duplicate logical participant messages/effects when source events/jobs/provider attempts repeat; exact keys/mechanics remain JIT.
10. Provider retry stays delivery execution for the same logical obligation and cannot create a new Programme release/progress event.
11. Duplicate/reordered provider/source observations cannot define current business truth by arrival order; reconcile from owning authority.
12. Stale queued work cannot outrank a current authoritative postponement, withdrawal, recovery-path change or other invalidation; exact cancellation/revalidation mechanics remain JIT.
13. Timezone/language/contact changes may affect future delivery under governed policy but do not rewrite historical destination/locale/content-version/timing provenance.
14. Late enrolment and recovery do not imply blanket replay of historical reminders; future obligations follow explicit Programme recovery policy.
15. Quiet-hours/caps suppression of optional reminders has no automatic Programme/HJP progress consequence.
16. Optional communication preferences do not suppress separately governed mandatory notices by implication; exact mandatory rules remain governed and message-specific.
17. Marketing channel/category opt-out and purpose-level marketing withdrawal remain distinct; enabling a preference cannot restore withdrawn purpose permission.
18. Programme participant communications do not default to the purchaser or sponsor merely because that actor paid.
19. Role-scoped operational dashboards expose only minimum necessary delivery evidence; facilitator/support role does not grant universal Communications-admin authority.
20. Programme communications must minimise sensitive source data and must not copy Health facts, Safety cases or private journal prose merely for message convenience.
21. A message/deep link cannot grant access or bypass current Entitlements/Identity/Safety checks at the protected destination.
22. Analytics may derive delivery/open/click aggregates but cannot override Programme, HJP, Communications, Privacy, Entitlements or Safety authority.
23. FP-008 and later FP-014 should reuse shared Communications capability rather than create Nuwe Jy/Foundation Programme messaging engines.
24. `OQ-017`, `OQ-027` and `OQ-036` remain the correct primary unresolved implementation/operations gates for this seam; exact Content/translation/urgent-help gates still apply where their subject matter is used.
25. Current FP-001 Communications dossier may inform the source-obligation/delivery ownership pattern but its narrow Identity-specific Resource/destination semantics are not automatically promoted to generic Programme law.
26. No new Product, Architecture or Domain amendment is justified by this pass.
27. No new `PRG-GAP` or `PRG-UPD` is justified by this pass.
28. Generic Programme notification engines, campaign builders, journey DSLs, provider catalogues and duplicate preference/consent stores remain `DEFER_YAGNI` / rejected.
29. Operator/manual correction of delivery/source state remains reserved for Pass 17 and cannot be inferred from a dashboard/control surface.
30. Exact Ash Resources, queues, workers, retry budgets, provider adapters, idempotency keys and delivery-retention mechanics remain later JIT/proof work.

**Pass hard stop:** Pass 17 — operator correction / source-authority exception semantics — has not started. Do not pull generic mark-complete, source correction, provider-status override, Safety override or admin exception mechanics into this Pass-16 candidate.

**Broad discovery remains unfrozen.** Later concurrency/retry, cancellation/transfer, historical reproducibility, analytics, FP-014 second-lens and final adversarial-convergence passes remain separate.