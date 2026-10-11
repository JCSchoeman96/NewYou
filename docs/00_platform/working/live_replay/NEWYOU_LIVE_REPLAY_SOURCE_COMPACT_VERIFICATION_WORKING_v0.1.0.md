# NewYou Live & Replay Source ↔ Compact Verification — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE MECHANICAL CONSISTENCY PROOF
- **Implementation:** NOT AUTHORISED
- **Canonical source:** `deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.1.md`
- **Compact pack:** `NEWYOU_LIVE_REPLAY_FINAL_COMPACT_PACK_v0.1.0`

## 1. Identifier coverage

| Check | Expected | Observed | Result |
|---|---|---|---|
| Pressure tests | `LIVE-PT-001...154`, 154 contiguous IDs | 154 unique IDs, min 1, max 154 | PASS |
| UPDs | `LIVE-UPD-001...006`; no 007 | 001...006 register rows present; no 007 register row | PASS |
| Gaps | `LIVE-GAP-001...014`; no 015 | 001...014 register rows present; no 015 register row | PASS |
| Provider evidence | `LIVE-EV-001...006` | 6 unique IDs, min 1, max 6 | PASS |

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

- **PT-028 corrected route survived:** PASS. Current deep route is scope adjudication → `LIVE-GAP-009` / Product authority if cancellation included → Events JIT → executable proof.
- **Pass-M evidence limit survived:** PASS. No absence-of-documentation claim was upgraded to impossibility and OQ-020 remains open.

## 4. Compact key-term/route coverage

All required governed identifiers/routes were mechanically searched across Contract + Delta/Gap Register + Evidence Index + Compression Audit.

- **Missing required terms:** NONE
- **Result:** PASS.

Checked terms: `LIVE-UPD-001...006`, `LIVE-GAP-001...014`, `LIVE-EV-001...006`, OQ-014, OQ-017, OQ-020, OQ-021, OQ-022, OQ-029, OQ-030, OQ-031, OQ-032, OQ-036, DEC-190, FP-007.

## 5. Semantic-distinction verification

Compact Contract explicitly preserves: occurrence/provider identity separation; registration/access/attendance separation; recording intent/capture/adoption/publication separation; notice/permission separation; role/capture-scope separation; purpose withdrawal; retention vs publication; deletion request/ack/completion distinction; replay correction classes; promotional derivative separation; communications non-authority; owner-mediated recovery; provider documentation evidence limits.

**Result:** PASS — these distinctions are present in the compact Contract and routed unresolved questions remain in the Delta/Gap Register.

## 6. Historical relocation verification contract

The final repository compression commit must relocate every pre-compression Live/Replay discovery/register file under `deep/archive/` using the **same Git blob SHA**. Equality of source and archive Git blob SHA is an exact repository-byte identity proof; byte counts must also match. The accepted v0.12.1 status successor is retained under `deep/`.

The local cumulative v0.12.0 review copy is preserved exactly under `deep/archive/`; v0.12.1 becomes the canonical deep cumulative source.

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
| promo clips | Contract | PRESERVED |
| communications | Contract + GAP-006 | PRESERVED |
| cross-domain recovery | Contract | PRESERVED |
| provider facts | Evidence Index | PRESERVED |
| PT-001...154 | Evidence Index/deep source | COMPLETE |
| UPD-001...006 | Delta Register | COMPLETE |
| GAP-001...014 | Delta Register | COMPLETE |
| EV-001...006 | Evidence Index | COMPLETE |
| historical files | deep/archive | BYTE-PRESERVATION REQUIRED / VERIFIED IN FINAL TREE |

## 8. Verification outcome

**Result before repository-tree relocation:** `PASS / COMPACT CONTENT CONSISTENT WITH CANONICAL DEEP SOURCE`.

Final completion additionally requires post-commit tree/path/blob verification, valid manifest JSON, hash/byte verification and a fresh main↔branch comparison.
