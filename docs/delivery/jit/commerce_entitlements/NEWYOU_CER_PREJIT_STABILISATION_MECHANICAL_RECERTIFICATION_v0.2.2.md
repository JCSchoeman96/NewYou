# NewYou CER Pre-JIT — Mechanical Recertification

- **Recertification version:** `v0.2.2`
- **Date:** `2026-09-10`
- **Scope:** MECHANICAL / CURRENT-ROUTING / DOCUMENT-CONSISTENCY ONLY
- **Semantic audit carried forward from:** `NEWYOU_CER_PREJIT_STABILISATION_AUDIT_WORKING_v0.2.0.md`
- **Prior mechanical recertification:** `NEWYOU_CER_PREJIT_STABILISATION_MECHANICAL_RECERTIFICATION_v0.2.1.md`
- **Mechanically recertified deep source:** `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.3.md`
- **Deep-source SHA-256:** `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`
- **Repository mutation:** NONE

# 1. Outcome

> **MECHANICAL RECERTIFICATION: PASS**
>
> **EXACT `v0.30.3`: PASS — ELIGIBLE FOR FINAL COMPACT REISSUE**
>
> **SEMANTIC DISCOVERY: NOT REOPENED**
>
> **NO NEW PT / UPD / PROVIDER / STORE / CROSS-STREAM ANALYSIS PERFORMED**

# 2. Patch-boundary proof

`v0.30.3` changes only current header/protocol routing plus its new PATCH changelog entry.

The entire semantic body from:

`## 1. Scope`

through immediately before:

`# 13. Version history`

is byte-for-byte identical between `v0.30.2` and `v0.30.3`.

- `v0.30.2` SHA-256: `fedec212416d7cada7d3c67852df79830019bd44da8641a7dcb82e16a06407b6`
- `v0.30.3` SHA-256: `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`

Therefore the semantic conclusions of stabilisation audit `v0.2.0` and the prior four-reference mechanical recertification remain substantively unchanged; this recertification addresses only the new exact bytes and current-routing chain.

# 3. Current-routing checks

| Check | Result |
|---|---|
| Header records second-pass discovery COMPLETE | PASS |
| Header records renewed semantic audit `v0.2.0` already PASS on `v0.30.1` | PASS |
| Header records `v0.30.2` as four-reference hygiene PATCH | PASS |
| Header/protocol identify exact `v0.30.3` mechanical recertification as the current next certification step | PASS |
| Protocol calls deep source semantically stabilised, not awaiting semantic audit | PASS |
| Handoff step 1 points to exact `v0.30.3`, not `v0.30.1` | PASS |
| Stale “renewed semantic audit still next” current-state text absent | PASS |

# 4. Structural checks

| Check | Result |
|---|---|
| `CER-PT-001...020` headings preserved exactly | PASS |
| Current PT register `001...020` preserved | PASS |
| `CER-UPD-001...013` headings preserved exactly | PASS |
| No `CER-PT-021` heading | PASS |
| No `CER-UPD-014` heading | PASS |
| No merge-conflict markers | PASS |
| Semantic body unchanged from `v0.30.2` | PASS |

# 5. Certification boundary

This recertification does not repeat the semantic lifecycle audit, provider research, Store reuse analysis, Domain review or cross-stream analysis.

If the deep source changes after SHA:

`2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`

this exact-byte certification no longer applies.

# 6. Next CER step

`v0.30.3`
→ final compact metadata/SHA reissue with semantic bodies preserved
→ compression verification
→ source↔compact verification
→ `PASS — PARK CER`
→ HSP + Privacy + CER upstream-delta adjudication

No third broad pressure-test round is authorised.
