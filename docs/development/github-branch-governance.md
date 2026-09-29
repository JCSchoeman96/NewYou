# GitHub branch governance (Pass 1 — P1-GOV-003)

The repository’s exact-head certification model assumes **`main` cannot change without review and a passing Foundation Integrity check**. As of Pass 1 audit, GitHub reported `main` as **unprotected** with **no rulesets**.

## Required controls on `main`

Apply these on the hosting repository (Settings → Rules → Rulesets, or legacy branch protection):

| Control | Purpose |
|--------|---------|
| Block direct pushes | Prevent bypass of PR + CI attestation |
| Require pull request before merge | Enforce independent review path |
| Require status check **Foundation Integrity** | Gate authority/tooling changes |
| Require branches to be up to date before merge | Stale-green protection |
| Block force pushes | Preserve linear provenance on `main` |
| Block branch deletion | Prevent accidental loss of trust anchor |

Solo-maintainer repos still benefit: mistakes, compromised tooling, and process drift are blocked at the platform layer.

## Foundation Integrity check name

The workflow file is `.github/workflows/foundation-integrity.yml`. The required check name in GitHub is typically **`Foundation Integrity`** (job id `foundation-integrity` under workflow display name **Foundation Integrity**).

## Administrator bypass

If administrators can bypass rules, document that explicitly in Open Work or operating model and treat bypass events as governance incidents.

## Verification

```bash
gh api repos/:owner/:repo/branches/main/protection
gh api repos/:owner/:repo/rulesets
```

A protected `main` should not return HTTP 404 for branch protection or should show an active ruleset targeting `main`.
