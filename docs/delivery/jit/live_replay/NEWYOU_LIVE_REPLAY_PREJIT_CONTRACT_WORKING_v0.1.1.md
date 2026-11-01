# NewYou Live & Replay Pre-JIT Contract — Working Consolidation v0.1.1

- **Status:** FINAL COMPACT WORKING PACK / NON-AUTHORITATIVE / HARDENED
- **Implementation:** NOT AUTHORISED
- **Authority:** NONE
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Accepted coverage:** Passes A–M; `LIVE-PT-001...154`; `LIVE-UPD-001...006`; `LIVE-GAP-001...014`; `LIVE-EV-001...006`
- **Deep semantic source:** `deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.2.md`
- **Provider evidence revalidated:** `2026-10-11`
- **Conflict rule:** live governed NewYou authority always wins.

This patch successor restores semantics that v0.1.0 compressed too weakly: replay-correction failure behaviour, Communications classification/resource guards, reconcile-before-repeat provider creation, exact Restream automatic-recording evidence, and the locked 14-day Full Deletion cancellation boundary. It creates no new Product rule, UPD, GAP, Domain, scope or implementation authority.

## 1. Scope and stop boundary

This is the normal-context semantic contract for future governed FP-007 planning. It covers occurrences, registration/admission/access, attendance, provider execution/recovery, recording notice/authority/capture, governed media/replay, withdrawal/deletion, corrections, optional promotional derivatives, communications, and failure/reconciliation.

It does **not** decide scarce event commerce/FP-015, exact Ash Resources/schemas/jobs/queues/tokens, provider production certification, unresolved legal/privacy rules, Phase-7A/7B/7C artifacts, final proof classification or implementation. Broad discovery remains parked; no default Pass N exists.

Verified authority baseline: `main@086ade7b28c000de1c387acb9760e5eb08bb0413`, routed through current README/manifest to Product/North Star v1.3.0, Platform v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and Operating Model v1.0.1 (plus FES v1.0.1 when relevant). `DEC-190` remains a preferred Restream→RTMPS→Cloudflare direction with architecture/provider validation pending; `OQ-020` and `OQ-021` remain open.

## 2. Authority ownership

| Truth | Owner | Never authority |
|---|---|---|
| occurrence/session, schedule context, registration, attendance | Events & Live | provider room/input/attendee state, message delivery |
| current general protected right | Entitlements | join/playback URL, provider membership |
| canonical participant/staff/practitioner identity/role | Identity & Access | provider email/display/host labels |
| occurrence recording notice/association | Events & Live | provider record toggle |
| media identity/bytes/lineage/correction/publication | Content & Media | provider recording object/status |
| purpose-specific recording authority/withdrawal; retention/deletion orchestration | Privacy & Consent | registration/attendance/provider checkbox by default |
| professional/case relationship | Professional Care | practitioner group-session presence |
| message intent/delivery evidence | Communications | occurrence/access/replay truth |
| append-only evidence | Audit & Evidence | source-domain truth |
| measurements/aggregates | Analytics | attendance/access/publication truth |

Cross-domain mutations go through the owner. Provider, cache/search/PubSub, Audit, Analytics and UI projections remain evidence/delivery/derived state.

## 3. Required semantic separations

```text
occurrence identity
!= schedule/version
!= provider binding/execution evidence
!= registration
!= current entitlement
!= join capability
!= provider presence
!= attendance
!= recording authority
!= provider capture
!= governed media
!= replay publication
!= replay entitlement
!= replay consumption
```

Independent dimensions must not be collapsed into one lifecycle/status.

## 4. Occurrence/provider identity

- NewYou occurrence identity is stable Events truth independent of provider resource identity.
- Provider replacement/recreation/key rotation does not itself create a new occurrence; ambiguous duplicate provider resources never multiply NewYou registration/attendance truth.
- Genuine duplicate NewYou occurrences require governed correction/supersession, not destructive merge.
- Intended schedule/history, actual execution, provider binding, registration, attendance, recording association and replay publication remain separate.
- Historical schedule meaning remains explainable; participant timezone rendering is derived.
- Exact reschedule/supersession boundary remains `LIVE-UPD-001` / `LIVE-GAP-001`.

## 5. Registration, admission and entitlement

```text
registration != entitlement != join capability != provider presence != attendance
```

- Registration never freezes a current right forever; Entitlements owns current protected access/scope/source/expiry/revocation.
- Valid entitlement does not bypass a Product-declared registration requirement; provider invite/link/member state cannot manufacture registration/access.
- Purchaser, beneficiary and participant may differ; sponsored/complimentary grants stay explicit/scoped/reasoned/auditable.
- Commercial reversal may change current rights without erasing historical delivered truth.
- Ordinary non-scarce registration cancellation is optional FP-007 scope. If included, Product authority resolves meaning, guards, re-registration and participant effect through `LIVE-GAP-009` before Events JIT implements it.
- Initial admission and continuing/reconnect authority are separate. `LIVE-UPD-004` / `LIVE-GAP-008` retain the unresolved immediate-disconnect versus governed-continuity question.
- Event-commerce tickets/holds/refunds/transfers remain outside FP-007.

## 6. Attendance

- Attendance is Events truth after governed evidence/reconciliation, not provider presence.
- Multiple devices/reconnects do not multiply attendance; provider duration/email/display identity are evidence only.
- Missing evidence does not automatically prove no-show; weak/public identity cannot silently become named attendance.
- Manual/provider-driven correction, where permitted, is explicit/attributed/auditable and does not erase evidence history.
- Replay consumption is not live attendance. Full Deletion/unlinking does not rewrite truthful historical attendance as no-show.
- Exact attendance meaning/assurance/finality remains `LIVE-UPD-002`, `LIVE-GAP-004`, `LIVE-GAP-010`.

## 7. Recording/capture, notice and roles

```text
recording intent/current authority != provider capture != governed-media adoption != replay publication
```

- Provider capture cannot manufacture recording authority or governed NewYou media identity.
- One occurrence can produce zero/one/many provider representations; partial/corrupt/wrong-source/segmented captures stay explicit evidence conditions.
- Provider ready/completed does not prove completeness, rights, source correctness or publication suitability; callback arrival order does not define finality.
- Exact capture→governed-media adoption remains `LIVE-GAP-012` JIT-only.
- Recording notice and recording permission/current purpose authority are distinct. Registration does not freeze recording authority; current authority is re-evaluated at consequential admission/capture boundaries, including late join and material policy/role changes.
- Camera-off does not imply non-capture of voice/name/chat/transcript. Provider-native notices/checkboxes remain evidence/enforcement unless mapped into Privacy authority.
- Attendee, speaker, guest, facilitator, staff and practitioner contexts remain distinct; provider role labels are non-authoritative. Staff authority is not blanket media permission.
- Lawful recording does not make every statement publishable; one participant cannot authorise another person's sensitive disclosure. Group practitioner presence does not create private Professional Care.
- `LIVE-UPD-005`, `LIVE-GAP-003`, `LIVE-GAP-013` remain open; OQ-021 is primary recording/privacy authority.

## 8. Post-capture withdrawal

- Purpose withdrawal changes current/future dependent processing, not historical occurrence/attendance/capture truth.
- Historical lawful capture does not grant indefinite replay/publication/promotion authority; recording, replay and promotional purposes can differ.
- One participant's withdrawal cannot be ignored in multi-person media but does not automatically control the entire asset; technical separability is evidence, not legal/Product authority.
- Materially inseparable contribution may require fail-closed replay handling pending approved policy.
- Captions/transcripts/clips/derivatives/successors must converge on current purpose authority.
- `LIVE-UPD-006` / `LIVE-GAP-003` retain unresolved consequences.

## 9. Retention, processor deletion and Full Deletion

```text
current publication/use eligibility != physical retention
```

- Retention needs positive scoped authority. Deletion obligation, request, transport success, provider acknowledgement/status and verified completion are distinct facts.
- Deletion inventory includes all required current/historical/replacement provider representations and derivatives. Unknown outcome remains unresolved; duplicate/reordered evidence cannot create false completion.
- Legal hold/independent retention basis never restores publication authority. Restored backups must reapply later withdrawal/deletion/suppression before promotion.
- Provider inability to satisfy approved retention/deletion evidence can block that provider path rather than weaken NewYou authority.
- Privacy orchestrates Full Deletion; source Domains execute owner-specific consequences.
- Locked Full Deletion flow is: **immediate normal-access revocation → 14-day cancellation window → irreversible deletion execution → verified completion**. Completed irreversible deletion has **no recovery or reconstruction path**.
- Timely cancellation does not resurrect already disposed data, registration, entitlement or provider admission; each owner re-evaluates current truth.
- Occurrence history may remain true while participant-identifiable representations change. Shared media needs participant-specific consequences without assuming whole-asset destruction/preservation.
- Audit may retain only independently authorised minimised evidence; participant-level Analytics is deleted/suppressed while sufficiently irreversible aggregates may remain only where governed.
- Required unresolved processor path prevents verified completion.
- OQ-021/OQ-029 govern applicable retention semantics; OQ-030/OQ-031/OQ-032 and `LIVE-GAP-014` govern processor/deletion/non-resurrection proof as applicable.

## 10. Replay publication, rights and correction

- Provider capture existence does not equal replay publication; replay publication does not grant entitlement; live attendance/live entitlement does not automatically create replay entitlement.
- Content & Media owns current published replay/version/withdrawal; Entitlements owns current replay access. Product-family rights remain `LIVE-UPD-003` / `LIVE-GAP-005`.
- Protected replay re-checks current owner authority before bounded delivery capability; stale signed/CDN/provider capability is not authority.
- Product correction classes remain distinct: `minor_editorial_correction`, `material_content_correction`, `safety_correction`, `legal_or_consent_correction`, `full_withdrawal`.
- History is never destructively rewritten. Material correction creates an approved successor; safety-invalid use withdraws immediately; legal/consent correction composes with current Privacy/legal authority; full withdrawal need not have a replacement.
- Derivatives converge with affected correction/withdrawal; correction-of-correction uses successor lineage. Replay-media and occurrence/schedule versions are independent; replay correction never rewrites occurrence/attendance truth.
- **Failure semantics are class-dependent:** an ordinary material V1 may remain current while V2 is prepared only while V1 remains otherwise safe, lawful and eligible. Once safety/legal/consent or another governing authority invalidates V1, failed successor preparation/processing remains fail-closed and cannot resurrect V1.

## 11. Promotional derivatives

Promotional clip ≠ shortened replay. If included, promotion has separate purpose/approval/publication authority and exact source/time-range lineage. Replay approval does not approve promotion and vice versa; one participant/role label cannot authorise another person's promotion. Promotional-purpose withdrawal can independently invalidate a clip, and safety-affected clips withdraw immediately. Promotional clips are not mandatory FP-007 Roadmap exit scope.

## 12. Communications

- Communications owns message intent/delivery/provider evidence, never originating occurrence/access/media/privacy truth.
- Future Final Contract enumerates included/promised journeys. Protected joining instructions are required, but email is not inherently the authority/channel. Confirmation, reschedule/cancellation, replay-available and reminders are not universal promises.
- Promised live journeys invoke OQ-036; reminders invoke OQ-017 only when promised.
- Material-correction notice follows governing affected-set/applicability rules; safety-correction notification is mandatory where Product requires it; legal/consent notice remains Privacy/legal dependent where not otherwise governed.
- Must-not-lose communication uses durable intent/retry/reconciliation; PubSub/provider acceptance is insufficient. Stale messages cannot restore old schedule/access/publication. Current source/privacy/deletion predicates are re-read before provider work.
- Marketing opt-out does not suppress a correctly governed mandatory safety/product notice, while **optional reminder/marketing/convenience roles may not masquerade as mandatory** to bypass preference, quiet-hour or purpose controls.
- **No Live-specific Communications Resource is justified by this discovery.** Reuse existing Communications ownership and logical `MessageIntent`/`DeliveryAttempt` seams unless future governed evidence explicitly changes that conclusion.

## 13. Cross-domain convergence/recovery

- No giant Live/Replay orchestration Domain or distributed transaction is required merely for correctness.
- Each owner commits its smallest coherent truth. Mandatory consequences use durable execution intent/job, retry-safe execution, current-precondition revalidation and visible terminal state.
- Queue uniqueness is not business idempotency; provider/network I/O stays outside authoritative locks/transactions.
- Current source authority beats stale provider/message/token/cache/search/PubSub/Analytics/Audit/read-model state.
- Duplicate/reordered callbacks are normal. Irreversible external work remains historical evidence and reconciles rather than being pretended away.
- Occurrence, entitlement, media, privacy and communications lifecycles remain independent. Crash/restart correctness is mandatory for must-not-lose consequences.
- Operator recovery is owner-mediated, guarded, idempotent and auditable; no universal Super Admin shared-write bypass.

## 14. Accepted provider evidence and limits

Pass M evidence remains provider documentation only.

**Restream:** Custom RTMP requires paid plan; RTMPS is supported; custom channels lose API-dependent Chat/Analytics; current documentation states **paid live streams are automatically recorded/saved**; retention/duration is plan-bounded; manual deletion is permanent. Reviewed docs did not expose a general disable control, but **absence from documentation is not proof no control exists**. A no-recording occurrence therefore fails closed against the preferred Restream path until OQ-020/OQ-021 prove an approved selected-account/configuration behaviour.

**Cloudflare Stream:** Live Inputs support RTMPS/SRT; recording mode is `off|automatic`; `timeoutSeconds` may segment recordings; signed URLs are transport enforcement; Live Input create idempotency is account-scoped/max 255 bytes/six-hour expiry; connected input can still be non-playable; live-input and video-processing evidence are distinct; deleting a Live Input retains recordings and video deletion is separate.

**Provider-create ordering:** provider idempotency does not replace NewYou identity/idempotency. Long-delayed or post-idempotency-expiry ambiguous create recovery **must reconcile provider state and the current NewYou binding before repeating external creation**. Provider-key expiry never authorises blind duplicate create.

```text
provider documentation != Product authority != controlled proof != OQ-020 closure
```

Future controlled proof still covers normal path, no-recording controls, connected≠playable, ambiguous creates/restarts/expiry, segmentation, duplicate/reordered/lost callbacks, multi-provider recording inventory, deletion residuals/non-resurrection, stale capabilities and owner-mediated recovery.

## 15. Critical open routes and future Phase 7

Current unresolved routes remain `LIVE-UPD-001...006` and `LIVE-GAP-001...014`; no UPD-007 or GAP-015 exists. Primary gates include OQ-020, OQ-021, OQ-036 where promised, OQ-017 for promised reminders, OQ-029...032 as applicable, OQ-014 for protected-delivery/correction propagation, and future OQ-022/FP-015 event commerce only.

When FP-007 is actually selected: re-read then-current authority → create real 7A Skeleton/Gate Manifest → classify required/conditional/no dossier → resolve upstream Product/gates → create only required 7B dossiers → STOP on contradiction → create 7C after prerequisites → classify synchronous authority/durable consequences/ephemeral observation → finalise proof classification from actual mechanisms → satisfy Development Entry Hard Stop before implementation.

## 16. Closure / reopen rule

`PASS — PARK BROAD LIVE & REPLAY PRE-JIT DISCOVERY`.

Reopen only for material authority/scope change, genuine future 7A/JIT contradiction not already routed, provider/legal/privacy resolution or executable proof falsifying an accepted assumption, materially different product-family semantics, or security/privacy/legal findings. Ordinary implementation questions and additional imaginable edge cases do not create Pass N.
