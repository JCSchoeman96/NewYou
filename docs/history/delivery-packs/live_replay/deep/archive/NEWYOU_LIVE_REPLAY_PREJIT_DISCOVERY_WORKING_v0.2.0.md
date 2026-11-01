# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.2.0.md

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY EVIDENCE
- **Document version:** v0.2.0
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.1.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Branch:** `prejit/live-replay`
- **Semantic rule:** v0.1.0 remains preserved unchanged. Read v0.1.0 first; this file is an append-only substantive continuation. No v0.1.0 semantic conclusion is silently rewritten.

---

# 12. Batch B objective

Pressure-test the ordinary occurrence, schedule, access, registration and attendance semantics far enough that later provider research has explicit NewYou invariants to test.

This batch does **not** select Resources, schemas, token formats, provider APIs, attendance thresholds or event-commerce mechanisms.

---

# 13. New or refined gaps from Batch B

## LIVE-GAP-008 — In-progress access continuity

**Classification:** `PRODUCT_AUTHORITY_GAP`

Current law requires current access before protected playback and makes revocation authoritative, but does not explicitly state whether an already-admitted participant must be disconnected immediately when a live right expires/revokes during an in-progress occurrence, or whether any narrowly governed occurrence-specific continuity/grace exists.

## LIVE-GAP-009 — Registration requirement and cancellation semantics

**Classification:** `PRODUCT_AUTHORITY_GAP`

Product Law says registration **may** include capacity/waitlist/entitlement checks and defines several access modes. It does not fully state when ordinary FP-007 registration is required, optional or absent, nor the participant-facing effect of cancelling a registration for a non-scarce live occurrence.

## LIVE-GAP-010 — Weak-identity/public live attendance

**Classification:** `PRODUCT_AUTHORITY_GAP`

Public/free live modes are permitted, but authoritative participant attendance requires sufficient identity/evidence. Product must not promise person-level attendance where the delivery mode cannot support that assurance.

---

# 14. LIVE-UPD-001 refinement — occurrence identity and independent lifecycle dimensions

Batch B strengthens `LIVE-UPD-001`.

The current working direction should not become one giant status enum. At least these concepts can vary independently:

- intended/scheduled occurrence identity and schedule version;
- publication/visibility state;
- provider binding/execution state;
- actual live-execution outcome;
- registration state per participant;
- attendance evidence/reconciliation state per participant;
- recording association state;
- replay publication state elsewhere in Content & Media.

A provider replacement, stream-key rotation or room recreation must not automatically change occurrence identity. Conversely, a genuine duplicate occurrence or materially replacement event must not be silently merged merely because staff intended “the same session”. Product/Domain authority must define the lawful correction/supersession boundary.

---

# 15. Pressure tests — Batch B

## LIVE-PT-013 — Draft → scheduled → published → started → completed ordinary occurrence

**Scenario class**

Occurrence lifecycle / normal path.

**Why it matters**

The Events & Live Domain profile currently says “event draft/published/etc. as configured”; FP-007 needs a more explicit semantic contract before JIT creates actions/transitions.

**Authority**

Events & Live owns definitions/versions/occurrences and schedule/publish capability; Roadmap FP-007 requires a governed session that can be published and joined.

**Owning Domains**

Events & Live.

**Preconditions**

Authorised Event Admin/session owner and approved live content/policy.

**Timeline**

Define → schedule → publish/announce → start → complete.

**Expected invariants**

- each transition is authorised and historically explainable;
- scheduled time and actual execution outcome are not the same fact;
- provider state cannot drive an authoritative transition merely because a callback arrived;
- completion does not itself publish replay.

**Questions**

Which states are Product-significant versus JIT mechanism? Is `started` an authoritative Events fact or an observation-derived transition? What evidence finalises `completed`?

**Adversarial variants**

Provider says started before host actually begins; provider says completed while backup stream continues; no completion callback.

**Analysis**

A complete ordinary occurrence lifecycle is not yet explicit enough to hand safely to JIT. The lifecycle should distinguish intended schedule from actual execution and provider evidence.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-001`.

**Evidence needed**

Product/Domain lifecycle adjudication, then provider evidence mapping and executable transition tests.

---

## LIVE-PT-014 — Published occurrence is rescheduled after registration

**Scenario class**

Schedule/version lifecycle.

**Why it matters**

The platform must preserve the participant’s registration and the exact schedule history without letting a provider calendar object become authority.

**Authority**

Events & Live occurrence/version ownership; Event occurrence concept includes date/time/timezone; Communications owns delivery only.

**Owning Domains**

Events & Live; Communications.

**Preconditions**

Published occurrence, valid registrations, no live execution yet.

**Timeline**

T1 published → participants register → staff changes schedule → NewYou records lawful change/version → participant-visible current schedule changes → communication may be attempted.

**Expected invariants**

- old schedule remains historically explainable;
- current schedule has one NewYou authority;
- registration continuity is deliberate;
- message success/failure does not decide current schedule;
- provider schedule is reconciled evidence/configuration.

**Questions**

Which changes preserve registration automatically? Does moving to a materially different date require re-acknowledgement or a replacement occurrence? Is there a cancellation-and-rebook boundary?

**Adversarial variants**

Change 5 minutes before start; change after participant opened stale join page; provider update fails.

**Analysis**

The identity boundary is strong but Product semantics for schedule replacement versus same-occurrence reschedule remain absent.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-001`.

**Evidence needed**

Schedule-version/reschedule policy before JIT.

---

## LIVE-PT-015 — Timezone and daylight-saving rendering

**Scenario class**

Time / localisation.

**Why it matters**

A correct instant can be displayed incorrectly across regions, and later support must explain what schedule was published.

**Authority**

Platform event occurrence requires date/time/timezone; Nuwe Jy scheduling is timezone-aware; Architecture distinguishes durable business schedules from execution machinery.

**Owning Domains**

Events & Live; frontend presentation only as projection.

**Preconditions**

Occurrence has an approved schedule/timezone; participant is in another timezone or crosses a DST boundary.

**Timeline**

Schedule stored/governed → participant views local representation → timezone/DST rules render → occurrence executes at authoritative instant.

**Expected invariants**

- one authoritative occurrence schedule is not rewritten per viewer;
- local rendering is derived presentation;
- historical schedule/version includes enough meaning to explain the intended time;
- a host timezone correction is a governed schedule change, not a UI tweak.

**Questions**

Which timezone is occurrence-owned (host/event/product default)? What must be retained when timezone rules or staff correction change the represented instant?

**Adversarial variants**

Host selects wrong zone; participant device zone wrong; DST boundary; international participant receives old email.

**Analysis**

The high-level invariant is already supported. Exact representation is JIT, but schedule history must preserve semantic intent and not merely a rendered string.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT`

**UPD if any**

None beyond `LIVE-UPD-001` if schedule-version policy remains unresolved.

**Evidence needed**

JIT time-contract and executable timezone/DST cases.

---

## LIVE-PT-016 — Delayed start, overrun and early end

**Scenario class**

Occurrence execution outcome.

**Why it matters**

The scheduled interval, provider stream interval and actual NewYou live experience can diverge.

**Authority**

Events owns occurrence truth; provider state evidence only.

**Owning Domains**

Events & Live; Communications for any delay notice; Analytics derived.

**Preconditions**

Published occurrence with scheduled start/end.

**Timeline**

Scheduled start passes → host starts late → session overruns or ends early → provider emits its own timestamps → Events reconciles actual execution.

**Expected invariants**

- schedule is not retrospectively falsified to match actual execution;
- actual start/end/outcome may be recorded separately where Product needs them;
- attendance evidence is interpreted against actual execution, not provider status order alone.

**Questions**

Does Product need explicit `delayed`, actual-start and actual-end truth? What participant promise triggers a delayed-start communication?

**Adversarial variants**

Provider stream exists but presenter absent; backup host starts a second room; stream remains technically live after session ends.

**Analysis**

A single “scheduled/live/completed” status would be too weak. Schedule and execution outcome should remain independent semantic dimensions.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-001` refinement.

**Evidence needed**

Product decision on which actual-execution facts are durable business truth versus provider/operator evidence.

---

## LIVE-PT-017 — Cancelled before start, cancelled after start, abandoned and emergency termination

**Scenario class**

Occurrence terminal states / operational safety.

**Why it matters**

These outcomes have different historical, attendance, recording and communication consequences.

**Authority**

Roadmap requires correction/withdrawal/operability; Events owns occurrence; Audit may retain incident evidence; Communications owns notices.

**Owning Domains**

Events & Live; Communications; Audit & Evidence; Content & Media if recording exists.

**Preconditions**

Occurrence scheduled or already running.

**Timeline**

A. Cancel before start. B. Start then organiser ends/cancels. C. Provider outage prevents useful delivery. D. Safety/incident requires emergency termination.

**Expected invariants**

- terminal outcome is explicit and cannot be inferred merely from provider disconnect;
- historical registrations/attendance evidence are preserved appropriately;
- any raw recording remains governed separately;
- required communications are consequences, not lifecycle authority.

**Questions**

Which terminal outcomes Product needs (`cancelled`, `abandoned`, `failed`, `terminated` or reason classes) without over-modeling? Does a started-then-cancelled occurrence count as completed for any downstream purpose? Who may declare each outcome?

**Adversarial variants**

Host accidentally clicks end; provider outage then backup resumes; emergency stop after sensitive disclosure.

**Analysis**

Consequential distinction exists, but exact vocabulary/guards must be kept minimal and Product-driven.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-001` refinement.

**Evidence needed**

Minimal terminal-state semantics and authority/guard rules.

---

## LIVE-PT-018 — Provider room replacement without occurrence replacement

**Scenario class**

Provider identity / recovery.

**Why it matters**

Provider resources are operational delivery machinery and may need replacement.

**Authority**

Events occurrence authority; provider IDs non-authoritative; provider adapters replaceable.

**Owning Domains**

Events & Live; Communications if join details change; Audit & Evidence for material operator action where required.

**Preconditions**

One NewYou occurrence, existing registrations, provider room A unusable.

**Timeline**

A active association → operator creates B → NewYou deliberately switches current provider association → A becomes stale/retired evidence → registrations remain on same occurrence.

**Expected invariants**

- occurrence identity and registration history survive the operational replacement;
- old provider credential cannot become the current join authority;
- attendance from A and B can later reconcile to one occurrence where lawful.

**Questions**

What switch guard/evidence is required? How are participants already in A handled? Does cross-provider restart ever become a replacement occurrence instead?

**Adversarial variants**

Some participants stay in A; both record; operator switches back; B create outcome ambiguous.

**Analysis**

This scenario is exactly why provider identity cannot equal occurrence identity. JIT needs an explicit current-association/supersession concept but not a Product-specific technology choice.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT`

**UPD if any**

`LIVE-UPD-001`.

**Evidence needed**

OQ-020 provider controls plus JIT reconciliation and operator-runbook contract.

---

## LIVE-PT-019 — Stream key rotates, provider room stays the same

**Scenario class**

Provider operational credential lifecycle.

**Why it matters**

A secret/configuration rotation must not become a new business occurrence or publication version.

**Authority**

Architecture secrets/configuration are separate from business state; provider delivery state is non-authoritative.

**Owning Domains**

No new business Domain; Events retains occurrence association context.

**Preconditions**

Existing occurrence/provider association; stream credential compromised or rotated.

**Timeline**

Credential active → rotate/revoke → production tool updates → occurrence continues.

**Expected invariants**

- secret rotation does not change occurrence identity, registration or attendance by itself;
- old secret cannot remain accepted beyond provider/security contract;
- secret values never become ordinary business/audit payload.

**Questions**

Which provider controls support rotation without room recreation? What operator runbook is needed?

**Adversarial variants**

Old key leaked; wrong key sends stream to wrong destination; rotation during live session.

**Analysis**

This is primarily provider/JIT/operator mechanism, not upstream Product semantics.

**Semantic disposition**

`PASS`

**Proof route**

`PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

OQ-020 provider credential/rotation evidence and controlled-live runbook proof.

---

## LIVE-PT-020 — Entitled participant when registration is required but missing

**Scenario class**

Access / registration distinction.

**Why it matters**

Entitlement alone must not silently bypass an occurrence-specific registration requirement.

**Authority**

Platform 21G.14 allows registration/access modes; Events owns registration; Entitlements owns general access.

**Owning Domains**

Events & Live; Entitlements.

**Preconditions**

Participant has valid general product/programme entitlement; occurrence requires registration.

**Timeline**

Participant opens join surface without registration → system evaluates occurrence registration requirement + current entitlement.

**Expected invariants**

- entitlement and registration checks remain independent;
- join is denied or routed to lawful registration when registration is required;
- provider join URL cannot bypass either guard.

**Questions**

Which FP-007 occurrence modes require registration? May authorised staff register/admit someone manually? If manual admission is allowed, what registration/attendance evidence is created?

**Adversarial variants**

Host directly admits provider participant; participant arrives via forwarded link; public event mode.

**Analysis**

The separation is clear; the Product gap is the rule that declares registration required/optional/absent per occurrence/access mode.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

Candidate extension to `LIVE-UPD-001` or a later dedicated registration-policy UPD if subsequent cases prove consequential.

**Evidence needed**

Minimal occurrence registration-mode semantics.

---

## LIVE-PT-021 — Joined but not registered through a forwarded provider link

**Scenario class**

Access leakage / provider bypass.

**Why it matters**

Provider admission may be technically possible even when NewYou authority denies it.

**Authority**

Joining instructions protected; provider state not access authority; protected playback re-authorises current platform state.

**Owning Domains**

Events & Live; Entitlements; Identity & Access.

**Preconditions**

Authorised participant forwards a provider-native join link to another person.

**Timeline**

Link forwarded → unauthorised person attempts provider join → provider may admit depending configuration → NewYou receives evidence later.

**Expected invariants**

- leaked provider capability must not create entitlement or valid registration;
- provider presence does not automatically become authoritative attendance for a NewYou participant;
- where provider cannot enforce NewYou access, that limitation is an OQ-020 blocker, not a reason to weaken authority.

**Questions**

Can the chosen path force platform-controlled admission/playback? What identity does provider expose? Can unauthorised provider attendees be removed or prevented reliably?

**Adversarial variants**

Screenshot; anonymous/incognito join; different provider email; host manually admits the forwarded attendee.

**Analysis**

NewYou invariant is clear. Provider enforceability is empirical and could invalidate a provider path for protected modes.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

OQ-020 admission/authentication/playback controls and controlled leak tests.

---

## LIVE-PT-022 — Entitlement expires or is revoked during the live session

**Scenario class**

In-progress access lifecycle.

**Why it matters**

Current authority is clear at admission but does not fully define continuity once live delivery has begun.

**Authority**

Entitlements owns current access/revocation; Architecture says protected playback checks current authority before bounded delivery capability and stale caches cannot override revocation.

**Owning Domains**

Entitlements; Events & Live.

**Preconditions**

Participant was lawfully admitted; right expires/revokes while session is in progress.

**Timeline**

Admit at T1 → entitlement ends T2 → active playback continues or is revalidated → attendance remains a historical fact for time actually present.

**Expected invariants**

- ending access does not erase registration or prior attendance evidence;
- provider URL/session continuity cannot create a new durable right;
- any grace/continuity is an explicit Product rule, not technical accident.

**Questions**

Must playback be terminated immediately? May an occurrence-specific bounded grace exist? Does commercial reversal differ from scheduled expiry? What about suspension/security containment?

**Adversarial variants**

Membership ends mid-session; refund is confirmed; account is suspended; entitlement restored five minutes later.

**Analysis**

This is consequential Product semantics, not merely signed-URL TTL selection.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

Candidate new `LIVE-UPD-004` below.

**Evidence needed**

Product continuity/revocation semantics followed by provider/JIT revalidation proof.

---

## LIVE-UPD-004 — Define in-progress live-access continuity independently of admission

- **Originating PT:** `LIVE-PT-022`.
- **Current authority gap:** current access is authoritative and protected playback checks it, but no explicit Product rule defines an already-admitted participant when the right expires/revokes mid-occurrence.
- **Candidate working direction:** distinguish admission authority from ongoing delivery continuity. Default must not be accidental provider persistence. Product should state whether revocation classes are immediate, bounded to an already-issued capability, or eligible for a named occurrence grace; security/privacy suspensions may require stricter fail-closed handling than ordinary commercial expiry.
- **Affected Domains:** Entitlements; Events & Live; Identity & Access for security containment; Commerce when reversal is cause.
- **Why JIT cannot decide safely:** TTL/revalidation mechanism would otherwise encode commercial/security Product semantics.
- **Provider/legal/privacy gate:** OQ-020 provider enforcement; privacy/security current authority remains upstream.
- **Likely authority target:** Product Law / Entitlements semantics.
- **Downstream impact:** live player admission/revalidation, support expectations, controlled-live proof.

---

## LIVE-PT-023 — Refund/reversal before live versus after attendance

**Scenario class**

Commerce/access/history seam.

**Why it matters**

Financial reversal changes current rights but must not rewrite historical attendance.

**Authority**

`DEC-300`: provider callback evidence reconciles into Commerce; Entitlements applies access consequence; post-delivery reversal ends current access while preserving historical delivery/reversal records.

**Owning Domains**

Commerce; Entitlements; Events & Live.

**Preconditions**

A commercial source granted live/replay access.

**Timeline**

A. reversal confirmed before live admission. B. participant attends, then reversal confirmed later.

**Expected invariants**

- Commerce owns reversal truth;
- Entitlements changes current access idempotently;
- Events attendance history is not erased by later reversal;
- replay access may end according to the entitlement consequence, independently of attendance.

**Questions**

Does any event-specific refund policy belong here? For ordinary FP-007, no scarce-ticket/refund semantics should be invented beyond existing commercial access consequences.

**Adversarial variants**

Provider callback reordered; reversal later restored; attendee watched replay before reversal.

**Analysis**

Current cross-domain authority is sufficient for the ordinary access seam. Full event-refund policy remains FP-015.

**Semantic disposition**

`PASS`

**Proof route**

`JIT`

**UPD if any**

None.

**Evidence needed**

Reuse Commerce/Entitlements reconciliation proof; Events confirms history preservation.

---

## LIVE-PT-024 — Purchaser is not participant

**Scenario class**

Identity/access provenance.

**Why it matters**

The purchaser must never gain the participant’s private attendance or replay history merely by paying.

**Authority**

Product Law separates purchaser/recipient/participant/account holder; Domain Law keeps commercial and access truth separate.

**Owning Domains**

Commerce; Entitlements; Identity & Access; Events & Live.

**Preconditions**

A gift/sponsored/commercial transaction benefits a different participant.

**Timeline**

Purchaser pays/grants → recipient redeems or is assigned lawful access → participant registers/attends → purchaser later views purchase status.

**Expected invariants**

- purchaser identity does not become attendee identity;
- purchaser cannot see private attendance/Q&A/recording participation without separate authority;
- entitlement provenance can identify source without leaking participant journey.

**Questions**

What purchaser-visible redemption status is already allowed? Are sponsored grants participant-identifiable to sponsor? Existing Product Law should control, not FP-007 invention.

**Adversarial variants**

Purchaser forwards their own join link instead of beneficiary redemption; sponsor requests attendance roster.

**Analysis**

The authority separation is already strong.

**Semantic disposition**

`PASS`

**Proof route**

`JIT`

**UPD if any**

None.

**Evidence needed**

JIT privacy/access tests and minimum-data operator views.

---

## LIVE-PT-025 — Free/public occurrence with weak participant identity

**Scenario class**

Public access / attendance assurance.

**Why it matters**

Product Law permits `public` and `free_account` live access modes, but not every delivery mode can support person-level attendance truth.

**Authority**

Platform 21G.14 access modes; Events owns attendance; Analytics derived; Identity assurance remains separate from provider display identity.

**Owning Domains**

Events & Live; Identity & Access where account-linked; Analytics downstream.

**Preconditions**

Occurrence is public or free-account access; provider may allow anonymous/pseudonymous viewing.

**Timeline**

Viewer joins with weak/no platform-linked identity → provider emits view/session evidence → NewYou attempts measurement.

**Expected invariants**

- anonymous/provider view evidence cannot silently become named participant attendance;
- Analytics may measure permitted aggregate viewing without creating Events attendance truth;
- any person-level attendance claim states its assurance basis honestly.

**Questions**

Does FP-007 need person-level attendance for public modes at all? If not, is aggregate live engagement sufficient? Which access modes require platform identity?

**Adversarial variants**

Shared link; NAT/shared device; anonymous social-destination viewer; later account creation.

**Analysis**

This is a Product evidence/assurance question. Forcing provider identifiers into a canonical person would be unsafe.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

Candidate future attendance-assurance refinement under `LIVE-UPD-002`.

**Evidence needed**

Product decision on required attendance assurance per access mode, then provider capability evidence.

---

## LIVE-PT-026 — Provider email does not match NewYou account email

**Scenario class**

Attendance identity correlation.

**Why it matters**

Provider identity fields are often mutable/user-controlled and cannot be assumed canonical.

**Authority**

Identity & Access owns canonical identity; Events owns attendance; provider evidence is non-authoritative.

**Owning Domains**

Identity & Access; Events & Live.

**Preconditions**

Registered NewYou participant joins using a different provider email/display identity.

**Timeline**

Registration tied to NewYou identity → provider emits unmatched attendee evidence → reconciliation attempts safe correlation.

**Expected invariants**

- email string equality is not the only possible proof nor an excuse to merge identities unsafely;
- uncertain correlation remains unresolved rather than fabricating attendance;
- operator correction, if allowed, is scoped and auditable.

**Questions**

Does provider support platform-issued participant identifiers, SSO, signed metadata or authenticated playback identity? What manual evidence is acceptable?

**Adversarial variants**

Shared provider account; mistyped email; display-name collision; malicious impersonation.

**Analysis**

NewYou should prefer platform-controlled correlation where provider supports it. Exact capability belongs to OQ-020 empirical work.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`PROVIDER_EMPIRICAL`

**UPD if any**

`LIVE-UPD-002` if provider limitations force a Product assurance choice.

**Evidence needed**

Provider identity/authentication/metadata documentation and controlled tests.

---

## LIVE-PT-027 — Facilitator manually confirms attendance when provider evidence is missing

**Scenario class**

Attendance correction/manual evidence.

**Why it matters**

Operations may know a participant was present even when provider reporting fails, but manual assertion must not casually become truth.

**Authority**

Events owns attendance; staff roles are scoped/auditable; Audit records evidence only.

**Owning Domains**

Events & Live; Audit & Evidence.

**Preconditions**

Provider attendance report missing or wrong; authorised facilitator/host has credible direct evidence.

**Timeline**

Provider evidence unresolved → staff proposes attendance correction → guard/authority/evidence evaluated → Events records lawful conclusion or leaves unresolved.

**Expected invariants**

- manual correction is explicit, attributed and auditable;
- Audit does not own the corrected attendance;
- staff role alone does not imply universal correction authority;
- original provider evidence is not destructively rewritten.

**Questions**

Does Product permit facilitator confirmation at all? Which roles/reasons/evidence classes qualify? Is second-person review needed for programme completion consequences?

**Adversarial variants**

Bulk mark-all attended; facilitator conflict; later provider report contradicts manual entry.

**Analysis**

Whether manual confirmation is legitimate evidence is a consequential Product/Domain choice, not merely an admin feature.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-002`.

**Evidence needed**

Attendance evidence hierarchy/correction authority.

---

## LIVE-PT-028 — Registration cancelled before a non-scarce live session

**Scenario class**

Registration lifecycle.

**Why it matters**

Ordinary FP-007 registration needs a clean lifecycle without importing ticket cancellation/refund mechanics.

**Authority**

Events owns registration; full event-ticket policy is later.

**Owning Domains**

Events & Live; Communications if cancellation notice exists.

**Preconditions**

Participant validly registered for an ordinary non-ticketed live session.

**Timeline**

Registered → participant/operator cancels registration → occurrence remains scheduled → participant later attempts re-register/join.

**Expected invariants**

- cancelling registration does not alter general entitlement;
- no event refund/credit semantics are invented;
- whether re-registration is allowed is governed by occurrence policy;
- historical registration/cancellation remains explainable.

**Questions**

Does FP-007 require participant registration cancellation? If registration is only informational for non-scarce access, is explicit cancellation Product value or unnecessary complexity?

**Adversarial variants**

Cancel after join; operator cancels by mistake; participant re-registers repeatedly.

**Analysis**

This may be unnecessary for first FP-007. Do not create lifecycle states merely because event platforms commonly have them.

**Semantic disposition**

`DEFER_NOT_PREJIT`

**Proof route**

`JIT`

**UPD if any**

None unless FP-007 acceptance later requires cancellation.

**Evidence needed**

Feature Pack scope decision, not generic event-platform precedent.

---

## LIVE-PT-029 — Staff accidentally creates two NewYou occurrences for one intended session

**Scenario class**

Duplicate business identity / correction.

**Why it matters**

Unlike duplicate provider rooms, this is a duplicate NewYou business record and cannot be solved by provider reconciliation alone.

**Authority**

Events owns occurrence identity/history; Product requires historical explainability; Audit evidence cannot erase business truth.

**Owning Domains**

Events & Live; Communications; Content & Media if replay associations diverged.

**Preconditions**

Two NewYou occurrences A and B represent what staff later asserts was one intended session; registrations may exist on both.

**Timeline**

A created → B created → both published or one used → duplicate discovered → correction required.

**Expected invariants**

- no destructive row merge that erases registration/attendance history;
- one occurrence may be marked duplicate/superseded/voided only through an explicit governed correction if Product allows;
- participant histories and sent communications remain explainable.

**Questions**

Is occurrence merge ever lawful, or should one occurrence be retained as erroneous/superseded and relationships reconciled explicitly? What happens if both were actually used?

**Adversarial variants**

Registrations split; both provider rooms used; replay attached to wrong occurrence.

**Analysis**

This reinforces the need for explicit occurrence correction/supersession semantics rather than a provider-centric identity model.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-001`.

**Evidence needed**

Occurrence duplicate/correction policy and later executable history-preservation tests.

---

## LIVE-PT-030 — Historical session remains true after replay withdrawal

**Scenario class**

Cross-lifecycle historical integrity.

**Why it matters**

Media withdrawal must not rewrite occurrence or attendance history.

**Authority**

Events owns occurrence/attendance; Content & Media owns publication/withdrawal; Platform correction classes preserve history; Entitlements owns current access.

**Owning Domains**

Events & Live; Content & Media; Entitlements; Audit & Evidence as required.

**Preconditions**

Occurrence completed, attendance reconciled, replay published; replay later withdrawn.

**Timeline**

Occurrence/attendance true → replay published → withdrawal/correction → current replay access ceases → participant/support views historical occurrence.

**Expected invariants**

- occurrence remains completed/historical according to its own truth;
- attendance remains unchanged unless attendance itself is corrected;
- replay publication shows withdrawn/superseded state without deleting occurrence association;
- old playback capability no longer grants future access.

**Questions**

What participant-facing explanation is required for withdrawn replay? Does safety/legal withdrawal require proactive communications under existing correction law?

**Adversarial variants**

Replacement replay later published; participant downloaded/previously viewed old replay; old provider asset persists externally.

**Analysis**

The cross-domain authority is coherent. Exact participant messaging and processor deletion are separate consequences/gates.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT`

**UPD if any**

None.

**Evidence needed**

Content correction/withdrawal JIT contract, Entitlement invalidation proof, OQ-021/OQ-030 processor handling where applicable.

---

# 16. Batch-B semantic synthesis

Batch B adds four durable conclusions:

1. **Occurrence identity and occurrence status must not be collapsed.** Schedule version, provider binding, execution outcome and media/replay state are independent dimensions.
2. **Attendance needs an assurance model, not only a boolean.** Public/weak-identity modes, missing provider evidence, provider-email mismatch and manual confirmation cannot all lawfully map to the same automatic `attended/no_show` transition.
3. **Admission and ongoing live access are different questions.** `LIVE-GAP-008` / `LIVE-UPD-004` must prevent a signed-link TTL or provider session persistence from silently deciding Product rights.
4. **Ordinary FP-007 registration must remain simpler than event commerce.** Registration requirements may be occurrence/access-mode policy; ticket/hold/refund complexity stays FP-015.

No database representation is selected. No attendance duration threshold is proposed. No generic “EventState” enum is authorised.

---

# 17. Current UPD register after Batch B

- `LIVE-UPD-001` — stable NewYou occurrence identity + schedule/execution/correction/supersession semantics independent of provider resource.
- `LIVE-UPD-002` — Product-defined attendance meaning, assurance, correction/finality and provider-evidence relationship.
- `LIVE-UPD-003` — explicit live-right versus replay-right semantics by access/product source.
- `LIVE-UPD-004` — in-progress access continuity/revocation semantics independent of initial admission.

All four remain **working candidates**, not authority changes.

---

# 18. Next batch

Batch C will pressure-test recording, consent, sensitive capture, replay processing/publication, correction/replacement/withdrawal, deletion/retention and safety-content correction. It will deliberately route unresolved privacy/legal semantics to `OQ-021`/retention/processors rather than invent them.
