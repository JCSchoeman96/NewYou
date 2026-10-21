from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import run_audit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
MANIFEST_RELATIVE = Path("docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")


class FoundationFullHistoricalTests(unittest.TestCase):
    def test_full_audit_rejects_changed_historical_certification_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(DOCS, root / "docs/00_platform")
            manifest_path = root / MANIFEST_RELATIVE
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            historical = manifest["historical_documents"][0]
            historical_path = root / historical["repository_path"]
            historical_path.write_bytes(historical_path.read_bytes() + b"\n")

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] in {"manifest_hash_parity", "frozen_provenance_hash"}
                    and finding["path"] == historical["repository_path"]
                    for finding in report["findings"]
                ),
                report["findings"],
            )


if __name__ == "__main__":
    unittest.main()
