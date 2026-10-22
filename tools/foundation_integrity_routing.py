#!/usr/bin/env python3
"""Route repository changes to Foundation Full and the application CI lane.

Every changed path is classified into exactly one category:

* ``application``: normal engineering files (application source, root
  engineering files, engineering skills and tooling). These run Application CI
  and never trigger Foundation Full on their own.
* ``governance``: the governed authority tree and the historical governance
  audit, test and workflow machinery. These trigger Foundation Full.
* ``unknown``: anything unclassified. Unknown paths fail closed to Full.

Pull requests are routed from their exact diff. A ``push`` to ``main`` never
routes Foundation Full. Governance-sensitive PRs automatically start the cold
Full lane as non-blocking historical evidence; the required Foundation
Integrity merge gate does not wait for it. Ordinary application PRs run
Application CI and Foundation Smoke without Full. Superseded PR workflow runs
are cancelled by the workflow concurrency policy. Scheduled nightly hardening
separately runs Foundation Full and ``mix check.deep`` against ``main``.
Deliberate exact-SHA certification is dispatched directly through the
Foundation Full workflow. If this classifier is invoked for a
``workflow_dispatch`` event it still fails closed to Full.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import PurePosixPath


# --- Application / normal engineering --------------------------------------

APPLICATION_FILES = frozenset(
    {
        "mix.exs",
        "mix.lock",
        ".formatter.exs",
        ".tool-versions",
        ".gitignore",
        ".gitattributes",
        ".credo.exs",
        "README.md",
        "AGENTS.md",
        ".github/workflows/application-ci.yml",
    }
)

APPLICATION_PREFIXES = (
    ".agents/",
    ".devcore/",
    "assets/",
    "config/",
    "lib/",
    "priv/",
    "test/",
    "tools/architecture/",
)

# --- Governance (historical authority and its audit machinery) -------------

GOVERNANCE_FILES = frozenset(
    {
        "tools/__init__.py",
        ".github/workflows/foundation-integrity.yml",
        ".github/workflows/foundation-full.yml",
    }
)

# `docs/` is the governed documentation tree. `tests/` is the historical Python
# governance suite; normal Elixir tests live under `test/`.
GOVERNANCE_PREFIXES = (
    "docs/",
    "tests/",
    "tools/foundation_integrity_",
)


def classify_path(path: str) -> str:
    """Return ``application``, ``governance`` or ``unknown`` for one repo path."""

    normalized = path.removeprefix("./")
    parts = PurePosixPath(normalized).parts
    if not normalized or normalized.startswith("/") or ".." in parts:
        return "unknown"
    if normalized in GOVERNANCE_FILES or normalized.startswith(GOVERNANCE_PREFIXES):
        return "governance"
    if normalized in APPLICATION_FILES or normalized.startswith(APPLICATION_PREFIXES):
        return "application"
    return "unknown"


def is_application_path(path: str) -> bool:
    """Return True only for normal engineering paths."""

    return classify_path(path) == "application"


def classify_changed_paths(paths: list[str]) -> dict[str, bool]:
    """Route a list of changed paths.

    * Empty change ranges fail closed to Foundation Full.
    * Governance and unknown paths select Foundation Full.
    * Application or engineering paths select Application CI.
    """

    normalized = [path for path in paths if path]
    if not normalized:
        return {"foundation_full": True, "application_changes": False}
    categories = {classify_path(path) for path in normalized}
    return {
        "foundation_full": bool(categories & {"governance", "unknown"}),
        "application_changes": "application" in categories,
    }


def _changed_paths(event_name: str, base_sha: str, head_sha: str, cwd: str) -> list[str]:
    separator = "..." if event_name == "pull_request" else ".."
    result = subprocess.run(
        ["git", "diff", "--no-renames", "--name-only", "-z", f"{base_sha}{separator}{head_sha}"],
        cwd=cwd,
        capture_output=True,
        check=True,
    )
    return [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]


def classify_event(event_name: str, base_sha: str, head_sha: str, cwd: str = ".") -> dict[str, bool]:
    """Classify a GitHub event, failing closed when its change range is unknown."""

    if event_name == "workflow_dispatch":
        return {"foundation_full": True, "application_changes": False}
    if event_name == "push":
        # The required push gate is Smoke plus any routed Application CI.
        # Foundation Full is retained separately by nightly/manual hardening.
        if not base_sha or not head_sha:
            return {"foundation_full": False, "application_changes": True}
        try:
            paths = _changed_paths(event_name, base_sha, head_sha, cwd)
        except (OSError, subprocess.CalledProcessError):
            return {"foundation_full": False, "application_changes": True}
        decision = classify_changed_paths(paths)
        return {"foundation_full": False, "application_changes": decision["application_changes"]}
    if event_name != "pull_request" or not base_sha or not head_sha:
        return {"foundation_full": True, "application_changes": False}
    try:
        paths = _changed_paths(event_name, base_sha, head_sha, cwd)
    except (OSError, subprocess.CalledProcessError):
        return {"foundation_full": True, "application_changes": False}
    return classify_changed_paths(paths)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", default=os.environ.get("GITHUB_EVENT_NAME", ""))
    parser.add_argument("--base-sha", default=os.environ.get("BASE_SHA", ""))
    parser.add_argument("--head-sha", default=os.environ.get("HEAD_SHA", ""))
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)

    decision = classify_event(args.event, args.base_sha, args.head_sha, args.root)
    print(f"foundation_full={str(decision['foundation_full']).lower()}")
    print(f"application_changes={str(decision['application_changes']).lower()}")
    if decision["foundation_full"]:
        print("Foundation Full selected as non-blocking historical evidence.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
