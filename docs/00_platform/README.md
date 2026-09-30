# NewYou Platform Documentation

This directory separates current platform authority from deep evidence and historical planning material. The separation is for agent-context hygiene only; it does not change Product Law, Architecture Law, Domain Law, Roadmap meaning or ownership.

## Default Agent Context

For foundation/default planning and delivery-preparation work, read **only** these current-authority documents first:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.51.md`
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
- `working/DELIVERY_ATLAS_WORKING_v0.3.3.md` — derived Delivery Atlas navigation with current-source routing for approved Feature Pack planning. It remains working/non-authoritative, outside authority-document records, and is listed only under graph/navigation paths. Atlas navigation may help delivery preparation when relevant; it cannot create a new authority gate or prerequisite. Predecessor v0.3.2 is preserved byte-identically at `archive/DELIVERY_ATLAS_WORKING_v0.3.2.md`; v0.3.1 remains at `archive/DELIVERY_ATLAS_WORKING_v0.3.1.md`; v0.2.3 remains preserved at `archive/DELIVERY_ATLAS_WORKING_v0.2.3.md`; earlier v0.2.2, v0.2.1 and v0.2.0 files remain at `archive/DELIVERY_ATLAS_WORKING_v0.2.2.md`, `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md` and `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`. The unchanged v0.2.1 working path remains available to existing FP-001 and HARDEN-02 source-at-freeze references.
- `working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md` — current-source-routing successor to v0.4.4 for the original v0.4.0 certified HARDEN-02 contract semantics; PR #40 exact-head certification, unchanged merge, both exact-SHA Foundation Integrity runs, fresh independent post-merge review and durable post-merge attestation are COMPLETE / PASS. HARDEN-02 execution is IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING. Working contracts remain outside the authority-document records in `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`. Predecessor v0.4.4 is preserved byte-identically at `archive/HARDEN-02_CONTRACT_WORKING_v0.4.4.md`; v0.4.3 remains at `archive/HARDEN-02_CONTRACT_WORKING_v0.4.3.md`; earlier v0.4.1 remains at `archive/HARDEN-02_CONTRACT_WORKING_v0.4.1.md`; archived v0.4.2 remains at `archive/HARDEN-02_CONTRACT_WORKING_v0.4.2.md`; certified contract artifact v0.4.0 remains at `archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md`.
- `working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md` — active Phase 7A planning artifact; OQ-034 is resolved for architecture selection and its Phase 8 executable proof remains incomplete; PMR reconciliation remains downstream and is not performed; intentionally outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`. Predecessor preserved at `archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md`.
- `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md` — non-authoritative Stage 3B classification; it does not amend Product Law, AR-000, Architecture Law or Engineering Standards and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage 4A Architecture Grill evidence; it does not amend Product Law, AR-000 or Architecture Law, creates no ARC identifiers, and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage 4B Engineering-Policy Grill evidence; it does not amend Product Law, AR-000 or Architecture Law, does not create Engineering Standards, does not install dependencies, and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md` — non-authoritative targeted Domain pressure-test evidence; it does not itself create Domain Law. Domain Law is created only by the versioned Domain Map successor.
- `working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage Roadmap Sequencing Grill evidence; it does not itself create Roadmap Law. Roadmap Law is created only by the versioned Roadmap successor.

## Delivery Atlas routing

Use the [Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.3.3.md) during delivery preparation when its derived navigation helps with an approved Roadmap Feature Pack or a relevant planning question. Consulting the Atlas is not itself a gate or prerequisite. It does not override the nine current-authority documents above, change Product/Architecture/Domain/Roadmap law, authorise Phase 7 or authorise implementation.

Do not load the whole Atlas by default. Load only the relevant sections: the Feature Pack and capability views in §§4–5, active-FP derivation contracts in §§6–12, and the routing/governance rules in §§23–25 as needed. Every material Atlas conclusion must resolve to an exact current upstream authority reference. The Atlas may point to the canonical Phase 7A Feature Pack Skeleton + preliminary Gate Manifest → Phase 7B required JIT Domain Dossiers → Phase 7C Final Feature Pack Contract sequence when relevant; that navigation adds no gate or artifact, and the Atlas creates none of those artifacts.

## Machine-readable inventory

`CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` is the machine-readable inventory of current authority and deep-reference evidence. It records canonical paths, SemVer, authority class, SHA-256 and superseded-version metadata; it does not create a new authority layer.

## Reference Documents

Use `reference/` only when the current authority requires exact evidence or identifier-level reasoning:

- `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` — current cumulative ARQ source tracing and Stage 3A.2 amendment.
- `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` — exact ARC legislative reasoning, including the Architecture-amendment successor.
- `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md` — detailed FLOW evidence and the seven targeted Architecture-amendment reviews.

These documents are valuable evidence, but they are not default context for routine planning or delivery preparation.

## Foundation integrity evidence

Current machine-backed foundation integrity evidence is **not** a static Markdown snapshot. It is the combination of:

- the exact `main` commit SHA under review;
- `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`;
- `tools/foundation_integrity_audit.py` and the regression tests under `tests/`;
- a passing **Foundation Integrity** GitHub Actions run on that exact commit.

The frozen August 2026 audit at `archive/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md` remains historical evidence only. It does not attest to the current authority baseline.

## Archive

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
- `archive/02_OPEN_WORK_v1.2.50.md` — byte-identical predecessor to current Open Work v1.2.51.
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
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.1.md` — preserved pending-post-merge status snapshot.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.2.md` — preserved completed-contract status snapshot; superseded for current routing and provenance by archived v0.4.3/v0.4.4 and current v0.4.5.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.4.md` — byte-identical predecessor to current v0.4.5 routing successor.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.3.md` — byte-identical predecessor to archived routing successor v0.4.4.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.4.md` — byte-identical predecessor to current routing successor v0.4.5.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md` — preserved certified contract semantics and pre-merge lifecycle artifact; its completed lifecycle and execution start were recorded by status successor v0.4.3, preserved at `archive/HARDEN-02_CONTRACT_WORKING_v0.4.3.md`; current routing and execution status are in working v0.4.5.
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
- `archive/DELIVERY_ATLAS_WORKING_v0.3.2.md` — byte-identical routing predecessor to current working Atlas v0.3.3.

Archive files are historical evidence only and are never current authority. Never use an archived document to override a current authoritative document.

## Authority Order

```text
Product Law
→ Architecture Law / 03_ARCHITECTURE
→ Domain Law / 04_DOMAIN_MAP
→ 05_ROADMAP
→ PLATFORM_OPERATING_MODEL
→ FRONTEND_EXPERIENCE_SYSTEM when frontend/UI/public-experience planning is in scope
→ current 02_OPEN_WORK / selected Feature Pack / JIT planning
```

Engineering Standards are **not yet current authority**. Current routing requires their separate supporting-authority promotion after certified HARDEN-02 execution and before FP-001 reconciliation resumes.

## Current State

- PLANNING FOUNDATION: READY
- CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING
- NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED
- CURRENT PRODUCT LAW: `00_PLATFORM_v1.6.0.md`; DEC-299 through DEC-312 record the accepted paid-plan, reversal, consent, provenance, marketing, personalisation, pilot and economics decisions
- PASS 2 FOUNDATION EVALUATION: ADJUDICATED / CORRECTION SPEC APPROVED; closure remains pending merge of the exact reviewed head, resulting-main Foundation Integrity and independent post-merge review
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
- ENGINEERING STANDARDS AUTHORITY PROMOTION: DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED
- ATLAS RECONCILIATION: COMPLETE — current routing successor `working/DELIVERY_ATLAS_WORKING_v0.3.3.md` (derived / non-authoritative; ATLAS-12 remains NOT_STARTED)
- HARDEN-02 v0.4.0 CONTRACT LIFECYCLE: COMPLETE / CERTIFIED
- PRE-MERGE CERTIFICATION: COMPLETE — [PR #40 record](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5827553565)
- EXACT-HEAD FOUNDATION INTEGRITY: PASS — [run 36091130615](https://github.com/JCSchoeman96/NewYou/actions/runs/36091130615)
- CERTIFIED-HEAD MERGE: COMPLETE / UNCHANGED — certified head `cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4` merged as `352f304139b9d4f8ee3ba205cde9e34d0ad8437f`
- RESULTING-MAIN FOUNDATION INTEGRITY: PASS — [run 36101210535](https://github.com/JCSchoeman96/NewYou/actions/runs/36101210535)
- POST-MERGE CERTIFICATION: COMPLETE — fresh independent review PASS and durable attestation COMPLETE at [PR #40 record](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5830618876)
- HARDEN-02 CURRENT STATUS: `working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md` records the completed v0.4.0 lifecycle and execution status; execution-start baseline main SHA is `1c8fc94058176795d88cb82e08857e3d30c553e9`; v0.4.0 semantics are unchanged
- HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING
- PR #38: STALE / BLOCKED / NOT AUTHORITY
- `FP001_RECONCILIATION_REQUIRED` — DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION
- COMMUNICATIONS JIT DOMAIN DOSSIER — DOWNSTREAM AFTER NARROW FP-001 RECONCILIATION
- FP-001 PHASE 7A: COMPLETE
- IDENTITY & ACCESS JIT DOMAIN DOSSIER: COMPLETE / MERGED
- OQ-034 ARCHITECTURE SELECTION: RESOLVED
- OQ-034 EXECUTABLE AUTHENTICATION PROOF: PHASE 8 OBLIGATION / INCOMPLETE; proof classification NOT FINALISED
- OQ-035: SECURITY / OPERATIONS REVIEW; UNRESOLVED; RELEASE-ONLY SCOPE
- OQ-036: VENDOR / OPERATIONS REVIEW; UNRESOLVED; RELEASE-ONLY SCOPE
- COMMUNICATIONS DOSSIER: REQUIRED / NOT_STARTED
- PRIVACY & CONSENT DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- CONTENT & MEDIA DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- ANALYTICS DOSSIER: NOT REQUIRED
- PHASE 7C: BLOCKED / NOT_STARTED pending the required Communications dossier and explicit conditional-dossier dispositions.
- PROOF CLASSIFICATION: NOT FINALISED
- EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS
- DELIVERY ATLAS WORKING BASELINE: ATLAS-01 THROUGH ATLAS-11 COMPLETE AT CURRENT SCOPE; ATLAS RECONCILIATION COMPLETE; ATLAS-12 NOT_STARTED (not this reconciliation); DERIVED / NON-AUTHORITATIVE

The v0.4.0 contract lifecycle is COMPLETE / CERTIFIED. Pre-merge attestation [#5827553565](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5827553565) binds the exact certified head and exact-head Foundation Integrity run; post-merge attestation [#5830618876](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5830618876) records PASS on resulting main SHA `352f304139b9d4f8ee3ba205cde9e34d0ad8437f` and resulting-main Foundation Integrity run [36101210535](https://github.com/JCSchoeman96/NewYou/actions/runs/36101210535). HARDEN-02 execution is IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING. The route after certified execution remains Engineering Standards Authority Promotion, certified Standards Promotion, FP-001 reconciliation, Communications, remaining required / conditional Phase-7B work, Phase 7C, proof classification, then Phase 8 only after the Development Entry Hard Stop passes. Store/CER remains excluded from HARDEN-02.

Foundation readiness does not authorise implementation. Do not begin FP-001 execution, JIT Domain Dossiers, TOON generation, Architectural Proof, Vertical Slices or implementation unless a later approved task explicitly authorises the applicable preparation and execution gates.

PRODUCT LAW AND GOVERNANCE HARDENING IS RECORDED IN THE CURRENT SUCCESSORS. HARDEN-02 EXECUTION IS IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING. EXECUTABLE DEVELOPMENT REMAINS BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS.
