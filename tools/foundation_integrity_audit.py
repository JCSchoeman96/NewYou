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
from typing import Any, Iterable


DEFAULT_MANIFEST = Path("docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")

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
}

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


def _all_entries(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for key in ("governing_documents", "reference_documents", "historical_documents"):
        value = manifest.get(key, [])
        if isinstance(value, list):
            entries.extend(entry for entry in value if isinstance(entry, dict))
    return entries


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
    return str(entry.get("repository_path", ""))


def _entry_path(root: Path, entry: dict[str, Any]) -> Path:
    return root / _relative_path(entry)


def _find_entry(entries: Iterable[dict[str, Any]], authority_class: str) -> dict[str, Any] | None:
    for entry in entries:
        if entry.get("authority_class") == authority_class and entry.get("lifecycle", "current") != "historical":
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
    _record_check(
        report,
        "manifest_schema",
        arrays_ok and bool(entries),
        "manifest contains governing, reference, and historical document arrays",
    )

    seen_ids: dict[str, int] = {}
    seen_paths: dict[str, int] = {}
    for entry in entries:
        for field in REQUIRED_ENTRY_FIELDS:
            if field not in entry:
                report["findings"].append(
                    {
                        "check": "manifest_schema",
                        "path": _relative_path(entry),
                        "message": f"missing manifest field {field}",
                    }
                )
        document_id = str(entry.get("document_id", ""))
        repository_path = _relative_path(entry)
        seen_ids[document_id] = seen_ids.get(document_id, 0) + 1
        seen_paths[repository_path] = seen_paths.get(repository_path, 0) + 1

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
        is_historical = entry.get("lifecycle", "current") == "historical"
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


def _markdown_section(text: str, heading: str) -> str | None:
    depth = len(heading) - len(heading.lstrip("#"))
    start = re.search(rf"(?m)^{re.escape(heading)}[ \t]*$", text)
    if start is None:
        return None
    remainder = text[start.end():]
    end = re.search(rf"(?m)^#{{1,{depth}}}[ \t]+", remainder)
    return remainder[:end.start()] if end is not None else remainder


def _default_authority_filenames(section: str | None) -> list[str]:
    if section is None:
        return []
    return re.findall(r"(?m)^\s*\d+\.\s+`([^`]+)`\s*$", section)


CURRENT_ROUTE_LABELS = (
    "CURRENT AUTHORITY-STAGE PROGRAMME",
    "NEXT STAGE",
    "CURRENT GOVERNANCE CONTRACT",
)


def _current_route_fields(section: str | None) -> tuple[dict[str, str], set[str]]:
    fields: dict[str, str] = {}
    invalid: set[str] = set()
    if section is None:
        return fields, invalid
    for label in CURRENT_ROUTE_LABELS:
        matches = re.findall(
            rf"(?m)^\s*(?:-\s*)?{re.escape(label)}:\s*(.*?)\s*$",
            section,
        )
        if len(matches) != 1 or not matches[0]:
            if matches:
                invalid.add(label)
        else:
            fields[label] = matches[0]
    return fields, invalid


def _check_current_authority_routing(
    root: Path,
    manifest: dict[str, Any],
    roots: dict[str, str],
    readme_text: str,
    report: dict[str, Any],
) -> None:
    governing_entries = [
        entry for entry in manifest.get("governing_documents", []) if isinstance(entry, dict)
    ]
    current_authority_section = _markdown_section(readme_text, "## Default Agent Context")
    expected_order = [str(entry.get("canonical_filename", "")) for entry in governing_entries]
    readme_order = _default_authority_filenames(current_authority_section)
    authority_order_ok = bool(current_authority_section is not None) and readme_order == expected_order
    _record_check(
        report,
        "readme_current_authority_order",
        authority_order_ok,
        "README default context lists governing documents in manifest order"
        if authority_order_ok
        else f"README default-context authority order mismatch: {readme_order}",
        path=roots["context_index"],
    )

    open_work_entries = [
        entry for entry in governing_entries if entry.get("document_id") == "OPEN_WORK"
    ]
    current_open_work = [
        entry for entry in open_work_entries if entry.get("lifecycle", "current") == "current"
    ]
    unique_current_open_work = len(open_work_entries) == 1 and len(current_open_work) == 1
    open_work_entry = current_open_work[0] if unique_current_open_work else None
    open_work_path = _relative_path(open_work_entry) if open_work_entry is not None else ""
    current_historical_paths = {
        _relative_path(entry)
        for entry in manifest.get("historical_documents", [])
        if isinstance(entry, dict)
    }
    canonical_filename = (
        str(open_work_entry.get("canonical_filename", "")) if open_work_entry is not None else ""
    )
    open_work_path_ok = (
        open_work_entry is not None
        and _path_is_under(open_work_path, roots["governing"])
        and not _path_is_under(open_work_path, roots["historical"])
        and Path(open_work_path).name == canonical_filename
        and open_work_path not in current_historical_paths
        and (root / open_work_path).is_file()
    )
    _record_check(
        report,
        "single_current_open_work",
        unique_current_open_work and open_work_path_ok,
        "manifest has exactly one current Open Work under the governing root"
        if unique_current_open_work and open_work_path_ok
        else f"expected one current governing OPEN_WORK entry with a current path; found {len(open_work_entries)}",
        path=open_work_path,
    )

    routed_open_work_count = readme_order.count(canonical_filename) if canonical_filename else 0
    readme_open_work_ok = (
        unique_current_open_work
        and open_work_path_ok
        and routed_open_work_count == 1
        and readme_order == expected_order
    )
    _record_check(
        report,
        "readme_open_work_manifest_parity",
        readme_open_work_ok,
        f"README routes the single manifest OPEN_WORK entry at {open_work_path}"
        if readme_open_work_ok
        else f"README current Open Work route does not match the manifest entry: {open_work_path or 'missing'}",
        path=open_work_path,
    )

    readme_state = _current_route_fields(_markdown_section(readme_text, "## Current State"))
    open_work_text = (
        (root / open_work_path).read_text(encoding="utf-8")
        if open_work_path_ok
        else ""
    )
    open_work_state = _current_route_fields(
        _markdown_section(open_work_text, "# 9. Immediate Next Action")
    )
    readme_fields, readme_invalid = readme_state
    open_work_fields, open_work_invalid = open_work_state
    required_route_labels = CURRENT_ROUTE_LABELS
    route_parity_ok = (
        not readme_invalid
        and not open_work_invalid
        and all(label in readme_fields and label in open_work_fields for label in required_route_labels)
        and all(readme_fields[label] == open_work_fields[label] for label in required_route_labels)
    )

    contract_label = CURRENT_ROUTE_LABELS[2]
    readme_contract = readme_fields.get(contract_label)
    open_work_contract = open_work_fields.get(contract_label)
    contract_route_match = re.fullmatch(
        r"v(?P<version>\d+\.\d+\.\d+)\s*/\s*(?P<path>[A-Za-z0-9_./-]+\.md)",
        readme_contract or "",
    )
    contract_route_path = (
        f"{roots['governing']}/{contract_route_match.group('path')}"
        if contract_route_match is not None
        else ""
    )
    contract_version_match = (
        VERSION_PATTERN.search(Path(contract_route_match.group("path")).name)
        if contract_route_match is not None
        else None
    )
    contract_file = root / contract_route_path if contract_route_path else None
    contract_path_is_current = (
        bool(contract_route_path)
        and ".." not in Path(contract_route_path).parts
        and _path_is_under(contract_route_path, roots["governing"])
        and not _path_is_under(contract_route_path, roots["historical"])
    )
    contract_metadata = (
        contract_file.read_text(encoding="utf-8")
        if contract_file is not None and contract_file.is_file()
        else ""
    )
    contract_id_match = re.search(
        r"(?m)^-\s+\*\*Contract ID:\*\*\s+`?([A-Za-z0-9_-]+)`?\s*$",
        contract_metadata,
    )
    contract_document_version_match = re.search(
        r"(?m)^-\s+\*\*Plan / contract version:\*\*\s+`?v?(\d+\.\d+\.\d+)`?\s*$",
        contract_metadata,
    )
    programme_name = readme_fields.get(CURRENT_ROUTE_LABELS[0], "")
    contract_identity_ok = (
        contract_id_match is not None
        and contract_document_version_match is not None
        and contract_id_match.group(1).casefold() in programme_name.casefold()
        and Path(contract_route_match.group("path")).name.startswith(
            f"{contract_id_match.group(1)}_"
        )
        and contract_document_version_match.group(1) == contract_route_match.group("version")
    )
    route_parity_ok = route_parity_ok and (
        readme_contract is not None
        and readme_contract == open_work_contract
        and contract_route_match is not None
        and contract_version_match is not None
        and contract_version_match.group(1) == contract_route_match.group("version")
        and contract_path_is_current
        and contract_identity_ok
        and contract_file is not None
        and contract_file.is_file()
    )

    _record_check(
        report,
        "readme_open_work_state_parity",
        route_parity_ok,
        "README and current Open Work agree on programme, next stage and routed contract"
        if route_parity_ok
        else "README and current Open Work current-state route fields are missing or disagree",
        path=open_work_path,
    )


def _check_production_graph(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    entries = _all_entries(manifest)
    governing_entries = [
        entry for entry in manifest.get("governing_documents", []) if isinstance(entry, dict)
    ]
    reference_entries = [
        entry for entry in manifest.get("reference_documents", []) if isinstance(entry, dict)
    ]
    historical_entries = [
        entry for entry in manifest.get("historical_documents", []) if isinstance(entry, dict)
    ]
    governing_paths = {_relative_path(entry) for entry in governing_entries}
    reference_paths = {_relative_path(entry) for entry in reference_entries}
    historical_paths = {_relative_path(entry) for entry in historical_entries}
    roots = integrity_rules["document_roots"]
    roots_ok = (
        bool(governing_entries)
        and bool(reference_entries)
        and all(_path_is_under(path, roots["governing"]) for path in governing_paths)
        and all(_path_is_under(path, roots["reference"]) for path in reference_paths)
        and all(_path_is_under(path, roots["historical"]) for path in historical_paths)
        and (root / roots["context_index"]).is_file()
    )
    _record_check(
        report,
        "authority_paths",
        roots_ok,
        "manifest authority, reference, and historical paths match declared document roots"
        if roots_ok
        else f"document graph root mismatch; governing={sorted(governing_paths)}, reference={sorted(reference_paths)}, historical={sorted(historical_paths)}",
    )

    context_index = roots["context_index"]
    readme = root / context_index
    readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    _check_current_authority_routing(root, manifest, roots, readme_text, report)

    graph_rules = integrity_rules["graph_rules"]
    stale_patterns = tuple(re.compile(pattern) for pattern in graph_rules["stale_reference_patterns"])
    navigation_document_ids = set(graph_rules["navigation_document_ids"])
    navigation_entries = [
        entry
        for entry in entries
        if entry.get("lifecycle", "current") != "historical"
        and entry.get("document_id") in navigation_document_ids
    ]
    stale_hits: list[str] = []
    scan_targets = [(context_index, False)] + [
        (_relative_path(entry), _path_is_under(_relative_path(entry), roots["reference"]))
        for entry in navigation_entries
    ]
    for relative, is_reference in scan_targets:
        path = root / relative
        if not path.is_file():
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

    open_work_entry = next(
        (entry for entry in governing_entries if entry.get("document_id") == "OPEN_WORK"),
        None,
    )
    readiness_paths = [roots["context_index"]]
    if open_work_entry is not None:
        readiness_paths.append(_relative_path(open_work_entry))
    readiness_text = "\n".join(
        (root / relative).read_text(encoding="utf-8")
        for relative in readiness_paths
        if (root / relative).is_file()
    )
    legacy_next = "NEXT: PHASE 7 / FP-001 PREPARATION" in readiness_text
    stage_3a1_started = "STAGE 3A.1" in readiness_text and "NOT_STARTED" in readiness_text
    stage_3a1_complete = (
        "STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE" in readiness_text
        and "STAGE 3A.2 — GOVERNED AR-000 AMENDMENT" in readiness_text
        and "NOT_STARTED / NEXT" in readiness_text
    )
    readiness_ok = (
        "PLANNING FOUNDATION: READY" in readiness_text
        and "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS" in readiness_text
        and (legacy_next or stage_3a1_started or stage_3a1_complete)
    )
    _record_check(
        report,
        "readiness_wording",
        readiness_ok,
        "current readiness wording distinguishes planning from executable development"
        if readiness_ok
        else "current readiness wording is incomplete",
    )


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

    counts_expectation = dict(
        integrity_rules["expected_counts"] if expected_counts is None else expected_counts
    )
    _check_manifest_entries(root, entries, report)
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
