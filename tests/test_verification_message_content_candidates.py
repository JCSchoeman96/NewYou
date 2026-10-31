from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
EVIDENCE_DIR = DOCS / "working/content_media/verification_messages"
PACKET_PATH = EVIDENCE_DIR / "VERIFICATION_MESSAGE_EVIDENCE_PACKET_v0.2.0.json"
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
        221,
        "a8ceecc466497bd3d79ae9255a7f004b18461a2d6a1791028a68bcb1efd2a072",
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
        247,
        "c3212222fdcd878af6bdc2b17895d4d6cab44e162814e2a8deee10b7fd916494",
    ),
}


class VerificationMessageCandidateTests(unittest.TestCase):
    def packet(self) -> dict:
        self.assertTrue(PACKET_PATH.is_file(), f"versioned development evidence packet is missing: {PACKET_PATH}")
        return json.loads(PACKET_PATH.read_text(encoding="utf-8"))

    def test_candidate_artifact_bytes_and_identity_are_exact(self) -> None:
        packet = self.packet()
        self.assertEqual(CONTENT_ITEM_ID, packet["content_item"]["id"])
        self.assertEqual("verification_message", packet["content_item"]["type"])
        self.assertEqual(CONTENT_VERSION_ID, packet["content_version"]["id"])
        self.assertEqual(CONTENT_ITEM_ID, packet["content_version"]["content_item_id"])
        self.assertEqual("CANDIDATE_IMMUTABLE_BYTES", packet["content_version"]["state"])
        self.assertIn("separate from the development_fixture_lifecycle decision", packet["content_version"]["state_semantics"])
        self.assertEqual(2, len(packet["locale_versions"]))
        self.assertEqual(TOKEN_DECLARATIONS, packet["approved_literal_tokens"])

        for locale, (version_id, filename, expected_text, expected_size, expected_digest) in EXPECTED_ARTIFACTS.items():
            with self.subTest(locale=locale):
                version = next(item for item in packet["locale_versions"] if item["locale"] == locale)
                self.assertEqual(version_id, version["id"])
                self.assertEqual(CONTENT_ITEM_ID, version["content_item_id"])
                self.assertEqual(CONTENT_VERSION_ID, version["content_version_id"])
                self.assertEqual(filename, Path(version["artifact_path"]).name)
                artifact = (ROOT / version["artifact_path"]).read_bytes()
                self.assertEqual(expected_text.encode("utf-8"), artifact)
                self.assertEqual(expected_size, len(artifact))
                self.assertEqual(expected_digest, hashlib.sha256(artifact).hexdigest())
                self.assertEqual(expected_size, version["byte_count"])
                self.assertEqual(expected_digest, version["sha256"])
                self.assertFalse(artifact.startswith(b"\xef\xbb\xbf"))
                self.assertNotIn(b"\r", artifact)
                self.assertTrue(artifact.endswith(b"\n"))
                self.assertEqual(TOKEN_DECLARATIONS, version["literal_tokens"])

    def test_only_approved_tokens_are_literal_and_artifacts_contain_no_link_secret(self) -> None:
        for version in self.packet()["locale_versions"]:
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
        policy = packet["immutability_and_versioning_policy"]
        self.assertIn("new ContentTranslationVersion ID", policy["wording_change"])
        self.assertIn("never edit", policy["historical_bytes"])
        self.assertEqual(
            "create a successor ContentVersion and bind new locale versions to it when the governed structure changes materially",
            policy["shared_structure_change"],
        )
        self.assertEqual("exact IDs only", packet["message_intent_binding"]["resolution"])
        self.assertFalse(packet["message_intent_binding"]["latest_alias"])
        self.assertFalse(packet["message_intent_binding"]["silent_locale_fallback"])

    def test_runtime_approval_slots_remain_empty_and_exact_byte_scoped(self) -> None:
        packet = self.packet()
        self.assertEqual("PENDING_REQUIRED_RUNTIME_APPROVAL", packet["approval_state"])
        expected = {
            ("en", "Content Approver", EN_VERSION_ID),
            ("en", "English Language Reviewer", EN_VERSION_ID),
            ("af", "Content Approver", AF_VERSION_ID),
            ("af", "Afrikaans Language Reviewer", AF_VERSION_ID),
        }
        release = packet["runtime_release_eligibility"]
        slots = release["approval_slots"]
        self.assertEqual(4, len(slots))
        self.assertEqual(expected, {(item["locale"], item["required_approver_role"], item["content_translation_version_id"]) for item in slots})
        for slot in slots:
            locale_version = next(i for i in packet["locale_versions"] if i["locale"] == slot["locale"])
            self.assertEqual(locale_version["sha256"], slot["exact_source_sha256"])
            self.assertEqual("PENDING_REQUIRED_APPROVAL", slot["decision"])
            self.assertIsNone(slot["approver_identity_id"])
            self.assertIsNone(slot["role_or_grant_evidence_reference"])
            self.assertIsNone(slot["decision_timestamp"])
            self.assertIsNone(slot["reason_or_comment"])
            self.assertTrue(slot["governing_authority_references"])
        self.assertEqual([], release["approval_evidence_events"])
        self.assertEqual([], release["lifecycle_grant_evidence"])
        self.assertEqual([], release["content_release_decisions"])
        self.assertFalse(packet["provenance"]["wording_acceptance_is_role_approval"])
        self.assertFalse(packet["provenance"]["repository_authorship_is_role_approval"])
        self.assertFalse(packet["provenance"]["plane_ownership_is_role_approval"])

    def test_development_baseline_is_approved_for_bounded_use_without_runtime_identity_or_grant(self) -> None:
        packet = self.packet()
        lifecycle = packet["development_fixture_lifecycle"]
        self.assertEqual("development_approved", lifecycle["status"])
        self.assertEqual(["candidate", "development_approved", "superseded", "withdrawn"], lifecycle["states"])
        self.assertEqual(
            ["local development", "automated tests", "development environments", "bounded P8-05 Phase-8 architectural proof"],
            lifecycle["applicability"],
        )
        self.assertFalse(lifecycle["runtime_identity_or_grant_required"])
        self.assertEqual("APPEND_ONLY", lifecycle["recording"])
        self.assertEqual("candidate", lifecycle["transition_guards"]["from"])
        self.assertIn("immutable version identity", lifecycle["transition_guards"]["development_approved"])
        self.assertIn("exact digest pinned", lifecycle["transition_guards"]["development_approved"])
        self.assertIn("owner/governance development decision", lifecycle["transition_guards"]["development_approved"])
        self.assertIn("bounded to approved non-production environments", lifecycle["transition_guards"]["development_approved"])
        self.assertIn("no production authority", lifecycle["side_effects"]["development_approved"])
        self.assertEqual(["superseded", "withdrawn"], lifecycle["terminal_for_new_consumption"])
        self.assertIn("same exact decision/version/digest is idempotent", lifecycle["idempotency"])
        self.assertIn("conflicting decisions for the same immutable version STOP and reconcile", lifecycle["conflict_policy"])
        self.assertIn("WELL-61", packet["provenance"]["wording_approval_reference"])
        self.assertIn("WELL-68", packet["provenance"]["development_decision_reference"])
        self.assertEqual([], packet["provenance"]["development_lifecycle_actor_identity_ids"])

    def test_production_release_and_real_participant_use_fail_closed(self) -> None:
        packet = self.packet()
        release = packet["runtime_release_eligibility"]
        self.assertEqual("PENDING_REQUIRED_EVIDENCE", release["status"])
        self.assertFalse(release["eligible"])
        self.assertEqual(
            ["production", "public release", "paid pilot", "real-participant delivery"],
            release["prohibited_applicability_for_development_baseline"],
        )
        self.assertEqual(
            [
                "all four exact-byte role approvals",
                "current Identity & Access grant for Content + verification_message_lifecycle",
                "explicit Content & Media release/eligibility decision for each exact locale version and digest",
            ],
            release["required_conditions"],
        )
        self.assertFalse(release["development_baseline_satisfies_runtime_release"])
        self.assertFalse(release["synthetic_grants_accepted"])
        self.assertFalse(release["development_shortcuts_accepted"])

    def test_development_fixture_lifecycle_is_append_only_with_terminal_outcomes(self) -> None:
        lifecycle = self.packet()["development_fixture_lifecycle"]
        self.assertEqual(["DEVELOPMENT_APPROVED", "SUPERSESSION", "WITHDRAWAL"], lifecycle["event_types"])
        self.assertEqual("APPEND_ONLY", lifecycle["recording"])
        self.assertEqual("successor version required; old bytes remain immutable", lifecycle["superseded_semantics"])
        self.assertEqual("no new development use; historical evidence remains", lifecycle["withdrawn_semantics"])
        self.assertEqual("new immutable version and fresh development approval", lifecycle["wording_or_byte_change"])

    def test_v010_packet_is_preserved_and_no_second_canonical_identity_is_introduced(self) -> None:
        previous = json.loads((EVIDENCE_DIR / "VERIFICATION_MESSAGE_EVIDENCE_PACKET_v0.1.0.json").read_text(encoding="utf-8"))
        self.assertEqual("verification-message-email-address-candidate-evidence-v0.1.0", previous["packet_id"])
        serialized = json.dumps(self.packet()).casefold()
        self.assertNotIn("governance_identity", serialized)
        self.assertNotIn("cross_environment_identity", serialized)
        self.assertIn("newyou.identity.account", serialized)

    def test_prejit_pack_remains_non_authoritative(self) -> None:
        pack = json.loads((DOCS / "working/content_media/PACK_MANIFEST_v0.1.0.json").read_text(encoding="utf-8"))
        self.assertEqual("NONE", pack["implementation_authority"])
        readme = (DOCS / "working/content_media/README.md").read_text(encoding="utf-8")
        self.assertIn("NON-AUTHORITATIVE", readme)
        self.assertIn("does not amend Product Law, Architecture Law, Domain Law", readme)


if __name__ == "__main__":
    unittest.main()
