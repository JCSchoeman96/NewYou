from __future__ import annotations

import json
import hashlib
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit
from foundation_test_support import current_working_path, materialize_historical_platform_readme


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
        self.assertEqual(
            "P8-05 IMPLEMENTATION AUTHORISED FOR BOUNDED PHASE 8 PROOF; "
            "WELL-48 COMPLETE; WELL-49 BLOCKED PENDING WELL-61; "
            "WELL-60 COMPLETE; WELL-50 BACKLOG / NOT STARTED",
            state["next_stage"],
        )
        self.assertEqual("CLOSED / COMPLETED", state["phase_7c_execution_tracker_state"])
        self.assertEqual("OPEN", state["programme_router_issue_111_state"])
        self.assertEqual("NEW_TRACER_BULLET", state["proof_classification"])
        self.assertEqual("NOT SELECTED", state["reuse_existing_proof"])
        self.assertEqual("TB-001", state["tracer_bullet_id"])
        self.assertEqual("STARTED", state["architectural_proof_execution"])
        self.assertEqual("INCOMPLETE / COVERAGE-INCOMPLETE", state["proof_result"])
        self.assertEqual("NOT CERTIFIED", state["proof_certification"])
        self.assertEqual("PASS / ALL 10 CONDITIONS SATISFIED", state["development_entry_hard_stop_status"])
        self.assertEqual("SATISFIED", state["development_entry_hard_stop_conditions_1_through_10"])
        self.assertEqual(
            "AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION AUTHORISED",
            state["application_implementation"],
        )
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

    def test_current_documentation_does_not_mirror_plane_tracker_state(self):
        readme = (ROOT / "docs/README.md").read_text(encoding="utf-8")
        governance = json.loads(
            (ROOT / "docs/governance/CURRENT_GOVERNANCE_ROUTER.json").read_text(encoding="utf-8")
        )
        delivery = json.loads(
            (ROOT / "docs/delivery/CURRENT_DELIVERY_ROUTER.json").read_text(encoding="utf-8")
        )

        self.assertNotIn("PHASE 7B EXECUTION/CONTROL TRACKER #120", readme)
        self.assertNotIn("OPEN_WORK", {item["document_id"] for item in governance["governing_documents"]})
        self.assertNotIn("WELL-49", json.dumps(delivery))

    def test_current_reconciliation_header_rejects_open_tracker_projection(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_fixture(directory)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            navigation = manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]
            current_route = next(
                relative
                for relative in navigation
                if Path(relative).name.startswith("FP-001_PHASE_7B_RECONCILIATION_WORKING_")
            )
            path = root / current_route
            current = path.read_text(encoding="utf-8")
            header, body = current.split("## 1. Baseline and authority set", 1)
            header = header.replace("CLOSED / COMPLETED", "OPEN", 1)
            path.write_text(header + "## 1. Baseline and authority set" + body, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] in {
                        "phase8_approved_status_successor_current",
                        "phase8_status_successor_phase7b_preservation",
                    }
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_current_derived_routes_reject_open_tracker_projection(self):
        cases = (
            (
                "DELIVERY_ATLAS_WORKING_",
                "preserves #120 as CLOSED / COMPLETED historical evidence",
                "preserves #120 as OPEN historical evidence",
            ),
            (
                "FP-001_FEATURE_PACK_SKELETON_WORKING_",
                "under completed tracker #120 (CLOSED / COMPLETED)",
                "under open tracker #120 (CLOSED / COMPLETED)",
            ),
            (
                "HARDEN-02_CONTRACT_WORKING_",
                "RECONCILIATION EXECUTION TRACKER: #120 CLOSED / COMPLETED",
                "RECONCILIATION EXECUTION TRACKER: #120 OPEN",
            ),
        )
        for filename_prefix, anchor, replacement in cases:
            with self.subTest(prefix=filename_prefix), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_fixture(directory)
                path = current_working_path(root, filename_prefix)
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
                "DELIVERY_ATLAS_WORKING_",
                "Programme router #111 remains OPEN",
                "Programme router #111 is CLOSED",
            ),
            (
                "FP-001_FEATURE_PACK_SKELETON_WORKING_",
                "Programme router #111 remains OPEN",
                "Programme router #111 is CLOSED",
            ),
        )
        for filename_prefix, anchor, replacement in cases:
            with self.subTest(prefix=filename_prefix), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_fixture(directory)
                path = current_working_path(root, filename_prefix)
                current = path.read_text(encoding="utf-8")
                self.assertIn(anchor, current)
                path.write_text(current.replace(anchor, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertEqual("FAIL", report["status"])
                self.assertTrue(report["findings"], report["findings"])

    def test_delivery_router_owns_current_paths_and_history_is_not_current(self):
        router = json.loads(
            (ROOT / "docs/delivery/CURRENT_DELIVERY_ROUTER.json").read_text(encoding="utf-8")
        )
        for route in router["delivery_contracts"]:
            self.assertTrue(route["repository_path"].startswith("docs/delivery/"), route)

    @staticmethod
    def _copy_fixture(directory: str) -> tuple[Path, Path]:
        root = Path(directory)
        fixture_docs = root / "docs" / "00_platform"
        shutil.copytree(DOCS, fixture_docs)
        fixture_execution = root / "docs" / "execution"
        fixture_execution.mkdir(parents=True, exist_ok=True)
        shutil.copy2(
            ROOT / "docs/delivery/execution/p8-05-registration-jit-spec.md",
            fixture_execution / "p8-05-registration-jit-spec.md",
        )
        materialize_historical_platform_readme(root, source_root=ROOT)
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
                    finding["check"] == "phase8_approved_status_successor_current"
                    for finding in report["findings"]
                ),
                report["findings"],
            )


if __name__ == "__main__":
    unittest.main()
