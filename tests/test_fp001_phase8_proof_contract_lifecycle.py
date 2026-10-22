from __future__ import annotations

import unittest
import shutil
import subprocess
import tempfile
import hashlib
from pathlib import Path

from tools.foundation_integrity_audit import (
    _fp001_phase8_proof_contract_content_issues,
    refresh_manifest,
    run_audit,
)
from tests.foundation_test_support import historical_snapshot_path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
LIFECYCLE_CHECK = "fp001_phase8_proof_contract_lifecycle"
SUCCESSOR_CHECK = "phase8_approved_status_successor_current"
CONTRACT = ROOT / "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
OPEN_WORK = ROOT / "docs/00_platform/02_OPEN_WORK_v1.2.78.md"
HISTORICAL_OPEN_WORK = historical_snapshot_path(ROOT, "02_OPEN_WORK_v1.2.77.md")


class FP001Phase8ProofContractLifecycleTests(unittest.TestCase):
    def _copy_production_fixture(self, root: Path) -> tuple[Path, Path]:
        shutil.copytree(ROOT / "docs", root / "docs")
        manifest = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        refresh_manifest(root, manifest)
        return root, manifest

    def test_contract_is_approved_without_claiming_executed_or_certified_proof(self):
        self.assertTrue(CONTRACT.is_file(), "the governed Phase 8 task contract is missing")
        text = CONTRACT.read_text(encoding="utf-8")
        for token in (
            "TB-001",
            "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
            "**Contract/design review:** COMPLETE / PASS",
            "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
            "PROOF EXECUTION: NOT STARTED",
            "PROOF RESULT: NOT STARTED",
            "PROOF CERTIFICATION: NOT STARTED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "0972864ef7f4638c96198e19a13977e0151e9726",
        ):
            self.assertIn(token, text)
        self.assertNotIn("mix fp001.proof", text)
        self.assertNotIn("lib/new_you/", text)
        self.assertNotIn("test/fp001/proof/", text)
        reviewed_candidate = ROOT / "docs/00_platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
        self.assertEqual(
            "f071d9edae90e3d5ae2030a98f79d9d1698aa68bf90ed9ce474a4f9120f82836",
            hashlib.sha256(reviewed_candidate.read_bytes()).hexdigest(),
        )

    def test_contract_preserves_the_locked_architecture_and_mandatory_proof_families(self):
        self.assertTrue(CONTRACT.is_file(), "the governed Phase 8 task contract is missing")
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertEqual([], _fp001_phase8_proof_contract_content_issues(text))
        self.assertIn(
            "Account, PMR, verification Token, required Communications MessageIntent, selected Audit EvidenceObligation and initial durable scheduling commit together or are absent together.",
            text,
        )
        self.assertIn(
            "Using security-hold release as the representative privileged effect",
            text,
        )
        self.assertIn(
            "Redis remains part of the accepted shared dev-core environment decision, but no Phase 8 application/proof component will use it absent a concrete requirement.",
            text,
        )

    def test_contract_traces_every_accepted_grill_batch_to_its_treatment(self):
        text = CONTRACT.read_text(encoding="utf-8")
        source_rows = (
            ("Q1–Q6", "e8215515-4a76-4dde-b809-ab4f17932dd9"),
            ("Q7–Q11", "e84a1ae5-8517-46c1-bb33-01d3fcc8b950"),
            ("Q12–Q16", "60fba648-e589-4e67-a6e4-4dd3818e8115"),
            ("Q17–Q21", "b24f0a08-8493-4dc3-9885-b47be44eda0d"),
            ("Q22", "cc6d56dd-344f-41ff-8b2f-64246d7f1c5b"),
            ("Q23", "446a4cc7-d1b3-4a06-a0ea-3e25d8d3149f"),
            ("Q24", "e26ca691-0980-42de-80d0-3eec3d221d67"),
            ("Q25", "b468c38e-662a-43c0-a6a5-b3abbca72499"),
            ("Q26–Q27", "4464891a-f1ad-44c2-8b80-1601e3f991b1"),
            ("Q28–Q38", "82ba53ea-b6ca-4906-a024-c6ebfb6054b3"),
            ("Q39–Q47", "ca2db611-f846-4d84-83ba-fbdfa3d8c102"),
            ("Q48–Q56", "20f6110e-582e-4498-bcac-c8cdbd54d7d8"),
            ("Q57–Q62", "7e8dc117-7ea5-4a0b-acf9-c7fc0cd2c39b"),
            ("Q63–Q70", "f75834d8-1908-4661-9b8f-be1b81fb8b0a"),
            ("Q71–Q80", "d55613cf-8026-44e3-8f90-0d7bf687231d"),
            ("Q81–Q90", "b45e180f-180a-4126-b043-3f7d555517aa"),
        )
        for question_range, comment_id in source_rows:
            self.assertIn(question_range, text)
            self.assertIn(comment_id, text)
        self.assertEqual([], _fp001_phase8_proof_contract_content_issues(text))

        weakened = text.replace("Q71–Q80", "Q71–Q79", 1)
        issues = _fp001_phase8_proof_contract_content_issues(weakened)
        self.assertTrue(
            any("Q71–Q80" in issue and "traceability" in issue for issue in issues),
            issues,
        )

    def test_content_check_rejects_a_weakened_atomicity_and_scenario_boundary(self):
        text = CONTRACT.read_text(encoding="utf-8")
        weakened = text.replace(
            "Failure to accept required E1 evidence blocks that effect.",
            "Failure to accept required E1 evidence does not block that effect.",
        ).replace(
            "| 9 | Source-authority / bypass negatives |",
            "| 9 | Optional source-authority checks |",
        ).replace(
            "without secrets, excess payload or a second business truth",
            "without secrets",
            1,
        ).replace(
            "support pressure",
            "ordinary use",
            1,
        )
        issues = _fp001_phase8_proof_contract_content_issues(weakened)
        self.assertTrue(any("approved proof-design clause" in issue and "failure to accept required e1 evidence" in issue for issue in issues))
        self.assertTrue(any("Source-authority / bypass negatives" in issue for issue in issues))
        self.assertTrue(any("Audit E2 scenario row omits approved proof detail" in issue for issue in issues))
        self.assertTrue(any("Non-enumeration / current Privacy re-read scenario row omits approved proof detail 'support pressure'" in issue for issue in issues))

    def test_content_check_requires_locked_mechanism_foundation_and_machine_evidence(self):
        text = CONTRACT.read_text(encoding="utf-8")
        required_phrases = (
            "`MessageIntent.dispatch_disposition` uses `ash_state_machine`",
            "for `open`, `held`, `reconciliation_required` and `closed`",
            "Account's orthogonal state dimensions remain outside this machine",
            "`DeliveryAttempt` admission, invocation, provider observation and reconciliation conclusion remain separate dimensions outside that machine",
            "## 7.2 Locked Phase-8 implementation foundation",
            "`PROJECT_KEY=new_you`",
            "`new_you_dev` / `new_you_dev`",
            "`new_you_test` / `new_you_test`",
            "## 7.3 Locked verification foundation",
            "`mix check.deep`",
            "machine-readable evidence suitable for CI/certification",
            "exact Git SHA",
            "relevant runtime and dependency versions",
            "PASS/FAIL for every mandatory proof family",
            "failing invariant/cut-point where applicable",
            "6. Current Open Work",
            "7. Approved FP-001 planning contracts",
            "8. This proof contract",
            "9. Proof evidence produced under it",
            "10. Implementation",
        )
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.casefold(), text.casefold())

        weakened_contracts = (
            text.replace(
                "uses `ash_state_machine`",
                "uses an implementation-selected mechanism",
                1,
            ),
            text.replace("`4220–4239`", "`4200–4219`", 1),
            text.replace("`new_you_test` / `new_you_test`", "`test_db` / `test_db`", 1),
            text.replace("UsageRules in skills-only mode", "UsageRules in unrestricted mode", 1),
            text.replace(
                "Supported framework/package installation and structural changes are Igniter-first.",
                "Supported framework/package installation and structural changes are manual-first.",
                1,
            ),
            text.replace(
                "Tidewave is mandatory DEV-only agent tooling",
                "Tidewave is mandatory development and production agent tooling",
                1,
            ),
            text.replace("HexDocs MCP is deferred initially", "HexDocs MCP is enabled initially", 1),
            text.replace("`mix check.deep`", "`mix check`", 1),
            text.replace(
                "emits concise machine-readable evidence suitable for CI/certification",
                "emits a human-readable summary suitable for CI/certification",
                1,
            ),
            text.replace("exact Git SHA", "branch name", 1),
            text.replace("relevant runtime and dependency versions", "runtime details", 1),
            text.replace("PASS/FAIL for every mandatory proof family", "overall result", 1),
            text.replace("failing invariant/cut-point where applicable", "failure note", 1),
            text.replace(
                "for `open`, `held`, `reconciliation_required` and `closed`",
                "for `open` and `closed`",
                1,
            ),
            text.replace(
                "remain separate dimensions outside that machine",
                "remain separate dimensions",
                1,
            ),
            text.replace(
                "HexDocs MCP is deferred initially and added only on demonstrated need. Ash AI dev MCP is deferred; do not add `ash_ai` solely for another MCP endpoint. Direct Sourceror is deferred unless a genuine low-level AST/source-transformation requirement appears; transitive use through Igniter is acceptable.",
                "HexDocs MCP, Ash AI dev MCP and direct Sourceror are deferred initially.",
                1,
            ),
            text.replace(
                "Credo uses a curated high-signal configuration; selected correctness/maintainability findings become blocking after a clean baseline, while subjective/noisy style remains advisory unless promoted. Sobelow begins from the Phoenix application baseline; materially applicable findings block unless explicitly reviewed or suppressed with rationale. Dialyxir/Dialyzer belongs in the slower deep gate, not the tight edit/test loop, and becomes required in PR CI after a clean approved baseline.",
                "Credo is curated. Sobelow and Dialyxir/Dialyzer run in the slower deep gate.",
                1,
            ),
            text.replace(
                "6. Current Open Work.\n7. Approved FP-001 planning contracts listed below.\n8. This proof contract.\n9. Proof evidence produced under it.\n10. Implementation.",
                "6. Approved FP-001 planning contracts listed below.\n7. Current Open Work.\n8. This proof contract.\n9. Proof evidence produced under it.\n10. Implementation.",
                1,
            ),
        )
        for index, weakened in enumerate(weakened_contracts):
            with self.subTest(weakened_contract=index):
                self.assertTrue(
                    _fp001_phase8_proof_contract_content_issues(weakened),
                    "Foundation Integrity accepted a contract with a locked decision removed",
                )

    def test_open_work_routes_to_well38_without_advancing_proof_or_phase9(self):
        self.assertTrue(OPEN_WORK.is_file(), "the Open Work status successor is missing")
        text = OPEN_WORK.read_text(encoding="utf-8")
        self.assertIn('"status_successor_version": "1.2.78"', text)
        self.assertIn('"status_successor_base_sha": "4234965c8da20dbb4ef0a7128614a5070244619a"', text)
        self.assertIn("working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md", text)
        self.assertIn("TB-001", text)
        self.assertIn("CONTRACT/DESIGN REVIEW: COMPLETE / PASS", text)
        self.assertIn("CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION", text)
        self.assertIn("PROOF EXECUTION: NOT STARTED", text)
        self.assertIn("PROOF CERTIFICATION: NOT STARTED", text)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", text)
        self.assertIn("NEXT GOVERNANCE ACTION: WELL-38 — Transition Foundation Integrity to implementation-era CI", text)
        self.assertIn("immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.19.md`", text)

    def test_current_status_summaries_route_the_approved_contract_and_status_successors(self):
        contract = CONTRACT.read_text(encoding="utf-8")
        lifecycle = contract.split("## 12. Lifecycle state", 1)[1].split("## 13.", 1)[0]
        self.assertIn("TRACER BULLET: REQUIRED / DEFINED", lifecycle)
        self.assertNotIn("DEFINED AS REVIEW CANDIDATE", lifecycle)
        self.assertIn("Open Work v1.2.78, Delivery Atlas v0.4.20, FP-001 Skeleton v0.1.22 and HARDEN-02 v0.5.22", contract)

        readme = (ROOT / "docs/00_platform/README.md").read_text(encoding="utf-8")
        active_status = next(line for line in readme.splitlines() if line.startswith("PR #76 candidate certification and completed post-merge certification evidence"))
        self.assertIn("contract/design review is COMPLETE / PASS", active_status)
        self.assertIn("CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION", active_status)
        self.assertIn("The next governance action is WELL-38", active_status)
        self.assertIn("[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.4.20.md)", readme)
        self.assertNotIn("The TB-001 proof-contract candidate is routed separately", readme)
        self.assertNotIn("TB-001 proof-contract candidate review / certification is next", readme)

        atlas = (ROOT / "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.20.md").read_text(encoding="utf-8")
        skeleton = (ROOT / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md").read_text(encoding="utf-8")
        harden = (ROOT / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.22.md").read_text(encoding="utf-8")
        self.assertIn("Planning tracker | `docs/00_platform/02_OPEN_WORK_v1.2.78.md`", atlas)
        self.assertIn("`docs/00_platform/02_OPEN_WORK_v1.2.78.md §9`", skeleton)
        self.assertIn("`02_OPEN_WORK_v1.2.78.md` | Programme routing", harden)
        self.assertIn("`working/DELIVERY_ATLAS_WORKING_v0.4.20.md` | Current derived", harden)

    def test_archived_open_work_preserves_the_review_candidate_status(self):
        self.assertTrue(HISTORICAL_OPEN_WORK.is_file(), "the historical Open Work status snapshot is missing")
        text = HISTORICAL_OPEN_WORK.read_text(encoding="utf-8")
        self.assertIn('"status_successor_version": "1.2.77"', text)
        self.assertIn("working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md", text)
        self.assertIn("PROOF EXECUTION: NOT STARTED", text)
        self.assertIn("PROOF CERTIFICATION: NOT STARTED", text)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", text)
        self.assertIn("TB-001 CONTRACT CANDIDATE REVIEW", text)

    def test_current_harden_route_uses_approved_tb001_successor_and_preserves_predecessors(self):
        atlas = (ROOT / "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.20.md").read_text(encoding="utf-8")
        skeleton = (ROOT / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md").read_text(encoding="utf-8")
        harden = (ROOT / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.22.md").read_text(encoding="utf-8")
        harden_phase7b_route = harden.split("## 23. FP-001 Phase 7B reconciliation current route", 1)[1].split("## 24.", 1)[0]
        self.assertIn("TRACER BULLET: REQUIRED / DEFINED", harden_phase7b_route)
        self.assertIn("TB-001 CONTRACT/DESIGN REVIEW: COMPLETE / PASS", harden_phase7b_route)
        self.assertIn("TB-001 CONTRACT STATUS: CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION", harden_phase7b_route)
        self.assertIn("NEXT GOVERNANCE ACTION: WELL-38", harden_phase7b_route)
        self.assertIn("Open Work v1.2.78", harden_phase7b_route)
        self.assertNotIn("CANDIDATE / REVIEW PENDING", harden_phase7b_route)

        open_work_history = OPEN_WORK.read_text(encoding="utf-8")
        self.assertIn("## 12.32 — TB-001 proof-contract v0.1.1 correction and route successor (historical predecessor)", open_work_history)
        self.assertIn("## 12.33 — TB-001 proof-contract v0.1.2 correction and route successor (historical predecessor)", open_work_history)
        self.assertIn("## 12.34 — TB-001 contract review and current-status promotion", open_work_history)
        self.assertIn("## 26.24 FP-001 Phase 8 TB-001 successor candidate route (historical predecessor)", atlas)
        self.assertIn("## v0.1.20 — TB-001 proof-contract successor candidate route (historical predecessor)", skeleton)
        self.assertIn("## v0.5.20 — FP-001 TB-001 proof-contract successor candidate route (historical predecessor)", harden)

    def test_foundation_integrity_rejects_a_stale_readme_active_successor_route(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            readme = root / "docs/00_platform/README.md"
            text = readme.read_text(encoding="utf-8")
            current = "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
            stale = "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.0.9.md"
            self.assertIn(current, text)
            readme.write_text(text.replace(current, stale, 1), encoding="utf-8")
            manifest = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            refresh_manifest(root, manifest)

            report = run_audit(root, manifest)
            check = next(item for item in report["checks"] if item["name"] == SUCCESSOR_CHECK)

            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn(
                f"README active working routing omits {current}",
                check["message"],
            )

    def test_foundation_integrity_checks_the_phase8_proof_contract_transition(self):
        report = run_audit(ROOT, MANIFEST)
        checks = {item["name"]: item for item in report["checks"]}
        self.assertIn(LIFECYCLE_CHECK, checks, "pinned predecessor certification is not preserved")
        self.assertEqual("PASS", checks[LIFECYCLE_CHECK]["status"], checks[LIFECYCLE_CHECK]["message"])
        self.assertEqual("PASS", checks[SUCCESSOR_CHECK]["status"], checks[SUCCESSOR_CHECK]["message"])

    def test_temporary_content_root_uses_canonical_git_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self._copy_production_fixture(Path(directory))
            self.assertFalse((root / ".git").exists())

            report = run_audit(root, manifest)
            checks = {item["name"]: item for item in report["checks"]}

            self.assertEqual("PASS", report["status"], report["findings"])
            self.assertEqual("PASS", checks[SUCCESSOR_CHECK]["status"], checks[SUCCESSOR_CHECK]["message"])
            self.assertEqual(
                "PASS",
                checks["phase8_approved_status_successor_predecessor_full_audit"]["status"],
                checks["phase8_approved_status_successor_predecessor_full_audit"]["message"],
            )

    def test_explicit_repository_without_git_fails_successor_provenance_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self._copy_production_fixture(Path(directory) / "content")
            repository_without_git = Path(directory) / "missing-git"
            repository_without_git.mkdir()

            report = run_audit(root, manifest, repository_root=repository_without_git)
            checks = {item["name"]: item for item in report["checks"]}

            self.assertEqual("FAIL", report["status"])
            self.assertEqual("FAIL", checks[SUCCESSOR_CHECK]["status"])
            self.assertIn("cannot locate Git repository", checks[SUCCESSOR_CHECK]["message"])
            predecessor = checks["phase8_approved_status_successor_predecessor_full_audit"]
            self.assertEqual("FAIL", predecessor["status"])
            self.assertIn("cannot locate Git repository", predecessor["message"])

    def test_git_repository_without_pinned_predecessor_fails_provenance_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self._copy_production_fixture(Path(directory) / "content")
            repository_without_predecessor = Path(directory) / "git-repository"
            repository_without_predecessor.mkdir()
            subprocess.run(
                ["git", "init", "--quiet"],
                cwd=repository_without_predecessor,
                check=True,
            )

            report = run_audit(
                root,
                manifest,
                repository_root=repository_without_predecessor,
            )
            checks = {item["name"]: item for item in report["checks"]}

            self.assertEqual("FAIL", report["status"])
            self.assertEqual("FAIL", checks[SUCCESSOR_CHECK]["status"])
            predecessor = checks["phase8_approved_status_successor_predecessor_full_audit"]
            self.assertEqual("FAIL", predecessor["status"])
            self.assertIn("pinned predecessor commit is unavailable", predecessor["message"])

    def test_corrupted_archived_predecessor_fails_even_for_temporary_content_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self._copy_production_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/02_OPEN_WORK_v1.2.77.md"
            archive.write_bytes(archive.read_bytes() + b"\nCORRUPTED HISTORICAL PREDECESSOR\n")

            report = run_audit(root, manifest)
            checks = {item["name"]: item for item in report["checks"]}

            self.assertEqual("FAIL", report["status"])
            self.assertEqual("FAIL", checks[SUCCESSOR_CHECK]["status"], checks[SUCCESSOR_CHECK]["message"])
            self.assertTrue(
                any(
                    item["check"] == "manifest_hash_parity"
                    and item["path"] == "docs/00_platform/archive/02_OPEN_WORK_v1.2.77.md"
                    for item in report["findings"]
                ),
                report["findings"],
            )



if __name__ == "__main__":
    unittest.main()
