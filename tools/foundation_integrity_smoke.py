#!/usr/bin/env python3
"""Cheap fail-closed checks for current NewYou authority and working routes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from tools.foundation_integrity_audit import (
    DEFAULT_MANIFEST,
    VERSION_PATTERN,
    _all_entries,
    _check_current_authority_delegated_routing,
    _check_current_authority_route_resolution,
    _check_current_authority_self_versions,
    _declared_document_version,
    _default_root,
    _load_integrity_rules,
    _print_human_report,
    _record_check,
    load_manifest,
    sha256_file,
)

REQUIRED_CURRENT_AUTHORITIES = {
    "PROJECT_NORTH_STAR_AND_MVP",
    "PLATFORM_BASELINE",
    "DECISION_REGISTER",
    "ARCHITECTURE_SYNTHESIS",
    "DOMAIN_MAP",
    "ROADMAP",
    "PLATFORM_OPERATING_MODEL",
    "FRONTEND_EXPERIENCE_SYSTEM",
    "OPEN_WORK",
}


def _active_working_routes(readme: str) -> list[str]:
    marker = "## Active Working Artifacts"
    if marker not in readme:
        return []
    section = readme.split(marker, 1)[1]
    section = re.split(r"(?m)^##\s+", section, maxsplit=1)[0]
    return re.findall(r"`(working/[^`\s]+\.md)`", section)


def run_smoke_audit(root: Path, manifest_path: Path = DEFAULT_MANIFEST) -> dict[str, Any]:
    """Validate active manifest entries and current README/Open Work routing only."""

    root = Path(root).resolve()
    manifest_path = Path(manifest_path)
    if not manifest_path.is_absolute():
        manifest_path = root / manifest_path
    report: dict[str, Any] = {
        "status": "PASS",
        "assertion_count": 0,
        "counts": {},
        "checks": [],
        "findings": [],
    }

    try:
        manifest = load_manifest(manifest_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        _record_check(report, "smoke_manifest_load", False, f"cannot load manifest: {error}", path=str(manifest_path))
        report["assertion_count"] = len(report["checks"])
        report["status"] = "FAIL"
        return report

    try:
        integrity_rules = _load_integrity_rules(manifest)
    except (KeyError, ValueError, TypeError) as error:
        _record_check(report, "smoke_manifest_rules", False, f"manifest rules are invalid: {error}", path=str(manifest_path))
        report["assertion_count"] = len(report["checks"])
        report["status"] = "FAIL"
        return report
    _record_check(report, "smoke_manifest_rules", True, "manifest integrity rules parse")

    expected_ids = REQUIRED_CURRENT_AUTHORITIES
    entries = _all_entries(manifest)
    active = [entry for entry in entries if entry.get("lifecycle", "current") != "historical"]
    active_by_id: dict[str, list[dict[str, Any]]] = {}
    for entry in active:
        active_by_id.setdefault(str(entry.get("document_id", "")), []).append(entry)

    missing_ids = sorted(expected_ids - active_by_id.keys())
    duplicate_ids = sorted(document_id for document_id, matches in active_by_id.items() if len(matches) != 1)
    _record_check(
        report,
        "smoke_current_authority_inventory",
        not missing_ids and not duplicate_ids,
        "each current authority has one active manifest entry"
        if not missing_ids and not duplicate_ids
        else f"missing current authorities={missing_ids}; duplicate active IDs={duplicate_ids}",
        path=str(manifest_path),
    )

    current_entries = [
        entry
        for group in ("governing_documents", "reference_documents")
        for entry in manifest.get(group, [])
        if isinstance(entry, dict) and entry.get("lifecycle", "current") != "historical"
    ]
    for entry in current_entries:
        relative = str(entry.get("repository_path", ""))
        route = Path(relative)
        target = (root / route).resolve()
        safe = bool(relative) and not route.is_absolute() and ".." not in route.parts and target.is_relative_to(root)
        not_archived = "archive" not in route.parts
        exists = safe and target.is_file()
        expected_filename = str(entry.get("canonical_filename", ""))
        filename_matches = target.name == expected_filename
        version_match = VERSION_PATTERN.search(expected_filename)
        semver_matches = version_match is not None and version_match.group(1) == str(entry.get("semver", ""))
        actual_hash = sha256_file(target) if exists else None
        hash_matches = exists and actual_hash == entry.get("sha256")
        declared_version = _declared_document_version(target.read_text(encoding="utf-8")) if exists else None
        metadata_matches = exists and declared_version == str(entry.get("semver", ""))
        entry_ok = safe and not_archived and exists and filename_matches and semver_matches and hash_matches and metadata_matches
        _record_check(
            report,
            "smoke_current_manifest_path",
            entry_ok,
            f"current path resolves and matches its manifest route: {relative}"
            if entry_ok
            else f"invalid current path or manifest metadata for {relative!r}; archived={not not_archived}, exists={exists}, filename={filename_matches}, semver={semver_matches}, hash={hash_matches}, metadata={metadata_matches}",
            path=relative,
        )

    readme_path = root / str(integrity_rules["document_roots"]["context_index"])
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    _record_check(
        report,
        "smoke_readme_exists",
        bool(readme),
        "current routing README is present" if readme else "current routing README is missing or empty",
        path=str(readme_path.relative_to(root)) if readme_path.is_relative_to(root) else str(readme_path),
    )

    working_routes = _active_working_routes(readme)
    manifest_working_routes = [
        Path(str(route)).relative_to("docs/00_platform").as_posix()
        for route in integrity_rules["graph_rules"].get("navigation_document_paths", [])
        if Path(str(route)).is_relative_to("docs/00_platform/working")
    ]
    readme_routes_by_artifact: dict[str, list[str]] = {}
    for route in working_routes:
        match = re.match(r"^(.*)_v\d+\.\d+\.\d+\.md$", Path(route).name)
        if match:
            readme_routes_by_artifact.setdefault(match.group(1), []).append(route)
    missing_or_stale_manifest_routes = []
    for relative in manifest_working_routes:
        match = re.match(r"^(.*)_v\d+\.\d+\.\d+\.md$", Path(relative).name)
        if not match:
            missing_or_stale_manifest_routes.append(relative)
            continue
        listed = readme_routes_by_artifact.get(match.group(1), [])
        if listed != [relative]:
            missing_or_stale_manifest_routes.append(f"{relative} (README lists {listed})")
    _record_check(
        report,
        "smoke_readme_manifest_working_routes",
        not missing_or_stale_manifest_routes,
        "README and manifest agree on current working artifact routes"
        if not missing_or_stale_manifest_routes
        else f"README current working routes do not match manifest routes: {missing_or_stale_manifest_routes}",
    )

    atlas_section = ""
    if "## Delivery Atlas routing" in readme:
        atlas_section = readme.split("## Delivery Atlas routing", 1)[1]
        atlas_section = re.split(r"(?m)^##\s+", atlas_section, maxsplit=1)[0]
    atlas_links = re.findall(r"\[Delivery Atlas\]\(([^)\s]+)\)", atlas_section)
    atlas_manifest_routes = [
        Path(str(route))
        for route in integrity_rules["graph_rules"].get("navigation_document_paths", [])
        if Path(str(route)).name.startswith("DELIVERY_ATLAS_WORKING_")
    ]
    expected_atlas_links = [
        route.relative_to("docs/00_platform").as_posix()
        for route in atlas_manifest_routes
        if route.is_relative_to("docs/00_platform/working")
    ]
    atlas_targets_resolve = True
    for link in atlas_links:
        route = Path(link)
        target = (root / "docs/00_platform" / route).resolve()
        atlas_targets_resolve = atlas_targets_resolve and (
            not route.is_absolute()
            and ".." not in route.parts
            and "archive" not in route.parts
            and target.is_relative_to(root)
            and target.is_file()
        )
    atlas_route_ok = (
        len(expected_atlas_links) == 1
        and atlas_links == expected_atlas_links
        and atlas_targets_resolve
    )
    _record_check(
        report,
        "smoke_delivery_atlas_route",
        atlas_route_ok,
        "README Delivery Atlas link resolves to the manifest current route"
        if atlas_route_ok
        else f"README Delivery Atlas link does not resolve to the single current manifest route: links={atlas_links}, expected={expected_atlas_links}, targets_resolve={atlas_targets_resolve}",
        path="docs/00_platform/README.md",
    )

    working_routes_valid = bool(working_routes)
    for relative in working_routes:
        route = Path("docs/00_platform") / relative
        target = (root / route).resolve()
        valid = (
            "archive" not in route.parts
            and target.is_relative_to(root)
            and target.is_file()
        )
        working_routes_valid = working_routes_valid and valid
        _record_check(
            report,
            "smoke_current_working_path",
            valid,
            f"active working path resolves: {route.as_posix()}"
            if valid
            else f"active working route is missing, unsafe, or archived: {route.as_posix()}",
            path=route.as_posix(),
        )

    graph_rules = integrity_rules["graph_rules"]
    navigation_paths = graph_rules.get("navigation_document_paths", [])
    navigation_routes_valid = isinstance(navigation_paths, list) and bool(navigation_paths)
    for relative in navigation_paths if isinstance(navigation_paths, list) else []:
        route = Path(str(relative))
        target = (root / route).resolve()
        valid = (
            not route.is_absolute()
            and ".." not in route.parts
            and "archive" not in route.parts
            and target.is_relative_to(root)
            and target.is_file()
        )
        navigation_routes_valid = navigation_routes_valid and valid
        _record_check(
            report,
            "smoke_current_navigation_path",
            valid,
            f"current navigation path resolves: {relative}"
            if valid
            else f"current navigation path is missing, unsafe, or archived: {relative}",
            path=str(relative),
        )
    _record_check(
        report,
        "smoke_current_navigation_inventory",
        navigation_routes_valid,
        "manifest current navigation paths resolve"
        if navigation_routes_valid
        else "manifest navigation_document_paths is missing or invalid",
    )

    _check_current_authority_self_versions(root, manifest, report)
    _check_current_authority_route_resolution(root, manifest, integrity_rules, report)
    _check_current_authority_delegated_routing(root, manifest, integrity_rules, report)

    report["counts"] = {
        "current_manifest_entries": len(current_entries),
        "current_working_routes": len(working_routes),
        "current_navigation_routes": len(navigation_paths) if isinstance(navigation_paths, list) else 0,
    }
    report["assertion_count"] = len(report["checks"])
    report["status"] = "PASS" if not report["findings"] else "FAIL"
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)
    root = args.root or _default_root()
    report = run_smoke_audit(root, args.manifest)
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        _print_human_report(report)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
