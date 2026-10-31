from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
ROUTER_PATH = DOCS / "CURRENT_AUTHORITY_ROUTER_v1.0.0.json"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
ROUTER = json.loads(ROUTER_PATH.read_text(encoding="utf-8"))
MANIFEST = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def current(document_id: str) -> str:
    entries = ROUTER["governing_documents"] + ROUTER["supporting_documents"]
    entry = next(item for item in entries if item["document_id"] == document_id)
    return (ROOT / entry["repository_path"]).read_text(encoding="utf-8")


class VerificationMessageAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = current("PLATFORM_BASELINE")
        cls.decisions = current("DECISION_REGISTER")
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

    def test_current_authority_successors_and_decisions_are_routed(self) -> None:
        routes = {row["document_id"]: row for row in ROUTER["governing_documents"]}
        self.assertEqual("00_PLATFORM_v1.13.0.md", routes["PLATFORM_BASELINE"]["canonical_filename"])
        self.assertEqual("01_DECISIONS_v1.13.0.md", routes["DECISION_REGISTER"]["canonical_filename"])
        self.assertEqual("PLATFORM_OPERATING_MODEL_v1.3.0.md", routes["PLATFORM_OPERATING_MODEL"]["canonical_filename"])
        self.assertIn("DEC-320", self.decisions)
        self.assertIn("DEC-319", self.decisions)
        self.assertIn("**Status:** LOCKED", self.decisions.split("## DEC-319 —", 1)[1].split("\n## ", 1)[0])

    def test_active_p805_contract_is_current_and_separates_development_from_release(self) -> None:
        section = self.spec.split("## WELL-63 bounded verification-message content eligibility", 1)[1].split("## Registration and retry contract", 1)[0]
        route = self.spec.split("## Purpose and current boundary", 1)[1].split("## Fixed design decisions", 1)[0]
        self.assertIn("current P8-05 verification-message proof contract", section)
        self.assertNotIn("proposed for Master Gate review", section)
        self.assertIn("live authority route is", route)
        self.assertIn("verification-message proof contract", self.spec)
        self.assertIn("development_approved", section)
        self.assertIn("runtime_release_eligibility", section)

    def test_locale_version_is_delivery_authority_not_mutable_authoring_template(self) -> None:
        definition = self.product.split("## 21E.19 Verification message content classification", 1)[1].split("## 21E.20", 1)[0]
        self.assertIn("ContentItem → ContentVersion → ContentTranslationVersion", definition)
        self.assertIn("mutable authoring template or editor representation is not delivery authority", definition)
        self.assertIn("exact `ContentTranslationVersion`", definition)
        self.assertIn("immutable bytes/digest", definition)
        self.assertIn("no `latest` lookup or silent locale fallback", definition)

    def test_approval_publication_latest_and_runtime_eligibility_are_distinct(self) -> None:
        proof = self.product.split("## 21E.20", 1)[1].split("# 21F.", 1)[0]
        self.assertIn("development_approved != runtime_approved != published != latest != production_eligible", proof)
        for phrase in (
            "English Content Approver and English Language Reviewer",
            "Afrikaans Content Approver and Afrikaans Language Reviewer",
            "each role approval remains independently recorded",
            "all four exact-byte role approvals",
            "current Identity & Access grant for Content + verification_message_lifecycle",
            "explicit Content & Media release/eligibility decision",
        ):
            self.assertIn(phrase, proof.replace("`", ""))

    def test_content_and_release_authority_remain_separate(self) -> None:
        proof = self.product.split("## 21E.20", 1)[1].split("# 21F.", 1)[0]
        for phrase in (
            "production", "public release", "paid-pilot use", "real-participant delivery",
            "identity & access owns durable grant evidence", "sensitive self-approval remains prohibited",
            "content & media owns each such release/eligibility decision", "communications owns current delivery", "identity owns challenge validity",
        ):
            self.assertIn(phrase, proof.casefold())
        spec = self.spec.casefold().replace("`", "")
        for phrase in (
            "no production authority", "public release", "paid-pilot", "real-participant",
            "fail closed", "current identity & access grant for content + verification_message_lifecycle",
        ):
            self.assertIn(phrase, spec)

    def test_withdrawal_supersession_and_retry_preserve_each_domain_authority(self) -> None:
        proof = self.product.split("## 21E.20", 1)[1].split("# 21F.", 1)[0]
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
            "Before every provider submission", "current Content & Media eligibility",
            "Identity independently revalidates challenge eligibility", "A queued job grants no authority",
            "Any successor rebind must be permitted by Communications’ owner contract",
            "Ambiguous provider outcome never silently rebinds or resubmits",
            "Already-admitted provider operations follow the existing Communications admission contract",
        ):
            self.assertIn(phrase, self.spec)

    def test_platform_name_snapshot_does_not_mutate_content_version(self) -> None:
        for phrase in (
            "Preserve literal `{{platform_name}}`", "snapshotted for each new MessageIntent",
            "A platform-name configuration change does not create a content version",
            "a literal copy change around the token does", "`{{verification_link}}` remains only a literal token",
            "no bearer is created or persisted here",
        ):
            self.assertIn(phrase, self.spec)

    def test_frozen_open_work_and_manifest_are_not_live_execution_authority(self) -> None:
        legacy = next(row for row in ROUTER["legacy_snapshots"] if row["document_id"] == "OPEN_WORK_FINAL_LEGACY_SNAPSHOT")
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.90.md", legacy["repository_path"])
        self.assertFalse(legacy["live_execution_authority"])
        self.assertEqual("2a8557193fc071996e23d9214980da22d48bdbf3", ROUTER["historical_integrity_baseline"]["git_blob_sha"])
        self.assertIn("through DEC-320", self.readme)
        self.assertIn("not live execution authority", self.readme)
        self.assertEqual("02_OPEN_WORK_v1.2.90.md", next(row for row in MANIFEST["governing_documents"] if row["document_id"] == "OPEN_WORK")["canonical_filename"])

    def test_prior_frozen_authority_snapshots_remain_byte_identifiable(self) -> None:
        for entry_id, path in (
            ("PLATFORM_BASELINE_V1_11_0", "docs/00_platform/archive/00_PLATFORM_v1.11.0.md"),
            ("DECISION_REGISTER_V1_11_0", "docs/00_platform/archive/01_DECISIONS_v1.11.0.md"),
        ):
            entry = next(item for item in MANIFEST["historical_documents"] if item["document_id"] == entry_id)
            data = (ROOT / path).read_bytes()
            self.assertEqual(path, entry["repository_path"])
            self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual(entry["sha256"], entry["provenance_sha256"])


if __name__ == "__main__":
    unittest.main()
