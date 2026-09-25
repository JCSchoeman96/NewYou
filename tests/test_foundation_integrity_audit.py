from __future__ import annotations

import hashlib
import json
import re
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
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/archive/00_PLATFORM_v1.2.1.md": "56a2b9a5db42a81e287f0c61deae37d6bbce5b19f48f67732584160b455f935a",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.0.0.md": "87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md": "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "cdf09ecced658635572a20e4f2feb04120b4f856e81762ef5af9ba179a11c40e",
    "docs/00_platform/archive/ARCHITECTURE_LAW_WORKING_v0.35.0.md": "a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639",
    "docs/00_platform/archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20",
}


class FoundationIntegrityAuditTests(unittest.TestCase):
    def test_frontend_experience_system_cannot_be_omitted_from_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"] = [
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] != "FRONTEND_EXPERIENCE_SYSTEM"
            ]
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "readme_manifest_current_authority_parity"
                    for finding in report["findings"]
                )
            )

    def test_manifest_current_authority_cannot_add_unrouted_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            duplicate = dict(manifest["governing_documents"][0])
            duplicate.update(
                document_id="UNROUTED_AUTHORITY",
                canonical_filename="UNROUTED_AUTHORITY_v1.0.0.md",
                semver="1.0.0",
                repository_path="docs/00_platform/UNROUTED_AUTHORITY_v1.0.0.md",
                authority_class="UNROUTED_AUTHORITY",
                sha256="0" * 64,
                superseded_version=None,
            )
            path = root / duplicate["repository_path"]
            path.write_text("- **Document version:** v1.0.0\n", encoding="utf-8")
            duplicate["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            manifest["governing_documents"].append(duplicate)
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "readme_manifest_current_authority_parity"
                    for finding in report["findings"]
                )
            )

    def test_historical_decision_register_must_have_historical_lifecycle(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["historical_documents"][0]["lifecycle"] = "current"
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "manifest_lifecycle" for finding in report["findings"])
            )

    def test_archive_artifact_cannot_be_routed_as_current_governing_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            entry = next(
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] == "DECISION_REGISTER"
            )
            entry["repository_path"] = "docs/00_platform/archive/01_DECISIONS_v1.2.1.md"
            path = root / entry["repository_path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("- **Document version:** v1.2.1\n", encoding="utf-8")
            entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            self._write_manifest(root, manifest)
            self._write_route_readme(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_path_classification"
                    for finding in report["findings"]
                )
            )

    def test_reference_artifact_must_remain_under_reference_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            entry = manifest["reference_documents"][0]
            entry["repository_path"] = "docs/00_platform/ARCHITECTURE_LAW_WORKING_v0.35.0.md"
            path = root / entry["repository_path"]
            path.write_text("- **Document version:** v0.35.0\n## ARC-001 — Example\n", encoding="utf-8")
            entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_path_classification"
                    for finding in report["findings"]
                )
            )

    def test_historical_artifact_must_remain_under_archive_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            entry = manifest["historical_documents"][0]
            entry["repository_path"] = "docs/00_platform/01_DECISIONS_v0.9.0.md"
            path = root / entry["repository_path"]
            path.write_text("- **Document version:** v0.9.0\n", encoding="utf-8")
            entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_path_classification"
                    for finding in report["findings"]
                )
            )

    def test_non_array_manifest_section_fails_without_crashing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["reference_documents"] = None
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(finding["check"] == "manifest_schema" for finding in report["findings"])
            )

    def test_current_authority_role_must_be_unique(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            duplicate = dict(
                next(
                    entry
                    for entry in manifest["governing_documents"]
                    if entry["document_id"] == "DECISION_REGISTER"
                )
            )
            duplicate.update(
                document_id="DECISION_REGISTER_DUPLICATE",
                canonical_filename="01_DECISIONS_v9.9.9.md",
                semver="9.9.9",
                repository_path="docs/00_platform/01_DECISIONS_v9.9.9.md",
                sha256="0" * 64,
                superseded_version=None,
            )
            path = root / duplicate["repository_path"]
            path.write_text("- **Document version:** v9.9.9\n", encoding="utf-8")
            duplicate["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            manifest["governing_documents"].append(duplicate)
            self._write_manifest(root, manifest)
            self._write_route_readme(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_role_uniqueness"
                    for finding in report["findings"]
                )
            )

    def test_reference_document_cannot_claim_a_singular_current_authority_role(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            relative = "docs/00_platform/reference/DECISION_REGISTER_REFERENCE_v1.0.0.md"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("- **Document version:** v1.0.0\n", encoding="utf-8")
            manifest["reference_documents"].append(
                {
                    "document_id": "MISCLASSIFIED_DECISION_REGISTER_REFERENCE",
                    "canonical_filename": path.name,
                    "semver": "1.0.0",
                    "repository_path": relative,
                    "authority_class": "DECISION_REGISTER",
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                    "lifecycle": "current",
                }
            )
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_role_uniqueness"
                    for finding in report["findings"]
                )
            )

    def test_manifest_entry_requires_lifecycle(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            del manifest["governing_documents"][0]["lifecycle"]
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(any(finding["check"] == "manifest_schema" for finding in report["findings"]))

    def test_manifest_rejects_non_string_required_entry_fields(self):
        for array_name, field, value in (
            ("reference_documents", "authority_class", ["DECISION_REGISTER"]),
            ("historical_documents", "document_id", None),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = self._write_clean_fixture(root)
                manifest[array_name][0][field] = value
                self._write_manifest(root, manifest)

                report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

                self.assertEqual("FAIL", report["status"])
                self.assertTrue(
                    any(finding["check"] == "manifest_schema" for finding in report["findings"])
                )

    def test_manifest_rejects_unknown_lifecycle(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["lifecycle"] = "pending"
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "manifest_lifecycle" for finding in report["findings"])
            )

    def test_manifest_rejects_non_normalized_path_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            entry = next(
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] == "DECISION_REGISTER"
            )
            entry["repository_path"] = "docs/00_platform/../DECISIONS_v1.2.1.md"
            self._write_manifest(root, manifest)
            self._write_route_readme(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_path_normalization"
                    for finding in report["findings"]
                )
            )

    def test_readme_and_manifest_current_versions_must_match(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            self._write_manifest(root, manifest)
            self._write_route_readme(root, manifest, overrides={"DECISION_REGISTER": {"semver": "9.9.9"}})

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "readme_manifest_current_authority_parity"
                    for finding in report["findings"]
                )
            )

    def test_frontend_experience_system_context_must_remain_conditional(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            entry = next(
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] == "FRONTEND_EXPERIENCE_SYSTEM"
            )
            entry["context_mode"] = "default"
            self._write_manifest(root, manifest)
            self._write_route_readme(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "readme_manifest_current_authority_parity"
                    for finding in report["findings"]
                )
            )

    def test_current_filename_in_archive_does_not_satisfy_current_route(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            self._write_manifest(root, manifest)
            self._write_route_readme(
                root,
                manifest,
                omit_document_id="OPEN_WORK",
                archive_lines=["- `02_OPEN_WORK_v1.0.0.md`"],
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "readme_manifest_current_authority_parity"
                    for finding in report["findings"]
                )
            )

    def test_declared_predecessor_must_be_registered_as_historical(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            next(
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] == "DECISION_REGISTER"
            )["superseded_version"] = "0.8.0"
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_predecessor_consistency"
                    for finding in report["findings"]
                )
            )

    def test_current_artifact_cannot_declare_itself_as_predecessor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            decision_register = next(
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] == "DECISION_REGISTER"
            )
            decision_register["superseded_version"] = decision_register["semver"]
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_predecessor_consistency"
                    for finding in report["findings"]
                )
            )

    def test_predecessor_version_must_be_older_than_current_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            decision_register = next(
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] == "DECISION_REGISTER"
            )
            decision_register["superseded_version"] = "2.0.0"
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_predecessor_consistency"
                    for finding in report["findings"]
                )
            )

    def test_current_reference_cannot_reuse_a_historical_predecessor_filename(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            historical_relative = "docs/00_platform/archive/01_DECISIONS_v0.8.0.md"
            historical_path = root / historical_relative
            historical_path.write_text("- **Document version:** v0.8.0\n", encoding="utf-8")
            manifest["historical_documents"].append(
                {
                    "document_id": "DECISION_REGISTER_V0_8_0",
                    "canonical_filename": historical_path.name,
                    "semver": "0.8.0",
                    "repository_path": historical_relative,
                    "authority_class": "DECISION_REGISTER_HISTORICAL",
                    "sha256": hashlib.sha256(historical_path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                    "lifecycle": "historical",
                }
            )
            relative = "docs/00_platform/reference/01_DECISIONS_v0.8.0.md"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("- **Document version:** v0.8.0\n", encoding="utf-8")
            manifest["reference_documents"].append(
                {
                    "document_id": "CURRENT_REFERENCE_WITH_PREDECESSOR_NAME",
                    "canonical_filename": path.name,
                    "semver": "0.8.0",
                    "repository_path": relative,
                    "authority_class": "DECISION_REGISTER_PREDECESSOR_REFERENCE",
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                    "lifecycle": "current",
                }
            )
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_predecessor_consistency"
                    for finding in report["findings"]
                )
            )

    def test_production_graph_does_not_read_traversal_context_index(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "repo"
            root.mkdir()
            outside = parent / "outside"
            outside.mkdir()
            outside_readme = outside / "README.md"
            outside_readme.write_text("02_OPEN_WORK_v1.2.26.md\n", encoding="utf-8")
            manifest = self._write_clean_fixture(root)
            manifest["integrity_rules"]["document_roots"]["context_index"] = "../outside/README.md"
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)02_OPEN_WORK_v1\.2\.26\.md"
            ]
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_production_graph_does_not_read_traversal_navigation_path(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "repo"
            root.mkdir()
            outside = parent / "02_OPEN_WORK_v1.2.26.md"
            outside.write_text("02_OPEN_WORK_v1.2.26.md\n", encoding="utf-8")
            manifest = self._write_clean_fixture(root)
            open_work = next(
                entry for entry in manifest["governing_documents"] if entry["document_id"] == "OPEN_WORK"
            )
            open_work["canonical_filename"] = outside.name
            open_work["semver"] = "1.2.26"
            open_work["repository_path"] = "../02_OPEN_WORK_v1.2.26.md"
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)02_OPEN_WORK_v1\.2\.26\.md"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = ["OPEN_WORK"]
            self._write_manifest(root, manifest)

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_blocked_state_rejects_each_explicit_application_root(self):
        for relative in ("mix.exs", "lib/example.ex", "config/", "priv/repo/migrations/001_create_example.exs", "assets/"):
            with self.subTest(path=relative), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self._write_clean_fixture(root)
                path = root / relative.rstrip("/")
                if relative.endswith("/"):
                    path.mkdir(parents=True)
                else:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text("# application root\n", encoding="utf-8")

                report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

                self.assertEqual("FAIL", report["status"])
                self.assertTrue(
                    any(
                        finding["check"] == "development_entry_repository_boundary"
                        and finding["path"] == relative.rstrip("/").split("/", 1)[0]
                        for finding in report["findings"]
                    )
                )

    def test_blocked_state_allows_docs_tools_and_tests(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            for relative in ("docs/notes.md", "tools/check.py", "tests/test_example.py"):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# allowed while blocked\n", encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertFalse(
                any(
                    finding["check"] == "development_entry_repository_boundary"
                    for finding in report["findings"]
                )
            )

    def test_authorised_state_allows_application_roots(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root, application_implementation="AUTHORISED")
            path = root / "lib" / "example.ex"
            path.parent.mkdir(parents=True)
            path.write_text("defmodule Example do\nend\n", encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            boundary_checks = [
                check
                for check in report["checks"]
                if check["name"] == "development_entry_repository_boundary"
            ]
            self.assertTrue(boundary_checks)
            self.assertTrue(all(check["status"] == "PASS" for check in boundary_checks))
            self.assertFalse(
                any(
                    finding["check"] == "development_entry_repository_boundary"
                    for finding in report["findings"]
                )
            )
            self.assertTrue(
                any(finding["check"] == "development_entry_formal_gate" for finding in report["findings"])
            )

    def test_unknown_application_state_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root, application_implementation="UNKNOWN")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "development_entry_repository_boundary"
                    for finding in report["findings"]
                )
            )

    def test_missing_application_state_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root, include_application_implementation=False)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "development_entry_repository_boundary"
                    for finding in report["findings"]
                )
            )

    def test_wrong_type_application_state_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root, application_implementation=[])

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "development_entry_repository_boundary"
                    for finding in report["findings"]
                )
            )

    def test_duplicate_application_state_key_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            open_work = root / "docs" / "00_platform" / "02_OPEN_WORK_v1.0.0.md"
            open_work.write_text(
                "<!-- HARDEN_02_RECOVERY_STATE_START -->\n"
                "```json\n"
                '{"application_implementation":"BLOCKED","application_implementation":"AUTHORISED"}\n'
                "```\n"
                "<!-- HARDEN_02_RECOVERY_STATE_END -->\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "development_entry_repository_boundary"
                    for finding in report["findings"]
                )
            )

    def test_workflow_runs_foundation_audit_for_all_pull_requests_and_main_pushes(self):
        workflow = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "foundation-integrity.yml"
        text = workflow.read_text(encoding="utf-8")

        self.assertRegex(text, r"(?m)^  pull_request:\s*$")
        self.assertRegex(text, r"(?ms)^  push:\n    branches:\n      - main\s*$")
        self.assertNotIn("paths:", text)
        self.assertIn("python tools/foundation_integrity_audit.py", text)
        self.assertNotIn("harden_02_github_verifier.py", text)

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

    def test_readme_active_state_mirror_matches_open_work(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)

            report = run_audit(root, root / "manifest.json")

            mirror_check = next(
                check for check in report["checks"] if check["name"] == "readme_active_state_mirror"
            )
            self.assertEqual("PASS", mirror_check["status"])

    def test_readme_active_state_mirror_rejects_phase_7c_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            self._write_route_readme(root, manifest, mirror_overrides={"phase_7c": "READY"})

            report = run_audit(root, root / "manifest.json")

            self.assertTrue(
                any(finding["check"] == "readme_active_state_mirror" for finding in report["findings"])
            )

    def test_readme_active_state_mirror_rejects_application_state_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            self._write_route_readme(
                root,
                manifest,
                mirror_overrides={"application_implementation": "AUTHORISED"},
            )

            report = run_audit(root, root / "manifest.json")

            self.assertTrue(
                any(finding["check"] == "readme_active_state_mirror" for finding in report["findings"])
            )

    def test_readme_active_state_mirror_rejects_duplicate_current_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs/00_platform/README.md"
            text = readme.read_text(encoding="utf-8")
            text = text.replace(
                '"current_stage": "EXAMPLE",',
                '"current_stage": "EXAMPLE",\n  "current_stage": "CONFLICTING",',
                1,
            )
            readme.write_text(text, encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertTrue(
                any(finding["check"] == "readme_active_state_mirror" for finding in report["findings"])
            )

    def test_readme_active_state_mirror_rejects_missing_declaration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs/00_platform/README.md"
            text = readme.read_text(encoding="utf-8").replace('  "next_stage": "EXAMPLE",\n', "", 1)
            readme.write_text(text, encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertTrue(
                any(finding["check"] == "readme_active_state_mirror" for finding in report["findings"])
            )

    def test_source_at_freeze_ready_prose_does_not_override_active_state_mirror(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs/00_platform/README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\nsource-at-freeze: Phase 7C READY; application implementation AUTHORIZED.\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "readme_active_state_mirror" for finding in report["findings"])
            )

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

    def _write_clean_fixture(
        self,
        root: Path,
        *,
        application_implementation: str = "BLOCKED",
        include_application_implementation: bool = True,
    ) -> dict:
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
            "docs/00_platform/02_OPEN_WORK_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "<!-- HARDEN_02_RECOVERY_STATE_START -->\n"
                "```json\n"
                + json.dumps(
                    {
                        "current_stage": "EXAMPLE",
                        "next_stage": "EXAMPLE",
                        "communications": "REQUIRED / NOT_STARTED",
                        "conditional_dossiers": {
                            "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                            "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                            "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                            "analytics": "NOT REQUIRED",
                        },
                        "phase_7c": "BLOCKED / NOT_STARTED",
                        "proof_classification": "NOT FINALISED",
                        "formal_artifacts": [
                            {
                                "registry_id": "FP001_SKELETON_GATE_MANIFEST",
                                "formal_type": "FEATURE_PACK_SKELETON_GATE_MANIFEST",
                                "path": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md",
                                "status": "COMPLETE",
                                "requirement": "REQUIRED",
                            },
                            {
                                "registry_id": "FP001_IDENTITY_ACCESS_JIT",
                                "formal_type": "JIT_DOMAIN_DOSSIER",
                                "path": "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
                                "status": "COMPLETE",
                                "requirement": "REQUIRED",
                            },
                            {
                                "registry_id": "FP001_COMMUNICATIONS_JIT",
                                "formal_type": "JIT_DOMAIN_DOSSIER",
                                "path": None,
                                "status": "NOT_STARTED",
                                "requirement": "REQUIRED",
                            },
                            {
                                "registry_id": "FP001_FINAL_CONTRACT",
                                "formal_type": "FINAL_FEATURE_PACK_CONTRACT",
                                "path": None,
                                "status": "NOT_STARTED",
                                "requirement": "REQUIRED",
                            },
                        ],
                        **(
                            {"application_implementation": application_implementation}
                            if include_application_implementation
                            else {}
                        ),
                    }
                )
                + "\n```\n"
                "<!-- HARDEN_02_RECOVERY_STATE_END -->\n"
            ),
            "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.0.0.md": "- **Document version:** v1.0.0\n",
            "docs/00_platform/00_PLATFORM_v1.0.0.md": "- **Document version:** v1.0.0\n",
            "docs/00_platform/03_ARCHITECTURE_v1.0.0.md": "- **Document version:** v1.0.0\n",
            "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "- **Document version:** v1.0.0\n",
            "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": "- **Document version:** v1.0.0\n",
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": (
                "PHASE 7A WORKING ARTIFACT\n"
            ),
            "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": (
                "PHASE 7B JIT DOMAIN DOSSIER\n"
            ),
            "docs/00_platform/archive/01_DECISIONS_v0.9.0.md": "- **Document version:** v0.9.0\n",
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
        document_metadata = {
            "PROJECT_NORTH_STAR_AND_MVP_v1.0.0.md": ("PROJECT_NORTH_STAR_AND_MVP", "PRODUCT_NORTH_STAR", "default"),
            "00_PLATFORM_v1.0.0.md": ("PLATFORM_BASELINE", "PLATFORM_PRODUCT_LAW", "default"),
            "01_DECISIONS_v1.2.1.md": ("DECISION_REGISTER", "DECISION_REGISTER", "default"),
            "02_OPEN_WORK_v1.0.0.md": ("OPEN_WORK", "PLANNING_TRACKER", "default"),
            "03_ARCHITECTURE_v1.0.0.md": ("ARCHITECTURE_SYNTHESIS", "ARCHITECTURE_SYNTHESIS", "default"),
            "04_DOMAIN_MAP_v1.0.0.md": ("DOMAIN_MAP", "DOMAIN_LAW", "default"),
            "05_ROADMAP_v1.0.0.md": ("ROADMAP", "ROADMAP", "default"),
            "PLATFORM_OPERATING_MODEL_v1.0.0.md": ("PLATFORM_OPERATING_MODEL", "PLATFORM_OPERATING_MODEL", "default"),
            "FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": ("FRONTEND_EXPERIENCE_SYSTEM", "FRONTEND_EXPERIENCE_SYSTEM", "conditional"),
        }
        reference_metadata = {
            "ARCHITECTURE_LAW_WORKING_v0.35.0.md": ("ARCHITECTURE_LAW_EVIDENCE", "ARCHITECTURE_LAW_EVIDENCE"),
            "ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": ("ARCHITECTURE_REQUIREMENTS_EVIDENCE", "ARCHITECTURE_REQUIREMENTS_EVIDENCE"),
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": ("REFERENCE_FLOW_EVIDENCE", "REFERENCE_FLOW_EVIDENCE"),
        }
        manifest["governing_documents"] = []
        manifest["reference_documents"] = []
        for relative, content in files.items():
            path = root / relative
            metadata = document_metadata.get(path.name)
            reference = reference_metadata.get(path.name)
            if metadata is None and reference is None:
                continue
            if metadata is not None:
                document_id, authority_class, context_mode = metadata
                entry = {
                    "document_id": document_id,
                    "canonical_filename": path.name,
                    "semver": path.name.split("_v", 1)[1][:-3],
                    "repository_path": relative,
                    "authority_class": authority_class,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                    "lifecycle": "current",
                    "context_mode": context_mode,
                }
                manifest["governing_documents"].append(entry)
            else:
                document_id, authority_class = reference
                manifest["reference_documents"].append(
                    {
                        "document_id": document_id,
                        "canonical_filename": path.name,
                        "semver": path.name.split("_v", 1)[1][:-3],
                        "repository_path": relative,
                        "authority_class": authority_class,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "superseded_version": None,
                        "lifecycle": "current",
                    }
                )

        history_path = root / "docs/00_platform/archive/01_DECISIONS_v0.9.0.md"
        manifest["historical_documents"] = [
            {
                "document_id": "DECISION_REGISTER_V0_9_0",
                "canonical_filename": history_path.name,
                "semver": "0.9.0",
                "repository_path": "docs/00_platform/archive/01_DECISIONS_v0.9.0.md",
                "authority_class": "DECISION_REGISTER_HISTORICAL",
                "sha256": hashlib.sha256(history_path.read_bytes()).hexdigest(),
                "superseded_version": None,
                "lifecycle": "historical",
            }
        ]

        # The Decision Register predecessor supplies a valid fixture for the
        # predecessor graph without adding a second active authority.
        next(entry for entry in manifest["governing_documents"] if entry["document_id"] == "DECISION_REGISTER")[
            "superseded_version"
        ] = "0.9.0"
        self._write_manifest(root, manifest)
        self._write_route_readme(root, manifest)
        return manifest

    @staticmethod
    def _write_manifest(root: Path, manifest: dict) -> None:
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    @staticmethod
    def _write_route_readme(
        root: Path,
        manifest: dict,
        *,
        overrides: dict[str, dict[str, str]] | None = None,
        omit_document_id: str | None = None,
        archive_lines: list[str] | None = None,
        mirror_overrides: dict[str, str] | None = None,
    ) -> None:
        overrides = overrides or {}
        rows = []
        for entry in manifest["governing_documents"]:
            if entry["document_id"] == omit_document_id:
                continue
            row = dict(entry)
            row.update(overrides.get(entry["document_id"], {}))
            rows.append(
                "| {document_id} | {authority_class} | {context_mode} | {canonical_filename} | {repository_path} | {semver} |".format(
                    **row
                )
            )
        table = "\n".join(
            [
                "| Document ID | Authority class | Context mode | Canonical filename | Repository path | SemVer |",
                "| --- | --- | --- | --- | --- | --- |",
                *rows,
            ]
        )
        archive = "\n".join(archive_lines or [])
        open_work = next(
            root.glob("docs/00_platform/02_OPEN_WORK_v*.md")
        ).read_text(encoding="utf-8")
        open_work_state_match = re.search(
            r"<!-- HARDEN_02_RECOVERY_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_RECOVERY_STATE_END -->",
            open_work,
            re.DOTALL,
        )
        if open_work_state_match is None:
            raise AssertionError("fixture Open Work state block is missing")
        canonical_state = json.loads(open_work_state_match.group(1))
        mirror_fields = (
            "current_stage",
            "next_stage",
            "phase_7c",
            "proof_classification",
            "application_implementation",
        )
        mirror_state = {
            field: canonical_state[field]
            for field in mirror_fields
            if field in canonical_state
        }
        mirror_state.update(mirror_overrides or {})
        mirror = json.dumps(mirror_state, indent=2)
        readme = (
            "# Fixture platform documentation\n\n"
            "## Current Authority\n\n"
            "<!-- CURRENT_AUTHORITY_TABLE_START -->\n"
            f"{table}\n"
            "<!-- CURRENT_AUTHORITY_TABLE_END -->\n\n"
            "## Active lifecycle state\n\n"
            "<!-- ACTIVE_STATE_MIRROR_START -->\n"
            "```json\n"
            f"{mirror}\n"
            "```\n"
            "<!-- ACTIVE_STATE_MIRROR_END -->\n\n"
            "## Archive\n\n"
            f"{archive}\n"
        )
        path = root / "docs/00_platform/README.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
