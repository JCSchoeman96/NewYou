from __future__ import annotations

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
BASE_MAIN = "69bef7bb2782cbff00a48505504ebd2686eb53d9"
CLASSIFICATION_BASE_MAIN = "24a9ad925ee1ab6d75ddb44bae6df0b4f3d09bca"
ROUTING_BASE_SHA = CLASSIFICATION_BASE_MAIN
CANDIDATE_HEAD = "bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5"
CANDIDATE_TREE = "8e5fc724b4c4f4a6a196d41e3beafc8e1384c2bf"
CANDIDATE_ARCHIVE_SHA256 = "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19"
CANDIDATE_ARCHIVE = DOCS / "archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
CURRENT_CONTRACT = DOCS / "working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.74.md"
PROMOTION_START = "<!-- FP001_PHASE7C_CURRENT_STATUS_START -->"
PROMOTION_END = "<!-- FP001_PHASE7C_CURRENT_STATUS_END -->"

PREDECESSORS = (
    (
        "docs/00_platform/02_OPEN_WORK_v1.2.72.md",
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.72.md",
    ),
    (
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.14.md",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.14.md",
    ),
    (
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md",
    ),
    (
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.16.md",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.16.md",
    ),
)

PROTECTED_PATHS = (
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
    "docs/00_platform/00_PLATFORM_v1.8.0.md",
    "docs/00_platform/01_DECISIONS_v1.8.0.md",
    "docs/00_platform/03_ARCHITECTURE_v1.1.1.md",
    "docs/00_platform/04_DOMAIN_MAP_v1.2.0.md",
        "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md",
    "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
    "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
)


def _git_show(commit: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def _json_marker(text: str, start: str, end: str) -> dict:
    pattern = re.escape(start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(end)
    match = re.search(pattern, text, re.DOTALL)
    if match is None:
        return {}
    return json.loads(match.group(1))


def _contract_semantic_body(text: str, final_heading: str) -> str:
    start = text.index("## B. Outcome and validation objective")
    end = text.index(final_heading, start)
    body = text[start:end]
    lifecycle_sentences = (
        "Phase 7C exit for this candidate means only that the contract is authored and ready for fresh independent exact-head review. Certification, current-status promotion, proof classification, and Phase 8 entry are separate later gates.",
        "Phase 7C contract delivery is COMPLETE / CERTIFIED / CURRENT under this separate status successor. The separate downstream classification status is COMPLETE / FINALISED as NEW_TRACER_BULLET; proof execution, Phase 8 entry and application implementation remain gated.",
    )
    for sentence in lifecycle_sentences:
        body = body.replace(sentence, "<PHASE_7C_EXIT_LIFECYCLE_STATUS>")
    return body


class FP001Phase7CCurrentPromotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = CURRENT_CONTRACT.read_text(encoding="utf-8") if CURRENT_CONTRACT.is_file() else ""
        cls.candidate = CANDIDATE_ARCHIVE.read_bytes() if CANDIDATE_ARCHIVE.is_file() else b""
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8") if OPEN_WORK.is_file() else ""
        cls.readme = (DOCS / "README.md").read_text(encoding="utf-8")
        cls.manifest = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
        cls.promotion = _json_marker(cls.contract, PROMOTION_START, PROMOTION_END)
        cls.open_work_state = _json_marker(
            cls.open_work,
            "<!-- HARDEN_02_LIFECYCLE_STATE_START -->",
            "<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        )

    def test_pr125_candidate_archive_is_exact_and_sha256_pinned(self):
        self.assertTrue(CANDIDATE_ARCHIVE.is_file())
        self.assertEqual(CANDIDATE_ARCHIVE_SHA256, hashlib.sha256(self.candidate).hexdigest())
        self.assertEqual(
            _git_show(CANDIDATE_HEAD, "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"),
            self.candidate,
        )

    def test_working_contract_is_the_complete_current_status_successor(self):
        self.assertTrue(self.contract.startswith(
            "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT\n"
            "COMPLETE\nCERTIFIED\nCURRENT\n\n"
            "NON-IMPLEMENTATION\n\nNOT PROOF CLASSIFICATION\n"
            "NOT PHASE 8 AUTHORITY\nNOT APPLICATION IMPLEMENTATION AUTHORITY\n"
        ))
        self.assertIn("FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT", self.contract)
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", self.promotion.get("phase_7c"))
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", self.promotion.get("contract_lifecycle"))

    def test_promotion_record_binds_exact_head_merge_tree_runs_and_review(self):
        expected = {
            "artifact_version": "v0.1.0",
            "promotion_state": "CURRENT / VERIFIED AFTER PR #126 RESULTING-MAIN PASS",
            "candidate_pr": 125,
            "approved_candidate_head_sha": CANDIDATE_HEAD,
            "pr125_reviewed_head_sha": CANDIDATE_HEAD,
            "candidate_tree_sha": CANDIDATE_TREE,
            "pr125_merge_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
            "pr125_merge_second_parent_sha": CANDIDATE_HEAD,
            "pr125_merge_tree_sha": CANDIDATE_TREE,
            "pr125_resulting_main_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
            "pr125_resulting_main_tree_sha": CANDIDATE_TREE,
            "pr125_candidate_resulting_main_tree_identity": "PASS",
            "independent_exact_head_review": "PASS",
            "pr125_exact_head_fia_run": 39121794222,
            "pr125_exact_head_fia_status": "completed",
            "pr125_exact_head_fia_conclusion": "success",
            "pr125_exact_head_fia_tests": 443,
            "pr125_exact_head_fia_assertions": 698,
            "pr125_exact_head_fia_findings": 0,
            "pr125_resulting_main_fia_run": 39126317950,
            "pr125_resulting_main_fia_status": "completed",
            "pr125_resulting_main_fia_conclusion": "success",
            "pr125_resulting_main_fia_tests": 443,
            "pr125_resulting_main_fia_assertions": 698,
            "pr125_resulting_main_fia_findings": 0,
            "pr126_base_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
            "pr126_reviewed_head_sha": "e7d5d3908bedf1a75c6627448c3ed0c067b076f8",
            "pr126_merge_sha": BASE_MAIN,
            "pr126_reviewed_head_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
            "pr126_merge_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
            "pr126_merge_head_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
            "pr126_head_merge_tree_identity": "PASS",
            "pr126_exact_head_fia_run": 39141076412,
            "pr126_exact_head_fia_status": "completed",
            "pr126_exact_head_fia_conclusion": "success",
            "resulting_main_sha": BASE_MAIN,
            "resulting_main_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
            "resulting_main_fia_run": 39143147487,
            "resulting_main_fia_status": "completed",
            "resulting_main_fia_conclusion": "success",
            "resulting_main_fia_tests": 455,
            "resulting_main_fia_assertions": 728,
            "resulting_main_fia_findings": 0,
            "fresh_resulting_main_verification": "PASS",
            "candidate_archive_path": "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
            "candidate_archive_sha256": CANDIDATE_ARCHIVE_SHA256,
            "phase_7c_execution_tracker_issue": 124,
            "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
            "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
            "phase_7b_tracker_issue": 120,
            "phase_7b_tracker_state": "CLOSED / COMPLETED",
            "programme_router_issue": 111,
            "programme_router_state": "OPEN",
            "proof_classification": "NEW_TRACER_BULLET",
            "architectural_proof_classification_status": "COMPLETE / FINALISED",
            "selected_proof_vehicle": "NEW_TRACER_BULLET",
            "reuse_existing_proof": "NOT SELECTED",
            "tracer_bullet": "REQUIRED / NOT YET DEFINED",
            "tracer_bullet_id": "NONE / NOT CREATED",
            "architectural_proof_execution": "NOT STARTED",
            "development_entry_hard_stop_condition_9": "SATISFIED",
            "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
            "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
            "phase8": "AUTHORISED",
            "application_implementation": "AUTHORISED",
            "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        }
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertEqual(value, self.promotion.get(key))

    def test_contract_semantic_sections_match_the_immutable_candidate(self):
        candidate_text = self.candidate.decode("utf-8")
        self.assertEqual(
            _contract_semantic_body(candidate_text, "## Candidate lifecycle handoff"),
            _contract_semantic_body(self.contract, "## Certification and current-status promotion record"),
        )

    def test_open_work_routes_to_development_entry_hard_stop_and_keeps_all_stops(self):
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", self.open_work_state.get("phase_7c"))
        self.assertEqual("NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION", self.open_work_state.get("next_stage"))
        self.assertEqual(124, self.open_work_state.get("phase_7c_execution_tracker_issue"))
        self.assertEqual("CLOSED / COMPLETED", self.open_work_state.get("phase_7c_execution_tracker_state"))
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", self.open_work_state.get("phase_7b_reconciliation"))
        self.assertEqual("CLOSED / COMPLETED", self.open_work_state.get("phase_7b_reconciliation_execution_tracker_state"))
        self.assertEqual("OPEN", self.open_work_state.get("programme_router_issue_111_state"))
        self.assertEqual("NEW_TRACER_BULLET", self.open_work_state.get("proof_classification"))
        self.assertEqual("AUTHORISED", self.open_work_state.get("application_implementation"))
        self.assertEqual("AUTHORISED", self.open_work_state.get("phase8"))
        contract_state = self.open_work_state.get("phase_7c_final_feature_pack_contract", {})
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", contract_state.get("lifecycle"))
        self.assertEqual("NEW_TRACER_BULLET", contract_state.get("proof_classification"))
        self.assertEqual("NOT SELECTED", self.open_work_state.get("reuse_existing_proof"))
        self.assertEqual("NONE / NOT CREATED", self.open_work_state.get("tracer_bullet_id"))
        self.assertEqual("NOT STARTED", self.open_work_state.get("architectural_proof_execution"))
        self.assertEqual("PASS / ALL 10 CONDITIONS SATISFIED", self.open_work_state.get("development_entry_hard_stop_status"))
        self.assertEqual("SATISFIED", self.open_work_state.get("development_entry_hard_stop_conditions_1_through_10"))
        self.assertEqual("AUTHORISED", contract_state.get("phase8"))
        self.assertIn("bounded Phase 8", self.open_work)
        self.assertIn("PHASE 7C: COMPLETE / CERTIFIED / CURRENT", self.open_work)
        self.assertIn("PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED", self.open_work)
        current_lifecycle = self.open_work.split("# 9. Immediate Next Action", 1)[1].split("# 10. Minimal Tools", 1)[0]
        self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED", current_lifecycle)
        self.assertIn("PROOF CLASSIFICATION: NEW_TRACER_BULLET", current_lifecycle)
        self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", self.open_work)

    def test_readme_and_manifest_route_current_lower_level_artifacts_without_new_root_authority(self):
        for path in (
            "working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
            "working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
            "02_OPEN_WORK_v1.2.74.md",
        ):
            with self.subTest(path=path):
                self.assertIn(path, self.readme)
        self.assertIn("PHASE 7C: COMPLETE / CERTIFIED / CURRENT", self.readme)
        self.assertIn("FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT", self.readme)
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", self.readme)
        historical = self.readme.split("## Historical status evidence", 1)[1]
        self.assertIn("Phase 8 and executable implementation remain UNAUTHORISED", historical)

        authorities = self.manifest["governing_documents"] + self.manifest["reference_documents"]
        self.assertNotIn(
            "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
            [entry["repository_path"] for entry in authorities],
        )
        archived = next(
            entry for entry in self.manifest["historical_documents"]
            if entry.get("document_id") == "FP001_PHASE_7C_CONTRACT_PR_125_CANDIDATE"
        )
        self.assertEqual(
            "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
            archived["repository_path"],
        )
        self.assertEqual(CANDIDATE_ARCHIVE_SHA256, archived["sha256"])

    def test_four_direct_predecessors_are_archived_byte_identically_and_hash_pinned(self):
        rule = self.manifest["integrity_rules"]["fp001_phase7c_final_contract_current_promotion"]
        pinned = rule["predecessor_archives_sha256"]
        for source, archived in PREDECESSORS:
            with self.subTest(archived=archived):
                source_bytes = _git_show(ROUTING_BASE_SHA, source)
                archived_bytes = (ROOT / archived).read_bytes()
                self.assertEqual(source_bytes, archived_bytes)
                self.assertEqual(hashlib.sha256(archived_bytes).hexdigest(), pinned.get(archived))

    def test_no_upstream_authority_or_application_source_changed(self):
        for path in PROTECTED_PATHS:
            with self.subTest(path=path):
                self.assertEqual(_git_show(CLASSIFICATION_BASE_MAIN, path), (ROOT / path).read_bytes())
        changed = subprocess.run(
            ["git", "diff", "--name-only", CLASSIFICATION_BASE_MAIN],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        application_prefixes = ("app/", "apps/", "backend/", "frontend/", "lib/", "src/")
        self.assertEqual([], [path for path in changed if path.startswith(application_prefixes)])
