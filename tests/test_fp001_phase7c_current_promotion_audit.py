from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit


ROOT = Path(__file__).resolve().parents[1]
PROMOTION_RULE = "fp001_phase7c_final_contract_current_promotion"
CONTRACT_REL = "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
OPEN_WORK_REL = "docs/00_platform/02_OPEN_WORK_v1.2.70.md"
ARCHIVE_REL = "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"


class FP001Phase7CCurrentPromotionAuditTests(unittest.TestCase):
    def _copy_fixture(self, root: Path) -> tuple[Path, Path]:
        source_docs = ROOT / "docs" / "00_platform"
        fixture_docs = root / "docs" / "00_platform"
        shutil.copytree(source_docs, fixture_docs)
        manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        refresh_manifest(root, manifest_path)
        return root, manifest_path

    def _promotion_check(self, root: Path, manifest_path: Path) -> dict | None:
        report = run_audit(root, manifest_path)
        return next((item for item in report["checks"] if item["name"] == PROMOTION_RULE), None)

    def _mutate_contract_state(self, root: Path, key: str, value) -> None:
        path = root / CONTRACT_REL
        text = path.read_text(encoding="utf-8")
        start = "<!-- FP001_PHASE7C_CURRENT_STATUS_START -->"
        end = "<!-- FP001_PHASE7C_CURRENT_STATUS_END -->"
        begin = text.index(start)
        finish = text.index(end, begin)
        prefix = text[:begin]
        block = text[begin:finish]
        suffix = text[finish:]
        json_start = block.index("```json") + len("```json")
        json_end = block.index("```", json_start)
        state = json.loads(block[json_start:json_end])
        state[key] = value
        updated = block[:json_start] + "\n" + json.dumps(state, indent=2) + "\n" + block[json_end:]
        path.write_text(prefix + updated + suffix, encoding="utf-8")

    def _mutate_manifest_rule(self, root: Path, manifest_path: Path, key: str, value) -> None:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["integrity_rules"][PROMOTION_RULE][key] = value
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    def test_phase7c_current_status_promotion_passes_foundation_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_fixture(Path(directory))

            check = self._promotion_check(root, manifest_path)

            self.assertIsNotNone(check, "Foundation Integrity must register the Phase 7C current-status promotion check")
            self.assertEqual("PASS", check["status"], check["message"])

    def test_readme_current_state_rejects_the_pre_certification_candidate_route(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_fixture(Path(directory))
            readme = root / "docs/00_platform/README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n\nPHASE 7C IS IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING UNDER OPEN TRACKER #124.\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            check = self._promotion_check(root, manifest_path)

            self.assertIsNotNone(check, "Foundation Integrity promotion guard is missing")
            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn("README current state retains the pre-certification Phase 7C route", check["message"])

    def test_phase7c_current_status_promotion_fails_closed_on_lifecycle_mutations(self):
        mutations = (
            (
                "archived PR 125 candidate bytes",
                lambda root, manifest: (root / ARCHIVE_REL).write_bytes((root / ARCHIVE_REL).read_bytes() + b"\nchanged\n"),
            ),
            (
                "candidate and resulting-main tree identity",
                lambda root, manifest: self._mutate_manifest_rule(root, manifest, "candidate_tree_sha", "bad-tree"),
            ),
            (
                "resulting-main tree identity",
                lambda root, manifest: self._mutate_manifest_rule(root, manifest, "resulting_main_tree_sha", "bad-tree"),
            ),
            (
                "tree identity declaration",
                lambda root, manifest: self._mutate_manifest_rule(
                    root, manifest, "candidate_resulting_main_tree_identity", "FAIL"
                ),
            ),
            (
                "reviewed candidate head",
                lambda root, manifest: self._mutate_manifest_rule(root, manifest, "reviewed_head_sha", "bad-head"),
            ),
            (
                "PR 125 merge SHA",
                lambda root, manifest: self._mutate_manifest_rule(root, manifest, "merge_sha", "bad-merge"),
            ),
            (
                "resulting-main run is not successful",
                lambda root, manifest: self._mutate_manifest_rule(root, manifest, "resulting_main_fia_conclusion", "failure"),
            ),
            (
                "resulting-main run is not completed",
                lambda root, manifest: self._mutate_manifest_rule(root, manifest, "resulting_main_fia_status", "in_progress"),
            ),
            (
                "working contract loses current status",
                lambda root, manifest: (root / CONTRACT_REL).write_text(
                    (root / CONTRACT_REL).read_text(encoding="utf-8").replace("\nCURRENT\n", "\nNOT CURRENT\n", 1),
                    encoding="utf-8",
                ),
            ),
            (
                "proof classification selected early",
                lambda root, manifest: (root / CONTRACT_REL).write_text(
                    (root / CONTRACT_REL).read_text(encoding="utf-8").replace(
                        "PROOF CLASSIFICATION: NOT FINALISED", "PROOF CLASSIFICATION: NEW_TRACER_BULLET", 1
                    ),
                    encoding="utf-8",
                ),
            ),
            (
                "Phase 8 authorised early",
                lambda root, manifest: (root / CONTRACT_REL).write_text(
                    (root / CONTRACT_REL).read_text(encoding="utf-8").replace(
                        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
                        "PHASE 8 / APPLICATION IMPLEMENTATION: AUTHORISED",
                        1,
                    ),
                    encoding="utf-8",
                ),
            ),
            (
                "tracker 124 closed early",
                lambda root, manifest: self._mutate_contract_state(root, "phase_7c_execution_tracker_state", "CLOSED"),
            ),
            (
                "Open Work closes tracker 124 early",
                lambda root, manifest: (root / OPEN_WORK_REL).write_text(
                    (root / OPEN_WORK_REL).read_text(encoding="utf-8").replace(
                        "PHASE 7C TRACKER #124: OPEN THROUGH CURRENT-STATUS PROMOTION MERGE AND RESULTING-MAIN VERIFICATION",
                        "PHASE 7C TRACKER #124: CLOSED",
                        1,
                    ),
                    encoding="utf-8",
                ),
            ),
            (
                "predecessor archive path missing",
                lambda root, manifest: (root / "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.11.md").unlink(),
            ),
            (
                "substantive contract semantics drift",
                lambda root, manifest: (root / CONTRACT_REL).write_text(
                    (root / CONTRACT_REL).read_text(encoding="utf-8").replace(
                        "create an individual 18+ account", "create an individual account", 1
                    ),
                    encoding="utf-8",
                ),
            ),
            (
                "status-successor route bytes drift",
                lambda root, manifest: (root / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.14.md").write_text(
                    (root / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.14.md")
                    .read_text(encoding="utf-8")
                    .replace("Programme router #111 remains OPEN", "Programme router #111 is CLOSED", 1),
                    encoding="utf-8",
                ),
            ),
            (
                "README current state regresses to candidate status",
                lambda root, manifest: (root / "docs/00_platform/README.md").write_text(
                    (root / "docs/00_platform/README.md").read_text(encoding="utf-8")
                    + "\n\nPHASE 7C IS IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING UNDER OPEN TRACKER #124.\n",
                    encoding="utf-8",
                ),
            ),
            (
                "historical JIT certification evidence drift",
                lambda root, manifest: (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").write_bytes(
                    (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").read_bytes()
                    + b"\nchanged\n"
                ),
            ),
        )

        for name, mutate in mutations:
            with self.subTest(mutation=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_fixture(Path(directory))
                mutate(root, manifest_path)
                refresh_manifest(root, manifest_path)

                check = self._promotion_check(root, manifest_path)

                self.assertIsNotNone(check, "Foundation Integrity promotion guard is missing")
                self.assertEqual("FAIL", check["status"], check["message"])
