# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PASS M PROPOSED / AWAITING USER ACCEPTANCE
- **Document version:** v0.12.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.11.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Predecessor corrected parked head:** `12db157f43da7c3743a4c0a7fc7dcbb415ac248c`
- **Pass M discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.13.0.md`
- **Pass M discovery commit:** `e2d15e2861b991a624e9e28d5e6224f6ac65dbae`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Broad semantic discovery:** REMAINS PARKED
- **Pass class:** BOUNDED PROVIDER EMPIRICAL PRESSURE TEST

---

# 1. Pass M scope

Pass M does not reopen broad semantic discovery.

It performs a bounded current-provider evidence pass prompted by independent-review provider observations and explicit user continuation. The pass is limited to the current preferred Restream → Custom RTMPS → Cloudflare Stream path and the existing OQ-020/OQ-021/OQ-030 proof seams.

No accepted Product, Architecture, Domain, Roadmap, UPD or gap semantics are silently rewritten.

---

# 2. Proposed provider evidence entries

Pass M proposes the first provider evidence records:

- `LIVE-EV-001` — Restream Custom RTMP requires paid plan, accepts RTMPS, and API-dependent Chat/Analytics do not work for custom channels.
- `LIVE-EV-002` — Restream paid streams are automatically recorded; current documented recording retention is 15 days Standard/Professional and 30 days Business; documented maximum recording duration is 6h Standard and 10h Professional/Business; manual delete is permanent.
- `LIVE-EV-003` — Cloudflare Live Inputs accept RTMPS/SRT; recording mode is `off` or `automatic`; automatic mode records for replay; `timeoutSeconds` controls disconnect→new-video segmentation; signed-URL policy can be applied at input/recording level.
- `LIVE-EV-004` — Cloudflare Create Live Input supports account-scoped provider idempotency with maximum 255-byte key, six-hour expiry, and 409 behaviour when a deleted input's key is reused before expiry.
- `LIVE-EV-005` — Cloudflare input connection and video readiness are separate evidence planes; connected input may still be non-playable; live-input connected/disconnected/error notifications are separate from video ready/error processing webhooks.
- `LIVE-EV-006` — deleting a Cloudflare Live Input retains existing recordings; deleting a Stream video is a separate operation documented to delete that video and its copies.

All EV items are current first-party provider evidence only. They are not NewYou authority and must be revalidated when OQ-020 is actually closed if provider behaviour/documentation changes.

---

# 3. Proposed Pass-M pressure tests

## `LIVE-PT-142` — Recording not authorised but preferred Restream Custom RTMP path is used

**Proposed disposition:** `BLOCKED_PENDING_PROVIDER_AND_PRIVACY_PROOF / FAIL_CLOSED`

Current Restream documentation creates a material compatibility risk: Custom RTMP requires paid Restream and paid Restream streams are documented as automatically recorded. The reviewed official docs did not expose a general disable-recording control; absence from docs is not proof of impossibility.

**Route:** `OQ-020 + OQ-021 → provider confirmation + controlled live proof`.

No new UPD/gap. Reuse existing provider/recording gaps.

## `LIVE-PT-143` — Cloudflare input connected but participant playback unavailable

**Proposed disposition:** `PASS / PROVIDER_CONNECTED_NOT_DELIVERY_TRUTH`

Connected provider input is not successful participant delivery, attendance, occurrence completion or replay readiness.

## `LIVE-PT-144` — Live Input create times out and retry occurs within Cloudflare idempotency window

**Proposed disposition:** `PASS_WITH_REFINEMENT / PROVIDER_IDEMPOTENCY_IS_BOUNDED`

Provider idempotency helps transport retries but does not replace NewYou durable identity, intent, idempotency or restart-safe reconciliation.

## `LIVE-PT-145` — Ambiguous create retry occurs after provider idempotency expiry

**Proposed disposition:** `PASS / RECONCILE_BEFORE_NEW_CREATE`

Six-hour provider-key expiry cannot authorise blind duplicate external creation.

## `LIVE-PT-146` — One occurrence creates Restream and Cloudflare recordings

**Proposed disposition:** `PASS_WITH_REFINEMENT / MULTIPLE_PROVIDER_COPIES_EXPECTED`

One occurrence can have multiple independent provider recording representations with different readiness/completeness. Neither automatically becomes governed media.

## `LIVE-PT-147` — Cloudflare disconnect exceeds timeout and another Video ID is created

**Proposed disposition:** `PASS / ONE_INPUT_MAY_CREATE_MANY_RECORDINGS`

One provider Live Input can map to several recordings while NewYou occurrence identity remains stable.

## `LIVE-PT-148` — Live-input and video-processing callbacks arrive in different orders

**Proposed disposition:** `PASS / SEPARATE_EVIDENCE_PLANES`

Connected/disconnected/error evidence cannot be collapsed with ready/error media-processing evidence.

## `LIVE-PT-149` — Cloudflare Live Input deleted but recordings remain

**Proposed disposition:** `PASS / INPUT_DELETION_NOT_RECORDING_COMPLETION`

Input retirement is not recording deletion and cannot terminalise privacy/media deletion obligations.

## `LIVE-PT-150` — Restream recording expires before governed media adoption completes

**Proposed disposition:** `PASS_WITH_REFINEMENT / PROVIDER_RETENTION_NOT_DURABLE_AUTHORITY`

Restream's documented retention window is an external operational constraint, not NewYou media-retention authority or a durable replay guarantee.

## `LIVE-PT-151` — Restream recording deleted while Cloudflare recording remains

**Proposed disposition:** `PASS / PARTIAL_PROVIDER_DELETION_REMAINS_PENDING`

One provider's deletion success/expiry cannot complete a multi-provider deletion obligation.

## `LIVE-PT-152` — Cloudflare signed playback enabled but current entitlement later revoked

**Proposed disposition:** `PASS_WITH_REFINEMENT / TRANSPORT_GUARD_NOT_AUTHORITY`

Provider signed URLs are enforcement mechanisms, not entitlement authority; stale-capability proof remains required.

## `LIVE-PT-153` — Restream and Cloudflare recordings disagree and operator manually selects one

**Proposed disposition:** `PASS_WITH_REFINEMENT / EXISTING_JIT_ADOPTION_SEAM`

Manual/external provider artifact adoption belongs under existing `LIVE-GAP-012` and Content & Media JIT; provider readiness or UI order cannot select governed media truth.

## `LIVE-PT-154` — Documentation is treated as sufficient to resolve OQ-020

**Proposed disposition:** `PASS / DOCUMENTATION_NOT_GATE_COMPLETION`

Current official docs define capabilities and constraints but cannot substitute for controlled live, failure-injection, retry/reorder/restart, deletion and operator-recovery evidence.

---

# 4. Proposed Pass-M conclusions

If accepted, Pass M establishes these working conclusions:

1. DEC-190's preferred path is technically plausible but remains empirically gated.
2. Restream paid-path automatic recording is a material privacy/provider constraint.
3. A no-recording occurrence must fail closed against the Restream path until OQ-020/OQ-021 prove a valid approved configuration.
4. The finding does not yet contradict DEC-190 because DEC-190 says `Prefer` and architecture detail/provider validation is pending.
5. Cloudflare connection is not participant delivery.
6. Live-input status and video-processing readiness are separate evidence planes.
7. Cloudflare provider idempotency is bounded and cannot replace NewYou durable idempotency/reconciliation.
8. Post-expiry ambiguous provider creates must reconcile before a new create.
9. One occurrence may generate multiple provider recordings across Restream and Cloudflare.
10. One Cloudflare Live Input may generate multiple Video IDs after qualifying disconnects/reconnects.
11. Deleting a Cloudflare Live Input does not delete its recordings.
12. Provider retention windows are not NewYou retention authority.
13. Partial multi-provider deletion is not completion.
14. Provider signed playback is transport enforcement, not entitlement authority.
15. Manual provider-artifact adoption remains a Content & Media JIT concern under `LIVE-GAP-012`.
16. Current provider evidence strengthens rather than resolves `LIVE-GAP-014`.
17. No `LIVE-UPD-007` is warranted.
18. No `LIVE-GAP-015` is warranted.
19. `LIVE-EV-001...LIVE-EV-006` are now justified as provider evidence identifiers.
20. OQ-020 remains open; documentation does not complete the gate.
21. Broad semantic discovery remains parked.

---

# 5. Gap and ID adjudication

## No `LIVE-UPD-007`

No new Product semantic owner is missing.

The material Restream recording finding routes through existing OQ/provider/privacy gates.

## No `LIVE-GAP-015`

Existing gaps already cover:

- provider path/failure: `LIVE-GAP-002`;
- recording/privacy: `LIVE-GAP-003`;
- provider capture lifecycle: `LIVE-GAP-011`;
- capture→governed-media adoption: `LIVE-GAP-012`;
- recording-aware provider enforcement: `LIVE-GAP-013`;
- processor deletion/non-resurrection: `LIVE-GAP-014`.

## Proposed new evidence range

`LIVE-EV-001...LIVE-EV-006`

Status: `PROPOSED / AWAITING USER ACCEPTANCE`.

---

# 6. Provider proof implications

Pass M proposes that future OQ-020 controlled validation must explicitly exercise:

- paid Restream Custom RTMP → Cloudflare RTMPS normal flow;
- exact Restream automatic recording behaviour and whether it can be disabled;
- Cloudflare recording mode `off` versus `automatic`;
- connected-but-not-playable startup;
- malformed audio/keyframe path;
- timeout + same-key retry;
- restart after provider accepted create but before local persistence;
- retry after provider idempotency expiry;
- disconnect/reconnect segmentation;
- duplicate/reordered/lost live-input notifications;
- duplicate/reordered/lost video-processing notifications;
- Restream + Cloudflare dual recording inventory and divergent completeness;
- Live Input deletion with residual recording checks;
- video deletion and residual-access checks;
- multi-provider partial deletion;
- signed playback stale-capability behaviour;
- provider outage and owner-mediated operator recovery.

No TB/VS/HH identifier is assigned here.

---

# 7. Proposed cumulative state

If Pass M is accepted:

- Passes A-M become `ACCEPTED_WORKING_LOCK`;
- `LIVE-PT-001...LIVE-PT-154` become accepted, with v0.11.0 continuing to supersede the historical PT-028 route;
- `LIVE-UPD-001...006` remain accepted;
- no `LIVE-UPD-007`;
- `LIVE-GAP-001...014` remain accepted;
- no `LIVE-GAP-015`;
- `LIVE-EV-001...006` become accepted provider evidence;
- broad semantic discovery remains parked;
- OQ-020 and OQ-021 remain unresolved/blocking according to their existing authority;
- FP-007 remains `BLOCKED / NOT_SELECTED / NOT_PHASE7_AUTHORISED`.

---

# 8. Proposed Pass-M outcome

**Outcome:** `PASS_WITH_BLOCKING_PROVIDER_FINDING / PROPOSED / AWAITING_USER_ACCEPTANCE`

The blocking provider finding is narrow and fail-closed:

> Until OQ-020/OQ-021 prove the exact Restream paid-plan recording controls for the selected account/path, the preferred Restream route must not be assumed compatible with an occurrence for which recording is not currently authorised.

No Product amendment is proposed from provider documentation alone.

---

# 9. Stop point

Pass M stops here.

Do not automatically start Pass N.

A future bounded pass is justified only if it materially advances an existing open gate or if new authority/evidence satisfies the accepted reopen criteria. A general semantic edge-case sweep remains prohibited.
