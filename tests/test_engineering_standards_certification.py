import json
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
STANDARDS = DOCS / "reference" / "ENGINEERING_STANDARDS_v1.0.1.md"


class EngineeringStandardsCertificationTests(unittest.TestCase):
    def test_production_audit_accepts_only_the_current_certified_reference(self):
        report = run_audit(ROOT, MANIFEST)

        self.assertEqual("PASS", report["status"], report["findings"])
        lifecycle_check = next(
            (check for check in report["checks"] if check["name"] == "engineering_standards_lifecycle"),
            None,
        )
        self.assertIsNotNone(lifecycle_check, report["checks"])
        self.assertEqual("PASS", lifecycle_check["status"])
        self.assertIn("certified", lifecycle_check["message"].lower())

        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        active_entries = [
            entry
            for key in ("governing_documents", "reference_documents")
            for entry in manifest[key]
            if "ENGINEERING_STANDARDS" in entry.get("document_id", "")
        ]
        self.assertEqual(1, len(active_entries))
        self.assertEqual("ENGINEERING_STANDARDS", active_entries[0]["document_id"])
        self.assertEqual("ENGINEERING_STANDARDS_SUPPORTING_AUTHORITY", active_entries[0]["authority_class"])
        self.assertEqual("current", active_entries[0]["lifecycle"])
        self.assertIn(active_entries[0], manifest["reference_documents"])
        self.assertNotIn(active_entries[0], manifest["governing_documents"])

        standards = STANDARDS.read_text(encoding="utf-8")
        self.assertIn("- **Document version:** v1.0.1", standards)
        self.assertIn("- **Status:** CERTIFIED / CURRENT", standards)
        self.assertIn("- **Authority class:** SUPPORTING AUTHORITY / ENGINEERING STANDARDS", standards)


if __name__ == "__main__":
    unittest.main()
