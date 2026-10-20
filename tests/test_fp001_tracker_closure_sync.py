from __future__ import annotations

import json
import hashlib
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
OPEN_WORK_START = "<!-- HARDEN_02_LIFECYCLE_STATE_START -->"
CANDIDATE_PATH = DOCS / "archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
CANDIDATE_SHA256 = "274306e73e2450806516a5b76ca96f1a768af7824ba823cca6c9371c58e65401"


def _open_work_entry(manifest: dict) -> dict:
    return next(
        entry
        for entry in manifest["governing_documents"]
        if entry["document_id"] == "OPEN_WORK"
    )


def _read_lifecycle_state(open_work: str) -> dict:
    start = open_work.index(OPEN_WORK_START)
    payload_start = open_work.index("{", start)
    payload_end = open_work.index("\n```", payload_start)
    return json.loads(open_work[payload_start:payload_end])


class FP001TrackerClosureSyncTests(unittest.TestCase):
    def test_current_lifecycle_records_tracker_120_closed_and_completed(self):
        manifest = json.loads(
            (DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8")
        )
        open_work = (ROOT / _open_work_entry(manifest)["repository_path"]).read_text(encoding="utf-8")
        state = _read_lifecycle_state(open_work)

        self.assertEqual(120, state["phase_7b_reconciliation_execution_tracker_issue"])
        self.assertEqual(
            "CLOSED / COMPLETED",
            state["phase_7b_reconciliation_execution_tracker_state"],
        )
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", state["phase_7b_reconciliation"])
        self.assertEqual(
            "COMPLETE / CERTIFIED / CURRENT",
            state["phase_7c"],
        )
        self.assertEqual("TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION", state["next_stage"])
        self.assertEqual("CLOSED / COMPLETED", state["phase_7c_execution_tracker_state"])
        self.assertEqual("OPEN", state["programme_router_issue_111_state"])
        self.assertEqual("NEW_TRACER_BULLET", state["proof_classification"])
        self.assertEqual("NOT SELECTED", state["reuse_existing_proof"])
        self.assertEqual("TB-001", state["tracer_bullet_id"])
        self.assertEqual("NOT STARTED", state["architectural_proof_execution"])
        self.assertEqual("PASS / ALL 10 CONDITIONS SATISFIED", state["development_entry_hard_stop_status"])
        self.assertEqual("SATISFIED", state["development_entry_hard_stop_conditions_1_through_10"])
        self.assertEqual("AUTHORISED", state["application_implementation"])
        self.assertEqual("AUTHORISED", state["phase8"])

    def test_current_route_and_immutable_candidate_semantics_are_preserved(self):
        manifest_path = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        open_work = (ROOT / _open_work_entry(manifest)["repository_path"]).read_text(encoding="utf-8")
        state = _read_lifecycle_state(open_work)
        candidate = CANDIDATE_PATH.read_text(encoding="utf-8")
        archived_bytes = CANDIDATE_PATH.read_bytes()
        current_reconciliation = (
            DOCS / "working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(CANDIDATE_SHA256, hashlib.sha256(archived_bytes).hexdigest())
        self.assertEqual(15, len(re.findall(r"(?m)^\| S-\d{2} \|", candidate)))
        domains = re.search(r"The six affected Domains remain:\s*```text\n(.*?)\n```", candidate, re.DOTALL)
        self.assertIsNotNone(domains)
        self.assertEqual(
            ["Identity & Access", "Privacy & Consent", "Content & Media", "Communications", "Audit & Evidence", "Analytics"],
            domains.group(1).splitlines(),
        )
        self.assertIn(
            "The seven material capability relationships remain `CAP-001`, `CAP-002`, `CAP-003`, `CAP-005`, `CAP-006`, `CAP-017` and `CAP-028`.",
            candidate,
        )
        self.assertEqual(
            candidate.split("## 3. Reconciliation method and terms", 1)[1].split(
                "## 8. Candidate result and certification boundary", 1
            )[0],
            current_reconciliation.split("## 3. Reconciliation method and terms", 1)[1].split(
                "## 8. Candidate result and certification boundary", 1
            )[0],
        )
        self.assertEqual(
            {
                "privacy_consent": "NOT_REQUIRED",
                "content_media": "NOT_REQUIRED",
                "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
                "analytics": "NOT_REQUIRED",
            },
            state["conditional_dossiers"],
        )
        self.assertIn("IDENTITY & ACCESS v0.1.4", open_work)
        self.assertIn("COMMUNICATIONS v0.1.0", open_work)
        self.assertIn("COMMUNICATIONS FINALISATION: BLOCKED / STOP", open_work)
        self.assertIn("OQ-035 SECURITY / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY", open_work)
        self.assertIn("OQ-036 VENDOR / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY", open_work)
        self.assertIn("#111 remains the open programme router", open_work)
        self.assertEqual("OPEN", state["phase_7b_reconciliation_certification"]["issue_120_state_while_status_successor_pr_unmerged"])
        self.assertEqual("39097918329", state["phase_7b_reconciliation_certification"]["pr_122_status_successor"]["resulting_main_run"])
        self.assertEqual("PASS", state["phase_7b_reconciliation_certification"]["pr_122_status_successor"]["resulting_main_result"])
        self.assertEqual(406, int(state["phase_7b_reconciliation_certification"]["pr_122_status_successor"]["resulting_main_tests"].split()[0]))
        self.assertEqual(0, state["phase_7b_reconciliation_certification"]["pr_122_status_successor"]["resulting_main_foundation_integrity"]["findings"])
        candidate_path = DOCS / "archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
        self.assertTrue(candidate_path.is_file())
        self.assertIn("CANDIDATE / NOT CERTIFIED / NOT CURRENT", candidate_path.read_text(encoding="utf-8"))
        current_contract = DOCS / "working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
        self.assertIn("COMPLETE / CERTIFIED / CURRENT", current_contract.read_text(encoding="utf-8"))

    def test_historical_open_predecessor_text_remains_valid(self):
        manifest_path = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        open_work = (DOCS / "archive/02_OPEN_WORK_v1.2.68.md").read_text(encoding="utf-8")
        historical_start = open_work.index("## 12.24 —")
        historical_end = open_work.index("## 12.25 —", historical_start)
        historical = open_work[historical_start:historical_end]
        self.assertIn("OPEN while this status successor PR is unmerged", historical)
        report = run_audit(ROOT, manifest_path)
        self.assertEqual("PASS", report["status"], report["findings"])

    def test_readme_current_route_rejects_open_tracker_projection(self):
        cases = (
            (
                "Current State",
                "PHASE 7B EXECUTION/CONTROL TRACKER #120: CLOSED / COMPLETED",
                "PHASE 7B EXECUTION/CONTROL TRACKER #120: OPEN",
            ),
            (
                "Current State",
                "TRACER BULLET ID: TB-001",
                "TRACER BULLET ID: NONE / NOT CREATED",
            ),
        )
        for section_name, anchor, replacement in cases:
            with self.subTest(section=section_name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_fixture(directory)
                readme_path = root / "docs/00_platform/README.md"
                readme = readme_path.read_text(encoding="utf-8")
                section_start = readme.index(f"## {section_name}")
                next_heading = readme.find("\n## ", section_start + 1)
                section_end = next_heading if next_heading >= 0 else len(readme)
                section = readme[section_start:section_end]
                self.assertIn(anchor, section)
                readme_path.write_text(
                    readme[:section_start] + section.replace(anchor, replacement, 1) + readme[section_end:],
                    encoding="utf-8",
                )
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertEqual("FAIL", report["status"])
                self.assertTrue(
                    any(finding["check"] == "platform_readme_router_consistency" for finding in report["findings"]),
                    report["findings"],
                )

    def test_current_reconciliation_header_rejects_open_tracker_projection(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_fixture(directory)
            path = root / "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
            current = path.read_text(encoding="utf-8")
            header, body = current.split("## 1. Baseline and authority set", 1)
            header = header.replace("CLOSED / COMPLETED", "OPEN", 1)
            path.write_text(header + "## 1. Baseline and authority set" + body, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any(finding["check"] == "fp001_phase7b_certification_current" for finding in report["findings"]))

    def test_current_derived_routes_reject_open_tracker_projection(self):
        cases = (
            (
                "working/DELIVERY_ATLAS_WORKING_v0.4.19.md",
                "preserves #120 as CLOSED / COMPLETED historical evidence",
                "preserves #120 as OPEN historical evidence",
            ),
            (
                "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md",
                "under completed tracker #120 (CLOSED / COMPLETED)",
                "under open tracker #120 (CLOSED / COMPLETED)",
            ),
            (
                "working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md",
                "RECONCILIATION EXECUTION TRACKER: #120 CLOSED / COMPLETED",
                "RECONCILIATION EXECUTION TRACKER: #120 OPEN",
            ),
        )
        for relative_path, anchor, replacement in cases:
            with self.subTest(path=relative_path), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_fixture(directory)
                path = root / "docs/00_platform" / relative_path
                current = path.read_text(encoding="utf-8")
                self.assertIn(anchor, current)
                path.write_text(current.replace(anchor, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertEqual("FAIL", report["status"])
                self.assertTrue(report["findings"], report["findings"])

    def test_current_derived_routes_keep_programme_router_open(self):
        cases = (
            (
                "working/DELIVERY_ATLAS_WORKING_v0.4.19.md",
                "Programme router #111 remains OPEN",
                "Programme router #111 is CLOSED",
            ),
            (
                "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md",
                "Programme router #111 remains OPEN",
                "Programme router #111 is CLOSED",
            ),
        )
        for relative_path, anchor, replacement in cases:
            with self.subTest(path=relative_path), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_fixture(directory)
                path = root / "docs/00_platform" / relative_path
                current = path.read_text(encoding="utf-8")
                self.assertIn(anchor, current)
                path.write_text(current.replace(anchor, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertEqual("FAIL", report["status"])
                self.assertTrue(report["findings"], report["findings"])

    def test_retired_predecessor_guards_allow_only_archive_qualified_paths(self):
        retired = (
            "02_OPEN_WORK_v1.2.74.md",
            "DELIVERY_ATLAS_WORKING_v0.4.16.md",
            "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
            "HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        )
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_fixture(directory)
            readme_path = root / "docs/00_platform/README.md"
            original_readme = readme_path.read_text(encoding="utf-8")
            readme = original_readme
            current_start = readme.index("## Current State")
            next_heading = readme.find("\n## ", current_start + 1)
            current_end = next_heading if next_heading >= 0 else len(readme)
            current = readme[current_start:current_end]
            with_unqualified = current + "\n" + "\n".join(f"Historical source: `{name}`" for name in retired)
            readme_path.write_text(readme[:current_start] + with_unqualified + readme[current_end:], encoding="utf-8")
            refresh_manifest(root, manifest_path)
            rejected = run_audit(root, manifest_path)
            self.assertEqual("FAIL", rejected["status"])

            readme = original_readme
            current_start = readme.index("## Current State")
            next_heading = readme.find("\n## ", current_start + 1)
            current_end = next_heading if next_heading >= 0 else len(readme)
            current = readme[current_start:current_end]
            archived = current + "\n" + "\n".join(f"Historical source: `archive/{name}`" for name in retired)
            readme_path.write_text(readme[:current_start] + archived + readme[current_end:], encoding="utf-8")
            refresh_manifest(root, manifest_path)
            accepted = run_audit(root, manifest_path)
            self.assertEqual("PASS", accepted["status"], accepted["findings"])

    @staticmethod
    def _copy_fixture(directory: str) -> tuple[Path, Path]:
        root = Path(directory)
        fixture_docs = root / "docs" / "00_platform"
        shutil.copytree(DOCS, fixture_docs)
        manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        return root, manifest_path

    def test_foundation_integrity_rejects_unassigned_current_tracer_bullet(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(DOCS, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            open_work_path = root / _open_work_entry(manifest)["repository_path"]
            open_work = open_work_path.read_text(encoding="utf-8")
            start = open_work.index(OPEN_WORK_START)
            payload_start = open_work.index("{", start)
            payload_end = open_work.index("\n```", payload_start)
            state = json.loads(open_work[payload_start:payload_end])
            state["tracer_bullet_id"] = "NONE / NOT CREATED"
            open_work_path.write_text(
                open_work[:payload_start]
                + json.dumps(state, indent=2)
                + open_work[payload_end:],
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "fp001_phase8_proof_contract_lifecycle"
                    for finding in report["findings"]
                ),
                report["findings"],
            )


if __name__ == "__main__":
    unittest.main()
