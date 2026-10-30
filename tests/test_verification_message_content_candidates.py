from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
EVIDENCE_DIR = DOCS / "working/content_media/verification_messages"
PACKET_PATH = EVIDENCE_DIR / "VERIFICATION_MESSAGE_EVIDENCE_PACKET_v0.1.0.json"
OPEN_WORK_PATH = DOCS / "02_OPEN_WORK_v1.2.88.md"
AUTHORITY_MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

CONTENT_ITEM_ID = "NEWYOU-CONTENTITEM-VERIFICATION-MESSAGE-EMAIL-ADDRESS"
CONTENT_VERSION_ID = "NEWYOU-CONTENTVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-V1"
EN_VERSION_ID = "NEWYOU-CONTENTTRANSLATIONVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-EN-V1"
AF_VERSION_ID = "NEWYOU-CONTENTTRANSLATIONVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-AF-V1"

TOKEN_DECLARATIONS = ["{{platform_name}}", "{{verification_link}}"]

EXPECTED_ARTIFACTS = {
    "en": (
        EN_VERSION_ID,
        "NEWYOU-VERIFICATION-MESSAGE-EMAIL-ADDRESS-EN-V1.txt",
        "subject: Verify your email address\n\n"
        "A request was made to verify this email address for {{platform_name}}.\n\n"
        "Use the link below to verify your email address:\n\n"
        "{{verification_link}}\n\n"
        "Verify email address\n\n"
        "{{platform_name}}\n",
    ),
    "af": (
        AF_VERSION_ID,
        "NEWYOU-VERIFICATION-MESSAGE-EMAIL-ADDRESS-AF-V1.txt",
        "subject: Verifieer jou e-posadres\n\n"
        "Daar is ’n versoek gemaak om hierdie e-posadres vir {{platform_name}} te verifieer.\n\n"
        "Gebruik die skakel hieronder om jou e-posadres te verifieer:\n\n"
        "{{verification_link}}\n\n"
        "Verifieer e-posadres\n\n"
        "{{platform_name}}\n",
    ),
}


class VerificationMessageCandidateTests(unittest.TestCase):
    def packet(self) -> dict:
        self.assertTrue(PACKET_PATH.is_file(), f"candidate packet is missing: {PACKET_PATH}")
        return json.loads(PACKET_PATH.read_text(encoding="utf-8"))

    def test_candidate_artifact_bytes_and_identity_are_exact(self) -> None:
        packet = self.packet()
        self.assertEqual(CONTENT_ITEM_ID, packet["content_item"]["id"])
        self.assertEqual("verification_message", packet["content_item"]["type"])
        self.assertEqual(CONTENT_VERSION_ID, packet["content_version"]["id"])
        self.assertEqual(CONTENT_ITEM_ID, packet["content_version"]["content_item_id"])
        self.assertEqual("CANDIDATE_IMMUTABLE_BYTES", packet["content_version"]["state"])
        self.assertEqual(
            {
                "message_kind": "email verification message",
                "fields": ["subject", "body"],
                "body_format": "plain text",
                "locale_specific_copy_is_stored_only_in_content_translation_versions": True,
            },
            packet["content_version"]["shared_structure"],
        )
        self.assertEqual(2, len(packet["locale_versions"]))
        self.assertEqual(TOKEN_DECLARATIONS, packet["approved_literal_tokens"])

        for locale, (version_id, filename, expected_text) in EXPECTED_ARTIFACTS.items():
            with self.subTest(locale=locale):
                version = next(item for item in packet["locale_versions"] if item["locale"] == locale)
                self.assertEqual(version_id, version["id"])
                self.assertEqual(CONTENT_ITEM_ID, version["content_item_id"])
                self.assertEqual(CONTENT_VERSION_ID, version["content_version_id"])
                self.assertEqual(filename, Path(version["artifact_path"]).name)
                self.assertEqual(packet["created_date"], version["created_date"])
                self.assertEqual(EVIDENCE_DIR / filename, ROOT / version["artifact_path"])
                artifact = (ROOT / version["artifact_path"]).read_bytes()
                expected = expected_text.encode("utf-8")
                self.assertEqual(expected, artifact)
                self.assertFalse(artifact.startswith(b"\xef\xbb\xbf"), "UTF-8 BOM is forbidden")
                self.assertNotIn(b"\r", artifact, "source bytes must use LF line endings")
                self.assertTrue(artifact.endswith(b"\n"), "source bytes must end with LF")
                self.assertEqual(len(artifact), version["byte_count"])
                digest = hashlib.sha256(artifact).hexdigest()
                self.assertEqual(digest, version["sha256"])
                self.assertEqual(TOKEN_DECLARATIONS, version["literal_tokens"])
                self.assertEqual(locale, version["locale"])

    def test_only_approved_tokens_are_literal_and_artifacts_contain_no_link_secret(self) -> None:
        packet = self.packet()
        for version in packet["locale_versions"]:
            source = (ROOT / version["artifact_path"]).read_text(encoding="utf-8")
            source_tokens = re.findall(r"\{\{[^{}]+\}\}", source)
            self.assertEqual(set(TOKEN_DECLARATIONS), set(source_tokens))
            self.assertEqual(2, source_tokens.count("{{platform_name}}"))
            self.assertEqual(1, source_tokens.count("{{verification_link}}"))
            self.assertNotRegex(source, r"(?i)https?://|www\.")
            self.assertNotRegex(source, r"(?i)\bBearer\s+[A-Za-z0-9._~-]{8,}")
            self.assertNotIn("Test Platform", source)
            self.assertNotIn("Development Platform", source)

    def test_serialization_and_versioning_rules_are_explicit(self) -> None:
        packet = self.packet()
        serialization = packet["serialization"]
        self.assertEqual("UTF-8", serialization["encoding"])
        self.assertEqual("LF", serialization["line_endings"])
        self.assertFalse(serialization["bom"])
        self.assertTrue(serialization["final_newline"])
        self.assertEqual("subject: ", serialization["subject_line_prefix"])
        self.assertEqual("one blank line", serialization["subject_body_boundary"])
        self.assertEqual("one blank line", serialization["body_paragraph_boundary"])
        self.assertEqual("exact file bytes", serialization["digest_input"])
        self.assertIn("new ContentTranslationVersion ID", packet["immutability_and_versioning_policy"]["wording_change"])
        self.assertIn("never edit", packet["immutability_and_versioning_policy"]["historical_bytes"])
        self.assertEqual(
            "create a successor ContentVersion and bind new locale versions to it when the governed structure changes materially",
            packet["immutability_and_versioning_policy"]["shared_structure_change"],
        )
        self.assertEqual("exact IDs only", packet["message_intent_binding"]["resolution"])
        self.assertFalse(packet["message_intent_binding"]["latest_alias"])
        self.assertFalse(packet["message_intent_binding"]["silent_locale_fallback"])

    def test_all_four_approval_slots_are_empty_and_exact_byte_scoped(self) -> None:
        packet = self.packet()
        expected = {
            ("en", "Content Approver", EN_VERSION_ID),
            ("en", "English Language Reviewer", EN_VERSION_ID),
            ("af", "Content Approver", AF_VERSION_ID),
            ("af", "Afrikaans Language Reviewer", AF_VERSION_ID),
        }
        slots = packet["approval_slots"]
        self.assertEqual(4, len(slots))
        self.assertEqual(
            expected,
            {(item["locale"], item["required_approver_role"], item["content_translation_version_id"]) for item in slots},
        )
        for slot in slots:
            locale_version = next(item for item in packet["locale_versions"] if item["locale"] == slot["locale"])
            self.assertEqual(locale_version["sha256"], slot["exact_source_sha256"])
            self.assertEqual("PENDING_REQUIRED_APPROVAL", slot["decision"])
            self.assertIsNone(slot["approver_identity_id"])
            self.assertIsNone(slot["role_or_grant_evidence_reference"])
            self.assertIsNone(slot["decision_timestamp"])
            self.assertIsNone(slot["reason_or_comment"])
            self.assertTrue(slot["governing_authority_references"])
        self.assertEqual([], packet["approval_evidence_events"])
        self.assertEqual("APPEND_ONLY", packet["approval_evidence_recording"])
        self.assertEqual("Each role approval is a separate evidence event, even when one identity holds both roles.", packet["approval_identity_rule"])
        approval_event_fields = set(packet["approval_event_required_fields"])
        self.assertTrue(
            {
                "approval_requirement_id", "content_translation_version_id", "locale", "exact_source_sha256",
                "approver_identity_id", "required_approver_role", "role_or_grant_evidence_reference",
                "decision_timestamp", "decision", "governing_authority_references",
            }.issubset(approval_event_fields)
        )
        self.assertFalse(packet["provenance"]["wording_acceptance_is_role_approval"])
        self.assertFalse(packet["provenance"]["repository_authorship_is_role_approval"])
        self.assertFalse(packet["provenance"]["plane_ownership_is_role_approval"])

    def test_candidate_is_not_approved_published_or_proof_eligible(self) -> None:
        packet = self.packet()
        self.assertEqual("PENDING_REQUIRED_APPROVAL", packet["approval_state"])
        self.assertEqual("NOT_PUBLISHED", packet["publication_state"])
        self.assertEqual("NOT YET ELIGIBLE — REQUIRED EVIDENCE MISSING", packet["proof_eligibility"]["status"])
        self.assertFalse(packet["proof_eligibility"]["eligible_for_new_message_intents"])
        self.assertEqual([], packet["proof_eligibility"]["eligible_applicability"])
        self.assertFalse(packet["proof_eligibility"]["approval_alone_is_sufficient"])
        self.assertFalse(packet["proof_eligibility"]["repository_bytes_alone_are_sufficient"])
        self.assertFalse(packet["proof_eligibility"]["wording_acceptance_is_sufficient"])
        self.assertEqual(
            [
                "all four exact-byte role approvals",
                "current Identity & Access grant for Content + verification_message_lifecycle",
                "Content & Media eligibility decision for each exact locale version and digest",
            ],
            packet["proof_eligibility"]["required_conditions"],
        )
        self.assertEqual(
            [
                "four exact-byte role approvals",
                "current Identity & Access grant for Content + verification_message_lifecycle",
                "explicit Content & Media eligibility decision for each exact locale version",
            ],
            packet["proof_eligibility"]["missing_evidence"],
        )
        lifecycle = packet["lifecycle_evidence"]
        self.assertEqual("NOT_RECORDED", lifecycle["decision"])
        self.assertEqual("Content", lifecycle["required_role"])
        self.assertEqual("verification_message_lifecycle", lifecycle["required_scope"])
        self.assertIsNone(lifecycle["actor_identity_id"])
        self.assertIsNone(lifecycle["grant_evidence_reference"])
        self.assertIsNone(lifecycle["effective_at"])
        self.assertEqual([], packet["lifecycle_evidence_events"])
        self.assertEqual(2, len(packet["lifecycle_evidence_slots"]))
        for slot in packet["lifecycle_evidence_slots"]:
            locale_version = next(item for item in packet["locale_versions"] if item["locale"] == slot["locale"])
            self.assertEqual(locale_version["id"], slot["content_translation_version_id"])
            self.assertEqual(locale_version["sha256"], slot["exact_source_sha256"])
            self.assertEqual("Content", slot["required_role"])
            self.assertEqual("verification_message_lifecycle", slot["required_scope"])
            self.assertEqual("NOT_RECORDED", slot["decision"])
            self.assertIsNone(slot["actor_identity_id"])
            self.assertIsNone(slot["grant_evidence_reference"])
            self.assertIsNone(slot["effective_at"])
        self.assertEqual(
            ["local development", "automated tests", "development environments", "bounded P8-05 Phase-8 architectural proof"],
            packet["proof_eligibility"]["requested_applicability"],
        )
        self.assertEqual(
            ["production", "public release", "paid pilot", "real-participant delivery"],
            packet["proof_eligibility"]["prohibited_applicability"],
        )

    def test_withdrawal_and_supersession_are_unset_and_future_evidence_is_append_only(self) -> None:
        packet = self.packet()
        self.assertEqual("APPEND_ONLY", packet["lifecycle_evidence_recording"])
        for version in packet["locale_versions"]:
            self.assertEqual(
                {"supersedes": None, "superseded_by": None, "event_reference": None},
                version["supersession"],
            )
            self.assertEqual("NOT_RECORDED", version["withdrawal"]["status"])
            self.assertIsNone(version["withdrawal"]["event_reference"])
            self.assertIsNone(version["withdrawal"]["effective_at"])
            self.assertIsNone(version["withdrawal"]["actor_identity_id"])
            self.assertIsNone(version["withdrawal"]["grant_evidence_reference"])
            self.assertIsNone(version["withdrawal"]["reason"])
        event_fields = set(packet["lifecycle_event_required_fields"])
        self.assertTrue(
            {
                "event_type", "content_translation_version_id", "locale", "exact_source_sha256",
                "related_content_translation_version_id", "lifecycle_actor_identity_id",
                "grant_evidence_reference", "grant_subject_identity_id", "grant_exact_role",
                "grant_exact_scope", "grant_bounded_applicability", "grant_reason",
                "grant_governing_authority", "granting_identity_id", "grant_effective_at",
                "grant_execution_evidence_reference", "grant_expiry_or_review",
                "grant_revocation_or_supersession_reference", "reason", "effective_at",
            }.issubset(event_fields)
        )
        self.assertEqual(
            ["BOUNDED_ELIGIBILITY", "WITHDRAWAL", "SUPERSESSION"],
            packet["lifecycle_event_types"],
        )

    def test_current_open_work_routes_candidate_state_without_reopening_well63(self) -> None:
        packet = self.packet()
        open_work = OPEN_WORK_PATH.read_text(encoding="utf-8")
        latest = open_work.split("## 12.41 —", 1)[1]
        self.assertIn("WELL-63 is COMPLETE", latest)
        self.assertIn("PR #162", latest)
        self.assertIn("40916815095", latest)
        self.assertIn("passed", latest)
        self.assertIn("e4bf8ded45a4842c3804728b062c0a94e39cda63", latest)
        self.assertIn("WELL-61 is PLANNING", latest)
        self.assertIn("WELL-49 remains BLOCKED / WAITING ON WELL-60 AND WELL-61", latest)
        self.assertIn("WELL-60 remains a separate", latest)
        self.assertIn(packet["packet_path"], latest)
        for version in packet["locale_versions"]:
            self.assertIn(version["id"], latest)
            self.assertIn(version["sha256"], latest)
            self.assertIn(version["artifact_path"], latest)
        self.assertIn("§12.41", open_work.split("## 12.40 —", 1)[1].split("\n## ", 1)[0])

        authority_manifest = json.loads(AUTHORITY_MANIFEST_PATH.read_text(encoding="utf-8"))
        current_open_work = next(item for item in authority_manifest["governing_documents"] if item["document_id"] == "OPEN_WORK")
        self.assertEqual("02_OPEN_WORK_v1.2.88.md", current_open_work["canonical_filename"])
        self.assertEqual(
            hashlib.sha256(OPEN_WORK_PATH.read_bytes()).hexdigest(),
            current_open_work["sha256"],
        )
        predecessor = DOCS / "archive/02_OPEN_WORK_v1.2.87.md"
        predecessor_entry = next(
            item for item in authority_manifest["historical_documents"]
            if item["document_id"] == "OPEN_WORK_V1_2_87"
        )
        self.assertEqual(predecessor, ROOT / predecessor_entry["repository_path"])
        self.assertEqual(hashlib.sha256(predecessor.read_bytes()).hexdigest(), predecessor_entry["sha256"])
        self.assertEqual("PLANNING_TRACKER_HISTORICAL", predecessor_entry["authority_class"])
        self.assertEqual("1.2.88", predecessor_entry["superseded_version"])
        self.assertEqual("historical", predecessor_entry["lifecycle"])
        self.assertEqual("frozen_provenance", predecessor_entry["graph_policy"])
        self.assertEqual(predecessor_entry["sha256"], predecessor_entry["provenance_sha256"])
        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        self.assertIn("02_OPEN_WORK_v1.2.88.md", readme)

    def test_prejit_pack_remains_non_authoritative(self) -> None:
        pack = json.loads((DOCS / "working/content_media/PACK_MANIFEST_v0.1.0.json").read_text(encoding="utf-8"))
        self.assertEqual("NONE", pack["implementation_authority"])
        readme = (DOCS / "working/content_media/README.md").read_text(encoding="utf-8")
        self.assertIn("NON-AUTHORITATIVE", readme)
        self.assertIn("does not amend Product Law, Architecture Law, Domain Law", readme)


if __name__ == "__main__":
    unittest.main()
