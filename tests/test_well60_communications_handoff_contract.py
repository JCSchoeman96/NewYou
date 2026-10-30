from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
CANDIDATE = DOCS / "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md"
APPROVED = DOCS / "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
APPROVED_ARCHIVE = DOCS / "archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_APPROVED_CURRENT_v0.1.2.md"
REVIEWED_CANDIDATE_ARCHIVE = DOCS / "archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
JIT = ROOT / "docs/execution/p8-05-registration-jit-spec.md"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.88.md"


class WELL60CommunicationsHandoffContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.candidate = CANDIDATE.read_text(encoding="utf-8")
        cls.jit = JIT.read_text(encoding="utf-8")
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_candidate_is_exactly_pinned_and_not_promoted(self) -> None:
        rule = self.manifest["integrity_rules"]["well60_communications_handoff_candidate"]
        self.assertEqual("0.1.3", rule["candidate_version"])
        self.assertEqual(
            "PROPOSED SUCCESSOR / REVIEW PENDING / NOT CERTIFIED / NOT CURRENT",
            rule["candidate_lifecycle"],
        )
        self.assertEqual(
            hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(),
            rule["candidate_sha256"],
        )
        self.assertEqual(APPROVED.read_bytes(), APPROVED_ARCHIVE.read_bytes())
        self.assertNotEqual(APPROVED.read_bytes(), REVIEWED_CANDIDATE_ARCHIVE.read_bytes())
        phase8 = self.manifest["integrity_rules"]["fp001_phase8_proof_contract_lifecycle"]
        self.assertEqual(
            hashlib.sha256(REVIEWED_CANDIDATE_ARCHIVE.read_bytes()).hexdigest(),
            phase8["reviewed_candidate_archive_sha256"],
        )
        self.assertEqual(
            hashlib.sha256(APPROVED_ARCHIVE.read_bytes()).hexdigest(),
            rule["predecessor_sha256"],
        )
        predecessor_header = re.search(
            r"(?m)^- \*\*Design predecessor:\*\* `([^`]+)`",
            self.candidate,
        )
        predecessor_history = re.search(
            r"approved-current v0\.1\.2 status snapshot at `([^`]+)`",
            self.candidate,
        )
        self.assertIsNotNone(predecessor_header)
        self.assertIsNotNone(predecessor_history)
        stated_predecessors = (
            predecessor_header.group(1),
            predecessor_history.group(1),
        )
        manifest_predecessor = rule["predecessor_archive_path"]
        self.assertEqual(
            "docs/00_platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_APPROVED_CURRENT_v0.1.2.md",
            manifest_predecessor,
        )
        manifest_predecessor_path = ROOT / manifest_predecessor
        self.assertTrue(manifest_predecessor_path.is_file())
        for stated_path in stated_predecessors:
            resolved_path = (
                ROOT / stated_path
                if stated_path.startswith("docs/")
                else DOCS / stated_path
            )
            self.assertEqual(manifest_predecessor_path, resolved_path)
            self.assertTrue(resolved_path.is_file())
            self.assertEqual(APPROVED_ARCHIVE.read_bytes(), resolved_path.read_bytes())
            self.assertEqual(
                hashlib.sha256(resolved_path.read_bytes()).hexdigest(),
                rule["predecessor_sha256"],
            )
        phase8 = self.manifest["integrity_rules"]["fp001_phase8_proof_contract_lifecycle"]
        self.assertEqual(APPROVED.as_posix().replace(str(ROOT) + "/", ""), phase8["candidate_path"])
        self.assertEqual(
            "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
            phase8["candidate_lifecycle"],
        )
        self.assertNotIn(
            CANDIDATE.as_posix().replace(str(ROOT) + "/", ""),
            {entry["repository_path"] for entry in self.manifest["governing_documents"]},
        )
        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        self.assertIn(APPROVED.name, readme)
        self.assertNotIn(CANDIDATE.name, readme)
        self.assertIn(CANDIDATE.name, self.open_work)
        self.assertNotIn(
            CANDIDATE.as_posix().replace(str(ROOT) + "/", ""),
            self.manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"],
        )

    def test_identity_source_contract_uses_current_v020_route(self) -> None:
        current_identity_route = (
            "docs/00_platform/working/"
            "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
        )
        graph_routes = self.manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]
        identity_routes = [
            route
            for route in graph_routes
            if "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_" in route
        ]
        self.assertEqual([current_identity_route], identity_routes)
        self.assertTrue((ROOT / current_identity_route).is_file())

        _, source_heading, source_contents = self.candidate.partition(
            "Current FP-001 source contracts:"
        )
        self.assertTrue(source_heading)
        current_sources = source_contents.split("\n## ", 1)[0]
        current_identity_source = "working/" + current_identity_route.rsplit("/", 1)[1]
        self.assertIn(f"`{current_identity_source}`", current_sources)
        self.assertNotIn("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md", current_sources)

        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        active_working = readme.split("## Active Working Artifacts", 1)[1].split("\n## ", 1)[0]
        self.assertIn(f"`{current_identity_source}`", active_working)

    def test_no_lost_handoff_and_executor_boundary_are_explicit(self) -> None:
        candidate_clauses = (
            "No Communications Oban job is required at registration/resend acceptance",
            "Failure to create a later P8-10 Communications job never rolls back",
            "durably discoverable through the Communications owner interface when no job exists",
            "recovers backlog after restart",
            "idempotently schedules",
            "concurrent discoverers/executors cannot multiply",
            "Oban uniqueness is not business idempotency",
            "only `MessageIntent.id`",
            "verification bearer, protected capability, destination, rendered body, Account data, Identity payload",
            "exact Content & Media content/locale eligibility and binding",
            "protected capability authority before DeliveryAttempt admission",
            "Failure before enqueue, after enqueue, or during execution",
            "DeliveryAttempt admission commits before provider I/O",
        )
        for clause in candidate_clauses:
            with self.subTest(candidate_clause=clause):
                self.assertIn(clause.casefold(), self.candidate.casefold())
        for clause in (
            "A Communications Oban job is not required to exist or be inserted by registration.",
            "Failure to create a future P8-10 Communications job cannot roll back an otherwise valid committed registration.",
            "remains durable and discoverable even when no Communications job exists",
            "restart/backlog discovery",
            "recreation of missing, deleted, or failed executor work",
            "duplicate scheduling convergence",
            "concurrent discoverer/executor safety",
            "AshOban job uniqueness is not business idempotency",
            "only Communications business reference in Oban arguments is `MessageIntent.id`",
            "Bearer, protected capability, destination, rendered body, Account data, Identity payload, and other protected source data remain absent from arguments",
            "exact content/locale eligibility and binding",
            "protected capability authority before `DeliveryAttempt` admission",
            "failures before enqueue, after enqueue, and during execution",
            "The admission transaction commits before provider I/O",
            "If later P8-10 scheduling fails, the valid resend remains committed",
        ):
            with self.subTest(jit_clause=clause):
                self.assertIn(clause.casefold(), self.jit.casefold())

    def test_states_resource_boundary_and_audit_atomicity_are_preserved(self) -> None:
        for clause in (
            "Communications physical Resources are exactly `MessageIntent` and `DeliveryAttempt`",
            "`open`, `held`, `reconciliation_required` and `closed`",
            "`queued`, `scheduled`, `ready`, or `preflighted`",
            "no placeholder/no-op action, inert worker, generic dispatcher",
            "initial Audit E2 schedule atomicity",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause.casefold(), self.candidate.casefold())
        self.assertIn("source transition, `EvidenceObligation` and initial durable scheduling share the required acceptance boundary", self.candidate)
        self.assertIn("rollback between Communications and Audit schedules", self.jit)
        self.assertIn("Audit E2 failure continues to roll back initial registration", self.jit)
        self.assertIn("P8-05 executes no Communications worker/provider", self.candidate)

    def test_p8_05_proof_does_not_depend_on_p8_10_executor(self) -> None:
        self.assertIn("P8-05 can complete this acceptance and discoverability proof without the P8-10 executor existing", self.candidate)
        self.assertIn("P8-05 is not blocked on P8-10 executor implementation", self.jit)
        self.assertIn("P8-10/WELL-10 follows the completed P8-05 intent contract", self.jit)
        self.assertIn("Candidate contract:", self.open_work)
        self.assertIn("WELL-49 remains BLOCKED until WELL-60 and WELL-61 clear", self.open_work)


if __name__ == "__main__":
    unittest.main()
