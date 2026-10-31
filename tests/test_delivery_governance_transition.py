import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLATFORM = ROOT / "docs" / "00_platform"
CURRENT_ROUTER = PLATFORM / "CURRENT_AUTHORITY_ROUTER_v1.0.0.json"
LEGACY_OPEN_WORK = PLATFORM / "02_OPEN_WORK_v1.2.90.md"
ROUTER_PATH = PLATFORM / "CURRENT_AUTHORITY_ROUTER_v1.0.0.json"


def routed_delivery_standard():
    router = json.loads(ROUTER_PATH.read_text(encoding="utf-8"))
    entry = next(item for item in router["supporting_documents"] if item["document_id"] == "DELIVERY_GOVERNANCE_STANDARD")
    return ROOT / entry["repository_path"]


class DeliveryGovernanceTransitionTest(unittest.TestCase):
    def test_current_router_separates_durable_governance_from_plane_execution(self):
        self.assertTrue(CURRENT_ROUTER.is_file(), "lean current-authority router must exist")
        router = json.loads(CURRENT_ROUTER.read_text(encoding="utf-8"))

        governing_ids = {entry["document_id"] for entry in router["governing_documents"]}
        self.assertNotIn("OPEN_WORK", governing_ids)
        expected_governing_ids = {
            "PROJECT_NORTH_STAR_AND_MVP",
            "PLATFORM_BASELINE",
            "DECISION_REGISTER",
            "ARCHITECTURE_SYNTHESIS",
            "DOMAIN_MAP",
            "ROADMAP",
            "PLATFORM_OPERATING_MODEL",
            "FRONTEND_EXPERIENCE_SYSTEM",
        }
        self.assertEqual(governing_ids, expected_governing_ids)

        deep_reference_ids = {
            entry["document_id"] for entry in router["deep_reference_documents"]
        }
        self.assertEqual(
            deep_reference_ids,
            {
                "ARCHITECTURE_REQUIREMENTS",
                "ARCHITECTURE_LAW",
                "REFERENCE_FLOW_PRESSURE_TESTS",
            },
        )

        supporting_ids = {entry["document_id"] for entry in router["supporting_documents"]}
        self.assertIn("ENGINEERING_STANDARDS", supporting_ids)
        self.assertIn("DELIVERY_GOVERNANCE_STANDARD", supporting_ids)

        execution = router["execution_authority"]
        self.assertEqual(execution["provider"], "Plane")
        self.assertEqual(execution["project_identifier"], "WELL")
        self.assertEqual(execution["agent_executable_state"], "Ready")
        self.assertTrue(execution["durable_governance_precedence"])
        self.assertTrue(execution["status_only_changes_are_plane_only"])

    def test_open_work_is_frozen_legacy_not_live_authority(self):
        router = json.loads(CURRENT_ROUTER.read_text(encoding="utf-8"))
        snapshots = {entry["document_id"]: entry for entry in router["legacy_snapshots"]}
        open_work = snapshots["OPEN_WORK_FINAL_LEGACY_SNAPSHOT"]
        self.assertEqual(open_work["repository_path"], "docs/00_platform/02_OPEN_WORK_v1.2.90.md")
        self.assertEqual(
            open_work["sha256"],
            "7ae61b682322628826d05e130546a644cb127baaf6f5fa737aa773aa19936ea5",
        )
        self.assertEqual(open_work["lifecycle"], "frozen_legacy")
        self.assertFalse(open_work["live_execution_authority"])
        self.assertFalse(open_work["successor_required_for_status_changes"])
        self.assertTrue(LEGACY_OPEN_WORK.is_file())

    def test_delivery_standard_and_agent_contract_lock_plane_ready_boundary(self):
        standard = routed_delivery_standard().read_text(encoding="utf-8")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        project_instructions = (
            ROOT / "docs" / "development" / "chatgpt-project-master-gate-instructions.md"
        ).read_text(encoding="utf-8")

        for text in (standard, agents, project_instructions):
            self.assertIn("Plane", text)
            self.assertIn("Ready", text)
            self.assertIn("Open Work", text)
            self.assertIn("exact-head", text.lower())
            self.assertIn("resulting-main", text.lower())

        self.assertIn("authoritative execution", standard.lower())
        self.assertIn("only `Ready`", standard)
        self.assertIn("status-only", standard.lower())
        self.assertIn("semantic", standard.lower())
        self.assertIn("JIT IMPLEMENTATION CHOICE", standard)
        self.assertIn("UPSTREAM GOVERNANCE CONTRADICTION", standard)
        self.assertIn("Durable authority plus a dependency-cleared Plane `Ready` ticket is sufficient permission to implement", standard)
        self.assertIn("runtime grants do not separately block ordinary implementation", standard.casefold())
        self.assertIn("genuine external real-world gate", standard)

    def test_readme_routes_current_authority_to_router_and_plane(self):
        readme = (PLATFORM / "README.md").read_text(encoding="utf-8")
        self.assertIn("CURRENT_AUTHORITY_ROUTER_v1.0.0.json", readme)
        self.assertIn("ARCHITECTURE_LAW_WORKING_v0.36.0.md", readme)
        self.assertIn("Plane", readme)
        self.assertIn("Ready", readme)
        self.assertIn("02_OPEN_WORK_v1.2.90.md", readme)
        self.assertIn("frozen legacy", readme.lower())
        self.assertIn("status", readme.lower())
        self.assertIn("semantic", readme.lower())

    def test_ci_splits_current_smoke_from_historical_full(self):
        integrity = (ROOT / ".github" / "workflows" / "foundation-integrity.yml").read_text(
            encoding="utf-8"
        )
        full = (ROOT / ".github" / "workflows" / "foundation-full.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("CURRENT_AUTHORITY_ROUTER_v1.0.0.json", integrity)
        self.assertNotIn(
            "--manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json",
            integrity,
        )
        self.assertIn(
            "--manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json",
            full,
        )
        self.assertIn("historical", full.lower())
        self.assertIn("non-blocking", integrity.lower())

    def test_legacy_manifest_is_not_mutated_into_the_live_router(self):
        router = json.loads(CURRENT_ROUTER.read_text(encoding="utf-8"))
        historical = router["historical_integrity_baseline"]
        self.assertEqual(
            historical["repository_path"],
            "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json",
        )
        self.assertEqual(
            historical["git_blob_sha"],
            "2a8557193fc071996e23d9214980da22d48bdbf3",
        )
        self.assertEqual(historical["purpose"], "Foundation Full historical/provenance certification")


if __name__ == "__main__":
    unittest.main()
