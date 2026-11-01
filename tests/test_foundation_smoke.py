from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_smoke import run_smoke_audit


ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE_ROUTER = Path("docs/governance/CURRENT_GOVERNANCE_ROUTER.json")
DELIVERY_ROUTER = Path("docs/delivery/CURRENT_DELIVERY_ROUTER.json")


class FoundationSmokeTests(unittest.TestCase):
    def _fixture(self, directory: str) -> Path:
        root = Path(directory)
        for relative in ("docs/governance", "docs/delivery", "docs/history"):
            shutil.copytree(ROOT / relative, root / relative)
        (root / "docs").mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "docs/README.md", root / "docs/README.md")
        shutil.copytree(ROOT / "docs/development", root / "docs/development")
        (root / ".github/workflows").mkdir(parents=True, exist_ok=True)
        shutil.copy2(
            ROOT / ".github/workflows/foundation-integrity.yml",
            root / ".github/workflows/foundation-integrity.yml",
        )
        return root

    def _mutate_router(self, root: Path, relative: Path, mutate) -> None:
        path = root / relative
        router = json.loads(path.read_text(encoding="utf-8"))
        mutate(router)
        path.write_text(json.dumps(router, indent=2) + "\n", encoding="utf-8")

    def test_smoke_passes_both_current_routers(self):
        report = run_smoke_audit(ROOT)
        self.assertEqual("PASS", report["status"], report["findings"])
        self.assertGreater(report["assertion_count"], 0)

    def test_smoke_rejects_missing_delivery_router(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            (root / DELIVERY_ROUTER).unlink()

            report = run_smoke_audit(root)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("delivery router" in item["message"].lower() for item in report["findings"]))

    def test_governance_router_cannot_route_into_delivery_or_history(self):
        for forbidden in ("docs/delivery/feature-contracts/example.md", "docs/history/example.md"):
            with self.subTest(path=forbidden), tempfile.TemporaryDirectory() as directory:
                root = self._fixture(directory)
                self._mutate_router(
                    root,
                    GOVERNANCE_ROUTER,
                    lambda router: router["governing_documents"].append(
                        {
                            "document_id": "CROSS_ROOT",
                            "canonical_filename": Path(forbidden).name,
                            "semver": "1.0.0",
                            "repository_path": forbidden,
                            "sha256": "0" * 64,
                        }
                    ),
                )

                report = run_smoke_audit(root)
                self.assertEqual("FAIL", report["status"])
                self.assertTrue(any("governance" in item["message"].lower() for item in report["findings"]))

    def test_delivery_router_cannot_route_into_governance_or_history(self):
        for forbidden in (
            "docs/governance/product/00_PLATFORM_v1.13.0.md",
            "docs/history/02_OPEN_WORK_v1.2.90.md",
        ):
            with self.subTest(path=forbidden), tempfile.TemporaryDirectory() as directory:
                root = self._fixture(directory)
                self._mutate_router(
                    root,
                    DELIVERY_ROUTER,
                    lambda router: router["delivery_contracts"].append(
                        {
                            "document_id": "CROSS_ROOT",
                            "contract_type": "jit",
                            "repository_path": forbidden,
                            "sha256": "0" * 64,
                        }
                    ),
                )

                report = run_smoke_audit(root)
                self.assertEqual("FAIL", report["status"])
                self.assertTrue(any("delivery" in item["message"].lower() for item in report["findings"]))

    def test_delivery_router_change_does_not_change_governance_routing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            governance_path = root / GOVERNANCE_ROUTER
            before = governance_path.read_bytes()

            def add_delivery_route(router):
                added = dict(router["delivery_contracts"][0])
                added["document_id"] = "ADDITIONAL_DELIVERY_ROUTE"
                router["delivery_contracts"].append(added)

            self._mutate_router(root, DELIVERY_ROUTER, add_delivery_route)

            report = run_smoke_audit(root)
            self.assertEqual("PASS", report["status"], report["findings"])
            self.assertEqual(before, governance_path.read_bytes())

    def test_governance_router_excludes_delivery_and_plane_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            self._mutate_router(
                root,
                GOVERNANCE_ROUTER,
                lambda router: router.update(
                    {"delivery_contracts": [], "execution_authority": {"provider": "Plane"}}
                ),
            )

            report = run_smoke_audit(root)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("boundary" in item["message"].lower() for item in report["findings"]))

    def test_smoke_requires_semantic_roots_and_plane_entrypoint(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            readme = root / "docs/README.md"
            readme.write_text("Old path only: docs/00_platform/README.md\n", encoding="utf-8")

            report = run_smoke_audit(root)
            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("documentation entrypoint" in item["message"].lower() for item in report["findings"]))


if __name__ == "__main__":
    unittest.main()
