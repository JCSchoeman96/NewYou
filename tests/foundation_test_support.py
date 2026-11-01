"""Manifest-aware path helpers for historical and current governance certification."""

from __future__ import annotations

import hashlib
import io
import json
import re
import shutil
import subprocess
import tarfile
from pathlib import Path
from typing import Any


MANIFEST_RELATIVE = Path("docs/history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
ROUTER_RELATIVE = Path("docs/delivery/CURRENT_DELIVERY_ROUTER.json")
FROZEN_ROUTER_RELATIVE = Path("docs/history/platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json")
LIVE_README_RELATIVE = Path("docs/README.md")
HISTORICAL_README_RELATIVE = Path("docs/history/platform/archive/README_PRE_WELL66_2026-10-30.md")
HISTORICAL_README_SHA256 = "1911f27b675aacae648f3c876361de28fb0a5b650262590aa5bb9ad4d1954649"

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
    materialize_historical_readme: bool = False,
) -> None:
    """Materialize committed paths as a content fixture without a .git directory."""

    repository_root = Path(repository_root)
    result = subprocess.run(
        ["git", "archive", "--format=tar", revision, *repository_paths],
        cwd=repository_root,
        capture_output=True,
        check=True,
    )
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(result.stdout), mode="r:") as archive:
        archive.extractall(destination, filter="data")
    if materialize_historical_readme:
        materialize_historical_platform_readme(destination, source_root=repository_root)


def git_repository_path_for_revision(path: Path, root: Path) -> str:
    """Map a fixture path to the git object path at an immutable revision."""

    relative = path.relative_to(root).as_posix()
    if relative == HISTORICAL_README_RELATIVE.as_posix():
        return "docs/00_platform/README.md"
    return relative


def git_show_text_at_revision(root: Path, revision: str, path: Path) -> str:
    """Read committed file text; archived historical README uses live README at that revision."""

    repository_path = git_repository_path_for_revision(path, root)
    return subprocess.check_output(
        ["git", "show", f"{revision}:{repository_path}"],
        cwd=Path(root),
    ).decode("utf-8")


def materialize_historical_readme_at_revision(
    root: Path,
    repository_root: Path,
    revision: str,
) -> Path:
    """Write the README bytes from an immutable revision into the archived historical README path."""

    text = git_show_text_at_revision(
        repository_root,
        revision,
        repository_root / HISTORICAL_README_RELATIVE,
    )
    destination = Path(root) / HISTORICAL_README_RELATIVE
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")
    return destination


def materialize_historical_platform_readme(
    root: Path,
    *,
    source_root: Path | None = None,
) -> Path:
    """Copy the byte-pinned pre-WELL-66 README into a fixture tree."""

    source_root = Path(source_root or root)
    destination = Path(root) / HISTORICAL_README_RELATIVE
    destination.parent.mkdir(parents=True, exist_ok=True)
    source = source_root / HISTORICAL_README_RELATIVE
    _assert_pinned_regular_file(
        source,
        HISTORICAL_README_SHA256,
        label="historical platform README source",
    )
    shutil.copy2(source, destination)
    return destination


def manifest_data(root: Path) -> dict[str, Any]:
    root = Path(root)
    path = root / MANIFEST_RELATIVE
    if not path.is_file():
        path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
    return json.loads(path.read_text(encoding="utf-8"))


def current_router_data(root: Path) -> dict[str, Any]:
    root = Path(root)
    path = root / ROUTER_RELATIVE
    if not path.is_file():
        path = root / FROZEN_ROUTER_RELATIVE
    if not path.is_file():
        path = root / "docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json"
    return json.loads(path.read_text(encoding="utf-8"))


def current_governance_router_data(root: Path) -> dict[str, Any]:
    """Load the current durable-law router, with no delivery fallback."""

    path = Path(root) / "docs/governance/CURRENT_GOVERNANCE_ROUTER.json"
    return json.loads(path.read_text(encoding="utf-8"))


def frozen_router_data(root: Path) -> dict[str, Any]:
    root = Path(root)
    path = root / FROZEN_ROUTER_RELATIVE
    if not path.is_file():
        path = root / "docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_pinned_regular_file(path: Path, expected_sha256: str, *, label: str) -> None:
    if not path.is_file() or path.is_symlink():
        raise AssertionError(f"{label} is missing or not a regular file: {path}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != expected_sha256:
        raise AssertionError(
            f"{label} digest mismatch: expected {expected_sha256}, got {digest}"
        )


def historical_platform_readme_path(root: Path) -> Path:
    """Byte-pinned pre-WELL-66 README used for frozen-manifest historical certification."""

    root = Path(root)
    path = root / HISTORICAL_README_RELATIVE
    if not path.is_file():
        path = root / "docs/00_platform/archive/README_PRE_WELL66_2026-10-30.md"
    _assert_pinned_regular_file(path, HISTORICAL_README_SHA256, label="historical platform README")
    return path


def historical_platform_readme_text(root: Path) -> str:
    return historical_platform_readme_path(root).read_text(encoding="utf-8")


def live_platform_readme_path(root: Path) -> Path:
    root = Path(root)
    path = root / LIVE_README_RELATIVE
    if not path.is_file():
        path = root / "docs/00_platform/README.md"
    if not path.is_file() or path.is_symlink():
        raise AssertionError(f"live platform README is missing: {path}")
    return path


def live_platform_readme_text(root: Path) -> str:
    return live_platform_readme_path(root).read_text(encoding="utf-8")


def frozen_open_work_path(root: Path) -> Path:
    """Frozen legacy Open Work snapshot pinned by the retained mixed-router snapshot."""

    root = Path(root)
    try:
        router = frozen_router_data(root)
    except FileNotFoundError:
        # Older pinned audit fixtures predate the mixed router. Resolve their
        # then-current Open Work route from that fixture's manifest.
        manifest = manifest_data(root)
        entries = [
            entry
            for group in ("governing_documents", "reference_documents", "historical_documents")
            for entry in manifest.get(group, [])
            if entry.get("document_id") == "OPEN_WORK"
            and entry.get("lifecycle", "current") != "historical"
        ]
        if len(entries) == 1:
            entry = entries[0]
            path = root / str(entry.get("repository_path", ""))
            if not path.is_file():
                path = root / "docs/00_platform" / str(entry.get("canonical_filename", ""))
            expected_hash = str(entry.get("sha256", ""))
            if path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash:
                return path
        raise AssertionError("legacy Open Work route is unavailable in the pinned fixture")
    entry = next(
        item
        for item in router["legacy_snapshots"]
        if item.get("document_id") == "OPEN_WORK_FINAL_LEGACY_SNAPSHOT"
    )
    path = root / "docs/history/02_OPEN_WORK_v1.2.90.md"
    if not path.is_file():
        path = root / entry["repository_path"]
    _assert_pinned_regular_file(path, str(entry["sha256"]), label="frozen Open Work snapshot")
    if entry.get("live_execution_authority"):
        raise AssertionError("frozen Open Work must not be live execution authority")
    return path


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

    archived_candidates = [
        root / "docs/history/platform/archive" / canonical_filename,
        root / "docs/00_platform/archive" / canonical_filename,
    ]
    for archived in archived_candidates:
        if repository_path.name == canonical_filename and matches_frozen_bytes(archived):
            return archived

    if isinstance(expected_hash, str):
        docs = root / "docs"
        if docs.is_dir():
            matches = []
            for candidate in docs.rglob(canonical_filename):
                if matches_frozen_bytes(candidate):
                    matches.append(candidate)
            if len(matches) == 1:
                return matches[0]

    raise AssertionError(
        f"frozen manifest document is missing or does not match its pinned bytes: {repository_path}"
    )


def frozen_manifest_document_by_id(root: Path, document_id: str) -> Path:
    """Resolve a non-historical manifest document route in frozen-manifest certification context."""

    root = Path(root)
    if document_id == "OPEN_WORK":
        return frozen_open_work_path(root)
    manifest = manifest_data(root)
    matches = [
        entry
        for group in ("governing_documents", "reference_documents", "historical_documents")
        for entry in manifest.get(group, [])
        if entry.get("document_id") == document_id
        and entry.get("lifecycle", "current") != "historical"
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"expected one frozen-manifest route for {document_id}, found {len(matches)}"
        )
    return frozen_manifest_document_path(root, matches[0])


def current_document_path(root: Path, document_id: str) -> Path:
    """Resolve a current governance route, retaining frozen Open Work as history."""

    root = Path(root)
    if document_id == "OPEN_WORK":
        return frozen_open_work_path(root)
    router_path = root / "docs/governance/CURRENT_GOVERNANCE_ROUTER.json"
    if router_path.is_file():
        router = json.loads(router_path.read_text(encoding="utf-8"))
        aliases = {
            "PROJECT_NORTH_STAR_AND_MVP": "NORTH_STAR_AND_MVP",
            "PLATFORM_BASELINE": "PLATFORM_PRODUCT_LAW",
            "DECISION_REGISTER": "PRODUCT_DECISIONS",
            "ARCHITECTURE_SYNTHESIS": "ARCHITECTURE_LAW",
            "DOMAIN_MAP": "DOMAIN_LAW",
            "ROADMAP": "GOVERNING_ROADMAP",
        }
        target_id = aliases.get(document_id, document_id)
        entries = [
            entry
            for collection in ("governing_documents", "architecture_references", "supporting_documents")
            for entry in router.get(collection, [])
            if entry.get("document_id") == target_id
        ]
        if len(entries) == 1:
            path = root / entries[0]["repository_path"]
            if not path.is_file() or path.is_symlink():
                raise AssertionError(f"current governance route is missing: {path}")
            return path
    return frozen_manifest_document_by_id(root, document_id)


def current_document_relative_path(root: Path, document_id: str) -> str:
    return current_document_path(root, document_id).relative_to(
        Path(root).resolve()
    ).as_posix()


def _historical_readme_working_routes(text: str, filename_prefix: str) -> list[Path]:
    if "## Active Working Artifacts" not in text:
        return []
    section = text.split("## Active Working Artifacts", 1)[-1].split("\n## ", 1)[0]
    return [
        Path("docs/00_platform") / route
        for route in re.findall(r"`(working/[^`\s]+\.md)`", section)
        if Path(route).name.startswith(filename_prefix)
    ]


def frozen_manifest_working_path(root: Path, filename_prefix: str) -> Path:
    """Working artifact route according to the frozen manifest and historical README."""

    root = Path(root)
    return current_router_working_path(root, filename_prefix)


def current_working_path(root: Path, filename_prefix: str) -> Path:
    """Alias: frozen-manifest working route for historical Foundation certification."""

    return frozen_manifest_working_path(root, filename_prefix)


def current_router_working_path(root: Path, filename_prefix: str) -> Path:
    """Delivery contract route from the current delivery router."""

    root = Path(root)
    router_path = root / ROUTER_RELATIVE
    if not router_path.is_file():
        router_path = root / FROZEN_ROUTER_RELATIVE
    if not router_path.is_file():
        router_path = root / "docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json"

    router = json.loads(router_path.read_text(encoding="utf-8")) if router_path.is_file() else {}
    if "delivery_contracts" in router:
        routes = [
            Path(entry["repository_path"])
            for entry in router.get("delivery_contracts", [])
            if Path(entry.get("repository_path", "")).name.startswith(filename_prefix)
        ]
    else:
        routes = [
            Path(route)
            for route in router.get("working_semantic_routes", [])
            if Path(route).name.startswith(filename_prefix)
        ]
    if not routes:
        historical_readme_path = root / HISTORICAL_README_RELATIVE
        if not historical_readme_path.is_file():
            historical_readme_path = (
                root / "docs/00_platform/archive/README_PRE_WELL66_2026-10-30.md"
            )
        historical_readme = historical_readme_path.read_text(encoding="utf-8")
        routes = _historical_readme_working_routes(historical_readme, filename_prefix)
    if len(routes) != 1:
        raise AssertionError(
            f"expected one current-router working route for {filename_prefix}, found {routes}"
        )
    path = root / routes[0]
    if not path.is_file() or path.is_symlink():
        raise AssertionError(f"current-router working route does not exist: {path}")
    return path


def current_working_relative_path(root: Path, filename_prefix: str) -> str:
    return current_router_working_path(root, filename_prefix).relative_to(
        Path(root).resolve()
    ).as_posix()


def historical_snapshot_path(root: Path, filename: str) -> Path:
    """Read a pinned archive snapshot when present, or its active baseline path."""

    root = Path(root)
    docs = root / "docs"
    archived_name = Path(filename).name
    candidates_on_disk = [
        path for path in (docs / "history").rglob(archived_name)
    ] if (docs / "history").is_dir() else []
    candidates_on_disk.extend(
        [path for path in (docs / "00_platform/archive").rglob(archived_name)]
        if (docs / "00_platform/archive").is_dir()
        else []
    )
    manifest = manifest_data(root)
    matching = [
        entry
        for group in ("governing_documents", "reference_documents", "historical_documents")
        for entry in manifest.get(group, [])
        if Path(entry.get("repository_path", "")).name == archived_name
        and entry.get("canonical_filename") == archived_name
    ]
    for archived in candidates_on_disk:
        digest = hashlib.sha256(archived.read_bytes()).hexdigest()
        pinned = [
            entry for entry in matching
            if digest in {entry.get("sha256"), entry.get("provenance_sha256")}
        ]
        if len(pinned) == 1:
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
        raise AssertionError(
            f"historical snapshot is not archived or active at baseline: {filename}"
        )
    return candidates[0]
