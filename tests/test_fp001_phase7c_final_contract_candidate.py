from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
CONTRACT_PATH = DOCS / "archive" / "FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
RECONCILIATION_PATH = DOCS / "working" / "FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
RECONCILIATION_ARCHIVE = DOCS / "archive" / "FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
OPEN_WORK_PATH = DOCS / "archive" / "02_OPEN_WORK_v1.2.69.md"

EXPECTED_DOMAINS = [
    "Identity & Access",
    "Privacy & Consent",
    "Content & Media",
    "Communications",
    "Audit & Evidence",
    "Analytics",
]
EXPECTED_CAPABILITIES = [
    "CAP-001",
    "CAP-002",
    "CAP-003",
    "CAP-005",
    "CAP-006",
    "CAP-017",
    "CAP-028",
]
EXPECTED_DOSSIERS = {
    "Identity & Access": "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4",
    "Communications": "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
    "Audit & Evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
    "Privacy & Consent": "NOT_REQUIRED",
    "Content & Media": "NOT_REQUIRED",
    "Analytics": "NOT_REQUIRED",
}
EXPECTED_PAIRS = [
    "Identity & Access ↔ Privacy & Consent",
    "Identity & Access ↔ Content & Media",
    "Identity & Access ↔ Communications",
    "Identity & Access ↔ Audit & Evidence",
    "Identity & Access ↔ Analytics",
    "Privacy & Consent ↔ Content & Media",
    "Privacy & Consent ↔ Communications",
    "Privacy & Consent ↔ Audit & Evidence",
    "Privacy & Consent ↔ Analytics",
    "Content & Media ↔ Communications",
    "Content & Media ↔ Audit & Evidence",
    "Content & Media ↔ Analytics",
    "Communications ↔ Audit & Evidence",
    "Communications ↔ Analytics",
    "Audit & Evidence ↔ Analytics",
]
PREDECESSOR_HASHES = {
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.68.md": "19a44b00e284b834aeaef65dfec06e27f744c1e955aa908ee860097320a5ec49",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.10.md": "a978316e4233938fad0bd9d88ec9764f2a73b6c15833f83c8aa79c5f5088f493",
    "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.12.md": "b71d5b69c2009b8dcb2d8409fbc60b8892c4d0968db51e6c491a201341d7007d",
    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.12.md": "51d411b272faef50007dd8d2b0941337caa163c57dc434e9fa24c376b502706f",
}


def _section(text: str, heading: str, next_heading: str | None = None) -> str:
    start = text.index(heading)
    tail = text[start + len(heading) :]
    if next_heading is None:
        return tail
    return tail.split(next_heading, 1)[0]


def _phase7c_state() -> dict:
    text = OPEN_WORK_PATH.read_text(encoding="utf-8")
    match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("Open Work lifecycle JSON is missing")
    return json.loads(match.group(1))


class FP001Phase7CFinalContractCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if CONTRACT_PATH.is_file():
            cls.contract = CONTRACT_PATH.read_text(encoding="utf-8")
        else:
            cls.contract = ""

    def test_candidate_is_preserved_at_its_exact_archive_path(self):
        self.assertTrue(CONTRACT_PATH.is_file(), str(CONTRACT_PATH))

    def test_candidate_header_keeps_noncurrent_lifecycle_boundary(self):
        self.assertTrue(self.contract.startswith(
            "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT\n"
            "CANDIDATE\n"
            "NOT CERTIFIED\n"
            "NOT CURRENT\n\n"
            "NON-IMPLEMENTATION\n\n"
            "NOT PROOF CLASSIFICATION\n"
            "NOT PHASE 8 AUTHORITY\n"
            "NOT APPLICATION IMPLEMENTATION AUTHORITY\n"
        ))
        header = self.contract.split("## A. Identity and provenance", 1)[0]
        self.assertIn("CANDIDATE AUTHORED / READY FOR INDEPENDENT REVIEW", header)
        self.assertIn("NOT CERTIFIED / NOT CURRENT", header)

    def test_phase7c_routing_and_phase7b_prerequisite_are_current(self):
        state = _phase7c_state()
        self.assertEqual(
            "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
            state["phase_7c"],
        )
        self.assertEqual(124, state["phase_7c_execution_tracker_issue"])
        self.assertEqual("OPEN", state["phase_7c_execution_tracker_state"])
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", state["phase_7b_reconciliation"])
        candidate = state["phase_7c_contract_candidate"]
        self.assertEqual(
            "CANDIDATE / NOT CERTIFIED / NOT CURRENT", candidate["lifecycle"]
        )
        self.assertEqual(
            "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE",
            state["next_stage"],
        )

    def test_preconditions_and_dossier_dispositions_are_preserved(self):
        for requirement in (
            "PHASE 7A: COMPLETE",
            "REQUIRED DOSSIER SET: DISPOSITION-COMPLETE",
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
            "BLOCKING_AUTHORITY_GAP: NONE",
            "BLOCKING_DOSSIER_CONTRADICTION: NONE",
        ):
            self.assertIn(requirement, self.contract)
        block = _section(self.contract, "### Required dossier dispositions", "### Six affected Domains")
        for domain, disposition in EXPECTED_DOSSIERS.items():
            with self.subTest(domain=domain):
                self.assertIn(domain, block)
                self.assertIn(disposition, block)

    def test_roadmap_outcome_and_validation_objective_are_preserved(self):
        self.assertIn(
            "A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, receive that Account's required human-facing Platform Member Reference (PMR), verify email, recover access and use a controlled support/admin path without exposing unfinished product spaces.",
            self.contract,
        )
        for requirement in (
            "public-to-verified-account entry is understandable",
            "privacy/age/terms gates are respected",
            "identity/session authority is reconstructible",
            "successful individual Account creation assigns exactly one canonical active PMR",
            "operators can resolve ordinary account-access issues through bounded authority",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, self.contract)

    def test_scope_excludes_later_feature_pack_outcomes(self):
        out_of_scope = _section(self.contract, "### Explicitly out of scope", "## E. Participant journey contract")
        for outcome in (
            "purchase",
            "payment",
            "entitlement",
            "assessment",
            "health intake",
            "personalised plan generation",
            "programme delivery",
            "community",
            "live sessions",
            "events",
            "full data-rights orchestration",
            "generic operator workflow",
        ):
            with self.subTest(outcome=outcome):
                self.assertIn(outcome, out_of_scope)

    def test_exact_six_domains_and_seven_capabilities_remain(self):
        domain_block = _section(self.contract, "### Six affected Domains", "### Material capability relationships")
        domains = [line.strip() for line in domain_block.splitlines() if line.strip() and not line.startswith("```")]
        self.assertEqual(EXPECTED_DOMAINS, domains)
        capability_block = _section(self.contract, "### Material capability relationships", "## D.")
        capabilities = re.findall(r"CAP-\d{3}", capability_block)
        self.assertEqual(EXPECTED_CAPABILITIES, capabilities)

    def test_all_fifteen_reconciliation_pairings_are_traced(self):
        matrix = _section(self.contract, "## H. Cross-Domain request/effect contract", "## I. Failure, retry, idempotency and concurrency")
        rows = [line for line in matrix.splitlines() if line.startswith("| S-")]
        self.assertEqual([f"S-{i:02}" for i in range(1, 16)], [re.match(r"\| (S-\d+)", row).group(1) for row in rows])
        self.assertEqual(EXPECTED_PAIRS, [row.split("|")[2].strip() for row in rows])
        for row in rows:
            cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
            self.assertGreaterEqual(len(cells), 4)
            self.assertTrue(cells[3], row)

    def test_three_out_of_scope_pairings_remain_out_of_scope(self):
        matrix = _section(self.contract, "## H. Cross-Domain request/effect contract", "## I. Failure, retry, idempotency and concurrency")
        rows = {line.split("|")[1].strip(): line for line in matrix.splitlines() if line.startswith("| S-")}
        for seam in ("S-11", "S-14", "S-15"):
            self.assertIn("OUT_OF_SCOPE_FOR_FP001", rows[seam])
        for seam in (f"S-{i:02}" for i in range(1, 16) if i not in (11, 14, 15)):
            self.assertNotIn("OUT_OF_SCOPE_FOR_FP001", rows[seam])

    def test_certified_reconciliation_input_is_unchanged_and_complete(self):
        self.assertEqual(
            "274306e73e2450806516a5b76ca96f1a768af7824ba823cca6c9371c58e65401",
            hashlib.sha256(RECONCILIATION_ARCHIVE.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            _section(RECONCILIATION_ARCHIVE.read_text(encoding="utf-8"), "## 1. Baseline and authority set", "## 8. Candidate result and certification boundary"),
            _section(RECONCILIATION_PATH.read_text(encoding="utf-8"), "## 1. Baseline and authority set", "## 8. Candidate result and certification boundary"),
        )
        for required in (
            "15 Domain pairings examined",
            "Twelve are exercised as FP-001 contract relationships",
            "BLOCKING_AUTHORITY_GAP: NONE",
            "BLOCKING_DOSSIER_CONTRADICTION: NONE",
        ):
            self.assertIn(required, self.contract)

    def test_architectural_proof_obligations_are_frozen_without_classification(self):
        section = _section(
            self.contract,
            "## P. Architectural proof requirement",
            "## Q. Vertical Slice map",
        )
        for requirement in (
            "REUSE_EXISTING_PROOF",
            "NEW_TRACER_BULLET",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "registration-to-verification-to-login",
            "duplicate or reordered requests",
            "session authority after restart or reconnect",
            "non-enumerating abuse",
            "consent changes during protected actions",
            "provider ambiguity",
            "restricted Audit evidence",
            "FLOW-01",
            "No TB ID or proof artifact is created",
            "A failed proof stops vertical expansion",
            "Correct an architecture or Domain-law defect through its owner",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement.casefold(), section.casefold())

    def test_vertical_slice_map_covers_the_complete_outcome_and_required_layers(self):
        section = _section(
            self.contract,
            "## Q. Vertical Slice map",
            "## R. Horizontal hardening requirements",
        )
        for outcome in (
            "Outcome-level planning map",
            "not authorized VS IDs",
            "Public entry to verified individual Account",
            "Afrikaans and English",
            "18+",
            "canonical PMR",
            "email verification",
            "Sign-in and protected access",
            "session authority",
            "unfinished product spaces",
            "Account recovery and primary-email change",
            "Controlled support/admin and duplicate reconciliation",
        ):
            with self.subTest(outcome=outcome):
                self.assertIn(outcome.casefold(), section.casefold())
        for layer in (
            "interface/LiveView",
            "authorised action",
            "actor/policy",
            "domain invariants",
            "durable state",
            "async consequences",
            "PubSub",
            "Audit",
            "observability",
            "concurrency/idempotency",
            "database constraints/indexes",
            "cache invalidation",
            "automated tests",
            "acceptance criteria",
        ):
            with self.subTest(layer=layer):
                self.assertIn(layer.casefold(), section.casefold())
        self.assertNotIn("page-by-page", section.casefold())
        self.assertNotIn("resource-by-resource", section.casefold())

    def test_horizontal_hardening_obligations_are_evidence_led_and_cross_cutting(self):
        section = _section(
            self.contract,
            "## R. Horizontal hardening requirements",
            "## S. Performance envelope",
        )
        for requirement in (
            "already-correct capabilities",
            "measurements",
            "failure tests",
            "security review",
            "pilot operation",
            "release gates",
            "security/privacy",
            "concurrency/idempotency",
            "async recovery",
            "provider backlog or failure",
            "restricted Audit evidence",
            "process/node restart",
            "multi-node",
            "telemetry failure",
            "Do not create hardening work merely because a technology exists",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement.casefold(), section.casefold())

    def test_performance_envelope_carries_source_pressures_without_new_thresholds(self):
        section = _section(
            self.contract,
            "## S. Performance envelope",
            "## T. Future extension hooks",
        )
        for requirement in (
            "Argon2id",
            "p90 ≤100ms",
            "excluding password hashing and provider latency",
            "registration, login, and recovery bursts",
            "verification delivery backlog",
            "abuse and rate pressure",
            "session reconstruction after restart or reconnect",
            "PMR allocation and merge",
            "bounded collections",
            "OQ-035",
            "OQ-039",
            "No new numeric thresholds are added",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement.casefold(), section.casefold())

    def test_future_extension_hooks_preserve_seams_and_exclude_deferred_work(self):
        section = _section(
            self.contract,
            "## T. Future extension hooks",
            "## U. Acceptance and exit criteria",
        )
        for hook in (
            "owner-mediated Domain seams",
            "OQ-036",
            "social login",
            "passkeys",
            "full CAP-004 export/deletion",
            "commercial work",
            "native clients",
            "generic tenancy",
            "FP-002",
            "adds no new Domain, capability, Feature Pack, or shared-write owner",
        ):
            with self.subTest(hook=hook):
                self.assertIn(hook.casefold(), section.casefold())

    def test_oq029_retention_duration_is_fail_closed(self):
        section = _section(self.contract, "## V. Downstream gates", "## W. STOP conditions")
        self.assertIn("OQ-029", section)
        self.assertIn("exact retention duration", section)
        self.assertIn("STOP", section)
        self.assertIn("route", section.lower())

    def test_downstream_open_questions_keep_their_governed_routes(self):
        section = _section(self.contract, "## V. Downstream gates", "## W. STOP conditions")
        expectations = (
            ("OQ-030", "OQ-031", "OQ-032", "later export/deletion"),
            ("OQ-034", "resolved", "executable proof", "Phase 8"),
            ("OQ-035", "security/operations"),
            ("OQ-036", "provider", "channel", "retry"),
            ("OQ-037", "RPO/RTO"),
            ("OQ-038", "FP-006"),
            ("OQ-039", "performance/scaling"),
        )
        section_folded = section.casefold()
        for group in expectations:
            for token in group:
                with self.subTest(token=token):
                    self.assertIn(token.casefold(), section_folded)

    def test_proof_classification_and_phase8_remain_downstream(self):
        header = self.contract.split("## A. Identity and provenance", 1)[0]
        self.assertIn("PROOF CLASSIFICATION: NOT FINALISED", self.contract)
        self.assertIn("PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED", self.contract)
        self.assertIn("no choice is made between `REUSE_EXISTING_PROOF` and `NEW_TRACER_BULLET`", self.contract)
        self.assertIn("no tracer bullet id or proof artifact is created", self.contract.casefold())
        self.assertNotIn("PHASE 8: AUTHORISED", header)

    def test_pmr_invariants_are_explicit(self):
        section = _section(self.contract, "## J. Platform Member Reference contract", "## K. Communications contract")
        for requirement in (
            "successful individual Account creation",
            "exactly one canonical active PMR",
            "ordinary PMR assignment is immutable",
            "legitimate reactivation preserves",
            "permanently non-reusable",
            "collision",
            "concurrency",
            "retry",
            "purpose-scoped",
            "minimum-disclosure",
            "not authentication or authorisation authority",
            "ARQ-IAM-013",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement.casefold(), section.casefold())

    def test_communications_preserves_identity_split_and_oq036_boundary(self):
        section = _section(self.contract, "## K. Communications contract", "## L. Audit & Evidence contract")
        for token in (
            "Identity owns",
            "canonical email",
            "verification proof",
            "recovery proof",
            "source operation",
            "Communications owns",
            "MessageIntent",
            "DeliveryAttempt",
            "destination snapshot",
            "provider observations/evidence and delivery evidence",
            "never establishes email verification",
            "primary-email change",
            "OQ-036",
        ):
            with self.subTest(token=token):
                self.assertIn(token, section)

    def test_audit_e1_e2_and_correction_boundaries_are_explicit(self):
        section = _section(self.contract, "## L. Audit & Evidence contract", "## M. Privacy and minimisation contract")
        for token in (
            "business truth = source Domain owned",
            "evidence truth = Audit owned",
            "E1",
            "before a protected effect",
            "E2",
            "source acceptance boundary",
            "central materialisation delay cannot reinterpret valid source truth",
            "E3",
            "append-only",
            "cannot repair source business state",
            "not best effort",
        ):
            with self.subTest(token=token):
                self.assertIn(token, section)

    def test_privacy_content_and_analytics_boundaries_are_explicit(self):
        privacy = _section(self.contract, "## M. Privacy and minimisation contract", "## N. Content and bilingual contract")
        content = _section(self.contract, "## N. Content and bilingual contract", "## O. Analytics boundary")
        analytics = _section(self.contract, "## O. Analytics boundary", "## P. Architectural proof requirement")
        for token in ("purpose-bound", "consent", "terms/privacy acceptance", "exact retention periods", "OQ-029", "does not invent a duration", "exact retention duration"):
            self.assertIn(token.casefold(), privacy.casefold())
        for token in ("Afrikaans", "English", "approved", "locale provenance", "machine translation", "withdrawn", "superseded"):
            self.assertIn(token.casefold(), content.casefold())
        for token in ("derived", "grant access", "prove identity", "verify an email", "allocate a PMR", "establish consent", "publish content", "delivery truth", "Audit truth", "CAP-027"):
            self.assertIn(token.casefold(), analytics.casefold())

    def test_acceptance_criteria_are_observable_and_traced(self):
        section = _section(self.contract, "## U. Acceptance and exit criteria", "## V. Downstream gates")
        rows = [line for line in section.splitlines() if line.startswith("| AC-")]
        self.assertGreaterEqual(len(rows), 8)
        self.assertEqual(len(rows), len({row.split("|")[1].strip() for row in rows}))
        for row in rows:
            cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
            self.assertGreaterEqual(len(cells), 4)
            self.assertTrue(cells[2], row)
            self.assertTrue(cells[3], row)
            self.assertTrue(any(anchor in cells[3] for anchor in ("Roadmap", "Product", "Decision", "Architecture", "Domain", "Dossier", "S-")), row)

    def test_configuration_is_not_misclassified_as_missing_product_meaning(self):
        section = _section(self.contract, "## V. Downstream gates", "## W. STOP conditions")
        self.assertIn("configuration", section.lower())
        self.assertIn("exact public copy", section.casefold())
        self.assertIn("provider choice", section)
        self.assertIn("retry schedule", section)
        self.assertIn("does not create an authority blocker", section)

    def test_contract_manifest_classifies_candidate_without_promoting_authority(self):
        manifest = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
        candidate_path = "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
        entries = manifest["governing_documents"] + manifest["reference_documents"] + manifest["historical_documents"]
        self.assertNotIn(candidate_path, {entry["repository_path"] for entry in entries})
        rules = manifest["integrity_rules"]["graph_rules"]
        self.assertIn(candidate_path, rules["navigation_document_paths"])
        candidate_archive = "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
        self.assertEqual(
            candidate_archive,
            manifest["integrity_rules"]["fp001_phase7c_final_contract_candidate"]["path"],
        )
        self.assertEqual(
            candidate_path,
            manifest["integrity_rules"]["fp001_phase7c_final_contract_candidate"]["current_contract_path"],
        )
        self.assertIn(
            candidate_archive,
            {entry["repository_path"] for entry in manifest["historical_documents"]},
        )

    def test_direct_routing_predecessors_are_archived_with_pinned_bytes(self):
        for relative, expected_hash in PREDECESSOR_HASHES.items():
            path = ROOT / relative
            with self.subTest(path=relative):
                self.assertTrue(path.is_file(), relative)
                self.assertEqual(expected_hash, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_current_readme_and_open_work_route_tracker_124_as_closed(self):
        current_open_work = (DOCS / "02_OPEN_WORK_v1.2.71.md").read_text(encoding="utf-8")
        state_match = re.search(
            r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
            current_open_work,
            re.DOTALL,
        )
        self.assertIsNotNone(state_match)
        state = json.loads(state_match.group(1))
        self.assertEqual(124, state["phase_7c_execution_tracker_issue"])
        self.assertEqual("CLOSED / COMPLETED", state["phase_7c_execution_tracker_state"])
        self.assertEqual("CLOSED / COMPLETED", state["phase_7b_reconciliation_execution_tracker_state"])
        self.assertEqual(120, state["phase_7b_reconciliation_execution_tracker_issue"])
        self.assertEqual("OPEN", state["programme_router_issue_111_state"])
        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        self.assertIn("PHASE 7C: COMPLETE / CERTIFIED / CURRENT", readme)
        self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: NEXT / NOT PERFORMED", readme)
        self.assertIn("PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED", readme)
        self.assertIn("PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT", readme)


if __name__ == "__main__":
    unittest.main()
