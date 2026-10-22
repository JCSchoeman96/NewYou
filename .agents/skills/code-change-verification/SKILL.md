---
name: code-change-verification
description: Use before handoff or any merge recommendation for a NewYou change. Covers exact diff review, exact head SHA, mix check, mix check.deep, architecture invariants, no accidental governance edits, Plane reconciliation, required CI state and a clean worktree.
---

# NewYou Change Verification

Do not claim success without evidence from this exact head.

1. **Review the exact diff.** Run `git diff --stat origin/main...HEAD` and read the full diff. Confirm every changed path is in ticket scope.
2. **Record the exact head SHA** with `git rev-parse HEAD`. All evidence below must refer to this SHA.
3. **Run the fast gate:** `devcore-project run test -- mix check`. It must pass.
4. **Run applicable targeted tests** for the changed behaviour.
5. **Run the deep gate where required:** `devcore-project run test -- mix check.deep`. Required for changes touching application code, dependencies or the architecture rules.
6. **Confirm architecture and lifecycle invariants:** `mix check.architecture` passes; no new Repo, raw-SQL or Multi business writes; no Redis, extra Repo or speculative infrastructure; Tidewave remains DEV-only.
7. **Confirm no accidental governance changes.** `docs/00_platform/**`, the governance tools under `tools/foundation_integrity_*`, `tests/**` and the Foundation workflows must not change unless the ticket explicitly governs them. If they changed, justify it against the ticket. Governance-sensitive PRs should automatically start Foundation Full as non-blocking evidence.
8. **Reconcile Plane.** Confirm the issue state, blockers, dependency relations and follow-ups. Nothing delivery-affecting may remain only in chat, PR comments or TODOs.
9. **Confirm required CI state** on the PR head SHA: required `Foundation Integrity` and any routed Application CI lanes are green for this SHA. Do not wait for non-blocking Foundation Full unless the task or governing authority explicitly requires full certification; report its state when it is still running.
10. **Confirm a clean worktree** with `git status --short` empty, then report the SHA, checks run, Plane state and remaining risks.
