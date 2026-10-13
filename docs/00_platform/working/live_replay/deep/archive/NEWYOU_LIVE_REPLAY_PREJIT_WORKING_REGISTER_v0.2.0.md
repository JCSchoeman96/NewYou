# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PROPOSED REGISTER SUCCESSOR
- **Document version:** v0.2.0
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.1.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Pre-pass accepted register commit:** `f3d705ee6fa434a1024caa3e026a7dd06a3ac927`
- **Pass D discovery commit:** `df5dc0871e956ac4060c3f27bafcb072ec242ecd`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic rule:** all `ACCEPTED_WORKING_LOCK` entries in v0.1.0 remain unchanged. This successor adds proposed Pass-D findings only. Until the user explicitly accepts Pass D, the new items below are not part of the accepted working lock.

---

# 1. Cumulative interpretation

Read this file together with `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.1.0.md`.

The predecessor remains the complete accepted register for Passes A–C:

- `LIVE-PT-001...LIVE-PT-039`;
- `LIVE-UPD-001...LIVE-UPD-004`;
- `LIVE-GAP-001...LIVE-GAP-012`;
- no `LIVE-EV-*` entries;
- accepted working conclusions through raw-capture Pass C.

Nothing in that accepted predecessor is reopened by Pass D.

Pass D adds only the recording notice/admission/join semantics below.

---

# 2. Pass register addition

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| D | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.4.0.md` | `df5dc0871e956ac4060c3f27bafcb072ec242ecd` | recording notice and consent/permission at admission/join, including late join and recording-intent change after admission | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Passes A–C remain `ACCEPTED_WORKING_LOCK` in v0.1.0.

---

# 3. Proposed Pass-D working conclusions

The following conclusions are **proposed** until Pass D is accepted:

1. **Recording notice and recording permission/consent are not one fact.** Product Law already distinguishes explicit notice, participant/speaker consent rules and participant controls.
2. **Registration does not permanently freeze recording authority.** The current applicable recording policy and current Privacy authority must be evaluated at the consequential admission/capture boundary.
3. **Late joiners receive no exemption because recording is already active.** The current rule must be satisfied before their captured participation begins.
4. **Declining or lacking required recording authority is a Product outcome question.** Deny, watch-only, non-captured participation or another alternative must be explicitly governed rather than inherited from provider defaults.
5. **Participant controls must reflect actual capture surfaces.** Camera-off alone cannot be assumed to mean non-capture where name, chat, Q&A, voice or transcript may still be recorded.
6. **Changing from non-recorded to recorded after admission is a participant-facing policy transition.** The provider's record toggle cannot silently authorise it.
7. **Provider-native notices/prompts are evidence/enforcement capability only until deliberately mapped into Privacy & Consent authority.**

These conclusions make no legal-sufficiency finding and do not choose a provider or implementation representation.

---

# 4. Pressure-test additions

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-040` | Ordinary recorded session: current notice and required recording rule satisfied before admission | v0.4.0 | `PASS_WITH_REFINEMENT / OQ-021_DEPENDENT` | `OQ-021 → JIT → CONTROLLED_LIVE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-041` | Recording policy changed after registration but before join | v0.4.0 | `NEEDS_WORKING_DELTA` | `OQ-021 + PRODUCT/PRIVACY_ADJUDICATION` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-042` | Late joiner arrives after recording is already active | v0.4.0 | `NEEDS_WORKING_DELTA` | `OQ-021 + PROVIDER_EMPIRICAL + JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-043` | Participant declines the applicable recording participation rule | v0.4.0 | `NEEDS_WORKING_DELTA` | `OQ-021 + PRODUCT_DECISION_PROMOTION` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-044` | Camera and microphone are off but chat/Q&A/display identity may still be captured | v0.4.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 + LATER_FOCUSED_SENSITIVE_CAPTURE_PASS` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-045` | Presenter, guest speaker or facilitator enters a recorded session | v0.4.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 + LATER_FOCUSED_ROLE_PASS` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-046` | Recording intent changes from false to true after participants have already been admitted | v0.4.0 | `NEEDS_WORKING_DELTA` | `OQ-021 + PRODUCT/PRIVACY_ADJUDICATION` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-047` | Provider-native recording notice/acknowledgement exists but NewYou has no canonical permission conclusion | v0.4.0 | `PASS_WITH_REFINEMENT` | `OQ-021 → PROVIDER_EMPIRICAL → JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Detailed preconditions, timelines, invariants, adversarial variants and evidence needs remain in the v0.4.0 discovery artifact and are not duplicated here.

---

# 5. Proposed upstream-delta addition

## LIVE-UPD-005 — Define the recording participation contract at admission and recording-policy change

**Status:** `PROPOSED / AWAITING_USER_ACCEPTANCE / NOT AUTHORITY`

**Origin:** `LIVE-PT-040...LIVE-PT-047`, especially PT-041, PT-042, PT-043 and PT-046.

**Decision package to be resolved through existing OQ-021/Product/Privacy authority:**

1. what recording participation rule applies to each relevant role/context;
2. what current notice/policy scope that rule covers;
3. when it must be satisfied relative to captured participation;
4. whether prior registration-time evidence remains valid at admission and under what material-change rule;
5. how late joiners satisfy the current rule before entering a captured interaction context;
6. what Product outcome applies when required recording authority is absent or declined;
7. whether enabling recording after admission is prohibited or, if allowed, what governed re-evaluation is required;
8. how provider-native controls may be used as evidence/enforcement without becoming Privacy authority;
9. confirmation that live entitlement, registration, attendance, general terms acceptance and provider presence do not automatically substitute for the recording-purpose rule.

**Owner/gate:** existing `OQ-021 — Video consent and retention` plus Product/Privacy governance. This candidate refines the decision package; it does not create a parallel legal gate.

---

# 6. Gap-register additions/refinements

## LIVE-GAP-003 refinement — recording notice/consent admission contract

**Existing classification:** `RECORDING_PRIVACY_GATE`

Proposed Pass D refinement adds these concrete questions to the existing OQ-021 gap:

- attendee recording rule at admission;
- registration-time evidence versus current join-time policy;
- late join after capture has begun;
- refusal/absence of required recording authority;
- material recording-policy change after registration/admission;
- participant capture surfaces such as voice/image/name/chat/Q&A;
- speaker/attendee role distinction;
- provider-native notice/acknowledgement mapping.

This remains one privacy/legal gate and does not create a second consent authority.

## LIVE-GAP-013 — Provider enforcement of recording-aware admission remains unverified

**Classification:** `PROVIDER_EMPIRICAL_GATE`

**Status:** `PROPOSED / AWAITING_USER_ACCEPTANCE`

After OQ-021 defines NewYou semantics, OQ-020/provider research must verify whether the selected path can enforce them, including as applicable:

- pre-admission/waiting-room gating;
- late-join gating while recording is active;
- participant camera/mic/interaction controls;
- host/manual-admit bypass behaviour;
- attributable provider notice/acknowledgement evidence;
- direct/deep-link behaviour;
- provider-native recording banners/prompts;
- recording start after people are already present.

Provider limitations may invalidate a configuration/path for protected interactive sessions; they cannot weaken NewYou authority.

No `LIVE-GAP-014` is created. Exact consent-record representation/version binding remains downstream JIT work after OQ-021 resolves the semantics.

---

# 7. Evidence register

No `LIVE-EV-*` item is added by Pass D.

Provider research remains deliberately deferred until the recording participation contract is accepted and OQ-021 has supplied enough semantics to know what provider controls must be tested.

---

# 8. Explicit non-decisions preserved

Pass D does **not** decide:

- legal sufficiency of any consent mechanism;
- exact notice text or UI;
- whether every attendee needs affirmative consent in every mode;
- exact role-specific speaker/guest/staff rules;
- consent withdrawal after capture;
- multi-person recording withdrawal consequences;
- retention durations;
- Full Deletion or processor deletion;
- replay publication/correction/withdrawal;
- promotional clip permission;
- provider/API/configuration selection;
- any Ash Resource, table, field, job or evidence-schema design.

---

# 9. Acceptance transition rule

If Pass D is accepted without semantic changes, the next register artifact should be a **non-semantic status patch** `v0.2.1` that changes Pass D / PT-040...047 / LIVE-UPD-005 / LIVE-GAP-013 from `PROPOSED / AWAITING_USER_ACCEPTANCE` to their accepted working-lock status.

If the user requests semantic changes, create a substantive successor instead and preserve this v0.2.0 unchanged.

No accepted Pass A–C entry should be rewritten in either case.

---

# 10. Proposed next-pass boundary

Only after Pass D acceptance:

> **Role and capture-scope distinctions: attendee vs speaker/guest/facilitator/staff, plus sensitive audience material, without yet addressing consent withdrawal, retention or deletion.**

Do not automatically proceed into that pass merely because this register names it.
