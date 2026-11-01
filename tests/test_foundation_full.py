from __future__ import annotations

import json
import hashlib
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import (
    PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA,
    PRE_MIGRATION_LAYOUT_BASE_SHA,
    _audit_exact_predecessor_commit,
    run_audit,
)
from tools.run_foundation_full_tests import PRE_MIGRATION_BASE_SHA
from tests.foundation_test_support import (
    WELL38_BASE_SHA,
    copy_git_snapshot_tree,
    frozen_manifest_document_path,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST_RELATIVE = Path("docs/history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")


class FoundationFullHistoricalTests(unittest.TestCase):
    def test_full_audit_and_test_runner_share_the_pinned_migration_base(self):
        self.assertEqual(PRE_MIGRATION_BASE_SHA, PRE_MIGRATION_LAYOUT_BASE_SHA)

    def test_semantic_root_migration_resolves_the_frozen_roadmap_source_at_freeze(self):
        report = run_audit(ROOT, MANIFEST_RELATIVE)
        self.assertEqual("PASS", report["status"], report["findings"])
        self.assertEqual([], report["findings"])

        manifest = json.loads((ROOT / MANIFEST_RELATIVE).read_text(encoding="utf-8"))
        relative = "docs/00_platform/05_ROADMAP_v1.2.4.md"
        exception = manifest["integrity_rules"]["graph_rules"][
            "source_at_freeze_reference_exceptions"
        ][relative]
        archived = ROOT / "docs/history/platform/archive/05_ROADMAP_v1.2.4.md"
        self.assertEqual(exception["sha256"], hashlib.sha256(archived.read_bytes()).hexdigest())
        self.assertFalse((ROOT / relative).exists())

    def test_successor_full_audit_uses_the_exact_historical_base_sha(self):
        passes, message = _audit_exact_predecessor_commit(
            ROOT,
            PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA,
        )
        self.assertTrue(passes, message)
        self.assertIn("900 Foundation Integrity assertions", message)

        passes, message = _audit_exact_predecessor_commit(ROOT, "0" * 40)
        self.assertFalse(passes)
        self.assertIn("required main baseline", message)

        with tempfile.TemporaryDirectory(dir=ROOT, prefix=".foundation-full-nested-root-") as nested_root:
            passes, message = _audit_exact_predecessor_commit(
                Path(nested_root),
                PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA,
            )
        self.assertTrue(passes, message)

    def test_full_audit_rejects_changed_governance_lifecycle_rule(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            copy_git_snapshot_tree(
                ROOT,
                WELL38_BASE_SHA,
                root,
                "docs/00_platform",
                materialize_historical_readme=True,
            )
            manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["integrity_rules"]["roadmap_proof_classification_lifecycle"][
                "selected_proof_vehicle"
            ] = "REUSE_EXISTING_PROOF"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "roadmap_proof_classification_lifecycle"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_full_audit_rejects_changed_historical_certification_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(DOCS, root / "docs", ignore=shutil.ignore_patterns("00_platform"))
            manifest_path = root / MANIFEST_RELATIVE
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            historical = manifest["historical_documents"][0]
            historical_path = frozen_manifest_document_path(root, historical)
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
