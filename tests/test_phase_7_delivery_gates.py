from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.phase_7_delivery_gates import validate_phase_7_state


class Phase7DeliveryGateTests(unittest.TestCase):
    def test_blocked_canonical_state_accepts_unresolved_downstream_work(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._base_state(root)

            report = validate_phase_7_state(state, root)

            self.assertEqual("PASS", report["status"])
            self.assertEqual([], report["findings"])

    def test_incomplete_communications_blocks_phase_7c(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._phase_7c_ready_state(root)
            state["communications"] = "REQUIRED / NOT_STARTED"
            self._set_artifact(
                state,
                "FP001_COMMUNICATIONS_JIT",
                status="NOT_STARTED",
                path=None,
            )

            report = validate_phase_7_state(state, root)

            self.assertTrue(self._has_finding(report, "phase_7c_communications_gate"))

    def test_pending_conditional_disposition_blocks_phase_7c(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._phase_7c_ready_state(root)
            state["conditional_dossiers"]["privacy_consent"] = (
                "CONDITIONAL / PENDING EXPLICIT ADJUDICATION"
            )

            report = validate_phase_7_state(state, root)

            self.assertTrue(self._has_finding(report, "phase_7c_conditional_dossiers_gate"))

    def test_not_required_conditional_disposition_satisfies_phase_7c(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._phase_7c_ready_state(root)

            report = validate_phase_7_state(state, root)

            self.assertFalse(self._has_finding(report, "phase_7c_conditional_dossiers_gate"))

    def test_required_conditional_dossier_needs_a_registered_jit_artifact(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._phase_7c_ready_state(root)
            state["conditional_dossiers"]["privacy_consent"] = "REQUIRED / COMPLETE"

            report = validate_phase_7_state(state, root)

            self.assertTrue(self._has_finding(report, "phase_7c_conditional_dossiers_gate"))

    def test_registered_complete_conditional_jit_dossier_satisfies_phase_7c(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._phase_7c_ready_state(root)
            state["conditional_dossiers"]["privacy_consent"] = "REQUIRED / COMPLETE"
            privacy_path = "working/FP-001_PRIVACY_CONSENT_JIT_DOMAIN_DOSSIER_v0.1.0.md"
            self._write_artifact(root, privacy_path)
            state["formal_artifacts"].append(
                self._artifact(
                    "FP001_PRIVACY_CONSENT_JIT",
                    "JIT_DOMAIN_DOSSIER",
                    privacy_path,
                    "COMPLETE",
                )
            )

            report = validate_phase_7_state(state, root)

            self.assertFalse(self._has_finding(report, "phase_7c_conditional_dossiers_gate"))

    def test_final_proof_requires_an_approved_registered_contract(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._base_state(root)
            state["proof_classification"] = "REUSE_EXISTING_PROOF"

            report = validate_phase_7_state(state, root)

            self.assertTrue(self._has_finding(report, "phase_8_proof_classification_gate"))

    def test_pre_jit_artifact_does_not_satisfy_required_jit_dossier(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._phase_7c_ready_state(root)
            pre_jit_path = "working/communications/COMMUNICATIONS_PRE_JIT_v0.1.0.md"
            self._write_artifact(root, pre_jit_path)
            self._set_artifact(
                state,
                "FP001_COMMUNICATIONS_JIT",
                formal_type="PRE_JIT_CONTRACT",
                status="COMPLETE",
                path=pre_jit_path,
            )

            report = validate_phase_7_state(state, root)

            self.assertTrue(self._has_finding(report, "phase_7_formal_artifact_registry"))
            self.assertTrue(self._has_finding(report, "phase_7c_communications_gate"))

    def test_complete_formal_prerequisites_allow_fixture_transition(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._phase_7c_ready_state(root)
            state["phase_7c"] = "COMPLETE"
            state["proof_classification"] = "REUSE_EXISTING_PROOF"
            state["application_implementation"] = "AUTHORISED"
            contract_path = "working/FP-001_FINAL_FEATURE_PACK_CONTRACT_v0.1.0.md"
            self._write_artifact(root, contract_path)
            self._set_artifact(
                state,
                "FP001_FINAL_CONTRACT",
                status="APPROVED",
                path=contract_path,
            )

            report = validate_phase_7_state(state, root)

            self.assertEqual("PASS", report["status"], report["findings"])
            self.assertEqual([], report["findings"])

    def test_application_authorisation_fails_without_phase_7_and_phase_8_entry(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._base_state(root)
            state["application_implementation"] = "AUTHORISED"

            report = validate_phase_7_state(state, root)

            self.assertTrue(self._has_finding(report, "development_entry_formal_gate"))

    def test_duplicate_artifact_identity_fails_closed(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state = self._base_state(root)
            state["formal_artifacts"].append(dict(state["formal_artifacts"][0]))

            report = validate_phase_7_state(state, root)

            self.assertTrue(self._has_finding(report, "phase_7_formal_artifact_registry"))

    @staticmethod
    def _artifact(registry_id: str, formal_type: str, path: str | None, status: str) -> dict:
        return {
            "registry_id": registry_id,
            "formal_type": formal_type,
            "path": path,
            "status": status,
            "requirement": "REQUIRED",
        }

    def _base_state(self, root: Path) -> dict:
        skeleton = "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md"
        identity = "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        self._write_artifact(root, skeleton)
        self._write_artifact(root, identity)
        return {
            "communications": "REQUIRED / NOT_STARTED",
            "conditional_dossiers": {
                "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                "analytics": "NOT REQUIRED",
            },
            "phase_7c": "BLOCKED / NOT_STARTED",
            "proof_classification": "NOT FINALISED",
            "application_implementation": "BLOCKED",
            "formal_artifacts": [
                self._artifact(
                    "FP001_SKELETON_GATE_MANIFEST",
                    "FEATURE_PACK_SKELETON_GATE_MANIFEST",
                    skeleton,
                    "COMPLETE",
                ),
                self._artifact("FP001_IDENTITY_ACCESS_JIT", "JIT_DOMAIN_DOSSIER", identity, "COMPLETE"),
                self._artifact("FP001_COMMUNICATIONS_JIT", "JIT_DOMAIN_DOSSIER", None, "NOT_STARTED"),
                self._artifact("FP001_FINAL_CONTRACT", "FINAL_FEATURE_PACK_CONTRACT", None, "NOT_STARTED"),
            ],
        }

    def _phase_7c_ready_state(self, root: Path) -> dict:
        state = self._base_state(root)
        state["phase_7c"] = "READY"
        state["communications"] = "REQUIRED / COMPLETE"
        communications_path = "working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_v0.1.0.md"
        self._write_artifact(root, communications_path)
        self._set_artifact(
            state,
            "FP001_COMMUNICATIONS_JIT",
            status="COMPLETE",
            path=communications_path,
        )
        for dossier in state["conditional_dossiers"]:
            state["conditional_dossiers"][dossier] = "NOT REQUIRED"
        return state

    @staticmethod
    def _set_artifact(
        state: dict,
        registry_id: str,
        *,
        status: str,
        path: str | None,
        formal_type: str | None = None,
    ) -> None:
        artifact = next(item for item in state["formal_artifacts"] if item["registry_id"] == registry_id)
        artifact["status"] = status
        artifact["path"] = path
        if formal_type is not None:
            artifact["formal_type"] = formal_type

    @staticmethod
    def _write_artifact(root: Path, relative: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("formal fixture artifact\n", encoding="utf-8")

    @staticmethod
    def _has_finding(report: dict, check_name: str) -> bool:
        return any(finding["check"] == check_name for finding in report["findings"])


if __name__ == "__main__":
    unittest.main()
