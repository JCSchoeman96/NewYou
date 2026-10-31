from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import (
    _check_platform_readme_router_consistency,
    _check_fp001_phase7c_current_promotion,
    run_audit,
)
from foundation_test_support import WELL38_BASE_SHA, copy_git_snapshot_tree


ROOT = Path(__file__).resolve().parents[1]
PROMOTION_RULE = "fp001_phase7c_final_contract_current_promotion"
CONTRACT_REL = "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
OPEN_WORK_REL = "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md"
README_REL = "docs/00_platform/archive/README_PRE_WELL66_2026-10-30.md"
ARCHIVE_REL = "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"


class FP001Phase7CCurrentPromotionAuditTests(unittest.TestCase):
    def _copy_fixture(self, root: Path) -> tuple[Path, dict]:
        copy_git_snapshot_tree(ROOT, WELL38_BASE_SHA, root, "docs/00_platform", materialize_historical_readme=True)
        manifest_path = root / "docs" / "00_platform" / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        return root, json.loads(manifest_path.read_text(encoding="utf-8"))

    def _promotion_check(self, root: Path, manifest: dict) -> dict:
        report = {"checks": [], "findings": []}
        _check_fp001_phase7c_current_promotion(
            root,
            manifest,
            manifest["integrity_rules"],
            report,
        )
        return report["checks"][0]

    @staticmethod
    def _read_marked_json(path: Path, start: str, end: str) -> tuple[str, dict, str]:
        text = path.read_text(encoding="utf-8")
        begin = text.index(start)
        finish = text.index(end, begin)
        block = text[begin:finish]
        match_start = block.index("```json") + len("```json")
        match_end = block.index("```", match_start)
        value = json.loads(block[match_start:match_end])
        return text[:begin], value, text[finish:]

    @classmethod
    def _write_marked_json(cls, path: Path, start: str, end: str, value: dict) -> None:
        prefix, _, suffix = cls._read_marked_json(path, start, end)
        text = path.read_text(encoding="utf-8")
        begin = text.index(start)
        finish = text.index(end, begin)
        block = text[begin:finish]
        match_start = block.index("```json") + len("```json")
        match_end = block.index("```", match_start)
        updated = block[:match_start] + "\n" + json.dumps(value, indent=2) + "\n" + block[match_end:]
        path.write_text(prefix + updated + suffix, encoding="utf-8")

    def _mutate_open_state(self, root: Path, key: str, value) -> None:
        path = root / OPEN_WORK_REL
        _, state, _ = self._read_marked_json(
            path,
            "<!-- HARDEN_02_LIFECYCLE_STATE_START -->",
            "<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        )
        state[key] = value
        self._write_marked_json(
            path,
            "<!-- HARDEN_02_LIFECYCLE_STATE_START -->",
            "<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
            state,
        )

    def _mutate_contract_status(self, root: Path, key: str, value) -> None:
        path = root / CONTRACT_REL
        _, state, _ = self._read_marked_json(
            path,
            "<!-- FP001_PHASE7C_CURRENT_STATUS_START -->",
            "<!-- FP001_PHASE7C_CURRENT_STATUS_END -->",
        )
        state[key] = value
        self._write_marked_json(
            path,
            "<!-- FP001_PHASE7C_CURRENT_STATUS_START -->",
            "<!-- FP001_PHASE7C_CURRENT_STATUS_END -->",
            state,
        )

    def _mutate_manifest_rule(self, manifest: dict, key: str, value) -> None:
        manifest["integrity_rules"][PROMOTION_RULE][key] = value

    @staticmethod
    def _append_to_current_route(path: Path, line: str) -> None:
        text = path.read_text(encoding="utf-8")
        if path.name == "README.md":
            start = text.index("## Current State")
            end = text.find("\n## ", start + 1)
        else:
            start = text.index("# 9. Immediate Next Action")
            end = text.find("# 10. Minimal Tools", start + 1)
        if end < 0:
            end = len(text)
        text = text[:end] + "\n" + line + "\n" + text[end:]
        path.write_text(text, encoding="utf-8")

    def test_current_successor_and_pinned_predecessor_pass_foundation_integrity(self):
        report = run_audit(ROOT, ROOT / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
        checks = {item["name"]: item for item in report["checks"]}
        for name in (
            "phase8_approved_status_successor_current",
            "phase8_status_successor_predecessor_provenance",
            PROMOTION_RULE,
        ):
            self.assertEqual("PASS", checks[name]["status"], checks[name]["message"])

    def test_fail_closed_mutations_cover_phase7c_closure_and_provenance(self):
        mutations = (
            ("tracker #124 reopens", lambda r, m: self._mutate_open_state(r, "phase_7c_execution_tracker_state", "OPEN")),
            ("Phase 7C status regresses", lambda r, m: self._mutate_open_state(r, "phase_7c", "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING")),
            ("contract lifecycle regresses", lambda r, m: self._mutate_contract_status(r, "contract_lifecycle", "CANDIDATE / NOT CERTIFIED / NOT CURRENT")),
            ("PR #126 reviewed head changes", lambda r, m: self._mutate_manifest_rule(m, "pr126_reviewed_head_sha", "bad-head")),
            ("PR #126 merge SHA changes", lambda r, m: self._mutate_manifest_rule(m, "pr126_merge_sha", "bad-merge")),
            ("merge/head tree identity changes", lambda r, m: self._mutate_manifest_rule(m, "pr126_head_merge_tree_identity", "FAIL")),
            ("resulting-main run is incomplete", lambda r, m: self._mutate_manifest_rule(m, "resulting_main_fia_status", "in_progress")),
            ("resulting-main run fails", lambda r, m: self._mutate_manifest_rule(m, "resulting_main_fia_conclusion", "failure")),
            ("resulting-main evidence counts drift", lambda r, m: self._mutate_manifest_rule(m, "resulting_main_fia_tests", 454)),
            ("programme router #111 closes", lambda r, m: self._mutate_open_state(r, "programme_router_issue_111_state", "CLOSED")),
            ("proof classification finalises", lambda r, m: self._mutate_open_state(r, "proof_classification", "FINALISED")),
            ("REUSE_EXISTING_PROOF selected early", lambda r, m: self._append_to_current_route(r / OPEN_WORK_REL, "PROOF CLASSIFICATION: REUSE_EXISTING_PROOF")),
            ("both proof options selected", lambda r, m: self._append_to_current_route(r / OPEN_WORK_REL, "REUSE_EXISTING_PROOF: SELECTED")),
            ("classification selects reuse", lambda r, m: self._mutate_open_state(r, "proof_classification", "REUSE_EXISTING_PROOF")),
            ("classification remains not finalised", lambda r, m: self._mutate_open_state(r, "architectural_proof_classification_status", "NOT FINALISED")),
            ("FLOW-01 is represented as executable proof", lambda r, m: (r / OPEN_WORK_REL).write_text((r / OPEN_WORK_REL).read_text(encoding="utf-8").replace("FLOW-01` is supporting evidence only", "FLOW-01` satisfies executable proof", 1), encoding="utf-8")),
            ("Tracer Bullet identifier is invented", lambda r, m: self._mutate_open_state(r, "tracer_bullet_id", "TB-001")),
            ("proof execution is represented as complete", lambda r, m: self._mutate_open_state(r, "architectural_proof_execution", "COMPLETE")),
            ("application implementation becomes authorised", lambda r, m: self._append_to_current_route(r / OPEN_WORK_REL, "APPLICATION IMPLEMENTATION: AUTHORISED")),
            ("classification is represented as executable proof", lambda r, m: self._append_to_current_route(r / OPEN_WORK_REL, "PROOF CLASSIFICATION: EXECUTABLE PROOF: COMPLETE")),
            ("Phase 8 becomes authorised", lambda r, m: self._append_to_current_route(r / OPEN_WORK_REL, "PHASE 8 / APPLICATION IMPLEMENTATION: AUTHORISED")),
            ("certified contract semantics drift", lambda r, m: (r / CONTRACT_REL).write_text((r / CONTRACT_REL).read_text(encoding="utf-8").replace("create an individual 18+ account", "create an individual account", 1), encoding="utf-8")),
            ("immutable PR #125 candidate archive changes", lambda r, m: (r / ARCHIVE_REL).write_bytes((r / ARCHIVE_REL).read_bytes() + b"\nchanged\n")),
            ("direct predecessor archive changes", lambda r, m: (r / "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.14.md").write_bytes((r / "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.14.md").read_bytes() + b"\nchanged\n")),
            ("current route projects #124 open", lambda r, m: self._append_to_current_route(r / OPEN_WORK_REL, "PHASE 7C TRACKER #124: OPEN THROUGH RESULTING-MAIN VERIFICATION")),
            ("current route retains transition wording", lambda r, m: self._append_to_current_route(r / OPEN_WORK_REL, "CURRENT CONTRACT AFTER THIS STATUS SUCCESSOR MERGES")),
        )
        for name, mutate in mutations:
            with self.subTest(mutation=name), tempfile.TemporaryDirectory() as directory:
                root, manifest = self._copy_fixture(Path(directory))
                mutate(root, manifest)
                check = self._promotion_check(root, manifest)
                self.assertEqual("FAIL", check["status"], check["message"])

    def test_foundation_integrity_rejects_a_created_tracer_bullet_or_proof_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self._copy_fixture(Path(directory))
            artifact = root / "docs/00_platform/working/FP001_TRACER_BULLET_CONTRACT_WORKING_v0.1.0.md"
            artifact.write_text("Candidate Tracer Bullet contract.\n", encoding="utf-8")
            manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

            report = run_audit(root, manifest_path)
            check = next(item for item in report["checks"] if item["name"] == "roadmap_proof_classification_lifecycle")
            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn("Tracer Bullet or architectural-proof artifact exists", check["message"])

    def test_status_record_rejects_tree_or_count_provenance_drift(self):
        mutations = (
            ("reviewed tree", "pr126_reviewed_head_tree_sha", "bad-tree"),
            ("merge tree", "pr126_merge_tree_sha", "bad-tree"),
            ("resulting-main run", "resulting_main_fia_run", 39143147488),
            ("resulting-main counts", "resulting_main_fia_assertions", 727),
        )
        for name, key, value in mutations:
            with self.subTest(field=name), tempfile.TemporaryDirectory() as directory:
                root, manifest = self._copy_fixture(Path(directory))
                self._mutate_contract_status(root, key, value)
                check = self._promotion_check(root, manifest)
                self.assertEqual("FAIL", check["status"], check["message"])

    def test_current_readme_route_rejects_candidate_projection(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self._copy_fixture(Path(directory))
            readme = root / README_REL
            text = readme.read_text(encoding="utf-8")
            start = text.index("## Current State")
            end = text.find("\n## ", start + 1)
            section = text[start:end]
            self.assertIn("TRACER BULLET ID: TB-001", section)
            section = section.replace(
                "TRACER BULLET ID: TB-001",
                "TRACER BULLET ID: NONE / NOT CREATED",
            )
            readme.write_text(text[:start] + section + text[end:], encoding="utf-8")
            report = {"checks": [], "findings": []}
            _check_platform_readme_router_consistency(root, report)
            check = report["checks"][0]
            self.assertEqual("FAIL", check["status"], check["message"])


if __name__ == "__main__":
    unittest.main()
