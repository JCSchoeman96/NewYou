# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.7.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 7 ONLY — EXACT ROADMAP v1.3.0 CANDIDATE ASSEMBLY / PROMOTION-INTEGRITY GATE
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked for this pass:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-pass branch head:** `676391fe1a643365201712fe1787986d0a3f65ff`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.6.0.md` — preserved unchanged.
- **Accepted predecessor result:** Pass 6 / `ANL-PT-019`–`ANL-PT-021` accepted by human review.
- **Purpose:** assemble and independently review the exact Roadmap v1.3.0 candidate from the current live v1.2.0 predecessor plus only the accepted nine-location `ANL-UPD-001` patch, preserve the predecessor exactly, and fail closed if current-authority routing cannot be integrity-pinned.
- **Scope:** Roadmap candidate bytes, archive predecessor preservation, exact semantic diff review, and promotion-collateral integrity only. No PR, merge, current-authority promotion, Feature Pack/JIT work, metric contract, privacy design, provider choice or implementation.

---

## 1. Pass discipline

Pass 7 was authorised to perform one bounded promotion-preparation step:

1. recheck live `main` and the Analytics branch;
2. lock current Roadmap, README, manifest and Open Work inputs;
3. assemble exact Roadmap v1.3.0 candidate bytes from the current Roadmap v1.2.0 source;
4. preserve the exact v1.2.0 predecessor in archive;
5. independently inspect the exact semantic diff;
6. prepare matching README / manifest / Open Work routing collateral;
7. stop before PR/merge/current-authority promotion if any integrity requirement cannot be proven.

The pass does **not** authorise implementation or any later Analytics Pre-JIT topic.

---

## 2. Baseline and exact source locks

### 2.1 Live repository baseline

```text
main: 086ade7b28c000de1c387acb9760e5eb08bb0413
pre-pass analytics branch: 676391fe1a643365201712fe1787986d0a3f65ff
```

No live-main drift was detected.

### 2.2 Exact Roadmap predecessor

```text
path: docs/00_platform/05_ROADMAP_v1.2.0.md
git blob SHA: 5432991071d4d1a7cbd9dc4c8fca48c823129f40
manifest SHA-256: 601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0
```

This is the same exact-current source lock accepted in Pass 6.

### 2.3 Current routing inputs before candidate assembly

```text
README Roadmap route: 05_ROADMAP_v1.2.0.md
README Open Work route: 02_OPEN_WORK_v1.2.59.md
manifest ROADMAP: 1.2.0 / current
manifest OPEN_WORK: 1.2.59 / current
```

Current Open Work v1.2.59 continues to keep Communications finalisation blocked, conditional FP-001 dossiers pending explicit adjudication, Phase 7C blocked/not started, proof classification not finalised and executable development unauthorised. Analytics remains NOT REQUIRED for the current FP-001 conditional-dossier programme. None of those current programme facts is changed by this pass.

---

## 3. Exact Roadmap v1.3.0 candidate

The exact candidate was assembled from the live v1.2.0 predecessor plus only the accepted nine-location Pass-6 patch contract.

```text
candidate path: docs/00_platform/05_ROADMAP_v1.3.0.md
candidate git blob: ddff1c2fa34b3b9185bef8eb72e49f8513479887
candidate commit: 25cef5c3eb6462292cb5c34fff2e4c59d3be2078
candidate commit message: docs: assemble analytics Roadmap v1.3.0 candidate
```

The same commit preserves the predecessor at:

```text
docs/00_platform/archive/05_ROADMAP_v1.2.0.md
blob: 5432991071d4d1a7cbd9dc4c8fca48c823129f40
```

GitHub comparison recognises the predecessor move as zero-addition / zero-deletion rename evidence. The archived predecessor therefore reuses the exact current v1.2.0 blob rather than reconstructed text.

The branch moved only to the candidate commit. `main` was not modified and no PR was opened.

---

## 4. Pass-7 pressure-test register

### ANL-PT-022 — exact candidate versus accepted nine-location patch

**Question:** Does exact candidate blob `ddff1c2fa34b3b9185bef8eb72e49f8513479887` contain only the accepted `ANL-UPD-001` semantic amendment plus successor lifecycle metadata, without unrelated Roadmap drift?

**Verification route:** an unreferenced verification commit was created solely to force an old-path → candidate-blob semantic diff:

```text
verification commit: f462c15fe0f2db1859533120f5dee9b1884ee8ea
parent: 676391fe1a643365201712fe1787986d0a3f65ff
branch ref moved to it: NO
purpose: diff evidence only
```

The forced same-path diff shows exactly the accepted nine logical locations:

1. v1.3.0 successor header / predecessor / SemVer / date and new amendment-scope section;
2. §2 Research & Feedback mature-capability row;
3. §3.3 Domain/Feature-Pack decision row;
4. §3A bounded activation, Research row and no-auto-OQ/JIT clarification;
5. FP-005 feedback-classification guardrail consistency repair;
6. FP-006 Affected Domains adds Research & Feedback;
7. FP-006 bounded activation paragraph;
8. FP-006 broader-Research deferral;
9. FP-017 non-ownership / bounded-exception consistency repair.

No Product-Law wording, Decision Register meaning, Domain ownership law, Architecture mechanism, Feature Pack identifier, dependency graph, Voting activation, FP-016 sequencing, provider/schema choice or implementation semantics were changed.

**Disposition:** `PASS`.

**Working lock:** Roadmap candidate blob `ddff1c2fa34b3b9185bef8eb72e49f8513479887` is the exact Pass-7 semantic candidate for `ANL-UPD-001`. Any later byte change requires a new exact-candidate review and invalidates this lock.

---

### ANL-PT-023 — can current authority routing be promoted without a real candidate SHA-256?

**Question:** May README / manifest / Open Work be changed to route Roadmap v1.3.0 when the candidate git blob is known but its manifest-required SHA-256 has not been independently computed from exact bytes?

**Analysis:** No. The authority manifest is an integrity control, not a decorative index. Its current Roadmap record pins SHA-256 and `provenance_sha256`; historical Roadmap entries follow the same convention. Git's blob SHA-1 is not interchangeable with the manifest SHA-256. Guessing, omitting, substituting or placeholder-routing the digest would weaken the repository's current integrity contract.

The available GitHub connector proves the candidate git blob and exact content but exposes no repository-file download/materialisation action and no SHA-256 field. The local execution environment cannot resolve GitHub directly. The existing Foundation Integrity workflow has an exact-head `workflow_dispatch` path, but the available GitHub connector does not expose an action to start a new dispatch run. No real SHA-256 is therefore claimed in this pass.

**Disposition:** `CONFLICT` for **promotion/routing now**; this is not a semantic Roadmap conflict.

**Required resolution:** obtain byte-local access to the exact `ddff1c2...` candidate through an approved repository-native/local route, compute SHA-256, assemble the manifest/Open Work/README successor collateral using that exact pin, and rerun Foundation Integrity plus exact-head review.

**Anti-shortcut lock:** do not fabricate or infer the digest; do not substitute SHA-1; do not route a placeholder hash as current authority.

---

## 5. Promotion-collateral contract established in Pass 7

The exact intended collateral is recorded separately in:

`NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_ROADMAP_PROMOTION_COLLATERAL_WORKING_v0.1.0.md`.

It specifies, but does not currently route:

- README Roadmap route `v1.2.0 → v1.3.0`;
- manifest current `ROADMAP` record `v1.2.0 → v1.3.0` with exact candidate SHA-256 still required;
- manifest historical registration of archived Roadmap v1.2.0 using known SHA-256 `601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0`;
- Open Work successor shape `v1.2.59 → v1.2.60` only if frozen at the same promotion boundary;
- exact Open Work v1.2.59 predecessor preservation;
- no FP-001, Phase 7C, proof-classification or implementation advancement;
- Delivery Atlas reconciliation only after successful authority promotion as derived/non-authoritative follow-up.

---

## 6. ANL-UPD-001 state after Pass 7

```text
SEMANTIC INTENT: WORKING_LOCKED
NINE-LOCATION PATCH CONTRACT: ACCEPTED / WORKING_LOCKED
EXACT ROADMAP v1.3.0 CANDIDATE: ASSEMBLED / SEMANTIC DIFF PASS
EXACT CANDIDATE GIT BLOB: ddff1c2fa34b3b9185bef8eb72e49f8513479887
ARCHIVED v1.2.0 PREDECESSOR BLOB: EXACT / 5432991071d4d1a7cbd9dc4c8fca48c823129f40
CANDIDATE SHA-256: NOT YET PROVEN
CURRENT README/MANIFEST/OPEN WORK ROUTING: UNCHANGED
CURRENT ROADMAP AUTHORITY: STILL 05_ROADMAP_v1.2.0.md ON main
ANL-GAP-001: UPSTREAM_ACTION_REQUIRED UNTIL GOVERNED PROMOTION COMPLETES
FP-006 SURVEY JIT/IMPLEMENTATION: BLOCKED AT ROADMAP AUTHORITY
```

The branch contains an authority **candidate**, not a promoted current authority. Current repository authority remains whatever live `main` routes.

---

## 7. Pass 7 disposition

**BLOCKED / STOP — EXACT ROADMAP CANDIDATE PASSES; CURRENT-AUTHORITY PROMOTION PACKAGE CANNOT YET PASS THE MANIFEST INTEGRITY GATE.**

This is a narrower result than a semantic failure:

- `ANL-UPD-001` wording/ownership/scope candidate: **PASS**;
- exact v1.2.0 archive preservation: **PASS**;
- exact candidate semantic diff: **PASS**;
- current-authority routing/promotion: **BLOCKED** until the exact candidate SHA-256 is independently computed and the complete promotion collateral passes repository integrity review.

No README, manifest or Open Work current-authority route is changed in this pass. No PR is opened. No merge occurs. No implementation or later Analytics Pre-JIT topic is authorised.

**Next focused step after human acceptance:** resolve only the byte-local SHA-256 / promotion-integrity blocker for the already-reviewed blob `ddff1c2...`, assemble the exact routing/status successor package, run Foundation Integrity/exact-head review, and stop again before PR/merge unless explicitly authorised.