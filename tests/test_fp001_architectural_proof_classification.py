from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
BASE_SHA = "24a9ad925ee1ab6d75ddb44bae6df0b4f3d09bca"
CLASSIFICATION_BRANCH = "governance/fp001-architectural-proof-classification"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.73.md"
CONTRACT = DOCS / "working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
CONTRACT_ARCHIVE = DOCS / "archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
HARDEN_02 = DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.17.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
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


def _git_show(commit: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def _marked_json(text: str, start: str, end: str) -> dict:
    match = re.search(re.escape(start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(end), text, re.DOTALL)
    return json.loads(match.group(1)) if match else {}


def _contract_section(text: str, label: str) -> str:
    start_match = re.search(rf"(?m)^## {re.escape(label)}\. ", text)
    if start_match is None:
        return ""
    end_match = re.search(r"(?m)^## ", text[start_match.end():])
    end = start_match.end() + end_match.start() if end_match else len(text)
    return text[start_match.start():end]


def _numbered_section(text: str, number: int) -> str:
    start_match = re.search(rf"(?m)^## {number}\. ", text)
    if start_match is None:
        return ""
    end_match = re.search(r"(?m)^## \d+\. ", text[start_match.end():])
    end = start_match.end() + end_match.start() if end_match else len(text)
    return text[start_match.start():end]


class FP001ArchitecturalProofClassificationTests(unittest.TestCase):
    def test_current_route_finishes_classification_and_keeps_phase8_unauthorised(self):
        self.assertTrue(OPEN_WORK.is_file(), "Open Work v1.2.73 must be the current successor")
        if not OPEN_WORK.is_file():
            return
        text = OPEN_WORK.read_text(encoding="utf-8")
        state = _marked_json(
            text,
            "<!-- HARDEN_02_LIFECYCLE_STATE_START -->",
            "<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        )
        expected = {
            "phase_7a": "COMPLETE",
            "required_jit_dossier_set": "DISPOSITION-COMPLETE",
            "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
            "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
            "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
            "programme_router_issue_111_state": "OPEN",
            "architectural_proof_classification_status": "COMPLETE / FINALISED",
            "architectural_proof_requirement": "NEW_TRACER_BULLET",
            "selected_proof_vehicle": "NEW_TRACER_BULLET",
            "reuse_existing_proof": "NOT SELECTED",
            "tracer_bullet": "REQUIRED / NOT YET DEFINED",
            "tracer_bullet_id": "NONE / NOT CREATED",
            "architectural_proof_execution": "NOT STARTED",
            "phase8": "UNAUTHORISED",
            "application_implementation": "UNAUTHORISED / BLOCKED UNTIL ALL DEVELOPMENT ENTRY HARD STOP CONDITIONS PASS",
            "development_entry_hard_stop_condition_9": "SATISFIED",
            "remaining_development_entry_hard_stop_conditions": "NOT EVALUATED / MUST PASS BEFORE PHASE 8",
            "next_governance_action": "DEVELOPMENT ENTRY HARD STOP EVALUATION",
        }
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertEqual(value, state.get(key))

        active = text.split("# 9. Immediate Next Action", 1)[1].split("# 10. Minimal Tools", 1)[0]
        for token in (
            "PHASE 7A: COMPLETE",
            "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
            "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
            "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
            "ISSUE #124: CLOSED / COMPLETED",
            "PROGRAMME ROUTER #111: OPEN",
            "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
            "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
            "REUSE_EXISTING_PROOF: NOT SELECTED",
            "TRACER BULLET: REQUIRED / NOT YET DEFINED",
            "TRACER BULLET ID: NONE / NOT CREATED",
            "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
            "PHASE 8: UNAUTHORISED",
            "APPLICATION IMPLEMENTATION: UNAUTHORISED",
            "NEXT GOVERNANCE ACTION: DEVELOPMENT ENTRY HARD STOP EVALUATION",
        ):
            with self.subTest(token=token):
                self.assertIn(token, active)
        self.assertIn("Classification satisfies only Development Entry Hard Stop condition 9", active)
        self.assertIn("every other applicable Development Entry Hard Stop condition is independently evaluated and satisfied", active)
        self.assertIn("OQ-035", active)
        self.assertIn("OQ-036", active)
        self.assertNotRegex(active, r"\bTB-\d{3,}\b")

    def test_classification_rationale_uses_contract_and_historical_baseline_evidence(self):
        self.assertTrue(OPEN_WORK.is_file(), "Open Work v1.2.73 must contain the classification record")
        if not OPEN_WORK.is_file():
            return
        text = OPEN_WORK.read_text(encoding="utf-8")
        for statement in (
            "Roadmap v1.2.3 records `PROBABLY_NEW_TRACER_BULLET` as provisional anticipation. That anticipation is not the basis for this decision.",
            "The certified/current Final Feature Pack Contract v0.1.0 says `FLOW-01` is supporting evidence only, and `PASS_WITH_DOWNSTREAM_GATES` does not close executable obligations.",
            "Reuse would have to exercise the same real selected architecture and every applicable proof obligation.",
            "A new Tracer Bullet must prove a materially unproven architectural claim through the real path.",
            f"At classification baseline `main@{BASE_SHA}`, the canonical repository contained no executable application, `mix.exs`, or Elixir `defmodule` implementation.",
            "No existing executable Ash/Phoenix Identity, session, or recovery implementation proof could satisfy `REUSE_EXISTING_PROOF`.",
            "The selected Identity architecture and the Final Contract's executable obligations remain materially unproven.",
            "The Final Feature Pack Contract is not the classification authority or event.",
        ):
            with self.subTest(statement=statement):
                self.assertIn(statement, text)

    def test_contract_status_reflects_selection_without_changing_frozen_proof_semantics(self):
        self.assertTrue(CONTRACT.is_file())
        if not CONTRACT.is_file():
            return
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("## P. Architectural proof requirement", text)
        proof_section = text.split("## P. Architectural proof requirement", 1)[1].split("## Q. Vertical Slice map", 1)[0]
        self.assertIn("The proof vehicle and final proof classification remain NOT FINALISED.", proof_section)
        self.assertIn("`FLOW-01` is supporting evidence.", proof_section)
        self.assertIn("Its `PASS_WITH_DOWNSTREAM_GATES` result does not close these executable obligations.", proof_section)
        self.assertIn("the later gate must select either `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`", proof_section)
        self.assertIn("If the later gate selects `REUSE_EXISTING_PROOF`, it must show that existing evidence exercises this same architecture and all applicable obligations.", proof_section)
        self.assertIn("If it selects `NEW_TRACER_BULLET`, the tracer must prove a materially unproven architectural claim through the real path.", proof_section)
        self.assertIn("ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET", text.split("## A. Identity and provenance", 1)[0])
        self.assertIn("The classification status above is a downstream lifecycle reflection only. Open Work v1.2.73 records the separate classification authority/event.", text)
        self.assertEqual(
            "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
            hashlib.sha256(CONTRACT_ARCHIVE.read_bytes()).hexdigest(),
        )

    def test_final_contract_hash_pins_match_each_other_and_current_bytes(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        rule = manifest["integrity_rules"]["roadmap_proof_classification_lifecycle"]
        contract_path = rule["phase7c_contract_path"]
        actual_sha256 = hashlib.sha256(CONTRACT.read_bytes()).hexdigest()

        self.assertEqual(actual_sha256, rule["phase7c_contract_sha256"])
        self.assertEqual(actual_sha256, rule["current_route_sha256"][contract_path])

    def test_harden_02_current_sections_route_the_completed_classification(self):
        text = HARDEN_02.read_text(encoding="utf-8")
        sections = {
            "18": _numbered_section(text, 18),
            "23": _numbered_section(text, 23),
        }
        stale_route = re.compile(
            r"(?is)(?:proof classification|architectural proof classification)"
            r"[^\n.]{0,120}(?:NOT FINALISED|NEXT\s*/\s*NOT PERFORMED|next and remains unperformed)"
        )
        required_current_state = (
            "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
            "NEW_TRACER_BULLET",
            "NEXT GOVERNANCE ACTION: DEVELOPMENT ENTRY HARD STOP EVALUATION",
            "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
        )

        for number, section in sections.items():
            with self.subTest(section=number):
                self.assertTrue(section, f"HARDEN-02 §{number} must exist")
                self.assertNotRegex(section, stale_route)
                for token in required_current_state:
                    with self.subTest(token=token):
                        self.assertIn(token, section)

        self.assertIn("REUSE_EXISTING_PROOF: NOT SELECTED", sections["18"])
        self.assertIn("ARCHITECTURAL PROOF EXECUTION: NOT STARTED", sections["18"])
        self.assertIn("CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9", sections["18"])
        self.assertIn("until every other applicable condition passes", sections["18"].lower())

    def test_certified_contract_semantic_sections_match_the_immutable_candidate(self):
        current = CONTRACT.read_text(encoding="utf-8")
        candidate = CONTRACT_ARCHIVE.read_text(encoding="utf-8")
        for label in "BCDEFGHIJKLMNOP":
            with self.subTest(section=label):
                self.assertEqual(_contract_section(candidate, label), _contract_section(current, label))

        candidate_q = _contract_section(candidate, "Q").replace(
            "Phase 7C exit for this candidate means only that the contract is authored and ready for fresh independent exact-head review. Certification, current-status promotion, proof classification, and Phase 8 entry are separate later gates.",
            "DOWNSTREAM LIFECYCLE STATUS REFLECTION",
        )
        current_q = _contract_section(current, "Q").replace(
            "Phase 7C contract delivery is COMPLETE / CERTIFIED / CURRENT under this separate status successor. The separate downstream classification status is COMPLETE / FINALISED as NEW_TRACER_BULLET; proof execution, Phase 8 entry and application implementation remain gated.",
            "DOWNSTREAM LIFECYCLE STATUS REFLECTION",
        )
        self.assertEqual(candidate_q, current_q)

    def test_direct_predecessor_archives_match_the_verified_base_byte_for_byte(self):
        manifest = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
        rule = manifest["integrity_rules"]["roadmap_proof_classification_lifecycle"]
        pinned = rule["predecessor_archives_sha256"]
        for source, archived in PREDECESSORS:
            with self.subTest(archived=archived):
                archived_bytes = (ROOT / archived).read_bytes()
                self.assertEqual(_git_show(BASE_SHA, source), archived_bytes)
                self.assertEqual(pinned[archived], hashlib.sha256(archived_bytes).hexdigest())

    def test_baseline_proves_no_application_source_without_banning_future_source(self):
        paths = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", BASE_SHA],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        executable = [
            path for path in paths
            if path == "mix.exs"
            or path.endswith(".ex")
            or any(part in {"lib", "src", "app", "apps", "priv", "migrations", "assets"} for part in Path(path).parts)
        ]
        self.assertEqual([], executable)
        self.assertEqual({".github", "docs", "tests", "tools", ".gitignore"}, {Path(path).parts[0] for path in paths})

    @unittest.skipUnless(
        os.getenv("GITHUB_HEAD_REF", "") == CLASSIFICATION_BRANCH
        or subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip() == CLASSIFICATION_BRANCH,
        "candidate-only changed-path guard runs only for the classification PR",
    )
    def test_classification_pr_does_not_add_executable_application_source(self):
        changed = subprocess.run(
            ["git", "diff", "--name-only", BASE_SHA],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        forbidden = []
        for path in changed:
            parts = Path(path).parts
            if Path(path).name == "mix.exs" or path.endswith(".ex"):
                forbidden.append(path)
            elif any(part in {"lib", "src", "app", "apps", "priv", "migrations", "assets"} for part in parts):
                forbidden.append(path)
        self.assertEqual([], forbidden)


if __name__ == "__main__":
    unittest.main()
