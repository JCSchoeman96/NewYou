# NewYou Commerce / Entitlements / Recurring Membership Compression Audit — Working v0.2.1

- **Status:** COMPLETE / NON-AUTHORITATIVE COMPRESSION AUDIT
- **Outcome:** **PASS**
- **Date:** 2026-09-10
- **Supersedes:** compression audit `v0.2.0`
- **Detailed source:** `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.3.md`
- **Detailed source SHA-256:** `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`
- **Semantic stabilisation audit:** `v0.2.0` — `05d6ac9cac911be98e69c9fd16c2465e04334e7d8dc5af8d983d0d6bcddeb9f7`
- **Mechanical recertification:** `v0.2.2` — `8c9e00ab3fb74b8739d1180cfe4b3ef9beb201d4b3c2f38bdb5509daea944af6`
- **Compact pack:** `v0.2.1`
- **Implementation:** NOT AUTHORISED

# 1. Scope

This is a provenance/SHA reissue audit. It does not recompress CER semantics from scratch.

The compact core was derived from the previously verified v0.2.0 bytes using only allowed provenance substitutions:
- deep source `v0.30.2` → `v0.30.3`;
- deep SHA update;
- mechanical recertification `v0.2.1` → `v0.2.2`;
- compact artifact `v0.2.0` → `v0.2.1` names/headings;
- supersession metadata reflecting the provenance PATCH.

# 2. Semantic-body equivalence proof

| Core file | v0.2.0 semantic content → v0.2.1 | Result |
|---|---|---|
| README | exact deterministic allowed-provenance transform only | PASS |
| Contract | exact deterministic allowed-provenance transform only | PASS |
| Delta Register | exact deterministic allowed-provenance transform only | PASS |
| Evidence Index | exact deterministic allowed-provenance transform only | PASS |

Additional exact checks:
- 20-row PT register unchanged and byte-for-byte equal to current deep source: **PASS**
- all thirteen accepted CER-UPD policy bodies unchanged: **PASS**
- no PT/UPD semantic text was regenerated or paraphrased: **PASS**

# 3. Current source/certification chain

`v0.30.1`
→ semantic stabilisation audit `v0.2.0` PASS
→ `v0.30.2` four-reference hygiene PATCH
→ mechanical recertification `v0.2.1`
→ `v0.30.3` current-routing/protocol hygiene PATCH
→ mechanical recertification `v0.2.2` PASS
→ compact provenance reissue `v0.2.1`

# 4. Structural preservation

| Check | Result |
|---|---|
| Deep SHA is exact mechanically recertified `v0.30.3` | PASS |
| Exact 20-row PT register in Contract | PASS |
| Exact 20-row PT register in Evidence Index | PASS |
| `CER-PT-001...020` preserved | PASS |
| `CER-UPD-001...013` preserved | PASS |
| All 13 accepted-policy-direction bodies preserved exactly | PASS |
| No `CER-PT-021` created | PASS |
| No `CER-UPD-014` created | PASS |
| NewYou/Store baselines unchanged | PASS |
| `OQ-004` preserved | PASS |
| HSP/Privacy seam ownership preserved | PASS |
| Implementation remains NOT AUTHORISED | PASS |

# 5. Compression characteristic

- Deep `v0.30.3`: `338814` bytes
- Compact core v0.2.1: `67294` bytes
- Compact/deep ratio: `0.199`

# 6. Core hashes

- `README.md`: `8f7e2f79e375e0c8a5f2ad11840563c803c9066d6e3ffc97d36fd002100fa1e5`
- `NEWYOU_CER_PREJIT_CONTRACT_WORKING_v0.2.1.md`: `e825d5beeb98d4a46bd863840f21b54bfa89fd026d8beecf8c4db007a3cdf193`
- `NEWYOU_CER_UPSTREAM_DELTA_REGISTER_WORKING_v0.2.1.md`: `eff45924cfd8d7c95c0d7cd727bc0a21c178ffa304de125d0cc23c53a250eea8`
- `NEWYOU_CER_EVIDENCE_INDEX_WORKING_v0.2.1.md`: `774009f9922d8be7f80b9ddb560154d90e6913ba304b50eaa90b39398de4d217`

# 7. Outcome

> **PASS**

Compact v0.2.1 preserves the already-verified CER semantic bodies and updates only provenance/certification metadata required by exact source `v0.30.3`.
