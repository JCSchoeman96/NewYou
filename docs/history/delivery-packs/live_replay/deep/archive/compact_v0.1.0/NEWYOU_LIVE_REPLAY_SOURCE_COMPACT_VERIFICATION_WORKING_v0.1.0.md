# NewYou Live & Replay Source ↔ Compact Verification — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE MECHANICAL CONSISTENCY PROOF
- **Implementation:** NOT AUTHORISED
- **Canonical source:** `deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.1.md`
- **Compact pack:** `NEWYOU_LIVE_REPLAY_FINAL_COMPACT_PACK_v0.1.0`
- **Historical relocation commit:** `baa848e8283677b784578105fe75f12184f07685`
- **Provider-evidence revalidation:** `2026-10-11`

## 1. Identifier coverage

| Check | Expected | Observed | Result |
|---|---|---|---|
| Pressure tests | `LIVE-PT-001...154`, 154 contiguous IDs | 154 unique accepted IDs represented by the deep source / evidence index, min 1, max 154 | PASS |
| UPDs | `LIVE-UPD-001...006`; no 007 | 001...006 register rows present; no 007 register row | PASS |
| Gaps | `LIVE-GAP-001...014`; no 015 | 001...014 register rows present; no 015 register row | PASS |
| Provider evidence | `LIVE-EV-001...006` | 6 accepted evidence records, min 1, max 6 | PASS |

## 2. Pass / status verification

```text
Passes A–M = ACCEPTED_WORKING_LOCK
Broad semantic discovery = PARKED
OQ-020 = OPEN
OQ-021 = OPEN
FP-007 = NOT SELECTED / NOT PHASE-7 AUTHORISED
IMPLEMENTATION = NOT AUTHORISED
PASS N = NOT JUSTIFIED BY DEFAULT
```

Pass-M evidence was revalidated against current first-party provider documentation on `2026-10-11` before acceptance. Documentation remains evidence only and does not complete OQ-020/OQ-021.

## 3. Corrected-route verification

- **PT-028 corrected route survived:** PASS. Current route is scope adjudication → `LIVE-GAP-009` / Product authority if cancellation is included → Events JIT → executable proof.
- **GAP-003 corrected routing survived:** PASS. Primary semantic route remains OQ-021; OQ-029...032 compose only where applicable; GAP-014 remains provider empirical proof.
- **Pass-M evidence limit survived:** PASS. No absence-of-documentation claim was upgraded to impossibility and OQ-020 remains open.

## 4. Compact key-term / route coverage

Required governed identifiers/routes are present across Contract + Delta/Gap Register + Evidence Index + Compression Audit.

Checked terms: `LIVE-UPD-001...006`, `LIVE-GAP-001...014`, `LIVE-EV-001...006`, OQ-014, OQ-017, OQ-020, OQ-021, OQ-022, OQ-029, OQ-030, OQ-031, OQ-032, OQ-036, DEC-190 and FP-007.

**Missing required terms:** NONE.

## 5. Semantic-distinction verification

The compact Contract explicitly preserves:

- occurrence identity versus provider resource identity;
- registration versus entitlement versus join capability versus provider presence versus attendance versus replay entitlement/consumption;
- canonical NewYou identity versus provider identity/role labels;
- recording intent versus provider capture versus governed-media adoption versus replay publication;
- recording notice versus recording permission;
- role/context versus capture scope;
- purpose withdrawal versus Full Deletion;
- current publication eligibility versus physical retention;
- deletion obligation/request/acknowledgement/provider status/verified completion;
- correction class and successor/withdrawal semantics;
- promotional derivative versus replay semantics;
- Communications delivery versus source authority;
- current owner authority over stale provider/message/token/cache/projection state;
- owner-mediated recovery without a shared-write Live orchestration Domain.

**Result:** PASS.

## 6. Historical relocation verification

Historical discovery/register sources were relocated from the Live/Replay root into `deep/archive/` at commit `baa848e8283677b784578105fe75f12184f07685` by reusing the exact pre-relocation Git blob SHA at the archive path and removing only the old path.

- historical discovery/register files relocated: **34**;
- accepted v0.12.1 status successor moved intact to `deep/` using its original blob SHA;
- source/archive Git blob identity: **PASS for all 34 relocated historical files**;
- byte counts remain identical because the same content-addressed Git blob object is referenced before and after relocation;
- no historical document content or line ending was rewritten.

The exact local human-review cumulative v0.12.0 Markdown copy used during compression remains separately identified by SHA-256 `e12f757253dea14738cc87d9254ffb9f2e1d001c925897a16fc55dbadce2ce3d` and 83103 bytes in the Evidence Index. It is not treated as a competing repository authority; exact repository provenance is the byte-preserved discovery/register series.

## 7. Compression verification matrix

| Source concept | Compact destination | Result |
|---|---|---|
| occurrence ownership | Contract | PRESERVED |
| entitlement/access | Contract | PRESERVED |
| attendance | Contract + Delta Register | PRESERVED |
| recording/capture | Contract | PRESERVED |
| notice/consent | Contract + Gap Register | PRESERVED |
| withdrawal | Contract + UPD-006 | PRESERVED |
| retention/deletion | Contract + GAP-014 | PRESERVED |
| Full Deletion | Contract | PRESERVED |
| replay correction | Contract | PRESERVED |
| promotional derivatives | Contract | PRESERVED |
| communications | Contract + GAP-006 | PRESERVED |
| cross-domain recovery | Contract | PRESERVED |
| provider facts | Evidence Index | PRESERVED |
| `LIVE-PT-001...154` | Evidence Index + deep source | COMPLETE |
| `LIVE-UPD-001...006` | Delta Register | COMPLETE |
| `LIVE-GAP-001...014` | Delta Register | COMPLETE |
| `LIVE-EV-001...006` | Evidence Index | COMPLETE |
| historical discovery/register files | `deep/archive/` | BYTE-PRESERVED |

## 8. Guard assertions

All required compression assertions remain true, including:

```text
LIVE-UPD-007 = NOT CREATED
LIVE-GAP-015 = NOT CREATED
OQ-020 = OPEN
OQ-021 = OPEN
provider documentation = evidence only
controlled proof = still required
FP-007 = NOT PHASE-7 AUTHORISED
implementation = NOT AUTHORISED
Pass N = NOT JUSTIFIED BY DEFAULT
```

Scarce event commerce remains outside FP-007. OQ-036 remains scoped to promised/required communication journeys. OQ-017 remains conditional on reminders being promised. DEC-190 remains a preferred path with architecture detail pending rather than irreversible provider certification.

## 9. Verification outcome

**Result:** `PASS / COMPACT CONTENT AND REPOSITORY RELOCATION CONSISTENT WITH ACCEPTED LIVE & REPLAY SOURCE`.

Final pack completion additionally requires the root `PACK_MANIFEST_v0.1.0.json` to validate as JSON and a fresh final main↔branch comparison after the manifest commit. Those checks are completion-time checks and are intentionally not self-referential claims about this file's own future manifest entry.
