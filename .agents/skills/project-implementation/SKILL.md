---
name: project-implementation
description: Use before implementing any NewYou ticket or code change. Covers Ready-state Plane authority, blockers, current durable routing, relevant generated skills, Igniter-first changes, test-first implementation, and stopping on real upstream governance contradictions.
---

# NewYou Implementation Procedure

Durable governance is read-only during ordinary implementation. Consume it; do not rewrite it unless implementation conclusively exposes an upstream governance contradiction.

1. **Read the authoritative Plane ticket.** A fresh implementation may start only when the ticket is in `Ready`. Confirm its contract, acceptance scope and current state. Search Plane for an existing owner before creating anything.
2. **Inspect live blockers and dependencies in Plane.** Confirm each prerequisite is actually resolved. Do not start work whose dependencies are open. Historical Open Work/status prose is not live execution authority.
3. **Perform relevant reconnaissance and identify durable authority.** Start at `docs/README.md` and `docs/governance/CURRENT_GOVERNANCE_ROUTER.json`. Inspect the applicable current Product/Decision, Architecture, Domain, governing Roadmap and supporting authority; load the governance router's Architecture references only when exact source tracing is needed. Use `docs/delivery/CURRENT_DELIVERY_ROUTER.json` for current Feature/JIT/proof contracts, then inspect current code, tests, migrations and dependencies before deciding the implementation shape. `docs/history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` is frozen historical/provenance Full input, not a current router.
4. **Classify material questions** as `LOCKED`, `JIT IMPLEMENTATION CHOICE` or `UPSTREAM GOVERNANCE CONTRADICTION` under `AGENTS.md` and the Delivery Governance Standard. Follow locked authority and choose the simplest compliant JIT option. On a contradiction, STOP the affected work, record the conflicting sources/evidence and blocker in Plane, and escalate the smallest correct upstream amendment; do not invent or silently repair law.
5. **Load only relevant generated skills** from `.agents/skills/` (for example `ash-framework` for resources or actions, `phoenix-framework` for web work, `elixir-otp` for processes).
6. **Perform the mandatory Ash capability evaluation** from `AGENTS.md` for material business/durable-state/auth/lifecycle/async/audit/cross-Domain work. Verify plausible current Ash capabilities from primary sources; evaluation is not dependency-installation authority.
7. **Use Igniter first** where it safely supports the change (`mix igniter.install`, generators). Hand-edit only where Igniter does not support it. Do not contort code to claim Igniter was used.
8. **Use Tidewave/runtime evidence** in DEV when it answers a question better than static reading. Tidewave is diagnostic only, never business authority.
9. **Implement ticket scope only.** Do not implement adjacent Domains, Resources or flows. Use focused, test-first development for material implementation or behaviour changes.
10. **Record discovered delivery work in Plane** as you find it, including blockers, missing prerequisites, deferred fixes, security/privacy/architecture concerns and proof gaps. Link dependencies. Do not create Open Work successors or mutate semantic contracts merely to mirror ticket state.
11. **Run required verification.** Use `devcore-project run test -- mix check` (or focused tests while iterating) and follow `.agents/skills/code-change-verification/SKILL.md` before handoff. Run `mix check.deep` where the repository contract requires it.
12. **Hand off exact evidence.** Update Plane, create the PR and report the exact diff, exact head SHA, checks and Plane state for independent Master Gate review. Do not self-certify merge authority.
