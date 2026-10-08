# NewYou Audit & Evidence Evidence Index — Working v0.1.3

```text
WORKING / NON-AUTHORITATIVE
TRACEABILITY INDEX
SUPERSEDES COMPACT v0.1.2
```

- **Prepared / re-reviewed:** 2026-10-08
- **Live repository baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Discovery ledger:** `NEWYOU_AUDIT_EVIDENCE_PREJIT_DISCOVERY_WORKING_v0.6.2.md`
- **Discovery SHA-256:** `6a82725d71a8b861d8be88711bba209a3ad390739c195f69fc0560c1d95bfc91`

## 1. Live governing/current sources checked

1. `docs/00_platform/README.md` — authority routing and active FP-001 state.
2. `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` — machine-readable current authority/deep-reference inventory.
3. `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
4. `docs/00_platform/00_PLATFORM_v1.6.0.md`
5. `docs/00_platform/01_DECISIONS_v1.6.0.md`
6. `docs/00_platform/02_OPEN_WORK_v1.2.59.md`
7. `docs/00_platform/03_ARCHITECTURE_v1.1.1.md`
8. `docs/00_platform/04_DOMAIN_MAP_v1.2.0.md`
9. `docs/00_platform/05_ROADMAP_v1.2.0.md`
10. `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md`
11. `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` where operator/front-end implications were relevant.

## 2. Live reference/supporting sources checked

1. `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`
2. `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`
3. `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`
4. `docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md`

The v0.1.0 compact Evidence Index incorrectly omitted the `reference/` path segment for Engineering Standards. This successor corrects it.

## 3. Current FP-001 working sources checked

- `docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md`
- `docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md`
- `docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md`

Key boundary:

> Identity owns Account/verification/recovery/security truth; Communications owns message intent/delivery/provider evidence; Audit owns only selected minimum cross-cutting evidence.

## 4. Supporting non-authoritative Pre-JIT inputs

Used only where compatible with live higher authority:

- Privacy / Consent / Data Lifecycle Pre-JIT
- Commerce / Entitlements / Recurring Membership Pre-JIT
- Health / Safety / Plans Pre-JIT
- Content & Media Pre-JIT
- Communications Pre-JIT

## 5. Discovery-decision trace

| Range | Subject |
|---|---|
| `AE-WD-001..006` | required evidence, E1/E2/E3, proof truthfulness, fail-closed privileged disclosure |
| `AE-WD-007..012` | identity/idempotency/exactly-once/correction/evidence authority |
| `AE-WD-013..020` | evidence envelope, minimisation, Audit access, audit-of-audit, retained linkage |
| `AE-WD-021..028` | retention, hold, disposition and independent lifecycle dimensions |
| `AE-WD-029..037` | source corrections, provider disorder and restore reconciliation |
| `AE-WD-038..050` | immutability/tamper resistance/operator powers/export/integrity/correction |
| `AE-WD-051..059` | FP-001 event-selection and criticality |
| `AE-WD-060..065` | FLOW-01 crash/race semantics and FP-001 dossier `REQUIRED` |
| `AE-WD-066..069` | Commerce/Health/Safety generalisation |
| `AE-WD-070..074` | downstream routing and Pre-JIT completeness |

## 6. Mechanism trace

- `AE-MECH-001` — Ash Temporal Resources are a JIT candidate only; current working preference is not to assume them for the core Audit ledger.
- `AE-MECH-002` — cryptographic chaining/signatures/Merkle/WORM/dedicated append-only services are JIT candidates only.

## 7. Supersession/current-state trace

- Historical section `FP-001 Audit dossier adjudication — NOT YET FINAL` records an earlier pass-state only.
- `AE-WH-001` is the historical provisional hypothesis.
- `AE-WD-065` is current working doctrine: **FP-001 Audit & Evidence JIT Domain Dossier = REQUIRED**.
- Discovery v0.6.1 corrects historical dual-primary routing labels without changing decision semantics.
- Compact pack v0.1.2 supersedes compact v0.1.0 because the first compression omitted accepted semantics.

## 7A. Programme-status precedence trace

At baseline `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`:

- `AE-WD-065` is the **working Pre-JIT adjudication**: Audit & Evidence JIT dossier `REQUIRED`.
- `README.md` / `02_OPEN_WORK_v1.2.59.md` remain the **governed programme status**: Audit & Evidence `CONDITIONAL / PENDING EXPLICIT ADJUDICATION`.
- Phase 7C remains `BLOCKED / NOT_STARTED`.

The working pack cannot promote itself. An explicit governed adjudication/current-status successor is required to change programme state.

## 7B. Upstream-scope trace

The completeness statement is Audit-scoped:

> **No unresolved Audit-specific Product or Architecture amendment prerequisite has been identified.**

Separately governed upstream gaps in participating Domains are outside this pack's authority and remain binding.

## 8. External ecosystem evidence snapshot

Official HexDocs was rechecked on 2026-10-08 for Ash Temporal Resources.

At that snapshot:
- the Ash guide marked Temporal Resources experimental;
- production AshPostgres use required PostgreSQL 18+;
- package/API details remain subject to change.

This evidence informs the JIT deferral only. It is not a package pin or Architecture authority.

## 9. Canonicality warning

This index is traceability/navigation only. It creates no Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority.
