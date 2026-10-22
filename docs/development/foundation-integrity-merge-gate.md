# Foundation Integrity merge gate

This is the current operational CI contract for implementation-era development. It is supporting engineering documentation, not Product, Architecture, Domain or Roadmap authority. The live workflows remain canonical for executable behaviour.

`docs/development/foundation-integrity-ci.md` preserves the WELL-38 transition design, baseline measurements and historical certification evidence. Its older statements that the required aggregate waits for Foundation Full, or that exact-SHA certification is dispatched through Foundation Integrity, are historical and are superseded operationally by this document and the live workflows.

## Required merge gate

The repository ruleset continues to require the status context **Foundation Integrity**.

For each pull request, the required gate waits only for:

- Route CI lanes;
- Foundation Smoke, including the merge-gate topology regression test and current-authority smoke audit;
- Application CI (`mix check` and `mix check.deep`) when the route classifies application/engineering changes.

A required lane failure still blocks merge. The required aggregate does not depend on Foundation Full.

## Foundation Full

Governance-sensitive, mixed or unknown pull-request changes still automatically start Foundation Full. That cold historical suite is retained as non-blocking evidence rather than a merge-critical dependency.

A new commit on the same pull request cancels the superseded Foundation Integrity workflow run so obsolete cold verification does not queue behind current work.

Foundation Full remains available independently for deliberate exact-SHA certification through its own `workflow_dispatch` input. Nightly hardening on `main` continues to run Foundation Full plus `mix check.deep` on fresh runners.

No historical tests, archives or certification evidence are removed by this routing change.

## Merge and handoff rule

Before merge or handoff, verify the exact diff and head SHA, required `Foundation Integrity`, any routed Application CI lanes, architecture invariants, Plane state and repository cleanliness. Do not wait for a non-blocking Foundation Full run unless the task or governing authority explicitly requires full certification.

A Foundation Full failure remains a delivery signal: record it in Plane and investigate it. The failure is not itself a required status check unless a later governed decision explicitly restores that requirement.
