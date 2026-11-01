# NewYou Live & Replay Pre-JIT Contract — Working Consolidation v0.1.0

- **Status:** FINAL COMPACT WORKING PACK / NON-AUTHORITATIVE
- **Implementation:** NOT AUTHORISED
- **Authority:** NONE
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Accepted coverage:** Passes A–M; `LIVE-PT-001...154`; `LIVE-UPD-001...006`; `LIVE-GAP-001...014`; `LIVE-EV-001...006`
- **Deep source:** `deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.1.md`
- **Provider evidence revalidated:** `2026-10-11`
- **Conflict rule:** live governed NewYou authority always wins. If this working contract conflicts with current Product, Architecture, Domain, Roadmap, Open Work or future governed Feature Pack/JIT authority, stop at the correct authority level.

## 1. Scope and stop boundary

This is the normal-context semantic contract for future governed Live & Replay planning. It preserves the durable current working model without requiring the full discovery chronology.

It covers:

- early governed live sessions and occurrences;
- registration, access, admission and attendance boundaries;
- provider execution and recovery;
- recording notice, recording authority and raw capture;
- governed-media adoption, replay publication and protected replay access;
- post-capture purpose withdrawal and Full Deletion seams;
- replay correction/versioning/withdrawal;
- promotional derivatives only where included;
- necessary/promised communications;
- cross-domain failure, retry, reconciliation and operator recovery;
- current accepted provider documentation evidence and its limits.

It does **not** authorise or decide:

- scarce event commerce, paid holds, reserved seating, ticket transfer/refund/credit mechanics or FP-015;
- a generic streaming platform or new orchestration Domain;
- exact Ash Resources, schemas, tables, indexes, actions, workers, queues, caches, token formats or provider adapters;
- exact provider production configuration or provider certification;
- exact retention periods, legal sufficiency or unresolved consent policy;
- an FP-007 Phase-7A Skeleton/Gate Manifest, 7B dossier, 7C Final Feature Pack Contract, proof classification or Phase 8;
- application implementation.

Broad semantic discovery is parked. No default Pass N exists.

## 2. Live authority baseline for this consolidation

Verified `main` baseline:

`086ade7b28c000de1c387acb9760e5eb08bb0413`

Current routed authority:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` where frontend experience is material.

This pack does not amend any of them.

Current Roadmap/Decision direction preserves `DEC-190` as a preference for Restream → custom RTMPS → Cloudflare Stream → entitlement-controlled platform player → governed replay records, with architecture detail/provider validation still pending. `OQ-020` and `OQ-021` remain open.

## 3. Core authority doctrine

Every durable business truth has exactly one authoritative owner. Provider resources/status, transport capabilities, sent messages, caches, PubSub, Audit evidence and Analytics projections remain evidence/delivery/derived state and may not silently become business authority.

| Truth | Authoritative owner / boundary | Must not masquerade as authority |
|---|---|---|
| Live/session definition, occurrence, schedule context, registration, attendance | Events & Live | provider room/input, provider attendee row/status, message delivery |
| Current general protected access/entitlement | Entitlements | join URL, playback URL, provider membership |
| Canonical participant/staff/practitioner identity and role | Identity & Access | provider email/display name/host/panelist label |
| Occurrence recording notice/association context | Events & Live | provider record toggle |
| Governed media identity, bytes, lineage, derivatives, correction/versioning, publication/withdrawal | Content & Media | provider recording object/status |
| Purpose-specific recording authority/consent/withdrawal and retention/deletion orchestration | Privacy & Consent | registration/attendance/provider checkbox by default |
| Professional/case relationship truth | Professional Care | practitioner presence in a group session |
| Message intent/delivery attempt/provider evidence | Communications | occurrence/access/replay truth |
| Governed append-only evidence | Audit & Evidence | source-domain truth |
| Derived measurements/aggregates | Analytics | attendance/entitlement/publication truth |

Cross-domain mutation goes through the owner. Operator recovery invokes owner commands; it does not create shared-write access.

## 4. Required semantic separations

These facts remain independently governed:

```text
occurrence identity
!= schedule/version truth
!= provider binding/execution evidence
!= registration
!= current entitlement/access
!= issued join capability
!= provider presence
!= authoritative attendance
!= recording intent/authority
!= provider capture
!= governed media adoption
!= replay publication
!= replay entitlement
!= replay consumption
```

A single lifecycle/status enum must not collapse them.

## 5. Occurrence and provider identity contract

- NewYou occurrence identity is stable business identity owned by Events & Live and is independent of provider room/input/resource identifiers.
- Provider room/input replacement, recreation, stream-key rotation or credential rotation does not by itself create a new occurrence.
- Duplicate provider resources after timeout/ambiguous retry cannot multiply NewYou occurrence, registration or attendance identity.
- A true duplicate NewYou occurrence is a business correction/supersession problem, not provider deduplication; history must not be destructively merged away.
- Intended schedule/history, actual execution outcome, provider binding, registration, attendance, recording association and replay publication remain separate dimensions.
- A reschedule must preserve historical schedule meaning and explicit continuity/supersession semantics; exact Product boundary remains `LIVE-UPD-001` / `LIVE-GAP-001`.
- Participant-local timezone display is derived presentation; it does not create per-viewer schedule authority.
- Provider connected/disconnected/completed state is evidence only; Events decides any authoritative occurrence transition under approved semantics.
- Provider replacement can leave stale links/messages/captures; current owner truth beats them.

No exact occurrence enum/schema is selected here.

## 6. Registration, admission and entitlement contract

```text
registration
!= entitlement
!= admission/join capability
!= live presence
!= attendance
```

- Registration is Events & Live truth describing an occurrence-specific relationship/intent; it does not freeze a revocable current access right.
- Entitlements owns general current protected access, validity, scope, expiry, source/provenance and revocation.
- Where event-specific ticket/admission truth exists later, it remains Events authority rather than becoming general Entitlements truth.
- A participant who validly registered can later fail current access checks without rewriting registration history.
- Valid entitlement does not bypass a Product-declared registration requirement.
- Provider invite/link/member state cannot manufacture registration or access.
- Purchaser, beneficiary and participant may differ; sponsored/complimentary grants remain explicit, scoped, reasoned and auditable.
- Commercial reversal can change current rights but does not erase historical registration/attendance/delivery truth.
- Ordinary non-scarce registration cancellation is not automatically required by FP-007. If included, `LIVE-GAP-009` requires Product authority to define meaning, guards, re-registration and participant-facing effects before Events JIT implements it.
- Scarce capacity/ticket cancellation/refund mechanics stay outside FP-007.

## 7. In-progress live access contract

Initial admission authority and ongoing/reconnect authority during an active session are distinct questions.

- Current owner authority is re-read at consequential access points; provider persistence does not decide continued authority.
- Revocation/expiry cannot be ignored merely because the participant is already connected.
- The exact immediate-disconnect versus narrowly governed continuity/grace rule is unresolved Product semantics under `LIVE-UPD-004` / `LIVE-GAP-008`.
- Reconnect after authority changes must not use stale provider capability as authority.
- Full Deletion's immediate normal-access revocation is a stronger governed path and does not silently answer every ordinary in-progress revocation case.

Do not invent the final revoke/grace rule in JIT.

## 8. Attendance contract

Attendance is Events & Live business truth derived from governed evidence/reconciliation, not a provider attendee row.

- Registration does not equal attendance.
- Multiple devices, reconnects or provider connection rows must not multiply one participant's attendance.
- Provider duration/presence is evidence, not the Product threshold.
- Missing provider evidence does not automatically prove `no_show`; unresolved/pending evidence must not be fabricated into a final conclusion.
- Weak/public/anonymous provider identity cannot silently become named participant attendance.
- Provider email/display identity is non-canonical evidence; safe platform correlation is required.
- Manual attendance correction, if Product permits it, must be explicit, attributed, scoped and auditable; Audit does not own the corrected fact.
- Provider corrections can change a governed Events attendance conclusion through explicit correction/reconciliation without destroying historical evidence.
- Replay viewing never becomes live attendance.
- Historical attendance remains true after later entitlement loss, replay withdrawal, commercial reversal, privacy disposition or deletion of participant-identifiable representation; it must not be rewritten as `no_show` merely because identity is later removed.

The actual attendance business meaning/assurance/correction/finality remains `LIVE-UPD-002`, `LIVE-GAP-004` and `LIVE-GAP-010`.

## 9. Recording/capture contract

```text
recording intent/current recording authority
!= provider capture
!= governed media adoption
!= replay publication
```

- Provider recording cannot manufacture NewYou recording authority.
- A provider recording object/ID is not NewYou governed media identity.
- One occurrence can have zero, one or many provider/raw captures; Restream/Cloudflare and reconnect segmentation can create multiple independent representations.
- Provider restart/replacement or Cloudflare disconnect segmentation can create additional capture objects without changing occurrence identity.
- `ready`, `complete` or similar provider states do not prove completeness, correct source, rights, suitability or publication eligibility.
- Late, partial, corrupt, wrong-screen/wrong-source, missing-audio and duplicated captures remain distinct evidence conditions.
- Composing multiple raw segments is governed Content & Media editing/adoption, not automatic provider finalisation.
- Duplicate/reordered/missing provider capture callbacks cannot define NewYou finality by arrival order.
- If current recording authority is absent/false, accidental provider capture is fail-closed and routes through Privacy/Content/processor consequences; it cannot be adopted merely because bytes exist.

Exact raw-capture adoption mechanism remains `LIVE-GAP-012` JIT-only after required semantics/gates.

## 10. Recording notice, consent and admission

Recording notice and recording permission/current purpose authority are distinct.

- Registration or entitlement does not permanently freeze recording authority.
- Current applicable recording authority must be satisfied at consequential admission/capture boundaries.
- Late joiners receive no automatic exemption from notice/authority requirements.
- A participant's refusal/decline consequence remains Product/privacy policy under `LIVE-UPD-005` / `LIVE-GAP-003`; JIT cannot invent it.
- Camera-off does not necessarily mean non-capture: name, voice, chat, transcript or other data may still be captured.
- A transition from unrecorded to recorded during a session is participant-facing and cannot be authorised merely by a provider toggle.
- Provider-native banner/checkbox/notice is evidence/enforcement only unless Privacy authority explicitly accepts and reconciles it.
- Recording-aware provider enforcement remains empirical under `LIVE-GAP-013` / `OQ-020`.

`OQ-021` remains open and is the primary recording/privacy semantic gate.

## 11. Role and capture-scope contract

Keep attendee, presenter/speaker, guest, facilitator, staff and practitioner contexts distinct.

- Provider role labels remain evidence; they do not become canonical NewYou identity/role authority.
- Promoting an attendee to speaker/presenter can materially expand voice/video/name/transcript capture and may require current-policy re-evaluation.
- Staff operational authority is not blanket media permission.
- Q&A may capture text, voice, name, transcript and/or video; the exact capture scope must be governed.
- Lawful recording/capture does not make every statement publishable.
- One participant cannot authorise another person's private or sensitive disclosure.
- Sensitive audience content may require editing/withdrawal before replay even if original capture was lawful.
- Group practitioner presence/Q&A does not create private Professional Care or private-case truth.

## 12. Post-capture purpose withdrawal

Purpose withdrawal is distinct from historical truth and from Full Deletion.

- Withdrawal ends dependent future/current processing authority for the withdrawn purpose according to governing Privacy law.
- Historical attendance and lawful historical capture facts are not rewritten.
- Lawful historical capture does not grant indefinite replay/publication/promotion authority.
- Recording, replay and promotional purposes may differ; withdrawal is purpose-specific.
- Replay/current publication must re-evaluate current authority after withdrawal.
- One participant's withdrawal from multi-person media cannot be ignored; equally, one participant does not automatically control the entire multi-person recording.
- Technical separability/inseparability is evidence, not Product/legal authority.
- Where a participant contribution is materially inseparable and current policy cannot lawfully support continued use, replay/derivative use must fail closed pending approved disposition.
- Derivatives, transcripts, captions, clips and replacement versions must converge on current purpose authority; they do not automatically inherit permission forever.

`LIVE-UPD-006` preserves the unresolved consequential Product/privacy package.

## 13. Retention and processor deletion contract

```text
current publication/use eligibility
!= physical media retention
```

- Continued retention requires positive, scoped authority; provider defaults, cheap storage, historical lawful capture or operational convenience do not create it.
- Deletion obligation, request creation, transport success, provider acknowledgement/status and verified governed completion are separate facts.
- Processor deletion must account for all required representations in scope: source/raw captures, segments, derivatives, transcripts/captions/thumbnails/clips, replacement/historical provider resources and applicable cache/CDN copies.
- Unknown external deletion outcome remains unresolved; reconcile rather than fabricate success/failure.
- Duplicate/reordered deletion callbacks/status cannot terminalise deletion by arrival order.
- A legal hold or independently approved retention basis pauses only destruction within its scope; it never restores replay/publication authority.
- Backup/restore can restore bytes but may not restore authority. Later withdrawal/deletion/suppression must be replayed/reconciled before restored service is promoted.
- Historical provider bindings remain relevant to deletion inventory; current provider association alone is insufficient.
- A processor that cannot satisfy approved retention/deletion/evidence requirements can block release of that provider path; it is not a reason to weaken NewYou authority.

Exact durations/actions/exceptions remain OQ-021/OQ-029; processor proof remains OQ-030/OQ-031 and `LIVE-GAP-014`.

## 14. Full Deletion seam

Privacy & Consent orchestrates Full Deletion but does not take over source-Domain ownership.

- Full Deletion immediately removes ordinary access according to governing rules; stale provider/token/cache state cannot preserve access.
- Events, Content & Media, Entitlements, Audit and Analytics execute owner-specific consequences.
- Occurrence history can remain true while participant-identifiable representations are deleted/anonymised/suppressed as governed.
- Exact identifiable registration/attendance disposition is category/policy dependent and must not be invented here.
- Historical attendance must not be rewritten as no-show merely because participant linkage is removed.
- Shared multi-person media requires participant-specific consequences without assuming either automatic whole-asset destruction or automatic preservation.
- Audit may retain only independently authorised, minimised, non-reconstructive evidence; source references may become non-resolvable.
- Participant-level Analytics is removed/suppressed; sufficiently irreversible aggregates may remain only where governing privacy/analytics rules permit.
- A required unresolved external processor path prevents verified Full Deletion completion.
- Cancellation during the deletion window does not itself restore Events registration, entitlement, provider admission or previously disposed data. Each owner re-evaluates current truth; irreversibly deleted representations are not resurrected.

No retention duration is selected here.

## 15. Replay publication and entitlement contract

Provider capture existence does not equal replay publication, and replay publication does not equal replay entitlement.

- Content & Media owns governed replay publication/current version/withdrawal.
- Entitlements owns current replay access scope/validity/source/expiry/revocation.
- Live attendance or live entitlement does not automatically create replay entitlement.
- Missing live attendance does not automatically remove replay entitlement.
- Product-family replay-right semantics remain `LIVE-UPD-003` / `LIVE-GAP-005`.
- Protected replay checks current owner authority before issuing bounded delivery capability.
- A stale signed/provider URL is not entitlement and may not restore withdrawn/revoked access.
- Provider signed URLs are transport enforcement, not business authority.

## 16. Replay correction/versioning contract

Use the current Product correction classes as governed:

- `minor_editorial_correction`;
- `material_content_correction`;
- `safety_correction`;
- `legal_or_consent_correction`;
- `full_withdrawal`.

Preserve these invariants:

- history is not destructively rewritten;
- minor editorial correction may update current presentation only within current Product law while preserving explainable history;
- material correction creates a governed approved successor and affected-participant notification where required;
- safety-invalidated use is withdrawn immediately; replacement/remediation may follow separately;
- legal/consent correction composes with current Privacy/legal authority and can require immediate withdrawal;
- full withdrawal need not have a replacement;
- historical publication/view evidence remains explainable after correction/withdrawal;
- exact media versions and derivative lineage remain explicit;
- captions/transcripts/thumbnail/other derivatives must converge with corrected source where affected;
- stale delivery capability/CDN reachability does not make superseded/withdrawn media current;
- correction-of-correction creates successor lineage rather than mutating prior immutable versions;
- replay-media correction and occurrence/schedule correction have independent version lineages;
- replay correction never rewrites occurrence/attendance truth.

Exact correction-impact/remediation detail remains a Content & Media/JIT concern under current authority.

## 17. Promotional derivative contract

> Promotional clip != shortened replay.

Promotional clips are Product-authorised but **not required by the current FP-007 Roadmap exit condition**. If included:

- promotion has separate purpose/approval/publication authority;
- protected replay approval does not automatically approve public promotional use;
- public promotional approval does not automatically approve replay use;
- source media identity/version and exact time-range/segment lineage remain explicit;
- public clip may derive from protected governed source; replay publication itself need not be a prerequisite if source lineage/rights are otherwise governed;
- one participant/speaker cannot authorise another person's promotional use;
- provider/staff role labels do not create promotional rights;
- promotional-purpose withdrawal can invalidate a clip independently of replay purpose;
- safety-affected clips withdraw immediately where the source segment is unsafe;
- legal/consent/correction propagation is reason- and lineage-specific rather than blanket unrelated takedown;
- stale public/social destinations and uncertain external takedown are operational evidence/reconciliation problems, not current NewYou publication authority.

Do not pull promotional clipping into mandatory FP-007 scope merely because the mechanism exists.

## 18. Communications contract

Communications owns durable message intent and delivery evidence, never the originating occurrence/access/media/privacy truth.

- The eventual FP-007 Final Contract must enumerate the included/promised communication journeys; good UX alone does not create Product obligations.
- Protected joining instructions are required by current live-access law, but email as a channel is not authority and is not inherently the only delivery mechanism.
- Registration confirmation, reschedule/cancellation notice, replay-available notice and other ordinary messages are not universal obligations unless current Product/Feature Pack scope promises them.
- Reminders remain conditional; if promised, OQ-017 applies in addition to communications policy.
- Promised/required live notification paths invoke OQ-036 as applicable.
- Material correction notification follows current Product correction applicability/affected-set rules.
- Safety correction notification is mandatory where current Product Law requires it; it must not be silently suppressed by marketing preference.
- Legal/consent/privacy notification duties remain OQ-021/Privacy/legal dependent where not otherwise governed.
- Must-not-lose messages use durable message intent/retry/reconciliation; PubSub or provider acceptance alone is insufficient.
- Provider delivery status is delivery evidence only.
- Stale queued/sent messages cannot restore old schedule, access, join capability or publication authority.
- Marketing opt-out does not suppress correctly governed mandatory safety/product communications.
- Current privacy/deletion/source authority must be revalidated before queued external provider work executes.

## 19. Cross-domain convergence and recovery

No giant Live/Replay orchestration Domain or one distributed transaction is required.

- Each Domain commits the smallest coherent durable transition of its own truth.
- Mandatory cross-domain consequences follow the approved durable-consequence pattern: source commit → durable execution intent/job → retry-safe execution → current precondition re-read → success/retry/terminal-visible state.
- Queue uniqueness is not business idempotency.
- Provider/network I/O does not occur inside authoritative business locks/transactions.
- Current source authority beats stale provider/message/token/cache/search/PubSub/Analytics/Audit/read-model state.
- Duplicate/reordered callbacks and consequences are normal; correlation and idempotency must survive them.
- Irreversible external work is preserved as historical evidence and reconciled rather than pretended away.
- Occurrence, entitlement, media, privacy and communications version/lifecycle dimensions remain independent.
- Crash/restart correctness is mandatory for must-not-lose consequences.
- Operator recovery remains owner-mediated, guard-aware, idempotent and auditable; no universal Super Admin shared-write bypass exists.
- Audit/Analytics/read models may lag but can never become current access/publication authority.

## 20. Accepted provider evidence contract

Pass M is accepted working provider evidence only. Provider documentation remains subordinate to NewYou authority and still requires controlled proof.

### 20.1 Restream

Current first-party documentation revalidated 2026-10-11 supports:

- Custom RTMP requires a paid Restream plan;
- RTMPS is supported for Custom RTMP destinations;
- API-dependent Restream Chat/Analytics do not work for custom channels;
- current paid recording retention is plan-bounded: 15 days Standard/Professional, 30 days Business;
- current documented maximum recording duration is 6 hours Standard and 10 hours Professional/Business;
- manual recording deletion is permanent.

Accepted evidence limit:

- reviewed documentation did not expose a general “disable automatic recording” control;
- absence from documentation is **not proof that such a control does not exist**;
- therefore a no-recording occurrence must fail closed against the preferred Restream path until OQ-020/OQ-021 prove an approved selected-account/configuration behavior.

### 20.2 Cloudflare Stream

Current first-party documentation revalidated 2026-10-11 supports:

- Live Inputs ingest RTMPS/SRT;
- recording mode supports `off` and `automatic`;
- automatic mode creates Stream video/recording state for replay;
- `timeoutSeconds` can cause reconnect/disconnect segmentation into additional Video IDs;
- `requireSignedURLs` is provider transport enforcement for live/recorded video;
- create Live Input supports account-scoped `Idempotency-Key`, max 255 bytes, six-hour expiry; reuse of a deleted input's key before expiry yields 409;
- provider `connected` status does not prove participant playback is available;
- live-input connected/disconnected/errored evidence is distinct from video-processing ready/error evidence;
- deleting a Live Input retains existing recordings;
- recording/video deletion therefore requires separate representation inventory/action.

Provider idempotency, signed URLs and webhooks do not replace NewYou authority/idempotency/reconciliation.

```text
PROVIDER DOCUMENTATION
!= PRODUCT AUTHORITY
!= CONTROLLED-LIVE PROOF
!= OQ-020 CLOSURE
```

## 21. Provider/failure proof obligations retained

Future OQ-020/OQ-030 controlled proof should exercise at least:

- paid Restream Custom RTMP → Cloudflare RTMPS normal flow;
- exact Restream recording behavior and any approved no-recording configuration;
- Cloudflare `off` versus `automatic` recording;
- connected-but-not-playable startup and malformed audio/keyframe cases;
- timeout/unknown create + same idempotency key;
- restart after provider accepted create but before local persistence;
- retry after provider idempotency expiry;
- disconnect/reconnect segmentation and multiple Video IDs;
- duplicate/reordered/lost live-input notifications;
- duplicate/reordered/lost video-processing notifications;
- simultaneous Restream + Cloudflare recording inventory and divergent completeness;
- Live Input deletion while recordings remain;
- video/recording deletion and residual accessibility;
- multi-provider partial deletion and non-resurrection;
- stale signed capability after entitlement/publication loss;
- provider outage and owner-mediated operator recovery.

Documentation alone does not satisfy these proof obligations.

## 22. Critical open routes

The compact Delta/Gap Register is authoritative only as working evidence; current higher authority still decides each resolution.

Key unresolved routes:

- `LIVE-UPD-001` / `LIVE-GAP-001` — occurrence lifecycle/schedule identity/supersession;
- `LIVE-UPD-002` / `LIVE-GAP-004` / `LIVE-GAP-010` — attendance meaning/assurance/correction;
- `LIVE-UPD-003` / `LIVE-GAP-005` — live versus replay rights;
- `LIVE-UPD-004` / `LIVE-GAP-008` — in-progress revocation/continuity;
- `LIVE-UPD-005` / `LIVE-GAP-003` — recording participation/admission/policy transition;
- `LIVE-UPD-006` / `LIVE-GAP-003` — post-capture purpose withdrawal;
- `LIVE-GAP-002`, `011`, `013` — OQ-020 provider empirical path/capture/enforcement;
- `LIVE-GAP-003` — primary OQ-021 recording/privacy gate, composing with OQ-029...032 as applicable;
- `LIVE-GAP-006` — promised communications: OQ-036, plus OQ-017 if reminders are promised;
- `LIVE-GAP-007` — future FP-015 event commerce;
- `LIVE-GAP-012` — exact capture→governed-media adoption JIT seam;
- `LIVE-GAP-014` — processor deletion/non-resurrection empirical proof.

No `LIVE-UPD-007` and no `LIVE-GAP-015` exist.

## 23. Future Phase-7 / JIT boundary

Pre-JIT closure does not select FP-007 and does not create Phase-7 authority.

When programme sequencing actually selects FP-007:

1. re-read then-current live authority;
2. create the real Phase-7A Skeleton + preliminary Gate Manifest;
3. treat this pack as derived evidence only;
4. explicitly classify affected Domains as required / conditional / no dossier;
5. route exact unresolved Product semantics upstream before any JIT/7C contract depends on them;
6. resolve applicable blocking expert/provider gates;
7. create only required Phase-7B JIT dossiers;
8. stop at the correct upstream authority on contradiction;
9. create Phase-7C Final Feature Pack Contract only after prerequisites;
10. classify synchronous authority, mandatory durable consequences and ephemeral observation explicitly;
11. make final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` classification from exact mechanism/proof coverage;
12. satisfy Development Entry Hard Stop before Phase 8/application implementation.

The current Roadmap `PROBABLY_NEW_TRACER_BULLET` signal is provisional, not the final proof decision.

## 24. Closure / reopen rule

**Working closure:** `PASS — PARK BROAD LIVE & REPLAY PRE-JIT DISCOVERY`.

Reopen broad discovery only for:

- material Product/Architecture/Domain/Roadmap change affecting FP-007;
- material Feature Pack scope change;
- a genuine 7A/JIT contradiction not already routed;
- OQ/provider/legal/privacy resolution that falsifies an accepted assumption;
- executable controlled proof/implementation evidence that falsifies a convergence invariant;
- materially different live/replay semantics required by a newly selected product family;
- a security/privacy/legal finding requiring upstream reconsideration.

Ordinary requests for more edge cases or implementation representation questions do not justify Pass N.

```text
BROAD SEMANTIC DISCOVERY = PARKED
PASS M PROVIDER EVIDENCE = ACCEPTED WORKING EVIDENCE ONLY
OQ-020 = OPEN
OQ-021 = OPEN
FP-007 = NOT SELECTED / NOT PHASE-7 AUTHORISED
IMPLEMENTATION = NOT AUTHORISED
PASS N = NOT JUSTIFIED BY DEFAULT
```
