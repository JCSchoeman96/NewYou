#!/usr/bin/env python3
"""Run the frozen Python suite with its bounded pre-migration path view."""

from __future__ import annotations

import subprocess
import sys
import tarfile
import tempfile
import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRE_MIGRATION_BASE_SHA = "a2dfeff5d6cf88d7534cd100c28f39d3045bc814"


def main() -> int:
    """Expose the pinned pre-migration tree at legacy test paths during the suite."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--test", help="run one unittest by fully qualified name")
    args = parser.parse_args()

    links: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="newyou-foundation-test-legacy-view-") as directory:
        legacy_root = Path(directory)
        archive = subprocess.run(
            [
                "git",
                "archive",
                "--format=tar",
                PRE_MIGRATION_BASE_SHA,
                "docs/00_platform",
                "docs/execution",
            ],
            cwd=ROOT,
            capture_output=True,
            check=True,
        )
        import io

        with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as source:
            source.extractall(legacy_root, filter="data")
        try:
            for relative in ("docs/00_platform", "docs/execution"):
                target = legacy_root / relative
                if not target.exists():
                    continue
                link = ROOT / relative
                if link.exists() or link.is_symlink():
                    raise RuntimeError(f"legacy compatibility path already exists: {link}")
                link.symlink_to(target, target_is_directory=True)
                links.append(link)
            command = (
                [sys.executable, "-m", "unittest", args.test, "-v"]
                if args.test
                else [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
            )
            environment = os.environ.copy()
            environment["PYTHONPATH"] = os.pathsep.join(
                [str(ROOT / "tests"), str(ROOT), environment.get("PYTHONPATH", "")]
            )
            result = subprocess.run(command, cwd=ROOT, env=environment, check=False)
        finally:
            for link in reversed(links):
                link.unlink(missing_ok=True)
        return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
