# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.8.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 8 ONLY — PROMOTION HASH RESOLUTION + FOUNDATION-INTEGRITY STOP
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-pass branch head:** `732b596e376b74d52e4f5bddaf3823047621d5c0`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.7.0.md` — preserved unchanged.
- **Accepted predecessor result:** Pass 7 accepted by human review.
- **Purpose:** resolve the exact Roadmap v1.3.0 SHA-256 blocker, assemble the intended authority-routing collateral in an isolated verification workspace, run the repository's own Foundation Integrity gate, and stop if that gate proves additional correction scope is required.
- **Scope boundary:** no PR, no merge, no `main` mutation, no FP-006 JIT, no metric design, no privacy/provider/schema design.

---

## 1. Pass-7 acceptance lock

Human acceptance of Pass 7 locks the following working findings:

- exact Roadmap v1.3.0 semantic candidate blob: `ddff1c2fa34b3b9185bef8eb72e49f8513479887`;
- exact candidate commit: `25cef5c3eb6462292cb5c34fff2e4c59d3be2078`;
- semantic diff: accepted nine-location `ANL-UPD-001` patch only, plus lifecycle metadata;
- exact current v1.2.0 predecessor preserved at `archive/05_ROADMAP_v1.2.0.md`, blob `5432991071d4d1a7cbd9dc4c8fca48c823129f40`;
- promotion must fail closed until SHA-256 and complete repository routing/integrity are proven.

These findings remain working-locked.

---

## 2. ANL-PT-024 — Can the exact candidate SHA-256 be proven without weakening the manifest contract?

**Measurement / governance question:** Is there a reproducible repository-native route to compute SHA-256 over the exact candidate bytes rather than substituting Git SHA-1 or a guessed value?

**Scenario:** A temporary isolated verification branch checked out the exact Analytics candidate and ran `git hash-object` plus `sha256sum` against `docs/00_platform/05_ROADMAP_v1.3.0.md`.

**Evidence:** GitHub Actions run `38041940588`, job `114183756629` reported:

```text
candidate blob: ddff1c2fa34b3b9185bef8eb72e49f8513479887
candidate SHA-256: bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261
archive predecessor blob: 5432991071d4d1a7cbd9dc4c8fca48c823129f40
```

The temporary branch was reset afterwards so the one-purpose verification workflow is not part of the Analytics candidate history.

**Analysis:** The byte-integrity blocker from Pass 7 is resolved. The SHA-256 is tied to the already-reviewed git blob and was computed by repository checkout, not transcribed from prose.

**Disposition:** `PASS`.

**Working lock:** Roadmap v1.3.0 candidate SHA-256 = `bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261`.

---

## 3. Intended promotion collateral assembled in isolated verification workspace

A fail-closed generation run prepared, but did not commit, the following intended promotion state:

1. README default authority route: Open Work v1.2.60 and Roadmap v1.3.0.
2. Archive exact `02_OPEN_WORK_v1.2.59.md` predecessor.
3. Create `02_OPEN_WORK_v1.2.60.md` as a planning-status successor that records only the bounded Roadmap activation and preserves the current FP-001 / Phase-7 STOP state.
4. Manifest current `ROADMAP` → v1.3.0 with exact candidate SHA-256.
5. Manifest current `OPEN_WORK` → v1.2.60 with generated exact SHA-256.
6. Add direct historical manifest entries for Roadmap v1.2.0 and Open Work v1.2.59.

Exact generated hashes from the verification workspace:

```text
ROADMAP v1.3.0 SHA-256:
bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261

OPEN WORK v1.2.59 predecessor SHA-256:
a3aaada01b6917903d5b9a7fd1236d253a0906c45c5cd06498fa6b91182b721f

GENERATED OPEN WORK v1.2.60 SHA-256:
56f64e1ad32533acd2f0da247b6f95f00582dfadee52df7b781eaf8ef58c6ca4
```

These values describe the isolated generated candidate only. Because the repository integrity gate failed before commit/push, no claim is made that Open Work v1.2.60 is frozen/current.

---

## 4. ANL-PT-025 — Are Roadmap + README + manifest + Open Work sufficient promotion collateral under the actual repository integrity contract?

**Question:** Can the promotion package stop at the semantic authority successor plus the three routing/status files assumed in Pass 5?

**Scenario:** Run the production `tools/foundation_integrity_audit.py` against the isolated generated promotion workspace.

**Observed result:** `FAIL`, with 571 assertions evaluated. The Roadmap/Open Work path, SemVer, archive and SHA checks passed, but `current_authority_route_resolution` failed because two active working artifacts explicitly route the old current sources:

- `working/DELIVERY_ATLAS_WORKING_v0.4.1.md` still routes Roadmap v1.2.0 and Open Work v1.2.59;
- `working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md` still declares those same files in its `CURRENT AUTHORITY` table.

**Analysis:** Pass 5 correctly classified Atlas as derived/non-authoritative, but the repository's integrity rules intentionally require active explicit current-source routes to resolve to the manifest. Therefore Atlas routing reconciliation is not semantic authority promotion, yet it is mechanically required collateral for a green authority promotion. HARDEN-02 has the same routing-only requirement because its contract explicitly says live authority wins and it maintains a `CURRENT AUTHORITY` table.

**Disposition:** `NEEDS_WORKING_DELTA`.

**Refinement:** a merge-ready promotion candidate must include routing-only successors or equivalent governed routing corrections for the active Atlas and HARDEN-02 contract. Their certified/derived semantics and stage states must remain unchanged.

---

## 5. ANL-PT-026 — Can the Foundation Integrity / PMR reconciliation checks remain pinned to Open Work v1.2.59 and Roadmap v1.2.0 after a legitimate authority successor?

**Question:** Is the failing PMR/FIA result evidence that Roadmap v1.3.0 is invalid, or that the integrity test contract itself requires lifecycle maintenance?

**Observed repository facts:**

- `tools/foundation_integrity_audit.py` contains an FP-001 PMR reconciliation check that explicitly rejects a current Open Work path other than `docs/00_platform/02_OPEN_WORK_v1.2.59.md` and separately requires the current Delivery Atlas to name v1.2.59.
- `tests/test_roadmap_routing_resilience.py` defines `CURRENT_ROADMAP = .../05_ROADMAP_v1.2.0.md` and `OPEN_WORK = .../02_OPEN_WORK_v1.2.59.md`, then asserts those exact versions as current and asserts preservation properties tied to the prior Roadmap lifecycle.

**Analysis:** Those guards were valid regression protection for the current baseline. Once governance deliberately creates legitimate successors, the tests must be advanced with the authority lifecycle. Keeping them pinned would make the integrity suite itself a competing authority and permanently block lawful successor versions. Conversely, simply deleting the checks would weaken governance. The safe correction is to update them prospectively so they still fail closed while deriving current route/version from the manifest/README or explicitly validating the new successor lifecycle.

This is engineering-governance/toolchain maintenance, not Analytics semantics and not a reason to alter Product, Domain or Roadmap meaning.

**Disposition:** `NEEDS_WORKING_DELTA`.

**Stop consequence:** do not silently modify `tools/` or `tests/` inside Pass 8; that is a materially wider correction surface requiring its own focused review.

---

## 6. ANL-PT-027 — Should historical files and source-at-freeze citations be globally rewritten to the new current versions?

**Question:** Because repository search finds many v1.2.0/v1.2.59 references, should promotion replace all of them?

**Analysis:** No. Archive documents, historical lifecycle evidence, source-at-freeze citations and historical working evidence must remain unchanged. Only explicit **current routing** and executable regression expectations that are supposed to follow current authority are candidates for a successor/correction. Broad search-and-replace would destroy provenance.

**Disposition:** `PASS`.

**Working lock:** update current route contracts only; preserve historical/source-at-freeze references.

---

## 7. ANL-GAP-002 — Authority-promotion integrity/tooling lifecycle gap

**Classification:** `GOVERNANCE ROUTING + FOUNDATION INTEGRITY TOOLING GAP`.

**Finding:** The exact Roadmap v1.3.0 bytes and SHA-256 are now proven, but the repository cannot accept the promotion package as assembled under Pass 5 because active derived/governance routing artifacts and version-pinned integrity tests still encode the v1.2.0/v1.2.59 baseline.

**This is not:**

- a Product Law contradiction;
- a Domain ownership contradiction;
- an Architecture contradiction;
- a defect in the accepted nine-location Roadmap semantic patch.

**Status:** `OPEN / UPSTREAM_ACTION_REQUIRED` before authority promotion.

---

## 8. Pass-8 stop ruling

The required integrity gate exposed correction scope outside the accepted Pass-8 promotion package:

1. active Delivery Atlas current-source routing;
2. active HARDEN-02 current-authority routing;
3. Foundation Integrity / roadmap-routing regression expectations that are legitimately version-pinned to the outgoing baseline.

Changing those files is not a harmless continuation of README/manifest/Open Work routing. It modifies the repository's governance/tooling regression contract and therefore requires a separate focused pass.

**No generated authority collateral from the failed verification workspace was committed to the Analytics branch.**

---

## 9. Pass 8 disposition

**CHANGES REQUIRED / STOP — ROADMAP HASH BLOCKER RESOLVED; FOUNDATION INTEGRITY PROVES ADDITIONAL ROUTING/TOOLING COLLATERAL IS REQUIRED BEFORE PROMOTION.**

Current live authority remains Roadmap v1.2.0 / Open Work v1.2.59 on `main`.

The Roadmap v1.3.0 semantic candidate remains accepted working intent and byte-reviewed candidate material, but it is not current authority.

**Recommended next focused pass after human acceptance:** inspect and update only the current-route portions of Delivery Atlas/HARDEN-02 plus the minimum Foundation Integrity/tests needed to follow the legitimate Roadmap/Open Work successor; regenerate the same promotion collateral; run the full unit-test + Foundation Integrity gate; stop before PR/merge again.
