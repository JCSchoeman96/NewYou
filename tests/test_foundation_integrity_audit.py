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

FAD72C1_FROZEN_HASHES = {
    "docs/00_platform/archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/archive/00_PLATFORM_v1.2.1.md": "56a2b9a5db42a81e287f0c61deae37d6bbce5b19f48f67732584160b455f935a",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.0.0.md": "87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md": "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "cdf09ecced658635572a20e4f2feb04120b4f856e81762ef5af9ba179a11c40e",
    "docs/00_platform/archive/ARCHITECTURE_LAW_WORKING_v0.35.0.md": "a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639",
    "docs/00_platform/archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20",
}


class FoundationIntegrityAuditTests(unittest.TestCase):
    def test_clean_fixture_returns_pass_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertEqual([], report["findings"])

    def test_production_audit_uses_manifest_expectations(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["integrity_rules"]["expected_counts"]["decisions"] = 2
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            decision_count_check = next(
                check for check in report["checks"] if check["name"] == "definition_count_dec"
            )
            self.assertEqual("DEC definition count is 1, expected 2", decision_count_check["message"])

    def test_completed_stage_3a1_readiness_wording_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            readme.write_text(
                "\n".join(
                    [f"`{entry['canonical_filename']}`" for entry in manifest["governing_documents"]]
                    + [
                        "PLANNING FOUNDATION: READY",
                        "STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE",
                        "STAGE 3A.2 — GOVERNED AR-000 AMENDMENT (NOT_STARTED / NEXT)",
                        "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json")

            readiness_check = next(
                check for check in report["checks"] if check["name"] == "readiness_wording"
            )
            self.assertEqual("PASS", readiness_check["status"])

    def test_source_at_freeze_references_are_not_stale(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            source_at_freeze = root / "docs" / "00_platform" / "reference" / "ARCHITECTURE_LAW_WORKING_v0.35.0.md"
            source_at_freeze.write_text(
                source_at_freeze.read_text(encoding="utf-8")
                + "\nSource tracker at freeze: 02_OPEN_WORK_v1.2.23.md\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)02_OPEN_WORK_v1\.2\.(?:[0-9]|1[0-9]|2[0-6])\.md"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = ["ROADMAP"]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_non_navigation_document_is_not_scanned_for_stale_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            current_navigation = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            current_navigation.write_text(
                current_navigation.read_text(encoding="utf-8") + "\nOLD_TRACKER_MARKER\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"OLD_TRACKER_MARKER"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = []
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_declared_current_navigation_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            current_navigation = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            current_navigation.write_text(
                current_navigation.read_text(encoding="utf-8") + "\nOLD_TRACKER_MARKER\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"OLD_TRACKER_MARKER"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = ["ROADMAP"]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertTrue(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_frozen_provenance_hash_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            manifest["governing_documents"][0]["provenance_sha256"] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
            path.write_text(path.read_text(encoding="utf-8") + "\nChanged after freeze.\n", encoding="utf-8")
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "frozen_provenance_hash" for finding in report["findings"])
            )

    def test_fad72c1_frozen_artifacts_match_accepted_hashes(self):
        root = Path(__file__).resolve().parents[1]

        for relative, expected_hash in FAD72C1_FROZEN_HASHES.items():
            with self.subTest(path=relative):
                actual_hash = hashlib.sha256((root / relative).read_bytes()).hexdigest()
                self.assertEqual(expected_hash, actual_hash)

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

    def test_duplicate_domain_name_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "04_DOMAIN_MAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "## 4. Platform-wide",
                    "| 2 | **Example Domain** | Duplicate |\n## 4. Platform-wide",
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "duplicate_domain_names" for finding in report["findings"])
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

    def test_document_version_metadata_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "**Document version:** v1.2.1", "**Document version:** v9.9.9"
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "document_version_parity" for finding in report["findings"])
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
                "- **Document version:** v1.2.1\n"
                "## DEC-001 — Example\n"
                "## OQ-001 — Example\n"
            ),
            "docs/00_platform/05_ROADMAP_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "# 14. Gate schedule\n"
                "| OQ-001 | Example |\n"
                "## 14.1 Non-OQ expert/vendor gates\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md": (
                "- **Document version:** v0.35.0\n"
                "## ARC-001 — Example\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "### ARQ-TEST-001 — Example\n"
            ),
            "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": (
                "- **Document version:** v0.2.0\n"
                "# 3. FLOW-01 — Example\n"
            ),
            "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
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

        manifest = {
            "governing_documents": [],
            "reference_documents": [],
            "historical_documents": [],
            "integrity_rules": {
                "document_roots": {
                    "governing": "docs/00_platform",
                    "reference": "docs/00_platform/reference",
                    "historical": "docs/00_platform/archive",
                    "context_index": "docs/00_platform/README.md",
                },
                "expected_counts": SMALL_COUNTS,
                "contiguous_ranges": {
                    "DEC": {"prefix": "DEC", "start": 1, "end": 1, "width": 3},
                    "OQ": {"prefix": "OQ", "start": 1, "end": 1, "width": 3},
                    "ARC": {"prefix": "ARC", "start": 1, "end": 1, "width": 3},
                    "FLOW": {"prefix": "FLOW", "start": 1, "end": 1, "width": 2},
                },
                "definition_sources": {
                    "decisions": "DECISION_REGISTER",
                    "architecture_law": "ARCHITECTURE_LAW_EVIDENCE",
                    "architecture_requirements": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
                    "reference_flows": "REFERENCE_FLOW_EVIDENCE",
                    "roadmap": "ROADMAP",
                    "domain_map": "DOMAIN_LAW",
                },
                "graph_rules": {
                    "stale_reference_patterns": [],
                    "reference_header_lines": 35,
                    "frozen_provenance_policy": "frozen_provenance",
                    "navigation_document_ids": ["ROADMAP"],
                },
            },
        }
        authority_classes = {
            "01_DECISIONS_v1.2.1.md": "DECISION_REGISTER",
            "05_ROADMAP_v1.0.0.md": "ROADMAP",
            "ARCHITECTURE_LAW_WORKING_v0.35.0.md": "ARCHITECTURE_LAW_EVIDENCE",
            "ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "REFERENCE_FLOW_EVIDENCE",
            "04_DOMAIN_MAP_v1.0.0.md": "DOMAIN_LAW",
        }
        document_ids = {
            "01_DECISIONS_v1.2.1.md": "DECISION_REGISTER",
            "05_ROADMAP_v1.0.0.md": "ROADMAP",
            "ARCHITECTURE_LAW_WORKING_v0.35.0.md": "ARCHITECTURE_LAW_EVIDENCE",
            "ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "REFERENCE_FLOW_EVIDENCE",
            "04_DOMAIN_MAP_v1.0.0.md": "DOMAIN_LAW",
        }
        for relative in files:
            path = root / relative
            manifest["governing_documents"].append(
                {
                    "document_id": document_ids[path.name],
                    "canonical_filename": path.name,
                    "semver": path.name.split("_v", 1)[1][:-3],
                    "repository_path": relative,
                    "authority_class": authority_classes[path.name],
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                }
            )

        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest


if __name__ == "__main__":
    unittest.main()
