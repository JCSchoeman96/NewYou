from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
BASE_SHA = "675a8c50ac53a995a48e4d262df42065f8ccd412"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.74.md"
CONTRACT = DOCS / "working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
CONTRACT_ARCHIVE = DOCS / "archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
PROBE_FIXTURE = ROOT / "tests/fixtures/fp001_phase8_authorization_probe"

PREDECESSORS = (
    (
        "docs/00_platform/02_OPEN_WORK_v1.2.73.md",
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.73.md",
    ),
    (
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.15.md",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.15.md",
    ),
    (
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md",
    ),
    (
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.17.md",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.17.md",
    ),
)


def _marked_json(text: str, start: str, end: str) -> dict:
    match = re.search(re.escape(start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(end), text, re.DOTALL)
    return json.loads(match.group(1)) if match else {}


def _contract_section_p(text: str) -> str:
    return text.split("## P. Architectural proof requirement", 1)[1].split("## Q. Vertical Slice map", 1)[0]


class FP001DevelopmentEntryHardStopPromotionTests(unittest.TestCase):
    def test_hard_stop_pass_authorises_bounded_phase8_only(self):
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
        self.assertEqual("REQUIRED / NOT YET DEFINED", state.get("tracer_bullet"))
        self.assertEqual("NONE / NOT CREATED", state.get("tracer_bullet_id"))
        self.assertEqual("NOT STARTED", state.get("architectural_proof_execution"))
        self.assertEqual(
            "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
            state.get("next_governance_action"),
        )

        active = text.split("# 9. Immediate Next Action", 1)[1].split("# 10. Minimal Tools", 1)[0]
        for token in (
            "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
            "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
            "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        ):
            self.assertIn(token, active)
        self.assertNotRegex(active, r"\bTB-\d{3,}\b")

    def test_contract_header_reflects_hard_stop_without_changing_frozen_section_p(self):
        text = CONTRACT.read_text(encoding="utf-8")
        header = text.split("## A. Identity and provenance", 1)[0]
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", header)
        self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", header)
        proof_section = _contract_section_p(text)
        self.assertIn("The proof vehicle and final proof classification remain NOT FINALISED.", proof_section)
        self.assertEqual(
            "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
            hashlib.sha256(CONTRACT_ARCHIVE.read_bytes()).hexdigest(),
        )

    def test_predecessor_archives_are_byte_identical(self):
        for current_rel, archive_rel in PREDECESSORS:
            archive = ROOT / archive_rel
            self.assertTrue(archive.is_file(), archive_rel)
            if current_rel.endswith("02_OPEN_WORK_v1.2.73.md"):
                continue
            # working predecessors were removed; archive bytes were copied at promotion time.
            manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
            rule = manifest["integrity_rules"]["fp001_development_entry_hard_stop_lifecycle"]
            expected = rule["predecessor_archives_sha256"][archive_rel]
            self.assertEqual(expected, hashlib.sha256(archive.read_bytes()).hexdigest())

    def test_manifest_pins_hard_stop_lifecycle(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        rule = manifest["integrity_rules"]["fp001_development_entry_hard_stop_lifecycle"]
        self.assertEqual(BASE_SHA, rule["base_sha"])
        self.assertEqual("AUTHORISED", rule["phase8"])
        self.assertEqual("AUTHORISED", rule["application_implementation"])
        open_work_entry = next(e for e in manifest["governing_documents"] if e["document_id"] == "OPEN_WORK")
        self.assertEqual("1.2.74", open_work_entry["semver"])
        self.assertEqual("1.2.73", open_work_entry["superseded_version"])

    def test_foundation_integrity_rejects_reverted_hard_stop_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            shutil.copytree(ROOT / "tests", root / "tests")
            shutil.copytree(ROOT / "tools", root / "tools")
            open_work = root / "docs/00_platform/02_OPEN_WORK_v1.2.74.md"
            text = open_work.read_text(encoding="utf-8")
            text = text.replace(
                "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
                "DEVELOPMENT ENTRY HARD STOP: FAIL",
                1,
            )
            open_work.write_text(text, encoding="utf-8")
            report = run_audit(root, root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
            self.assertEqual("FAIL", report["status"])
            messages = [f.get("message", "") if isinstance(f, dict) else str(f) for f in report["findings"]]
            self.assertTrue(any("hard_stop" in m.lower() or "hard stop" in m.lower() or "hard-stop" in m.lower() for m in messages))

    def test_foundation_integrity_rejects_unauthorised_root_application_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            shutil.copytree(ROOT / "tests", root / "tests")
            shutil.copytree(ROOT / "tools", root / "tools")
            manifest = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            data = json.loads(manifest.read_text(encoding="utf-8"))
            rule = data["integrity_rules"]["fp001_development_entry_hard_stop_lifecycle"]
            rule["phase8"] = "UNAUTHORISED"
            rule["application_implementation"] = "UNAUTHORISED"
            manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            (root / "mix.exs").write_text("defmodule Mix.Project, do: def project, do: [app: :newyou]\n", encoding="utf-8")
            report = run_audit(root, manifest)
            self.assertEqual("FAIL", report["status"])
            messages = [f.get("message", "") if isinstance(f, dict) else str(f) for f in report["findings"]]
            self.assertTrue(any("application" in m.lower() or "source" in m.lower() for m in messages))

    def test_authorization_probe_fixture_allowed_without_root_application_source(self):
        self.assertTrue((PROBE_FIXTURE / ".authorization_probe").is_file())
        self.assertTrue((PROBE_FIXTURE / "lib/probe.ex").is_file())
        self.assertFalse((ROOT / "mix.exs").exists())
        report = run_audit(ROOT, MANIFEST)
        self.assertEqual("PASS", report["status"])


if __name__ == "__main__":
    unittest.main()
