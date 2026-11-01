# NewYou Content & Media Source ↔ Compact Verification — Working v0.1.0

- **Status:** COMPLETE / NON-AUTHORITATIVE VERIFICATION
- **Outcome:** **PASS — PARK BROAD C&M / BEACON REUSE DISCOVERY**
- **Date:** 2026-09-21
- **Source:** `BEACON_REUSE_GRILL_AND_EXTRACTION_WORKING_v0.42.1.md`
- **Source SHA-256:** `08823adec046ae7222aff83725ded76a0bed68f629a1b7466a18acdc8efc4291`
- **Compact pack:** `NEWYOU_CM_PREJIT_PACK_v0.1.0`
- **Compression audit:** `NEWYOU_CM_COMPRESSION_AUDIT_WORKING_v0.1.0.md`
- **Repository mutation:** NONE

## 1. Exact source certification chain

```text
v0.42.0 deep source
→ whole-source stabilisation audit v0.1.0
→ PASS WITH NON-BLOCKING CORRECTIONS
→ v0.42.1 consistency PATCH
→ mechanical recertification v0.1.1 PASS
→ compact pack v0.1.0
→ compression audit v0.1.0 PASS
→ this source↔compact verification
```

No compact semantic clause was derived from an unrecertified source revision.

## 2. Accepted-decision coverage

Automated checks against the Evidence Index:

- `GRILL-01...GRILL-41` all have an explicit trace row: **PASS (41/41)**;
- no `GRILL-42` is introduced: **PASS**;
- branch closures GRILL-19 / 30 / 38 / 41 are preserved: **PASS**;
- GRILL-36/37 media refinements are represented as controlling latest meaning: **PASS**;
- GRILL-40 route refinement is represented as controlling latest meaning: **PASS**.

## 3. Open-delta coverage

- `CM-UPD-001...CM-UPD-013` all exist in the Delta Register: **PASS (13/13)**;
- all 13 appear in the Evidence Index open-gate trace: **PASS**;
- governed OQs retained: **PASS** for `OQ-013`, `014`, `015`, `016`, `020`, `021`, `024`, `029`, `030`, `031`, `032`;
- historical-address expiry/unrelated reuse remains open: **PASS**;
- correction-impact/remediation detail remains open: **PASS**;
- source-copy/IP/provenance review remains open: **PASS**;
- FP-001 conditional C&M dossier adjudication remains governed downstream: **PASS**.

## 4. Authority boundary checks

- C&M remains content/media/public-address authority inside its scope: **PASS**.
- Phoenix/application remains routing mechanism/namespace authority: **PASS**.
- Entitlements/I&A remain access authority: **PASS**.
- Privacy remains consent/deletion-orchestration authority: **PASS**.
- Experimentation remains experiment authority: **PASS**.
- provider/object-store state is not business authority: **PASS**.
- ETS/cache/search/sitemap/generated routes/reverse indexes/workers remain derived: **PASS**.
- no new SEO/Route/Sitemap/MediaBlob/Workflow Domain is introduced: **PASS**.

## 5. Donor/reuse boundary checks

- Beacon CMS baseline pinned to stable `v0.5.1`: **PASS**.
- Beacon LiveAdmin baseline pinned to stable `v0.4.3`: **PASS**.
- donor paths for content/composition, routing and media preserved in Evidence Index: **PASS**.
- mutable Beacon Page / PageEvent / PageSnapshot are not adopted as NewYou authority: **PASS**.
- broad catch-all CMS routing and ETS RouterServer correctness are rejected: **PASS**.
- PageVariant is not experimentation authority: **PASS**.
- arbitrary stored executable HEEx/helpers/JS/CSS remain rejected: **PASS**.
- LiveAdmin is not adopted as a second operator application: **PASS**.
- no direct source copy is authorised by the compact pack: **PASS**.

## 6. Current semantic model checks

The compact Contract explicitly preserves:

- code-authoritative block contracts and schema evolution;
- subordinate version-owned block occurrences;
- bounded slots/pattern copy-on-instantiation semantics;
- dedicated Template identity/version semantics and safe migration;
- mutable ContentDraft versus immutable ContentVersion;
- shared ContentVersion + independent locale version lineages;
- exact translation provenance/staleness and no Approval carry-forward;
- separate Review/Approval/Publication truth;
- version-addressable Content Type contracts;
- exact Publication/schedule target and activation revalidation;
- Correction/Withdrawal/supersession separation;
- stable MediaAsset + immutable MediaAssetVersion;
- durable ingest intent + verified idempotent finalisation;
- rights/protected delivery/withdrawal/deletion/reference semantics;
- exact public Publication route claims/history;
- atomic Publication + route claim/history transition;
- normalised route uniqueness and schedule non-reservation;
- loop-free slug reversion and protected historical aliases;
- discovery/search/sitemap/cache/router projections as rebuildable non-authority.

**Result: PASS.**

## 7. Core file hashes

- `README.md`: `dd9dc18e6c21039e176b5b2bc16a3fa599570a9af397c6a9ec82bdd550a3c2da`
- `NEWYOU_CM_PREJIT_CONTRACT_WORKING_v0.1.0.md`: `af1e85529194f554c421431d651fb04790549ab86285347876d56483660bb387`
- `NEWYOU_CM_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.0.md`: `e9aa244a7e68fea98db79f62ab5e48851c6e3ce92404b35d099ce239f18f5dcd`
- `NEWYOU_CM_EVIDENCE_INDEX_WORKING_v0.1.0.md`: `345bbedc9e08785f7d3a14435d7d87c5dc9d76c144734b6da8dfd46129b1ca31`
- `NEWYOU_CM_COMPRESSION_AUDIT_WORKING_v0.1.0.md`: `0131a08c935e12aa6a1c245d695ab160eab84fb95fb030699e41e2e62f9b9aa2`
- `NEWYOU_CM_PREJIT_STABILISATION_AUDIT_WORKING_v0.1.0.md`: `afdd3c1b76bc92fefef2d8c32bebda17a55d7e98a54b0c55278ae3c84b024269`
- `NEWYOU_CM_PREJIT_STABILISATION_MECHANICAL_RECERTIFICATION_v0.1.1.md`: `8c55614946ffa57baba0c880692e4c96c8b113f207e6e9a8ef778f1f5ed63cac`

## 8. Final certification

> **PASS — PARK BROAD C&M / BEACON REUSE DISCOVERY**

Normal future C&M planning should use the compact pack first and consult the archived deep source only for exact pressure-test/donor/provenance questions.

The next legitimate step is governed Feature Pack/JIT work when current sequencing permits it—not another broad Beacon comparison round and not implementation from this pack.
