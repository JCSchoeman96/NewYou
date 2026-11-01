# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.3.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PROPOSED REGISTER SUCCESSOR
- **Document version:** v0.3.0
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.1.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted predecessor commit:** `2f1752f30fe9d26ad856f749c93b1bb6fe802932`
- **Pass E discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.5.0.md`
- **Pass E discovery commit:** `378cc9d8d900170f200d9a4524d9887e43e2d8f3`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic rule:** Passes A–D remain `ACCEPTED_WORKING_LOCK`. Pass-E additions below remain `PROPOSED / AWAITING_USER_ACCEPTANCE` until explicitly accepted.

---

# 1. Cumulative state

Accepted working lock currently covers:

- Pass A / discovery v0.1.0;
- Pass B / discovery v0.2.0;
- Pass C / discovery v0.3.0;
- Pass D / discovery v0.4.0;
- `LIVE-PT-001...LIVE-PT-047`;
- `LIVE-UPD-001...LIVE-UPD-005`;
- `LIVE-GAP-001...LIVE-GAP-013`;
- no `LIVE-EV-*` entries.

Pass E adds proposed role/capture-scope and sensitive-audience findings only. It does not reopen an accepted predecessor conclusion.

---

# 2. Pass register addition

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| E | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.5.0.md` | `378cc9d8d900170f200d9a4524d9887e43e2d8f3` | attendee vs speaker/guest/facilitator/staff roles, capture-scope changes and sensitive audience material | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

---

# 3. Proposed Pass-E working conclusions

1. **Role/context and capture scope are separate facts.** Attendee, speaker, guest, facilitator, staff and practitioner contexts can carry different capture consequences.
2. **Provider role labels are evidence/delivery state only.** They do not create canonical NewYou identity, staff/practitioner authority or recording permission.
3. **A role transition that materially expands capture is a consequential boundary.** Attendee admission evidence must not silently become speaker capture authority.
4. **Operational staff authority is not blanket media/publication permission.** Host/facilitator status remains distinct from recording/downstream-use rights.
5. **Q&A participation may be captured through text, voice, display identity, captions/transcripts or video.** Camera/mic state alone is not an adequate capture model.
6. **Valid participation/capture authority does not make every captured statement publishable.** Sensitive audience-material handling is a second governance gate.
7. **A participant cannot manufacture authority over another person's private information by disclosing it during a recorded session.**
8. **Recorded group Q&A remains group educational Q&A.** Practitioner presence does not create a private Professional Care relationship or permit private diagnosis/prescription/treatment in group context.
9. **No new upstream/gap identifier is warranted.** Existing `LIVE-UPD-005`, `LIVE-GAP-003` and `LIVE-GAP-013` are the correct routing seams when refined rather than duplicated.

These are proposed working conclusions only until accepted.

---

# 4. Pressure-test additions

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-048` | Planned presenter or guest speaker joins a recorded occurrence | v0.5.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 → JIT → CONTROLLED_LIVE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-049` | Attendee is promoted to speaker/on-stage after admission | v0.5.0 | `NEEDS_WORKING_DELTA / COVERED_BY_LIVE-UPD-005` | `OQ-021 + PRODUCT/PRIVACY_ADJUDICATION → JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-050` | Facilitator, host or staff member is captured in the recording | v0.5.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 + LEGAL/OPERATIONS REVIEW` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-051` | Participant asks an ordinary educational Q&A question while recording | v0.5.0 | `PASS_WITH_REFINEMENT / OQ-021_DEPENDENT` | `OQ-021 → PROVIDER_EMPIRICAL → JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-052` | Participant discloses sensitive personal or health information during recorded Q&A | v0.5.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 + LATER_REPLAY/CORRECTION_PASS` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-053` | Participant reveals another person's private information | v0.5.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 + PRIVACY/CONTENT REMEDIATION` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-054` | Practitioner or dietitian participates in recorded group Q&A | v0.5.0 | `PASS_WITH_REFINEMENT / OQ-021_DEPENDENT` | `JIT + CLINICAL/OPERATIONS POLICY + OQ-021` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-055` | Screen share or visual capture exposes sensitive information accidentally | v0.5.0 | `PASS_WITH_REFINEMENT / REMEDIATION_DEFERRED` | `OQ-021 + CONTENT/JIT + LATER_REPLAY/CORRECTION_PASS` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-056` | Provider role label disagrees with NewYou role/context | v0.5.0 | `PASS_WITH_REFINEMENT` | `PROVIDER_EMPIRICAL + JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Detailed timelines, invariants, adversarial variants, questions and evidence needs remain in discovery v0.5.0.

---

# 5. UPD register adjudication

No `LIVE-UPD-006` is created.

Pass E refines accepted `LIVE-UPD-005 — Define the recording participation contract at admission and recording-policy change` with these additional working requirements:

- applicable recording rule is role/context-aware;
- attendee → speaker/on-stage promotion may require current re-evaluation where capture materially expands;
- operational staff/provider role does not substitute for recording-purpose authority;
- valid participation/capture authority does not automatically authorise every captured statement or downstream use.

This remains one coherent OQ-021/Product/Privacy decision package.

---

# 6. Gap register adjudication

No `LIVE-GAP-014` is created.

`LIVE-GAP-003 — RECORDING_PRIVACY_GATE` is proposed to be refined with:

- planned speaker/guest/facilitator/staff recording rules;
- attendee → speaker/on-stage transition;
- capture-surface expansion by role change;
- Q&A/chat/display-name/transcript capture;
- sensitive participant health/personal disclosure;
- third-party private information disclosed by a participant;
- practitioner participation in recorded group Q&A;
- accidental visual/screen-share sensitive capture;
- the separation between lawful capture participation and publishable replay content.

`LIVE-GAP-013 — PROVIDER_EMPIRICAL_GATE` is reinforced by the provider-role mismatch scenario; provider labels/promotions must not become NewYou authority.

---

# 7. Evidence register

No `LIVE-EV-*` item is added.

Provider research remains deferred until the relevant NewYou/OQ-021 semantics are sufficiently explicit to define the provider evidence required.

---

# 8. Explicit non-decisions preserved

Pass E does **not** decide:

- legal sufficiency of speaker/attendee/staff permission wording;
- exact moderator workflow/UI;
- consent/permission withdrawal after capture;
- one participant withdrawing from a multi-person recording;
- retention periods;
- Full Deletion;
- processor/provider deletion;
- exact replay editing/correction/replacement/withdrawal rules;
- promotional clip permission;
- participant communications after sensitive disclosure;
- automated sensitive-content detection;
- provider/API/configuration selection;
- Ash Resource/schema/job/storage representation.

---

# 9. Acceptance transition rule

If Pass E is accepted without semantic changes, create non-semantic status successor `v0.3.1` that promotes:

- Pass E;
- `LIVE-PT-048...LIVE-PT-056`;
- the §3 Pass-E conclusions;
- the refinements to `LIVE-UPD-005`, `LIVE-GAP-003` and `LIVE-GAP-013`;

to `ACCEPTED_WORKING_LOCK`.

If semantic changes are requested, create a substantive successor instead and preserve this v0.3.0 unchanged.

---

# 10. Proposed next focused pass

Only after Pass E acceptance:

> **Consent/permission withdrawal after capture, including one participant withdrawing from a multi-person recording, without yet deciding retention periods or Full Deletion.**

That pass must distinguish withdrawal from Full Deletion and may only touch replay correction/withdrawal as far as necessary to define the recording-purpose consequence.
