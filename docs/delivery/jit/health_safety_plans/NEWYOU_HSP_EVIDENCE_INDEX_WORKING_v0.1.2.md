# Health / Safety / Plans Compressed Evidence Index — Working v0.1.2

- **Status:** WORKING / NON-AUTHORITATIVE TRACEABILITY
- **Purpose:** Let FP-004/FP-005 JIT planning trace each compressed clause without loading the full v0.42.0 discovery suite.
- **Implementation:** NOT AUTHORISED.
- **v0.1.2 hygiene patch:** Traceability content is unchanged. This successor standardises canonical `Phase 7C Final Feature Pack Contract` terminology where referenced and replaces chat-specific “uploaded” source wording with durable source-artifact wording.

## Live authority baseline used for this consolidation

Verified against the live `JCSchoeman96/NewYou` default branch at commit:

`c4ed5ce95b151c060c104bbec6b25edefb271814`

Current routed authority:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.39.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.1.1.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` only when frontend/experience planning is in scope.

The current `v1.3.0` Product amendment and `v1.1.0` Architecture/Domain/Roadmap amendments are additive for Research & Feedback, Voting & Balloting, Interactive Tools and Platform Member Reference. They do not alter the Health → Safety → Plans authority model or FP-004/FP-005 sequencing used here.

The source `HEALTH_SAFETY_PLAN_PREJIT_DISCOVERY_WORKING_v0.42.0.md` remains working evidence only.


## Index

| Contract clause | Working decisions | Pressure-test evidence | Current authoritative anchors |
|---|---|---|---|
| **Ownership / one authority per durable truth** | `HSP-WD-022`, `HSP-WD-023`, `HSP-WD-030` | `HSP-PT-001`, `HSP-PT-006`, `HSP-PT-014`, `HSP-PT-016` | `04_DOMAIN_MAP_v1.1.0` §§6.4 Health Records, 6.5 Safety & Eligibility, 6.6 Plans & Nutrition, 6.10 Commerce, 6.11 Entitlements, 6.14 Professional Care; `03_ARCHITECTURE_v1.1.0` §5. |
| **Health update semantics: observation/change/correction/verification/conflict** | `HSP-WD-001...004`, `HSP-WD-017...020`, `HSP-WD-027...029` | `HSP-PT-001`, `HSP-PT-004`, `HSP-PT-010...013` | `DEC-073...DEC-095`; Domain Map §6.4; Architecture current-authority/privacy boundaries. |
| **Temporal truth / authoritative known time** | `HSP-WD-018`, `HSP-WD-027`, `HSP-WD-029` | `HSP-PT-010`, `HSP-PT-012` | Product provenance/history rules `DEC-076`, `DEC-086`; Architecture durability/current-authority doctrine. |
| **Conflict-aware Health evidence** | `HSP-WD-004`, `HSP-WD-028` | `HSP-PT-011` | `DEC-076...DEC-080`, `DEC-084...DEC-086`; Domain Map §6.4–6.5; Roadmap FP-004 fail-closed objective. |
| **Intake purpose/version readiness** | `HSP-WD-001`, `HSP-WD-017`, `HSP-WD-019` | `HSP-PT-001`, `HSP-PT-005` | `DEC-073`, `DEC-074`, `DEC-077...DEC-080`; `05_ROADMAP_v1.1.0` FP-004. |
| **Positive automation admission** | `HSP-WD-005` | `HSP-PT-001`, `HSP-PT-004`, `HSP-PT-011` | `DEC-078...DEC-085`; FP-004 validation objective; Product safety boundaries. |
| **Safety permission ≠ Plans capability** | `HSP-WD-006`, `HSP-WD-016` | `HSP-PT-015` | `DEC-078`, `DEC-096`, `DEC-109`, `DEC-116`; Domain Map §§6.5–6.6; FP-004 → FP-005 sequencing. |
| **Eligibility Evaluation vs Safety Impact Assessment vs Safety Case** | `HSP-WD-020`, `HSP-WD-021` | `HSP-PT-004`, `HSP-PT-005`, `HSP-PT-013` | `DEC-089...DEC-093`; Safety Domain §6.5. |
| **Request ≠ Attempt ≠ Plan Version** | `HSP-WD-007...012`, refined by `HSP-WD-031` | `HSP-PT-002`, `HSP-PT-003`, `HSP-PT-015`, `HSP-PT-017`, `HSP-PT-018`, `HSP-PT-020` | `DEC-109...DEC-111`; Plans Domain §6.6; Architecture §8 idempotency/recovery. |
| **Request lifecycle `open → fulfilled/cancelled/invalidated/unfulfillable`** | `HSP-WD-011`, `HSP-WD-016`, `HSP-WD-031` | `HSP-PT-001`, `HSP-PT-015`, `HSP-PT-017`, `HSP-PT-020` | Product fail-closed and Plan lifecycle `DEC-109...DEC-111`; no upstream Request-state model exists, so this remains working/JIT evidence. |
| **Attempt execution/outcome separation and crash recovery** | `HSP-WD-007`, `HSP-WD-012` | `HSP-PT-002`, `HSP-PT-003`, `HSP-PT-020` | Architecture §8.1–8.2; `DEC-109`; Operating Model current-authority revalidation. |
| **Generation Input Basis / minimum necessary** | `HSP-WD-008`, `HSP-WD-013`, `HSP-WD-014`, `HSP-WD-018` | `HSP-PT-001`, `HSP-PT-007`, `HSP-PT-010`, `HSP-PT-021` | `DEC-108` explainability, `DEC-119` delivered translation-version provenance, Domain Map §6.6, Architecture minimum-data/privacy rules. |
| **Result provenance distinct from input basis** | `HSP-WD-024` | `HSP-PT-007`, `HSP-PT-008`, `HSP-PT-017` | `DEC-108`, `DEC-118...DEC-121`; Plans and Content ownership; Architecture versioned/provenance doctrine. |
| **Hard constraints vs soft preferences / unfulfillable** | `HSP-WD-014...016` | `HSP-PT-015`, `HSP-PT-021` | `DEC-083`, `DEC-096...DEC-109`, `DEC-116`; FP-005 OQ-010 gate. |
| **Entitlement admission/claim/consumption separation** | `HSP-WD-023`, `HSP-WD-031` | `HSP-PT-006`, `HSP-PT-017`, `HSP-PT-018`, `HSP-PT-020` | `DEC-109`; Domain Map §6.11 Entitlements and §6.10 Commerce; Architecture cross-domain durable consequence/idempotency. |
| **Fulfilment = final governed delivery, not generation** | `HSP-WD-031` (supersedes older HSP-WD-010/011 shorthand) | `HSP-PT-017`, `HSP-PT-020` | `DEC-110` generated/review/approval/active states; `DEC-111` activation revalidation; Product refund wording exposes separate commercial boundary. |
| **Plan safety pause vs withdrawal** | `HSP-WD-025`, `HSP-WD-026` | `HSP-PT-008`, `HSP-PT-009` | `DEC-089`, `DEC-110`, `DEC-111`, `DEC-121`; Safety/Plans ownership. |
| **Ordinary supersession vs withdrawal** | `HSP-WD-024...026` | `HSP-PT-007`, `HSP-PT-008` | Product/Operating Content lifecycle distinguishes superseded/withdrawn; `DEC-121`; Operating Model §13. Exact in-flight ordinary-supersession policy remains JIT. |
| **Professional Care uses one Safety gateway** | `HSP-WD-021`, `HSP-WD-022`, `HSP-WD-031` | `HSP-PT-013`, `HSP-PT-016...018` | `DEC-091...DEC-093`, `DEC-117`, `DEC-229`; Domain Map §6.14 + cross-domain table; Roadmap FP-012 later. |
| **Same-lineage successor concurrency** | `HSP-WD-032` | `HSP-PT-019`, `HSP-PT-020` | `DEC-110` superseded lifecycle, `DEC-117` immutable practitioner-derived versions; Architecture §8.1 concurrency invariant; Plans Domain §6.6. |
| **Participant-owned in-flight edits / applicability semantics** | `HSP-WD-033` | `HSP-PT-021` | `DEC-038`, `DEC-083`, `DEC-108`, `DEC-116`; open `HSP-UPD-008`. |
| **Frequent progress logging ≠ Plan adjustment cadence** | upstream-derived v0.41 consolidation; compatible with `HSP-WD-014`, `HSP-WD-033` | `HSP-PT-022` | `DEC-087`; `DEC-112...DEC-115`; `00_PLATFORM_v1.3.0` progress rules; Roadmap FP-005 basic feedback vs FP-010 recurring adjustment. |
| **Review entitlement ≠ guaranteed generation/change** | existing Product rule carried into compression | `HSP-PT-022` | `DEC-042`, `DEC-112...DEC-115`; Roadmap FP-010 gates `OQ-003`, `OQ-011`, `OQ-012`. |
| **Correction/replacement ≠ later re-personalisation** | `HSP-WD-029`, `HSP-WD-030`, `HSP-WD-033` | `HSP-PT-008`, `HSP-PT-022` | `DEC-037`, `DEC-038`, `DEC-121`; Plan correction/safety replacement without new entitlement vs later repersonalisation requiring qualifying right. |
| **Immutability while retained ≠ indefinite retention** | `HSP-WD-030` | `HSP-PT-014`, `HSP-PT-020` | `DEC-225`, `DEC-226`, `DEC-229`; Architecture §11; OQ-009/OQ-029/OQ-033. |
| **One-tab/LiveView coordination is UX only** | `HSP-WD-009` | `HSP-PT-003`, `HSP-PT-019`, `HSP-PT-020` | Architecture §4.1 LiveView projections/untrusted intent; §8.1 concurrency; Operating Model work/authority separation. |
| **Fail-closed and all-or-nothing** | `HSP-WD-004...008`, `HSP-WD-015...016`, `HSP-WD-031` | `HSP-PT-001`, `HSP-PT-003`, `HSP-PT-007`, `HSP-PT-011`, `HSP-PT-015`, `HSP-PT-017`, `HSP-PT-020` | `DEC-109`; Architecture executive degradation doctrine; FP-004/FP-005 validation/exit conditions. |

## Current Roadmap gate trace

### FP-004

Current `05_ROADMAP_v1.1.0` classifies:

- `OQ-005` — **BLOCKS_THIS_FP**
- `OQ-008` — **BLOCKS_THIS_FP**
- `OQ-007` — **FUTURE_ONLY** unless lab inputs are introduced
- `OQ-009` / `OQ-029` — **BLOCKS_RELEASE_ONLY**
- `OQ-033` — **NON_BLOCKING_FOR_THIS_FP**

### FP-005

Current Roadmap classifies:

- `OQ-010` — **BLOCKS_THIS_FP**
- `OQ-013` — **BLOCKS_THIS_FP**
- `OQ-016` — **BLOCKS_RELEASE_ONLY**
- `OQ-014` — **NON_BLOCKING_FOR_THIS_FP**
- `OQ-011` / `OQ-012` — **FUTURE_ONLY** for recurring adjustment

The HSP consolidation adds no new clinical gate. It only identifies the two unresolved Product/commercial seams that must not be invented when FP-005 freezes its contract: `HSP-UPD-005` and `HSP-UPD-008`.

## Hypothesis provenance

Resolved working hypotheses are not left open:

- `HSP-WH-001 → HSP-WD-021`
- `HSP-WH-002 → HSP-WD-023`
- `HSP-WH-004 → HSP-WD-024`
- `HSP-WH-005 → HSP-WD-025`
- `HSP-WH-006 → HSP-WD-026`
- `HSP-WH-007 → HSP-WD-027`
- `HSP-WH-008 → HSP-WD-028`
- `HSP-WH-009 → HSP-WD-029`
- `HSP-WH-010 → HSP-WD-030`
- `HSP-WH-011 → HSP-WD-031`
- `HSP-WH-012 → HSP-WD-032`
- `HSP-WH-013 → HSP-WD-033`

`HSP-WH-003` remains only as historical preferred-direction evidence for the unresolved Product policy in `HSP-UPD-001`; it is not normative in the compressed contract.
