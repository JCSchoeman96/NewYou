from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
CURRENT = {entry["document_id"]: entry for entry in MANIFEST["governing_documents"]}


def read_current(document_id: str) -> str:
    filename = CURRENT[document_id]["canonical_filename"]
    return (DOCS / filename).read_text(encoding="utf-8")


def section(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


class DuplicateCollectionMakeWholeAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = read_current("PLATFORM_BASELINE")
        cls.decisions = read_current("DECISION_REGISTER")
        cls.roadmap = read_current("ROADMAP")
        cls.reversal = section(
            cls.product,
            "## 21R.2 Refund, dispute and reversal consequences",
            "## 21R.3 Consent withdrawal and delivered plan access",
        )

    def test_duplicate_webhook_with_one_actual_collection_does_not_create_make_whole(self):
        self.assertIn(
            "duplicate provider evidence alone is not evidence of multiple genuine financial collections",
            self.reversal.lower(),
        )
        self.assertIn("one actual collection", self.reversal.lower())
        self.assertIn("does not create a make-whole obligation", self.reversal.lower())

    def test_two_genuine_collections_for_one_obligation_create_one_exact_excess_claim_and_one_right(self):
        for required in (
            "one intended commercial obligation",
            "multiple verified genuine collections",
            "retains only the lawful amount",
            "make-whole obligation equal to the verified excess",
            "satisfies that claim exactly once",
            "at most one valid entitlement consequence",
        ):
            self.assertIn(required.lower(), self.reversal.lower())

    def test_payer_a_for_recipient_b_keeps_make_whole_at_payment_relationship(self):
        """Payer A funds one intended obligation for recipient B, collected twice."""
        decision = section(
            self.decisions,
            "## DEC-314 — Duplicate collections, make-whole and component attribution",
            "# Open Gates",
        )
        for authority in (self.reversal.lower(), decision.lower()):
            for required in (
                "one intended commercial obligation",
                "multiple verified genuine collections",
                "authoritative payer/payment relationship",
                "owes this correction to that relationship",
                "satisfies that claim exactly once, making the authoritative payer/payment relationship whole for the verified excess",
                "authoritative commercial and payment truth",
                "account holder, entitlement recipient or beneficiary",
                "does not become the monetary claimant",
                "provider evidence cannot redefine that claimant",
                "at most one valid entitlement consequence",
            ):
                self.assertIn(required, authority)
        self.assertIn(
            "does not freeze any provider-specific execution mechanism",
            decision.lower(),
        )

    def test_two_deliberate_same_amount_purchases_close_together_remain_distinct(self):
        for required in (
            "two independently intended and accepted purchases remain two distinct commercial obligations",
            "same payer, product and amount",
            "occur close together",
            "amount or timing similarity alone must not collapse them",
        ):
            self.assertIn(required.lower(), self.reversal.lower())

    def test_stale_duplicate_evidence_after_excess_satisfaction_does_not_repeat_claim(self):
        self.assertIn("replayed or stale provider evidence", self.reversal.lower())
        self.assertIn("must not create or satisfy another make-whole claim", self.reversal.lower())

    def test_partial_refund_amount_matching_assessment_or_plan_price_cannot_select_component(self):
        for required in (
            "component identity comes only from the immutable accepted order allocation",
            "partial refund or excess amount",
            "current Assessment price",
            "current Plan price",
            "another catalogue price",
            "provider fragment",
            "callback arrival order",
        ):
            self.assertIn(required.lower(), self.reversal.lower())

    def test_catalogue_price_changes_and_bundle_split_use_historical_order_allocation(self):
        for required in (
            "original accepted order allocation",
            "even after catalogue prices change",
            "bundle allocation differs from current standalone prices",
            "under §21R.1",
        ):
            self.assertIn(required.lower(), self.reversal.lower())

    def test_out_of_order_refund_and_reversal_evidence_is_reconciled_by_commerce(self):
        self.assertIn("refund or reversal evidence arrives out of order", self.reversal.lower())
        self.assertIn("arrival order does not determine the commercial outcome", self.reversal.lower())
        self.assertIn("commerce verifies and reconciles", self.reversal.lower())

    def test_unresolved_provider_ambiguity_fails_closed(self):
        for required in (
            "unknown consequential monetary outcome",
            "fails closed into reconciliation",
            "do not issue a blind repeated refund",
            "an additional entitlement consequence",
        ):
            self.assertIn(required.lower(), self.reversal.lower())

    def test_provider_state_never_becomes_commerce_or_entitlements_authority(self):
        for required in (
            "Provider state remains evidence",
            "Commerce owns monetary truth and the make-whole obligation",
            "Entitlements owns the resulting right/access truth",
            "preserve legitimate historical payment, delivery and reversal records",
        ):
            self.assertIn(required.lower(), self.reversal.lower())
        self.assertIn("DEC-300", self.decisions)
        self.assertIn("composes with and narrowly extends dec-300", self.decisions.lower())

        historical_decisions = (DOCS / "archive" / "01_DECISIONS_v1.7.0.md").read_text(encoding="utf-8")
        current_decision_300 = section(
            self.decisions,
            "## DEC-300 — Commercial reversal and entitlement effects",
            "## DEC-301 — Consent withdrawal and delivered access",
        )
        historical_decision_300 = section(
            historical_decisions,
            "## DEC-300 — Commercial reversal and entitlement effects",
            "## DEC-301 — Consent withdrawal and delivered access",
        )
        self.assertEqual(historical_decision_300, current_decision_300)

    def test_successor_does_not_change_architecture_domains_north_star_or_feature_pack_count(self):
        expected_routes = {
            "PROJECT_NORTH_STAR_AND_MVP": (
                "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
                "249f5985ff1e8971e1ac4437e4bbebd5a3db9254ab25a2238e135cb7a7ae5f4b",
            ),
            "ARCHITECTURE_SYNTHESIS": (
                "03_ARCHITECTURE_v1.1.1.md",
                "342d02a7946f99aca9e6683647fc3a2505901b3d0cc2d13c21d807442025f0b3",
            ),
            "DOMAIN_MAP": (
                "04_DOMAIN_MAP_v1.2.0.md",
                "e09e14ee0a773c5855257c48685cf3a75d413c983a98d22a56b42af57dc2c078",
            ),
        }
        for document_id, (filename, digest) in expected_routes.items():
            self.assertEqual(filename, CURRENT[document_id]["canonical_filename"])
            self.assertEqual(digest, CURRENT[document_id]["sha256"])
            self.assertEqual(
                digest,
                hashlib.sha256((DOCS / filename).read_bytes()).hexdigest(),
            )
        reference_routes = {
            entry["document_id"]: entry
            for entry in MANIFEST["reference_documents"]
            if entry.get("lifecycle", "current") != "historical"
        }
        for document_id, filename, digest in (
            (
                "ARCHITECTURE_REQUIREMENTS",
                "ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md",
                "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
            ),
            (
                "ARCHITECTURE_LAW",
                "ARCHITECTURE_LAW_WORKING_v0.36.0.md",
                "26ff1e7a7e40945e501793c2bfb2ede9c01ae03f7949383ae724e3b031fa4faa",
            ),
        ):
            entry = reference_routes[document_id]
            self.assertTrue(entry["repository_path"].endswith(filename))
            self.assertEqual(digest, entry["sha256"])
            self.assertEqual(digest, hashlib.sha256((ROOT / entry["repository_path"]).read_bytes()).hexdigest())
        self.assertEqual(17, len(re.findall(r"(?m)^## FP-\d{3}\b", self.roadmap)))
        self.assertIn("no architecture, domain ownership, shared-write authority", self.decisions.lower())


if __name__ == "__main__":
    unittest.main()
