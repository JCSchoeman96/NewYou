from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import refresh_manifest
from tools.foundation_integrity_routing import classify_changed_paths, classify_event
from tools.foundation_integrity_smoke import run_smoke_audit
from foundation_test_support import current_working_relative_path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/00_platform"
MANIFEST_RELATIVE = Path("docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")


class FoundationSmokeTests(unittest.TestCase):
    def _fixture(self, directory: str) -> tuple[Path, Path]:
        root = Path(directory)
        shutil.copytree(DOCS, root / "docs/00_platform")
        return root, root / MANIFEST_RELATIVE

    def test_smoke_passes_current_authority_routes(self):
        report = run_smoke_audit(ROOT, MANIFEST_RELATIVE)
        self.assertEqual("PASS", report["status"], report["findings"])
        self.assertGreater(report["assertion_count"], 0)

    def test_smoke_rejects_manifest_current_path_into_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._fixture(directory)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            open_work = next(item for item in manifest["governing_documents"] if item["document_id"] == "OPEN_WORK")
            open_work["repository_path"] = "docs/00_platform/archive/02_OPEN_WORK_v1.2.76.md"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

            report = run_smoke_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            failed_paths = [item for item in report["checks"] if item["name"] == "smoke_current_manifest_path" and item["status"] == "FAIL"]
            self.assertTrue(failed_paths)
            self.assertIn("archived=True", failed_paths[0]["message"])

    def test_smoke_rejects_stale_readme_working_route(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._fixture(directory)
            readme_path = root / "docs/00_platform/README.md"
            readme = readme_path.read_text(encoding="utf-8")
            current_route = Path(current_working_relative_path(root, "DELIVERY_ATLAS_WORKING_")).relative_to(
                "docs/00_platform"
            ).as_posix()
            current_name = Path(current_route).name
            major, minor, patch = (int(part) for part in re.search(r"v(\d+)\.(\d+)\.(\d+)", current_name).groups())
            previous_name = f"DELIVERY_ATLAS_WORKING_v{major}.{minor}.{patch - 1}.md"
            readme_path.write_text(
                readme.replace(
                    current_route,
                    f"working/{previous_name}",
                    1,
                ),
                encoding="utf-8",
            )

            report = run_smoke_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(any("OPEN_WORK" in finding["message"] or "current route" in finding["message"] for finding in report["findings"]))

    def test_smoke_rejects_active_unmanifested_working_route_into_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._fixture(directory)
            readme_path = root / "docs/00_platform/README.md"
            readme = readme_path.read_text(encoding="utf-8")
            section = readme.split("## Active Working Artifacts", 1)[1].split("\n## ", 1)[0]
            active_routes = re.findall(r"(?m)^-\s+`([^`\s]+\.md)`", section)
            current_route = next(
                route
                for route in active_routes
                if Path(route).name.startswith("EXPERIENCE_DECISIONS_WORKING_")
            )
            self.assertTrue(current_route.startswith("working/"), current_route)
            archived_route = f"archive/{Path(current_route).name}"
            readme_path.write_text(
                readme.replace(f"`{current_route}`", f"`{archived_route}`", 1),
                encoding="utf-8",
            )

            report = run_smoke_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    check["name"] == "smoke_current_working_path" and check["status"] == "FAIL"
                    for check in report["checks"]
                ),
                report["checks"],
            )

    def test_smoke_rejects_stale_delivery_atlas_navigation_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._fixture(directory)
            readme_path = root / "docs/00_platform/README.md"
            readme = readme_path.read_text(encoding="utf-8")
            current_route = current_working_relative_path(root, "DELIVERY_ATLAS_WORKING_").removeprefix(
                "docs/00_platform/"
            )
            section = readme.split("## Delivery Atlas routing", 1)[1].split("\n## ", 1)[0]
            current_link = f"[Delivery Atlas]({current_route})"
            self.assertIn(current_link, section)
            stale_link = "[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v9.9.9.md)"
            readme_path.write_text(readme.replace(current_link, stale_link, 1), encoding="utf-8")

            report = run_smoke_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    check["name"] == "smoke_delivery_atlas_route" and check["status"] == "FAIL"
                    for check in report["checks"]
                ),
                report["checks"],
            )

    def test_smoke_rejects_current_authority_route_into_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._fixture(directory)
            contract_path = root / current_working_relative_path(root, "HARDEN-02_CONTRACT_WORKING_")
            contract = contract_path.read_text(encoding="utf-8")
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            architecture = next(
                entry
                for entry in manifest["governing_documents"]
                if entry["document_id"] == "ARCHITECTURE_SYNTHESIS"
                and entry.get("lifecycle", "current") != "historical"
            )
            marker = "### CURRENT AUTHORITY"
            end_marker = "### CURRENT DERIVED EVIDENCE"
            start = contract.index(marker)
            end = contract.index(end_marker, start)
            authority = contract[start:end]
            current_route = f"`{architecture['canonical_filename']}`"
            self.assertIn(current_route, authority)
            archived_route = f"`archive/{architecture['canonical_filename']}`"
            authority = authority.replace(current_route, archived_route, 1)
            contract_path.write_text(contract[:start] + authority + contract[end:], encoding="utf-8")

            report = run_smoke_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    check["name"] == "current_authority_route_resolution" and check["status"] == "FAIL"
                    for check in report["checks"]
                ),
                report["checks"],
            )

    def test_smoke_accepts_a_successor_with_archived_predecessor(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._fixture(directory)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            open_work = next(item for item in manifest["governing_documents"] if item["document_id"] == "OPEN_WORK")
            old_relative = Path(open_work["repository_path"])
            old_path = root / old_relative
            archive_path = root / "docs/00_platform/archive" / old_path.name
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            old_path.rename(archive_path)

            old_version = str(open_work["semver"])
            major, minor, patch = (int(part) for part in old_version.split("."))
            new_version = f"{major}.{minor}.{patch + 1}"
            new_filename = f"02_OPEN_WORK_v{new_version}.md"
            new_relative = (Path("docs/00_platform") / new_filename).as_posix()
            new_path = root / "docs/00_platform" / new_filename
            text = archive_path.read_text(encoding="utf-8")
            text = re.sub(r"(?m)^# 02_OPEN_WORK_v\d+\.\d+\.\d+\.md$", f"# {new_filename}", text, count=1)
            text = re.sub(
                r"(?m)^- \*\*Document status:\*\* PRODUCT LAW AND GOVERNANCE OPEN-WORK SUCCESSOR v\d+\.\d+\.\d+$",
                f"- **Document status:** PRODUCT LAW AND GOVERNANCE OPEN-WORK SUCCESSOR v{new_version}",
                text,
                count=1,
            )
            text = re.sub(
                r"(?m)^- \*\*Document version:\*\* v\d+\.\d+\.\d+$",
                f"- **Document version:** v{new_version}",
                text,
                count=1,
            )
            text = re.sub(
                r"(?m)^- \*\*Predecessor:\*\* `archive/[^`]+`",
                f"- **Predecessor:** `archive/{archive_path.name}`",
                text,
                count=1,
            )
            text = re.sub(r"(?<!archive/)02_OPEN_WORK_v\d+\.\d+\.\d+\.md", new_filename, text)
            text = re.sub(r"current Open Work v\d+\.\d+\.\d+", f"current Open Work v{new_version}", text)
            new_path.write_text(text, encoding="utf-8")
            open_work.update(
                {
                    "canonical_filename": new_filename,
                    "semver": new_version,
                    "repository_path": new_relative,
                    "superseded_version": old_version,
                }
            )
            manifest["historical_documents"].append(
                {
                    "document_id": "OPEN_WORK_V" + old_version.replace(".", "_"),
                    "canonical_filename": archive_path.name,
                    "semver": old_version,
                    "repository_path": "docs/00_platform/archive/" + archive_path.name,
                    "authority_class": "PLANNING_TRACKER_ARCHIVE",
                    "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(),
                    "superseded_version": new_version,
                    "lifecycle": "historical",
                }
            )

            def update_current_paths(value):
                if isinstance(value, dict):
                    return {key: update_current_paths(item) for key, item in value.items()}
                if isinstance(value, list):
                    return [update_current_paths(item) for item in value]
                if value == old_relative.as_posix():
                    return new_relative
                return value

            manifest = update_current_paths(manifest)
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

            readme_path = root / "docs/00_platform/README.md"
            readme = readme_path.read_text(encoding="utf-8")
            readme = re.sub(r"(?<!archive/)02_OPEN_WORK_v\d+\.\d+\.\d+\.md", new_filename, readme)
            readme = re.sub(r"current Open Work v\d+\.\d+\.\d+", f"current Open Work v{new_version}", readme)
            readme_path.write_text(readme, encoding="utf-8")
            for route in manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]:
                route_path = root / route
                if route_path.is_file():
                    route_text = route_path.read_text(encoding="utf-8")
                    route_text = re.sub(r"(?<!archive/)02_OPEN_WORK_v\d+\.\d+\.\d+\.md", new_filename, route_text)
                    route_text = re.sub(
                        r"current Open Work v\d+\.\d+\.\d+", f"current Open Work v{new_version}", route_text
                    )
                    route_path.write_text(route_text, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_smoke_audit(root, manifest_path)

            self.assertEqual("PASS", report["status"], report["findings"])
            self.assertTrue(archive_path.is_file())
            self.assertTrue(new_path.is_file())

    def test_governance_sensitive_paths_trigger_foundation_full(self):
        decision = classify_changed_paths(
            ["docs/00_platform/02_OPEN_WORK_v1.2.78.md", "tools/foundation_integrity_audit.py"]
        )
        self.assertTrue(decision["foundation_full"])
        self.assertFalse(decision["application_changes"])

    def test_pull_request_path_diff_routes_application_and_governance_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            def git(*args):
                return subprocess.run(
                    ["git", *args], cwd=root, check=True, capture_output=True, text=True
                ).stdout.strip()

            git("init", "--quiet")
            git("config", "user.email", "foundation-smoke@example.invalid")
            git("config", "user.name", "Foundation Smoke Test")
            (root / "mix.exs").write_text("defmodule Fixture.MixProject do end\n", encoding="utf-8")
            (root / "assets").mkdir()
            (root / "assets/café.svg").write_text("<svg/>\n", encoding="utf-8")
            git("add", ".")
            git("commit", "--quiet", "-m", "baseline")
            base_sha = git("rev-parse", "HEAD")

            (root / "assets/café.svg").write_text("<svg><!-- update --></svg>\n", encoding="utf-8")
            git("commit", "--quiet", "-am", "application-only change")
            app_sha = git("rev-parse", "HEAD")
            app_decision = classify_event("pull_request", base_sha, app_sha, str(root))
            self.assertFalse(app_decision["foundation_full"])
            self.assertTrue(app_decision["application_changes"])

            (root / "docs").mkdir()
            (root / "docs/authority.md").write_text("governed change\n", encoding="utf-8")
            git("add", ".")
            git("commit", "--quiet", "-m", "governance change")
            governance_sha = git("rev-parse", "HEAD")
            governance_decision = classify_event("pull_request", app_sha, governance_sha, str(root))
            self.assertTrue(governance_decision["foundation_full"])

    def test_renamed_governance_artifact_into_application_path_routes_full(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            def git(*args):
                return subprocess.run(
                    ["git", *args], cwd=root, check=True, capture_output=True, text=True
                ).stdout.strip()

            git("init", "--quiet")
            git("config", "user.email", "foundation-smoke@example.invalid")
            git("config", "user.name", "Foundation Smoke Test")
            (root / "docs").mkdir()
            (root / "docs/authority.md").write_text("governance evidence\n", encoding="utf-8")
            git("add", ".")
            git("commit", "--quiet", "-m", "baseline")
            base_sha = git("rev-parse", "HEAD")

            (root / "lib").mkdir()
            git("mv", "docs/authority.md", "lib/authority.ex")
            git("commit", "--quiet", "-m", "move evidence into application tree")
            head_sha = git("rev-parse", "HEAD")

            decision = classify_event("pull_request", base_sha, head_sha, str(root))

            self.assertTrue(decision["foundation_full"])

    def test_application_only_paths_do_not_trigger_foundation_full(self):
        decision = classify_changed_paths(
            ["mix.exs", "mix.lock", "lib/new_you/accounts.ex", "test/new_you/accounts_test.exs"]
        )
        self.assertFalse(decision["foundation_full"])
        self.assertTrue(decision["application_changes"])

    def test_empty_change_range_fails_closed_to_foundation_full(self):
        decision = classify_changed_paths([])
        self.assertTrue(decision["foundation_full"])
        self.assertFalse(decision["application_changes"])

    def test_unknown_paths_fail_closed_to_foundation_full(self):
        decision = classify_changed_paths(["new-governance-surface/authority.md"])
        self.assertTrue(decision["foundation_full"])

    def test_literal_backslash_filename_does_not_become_application_path(self):
        decision = classify_changed_paths([r"lib\authority.md"])
        self.assertTrue(decision["foundation_full"])
        self.assertFalse(decision["application_changes"])

    def test_manual_dispatch_selects_full_lane(self):
        decision = classify_event("workflow_dispatch", "", "", str(ROOT))
        self.assertTrue(decision["foundation_full"])

    def test_manual_full_workflow_uses_and_verifies_an_exact_sha(self):
        workflow = (ROOT / ".github/workflows/foundation-integrity.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("sha:", workflow)
        self.assertIn("inputs.sha", workflow)
        self.assertIn('if [[ "$actual" != "$expected" ]]', workflow)
        self.assertIn('if [[ "$GITHUB_SHA" != "$expected" ]]', workflow)
        self.assertIn("needs.route.outputs.foundation_full == 'true'", workflow)
        self.assertIn("python tools/foundation_integrity_routing.py --root .", workflow)
        self.assertIn("  foundation-integrity:\n    name: Foundation Integrity", workflow)
        self.assertIn("needs: [route, foundation-smoke, foundation-full]", workflow)
        smoke_job = workflow.split("  foundation-smoke:\n", 1)[1].split("\n  foundation-full:", 1)[0]
        self.assertNotRegex(smoke_job, r"(?m)^    if:")
        self.assertIn("fetch-depth: 1", smoke_job)
        self.assertNotIn("fetch-depth: 0", smoke_job)


if __name__ == "__main__":
    unittest.main()
