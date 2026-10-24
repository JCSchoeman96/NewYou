"""Historical scope must remain independent of later application commits."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tests import foundation_test_support as history
from tools import foundation_integrity_audit as audit

ROOT = Path(__file__).resolve().parents[1]
APPLICATION_PATHS = (
    "mix.exs", "lib/new_you.ex", "config/config.exs", "test/new_you_test.exs",
    "assets/js/app.js", "priv/repo/seeds.exs",
)


class HistoricalScopeTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.git("init", "--quiet")
        self.git("config", "user.name", "Historical scope fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.write("planning.md", "base\n")
        self.base = self.commit("base")
        self.write("planning.md", "historical candidate\n")
        self.candidate = self.commit("historical candidate")
        for path in APPLICATION_PATHS:
            self.write(path, "later application source\n")
        self.later = self.commit("later authorised application")

    def git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.root, check=True, capture_output=True,
            text=True, env={**os.environ, "GIT_CONFIG_NOSYSTEM": "1"},
        ).stdout.strip()

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", message)
        return self.git("rev-parse", "HEAD")

    def test_historical_absence_ignores_later_application_tree(self):
        self.assertTrue((self.root / "mix.exs").exists())
        for path in APPLICATION_PATHS:
            self.assertFalse(history.git_snapshot_path_exists(self.root, self.candidate, path), path)
        self.assertTrue(history.git_snapshot_path_exists(self.root, self.later, "lib"))
        self.assertTrue(history.git_snapshot_path_exists(self.root, self.later, "mix.exs"))

    def test_historical_diff_ignores_later_application_commits_and_working_tree(self):
        self.write("lib/uncommitted.ex", "uncommitted\n")
        self.assertEqual(["planning.md"], history.git_changed_paths(self.root, self.base, self.candidate))
        changed = history.git_changed_paths(self.root, self.candidate, self.later)
        self.assertEqual(sorted(APPLICATION_PATHS), changed)

    def test_contaminated_historical_candidate_remains_visible(self):
        self.assertTrue(history.git_snapshot_path_exists(self.root, self.later, "mix.exs"))
        self.assertIn("lib/new_you.ex", history.git_changed_paths(self.root, self.base, self.later))

    def test_missing_or_symbolic_revisions_fail_closed(self):
        for revision in ("0" * 40, "", "HEAD"):
            with self.subTest(revision=revision):
                with self.assertRaises((ValueError, subprocess.CalledProcessError)):
                    history.git_snapshot_path_exists(self.root, revision, "mix.exs")
                for base, candidate in ((revision, self.candidate), (self.base, revision)):
                    with self.assertRaises((ValueError, subprocess.CalledProcessError)):
                        history.git_changed_paths(self.root, base, candidate)


class HistoricalSuccessorAuditTests(unittest.TestCase):
    def test_later_application_source_does_not_invalidate_historical_successor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            for path in APPLICATION_PATHS:
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("legitimate later application source\n", encoding="utf-8")
            manifest = json.loads((root / audit.DEFAULT_MANIFEST).read_text(encoding="utf-8"))
            issues = audit._phase8_approved_status_successor_issues(
                root, ROOT, manifest, manifest["integrity_rules"],
            )
            self.assertEqual([], issues)

    def test_historical_source_contamination_fails_successor_audit(self):
        # Mutate the exact historical successor tree using a separate index and
        # object store. The current content fixture still contains only docs.
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "content"
            shutil.copytree(ROOT / "docs", root / "docs")
            repository = Path(directory) / "history"
            subprocess.run(
                ["git", "clone", "--quiet", "--shared", "--no-checkout", str(ROOT), str(repository)],
                check=True, capture_output=True,
            )
            env = {
                **os.environ,
                "GIT_AUTHOR_NAME": "Historical scope fixture",
                "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
                "GIT_COMMITTER_NAME": "Historical scope fixture",
                "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
            }

            def git(*args, input=None):
                return subprocess.run(
                    ["git", *args], cwd=repository, env=env, input=input,
                    check=True, capture_output=True, text=True,
                ).stdout.strip()

            historical_head = audit.PHASE8_APPROVED_STATUS_SUCCESSOR_HEAD_SHA
            git("read-tree", historical_head)
            blob = git("hash-object", "-w", "--stdin", input="forbidden historical source\n")
            for path in APPLICATION_PATHS:
                git("update-index", "--add", "--cacheinfo", f"100644,{blob},{path}")
            tree = git("write-tree")
            contaminated = git("commit-tree", tree, "-p", historical_head, input="contaminated historical candidate\n")
            manifest = json.loads((root / audit.DEFAULT_MANIFEST).read_text(encoding="utf-8"))
            with patch.object(audit, "PHASE8_APPROVED_STATUS_SUCCESSOR_HEAD_SHA", contaminated):
                issues = audit._phase8_approved_status_successor_issues(
                    root, repository, manifest, manifest["integrity_rules"],
                )
            self.assertTrue(any("status transition added executable application source" in issue for issue in issues), issues)
            for path in APPLICATION_PATHS:
                self.assertTrue(any(path in issue for issue in issues), path)

    def test_missing_historical_successor_fails_closed(self):
        with patch.object(audit, "PHASE8_APPROVED_STATUS_SUCCESSOR_HEAD_SHA", "0" * 40):
            issues = audit._phase8_status_transition_source_issues(ROOT)
        self.assertEqual(["pinned status transition revision is unavailable: " + "0" * 40], issues)

    def test_current_authority_hashes_remain_enforced_with_later_application_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "docs", root / "docs")
            (root / "mix.exs").write_text("later application source\n", encoding="utf-8")
            manifest = json.loads((root / audit.DEFAULT_MANIFEST).read_text(encoding="utf-8"))
            route = manifest["integrity_rules"]["fp001_phase8_proof_contract_lifecycle"]["current_routes"]["delivery_atlas"]
            (root / route).write_bytes((root / route).read_bytes() + b"\n")
            issues = audit._phase8_approved_status_successor_issues(
                root, ROOT, manifest, manifest["integrity_rules"],
            )
            self.assertIn("Phase 8 current-route SHA-256 differs: " + route, issues)


if __name__ == "__main__":
    unittest.main()
