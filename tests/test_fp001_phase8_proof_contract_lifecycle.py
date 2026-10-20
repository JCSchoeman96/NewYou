from __future__ import annotations

import unittest
import shutil
import tempfile
from pathlib import Path

from tools.foundation_integrity_audit import (
    _fp001_phase8_proof_contract_content_issues,
    refresh_manifest,
    run_audit,
)


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
LIFECYCLE_CHECK = "fp001_phase8_proof_contract_lifecycle"
CONTRACT = ROOT / "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.0.md"
OPEN_WORK = ROOT / "docs/00_platform/02_OPEN_WORK_v1.2.75.md"


class FP001Phase8ProofContractLifecycleTests(unittest.TestCase):
    def test_contract_is_a_review_candidate_and_does_not_claim_executed_proof(self):
        self.assertTrue(CONTRACT.is_file(), "the governed Phase 8 task contract is missing")
        text = CONTRACT.read_text(encoding="utf-8")
        for token in (
            "TB-001",
            "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
            "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
            "PROOF EXECUTION: NOT STARTED",
            "PROOF RESULT: NOT STARTED",
            "PROOF CERTIFICATION: NOT STARTED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "0972864ef7f4638c96198e19a13977e0151e9726",
        ):
            self.assertIn(token, text)
        self.assertNotIn("mix fp001.proof", text)
        self.assertNotIn("lib/new_you/", text)
        self.assertNotIn("test/fp001/proof/", text)

    def test_contract_preserves_the_locked_architecture_and_mandatory_proof_families(self):
        self.assertTrue(CONTRACT.is_file(), "the governed Phase 8 task contract is missing")
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertEqual([], _fp001_phase8_proof_contract_content_issues(text))
        self.assertIn(
            "Account, PMR, verification Token, required Communications MessageIntent, selected Audit EvidenceObligation and initial durable scheduling commit together or are absent together.",
            text,
        )
        self.assertIn(
            "Using security-hold release as the representative privileged effect",
            text,
        )
        self.assertIn(
            "Redis remains part of the accepted shared dev-core environment decision, but no Phase 8 application/proof component will use it absent a concrete requirement.",
            text,
        )

    def test_contract_traces_every_accepted_grill_batch_to_its_treatment(self):
        text = CONTRACT.read_text(encoding="utf-8")
        source_rows = (
            ("Q1–Q6", "e8215515-4a76-4dde-b809-ab4f17932dd9"),
            ("Q7–Q11", "e84a1ae5-8517-46c1-bb33-01d3fcc8b950"),
            ("Q12–Q16", "60fba648-e589-4e67-a6e4-4dd3818e8115"),
            ("Q17–Q21", "b24f0a08-8493-4dc3-9885-b47be44eda0d"),
            ("Q22", "cc6d56dd-344f-41ff-8b2f-64246d7f1c5b"),
            ("Q23", "446a4cc7-d1b3-4a06-a0ea-3e25d8d3149f"),
            ("Q24", "e26ca691-0980-42de-80d0-3eec3d221d67"),
            ("Q25", "b468c38e-662a-43c0-a6a5-b3abbca72499"),
            ("Q26–Q27", "4464891a-f1ad-44c2-8b80-1601e3f991b1"),
            ("Q28–Q38", "82ba53ea-b6ca-4906-a024-c6ebfb6054b3"),
            ("Q39–Q47", "ca2db611-f846-4d84-83ba-fbdfa3d8c102"),
            ("Q48–Q56", "20f6110e-582e-4498-bcac-c8cdbd54d7d8"),
            ("Q57–Q62", "7e8dc117-7ea5-4a0b-acf9-c7fc0cd2c39b"),
            ("Q63–Q70", "f75834d8-1908-4661-9b8f-be1b81fb8b0a"),
            ("Q71–Q80", "d55613cf-8026-44e3-8f90-0d7bf687231d"),
            ("Q81–Q90", "b45e180f-180a-4126-b043-3f7d555517aa"),
        )
        for question_range, comment_id in source_rows:
            self.assertIn(question_range, text)
            self.assertIn(comment_id, text)
        self.assertEqual([], _fp001_phase8_proof_contract_content_issues(text))

        weakened = text.replace("Q71–Q80", "Q71–Q79", 1)
        issues = _fp001_phase8_proof_contract_content_issues(weakened)
        self.assertTrue(
            any("Q71–Q80" in issue and "traceability" in issue for issue in issues),
            issues,
        )

    def test_content_check_rejects_a_weakened_atomicity_and_scenario_boundary(self):
        text = CONTRACT.read_text(encoding="utf-8")
        weakened = text.replace(
            "Failure to accept required E1 evidence blocks that effect.",
            "Failure to accept required E1 evidence does not block that effect.",
        ).replace(
            "| 9 | Source-authority / bypass negatives |",
            "| 9 | Optional source-authority checks |",
        ).replace(
            "without secrets, excess payload or a second business truth",
            "without secrets",
            1,
        ).replace(
            "support pressure",
            "ordinary use",
            1,
        )
        issues = _fp001_phase8_proof_contract_content_issues(weakened)
        self.assertTrue(any("approved proof-design clause" in issue and "failure to accept required e1 evidence" in issue for issue in issues))
        self.assertTrue(any("Source-authority / bypass negatives" in issue for issue in issues))
        self.assertTrue(any("Audit E2 scenario row omits approved proof detail" in issue for issue in issues))
        self.assertTrue(any("Non-enumeration / current Privacy re-read scenario row omits approved proof detail 'support pressure'" in issue for issue in issues))

    def test_open_work_routes_to_review_without_advancing_proof_or_phase9(self):
        self.assertTrue(OPEN_WORK.is_file(), "the Open Work status successor is missing")
        text = OPEN_WORK.read_text(encoding="utf-8")
        self.assertIn("working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.0.md", text)
        self.assertIn("TB-001", text)
        self.assertIn("PROOF EXECUTION: NOT STARTED", text)
        self.assertIn("PROOF CERTIFICATION: NOT STARTED", text)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", text)
        self.assertIn("TB-001 CONTRACT CANDIDATE REVIEW", text)

    def test_foundation_integrity_rejects_a_stale_readme_active_candidate_route(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            readme = root / "docs/00_platform/README.md"
            text = readme.read_text(encoding="utf-8")
            current = "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.0.md"
            stale = "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.0.9.md"
            self.assertIn(current, text)
            readme.write_text(text.replace(current, stale, 1), encoding="utf-8")
            manifest = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            refresh_manifest(root, manifest)

            report = run_audit(root, manifest)
            check = next(item for item in report["checks"] if item["name"] == LIFECYCLE_CHECK)

            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn(
                f"README active working artifacts do not route current Phase 8 source: {current}",
                check["message"],
            )

    def test_foundation_integrity_checks_the_phase8_proof_contract_transition(self):
        report = run_audit(ROOT, MANIFEST)
        check = next(
            (item for item in report["checks"] if item["name"] == LIFECYCLE_CHECK),
            None,
        )

        self.assertIsNotNone(check, "Foundation Integrity does not check the Phase 8 proof-contract route")
        self.assertEqual("PASS", check["status"], check["message"])



if __name__ == "__main__":
    unittest.main()
