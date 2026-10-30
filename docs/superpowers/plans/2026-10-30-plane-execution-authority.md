# WELL-66 implementation plan — Plane execution authority

**Baseline:** `main@401a9a1660219580e6a95139bc89610f994f9349`  
**Branch:** `governance/well66-plane-execution-authority`  
**Plane:** WELL-66

## Contract

Implement the approved split in `docs/superpowers/specs/2026-10-30-plane-execution-authority-design.md` without changing Product, Architecture, Domain or Feature Pack semantics.

## Steps

1. Add a transition regression test that fails until the full authority split exists.
2. Open a draft PR and capture the expected RED CI result.
3. Add `docs/00_platform/reference/DELIVERY_GOVERNANCE_STANDARD_v1.0.0.md` as the supporting authority for Plane execution state, Ready-only agent execution, proportional planning, upstream-discovery escalation, Open Work retirement and semantic-only derived artifacts.
4. Add lean `docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json` containing current durable routes, supporting authority routes, Plane execution metadata, the final Open Work legacy snapshot and current semantic working routes.
5. Update `docs/00_platform/README.md` so agents route durable law through the lean router and obtain live execution state from Plane. Explicitly mark Open Work v1.2.90 and status prose in derived artifacts as legacy/freeze-time evidence.
6. Update `AGENTS.md` to enforce the same authority split, `Ready` execution boundary, proportional `/grilling`/`to-spec`/`to-tickets` use, and upstream-governance escalation rule.
7. Replace `tools/foundation_integrity_smoke.py` with a lightweight current-router audit independent of the historical manifest graph.
8. Point Foundation Smoke in `.github/workflows/foundation-integrity.yml` at the lean current router. Keep the required aggregate independent of Foundation Full.
9. Keep `.github/workflows/foundation-full.yml` on the frozen `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` and document it as historical/provenance certification.
10. Update `tools/foundation_integrity_routing.py`, `tests/test_foundation_lane_routing.py` and `docs/development/foundation-integrity-merge-gate.md` so governance-sensitive repository changes still run non-blocking Full, while ordinary delivery-state changes are Plane-only and generate no repository CI event.
11. Add `docs/development/chatgpt-project-master-gate-instructions.md` containing the exact post-transition Project instruction source for manual installation in ChatGPT Project settings.
12. Run exact-head GitHub CI. Correct every required-lane failure and any meaningful Foundation Full regression caused by WELL-66. Do not rewrite immutable historical evidence to silence obsolete historical assertions unless the test itself is current-routing machinery.
13. Independently review exact PR diff, base/head, authority, Plane state and CI. Keep WELL-66 nonterminal until merge plus resulting-main verification.

## Verification contract

Required before merge recommendation:

- PR base is the expected live `main` or any intervening main movement has been reconciled.
- Full diff contains only WELL-66 transition scope.
- New current router has no `OPEN_WORK` governing entry.
- `DELIVERY_GOVERNANCE_STANDARD_v1.0.0.md` is routed as current supporting authority.
- Plane is named authoritative execution state and `Ready` is the executable state.
- Open Work v1.2.90 is hash-pinned as frozen legacy and no successor is introduced.
- Foundation Smoke reads the new router.
- Foundation Full still reads the frozen old manifest.
- Application CI routing remains intact.
- AGENTS and Project-instruction source agree on the authority hierarchy and Master Gate.
- Required exact-head Route CI, Foundation Smoke and Foundation Integrity pass. Application CI must pass when routed.
- Foundation Full remains non-blocking, but WELL-66-caused failures must be understood and corrected unless they are intentionally retired historical expectations documented by the transition.

After merge, verify the exact reviewed head integrated without drift and required resulting-main CI passed before marking WELL-66 Done.
