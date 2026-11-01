import hashlib
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE_ROUTER = ROOT / "docs/governance/CURRENT_GOVERNANCE_ROUTER.json"
DELIVERY_ROUTER = ROOT / "docs/delivery/CURRENT_DELIVERY_ROUTER.json"
FROZEN_ROUTER = ROOT / "docs/history/platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json"
FROZEN_MANIFEST = ROOT / "docs/history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
FROZEN_OPEN_WORK = ROOT / "docs/history/02_OPEN_WORK_v1.2.90.md"


class DeliveryGovernanceTransitionTest(unittest.TestCase):
    def test_governance_router_contains_only_current_governance(self):
        router = json.loads(GOVERNANCE_ROUTER.read_text(encoding="utf-8"))
        self.assertEqual("CURRENT_GOVERNANCE_ROUTER", router["router_id"])
        self.assertEqual("CURRENT", router["status"])

        expected_ids = {
            "NORTH_STAR_AND_MVP",
            "PLATFORM_PRODUCT_LAW",
            "PRODUCT_DECISIONS",
            "ARCHITECTURE_LAW",
            "DOMAIN_LAW",
            "GOVERNING_ROADMAP",
        }
        self.assertEqual(
            expected_ids,
            {entry["document_id"] for entry in router["governing_documents"]},
        )
        self.assertEqual(
            {
                "PLATFORM_OPERATING_MODEL",
                "FRONTEND_EXPERIENCE_SYSTEM",
                "ENGINEERING_STANDARDS",
                "DELIVERY_GOVERNANCE_STANDARD",
            },
            {entry["document_id"] for entry in router["supporting_documents"]},
        )
        for collection in (
            "governing_documents",
            "architecture_references",
            "supporting_documents",
        ):
            for entry in router[collection]:
                self.assertTrue(entry["repository_path"].startswith("docs/governance/"))
        self.assertNotIn("delivery_contracts", router)
        self.assertNotIn("execution_authority", router)
        self.assertNotIn("plane", router)

    def test_delivery_router_contains_only_beneath_governance_contracts(self):
        router = json.loads(DELIVERY_ROUTER.read_text(encoding="utf-8"))
        self.assertEqual("CURRENT_DELIVERY_ROUTER", router["router_id"])
        self.assertEqual("CURRENT", router["status"])
        contract_types = {entry["contract_type"] for entry in router["delivery_contracts"]}
        self.assertTrue(
            {"feature_contract", "jit", "proof", "execution", "content_evidence"}
            .issubset(contract_types)
        )
        for entry in router["delivery_contracts"]:
            self.assertTrue(entry["repository_path"].startswith("docs/delivery/"))
            self.assertTrue((ROOT / entry["repository_path"]).is_file())
        self.assertNotIn("governing_documents", router)
        self.assertNotIn("authority_precedence", router)
        self.assertNotIn("execution_authority", router)

    def test_plane_remains_live_execution_authority_and_history_is_frozen(self):
        readme = (ROOT / "docs/README.md").read_text(encoding="utf-8")
        self.assertIn("governance/", readme)
        self.assertIn("delivery/", readme)
        self.assertIn("development/", readme)
        self.assertIn("history/", readme)
        self.assertIn("Plane", readme)

        legacy_open_work = json.loads(FROZEN_ROUTER.read_text(encoding="utf-8"))
        open_work = next(
            item
            for item in legacy_open_work["legacy_snapshots"]
            if item["document_id"] == "OPEN_WORK_FINAL_LEGACY_SNAPSHOT"
        )
        self.assertEqual("frozen_legacy", open_work["lifecycle"])
        self.assertFalse(open_work["live_execution_authority"])
        self.assertEqual(
            "7ae61b682322628826d05e130546a644cb127baaf6f5fa737aa773aa19936ea5",
            hashlib.sha256(FROZEN_OPEN_WORK.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            "2a8557193fc071996e23d9214980da22d48bdbf3",
            subprocess.run(
                ["git", "hash-object", str(FROZEN_MANIFEST)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip(),
        )

    def test_foundation_ci_uses_both_current_routers_and_historical_manifest(self):
        integrity = (ROOT / ".github/workflows/foundation-integrity.yml").read_text(
            encoding="utf-8"
        )
        full = (ROOT / ".github/workflows/foundation-full.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("docs/governance/CURRENT_GOVERNANCE_ROUTER.json", integrity)
        self.assertIn("docs/delivery/CURRENT_DELIVERY_ROUTER.json", integrity)
        self.assertIn(
            "--manifest docs/history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json",
            full,
        )
        self.assertIn("historical", full.lower())


if __name__ == "__main__":
    unittest.main()
