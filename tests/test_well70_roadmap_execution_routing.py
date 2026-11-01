"""WELL-70: current Roadmap execution routing matches post-WELL-66 Plane model."""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ROUTER_PATH = DOCS / "governance/CURRENT_GOVERNANCE_ROUTER.json"
FROZEN_ROUTER_PATH = DOCS / "history/platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json"
MANIFEST_PATH = DOCS / "history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
OPEN_WORK_PATH = DOCS / "history/02_OPEN_WORK_v1.2.90.md"
ARCHIVED_ROADMAP_V124 = DOCS / "history/platform/archive/05_ROADMAP_v1.2.4.md"

CURRENT_OPEN_WORK_AS_EXECUTION_AUTHORITY = re.compile(
    r"(?im)"
    r"(?:"
    r"current\s+open\s+work\s+(?:own|authoris(?:e|es)|path\s+it\s+identifies)"
    r"|open\s+work\s+own\s+programme\s+routing"
    r"|use\s+those\s+current\s+sources\s+for\s+operational\s+status"
    r"|see\s+current\s+open\s+work\s+§"
    r")"
)


class Well70RoadmapExecutionRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.router = json.loads(ROUTER_PATH.read_text(encoding="utf-8"))
        roadmap_entry = next(
            row for row in cls.router["governing_documents"]
            if row["document_id"] == "GOVERNING_ROADMAP"
        )
        cls.roadmap_path = ROOT / roadmap_entry["repository_path"]
        cls.roadmap = cls.roadmap_path.read_text(encoding="utf-8")
        cls.readme = (DOCS / "README.md").read_text(encoding="utf-8")

    def test_router_points_at_current_roadmap_successor(self) -> None:
        entry = next(row for row in self.router["governing_documents"] if row["document_id"] == "GOVERNING_ROADMAP")
        self.assertEqual("05_ROADMAP_v1.2.5.md", entry["canonical_filename"])
        self.assertEqual("1.2.5", entry["semver"])
        digest = hashlib.sha256(self.roadmap_path.read_bytes()).hexdigest()
        self.assertEqual(entry["sha256"], digest)

    def test_current_roadmap_does_not_name_open_work_as_live_execution_authority(self) -> None:
        section_21 = self.roadmap.split("# 21. Phase 7 handoff", 1)[1]
        self.assertIsNone(CURRENT_OPEN_WORK_AS_EXECUTION_AUTHORITY.search(section_21))
        self.assertIn("not current execution authority", section_21.casefold())

    def test_current_roadmap_identifies_plane_and_ready(self) -> None:
        for phrase in (
            "Plane project `WELL`",
            "dependency-cleared Plane **`Ready`**",
            "live execution state",
        ):
            self.assertIn(phrase, self.roadmap)

    def test_current_roadmap_identifies_authority_router(self) -> None:
        self.assertIn("CURRENT_GOVERNANCE_ROUTER.json", self.roadmap)
        self.assertIn("CURRENT_DELIVERY_ROUTER.json", self.roadmap)
        self.assertIn(
            "resolved by `docs/governance/CURRENT_GOVERNANCE_ROUTER.json`",
            self.roadmap,
        )

    def test_readme_is_not_restored_as_live_status_ledger(self) -> None:
        self.assertIn("Plane project `WELL`", self.readme)
        self.assertIn("live execution authority", self.readme)
        self.assertNotRegex(
            self.readme,
            r"(?im)^\s*[-*].*open work.*current execution authority",
        )

    def test_frozen_open_work_and_manifest_unchanged(self) -> None:
        open_work_hash = hashlib.sha256(OPEN_WORK_PATH.read_bytes()).hexdigest()
        self.assertEqual(
            "7ae61b682322628826d05e130546a644cb127baaf6f5fa737aa773aa19936ea5",
            open_work_hash,
        )
        frozen_router = json.loads(FROZEN_ROUTER_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            "2a8557193fc071996e23d9214980da22d48bdbf3",
            frozen_router["historical_integrity_baseline"]["git_blob_sha"],
        )

    def test_historical_open_work_and_patch_provenance_preserved(self) -> None:
        self.assertTrue(ARCHIVED_ROADMAP_V124.is_file())
        self.assertEqual(
            "99ee1e6b5e0d23b12a877e17a001b6b92250248fe1b2ab9c1a12e1e5ff966b3e",
            hashlib.sha256(ARCHIVED_ROADMAP_V124.read_bytes()).hexdigest(),
        )
        self.assertIn("archive/02_OPEN_WORK_v1.2.45.md", self.roadmap)
        self.assertIn("v1.1.4 Patch Scope", self.roadmap)
        self.assertIn(
            "README and the current Open Work path it identifies remain the operational route",
            self.roadmap,
        )


if __name__ == "__main__":
    unittest.main()
