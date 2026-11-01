# Privacy / Consent Pre-JIT Evidence Index — Working v0.1.3

- **Status:** WORKING / NON-AUTHORITATIVE INDEX
- **v0.1.3 hygiene patch:** Repairs traceability hygiene only: previously unqualified Privacy-delta references are restored to their full `PRIV-UPD-*` identifiers, abbreviated OQ references are fully namespaced, and compact-pack version references are aligned to v0.1.3. PT/WD/UPD meaning and authority classifications are unchanged.
- **Purpose:** Route future JIT reviewers from the compact Privacy contract to exact detailed discovery evidence without reloading the full cumulative file by default.
- **Live authority baseline:** `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`
- **Detailed source:** `PRIVACY_CONSENT_PREJIT_DISCOVERY_WORKING_v0.12.1.md`
- **Detailed source SHA-256:** `f28d9c1e1875a90c6797d6e058a0f043da77e5641993baa02219a25fa13536e6`
- **Compression audit:** `NEWYOU_PRIVACY_PREJIT_COMPRESSION_AUDIT_WORKING_v0.1.3.md`
- **Implementation:** NOT AUTHORISED.

## 1. Artifact hierarchy

Use:

```text
live governed NewYou authority
→ compact Privacy Pre-JIT contract
→ delta register / evidence index
→ detailed cumulative Privacy discovery when exact reasoning is needed
```

The compact artifacts are navigation/planning evidence only.

## 2. Current live authority routing

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.39.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.1.1.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when frontend/experience is in scope.

Deep references only when exact source tracing is needed:

- `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`
- `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`
- `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`
- `reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md`

## 3. Pressure-test index

| PT | Verdict | Main subject | Contract route | Additional dependency |
|---|---|---|---|---|
| `PRIV-PT-001` | PASS | deletion vs concurrent writes | §§5–6, 12.1 | none |
| `PRIV-PT-002` | PASS | pre-deletion backup restore | §8.4, §12.3 | `OQ-031`, `OQ-037` |
| `PRIV-PT-003` | PASS | purpose-specific withdrawal in flight | §5, §12.1 | legal basis expert decision where applicable |
| `PRIV-PT-004` | PASS | stale/duplicate/reordered async | §§5–6, §12.1 | none |
| `PRIV-PT-005` | CHANGES REQUIRED | export races deletion/mutation | §§7, 10–12 | `PRIV-WD-001`, `PRIV-UPD-001`, `OQ-032` |
| `PRIV-PT-006` | PASS | processor unavailable/delayed | §§6.2, 8, 12.2 | `OQ-029`, `OQ-030`, `OQ-032` |
| `PRIV-PT-007` | PASS | scoped legal hold during deletion | §8.2, §12.5 | legal/privacy authority |
| `PRIV-PT-008` | PASS | Health/Safety/Plan vs professional retention | §§6.3, 9, 12.7 | `HSP-UPD-004`, `OQ-009`, `OQ-029`, `OQ-033` |
| `PRIV-PT-009` | PASS | retained Commerce/Audit non-reconstruction | §§6.4, 9, 12.8 | `CER-PT-001` |
| `PRIV-PT-010` | PASS | pseudonymous data re-identifiability | §8.3, §12.6 | anonymisation expert threshold |
| `PRIV-PT-011` | PASS | closure/reopen/deletion/new Account | §6.5, §12.9 | Identity current authority |
| `PRIV-PT-012` | PASS | mixed-category export | §7, §12.4 | `OQ-032`, `OQ-033` |
| `PRIV-PT-013` | CHANGES REQUIRED | deletion vs recurring/refund/dispute | §§6.4, 10–12 | `PRIV-WD-002`, `PRIV-UPD-002`, `CER-PT-004`, `OQ-004` |
| `PRIV-PT-014` | CHANGES REQUIRED | identity reconciliation vs deletion | §§6.5, 10–12 | `PRIV-WD-003`; JIT/governance-first delta |
| `PRIV-PT-015` | CHANGES REQUIRED | Community/moderation/Security after deletion | §§6.6, 10–12 | `PRIV-WD-004`, `PRIV-UPD-004`, `OQ-023` |

## 4. Working doctrine index

| WD | Origin | Contract route | Authority status |
|---|---|---|---|
| `PRIV-WD-001` | PT-005 | §10 | accepted working doctrine only |
| `PRIV-WD-002` | PT-013 | §10 | accepted working doctrine only |
| `PRIV-WD-003` | PT-014 | §10 | accepted working doctrine only |
| `PRIV-WD-004` | PT-015 | §10 | accepted working doctrine only |

Exact wording remains in the compact contract and detailed source.

## 5. Delta index

| Delta | Classification | Register route |
|---|---|---|
| `PRIV-UPD-001` | upstream Product/Privacy policy | Delta Register §`PRIV-UPD-001` |
| `PRIV-UPD-002` | upstream Product/Commerce policy + CER/provider | Delta Register §`PRIV-UPD-002` |
| `PRIV-UPD-003` | JIT/governance first; Product escalation conditional | Delta Register §`PRIV-UPD-003` |
| `PRIV-UPD-004` | upstream Product/Trust & Safety policy | Delta Register §`PRIV-UPD-004` |

## 6. Cross-stream evidence

### HSP

Current live working suite is `v0.1.3`.

Most relevant:

- `NEWYOU_HSP_PREJIT_CONTRACT_WORKING_v0.1.3.md`
- `NEWYOU_HSP_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.3.md`
- `NEWYOU_HSP_COMPRESSION_AUDIT_WORKING_v0.1.3.md`
- `NEWYOU_HSP_EVIDENCE_INDEX_WORKING_v0.1.3.md`

Use `HSP-UPD-004` for category-specific full-deletion treatment. Do not duplicate it.

### CER

Current live working discovery:

- `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.1.0.md`

Relevant accepted findings:

- `CER-PT-001` — commercial success and Entitlement consequence separation;
- `CER-PT-004` — stable logical recurring-collection identity across retries/reconciliation.

CER remains working/non-authoritative.

## 7. Existing gate routing

| Gate | Privacy relevance |
|---|---|
| `OQ-004` | recurring billing/refund/chargeback provider semantics |
| `OQ-009` | Health/professional retention umbrella |
| `OQ-018` | journal encryption/retention |
| `OQ-021` | recording/video consent/retention |
| `OQ-023` | Facebook moderation/privacy operations |
| `OQ-029` | retention schedule matrix |
| `OQ-030` | external processor deletion/export inventory |
| `OQ-031` | backup restore/deletion replay |
| `OQ-032` | export/deletion operational contract |
| `OQ-033` | professional record authority/access boundary |
| `OQ-037` | RPO/RTO |
| `OQ-038` | incident ownership |
| `OQ-040` | experimentation privacy/deletion proof |

Adjacent:

- `OQ-035` abuse-control thresholds where relevant to Security/anti-abuse proof; does not define sanction scope.

## 8. Mechanical coverage checks

At creation:

- accepted PT headings: **15** (`001...015`);
- accepted WD identifiers: **4** (`001...004`);
- working delta identifiers: **4** (`001...004`);
- code fences in detailed source: balanced;
- top-level numbered sections in detailed source: contiguous;
- live root: no `mix.exs` at audited SHA.

## 9. When to reopen detailed discovery

Load the cumulative detailed file only when:

- exact PT reasoning/provenance is required;
- a working doctrine is challenged;
- a live authority change may conflict;
- a new JIT scenario is not answered by the compact contract;
- a legal/vendor/expert result changes assumptions;
- a cross-stream HSP/CER conclusion changes.

Do not reopen broad discovery merely because implementation detail is still undecided.
