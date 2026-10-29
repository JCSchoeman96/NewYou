from __future__ import annotations

import hashlib
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest, run_audit
from foundation_test_support import (
    WELL38_BASE_SHA,
    git_changed_paths,
    copy_git_snapshot_tree,
    current_document_path,
    current_working_path,
    historical_snapshot_path,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
BASE_SHA = "675a8c50ac53a995a48e4d262df42065f8ccd412"
# The v1.2.77-era assertions below certify the archived transition snapshot.
OPEN_WORK = historical_snapshot_path(ROOT, "02_OPEN_WORK_v1.2.77.md")
CONTRACT = DOCS / "working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
CONTRACT_ARCHIVE = DOCS / "archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
ATLAS = historical_snapshot_path(ROOT, "DELIVERY_ATLAS_WORKING_v0.4.19.md")
ATLAS_V416_ARCHIVE = DOCS / "archive/DELIVERY_ATLAS_WORKING_v0.4.16.md"
ATLAS_V417_ARCHIVE = DOCS / "archive/DELIVERY_ATLAS_WORKING_v0.4.17.md"
SKELETON = historical_snapshot_path(ROOT, "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md")
SKELETON_V117_ARCHIVE = DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md"
SKELETON_V118_ARCHIVE = DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md"
SKELETON_V119_ARCHIVE = DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.19.md"
SKELETON_V120_ARCHIVE = DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.20.md"
ATLAS_V418_ARCHIVE = DOCS / "archive/DELIVERY_ATLAS_WORKING_v0.4.18.md"
HARDEN = historical_snapshot_path(ROOT, "HARDEN-02_CONTRACT_WORKING_v0.5.21.md")
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
HARD_STOP_CHECK = "fp001_development_entry_hard_stop_lifecycle"
SOURCE_FAILURE = "executable application/bootstrap source present while application implementation is not authorised"

PREDECESSORS = (
    (
        "docs/00_platform/02_OPEN_WORK_v1.2.74.md",
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md",
    ),
    (
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.16.md",
    ),
    (
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
    ),
    (
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
    ),
)

# Phrases that describe the pre-hard-stop state. They must not appear in CURRENT
# sections. Historical sections (predecessor records, freeze-time text) may keep them.
PRE_HARD_STOP_CURRENT_PATTERNS = (
    r"CONDITION 9",
    r"NOT EVALUATED",
    r"DEVELOPMENT ENTRY HARD STOP EVALUATION: NEXT",
    r"NEXT GOVERNANCE ACTION: DEVELOPMENT ENTRY HARD STOP",
    r"Phase 8[^.\n]{0,40}UNAUTHORISED",
    r"APPLICATION IMPLEMENTATION: UNAUTHORISED",
    r"remains UNAUTHORISED",
    r"UNAUTHORISED UNTIL",
)


def _marked_json(text: str, start: str, end: str) -> dict:
    match = re.search(re.escape(start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(end), text, re.DOTALL)
    return json.loads(match.group(1)) if match else {}


def _rewrite_marked_json(path: Path, start: str, end: str, updates: dict) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.search(re.escape(start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(end), text, re.DOTALL)
    assert match, "lifecycle state block not found"
    data = json.loads(match.group(1))
    data.update(updates)
    replacement = f"{start}\n```json\n{json.dumps(data, indent=2, ensure_ascii=False)}\n```\n{end}"
    path.write_text(text[: match.start()] + replacement + text[match.end():], encoding="utf-8")


def _between(text: str, start_marker: str, end_marker: str) -> str:
    start = text.index(start_marker)
    end = text.index(end_marker, start + len(start_marker))
    return text[start:end]


def _md_section(text: str, heading_prefix: str) -> str:
    """Return one level-2 markdown section (heading through the line before the next `## ` heading)."""
    lines = text.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.startswith(heading_prefix))
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return "".join(lines[start:end])


def _contract_section_p(text: str) -> str:
    return text.split("## P. Architectural proof requirement", 1)[1].split("## Q. Vertical Slice map", 1)[0]


def _pre_hard_stop_hits(text: str) -> list[str]:
    return [pattern for pattern in PRE_HARD_STOP_CURRENT_PATTERNS if re.search(pattern, text)]


def _hard_stop_check(report: dict) -> dict:
    return next(check for check in report["checks"] if check["name"] == HARD_STOP_CHECK)


SYNTHETIC_SOURCE_FILES = {
    "mix.exs": 'defmodule NewYou.MixProbe.MixProject do\n  use Mix.Project\nend\n',
    "lib/newyou/synthetic_probe.ex": "defmodule NewYou.SyntheticProbe do\n  def ping, do: :ok\nend\n",
}


class FP001DevelopmentEntryHardStopPromotionTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Current route state
    # ------------------------------------------------------------------
    def test_historical_open_work_hard_stop_pass_authorises_bounded_phase8_only(self):
        text = OPEN_WORK.read_text(encoding="utf-8")
        state = _marked_json(
            text,
            "<!-- HARDEN_02_LIFECYCLE_STATE_START -->",
            "<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        )
        self.assertEqual("PASS / ALL 10 CONDITIONS SATISFIED", state.get("development_entry_hard_stop_status"))
        self.assertEqual("SATISFIED", state.get("development_entry_hard_stop_conditions_1_through_10"))
        self.assertEqual("AUTHORISED", state.get("phase8"))
        self.assertEqual("AUTHORISED", state.get("application_implementation"))
        self.assertEqual("NEW_TRACER_BULLET", state.get("proof_classification"))
        self.assertEqual("NOT SELECTED", state.get("reuse_existing_proof"))
        self.assertEqual("REQUIRED / DEFINED AS REVIEW CANDIDATE", state.get("tracer_bullet"))
        self.assertEqual("TB-001", state.get("tracer_bullet_id"))
        self.assertEqual("NOT STARTED", state.get("architectural_proof_execution"))
        self.assertEqual("TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION", state.get("next_governance_action"))

        active = text.split("# 9. Immediate Next Action", 1)[1].split("# 10. Minimal Tools", 1)[0]
        for token in (
            "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
            "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
            "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
        ):
            self.assertIn(token, active)
        self.assertNotRegex(active, r"\bTB-(?!001\b)\d{3,}\b")

    def test_contract_header_reflects_hard_stop_without_changing_frozen_section_p(self):
        text = CONTRACT.read_text(encoding="utf-8")
        header = text.split("## A. Identity and provenance", 1)[0]
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", header)
        self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", header)
        proof_section = _contract_section_p(text)
        # Section P is frozen freeze-time text: NOT FINALISED remains correct there.
        self.assertIn("The proof vehicle and final proof classification remain NOT FINALISED.", proof_section)
        self.assertEqual(
            "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
            hashlib.sha256(CONTRACT_ARCHIVE.read_bytes()).hexdigest(),
        )

    def test_predecessor_archives_are_byte_identical(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        historical_documents = {
            entry.get("repository_path"): entry
            for entry in manifest["historical_documents"]
            if isinstance(entry, dict)
        }
        for _current_rel, archive_rel in PREDECESSORS:
            archive = ROOT / archive_rel
            self.assertTrue(archive.is_file(), archive_rel)
            entry = historical_documents.get(archive_rel)
            self.assertIsNotNone(entry, f"historical archive is not registered: {archive_rel}")
            self.assertEqual("historical", entry.get("lifecycle"), archive_rel)
            digest = hashlib.sha256(archive.read_bytes()).hexdigest()
            self.assertEqual(entry.get("sha256"), digest, archive_rel)
            self.assertEqual(entry.get("provenance_sha256"), digest, archive_rel)

    def test_manifest_pins_hard_stop_lifecycle(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        rule = manifest["integrity_rules"]["fp001_development_entry_hard_stop_lifecycle"]
        self.assertEqual(BASE_SHA, rule["base_sha"])
        self.assertEqual("AUTHORISED", rule["phase8"])
        self.assertEqual("AUTHORISED", rule["application_implementation"])
        self.assertNotIn("synthetic_authorization_fixture_relative_path", rule)
        open_work_entry = next(e for e in manifest["governing_documents"] if e["document_id"] == "OPEN_WORK")
        self.assertEqual(current_document_path(ROOT, "OPEN_WORK").name, open_work_entry["canonical_filename"])
        self.assertEqual(
            open_work_entry["semver"],
            re.search(r"v(\d+\.\d+\.\d+)", open_work_entry["canonical_filename"]).group(1),
        )
        current_open_work = current_document_path(ROOT, "OPEN_WORK").read_text(encoding="utf-8")
        predecessor_match = re.search(r"(?m)^- \*\*Predecessor:\*\* `archive/02_OPEN_WORK_v([\d.]+)\.md`", current_open_work)
        self.assertIsNotNone(predecessor_match)
        self.assertEqual(predecessor_match.group(1), open_work_entry["superseded_version"])

    def test_foundation_integrity_rejects_reverted_hard_stop_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(DOCS, root / "docs" / "00_platform")
            shutil.copytree(ROOT / "tests", root / "tests", ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copytree(ROOT / "tools", root / "tools", ignore=shutil.ignore_patterns("__pycache__"))
            open_work = current_document_path(root, "OPEN_WORK")
            text = open_work.read_text(encoding="utf-8")
            open_work.write_text(
                text.replace("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", "DEVELOPMENT ENTRY HARD STOP: FAIL", 1),
                encoding="utf-8",
            )
            report = run_audit(root, root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
            phase8_check = next(
                check for check in report["checks"]
                if check["name"] == "phase8_approved_status_successor_current"
            )
            self.assertEqual("FAIL", report["status"])
            self.assertEqual("FAIL", phase8_check["status"])

    # ------------------------------------------------------------------
    # Application-source guard: authorisation-conditional, state-derived
    # ------------------------------------------------------------------
    def _synthetic_repo(self, root: Path, *, historical: bool = False) -> Path:
        for name in ("docs", "tests", "tools"):
            shutil.copytree(ROOT / name, root / name, ignore=shutil.ignore_patterns("__pycache__"))
        if historical:
            shutil.rmtree(root / "docs" / "00_platform")
            copy_git_snapshot_tree(ROOT, WELL38_BASE_SHA, root, "docs/00_platform")
        for relative, content in SYNTHETIC_SOURCE_FILES.items():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        return root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

    def test_review_pending_state_blocks_synthetic_application_source(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = self._synthetic_repo(Path(directory), historical=True)
            report = run_audit(Path(directory), manifest)
            check = next(
                item for item in report["checks"]
                if item["name"] == "fp001_phase8_proof_contract_lifecycle"
            )
            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn("application implementation source exists before TB-001 contract approval and execution start", check["message"])

    def test_unauthorised_state_rejects_identical_synthetic_source(self):
        scenarios = {
            "manifest_rule_phase8_unauthorised": ("rule", {"phase8": "UNAUTHORISED"}),
            "manifest_rule_application_unauthorised": (
                "rule",
                {"application_implementation": "UNAUTHORISED"},
            ),
            "open_work_phase8_unauthorised": ("state", {"phase8": "UNAUTHORISED"}),
            "open_work_application_unauthorised": (
                "state",
                {"application_implementation": "UNAUTHORISED"},
            ),
            "both_unauthorised": (
                "both",
                {"phase8": "UNAUTHORISED", "application_implementation": "UNAUTHORISED"},
            ),
        }
        for label, (mode, updates) in scenarios.items():
            with self.subTest(scenario=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = self._synthetic_repo(root, historical=True)
                if mode in ("rule", "both"):
                    data = json.loads(manifest.read_text(encoding="utf-8"))
                    rule = data["integrity_rules"]["fp001_development_entry_hard_stop_lifecycle"]
                    rule.update(updates)
                    manifest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                if mode in ("state", "both"):
                    _rewrite_marked_json(
                        current_document_path(root, "OPEN_WORK"),
                        "<!-- HARDEN_02_LIFECYCLE_STATE_START -->",
                        "<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
                        updates,
                    )
                refresh_manifest(root, manifest)
                report = run_audit(root, manifest)
                check = next(
                    item for item in report["checks"]
                    if item["name"] == "fp001_phase8_proof_contract_lifecycle"
                )
                self.assertEqual("FAIL", check["status"], label)
                self.assertIn("application implementation source exists before TB-001 contract approval and execution start", check["message"], label)

    def test_foundation_integrity_rejects_stale_current_atlas_jit_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._synthetic_repo(root)
            atlas_path = current_working_path(root, "DELIVERY_ATLAS_WORKING_")
            atlas = atlas_path.read_text(encoding="utf-8")
            current = (
                "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS. "
                "PROOF EXECUTION: NOT STARTED."
            )
            stale = (
                "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS. "
                "PROOF EXECUTION: COMPLETE."
            )
            self.assertIn(current, atlas)
            atlas_path.write_text(atlas.replace(current, stale, 1), encoding="utf-8")
            refresh_manifest(root, manifest)
            manifest_data = json.loads(manifest.read_text(encoding="utf-8"))
            hard_stop_rule = manifest_data["integrity_rules"]["fp001_development_entry_hard_stop_lifecycle"]
            for relative in hard_stop_rule["current_route_sha256"]:
                hard_stop_rule["current_route_sha256"][relative] = hashlib.sha256(
                    (root / relative).read_bytes()
                ).hexdigest()
            manifest.write_text(json.dumps(manifest_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            report = run_audit(root, manifest)
            check = next(
                item for item in report["checks"]
                if item["name"] == "phase8_approved_status_successor_current"
            )
            self.assertEqual("FAIL", check["status"], check["message"])
            self.assertIn(
                "Phase 8 current-route SHA-256 differs: " + atlas_path.relative_to(root).as_posix(),
                check["message"],
            )

    def test_pr_scope_base_to_candidate_adds_no_application_source(self):
        """Scope record for PR #131 only: the promotion itself adds no executable application source."""
        # PR #131 resulting main is recorded in the approved TB-001 contract.
        changed = git_changed_paths(ROOT, BASE_SHA, "0972864ef7f4638c96198e19a13977e0151e9726")
        self.assertTrue(changed, "base-to-candidate diff unexpectedly empty")
        source_like = [
            path
            for path in changed
            if path == "mix.exs"
            or path.endswith((".ex", ".exs"))
            or set(Path(path).parts) & {"lib", "src", "app", "apps", "priv", "migrations", "assets"}
        ]
        self.assertEqual([], source_like)

    # ------------------------------------------------------------------
    # Section-aware current versus historical status
    # ------------------------------------------------------------------
    def test_skeleton_direct_predecessor_is_v0_1_20(self):
        text = SKELETON.read_text(encoding="utf-8")
        self.assertIn("**Artifact version:** v0.1.21", text)
        self.assertIn(
            "Direct predecessor v0.1.20 is preserved byte-identically at archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.20.md.",
            text,
        )
        self.assertNotIn("Direct predecessor v0.1.18", text)
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        archive_rel = "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.20.md"
        entry = next(
            (
                item for item in manifest["historical_documents"]
                if item.get("repository_path") == archive_rel
            ),
            None,
        )
        self.assertIsNotNone(entry, "historical Skeleton v0.1.20 archive is not registered")
        self.assertEqual("historical", entry.get("lifecycle"))
        expected = entry["sha256"]
        self.assertEqual(expected, entry.get("provenance_sha256"))
        self.assertEqual(expected, hashlib.sha256(SKELETON_V120_ARCHIVE.read_bytes()).hexdigest())

    def test_historical_skeleton_successor_status_is_pass_bounded_and_not_pre_hard_stop(self):
        text = SKELETON.read_text(encoding="utf-8")
        current_body = text.split("## v0.1.13 current-route status (historical predecessor)", 1)[0]
        self.assertEqual([], _pre_hard_stop_hits(current_body))
        current_v0118 = _md_section(text, "## v0.1.21 — TB-001 proof-contract successor candidate route (current)")
        for token in (
            "identifier TB-001",
            "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
            "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
            "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
            "PROOF EXECUTION: NOT STARTED",
            "PROOF RESULT: NOT STARTED",
            "PROOF CERTIFICATION: NOT STARTED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        ):
            self.assertIn(token, current_v0118)
        self.assertIn("Phase 9", current_body)
        self.assertIn("confers no Phase 8 authority", current_body)
        self.assertIn("Open Work v1.2.77", current_body)
        self.assertIn("NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION", current_body)

    def test_skeleton_historical_sections_match_archived_v0_1_17(self):
        text = SKELETON.read_text(encoding="utf-8")
        archive = SKELETON_V117_ARCHIVE.read_text(encoding="utf-8")
        for heading in ("## v0.1.15 current-route status", "## v0.1.16 current-route status"):
            self.assertEqual(
                _md_section(archive, heading),
                _md_section(text, heading),
                heading,
            )
        self.assertIn("PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED", _md_section(text, "## v0.1.15 current-route status"))
        self.assertIn("PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED", _md_section(text, "## v0.1.16 current-route status"))
        v117 = _md_section(text, "## v0.1.17 current-route status (historical predecessor)")
        self.assertEqual(
            _md_section(archive, "## v0.1.17 current-route status").split("\n", 1)[1].rstrip(),
            v117.split("\n", 1)[1].rstrip(),
        )
        self.assertIn("PHASE 8: UNAUTHORISED", v117)

    def test_atlas_transition_v0_4_18_to_v0_4_19(self):
        text = ATLAS.read_text(encoding="utf-8")
        self.assertIn("# Delivery Atlas working v0.4.19", text)
        self.assertIn("`v0.4.18 → v0.4.19`", text)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.4.18.md", text)
        self.assertIn("TB-001 proof-contract successor", text)
        self.assertNotIn("routes the next action to Development Entry Hard Stop evaluation", text.split("## v0.4.16 Patch Scope", 1)[0])
        self.assertIn("DOES NOT AUTHORISE IMPLEMENTATION", text)
        self.assertIn("DERIVED", text)
        self.assertIn("NON-AUTHORITATIVE", text)
        prior_route = ATLAS_V417_ARCHIVE.read_text(encoding="utf-8")
        self.assertIn("`v0.4.16 → v0.4.17`", prior_route)
        self.assertIn("TB-001 proof contract", prior_route)
        self.assertEqual(
            "9636c1ed2a12f156ebeb31004e0d3823f7e2824b55d9e7107646d8178f5eab32",
            hashlib.sha256(ATLAS_V416_ARCHIVE.read_bytes()).hexdigest(),
        )

    def test_atlas_patch_scope_sections_restore_history(self):
        text = ATLAS.read_text(encoding="utf-8")
        archive = ATLAS_V416_ARCHIVE.read_text(encoding="utf-8")
        self.assertIn("## v0.4.16 Patch Scope", text)
        self.assertEqual(
            _md_section(archive, "## v0.4.9 Patch Scope"),
            _md_section(text, "## v0.4.9 Patch Scope"),
        )
        self.assertIn("Development Entry Hard Stop PASS", _md_section(text, "## v0.4.16 Patch Scope"))

    def test_historical_atlas_successor_status_has_no_contradictory_authorisation(self):
        text = ATLAS.read_text(encoding="utf-8")
        header = text.split("## v0.4.16 Patch Scope", 1)[0]
        current = _md_section(text, "## 26.25 FP-001 Phase 8 TB-001 successor candidate route (current)")
        jit_boundary = _between(text, "**JIT Boundary:**", "\n### CAP-002")
        self.assertEqual([], _pre_hard_stop_hits(header))
        self.assertEqual([], _pre_hard_stop_hits(current))
        for token in (
            "identifier TB-001",
            "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
            "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
            "PROOF EXECUTION: NOT STARTED",
            "PROOF RESULT: NOT STARTED",
            "PROOF CERTIFICATION: NOT STARTED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "next governance action is TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
        ):
            self.assertIn(token, current)
        self.assertNotIn("PHASE 8: UNAUTHORISED", current)
        self.assertIn("does not authorize implementation", current)
        self.assertEqual([], _pre_hard_stop_hits(jit_boundary))
        self.assertIn("Development Entry Hard Stop", jit_boundary)
        self.assertIn("Phase 8 remains authorised only for the bounded architectural proof after candidate approval", jit_boundary)
        # Historical records keep their freeze-time state.
        self.assertIn("UNAUTHORISED", _md_section(text, "## 26.20 Phase 7C tracker closure routing"))
        self.assertIn("UNAUTHORISED", _md_section(text, "## 26.21 FP-001 architectural proof classification route (historical predecessor)"))

    def test_historical_harden_sections_do_not_project_pre_hard_stop_state(self):
        text = HARDEN.read_text(encoding="utf-8")
        section_18 = _between(text, "## 18. Downstream consequence", "## 19. Explicit exclusion confirmations")
        section_23 = _between(text, "## 23. FP-001 Phase 7B reconciliation current route", "## 24. FP-001 Phase 7C tracker closure")
        i07 = _between(text, "### I-07 — Phase 7C readiness fail-closed", "### I-08 — Proof classification timing")
        for label, block in (("section 18", section_18), ("section 23", section_23), ("I-07", i07)):
            with self.subTest(block=label):
                self.assertEqual([], _pre_hard_stop_hits(block))
        self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", section_18)
        self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", section_23)
        self.assertIn("HARDEN-02 itself confers no implementation authority", i07)
        self.assertIn("current Open Work v1.2.77 separately records bounded Phase 8 authorisation", i07)
        self.assertNotIn("satisfies only Development Entry Hard Stop condition 9", i07)
        self.assertIn(
            "Current Open Work v1.2.77 routes TB-001 for contract review; proof execution waits for approval of the task contract.",
            section_18,
        )

    def test_historical_harden_predecessor_and_section_20_authority_are_unambiguous(self):
        text = HARDEN.read_text(encoding="utf-8")
        header = text.split("### Revision log", 1)[0]
        section_20 = _md_section(text, "## 20. Contract-stage STOP")

        self.assertIn(
            "- **Immediate predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.20.md`",
            header,
        )
        self.assertNotRegex(
            header,
            r"(?im)^-\s*\*\*(?:current|direct|immediate) predecessor:\*\*[^\n]*v0\.5\.15\.md",
        )
        self.assertIn("No application implementation is authorised by HARDEN-02 itself.", section_20)
        self.assertIn(
            "Current Open Work v1.2.77 separately records application implementation as AUTHORISED only inside the bounded Phase 8 / NEW_TRACER_BULLET architectural-proof stage.",
            section_20,
        )
        self.assertNotRegex(section_20, r"(?i)\bNo application implementation is authorised\.(?:\s|$)")

    def test_harden_historical_pre_classification_record_is_preserved(self):
        text = HARDEN.read_text(encoding="utf-8")
        historical = _between(text, "## 24. FP-001 Phase 7C tracker closure", "## 25. FP-001 architectural proof classification current status")
        self.assertIn("(historical pre-classification status)", historical)
        self.assertIn("PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED", historical)


if __name__ == "__main__":
    unittest.main()
