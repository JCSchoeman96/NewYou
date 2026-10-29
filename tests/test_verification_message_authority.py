from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
MANIFEST = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def current(document_id: str) -> str:
    entry = next(item for item in MANIFEST["governing_documents"] if item["document_id"] == document_id)
    return (ROOT / entry["repository_path"]).read_text(encoding="utf-8")


class VerificationMessageAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = current("PLATFORM_BASELINE")
        cls.decisions = current("DECISION_REGISTER")
        cls.open_work = current("OPEN_WORK")
        cls.spec = (ROOT / "docs/execution/p8-05-registration-jit-spec.md").read_text(encoding="utf-8")
        cls.readme = (DOCS / "README.md").read_text(encoding="utf-8")

    def test_controlled_type_is_narrow_and_does_not_authorize_other_messages(self) -> None:
        types = self.product.split("Initial controlled content types include:", 1)[1].split("New types require", 1)[0]
        self.assertIn("verification_message", types)
        self.assertNotIn("transactional_message", types)
        definition = self.product.split("## 21E.19 Verification message content classification", 1)[1].split("## 21E.20", 1)[0]
        self.assertIn("verification of an address or comparable identity claim", definition)
        for excluded in (
            "password recovery", "magic-link authentication", "billing", "safety communication",
            "marketing", "practitioner communication", "entitlement notices", "other transactional messages",
        ):
            self.assertIn(excluded, definition)

    def test_current_successors_are_frozen_and_dec319_is_locked(self) -> None:
        product_header = self.product.split("## v1.12.0 Amendment Scope", 1)[0]
        decision_header = self.decisions.split("## v1.12.0 Amendment Scope", 1)[0]
        self.assertIn("FROZEN PRODUCT BASELINE v1.12.0", product_header)
        self.assertIn("FROZEN PRODUCT DECISION REGISTER v1.12.0", decision_header)
        self.assertNotIn("PROPOSED", product_header)
        self.assertNotIn("PENDING MASTER GATE", product_header)
        self.assertNotIn("proposed for Master Gate review and not yet accepted on canonical main", self.product)
        self.assertNotIn("PROPOSED", decision_header)
        self.assertNotIn("PENDING MASTER GATE", decision_header)
        decision = self.decisions.split("## DEC-319 —", 1)[1].split("\n## ", 1)[0]
        self.assertIn("**Status:** LOCKED", decision)
        self.assertNotIn("ON ACCEPTANCE", decision)
        self.assertIn("Ordinary delegation of this exact scope is governed by DEC-317", decision)
        self.assertIn("Identity & Access owns durable grant evidence under Product §15.1B", decision)
        self.assertIn("DEC-318 continues to govern bootstrap and privileged/sensitive approval", decision)

    def test_active_p805_contract_has_no_proposal_gate_language(self) -> None:
        section = self.spec.split("## WELL-63 bounded verification-message content eligibility", 1)[1].split("## Registration and retry contract", 1)[0]
        route = self.spec.split("## Purpose and current boundary", 1)[1].split("## Fixed design decisions", 1)[0]
        self.assertIn("current P8-05 implementation contract", section)
        self.assertNotIn("proposed", section.casefold())
        self.assertNotIn("pending", section.casefold())
        self.assertIn("current authority route is Product", route)
        self.assertNotIn("authority proposal", route.casefold())
        self.assertIn("verification-message proof contract", self.spec)
        self.assertNotIn("proposed verification-message proof contract", self.spec)

    def test_locale_version_is_delivery_authority_not_mutable_authoring_template(self) -> None:
        definition = self.product.split("## 21E.19 Verification message content classification", 1)[1].split("## 21E.20", 1)[0]
        self.assertIn("ContentItem → ContentVersion → ContentTranslationVersion", definition)
        self.assertIn("mutable authoring template or editor representation is not delivery authority", definition)
        self.assertIn("exact `ContentTranslationVersion`", definition)
        self.assertIn("immutable bytes/digest", definition)
        self.assertIn("no `latest` lookup or silent locale fallback", definition)
        self.assertIn("`approved != published != latest`", self.product)

    def test_proof_eligibility_is_non_public_non_production_and_scope_bound(self) -> None:
        proof = self.product.split("## 21E.20 Bounded P8-05 verification-message eligibility", 1)[1].split("# 21F.", 1)[0]
        for permitted in ("local development", "automated tests", "development environments", "bounded P8-05 Phase-8 architectural proof"):
            self.assertIn(permitted, proof)
        for prohibited in ("production", "public release", "paid-pilot use", "real-participant delivery"):
            self.assertIn(prohibited, proof)
        self.assertIn("not public publication", proof)
        self.assertIn("repository-held file or queued job cannot create or preserve eligibility", proof)

    def test_content_lifecycle_scope_and_dec317_delegation_are_explicit(self) -> None:
        proof = self.product.split("## 21E.20 Bounded P8-05 verification-message eligibility", 1)[1].split("# 21F.", 1)[0]
        self.assertIn("governed `Content` role with scope `verification_message_lifecycle`", proof)
        self.assertIn("ordinary / non-sensitive", proof)
        self.assertIn("does not replace the content risk classification", proof)
        self.assertIn("Platform Administrator may grant or revoke", proof)
        self.assertIn("delegation catalogue under DEC-317", proof)
        self.assertIn("Identity & Access owns and durably evidences the grant", proof)
        self.assertIn("No named person defines the capability", proof)
        self.assertIn("Self-assignment is prohibited", proof)
        self.assertIn("Expiry, overdue review, revocation or supersession ends authority for future lifecycle actions", proof)
        self.assertIn("does not rewrite prior owner evidence or silently withdraw eligibility", proof)
        self.assertIn("Sensitive self-approval remains prohibited under DEC-318", self.product)
        self.assertIn("Super Admin", self.product.split("## 15.1A Role-based capability and delegation authority", 1)[1].split("## 15.1B", 1)[0])
        self.assertIn("Super Admin is not a universal bypass and conveys no Domain business authority", self.product)

    def test_grant_evidence_and_locale_approvals_are_separate(self) -> None:
        proof = self.product.split("## 21E.20 Bounded P8-05 verification-message eligibility", 1)[1].split("# 21F.", 1)[0]
        for item in (
            "the subject", "exact role and scope", "bounded applicability", "reason",
            "governing authority", "effective time", "execution evidence", "expiry or review",
            "revocation/supersession",
        ):
            self.assertIn(item, proof)
        for item in (
            "subject identity", "exact role and scope", "environment/applicability", "reason",
            "governing Product/Decision authority version", "effective time", "granting identity",
            "expiry/review", "revocation or supersession",
        ):
            self.assertIn(item, self.spec)
        self.assertIn("English: `Content Approver` and `English Language Reviewer`", proof)
        self.assertIn("Afrikaans: `Content Approver` and `Afrikaans Language Reviewer`", proof)
        self.assertIn("each role approval remains independently recorded", proof)
        self.assertIn("Wording acceptance, lifecycle authority and Identity & Access grant evidence satisfy none", proof)
        self.assertIn("Content Approver, language reviewer, responsible-editor status", proof)
        self.assertIn("does not grant it", proof)

    def test_withdrawal_supersession_and_retry_preserve_each_domain_authority(self) -> None:
        proof = self.product.split("## 21E.20 Bounded P8-05 verification-message eligibility", 1)[1].split("# 21F.", 1)[0]
        for phrase in (
            "A material wording change requires a new immutable locale version",
            "New MessageIntents may bind only an eligible exact locale version",
            "Existing MessageIntent binding remains historical provenance",
            "Withdrawal ends eligibility for new intents",
            "cannot be overridden by an existing job",
            "Communications owns current delivery, retry and any safe rebinding decision",
            "Identity owns challenge validity",
        ):
            self.assertIn(phrase, proof)
        for phrase in (
            "successor existence alone does not bar a retry while the original remains eligible",
            "Withdrawal before intent creation bars new binding",
            "withdrawal before a provider submission or retry requires Communications to hold",
            "Before every provider submission",
            "current Content & Media eligibility",
            "Identity independently revalidates challenge eligibility",
            "A queued job grants no authority",
            "Any successor rebind must be permitted by Communications’ owner contract",
            "Ambiguous provider outcome never silently rebinds or resubmits",
            "Already-admitted provider operations follow the existing Communications admission contract",
        ):
            self.assertIn(phrase, self.spec)

    def test_platform_name_snapshot_does_not_mutate_content_version(self) -> None:
        for phrase in (
            "Preserve literal `{{platform_name}}`",
            "snapshotted for each new MessageIntent",
            "A platform-name configuration change does not create a content version",
            "a literal copy change around the token does",
            "`{{verification_link}}` remains only a literal token",
            "no bearer is created or persisted here",
        ):
            self.assertIn(phrase, self.spec)

    def test_current_route_and_well64_closure_do_not_regress(self) -> None:
        self.assertEqual("00_PLATFORM_v1.12.0.md", next(x for x in MANIFEST["governing_documents"] if x["document_id"] == "PLATFORM_BASELINE")["canonical_filename"])
        self.assertEqual("01_DECISIONS_v1.12.0.md", next(x for x in MANIFEST["governing_documents"] if x["document_id"] == "DECISION_REGISTER")["canonical_filename"])
        self.assertEqual("02_OPEN_WORK_v1.2.87.md", next(x for x in MANIFEST["governing_documents"] if x["document_id"] == "OPEN_WORK")["canonical_filename"])
        self.assertIn("WELL-64 is COMPLETE", self.open_work)
        self.assertNotIn("pending independent Master Gate review", self.open_work)
        self.assertIn("resulting-main Foundation Integrity push run `40892033221` passed", self.open_work)
        current_status = self.open_work.split("## 12.41 — WELL-63 completion and WELL-61 verification-message candidate evidence", 1)[1]
        self.assertIn("WELL-63 is COMPLETE", current_status)
        self.assertIn("WELL-61 is PLANNING and unblocked by WELL-63", current_status)
        self.assertIn("WELL-49 remains BLOCKED / WAITING ON WELL-60 AND WELL-61", current_status)
        self.assertIn("WELL-49 remains blocked by WELL-60 and WELL-61", self.open_work)
        self.assertIn("WELL-60 remains separate", self.open_work)
        self.assertIn("DEC-299 through DEC-319", self.readme)

    def test_prior_current_authority_snapshots_remain_byte_identifiable(self) -> None:
        for entry_id, path in (
            ("PLATFORM_BASELINE_V1_11_0", "docs/00_platform/archive/00_PLATFORM_v1.11.0.md"),
            ("DECISION_REGISTER_V1_11_0", "docs/00_platform/archive/01_DECISIONS_v1.11.0.md"),
            ("OPEN_WORK_V1_2_85", "docs/00_platform/archive/02_OPEN_WORK_v1.2.85.md"),
        ):
            entry = next(item for item in MANIFEST["historical_documents"] if item["document_id"] == entry_id)
            data = (ROOT / path).read_bytes()
            self.assertEqual(path, entry["repository_path"])
            self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual(entry["sha256"], entry["provenance_sha256"])


if __name__ == "__main__":
    unittest.main()
