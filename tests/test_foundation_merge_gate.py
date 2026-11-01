from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"


class FoundationMergeGateTopologyTests(unittest.TestCase):
    def test_path_routing_regressions_run_in_always_on_smoke_job(self):
        workflow = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")

        self.assertIn(
            "python -m unittest discover -s tests -p 'test_foundation_lane_routing.py' -v",
            workflow,
        )

    def test_required_gate_does_not_wait_for_foundation_full(self):
        workflow = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")

        self.assertIn("needs: [route, foundation-smoke, application-ci]", workflow)
        self.assertNotIn("needs: [route, foundation-smoke, application-ci, foundation-full]", workflow)
        self.assertNotIn("FULL_REQUIRED:", workflow)
        self.assertNotIn("FULL_RESULT:", workflow)

    def test_governance_full_still_routes_automatically(self):
        workflow = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")

        self.assertIn("uses: ./.github/workflows/foundation-full.yml", workflow)
        self.assertIn("if: needs.route.outputs.foundation_full == 'true'", workflow)

    def test_deep_application_lane_is_selected_by_code_routing(self):
        integrity = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")
        application = (WORKFLOWS / "application-ci.yml").read_text(encoding="utf-8")

        self.assertIn("deep_application_changes:", integrity)
        self.assertIn(
            "deep_application_changes: ${{ needs.route.outputs.deep_application_changes == 'true' }}",
            integrity,
        )
        self.assertIn("deep_application_changes:", application)
        self.assertIn("if: inputs.deep_application_changes", application)

    def test_superseded_pr_runs_are_cancelled(self):
        workflow = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")

        self.assertIn("concurrency:", workflow)
        self.assertIn("group: foundation-integrity-${{ github.event.pull_request.number || github.ref }}", workflow)
        self.assertIn("cancel-in-progress: true", workflow)

    def test_exact_sha_dispatch_is_owned_by_foundation_full(self):
        integrity = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")
        full = (WORKFLOWS / "foundation-full.yml").read_text(encoding="utf-8")

        self.assertNotIn("  workflow_dispatch:", integrity)
        self.assertIn("  workflow_call:", full)
        self.assertIn("  workflow_dispatch:", full)
        self.assertIn("description: Exact 40-character commit SHA to certify.", full)
        self.assertIn("if: github.event_name == 'workflow_dispatch'", full)


if __name__ == "__main__":
    unittest.main()
