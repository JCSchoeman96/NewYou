# NewYou Live & Replay Source ↔ Compact Verification — Working v0.1.1

- **Status:** WORKING / NON-AUTHORITATIVE MECHANICAL CONSISTENCY PROOF / HARDENED
- **Implementation:** NOT AUTHORISED
- **Canonical semantic source:** `deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.2.md`
- **Compact pack:** `NEWYOU_LIVE_REPLAY_FINAL_COMPACT_PACK_v0.1.1`
- **Historical discovery/register relocation commit:** `baa848e8283677b784578105fe75f12184f07685`
- **Provider-evidence revalidation:** `2026-10-11`

## 1. Identifier coverage

| Check | Expected | Result |
|---|---|---|
| Pressure tests | `LIVE-PT-001...154`, contiguous accepted coverage | PASS |
| UPDs | `LIVE-UPD-001...006`; no 007 | PASS |
| Gaps | `LIVE-GAP-001...014`; no 015 | PASS |
| Provider evidence | `LIVE-EV-001...006` | PASS |

## 2. Guard state

```text
Passes A–M = ACCEPTED_WORKING_LOCK
Broad semantic discovery = PARKED
OQ-020 = OPEN
OQ-021 = OPEN
FP-007 = NOT SELECTED / NOT PHASE-7 AUTHORISED
IMPLEMENTATION = NOT AUTHORISED
PASS N = NOT JUSTIFIED BY DEFAULT
```

Provider documentation remains evidence only; it does not complete OQ-020/OQ-021.

## 3. Corrected-route verification

- **PT-028:** PASS — cancellation is optional FP-007 scope; if included, Product authority resolves through `LIVE-GAP-009` before Events JIT.
- **GAP-003:** PASS — OQ-021 remains primary semantic route; OQ-029...032 compose only as applicable; GAP-014 remains provider proof.
- **Pass-M evidence limit:** PASS — EV-002 explicitly retains current paid-stream automatic-recording documentation, while absence of a documented disable control is not upgraded to impossibility.

## 4. Hardening-invariant verification

- **Replay correction failure:** PASS — ordinary material V1 may remain current only while still safe/lawful/currently eligible; safety/legal/consent-invalid V1 remains withdrawn/fail-closed if successor processing fails.
- **Communications mandatory-class guard:** PASS — optional reminder/marketing/convenience roles may not masquerade as mandatory safety/product notices.
- **Communications Resource guard:** PASS — no Live-specific Communications Resource is introduced; existing Communications ownership and logical MessageIntent/DeliveryAttempt seams are reused unless future governed evidence changes that conclusion.
- **Provider-create ordering:** PASS — ambiguous create after timeout/restart/idempotency expiry requires reconciliation before repeat; provider-key expiry is not authority for blind duplicate create.
- **Full Deletion timing:** PASS — locked 14-day cancellation window and no recovery/reconstruction after irreversible completion are explicit.

## 5. Semantic distinctions retained

The compact Contract explicitly preserves:

- occurrence identity vs schedule/version vs provider resource identity;
- registration vs entitlement vs join capability vs provider presence vs attendance;
- canonical identity/role vs provider labels;
- recording authority vs provider capture vs governed-media adoption vs replay publication;
- recording notice vs recording permission/current purpose authority;
- role/context vs capture scope;
- purpose withdrawal vs Full Deletion;
- current publication eligibility vs physical retention;
- deletion obligation/request/transport/provider ack/status/verified completion;
- replay correction class, successor/withdrawal and class-dependent failure semantics;
- replay/media versioning vs occurrence/schedule versioning;
- promotional derivative vs replay;
- Communications delivery vs source authority;
- mandatory vs optional communication classification;
- current owner authority over stale provider/message/token/cache/projection state;
- owner-mediated recovery without shared-write orchestration;
- provider idempotency vs NewYou business identity/idempotency, including reconcile-before-repeat.

**Result:** PASS.

## 6. Compact mapping

| Source concept | Compact destination | Result |
|---|---|---|
| occurrence ownership/identity | Contract | PRESERVED |
| registration/access | Contract + Delta | PRESERVED |
| attendance | Contract + Delta | PRESERVED |
| recording/capture/notice/roles | Contract + Delta | PRESERVED |
| withdrawal | Contract + UPD-006/GAP-003 | PRESERVED |
| retention/deletion/Full Deletion | Contract + GAP-014 | PRESERVED |
| replay rights/correction | Contract | PRESERVED |
| promotional derivatives | Contract | PRESERVED |
| communications | Contract + GAP-006 | PRESERVED |
| cross-domain recovery | Contract | PRESERVED |
| provider facts | Contract + Evidence Index | PRESERVED |
| `LIVE-PT-001...154` | Evidence Index + Deep Ledger + archive | COMPLETE |
| `LIVE-UPD-001...006` | Delta Register | COMPLETE |
| `LIVE-GAP-001...014` | Delta Register | COMPLETE |
| `LIVE-EV-001...006` | Evidence Index | COMPLETE |

## 7. Historical preservation

- The 34 historical discovery/register files relocated at `baa848e8283677b784578105fe75f12184f07685` retain identical Git blob identity at archive paths.
- Accepted status successor `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.1.md` remains intact under `deep/`.
- Superseded compact-pack v0.1.0 files are to be archived under `docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0` using their existing Git blob objects in the hardening commit.
- The local 83,103-byte v0.12.0 human-review Markdown source is referenced by SHA-256 only and is not falsely represented as a repository archive file.

## 8. Required pack checks before completion claim

Completion requires all of the following after the hardening manifest commit:

1. root read order resolves only to v0.1.1 compact artifacts;
2. `PACK_MANIFEST_v0.1.1.json` parses as valid JSON;
3. manifest byte counts/SHA-256 values match the generated hardened files;
4. deep ledger v0.12.2 hash/bytes match Evidence Index/manifest;
5. v0.1.0 compact predecessors are present under `docs/history/delivery-packs/live_replay/deep/archive/compact_v0.1.0` with original Git blob SHA identity;
6. main is unchanged from the verified baseline or, if changed, authority is re-resolved before certification;
7. branch remains ahead with merge base at the verified main baseline and diff remains confined to `docs/delivery/jit/live_replay/**`;
8. guard searches confirm no UPD-007/GAP-015/Phase-7 or implementation-authority promotion.

## 9. Verification outcome

**Result:** `PASS / HARDENED COMPACT CONTENT IS SEMANTICALLY CONSISTENT WITH THE ACCEPTED LIVE & REPLAY SOURCE`, subject to the completion-time repository and manifest checks in §8.
