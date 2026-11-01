# NewYou Live & Replay Pre-JIT — Cumulative Working Ledger v0.12.1

- **Status:** WORKING / NON-AUTHORITATIVE CUMULATIVE DEEP SOURCE
- **Implementation:** NOT AUTHORISED
- **Authority:** NONE
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Pass-M acceptance successor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.1.md`
- **Pass-M acceptance commit:** `31783ad23486eec898ff8555fa6198b7cc8e3d5f`
- **Provider-evidence revalidation:** `2026-10-11`
- **Compression rule:** historical discovery/register sources remain immutable provenance under `deep/archive/`; this ledger records the current accepted cumulative state.

## 1. How to use this ledger

This is the canonical deep working source for the accepted Live & Replay Pre-JIT stream after Pass-M acceptance. It is intended for exact cumulative reasoning when the normal-context compact pack is insufficient.

Read order for ordinary future work remains:

```text
current governed NewYou authority
→ ../README.md
→ docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0/NEWYOU_LIVE_REPLAY_PREJIT_CONTRACT_WORKING_v0.1.0.md
→ docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0/NEWYOU_LIVE_REPLAY_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.0.md when an unresolved rule matters
→ docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0/NEWYOU_LIVE_REPLAY_EVIDENCE_INDEX_WORKING_v0.1.0.md when provenance/provider evidence matters
→ this cumulative deep ledger only when exact cumulative reasoning is required
→ archive/ only for exact historical PT narrative or supersession audit
```

This ledger cannot amend current authority and cannot authorise FP-007 Phase 7 or implementation.

## 2. Accepted cumulative state

```text
PASSES A–M
=> ACCEPTED_WORKING_LOCK

LIVE-PT-001...154
=> ACCEPTED WORKING EVIDENCE

LIVE-UPD-001...006
=> CURRENT WORKING UPSTREAM-DELTA SET

LIVE-GAP-001...014
=> CURRENT WORKING GAP SET

LIVE-EV-001...006
=> ACCEPTED WORKING PROVIDER DOCUMENTATION EVIDENCE

LIVE-UPD-007
=> NOT WARRANTED

LIVE-GAP-015
=> NOT WARRANTED

BROAD SEMANTIC DISCOVERY
=> PARKED

OQ-020
=> OPEN

OQ-021
=> OPEN

FP-007
=> NOT SELECTED / NOT PHASE-7 AUTHORISED

IMPLEMENTATION
=> NOT AUTHORISED

PASS N
=> NOT JUSTIFIED BY DEFAULT
```

## 3. Pass / pressure-test acceptance log

| Pass | PT range | Accepted focus |
|---|---|---|
| A | `LIVE-PT-001...012` | initial authority/truth separation; ordinary live→replay path; provider/registration/attendance/access/replay seams |
| B | `LIVE-PT-013...030` | occurrence lifecycle, schedule/versioning, registration/access, attendance identity/correction |
| C | `LIVE-PT-031...039` | recording intent, raw capture, capture multiplicity/failure/finality |
| D | `LIVE-PT-040...047` | recording notice/permission, admission, late join and policy transition |
| E | `LIVE-PT-048...056` | role/capture scope, presenter/guest/staff/practitioner/Q&A and sensitive material |
| F | `LIVE-PT-057...065` | post-capture purpose withdrawal and multi-person consequences |
| G | `LIVE-PT-066...075` | retention, processor deletion, reconciliation, legal hold and non-resurrection |
| H | `LIVE-PT-076...086` | Full Deletion composition |
| I | `LIVE-PT-087...097` | replay correction, successor versions, withdrawal, stale delivery capability |
| J | `LIVE-PT-098...109` | promotional derivatives/clips and separate promotional purpose/rights |
| K | `LIVE-PT-110...125` | participant communications, promise scope and durable delivery |
| L | `LIVE-PT-126...141` | cross-dimensional convergence and broad Pre-JIT closure |
| M | `LIVE-PT-142...154` | bounded Restream/Cloudflare provider documentation evidence and empirical-proof implications |

Every PT remains accepted with its exact historical reasoning available in the corresponding immutable Pass A–M discovery source under `archive/`. The compact Evidence Index provides tranche routing; the Compression Audit accounts for every accepted numbered conclusion.

## 4. Core authority / truth separation

| Durable or derived fact | Owner / boundary |
|---|---|
| NewYou occurrence/session definition, version/schedule context, registration, attendance | Events & Live |
| General current protected right/source/validity/expiry/revocation | Entitlements |
| Canonical participant/staff/practitioner identity and role | Identity & Access |
| Occurrence recording notice/association context | Events & Live |
| Governed media identity, bytes, lineage, derivatives, correction/versioning and publication | Content & Media |
| Purpose-specific recording authority/consent/withdrawal; retention/deletion orchestration | Privacy & Consent |
| Professional/case relationship truth | Professional Care |
| Message intent/delivery/provider evidence | Communications |
| Central append-only evidence where selected | Audit & Evidence |
| Derived measurements/aggregates | Analytics |
| Provider room/input/recording/status, signed URL, CDN state | external evidence/delivery only |

Provider state, delivery reachability, messages, cache/PubSub/search/read models, Audit and Analytics never silently become business authority.

## 5. Cumulative semantic contract

The accepted semantic model is cumulative and intentionally keeps independent dimensions independent.

### 5.1 Occurrence/provider identity

- Stable NewYou occurrence identity is independent of provider room/input/resource identity.
- Provider replacement, recreation or credential rotation does not itself create a new occurrence.
- Duplicate provider resources after ambiguous create/retry do not multiply NewYou business identity.
- Genuine duplicate NewYou occurrences require governed correction/supersession rather than destructive merge.
- Intended schedule/history, actual execution outcome, provider binding, registration, attendance, recording association and replay publication remain separate dimensions.
- Historical schedule meaning remains explainable; participant-local timezone rendering is derived presentation.
- Exact identity-preserving reschedule/supersession semantics remain `LIVE-UPD-001` / `LIVE-GAP-001`.

### 5.2 Registration/access/admission

```text
registration
!= entitlement
!= join capability
!= provider presence
!= attendance
```

- Registration never freezes a current right forever.
- Entitlements owns general current protected access; stale provider links cannot restore expired/revoked authority.
- Valid entitlement does not bypass an occurrence registration requirement where Product declares one.
- Purchaser, beneficiary and participant may differ; sponsored/complimentary grants remain explicit/scoped/auditable.
- Commercial reversal may change current rights without erasing historical delivered truth.
- Ordinary non-scarce registration cancellation is optional scope. If included, Product authority resolves it through `LIVE-GAP-009` before Events JIT implements it.
- Initial admission and continuing/reconnect authority are independent; `LIVE-UPD-004` / `LIVE-GAP-008` preserve the unresolved immediate-disconnect versus governed-continuity question.

### 5.3 Attendance

- Attendance is Events & Live truth after governed evidence/reconciliation, not a provider row.
- Multiple devices/reconnects do not multiply participant attendance.
- Provider duration/presence/email/display identity are evidence, not the business definition or canonical identity.
- Missing provider evidence does not automatically prove no-show.
- Weak/public identity cannot silently become named participant attendance.
- Manual correction, if permitted, is explicit/attributed/auditable and remains Events truth.
- Provider corrections can lawfully change an Events conclusion through governed correction without rewriting evidence history.
- Replay consumption is not live attendance.
- Full Deletion or participant unlinking does not rewrite truthful historical attendance as no-show.
- Exact attendance meaning/assurance/finality remains `LIVE-UPD-002`, `LIVE-GAP-004`, `LIVE-GAP-010`.

### 5.4 Recording/capture

```text
recording intent/current authority
!= provider capture
!= governed media adoption
!= replay publication
```

- Provider recording cannot manufacture recording authority.
- Provider recording object/ID is not governed NewYou media identity.
- One occurrence can create zero/one/many raw/provider capture representations; restart/replacement/segmentation can create additional objects.
- Provider ready/completed does not prove completeness, correct source, rights or publication suitability.
- Partial/corrupt/wrong-source/multiple captures remain explicit evidence conditions.
- Segment composition/adoption is governed Content & Media work.
- Duplicate/reordered/missing provider capture callbacks do not define finality by arrival order.
- Accidental capture without current authority fails closed and routes through Privacy/Content/processor consequences.
- Exact capture→governed-media adoption remains `LIVE-GAP-012` JIT-only.

### 5.5 Recording notice/current authority/roles

- Recording notice and recording permission/current purpose authority are distinct.
- Registration does not permanently freeze recording authority.
- Relevant current authority is re-evaluated at consequential admission/capture boundaries.
- Late joiners receive no automatic exemption.
- Camera-off does not necessarily mean non-capture of name/voice/chat/transcript.
- Unrecorded→recorded policy transition cannot be authorised by provider toggle alone.
- Provider-native notice/checkbox is evidence/enforcement only until mapped into Privacy authority.
- Attendee, presenter/speaker, guest, facilitator, staff and practitioner contexts remain distinct; provider role labels are non-authoritative.
- Role promotion can materially expand capture scope and trigger re-evaluation.
- Staff authority is not blanket media permission.
- Lawful recording does not make every statement publishable; one participant cannot authorise another person's sensitive disclosure.
- Group practitioner presence does not create private Professional Care.
- `LIVE-UPD-005`, `LIVE-GAP-003`, `LIVE-GAP-013` remain open routes; OQ-021 remains primary policy authority.

### 5.6 Post-capture withdrawal

- Purpose withdrawal affects current/future dependent processing, not historical occurrence/attendance/capture truth.
- Historical lawful capture does not create indefinite replay/publication/promotion authority.
- Recording, replay and promotional purposes can differ.
- One participant's withdrawal cannot be ignored in multi-person media, but does not automatically grant that participant control over the entire recording.
- Technical separability/inseparability is evidence, not Product/legal authority.
- Materially inseparable contribution may require fail-closed replay handling pending approved policy.
- Derivatives/transcripts/captions/clips/replacement versions must converge on current purpose authority.
- `LIVE-UPD-006` / `LIVE-GAP-003` preserve unresolved consequences.

### 5.7 Retention/deletion/Full Deletion

```text
current publication/use eligibility
!= physical retention
```

- Retention requires positive scoped authority.
- Deletion obligation, request, transport success, provider acknowledgement/status and verified completion are different facts.
- Processor deletion inventory must include all required representations, including historical/replacement provider resources and derivatives.
- Unknown provider deletion outcome remains unresolved; duplicate/reordered evidence cannot create false terminality.
- Legal hold/independent retention basis never restores publication authority.
- Backup restore may restore bytes but cannot restore later-withdrawn/deleted authority; restore must reconcile suppression before promotion.
- Provider incompatibility with approved deletion/retention requirements can block that release path.
- Privacy orchestrates Full Deletion without taking over source-domain truth.
- Occurrence history can remain true while identifiable participant representation changes.
- Shared multi-person media needs participant-specific consequences without assuming automatic whole-asset deletion or preservation.
- Audit may retain only independently authorised minimum evidence; Analytics participant-level linkage is deleted/suppressed while sufficiently irreversible aggregates may remain where governed.
- Required unresolved processor path prevents verified Full Deletion completion.
- Timely deletion cancellation does not itself resurrect disposed data, registration, entitlement or provider admission.
- `LIVE-GAP-014` preserves processor deletion/non-resurrection proof; exact durations remain expert-gated.

### 5.8 Replay publication/rights/correction

- Provider capture existence does not equal governed replay publication.
- Replay publication does not grant entitlement; live attendance/live entitlement does not automatically create replay entitlement.
- `LIVE-UPD-003` / `LIVE-GAP-005` preserve product-family live/replay rights.
- Protected replay checks current authority before bounded transport capability; stale signed URLs are not authority.
- Current Product correction classes remain distinct: `minor_editorial_correction`, `material_content_correction`, `safety_correction`, `legal_or_consent_correction`, `full_withdrawal`.
- History is never destructively rewritten.
- Material correction creates a governed successor; safety/legal-invalid use can require immediate withdrawal; full withdrawal need not have a replacement.
- Derivatives converge with affected source correction/withdrawal.
- Stale CDN/provider capability cannot become current publication truth.
- Correction-of-correction uses successor lineage.
- Replay correction/versioning and occurrence/schedule correction are independent lineages; replay correction does not rewrite occurrence/attendance truth.

### 5.9 Promotional derivatives

> Promotional clip != shortened replay.

- Promotional use has separate purpose, approval, publication and exact source lineage.
- Replay approval does not automatically approve promotion and vice versa.
- Public promotional derivative can derive from protected governed source without making protected replay public.
- One participant/role label cannot authorise another person's promotional use.
- Promotional-purpose withdrawal can invalidate a clip independently; safety-affected clip withdraws immediately where affected.
- Correction/withdrawal propagation is reason- and lineage-specific.
- Promotional clips are not mandatory FP-007 Roadmap exit scope.

### 5.10 Communications

- Communications owns delivery evidence only; it never owns occurrence/access/replay/privacy truth.
- Future FP-007 Final Contract must enumerate included/promised journeys.
- Protected joining instructions are required, but email is not inherent authority.
- Confirmation/reschedule/cancellation/replay-available/reminder journeys are not universal promises unless Product/Feature Pack scope includes them.
- Promised live journeys invoke OQ-036; reminders invoke OQ-017 only when promised.
- Safety correction notification remains mandatory where current Product law requires it; legal/consent notification remains Privacy/legal dependent where not otherwise governed.
- Must-not-lose messages require durable intent/retry/reconciliation; PubSub/provider acceptance is insufficient.
- Stale queued/sent messages cannot restore stale schedule/access/publication.
- Marketing preference does not suppress correctly governed mandatory safety/product notice.
- Current deletion/privacy/source authority is revalidated before queued external work.

### 5.11 Cross-domain convergence/recovery

- No giant Live/Replay orchestration Domain is required.
- No distributed transaction across all Domains is required merely for correctness.
- Each owner commits its own smallest coherent truth; mandatory consequences follow durable retry-safe execution with current-precondition revalidation.
- Queue uniqueness is not business idempotency; provider/network I/O stays outside authoritative locks.
- Current source authority beats stale provider/message/token/cache/search/PubSub/Analytics/Audit/read-model state.
- Duplicate/reordered callbacks are normal; irreversible external work remains historical evidence and reconciles.
- Occurrence/entitlement/media/privacy/communications lifecycles remain independently versioned.
- Crash/restart safety is correctness for must-not-lose consequences.
- Operator recovery is owner-mediated, guarded, idempotent and auditable; no universal Super Admin shared-write bypass.
- Derived Audit/Analytics/read models may lag but never become current access/publication authority.

## 6. Current upstream-delta register

| ID | Accepted working question/direction | Primary route |
|---|---|---|
| `LIVE-UPD-001` | stable occurrence identity plus schedule/execution/correction/supersession semantics | Product / Events & Live |
| `LIVE-UPD-002` | attendance meaning, assurance, correction and finality | Product / Events & Live |
| `LIVE-UPD-003` | live-right versus replay-right product-family semantics | Product / Entitlements |
| `LIVE-UPD-004` | in-progress continuity/revocation | Product / Entitlements + Events context |
| `LIVE-UPD-005` | recording participation contract at admission/policy transition | OQ-021 / Product-Privacy-Legal-Operations |
| `LIVE-UPD-006` | post-capture purpose-withdrawal consequences | OQ-021 plus applicable retention/deletion routes |

No `LIVE-UPD-007` is warranted.

## 7. Current gap register

| ID | Classification | Primary route |
|---|---|---|
| `LIVE-GAP-001` | `PRODUCT_AUTHORITY_GAP` | occurrence lifecycle/schedule semantics |
| `LIVE-GAP-002` | `PROVIDER_EMPIRICAL_GATE` | OQ-020 |
| `LIVE-GAP-003` | `RECORDING_PRIVACY_GATE` | primary OQ-021; OQ-029...032 compose as applicable |
| `LIVE-GAP-004` | `PRODUCT_AUTHORITY_GAP` | attendance meaning |
| `LIVE-GAP-005` | `PRODUCT_AUTHORITY_GAP` | replay-right policy |
| `LIVE-GAP-006` | `COMMUNICATIONS_GATE` | OQ-036 as promised; OQ-017 if reminders promised |
| `LIVE-GAP-007` | `FUTURE_EVENT_COMMERCE` | FP-015 |
| `LIVE-GAP-008` | `PRODUCT_AUTHORITY_GAP` | in-progress access continuity |
| `LIVE-GAP-009` | `PRODUCT_AUTHORITY_GAP` | registration/cancellation if included |
| `LIVE-GAP-010` | `PRODUCT_AUTHORITY_GAP` | weak/public attendance assurance |
| `LIVE-GAP-011` | `PROVIDER_EMPIRICAL_GATE` | capture/finalisation / OQ-020 |
| `LIVE-GAP-012` | `JIT_ONLY` | capture→governed-media adoption mechanism |
| `LIVE-GAP-013` | `PROVIDER_EMPIRICAL_GATE` | recording-aware provider enforcement / OQ-020 after OQ-021 semantics |
| `LIVE-GAP-014` | `PROVIDER_EMPIRICAL_GATE` | processor deletion/non-resurrection / OQ-030+031 |

No `LIVE-GAP-015` is warranted.

## 8. Independent-review corrections

Two post-closure corrections remain current and supersede older historical wording:

1. **PT-028:** ordinary non-scarce registration cancellation is optional FP-007 scope. If included: `LIVE-GAP-009` / Product authority resolves meaning/guards/re-registration/participant effect → Events JIT implements. JIT does not invent the Product rule.
2. **LIVE-GAP-003:** primary semantic route is OQ-021; it composes as applicable with OQ-029 category retention/disposition, OQ-030 external processor deletion, OQ-031 restore/non-resurrection, OQ-032 deletion/export operations and `LIVE-GAP-014` provider proof. Those inherited gates keep their own existing classifications.

These corrections did not create UPD-007, GAP-015, a new Domain or a new broad discovery pass.

## 9. Accepted Pass-M provider evidence

Pass M is a bounded evidence extension. Provider documentation remains evidence only.

| EV | Provider | Accepted current fact | Evidence limit |
|---|---|---|---|
| `LIVE-EV-001` | Restream | Custom RTMP paid-plan capability; RTMPS; API-dependent custom-channel feature limits | capability evidence only; OQ-020 open |
| `LIVE-EV-002` | Restream | plan-bounded recording retention/duration and permanent manual deletion | lack of documented general disable control is not proof no control exists; OQ-020/OQ-021 proof required |
| `LIVE-EV-003` | Cloudflare | RTMPS/SRT Live Inputs; recording `off|automatic`; timeout segmentation; signed-URL policy; recording-deletion scheduling field | provider mechanism, not Product authority |
| `LIVE-EV-004` | Cloudflare | account-scoped idempotency key ≤255 bytes; six-hour expiry; documented deleted-key 409 behavior | bounded provider idempotency, not NewYou business idempotency |
| `LIVE-EV-005` | Cloudflare | connected can be non-playable; live-input and video-processing evidence planes are distinct | controlled duplicate/reorder/loss/failure proof required |
| `LIVE-EV-006` | Cloudflare | deleting a Live Input retains existing recordings; video deletion separate | not representation-complete governed deletion proof |

Pass-M accepted provider conclusion:

> Until OQ-020/OQ-021 prove the exact selected-account Restream paid-plan recording controls, the preferred Restream route must not be assumed compatible with an occurrence for which recording is not currently authorised.

This does not contradict DEC-190 because DEC-190 is a preferred direction with architecture detail/provider validation pending.

## 10. Explicit non-decisions / deferred work

This cumulative source does not decide:

- exact occurrence enum/state vocabulary or schedule supersession thresholds;
- exact attendance threshold/evidence hierarchy/finality;
- exact product-family live/replay entitlement matrix;
- exact in-progress revoke/grace behavior;
- exact recording consent/refusal/late-join policy or legal sufficiency;
- exact retention periods/categories/exceptions;
- provider certification or production account settings;
- exact capture→media Resource/action/worker/storage model;
- exact operator-recovery commands;
- exact messaging channel/provider/retry timings beyond durable-consequence invariants;
- exact signed token/link format or expiry timing;
- exact Full Deletion schema/job implementation;
- Event Commerce/ticketing/holds/transfers/refunds/credits/reserved seating;
- promotional clips as mandatory FP-007 scope;
- final Phase-7 dossier set, 7C contract or proof classification;
- application implementation.

## 11. Future controlled proof requirements

Existing OQ/provider routes must eventually exercise, as applicable:

- Restream Custom RTMP → Cloudflare normal path and selected account constraints;
- exact no-recording behavior/control;
- Cloudflare recording `off` versus `automatic`;
- connected-but-not-playable startup and malformed media paths;
- ambiguous provider create, same-key retry, restart and post-idempotency-expiry reconciliation;
- disconnect/reconnect segmentation;
- duplicate/reordered/lost live-input and video-processing notifications;
- Restream + Cloudflare multi-representation recording inventory;
- input deletion with surviving recordings; video deletion residual access;
- multi-provider partial deletion and restore/non-resurrection;
- stale signed capability after entitlement/publication loss;
- owner-mediated operator recovery under outage/ambiguity.

No TB/VS/HH identifier is created here. Final proof classification belongs to future Phase 7C.

## 12. Parked closure / future handoff

**Current working closure:** `PASS — PARK BROAD LIVE & REPLAY PRE-JIT DISCOVERY`.

When FP-007 is actually selected, future governed work must re-read then-current authority, derive Phase-7A independently, adjudicate affected Domains, route unresolved Product semantics upstream, resolve applicable gates, complete required JIT dossiers, write 7C only after prerequisites, classify durable consequences explicitly, finalise proof from actual mechanisms and pass the Development Entry Hard Stop before implementation.

Reopen this broad stream only for material authority/scope change, genuine future 7A/JIT contradiction not already routed, provider/legal/privacy resolution or executable proof that falsifies an accepted assumption, materially different product-family semantics, or a security/privacy/legal finding.

Ordinary implementation questions and additional imaginable edge cases do not create Pass N.

## 13. Provenance

Historical discovery/register chronology is preserved byte-identically under `archive/` by reusing original Git blob objects. The current accepted status successor is retained next to this ledger as `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.1.md`.

Detailed provenance/indexing lives in:

- `docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0/NEWYOU_LIVE_REPLAY_EVIDENCE_INDEX_WORKING_v0.1.0.md`;
- `docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0/NEWYOU_LIVE_REPLAY_COMPRESSION_AUDIT_WORKING_v0.1.0.md`;
- `docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0/NEWYOU_LIVE_REPLAY_SOURCE_COMPACT_VERIFICATION_WORKING_v0.1.0.md`.

The Compression Audit mechanically accounts for all accepted numbered conclusion series (179 cumulative numbered conclusions) and maps them to compact destinations. Exact PT scenario narrative remains recoverable from the historical Pass A–M discovery files.

```text
provider documentation != Product authority
provider documentation != controlled empirical proof
provider documentation != OQ-020 closure

FP-007 != selected
FP-007 != Phase-7 authorised
implementation != authorised
```
