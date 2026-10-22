---
name: project-implementation
description: Use before implementing any NewYou ticket or code change. Covers reading the Plane issue, checking blockers, identifying governing authority, loading relevant generated skills, Igniter-first changes, and stopping on real authority contradictions.
---

# NewYou Implementation Procedure

Governance is frozen during ordinary implementation. Consume it; do not rewrite it.

1. **Read the Plane issue.** Find the ticket and its acceptance scope. Search Plane for an existing owner before creating anything.
2. **Inspect blockers and dependencies.** Confirm each blocker is actually resolved. Do not start work whose prerequisites are open.
3. **Identify applicable authority.** Start at `docs/00_platform/README.md` and the current authority manifest. Note the ARC/ADR/contract IDs the ticket touches.
4. **Load only relevant generated skills** from `.agents/skills/` (for example `ash-framework` for resources or actions, `phoenix-framework` for web work, `elixir-otp` for processes).
5. **Use Igniter first** where it safely supports the change (`mix igniter.install`, generators). Hand-edit only where Igniter does not support it. Do not contort code to claim Igniter was used.
6. **Use Tidewave/runtime evidence** in DEV when it answers a question better than static reading. Tidewave is diagnostic only, never business authority.
7. **Implement ticket scope only.** Do not implement adjacent domains, resources or flows.
8. **Record discovered delivery work in Plane** as you find it: blockers, missing prerequisites, deferred fixes, security or architecture concerns. Link dependencies.
9. **Run fast checks continuously** with `devcore-project run test -- mix check` (or the focused test while iterating). Use test-first for new guardrails and bug fixes.
10. **Stop on a real authority contradiction.** Record it in Plane with the conflicting sources and the smallest recommended amendment. Do not silently fix upstream law from application code.
