from __future__ import annotations

from foundation_test_support import (
    frozen_open_work_path,
    historical_platform_readme_text,
)
import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/history"
BASE_SHA = "ac8b7c7eeaddd2001c3ad3e2a8fbce46296b0a40"
PR165_HEAD = "98ad1ce5ef33cf10183cda68802b623afcf41378"
PR165_MERGE = "ac8b7c7eeaddd2001c3ad3e2a8fbce46296b0a40"
PR165_TREE = "8d98e9db1780cbd45885b5d0859ecf2987b57a28"
PR164_CANDIDATE_SHA256 = "e4ad6fd47bb1a04cd299fd900c2757e075352235ca286b6f368637942ae3cf6d"

PREDECESSORS = {
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.89.md": (
        "docs/00_platform/02_OPEN_WORK_v1.2.89.md",
        "OPEN_WORK_V1_2_89",
        "PLANNING_TRACKER_HISTORICAL",
    ),
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.30.md": (
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.30.md",
        "DELIVERY_ATLAS_V0_4_30",
        "DERIVED_DELIVERY_NAVIGATION_HISTORICAL",
    ),
    "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.30.md": (
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.30.md",
        "FP001_SKELETON_V0_1_30",
        "DERIVED_FEATURE_PACK_NAVIGATION_HISTORICAL",
    ),
    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.32.md": (
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.32.md",
        "HARDEN_02_V0_5_32",
        "DERIVED_GOVERNANCE_CONTRACT_HISTORICAL",
    ),
}


class WELL60TrackerClosureSyncTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.readme = historical_platform_readme_text(ROOT)
        cls.manifest = json.loads(
            (DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8")
        )
        cls.rules = cls.manifest["integrity_rules"]
        cls.well60 = cls.rules["well60_communications_handoff_candidate"]
        cls.phase8 = cls.rules["fp001_phase8_proof_contract_lifecycle"]
        cls.closure = cls.well60["post_merge_tracker_closure"]
        cls.open_work_path = frozen_open_work_path(ROOT)
        cls.open_work = cls.open_work_path.read_text(encoding="utf-8")
        cls.state_match = re.search(
            r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
            cls.open_work,
            re.DOTALL,
        )
        cls.state = json.loads(cls.state_match.group(1)) if cls.state_match else {}
        cls.closure_section = cls.open_work.split(
            "## 12.44 — WELL-60 post-merge tracker closure", 1
        )[1]

    def test_pr165_review_merge_tree_and_resulting_main_ci_are_pinned(self) -> None:
        expected = {
            "pr_number": 165,
            "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/165",
            "reviewed_head_sha": PR165_HEAD,
            "base_main_sha": "429677295a396b8c78e9ab6b436a57d9249eaddc",
            "merge_sha": PR165_MERGE,
            "resulting_main_sha": PR165_MERGE,
            "resulting_tree_sha": PR165_TREE,
            "merge_second_parent_sha": PR165_HEAD,
            "certified_head_to_resulting_main_changed_files": 0,
            "exact_head_workflow_run": 41030195757,
            "exact_head_required_checks": "PASS",
            "resulting_main_workflow_run": 41031269566,
            "resulting_main_workflow_conclusion": "PASS",
            "resulting_main_required_checks": "PASS",
            "master_gate_review": "PASS",
            "well_60_closure_status": "COMPLETE",
            "well_49_status": "BLOCKED / WAITING ON WELL-61",
            "well_49_execution_status": "NOT STARTED",
            "well_61_status": "PLANNING / INCOMPLETE",
            "application_source_paths_created": [],
            "dependency_changes": "NONE",
            "migration_changes": "NONE",
            "runtime_behavior_changes": "NONE",
        }
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertEqual(value, self.closure[key])

    def test_current_routes_and_well49_blocker_are_reconciled(self) -> None:
        expected_routes = {
            "open_work": "docs/00_platform/02_OPEN_WORK_v1.2.90.md",
            "delivery_atlas": "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.31.md",
            "fp001_skeleton": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.31.md",
            "harden_02": "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.33.md",
        }
        for key, path in expected_routes.items():
            with self.subTest(route=key):
                self.assertEqual(path, self.phase8["current_routes"][key])

        self.assertEqual(
            self.phase8["current_route_sha256"][self.phase8["current_routes"]["open_work"]],
            hashlib.sha256(self.open_work_path.read_bytes()).hexdigest(),
        )
        current_delivery = json.loads(
            (ROOT / "docs/delivery/CURRENT_DELIVERY_ROUTER.json").read_text(encoding="utf-8")
        )
        routed = {
            entry["document_id"]: entry
            for entry in current_delivery["delivery_contracts"]
        }
        for document_id in (
            "DELIVERY_ATLAS",
            "FP001_FEATURE_PACK_SKELETON",
            "HARDEN_02_CONTRACT",
        ):
            entry = routed[document_id]
            target = ROOT / entry["repository_path"]
            self.assertTrue(target.is_file())
            self.assertEqual(entry["sha256"], hashlib.sha256(target.read_bytes()).hexdigest())

        self.assertEqual("COMPLETE / PR #165 RESULTING-MAIN VERIFIED", self.state["well_60"])
        self.assertEqual("BLOCKED / WAITING ON WELL-61", self.state["well_49"])
        self.assertEqual("PLANNING / INCOMPLETE", self.state["well_61"])
        self.assertIn("WELL-60: COMPLETE", self.closure_section)
        self.assertIn("WELL-49 remains BLOCKED / WAITING ON WELL-61", self.closure_section)
        self.assertIn("WELL-49 execution has not started", self.closure_section)
        self.assertNotIn("WELL-49 remains BLOCKED / WAITING ON WELL-60", self.closure_section)

    def test_tb001_proof_stops_and_reviewed_candidate_archive_remain_unchanged(self) -> None:
        self.assertEqual(
            "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md",
            self.phase8["candidate_relative_path"],
        )
        self.assertEqual("INCOMPLETE / COVERAGE-INCOMPLETE", self.phase8["proof_result"])
        self.assertEqual("NOT CERTIFIED", self.phase8["proof_certification"])
        self.assertEqual("NOT STARTED / NOT AUTHORISED", self.phase8["phase9_vertical_slices"])
        archive = DOCS / "platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md"
        self.assertEqual(PR164_CANDIDATE_SHA256, hashlib.sha256(archive.read_bytes()).hexdigest())
        reviewed_bytes = subprocess.run(
            [
                "git",
                "show",
                f"{self.phase8['reviewed_candidate_head_sha']}:docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        self.assertEqual(reviewed_bytes, archive.read_bytes())
        self.assertIn("Phase 9 remains NOT STARTED / NOT AUTHORISED", self.closure_section)
        self.assertIn("TB-001 proof remains INCOMPLETE / COVERAGE-INCOMPLETE", self.closure_section)

    def test_direct_predecessor_archives_are_byte_identical_and_lineage_is_typed(self) -> None:
        entries = {
            item["repository_path"]: item
            for item in self.manifest["historical_documents"]
        }
        hashes = self.phase8["predecessor_archives_sha256"]
        for archive_path, (source_path, document_id, authority_class) in PREDECESSORS.items():
            with self.subTest(archive=archive_path):
                archived = ROOT / "docs/history/platform/archive" / Path(archive_path).name
                expected_bytes = subprocess.run(
                    ["git", "show", f"{BASE_SHA}:{source_path}"],
                    cwd=ROOT,
                    check=True,
                    capture_output=True,
                ).stdout
                digest = hashlib.sha256(expected_bytes).hexdigest()
                self.assertEqual(expected_bytes, archived.read_bytes())
                self.assertFalse((ROOT / source_path).exists())
                self.assertEqual(digest, hashes[archive_path])
                self.assertEqual(document_id, entries[archive_path]["document_id"])
                self.assertEqual(authority_class, entries[archive_path]["authority_class"])
                self.assertEqual(digest, entries[archive_path]["sha256"])

    def test_readme_and_manifest_route_v013_without_claiming_runtime_or_proof_completion(self) -> None:
        self.assertEqual(
            "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md",
            self.phase8["candidate_path"],
        )
        self.assertEqual(
            "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
            self.phase8["candidate_lifecycle"],
        )
        self.assertEqual("COMPLETE / PASS", self.phase8["contract_design_review"])
        current_prose = self.readme.split("## Historical status evidence", 1)[0]
        self.assertIn("9. `02_OPEN_WORK_v1.2.90.md`", current_prose)
        self.assertIn("02_OPEN_WORK_v1.2.90.md", current_prose)
        self.assertIn("DELIVERY_ATLAS_WORKING_v0.4.31.md", current_prose)
        self.assertIn("FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.31.md", current_prose)
        self.assertIn("HARDEN-02_CONTRACT_WORKING_v0.5.33.md", current_prose)
        self.assertNotIn("9. `02_OPEN_WORK_v1.2.89.md`", current_prose)
        self.assertEqual("NONE", self.closure["dependency_changes"])
        self.assertEqual("NONE", self.closure["migration_changes"])
        self.assertEqual("NONE", self.closure["runtime_behavior_changes"])
        self.assertEqual([], self.closure["application_source_paths_created"])


if __name__ == "__main__":
    unittest.main()
