from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit


SMALL_COUNTS = {
    "decisions": 1,
    "open_questions": 1,
    "architecture_law": 1,
    "architecture_requirements": 1,
    "reference_flows": 1,
    "domains": 1,
    "ownership_rows": 1,
    "feature_packs": 0,
}


class FoundationIntegrityAuditTests(unittest.TestCase):
    def test_clean_fixture_returns_pass_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertEqual([], report["findings"])

    def test_hash_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["sha256"] = "0" * 64
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(finding["check"] == "manifest_hash_parity" for finding in report["findings"])
            )

    def test_unresolved_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nSee OQ-999.\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(finding["check"] == "identifier_resolution" for finding in report["findings"])
            )

    def test_duplicate_definition_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "## DEC-001 — Duplicate\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "duplicate_definitions_dec" for finding in report["findings"])
            )

    def test_missing_roadmap_gate_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace("| OQ-001 |", "| Gate omitted |"),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "roadmap_gate_coverage" for finding in report["findings"])
            )

    def test_duplicate_roadmap_gate_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "## 14.1", "| OQ-001 | Duplicate |\n## 14.1"
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "roadmap_gate_coverage" for finding in report["findings"])
            )

    def test_multiple_domain_owners_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "04_DOMAIN_MAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "| Truth | **Example Domain** |",
                    "| Truth | **Example Domain** and **Other Domain** |",
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "domain_ownership_uniqueness" for finding in report["findings"])
            )

    def test_missing_current_version_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["semver"] = "9.9.9"
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "manifest_version_parity" for finding in report["findings"])
            )

    def test_refresh_manifest_updates_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text("## DEC-001 — Changed\n## OQ-001 — Example\n", encoding="utf-8")

            refresh_manifest(root, root / "manifest.json")
            manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
            expected_hash = hashlib.sha256(path.read_bytes()).hexdigest()

            self.assertEqual(expected_hash, manifest["governing_documents"][0]["sha256"])

    def _write_clean_fixture(self, root: Path) -> dict:
        files = {
            "docs/00_platform/01_DECISIONS_v1.2.1.md": (
                "## DEC-001 — Example\n"
                "## OQ-001 — Example\n"
            ),
            "docs/00_platform/05_ROADMAP_v1.0.0.md": (
                "# 14. Gate schedule\n"
                "| OQ-001 | Example |\n"
                "## 14.1 Non-OQ expert/vendor gates\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md": (
                "## ARC-001 — Example\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": (
                "### ARQ-TEST-001 — Example\n"
            ),
            "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": (
                "# 3. FLOW-01 — Example\n"
            ),
            "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md": (
                "## 3. Approved domain set\n"
                "| 1 | **Example Domain** | Example |\n"
                "## 4. Platform-wide business-truth ownership matrix\n"
                "| Business truth | Authoritative domain | Dependents | Rule |\n"
                "| Truth | **Example Domain** | None | READ |\n"
                "### 4.1 Ownership interpretation\n"
            ),
        }

        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        manifest = {"governing_documents": [], "reference_documents": []}
        for relative in files:
            path = root / relative
            manifest["governing_documents"].append(
                {
                    "document_id": path.stem,
                    "canonical_filename": path.name,
                    "semver": path.name.split("_v", 1)[1][:-3],
                    "repository_path": relative,
                    "authority_class": "TEST",
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                }
            )

        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest


if __name__ == "__main__":
    unittest.main()
