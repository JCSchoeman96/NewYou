# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.1.md

- **Status:** WORKING / NON-AUTHORITATIVE / PASS M ACCEPTED STATUS SUCCESSOR / PRE-JIT DISCOVERY PARKED
- **Document version:** v0.12.1
- **Date:** 2026-10-11
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.0.md`
- **Repository baseline revalidated:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Predecessor proposed Pass-M head:** `c40ffd1debe574982ba6850b8e759f252af18e22`
- **Pass M discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.13.0.md`
- **Pass M discovery commit:** `e2d15e2861b991a624e9e28d5e6224f6ac65dbae`
- **Provider evidence revalidation date:** `2026-10-11`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic effect:** STATUS / PROVENANCE ACCEPTANCE ONLY. No new Product semantics, pressure tests, UPD, gap, Domain, gate closure, provider certification or implementation authority are created here.

---

# 1. Acceptance event

The user explicitly accepted Pass M on 2026-10-11 and instructed continuation into semantic-preserving compression.

Before recording acceptance, the current repository baseline, current authority routing and the six first-party provider evidence records were revalidated.

The material Pass-M evidence remains supported as of 2026-10-11.

Therefore:

```text
PASS M
=> ACCEPTED_WORKING_LOCK

LIVE-PT-142...154
=> ACCEPTED_WORKING_LOCK

LIVE-EV-001...006
=> ACCEPTED WORKING PROVIDER EVIDENCE

BROAD SEMANTIC DISCOVERY
=> STILL PARKED
```

---

# 2. Provider-evidence revalidation

## LIVE-EV-001 — Restream Custom RTMP

Current first-party Restream documentation still states that Custom RTMP requires a paid plan, accepts RTMPS, and does not provide API-dependent Restream Chat/Analytics features for custom channels.

**Revalidation source:** `https://support.restream.io/en/articles/369436-stream-to-a-custom-rtmp-channel`

**Evidence class:** provider capability documentation only.

## LIVE-EV-002 — Restream recording

Current first-party Restream documentation still supports the accepted plan-bounded recording facts: Standard/Professional recordings are stored for 15 days, Business for 30 days; maximum recording duration is 6 hours on Standard and 10 hours on Professional/Business; manual deletion is permanent.

**Revalidation sources:**

- `https://support.restream.io/en/articles/10599465-where-is-my-recording`
- `https://support.restream.io/en/articles/4379939-download-your-recordings`

**Evidence limit preserved:** failure to find a documented general “disable automatic recording” control is **not proof that such a control does not exist**. Exact no-recording compatibility remains fail-closed pending OQ-020/OQ-021 provider/privacy proof.

## LIVE-EV-003 — Cloudflare recording configuration

Current first-party Cloudflare documentation still supports RTMPS/SRT live inputs; recording mode `off | automatic`; `timeoutSeconds`; `requireSignedURLs`; and recording deletion scheduling via `deleteRecordingAfterDays` where applicable.

**Revalidation sources:**

- `https://developers.cloudflare.com/stream/stream-live/start-stream-live/`
- `https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/create/`
- `https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/update/`

**Evidence class:** provider mechanism documentation only.

## LIVE-EV-004 — Cloudflare create idempotency

Current first-party Cloudflare API documentation still states that Create Live Input accepts an account-scoped `Idempotency-Key` of up to 255 bytes, expiring six hours after the live input is created; reusing a key for a deleted input before expiry returns `409 Conflict`.

**Revalidation source:** `https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/create/`

**Evidence limit:** provider idempotency is bounded transport assistance; it does not replace NewYou durable intent/idempotency/reconciliation.

## LIVE-EV-005 — Cloudflare evidence planes

Current first-party Cloudflare documentation still supports the accepted distinction that an input can be connected while playback is not yet available; live-input connected/disconnected/errored notifications are distinct from video-processing ready/error evidence.

**Revalidation sources:**

- `https://developers.cloudflare.com/stream/stream-live/troubleshooting/`
- `https://developers.cloudflare.com/stream/stream-live/webhooks/`
- `https://developers.cloudflare.com/stream/manage-video-library/using-webhooks/`

**Evidence limit:** callback/status evidence remains non-authoritative and controlled failure/reorder/retry proof is still required.

## LIVE-EV-006 — Cloudflare deletion

Current first-party Cloudflare API documentation still states that deleting a Live Input retains existing recordings. Recording/video deletion remains a separate operation and must be accounted for independently.

**Revalidation source:** `https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/delete/`

**Evidence limit:** this proves a provider representation boundary, not representation-complete governed deletion.

---

# 3. Accepted Pass-M pressure tests

`LIVE-PT-142...LIVE-PT-154` are accepted exactly as proposed in predecessor v0.12.0 and Pass-M discovery v0.13.0.

Their accepted dispositions are:

| PT | Accepted disposition |
|---|---|
| `LIVE-PT-142` | `BLOCKED_PENDING_PROVIDER_AND_PRIVACY_PROOF / FAIL_CLOSED` |
| `LIVE-PT-143` | `PASS / PROVIDER_CONNECTED_NOT_DELIVERY_TRUTH` |
| `LIVE-PT-144` | `PASS_WITH_REFINEMENT / PROVIDER_IDEMPOTENCY_IS_BOUNDED` |
| `LIVE-PT-145` | `PASS / RECONCILE_BEFORE_NEW_CREATE` |
| `LIVE-PT-146` | `PASS_WITH_REFINEMENT / MULTIPLE_PROVIDER_COPIES_EXPECTED` |
| `LIVE-PT-147` | `PASS / ONE_INPUT_MAY_CREATE_MANY_RECORDINGS` |
| `LIVE-PT-148` | `PASS / SEPARATE_EVIDENCE_PLANES` |
| `LIVE-PT-149` | `PASS / INPUT_DELETION_NOT_RECORDING_COMPLETION` |
| `LIVE-PT-150` | `PASS_WITH_REFINEMENT / PROVIDER_RETENTION_NOT_DURABLE_AUTHORITY` |
| `LIVE-PT-151` | `PASS / PARTIAL_PROVIDER_DELETION_REMAINS_PENDING` |
| `LIVE-PT-152` | `PASS_WITH_REFINEMENT / TRANSPORT_GUARD_NOT_AUTHORITY` |
| `LIVE-PT-153` | `PASS_WITH_REFINEMENT / EXISTING_JIT_ADOPTION_SEAM` |
| `LIVE-PT-154` | `PASS / DOCUMENTATION_NOT_GATE_COMPLETION` |

No accepted Product semantic conclusion from Passes A–L is reopened.

---

# 4. Accepted Pass-M conclusions

The 21 Pass-M conclusions proposed in predecessor v0.12.0 are accepted as working evidence:

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
19. `LIVE-EV-001...LIVE-EV-006` are accepted provider evidence identifiers.
20. OQ-020 remains open; documentation does not complete the gate.
21. Broad semantic discovery remains parked.

---

# 5. Correct cumulative working state

After this acceptance:

- Passes A–M: `ACCEPTED_WORKING_LOCK`;
- `LIVE-PT-001...LIVE-PT-154`: accepted working evidence;
- `LIVE-UPD-001...LIVE-UPD-006`: current accepted working upstream-delta set;
- no `LIVE-UPD-007`;
- `LIVE-GAP-001...LIVE-GAP-014`: current accepted working gap set;
- no `LIVE-GAP-015`;
- `LIVE-EV-001...LIVE-EV-006`: accepted working provider evidence;
- the independent-review PT-028 correction remains current;
- the independent-review `LIVE-GAP-003` routing clarification remains current;
- broad semantic discovery remains parked.

---

# 6. Gates and delivery state remain unchanged

```text
OQ-020
=> OPEN

OQ-021
=> OPEN

PROVIDER DOCUMENTATION
!= CONTROLLED EMPIRICAL PROOF
!= GATE COMPLETION

FP-007
=> BLOCKED / NOT_SELECTED / NOT_PHASE7_AUTHORISED

IMPLEMENTATION
=> NOT AUTHORISED

PASS N
=> NOT AUTHORISED / NOT JUSTIFIED BY DEFAULT
```

Where promised communication scope requires them, OQ-036 remains applicable; OQ-017 remains conditional on reminder scope. OQ-029...OQ-032 retain their existing retention/deletion classifications. OQ-014 remains applicable to protected playback/correction propagation where relevant. OQ-022 remains the future event-commerce boundary.

---

# 7. Explicit non-changes

Pass-M acceptance does **not** mean:

- Restream is irrevocably selected;
- Cloudflare is irrevocably selected;
- the preferred provider path is certified;
- OQ-020 is closed;
- OQ-021 is closed;
- recording/consent/retention law is resolved;
- controlled-live proof is complete;
- provider documentation is elevated into NewYou authority;
- FP-007 is selected;
- Phase 7 has started;
- a Final Feature Pack Contract exists;
- proof classification is finalised;
- implementation is authorised.

---

# 8. Accepted outcome

**Outcome:** `PASS_WITH_BLOCKING_PROVIDER_FINDING / ACCEPTED_WORKING_LOCK / PREJIT_DISCOVERY_PARKED`

The narrow blocking provider finding remains fail-closed:

> Until OQ-020/OQ-021 prove the exact Restream paid-plan recording controls for the selected account/path, the preferred Restream route must not be assumed compatible with an occurrence for which recording is not currently authorised.

This accepted provider evidence is now eligible to be compressed into the final compact working pack while retaining exact deep provenance.
