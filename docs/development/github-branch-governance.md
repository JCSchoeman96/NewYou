# GitHub branch governance (Pass 1 — P1-GOV-003)

The repository’s exact-head certification model assumes **`main` cannot change without review and a passing Foundation Integrity check**. As of Pass 1 audit, GitHub reported `main` as **unprotected** with **no rulesets**.

## Required controls on `main`

Apply these on the hosting repository (Settings → Rules → Rulesets, or legacy branch protection):

| Control | Purpose |
|--------|---------|
| Block direct pushes | Prevent bypass of PR + CI attestation |
| Require pull request before merge | Enforce independent review path |
| Require status check **Foundation Integrity** | Gate every merge (see check name below) |
| Require branches to be up to date before merge | Stale-green protection |
| Block force pushes | Preserve linear provenance on `main` |
| Block branch deletion | Prevent accidental loss of trust anchor |

Solo-maintainer repos still benefit: mistakes, compromised tooling, and process drift are blocked at the platform layer.

## Foundation Integrity workflow and check name

- Workflow: `.github/workflows/foundation-integrity.yml`
- Triggers: **every** `pull_request`, **every** push to `main`, and manual `workflow_dispatch` (no `paths:` filters). Required checks must not be skippable by path filtering.
- **Merge-preview vs exact-head:** `pull_request` runs validate GitHub’s PR merge preview (integration evidence). Pre-merge **exact-head** certification requires a `workflow_dispatch` run with **Use workflow from** set to the candidate branch whose tip is the certified head, and `ref` set to that same **40-character SHA**; the workflow fails closed if `GITHUB_SHA`, checkout (`git rev-parse HEAD`), or `ref` disagree. Bind attestation `pre_merge_ci.head_sha` to the Actions run only when the run `event` is `workflow_dispatch` and `head_sha` equals that same certified SHA.
- **Dispatch bootstrap:** `workflow_dispatch` is only available after the workflow file exists on the default branch. A PR that introduces dispatch cannot use dispatch for its own pre-merge evidence until it merges; narrow toolchain corrections may rely on `pull_request` merge-preview CI for merge gating while dossier/feature certification uses dispatch only after the mechanism is on `main`.
- Job id: `foundation-integrity`
- **Required status check context:** **`Foundation Integrity`** — set explicitly via `jobs.foundation-integrity.name` in the workflow.

Do **not** require `foundation-integrity` (job id) unless the Check Runs API on the PR head proves that is the published context. After workflow changes, verify:

```bash
gh api repos/:owner/:repo/commits/:pr_head_sha/check-runs --jq '.check_runs[] | select(.name | test("Foundation"; "i")) | {name, conclusion, status}'
```

Configure branch protection / rulesets to match the **exact** `name` field returned there.

## Administrator bypass

If administrators can bypass rules, document that explicitly in Open Work or operating model and treat bypass events as governance incidents.

## Verification

```bash
gh api repos/:owner/:repo/branches/main/protection
gh api repos/:owner/:repo/rulesets
```

A protected `main` should not return HTTP 404 for branch protection or should show an active ruleset targeting `main`.

## Pass 1 merge sequence

1. PR head passes **Foundation Integrity** with the verified check context name.
2. Activate ruleset / branch protection on `main` **before** merging the Pass 1 closure PR.
3. Merge through the protection; confirm post-merge **Foundation Integrity** on resulting `main` SHA.
