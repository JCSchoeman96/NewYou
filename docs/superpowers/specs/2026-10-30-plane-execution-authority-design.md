# Plane execution authority and durable-governance split

**Status:** APPROVED DESIGN / WELL-66 IMPLEMENTATION INPUT  
**Date:** 2026-10-30  
**Scope:** delivery governance, authority routing and CI topology only

## Intent

Reduce governance churn without weakening durable Product, Architecture, Domain, security, safety or integration controls. GitHub remains the durable constitutional source; Plane becomes the authoritative live delivery ledger and execution roadmap beneath that law. Symphony and local coding agents consume implementation-ready Plane work rather than infer work from governance prose.

## Goals

- Keep durable Product, Decision, Architecture, Domain, governing Roadmap, Operating, Engineering and semantic Feature/JIT/proof contracts versioned in GitHub.
- Make Plane authoritative for current work state, priority, blockers, dependencies, sequencing, acceptance criteria, discovered work, review/merge state and implementation readiness.
- Make Plane `Ready` the only agent/Symphony-executable state.
- Retire `02_OPEN_WORK_v1.2.90.md` as the final frozen legacy planning snapshot. No status-only successor is required.
- Stop propagating ticket status into Delivery Atlas, Skeleton, HARDEN, proof/JIT or other semantic contracts.
- Separate cheap current-authority validation from expensive historical/provenance certification.
- Preserve exact-head Master Gate and resulting-main verification.

## Non-goals

- No Product, Architecture, Domain, Feature Pack outcome or release/safety rule changes.
- Plane does not become a competing source of durable law.
- No weakening of safety, privacy, security, ownership or cross-Domain stop conditions.
- No requirement to pre-populate Plane with speculative future implementation work.

## Approaches considered

### 1. Keep Open Work authoritative and merely exclude it from Foundation Full

This reduces CI cost but retains two live execution ledgers (GitHub Open Work and Plane), so status synchronisation and successor churn remain. Rejected.

### 2. Move all governance and Roadmap authority to Plane

This would make durable product/architecture sequencing too easy to mutate and would weaken reviewable repository history. Rejected.

### 3. Durable GitHub law + authoritative Plane execution state

Selected. The high-level Plane roadmap is a delivery projection of the governed GitHub Roadmap. Changes to durable outcomes, ownership or governing sequencing still amend GitHub law; ordinary delivery state stays in Plane.

## Authority model

```text
GitHub durable governance
  Product / Decisions / Architecture / Domain / governing Roadmap
  Operating / Engineering / Frontend supporting law
  semantic Feature/JIT/proof contracts when required
        ↓
Plane authoritative execution state
  current roadmap projection / tickets / state / priority
  blockers / dependencies / acceptance / discovered work / review state
        ↓
Implementation evidence
  code / migrations / tests / PR / exact-head CI / resulting-main CI
```

Durable GitHub law always wins if Plane conflicts with it. A conflict is a stop condition, not permission to silently reconcile either side.

## Planning and execution model

For a major slice: repository reconnaissance → `/grilling` only for material ambiguity → `to-spec` only if durable implementation law is genuinely missing → `to-tickets` only when decomposition is useful → focused Plane work → `Ready` → implementation.

For narrow settled work: one Plane ticket → `Ready` → implementation.

Plane should contain the active delivery projection and near-term executable decomposition, not every speculative future task.

## Implementation-discovery boundary

During implementation classify discoveries as:

- `LOCKED`: already governed; follow it.
- `JIT IMPLEMENTATION CHOICE`: intentionally open and reversible enough; choose the simplest compliant implementation and record material work in Plane.
- `UPSTREAM GOVERNANCE CONTRADICTION`: missing/conflicting Product, Architecture, Domain, Roadmap, lifecycle, ownership, security, privacy or safety law, or another expensive-to-reverse governed semantic. Stop the affected work, record the blocker in Plane and amend the smallest correct upstream authority.

Implementation details do not become governance merely because they were discovered during coding.

## Open Work and derived artifacts

`02_OPEN_WORK_v1.2.90.md` is the final legacy snapshot. It remains immutable historical evidence but no longer governs live work. Future Ready/In Progress/Blocked/Done changes, dependency changes and PR/review state live only in Plane.

Delivery Atlas, Skeleton, HARDEN and semantic working contracts change only when their meaning changes. Their old status prose is freeze-time evidence and does not override Plane live execution state.

## Current routing versus historical integrity

The accumulated `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` is retained as a frozen historical/provenance integrity baseline for Foundation Full. A new lean `CURRENT_AUTHORITY_ROUTER_v1.0.0.json` owns current durable routing, supporting delivery authority, Plane execution metadata, legacy Open Work classification and current semantic working routes.

This intentionally prevents fast live routing from depending on the historical audit graph.

## CI model

- **Foundation Smoke:** always-on current-router validation and merge-gate topology.
- **Application CI:** routed for engineering changes.
- **Foundation Full:** non-blocking on material durable-governance/provenance/workflow PRs, plus nightly/manual exact-SHA historical certification. It keeps the frozen historical manifest/audit suite.
- Ordinary execution-state changes happen in Plane and therefore create no governance PR and no Foundation Full run.

Exact-head Master Gate and resulting-main verification remain mandatory.

## Transition

WELL-66 is the one-time transition. Until its PR merges and resulting-main verification passes, the pre-transition repository routing remains canonical. WELL-66 itself remains nonterminal through that post-merge gate.
