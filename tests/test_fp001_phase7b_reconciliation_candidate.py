from __future__ import annotations

import hashlib
import json
import re
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import (
    _fp001_phase7b_candidate_text_issues,
    run_audit,
)
from foundation_test_support import (
    WELL38_BASE_SHA,
    git_changed_paths,
    copy_git_snapshot_tree,
    current_working_path,
)


# PR #121 candidate recorded in its certification contract.
HISTORICAL_SCOPE_HEAD = "b6f82218026f3372ccacc96ffdbb37430e8e503f"

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
BASELINE_MAIN_SHA = "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd"
AUDIT_CERTIFIED_ARCHIVE_SHA256 = "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea"


def manifest_and_rules() -> tuple[dict, dict]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    rules = manifest["integrity_rules"]["fp001_phase7b_reconciliation_candidate"]
    return manifest, rules


def candidate_text() -> str:
    _, rules = manifest_and_rules()
    return (ROOT / rules["path"]).read_text(encoding="utf-8")


class FP001Phase7BReconciliationCandidateTests(unittest.TestCase):
    def test_baseline_authorities_and_certified_dossiers_remain_pinned(self):
        manifest, rules = manifest_and_rules()
        self.assertEqual(rules["baseline_main_sha"], BASELINE_MAIN_SHA)

        all_entries = {
            entry.get("document_id"): entry
            for group in ("governing_documents", "reference_documents")
            for entry in manifest[group]
        }
        all_entries.update(
            {entry.get("document_id"): entry for entry in manifest["historical_documents"]}
        )
        for document_id, expected in rules["baseline_authority_versions"].items():
            if document_id == "OPEN_WORK":
                entry = all_entries["OPEN_WORK_V1_2_65"]
            elif document_id == "ROADMAP":
                entry = all_entries["ROADMAP_V1_2_2"]
            elif document_id == "PLATFORM_BASELINE":
                entry = all_entries["PLATFORM_BASELINE_V1_8_0"]
            elif document_id == "DECISION_REGISTER":
                entry = all_entries["DECISION_REGISTER_V1_8_0"]
            elif document_id == "PLATFORM_OPERATING_MODEL":
                entry = all_entries["PLATFORM_OPERATING_MODEL_V1_0_1"]
            else:
                entry = all_entries[document_id]
            self.assertEqual(entry["semver"], expected["version"], document_id)
            expected_path = expected["path"]
            if document_id == "PLATFORM_OPERATING_MODEL":
                expected_path = "docs/00_platform/archive/PLATFORM_OPERATING_MODEL_v1.0.1.md"
            self.assertEqual(entry["repository_path"], expected_path, document_id)

        for path, expected_sha256 in rules["baseline_current_document_sha256"].items():
            workspace_path = path
            if path == "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md":
                workspace_path = "docs/00_platform/archive/PLATFORM_OPERATING_MODEL_v1.0.1.md"
            self.assertEqual(
                hashlib.sha256((ROOT / workspace_path).read_bytes()).hexdigest(),
                expected_sha256,
                path,
            )

        for domain, filename in (
            ("Identity & Access", "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"),
            ("Communications", "FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"),
            ("Audit & Evidence", "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"),
        ):
            path = (
                DOCS / "archive/identity_promotions" / filename
                if domain == "Identity & Access"
                else DOCS / "working" / filename
            )
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                rules["dossier_sha256"][domain],
                domain,
            )
        audit_archive = DOCS / "archive" / "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        self.assertEqual(
            hashlib.sha256(audit_archive.read_bytes()).hexdigest(),
            AUDIT_CERTIFIED_ARCHIVE_SHA256,
        )

    def test_scope_and_candidate_lifecycle_preserve_the_existing_gates(self):
        manifest, rules = manifest_and_rules()
        text = candidate_text()
        self.assertEqual(_fp001_phase7b_candidate_text_issues(text, rules), [])

        domain_block = re.search(
            r"The six affected Domains remain:\s*```text\s*(.*?)\s*```", text, re.DOTALL
        )
        self.assertIsNotNone(domain_block)
        self.assertEqual(
            [line.strip() for line in domain_block.group(1).splitlines() if line.strip()],
            rules["six_affected_domains"],
        )
        capability_statement = next(
            line for line in text.splitlines() if line.startswith("The seven material capability relationships remain")
        )
        first_statement = capability_statement.split(". Analytics", 1)[0]
        self.assertEqual(re.findall(r"CAP-\d{3}", first_statement), rules["seven_material_capabilities"])
        self.assertIn("CAP-004`, `CAP-027`, `CAP-029`", capability_statement)
        self.assertIn("Analytics stays `CONSUMER`", text)
        self.assertIn("issue #107", text.casefold())
        self.assertIn("not an FP-001 blocker", text)
        self.assertIn("prior PR #67 PMR reconciliation is complete", text)

        open_work = (DOCS / "archive/02_OPEN_WORK_v1.2.66.md").read_text(encoding="utf-8")
        state_match = re.search(
            r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
            open_work,
            re.DOTALL,
        )
        self.assertIsNotNone(state_match)
        state = json.loads(state_match.group(1))
        self.assertEqual(state["status_successor_base_sha"], BASELINE_MAIN_SHA)
        self.assertEqual(
            state["phase_7b_reconciliation"],
            "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        )
        self.assertEqual(state["phase_7b_reconciliation_candidate"]["lifecycle"], "NOT CERTIFIED / NOT CURRENT")
        self.assertEqual(state["phase_7c"], "BLOCKED / NOT_STARTED")
        self.assertEqual(state["proof_classification"], "NOT FINALISED")
        self.assertTrue(state["application_implementation"].startswith("UNAUTHORISED"))

        pmr_markers = (
            "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:START -->",
            "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:END -->",
        )
        current_skeleton = current_working_path(ROOT, "FP-001_FEATURE_PACK_SKELETON_WORKING_").read_text()
        archived_skeleton = (DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md").read_text()
        for marker in pmr_markers:
            self.assertEqual(current_skeleton.count(marker), 1)
            self.assertEqual(archived_skeleton.count(marker), 1)
        current_start = current_skeleton.index(pmr_markers[0])
        current_end = current_skeleton.index(pmr_markers[1]) + len(pmr_markers[1])
        archive_start = archived_skeleton.index(pmr_markers[0])
        archive_end = archived_skeleton.index(pmr_markers[1]) + len(pmr_markers[1])
        self.assertEqual(current_skeleton[current_start:current_end], archived_skeleton[archive_start:archive_end])

        changed = git_changed_paths(ROOT, BASELINE_MAIN_SHA, HISTORICAL_SCOPE_HEAD)
        self.assertFalse(
            [path for path in changed if path.startswith(("app/", "assets/", "lib/", "src/", "web/"))],
            changed,
        )

    def test_missing_or_unclassified_material_seam_fails_closed(self):
        _, rules = manifest_and_rules()
        text = candidate_text()
        without_last_seam = "\n".join(line for line in text.splitlines() if not line.startswith("| S-15 |"))
        self.assertTrue(any("missing material seams: S-15" in issue for issue in _fp001_phase7b_candidate_text_issues(without_last_seam, rules)))

        s05 = next(line for line in text.splitlines() if line.startswith("| S-05 |"))
        self.assertIn("`CONSISTENT`", s05)
        unclassified = text.replace(s05, s05.replace("`CONSISTENT`.", "unclassified."), 1)
        self.assertTrue(
            any("S-05" in issue and "determinate classification" in issue for issue in _fp001_phase7b_candidate_text_issues(unclassified, rules))
        )

    def test_a_blocking_seam_cannot_coexist_with_candidate_pass(self):
        _, rules = manifest_and_rules()
        text = candidate_text()
        s01 = next(line for line in text.splitlines() if line.startswith("| S-01 |"))
        blocked = text.replace(s01, s01.replace("`CONSISTENT`.", "`BLOCKING_AUTHORITY_GAP`.", 1), 1)
        issues = _fp001_phase7b_candidate_text_issues(blocked, rules)
        self.assertIn(
            "candidate PASS result cannot coexist with a blocking authority gap or dossier contradiction",
            issues,
        )

    def test_production_foundation_integrity_accepts_the_successor_and_pins_predecessor_provenance(self):
        report = run_audit(ROOT, MANIFEST_PATH)
        checks = {check["name"]: check for check in report["checks"]}
        for name in (
            "phase8_approved_status_successor_current",
            "phase8_status_successor_predecessor_provenance",
            "phase8_status_successor_phase7b_preservation",
        ):
            self.assertEqual(checks[name]["status"], "PASS", checks[name]["message"])

    def test_historical_candidate_seam_matrix_mutations_fail_the_full_audit(self):
        for mutation in ("missing", "unclassified"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                copy_git_snapshot_tree(ROOT, WELL38_BASE_SHA, root, "docs/00_platform", materialize_historical_readme=True)
                manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                rules = manifest["integrity_rules"]["fp001_phase7b_reconciliation_candidate"]
                candidate_path = root / rules["path"]
                text = candidate_path.read_text(encoding="utf-8")
                row = next(line for line in text.splitlines() if line.startswith("| S-15 |"))
                if mutation == "missing":
                    text = text.replace(row + "\n", "", 1)
                else:
                    text = text.replace(row, row.replace("`OUT_OF_SCOPE_FOR_FP001`", "unclassified", 1), 1)
                candidate_path.write_text(text, encoding="utf-8")

                report = run_audit(root, manifest_path)
                check = next(
                    item for item in report["checks"]
                    if item["name"] == "fp001_phase7b_seam_matrix"
                )
                self.assertEqual("FAIL", check["status"], check["message"])


if __name__ == "__main__":
    unittest.main()
