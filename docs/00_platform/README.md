# NewYou Platform Documentation

This directory separates current platform authority from deep evidence and historical planning material. The separation is for agent-context hygiene only; it does not change Product Law, Architecture Law, Domain Law, Roadmap meaning or ownership.

## Default Agent Context

For foundation/default planning and delivery-preparation work, read **only** these current-authority documents first:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.43.md`
5. `03_ARCHITECTURE_v1.1.0.md`
6. `04_DOMAIN_MAP_v1.1.0.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.0.md`

For frontend, UI, public-experience, design-system, accessibility, SEO, analytics-UI or Feature Pack planning, additionally load:

9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md`

Do not automatically read files under `reference/` or `archive/`.

Routine Phase 7 work should use the README, current Roadmap, current Open Work, the relevant Feature Pack section, frozen Architecture, relevant Domain Map sections and specific Product/Decision references. Consult deep evidence only when a real question requires exact source tracing.

## Current Authority

The nine documents listed above describe the current platform state. Their explicit versioned filenames are intentional and should not be replaced with unversioned aliases without a separate governance decision.

The README and manifest are the current routing pointers. Frozen artifacts may retain source-at-freeze filenames as historical provenance; those references do not override the current routing above.

The frozen Frontend Experience System is current authority for affected frontend-experience planning, but it is conditionally loaded rather than default context for unrelated routine work.

## Active Working Artifacts

`working/` contains active, derived planning artifacts. These files are not current authority, deep-reference evidence or historical archive, and they are intentionally outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`. Read them only when a task explicitly concerns experience or operating-model planning; they must not override the nine current-authority documents. They remain working until an explicit freeze review and governance decision.

- `working/EXPERIENCE_DECISIONS_WORKING_v0.7.0.md` — cumulative experience decision register; remains working/non-authoritative provenance.
- `working/DELIVERY_ATLAS_WORKING_v0.2.0.md` — derived Delivery Atlas navigation for approved Feature Pack planning after post-Roadmap reconciliation; remains working/non-authoritative and is intentionally outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`. Predecessor preserved at `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`.
- `working/HARDEN-02_CONTRACT_WORKING_v0.4.0.md` — HARDEN-02 Phase-7 governance / structural-hardening contract; solo-maintainer certification-mechanism amendment (review actor vs attestation poster); WORKING GOVERNANCE CONTRACT only; OPEN / PENDING INDEPENDENT PRE-MERGE CERTIFICATION; re-baselined from main SHA `6f9ce049616881805b1086d19ce747358de3c067`; PR #39 merged v0.3.0 without retroactive certification; requires independent review-actor exact-SHA attestation and CI lifecycle; execution remains NOT STARTED / NOT AUTHORISED; intentionally outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md` — non-authoritative Stage 3B classification; it does not amend Product Law, AR-000, Architecture Law or Engineering Standards and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage 4A Architecture Grill evidence; it does not amend Product Law, AR-000 or Architecture Law, creates no ARC identifiers, and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage 4B Engineering-Policy Grill evidence; it does not amend Product Law, AR-000 or Architecture Law, does not create Engineering Standards, does not install dependencies, and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.
- `working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md` — non-authoritative targeted Domain pressure-test evidence; it does not itself create Domain Law. Domain Law is created only by the versioned Domain Map successor.
- `working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md` — non-authoritative Stage Roadmap Sequencing Grill evidence; it does not itself create Roadmap Law. Roadmap Law is created only by the versioned Roadmap successor.

## Delivery Atlas routing

Use the [Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.2.0.md) only after selecting or investigating an approved Roadmap Feature Pack or an Atlas planning question. It does not override the nine current-authority documents above, change Product/Architecture/Domain/Roadmap law, authorise Phase 7 or authorise implementation.

Do not load the whole Atlas by default. Load only the relevant sections: the Feature Pack and capability views in §§4–5, active-FP derivation contracts in §§6–12, and the routing/governance rules in §§23–25 as needed. Every material Atlas conclusion must resolve to an exact current upstream authority reference. Atlas navigation feeds the canonical Phase 7A Feature Pack Skeleton + preliminary Gate Manifest → Phase 7B required JIT Domain Dossiers → Phase 7C Final Feature Pack Contract sequence; the Atlas creates none of those artifacts.

## Machine-readable inventory

`CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` is the machine-readable inventory of current authority and deep-reference evidence. It records canonical paths, SemVer, authority class, SHA-256 and superseded-version metadata; it does not create a new authority layer.

## Reference Documents

Use `reference/` only when the current authority requires exact evidence or identifier-level reasoning:

- `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` — current cumulative ARQ source tracing and Stage 3A.2 amendment.
- `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` — exact ARC legislative reasoning, including the Architecture-amendment successor.
- `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md` — detailed FLOW evidence and the seven targeted Architecture-amendment reviews.
- `reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md` — current machine-backed foundation integrity evidence.

These documents are valuable evidence, but they are not default context for routine planning or delivery preparation.

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
- `archive/02_OPEN_WORK_v1.2.42.md` — preserved predecessor to current Open Work v1.2.43.
- `archive/02_OPEN_WORK_v1.2.41.md` — preserved earlier Open Work predecessor.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.3.0.md` — preserved contract merged via PR #39; v0.3.0 lifecycle not retroactively certified.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.2.0.md` — preserved previous contract attempt; historical evidence, not repository-verifiably certified.
- `archive/HARDEN-02_CONTRACT_WORKING_v0.1.0.md` — preserved pre-H02-3R HARDEN-02 working governance contract.
- `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md` — preserved pre-reconciliation Delivery Atlas working predecessor (ATLAS-01 through ATLAS-11 baseline).

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
- CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 CONTRACT RECOVERY / SOLO-MAINTAINER CERTIFICATION AMENDMENT
- NEXT STAGE: HARDEN-02_CONTRACT_RECOVERY_REQUIRED
- TARGETED PRODUCT AMENDMENT STAGE 1 (GRILL): COMPLETE
- TARGETED PRODUCT AMENDMENT STAGE 2 (PRODUCT LAW AMENDMENT): COMPLETE
- STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE / ARCHIVED AS HISTORICAL EVIDENCE
- STAGE 3A.2 — GOVERNED AR-000 AMENDMENT: COMPLETE
- STAGE 3B — INDEPENDENT ARCHITECTURE/ENGINEERING CLASSIFICATION: COMPLETE
- STAGE 4A — PRODUCT-DERIVED ARCHITECTURE GRILL: COMPLETE
- STAGE 4B — ENGINEERING-POLICY GRILL: COMPLETE
- ARCHITECTURE GRILL: COMPLETE
- ENGINEERING-POLICY GRILL: COMPLETE
- ARCHITECTURE AMENDMENT: COMPLETE — current law `v0.36.0`, synthesis `v1.1.0`, targeted flows `v0.3.0`
- DOMAIN PRESSURE TEST: COMPLETE
- DOMAIN AMENDMENT: COMPLETE — current Domain Law `v1.1.0`; 20 Domains; Domain 19 Research & Feedback; Domain 20 Voting & Balloting
- ROADMAP SEQUENCING GRILL: COMPLETE
- ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.1.0`; Feature Packs 17; PMR REQUIRED in FP-001; Research/Voting FUTURE-GATED / FEATURE-PACK-UNASSIGNED
- ENGINEERING STANDARDS AUTHORITY PROMOTION: DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED
- ATLAS RECONCILIATION: COMPLETE — `working/DELIVERY_ATLAS_WORKING_v0.2.0.md` (derived / non-authoritative)
- HARDEN-02 CONTRACT RECOVERY: OPEN / PENDING INDEPENDENT REVIEW-ACTOR PRE-MERGE CERTIFICATION — `working/HARDEN-02_CONTRACT_WORKING_v0.4.0.md`; baseline main SHA `6f9ce049616881805b1086d19ce747358de3c067`; PR #39 merged v0.3.0 (not retroactively certified)
- HARDEN-02 EXECUTION: NOT STARTED / NOT AUTHORISED
- PR #38: STALE / BLOCKED / NOT AUTHORITY
- `FP001_RECONCILIATION_REQUIRED` — DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION
- COMMUNICATIONS JIT DOMAIN DOSSIER — DOWNSTREAM AFTER NARROW FP-001 RECONCILIATION
- FP-001 PHASE 7A: COMPLETE
- IDENTITY & ACCESS JIT DOMAIN DOSSIER: COMPLETE / MERGED
- OQ-034 ARCHITECTURE SELECTION: RESOLVED
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

Ordinary FP-001 Phase 7B preparation remains suspended / downstream. v0.4.0 amends the certification mechanism for solo-maintainer workflow (independent review actor with truthful GitHub attestation; poster may equal PR author). PR #39 merged v0.3.0 with valid post-merge CI but v0.3.0 is not retroactively certified. Execution stays NOT STARTED / NOT AUTHORISED until the v0.4.0 lifecycle completes with review-actor certification, exact-head CI PASS, unchanged-head merge, post-merge CI PASS and post-merge attestation. After certified HARDEN-02 execution, the downstream route remains Engineering Standards Authority Promotion, certified Standards Promotion, FP-001 reconciliation, Communications, remaining required / conditional Phase-7B work, Phase 7C, proof classification, then Phase 8 only after the Development Entry Hard Stop passes. Store/CER remains excluded from HARDEN-02.

Foundation readiness does not authorise implementation. Do not begin FP-001 execution, JIT Domain Dossiers, TOON generation, Architectural Proof, Vertical Slices or implementation unless a later approved task explicitly authorises the applicable preparation and execution gates.

FOUNDATION INTEGRITY PATCH COMPLETE. NO FURTHER FOUNDATION EXPANSION WITHOUT AN UPSTREAM CONTRADICTION.
