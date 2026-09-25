from __future__ import annotations

import copy
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
README = DOCS / "README.md"
STATE_START = "<!-- HARDEN_02_RECOVERY_STATE_START -->"
STATE_END = "<!-- HARDEN_02_RECOVERY_STATE_END -->"

EXPECTED_PMR_COMPLETION_PRECONDITIONS = {
    "current_skeleton_gate_manifest": "MUST_RESOLVE_TO_CURRENT_AUTHORITY",
    "current_skeleton_pmr_requirement": "MUST_INCLUDE_REQUIRED_PMR_OUTCOME",
    "current_identity_jit": "MUST_BE_CURRENT_COMPLETE_AND_MERGED",
    "arq_iam_011": "MUST_PRESERVE_PMR_ACCOUNT_LIFECYCLE_AND_NON_AUTHORITY",
    "arq_iam_012": "MUST_PRESERVE_MINIMUM_DISCLOSURE_AND_LOOKUP_BOUNDARIES",
    "arq_iam_013": "MUST_REMAIN_DEFERRED_WITH_NO_ENCODING_SELECTED",
    "oq_034": "MUST_BE_RESOLVED_IN_CURRENT_DECISION_AUTHORITY",
    "communications": "MUST_REMAIN_REQUIRED_UNTIL_ITS_OWN_JIT_IS_COMPLETE",
    "conditional_dossiers": "MUST_REMAIN_CONDITIONAL_PENDING_EXPLICIT_ADJUDICATION",
    "phase_7c": "MUST_REMAIN_BLOCKED_UNTIL_REQUIRED_WORK_AND_DISPOSITIONS_COMPLETE",
    "proof_classification": "MUST_FOLLOW_APPROVED_FINAL_FEATURE_PACK_CONTRACT",
    "phase_8": "MUST_REMAIN_BLOCKED_UNTIL_DEVELOPMENT_ENTRY_HARD_STOP_PASSES",
    "implementation": "MUST_NOT_BE_AUTHORISED_BY_RECONCILIATION",
}

REQUIRED_IAM_011_CONCEPTS = (
    ("arq-iam-011",),
    ("successfully created individual account", "platform member reference"),
    ("human-facing",),
    ("not database identity",),
    ("not authentication",),
    ("not authorisation",),
    ("identity-verification assurance",),
    ("not membership",),
    ("not subscription",),
    ("not entitlement",),
    ("no account rights",),
    ("non-secret", "private-by-default"),
    ("unique", "immutable", "never reassigned"),
    ("reactivated", "retains"),
    ("genuine final deletion", "permanently non-reusable"),
    ("duplicate-account merge", "canonical active", "retires"),
    ("security", "privacy", "integrity", "reconciliation", "operational-correctness"),
)

REQUIRED_IAM_012_CONCEPTS = (
    ("arq-iam-012",),
    ("minimum information",),
    ("not authentication",),
    ("not authorisation",),
    ("purchaser", "control", "beneficiary consent"),
    ("discount", "entitlement eligibility"),
    ("pseudo-coupon",),
    ("scoped access", "audit"),
)

DEFERRED_IAM_013_TERMS = (
    "prefix",
    "alphabet",
    "payload length",
    "grouping",
    "check algorithm",
    "generation algorithm",
    "collision strategy",
    "database representation",
)


def _manifest_entries() -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    current = {
        entry["document_id"]: entry
        for section in ("governing_documents", "reference_documents")
        for entry in manifest[section]
    }
    return manifest, current


def _marked_json(text: str) -> dict[str, object]:
    if text.count(STATE_START) != 1 or text.count(STATE_END) != 1:
        raise AssertionError("expected one current HARDEN-02 state block")
    start = text.index(STATE_START) + len(STATE_START)
    end = text.index(STATE_END, start)
    match = re.search(r"```json\s*(\{.*?\})\s*```", text[start:end], re.DOTALL)
    if match is None:
        raise AssertionError("current HARDEN-02 state block is missing JSON")
    return json.loads(match.group(1))


def _current_active_working_artifact(pattern: str) -> tuple[Path, str]:
    matches = sorted((DOCS / "working").glob(pattern))
    if len(matches) != 1:
        raise AssertionError(f"expected one current active artifact matching {pattern}, found {len(matches)}")
    path = matches[0]
    return path, path.read_text(encoding="utf-8")


def _has_all_groups(text: str, groups: tuple[tuple[str, ...], ...]) -> bool:
    normalized = text.casefold()
    return all(all(concept in normalized for concept in group) for group in groups)


def _current_authority_references_resolve(
    text: str,
    current: dict[str, dict[str, object]],
    document_ids: tuple[str, ...],
) -> bool:
    return all(
        Path(str(current[document_id]["repository_path"])).name in text
        for document_id in document_ids
    )


def _pmr_lifecycle_and_lookup_are_current(identity_jit: str) -> bool:
    if not _has_all_groups(identity_jit, REQUIRED_IAM_011_CONCEPTS):
        return False
    if not _has_all_groups(identity_jit, REQUIRED_IAM_012_CONCEPTS):
        return False
    normalized = identity_jit.casefold()
    if "arq-iam-013" not in normalized or "deferred" not in normalized:
        return False
    if not all(term in normalized for term in DEFERRED_IAM_013_TERMS):
        return False
    if re.search(r"(?im)^\s*arq-iam-013\s*:\s*(?:selected|resolved|complete)", identity_jit):
        return False
    return True


def _pmr_completion_evidence_valid(
    state: dict[str, object],
    skeleton: str,
    gate_manifest: str,
    identity_jit: str,
    decisions: str,
    current: dict[str, dict[str, object]],
) -> bool:
    if state.get("fp001_reconciliation_completion_preconditions") != EXPECTED_PMR_COMPLETION_PRECONDITIONS:
        return False
    current_source_ids = (
        "PLATFORM_BASELINE",
        "DECISION_REGISTER",
        "ARCHITECTURE_SYNTHESIS",
        "DOMAIN_MAP",
        "ROADMAP",
        "ARCHITECTURE_REQUIREMENTS",
    )
    if not _current_authority_references_resolve(skeleton, current, current_source_ids):
        return False
    if not _current_authority_references_resolve(gate_manifest, current, current_source_ids):
        return False
    if not _current_authority_references_resolve(identity_jit, current, current_source_ids):
        return False
    if not re.search(r"(?is)(?:platform member reference|\bpmr\b).{0,100}\brequired\b", skeleton):
        return False
    if not re.search(r"(?is)(?:platform member reference|\bpmr\b).{0,100}\brequired\b", gate_manifest):
        return False

    oq_034_start = decisions.find("## OQ-034 —")
    oq_035_start = decisions.find("## OQ-035 —", oq_034_start)
    if oq_034_start < 0 or oq_035_start < 0:
        return False
    oq_034 = decisions[oq_034_start:oq_035_start]
    if not re.search(r"(?im)^\*\*Status:\*\*\s*RESOLVED\b", oq_034):
        return False

    if not _pmr_lifecycle_and_lookup_are_current(identity_jit):
        return False
    if "READY_FOR_EXPLICIT_RESOLUTION" in identity_jit:
        return False
    if not re.search(r"(?im)^\s*MERGED:\s*YES\s*$", identity_jit):
        return False
    if re.search(r"(?im)^\s*MERGED:\s*NO\s*$", identity_jit):
        return False

    conditional = state.get("conditional_dossiers")
    expected_conditional = {
        "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "analytics": "NOT REQUIRED",
    }
    return all(
        (
            isinstance(conditional, dict) and conditional == expected_conditional,
            state.get("communications") == "REQUIRED / NOT_STARTED",
            state.get("phase_7c") == "BLOCKED / NOT_STARTED",
            state.get("proof_classification") == "NOT FINALISED",
            state.get("final_feature_pack_contract") == "NOT STARTED",
            state.get("phase_8") == "BLOCKED",
            state.get("application_implementation") == "BLOCKED",
        )
    )


def _pmr_reconciliation_state_consistent(
    state: dict[str, object],
    skeleton: str,
    gate_manifest: str,
    identity_jit: str,
    decisions: str,
    current: dict[str, dict[str, object]],
) -> bool:
    status = state.get("fp001_reconciliation")
    if status == "COMPLETE":
        return _pmr_completion_evidence_valid(state, skeleton, gate_manifest, identity_jit, decisions, current)
    return status == "REQUIRED / DOWNSTREAM / NOT PERFORMED"


def _conditional_dossier_gate_consistent(state: dict[str, object]) -> bool:
    phase_7c = str(state.get("phase_7c", ""))
    if not re.search(r"\b(?:READY|COMPLETE|APPROVED)\b", phase_7c):
        return True
    conditional = state.get("conditional_dossiers")
    return (
        isinstance(conditional, dict)
        and all("PENDING" not in str(value) for value in conditional.values())
        and state.get("communications") == "COMPLETE / MERGED"
    )


def _proof_timing_consistent(state: dict[str, object]) -> bool:
    proof = str(state.get("proof_classification", ""))
    if proof == "NOT FINALISED":
        return True
    return (
        proof in {"REUSE_EXISTING_PROOF", "NEW_TRACER_BULLET"}
        and state.get("final_feature_pack_contract") == "APPROVED"
    )


def _development_entry_preconditions_complete(state: dict[str, object]) -> bool:
    return all(
        (
            state.get("hardening_programme_complete") is True,
            state.get("engineering_standards_authority_promotion") == "COMPLETE / CERTIFIED",
            state.get("fp001_reconciliation") == "COMPLETE",
            state.get("communications") == "COMPLETE / MERGED",
            state.get("phase_7c") == "COMPLETE / APPROVED",
            state.get("final_feature_pack_contract") == "APPROVED",
            state.get("proof_classification") in {"REUSE_EXISTING_PROOF", "NEW_TRACER_BULLET"},
            _conditional_dossier_gate_consistent(state),
            _proof_timing_consistent(state),
        )
    )


def _phase_8_gate_consistent(state: dict[str, object]) -> bool:
    if state.get("phase_8") == "BLOCKED":
        return state.get("application_implementation") == "BLOCKED"
    return state.get("phase_8") == "PASSED" and _development_entry_preconditions_complete(state)


def _implementation_authority_consistent(state: dict[str, object]) -> bool:
    if state.get("application_implementation") == "BLOCKED":
        return True
    return state.get("phase_8") == "PASSED" and _development_entry_preconditions_complete(state)


def _single_current_stage(text: str, state: dict[str, object]) -> bool:
    current = re.findall(r"^CURRENT AUTHORITY-STAGE PROGRAMME:\s*(.+)$", text, re.MULTILINE)
    next_stage = re.findall(r"^NEXT STAGE:\s*(.+)$", text, re.MULTILINE)
    return (
        current == ["HARDEN-02 EXECUTION / STRUCTURAL HARDENING"]
        and next_stage == ["HARDEN-02_EXECUTION_REQUIRED"]
        and state.get("current_stage") == next_stage[0]
        and state.get("next_stage") == next_stage[0]
    )


class Harden02ExecutionInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest, cls.current = _manifest_entries()
        cls.open_work_path = ROOT / str(cls.current["OPEN_WORK"]["repository_path"])
        cls.open_work = cls.open_work_path.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.state = _marked_json(cls.open_work)
        _, cls.skeleton = _current_active_working_artifact("FP-001_FEATURE_PACK_SKELETON_WORKING_v*.md")
        _, cls.identity_jit = _current_active_working_artifact("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v*.md")
        cls.gate_manifest = ""
        decisions_path = ROOT / str(cls.current["DECISION_REGISTER"]["repository_path"])
        cls.decisions = decisions_path.read_text(encoding="utf-8")

    def _complete_pmr_fixture(self):
        source_ids = (
            "PLATFORM_BASELINE",
            "DECISION_REGISTER",
            "ARCHITECTURE_SYNTHESIS",
            "DOMAIN_MAP",
            "ROADMAP",
            "ARCHITECTURE_REQUIREMENTS",
        )
        current_refs = " ".join(
            Path(str(self.current[document_id]["repository_path"])).name
            for document_id in source_ids
        )
        skeleton = f"Platform Member Reference is REQUIRED. {current_refs}"
        gate_manifest = f"Platform Member Reference is REQUIRED. {current_refs}"
        iam_terms = " ".join(term for group in REQUIRED_IAM_011_CONCEPTS + REQUIRED_IAM_012_CONCEPTS for term in group)
        identity_jit = (
            f"{iam_terms} ARQ-IAM-013 is deferred. "
            f"{' '.join(DEFERRED_IAM_013_TERMS)}. {current_refs}\nMERGED: YES\n"
        )
        decisions = "## OQ-034 — Authentication\n**Status:** RESOLVED\n## OQ-035 — Abuse\n"
        complete_state = copy.deepcopy(self.state)
        complete_state["fp001_reconciliation"] = "COMPLETE"
        complete_state["fp001_reconciliation_completion_preconditions"] = EXPECTED_PMR_COMPLETION_PRECONDITIONS
        complete_state["final_feature_pack_contract"] = "NOT STARTED"
        complete_state["phase_8"] = "BLOCKED"
        return complete_state, skeleton, gate_manifest, identity_jit, decisions

    def test_single_current_stage_rejects_conflicting_active_routes(self):
        self.assertTrue(_single_current_stage(self.open_work, self.state))
        duplicate = self.open_work + (
            "\nCURRENT AUTHORITY-STAGE PROGRAMME: ENGINEERING STANDARDS\n"
            "NEXT STAGE: ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED\n"
        )
        self.assertFalse(_single_current_stage(duplicate, self.state))

    def test_execution_candidate_is_in_progress_but_not_complete(self):
        self.assertEqual("COMPLETE / CERTIFIED", self.state["contract_status"])
        self.assertEqual("IN PROGRESS / NOT COMPLETE / AWAITING INDEPENDENT REVIEW", self.state["harden_02_execution"])
        self.assertEqual("CLOSED / SUPERSEDED / HISTORICAL BRANCH NOT MERGED", self.state["pr_38"])
        self.assertNotIn("HARDEN-02 EXECUTION: COMPLETE", self.open_work)
        self.assertNotIn("HARDEN-02 EXECUTION: COMPLETE", self.readme)

    def test_downstream_work_remains_blocked_in_governed_order(self):
        self.assertEqual("DOWNSTREAM / NOT STARTED", self.state["engineering_standards_authority_promotion"])
        self.assertEqual("REQUIRED / DOWNSTREAM / NOT PERFORMED", self.state["fp001_reconciliation"])
        self.assertEqual("REQUIRED / NOT_STARTED", self.state["communications"])
        self.assertEqual("BLOCKED / NOT_STARTED", self.state["phase_7c"])
        self.assertEqual("NOT FINALISED", self.state["proof_classification"])
        self.assertEqual("NOT STARTED", self.state.get("final_feature_pack_contract"))
        self.assertEqual("BLOCKED", self.state.get("phase_8"))
        self.assertEqual("BLOCKED", self.state["application_implementation"])
        self.assertEqual("EXCLUDED", self.state["store_cer"])
        self.assertTrue(_conditional_dossier_gate_consistent(self.state))
        self.assertTrue(_proof_timing_consistent(self.state))
        self.assertTrue(_phase_8_gate_consistent(self.state))
        self.assertTrue(_implementation_authority_consistent(self.state))
        self.assertIn("- FINAL FEATURE PACK CONTRACT: NOT STARTED", self.readme)
        self.assertIn("- PHASE 8: BLOCKED", self.readme)

    def test_release_only_open_questions_remain_release_only(self):
        self.assertEqual("UNRESOLVED / RELEASE-ONLY", self.state.get("oq_035"))
        self.assertEqual("UNRESOLVED / RELEASE-ONLY", self.state.get("oq_036"))
        self.assertIn("OQ-035: SECURITY / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY", self.open_work)
        self.assertIn("OQ-036: VENDOR / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY", self.open_work)

    def test_pmr_exit_preconditions_are_explicit_without_reconciling_current_artifacts(self):
        self.assertEqual("REQUIRED / DOWNSTREAM / NOT PERFORMED", self.state["fp001_reconciliation"])
        self.assertEqual(EXPECTED_PMR_COMPLETION_PRECONDITIONS, self.state.get("fp001_reconciliation_completion_preconditions"))
        self.assertTrue(_pmr_reconciliation_state_consistent(
            self.state,
            self.skeleton,
            self.gate_manifest,
            self.identity_jit,
            self.decisions,
            self.current,
        ))
        self.assertIn("FP001_RECONCILIATION_REQUIRED", self.open_work)
        self.assertNotEqual("COMPLETE", self.state["fp001_reconciliation"])

    def test_adversarial_partial_pmr_reconciliation_fails_when_identity_jit_is_stale(self):
        complete, _, _, _, decisions = self._complete_pmr_fixture()
        self.assertFalse(_pmr_reconciliation_state_consistent(
            complete,
            self.skeleton,
            self.gate_manifest,
            self.identity_jit,
            decisions,
            self.current,
        ))

        skeleton_only_updated = self.skeleton + (
            "\nPlatform Member Reference is REQUIRED for each successfully created individual Account.\n"
        )
        self.assertFalse(_pmr_reconciliation_state_consistent(
            complete,
            skeleton_only_updated,
            self.gate_manifest,
            self.identity_jit,
            decisions,
            self.current,
        ))

    def test_pmr_completion_requires_gate_manifest_with_current_authority_links(self):
        complete, skeleton, gate_manifest, identity_jit, decisions = self._complete_pmr_fixture()
        self.assertTrue(_pmr_reconciliation_state_consistent(
            complete,
            skeleton,
            gate_manifest,
            identity_jit,
            decisions,
            self.current,
        ))
        self.assertFalse(_pmr_reconciliation_state_consistent(
            complete,
            skeleton,
            "",
            identity_jit,
            decisions,
            self.current,
        ))

        stale_current = copy.deepcopy(self.current)
        stale_current["ROADMAP"] = {
            **stale_current["ROADMAP"],
            "repository_path": "docs/00_platform/archive/05_ROADMAP_v1.0.0.md",
        }
        self.assertFalse(_pmr_reconciliation_state_consistent(
            complete,
            skeleton,
            gate_manifest,
            identity_jit,
            decisions,
            stale_current,
        ))

    def test_adversarial_conditional_dossier_bypass_fails_closed(self):
        bypass = copy.deepcopy(self.state)
        bypass["phase_7c"] = "READY"
        self.assertFalse(_conditional_dossier_gate_consistent(bypass))
        self.assertFalse(_implementation_authority_consistent({**bypass, "application_implementation": "AUTHORISED"}))

    def test_adversarial_proof_skip_fails_before_final_contract(self):
        bypass = copy.deepcopy(self.state)
        bypass["proof_classification"] = "REUSE_EXISTING_PROOF"
        self.assertFalse(_proof_timing_consistent(bypass))

    def test_adversarial_phase_8_and_implementation_cannot_skip_entry_hard_stop(self):
        bypass = copy.deepcopy(self.state)
        bypass["phase_8"] = "PASSED"
        self.assertFalse(_phase_8_gate_consistent(bypass))
        bypass["application_implementation"] = "AUTHORISED"
        self.assertFalse(_implementation_authority_consistent(bypass))

    def test_current_identity_jit_is_not_mistaken_for_pmr_reconciled_state(self):
        self.assertFalse(_pmr_lifecycle_and_lookup_are_current(self.identity_jit))
        self.assertIn("READY_FOR_EXPLICIT_RESOLUTION", self.identity_jit)
        self.assertIn("MERGED: NO", self.identity_jit)

    def test_current_fp001_artifacts_have_stale_authority_pointers(self):
        current_source_ids = (
            "PLATFORM_BASELINE",
            "DECISION_REGISTER",
            "ARCHITECTURE_SYNTHESIS",
            "DOMAIN_MAP",
            "ROADMAP",
            "ARCHITECTURE_REQUIREMENTS",
        )
        self.assertFalse(_current_authority_references_resolve(self.skeleton, self.current, current_source_ids))
        self.assertFalse(_current_authority_references_resolve(self.identity_jit, self.current, current_source_ids))


if __name__ == "__main__":
    unittest.main()
