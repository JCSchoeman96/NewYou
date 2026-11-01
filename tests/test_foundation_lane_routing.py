from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_routing import classify_changed_paths, classify_event, classify_path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"


def _route(paths: list[str]) -> dict[str, bool]:
    return classify_changed_paths(paths)


class ApplicationAndEngineeringRoutingTests(unittest.TestCase):
    """Scenario A and B: ordinary application and engineering changes never select Full."""

    def test_application_source_runs_application_ci_without_full(self):
        decision = _route(["lib/new_you/accounts.ex"])
        self.assertEqual({"foundation_full": False, "application_changes": True}, decision)

    def test_root_engineering_files_run_engineering_checks_without_full(self):
        paths = [
            "AGENTS.md",
            ".tool-versions",
            ".gitattributes",
            ".devcore/project.conf",
            ".agents/skills/code-change-verification/SKILL.md",
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertEqual("application", classify_path(path))
                self.assertEqual({"foundation_full": False, "application_changes": True}, _route([path]))

    def test_ready_ticket_uses_packaged_skill_with_only_a_legacy_path_shim(self):
        instructions = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("`$ticket-implement`", instructions)
        self.assertIn("identify the NewYou Plane ticket to implement", instructions)
        self.assertIn("compatibility skill for existing references", instructions)
        self.assertIn("thin shim for the pinned TB-001 reference", instructions)
        self.assertNotIn(".agents/skills/ticket-implement/SKILL.md", instructions)
        self.assertFalse((ROOT / ".agents/skills/ticket-implement/SKILL.md").exists())
        shim = (ROOT / ".agents/skills/project-implementation/SKILL.md").read_text(encoding="utf-8")
        self.assertEqual(
            "---\n"
            "name: project-implementation\n"
            "description: Compatibility shim for the pinned NewYou repository skill path.\n"
            "---\n\n"
            "# Compatibility shim\n\n"
            "This file preserves a pinned repository reference. For implementation, invoke the installed `$ticket-implement` skill, then identify the NewYou Plane ticket to implement.\n",
            shim,
        )

    def test_unpinned_live_implementation_documents_use_packaged_skill_name(self):
        live_documents = [
            "AGENTS.md",
            "docs/execution/p8-05-registration-jit-spec.md",
            "docs/superpowers/specs/2026-10-22-well-5-p8-04-proof-harness-spec.md",
        ]
        local_skill_path = ".agents/skills/project-implementation/SKILL.md"
        for path in live_documents:
            with self.subTest(path=path):
                self.assertFalse(
                    local_skill_path in (ROOT / path).read_text(encoding="utf-8"),
                    msg=f"{path} still points to the repo-local legacy path",
                )

    def test_known_engineering_document_paths_run_application_ci_without_full(self):
        for path in [
            "docs/development/example.md",
            "docs/superpowers/specs/example.md",
            "docs/execution/FP-001/specs/example.md",
        ]:
            with self.subTest(path=path):
                self.assertEqual("application", classify_path(path))
                self.assertEqual({"foundation_full": False, "application_changes": True}, _route([path]))

    def test_engineering_tooling_and_ci_are_classified_intentionally(self):
        for path in [
            "mix.exs",
            "mix.lock",
            ".credo.exs",
            "tools/architecture/ash_write_boundary.ex",
            ".github/workflows/application-ci.yml",
            "config/test.exs",
            "priv/repo/migrations/20261022104847_initialize_extensions_1.exs",
        ]:
            with self.subTest(path=path):
                self.assertEqual("application", classify_path(path))


class GovernanceRoutingTests(unittest.TestCase):
    """Scenario C: governance-sensitive changes select Full."""

    def test_current_platform_authority_selects_full_only(self):
        path = "docs/00_platform/00_PLATFORM_v1.9.0.md"
        self.assertEqual("governance", classify_path(path))
        self.assertEqual({"foundation_full": True, "application_changes": False}, _route([path]))

    def test_platform_working_documents_remain_governance_paths(self):
        path = "docs/00_platform/working/example.md"
        self.assertEqual("governance", classify_path(path))
        self.assertEqual({"foundation_full": True, "application_changes": False}, _route([path]))

    def test_governed_authority_document_selects_full(self):
        decision = _route(["docs/00_platform/02_OPEN_WORK_v1.2.78.md"])
        self.assertEqual({"foundation_full": True, "application_changes": False}, decision)

    def test_governance_audit_code_selects_full(self):
        for path in ["tools/foundation_integrity_audit.py", "tools/foundation_integrity_routing.py", "tests/test_foundation_smoke.py"]:
            with self.subTest(path=path):
                self.assertEqual("governance", classify_path(path))
                self.assertTrue(_route([path])["foundation_full"])

    def test_governance_full_workflow_itself_selects_full(self):
        self.assertEqual("governance", classify_path(".github/workflows/foundation-full.yml"))
        self.assertEqual("governance", classify_path(".github/workflows/foundation-integrity.yml"))
        self.assertTrue(_route([".github/workflows/foundation-full.yml"])["foundation_full"])


class MixedAndUnknownRoutingTests(unittest.TestCase):
    """Scenario D (mixed) and scenario E (unknown, fails closed)."""

    def test_mixed_application_and_governance_runs_both(self):
        decision = _route(["lib/new_you/accounts.ex", "docs/00_platform/02_OPEN_WORK_v1.2.78.md"])
        self.assertEqual({"foundation_full": True, "application_changes": True}, decision)

    def test_unknown_paths_fail_closed_to_full(self):
        for path in ["new-surface/authority.md", ".github/CODEOWNERS", "tools/unclassified.py", "vendor/blob.bin"]:
            with self.subTest(path=path):
                self.assertEqual("unknown", classify_path(path))
                self.assertTrue(_route([path])["foundation_full"])

    def test_unclassified_document_paths_fail_closed_to_full(self):
        for path in ["docs/unclassified-area/example.md", "docs/something-new/foo.md"]:
            with self.subTest(path=path):
                self.assertEqual("unknown", classify_path(path))
                self.assertEqual({"foundation_full": True, "application_changes": False}, _route([path]))

    def test_path_escapes_and_backslashes_fail_closed(self):
        for path in ["../lib/x.ex", "/lib/x.ex", r"lib\x.ex"]:
            with self.subTest(path=path):
                self.assertEqual("unknown", classify_path(path))

    def test_empty_change_range_fails_closed(self):
        self.assertEqual({"foundation_full": True, "application_changes": False}, _route([]))


class EventRoutingTests(unittest.TestCase):
    """Scenario F and manual certification."""

    def _repo(self, directory: str):
        root = Path(directory)

        def git(*args: str) -> str:
            return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout.strip()

        git("init", "--quiet", "-b", "main")
        git("config", "user.email", "routing@example.invalid")
        git("config", "user.name", "Routing Test")
        (root / "lib").mkdir()
        (root / "lib/app.ex").write_text("defmodule App do\nend\n", encoding="utf-8")
        (root / "docs/00_platform").mkdir(parents=True)
        (root / "docs/00_platform/authority.md").write_text("v1\n", encoding="utf-8")
        git("add", ".")
        git("commit", "--quiet", "-m", "baseline")
        return root, git

    def test_manual_dispatch_selects_full_only(self):
        decision = classify_event("workflow_dispatch", "", "", str(ROOT))
        self.assertEqual({"foundation_full": True, "application_changes": False}, decision)

    def test_post_merge_push_of_reviewed_application_tree_does_not_rerun_full(self):
        """Scenario F: the merged application tree was verified on its PR head; main must not
        re-run cold Full for it, while application verification still runs on the push."""
        with tempfile.TemporaryDirectory() as directory:
            root, git = self._repo(directory)
            git("checkout", "--quiet", "-b", "feature")
            (root / "lib/app.ex").write_text("defmodule App do\n  def run, do: :ok\nend\n", encoding="utf-8")
            git("commit", "--quiet", "-am", "application change")
            pr_head = git("rev-parse", "HEAD")
            git("checkout", "--quiet", "main")
            merge_base = git("rev-parse", "HEAD")
            git("merge", "--quiet", "--no-ff", "-m", "merge PR", "feature")
            merged = git("rev-parse", "HEAD")

            pull_request = classify_event("pull_request", merge_base, pr_head, str(root))
            self.assertEqual({"foundation_full": False, "application_changes": True}, pull_request)

            post_merge = classify_event("push", merge_base, merged, str(root))
            self.assertFalse(post_merge["foundation_full"])
            self.assertTrue(post_merge["application_changes"])

    def test_pull_request_with_governance_change_selects_full_from_exact_diff(self):
        with tempfile.TemporaryDirectory() as directory:
            root, git = self._repo(directory)
            base = git("rev-parse", "HEAD")
            git("checkout", "--quiet", "-b", "governed")
            (root / "docs/00_platform/authority.md").write_text("v2\n", encoding="utf-8")
            git("commit", "--quiet", "-am", "governance change")
            head = git("rev-parse", "HEAD")
            self.assertTrue(classify_event("pull_request", base, head, str(root))["foundation_full"])


class TopologyTests(unittest.TestCase):
    """The lane topology is physically split and wired through native reusable workflows."""

    def test_nightly_hardening_is_main_only_cold_and_separate_from_pr_checks(self):
        workflow = (WORKFLOWS / "nightly-hardening.yml").read_text(encoding="utf-8")
        self.assertIn("  schedule:", workflow)
        self.assertIn("    - cron:", workflow)
        self.assertIn("  workflow_dispatch:", workflow)
        self.assertNotIn("  push:", workflow)
        self.assertNotIn("  pull_request:", workflow)
        self.assertEqual(2, workflow.count("if: github.ref == 'refs/heads/main'"))
        self.assertIn("uses: ./.github/workflows/foundation-full.yml", workflow)
        self.assertIn("sha: ${{ github.sha }}", workflow)
        self.assertIn("run: mix check.deep", workflow)
        self.assertNotIn("actions/cache", workflow)
        full = (WORKFLOWS / "foundation-full.yml").read_text(encoding="utf-8")
        self.assertNotIn("actions/cache", full)
        integrity = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")
        self.assertNotIn("nightly-hardening", integrity)

    def test_required_entry_point_keeps_name_and_routes_both_lanes(self):
        workflow = (WORKFLOWS / "foundation-integrity.yml").read_text(encoding="utf-8")
        self.assertIn("name: Foundation Integrity", workflow)
        self.assertIn("uses: ./.github/workflows/application-ci.yml", workflow)
        self.assertIn("uses: ./.github/workflows/foundation-full.yml", workflow)
        self.assertIn("needs.route.outputs.application_changes == 'true'", workflow)
        self.assertIn("needs.route.outputs.foundation_full == 'true'", workflow)

    def test_application_ci_runs_canonical_gates_and_never_historical_full(self):
        workflow = (WORKFLOWS / "application-ci.yml").read_text(encoding="utf-8")
        self.assertIn("run: mix check\n", workflow)
        self.assertIn("run: mix check.deep", workflow)
        lowered = workflow.lower()
        self.assertNotIn("unittest", lowered)
        self.assertNotIn("foundation_integrity", lowered)
        self.assertNotIn("redis", lowered)
        self.assertNotIn("dev_database", lowered)

    def test_application_ci_uses_isolated_test_database_contract(self):
        workflow = (WORKFLOWS / "application-ci.yml").read_text(encoding="utf-8")
        self.assertIn('TEST_DATABASE_PORT: "55433"', workflow)
        self.assertIn("TEST_DATABASE_USERNAME: new_you_test", workflow)
        self.assertIn("CREATE ROLE new_you_test LOGIN NOSUPERUSER NOCREATEDB", workflow)
        self.assertNotIn("DEV_DATABASE", workflow)

    def test_foundation_full_is_called_only_and_keeps_historical_checks(self):
        workflow = (WORKFLOWS / "foundation-full.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_call:", workflow)
        self.assertNotIn("pull_request:", workflow)
        self.assertNotIn("push:", workflow)
        self.assertIn("python -m unittest discover -s tests -v", workflow)
        self.assertIn("tools/foundation_integrity_audit.py --manifest docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json --json", workflow)


if __name__ == "__main__":
    unittest.main()
