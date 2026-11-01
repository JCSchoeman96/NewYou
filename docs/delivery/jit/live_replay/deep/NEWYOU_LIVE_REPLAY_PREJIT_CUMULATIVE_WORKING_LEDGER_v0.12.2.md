# NewYou Live & Replay Pre-JIT — Cumulative Working Ledger v0.12.2

- **Status:** WORKING / NON-AUTHORITATIVE CUMULATIVE DEEP SOURCE / HARDENED SUCCESSOR
- **Implementation:** NOT AUTHORISED
- **Authority:** NONE
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Authority baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Accepted Pass-M status successor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.1.md`
- **Provider evidence revalidated:** `2026-10-11`
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.1.md`

This successor restores semantic detail weakened by the first compression. It does not reopen discovery, amend authority, create UPD/GAP/Domain identifiers or authorise implementation.

## 1. Accepted state and use

```text
Passes A–M                  ACCEPTED_WORKING_LOCK
LIVE-PT-001...154           ACCEPTED WORKING EVIDENCE
LIVE-UPD-001...006          CURRENT WORKING DELTA SET
LIVE-GAP-001...014          CURRENT GAP SET
LIVE-EV-001...006           ACCEPTED PROVIDER DOCUMENTATION EVIDENCE
LIVE-UPD-007                NOT WARRANTED
LIVE-GAP-015                NOT WARRANTED
Broad semantic discovery    PARKED
OQ-020                       OPEN
OQ-021                       OPEN
FP-007                        NOT SELECTED / NOT PHASE-7 AUTHORISED
Implementation                NOT AUTHORISED
Pass N                        NOT JUSTIFIED BY DEFAULT
```

Normal route: current governed authority → compact Contract v0.1.1 → Delta/Gap v0.1.1 as needed → Evidence Index v0.1.1 as needed → this ledger for cumulative semantics → `archive/` only for exact historical PT narrative.

Accepted pass ranges remain A `001...012`, B `013...030`, C `031...039`, D `040...047`, E `048...056`, F `057...065`, G `066...075`, H `076...086`, I `087...097`, J `098...109`, K `110...125`, L `126...141`, M `142...154`.

## 2. Ownership and separations

| Fact | Owner |
|---|---|
| occurrence/session, schedule context, registration, attendance | Events & Live |
| general current protected entitlement | Entitlements |
| canonical identity/role | Identity & Access |
| occurrence recording notice/association | Events & Live |
| media identity/bytes/lineage/correction/publication | Content & Media |
| recording authority/withdrawal; retention/deletion orchestration | Privacy & Consent |
| professional/case relationship | Professional Care |
| message intent/delivery evidence | Communications |
| selected evidence | Audit & Evidence |
| measurements/aggregates | Analytics |
| provider room/input/recording/status/URL/CDN state | evidence/delivery only |

Provider state, messages, cache/search/PubSub/read models, Audit and Analytics never become business authority.

```text
occurrence != schedule != provider binding != registration != entitlement
!= join capability != provider presence != attendance
!= recording authority != provider capture != governed media
!= replay publication != replay entitlement != replay consumption
```

## 3. Cumulative semantic contract

### Occurrence/provider identity

Occurrence identity is stable Events truth independent of provider resources. Provider replacement/recreation/key rotation does not create a new occurrence; ambiguous duplicate provider resources do not multiply registration/attendance. Genuine duplicate occurrences require governed correction/supersession, not destructive merge. Schedule/history, actual execution, provider binding, registration, attendance, recording association and replay publication remain separate. Exact reschedule/supersession meaning remains `LIVE-UPD-001` / `LIVE-GAP-001`.

### Registration/access/admission

Registration never freezes a current right; Entitlements owns current access/scope/source/expiry/revocation. Provider invites/links cannot manufacture access. Valid entitlement does not bypass Product-declared registration. Purchaser/beneficiary/participant may differ; sponsored/complimentary grants remain explicit/scoped/auditable. Commercial reversal may change current rights without erasing history. Ordinary non-scarce cancellation is optional FP-007 scope; if included, `LIVE-GAP-009` requires Product authority before Events JIT. Initial admission and continuing/reconnect authority are separate; `LIVE-UPD-004` / `LIVE-GAP-008` retain the unresolved ordinary continuity rule.

### Attendance

Attendance is Events truth after governed evidence/reconciliation, not provider presence. Reconnects/devices do not multiply attendance; provider duration/email/display identity are evidence only. Missing evidence does not automatically mean no-show; weak/public identity cannot silently become named attendance. Corrections are explicit/attributed/auditable and preserve evidence history. Replay consumption is not live attendance; Full Deletion/unlinking does not rewrite truthful attendance as no-show. Exact meaning/assurance/finality remains `LIVE-UPD-002`, `LIVE-GAP-004`, `LIVE-GAP-010`.

### Recording/capture/notice/roles

Provider capture cannot manufacture recording authority or governed media. One occurrence may create zero/one/many raw/provider representations; partial/corrupt/wrong-source/segmented captures remain explicit evidence. Provider ready/completed does not prove completeness/rights/publication suitability; callback order does not define finality. Capture→governed-media adoption remains `LIVE-GAP-012` JIT-only.

Recording notice != recording permission/current purpose authority. Registration does not freeze recording authority; current authority is re-read at consequential admission/capture boundaries, including late join, role promotion and policy transitions. Camera-off does not necessarily mean non-capture. Provider notices/checkboxes/role labels remain evidence/enforcement only unless mapped into NewYou authority. Staff authority is not blanket media permission. One participant cannot authorise another person's sensitive disclosure. Group practitioner presence does not create private Professional Care. `LIVE-UPD-005`, `LIVE-GAP-003`, `LIVE-GAP-013` remain open; OQ-021 is primary.

### Purpose withdrawal

Withdrawal changes current/future dependent processing, not historical occurrence/attendance/capture truth. Historical lawful capture does not grant indefinite replay/promotion authority; recording, replay and promotion may have different purposes. One person's withdrawal cannot be ignored in shared media but does not automatically control the whole asset. Technical separability is evidence, not Product/legal authority; inseparable contribution may require fail-closed handling. Derivatives/successors converge on current purpose authority. `LIVE-UPD-006` / `LIVE-GAP-003` retain unresolved consequences.

### Retention/deletion/Full Deletion

Current publication/use eligibility != physical retention. Deletion obligation/request/transport/provider acknowledgement/status/verified completion are separate. Inventory includes current/historical/replacement provider representations and derivatives. Unknown outcome remains unresolved; callback order cannot create false completion. Legal hold/independent retention never restores publication. Restored backups reapply later suppression/deletion before promotion. Provider incompatibility with approved deletion/retention can block that provider path.

Privacy orchestrates Full Deletion while source Domains execute owner consequences. Locked flow:

```text
immediate normal-access revocation
→ 14-day Full Deletion cancellation window
→ irreversible deletion execution
→ verified completion
```

After irreversible completion there is no recovery/reconstruction path. Timely cancellation does not resurrect already disposed data, registration, entitlement or provider admission. Occurrence history may remain true while identifiable participant representation changes. Shared media needs participant-specific consequences without assuming whole-asset destruction/preservation. Audit retains only independently authorised minimum evidence; participant-level Analytics is deleted/suppressed while irreversible aggregates may remain only where governed. Required unresolved processor path prevents verified completion. OQ-021/OQ-029 and OQ-030/031/032 plus `LIVE-GAP-014` compose according to existing classifications.

### Replay rights/correction/versioning

Provider capture != replay publication; replay publication != entitlement; live attendance/live entitlement does not automatically grant replay rights. Content & Media owns publication/version/withdrawal; Entitlements owns replay access. `LIVE-UPD-003` / `LIVE-GAP-005` retain product-family rights. Protected playback re-checks current authority; stale signed/provider/CDN capability is not authority.

Correction classes remain `minor_editorial_correction`, `material_content_correction`, `safety_correction`, `legal_or_consent_correction`, `full_withdrawal`. History is never destructively rewritten. Material correction creates approved successor; safety-invalid use withdraws immediately; legal/consent correction composes with current Privacy/legal authority; full withdrawal need not have replacement. Derivatives converge; correction-of-correction uses successor lineage; replay-media and occurrence/schedule versions remain independent.

**Class-dependent failure invariant:** ordinary material V1 may remain current while V2 is prepared only while V1 remains otherwise safe, lawful and currently eligible. Once safety/legal/consent or another governing authority invalidates V1, successor failure remains fail-closed and cannot resurrect V1.

### Promotional derivatives

Promotional clip != shortened replay. Promotion has separate purpose/approval/publication and exact source lineage; replay approval does not approve promotion and vice versa. One participant/role cannot authorise another person's promotion. Promotional withdrawal may invalidate a clip independently; safety-affected clips withdraw immediately. Clips are not mandatory FP-007 exit scope.

### Communications

Communications owns message intent/delivery/provider evidence, never source occurrence/access/media/privacy truth. Final Contract enumerates promised journeys. Protected joining instructions are required, but email is not inherently authority. Confirmation/reschedule/cancellation/replay-available/reminders are not universal promises. Promised live journeys invoke OQ-036; reminders invoke OQ-017 only when promised. Safety-correction notice is mandatory where Product requires it; legal/consent notice remains Privacy/legal dependent.

Must-not-lose communications require durable intent/retry/reconciliation; PubSub/provider acceptance is insufficient. Stale messages cannot restore old truth; current source/privacy/deletion predicates are revalidated before provider work. Marketing opt-out does not suppress correctly governed mandatory safety/product notice, while optional reminder/marketing/convenience roles may not masquerade as mandatory to bypass controls. **No Live-specific Communications Resource is justified**; reuse existing Communications ownership and logical `MessageIntent`/`DeliveryAttempt` seams unless future governed evidence explicitly changes that conclusion.

### Cross-domain convergence/recovery

No giant Live/Replay orchestration Domain or distributed transaction is required merely for correctness. Each owner commits its smallest coherent truth; mandatory consequences use durable intent/job, retry-safe execution, current-precondition re-read and visible terminal state. Queue uniqueness is not business idempotency; provider/network I/O stays outside authoritative locks. Current owner truth beats stale provider/message/token/cache/search/PubSub/Analytics/Audit/read models. Duplicate/reordered callbacks are normal. Irreversible external work remains historical evidence and reconciles. Lifecycles remain independent. Crash/restart correctness is required. Operator recovery is owner-mediated/guarded/idempotent/auditable; no universal Super Admin shared-write bypass.

### Provider create ambiguity

Provider idempotency is bounded external mechanism, not NewYou business identity/idempotency. Timeout/crash/lost response can leave create ambiguous. Same-key retry may help within provider window, but durable NewYou correlation/reconciliation still applies. **Long-delayed or post-idempotency-expiry ambiguous create recovery must reconcile provider state and current NewYou binding before repeating external creation. Provider-key expiry never authorises blind duplicate create.**

## 4. UPDs and gaps

Current UPDs: `LIVE-UPD-001` occurrence lifecycle; `002` attendance; `003` live vs replay rights; `004` in-progress continuity; `005` recording participation/admission; `006` post-capture withdrawal. No UPD-007.

Current gaps:

- `001 PRODUCT_AUTHORITY_GAP` occurrence lifecycle/schedule;
- `002 PROVIDER_EMPIRICAL_GATE` OQ-020 provider path;
- `003 RECORDING_PRIVACY_GATE` primary OQ-021; OQ-029...032 compose as applicable;
- `004 PRODUCT_AUTHORITY_GAP` attendance meaning;
- `005 PRODUCT_AUTHORITY_GAP` replay-right policy;
- `006 COMMUNICATIONS_GATE` OQ-036 as promised; OQ-017 for promised reminders;
- `007 FUTURE_EVENT_COMMERCE` FP-015;
- `008 PRODUCT_AUTHORITY_GAP` in-progress access;
- `009 PRODUCT_AUTHORITY_GAP` registration/cancellation if included;
- `010 PRODUCT_AUTHORITY_GAP` weak/public attendance;
- `011 PROVIDER_EMPIRICAL_GATE` capture/finalisation/OQ-020;
- `012 JIT_ONLY` capture→governed-media adoption;
- `013 PROVIDER_EMPIRICAL_GATE` recording-aware provider enforcement after OQ-021 semantics;
- `014 PROVIDER_EMPIRICAL_GATE` processor deletion/non-resurrection/OQ-030+031.

No GAP-015.

PT-028 remains corrected: cancellation optional → if included Product/GAP-009 decides → Events JIT implements. GAP-003 remains corrected: OQ-021 primary; OQ-029 retention, OQ-030 processor deletion, OQ-031 restore/non-resurrection, OQ-032 deletion/export operations and GAP-014 proof compose only as applicable.

## 5. Pass-M evidence

| EV | Accepted fact | Limit |
|---|---|---|
| `001` | Restream Custom RTMP requires paid; RTMPS supported; custom-channel API limits | capability evidence only |
| `002` | **Restream currently documents paid live streams as automatically recorded/saved**; retention/duration plan-bounded; manual deletion permanent | no documented general disable control is **not proof none exists**; OQ-020/OQ-021 confirmation + controlled proof required |
| `003` | Cloudflare RTMPS/SRT; `off|automatic` recording; timeout segmentation; signed-URL/deletion mechanisms | provider mechanism only |
| `004` | Cloudflare create idempotency account-scoped, ≤255 bytes, six-hour expiry, deleted-key 409 | bounded provider idempotency only |
| `005` | connected input can be non-playable; live-input and video-processing evidence separate | controlled timing/reorder/loss proof required |
| `006` | deleting Live Input retains recordings; video deletion separate | not representation-complete deletion proof |

Until OQ-020/OQ-021 prove selected Restream recording controls, the preferred path must not be assumed compatible with an occurrence where recording is not currently authorised. This does not contradict DEC-190 because it remains preferred direction with validation pending.

## 6. Non-decisions, proof and closure

Not decided: exact occurrence enum/schedule thresholds; attendance threshold/finality; product-family rights matrix; ordinary revoke/grace; exact consent/refusal/late-join legal rule; category retention periods/exceptions; provider certification/settings; exact Resources/actions/jobs/storage; operator commands; channel/provider retry timings; token format/TTL; exact Full Deletion implementation; Event Commerce; clips as mandatory FP-007 scope; final dossier set/7C/proof classification; implementation.

Controlled proof eventually covers normal Restream→Cloudflare path, no-recording control, Cloudflare off/automatic, connected≠playable, ambiguous create/same-key retry/restart/**reconcile-before-repeat after expiry**, segmentation, duplicate/reordered/lost callbacks, multi-provider recording inventory, deletion residuals/non-resurrection, stale capabilities, owner recovery, correction-successor failure classes and mandatory-communications revalidation.

The hardening successor restores six compression losses: class-dependent replay failure; Communications mandatory-class guard; no Live-specific Communications Resource; reconcile-before-repeat provider create; exact EV-002 automatic-recording fact; and locked 14-day Full Deletion/no-recovery boundary. These are preservation corrections, not new discovery.

Current closure remains `PASS — PARK BROAD LIVE & REPLAY PRE-JIT DISCOVERY`. Reopen only for material authority/scope change, genuine future 7A/JIT contradiction, provider/legal/privacy resolution or proof falsifying an assumption, materially different product-family semantics, or security/privacy/legal findings. Ordinary edge cases do not create Pass N.

Historical discovery/register chronology remains byte-preserved under `archive/`. The exact local 83,103-byte cumulative v0.12.0 review copy (SHA-256 `e12f757253dea14738cc87d9254ffb9f2e1d001c925897a16fc55dbadce2ce3d`) is a local review source only, not a repository archive artifact.

```text
provider documentation != Product authority != controlled proof != OQ-020 closure
FP-007 != selected
FP-007 != Phase-7 authorised
implementation != authorised
```
