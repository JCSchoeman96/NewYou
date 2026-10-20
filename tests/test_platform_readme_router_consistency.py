from __future__ import annotations

import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
README = DOCS / "README.md"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.77.md"
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
        cls.readme = README.read_text(encoding="utf-8")
        cls.current_prose = _current_readme_prose(cls.readme)
        cls.current_state = cls.readme.split("## Current State", 1)[1].split("\n## ", 1)[0]
        cls.atlas_routing = cls.readme.split("## Delivery Atlas routing", 1)[1].split("\n## ", 1)[0]
        cls.open_work_state = _open_work_lifecycle_state(OPEN_WORK.read_text(encoding="utf-8"))

    def test_delivery_atlas_routing_points_at_current_successor(self) -> None:
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.19.md", self.atlas_routing)
        self.assertNotRegex(self.atlas_routing, r"\(working/DELIVERY_ATLAS_WORKING_v0\.4\.16\.md\)")

    def test_current_prose_agrees_with_open_work_classification(self) -> None:
        self.assertEqual("NEW_TRACER_BULLET", self.open_work_state.get("proof_classification"))
        self.assertEqual("COMPLETE / FINALISED", self.open_work_state.get("architectural_proof_classification_status"))
        self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED", self.current_state)
        self.assertIn("PROOF CLASSIFICATION: NEW_TRACER_BULLET", self.current_state)
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", self.current_state)
        self.assertIn("NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION", self.current_state)

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
            stale_atlas = atlas.replace(
                "working/DELIVERY_ATLAS_WORKING_v0.4.19.md",
                "working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
                1,
            )
            stale_prose = prose.replace(atlas, stale_atlas, 1)
            readme.write_text(
                stale_prose + text.split("## Historical status evidence", 1)[1],
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)
            check = next(item for item in report["checks"] if item["name"] == "platform_readme_router_consistency")
            self.assertEqual("FAIL", check["status"])
            self.assertIn("v0.4.19", check["message"])

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
            check = next(item for item in report["checks"] if item["name"] == "platform_readme_router_consistency")
            self.assertEqual("PASS", check["status"])


if __name__ == "__main__":
    unittest.main()
