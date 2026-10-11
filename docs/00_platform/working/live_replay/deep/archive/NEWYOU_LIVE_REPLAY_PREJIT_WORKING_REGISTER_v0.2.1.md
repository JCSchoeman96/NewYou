# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.1.md

- **Status:** WORKING / NON-AUTHORITATIVE / ACCEPTED STATUS SUCCESSOR
- **Document version:** v0.2.1
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Pass D discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.4.0.md`
- **Pass D discovery commit:** `df5dc0871e956ac4060c3f27bafcb072ec242ecd`
- **Predecessor register commit:** `34df0cfb2d69648a03b87893746919d7c298f0f5`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **SemVer scope:** non-semantic status patch only. No pressure-test analysis, semantic conclusion, gap classification, upstream-delta content or deferred boundary is changed from v0.2.0.

---

# 1. Acceptance promotion

The user explicitly accepted and approved Pass D without semantic changes.

Therefore the following v0.2.0 items move from:

`PROPOSED / AWAITING_USER_ACCEPTANCE`

to:

`ACCEPTED_WORKING_LOCK`

This working lock means the accepted discovery conclusion is stable planning evidence and should not be reopened casually. It is **not** Product Law, Architecture Law, Domain Law, Roadmap Law, legal advice, provider validation or implementation authority.

Reopen only for:

- new evidence;
- changed scope;
- contradiction with higher authority;
- explicit user-directed reconsideration;
- a genuine downstream JIT/proof finding that exposes a semantic defect.

---

# 2. Accepted pass register through Pass D

| Pass | Discovery artifact | Focus | Status |
|---|---|---|---|
| A | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.1.0.md` | authority baseline, truth separation, ordinary lifecycle and first pressure tests | `ACCEPTED_WORKING_LOCK` |
| B | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.2.0.md` | occurrence identity, schedule/version, execution outcomes, registration/access/attendance and in-progress access | `ACCEPTED_WORKING_LOCK` |
| C | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.3.0.md` | recording intent and raw-capture boundary | `ACCEPTED_WORKING_LOCK` |
| D | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.4.0.md` | recording notice and consent/permission at admission/join, including late join and policy change after admission | `ACCEPTED_WORKING_LOCK` |

---

# 3. Accepted Pass-D pressure tests

The following pressure tests are now accepted working evidence with their v0.4.0 analysis/dispositions unchanged:

- `LIVE-PT-040` — Ordinary recorded session: current notice and required recording rule satisfied before admission.
- `LIVE-PT-041` — Recording policy changed after registration but before join.
- `LIVE-PT-042` — Late joiner arrives after recording is already active.
- `LIVE-PT-043` — Participant declines the applicable recording participation rule.
- `LIVE-PT-044` — Camera and microphone are off but chat/Q&A/display identity may still be captured.
- `LIVE-PT-045` — Presenter, guest speaker or facilitator enters a recorded session.
- `LIVE-PT-046` — Recording intent changes from false to true after participants have already been admitted.
- `LIVE-PT-047` — Provider-native recording notice/acknowledgement exists but NewYou has no canonical permission conclusion.

All eight are `ACCEPTED_WORKING_LOCK` as discovery evidence. Their underlying unresolved Product/Privacy/provider gates remain unresolved exactly as classified in v0.4.0.

---

# 4. Accepted LIVE-UPD-005 candidate

## LIVE-UPD-005 — Define the recording participation contract at admission and recording-policy change

**Working status:** `ACCEPTED_WORKING_LOCK / CANDIDATE UPSTREAM DECISION PACKAGE / NOT AUTHORITY`

The accepted working direction is that existing `OQ-021` / Product / Privacy governance must eventually state:

1. what recording participation rule applies to each relevant participant role/context;
2. what current notice/policy scope that rule covers;
3. when the rule must be satisfied relative to captured participation;
4. whether registration-time evidence remains valid at admission and under what material-change rule;
5. how late joiners satisfy the current rule before entering a captured interaction context;
6. what Product outcome applies when required recording authority is absent or declined;
7. whether enabling recording after admission is prohibited or, if allowed, what governed re-evaluation is required;
8. that provider-native controls are enforcement/evidence only unless deliberately mapped into Privacy & Consent authority;
9. that live entitlement, registration, attendance, general terms acceptance and provider presence do not automatically substitute for the recording-purpose rule.

This acceptance does not resolve OQ-021 and does not make the above legal policy.

---

# 5. Gap-register status through Pass D

`LIVE-GAP-003` remains one `RECORDING_PRIVACY_GATE` and now includes the accepted Pass-D refinements around:

- attendee recording rule at admission;
- registration-time evidence versus current join-time policy;
- late join after capture has begun;
- refusal/absence of required recording authority;
- material recording-policy change after registration/admission;
- voice/image/name/chat/Q&A capture surfaces;
- speaker/attendee role distinctions;
- provider-native notice/acknowledgement mapping.

`LIVE-GAP-013 — Provider enforcement of recording-aware admission remains unverified` is now:

`ACCEPTED_WORKING_LOCK / PROVIDER_EMPIRICAL_GATE`

It remains unresolved until OQ-021 defines the required NewYou semantics and later OQ-020/provider evidence establishes actual enforcement capability.

No `LIVE-GAP-014` exists yet.

---

# 6. Evidence status

No `LIVE-EV-*` items exist through accepted Pass D.

Provider research remains deliberately deferred until NewYou semantics are sufficiently explicit to define what evidence must be gathered.

---

# 7. Current accepted cumulative identifiers

- Pressure tests: `LIVE-PT-001...LIVE-PT-047`
- Working upstream decision packages: `LIVE-UPD-001...LIVE-UPD-005`
- Gap register: `LIVE-GAP-001...LIVE-GAP-013`, with no `LIVE-GAP-014`
- Evidence register: no `LIVE-EV-*` entries yet

All accepted items remain subject to higher authority and their recorded unresolved gates.

---

# 8. Explicit non-decisions still preserved

The accepted discovery still does **not** decide:

- legal sufficiency of a recording-consent mechanism;
- exact notice text or UI;
- exact role-specific speaker/guest/facilitator/staff recording rules;
- consent withdrawal after capture;
- consequences when one person withdraws from a multi-person recording;
- retention periods;
- Full Deletion or external-processor deletion;
- replay publication/correction/replacement/withdrawal;
- promotional-clip permission;
- communications policy;
- safety-content remediation beyond named seams;
- provider/API/configuration selection;
- Ash Resources, schemas, tables, fields, workers, queues or storage mechanisms.

---

# 9. Next focused pass boundary

The next approved focused pass is only:

> **Role and capture-scope distinctions: attendee vs speaker/guest/facilitator/staff, plus sensitive audience material, without yet addressing consent withdrawal, retention or deletion.**

It may pressure-test:

- planned and ad-hoc speakers;
- facilitator/host/staff participation;
- participant promotion to speaker/on-stage role;
- audience Q&A/chat/display-name capture;
- sensitive personal/health disclosure captured in recorded interaction;
- whether role/capture-scope changes require a distinct current recording rule.

It must still defer:

- post-capture withdrawal;
- one-person withdrawal from multi-person recording;
- Full Deletion;
- retention/provider deletion;
- replay publication/correction/withdrawal;
- communications;
- detailed safety-correction/remediation.

---

# 10. Cumulative-document rule

A separate downloadable human-review document may consolidate these accepted working results for easier review and later Pre-JIT compression.

That document is a convenience copy only. The versioned repository discovery ledgers and accepted register successors remain the precise provenance record for what was tested, when, and under which acceptance state.
