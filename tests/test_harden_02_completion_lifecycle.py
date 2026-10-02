from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import _h02_lifecycle_state


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.55.md"
README = DOCS / "README.md"
CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.9.md"
JSON_START = "<!-- HARDEN_02_LIFECYCLE_STATE_START -->"
JSON_END = "<!-- HARDEN_02_LIFECYCLE_STATE_END -->"
JSON_BLOCK = re.compile(
    re.escape(JSON_START) + r"\s*```json\s*(\{.*?\})\s*```\s*" + re.escape(JSON_END),
    re.DOTALL,
)


class Harden02CompletionLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.open_work = OPEN_WORK.read_text(encoding="utf-8")
        self.readme = README.read_text(encoding="utf-8")
        self.contract = CONTRACT.read_text(encoding="utf-8")

    def _state(self, open_work: str | None = None) -> dict[str, object]:
        text = self.open_work if open_work is None else open_work
        match = JSON_BLOCK.search(text)
        self.assertIsNotNone(match, "current Open Work must contain one marked lifecycle JSON object")
        return json.loads(match.group(1))

    def _with_state(self, state: dict[str, object], text: str | None = None) -> str:
        source = self.open_work if text is None else text
        match = JSON_BLOCK.search(source)
        self.assertIsNotNone(match)
        encoded = json.dumps(state, indent=2, ensure_ascii=False)
        return source[: match.start(1)] + encoded + source[match.end(1) :]

    def _assert_rejected(self, open_work: str, readme: str | None = None, contract: str | None = None):
        valid, reason = _h02_lifecycle_state(
            open_work,
            self.readme if readme is None else readme,
            self.contract if contract is None else contract,
        )
        self.assertFalse(valid, reason)

    def test_complete_state_binds_the_execution_evidence_and_downstream_route(self):
        state = self._state()
        self.assertEqual("COMPLETE / CERTIFIED", state["harden_02_execution"])
        self.assertEqual("CERTIFIED FP-001 PMR RECONCILIATION", state["current_stage"])
        self.assertEqual("COMMUNICATIONS JIT DOMAIN DOSSIER", state["next_stage"])
        self.assertEqual("COMPLETE / CERTIFIED", state["engineering_standards_authority_promotion"])
        self.assertEqual("COMPLETE / CERTIFIED", state["fp001_reconciliation"])
        self.assertEqual("REQUIRED / NEXT / NOT_STARTED", state["communications"])
        self.assertEqual(
            (True, "HARDEN-02 execution completion and downstream route are coherent"),
            _h02_lifecycle_state(self.open_work, self.readme, self.contract),
        )

    def test_complete_execution_cannot_keep_the_harden_route(self):
        state = self._state()
        state["current_stage"] = "HARDEN-02 EXECUTION / STRUCTURAL HARDENING"
        state["next_stage"] = "HARDEN-02_EXECUTION_REQUIRED"
        text = self._with_state(state)
        text = text.replace(
            "CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED FP-001 PMR RECONCILIATION",
            "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
            1,
        ).replace(
            "NEXT STAGE: COMMUNICATIONS JIT DOMAIN DOSSIER",
            "NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED",
            1,
        )
        self._assert_rejected(text)

    def test_complete_execution_cannot_keep_a_conflicting_current_contract_route(self):
        contract = self.contract.replace(
            "The immediate next task is `COMMUNICATIONS JIT DOMAIN DOSSIER`",
            "The immediate next task is HARDEN-02_EXECUTION_REQUIRED",
            1,
        )
        self._assert_rejected(self.open_work, contract=contract)

    def test_current_programme_state_row_cannot_remain_in_progress(self):
        text = self.open_work.replace(
            "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION COMPLETE / CERTIFIED",
            "HARDEN-02 EXECUTION IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
            1,
        )
        self._assert_rejected(text)

    def test_current_programme_state_row_must_name_the_current_status_successor(self):
        start = self.open_work.index("## 12.1 Programme state")
        end = self.open_work.index("## 12.2", start)
        row = self.open_work[start:end]
        changed_row = row.replace(
            "`working/HARDEN-02_CONTRACT_WORKING_v0.4.9.md`",
            "`working/HARDEN-02_CONTRACT_WORKING_v0.4.6.md`",
            1,
        )
        text = self.open_work[:start] + changed_row + self.open_work[end:]
        self._assert_rejected(text)

    def test_incomplete_execution_cannot_route_to_engineering_standards(self):
        state = self._state()
        state["harden_02_execution"] = "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
        state["execution_certification"] = None
        text = self._with_state(state)
        self._assert_rejected(text)

    def test_certified_standards_cannot_skip_fp001_reconciliation(self):
        state = self._state()
        state["next_stage"] = "COMMUNICATIONS"
        self._assert_rejected(self._with_state(state))

    def test_fp001_reconciliation_cannot_be_performed(self):
        state = self._state()
        state["fp001_reconciliation"] = "REQUIRED / NEXT / NOT PERFORMED"
        self._assert_rejected(self._with_state(state))

    def test_communications_cannot_start_early(self):
        state = self._state()
        state["communications"] = "REQUIRED / STARTED"
        self._assert_rejected(self._with_state(state))

    def test_phase_7c_cannot_be_unblocked(self):
        state = self._state()
        state["phase_7c"] = "NEXT / AUTHORISED"
        self._assert_rejected(self._with_state(state))

    def test_proof_classification_cannot_be_finalised(self):
        state = self._state()
        state["proof_classification"] = "FINALISED"
        self._assert_rejected(self._with_state(state))

    def test_application_implementation_cannot_be_authorised(self):
        state = self._state()
        state["application_implementation"] = "AUTHORISED"
        self._assert_rejected(self._with_state(state))

    def test_store_and_cer_remain_excluded(self):
        state = self._state()
        state["store_cer"] = "IN SCOPE"
        self._assert_rejected(self._with_state(state))

    def test_readme_open_work_and_lifecycle_json_must_agree(self):
        self._assert_rejected(
            self.open_work,
            self.readme.replace(
                "HARDEN-02 EXECUTION: COMPLETE / CERTIFIED",
                "HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
                1,
            ),
        )

    def test_readme_current_programme_must_match_the_lifecycle_json(self):
        self._assert_rejected(
            self.open_work,
            self.readme.replace(
            "- CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED FP-001 PMR RECONCILIATION",
                "- CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
                1,
            ),
        )

    def test_unsupported_status_successor_version_is_rejected(self):
        state = self._state()
        state["status_successor_version"] = "0.4.8"
        self._assert_rejected(self._with_state(state))

    def test_missing_or_changed_execution_certificate_evidence_is_rejected(self):
        state = self._state()
        evidence = state["execution_certification"]
        mutants = []
        for field in (
            "pre_merge_attestation_url",
            "exact_head_ci_run_url",
            "candidate_sha",
            "resulting_main_sha",
            "resulting_main_tree_sha",
            "resulting_main_ci_run_url",
            "post_merge_review_outcome",
            "post_merge_attestation_url",
            "whole_roadmap_section_21_preserved_sha256",
        ):
            changed = dict(state)
            changed_evidence = dict(evidence)
            changed_evidence[field] = ""
            changed["execution_certification"] = changed_evidence
            mutants.append(changed)
        for mutant in mutants:
            with self.subTest(evidence=mutant["execution_certification"]):
                self._assert_rejected(self._with_state(mutant))


if __name__ == "__main__":
    unittest.main()
