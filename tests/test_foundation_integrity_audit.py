from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.foundation_integrity_audit import (
    _fp001_pinned_historical_proof_contract_archives,
    _h02_lifecycle_state,
    _markdown_h2_section,
    refresh_manifest,
    run_audit,
    sha256_file,
)
from foundation_test_support import (
    WELL38_BASE_SHA,
    copy_git_snapshot_tree,
    current_document_path,
    current_document_relative_path,
    current_working_path,
    current_working_relative_path,
    historical_snapshot_path,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def _current_open_work_path(root: Path) -> Path:
    return current_document_path(root, "OPEN_WORK")


def _current_open_work_relative_path(root: Path) -> str:
    return current_document_relative_path(root, "OPEN_WORK")


def _current_working_path(root: Path, prefix: str) -> Path:
    return current_working_path(root, prefix)


def _current_working_relative_path(root: Path, prefix: str) -> str:
    return current_working_relative_path(root, prefix)


def _current_working_route(root: Path, prefix: str) -> str:
    return Path(_current_working_relative_path(root, prefix)).relative_to(
        "docs/00_platform"
    ).as_posix()


def _current_open_work_route(root: Path) -> str:
    return Path(_current_open_work_relative_path(root)).relative_to(
        "docs/00_platform"
    ).as_posix()


def _sync_integrity_route_pin(root: Path, manifest_path: Path, relative: str) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    digest = sha256_file(root / relative)
    for rule_name, rule in manifest.get("integrity_rules", {}).items():
        if not isinstance(rule, dict):
            continue
        for key in ("current_route_sha256", "protected_current_artifacts_sha256"):
            pins = rule.get(key)
            if rule_name != "fp001_phase8_proof_contract_lifecycle" and isinstance(pins, dict) and relative in pins:
                pins[relative] = digest
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


SMALL_COUNTS = {
    "decisions": 1,
    "open_questions": 1,
    "architecture_law": 1,
    "architecture_requirements": 1,
    "reference_flows": 1,
    "domains": 1,
    "ownership_rows": 1,
    "feature_packs": 0,
}

FAD72C1_FROZEN_HASHES = {
    "docs/00_platform/archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/archive/00_PLATFORM_v1.2.1.md": "56a2b9a5db42a81e287f0c61deae37d6bbce5b19f48f67732584160b455f935a",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.0.0.md": "87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md": "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "cdf09ecced658635572a20e4f2feb04120b4f856e81762ef5af9ba179a11c40e",
    "docs/00_platform/archive/ARCHITECTURE_LAW_WORKING_v0.35.0.md": "a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639",
    "docs/00_platform/archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20",
}

IDENTITY_LIFECYCLE_START = "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_START -->"
IDENTITY_LIFECYCLE_END = "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_END -->"
IDENTITY_LIFECYCLE_STATE = {
    "artifact_version": "v0.1.4",
    "identity_lifecycle": "CERTIFIED / CURRENT",
    "pr_76_candidate_certification": "COMPLETE",
    "pr_76_post_merge_certification_evidence": "COMPLETE",
    "current_status_promotion": "PR #77 STATUS SUCCESSOR",
    "communications": "REQUIRED / NEXT / NOT_STARTED",
    "communications_finalisation": "BLOCKED / STOP",
    "phase_7c": "BLOCKED / NOT_STARTED",
    "proof_classification": "NOT FINALISED",
    "phase_8_application_implementation": "UNAUTHORISED",
}


class FoundationIntegrityAuditTests(unittest.TestCase):
    def test_markdown_h2_section_keeps_h3_h4_and_stops_at_next_peer_h2(self):
        text = """## Current State

Phase 7C is NEXT / NOT_STARTED.

### Current details

#### Nested current details

Phase 7C remains BLOCKED / NOT_STARTED.

## Archive

At that predecessor state, Phase 7C was BLOCKED / NOT_STARTED.
"""

        current_state = _markdown_h2_section(text, "Current State")

        self.assertIsNotNone(current_state)
        self.assertIn("### Current details", current_state)
        self.assertIn("#### Nested current details", current_state)
        self.assertIn("Phase 7C remains BLOCKED / NOT_STARTED.", current_state)
        self.assertNotIn("## Archive", current_state)
        self.assertNotIn("At that predecessor state", current_state)

    def _ensure_identity_lifecycle_block(self, dossier_path: Path) -> str:
        dossier = dossier_path.read_text(encoding="utf-8")
        if IDENTITY_LIFECYCLE_START in dossier or IDENTITY_LIFECYCLE_END in dossier:
            return dossier
        status_start = dossier.index("**Status:**")
        status_end = dossier.index("\n", status_start)
        block = (
            f"{IDENTITY_LIFECYCLE_START}\n"
            "This structured block is the machine-authoritative lifecycle projection for this artifact. "
            "Historical narrative and explanatory prose do not independently redefine current lifecycle state.\n"
            "```json\n"
            f"{json.dumps(IDENTITY_LIFECYCLE_STATE, indent=2)}\n"
            "```\n"
            f"{IDENTITY_LIFECYCLE_END}\n"
        )
        return dossier[: status_end + 1] + "\n" + block + dossier[status_end + 1 :]

    def _rewrite_identity_lifecycle_payload(self, dossier: str, mutate) -> str:
        start = dossier.index(IDENTITY_LIFECYCLE_START)
        payload_start = dossier.index("```json\n", start) + len("```json\n")
        payload_end = dossier.index("\n```", payload_start)
        payload = json.loads(dossier[payload_start:payload_end])
        mutate(payload)
        return dossier[:payload_start] + json.dumps(payload, indent=2) + dossier[payload_end:]

    def test_clean_fixture_returns_pass_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertEqual([], report["findings"])

    def test_pending_post_merge_lifecycle_state_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            open_work_entry = next(
                entry for entry in manifest["governing_documents"]
                if entry["document_id"] == "OPEN_WORK"
            )
            open_work_path = root / open_work_entry["repository_path"]
            open_work = open_work_path.read_text(encoding="utf-8")
            replacements = (
                (
                    "| POST_MERGE_INDEPENDENT_REVIEW | PASS |",
                    "| POST_MERGE_INDEPENDENT_REVIEW | PENDING |",
                ),
                (
                    "| POST_MERGE_ATTESTATION | COMPLETE |",
                    "| POST_MERGE_ATTESTATION | PENDING |",
                ),
                (
                    "| EXECUTION | COMPLETE_CERTIFIED |",
                    "| EXECUTION | IN_PROGRESS_NOT_COMPLETE_CERTIFICATION_PENDING |",
                ),
            )
            for current, stale in replacements:
                self.assertEqual(1, open_work.count(current), current)
                open_work = open_work.replace(current, stale)
            open_work_path.write_text(open_work, encoding="utf-8")

            readme_path = fixture_docs / "README.md"
            readme = readme_path.read_text(encoding="utf-8")
            for current, stale in (
                (
                    "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
                    "AUDIT & EVIDENCE DOSSIER: REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
                ),
            ):
                self.assertEqual(1, readme.count(current), current)
                readme = readme.replace(current, stale)
            readme_path.write_text(readme, encoding="utf-8")

            refresh_manifest(root, manifest_path)
            report = run_audit(root, manifest_path)
            lifecycle_check = next(
                check for check in report["checks"]
                if check["name"] == "harden_02_lifecycle_state"
            )

            self.assertEqual("FAIL", lifecycle_check["status"])

    def test_fp001_pmr_certified_successors_pass_production_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))

            report = run_audit(root, manifest_path)

            check = next(
                check for check in report["checks"] if check["name"] == "fp001_pmr_reconciliation"
            )
            self.assertEqual("PASS", check["status"], check["message"])

    def test_fp001_audit_status_successor_requires_current_lifecycle_header(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            candidate = root / (
                "docs/00_platform/working/"
                "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            )

            report = run_audit(root, manifest_path)
            check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )
            self.assertEqual("PASS", check["status"], check["message"])

            candidate_text = candidate.read_text(encoding="utf-8")
            candidate.write_text(
                candidate_text.replace(
                    "**Status:** `CERTIFIED / CURRENT`",
                    "**Status:** `NOT CERTIFIED / NOT CURRENT`",
                    1,
                ),
                encoding="utf-8",
            )
            report = run_audit(root, manifest_path)
            check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("FAIL", check["status"])
            self.assertIn("FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", check["message"])

    def test_fp001_audit_current_promotion_rejects_misattributed_successor_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            docs = root / "docs/00_platform"

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            graph_rules = manifest["integrity_rules"]["graph_rules"]
            guard_note = graph_rules["stale_predecessor_current_path_guard_note"]
            self.assertIn("The separate PR #119 Audit v0.1.0 current-status promotion", guard_note)
            graph_rules["stale_predecessor_current_path_guard_note"] = guard_note.replace(
                "The separate PR #119 Audit v0.1.0 current-status promotion",
                "The separate PR #118 Audit v0.1.0 current-status promotion",
                1,
            )
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

            skeleton_path = docs / _current_working_route(root, "FP-001_FEATURE_PACK_SKELETON_WORKING_")
            skeleton = skeleton_path.read_text(encoding="utf-8")
            current_audit_route = "working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            self.assertIn(current_audit_route, skeleton)
            skeleton = skeleton.replace(
                current_audit_route,
                "archive/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
                1,
            )
            skeleton_path.write_text(skeleton, encoding="utf-8")

            atlas_path = docs / _current_working_route(root, "DELIVERY_ATLAS_WORKING_")
            atlas = atlas_path.read_text(encoding="utf-8")
            history_start = atlas.index("## v0.4.6 Patch Scope (historical predecessor record)")
            history_end = atlas.index("## v0.4.4 Patch Scope", history_start)
            history = atlas[history_start:history_end].replace("Open Work v1.2.64", "Open Work v1.2.65", 1)
            atlas_path.write_text(atlas[:history_start] + history + atlas[history_end:], encoding="utf-8")

            harden_path = docs / _current_working_route(root, "HARDEN-02_CONTRACT_WORKING_")
            harden = harden_path.read_text(encoding="utf-8")
            harden_path.write_text(
                harden.replace(
                    "v0.5.8 routing-successor base main SHA:** `5f5a994e48d9458aaa6397044b3af4d72c5d5e81`",
                    "v0.5.9 routing-successor base main SHA:** `3566f1353ef34af58773aa13c6f5bd61d2613d96`",
                    1,
                ),
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_phase8_proof_contract_lifecycle"
            )

            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn("manifest Phase 8 route hash differs", check["message"])

    def test_fp001_audit_rejects_unexpected_additional_active_dossier_candidates(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            unexpected = root / (
                "docs/00_platform/working/"
                "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md"
            )
            unexpected.write_text("unexpected second Audit candidate\n", encoding="utf-8")

            report = run_audit(root, manifest_path)
            check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("FAIL", check["status"])
            self.assertIn("only the current FP-001 Audit dossier v0.1.0 status successor", check["message"])

    def test_fp001_identity_v013_archives_and_durable_delivery_section_are_preserved(self):
        tick = chr(96)
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        active = source_docs / "archive/identity_promotions/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
        current = source_docs / "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
        old_active = source_docs / "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
        predecessor = source_docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md"
        candidate = source_docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
        snapshot = source_docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
        stale_candidate = source_docs / "working/candidates/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"

        self.assertTrue(active.is_file(), "promoted/current v0.1.4 must remain as an archive-qualified snapshot")
        self.assertTrue(current.is_file(), "v0.2.0 must be the active Identity dossier after the current-status promotion")
        self.assertFalse(old_active.exists(), "the superseded v0.1.3 file must no longer be an active route")
        self.assertTrue(predecessor.is_file(), "v0.1.2 must be preserved in the archive")
        self.assertTrue(candidate.is_file(), "the exact PR #70 candidate must be preserved in the archive")
        self.assertTrue(snapshot.is_file(), "the promoted/current v0.1.3 snapshot must be separately preserved")
        self.assertFalse(stale_candidate.exists(), "the promoted candidate path must be retired")
        self.assertEqual(
            "28dfe34dce0e9c48c737f666b112aeb89ccf45c0dfa10d2cfb81877def2538db",
            hashlib.sha256(predecessor.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            "52fe67fcf6335bc0f2675c772a15a5ccdf75150f2ac4d92c98d61a9c48369285",
            hashlib.sha256(candidate.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            "a88f993d92ea9ff0dc5652c284ccf4e2c17f4bb16b31759fb3417044d7f8e254",
            hashlib.sha256(snapshot.read_bytes()).hexdigest(),
        )
        self.assertNotEqual(candidate.read_bytes(), snapshot.read_bytes())
        active_text = active.read_text(encoding="utf-8")
        candidate_text = candidate.read_text(encoding="utf-8")
        snapshot_text = snapshot.read_text(encoding="utf-8")
        self.assertIn("**Status:** " + tick + "CERTIFIED / CURRENT" + tick, active_text)
        self.assertIn("**Status:** " + tick + "CERTIFIED / CURRENT" + tick, current.read_text(encoding="utf-8"))
        section = "### J.1 Narrow Identity/Communications durable-delivery correction"
        next_heading = "### J.1a Automated retrieval / scanner-safe proof consumption"
        end_heading = "### J.2 Technical evidence and certification boundary"
        active_j1 = active_text.split(section, 1)[1].split(next_heading, 1)[0]
        candidate_j1 = candidate_text.split(section, 1)[1].split(end_heading, 1)[0]
        snapshot_j1 = snapshot_text.split(section, 1)[1].split(end_heading, 1)[0]
        self.assertEqual(candidate_j1, snapshot_j1, "v0.1.3 candidate and promoted snapshot must retain distinct files but same J.1")
        self.assertEqual(candidate_j1, active_j1, "the promoted/current v0.1.4 snapshot must preserve the certified J.1 section byte-for-byte")

    def test_fp001_identity_v014_promotion_is_current_and_pins_distinct_same_version_archives(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("PASS", promotion_check["status"], promotion_check["message"])

            docs = root / "docs/00_platform"
            active = docs / "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            pr70_candidate = docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            superseded_v013_current = docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
            pr76_candidate = docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            stale_candidate = docs / "working/candidates/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"

            self.assertTrue(active.is_file())
            self.assertFalse(stale_candidate.exists())
            self.assertEqual("CERTIFIED / CURRENT", active.read_text(encoding="utf-8").split("**Status:** `", 1)[1].split("`", 1)[0])
            self.assertEqual(
                "52fe67fcf6335bc0f2675c772a15a5ccdf75150f2ac4d92c98d61a9c48369285",
                hashlib.sha256(pr70_candidate.read_bytes()).hexdigest(),
            )
            self.assertEqual(
                "a88f993d92ea9ff0dc5652c284ccf4e2c17f4bb16b31759fb3417044d7f8e254",
                hashlib.sha256(superseded_v013_current.read_bytes()).hexdigest(),
            )
            self.assertEqual(
                "1557a4bded20b94fc363d96dd5a601213de105e0daccfa1970b869a0e38f362f",
                hashlib.sha256(pr76_candidate.read_bytes()).hexdigest(),
            )
            self.assertNotEqual(pr70_candidate.read_bytes(), superseded_v013_current.read_bytes())

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            pinned_archives = manifest["integrity_rules"]["identity_v014_promotion_archives"]
            self.assertEqual(
                {
                    "docs/00_platform/archive/02_OPEN_WORK_v1.2.56.md",
                    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.3.8.md",
                    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.0.md",
                    "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md",
                    "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
                },
                set(pinned_archives),
            )

    def test_fp001_identity_v014_structured_lifecycle_rejects_invalid_state_and_mirrors(self):
        def remove_block(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start) + len(IDENTITY_LIFECYCLE_END)
            return dossier[:start] + dossier[end:]

        def duplicate_block(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start) + len(IDENTITY_LIFECYCLE_END)
            block = dossier[start:end]
            history = dossier.index("### Inherited v0.1.3 certification evidence")
            return dossier[:history] + block + "\n\n" + dossier[history:]

        def malformed_marker(dossier: str) -> str:
            return dossier.replace(IDENTITY_LIFECYCLE_START, "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_BEGIN -->", 1)

        def relocate_block(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start) + len(IDENTITY_LIFECYCLE_END)
            block = dossier[start:end]
            remaining = dossier[:start] + dossier[end:]
            history = remaining.index("### Inherited v0.1.3 certification evidence")
            return remaining.replace(
                "### Inherited v0.1.3 certification evidence",
                "### Inherited v0.1.3 certification evidence\n\n" + block,
                1,
            )

        def reverse_markers(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start)
            return (
                dossier[:start]
                + dossier[end : end + len(IDENTITY_LIFECYCLE_END)]
                + dossier[start + len(IDENTITY_LIFECYCLE_START) : end]
                + IDENTITY_LIFECYCLE_START
                + dossier[end + len(IDENTITY_LIFECYCLE_END) :]
            )

        def malformed_payload(dossier: str) -> str:
            return self._rewrite_identity_lifecycle_payload(dossier, lambda _payload: None).replace(
                '"artifact_version": "v0.1.4"',
                '"artifact_version": v0.1.4',
                1,
            )

        def duplicate_json_key(dossier: str) -> str:
            return dossier.replace(
                '"artifact_version": "v0.1.4",',
                '"artifact_version": "v0.1.4",\n  "artifact_version": "v0.1.4",',
                1,
            )

        def missing_field(dossier: str) -> str:
            return self._rewrite_identity_lifecycle_payload(
                dossier, lambda payload: payload.pop("communications_finalisation")
            )

        def wrong_payload(field: str, value: str):
            return lambda dossier: self._rewrite_identity_lifecycle_payload(
                dossier, lambda payload: payload.update({field: value})
            )

        def wrong_header_status(dossier: str) -> str:
            return dossier.replace(
                "**Status:** `CERTIFIED / CURRENT`",
                "**Status:** `NOT CURRENT`.",
                1,
            )

        def wrong_phase7c_mirror(dossier: str) -> str:
            return dossier.replace(
                "Identity v0.1.4 is `CERTIFIED / CURRENT`",
                "Identity v0.1.4 is `NOT CURRENT`",
                1,
            )

        def wrong_header_provenance(dossier: str) -> str:
            status_start = dossier.index("**Status:**")
            status_end = dossier.index("\n", status_start)
            status_line = dossier[status_start:status_end]
            if "current-status promotion is `PR #77 STATUS SUCCESSOR`" in status_line:
                changed = status_line.replace(
                    "PR #77 STATUS SUCCESSOR", "PR #76 CERTIFICATION/PROMOTION", 1
                )
            else:
                changed = status_line.replace(
                    "PR #76 certified and merged this v0.1.4 dossier unchanged.",
                    "PR #76 certified and merged this v0.1.4 dossier unchanged and made it current.",
                    1,
                )
            return dossier[:status_start] + changed + dossier[status_end:]

        def pr76_claims_phase7c_promotion(dossier: str) -> str:
            current_promotion = "* Current-status promotion is recorded by `PR #77 STATUS SUCCESSOR`."
            if current_promotion in dossier:
                return dossier.replace(
                    current_promotion,
                    "* Current-status promotion is recorded by `PR #76`;",
                    1,
                )
            communications = "* Communications remains `REQUIRED / NEXT / NOT_STARTED`;"
            self.assertEqual(1, dossier.count(communications))
            return dossier.replace(
                communications,
                "* Current-status promotion is recorded by `PR #76`;\n" + communications,
                1,
            )

        def remove_state_field(field: str):
            return lambda dossier: self._rewrite_identity_lifecycle_payload(
                dossier, lambda payload: payload.pop(field, None)
            )

        mutations = (
            ("missing block", remove_block),
            ("duplicate block", duplicate_block),
            ("malformed marker", malformed_marker),
            ("block outside current-state region", relocate_block),
            ("out-of-order markers", reverse_markers),
            ("malformed JSON", malformed_payload),
            ("duplicate JSON key", duplicate_json_key),
            ("missing required field", missing_field),
            ("wrong Identity lifecycle", wrong_payload("identity_lifecycle", "NOT CURRENT")),
            ("wrong dossier version", wrong_payload("artifact_version", "v0.1.3")),
            ("Communications advanced", wrong_payload("communications", "COMPLETE / FINALISED")),
            ("Phase 7C advanced", wrong_payload("phase_7c", "READY / STARTED")),
            ("proof classification finalised", wrong_payload("proof_classification", "FINALISED")),
            ("unexpected canonical JSON field", wrong_payload("unexpected_state", "UNEXPECTED")),
            (
                "PR #76 cannot collapse certification and promotion",
                wrong_payload("pr_76_certification_promotion", "COMPLETE"),
            ),
            ("PR #76 candidate certification missing", remove_state_field("pr_76_candidate_certification")),
            (
                "PR #76 candidate certification wrong",
                wrong_payload("pr_76_candidate_certification", "PENDING"),
            ),
            (
                "PR #76 post-merge certification evidence missing",
                remove_state_field("pr_76_post_merge_certification_evidence"),
            ),
            (
                "PR #76 post-merge certification evidence wrong",
                wrong_payload("pr_76_post_merge_certification_evidence", "PENDING"),
            ),
            (
                "current-status promotion source missing",
                remove_state_field("current_status_promotion"),
            ),
            (
                "current-status promotion source wrong",
                wrong_payload("current_status_promotion", "PR #76"),
            ),
            (
                "Phase 8 authorised",
                wrong_payload("phase_8_application_implementation", "AUTHORISED"),
            ),
            ("header Status conflicts", wrong_header_status),
            ("BLOCKS_PHASE7C mirror conflicts", wrong_phase7c_mirror),
            ("header Status provenance conflicts", wrong_header_provenance),
            ("BLOCKS_PHASE7C attributes promotion to PR #76", pr76_claims_phase7c_promotion),
        )
        for name, mutate in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                dossier_path = root / "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                dossier = self._ensure_identity_lifecycle_block(dossier_path)
                dossier_path.write_text(mutate(dossier), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("Identity current lifecycle", promotion_check["message"])

    def test_fp001_identity_v014_current_dossier_bytes_remain_pinned(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            dossier_path = root / "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            dossier = self._ensure_identity_lifecycle_block(dossier_path)
            historical_heading = "### Inherited v0.1.3 certification evidence\n"
            historical_claim = (
                "Historical PR #76 evidence: the exact v0.1.4 candidate was not current and its "
                "certification was pending before promotion.\n\n"
            )
            self.assertEqual(1, dossier.count(historical_heading))
            dossier_path.write_text(
                dossier.replace(historical_heading, historical_heading + "\n" + historical_claim, 1),
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("certified Identity & Access dossier changed from its Phase 7B baseline", promotion_check["message"])

    def test_fp001_identity_v014_open_work_separates_pr76_certification_from_pr77_promotion(self):
        canonical_provenance = (
            "PR #76 certified the v0.1.4 candidate and supplied completed post-merge certification evidence. "
            "It did not make v0.1.4 current. This separate PR #77 status successor records the current-status "
            "promotion; the resulting Identity state is CERTIFIED / CURRENT."
        )
        collapsed_provenance = "PR #76 certification/promotion is COMPLETE / CERTIFIED / CURRENT."
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            open_work_path = _current_open_work_path(root)
            open_work = open_work_path.read_text(encoding="utf-8")
            section_start = open_work.index("## 12.14 —")
            section_end = open_work.find("\n## ", section_start + 1)
            if section_end < 0:
                section_end = len(open_work)
            section = open_work[section_start:section_end]
            if canonical_provenance in section:
                section = section.replace(canonical_provenance, collapsed_provenance, 1)
                open_work = open_work[:section_start] + section + open_work[section_end:]
            else:
                open_work = open_work[:section_end] + "\n\n" + collapsed_provenance + open_work[section_end:]
            open_work_path.write_text(open_work, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_phase8_proof_contract_lifecycle"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("manifest Phase 8 route hash differs", promotion_check["message"])

    def test_fp001_identity_v014_lifecycle_evidence_boundaries_fail_closed(self):
        mutations = (
            ("missing evidence boundary", "### Inherited v0.1.3 certification evidence\n", ""),
            (
                "duplicate evidence boundary",
                "## A. Baseline and scope\n",
                "### Inherited v0.1.3 certification evidence\n\n## A. Baseline and scope\n",
            ),
            (
                "malformed evidence boundary",
                "## A. Baseline and scope\n",
                "### A. Baseline and scope\n",
            ),
        )
        for name, anchor, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                dossier_path = root / "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                dossier = self._ensure_identity_lifecycle_block(dossier_path)
                self.assertIn(anchor, dossier)
                dossier_path.write_text(dossier.replace(anchor, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("active Identity lifecycle evidence boundaries", promotion_check["message"])

    def test_fp001_pmr_validates_atlas_artifact_lineage_independently_of_open_work(self):
        mutations = (
            (
                "wrong direct predecessor",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.18.md`",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`",
            ),
            (
                "wrong semver transition",
                "- **SemVer transition:** `v0.4.18 → v0.4.19`",
                "- **SemVer transition:** `v0.4.2 → v0.4.3`",
            ),
            (
                "missing predecessor metadata",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.18.md` (direct routing predecessor; preserved byte-identically). Earlier predecessors remain at their archive paths.\n",
                "",
            ),
            (
                "duplicate predecessor metadata",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.18.md` (direct routing predecessor; preserved byte-identically). Earlier predecessors remain at their archive paths.\n"
                "- **SemVer transition:** `v0.4.18 → v0.4.19`",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.18.md` (direct routing predecessor; preserved byte-identically). Earlier predecessors remain at their archive paths.\n"
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.18.md` (duplicate)\n"
                "- **SemVer transition:** `v0.4.18 → v0.4.19`",
            ),
        )
        for name, anchor, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                atlas_path = historical_snapshot_path(root, "DELIVERY_ATLAS_WORKING_v0.4.19.md")
                is_archived = "archive" in atlas_path.parts
                original_open_work = _current_open_work_path(root).read_bytes()
                atlas = atlas_path.read_text(encoding="utf-8")
                self.assertIn(anchor, atlas)
                atlas_path.write_text(atlas.replace(anchor, replacement, 1), encoding="utf-8")
                self.assertEqual(original_open_work, _current_open_work_path(root).read_bytes())
                if not is_archived:
                    refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                if is_archived:
                    self.assertTrue(
                        any(
                            finding["check"] == "manifest_hash_parity"
                            and finding.get("path") == atlas_path.relative_to(root).as_posix()
                            for finding in report["findings"]
                        ),
                        report["findings"],
                    )
                else:
                    promotion_check = next(
                        check for check in report["checks"]
                        if check["name"] == "fp001_phase8_proof_contract_lifecycle"
                    )
                    self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                    self.assertIn("manifest Phase 8 route hash differs", promotion_check["message"])

    def test_fp001_pmr_rejects_atlas_metadata_declarations_outside_header(self):
        mutations = (
            (
                "later predecessor declaration",
                "\n- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md` (contradictory later declaration)\n",
            ),
            (
                "later transition declaration",
                "\n- **SemVer transition:** `v0.3.8 → v0.4.0` (contradictory later declaration)\n",
            ),
        )
        for name, declaration in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                atlas_path = historical_snapshot_path(root, "DELIVERY_ATLAS_WORKING_v0.4.19.md")
                is_archived = "archive" in atlas_path.parts
                atlas = atlas_path.read_text(encoding="utf-8")
                header = atlas.split("## v0.4.10 Patch Scope", 1)[0]
                self.assertIn("- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.18.md`", header)
                self.assertIn("- **SemVer transition:** `v0.4.18 → v0.4.19`", header)
                atlas_path.write_text(atlas + declaration, encoding="utf-8")
                if not is_archived:
                    refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                if is_archived:
                    self.assertTrue(
                        any(
                            finding["check"] == "manifest_hash_parity"
                            and finding.get("path") == atlas_path.relative_to(root).as_posix()
                            for finding in report["findings"]
                        ),
                        report["findings"],
                    )
                else:
                    promotion_check = next(
                        check for check in report["checks"]
                        if check["name"] == "fp001_phase8_proof_contract_lifecycle"
                    )
                    self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                    self.assertIn("manifest Phase 8 route hash differs", promotion_check["message"])

    def test_fp001_phase8_rejects_unreviewed_current_route_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            atlas_path = _current_working_path(root, "DELIVERY_ATLAS_WORKING_")
            atlas_path.write_text(
                atlas_path.read_text(encoding="utf-8")
                + "\nHistorical prose: Atlas v0.3.8 preceded the direct v0.3.9 predecessor, and the current transition is v0.3.9 to v0.4.0.\n",
                encoding="utf-8",
            )
            harden_path = _current_working_path(root, "HARDEN-02_CONTRACT_WORKING_")
            harden_path.write_text(
                harden_path.read_text(encoding="utf-8")
                + "\nHistorical prose: v0.4.9 came before the current v0.5.0 predecessor; the certified semantics originate in v0.4.0.\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "phase8_approved_status_successor_current"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("Phase 8 current-route SHA-256 differs", promotion_check["message"])

    def test_fp001_pmr_validates_harden_v0520_successor_metadata(self):
        predecessor = "- **Immediate predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.20.md` (preserved byte-identically)\n"
        mutations = (
            (
                "multiple current predecessors",
                predecessor,
                predecessor + "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.1.md`\n",
            ),
            (
                "stale v0.5.15 current predecessor",
                predecessor,
                predecessor + "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.15.md` (direct predecessor; preserved byte-identically).\n",
            ),
            (
                "wrong current predecessor",
                predecessor,
                "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.1.md` — wrong direct predecessor\n",
            ),
            (
                "wrong certified successor version",
                "this v0.5.19 successor preserves them and records current routing",
                "this v0.5.5 successor preserves them and records current routing",
            ),
            (
                "missing successor base SHA",
                "- **v0.5.21 routing successor base main SHA:** `0972864ef7f4638c96198e19a13977e0151e9726`\n",
                "",
            ),
            (
                "incorrect successor base SHA",
                "- **v0.5.21 routing successor base main SHA:** `0972864ef7f4638c96198e19a13977e0151e9726`",
                "- **v0.5.18 status successor base main SHA:** `0000000000000000000000000000000000000000`",
            ),
        )
        for name, anchor, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                harden_path = historical_snapshot_path(root, "HARDEN-02_CONTRACT_WORKING_v0.5.21.md")
                is_archived = "archive" in harden_path.parts
                harden = harden_path.read_text(encoding="utf-8")
                self.assertIn(anchor, harden)
                harden_path.write_text(harden.replace(anchor, replacement, 1), encoding="utf-8")
                if not is_archived:
                    refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                if is_archived:
                    self.assertTrue(
                        any(
                            finding["check"] == "manifest_hash_parity"
                            and finding.get("path") == harden_path.relative_to(root).as_posix()
                            for finding in report["findings"]
                        ),
                        report["findings"],
                    )
                else:
                    promotion_check = next(
                        check for check in report["checks"]
                        if check["name"] == "fp001_phase8_proof_contract_lifecycle"
                    )
                    self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                    self.assertIn("manifest Phase 8 route hash differs", promotion_check["message"])

    def test_fp001_pmr_rejects_unqualified_current_harden_section_20_stop(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            harden_path = _current_working_path(root, "HARDEN-02_CONTRACT_WORKING_")
            harden = harden_path.read_text(encoding="utf-8")
            current_open_work_name = _current_open_work_path(root).name
            current_open_work_version = re.search(r"v(\d+\.\d+\.\d+)", current_open_work_name).group(1)
            current_statement = (
                "No application implementation is authorised by HARDEN-02 itself. "
                f"Current Open Work v{current_open_work_version} separately records application implementation as AUTHORISED only inside "
                "the bounded Phase 8 / NEW_TRACER_BULLET architectural-proof stage."
            )
            self.assertIn(current_statement, harden)
            harden_path.write_text(
                harden.replace(current_statement, "No application implementation is authorised.", 1),
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "phase8_approved_status_successor_current"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("Phase 8 current-route SHA-256 differs", promotion_check["message"])

    def test_fp001_pmr_rejects_harden_metadata_declarations_outside_header(self):
        declarations = (
            ("Plan / contract version", "v0.5.0"),
            ("Current predecessor", "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md`"),
            ("Earlier historical status predecessor", "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md`"),
            (
                "Certified contract semantics",
                "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md` — this v0.4.9 successor changes status",
            ),
            ("v0.5.0 status-successor base main SHA", "`0000000000000000000000000000000000000000`"),
            ("v0.5.18 status successor base main SHA", "`0000000000000000000000000000000000000000`"),
        )
        for field, value in declarations:
            declaration = f"\n- **{field}:** {value}\n"
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                harden_path = _current_working_path(root, "HARDEN-02_CONTRACT_WORKING_")
                harden = harden_path.read_text(encoding="utf-8")
                current_harden_version = re.search(r"v(\d+\.\d+\.\d+)", harden_path.name).group(1)
                self.assertIn(
                    f"- **Plan / contract version:** `v{current_harden_version}`",
                    harden.split("### Revision log", 1)[0],
                )
                harden_path.write_text(harden + declaration, encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "phase8_approved_status_successor_current"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("Phase 8 current-route SHA-256 differs", promotion_check["message"])

    def test_fp001_pmr_rejects_immediate_predecessors_left_in_working_routes(self):
        stale_routes = (
            (
                "Atlas v0.4.13",
                "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.14.md",
                "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.16.md",
                "direct predecessor remains at its retired working path",
            ),
            (
                "HARDEN-02 v0.5.16",
                "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.16.md",
                "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.14.md",
                "direct predecessor remains at its retired working path",
            ),
        )
        for name, stale_route, other_route, expected_message in stale_routes:
            with self.subTest(route=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                stale_path = root / stale_route
                other_path = root / other_route
                archive_path = root / stale_route.replace("/working/", "/archive/")
                self.assertTrue(archive_path.is_file())
                stale_path.write_bytes(archive_path.read_bytes())
                if other_path.exists():
                    other_path.unlink()

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_phase7c_final_contract_current_promotion"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn(expected_message, promotion_check["message"])

    def test_fp001_pmr_current_status_successor_artifacts_are_byte_pinned(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            atlas_path = _current_working_path(root, "DELIVERY_ATLAS_WORKING_")
            harden_path = _current_working_path(root, "HARDEN-02_CONTRACT_WORKING_")
            atlas_path.write_text(
                atlas_path.read_text(encoding="utf-8")
                + "\n- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md` (unreviewed declaration)\n",
                encoding="utf-8",
            )
            harden_path.write_text(
                harden_path.read_text(encoding="utf-8")
                + "\n- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md` (unreviewed declaration)\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "phase8_approved_status_successor_current"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("Phase 8 current-route SHA-256 differs", promotion_check["message"])

    def test_fp001_identity_v014_promotion_rejects_non_immediate_atlas_predecessor(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            open_work_path = _current_open_work_path(root)
            open_work = open_work_path.read_text(encoding="utf-8")
            current_atlas = _current_working_path(root, "DELIVERY_ATLAS_WORKING_")
            atlas = current_atlas.read_text(encoding="utf-8")
            predecessor_match = re.search(r"(?m)^- \*\*Predecessor:\*\* `([^`]+)`", atlas)
            self.assertIsNotNone(predecessor_match, "current Atlas direct predecessor metadata is missing")
            current_predecessor = f"immediate routing predecessor `{predecessor_match.group(1)}`"
            self.assertIn(current_predecessor, open_work, "current Open Work does not route the Atlas predecessor")
            open_work = open_work.replace(
                current_predecessor,
                "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.9.md`",
                1,
            )
            open_work_path.write_text(open_work, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "phase8_approved_status_successor_current"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("Atlas predecessor", promotion_check["message"])

    def test_fp001_identity_v014_promotion_rejects_lineage_route_and_gate_mutations(self):
        def rewrite_current_open_work_state(root: Path, mutate) -> None:
            manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            current = next(
                entry for entry in manifest["governing_documents"]
                if entry["document_id"] == "OPEN_WORK" and entry.get("lifecycle") != "historical"
            )
            open_work_path = root / current["repository_path"]
            open_work = open_work_path.read_text(encoding="utf-8")
            start = open_work.index("<!-- HARDEN_02_LIFECYCLE_STATE_START -->")
            json_start = open_work.index("{", start)
            json_end = open_work.index("\n```", json_start)
            state = json.loads(open_work[json_start:json_end])
            mutate(state)
            open_work_path.write_text(
                open_work[:json_start] + json.dumps(state, indent=2) + open_work[json_end:],
                encoding="utf-8",
            )

        def replace_once(root: Path, relative: str, old: str, new: str) -> None:
            path = root / "docs/00_platform" / relative
            text = path.read_text(encoding="utf-8")
            if old not in text:
                raise AssertionError(f"mutation anchor missing from {relative}: {old}")
            path.write_text(text.replace(old, new, 1), encoding="utf-8")

        def restore_candidate_route(root: Path) -> None:
            candidate = (
                root / "docs/00_platform/working/candidates/"
                "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            )
            candidate.parent.mkdir(parents=True, exist_ok=True)
            candidate.write_bytes(
                (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").read_bytes()
            )

        mutations = (
            (
                "wrong current dossier version",
                lambda root: replace_once(
                    root,
                    "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
                    "**Artifact version:** v0.1.4",
                    "**Artifact version:** v0.1.3",
                ),
            ),
            (
                "candidate remains on active route",
                restore_candidate_route,
            ),
            (
                "missing exact PR #76 candidate archive",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                ).unlink(),
            ),
            (
                "altered exact PR #76 candidate archive",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                ).write_bytes(
                    (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").read_bytes()
                    + b"\nALTERED CANDIDATE\n"
                ),
            ),
            (
                "missing superseded promoted-current v0.1.3 snapshot",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
                ).unlink(),
            ),
            (
                "altered superseded promoted-current v0.1.3 snapshot",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
                ).write_bytes(
                    (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md").read_bytes()
                    + b"\nALTERED CURRENT SNAPSHOT\n"
                ),
            ),
            (
                "PR #70 candidate confused with promoted-current snapshot",
                lambda root: (
                    (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md").write_bytes(
                        (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md").read_bytes()
                    ),
                ),
            ),
            (
                "wrong PR #76 post-merge attestation URL",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state["identity_v014_promotion_certification"].update(
                        {"post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/76"}
                    ),
                ),
            ),
            (
                "missing PR #76 post-merge attestation URL",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state["identity_v014_promotion_certification"].pop(
                        "post_merge_attestation_url", None
                    ),
                ),
            ),
            (
                "post-merge reviewer falsely attributed to poster",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state["identity_v014_promotion_certification"].update(
                        {"post_merge_independent_review_actor": "JCSchoeman96"}
                    ),
                ),
            ),
            (
                "stale Open Work Identity lifecycle route",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"identity_dossier": "CERTIFIED / CURRENT v0.1.3"})
                ),
            ),
            (
                "stale README Identity route",
                lambda root: replace_once(
                    root,
                    "README.md",
                    "- IDENTITY v0.1.4: CERTIFIED / CURRENT under the separate PR #77 status successor",
                    "- IDENTITY v0.1.3: CERTIFIED / CURRENT under PR #70",
                ),
            ),
            (
                "stale Delivery Atlas Identity route",
                lambda root: replace_once(
                    root,
                    _current_working_route(root, "DELIVERY_ATLAS_WORKING_"),
                    "Identity dossier v0.1.4 is CERTIFIED / CURRENT",
                    "Identity dossier v0.1.3 is CERTIFIED / CURRENT",
                ),
            ),
            (
                "stale HARDEN-02 Identity route",
                lambda root: replace_once(
                    root,
                    _current_working_route(root, "HARDEN-02_CONTRACT_WORKING_"),
                    "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
                    "IDENTITY v0.1.3 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
                ),
            ),
            (
                "Communications started or finalised",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state.update(
                        {
                            "communications": "COMPLETE / FINALISED",
                            "communications_finalisation": "COMPLETE / FINALISED",
                        }
                    ),
                ),
            ),
            (
                "Phase 7C prematurely advanced",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"phase_7c": "READY / STARTED"})
                ),
            ),
            (
                "proof classification prematurely finalised",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"proof_classification": "FINALISED"})
                ),
            ),
            (
                "Phase 8 or implementation prematurely authorised",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"application_implementation": "AUTHORISED"})
                ),
            ),
        )

        for name, mutate in mutations:
            with self.subTest(mutation=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                mutate(root)
                if name not in {
                    "missing exact PR #76 candidate archive",
                    "altered exact PR #76 candidate archive",
                    "missing superseded promoted-current v0.1.3 snapshot",
                    "altered superseded promoted-current v0.1.3 snapshot",
                    "PR #70 candidate confused with promoted-current snapshot",
                }:
                    refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                expected_check = (
                    "fp001_pmr_reconciliation"
                    if name in {
                        "wrong current dossier version",
                        "candidate remains on active route",
                        "missing exact PR #76 candidate archive",
                        "altered exact PR #76 candidate archive",
                        "missing superseded promoted-current v0.1.3 snapshot",
                        "altered superseded promoted-current v0.1.3 snapshot",
                        "PR #70 candidate confused with promoted-current snapshot",
                    }
                    else "fp001_phase8_proof_contract_lifecycle"
                )
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == expected_check
                )
                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                if expected_check == "fp001_phase8_proof_contract_lifecycle":
                    if name == "stale README Identity route":
                        self.assertIn(
                            "README current state omits TB-001 lifecycle state 'IDENTITY v0.1.4'",
                            promotion_check["message"],
                        )
                    else:
                        self.assertIn("manifest Phase 8 route hash differs", promotion_check["message"])

    def test_fp001_durable_delivery_attestation_requires_bound_post_merge_comment(self):
        mutations = (
            ("missing_url", lambda evidence: evidence.pop("post_merge_attestation_url", None)),
            (
                "self_assertion_used_as_url",
                lambda evidence: evidence.update(
                    {
                        "post_merge_attestation": "COMPLETE",
                        "post_merge_attestation_url": (
                            "COMPLETE / preserved in this status successor and Identity dossier v0.1.3"
                        ),
                    }
                ),
            ),
        )
        for name, mutate in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                open_work_path = _current_open_work_path(root)
                open_work = open_work_path.read_text(encoding="utf-8")
                lifecycle_start = open_work.index("<!-- HARDEN_02_LIFECYCLE_STATE_START -->")
                json_start = open_work.index("{", lifecycle_start)
                json_end = open_work.index("\n```", json_start)
                lifecycle_state = json.loads(open_work[json_start:json_end])
                mutate(lifecycle_state["identity_durable_delivery_certification"])
                open_work = (
                    open_work[:json_start]
                    + json.dumps(lifecycle_state, indent=2)
                    + open_work[json_end:]
                )
                open_work_path.write_text(open_work, encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                reconciliation = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_phase8_proof_contract_lifecycle"
                )

                self.assertEqual("FAIL", reconciliation["status"], reconciliation["message"])
                self.assertIn("manifest Phase 8 route hash differs", reconciliation["message"])

    def test_fp001_pmr_rejects_unarchived_predecessor_route_in_current_atlas(self):
        mutations = (
            ("atlas", "02_OPEN_WORK_v1.2.54.md"),
            ("atlas", "DELIVERY_ATLAS_WORKING_v0.3.6.md"),
            ("harden", "HARDEN-02_CONTRACT_WORKING_v0.4.8.md"),
            (
                "atlas",
                "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
            ),
        )
        for route_kind, predecessor in mutations:
            with self.subTest(predecessor=predecessor), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                route_path = _current_working_route(
                    root,
                    "DELIVERY_ATLAS_WORKING_" if route_kind == "atlas" else "HARDEN-02_CONTRACT_WORKING_",
                )
                current_route = root / "docs/00_platform" / route_path
                current_route.write_text(
                    current_route.read_text(encoding="utf-8")
                    + f"\nCurrent route pointer: {predecessor}\n",
                    encoding="utf-8",
                )
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] == "phase8_approved_status_successor_current"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )
                self.assertTrue(
                    any(
                        finding["check"] == "active_document_graph"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_fp001_audit_work_start_predecessors_fail_in_unqualified_active_routes(self):
        mutations = (
            ("open_work", "02_OPEN_WORK_v1.2.65.md"),
            ("atlas", "DELIVERY_ATLAS_WORKING_v0.4.7.md"),
            (
                "skeleton",
                "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.9.md",
            ),
            (
                "harden",
                "HARDEN-02_CONTRACT_WORKING_v0.5.9.md",
            ),
        )
        for route_kind, predecessor in mutations:
            with self.subTest(predecessor=predecessor), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                route_path = {
                    "open_work": _current_open_work_route(root),
                    "atlas": _current_working_route(root, "DELIVERY_ATLAS_WORKING_"),
                    "skeleton": _current_working_route(root, "FP-001_FEATURE_PACK_SKELETON_WORKING_"),
                    "harden": _current_working_route(root, "HARDEN-02_CONTRACT_WORKING_"),
                }[route_kind]
                current_route = root / "docs/00_platform" / route_path
                current_route.write_text(
                    current_route.read_text(encoding="utf-8")
                    + f"\nCurrent route pointer: {predecessor}\n",
                    encoding="utf-8",
                )
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(finding["check"] == "active_document_graph" for finding in report["findings"]),
                    report["findings"],
                )

    def test_fp001_pmr_rejects_unreviewed_additions_to_current_route(self):
        archived_predecessors = (
            "archive/02_OPEN_WORK_v1.2.66.md",
            "archive/DELIVERY_ATLAS_WORKING_v0.4.8.md",
            "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md",
            "archive/HARDEN-02_CONTRACT_WORKING_v0.5.10.md",
        )
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            current_atlas = _current_working_path(root, "DELIVERY_ATLAS_WORKING_")
            current_atlas.write_text(
                current_atlas.read_text(encoding="utf-8")
                + "\nHistorical archive references: "
                + ", ".join(archived_predecessors)
                + "\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"], report["findings"])
            self.assertTrue(
                any(
                    finding["check"] == "phase8_approved_status_successor_current"
                    and "Phase 8 current-route SHA-256 differs" in finding["message"]
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_fails_closed_if_final_contract_proof_obligations_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            contract_path = root / (
                "docs/00_platform/working/"
                "FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
            )
            contract = contract_path.read_text(encoding="utf-8")
            self.assertEqual(1, contract.count("registration-to-verification-to-login"))
            contract_path.write_text(
                contract.replace("registration-to-verification-to-login", "registration-to-login", 1),
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "phase8_approved_status_successor_current"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn(
                "Phase 8 current-route SHA-256 differs: docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
                promotion_check["message"],
            )

    def test_fp001_pmr_rejects_multiple_active_skeleton_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            working = root / "docs/00_platform/working"
            active = working / _current_working_path(root, "FP-001_FEATURE_PACK_SKELETON_WORKING_").name
            duplicate = working / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.4.md"
            duplicate.write_bytes(active.read_bytes())

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_rejects_multiple_active_identity_dossier_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            working = root / "docs/00_platform/working"
            active = working / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            duplicate = working / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            duplicate.write_bytes(active.read_bytes())

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_mutation_matrix_fails_closed(self):
        mutations = (
            ("skeleton_pre_pmr_outcome", "skeleton", "A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, receive that Account's required human-facing Platform Member Reference (PMR), verify email, recover access and use a controlled support/admin path without exposing unfinished product spaces.", "A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, verify email, recover access and use a controlled support/admin path without exposing unfinished product spaces."),
            ("identity_dossier_omits_pmr", "dossier", "The PMR is stable and human-facing.", "The PMR is opaque and non-human-facing."),
            ("pmr_before_account_success", "dossier", "only after successful individual Account creation", "before successful individual Account creation"),
            ("failed_partial_ambiguous_creation_exposes_pmr", "dossier", "A failed, partial or ambiguous Account creation does not assign an externally usable PMR", "A failed, partial or ambiguous Account creation assigns an externally usable PMR"),
            ("retry_does_not_converge", "dossier", "retries converge on the one committed Account/reference result", "retries create a new PMR on each attempt"),
            ("reference_not_stable_human_facing", "dossier", "The PMR is stable and human-facing.", "The PMR is unstable and opaque."),
            ("pmr_other_domain_owner", "dossier", "The Platform Member Reference is Identity & Access Account truth", "The Platform Member Reference is Communications Account truth"),
            ("pmr_is_authentication", "dossier", "it is not authentication", "it is authentication"),
            ("pmr_is_authorisation", "dossier", "it is not authorisation", "it is authorisation"),
            ("pmr_is_database_identity", "dossier", "It is not database identity", "It is database identity"),
            ("pmr_is_verification_assurance", "dossier", "it is not verification assurance", "it is verification assurance"),
            ("pmr_is_membership", "dossier", "it is not paid Membership", "it is paid Membership"),
            ("pmr_is_subscription", "dossier", "it is not subscription state", "it is subscription state"),
            ("pmr_is_entitlement", "dossier", "it is not entitlement", "it is entitlement"),
            ("pmr_is_payment_authority", "dossier", "it is not payment authority", "it is payment authority"),
            ("pmr_is_voucher_coupon_discount_authority", "dossier", "it is not a voucher/coupon/discount authority", "it is a voucher/coupon/discount authority"),
            ("pmr_is_bearer_credential", "dossier", "it is not a bearer credential", "it is a bearer credential"),
            ("multiple_active_pmrs", "dossier", "one canonical active PMR per canonical individual Account", "multiple canonical active PMRs per canonical individual Account"),
            ("ordinary_pmr_mutable", "dossier", "Ordinary PMR values are immutable.", "Ordinary PMR values are mutable."),
            ("reactivation_loses_reference", "dossier", "Legitimate reactivation retains the correct reference.", "Legitimate reactivation issues a new reference."),
            ("retired_reuse", "dossier", "never reassign or reuse it", "may reassign or reuse it"),
            ("duplicate_survivor_semantics_changed", "dossier", "one canonical active Account/reference and permanently retires the non-surviving reference", "two canonical active Accounts/references are retained"),
            ("allocation_collision_safety_lost", "dossier", "collision-safe, concurrency-correct and idempotent", "collision-prone, concurrency-unsafe and non-idempotent"),
            ("lookup_not_purpose_scoped", "dossier", "purpose-scoped, minimum-disclosure and non-authoritative", "unscoped, full-disclosure and authoritative"),
            ("lifecycle_dimensions_collapsed", "dossier", "orthogonal account, verification and security dimensions", "one collapsed Account status for account, verification and security"),
            ("representation_frozen", "skeleton", "Exact PMR representation remains unfrozen under `ARQ-IAM-013`", "The PMR prefix is VG and the alphabet is fixed"),
            ("arq_iam_013_resolved", "skeleton", "Exact PMR representation remains unfrozen under `ARQ-IAM-013`", "Exact PMR representation is resolved under `ARQ-IAM-013`"),
            ("oq034_proof_complete", "skeleton", "The approved authentication architecture is selected; proof execution has not started. Classification is complete as NEW_TRACER_BULLET.", "The approved authentication architecture is selected; proof execution is complete. Classification is complete as NEW_TRACER_BULLET."),
            ("oq035_resolved", "skeleton", "| `OQ-035` | `BLOCKS_RELEASE_ONLY` |", "| `OQ-035` | `RESOLVED` |"),
            ("oq036_resolved", "skeleton", "| `OQ-036` | `BLOCKS_RELEASE_ONLY` |", "| `OQ-036` | `RESOLVED` |"),
            ("communications_completed", "open_work", "COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0", "COMMUNICATIONS: COMPLETE / CERTIFIED"),
            ("reconciliation_started", "open_work", '"phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT"', '"phase_7b_reconciliation": "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"'),
            ("communications_route_still_downstream", "open_work", "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION", "NEXT GOVERNANCE ACTION: RUN FP-001 PROOF CLASSIFICATION; STATUS: NOT_STARTED"),
            ("reconciliation_completed", "open_work", "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT", "PHASE 7B RECONCILIATION: NEXT / NOT_STARTED"),
            ("communications_dossier_started", "dossier", "COMMUNICATIONS DOSSIER STARTED: NO", "COMMUNICATIONS DOSSIER STARTED: YES"),
            ("conditional_dossiers_adjudicated", "open_work", "- AUDIT & EVIDENCE: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0", "- AUDIT & EVIDENCE: NOT_REQUIRED"),
            ("phase_7c_unblocked", "open_work", "PHASE 7C: COMPLETE / CERTIFIED / CURRENT", "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"),
            ("proof_finalised", "open_work", "PROOF CLASSIFICATION: NEW_TRACER_BULLET", "PROOF CLASSIFICATION: NOT FINALISED"),
            ("phase_8_authorised", "open_work", "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", "PHASE 8: AUTHORISED"),
            ("candidate_status_promoted_without_pr67_evidence", "skeleton", "79d0540c66f0224ece0330181e61dfef8ab4b458", "0000000000000000000000000000000000000000"),
            ("skeleton_remains_candidate", "skeleton", "**Lifecycle status:** CERTIFIED / CURRENT as a Phase 7A skeleton", "**Lifecycle status:** RECONCILIATION CANDIDATE / NOT CERTIFIED as a Phase 7A skeleton"),
            ("identity_dossier_remains_candidate", "dossier", "**Status:** `CERTIFIED / CURRENT`", "**Status:** `RECONCILIATION CANDIDATE / NOT CERTIFIED`"),
            ("communication_started", "open_work", "COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0", "COMMUNICATIONS: STARTED"),
            (
                "proof_classification_marked_complete",
                "open_work",
                '    "PR #125 Phase 7C candidate certification and resulting-main verification COMPLETE",\n    "PR #126 resulting-main verification and Phase 7C tracker #124 closure COMPLETE"\n  ],\n  "engineering_standards_authority_promotion"',
                '    "PR #125 Phase 7C candidate certification and resulting-main verification COMPLETE",\n    "PR #126 resulting-main verification and Phase 7C tracker #124 closure COMPLETE",\n    "FP-001 ARCHITECTURAL PROOF CLASSIFICATION"\n  ],\n  "engineering_standards_authority_promotion"',
            ),
            ("oq038_changed", "skeleton", "| `OQ-038` | `FUTURE_ONLY` |", "| `OQ-038` | `BLOCKS_RELEASE_ONLY` |"),
            ("store_cer_included", "open_work", "STORE / CER: EXCLUDED FROM HARDEN-02", "STORE / CER: INCLUDED IN SCOPE"),
        )
        source_root = Path(__file__).resolve().parents[1]
        for name, target, current, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                relative = {
                    "skeleton": _current_working_relative_path(root, "FP-001_FEATURE_PACK_SKELETON_WORKING_"),
                    "dossier": "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
                    "open_work": _current_open_work_relative_path(root),
                }[target]
                path = root / relative
                text = path.read_text(encoding="utf-8")
                if target == "open_work" and name in {
                    "reconciliation_started",
                    "communications_route_still_downstream",
                    "reconciliation_completed",
                    "phase_7c_unblocked",
                    "proof_finalised",
                    "phase_8_authorised",
                }:
                    active_start = text.index("# 9. Immediate Next Action")
                    active_end = text.index("# 10. Minimal Tools", active_start + 1)
                    active = text[active_start:active_end]
                    if name == "communications_route_still_downstream":
                        current_action = re.findall(r"(?m)^NEXT GOVERNANCE ACTION:.*$", active)
                        self.assertEqual(1, len(current_action), "current next-action route must be unique")
                        current = current_action[0]
                    self.assertIn(current, active, f"current-route mutation anchor missing: {name}")
                    active = active.replace(current, replacement, 1)
                    text = text[:active_start] + active + text[active_end:]
                else:
                    self.assertIn(current, text, f"mutation anchor missing: {name}")
                    text = text.replace(current, replacement, 1)
                path.write_text(text, encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] in {
                            "fp001_pmr_reconciliation",
                            "fp001_phase8_proof_contract_lifecycle",
                            "roadmap_proof_classification_lifecycle",
                        }
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_fp001_pmr_successor_requires_archived_predecessors_and_current_routes(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            predecessor_paths = (
                root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
                root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md",
            )
            for predecessor in predecessor_paths:
                predecessor.unlink()

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_rejects_stale_candidate_path_alongside_certified_successor(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            working = root / "docs/00_platform/working"
            stale = working / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"
            certified = working / _current_working_path(root, "FP-001_FEATURE_PACK_SKELETON_WORKING_").name
            stale.write_bytes(certified.read_bytes())

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_rejects_communications_dossier_when_not_certified_current(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            communications = root / "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            communications.write_text("status-only PR mutation\n", encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_phase8_proof_contract_lifecycle"
                    and "frozen Phase 8 proof source changed" in finding["message"]
                    and "FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md" in finding["message"]
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_communications_v010_promotion_is_current_and_pins_archives(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )
            self.assertEqual("PASS", promotion_check["status"], promotion_check["message"])

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            pinned = manifest["integrity_rules"]["communications_v010_promotion_archives"]
            self.assertEqual(
                {
                    "docs/00_platform/archive/02_OPEN_WORK_v1.2.58.md",
                    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.0.md",
                    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md",
                    "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.4.md",
                    "docs/00_platform/archive/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
                },
                set(pinned),
            )
            archive = root / "docs/00_platform/archive/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            self.assertEqual(
                "039f1b0e249f62dfd606fc6484681d4e821077fb4c89eba65c4f33eb752277a9",
                hashlib.sha256(archive.read_bytes()).hexdigest(),
            )

    def test_fp001_communications_v010_promotion_coherence_guards_fail_closed(self):
        mutations = (
            (
                "wrong_pr78_base",
                lambda text: text.replace(
                    "based on merge base `ff1ff5c64b764fc4229e4dccfc46e58482d2b3d0`",
                    "based on `a062bd56e3ae94e815e2991ee00bf133ee9f3b56`",
                    1,
                ),
            ),
            (
                "live_work_start_section",
                lambda text: text.replace(
                    "(historical predecessor record)",
                    "",
                    1,
                ).replace(
                    "At the Open Work v1.2.58 predecessor state, Communications Phase 7B work had begun",
                    "Communications Phase 7B work has begun",
                    1,
                ),
            ),
            (
                "harden_i07_stale",
                None,
            ),
            (
                "harden_route_stale",
                None,
            ),
        )
        for label, mutator in mutations:
            with self.subTest(mutation=label), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                if label == "harden_i07_stale":
                    path = _current_working_path(root, "HARDEN-02_CONTRACT_WORKING_")
                    path.write_text(
                        path.read_text(encoding="utf-8").replace(
                            "Audit & Evidence v0.1.0 REQUIRED / COMPLETE / CERTIFIED / CURRENT",
                            "Audit & Evidence v0.1.0 REQUIRED / IN PROGRESS / NOT COMPLETE",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, manifest_path)
                elif label == "harden_route_stale":
                    open_work_path = _current_open_work_path(root)
                    open_work = open_work_path.read_text(encoding="utf-8")
                    lifecycle_match = re.search(
                        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
                        open_work,
                        re.DOTALL,
                    )
                    self.assertIsNotNone(lifecycle_match)
                    lifecycle_state = json.loads(lifecycle_match.group(1))
                    current_action = f"NEXT GOVERNANCE ACTION: {lifecycle_state['next_governance_action']}"
                    self.assertIn(current_action, open_work)
                    open_work_path.write_text(
                        open_work.replace(current_action, "NEXT GOVERNANCE ACTION: TRACER BULLET IMPLEMENTATION", 1),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, manifest_path)
                else:
                    open_work_path = _current_open_work_path(root)
                    open_work_path.write_text(mutator(open_work_path.read_text(encoding="utf-8")), encoding="utf-8")
                    refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                expected_check = {
                    "harden_route_stale": "fp001_phase8_proof_contract_lifecycle",
                    "harden_i07_stale": "fp001_phase8_proof_contract_lifecycle",
                }.get(label, "fp001_phase8_proof_contract_lifecycle")
                self.assertTrue(
                    any(finding["check"] == expected_check for finding in report["findings"]),
                    report["findings"],
                )

    def test_communications_v010_promotion_archive_manifest_contract_fails_closed(self):
        relative = "docs/00_platform/archive/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        for mutation in ("missing", "wrong_hash", "path_substitution"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                archives = manifest["integrity_rules"]["communications_v010_promotion_archives"]
                if mutation == "missing":
                    archives.pop(relative)
                elif mutation == "wrong_hash":
                    archives[relative] = "0" * 64
                else:
                    archives.pop(relative)
                    archives["docs/00_platform/archive/UNEXPECTED.md"] = "0" * 64
                manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(finding["check"] == "fp001_pmr_reconciliation" for finding in report["findings"]),
                    report["findings"],
                )

    def test_fp001_pmr_archive_hash_contract_mutations_fail_closed(self):
        archive_paths = {
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md",
        }
        for mutation in ("missing", "malformed", "wrong", "path_substitution"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                hashes = manifest["integrity_rules"]["fp001_pmr_predecessor_archives"]
                if mutation == "missing":
                    hashes.pop("docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md")
                elif mutation == "malformed":
                    hashes["docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"] = "not-a-sha256"
                elif mutation == "wrong":
                    hashes["docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"] = "0" * 64
                else:
                    hashes.pop("docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md")
                    hashes["docs/00_platform/archive/UNEXPECTED_SUBSTITUTE.md"] = "a09bf07b189cbf3384cfe803d2ef1f32c3eaa6556333141fde1e323b6174b207"
                manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] == "fp001_pmr_reconciliation"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_communications_start_status_archive_manifest_contract_fails_closed(self):
        relative = "docs/00_platform/archive/02_OPEN_WORK_v1.2.57.md"
        for mutation in ("missing", "wrong_hash", "path_substitution"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                archives = manifest["integrity_rules"]["communications_start_status_archives"]
                if mutation == "missing":
                    archives.pop(relative)
                elif mutation == "wrong_hash":
                    archives[relative] = "0" * 64
                else:
                    archives.pop(relative)
                    archives["docs/00_platform/archive/UNEXPECTED.md"] = "0" * 64
                manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(finding["check"] == "fp001_pmr_reconciliation" for finding in report["findings"]),
                    report["findings"],
                )

    def test_communications_start_status_archive_bytes_are_pinned(self):
        relative = "docs/00_platform/archive/02_OPEN_WORK_v1.2.57.md"
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            archive = root / relative
            archive.write_bytes(archive.read_bytes() + b"\nALTERED PRE-START STATUS\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "manifest_hash_parity"
                    and finding["path"] == relative
                    and "SHA-256 mismatch" in finding["message"]
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_candidate_archive_missing_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            (root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md").unlink()

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_corrupted_skeleton_archive_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_corrupted_identity_archive_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_corrupted_candidate_archive_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_identity_v013_candidate_archive_corruption_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_identity_v013_candidate_path_is_retired_after_promotion(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            stale_candidate = root / "docs/00_platform/working/candidates/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            stale_candidate.parent.mkdir(parents=True, exist_ok=True)
            stale_candidate.write_text("unpromoted candidate route\n", encoding="utf-8")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def _copy_production_fixture(self, root: Path) -> tuple[Path, Path]:
        source_root = Path(__file__).resolve().parents[1]
        fixture_docs = root / "docs" / "00_platform"
        shutil.copytree(source_root / "docs" / "00_platform", fixture_docs)
        execution_docs = root / "docs" / "execution"
        execution_docs.mkdir(parents=True)
        shutil.copyfile(
            source_root / "docs" / "execution" / "p8-05-registration-jit-spec.md",
            execution_docs / "p8-05-registration-jit-spec.md",
        )
        manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        refresh_manifest(root, manifest_path)
        return root, manifest_path

    def _copy_predecessor_fixture(self, root: Path) -> tuple[Path, Path]:
        """Materialize the exact v1.2.77 governance snapshot for historical tests."""

        copy_git_snapshot_tree(
            REPOSITORY_ROOT,
            WELL38_BASE_SHA,
            root,
            "docs/00_platform",
        )
        manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        return root, manifest_path

    def test_phase7b_certification_rejects_stale_current_readme_but_allows_history(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            readme = root / "docs" / "00_platform" / "README.md"
            text = readme.read_text(encoding="utf-8")
            current_route = "- PHASE 7C: COMPLETE / CERTIFIED / CURRENT\n- FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT\n- PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED"
            self.assertIn(current_route, text)
            readme.write_text(
                text.replace(
                    current_route,
                    current_route
                    + "\n\n### Current state details\n\n#### Nested status detail\n\n"
                    + "Phase 7C remains BLOCKED / NOT_STARTED.",
                    1,
                ),
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)

            certification_check = next(
                item
                for item in report["checks"]
                if item["name"] == "phase8_approved_status_successor_current"
            )
            self.assertEqual("FAIL", certification_check["status"])
            self.assertIn("BLOCKED / NOT_STARTED Phase 7C statement", certification_check["message"])

        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            readme = root / "docs" / "00_platform" / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n\n## Archive\n\n"
                + "At that predecessor state, Phase 7C was BLOCKED / NOT_STARTED.\n",
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)

            certification_check = next(
                item
                for item in report["checks"]
                if item["name"] == "phase8_approved_status_successor_current"
            )
            self.assertEqual("PASS", certification_check["status"], certification_check["message"])

    def test_roadmap_proof_classification_lifecycle_is_a_foundation_integrity_check(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))

            report = run_audit(root, manifest_path)

            lifecycle_check = next(
                (
                    item
                    for item in report["checks"]
                    if item["name"] == "roadmap_proof_classification_lifecycle"
                ),
                None,
            )
            self.assertIsNotNone(lifecycle_check, "Foundation Integrity must check the Roadmap proof gate")
            if lifecycle_check is not None:
                self.assertEqual("PASS", lifecycle_check["status"], lifecycle_check["message"])

    def test_archived_proof_contract_requires_historical_manifest_and_immutable_hash(self):
        relative = "docs/00_platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
        content = b"reviewed TB-001 proof contract\n"
        digest = hashlib.sha256(content).hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / relative
            archive.parent.mkdir(parents=True)
            archive.write_bytes(content)
            manifest = {
                "historical_documents": [
                    {
                        "repository_path": relative,
                        "lifecycle": "historical",
                        "authority_class": "FP001_PHASE8_PROOF_CONTRACT_HISTORICAL",
                        "graph_policy": "frozen_provenance",
                        "sha256": digest,
                        "provenance_sha256": digest,
                    }
                ]
            }
            integrity_rules = {
                "fp001_phase8_proof_contract_lifecycle": {
                    "reviewed_candidate_archive_path": relative,
                    "reviewed_candidate_archive_sha256": digest,
                }
            }

            self.assertEqual(
                {relative},
                _fp001_pinned_historical_proof_contract_archives(root, manifest, integrity_rules),
            )

            archive.write_bytes(content + b"changed\n")
            self.assertEqual(
                set(),
                _fp001_pinned_historical_proof_contract_archives(root, manifest, integrity_rules),
            )

    def test_roadmap_proof_classification_final_contract_hash_pins_fail_closed(self):
        for pin in ("phase7c_contract_sha256", "current_route_sha256"):
            with self.subTest(pin=pin), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                rule = manifest["integrity_rules"]["roadmap_proof_classification_lifecycle"]
                if pin == "phase7c_contract_sha256":
                    rule[pin] = "0" * 64
                else:
                    contract_path = rule["phase7c_contract_path"]
                    rule[pin][contract_path] = "0" * 64
                manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

                report = run_audit(root, manifest_path)

                lifecycle_check = next(
                    item for item in report["checks"]
                    if item["name"] == "roadmap_proof_classification_lifecycle"
                )
                self.assertEqual("FAIL", lifecycle_check["status"], lifecycle_check["message"])
                self.assertIn("manifest SHA-256 pins disagree with actual bytes", lifecycle_check["message"])

    def test_current_phase8_status_is_independent_of_branch_and_head_ref(self):
        """The started Phase 8 route remains governed by repository authority."""
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            (root / "mix.exs").write_text("# application source\n", encoding="utf-8")
            refresh_manifest(root, manifest_path)

            real_run = subprocess.run

            def run_with_detached_head(args, *positional, **kwargs):
                if args == ["git", "branch", "--show-current"]:
                    return subprocess.CompletedProcess(args, 0, stdout="", stderr="")
                return real_run(args, *positional, **kwargs)

            with patch.dict(os.environ):
                os.environ.pop("GITHUB_HEAD_REF", None)
                with patch("tools.foundation_integrity_audit.subprocess.run", side_effect=run_with_detached_head):
                    report = run_audit(root, manifest_path)

            route_check = next(
                item for item in report["checks"]
                if item["name"] == "phase8_approved_status_successor_current"
            )
            self.assertEqual("PASS", route_check["status"], route_check["message"])
            lifecycle_check = next(
                item for item in report["checks"]
                if item["name"] == "harden_02_lifecycle_state"
            )
            self.assertEqual("PASS", lifecycle_check["status"], lifecycle_check["message"])
            self.assertIn("the TB-001 result is incomplete", lifecycle_check["message"])

    def test_roadmap_proof_classification_lifecycle_fails_closed_on_scope_regressions(self):
        mutations = (
            (
                "global_phase7_ownership",
                "docs/00_platform/05_ROADMAP_v1.2.3.md",
                "Anticipated proof labels are provisional. An anticipated Roadmap proof label is not a proof classification.",
                "Anticipated proof labels are deliberately provisional. Phase 7 Final Feature Pack Contracts own the final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` decision.",
                "Roadmap no longer distinguishes anticipation from classification",
            ),
            (
                "fp001_phase7_ownership",
                "docs/00_platform/05_ROADMAP_v1.2.3.md",
                "The separate architectural proof classification gate after Phase 7C and before Phase 8 selects the final proof vehicle.",
                "Phase 7 decides whether one proof can cover the complete path.",
                "current Roadmap v1.2.3 is missing, changed or no longer provisional",
            ),
            (
                "classification_boundary_removed",
                "docs/00_platform/05_ROADMAP_v1.2.3.md",
                "The separate architectural proof classification gate runs after Phase 7C and before Phase 8 executable proof.",
                "The architectural proof classification gate occurs during Phase 8 executable proof.",
                "current Roadmap v1.2.3 is missing, changed or no longer provisional",
            ),
            (
                "atlas_contract_owns_choice",
                "atlas",
                "After Phase 7C and before Phase 8 executable proof, the separate architectural proof classification gate selects `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`.",
                "Phase 7C selects `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET` before Phase 8 executable proof.",
                "Delivery Atlas no longer preserves the separate post-7C classification boundary",
            ),
            (
                "atlas_classification_boundary_removed",
                "atlas",
                "After Phase 7C and before Phase 8 executable proof, the separate architectural proof classification gate selects `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`.",
                "Phase 7C selects `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET` before Phase 8 executable proof.",
                "Delivery Atlas no longer preserves the separate post-7C classification boundary",
            ),
            (
                "anticipated_label_promoted",
                "docs/00_platform/05_ROADMAP_v1.2.3.md",
                "**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET`. This direction is provisional.",
                "**Anticipated Architectural Proof:** `NEW_TRACER_BULLET`.",
                "current Roadmap v1.2.3 is missing, changed or no longer provisional",
            ),
            (
                "current_selection",
                "open_work",
                "REUSE_EXISTING_PROOF: NOT SELECTED",
                "REUSE_EXISTING_PROOF: SELECTED",
                "Open Work active route selects REUSE_EXISTING_PROOF",
            ),
            (
                "current_reuse_selection",
                "open_work",
                "REUSE_EXISTING_PROOF: NOT SELECTED",
                "REUSE_EXISTING_PROOF: SELECTED",
                "Open Work active route selects REUSE_EXISTING_PROOF",
            ),
            (
                "tracer_bullet_id",
                "open_work",
                "TRACER BULLET ID: TB-001",
                "TRACER BULLET ID: TB-002",
                "Open Work active route assigns a different Tracer Bullet identifier",
            ),
            (
                "phase8_authorised",
                "open_work",
                "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
                "PHASE 8: AUTHORISED",
                "Open Work active route authorises Phase 8 without bounded architectural-proof scope",
            ),
            (
                "issue_124_reopened",
                "open_work",
                "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
                "PHASE 7C EXECUTION/CONTROL TRACKER #124: OPEN / IN PROGRESS",
                "issue #124 is reopened in the current Open Work route",
            ),
            (
                "issue_111_closed",
                "open_work",
                "PROGRAMME ROUTER #111: OPEN",
                "PROGRAMME ROUTER #111: CLOSED / COMPLETED",
                "Open Work active route omits current classification state 'PROGRAMME ROUTER #111: OPEN'",
            ),
            (
                "roadmap_archive_drift",
                "docs/00_platform/archive/05_ROADMAP_v1.2.2.md",
                "# 05_ROADMAP_v1.2.2.md",
                "# changed Roadmap archive",
                "archived Roadmap v1.2.2 is missing or its immutable bytes changed",
            ),
            (
                "upstream_authority_drift",
                "docs/00_platform/03_ARCHITECTURE_v1.1.1.md",
                "# 03_ARCHITECTURE_v1.1.1.md",
                "# changed architecture authority",
                "protected Product, Decision, Architecture or Domain authority changed",
            ),
            (
                "product_authority_drift",
                "docs/00_platform/00_PLATFORM_v1.8.0.md",
                "# 00_PLATFORM_v1.8.0.md",
                "# changed Product authority",
                "protected Product, Decision, Architecture or Domain authority changed",
            ),
            (
                "domain_authority_drift",
                "docs/00_platform/04_DOMAIN_MAP_v1.2.0.md",
                "# 04_DOMAIN_MAP_v1.2.0.md",
                "# changed Domain authority",
                "protected Product, Decision, Architecture or Domain authority changed",
            ),
        )
        for name, relative, old, new, expected_message in mutations:
            with self.subTest(regression=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                relative = {
                    "atlas": _current_working_relative_path(root, "DELIVERY_ATLAS_WORKING_"),
                    "open_work": _current_open_work_relative_path(root),
                }.get(relative, relative)
                target = root / relative
                text = target.read_text(encoding="utf-8")
                if relative == _current_open_work_relative_path(root):
                    active_start = text.index("# 9. Immediate Next Action")
                    active_end = text.index("# 10. Minimal Tools", active_start + 1)
                    active = text[active_start:active_end]
                    self.assertIn(old, active)
                    active = active.replace(old, new, 1)
                    text = text[:active_start] + active + text[active_end:]
                else:
                    self.assertIn(old, text)
                    text = text.replace(old, new, 1)
                target.write_text(text, encoding="utf-8")
                refresh_manifest(root, manifest_path)
                _sync_integrity_route_pin(root, manifest_path, relative)

                report = run_audit(root, manifest_path)

                expected_check = (
                    "fp001_phase8_proof_contract_lifecycle"
                    if relative in {
                        _current_working_relative_path(root, "DELIVERY_ATLAS_WORKING_"),
                        _current_open_work_relative_path(root),
                    }
                    else "roadmap_proof_classification_lifecycle"
                )
                lifecycle_check = next(
                    item for item in report["checks"]
                    if item["name"] == expected_check
                )
                self.assertEqual("FAIL", lifecycle_check["status"], lifecycle_check["message"])
                if expected_check == "roadmap_proof_classification_lifecycle":
                    self.assertIn(expected_message, lifecycle_check["message"])
                else:
                    self.assertIn("manifest Phase 8 route hash differs", lifecycle_check["message"])

        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/02_OPEN_WORK_v1.2.72.md"
            archive.write_text(archive.read_text(encoding="utf-8") + "\narchive drift\n", encoding="utf-8")

            report = run_audit(root, manifest_path)

            predecessor_check = next(
                item for item in report["checks"]
                if item["name"] == "roadmap_proof_classification_lifecycle"
            )
            self.assertEqual("FAIL", predecessor_check["status"], predecessor_check["message"])
            self.assertIn("direct predecessor archive is missing or changed: docs/00_platform/archive/02_OPEN_WORK_v1.2.72.md", predecessor_check["message"])

        for relative in (
            "docs/00_platform/working/TRACER_BULLET_TB-001.md",
            "docs/00_platform/FP-001_ARCHITECTURAL_PROOF_CLASSIFICATION_v0.1.0.md",
        ):
            with self.subTest(artifact=relative), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_predecessor_fixture(Path(directory))
                artifact = root / relative
                artifact.write_text("proof artifact\n", encoding="utf-8")

                report = run_audit(root, manifest_path)

                lifecycle_check = next(
                    item for item in report["checks"]
                    if item["name"] == "roadmap_proof_classification_lifecycle"
                )
                self.assertEqual("FAIL", lifecycle_check["status"], lifecycle_check["message"])
                self.assertIn("Tracer Bullet or architectural-proof artifact exists", lifecycle_check["message"])

        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_predecessor_fixture(Path(directory))
            (root / "mix.exs").write_text("# application source\n", encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            # Authorised governed state permits application source; unauthorised rejection is covered in
            # tests/test_fp001_development_entry_hard_stop_promotion.py.
            hard_stop_check = next(
                item for item in report["checks"]
                if item["name"] == "fp001_development_entry_hard_stop_lifecycle"
            )
            self.assertEqual("PASS", hard_stop_check["status"], hard_stop_check["message"])

    def test_harden_execution_state_machine_fixtures(self):
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        candidate_open_work = historical_snapshot_path(REPOSITORY_ROOT, "02_OPEN_WORK_v1.2.77.md").read_text(encoding="utf-8")
        # v1.2.77 is a historical lifecycle fixture after a successor promotion. Its former
        # README mirror is represented here as fixture data rather than required to remain current.
        historical_readme_snapshot = """## Current State

TB-001 is CANDIDATE / REVIEW PENDING / NOT CERTIFIED
DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED
PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS
PROOF EXECUTION: NOT STARTED
PROOF RESULT: NOT STARTED
PROOF CERTIFICATION: NOT STARTED
PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED
NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION
"""
        contract = historical_snapshot_path(
            REPOSITORY_ROOT, "HARDEN-02_CONTRACT_WORKING_v0.5.21.md"
        ).read_text(encoding="utf-8")
        expected = (True, "TB-001 remains a review candidate; proof execution and Phase 9 remain unstarted")
        self.assertEqual(expected, _h02_lifecycle_state(candidate_open_work, historical_readme_snapshot, contract))

        archived_candidate_open_work = (source_docs / "archive" / "02_OPEN_WORK_v1.2.69.md").read_text(encoding="utf-8")
        archived_candidate_harden = (source_docs / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.13.md").read_text(encoding="utf-8")
        active_start = archived_candidate_open_work.find("# 9. Immediate Next Action")
        active_end = archived_candidate_open_work.find("# 10. Minimal Tools", active_start + 1)
        archived_candidate_active = archived_candidate_open_work[active_start:active_end]
        archived_candidate_readme = "## Current State\n\n" + archived_candidate_active
        self.assertEqual(
            (True, "Phase 7B remains certified/current; Phase 7C candidate awaits independent review and all later gates remain closed"),
            _h02_lifecycle_state(archived_candidate_open_work, archived_candidate_readme, archived_candidate_harden),
        )

        incomplete = candidate_open_work.replace(
            '"development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED"',
            '"development_entry_hard_stop_status": "FAIL / CONDITIONS NOT SATISFIED"',
            1,
        )
        self.assertFalse(_h02_lifecycle_state(incomplete, historical_readme_snapshot, contract)[0])

        old_route = candidate_open_work.replace(
            "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
            "DEVELOPMENT ENTRY HARD STOP: FAIL / CONDITIONS NOT SATISFIED",
            1,
        )
        self.assertFalse(_h02_lifecycle_state(old_route, historical_readme_snapshot, contract)[0])

        premature_authorisation = candidate_open_work.replace(
            '"phase8": "AUTHORISED"',
            '"phase8": "UNAUTHORISED"',
            1,
        ).replace(
            '"application_implementation": "AUTHORISED"',
            '"application_implementation": "UNAUTHORISED"',
            1,
        )
        self.assertFalse(_h02_lifecycle_state(premature_authorisation, historical_readme_snapshot, contract)[0])

    def test_production_audit_uses_manifest_expectations(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["integrity_rules"]["expected_counts"]["decisions"] = 2
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            decision_count_check = next(
                check for check in report["checks"] if check["name"] == "definition_count_dec"
            )
            self.assertEqual("DEC definition count is 1, expected 2", decision_count_check["message"])

    def test_completed_stage_3a1_readiness_wording_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            readme.write_text(
                "\n".join(
                    [f"`{entry['canonical_filename']}`" for entry in manifest["governing_documents"]]
                    + [
                        "PLANNING FOUNDATION: READY",
                        "STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE",
                        "STAGE 3A.2 — GOVERNED AR-000 AMENDMENT (NOT_STARTED / NEXT)",
                        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json")

            readiness_check = next(
                check for check in report["checks"] if check["name"] == "readiness_wording"
            )
            self.assertEqual("PASS", readiness_check["status"])

    def test_source_at_freeze_references_are_not_stale(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            source_at_freeze = root / "docs" / "00_platform" / "reference" / "ARCHITECTURE_LAW_WORKING_v0.35.0.md"
            source_at_freeze.write_text(
                source_at_freeze.read_text(encoding="utf-8")
                + "\nSource tracker at freeze: 02_OPEN_WORK_v1.2.23.md\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)02_OPEN_WORK_v1\.2\.(?:[0-9]|1[0-9]|2[0-6])\.md"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = ["ROADMAP"]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_non_navigation_document_is_not_scanned_for_stale_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            current_navigation = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            current_navigation.write_text(
                current_navigation.read_text(encoding="utf-8") + "\nOLD_TRACKER_MARKER\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"OLD_TRACKER_MARKER"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = []
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_declared_current_navigation_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            current_navigation = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            current_navigation.write_text(
                current_navigation.read_text(encoding="utf-8") + "\nOLD_TRACKER_MARKER\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"OLD_TRACKER_MARKER"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = ["ROADMAP"]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertTrue(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_current_authorities_reject_unarchived_historical_open_work(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            pattern = r"(?<!archive/)02_OPEN_WORK_v1\.2\.44\.md"
            self.assertIn(pattern, manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"])
            self.assertIn(
                "routing guard only",
                manifest["integrity_rules"]["graph_rules"]["stale_open_work_v1_2_44_guard_note"],
            )

            authority_ids = (
                "PROJECT_NORTH_STAR_AND_MVP",
                "PLATFORM_BASELINE",
                "DECISION_REGISTER",
                "ROADMAP",
            )
            for document_id in authority_ids:
                entry = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == document_id
                )
                path = root / entry["repository_path"]
                path.write_text(
                    path.read_text(encoding="utf-8") + "\nStale route: 02_OPEN_WORK_v1.2.44.md\n",
                    encoding="utf-8",
                )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"])
            for document_id in authority_ids:
                entry = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == document_id
                )
                self.assertIn(entry["repository_path"], graph_check["message"])

    def test_archived_open_work_reference_is_allowed_in_current_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            product_entry = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8") + "\nHistorical source: archive/02_OPEN_WORK_v1.2.44.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("PASS", graph_check["status"], graph_check["message"])

    def test_stale_reference_route_rejects_former_integrity_audit_reference_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            product_entry = next(
                item for item in json.loads(manifest_path.read_text(encoding="utf-8"))["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\nStale route: reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"], graph_check["message"])
            self.assertIn(product_entry["repository_path"], graph_check["message"])
            self.assertIn("FOUNDATION_INTEGRITY_AUDIT", graph_check["message"])

    def test_archived_integrity_audit_reference_is_allowed_in_current_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            product_entry = next(
                item for item in json.loads(manifest_path.read_text(encoding="utf-8"))["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\nHistorical evidence: archive/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("PASS", graph_check["status"], graph_check["message"])

    def test_declared_working_navigation_path_is_scanned_for_stale_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            relative = "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("See STALE_MOVED_SOURCE.md for the source.\n", encoding="utf-8")
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)STALE_MOVED_SOURCE\.md"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = []
            manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"] = [relative]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"])
            self.assertIn(relative, graph_check["message"])

    def test_readme_current_authority_order_uses_positions_from_the_readme(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            readme.write_text(
                "\n".join(
                    f"{index}. `{entry['canonical_filename']}`"
                    for index, entry in enumerate(reversed(manifest["governing_documents"]), start=1)
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json")

            order_check = next(
                check for check in report["checks"] if check["name"] == "readme_current_authority_order"
            )
            self.assertEqual("FAIL", order_check["status"])

    def test_frozen_provenance_hash_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            manifest["governing_documents"][0]["provenance_sha256"] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
            path.write_text(path.read_text(encoding="utf-8") + "\nChanged after freeze.\n", encoding="utf-8")
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "frozen_provenance_hash" for finding in report["findings"])
            )

    def test_fad72c1_frozen_artifacts_match_accepted_hashes(self):
        root = Path(__file__).resolve().parents[1]

        for relative, expected_hash in FAD72C1_FROZEN_HASHES.items():
            with self.subTest(path=relative):
                actual_hash = hashlib.sha256((root / relative).read_bytes()).hexdigest()
                self.assertEqual(expected_hash, actual_hash)

    def test_hash_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["sha256"] = "0" * 64
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(finding["check"] == "manifest_hash_parity" for finding in report["findings"])
            )

    def test_unresolved_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nSee OQ-999.\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(finding["check"] == "identifier_resolution" for finding in report["findings"])
            )

    def test_duplicate_definition_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "## DEC-001 — Duplicate\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "duplicate_definitions_dec" for finding in report["findings"])
            )

    def test_missing_roadmap_gate_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace("| OQ-001 |", "| Gate omitted |"),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "roadmap_gate_coverage" for finding in report["findings"])
            )

    def test_duplicate_roadmap_gate_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "## 14.1", "| OQ-001 | Duplicate |\n## 14.1"
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "roadmap_gate_coverage" for finding in report["findings"])
            )

    def test_multiple_domain_owners_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "04_DOMAIN_MAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "| Truth | **Example Domain** |",
                    "| Truth | **Example Domain** and **Other Domain** |",
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "domain_ownership_uniqueness" for finding in report["findings"])
            )

    def test_duplicate_domain_name_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "04_DOMAIN_MAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "## 4. Platform-wide",
                    "| 2 | **Example Domain** | Duplicate |\n## 4. Platform-wide",
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "duplicate_domain_names" for finding in report["findings"])
            )

    def test_missing_current_version_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["semver"] = "9.9.9"
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "manifest_version_parity" for finding in report["findings"])
            )

    def test_document_version_metadata_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "**Document version:** v1.2.1", "**Document version:** v9.9.9"
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "document_version_parity" for finding in report["findings"])
            )

    def test_current_north_star_and_product_self_versions_match_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)

            for document_id, old_version, new_version in (
                ("PROJECT_NORTH_STAR_AND_MVP", "1.2.3", "9.9.9"),
                ("PLATFORM_BASELINE", "1.5.0", "9.9.9"),
            ):
                with self.subTest(document_id=document_id):
                    entry = next(
                        item for item in manifest["governing_documents"]
                        if item["document_id"] == document_id
                    )
                    path = root / entry["repository_path"]
                    path.write_text(
                        path.read_text(encoding="utf-8").replace(
                            f"**Document version:** v{old_version}",
                            f"**Document version:** v{new_version}",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, root / "manifest.json")

                    report = run_audit(
                        root,
                        root / "manifest.json",
                        expected_counts=SMALL_COUNTS,
                    )

                    self.assertTrue(
                        any(
                            finding["check"] == "current_authority_self_version"
                            and finding["path"] == entry["repository_path"]
                            for finding in report["findings"]
                        )
                    )

                    path.write_text(
                        path.read_text(encoding="utf-8").replace(
                            f"**Document version:** v{new_version}",
                            f"**Document version:** v{old_version}",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, root / "manifest.json")

    def test_north_star_governance_self_state_matches_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            north_star = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PROJECT_NORTH_STAR_AND_MVP"
            )
            path = root / north_star["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "governance-alignment condition: MET (v1.2.3)",
                    "governance-alignment condition: MET (v1.2.2)",
                    1,
                ),
                encoding="utf-8",
            )
            refresh_manifest(root, root / "manifest.json")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_self_version"
                    and finding["path"] == north_star["repository_path"]
                    for finding in report["findings"]
                )
            )

    def test_product_current_programme_lifecycle_mirror_is_rejected(self):
        for lifecycle in (
            "NEXT / AUTHORISED / NOT STARTED",
            "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
            "COMPLETE / CERTIFIED",
        ):
            with self.subTest(lifecycle=lifecycle), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = self._write_current_authority_fixture(root)
                product = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == "PLATFORM_BASELINE"
                )
                path = root / product["repository_path"]
                with path.open("a", encoding="utf-8") as file:
                    file.write(f"HARDEN-02 execution is {lifecycle}.\n")
                refresh_manifest(root, root / "manifest.json")

                report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

                self.assertTrue(
                    any(
                        finding["check"] == "current_authority_delegated_routing"
                        and finding["path"] == product["repository_path"]
                        for finding in report["findings"]
                    )
                )

    def test_current_authority_fixture_passes_self_state_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_current_authority_fixture(root)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertEqual(
                {
                    "current_authority_self_version",
                    "current_authority_route_resolution",
                    "current_authority_delegated_routing",
                },
                {
                    check["name"]
                    for check in report["checks"]
                    if check["name"].startswith("current_authority_")
                },
            )

    def test_current_routing_field_must_resolve_to_manifest_routes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            north_star = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PROJECT_NORTH_STAR_AND_MVP"
            )
            path = root / north_star["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "CURRENT_AUTHORITY_MANIFEST",
                    "00_PLATFORM_v1.4.1.md",
                    1,
                ),
                encoding="utf-8",
            )
            refresh_manifest(root, root / "manifest.json")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_route_resolution"
                    and finding["path"] == north_star["repository_path"]
                    for finding in report["findings"]
                )
            )

    def test_unregistered_governing_root_authority_document_fails_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            shutil.copytree(source_docs, root / "docs" / "00_platform")
            manifest_path = root / "docs" / "00_platform" / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            stale_copy = root / "docs" / "00_platform" / "00_PLATFORM_v1.4.1.md"
            archive_copy = root / "docs" / "00_platform" / "archive" / "00_PLATFORM_v1.4.1.md"
            shutil.copyfile(archive_copy, stale_copy)

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "governing_root_exclusivity"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_explicit_current_routes_in_roadmap_atlas_and_harden_resolve_relationally(self):
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        mutations = (
            (
                "roadmap",
                "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
                "PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md",
            ),
            (
                "atlas",
                "00_PLATFORM_v1.8.0.md",
                "00_PLATFORM_v1.5.1.md",
            ),
            (
                "harden_open_work",
                None,
                "02_OPEN_WORK_v1.2.50.md",
            ),
            (
                "open_work_atlas",
                None,
                "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.2.md`",
            ),
        )
        for route_kind, current_route, stale_route in mutations:
            with self.subTest(path=route_kind), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                fixture_docs = root / "docs" / "00_platform"
                shutil.copytree(source_docs, fixture_docs)
                manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                if route_kind == "roadmap":
                    relative = next(
                        entry["repository_path"]
                        for entry in manifest["governing_documents"]
                        if entry["document_id"] == "ROADMAP" and entry.get("lifecycle") == "current"
                    )
                    current_route = "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md"
                elif route_kind == "atlas":
                    atlas = _current_working_path(root, "DELIVERY_ATLAS_WORKING_")
                    relative = atlas.relative_to(root).as_posix()
                    current_route = "00_PLATFORM_v1.9.0.md"
                elif route_kind == "harden_open_work":
                    harden = _current_working_path(root, "HARDEN-02_CONTRACT_WORKING_")
                    relative = harden.relative_to(root).as_posix()
                    current_route = _current_open_work_path(root).name
                else:
                    open_work = _current_open_work_path(root)
                    relative = open_work.relative_to(root).as_posix()
                    current_route = (
                        "ATLAS RECONCILIATION: COMPLETE — current Atlas "
                        f"`{_current_working_route(root, 'DELIVERY_ATLAS_WORKING_')}`"
                    )
                path = root / relative
                text = path.read_text(encoding="utf-8")
                self.assertIn(current_route, text)
                path.write_text(text.replace(current_route, stale_route, 1), encoding="utf-8")
                governing_entry = next(
                    entry
                    for entry in manifest["governing_documents"]
                    if entry["repository_path"] == relative
                ) if not relative.startswith("docs/00_platform/working/") else None
                if governing_entry is not None and "provenance_sha256" in governing_entry:
                    governing_entry["provenance_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
                    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                expected_checks = {"current_authority_route_resolution"}
                if route_kind == "harden_open_work":
                    expected_checks.add("fp001_pmr_reconciliation")
                self.assertTrue(
                    any(
                        finding["check"] in expected_checks
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_current_state_delegated_routing_must_match_readme_and_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            current_open_work = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "OPEN_WORK"
            )["canonical_filename"]
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    current_open_work,
                    "02_OPEN_WORK_v1.2.48.md",
                    1,
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_delegated_routing"
                    for finding in report["findings"]
                )
            )

    def test_refresh_manifest_updates_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text("## DEC-001 — Changed\n## OQ-001 — Example\n", encoding="utf-8")

            refresh_manifest(root, root / "manifest.json")
            manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
            expected_hash = hashlib.sha256(path.read_bytes()).hexdigest()

            self.assertEqual(expected_hash, manifest["governing_documents"][0]["sha256"])

    def _copy_phase7c_audit_fixture(self, root: Path) -> tuple[Path, Path]:
        return self._copy_predecessor_fixture(root)

    def _mutate_phase7c_open_work(
        self,
        root: Path,
        *,
        state_changes: dict | None = None,
        route_replacements: tuple[tuple[str, str], ...] = (),
    ) -> None:
        path = _current_open_work_path(root)
        text = path.read_text(encoding="utf-8")
        if state_changes:
            pattern = re.compile(
                r"(<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*)(.*?)(\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->)",
                re.DOTALL,
            )
            match = pattern.search(text)
            self.assertIsNotNone(match, "Open Work lifecycle JSON is missing")
            state = json.loads(match.group(2))
            state.update(state_changes)
            text = pattern.sub(
                lambda found: found.group(1) + json.dumps(state, indent=2) + found.group(3),
                text,
                count=1,
            )
        active_start = text.index("# 9. Immediate Next Action")
        active_end = text.index("# 10. Minimal Tools", active_start + 1)
        active = text[active_start:active_end]
        for old, new in route_replacements:
            self.assertIn(old, active)
            active = active.replace(old, new, 1)
        path.write_text(text[:active_start] + active + text[active_end:], encoding="utf-8")

    def test_phase7c_current_status_successor_passes_foundation_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _, manifest_path = self._copy_phase7c_audit_fixture(root)

            report = run_audit(root, manifest_path)

            self.assertEqual("PASS", report["status"], report["findings"])
            self.assertEqual([], report["findings"])

    def test_identity_v020_current_status_promotion_passes_foundation_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))

            report = run_audit(root, manifest_path)

            identity_check = next(
                check for check in report["checks"]
                if check["name"] == "identity_v020_current_status_promotion"
            )
            self.assertEqual("PASS", identity_check["status"], identity_check["message"])
            identity_path = root / (
                "docs/00_platform/working/"
                "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
            )
            lifecycle = json.loads(
                re.search(
                    r"```json\s*(\{.*?\})\s*```",
                    identity_path.read_text(encoding="utf-8").split(
                        "<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_START -->", 1
                    )[1].split("<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_END -->", 1)[0],
                    re.DOTALL,
                ).group(1)
            )
            self.assertEqual(
                "AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION UNAUTHORISED",
                lifecycle["phase_8_application_implementation"],
            )
            self.assertEqual("UNAUTHORISED", lifecycle["p8_05_registration_implementation"])

    def test_identity_v020_current_status_promotion_rejects_lifecycle_regression(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            identity_path = root / (
                "docs/00_platform/working/"
                "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
            )
            dossier = identity_path.read_text(encoding="utf-8")
            marker = "<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_START -->"
            end_marker = "<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_END -->"
            start = dossier.index(marker)
            end = dossier.index(end_marker, start)
            region = dossier[start:end]
            payload_match = re.search(r"```json\s*(\{.*?\})\s*```", region, re.DOTALL)
            self.assertIsNotNone(payload_match, "Identity v0.2.0 lifecycle JSON is missing")
            lifecycle = json.loads(payload_match.group(1))
            lifecycle["identity_lifecycle"] = "CANDIDATE / CERTIFICATION PENDING / NOT CURRENT"
            region = region[:payload_match.start(1)] + json.dumps(lifecycle, indent=2) + region[payload_match.end(1):]
            identity_path.write_text(dossier[:start] + region + dossier[end:], encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            identity_check = next(
                check for check in report["checks"]
                if check["name"] == "identity_v020_current_status_promotion"
            )
            self.assertEqual("FAIL", identity_check["status"], identity_check["message"])

    def test_identity_v020_current_status_promotion_rejects_broad_implementation_regression(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            identity_path = root / (
                "docs/00_platform/working/"
                "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
            )
            dossier = identity_path.read_text(encoding="utf-8")
            start = dossier.index("<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_START -->")
            end = dossier.index("<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_END -->", start)
            region = dossier[start:end]
            payload_match = re.search(r"```json\s*(\{.*?\})\s*```", region, re.DOTALL)
            self.assertIsNotNone(payload_match)
            lifecycle = json.loads(payload_match.group(1))
            lifecycle["phase_8_application_implementation"] = "UNAUTHORISED"
            region = region[:payload_match.start(1)] + json.dumps(lifecycle, indent=2) + region[payload_match.end(1):]
            identity_path.write_text(dossier[:start] + region + dossier[end:], encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            identity_check = next(
                check for check in report["checks"]
                if check["name"] == "identity_v020_current_status_promotion"
            )
            self.assertEqual("FAIL", identity_check["status"], identity_check["message"])

    def test_phase7c_foundation_integrity_rejects_candidate_mutations(self):
        candidate_rel = "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"

        def replace_in_candidate(old: str, new: str, *, section: str | None = None, count: int = 1):
            def mutate(root: Path) -> None:
                path = root / candidate_rel
                text = path.read_text(encoding="utf-8")
                if section is not None:
                    start = text.index(section)
                    level = len(section) - len(section.lstrip("#"))
                    heading_end = start + len(section)
                    next_heading = re.search(
                        rf"(?m)^#{{1,{level}}}[ \t]+",
                        text[heading_end:],
                    )
                    end = heading_end + next_heading.start() if next_heading else len(text)
                    block = text[start:end]
                    self.assertIn(old, block)
                    text = text[:start] + block.replace(old, new, 1) + text[end:]
                else:
                    self.assertIn(old, text)
                    text = text.replace(old, new, count)
                path.write_text(text, encoding="utf-8")
            return mutate

        def premature_phase7c_completion(root: Path) -> None:
            self._mutate_phase7c_open_work(
                root,
                state_changes={"phase_7c": "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"},
                route_replacements=((
                    "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
                    "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
                ),),
            )

        def phase7b_prerequisite_regression(root: Path) -> None:
            self._mutate_phase7c_open_work(
                root,
                state_changes={"phase_7b_reconciliation": "IN PROGRESS"},
                route_replacements=((
                    "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
                    "PHASE 7B RECONCILIATION: IN PROGRESS",
                ),),
            )

        def remove_oq029_stop(root: Path) -> None:
            sentence = "If any contract clause requires a numeric or exact retention duration required by legal authority but absent from current authority, STOP and route the missing authority before claiming the contract complete."
            replace_in_candidate(
                sentence,
                "Retention questions remain on their applicable downstream authority routes.",
                section="## V. Downstream gates",
            )(root)

        def remove_architectural_proof_obligation(root: Path) -> None:
            replace_in_candidate(
                "registration-to-verification-to-login",
                "registration-to-login",
                section="## P. Architectural proof requirement",
            )(root)

        def remove_vertical_slice_outcome(root: Path) -> None:
            replace_in_candidate(
                "Public entry to verified individual Account",
                "Public entry",
                section="## Q. Vertical Slice map",
            )(root)

        def remove_hardening_obligation(root: Path) -> None:
            replace_in_candidate(
                "Concurrency/idempotency",
                "concurrency only",
                section="## R. Horizontal hardening requirements",
            )(root)

        def remove_performance_pressure(root: Path) -> None:
            replace_in_candidate(
                "OQ-035",
                "threshold decision pending",
                section="## S. Performance envelope",
            )(root)

        def remove_extension_boundary(root: Path) -> None:
            replace_in_candidate(
                "Social login",
                "optional identity extension",
                section="## T. Future extension hooks",
            )(root)

        def alter_reconciliation_archive(root: Path) -> None:
            path = root / "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
            path.write_bytes(path.read_bytes() + b"\nmutation\n")

        def reintroduce_retired_current_paths(root: Path) -> None:
            docs = root / "docs" / "00_platform"
            for archived, current in (
                ("archive/02_OPEN_WORK_v1.2.70.md", "02_OPEN_WORK_v1.2.70.md"),
                ("archive/DELIVERY_ATLAS_WORKING_v0.4.14.md", "working/DELIVERY_ATLAS_WORKING_v0.4.12.md"),
                ("archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.14.md", "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.14.md"),
                ("archive/HARDEN-02_CONTRACT_WORKING_v0.5.14.md", "working/HARDEN-02_CONTRACT_WORKING_v0.5.14.md"),
            ):
                shutil.copyfile(docs / archived, docs / current)

        mutations = (
            (
                "premature certification",
                replace_in_candidate("CANDIDATE\nNOT CERTIFIED\nNOT CURRENT", "CANDIDATE\nCERTIFIED\nCURRENT"),
                "fp001_phase7c_candidate_lifecycle",
            ),
            ("premature Phase 7C completion", premature_phase7c_completion, "fp001_phase8_proof_contract_lifecycle"),
            (
                "premature proof selection",
                replace_in_candidate("PROOF CLASSIFICATION: NOT FINALISED", "PROOF CLASSIFICATION: NEW_TRACER_BULLET"),
                "fp001_phase7c_candidate_downstream_gates",
            ),
            (
                "premature Phase 8 authorisation",
                replace_in_candidate(
                    "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
                    "PHASE 8: AUTHORISED",
                ),
                "fp001_phase7c_candidate_downstream_gates",
            ),
            (
                "affected Domain drift",
                replace_in_candidate("Analytics", "Future Domain", section="### Six affected Domains"),
                "fp001_phase7c_candidate_scope",
            ),
            (
                "material capability drift",
                replace_in_candidate("CAP-028", "CAP-029", section="### Material capability relationships"),
                "fp001_phase7c_candidate_scope",
            ),
            (
                "dossier disposition drift",
                replace_in_candidate(
                    "| Identity & Access | REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4 |",
                    "| Identity & Access | NOT_REQUIRED |",
                    section="### Required dossier dispositions",
                ),
                "fp001_phase7c_candidate_scope",
            ),
            ("Phase 7B prerequisite regression", phase7b_prerequisite_regression, "fp001_phase8_proof_contract_lifecycle"),
            ("OQ-029 STOP removal", remove_oq029_stop, "fp001_phase7c_candidate_downstream_gates"),
            ("architectural proof obligation removal", remove_architectural_proof_obligation, "fp001_phase7c_candidate_delivery_dimensions"),
            ("Vertical Slice outcome removal", remove_vertical_slice_outcome, "fp001_phase7c_candidate_delivery_dimensions"),
            ("horizontal-hardening obligation removal", remove_hardening_obligation, "fp001_phase7c_candidate_delivery_dimensions"),
            ("performance pressure removal", remove_performance_pressure, "fp001_phase7c_candidate_delivery_dimensions"),
            ("future extension boundary removal", remove_extension_boundary, "fp001_phase7c_candidate_delivery_dimensions"),
            ("immutable reconciliation mutation", alter_reconciliation_archive, "fp001_phase7c_candidate_immutable_inputs"),
            ("retired current-path reintroduction", reintroduce_retired_current_paths, "fp001_phase7c_candidate_current_routes"),
        )

        for name, mutate, expected_check in mutations:
            with self.subTest(mutation=name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                _, manifest_path = self._copy_phase7c_audit_fixture(root)
                mutate(root)
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertEqual("FAIL", report["status"], report["findings"])
                self.assertTrue(
                    any(finding["check"] == expected_check for finding in report["findings"]),
                    report["findings"],
                )

    def _write_clean_fixture(self, root: Path) -> dict:
        files = {
            "docs/00_platform/01_DECISIONS_v1.2.1.md": (
                "- **Document version:** v1.2.1\n"
                "## DEC-001 — Example\n"
                "## OQ-001 — Example\n"
            ),
            "docs/00_platform/05_ROADMAP_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "# 14. Gate schedule\n"
                "| OQ-001 | Example |\n"
                "## 14.1 Non-OQ expert/vendor gates\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md": (
                "- **Document version:** v0.35.0\n"
                "## ARC-001 — Example\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "### ARQ-TEST-001 — Example\n"
            ),
            "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": (
                "- **Document version:** v0.2.0\n"
                "# 3. FLOW-01 — Example\n"
            ),
            "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "## 3. Approved domain set\n"
                "| 1 | **Example Domain** | Example |\n"
                "## 4. Platform-wide business-truth ownership matrix\n"
                "| Business truth | Authoritative domain | Dependents | Rule |\n"
                "| Truth | **Example Domain** | None | READ |\n"
                "### 4.1 Ownership interpretation\n"
            ),
        }

        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        manifest = {
            "governing_documents": [],
            "reference_documents": [],
            "historical_documents": [],
            "integrity_rules": {
                "document_roots": {
                    "governing": "docs/00_platform",
                    "reference": "docs/00_platform/reference",
                    "historical": "docs/00_platform/archive",
                    "context_index": "docs/00_platform/README.md",
                },
                "expected_counts": SMALL_COUNTS,
                "contiguous_ranges": {
                    "DEC": {"prefix": "DEC", "start": 1, "end": 1, "width": 3},
                    "OQ": {"prefix": "OQ", "start": 1, "end": 1, "width": 3},
                    "ARC": {"prefix": "ARC", "start": 1, "end": 1, "width": 3},
                    "FLOW": {"prefix": "FLOW", "start": 1, "end": 1, "width": 2},
                },
                "definition_sources": {
                    "decisions": "DECISION_REGISTER",
                    "architecture_law": "ARCHITECTURE_LAW_EVIDENCE",
                    "architecture_requirements": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
                    "reference_flows": "REFERENCE_FLOW_EVIDENCE",
                    "roadmap": "ROADMAP",
                    "domain_map": "DOMAIN_LAW",
                },
                "graph_rules": {
                    "stale_reference_patterns": [],
                    "reference_header_lines": 35,
                    "frozen_provenance_policy": "frozen_provenance",
                    "navigation_document_ids": ["ROADMAP"],
                },
            },
        }
        authority_classes = {
            "01_DECISIONS_v1.2.1.md": "DECISION_REGISTER",
            "05_ROADMAP_v1.0.0.md": "ROADMAP",
            "ARCHITECTURE_LAW_WORKING_v0.35.0.md": "ARCHITECTURE_LAW_EVIDENCE",
            "ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "REFERENCE_FLOW_EVIDENCE",
            "04_DOMAIN_MAP_v1.0.0.md": "DOMAIN_LAW",
        }
        document_ids = {
            "01_DECISIONS_v1.2.1.md": "DECISION_REGISTER",
            "05_ROADMAP_v1.0.0.md": "ROADMAP",
            "ARCHITECTURE_LAW_WORKING_v0.35.0.md": "ARCHITECTURE_LAW_EVIDENCE",
            "ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "REFERENCE_FLOW_EVIDENCE",
            "04_DOMAIN_MAP_v1.0.0.md": "DOMAIN_LAW",
        }
        for relative in files:
            path = root / relative
            manifest["governing_documents"].append(
                {
                    "document_id": document_ids[path.name],
                    "canonical_filename": path.name,
                    "semver": path.name.split("_v", 1)[1][:-3],
                    "repository_path": relative,
                    "authority_class": authority_classes[path.name],
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                }
            )

        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest

    def _write_current_authority_fixture(self, root: Path) -> dict:
        manifest = self._write_clean_fixture(root)
        files = {
            "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": (
                "# PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md\n"
                "- **Document version:** v1.2.3\n"
                "# 23. Current Planning Position\n"
                "Current Product/Decision/Roadmap authority is routed by README and CURRENT_AUTHORITY_MANIFEST. README and current Open Work own the active programme stage and NEXT route.\n"
                "# 24. Document Stop Condition\n"
                "**Current Product Law / governance-alignment condition: MET (v1.2.3).**\n"
                "**Implementation STOP:** planning gates remain mandatory.\n"
            ),
            "docs/00_platform/00_PLATFORM_v1.5.0.md": (
                "# 00_PLATFORM_v1.5.0.md\n"
                "- **Document version:** v1.5.0\n"
                "# 24. Current Planning Stop Condition\n"
                "Current Product Law is v1.5.0. This Product Law does not execute HARDEN-02 or authorise implementation. README and current Open Work own current programme routing and lifecycle status.\n"
            ),
            "docs/00_platform/02_OPEN_WORK_v1.0.0.md": (
                "# 02_OPEN_WORK_v1.0.0.md\n"
                "- **Document version:** v1.0.0\n"
            ),
            "docs/00_platform/README.md": (
                "## Default Agent Context\n"
                "1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`\n"
                "2. `00_PLATFORM_v1.5.0.md`\n"
                "3. `01_DECISIONS_v1.2.1.md`\n"
                "4. `02_OPEN_WORK_v1.0.0.md`\n"
                "5. `05_ROADMAP_v1.0.0.md`\n"
                "\n## Active Working Artifacts\n"
            ),
        }
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        authority_classes = {
            "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": "PRODUCT_NORTH_STAR",
            "00_PLATFORM_v1.5.0.md": "PLATFORM_PRODUCT_LAW",
            "02_OPEN_WORK_v1.0.0.md": "PLANNING_TRACKER",
        }
        document_ids = {
            "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": "PROJECT_NORTH_STAR_AND_MVP",
            "00_PLATFORM_v1.5.0.md": "PLATFORM_BASELINE",
            "02_OPEN_WORK_v1.0.0.md": "OPEN_WORK",
        }
        for relative in files:
            path = root / relative
            if path.name == "README.md":
                continue
            manifest["governing_documents"].append(
                {
                    "document_id": document_ids[path.name],
                    "canonical_filename": path.name,
                    "semver": path.name.split("_v", 1)[1][:-3],
                    "repository_path": relative,
                    "authority_class": authority_classes[path.name],
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                }
            )
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest


if __name__ == "__main__":
    unittest.main()
