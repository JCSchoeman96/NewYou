from __future__ import annotations

import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit
from foundation_test_support import current_document_path, current_working_path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

STALE_PATTERNS = (
    r"(?i)proof classification (?:is|remains) not finalised",
    r"(?i)architectural proof classification is next",
    r"(?i)architectural proof classification.*remains unperformed",
)


def _current_readme_prose(text: str) -> str:
    return text.split("## Historical status evidence", 1)[0]


def _open_work_lifecycle_state(text: str) -> dict:
    match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        text,
        re.DOTALL,
    )
    return json.loads(match.group(1)) if match else {}


class PlatformReadmeRouterConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.open_work_path = current_document_path(ROOT, "OPEN_WORK")
        cls.atlas_path = current_working_path(ROOT, "DELIVERY_ATLAS_WORKING_")
        cls.readme = README.read_text(encoding="utf-8")
        cls.current_prose = _current_readme_prose(cls.readme)
        cls.current_state = cls.readme.split("## Current State", 1)[1].split("\n## ", 1)[0]
        cls.atlas_routing = cls.readme.split("## Delivery Atlas routing", 1)[1].split("\n## ", 1)[0]
        cls.open_work_state = _open_work_lifecycle_state(cls.open_work_path.read_text(encoding="utf-8"))

    def test_delivery_atlas_routing_points_at_current_successor(self) -> None:
        current_route = self.atlas_path.relative_to(DOCS).as_posix()
        self.assertIn(current_route, self.atlas_routing)
        self.assertNotRegex(self.atlas_routing, r"\(working/DELIVERY_ATLAS_WORKING_v0\.4\.16\.md\)")

    def test_current_prose_agrees_with_open_work_classification(self) -> None:
        self.assertEqual("NEW_TRACER_BULLET", self.open_work_state.get("proof_classification"))
        self.assertEqual("COMPLETE / FINALISED", self.open_work_state.get("architectural_proof_classification_status"))
        self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED", self.current_state)
        self.assertIn("PROOF CLASSIFICATION: NEW_TRACER_BULLET", self.current_state)
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", self.current_state)
        self.assertIn(self.open_work_state["next_governance_action"], self.current_state)

    def test_current_prose_cannot_regress_to_stale_classification_routing(self) -> None:
        for pattern in STALE_PATTERNS:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, self.current_prose))

    def test_foundation_integrity_rejects_stale_router_prose_but_allows_historical_section(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(DOCS, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            refresh_manifest(root, manifest_path)

            readme = fixture_docs / "README.md"
            text = readme.read_text(encoding="utf-8")
            prose = _current_readme_prose(text)
            atlas = prose.split("## Delivery Atlas routing", 1)[1].split("\n## ", 1)[0]
            current_atlas_path = current_working_path(root, "DELIVERY_ATLAS_WORKING_")
            current_route = current_atlas_path.relative_to(fixture_docs).as_posix()
            current_atlas = current_atlas_path.read_text(encoding="utf-8")
            predecessor_match = re.search(r"(?m)^- \*\*Predecessor:\*\* `archive/([^`]+)`", current_atlas)
            self.assertIsNotNone(predecessor_match)
            stale_route = "working/" + predecessor_match.group(1)
            stale_atlas = atlas.replace(current_route, stale_route, 1)
            stale_prose = prose.replace(atlas, stale_atlas, 1)
            readme.write_text(
                stale_prose + text.split("## Historical status evidence", 1)[1],
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)
            check = next(item for item in report["checks"] if item["name"] == "phase8_approved_status_successor_current")
            self.assertEqual("FAIL", check["status"])
            self.assertIn(current_atlas_path.name.rsplit("v", 1)[-1].removesuffix(".md"), check["message"])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(DOCS, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            refresh_manifest(root, manifest_path)

            readme = fixture_docs / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n\n## Historical status evidence\n\nProof classification remains NOT FINALISED in this preserved snapshot only.\n",
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)
            checks = {item["name"]: item for item in report["checks"]}
            self.assertEqual("PASS", checks["phase8_approved_status_successor_current"]["status"])
            self.assertEqual("PASS", checks["platform_readme_router_consistency"]["status"])


if __name__ == "__main__":
    unittest.main()
