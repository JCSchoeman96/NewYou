# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.13.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PASS M PROPOSED / AWAITING USER ACCEPTANCE
- **Document version:** v0.13.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.12.0.md`
- **Corrected accepted-register baseline:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.11.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch before this artifact:** `prejit/live-replay@12db157f43da7c3743a4c0a7fc7dcbb415ac248c`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap amendment:** NONE
- **Pass class:** BOUNDED PROVIDER EMPIRICAL PRESSURE TEST / OQ-020 + OQ-030 EVIDENCE CAPTURE
- **Broad semantic discovery state:** REMAINS PARKED

---

# 1. Why Pass M is legitimate without reopening broad discovery

The accepted v0.11.0 closure remains valid: ordinary requests for more edge cases do not justify a new general semantic pass.

Pass M is narrower. It records and pressure-tests **current first-party provider evidence** that became materially relevant during independent review, especially facts about:

- Restream Custom RTMP / RTMPS delivery;
- Restream automatic paid-plan recording and retention;
- Cloudflare Stream live-input connection versus participant playability;
- Cloudflare automatic recording and segmentation;
- provider create idempotency limits;
- live-input notifications versus video-processing notifications;
- deletion of live inputs versus deletion of recorded videos.

This is therefore a bounded provider-evidence pass under existing `OQ-020`, `OQ-021`, `OQ-030`, `LIVE-GAP-002`, `LIVE-GAP-003`, `LIVE-GAP-011`, `LIVE-GAP-012`, `LIVE-GAP-013` and `LIVE-GAP-014` routes.

It does **not** reopen occurrence, entitlement, attendance, privacy, correction, communications or deletion semantics already accepted in Passes A-L.

---

# 2. Hard boundaries

Pass M does **not**:

- resolve `OQ-020` from documentation alone;
- resolve `OQ-021` legal/privacy policy;
- select a Restream subscription tier;
- certify Restream or Cloudflare for production;
- assert undocumented provider behaviour;
- infer that lack of a documented control proves the control does not exist;
- choose Ash Resources, schemas, actions, queues or workers;
- create Phase-7A, 7B or 7C artifacts;
- assign TB/VS/HH identifiers;
- authorise implementation;
- modify Product, Architecture, Domain or Roadmap authority;
- create a new live/replay Domain or orchestration owner;
- expand FP-007 into Event Commerce or promotional-clip delivery.

Current provider documentation is evidence, not NewYou business authority.

---

# 3. Authority frame retained from accepted A-L

The following accepted invariants remain controlling:

1. NewYou occurrence truth is owned by Events & Live.
2. Provider room/input state is delivery evidence, not occurrence authority.
3. Registration, entitlement, admission, presence and attendance remain separate facts.
4. Recording intent/current recording authority is not created by provider capture.
5. Provider artifact existence is not governed media identity.
6. Governed media identity is not replay publication.
7. Replay publication is not replay entitlement.
8. Provider reachability, connection, callback or URL possession does not create current access.
9. Current owner authority defeats stale provider, message, token, cache and projection state.
10. External irreversible operations reconcile; they are not rewritten as if they never happened.
11. Processor deletion requires representation-complete accounting for the governed scope.
12. Unknown provider outcome remains unresolved until reconciled.
13. Broad Live & Replay semantic discovery remains parked unless a genuine reopen criterion occurs.

---

# 4. Current authority facts relevant to this pass

## 4.1 DEC-190 remains preference, not provider proof

Current `DEC-190 — Platform live-video path` is:

`LOCKED / ARCHITECTURE DETAIL PENDING`

and says:

> Prefer Restream → custom RTMPS → Cloudflare Stream → entitlement-controlled platform player with governed automatic replay records.

The word `Prefer` does not override `OQ-020` or `OQ-021`. The path remains subject to empirical and privacy/legal validation.

## 4.2 Roadmap provider/privacy gates remain open

Pass M does not change the existing FP-007 gate model:

- `OQ-020` remains the provider-path/failure-behaviour blocker;
- `OQ-021` remains the recording/attendee/replay/withdrawal blocker;
- external processor deletion/non-resurrection remains inherited through OQ-030/OQ-031/OQ-032 where applicable;
- `LIVE-GAP-014` remains the recording-media processor empirical proof seam.

---

# 5. Provider evidence register

These are the first `LIVE-EV-*` entries because Pass M performs explicit first-party provider research.

Each evidence item records only what the cited source currently states. It does not promote vendor behaviour into Product Law.

## LIVE-EV-001 — Restream Custom RTMP requires paid plan and accepts RTMPS

**Provider:** Restream

**Source:** Restream Help Center — `Stream to a Custom RTMP channel`

**URL:** https://support.restream.io/en/articles/369436-stream-to-a-custom-rtmp-channel

**Retrieved:** 2026-10-10

**Verified factual claim:**

- Custom RTMP channels require a paid Restream plan.
- Restream permits an RTMPS URL in place of RTMP for a Custom RTMP channel.
- Restream says API-dependent features such as Restream Chat and Analytics do not work for custom channels.

**Evidence limit:**

This does not prove end-to-end Restream → Cloudflare reliability, latency, retry semantics, attendance evidence quality or production suitability.

---

## LIVE-EV-002 — Restream paid streams are automatically recorded and retained for a plan-bounded period

**Provider:** Restream

**Sources:**

- Restream Help Center — `Download your recordings`
- Restream Help Center — `Where is my recording?`

**URLs:**

- https://support.restream.io/en/articles/4379939-download-your-recordings
- https://support.restream.io/en/articles/10599465-where-is-my-recording

**Retrieved:** 2026-10-10

**Verified factual claim:**

- Restream states that it automatically records and saves live streams on paid plans.
- Standard recordings are retained for 15 days; Professional recordings are retained for 15 days; Business recordings are retained for 30 days.
- Current documented maximum recording length is 6 hours on Standard and 10 hours on Professional/Business.
- Restream states manual recording deletion is permanent and cannot be undone.

**Evidence limit:**

The reviewed official documentation did not expose a general disable-automatic-recording control for paid live streams. **Absence from reviewed documentation is not proof that disabling is impossible.** OQ-020 must obtain explicit provider confirmation and controlled observation before any no-recording occurrence is allowed to use the Restream path.

---

## LIVE-EV-003 — Cloudflare live input supports RTMPS/SRT and recording mode is separately configured

**Provider:** Cloudflare Stream

**Sources:**

- Cloudflare Stream — `Start a live stream`
- Cloudflare Stream API — Live Input create/update documentation

**URLs:**

- https://developers.cloudflare.com/stream/stream-live/start-stream-live/
- https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/create/
- https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/update/

**Retrieved:** 2026-10-10

**Verified factual claim:**

- Cloudflare Live Inputs accept RTMPS or SRT ingest.
- `recording.mode` may be `off` or `automatic`.
- `automatic` makes the live stream available for viewing and records it for later replay.
- `timeoutSeconds` controls how long a disconnected automatic-mode feed may remain associated before a new video is created.
- `requireSignedURLs` may be applied at the live-input level and is also applied to videos recorded from that input.
- `deleteRecordingAfterDays`, where used, schedules deletion of recordings rather than deletion of the live input itself.

**Evidence limit:**

These are Cloudflare mechanisms. They do not decide NewYou recording authority, replay publication, entitlement or retention policy.

---

## LIVE-EV-004 — Cloudflare Live Input create supports bounded provider idempotency

**Provider:** Cloudflare Stream

**Source:** Cloudflare API — `Create a live input`

**URL:** https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/create/

**Retrieved:** 2026-10-10

**Verified factual claim:**

- Create Live Input accepts an optional `Idempotency-Key`.
- Cloudflare documents the key as account-scoped, maximum 255 bytes, expiring six hours after the input is created.
- Reusing a key for a deleted input before expiry returns HTTP 409 Conflict.

**Evidence limit:**

Provider idempotency is bounded by provider semantics and lifetime. It cannot replace NewYou durable identity, business idempotency or reconciliation after an ambiguous outcome.

---

## LIVE-EV-005 — Cloudflare connection state and video readiness are separate evidence planes

**Provider:** Cloudflare Stream

**Sources:**

- Cloudflare Stream — `Troubleshooting a live stream`
- Cloudflare Stream — `Receive Live Webhooks`
- Cloudflare Stream — `Use webhooks`

**URLs:**

- https://developers.cloudflare.com/stream/stream-live/troubleshooting/
- https://developers.cloudflare.com/stream/stream-live/webhooks/
- https://developers.cloudflare.com/stream/manage-video-library/using-webhooks/

**Retrieved:** 2026-10-10

**Verified factual claim:**

- Cloudflare documents a state where an encoder/input is connected and the dashboard shows `Connected`, while the player still reports that the stream has not started.
- Live-input notifications distinguish `live_input.connected`, `live_input.disconnected` and `live_input.errored`.
- Video processing webhooks are a separate mechanism that report when a video finishes processing and is ready, or enters an error state.
- For video playback, `readyToStream=true` and processing status remain distinct from live-input connection.

**Evidence limit:**

Documentation proves the distinction exists but not the exact timing/reordering/duplication characteristics NewYou will observe in production. Those remain controlled-test obligations under OQ-020.

---

## LIVE-EV-006 — Cloudflare deleting a Live Input does not delete existing recordings

**Provider:** Cloudflare Stream

**Sources:**

- Cloudflare API — `Delete a live input`
- Cloudflare API — `Delete video`

**URLs:**

- https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/delete/
- https://developers.cloudflare.com/api/resources/stream/methods/delete/

**Retrieved:** 2026-10-10

**Verified factual claim:**

- Deleting a Live Input permanently disables that input and blocks current/future broadcasts to it.
- Cloudflare explicitly states that existing recordings are retained when the Live Input is deleted.
- Deleting a video is a separate operation; Cloudflare documents that it deletes the video and its copies from Cloudflare Stream.

**Evidence limit:**

The API statement does not by itself prove NewYou representation-complete deletion across Restream, Cloudflare downloads/captions/derivatives, NewYou storage, backups, caches or other processors. `LIVE-GAP-014` therefore remains open.

---

# 6. Pass M pressure tests

## LIVE-PT-142 — Recording is not authorised but the preferred Restream Custom RTMP path is used

**Scenario class**

Recording authority / provider default / privacy fail-closed.

**Why it matters**

The current preferred path uses Restream Custom RTMP, which requires a paid plan, while current Restream documentation says paid streams are automatically recorded. A provider-side recording can therefore exist even if NewYou does not intend to create a replay.

**Authority**

Product recording notice/consent law; `DEC-190`; `OQ-020`; `OQ-021`; accepted Pass D/F recording-authority doctrine.

**Owning Domains**

Events & Live for occurrence recording intent/association; Privacy & Consent for current recording authority; Content & Media only after governed adoption; provider state remains evidence.

**Preconditions**

Occurrence is otherwise eligible to run live. NewYou recording/replay authority is absent or intentionally disabled for the occurrence.

**Timeline**

Occurrence configured as no-recording → Restream paid Custom RTMP path selected → live stream begins → Restream provider may automatically create a recording → Cloudflare may be configured with recording mode off → provider-side Restream bytes still exist.

**Expected invariants**

- `Cloudflare recording.mode=off` does not prove no provider recording exists elsewhere;
- provider default capture cannot manufacture NewYou recording authority;
- a no-recording occurrence must fail closed against any provider path that necessarily or unavoidably records;
- provider recording existence does not create governed media/replay authority;
- retained provider bytes still enter processor/privacy inventory where applicable.

**Questions**

Can Restream automatic recording be disabled for the exact paid Custom RTMP path? Is there an account/stream-level contractual or support-controlled option? What evidence proves the setting before live execution? If not, is the Restream path incompatible with occurrences for which recording is not currently authorised?

**Adversarial variants**

Cloudflare recording disabled; Restream still records. Recording consent withdrawn minutes before start. Operator believes `recording=false` means the full chain does not retain bytes.

**Analysis**

Current documentation creates a material compatibility risk, not a completed provider verdict. Because the reviewed Restream docs do not expose a disable control, the safe working rule is to block the Restream path for no-recording occurrences until OQ-020/OQ-021 prove an approved non-recording configuration or Product/privacy authority explicitly permits the provider capture.

**Semantic disposition**

`BLOCKED_PENDING_PROVIDER_AND_PRIVACY_PROOF / FAIL_CLOSED`

**Proof route**

`OQ-020 + OQ-021 → PROVIDER_CONFIRMATION + CONTROLLED_LIVE_PROOF`

**UPD if any**

None. Reuse `LIVE-GAP-002`, `LIVE-GAP-003`, `LIVE-GAP-011` and `LIVE-GAP-013` as applicable.

**Evidence needed**

First-party contractual/support confirmation plus controlled account test showing exact Restream recording behaviour and whether it can be disabled before any no-recording occurrence uses this path.

---

## LIVE-PT-143 — Cloudflare reports Live Input connected but participant playback is not available

**Scenario class**

Provider connection / participant delivery divergence.

**Why it matters**

Current Cloudflare documentation explicitly says the encoder may be connected while the player still says the stream has not started.

**Authority**

Events occurrence truth; provider state evidence only; FP-007 operational visibility; OQ-020.

**Owning Domains**

Events & Live for occurrence execution truth; provider evidence integration only for delivery observations; Audit/Analytics derived where selected.

**Preconditions**

Cloudflare Live Input exists and Restream/encoder is transmitting.

**Timeline**

Provider input reports connected → participant playback unavailable or malformed → live input may later become playable or error.

**Expected invariants**

- provider connected != occurrence successfully delivered;
- provider connected != participant joined;
- provider connected != authoritative attendance;
- provider connected != replay-ready media;
- operator state must be able to represent delivery degradation without rewriting occurrence truth.

**Questions**

What bounded grace/health rule should future JIT use before surfacing degraded delivery? Which exact Cloudflare observations are sufficiently reliable for operator diagnosis?

**Adversarial variants**

Missing AAC audio; invalid keyframe interval; transient 30-second warm-up; input flaps connected/disconnected.

**Analysis**

No new Product semantic is required. The provider evidence confirms the existing separation between provider connection and participant delivery.

**Semantic disposition**

`PASS / PROVIDER_CONNECTED_NOT_DELIVERY_TRUTH`

**Proof route**

`OQ-020 → JIT OBSERVABILITY CONTRACT → CONTROLLED_LIVE_PROOF`

**UPD if any**

None.

**Evidence needed**

Controlled test of normal startup, malformed audio/keyframe input and transient connection/playability divergence.

---

## LIVE-PT-144 — Live Input create times out and NewYou retries within Cloudflare's idempotency window

**Scenario class**

Ambiguous external create / bounded provider idempotency.

**Why it matters**

A timeout may hide a successful provider create. Cloudflare supplies an idempotency key, but its semantics and lifetime are provider-bounded.

**Authority**

Architecture ambiguous irreversible outcome/reconciliation law; Events occurrence identity; OQ-020.

**Owning Domains**

Events & Live integration state only; provider resource remains operational evidence.

**Preconditions**

One NewYou occurrence, create request issued with durable local correlation and provider idempotency key.

**Timeline**

Create sent → response lost/timeout → NewYou retries same logical operation within six hours using same key → provider returns same/create-safe result or conflict according to documented semantics → NewYou reconciles one current provider association.

**Expected invariants**

- provider idempotency key is acceleration, not business identity;
- one NewYou occurrence does not become multiple occurrences;
- no second logical provider-create intent is invented merely because transport outcome is unknown;
- local correlation and reconciliation survive process restart.

**Questions**

What exact response does Cloudflare return for repeated successful same-key create? How does the SDK expose it? Which lookup/reconciliation API is sufficient after ambiguous transport?

**Adversarial variants**

Node crashes after provider accepts create; retry from another worker; input deleted then same key retried before six-hour expiry.

**Analysis**

Cloudflare idempotency materially helps, but cannot replace NewYou durable intent/idempotency because the key expires and deleted-input reuse can return 409.

**Semantic disposition**

`PASS_WITH_REFINEMENT / PROVIDER_IDEMPOTENCY_IS_BOUNDED`

**Proof route**

`OQ-020 → JIT DURABLE-CORRELATION CONTRACT → FAILURE-INJECTION PROOF`

**UPD if any**

None.

**Evidence needed**

Controlled timeout/retry/restart tests and exact API-response observation.

---

## LIVE-PT-145 — Ambiguous create is retried after the provider idempotency key has expired

**Scenario class**

Delayed retry / provider idempotency expiry / duplicate resource risk.

**Why it matters**

Cloudflare documents a six-hour idempotency-key expiry. Long outages or delayed repair can outlive it.

**Authority**

Architecture reconciliation-before-repeat for ambiguous irreversible outcomes; provider state non-authoritative.

**Owning Domains**

Events & Live integration/reconciliation only.

**Preconditions**

Earlier create outcome remains ambiguous and more than six hours have elapsed.

**Timeline**

Create attempted → outcome unknown → idempotency key expires → recovery worker/operator resumes → system must reconcile existing provider resources before a new create.

**Expected invariants**

- expiry of provider idempotency does not authorise blind duplicate create;
- NewYou occurrence identity remains stable;
- duplicate provider resources, if discovered, are reconciled/superseded rather than treated as duplicate business occurrences;
- manual recovery follows same owner-mediated rules as automation.

**Questions**

Which Cloudflare list/metadata/correlation mechanism can safely identify candidate resources after local transport ambiguity?

**Adversarial variants**

Provider create succeeded but local persistence failed; two operators both attempt repair; stale resource was deleted independently.

**Analysis**

Existing occurrence/provider-replacement doctrine composes. The provider idempotency window strengthens the need for NewYou-owned reconciliation rather than eliminating it.

**Semantic disposition**

`PASS / RECONCILE_BEFORE_NEW_CREATE`

**Proof route**

`OQ-020 → JIT RECONCILIATION CONTRACT → FAILURE-INJECTION PROOF`

**UPD if any**

None.

**Evidence needed**

Controlled post-expiry recovery case.

---

## LIVE-PT-146 — One NewYou occurrence creates both a Restream recording and a Cloudflare recording

**Scenario class**

Multiple provider representations / recording inventory.

**Why it matters**

The preferred path can produce at least two distinct external recording representations: Restream's paid-plan recording plus a Cloudflare recording when its mode is automatic.

**Authority**

Accepted zero/one/many raw-capture model; Content & Media adoption boundary; OQ-021/OQ-030; `LIVE-GAP-011`, `LIVE-GAP-012`, `LIVE-GAP-014`.

**Owning Domains**

Providers own their artifacts; NewYou records provider evidence; Content & Media owns governed adoption/publication; Privacy owns purpose authority/orchestration.

**Preconditions**

Paid Restream path; Cloudflare automatic recording enabled; recording authority valid.

**Timeline**

Occurrence runs → Restream saves recording A → Cloudflare creates recording/video B → A and B may become ready at different times and may differ in completeness → NewYou deliberately adopts zero/one/more governed source artifacts according to later JIT policy.

**Expected invariants**

- one occurrence != one provider recording;
- neither A nor B automatically becomes governed media;
- provider readiness order does not choose authoritative source;
- deletion/withdrawal inventory includes every in-scope provider representation;
- replay publication references exact governed media version, not “whichever provider is ready first.”

**Questions**

Which representation, if any, should be preferred for adoption? How are quality/completeness compared? Must one provider copy be deleted after successful governed adoption?

**Adversarial variants**

Restream complete/Cloudflare partial; Cloudflare complete/Restream truncated; only one provider recording exists; both expire/delete on different schedules.

**Analysis**

The independent review's double-representation concern is verified and is already covered by existing semantic seams. It requires provider/C&M JIT proof, not a new Product decision.

**Semantic disposition**

`PASS_WITH_REFINEMENT / MULTIPLE_PROVIDER_COPIES_EXPECTED`

**Proof route**

`OQ-020 + OQ-021/OQ-030 → CONTENT_MEDIA_JIT → PROVIDER/DELETION_PROOF`

**UPD if any**

None.

**Evidence needed**

Controlled dual-recording session with exact object inventory, timestamps, durations, quality/completeness and deletion behaviour.

---

## LIVE-PT-147 — Cloudflare disconnect exceeds timeout and creates another Video ID

**Scenario class**

Live disconnect / recording segmentation / one-input-many-videos.

**Why it matters**

Cloudflare documents `timeoutSeconds` as the boundary after which a disconnected automatic-mode feed results in a new video being created.

**Authority**

Occurrence identity independent of provider object identity; accepted capture multiplicity model.

**Owning Domains**

Events & Live occurrence association; Content & Media only after governed media adoption.

**Preconditions**

One Cloudflare Live Input in automatic mode; live feed disconnects long enough to exceed configured/provider timeout and later reconnects.

**Timeline**

Video A live → disconnect exceeds timeout → A transitions toward on-demand → feed reconnects to same Live Input → provider creates Video B → both provider videos belong to one NewYou occurrence unless owner truth says otherwise.

**Expected invariants**

- one Live Input != one recording;
- one occurrence can have multiple provider recording segments;
- reconnect does not create a new NewYou occurrence merely because provider creates a new video ID;
- attendance and occurrence execution remain independently reconciled;
- governed replay adoption must preserve exact multi-segment lineage if segments are combined/edited.

**Questions**

What exact timeout value is operationally safe? When is a disconnect a continuation versus materially separate occurrence according to Product truth?

**Adversarial variants**

Repeated flapping creates many videos; reconnect after host believed session ended; backup source reconnects to same input.

**Analysis**

Provider evidence confirms why stable platform occurrence identity and zero/one/many capture semantics were necessary.

**Semantic disposition**

`PASS / ONE_INPUT_MAY_CREATE_MANY_RECORDINGS`

**Proof route**

`OQ-020 → EVENTS/C&M JIT CORRELATION → CONTROLLED_DISCONNECT_PROOF`

**UPD if any**

None beyond existing `LIVE-UPD-001` where occurrence-continuity Product boundaries remain unresolved.

**Evidence needed**

Controlled timeout/reconnect matrix.

---

## LIVE-PT-148 — Live-input callbacks and video-processing callbacks arrive in different orders

**Scenario class**

Callback reordering / separate provider evidence planes.

**Why it matters**

Cloudflare exposes live-input connected/disconnected/error notifications separately from video-processing ready/error webhooks.

**Authority**

Architecture provider callback evidence, duplicate/reorder tolerance and reconcile-after-commit doctrine.

**Owning Domains**

Provider integration evidence; Events and Content & Media independently consume only the evidence relevant to their own authority.

**Preconditions**

Automatic recording enabled and webhooks configured.

**Timeline**

Possible order examples:

- connected → disconnected → video ready;
- connected → video processing error → disconnected;
- disconnected callback delayed until after video ready observation;
- duplicate live or video callbacks.

**Expected invariants**

- callback arrival order cannot manufacture occurrence terminality;
- `disconnected` cannot equal replay ready;
- video ready cannot equal occurrence completed;
- duplicate/reordered callbacks converge idempotently;
- Events and C&M remain separate owners.

**Questions**

What exact correlation fields are present across live-input and resulting-video APIs/webhooks? Which polling/reconciliation paths are needed when callbacks are lost?

**Adversarial variants**

Webhook endpoint unavailable; duplicate webhook; callbacks delayed across restart; video ready appears before local disconnect evidence.

**Analysis**

This strongly validates the accepted architecture split. Controlled evidence is still required for exact correlation and recovery mechanics.

**Semantic disposition**

`PASS / SEPARATE_EVIDENCE_PLANES`

**Proof route**

`OQ-020 → JIT CALLBACK CORRELATION → DUPLICATE/REORDER/LOSS PROOF`

**UPD if any**

None.

**Evidence needed**

Captured signed webhook samples plus deliberate duplicate/reorder/loss scenarios.

---

## LIVE-PT-149 — Cloudflare Live Input is deleted but its recordings remain

**Scenario class**

Provider resource retirement / deletion incompleteness.

**Why it matters**

Cloudflare explicitly documents that deleting a Live Input retains existing recordings.

**Authority**

OQ-030/OQ-031; accepted representation-complete deletion; `LIVE-GAP-014`.

**Owning Domains**

Privacy orchestrates deletion where applicable; Content & Media owns governed media consequences; provider evidence remains external.

**Preconditions**

Live Input and one or more recorded videos exist; a privacy/retention/operator action deletes or retires the input.

**Timeline**

Delete Live Input → input cannot be reused → recorded videos remain → separate video deletion/disposition actions are still required where policy demands them.

**Expected invariants**

- input deletion != recording deletion;
- current provider binding deletion cannot be reported as recording-media deletion completion;
- historical/replacement inputs and videos remain inventory subjects where applicable;
- replay withdrawal/publication state remains independent of physical deletion progress.

**Questions**

How does NewYou enumerate all videos created by historical inputs? What evidence proves each required video delete completed? What additional downloads/captions/derivatives need separate handling?

**Adversarial variants**

Input deleted before recordings are indexed locally; replacement input exists; video delete succeeds for one recording but not another.

**Analysis**

This is direct empirical support for `LIVE-GAP-014`; it does not resolve that gap.

**Semantic disposition**

`PASS / INPUT_DELETION_NOT_RECORDING_COMPLETION`

**Proof route**

`OQ-030/OQ-031 + LIVE-GAP-014 → PROVIDER_DELETION_RECONCILIATION_PROOF`

**UPD if any**

None.

**Evidence needed**

Controlled input deletion followed by enumeration/residual-access/video-deletion checks.

---

## LIVE-PT-150 — Restream recording expires before NewYou has completed governed media adoption

**Scenario class**

Provider retention expiry / adoption durability.

**Why it matters**

Restream recordings are retained for a plan-bounded 15/30-day window. Provider retention therefore cannot be NewYou's durable media-retention contract.

**Authority**

Content & Media governed media ownership; OQ-021/OQ-029; provider state non-authoritative.

**Owning Domains**

Content & Media for governed media adoption; provider artifact remains external evidence.

**Preconditions**

Recording authority valid; Restream copy exists; governed adoption is delayed or fails.

**Timeline**

Restream records → adoption worker/process fails or remains pending → provider retention window expires → Restream artifact becomes unavailable.

**Expected invariants**

- provider expiry does not rewrite occurrence/attendance truth;
- provider expiry does not create a replay withdrawal event if no governed replay was ever published;
- a replay promise cannot depend on undocumented/provider-default retention luck;
- if a provider artifact is required for governed adoption, the Final Contract/JIT must define a bounded durable acquisition path and failure visibility.

**Questions**

Is Cloudflare, Restream or another platform intended as the acquisition source of record? What adoption deadline is safe relative to provider retention and maximum session duration?

**Adversarial variants**

Adoption fails for 14 days; account downgraded; long session exceeds Restream recording duration; only Cloudflare copy is complete.

**Analysis**

Provider retention is an external operational constraint, not business retention authority. Exact acquisition strategy belongs to C&M/provider JIT after gates resolve.

**Semantic disposition**

`PASS_WITH_REFINEMENT / PROVIDER_RETENTION_NOT_DURABLE_AUTHORITY`

**Proof route**

`OQ-020/OQ-021/OQ-029 → CONTENT_MEDIA_JIT → DELAY/EXPIRY FAILURE PROOF`

**UPD if any**

None.

**Evidence needed**

Controlled delayed-adoption and provider-expiry handling plan; exact contract/plan retention evidence.

---

## LIVE-PT-151 — Restream recording is deleted while Cloudflare recording remains

**Scenario class**

Partial multi-provider deletion.

**Why it matters**

Restream documents permanent manual deletion, while Cloudflare recordings are independent objects.

**Authority**

Representation-complete deletion; Privacy orchestration; C&M ownership; OQ-030; `LIVE-GAP-014`.

**Owning Domains**

Privacy orchestration; Content & Media source consequences; external providers as evidence/processors.

**Preconditions**

Both Restream and Cloudflare copies are in scope for deletion/disposition.

**Timeline**

Restream delete completes → Cloudflare recording remains → NewYou reconciliation sees partial completion → overall governed deletion remains pending for the scope requiring both.

**Expected invariants**

- one provider's delete success cannot terminalise another provider's obligation;
- processor progress remains per-representation/per-provider;
- deletion completion is not inferred from current provider binding;
- retry exhaustion on remaining copy is not completion.

**Questions**

What Restream evidence can be captured beyond UI success? Is an API/contractual evidence path available? How is Cloudflare residual reachability verified?

**Adversarial variants**

Restream copy expires naturally while Cloudflare persists; Cloudflare delete succeeds first; one provider result is unknown.

**Analysis**

No new semantic rule is required. This is a concrete multi-provider proof obligation under existing deletion doctrine.

**Semantic disposition**

`PASS / PARTIAL_PROVIDER_DELETION_REMAINS_PENDING`

**Proof route**

`OQ-030 + LIVE-GAP-014 → PROVIDER EMPIRICAL + RECONCILIATION PROOF`

**UPD if any**

None.

**Evidence needed**

Provider-specific deletion evidence and residual-access testing.

---

## LIVE-PT-152 — Cloudflare signed playback is enabled but participant entitlement is later revoked

**Scenario class**

Provider playback protection / NewYou access authority.

**Why it matters**

Cloudflare can require signed URLs on live input/videos, but provider signing is a delivery mechanism, not NewYou entitlement authority.

**Authority**

Entitlements current-authority rule; Architecture bounded delivery capability; Product protected playback.

**Owning Domains**

Entitlements for access; C&M for publication; provider for transport enforcement only.

**Preconditions**

Cloudflare `requireSignedURLs=true`; participant previously obtained a valid bounded playback capability; current entitlement is revoked/expired/deleted.

**Timeline**

Authorised request → signed provider capability issued → entitlement later ends → participant retries old/new playback.

**Expected invariants**

- signed provider URL/token never becomes entitlement;
- NewYou refuses issuance of new capability after current access ends;
- already-issued capability must be bounded according to approved security policy/provider behaviour;
- C&M withdrawal and Entitlement revocation remain independent guards.

**Questions**

What token lifetime/revocation controls are actually available? Can an already-open player continue after token expiry/revocation? What cache/CDN effects apply?

**Adversarial variants**

Copied token; second browser; entitlement revoked during active playback; replay withdrawn while entitlement remains.

**Analysis**

Current documentation supports the mechanism seam but does not resolve exact stale-capability behaviour. Existing OQ-014/OQ-020 proof remains required.

**Semantic disposition**

`PASS_WITH_REFINEMENT / TRANSPORT_GUARD_NOT_AUTHORITY`

**Proof route**

`OQ-014/OQ-020 → ENTITLEMENT+C&M JIT → STALE_CAPABILITY PROOF`

**UPD if any**

None.

**Evidence needed**

Signed-token TTL/revocation/cache and already-open-player tests.

---

## LIVE-PT-153 — Restream and Cloudflare recordings disagree on completeness and an operator manually selects one for adoption

**Scenario class**

Manual provider artifact adoption / quality divergence / governed media identity.

**Why it matters**

Dual-provider recording can leave one complete representation and one partial/corrupt/truncated representation. Operational convenience must not silently choose governed media truth.

**Authority**

Content & Media owns governed media identity/version/publication; accepted `LIVE-GAP-012` capture→governed-media adoption seam.

**Owning Domains**

Content & Media; Events only for occurrence association; providers evidence only.

**Preconditions**

At least two provider artifacts exist for one occurrence with different completeness/quality.

**Timeline**

Artifacts A/B discovered → operator/JIT evaluates approved evidence → exact artifact(s) deliberately adopted into platform media identity/version lineage → publication remains separate approval.

**Expected invariants**

- import/selection is an explicit governed adoption action;
- provider readiness or UI ordering cannot select the source automatically;
- adopted media retains exact provider/source lineage;
- manual selection is attributable/auditable where material;
- adoption does not itself publish replay.

**Questions**

What evidence/role/review is required for manual adoption? Can segments from both providers be composed into one successor? What quality checks are mandatory?

**Adversarial variants**

Restream full but audio degraded; Cloudflare partial but better quality; operator selects wrong source; later better artifact arrives.

**Analysis**

The independent review's manual-adoption case belongs exactly under existing `LIVE-GAP-012`. No new Product gap is warranted.

**Semantic disposition**

`PASS_WITH_REFINEMENT / EXISTING_JIT_ADOPTION_SEAM`

**Proof route**

`LIVE-GAP-012 → CONTENT_MEDIA_JIT → MANUAL/CONCURRENT ADOPTION PROOF`

**UPD if any**

None.

**Evidence needed**

JIT adoption contract and concurrent/manual selection tests.

---

## LIVE-PT-154 — Provider documentation appears sufficient, so OQ-020 is declared resolved without controlled proof

**Scenario class**

Evidence sufficiency / governance failure.

**Why it matters**

Provider documentation describes nominal capabilities but cannot establish NewYou's exact retry, ambiguity, callback-order, latency, residual-access and cross-provider behaviour.

**Authority**

Roadmap OQ-020; Architecture provider-evidence and failure-injection requirements; accepted closure/proof doctrine.

**Owning Domains**

No new Domain. Gate resolution belongs to governed provider/architecture review.

**Preconditions**

Current first-party documentation gathered as in `LIVE-EV-001...006`.

**Timeline**

Documentation reviewed → team proposes marking OQ-020 complete without controlled live tests → governance evaluates evidence sufficiency.

**Expected invariants**

- documentation establishes capability claims, not production proof;
- OQ-020 remains open until the approved gate owner accepts controlled/contractual evidence sufficient for the selected path;
- exact provider failure behaviour is tested rather than inferred;
- vendor fact never becomes Product meaning.

**Questions**

Which OQ-020 acceptance matrix and controlled-live cases are required before the path is certified?

**Adversarial variants**

Docs omit retry behaviour; account plan differs; provider changes feature; UI behaviour differs from API; callback timing varies.

**Analysis**

Pass M is evidence preparation, not provider certification.

**Semantic disposition**

`PASS / DOCUMENTATION_NOT_GATE_COMPLETION`

**Proof route**

`OQ-020 → CONTROLLED_LIVE + FAILURE_INJECTION + OPERATOR RECOVERY EVIDENCE`

**UPD if any**

None.

**Evidence needed**

Approved provider-validation matrix and controlled execution evidence on the selected account/configuration.

---

# 7. Pass M synthesis

Pass M proposes the following working conclusions:

1. **The preferred DEC-190 path is technically plausible but remains empirically gated.** Current first-party docs support Restream Custom RTMPS → Cloudflare Stream, but do not certify NewYou's production path.
2. **Restream paid-path automatic recording is a material privacy/provider constraint.** Custom RTMP requires paid Restream, and current Restream docs say paid live streams are automatically recorded.
3. **No-recording occurrences must fail closed against an unproven Restream path.** Until OQ-020/OQ-021 prove a valid non-recording configuration or approved recording authority, the path cannot be assumed safe for an occurrence where recording is not authorised.
4. **This does not yet contradict DEC-190.** DEC-190 says `Prefer`, and its architecture detail/provider validation is explicitly pending. OQ-020/OQ-021 are the correct adjudication route.
5. **Cloudflare connection is not participant delivery.** A connected input may still be non-playable.
6. **Cloudflare live-input evidence and video-processing evidence are separate planes.** Events must not infer replay readiness from disconnect; C&M must not infer occurrence completion from video readiness.
7. **Cloudflare provider idempotency is useful but bounded.** Its six-hour account-scoped key cannot replace NewYou durable identity/idempotency/reconciliation.
8. **Long-delayed ambiguous create recovery must reconcile before repeating external creation.** Provider key expiry does not authorise blind duplicate create.
9. **One Restream→Cloudflare occurrence may generate multiple external recording representations.** Restream and Cloudflare copies can coexist and may differ in readiness/completeness.
10. **One Cloudflare Live Input may generate multiple video IDs.** Disconnect/reconnect beyond timeout can segment the same business occurrence into multiple provider recordings.
11. **Deleting a Cloudflare Live Input does not delete its recordings.** Input retirement and recording disposition are separate obligations.
12. **Provider retention is not NewYou retention authority.** Restream's 15/30-day recording window is an external operational constraint, not a Product/media retention policy.
13. **Partial deletion across providers is not completion.** Restream deletion/expiry cannot terminalise Cloudflare or other in-scope obligations.
14. **Provider signed playback is transport enforcement, not entitlement authority.** Existing current-access/stale-capability doctrine remains correct.
15. **Manual artifact adoption belongs to existing Content & Media JIT.** Dual-provider quality divergence does not justify a new Domain or gap.
16. **Current provider documentation strengthens, rather than resolves, `LIVE-GAP-014`.** Representation inventory and non-resurrection proof remain necessary.
17. **No new Product semantic delta is warranted.** `LIVE-UPD-007` remains unwarranted.
18. **No new Live gap is warranted.** `LIVE-GAP-015` remains unwarranted; existing gaps route every finding.
19. **The first provider evidence entries are now justified.** `LIVE-EV-001...LIVE-EV-006` record current first-party facts with explicit evidence limits.
20. **OQ-020 remains open.** Documentation alone is insufficient for gate completion.
21. **Broad semantic discovery remains parked.** Pass M is a bounded empirical-evidence extension only.

---

# 8. Gap/UPD adjudication

## 8.1 No LIVE-UPD-007

No new Product decision package is justified.

The most material new fact — Restream automatic paid-plan recording — routes through existing:

- `LIVE-GAP-002 / OQ-020` for provider compatibility;
- `LIVE-GAP-003 / OQ-021` for recording/privacy authority;
- `LIVE-GAP-011` for provider capture lifecycle/finalisation;
- `LIVE-GAP-013` for provider enforcement of recording-aware behaviour where applicable;
- `LIVE-GAP-014 / OQ-030/OQ-031` for processor deletion/non-resurrection.

Creating `LIVE-UPD-007` would duplicate existing authority/gates.

## 8.2 No LIVE-GAP-015

Every Pass-M uncertainty already has an owner:

- provider path/failure → GAP-002/OQ-020;
- recording/privacy → GAP-003/OQ-021;
- provider capture lifecycle → GAP-011;
- capture→governed media → GAP-012;
- recording-aware provider capability → GAP-013;
- processor deletion/non-resurrection → GAP-014/OQ-030/OQ-031;
- stale protected delivery → existing C&M/OQ-014 route.

No new gap is justified merely because provider evidence became more specific.

## 8.3 LIVE-EV-001...006 are proposed

Unlike earlier passes, Pass M explicitly researched current first-party provider documentation. Provider evidence identifiers are therefore now appropriate.

They remain non-authoritative evidence records and must be revalidated when OQ-020 is actually closed if provider documentation/configuration has changed.

---

# 9. Required future controlled proof matrix

Pass M does not execute provider tests, but narrows the later OQ-020 matrix.

At minimum controlled evidence should include:

1. Restream paid Custom RTMP → Cloudflare RTMPS normal path.
2. Exact Restream automatic recording behaviour for that path.
3. Whether Restream recording can be disabled, and how the setting is proven before live execution.
4. Cloudflare `recording.mode=off` and `automatic` behaviour.
5. Connected-but-not-playable startup.
6. Malformed/missing AAC and bad keyframe input error path.
7. Create timeout + same idempotency key retry.
8. Restart after provider accepted create but before local response persistence.
9. Recovery after idempotency-key expiry.
10. Disconnect shorter/longer than `timeoutSeconds` and resulting Video IDs.
11. Duplicate/reordered/lost live-input notifications.
12. Duplicate/reordered/lost video processing notifications.
13. Restream and Cloudflare dual-recording inventory and divergent completeness.
14. Live Input deletion with residual recording enumeration.
15. Video deletion and residual access checks.
16. Restream deletion/expiry versus Cloudflare retained copies.
17. Signed playback TTL/stale-capability behaviour.
18. Provider outage and operator recovery without rewriting NewYou truth.

This matrix is future evidence work only. It does not assign proof identifiers or authorise Phase 8.

---

# 10. Pass M proposed disposition

**Pass M outcome:** `PASS_WITH_BLOCKING_PROVIDER_FINDING / PROPOSED / AWAITING_USER_ACCEPTANCE`

The pass does **not** find an architecture contradiction or new Product gap.

It does find one materially stronger provider-path condition:

> Until OQ-020/OQ-021 prove exact Restream paid-plan recording controls, the preferred Restream path must not be assumed compatible with an occurrence for which recording is not currently authorised.

This is a fail-closed provider/privacy finding under existing gates, not a new rule invented by Pass M.

Broad semantic discovery remains parked.

---

# 11. Stop point

Pass M stops here.

Do **not** automatically proceed to Pass N.

If the user accepts Pass M, the next legitimate bounded pass should only be selected after reassessing whether another evidence class materially advances an existing open gate. A general edge-case sweep remains prohibited by the accepted parking rule.
