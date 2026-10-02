from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import _h02_lifecycle_state, refresh_manifest, run_audit


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

    def test_pending_post_merge_lifecycle_state_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            open_work_entry = next(
                entry for entry in manifest["governing_documents"]
                if entry["document_id"] == "OPEN_WORK"
            )
            open_work_path = root / open_work_entry["repository_path"]
            open_work = open_work_path.read_text(encoding="utf-8")
            replacements = (
                (
                    "| POST_MERGE_INDEPENDENT_REVIEW | PASS |",
                    "| POST_MERGE_INDEPENDENT_REVIEW | PENDING |",
                ),
                (
                    "| POST_MERGE_ATTESTATION | COMPLETE |",
                    "| POST_MERGE_ATTESTATION | PENDING |",
                ),
                (
                    "| EXECUTION | COMPLETE_CERTIFIED |",
                    "| EXECUTION | IN_PROGRESS_NOT_COMPLETE_CERTIFICATION_PENDING |",
                ),
            )
            for current, stale in replacements:
                self.assertEqual(1, open_work.count(current), current)
                open_work = open_work.replace(current, stale)
            open_work_path.write_text(open_work, encoding="utf-8")

            readme_path = fixture_docs / "README.md"
            readme = readme_path.read_text(encoding="utf-8")
            for current, stale in (
                ("CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION", "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING"),
                ("NEXT STAGE: FP001_RECONCILIATION_REQUIRED", "NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED"),
                (
                    "HARDEN-02 EXECUTION: COMPLETE / CERTIFIED",
                    "HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
                ),
            ):
                self.assertEqual(1, readme.count(current), current)
                readme = readme.replace(current, stale)
            readme_path.write_text(readme, encoding="utf-8")

            refresh_manifest(root, manifest_path)
            report = run_audit(root, manifest_path)
            lifecycle_check = next(
                check for check in report["checks"]
                if check["name"] == "harden_02_lifecycle_state"
            )

            self.assertEqual("FAIL", lifecycle_check["status"])

    def test_harden_execution_state_machine_fixtures(self):
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        candidate_open_work = (source_docs / "02_OPEN_WORK_v1.2.54.md").read_text(encoding="utf-8")
        current_readme = (source_docs / "README.md").read_text(encoding="utf-8")
        contract = (source_docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.8.md").read_text(encoding="utf-8")
        expected = (True, "HARDEN-02 execution completion and downstream route are coherent")
        self.assertEqual(expected, _h02_lifecycle_state(candidate_open_work, current_readme, contract))

        incomplete = candidate_open_work.replace(
            '"harden_02_execution": "COMPLETE / CERTIFIED"',
            '"harden_02_execution": "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"',
            1,
        )
        self.assertFalse(_h02_lifecycle_state(incomplete, current_readme, contract)[0])

        old_route = candidate_open_work.replace(
            "CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
            "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
            1,
        ).replace(
            "NEXT STAGE: FP001_RECONCILIATION_REQUIRED",
            "NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED",
            1,
        )
        self.assertFalse(_h02_lifecycle_state(old_route, current_readme, contract)[0])

        premature_standards = candidate_open_work.replace(
            '"engineering_standards_authority_promotion": "COMPLETE / CERTIFIED"',
            '"engineering_standards_authority_promotion": "NEXT / AUTHORISED / NOT STARTED"',
            1,
        )
        self.assertFalse(_h02_lifecycle_state(premature_standards, current_readme, contract)[0])

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

    def test_current_authorities_reject_unarchived_historical_open_work(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            pattern = r"(?<!archive/)02_OPEN_WORK_v1\.2\.44\.md"
            self.assertIn(pattern, manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"])
            self.assertIn(
                "routing guard only",
                manifest["integrity_rules"]["graph_rules"]["stale_open_work_v1_2_44_guard_note"],
            )

            authority_ids = (
                "PROJECT_NORTH_STAR_AND_MVP",
                "PLATFORM_BASELINE",
                "DECISION_REGISTER",
                "ROADMAP",
            )
            for document_id in authority_ids:
                entry = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == document_id
                )
                path = root / entry["repository_path"]
                path.write_text(
                    path.read_text(encoding="utf-8") + "\nStale route: 02_OPEN_WORK_v1.2.44.md\n",
                    encoding="utf-8",
                )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"])
            for document_id in authority_ids:
                entry = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == document_id
                )
                self.assertIn(entry["repository_path"], graph_check["message"])

    def test_archived_open_work_reference_is_allowed_in_current_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            product_entry = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8") + "\nHistorical source: archive/02_OPEN_WORK_v1.2.44.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("PASS", graph_check["status"], graph_check["message"])

    def test_stale_reference_route_rejects_former_integrity_audit_reference_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            product_entry = next(
                item for item in json.loads(manifest_path.read_text(encoding="utf-8"))["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\nStale route: reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"], graph_check["message"])
            self.assertIn(product_entry["repository_path"], graph_check["message"])
            self.assertIn("FOUNDATION_INTEGRITY_AUDIT", graph_check["message"])

    def test_archived_integrity_audit_reference_is_allowed_in_current_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            product_entry = next(
                item for item in json.loads(manifest_path.read_text(encoding="utf-8"))["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\nHistorical evidence: archive/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("PASS", graph_check["status"], graph_check["message"])

    def test_declared_working_navigation_path_is_scanned_for_stale_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            relative = "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("See STALE_MOVED_SOURCE.md for the source.\n", encoding="utf-8")
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)STALE_MOVED_SOURCE\.md"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = []
            manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"] = [relative]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"])
            self.assertIn(relative, graph_check["message"])

    def test_readme_current_authority_order_uses_positions_from_the_readme(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            readme.write_text(
                "\n".join(
                    f"{index}. `{entry['canonical_filename']}`"
                    for index, entry in enumerate(reversed(manifest["governing_documents"]), start=1)
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json")

            order_check = next(
                check for check in report["checks"] if check["name"] == "readme_current_authority_order"
            )
            self.assertEqual("FAIL", order_check["status"])

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

    def test_current_north_star_and_product_self_versions_match_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)

            for document_id, old_version, new_version in (
                ("PROJECT_NORTH_STAR_AND_MVP", "1.2.3", "9.9.9"),
                ("PLATFORM_BASELINE", "1.5.0", "9.9.9"),
            ):
                with self.subTest(document_id=document_id):
                    entry = next(
                        item for item in manifest["governing_documents"]
                        if item["document_id"] == document_id
                    )
                    path = root / entry["repository_path"]
                    path.write_text(
                        path.read_text(encoding="utf-8").replace(
                            f"**Document version:** v{old_version}",
                            f"**Document version:** v{new_version}",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, root / "manifest.json")

                    report = run_audit(
                        root,
                        root / "manifest.json",
                        expected_counts=SMALL_COUNTS,
                    )

                    self.assertTrue(
                        any(
                            finding["check"] == "current_authority_self_version"
                            and finding["path"] == entry["repository_path"]
                            for finding in report["findings"]
                        )
                    )

                    path.write_text(
                        path.read_text(encoding="utf-8").replace(
                            f"**Document version:** v{new_version}",
                            f"**Document version:** v{old_version}",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, root / "manifest.json")

    def test_north_star_governance_self_state_matches_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            north_star = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PROJECT_NORTH_STAR_AND_MVP"
            )
            path = root / north_star["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "governance-alignment condition: MET (v1.2.3)",
                    "governance-alignment condition: MET (v1.2.2)",
                    1,
                ),
                encoding="utf-8",
            )
            refresh_manifest(root, root / "manifest.json")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_self_version"
                    and finding["path"] == north_star["repository_path"]
                    for finding in report["findings"]
                )
            )

    def test_product_current_programme_lifecycle_mirror_is_rejected(self):
        for lifecycle in (
            "NEXT / AUTHORISED / NOT STARTED",
            "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
            "COMPLETE / CERTIFIED",
        ):
            with self.subTest(lifecycle=lifecycle), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = self._write_current_authority_fixture(root)
                product = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == "PLATFORM_BASELINE"
                )
                path = root / product["repository_path"]
                with path.open("a", encoding="utf-8") as file:
                    file.write(f"HARDEN-02 execution is {lifecycle}.\n")
                refresh_manifest(root, root / "manifest.json")

                report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

                self.assertTrue(
                    any(
                        finding["check"] == "current_authority_delegated_routing"
                        and finding["path"] == product["repository_path"]
                        for finding in report["findings"]
                    )
                )

    def test_current_authority_fixture_passes_self_state_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_current_authority_fixture(root)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertEqual(
                {
                    "current_authority_self_version",
                    "current_authority_route_resolution",
                    "current_authority_delegated_routing",
                },
                {
                    check["name"]
                    for check in report["checks"]
                    if check["name"].startswith("current_authority_")
                },
            )

    def test_current_routing_field_must_resolve_to_manifest_routes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            north_star = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PROJECT_NORTH_STAR_AND_MVP"
            )
            path = root / north_star["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "CURRENT_AUTHORITY_MANIFEST",
                    "00_PLATFORM_v1.4.1.md",
                    1,
                ),
                encoding="utf-8",
            )
            refresh_manifest(root, root / "manifest.json")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_route_resolution"
                    and finding["path"] == north_star["repository_path"]
                    for finding in report["findings"]
                )
            )

    def test_unregistered_governing_root_authority_document_fails_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            shutil.copytree(source_docs, root / "docs" / "00_platform")
            manifest_path = root / "docs" / "00_platform" / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            stale_copy = root / "docs" / "00_platform" / "00_PLATFORM_v1.4.1.md"
            archive_copy = root / "docs" / "00_platform" / "archive" / "00_PLATFORM_v1.4.1.md"
            shutil.copyfile(archive_copy, stale_copy)

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "governing_root_exclusivity"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_explicit_current_routes_in_roadmap_atlas_and_harden_resolve_relationally(self):
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        mutations = (
            (
                "05_ROADMAP_v1.2.0.md",
                "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
                "PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md",
            ),
            (
                "working/DELIVERY_ATLAS_WORKING_v0.3.6.md",
                "00_PLATFORM_v1.6.0.md",
                "00_PLATFORM_v1.5.1.md",
            ),
            (
                "working/HARDEN-02_CONTRACT_WORKING_v0.4.8.md",
                "02_OPEN_WORK_v1.2.54.md",
                "02_OPEN_WORK_v1.2.50.md",
            ),
            (
                "02_OPEN_WORK_v1.2.54.md",
                "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.6.md`",
                "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.2.md`",
            ),
        )
        for relative, current_route, stale_route in mutations:
            with self.subTest(path=relative), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                fixture_docs = root / "docs" / "00_platform"
                shutil.copytree(source_docs, fixture_docs)
                manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                path = fixture_docs / relative
                text = path.read_text(encoding="utf-8")
                self.assertIn(current_route, text)
                path.write_text(text.replace(current_route, stale_route, 1), encoding="utf-8")
                governing_entry = next(
                    entry
                    for entry in manifest["governing_documents"]
                    if entry["repository_path"] == f"docs/00_platform/{relative}"
                ) if not relative.startswith("working/") else None
                if governing_entry is not None and "provenance_sha256" in governing_entry:
                    governing_entry["provenance_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
                    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] == "current_authority_route_resolution"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_current_state_delegated_routing_must_match_readme_and_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            current_open_work = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "OPEN_WORK"
            )["canonical_filename"]
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    current_open_work,
                    "02_OPEN_WORK_v1.2.48.md",
                    1,
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_delegated_routing"
                    for finding in report["findings"]
                )
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

    def _write_current_authority_fixture(self, root: Path) -> dict:
        manifest = self._write_clean_fixture(root)
        files = {
            "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": (
                "# PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md\n"
                "- **Document version:** v1.2.3\n"
                "# 23. Current Planning Position\n"
                "Current Product/Decision/Roadmap authority is routed by README and CURRENT_AUTHORITY_MANIFEST. README and current Open Work own the active programme stage and NEXT route.\n"
                "# 24. Document Stop Condition\n"
                "**Current Product Law / governance-alignment condition: MET (v1.2.3).**\n"
                "**Implementation STOP:** planning gates remain mandatory.\n"
            ),
            "docs/00_platform/00_PLATFORM_v1.5.0.md": (
                "# 00_PLATFORM_v1.5.0.md\n"
                "- **Document version:** v1.5.0\n"
                "# 24. Current Planning Stop Condition\n"
                "Current Product Law is v1.5.0. This Product Law does not execute HARDEN-02 or authorise implementation. README and current Open Work own current programme routing and lifecycle status.\n"
            ),
            "docs/00_platform/02_OPEN_WORK_v1.0.0.md": (
                "# 02_OPEN_WORK_v1.0.0.md\n"
                "- **Document version:** v1.0.0\n"
            ),
            "docs/00_platform/README.md": (
                "## Default Agent Context\n"
                "1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`\n"
                "2. `00_PLATFORM_v1.5.0.md`\n"
                "3. `01_DECISIONS_v1.2.1.md`\n"
                "4. `02_OPEN_WORK_v1.0.0.md`\n"
                "5. `05_ROADMAP_v1.0.0.md`\n"
                "\n## Active Working Artifacts\n"
            ),
        }
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        authority_classes = {
            "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": "PRODUCT_NORTH_STAR",
            "00_PLATFORM_v1.5.0.md": "PLATFORM_PRODUCT_LAW",
            "02_OPEN_WORK_v1.0.0.md": "PLANNING_TRACKER",
        }
        document_ids = {
            "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": "PROJECT_NORTH_STAR_AND_MVP",
            "00_PLATFORM_v1.5.0.md": "PLATFORM_BASELINE",
            "02_OPEN_WORK_v1.0.0.md": "OPEN_WORK",
        }
        for relative in files:
            path = root / relative
            if path.name == "README.md":
                continue
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
