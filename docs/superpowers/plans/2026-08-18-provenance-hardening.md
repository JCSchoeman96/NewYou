# Provenance Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Correct PR #3's provenance cleanup without reopening foundation semantics by restoring frozen/source-at-freeze bytes, versioning the compacted Open Work tracker, and teaching the integrity audit to distinguish current navigation from historical provenance.

**Architecture:** `fad72c1` is the byte-authoritative baseline for artifacts that were not formally versioned. Current authority remains represented by the manifest and README. The audit scans only manifest-declared current navigation documents for stale routing references, while frozen/source-at-freeze artifacts retain accepted baseline hashes and are checked for byte parity.

**Tech Stack:** Markdown, JSON, Python 3 standard library, `unittest`, GitHub Actions.

---

### Task 1: Establish the failing provenance tests

**Files:**
- Modify: `tests/test_foundation_integrity_audit.py`
- Test: `tools/foundation_integrity_audit.py`

- [ ] **Step 1: Add a source-at-freeze regression test**

Add a production-mode fixture test that places an old `02_OPEN_WORK_v1.2.23.md` reference inside the Architecture Law evidence document, configures only the Roadmap fixture as current navigation, and asserts that `active_document_graph` has no finding. This must exercise the public `run_audit` path, not a mocked helper.

- [ ] **Step 2: Add a current-navigation stale-reference test**

Add a companion test that places the same old tracker reference in the configured current navigation document and asserts that `active_document_graph` reports it. This preserves the stale-reference guard where it is still meaningful.

- [ ] **Step 3: Add accepted frozen-hash coverage**

Add a test covering the exact `fad72c1` SHA-256 values for the eight unversioned frozen artifacts:

```text
PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md  5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20
00_PLATFORM_v1.2.1.md                 56a2b9a5db42a81e287f0c61deae37d6bbce5b19f48f67732584160b455f935a
03_ARCHITECTURE_v1.0.0.md             87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b
04_DOMAIN_MAP_v1.0.0.md               f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a
05_ROADMAP_v1.0.0.md                  b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20
ARCHITECTURE_REQUIREMENTS...           cdf09ecced658635572a20e4f2feb04120b4f856e81762ef5af9ba179a11c40e
ARCHITECTURE_LAW...                    a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639
REFERENCE_FLOW_PRESSURE_TESTS...       f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20
```

The test must read the repository files and compare their SHA-256 values to these accepted canonical values.

- [ ] **Step 4: Run the focused tests and confirm RED**

Run:

```bash
python3 -m unittest tests.test_foundation_integrity_audit.FoundationIntegrityAuditTests.test_source_at_freeze_references_are_not_stale -v
python3 -m unittest tests.test_foundation_integrity_audit.FoundationIntegrityAuditTests.test_declared_current_navigation_reference_is_reported -v
```

Expected result: the new tests fail because the current runner scans all current evidence documents and does not yet have navigation-scoped graph policy.

### Task 2: Restore frozen bytes and version the current tracker

**Files:**
- Restore from `fad72c1`: `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
- Restore from `fad72c1`: `docs/00_platform/00_PLATFORM_v1.2.1.md`
- Restore from `fad72c1`: `docs/00_platform/03_ARCHITECTURE_v1.0.0.md`
- Restore from `fad72c1`: `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md`
- Restore from `fad72c1`: `docs/00_platform/05_ROADMAP_v1.0.0.md`
- Restore from `fad72c1`: `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`
- Restore from `fad72c1`: `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md`
- Restore from `fad72c1`: `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`
- Rename: `docs/00_platform/02_OPEN_WORK_v1.2.27.md` → `docs/00_platform/02_OPEN_WORK_v1.2.28.md`
- Create archive snapshot: `docs/00_platform/archive/02_OPEN_WORK_v1.2.27.md`

- [ ] **Step 1: Move the compacted current tracker to v1.2.28**

Move the current PR #3 tracker to `02_OPEN_WORK_v1.2.28.md`, then update only its title, status version, and current-version self-references as needed. Preserve its compacted changelog extraction and current readiness wording.

- [ ] **Step 2: Restore and archive the exact pre-PR3 tracker**

Restore `02_OPEN_WORK_v1.2.27.md` from `fad72c1`, verify its SHA-256 is `db50ff91eac66033c58824c6e139a74ddbce58ab2292a0655de68ef223bccc42`, then move that exact file to `archive/02_OPEN_WORK_v1.2.27.md`.

- [ ] **Step 3: Restore all unversioned frozen/source-at-freeze artifacts**

Restore the eight listed frozen artifacts from `fad72c1` without editorial edits. Verify every restored file against the accepted hash test before changing any current navigation metadata.

### Task 3: Make the manifest and audit provenance-aware

**Files:**
- Modify: `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`
- Modify: `tools/foundation_integrity_audit.py`
- Modify: `tests/test_foundation_integrity_audit.py`

- [ ] **Step 1: Add v1.2.28 and historical tracker entries**

Make `02_OPEN_WORK_v1.2.28.md` the current `OPEN_WORK` entry, set its superseded version to `1.2.27`, and add `archive/02_OPEN_WORK_v1.2.27.md` as a historical entry with its exact baseline hash.

- [ ] **Step 2: Add accepted provenance hashes**

Add `provenance_sha256` to the eight frozen manifest entries using the accepted `fad72c1` hashes. Mark frozen/source-at-freeze entries with the existing `frozen_provenance` graph policy. Keep the current integrity audit and v1.2.2 Decision Register as current non-frozen artifacts.

- [ ] **Step 3: Declare current navigation in manifest rules**

Add `navigation_document_ids: ["OPEN_WORK"]` to `integrity_rules.graph_rules`. The README/context index remains the manifest-declared `context_index`.

- [ ] **Step 4: Scope stale-reference scanning to navigation documents**

Refactor `_check_production_graph` to derive scan targets from `navigation_document_ids` plus the manifest context index. Do not scan frozen/source-at-freeze evidence documents for current tracker versions. Continue applying stale-reference patterns to the declared current navigation documents.

- [ ] **Step 5: Check accepted frozen hashes in the runner**

When a manifest entry contains `provenance_sha256`, record a `frozen_provenance_hash` check comparing the file's actual SHA-256 with that accepted value. Missing or mismatched provenance hashes must fail the audit.

- [ ] **Step 6: Run the focused tests and confirm GREEN**

Run the two graph tests and the frozen-hash test from Task 1. Expected result: all pass, with the source-at-freeze test proving old references are allowed only outside current navigation.

### Task 4: Synchronize current navigation and evidence

**Files:**
- Modify: `docs/00_platform/README.md`
- Modify: `docs/00_platform/01_DECISIONS_v1.2.2.md`
- Modify: `docs/00_platform/02_OPEN_WORK_v1.2.28.md`
- Modify: `docs/00_platform/reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md`
- Modify: `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`

- [ ] **Step 1: Update current navigation to v1.2.28**

Change only current navigation metadata and current-document related links to identify `02_OPEN_WORK_v1.2.28.md`. Add the archived v1.2.27 tracker to README/archive documentation. Do not edit restored frozen artifacts to make them current.

- [ ] **Step 2: Update integrity evidence**

Update the current audit's authority baseline and mechanical count only as required by the actual runner output. Keep the original readiness audit and all frozen/source-at-freeze evidence out of the current audit identity.

- [ ] **Step 3: Refresh manifest hashes**

Run the existing manifest refresh command after all content changes, then audit that current and historical entries point to existing paths with matching hashes and SemVer metadata.

### Task 5: Verify, commit, push and prepare PR #4

**Files:**
- All files above
- Create: `.github/workflows/foundation-integrity.yml` only if the merged workflow is not inherited in the branch (otherwise leave unchanged)

- [ ] **Step 1: Run the complete verification suite**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 tools/foundation_integrity_audit.py --manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json
python3 -m py_compile tools/foundation_integrity_audit.py
python3 -m json.tool docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json
git diff --check
```

Expected result: all tests pass, the audit reports PASS with zero findings, and the frozen hash/provenance comparisons pass.

- [ ] **Step 2: Verify exact restoration against `fad72c1`**

Use `git diff --quiet fad72c1 --` for each restored frozen artifact and `cmp`/SHA-256 verification for the archived v1.2.27 tracker. Confirm the current PR diff does not modify those frozen paths.

- [ ] **Step 3: Commit and push the bounded correction**

Commit with:

```bash
git add .github docs/00_platform tests tools
git commit -m "harden frozen document provenance"
git push -u origin agent/provenance-hardening
```

- [ ] **Step 4: Create PR #4 against `main`**

Describe the correction as provenance-only, list the v1.2.28 tracker transition, and explicitly state that Product Law, Architecture, Domain Law, Roadmap semantics and FP-001 remain untouched.

- [ ] **Step 5: Stop after PR verification**

Do not start Phase 7 tooling or implementation. The completion condition is restored provenance, versioned current tracker, synchronized manifest/README, provenance-aware audit, and passing tests/audit/CI.
