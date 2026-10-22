#!/usr/bin/env python3
"""Route repository changes to Foundation Full or the application lane."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import PurePosixPath


APPLICATION_FILES = {"mix.exs", "mix.lock", ".formatter.exs"}
APPLICATION_ROOTS = {"apps", "assets", "config", "lib", "priv", "test"}


def is_application_path(path: str) -> bool:
    """Return True only for paths reserved for governed application work."""

    normalized = path.removeprefix("./")
    parts = PurePosixPath(normalized).parts
    if not normalized or normalized.startswith("/") or ".." in parts:
        return False
    return normalized in APPLICATION_FILES or bool(parts and parts[0] in APPLICATION_ROOTS)


def classify_changed_paths(paths: list[str]) -> dict[str, bool]:
    """Unknown or mixed paths require Full; application-only paths do not."""

    normalized = [path for path in paths if path]
    if not normalized:
        return {"foundation_full": True, "application_changes": False}
    app_changes = any(is_application_path(path) for path in normalized)
    non_application_changes = any(not is_application_path(path) for path in normalized)
    return {
        "foundation_full": non_application_changes,
        "application_changes": app_changes,
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
    if event_name not in {"pull_request", "push"} or not base_sha or not head_sha:
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
        print("Foundation Full required for this change range.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
