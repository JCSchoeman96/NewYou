#!/usr/bin/env python3
"""Fast fail-closed checks for NewYou's current durable-authority router.

Foundation Smoke intentionally validates only live routing and execution-authority
metadata. Historical/provenance graph certification remains the responsibility of
Foundation Full and CURRENT_AUTHORITY_MANIFEST_v1.0.0.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_ROUTER = Path("docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json")
EXPECTED_GOVERNING_ORDER = (
    "PROJECT_NORTH_STAR_AND_MVP",
    "PLATFORM_BASELINE",
    "DECISION_REGISTER",
    "ARCHITECTURE_SYNTHESIS",
    "DOMAIN_MAP",
    "ROADMAP",
    "PLATFORM_OPERATING_MODEL",
    "FRONTEND_EXPERIENCE_SYSTEM",
)
REQUIRED_SUPPORTING = frozenset({"ENGINEERING_STANDARDS", "DELIVERY_GOVERNANCE_STANDARD"})


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _record(
    report: dict[str, Any],
    name: str,
    ok: bool,
    message: str,
    *,
    path: str | None = None,
) -> None:
    check: dict[str, Any] = {"name": name, "status": "PASS" if ok else "FAIL", "message": message}
    if path is not None:
        check["path"] = path
    report["checks"].append(check)
    if not ok:
        finding = {"check": name, "message": message}
        if path is not None:
            finding["path"] = path
        report["findings"].append(finding)


def _safe_regular_file(root: Path, relative: str, *, allow_legacy_open_work: bool = False) -> tuple[bool, Path]:
    route = Path(relative)
    target = (root / route).resolve()
    try:
        resolved_relative = target.relative_to(root)
    except ValueError:
        return False, target

    lexical_archive = "archive" in route.parts
    resolved_archive = "archive" in resolved_relative.parts
    if route.is_absolute() or ".." in route.parts or lexical_archive or resolved_archive:
        return False, target
    if not target.is_file():
        return False, target
    if not allow_legacy_open_work and (root / route).is_symlink():
        return False, target
    return True, target


def _check_hashed_entry(root: Path, report: dict[str, Any], entry: dict[str, Any], kind: str) -> None:
    document_id = str(entry.get("document_id", ""))
    relative = str(entry.get("repository_path", ""))
    canonical = str(entry.get("canonical_filename", ""))
    semver = str(entry.get("semver", ""))
    expected_hash = str(entry.get("sha256", ""))

    safe, target = _safe_regular_file(root, relative)
    filename_ok = safe and target.name == canonical
    version_ok = bool(semver) and f"v{semver}" in canonical
    actual_hash = _sha256_file(target) if safe else None
    hash_ok = safe and len(expected_hash) == 64 and actual_hash == expected_hash
    ok = safe and filename_ok and version_ok and hash_ok

    _record(
        report,
        f"smoke_{kind}_route",
        ok,
        f"{kind} route/hash valid for {document_id}"
        if ok
        else (
            f"invalid {kind} route/hash for {document_id}: safe={safe}, "
            f"filename={filename_ok}, semver={version_ok}, hash={hash_ok}"
        ),
        path=relative,
    )


def run_smoke_audit(root: Path, router_path: Path = DEFAULT_ROUTER) -> dict[str, Any]:
    """Validate the lean current router, README contract and semantic working routes."""

    root = Path(root).resolve()
    router_path = Path(router_path)
    if not router_path.is_absolute():
        router_path = root / router_path

    report: dict[str, Any] = {
        "status": "PASS",
        "assertion_count": 0,
        "counts": {},
        "checks": [],
        "findings": [],
    }

    try:
        router = json.loads(router_path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        _record(
            report,
            "smoke_router_load",
            False,
            f"cannot load current authority router: {error}",
            path=str(router_path),
        )
        report["assertion_count"] = len(report["checks"])
        report["status"] = "FAIL"
        return report

    _record(
        report,
        "smoke_router_identity",
        router.get("router_id") == "CURRENT_AUTHORITY_ROUTER" and router.get("status") == "CURRENT",
        "current authority router identity/status valid"
        if router.get("router_id") == "CURRENT_AUTHORITY_ROUTER" and router.get("status") == "CURRENT"
        else "current authority router must identify CURRENT_AUTHORITY_ROUTER with CURRENT status",
        path=str(router_path.relative_to(root)) if router_path.is_relative_to(root) else str(router_path),
    )

    governing = router.get("governing_documents", [])
    governing_ids = tuple(entry.get("document_id") for entry in governing if isinstance(entry, dict))
    governing_ok = governing_ids == EXPECTED_GOVERNING_ORDER and "OPEN_WORK" not in governing_ids
    _record(
        report,
        "smoke_governing_inventory",
        governing_ok,
        "governing inventory is the eight durable authorities and excludes Open Work"
        if governing_ok
        else f"governing inventory must be {EXPECTED_GOVERNING_ORDER} and must not include OPEN_WORK; got {governing_ids}",
    )
    for entry in governing if isinstance(governing, list) else []:
        if isinstance(entry, dict):
            _check_hashed_entry(root, report, entry, "governing")

    supporting = router.get("supporting_documents", [])
    supporting_ids = {
        str(entry.get("document_id")) for entry in supporting if isinstance(entry, dict)
    }
    supporting_ok = REQUIRED_SUPPORTING.issubset(supporting_ids)
    _record(
        report,
        "smoke_supporting_inventory",
        supporting_ok,
        "required Engineering and Delivery Governance supporting authority is routed"
        if supporting_ok
        else f"supporting authority must include {sorted(REQUIRED_SUPPORTING)}; got {sorted(supporting_ids)}",
    )
    for entry in supporting if isinstance(supporting, list) else []:
        if isinstance(entry, dict):
            _check_hashed_entry(root, report, entry, "supporting")

    execution = router.get("execution_authority", {})
    plane_ok = execution.get("provider") == "Plane" and execution.get("project_identifier") == "WELL"
    _record(
        report,
        "smoke_plane_execution_authority",
        plane_ok,
        "Plane WELL is the live execution authority"
        if plane_ok
        else "Plane project WELL must be the live execution authority",
    )
    ready_ok = execution.get("agent_executable_state") == "Ready"
    _record(
        report,
        "smoke_ready_execution_boundary",
        ready_ok,
        "Ready is the only agent/Symphony executable state"
        if ready_ok
        else "Ready must be the agent/Symphony executable state",
    )
    flags_ok = (
        execution.get("durable_governance_precedence") is True
        and execution.get("status_only_changes_are_plane_only") is True
    )
    _record(
        report,
        "smoke_execution_precedence",
        flags_ok,
        "durable governance precedence and Plane-only status changes are locked"
        if flags_ok
        else "execution authority must preserve durable-governance precedence and Plane-only status changes",
    )

    legacy = router.get("legacy_snapshots", [])
    open_work = next(
        (
            entry
            for entry in legacy
            if isinstance(entry, dict) and entry.get("document_id") == "OPEN_WORK_FINAL_LEGACY_SNAPSHOT"
        ),
        None,
    )
    legacy_shape_ok = bool(open_work) and (
        open_work.get("repository_path") == "docs/00_platform/02_OPEN_WORK_v1.2.90.md"
        and open_work.get("lifecycle") == "frozen_legacy"
        and open_work.get("live_execution_authority") is False
        and open_work.get("successor_required_for_status_changes") is False
    )
    legacy_hash_ok = False
    if legacy_shape_ok:
        safe, target = _safe_regular_file(root, str(open_work["repository_path"]), allow_legacy_open_work=True)
        legacy_hash_ok = safe and _sha256_file(target) == open_work.get("sha256")
    _record(
        report,
        "smoke_legacy_open_work",
        legacy_shape_ok and legacy_hash_ok,
        "legacy Open Work snapshot is frozen and hash-pinned"
        if legacy_shape_ok and legacy_hash_ok
        else "legacy Open Work snapshot must be frozen, non-authoritative, successor-free and hash-correct",
        path="docs/00_platform/02_OPEN_WORK_v1.2.90.md",
    )

    working_routes = router.get("working_semantic_routes", [])
    working_inventory_ok = isinstance(working_routes, list) and bool(working_routes)
    _record(
        report,
        "smoke_working_inventory",
        working_inventory_ok,
        "semantic working route inventory is present"
        if working_inventory_ok
        else "semantic working route inventory must be a non-empty list",
    )
    for relative in working_routes if isinstance(working_routes, list) else []:
        route = Path(str(relative))
        safe, target = _safe_regular_file(root, str(relative))
        under_working = route.is_relative_to(Path("docs/00_platform/working"))
        ok = safe and under_working
        _record(
            report,
            "smoke_working_semantic_route",
            ok,
            f"working semantic route resolves outside archive: {relative}"
            if ok
            else f"working semantic route is missing, unsafe or archived: {relative}",
            path=str(relative),
        )

    readme_path = root / "docs/00_platform/README.md"
    readme_safe, readme_target = _safe_regular_file(root, "docs/00_platform/README.md")
    readme = readme_target.read_text(encoding="utf-8") if readme_safe else ""
    readme_tokens = (
        "CURRENT_AUTHORITY_ROUTER_v1.0.0.json",
        "Plane",
        "Ready",
        "02_OPEN_WORK_v1.2.90.md",
        "frozen legacy",
    )
    readme_ok = readme_safe and all(token.lower() in readme.lower() for token in readme_tokens)
    _record(
        report,
        "smoke_readme_contract",
        readme_ok,
        "README routes current authority, Plane/Ready execution and frozen legacy Open Work"
        if readme_ok
        else "README must route CURRENT_AUTHORITY_ROUTER, Plane, Ready and frozen legacy Open Work",
        path="docs/00_platform/README.md",
    )

    historical = router.get("historical_integrity_baseline", {})
    historical_path = str(historical.get("repository_path", ""))
    historical_ok = (
        historical_path == "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        and historical.get("purpose") == "Foundation Full historical/provenance certification"
        and len(str(historical.get("git_blob_sha", ""))) == 40
        and (root / historical_path).is_file()
    )
    _record(
        report,
        "smoke_historical_integrity_baseline",
        historical_ok,
        "frozen historical manifest remains routed only as Foundation Full integrity baseline"
        if historical_ok
        else "historical integrity baseline must point to the frozen manifest for Foundation Full certification",
        path=historical_path or None,
    )

    report["counts"] = {
        "governing_documents": len(governing) if isinstance(governing, list) else 0,
        "supporting_documents": len(supporting) if isinstance(supporting, list) else 0,
        "working_semantic_routes": len(working_routes) if isinstance(working_routes, list) else 0,
    }
    report["assertion_count"] = len(report["checks"])
    report["status"] = "PASS" if not report["findings"] else "FAIL"
    return report


def _print_human(report: dict[str, Any]) -> None:
    print(f"Foundation Smoke: {report['status']} ({report['assertion_count']} assertions)")
    for finding in report["findings"]:
        location = f" [{finding.get('path')}]" if finding.get("path") else ""
        print(f"- {finding['check']}{location}: {finding['message']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--router", type=Path, default=DEFAULT_ROUTER)
    # Temporary compatibility alias for callers while WELL-66 transitions the workflow.
    parser.add_argument("--manifest", type=Path, default=None, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)
    root = args.root or _default_root()
    router = args.manifest if args.manifest is not None else args.router
    report = run_smoke_audit(root, router)
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        _print_human(report)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
