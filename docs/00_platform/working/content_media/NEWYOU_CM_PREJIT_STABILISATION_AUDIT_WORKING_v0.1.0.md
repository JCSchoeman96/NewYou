# NewYou Content & Media / Beacon Pre-JIT Stabilisation Audit — Working v0.1.0

- **Status:** COMPLETE / NON-AUTHORITATIVE STABILISATION AUDIT
- **Outcome:** **PASS WITH NON-BLOCKING CORRECTIONS**
- **Date:** 2026-09-21
- **Audited deep source:** `BEACON_REUSE_GRILL_AND_EXTRACTION_WORKING_v0.42.0.md`
- **Audited deep-source SHA-256:** `1b759a485c692bc60df2aa3a7935ece2a73f85a3e694c690615fa7a7a8ca84c0`
- **Corrected successor:** `BEACON_REUSE_GRILL_AND_EXTRACTION_WORKING_v0.42.1.md`
- **Corrected successor SHA-256:** `08823adec046ae7222aff83725ded76a0bed68f629a1b7466a18acdc8efc4291`
- **Implementation:** NOT AUTHORISED
- **Repository mutation:** NONE

## 1. Audit purpose

This audit determines whether the completed Beacon/Content & Media reuse-discovery dossier is semantically stable enough to become deep archived evidence and be compressed into a smaller pre-JIT working pack without reopening discovery.

It checks:

- current NewYou authority alignment;
- accepted-decision completeness and supersession;
- branch closure integrity;
- authority ownership and non-authority projections;
- lifecycle/concurrency/retry/recovery semantics;
- Beacon/LiveAdmin donor provenance and rejection boundaries;
- preservation of unresolved OQs and legal/privacy/vendor gates;
- FP-001 governance boundaries;
- stale historical/current-state wording;
- readiness for compact contract/evidence packaging.

The audit does **not** approve implementation, decide exact Ash Resources, or change any governed NewYou document.

## 2. Live authority baseline

Verified against `JCSchoeman96/NewYou` default branch at:

`be6b9ea4bdfc5a638a24affa20e6c75cd9fc321f`

Current routed authority:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.40.md`
5. `03_ARCHITECTURE_v1.1.0.md`
6. `04_DOMAIN_MAP_v1.1.0.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.0.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` where frontend/public publishing is in scope.

The live README continues to classify `working/` as non-authoritative derived planning and `archive/` as historical/deep evidence. Current Open Work still leaves the relevant Content & Media gates open, including `OQ-013`, `OQ-014`, `OQ-015`, `OQ-016`, `OQ-020`, `OQ-021`, `OQ-024`, and the privacy/deletion gates applicable to media.

## 3. External donor baseline

### Beacon CMS

Verified stable baseline:

- repository: `BeaconCMS/beacon`;
- stable tag: `v0.5.1`;
- annotated tag SHA: `565587625714465643888a64f62a62f553daab9e`;
- tagged commit SHA: `97024750c88d7ccce34e21e802d8936c8e83c573`;
- release date: 2025-04-01;
- Hex package stable CMS release: `beacon 0.5.1`;
- licence: MIT.

The stable tree still contains the donor mechanisms referenced by the dossier, including content components/slots, page/page event/page snapshot, lifecycle, router/router server/routes loader, media asset/provider/image processing and upload metadata. The correct S3 path is `lib/beacon/media_library/provider/s3.ex` with signed/unsigned support beneath that path.

### Beacon LiveAdmin

Verified stable baseline:

- repository: `BeaconCMS/beacon_live_admin`;
- stable/latest release: `v0.4.3`;
- release date: 2025-03-31;
- annotated tag SHA: `17ee8a75c2ebb461a4d6f6585d3078275b93a596`;
- licence: MIT.

Beacon/LiveAdmin remain pre-1.0 donor/reference evidence. No package adoption or runtime dependency is authorised by this audit.

## 4. Mechanical integrity audit

| Check | Result |
|---|---|
| Accepted GRILL sections | **41 / 41** |
| Accepted GRILL IDs contiguous | **PASS — GRILL-01...GRILL-41** |
| Accepted-decision register entries | **41 / 41** |
| Register IDs contiguous | **PASS** |
| SemVer progression includes every GRILL | **PASS** |
| Markdown code fences balanced | **PASS** |
| Active conclusion states Block 3A closed | **PASS** |
| Active conclusion states Block 4A closed | **PASS** |
| Active conclusion states Block 5A closed | **PASS** |
| Implementation remains unauthorised | **PASS** |

No missing, duplicate or out-of-order accepted GRILL was found.

## 5. Whole-source consistency findings

### 5.1 Finding CM-AUD-001 — stale GRILL-28 “next seam” wording

The GRILL-28-era scheduling section still stated unqualified that exact correction classification/reason/impact propagation “is the next seam”, although GRILL-29 later resolved the durable Correction/Withdrawal ownership boundary.

**Classification:** non-semantic historical wording defect.

**Correction:** v0.42.1 explicitly marks the statement historical and routes exact classification/impact mechanics to downstream JIT/policy detail.

### 5.2 Finding CM-AUD-002 — pre-GRILL-41 Block 5A state not consistently historical

Several pre-GRILL-41 passages still used current-tense wording such as Block 5A being OPEN or formal closure still pending. The final conclusion and GRILL-41 register were correct, but the earlier state was insufficiently qualified under the dossier's own mandatory consistency-sweep rule.

**Classification:** non-semantic historical/current-state wording defect.

**Correction:** v0.42.1 explicitly labels the GRILL-39 continuation state and GRILL-40 closure-audit state as historical.

### 5.3 Finding CM-AUD-003 — current grill-sequence table stopped at GRILL-39

The strategy sequence ended at Block 5A.1 / GRILL-39 and still said Block 5A OPEN. It omitted Block 5A.2 / GRILL-40 and Block 5A.3 / GRILL-41.

**Classification:** non-semantic sequence/index defect.

**Correction:** v0.42.1 extends the sequence through GRILL-41 and records Block 5A CLOSED / PASS.

### 5.4 No accepted decision text required semantic repair

The audit found no need to modify the accepted GRILL-01...41 decision bodies. The corrections are routing/history/index hygiene only.

## 6. Supersession/refinement audit

**PASS.** The controlling meanings are coherent when latest refinements are applied:

- GRILL-20 is refined by GRILL-21/24/25 for version-cut and locale-draft semantics.
- GRILL-22/23/24/25 establish shared-versus-locale truth and translation lineage without duplicating independent block trees.
- GRILL-26 keeps Review, Approval and readiness distinct.
- GRILL-27 resolves version-addressable Content Type contract compatibility.
- GRILL-28 fixes exact Publication/scheduling target and revalidation; it does not close OQ-016 operations.
- GRILL-29 distinguishes Correction, Withdrawal and supersession.
- GRILL-30 closes the content-governance branch.
- GRILL-36 narrowly supersedes GRILL-31's earlier no-version-hierarchy conclusion and refines exact-version references.
- GRILL-37 refines media deletion terminality and shared-byte semantics.
- GRILL-38 closes the media branch.
- GRILL-40 refines GRILL-39's transaction/exact-target/normalised-route/scheduling/reversion semantics.
- GRILL-41 closes the public-addressability/discovery-projection branch.

No superseded wording is required in the compact contract as current doctrine. Historical contradictions remain useful only in deep evidence.

## 7. Authority/ownership audit

**PASS.** The dossier remains consistent with current Domain and Architecture law:

- Content & Media owns content/media identity, immutable versions, locale branches, publication/correction/withdrawal, authoritative discovery metadata and governed media publication state.
- Phoenix/application code owns application routing mechanism/namespace; C&M owns only durable permitted public-content address claims.
- Identity/Access/Entitlements/Privacy/Safety retain their own access, consent and safety authorities.
- Experimentation remains experiment authority; Beacon `PageVariant` is not adopted as experiment authority.
- object-storage/provider state owns bytes/locators, not C&M business truth;
- workers, PubSub, ETS, caches, generated routes, sitemap, native-search indexes and external crawler state remain derived/non-authoritative;
- reverse media-usage indexes remain derived; consuming Domains own exact forward references.

No new Domain is justified by the dossier.

## 8. Resource/process over-design audit

**PASS.** The accepted semantics justify some conceptual Resources/aggregates but do not require one Resource per distinction.

The dossier correctly leaves exact Ash representation to JIT for:

- block envelope/value types;
- ContentDraft / ContentLocaleDraft / TranslationWork exact fields/actions;
- Review/Approval persistence shape;
- Publication/schedule intent/correction/withdrawal topology;
- media asset/version/reference/deletion accounting;
- route/address claim topology;
- caches/indexes/workers/queues.

No Redis/ETS/GenServer/service is introduced as correctness authority.

## 9. Lifecycle/concurrency/failure audit

**PASS.** The current working model covers the material failure classes discovered in this stream:

- exact draft revision → immutable version cut;
- single-active draft boundaries and explicit abandonment;
- reader-before-writer block schema evolution;
- translation staleness from exact source provenance;
- Review/Approval/Publication separation;
- schedule pins exact intent and revalidates current eligibility;
- duplicate/reordered async media work converges from durable accepted intent;
- provider/object-store completion is verified rather than inferred from worker success;
- media withdrawal is immediate authority removal while physical deletion is separate durable disposition;
- deletion is version/asset subject-aware and shared bytes cannot evade deletion law;
- route activation + canonical claim + required redirect/history update is one coherent PostgreSQL authoritative transition;
- schedule creation does not reserve routes;
- historical slug reversion must remain loop-free;
- stale caches/search/sitemap/router state cannot preserve access or publication authority.

Exact implementation mechanics remain JIT/proof work.

## 10. Beacon extraction/classification audit

**PASS.** The dossier remains adversarial rather than adoptive.

Current durable posture:

- **ADAPT / REIMPLEMENT** useful concepts: bounded block/component contracts, slots, mutable-vs-published separation, route/path uniqueness and URL generation concepts, media lineage/provider boundary, selected generic LiveAdmin table/editor UX mechanics.
- **REJECT as authority/runtime dependency:** Beacon Page as C&M authority, PageEvent lifecycle as NewYou lifecycle authority, serialised PageSnapshot as business version model, PageVariant as experiment authority, broad catch-all CMS routing, ETS/RouterServer correctness authority, executable stored HEEx/helpers/JS/CSS, generic multisite authority, LiveAdmin as a second operator application.
- **DEFER/JIT:** any narrow direct source reuse, Markdown support, exact admin component reuse and package-level choices.

The exact accepted NewYou semantics come from NewYou authority + pressure testing; Beacon remains donor/reference evidence.

## 11. Unresolved gate preservation audit

**PASS.** The dossier does not silently close the following downstream authority/proof work:

- `OQ-013` translation resource design — semantic boundaries are constrained by GRILL-22...27, but exact governed resource/index/approval implementation remains open;
- `OQ-014` edge/cache design;
- `OQ-015` native-search configuration;
- `OQ-016` publication scheduler reliability/retry/alerts/stale-approval/recovery;
- `OQ-020` live/video vendor validation;
- `OQ-021` recording/video consent and retention;
- `OQ-024` source-content/media inventory;
- `OQ-029` retention matrix where applicable;
- `OQ-030` external processor deletion inventory;
- `OQ-031` backup restore/deletion replay;
- `OQ-032` export/deletion operations;
- IP/licence/contributor-rights review for copied or migrated content/source;
- historical public-address obligation expiry / unrelated-content reuse policy;
- exact correction-impact/severity vocabulary and owner-specific remediation mechanics.

These must remain visible in the compact delta register.

## 12. FP-001 and development-entry audit

**PASS.** The dossier correctly does **not** change FP-001's governed Content & Media JIT dossier disposition.

The reuse evidence may later inform the required governed FP-001 reconciliation/JIT process, but this working artifact cannot flip `CONDITIONAL → YES`, change Feature Pack scope or authorise implementation.

Current Open Work sequencing remains controlling. Broad C&M reuse discovery being stable does not bypass HARDEN-02 / FP-001 reconciliation / Phase-8 entry gates.

## 13. Licence/source-copy audit

**PASS WITH PRESERVED OPEN POLICY.**

The deep source's direct-copy policy is explicitly “proposed, not yet approved”. Compression must not promote it into an accepted NewYou policy.

Current safe compact statement:

- no Beacon/LiveAdmin source copy is authorised by the pre-JIT pack;
- if later JIT work proposes copying or substantial derivation, it must pin exact repository/tag-or-commit/path/blob/licence and preserve required MIT notices/provenance;
- legal/IP/contributor-rights gates remain upstream/downstream as applicable;
- clean reimplementation remains preferred where it reduces lifetime coupling and provenance burden.

## 14. Compression readiness

### Outcome

**PASS WITH NON-BLOCKING CORRECTIONS → READY FOR COMPRESSION FROM v0.42.1**

The exact v0.42.0 source is semantically sound but contains the stale-state/index defects in §5. Those defects do not require a new GRILL or architecture decision.

The corrected v0.42.1 successor is the appropriate compression source after narrow mechanical recertification proves:

- all 41 accepted decision bodies are byte-for-byte unchanged;
- the accepted-decision register is unchanged;
- only historical/current-sequence/version-routing text changed;
- no OQ/deferred boundary was removed;
- implementation remains unauthorised.

After that recertification, the compact pack should become normal working context and v0.42.1 should be retained as deep archived provenance rather than loaded by default.

## 15. Recommended repository placement after compact verification

```text
docs/00_platform/archive/
└── BEACON_REUSE_GRILL_AND_EXTRACTION_WORKING_v0.42.1.md

docs/00_platform/working/content_media/
├── README.md
├── NEWYOU_CM_PREJIT_CONTRACT_WORKING_v0.1.0.md
├── NEWYOU_CM_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.0.md
├── NEWYOU_CM_EVIDENCE_INDEX_WORKING_v0.1.0.md
├── NEWYOU_CM_PREJIT_STABILISATION_AUDIT_WORKING_v0.1.0.md
├── NEWYOU_CM_PREJIT_STABILISATION_MECHANICAL_RECERTIFICATION_v0.1.1.md
├── NEWYOU_CM_COMPRESSION_AUDIT_WORKING_v0.1.0.md
├── NEWYOU_CM_SOURCE_COMPACT_VERIFICATION_WORKING_v0.1.0.md
└── PACK_MANIFEST_v0.1.0.json
```

This is packaging only. It does not create a new authority layer.
