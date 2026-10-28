---
name: project-implementation
description: Use before implementing any NewYou ticket or code change. Covers reading the Plane issue, checking blockers, identifying governing authority, loading relevant generated skills, Igniter-first changes, and stopping on real authority contradictions.
---

# NewYou Implementation Procedure

Governance is frozen during ordinary implementation. Consume it; do not rewrite it.

1. **Read the authorised Plane ticket.** Confirm its contract and acceptance scope. Search Plane for an existing owner before creating anything.
2. **Inspect blockers and dependencies.** Confirm each blocker is actually resolved. Do not start work whose prerequisites are open.
3. **Perform relevant reconnaissance and identify authority.** Start at `docs/00_platform/README.md` and the current authority manifest. Inspect applicable contracts and current Open Work, and note the ARC/ADR/contract IDs the ticket touches. Inspect current code, tests, migrations and dependencies before deciding the implementation shape.
4. **Classify material questions** as `LOCKED`, `JIT IMPLEMENTATION CHOICE` or `UNRESOLVED GOVERNED QUESTION` under `AGENTS.md`. Follow locked authority and choose the simplest compliant JIT option. Stop, record in Plane and escalate unresolved governed questions; do not invent answers.
5. **Load only relevant generated skills** from `.agents/skills/` (for example `ash-framework` for resources or actions, `phoenix-framework` for web work, `elixir-otp` for processes).
6. **Use Igniter first** where it safely supports the change (`mix igniter.install`, generators). Hand-edit only where Igniter does not support it. Do not contort code to claim Igniter was used.
7. **Use Tidewave/runtime evidence** in DEV when it answers a question better than static reading. Tidewave is diagnostic only, never business authority.
8. **Implement ticket scope only.** Do not implement adjacent domains, resources or flows. Use focused, test-first development for material implementation or behaviour changes.
9. **Record discovered delivery work in Plane** as you find it, including blockers, missing prerequisites, deferred fixes, security or architecture concerns and proof gaps. Link dependencies.
10. **Run required verification.** Use `devcore-project run test -- mix check` (or the focused test while iterating) and follow `.agents/skills/code-change-verification/SKILL.md` before handoff.
11. **Stop on a real authority contradiction.** Record it in Plane with the conflicting sources and the smallest recommended amendment. Do not silently fix upstream law from application code.
12. **Hand off exact evidence.** Update Plane, create the PR and report the exact diff, head SHA, checks and Plane state for independent Master Gate review.
