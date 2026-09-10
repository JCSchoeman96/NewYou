# NewYou CER Source ↔ Compact Verification — Working v0.2.1

- **Status:** COMPLETE / NON-AUTHORITATIVE VERIFICATION
- **Outcome:** **PASS — PARK CER**
- **Date:** 2026-09-10
- **Supersedes:** source↔compact verification `v0.2.0`
- **Source:** `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.3.md`
- **Source SHA-256:** `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`
- **Mechanical recertification:** `v0.2.2` — `8c9e00ab3fb74b8739d1180cfe4b3ef9beb201d4b3c2f38bdb5509daea944af6`
- **Compact pack:** `NEWYOU_CER_FINAL_COMPACT_PACK_v0.2.1`
- **Compression audit:** `NEWYOU_CER_COMPRESSION_AUDIT_WORKING_v0.2.1.md` — `9cf60d1fa0348eb7a8d44cb987a9f58516ef2475c3d2087ef93f177b6d73b8ca`
- **Repository mutation:** NONE

# 1. Exact source checks

- Exact current 20-row PT register present in Contract: **PASS**
- Exact current 20-row PT register present in Evidence Index: **PASS**
- PT set `CER-PT-001...020`: **PASS**
- UPD set `CER-UPD-001...013`: **PASS**
- Each accepted-policy-direction body from deep UPD-001...013 appears exactly in Delta Register: **PASS**
- No `CER-PT-021` or `CER-UPD-014` created: **PASS**

# 2. Provenance-PATCH equivalence

The four compact semantic core files were not semantically recompressed.

Each v0.2.1 file equals the prior verified v0.2.0 bytes after only the explicitly allowed source-version/SHA/certification/artifact-version/supersession substitutions.

- README: **PASS**
- Contract: **PASS**
- Delta Register: **PASS**
- Evidence Index: **PASS**

Therefore the semantic bodies previously verified at v0.2.0 remain unchanged.

# 3. README completeness

The package contains its actual final `README.md`.

A standalone inspection snapshot is byte-for-byte identical to that packaged README: **PASS**.

Packaged README SHA-256:

`8f7e2f79e375e0c8a5f2ad11840563c803c9066d6e3ffc97d36fd002100fa1e5`

# 4. Boundary preservation

- Commerce / Entitlements / I&A ownership: **PASS**
- Provider/cache/queue/UI non-authority: **PASS**
- `OQ-004` remains open: **PASS**
- HSP-owned seams remain HSP-owned: **PASS**
- Privacy deletion/retention seam remains Privacy-owned: **PASS**
- Store remains reuse evidence, not NewYou authority: **PASS**
- NewYou-specific Premium benefit policy remains outside generic Store: **PASS**
- Implementation remains unauthorised: **PASS**

# 5. Live baseline recheck

At final reissue review:
- NewYou `main` remains `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`;
- Store `hardening/subscriptions` remains `54871ef3bdda42f067ed5dbd398305151610c060`.

No authority/runtime-head movement requires CER reopening.

# 6. Final certification

> **PASS — PARK CER**

Broad CER discovery remains closed at `CER-PT-020`.

The exact deep source `v0.30.3`, mechanical recertification `v0.2.2`, compact pack `v0.2.1`, compression audit `v0.2.1` and this source↔compact verification form the final current certification chain.

Next programme:

`HSP + Privacy + CER`
→ cross-stream upstream-delta adjudication
→ smallest coherent governed Product amendments
→ downstream impact cascade only where required.

This verification does not authorise repository mutation or implementation.
