# Foundation Integrity hardening implementation plan

> **For agentic workers:** Execute tasks in order. Keep each change tied to the invariant it implements, and run the full governance suite after each patch group.

**Goal:** Make Foundation Integrity enforce authority parity, lifecycle implications, and the blocked Development Entry boundary, while adding a separate live GitHub evidence verifier.

**Architecture:** Reuse the marked JSON state in the current Open Work authority. Extend FIA with strict manifest/README relation checks and explicit repository-root checks. Keep Phase 7 implication rules and GitHub transport separately testable; invoke the latter only through its own certification command.

**Tech Stack:** Python 3 standard library, `unittest`, GitHub REST API, GitHub Actions YAML.

---

## Files and boundaries

- Modify `.github/workflows/foundation-integrity.yml` to remove partial path filters.
- Modify `tools/foundation_integrity_audit.py` for strict manifest lifecycle/path checks, README route parity, canonical state parsing, state mirror validation, and repository-root enforcement.
- Add `tools/phase_7_delivery_gates.py` for pure formal-artifact and prerequisite rules.
- Add `tools/harden_02_github_evidence.py` for live, read-only GitHub verification and deterministic JSON output.
- Modify `tests/test_foundation_integrity_audit.py` for temporary repository mutations.
- Add `tests/test_phase_7_delivery_gates.py` for lifecycle implications and artifact identity.
- Add `tests/test_harden_02_github_evidence.py` for fake-transport evidence verification.
- Modify `tests/test_atlas_reconciliation.py` so current Open Work is resolved from the manifest.
- Add a versioned Atlas successor and preserve its predecessor if repository versioning rules require it.
- Add an Open Work successor only if machine-readable lifecycle metadata requires a governed state-artifact transition. Preserve its predecessor byte-identically, update its manifest entry and README route, and keep current lifecycle values unchanged.
- Modify Roadmap and dossier provenance labels only through governed successors when needed; do not alter their decisions.

## Task 1: Enforce Development Entry at the repository boundary

**Files:** `.github/workflows/foundation-integrity.yml`, `tools/foundation_integrity_audit.py`, `tests/test_foundation_integrity_audit.py`.

1. Add temporary-repository tests for `BLOCKED` with `mix.exs`, `lib/example.ex`, `priv/repo/migrations/001_create_example.exs`, `config/`, and `assets/`. Confirm each produces an FIA finding.
2. Add passing tests for a docs-only repository and repositories containing `tools/` and `tests/` while blocked. Add an `AUTHORISED` fixture with `lib/example.ex` and require it to pass the physical-boundary check.
3. Add a static workflow test that confirms both `pull_request` and pushes to `main` lack `paths` filters.
4. Run the targeted tests and confirm they fail against current behavior.
5. Parse the single marked Open Work JSON state with duplicate-key rejection. Define explicit Phoenix roots in one constant. Fail closed on missing or unknown `application_implementation`; reject roots only when the state is `BLOCKED`.
6. Remove `paths` from the pull-request and main-push triggers.
7. Run `python3 -m unittest tests.test_foundation_integrity_audit -v` and confirm the new mutations pass.

## Task 2: Enforce README and manifest authority parity

**Files:** `docs/00_platform/README.md`, `tools/foundation_integrity_audit.py`, `tests/test_foundation_integrity_audit.py`.

1. Add a marked table under `## Current Authority` with columns for document ID, authority class, context mode, canonical filename, repository path, and SemVer. Mark Frontend Experience System as conditional current authority.
2. Update the clean manifest fixture to include `lifecycle` and all README route columns.
3. Add mutations for omitted Frontend Experience System, extra manifest authority, historical Decision Register marked current, archived governing path, duplicate singular role, missing lifecycle, invalid lifecycle, path escape, route version mismatch, and current filename present only under README Archive.
4. Run `python3 -m unittest tests.test_foundation_integrity_audit -v` and confirm each mutation fails for its intended finding.
5. Require lifecycle for every entry. Permit only `current` and `historical`; require governing entries to be current, reference entries to be current, and historical entries to be historical.
6. Normalize repository-relative paths, reject absolute paths and traversal, resolve paths beneath the repository root, and enforce the manifest's governing/reference/archive roots.
7. Parse only the marked Current Authority table and compare its exact identity, class, path, filename, and version set with current governing manifest entries. Require one current entry per current authority class. Validate declared predecessors against historical entries when a predecessor is declared.
8. Replace `readme_current_authority_order` with a check name that states the exact parity predicate.
9. Run the targeted suite and the manifest-backed FIA command.

## Task 3: Check canonical active state and README mirror

**Files:** `docs/00_platform/README.md`, `tools/foundation_integrity_audit.py`, `tests/test_foundation_integrity_audit.py`.

1. Add a marked active-state mirror block in README with current stage, next stage, Phase 7C state, proof classification, and application implementation state.
2. Add tests for matching values, Phase 7C `READY` against canonical `BLOCKED`, application `AUTHORISED` against canonical `BLOCKED`, duplicate current-stage declarations, missing declarations, and historical `source-at-freeze` READY prose outside the reserved block.
3. Confirm mutations fail against current behavior.
4. Parse each block once, reject duplicate keys, and compare reserved values directly with the Open Work JSON. Do not scan unrelated Markdown prose.
5. Replace `readiness_wording` with a name and message that describe the literal state-mirror check.
6. Run the targeted FIA suite and full governance suite.

## Task 4: Repair Delivery Atlas current-source routing

**Files:** `docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.2.1.md` (or the governed successor selected after version review), `docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`, `docs/00_platform/README.md`, `tests/test_atlas_reconciliation.py`, current Open Work routing if required.

1. Add a test that reads the manifest's current Open Work entry and compares it to Atlas rows labelled `Current source`.
2. Add mutations for archived Open Work labelled current, a source-at-freeze row labelled historical, and a manifest successor while Atlas still points to the older route.
3. Confirm the tests reject the stale Atlas before changing it.
4. Create a versioned Atlas successor, preserve v0.2.0 byte-identically, route the current-source table and FP-001 authority anchor through the current Open Work manifest entry, and label retained archived references `source-at-freeze`.
5. Update README and any current Open Work Atlas pointer. Refresh only affected provenance hashes.
6. Run `python3 -m unittest tests.test_atlas_reconciliation -v` and the full suite.

## Task 5: Add Phase 7 artifact and gate implications

**Files:** canonical Open Work state successor if required, `tools/phase_7_delivery_gates.py`, `tools/foundation_integrity_audit.py`, `tests/test_phase_7_delivery_gates.py`.

1. Add pure tests for incomplete required Communications blocking Phase 7C, pending conditional dispositions blocking Phase 7C, `NOT REQUIRED` satisfying disposition, missing Final Contract blocking final proof, Pre-JIT completion not satisfying a registered formal JIT requirement, and complete prerequisites permitting the fixture transition.
2. Confirm each invalid fixture fails before implementation changes.
3. Define a small formal-artifact registry inside the existing canonical state. Identify formal artifacts by registry ID and type; never search all `working/` documents for status words.
4. Implement implication rules for Phase 7C, proof finalisation, and Development Entry. Keep the production state blocked and do not create or advance any dossier, contract, or proof.
5. Call the pure gate validator from FIA and report each failed implication as a named finding.
6. Run `python3 -m unittest tests.test_phase_7_delivery_gates -v` and the full suite.

## Task 6: Add separate live certification evidence verification

**Files:** `tools/harden_02_github_evidence.py`, `tests/test_harden_02_github_evidence.py`; do not add this command to Foundation Integrity workflow.

1. Define a fake GitHub transport and fixtures for PR metadata, reviews/comments, workflow runs, workflow definitions, merge SHA, and the post-merge `main` ref.
2. Add negative tests for a missing run, wrong head SHA, wrong workflow, failed or incomplete workflow, wrong PR record, unrelated comment/review, wrong merge relationship, wrong post-merge SHA, and false reviewer relationship. Confirm each fails before writing the live adapter.
3. Implement a read-only GitHub REST client using an injected transport for tests and `GITHUB_TOKEN` for explicit certification invocations.
4. Verify PR/base/head/author/merge data, review or attestation ownership and PR association, run identity/status/conclusion/SHA, and resulting-main/post-merge relationships against the supplied HARDEN-02 evidence fields.
5. Emit deterministic JSON with status, repository, PR, certified head, CI run IDs, merge SHA, checks, and findings. Return nonzero on API errors or unmet evidence.
6. Keep `run_audit()` and all existing unit validation free of GitHub requests. Do not edit Open Work to record verifier results or authorize HARDEN-02.
7. Run `python3 -m unittest tests.test_harden_02_github_evidence -v` and confirm the routine FIA command works with no token or network.

## Task 7: Clarify historical state boundaries

**Files:** Roadmap handoff successor if needed, Identity dossier handoff successor if needed, historical-stage tests that pin current Open Work routing.

1. Add tests that identify active route checks owned by FIA and historical provenance checks owned by their stage tests.
2. Label Roadmap tracker values with the Roadmap freeze time and Identity dossier merge/adjudication fields with dossier handoff time. Preserve previous files and hashes.
3. Remove only present-day Open Work filename, active programme, next-stage, and unrelated current hash assertions from completed historical-stage tests. Retain predecessor-byte and permanent stage-invariant checks.
4. Run all affected stage tests and review every removed assertion against an existing current FIA assertion.

## Task 8: Final verification, review, and PR

1. Run `python3 -m unittest discover -s tests -v` and record total count and result.
2. Run `python3 tools/foundation_integrity_audit.py --manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json`; record status, check count, and findings.
3. Check workflow triggers statically and run all live-verifier fixture tests.
4. Inspect `git diff --check`, changed paths, version successors, predecessor hashes, application roots, and current Open Work lifecycle state.
5. Commit changes in invariant-based groups, request code review, push the branch, and create a focused PR with the review baseline and implementation report.

## Self-review and stop conditions

The plan follows the requested P0-before-P1 order. Every new control has negative mutations. Atlas and governance successors preserve predecessors. The live verifier stays outside routine FIA. No step authorizes an application artifact or HARDEN-02 lifecycle transition. If implementing live verification requires changing certification requirements beyond the v0.4.0 contract, stop that task and report the exact unresolved rule.
