"""Regression tests for historical vs current Foundation certification context."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from foundation_test_support import (
    HISTORICAL_README_RELATIVE,
    HISTORICAL_README_SHA256,
    current_router_data,
    current_router_working_path,
    frozen_manifest_document_by_id,
    frozen_manifest_working_path,
    frozen_open_work_path,
    historical_platform_readme_path,
    historical_platform_readme_text,
    live_platform_readme_path,
    live_platform_readme_text,
    manifest_data,
)


ROOT = Path(__file__).resolve().parents[1]


class FoundationContextBoundaryTest(unittest.TestCase):
    def test_historical_readme_is_archived_not_live(self):
        historical = historical_platform_readme_path(ROOT)
        live = live_platform_readme_path(ROOT)
        self.assertNotEqual(historical.resolve(), live.resolve())
        self.assertEqual(historical.relative_to(ROOT), HISTORICAL_README_RELATIVE)
        self.assertIn("## Current State", historical.read_text(encoding="utf-8"))
        self.assertNotIn("## Current State", live.read_text(encoding="utf-8"))

    def test_historical_readme_rejects_altered_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs" / "00_platform" / "archive").mkdir(parents=True)
            path = root / HISTORICAL_README_RELATIVE
            path.write_text("corrupted historical readme\n", encoding="utf-8")
            with self.assertRaises(AssertionError):
                historical_platform_readme_path(root)

    def test_live_readme_resolver_never_returns_historical_archive(self):
        text = live_platform_readme_text(ROOT)
        self.assertIn("Plane project `WELL`", text)
        self.assertNotIn("## Default Agent Context", text)
        historical = historical_platform_readme_text(ROOT)
        self.assertNotEqual(text, historical)

    def test_frozen_open_work_is_pinned_legacy_not_live_execution(self):
        path = frozen_open_work_path(ROOT)
        self.assertEqual(path.name, "02_OPEN_WORK_v1.2.90.md")
        router = current_router_data(ROOT)
        snapshot = next(
            entry
            for entry in router["legacy_snapshots"]
            if entry["document_id"] == "OPEN_WORK_FINAL_LEGACY_SNAPSHOT"
        )
        self.assertFalse(snapshot["live_execution_authority"])
        manifest_open = frozen_manifest_document_by_id(ROOT, "OPEN_WORK")
        self.assertEqual(path.resolve(), manifest_open.resolve())

    def test_frozen_manifest_document_by_id_resolves_governing_route(self):
        path = frozen_manifest_document_by_id(ROOT, "ROADMAP")
        entry = next(
            item
            for group in ("governing_documents", "reference_documents", "historical_documents")
            for item in manifest_data(ROOT).get(group, [])
            if item.get("document_id") == "ROADMAP"
            and item.get("lifecycle", "current") != "historical"
        )
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        self.assertEqual(digest, entry["sha256"])
        live = live_platform_readme_text(ROOT)
        self.assertNotIn("## Active Working Artifacts", live)
        path = frozen_manifest_working_path(ROOT, "DELIVERY_ATLAS_WORKING_")
        self.assertTrue(path.is_file())
        self.assertIn("DELIVERY_ATLAS_WORKING_", path.name)

    def test_current_router_working_path_matches_router_only(self):
        path = current_router_working_path(ROOT, "HARDEN-02_CONTRACT_WORKING_")
        self.assertTrue(path.name.startswith("HARDEN-02_CONTRACT_WORKING_"))
        self.assertIn(str(path.relative_to(ROOT)), current_router_data(ROOT)["working_semantic_routes"])

    def test_frozen_manifest_working_path_does_not_depend_on_live_readme_sections(self):
        live = live_platform_readme_text(ROOT)
        self.assertNotIn("## Active Working Artifacts", live)
        path = frozen_manifest_working_path(ROOT, "DELIVERY_ATLAS_WORKING_")
        self.assertTrue(path.is_file())
        self.assertIn("DELIVERY_ATLAS_WORKING_", path.name)


if __name__ == "__main__":
    unittest.main()
