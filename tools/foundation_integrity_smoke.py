#!/usr/bin/env python3
"""Fast checks for current governance and delivery routing boundaries."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_GOVERNANCE_ROUTER = Path("docs/governance/CURRENT_GOVERNANCE_ROUTER.json")
DEFAULT_DELIVERY_ROUTER = Path("docs/delivery/CURRENT_DELIVERY_ROUTER.json")
EXPECTED_GOVERNING_IDS = frozenset(
    {
        "NORTH_STAR_AND_MVP",
        "PLATFORM_PRODUCT_LAW",
        "PRODUCT_DECISIONS",
        "ARCHITECTURE_LAW",
        "DOMAIN_LAW",
        "GOVERNING_ROADMAP",
    }
)
EXPECTED_ARCHITECTURE_REFERENCES = frozenset(
    {"ARCHITECTURE_REQUIREMENTS", "ARCHITECTURE_LAW_REFERENCE", "REFERENCE_FLOW_PRESSURE_TESTS"}
)
EXPECTED_SUPPORTING_IDS = frozenset(
    {
        "PLATFORM_OPERATING_MODEL",
        "FRONTEND_EXPERIENCE_SYSTEM",
        "ENGINEERING_STANDARDS",
        "DELIVERY_GOVERNANCE_STANDARD",
    }
)
EXPECTED_DELIVERY_TYPES = frozenset(
    {"feature_contract", "jit", "proof", "execution", "content_evidence"}
)
FORBIDDEN_GOVERNANCE_KEYS = frozenset(
    {
        "delivery_contracts",
        "feature_contracts",
        "jit",
        "proof",
        "execution_authority",
        "delivery_status",
        "plane",
    }
)
FORBIDDEN_DELIVERY_KEYS = frozenset(
    {
        "governing_documents",
        "architecture_references",
        "supporting_documents",
        "authority_precedence",
        "execution_authority",
        "plane",
    }
)
DOCUMENT_VERSION_PATTERN = re.compile(
    r"^[-*]\s+\*\*Document version:\*\*\s+v?(\d+\.\d+\.\d+)\s*$", re.MULTILINE
)
STATUS_VERSION_PATTERN = re.compile(
    r"^[-*]\s+\*\*Document status:\*\*.*?\bv(\d+\.\d+\.\d+)\b", re.MULTILINE
)


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1]


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


def _relative_target(root: Path, relative: str, required_root: str) -> tuple[bool, Path]:
    route = Path(relative)
    target = root / route
    try:
        resolved = target.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError):
        return False, target
    if (
        route.is_absolute()
        or ".." in route.parts
        or not route.is_relative_to(Path(required_root))
        or "history" in route.parts
        or "archive" in route.parts
        or target.is_symlink()
        or not resolved.is_file()
    ):
        return False, resolved
    # Reject symlinked parent directories as well as symlinked final files.
    cursor = root
    for part in route.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            return False, resolved
    return True, resolved


def _declared_version(text: str) -> str | None:
    match = DOCUMENT_VERSION_PATTERN.search(text)
    if match:
        return match.group(1)
    match = STATUS_VERSION_PATTERN.search(text)
    return match.group(1) if match else None


def _check_hashed_route(
    root: Path,
    report: dict[str, Any],
    entry: dict[str, Any],
    *,
    kind: str,
    required_root: str,
) -> None:
    relative = str(entry.get("repository_path", ""))
    document_id = str(entry.get("document_id", ""))
    safe, target = _relative_target(root, relative, required_root)
    filename_ok = safe and target.name == entry.get("canonical_filename")
    expected_hash = str(entry.get("sha256", ""))
    actual_hash = hashlib.sha256(target.read_bytes()).hexdigest() if safe else None
    hash_ok = safe and len(expected_hash) == 64 and actual_hash == expected_hash
    version_ok = True
    if "semver" in entry:
        try:
            declared = _declared_version(target.read_text(encoding="utf-8")) if safe else None
        except UnicodeDecodeError:
            declared = None
        version_ok = declared == str(entry.get("semver"))
    ok = safe and filename_ok and hash_ok and version_ok
    _record(
        report,
        f"smoke_{kind}_route",
        ok,
        f"{kind} route valid for {document_id}"
        if ok
        else (
            f"invalid {kind} route for {document_id}: safe={safe}, filename={filename_ok}, "
            f"hash={hash_ok}, version={version_ok}"
        ),
        path=relative,
    )


def _load_router(root: Path, report: dict[str, Any], relative: Path, label: str) -> dict[str, Any] | None:
    path = root / relative
    try:
        router = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        _record(report, f"smoke_{label}_router_load", False, f"cannot load {label} router: {error}", path=relative.as_posix())
        return None
    _record(
        report,
        f"smoke_{label}_router_identity",
        isinstance(router, dict)
        and router.get("router_id") == f"CURRENT_{label.upper()}_ROUTER"
        and router.get("status") == "CURRENT",
        f"current {label} router identity and status valid"
        if isinstance(router, dict)
        and router.get("router_id") == f"CURRENT_{label.upper()}_ROUTER"
        and router.get("status") == "CURRENT"
        else f"{label} router must identify CURRENT_{label.upper()}_ROUTER with CURRENT status",
        path=relative.as_posix(),
    )
    return router if isinstance(router, dict) else None


def _check_router_boundary(
    report: dict[str, Any], router: dict[str, Any], *, label: str, forbidden: frozenset[str]
) -> None:
    forbidden_found = sorted(forbidden.intersection(router))
    _record(
        report,
        f"smoke_{label}_router_boundary",
        not forbidden_found,
        f"{label} router stays within its semantic boundary"
        if not forbidden_found
        else f"{label} router contains fields owned by another authority boundary: {forbidden_found}",
    )


def run_smoke_audit(
    root: Path,
    governance_router_path: Path = DEFAULT_GOVERNANCE_ROUTER,
    delivery_router_path: Path = DEFAULT_DELIVERY_ROUTER,
) -> dict[str, Any]:
    """Validate both current routers, semantic roots, entrypoint and CI topology."""

    root = Path(root).resolve()
    governance_router_path = Path(governance_router_path)
    delivery_router_path = Path(delivery_router_path)
    if not governance_router_path.is_absolute():
        governance_router_path = root / governance_router_path
    if not delivery_router_path.is_absolute():
        delivery_router_path = root / delivery_router_path

    report: dict[str, Any] = {
        "status": "PASS",
        "assertion_count": 0,
        "counts": {},
        "checks": [],
        "findings": [],
    }

    governance_relative = governance_router_path.relative_to(root) if governance_router_path.is_relative_to(root) else Path(str(governance_router_path))
    delivery_relative = delivery_router_path.relative_to(root) if delivery_router_path.is_relative_to(root) else Path(str(delivery_router_path))
    governance = _load_router(root, report, governance_relative, "governance")
    delivery = _load_router(root, report, delivery_relative, "delivery")

    if governance is not None:
        _check_router_boundary(report, governance, label="governance", forbidden=FORBIDDEN_GOVERNANCE_KEYS)
        precedence_ok = governance.get("authority_precedence") == [
            "product", "architecture", "domain", "roadmap", "supporting"
        ]
        _record(
            report,
            "smoke_governance_precedence",
            precedence_ok,
            "governance router preserves authority precedence"
            if precedence_ok
            else "governance router authority_precedence must be Product, Architecture, Domain, Roadmap, supporting",
        )

        collections = (
            ("governing_documents", EXPECTED_GOVERNING_IDS),
            ("architecture_references", EXPECTED_ARCHITECTURE_REFERENCES),
            ("supporting_documents", EXPECTED_SUPPORTING_IDS),
        )
        for collection, expected_ids in collections:
            entries = governance.get(collection, [])
            ids = {str(entry.get("document_id")) for entry in entries if isinstance(entry, dict)} if isinstance(entries, list) else set()
            valid = ids == expected_ids
            _record(
                report,
                f"smoke_governance_{collection}",
                valid,
                f"governance {collection} inventory valid"
                if valid
                else f"governance {collection} must contain exactly {sorted(expected_ids)}; got {sorted(ids)}",
            )
            for entry in entries if isinstance(entries, list) else []:
                if isinstance(entry, dict):
                    _check_hashed_route(root, report, entry, kind="governance", required_root="docs/governance")

    if delivery is not None:
        _check_router_boundary(report, delivery, label="delivery", forbidden=FORBIDDEN_DELIVERY_KEYS)
        contracts = delivery.get("delivery_contracts", [])
        contract_types = {
            str(entry.get("contract_type")) for entry in contracts if isinstance(entry, dict)
        } if isinstance(contracts, list) else set()
        types_ok = EXPECTED_DELIVERY_TYPES.issubset(contract_types)
        _record(
            report,
            "smoke_delivery_contract_types",
            types_ok,
            "delivery router covers Feature, JIT, proof, execution and content evidence"
            if types_ok
            else f"delivery router is missing contract types: {sorted(EXPECTED_DELIVERY_TYPES - contract_types)}",
        )
        ids = [str(entry.get("document_id")) for entry in contracts if isinstance(entry, dict)] if isinstance(contracts, list) else []
        unique_ids = len(ids) == len(set(ids)) and bool(ids)
        _record(
            report,
            "smoke_delivery_inventory",
            unique_ids,
            "delivery router has a non-empty unique contract inventory"
            if unique_ids
            else "delivery router contracts must be a non-empty list with unique document_id values",
        )
        for entry in contracts if isinstance(contracts, list) else []:
            if isinstance(entry, dict):
                _check_hashed_route(root, report, entry, kind="delivery", required_root="docs/delivery")

    required_paths = (
        "docs/README.md",
        "docs/governance/README.md",
        "docs/delivery/README.md",
        "docs/history/README.md",
        "docs/history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json",
        "docs/history/02_OPEN_WORK_v1.2.90.md",
        "docs/development/foundation-integrity-merge-gate.md",
    )
    for relative in required_paths:
        path = root / relative
        _record(
            report,
            "smoke_required_file",
            path.is_file() and not path.is_symlink(),
            f"required current/history entrypoint exists: {relative}"
            if path.is_file() and not path.is_symlink()
            else f"required current/history entrypoint is missing or not a regular file: {relative}",
            path=relative,
        )

    entrypoint_path = root / "docs/README.md"
    entrypoint = entrypoint_path.read_text(encoding="utf-8") if entrypoint_path.is_file() else ""
    entrypoint_tokens = ("governance/", "delivery/", "development/", "history/", "Plane")
    entrypoint_ok = all(token.lower() in entrypoint.lower() for token in entrypoint_tokens)
    _record(
        report,
        "smoke_documentation_entrypoint",
        entrypoint_ok,
        "documentation entrypoint describes the semantic roots and Plane"
        if entrypoint_ok
        else "documentation entrypoint must describe governance, delivery, development, history and Plane",
        path="docs/README.md",
    )

    workflow_path = root / ".github/workflows/foundation-integrity.yml"
    workflow = workflow_path.read_text(encoding="utf-8") if workflow_path.is_file() else ""
    smoke_match = re.search(r"(?ms)^  foundation-smoke:\n(.*?)(?=^  [a-zA-Z0-9_-]+:\n|\Z)", workflow)
    aggregate_match = re.search(r"(?m)^    needs: \[([^\]]+)\]$", workflow)
    aggregate_needs = {item.strip() for item in aggregate_match.group(1).split(",")} if aggregate_match else set()
    topology_ok = (
        smoke_match is not None
        and "if:" not in smoke_match.group(1)
        and "foundation-full:" in workflow
        and "if: needs.route.outputs.foundation_full == 'true'" in workflow
        and "application-ci:" in workflow
        and aggregate_needs == {"route", "foundation-smoke", "application-ci"}
    )
    _record(
        report,
        "smoke_merge_gate_topology",
        topology_ok,
        "Foundation Smoke is always-on; Full is separately routed; required aggregate waits on Smoke and applicable Application CI"
        if topology_ok
        else "merge-gate topology must keep Smoke always-on, route Full separately and exclude Full from the required aggregate",
        path=".github/workflows/foundation-integrity.yml",
    )

    report["counts"] = {
        "governing_documents": len(governance.get("governing_documents", [])) if governance else 0,
        "architecture_references": len(governance.get("architecture_references", [])) if governance else 0,
        "supporting_documents": len(governance.get("supporting_documents", [])) if governance else 0,
        "delivery_contracts": len(delivery.get("delivery_contracts", [])) if delivery else 0,
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
    parser.add_argument("--governance-router", type=Path, default=DEFAULT_GOVERNANCE_ROUTER)
    parser.add_argument("--delivery-router", type=Path, default=DEFAULT_DELIVERY_ROUTER)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)
    root = args.root or _default_root()
    report = run_smoke_audit(root, args.governance_router, args.delivery_router)
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        _print_human(report)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
