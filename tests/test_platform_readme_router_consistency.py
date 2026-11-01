from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from tools.foundation_integrity_smoke import run_smoke_audit
from foundation_test_support import current_document_path, current_router_data, current_working_path, historical_platform_readme_path, historical_platform_readme_text


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
README = historical_platform_readme_path(ROOT)
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

STALE_PATTERNS = (
    r"(?i)proof classification (?:is|remains) not finalised",
    r"(?i)architectural proof classification is next",
    r"(?i)architectural proof classification.*remains unperformed",
)


def _current_readme_prose(text: str) -> str:
    return text.split("## Historical status evidence", 1)[0]


def _open_work_lifecycle_state(text: str) -> dict:
    match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        text,
        re.DOTALL,
    )
    return json.loads(match.group(1)) if match else {}


class PlatformReadmeRouterConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.open_work_path = current_document_path(ROOT, "OPEN_WORK")
        cls.atlas_path = current_working_path(ROOT, "DELIVERY_ATLAS_WORKING_")
        cls.readme = historical_platform_readme_text(ROOT)
        cls.current_prose = _current_readme_prose(cls.readme)
        cls.current_state = cls.readme.split("## Current State", 1)[1].split("\n## ", 1)[0]
        cls.atlas_routing = cls.readme.split("## Delivery Atlas routing", 1)[1].split("\n## ", 1)[0]
        cls.open_work_state = _open_work_lifecycle_state(cls.open_work_path.read_text(encoding="utf-8"))

    def test_delivery_atlas_routing_points_at_current_successor(self) -> None:
        current_route = self.atlas_path.relative_to(ROOT).as_posix()
        routed_paths = {
            item["repository_path"]
            for item in current_router_data(ROOT)["delivery_contracts"]
        }
        self.assertIn(current_route, routed_paths)
        self.assertIn("delivery/CURRENT_DELIVERY_ROUTER.json", (ROOT / "docs/README.md").read_text(encoding="utf-8"))

    def test_tb001_current_status_route_is_v013_and_preserves_v012_history(self) -> None:
        phase8 = self.manifest["integrity_rules"]["fp001_phase8_proof_contract_lifecycle"]
        expected = "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md"
        self.assertEqual(expected, phase8["candidate_path"])
        self.assertEqual("CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION", phase8["candidate_lifecycle"])
        self.assertEqual("COMPLETE / PASS", phase8["contract_design_review"])
        self.assertIn("working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.3.md", self.current_prose)
        self.assertNotIn("working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md", self.current_prose)
        self.assertIn("archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_APPROVED_CURRENT_v0.1.2.md", self.current_prose)
        self.assertIn("PROOF CERTIFICATION: NOT CERTIFIED", self.current_state)
        self.assertIn("PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED", self.current_state)

    def test_current_prose_agrees_with_open_work_classification(self) -> None:
        self.assertEqual("NEW_TRACER_BULLET", self.open_work_state.get("proof_classification"))
        self.assertEqual("COMPLETE / FINALISED", self.open_work_state.get("architectural_proof_classification_status"))
        self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED", self.current_state)
        self.assertIn("PROOF CLASSIFICATION: NEW_TRACER_BULLET", self.current_state)
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", self.current_state)
        for token in (
            "WELL-5 / P8-04: COMPLETE",
            "PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
            "PHASE 8: NOT CERTIFIED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
            "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
            "WELL-48: COMPLETE / MERGED VIA PR #156",
            "WELL-49: BLOCKED / WAITING ON WELL-61",
            "WELL-50: BACKLOG / NOT STARTED",
        ):
            self.assertIn(token, self.current_state)
        next_execution = re.search(r"(?m)^- NEXT EXECUTION ACTION: (.+)$", self.current_state)
        self.assertIsNotNone(next_execution)
        for token in (
            "WELL-48: COMPLETE",
            "WELL-49: BLOCKED",
            "WELL-50: BACKLOG",
            "WELL-60",
            "WELL-61",
            "WELL-51 follows the required WELL-48–50 seams",
        ):
            self.assertIn(token, next_execution.group(1))
        self.assertIn(
            "WELL-45: LEGAL/PRIVACY RELEASE GATE OPEN — DEVELOPMENT BASELINE PERMITTED; NOT LEGALLY APPROVED",
            self.current_state,
        )
        for token in (
            "p8-05 implementation authorised",
            "bounded phase 8",
            "well-48: complete",
            "well-49: blocked",
            "well-60",
            "well-61",
            "well-50: backlog",
        ):
            self.assertIn(token, self.open_work_state["next_governance_action"].casefold())
        self.assertEqual(
            "AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION AUTHORISED",
            self.open_work_state["application_implementation"],
        )

    def test_current_prose_cannot_regress_to_stale_classification_routing(self) -> None:
        for pattern in STALE_PATTERNS:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, self.current_prose))

    def test_foundation_smoke_checks_current_entrypoint_prose(self) -> None:
        report = run_smoke_audit(ROOT)
        checks = {item["name"]: item for item in report["checks"]}
        self.assertEqual("PASS", checks["smoke_documentation_entrypoint_current_prose"]["status"])


if __name__ == "__main__":
    unittest.main()
