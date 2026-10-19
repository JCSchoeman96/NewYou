from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
BASE_MAIN = "24a9ad925ee1ab6d75ddb44bae6df0b4f3d09bca"
PR126_MAIN = "69bef7bb2782cbff00a48505504ebd2686eb53d9"
REVIEWED_HEAD = "e7d5d3908bedf1a75c6627448c3ed0c067b076f8"
MERGE_TREE = "f5586314db6c3addab6482e866b8d781faba75bc"
CANDIDATE_ARCHIVE = DOCS / "archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
CANDIDATE_ARCHIVE_SHA256 = "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19"
PROMOTION_RULE = "fp001_phase7c_final_contract_current_promotion"

PREDECESSORS = (
    ("docs/00_platform/02_OPEN_WORK_v1.2.72.md", "docs/00_platform/archive/02_OPEN_WORK_v1.2.72.md"),
    ("docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.14.md", "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.14.md"),
    (
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md",
    ),
    ("docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.16.md", "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.16.md"),
)


def _marked_json(text: str, start: str, end: str) -> dict:
    match = re.search(re.escape(start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(end), text, re.DOTALL)
    return json.loads(match.group(1)) if match else {}


def _git_show(commit: str, path: str) -> bytes:
    return subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT, check=True, capture_output=True).stdout


class FP001Phase7CTrackerClosureSyncTests(unittest.TestCase):
    def test_current_tracker_closure_and_hosted_provenance_are_pinned(self):
        manifest = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
        rule = manifest["integrity_rules"][PROMOTION_RULE]
        expected = {
            "status_successor_base_sha": BASE_MAIN,
            "pr126_reviewed_head_sha": REVIEWED_HEAD,
            "pr126_merge_sha": PR126_MAIN,
            "pr126_merge_head_tree_sha": MERGE_TREE,
            "pr126_head_merge_tree_identity": "PASS",
            "pr126_exact_head_fia_run": 39141076412,
            "pr126_exact_head_fia_status": "completed",
            "pr126_exact_head_fia_conclusion": "success",
            "resulting_main_sha": PR126_MAIN,
            "resulting_main_fia_run": 39143147487,
            "resulting_main_fia_status": "completed",
            "resulting_main_fia_conclusion": "success",
            "resulting_main_fia_tests": 455,
            "resulting_main_fia_assertions": 728,
            "resulting_main_fia_findings": 0,
            "fresh_resulting_main_verification": "PASS",
            "phase_7c_execution_tracker_issue": 124,
            "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
            "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
            "contract_lifecycle": "COMPLETE / CERTIFIED / CURRENT",
            "programme_router_state": "OPEN",
            "proof_classification": "NEW_TRACER_BULLET",
            "phase8": "AUTHORISED",
            "application_implementation": "AUTHORISED",
            "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        }
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertEqual(value, rule.get(key))

        current_paths = rule["current_paths"]
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.74.md", current_paths["open_work"])
        self.assertEqual("docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.16.md", current_paths["delivery_atlas"])
        self.assertEqual("docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md", current_paths["fp001_skeleton"])
        self.assertEqual("docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md", current_paths["harden_02"])

        open_work = (ROOT / current_paths["open_work"]).read_text(encoding="utf-8")
        state = _marked_json(open_work, "<!-- HARDEN_02_LIFECYCLE_STATE_START -->", "<!-- HARDEN_02_LIFECYCLE_STATE_END -->")
        self.assertEqual("CLOSED / COMPLETED", state["phase_7c_execution_tracker_state"])
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", state["phase_7c"])
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", state["phase_7c_final_feature_pack_contract"]["lifecycle"])
        self.assertEqual("OPEN", state["programme_router_issue_111_state"])
        self.assertEqual("NEW_TRACER_BULLET", state["proof_classification"])
        self.assertEqual("NOT SELECTED", state["reuse_existing_proof"])
        self.assertEqual("NONE / NOT CREATED", state["tracer_bullet_id"])
        self.assertEqual("NOT STARTED", state["architectural_proof_execution"])
        self.assertEqual("NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION", state["next_stage"])
        self.assertEqual("AUTHORISED", state["application_implementation"])
        self.assertEqual("AUTHORISED", state["phase8"])

    def test_current_routes_project_closed_tracker_and_keep_downstream_gates_closed(self):
        manifest = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
        paths = manifest["integrity_rules"][PROMOTION_RULE]["current_paths"]
        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        current_state = readme.split("## Current State", 1)[1].split("\n## ", 1)[0]
        self.assertIn("PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED", current_state)
        self.assertIn("PROGRAMME ROUTER #111: OPEN", current_state)
        self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED", current_state)
        self.assertIn("PROOF CLASSIFICATION: NEW_TRACER_BULLET", current_state)
        self.assertIn("REUSE_EXISTING_PROOF: NOT SELECTED", current_state)
        self.assertIn("TRACER BULLET ID: NONE / NOT CREATED", current_state)
        self.assertIn("ARCHITECTURAL PROOF EXECUTION: NOT STARTED", current_state)
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", current_state)
        self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", current_state)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", current_state)
        self.assertNotRegex(current_state, r"(?i)(?:PHASE 7C EXECUTION/CONTROL TRACKER #124:\s*OPEN|ISSUE #124 IS (?:OPEN|REOPENED))\b")
        self.assertNotRegex(current_state, r"(?i)REUSE_EXISTING_PROOF:\s*SELECTED")
        self.assertNotRegex(current_state, r"\bTB-\d{3,}\b")

        open_work = (ROOT / paths["open_work"]).read_text(encoding="utf-8")
        active = open_work.split("# 9. Immediate Next Action", 1)[1].split("# 10. Minimal Tools", 1)[0]
        self.assertIn("PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED", active)
        self.assertIn("PROGRAMME ROUTER #111: OPEN", active)
        self.assertIn("NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION", active)
        self.assertNotRegex(active, r"(?i)(?:PHASE 7C EXECUTION/CONTROL TRACKER #124:\s*OPEN|ISSUE #124 IS (?:OPEN|REOPENED))\b")

        for key, route_heading in (
            ("delivery_atlas", "## 26.21 FP-001 architectural proof classification current route"),
            ("fp001_skeleton", "## v0.1.18 current-route status"),
            ("harden_02", "## 21. Current execution certification and next stage"),
        ):
            content = (ROOT / paths[key]).read_text(encoding="utf-8")
            self.assertIn(route_heading, content)
            route = content.split(route_heading, 1)[1].split("\n## ", 1)[0]
            if key == "delivery_atlas":
                route = route.split("\n- v0.4.12 — historical", 1)[0]
            self.assertIn("PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED", route)
            self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED", route)
            self.assertIn("PROOF CLASSIFICATION: NEW_TRACER_BULLET", route)
            self.assertIn("REUSE_EXISTING_PROOF: NOT SELECTED", route)
            self.assertIn("TRACER BULLET ID: NONE / NOT CREATED", route)
            self.assertIn("ARCHITECTURAL PROOF EXECUTION: NOT STARTED", route)
            self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", route)
            self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", route)
            self.assertNotRegex(route, r"(?i)(?:PHASE 7C EXECUTION/CONTROL TRACKER #124:\s*OPEN|ISSUE #124 IS (?:OPEN|REOPENED))\b")

    def test_foundation_integrity_rejects_open_tracker_projection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(DOCS, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            open_work_path = root / manifest["integrity_rules"][PROMOTION_RULE]["current_paths"]["open_work"]
            open_work = open_work_path.read_text(encoding="utf-8")
            start = "<!-- HARDEN_02_LIFECYCLE_STATE_START -->"
            end = "<!-- HARDEN_02_LIFECYCLE_STATE_END -->"
            begin = open_work.index(start)
            finish = open_work.index(end, begin)
            match = re.search(r"```json\s*(.*?)\s*```", open_work[begin:finish], re.DOTALL)
            state = json.loads(match.group(1))
            state["phase_7c_execution_tracker_state"] = "OPEN"
            rewritten = open_work[:begin] + open_work[begin:finish].replace(match.group(1), json.dumps(state, indent=2)) + open_work[finish:]
            open_work_path.write_text(rewritten, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            check = next(item for item in report["checks"] if item["name"] == PROMOTION_RULE)
            self.assertEqual("FAIL", check["status"], check["message"])

    def test_candidate_archive_and_direct_predecessor_archives_are_immutable(self):
        self.assertEqual(CANDIDATE_ARCHIVE_SHA256, hashlib.sha256(CANDIDATE_ARCHIVE.read_bytes()).hexdigest())
        manifest = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
        pinned = manifest["integrity_rules"][PROMOTION_RULE]["predecessor_archives_sha256"]
        for current, archived in PREDECESSORS:
            with self.subTest(archived=archived):
                source_bytes = _git_show(BASE_MAIN, current)
                archive_bytes = (ROOT / archived).read_bytes()
                self.assertEqual(source_bytes, archive_bytes)
                self.assertEqual(hashlib.sha256(archive_bytes).hexdigest(), pinned[archived])
                self.assertFalse((ROOT / current).exists())


if __name__ == "__main__":
    unittest.main()
