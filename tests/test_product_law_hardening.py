from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from tools import foundation_integrity_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"


def current_document(document_id: str) -> str:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entry = next(item for item in manifest["governing_documents"] if item["document_id"] == document_id)
    return (ROOT / entry["repository_path"]).read_text(encoding="utf-8")


def matrix_rows(text: str, name: str) -> list[dict[str, str]]:
    start = f"<!-- NEWYOU:PRODUCT-MATRIX:{name}:START -->"
    end = f"<!-- NEWYOU:PRODUCT-MATRIX:{name}:END -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise AssertionError(f"expected one marked {name} matrix")
    section = text.split(start, 1)[1].split(end, 1)[0]
    table = [line for line in section.splitlines() if line.strip().startswith("|")]
    if len(table) < 3:
        raise AssertionError(f"{name} matrix has no data rows")

    def cells(line: str) -> list[str]:
        return [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]

    headers = cells(table[0])
    rows: list[dict[str, str]] = []
    for line in table[2:]:
        values = cells(line)
        if len(values) != len(headers):
            raise AssertionError(f"malformed row in {name} matrix: {line}")
        rows.append(dict(zip(headers, values)))
    return rows


class ProductLawHardeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = current_document("PLATFORM_BASELINE")
        cls.decisions = current_document("DECISION_REGISTER")
        cls.open_work = current_document("OPEN_WORK")
        cls.roadmap = current_document("ROADMAP")
        cls.readme = (DOCS / "README.md").read_text(encoding="utf-8")
        cls.fp001 = (DOCS / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md").read_text(
            encoding="utf-8"
        )
        cls.integrity_rules = json.loads(MANIFEST.read_text(encoding="utf-8"))["integrity_rules"]

    def test_paid_plan_matrix_covers_each_safety_outcome_and_terminal_closeout(self):
        rows = matrix_rows(self.product, "ELIGIBILITY-PAID-PLAN")
        cases = {row["case"]: row for row in rows}
        self.assertEqual(
            {
                "eligible_automated",
                "insufficient_information",
                "professional_review_required",
                "general_wellness_only",
                "terminal_unfulfillable_outcome",
            },
            set(cases),
        )
        self.assertIn("consume_on_successful_delivery", cases["eligible_automated"]["entitlement consequence"])
        self.assertIn("technical_failure=preserve_unconsumed", cases["eligible_automated"]["entitlement consequence"])
        self.assertIn("held_unconsumed", cases["insufficient_information"]["entitlement consequence"])
        self.assertIn("no_expiry_for_incomplete_information", cases["insufficient_information"]["entitlement consequence"])
        self.assertIn("held_unconsumed_pending_review", cases["professional_review_required"]["entitlement consequence"])
        self.assertIn("not_personalised_plan_fulfilment", cases["general_wellness_only"]["commercial consequence"])
        self.assertIn("refund_allocated_plan_component", cases["terminal_unfulfillable_outcome"]["commercial consequence"])

    def test_commercial_reversal_matrix_covers_access_and_history_consequences(self):
        rows = matrix_rows(self.product, "COMMERCIAL-REVERSAL")
        cases = {row["case"]: row for row in rows}
        self.assertEqual(
            {
                "refund_before_entitlement_use",
                "plan_refund_before_generation",
                "verified_technical_failure_refund",
                "duplicate_payment_refund",
                "membership_duplicate_billing_refund",
                "unverified_provider_signal",
                "confirmed_disputed_chargeback",
                "chargeback_payment_restored",
                "final_lost_chargeback",
                "post_delivery_full_reversal",
            },
            set(cases),
        )
        self.assertIn("end_refunded_component", cases["refund_before_entitlement_use"]["entitlement/access consequence"])
        self.assertIn("preserve_one_valid_right", cases["duplicate_payment_refund"]["entitlement/access consequence"])
        self.assertIn("no_entitlement_mutation", cases["unverified_provider_signal"]["entitlement/access consequence"])
        self.assertIn("suspend_after_commerce_confirmation", cases["confirmed_disputed_chargeback"]["entitlement/access consequence"])
        self.assertIn("restore_idempotently", cases["chargeback_payment_restored"]["entitlement/access consequence"])
        self.assertIn("end_paid_access", cases["final_lost_chargeback"]["entitlement/access consequence"])
        for row in rows:
            self.assertIn("preserve_historical_record", row["historical record consequence"])

    def test_consent_matrix_separates_future_processing_from_delivered_plan_access(self):
        rows = matrix_rows(self.product, "CONSENT-WITHDRAWAL")
        cases = {row["event"]: row for row in rows}
        self.assertEqual(
            {
                "personalisation_withdrawal",
                "automated_recommendation_withdrawal",
                "practitioner_sharing_withdrawal",
                "optional_ai_withdrawal",
                "health_storage_withdrawal",
                "full_account_deletion",
            },
            set(cases),
        )
        for event in (
            "personalisation_withdrawal",
            "automated_recommendation_withdrawal",
            "practitioner_sharing_withdrawal",
            "optional_ai_withdrawal",
        ):
            self.assertIn("stop_affected_future_processing", cases[event]["future processing"])
            self.assertIn("entitlement_unchanged", cases[event]["commercial entitlement"])
        self.assertIn("conditional_on_independent_lawful_basis", cases["health_storage_withdrawal"]["delivered plan access"])
        self.assertIn("end_ordinary_access", cases["full_account_deletion"]["delivered plan access"])
        self.assertIn("separate_lifecycle", cases["full_account_deletion"]["commercial entitlement"])

    def test_provenance_matrix_forbids_exact_scores_without_digital_assessment(self):
        rows = matrix_rows(self.product, "TEMPERAMENT-PROVENANCE")
        cases = {row["provenance"]: row for row in rows}
        self.assertEqual(
            {"self_reported", "book_derived", "digitally_assessed", "later_digital_completion"},
            set(cases),
        )
        for provenance in ("self_reported", "book_derived"):
            self.assertEqual("no", cases[provenance]["exact digital scores"])
            self.assertEqual("no", cases[provenance]["paid digital report"])
            self.assertEqual("unused", cases[provenance]["included assessment credit"])
        self.assertEqual("yes", cases["digitally_assessed"]["exact digital scores"])
        self.assertEqual("yes", cases["digitally_assessed"]["paid digital report"])
        self.assertIn("preserve_prior_provenance", cases["later_digital_completion"]["result history"])

    def test_repeat_assessment_matrix_distinguishes_sale_credit_attempt_and_retake(self):
        rows = matrix_rows(self.product, "ASSESSMENT-PURCHASE-USE")
        cases = {row["case"]: row for row in rows}
        self.assertEqual(
            {
                "standalone_purchase_without_unused_credit",
                "standalone_purchase_with_unused_paid_credit",
                "purchase_when_annual_use_interval_blocks_attempt",
                "bundle_purchase_with_unused_paid_credit",
                "premium_annual_reassessment_credit",
                "plan_only_purchase_with_assessment_credit",
            },
            set(cases),
        )
        self.assertEqual("one", cases["standalone_purchase_without_unused_credit"]["maximum active unused ordinary paid credits"])
        self.assertIn("reject", cases["standalone_purchase_with_unused_paid_credit"]["purchase eligibility"])
        self.assertIn("reject", cases["purchase_when_annual_use_interval_blocks_attempt"]["purchase eligibility"])
        self.assertIn("route_to_approved_plan_only_offer", cases["bundle_purchase_with_unused_paid_credit"]["purchase eligibility"])
        self.assertIn("non_accumulating", cases["premium_annual_reassessment_credit"]["Premium credit rule"])
        self.assertIn("independent_of_assessment_credit", cases["plan_only_purchase_with_assessment_credit"]["purchase eligibility"])

    def test_resolved_oq034_and_harden02_lifecycle_are_current_in_all_routes(self):
        decision = re.search(r"^## OQ-034[^\n]*\n\*\*Status:\*\* ([^\n]+)", self.decisions, re.MULTILINE)
        self.assertIsNotNone(decision)
        self.assertIn("RESOLVED / ARCHITECTURE SELECTION", decision.group(1))
        for document_name, document in (("Roadmap", self.roadmap), ("FP-001", self.fp001)):
            for line in document.splitlines():
                if "OQ-034" in line:
                    self.assertNotIn("BLOCKS_THIS_FP", line, f"{document_name} still blocks on resolved OQ-034")
            self.assertRegex(document.lower(), r"phase 8.{0,180}proof|proof.{0,180}phase 8")
            self.assertRegex(document.lower(), r"proof[^\n]{0,100}(not complete|not finalised|not finalized|incomplete)")

        identity_pmr_gate = next(
            line for line in self.roadmap.splitlines() if "Verified account + required PMR" in line
        )
        self.assertNotIn("OQ-034", identity_pmr_gate)
        self.assertIn("OQ-035", identity_pmr_gate)
        self.assertIn("OQ-036", identity_pmr_gate)
        major_gate_lines = [
            line for line in self.roadmap.splitlines() if line.lower().startswith("**major gates")
        ]
        self.assertTrue(major_gate_lines)
        self.assertFalse(any("OQ-034" in line for line in major_gate_lines))

        state = matrix_rows(self.open_work, "HARDEN-02-LIFECYCLE")
        statuses = {row["gate"]: row["status"] for row in state}
        self.assertEqual(
            {
                "PRE_MERGE_CERTIFICATION": "COMPLETE",
                "CERTIFIED_HEAD_MERGED_UNCHANGED": "COMPLETE",
                "RESULTING_MAIN_CI": "PASS",
                "POST_MERGE_INDEPENDENT_INSPECTION": "PENDING",
                "POST_MERGE_ATTESTATION": "PENDING",
                "EXECUTION": "NOT_STARTED_NOT_AUTHORISED",
            },
            statuses,
        )
        self.assertIn("POST-MERGE CERTIFICATION: PENDING", self.readme)
        self.assertIn("NOT STARTED / NOT AUTHORISED", self.readme)
        self.assertNotIn("PENDING INDEPENDENT PRE-MERGE CERTIFICATION", self.readme)

    def test_foundation_integrity_audit_runs_the_product_semantic_checks(self):
        report = foundation_integrity_audit.run_audit(ROOT, MANIFEST)
        checks = {item["name"]: item for item in report["checks"]}
        expected = {
            "eligibility_commercial_consequences",
            "commercial_reversal_consequences",
            "consent_withdrawal_consequences",
            "temperament_provenance_outputs",
            "assessment_purchase_governance",
            "resolved_oq_not_blocking",
            "harden_02_lifecycle_state",
            "bundle_component_allocation_governance",
            "product_hardening_feature_pack_propagation",
        }
        self.assertTrue(expected <= checks.keys())
        for check in expected:
            self.assertEqual("PASS", checks[check]["status"], checks[check]["message"])

    def test_feature_pack_propagation_checker_catches_missing_pack_contract(self):
        requirements = self.integrity_rules["product_hardening_feature_pack_requirements"]
        self.assertEqual(
            {"FP-002", "FP-003", "FP-004", "FP-005", "FP-010"},
            set(requirements),
        )
        self.assertEqual(
            [], foundation_integrity_audit._feature_pack_propagation_issues(self.roadmap, requirements)
        )

        missing_provenance = self.roadmap.replace(
            "declared_temperament_has_no_exact_digital_score_or_report",
            "declared_temperament_may_have_exact_digital_score_or_report",
            1,
        )
        issues = foundation_integrity_audit._feature_pack_propagation_issues(
            missing_provenance, requirements
        )
        self.assertTrue(any("FP-003" in issue for issue in issues), issues)

        missing_authority = self.roadmap.replace(
            "`DEC-302`, `DEC-303`", "`DEC-303`", 1
        )
        issues = foundation_integrity_audit._feature_pack_propagation_issues(
            missing_authority, requirements
        )
        self.assertTrue(any("FP-003 does not cite DEC-302" in issue for issue in issues), issues)

    def test_bundle_allocation_checker_requires_snapshot_governance_and_reconciled_prices(self):
        requirements = self.integrity_rules["product_hardening_bundle_allocation_requirements"]
        self.assertEqual(
            [],
            foundation_integrity_audit._bundle_component_allocation_issues(
                self.product, self.decisions, requirements
            ),
        )

        missing_refund_basis = self.product.replace(
            "| `component_refund` | `refund_from_original_order_snapshot; never_current_price` |",
            "| `component_refund` | `refund_from_current_price` |",
            1,
        )
        issues = foundation_integrity_audit._bundle_component_allocation_issues(
            missing_refund_basis, self.decisions, requirements
        )
        self.assertTrue(any("component_refund" in issue for issue in issues), issues)

        invalid_example = self.product.replace(
            "R249_assessment + R399_plan - R99_bundle_discount = R549_accepted_bundle_amount",
            "R249_assessment + R399_plan - R99_bundle_discount = R550_accepted_bundle_amount",
            1,
        )
        issues = foundation_integrity_audit._bundle_component_allocation_issues(
            invalid_example, self.decisions, requirements
        )
        self.assertTrue(any("launch_bundle" in issue for issue in issues), issues)

        missing_decision_rule = self.decisions.replace(
            "versioned deterministic allocation rule",
            "unversioned allocation rule",
            1,
        )
        issues = foundation_integrity_audit._bundle_component_allocation_issues(
            self.product, missing_decision_rule, requirements
        )
        self.assertTrue(
            any("DEC-299 does not carry" in issue for issue in issues), issues
        )

    def test_current_governance_source_trails_resolve_to_current_or_archived_files(self):
        self.assertIn("05_ROADMAP_v1.1.1.md", self.open_work)
        self.assertIn("archive/05_ROADMAP_v1.1.0.md", self.open_work)
        self.assertIn("archive/00_PLATFORM_v1.3.0.md", self.decisions)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.2.0.md", self.fp001)
        self.assertIn("reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md", self.fp001)
        self.assertIn("docs/00_platform/archive/02_OPEN_WORK_v1.2.28.md", self.fp001)
        self.assertIn("docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md", self.fp001)

        source_trails = {
            "Open Work": self.open_work,
            "Decision Register": self.decisions,
            "FP-001": self.fp001,
        }
        moved_predecessors = (
            "00_PLATFORM_v1.3.0.md",
            "05_ROADMAP_v1.1.0.md",
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md",
            "DELIVERY_ATLAS_WORKING_v0.1.0.md",
            "02_OPEN_WORK_v1.2.28.md",
        )
        for document_name, document in source_trails.items():
            for filename in moved_predecessors:
                with self.subTest(document=document_name, filename=filename):
                    self.assertIsNone(
                        re.search(r"(?<!archive/)" + re.escape(filename), document),
                        f"{document_name} uses an unarchived predecessor path: {filename}",
                    )

        archived_source_paths = (
            "docs/00_platform/archive/05_ROADMAP_v1.1.0.md",
            "docs/00_platform/archive/00_PLATFORM_v1.3.0.md",
            "docs/00_platform/archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md",
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.28.md",
        )
        for relative_path in archived_source_paths:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

        current_source_paths = (
            "docs/00_platform/05_ROADMAP_v1.1.1.md",
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.2.0.md",
            "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md",
        )
        for relative_path in current_source_paths:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())


if __name__ == "__main__":
    unittest.main()
