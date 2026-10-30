from __future__ import annotations

import unittest
import shutil
import subprocess
import tempfile
import hashlib
import json
import re
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
PROVENANCE_CHECK = "phase8_status_successor_predecessor_provenance"
CONTRACT = ROOT / "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md"
OPEN_WORK = ROOT / "docs/00_platform/02_OPEN_WORK_v1.2.90.md"
PRE_AUTHORIZATION_OPEN_WORK = ROOT / "docs/00_platform/archive/02_OPEN_WORK_v1.2.83.md"
HISTORICAL_OPEN_WORK = historical_snapshot_path(ROOT, "02_OPEN_WORK_v1.2.77.md")
APPROVAL_TIME_OPEN_WORK = ROOT / "docs/00_platform/archive/02_OPEN_WORK_v1.2.78.md"
APPROVAL_TIME_ATLAS = ROOT / "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.20.md"
APPROVAL_TIME_SKELETON = ROOT / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md"
APPROVAL_TIME_HARDEN = ROOT / "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.22.md"
FROZEN_ROUTE_ARCHIVE_SHA256 = {
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.78.md": "7ab24ce13ba37306c78cd795f3bb308c75a8d6627aa5ea8780bd2b162f013770",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.79.md": "f08b6c9cd8685bb4f5df7cebf36476e4fcdd8e07eb0d2b148cb39baf95bca24a",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.20.md": "222c9f14889196cb6d35d58fedfcf47a0aec83a30b5b7a6e1bf2ab5c95273eae",
    "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md": "5bb5acde41de8cd9ccd0b356de13a25c7c4b18abc21b09d7b3caf5c22e49d6f9",
    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.22.md": "0b07d28dce1f212469fdb0863f93f6d03fe16c6a4e5e6b0c7d181d4dab58bd2f",
}


class FP001Phase8ProofContractLifecycleTests(unittest.TestCase):
    def _copy_production_fixture(self, root: Path) -> tuple[Path, Path]:
        shutil.copytree(ROOT / "docs", root / "docs")
        manifest = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        refresh_manifest(root, manifest)
        return root, manifest

    def test_immediate_archived_predecessors_keep_artifact_specific_lineage(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        expected = {
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.88.md": (
                "OPEN_WORK_V1_2_88",
                "PLANNING_TRACKER_HISTORICAL",
            ),
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.29.md": (
                "DELIVERY_ATLAS_V0_4_29",
                "DERIVED_DELIVERY_NAVIGATION_HISTORICAL",
            ),
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.29.md": (
                "FP001_SKELETON_V0_1_29",
                "DERIVED_FEATURE_PACK_NAVIGATION_HISTORICAL",
            ),
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.31.md": (
                "HARDEN_02_V0_5_31",
                "DERIVED_GOVERNANCE_CONTRACT_HISTORICAL",
            ),
        }
        actual = {
            entry["repository_path"]: (entry["document_id"], entry["authority_class"])
            for entry in manifest["historical_documents"]
            if entry.get("repository_path") in expected
        }

        self.assertEqual(expected, actual)

    def test_current_successor_resolves_manifest_routes_and_preserves_lifecycle_boundaries(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        rules = manifest["integrity_rules"]
        phase8 = rules["fp001_phase8_proof_contract_lifecycle"]
        routes = phase8["current_routes"]
        current_open_work = next(
            entry
            for entry in manifest["governing_documents"]
            if entry["document_id"] == "OPEN_WORK" and entry.get("lifecycle") != "historical"
        )
        self.assertEqual(current_open_work["repository_path"], routes["open_work"])

        promotion = rules["fp001_phase7c_final_contract_current_promotion"]
        self.assertEqual(routes, promotion["current_paths"])
        route_status = promotion["current_route_status_successor_version"].split(" / ")
        self.assertEqual(
            [Path(routes[key]).stem.rsplit("_v", 1)[1] for key in ("open_work", "delivery_atlas", "fp001_skeleton", "harden_02")],
            route_status,
        )

        route_hashes = phase8["current_route_sha256"]
        README = ROOT / "docs/00_platform/README.md"
        readme = README.read_text(encoding="utf-8")
        for relative in routes.values():
            path = ROOT / relative
            self.assertTrue(path.is_file(), f"current route is missing: {relative}")
            self.assertEqual(route_hashes[relative], hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertIn(Path(relative).name, readme)

        historical = manifest["historical_documents"]
        predecessor_hashes = phase8["predecessor_archives_sha256"]
        for label in ("open_work", "delivery_atlas", "fp001_skeleton", "harden_02"):
            current_path = ROOT / routes[label]
            metadata = "\n".join(current_path.read_text(encoding="utf-8").splitlines()[:40])
            predecessor = re.search(r"(?im)^.*predecessor.*`(archive/[^`]+\.md)`", metadata)
            self.assertIsNotNone(predecessor, f"{label} has no direct predecessor metadata")
            archive_path = f"docs/00_platform/{predecessor.group(1)}"
            archived = ROOT / archive_path
            archive_entry = next(
                (entry for entry in historical if entry.get("repository_path") == archive_path),
                None,
            )
            self.assertTrue(archived.is_file(), f"predecessor archive is missing: {archive_path}")
            digest = hashlib.sha256(archived.read_bytes()).hexdigest()
            self.assertEqual(predecessor_hashes[archive_path], digest)
            if archive_entry is not None:
                self.assertEqual(archive_entry["sha256"], digest)
                self.assertEqual(archive_entry["provenance_sha256"], digest)

        open_work = (ROOT / routes["open_work"]).read_text(encoding="utf-8")
        lifecycle = re.search(
            r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
            open_work,
            re.DOTALL,
        )
        self.assertIsNotNone(lifecycle, "current Open Work lifecycle state is missing")
        state = json.loads(lifecycle.group(1))
        self.assertEqual(current_open_work["semver"], state["status_successor_version"])
        self.assertEqual("STARTED", state["architectural_proof_execution"])
        self.assertEqual("INCOMPLETE / COVERAGE-INCOMPLETE", state["proof_result"])
        self.assertEqual("NOT CERTIFIED", state["proof_certification"])
        self.assertEqual("NOT STARTED / NOT AUTHORISED", state["phase9_vertical_slices"])
        self.assertIn("p8-05 implementation authorised", state["next_governance_action"].casefold())
        self.assertEqual("COMPLETE / MERGED VIA PR #156", state["well_48"])
        self.assertEqual("eb28943cd8353cdec6625a053e157af449587d2c", state["well_48_merge_sha"])
        self.assertEqual("BLOCKED / WAITING ON WELL-61", state["well_49"])
        self.assertEqual("BACKLOG / NOT STARTED", state["well_50"])
        self.assertIn("well-48: complete", state["next_governance_action"].casefold())
        self.assertIn("well-49: blocked", state["next_governance_action"].casefold())
        self.assertIn("well-60", state["next_governance_action"].casefold())
        self.assertIn("well-61", state["next_governance_action"].casefold())
        self.assertIn("well-50: backlog", state["next_governance_action"].casefold())
        current_authorization = open_work.split("## Current P8-05 implementation authorization", 1)[1].split("\n## ", 1)[0]
        for token in (
            "WELL-48: COMPLETE / MERGED VIA PR #156",
            "WELL-49: BLOCKED / WAITING ON WELL-61",
            "WELL-50: BACKLOG / NOT STARTED",
        ):
            self.assertIn(token, current_authorization)
        predecessor = (ROOT / "docs/00_platform/archive/02_OPEN_WORK_v1.2.84.md").read_text(encoding="utf-8")
        prior_section = predecessor.split("\n## Current P8-05 implementation authorization\n", 1)[1]
        prior_section = prior_section.split("\n## ", 1)[0].strip()
        historical_section = open_work.split(
            "\n### Historical P8-05 implementation authorization (v1.2.84 snapshot)\n",
            1,
        )[1]
        historical_section = historical_section.split("\n## ", 1)[0].strip()
        self.assertEqual(prior_section, historical_section)
        self.assertIn("p8-05 implementation authorised", state["phase8_execution_gate"].casefold())
        self.assertEqual("AUTHORISED", state["phase8"])
        self.assertEqual(
            "AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION AUTHORISED",
            state["application_implementation"],
        )

        for token in (
            "WELL-5 / P8-04",
            "PROOF EXECUTION: STARTED",
            "PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
            "PROOF CERTIFICATION: NOT CERTIFIED",
            "Phase 8 is NOT CERTIFIED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
            "WELL-48: COMPLETE / MERGED VIA PR #156",
            "WELL-49: BLOCKED / WAITING ON WELL-61",
            "WELL-50: BACKLOG / NOT STARTED",
            "NEXT EXECUTION ACTION: WELL-48: COMPLETE / MERGED VIA PR #156",
        ):
            self.assertIn(token, readme)

        for relative, expected_digest in FROZEN_ROUTE_ARCHIVE_SHA256.items():
            archive = ROOT / relative
            self.assertTrue(archive.is_file(), f"frozen route archive is missing: {relative}")
            self.assertEqual(expected_digest, hashlib.sha256(archive.read_bytes()).hexdigest())

        report = run_audit(ROOT, MANIFEST)
        checks = {item["name"]: item for item in report["checks"]}
        self.assertEqual("PASS", checks["harden_02_lifecycle_state"]["status"])
        self.assertIn(SUCCESSOR_CHECK, checks)
        self.assertEqual("PASS", checks[SUCCESSOR_CHECK]["status"], checks[SUCCESSOR_CHECK]["message"])
        self.assertEqual("PASS", checks[PROVENANCE_CHECK]["status"], checks[PROVENANCE_CHECK]["message"])
        self.assertEqual("PASS", checks["fp001_phase7c_final_contract_current_promotion"]["status"])
        self.assertEqual("PASS", checks["phase8_status_successor_phase7b_preservation"]["status"])

    def test_current_successor_rejects_mutated_historical_promotion_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["integrity_rules"]["fp001_phase7c_final_contract_current_promotion"][
                "pr126_reviewed_head_sha"
            ] = "altered-historical-head"
            manifest_path.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)
            checks = {item["name"]: item for item in report["checks"]}
            promotion = checks["fp001_phase7c_final_contract_current_promotion"]
            self.assertEqual("FAIL", promotion["status"], promotion["message"])
            self.assertIn("PR #126 promotion evidence changed", promotion["message"])

    def test_current_successor_requires_archive_pins_for_the_full_route_chain(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            promotion = manifest["integrity_rules"]["fp001_phase7c_final_contract_current_promotion"]
            del promotion["predecessor_archives_sha256"][
                "docs/00_platform/archive/02_OPEN_WORK_v1.2.81.md"
            ]
            manifest_path.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)
            checks = {item["name"]: item for item in report["checks"]}
            promotion_check = checks["fp001_phase7c_final_contract_current_promotion"]
            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("archived current-route successor chain", promotion_check["message"])

    def test_current_contract_is_approved_without_claiming_proof_certification_or_phase9(self):
        self.assertTrue(CONTRACT.is_file(), "the governed Phase 8 task contract is missing")
        text = CONTRACT.read_text(encoding="utf-8")
        for token in (
            "TB-001",
            "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
            "**Contract/design review:** COMPLETE / PASS",
            "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
            "PROOF EXECUTION: STARTED UNDER THE APPROVED v0.1.2 CONTRACT; THIS SUCCESSOR ADDS NO RUNTIME PROOF",
            "PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
            "PROOF CERTIFICATION: NOT CERTIFIED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "PR #164's exact reviewed head was `73725a3d3339bf07fdcd44b9a7ec86026db3e984`",
            "status promotion base main SHA `429677295a396b8c78e9ab6b436a57d9249eaddc`",
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
            "A valid registration or resend commits its source transition, exact Communications `MessageIntent`, required source/provenance references, and required WELL-46 protected-delivery envelope in the same authoritative PostgreSQL transaction.",
            text,
        )
        self.assertIn("No Communications Oban job is required at registration/resend acceptance.", text)
        self.assertIn("The committed eligible open MessageIntent remains durably discoverable", text)
        self.assertIn("P8-10 discovers eligible committed open MessageIntents, recovers backlog after restart", text)
        self.assertIn("DeliveryAttempt admission commits before provider I/O", text)
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

    def test_open_work_routes_to_p805_after_well5_without_certifying_tb001_or_phase9(self):
        self.assertTrue(OPEN_WORK.is_file(), "the Open Work status successor is missing")
        text = OPEN_WORK.read_text(encoding="utf-8")
        self.assertIn('"status_successor_version": "1.2.90"', text)
        self.assertIn("working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md", text)
        self.assertIn("TB-001", text)
        self.assertIn("CONTRACT/DESIGN REVIEW: COMPLETE / PASS", text)
        self.assertIn("CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION", text)
        self.assertIn("WELL-5 / P8-04 deterministic proof harness implementation is COMPLETE", text)
        self.assertIn("PROOF EXECUTION: STARTED", text)
        self.assertIn("PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE", text)
        self.assertIn("PROOF CERTIFICATION: NOT CERTIFIED", text)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", text)
        self.assertIn("P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY", text)
        self.assertIn("## 12.41 — WELL-63 completion and WELL-61 verification-message candidate evidence", text)
        self.assertIn("historical status; superseded by §12.44", text.split("## 12.41 —", 1)[1].split("\n", 1)[0])
        current_status = text.split("## 12.41 — WELL-63 completion and WELL-61 verification-message candidate evidence", 1)[1]
        self.assertIn("WELL-63 is COMPLETE", current_status)
        self.assertIn("PR #162 merged certified head", current_status)
        self.assertIn("WELL-61 is PLANNING and unblocked by WELL-63", current_status)
        self.assertIn("WELL-49 remains BLOCKED / WAITING ON WELL-60 AND WELL-61", current_status)
        self.assertIn("WELL-60 remains a separate unresolved prerequisite", current_status)
        self.assertIn("WELL-64 is COMPLETE", text.split("## 12.39 — WELL-64 completion and P8-05 boundary", 1)[1])
        self.assertIn("immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.30.md`", text)
        self.assertFalse((ROOT / "docs/00_platform/02_OPEN_WORK_v1.2.81.md").exists())
        archived_predecessor = ROOT / "docs/00_platform/archive/02_OPEN_WORK_v1.2.81.md"
        self.assertEqual(
            "ddffe1b32b42e6132ec855ad6bc6234aabff6b01b36fc60f60e1e94f16d9df56",
            hashlib.sha256(archived_predecessor.read_bytes()).hexdigest(),
        )
        prior_atlas = ROOT / "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.22.md"
        self.assertIn(
            "**Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.21.md` (direct routing predecessor",
            prior_atlas.read_text(encoding="utf-8"),
        )

    def test_approval_time_route_remains_archived_while_current_summaries_route_p805(self):
        contract = CONTRACT.read_text(encoding="utf-8")
        lifecycle = contract.split("## 12. Lifecycle state", 1)[1].split("## 13.", 1)[0]
        self.assertIn("TRACER BULLET: REQUIRED / DEFINED", lifecycle)
        self.assertNotIn("DEFINED AS REVIEW CANDIDATE", lifecycle)
        self.assertIn("Open Work v1.2.78, Delivery Atlas v0.4.20, FP-001 Skeleton v0.1.22 and HARDEN-02 v0.5.22", contract)

        for archived in (APPROVAL_TIME_OPEN_WORK, APPROVAL_TIME_ATLAS, APPROVAL_TIME_SKELETON, APPROVAL_TIME_HARDEN):
            self.assertTrue(archived.is_file(), f"approval-time archive is missing: {archived.name}")
        approval_open_work = APPROVAL_TIME_OPEN_WORK.read_text(encoding="utf-8")
        self.assertIn('"status_successor_version": "1.2.78"', approval_open_work)
        self.assertIn("PROOF EXECUTION: NOT STARTED", approval_open_work)
        self.assertIn("PROOF RESULT: NOT STARTED", approval_open_work)
        self.assertIn("PROOF CERTIFICATION: NOT STARTED", approval_open_work)
        self.assertIn("NEXT GOVERNANCE ACTION: WELL-38", approval_open_work)

        readme = (ROOT / "docs/00_platform/README.md").read_text(encoding="utf-8")
        current_state = readme.split("## Current State", 1)[1].split("## Historical status evidence", 1)[0]
        self.assertIn("NEXT EXECUTION ACTION: WELL-48: COMPLETE / MERGED VIA PR #156", current_state)
        self.assertIn("P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY", current_state)
        self.assertIn("PROOF EXECUTION: STARTED", current_state)
        self.assertIn("PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE", current_state)
        self.assertIn("PROOF CERTIFICATION: NOT CERTIFIED", current_state)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", current_state)
        self.assertNotIn("NEXT GOVERNANCE ACTION: WELL-38", current_state)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.4.26.md", readme)
        self.assertIn("archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.27.md", readme)
        self.assertIn("archive/HARDEN-02_CONTRACT_WORKING_v0.5.28.md", readme)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.4.24.md", readme)
        self.assertIn("archive/HARDEN-02_CONTRACT_WORKING_v0.5.26.md", readme)

        atlas = APPROVAL_TIME_ATLAS.read_text(encoding="utf-8")
        skeleton = APPROVAL_TIME_SKELETON.read_text(encoding="utf-8")
        harden = APPROVAL_TIME_HARDEN.read_text(encoding="utf-8")
        self.assertIn("Open Work v1.2.78, Delivery Atlas v0.4.20, FP-001 Skeleton v0.1.22 and HARDEN-02 v0.5.22", contract)
        for relative, expected_digest in FROZEN_ROUTE_ARCHIVE_SHA256.items():
            archive = ROOT / relative
            self.assertEqual(expected_digest, hashlib.sha256(archive.read_bytes()).hexdigest())

    def test_archived_open_work_preserves_the_review_candidate_status(self):
        self.assertTrue(HISTORICAL_OPEN_WORK.is_file(), "the historical Open Work status snapshot is missing")
        text = HISTORICAL_OPEN_WORK.read_text(encoding="utf-8")
        self.assertIn('"status_successor_version": "1.2.77"', text)
        self.assertIn("working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md", text)
        self.assertIn("PROOF EXECUTION: NOT STARTED", text)
        self.assertIn("PROOF CERTIFICATION: NOT STARTED", text)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", text)
        self.assertIn("TB-001 CONTRACT CANDIDATE REVIEW", text)

    def test_archived_harden_route_preserves_approved_tb001_predecessor_evidence(self):
        atlas = APPROVAL_TIME_ATLAS.read_text(encoding="utf-8")
        skeleton = APPROVAL_TIME_SKELETON.read_text(encoding="utf-8")
        harden = APPROVAL_TIME_HARDEN.read_text(encoding="utf-8")
        harden_approved_contract_route = harden.split(
            "## v0.5.22 — FP-001 TB-001 approved contract route (current)", 1
        )[1].split("\n## ", 1)[0]
        self.assertIn("TB-001 CONTRACT/DESIGN REVIEW: COMPLETE / PASS", harden_approved_contract_route)
        self.assertIn("TB-001 CONTRACT STATUS: CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION", harden_approved_contract_route)
        self.assertIn("PROOF RESULT: NOT STARTED", harden_approved_contract_route)
        self.assertIn("NEXT EXECUTION ACTION: FP-001 P8 04", harden_approved_contract_route)
        for relative, expected_digest in FROZEN_ROUTE_ARCHIVE_SHA256.items():
            archive = ROOT / relative
            self.assertEqual(expected_digest, hashlib.sha256(archive.read_bytes()).hexdigest())

        open_work_history = APPROVAL_TIME_OPEN_WORK.read_text(encoding="utf-8")
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
            current = "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md"
            stale = "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.0.9.md"
            self.assertIn(current, text)
            readme.write_text(text.replace(current, stale, 1), encoding="utf-8")
            manifest = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            refresh_manifest(root, manifest)

            report = run_audit(root, manifest)
            check = next(item for item in report["checks"] if item["name"] == SUCCESSOR_CHECK)

            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn(
                "README active working artifacts omit the approved TB-001 contract",
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
                checks[PROVENANCE_CHECK]["status"],
                checks[PROVENANCE_CHECK]["message"],
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
            predecessor = checks[PROVENANCE_CHECK]
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
            predecessor = checks[PROVENANCE_CHECK]
            self.assertEqual("FAIL", predecessor["status"])
            self.assertIn("pinned status successor base commit is unavailable", predecessor["message"])

    def test_pre_authorization_open_work_preserves_unauthorised_p8_05_state(self):
        self.assertTrue(PRE_AUTHORIZATION_OPEN_WORK.is_file())
        text = PRE_AUTHORIZATION_OPEN_WORK.read_text(encoding="utf-8")
        self.assertEqual(
            "a373a09fddc6ce945792a9d88e579331452f10045ef5b913d2da8721467ab6ad",
            hashlib.sha256(PRE_AUTHORIZATION_OPEN_WORK.read_bytes()).hexdigest(),
        )
        self.assertIn('"status_successor_version": "1.2.83"', text)
        self.assertIn(
            "AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION UNAUTHORISED",
            text,
        )
        self.assertIn("P8-05 implementation remains UNAUTHORISED", text)
        self.assertIn("WELL-48 remains Backlog / non-executable", text)

    def test_bounded_authorization_boundary_mutations_fail_foundation_integrity(self):
        mutations = (
            (
                "p8-05 unauthorised",
                "P8-05 IMPLEMENTATION AUTHORISED",
                "P8-05 IMPLEMENTATION UNAUTHORISED",
            ),
            (
                "unbounded p8-05",
                "AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
                "AUTHORISED — GENERAL IMPLEMENTATION",
            ),
            (
                "phase 8 certified",
                "PHASE 8: NOT CERTIFIED",
                "PHASE 8: CERTIFIED",
            ),
            (
                "tb-001 pass",
                "TB-001 PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
                "TB-001 PROOF RESULT: PASS / COMPLETE",
            ),
            (
                "phase 9 authorised",
                "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
                "PHASE 9 / VERTICAL SLICES: AUTHORISED / STARTED",
            ),
            (
                "well-48 regressed to incomplete",
                '"well_48": "COMPLETE / MERGED VIA PR #156"',
                '"well_48": "BACKLOG / NOT STARTED"',
            ),
            (
                "well-49 advanced while blocked",
                '"well_49": "BLOCKED / WAITING ON WELL-61"',
                '"well_49": "COMPLETE"',
            ),
            (
                "well-50 advanced from backlog",
                '"well_50": "BACKLOG / NOT STARTED"',
                '"well_50": "COMPLETE"',
            ),
            (
                "well-45 legally approved",
                "NOT LEGALLY APPROVED",
                "LEGALLY APPROVED FOR PRODUCTION RELEASE",
            ),
        )
        for name, current, replacement in mutations:
            with self.subTest(mutation=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                open_work = root / OPEN_WORK.relative_to(ROOT)
                text = open_work.read_text(encoding="utf-8")
                self.assertIn(current, text)
                open_work.write_text(text.replace(current, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)
                report = run_audit(root, manifest_path)
                check = next(
                    item for item in report["checks"] if item["name"] == SUCCESSOR_CHECK
                )
                self.assertEqual("FAIL", check["status"], check["message"])

    def test_additive_contradictions_fail_foundation_integrity(self):
        duplicate_section = (
            "\n## Current P8-05 implementation authorization\n\n"
            "P8-05 / WELL-6 IMPLEMENTATION: UNAUTHORISED — BROAD IMPLEMENTATION\n"
            "PHASE 8: CERTIFIED\n"
        )
        additive_cases = (
            (
                "duplicate current authorization section",
                lambda text: text + duplicate_section,
            ),
            (
                "additive unauthorised marker",
                lambda text: text.replace(
                    "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
                    "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY\n"
                    "P8-05 IMPLEMENTATION: UNAUTHORISED",
                    1,
                ),
            ),
            (
                "additive well-6 implementation unauthorised line",
                lambda text: text.replace(
                    "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
                    "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY\n"
                    "P8-05 / WELL-6 IMPLEMENTATION: UNAUTHORISED",
                    1,
                ),
            ),
            (
                "additive broad authorization",
                lambda text: text.replace(
                    "AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
                    "AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY\n"
                    "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — GENERAL IMPLEMENTATION",
                    1,
                ),
            ),
            (
                "additive phase 8 certified",
                lambda text: text.replace(
                    "PHASE 8: NOT CERTIFIED",
                    "PHASE 8: NOT CERTIFIED\nPHASE 8: CERTIFIED",
                    1,
                ),
            ),
            (
                "additive phase 8 certified with suffix",
                lambda text: text.replace(
                    "PHASE 8: NOT CERTIFIED",
                    "PHASE 8: NOT CERTIFIED\nPHASE 8: CERTIFIED / COMPLETE",
                    1,
                ),
            ),
            (
                "additive phase 9 authorised",
                lambda text: text.replace(
                    "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
                    "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED\n"
                    "PHASE 9 / VERTICAL SLICES: AUTHORISED / STARTED",
                    1,
                ),
            ),
            (
                "additive well-51 before seams",
                lambda text: text.replace(
                    "WELL-51 follows the required WELL-48–50 seams",
                    "WELL-51 follows the required WELL-48–50 seams\nWELL-51: AUTHORISED",
                    1,
                ),
            ),
            (
                "additive production release authorised",
                lambda text: text.replace(
                    "NOT LEGALLY APPROVED",
                    "NOT LEGALLY APPROVED\nProduction release is authorised without approved legal evidence",
                    1,
                ),
            ),
            (
                "additive development baselines legally approved",
                lambda text: text.replace(
                    "NOT LEGALLY APPROVED",
                    "NOT LEGALLY APPROVED\nDevelopment baselines are legally approved for production release",
                    1,
                ),
            ),
        )
        for name, mutate in additive_cases:
            with self.subTest(contradiction=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                open_work = root / OPEN_WORK.relative_to(ROOT)
                text = open_work.read_text(encoding="utf-8")
                open_work.write_text(mutate(text), encoding="utf-8")
                refresh_manifest(root, manifest_path)
                report = run_audit(root, manifest_path)
                check = next(
                    item for item in report["checks"] if item["name"] == SUCCESSOR_CHECK
                )
                self.assertEqual("FAIL", check["status"], check["message"])

    def test_pre_authorization_archive_mutation_fails_foundation_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            archive = root / PRE_AUTHORIZATION_OPEN_WORK.relative_to(ROOT)
            archive.write_bytes(archive.read_bytes() + b"\n# mutated historical evidence\n")
            report = run_audit(root, manifest_path)
            check = next(item for item in report["checks"] if item["name"] == SUCCESSOR_CHECK)
            self.assertEqual("FAIL", check["status"], check["message"])

    def test_corrupted_archived_predecessor_fails_even_for_temporary_content_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self._copy_production_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/02_OPEN_WORK_v1.2.79.md"
            archive.write_bytes(archive.read_bytes() + b"\nCORRUPTED HISTORICAL PREDECESSOR\n")

            report = run_audit(root, manifest)
            checks = {item["name"]: item for item in report["checks"]}

            self.assertEqual("FAIL", report["status"])
            self.assertEqual("FAIL", checks[SUCCESSOR_CHECK]["status"], checks[SUCCESSOR_CHECK]["message"])
            self.assertIn("predecessor archive differs from exact base bytes", checks[SUCCESSOR_CHECK]["message"])



if __name__ == "__main__":
    unittest.main()
