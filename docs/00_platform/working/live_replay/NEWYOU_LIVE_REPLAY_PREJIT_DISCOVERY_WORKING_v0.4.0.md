# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.4.0.md

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY EVIDENCE
- **Document version:** v0.4.0
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.3.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Discovery predecessor commit:** `2d64f290a261826b70984cf3f0d61699db0ab631`
- **Pre-pass branch head:** `f3d705ee6fa434a1024caa3e026a7dd06a3ac927`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap amendment:** NONE
- **Register:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.1.0.md` locks accepted discovery through Pass C only; this Pass D remains proposed until separately accepted.
- **Pass scope:** recording notice and consent/permission at admission/join, including late join and recording-intent change around admission.

---

# 28. Pass D objective and hard boundary

This pass asks only:

> What must NewYou know and enforce before a participant or speaker enters a live context that is being recorded, including a late joiner and a recording-intent change after people have already been admitted?

This pass may establish:

- the distinction between recording notice and recording permission/consent authority;
- when current recording policy must be evaluated relative to registration/admission/capture;
- how a late joiner is treated when recording is already active;
- what must happen when recording intent changes after registration or admission;
- what Product/Privacy decision is required when a person declines whatever recording participation rule OQ-021 ultimately approves;
- why provider-native notice/consent controls remain evidence/enforcement capability rather than NewYou authority.

This pass deliberately does **not** decide:

- the legally sufficient form of recording consent;
- whether every attendee must affirmatively consent in every live mode;
- exact wording, checkbox design or UI presentation;
- legal basis by jurisdiction;
- consent withdrawal after capture;
- one participant withdrawing from a multi-person recording;
- retention periods;
- Full Deletion;
- processor deletion or backup handling;
- replay publication, correction or withdrawal;
- promotional clip permission;
- detailed speaker/guest/staff category rules beyond identifying their seam;
- sensitive audience-material remediation beyond identifying the capture risk;
- exact Restream/Cloudflare capabilities or configuration.

No provider research is performed in this pass. No `LIVE-EV-*` item is created.

---

# 29. Authority and adjacent-working-evidence extraction

## 29.1 Product / Decision authority

Current Product Law §21G.15 requires a recorded session to have:

- explicit recording notice;
- participant/speaker consent rules;
- attendee privacy controls;
- handling of sensitive audience material;
- governed editing;
- replay entitlement/expiry where applicable;
- content/version history;
- correction/withdrawal;
- separate promotional-clip approval.

A recording is not automatically public merely because the live session occurred.

`DEC-188 — Recording governance` is LOCKED and requires explicit recording notice, participant controls, governed editing, replay entitlements, versioning, correction and clip approval.

`OQ-021 — Video consent and retention` remains **LEGAL / OPERATIONS REVIEW** and explicitly requires speaker, attendee, recording, editing, replay, clip, retention and withdrawal rules to be defined.

Therefore this pass may identify the semantic contract OQ-021 must settle, but it may not invent legal sufficiency.

## 29.2 Domain ownership

Events & Live owns the occurrence and its session/event recording notice/association context.

Privacy & Consent is the sole owner of purpose-specific consent/current consent grants and withdrawals. Other domains may read/check that authority; they do not write a competing recording-permission truth.

Content & Media owns governed media identity/rights/publication after the capture/media handoff. Recording permission at admission is not Content publication authority.

Identity & Access establishes the canonical actor/account context where the participant is account-linked. Provider display name/email is not canonical identity.

## 29.3 Architecture / privacy execution rule

Current Architecture requires current authority before protected consequences and treats provider status/callbacks as evidence, not source truth.

The existing non-authoritative Privacy Pre-JIT contract is consistent with that authority and records the working execution rule:

```text
read current owner authority
→ read current purpose/consent/lawful-basis authority
→ execute only if still valid
```

That Privacy artifact is supporting working evidence only; it does not resolve OQ-021.

## 29.4 Existing cross-stream routing

The existing Content & Media working delta register already routes `CM-UPD-006` to `OQ-021` and explicitly says C&M media rights/publication do not override consent/privacy authority.

The existing Privacy working delta register also lists `OQ-021` as an existing gate that should not be duplicated.

This pass therefore refines `LIVE-GAP-003`; it does not create a competing recording-consent authority or a second legal gate.

---

# 30. Focused semantic model

This model is deliberately legal-mechanism-neutral.

## 30.1 Notice is not the same fact as permission

Current Product Law separately requires explicit recording notice and participant/speaker consent rules.

Therefore NewYou must not collapse these into one generic boolean such as `recording_ok`.

At minimum the platform must be able to distinguish:

- what the current occurrence says about recording intent;
- what recording notice/policy applied at the relevant time;
- whether the applicable Product/Privacy rule for this actor/role has been satisfied;
- whether provider capture is active;
- what participant controls are available/enforced.

The exact legal form of the permission/consent state remains OQ-021.

## 30.2 Registration is not permanent recording authority

A participant may register days or weeks before live execution.

Registration therefore cannot permanently freeze recording permission or notice state. At admission/join, NewYou must evaluate the **current** applicable occurrence recording policy and current Privacy authority required by the approved OQ-021 rule.

A prior registration interaction may supply valid evidence if the approved policy says it remains applicable, but JIT must not assume that merely because registration once succeeded.

## 30.3 Admission is a meaningful enforcement boundary

Where an attendee would enter a context in which her voice, image, display identity, chat/Q&A contribution or other participation may be recorded, admission is a consequential point at which current recording authority must be satisfied.

This does not mean every live mode must use the same consent mechanism. It means provider admission/capture cannot silently outrun NewYou's current policy decision.

If the selected provider cannot enforce the required NewYou boundary, that is a provider-path limitation under OQ-020, not permission to weaken the Product/Privacy rule.

## 30.4 Late join is not a special exemption

A participant who joins after recording has already begun must not be treated as though the earlier attendees' notice/permission automatically covers her.

The applicable current recording rule must be satisfied **before her participation enters the recorded context**, subject to whatever attendee/speaker/capture-mode semantics OQ-021 ultimately approves.

Exact provider waiting-room, player, mute, camera or interaction controls remain downstream empirical/JIT questions.

## 30.5 Recording-intent change after admission is a policy transition, not a provider toggle

Changing an occurrence from `not intended to be recorded` to `recording intended` after participants have already been admitted changes the participant-facing privacy context.

The provider's record button cannot be the authority for that transition.

Before future capture begins, NewYou must re-evaluate the current applicable recording notice/permission rules for already-admitted people. The pass does not prescribe whether that means fresh consent, acknowledgement, an opt-out path, a non-captured participation mode or refusal to start recording; OQ-021/Product must decide.

Changing from `recording intended` to `not intended` can stop future intended capture without erasing or adjudicating already-captured material. Treatment of prior bytes belongs to later privacy/withdrawal/retention passes.

## 30.6 Provider-native consent UI is not automatically NewYou consent authority

A provider may offer waiting-room text, recording banners, prompts or acknowledgements.

Those controls can be useful enforcement/evidence **only if** the governed NewYou contract deliberately accepts and reconciles them into the owning Privacy & Consent authority.

Provider acceptance, provider UI state or a provider checkbox cannot silently become the canonical NewYou purpose-permission record by default.

---

# 31. Pressure tests — recording notice and admission/join

## LIVE-PT-040 — Ordinary recorded session: current notice and required recording rule satisfied before admission

**Scenario class**

Recording notice / ordinary admission path.

**Why it matters**

The ordinary path must establish the minimum semantic boundary before late-join and policy-change cases can be judged.

**Authority**

Product §21G.15; `DEC-188`; Privacy & Consent purpose-specific authority; Events & Live recording notice/association ownership.

**Owning Domains**

Events & Live; Privacy & Consent; Identity & Access for actor context.

**Preconditions**

Occurrence intends recording. Applicable OQ-021 recording rule is assumed to exist for purposes of the scenario but its legal form is not invented here.

**Timeline**

Participant registers if required → opens current join surface → NewYou evaluates current occurrence recording policy → explicit notice is presented/available as required → applicable Privacy recording rule is satisfied → participant enters recorded context → provider may capture.

**Expected invariants**

- registration alone does not prove current recording authority;
- notice and purpose permission remain distinct facts where the approved rule requires both;
- the current rule is evaluated before recorded participation;
- provider admission/capture does not manufacture permission;
- the permission truth, where required, is Privacy & Consent authority;
- replay publication remains separate.

**Questions**

What exactly constitutes the required attendee rule: notice only, acknowledgement, explicit consent, role/capture-specific consent or another lawful basis/control model? How long may a prior valid recording grant remain applicable? OQ-021 must answer.

**Adversarial variants**

Participant registered a month earlier; notice wording changed; provider auto-joins; participant uses a deep link.

**Analysis**

The owner/enforcement boundary is clear. The legal/Product form of the recording rule remains unresolved.

**Semantic disposition**

`PASS_WITH_REFINEMENT / OQ-021_DEPENDENT`

**Proof route**

`OQ-021 → JIT → CONTROLLED_LIVE_PROOF`

**UPD if any**

Candidate `LIVE-UPD-005` below.

**Evidence needed**

OQ-021 approved attendee/speaker rule, then JIT evidence model and controlled admission proof.

---

## LIVE-PT-041 — Recording policy changed after registration but before join

**Scenario class**

Recording policy/current-authority revalidation.

**Why it matters**

A stale registration-time interaction must not silently authorise a materially different recording context at live admission.

**Authority**

Purpose-specific current consent authority; Product explicit recording notice/participant controls; Events occurrence/version ownership.

**Owning Domains**

Events & Live; Privacy & Consent.

**Preconditions**

Participant registered under recording policy/context A. Before live join, the current occurrence recording policy becomes B.

**Timeline**

Register under A → governed policy/intention change → participant opens join under B → NewYou evaluates whether prior permission/evidence remains applicable → current rule satisfied or admission to captured participation fails closed.

**Expected invariants**

- historical A remains explainable;
- current B is not overwritten by old registration evidence;
- a materially changed purpose/scope cannot be silently treated as identical merely because the same participant registered;
- provider join URL does not bypass current evaluation.

**Questions**

Which changes are material enough to require a new participant decision? Does a copy-only notice correction differ from changing `not recorded` to `recorded`, capture modes, reuse/replay scope or participant controls? Current authority does not fully define that boundary.

**Adversarial variants**

Recording added after registration; promotional-use language added; attendee capture mode changes; policy change occurs minutes before start.

**Analysis**

This is consequential Product/Privacy semantics. JIT cannot define materiality or assume old evidence covers new scope.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`OQ-021 + PRODUCT/PRIVACY_ADJUDICATION`

**UPD if any**

`LIVE-UPD-005`.

**Evidence needed**

Approved material-change/current-policy semantics before JIT freezes evidence/version binding.

---

## LIVE-PT-042 — Late joiner arrives after recording is already active

**Scenario class**

Late admission / already-active capture.

**Why it matters**

The late joiner is the clearest case where provider capture may already be running before NewYou evaluates the individual participant.

**Authority**

Product explicit recording notice and participant/speaker consent rules; purpose-specific current Privacy authority; provider capture non-authority.

**Owning Domains**

Events & Live; Privacy & Consent; Identity & Access where account-linked.

**Preconditions**

Recording is active. Participant has valid live access and, where applicable, registration, but has not yet satisfied the current recording participation rule.

**Timeline**

Recording active → participant opens join → access/registration checks pass → recording notice/current policy evaluated → applicable rule satisfied → only then participant may enter the captured interaction context.

**Expected invariants**

- recording already being active does not waive the late joiner's rule;
- another attendee's permission cannot cover this participant;
- provider auto-admit cannot become the privacy authority;
- if lawful captured admission cannot be achieved, the system fails closed for captured participation rather than fabricating permission.

**Questions**

Can Product offer a passive/watch-only path that avoids participant capture? Must late joiners be muted/camera-off until a current rule is satisfied? Can chat/Q&A still create capture? These answers depend on OQ-021 and provider capability.

**Adversarial variants**

Direct provider deep link; host manually admits; participant's camera/mic auto-enable; social-destination public viewer; participant joins during a sensitive Q&A segment.

**Analysis**

The fail-closed principle is clear; the alternative-path and exact permission rule are unresolved.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`OQ-021 + PROVIDER_EMPIRICAL + JIT`

**UPD if any**

`LIVE-UPD-005`.

**Evidence needed**

OQ-021 late-join rule plus OQ-020 admission/waiting-room/participant-control capability evidence.

---

## LIVE-PT-043 — Participant declines the applicable recording participation rule

**Scenario class**

Consent/permission refusal / Product experience.

**Why it matters**

A provider or JIT engineer must not decide whether refusal means no live access, watch-only access, non-captured participation or another alternative.

**Authority**

Product requires participant controls; Privacy owns purpose-specific permission; Entitlements owns live access independently.

**Owning Domains**

Privacy & Consent; Events & Live; Entitlements for the separate live right.

**Preconditions**

Participant otherwise has current live access. Occurrence intends recording. The approved recording rule requires a participant decision that the participant does not provide.

**Timeline**

Access valid → current recording notice/rule presented → participant declines/does not satisfy required permission → system must choose a governed outcome before participant enters captured participation.

**Expected invariants**

- refusal does not silently revoke unrelated general entitlement unless Product says the recorded session itself requires that condition;
- provider admission cannot override refusal;
- refusal cannot be converted to consent by attendance/join persistence;
- the Product outcome must be explicit rather than accidental provider behaviour.

**Questions**

Is the participant denied this occurrence entirely? Is a non-interactive/no-capture path required or merely optional? Can the participant watch while preventing camera/mic/chat capture? Does the answer vary by access mode or session type?

**Adversarial variants**

Participant declines but host manually admits; watch-only provider mode still records display identity; participant later tries Q&A; public livestream has no participant capture.

**Analysis**

This is a genuine Product/privacy participation decision. JIT/provider configuration cannot choose it safely.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`OQ-021 + PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-005`.

**Evidence needed**

Approved refusal/alternative-participation policy, then provider capability proof.

---

## LIVE-PT-044 — Camera and microphone are off but chat/Q&A/display identity may still be captured

**Scenario class**

Capture-scope ambiguity / attendee privacy controls.

**Why it matters**

A simplistic `camera off = not recorded` assumption can be false. Recorded participation can include more than audiovisual streams.

**Authority**

Product requires attendee privacy controls and handling of sensitive audience material; `DEC-188` requires participant controls; OQ-021 must define attendee/recording rules.

**Owning Domains**

Privacy & Consent; Events & Live for occurrence context; Content & Media later for captured media/derivatives.

**Preconditions**

Recorded session; participant enters with camera/mic disabled but can post chat, Q&A, polls or expose display identity.

**Timeline**

Join → camera/mic off → participant interacts or appears in provider UI → recording/export may include text/name/voice if later unmuted → replay/editing scope later remains separate.

**Expected invariants**

- participant controls must correspond to actual capture surfaces rather than a misleading single AV toggle;
- current authority must not promise non-capture where provider/export behaviour still captures participant-identifiable contribution;
- sensitive audience material cannot be treated as ordinary presenter content merely because it appeared in the live interface.

**Questions**

Which interaction surfaces count as recording participation for the approved Product/privacy rule? Are chat/Q&A exported into replay, transcript or operator artefacts? What controls/notice are required per surface?

**Adversarial variants**

Camera off but name overlay captured; chat appears on-screen in recording; host reads participant question aloud; auto-transcript records participant voice after temporary unmute.

**Analysis**

Current Product Law correctly requires attendee privacy controls, but the category-specific recording rule remains OQ-021 work.

**Semantic disposition**

`BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE`

**Proof route**

`OQ-021 + LATER_FOCUSED_SENSITIVE_CAPTURE_PASS`

**UPD if any**

`LIVE-UPD-005` only at the general admission-contract level; do not encode capture-category legal rules here.

**Evidence needed**

OQ-021 category semantics and later provider evidence about what is captured/exported.

---

## LIVE-PT-045 — Presenter, guest speaker or facilitator enters a recorded session

**Scenario class**

Role-specific recording permission seam.

**Why it matters**

Product Law explicitly names participant/speaker consent rules, which prevents the attendee rule from being assumed automatically sufficient for presenters or guest speakers.

**Authority**

Product §21G.15; `DEC-188`; Privacy purpose-specific authority; Events occurrence role/context.

**Owning Domains**

Privacy & Consent; Events & Live; Identity & Access for known platform actors.

**Preconditions**

Recording intended. Host/facilitator/guest speaker will be captured as part of the programme rather than merely attending.

**Timeline**

Role assigned/agreed → speaker enters production/live context → current role-specific recording rule evaluated → capture begins/continues → later replay/edit/clip permissions remain separate concerns.

**Expected invariants**

- attendee permission is not automatically speaker permission;
- employment/contract/guest arrangement cannot be guessed by JIT as sufficient recording authority;
- provider host role does not become consent authority;
- later promotional-clip use remains separately governed even where the full-session recording rule is satisfied.

**Questions**

Which role classes require separate agreements? Can staff/facilitator recording authority derive from an employment/contract basis rather than consent? What about spontaneous guest participation? These are legal/Product questions for OQ-021/later focused role pass.

**Adversarial variants**

Guest joins without pre-event paperwork; participant becomes ad-hoc panelist; staff member speaks briefly; external practitioner appears.

**Analysis**

The ownership and separation are clear, but the role-specific rule is intentionally unresolved.

**Semantic disposition**

`BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE`

**Proof route**

`OQ-021 + LATER_FOCUSED_ROLE_PASS`

**UPD if any**

No separate UPD yet; `LIVE-UPD-005` can require role-aware policy without deciding each role.

**Evidence needed**

Approved speaker/attendee/staff/guest rule matrix.

---

## LIVE-PT-046 — Recording intent changes from false to true after participants have already been admitted

**Scenario class**

Mid-session privacy-context transition.

**Why it matters**

This is the strongest test that the provider's record button cannot define Product/privacy truth.

**Authority**

Events owns occurrence recording intent/association; Product requires explicit recording notice and participant controls; Privacy owns purpose-specific authority.

**Owning Domains**

Events & Live; Privacy & Consent.

**Preconditions**

Participants entered under a `not intended to be recorded` occurrence context. Operator now wants to start recording.

**Timeline**

Participants admitted under non-recorded context → authorised operator requests policy change → NewYou records/authorises the occurrence-policy transition only if allowed → current recording rule must be satisfied for already-present actors → provider capture may begin only after the governed boundary is met.

**Expected invariants**

- provider record toggle is downstream of NewYou policy, not the policy itself;
- prior admission under non-recorded context is not recording permission;
- already-present participants must not be silently swept into a newly recorded purpose/context;
- if required participant authority cannot be satisfied, recorded capture fails closed or follows an explicitly approved alternative;
- historical policy timing remains explainable.

**Questions**

Is such a mid-session transition permitted at all? If yes, what re-notice/decision is required and what happens to people who decline? Is the safer Product rule to prohibit enabling recording after admission for first release?

**Adversarial variants**

Operator starts provider recording before completing NewYou transition; some participants are away from screen; one participant declines; recording is toggled off/on repeatedly.

**Analysis**

This cannot be left to JIT. Product/Privacy must define whether the transition exists and its participant consequences.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`OQ-021 + PRODUCT/PRIVACY_ADJUDICATION`

**UPD if any**

`LIVE-UPD-005`.

**Evidence needed**

Approved transition rule and later provider start/stop/control proof.

---

## LIVE-PT-047 — Provider-native recording notice/acknowledgement exists but NewYou has no canonical permission conclusion

**Scenario class**

Provider evidence versus Privacy authority.

**Why it matters**

Provider UX may tempt implementation to treat a provider banner/checkbox as sufficient canonical consent state.

**Authority**

Privacy & Consent sole ownership of purpose-specific current consent; provider state evidence only; Architecture authority-before-provider doctrine.

**Owning Domains**

Privacy & Consent; Events & Live for occurrence context; Audit & Evidence only if material evidence must be retained.

**Preconditions**

Provider displays its own recording notice or captures a provider-native acknowledgement; NewYou has not yet deliberately defined how that evidence maps to its governed recording rule.

**Timeline**

Provider prompt → user clicks/continues → provider says accepted/notified → NewYou receives provider evidence or no evidence → NewYou must not infer canonical purpose permission without a governed mapping.

**Expected invariants**

- provider checkbox/banner state does not become Privacy authority by default;
- provider evidence may support the governed NewYou conclusion only through an approved mapping;
- provider identity mismatch/anonymous join prevents unsafe attribution;
- duplicate/reordered provider events cannot duplicate or regress a canonical permission conclusion;
- provider UX changes cannot silently change NewYou legal/Product semantics.

**Questions**

Can provider controls satisfy part or all of the approved recording rule? Does the provider expose durable attributable evidence? Can NewYou supply its own pre-admission control instead? These are OQ-020/OQ-021 empirical/governance questions.

**Adversarial variants**

Provider changes wording; provider records only timestamp not text/version; attendee joins anonymously; host bypasses waiting room; provider acceptance event arrives late.

**Analysis**

The authority rule is already clear. The mapping/enforcement capability remains empirical/JIT work after OQ-021 defines the required semantics.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`OQ-021 → PROVIDER_EMPIRICAL → JIT`

**UPD if any**

`LIVE-UPD-005` for the platform contract; no provider-specific Product rule.

**Evidence needed**

Approved recording rule plus first-party provider documentation and controlled admission evidence later.

---

# 32. LIVE-UPD-005 — Define the recording participation contract at admission and recording-policy change

**Status:** WORKING CANDIDATE / NOT AUTHORITY

**Originating pressure tests:** `LIVE-PT-040...LIVE-PT-047`, especially PT-041, PT-042, PT-043 and PT-046.

**Current authority gap**

Current Product Law correctly requires explicit recording notice, participant/speaker consent rules and participant privacy controls; Privacy & Consent owns purpose-specific authority; OQ-021 explicitly keeps speaker/attendee rules open. What is missing for FP-007 JIT is the approved semantic contract connecting those rules to admission, late join and policy change.

**Candidate working direction**

The eventual OQ-021/Product/Privacy resolution should state, without provider-specific coupling:

1. what recording participation rule applies to each relevant participant role/context;
2. what current notice/policy scope that rule covers;
3. when the rule must be satisfied relative to captured participation;
4. whether prior registration-time evidence remains valid at admission and under what material-change rule;
5. how late joiners satisfy the current rule before entering a captured interaction context;
6. what Product outcome applies when required recording authority is not satisfied or is declined;
7. whether enabling recording after admission is prohibited or, if allowed, what governed re-evaluation is required;
8. that provider-native controls are enforcement/evidence only unless deliberately mapped into Privacy & Consent authority;
9. that general live entitlement, registration, attendance, terms acceptance and provider presence do not automatically substitute for the recording-purpose rule.

**Affected Domains**

Privacy & Consent; Events & Live; Identity & Access for actor/role context; Entitlements only for the independent live-right question; Content & Media later for captured-media use/publication.

**Why JIT cannot decide safely**

A waiting-room checkbox, provider auto-admit setting, join-button wording or database boolean would otherwise encode participant privacy and Product-access semantics that are still explicitly under legal/operations review.

**Existing governed gate**

`OQ-021` remains the owner/gate. `LIVE-UPD-005` refines the decision package; it does not create a parallel legal gate.

**Likely authority target**

Product/Privacy policy plus OQ-021 legal/operations resolution, followed by Events/Privacy JIT contract.

**Downstream impact**

FP-007 admission flow, late join, provider path validation, current permission checks, operator controls, audit evidence as applicable and controlled-live proof.

---

# 33. Gap-register refinement

## LIVE-GAP-003 refinement — recording notice/consent admission contract

**Classification:** `RECORDING_PRIVACY_GATE`

Existing `LIVE-GAP-003` now explicitly includes:

- attendee recording rule at admission;
- registration-time evidence versus current join-time policy;
- late join after capture has begun;
- refusal/absence of required recording authority;
- material recording-policy change after registration/admission;
- participant capture surfaces such as voice/image/name/chat/Q&A where applicable;
- speaker/attendee role distinction;
- provider-native notice/acknowledgement mapping.

This remains one OQ-021 privacy gate, not multiple competing gaps.

## LIVE-GAP-013 — Provider enforcement of recording-aware admission remains unverified

**Classification:** `PROVIDER_EMPIRICAL_GATE`

Once OQ-021 defines the required NewYou semantics, OQ-020/provider research must establish whether the selected path can enforce them, including as applicable:

- pre-admission/waiting-room gating;
- late-join gating while recording is active;
- participant camera/mic/interaction controls;
- host/manual-admit bypass behaviour;
- attributable provider notice/acknowledgement evidence;
- direct/deep-link behaviour;
- provider-native recording banners/prompts;
- behaviour when recording starts after people are already present.

Provider limitations may rule out a configuration/path for certain protected interactive modes; they do not weaken NewYou authority.

No `LIVE-GAP-014` is created. Exact consent-record representation/version binding remains downstream JIT work **after** OQ-021 supplies the semantics; escalating a representation question now would be premature.

---

# 34. Pass-D semantic synthesis

This focused pass adds seven proposed working conclusions:

1. **Recording notice and recording permission/consent are not one fact.** Product Law already distinguishes them; implementation must preserve that distinction.
2. **Registration does not permanently freeze recording authority.** Current applicable recording policy/Privacy authority must be evaluated at the consequential admission/capture boundary.
3. **Late joiners receive no exemption because recording is already active.** The current rule must be satisfied before their captured participation begins.
4. **Declining/absent recording authority is a Product outcome question, not a provider default.** Deny, watch-only, non-captured participation or another alternative must be explicitly decided.
5. **Participant controls must reflect actual capture surfaces.** Camera-off alone cannot be assumed to mean non-capture where name/chat/Q&A/voice/transcript may still be recorded.
6. **Changing from non-recorded to recorded after admission is a participant-facing policy transition.** A provider record toggle cannot silently authorise it.
7. **Provider-native notices/prompts are evidence/enforcement capability only until deliberately mapped into Privacy & Consent authority.**

The pass therefore proposes `LIVE-UPD-005` as a focused decision package under existing `OQ-021`, and adds `LIVE-GAP-013` as the later provider-enforcement evidence gate under OQ-020.

No legal sufficiency finding is made. No provider is selected/validated. No Resource, schema, consent checkbox, notice wording, retention duration, deletion rule or replay policy is selected.

---

# 35. Current stop point

**Pass D stops here.**

The next focused pass, only after acceptance, should be:

> **Role and capture-scope distinctions: attendee vs speaker/guest/facilitator/staff, plus sensitive audience material, without yet addressing consent withdrawal, retention or deletion.**

That pass should determine whether the general admission contract needs role/capture-specific Product refinements and should pressure-test ad-hoc speaker promotion, sensitive Q&A/chat, practitioner participation and recording of audience disclosures.

It must still defer:

- consent withdrawal after capture;
- one-person withdrawal from a multi-person recording;
- Full Deletion;
- provider/processor retention deletion;
- replay publication/correction/withdrawal;
- communications;
- safety-content correction except where needed to identify the capture seam.
