from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_smoke import run_smoke_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
ROUTER_RELATIVE = Path("docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json")


class FoundationSmokeTests(unittest.TestCase):
    def _fixture(self, directory: str) -> tuple[Path, Path]:
        root = Path(directory)
        shutil.copytree(DOCS, root / "docs/00_platform")
        return root, root / ROUTER_RELATIVE

    def test_smoke_passes_current_router(self):
        report = run_smoke_audit(ROOT, ROUTER_RELATIVE)
        self.assertEqual("PASS", report["status"], report["findings"])
        self.assertGreater(report["assertion_count"], 0)

    def test_smoke_rejects_open_work_as_governing_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root, router_path = self._fixture(directory)
            router = json.loads(router_path.read_text(encoding="utf-8"))
            router["governing_documents"].append(
                {
                    "document_id": "OPEN_WORK",
                    "canonical_filename": "02_OPEN_WORK_v1.2.90.md",
                    "semver": "1.2.90",
                    "repository_path": "docs/00_platform/02_OPEN_WORK_v1.2.90.md",
                    "sha256": "7ae61b682322628826d05e130546a644cb127baaf6f5fa737aa773aa19936ea5",
                }
            )
            router_path.write_text(json.dumps(router, indent=2) + "\n", encoding="utf-8")

            report = run_smoke_audit(root, router_path)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("governing" in finding["message"].lower() for finding in report["findings"]))

    def test_smoke_rejects_wrong_plane_execution_provider(self):
        with tempfile.TemporaryDirectory() as directory:
            root, router_path = self._fixture(directory)
            router = json.loads(router_path.read_text(encoding="utf-8"))
            router["execution_authority"]["provider"] = "GitHub Open Work"
            router_path.write_text(json.dumps(router, indent=2) + "\n", encoding="utf-8")

            report = run_smoke_audit(root, router_path)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("Plane" in finding["message"] for finding in report["findings"]))

    def test_smoke_rejects_non_ready_agent_execution_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root, router_path = self._fixture(directory)
            router = json.loads(router_path.read_text(encoding="utf-8"))
            router["execution_authority"]["agent_executable_state"] = "Planning"
            router_path.write_text(json.dumps(router, indent=2) + "\n", encoding="utf-8")

            report = run_smoke_audit(root, router_path)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("Ready" in finding["message"] for finding in report["findings"]))

    def test_smoke_rejects_current_authority_hash_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root, router_path = self._fixture(directory)
            router = json.loads(router_path.read_text(encoding="utf-8"))
            router["governing_documents"][0]["sha256"] = "0" * 64
            router_path.write_text(json.dumps(router, indent=2) + "\n", encoding="utf-8")

            report = run_smoke_audit(root, router_path)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("hash" in finding["message"].lower() for finding in report["findings"]))

    def test_smoke_rejects_legacy_open_work_hash_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root, router_path = self._fixture(directory)
            router = json.loads(router_path.read_text(encoding="utf-8"))
            router["legacy_snapshots"][0]["sha256"] = "0" * 64
            router_path.write_text(json.dumps(router, indent=2) + "\n", encoding="utf-8")

            report = run_smoke_audit(root, router_path)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("legacy" in finding["message"].lower() for finding in report["findings"]))

    def test_smoke_rejects_readme_that_does_not_route_plane(self):
        with tempfile.TemporaryDirectory() as directory:
            root, router_path = self._fixture(directory)
            readme_path = root / "docs/00_platform/README.md"
            readme = readme_path.read_text(encoding="utf-8")
            readme_path.write_text(readme.replace("Plane", "Delivery Ledger"), encoding="utf-8")

            report = run_smoke_audit(root, router_path)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("README" in finding["message"] for finding in report["findings"]))

    def test_smoke_rejects_semantic_working_route_into_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root, router_path = self._fixture(directory)
            router = json.loads(router_path.read_text(encoding="utf-8"))
            route = router["working_semantic_routes"][0]
            source = root / route
            archive = root / "docs/00_platform/archive" / source.name
            archive.parent.mkdir(parents=True, exist_ok=True)
            source.rename(archive)
            source.symlink_to(archive)

            report = run_smoke_audit(root, router_path)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("working" in finding["message"].lower() for finding in report["findings"]))


if __name__ == "__main__":
    unittest.main()
