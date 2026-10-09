# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.5.0.md

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY EVIDENCE
- **Document version:** v0.5.0
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.4.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted-register baseline:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.1.md`
- **Accepted-register commit:** `2f1752f30fe9d26ad856f749c93b1bb6fe802932`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap amendment:** NONE
- **Semantic rule:** Passes A–D remain accepted working locks. This file is an append-only substantive continuation and does not silently reopen them.
- **Pass scope:** role and capture-scope distinctions only: attendee vs speaker/guest/facilitator/staff plus sensitive audience material.

---

# 36. Pass E objective and hard boundary

This pass asks only:

> What additional semantic distinctions are required when a recorded live session contains different participant roles, role changes, different capture surfaces, or sensitive audience material?

The pass is limited to:

- planned presenter / guest speaker participation;
- attendee promoted to speaker/on-stage participation;
- facilitator/host/staff participation;
- participant Q&A/chat/display-name/voice/image capture;
- sensitive personal/health disclosures during recorded interaction;
- disclosure of another person's private information;
- practitioner/dietitian participation in group Q&A;
- accidental screen-share/visual capture of sensitive information;
- provider-native role labels versus canonical NewYou role/context.

This pass deliberately does **not** decide:

- consent withdrawal after capture;
- one participant withdrawing from a multi-person recording;
- retention periods;
- Full Deletion;
- processor/provider deletion;
- exact replay editing/correction/replacement/withdrawal rules;
- promotional clip permission;
- exact moderator workflow or UI;
- participant communications after a sensitive disclosure;
- exact provider controls/APIs;
- automated sensitive-content detection;
- exact legal sufficiency of any participant/speaker permission model.

Those remain later focused passes or existing governed gates.

No `LIVE-EV-*` evidence is added in this pass because provider research remains intentionally deferred.

---

# 37. Focused authority extraction

## 37.1 Product Law: recording governance already names the distinction

Current Product Law §21G.15 requires a recorded session to have, among other things:

- explicit recording notice;
- participant/speaker consent rules;
- attendee privacy controls;
- handling of sensitive audience material;
- governed editing;
- replay entitlement;
- content/version history;
- correction/withdrawal;
- separate promotional-clip approval.

Therefore this pass must **not** invent a new principle that speakers differ from attendees or that sensitive audience material needs special handling. Product Law already says both things.

The unresolved work is to make those Product requirements implementation-grade enough that FP-007 JIT does not invent the role/capture consequences.

## 37.2 Group Q&A and sensitive-disclosure law

`DEC-175 — Sensitive disclosures` is LOCKED: general wellbeing discussion is permitted while highly sensitive health and personal disclosures are warned, redirected or moderated.

`DEC-187 — Group Q&A` is LOCKED: group Q&A is moderated educational Q&A and private diagnosis, prescription and treatment requests are redirected to professional pathways.

Current Product Law also warns members not to publish highly sensitive material such as laboratory reports, diagnoses, medication lists, detailed trauma histories and private consultation requests in community contexts, and permits unsafe disclosures to be edited/hidden/removed with restricted evidence where required.

Those controls matter here as **existing safety/privacy context**, but they do not automatically create a complete recorded-live remediation workflow. A recorded live Q&A creates a separate media/replay consequence that still routes through §21G.15 and OQ-021.

## 37.3 Domain ownership remains unchanged

- **Events & Live** owns the occurrence, participant registration/attendance and recording notice/association context.
- **Privacy & Consent** owns purpose-specific permission/current authority and later withdrawal/deletion orchestration.
- **Content & Media** owns governed captured media identity, editing, derivatives and publication.
- **Identity & Access** owns canonical identity and staff/practitioner role assignments; provider role labels do not become canonical identity/role truth.
- **Safety & Eligibility / Professional Care** retain their own safety/professional authority where a live interaction crosses into private clinical/professional handling.
- **Audit & Evidence** may record material governed actions where required but does not become recording, privacy or clinical authority.

No new Domain is justified by the presence of speakers, hosts or Q&A.

## 37.4 Existing gate remains OQ-021

`OQ-021 — Video consent and retention` remains under LEGAL / OPERATIONS REVIEW and explicitly requires speaker, attendee, recording, editing, replay, clip, retention and withdrawal rules.

Pass D already created accepted working candidate `LIVE-UPD-005` requiring the eventual participation contract to vary by relevant role/context and to be evaluated at the consequential admission/capture boundary.

This pass therefore begins with a strong anti-duplication hypothesis:

> role-specific and sensitive-audience findings should refine `LIVE-UPD-005` / `LIVE-GAP-003` unless a genuinely different authority problem is discovered.

---

# 38. Focused semantic model

## 38.1 Role and capture scope are independent dimensions

A participant's current role/context and the actual capture surfaces affecting that person are separate facts.

Examples:

- attendee with camera/mic off but display name/chat captured;
- attendee promoted to speaker with voice/video now captured;
- host/facilitator visible and audible throughout;
- guest speaker screen sharing slides but not participant gallery;
- practitioner answering general educational questions while private diagnosis remains prohibited;
- participant Q&A voice included in full recording but later omitted from an approved replay.

The platform must not use one boolean such as `recording_consent=true` to imply every role, every capture surface and every downstream use is equivalent.

This is a semantic invariant, not a schema proposal.

## 38.2 Provider role labels are operational evidence

Provider labels such as `host`, `co-host`, `panelist`, `presenter`, `attendee` or equivalent are provider/delivery facts.

They may help enforce or evidence a NewYou role/context, but they do not create canonical staff/practitioner/participant authority.

If provider role state and NewYou role/context disagree, NewYou must not silently upgrade provider state into Privacy, Identity or Professional authority.

## 38.3 Role changes are consequential when capture changes

Changing a participant from attendee to a speaking/on-stage role may materially change:

- voice capture;
- image/video capture;
- display identity exposure;
- transcript/caption inclusion;
- screen-share capability;
- likelihood of sensitive personal disclosure;
- downstream editing/replay significance.

Therefore a role transition that expands capture cannot be treated as a purely provider-side UI action. It must remain consistent with the current role/context participation rule already required by `LIVE-UPD-005`.

Exact permission mechanics remain OQ-021/JIT work.

## 38.4 Recording participation authority does not authorise sensitive content publication

A participant may lawfully satisfy the current rule for being captured and still disclose material that should not be included in a governed replay.

Therefore:

```text
valid participation/capture authority
        !=
permission to publish every captured utterance/image/data item
```

Sensitive audience handling is a second governance question, not a substitute for recording participation authority.

## 38.5 Sensitive audience material can belong to someone else

A speaker/participant can reveal another person's private information. The speaker's own recording participation rule cannot manufacture authority over the third person's data.

This is particularly important for:

- family-member health details;
- practitioner/client examples;
- screenshots containing another person's information;
- names plus diagnoses/medication/trauma details;
- correspondence or records belonging to another person.

The fail-closed conclusion is only that such material cannot automatically flow into replay/publication merely because the session participant was authorised to speak.

Exact legal/remediation handling remains deferred.

## 38.6 Group educational boundaries survive recording

Recording does not turn group Q&A into a private consultation or clinical record.

Private diagnosis, prescription and treatment requests still route to professional pathways under locked Product Law. A practitioner appearing in a live session does not convert the whole occurrence into Professional Care authority.

Conversely, if a separate governed private professional interaction exists, that authority must come from the Professional Care/health/privacy model rather than from the live-session provider role.

---

# 39. Pressure tests — Pass E

## LIVE-PT-048 — Planned presenter or guest speaker joins a recorded occurrence

**Scenario class**

Role-specific recording participation / planned speaker.

**Why it matters**

Product Law explicitly distinguishes participant/speaker rules. A planned speaker is likely to have materially broader capture and downstream-use exposure than an ordinary attendee.

**Authority**

Product §21G.15; `DEC-188`; `OQ-021`; Privacy & Consent purpose authority; Identity & Access role context where applicable.

**Owning Domains**

Privacy & Consent for recording-purpose authority; Events & Live for occurrence role/association context; Identity & Access for canonical staff/practitioner identity/role; Content & Media for later captured media/edit/publication.

**Preconditions**

A recorded occurrence is planned; a named presenter/guest speaker will speak and may appear on camera/share screen.

**Timeline**

Speaker invited/assigned → applicable speaker rule exists → speaker joins/admitted → current rule evaluated → speaker presents → capture occurs → later media handling remains separate.

**Expected invariants**

- ordinary attendee terms do not automatically prove speaker permission;
- provider `panelist/host` state does not create NewYou speaker/privacy authority;
- applicable role/context is current and historically explainable;
- speaker capture authority does not itself approve promotional clips or every downstream use;
- replay publication remains Content & Media governance.

**Questions**

What materially differs between speaker and attendee rule? Does a contracted/paid guest require separate rights language? Does staff role change anything? These remain OQ-021/legal/Product questions.

**Adversarial variants**

Speaker joins through ordinary attendee link; provider promotes speaker automatically; substitute speaker appears; guest refuses camera but allows audio; speaker shares copyrighted/sensitive material.

**Analysis**

Current Product Law already requires a speaker-specific rule, so no new upstream principle is needed. The missing detail remains within accepted `LIVE-UPD-005` / OQ-021.

**Semantic disposition**

`BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE`

**Proof route**

`OQ-021 → JIT → CONTROLLED_LIVE_PROOF`

**UPD if any**

Refines `LIVE-UPD-005`; no new UPD.

**Evidence needed**

OQ-021 role-specific rule; later provider enforcement evidence.

---

## LIVE-PT-049 — Attendee is promoted to speaker/on-stage after admission

**Scenario class**

Role transition / capture-scope expansion.

**Why it matters**

An attendee may have satisfied one participation rule while the promotion exposes voice, image, transcript or screen share that were not previously active.

**Authority**

Accepted `LIVE-UPD-005`; Product §21G.15 participant/speaker distinction; Privacy current-authority doctrine.

**Owning Domains**

Events & Live for live occurrence/role context; Privacy & Consent for applicable recording-purpose authority; provider is enforcement/evidence only.

**Preconditions**

Participant is lawfully admitted as attendee; recording is active; host wishes to promote participant to a speaking role.

**Timeline**

Attendee admitted → host/operator requests promotion → role/capture scope would expand → current applicable speaker/participation rule must be evaluated → promotion allowed/refused according to approved policy → provider state follows the platform decision.

**Expected invariants**

- provider promotion cannot silently authorise broader capture;
- attendee admission evidence is not automatically speaker evidence;
- refusal/failure of the required current rule does not fabricate permission;
- role transition is historically explainable;
- prior attendance remains true even if promotion is refused.

**Questions**

Is explicit re-evaluation always required when capture scope materially expands? Can some occurrence policy cover planned attendee-to-speaker transitions in advance? What counts as material expansion?

**Adversarial variants**

Host promotes by mistake; participant begins speaking before re-evaluation completes; provider hotkey promotes instantly; promotion then immediately reverses.

**Analysis**

This is a direct application of accepted `LIVE-UPD-005`: current role/context matters at the consequential capture boundary. It strengthens the candidate without creating a separate Product decision package.

**Semantic disposition**

`NEEDS_WORKING_DELTA / COVERED_BY_LIVE-UPD-005`

**Proof route**

`OQ-021 + PRODUCT/PRIVACY_ADJUDICATION → JIT`

**UPD if any**

`LIVE-UPD-005` refinement only.

**Evidence needed**

Approved role-transition participation rule; later provider promotion/gating evidence.

---

## LIVE-PT-050 — Facilitator, host or staff member is captured in the recording

**Scenario class**

Staff/facilitator capture / role boundary.

**Why it matters**

Internal staff authority to operate a session is not automatically permission for every recorded/public use of their image, voice or contribution.

**Authority**

Product §21G.15 participant/speaker rules; Identity & Access scoped staff roles; Privacy & Consent purpose authority; Content & Media publication/rights.

**Owning Domains**

Identity & Access for staff identity/role; Privacy & Consent for recording-purpose authority; Events & Live for occurrence role context; Content & Media for later use/publication.

**Preconditions**

A facilitator/host/staff member operates or participates in a recorded session.

**Timeline**

Staff assigned operational role → session begins → staff voice/image/name may be captured → later recording/replay editing occurs.

**Expected invariants**

- operational staff role does not automatically equal unrestricted media rights;
- provider host status does not create canonical staff authority or publication permission;
- role/context and capture scope remain explainable;
- promotional clip use remains separately approved;
- staff capture does not change participant privacy rules.

**Questions**

Does employment/contract cover some speaker/recording rights? Which staff roles are on-camera versus operational-only? Those are legal/operations inputs to OQ-021, not JIT assumptions.

**Adversarial variants**

Support staff enters briefly; technician appears on camera; moderator speaks only during incident; staff uses personal provider account.

**Analysis**

Existing authority is enough to reject `staff role = blanket recording/publication permission`. Exact staff/contract rights remain OQ-021/legal/operations detail.

**Semantic disposition**

`BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE`

**Proof route**

`OQ-021 + LEGAL/OPERATIONS REVIEW`

**UPD if any**

Refines `LIVE-UPD-005`; no new UPD.

**Evidence needed**

Approved staff/facilitator rule and applicable contract/legal review.

---

## LIVE-PT-051 — Participant asks an ordinary educational Q&A question while recording

**Scenario class**

Audience participation / multi-surface capture.

**Why it matters**

A participant may contribute through voice, typed Q&A or chat, and the resulting capture may include identity and content even if camera/video is disabled.

**Authority**

`DEC-187` moderated educational Q&A; Product §21G.15 attendee privacy + sensitive-audience handling; accepted Pass-D capture-surface conclusions.

**Owning Domains**

Events & Live for occurrence/Q&A context as applicable; Privacy & Consent for recording-purpose authority; Content & Media for captured recording/editing/publication.

**Preconditions**

Participant is admitted under the current applicable recording rule; Q&A is enabled; recording is active.

**Timeline**

Participant submits/asks question → moderator admits/reads/responds → name/voice/text may be captured → full recording exists → later replay editing/publication remains separate.

**Expected invariants**

- camera-off does not mean non-capture;
- Q&A submission does not become public replay content automatically;
- participant display name/text/voice are distinct capture surfaces;
- moderation may prevent unsafe/private questions from being aired;
- replay editing may lawfully differ from raw capture without rewriting occurrence history.

**Questions**

Which Q&A modes are anonymous/pseudonymous/named? Can moderator paraphrase without exposing identity? Does typed Q&A enter provider recording/transcript? Provider capability is empirical later.

**Adversarial variants**

Moderator reads full participant name; typed private question displayed on-screen; question appears in transcript even though not read aloud; participant changes display name.

**Analysis**

The semantic separation is already supported by Pass D and Product Law. Exact Q&A privacy controls and provider capture behaviour remain OQ-021/OQ-020/JIT work.

**Semantic disposition**

`PASS_WITH_REFINEMENT / OQ-021_DEPENDENT`

**Proof route**

`OQ-021 → PROVIDER_EMPIRICAL → JIT`

**UPD if any**

None beyond `LIVE-UPD-005`.

**Evidence needed**

Approved Q&A participation/privacy rule; later provider evidence for Q&A/chat/transcript capture.

---

## LIVE-PT-052 — Participant discloses sensitive personal or health information during recorded Q&A

**Scenario class**

Sensitive audience material / participant disclosure.

**Why it matters**

A participant may satisfy the recording participation rule and still reveal material that Product Law says should be warned, redirected or moderated and that should not automatically enter replay/publication.

**Authority**

Product §21G.15 handling of sensitive audience material; `DEC-175`; `DEC-187`; existing community sensitive-disclosure prohibitions; Content & Media governed editing/publication.

**Owning Domains**

Privacy & Consent for purpose/privacy authority; Events & Live for occurrence/Q&A context; Content & Media for captured media/editing/publication; Safety & Eligibility / Professional Care only for their own governed downstream safety/professional consequences.

**Preconditions**

Recording active; participant lawfully admitted; participant asks or states highly sensitive health/personal information.

**Timeline**

Participant begins disclosure → moderator may interrupt/redirect → raw capture may already contain some/all disclosure → full recording retained/processed according to later governed rules → replay/publication decision must treat sensitive material separately.

**Expected invariants**

- valid recording participation authority does not authorise unrestricted replay of sensitive content;
- group Q&A does not become private diagnosis/prescription/treatment;
- moderator/provider state does not become privacy authority;
- raw capture history may exist while publication remains blocked/edited;
- downstream Safety/Professional Care consequences use their own authority, not the recording as a substitute health record;
- Analytics must not duplicate sensitive disclosure content.

**Questions**

What categories trigger mandatory omission/redaction from replay? When must moderator stop/redirect? Is participant follow-up required? What restricted evidence is retained? These are deferred to OQ-021/later correction/remediation passes.

**Adversarial variants**

Lab values; diagnosis; medication list; trauma history; pregnancy disclosure; mental-health crisis statement; private consultation request.

**Analysis**

This proves that `participation permission` and `publishable captured content` are independent gates. The existence of the sensitive-material rule is already Product Law; the remediation matrix remains unresolved under OQ-021 and later replay/correction work.

**Semantic disposition**

`BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE`

**Proof route**

`OQ-021 + LATER_REPLAY/CORRECTION_PASS`

**UPD if any**

No new UPD; refine `LIVE-GAP-003` and preserve `LIVE-UPD-005` role/context rule.

**Evidence needed**

OQ-021 sensitive-material handling rule; later replay editing/correction contract; provider capture evidence only after semantics.

---

## LIVE-PT-053 — Participant reveals another person's private information

**Scenario class**

Third-party privacy / sensitive audience material.

**Why it matters**

A participant cannot create authority over another person's private data merely by being allowed to speak on a recorded session.

**Authority**

Product sensitive-disclosure rules; §21G.15 attendee privacy/sensitive audience material; Privacy & Consent purpose authority; minimum-data doctrine.

**Owning Domains**

Privacy & Consent for applicable privacy handling; Content & Media for captured-media editing/publication; source Domains retain any pre-existing business truth if the information already exists there.

**Preconditions**

Participant is lawfully captured but mentions or shows another identifiable person's private health/personal information.

**Timeline**

Disclosure occurs → raw recording captures it → moderator may intervene → later media review identifies third-party material → replay/publication cannot infer permission from the speaker's authority.

**Expected invariants**

- speaker's participation rule cannot manufacture third-party permission;
- third-party information does not become Events/Content business truth merely because it was uttered;
- replay/public use fails closed pending lawful handling;
- no automatic Health Record is created for the third party;
- Audit/Analytics do not replicate the sensitive content unnecessarily.

**Questions**

What exact redaction/removal/incident route applies? Is participant notification required? How are already-generated transcripts/captions treated? These remain deferred.

**Adversarial variants**

Family member diagnosis; spouse medication; child's health details; another participant's name and condition; practitioner describes a client case too specifically.

**Analysis**

The authority boundary is clear enough to reject automatic publication. Exact remediation belongs to OQ-021/privacy/content correction, not a new Domain or Product principle.

**Semantic disposition**

`BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE`

**Proof route**

`OQ-021 + PRIVACY/CONTENT REMEDIATION`

**UPD if any**

None.

**Evidence needed**

OQ-021 third-party/sensitive-material handling plus later transcript/derivative propagation rules.

---

## LIVE-PT-054 — Practitioner or dietitian participates in recorded group Q&A

**Scenario class**

Professional role / group boundary.

**Why it matters**

A qualified practitioner may participate in educational Q&A, but provider host/panelist status must not convert a group session into private professional care or weaken the prohibition on private diagnosis/prescription/treatment in group Q&A.

**Authority**

`DEC-187`; practitioner access/relationship law; Professional Care ownership; Product §21G.15 speaker rules; Privacy & Consent.

**Owning Domains**

Professional Care for genuine professional relationship/case truth; Identity & Access for practitioner identity/role; Events & Live for live occurrence; Privacy & Consent for recording-purpose authority; Content & Media for recording/publication.

**Preconditions**

Verified practitioner/dietitian joins as presenter/guest; session is a group educational Q&A, not a private consultation.

**Timeline**

Practitioner admitted under applicable speaker rule → educational questions answered → participant asks for individual diagnosis/prescription → practitioner/moderator redirects to professional pathway → recording captures only what occurs → later replay governance separate.

**Expected invariants**

- practitioner provider role does not create active care relationship;
- group live occurrence does not become Professional Care authority by accident;
- private diagnosis/prescription/treatment requests are redirected;
- any actual professional follow-up uses separate governed relationship/consent/case authority;
- recording publication cannot expose private consultation material merely because practitioner was present.

**Questions**

How are borderline individualised questions handled? What participant-facing disclaimer is required? Those are Product/clinical/operations matters, not provider configuration.

**Adversarial variants**

Practitioner starts giving individual dosing advice; participant shares lab results on screen; practitioner recognises an existing client; emergency/safety concern arises.

**Analysis**

Current Product/Domain law is strong: recording/live transport does not alter professional-care authority. The remaining recording-specific privacy handling remains OQ-021.

**Semantic disposition**

`PASS_WITH_REFINEMENT / OQ-021_DEPENDENT`

**Proof route**

`JIT + CLINICAL/OPERATIONS POLICY + OQ-021`

**UPD if any**

None.

**Evidence needed**

JIT role boundary and approved group-Q&A operational wording; recording-specific rule from OQ-021.

---

## LIVE-PT-055 — Screen share or visual capture exposes sensitive information accidentally

**Scenario class**

Sensitive visual capture / operator mistake.

**Why it matters**

Sensitive material may enter the recording without being deliberately spoken, for example through notifications, participant lists, private messages, health records or another window on a shared screen.

**Authority**

Product §21G.15 sensitive audience handling; minimum-data/privacy doctrine; Content & Media editing/correction/withdrawal law; provider capture remains evidence.

**Owning Domains**

Privacy & Consent for privacy consequence; Content & Media for captured media/editing/publication; Events & Live for occurrence context; source Domain remains owner of any underlying business record accidentally displayed.

**Preconditions**

Authorised speaker/host shares screen or provider layout includes information not intended for replay exposure.

**Timeline**

Screen share begins → sensitive window/notification/data appears → recording captures frames/audio → operator notices during or after session → raw artifact exists → replay/publication must fail closed until governed handling.

**Expected invariants**

- screen-share permission does not transfer ownership of displayed data;
- accidental visual capture cannot create publication authority;
- original source-domain truth is not copied into Events merely because captured;
- derived transcript/thumbnail/clip generation cannot bypass sensitive handling;
- provider `recording complete` remains irrelevant to replay approval.

**Questions**

What review/redaction threshold applies? Must raw media be access-restricted immediately? How are thumbnails/transcripts/AI derivatives suppressed? Deferred to later replay/privacy/processor passes.

**Adversarial variants**

Desktop notification with diagnosis; participant roster; private chat; email; health-record screen; another person's name; browser autofill/password manager popup.

**Analysis**

The semantic rule is already implied by sensitive-material governance and owner boundaries. The exact remediation/derivative-suppression mechanism remains downstream.

**Semantic disposition**

`PASS_WITH_REFINEMENT / REMEDIATION_DEFERRED`

**Proof route**

`OQ-021 + CONTENT/JIT + LATER_REPLAY/CORRECTION_PASS`

**UPD if any**

None.

**Evidence needed**

Approved sensitive-capture handling and later derivative propagation/correction proof.

---

## LIVE-PT-056 — Provider role label disagrees with NewYou role/context

**Scenario class**

Provider role evidence / authority mismatch.

**Why it matters**

A provider can label a person `host`, `panelist` or equivalent for delivery reasons even when NewYou has not granted the corresponding business/staff/practitioner context.

**Authority**

Identity & Access owns canonical identity/roles; provider state is evidence only; Privacy & Consent owns recording-purpose authority; Events owns occurrence participation context.

**Owning Domains**

Identity & Access; Events & Live; Privacy & Consent. Provider remains non-authoritative.

**Preconditions**

Provider role assignment differs from current platform role/context because of operator error, provider default, stale sync or direct provider administration.

**Timeline**

NewYou context says attendee → provider says panelist/host → provider may expose speaking/capture controls → NewYou receives evidence → no canonical role/privacy authority changes merely from provider state.

**Expected invariants**

- provider role does not create staff/practitioner authority;
- provider role does not create recording permission;
- provider mismatch is visible/reconcilable operational evidence;
- where provider cannot enforce NewYou role/capture policy, that is an OQ-020 blocker/limitation;
- correction must not rewrite historical identity/role truth.

**Questions**

Can chosen provider prevent direct out-of-band role promotion? What provider evidence and webhook/API controls exist? Those are later empirical questions.

**Adversarial variants**

Provider admin promotes participant directly; stale panelist link reused; host transfers host role; provider account email belongs to someone else.

**Analysis**

The NewYou authority rule is already clear. Provider enforcement is empirical and falls under accepted `LIVE-GAP-013` / OQ-020 rather than a new upstream semantic gap.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`PROVIDER_EMPIRICAL + JIT`

**UPD if any**

None; reinforces `LIVE-GAP-013`.

**Evidence needed**

OQ-020 provider role/promotion controls and controlled mismatch tests.

---

# 40. Pass-E gap and UPD adjudication

## 40.1 LIVE-UPD-005 is sufficient; no LIVE-UPD-006

**Decision:** no new upstream-delta identifier is justified by this pass.

Reasoning:

1. Product Law already requires distinct participant/speaker consent rules, attendee privacy controls and sensitive audience-material handling.
2. Accepted `LIVE-UPD-005` already requires the eventual recording participation contract to state the applicable rule for each relevant role/context and to re-evaluate consequential changes.
3. The new role-transition cases therefore refine an existing accepted decision package rather than expose a different Product authority problem.
4. Sensitive audience handling is already an explicit Product requirement. What remains unresolved is the detailed remediation/edit/replay consequence under OQ-021 and later Content/Privacy work.

Creating `LIVE-UPD-006` now would duplicate current Product Law and fragment one coherent OQ-021 decision package.

## 40.2 LIVE-GAP-003 refinement; no LIVE-GAP-014

Existing `LIVE-GAP-003 — RECORDING_PRIVACY_GATE` is refined to explicitly include:

- planned speaker/guest/facilitator/staff recording rules;
- attendee → speaker/on-stage role transition;
- capture-surface expansion by role change;
- Q&A/chat/display-name/transcript capture;
- sensitive participant health/personal disclosure;
- third-party private information disclosed by a participant;
- practitioner participation in recorded group Q&A;
- accidental visual/screen-share sensitive capture;
- the distinction between lawful capture participation and publishable replay content.

No `LIVE-GAP-014` is created. These questions share the same governing Product/Privacy/OQ-021 seam and should not be split merely because the scenarios are operationally different.

`LIVE-GAP-013` remains the provider-enforcement empirical gate and is reinforced by provider role/promotion mismatch cases.

---

# 41. Pass-E semantic synthesis

This focused pass adds nine proposed working conclusions:

1. **Role/context and capture scope are separate facts.** Attendee, speaker, guest, facilitator, staff and practitioner contexts can carry different capture consequences.
2. **Provider role labels are evidence/delivery state, not canonical NewYou identity, staff/practitioner authority or recording permission.**
3. **A role transition that materially expands capture is a consequential boundary.** Attendee admission evidence must not silently become speaker capture authority.
4. **Operational staff authority is not blanket media/publication permission.** Host/facilitator status must remain distinct from recording/downstream-use rights.
5. **Q&A participation can be captured through text, voice, display identity, captions/transcripts or video even when camera/mic assumptions suggest otherwise.**
6. **Valid participation/capture authority does not make every captured statement publishable.** Sensitive audience-material handling is a second governance gate.
7. **A participant cannot manufacture authority over another person's private information by disclosing it on a recorded session.**
8. **Recorded group Q&A remains group educational Q&A.** Practitioner presence does not create a private professional-care relationship or permit private diagnosis/prescription/treatment in group context.
9. **No new UPD or gap identifier is warranted.** `LIVE-UPD-005`, `LIVE-GAP-003` and `LIVE-GAP-013` already provide the correct routing if refined rather than duplicated.

No legal sufficiency finding is made. No provider capability is assumed. No Resource/schema/moderation workflow/automatic detection/editing mechanism is selected.

---

# 42. Current proposed register additions from Pass E

If accepted, the cumulative register should add:

- `LIVE-PT-048...LIVE-PT-056`;
- the nine Pass-E semantic conclusions in §41;
- refinements to `LIVE-UPD-005`, `LIVE-GAP-003` and `LIVE-GAP-013`;
- an explicit reserved fact that **no `LIVE-UPD-006` and no `LIVE-GAP-014` exist after Pass E**;
- no `LIVE-EV-*` entries.

The accepted identifier ranges would then remain:

- `LIVE-UPD-001...LIVE-UPD-005` only;
- `LIVE-GAP-001...LIVE-GAP-013` only.

---

# 43. Stop point and next-pass boundary

**Pass E stops here.**

The next focused pass, only after acceptance, should be:

> **Consent/permission withdrawal after capture, including one participant withdrawing from a multi-person recording, without yet deciding retention periods or Full Deletion.**

That pass should pressure-test:

- withdrawal while session is still live;
- withdrawal after raw capture but before replay approval;
- withdrawal after replay publication;
- one participant withdrawing from a multi-person recording;
- speaker withdrawal versus attendee withdrawal;
- already-created transcript/caption/thumbnail/clip derivatives;
- whether lawful historical occurrence/attendance remains true;
- separation between withdrawal of recording-purpose authority and Full Deletion.

It must still defer:

- exact retention durations;
- Full Deletion orchestration;
- external processor deletion deadlines/mechanics;
- final replay correction/replacement/withdrawal taxonomy beyond what is necessary to identify withdrawal consequences;
- communications policy;
- provider-specific deletion capabilities until NewYou semantics are explicit.
