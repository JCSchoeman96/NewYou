#!/usr/bin/env python3
"""Deterministic integrity checks for the NewYou planning foundation."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from pathlib import PurePosixPath
from typing import Any, Iterable

if __package__:
    from .phase_7_delivery_gates import validate_phase_7_state
else:
    from phase_7_delivery_gates import validate_phase_7_state


DEFAULT_MANIFEST = Path("docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")

OPEN_WORK_STATE_START = "<!-- HARDEN_02_RECOVERY_STATE_START -->"
OPEN_WORK_STATE_END = "<!-- HARDEN_02_RECOVERY_STATE_END -->"
PHOENIX_APPLICATION_ROOTS = ("mix.exs", "lib", "config", "priv", "assets")
MARKED_JSON_FENCE_PATTERN = re.compile(r"```json\s*(.*?)\s*```", re.DOTALL)
CURRENT_AUTHORITY_TABLE_START = "<!-- CURRENT_AUTHORITY_TABLE_START -->"
CURRENT_AUTHORITY_TABLE_END = "<!-- CURRENT_AUTHORITY_TABLE_END -->"
ACTIVE_STATE_MIRROR_START = "<!-- ACTIVE_STATE_MIRROR_START -->"
ACTIVE_STATE_MIRROR_END = "<!-- ACTIVE_STATE_MIRROR_END -->"
ACTIVE_STATE_MIRROR_FIELDS = (
    "current_stage",
    "next_stage",
    "phase_7c",
    "proof_classification",
    "application_implementation",
)
ALLOWED_LIFECYCLE_VALUES = frozenset({"current", "historical"})
ALLOWED_CONTEXT_MODES = frozenset({"default", "conditional"})
SINGULAR_CURRENT_AUTHORITY_CLASSES = frozenset(
    {
        "PRODUCT_NORTH_STAR",
        "PLATFORM_PRODUCT_LAW",
        "DECISION_REGISTER",
        "PLANNING_TRACKER",
        "ARCHITECTURE_SYNTHESIS",
        "DOMAIN_LAW",
        "ROADMAP",
        "PLATFORM_OPERATING_MODEL",
        "FRONTEND_EXPERIENCE_SYSTEM",
    }
)
CONDITIONAL_CURRENT_AUTHORITY_CLASSES = frozenset({"FRONTEND_EXPERIENCE_SYSTEM"})
CURRENT_AUTHORITY_TABLE_COLUMNS = (
    "Document ID",
    "Authority class",
    "Context mode",
    "Canonical filename",
    "Repository path",
    "SemVer",
)

ID_PATTERNS = {
    "DEC": re.compile(r"\bDEC-\d{3}\b"),
    "OQ": re.compile(r"\bOQ-\d{3}\b"),
    "ARC": re.compile(r"\bARC-\d{3}\b"),
    "ARQ": re.compile(r"\bARQ-[A-Z]+-\d{3}\b"),
    "FLOW": re.compile(r"\bFLOW-\d{2}\b"),
    "FP": re.compile(r"\bFP-\d{3}\b"),
}

DEFINITION_PATTERNS = {
    "DEC": re.compile(r"^## (DEC-\d{3})\b"),
    "OQ": re.compile(r"^## (OQ-\d{3})\b"),
    "ARC": re.compile(r"^## (ARC-\d{3})\b"),
    "ARQ": re.compile(r"^#{1,6} (ARQ-[A-Z]+-\d{3})\b"),
    "FLOW": re.compile(r"^# \d+\. (FLOW-\d{2})\b"),
    "FP": re.compile(r"^## (FP-\d{3})\b"),
}

VERSION_PATTERN = re.compile(r"_v(\d+\.\d+\.\d+)\.md$")
DOCUMENT_VERSION_PATTERN = re.compile(
    r"^-\s+\*\*Document version:\*\*\s+v?(\d+\.\d+\.\d+)\s*$", re.MULTILINE
)
STATUS_VERSION_PATTERN = re.compile(
    r"^-\s+\*\*Document status:\*\*.*?\bv(\d+\.\d+\.\d+)\b", re.MULTILINE
)
BOLD_PATTERN = re.compile(r"\*\*([^*]+)\*\*")

REQUIRED_ENTRY_FIELDS = {
    "document_id",
    "canonical_filename",
    "semver",
    "repository_path",
    "authority_class",
    "sha256",
    "superseded_version",
    "lifecycle",
}
REQUIRED_ENTRY_TEXT_FIELDS = REQUIRED_ENTRY_FIELDS - {"superseded_version"}

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("manifest root must be a JSON object")
    return value


def _reject_duplicate_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def _parse_marked_open_work_state(text: str) -> dict[str, Any]:
    if text.count(OPEN_WORK_STATE_START) != 1 or text.count(OPEN_WORK_STATE_END) != 1:
        raise ValueError("Open Work must contain exactly one marked JSON state")

    start = text.index(OPEN_WORK_STATE_START) + len(OPEN_WORK_STATE_START)
    end = text.index(OPEN_WORK_STATE_END, start)
    if end < start:
        raise ValueError("Open Work JSON state markers are out of order")
    region = text[start:end]
    matches = list(MARKED_JSON_FENCE_PATTERN.finditer(region))
    if len(matches) != 1:
        raise ValueError("Open Work marked state must contain exactly one JSON fence")
    match = matches[0]
    if region[: match.start()].strip() or region[match.end() :].strip():
        raise ValueError("Open Work marked state contains content outside its JSON fence")

    try:
        value = json.loads(
            match.group(1),
            object_pairs_hook=_reject_duplicate_json_keys,
            parse_constant=lambda constant: (_ for _ in ()).throw(
                ValueError(f"invalid JSON constant: {constant}")
            ),
        )
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot parse Open Work marked JSON state: {error}") from error
    if not isinstance(value, dict):
        raise ValueError("Open Work marked JSON state must be an object")
    return value


def _parse_marked_active_state_mirror(text: str) -> dict[str, Any]:
    if text.count(ACTIVE_STATE_MIRROR_START) != 1 or text.count(ACTIVE_STATE_MIRROR_END) != 1:
        raise ValueError("README must contain exactly one marked active-state mirror")

    start = text.index(ACTIVE_STATE_MIRROR_START) + len(ACTIVE_STATE_MIRROR_START)
    end = text.index(ACTIVE_STATE_MIRROR_END, start)
    if end < start:
        raise ValueError("README active-state mirror markers are out of order")
    region = text[start:end]
    matches = list(MARKED_JSON_FENCE_PATTERN.finditer(region))
    if len(matches) != 1:
        raise ValueError("README active-state mirror must contain exactly one JSON fence")
    match = matches[0]
    if region[: match.start()].strip() or region[match.end() :].strip():
        raise ValueError("README active-state mirror contains content outside its JSON fence")

    try:
        value = json.loads(
            match.group(1),
            object_pairs_hook=_reject_duplicate_json_keys,
            parse_constant=lambda constant: (_ for _ in ()).throw(
                ValueError(f"invalid JSON constant: {constant}")
            ),
        )
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot parse README active-state mirror: {error}") from error
    if not isinstance(value, dict):
        raise ValueError("README active-state mirror must be a JSON object")
    if set(value) != set(ACTIVE_STATE_MIRROR_FIELDS):
        missing = sorted(set(ACTIVE_STATE_MIRROR_FIELDS) - set(value))
        extra = sorted(set(value) - set(ACTIVE_STATE_MIRROR_FIELDS))
        raise ValueError(f"README active-state mirror fields differ; missing={missing}, extra={extra}")
    if any(not isinstance(value[field], str) for field in ACTIVE_STATE_MIRROR_FIELDS):
        raise ValueError("README active-state mirror values must all be strings")
    return value


def _all_entries(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for key in ("governing_documents", "reference_documents", "historical_documents"):
        entries.extend(_entries_for_array(manifest, key))
    return entries


def _entries_for_array(manifest: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = manifest.get(key, [])
    if not isinstance(value, list):
        return []
    return [entry for entry in value if isinstance(entry, dict)]


def _load_integrity_rules(manifest: dict[str, Any]) -> dict[str, Any]:
    rules = manifest.get("integrity_rules")
    if not isinstance(rules, dict):
        raise ValueError("manifest integrity_rules must be an object")

    expected_counts = rules.get("expected_counts")
    required_count_keys = {
        "decisions",
        "open_questions",
        "architecture_law",
        "architecture_requirements",
        "reference_flows",
        "domains",
        "ownership_rows",
        "feature_packs",
    }
    if not isinstance(expected_counts, dict) or not required_count_keys <= expected_counts.keys():
        raise ValueError("manifest integrity_rules.expected_counts is incomplete")
    if any(not isinstance(expected_counts[key], int) or expected_counts[key] < 0 for key in required_count_keys):
        raise ValueError("manifest expected counts must be non-negative integers")

    contiguous_ranges = rules.get("contiguous_ranges")
    required_range_families = {"DEC", "OQ", "ARC", "FLOW"}
    if not isinstance(contiguous_ranges, dict) or not required_range_families <= contiguous_ranges.keys():
        raise ValueError("manifest integrity_rules.contiguous_ranges is incomplete")
    if expected_counts["feature_packs"]:
        if "FP" not in contiguous_ranges:
            raise ValueError("manifest integrity_rules.contiguous_ranges must define FP")
    for family, range_rule in contiguous_ranges.items():
        if not isinstance(range_rule, dict):
            raise ValueError(f"manifest contiguous range for {family} must be an object")
        if not {"prefix", "start", "end", "width"} <= range_rule.keys():
            raise ValueError(f"manifest contiguous range for {family} is incomplete")
        if (
            not isinstance(range_rule["prefix"], str)
            or not isinstance(range_rule["start"], int)
            or not isinstance(range_rule["end"], int)
            or not isinstance(range_rule["width"], int)
            or range_rule["start"] < 1
            or range_rule["end"] < range_rule["start"] - 1
            or range_rule["width"] < 1
        ):
            raise ValueError(f"manifest contiguous range for {family} is invalid")

    document_roots = rules.get("document_roots")
    required_roots = {"governing", "reference", "historical", "context_index"}
    if not isinstance(document_roots, dict) or not required_roots <= document_roots.keys():
        raise ValueError("manifest integrity_rules.document_roots is incomplete")
    if any(not isinstance(document_roots[key], str) or not document_roots[key] for key in required_roots):
        raise ValueError("manifest document roots must be non-empty strings")

    definition_sources = rules.get("definition_sources")
    required_sources = {
        "decisions",
        "architecture_law",
        "architecture_requirements",
        "reference_flows",
        "roadmap",
        "domain_map",
    }
    if not isinstance(definition_sources, dict) or not required_sources <= definition_sources.keys():
        raise ValueError("manifest integrity_rules.definition_sources is incomplete")
    if any(not isinstance(definition_sources[key], str) or not definition_sources[key] for key in required_sources):
        raise ValueError("manifest definition sources must be non-empty strings")

    graph_rules = rules.get("graph_rules")
    if not isinstance(graph_rules, dict):
        raise ValueError("manifest integrity_rules.graph_rules must be an object")
    stale_patterns = graph_rules.get("stale_reference_patterns")
    if not isinstance(stale_patterns, list) or any(not isinstance(pattern, str) for pattern in stale_patterns):
        raise ValueError("manifest graph stale_reference_patterns must be a string list")
    try:
        for pattern in stale_patterns:
            re.compile(pattern)
    except re.error as error:
        raise ValueError(f"manifest graph stale_reference_patterns contains invalid regex: {error}") from error
    if not isinstance(graph_rules.get("reference_header_lines"), int) or graph_rules["reference_header_lines"] < 1:
        raise ValueError("manifest graph reference_header_lines must be a positive integer")
    if not isinstance(graph_rules.get("frozen_provenance_policy"), str):
        raise ValueError("manifest graph frozen_provenance_policy must be a string")
    navigation_document_ids = graph_rules.get("navigation_document_ids")
    if not isinstance(navigation_document_ids, list) or any(
        not isinstance(document_id, str) or not document_id for document_id in navigation_document_ids
    ):
        raise ValueError("manifest graph navigation_document_ids must be a string list")

    return rules


def _relative_path(entry: dict[str, Any]) -> str:
    value = entry.get("repository_path", "")
    return value if isinstance(value, str) else ""


def _safe_repository_path(root: Path, relative: str) -> Path | None:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        return None
    try:
        path = PurePosixPath(relative)
        if path.is_absolute() or path.as_posix() != relative or any(part in {".", ".."} for part in path.parts):
            return None
        resolved_root = root.resolve()
        resolved_path = root.joinpath(*path.parts).resolve(strict=False)
        resolved_path.relative_to(resolved_root)
    except (OSError, RuntimeError, ValueError):
        return None
    return resolved_path


def _entry_path(root: Path, entry: dict[str, Any]) -> Path:
    safe_path = _safe_repository_path(root, _relative_path(entry))
    return safe_path if safe_path is not None else root / "__invalid_manifest_path__"


def _find_entry(entries: Iterable[dict[str, Any]], authority_class: str) -> dict[str, Any] | None:
    for entry in entries:
        if entry.get("authority_class") == authority_class and entry.get("lifecycle") == "current":
            return entry
    return None


def _read_entry_text(root: Path, entry: dict[str, Any] | None) -> str:
    if entry is None:
        return ""
    path = _entry_path(root, entry)
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _declared_document_version(text: str) -> str | None:
    metadata = "\n".join(text.splitlines()[:40])
    explicit_versions = DOCUMENT_VERSION_PATTERN.findall(metadata)
    if explicit_versions:
        return explicit_versions[0] if len(explicit_versions) == 1 else None
    status_versions = STATUS_VERSION_PATTERN.findall(metadata)
    return status_versions[0] if len(status_versions) == 1 else None


def _record_check(
    report: dict[str, Any],
    name: str,
    passed: bool,
    message: str,
    *,
    path: str = "",
) -> None:
    report["checks"].append(
        {
            "name": name,
            "status": "PASS" if passed else "FAIL",
            "message": message,
        }
    )
    if not passed:
        report["findings"].append(
            {
                "check": name,
                "path": path,
                "message": message,
            }
        )


def _definition_locations(
    text: str,
    pattern: re.Pattern[str],
    path: str,
) -> dict[str, list[str]]:
    locations: dict[str, list[str]] = {}
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = pattern.match(line)
        if match:
            locations.setdefault(match.group(1), []).append(f"{path}:{line_number}")
    return locations


def _merge_locations(*groups: dict[str, list[str]]) -> dict[str, list[str]]:
    merged: dict[str, list[str]] = {}
    for group in groups:
        for identifier, locations in group.items():
            merged.setdefault(identifier, []).extend(locations)
    return merged


def _extract_references(text: str) -> dict[str, set[str]]:
    return {
        family: set(pattern.findall(text))
        for family, pattern in ID_PATTERNS.items()
    }


def _table_rows(text: str, start_marker: str, end_marker: str) -> list[list[str]]:
    start = text.find(start_marker)
    if start == -1:
        return []
    end = text.find(end_marker, start + len(start_marker))
    section = text[start:] if end == -1 else text[start:end]
    rows: list[list[str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or stripped.count("|") < 3:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        rows.append(cells)
    return rows


def _expected_contiguous(range_rule: dict[str, Any]) -> set[str]:
    prefix = str(range_rule["prefix"])
    start = int(range_rule["start"])
    end = int(range_rule["end"])
    width = int(range_rule["width"])
    return {f"{prefix}-{number:0{width}d}" for number in range(start, end + 1)}


def _production_mode(expected_counts: dict[str, int] | None) -> bool:
    return expected_counts is None


def _check_manifest_shape(root: Path, manifest: dict[str, Any], report: dict[str, Any]) -> list[dict[str, Any]]:
    entries = _all_entries(manifest)
    arrays_ok = all(
        isinstance(manifest.get(key), list)
        for key in ("governing_documents", "reference_documents", "historical_documents")
    )
    schema_issues: list[str] = []
    if not arrays_ok:
        schema_issues.append("manifest must contain governing, reference, and historical document arrays")
    if not entries:
        schema_issues.append("manifest document arrays must contain entries")
    for array_name in ("governing_documents", "reference_documents", "historical_documents"):
        array = manifest.get(array_name, [])
        if isinstance(array, list):
            for index, entry in enumerate(array):
                if not isinstance(entry, dict):
                    schema_issues.append(f"{array_name}[{index}] must be an object")

    seen_ids: dict[str, int] = {}
    seen_paths: dict[str, int] = {}
    for entry in entries:
        for field in sorted(REQUIRED_ENTRY_FIELDS):
            if field not in entry:
                schema_issues.append(f"{_relative_path(entry)}: missing manifest field {field}")
            elif field in REQUIRED_ENTRY_TEXT_FIELDS and (
                not isinstance(entry[field], str) or not entry[field]
            ):
                schema_issues.append(f"{_relative_path(entry)}: manifest field {field} must be a non-empty string")
            elif field == "superseded_version" and entry[field] is not None and not isinstance(entry[field], str):
                schema_issues.append(f"{_relative_path(entry)}: manifest field superseded_version must be a string or null")
        if "provenance_sha256" in entry and entry["provenance_sha256"] is not None and not isinstance(
            entry["provenance_sha256"], str
        ):
            schema_issues.append(f"{_relative_path(entry)}: manifest field provenance_sha256 must be a string or null")
        document_id = str(entry.get("document_id", ""))
        repository_path = _relative_path(entry)
        seen_ids[document_id] = seen_ids.get(document_id, 0) + 1
        seen_paths[repository_path] = seen_paths.get(repository_path, 0) + 1

    _record_check(
        report,
        "manifest_schema",
        not schema_issues,
        "manifest contains valid document arrays and all required entry fields"
        if not schema_issues
        else "; ".join(schema_issues),
    )

    duplicate_ids = sorted(identifier for identifier, count in seen_ids.items() if count > 1)
    duplicate_paths = sorted(path for path, count in seen_paths.items() if count > 1)
    _record_check(
        report,
        "manifest_unique_document_ids",
        not duplicate_ids,
        "document IDs are unique" if not duplicate_ids else f"duplicate document IDs: {duplicate_ids}",
    )
    _record_check(
        report,
        "manifest_unique_repository_paths",
        not duplicate_paths,
        "repository paths are unique" if not duplicate_paths else f"duplicate repository paths: {duplicate_paths}",
    )
    return entries


def _parse_current_authority_table(readme_text: str) -> list[dict[str, str]]:
    heading_pattern = re.compile(r"^## Current Authority\s*$", re.MULTILINE)
    headings = list(heading_pattern.finditer(readme_text))
    if len(headings) != 1:
        raise ValueError("README must contain exactly one ## Current Authority section")
    section_start = headings[0].end()
    next_heading = re.search(r"^##\s+", readme_text[section_start:], re.MULTILINE)
    section_end = section_start + next_heading.start() if next_heading else len(readme_text)
    section = readme_text[section_start:section_end]
    if section.count(CURRENT_AUTHORITY_TABLE_START) != 1 or section.count(CURRENT_AUTHORITY_TABLE_END) != 1:
        raise ValueError("Current Authority must contain exactly one marked route table")
    start = section.index(CURRENT_AUTHORITY_TABLE_START) + len(CURRENT_AUTHORITY_TABLE_START)
    end = section.index(CURRENT_AUTHORITY_TABLE_END, start)
    if end < start:
        raise ValueError("Current Authority route table markers are out of order")

    content = section[start:end]
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    if len(lines) < 2 or any(not line.startswith("|") for line in lines):
        raise ValueError("Current Authority route table must contain only Markdown table rows")

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip("|").split("|")]

    if tuple(cells(lines[0])) != CURRENT_AUTHORITY_TABLE_COLUMNS:
        raise ValueError("Current Authority route table has an unexpected header")
    if len(cells(lines[1])) != len(CURRENT_AUTHORITY_TABLE_COLUMNS) or any(
        not re.fullmatch(r":?-{3,}:?", cell) for cell in cells(lines[1])
    ):
        raise ValueError("Current Authority route table has an invalid separator row")

    routes: list[dict[str, str]] = []
    for line in lines[2:]:
        values = cells(line)
        if len(values) != len(CURRENT_AUTHORITY_TABLE_COLUMNS) or any(not value for value in values):
            raise ValueError("Current Authority route rows must contain six non-empty columns")
        routes.append(dict(zip(CURRENT_AUTHORITY_TABLE_COLUMNS, values, strict=True)))
    return routes


def _check_manifest_lifecycle_and_paths(
    root: Path,
    manifest: dict[str, Any],
    entries: list[dict[str, Any]],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    lifecycle_issues: list[str] = []
    path_issues: list[str] = []
    class_issues: list[str] = []
    roots = integrity_rules["document_roots"]
    expected_by_array = {
        "governing_documents": "current",
        "reference_documents": "current",
        "historical_documents": "historical",
    }

    for array_name, expected_lifecycle in expected_by_array.items():
        array = manifest.get(array_name, [])
        if not isinstance(array, list):
            lifecycle_issues.append(f"{array_name} is not an array")
            continue
        for entry in array:
            if not isinstance(entry, dict):
                lifecycle_issues.append(f"{array_name} contains a non-object entry")
                continue
            relative = _relative_path(entry)
            lifecycle = entry.get("lifecycle")
            if not isinstance(lifecycle, str) or lifecycle not in ALLOWED_LIFECYCLE_VALUES:
                lifecycle_issues.append(f"{relative}: invalid lifecycle {lifecycle!r}")
            elif lifecycle != expected_lifecycle:
                lifecycle_issues.append(
                    f"{relative}: {array_name} requires lifecycle {expected_lifecycle!r}, got {lifecycle!r}"
                )

    category_by_identity: dict[int, str] = {}
    for category, array_name in (
        ("governing", "governing_documents"),
        ("reference", "reference_documents"),
        ("historical", "historical_documents"),
    ):
        category_by_identity.update(
            {id(entry): category for entry in _entries_for_array(manifest, array_name)}
        )
    for entry in entries:
        relative = _relative_path(entry)
        safe_path = _safe_repository_path(root, relative)
        if safe_path is None:
            path_issues.append(f"{relative!r} is not a normalized in-repository relative path")
            continue

        category = category_by_identity.get(id(entry), "governing")
        declared_root = roots[category]
        normalized_root = PurePosixPath(declared_root)
        normalized_path = PurePosixPath(relative)
        if normalized_root.is_absolute() or normalized_root.as_posix() != declared_root or any(
            part in {".", ".."} for part in normalized_root.parts
        ):
            class_issues.append(f"declared {category} root {declared_root!r} is not normalized")
            continue
        if normalized_path != normalized_root and normalized_root not in normalized_path.parents:
            class_issues.append(f"{relative}: path is outside declared {category} root {declared_root}")
            continue

        if category == "governing":
            forbidden_segments = {"archive", "working", "reference"}
            if forbidden_segments.intersection(normalized_path.parts[len(normalized_root.parts) :]):
                class_issues.append(f"{relative}: current governing authority is under a non-current directory")
        if category == "reference" and normalized_path == normalized_root:
            class_issues.append(f"{relative}: reference entry must identify a file beneath the reference root")
        if category == "historical" and normalized_path == normalized_root:
            class_issues.append(f"{relative}: historical entry must identify a file beneath the archive root")

        declared = _safe_repository_path(root, declared_root)
        if declared is None:
            class_issues.append(f"declared {category} root {declared_root!r} is invalid")
        else:
            try:
                safe_path.relative_to(declared)
            except ValueError:
                class_issues.append(f"{relative}: resolved path escapes declared {category} root {declared_root}")

    _record_check(
        report,
        "manifest_lifecycle",
        not lifecycle_issues,
        "manifest lifecycle values agree with array placement"
        if not lifecycle_issues
        else "; ".join(lifecycle_issues),
    )
    _record_check(
        report,
        "manifest_path_normalization",
        not path_issues,
        "manifest paths are normalized repository-relative paths"
        if not path_issues
        else "; ".join(path_issues),
    )
    _record_check(
        report,
        "manifest_path_classification",
        not class_issues,
        "manifest paths match their declared document classes"
        if not class_issues
        else "; ".join(class_issues),
    )


def _check_current_authority_roles(
    governing_entries: list[dict[str, Any]],
    reference_entries: list[dict[str, Any]],
    report: dict[str, Any],
) -> None:
    counts = Counter(
        str(entry.get("authority_class", ""))
        for entry in governing_entries
        if entry.get("lifecycle") == "current"
    )
    missing_or_duplicate = {
        authority_class: counts.get(authority_class, 0)
        for authority_class in SINGULAR_CURRENT_AUTHORITY_CLASSES
        if counts.get(authority_class, 0) != 1
    }
    unexpected = sorted(set(counts) - SINGULAR_CURRENT_AUTHORITY_CLASSES)
    conflicting_references = sorted(
        f"{entry.get('document_id')}: {entry.get('authority_class')}"
        for entry in reference_entries
        if entry.get("lifecycle") == "current"
        and isinstance(entry.get("authority_class"), str)
        and entry.get("authority_class") in SINGULAR_CURRENT_AUTHORITY_CLASSES
    )
    passed = not missing_or_duplicate and not unexpected and not conflicting_references
    _record_check(
        report,
        "current_authority_role_uniqueness",
        passed,
        "each singular current authority role has exactly one governing artifact and no reference claims it"
        if passed
        else (
            f"missing or duplicate current roles={missing_or_duplicate}, "
            f"unexpected roles={unexpected}, current references claiming singular roles={conflicting_references}"
        ),
    )


def _check_readme_manifest_current_authority_parity(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    context_index = integrity_rules["document_roots"]["context_index"]
    readme_path = _safe_repository_path(root, context_index)
    try:
        if readme_path is None or not readme_path.is_file():
            raise ValueError(f"README route document is missing at {context_index!r}")
        routes = _parse_current_authority_table(readme_path.read_text(encoding="utf-8"))
        governing = _entries_for_array(manifest, "governing_documents")
        expected_routes: list[dict[str, str]] = []
        context_issues: list[str] = []
        for entry in governing:
            context_mode = entry.get("context_mode")
            authority_class = entry.get("authority_class")
            expected_mode = (
                "conditional"
                if isinstance(authority_class, str)
                and authority_class in CONDITIONAL_CURRENT_AUTHORITY_CLASSES
                else "default"
            )
            if not isinstance(context_mode, str) or context_mode not in ALLOWED_CONTEXT_MODES or context_mode != expected_mode:
                context_issues.append(
                    f"{entry.get('document_id')}: expected context_mode {expected_mode!r}, got {context_mode!r}"
                )
            expected_routes.append(
                {
                    "Document ID": str(entry.get("document_id", "")),
                    "Authority class": str(authority_class or ""),
                    "Context mode": str(context_mode or ""),
                    "Canonical filename": str(entry.get("canonical_filename", "")),
                    "Repository path": _relative_path(entry),
                    "SemVer": str(entry.get("semver", "")),
                }
            )

        route_ids = [route["Document ID"] for route in routes]
        duplicate_ids = sorted(identifier for identifier, count in Counter(route_ids).items() if count > 1)
        if duplicate_ids:
            raise ValueError(f"Current Authority table repeats document IDs {duplicate_ids}")
        parity = routes == expected_routes
        passed = parity and not context_issues
        message = (
            "README Current Authority table exactly matches current governing manifest entries"
            if passed
            else f"README Current Authority table differs from manifest; expected={expected_routes}, actual={routes}, context issues={context_issues}"
        )
    except (OSError, UnicodeError, ValueError) as error:
        passed = False
        message = f"cannot verify README Current Authority table: {error}"
    _record_check(
        report,
        "readme_manifest_current_authority_parity",
        passed,
        message,
        path=context_index,
    )


def _check_readme_active_state_mirror(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    context_index = integrity_rules["document_roots"]["context_index"]
    readme_path = _safe_repository_path(root, context_index)
    try:
        if readme_path is None or not readme_path.is_file():
            raise ValueError(f"README route document is missing at {context_index!r}")
        readme_text = readme_path.read_text(encoding="utf-8")
        mirror = _parse_marked_active_state_mirror(readme_text)

        open_work_entries = [
            entry
            for entry in _entries_for_array(manifest, "governing_documents")
            if entry.get("document_id") == "OPEN_WORK" and entry.get("lifecycle") == "current"
        ]
        if len(open_work_entries) != 1:
            raise ValueError(f"manifest must contain one current Open Work route, found {len(open_work_entries)}")
        open_work_path = _entry_path(root, open_work_entries[0])
        if not open_work_path.is_file():
            raise ValueError(f"current Open Work document is missing at {_relative_path(open_work_entries[0])!r}")
        canonical_state = _parse_marked_open_work_state(open_work_path.read_text(encoding="utf-8"))
        missing = [field for field in ACTIVE_STATE_MIRROR_FIELDS if field not in canonical_state]
        invalid = [
            field
            for field in ACTIVE_STATE_MIRROR_FIELDS
            if field in canonical_state and not isinstance(canonical_state[field], str)
        ]
        if missing or invalid:
            raise ValueError(f"Open Work active-state fields are incomplete; missing={missing}, non-string={invalid}")
        expected = {field: canonical_state[field] for field in ACTIVE_STATE_MIRROR_FIELDS}
        passed = mirror == expected
        message = (
            "README active-state mirror matches the current Open Work JSON"
            if passed
            else f"README active-state mirror differs from current Open Work JSON; expected={expected}, actual={mirror}"
        )
    except (OSError, UnicodeError, ValueError) as error:
        passed = False
        message = f"cannot verify README active-state mirror: {error}"
    _record_check(
        report,
        "readme_active_state_mirror",
        passed,
        message,
        path=context_index,
    )


def _check_manifest_predecessors(
    manifest: dict[str, Any],
    report: dict[str, Any],
) -> None:
    historical = _entries_for_array(manifest, "historical_documents")
    historical_by_name: dict[str, list[dict[str, Any]]] = {}
    for entry in historical:
        historical_by_name.setdefault(str(entry.get("canonical_filename", "")), []).append(entry)

    issues: list[str] = []
    current_entries = [
        entry
        for key in ("governing_documents", "reference_documents")
        for entry in _entries_for_array(manifest, key)
        if entry.get("lifecycle") == "current"
    ]
    historical_names = {
        str(entry.get("canonical_filename", ""))
        for entry in historical
        if entry.get("canonical_filename")
    }
    for entry in current_entries:
        filename = entry.get("canonical_filename")
        if isinstance(filename, str) and filename in historical_names:
            issues.append(f"{entry.get('document_id')}: current filename {filename} is also registered as historical")
    for entry in current_entries:
        predecessor_version = entry.get("superseded_version")
        if predecessor_version is None:
            continue
        current_version = str(entry.get("semver", ""))
        if not isinstance(predecessor_version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", predecessor_version):
            issues.append(f"{entry.get('document_id')}: invalid superseded_version {predecessor_version!r}")
            continue
        if predecessor_version == current_version:
            issues.append(f"{entry.get('document_id')}: artifact cannot supersede itself")
            continue
        current_parts = tuple(int(part) for part in current_version.split(".")) if re.fullmatch(
            r"\d+\.\d+\.\d+", current_version
        ) else ()
        predecessor_parts = tuple(int(part) for part in predecessor_version.split("."))
        if not current_parts or predecessor_parts >= current_parts:
            issues.append(f"{entry.get('document_id')}: predecessor version is not older than current version")
            continue
        filename = str(entry.get("canonical_filename", ""))
        match = VERSION_PATTERN.search(filename)
        if match is None:
            issues.append(f"{entry.get('document_id')}: predecessor cannot be derived from unversioned filename")
            continue
        expected_name = f"{filename[:match.start()]}_v{predecessor_version}.md"
        predecessors = historical_by_name.get(expected_name, [])
        if len(predecessors) != 1 or predecessors[0].get("lifecycle") != "historical":
            issues.append(
                f"{entry.get('document_id')}: predecessor {expected_name} must exist exactly once as historical"
            )
        if any(
            current.get("canonical_filename") == expected_name
            for key in ("governing_documents", "reference_documents")
            for current in _entries_for_array(manifest, key)
        ):
            issues.append(f"{entry.get('document_id')}: predecessor {expected_name} is also current")

    _record_check(
        report,
        "manifest_predecessor_consistency",
        not issues,
        "declared current predecessors are registered as historical artifacts"
        if not issues
        else "; ".join(issues),
    )


def _check_manifest_entries(root: Path, entries: list[dict[str, Any]], report: dict[str, Any]) -> None:
    for entry in entries:
        path = _entry_path(root, entry)
        repository_path = _relative_path(entry)
        canonical_filename = str(entry.get("canonical_filename", ""))
        exists = path.is_file()
        _record_check(
            report,
            "manifest_path_exists",
            exists,
            f"{repository_path} exists" if exists else f"missing manifest path {repository_path}",
            path=repository_path,
        )
        filename_matches = path.name == canonical_filename
        _record_check(
            report,
            "manifest_canonical_filename",
            filename_matches,
            f"canonical filename matches {repository_path}"
            if filename_matches
            else f"canonical filename {canonical_filename!r} does not match {repository_path!r}",
            path=repository_path,
        )
        actual_hash = sha256_file(path) if exists else None
        if actual_hash is not None:
            hash_matches = actual_hash == entry.get("sha256")
            _record_check(
                report,
                "manifest_hash_parity",
                hash_matches,
                f"SHA-256 matches for {repository_path}"
                if hash_matches
                else f"SHA-256 mismatch for {repository_path}: expected {entry.get('sha256')}, actual {actual_hash}",
                path=repository_path,
            )
        provenance_hash = entry.get("provenance_sha256")
        if provenance_hash is not None:
            provenance_matches = actual_hash is not None and actual_hash == provenance_hash
            _record_check(
                report,
                "frozen_provenance_hash",
                provenance_matches,
                f"frozen provenance SHA-256 matches for {repository_path}"
                if provenance_matches
                else f"frozen provenance SHA-256 mismatch for {repository_path}: expected {provenance_hash}, actual {actual_hash}",
                path=repository_path,
            )
        version_match = VERSION_PATTERN.search(canonical_filename)
        semver_matches = version_match is not None and version_match.group(1) == str(entry.get("semver", ""))
        _record_check(
            report,
            "manifest_version_parity",
            semver_matches,
            f"SemVer matches for {repository_path}"
            if semver_matches
            else f"SemVer {entry.get('semver')!r} does not match versioned filename {canonical_filename!r}",
            path=repository_path,
        )
        is_historical = entry.get("lifecycle") == "historical"
        declared_version = _declared_document_version(path.read_text(encoding="utf-8")) if exists else None
        document_version_matches = (
            exists
            if is_historical
            else exists and declared_version == str(entry.get("semver", ""))
        )
        _record_check(
            report,
            "document_version_parity",
            document_version_matches,
            f"historical artifact is preserved for {repository_path}"
            if is_historical and document_version_matches
            else f"document metadata version matches for {repository_path}"
            if document_version_matches
            else f"document metadata version {declared_version!r} does not match manifest SemVer {entry.get('semver')!r}",
            path=repository_path,
        )


def _build_definitions(
    root: Path,
    entries: list[dict[str, Any]],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> dict[str, dict[str, list[str]]]:
    definitions: dict[str, dict[str, list[str]]] = {family: {} for family in ID_PATTERNS}
    source_authority_classes = integrity_rules["definition_sources"]
    source_entries: dict[str, dict[str, Any] | None] = {
        key: _find_entry(entries, authority_class)
        for key, authority_class in source_authority_classes.items()
    }
    source_families = {
        "decisions": ("DEC", "OQ"),
        "architecture_law": ("ARC",),
        "architecture_requirements": ("ARQ",),
        "reference_flows": ("FLOW",),
        "roadmap": ("FP",),
    }
    for source_name, families in source_families.items():
        entry = source_entries.get(source_name)
        source_path = _relative_path(entry) if entry else ""
        source_text = _read_entry_text(root, entry)
        for family in families:
            locations = _definition_locations(source_text, DEFINITION_PATTERNS[family], source_path)
            definitions[family] = _merge_locations(definitions[family], locations)
            _record_check(
                report,
                f"definition_source_{family.lower()}",
                entry is not None and bool(source_text),
                f"source document for {family} definitions is present"
                if entry is not None and bool(source_text)
                else f"source document for {family} definitions is missing",
                path=source_path,
            )
    return definitions


def _check_definitions_and_references(
    root: Path,
    entries: list[dict[str, Any]],
    definitions: dict[str, dict[str, list[str]]],
    expected_counts: dict[str, int],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    count_keys = {
        "DEC": "decisions",
        "OQ": "open_questions",
        "ARC": "architecture_law",
        "ARQ": "architecture_requirements",
        "FLOW": "reference_flows",
        "FP": "feature_packs",
    }
    report["counts"].update({key: len(definitions[family]) for family, key in count_keys.items()})
    for family, count_key in count_keys.items():
        actual_ids = set(definitions[family])
        expected_count = expected_counts[count_key]
        count_matches = len(actual_ids) == expected_count
        _record_check(
            report,
            f"definition_count_{family.lower()}",
            count_matches,
            f"{family} definition count is {expected_count}"
            if count_matches
            else f"{family} definition count is {len(actual_ids)}, expected {expected_count}",
        )
        duplicate_ids = sorted(identifier for identifier, locations in definitions[family].items() if len(locations) > 1)
        _record_check(
            report,
            f"duplicate_definitions_{family.lower()}",
            not duplicate_ids,
            f"no duplicate {family} definitions"
            if not duplicate_ids
            else f"duplicate {family} definitions: {duplicate_ids}",
        )

        range_rule = integrity_rules["contiguous_ranges"].get(family)
        if range_rule is not None and expected_count:
            expected_range = _expected_contiguous(range_rule)
            contiguous = actual_ids == expected_range
            _record_check(
                report,
                f"contiguous_definitions_{family.lower()}",
                contiguous,
                f"{family} definitions match the manifest contiguous range"
                if contiguous
                else f"{family} definitions are not the expected contiguous range",
            )

    references: dict[str, set[str]] = {family: set() for family in ID_PATTERNS}
    for entry in entries:
        path = _entry_path(root, entry)
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for family, identifiers in _extract_references(text).items():
            references[family].update(identifiers)
    unresolved: list[str] = []
    for family, identifiers in references.items():
        unresolved.extend(sorted(identifier for identifier in identifiers if identifier not in definitions[family]))
    _record_check(
        report,
        "identifier_resolution",
        not unresolved,
        "all DEC/OQ/ARC/ARQ/FLOW/FP references resolve"
        if not unresolved
        else f"unresolved identifiers: {unresolved}",
    )


def _check_roadmap_gate_coverage(
    root: Path,
    entries: list[dict[str, Any]],
    definitions: dict[str, dict[str, list[str]]],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    entry = _find_entry(entries, integrity_rules["definition_sources"]["roadmap"])
    text = _read_entry_text(root, entry)
    start = text.find("# 14. Gate schedule")
    end = text.find("## 14.1", start + 1) if start != -1 else -1
    section = text[start:] if start == -1 else text[start:end if end != -1 else len(text)]
    gate_ids = ID_PATTERNS["OQ"].findall(section)
    gate_counts = Counter(gate_ids)
    gates = set(gate_ids)
    expected = set(definitions["OQ"])
    duplicates = sorted(identifier for identifier in expected if gate_counts[identifier] != 1)
    missing = sorted(expected - gates)
    extra = sorted(gates - expected)
    passed = start != -1 and not missing and not extra and not duplicates
    _record_check(
        report,
        "roadmap_gate_coverage",
        passed,
        "Roadmap gate schedule covers every current OQ exactly"
        if passed
        else f"Roadmap OQ coverage mismatch; missing={missing}, extra={extra}, duplicate_or_missing_once={duplicates}",
        path=_relative_path(entry) if entry else "",
    )


def _check_domain_ownership(
    root: Path,
    entries: list[dict[str, Any]],
    report: dict[str, Any],
    expected_counts: dict[str, int],
    integrity_rules: dict[str, Any],
) -> None:
    entry = _find_entry(entries, integrity_rules["definition_sources"]["domain_map"])
    text = _read_entry_text(root, entry)
    domain_rows = _table_rows(text, "## 3. Approved domain set", "## 4.")
    domain_names = [
        row[1].strip().strip("*").strip()
        for row in domain_rows
        if len(row) >= 2 and row[0].isdigit()
    ]
    domains = set(domain_names)
    duplicate_domains = sorted(
        name for name, count in Counter(domain_names).items() if count > 1
    )
    ownership_rows = _table_rows(
        text,
        "## 4. Platform-wide business-truth ownership matrix",
        "### 4.1 Ownership interpretation",
    )
    ownership_rows = [row for row in ownership_rows if len(row) >= 2 and row[0] != "Business truth"]
    report["counts"]["domains"] = len(domain_names)
    report["counts"]["ownership_rows"] = len(ownership_rows)
    _record_check(
        report,
        "domain_count",
        len(domain_names) == expected_counts["domains"],
        f"approved domain row count is {expected_counts['domains']}"
        if len(domain_names) == expected_counts["domains"]
        else f"approved domain row count is {len(domain_names)}, expected {expected_counts['domains']}",
        path=_relative_path(entry) if entry else "",
    )
    _record_check(
        report,
        "duplicate_domain_names",
        not duplicate_domains,
        "approved domain names are unique"
        if not duplicate_domains
        else f"duplicate approved domain names: {duplicate_domains}",
        path=_relative_path(entry) if entry else "",
    )
    _record_check(
        report,
        "ownership_row_count",
        len(ownership_rows) == expected_counts["ownership_rows"],
        f"ownership row count is {expected_counts['ownership_rows']}"
        if len(ownership_rows) == expected_counts["ownership_rows"]
        else f"ownership row count is {len(ownership_rows)}, expected {expected_counts['ownership_rows']}",
        path=_relative_path(entry) if entry else "",
    )
    invalid_rows: list[str] = []
    for row in ownership_rows:
        owners = [owner.strip() for owner in BOLD_PATTERN.findall(row[1])]
        if len(owners) != 1 or owners[0] not in domains:
            invalid_rows.append(row[0])
    _record_check(
        report,
        "domain_ownership_uniqueness",
        not invalid_rows,
        "every durable-truth row has exactly one approved owner"
        if not invalid_rows
        else f"invalid ownership rows: {invalid_rows}",
        path=_relative_path(entry) if entry else "",
    )


def _path_is_under(path: str, directory: str) -> bool:
    normalized_directory = directory.rstrip("/")
    return path.startswith(f"{normalized_directory}/")


def _check_production_graph(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    entries = _all_entries(manifest)
    governing_entries = _entries_for_array(manifest, "governing_documents")
    reference_entries = _entries_for_array(manifest, "reference_documents")
    historical_entries = _entries_for_array(manifest, "historical_documents")
    governing_paths = {_relative_path(entry) for entry in governing_entries}
    reference_paths = {_relative_path(entry) for entry in reference_entries}
    historical_paths = {_relative_path(entry) for entry in historical_entries}
    roots = integrity_rules["document_roots"]
    context_index = roots["context_index"]
    context_path = _safe_repository_path(root, context_index)
    roots_ok = (
        bool(governing_entries)
        and bool(reference_entries)
        and all(_path_is_under(path, roots["governing"]) for path in governing_paths)
        and all(_path_is_under(path, roots["reference"]) for path in reference_paths)
        and all(_path_is_under(path, roots["historical"]) for path in historical_paths)
        and context_path is not None
        and context_path.is_file()
    )
    _record_check(
        report,
        "authority_paths",
        roots_ok,
        "manifest authority, reference, and historical paths match declared document roots"
        if roots_ok
        else f"document graph root mismatch; governing={sorted(governing_paths)}, reference={sorted(reference_paths)}, historical={sorted(historical_paths)}",
    )

    readme = context_path
    readme_text = readme.read_text(encoding="utf-8") if readme is not None and readme.is_file() else ""
    graph_rules = integrity_rules["graph_rules"]
    stale_patterns = tuple(re.compile(pattern) for pattern in graph_rules["stale_reference_patterns"])
    navigation_document_ids = set(graph_rules["navigation_document_ids"])
    navigation_entries = [
        entry
        for entry in entries
        if entry.get("lifecycle") == "current"
        and isinstance(entry.get("document_id"), str)
        and entry.get("document_id") in navigation_document_ids
    ]
    stale_hits: list[str] = []
    scan_targets = [(context_index, False)] + [
        (_relative_path(entry), _path_is_under(_relative_path(entry), roots["reference"]))
        for entry in navigation_entries
    ]
    for relative, is_reference in scan_targets:
        path = _safe_repository_path(root, relative)
        if path is None or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if is_reference:
            text = "\n".join(text.splitlines()[: graph_rules["reference_header_lines"]])
            patterns = stale_patterns[:1] + stale_patterns[-1:]
        else:
            patterns = stale_patterns
        for pattern in patterns:
            if pattern.search(text):
                stale_hits.append(f"{relative}: {pattern.pattern}")
    _record_check(
        report,
        "active_document_graph",
        not stale_hits,
        "active document graph contains no stale moved-path references"
        if not stale_hits
        else f"stale active graph references: {stale_hits}",
    )

def _check_development_entry_boundary(
    root: Path,
    entries: list[dict[str, Any]],
    report: dict[str, Any],
) -> dict[str, Any] | None:
    open_work_entries = [
        entry
        for entry in entries
        if entry.get("document_id") == "OPEN_WORK"
        and entry.get("lifecycle") == "current"
    ]
    state_path = "OPEN_WORK"
    try:
        if len(open_work_entries) != 1:
            raise ValueError("manifest must identify exactly one current OPEN_WORK document")
        state_entry = open_work_entries[0]
        state_path = _relative_path(state_entry)
        open_work_path = _entry_path(root, state_entry)
        if not open_work_path.is_file():
            raise ValueError("current OPEN_WORK document is missing")
        state = _parse_marked_open_work_state(open_work_path.read_text(encoding="utf-8"))
        application_implementation = state.get("application_implementation")
        if not isinstance(application_implementation, str) or application_implementation not in {
            "BLOCKED",
            "AUTHORISED",
        }:
            raise ValueError(
                "application_implementation must be BLOCKED or AUTHORISED"
            )
    except (OSError, UnicodeError, ValueError) as error:
        _record_check(
            report,
            "development_entry_repository_boundary",
            False,
            f"cannot establish application implementation state: {error}",
            path=state_path,
        )
        return None

    blocked = application_implementation == "BLOCKED"
    for relative in PHOENIX_APPLICATION_ROOTS:
        application_root = root / relative
        exists = application_root.exists() or application_root.is_symlink()
        permitted = not blocked or not exists
        if blocked and exists:
            message = "application root exists while application implementation is BLOCKED"
        elif blocked:
            message = "application root is absent while application implementation is BLOCKED"
        else:
            message = "application root is permitted while application implementation is AUTHORISED"
        _record_check(
            report,
            "development_entry_repository_boundary",
            permitted,
            message,
            path=relative,
        )
    return state


def run_audit(
    root: Path,
    manifest_path: Path,
    expected_counts: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Run all foundation checks and return a JSON-serializable report."""

    root = Path(root)
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
        _record_check(report, "manifest_load", False, f"cannot load manifest: {error}", path=str(manifest_path))
        report["assertion_count"] = len(report["checks"])
        report["status"] = "FAIL"
        return report

    entries = _check_manifest_shape(root, manifest, report)
    try:
        integrity_rules = _load_integrity_rules(manifest)
    except ValueError as error:
        _record_check(report, "manifest_integrity_rules", False, str(error))
        report["assertion_count"] = len(report["checks"])
        report["status"] = "FAIL"
        return report
    _record_check(report, "manifest_integrity_rules", True, "manifest integrity rules are valid")

    _check_manifest_lifecycle_and_paths(root, manifest, entries, integrity_rules, report)
    governing_entries = _entries_for_array(manifest, "governing_documents")
    reference_entries = _entries_for_array(manifest, "reference_documents")
    _check_current_authority_roles(governing_entries, reference_entries, report)
    _check_readme_manifest_current_authority_parity(root, manifest, integrity_rules, report)
    _check_readme_active_state_mirror(root, manifest, integrity_rules, report)
    _check_manifest_predecessors(manifest, report)

    counts_expectation = dict(
        integrity_rules["expected_counts"] if expected_counts is None else expected_counts
    )
    _check_manifest_entries(root, entries, report)
    open_work_state = _check_development_entry_boundary(root, entries, report)
    phase_7_report = validate_phase_7_state(open_work_state or {}, root)
    for check in phase_7_report["checks"]:
        _record_check(
            report,
            check["name"],
            check["status"] == "PASS",
            check["message"],
            path=check.get("path", ""),
        )
    definitions = _build_definitions(root, entries, integrity_rules, report)
    _check_definitions_and_references(
        root, entries, definitions, counts_expectation, integrity_rules, report
    )
    _check_roadmap_gate_coverage(root, entries, definitions, integrity_rules, report)
    _check_domain_ownership(root, entries, report, counts_expectation, integrity_rules)
    if _production_mode(expected_counts):
        _check_production_graph(root, manifest, integrity_rules, report)
    else:
        _record_check(report, "fixture_graph_scope", True, "fixture graph checks use explicit reduced expectations")

    report["assertion_count"] = len(report["checks"])
    report["status"] = "PASS" if not report["findings"] else "FAIL"
    return report


def refresh_manifest(root: Path, manifest_path: Path) -> None:
    root = Path(root)
    manifest_path = Path(manifest_path)
    if not manifest_path.is_absolute():
        manifest_path = root / manifest_path
    manifest = load_manifest(manifest_path)
    for entry in _all_entries(manifest):
        path = _entry_path(root, entry)
        if path.is_file():
            entry["sha256"] = sha256_file(path)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _print_human_report(report: dict[str, Any]) -> None:
    print(f"FOUNDATION INTEGRITY AUDIT: {report['status']}")
    for key in (
        "decisions",
        "open_questions",
        "architecture_law",
        "architecture_requirements",
        "reference_flows",
        "domains",
        "ownership_rows",
        "feature_packs",
    ):
        if key in report["counts"]:
            print(f"{key}: {report['counts'][key]}")
    print(f"checks: {report['assertion_count']}")
    if report["findings"]:
        for finding in report["findings"]:
            location = f" [{finding['path']}]" if finding["path"] else ""
            print(f"FAIL {finding['check']}{location}: {finding['message']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None, help="repository root (defaults to this repository)")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--json", action="store_true", dest="as_json", help="emit the full JSON report")
    parser.add_argument(
        "--refresh-manifest",
        nargs="?",
        const=DEFAULT_MANIFEST,
        type=Path,
        metavar="PATH",
        help="refresh existing manifest SHA-256 fields before auditing",
    )
    args = parser.parse_args(argv)
    root = args.root or _default_root()
    manifest_path = args.manifest
    if args.refresh_manifest is not None:
        refresh_manifest(root, args.refresh_manifest)
        manifest_path = args.refresh_manifest
    report = run_audit(root, manifest_path)
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        _print_human_report(report)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
