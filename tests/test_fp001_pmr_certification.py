import json
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import run_audit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

class FP001PMRCertificationTests(unittest.TestCase):
    def test_certified_successors_route_only_to_unstarted_communications(self):
        report = run_audit(ROOT, MANIFEST)
        check = next(item for item in report["checks"] if item["name"] == "fp001_pmr_reconciliation")
        self.assertEqual("PASS", check["status"], report["findings"])
        open_work = (DOCS / "02_OPEN_WORK_v1.2.55.md").read_text(encoding="utf-8")
        self.assertIn("FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED", open_work)
        self.assertIn("NEXT STAGE: COMMUNICATIONS JIT DOMAIN DOSSIER", open_work)
        self.assertIn("COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED", open_work)
        self.assertIn("PHASE 7C: BLOCKED / NOT_STARTED", open_work)
        self.assertIn("PROOF CLASSIFICATION: NOT FINALISED", open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS", open_work)

    def test_pr67_candidate_archives_are_pinned(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        pinned = manifest["integrity_rules"]["fp001_pmr_reconciliation_candidate_archives"]
        self.assertEqual({
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md",
        }, set(pinned))

if __name__ == "__main__":
    unittest.main()
