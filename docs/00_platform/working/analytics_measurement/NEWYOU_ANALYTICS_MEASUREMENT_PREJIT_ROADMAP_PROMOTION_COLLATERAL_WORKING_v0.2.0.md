# NewYou Analytics & Measurement Pre-JIT — Roadmap Promotion Collateral Working v0.2.0

```text
WORKING / NON-AUTHORITATIVE
PROMOTION COLLATERAL CONTRACT
IMPLEMENTATION NOT AUTHORISED
CURRENT PROMOTION STATE: BLOCKED / STOP
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_ROADMAP_PROMOTION_COLLATERAL_WORKING_v0.1.0.md` — preserved unchanged.
- **Source discovery:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.8.0.md`.
- **Roadmap candidate blob:** `ddff1c2fa34b3b9185bef8eb72e49f8513479887`.
- **Roadmap candidate SHA-256:** `bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261`.

---

## 1. Purpose

This successor refines the Pass-7 promotion-collateral contract using fresh Foundation Integrity evidence. It does not change the accepted `ANL-UPD-001` Roadmap semantics. It records the **actual minimum repository promotion surface** required by current integrity rules and distinguishes semantic authority changes from routing/tooling maintenance.

---

## 2. Semantic authority payload — unchanged

The sole semantic authority change remains:

- `05_ROADMAP_v1.3.0.md` — accepted nine-location bounded FP-006 Research & Feedback activation.
- `archive/05_ROADMAP_v1.2.0.md` — exact byte-preserved predecessor.

No Product Law, Decision Register, Domain Law or Architecture semantic change is required.

---

## 3. Exact integrity pins

```text
Roadmap v1.3.0 git blob:
ddff1c2fa34b3b9185bef8eb72e49f8513479887

Roadmap v1.3.0 SHA-256:
bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261

Roadmap v1.2.0 predecessor git blob:
5432991071d4d1a7cbd9dc4c8fca48c823129f40

Roadmap v1.2.0 predecessor SHA-256:
601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0

Open Work v1.2.59 predecessor SHA-256:
a3aaada01b6917903d5b9a7fd1236d253a0906c45c5cd06498fa6b91182b721f

Isolated generated Open Work v1.2.60 SHA-256:
56f64e1ad32533acd2f0da247b6f95f00582dfadee52df7b781eaf8ef58c6ca4
```

The Open Work v1.2.60 digest remains a generated-candidate value, not current authority, until the complete package is rebuilt and passes the full gate.

---

## 4. Minimum merge-ready promotion package after Pass 8 evidence

### 4.1 Authority and status/routing files

1. `docs/00_platform/05_ROADMAP_v1.3.0.md` — semantic authority successor.
2. `docs/00_platform/archive/05_ROADMAP_v1.2.0.md` — exact predecessor.
3. `docs/00_platform/README.md` — current default route only.
4. `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` — current Roadmap/Open Work records plus direct historical predecessors and exact hashes.
5. `docs/00_platform/02_OPEN_WORK_v1.2.60.md` — planning-status successor only.
6. `docs/00_platform/archive/02_OPEN_WORK_v1.2.59.md` — exact predecessor.

### 4.2 Active routing artifacts required by current integrity rules

7. Current Delivery Atlas working successor or equivalent routing-only correction:
   - change only current source routes from Roadmap v1.2.0/Open Work v1.2.59 to v1.3.0/v1.2.60;
   - preserve `DERIVED / NON-AUTHORITATIVE` status and all Feature Pack/capability semantics unless a separate governed reconciliation later authorises semantic derivation updates.

8. Current HARDEN-02 working status/routing successor or equivalent routing-only correction:
   - update only `CURRENT AUTHORITY` source routes to Roadmap v1.3.0/Open Work v1.2.60;
   - preserve the certified v0.4.0 semantics, HARDEN execution/certification evidence, current Communications/conditional-dossier state, Phase 7C STOP, proof STOP and implementation STOP.

### 4.3 Foundation Integrity / regression maintenance

9. Update `tools/foundation_integrity_audit.py` only where current-route lifecycle checks are hard-pinned to the outgoing Open Work/Roadmap versions.
10. Update affected tests, including `tests/test_roadmap_routing_resilience.py`, so the suite continues to fail closed against stale/incorrect routing while accepting the legitimate semantic Roadmap successor.
11. Inspect other executable test pins to outgoing current versions and change only those that represent **current-route expectations**, never historical/source-at-freeze evidence.

---

## 5. Required anti-drift rules for the tooling correction

The next correction pass must satisfy all of these:

1. Do not weaken SHA-256, archive, SemVer or current-route checks.
2. Prefer deriving current Open Work/Roadmap routes from the manifest/README rather than embedding a perpetual filename constant where feasible.
3. Where a test exists specifically to certify a named historical successor, keep the historical pin.
4. Do not rewrite archived documents or source-at-freeze citations.
5. Do not make Delivery Atlas or HARDEN-02 a new authority layer.
6. Do not change current FP-001 programme state.
7. Do not change `Analytics NOT REQUIRED` for the current FP-001 conditional-dossier programme.
8. Do not authorise Phase 7C, proof classification, Phase 8 or implementation.
9. Do not broaden `ANL-UPD-001` beyond the bounded FP-006 Research instrument.
10. Rerun the full unit-test suite and Foundation Integrity against the exact final candidate head.

---

## 6. Pass-8 verification result

The isolated candidate generation proved that the intended Roadmap/Open Work manifest records and archive hashes are individually coherent. Foundation Integrity nevertheless failed because the promotion package omitted current-route and regression-contract maintenance that the repository deliberately enforces.

Therefore:

```text
ROADMAP SEMANTICS: PASS / WORKING_LOCKED
ROADMAP BYTE HASH: PASS / PROVEN
README + MANIFEST + OPEN WORK ONLY: INSUFFICIENT
ACTIVE ATLAS/HARDEN CURRENT-ROUTE SYNC: REQUIRED
FOUNDATION INTEGRITY CURRENT-VERSION TEST MAINTENANCE: REQUIRED
PROMOTION: BLOCKED / STOP
PR: NOT OPENED
MAIN: UNCHANGED
IMPLEMENTATION: UNAUTHORISED
```

---

## 7. Explicit non-changes

This refinement does not authorise or require:

- Product/Decision/Domain/Architecture semantic amendments;
- a Research Feature Pack;
- FP-005 ownership changes;
- Voting activation;
- FP-016 experimentation;
- a new OQ by fiat;
- provider/package selection;
- response identity mode;
- retention/deletion policy selection;
- Resource/schema/event design;
- proof classification;
- application implementation.

---

## 8. Promotion gate after this successor

`ANL-UPD-001` may be treated as Roadmap-resolved only after a later focused correction/promotion pass:

1. updates the required current-route/tooling collateral without semantic drift;
2. regenerates exact README/manifest/Open Work successor bytes;
3. proves all hashes and archive preservation;
4. runs the complete unit-test suite successfully;
5. runs Foundation Integrity with zero findings;
6. independently reviews the exact resulting candidate head;
7. still stops before PR/merge unless separately authorised.

Until then:

```text
ANL-GAP-001 = UPSTREAM_ACTION_REQUIRED
ANL-GAP-002 = OPEN / UPSTREAM_ACTION_REQUIRED
ANL-UPD-001 = EXACT SEMANTIC CANDIDATE HASHED / PROMOTION BLOCKED
CURRENT LIVE ROADMAP = v1.2.0
CURRENT LIVE OPEN WORK = v1.2.59
FP-006 SURVEY JIT/IMPLEMENTATION = BLOCKED AT ROADMAP AUTHORITY
```
