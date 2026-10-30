# Foundation Integrity merge gate

This is the current operational CI contract for implementation-era development. It is supporting engineering documentation, not Product, Architecture, Domain or Roadmap authority. The live workflows remain canonical for executable behaviour.

WELL-66 separates **current routing safety** from **historical/provenance certification**:

- Foundation Smoke validates `docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json` and current merge-gate topology.
- Foundation Full validates the historical Python governance suite plus the frozen pre-WELL-66 `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` baseline.
- Live delivery-state changes happen in Plane and therefore generate no repository PR or Foundation Full run.

`docs/development/foundation-integrity-ci.md` preserves the earlier WELL-38 transition design, baseline measurements and historical certification evidence. Older statements that the required aggregate waits for Foundation Full, that Open Work is live delivery authority, or that exact-SHA certification is dispatched through Foundation Integrity are historical.

## Required merge gate

The repository ruleset continues to require the status context **Foundation Integrity**.

For each pull request, the required gate waits only for:

- Route CI lanes;
- Foundation Smoke, including the merge-gate topology regression test and current-authority router smoke audit;
- Application CI (`mix check` and `mix check.deep`) when the route classifies application/engineering changes.

A required lane failure blocks merge. The required aggregate does not depend on Foundation Full.

## Foundation Smoke — current state

Foundation Smoke is intentionally small and fail-closed. It checks the lean current router for:

- the eight current durable governing documents and their hashes;
- current Engineering and Delivery Governance supporting authority;
- Plane project `WELL` as authoritative execution state;
- `Ready` as the only fresh agent/Symphony executable state;
- durable-governance precedence and Plane-only status changes;
- the final hash-pinned frozen legacy Open Work snapshot;
- current semantic working routes staying outside archive; and
- the live README routing contract.

It does not traverse the historical manifest graph. That work belongs to Foundation Full.

## Application CI — engineering state

Known engineering/application paths run the canonical fast and slower engineering gates through Application CI. Foundation Smoke still runs alongside them because current authority routing is an always-on repository safety net.

## Foundation Full — historical/provenance evidence

Durable-governance, provenance, workflow, mixed or unknown pull-request changes continue to start Foundation Full automatically. Foundation Full is cold, historical/provenance evidence and is not a dependency of the required merge aggregate.

It deliberately keeps using `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`, the frozen pre-WELL-66 historical integrity baseline. That manifest is not the live delivery router after WELL-66.

Routing remains path-specific. `docs/00_platform/**`, `tests/**`, `tools/foundation_integrity_*` and the explicit Foundation workflows are governance-sensitive. Known engineering and execution documentation under `docs/development/**`, `docs/superpowers/**` and `docs/execution/**` also routes Application CI where configured. Unclassified paths fail closed to Foundation Full.

This is intentional: after WELL-66, ordinary Ready/In Progress/Blocked/Done movement, dependency edits and delivery sequencing happen only in Plane. There should be no status-only repository patch to carve out of Full.

A new commit on the same pull request cancels the superseded Foundation Integrity workflow run so obsolete cold verification does not queue behind current work.

Foundation Full remains available independently for deliberate exact-SHA certification through its own `workflow_dispatch` input. Nightly hardening on `main` continues to run Foundation Full plus `mix check.deep` on fresh runners.

Historical tests, archives and certification evidence are not current execution authority merely because Foundation Full preserves them.

## Master Gate and handoff rule

Before handoff or merge recommendation, independently verify the exact PR diff and head SHA, durable authority, live Plane ticket/acceptance criteria, required `Foundation Integrity`, routed Application CI lanes and any applicable architecture/security/privacy/persistence invariants.

Do not wait for non-blocking Foundation Full unless the affected task or governing authority explicitly requires full certification. A Foundation Full failure remains evidence: investigate whether the PR caused a meaningful historical/provenance regression. Do not suppress a real regression simply because Full is non-blocking.

Any new PR head invalidates prior exact-head certification.

Merge is not delivery completion. After merge, verify resulting-main SHA/tree, reviewed-candidate integration/no drift and required resulting-main CI/proof before reconciling Plane to `Done` or opening dependent work.
