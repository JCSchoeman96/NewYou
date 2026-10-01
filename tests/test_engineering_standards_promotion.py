from __future__ import annotations

import hashlib
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import _engineering_standards_promotion_state, run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
README = DOCS / "README.md"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.53.md"
HARDEN = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.7.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
STANDARDS = DOCS / "reference" / "ENGINEERING_STANDARDS_v1.0.0.md"
GRILL = DOCS / "working" / "TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md"

EXPECTED_MAIN_SHA = "73eca9d9148a82cab8ae988c5950539bfee0d7f9"
EXPECTED_GRILL_SHA256 = "27bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017"
EXPECTED_DOCUMENT_ID = "ENGINEERING_STANDARDS_CANDIDATE"
EXPECTED_AUTHORITY_CLASS = "ENGINEERING_STANDARDS_SUPPORTING_AUTHORITY_CANDIDATE"
PROHIBITED_PATHS = (
    DOCS / "ENGINEERING_STANDARDS_v1.0.0.md",
    DOCS / "reference" / "ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    DOCS / "working" / "ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
)


class EngineeringStandardsPromotionTests(unittest.TestCase):
    def setUp(self):
        self.readme = README.read_text(encoding="utf-8")
        self.open_work = OPEN_WORK.read_text(encoding="utf-8")
        self.harden = HARDEN.read_text(encoding="utf-8")
        self.standards = STANDARDS.read_text(encoding="utf-8") if STANDARDS.is_file() else ""
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def _assert_valid(self):
        valid, reason = _engineering_standards_promotion_state(
            ROOT,
            self.manifest,
            self.readme,
            self.open_work,
            self.harden,
        )
        self.assertTrue(valid, reason)

    def _assert_rejected(self, root: Path, manifest: dict, readme: str, open_work: str, harden: str):
        valid, _reason = _engineering_standards_promotion_state(
            root,
            manifest,
            readme,
            open_work,
            harden,
        )
        self.assertFalse(valid)

    def test_candidate_is_registered_as_supporting_reference_and_not_governing_authority(self):
        self._assert_valid()
        entries = [
            entry
            for entry in self.manifest["reference_documents"]
            if entry.get("document_id") == EXPECTED_DOCUMENT_ID
        ]
        self.assertEqual(1, len(entries))
        self.assertEqual(EXPECTED_AUTHORITY_CLASS, entries[0]["authority_class"])
        self.assertEqual("candidate", entries[0]["lifecycle"])
        self.assertNotIn(EXPECTED_DOCUMENT_ID, {entry["document_id"] for entry in self.manifest["governing_documents"]})
        self.assertIn("## Engineering Standards promotion candidate", self.readme)
        self.assertIn("reference/ENGINEERING_STANDARDS_v1.0.0.md", self.readme)
        self.assertTrue(all(not path.exists() for path in PROHIBITED_PATHS))

    def test_candidate_provenance_is_bound_to_live_main_and_the_grill(self):
        self._assert_valid()
        self.assertIn(f"Promotion baseline main SHA:** `{EXPECTED_MAIN_SHA}`", self.standards)
        self.assertIn(f"Source Grill SHA-256:** `{EXPECTED_GRILL_SHA256}`", self.standards)
        self.assertIn("working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md", self.standards)
        self.assertEqual(EXPECTED_GRILL_SHA256, hashlib.sha256(GRILL.read_bytes()).hexdigest())

    def test_certified_status_without_a_promoted_artifact_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            shutil.copytree(ROOT / "tools", root / "tools")
            shutil.copytree(ROOT / "tests", root / "tests")
            manifest = json.loads((root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text())
            (root / "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.0.md").unlink()
            readme = (root / "docs/00_platform/README.md").read_text()
            readme = readme.replace(
                "ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
                "ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED",
                1,
            )
            self._assert_rejected(
                root,
                manifest,
                readme,
                (root / "docs/00_platform/02_OPEN_WORK_v1.2.53.md").read_text(),
                (root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md").read_text(),
            )

    def test_certified_candidate_status_is_rejected_even_with_an_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            manifest = json.loads((root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text())
            candidate = root / "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.0.md"
            candidate.write_text(
                self.standards.replace(
                    "PROMOTION CANDIDATE / NOT CERTIFIED",
                    "COMPLETE / CERTIFIED",
                    1,
                ),
                encoding="utf-8",
            )
            self._assert_rejected(
                root,
                manifest,
                (root / "docs/00_platform/README.md").read_text(),
                (root / "docs/00_platform/02_OPEN_WORK_v1.2.53.md").read_text(),
                (root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md").read_text(),
            )

    def test_contradictory_readme_or_open_work_state_is_rejected(self):
        mutations = (
            (
                "README",
                self.readme.replace(
                    "- ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
                    "- ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED",
                    1,
                ),
                self.open_work,
            ),
            (
                "Open Work",
                self.readme,
                self.open_work.replace(
                    "ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
                    "ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED",
                    1,
                ),
            ),
        )
        for label, readme, open_work in mutations:
            with self.subTest(label=label):
                self._assert_rejected(ROOT, self.manifest, readme, open_work, self.harden)

    def test_unregistered_or_duplicate_authority_routes_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            shutil.copytree(ROOT / "tools", root / "tools")
            manifest = json.loads((root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text())
            (root / "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.1.0.md").write_text("candidate\n")
            self._assert_rejected(
                root,
                manifest,
                (root / "docs/00_platform/README.md").read_text(),
                (root / "docs/00_platform/02_OPEN_WORK_v1.2.53.md").read_text(),
                (root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md").read_text(),
            )

    def test_missing_manifest_registration_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            manifest = json.loads((root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text())
            manifest["reference_documents"] = [
                entry
                for entry in manifest["reference_documents"]
                if entry.get("document_id") != EXPECTED_DOCUMENT_ID
            ]
            self._assert_rejected(
                root,
                manifest,
                (root / "docs/00_platform/README.md").read_text(),
                (root / "docs/00_platform/02_OPEN_WORK_v1.2.53.md").read_text(),
                (root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md").read_text(),
            )

    def test_run_audit_fails_when_candidate_manifest_registration_is_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["reference_documents"] = [
                entry
                for entry in manifest["reference_documents"]
                if entry.get("document_id") != EXPECTED_DOCUMENT_ID
            ]
            manifest_path.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "engineering_standards_promotion_candidate"
                    and "exactly one manifest entry" in finding["message"]
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_run_audit_fails_when_candidate_manifest_registration_is_renamed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            entry = next(
                entry
                for entry in manifest["reference_documents"]
                if entry.get("document_id") == EXPECTED_DOCUMENT_ID
            )
            entry["document_id"] = "RENAMED_ENGINEERING_STANDARDS_CANDIDATE"
            manifest_path.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "engineering_standards_promotion_candidate"
                    and "exactly one manifest entry" in finding["message"]
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_incomplete_promotion_cannot_advance_downstream_work(self):
        mutated = self.standards + "\nFP-001 reconciliation is COMPLETE / PERFORMED.\n"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            shutil.copytree(ROOT / "tools", root / "tools")
            standards_path = root / "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.0.md"
            standards_path.write_text(mutated, encoding="utf-8")
            self._assert_rejected(
                root,
                json.loads((root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text()),
                (root / "docs/00_platform/README.md").read_text(),
                (root / "docs/00_platform/02_OPEN_WORK_v1.2.53.md").read_text(),
                (root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md").read_text(),
            )

    def test_all_downstream_advancement_markers_are_rejected(self):
        markers = (
            "COMMUNICATIONS: STARTED",
            "PHASE 7C: UNBLOCKED",
            "PROOF CLASSIFICATION: FINALISED",
            "APPLICATION IMPLEMENTATION: AUTHORISED",
            "STORE / CER: IN SCOPE",
        )
        for marker in markers:
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                shutil.copytree(ROOT / "docs", root / "docs")
                candidate = root / "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.0.md"
                candidate.write_text(self.standards + f"\n{marker}.\n", encoding="utf-8")
                self._assert_rejected(
                    root,
                    json.loads((root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text()),
                    (root / "docs/00_platform/README.md").read_text(),
                    (root / "docs/00_platform/02_OPEN_WORK_v1.2.53.md").read_text(),
                    (root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md").read_text(),
                )

    def test_provenance_and_route_mutations_are_rejected(self):
        mutations = (
            ("source SHA", self.standards.replace(EXPECTED_GRILL_SHA256, "0" * 64, 1)),
            ("working-only copy", self.standards.replace("EP-Q5", "EP-Q5-REMOVED", 1)),
            ("copied upstream law", self.standards + "\n- ARC-328 is an Engineering Standard.\n"),
        )
        for label, mutated in mutations:
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                shutil.copytree(ROOT / "docs", root / "docs")
                candidate = root / "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.0.md"
                candidate.write_text(mutated, encoding="utf-8")
                self._assert_rejected(
                    root,
                    json.loads((root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text()),
                    (root / "docs/00_platform/README.md").read_text(),
                    (root / "docs/00_platform/02_OPEN_WORK_v1.2.53.md").read_text(),
                    (root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.7.md").read_text(),
                )

    def test_normative_sections_require_explicit_grill_provenance(self):
        self._assert_valid()
        for marker in ("EP-Q1", "EP-Q2", "EP-Q3", "EP-Q4", "EP-Q5", "A-08", "B-09", "D-02", "D-03", "D-04", "D-05", "D-07"):
            self.assertIn(marker, self.standards)
        self.assertIn("No package, framework, tool, version, flag, provider or vendor is selected by this candidate.", self.standards)
        self.assertNotRegex(self.standards, r"(?im)^.*ENGINEERING STANDARDS.*COMPLETE / CERTIFIED.*$")


if __name__ == "__main__":
    unittest.main()
