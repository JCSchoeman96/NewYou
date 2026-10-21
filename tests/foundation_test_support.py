"""Manifest-aware path helpers for current and historical governance tests."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
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


def manifest_data(root: Path) -> dict[str, Any]:
    return json.loads((Path(root) / MANIFEST_RELATIVE).read_text(encoding="utf-8"))


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
            if entry.get("repository_path") == relative
            and entry.get("lifecycle") == "historical"
        ]
        digest = hashlib.sha256(archived.read_bytes()).hexdigest()
        if (
            len(matching) != 1
            or matching[0].get("sha256") != digest
            or matching[0].get("provenance_sha256") != digest
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
    if len(candidates) != 1 or not candidates[0].is_file():
        raise AssertionError(f"historical snapshot is not archived or active at baseline: {filename}")
    return candidates[0]
