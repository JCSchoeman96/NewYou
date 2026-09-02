# NewYou Platform Documentation

This directory separates current platform authority from deep evidence and historical planning material. The separation is for agent-context hygiene only; it does not change Product Law, Architecture Law, Domain Law, Roadmap meaning or ownership.

## Default Agent Context

For foundation/default planning and delivery-preparation work, read **only** these current-authority documents first:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.2.1.md`
3. `01_DECISIONS_v1.2.3.md`
4. `02_OPEN_WORK_v1.2.29.md`
5. `03_ARCHITECTURE_v1.0.0.md`
6. `04_DOMAIN_MAP_v1.0.0.md`
7. `05_ROADMAP_v1.0.0.md`
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
- `working/DELIVERY_ATLAS_WORKING_v0.1.0.md` — derived Delivery Atlas navigation for approved Feature Pack planning; remains working/non-authoritative and is intentionally outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.

## Delivery Atlas routing

Use the [Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.1.0.md) only after selecting or investigating an approved Roadmap Feature Pack or an Atlas planning question. It does not override the nine current-authority documents above, change Product/Architecture/Domain/Roadmap law, authorise Phase 7 or authorise implementation.

Do not load the whole Atlas by default. Load only the relevant sections: the Feature Pack and capability views in §§4–5, active-FP derivation contracts in §§6–12, and the routing/governance rules in §§23–25 as needed. Every material Atlas conclusion must resolve to an exact current upstream authority reference. Atlas navigation feeds the canonical Phase 7A Feature Pack Skeleton + preliminary Gate Manifest → Phase 7B required JIT Domain Dossiers → Phase 7C Final Feature Pack Contract sequence; the Atlas creates none of those artifacts.

## Machine-readable inventory

`CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` is the machine-readable inventory of current authority and deep-reference evidence. It records canonical paths, SemVer, authority class, SHA-256 and superseded-version metadata; it does not create a new authority layer.

## Reference Documents

Use `reference/` only when the current authority requires exact evidence or identifier-level reasoning:

- `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` — exact ARQ source tracing.
- `reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md` — exact ARC legislative reasoning.
- `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md` — detailed FLOW evidence.
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
- `archive/PLATFORM_OPERATING_MODEL_WORKING_v0.2.0.md` — preserved pre-freeze Operating Model working provenance.
- `archive/FRONTEND_EXPERIENCE_SYSTEM_WORKING_v0.1.0.md` — preserved pre-hardening Frontend Experience System source provenance.
- `archive/FRONTEND_EXPERIENCE_SYSTEM_WORKING_v0.2.0.md` — preserved final pre-freeze Frontend Experience System working provenance.
- `archive/FOUNDATION_READINESS_AUDIT_v1.0.0.md` — preserved original foundation-readiness evidence.

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

## Current State

- PLANNING FOUNDATION: READY
- FP-001 PHASE 7A: COMPLETE
- IDENTITY & ACCESS JIT DOMAIN DOSSIER: COMPLETE / MERGED
- OQ-034 ARCHITECTURE SELECTION: RESOLVED
- OQ-035: UNRESOLVED / SECURITY & OPERATIONS REVIEW
- OQ-036: UNRESOLVED / VENDOR & OPERATIONS REVIEW
- COMMUNICATIONS DOSSIER: REQUIRED / NOT STARTED
- PRIVACY & CONSENT DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- CONTENT & MEDIA DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION
- ANALYTICS DOSSIER: NOT REQUIRED
- NEXT: PHASE 7 / FP-001 PREPARATION
- NEXT GOVERNANCE / DELIVERY-PIPELINE TASK: HARDEN-02
- NEXT FP-001 PHASE-7B DOMAIN TASK AFTER HARDEN-02: COMMUNICATIONS JIT DOMAIN DOSSIER
- PHASE 7C: BLOCKED / NOT STARTED
- PROOF CLASSIFICATION: NOT FINALISED
- EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS
- DELIVERY ATLAS WORKING BASELINE: ATLAS-01 THROUGH ATLAS-11 COMPLETE AT CURRENT SCOPE; ATLAS-12 NOT STARTED; DERIVED / NON-AUTHORITATIVE

HARDEN-02 is governance sequencing only and is not a Roadmap gate, Product requirement, FP-001 dependency or blocking OQ.

Foundation readiness does not authorise implementation. Do not begin FP-001 execution, JIT Domain Dossiers, TOON generation, Architectural Proof, Vertical Slices or implementation unless a later approved task explicitly authorises the applicable preparation and execution gates.
