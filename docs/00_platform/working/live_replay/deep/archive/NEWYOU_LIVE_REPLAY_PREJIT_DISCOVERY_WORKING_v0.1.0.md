# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.1.0.md

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY EVIDENCE
- **Document version:** v0.1.0
- **Date:** 2026-10-09
- **Branch:** `prejit/live-replay`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap amendment:** NONE
- **SemVer rule:** append-only successors; semantic conclusions are superseded explicitly, never silently rewritten.

---

# 1. Purpose and scope

This ledger asks one narrow question:

> What must NewYou know and govern about a live occurrence from definition and scheduling through access, registration, attendance, provider execution, recording, replay, correction and withdrawal so that FP-007 JIT can implement rather than invent the lifecycle?

This is not implementation design, a generic webinar-platform design or the later scarce-capacity event-commerce problem.

The work deliberately keeps these dimensions separate:

1. NewYou occurrence truth;
2. provider state/evidence;
3. registration truth;
4. attendance truth;
5. entitlement/access truth;
6. recording/media truth;
7. privacy/consent truth;
8. communications truth;
9. audit evidence;
10. derived analytics.

Later scarce seats, paid capacity holds, ticket transfers, event refunds, reserved seating and flash-sale admission are **FUTURE / FP-015** unless a seam must be named to prevent FP-007 from absorbing them.

---

# 2. Exact live repository baseline

The live repository was resolved before substantive analysis.

## 2.1 Exact head

`main = 086ade7b28c000de1c387acb9760e5eb08bb0413`

This equals the creation-time baseline supplied for this stream. No baseline drift exists at v0.1.0 creation.

## 2.2 Current authority routing

Current routing at the exact baseline is:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `00_PLATFORM_v1.6.0.md`
- `01_DECISIONS_v1.6.0.md`
- `02_OPEN_WORK_v1.2.59.md`
- `03_ARCHITECTURE_v1.1.1.md`
- `04_DOMAIN_MAP_v1.2.0.md`
- `05_ROADMAP_v1.2.0.md`
- `PLATFORM_OPERATING_MODEL_v1.0.1.md`
- `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when frontend experience is material
- current supporting Engineering Standards: `reference/ENGINEERING_STANDARDS_v1.0.1.md`

Uploaded older snapshots are orientation evidence only and are not used to override this live baseline.

## 2.3 Current FP-007 position

Current Roadmap keeps the Feature Pack named:

`FP-007 — Governed live sessions and replay`

The current outcome requires an approved live session to be discoverable/registerable, current entitlement/access to be checked, protected playback to be joinable, governed replay to be available only where recording/consent allow, and provider/delivery failure to remain visible without becoming platform truth.

Current gates remain:

- `OQ-020 — BLOCKS_THIS_FP` — Restream/Cloudflare live validation;
- `OQ-021 — BLOCKS_THIS_FP` — recording/video consent/retention;
- `OQ-036 — BLOCKS_THIS_FP` only where a promised live notification journey depends on it;
- `OQ-017 — NON_BLOCKING_FOR_THIS_FP` until reminder delivery is an actual promise;
- `OQ-022 — FUTURE_ONLY` for ordinary FP-007 live access; scarce event reservation/performance belongs to FP-015.

Restream remains **PROVISIONAL / VALIDATION REQUIRED** under `DEC-189`. The preferred Restream → custom RTMPS → Cloudflare Stream platform path remains locked as direction with architecture detail pending under `DEC-190`; this does not resolve `OQ-020` empirically.

---

# 3. Authority extraction: what is already law

## 3.1 Events & Live

Current Domain Law gives **Events & Live** authority over:

- live-session/event definitions, versions and occurrences;
- registration/capacity/waitlist state;
- ticket/check-in/attendance truth where ticketing is in scope;
- session/event recording notice/association.

It explicitly does **not** own:

- payment/refund financial authority;
- the general entitlement system;
- replay/media publication;
- provider stream-delivery state as business truth.

Provider capture or stream status therefore cannot manufacture NewYou occurrence, registration, ticket, attendance, entitlement or replay-publication truth.

## 3.2 Entitlements

**Entitlements** owns entitlement identity, scope, source/provenance, validity, expiry and revocation. Current access is server-authoritative and stale cache cannot override revocation.

A provider invite, meeting membership, join URL, signed playback URL or provider-side attendee row is not entitlement authority.

## 3.3 Content & Media

**Content & Media** owns governed media identity, rights, derivatives and publication state. Provider/object IDs are not platform media identity. Published governed versions are immutable; corrections supersede or withdraw rather than silently rewrite history.

Current Architecture explicitly distinguishes provider capture from replay publication and distinguishes full recording, approved replay and promotional clips as separate governed publication/rights states. Captions and transcripts are derivatives.

## 3.4 Privacy & Consent

**Privacy & Consent** owns purpose-specific permission, withdrawal, retention/deletion orchestration, legal hold and export lifecycle. Participation does not imply unrelated consent. Withdrawal stops dependent future processing where applicable. Full deletion must cover eligible live, derived, cached, external-processor and access paths without blindly deleting records that must lawfully remain.

`OQ-021`, `OQ-029` and the processor deletion/export gates prevent this stream from inventing recording-retention or deletion law.

## 3.5 Communications

**Communications** owns communication preferences, quiet hours/frequency caps, durable message intent, delivery attempts/provider evidence and terminal-visible failure. It does not own the originating occurrence fact.

A late, duplicated, bounced or failed message cannot change whether a session was scheduled, rescheduled, cancelled, joined or attended.

## 3.6 Analytics

**Analytics** owns governed derived observations/projections/aggregates. It does not own attendance, entitlement, replay publication or provider truth. Provider analytics remain external evidence.

## 3.7 Audit & Evidence

**Audit & Evidence** owns append-only minimised central evidence where required. It never becomes a second occurrence, attendance, entitlement or media-publication authority.

---

# 4. Required semantic separation

| Dimension | Authoritative owner | What is authoritative | What must not masquerade as authority |
|---|---|---|---|
| Occurrence | Events & Live | NewYou live-session definition/version/occurrence and its lawful lifecycle | provider meeting/stream object, provider dashboard status |
| Registration | Events & Live | participant registration state for the occurrence | calendar invite, provider attendee list, message delivery |
| Attendance | Events & Live | governed attendance business fact after applicable evidence/reconciliation | provider join row alone, analytics event, replay view |
| Access / entitlement | Entitlements, with event-ticket admission remaining Events truth when later applicable | current right, scope, validity, expiry, revocation | join URL, playback URL, provider membership |
| Recording/media | Content & Media after governed media handoff/publication; Events retains occurrence association/notice context | media identity, lineage, derivatives, publication/correction/withdrawal | provider recording existence or processing status |
| Privacy/consent | Privacy & Consent | purpose-specific permission/withdrawal/retention/deletion orchestration | registration, attendance, provider checkbox unless reconciled into platform authority |
| Communications | Communications | intent, preference, delivery attempt/evidence | session lifecycle or access truth |
| Audit | Audit & Evidence | append-only evidence of governed actions | source business state |
| Analytics | Analytics | derived measurement | attendance, entitlement or replay publication truth |

This separation is the baseline invariant for all later pressure tests.

---

# 5. Ordinary lifecycle — first-pass semantic model

This is a **working semantic decomposition**, not a proposed database enum.

## 5.1 Occurrence lifecycle dimension

Authority clearly requires a stable NewYou occurrence and supports schedule/publish behaviour, but current law does not yet provide a complete FP-007 ordinary-state vocabulary. The minimum concepts that must be pressure-tested are:

`defined/draft → scheduled → visible/published → live execution → completed | cancelled | abandoned/failed`

Reschedule, delay and provider replacement may change schedule/provider bindings without silently creating a new NewYou occurrence. Whether a material schedule change creates a new occurrence version, and which changes preserve occurrence identity, remain unresolved documentary semantics.

## 5.2 Registration dimension

Registration is distinct from access and attendance. A registration may be valid even when a later entitlement check fails at join time; conversely Product Law permits access modes where explicit registration may not be required.

No registration state may be inferred merely because a provider join credential was issued.

## 5.3 Entitlement/access dimension

Access is evaluated from current owning authority. Registration does not freeze access forever. Protected playback authorises current access before issuing bounded delivery capability.

Unresolved Product semantics include what should happen if access expires or is revoked immediately before or during an already-running ordinary live session, and how live-right versus replay-right scope differs for each product family.

## 5.4 Attendance dimension

Attendance is Events & Live truth, but current Product Law does not define the business threshold for `attended` beyond privacy-preserving attendance and the registration → attended/no-show Domain profile shorthand.

Provider join duration, multiple connections, facilitator confirmation and manual correction are evidence candidates, not yet Product-defined attendance semantics.

## 5.5 Recording → replay dimension

A useful conceptual sequence is:

`provider/raw capture evidence → imported/governed media identity → optional edit/derivatives → approved published replay → superseded/replaced/withdrawn`

This is a boundary model, not an implementation schema. Recording existence never equals replay publication. Replay publication never equals participant replay entitlement. A working playback URL never proves either.

---

# 6. Initial unresolved gap register

## LIVE-GAP-001 — Complete occurrence lifecycle and schedule-version semantics

**Classification:** `PRODUCT_AUTHORITY_GAP`

Current authority establishes occurrence/version ownership and schedule/publish capability but does not answer all FP-007 identity-preserving reschedule/delay/provider-replacement cases.

## LIVE-GAP-002 — Provider/live path empirical validation

**Classification:** `PROVIDER_EMPIRICAL_GATE`

`OQ-020` remains open. No provider claims are accepted merely because the preferred path is documented.

## LIVE-GAP-003 — Recording consent/retention/deletion rules

**Classification:** `RECORDING_PRIVACY_GATE`

`OQ-021` remains open. This stream may identify required questions and proof but may not invent consent or retention law.

## LIVE-GAP-004 — Attendance business meaning

**Classification:** `PRODUCT_AUTHORITY_GAP`

Events owns attendance, but current authority does not define what evidence is sufficient to classify `attended`, whether duration matters, or how manual correction works.

## LIVE-GAP-005 — Replay-right policy across product/access sources

**Classification:** `PRODUCT_AUTHORITY_GAP`

Replay entitlement is required, but live entitlement, registration, attendance and replay entitlement are not declared equivalent. Product-family rules for membership/programme/once-off/sponsored/public access need explicit adjudication before JIT can encode them.

## LIVE-GAP-006 — Promised live communications

**Classification:** `COMMUNICATIONS_GATE`

`OQ-036` remains open for promised live communication journeys; optional reminders remain separately non-blocking under `OQ-017` until promised.

## LIVE-GAP-007 — Scarce event commerce

**Classification:** `FUTURE_EVENT_COMMERCE`

Capacity holds, paid waitlists, ticket transfers, event refunds/credits, seat allocation and flash-sale mechanics remain **FUTURE / FP-015**.

---

# 7. Candidate upstream semantic deltas

These are discovery findings only. They do not amend authority.

## LIVE-UPD-001 — Occurrence identity survives provider-resource replacement unless Product meaning changes

- **Originating PT:** `LIVE-PT-002`, reinforced by `LIVE-PT-003`.
- **Current authority gap:** Events owns the occurrence and Architecture makes provider identity non-authoritative, but current Product wording does not explicitly state which provider-room replacement/reschedule scenarios preserve the same occurrence versus create a replacement occurrence.
- **Candidate working direction:** define stable NewYou occurrence identity independently of provider session/stream IDs and require explicit supersession/replacement when Product meaning truly changes.
- **Affected Domains:** Events & Live; Content & Media; Communications; Audit & Evidence.
- **Why JIT cannot decide safely:** identity determines registration continuity, attendance history, sent-link staleness, replay association and historical explanation.
- **Provider/legal/privacy gate:** provider behaviour is `OQ-020`; no legal rule is decided here.
- **Likely authority target:** Product Law / Events & Live Domain Law clarification, then JIT specialisation.
- **Downstream impact:** FP-007 occurrence lifecycle, provider reconciliation, reschedule/cancel messaging and historical support.

## LIVE-UPD-002 — Attendance requires a Product-defined business meaning independent of provider attendee rows

- **Originating PT:** `LIVE-PT-006` and `LIVE-PT-007`.
- **Current authority gap:** Events & Live owns attendance; provider state is evidence; no approved threshold/evidence rule defines `attended` versus `no_show`.
- **Candidate working direction:** Product authority must choose the business meaning needed for FP-007 (for example whether any verified live presence is enough, whether duration/minimum/present-at-end matters, and whether facilitator confirmation is legitimate evidence). No threshold is proposed here.
- **Affected Domains:** Events & Live; Programmes & Challenges; Analytics; Audit & Evidence.
- **Why JIT cannot decide safely:** the definition affects programme participation, membership evidence, support corrections and analytics denominators.
- **Provider/legal/privacy gate:** provider identity/evidence quality under `OQ-020`; privacy minimisation under current law/OQ-021 where attendance evidence contains participant data.
- **Likely authority target:** Product Law decision, then Events & Live JIT reconciliation rules.
- **Downstream impact:** FP-007 acceptance/proof, FP-008 programme evidence, FP-009 live-value evidence and later Events.

## LIVE-UPD-003 — Live access and replay access need explicit product-family semantics

- **Originating PT:** `LIVE-PT-009` and `LIVE-PT-010`.
- **Current authority gap:** Product Law requires replay entitlement and allows replay expiry, while Entitlements owns current access. It does not state that live entitlement, attendance or registration implies replay entitlement.
- **Candidate working direction:** each relevant live product/occurrence must name live-access scope and replay-access scope separately, including validity/expiry/revocation/source and whether historical attendance changes nothing about current replay access.
- **Affected Domains:** Entitlements; Events & Live; Programmes & Challenges; Commerce only where a commercial source exists; Content & Media.
- **Why JIT cannot decide safely:** replay availability after membership cancellation, programme windows, missed live sessions, gifts/sponsorship and separately purchased rights are Product semantics.
- **Provider/legal/privacy gate:** recording availability still depends on `OQ-021`; provider playback protection on `OQ-020`.
- **Likely authority target:** Product Law / Entitlement semantics, then FP-007 JIT.
- **Downstream impact:** FP-007, FP-008, FP-009 and later event products.

---

# 8. Pressure tests — batch A

## LIVE-PT-001 — Ordinary live-to-replay journey

**Scenario class**

Normal lifecycle / reference flow.

**Why it matters**

FP-007 needs one coherent ordinary path before edge cases can be interpreted.

**Authority**

Roadmap FP-007; `DEC-186`, `DEC-188`, `DEC-190`, `DEC-206`, `DEC-279`; Platform §§21G.14–21G.16; Architecture §§7–10; Events & Live / Entitlements / Content & Media Domain Law.

**Owning Domains**

Events & Live; Entitlements; Content & Media; Privacy & Consent; Communications; Audit & Evidence; Analytics.

**Preconditions**

Authorised staff; approved session owner/content; applicable access rule; recording policy known; participant has any required current access.

**Timeline**

1. staff defines NewYou session;
2. occurrence is scheduled;
3. occurrence becomes visible;
4. participant passes current access requirement;
5. participant registers if required;
6. communications deliver appropriate details if configured;
7. participant joins;
8. participant may disconnect/reconnect;
9. session completes;
10. provider attendance/capture evidence arrives;
11. Events reconciles attendance;
12. recording/media processing occurs;
13. Content & Media publishes a governed replay if approved;
14. participant passes current replay entitlement check;
15. replay is consumed through bounded protected delivery;
16. history remains explainable after later correction/withdrawal.

**Expected invariants**

- provider state does not become occurrence/attendance/publication/entitlement authority;
- registration, access, attendance, replay publication and replay viewing remain distinct;
- recording existence does not imply publication;
- message delivery failure does not rewrite occurrence truth;
- historical occurrence and attendance can remain true after replay access ends.

**Questions**

What exact occurrence states/terminal states are Product-significant? What attendance meaning is needed? Which recording/replay state changes are Content-owned versus Events associations?

**Adversarial variants**

Disconnect/reconnect; recording late; delayed attendance webhook; replay processing before completion callback; replay withdrawn later.

**Analysis**

Authority is coherent on ownership but incomplete on the full ordinary occurrence and attendance lifecycle. JIT would otherwise invent business semantics around schedule identity, attendance qualification and replay-right policy.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-001`, `LIVE-UPD-002`, `LIVE-UPD-003`.

**Evidence needed**

Product adjudication of the semantic gaps; later provider evidence for `OQ-020`; privacy review for `OQ-021`; Phase-8 executable reconciliation/protected-playback proof.

---

## LIVE-PT-002 — Provider creates exactly one room for one NewYou occurrence

**Scenario class**

Occurrence identity / normal provider binding.

**Why it matters**

Even the happy path must establish which identifier carries business continuity.

**Authority**

Events & Live owns occurrence identity; Architecture makes provider IDs evidence/delivery only and media identity provider-independent.

**Owning Domains**

Events & Live; Content & Media.

**Preconditions**

One scheduled NewYou occurrence; provider create succeeds once.

**Timeline**

Occurrence created → provider resource created → provider identifier associated → session runs → evidence reconciles.

**Expected invariants**

NewYou occurrence identity does not equal provider identifier; provider association is replaceable evidence/configuration.

**Questions**

Does provider association itself need history/version provenance? Which changes are operator-visible history rather than Product state?

**Adversarial variants**

Provider changes its own mutable title/time; provider UI disagrees with API.

**Analysis**

The authority boundary is clear, but stable occurrence identity across later replacement deserves explicit downstream contract.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT`

**UPD if any**

`LIVE-UPD-001` only if Product-level identity/supersession semantics cannot be fully derived during subsequent PTs.

**Evidence needed**

JIT provider-association lifecycle and Phase-8 proof that provider mutation cannot overwrite occurrence authority.

---

## LIVE-PT-003 — Duplicate provider rooms after ambiguous create

**Scenario class**

Provider ambiguity / duplicate external resource.

**Why it matters**

A create timeout may succeed remotely; blind retry can create a second provider room and leak conflicting links.

**Authority**

Architecture provider-ingress/reconciliation doctrine; provider evidence is non-authoritative; ambiguous irreversible outcomes remain unresolved and reconcile before repeating harmful effect.

**Owning Domains**

Events & Live; Audit & Evidence for minimal evidence only; Communications if stale links were sent.

**Preconditions**

One NewYou occurrence; provider create request times out after unknown remote outcome.

**Timeline**

Create request → timeout/unknown → operator/job retries → provider now has A and B → NewYou must determine the active association without cloning occurrence truth.

**Expected invariants**

- at most one current provider association is treated as active for the occurrence at a time;
- duplicate provider resources do not create duplicate NewYou occurrences, registrations or attendance histories;
- abandoned provider resources are reconciled/disabled where provider capability allows;
- previously sent credentials are treated as potentially stale.

**Questions**

What provider evidence can prove existence/searchability/idempotent create? Can the provider support client-supplied idempotency or lookup by platform correlation? What operator action is required when both resources were used?

**Adversarial variants**

Both rooms receive participants; one records; host starts the wrong room; delete result is also ambiguous.

**Analysis**

NewYou semantic requirement is clear: provider multiplicity cannot multiply business identity. Exact recovery depends on provider capability and must not be guessed.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`PROVIDER_EMPIRICAL`

**UPD if any**

`LIVE-UPD-001`.

**Evidence needed**

`LIVE-EV` evidence under OQ-020 for provider create/idempotency/list/get/delete behaviour; controlled ambiguity tests later.

---

## LIVE-PT-004 — Registered participant whose entitlement expires before join

**Scenario class**

Registration/access separation.

**Why it matters**

Registration must not freeze a revocable access right.

**Authority**

Entitlements current-access law; Platform 21G.14 entitlement-aware registration; Architecture protected playback current-authority check.

**Owning Domains**

Events & Live; Entitlements.

**Preconditions**

Participant registered while entitled; entitlement later expires/revokes before session join.

**Timeline**

Register validly → entitlement ends → participant follows prior join path → current admission check occurs.

**Expected invariants**

- registration history remains true;
- access is denied if the current governing right no longer authorises join;
- stale join credentials cannot restore authority;
- denied join does not fabricate no-show/attendance semantics beyond whatever Product later defines.

**Questions**

Does any product promise grace for a currently running session or last-minute expiry? Does a commercial reversal produce different access timing from ordinary expiry?

**Adversarial variants**

Entitlement revoked five seconds before start; cached browser already has player page; signed provider URL remains technically valid.

**Analysis**

Authority clearly requires current access at protected playback. Product-specific grace semantics, if any, are not yet approved and must not be invented.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`PHASE8_EXECUTABLE`

**UPD if any**

Potentially `LIVE-UPD-003` for product-specific rights, not for the authority-first invariant.

**Evidence needed**

JIT access-check points and stale-capability invalidation contract; executable revocation tests.

---

## LIVE-PT-005 — Registered no-show versus joined participant

**Scenario class**

Registration/attendance separation.

**Why it matters**

Registration is intent; attendance is a later business fact.

**Authority**

Events & Live owns both registration and attendance as distinct rows of truth; Domain profile names registration → attended/no-show shorthand.

**Owning Domains**

Events & Live; Analytics downstream.

**Preconditions**

Two valid registrations; A never joins; B has provider join evidence.

**Timeline**

Both register → occurrence runs → provider evidence received → Events classifies after reconciliation.

**Expected invariants**

- registration does not equal attendance;
- no provider evidence must not automatically prove no-show when provider evidence itself may be missing;
- Analytics consumes the Events conclusion rather than defining it.

**Questions**

When provider evidence is incomplete, is attendance `unknown/pending` required rather than immediately `no_show`? When does the occurrence become final enough to classify no-show?

**Adversarial variants**

Provider attendance export is delayed or missing for all users; facilitator manually knows B attended.

**Analysis**

Ownership is clear but binary attended/no-show is insufficient under missing evidence unless an explicit unresolved/reconciliation state or equivalent lifecycle exists.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-002`.

**Evidence needed**

Approved attendance semantics including unresolved evidence and correction/finalisation behaviour.

---

## LIVE-PT-006 — Five-second join, reconnects and two devices

**Scenario class**

Attendance meaning / identity correlation.

**Why it matters**

Provider presence rows can overcount one human or misrepresent meaningful live attendance.

**Authority**

Events & Live attendance authority; provider evidence non-authoritative; privacy minimisation.

**Owning Domains**

Events & Live; Identity & Access for identity context; Analytics downstream.

**Preconditions**

One registered participant joins for five seconds, later reconnects, and at one point uses phone and laptop simultaneously.

**Timeline**

Provider emits multiple connection identities/durations → NewYou correlates evidence → one participant attendance conclusion is required.

**Expected invariants**

- multiple devices/connections do not create multiple participants;
- replay consumption is not live attendance;
- provider duration is evidence, not automatically the business threshold.

**Questions**

Does Product need joined-at-least-once, cumulative duration, a minimum duration, present-at-end, facilitator confirmation or another meaning? How are anonymous/weak-identity public streams treated?

**Adversarial variants**

Different provider email; display name changed; shared household device; host manually admits participant.

**Analysis**

This cannot be decided by JIT as a technical deduplication choice because it changes programme/live-value semantics and analytics interpretation.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-002`.

**Evidence needed**

Product attendance definition plus OQ-020 evidence on available provider identifiers/duration fields and correction APIs/exports.

---

## LIVE-PT-007 — Provider reports attendance late, then corrects it

**Scenario class**

Provider reorder/correction/reconciliation.

**Why it matters**

Attendance truth must remain correct when external evidence is delayed or amended.

**Authority**

Architecture duplicate/reorder/reconciliation doctrine; Events & Live attendance authority; Audit append-only evidence only.

**Owning Domains**

Events & Live; Audit & Evidence; Analytics derived.

**Preconditions**

Occurrence complete; initial provider evidence omitted participant; corrected provider report arrives later.

**Timeline**

Occurrence completes → evidence E1 → provisional/pending interpretation → evidence E2 correction → Events reconciles lawful business conclusion → Analytics later rebuilds/updates derived measurement.

**Expected invariants**

- callback arrival order is not authority;
- corrected evidence can change the authoritative attendance conclusion through a governed correction, not destructive historical falsification;
- Analytics follows corrected Events truth;
- Audit records the material correction without becoming attendance truth.

**Questions**

Does attendance need explicit finalised/corrected provenance? What is the support/operator correction authority when provider evidence remains wrong?

**Adversarial variants**

Correction arrives after programme completion calculation; duplicate correction; contradictory manual operator evidence.

**Analysis**

Reconciliation law is strong; the remaining gap is the business attendance definition and correction/finality lifecycle.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`JIT`

**UPD if any**

`LIVE-UPD-002`.

**Evidence needed**

JIT correction/finality lifecycle after Product defines attendance; executable duplicate/reorder tests.

---

## LIVE-PT-008 — Recording exists but replay is not yet governed

**Scenario class**

Recording/media ownership boundary.

**Why it matters**

Provider recording availability is the most likely place for external state to masquerade as NewYou publication truth.

**Authority**

Platform 21G.15; Architecture 10.3; Content & Media Domain Law; Events & Live explicitly does not own replay publication.

**Owning Domains**

Events & Live for occurrence association/notice context; Content & Media for media identity/publication; Privacy & Consent; Entitlements.

**Preconditions**

Recording was intended and provider reports a completed recording asset.

**Timeline**

Live ends → provider recording available → NewYou imports/associates evidence → governed media/rights/editing review occurs → replay may later publish.

**Expected invariants**

- provider recording existence != governed media publication;
- provider object ID != NewYou media identity;
- replay publication requires current lawful approvals/policy;
- participant access additionally requires current replay entitlement.

**Questions**

Which minimum states are needed for raw/imported/editing/approved/published/withdrawn/replaced media? Does every raw capture become a governed Content & Media asset or only once imported/accepted?

**Adversarial variants**

Multiple segments; corrupted recording; wrong screen; chat/private breakout captured; transcript arrives before video.

**Analysis**

The ownership boundary is already strong. Exact internal media workflow is JIT unless a Product promise depends on a state distinction. OQ-021 still gates recording/privacy semantics.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT`

**UPD if any**

None yet.

**Evidence needed**

Content & Media JIT lifecycle; OQ-021 privacy adjudication; OQ-020 provider recording behaviour.

---

## LIVE-PT-009 — Participant never saw recording notice

**Scenario class**

Recording privacy / consent gate.

**Why it matters**

Current Product Law requires explicit notice and participant/speaker consent rules, but the legal/product mechanism is not resolved.

**Authority**

`DEC-188`; Platform 21G.15; Privacy & Consent law; `OQ-021` open.

**Owning Domains**

Privacy & Consent; Events & Live for occurrence notice association; Content & Media for recording/replay publication; Audit & Evidence where required.

**Preconditions**

Recording is intended; participant joins late via a valid protected path but did not see pre-session notice.

**Timeline**

Participant entitled/registers → notice may be missed → participant joins → recording already active → participant voice/name may be captured.

**Expected invariants**

- attendance permission, communications permission, recording privacy/consent, replay entitlement and retention remain distinct;
- NewYou must not infer recording permission merely from attendance;
- provider UI notice cannot silently become platform consent authority unless governed authority explicitly accepts that evidence/mechanism.

**Questions**

What notice/consent model is legally/product acceptable? Must late joiners receive in-session notice? Are voice/name/chat treated differently? What are presenter/guest-speaker rules?

**Adversarial variants**

Camera off but voice recorded; host says participant name; participant posts sensitive chat; practitioner/health discussion accidentally captured.

**Analysis**

This is intentionally unresolved and cannot be fixed with plausible engineering prose.

**Semantic disposition**

`INSUFFICIENT_AUTHORITY`

**Proof route**

`LEGAL_PRIVACY_REVIEW`

**UPD if any**

None until `OQ-021` governed resolution supplies authority.

**Evidence needed**

OQ-021 legal/privacy/product decision; provider notice/control capabilities as empirical evidence afterward.

---

## LIVE-PT-010 — Live right ends but replay right may differ

**Scenario class**

Replay entitlement semantics.

**Why it matters**

Membership, programme, sponsored, public and future separately purchased access can have different durations and revocation rules.

**Authority**

Platform 21G.15 requires replay entitlement/expiry where applicable; Entitlements owns scope/validity/revocation; Domain Law separates replay eligibility from Events occurrence truth.

**Owning Domains**

Entitlements; Events & Live; Content & Media; Programmes & Challenges where programme-linked.

**Preconditions**

Occurrence completed and governed replay published.

**Timeline**

Participant had live access → live concludes → access source changes/ends → participant requests replay.

**Expected invariants**

- live attendance does not by itself create replay entitlement;
- missing live attendance does not by itself remove replay entitlement;
- current replay access derives from an explicit right/source;
- historical attendance remains true after replay access ends.

**Questions**

Membership cancellation: immediate/end-of-period? Programme replay window? Missed live but entitled replay? Separately purchased permanent/longer replay? Sponsored/gift access? Public replay?

**Adversarial variants**

Commercial reversal after attendance; account suspension; programme ends; replay corrected/replaced while entitlement remains.

**Analysis**

JIT cannot choose these product semantics. The entitlement system can represent them once Product states the rules.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-003`.

**Evidence needed**

Product-family replay-right matrix before FP-007 final JIT contract.

---

## LIVE-PT-011 — Leaked replay URL after entitlement revocation

**Scenario class**

Join/playback security.

**Why it matters**

A technically working URL must not become durable authority.

**Authority**

Architecture protected playback: current policy before bounded delivery capability; Entitlements stale-cache revocation invariant; Platform protected media uses entitlement checks and short-lived signed delivery links.

**Owning Domains**

Entitlements; Content & Media; Identity & Access.

**Preconditions**

Authorised participant obtained a valid replay delivery capability; entitlement is later revoked/expired; URL or screenshot is shared.

**Timeline**

Authorised request → bounded delivery issued → capability leaks → current right ends → attacker/original participant retries access.

**Expected invariants**

- possession of a stale URL is not entitlement;
- new protected access fails after revocation;
- caches cannot make revocation ineffective;
- exact token/link format is JIT, not Product Law.

**Questions**

How quickly must already-issued provider delivery capability cease? What provider controls are available to invalidate or bound playback sessions? What happens to an already-open player after expiry?

**Adversarial variants**

Same link on multiple devices; CDN cache; browser tab remains open; provider URL copied to anonymous browser.

**Analysis**

NewYou invariant is already clear; provider enforcement characteristics require OQ-020 empirical validation and exact mechanism belongs JIT/proof.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

Provider auth/signed playback/expiry/revocation behaviour; Phase-8 executable stale-access tests; later controlled-live leak exercise if needed.

---

## LIVE-PT-012 — Reschedule after registration and sent join details

**Scenario class**

Schedule lifecycle / communications seam.

**Why it matters**

A schedule correction can leave stale provider links and stale messages while the occurrence itself may remain the same business event.

**Authority**

Events & Live owns occurrence/registration; Communications owns sent-message state; provider state is evidence; dynamic business schedules remain governed business state.

**Owning Domains**

Events & Live; Communications; Entitlements; Audit & Evidence where material.

**Preconditions**

Occurrence published; participant registrations exist; prior message with date/time/join instructions was sent.

**Timeline**

Schedule changes → occurrence authority changes/version/supersession as governed → provider association may update/replace → new communication intent may be created → old sent message remains historical evidence.

**Expected invariants**

- sent message cannot be edited into current truth;
- occurrence schedule truth does not depend on delivery success;
- stale join link cannot override current access/current occurrence configuration;
- registration continuity is explicit rather than accidental.

**Questions**

Which reschedule changes preserve registration? When does a schedule correction create a replacement occurrence? Is re-acknowledgement ever required? What Product promise exists for cancellation/reschedule notice?

**Adversarial variants**

Five minutes before start; host timezone mistake; DST participant rendering; wrong date; provider room deleted/recreated; notification channel unavailable.

**Analysis**

The domain boundary is coherent, but occurrence identity/version semantics are not complete enough for JIT to decide silently.

**Semantic disposition**

`NEEDS_WORKING_DELTA`

**Proof route**

`PRODUCT_DECISION_PROMOTION`

**UPD if any**

`LIVE-UPD-001`.

**Evidence needed**

Occurrence reschedule/supersession decision; later JIT communication-dedup/current-link contract; OQ-036 only if the notification is promised.

---

# 9. Batch-A findings

The first batch supports these conclusions:

1. **Provider state is evidence, never NewYou occurrence/access/attendance/replay authority.** Current Domain and Architecture law are strong on this point.
2. **Events & Live, Entitlements and Content & Media are intentionally independent authorities.** A live occurrence can remain historically true while current access is gone and replay is withdrawn.
3. **Registration, entitlement, issued join capability, live presence, authoritative attendance, replay entitlement and replay view are independent facts.** No single status should collapse them.
4. **The most material documentary gaps are Product semantics, not technology:** occurrence identity/reschedule/supersession; attendance meaning/finality/correction; and live-right versus replay-right policy.
5. **Recording privacy is a real gate, not a wording exercise.** `OQ-021` remains unresolved and must route to legal/privacy governance.
6. **Provider validation should begin only against explicit NewYou invariants.** `OQ-020` must test provider create/reconcile/playback/recording/deletion behaviour, not decide NewYou business meaning.
7. **Full event commerce remains out.** Ordinary live access may reuse registration/capacity concepts where Product requires, but scarce paid holds/tickets/flash-sale mechanics remain FP-015.

---

# 10. Next pressure-test batches

The next semantic batches should cover, without re-running classes already resolved:

- detailed occurrence schedule states and terminal/recovery cases;
- entitlement changes during an in-progress session;
- purchaser ≠ participant, gift/sponsored/free/public access;
- full recording failure/corruption/edit/transcript/clip matrix;
- participant/presenter consent withdrawal and deletion after recording;
- replay correction/replacement/withdrawal and unsafe-content response;
- provider webhook reorder/missing/unknown/deletion ambiguity;
- communications confirmation/reminder/reschedule/cancellation/delayed-start/replay journeys;
- moderator/host/provider-outage/backup-provider operational scenarios;
- Full Deletion versus retained occurrence/attendance/audit/provider copies;
- second-pass adversarial mutations: duplicate/retry/reorder/crash/restart/outage/stale entitlement/privacy withdrawal/staff mistake/leaked link.

Provider empirical research will be performed only after the relevant NewYou semantic invariants are sufficiently explicit. External facts will receive `LIVE-EV-###` identifiers and will be distinguished from NewYou requirements and assumptions.

---

# 11. Current convergence status

**NOT CONVERGED.**

Broad documentary discovery must continue. The stream already has a coherent ownership boundary, but `LIVE-GAP-001`, `LIVE-GAP-003`, `LIVE-GAP-004` and `LIVE-GAP-005` are material semantic blockers to a clean FP-007 JIT handoff. `LIVE-GAP-002` is an explicit provider empirical gate. No claim is made that FP-007 is ready for implementation or that `OQ-020`, `OQ-021`, `OQ-036` or any privacy/retention decision is resolved.
