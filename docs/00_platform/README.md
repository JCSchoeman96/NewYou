# NewYou Platform Documentation

This directory separates current platform authority from deep evidence and historical planning material. The separation is for agent-context hygiene only; it does not change Product Law, Architecture Law, Domain Law, Roadmap meaning or ownership.

## Default Agent Context

For foundation/default planning and delivery-preparation work, read **only** these current-authority documents first:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.57.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`

For frontend, UI, public-experience, design-system, accessibility, SEO, analytics-UI or Feature Pack planning, additionally load:

9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md`

Do not automatically read files under `reference/` or `archive/`.

Routine Phase 7 work should use the README, current Roadmap, current Open Work, the relevant Feature Pack section, frozen Architecture, relevant Domain Map sections and specific Product/Decision references. Consult deep evidence only when a real question requires exact source tracing.

## Current Authority

The nine documents listed above describe the current platform state. Their explicit versioned filenames are intentional and should not be replaced with unversioned aliases without a separate governance decision.

The README and manifest are the current routing pointers. Frozen artifacts may retain source-at-freeze filenames as historical provenance; those references do not override the current routing above.

The frozen Frontend Experience System is current authority for affected frontend-experience planning, but it is conditionally loaded rather than default context for unrelated routine work.

## Active Working Artifacts

`working/` contains active, derived planning artifacts. These files are not current authority, deep-reference evidence or historical archive, and they are outside the manifest's governing/reference document records. The manifest may list a derived path under graph rules for integrity scanning without elevating it to authority. Read working artifacts only when a task explicitly concerns them; they must not override the nine current-authority documents. They remain working until an explicit freeze review and governance decision.

- `working/EXPERIENCE_DECISIONS_WORKING_v0.7.0.md` — cumulative experience decision register; remains working/non-authoritative provenance.
- `working/DELIVERY_ATLAS_WORKING_v0.3.9.md` — derived Delivery Atlas navigation with current-source routing for approved Feature Pack planning. It remains working/non-authoritative, outside authority-document records, and is listed only under graph/navigation paths. Its active Open Work route is v1.2.57; direct predecessor v0.3.8 is preserved byte-identically at `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md`. The unchanged v0.2.1 working path remains available to existing FP-001 and HARDEN-02 source-at-freeze references.
- `working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md` — preserves certified HARDEN-02 execution evidence and records Engineering Standards Authority Promotion, FP-001 PMR reconciliation and Identity v0.1.4 promotion COMPLETE / CERTIFIED. NEXT is `COMMUNICATIONS JIT DOMAIN DOSSIER`, which remains REQUIRED / NEXT / NOT_STARTED; Communications finalisation remains BLOCKED / STOP. Later gates remain downstream or blocked. Predecessor v0.5.0 is preserved byte-identically at `archive/HARDEN-02_CONTRACT_WORKING_v0.5.0.md`.
- `working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md` — certified/current FP-001 skeleton status successor. PR #67 PMR reconciliation is COMPLETE / CERTIFIED; the normative PMR block is unchanged and representation remains unfrozen under `ARQ-IAM-013`. NEXT is `COMMUNICATIONS JIT DOMAIN DOSSIER`; Communications remains NOT_STARTED, and all later gates remain blocked or downstream. The v0.1.2 candidate is preserved byte-identically at `archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md`; v0.1.1 remains preserved at its archive path.
- `working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md` — certified/current Identity dossier. It preserves the PR #67 PMR and PR #70 J.1 durable-delivery corrections and records PR #76 certification of COMM-UPD-001 and COMM-UPD-002. It selects no provider/package/storage representation/retry policy/OQ-036 option and does not authorise Phase 7C, proof classification or implementation. The exact PR #70 candidate, superseded promoted/current v0.1.3 snapshot and PR #76 candidate are separately preserved in archive.
- archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md — exact PR #76 candidate bytes, byte-identically preserved; current dossier is at working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md.
- `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md` — non-authoritative Stage 3B classification; it does not amend Product Law, AR-000, Architecture Law or Engineering Standards and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage 4A Architecture Grill evidence; it does not amend Product Law, AR-000 or Architecture Law, creates no ARC identifiers, and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage 4B Engineering-Policy Grill evidence; it does not amend Product Law, AR-000 or Architecture Law, does not create Engineering Standards, does not install dependencies, and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md` — non-authoritative targeted Domain pressure-test evidence; it does not itself create Domain Law. Domain Law is created only by the versioned Domain Map successor.
- `working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage Roadmap Sequencing Grill evidence; it does not itself create Roadmap Law. Roadmap Law is created only by the versioned Roadmap successor.


PR #70 closed the Identity/Communications durable-delivery contradiction and merged its certified v0.1.3 candidate unchanged. Exact-head CI run 37198148095 and resulting-main CI run 37205571249 each passed with 287 tests, 535 Foundation Integrity assertions and zero findings. Fresh independent exact-head and post-merge reviews passed. Candidate head `613ea1d52f6ffdadb3910cee3c62ea5dbd88f583` and resulting main `df6190a06bdc8aa4b99f6ed3a18cb9e3e12e22fb` have identical tree `421b9c1670586699e12807bc28f01179ca755fa7`, with zero changed files between them. The exact candidate remains at `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md` as certification evidence.

PR #76 candidate certification and completed post-merge certification evidence are COMPLETE / CERTIFIED. PR #76 did not make v0.1.4 current: resulting main kept v0.1.3 current and v0.1.4 under `working/candidates/`. The separate PR #77 status successor records Identity v0.1.4 as CERTIFIED / CURRENT. PR #76 exact-head and resulting-main runs 37419452502 and 37425057900 passed with 291 tests, 541 assertions and zero findings; attestations and reviewer attribution are preserved in Open Work v1.2.57 and the dossier. The PR #76 candidate, PR #70 candidate and prior promoted/current v0.1.3 snapshot are distinct archive artifacts. Communications remains REQUIRED / NEXT / NOT_STARTED; finalisation remains BLOCKED / STOP pending its own dossier and applicable gates. Phase 7C remains blocked, proof classification is not finalised, and Phase 8/application implementation remain unauthorised.


## Delivery Atlas routing

Use the [Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.3.9.md) during delivery preparation when its derived navigation helps with an approved Roadmap Feature Pack or a relevant planning question. Consulting the Atlas is not itself a gate or prerequisite. It does not override the nine current-authority documents above, change Product/Architecture/Domain/Roadmap law, authorise Phase 7 or authorise implementation.

Do not load the whole Atlas by default. Load only the relevant sections: the Feature Pack and capability views in §§4–5, active-FP derivation contracts in §§6–12, and the routing/governance rules in §§23–25 as needed. Every material Atlas conclusion must resolve to an exact current upstream authority reference. The Atlas may point to the canonical Phase 7A Feature Pack Skeleton + preliminary Gate Manifest → Phase 7B required JIT Domain Dossiers → Phase 7C Final Feature Pack Contract sequence when relevant; that navigation adds no gate or artifact, and the Atlas creates none of those artifacts.

## Machine-readable inventory

`CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` is the machine-readable inventory of current authority and deep-reference evidence. It records canonical paths, SemVer, authority class, SHA-256 and superseded-version metadata; it does not create a new authority layer.

## Reference Documents

Use `reference/` only when the current authority requires exact evidence or identifier-level reasoning:

- `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` — current cumulative ARQ source tracing and Stage 3A.2 amendment.
- `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` — exact ARC legislative reasoning, including the Architecture-amendment successor.
- `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md` — detailed FLOW evidence and the seven targeted Architecture-amendment reviews.

These documents are valuable evidence, but they are not default context for routine planning or delivery preparation.

## Certified Engineering Standards supporting authority

`reference/ENGINEERING_STANDARDS_v1.0.1.md` is the current certified Engineering Standards supporting authority. It remains registered in `reference_documents`, not `governing_documents`. Its sole normative source is the accepted Stage 4B Engineering-Policy Grill at `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md`; the Grill remains working/non-authoritative provenance. The Stage 4A Architecture Grill remains constraint context.

The promotion is COMPLETE / CERTIFIED. The exact PR #65 candidate bytes remain at `archive/ENGINEERING_STANDARDS_v1.0.0.md`; v1.0.1 preserves the EP-Q1…EP-Q5 normative body and binds the candidate, merge, tree, CI, attestations and fresh post-merge PASS review. Current programme status is in Open Work v1.2.57. PR #67 PMR reconciliation is COMPLETE / CERTIFIED. PR #76 candidate certification and post-merge certification evidence are COMPLETE / CERTIFIED; current Identity status is recorded by the separate PR #77 status successor. NEXT is `COMMUNICATIONS JIT DOMAIN DOSSIER`, REQUIRED / NEXT / NOT_STARTED, with finalisation BLOCKED / STOP. The Communications dossier has not started. Conditional dossiers remain pending explicit adjudication; Phase 7C, proof classification, Phase 8 and implementation remain blocked.

## Foundation integrity evidence

Current machine-backed foundation integrity evidence is **not** a static Markdown snapshot. It is the combination of:

- the exact `main` commit SHA under review;
- `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`;
- `tools/foundation_integrity_audit.py` and the regression tests under `tests/`;
- a passing **Foundation Integrity** GitHub Actions run on that exact commit.

The frozen August 2026 audit at `archive/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md` remains historical evidence only. It does not attest to the current authority baseline.

## Archive

- `archive/02_OPEN_WORK_v1.2.56.md` — byte-identical direct predecessor to current Open Work v1.2.57; its hash is pinned in the manifest.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md` — byte-identical direct predecessor to current Atlas v0.3.9; its hash is pinned in the manifest.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.5.0.md` — byte-identical direct predecessor to current HARDEN-02 v0.5.1; its hash is pinned in the manifest.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md` — byte-identical prior promoted/current v0.1.3 snapshot; SHA-256 `a88f993d92ea9ff0dc5652c284ccf4e2c17f4bb16b31759fb3417044d7f8e254`.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md` — exact PR #76 candidate bytes; SHA-256 `1557a4bded20b94fc363d96dd5a601213de105e0daccfa1970b869a0e38f362f`.

- `archive/02_OPEN_WORK_v1.2.55.md` — historical predecessor to archived Open Work v1.2.56, the direct predecessor to current v1.2.57.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.7.md` — byte-identical routing predecessor to archived Atlas v0.3.8.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md` — byte-identical status predecessor to archived HARDEN-02 v0.5.0.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md` — byte-identical prior current Identity dossier; SHA-256 `28dfe34dce0e9c48c737f666b112aeb89ccf45c0dfa10d2cfb81877def2538db`.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md` — exact PR #70 candidate bytes; SHA-256 `52fe67fcf6335bc0f2675c772a15a5ccdf75150f2ac4d92c98d61a9c48369285`.

`archive/` contains superseded tracker versions and working drafts:

- `archive/02_OPEN_WORK_v1.2.25.md`
- `archive/02_OPEN_WORK_v1.2.26.md`
- `archive/03_ARCHITECTURE_WORKING_v0.1.0.md`
- `archive/04_DOMAIN_MAP_WORKING_v0.1.0.md`
- `archive/04_DOMAIN_MAP_WORKING_v0.2.0.md`
- `archive/05_ROADMAP_WORKING_v0.1.0.md`
- `archive/01_DECISIONS_v1.2.1.md` — preserved superseded Decision Register.
- `archive/01_DECISIONS_v1.2.2.md`
- `archive/02_OPEN_WORK_v1.2.27.md` — preserved pre-compaction Open Work snapshot.
- `archive/02_OPEN_WORK_v1.2.28.md`
- `archive/02_OPEN_WORK_v1.2.29.md`
- `archive/02_OPEN_WORK_v1.2.30.md` — preserved pre-Stage-3A.1 Open Work snapshot.
- `archive/02_OPEN_WORK_v1.2.31.md` — preserved pre-Stage-3A.2 Open Work snapshot.
- `archive/02_OPEN_WORK_v1.2.32.md` — preserved pre-Stage-3B Open Work snapshot.
- `archive/02_OPEN_WORK_v1.2.33.md` — preserved pre-Stage-4A Open Work snapshot.
- `archive/02_OPEN_WORK_v1.2.34.md` — preserved pre-Stage-4B Open Work snapshot.
- `archive/00_PLATFORM_v1.2.1.md`
- `archive/01_DECISIONS_v1.2.3.md`
- `archive/PLATFORM_OPERATING_MODEL_WORKING_v0.2.0.md` — preserved pre-freeze Operating Model working provenance.
- `archive/FRONTEND_EXPERIENCE_SYSTEM_WORKING_v0.1.0.md` — preserved pre-hardening Frontend Experience System source provenance.
- `archive/FRONTEND_EXPERIENCE_SYSTEM_WORKING_v0.2.0.md` — preserved final pre-freeze Frontend Experience System working provenance.
- `archive/FOUNDATION_READINESS_AUDIT_v1.0.0.md` — preserved original foundation-readiness evidence.
- `archive/TARGETED_PRODUCT_AMENDMENT_GRILL_WORKING_v0.5.0.md` — completed non-authoritative Stage 1 evidence for the targeted Product amendment programme (Research & Feedback, Voting, Interactive Tools, Platform Member Reference). Historical working input only; not Product Law.
- `archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md` — completed non-authoritative Stage 3A.1 evidence; historical input to the governed v1.1.0 AR-000 amendment.
- `archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` — preserved frozen AR-000 v1.0.0 register; historical predecessor of the current v1.1.0 successor.
- `archive/02_OPEN_WORK_v1.2.35.md` — preserved pre-Architecture-amendment Open Work successor.
- `archive/03_ARCHITECTURE_v1.0.0.md` — preserved frozen Architecture synthesis predecessor.
- `archive/ARCHITECTURE_LAW_WORKING_v0.35.0.md` — preserved pre-Architecture-amendment Architecture Law predecessor.
- `archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md` — preserved pre-Architecture-amendment Reference Flow predecessor.
- `archive/02_OPEN_WORK_v1.2.36.md` — preserved pre-Domain-amendment Open Work successor.
- `archive/04_DOMAIN_MAP_v1.0.0.md` — preserved frozen Domain Map predecessor.
- `archive/02_OPEN_WORK_v1.2.37.md` — preserved pre-Roadmap-amendment Open Work successor.
- `archive/05_ROADMAP_v1.0.0.md` — preserved frozen Roadmap predecessor.
- `archive/02_OPEN_WORK_v1.2.38.md` — preserved pre-Atlas-reconciliation Open Work successor.
- `archive/02_OPEN_WORK_v1.2.39.md` — preserved pre-HARDEN-02-contract Open Work successor.
- `archive/02_OPEN_WORK_v1.2.40.md` — preserved pre-H02-3R routing-refinement Open Work successor.
- `archive/02_OPEN_WORK_v1.2.42.md` — preserved earlier Open Work predecessor.
- `archive/02_OPEN_WORK_v1.2.41.md` — preserved earlier Open Work predecessor.
- `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` — preserved predecessor to North Star v1.2.2.
- `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.2.md` — preserved predecessor to archived North Star v1.2.3.
- `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md` — preserved predecessor to archived North Star v1.2.4.
- `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md` — byte-identical predecessor to current North Star v1.3.0.
- `archive/00_PLATFORM_v1.3.0.md` — preserved earlier Product Law predecessor in the v1.3.0 → v1.4.0 → v1.4.1 history.
- `archive/00_PLATFORM_v1.4.0.md` — preserved earlier Product Law predecessor in the v1.3.0 → v1.4.0 → v1.4.1 → v1.5.0 history.
- `archive/00_PLATFORM_v1.4.1.md` — byte-identical predecessor to archived Product Law v1.5.0.
- `archive/00_PLATFORM_v1.5.0.md` — preserved predecessor to archived Product Law v1.5.1.
- `archive/00_PLATFORM_v1.5.1.md` — byte-identical predecessor to current Product Law v1.6.0.
- `archive/01_DECISIONS_v1.3.0.md` — preserved earlier Decision Register predecessor in the v1.3.0 → v1.4.0 → v1.4.1 history.
- `archive/01_DECISIONS_v1.4.0.md` — preserved earlier Decision Register predecessor in the v1.3.0 → v1.4.0 → v1.4.1 → v1.5.0 history.
- `archive/01_DECISIONS_v1.4.1.md` — preserved predecessor to archived Decision Register v1.5.0.
- `archive/01_DECISIONS_v1.5.0.md` — byte-identical predecessor to current Decision Register v1.6.0.
- `archive/02_OPEN_WORK_v1.2.44.md` — preserved earlier Open Work predecessor; v1.2.45 is preserved at archive as the predecessor to archived v1.2.46.
- `archive/02_OPEN_WORK_v1.2.45.md` — byte-identical predecessor to archived Open Work v1.2.46.
- `archive/02_OPEN_WORK_v1.2.46.md` — byte-identical predecessor to archived Open Work v1.2.47.
- `archive/02_OPEN_WORK_v1.2.47.md` — byte-identical predecessor to archived Open Work v1.2.48.
- `archive/02_OPEN_WORK_v1.2.48.md` — byte-identical predecessor to archived Open Work v1.2.49.
- `archive/02_OPEN_WORK_v1.2.49.md` — preserved predecessor to archived Open Work v1.2.50.
- `archive/02_OPEN_WORK_v1.2.54.md` — exact predecessor to archived Open Work v1.2.55.
- `archive/02_OPEN_WORK_v1.2.53.md` — byte-identical predecessor to archived Open Work v1.2.54; active Open Work is v1.2.57.
- `archive/02_OPEN_WORK_v1.2.52.md` — byte-identical predecessor to archived Open Work v1.2.53.
- `archive/02_OPEN_WORK_v1.2.50.md` — preserved predecessor to archived Open Work v1.2.51.
- `archive/02_OPEN_WORK_v1.2.43.md` — earlier preserved Open Work predecessor.
- `archive/05_ROADMAP_v1.1.0.md` — preserved earlier Roadmap predecessor in the v1.1.0 → v1.1.1 → v1.1.2 history.
- `archive/05_ROADMAP_v1.1.1.md` — preserved predecessor to archived Roadmap v1.1.2.
- `archive/05_ROADMAP_v1.1.2.md` — byte-identical predecessor to archived Roadmap v1.1.3.
- `archive/05_ROADMAP_v1.1.3.md` — byte-identical immediate predecessor to archived Roadmap v1.1.4.
- `archive/05_ROADMAP_v1.1.4.md` — preserved immediate predecessor to archived Roadmap v1.1.5.
- `archive/05_ROADMAP_v1.1.5.md` — byte-identical predecessor to current Roadmap v1.2.0.
- `archive/03_ARCHITECTURE_v1.1.0.md` — preserved amended synthesis predecessor to current path-only v1.1.1.
- `archive/04_DOMAIN_MAP_v1.1.0.md` — preserved amended Domain Map predecessor; v1.1.1 is preserved at archive as the predecessor to current v1.2.0.
- `archive/04_DOMAIN_MAP_v1.1.1.md` — byte-identical predecessor to current semantic Domain Map v1.2.0.
- `archive/PLATFORM_OPERATING_MODEL_v1.0.0.md` — preserved frozen predecessor to current path-only v1.0.1.
- `archive/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` — preserved frozen predecessor to current path-only v1.0.1.
- `archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md` — preserved FP-001 Phase 7A skeleton before current-source/OQ-034 routing correction.
- `archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md` — byte-identical predecessor to the PR #67 reconciliation candidate.
- `archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md` — byte-identical PR #67 skeleton candidate preserved by the certified/current v0.1.3 status successor.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` — byte-identical predecessor to the PR #67 reconciliation candidate.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md` — byte-identical PR #67 Identity dossier candidate preserved by the certified/current v0.1.2 status successor.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md` — byte-identical predecessor to the certified/current v0.1.3 dossier.
- `archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md` — exact PR #70 certified candidate bytes, retained with its SHA-256 pin as promotion evidence.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.1.md` — preserved pending-post-merge status snapshot.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.2.md` — preserved completed-contract status snapshot; superseded for current routing and provenance by archived v0.4.3/v0.4.4 and current v0.4.9.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.8.md` — byte-identical predecessor to archived HARDEN-02 v0.4.9; current status is v0.5.1.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.7.md` — byte-identical predecessor to archived v0.4.8; active HARDEN-02 status is v0.5.1.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.6.md` — byte-identical predecessor to archived v0.4.7.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.4.md` — byte-identical predecessor to archived v0.4.5 routing successor.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.3.md` — byte-identical predecessor to archived routing successor v0.4.4.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.4.md` — byte-identical predecessor to archived routing successor v0.4.5.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md` — preserved certified contract semantics and pre-merge lifecycle artifact; its completed lifecycle and execution start were recorded by status successor v0.4.3, preserved at `archive/HARDEN-02_CONTRACT_WORKING_v0.4.3.md`; current routing and execution status are in working v0.5.1.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.3.0.md` — preserved contract merged via PR #39; v0.3.0 lifecycle not retroactively certified.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.2.0.md` — preserved previous contract attempt; historical evidence, not repository-verifiably certified.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.1.0.md` — preserved pre-H02-3R HARDEN-02 working governance contract.
- `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md` — preserved pre-reconciliation Delivery Atlas working predecessor (ATLAS-01 through ATLAS-11 baseline).
- `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md` — preserved current-source routing and gate-status predecessor to the pinned v0.2.1 Atlas snapshot.
- `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md` — byte-identical predecessor to archived Atlas v0.2.2; the unchanged working path remains pinned by existing FP-001 and HARDEN-02 source-at-freeze references.
- `archive/DELIVERY_ATLAS_WORKING_v0.2.2.md` — preserved predecessor to archived Atlas v0.2.3.
- `archive/DELIVERY_ATLAS_WORKING_v0.2.3.md` — preserved predecessor to archived working Atlas v0.3.0.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.0.md` — byte-identical routing predecessor to archived working Atlas v0.3.1.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.1.md` — byte-identical routing predecessor to archived working Atlas v0.3.2.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.6.md` — byte-identical routing predecessor to archived Atlas v0.3.7; current Atlas is v0.3.9.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.5.md` — byte-identical routing predecessor to archived Atlas v0.3.6; active Atlas is v0.3.9.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.4.md` — byte-identical routing predecessor to archived working Atlas v0.3.5.
- `archive/DELIVERY_ATLAS_WORKING_v0.3.2.md` — preserved routing predecessor to archived Atlas v0.3.3.
- `archive/ENGINEERING_STANDARDS_v1.0.0.md` — PR #65 supporting-authority candidate bytes, preserved byte-identically and registered as historical provenance for current v1.0.1.

Archive files are historical evidence only and are never current authority. Never use an archived document to override a current authoritative document.

## Authority Order

```text
Product Law
→ Architecture Law / 03_ARCHITECTURE
→ Domain Law / 04_DOMAIN_MAP
→ 05_ROADMAP
→ PLATFORM_OPERATING_MODEL
→ FRONTEND_EXPERIENCE_SYSTEM when frontend/UI/public-experience planning is in scope
→ ENGINEERING_STANDARDS_v1.0.1.md as current supporting engineering HOW authority
→ current 02_OPEN_WORK / selected Feature Pack / JIT planning
```

Engineering Standards remain supporting authority under `reference_documents`. They do not create a governing-root layer or replace the upstream Product, Architecture, Domain, Roadmap, operating, frontend or planning documents.

## Current State

- PLANNING FOUNDATION: READY
- CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION
- NEXT STAGE: COMMUNICATIONS JIT DOMAIN DOSSIER
- CURRENT PRODUCT LAW: `00_PLATFORM_v1.6.0.md`; DEC-299 through DEC-312 record the accepted paid-plan, reversal, consent, provenance, marketing, personalisation, pilot and economics decisions
- PASS 2 FOUNDATION EVALUATION: **CLOSED / PASS** — reviewed head `4d18ef33ed8799340d6147403ac51c61237853ca` merged through PR #62 to resulting `main` `24eeb2834d58e19e0c833f09d769118d75fc9061`; reviewed and merged trees are identical (`aa4edc210d0a98aabbbdccb5ab9d4adbdc57a296`); post-merge Foundation Integrity run `36852114112` passed (250 tests / 500 assertions); independent post-merge semantic review passed. This closure advances no downstream lifecycle stage.
- ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.2.0`; the 17 existing Feature Pack identifiers are preserved
- DOL-01 POLICY: channel/category opt-out and purpose-level marketing withdrawal have separate participant-visible scope and sole owners; this does not close legal/expert gates or authorize implementation
- TARGETED PRODUCT AMENDMENT STAGE 1 (GRILL): COMPLETE
- TARGETED PRODUCT AMENDMENT STAGE 2 (PRODUCT LAW AMENDMENT): COMPLETE
- STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE / ARCHIVED AS HISTORICAL EVIDENCE
- STAGE 3A.2 — GOVERNED AR-000 AMENDMENT: COMPLETE
- STAGE 3B — INDEPENDENT ARCHITECTURE/ENGINEERING CLASSIFICATION: COMPLETE
- STAGE 4A — PRODUCT-DERIVED ARCHITECTURE GRILL: COMPLETE
- STAGE 4B — ENGINEERING-POLICY GRILL: COMPLETE
- ARCHITECTURE GRILL: COMPLETE
- ENGINEERING-POLICY GRILL: COMPLETE
- ARCHITECTURE AMENDMENT: COMPLETE — current law `v0.36.0`, synthesis `v1.1.1` (path-only successor to archived v1.1.0), targeted flows `v0.3.0`
- DOMAIN PRESSURE TEST: COMPLETE
- DOMAIN AMENDMENT: COMPLETE — current Domain Law `v1.2.0` (semantic successor to archived v1.1.1); 20 Domains; Domain 19 Research & Feedback; Domain 20 Voting & Balloting
- ROADMAP SEQUENCING GRILL: COMPLETE
- ROADMAP SEQUENCING AMENDMENT: COMPLETE — current semantic successor `05_ROADMAP_v1.2.0.md`; predecessor `archive/05_ROADMAP_v1.1.5.md`; Feature Packs 17; PMR REQUIRED in FP-001; Research/Voting FUTURE-GATED / FEATURE-PACK-UNASSIGNED
- ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED — current supporting authority `reference/ENGINEERING_STANDARDS_v1.0.1.md`; PR #65 candidate lifecycle evidence is bound in the artifact; v1.0.0 candidate bytes are preserved in `archive/`
- ATLAS RECONCILIATION: COMPLETE — current routing successor `working/DELIVERY_ATLAS_WORKING_v0.3.9.md` (derived / non-authoritative; ATLAS-12 remains NOT_STARTED)
- HARDEN-02 v0.4.0 CONTRACT LIFECYCLE: COMPLETE / CERTIFIED
- PRE-MERGE CERTIFICATION: COMPLETE — [PR #40 record](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5827553565)
- EXACT-HEAD FOUNDATION INTEGRITY: PASS — [run 36091130615](https://github.com/JCSchoeman96/NewYou/actions/runs/36091130615)
- CERTIFIED-HEAD MERGE: COMPLETE / UNCHANGED — certified head `cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4` merged as `352f304139b9d4f8ee3ba205cde9e34d0ad8437f`
- RESULTING-MAIN FOUNDATION INTEGRITY: PASS — [run 36101210535](https://github.com/JCSchoeman96/NewYou/actions/runs/36101210535)
- POST-MERGE CERTIFICATION: COMPLETE — fresh independent review PASS and durable attestation COMPLETE at [PR #40 record](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5830618876)
- HARDEN-02 CURRENT STATUS: working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md records PR #76 candidate certification evidence and the separate PR #77 Identity v0.1.4 current-status successor; v0.4.0 semantics and prior execution evidence are unchanged
- HARDEN-02 EXECUTION: COMPLETE / CERTIFIED
- PR #38: STALE / BLOCKED / NOT AUTHORITY
- FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED
- IDENTITY v0.1.4: CERTIFIED / CURRENT under the separate PR #77 status successor; PR #76 candidate and post-merge certification evidence are COMPLETE
- COMM-UPD-001 content ownership and COMM-UPD-002 scanner-safe proof consumption: CERTIFIED / CURRENT
- COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED
- COMMUNICATIONS FINALISATION: BLOCKED / STOP pending Communications dossier and applicable gates
- FP-001 PHASE 7A: COMPLETE
- IDENTITY & ACCESS JIT DOMAIN DOSSIER v0.1.4: COMPLETE / CERTIFIED / CURRENT
- OQ-034 ARCHITECTURE SELECTION: RESOLVED
- OQ-034 EXECUTABLE AUTHENTICATION PROOF: PHASE 8 OBLIGATION / INCOMPLETE; proof classification NOT FINALISED
- OQ-035: SECURITY / OPERATIONS REVIEW; UNRESOLVED; RELEASE-ONLY SCOPE
- OQ-036: VENDOR / OPERATIONS REVIEW; UNRESOLVED; RELEASE-ONLY SCOPE
- COMMUNICATIONS DOSSIER: REQUIRED / NEXT / NOT_STARTED
- PRIVACY & CONSENT DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- CONTENT & MEDIA DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- ANALYTICS DOSSIER: NOT REQUIRED
- PHASE 7C: BLOCKED / NOT_STARTED pending the required Communications dossier and explicit conditional-dossier dispositions.
- PROOF CLASSIFICATION: NOT FINALISED
- EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS
- DELIVERY ATLAS WORKING BASELINE: ATLAS-01 THROUGH ATLAS-11 COMPLETE AT CURRENT SCOPE; ATLAS RECONCILIATION COMPLETE; ATLAS-12 NOT_STARTED (not this reconciliation); DERIVED / NON-AUTHORITATIVE

The v0.4.0 contract lifecycle is COMPLETE / CERTIFIED. PR #40's pre-merge attestation [#5827553565](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5827553565) binds the exact certified head and exact-head Foundation Integrity run; its post-merge attestation [#5830618876](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5830618876) records PASS on resulting main SHA `352f304139b9d4f8ee3ba205cde9e34d0ad8437f` and resulting-main Foundation Integrity run [36101210535](https://github.com/JCSchoeman96/NewYou/actions/runs/36101210535). HARDEN-02 execution is COMPLETE / CERTIFIED based on the full PR #59 recovery lifecycle and current-main revalidation. PR #59's fresh independent post-merge outcome remains PASS WITH NON-BLOCKING CORRECTIONS; its retained Roadmap §21 direct-helper mutation-coverage correction is non-blocking because the whole current §21 remains byte-identical to archived v1.1.5 and this successor adds an explicit whole-section preservation test. Engineering Standards Authority Promotion is COMPLETE / CERTIFIED. PR #67 records FP-001 reconciliation COMPLETE / CERTIFIED; PR #76 certified the v0.1.4 candidate and supplied completed post-merge certification evidence but did not make it current. The separate PR #77 status successor records Identity v0.1.4 as CURRENT. Communications is REQUIRED / NEXT / NOT_STARTED. Phase 7C remains blocked / not started; proof classification remains not finalised; Phase 8 and executable implementation remain blocked. Store/CER remains excluded from HARDEN-02.

Foundation readiness does not authorise implementation. Do not begin FP-001 execution, JIT Domain Dossiers, TOON generation, Architectural Proof, Vertical Slices or implementation unless a later approved task explicitly authorises the applicable preparation and execution gates.

PRODUCT LAW AND GOVERNANCE HARDENING IS RECORDED IN THE CURRENT SUCCESSORS. HARDEN-02 EXECUTION, ENGINEERING STANDARDS AUTHORITY PROMOTION, FP-001 PMR RECONCILIATION AND IDENTITY v0.1.4 PROMOTION ARE COMPLETE / CERTIFIED; COMMUNICATIONS JIT DOMAIN DOSSIER REMAINS REQUIRED / NEXT / NOT_STARTED AND COMMUNICATIONS FINALISATION REMAINS BLOCKED / STOP PENDING ITS OWN DOSSIER AND APPLICABLE GATES. PHASE 7C REMAINS BLOCKED / NOT_STARTED, PROOF CLASSIFICATION IS NOT FINALISED, AND PHASE 8 / EXECUTABLE DEVELOPMENT REMAIN BLOCKED UNTIL THEIR ENTRY CONDITIONS PASS.
