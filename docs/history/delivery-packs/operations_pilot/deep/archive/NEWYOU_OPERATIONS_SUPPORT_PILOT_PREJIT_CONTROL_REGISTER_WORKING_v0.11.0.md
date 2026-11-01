# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.11.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.11.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact current `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_CONTROL_REGISTER_WORKING_v0.10.0.md`
- **Latest semantic discovery:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.14.0.md`
- **Semantic pressure tests:** `OPS-PT-001...210`
- **Bounded change:** `OPS-UPD-004` exact cumulative v1.7 materialisation + diff/integrity review only.
- **No new semantic IDs:** no new `OPS-PT`, `OPS-UPD`, or `OPS-GAP`.
- **Current authority modification:** NONE. README/manifest still route Product/Decisions v1.6.

---

# 1. Inherited state

All unchanged v0.10.0 classifications and working locks remain inherited.

Current upstream deltas remain exactly `OPS-UPD-001...007`. `OPS-UPD-004` remains the serial STOP before `OPS-UPD-001` promotion work proceeds.

---

# 2. Clean authority-materialisation branch

A dedicated branch isolates the Product/Decision candidate from the long-lived discovery history:

```text
branch = authority/ops-upd-004-assessment-credit-v1.7.0
base/main = 086ade7b28c000de1c387acb9760e5eb08bb0413
candidate head = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
ahead = 1
behind = 0
```

The one candidate commit adds exactly:

1. `docs/00_platform/working/operations_pilot/authority_candidates/00_PLATFORM_v1.7.0.md`;
2. `docs/00_platform/working/operations_pilot/authority_candidates/01_DECISIONS_v1.7.0.md`;
3. `tests/test_ops_upd_004_authority_materialization.py`.

It does not mutate README, the authority manifest, current authority paths, Roadmap, Architecture or Domain Law.

---

# 3. Materialised candidate review

The cumulative Product/Decision candidates implement the corrected v0.2.0 promotion contract:

- Product §21B.3: first-answer save **claims/holds** the existing credit and does not consume it;
- Product §21R.6: separates credit state from attempt/result/report state and governs qualifying delivery, expiry closure, technical recovery/refund and exactly-once consumption;
- ownership remains: Temperament owns attempt/result/report truth; Entitlements owns credit/right truth; Identity & Access governs access assurance;
- Product §24 is internally consistent as a prospective v1.7 candidate;
- `DEC-055` preserves its historical wording and becomes `SUPERSEDED BY DEC-313`;
- `DEC-313` uses `DEC-034` for the annual retake boundary and limits supersession to assessment-credit claim/closure/consumption semantics;
- no Roadmap semantic successor is introduced.

Document-level disposition: **PASS**.

---

# 4. Full-file deterministic integrity coverage

The candidate commit already contains `tests/test_ops_upd_004_authority_materialization.py`.

It:

- pins source Git blob SHAs:
  - Product v1.6 = `bb98081841b432a5a3d5e961929acf494ac9c8ba`;
  - Decisions v1.6 = `85402cb169e095771f03482981d0691e08efb021`;
- reverses every permitted Product v1.7 delta and requires byte-for-byte equality with `00_PLATFORM_v1.6.0.md`;
- reverses every permitted Decisions v1.7 delta and requires byte-for-byte equality with `01_DECISIONS_v1.6.0.md`;
- rejects the old first-answer consumption pair from the Product candidate;
- requires exactly one `DEC-313` and explicit `DEC-055` supersession;
- verifies owner/lifecycle boundaries and `DEC-034`;
- requires README/manifest to remain on v1.6 before promotion;
- requires DEC identifiers to remain contiguous through 313.

A duplicate review test briefly created during this pass was removed with a lease-protected ref reset. The authority branch is again exactly the single candidate commit at `feaacff6...`.

---

# 5. Exact-head CI hard gate

The repository's `Foundation Integrity` workflow runs:

```text
python -m unittest discover -s tests -v
python tools/foundation_integrity_audit.py --manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json
```

The workflow triggers on:

- pull request;
- push to `main`;
- explicit `workflow_dispatch` with an exact SHA.

At `feaacff6fb0ca05ed7c0a341852b8f114483dcb7`:

```text
exact-head workflow runs = NONE
open PR from authority branch = NONE
```

The available GitHub connector can inspect/re-run existing workflows but cannot initiate a fresh `workflow_dispatch`. No PR is opened without explicit user authorisation.

Therefore this pass cannot truthfully certify exact-head CI.

---

# 6. Current disposition

```text
MATERIALISED CUMULATIVE PRODUCT v1.7.0: PRESENT
MATERIALISED CUMULATIVE DECISIONS v1.7.0 / DEC-313: PRESENT
DOCUMENT-LEVEL INDEPENDENT REVIEW: PASS
FULL-FILE DETERMINISTIC REGRESSION TESTS: PRESENT / REVIEWED
CURRENT README/MANIFEST ROUTING: v1.6 / UNCHANGED
ROADMAP SEMANTIC SUCCESSOR: NOT JUSTIFIED
ARCHITECTURE AMENDMENT: NOT JUSTIFIED
DOMAIN MAP AMENDMENT: NOT JUSTIFIED
EXACT-HEAD FOUNDATION INTEGRITY CI: NOT RUN / REQUIRED
AUTHORITY PROMOTION: BLOCKED / STOP
OPS-UPD-004: CONFLICT_STOP REMAINS
OPS-GAP-010: OPEN / CONFLICT_STOP
IMPLEMENTATION: NOT AUTHORISED TO CHOOSE A RULE
BROAD PRE-JIT FREEZE: NOT READY
```

No claim is made that v1.7 is current authority.

---

# 7. Next exact action

Obtain Foundation Integrity on exact candidate SHA:

`feaacff6fb0ca05ed7c0a341852b8f114483dcb7`

Either:

1. explicitly authorise opening a PR from `authority/ops-upd-004-assessment-credit-v1.7.0` to `main` so the normal PR workflow runs; or
2. manually run the `Foundation Integrity` workflow via `workflow_dispatch`, supplying that exact SHA.

After a passing exact-head run, independently review that same SHA and CI evidence before any archive/routing/promotion pass begins.

Do not begin `OPS-UPD-001` before this gate is resolved unless the user explicitly changes the serial order.
