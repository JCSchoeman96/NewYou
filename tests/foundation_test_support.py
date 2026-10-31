"""Manifest-aware path helpers for current and historical governance tests."""

from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path
from typing import Any


MANIFEST_RELATIVE = Path("docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
WELL38_BASE_SHA = "4234965c8da20dbb4ef0a7128614a5070244619a"
FOUNDATION_WORKFLOW_BASELINE_SHA256 = "5e63c77707fe767bbb89a38f4cfe1d9c972d4aefdcc13296bf5048cd4a3ae0f3"


def git_snapshot_bytes(root: Path, revision: str, repository_path: str) -> bytes:
    """Read a committed historical artifact without requiring it to stay current."""

    result = subprocess.run(
        ["git", "show", f"{revision}:{repository_path}"],
        cwd=Path(root),
        capture_output=True,
        check=True,
    )
    return result.stdout


def _exact_git_tree(root: Path, revision: str) -> str:
    """Resolve only an immutable full object ID; missing history is an error."""

    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("historical revision must be a full 40-character Git object ID")
    return subprocess.run(
        ["git", "rev-parse", "--verify", f"{revision}^{{tree}}"],
        cwd=Path(root), capture_output=True, text=True, check=True,
    ).stdout.strip()


def git_snapshot_path_exists(root: Path, revision: str, repository_path: str) -> bool:
    """Test file or directory existence in an exact tree, never the checkout."""

    tree = _exact_git_tree(root, revision)
    paths = subprocess.run(
        ["git", "ls-tree", "--full-tree", "-r", "--name-only", "-z", tree],
        cwd=Path(root), capture_output=True, text=True, check=True,
    ).stdout.split("\0")
    return any(path == repository_path or path.startswith(repository_path.rstrip("/") + "/") for path in paths)


def git_snapshot_directory_names(root: Path, revision: str, directory: str) -> list[str]:
    """Immediate child names of a directory in an exact historical tree, never the checkout."""

    tree = _exact_git_tree(root, revision)
    paths = subprocess.run(
        ["git", "ls-tree", "--full-tree", "-r", "--name-only", "-z", tree],
        cwd=Path(root), capture_output=True, text=True, check=True,
    ).stdout.split("\0")
    prefix = directory.rstrip("/") + "/"
    return sorted({path[len(prefix):].split("/", 1)[0] for path in paths if path.startswith(prefix)})


def git_changed_paths(root: Path, base_revision: str, candidate_revision: str) -> list[str]:
    """Compare two exact trees without including HEAD or working-tree changes."""

    base = _exact_git_tree(root, base_revision)
    candidate = _exact_git_tree(root, candidate_revision)
    result = subprocess.run(
        ["git", "diff", "--no-renames", "--name-only", "-z", base, candidate, "--"],
        cwd=Path(root), capture_output=True, text=True, check=True,
    )
    return sorted(path for path in result.stdout.split("\0") if path)


def copy_git_snapshot_tree(
    repository_root: Path,
    revision: str,
    destination: Path,
    *repository_paths: str,
) -> None:
    """Materialize committed paths as a content fixture without a .git directory."""

    result = subprocess.run(
        ["git", "archive", "--format=tar", revision, *repository_paths],
        cwd=Path(repository_root),
        capture_output=True,
        check=True,
    )
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(result.stdout), mode="r:") as archive:
        archive.extractall(destination, filter="data")


def manifest_data(root: Path) -> dict[str, Any]:
    return json.loads((Path(root) / MANIFEST_RELATIVE).read_text(encoding="utf-8"))


def frozen_manifest_document_path(root: Path, entry: dict[str, Any]) -> Path:
    """Resolve a frozen manifest document at its original or byte-pinned archive path."""

    root = Path(root)
    repository_path = Path(str(entry.get("repository_path", "")))
    path = root / repository_path
    canonical_filename = str(entry.get("canonical_filename", ""))
    expected_hash = entry.get("sha256")
    expected_provenance_hash = entry.get("provenance_sha256")

    def matches_frozen_bytes(candidate: Path) -> bool:
        if not candidate.is_file() or candidate.is_symlink() or not isinstance(expected_hash, str):
            return False
        digest = hashlib.sha256(candidate.read_bytes()).hexdigest()
        return digest == expected_hash and (
            expected_provenance_hash is None or digest == expected_provenance_hash
        )

    if matches_frozen_bytes(path):
        return path

    archived = root / "docs/00_platform/archive" / canonical_filename
    if (
        repository_path.name == canonical_filename
        and matches_frozen_bytes(archived)
    ):
        return archived

    raise AssertionError(f"frozen manifest document is missing or does not match its pinned bytes: {repository_path}")


def current_document_path(root: Path, document_id: str) -> Path:
    root = Path(root)
    manifest = manifest_data(root)
    matches = [
        entry
        for group in ("governing_documents", "reference_documents", "historical_documents")
        for entry in manifest.get(group, [])
        if entry.get("document_id") == document_id
        and entry.get("lifecycle", "current") != "historical"
    ]
    if len(matches) != 1:
        raise AssertionError(f"expected one current manifest route for {document_id}, found {len(matches)}")
    return root / matches[0]["repository_path"]


def current_document_relative_path(root: Path, document_id: str) -> str:
    """Return a current manifest route relative to the repository root."""

    return current_document_path(root, document_id).relative_to(Path(root).resolve()).as_posix()


def current_working_path(root: Path, filename_prefix: str) -> Path:
    root = Path(root)
    manifest = manifest_data(root)
    graph_rules = manifest.get("integrity_rules", {}).get("graph_rules", {})
    routes = [
        Path(route)
        for route in graph_rules.get("navigation_document_paths", [])
        if Path(route).name.startswith(filename_prefix)
    ]
    if not routes:
        readme = (root / "docs/00_platform/README.md").read_text(encoding="utf-8")
        section = readme.split("## Active Working Artifacts", 1)[-1].split("\n## ", 1)[0]
        routes = [
            Path("docs/00_platform") / route
            for route in re.findall(r"`(working/[^`\s]+\.md)`", section)
            if Path(route).name.startswith(filename_prefix)
        ]
    if len(routes) != 1:
        raise AssertionError(f"expected one current working route for {filename_prefix}, found {routes}")
    route = routes[0]
    if "archive" in route.parts:
        raise AssertionError(f"current working route points into archive: {route}")
    path = root / route
    if not path.is_file():
        raise AssertionError(f"current working route does not exist: {path}")
    return path


def current_working_relative_path(root: Path, filename_prefix: str) -> str:
    """Return a current working route relative to the repository root."""

    return current_working_path(root, filename_prefix).relative_to(Path(root).resolve()).as_posix()


def historical_snapshot_path(root: Path, filename: str) -> Path:
    """Read a pinned archive snapshot when present, or its active baseline path."""

    root = Path(root)
    docs = root / "docs/00_platform"
    archived = docs / "archive" / Path(filename).name
    if archived.is_file():
        relative = archived.resolve().relative_to(root.resolve()).as_posix()
        manifest = manifest_data(root)
        matching = [
            entry
            for group in ("governing_documents", "reference_documents", "historical_documents")
            for entry in manifest.get(group, [])
            if (
                entry.get("repository_path") == relative
                and entry.get("lifecycle") == "historical"
            )
            or (
                Path(entry.get("repository_path", "")).name == archived.name
                and entry.get("canonical_filename") == archived.name
                and entry.get("lifecycle", "current") != "historical"
            )
        ]
        digest = hashlib.sha256(archived.read_bytes()).hexdigest()
        if (
            len(matching) != 1
            or digest not in {
                matching[0].get("sha256"),
                matching[0].get("provenance_sha256"),
            }
        ):
            raise AssertionError(f"historical archive is not uniquely pinned by the manifest: {relative}")
        return archived

    candidates = [
        root / entry["repository_path"]
        for group in ("governing_documents", "reference_documents", "historical_documents")
        for entry in manifest_data(root).get(group, [])
        if Path(entry.get("repository_path", "")).name == Path(filename).name
        and entry.get("lifecycle", "current") != "historical"
    ]
    candidates.extend(
        root / route
        for route in manifest_data(root)
        .get("integrity_rules", {})
        .get("graph_rules", {})
        .get("navigation_document_paths", [])
        if Path(route).name == Path(filename).name
    )
    candidates = list(dict.fromkeys(candidates))
    if len(candidates) != 1 or not candidates[0].is_file():
        raise AssertionError(f"historical snapshot is not archived or active at baseline: {filename}")
    return candidates[0]
