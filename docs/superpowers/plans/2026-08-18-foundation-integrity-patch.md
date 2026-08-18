# Foundation Integrity Patch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Correct the known foundation integrity defects, add a reproducible standard-library audit and authority manifest, compact current planning context, and close foundation work before Phase 7 / FP-001 preparation.

**Architecture:** Keep the seven current authority documents and four current reference-evidence documents as explicit manifest entries. A read-only Python audit runner parses only the bounded Markdown structures needed for governance checks, reports all findings in one run, and supports deterministic JSON output. Document edits remain surgical and preserve archive history; no upstream law is redesigned.

**Tech Stack:** Markdown, JSON, Python 3 standard library, `unittest`, SHA-256.

---

## File map

**Create:**

- `tools/__init__.py` — makes the audit module importable from tests.
- `tools/foundation_integrity_audit.py` — manifest loader, Markdown integrity checks, deterministic report, and CLI.
- `tests/test_foundation_integrity_audit.py` — fixture/unit tests for the audit contract and failure modes.
- `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` — checked-in current authority/evidence inventory and hashes.
- `docs/00_platform/archive/02_OPEN_WORK_CHANGELOG_v1.0.0.md` — preserved historical Open Work changelog.

**Modify:**

- `docs/00_platform/README.md` — current manifest pointer, corrected readiness language, and reference-audit pointer.
- `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` — current Open Work path repair.
- `docs/00_platform/00_PLATFORM_v1.2.1.md` — current Open Work path repair.
- `docs/00_platform/01_DECISIONS_v1.2.1.md` — formal `OQ-040` entry tied to `DEC-293`, plus current path metadata.
- `docs/00_platform/02_OPEN_WORK_v1.2.27.md` — current/reference/archive path repairs, changelog pointer, and readiness closure wording.
- `docs/00_platform/03_ARCHITECTURE_v1.0.0.md` — current/reference/archive path repairs.
- `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md` — current Open Work/reference path repairs.
- `docs/00_platform/05_ROADMAP_v1.0.0.md` — current Open Work/archive path repairs and readiness handoff wording where present.
- `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md` — current source-pack path repair; retain historical references as historical evidence.
- `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md` — current source-pack path repair; retain historical references as historical evidence.
- `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md` — current source-pack path repair.
- `docs/00_platform/reference/FOUNDATION_READINESS_AUDIT_v1.0.0.md` — machine-backed audit report and unambiguous readiness state.

## Task 1: Establish the failing audit contract

**Files:**

- Create: `tools/__init__.py`
- Create: `tests/test_foundation_integrity_audit.py`
- Test: `tests/test_foundation_integrity_audit.py`

- [ ] **Step 1: Create the import package marker.**

Create an empty `tools/__init__.py` so the test runner can import `tools.foundation_integrity_audit` from the repository root.

- [ ] **Step 2: Write failing tests for the public audit contract.**

The initial test module must import `run_audit` and assert these behaviours against temporary fixture files:

```python
from pathlib import Path
import hashlib
import json
import tempfile
import unittest

from tools.foundation_integrity_audit import run_audit


class FoundationIntegrityAuditTests(unittest.TestCase):
    def test_clean_fixture_returns_pass_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            report = run_audit(root, root / "manifest.json", expected_counts={
                "decisions": 1,
                "open_questions": 1,
                "architecture_law": 1,
                "architecture_requirements": 1,
                "reference_flows": 1,
                "domains": 1,
                "ownership_rows": 1,
                "feature_packs": 0,
            })
            self.assertEqual("PASS", report["status"])
            self.assertEqual([], report["findings"])

    def test_hash_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["sha256"] = "0" * 64
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            report = run_audit(root, root / "manifest.json", expected_counts={
                "decisions": 1,
                "open_questions": 1,
                "architecture_law": 1,
                "architecture_requirements": 1,
                "reference_flows": 1,
                "domains": 1,
                "ownership_rows": 1,
                "feature_packs": 0,
            })
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any(f["check"] == "manifest_hash_parity" for f in report["findings"]))

    def test_unresolved_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nSee OQ-999.\n", encoding="utf-8")
            report = run_audit(root, root / "manifest.json", expected_counts={
                "decisions": 1,
                "open_questions": 1,
                "architecture_law": 1,
                "architecture_requirements": 1,
                "reference_flows": 1,
                "domains": 1,
                "ownership_rows": 1,
                "feature_packs": 0,
            })
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any(f["check"] == "identifier_resolution" for f in report["findings"]))

    def _write_clean_fixture(self, root):
        files = {
            "docs/00_platform/01_DECISIONS_v1.2.1.md": "## DEC-001 — Example\n## OQ-001 — Example\n",
            "docs/00_platform/05_ROADMAP_v1.0.0.md": "# 14. Gate schedule\n| OQ-001 | Example |\n## 14.1 Non-OQ expert/vendor gates\n",
            "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md": "## ARC-001 — Example\n",
            "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "### ARQ-TEST-001 — Example\n",
            "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "# 3. FLOW-01 — Example\n",
            "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md": "## 3. Approved domain set\n| 1 | **Example Domain** | Example |\n## 4. Platform-wide business-truth ownership matrix\n| Business truth | Authoritative domain | Dependents | Rule |\n| Truth | **Example Domain** | None | READ |\n### 4.1 Ownership interpretation\n",
        }
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        manifest = {"governing_documents": [], "reference_documents": []}
        for relative in files:
            path = root / relative
            manifest["governing_documents"].append({
                "document_id": path.stem,
                "canonical_filename": path.name,
                "semver": path.name.split("_v", 1)[1][:-3],
                "repository_path": relative,
                "authority_class": "TEST",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "superseded_version": None,
            })
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest
```

The helper must use real files and real SHA-256 values. It must not mock filesystem or hashing behaviour. The fixture may use small identifier sets through an explicit audit configuration fixture mode, while the production repository uses the full configured ranges.

- [ ] **Step 3: Run the tests and verify the expected red failure.**

Run:

```bash
python3 -m unittest tests/test_foundation_integrity_audit.py -v
```

Expected: collection fails because `tools.foundation_integrity_audit` does not yet exist. This confirms the tests are exercising the intended missing audit API.

## Task 2: Implement the manifest and audit core

**Files:**

- Create: `tools/foundation_integrity_audit.py`
- Test: `tests/test_foundation_integrity_audit.py`

- [ ] **Step 1: Define the manifest schema and audit constants.**

Implement the seven governing entries and four reference-evidence entries as explicit metadata constants used only for fixture expectations and schema validation. The checked-in JSON remains the source of current hashes and paths. Define the identifier patterns, current authority paths, reference paths, and expected counts:

```python
EXPECTED_COUNTS = {
    "decisions": 293,
    "open_questions": 40,
    "architecture_law": 327,
    "architecture_requirements": 417,
    "reference_flows": 12,
    "domains": 18,
    "ownership_rows": 48,
    "feature_packs": 17,
}

ID_PATTERNS = {
    "DEC": re.compile(r"\bDEC-\d{3}\b"),
    "OQ": re.compile(r"\bOQ-\d{3}\b"),
    "ARC": re.compile(r"\bARC-\d{3}\b"),
    "ARQ": re.compile(r"\bARQ-[A-Z]+-\d{3}\b"),
    "FLOW": re.compile(r"\bFLOW-\d{2}\b"),
    "FP": re.compile(r"\bFP-\d{3}\b"),
}
```

Use `Path` throughout. Compute hashes by streaming bytes with `hashlib.sha256`; never normalize line endings before hashing.

- [ ] **Step 2: Implement pure parsing and reporting helpers.**

Implement `load_manifest`, `sha256_file`, `extract_identifier_tokens`, `collect_definitions`, `add_finding`, and `parse_semver`. `run_audit(root, manifest_path, expected_counts=None)` must use the production `EXPECTED_COUNTS` when `expected_counts` is omitted and accept reduced counts only for self-contained tests. Every finding must be a JSON-serializable dictionary with at least `check`, `path`, and `message`; the report must contain `status`, `assertion_count`, `counts`, `checks`, and `findings`.

- [ ] **Step 3: Implement manifest/path/hash/version checks.**

`run_audit(root, manifest_path)` must report all of these independently:

1. manifest JSON is an object with `governing_documents` and `reference_documents` arrays;
2. document IDs and repository paths are unique;
3. every repository path exists and is a file;
4. every canonical filename equals the repository path basename;
5. every manifest hash equals the file’s actual SHA-256;
6. every versioned filename SemVer equals the entry’s `semver`;
7. governing paths are current authority paths, while reference paths are under `docs/00_platform/reference/`.

- [ ] **Step 4: Run the focused tests and verify green.**

Run:

```bash
python3 -m unittest tests/test_foundation_integrity_audit.py -v
```

Expected: the Task 1 contract tests pass.

## Task 3: Add identifier, gate, and ownership checks test-first

**Files:**

- Modify: `tests/test_foundation_integrity_audit.py`
- Modify: `tools/foundation_integrity_audit.py`

- [ ] **Step 1: Add failing tests for each governance defect class.**

Add real-fixture tests named exactly `test_duplicate_definition_is_reported`, `test_missing_roadmap_gate_is_reported`, `test_multiple_domain_owners_are_reported`, and `test_missing_current_version_is_reported`.

Each test must mutate only the relevant fixture text and assert the corresponding check name, not merely that the overall report failed.

- [ ] **Step 2: Run the tests and verify each new test fails for the intended missing check.**

Run:

```bash
python3 -m unittest tests/test_foundation_integrity_audit.py -v
```

Expected: the original tests pass and each new governance test fails because its check is not implemented.

- [ ] **Step 3: Implement definition and reference resolution.**

Collect definitions from the authoritative source shapes only:

- `^## DEC-\d{3}` and `^## OQ-\d{3}` in the Decision Register;
- `^## ARC-\d{3}` in the Architecture Law register;
- `^#{1,6} ARQ-[A-Z]+-\d{3}` in the Architecture Requirements register;
- `^# \d+\. FLOW-\d{2}` in the Reference Flow register;
- `^## FP-\d{3}` in the Roadmap.

Report duplicate definitions, unresolved exact references, and the configured contiguous/count expectations. Do not treat family labels such as `ARQ-AN` without a numeric suffix as individual requirements.

- [ ] **Step 4: Implement Roadmap gate coverage.**

Extract the `# 14. Gate schedule` section through `## 14.1`, collect its `OQ-*` IDs, and require exact equality with the current Decision Register’s OQ definitions. This directly protects the `OQ-040` failure mode.

- [ ] **Step 5: Implement Domain ownership uniqueness.**

Parse the approved domain table between `## 3. Approved domain set` and `## 4.` and the ownership matrix between `## 4. Platform-wide business-truth ownership matrix` and `### 4.1`. Require 18 approved domains, 48 ownership rows, and exactly one bold owner in the second cell of every matrix row; the owner must be one of the approved domains.

- [ ] **Step 6: Implement active authority graph and path checks.**

Scan current authority metadata and current reference-document front matter for stale moved-file references. Require current Open Work to resolve to `02_OPEN_WORK_v1.2.27.md`, Architecture Law/Requirements/Flows to use `reference/`, and working Roadmap/Architecture artifacts to use `archive/` when referenced as historical files. Exclude `archive/` contents from active graph validation.

- [ ] **Step 7: Run the full unit test module and verify green.**

Run:

```bash
python3 -m unittest tests/test_foundation_integrity_audit.py -v
```

Expected: all fixture tests pass, including all intentional failure assertions.

## Task 4: Run the audit against the untouched foundation and capture the baseline failures

**Files:**

- Modify: none

- [ ] **Step 1: Run the new audit against the current repository content.**

Run:

```bash
python3 tools/foundation_integrity_audit.py --manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json
```

Expected: non-zero because the manifest does not yet exist and the current Decision Register lacks a formal `OQ-040` definition. Record the finding categories in the implementation notes, not in a new authority document.

## Task 5: Repair `OQ-040` and the active document graph

**Files:**

- Modify: `docs/00_platform/01_DECISIONS_v1.2.1.md`
- Modify: `docs/00_platform/00_PLATFORM_v1.2.1.md`
- Modify: `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
- Modify: `docs/00_platform/02_OPEN_WORK_v1.2.27.md`
- Modify: `docs/00_platform/03_ARCHITECTURE_v1.0.0.md`
- Modify: `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md`
- Modify: `docs/00_platform/05_ROADMAP_v1.0.0.md`
- Modify: `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md`
- Modify: `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md`
- Modify: `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md`

- [ ] **Step 1: Add `OQ-040` immediately after `OQ-039`.**

Use this exact entry shape in `01_DECISIONS`:

```markdown
## OQ-040 — First-party experimentation proof
**Status:** ARCHITECTURE / EXPERIMENTATION PROOF  
**Source decision:** DEC-293  
Prove the first-party governed A/B/n architecture before the first governed activation. The proof must cover deterministic/sticky assignment, anonymous-to-known continuity, concurrent-experiment isolation, exposure logging, authoritative conversion attribution, statistical validity, immutable aggregate learning evidence, privacy/deletion handling, variant-safe delivery/caching and failure/recovery. Exact assignment, cache and statistical mechanisms remain downstream Architecture and Feature Pack decisions.
```

Do not alter any existing `DEC-*` or `OQ-*` number.

- [ ] **Step 2: Repair current authority metadata paths.**

Change stale current Open Work references to `02_OPEN_WORK_v1.2.27.md`; prefix current deep evidence with `reference/`; prefix preserved working drafts with `archive/`; change the Architecture and Domain Map stale `v1.2.23`/`v1.2.24` tracker references to the current tracker. Remove the untracked `CORE_DOCS_AMENDMENT_AND_PRESERVATION_AUDIT_v1.2.1_2026-08-16.md` source-pack filename from active reference metadata and state that current Product Law files are canonical.

- [ ] **Step 3: Add explicit historical-reference boundary notes where needed.**

Keep historical version references inside cumulative evidence intact, but label them as contemporaneous historical evidence so they cannot be interpreted as current authority paths.

- [ ] **Step 4: Run the audit and targeted reference checks.**

Run:

```bash
python3 -m unittest tests/test_foundation_integrity_audit.py -v
rg -n '02_OPEN_WORK_v1\.2\.(?:[0-9]|1[0-9]|2[0-6])\.md|CORE_DOCS_AMENDMENT|(?<!archive/)05_ROADMAP_WORKING|(?<!reference/)ARCHITECTURE_(?:LAW|REQUIREMENTS)_WORKING' docs/00_platform/*.md docs/00_platform/reference/*.md
```

Expected: unit tests pass; only intentionally historical references in cumulative evidence remain, and no active metadata path is stale.

## Task 6: Compact current Open Work context without losing history

**Files:**

- Create: `docs/00_platform/archive/02_OPEN_WORK_CHANGELOG_v1.0.0.md`
- Modify: `docs/00_platform/02_OPEN_WORK_v1.2.27.md`

- [ ] **Step 1: Copy the complete historical changelog block into the archive artifact.**

Preserve the existing `## v1.2.27` through `## v1.2.1` entries verbatim under an archival header. Mark the artifact `HISTORICAL / NON-AUTHORITATIVE` and point readers to current `02_OPEN_WORK_v1.2.27.md`.

- [ ] **Step 2: Replace the current changelog block with a short archive pointer.**

Leave the current tracker metadata and numbered current sections intact. Add a short `Historical changelog` note immediately before `# 1. Purpose` pointing to `archive/02_OPEN_WORK_CHANGELOG_v1.0.0.md`.

- [ ] **Step 3: Verify preservation and context reduction.**

Run:

```bash
git diff --stat
wc -l docs/00_platform/02_OPEN_WORK_v1.2.27.md docs/00_platform/archive/02_OPEN_WORK_CHANGELOG_v1.0.0.md
```

Expected: the current tracker is materially shorter, the archive contains the removed historical sections, and no current numbered section is lost.

## Task 7: Rename readiness state and update the human audit report

**Files:**

- Modify: `docs/00_platform/README.md`
- Modify: `docs/00_platform/02_OPEN_WORK_v1.2.27.md`
- Modify: `docs/00_platform/reference/FOUNDATION_READINESS_AUDIT_v1.0.0.md`

- [ ] **Step 1: Replace ambiguous readiness wording everywhere in active current/report files.**

Use these exact lines:

```text
PLANNING FOUNDATION: READY
NEXT: PHASE 7 / FP-001 PREPARATION
EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS
```

- [ ] **Step 2: Add the explicit foundation closure statement.**

Add the exact sentence to the current Open Work closure and the audit report:

```text
FOUNDATION INTEGRITY PATCH COMPLETE. NO FURTHER FOUNDATION EXPANSION WITHOUT AN UPSTREAM CONTRADICTION.
```

- [ ] **Step 3: Replace audit prose with machine-backed evidence.**

Record the audit command, manifest path, current authority baseline, deterministic counts, check names, and the distinction between planning readiness and executable development. Do not introduce a second authority document.

## Task 8: Create and refresh the current authority manifest

**Files:**

- Create: `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`
- Modify: `tools/foundation_integrity_audit.py`
- Modify: `docs/00_platform/README.md`

- [ ] **Step 1: Add the manifest with all current entries and null/known superseded versions.**

Use stable JSON formatting: two-space indentation, sorted keys within entries, arrays in README authority order, and a trailing newline. Include the seven governing documents and four current reference-evidence documents with their correct authority classes and repository paths. Set hashes to the actual final file content using the audit tool’s refresh command.

- [ ] **Step 2: Add manifest refresh support.**

Implement:

```bash
python3 tools/foundation_integrity_audit.py --refresh-manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json
```

The command must update only SHA-256 values for existing entries and write deterministic JSON. It must not discover or silently add documents.

- [ ] **Step 3: Add the manifest link to the platform README.**

Describe it as machine-readable inventory/evidence, not a new authority class, and retain the existing seven-document default context order.

## Task 9: Run the complete verification suite and review the patch

**Files:**

- Test: `tests/test_foundation_integrity_audit.py`
- Verify: all modified files in the worktree

- [ ] **Step 1: Run unit tests.**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all audit fixture tests pass.

- [ ] **Step 2: Refresh and run the real audit.**

Run:

```bash
python3 tools/foundation_integrity_audit.py --refresh-manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json
python3 tools/foundation_integrity_audit.py --manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json
```

Expected: exit code `0`, status `PASS`, no findings, and counts of 293 decisions, 40 OQs, 327 ARCs, 417 ARQs, 12 flows, 18 domains, 48 ownership rows, and 17 feature packs.

- [ ] **Step 3: Run repository hygiene checks.**

Run:

```bash
git diff --check
rg -n 'Foundation READY|FOUNDATION READY|foundation baseline is READY|02_OPEN_WORK_v1\.2\.(?:[0-9]|1[0-9]|2[0-6])\.md|CORE_DOCS_AMENDMENT' docs/00_platform/*.md docs/00_platform/reference/*.md
git status --short
```

Expected: no ambiguous readiness wording or active stale-path hits; only the intended worktree changes are present.

- [ ] **Step 4: Read the final diff against the requirements.**

Verify line-by-line that all six patch items are covered, no architecture/domain/product law sections changed semantically, and the explicit “no further foundation expansion” closure is present.

- [ ] **Step 5: Commit the implementation in focused checkpoints.**

Use these commits, in order, after each checkpoint is green:

```bash
git add tools tests
git commit -m "test: add foundation integrity audit contract"

git add docs/00_platform/01_DECISIONS_v1.2.1.md docs/00_platform/00_PLATFORM_v1.2.1.md docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md docs/00_platform/02_OPEN_WORK_v1.2.27.md docs/00_platform/03_ARCHITECTURE_v1.0.0.md docs/00_platform/04_DOMAIN_MAP_v1.0.0.md docs/00_platform/05_ROADMAP_v1.0.0.md docs/00_platform/reference
git commit -m "docs: repair foundation document graph"

git add docs/00_platform/archive/02_OPEN_WORK_CHANGELOG_v1.0.0.md docs/00_platform/02_OPEN_WORK_v1.2.27.md
git commit -m "docs: compact open work current context"

git add docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json docs/00_platform/README.md
git commit -m "chore: add current authority manifest"
```

Do not commit until the complete verification commands above have been run freshly and their exit codes/output have been read.

## Completion handoff

After verification, report the isolated worktree path, audit command and output summary, files changed, and the next authorized action: Phase 7 / FP-001 preparation. Do not begin FP-001 implementation or create JIT dossiers in this patch.
