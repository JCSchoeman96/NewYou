#!/usr/bin/env python3
"""Deterministic integrity checks for the NewYou planning foundation."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import tarfile
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
CURRENT_ROUTE_FILENAME_PATTERN = re.compile(
    r"(?<![\w/.-])(?:[\w.-]+/)*[\w.-]+_v\d+\.\d+\.\d+\.md"
)
CURRENT_ROUTE_VERSION_PATTERN = re.compile(r"\bv(\d+\.\d+\.\d+)\b")
TRACKER_120_OPEN_PROJECTION_PATTERN = re.compile(
    r"(?:\bopen\s+tracker\s+#120\b|\b(?:tracker|issue)\b[^;\n]{0,48}#120\b[^;.!?\n]{0,28}\bopen\b|#120\b[^;.!?\n]{0,28}\bopen\b)",
    re.IGNORECASE,
)

CURRENT_AUTHORITY_STATE_SECTIONS = {
    "PROJECT_NORTH_STAR_AND_MVP": ("# 23. Current Planning Position", "# 24. Document Stop Condition"),
    "PLATFORM_BASELINE": ("# 24. Current Planning Stop Condition", None),
}

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


def _active_open_work_entry(manifest: dict[str, Any]) -> dict[str, Any] | None:
    active = [
        entry
        for entry in _all_entries(manifest)
        if entry.get("document_id") == "OPEN_WORK"
        and entry.get("lifecycle", "current") != "historical"
    ]
    return active[0] if len(active) == 1 else None


def _fp001_phase8_candidate_route_is_current(manifest: dict[str, Any]) -> bool:
    entry = _active_open_work_entry(manifest)
    return (
        entry is not None
        and entry.get("semver") in {"1.2.77", "1.2.78"}
        and _relative_path(entry) == f"docs/00_platform/02_OPEN_WORK_v{entry.get('semver')}.md"
    )


def _fp001_phase8_approved_status_successor_is_current(
    manifest: dict[str, Any],
) -> bool:
    entry = _active_open_work_entry(manifest)
    return (
        entry is not None
        and entry.get("semver") == "1.2.78"
        and _relative_path(entry) == "docs/00_platform/02_OPEN_WORK_v1.2.78.md"
    )


def _fp001_phase8_execution_status_successor_is_current(
    manifest: dict[str, Any],
) -> bool:
    entry = _active_open_work_entry(manifest)
    phase8 = manifest.get("integrity_rules", {}).get("fp001_phase8_proof_contract_lifecycle", {})
    if entry is None or not isinstance(phase8, dict):
        return False
    current_routes = phase8.get("current_routes", {})
    if not isinstance(current_routes, dict) or current_routes.get("open_work") != _relative_path(entry):
        return False
    path_version = re.search(r"_v(\d+\.\d+\.\d+)\.md$", _relative_path(entry))
    return (
        path_version is not None
        and entry.get("semver") == path_version.group(1)
        and phase8.get("proof_execution") == "STARTED"
        and phase8.get("proof_result") == "INCOMPLETE / COVERAGE-INCOMPLETE"
        and phase8.get("proof_certification") == "NOT CERTIFIED"
    )


def _open_work_lifecycle_state(open_work: str) -> dict[str, Any] | None:
    marker_start = "<!-- HARDEN_02_LIFECYCLE_STATE_START -->"
    marker_end = "<!-- HARDEN_02_LIFECYCLE_STATE_END -->"
    if open_work.count(marker_start) != 1 or open_work.count(marker_end) != 1:
        return None
    match = re.search(
        re.escape(marker_start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(marker_end),
        open_work,
        re.DOTALL,
    )
    if match is None:
        return None
    try:
        state = json.loads(match.group(1), object_pairs_hook=_reject_duplicate_json_keys)
    except (json.JSONDecodeError, TypeError, ValueError):
        return None
    return state if isinstance(state, dict) else None


_P8_05_CURRENT_AUTHORIZATION_SECTION_RE = re.compile(
    r"(?m)^## (?:Current P8-05 implementation authorization|.*WELL-5 / P8-04 completion and P8-05 planning route|.*WELL-5 completion and P8-05 planning route \(current\))\s*$"
)


def _p8_05_current_authorization_section(text: str) -> str:
    match = _P8_05_CURRENT_AUTHORIZATION_SECTION_RE.search(text)
    if match is None:
        return ""
    section_tail = text[match.end():]
    next_section = re.search(r"(?m)^## ", section_tail)
    return section_tail[:next_section.start()] if next_section else section_tail


_P8_05_BOUNDED_APPLICATION_IMPLEMENTATION = (
    "AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION AUTHORISED"
)
_P8_05_PHASE8_EXECUTION_GATE_AUTHORISED = (
    "STARTED / BOUNDED PHASE 8 / P8-05 IMPLEMENTATION AUTHORISED"
)
_P8_05_NEXT_STAGE_AUTHORISED = (
    "P8-05 IMPLEMENTATION AUTHORISED FOR BOUNDED PHASE 8 PROOF; WELL-48–50 MAY BEGIN AFTER RESULTING-MAIN VERIFICATION"
)
_P8_05_NEXT_GOVERNANCE_ACTION_AUTHORISED = _P8_05_NEXT_STAGE_AUTHORISED


def _p8_05_current_authorization_section_tokens() -> tuple[str, ...]:
    return (
        "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
        "PHASE 8: NOT CERTIFIED",
        "TB-001 PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "WELL-45: LEGAL/PRIVACY RELEASE GATE OPEN — DEVELOPMENT BASELINE PERMITTED",
        "NOT LEGALLY APPROVED",
        "resulting-main verification",
        "WELL-48",
        "none is complete",
        "WELL-51 follows the required WELL-48–50 seams",
        "This authorization does not authorize production",
    )


def _p8_05_bounded_authorization_route_tokens() -> tuple[str, ...]:
    return _p8_05_current_authorization_section_tokens() + (
        "WELL-5 / P8-04 deterministic proof harness implementation is COMPLETE",
        "proof certification is not complete",
        "INCOMPLETE / COVERAGE-INCOMPLETE",
        "NOT CERTIFIED",
        "Phase 8 is NOT CERTIFIED",
        "Phase 9 / Vertical Slices remain NOT STARTED / NOT AUTHORISED",
        "business/browser manifests remain unavailable",
        "P8-05 / WELL-6 Grill-Me/JIT planning and spec/ticket decomposition are complete",
        "independent planning review is COMPLETE / PASS WITH NON-BLOCKING CORRECTIONS",
        "WELL-45 is LEGAL/PRIVACY RELEASE GATE OPEN — DEVELOPMENT BASELINE PERMITTED",
        "not legally approved",
        "WELL-48–50: NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION",
        "Production, public release, paid pilot and applicable real-participant flows remain fail-closed",
    )


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
    references = {
        family: set(pattern.findall(text))
        for family, pattern in ID_PATTERNS.items()
    }
    # An Atlas integrity note may explicitly deny an unassigned Feature Pack ID
    # (for example, "no FP-018 ... Feature Pack exists"). Keep negative assertions
    # out of unresolved references while still checking positive FP references.
    negative_fp_mentions = set(re.findall(r"(?i)\bno\s+(FP-\d{3})\b", text))
    references["FP"].difference_update(negative_fp_mentions)
    return references


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


def _marked_matrix_rows(text: str, matrix_name: str) -> list[dict[str, str]]:
    start_marker = f"<!-- NEWYOU:PRODUCT-MATRIX:{matrix_name}:START -->"
    end_marker = f"<!-- NEWYOU:PRODUCT-MATRIX:{matrix_name}:END -->"
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        return []
    section = text.split(start_marker, 1)[1].split(end_marker, 1)[0]
    lines = [line for line in section.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return []

    def cells(line: str) -> list[str]:
        return [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]

    headers = cells(lines[0])
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        values = cells(line)
        if len(values) != len(headers):
            return []
        rows.append(dict(zip(headers, values)))
    return rows


H02_LIFECYCLE_MATRIX_GATES = (
    "CONTRACT_LIFECYCLE",
    "PRE_MERGE_CERTIFICATION",
    "EXACT_HEAD_CI",
    "CERTIFIED_HEAD_MERGE",
    "RESULTING_MAIN_CI",
    "POST_MERGE_INDEPENDENT_REVIEW",
    "POST_MERGE_ATTESTATION",
    "EXECUTION",
)

H02_LIFECYCLE_MATRIX_STATUSES = {
    "CONTRACT_LIFECYCLE": "COMPLETE / CERTIFIED",
    "PRE_MERGE_CERTIFICATION": "COMPLETE",
    "EXACT_HEAD_CI": "PASS",
    "CERTIFIED_HEAD_MERGE": "COMPLETE_UNCHANGED",
    "RESULTING_MAIN_CI": "PASS",
    "POST_MERGE_INDEPENDENT_REVIEW": "PASS",
    "POST_MERGE_ATTESTATION": "COMPLETE",
}

H02_PR40_LIFECYCLE_FACTS = {
    "certified_contract_version": "0.4.0",
    "contract_status": "COMPLETE / CERTIFIED",
    "pr_40_certified_head": "cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4",
    "pr_40_merged_sha": "352f304139b9d4f8ee3ba205cde9e34d0ad8437f",
    "pr_40_merged_unchanged": True,
    "merge_base_sha": "6f9ce049616881805b1086d19ce747358de3c067",
    "merge_certified_head_second_parent": "cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4",
    "merge_tree_matches_certified_head": True,
    "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5827553565",
    "pre_merge_independent_review_actor": "ChatGPT / GPT-5.6 Sol",
    "pre_merge_attestation_poster": "JCSchoeman96",
    "pre_merge_poster_equals_pr_author_disclosed": True,
    "pre_merge_review_actor_authored_or_modified_candidate": False,
    "pre_merge_substantive_reviewer_is_review_actor_not_poster": True,
    "exact_head_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36091130615",
    "exact_head_ci_head_sha": "cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4",
    "exact_head_ci_workflow": "Foundation Integrity",
    "exact_head_ci_conclusion": "PASS",
    "pre_merge_certification": "COMPLETE",
    "pr_40_exact_head_ci": "PASS / 36091130615 / 142 TESTS / 280 FIA CHECKS / NO FINDINGS",
    "certified_head_merge": "COMPLETE_UNCHANGED",
    "post_merge_ci": "PASS",
    "resulting_main_ci": "PASS",
    "resulting_main_ci_evidence": "PASS / 36101210535 / 142 TESTS / 280 FIA CHECKS / NO FINDINGS",
    "resulting_main_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36101210535",
    "resulting_main_ci_head_sha": "352f304139b9d4f8ee3ba205cde9e34d0ad8437f",
    "resulting_main_ci_workflow": "Foundation Integrity",
    "resulting_main_ci_conclusion": "PASS",
    "post_merge_independent_review": "PASS",
    "post_merge_independent_review_actor": "Codex / GPT-6",
    "post_merge_attestation_poster": "JCSchoeman96",
    "post_merge_poster_equals_pr_author_disclosed": True,
    "post_merge_review_actor_authored_or_modified_candidate": False,
    "post_merge_substantive_reviewer_is_review_actor_not_poster": True,
    "post_merge_attestation": "COMPLETE",
    "post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5830618876",
    "pr_39_merged": True,
    "v0_3_0_retroactive_certification": "NOT SATISFIED",
    "exact_head_ci": "PASS",
    "post_merge_certification": "COMPLETE",
}

H02_EXECUTION_STATES = {
    "NEXT / AUTHORISED / NOT STARTED": {
        "matrix": "NEXT_AUTHORISED_NOT_STARTED",
        "successor_versions": ("0.4.2",),
        "current_stage": "HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
        "next_stage": "HARDEN-02_EXECUTION_REQUIRED",
        "readme": "HARDEN-02 EXECUTION: NEXT / AUTHORISED / NOT STARTED",
        "programme_status": "HARDEN-02 EXECUTION NEXT / AUTHORISED / NOT STARTED",
    },
    "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING": {
        "matrix": "IN_PROGRESS_NOT_COMPLETE_CERTIFICATION_PENDING",
        "successor_versions": ("0.4.3", "0.4.4", "0.4.5", "0.4.6"),
        "current_stage": "HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
        "next_stage": "HARDEN-02_EXECUTION_REQUIRED",
        "readme": "HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
        "programme_status": "HARDEN-02 EXECUTION IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
    },
    "COMPLETE / CERTIFIED": {
        "matrix": "COMPLETE_CERTIFIED",
        "successor_versions": ("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3", "0.5.4", "0.5.5", "0.5.6", "0.5.7"),
        "current_stage": "COMMUNICATIONS v0.1.0 CURRENT-STATUS PROMOTION",
        "next_stage": "REMAINING REQUIRED / CONDITIONAL PHASE 7B",
        "readme": "HARDEN-02 EXECUTION: COMPLETE / CERTIFIED",
        "programme_status": "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION COMPLETE / CERTIFIED; FP-001 RECONCILIATION COMPLETE / CERTIFIED; IDENTITY v0.1.4 COMPLETE / CERTIFIED / CURRENT; COMMUNICATIONS DOSSIER v0.1.0 COMPLETE / CERTIFIED / CURRENT",
    },
}

H02_COMPLETE_CERTIFICATION_FACTS = {
    "historical_execution_pr56": {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/56",
        "exact_head_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36452024211",
        "exact_head_ci_result": "PASS / 229 TESTS / 424 FIA ASSERTIONS / ZERO FINDINGS",
        "resulting_main_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36462211976",
        "resulting_main_ci_result": "PASS / 229 TESTS / 424 FIA ASSERTIONS / ZERO FINDINGS",
        "classification": "HISTORICAL EXECUTION EVIDENCE; NOT THE FINAL COMPLETION CERTIFICATION",
    },
    "pr57_prospective_recovery": {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/57",
        "candidate_head_sha": "264ca5f7dfd600440e9b4e53adac9929e46b30d3",
        "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/57#issuecomment-5889396716",
        "exact_head_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36556153518",
        "resulting_main_sha": "11ac2d940cf1e9728ea40f505ac44eafe45f305b",
        "resulting_main_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36563392212",
        "classification": "PROSPECTIVE RECOVERY; PR #59 LATER FOUND A SUMMARY-PATH BYPASS; REQUIRED DURABLE POST-MERGE ATTESTATION WAS ABSENT",
    },
    "pr59_final_summary_recovery": {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/59",
        "base_main_sha": "11ac2d940cf1e9728ea40f505ac44eafe45f305b",
        "candidate_sha": "0dd89f749eb3d3dbd659d1f6f01485984952ddfd",
        "candidate_tree_sha": "9c7f70df8fd4d7a688e7c76e7c217cf33c0c5752",
        "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/59#issuecomment-5890210520",
        "exact_head_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36565948391",
        "exact_head_ci_result": "PASS / 241 TESTS / 451 FIA ASSERTIONS / ZERO FINDINGS",
        "resulting_main_sha": "6fea69eadf18f2fb79d78c2a94ab035b10abe31f",
        "resulting_main_tree_sha": "9c7f70df8fd4d7a688e7c76e7c217cf33c0c5752",
        "resulting_main_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36567933267",
        "resulting_main_ci_result": "PASS / 241 TESTS / 451 FIA ASSERTIONS / ZERO FINDINGS",
        "post_merge_review_outcome": "PASS WITH NON-BLOCKING CORRECTIONS",
        "non_blocking_correction": "Direct helper-level mutation coverage for the Roadmap §21 fenced phase-diagram body was absent. On resulting main 6fea69e, the entire Roadmap §21 section remained byte-identical to its archived source, so the reviewer classified this as non-blocking.",
        "post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/59#issuecomment-5890574449",
    },
    "current_main_revalidation": {
        "main_sha": "d4e7390b71cdf61b649b534e1080102a044efe63",
        "foundation_integrity_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36856102830",
        "foundation_integrity_job_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36856102830/job/110348834922",
        "unit_tests": "251 PASS",
        "invariant_proofs": "I-01 THROUGH I-13 PASS",
        "i04_adversarial_tests": "BOTH PASS",
        "fia_assertions": 506,
        "fia_findings": 0,
        "fia_result": "PASS",
    },
    "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/59#issuecomment-5890210520",
    "exact_head_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36565948391",
    "candidate_sha": "0dd89f749eb3d3dbd659d1f6f01485984952ddfd",
    "resulting_main_sha": "6fea69eadf18f2fb79d78c2a94ab035b10abe31f",
    "resulting_main_tree_sha": "9c7f70df8fd4d7a688e7c76e7c217cf33c0c5752",
    "resulting_main_ci_run_url": "https://github.com/JCSchoeman96/NewYou/actions/runs/36567933267",
    "post_merge_review_outcome": "PASS WITH NON-BLOCKING CORRECTIONS",
    "post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/59#issuecomment-5890574449",
    "whole_roadmap_section_21_preserved_sha256": "611abef74ce306eba824f44241189413c6be0c305c922166f3a338cc7f019b83",
    "whole_roadmap_section_21_test": "test_all_feature_pack_sections_and_section_21_are_exactly_preserved",
}


def _reject_duplicate_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _markdown_header_metadata(text: str, expected_title: str) -> list[str] | None:
    """Return the contiguous metadata bullets directly below a document title."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != expected_title:
        return None
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    fields: list[str] = []
    while index < len(lines) and lines[index].startswith("- "):
        fields.append(lines[index])
        index += 1
    return fields or None


def _metadata_values(fields: list[str] | None, label: str) -> list[str]:
    if fields is None:
        return []
    pattern = re.compile(rf"^-\s+\*\*{re.escape(label)}:\*\*\s*(.*?)\s*$")
    return [match.group(1) for field in fields if (match := pattern.fullmatch(field))]


def _metadata_declarations(text: str, label: str) -> list[str]:
    """Find exact Markdown metadata declarations outside fenced code examples."""
    pattern = re.compile(rf"^-\s+\*\*{re.escape(label)}:\*\*\s*(.*?)\s*$")
    declarations: list[str] = []
    fence_character: str | None = None
    fence_length = 0
    for line in text.splitlines():
        if fence_character is not None:
            closing_fence = re.fullmatch(
                rf" {{0,3}}{re.escape(fence_character)}{{{fence_length},}}[ \t]*",
                line,
            )
            if closing_fence is not None:
                fence_character = None
                fence_length = 0
            continue

        opening_fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if opening_fence is not None:
            marker = opening_fence.group(1)
            info_string = opening_fence.group(2)
            if marker[0] == "`" and "`" in info_string:
                continue
            fence_character = marker[0]
            fence_length = len(marker)
            continue

        if match := pattern.fullmatch(line):
            declarations.append(match.group(1))
    return declarations


def _h02_lifecycle_state(
    open_work: str,
    readme: str,
    contract: str = "",
) -> tuple[bool, str]:
    """Fail closed across HARDEN-02 lifecycle, completion proof and downstream routing."""
    matrix_start = "<!-- NEWYOU:PRODUCT-MATRIX:HARDEN-02-LIFECYCLE:START -->"
    matrix_end = "<!-- NEWYOU:PRODUCT-MATRIX:HARDEN-02-LIFECYCLE:END -->"
    json_start = "<!-- HARDEN_02_LIFECYCLE_STATE_START -->"
    json_end = "<!-- HARDEN_02_LIFECYCLE_STATE_END -->"
    markers = (matrix_start, matrix_end, json_start, json_end)
    if any(open_work.count(marker) != 1 for marker in markers):
        return False, "HARDEN lifecycle markers are missing or duplicated"

    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    if active_start < 0 or active_end < 0 or active_start >= active_end:
        return False, "HARDEN active-state section is missing or malformed"
    if any(not active_start < open_work.find(marker) < active_end for marker in markers):
        return False, "HARDEN lifecycle markers are outside the active-state section"
    active = open_work[active_start:active_end]

    matrix_body = open_work.split(matrix_start, 1)[1].split(matrix_end, 1)[0]
    matrix_lines = [line.strip() for line in matrix_body.splitlines() if line.strip().startswith("|")]
    if len(matrix_lines) < 3:
        return False, "HARDEN lifecycle matrix is malformed"

    def cells(line: str) -> list[str]:
        return [cell.strip().strip(chr(96)) for cell in line.strip().strip("|").split("|")]

    if cells(matrix_lines[0]) != ["gate", "status", "evidence"]:
        return False, "HARDEN lifecycle matrix header is invalid"
    if not all(set(cell) <= {"-", ":", " "} for cell in cells(matrix_lines[1])):
        return False, "HARDEN lifecycle matrix separator is invalid"
    data_rows = [cells(line) for line in matrix_lines[2:]]
    if any(len(row) != 3 or not all(row) for row in data_rows):
        return False, "HARDEN lifecycle matrix contains a malformed row"
    gates = [row[0] for row in data_rows]
    if tuple(gates) != H02_LIFECYCLE_MATRIX_GATES or len(set(gates)) != len(gates):
        return False, "HARDEN lifecycle matrix gates are missing, duplicated, or out of order"
    matrix = {row[0]: row[1] for row in data_rows}
    if any(matrix.get(gate) != status for gate, status in H02_LIFECYCLE_MATRIX_STATUSES.items()):
        return False, "HARDEN v0.4.0 contract lifecycle facts are inconsistent"

    fence = chr(96) * 3
    json_region = open_work.split(json_start, 1)[1].split(json_end, 1)[0]
    json_blocks = re.findall(re.escape(fence) + r"json\s*(\{.*?\})\s*" + re.escape(fence), json_region, re.DOTALL)
    if len(json_blocks) != 1:
        return False, "HARDEN lifecycle JSON block is missing, duplicate, or malformed"
    try:
        state = json.loads(json_blocks[0], object_pairs_hook=_reject_duplicate_json_keys)
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        return False, f"HARDEN lifecycle JSON is invalid: {error}"
    if not isinstance(state, dict):
        return False, "HARDEN lifecycle JSON must be an object"
    if any(state.get(key) != value for key, value in H02_PR40_LIFECYCLE_FACTS.items()):
        return False, "prior PR #40 certification facts or certified contract lifecycle changed"
    if state.get("status_successor_version") == "1.2.74":
        return _h02_fp001_hard_stop_lifecycle_state(state, active, readme, contract)
    if state.get("status_successor_version") == "1.2.77":
        return _h02_fp001_phase8_contract_candidate_lifecycle_state(state, active, readme, contract)
    if state.get("status_successor_version") == "1.2.78":
        return _h02_fp001_phase8_contract_approved_lifecycle_state(state, active, readme, contract)
    if (
        state.get("proof_result") == "INCOMPLETE / COVERAGE-INCOMPLETE"
        or state.get("architectural_proof_execution") == "STARTED"
    ):
        return _h02_fp001_phase8_proof_execution_lifecycle_state(state, active, readme, contract)
    if state.get("status_successor_version") == "1.2.73":
        return _h02_fp001_classification_lifecycle_state(state, active, readme, contract)
    if state.get("status_successor_version") in {"0.5.9", "0.5.10", "0.5.11", "0.5.12", "0.5.13", "0.5.14", "0.5.15", "0.5.16"}:
        return _h02_audit_v010_promotion_lifecycle_state(state, active, readme, contract)

    execution = state.get("harden_02_execution")
    if execution not in H02_EXECUTION_STATES:
        return False, "HARDEN execution status is not one of the permitted lifecycle states"
    expected = dict(H02_EXECUTION_STATES[execution])
    promotion_status = state.get("engineering_standards_authority_promotion")
    if execution == "COMPLETE / CERTIFIED":
        if promotion_status == "COMPLETE / CERTIFIED":
            if state.get("status_successor_version") == "0.5.6":
                expected.update(
                    {
                        "successor_versions": ("0.5.6",),
                        "current_stage": "FP-001 PHASE 7A/7B CONDITIONAL-DOSSIER ADJUDICATION",
                        "next_stage": "FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER",
                        "programme_status": "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION COMPLETE / CERTIFIED; FP-001 RECONCILIATION COMPLETE / CERTIFIED; IDENTITY v0.1.4 COMPLETE / CERTIFIED / CURRENT under the separate PR #77 status successor; COMMUNICATIONS JIT DOMAIN DOSSIER v0.1.0 COMPLETE / CERTIFIED / CURRENT under the separate PR #81 status successor; PRIVACY & CONSENT NOT_REQUIRED; CONTENT & MEDIA NOT_REQUIRED; AUDIT & EVIDENCE REQUIRED / NEXT / NOT_STARTED; ANALYTICS NOT_REQUIRED",
                    }
                )
            elif state.get("status_successor_version") == "0.5.7":
                expected.update(
                    {
                        "successor_versions": ("0.5.7",),
                        "current_stage": "FP-001 PHASE 7B AUDIT & EVIDENCE JIT DOMAIN DOSSIER WORK START",
                        "next_stage": "AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE",
                        "programme_status": "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION COMPLETE / CERTIFIED; FP-001 RECONCILIATION COMPLETE / CERTIFIED; IDENTITY v0.1.4 COMPLETE / CERTIFIED / CURRENT under the separate PR #77 status successor; COMMUNICATIONS JIT DOMAIN DOSSIER v0.1.0 COMPLETE / CERTIFIED / CURRENT under the separate PR #81 status successor; PRIVACY & CONSENT NOT_REQUIRED; CONTENT & MEDIA NOT_REQUIRED; AUDIT & EVIDENCE REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING; ANALYTICS NOT_REQUIRED",
                    }
                )
            elif state.get("status_successor_version") == "0.5.8":
                expected.update(
                    {
                        "successor_versions": ("0.5.8",),
                        "current_stage": "FP-001 PHASE 7B AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE REVIEW",
                        "next_stage": "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION",
                        "programme_status": "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION COMPLETE / CERTIFIED; FP-001 RECONCILIATION COMPLETE / CERTIFIED; IDENTITY v0.1.4 COMPLETE / CERTIFIED / CURRENT under the separate PR #77 status successor; COMMUNICATIONS JIT DOMAIN DOSSIER v0.1.0 COMPLETE / CERTIFIED / CURRENT under the separate PR #81 status successor; PRIVACY & CONSENT NOT_REQUIRED; CONTENT & MEDIA NOT_REQUIRED; AUDIT & EVIDENCE REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING; ANALYTICS NOT_REQUIRED",
                    }
                )
            else:
                expected.update(
                    {
                        "successor_versions": ("0.5.5",),
                        "current_stage": "COMMUNICATIONS v0.1.0 CURRENT-STATUS PROMOTION",
                        "next_stage": "REMAINING REQUIRED / CONDITIONAL PHASE 7B",
                        "programme_status": "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION COMPLETE / CERTIFIED; FP-001 RECONCILIATION COMPLETE / CERTIFIED; IDENTITY v0.1.4 COMPLETE / CERTIFIED / CURRENT under the separate PR #77 status successor, based on PR #76 candidate and post-merge certification evidence; COMMUNICATIONS JIT DOMAIN DOSSIER v0.1.0 COMPLETE / CERTIFIED / CURRENT under the separate PR #81 status successor, based on PR #78 candidate and post-merge certification evidence",
                    }
                )
        elif promotion_status != "NEXT / AUTHORISED / NOT STARTED":
            return False, "completed HARDEN execution must route through one permitted Standards promotion state"
    elif promotion_status != "DOWNSTREAM / NOT STARTED":
        return False, "incomplete HARDEN execution cannot advance Engineering Standards promotion"
    if state.get("status_successor_version") not in expected["successor_versions"]:
        return False, "HARDEN status successor version is unsupported"
    if state.get("current_stage") != expected["current_stage"]:
        return False, "HARDEN current programme route disagrees with execution lifecycle state"
    if state.get("next_stage") != expected["next_stage"]:
        return False, "HARDEN NEXT stage token disagrees with execution lifecycle state"

    current_routes = re.findall(r"(?m)^CURRENT AUTHORITY-STAGE PROGRAMME:\s*(.*?)\s*$", active)
    next_routes = re.findall(r"(?m)^NEXT STAGE:\s*(.*?)\s*$", active)
    if current_routes != [expected["current_stage"]]:
        return False, "HARDEN current programme route is missing, duplicate, or contradictory"
    if next_routes != [expected["next_stage"]]:
        return False, "HARDEN next-stage token is missing, duplicate, or contradictory"

    if matrix.get("EXECUTION") != expected["matrix"]:
        return False, "HARDEN lifecycle matrix disagrees with the execution state"
    if active.count(expected["readme"]) != 1:
        return False, "Open Work current execution status is missing or duplicated"
    other_statuses = [item["readme"] for label, item in H02_EXECUTION_STATES.items() if label != execution]
    if any(status in active for status in other_statuses):
        return False, "Open Work active state contains a contradictory execution status"

    programme_start = open_work.find("## 12.1 Programme state")
    programme_end = open_work.find("## 12.2", programme_start + 1)
    if programme_start < 0 or programme_end < 0 or programme_start >= programme_end:
        return False, "Open Work programme-state table is missing or malformed"
    programme_rows = [
        line.strip()
        for line in open_work[programme_start:programme_end].splitlines()
        if line.startswith("| Current / later |")
    ]
    if len(programme_rows) != 1 or expected["programme_status"] not in programme_rows[0]:
        return False, "Open Work current programme-state row disagrees with the execution lifecycle"
    other_programme_statuses = [
        item["programme_status"] for label, item in H02_EXECUTION_STATES.items() if label != execution
    ]
    if any(status in programme_rows[0] for status in other_programme_statuses):
        return False, "Open Work current programme-state row contains a contradictory execution status"
    expected_status_version = state.get("status_successor_version")
    expected_status_path = f"working/HARDEN-02_CONTRACT_WORKING_v{expected_status_version}.md"
    if execution in {"NEXT / AUTHORISED / NOT STARTED", "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING", "COMPLETE / CERTIFIED"}:
        if expected_status_path not in programme_rows[0]:
            return False, "Open Work current programme-state row does not name its current HARDEN successor"

    expected_milestones = [
        "TARGETED PRODUCT AMENDMENT PROGRAMME",
        "FP-001 PHASE 7A",
        "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
    ]
    expected_downstream = {
        "harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY",
        "store_cer": "EXCLUDED",
        "phase_7c": "BLOCKED / NOT_STARTED",
        "proof_classification": "NOT FINALISED",
        "application_implementation": "BLOCKED",
        "pr_38": "STALE / BLOCKED / NOT AUTHORITY",
    }
    if execution == "COMPLETE / CERTIFIED":
        expected_milestones = expected_milestones + ["HARDEN-02 EXECUTION"]
        if promotion_status == "COMPLETE / CERTIFIED":
            expected_milestones = expected_milestones + [
                "ENGINEERING STANDARDS AUTHORITY PROMOTION",
                "FP-001 PMR RECONCILIATION",
                "FP-001 IDENTITY v0.1.3 DURABLE-DELIVERY PATCH PROMOTION",
                "FP-001 IDENTITY v0.1.4 GOVERNANCE-CORRECTION PATCH PROMOTION",
                "FP-001 COMMUNICATIONS v0.1.0 JIT DOMAIN DOSSIER PROMOTION",
            ]
            expected_downstream.update({
                "engineering_standards_authority_promotion": "COMPLETE / CERTIFIED",
                "fp001_reconciliation": "COMPLETE / CERTIFIED",
                "communications_dossier": "CERTIFIED / CURRENT v0.1.0",
                "communications_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
                "communications": "COMPLETE / CERTIFIED / CURRENT v0.1.0",
                "communications_finalisation": "BLOCKED / STOP",
                "pr_60": "STALE HISTORICAL CANDIDATE / SUPERSEDED BY THIS SUCCESSOR / NOT MERGED / NOT AUTHORITY",
            })
            if state.get("status_successor_version") in {"0.5.6", "0.5.7", "0.5.8"}:
                expected_milestones.append("FP-001 PHASE 7A/7B CONDITIONAL-DOSSIER ADJUDICATION")
                expected_downstream.update({
                    "audit_dossier": (
                        "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                        if state.get("status_successor_version") in {"0.5.7", "0.5.8"}
                        else "REQUIRED / NEXT / NOT_STARTED"
                    ),
                    "phase_7c_block_reason": "Audit & Evidence dossier must be COMPLETE / CERTIFIED / CURRENT and subsequent Phase 7B reconciliation must succeed",
                    "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
                })
        else:
            expected_downstream.update({
                "engineering_standards_authority_promotion": "NEXT / AUTHORISED / NOT STARTED",
                "fp001_reconciliation": "REQUIRED / DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION / NOT PERFORMED",
                "communications": "REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION",
                "pr_60": "STALE HISTORICAL CANDIDATE / SUPERSEDED BY THIS SUCCESSOR / NOT MERGED / NOT AUTHORITY",
            })
    else:
        expected_downstream.update({
            "engineering_standards_authority_promotion": "DOWNSTREAM / NOT STARTED",
            "fp001_reconciliation": "REQUIRED / DOWNSTREAM / NOT PERFORMED",
            "communications": "REQUIRED / NOT_STARTED",
        })
    if state.get("completed_milestones") != expected_milestones:
        return False, "completed programme milestones are missing, duplicated, or changed"
    if any(state.get(key) != value for key, value in expected_downstream.items()):
        return False, "a downstream, blocked, or excluded HARDEN state changed"
    expected_conditionals = (
        {
            "privacy_consent": "NOT_REQUIRED",
            "content_media": "NOT_REQUIRED",
            "audit_evidence": (
                "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                if state.get("status_successor_version") in {"0.5.7", "0.5.8"}
                else "REQUIRED / NEXT / NOT_STARTED"
            ),
            "analytics": "NOT_REQUIRED",
        }
        if state.get("status_successor_version") in {"0.5.6", "0.5.7", "0.5.8"}
        else {
            "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "analytics": "NOT REQUIRED",
        }
    )
    if state.get("conditional_dossiers") != expected_conditionals:
        return False, "conditional dossier or Analytics state changed"

    expected_route = [
        "CERTIFIED HARDEN-02 EXECUTION",
        "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
        "CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
        "FP001_RECONCILIATION_REQUIRED",
        "CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
        "COMMUNICATIONS JIT DOMAIN DOSSIER",
        "CERTIFIED FP-001 COMMUNICATIONS v0.1.0 DOSSIER PROMOTION",
        "REMAINING REQUIRED / CONDITIONAL PHASE 7B",
        "PHASE 7C",
        "PROOF CLASSIFICATION",
        "PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
    ]
    if state.get("status_successor_version") in {"0.5.6", "0.5.7", "0.5.8"}:
        expected_route = [
            "CERTIFIED HARDEN-02 EXECUTION",
            "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
            "CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
            "FP001_RECONCILIATION_REQUIRED",
            "CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
            "COMMUNICATIONS JIT DOMAIN DOSSIER",
            "CERTIFIED FP-001 COMMUNICATIONS v0.1.0 DOSSIER PROMOTION",
            (
                (
                    "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
                    if state.get("status_successor_version") == "0.5.8"
                    else "AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE"
                )
                if state.get("status_successor_version") in {"0.5.7", "0.5.8"}
                else "FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER"
            ),
            "FP-001 PHASE 7B RECONCILIATION",
            "PHASE 7C",
            "PROOF CLASSIFICATION",
            "PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
        ]
    if state.get("downstream_route") != expected_route:
        return False, "the governed post-execution route changed"
    if state.get("status_successor_version") == "0.5.7":
        if (
            state.get("audit_dossier_execution_tracker_issue") != 116
            or state.get("audit_dossier_candidate") != "NOT_AUTHORED / NOT_CERTIFIED / NOT_CURRENT"
            or state.get("audit_dossier_work_start_baseline_main_sha") != "332d51f19d77430fe4e95911920fe0c87cab524a"
        ):
            return False, "Audit work-start tracker, baseline, or not-authored candidate state is missing"
    elif state.get("status_successor_version") == "0.5.8":
        if (
            state.get("audit_dossier_execution_tracker_issue") != 116
            or state.get("audit_dossier_candidate") != "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
            or state.get("audit_dossier_candidate_pr") != 118
            or state.get("audit_dossier_work_start_baseline_main_sha") != "332d51f19d77430fe4e95911920fe0c87cab524a"
        ):
            return False, "Audit candidate-review tracker, candidate status, or work-start provenance is missing"
    if execution == "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING":
        if state.get("execution_start_baseline_main_sha") != "1c8fc94058176795d88cb82e08857e3d30c553e9":
            return False, "HARDEN execution-start baseline main SHA is missing or incorrect"
    elif execution == "COMPLETE / CERTIFIED":
        if state.get("execution_start_baseline_main_sha") != "1c8fc94058176795d88cb82e08857e3d30c553e9":
            return False, "completed execution lost its execution-start provenance"
    elif "execution_start_baseline_main_sha" in state:
        return False, "not-started HARDEN state must not claim an execution-start baseline"

    if execution == "COMPLETE / CERTIFIED":
        cert = state.get("execution_certification")
        if not isinstance(cert, dict):
            return False, "complete execution certification evidence is missing"
        if cert != H02_COMPLETE_CERTIFICATION_FACTS:
            return False, "complete execution certification evidence is incomplete or contradictory"
        expected_base_sha = (
            "5f5a994e48d9458aaa6397044b3af4d72c5d5e81"
            if state.get("status_successor_version") == "0.5.8"
            else "332d51f19d77430fe4e95911920fe0c87cab524a"
            if state.get("status_successor_version") == "0.5.7"
            else "6036491dfbda0a311b8fcd0ddcdc3af5c3f11ac3"
            if state.get("status_successor_version") == "0.5.6"
            else "3f09bc91199e74d27645ebbb37d45c4831340952"
            if state.get("status_successor_version") == "0.5.5"
            else "3de114fef1961abebd3bfc9c057ef6366e14624f"
            if state.get("status_successor_version") == "0.5.4"
            else "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"
            else "0473cd69416f72fd94f2cee24a4d02c7f4fe0992"
            if state.get("status_successor_version") == "0.5.2"
            else "90f96ba3452c95112bf6ec4ce5bb897676adbed4"
            if state.get("status_successor_version") == "0.5.1"
            else "df6190a06bdc8aa4b99f6ed3a18cb9e3e12e22fb"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "d4e7390b71cdf61b649b534e1080102a044efe63"
        )
        if state.get("status_successor_base_sha") != expected_base_sha:
            return False, "completion status successor is not based on verified current main"
        if promotion_status == "COMPLETE / CERTIFIED":
            expected_fp001_certification = {
                "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/67",
                "candidate_sha": "79d0540c66f0224ece0330181e61dfef8ab4b458",
                "prior_main_sha": "38022caea64cb2522ab8fc4db730099a94cd6600",
                "resulting_main_sha": "4000ae50660930114e3ad43108dc029fd0673d32",
                "candidate_tree_sha": "a71dbeb2cca79bea0013f9997e40f34769f262f3",
                "exact_head_ci_run": "36991113390",
                "resulting_main_ci_run": "37009244020",
                "pre_merge_attestation_comment": "5952693308",
                "post_merge_attestation_comment": "5955641536",
                "post_merge_independent_review": "PASS",
            }
            if state.get("fp001_reconciliation_certification") != expected_fp001_certification:
                return False, "completed FP-001 reconciliation is missing or contradicts PR #67 certification evidence"
        promotion_route = (
            (
                "ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED",
                "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
                "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
                "IDENTITY v0.1.4 CURRENT-STATUS PROMOTION SOURCE: PR #77 STATUS SUCCESSOR; PR #76 CANDIDATE AND POST-MERGE CERTIFICATION EVIDENCE: COMPLETE",
            )
            if promotion_status == "COMPLETE / CERTIFIED"
            else (
                "ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
                "FP001_RECONCILIATION_REQUIRED: REQUIRED / DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION / NOT PERFORMED",
            )
        )
        communications_route = (
            "COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION"
        )
        adjudication_current = state.get("status_successor_version") in {"0.5.6", "0.5.7", "0.5.8"}
        audit_work_start_current = state.get("status_successor_version") in {"0.5.7", "0.5.8"}
        audit_candidate_review_current = state.get("status_successor_version") == "0.5.8"
        conditional_active_status = (
            (
                "- PRIVACY & CONSENT: NOT_REQUIRED",
                "- CONTENT & MEDIA: NOT_REQUIRED",
                "- AUDIT & EVIDENCE: " + (
                    "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                    if audit_work_start_current
                    else "REQUIRED / NEXT / NOT_STARTED"
                ),
                *(
                    (
                        "AUDIT DOSSIER CANDIDATE: " + (
                            "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
                            if audit_candidate_review_current
                            else "NOT AUTHORED / NOT CERTIFIED / NOT CURRENT"
                        ),
                    )
                    if audit_work_start_current
                    else ()
                ),
                "- ANALYTICS: NOT_REQUIRED",
                "PHASE 7C: BLOCKED / NOT_STARTED UNTIL AUDIT DOSSIER COMPLETE / CERTIFIED / CURRENT AND PHASE 7B RECONCILIATION SUCCEEDS",
                "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
            )
            if adjudication_current
            else (
                "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
                "PHASE 7C: BLOCKED / NOT_STARTED",
                "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
            )
        )
        required_active = promotion_route + (
            "PR #38: STALE / BLOCKED / NOT AUTHORITY",
            "PR #60: STALE HISTORICAL CANDIDATE / SUPERSEDED BY THIS SUCCESSOR / NOT MERGED / NOT AUTHORITY",
            *conditional_active_status,
            "PROOF CLASSIFICATION: NOT FINALISED",
            "STORE / CER: EXCLUDED FROM HARDEN-02",
        )
        if any(active.count(line) != 1 for line in required_active):
            return False, "Open Work omits a required completion or downstream boundary"
        if audit_work_start_current and (
            "AUDIT DOSSIER EXECUTION TRACKER: #116" not in active
            or "AUDIT DOSSIER WORK-START BASELINE MAIN SHA: `332d51f19d77430fe4e95911920fe0c87cab524a`" not in active
        ):
            return False, "Open Work omits the Audit work-start tracker or baseline"
        if active.count(communications_route) != 1 or active.count("- COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0") != 1:
            return False, "Open Work Communications summary and required-dossier route disagree or are duplicated"
    else:
        required_active = (
            "ENGINEERING STANDARDS AUTHORITY PROMOTION: DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED",
            "FP001_RECONCILIATION_REQUIRED: REQUIRED / DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION / NOT PERFORMED",
            "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION",
            "PR #38: STALE / BLOCKED / NOT AUTHORITY",
            "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
            "PHASE 7C: BLOCKED / NOT_STARTED",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
            "STORE / CER: EXCLUDED FROM HARDEN-02",
        )
        if any(active.count(line) != 1 for line in required_active):
            return False, "Open Work omits a required downstream boundary"

    readme_start = readme.find("## Current State")
    if readme_start < 0:
        return False, "README current-state section is missing"
    readme_current = readme[readme_start:]
    readme_status = "- " + expected["readme"]
    if readme_current.count(readme_status) != 1:
        return False, "README execution status is missing, duplicated, or contradictory"
    stale_current_routes = (
        "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
        "NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED",
        "HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
        "HARDEN-02 EXECUTION: NEXT / AUTHORISED / NOT STARTED",
    )
    if any(line in readme_current for line in stale_current_routes):
        return False, "README retains a contradictory current HARDEN route"
    if adjudication_current:
        conditional_readme = (
            "- PRIVACY & CONSENT DOSSIER: NOT_REQUIRED",
            "- CONTENT & MEDIA DOSSIER: NOT_REQUIRED",
            "- AUDIT & EVIDENCE DOSSIER: " + (
                "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                if audit_work_start_current
                else "REQUIRED / NEXT / NOT_STARTED"
            ),
            *(
                (
                    "- AUDIT DOSSIER CANDIDATE: " + (
                        "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
                        if audit_candidate_review_current
                        else "NOT_AUTHORED / NOT_CERTIFIED / NOT_CURRENT"
                    ),
                )
                if audit_work_start_current
                else ()
            ),
            "- ANALYTICS DOSSIER: NOT_REQUIRED",
            "- PHASE 7C: BLOCKED / NOT_STARTED until Audit dossier is COMPLETE / CERTIFIED / CURRENT and Phase 7B reconciliation succeeds.",
        )
    else:
        conditional_readme = (
            "- PRIVACY & CONSENT DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "- CONTENT & MEDIA DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "- AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "- ANALYTICS DOSSIER: NOT REQUIRED",
            "- PHASE 7C: BLOCKED / NOT_STARTED pending explicit conditional-dossier dispositions.",
        )
    required_readme = (
        "- CURRENT AUTHORITY-STAGE PROGRAMME: " + expected["current_stage"],
        "- NEXT STAGE: " + expected["next_stage"],
        "- IDENTITY v0.1.4: CERTIFIED / CURRENT under the separate PR #77 status successor; PR #76 candidate and post-merge certification evidence are COMPLETE",
        "- COMMUNICATIONS FINALISATION: BLOCKED / STOP",
        "- ENGINEERING STANDARDS AUTHORITY PROMOTION: " + (
            "COMPLETE / CERTIFIED"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "NEXT / AUTHORISED / NOT STARTED"
            if execution == "COMPLETE / CERTIFIED"
            else "DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED"
        ),
        *conditional_readme,
        "- PROOF CLASSIFICATION: NOT FINALISED",
        (
            "- EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED"
            if audit_work_start_current
            else "- EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS"
        ),
    )
    if any(readme_current.count(line) != 1 for line in required_readme):
        return False, "README current route or downstream status is missing or contradictory"
    communications_status = (
        "- COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0"
        if promotion_status == "COMPLETE / CERTIFIED"
        else "- COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION"
        if execution == "COMPLETE / CERTIFIED"
        else "- COMMUNICATIONS DOSSIER: REQUIRED / NOT_STARTED"
    )
    if readme_current.count(communications_status) != 1:
        return False, "README Communications status or downstream route is missing or contradictory"
    if execution == "COMPLETE / CERTIFIED":
        required_completed_readme = (
            "- FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "- FP001_RECONCILIATION_REQUIRED: REQUIRED / NEXT / NOT PERFORMED",
            "- ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "- ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
        )
        if any(readme_current.count(line) != 1 for line in required_completed_readme):
            return False, "README completed HARDEN route or FP-001 gate is missing or contradictory"
    if "Store/CER remains excluded from HARDEN-02." not in readme_current:
        return False, "README does not preserve the Store/CER exclusion"

    if execution == "COMPLETE / CERTIFIED":
        if not contract:
            return False, "current HARDEN status successor is missing from lifecycle validation"
        version_header = contract.split("## 1. Objective", 1)[0]
        expected_harden_version = "0.5.8" if audit_candidate_review_current else "0.5.7" if audit_work_start_current else "0.5.6" if adjudication_current else "0.5.5" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"
        version_marker = "**Plan / contract version:** " + chr(96) + f"v{expected_harden_version}" + chr(96)
        if version_marker not in version_header:
            return False, "current HARDEN status successor version is missing or unsupported"
        contract_current_start = contract.rfind("## 20. Contract-stage STOP")
        if contract_current_start < 0:
            return False, "current HARDEN status successor has no current STOP section"
        contract_current = contract[contract_current_start:]
        required_contract = (
            "HARDEN-02 execution is COMPLETE / CERTIFIED",
            "PASS WITH NON-BLOCKING CORRECTIONS",
            "36565948391",
            "36567933267",
            "36856102830",
            "110348834922",
            "611abef74ce306eba824f44241189413c6be0c305c922166f3a338cc7f019b83",
            "PR #67",
            "79d0540c66f0224ece0330181e61dfef8ab4b458",
            "37009244020",
            "5955641536",
        )
        if any(value not in contract_current for value in required_contract):
            return False, "current HARDEN contract completion evidence or next route is incomplete"
        expected_promotion_contract_status = (
            "Engineering Standards Authority Promotion is COMPLETE / CERTIFIED"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "Engineering Standards Authority Promotion NEXT / AUTHORISED / NOT STARTED"
        )
        if expected_promotion_contract_status not in contract_current:
            return False, "current HARDEN contract Standards promotion status is missing or contradictory"
        if "Current HARDEN-02 execution is IN PROGRESS" in contract_current:
            return False, "current HARDEN contract retains an active pre-completion route"
        route_start = contract_current.find("## 21. Current execution certification and next stage")
        if route_start < 0:
            return False, "current HARDEN contract has no explicit completion route section"
        current_route = contract_current[route_start:]
        required_route = (
            (
                "HARDEN-02 execution, Engineering Standards Authority Promotion, FP-001 PMR reconciliation and Identity dossier v0.1.4 are COMPLETE / CERTIFIED",
                "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
                "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
                "IDENTITY v0.1.4 CURRENT-STATUS PROMOTION SOURCE: PR #77 STATUS SUCCESSOR; PR #76 CANDIDATE AND POST-MERGE CERTIFICATION EVIDENCE: COMPLETE",
                "Communications JIT Domain Dossier v0.1.0 is COMPLETE / CERTIFIED / CURRENT under the separate PR #81 status successor",
                "Communications finalisation remains BLOCKED / STOP pending applicable release gates"
                if adjudication_current
                else "Communications finalisation remains BLOCKED / STOP pending applicable gates and conditional-dossier adjudication",
            )
            if promotion_status == "COMPLETE / CERTIFIED"
            else (
                "HARDEN-02 execution is COMPLETE / CERTIFIED",
                "immediate next stage is ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
                "Engineering Standards Authority Promotion NEXT / AUTHORISED / NOT STARTED",
            )
        )
        if any(current_route.count(value) != 1 for value in required_route):
            return False, "current HARDEN contract completion route is missing or duplicated"
        if adjudication_current:
            adjudication_route = (
                "PRIVACY & CONSENT DOSSIER: NOT_REQUIRED",
                "CONTENT & MEDIA DOSSIER: NOT_REQUIRED",
                "AUDIT & EVIDENCE DOSSIER: " + (
                    "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                    if audit_work_start_current
                    else "REQUIRED / NEXT / NOT_STARTED"
                ),
                *(
                    (
                        "AUDIT DOSSIER CANDIDATE: " + (
                            "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
                            if audit_candidate_review_current
                            else "NOT_AUTHORED / NOT_CERTIFIED / NOT_CURRENT"
                        ),
                    )
                    if audit_work_start_current
                    else ()
                ),
                "PHASE 7C: BLOCKED / NOT_STARTED UNTIL AUDIT DOSSIER COMPLETE / CERTIFIED / CURRENT AND PHASE 7B RECONCILIATION SUCCEEDS",
                "PROOF CLASSIFICATION: NOT FINALISED",
                (
                    "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED"
                    if audit_work_start_current
                    else "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS"
                ),
            )
            if any(value not in current_route for value in adjudication_route):
                return False, "current HARDEN contract does not preserve the adjudicated dossier and Phase 7C block"
            communications_to_audit = (
                "→ CERTIFIED FP-001 COMMUNICATIONS v0.1.0 DOSSIER PROMOTION\n"
                + (
                    (
                        "→ FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
                        if audit_candidate_review_current
                        else "→ AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE"
                    )
                    if audit_work_start_current
                    else "→ FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER"
                )
            )
            if communications_to_audit not in current_route:
                return False, "current HARDEN contract skips the Audit dossier after Communications promotion"
        contradictory_route = (
            "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
            "NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED",
            "HARDEN-02 execution is IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
            "Engineering Standards Authority Promotion is DOWNSTREAM / NOT STARTED",
        )
        if any(value in current_route for value in contradictory_route):
            return False, "current HARDEN contract retains a contradictory execution or downstream route"

    return True, (
        "HARDEN-02 execution completion and downstream route are coherent"
        if execution == "COMPLETE / CERTIFIED"
        else "HARDEN-02 preserves the certified v0.4.0 lifecycle and one coherent permitted execution state"
    )


def _h02_phase7c_candidate_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate the v0.5.13 status-only route with Phase 7C still a candidate."""

    expected = {
        "status_successor_version": "0.5.13",
        "status_successor_base_sha": "1a51755d505279821afe166b030be735fe0b6a1c",
        "current_stage": "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
        "next_stage": "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE",
        "harden_02_execution": "COMPLETE / CERTIFIED",
        "harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY",
        "engineering_standards_authority_promotion": "COMPLETE / CERTIFIED",
        "store_cer": "EXCLUDED",
        "audit_dossier": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c": "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "OPEN",
        "phase_7c_contract_candidate": {
            "path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
            "version": "0.1.0",
            "lifecycle": "CANDIDATE / NOT CERTIFIED / NOT CURRENT",
            "authored": True,
            "certification": "PENDING",
            "current_status_promotion": "PENDING",
        },
        "phase_7b_reconciliation_execution_tracker_issue": 120,
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
        "programme_router_issue_111_state": "OPEN",
        "proof_classification": "NOT FINALISED",
        "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.11.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.13.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.13.md",
        "audit_dossier_execution_tracker_issue": 116,
        "audit_dossier_candidate_pr": 118,
        "audit_dossier_work_start_baseline_main_sha": "332d51f19d77430fe4e95911920fe0c87cab524a",
        "audit_current_status_promotion": "PR #119 STATUS SUCCESSOR",
        "audit_certified_candidate_sha256": "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea",
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "HARDEN .5.13 current state omits the Phase 7C candidate lifecycle or alters a protected gate"
    if state.get("conditional_dossiers") != {
        "privacy_consent": "NOT_REQUIRED",
        "content_media": "NOT_REQUIRED",
        "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "analytics": "NOT_REQUIRED",
    }:
        return False, "HARDEN .5.13 conditional dossier dispositions changed"
    expected_milestones = [
        "TARGETED PRODUCT AMENDMENT PROGRAMME",
        "FP-001 PHASE 7A",
        "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
        "HARDEN-02 EXECUTION",
        "ENGINEERING STANDARDS AUTHORITY PROMOTION",
        "FP-001 PMR RECONCILIATION",
        "FP-001 IDENTITY v0.1.3 DURABLE-DELIVERY PATCH PROMOTION",
        "FP-001 IDENTITY v0.1.4 GOVERNANCE-CORRECTION PATCH PROMOTION",
        "FP-001 COMMUNICATIONS v0.1.0 JIT DOMAIN DOSSIER PROMOTION",
        "FP-001 PHASE 7A/7B CONDITIONAL-DOSSIER ADJUDICATION",
        "FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION",
    ]
    if state.get("completed_milestones") != expected_milestones:
        return False, "HARDEN .5.13 completed milestones omit a certified prerequisite or advance a later stage"
    if state.get("execution_certification") != H02_COMPLETE_CERTIFICATION_FACTS:
        return False, "HARDEN .5.13 lost certified HARDEN-02 execution lifecycle evidence"
    if state.get("phase_7b_reconciliation_candidate") != {
        "path": "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
        "current_status_successor_path": "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
        "version": "0.1.0",
        "result": "PASS / READY FOR INDEPENDENT REVIEW",
        "lifecycle": "CERTIFIED / CURRENT",
        "certification": "COMPLETE; EXACT CANDIDATE MERGED UNCHANGED; RESULTING-MAIN VERIFIED",
        "tracker_issue": 120,
    }:
        return False, "HARDEN .5.13 does not preserve the immutable Phase 7B candidate/current-successor distinction"
    expected_route = [
        "FP-001 PHASE 7A: COMPLETE",
        "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
        "FP-001 PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C FINAL FEATURE PACK CONTRACT: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: CANDIDATE / NOT CERTIFIED / NOT CURRENT",
        "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE",
        "SEPARATE CERTIFICATION AND CURRENT-STATUS PROMOTION",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
    ]
    if state.get("downstream_route") != expected_route:
        return False, "HARDEN .5.13 downstream route skips candidate review or advances proof/Phase 8"

    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    active_lines = (
        "CURRENT AUTHORITY-STAGE PROGRAMME: FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
        "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        "PHASE 7C TRACKER #124: OPEN",
        "PHASE 7C CONTRACT CANDIDATE: working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md; CANDIDATE / NOT CERTIFIED / NOT CURRENT",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
    )
    if any(len(re.findall(r"(?m)^" + re.escape(line) + r"\s*$", active_summary)) != 1 for line in active_lines):
        return False, "Open Work .5.13 active route omits or duplicates a candidate-only lifecycle boundary"
    if "PHASE 7B TRACKER #120: CLOSED / COMPLETED (HISTORICAL)" not in active_summary or "#111 remains the open programme router" not in active_summary:
        return False, "Open Work .5.13 does not keep #120 historical and #111 open"
    if re.search(r"(?im)^.*PHASE 7C\s*:\s*(?:COMPLETE|CERTIFIED|CURRENT|AUTHORI[ZS]ED).*$", active_summary):
        return False, "Open Work .5.13 completes or authorises Phase 7C"
    if re.search(r"(?im)^.*PROOF CLASSIFICATION\s*:\s*(?:FINAL|FINALI[ZS]ED|CERTIFIED|REUSE_EXISTING_PROOF|NEW_TRACER_BULLET).*$", active_summary):
        return False, "Open Work .5.13 finalises proof classification"
    if re.search(r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$", active_summary):
        return False, "Open Work .5.13 authorises Phase 8 or application implementation"

    readme_current = _markdown_h2_section(readme, "Current State") or ""
    if any(line not in readme_current for line in active_lines[1:]):
        return False, "README current state does not mirror the candidate-only Phase 7C lifecycle"
    route_start = contract.find("## 21. Current execution certification and next stage")
    route_end = contract.find("## 22.", route_start + 1)
    route = contract[route_start:route_end] if route_start >= 0 and route_end > route_start else ""
    route_lines = (
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE; STATUS: PENDING",
        "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        "PHASE 7C TRACKER #124: OPEN",
        "FINAL FEATURE PACK CONTRACT v0.1.0: CANDIDATE / NOT CERTIFIED / NOT CURRENT",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
    )
    if not route or any(line not in route for line in route_lines):
        return False, "HARDEN .5.13 current route omits the candidate review stop or downstream gate"
    if "## 23. FP-001 Phase 7B reconciliation current route" not in contract or "PHASE 7C EXECUTION/CONTROL TRACKER: #124 OPEN" not in contract:
        return False, "HARDEN .5.13 Phase 7B current route omits Phase 7C tracker #124"
    return True, "Phase 7B remains certified/current; Phase 7C candidate awaits independent review and all later gates remain closed"


def _h02_phase7c_current_status_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate the current Phase 7C closure route and downstream gates."""

    expected = {
        "status_successor_version": "0.5.16",
        "status_successor_base_sha": "5b56d4070b422bf969667e84faae973522b52414",
        "current_stage": "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
        "next_stage": "ARCHITECTURAL PROOF CLASSIFICATION",
        "harden_02_execution": "COMPLETE / CERTIFIED",
        "harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY",
        "engineering_standards_authority_promotion": "COMPLETE / CERTIFIED",
        "store_cer": "EXCLUDED",
        "audit_dossier": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation_execution_tracker_issue": 120,
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
        "programme_router_issue_111_state": "OPEN",
        "proof_classification": "NOT FINALISED",
        "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PROOF CLASSIFICATION AND ALL DEVELOPMENT ENTRY HARD STOP CONDITIONS PASS",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.14.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.16.md",
        "audit_dossier_execution_tracker_issue": 116,
        "audit_dossier_candidate_pr": 118,
        "audit_dossier_work_start_baseline_main_sha": "332d51f19d77430fe4e95911920fe0c87cab524a",
        "audit_current_status_promotion": "PR #119 STATUS SUCCESSOR",
        "audit_certified_candidate_sha256": "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea",
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "HARDEN .5.16 current state omits certification evidence or advances a protected gate"
    if state.get("conditional_dossiers") != {
        "privacy_consent": "NOT_REQUIRED",
        "content_media": "NOT_REQUIRED",
        "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "analytics": "NOT_REQUIRED",
    }:
        return False, "HARDEN .5.15 conditional dossier dispositions changed"
    if state.get("execution_certification") != H02_COMPLETE_CERTIFICATION_FACTS:
        return False, "HARDEN .5.15 lost certified execution lifecycle evidence"
    phase7c = state.get("phase_7c_final_feature_pack_contract")
    expected_phase7c = {
        "path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "version": "0.1.0",
        "lifecycle": "COMPLETE / CERTIFIED / CURRENT",
        "candidate_archive_path": "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "candidate_archive_sha256": "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
        "pr126_reviewed_head_sha": "e7d5d3908bedf1a75c6627448c3ed0c067b076f8",
        "pr126_merge_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "pr126_merge_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_exact_head_fia_run": 39141076412,
        "resulting_main_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "resulting_main_fia_run": 39143147487,
        "resulting_main_fia_status": "completed",
        "resulting_main_fia_conclusion": "success",
        "resulting_main_fia_tests": 455,
        "resulting_main_fia_assertions": 728,
        "resulting_main_fia_findings": 0,
        "fresh_resulting_main_verification": "PASS",
        "proof_classification": "NOT FINALISED",
        "phase8": "UNAUTHORISED",
    }
    if not isinstance(phase7c, dict) or any(phase7c.get(key) != value for key, value in expected_phase7c.items()):
        return False, "HARDEN .5.16 current state omits resulting-main provenance or advances a protected gate"
    if state.get("completed_milestones", [])[-1:] != [
        "PR #126 resulting-main verification and Phase 7C tracker #124 closure COMPLETE"
    ]:
        return False, "HARDEN .5.15 milestones omit PR #126 resulting-main verification or tracker closure"
    if state.get("downstream_route") != [
        "FP-001 PHASE 7A: COMPLETE",
        "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
        "FP-001 PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "ARCHITECTURAL PROOF CLASSIFICATION: NEXT / NOT PERFORMED",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
    ]:
        return False, "HARDEN .5.16 downstream route skips tracker closure or advances a later gate"

    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    active_lines = (
        "CURRENT AUTHORITY-STAGE PROGRAMME: FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
        "NEXT STAGE: ARCHITECTURAL PROOF CLASSIFICATION",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "ARCHITECTURAL PROOF CLASSIFICATION: NEXT / NOT PERFORMED",
        "PROOF CLASSIFICATION: NOT FINALISED; NO REUSE OR NEW TRACER BULLET SELECTION HAS BEEN MADE",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
    )
    if any(len(re.findall(r"(?m)^" + re.escape(line) + r"\s*$", active_summary)) != 1 for line in active_lines):
        return False, "Open Work .5.16 active route omits or duplicates a lifecycle boundary"
    if "PROGRAMME ROUTER #111: OPEN" not in active_summary:
        return False, "Open Work .5.15 changes programme router #111 state"
    if re.search(r"(?im)^.*PROOF CLASSIFICATION\s*:\s*(?:FINAL|FINALI[ZS]ED|REUSE_EXISTING_PROOF|NEW_TRACER_BULLET).*$", active_summary):
        return False, "Open Work .5.15 selects or finalises proof classification"
    if re.search(r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$", active_summary):
        return False, "Open Work .5.15 authorises Phase 8 or implementation"

    readme_current = _markdown_h2_section(readme, "Current State") or ""
    for line in (
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "ARCHITECTURAL PROOF CLASSIFICATION: NEXT / NOT PERFORMED",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
    ):
        if line not in readme_current:
            return False, "README current state does not mirror the closed Phase 7C route"
    if re.search(r"(?im)^.*#124[^\n]{0,120}\bOPEN\b.*$", readme_current):
        return False, "README current state projects issue #124 as OPEN"

    route_start = contract.find("## 21. Current execution certification and next stage")
    route_end = contract.find("## 22.", route_start + 1)
    route = contract[route_start:route_end] if route_start >= 0 and route_end > route_start else ""
    route_lines = (
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "NEXT STAGE: ARCHITECTURAL PROOF CLASSIFICATION; STATUS: NEXT / NOT PERFORMED",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
    )
    if not route or any(line not in route for line in route_lines):
        return False, "HARDEN .5.16 current route omits certification evidence or a downstream stop"
    return True, "Phase 7C closure is current; proof classification and Phase 8 remain gated"


def _h02_fp001_classification_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate classification completion without turning it into Phase 8 authority."""

    expected = {
        "status_successor_version": "1.2.73",
        "status_successor_base_sha": "24a9ad925ee1ab6d75ddb44bae6df0b4f3d09bca",
        "current_stage": "FP-001 DEVELOPMENT ENTRY HARD STOP EVALUATION",
        "next_stage": "DEVELOPMENT ENTRY HARD STOP EVALUATION",
        "harden_02_execution": "COMPLETE / CERTIFIED",
        "harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY",
        "engineering_standards_authority_promotion": "COMPLETE / CERTIFIED",
        "store_cer": "EXCLUDED",
        "audit_dossier": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation_execution_tracker_issue": 120,
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
        "programme_router_issue_111_state": "OPEN",
        "proof_classification": "NEW_TRACER_BULLET",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "phase8": "UNAUTHORISED",
        "application_implementation": "UNAUTHORISED / BLOCKED UNTIL ALL DEVELOPMENT ENTRY HARD STOP CONDITIONS PASS",
        "development_entry_hard_stop_condition_9": "SATISFIED",
        "remaining_development_entry_hard_stop_conditions": "NOT EVALUATED / MUST PASS BEFORE PHASE 8",
        "next_governance_action": "DEVELOPMENT ENTRY HARD STOP EVALUATION",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.15.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.17.md",
        "audit_dossier_execution_tracker_issue": 116,
        "audit_dossier_candidate_pr": 118,
        "audit_dossier_work_start_baseline_main_sha": "332d51f19d77430fe4e95911920fe0c87cab524a",
        "audit_current_status_promotion": "PR #119 STATUS SUCCESSOR",
        "audit_certified_candidate_sha256": "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea",
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "FP-001 classification state is incomplete, selects reuse, or advances Phase 8"
    if state.get("phase_7c_final_feature_pack_contract", {}).get("classification_authority_event") != "SEPARATE OPEN WORK POST-PHASE-7C STATUS DECISION":
        return False, "Final Feature Pack Contract is incorrectly represented as the classification authority"
    if state.get("conditional_dossiers") != {
        "privacy_consent": "NOT_REQUIRED",
        "content_media": "NOT_REQUIRED",
        "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "analytics": "NOT_REQUIRED",
    }:
        return False, "classification successor changes a protected conditional dossier disposition"
    if state.get("execution_certification") != H02_COMPLETE_CERTIFICATION_FACTS:
        return False, "classification successor changes certified HARDEN-02 execution evidence"
    if state.get("completed_milestones", [])[-1:] != [
        "PR #126 resulting-main verification and Phase 7C tracker #124 closure COMPLETE"
    ]:
        return False, "classification successor omits PR #126 resulting-main verification or tracker closure"
    phase7c = state.get("phase_7c_final_feature_pack_contract")
    expected_phase7c = {
        "path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "version": "0.1.0",
        "lifecycle": "COMPLETE / CERTIFIED / CURRENT",
        "candidate_archive_path": "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "candidate_archive_sha256": "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
        "pr126_reviewed_head_sha": "e7d5d3908bedf1a75c6627448c3ed0c067b076f8",
        "pr126_merge_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "pr126_merge_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_exact_head_fia_run": 39141076412,
        "resulting_main_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "resulting_main_fia_run": 39143147487,
        "resulting_main_fia_status": "completed",
        "resulting_main_fia_conclusion": "success",
        "resulting_main_fia_tests": 455,
        "resulting_main_fia_assertions": 728,
        "resulting_main_fia_findings": 0,
        "fresh_resulting_main_verification": "PASS",
        "proof_classification": "NEW_TRACER_BULLET",
        "phase8": "UNAUTHORISED",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "classification_authority_event": "SEPARATE OPEN WORK POST-PHASE-7C STATUS DECISION",
    }
    if not isinstance(phase7c, dict) or any(
        phase7c.get(key) != value for key, value in expected_phase7c.items()
    ):
        return False, "classification successor changes certified Final Feature Pack Contract or PR #126 provenance"
    if state.get("downstream_route") != [
        "FP-001 PHASE 7A: COMPLETE",
        "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
        "FP-001 PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "ISSUE #124: CLOSED / COMPLETED",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET: REQUIRED / NOT YET DEFINED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "DEVELOPMENT ENTRY HARD STOP CONDITION 9: SATISFIED",
        "REMAINING DEVELOPMENT ENTRY HARD STOP CONDITIONS: NOT EVALUATED / MUST PASS BEFORE PHASE 8",
        "PHASE 8: UNAUTHORISED",
        "APPLICATION IMPLEMENTATION: UNAUTHORISED",
    ]:
        return False, "FP-001 downstream route skips remaining Development Entry Hard Stop evaluation"

    active_lines = (
        "CURRENT AUTHORITY-STAGE PROGRAMME: FP-001 DEVELOPMENT ENTRY HARD STOP EVALUATION",
        "NEXT STAGE: DEVELOPMENT ENTRY HARD STOP EVALUATION",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET: REQUIRED / NOT YET DEFINED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "DEVELOPMENT ENTRY HARD STOP CONDITION 9: SATISFIED",
        "REMAINING DEVELOPMENT ENTRY HARD STOP CONDITIONS: NOT EVALUATED / MUST PASS BEFORE PHASE 8",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9; ALL OTHER APPLICABLE CONDITIONS REQUIRE INDEPENDENT EVALUATION",
        "OPEN GATES: OQ-035 SECURITY / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY; OQ-036 VENDOR / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY",
    )
    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    if any(line not in active_summary for line in active_lines):
        return False, "Open Work active route omits classification, condition 9 or the remaining hard stop"
    if "PROGRAMME ROUTER #111: OPEN" not in active_summary or "PHASE 8: UNAUTHORISED" not in active_summary:
        return False, "Open Work closes programme router #111 or authorises Phase 8"
    if "OQ-035" not in active_summary or "OQ-036" not in active_summary:
        return False, "Open Work omits unresolved expert/provider gates"
    if re.search(r"(?im)^\s*REUSE_EXISTING_PROOF\s*:\s*SELECTED\b", active_summary):
        return False, "Open Work selects REUSE_EXISTING_PROOF"
    if re.search(r"\bTB-\d{3,}\b", active_summary):
        return False, "Open Work introduces a Tracer Bullet identifier"
    if re.search(r"(?im)^.*(?:PHASE 8|APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$", active_summary):
        return False, "Open Work authorises Phase 8 or application implementation"

    current_state = _markdown_h2_section(readme, "Current State") or ""
    for token in active_lines[2:-1]:
        if token not in current_state:
            return False, "README current state does not mirror the classification status"
    if "PROGRAMME ROUTER #111: OPEN" not in current_state or "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED" not in current_state:
        return False, "README current state closes the programme router or authorises implementation"
    contract_current = _markdown_h2_section(
        contract,
        "25. FP-001 architectural proof classification current status",
    ) or ""
    contract_current_lines = (
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET: REQUIRED / NOT YET DEFINED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "DEVELOPMENT ENTRY HARD STOP CONDITION 9: SATISFIED",
        "REMAINING DEVELOPMENT ENTRY HARD STOP CONDITIONS: NOT EVALUATED / MUST PASS BEFORE PHASE 8",
        "PHASE 8: UNAUTHORISED",
        "APPLICATION IMPLEMENTATION: UNAUTHORISED",
        "NEXT GOVERNANCE ACTION: DEVELOPMENT ENTRY HARD STOP EVALUATION",
        "Classification satisfies only Development Entry Hard Stop condition 9.",
        "until every other applicable condition is independently evaluated and satisfied.",
        "OQ-035, OQ-036 and other expert, provider, release-only and future gates retain their existing status.",
    )
    if any(line not in contract_current for line in contract_current_lines):
        return False, "Current HARDEN-02 status omits classification or the remaining Development Entry Hard Stop"
    if re.search(r"(?im)^\s*REUSE_EXISTING_PROOF\s*:\s*SELECTED\b", contract_current):
        return False, "Current HARDEN-02 status selects REUSE_EXISTING_PROOF"
    if re.search(r"\bTB-\d{3,}\b", contract_current):
        return False, "Current HARDEN-02 status introduces a Tracer Bullet identifier"
    return True, "classification satisfies only condition 9; Development Entry Hard Stop evaluation remains next and Phase 8 stays unauthorised"


def _h02_fp001_hard_stop_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate Development Entry Hard Stop PASS and bounded Phase 8 authorisation."""

    expected = {
        "status_successor_version": "1.2.74",
        "status_successor_base_sha": "675a8c50ac53a995a48e4d262df42065f8ccd412",
        "current_stage": "FP-001 PHASE 8 ARCHITECTURAL PROOF (BOUNDED)",
        "next_stage": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "proof_classification": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "programme_router_issue_111_state": "OPEN",
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "FP-001 hard-stop state is incomplete, reverts authorisation, or changes proof classification"
    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    for token in (
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
        "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
    ):
        if token not in active_summary:
            return False, f"Open Work active route omits hard-stop state {token!r}"
    if re.search(r"\bTB-\d{3,}\b", active_summary):
        return False, "Open Work introduces a Tracer Bullet identifier"
    current_state = _markdown_h2_section(readme, "Current State") or ""
    for token in (
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
    ):
        if token not in current_state:
            return False, "README current state does not mirror the hard-stop promotion"
    return True, "Development Entry Hard Stop PASS authorises bounded Phase 8 Architectural Proof only"


def _h02_fp001_phase8_contract_candidate_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate the first governed Phase 8 proof-contract candidate state."""

    expected = {
        "status_successor_version": "1.2.77",
        "status_successor_base_sha": "0972864ef7f4638c96198e19a13977e0151e9726",
        "current_stage": "FP-001 PHASE 8 ARCHITECTURAL PROOF (BOUNDED)",
        "next_stage": "TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "proof_classification": "NEW_TRACER_BULLET",
        "tracer_bullet": "REQUIRED / DEFINED AS REVIEW CANDIDATE",
        "tracer_bullet_id": "TB-001",
        "proof_design": "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "architectural_proof_execution": "NOT STARTED",
        "proof_result": "NOT STARTED",
        "proof_certification": "NOT STARTED",
        "proof_contract_path": "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md",
        "proof_contract_lifecycle": "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        "next_governance_action": "TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.19.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md",
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "FP-001 TB-001 candidate state is incomplete or advances proof execution"
    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    for token in (
        "TB-001 CONTRACT LIFECYCLE: CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
    ):
        if token not in active_summary:
            return False, f"Open Work active route omits TB-001 lifecycle state {token!r}"
    if re.search(r"(?im)^\s*PHASE 9(?: / VERTICAL SLICES)?\s*:\s*(?:AUTHORI[ZS]ED|STARTED|IN PROGRESS|COMPLETE)", active_summary):
        return False, "Open Work advances Phase 9 or Vertical Slices"
    if re.search(r"(?im)^\s*PROOF (?:EXECUTION|RESULT|CERTIFICATION)\s*:\s*(?:PASS|COMPLETE|CERTIFIED)", active_summary):
        return False, "Open Work claims proof execution, result or certification"
    current_state = _markdown_h2_section(readme, "Current State") or ""
    for token in (
        "TB-001 is CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
    ):
        if token not in current_state:
            return False, "README current state does not mirror the TB-001 review lifecycle"
    route = _markdown_h2_section(contract, "v0.5.21 — FP-001 TB-001 proof-contract successor candidate route (current)") or ""
    if any(token not in route for token in (
        "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
    )):
        return False, "current HARDEN-02 route omits the TB-001 candidate boundary"
    return True, "TB-001 remains a review candidate; proof execution and Phase 9 remain unstarted"


def _h02_fp001_phase8_contract_approved_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate the approved contract route while keeping proof execution separate."""

    expected = {
        "status_successor_version": "1.2.78",
        "status_successor_base_sha": "4234965c8da20dbb4ef0a7128614a5070244619a",
        "current_stage": "FP-001 PHASE 8 ARCHITECTURAL PROOF (BOUNDED)",
        "next_stage": "WELL-38 — Transition Foundation Integrity to implementation-era CI",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation_execution_tracker_issue": 120,
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "proof_classification": "NEW_TRACER_BULLET",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / DEFINED",
        "tracer_bullet_id": "TB-001",
        "proof_design": "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "architectural_proof_execution": "NOT STARTED",
        "proof_result": "NOT STARTED",
        "proof_certification": "NOT STARTED",
        "proof_contract_path": "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md",
        "proof_contract_lifecycle": "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        "next_governance_action": "WELL-38 — Transition Foundation Integrity to implementation-era CI",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.20.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.22.md",
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "approved TB-001 status successor is incomplete or advances proof/Phase 9"
    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    required_active = (
        "CONTRACT/DESIGN REVIEW: COMPLETE / PASS",
        "TB-001 CONTRACT LIFECYCLE: CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "NEXT GOVERNANCE ACTION: WELL-38 — Transition Foundation Integrity to implementation-era CI",
    )
    if any(token not in active_summary for token in required_active):
        return False, "Open Work active route omits the approved-contract state or proof execution stop"
    if re.search(r"(?im)^\s*PHASE 9(?: / VERTICAL SLICES)?\s*:\s*(?:AUTHORI[ZS]ED|STARTED|IN PROGRESS|COMPLETE)", active_summary):
        return False, "Open Work advances Phase 9 or Vertical Slices"
    if re.search(r"(?im)^\s*PROOF (?:EXECUTION|RESULT|CERTIFICATION)\s*:\s*(?:PASS|COMPLETE|CERTIFIED)", active_summary):
        return False, "Open Work claims proof execution, result or certification"

    readme_current = _markdown_h2_section(readme, "Current State") or ""
    for token in required_active:
        if token not in readme_current:
            return False, "README current state does not mirror the approved-contract lifecycle"
    route = _markdown_h2_section(
        contract,
        "v0.5.22 — FP-001 TB-001 approved contract route (current)",
    ) or ""
    for token in (
        "TB-001 CONTRACT/DESIGN REVIEW: COMPLETE / PASS",
        "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "NEXT GOVERNANCE ACTION: WELL-38 — Transition Foundation Integrity to implementation-era CI",
    ):
        if token not in route:
            return False, "current HARDEN-02 route omits the approved-contract boundary"
    return True, "TB-001 is approved for bounded Phase 8 proof execution; proof execution and Phase 9 remain unstarted"


def _h02_fp001_phase8_proof_execution_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate the started proof route without claiming a complete TB-001 result."""

    expected = {
        "current_stage": "FP-001 PHASE 8 ARCHITECTURAL PROOF (BOUNDED)",
        "next_stage": _P8_05_NEXT_STAGE_AUTHORISED,
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "proof_classification": "NEW_TRACER_BULLET",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / DEFINED",
        "tracer_bullet_id": "TB-001",
        "proof_design": "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "architectural_proof_execution": "STARTED",
        "proof_result": "INCOMPLETE / COVERAGE-INCOMPLETE",
        "proof_certification": "NOT CERTIFIED",
        "proof_contract_path": "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md",
        "proof_contract_lifecycle": "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "phase8": "AUTHORISED",
        "application_implementation": _P8_05_BOUNDED_APPLICATION_IMPLEMENTATION,
        "phase8_execution_gate": _P8_05_PHASE8_EXECUTION_GATE_AUTHORISED,
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        "next_governance_action": _P8_05_NEXT_GOVERNANCE_ACTION_AUTHORISED,
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "started Phase 8 proof route misstates the incomplete result or downstream stop"

    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    required_status = (
        "WELL-5 / P8-04",
        "PROOF EXECUTION: STARTED",
        "PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
        "PROOF CERTIFICATION: NOT CERTIFIED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
        "WELL-48–50: NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION",
    )
    if any(token not in active_summary for token in required_status):
        return False, "Open Work active route omits WELL-5 completion or the incomplete proof boundary"
    if re.search(r"(?im)^\s*PROOF (?:RESULT|CERTIFICATION)\s*:\s*(?:PASS|COMPLETE|CERTIFIED)", active_summary):
        return False, "Open Work claims a complete TB-001 proof result or certification"
    if re.search(r"(?im)^\s*PHASE 9(?: / VERTICAL SLICES)?\s*:\s*(?:AUTHORI[ZS]ED|STARTED|IN PROGRESS|COMPLETE)", active_summary):
        return False, "Open Work advances Phase 9 or Vertical Slices"

    readme_current = _markdown_h2_section(readme, "Current State") or ""
    readme_status = required_status[1:] + (
        "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
        "WELL-48–50: NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION; NOT COMPLETE",
        "APPLICATION IMPLEMENTATION: AUTHORISED ONLY INSIDE BOUNDED PHASE 8 ARCHITECTURAL PROOF, INCLUDING P8-05",
        "WELL-45: LEGAL/PRIVACY RELEASE GATE OPEN — DEVELOPMENT BASELINE PERMITTED; NOT LEGALLY APPROVED",
        "NEXT EXECUTION ACTION: After this authorization is current and resulting-main verification succeeds",
        "WELL-45 remains a legal/privacy release gate",
    )
    if any(token.casefold() not in readme_current.casefold() for token in readme_status):
        return False, "README current state does not mirror the incomplete Phase 8 proof route"
    route = _p8_05_current_authorization_section(contract)
    if not route:
        return False, "current HARDEN-02 route omits the bounded P8-05 authorization section"
    required_route = _p8_05_current_authorization_section_tokens()
    if any(token.casefold() not in route.casefold() for token in required_route):
        return False, "current HARDEN-02 route omits bounded P8-05 authorization or proof boundaries"
    if "phase 8" not in route.casefold():
        return False, "current HARDEN-02 route omits the Phase 8 certification boundary"
    return True, "WELL-5 is complete; bounded P8-05 implementation is authorised and Phase 8 remains uncertified"


def _h02_audit_v010_promotion_lifecycle_state(
    state: dict[str, Any],
    active: str,
    readme: str,
    contract: str,
) -> tuple[bool, str]:
    """Validate the current Audit promotion and Phase 7B candidate routing."""
    current_successor_version = state.get("status_successor_version")
    if current_successor_version in {"0.5.15", "0.5.16"}:
        return _h02_phase7c_current_status_lifecycle_state(state, active, readme, contract)
    if current_successor_version == "0.5.13":
        return _h02_phase7c_candidate_lifecycle_state(state, active, readme, contract)
    if current_successor_version in {"0.5.11", "0.5.12"}:
        tracker_closure_sync = current_successor_version == "0.5.12"
        expected = {
            "status_successor_version": current_successor_version,
            "status_successor_base_sha": "3f4c9bf564b2b011e96171b8664428423eeba558" if tracker_closure_sync else "f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3",
            "current_stage": "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
            "next_stage": "AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
            "harden_02_execution": "COMPLETE / CERTIFIED",
            "harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY",
            "store_cer": "EXCLUDED",
            "audit_dossier": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
            "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
            "phase_7c": "NEXT / NOT_STARTED",
            "proof_classification": "NOT FINALISED",
            "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
            "pr_38": "STALE / BLOCKED / NOT AUTHORITY",
            "engineering_standards_authority_promotion": "COMPLETE / CERTIFIED",
            "fp001_reconciliation": "COMPLETE / CERTIFIED",
            "communications_dossier": "CERTIFIED / CURRENT v0.1.0",
            "communications_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
            "communications": "COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "communications_finalisation": "BLOCKED / STOP",
            "identity_dossier": "CERTIFIED / CURRENT v0.1.4",
            "identity_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
            "audit_dossier_execution_tracker_issue": 116,
            "audit_dossier_candidate_pr": 118,
            "audit_dossier_work_start_baseline_main_sha": "332d51f19d77430fe4e95911920fe0c87cab524a",
            "phase_7b_reconciliation_execution_tracker_issue": 120,
            "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
            "audit_current_status_promotion": "PR #119 STATUS SUCCESSOR",
            "audit_certified_candidate_sha256": "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea",
            "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.10.md",
            "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.12.md",
            "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.12.md",
        }
        if tracker_closure_sync:
            expected["phase_7b_reconciliation_execution_tracker_state"] = "CLOSED / COMPLETED"
        if any(state.get(key) != value for key, value in expected.items()):
            return False, f"HARDEN .{current_successor_version} current state omits certification or misstates a protected gate"
        expected_conditionals = {
            "privacy_consent": "NOT_REQUIRED",
            "content_media": "NOT_REQUIRED",
            "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
            "analytics": "NOT_REQUIRED",
        }
        if state.get("conditional_dossiers") != expected_conditionals:
            return False, f"HARDEN .{current_successor_version} conditional dossier dispositions changed"
        expected_milestones = [
            "TARGETED PRODUCT AMENDMENT PROGRAMME",
            "FP-001 PHASE 7A",
            "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
            "HARDEN-02 EXECUTION",
            "ENGINEERING STANDARDS AUTHORITY PROMOTION",
            "FP-001 PMR RECONCILIATION",
            "FP-001 IDENTITY v0.1.3 DURABLE-DELIVERY PATCH PROMOTION",
            "FP-001 IDENTITY v0.1.4 GOVERNANCE-CORRECTION PATCH PROMOTION",
            "FP-001 COMMUNICATIONS v0.1.0 JIT DOMAIN DOSSIER PROMOTION",
            "FP-001 PHASE 7A/7B CONDITIONAL-DOSSIER ADJUDICATION",
            "FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION",
        ]
        if state.get("completed_milestones") != expected_milestones:
            return False, f"HARDEN .{current_successor_version} completed milestones are missing or advance an unapproved stage"
        if state.get("execution_certification") != H02_COMPLETE_CERTIFICATION_FACTS:
            return False, f"HARDEN .{current_successor_version} lost its certified execution lifecycle evidence"
        if state.get("phase_7b_reconciliation_candidate") != {
            "path": "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
            "current_status_successor_path": "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
            "version": "0.1.0",
            "result": "PASS / READY FOR INDEPENDENT REVIEW",
            "lifecycle": "CERTIFIED / CURRENT",
            "certification": "COMPLETE; EXACT CANDIDATE MERGED UNCHANGED; RESULTING-MAIN VERIFIED",
            "tracker_issue": 120,
        }:
            return False, f"HARDEN .{current_successor_version} does not distinguish the immutable candidate from its current successor"
        if state.get("downstream_route") != [
            "CERTIFIED HARDEN-02 EXECUTION",
            "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
            "CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
            "FP001_RECONCILIATION_REQUIRED",
            "CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
            "COMMUNICATIONS JIT DOMAIN DOSSIER",
            "CERTIFIED FP-001 COMMUNICATIONS v0.1.0 DOSSIER PROMOTION",
            "CERTIFIED FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION",
            "FP-001 PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
            "PHASE 7C FINAL FEATURE PACK CONTRACT: NEXT / NOT_STARTED",
            "PROOF CLASSIFICATION",
            "PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
        ]:
            return False, f"HARDEN .{current_successor_version} downstream route starts Phase 7C, proof or Phase 8 early"

        active_checks = (
            "CURRENT AUTHORITY-STAGE PROGRAMME: FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
            "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
            "PHASE 7C: NEXT / NOT_STARTED",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
            "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "APPROVED AFFECTED DOMAINS: IDENTITY & ACCESS; PRIVACY & CONSENT; CONTENT & MEDIA; COMMUNICATIONS; AUDIT & EVIDENCE; ANALYTICS",
            "MATERIAL CAPABILITY RELATIONSHIPS: CAP-001, CAP-002, CAP-003, CAP-005, CAP-006, CAP-017, CAP-028 (seven; unchanged)",
        )
        if any(
            active.count(token) != 1
            for token in active_checks
            if token != "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT"
        ) or active.count("PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT") < 1:
            return False, f"Open Work .{current_successor_version} active route omits the certified Phase 7B or downstream gate state"
        expected_tracker = (
            "RECONCILIATION EXECUTION TRACKER: #120 CLOSED / COMPLETED"
            if tracker_closure_sync
            else "RECONCILIATION EXECUTION TRACKER: #120 OPEN"
        )
        if active.count(expected_tracker) != 1:
            return False, f"Open Work .{current_successor_version} tracker route is missing or contradictory"
        if tracker_closure_sync and TRACKER_120_OPEN_PROJECTION_PATTERN.search(active):
            return False, "Open Work current active route still projects tracker #120 as open"
        if re.search(r"(?im)^.*PHASE 7B RECONCILIATION\s*:\s*(?:IN PROGRESS|NEXT / NOT_STARTED|STARTED).*$", active):
            return False, f"Open Work .{current_successor_version} leaves completed Phase 7B reconciliation unverified"
        if re.search(r"(?im)^.*PHASE 7C\s*:\s*(?:BLOCKED|IN PROGRESS|COMPLETE|CERTIFIED|AUTHORI[ZS]ED).*$", active):
            return False, f"Open Work .{current_successor_version} starts or incorrectly blocks Phase 7C"
        if re.search(r"(?im)^.*PROOF CLASSIFICATION\s*:\s*(?:FINAL|FINALI[ZS]ED|CERTIFIED).*$", active):
            return False, f"Open Work .{current_successor_version} finalises proof classification"
        if re.search(r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$", active):
            return False, f"Open Work .{current_successor_version} authorises Phase 8 or application implementation"

        readme_current = _markdown_h2_section(readme, "Current State") or ""
        readme_checks = (
            *(token for token in active_checks if not token.startswith(("APPROVED AFFECTED DOMAINS:", "MATERIAL CAPABILITY RELATIONSHIPS:"))),
            "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT; STATUS: NOT_STARTED",
            "HARDEN-02 CURRENT STATUS: `working/HARDEN-02_CONTRACT_WORKING_v0.5.12.md`",
        )
        if any(token not in readme_current for token in readme_checks) or "Current programme status is in Open Work v1.2.68." not in readme:
            return False, "README current route omits the Phase 7B certification or current successor routes"
        if tracker_closure_sync and TRACKER_120_OPEN_PROJECTION_PATTERN.search(readme_current):
            return False, "README current route still projects tracker #120 as open"
        section_start = contract.find("## 21. Current execution certification and next stage")
        section_end = contract.find("## 22.", section_start + 1)
        section = contract[section_start:section_end] if section_start >= 0 and section_end > section_start else ""
        route_checks = (
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
            "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT; STATUS: NOT_STARTED",
            "PHASE 7C: NEXT / NOT_STARTED",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
            "→ CERTIFIED FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION\n→ COMPLETED FP-001 PHASE 7B RECONCILIATION",
            "→ COMPLETED FP-001 PHASE 7B RECONCILIATION",
            "→ AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT (NEXT / NOT_STARTED)",
        )
        if not section or any(token not in section for token in route_checks):
            return False, f"HARDEN .{current_successor_version} current route is missing its final certified lifecycle or NEXT-only Phase 7C boundary"
        current_route = _markdown_h2_section(contract, "23. FP-001 Phase 7B reconciliation current route") or ""
        if tracker_closure_sync and "RECONCILIATION EXECUTION TRACKER: #120 CLOSED / COMPLETED" not in current_route:
            return False, "HARDEN current route does not record issue #120 as CLOSED / COMPLETED"
        if "PHASE 7C: BLOCKED / NOT_STARTED" in section or "PHASE 7B RECONCILIATION CANDIDATE CERTIFICATION" in section:
            return False, f"HARDEN .{current_successor_version} current section retains a superseded candidate route"
        current_route_start = contract.find("## 23. FP-001 Phase 7B reconciliation current route")
        if current_route_start < 0 or "NEXT: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT\nSTATUS: NOT_STARTED" not in contract[current_route_start:]:
            return False, "HARDEN .5.11 current reconciliation route is missing"
        return True, "HARDEN preserves its certified contract and routes completed Phase 7B to the unstarted Phase 7C contract"

    reconciliation_candidate_current = state.get("status_successor_version") == "0.5.10"
    expected = {
        "status_successor_version": "0.5.10" if reconciliation_candidate_current else "0.5.9",
        "status_successor_base_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd" if reconciliation_candidate_current else "3566f1353ef34af58773aa13c6f5bd61d2613d96",
        "current_stage": "FP-001 PHASE 7B RECONCILIATION CANDIDATE REVIEW" if reconciliation_candidate_current else "FP-001 AUDIT & EVIDENCE DOSSIER CURRENT-STATUS PROMOTION",
        "next_stage": "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION" if reconciliation_candidate_current else "FP-001 PHASE 7B RECONCILIATION",
        "harden_02_execution": "COMPLETE / CERTIFIED",
        "harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY",
        "store_cer": "EXCLUDED",
        "audit_dossier": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation": "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING" if reconciliation_candidate_current else "NEXT / NOT_STARTED",
        "phase_7c": "BLOCKED / NOT_STARTED",
        "phase_7c_block_reason": "Successful Phase 7B reconciliation is required; Audit dossier authorship and current status are complete",
        "proof_classification": "NOT FINALISED",
        "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
        "pr_38": "STALE / BLOCKED / NOT AUTHORITY",
        "engineering_standards_authority_promotion": "COMPLETE / CERTIFIED",
        "fp001_reconciliation": "COMPLETE / CERTIFIED",
        "communications_dossier": "CERTIFIED / CURRENT v0.1.0",
        "communications_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
        "communications": "COMPLETE / CERTIFIED / CURRENT v0.1.0",
        "communications_finalisation": "BLOCKED / STOP",
        "identity_dossier": "CERTIFIED / CURRENT v0.1.4",
        "identity_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
        "audit_dossier_execution_tracker_issue": 116,
        "audit_dossier_candidate_pr": 118,
        "audit_dossier_work_start_baseline_main_sha": "332d51f19d77430fe4e95911920fe0c87cab524a",
    }
    if any(state.get(key) != value for key, value in expected.items()):
        return False, "HARDEN .5.9 lifecycle state omits the Audit current-status route or changes a protected gate"
    if state.get("conditional_dossiers") != {
        "privacy_consent": "NOT_REQUIRED",
        "content_media": "NOT_REQUIRED",
        "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "analytics": "NOT_REQUIRED",
    }:
        return False, "HARDEN .5.9 conditional dossier dispositions are inconsistent"
    if state.get("completed_milestones") != [
        "TARGETED PRODUCT AMENDMENT PROGRAMME",
        "FP-001 PHASE 7A",
        "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
        "HARDEN-02 EXECUTION",
        "ENGINEERING STANDARDS AUTHORITY PROMOTION",
        "FP-001 PMR RECONCILIATION",
        "FP-001 IDENTITY v0.1.3 DURABLE-DELIVERY PATCH PROMOTION",
        "FP-001 IDENTITY v0.1.4 GOVERNANCE-CORRECTION PATCH PROMOTION",
        "FP-001 COMMUNICATIONS v0.1.0 JIT DOMAIN DOSSIER PROMOTION",
        "FP-001 PHASE 7A/7B CONDITIONAL-DOSSIER ADJUDICATION",
        "FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION",
    ]:
        return False, "HARDEN .5.9 completed milestones are missing or advance an unapproved stage"
    if state.get("execution_certification") != H02_COMPLETE_CERTIFICATION_FACTS:
        return False, "HARDEN .5.9 lost its certified execution lifecycle evidence"
    expected_fp001_certification = {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/67",
        "candidate_sha": "79d0540c66f0224ece0330181e61dfef8ab4b458",
        "prior_main_sha": "38022caea64cb2522ab8fc4db730099a94cd6600",
        "resulting_main_sha": "4000ae50660930114e3ad43108dc029fd0673d32",
        "candidate_tree_sha": "a71dbeb2cca79bea0013f9997e40f34769f262f3",
        "exact_head_ci_run": "36991113390",
        "resulting_main_ci_run": "37009244020",
        "pre_merge_attestation_comment": "5952693308",
        "post_merge_attestation_comment": "5955641536",
        "post_merge_independent_review": "PASS",
    }
    if state.get("fp001_reconciliation_certification") != expected_fp001_certification:
        return False, "HARDEN .5.9 lost the completed FP-001 reconciliation certification facts"
    promotion = state.get("audit_current_status_promotion", "")
    if not isinstance(promotion, str) or not re.fullmatch(r"PR #[1-9][0-9]* STATUS SUCCESSOR", promotion):
        return False, "HARDEN .5.9 does not bind the Audit status successor to a real promotion PR"
    if state.get("audit_certified_candidate_sha256") != "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea":
        return False, "HARDEN .5.9 Audit candidate certification hash is missing or incorrect"
    if reconciliation_candidate_current and (
        state.get("phase_7b_reconciliation_candidate") != {
            "path": "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
            "version": "0.1.0",
            "result": "PASS / READY FOR INDEPENDENT REVIEW",
            "lifecycle": "NOT CERTIFIED / NOT CURRENT",
            "certification": "PENDING FRESH INDEPENDENT EXACT-HEAD REVIEW",
            "tracker_issue": 120,
        }
        or state.get("phase_7b_reconciliation_execution_tracker_issue") != 120
        or state.get("phase_7b_reconciliation_baseline_main_sha") != "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd"
    ):
        return False, "HARDEN .5.10 candidate record is missing, stale or falsely certified"

    expected_route = [
        "CERTIFIED HARDEN-02 EXECUTION",
        "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
        "CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
        "FP001_RECONCILIATION_REQUIRED",
        "CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
        "COMMUNICATIONS JIT DOMAIN DOSSIER",
        "CERTIFIED FP-001 COMMUNICATIONS v0.1.0 DOSSIER PROMOTION",
        "CERTIFIED FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION",
        "FP-001 PHASE 7B RECONCILIATION",
        "PHASE 7C",
        "PROOF CLASSIFICATION",
        "PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
    ]
    if state.get("downstream_route") != expected_route:
        return False, "HARDEN downstream route advances or skips a required lifecycle stage"
    if re.findall(r"(?m)^CURRENT AUTHORITY-STAGE PROGRAMME:\s*(.*?)\s*$", active) != [expected["current_stage"]]:
        return False, "Open Work current programme stage is missing, duplicated or contradictory"
    if re.findall(r"(?m)^NEXT STAGE:\s*(.*?)\s*$", active) != [expected["next_stage"]]:
        return False, "Open Work NEXT route is missing, duplicated or contradictory"
    if reconciliation_candidate_current and (
        active.count("RECONCILIATION CANDIDATE: NOT CERTIFIED / NOT CURRENT") != 1
        or active.count("RECONCILIATION EXECUTION TRACKER: #120 OPEN — links #111, completed #114 and completed #116") != 1
    ):
        return False, "Open Work .5.10 candidate lifecycle or tracker is missing"
    for token in (
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
        "PR #118 CANDIDATE CERTIFICATION: COMPLETE",
        "PR #118 POST-MERGE CERTIFICATION EVIDENCE: COMPLETE",
        "PHASE 7B RECONCILIATION: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING" if reconciliation_candidate_current else "PHASE 7B RECONCILIATION: NEXT / NOT_STARTED",
        "PHASE 7C: BLOCKED / NOT_STARTED UNTIL SUCCESSFUL PHASE 7B RECONCILIATION",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
    ):
        if token not in active:
            return False, f"Open Work .5.9 active route omits {token!r}"
    if re.search(r"(?im)^.*PHASE 7B RECONCILIATION\s*:\s*(?:COMPLETE|CERTIFIED|STARTED).*$", active):
        return False, "Open Work .5.9 falsely advances Phase 7B reconciliation"
    if re.search(r"(?im)^.*PHASE 7C\s*:\s*(?:NEXT|READY|UNBLOCKED|COMPLETE|CERTIFIED|AUTHORI[ZS]ED).*$", active):
        return False, "Open Work .5.9 unblocks Phase 7C before successful reconciliation"
    if re.search(r"(?im)^.*PROOF CLASSIFICATION\s*:\s*(?:FINAL|FINALI[ZS]ED|CERTIFIED).*$", active):
        return False, "Open Work .5.9 finalises proof classification"
    if re.search(r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$", active):
        return False, "Open Work .5.9 authorises Phase 8 or application implementation"

    readme_current = readme.split("## Current State", 1)[-1]
    for token in (
        "CURRENT AUTHORITY-STAGE PROGRAMME: " + expected["current_stage"],
        (
            "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
            if reconciliation_candidate_current
            else "NEXT STAGE: FP-001 PHASE 7B RECONCILIATION (NEXT / NOT_STARTED)"
        ),
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: BLOCKED / NOT_STARTED",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED",
    ):
        if token not in readme_current:
            return False, f"README .5.9 current route omits {token!r}"
    current_route_start = contract.rfind("## 21. Current execution certification and next stage")
    current_route = contract[current_route_start:] if current_route_start >= 0 else ""
    route_marker = "The current route continues:\n\n```text\n"
    current_route_flow = current_route.split(route_marker, 1)[1] if route_marker in current_route else ""
    required_route_flow = "\n".join(
        [
            "CERTIFIED HARDEN-02 EXECUTION",
            "→ CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
            "→ CERTIFIED FP-001 PMR RECONCILIATION",
            "→ CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
            "→ COMMUNICATIONS JIT DOMAIN DOSSIER",
            "→ CERTIFIED FP-001 COMMUNICATIONS v0.1.0 DOSSIER PROMOTION",
            "→ CERTIFIED FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION",
            "→ FP-001 PHASE 7B RECONCILIATION CANDIDATE CERTIFICATION"
            if reconciliation_candidate_current
            else "→ FP-001 PHASE 7B RECONCILIATION",
            "→ PHASE 7C",
            "→ PROOF CLASSIFICATION",
            "→ PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
        ]
    )
    if required_route_flow not in current_route_flow:
        return False, "HARDEN .5.9 Markdown route skips the Audit dossier or advances a blocked downstream stage"
    for token in (
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        (
            "Phase 7B reconciliation is IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if reconciliation_candidate_current
            else "Phase 7B reconciliation is NEXT / NOT_STARTED"
        ),
        "Phase 7C remains BLOCKED / NOT_STARTED until successful Phase 7B reconciliation",
        "proof classification remains NOT FINALISED",
        "Phase 8/application implementation remains UNAUTHORISED",
    ):
        if token.casefold() not in current_route.casefold():
            return False, f"HARDEN .5.9 current route omits {token!r}"
    return True, "HARDEN preserves certified execution, Audit current status and the candidate-only Phase 7B stop route"


def _engineering_standards_candidate_signal(
    root: Path,
    manifest: dict[str, Any],
    readme: str,
) -> bool:
    """Detect any Standards-candidate signal so production audit cannot skip validation."""

    docs = Path(root) / "docs" / "00_platform"
    manifest_signal = any(
        "ENGINEERING_STANDARDS" in str(entry.get(field, "")).upper()
        for entry in _all_entries(manifest)
        for field in ("document_id", "canonical_filename", "repository_path", "authority_class")
    )
    readme_signal = (
        "## Engineering Standards promotion candidate" in readme
        or "reference/ENGINEERING_STANDARDS_v1.0.0.md" in readme
    )

    artifact_signal = False
    if docs.is_dir():
        for path in docs.rglob("*"):
            if not path.is_file():
                continue
            if "engineering_standards" in path.name.casefold():
                artifact_signal = True
                break
            if path.suffix.casefold() != ".md":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue
            if (
                "# Engineering Standards v1.0.0" in text
                or "- **Status:** PROMOTION CANDIDATE / NOT CERTIFIED" in text
                or "- **Authority class:** SUPPORTING AUTHORITY / ENGINEERING STANDARDS CANDIDATE" in text
            ):
                artifact_signal = True
                break

    return manifest_signal or readme_signal or artifact_signal


def _engineering_standards_promotion_state(
    root: Path,
    manifest: dict[str, Any],
    readme: str,
    open_work: str,
    harden: str,
) -> tuple[bool, str]:
    """Validate the fail-closed, pre-certification Standards promotion candidate."""

    docs = Path(root) / "docs" / "00_platform"
    candidate = docs / "reference" / "ENGINEERING_STANDARDS_v1.0.0.md"
    prohibited = (
        docs / "ENGINEERING_STANDARDS_v1.0.0.md",
        docs / "reference" / "ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
        docs / "working" / "ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    )
    if not candidate.is_file():
        return False, "Engineering Standards promotion candidate artifact is missing"
    if any(path.exists() for path in prohibited):
        return False, "a prohibited or stale Engineering Standards path exists"
    competing_artifacts = [
        path
        for path in docs.rglob("*")
        if path.is_file()
        and "engineering_standards" in path.name.casefold()
        and path != candidate
    ]
    if competing_artifacts:
        return False, "duplicate or competing Engineering Standards artifact exists"

    candidate_text = candidate.read_text(encoding="utf-8")
    if candidate_text.count("- **Status:** PROMOTION CANDIDATE / NOT CERTIFIED") != 1:
        return False, "candidate status is missing, duplicated, or claims certification"
    if candidate_text.count("- **Authority class:** SUPPORTING AUTHORITY / ENGINEERING STANDARDS CANDIDATE") != 1:
        return False, "candidate authority classification is missing or contradictory"
    if "Promotion baseline main SHA:** `73eca9d9148a82cab8ae988c5950539bfee0d7f9`" not in candidate_text:
        return False, "candidate is not bound to the live main baseline"
    if "Source Grill:** `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md`" not in candidate_text:
        return False, "candidate source Grill route is missing"
    if "Source Grill SHA-256:** `27bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017`" not in candidate_text:
        return False, "candidate source Grill provenance is missing"
    if "No package, framework, tool, version, flag, provider or vendor is selected by this candidate." not in candidate_text:
        return False, "candidate does not preserve deferred package and tool selection"
    if "No Architecture, Product or Domain rule is copied into this document as a new authority." not in candidate_text:
        return False, "candidate does not preserve the upstream-authority boundary"
    if re.search(r"(?im)^\s*[-*].*\b(?:DEC|ARC|ARQ|DOL|OQ)-\d+\b", candidate_text):
        return False, "candidate introduces an unapproved upstream governed identifier"

    required_provenance = (
        "EP-Q1",
        "EP-Q2",
        "EP-Q3",
        "EP-Q4",
        "EP-Q5",
        "A-08",
        "B-09",
        "D-02",
        "D-03",
        "D-04",
        "D-05",
        "D-07",
    )
    if any(marker not in candidate_text for marker in required_provenance):
        return False, "candidate normative content lacks complete Grill provenance"
    if re.search(r"(?im)^.*ENGINEERING STANDARDS.*COMPLETE / CERTIFIED.*$", candidate_text):
        return False, "candidate claims uncertified Standards are complete or certified"

    forbidden_advancement = (
        r"(?im)FP-001 reconciliation is COMPLETE / PERFORMED",
        r"(?im)COMMUNICATIONS\s*:\s*(?:STARTED|COMPLETE|AUTHORI[ZS]ED)",
        r"(?im)PHASE 7C\s*:\s*(?:NEXT|UNBLOCKED|COMPLETE|AUTHORI[ZS]ED)",
        r"(?im)PROOF CLASSIFICATION\s*:\s*FINALI[SZ]ED",
        r"(?im)(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE)",
        r"(?im)STORE\s*/\s*CER\s*:\s*IN SCOPE",
    )
    if any(re.search(pattern, candidate_text) for pattern in forbidden_advancement):
        return False, "candidate advances a downstream stage or expands HARDEN-02 scope"

    entries = [entry for key in ("governing_documents", "reference_documents", "historical_documents") for entry in manifest.get(key, [])]
    candidate_entries = [entry for entry in entries if entry.get("document_id") == "ENGINEERING_STANDARDS_CANDIDATE"]
    if len(candidate_entries) != 1:
        return False, "candidate must have exactly one manifest entry"
    entry = candidate_entries[0]
    if entry not in manifest.get("reference_documents", []):
        return False, "candidate must be registered under reference_documents"
    if entry.get("repository_path") != "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.0.md":
        return False, "candidate manifest route is not canonical"
    if entry.get("canonical_filename") != "ENGINEERING_STANDARDS_v1.0.0.md":
        return False, "candidate manifest filename is not canonical"
    if entry.get("semver") != "1.0.0":
        return False, "candidate manifest version is not v1.0.0"
    if entry.get("authority_class") != "ENGINEERING_STANDARDS_SUPPORTING_AUTHORITY_CANDIDATE":
        return False, "candidate manifest authority class is missing or competing"
    if entry.get("lifecycle") != "candidate":
        return False, "candidate manifest lifecycle must remain candidate until certification"
    if entry.get("sha256") != sha256_file(candidate):
        return False, "candidate manifest hash does not match the artifact"
    if any(
        entry_item is not entry
        and re.search(
            r"ENGINEERING_STANDARDS",
            str(entry_item.get("repository_path", "")),
            re.IGNORECASE,
        )
        and entry_item.get("document_id") != "ENGINEERING_STANDARDS_CANDIDATE"
        for entry_item in entries
    ):
        return False, "duplicate or competing Engineering Standards manifest route exists"

    if readme.count("## Engineering Standards promotion candidate") != 1:
        return False, "README candidate route is missing or duplicated"
    if readme.count("reference/ENGINEERING_STANDARDS_v1.0.0.md") != 1:
        return False, "README does not route the canonical candidate"
    if len(re.findall(r"(?m)^- ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED$", readme)) != 1:
        return False, "README incorrectly advances or omits the pre-certification status"
    if re.search(r"(?m)^- ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED$", readme):
        return False, "README claims Standards certification before the lifecycle completes"
    if open_work.count("ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED") != 1:
        return False, "Open Work incorrectly advances or omits the pre-certification status"
    if "FP001_RECONCILIATION_REQUIRED: REQUIRED / DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION / NOT PERFORMED" not in open_work:
        return False, "Open Work does not preserve the downstream FP-001 gate"
    current_harden_status = re.search(
        r"(?m)^\| `ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED` \|",
        harden,
    )
    if current_harden_status is None:
        return False, "HARDEN status does not preserve the pre-certification route"
    return True, "Engineering Standards promotion candidate is registered, traceable and not certified"


def _engineering_standards_normative_body(text: str) -> str:
    start = re.search(r"(?m)^## Risk classification\s*$", text)
    end = re.search(r"(?m)^## Deferred choices and closed alternatives\s*$", text)
    if start is None or end is None or start.start() >= end.start():
        return ""
    return text[start.start() : end.start()]


def _engineering_standards_certified_state(
    root: Path,
    manifest: dict[str, Any],
    readme: str,
    open_work: str,
    harden: str,
) -> tuple[bool, str]:
    """Validate the certified Standards authority and its one-stage downstream route."""

    docs = Path(root) / "docs" / "00_platform"
    current = docs / "reference" / "ENGINEERING_STANDARDS_v1.0.1.md"
    predecessor = docs / "archive" / "ENGINEERING_STANDARDS_v1.0.0.md"
    source_grill = docs / "working" / "TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md"
    expected_source_sha = "27bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017"
    expected_predecessor_sha = "feb2bf132fdca74bd534c83526a19e06659879a9b4f09bec7f5ca4b2e3c89df4"

    all_entries = _all_entries(manifest)
    is_standards_entry = lambda entry: (
        "ENGINEERING_STANDARDS" in str(entry.get("document_id", "")).upper()
        or "ENGINEERING_STANDARDS" in str(entry.get("authority_class", "")).upper()
        or "ENGINEERING_STANDARDS" in str(entry.get("repository_path", "")).upper()
    )
    active_entries = [
        entry
        for key in ("governing_documents", "reference_documents")
        for entry in manifest.get(key, [])
        if is_standards_entry(entry) and entry.get("lifecycle", "current") != "historical"
    ]
    if len(active_entries) != 1:
        return False, "exactly one active Engineering Standards registration is required"
    active_entry = active_entries[0]
    if active_entry not in manifest.get("reference_documents", []):
        return False, "certified Engineering Standards must remain under reference_documents"
    if active_entry in manifest.get("governing_documents", []):
        return False, "certified Engineering Standards cannot be governing-root authority"
    if (
        active_entry.get("document_id") != "ENGINEERING_STANDARDS"
        or active_entry.get("repository_path") != "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md"
        or active_entry.get("canonical_filename") != "ENGINEERING_STANDARDS_v1.0.1.md"
        or active_entry.get("semver") != "1.0.1"
        or active_entry.get("authority_class") != "ENGINEERING_STANDARDS_SUPPORTING_AUTHORITY"
        or active_entry.get("lifecycle") != "current"
        or active_entry.get("superseded_version") != "1.0.0"
    ):
        return False, "certified Engineering Standards registration has an unsupported route, class, lifecycle or version"

    historical_candidates = [
        entry
        for entry in manifest.get("historical_documents", [])
        if entry.get("document_id") == "ENGINEERING_STANDARDS_CANDIDATE_V1_0_0"
    ]
    if len(historical_candidates) != 1:
        return False, "the PR #65 candidate must be retained as one historical manifest registration"
    archived = historical_candidates[0]
    if (
        archived.get("repository_path") != "docs/00_platform/archive/ENGINEERING_STANDARDS_v1.0.0.md"
        or archived.get("canonical_filename") != "ENGINEERING_STANDARDS_v1.0.0.md"
        or archived.get("semver") != "1.0.0"
        or archived.get("authority_class") != "ENGINEERING_STANDARDS_SUPPORTING_AUTHORITY_CANDIDATE"
        or archived.get("lifecycle") != "historical"
        or archived.get("sha256") != expected_predecessor_sha
    ):
        return False, "the archived PR #65 candidate registration is missing or contradictory"
    active_candidate_entries = [
        entry
        for entry in all_entries
        if entry.get("authority_class") == "ENGINEERING_STANDARDS_SUPPORTING_AUTHORITY_CANDIDATE"
        and entry.get("lifecycle", "current") != "historical"
    ]
    if active_candidate_entries:
        return False, "a candidate and certified Engineering Standards authority cannot both be active"

    if not current.is_file() or not predecessor.is_file():
        return False, "the certified Standards artifact or byte-preserved candidate archive is missing"
    competing_artifacts = [
        path
        for path in docs.rglob("*")
        if path.is_file()
        and "engineering_standards" in path.name.casefold()
        and path not in {current, predecessor}
    ]
    if competing_artifacts:
        return False, "duplicate or competing Engineering Standards artifact exists"
    current_text = current.read_text(encoding="utf-8")
    predecessor_text = predecessor.read_text(encoding="utf-8")
    if sha256_file(predecessor) != expected_predecessor_sha:
        return False, "archived candidate bytes do not match the PR #65 candidate SHA-256"
    if active_entry.get("sha256") != sha256_file(current):
        return False, "certified Standards manifest hash does not match the artifact"
    if _engineering_standards_normative_body(current_text) != _engineering_standards_normative_body(predecessor_text):
        return False, "certified Standards normative body differs from the byte-preserved candidate"
    if not _engineering_standards_normative_body(current_text):
        return False, "certified Standards normative body could not be isolated"
    if not source_grill.is_file() or sha256_file(source_grill) != expected_source_sha:
        return False, "the sole Stage 4B source Grill is missing or has changed"

    required_metadata = (
        "# Engineering Standards v1.0.1",
        "- **Document version:** v1.0.1",
        "- **Status:** CERTIFIED / CURRENT",
        "- **Authority class:** SUPPORTING AUTHORITY / ENGINEERING STANDARDS",
        "Promotion baseline main SHA:** `73eca9d9148a82cab8ae988c5950539bfee0d7f9`",
        "Certification status successor base main SHA:** `596d9560aa2b3b3cb941560b01bdc6c8ba7c525a`",
        "Source Grill:** `working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md`",
        f"Source Grill SHA-256:** `{expected_source_sha}`",
        "PR | [#65](https://github.com/JCSchoeman96/NewYou/pull/65)",
        "Certified pre-merge candidate head | `36de8f04c83a837f8b2d5e162ce10cc29f817d55`",
        "Candidate and resulting-main tree | `1206905fe7b5391564841fa2a8b9198635c84848`",
        "Resulting main | `596d9560aa2b3b3cb941560b01bdc6c8ba7c525a`",
        f"Candidate artifact SHA-256 | `{expected_predecessor_sha}`",
        "Exact-head Foundation Integrity run | [36920390090]",
        "Resulting-main Foundation Integrity run | [36967771106]",
        "Pre-merge attestation | [PR #65 comment 5945899280]",
        "Post-merge attestation | [PR #65 comment 5946270554]",
        "Fresh independent post-merge review | PASS",
    )
    if any(marker not in current_text for marker in required_metadata):
        return False, "certified Standards lifecycle evidence is incomplete or contradictory"
    if "PROMOTION CANDIDATE / NOT CERTIFIED" in current_text:
        return False, "the current Standards artifact still says NOT CERTIFIED"
    if re.search(r"(?im)^.*ENGINEERING STANDARDS AUTHORITY PROMOTION.*NEXT / AUTHORISED / NOT STARTED.*$", current_text):
        return False, "certified Standards still routes its own promotion as NEXT"
    if "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED" in current_text:
        return False, "certified Standards retains the stale candidate-only promotion route"

    if readme.count("## Certified Engineering Standards supporting authority") != 1:
        return False, "README certified Standards route is missing or duplicated"
    if "reference/ENGINEERING_STANDARDS_v1.0.1.md" not in readme:
        return False, "README does not route the certified Standards artifact"
    if "archive/ENGINEERING_STANDARDS_v1.0.0.md" not in readme:
        return False, "README does not identify the archived PR #65 candidate"
    if "## Engineering Standards promotion candidate" in readme:
        return False, "README retains stale candidate-only Standards routing"

    if _fp001_phase8_execution_status_successor_is_current(manifest):
        phase8 = manifest.get("integrity_rules", {}).get(
            "fp001_phase8_proof_contract_lifecycle", {}
        )
        routes = phase8.get("current_routes", {}) if isinstance(phase8, dict) else {}
        harden_path = routes.get("harden_02") if isinstance(routes, dict) else None
        harden_text = (Path(root) / harden_path).read_text(encoding="utf-8") if isinstance(harden_path, str) and (Path(root) / harden_path).is_file() else ""
        route = _p8_05_current_authorization_section(harden_text)
        if not route:
            return False, "current HARDEN successor omits the bounded P8-05 authorization route"
        required_current_route = _p8_05_current_authorization_section_tokens()
        if any(token.casefold() not in route.casefold() for token in required_current_route):
            return False, "current HARDEN successor omits bounded P8-05 authorization or a downstream gate"
        if "phase 8" not in route.casefold():
            return False, "current HARDEN successor omits the bounded Phase 8 boundary"
        return True, "certified Engineering Standards remain current; bounded Phase 8 P8-05 authorization remains explicit"

    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    if active_start < 0 or active_end < 0 or active_start >= active_end:
        return False, "current Open Work programme-state section is missing"
    active = open_work[active_start:active_end]
    reconciliation_candidate_current = (
        "PHASE 7B RECONCILIATION: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
        in active
    )
    reconciliation_certified_current = "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT" in active
    phase7c_candidate_current = "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING" in active
    phase7c_status_current = ("PHASE 7C: COMPLETE / CERTIFIED / CURRENT" in active and "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED" in active)
    classification_current = (
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED" in active
        and "PROOF CLASSIFICATION: NEW_TRACER_BULLET" in active
    )
    hard_stop_current = "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED" in active
    proof_contract_candidate_current = "NEXT STAGE: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION" in active
    proof_contract_approved_current = (
        "TB-001 CONTRACT LIFECYCLE: CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION" in active
        and "CONTRACT/DESIGN REVIEW: COMPLETE / PASS" in active
    )
    audit_promotion_current = reconciliation_certified_current or reconciliation_candidate_current or "NEXT STAGE: FP-001 PHASE 7B RECONCILIATION" in active
    audit_candidate_review_current = reconciliation_candidate_current or audit_promotion_current or "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION" in active
    audit_work_start_current = audit_promotion_current or audit_candidate_review_current or "NEXT STAGE: AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE" in active
    adjudication_current = audit_work_start_current or "NEXT STAGE: FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER" in active
    conditional_status = (
        (
            "- PRIVACY & CONSENT: NOT_REQUIRED",
            "- CONTENT & MEDIA: NOT_REQUIRED",
            "- AUDIT & EVIDENCE: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "- ANALYTICS: NOT_REQUIRED",
            *(
                (
                    "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
                    "PHASE 7C TRACKER #124: OPEN",
                    "PHASE 7C CONTRACT CANDIDATE: working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md; CANDIDATE / NOT CERTIFIED / NOT CURRENT",
                )
                if phase7c_candidate_current
                else (
                    "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
                    "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
                    "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
                    *(
                        (
                            "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
                            "DEVELOPMENT ENTRY HARD STOP CONDITIONS 1–10: SATISFIED",
                            "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
                            "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
                            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
                        )
                        if hard_stop_current
                        else ()
                    ),
                )
                if phase7c_status_current
                else ("PHASE 7C: NEXT / NOT_STARTED",)
            ),
            (
                "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET; PHASE 9 VERTICAL SLICES AND BROAD FP-001 IMPLEMENTATION REMAIN UNAUTHORISED"
                if hard_stop_current
                else "EXECUTABLE DEVELOPMENT: UNAUTHORISED; CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9; ALL OTHER APPLICABLE CONDITIONS REQUIRE INDEPENDENT EVALUATION"
                if classification_current
                else "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED"
            ),
        )
        if reconciliation_certified_current
        else
        (
            "- PRIVACY & CONSENT: NOT_REQUIRED",
            "- CONTENT & MEDIA: NOT_REQUIRED",
            "- AUDIT & EVIDENCE: " + (
                "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0"
                if audit_promotion_current
                else "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                if audit_work_start_current
                else "REQUIRED / NEXT / NOT_STARTED"
            ),
            *(
                (
                    "AUDIT DOSSIER CANDIDATE: " + (
                        "COMPLETE / CERTIFIED / MERGED UNCHANGED"
                        if audit_promotion_current
                        else "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
                        if audit_candidate_review_current
                        else "NOT AUTHORED / NOT CERTIFIED / NOT CURRENT"
                    ),
                )
                if audit_work_start_current
                else ()
            ),
            "- ANALYTICS: NOT_REQUIRED",
            "PHASE 7C: BLOCKED / NOT_STARTED UNTIL SUCCESSFUL PHASE 7B RECONCILIATION"
            if audit_promotion_current
            else "PHASE 7C: BLOCKED / NOT_STARTED UNTIL AUDIT DOSSIER COMPLETE / CERTIFIED / CURRENT AND PHASE 7B RECONCILIATION SUCCEEDS",
            "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
        )
        if adjudication_current
        else (
            "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
            "PHASE 7C: BLOCKED / NOT_STARTED",
            "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
        )
    )
    required_route = (
        "ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED",
        "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
        "PR #38: STALE / BLOCKED / NOT AUTHORITY",
        "PR #60: STALE HISTORICAL CANDIDATE / SUPERSEDED BY THIS SUCCESSOR / NOT MERGED / NOT AUTHORITY",
        *conditional_status,
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET" if classification_current else "PROOF CLASSIFICATION: NOT FINALISED",
        "STORE / CER: EXCLUDED FROM HARDEN-02",
    )
    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    if any(active_summary.count(line) != 1 for line in required_route):
        return False, "Open Work current route omits or duplicates the certified stage or a downstream boundary"
    if reconciliation_candidate_current and (
        active.count("PHASE 7B RECONCILIATION: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING") != 1
        or active.count("RECONCILIATION CANDIDATE: NOT CERTIFIED / NOT CURRENT") != 1
        or active.count("RECONCILIATION EXECUTION TRACKER: #120 OPEN — links #111, completed #114 and completed #116") != 1
    ):
        return False, "Open Work candidate route omits its non-current lifecycle or dedicated tracker"
    if active.count("COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0") != 1:
        return False, "Open Work Communications dossier route is missing or duplicated"
    if active.count("- COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0") != 1:
        return False, "Open Work required-dossier Communications route is missing or duplicated"
    expected_next = (
        "NEXT GOVERNANCE ACTION: WELL-6 / P8-05"
        if _fp001_phase8_execution_status_successor_is_current(manifest)
        else "NEXT STAGE: WELL-38 — Transition Foundation Integrity to implementation-era CI"
        if proof_contract_approved_current
        else
        "NEXT STAGE: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION"
        if hard_stop_current and proof_contract_candidate_current
        else "NEXT STAGE: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION"
        if hard_stop_current
        else "NEXT STAGE: DEVELOPMENT ENTRY HARD STOP EVALUATION"
        if classification_current
        else "NEXT STAGE: ARCHITECTURAL PROOF CLASSIFICATION"
        if phase7c_status_current
        else "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE"
        if phase7c_candidate_current
        else "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT"
        if reconciliation_certified_current
        else
        "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
        if reconciliation_candidate_current
        else "NEXT STAGE: FP-001 PHASE 7B RECONCILIATION"
        if audit_promotion_current
        else (
            "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
            if audit_candidate_review_current
            else "NEXT STAGE: AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE"
        )
        if audit_work_start_current
        else "NEXT STAGE: FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER"
        if adjudication_current
        else "NEXT STAGE: REMAINING REQUIRED / CONDITIONAL PHASE 7B"
    )
    if expected_next not in active_summary:
        return False, "Open Work does not route NEXT to the single remaining required Phase 7B action"
    historical_pr59_status = "**Historical pre-PR #65 status as recorded in Open Work v1.2.53:**"
    former_promotion_status = "Engineering Standards Authority Promotion was NEXT / AUTHORISED / NOT STARTED"
    if active.count(historical_pr59_status) != 1:
        return False, "the superseded pre-PR #65 promotion state is not clearly marked as historical"
    historical_status_start = active.index(historical_pr59_status)
    historical_status_end = active.find("\n\n", historical_status_start)
    if historical_status_end < 0:
        historical_status_end = len(active)
    historical_status = active[historical_status_start:historical_status_end]
    if historical_status.count(former_promotion_status) != 1:
        return False, "the prior promotion NEXT state is not confined to its labelled historical record"
    if active.count(former_promotion_status) != 1:
        return False, "Open Work retains an unlabelled stale Standards promotion NEXT status"
    if re.search(r"(?im)THIS STATUS SUCCESSOR (?:PERFORMS|EXECUTES) FP-001 RECONCILIATION", active):
        return False, "the status successor claims to perform the already-certified FP-001 reconciliation"
    if re.search(r"(?im)^.*COMMUNICATIONS\s*:\s*(?:STARTED|AUTHORI[ZS]ED).*$", active):
        return False, "Communications has advanced before FP-001 reconciliation"
    if re.search(
        r"(?im)^.*COMMUNICATIONS\s*:\s*COMPLETE(?!.*/\s*CERTIFIED\s*/\s*CURRENT\s*v0\.1\.0).*$",
        active,
    ):
        return False, "Communications has advanced before FP-001 reconciliation"
    if not reconciliation_certified_current and re.search(r"(?im)^.*PHASE 7C\s*:\s*(?:NEXT|UNBLOCKED|COMPLETE|AUTHORI[ZS]ED).*$", active):
        return False, "Phase 7C has been unblocked prematurely"
    if reconciliation_certified_current and not phase7c_candidate_current and not phase7c_status_current and "PHASE 7C: NEXT / NOT_STARTED" not in active:
        return False, "Open Work does not route Phase 7C as the next unstarted stage"
    if phase7c_candidate_current and (
        active.count("PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING") != 1
        or "PHASE 7C CONTRACT CANDIDATE: working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md; CANDIDATE / NOT CERTIFIED / NOT CURRENT" not in active
        or "NEXT PHASE 7 ACTION: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE; STATUS: PENDING" not in active
    ):
        return False, "Open Work current route omits the Phase 7C candidate-only lifecycle or review stop"
    if not classification_current and re.search(r"(?im)^.*PROOF CLASSIFICATION\s*:\s*FINALI[ZS]ED.*$", active):
        return False, "proof classification has been finalised prematurely"
    if not hard_stop_current and re.search(
        r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$",
        active,
    ):
        return False, "Phase 8 or application implementation has been authorised prematurely"
    if re.search(r"(?im)^.*STORE\s*/\s*CER\s*:\s*IN SCOPE.*$", active):
        return False, "Store/CER has been included in scope"

    harden_section_start = open_work.find("## 12.9 — HARDEN-02 contract lifecycle completion")
    harden_section_end = open_work.find("## 12.10", harden_section_start + 1)
    if harden_section_start < 0 or harden_section_end < 0 or harden_section_start >= harden_section_end:
        return False, "Open Work current HARDEN lifecycle status section is missing or malformed"
    harden_section = open_work[harden_section_start:harden_section_end]
    required_harden_status = (
        (
            "Historical execution and Engineering Standards Authority Promotion remain COMPLETE / CERTIFIED.",
            "FP-001 PMR reconciliation is COMPLETE / CERTIFIED under PR #67.",
            "Identity v0.1.4 is COMPLETE / CERTIFIED / CURRENT under PR #77",
            "Communications v0.1.0 is COMPLETE / CERTIFIED / CURRENT under PR #81",
            "Audit & Evidence v0.1.0 is REQUIRED / COMPLETE / CERTIFIED / CURRENT following PR #119.",
            "At the v1.2.65 predecessor point the dossier set was disposition-complete and Phase 7B reconciliation was NEXT / NOT_STARTED.",
            "At the v1.2.66 candidate point, Phase 7B was in progress and awaiting certification; that historical state is recorded in §12.23.",
            "The v1.2.67 and v1.2.68 predecessor routes recorded Phase 7B as COMPLETE / CERTIFIED / CURRENT and Phase 7C as NEXT / NOT_STARTED.",
            (
                "The historical v1.2.70 route in §9 recorded Phase 7C and Final Feature Pack Contract v0.1.0 as COMPLETE / CERTIFIED / CURRENT after that status successor merged, with issue #124 OPEN through resulting-main verification."
                if phase7c_status_current
                else "The current v1.2.69 route in §9 records Phase 7C contract work in progress and the candidate pending independent exact-head review."
                if phase7c_candidate_current
                else "The current v1.2.68 route records the same Phase 7B and Phase 7C state."
            ),
            "Proof classification remains NOT FINALISED",
            "Phase 8/application implementation remains UNAUTHORISED",
        )
        if reconciliation_certified_current
        else
        (
            "Historical execution and Engineering Standards Authority Promotion remain COMPLETE / CERTIFIED.",
            "FP-001 PMR reconciliation is COMPLETE / CERTIFIED under PR #67.",
            "Identity v0.1.4 is COMPLETE / CERTIFIED / CURRENT under PR #77",
            "Communications v0.1.0 is COMPLETE / CERTIFIED / CURRENT under PR #81",
            "Audit & Evidence v0.1.0 is REQUIRED / COMPLETE / CERTIFIED / CURRENT following PR #119.",
            "At the v1.2.65 predecessor point the dossier set was disposition-complete and Phase 7B reconciliation was NEXT / NOT_STARTED.",
            "The current v1.2.66 candidate state is recorded in §12.23.",
            "Phase 7C remains BLOCKED / NOT_STARTED",
            "proof classification remains NOT FINALISED",
            "Phase 8/application implementation remains UNAUTHORISED",
        )
        if reconciliation_candidate_current
        else (
            "Engineering Standards Authority Promotion is COMPLETE / CERTIFIED under `reference/ENGINEERING_STANDARDS_v1.0.1.md`",
            "FP-001 PMR reconciliation is COMPLETE / CERTIFIED under PR #67",
            "Identity v0.1.4 is COMPLETE / CERTIFIED / CURRENT under the separate PR #77 status successor",
            "PR #76 candidate certification and completed post-merge certification evidence are COMPLETE; the separate PR #77 status successor records Identity v0.1.4 as COMPLETE / CERTIFIED / CURRENT.",
            "Communications JIT Domain Dossier v0.1.0 is COMPLETE / CERTIFIED / CURRENT under the separate PR #81 status successor",
            "Audit & Evidence v0.1.0 is REQUIRED / COMPLETE / CERTIFIED / CURRENT"
            if audit_promotion_current
            else "Audit & Evidence is REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING under tracker #116"
            if audit_work_start_current
            else "Audit & Evidence is REQUIRED / NEXT / NOT_STARTED",
            "Phase 7C remains BLOCKED / NOT_STARTED until successful Phase 7B reconciliation; Audit dossier authorship and current status are complete"
            if audit_promotion_current
            else "Phase 7C remains BLOCKED / NOT_STARTED until Audit dossier is COMPLETE / CERTIFIED / CURRENT and Phase 7B reconciliation succeeds"
            if adjudication_current
            else "Phase 7C remains blocked / not started",
            "proof classification remains NOT FINALISED" if adjudication_current else "proof classification remains not finalised",
            "executable development remains UNAUTHORISED until Phase 8 entry conditions pass"
            if adjudication_current
            else "executable development remains blocked until Phase 8 entry conditions pass",
        )
    )
    if any(harden_section.count(line) != 1 for line in required_harden_status):
        return False, "Open Work current HARDEN status section has stale promotion status or altered downstream gates"
    if audit_work_start_current:
        lifecycle_phrase = (
            "Audit & Evidence v0.1.0 is REQUIRED / COMPLETE / CERTIFIED / CURRENT following PR #119"
            if reconciliation_certified_current
            else
            "Audit & Evidence v0.1.0 is REQUIRED / COMPLETE / CERTIFIED / CURRENT following PR #119"
            if reconciliation_candidate_current
            else "PR #118 candidate certification and post-merge evidence are COMPLETE; Audit & Evidence v0.1.0 is REQUIRED / COMPLETE / CERTIFIED / CURRENT"
            if audit_promotion_current
            else "candidate v0.1.0 is authored and review-ready in PR #118 but remains NOT CERTIFIED / NOT CURRENT"
            if audit_candidate_review_current
            else "the candidate is not authored, certified or current"
        )
        next_phrase = (
            "The historical v1.2.70 route in §9 recorded Phase 7C and Final Feature Pack Contract v0.1.0 as COMPLETE / CERTIFIED / CURRENT after that status successor merged"
            if phase7c_status_current
            else "The current v1.2.69 route in §9 records Phase 7C contract work in progress and the candidate pending independent exact-head review"
            if phase7c_candidate_current
            else "The current v1.2.68 route records the same Phase 7B and Phase 7C state"
            if reconciliation_certified_current
            else
            "current v1.2.66 candidate state is recorded in §12.23"
            if reconciliation_candidate_current
            else "Phase 7B reconciliation is NEXT / NOT_STARTED"
            if audit_promotion_current
            else "fresh independent exact-head review/certification is next"
            if audit_candidate_review_current
            else "candidate authoring and review are next"
        )
        if lifecycle_phrase.casefold() not in harden_section.casefold() or next_phrase.casefold() not in harden_section.casefold():
            return False, "Open Work current HARDEN status section advances or misstates the Audit candidate lifecycle"
    if "Engineering Standards Authority Promotion is NEXT / AUTHORISED / NOT STARTED" in harden_section:
        return False, "Open Work current HARDEN status section retains the pre-certification Standards route"

    if not harden:
        return False, "current HARDEN status successor is missing"
    harden_route = _markdown_h2_section(
        harden, "21. Current execution certification and next stage"
    )
    if harden_route is None:
        harden_route = _markdown_h2_section(
            harden,
            "21. Current execution certification and next stage (historical v0.5.18 predecessor state)",
        )
    if harden_route is None:
        return False, "current HARDEN successor has no current route section"
    required_harden_route = (
        (
            "HARDEN-02 execution, Engineering Standards Authority Promotion, FP-001 PMR reconciliation and Identity dossier v0.1.4 remain COMPLETE / CERTIFIED."
            if reconciliation_certified_current
            else "Engineering Standards Authority Promotion, FP-001 PMR reconciliation and Identity dossier v0.1.4 are COMPLETE / CERTIFIED"
        ),
        "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
        "IDENTITY v0.1.4 CURRENT-STATUS PROMOTION SOURCE: PR #77 STATUS SUCCESSOR; PR #76 CANDIDATE AND POST-MERGE CERTIFICATION EVIDENCE: COMPLETE",
        "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
        "COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0",
    )
    if any(value not in harden_route for value in required_harden_route):
        return False, "current HARDEN successor does not route the certified promotion to FP-001"
    if "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION" in harden_route:
        return False, "current HARDEN successor starts or misroutes Communications"
    if reconciliation_certified_current:
        required_phase_route = ["PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT"]
        if hard_stop_current:
            required_phase_route.extend((
                "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
                "FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
                "NEXT STAGE: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
                "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
                "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
            ))
        elif classification_current:
            required_phase_route.extend((
                "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
                "FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
                "NEXT STAGE: DEVELOPMENT ENTRY HARD STOP EVALUATION",
                "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
            ))
        elif phase7c_status_current:
            required_phase_route.extend((
                "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
                "FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
                "NEXT STAGE: ARCHITECTURAL PROOF CLASSIFICATION; STATUS: NEXT / NOT PERFORMED",
                "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
            ))
        elif phase7c_candidate_current:
            required_phase_route.extend((
                "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
                "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE; STATUS: PENDING",
                "FINAL FEATURE PACK CONTRACT v0.1.0: CANDIDATE / NOT CERTIFIED / NOT CURRENT",
            ))
        else:
            required_phase_route.extend((
                "PHASE 7C: NEXT / NOT_STARTED",
                "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT; STATUS: NOT_STARTED",
            ))
        if any(value not in harden_route for value in required_phase_route):
            return False, "current HARDEN successor omits the completed Phase 7B or candidate-only Phase 7C route"
    elif "PHASE 7C: BLOCKED / NOT_STARTED" not in harden_route:
        return False, "current HARDEN successor unblocks Phase 7C"
    if audit_promotion_current and (
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT" not in harden_route
        or (
            "NEXT STAGE: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION"
            if hard_stop_current
            else "NEXT STAGE: DEVELOPMENT ENTRY HARD STOP EVALUATION"
            if classification_current
            else "NEXT STAGE: ARCHITECTURAL PROOF CLASSIFICATION"
            if phase7c_status_current
            else "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE"
            if phase7c_candidate_current
            else "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT; STATUS: NOT_STARTED"
            if reconciliation_certified_current
            else "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
            if reconciliation_candidate_current
            else "NEXT STAGE: FP-001 PHASE 7B RECONCILIATION"
        ) not in harden_route
        or (
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT"
            if reconciliation_certified_current
            else "PHASE 7B RECONCILIATION: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if reconciliation_candidate_current
            else "PHASE 7B RECONCILIATION: NEXT / NOT_STARTED"
        ) not in harden_route
    ):
        return False, "current HARDEN successor omits the completed Audit dossier or Phase 7B reconciliation route"
    if audit_work_start_current and not audit_promotion_current and (
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING" not in harden_route
        or (
            "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION" if audit_candidate_review_current
            else "AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE"
        ) not in harden_route
    ):
        return False, "current HARDEN successor omits the Audit work-start status or candidate authoring route"
    if classification_current or hard_stop_current:
        required_classification_route = (
            "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
            "REUSE_EXISTING_PROOF: NOT SELECTED",
            "TRACER BULLET ID: NONE / NOT CREATED",
            "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
            *(
                (
                    "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
                    "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
                    "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
                )
                if hard_stop_current
                else ("REMAINING DEVELOPMENT ENTRY HARD STOP CONDITIONS: NOT EVALUATED / MUST PASS BEFORE PHASE 8",)
            ),
        )
        if any(value not in harden_route for value in required_classification_route):
            return False, "current HARDEN successor omits the selected proof vehicle or its fail-closed downstream gates"
    elif "PROOF CLASSIFICATION: NOT FINALISED" not in harden_route:
        return False, "current HARDEN successor finalises proof classification"
    expected_development_gate = (
        "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET; PHASE 9 VERTICAL SLICES AND BROAD FP-001 IMPLEMENTATION REMAIN UNAUTHORISED"
        if hard_stop_current
        else "EXECUTABLE DEVELOPMENT: UNAUTHORISED; CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9; ALL OTHER APPLICABLE DEVELOPMENT ENTRY HARD STOP CONDITIONS REQUIRE INDEPENDENT EVALUATION"
        if classification_current
        else "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED"
        if audit_work_start_current
        else "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS"
    )
    if expected_development_gate not in harden_route:
        return False, "current HARDEN successor authorises Phase 8 or implementation"
    if "STORE / CER: EXCLUDED FROM HARDEN-02" not in harden_route:
        return False, "current HARDEN successor includes Store/CER"

    return True, (
        "Development Entry Hard Stop is PASS; bounded Phase 8 Architectural Proof is authorised and NEW_TRACER_BULLET proof contract/task definition is next"
        if hard_stop_current
        else "Phase 7C and the Final Feature Pack Contract remain complete, certified and current; classification is finalised as NEW_TRACER_BULLET and Development Entry Hard Stop evaluation is next"
        if classification_current
        else
        "Phase 7C and the Final Feature Pack Contract remain complete, certified and current after PR #126 resulting-main verification; proof classification is next and Phase 8 remains unauthorised"
        if phase7c_status_current
        else "Phase 7C contract candidate remains in progress and review-only after certified Phase 7B reconciliation"
        if phase7c_candidate_current
        else "certified Phase 7B reconciliation routes NEXT to the unstarted Phase 7C Final Feature Pack Contract"
        if reconciliation_certified_current
        else "certified Engineering Standards, FP-001 reconciliation and Identity promotion route NEXT to the Audit & Evidence JIT Domain Dossier"
        if adjudication_current
        else "certified Engineering Standards, FP-001 reconciliation and Identity promotion route NEXT to the Communications JIT Domain Dossier"
    )


def _engineering_standards_lifecycle_state(
    root: Path,
    manifest: dict[str, Any],
    readme: str,
    open_work: str,
    harden: str,
) -> tuple[bool, str]:
    """Accept the current candidate predecessor or its fully certified successor."""

    active_entries = [
        entry
        for key in ("governing_documents", "reference_documents")
        for entry in manifest.get(key, [])
        if "ENGINEERING_STANDARDS" in (
            str(entry.get("document_id", ""))
            + str(entry.get("authority_class", ""))
            + str(entry.get("repository_path", ""))
        ).upper()
        and entry.get("lifecycle", "current") != "historical"
    ]
    if (
        len(active_entries) == 1
        and active_entries[0].get("document_id") == "ENGINEERING_STANDARDS_CANDIDATE"
        and active_entries[0].get("lifecycle") == "candidate"
    ):
        return _engineering_standards_promotion_state(root, manifest, readme, open_work, harden)
    return _engineering_standards_certified_state(root, manifest, readme, open_work, harden)

def _section_body(text: str, heading_pattern: str) -> str:
    match = re.search(heading_pattern, text, re.MULTILINE)
    if match is None:
        return ""
    next_heading = re.search(r"^## ", text[match.end() :], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading is not None else len(text)
    return text[match.end() : end]


def _markdown_h2_section(text: str, title: str) -> str | None:
    """Return one exact ATX H2 section body, stopping at the next peer H2."""

    heading = re.compile(
        rf"(?m)^ {{0,3}}##[ \t]+{re.escape(title)}(?:[ \t]+#+)?[ \t]*\r?$"
    )
    matches = list(heading.finditer(text))
    if len(matches) != 1:
        return None

    start = matches[0].end()
    next_h2 = re.search(r"(?m)^ {0,3}##[ \t]+", text[start:])
    end = start + next_h2.start() if next_h2 is not None else len(text)
    return text[start:end]


def _bundle_component_allocation_issues(
    product: str,
    decisions: str,
    requirements: dict[str, Any],
) -> list[str]:
    issues: list[str] = []
    matrix_name = requirements.get("matrix")
    expected_rules = requirements.get("rules")
    if not isinstance(matrix_name, str) or not isinstance(expected_rules, dict):
        return ["bundle component allocation audit requirements are incomplete"]

    section = _section_body(product, r"^## 21R\.1\b[^\n]*\n")
    rows = _marked_matrix_rows(section, matrix_name)
    allocation_rules = {
        row.get("invariant", ""): row.get("governed rule", "")
        for row in rows
    }
    if set(allocation_rules) != set(expected_rules):
        issues.append("bundle allocation matrix has missing, duplicate or unexpected invariants")
    for invariant, required_terms in expected_rules.items():
        rule_text = allocation_rules.get(invariant, "")
        if not isinstance(required_terms, list) or any(
            not isinstance(term, str) or term not in rule_text for term in required_terms
        ):
            issues.append(f"bundle allocation invariant {invariant} is missing a required rule")

    decision_section = _section_body(decisions, r"^## DEC-299\b[^\n]*\n")
    decision_terms = requirements.get("decision_terms", [])
    if not isinstance(decision_terms, list) or any(
        not isinstance(term, str) or term.casefold() not in decision_section.casefold()
        for term in decision_terms
    ):
        issues.append("DEC-299 does not carry the complete versioned bundle allocation rule")

    example = requirements.get("launch_example")
    price_section = _section_body(product, r"^## 21L\.15\b[^\n]*\n")
    decision_price_section = _section_body(decisions, r"^## DEC-282\b[^\n]*\n")
    if not isinstance(example, dict) or any(
        not isinstance(example.get(key), int)
        for key in ("assessment", "plan", "discount", "bundle")
    ):
        issues.append("bundle launch-price reconciliation requirements are incomplete")
    else:
        assessment = example["assessment"]
        plan = example["plan"]
        discount = example["discount"]
        bundle = example["bundle"]
        launch_rule = allocation_rules.get("launch_bundle", "")
        expected_equation = (
            f"R{assessment}_assessment + R{plan}_plan - R{discount}_bundle_discount "
            f"= R{bundle}_accepted_bundle_amount"
        )
        if assessment + plan - discount != bundle or expected_equation not in launch_rule:
            issues.append("launch_bundle allocation example does not reconcile arithmetically")
        for amount in (assessment, plan, bundle):
            marker = f"R{amount}"
            if marker not in price_section or marker not in decision_price_section:
                issues.append(f"launch bundle amount {marker} differs from locked list-price authority")
                break
        discount_marker = f"R{discount}"
        if discount_marker not in price_section:
            issues.append(f"launch bundle discount {discount_marker} is absent from Product Law")

    return issues


def _feature_pack_propagation_issues(
    roadmap: str,
    requirements: dict[str, Any],
) -> list[str]:
    issues: list[str] = []
    if not requirements:
        return ["feature-pack hardening requirements are missing"]

    matches = list(re.finditer(r"^## (FP-\d{3})\s+—", roadmap, re.MULTILINE))
    sections: dict[str, str] = {}
    counts: dict[str, int] = {}
    for index, match in enumerate(matches):
        pack_id = match.group(1)
        counts[pack_id] = counts.get(pack_id, 0) + 1
        end = matches[index + 1].start() if index + 1 < len(matches) else len(roadmap)
        sections[pack_id] = roadmap[match.start() : end]

    for pack_id, rule in requirements.items():
        section = sections.get(pack_id, "")
        if counts.get(pack_id) != 1:
            issues.append(f"{pack_id} must have one Roadmap contract section")
            continue
        authority_match = re.search(
            r"^\*\*Product Authority:\*\*\s*(.*)$", section, re.MULTILINE
        )
        contract_match = re.search(
            r"^\*\*Product Hardening Contract:\*\*\s*(.*)$", section, re.MULTILINE
        )
        if authority_match is None:
            issues.append(f"{pack_id} is missing its Product Authority declaration")
            continue
        if contract_match is None:
            issues.append(f"{pack_id} is missing its Product Hardening Contract")
            continue

        authority = authority_match.group(1)
        for section_ref in rule.get("sections", []):
            required_section = re.fullmatch(r"(\d+[A-Z])\.(\d+)", section_ref)
            section_is_cited = section_ref in authority
            if required_section is not None and not section_is_cited:
                required_family, required_number = required_section.group(1), int(required_section.group(2))
                for span in re.finditer(
                    r"(?P<start_family>\d+[A-Z])\.(?P<start>\d+)\s*[–—-]\s*"
                    r"(?:(?P<end_family>\d+[A-Z])\.)?(?P<end>\d+)",
                    authority,
                ):
                    end_family = span.group("end_family") or span.group("start_family")
                    if (
                        span.group("start_family") == required_family == end_family
                        and int(span.group("start")) <= required_number <= int(span.group("end"))
                    ):
                        section_is_cited = True
                        break
            if not section_is_cited:
                issues.append(f"{pack_id} does not cite §{section_ref}")
        for decision in rule.get("decisions", []):
            if re.search(rf"(?<![A-Za-z0-9-]){re.escape(decision)}(?!\d)", authority) is None:
                issues.append(f"{pack_id} does not cite {decision}")

        contract_tokens = set(re.findall(r"`([^`]+)`", contract_match.group(1)))
        for outcome in rule.get("outcomes", []):
            if outcome not in contract_tokens:
                issues.append(f"{pack_id} is missing product outcome {outcome}")

    return issues


def _has_oq034_fp_blocker(documents: list[str]) -> bool:
    return any(
        "OQ-034" in line and "BLOCKS_THIS_FP" in line
        for document in documents
        for line in document.splitlines()
    )


def _check_product_semantics(
    root: Path,
    entries: list[dict[str, Any]],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    by_id = {
        str(entry.get("document_id")): entry
        for entry in entries
        if entry.get("lifecycle", "current") != "historical"
    }
    product = _read_entry_text(root, by_id.get("PLATFORM_BASELINE"))
    decisions = _read_entry_text(root, by_id.get("DECISION_REGISTER"))
    open_work = _read_entry_text(root, by_id.get("OPEN_WORK"))
    roadmap = _read_entry_text(root, by_id.get("ROADMAP"))
    roots = integrity_rules["document_roots"]
    readme_path = root / roots["context_index"]
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    phase8_routes = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {}).get("current_routes", {})
    skeleton_relative = phase8_routes.get("fp001_skeleton") if isinstance(phase8_routes, dict) else None
    if not isinstance(skeleton_relative, str):
        skeleton_relative = next(
            (
                str(path)
                for path in integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])
                if Path(str(path)).name.startswith("FP-001_FEATURE_PACK_SKELETON_WORKING_")
                and "/archive/" not in f"/{path}"
            ),
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
        )
    fp001_path = root / skeleton_relative
    fp001 = fp001_path.read_text(encoding="utf-8") if fp001_path.is_file() else ""
    atlas_relative_path = (
        phase8_routes.get("delivery_atlas")
        if isinstance(phase8_routes, dict)
        else None
    )
    if not isinstance(atlas_relative_path, str):
        atlas_relative_path = next(
            (
                str(path)
                for path in integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])
                if Path(str(path)).name.startswith("DELIVERY_ATLAS_WORKING_")
                and "/archive/" not in f"/{path}"
            ),
            "",
        )
    atlas_path = root / atlas_relative_path if atlas_relative_path else None
    atlas = atlas_path.read_text(encoding="utf-8") if atlas_path is not None and atlas_path.is_file() else ""

    eligibility_rows = _marked_matrix_rows(product, "ELIGIBILITY-PAID-PLAN")
    eligibility = {row.get("case", ""): row for row in eligibility_rows}
    eligibility_cases = {
        "eligible_automated",
        "insufficient_information",
        "professional_review_required",
        "general_wellness_only",
        "terminal_unfulfillable_outcome",
    }
    eligibility_ok = eligibility_cases <= eligibility.keys() and all(
        token in eligibility.get(case, {}).get(field, "")
        for case, field, token in (
            ("eligible_automated", "entitlement consequence", "consume_on_successful_delivery"),
            ("eligible_automated", "entitlement consequence", "technical_failure=preserve_unconsumed"),
            ("insufficient_information", "entitlement consequence", "held_unconsumed"),
            ("insufficient_information", "entitlement consequence", "no_expiry_for_incomplete_information"),
            ("professional_review_required", "entitlement consequence", "held_unconsumed_pending_review"),
            ("general_wellness_only", "commercial consequence", "not_personalised_plan_fulfilment"),
            ("terminal_unfulfillable_outcome", "commercial consequence", "refund_allocated_plan_component"),
        )
    )
    _record_check(
        report,
        "eligibility_commercial_consequences",
        eligibility_ok,
        "paid-plan rights are held or consumed by governed eligibility and delivery outcome"
        if eligibility_ok
        else "paid-plan eligibility matrix is missing required outcomes or entitlement/refund consequences",
        path=str(by_id.get("PLATFORM_BASELINE", {}).get("repository_path", "")),
    )

    reversal_rows = _marked_matrix_rows(product, "COMMERCIAL-REVERSAL")
    reversals = {row.get("case", ""): row for row in reversal_rows}
    reversal_cases = {
        "refund_before_entitlement_use",
        "plan_refund_before_generation",
        "verified_technical_failure_refund",
        "duplicate_payment_refund",
        "membership_duplicate_billing_refund",
        "unverified_provider_signal",
        "confirmed_disputed_chargeback",
        "chargeback_payment_restored",
        "final_lost_chargeback",
        "post_delivery_full_reversal",
    }
    reversal_ok = reversal_cases <= reversals.keys() and all(
        "preserve_historical_record" in row.get("historical record consequence", "")
        for row in reversals.values()
    ) and all(
        token in reversals.get(case, {}).get("entitlement/access consequence", "")
        for case, token in (
            ("refund_before_entitlement_use", "end_refunded_component"),
            ("duplicate_payment_refund", "preserve_one_valid_right"),
            ("unverified_provider_signal", "no_entitlement_mutation"),
            ("confirmed_disputed_chargeback", "suspend_after_commerce_confirmation"),
            ("chargeback_payment_restored", "restore_idempotently"),
            ("final_lost_chargeback", "end_paid_access"),
            ("post_delivery_full_reversal", "exceptional_full_refund_ends_current_access"),
        )
    )
    _record_check(
        report,
        "commercial_reversal_consequences",
        reversal_ok,
        "verified commercial reversals control access while preserving historical records"
        if reversal_ok
        else "commercial reversal matrix is missing required cases or current-access/history consequences",
        path=str(by_id.get("PLATFORM_BASELINE", {}).get("repository_path", "")),
    )

    consent_rows = _marked_matrix_rows(product, "CONSENT-WITHDRAWAL")
    consent = {row.get("event", ""): row for row in consent_rows}
    consent_cases = {
        "personalisation_withdrawal",
        "automated_recommendation_withdrawal",
        "practitioner_sharing_withdrawal",
        "optional_ai_withdrawal",
        "health_storage_withdrawal",
        "full_account_deletion",
    }
    consent_ok = consent_cases <= consent.keys() and all(
        bool(row.get("future processing"))
        and bool(row.get("delivered plan access"))
        and bool(row.get("commercial entitlement"))
        for row in consent.values()
    ) and all(
        token in consent.get(case, {}).get(field, "")
        for case, field, token in (
            ("personalisation_withdrawal", "future processing", "stop_affected_future_processing"),
            ("practitioner_sharing_withdrawal", "delivered plan access", "practitioner_access_ends"),
            ("health_storage_withdrawal", "future processing", "independent_lawful_basis"),
            ("health_storage_withdrawal", "delivered plan access", "restrict_access"),
            ("full_account_deletion", "delivered plan access", "end_ordinary_access"),
        )
    )
    _record_check(
        report,
        "consent_withdrawal_consequences",
        consent_ok,
        "purpose withdrawal, delivered access and commercial rights have separate consequences"
        if consent_ok
        else "consent matrix is missing an event or fails to distinguish future processing, delivered access and entitlement",
        path=str(by_id.get("PLATFORM_BASELINE", {}).get("repository_path", "")),
    )

    provenance_rows = _marked_matrix_rows(product, "TEMPERAMENT-PROVENANCE")
    provenance = {row.get("provenance", ""): row for row in provenance_rows}
    provenance_cases = {"self_reported", "book_derived", "digitally_assessed", "later_digital_completion"}
    provenance_ok = provenance_cases <= provenance.keys() and all(
        provenance.get(case, {}).get(field) == "no"
        for case in ("self_reported", "book_derived")
        for field in ("exact digital scores", "paid digital report")
    ) and all(
        provenance.get(case, {}).get(field) == "unused"
        for case in ("self_reported", "book_derived")
        for field in ("included assessment credit",)
    ) and provenance.get("digitally_assessed", {}).get("exact digital scores") == "yes" and provenance.get(
        "digitally_assessed", {}
    ).get("paid digital report") == "yes" and "preserve_prior_provenance" in provenance.get(
        "later_digital_completion", {}
    ).get("result history", "")
    _record_check(
        report,
        "temperament_provenance_outputs",
        provenance_ok,
        "assessment outputs and reports follow declared versus digital result provenance"
        if provenance_ok
        else "temperament provenance matrix permits a report/score mismatch or overwrites prior provenance",
        path=str(by_id.get("PLATFORM_BASELINE", {}).get("repository_path", "")),
    )

    purchase_rows = _marked_matrix_rows(product, "ASSESSMENT-PURCHASE-USE")
    purchases = {row.get("case", ""): row for row in purchase_rows}
    purchase_cases = {
        "standalone_purchase_without_unused_credit",
        "standalone_purchase_with_unused_paid_credit",
        "purchase_when_annual_use_interval_blocks_attempt",
        "bundle_purchase_with_unused_paid_credit",
        "premium_annual_reassessment_credit",
        "plan_only_purchase_with_assessment_credit",
    }
    purchase_ok = purchase_cases <= purchases.keys() and all(
        row.get("maximum active unused ordinary paid credits") == "one"
        for case, row in purchases.items()
        if case != "premium_annual_reassessment_credit"
    ) and all(
        token in purchases.get(case, {}).get("purchase eligibility", "")
        for case, token in (
            ("standalone_purchase_with_unused_paid_credit", "reject"),
            ("purchase_when_annual_use_interval_blocks_attempt", "reject"),
            ("bundle_purchase_with_unused_paid_credit", "route_to_approved_plan_only_offer"),
            ("plan_only_purchase_with_assessment_credit", "independent_of_assessment_credit"),
        )
    ) and "non_accumulating" in purchases.get("premium_annual_reassessment_credit", {}).get(
        "Premium credit rule", ""
    )
    _record_check(
        report,
        "assessment_purchase_governance",
        purchase_ok,
        "assessment sale credits, attempts, annual interval and Premium credit are distinct"
        if purchase_ok
        else "assessment purchase matrix does not enforce the active-credit limit and separate Premium rule",
        path=str(by_id.get("PLATFORM_BASELINE", {}).get("repository_path", "")),
    )

    decision_match = re.search(
        r"^## OQ-034[^\n]*\n\*\*Status:\*\* ([^\n]+)", decisions, re.MULTILINE
    )
    no_blocking_reference = (
        atlas_path is not None
        and atlas_path.is_file()
        and not _has_oq034_fp_blocker([roadmap, fp001, atlas])
    )
    proof_is_downstream = all(
        "phase 8" in document.lower()
        and "proof" in document.lower()
        and re.search(r"proof[^\n]{0,100}(not complete|not finalised|not finalized|incomplete)", document.lower())
        for document in (roadmap, fp001)
    )
    identity_pmr_gate = next(
        (line for line in roadmap.splitlines() if "Verified account + required PMR" in line),
        "",
    )
    major_gate_lines = [
        line for line in roadmap.splitlines() if line.lower().startswith("**major gates")
    ]
    oq_ok = bool(
        decision_match
        and "RESOLVED / ARCHITECTURE SELECTION" in decision_match.group(1)
        and no_blocking_reference
        and proof_is_downstream
        and identity_pmr_gate
        and "OQ-034" not in identity_pmr_gate
        and major_gate_lines
        and not any("OQ-034" in line for line in major_gate_lines)
    )
    _record_check(
        report,
        "resolved_oq_not_blocking",
        oq_ok,
        "OQ-034 selection is resolved without claiming Phase 8 proof complete or finalised"
        if oq_ok
        else "OQ-034 is absent/resolved incorrectly, still blocks a pack, or its Phase 8 proof state is overstated",
        path=str(by_id.get("ROADMAP", {}).get("repository_path", "")),
    )

    contract = ""
    contract_route = re.search(
        r"(?m)^CURRENT HARDEN-02 STATUS SUCCESSOR:\s*([^;\s]+)",
        open_work,
    )
    if contract_route:
        contract_path = root / "docs/00_platform" / contract_route.group(1)
        if contract_path.is_file():
            contract = contract_path.read_text(encoding="utf-8")
    h02_ok, h02_message = _h02_lifecycle_state(open_work, readme, contract)
    _record_check(
        report,
        "harden_02_lifecycle_state",
        h02_ok,
        h02_message,
        path=str(by_id.get("OPEN_WORK", {}).get("repository_path", "")),
    )

    allocation_issues = _bundle_component_allocation_issues(
        product,
        decisions,
        integrity_rules.get("product_hardening_bundle_allocation_requirements", {}),
    )
    _record_check(
        report,
        "bundle_component_allocation_governance",
        not allocation_issues,
        "bundle allocations are versioned before sale, disclosed, reconciled and snapshotted for component refunds"
        if not allocation_issues
        else "; ".join(allocation_issues),
        path=str(by_id.get("PLATFORM_BASELINE", {}).get("repository_path", "")),
    )

    pack_issues = _feature_pack_propagation_issues(
        roadmap,
        integrity_rules.get("product_hardening_feature_pack_requirements", {}),
    )
    _record_check(
        report,
        "product_hardening_feature_pack_propagation",
        not pack_issues,
        "affected Feature Packs cite and carry their DEC-299…303 product outcomes"
        if not pack_issues
        else "; ".join(pack_issues),
        path=str(by_id.get("ROADMAP", {}).get("repository_path", "")),
    )


def _current_authority_north_star_stop_condition(text: str) -> str:
    start_marker = "# 24. Document Stop Condition"
    end_marker = "**Implementation STOP:**"
    start = re.search(rf"(?m)^{re.escape(start_marker)}\s*$", text)
    if start is None:
        return ""
    end = re.search(re.escape(end_marker), text[start.end() :])
    return text[start.end() : start.end() + end.start()] if end is not None else ""


def _current_authority_state_section(
    text: str,
    document_id: str,
) -> str:
    section_markers = CURRENT_AUTHORITY_STATE_SECTIONS.get(document_id)
    if section_markers is None:
        return ""
    start_marker, end_marker = section_markers
    start = re.search(rf"(?m)^{re.escape(start_marker)}\s*$", text)
    if start is None:
        return ""
    if end_marker is not None:
        end = re.search(rf"(?m)^{re.escape(end_marker)}\s*$", text[start.end() :])
        return text[start.end() : start.end() + end.start()] if end is not None else ""
    return text[start.end() :]


def _readme_current_authority_filenames(text: str) -> list[str]:
    start = text.find("## Default Agent Context")
    if start < 0:
        return []
    section = text[start:]
    end = re.search(r"^##\s+", section[len("## Default Agent Context") :], re.MULTILINE)
    if end is not None:
        section = section[: len("## Default Agent Context") + end.start()]
    return re.findall(r"(?m)^\s*\d+\.\s+`([^`]+)`", section)


def _current_authority_entries(
    manifest: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    current_governing = {
        str(entry.get("document_id")): entry
        for entry in manifest.get("governing_documents", [])
        if isinstance(entry, dict) and entry.get("lifecycle", "current") != "historical"
    }
    by_filename = {
        str(entry.get("canonical_filename")): entry
        for entry in current_governing.values()
        if entry.get("canonical_filename")
    }
    return current_governing, by_filename


def _check_current_authority_self_versions(
    root: Path,
    manifest: dict[str, Any],
    report: dict[str, Any],
) -> None:
    current_governing, _ = _current_authority_entries(manifest)
    target_entries = [
        current_governing[document_id]
        for document_id in CURRENT_AUTHORITY_STATE_SECTIONS
        if document_id in current_governing
    ]
    if not target_entries:
        return

    issues: list[str] = []
    issue_paths: list[str] = []
    for entry in target_entries:
        document_id = str(entry.get("document_id"))
        relative = _relative_path(entry)
        path = _entry_path(root, entry)
        expected_version = str(entry.get("semver", ""))
        if not path.is_file():
            issues.append(f"{document_id}: current artifact is missing at {relative}")
            issue_paths.append(relative)
            continue
        text = path.read_text(encoding="utf-8")
        declared_version = _declared_document_version(text)
        filename_version = VERSION_PATTERN.search(str(entry.get("canonical_filename", "")))
        if declared_version != expected_version or filename_version is None or filename_version.group(1) != expected_version:
            issues.append(
                f"{document_id}: self-version is {declared_version!r} with manifest {expected_version!r}"
            )
            issue_paths.append(relative)

        active = _current_authority_state_section(text, document_id)
        if document_id == "PROJECT_NORTH_STAR_AND_MVP":
            stop_condition = _current_authority_north_star_stop_condition(text)
            current_state_versions = re.findall(
                r"(?i)Current Product Law / governance-alignment condition:\s+MET\s+\(v(\d+\.\d+\.\d+)\)",
                stop_condition,
            )
            if current_state_versions != [expected_version]:
                issues.append(
                    f"{document_id}: active governance-alignment self-state is {current_state_versions!r}, expected {expected_version!r}"
                )
                issue_paths.append(relative)
        elif document_id == "PLATFORM_BASELINE":
            current_product_versions = re.findall(
                r"(?im)^\s*Current Product Law\s+(?:is|:)\s+v?(\d+\.\d+\.\d+)\b",
                active,
            )
            if current_product_versions and any(
                version != expected_version for version in current_product_versions
            ):
                issues.append(
                    f"{document_id}: active Current Product Law versions {current_product_versions!r} do not match {expected_version!r}"
                )
                issue_paths.append(relative)

    _record_check(
        report,
        "current_authority_self_version",
        not issues,
        "current North Star and Product self-versions match their manifest entries"
        if not issues
        else "; ".join(issues),
        path=issue_paths[0] if issue_paths else "",
    )


def _check_current_authority_route_resolution(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    current_governing, by_filename = _current_authority_entries(manifest)
    target_entries = [
        current_governing[document_id]
        for document_id in CURRENT_AUTHORITY_STATE_SECTIONS
        if document_id in current_governing
    ]
    if not target_entries:
        return

    context_index = str(integrity_rules["document_roots"]["context_index"])
    readme_path = root / context_index
    readme_filenames = _readme_current_authority_filenames(
        readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    )
    issues: list[str] = []
    issue_paths: list[str] = []

    def route_matches_current_manifest_path(route_value: str, entry: dict[str, Any]) -> bool:
        route = Path(route_value)
        entry_path = Path(_relative_path(entry))
        try:
            docs_relative_entry = entry_path.relative_to("docs/00_platform")
        except ValueError:
            return False
        allowed_routes = {entry_path.as_posix(), docs_relative_entry.as_posix()}
        if docs_relative_entry.parent == Path("."):
            allowed_routes.add(entry_path.name)
        return (
            not route.is_absolute()
            and ".." not in route.parts
            and "archive" not in route.parts
            and "archive" not in entry_path.parts
            and route.as_posix() in allowed_routes
        )

    for entry in target_entries:
        document_id = str(entry.get("document_id"))
        relative = _relative_path(entry)
        path = _entry_path(root, entry)
        active = _current_authority_state_section(
            path.read_text(encoding="utf-8") if path.is_file() else "",
            document_id,
        )
        if not active:
            issues.append(f"{document_id}: active current-state section is missing or malformed")
            issue_paths.append(relative)
            continue

        route_lines = [
            line for line in active.splitlines()
            if re.search(
                r"(?i)^\s*(?:current\s+routing|current\s+product\s+law|current\s+product/decision/roadmap\s+authority)\s*(?:is|:)",
                line,
            )
        ]
        if len(route_lines) != 1:
            issues.append(
                f"{document_id}: expected one active CURRENT/current-routing field, found {len(route_lines)}"
            )
            issue_paths.append(relative)
            continue

        route_line = route_lines[0]
        route_values = CURRENT_ROUTE_FILENAME_PATTERN.findall(route_line)
        route_filenames = [Path(value).name for value in route_values]
        if document_id == "PROJECT_NORTH_STAR_AND_MVP":
            if route_filenames:
                issues.append(
                    f"{document_id}: active §23 caches versioned current-route filenames {route_filenames!r}"
                )
                issue_paths.append(relative)
            if "README" not in route_line or "CURRENT_AUTHORITY_MANIFEST" not in route_line:
                issues.append(
                    f"{document_id}: active §23 routing must delegate Product/Decision/Roadmap authority to README and CURRENT_AUTHORITY_MANIFEST"
                )
                issue_paths.append(relative)
        if document_id == "PLATFORM_BASELINE" and not route_filenames:
            current_versions = CURRENT_ROUTE_VERSION_PATTERN.findall(route_line)
            expected_version = str(entry.get("semver", ""))
            if not current_versions or any(version != expected_version for version in current_versions):
                issues.append(
                    f"{document_id}: active Current Product Law version does not resolve to manifest SemVer {expected_version!r}"
                )
                issue_paths.append(relative)
                continue
            route_filenames = [str(entry.get("canonical_filename", ""))]
            route_values = route_filenames
        if document_id == "PLATFORM_BASELINE" and route_filenames != [str(entry.get("canonical_filename", ""))]:
            issues.append(
                f"{document_id}: Current Product Law route {route_filenames!r} does not match its manifest route {entry.get('canonical_filename')!r}"
            )
            issue_paths.append(relative)

        for route_value, filename in zip(route_values, route_filenames):
            routed_entry = by_filename.get(filename)
            if routed_entry is None:
                issues.append(
                    f"{document_id}: active route {filename!r} is not a current manifest route"
                )
                issue_paths.append(relative)
                continue
            if filename not in readme_filenames:
                issues.append(
                    f"{document_id}: active route {filename!r} is absent from README current authority"
                )
                issue_paths.append(relative)
                continue
            if not route_matches_current_manifest_path(route_value, routed_entry):
                issues.append(
                    f"{document_id}: active route {route_value!r} does not resolve to the current manifest path {routed_entry.get('repository_path')!r}"
                )
                issue_paths.append(relative)

    def record_current_routes(
        document_id: str,
        relative: str,
        routed_names: list[str],
        expected_names: list[str],
        route_values: list[str],
    ) -> None:
        if routed_names != expected_names:
            issues.append(
                f"{document_id}: explicitly current routes {routed_names!r} do not match manifest routes {expected_names!r}"
            )
            issue_paths.append(relative)
        for route_value, filename in zip(route_values, routed_names):
            if filename not in by_filename:
                issues.append(f"{document_id}: active route {filename!r} is not a current manifest route")
                issue_paths.append(relative)
            elif filename not in readme_filenames:
                issues.append(f"{document_id}: active route {filename!r} is absent from README current authority")
                issue_paths.append(relative)
            else:
                if not route_matches_current_manifest_path(route_value, by_filename[filename]):
                    issues.append(
                        f"{document_id}: active route {route_value!r} does not resolve to the current manifest path {_relative_path(by_filename[filename])!r}"
                    )
                    issue_paths.append(relative)

    expected_product_authority = [
        str(current_governing[document_id].get("canonical_filename", ""))
        for document_id in ("PROJECT_NORTH_STAR_AND_MVP", "PLATFORM_BASELINE", "DECISION_REGISTER")
        if document_id in current_governing
    ]
    complete_authority_inventory = {
        "PROJECT_NORTH_STAR_AND_MVP", "PLATFORM_BASELINE", "DECISION_REGISTER", "OPEN_WORK",
        "ARCHITECTURE_SYNTHESIS", "DOMAIN_MAP", "ROADMAP", "PLATFORM_OPERATING_MODEL",
        "FRONTEND_EXPERIENCE_SYSTEM",
    }.issubset(current_governing)
    graph_rules = integrity_rules.get("graph_rules", {})
    roadmap_entry = current_governing.get("ROADMAP")
    if roadmap_entry is not None:
        relative = _relative_path(roadmap_entry)
        path = _entry_path(root, roadmap_entry)
        roadmap_text = path.read_text(encoding="utf-8") if path.is_file() else ""
        header = roadmap_text.split("## Amendment summary", 1)[0]
        current_authority_lines = re.findall(
            r"(?m)^-\s+\*\*Current Product authority:\*\*\s*(.+)$",
            header,
        )
        route_values = CURRENT_ROUTE_FILENAME_PATTERN.findall(current_authority_lines[0]) if len(current_authority_lines) == 1 else []
        route_names = [Path(filename).name for filename in route_values]
        if len(current_authority_lines) == 1 or complete_authority_inventory:
            frozen_route_exception = graph_rules.get(
                "current_route_source_at_freeze_exceptions", {}
            ).get(relative)
            if frozen_route_exception is None:
                record_current_routes("ROADMAP", relative, route_names, expected_product_authority, route_values)
            else:
                expected_hash = frozen_route_exception.get("sha256")
                if (
                    len(current_authority_lines) != 1
                    or route_names != frozen_route_exception.get("route_filenames")
                    or not path.is_file()
                    or expected_hash != sha256_file(path)
                    or expected_hash != roadmap_entry.get("sha256")
                    or not str(frozen_route_exception.get("reason", "")).strip()
                ):
                    issues.append(
                        f"ROADMAP ({relative}): invalid source-at-freeze current-route exception for the exact path and SHA-256"
                    )
                    issue_paths.append(relative)

    navigation_paths = [str(path) for path in graph_rules.get("navigation_document_paths", [])]
    working_nav_paths = [path for path in navigation_paths if path.startswith("docs/00_platform/working/")]
    readme_text = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    readme_working_section = readme_text.split("## Active Working Artifacts", 1)[-1]
    readme_working_section = re.split(r"(?m)^##\s+", readme_working_section, maxsplit=1)[0]
    readme_working_paths = set(
        re.findall(r"`(working/[^`]+\.md)`", readme_working_section)
    )
    for relative in working_nav_paths:
        working_relative = relative.removeprefix("docs/00_platform/")
        if working_relative not in readme_working_paths:
            issues.append(f"README: active working route {working_relative!r} is absent from its working-artifact list")
            issue_paths.append(context_index)

    atlas_relative = next(
        (path for path in working_nav_paths if Path(path).name.startswith("DELIVERY_ATLAS_WORKING_")),
        None,
    )
    if atlas_relative is not None:
        atlas_path = root / atlas_relative
        atlas_text = atlas_path.read_text(encoding="utf-8") if atlas_path.is_file() else ""
        start = atlas_text.find("# 1. Authority, purpose and boundaries")
        end = atlas_text.find("## 1.2 Purpose", start + 1) if start >= 0 else -1
        current_sources = atlas_text[start:end] if start >= 0 and end > start else ""
        source_rows: dict[str, list[str]] = {}
        for line in current_sources.splitlines():
            if not line.lstrip().startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] in {"Product Law", "Roadmap", "Planning tracker"}:
                source_rows[cells[0]] = CURRENT_ROUTE_FILENAME_PATTERN.findall(cells[1])
        expected_atlas_sources = {
            "Product Law": expected_product_authority,
            "Roadmap": [str(current_governing["ROADMAP"].get("canonical_filename", ""))]
            if "ROADMAP" in current_governing else [],
            "Planning tracker": [str(current_governing["OPEN_WORK"].get("canonical_filename", ""))]
            if "OPEN_WORK" in current_governing else [],
        }
        for label, expected_names in expected_atlas_sources.items():
            record_current_routes(
                "DELIVERY_ATLAS_WORKING",
                atlas_relative,
                [Path(route).name for route in source_rows.get(label, [])],
                expected_names,
                source_rows.get(label, []),
            )

    harden_relative = next(
        (path for path in working_nav_paths if Path(path).name.startswith("HARDEN-02_CONTRACT_WORKING_")),
        None,
    )
    harden_nav = next(
        (path for path in navigation_paths if Path(path).name.startswith("HARDEN-02_CONTRACT_WORKING_")),
        None,
    )
    if harden_relative is not None:
        harden_path = root / harden_relative
        harden_text = harden_path.read_text(encoding="utf-8") if harden_path.is_file() else ""
        authority_start = harden_text.find("### CURRENT AUTHORITY")
        authority_end = harden_text.find("### CURRENT DERIVED EVIDENCE", authority_start + 1)
        authority_section = harden_text[authority_start:authority_end] if authority_start >= 0 and authority_end > authority_start else ""
        authority_sources: list[str] = []
        for line in authority_section.splitlines():
            if line.lstrip().startswith("|") and "|---" not in line:
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if cells:
                    authority_sources.extend(CURRENT_ROUTE_FILENAME_PATTERN.findall(cells[0]))
        expected_harden_authority = [
            str(current_governing[document_id].get("canonical_filename", ""))
            for document_id in (
                "PROJECT_NORTH_STAR_AND_MVP", "PLATFORM_BASELINE", "DECISION_REGISTER",
                "OPEN_WORK", "ARCHITECTURE_SYNTHESIS", "DOMAIN_MAP", "ROADMAP",
                "PLATFORM_OPERATING_MODEL", "FRONTEND_EXPERIENCE_SYSTEM",
            )
            if document_id in current_governing
        ]
        record_current_routes(
            "HARDEN-02_CONTRACT_WORKING",
            harden_relative,
            [Path(route).name for route in authority_sources],
            expected_harden_authority,
            authority_sources,
        )

    open_work_entry = current_governing.get("OPEN_WORK")
    if open_work_entry is not None and harden_nav is not None:
        relative = _relative_path(open_work_entry)
        open_work_path = _entry_path(root, open_work_entry)
        open_work_text = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() else ""
        stage = open_work_text.split("# 9. Immediate Next Action", 1)
        stage = stage[1].split("# 10. Minimal Tools", 1)[0] if len(stage) == 2 else ""
        harden_current_lines = re.findall(
            r"(?m)^CURRENT HARDEN-02 STATUS SUCCESSOR:\s*([^;\n]+)",
            stage,
        )
        harden_current_routes = [
            value.strip().strip("`")
            for value in harden_current_lines
        ]
        expected_harden_route = harden_nav.removeprefix("docs/00_platform/")
        if harden_current_routes != [expected_harden_route] or expected_harden_route not in readme_working_paths:
            issues.append(
                f"OPEN_WORK: explicit CURRENT HARDEN route {harden_current_routes!r} does not match README/manifest navigation path {expected_harden_route!r}"
            )
            issue_paths.append(relative)

    open_work_entry = current_governing.get("OPEN_WORK")
    if open_work_entry is not None and atlas_relative is not None:
        relative = _relative_path(open_work_entry)
        open_work_path = _entry_path(root, open_work_entry)
        open_work_text = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() else ""
        stage = open_work_text.split("# 9. Immediate Next Action", 1)
        stage = stage[1].split("# 10. Minimal Tools", 1)[0] if len(stage) == 2 else ""
        atlas_lines = re.findall(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", stage)
        atlas_names = [
            Path(filename).as_posix()
            for filename in CURRENT_ROUTE_FILENAME_PATTERN.findall(atlas_lines[0])
            if filename.startswith("working/") and "DELIVERY_ATLAS_WORKING_" in filename
        ] if len(atlas_lines) == 1 else []
        expected_atlas_route = atlas_relative.removeprefix("docs/00_platform/")
        if atlas_names != [expected_atlas_route] or expected_atlas_route not in readme_working_paths:
            issues.append(
                f"OPEN_WORK: current Atlas route {atlas_names!r} does not match README/manifest navigation path {expected_atlas_route!r}"
            )
            issue_paths.append(relative)

    _record_check(
        report,
        "current_authority_route_resolution",
        not issues,
        "active CURRENT/current-routing fields resolve to README and manifest routes"
        if not issues
        else "; ".join(issues),
        path=issue_paths[0] if issue_paths else context_index,
    )


def _check_current_authority_delegated_routing(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    current_governing, _ = _current_authority_entries(manifest)
    target_entries = [
        current_governing[document_id]
        for document_id in CURRENT_AUTHORITY_STATE_SECTIONS
        if document_id in current_governing
    ]
    if not target_entries:
        return

    context_index = str(integrity_rules["document_roots"]["context_index"])
    readme_path = root / context_index
    readme_text = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    readme_filenames = _readme_current_authority_filenames(readme_text)
    issues: list[str] = []
    issue_paths: list[str] = []
    for entry in target_entries:
        document_id = str(entry.get("document_id"))
        relative = _relative_path(entry)
        path = _entry_path(root, entry)
        active = _current_authority_state_section(
            path.read_text(encoding="utf-8") if path.is_file() else "",
            document_id,
        )
        delegated_lines = [
            line for line in active.splitlines()
            if "readme" in line.lower() and re.search(r"current\s+open\s+work", line, re.IGNORECASE)
        ]
        if document_id == "PLATFORM_BASELINE":
            volatile_states = (
                "NEXT / AUTHORISED / NOT STARTED",
                "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
                "COMPLETE / CERTIFIED",
            )
            present_states = [state for state in volatile_states if state in active]
            if present_states:
                issues.append(
                    f"{document_id}: §24 mirrors volatile HARDEN execution state {present_states!r}"
                )
                issue_paths.append(relative)
        if not delegated_lines:
            if document_id in {"PROJECT_NORTH_STAR_AND_MVP", "PLATFORM_BASELINE"}:
                issues.append(f"{document_id}: active current-state block does not delegate programme routing to README and current Open Work")
                issue_paths.append(relative)
            continue

        required_ids = (document_id, "OPEN_WORK")
        missing_routes = [
            required_id
            for required_id in required_ids
            if required_id not in current_governing
            or str(current_governing[required_id].get("canonical_filename")) not in readme_filenames
        ]
        if len(delegated_lines) != 1 or missing_routes:
            detail = (
                f"delegated routing fields={len(delegated_lines)}, missing README/manifest routes={sorted(set(missing_routes))}"
            )
            issues.append(f"{document_id}: {detail}")
            issue_paths.append(relative)

    _record_check(
        report,
        "current_authority_delegated_routing",
        not issues,
        "active current-state blocks agree with README and delegated current Open Work routing"
        if not issues
        else "; ".join(issues),
        path=issue_paths[0] if issue_paths else context_index,
    )


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
        document_id = str(entry.get("document_id", ""))
        document_id_version = re.search(r"(?:^|_)V(\d+(?:_\d+){2})$", document_id)
        document_id_version_matches = (
            document_id_version is None
            or document_id_version.group(1).replace("_", ".") == str(entry.get("semver", ""))
        )
        if document_id_version is None:
            document_id_version_message = f"document ID {document_id!r} has no version suffix"
        elif document_id_version_matches:
            document_id_version_message = (
                f"versioned document ID {document_id!r} matches manifest SemVer {entry.get('semver')!r}"
            )
        else:
            encoded_version = document_id_version.group(1).replace("_", ".")
            document_id_version_message = (
                f"document ID {document_id!r} encodes version {encoded_version!r}, "
                f"not manifest SemVer {entry.get('semver')!r}"
            )
        _record_check(
            report,
            "manifest_document_id_version_parity",
            document_id_version_matches,
            document_id_version_message,
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


def _check_audit_v010_current_promotion(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    readme: str,
    open_work: str,
    report: dict[str, Any],
) -> None:
    """Fail closed on the Audit v0.1.0 certified-candidate/status-successor split."""
    docs = root / "docs" / "00_platform"
    current_relative = (
        "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    )
    archive_relative = (
        "docs/00_platform/archive/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    )
    expected_candidate_hash = "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea"
    expected_archives = {
        archive_relative: expected_candidate_hash,
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.64.md": "1a96a3720de79432255e6ad2c947221900233b6928ef1e64150d1fa08a54a494",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.6.md": "af0142658034ea80b388a2e8f024461cbe95da2c724e51651e0990a883d6aa34",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md": "0f7da7407ddd2b1c57e6eb72843f963ad0486a82022b943910501e8fca541ea9",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.8.md": "bf7e75f74267957cb4f9da6851ce0c0d9b56fee8aa806009b86efe6fb2c0192d",
    }
    issues: list[str] = []
    open_state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work,
        re.DOTALL,
    )
    try:
        current_open_state = json.loads(open_state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if open_state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        current_open_state = {}
    reconciliation_certified_current = current_open_state.get("status_successor_version") in {"0.5.11", "0.5.12", "0.5.13"}
    tracker_closure_sync_current = current_open_state.get("status_successor_version") in {"0.5.12", "0.5.13"}
    phase7c_candidate_current = current_open_state.get("status_successor_version") == "0.5.13"

    configured_archives = integrity_rules.get("audit_v010_promotion_archives")
    if not isinstance(configured_archives, dict) or configured_archives != expected_archives:
        issues.append("manifest Audit v0.1.0 promotion archive pins are missing, substituted or incorrect")
    for relative, expected_hash in expected_archives.items():
        path = root / relative
        if not path.is_file():
            issues.append(f"required Audit promotion archive is missing: {relative}")
        elif sha256_file(path) != expected_hash:
            issues.append(f"Audit promotion archive bytes changed: {relative}")

    current_path = root / current_relative
    archived_path = root / archive_relative
    current_bytes = current_path.read_bytes() if current_path.is_file() else b""
    archived_bytes = archived_path.read_bytes() if archived_path.is_file() else b""
    boundary = b"## 1. Baseline, purpose and scope"
    if not archived_bytes or hashlib.sha256(archived_bytes).hexdigest() != expected_candidate_hash:
        issues.append("certified PR #118 Audit candidate archive is missing or does not match its exact SHA-256")
    if boundary not in current_bytes or boundary not in archived_bytes:
        issues.append("current or archived Audit dossier is missing the certified semantic-body boundary")
    elif current_bytes[current_bytes.index(boundary):] != archived_bytes[archived_bytes.index(boundary):]:
        issues.append("current Audit dossier semantic body differs from the archived certified candidate")

    current_text = current_bytes.decode("utf-8", errors="replace")
    current_header = current_text.split("## 1. Baseline, purpose and scope", 1)[0]
    status_mirrors = re.findall(r"(?m)^\*\*Status:\*\* `([^`]+)`\.", current_header)
    if (
        "**Artifact version:** v0.1.0 narrow status successor" not in current_header
        or status_mirrors != ["CERTIFIED / CURRENT"]
    ):
        issues.append("current Audit dossier lifecycle header does not record the v0.1.0 CERTIFIED / CURRENT status successor")
    candidate_start = "<!-- AUDIT_EVIDENCE_V010_CURRENT_LIFECYCLE_STATE_START -->"
    candidate_end = "<!-- AUDIT_EVIDENCE_V010_CURRENT_LIFECYCLE_STATE_END -->"
    state_pattern = re.compile(
        re.escape(candidate_start) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(candidate_end),
        re.DOTALL,
    )
    state_matches = list(state_pattern.finditer(current_text))
    if current_text.count(candidate_start) != 1 or current_text.count(candidate_end) != 1 or len(state_matches) != 1:
        issues.append("Audit current lifecycle projection is missing, duplicated or malformed")
        lifecycle: dict[str, Any] = {}
    else:
        try:
            parsed = json.loads(state_matches[0].group(1), object_pairs_hook=_reject_duplicate_json_keys)
        except (json.JSONDecodeError, TypeError, ValueError):
            parsed = None
        lifecycle = parsed if isinstance(parsed, dict) else {}
        if not isinstance(parsed, dict):
            issues.append("Audit current lifecycle projection is not a valid unique-key JSON object")
    expected_lifecycle = {
        "artifact_version": "v0.1.0",
        "audit_lifecycle": "CERTIFIED / CURRENT",
        "pr_118_candidate_certification": "COMPLETE",
        "pr_118_post_merge_certification_evidence": "COMPLETE",
        "proof_classification": "NOT FINALISED",
        "phase_8_application_implementation": "UNAUTHORISED",
    }
    if not reconciliation_certified_current:
        expected_lifecycle.update(
            {
                "phase_7b_reconciliation": "NEXT / NOT_STARTED",
                "phase_7c": "BLOCKED / NOT_STARTED",
            }
        )
    for key, value in expected_lifecycle.items():
        if lifecycle.get(key) != value:
            issues.append(f"Audit lifecycle value {key!r} is missing or contradictory")
    promotion_value = lifecycle.get("current_status_promotion")
    if not isinstance(promotion_value, str) or not re.fullmatch(r"PR #[1-9][0-9]* STATUS SUCCESSOR", promotion_value):
        issues.append("Audit current-status promotion does not bind a real PR number")

    required_provenance = (
        "PR #118",
        "68df8bfb2723c6d4bb414fffae63f20ba0744a6d",
        "5f5a994e48d9458aaa6397044b3af4d72c5d5e81",
        "acd04f523997a0ae8a7ae3edbbfb9280bd4de1ca",
        "3566f1353ef34af58773aa13c6f5bd61d2613d96",
        "38698409603",
        "38704942507",
        expected_candidate_hash,
        "Independent exact-head review | PASS",
        "Candidate/resulting-main tree identity | PASS",
    )
    if any(item not in current_text for item in required_provenance):
        issues.append("Audit current-status preamble omits inherited PR #118 certification provenance")
    if "resulting-main workflow" in current_text.casefold() and "38704942507" not in current_text:
        issues.append("Audit resulting-main certification evidence is not bound to the verified workflow")

    active_audit_dossiers = sorted(
        path
        for path in docs.rglob("*.md")
        if path.name.upper().startswith("FP-001")
        and "AUDIT" in path.name.upper()
        and "DOSSIER" in path.name.upper()
        and "archive" not in path.parts
    )
    if active_audit_dossiers != [current_path]:
        issues.append("exactly one current Audit dossier status successor must exist outside archive")

    nav = integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])
    if not isinstance(nav, list) or nav.count(current_relative) != 1:
        issues.append("manifest navigation must include the current Audit dossier exactly once")
    current_authority_paths = {
        _relative_path(entry)
        for key in ("governing_documents", "reference_documents")
        for entry in manifest.get(key, [])
        if isinstance(entry, dict) and entry.get("lifecycle", "current") != "historical"
    }
    if current_relative in current_authority_paths:
        issues.append("Audit dossier is incorrectly registered as a governing or reference authority")
    archived_candidate_rows = [
        entry
        for entry in manifest.get("historical_documents", [])
        if isinstance(entry, dict) and _relative_path(entry) == archive_relative
    ]
    if len(archived_candidate_rows) != 1 or archived_candidate_rows[0].get("sha256") != expected_candidate_hash:
        issues.append("manifest must identify the exact archived PR #118 Audit candidate as historical evidence")

    graph_rules = integrity_rules.get("graph_rules", {})
    guard_note = graph_rules.get("stale_predecessor_current_path_guard_note", "") if isinstance(graph_rules, dict) else ""
    if (
        "The separate PR #119 Audit v0.1.0 current-status promotion" not in guard_note
        or "The separate PR #118 Audit v0.1.0 current-status promotion" in guard_note
        or "the exact PR #118 candidate is pinned as historical certification evidence" not in guard_note
    ):
        issues.append("manifest Audit promotion guard note must distinguish PR #119 promotion from PR #118 candidate")

    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    active = open_work[active_start:active_end] if active_start >= 0 and active_end > active_start else ""
    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    reconciliation_candidate_current = current_open_state.get("status_successor_version") == "0.5.10"
    open_work_state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work,
        re.DOTALL,
    )
    open_work_state: dict[str, Any] = {}
    if open_work_state_match:
        try:
            parsed_open_state = json.loads(open_work_state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys)
            open_work_state = parsed_open_state if isinstance(parsed_open_state, dict) else {}
        except (json.JSONDecodeError, TypeError, ValueError):
            pass
    expected_open_state = {
        "status_successor_version": "0.5.13" if phase7c_candidate_current else "0.5.12" if tracker_closure_sync_current else "0.5.11" if reconciliation_certified_current else "0.5.10" if reconciliation_candidate_current else "0.5.9",
        "status_successor_base_sha": (
            "1a51755d505279821afe166b030be735fe0b6a1c"
            if phase7c_candidate_current
            else
            "3f4c9bf564b2b011e96171b8664428423eeba558"
            if tracker_closure_sync_current
            else
            "f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3"
            if reconciliation_certified_current
            else "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd"
            if reconciliation_candidate_current
            else "3566f1353ef34af58773aa13c6f5bd61d2613d96"
        ),
        "current_stage": (
            "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT"
            if reconciliation_certified_current
            else "FP-001 PHASE 7B RECONCILIATION CANDIDATE REVIEW"
            if reconciliation_candidate_current
            else "FP-001 AUDIT & EVIDENCE DOSSIER CURRENT-STATUS PROMOTION"
        ),
        "next_stage": (
            "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE"
            if phase7c_candidate_current
            else "AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT"
            if reconciliation_certified_current
            else "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
            if reconciliation_candidate_current
            else "FP-001 PHASE 7B RECONCILIATION"
        ),
        "audit_dossier": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation": (
            "COMPLETE / CERTIFIED / CURRENT"
            if reconciliation_certified_current
            else "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if reconciliation_candidate_current
            else "NEXT / NOT_STARTED"
        ),
        "phase_7c": (
            "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if phase7c_candidate_current
            else "NEXT / NOT_STARTED" if reconciliation_certified_current else "BLOCKED / NOT_STARTED"
        ),
        "proof_classification": "NOT FINALISED",
        "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
    }
    if not reconciliation_certified_current:
        expected_open_state["phase_7c_block_reason"] = "Successful Phase 7B reconciliation is required; Audit dossier authorship and current status are complete"
    for key, value in expected_open_state.items():
        if open_work_state.get(key) != value:
            issues.append(f"Open Work lifecycle value {key!r} is missing or contradictory")
    if open_work_state.get("conditional_dossiers") != {
        "privacy_consent": "NOT_REQUIRED",
        "content_media": "NOT_REQUIRED",
        "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "analytics": "NOT_REQUIRED",
    }:
        issues.append("Open Work conditional dossier dispositions disagree with the certified current dossier set")
    for status in (
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "IDENTITY & ACCESS: REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "PRIVACY & CONSENT: NOT_REQUIRED",
        "CONTENT & MEDIA: NOT_REQUIRED",
        "ANALYTICS: NOT_REQUIRED",
        (
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT"
            if reconciliation_certified_current
            else "PHASE 7B RECONCILIATION: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if reconciliation_candidate_current
            else "PHASE 7B RECONCILIATION: NEXT / NOT_STARTED"
        ),
        (
            "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE"
            if phase7c_candidate_current
            else "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT (NOT_STARTED)"
            if reconciliation_certified_current
            else "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
            if reconciliation_candidate_current
            else "NEXT STAGE: FP-001 PHASE 7B RECONCILIATION"
        ),
        (
            "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if phase7c_candidate_current
            else "PHASE 7C: NEXT / NOT_STARTED" if reconciliation_certified_current
            else "PHASE 7C: BLOCKED / NOT_STARTED UNTIL SUCCESSFUL PHASE 7B RECONCILIATION"
        ),
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED",
    ):
        if status not in active_summary:
            issues.append(f"Open Work active route omits {status!r}")
    if reconciliation_certified_current:
        if re.search(r"(?im)^.*PHASE 7B RECONCILIATION\s*:\s*(?:IN PROGRESS|NEXT / NOT_STARTED|STARTED).*$", active):
            issues.append("Open Work leaves completed Phase 7B reconciliation unverified")
        if not phase7c_candidate_current and re.search(r"(?im)^.*PHASE 7C\s*:\s*(?:BLOCKED|IN PROGRESS|READY|UNBLOCKED|COMPLETE|CERTIFIED|AUTHORI[ZS]ED).*$", active):
            issues.append("Open Work blocks or starts Phase 7C instead of routing it as NEXT / NOT_STARTED")
        if phase7c_candidate_current and re.search(r"(?im)^PHASE 7C:\s*(?:COMPLETE|CERTIFIED|CURRENT|AUTHORI[ZS]ED).*$", active):
            issues.append("Open Work prematurely completes or authorises the Phase 7C candidate")
    else:
        if re.search(r"(?im)^.*PHASE 7B RECONCILIATION\s*:\s*(?:COMPLETE|CERTIFIED|STARTED).*$", active):
            issues.append("Open Work falsely claims Phase 7B reconciliation has started or completed")
        if re.search(r"(?im)^.*PHASE 7C\s*:\s*(?:NEXT|READY|UNBLOCKED|COMPLETE|CERTIFIED|AUTHORI[ZS]ED).*$", active):
            issues.append("Open Work prematurely starts or unblocks Phase 7C")
    if re.search(r"(?im)^.*PROOF CLASSIFICATION\s*:\s*(?:FINAL|FINALI[ZS]ED|CERTIFIED).*$", active):
        issues.append("Open Work prematurely finalises proof classification")
    if re.search(r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$", active):
        issues.append("Open Work prematurely authorises Phase 8 or application implementation")

    atlas_current_path = docs / ("working/DELIVERY_ATLAS_WORKING_v0.4.11.md" if phase7c_candidate_current else "working/DELIVERY_ATLAS_WORKING_v0.4.10.md" if reconciliation_certified_current else "working/DELIVERY_ATLAS_WORKING_v0.4.8.md")
    skeleton_current_path = docs / ("working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.13.md" if phase7c_candidate_current else "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.12.md" if reconciliation_certified_current else "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md")
    harden_current_path = docs / ("working/HARDEN-02_CONTRACT_WORKING_v0.5.13.md" if phase7c_candidate_current else "working/HARDEN-02_CONTRACT_WORKING_v0.5.12.md" if reconciliation_certified_current else "working/HARDEN-02_CONTRACT_WORKING_v0.5.10.md")
    current_surfaces = (
        ("README current state", _markdown_h2_section(readme, "Current State") or ""),
        ("README active working artifacts", _markdown_h2_section(readme, "Active Working Artifacts") or ""),
        ("Delivery Atlas current state", atlas_current_path.read_text(encoding="utf-8") if atlas_current_path.is_file() else ""),
        ("FP-001 Skeleton current state", skeleton_current_path.read_text(encoding="utf-8") if skeleton_current_path.is_file() else ""),
        ("HARDEN-02 current state", harden_current_path.read_text(encoding="utf-8") if harden_current_path.is_file() else ""),
    )
    for label, text in current_surfaces:
        if current_relative.removeprefix("docs/00_platform/") not in text:
            issues.append(f"{label} omits the current Audit dossier route")
        if "Audit & Evidence" not in text or "REQUIRED / COMPLETE / CERTIFIED / CURRENT" not in text:
            issues.append(f"{label} does not record the current Audit lifecycle")
        if tracker_closure_sync_current and label in {
            "README active working artifacts",
            "Delivery Atlas current state",
            "FP-001 Skeleton current state",
            "HARDEN-02 current state",
        }:
            if label == "Delivery Atlas current state":
                current_tracker_projection = text.split("## v0.4.9 Patch Scope", 1)[0]
            elif label == "FP-001 Skeleton current state":
                current_tracker_projection = text.split("## 1. Identity", 1)[0]
            elif label == "HARDEN-02 current state":
                current_tracker_projection = _markdown_h2_section(
                    text, "23. FP-001 Phase 7B reconciliation current route"
                ) or ""
            else:
                current_tracker_projection = text
            if (
                "tracker" not in current_tracker_projection.casefold()
                or "#120" not in current_tracker_projection.casefold()
                or "closed / completed" not in current_tracker_projection.casefold()
                or TRACKER_120_OPEN_PROJECTION_PATTERN.search(current_tracker_projection)
            ):
                issues.append(f"{label} does not project tracker #120 as CLOSED / COMPLETED")
        if label == "FP-001 Skeleton current state":
            if "records the work start for the already-adjudicated required FP-001 Audit & Evidence JIT Domain Dossier" in text:
                issues.append("FP-001 Skeleton current-state prose misidentifies Audit status promotion as work start")
            for required in (
                (
                    "Audit & Evidence v0.1.0 remain REQUIRED / COMPLETE / CERTIFIED / CURRENT"
                    if reconciliation_certified_current
                    else "records the Audit v0.1.0 current-status promotion under PR #119"
                ),
                (
                    "Phase 7B reconciliation v0.1.0 is COMPLETE / CERTIFIED / CURRENT under completed tracker #120 (CLOSED / COMPLETED)"
                    if tracker_closure_sync_current
                    else "Phase 7B reconciliation v0.1.0 is COMPLETE / CERTIFIED / CURRENT under tracker #120"
                    if reconciliation_certified_current
                    else "Phase 7B reconciliation is `IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING`"
                    if reconciliation_candidate_current
                    else "routes Phase 7B reconciliation as `NEXT / NOT_STARTED`"
                ),
                "preserves accepted PMR reconciliation semantics",
                "all seven material capability relationships",
                "the six affected Domains",
                "the existing stage gates",
                *(() if reconciliation_certified_current else ("does not perform Phase 7B reconciliation",)),
                "does not authorise Phase 7C",
                "does not finalise proof classification",
                "does not authorise Phase 8/application implementation",
            ):
                if required not in text:
                    issues.append(f"FP-001 Skeleton current-status successor omits {required!r}")
        elif label == "Delivery Atlas current state":
            historical_start = text.find("## v0.4.6 Patch Scope (historical predecessor record)")
            historical = text[historical_start:] if historical_start >= 0 else ""
            if historical:
                historical = historical.split("## v0.4.4 Patch Scope", 1)[0]
            current_atlas = text[:historical_start] if historical_start >= 0 else text
            if (
                "Open Work v1.2.64" not in historical
                or "Open Work v1.2.65" in historical
                or "review-ready in PR #118" not in historical
                or "NOT CERTIFIED / NOT CURRENT" not in historical
            ):
                issues.append("Atlas v0.4.6 historical route must use Open Work v1.2.64 and preserve candidate-review status")
            if (
            ("Open Work v1.2.69" if phase7c_candidate_current else "Open Work v1.2.68" if reconciliation_certified_current else "Open Work v1.2.66" if reconciliation_candidate_current else "Open Work v1.2.65") not in current_atlas
                or (
                    "Phase 7B reconciliation v0.1.0 is COMPLETE / CERTIFIED / CURRENT" not in current_atlas
                    if reconciliation_certified_current
                    else "separate current-status promotion PR #119" not in current_atlas
                )
                or (
                    reconciliation_candidate_current
                    and "candidate v0.1.0 is open for independent review under tracker #120" not in current_atlas.casefold()
                )
            ):
                issues.append("current Atlas route must use the current Open Work version and identify the candidate and PR #119 lifecycle")
        elif label == "HARDEN-02 current state":
            header = text.split("### Revision log", 1)[0]
            if (
        header.count("v0.5.10 current-status successor base main SHA") != 1
                or "v0.5.10 current-status successor base main SHA:** `5d282ecca4e13b621c7f96c05c47d6fac43ec1bd`" not in header
                or (
                    phase7c_candidate_current
                    and (
                        header.count("v0.5.13 current-status successor base main SHA") != 1
                        or "v0.5.13 current-status successor base main SHA:** `1a51755d505279821afe166b030be735fe0b6a1c`" not in header
                    )
                )
                or (
                    reconciliation_certified_current
                    and not phase7c_candidate_current
                    and (
                        header.count("v0.5.11 current-status successor base main SHA") != 1
                        or "v0.5.11 current-status successor base main SHA:** `f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3`" not in header
                    )
                )
                or text.count("v0.5.8 routing-successor base main SHA") != 1
                or "v0.5.8 routing-successor base main SHA:** `5f5a994e48d9458aaa6397044b3af4d72c5d5e81`" not in header
                or text.count("v0.5.9 current-status successor base main SHA") != 1
                or "v0.5.9 current-status successor base main SHA:** `3566f1353ef34af58773aa13c6f5bd61d2613d96`" not in header
            ):
                issues.append("HARDEN-02 v0.5.10 provenance must preserve the v0.5.9 and v0.5.8 status-successor bases")
        current_status_text = text
        if label == "Delivery Atlas current state":
            current_status_text = text.split("## v0.4.7 Patch Scope", 1)[0]
        elif label == "FP-001 Skeleton current state":
            current_status_text = text.split("## 1. ", 1)[0]
        elif label == "HARDEN-02 current state":
            current_status_text = text.split("## 21. Current execution certification and next stage", 1)[-1]
        if re.search(
            r"(?i)Audit(?: &| and ) Evidence[^\n]{0,100}REQUIRED\s*/\s*(?:IN PROGRESS|NEXT|NOT STARTED|NOT COMPLETE|CERTIFICATION PENDING)",
            current_status_text,
        ):
            issues.append(f"{label} retains an obsolete in-progress or incomplete Audit status")
    readme_current = readme.split("## Current State", 1)[-1]
    for required in (
        (
            "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE"
            if phase7c_candidate_current
            else "NEXT STAGE: AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT; STATUS: NOT_STARTED"
            if reconciliation_certified_current
            else "NEXT STAGE: FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
            if reconciliation_candidate_current
            else "NEXT STAGE: FP-001 PHASE 7B RECONCILIATION"
        ),
        (
            "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if phase7c_candidate_current
            else "PHASE 7C: NEXT / NOT_STARTED" if reconciliation_certified_current
            else "PHASE 7C: BLOCKED / NOT_STARTED"
        ),
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED",
    ):
        if required not in readme_current:
            issues.append(f"README current state omits {required!r}")

    _record_check(
        report,
        "fp001_audit_v010_current_promotion",
        not issues,
        "Audit v0.1.0 certified candidate, current-status successor, routing and downstream stops are consistent"
        if not issues
        else "; ".join(issues),
        path=current_relative,
    )


def _fp001_phase7b_candidate_text_issues(
    candidate_text: str,
    candidate_rules: dict[str, Any],
) -> list[str]:
    """Validate the reconciliation candidate's fail-closed seam matrix."""

    issues: list[str] = []
    header = candidate_text.split("## 1. Baseline and authority set", 1)[0]
    required_header = (
        "FP-001 PHASE 7B RECONCILIATION CANDIDATE",
        "NOT CERTIFIED",
        "NOT CURRENT",
        "NON-IMPLEMENTATION",
        "NOT PHASE 7C",
        "NOT DEVELOPMENT-ENTRY AUTHORITY",
        "PASS / READY FOR INDEPENDENT REVIEW",
        "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
    )
    if any(token not in header for token in required_header):
        issues.append("candidate header omits its exact baseline, PASS result or non-current lifecycle boundary")
    for heading in (
        "## 4. Cross-Domain seam matrix",
        "## 5. End-to-end participant and operator journey",
        "## 6. Pressure cases",
        "## 7. PMR preservation and open-question routing",
    ):
        if candidate_text.count(heading) != 1:
            issues.append(f"candidate is missing or duplicates required section {heading!r}")
    if any(
        heading not in candidate_text
        for heading in (
            "Source authority and Domain; receiving or affected Domain",
            "Business truth and durable consequence owner",
            "Request or command boundary",
            "Evidence boundary; failure and retry consequence",
            "Privacy and minimisation",
            "Dossier and higher-authority anchors",
            "Classification and remaining downstream work",
        )
    ):
        issues.append("candidate seam matrix omits a required reconciliation field")

    expected_ids = candidate_rules.get("required_seam_ids")
    allowed = candidate_rules.get("allowed_classifications")
    if not isinstance(expected_ids, list) or not isinstance(allowed, list):
        return issues + ["manifest candidate seam ids or allowed classifications are malformed"]
    rows: dict[str, list[str]] = {}
    matrix_text = candidate_text.split("## 4. Cross-Domain seam matrix", 1)[-1].split("## 5.", 1)[0]
    for line in matrix_text.splitlines():
        if not line.startswith("| S-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        seam_id = cells[0] if cells else ""
        rows.setdefault(seam_id, []).append(line)
        if len(cells) != 8:
            issues.append(f"material seam {seam_id or '<unknown>'} does not have all eight matrix fields")
            continue
        classifications = [classification for classification in allowed if f"`{classification}`" in cells[-1]]
        if len(classifications) != 1:
            issues.append(f"material seam {seam_id} is missing one allowed determinate classification")
    missing = sorted(set(expected_ids) - set(rows))
    unexpected = sorted(set(rows) - set(expected_ids))
    duplicates = sorted(seam_id for seam_id, occurrences in rows.items() if len(occurrences) != 1)
    if missing:
        issues.append("candidate is missing material seams: " + ", ".join(missing))
    if unexpected:
        issues.append("candidate includes unregistered seam ids: " + ", ".join(unexpected))
    if duplicates:
        issues.append("candidate duplicates material seams: " + ", ".join(duplicates))

    result_is_pass = "PASS / READY FOR INDEPENDENT REVIEW" in header
    assigned_classifications = []
    for lines in rows.values():
        for line in lines:
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) == 8:
                assigned_classifications.extend(
                    classification for classification in allowed if f"`{classification}`" in cells[-1]
                )
    blocker_present = any(
        classification in {"BLOCKING_AUTHORITY_GAP", "BLOCKING_DOSSIER_CONTRADICTION"}
        for classification in assigned_classifications
    )
    if result_is_pass and blocker_present:
        issues.append("candidate PASS result cannot coexist with a blocking authority gap or dossier contradiction")
    return issues


def _check_fp001_phase7b_candidate(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Fail closed around the immutable, pre-certification FP-001 candidate."""

    docs = root / "docs" / "00_platform"
    rules = integrity_rules.get("fp001_phase7b_reconciliation_candidate", {})
    path = str(rules.get("path", "")) if isinstance(rules, dict) else ""
    candidate_path = root / path
    candidate_text = candidate_path.read_text(encoding="utf-8") if candidate_path.is_file() else ""
    if not candidate_text:
        _record_check(report, "fp001_phase7b_candidate_lifecycle", False, "Phase 7B reconciliation candidate is missing", path=path)
        _record_check(report, "fp001_phase7b_seam_matrix", False, "candidate seam matrix cannot be read", path=path)
        _record_check(report, "fp001_phase7b_baseline_and_dossiers", False, "candidate baseline/dossier checks cannot run", path=path)
        _record_check(report, "fp001_phase7b_gate_routing", False, "candidate lifecycle routing cannot be read", path=path)
        return

    lifecycle_issues: list[str] = []
    expected_candidate_route = {
        "path": "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
        "version": "0.1.0",
        "baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
        "tracker_issue": 120,
    }
    for key, expected in expected_candidate_route.items():
        if rules.get(key) != expected:
            lifecycle_issues.append(f"manifest Phase 7B candidate route {key!r} is missing or stale")
    current_routes = {
        _relative_path(entry)
        for entry in _all_entries(manifest)
        if entry.get("lifecycle", "current") != "historical"
    }
    if path in current_routes:
        lifecycle_issues.append("reconciliation candidate is incorrectly routed as current authority")
    if "[#120](https://github.com/JCSchoeman96/NewYou/issues/120)" not in candidate_text:
        lifecycle_issues.append("candidate does not reference the dedicated open reconciliation tracker")
    if "#111" not in candidate_text or "#114" not in candidate_text or "#116" not in candidate_text:
        lifecycle_issues.append("candidate does not link the programme router and completed dossier trackers")
    for token in (
        "PHASE 7B RECONCILIATION: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        "RECONCILIATION CANDIDATE: NOT CERTIFIED / NOT CURRENT",
        "PHASE 7C: BLOCKED / NOT_STARTED",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
    ):
        if token not in candidate_text:
            lifecycle_issues.append(f"candidate omits required lifecycle stop state {token!r}")
    _record_check(
        report,
        "fp001_phase7b_candidate_lifecycle",
        not lifecycle_issues,
        "candidate remains a review-only Phase 7B artifact with downstream gates closed"
        if not lifecycle_issues
        else "; ".join(lifecycle_issues),
        path=path,
    )

    seam_issues = _fp001_phase7b_candidate_text_issues(candidate_text, rules if isinstance(rules, dict) else {})
    _record_check(
        report,
        "fp001_phase7b_seam_matrix",
        not seam_issues,
        "all 15 material seam pairings are present, complete and determinately classified"
        if not seam_issues
        else "; ".join(seam_issues),
        path=path,
    )

    baseline_issues: list[str] = []
    baseline_authorities = rules.get("baseline_authority_versions", {})
    entries_by_id = {
        str(entry.get("document_id", "")): entry
        for entry in _all_entries(manifest)
        if entry.get("lifecycle", "current") != "historical"
    }
    for document_id, expected in baseline_authorities.items():
        if document_id == "OPEN_WORK":
            historical_id = "OPEN_WORK_V1_2_65"
        elif document_id == "ROADMAP":
            historical_id = "ROADMAP_V1_2_2"
        else:
            historical_id = None
        if historical_id is not None:
            entry = next(
                (
                    item
                    for item in _all_entries(manifest)
                    if item.get("document_id") == historical_id
                    and item.get("lifecycle") == "historical"
                ),
                None,
            )
        else:
            entry = entries_by_id.get(document_id)
        if (
            entry is None
            or entry.get("semver") != expected.get("version")
            or _relative_path(entry) != expected.get("path")
        ):
            baseline_issues.append(f"baseline authority {document_id} version or route changed")
    for relative, expected_hash in rules.get("baseline_current_document_sha256", {}).items():
        source = root / relative
        if not source.is_file() or sha256_file(source) != expected_hash:
            baseline_issues.append(f"baseline current authority bytes changed: {relative}")

    for domain, expected_hash in rules.get("dossier_sha256", {}).items():
        filename = {
            "Identity & Access": "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
            "Communications": "FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
            "Audit & Evidence": "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        }.get(domain)
        source = docs / "working" / filename if filename else None
        if source is None or not source.is_file() or sha256_file(source) != expected_hash:
            baseline_issues.append(f"certified {domain} dossier changed from its baseline bytes")
    audit_archive = docs / "archive" / "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    expected_audit_archive = rules.get("audit_certified_archive_sha256")
    if not audit_archive.is_file() or sha256_file(audit_archive) != expected_audit_archive:
        baseline_issues.append("certified Audit candidate archive SHA-256 changed")
    for relative, expected_hash in rules.get("predecessor_archives_sha256", {}).items():
        archive = root / relative
        if not archive.is_file() or sha256_file(archive) != expected_hash:
            baseline_issues.append(f"status predecessor archive is missing or changed: {relative}")

    manifest_authority_hashes = {
        _relative_path(entry): entry.get("sha256")
        for entry in _all_entries(manifest)
    }
    for relative, expected_hash in rules.get("baseline_current_document_sha256", {}).items():
        if manifest_authority_hashes.get(relative) != expected_hash:
            baseline_issues.append(f"manifest hash for baseline authority changed: {relative}")

    for domain, disposition in rules.get("required_dossiers", {}).items():
        if domain not in candidate_text or disposition not in candidate_text:
            baseline_issues.append(f"candidate does not preserve dossier disposition for {domain}")
    domains = rules.get("six_affected_domains", [])
    capabilities = rules.get("seven_material_capabilities", [])
    domain_block_match = re.search(
        r"The six affected Domains remain:\s*```text\s*(.*?)\s*```",
        candidate_text,
        re.DOTALL,
    )
    candidate_domains = [line.strip() for line in domain_block_match.group(1).splitlines() if line.strip()] if domain_block_match else []
    if len(domains) != 6 or candidate_domains != domains:
        baseline_issues.append("candidate does not preserve exactly the six affected FP-001 Domains")
    cap_line = next(
        (line for line in candidate_text.splitlines() if line.startswith("The seven material capability relationships remain")),
        "",
    )
    cap_group = re.search(r"The seven material capability relationships remain (.*?)(?:\. Analytics|$)", cap_line)
    if not cap_group or re.findall(r"CAP-\d{3}", cap_group.group(1)) != capabilities:
        baseline_issues.append("candidate does not preserve exactly the seven material capability relationships")
    if "issue #107" not in candidate_text.casefold() or "not an fp-001 blocker" not in candidate_text.casefold():
        baseline_issues.append("candidate incorrectly omits the issue #107 Full-Deletion scope boundary")
    if "Analytics stays `CONSUMER`" not in candidate_text or "Analytics is a consumer" not in candidate_text:
        baseline_issues.append("candidate grants Analytics source-truth ownership or omits its consumer boundary")
    if "PMR" not in candidate_text or "prior PR #67 PMR reconciliation is complete" not in candidate_text:
        baseline_issues.append("candidate does not preserve the completed PMR reconciliation")

    skeleton_path = docs / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md"
    skeleton_archive = docs / "archive" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md"
    pmr_start = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:START -->"
    pmr_end = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:END -->"
    def marked_block(text: str, start: str, end: str) -> str:
        if text.count(start) != 1 or text.count(end) != 1:
            return ""
        left = text.index(start)
        right = text.index(end)
        return text[left : right + len(end)] if left < right else ""
    if (
        not skeleton_path.is_file()
        or not skeleton_archive.is_file()
        or marked_block(skeleton_path.read_text(encoding="utf-8"), pmr_start, pmr_end)
        != marked_block(skeleton_archive.read_text(encoding="utf-8"), pmr_start, pmr_end)
    ):
        baseline_issues.append("certified PMR reconciliation contract changed in the current skeleton successor")
    _record_check(
        report,
        "fp001_phase7b_baseline_and_dossiers",
        not baseline_issues,
        "baseline authorities, dossier bodies, archive hashes, scope and PMR semantics are preserved"
        if not baseline_issues
        else "; ".join(baseline_issues),
        path=path,
    )

    route_issues: list[str] = []
    open_work_entry = entries_by_id.get("OPEN_WORK", {})
    open_work_path = root / _relative_path(open_work_entry) if open_work_entry else None
    open_work_text = open_work_path.read_text(encoding="utf-8") if open_work_path and open_work_path.is_file() else ""
    state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work_text,
        re.DOTALL,
    )
    try:
        open_work_state = json.loads(state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        open_work_state = {}
    status_version = open_work_state.get("status_successor_version")
    phase8_contract_candidate = status_version == "1.2.77"
    expected_state = {
        "status_successor_version": status_version if status_version in {"1.2.74", "1.2.77"} else "1.2.77",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation_execution_tracker_issue": 120,
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "proof_classification": "NEW_TRACER_BULLET",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / DEFINED AS REVIEW CANDIDATE" if phase8_contract_candidate else "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "TB-001" if phase8_contract_candidate else "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "application_implementation": "AUTHORISED",
        "phase8": "AUTHORISED",
        "next_stage": "TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION" if phase8_contract_candidate else "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "next_governance_action": "TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION" if phase8_contract_candidate else "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
    }
    if phase8_contract_candidate:
        expected_state.update({
            "proof_design": "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
            "proof_result": "NOT STARTED",
            "proof_certification": "NOT STARTED",
            "proof_contract_path": "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md",
            "proof_contract_lifecycle": "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
            "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        })
    for key, expected in expected_state.items():
        if open_work_state.get(key) != expected:
            route_issues.append(f"current Open Work lifecycle state {key!r} is missing or contradictory")
    candidate_state = open_work_state.get("phase_7b_reconciliation_candidate", {})
    if (
        not isinstance(candidate_state, dict)
        or candidate_state.get("lifecycle") != "CERTIFIED / CURRENT"
        or candidate_state.get("path") != "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
        or candidate_state.get("current_status_successor_path")
        != "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
    ):
        route_issues.append("current Open Work omits the certified archive and current status successor routes")
    if open_work_state.get("conditional_dossiers") != {
        "privacy_consent": "NOT_REQUIRED",
        "content_media": "NOT_REQUIRED",
        "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
        "analytics": "NOT_REQUIRED",
    }:
        route_issues.append("current Open Work changes Privacy, Content & Media, Audit or Analytics disposition")
    for token in (
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "RECONCILIATION v0.1.0: CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C FINAL FEATURE PACK CONTRACT: `working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md`; v0.1.0 COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION" if phase8_contract_candidate else "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET: REQUIRED / DEFINED AS REVIEW CANDIDATE" if phase8_contract_candidate else "TRACER BULLET: REQUIRED / NOT YET DEFINED",
        "TRACER BULLET ID: TB-001" if phase8_contract_candidate else "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
        "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET",
    ):
        if token not in open_work_text:
            route_issues.append(f"current Open Work omits fail-closed gate state {token!r}")
    _record_check(
        report,
        "fp001_phase7b_gate_routing",
        not route_issues,
        "Phase 7B and Phase 7C certification routes remain current; Development Entry Hard Stop PASS authorises bounded Phase 8 only"
        if not route_issues
        else "; ".join(route_issues),
        path="docs/00_platform/02_OPEN_WORK_v1.2.77.md",
    )


def _check_fp001_phase7c_candidate(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Keep the Phase 7C contract candidate separate from certification and authority."""

    docs = root / "docs" / "00_platform"
    rules = integrity_rules.get("fp001_phase7c_final_contract_candidate", {})
    candidate_path = str(rules.get("path", "")) if isinstance(rules, dict) else ""
    current_contract_path = str(rules.get("current_contract_path", "")) if isinstance(rules, dict) else ""
    candidate_file = root / candidate_path
    candidate = candidate_file.read_text(encoding="utf-8") if candidate_file.is_file() else ""

    def check(name: str, issues: list[str], success: str, path: str | None = None) -> None:
        _record_check(
            report,
            name,
            not issues,
            success if not issues else "; ".join(issues),
            path=path,
        )

    expected_rule = {
        "path": "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "current_contract_path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "version": "0.1.0",
        "baseline_main_sha": "1a51755d505279821afe166b030be735fe0b6a1c",
        "baseline_tree_sha": "d1298e3c567973e92e5c909ff1312e049b8718fb",
        "tracker_issue": 124,
        "tracker_state": "OPEN",
        "lifecycle": "CANDIDATE / NOT CERTIFIED / NOT CURRENT",
        "phase7c_state": "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        "phase7b_state": "COMPLETE / CERTIFIED / CURRENT",
        "phase7b_tracker_issue": 120,
        "phase7b_tracker_state": "CLOSED / COMPLETED",
        "programme_router_issue": 111,
        "programme_router_state": "OPEN",
        "reconciliation_archive_path": "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
        "reconciliation_archive_sha256": "274306e73e2450806516a5b76ca96f1a768af7824ba823cca6c9371c58e65401",
        "required_seam_ids": [f"S-{i:02}" for i in range(1, 16)],
        "out_of_scope_seam_ids": ["S-11", "S-14", "S-15"],
        "six_affected_domains": [
            "Identity & Access", "Privacy & Consent", "Content & Media",
            "Communications", "Audit & Evidence", "Analytics",
        ],
        "seven_material_capabilities": [
            "CAP-001", "CAP-002", "CAP-003", "CAP-005",
            "CAP-006", "CAP-017", "CAP-028",
        ],
        "required_dossiers": {
            "Identity & Access": "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4",
            "Communications": "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "Audit & Evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "Privacy & Consent": "NOT_REQUIRED",
            "Content & Media": "NOT_REQUIRED",
            "Analytics": "NOT_REQUIRED",
        },
        "fail_closed_oq": "OQ-029",
        "proof_classification": "NOT FINALISED",
        "phase8": "UNAUTHORISED",
        "application_implementation": "UNAUTHORISED",
    }
    lifecycle_issues: list[str] = []
    if not candidate:
        lifecycle_issues.append("Phase 7C Final Feature Pack Contract candidate is missing")
    if not isinstance(rules, dict):
        lifecycle_issues.append("manifest Phase 7C candidate rule is missing")
    elif any(rules.get(key) != value for key, value in expected_rule.items()):
        lifecycle_issues.append("manifest Phase 7C candidate route or scope guard changed")
    current_routes = {
        _relative_path(entry)
        for entry in _all_entries(manifest)
        if entry.get("lifecycle", "current") != "historical"
    }
    if current_contract_path in current_routes:
        lifecycle_issues.append("working contract is incorrectly registered as a current authority document")
    if candidate_path in current_routes:
        lifecycle_issues.append("candidate archive is incorrectly registered as a current authority document")
    historical_paths = {
        _relative_path(entry) for entry in manifest.get("historical_documents", [])
    }
    if candidate_path not in historical_paths:
        lifecycle_issues.append("PR #125 candidate archive is not registered as historical evidence")
    if current_contract_path in historical_paths:
        lifecycle_issues.append("working contract route is incorrectly classified as historical evidence")
    graph_rules = integrity_rules.get("graph_rules", {})
    if current_contract_path not in graph_rules.get("navigation_document_paths", []):
        lifecycle_issues.append("manifest navigation routes do not expose the current Phase 7C contract path")
    if candidate_path in graph_rules.get("navigation_document_paths", []):
        lifecycle_issues.append("manifest navigation routes expose the immutable candidate archive as current navigation")
    if not candidate.startswith(
        "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT\n"
        "CANDIDATE\nNOT CERTIFIED\nNOT CURRENT\n\n"
        "NON-IMPLEMENTATION\n\n"
        "NOT PROOF CLASSIFICATION\nNOT PHASE 8 AUTHORITY\n"
        "NOT APPLICATION IMPLEMENTATION AUTHORITY\n"
    ):
        lifecycle_issues.append("candidate lifecycle header no longer makes its review-only boundary explicit")
    for token in (
        "CANDIDATE AUTHORED / READY FOR INDEPENDENT REVIEW",
        "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: CANDIDATE / NOT CERTIFIED / NOT CURRENT",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
        "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE",
    ):
        if token not in candidate:
            lifecycle_issues.append(f"candidate omits required lifecycle boundary {token!r}")
    if "Closes #124" in candidate or "closes #124" in candidate:
        lifecycle_issues.append("candidate PR routing text would close the open Phase 7C tracker")

    check(
        "fp001_phase7c_candidate_lifecycle",
        lifecycle_issues,
        "PR #125 candidate remains immutable historical evidence outside governing authority",
        candidate_path,
    )

    scope_issues: list[str] = []
    domains = expected_rule["six_affected_domains"]
    capabilities = expected_rule["seven_material_capabilities"]
    domain_block = ""
    capability_block = ""
    dossier_block = ""
    if candidate:
        try:
            domain_block = candidate.split("### Six affected Domains", 1)[1].split("### Material capability relationships", 1)[0]
            capability_block = candidate.split("### Material capability relationships", 1)[1].split("## D.", 1)[0]
            dossier_block = candidate.split("### Required dossier dispositions", 1)[1].split("### Six affected Domains", 1)[0]
        except IndexError:
            scope_issues.append("candidate scope headings are missing or reordered")
    candidate_domains = [line.strip() for line in domain_block.splitlines() if line.strip()]
    candidate_capabilities = re.findall(r"CAP-\d{3}", capability_block)
    if candidate_domains != domains:
        scope_issues.append("candidate does not contain exactly the six affected Domains")
    if candidate_capabilities != capabilities:
        scope_issues.append("candidate does not contain exactly the seven material capabilities")
    for domain, disposition in expected_rule["required_dossiers"].items():
        if f"| {domain} | {disposition} |" not in dossier_block:
            scope_issues.append(f"candidate dossier disposition changed for {domain}")
    if "NOT_REQUIRED means no separate FP-001 dossier was needed" not in candidate:
        scope_issues.append("candidate does not preserve the NOT_REQUIRED scope meaning")
    check(
        "fp001_phase7c_candidate_scope",
        scope_issues,
        "six Domains, seven capabilities and all dossier dispositions remain exact",
        candidate_path,
    )

    pairing_names = [
        "Identity & Access ↔ Privacy & Consent",
        "Identity & Access ↔ Content & Media",
        "Identity & Access ↔ Communications",
        "Identity & Access ↔ Audit & Evidence",
        "Identity & Access ↔ Analytics",
        "Privacy & Consent ↔ Content & Media",
        "Privacy & Consent ↔ Communications",
        "Privacy & Consent ↔ Audit & Evidence",
        "Privacy & Consent ↔ Analytics",
        "Content & Media ↔ Communications",
        "Content & Media ↔ Audit & Evidence",
        "Content & Media ↔ Analytics",
        "Communications ↔ Audit & Evidence",
        "Communications ↔ Analytics",
        "Audit & Evidence ↔ Analytics",
    ]
    seam_issues: list[str] = []
    try:
        seam_block = candidate.split("## H. Cross-Domain request/effect contract", 1)[1].split("## I. Failure, retry, idempotency and concurrency", 1)[0]
    except IndexError:
        seam_block = ""
        seam_issues.append("candidate cross-Domain seam section is missing")
    rows = [line for line in seam_block.splitlines() if line.startswith("| S-")]
    if [re.match(r"\| (S-\d+)", row).group(1) for row in rows if re.match(r"\| (S-\d+)", row)] != expected_rule["required_seam_ids"]:
        seam_issues.append("candidate does not preserve all 15 reconciliation pairings in order")
    parsed_rows = {}
    for row in rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if len(cells) < 4:
            seam_issues.append(f"candidate seam row is incomplete: {row}")
            continue
        parsed_rows[cells[0]] = cells
    for seam_id, pairing in zip(expected_rule["required_seam_ids"], pairing_names):
        cells = parsed_rows.get(seam_id, [])
        if not cells or cells[1] != pairing or not cells[3]:
            seam_issues.append(f"candidate seam {seam_id} is missing its pairing or contractual boundary")
        if seam_id in expected_rule["out_of_scope_seam_ids"]:
            if len(cells) < 3 or cells[2].replace(chr(96), "") != "OUT_OF_SCOPE_FOR_FP001":
                seam_issues.append(f"candidate changes the certified out-of-scope disposition for {seam_id}")
        elif len(cells) < 3 or "Exercised" not in cells[2]:
            seam_issues.append(f"candidate no longer materially exercises reconciliation seam {seam_id}")
    for token in ("15 Domain pairings examined", "Twelve are exercised", "BLOCKING_AUTHORITY_GAP: NONE", "BLOCKING_DOSSIER_CONTRADICTION: NONE"):
        if token not in candidate:
            seam_issues.append(f"candidate omits certified reconciliation result {token!r}")
    check(
        "fp001_phase7c_candidate_reconciliation_seams",
        seam_issues,
        "all 15 certified pairings are traced, including the three unchanged out-of-scope seams",
        candidate_path,
    )

    delivery_dimensions = (
        (
            "architectural proof requirement",
            "## P. Architectural proof requirement",
            "## Q. Vertical Slice map",
            (
                "reuse_existing_proof",
                "new_tracer_bullet",
                "proof classification: not finalised",
                "registration-to-verification-to-login",
                "duplicate or reordered requests",
                "session authority after restart or reconnect",
                "non-enumerating abuse",
                "consent changes during protected actions",
                "provider ambiguity",
                "restricted audit evidence",
                "flow-01",
                "no tb id or proof artifact is created",
                "a failed proof stops vertical expansion",
                "correct an architecture or domain-law defect through its owner",
            ),
        ),
        (
            "Vertical Slice map",
            "## Q. Vertical Slice map",
            "## R. Horizontal hardening requirements",
            (
                "outcome-level planning map",
                "not authorized vs ids",
                "public entry to verified individual account",
                "sign-in and protected access",
                "account recovery and primary-email change",
                "controlled support/admin and duplicate reconciliation",
                "interface/liveview",
                "authorised action",
                "actor/policy",
                "domain invariants",
                "durable state",
                "async consequences",
                "pubsub",
                "audit",
                "observability",
                "concurrency/idempotency",
                "database constraints/indexes",
                "cache invalidation",
                "automated tests",
                "acceptance criteria",
                "no vs ids, toons, executable tasks",
            ),
        ),
        (
            "horizontal hardening requirements",
            "## R. Horizontal hardening requirements",
            "## S. Performance envelope",
            (
                "already-correct capabilities",
                "measurements",
                "failure tests",
                "security review",
                "pilot operation",
                "release gates",
                "security/privacy",
                "concurrency/idempotency",
                "async recovery",
                "provider backlog or failure",
                "restricted audit evidence",
                "process/node restart",
                "multi-node",
                "telemetry failure",
                "do not create hardening work merely because a technology exists",
                "no hh id",
            ),
        ),
        (
            "performance envelope",
            "## S. Performance envelope",
            "## T. Future extension hooks",
            (
                "argon2id",
                "p90 ≤100ms",
                "excluding password hashing and provider latency",
                "registration, login, and recovery bursts",
                "verification delivery backlog",
                "abuse and rate pressure",
                "session reconstruction after restart or reconnect",
                "pmr allocation and merge",
                "bounded collections",
                "oq-035",
                "oq-039",
                "no new numeric thresholds are added",
            ),
        ),
        (
            "future extension hooks",
            "## T. Future extension hooks",
            "## U. Acceptance and exit criteria",
            (
                "owner-mediated domain seams",
                "oq-036",
                "social login",
                "passkeys",
                "full cap-004 export/deletion",
                "commercial work",
                "native clients",
                "generic tenancy",
                "fp-002",
                "adds no new domain, capability, feature pack, or shared-write owner",
                "remain future-only",
            ),
        ),
    )
    dimension_issues: list[str] = []
    for label, heading, next_heading, required_markers in delivery_dimensions:
        start = candidate.find(heading)
        end = candidate.find(next_heading, start + len(heading)) if start >= 0 else -1
        if start < 0 or end < 0:
            dimension_issues.append(f"candidate {label} section is missing or out of order")
            continue
        section = candidate[start:end].casefold()
        missing = [marker for marker in required_markers if marker.casefold() not in section]
        if missing:
            dimension_issues.append(
                f"candidate {label} contract is incomplete; missing {', '.join(missing)}"
            )
    check(
        "fp001_phase7c_candidate_delivery_dimensions",
        dimension_issues,
        "proof obligations, outcome-level slices, evidence-led hardening, sourced performance pressures, and bounded extension hooks are explicit",
        candidate_path,
    )

    evidence_issues: list[str] = []
    archive_rel = expected_rule["reconciliation_archive_path"]
    archive = root / archive_rel
    working = docs / "working" / "FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
    archive_hash = expected_rule["reconciliation_archive_sha256"]
    if not archive.is_file() or sha256_file(archive) != archive_hash:
        evidence_issues.append("immutable Phase 7B candidate archive hash changed")
    if not working.is_file() or not archive.is_file():
        evidence_issues.append("certified Phase 7B current route or immutable candidate archive is missing")
    else:
        def semantic_body(path: Path) -> str:
            value = path.read_text(encoding="utf-8")
            return value.split("## 1. Baseline and authority set", 1)[1].split("## 8. Candidate result and certification boundary", 1)[0]
        try:
            if semantic_body(working) != semantic_body(archive):
                evidence_issues.append("Phase 7C changed the certified Phase 7B reconciliation semantic body")
        except IndexError:
            evidence_issues.append("Phase 7B reconciliation semantic boundaries are malformed")
    for relative, digest in rules.get("predecessor_archives_sha256", {}).items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != digest:
            evidence_issues.append(f"direct-predecessor archive is missing or changed: {relative}")
    check(
        "fp001_phase7c_candidate_immutable_inputs",
        evidence_issues,
        "certified Phase 7B evidence and byte-identical immediate predecessor archives are preserved",
        archive_rel,
    )

    gate_issues: list[str] = []
    try:
        oq029 = candidate.split("## V. Downstream gates", 1)[1].split("## W. STOP conditions", 1)[0]
    except IndexError:
        oq029 = ""
        gate_issues.append("candidate downstream-gate section is missing")
    for token in ("OQ-029", "exact retention duration", "STOP", "route"):
        if token.lower() not in oq029.lower():
            gate_issues.append(f"OQ-029 fail-closed retention rule omits {token!r}")
    oq029_lines = [line.strip() for line in oq029.splitlines() if line.lstrip().startswith("- **OQ-029:**")]
    if len(oq029_lines) != 1 or not re.search(
        r"(?i)exact retention duration.*\bSTOP\b.*\broute\b",
        oq029_lines[0] if len(oq029_lines) == 1 else "",
    ):
        gate_issues.append("OQ-029 does not bind the exact-retention-duration STOP and route to its own disposition")
    for token in (
        "OQ-030", "OQ-031", "OQ-032", "later export/deletion",
        "OQ-034", "resolved", "executable proof", "Phase 8",
        "OQ-035", "security/operations", "OQ-036", "provider", "channel", "retry",
        "OQ-037", "RPO/RTO", "OQ-038", "FP-006", "OQ-039", "performance",
    ):
        if token.lower() not in oq029.lower():
            gate_issues.append(f"candidate downstream route omits {token!r}")
    if "no choice is made between" not in candidate or "REUSE_EXISTING_PROOF" not in candidate or "NEW_TRACER_BULLET" not in candidate:
        gate_issues.append("candidate does not explicitly defer proof-vehicle selection")
    proof_statuses = re.findall(r"(?im)^PROOF CLASSIFICATION:[ \t]*(.+?)[ \t]*$", candidate)
    if proof_statuses and any(status.strip().upper() != "NOT FINALISED" for status in proof_statuses):
        gate_issues.append("candidate contains a premature proof classification")
    if "no tracer bullet id or proof artifact is created" not in candidate.casefold():
        gate_issues.append("candidate creates or fails to prohibit a Tracer Bullet/proof artifact")
    phase8_statuses = re.findall(
        r"(?im)^PHASE 8(?:\s*/\s*APPLICATION IMPLEMENTATION)?[ \t]*:[ \t]*(.+?)[ \t]*$",
        candidate,
    )
    if not phase8_statuses or any(status.strip().upper() != "UNAUTHORISED" for status in phase8_statuses):
        gate_issues.append("candidate removes the Phase 8/application implementation stop")
    mechanisms = ("Ash Resource", "Ash action", "database table", "Ecto schema", "Phoenix route", "LiveView module", "Oban worker", "Terraform", "queue name", "provider SDK")
    for line in candidate.splitlines():
        folded_line = line.casefold()
        if any(marker in folded_line for marker in mechanisms) and not re.search(r"\b(?:no|none|not|never|downstream|unfrozen|unselected)\b", folded_line):
            if re.search(r"\b(?:select(?:s|ed)?|choos(?:e|es|en)|use(?:s|d)?|implement(?:s|ed)?|configure(?:s|d)?)\b", folded_line):
                gate_issues.append("candidate positively selects a prohibited implementation mechanism")
                break
    check(
        "fp001_phase7c_candidate_downstream_gates",
        gate_issues,
        "retention authority, downstream OQs, proof and Phase 8 gates remain explicit",
        candidate_path,
    )

    route_issues: list[str] = []
    expected_retired = [
        "docs/00_platform/02_OPEN_WORK_v1.2.69.md",
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.11.md",
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.13.md",
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.13.md",
        "docs/00_platform/02_OPEN_WORK_v1.2.70.md",
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.12.md",
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.14.md",
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.14.md",
        "docs/00_platform/02_OPEN_WORK_v1.2.71.md",
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.13.md",
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.15.md",
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.15.md",
        "docs/00_platform/05_ROADMAP_v1.2.2.md",
        "docs/00_platform/02_OPEN_WORK_v1.2.72.md",
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.14.md",
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md",
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.16.md",
        "docs/00_platform/02_OPEN_WORK_v1.2.73.md",
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.15.md",
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md",
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.17.md",
    ]
    phase8_candidate_current = any(
        entry.get("document_id") == "OPEN_WORK"
        and entry.get("lifecycle", "current") != "historical"
        and entry.get("semver") in {"1.2.77", "1.2.78"}
        for entry in _all_entries(manifest)
    )
    if phase8_candidate_current:
        expected_retired.extend((
            "docs/00_platform/02_OPEN_WORK_v1.2.74.md",
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
            "docs/00_platform/02_OPEN_WORK_v1.2.75.md",
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.17.md",
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.19.md",
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.19.md",
            "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.0.md",
            "docs/00_platform/02_OPEN_WORK_v1.2.76.md",
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.18.md",
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.20.md",
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.20.md",
            "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.1.md",
        ))
    if _fp001_phase8_approved_status_successor_is_current(manifest):
        expected_retired.extend((
            "docs/00_platform/02_OPEN_WORK_v1.2.77.md",
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.19.md",
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md",
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md",
        ))
    if _fp001_phase8_execution_status_successor_is_current(manifest):
        expected_retired = list(graph_rules.get("retired_current_predecessor_paths", []))
    if graph_rules.get("retired_current_predecessor_paths") != expected_retired:
        route_issues.append("manifest does not pin the retired current-predecessor paths")
    for relative in expected_retired:
        if (root / relative).exists():
            route_issues.append(f"unarchived retired predecessor remains at a current path: {relative}")
    if _fp001_phase8_execution_status_successor_is_current(manifest):
        current_routes = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {}).get("current_routes", {})
        expected_current_paths = {
            "current_delivery_atlas": Path(current_routes["delivery_atlas"]).relative_to("docs/00_platform").as_posix(),
            "current_fp001_skeleton": Path(current_routes["fp001_skeleton"]).relative_to("docs/00_platform").as_posix(),
            "current_harden_02": Path(current_routes["harden_02"]).relative_to("docs/00_platform").as_posix(),
        }
        current_open_work_entry = _active_open_work_entry(manifest)
        open_work_version = current_open_work_entry.get("semver", "") if current_open_work_entry else ""
    else:
        expected_current_paths = {
            "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.20.md" if _fp001_phase8_approved_status_successor_is_current(manifest) else "working/DELIVERY_ATLAS_WORKING_v0.4.19.md" if phase8_candidate_current else "working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
            "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md" if _fp001_phase8_approved_status_successor_is_current(manifest) else "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md" if phase8_candidate_current else "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
            "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.22.md" if _fp001_phase8_approved_status_successor_is_current(manifest) else "working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md" if phase8_candidate_current else "working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        }
        open_work_version = "1.2.78" if _fp001_phase8_approved_status_successor_is_current(manifest) else "1.2.77" if phase8_candidate_current else "1.2.74"
    open_work_path = docs / f"02_OPEN_WORK_v{open_work_version}.md"
    open_work = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() else ""
    state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work,
        re.DOTALL,
    )
    try:
        state = json.loads(state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        state = {}
    for key, value in expected_current_paths.items():
        if state.get(key) != value:
            route_issues.append(f"Open Work current route {key!r} does not point to its successor")
    if state.get("phase_7c_execution_tracker_state") != "CLOSED / COMPLETED":
        route_issues.append("Open Work current route does not close tracker #124")
    for relative in expected_retired:
        if "/working/" in relative and relative in graph_rules.get("navigation_document_paths", []):
            route_issues.append(f"manifest still routes retired predecessor as current navigation: {relative}")
    readme_path = docs / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    current_state = _markdown_h2_section(readme_text, "Current State") or ""
    if f"02_OPEN_WORK_v{open_work_version}.md" not in readme_text:
        route_issues.append(f"README does not route Open Work v{open_work_version}")
    for path in expected_current_paths.values():
        if Path(path).name not in readme_text:
            route_issues.append(f"README does not route current successor {path}")
    if re.search(r"(?im)^.*#124[^\n]{0,120}\bOPEN\b.*$", current_state):
        route_issues.append("README current state projects issue #124 as OPEN")
    check(
        "fp001_phase7c_candidate_current_routes",
        route_issues,
        "current routing uses the Phase 7C tracker-closure successors; retired predecessor paths remain archive-qualified",
        "docs/00_platform/README.md",
    )

def _fp001_protected_historical_evidence_issues(
    root: Path,
    promotion: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> list[str]:
    """Keep prior FP-001 certification evidence pinned through the Phase 7C successor."""

    issues: list[str] = []
    artifacts = promotion.get("protected_historical_evidence_sha256", {})
    if not isinstance(artifacts, dict):
        return ["manifest historical FP-001 evidence hashes are malformed"]
    serialized = json.dumps(artifacts, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if hashlib.sha256(serialized).hexdigest() != "8c94f683e27863d94df439e8b1c7f66ae62b025a475e850341eeba8e6d499706":
        issues.append("manifest does not preserve the pinned historical FP-001 certification evidence map")
    for relative, expected_hash in artifacts.items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != expected_hash:
            issues.append(f"protected historical FP-001 evidence is missing or changed: {relative}")

    groups = {
        "fp001_pmr_predecessor_archives": (
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md",
        ),
        "identity_v014_promotion_archives": (
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.56.md",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.3.8.md",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.0.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
        ),
        "communications_start_status_archives": (
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.57.md",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.3.9.md",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.1.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md",
        ),
        "communications_v010_promotion_archives": (
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.58.md",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.0.md",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.4.md",
            "docs/00_platform/archive/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        ),
        "audit_v010_promotion_archives": (
            "docs/00_platform/archive/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.64.md",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.6.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.8.md",
        ),
    }
    if set(artifacts) != {path for paths in groups.values() for path in paths}:
        issues.append("manifest protected historical FP-001 evidence paths are missing, substituted or unexpected")
    group_diagnostics = {
        "fp001_pmr_predecessor_archives": "FP-001 PMR predecessor archive bytes changed",
        "identity_v014_promotion_archives": "Identity v0.1.4 promotion archive bytes changed",
        "communications_start_status_archives": "Communications-start predecessor bytes changed",
        "communications_v010_promotion_archives": "Communications v0.1.0 promotion archive bytes changed",
        "audit_v010_promotion_archives": "Audit promotion archive bytes changed",
    }
    for rule_name, paths in groups.items():
        expected_group = {path: artifacts[path] for path in paths if path in artifacts}
        if integrity_rules.get(rule_name) != expected_group:
            issues.append(f"manifest {rule_name} no longer matches protected historical certification evidence")
        for relative in paths:
            path = root / relative
            expected_hash = artifacts.get(relative)
            if path.is_file() and isinstance(expected_hash, str) and sha256_file(path) != expected_hash:
                issues.append(f"{group_diagnostics[rule_name]}: {relative}")
    return issues


def _fp001_pinned_historical_proof_contract_archives(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> set[str]:
    """Return proof-contract archives whose lifecycle and immutable bytes are pinned."""

    phase8 = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    if not isinstance(phase8, dict):
        return set()

    predecessor_archives = phase8.get("predecessor_archives_sha256", {})
    if not isinstance(predecessor_archives, dict):
        predecessor_archives = {}
    expected: dict[str, str] = {
        relative: digest
        for relative, digest in predecessor_archives.items()
        if isinstance(relative, str)
        and isinstance(digest, str)
        and re.search(r"FP-001_TRACER_BULLET_CONTRACT_WORKING_v\d+\.\d+\.\d+\.md$", relative)
    }
    reviewed_path = phase8.get("reviewed_candidate_archive_path")
    reviewed_digest = phase8.get("reviewed_candidate_archive_sha256")
    if isinstance(reviewed_path, str) and isinstance(reviewed_digest, str):
        expected[reviewed_path] = reviewed_digest

    entries = [
        entry
        for entry in _all_entries(manifest)
        if entry.get("lifecycle") == "historical"
    ]
    pinned: set[str] = set()
    for relative, digest in expected.items():
        path = root / relative
        matches = [entry for entry in entries if _relative_path(entry) == relative]
        if (
            len(matches) == 1
            and path.is_file()
            and sha256_file(path) == digest
            and matches[0].get("authority_class") == "FP001_PHASE8_PROOF_CONTRACT_HISTORICAL"
            and matches[0].get("graph_policy") == "frozen_provenance"
            and matches[0].get("sha256") == digest
            and matches[0].get("provenance_sha256") == digest
        ):
            pinned.add(relative)
    return pinned


def _check_roadmap_proof_classification_lifecycle(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Preserve the classification decision and its immutable source boundary."""

    rule = integrity_rules.get("roadmap_proof_classification_lifecycle", {})
    issues: list[str] = []
    base_sha = "24a9ad925ee1ab6d75ddb44bae6df0b4f3d09bca"
    expected_routes = {
        "open_work": "docs/00_platform/02_OPEN_WORK_v1.2.77.md",
        "delivery_atlas": "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.19.md",
        "fp001_skeleton": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md",
        "harden_02": "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md",
    }
    expected_upstream = {
        "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md": "249f5985ff1e8971e1ac4437e4bbebd5a3db9254ab25a2238e135cb7a7ae5f4b",
        "docs/00_platform/00_PLATFORM_v1.8.0.md": "cb93abfee9a6337a7f2a23c16f35413b8b2ea84608974fcf5a0033822578905e",
        "docs/00_platform/01_DECISIONS_v1.8.0.md": "123d3a622f89c22e364df565b87117c22244378c5c51b10d621597909b569140",
        "docs/00_platform/03_ARCHITECTURE_v1.1.1.md": "342d02a7946f99aca9e6683647fc3a2505901b3d0cc2d13c21d807442025f0b3",
        "docs/00_platform/04_DOMAIN_MAP_v1.2.0.md": "e09e14ee0a773c5855257c48685cf3a75d413c983a98d22a56b42af57dc2c078",
        "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md": "26ff1e7a7e40945e501793c2bfb2ede9c01ae03f7949383ae724e3b031fa4faa",
    }
    expected_predecessors = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.72.md": "ea515aff852cdf4e74714793ac3d390d6291a37903f0a1c15e887cdb9f44da5e",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.14.md": "a12ea6f734ad192a5b735bda8018cac3db7fc37d662f75643eb9758310414894",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md": "8bc2b7c61d6feba1c61ea5233677dd8b7344d0704426d8d113e8e5f2b2395f6e",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.16.md": "75b6e739b82a63fe85bb7d2e20f862883bd3e60cb00b2fcce72e7f92849c5cea",
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.73.md": "86b8a0b9d181ad6551b5174d3856a1d700209d583970dcc90a7aaa4b72ef8577",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.15.md": "a5b7e2d94b29e077adb6d85605f2cbbbf139dff4983711ee73bfedce2b9bba26",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md": "99c72571ef4243e6d765c4d5dd4b0e5b3dce73d993662916d8bed839ebd2ad55",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.17.md": "a80c6870a6b86dc4e871d0357a11edc877379085b846a348e750ab037741e1d7",
    }
    expected_jit = {
        "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "aa6c4a52518225a2d5bbe86734410e5e9e330e29613b1c1e150174e2e3a12046",
        "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "cc664c1e5d148c1a8f30f2a8d769645646162ff029494a2187e0a65775c27c83",
        "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md": "3560e0cb147e21cdaa149b7e1c2abe43ad03af04619d08175ef0544279fa0d0f",
    }
    baseline_facts = {
        "classification_baseline_sha": base_sha,
        "classification_baseline_tree_sha": "48069be0cab399a00464f2e0f40be584a0349615",
        "classification_baseline_top_level_paths": [".github", ".gitignore", "docs", "tests", "tools"],
        "classification_baseline_executable_source_paths": [],
        "classification_baseline_has_mix_exs": False,
        "classification_baseline_has_elixir_defmodule_implementation": False,
        "classification_candidate_branch": "governance/fp001-architectural-proof-classification",
    }
    expected_fixed = {
        "base_sha": base_sha,
        "roadmap_current_path": "docs/00_platform/05_ROADMAP_v1.2.3.md",
        "roadmap_current_sha256": "044b5c6308d59253cb0e5ae86d53e13611fb84dec04135b1175880d7881593c2",
        "roadmap_predecessor_archive_path": "docs/00_platform/archive/05_ROADMAP_v1.2.2.md",
        "roadmap_predecessor_archive_sha256": "4225fad688589d3c66733527303cbda39ef3c8bf52b78c4cc372c0736d202cdc",
        "phase7c_contract_path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "current_routes": expected_routes,
        "protected_upstream_authority_sha256": expected_upstream,
        **baseline_facts,
        "predecessor_archives_sha256": expected_predecessors,
        "pr125_candidate_archive_path": "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "pr125_candidate_archive_sha256": "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
        "classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "phase8": "UNAUTHORISED",
        "application_implementation": "UNAUTHORISED",
        "development_entry_hard_stop_condition_9": "SATISFIED",
        "remaining_development_entry_hard_stop_conditions": "NOT EVALUATED / MUST PASS BEFORE PHASE 8",
        "next_governance_action": "DEVELOPMENT ENTRY HARD STOP EVALUATION",
        "protected_required_jit_dossier_sha256": expected_jit,
        "candidate_contract_path": "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md",
    }
    if not isinstance(rule, dict) or any(rule.get(key) != value for key, value in expected_fixed.items()):
        issues.append("manifest does not pin the classification baseline, authority, selected vehicle and historical lifecycle")

    route_hashes = rule.get("current_route_sha256", {}) if isinstance(rule, dict) else {}
    contract_path = str(expected_fixed["phase7c_contract_path"])
    if not isinstance(route_hashes, dict) or set(route_hashes) != {*expected_routes.values(), contract_path}:
        issues.append("manifest current-route hash map is incomplete or contains an unrouteable path")

    roadmap_path = str(expected_fixed["roadmap_current_path"])
    roadmap_file = root / roadmap_path
    roadmap = roadmap_file.read_text(encoding="utf-8") if roadmap_file.is_file() else ""
    if not roadmap_file.is_file() or sha256_file(roadmap_file) != expected_fixed["roadmap_current_sha256"]:
        issues.append("current Roadmap v1.2.3 is missing, changed or no longer provisional")
    predecessor_roadmap = root / str(expected_fixed["roadmap_predecessor_archive_path"])
    if not predecessor_roadmap.is_file() or sha256_file(predecessor_roadmap) != expected_fixed["roadmap_predecessor_archive_sha256"]:
        issues.append("archived Roadmap v1.2.2 is missing or its immutable bytes changed")
    current_roadmap_entry = next((entry for entry in manifest.get("governing_documents", []) if entry.get("document_id") == "ROADMAP"), None)
    if (not isinstance(current_roadmap_entry, dict) or _relative_path(current_roadmap_entry) != roadmap_path
            or current_roadmap_entry.get("semver") != "1.2.3" or current_roadmap_entry.get("superseded_version") != "1.2.2"):
        issues.append("manifest does not route Roadmap v1.2.3 as the unchanged current successor")
    if "**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET`. This direction is provisional." not in roadmap:
        issues.append("Roadmap v1.2.3 anticipation is missing or no longer provisional")
    if "Anticipated proof labels are provisional." not in roadmap:
        issues.append("Roadmap no longer distinguishes anticipation from classification")

    for relative, digest in expected_upstream.items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != digest:
            issues.append(f"protected Product, Decision, Architecture or Domain authority changed: {relative}")
    for relative, digest in expected_jit.items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != digest:
            issues.append(f"current required FP-001 JIT dossier changed: {relative}")
    for relative, digest in expected_predecessors.items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != digest:
            issues.append(f"direct predecessor archive is missing or changed: {relative}")

    for key, relative in expected_routes.items():
        path = root / relative
        if not path.is_file():
            issues.append(f"current route {key!r} is missing: {relative}")
        elif route_hashes.get(relative) != sha256_file(path):
            issues.append(f"manifest current-route hash differs: {relative}")
    current_contract = root / contract_path
    actual_contract_hash = sha256_file(current_contract) if current_contract.is_file() else None
    if (actual_contract_hash is None or rule.get("phase7c_contract_sha256") != actual_contract_hash
            or route_hashes.get(contract_path) != actual_contract_hash):
        issues.append("current Final Feature Pack Contract manifest SHA-256 pins disagree with actual bytes")

    candidate_path = str(expected_fixed["candidate_contract_path"])
    candidate = root / candidate_path
    if not candidate.is_file():
        issues.append(f"routed TB-001 candidate contract is missing: {candidate_path}")
    authority_entries = [entry for entry in _all_entries(manifest) if _relative_path(entry) == candidate_path and entry.get("lifecycle", "current") != "historical"]
    if authority_entries:
        issues.append("TB-001 candidate contract is incorrectly promoted into authority-document records")

    candidate_archive_path = str(expected_fixed["pr125_candidate_archive_path"])
    candidate_archive = root / candidate_archive_path
    if not candidate_archive.is_file() or sha256_file(candidate_archive) != expected_fixed["pr125_candidate_archive_sha256"]:
        issues.append("immutable PR #125 candidate archive is missing or changed")

    historical_proof_contract_archives = _fp001_pinned_historical_proof_contract_archives(
        root,
        manifest,
        integrity_rules,
    )
    platform_docs_root = root / "docs/00_platform"
    if platform_docs_root.is_dir():
        for path in platform_docs_root.rglob("*"):
            if not path.is_file() or not re.search(r"(?:TRACER_BULLET|ARCHITECTURAL_PROOF)(?:[-_\.]|$)", path.name, re.IGNORECASE):
                continue
            relative = path.relative_to(root).as_posix()
            if relative == candidate_path or relative in historical_proof_contract_archives:
                continue
            issues.append(f"Tracer Bullet or architectural-proof artifact exists: {relative}")
            break

    _record_check(
        report,
        "roadmap_proof_classification_lifecycle",
        not issues,
        "FP-001 classification remains NEW_TRACER_BULLET, its higher authority is unchanged and TB-001 is the sole routed proof-contract candidate"
        if not issues else "; ".join(issues),
        path=roadmap_path,
    )


APPLICATION_SOURCE_DIRECTORY_NAMES = frozenset({"lib", "src", "app", "apps", "priv", "migrations", "assets"})


def _executable_application_source_paths(root: Path) -> list[str]:
    """Return executable/bootstrap source paths present in the tree (authorisation is decided by the caller)."""
    found: list[str] = []
    for directory, child_directories, filenames in os.walk(root):
        child_directories[:] = [name for name in child_directories if name != ".git"]
        relative_directory = Path(directory).relative_to(root)
        for filename in filenames:
            relative_path = relative_directory / filename
            if (
                filename == "mix.exs"
                or filename.endswith((".ex", ".exs"))
                or set(relative_path.parts) & APPLICATION_SOURCE_DIRECTORY_NAMES
            ):
                found.append(relative_path.as_posix())
    return sorted(found)


def _check_fp001_development_entry_hard_stop_lifecycle(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Pin Development Entry Hard Stop PASS and bounded Phase 8 authorisation."""

    rule = integrity_rules.get("fp001_development_entry_hard_stop_lifecycle", {})
    issues: list[str] = []
    base_sha = "675a8c50ac53a995a48e4d262df42065f8ccd412"
    promoted_open_work = root / "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md"
    if not promoted_open_work.is_file():
        _record_check(
            report,
            "fp001_development_entry_hard_stop_lifecycle",
            True,
            "hard-stop promotion routes are not present in this tree",
        )
        return
    expected_routes = {
        "open_work": "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md",
        "delivery_atlas": "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.16.md",
        "fp001_skeleton": "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
        "harden_02": "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
    }
    expected_predecessors = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.73.md": "86b8a0b9d181ad6551b5174d3856a1d700209d583970dcc90a7aaa4b72ef8577",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.15.md": "a5b7e2d94b29e077adb6d85605f2cbbbf139dff4983711ee73bfedce2b9bba26",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md": "99c72571ef4243e6d765c4d5dd4b0e5b3dce73d993662916d8bed839ebd2ad55",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.17.md": "a80c6870a6b86dc4e871d0357a11edc877379085b846a348e750ab037741e1d7",
    }
    expected_fixed = {
        "base_sha": base_sha,
        "hard_stop_evaluation_baseline_sha": base_sha,
        "current_routes": expected_routes,
        "phase7c_contract_path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "phase7c_contract_sha256": "9b2c1a6c16df3a48f041403fd336df926132bba46168e07b55acce148c4f59c2",
        "pr125_candidate_archive_path": "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
        "pr125_candidate_archive_sha256": "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "predecessor_archives_sha256": expected_predecessors,
        "authorization_scope_note": "APPLICATION IMPLEMENTATION AUTHORISED only for bounded Phase 8 Architectural Proof / NEW_TRACER_BULLET",
    }
    if not isinstance(rule, dict):
        issues.append("manifest hard-stop lifecycle rule is missing")
        rule = {}
    for key, value in expected_fixed.items():
        if key == "predecessor_archives_sha256":
            if rule.get(key) != value:
                issues.append("manifest hard-stop predecessor archives are wrong")
        elif rule.get(key) != value:
            issues.append(f"manifest hard-stop lifecycle field {key!r} is wrong")

    route_hashes = rule.get("current_route_sha256", {}) if isinstance(rule, dict) else {}
    contract_path = str(expected_fixed["phase7c_contract_path"])
    expected_route_hash_keys = {*expected_routes.values(), contract_path}
    if not isinstance(route_hashes, dict) or set(route_hashes) != expected_route_hash_keys:
        issues.append("manifest hard-stop current-route hash map is incomplete")

    route_docs: dict[str, str] = {}
    for key, relative in expected_routes.items():
        path = root / relative
        if not path.is_file():
            issues.append(f"hard-stop current route {key!r} is missing: {relative}")
            route_docs[key] = ""
            continue
        route_docs[key] = path.read_text(encoding="utf-8")
        if isinstance(route_hashes, dict) and route_hashes.get(relative) != sha256_file(path):
            issues.append(f"manifest hard-stop route hash differs: {relative}")

    contract_file = root / contract_path
    contract = contract_file.read_text(encoding="utf-8") if contract_file.is_file() else ""
    if not contract_file.is_file() or sha256_file(contract_file) != expected_fixed["phase7c_contract_sha256"]:
        issues.append("hard-stop Final Contract bytes disagree with manifest pin")
    if "The proof vehicle and final proof classification remain NOT FINALISED." not in contract:
        issues.append("Final Contract §P freeze-time NOT FINALISED semantics were altered")

    for relative, digest in expected_predecessors.items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != digest:
            issues.append(f"hard-stop direct predecessor archive is missing or changed: {relative}")
        retired_current = relative.replace("/archive/", "/")
        if (root / retired_current).exists():
            issues.append(f"hard-stop predecessor remains at retired current path: {retired_current}")

    open_work = route_docs.get("open_work", "")
    state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work,
        re.DOTALL,
    )
    try:
        state = json.loads(state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        state = {}
    required_state = {
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
    }
    for key, value in required_state.items():
        if state.get(key) != value:
            issues.append(f"Open Work lifecycle state missing hard-stop field {key!r}")

    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    active = open_work[active_start:active_end] if active_start >= 0 and active_end > active_start else ""
    required_active = (
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
        "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
    )
    for token in required_active:
        if token not in active:
            issues.append(f"Open Work active route omits hard-stop state {token!r}")
    if "OQ-035" not in active or "OQ-036" not in active:
        issues.append("Open Work active route omits release-only OQ-035/OQ-036 gates")
    if re.search(r"\bTB-\d{3,}\b", active):
        issues.append("Open Work active route introduces a Tracer Bullet identifier")

    readme_path = root / "docs/00_platform/README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        current_state = _markdown_h2_section(readme, "Current State") or ""
        for token in (
            "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
            "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
            "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
            "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
            "TB-001 is CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
            "PROOF EXECUTION: NOT STARTED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        ):
            if token not in current_state:
                issues.append(f"README current state omits hard-stop state {token!r}")
    else:
        issues.append("README is missing for hard-stop promotion coherence")

    atlas = route_docs.get("delivery_atlas", "")
    atlas_jit_start = atlas.find("**JIT Boundary:**")
    atlas_jit_end = atlas.find("\n### CAP-002", atlas_jit_start + 1)
    if atlas_jit_start < 0 or atlas_jit_end < 0:
        issues.append("Atlas FP-001 JIT boundary is missing or malformed")
    else:
        atlas_jit_boundary = atlas[atlas_jit_start:atlas_jit_end]
        if any(
            phrase in atlas_jit_boundary
            for phrase in (
                "Classification satisfies only Development Entry Hard Stop condition 9",
                "remaining conditions are not evaluated",
                "Phase 8/application implementation remains UNAUTHORISED",
                "Development Entry Hard Stop evaluation is next",
            )
        ):
            issues.append("Atlas FP-001 JIT boundary projects the pre-hard-stop state")
        atlas_jit_required = (
            "Development Entry Hard Stop is PASS / ALL 10 CONDITIONS SATISFIED",
            "Phase 8 Architectural Proof is AUTHORISED",
            "application implementation is AUTHORISED only inside that bounded NEW_TRACER_BULLET proof",
            "Tracer Bullet is REQUIRED / NOT YET DEFINED with no ID",
            "proof execution is NOT STARTED",
            "NEW_TRACER_BULLET proof contract/task definition",
            "Current Open Work v1.2.74 records this authority",
        )
        for token in atlas_jit_required:
            if token not in atlas_jit_boundary:
                issues.append(f"Atlas FP-001 JIT boundary omits current state {token!r}")

    skeleton = route_docs.get("fp001_skeleton", "")
    skeleton_current = _markdown_h2_section(skeleton, "v0.1.18 current-route status") or ""
    skeleton_current_required = (
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "TRACER BULLET: REQUIRED / NOT YET DEFINED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
    )
    for token in skeleton_current_required:
        if token not in skeleton_current:
            issues.append(f"Skeleton v0.1.18 current route omits state {token!r}")

    harden = route_docs.get("harden_02", "")
    harden_current_sections = {
        "§18": _markdown_h2_section(harden, "18. Downstream consequence") or "",
        "§23": _markdown_h2_section(harden, "23. FP-001 Phase 7B reconciliation current route") or "",
    }
    harden_current_required = (
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
        "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
    )
    for section_name, section in harden_current_sections.items():
        for token in harden_current_required:
            if token not in section:
                issues.append(f"HARDEN-02 {section_name} current route omits state {token!r}")
        if any(
            phrase in section
            for phrase in (
                "satisfies only Development Entry Hard Stop condition 9",
                "Phase 8/application implementation remains UNAUTHORISED",
                "Development Entry Hard Stop evaluation remains next",
            )
        ):
            issues.append(f"HARDEN-02 {section_name} current route projects the pre-hard-stop state")

    # Authorisation is derived only from repository-governed lifecycle state.
    application_authorised = (
        isinstance(rule, dict)
        and rule.get("phase8") == "AUTHORISED"
        and rule.get("application_implementation") == "AUTHORISED"
        and state.get("phase8") == "AUTHORISED"
        and state.get("application_implementation") == "AUTHORISED"
        and state.get("development_entry_hard_stop_status") == "PASS / ALL 10 CONDITIONS SATISFIED"
    )
    if not application_authorised:
        issues.append("governed hard-stop authorisation state is incomplete or inconsistent")

    # Long-lived guard: executable source is permitted only when governed state authorises it.
    application_source_paths = _executable_application_source_paths(root)
    if application_source_paths and not application_authorised:
        issues.append(
            "executable application/bootstrap source present while application implementation is not authorised: "
            + ", ".join(application_source_paths)
        )

    open_work_entry = next((entry for entry in manifest.get("governing_documents", []) if entry.get("document_id") == "OPEN_WORK"), None)
    if (
        not isinstance(open_work_entry, dict)
        or _relative_path(open_work_entry) != "docs/00_platform/02_OPEN_WORK_v1.2.77.md"
        or open_work_entry.get("semver") != "1.2.77"
        or open_work_entry.get("superseded_version") != "1.2.76"
    ):
        issues.append("manifest Open Work lineage is not v1.2.76 → v1.2.77")

    _record_check(
        report,
        "fp001_development_entry_hard_stop_lifecycle",
        not issues,
        "FP-001 Development Entry Hard Stop is PASS; Phase 8 Architectural Proof is authorised within bounded scope"
        if not issues
        else "; ".join(issues),
        path="docs/00_platform/02_OPEN_WORK_v1.2.77.md",
    )


def _fp001_phase8_proof_contract_content_issues(text: str) -> list[str]:
    """Check the frozen Phase 8 design and complete proof-task boundary."""

    folded = text.casefold()
    authority_marker = "## 1. Authority and provenance"
    if authority_marker not in text:
        issues = ["TB-001 contract omits the ordered authority hierarchy"]
        authority = ""
    else:
        authority = text.split(authority_marker, 1)[1].split("\n## ", 1)[0].casefold()
        hierarchy = (
            "1. product law:",
            "2. architecture law and current synthesis:",
            "3. domain law:",
            "4. roadmap:",
            "5. supporting operating, frontend and engineering contracts:",
            "6. current open work.",
            "7. approved fp-001 planning contracts listed below.",
            "8. this proof contract.",
            "9. proof evidence produced under it.",
            "10. implementation.",
        )
        hierarchy_positions = [authority.find(item) for item in hierarchy]
        issues = []
        if any(position < 0 for position in hierarchy_positions) or hierarchy_positions != sorted(hierarchy_positions):
            issues.append(
                "TB-001 authority hierarchy must place current Open Work, approved FP-001 contracts, the proof contract, proof evidence and implementation in order"
            )

    decision_sources = {
        "Q1–Q6": "e8215515-4a76-4dde-b809-ab4f17932dd9",
        "Q7–Q11": "e84a1ae5-8517-46c1-bb33-01d3fcc8b950",
        "Q12–Q16": "60fba648-e589-4e67-a6e4-4dd3818e8115",
        "Q17–Q21": "b24f0a08-8493-4dc3-9885-b47be44eda0d",
        "Q22": "cc6d56dd-344f-41ff-8b2f-64246d7f1c5b",
        "Q23": "446a4cc7-d1b3-4a06-a0ea-3e25d8d3149f",
        "Q24": "e26ca691-0980-42de-80d0-3eec3d221d67",
        "Q25": "b468c38e-662a-43c0-a6a5-b3abbca72499",
        "Q26–Q27": "4464891a-f1ad-44c2-8b80-1601e3f991b1",
        "Q28–Q38": "82ba53ea-b6ca-4906-a024-c6ebfb6054b3",
        "Q39–Q47": "ca2db611-f846-4d84-83ba-fbdfa3d8c102",
        "Q48–Q56": "20f6110e-582e-4498-bcac-c8cdbd54d7d8",
        "Q57–Q62": "7e8dc117-7ea5-4a0b-acf9-c7fc0cd2c39b",
        "Q63–Q70": "f75834d8-1908-4661-9b8f-be1b81fb8b0a",
        "Q71–Q80": "d55613cf-8026-44e3-8f90-0d7bf687231d",
        "Q81–Q90": "b45e180f-180a-4126-b043-3f7d555517aa",
    }
    traceability_marker = "## Decision traceability"
    if traceability_marker not in text:
        issues.append("TB-001 contract omits the Q1–Q90 decision traceability section")
        traceability = ""
    else:
        traceability = text.split(traceability_marker, 1)[1].split("\n## ", 1)[0]
    for question_range, comment_id in decision_sources.items():
        row = next(
            (
                line
                for line in traceability.splitlines()
                if line.startswith("|") and question_range in line
            ),
            "",
        )
        if not row or comment_id not in row or "§" not in row:
            issues.append(
                f"TB-001 {question_range} traceability row must cite its accepted WELL-1 source and contract treatment"
            )

    required_clauses = (
        "one modular phoenix/ash application",
        "otp app `:new_you`",
        "application modules `newyou` and `newyouweb`",
        "one `newyou.repo`",
        "postgresql as durable business authority by default",
        "ordinary business mutation boundaries",
        "no ordinary direct repo/ecto/raw-sql alternate business-write api",
        "oban as the durable executor",
        "`ash_oban` for the phase 8 durable async integration",
        "ash signals are narrow coordination only",
        "never a universal event bus or business authority",
        "cross-domain listeners call the receiving domain's owning ash interface",
        "messageintent as communications authority and oban/job state as executor state",
        "password and magic-link authentication are both in phase 8",
        "registration establishes a password",
        "magic-link get, head, link preview, scanner and prefetch are passive",
        "only an explicit participant action reaches the purpose-bound consume action",
        "one current magic-login proof per account and purpose",
        "identity owns one session model",
        "verification does not implicitly log in",
        "single-use, expiry-, revocation- and supersession-aware",
        "email verification, password reset, recovery and primary-email-change confirmation",
        "pmr is account-owned durable truth",
        "allocation is concurrency-safe and externally opaque; a retired pmr is permanently non-reusable",
        "a deliveryattempt admission is durably committed before any provider i/o",
        "the authoritative postgresql transaction is never held open across provider i/o",
        "an ambiguous possibly-submitted provider operation enters reconciliation and blocks blind retry",
        "a provider response cannot verify an account, complete recovery, apply a primary-email change or create session authority",
        "required evidence admission is accepted before the protected effect",
        "failure to accept required e1 evidence blocks that effect",
        "a successful admission followed by a failed source effect remains truthful evidence of the admitted attempt",
        "the source transition, `evidenceobligation` and initial durable scheduling share the required acceptance boundary",
        "failure to commit that shared boundary leaves none of those three changes committed",
        "retry materialises the same obligation instead of multiplying assertions",
        "`evidencerecord` is append-only at the business layer",
        "one real minimal browser spine plus focused architectural fault probes",
        "all through the same production business path",
        "real postgresql, deterministic failure injection, genuine concurrent transactions wherever concurrency is the claim",
        "restart/reconnect proof",
        "deterministic provider ambiguity/reconciliation",
        "both e1 and e2 proof",
        "explicit authority-negative proof",
        "failure to preserve required postgresql atomicity, identity ownership, must-not-lose consequences, e1/e2 acceptance, safe provider ambiguity or current authority is `blocked / stop`",
        "there is no weighted score or partial architectural pass",
        "proof execution and proof certification remain separate lifecycle gates",
        "only a separate governed transition after certified proof can consider phase 9",
        "no implementation paths or proof command are assigned in this candidate because the repository has no phoenix/ash scaffold or mix task to inspect",
        "redis remains part of the accepted shared dev-core environment decision, but no phase 8 application/proof component will use it absent a concrete requirement",
        "registration uses one authoritative postgresql acceptance boundary: account, pmr, verification token, required communications messageintent, selected audit evidenceobligation and initial durable scheduling commit together or are absent together",
        "`ash_state_machine` is used selectively for genuine single-dimension lifecycles only",
        "`messageintent.dispatch_disposition` uses `ash_state_machine` for `open`, `held`, `reconciliation_required` and `closed`",
        "account's orthogonal state dimensions remain outside this machine",
        "`deliveryattempt` admission, invocation, provider observation and reconciliation conclusion remain separate dimensions outside that machine",
        "exits non-zero on invariant failure and emits concise machine-readable evidence suitable for ci/certification",
        "records the exact git sha, relevant runtime and dependency versions, pass/fail for every mandatory proof family, and the failing invariant/cut-point where applicable",
        "the exact mix command name remains unfrozen until the scaffold establishes the supported entrypoint",
    )
    issues.extend(
        f"TB-001 contract omits approved proof-design clause {clause!r}"
        for clause in required_clauses
        if clause not in folded
    )

    foundation_sections = {}
    for key, heading in (
        ("implementation", "## 7.2 Locked Phase-8 implementation foundation"),
        ("verification", "## 7.3 Locked verification foundation"),
    ):
        if heading not in text:
            issues.append(f"TB-001 contract omits the {key} foundation section")
            foundation_sections[key] = ""
        else:
            foundation_sections[key] = text.split(heading, 1)[1].split("\n## ", 1)[0].casefold()

    foundation_clauses = {
        "implementation": (
            "ports `4220–4239`",
            "primary phoenix port is `4220`",
            "worktrees use deterministic ports `4221–4239`",
            "startup fails closed if an assigned port is occupied",
            "`project_key=new_you`",
            "shared workstation `dev-core` owns `shared_local` postgresql",
            "repository connects to `dev-core` but never starts, stops, recreates, deletes or otherwise lifecycle-manages it",
            "`new_you_dev` / `new_you_dev`",
            "dev uses postgresql role/database `new_you_dev` / `new_you_dev` with `nocreatedb`",
            "`new_you_test` / `new_you_test`",
            "dev and test use isolated databases",
            "test `createdb` is disabled initially",
            "redis is not used for fp-001 phase 8 absent a demonstrated concrete requirement",
            "root `agents.md` newyou-controlled",
            "`.agents/skills/project-implementation/skill.md`",
            "`.agents/skills/code-change-verification/skill.md`",
            "usagerules in skills-only mode",
            "framework skills progressively when relevant",
            "installation and structural changes are igniter-first",
            "tidewave is mandatory dev-only agent tooling",
            "agent tooling at the direct deterministic endpoint `http://127.0.0.1:4220/tidewave/mcp`",
            "hexdocs mcp is deferred initially",
            "ash ai dev mcp is deferred",
            "direct sourceror is deferred",
            "added only on demonstrated need",
            "do not add `ash_ai` solely for another mcp endpoint",
            "unless a genuine low-level ast/source-transformation requirement appears",
            "transitive use through igniter is acceptable",
            "recheck current stable versions immediately before installation or pinning",
        ),
        "verification": (
            "`mix check` is the canonical fast check",
            "`mix check.deep` is the separate slower deep check",
            "cheap, repeatable, blocking checks and the ordinary test suite run fail-fast",
            "credo uses a curated high-signal configuration",
            "selected correctness/maintainability findings become blocking after a clean baseline",
            "subjective/noisy style remains advisory unless promoted",
            "sobelow begins from the phoenix application baseline",
            "materially applicable findings block unless explicitly reviewed or suppressed with rationale",
            "dialyxir/dialyzer belongs in the slower deep gate",
            "not the tight edit/test loop",
            "becomes required in pr ci after a clean approved baseline",
            "required ci runs the fast `mix check` gate before `mix check.deep`",
            "local hooks are optional convenience only, never correctness authority",
            "dedicated deterministic proof command/workflow separate from routine ci",
        ),
    }
    for section, clauses in foundation_clauses.items():
        body = foundation_sections[section]
        issues.extend(
            f"TB-001 {section} foundation omits locked clause {clause!r}"
            for clause in clauses
            if clause not in body
        )

    expected_resources = {
        "Identity": ["Account", "Identity-owned Token", "Session", "DeviceAssurance", "IdentityGrant", "RecoveryCase", "ReconciliationCase"],
        "Communications": ["MessageIntent", "DeliveryAttempt"],
        "Audit": ["EvidenceObligation", "EvidenceRecord"],
    }
    for domain, expected in expected_resources.items():
        marker = f"{domain} physical Resources are exactly"
        if marker not in text:
            issues.append(f"TB-001 contract omits the exact {domain} physical Resource set")
            continue
        declaration = text.split(marker, 1)[1].lstrip()
        if declaration.startswith(":"):
            declaration = declaration[1:].lstrip()
        if declaration.startswith("|"):
            table = declaration.split("\n\n", 1)[0]
            names = [match.group(1).strip() for match in re.finditer(r"(?m)^\|\s*([^|]+?)\s*\|", table)]
            names = [name for name in names if name.casefold() != "resource" and not set(name) <= {"-", ":"}]
        else:
            line = declaration.splitlines()[0]
            names = re.findall(r"`([^`]+)`", line)
        if names != expected:
            issues.append(f"TB-001 contract {domain} Resource set differs from the accepted list")

    scenario_families = (
        "Registration / PMR / reconciliation",
        "Proof capability / scanner / replay / supersession",
        "Session / login / revocation / restart",
        "Communications durability / backlog / provider ambiguity",
        "Audit E2",
        "Audit E1",
        "Recovery / primary-email change",
        "Non-enumeration / current Privacy re-read",
        "Source-authority / bypass negatives",
    )
    for family in scenario_families:
        if family.casefold() not in folded:
            issues.append(f"TB-001 contract omits mandatory scenario family {family!r}")

    required_scenario_row_clauses = {
        "Registration / PMR / reconciliation": (
            "verification Token",
            "Communications MessageIntent",
            "Audit EvidenceObligation",
            "initial durable scheduling commit together",
            "are absent together",
        ),
        "Audit E2": (
            "restricted accepted source consequence",
            "without secrets, excess payload or a second business truth",
        ),
        "Audit E1": (
            "security-hold release as the representative privileged effect",
            "bounded admission evidence",
            "without secrets, excess payload or a second business truth",
        ),
        "Non-enumeration / current Privacy re-read": (
            "non-enumerating",
            "support pressure",
            "consent changes",
            "current Privacy and Identity authority",
        ),
    }
    for family, clauses in required_scenario_row_clauses.items():
        row = next(
            (
                line.casefold()
                for line in text.splitlines()
                if line.startswith("|")
                and any(cell.strip().casefold() == family.casefold() for cell in line.split("|"))
            ),
            "",
        )
        for clause in clauses:
            if clause.casefold() not in row:
                issues.append(f"TB-001 {family} scenario row omits approved proof detail {clause!r}")

    return issues


def _check_fp001_phase8_proof_contract_lifecycle(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Verify the TB-001 task-definition route without claiming proof execution."""

    rule_name = "fp001_phase8_proof_contract_lifecycle"
    rule = integrity_rules.get(rule_name, {})
    issues: list[str] = []
    candidate_path = "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
    candidate_rel = "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
    current_routes = {
        "open_work": "docs/00_platform/02_OPEN_WORK_v1.2.77.md",
        "delivery_atlas": "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.19.md",
        "fp001_skeleton": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md",
        "harden_02": "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md",
        "final_feature_pack_contract": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
    }
    expected_fixed = {
        "candidate_path": candidate_path,
        "candidate_relative_path": candidate_rel,
        "candidate_version": "0.1.2",
        "candidate_lifecycle": "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "tracer_bullet_id": "TB-001",
        "id_allocation_authority": "Open Work v1.2.74 §§7, 9 and 12.30: Phase 8 uses TB-nnn for materially unproven paths; the prior promotion deferred the identifier and routed contract/task definition next. WELL-2 is that definition stage; Atlas lifecycle does not allocate IDs.",
        "candidate_base_main_sha": "0972864ef7f4638c96198e19a13977e0151e9726",
        "candidate_sha256": "f071d9edae90e3d5ae2030a98f79d9d1698aa68bf90ed9ce474a4f9120f82836",
        "proof_design": "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "proof_execution": "NOT STARTED",
        "proof_result": "NOT STARTED",
        "proof_certification": "NOT STARTED",
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        "phase8_execution_gate": "WAITING FOR CONTRACT APPROVAL AND A SEPARATE EXECUTION START",
        "current_routes": current_routes,
        "current_route_sha256": {
            "docs/00_platform/02_OPEN_WORK_v1.2.77.md": "083afb593ef2e073b1f3d2964637a35dd91004a7d28c2d501814ba35a767db48",
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.19.md": "f128e80165510e0934dd3076408b736a6cca88707226df199265715dc3f39922",
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md": "f744d32468d93eab25f3ac88c4d30ef981087ce22b4b75675f9ded38b3916c3b",
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md": "1549525632055bb8a44b905e9bac32a32901f84e17b0358579751d3ad6458096",
            "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md": "9b2c1a6c16df3a48f041403fd336df926132bba46168e07b55acce148c4f59c2",
            "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md": "f071d9edae90e3d5ae2030a98f79d9d1698aa68bf90ed9ce474a4f9120f82836",
        },
        "predecessor_archives_sha256": {
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md": "0872b5566f38a6c9cff53dbf7a236c0ba5b74308053aeb91796a45a3e9d9f852",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.16.md": "9636c1ed2a12f156ebeb31004e0d3823f7e2824b55d9e7107646d8178f5eab32",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md": "9401dc20a362115534dbb2ce16262c032debbe8dcb8e3d2fd5d9c87a1c1c836b",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.18.md": "4de81f097562def5dcba983031bee1052a34193f6c14ec6b2cfa81b6e8f79e58",
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.75.md": "ed8bb8c7ec30ace154c3eff3e4c90f851879dc4b9819f7f23a35cf81b0856045",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.17.md": "84d189e7589a29d2fa47978939d47bcadc6420048e7925eed4d1b7b8c7ef9c3c",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.19.md": "6595a04af2415aa89954c1f281907622a4dc58c613901fae2f084c6be8bfe835",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.19.md": "252c8ae8a74eea94f499d5a68d57323ba7810c8566ba1b27e47b4654dbc590bb",
            "docs/00_platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.0.md": "a33c8f7df067c123109a817bf54c08e3fb649449cf32f2b8294fee12ad601103",
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.76.md": "34defce057e0663fb325edb5cf5ed69b97720cb6abd78016864978c8adfe2bb3",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.18.md": "e1c440dc0dab6a0faa3e1179de75dfe07b3c5c391c8ef0a84d14b4a6d99f302b",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.20.md": "d3fd678e8eef6ac43109f294ed811587e323d3d2ff555459eb47e9c8324087f1",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.20.md": "d36133b08b496dd6c000c1e96ff5e78a352c4376e784efd2b3cab9838c710f31",
            "docs/00_platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.1.md": "817137641e33d9d74350e7f74a05778b3a80c0ea34e1e125dce905467c8974d2",
        },
        "frozen_source_sha256": {
            "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md": "249f5985ff1e8971e1ac4437e4bbebd5a3db9254ab25a2238e135cb7a7ae5f4b",
            "docs/00_platform/00_PLATFORM_v1.8.0.md": "cb93abfee9a6337a7f2a23c16f35413b8b2ea84608974fcf5a0033822578905e",
            "docs/00_platform/01_DECISIONS_v1.8.0.md": "123d3a622f89c22e364df565b87117c22244378c5c51b10d621597909b569140",
            "docs/00_platform/03_ARCHITECTURE_v1.1.1.md": "342d02a7946f99aca9e6683647fc3a2505901b3d0cc2d13c21d807442025f0b3",
            "docs/00_platform/04_DOMAIN_MAP_v1.2.0.md": "e09e14ee0a773c5855257c48685cf3a75d413c983a98d22a56b42af57dc2c078",
            "docs/00_platform/05_ROADMAP_v1.2.3.md": "044b5c6308d59253cb0e5ae86d53e13611fb84dec04135b1175880d7881593c2",
            "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md": "3560e0cb147e21cdaa149b7e1c2abe43ad03af04619d08175ef0544279fa0d0f",
            "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "cc664c1e5d148c1a8f30f2a8d769645646162ff029494a2187e0a65775c27c83",
            "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "aa6c4a52518225a2d5bbe86734410e5e9e330e29613b1c1e150174e2e3a12046",
            "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md": "d6fb70a9a19286263404d191a60447158c1ccf8097c8be35465def37046169c6",
            "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md": "9b2c1a6c16df3a48f041403fd336df926132bba46168e07b55acce148c4f59c2",
            "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md": "8c02f367c97b3b9f977eb1572e2af0bd29ee87112215989180ed1bd90d0fdd7f",
        },
        "application_source_paths_created": [],
    }
    if not isinstance(rule, dict):
        rule = {}
        issues.append("manifest Phase 8 proof-contract lifecycle rule is missing")
    for key, value in expected_fixed.items():
        if rule.get(key) != value:
            issues.append(f"manifest Phase 8 proof-contract lifecycle field {key!r} is wrong")

    route_hashes = rule.get("current_route_sha256", {})
    if not isinstance(route_hashes, dict) or set(route_hashes) != {*current_routes.values(), candidate_path}:
        issues.append("manifest Phase 8 proof-contract route hash map is incomplete or contains an unexpected path")
    for label, relative in current_routes.items():
        path = root / relative
        if not path.is_file():
            issues.append(f"current Phase 8 route {label!r} is missing: {relative}")
        elif isinstance(route_hashes, dict) and route_hashes.get(relative) != sha256_file(path):
            issues.append(f"manifest Phase 8 route hash differs: {relative}")
    candidate = root / candidate_path
    candidate_hash = sha256_file(candidate) if candidate.is_file() else None
    if candidate_hash is None:
        issues.append(f"routed TB-001 proof contract is missing: {candidate_path}")
    elif isinstance(route_hashes, dict) and route_hashes.get(candidate_path) != candidate_hash:
        issues.append("manifest TB-001 candidate contract SHA-256 differs from its bytes")
    if isinstance(rule, dict) and candidate_hash != rule.get("candidate_sha256"):
        issues.append("manifest does not pin the TB-001 candidate contract bytes")

    # The candidate is a navigation-only working contract, never governing/reference authority.
    graph_rules = integrity_rules.get("graph_rules", {})
    navigation = graph_rules.get("navigation_document_paths", []) if isinstance(graph_rules, dict) else []
    if candidate_path not in navigation:
        issues.append("manifest graph navigation does not route the TB-001 candidate contract")
    authority_entries = [
        entry for entry in _all_entries(manifest)
        if _relative_path(entry) == candidate_path and entry.get("lifecycle", "current") != "historical"
    ]
    if authority_entries:
        issues.append("TB-001 candidate contract is incorrectly promoted into authority-document records")

    predecessor_archives = expected_fixed["predecessor_archives_sha256"]
    for archived_path, digest in predecessor_archives.items():
        path = root / archived_path
        if not path.is_file() or sha256_file(path) != digest:
            issues.append(f"TB-001 direct predecessor archive is missing or changed: {archived_path}")
        retired = archived_path.replace("/archive/", "/")
        if (root / retired).exists():
            issues.append(f"TB-001 predecessor remains at its retired current path: {retired}")
        entry = next((item for item in _all_entries(manifest) if _relative_path(item) == archived_path), None)
        if (not isinstance(entry, dict) or entry.get("lifecycle") != "historical"
                or entry.get("sha256") != digest or entry.get("provenance_sha256") != digest):
            issues.append(f"manifest does not preserve the direct predecessor as historical evidence: {archived_path}")

    for relative, digest in expected_fixed["frozen_source_sha256"].items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != digest:
            if relative.endswith("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"):
                issues.append(
                    "certified Identity & Access dossier changed from its Phase 7B baseline; "
                    f"Identity current lifecycle or semantic body changed from the proof-contract baseline: {relative}"
                )
            else:
                issues.append(f"frozen Phase 8 proof source changed: {relative}")

    manifest_open_work = next((entry for entry in manifest.get("governing_documents", []) if entry.get("document_id") == "OPEN_WORK"), None)
    if (not isinstance(manifest_open_work, dict) or _relative_path(manifest_open_work) != current_routes["open_work"]
            or manifest_open_work.get("semver") != "1.2.77" or manifest_open_work.get("superseded_version") != "1.2.76"):
        issues.append("manifest does not route Open Work v1.2.77 as the planning-state successor")

    current_state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        (root / current_routes["open_work"]).read_text(encoding="utf-8") if (root / current_routes["open_work"]).is_file() else "",
        re.DOTALL,
    )
    try:
        state = json.loads(current_state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if current_state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        state = {}
    expected_state = {
        "phase_7b_reconciliation_execution_tracker_issue": 120,
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "programme_router_issue_111_state": "OPEN",
        "identity_dossier": "CERTIFIED / CURRENT v0.1.4",
        "identity_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
        "tracer_bullet": "REQUIRED / DEFINED AS REVIEW CANDIDATE",
        "tracer_bullet_id": "TB-001",
        "proof_design": "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "architectural_proof_execution": "NOT STARTED",
        "proof_result": "NOT STARTED",
        "proof_certification": "NOT STARTED",
        "proof_contract_path": candidate_rel,
        "proof_contract_lifecycle": "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "next_stage": "TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
    }
    for key, value in expected_state.items():
        if state.get(key) != value:
            issues.append(f"Open Work current lifecycle state disagrees on {key!r}")
    phase7c_contract = state.get("phase_7c_final_feature_pack_contract", {})
    if not isinstance(phase7c_contract, dict) or phase7c_contract.get("lifecycle") != "COMPLETE / CERTIFIED / CURRENT":
        issues.append("Open Work no longer preserves the certified Phase 7C contract status")

    readme_path = root / "docs/00_platform/README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    current_readme = _markdown_h2_section(readme, "Current State") or ""
    active_working_artifacts = _markdown_h2_section(readme, "Active Working Artifacts") or ""
    current_working_paths = {
        relative.removeprefix("docs/00_platform/")
        for key, relative in current_routes.items()
        if key != "open_work"
    }
    current_working_paths.add(candidate_rel)
    current_working_paths.update(
        relative.removeprefix("docs/00_platform/")
        for relative in expected_fixed["frozen_source_sha256"]
        if relative.startswith("docs/00_platform/working/")
    )
    for relative in sorted(current_working_paths):
        if relative not in active_working_artifacts:
            issues.append(f"README active working artifacts do not route current Phase 8 source: {relative}")
    for archive_relative in expected_fixed["predecessor_archives_sha256"]:
        predecessor_name = Path(archive_relative).name
        if predecessor_name in current_readme.replace(f"archive/{predecessor_name}", ""):
            issues.append(f"README current route cites retired predecessor without archive qualification: {predecessor_name}")
    active_start = (root / current_routes["open_work"]).read_text(encoding="utf-8").find("# 9. Immediate Next Action") if (root / current_routes["open_work"]).is_file() else -1
    open_work = (root / current_routes["open_work"]).read_text(encoding="utf-8") if (root / current_routes["open_work"]).is_file() else ""
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    open_work_active = open_work[active_start:active_end] if active_start >= 0 and active_end > active_start else ""
    required_status_tokens = (
        "TB-001",
        "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "TRACER BULLET: REQUIRED / DEFINED AS REVIEW CANDIDATE",
        "TRACER BULLET ID: TB-001",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "PROGRAMME ROUTER #111: OPEN",
        "IDENTITY v0.1.4",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
    )
    required_route_status_tokens = (
        "TB-001",
        "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
    )
    for label, text in (("README current state", current_readme), ("Open Work active route", open_work_active)):
        for token in required_status_tokens:
            if token not in text:
                issues.append(f"{label} omits TB-001 lifecycle state {token!r}")
        if re.search(r"(?i)(?:proof|classification)[^\n]{0,100}(?:PROOF EXECUTION)\s*:\s*(?:COMPLETE|PASS)", text):
            issues.append(f"{label} claims proof execution has passed")
        if re.search(r"(?im)^\s*PHASE 9(?: / VERTICAL SLICES)?\s*:\s*(?:AUTHORI[ZS]ED|STARTED|IN PROGRESS|COMPLETE)", text):
            issues.append(f"{label} advances Phase 9 or Vertical Slices")
        if re.search(
            r"(?i)\bphase\s+7c\b[^.!?\n]{0,100}\bblocked\b[^.!?\n]{0,40}\bnot[\s/_-]*started\b",
            text,
        ):
            issues.append(f"{label} contains a BLOCKED / NOT_STARTED Phase 7C statement")
    identifier_lines = re.findall(r"(?im)^\s*TRACER BULLET ID:\s*(.*?)\s*$", open_work_active)
    if any(identifier != "TB-001" for identifier in identifier_lines):
        issues.append("Open Work active route assigns a different Tracer Bullet identifier")
    if not identifier_lines:
        issues.append("Open Work active route retracts the TB-001 task-definition identifier")
    if candidate_rel not in current_readme or candidate_rel not in open_work_active:
        issues.append("README and Open Work do not route the same TB-001 candidate file")
    if "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION" not in current_readme:
        issues.append("README does not route TB-001 for review")
    if "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION" not in open_work_active:
        issues.append("Open Work does not route TB-001 for review")

    route_sections = {
        "delivery_atlas": ("## 26.25 FP-001 Phase 8 TB-001 successor candidate route (current)", None),
        "fp001_skeleton": ("## v0.1.21 — TB-001 proof-contract successor candidate route (current)", None),
        "harden_02": ("## v0.5.21 — FP-001 TB-001 proof-contract successor candidate route (current)", None),
    }
    for key, (heading, end_heading) in route_sections.items():
        text = (root / current_routes[key]).read_text(encoding="utf-8") if (root / current_routes[key]).is_file() else ""
        if heading not in text:
            issues.append(f"current {key} is missing its TB-001 route section")
            continue
        route = text.split(heading, 1)[1]
        if end_heading and end_heading in route:
            route = route.split(end_heading, 1)[0]
        elif "\n## " in route:
            route = route.split("\n## ", 1)[0]
        for token in required_route_status_tokens:
            if token not in route:
                issues.append(f"current {key} route omits TB-001 lifecycle state {token!r}")
        if "TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION" not in route:
            issues.append(f"current {key} route does not identify contract review as next")

    text = candidate.read_text(encoding="utf-8") if candidate.is_file() else ""
    for token in (
        "TB-001",
        "CANDIDATE / REVIEW PENDING / NOT CERTIFIED",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
    ):
        if token not in text:
            issues.append(f"TB-001 contract omits lifecycle requirement {token!r}")
    issues.extend(_fp001_phase8_proof_contract_content_issues(text))
    if re.search(r"(?im)^\s*PROOF (?:RESULT|CERTIFICATION)\s*:\s*(?:PASS|COMPLETE|CERTIFIED)", text):
        issues.append("TB-001 candidate claims a proof result or certification")
    if re.search(r"(?im)^\s*PHASE 9(?: / VERTICAL SLICES)?\s*:\s*(?:AUTHORI[ZS]ED|STARTED|IN PROGRESS|COMPLETE)", text):
        issues.append("TB-001 candidate authorises Phase 9 / Vertical Slices")
    if _executable_application_source_paths(root):
        issues.append("application implementation source exists before TB-001 contract approval and execution start")

    _record_check(
        report,
        rule_name,
        not issues,
        "TB-001 proof contract is routed as a frozen-design review candidate; execution, result, certification and Phase 9 remain separate and unstarted"
        if not issues else "; ".join(issues),
        path=candidate_path,
    )


PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA = "4234965c8da20dbb4ef0a7128614a5070244619a"
# Exact final PR #133 head, preserved as the second parent of merge
# 9e5bd3189aa5c79bbf128da464654c917def8a90. Later implementation is outside
# this historical status transition.
PHASE8_APPROVED_STATUS_SUCCESSOR_HEAD_SHA = "c30388f8ae548040126483ec53957d0fc80b8246"
PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA = "5c7acdd690008af24dc0242ca734cb900c56ea88"
_PHASE8_PREDECESSOR_AUDIT_CACHE: dict[tuple[Path, str], tuple[bool, str]] = {}
_PHASE8_PINNED_ARCHIVE_SHA256_CACHE: dict[tuple[Path, str, str, str], tuple[str | None, str]] = {}
_PHASE8_PINNED_BASE_MANIFEST_CACHE: dict[tuple[Path, str], tuple[dict[str, Any] | None, str]] = {}


def _phase8_status_transition_source_issues(repository_root: Path) -> list[str]:
    """Prove the pinned status transition itself changed no application source."""

    trees: list[str] = []
    for revision in (PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA, PHASE8_APPROVED_STATUS_SUCCESSOR_HEAD_SHA):
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            return ["status transition historical revision is not an exact Git object ID"]
        result = subprocess.run(
            ["git", "rev-parse", "--verify", f"{revision}^{{tree}}"],
            cwd=repository_root, capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            return [f"pinned status transition revision is unavailable: {revision}"]
        trees.append(result.stdout.strip())
    result = subprocess.run(
        ["git", "diff", "--no-renames", "--name-only", "-z", *trees, "--"],
        cwd=repository_root, capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        return ["cannot compare the pinned historical status transition trees"]
    source_paths = [
        path for path in result.stdout.split("\0") if path and (
            Path(path).name == "mix.exs"
            or path.endswith((".ex", ".exs"))
            or set(Path(path).parts) & APPLICATION_SOURCE_DIRECTORY_NAMES
        )
    ]
    if source_paths:
        return ["implementation-era status transition added executable application source: " + ", ".join(source_paths)]
    return []


def _phase8_successor_manifest_history_issues(
    root: Path,
    repository_root: Path,
    manifest: dict[str, Any],
    expected_routes: dict[str, str],
    predecessor_routes: dict[str, tuple[str, str, str, str]],
    candidate_path: str,
) -> list[str]:
    """Allow only the recorded v1.2.78 route/status delta from its pinned base."""

    issues: list[str] = []
    repository = subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if repository.returncode != 0:
        return ["cannot locate Git repository for the successor manifest comparison"]
    base_result = subprocess.run(
        [
            "git",
            "-C",
            repository.stdout.strip(),
            "show",
            f"{PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA}:{DEFAULT_MANIFEST}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if base_result.returncode != 0:
        return ["pinned predecessor manifest is unavailable for successor comparison"]
    try:
        base_manifest = json.loads(
            base_result.stdout,
            object_pairs_hook=_reject_duplicate_json_keys,
        )
    except (json.JSONDecodeError, TypeError, ValueError):
        return ["pinned predecessor manifest cannot be parsed for successor comparison"]
    if not isinstance(base_manifest, dict):
        return ["pinned predecessor manifest has an invalid root"]

    expected = copy.deepcopy(base_manifest)
    base_rules = base_manifest.get("integrity_rules", {})
    expected_rules = expected.get("integrity_rules", {})
    if not isinstance(base_rules, dict) or not isinstance(expected_rules, dict):
        return ["pinned predecessor manifest has no integrity rules"]

    base_phase8 = base_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    phase8 = expected_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    if not isinstance(base_phase8, dict) or not isinstance(phase8, dict):
        return ["pinned predecessor manifest has no Phase 8 lifecycle rule"]

    route_hashes = {
        relative: sha256_file(root / relative) if (root / relative).is_file() else ""
        for relative in expected_routes.values()
    }
    route_hashes[candidate_path] = sha256_file(root / candidate_path) if (root / candidate_path).is_file() else ""
    phase8_predecessor_hashes = copy.deepcopy(base_phase8.get("predecessor_archives_sha256", {}))
    base_current_hashes = base_phase8.get("current_route_sha256", {})
    base_current_routes = base_phase8.get("current_routes", {})
    if not isinstance(phase8_predecessor_hashes, dict) or not isinstance(base_current_hashes, dict) or not isinstance(base_current_routes, dict):
        return ["pinned predecessor Phase 8 route or archive hashes are invalid"]

    authority_classes = {
        "OPEN_WORK_V1_2_77": "PLANNING_TRACKER_HISTORICAL",
        "DELIVERY_ATLAS_V0_4_19": "DELIVERY_ATLAS_HISTORICAL",
        "FP001_SKELETON_V0_1_21": "FP001_SKELETON_HISTORICAL",
        "HARDEN_02_V0_5_21": "HARDEN_02_HISTORICAL",
    }
    new_history: list[dict[str, Any]] = []
    for current_path, (archive_path, document_id, version, successor) in predecessor_routes.items():
        key = next(
            (name for name, path in expected_routes.items() if path == current_path),
            None,
        )
        base_current_path = base_current_routes.get(key) if key is not None else None
        digest = base_current_hashes.get(base_current_path) if isinstance(base_current_path, str) else None
        if key is None or not isinstance(digest, str) or document_id not in authority_classes:
            issues.append(f"pinned predecessor manifest does not bind route archive {archive_path}")
            continue
        phase8_predecessor_hashes[archive_path] = digest
        new_history.append(
            {
                "document_id": document_id,
                "canonical_filename": Path(archive_path).name,
                "semver": version,
                "repository_path": archive_path,
                "authority_class": authority_classes[document_id],
                "sha256": digest,
                "superseded_version": successor,
                "lifecycle": "historical",
                "graph_policy": "frozen_provenance",
                "provenance_sha256": digest,
            }
        )

    candidate_digest = base_phase8.get("candidate_sha256")
    candidate_archive_path = "docs/00_platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
    new_history.append(
        {
            "document_id": "FP001_PHASE8_PROOF_CONTRACT_V0_1_2_REVIEWED_CANDIDATE",
            "canonical_filename": Path(candidate_path).name,
            "semver": "0.1.2",
            "repository_path": candidate_archive_path,
            "authority_class": "FP001_PHASE8_PROOF_CONTRACT_HISTORICAL",
            "sha256": candidate_digest,
            "superseded_version": None,
            "lifecycle": "historical",
            "graph_policy": "frozen_provenance",
            "provenance_sha256": candidate_digest,
        }
    )

    phase8.update(
        {
            "candidate_exact_head_ci_run": 39484403424,
            "candidate_lifecycle": "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
            "candidate_merge_sha": PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA,
            "contract_design_review": "COMPLETE / PASS",
            "current_contract_sha256": route_hashes.get(candidate_path),
            "current_route_sha256": route_hashes,
            "current_routes": expected_routes,
            "phase8_execution_gate": "WAITING FOR A SEPARATE EXECUTION START",
            "predecessor_archives_sha256": phase8_predecessor_hashes,
            "resulting_main_ci_run": 39487861172,
            "reviewed_candidate_archive_path": candidate_archive_path,
            "reviewed_candidate_archive_sha256": candidate_digest,
            "reviewed_candidate_head_sha": "5486c94c1b659dfeb026dcbe6abf91978655c535",
            "reviewed_candidate_review": "INDEPENDENT REVIEW PASS",
        }
    )

    roadmap_name = "roadmap_proof_classification_lifecycle"
    base_roadmap = base_rules.get(roadmap_name, {})
    roadmap = expected_rules.get(roadmap_name, {})
    if not isinstance(base_roadmap, dict) or not isinstance(roadmap, dict):
        issues.append("pinned predecessor has no Roadmap proof-classification lifecycle rule")
    else:
        roadmap_routes = copy.deepcopy(base_roadmap.get("current_routes", {}))
        roadmap_hashes = copy.deepcopy(base_roadmap.get("current_route_sha256", {}))
        if not isinstance(roadmap_routes, dict) or not isinstance(roadmap_hashes, dict):
            issues.append("pinned predecessor Roadmap proof-classification routes are invalid")
        else:
            for key in tuple(roadmap_routes):
                if key not in expected_routes:
                    issues.append(f"pinned Roadmap proof-classification route has no successor: {key}")
                    continue
                old_path = roadmap_routes[key]
                roadmap_routes[key] = expected_routes[key]
                roadmap_hashes.pop(old_path, None)
                roadmap_hashes[expected_routes[key]] = route_hashes.get(expected_routes[key], "")
            roadmap["current_routes"] = roadmap_routes
            roadmap["current_route_sha256"] = roadmap_hashes

    promotion_name = "fp001_phase7c_final_contract_current_promotion"
    promotion = expected_rules.get(promotion_name, {})
    if not isinstance(promotion, dict):
        issues.append("pinned predecessor has no Phase 7C promotion rule")
    else:
        promotion["current_paths"] = expected_routes
        promotion["current_route_status_successor_version"] = "1.2.78 / 0.4.20 / 0.1.22 / 0.5.22"

    graph = expected_rules.get("graph_rules", {})
    base_graph = base_rules.get("graph_rules", {})
    if not isinstance(graph, dict) or not isinstance(base_graph, dict):
        issues.append("pinned predecessor has no graph routing rules")
    else:
        navigation = list(base_graph.get("navigation_document_paths", []))
        for key in ("delivery_atlas", "fp001_skeleton", "harden_02"):
            old_path = base_phase8.get("current_routes", {}).get(key)
            if old_path not in navigation:
                issues.append(f"pinned graph navigation omits predecessor route {old_path}")
            else:
                navigation[navigation.index(old_path)] = expected_routes[key]
        graph["navigation_document_paths"] = navigation
        graph["retired_current_predecessor_paths"] = list(
            base_graph.get("retired_current_predecessor_paths", [])
        ) + [
            current_path.replace(Path(current_path).name, Path(details[0]).name)
            for current_path, details in predecessor_routes.items()
        ]
        guard_note = str(base_graph.get("stale_predecessor_current_path_guard_note", ""))
        marker = "Current WELL-2 routing uses "
        if marker not in guard_note:
            issues.append("pinned graph predecessor note has no current WELL-2 route statement")
        else:
            graph["stale_predecessor_current_path_guard_note"] = guard_note.split(marker, 1)[0] + (
                "Current WELL-2 routing uses Open Work v1.2.78, Atlas v0.4.20, "
                "FP-001 Skeleton v0.1.22, HARDEN-02 v0.5.22 and approved proof contract v0.1.2; "
                "its exact reviewed candidate is preserved at the archive path."
            )

    open_work = next(
        (
            item
            for item in expected.get("governing_documents", [])
            if item.get("document_id") == "OPEN_WORK"
        ),
        None,
    )
    if not isinstance(open_work, dict):
        issues.append("pinned manifest has no current Open Work entry")
    else:
        open_work.update(
            {
                "canonical_filename": Path(expected_routes["open_work"]).name,
                "semver": "1.2.78",
                "repository_path": expected_routes["open_work"],
                "sha256": route_hashes.get(expected_routes["open_work"], ""),
                "superseded_version": "1.2.77",
                "lifecycle": "current",
            }
        )

    expected.setdefault("historical_documents", []).extend(new_history)
    expected["integrity_rules"] = expected_rules
    if expected != manifest:
        changed = [
            key
            for key in set(expected) | set(manifest)
            if expected.get(key) != manifest.get(key)
        ]
        if "integrity_rules" in changed:
            expected_rule_map = expected.get("integrity_rules", {})
            manifest_rule_map = manifest.get("integrity_rules", {})
            changed.extend(
                f"integrity_rules.{key}"
                for key in set(expected_rule_map) | set(manifest_rule_map)
                if expected_rule_map.get(key) != manifest_rule_map.get(key)
            )
            for name in ("fp001_phase8_proof_contract_lifecycle", "graph_rules"):
                expected_section = expected_rule_map.get(name, {})
                actual_section = manifest_rule_map.get(name, {})
                if isinstance(expected_section, dict) and isinstance(actual_section, dict):
                    changed.extend(
                        f"integrity_rules.{name}.{key}"
                        for key in set(expected_section) | set(actual_section)
                        if expected_section.get(key) != actual_section.get(key)
                    )
        changed.sort()
        issues.append(
            "successor manifest changes more than the pinned status, route and archive transition: "
            + ", ".join(changed)
        )
    return issues


def _phase8_approved_status_successor_issues(
    root: Path,
    repository_root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> list[str]:
    """Check the v1.2.78 route, archived predecessors and bounded proof stop."""

    if _fp001_phase8_execution_status_successor_is_current(manifest):
        return _phase8_started_status_successor_issues(
            root, repository_root, manifest, integrity_rules
        )

    issues: list[str] = []
    if not _fp001_phase8_approved_status_successor_is_current(manifest):
        return ["Open Work v1.2.78 is not the sole current status successor"]

    expected_routes = {
        "open_work": "docs/00_platform/02_OPEN_WORK_v1.2.78.md",
        "delivery_atlas": "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.20.md",
        "fp001_skeleton": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md",
        "harden_02": "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.22.md",
        "final_feature_pack_contract": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
    }
    predecessor_routes = {
        "docs/00_platform/02_OPEN_WORK_v1.2.78.md": (
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.77.md",
            "OPEN_WORK_V1_2_77",
            "1.2.77",
            "1.2.78",
        ),
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.20.md": (
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.19.md",
            "DELIVERY_ATLAS_V0_4_19",
            "0.4.19",
            "0.4.20",
        ),
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md": (
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md",
            "FP001_SKELETON_V0_1_21",
            "0.1.21",
            "0.1.22",
        ),
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.22.md": (
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.21.md",
            "HARDEN_02_V0_5_21",
            "0.5.21",
            "0.5.22",
        ),
    }
    phase8_rule = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    if not isinstance(phase8_rule, dict):
        return ["Phase 8 proof-contract lifecycle rule is missing"]
    if phase8_rule.get("current_routes") != expected_routes:
        issues.append("Phase 8 lifecycle current routes do not match the v1.2.78 successor set")
    candidate_path = "docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
    expected_route_hashes = {*expected_routes.values(), candidate_path}
    route_hashes = phase8_rule.get("current_route_sha256", {})
    if not isinstance(route_hashes, dict) or set(route_hashes) != expected_route_hashes:
        issues.append("Phase 8 lifecycle route hash map is incomplete or includes a stale route")
    issues.extend(
        _phase8_successor_manifest_history_issues(
            root,
            repository_root,
            manifest,
            expected_routes,
            predecessor_routes,
            candidate_path,
        )
    )

    entries = _all_entries(manifest)
    current_open_work = _active_open_work_entry(manifest)
    if (
        not isinstance(current_open_work, dict)
        or _relative_path(current_open_work) != expected_routes["open_work"]
        or current_open_work.get("semver") != "1.2.78"
        or current_open_work.get("superseded_version") != "1.2.77"
    ):
        issues.append("manifest Open Work lineage is not v1.2.77 → v1.2.78")

    active_files: dict[str, str] = {}
    for label, relative in expected_routes.items():
        path = root / relative
        if not path.is_file() or path.is_symlink():
            issues.append(f"current {label} route is missing or is a symlink: {relative}")
            active_files[label] = ""
            continue
        digest = sha256_file(path)
        active_files[label] = path.read_text(encoding="utf-8")
        if route_hashes.get(relative) != digest:
            issues.append(f"Phase 8 current-route SHA-256 differs: {relative}")
        archived_route, document_id, version, successor = predecessor_routes.get(relative, ("", "", "", ""))
        if archived_route:
            archived = root / archived_route
            historical_entry = next(
                (entry for entry in entries if entry.get("document_id") == document_id),
                None,
            )
            retired_current = root / relative
            retired_current = retired_current.with_name(Path(archived_route).name)
            expected_hash = historical_entry.get("sha256") if isinstance(historical_entry, dict) else None
            if (
                not archived.is_file()
                or not isinstance(expected_hash, str)
                or sha256_file(archived) != expected_hash
                or historical_entry.get("repository_path") != archived_route
                or historical_entry.get("semver") != version
                or historical_entry.get("superseded_version") != successor
                or historical_entry.get("lifecycle") != "historical"
                or historical_entry.get("graph_policy") != "frozen_provenance"
                or historical_entry.get("provenance_sha256") != expected_hash
            ):
                issues.append(f"immediate predecessor archive is missing or not manifest-pinned: {archived_route}")
            if retired_current.exists():
                issues.append(f"predecessor remains at its former current path: {retired_current.relative_to(root).as_posix()}")

    navigation = integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])
    for key, relative in expected_routes.items():
        if key != "open_work" and relative not in navigation:
            issues.append(f"manifest graph navigation omits current route: {relative}")
    if candidate_path not in navigation:
        issues.append("manifest graph navigation omits the current TB-001 contract")

    open_work = active_files.get("open_work", "")
    state = _open_work_lifecycle_state(open_work)
    expected_state = {
        "status_successor_version": "1.2.78",
        "status_successor_base_sha": PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA,
        "next_stage": "WELL-38 — Transition Foundation Integrity to implementation-era CI",
        "proof_classification": "NEW_TRACER_BULLET",
        "tracer_bullet": "REQUIRED / DEFINED",
        "tracer_bullet_id": "TB-001",
        "proof_design": "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "architectural_proof_execution": "NOT STARTED",
        "proof_result": "NOT STARTED",
        "proof_certification": "NOT STARTED",
        "proof_contract_path": "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md",
        "proof_contract_lifecycle": "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        "next_governance_action": "WELL-38 — Transition Foundation Integrity to implementation-era CI",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.20.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.22.md",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
    }
    if state is None or any(state.get(key) != value for key, value in expected_state.items()):
        issues.append("Open Work lifecycle state changes a certified route or weakens the bounded proof stop")
    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    open_work_active = open_work[active_start:active_end] if active_start >= 0 and active_end > active_start else ""
    current_status_tokens = (
        "TB-001 CONTRACT LIFECYCLE: CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
        "TRACER BULLET ID: TB-001",
        "CONTRACT/DESIGN REVIEW: COMPLETE / PASS",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "NEXT GOVERNANCE ACTION: WELL-38 — Transition Foundation Integrity to implementation-era CI",
    )
    if any(token not in open_work_active for token in current_status_tokens):
        issues.append("current Open Work route omits the approved contract or downstream stop state")
    if "PHASE 7B TRACKER #120: CLOSED / COMPLETED" not in open_work_active:
        issues.append("current Open Work route does not keep completed tracker #120 historical")
    if re.search(r"(?im)^\s*PHASE 9(?: / VERTICAL SLICES)?\s*:\s*(?:AUTHORI[ZS]ED|STARTED|IN PROGRESS|COMPLETE)", open_work_active):
        issues.append("current Open Work authorises or starts Phase 9")
    if re.search(r"(?im)^\s*PROOF (?:EXECUTION|RESULT|CERTIFICATION)\s*:\s*(?:PASS|COMPLETE|CERTIFIED)", open_work_active):
        issues.append("current Open Work claims proof execution, result or certification")

    candidate = root / candidate_path
    candidate_hash = sha256_file(candidate) if candidate.is_file() else None
    candidate_archive_path = "docs/00_platform/archive/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md"
    candidate_archive = root / candidate_archive_path
    candidate_history = next(
        (entry for entry in entries if entry.get("document_id") == "FP001_PHASE8_PROOF_CONTRACT_V0_1_2_REVIEWED_CANDIDATE"),
        None,
    )
    reviewed_hash = phase8_rule.get("reviewed_candidate_archive_sha256")
    if (
        phase8_rule.get("candidate_path") != candidate_path
        or phase8_rule.get("candidate_lifecycle") != "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION"
        or phase8_rule.get("contract_design_review") != "COMPLETE / PASS"
        or phase8_rule.get("proof_design") != "FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS"
        or phase8_rule.get("proof_execution") != "NOT STARTED"
        or phase8_rule.get("proof_result") != "NOT STARTED"
        or phase8_rule.get("proof_certification") != "NOT STARTED"
        or phase8_rule.get("phase9_vertical_slices") != "NOT STARTED / NOT AUTHORISED"
        or phase8_rule.get("phase8_execution_gate") != "WAITING FOR A SEPARATE EXECUTION START"
        or phase8_rule.get("reviewed_candidate_archive_path") != candidate_archive_path
        or not isinstance(reviewed_hash, str)
        or candidate_hash is None
        or not candidate_archive.is_file()
        or sha256_file(candidate_archive) != reviewed_hash
        or reviewed_hash != phase8_rule.get("candidate_sha256")
        or not isinstance(candidate_history, dict)
        or candidate_history.get("repository_path") != candidate_archive_path
        or candidate_history.get("lifecycle") != "historical"
        or candidate_history.get("graph_policy") != "frozen_provenance"
        or candidate_history.get("sha256") != reviewed_hash
        or candidate_history.get("provenance_sha256") != reviewed_hash
    ):
        issues.append("reviewed TB-001 candidate bytes or approved lifecycle provenance are not preserved")
    if isinstance(route_hashes, dict) and route_hashes.get(candidate_path) != candidate_hash:
        issues.append("current TB-001 contract hash differs from the manifest route pin")
    candidate_text = candidate.read_text(encoding="utf-8") if candidate.is_file() else ""
    for token in (
        "TB-001",
        "CURRENT / APPROVED FOR BOUNDED PHASE 8 PROOF EXECUTION",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
    ):
        if token.casefold() not in candidate_text.casefold():
            issues.append(f"current TB-001 contract omits required boundary {token!r}")
    if not re.search(
        r"(?i)contract/design review:\*{0,2}\s*complete / pass",
        candidate_text,
    ):
        issues.append("current TB-001 contract omits the completed design-review status")

    readme_path = root / "docs/00_platform/README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() and not readme_path.is_symlink() else ""
    readme_current = _markdown_h2_section(readme, "Current State") or ""
    if any(token not in readme_current for token in current_status_tokens):
        issues.append("README current state does not mirror the approved contract and execution stop")
    if "PHASE 7B EXECUTION/CONTROL TRACKER #120: CLOSED / COMPLETED" not in readme_current:
        issues.append("README current state omits tracker #120 completion")
    graph_rules = integrity_rules.get("graph_rules", {})
    retired_predecessors = graph_rules.get("retired_current_predecessor_paths", []) if isinstance(graph_rules, dict) else []
    for retired_path in retired_predecessors:
        if not isinstance(retired_path, str):
            continue
        filename = Path(retired_path).name
        current_without_archived_references = readme_current.replace(f"archive/{filename}", "")
        if re.search(
            rf"(?<![A-Za-z0-9_.-]){re.escape(filename)}(?![A-Za-z0-9_.-])",
            current_without_archived_references,
        ):
            issues.append(
                "README current state routes retired predecessor without archive qualification: "
                f"{filename}"
            )
    blocked_phase7c = re.compile(
        r"\bphase\s+7c\b[^.!?\n]{0,100}\bblocked\b[^.!?\n]{0,40}\bnot[\s/_-]*started\b",
        re.IGNORECASE,
    )
    if any(
        blocked_phase7c.search(sentence)
        for paragraph in re.split(r"\n\s*\n", readme_current)
        for sentence in re.split(r"(?<=[.!?])\s+", paragraph)
    ):
        issues.append("README current state contains a BLOCKED / NOT_STARTED Phase 7C statement")
    active_artifacts = _markdown_h2_section(readme, "Active Working Artifacts") or ""
    phase7b_routes = [
        relative
        for relative in navigation
        if Path(relative).name.startswith("FP-001_PHASE_7B_RECONCILIATION_WORKING_")
    ]
    if len(phase7b_routes) != 1:
        issues.append("manifest navigation does not resolve one current Phase 7B reconciliation route")
    else:
        phase7b_route = phase7b_routes[0]
        phase7b_path = root / phase7b_route
        if phase7b_path.is_symlink() or not phase7b_path.is_file():
            issues.append(f"current Phase 7B reconciliation route is missing or is a symlink: {phase7b_route}")
        else:
            phase7b_header = phase7b_path.read_text(encoding="utf-8").split(
                "## 1. Baseline and authority set", 1
            )[0]
            phase7b_status_tokens = (
                "COMPLETE\nCERTIFIED\nCURRENT",
                "CLOSED / COMPLETED",
                "NON-IMPLEMENTATION",
                "NOT PHASE 7C",
                "NOT DEVELOPMENT-ENTRY AUTHORITY",
            )
            if any(token not in phase7b_header for token in phase7b_status_tokens):
                issues.append("current Phase 7B reconciliation route does not preserve its certified closed status")
        if phase7b_route.removeprefix("docs/00_platform/") not in active_artifacts:
            issues.append("README active working routing omits the current Phase 7B reconciliation route")
    for relative in (*[path for key, path in expected_routes.items() if key != "open_work"], candidate_path):
        route = relative.removeprefix("docs/00_platform/")
        if route not in active_artifacts:
            issues.append(f"README active working routing omits {route}")
    atlas_routing = _markdown_h2_section(readme, "Delivery Atlas routing") or ""
    if "working/DELIVERY_ATLAS_WORKING_v0.4.20.md" not in atlas_routing:
        issues.append("README Delivery Atlas routing does not name the current v0.4.20 route")
    default_context = _markdown_h2_section(readme, "Default Agent Context") or ""
    if "02_OPEN_WORK_v1.2.78.md" not in default_context or "02_OPEN_WORK_v1.2.77.md" in default_context:
        issues.append("README default context does not route current Open Work v1.2.78")

    route_status_tokens = (
        "current / approved for bounded phase 8 proof execution",
        "contract/design review: complete / pass",
        "proof execution: not started",
        "proof result: not started",
        "proof certification: not started",
        "phase 9 / vertical slices: not started / not authorised",
    )
    for key in ("delivery_atlas", "fp001_skeleton", "harden_02"):
        route_text = active_files.get(key, "")
        if any(token not in route_text.casefold() for token in route_status_tokens):
            issues.append(f"current {key} route omits the approved TB-001 status or downstream stop")
        if "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md" not in route_text:
            issues.append(f"current {key} route does not link the approved TB-001 contract")

    skeleton_text = active_files.get("fp001_skeleton", "")
    skeleton_predecessor = root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md"
    marker_start = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:START -->"
    marker_end = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:END -->"

    def pmr_block(text: str) -> str:
        if text.count(marker_start) != 1 or text.count(marker_end) != 1:
            return ""
        start = text.index(marker_start)
        end = text.index(marker_end)
        return text[start : end + len(marker_end)] if start < end else ""

    predecessor_skeleton_text = skeleton_predecessor.read_text(encoding="utf-8") if skeleton_predecessor.is_file() else ""
    if not pmr_block(skeleton_text) or pmr_block(skeleton_text) != pmr_block(predecessor_skeleton_text):
        issues.append("current Skeleton PMR contract block differs from archived v0.1.21")
    if "The six affected Domains and seven material capability relationships remain unchanged." not in skeleton_text:
        issues.append("current Skeleton does not preserve the certified six-Domain/seven-capability scope")

    application_sources = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {}).get("application_source_paths_created")
    if application_sources != []:
        issues.append("implementation-era status transition added executable application source")
    issues.extend(_phase8_status_transition_source_issues(repository_root))
    standards = [
        entry for entry in manifest.get("reference_documents", [])
        if entry.get("document_id") == "ENGINEERING_STANDARDS"
        and entry.get("lifecycle") == "current"
    ]
    if len(standards) != 1 or standards[0].get("repository_path") != "docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md":
        issues.append("Engineering Standards supporting authority is not uniquely current")

    return issues


def _phase8_pinned_archive_sha256(
    repository_root: Path,
    archive_relative: str,
) -> tuple[str | None, str]:
    """Resolve an archived status artifact to its exact bytes at the pinned base."""

    repository = subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if repository.returncode != 0:
        return None, "cannot locate Git repository for pinned archive provenance"
    repository_path = Path(repository.stdout.strip()).resolve()
    head = subprocess.run(
        ["git", "-C", str(repository_path), "rev-parse", "--verify", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    current_head = head.stdout.strip()
    if head.returncode != 0 or not current_head:
        return None, "cannot resolve current Git HEAD for pinned archive provenance"
    cache_key = (
        repository_path,
        PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA,
        current_head,
        archive_relative,
    )
    cached = _PHASE8_PINNED_ARCHIVE_SHA256_CACHE.get(cache_key)
    if cached is not None:
        return cached

    def read_revision_path(relative: str, revision: str = PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA) -> bytes | None:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(repository_path),
                "show",
                f"{revision}:{relative}",
            ],
            capture_output=True,
            check=False,
        )
        return result.stdout if result.returncode == 0 else None

    base_bytes = read_revision_path(archive_relative)
    if base_bytes is None:
        manifest_bytes = read_revision_path(DEFAULT_MANIFEST.as_posix())
        if manifest_bytes is None:
            result = (None, "pinned predecessor manifest is unavailable for archive provenance")
            _PHASE8_PINNED_ARCHIVE_SHA256_CACHE[cache_key] = result
            return result
        try:
            base_manifest = json.loads(
                manifest_bytes,
                object_pairs_hook=_reject_duplicate_json_keys,
            )
        except (json.JSONDecodeError, TypeError, ValueError):
            result = (None, "pinned predecessor manifest is invalid for archive provenance")
            _PHASE8_PINNED_ARCHIVE_SHA256_CACHE[cache_key] = result
            return result
        phase8 = base_manifest.get("integrity_rules", {}).get(
            "fp001_phase8_proof_contract_lifecycle", {}
        )
        routes = phase8.get("current_routes", {}) if isinstance(phase8, dict) else {}
        source_paths = [
            path
            for path in routes.values()
            if isinstance(path, str) and Path(path).name == Path(archive_relative).name
        ] if isinstance(routes, dict) else []
        for source_path in source_paths:
            base_bytes = read_revision_path(source_path)
            if base_bytes is not None:
                break

    if base_bytes is None:
        # A later routing successor can archive a predecessor that was still at its
        # current path in the PR base, after the original status-certification base.
        # A merge-ref checkout has that base at HEAD^; a direct branch checkout can
        # have several commits since the base. Walk first-parent history to the
        # nearest source snapshot, then let the manifest hash comparison verify the
        # archived bytes exactly.
        filename = Path(archive_relative).name
        source_paths = list(dict.fromkeys((
            f"docs/00_platform/{filename}",
            f"docs/00_platform/working/{filename}",
        )))

        history = subprocess.run(
            ["git", "-C", str(repository_path), "rev-list", "--first-parent", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
        revisions = history.stdout.splitlines() if history.returncode == 0 else []
        for revision in revisions:
            for source_path in source_paths:
                base_bytes = read_revision_path(source_path, revision)
                if base_bytes is not None:
                    break
            if base_bytes is not None:
                break

    if base_bytes is None:
        result = (None, f"pinned predecessor has no source bytes for archive {archive_relative}")
    else:
        result = (hashlib.sha256(base_bytes).hexdigest(), "")
    _PHASE8_PINNED_ARCHIVE_SHA256_CACHE[cache_key] = result
    return result


def _phase8_started_status_successor_issues(
    root: Path,
    repository_root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> list[str]:
    """Validate current status routing while keeping the approved contract historical."""

    issues: list[str] = []
    phase8 = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    if not isinstance(phase8, dict):
        return ["Phase 8 proof-contract lifecycle rule is missing"]
    routes = phase8.get("current_routes", {})
    expected_route_keys = {
        "open_work",
        "delivery_atlas",
        "fp001_skeleton",
        "harden_02",
        "final_feature_pack_contract",
    }
    if not isinstance(routes, dict) or set(routes) != expected_route_keys:
        return ["Phase 8 lifecycle current-route map is incomplete or contains an unexpected route"]

    current_open_work = _active_open_work_entry(manifest)
    if current_open_work is None or _relative_path(current_open_work) != routes["open_work"]:
        issues.append("manifest does not route its sole current Open Work record to the Phase 8 route")
    if current_open_work is not None:
        open_work_version = re.search(r"_v(\d+\.\d+\.\d+)\.md$", routes["open_work"])
        if open_work_version is None or current_open_work.get("semver") != open_work_version.group(1):
            issues.append("manifest Open Work version and current route filename disagree")

    promotion = integrity_rules.get("fp001_phase7c_final_contract_current_promotion", {})
    if not isinstance(promotion, dict):
        issues.append("Phase 7C current-promotion routing rule is missing")
    else:
        if promotion.get("current_paths") != routes:
            issues.append("Phase 7C promotion and Phase 8 current routes disagree")
        version_order = ("open_work", "delivery_atlas", "fp001_skeleton", "harden_02")
        route_versions = []
        for key in version_order:
            version = re.search(r"_v(\d+\.\d+\.\d+)\.md$", routes[key])
            if version is None:
                issues.append(f"current {key} route has no versioned filename")
            else:
                route_versions.append(version.group(1))
        if len(route_versions) == len(version_order):
            expected_successor = " / ".join(route_versions)
            if promotion.get("current_route_status_successor_version") != expected_successor:
                issues.append("current-route successor version tuple disagrees with its routed files")

    candidate_path = phase8.get("candidate_path")
    if not isinstance(candidate_path, str) or not candidate_path:
        return issues + ["approved TB-001 contract path is missing from the Phase 8 lifecycle rule"]
    route_hashes = phase8.get("current_route_sha256", {})
    expected_hash_paths = {*routes.values(), candidate_path}
    if not isinstance(route_hashes, dict) or set(route_hashes) != expected_hash_paths:
        issues.append("Phase 8 lifecycle route hash map is incomplete or contains a stale route")
        route_hashes = route_hashes if isinstance(route_hashes, dict) else {}

    entries = _all_entries(manifest)
    active_files: dict[str, str] = {}
    for label, relative in routes.items():
        path = root / relative
        if not path.is_file() or path.is_symlink():
            issues.append(f"current {label} route is missing or is a symlink: {relative}")
            active_files[label] = ""
            continue
        digest = sha256_file(path)
        active_files[label] = path.read_text(encoding="utf-8")
        if route_hashes.get(relative) != digest:
            issues.append(f"Phase 8 current-route SHA-256 differs: {relative}")
        if label == "open_work":
            if not isinstance(current_open_work, dict) or current_open_work.get("sha256") != digest:
                issues.append("manifest Open Work SHA-256 differs from the current route bytes")

    predecessor_hashes = phase8.get("predecessor_archives_sha256", {})
    if not isinstance(predecessor_hashes, dict):
        issues.append("Phase 8 predecessor archive hash map is invalid")
        predecessor_hashes = {}
    for label in ("open_work", "delivery_atlas", "fp001_skeleton", "harden_02"):
        relative = routes[label]
        current_text = active_files.get(label, "")
        header = "\n".join(current_text.splitlines()[:45])
        predecessor = re.search(r"(?im)^.*predecessor.*`(archive/[^`]+\.md)`", header)
        if predecessor is None:
            issues.append(f"current {label} route omits direct predecessor archive metadata")
            continue
        archive_relative = f"docs/00_platform/{predecessor.group(1)}"
        archive = root / archive_relative
        expected_digest = predecessor_hashes.get(archive_relative)
        if (
            not archive.is_file()
            or not isinstance(expected_digest, str)
            or sha256_file(archive) != expected_digest
        ):
            issues.append(f"immediate predecessor archive is missing or not hash-pinned: {archive_relative}")
        retired_current = Path(relative).with_name(Path(archive_relative).name)
        if (root / retired_current).exists():
            issues.append(f"predecessor remains at its former current path: {retired_current.as_posix()}")
        archive_entry = next(
            (entry for entry in entries if _relative_path(entry) == archive_relative),
            None,
        )
        if archive_entry is not None and (
            archive_entry.get("lifecycle") != "historical"
            or archive_entry.get("sha256") != expected_digest
            or archive_entry.get("provenance_sha256") != expected_digest
        ):
            issues.append(f"manifest historical provenance differs for predecessor archive: {archive_relative}")

    approval_time_archives = (
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.78.md",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.20.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.22.md",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.22.md",
    )
    for archive_relative in approval_time_archives:
        archive = root / archive_relative
        expected_digest = predecessor_hashes.get(archive_relative)
        if (
            not archive.is_file()
            or not isinstance(expected_digest, str)
            or sha256_file(archive) != expected_digest
        ):
            issues.append(f"TB-001 approval-time route archive is missing or changed: {archive_relative}")

    for archive_relative, expected_digest in predecessor_hashes.items():
        pinned_digest, provenance_issue = _phase8_pinned_archive_sha256(
            repository_root, archive_relative
        )
        if pinned_digest is None:
            issues.append(provenance_issue)
            continue
        if expected_digest != pinned_digest:
            issues.append(f"manifest predecessor archive pin differs from exact base bytes: {archive_relative}")
        archive = root / archive_relative
        if not archive.is_file() or sha256_file(archive) != pinned_digest:
            issues.append(f"predecessor archive differs from exact base bytes: {archive_relative}")

    candidate = root / candidate_path
    candidate_hash = sha256_file(candidate) if candidate.is_file() and not candidate.is_symlink() else None
    if candidate_hash is None:
        issues.append(f"approved TB-001 contract is missing or is a symlink: {candidate_path}")
    else:
        if route_hashes.get(candidate_path) != candidate_hash:
            issues.append("approved TB-001 contract SHA-256 differs from its route pin")
        candidate_text = candidate.read_text(encoding="utf-8")
        candidate_archive_path = phase8.get("reviewed_candidate_archive_path")
        candidate_archive_digest = phase8.get("reviewed_candidate_archive_sha256")
        candidate_archive = root / candidate_archive_path if isinstance(candidate_archive_path, str) else None
        if (
            candidate_archive is None
            or not candidate_archive.is_file()
            or sha256_file(candidate_archive) != candidate_archive_digest
            or candidate_archive_digest != phase8.get("candidate_sha256")
        ):
            issues.append("reviewed TB-001 contract archive bytes are not preserved")
        if _fp001_phase8_proof_contract_content_issues(candidate_text):
            issues.extend(_fp001_phase8_proof_contract_content_issues(candidate_text))
        approval_route = (
            "Open Work v1.2.78, Delivery Atlas v0.4.20, "
            "FP-001 Skeleton v0.1.22 and HARDEN-02 v0.5.22"
        )
        if approval_route not in candidate_text:
            issues.append("TB-001 contract no longer records its approval-time route")

    open_work = active_files.get("open_work", "")
    state = _open_work_lifecycle_state(open_work)
    expected_state = {
        "status_successor_version": current_open_work.get("semver") if current_open_work else None,
        "architectural_proof_execution": "STARTED",
        "proof_result": "INCOMPLETE / COVERAGE-INCOMPLETE",
        "proof_certification": "NOT CERTIFIED",
        "phase8": "AUTHORISED",
        "application_implementation": _P8_05_BOUNDED_APPLICATION_IMPLEMENTATION,
        "next_stage": _P8_05_NEXT_STAGE_AUTHORISED,
        "phase9_vertical_slices": "NOT STARTED / NOT AUTHORISED",
        "phase8_execution_gate": _P8_05_PHASE8_EXECUTION_GATE_AUTHORISED,
        "current_delivery_atlas": routes["delivery_atlas"].removeprefix("docs/00_platform/"),
        "current_fp001_skeleton": routes["fp001_skeleton"].removeprefix("docs/00_platform/"),
        "current_harden_02": routes["harden_02"].removeprefix("docs/00_platform/"),
        "proof_contract_path": Path(candidate_path).relative_to("docs/00_platform").as_posix(),
    }
    if state is None or any(state.get(key) != value for key, value in expected_state.items()):
        issues.append("Open Work lifecycle state disagrees with current Phase 8 routes or proof status")
    if state is not None:
        next_action = str(state.get("next_governance_action", ""))
        required_next_action_tokens = (
            "p8-05 implementation authorised",
            "bounded phase 8",
            "well-48",
            "resulting-main verification",
        )
        if any(token.casefold() not in next_action.casefold() for token in required_next_action_tokens):
            issues.append("Open Work does not route bounded P8-05 authorization and the WELL-48–50 frontier")
        if "unauthorised" in next_action.casefold() and "implementation authorised" not in next_action.casefold():
            issues.append("Open Work current action reverts bounded P8-05 implementation authorization")
        atlas_text = active_files.get("delivery_atlas", "")
        atlas_predecessor = re.search(
            r"(?im)^- \*\*Predecessor:\*\* `archive/([^`]+\.md)`",
            "\n".join(atlas_text.splitlines()[:45]),
        )
        if atlas_predecessor is not None and (
            f"immediate routing predecessor `archive/{atlas_predecessor.group(1)}`" not in open_work
        ):
            issues.append(f"Open Work Atlas predecessor does not match current route: {atlas_predecessor.group(1)}")

    current_open_work_text = _p8_05_current_authorization_section(open_work)
    if not current_open_work_text:
        issues.append("current Open Work has no bounded P8-05 implementation authorization section")

    required_current_tokens = _p8_05_current_authorization_section_tokens() + (
        "Implementation/JIT verification is COMPLETE",
    )
    if any(token.casefold() not in current_open_work_text.casefold() for token in required_current_tokens):
        issues.append("current Open Work status omits bounded P8-05 authorization or proof boundaries")
    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    if active_start < 0 or active_end < 0 or active_start >= active_end:
        issues.append("current Open Work programme-state section is missing")
    else:
        active_summary = open_work[active_start:active_end]
        programme_proof_tokens = (
            "WELL-5 / P8-04",
            "PROOF EXECUTION: STARTED",
            "PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
            "PROOF CERTIFICATION: NOT CERTIFIED",
            "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
            "WELL-48–50: NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION",
        )
        if any(token.casefold() not in active_summary.casefold() for token in programme_proof_tokens):
            issues.append("current Open Work programme state omits proof execution or authorization boundaries")
    if not any(
        token in current_open_work_text.casefold()
        for token in ("incomplete / coverage-incomplete", "coverage.incomplete")
    ):
        issues.append("current Open Work status omits the coverage-incomplete TB-001 result")
    if re.search(r"(?im)^\s*PROOF (?:RESULT|CERTIFICATION)\s*:\s*(?:PASS|COMPLETE|CERTIFIED)", current_open_work_text):
        issues.append("current Open Work claims a completed TB-001 proof result or certification")

    readme_path = root / "docs/00_platform/README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() and not readme_path.is_symlink() else ""
    readme_current = _markdown_h2_section(readme, "Current State") or ""
    active_artifacts = _markdown_h2_section(readme, "Active Working Artifacts") or ""
    for relative in routes.values():
        name = Path(relative).name
        if name not in readme:
            issues.append(f"README does not route current artifact {relative}")
        if relative.startswith("docs/00_platform/working/") and relative.removeprefix("docs/00_platform/") not in active_artifacts:
            issues.append(f"README active working artifacts omit {relative}")
    if candidate_path.removeprefix("docs/00_platform/") not in active_artifacts:
        issues.append("README active working artifacts omit the approved TB-001 contract")
    current_state_tokens = (
        "PHASE 7B EXECUTION/CONTROL TRACKER #120: CLOSED / COMPLETED",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "TRACER BULLET ID: TB-001",
        "WELL-5 / P8-04: COMPLETE",
        "PROOF EXECUTION: STARTED",
        "PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
        "PROOF CERTIFICATION: NOT CERTIFIED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        "P8-05 planning: COMPLETE",
        "Spec/ticket decomposition: COMPLETE",
        "Independent planning review: COMPLETE / PASS WITH NON-BLOCKING CORRECTIONS",
        "WELL-45: LEGAL/PRIVACY RELEASE GATE OPEN — DEVELOPMENT BASELINE PERMITTED; NOT LEGALLY APPROVED",
        "WELL-48–50: NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION; NOT COMPLETE",
        "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
        "APPLICATION IMPLEMENTATION: AUTHORISED ONLY INSIDE BOUNDED PHASE 8 ARCHITECTURAL PROOF, INCLUDING P8-05",
        "NEXT EXECUTION ACTION: After this authorization is current and resulting-main verification succeeds",
        "WELL-45 remains a legal/privacy release gate",
        "PROOF RESULT: INCOMPLETE / COVERAGE-INCOMPLETE",
    )
    for token in current_state_tokens:
        if token.casefold() not in readme_current.casefold():
            issues.append(f"README current state omits {token!r}")
    if not re.search(r"(?i)\bPhase 8(?:\s+(?:is|are|remains))?\s+NOT CERTIFIED\b", readme_current):
        issues.append("README current state does not mark Phase 8 as NOT CERTIFIED")
    if "PROOF RESULT: NOT STARTED" in readme_current or "PROOF CERTIFICATION: NOT STARTED" in readme_current:
        issues.append("README current state retains a stale not-started proof result or certification")
    if re.search(
        r"(?i)\bphase\s+7c\b[^.!?\n]{0,100}\bblocked\b[^.!?\n]{0,40}\bnot[\s/_-]*started\b",
        readme_current,
    ):
        issues.append("README current state contains a BLOCKED / NOT_STARTED Phase 7C statement")

    current_prose = "\n".join(
        _markdown_h2_section(readme, heading) or ""
        for heading in (
            "Default Agent Context",
            "Current Authority",
            "Active Working Artifacts",
            "Delivery Atlas routing",
            "Current State",
        )
    )
    graph_rules = integrity_rules.get("graph_rules", {})
    retired_predecessors = (
        graph_rules.get("retired_current_predecessor_paths", [])
        if isinstance(graph_rules, dict)
        else []
    )
    for retired_path in retired_predecessors:
        if not isinstance(retired_path, str):
            continue
        filename = Path(retired_path).name
        prose_without_archived_references = current_prose.replace(f"archive/{filename}", "")
        if re.search(
            rf"(?<![A-Za-z0-9_.-]){re.escape(filename)}(?![A-Za-z0-9_.-])",
            prose_without_archived_references,
        ):
            issues.append(
                "README current prose routes retired predecessor without archive qualification: "
                f"{filename}"
            )

    current_authority = _markdown_h2_section(readme, "Default Agent Context") or ""
    open_work_name = Path(routes["open_work"]).name
    if open_work_name not in current_authority:
        issues.append(f"README current authority omits the routed Open Work file {open_work_name}")
    atlas_routing = _markdown_h2_section(readme, "Delivery Atlas routing") or ""
    atlas_name = Path(routes["delivery_atlas"]).name
    if atlas_name not in atlas_routing:
        issues.append(f"README Delivery Atlas routing does not resolve to {atlas_name}")

    support_tokens = _p8_05_current_authorization_section_tokens()
    for label in ("delivery_atlas", "fp001_skeleton", "harden_02"):
        text = active_files.get(label, "")
        section = _p8_05_current_authorization_section(text)
        if not section:
            issues.append(f"current {label} does not have a bounded P8-05 authorization section")
            continue
        for token in support_tokens:
            if token.casefold() not in section.casefold():
                issues.append(f"current {label} status omits {token!r}")
        if "phase 8" not in section.casefold():
            issues.append(f"current {label} status omits the Phase 8 certification boundary")
        if "independent planning review" in section.casefold() and not any(
            status in section.casefold()
            for status in ("complete", "pass with non-blocking corrections")
        ):
            issues.append(f"current {label} status incorrectly leaves the completed independent planning review outstanding")

    current_harden = active_files.get("harden_02", "")
    if "No application implementation is authorised by HARDEN-02 itself" not in current_harden:
        issues.append("current HARDEN-02 does not preserve its implementation-authority boundary")
    harden_authorization = _p8_05_current_authorization_section(current_harden)
    if not harden_authorization or "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED" not in harden_authorization:
        issues.append("current HARDEN-02 does not record bounded P8-05 implementation authorization")

    issues.extend(_phase8_status_transition_source_issues(repository_root))

    return issues


def _phase8_status_successor_base_commit_issue(repository_root: Path) -> str | None:
    repository = subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if repository.returncode != 0:
        return "cannot locate Git repository for pinned status successor base"
    result = subprocess.run(
        [
            "git",
            "-C",
            repository.stdout.strip(),
            "cat-file",
            "-e",
            f"{PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA}^{{commit}}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return f"pinned status successor base commit is unavailable: {PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA}"
    return None


def _phase8_pinned_base_manifest(
    repository_root: Path,
) -> tuple[dict[str, Any] | None, str]:
    repository = subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if repository.returncode != 0:
        return None, "cannot locate Git repository for pinned status successor manifest"
    repository_path = Path(repository.stdout.strip()).resolve()
    cache_key = (repository_path, PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA)
    cached = _PHASE8_PINNED_BASE_MANIFEST_CACHE.get(cache_key)
    if cached is not None:
        return cached
    result = subprocess.run(
        [
            "git",
            "-C",
            str(repository_path),
            "show",
            f"{PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA}:{DEFAULT_MANIFEST.as_posix()}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        value = (None, "pinned status successor base manifest is unavailable")
    else:
        try:
            manifest = json.loads(
                result.stdout,
                object_pairs_hook=_reject_duplicate_json_keys,
            )
        except (json.JSONDecodeError, TypeError, ValueError):
            value = (None, "pinned status successor base manifest is invalid")
        else:
            value = (
                (manifest, "")
                if isinstance(manifest, dict)
                else (None, "pinned status successor base manifest has an invalid root")
            )
    _PHASE8_PINNED_BASE_MANIFEST_CACHE[cache_key] = value
    return value


def _phase8_phase7c_promotion_rule_issues(
    root: Path,
    repository_root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> list[str]:
    base_manifest, base_issue = _phase8_pinned_base_manifest(repository_root)
    if base_manifest is None:
        return [base_issue]
    base_rules = base_manifest.get("integrity_rules", {})
    base_rule = base_rules.get("fp001_phase7c_final_contract_current_promotion", {}) if isinstance(base_rules, dict) else {}
    current_rule = integrity_rules.get("fp001_phase7c_final_contract_current_promotion", {})
    phase8 = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    if not isinstance(base_rule, dict) or not isinstance(current_rule, dict) or not isinstance(phase8, dict):
        return ["pinned or current Phase 7C promotion rule is missing"]

    issues: list[str] = []
    mutable_fields = {
        "current_paths",
        "current_route_status_successor_version",
        "predecessor_archives_sha256",
        "protected_current_artifacts_sha256",
    }
    for key in (set(base_rule) | set(current_rule)) - mutable_fields:
        if base_rule.get(key) != current_rule.get(key):
            issues.append(f"Phase 7C PR #126 promotion evidence changed outside current routing: {key}")

    routes = phase8.get("current_routes", {})
    if current_rule.get("current_paths") != routes:
        issues.append("Phase 7C promotion current paths disagree with the Phase 8 route map")
    route_versions = []
    for key in ("open_work", "delivery_atlas", "fp001_skeleton", "harden_02"):
        route = routes.get(key, "") if isinstance(routes, dict) else ""
        version = re.search(r"_v(\d+\.\d+\.\d+)\.md$", route)
        if version is None:
            issues.append(f"Phase 7C promotion current route is unversioned: {key}")
        else:
            route_versions.append(version.group(1))
    if len(route_versions) == 4 and current_rule.get("current_route_status_successor_version") != " / ".join(route_versions):
        issues.append("Phase 7C promotion successor tuple disagrees with current route filenames")

    base_hashes = base_rule.get("predecessor_archives_sha256", {})
    current_hashes = current_rule.get("predecessor_archives_sha256", {})
    if not isinstance(base_hashes, dict) or not isinstance(current_hashes, dict):
        return issues + ["Phase 7C promotion predecessor archive hash maps are malformed"]
    if any(current_hashes.get(path) != digest for path, digest in base_hashes.items()):
        issues.append("Phase 7C promotion changed an existing predecessor archive hash")


    # The pinned Phase 7C promotion baseline can be several routing successors
    # behind the current route. Preserve each archived route in that chain, not
    # only the current file's immediate predecessor. Otherwise a later status
    # successor would either drop valid history pins or fail because earlier
    # successors added their direct predecessor archives after the pinned base.
    base_phase8 = base_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    base_routes = base_phase8.get("current_routes", {}) if isinstance(base_phase8, dict) else {}
    if not isinstance(base_routes, dict):
        return issues + ["pinned Phase 8 route map is invalid"]


    base_protected = base_rule.get("protected_current_artifacts_sha256", {})
    current_protected = current_rule.get("protected_current_artifacts_sha256", {})
    identity_path = "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
    prior_identity_path = "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
    if not isinstance(base_protected, dict) or not isinstance(current_protected, dict):
        issues.append("Phase 7C promotion protected-current artifact maps are malformed")
    else:
        if current_protected.get(identity_path) != sha256_file(root / identity_path):
            issues.append("current Identity v0.2.0 protected dossier hash differs from its bytes")
        if prior_identity_path in current_protected:
            issues.append("superseded Identity v0.1.4 remains pinned as current")
        for path, digest in base_protected.items():
            if path == prior_identity_path:
                continue
            if current_protected.get(path) != digest:
                issues.append(f"Phase 7C promotion changed protected current artifact outside Identity routing: {path}")
        expected_current_protected = (set(base_protected) - {prior_identity_path}) | {identity_path}
        if set(current_protected) != expected_current_protected:
            issues.append("Phase 7C promotion protected-current change is not limited to the Identity v0.1.4-to-v0.2.0 route")

    new_archives: set[str] = set()
    for label in ("open_work", "delivery_atlas", "fp001_skeleton", "harden_02"):
        route = routes.get(label, "") if isinstance(routes, dict) else ""
        baseline_route = base_routes.get(label)
        if not isinstance(route, str) or not isinstance(baseline_route, str):
            issues.append(f"current or pinned {label} route is invalid")
            continue

        cursor = route
        visited: set[str] = set()
        baseline_filename = Path(baseline_route).name
        reached_baseline = cursor == baseline_route
        while cursor != baseline_route:
            if cursor in visited:
                issues.append(f"current {label} route predecessor chain contains a cycle")
                break
            visited.add(cursor)
            path = root / cursor
            text = path.read_text(encoding="utf-8") if path.is_file() else ""
            header = "\n".join(text.splitlines()[:45])
            predecessor = re.search(r"(?im)^.*predecessor.*`(archive/[^`]+\.md)`", header)
            if predecessor is None:
                issues.append(f"current {label} route predecessor chain does not reach its pinned route")
                break
            archive_relative = f"docs/00_platform/{predecessor.group(1)}"
            archive = root / archive_relative
            if not archive.is_file():
                issues.append(f"current {label} route predecessor chain is missing {archive_relative}")
                break
            new_archives.add(archive_relative)
            if Path(archive_relative).name == baseline_filename:
                if archive_relative != f"docs/00_platform/archive/{baseline_filename}":
                    issues.append(f"current {label} route predecessor chain reaches the pinned filename outside archive/")
                reached_baseline = True
                break
            cursor = archive_relative
        if not reached_baseline:
            issues.append(f"current {label} route predecessor chain does not reach its pinned route")
    if set(current_hashes) - set(base_hashes) != new_archives:
        issues.append("Phase 7C promotion predecessor pins do not add exactly the archived current-route successor chain")
    return issues


def _phase8_phase7b_preservation_issues(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> list[str]:
    issues: list[str] = []
    routes = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {}).get("current_routes", {})
    skeleton_relative = routes.get("fp001_skeleton") if isinstance(routes, dict) else None
    skeleton = root / skeleton_relative if isinstance(skeleton_relative, str) else None
    skeleton_text = skeleton.read_text(encoding="utf-8") if skeleton is not None and skeleton.is_file() else ""
    header = "\n".join(skeleton_text.splitlines()[:45])
    predecessor = re.search(r"(?im)^.*predecessor.*`(archive/[^`]+\.md)`", header)
    if predecessor is None:
        issues.append("current Skeleton does not name its direct predecessor archive")
        predecessor_text = ""
    else:
        predecessor_path = root / "docs/00_platform" / predecessor.group(1)
        predecessor_text = predecessor_path.read_text(encoding="utf-8") if predecessor_path.is_file() else ""
        if not predecessor_text:
            issues.append("current Skeleton predecessor archive is missing")

    marker_start = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:START -->"
    marker_end = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:END -->"

    def marked_pmr(text: str) -> str:
        if text.count(marker_start) != 1 or text.count(marker_end) != 1:
            return ""
        start = text.index(marker_start)
        end = text.index(marker_end)
        return text[start : end + len(marker_end)] if start < end else ""

    current_pmr = marked_pmr(skeleton_text)
    predecessor_pmr = marked_pmr(predecessor_text)
    if not current_pmr or current_pmr != predecessor_pmr:
        issues.append("current Skeleton changed the certified Phase 7B PMR contract block")
    for token in (
        "Phase 7B reconciliation v0.1.0 is COMPLETE / CERTIFIED / CURRENT",
        "The six affected Domains and seven material capability relationships remain unchanged.",
        "exact PR #121 candidate bytes remain preserved as immutable archive evidence",
    ):
        if token.casefold() not in skeleton_text.casefold():
            issues.append(f"current Skeleton omits preserved Phase 7B evidence: {token}")

    promotion = integrity_rules.get("fp001_phase7c_final_contract_current_promotion", {})
    protected = promotion.get("protected_current_artifacts_sha256", {}) if isinstance(promotion, dict) else {}
    if not isinstance(protected, dict) or not any("PHASE_7B_RECONCILIATION" in path for path in protected):
        issues.append("Phase 7C promotion rule does not protect the certified Phase 7B artifact")
    else:
        for relative, digest in protected.items():
            path = root / relative
            if not path.is_file() or sha256_file(path) != digest:
                issues.append(f"protected Phase 7B/Phase 7C source changed: {relative}")

    active_phase7b = [
        entry
        for entry in _all_entries(manifest)
        if entry.get("document_id") == "FP001_PHASE_7B_RECONCILIATION_PR_121_CANDIDATE"
        and entry.get("lifecycle") == "historical"
        and entry.get("repository_path") == "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
    ]
    if len(active_phase7b) != 1:
        issues.append("manifest does not preserve the exact PR #121 Phase 7B candidate as historical evidence")
    return issues


def _audit_exact_predecessor_commit(repository_root: Path, sha: str) -> tuple[bool, str]:
    """Run the full audit on the pinned pre-transition tree from Git history."""

    if sha != PHASE8_APPROVED_STATUS_SUCCESSOR_BASE_SHA:
        return False, "status successor base SHA is not the required main baseline"
    repository = subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if repository.returncode != 0:
        return False, "cannot locate Git repository for the pinned predecessor audit"
    repository_root = Path(repository.stdout.strip())
    check = subprocess.run(
        ["git", "-C", str(repository_root), "cat-file", "-e", f"{sha}^{{commit}}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if check.returncode != 0:
        return False, f"pinned predecessor commit is unavailable: {sha}"
    cache_key = (repository_root.resolve(), sha)
    cached = _PHASE8_PREDECESSOR_AUDIT_CACHE.get(cache_key)
    if cached is not None:
        return cached
    with tempfile.TemporaryDirectory(prefix="foundation-integrity-predecessor-") as directory:
        archive_path = Path(directory) / "predecessor.tar"
        tree_path = Path(directory) / "tree"
        tree_path.mkdir()
        with archive_path.open("wb") as output:
            archived = subprocess.run(
                ["git", "-C", str(repository_root), "archive", "--format=tar", sha],
                stdout=output,
                stderr=subprocess.PIPE,
                text=False,
                check=False,
            )
        if archived.returncode != 0:
            error = archived.stderr.decode("utf-8", errors="replace").strip()
            return False, f"cannot export pinned predecessor tree: {error}"
        try:
            with tarfile.open(archive_path, "r:") as archive:
                archive.extractall(tree_path, filter="data")
        except (OSError, tarfile.TarError) as error:
            return False, f"cannot materialize pinned predecessor tree: {error}"
        predecessor_manifest = tree_path / DEFAULT_MANIFEST
        if not predecessor_manifest.is_file():
            return False, "pinned predecessor has no current authority manifest"
        historical_tool_path = tree_path / "tools/foundation_integrity_audit.py"
        historical_spec = importlib.util.spec_from_file_location(
            f"foundation_integrity_audit_{sha[:12]}", historical_tool_path
        )
        if historical_spec is None or historical_spec.loader is None:
            return False, "cannot load Foundation Integrity tool from the exact historical tree"
        historical_tool = importlib.util.module_from_spec(historical_spec)
        historical_spec.loader.exec_module(historical_tool)
        report = historical_tool.run_audit(
            tree_path,
            predecessor_manifest,
        )
        if report.get("status") != "PASS":
            failures = "; ".join(
                f"{finding.get('check')}: {finding.get('message')}"
                for finding in report.get("findings", [])[:5]
            )
            return False, f"pinned predecessor full audit failed: {failures}"
        result = (
            True,
            f"exact predecessor {sha} passes {report.get('assertion_count')} Foundation Integrity assertions",
        )
        _PHASE8_PREDECESSOR_AUDIT_CACHE[cache_key] = result
        return result


def _identity_v020_promotion_issues(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> list[str]:
    """Check the separate Identity v0.2.0 current-status promotion and its evidence pins."""

    issues: list[str] = []
    active_path = "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
    candidate_path = "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
    predecessor_path = "docs/00_platform/archive/identity_promotions/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
    expected_hashes = {
        candidate_path: "3a6d914cef77c198e6068f3e27f4b968225dd06939c286557d99797af90df699",
        predecessor_path: "3560e0cb147e21cdaa149b7e1c2abe43ad03af04619d08175ef0544279fa0d0f",
    }
    if integrity_rules.get("identity_v020_promotion_archives") != expected_hashes:
        issues.append("Identity candidate and v0.1.4 promoted-current archive pins differ from accepted evidence")
    for path, expected_hash in expected_hashes.items():
        source = root / path
        if not source.is_file() or source.is_symlink() or sha256_file(source) != expected_hash:
            issues.append(f"Identity promotion archive is missing or differs from exact source bytes: {path}")

    active = root / active_path
    if not active.is_file() or active.is_symlink():
        issues.append("Identity v0.2.0 current dossier is missing or is a symlink")
        active_text = ""
        lifecycle: dict[str, Any] = {}
    else:
        active_text = active.read_text(encoding="utf-8")
        region_parts = active_text.split("<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_START -->", 1)
        region = region_parts[1].split("<!-- IDENTITY_V020_CURRENT_LIFECYCLE_STATE_END -->", 1)[0] if len(region_parts) == 2 else ""
        state_match = re.search(r"```json\s*(\{.*?\})\s*```", region, re.DOTALL)
        try:
            lifecycle = json.loads(state_match.group(1)) if state_match else {}
        except json.JSONDecodeError:
            lifecycle = {}
        required_lifecycle = {
            "artifact_version": "v0.2.0",
            "identity_lifecycle": "CERTIFIED / CURRENT",
            "pr_150_candidate_certification": "COMPLETE",
            "pr_150_post_merge_certification_evidence": "COMPLETE",
            "current_status_promotion": "PR #151 STATUS SUCCESSOR",
            "well_45": "LEGAL/PRIVACY RELEASE GATE OPEN — DEVELOPMENT BASELINE PERMITTED; NOT LEGALLY APPROVED",
            "well_48": "NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION / NOT COMPLETE",
            "phase_8_application_implementation": "AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION AUTHORISED",
            "p8_05_registration_implementation": "AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
            "owner_decisions": "CANONICALLY RECORDED",
        }
        if any(lifecycle.get(key) != value for key, value in required_lifecycle.items()):
            issues.append("Identity v0.2.0 lifecycle state does not record current status and retained gates")
        if "**Status:** `CERTIFIED / CURRENT`" not in active_text:
            issues.append("Identity v0.2.0 dossier header does not state CERTIFIED / CURRENT")
        for token in (
            "Identity-owned `RegistrationOperation` Ash Resource",
            "Eight-resource physical Ash implementation set",
            "HMAC-SHA-256",
            "Identity registration-binding key",
            "24-hour",
            "duplicate-email",
        ):
            if token.casefold() not in active_text.casefold():
                issues.append(f"current Identity dossier omits accepted RegistrationOperation contract token: {token}")

    candidate = root / candidate_path
    if candidate.is_file() and not candidate.is_symlink():
        candidate_text = candidate.read_text(encoding="utf-8")
        for token in (
            "CANDIDATE / CERTIFICATION PENDING / NOT CURRENT",
            "RegistrationOperation",
        ):
            if token not in candidate_text:
                issues.append(f"archived PR #150 candidate evidence omits {token!r}")
    for token in (
        "d43b6b32c2dec9cf54b5d4492d942a70984a8591",
        "40299236086",
        "40302375237",
    ):
        if token not in active_text:
            issues.append(f"current Identity dossier omits PR #150 certification evidence {token}")

    phase7c = integrity_rules.get("fp001_phase7c_final_contract_current_promotion", {})
    phase8 = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {})
    protected_current = phase7c.get("protected_current_artifacts_sha256", {}) if isinstance(phase7c, dict) else {}
    protected_jit = phase8.get("protected_required_jit_dossier_sha256", {}) if isinstance(phase8, dict) else {}
    active_digest = sha256_file(active) if active.is_file() and not active.is_symlink() else None
    if protected_current.get(active_path) != active_digest or protected_jit.get(active_path) != active_digest:
        issues.append("Identity v0.2.0 current dossier hash is not pinned in both current-artifact maps")
    prior_identity_path = "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
    if prior_identity_path in protected_current:
        issues.append("superseded Identity v0.1.4 remains pinned as current")
    if (root / "docs/00_platform/working/candidates/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md").exists():
        issues.append("PR #150 candidate remains routed under the mutable candidates directory")
    if (root / prior_identity_path).exists():
        issues.append("superseded Identity v0.1.4 remains at the active working route")

    history = manifest.get("historical_documents", [])
    predecessor_entry = next(
        (entry for entry in history if isinstance(entry, dict) and entry.get("document_id") == "FP001_IDENTITY_ACCESS_DOSSIER_V0_1_4_PROMOTED_CURRENT"),
        None,
    )
    if (
        not isinstance(predecessor_entry, dict)
        or predecessor_entry.get("repository_path") != predecessor_path
        or predecessor_entry.get("sha256") != expected_hashes[predecessor_path]
    ):
        issues.append("promoted/current Identity v0.1.4 snapshot is not registered as distinct historical evidence")

    spec_path = root / "docs/execution/p8-05-registration-jit-spec.md"
    spec = spec_path.read_text(encoding="utf-8") if spec_path.is_file() and not spec_path.is_symlink() else ""
    for token in (
        "preserve local-part bytes and case",
        "IDNA has a separately reviewed rule",
        "36^16",
        "ISO/IEC 7064 MOD 37,2",
        "registration-binding:v1",
        "HMAC-SHA-256",
        "dedicated environment-specific Identity registration-binding key",
        "24 hours",
        "WELL-45 remains",
        "WELL-48",
    ):
        if token.casefold() not in spec.casefold():
            issues.append(f"P8-05 spec omits canonically recorded WELL-48 decision: {token}")
    if "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY" not in spec:
        issues.append("P8-05 spec omits the bounded implementation authorization")

    readme_path = root / "docs/00_platform/README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() and not readme_path.is_symlink() else ""
    for token in (
        active_path.removeprefix("docs/00_platform/"),
        candidate_path.removeprefix("docs/00_platform/"),
        "promoted/current v0.1.4 snapshot",
        "CERTIFIED / CURRENT",
        "WELL-45 is a legal/privacy release gate",
        "WELL-48–50: NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION; NOT COMPLETE",
        "APPLICATION IMPLEMENTATION: AUTHORISED ONLY INSIDE BOUNDED PHASE 8 ARCHITECTURAL PROOF, INCLUDING P8-05",
        "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
    ):
        if token not in readme:
            issues.append(f"README Identity current route omits {token!r}")

    open_work_path = root / "docs/00_platform/02_OPEN_WORK_v1.2.84.md"
    open_work = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() and not open_work_path.is_symlink() else ""
    for token in (
        "PR #150",
        "40299236086",
        "40302375237",
        "Identity v0.2.0: COMPLETE / CERTIFIED / CURRENT under PR #151 status successor",
        "P8-05 / WELL-6 IMPLEMENTATION: AUTHORISED — BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY",
        "WELL-48–50: NEXT PERMITTED IMPLEMENTATION FRONTIER AFTER RESULTING-MAIN VERIFICATION; NOT COMPLETE",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY); P8-05 IMPLEMENTATION AUTHORISED",
        "PHASE 8: NOT CERTIFIED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
    ):
        if token.casefold() not in open_work.casefold():
            issues.append(f"Open Work omits Identity promotion evidence or retained gate: {token}")
    return issues


def _check_phase8_approved_status_successor(
    root: Path,
    repository_root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> bool:
    started_status_is_current = _fp001_phase8_execution_status_successor_is_current(manifest)
    issues = _phase8_approved_status_successor_issues(
        root, repository_root, manifest, integrity_rules
    )
    identity_issues = _identity_v020_promotion_issues(root, manifest, integrity_rules) if _fp001_phase8_execution_status_successor_is_current(manifest) else []
    issues.extend(identity_issues)
    transition_ok = not issues
    active_open_work = _active_open_work_entry(manifest)
    current_path = _relative_path(active_open_work) if active_open_work else "docs/00_platform/02_OPEN_WORK_v1.2.78.md"
    _record_check(
        report,
        "phase8_approved_status_successor_current",
        transition_ok,
        "Current Open Work status routes WELL-5 completion, the incomplete TB-001 result and the P8-05 planning gate"
        if transition_ok and started_status_is_current
        else "Open Work v1.2.78 routes approved TB-001 and preserves the separate proof-execution and Phase 9 stops"
        if transition_ok
        else "; ".join(issues),
        path=current_path,
    )

    if started_status_is_current:
        identity_path = "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md"
        _record_check(
            report,
            "identity_v020_current_status_promotion",
            not identity_issues,
            "Identity v0.2.0 is current with PR #150 evidence, preserved predecessor snapshots, and canonical P8-05 owner decisions"
            if not identity_issues
            else "; ".join(identity_issues),
            path=identity_path,
        )

    if started_status_is_current:
        phase8_rule = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {})
        candidate_path = phase8_rule.get("candidate_path") if isinstance(phase8_rule, dict) else None
        candidate = root / candidate_path if isinstance(candidate_path, str) else None
        candidate_archive_path = phase8_rule.get("reviewed_candidate_archive_path") if isinstance(phase8_rule, dict) else None
        candidate_archive = root / candidate_archive_path if isinstance(candidate_archive_path, str) else None
        candidate_issues: list[str] = []
        if candidate is None or not candidate.is_file() or candidate.is_symlink():
            candidate_issues.append("approved TB-001 proof contract is missing")
            candidate_text = ""
        else:
            candidate_text = candidate.read_text(encoding="utf-8")
            candidate_digest = sha256_file(candidate)
            route_hashes = phase8_rule.get("current_route_sha256", {})
            if not isinstance(route_hashes, dict) or candidate_digest != route_hashes.get(candidate_path):
                candidate_issues.append("approved TB-001 proof contract bytes differ from its frozen hash")
            candidate_issues.extend(_fp001_phase8_proof_contract_content_issues(candidate_text))
        if (
            candidate_archive is None
            or not candidate_archive.is_file()
            or sha256_file(candidate_archive) != phase8_rule.get("reviewed_candidate_archive_sha256")
            or phase8_rule.get("reviewed_candidate_archive_sha256") != phase8_rule.get("candidate_sha256")
        ):
            candidate_issues.append("approved TB-001 contract archive bytes are not preserved")
        approval_route = (
            "Open Work v1.2.78, Delivery Atlas v0.4.20, "
            "FP-001 Skeleton v0.1.22 and HARDEN-02 v0.5.22"
        )
        if approval_route not in candidate_text:
            candidate_issues.append("TB-001 contract approval-time route is not preserved")
        _record_check(
            report,
            "fp001_phase8_proof_contract_lifecycle",
            not candidate_issues,
            "approved TB-001 design and approval-time route remain frozen"
            if not candidate_issues
            else "; ".join(candidate_issues),
            path=str(candidate_path or ""),
        )

        promotion_issues = _phase8_phase7c_promotion_rule_issues(
            root, repository_root, manifest, integrity_rules
        )
        _record_check(
            report,
            "fp001_phase7c_final_contract_current_promotion",
            not promotion_issues,
            "PR #126 Phase 7C certification evidence is unchanged and current routes match the status successor"
            if not promotion_issues
            else "; ".join(promotion_issues),
            path=phase8_rule.get("current_routes", {}).get("open_work", ""),
        )

        phase7b_issues = _phase8_phase7b_preservation_issues(
            root, manifest, integrity_rules
        )
        _record_check(
            report,
            "phase8_status_successor_phase7b_preservation",
            not phase7b_issues,
            "certified Phase 7B PMR semantics and PR #121 archive remain unchanged"
            if not phase7b_issues
            else "; ".join(phase7b_issues),
            path=phase8_rule.get("current_routes", {}).get("fp001_skeleton", ""),
        )

    if started_status_is_current:
        base_issue = _phase8_status_successor_base_commit_issue(repository_root)
        _record_check(
            report,
            "phase8_status_successor_predecessor_provenance",
            base_issue is None,
            f"pinned status successor base {PHASE8_WELL5_STATUS_SUCCESSOR_BASE_SHA} is available for archive verification"
            if base_issue is None
            else base_issue,
            path="docs/00_platform/archive/02_OPEN_WORK_v1.2.79.md",
        )
        return transition_ok and base_issue is None

    current_open_work_path = root / current_path
    state = _open_work_lifecycle_state(current_open_work_path.read_text(encoding="utf-8")) if current_open_work_path.is_file() else None
    base_sha = state.get("status_successor_base_sha") if isinstance(state, dict) else ""
    predecessor_ok, predecessor_message = _audit_exact_predecessor_commit(repository_root, str(base_sha))
    _record_check(
        report,
        "phase8_approved_status_successor_predecessor_full_audit",
        predecessor_ok,
        predecessor_message,
        path=(
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.78.md"
            if started_status_is_current
            else "docs/00_platform/02_OPEN_WORK_v1.2.77.md"
        ),
    )

    historical_names = (
        "roadmap_proof_classification_lifecycle",
        "fp001_development_entry_hard_stop_lifecycle",
        "fp001_phase8_proof_contract_lifecycle",
        "fp001_pmr_reconciliation",
        "fp001_phase7b_baseline_and_dossiers",
        "fp001_phase7b_gate_routing",
        "fp001_phase7b_certification_current",
        "fp001_phase7c_final_contract_current_promotion",
        "platform_readme_router_consistency",
    )
    for name in historical_names:
        _record_check(
            report,
            name,
            predecessor_ok,
            "predecessor-era current-status assertions pass on the pinned exact-SHA snapshot; v1.2.78 routing is checked separately"
            if predecessor_ok
            else predecessor_message,
            path=(
                "docs/00_platform/archive/02_OPEN_WORK_v1.2.78.md"
                if started_status_is_current
                else "docs/00_platform/archive/02_OPEN_WORK_v1.2.77.md"
            ),
        )
    return transition_ok and predecessor_ok


def _check_platform_readme_router_consistency(
    root: Path,
    report: dict[str, Any],
) -> None:
    """Fail closed when README current routing prose drifts from Open Work classification status."""

    issues: list[str] = []
    readme_path = root / "docs" / "00_platform" / "README.md"
    open_work_path = root / "docs" / "00_platform" / "02_OPEN_WORK_v1.2.77.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    open_work = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() else ""

    current_prose = readme.split("## Historical status evidence", 1)[0] if "## Historical status evidence" in readme else readme
    stale_patterns = (
        (r"(?i)proof classification (?:is|remains) not finalised", "README current prose claims proof classification is not finalised"),
        (r"(?i)architectural proof classification is next", "README current prose treats architectural proof classification as next/unperformed"),
        (r"(?i)architectural proof classification.*remains unperformed", "README current prose treats architectural proof classification as unperformed"),
    )
    for pattern, message in stale_patterns:
        if re.search(pattern, current_prose):
            issues.append(message)

    atlas_routing = _markdown_h2_section(readme, "Delivery Atlas routing") or ""
    if "working/DELIVERY_ATLAS_WORKING_v0.4.19.md" not in atlas_routing:
        issues.append("README Delivery Atlas routing section does not route v0.4.19")
    if re.search(r"\(working/DELIVERY_ATLAS_WORKING_v0\.4\.(?:15|16|17)\.md\)", atlas_routing):
        issues.append("README Delivery Atlas routing section still links a retired predecessor")

    state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work,
        re.DOTALL,
    )
    try:
        state = json.loads(state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        state = {}
    if state.get("proof_classification") != "NEW_TRACER_BULLET":
        issues.append("Open Work lifecycle state does not record NEW_TRACER_BULLET")
    if state.get("architectural_proof_classification_status") != "COMPLETE / FINALISED":
        issues.append("Open Work lifecycle state does not record COMPLETE / FINALISED classification")

    current_state = _markdown_h2_section(readme, "Current State") or ""
    for token in (
        "PHASE 7B EXECUTION/CONTROL TRACKER #120: CLOSED / COMPLETED",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "PROGRAMME ROUTER #111: OPEN",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "NEXT GOVERNANCE ACTION: TB-001 CONTRACT CANDIDATE REVIEW / CERTIFICATION",
        "TRACER BULLET: REQUIRED / DEFINED AS REVIEW CANDIDATE",
        "TRACER BULLET ID: TB-001",
        "PROOF DESIGN: FROZEN TO THE ACCEPTED Q1–Q90 DECISIONS",
        "PROOF EXECUTION: NOT STARTED",
        "PROOF RESULT: NOT STARTED",
        "PROOF CERTIFICATION: NOT STARTED",
        "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
    ):
        if token not in current_state:
            issues.append(f"README Current State omits {token!r}")

    _record_check(
        report,
        "platform_readme_router_consistency",
        not issues,
        "README current routing agrees with Open Work hard-stop PASS and the TB-001 candidate route"
        if not issues
        else "; ".join(issues),
        path="docs/00_platform/README.md",
    )


def _check_fp001_phase7c_current_promotion(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Pin the closed Phase 7C tracker route and its hosted provenance."""

    phase8_candidate_current = _fp001_phase8_candidate_route_is_current(manifest)
    current_paths = {
        "open_work": "docs/00_platform/02_OPEN_WORK_v1.2.77.md" if phase8_candidate_current else "docs/00_platform/02_OPEN_WORK_v1.2.74.md",
        "delivery_atlas": "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.19.md" if phase8_candidate_current else "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
        "fp001_skeleton": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md" if phase8_candidate_current else "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
        "harden_02": "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.21.md" if phase8_candidate_current else "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        "final_feature_pack_contract": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
    }
    predecessor_archives = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.72.md": "ea515aff852cdf4e74714793ac3d390d6291a37903f0a1c15e887cdb9f44da5e",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.14.md": "a12ea6f734ad192a5b735bda8018cac3db7fc37d662f75643eb9758310414894",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md": "8bc2b7c61d6feba1c61ea5233677dd8b7344d0704426d8d113e8e5f2b2395f6e",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.16.md": "75b6e739b82a63fe85bb7d2e20f862883bd3e60cb00b2fcce72e7f92849c5cea",
    }
    candidate_archive_path = "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
    candidate_archive_sha256 = "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19"
    protected_current_artifacts = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md": "0872b5566f38a6c9cff53dbf7a236c0ba5b74308053aeb91796a45a3e9d9f852",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.16.md": "9636c1ed2a12f156ebeb31004e0d3823f7e2824b55d9e7107646d8178f5eab32",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md": "9401dc20a362115534dbb2ce16262c032debbe8dcb8e3d2fd5d9c87a1c1c836b",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.18.md": "4de81f097562def5dcba983031bee1052a34193f6c14ec6b2cfa81b6e8f79e58",
        "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md": "9b2c1a6c16df3a48f041403fd336df926132bba46168e07b55acce148c4f59c2",
        "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md": "3560e0cb147e21cdaa149b7e1c2abe43ad03af04619d08175ef0544279fa0d0f",
        "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "cc664c1e5d148c1a8f30f2a8d769645646162ff029494a2187e0a65775c27c83",
        "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "aa6c4a52518225a2d5bbe86734410e5e9e330e29613b1c1e150174e2e3a12046",
        "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md": "d6fb70a9a19286263404d191a60447158c1ccf8097c8be35465def37046169c6",
    }
    expected_rule = {
        "status_successor_base_sha": "24a9ad925ee1ab6d75ddb44bae6df0b4f3d09bca",
        "candidate_pr": 125,
        "approved_candidate_head_sha": "bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5",
        "pr125_reviewed_head_sha": "bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5",
        "candidate_tree_sha": "8e5fc724b4c4f4a6a196d41e3beafc8e1384c2bf",
        "pr125_merge_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
        "pr125_merge_second_parent_sha": "bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5",
        "pr125_merge_tree_sha": "8e5fc724b4c4f4a6a196d41e3beafc8e1384c2bf",
        "pr125_resulting_main_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
        "pr125_resulting_main_tree_sha": "8e5fc724b4c4f4a6a196d41e3beafc8e1384c2bf",
        "pr125_candidate_resulting_main_tree_identity": "PASS",
        "independent_exact_head_review": "PASS",
        "pr125_exact_head_fia_run": 39121794222,
        "pr125_exact_head_fia_status": "completed",
        "pr125_exact_head_fia_conclusion": "success",
        "pr125_exact_head_fia_tests": 443,
        "pr125_exact_head_fia_assertions": 698,
        "pr125_exact_head_fia_findings": 0,
        "pr125_resulting_main_fia_run": 39126317950,
        "pr125_resulting_main_fia_status": "completed",
        "pr125_resulting_main_fia_conclusion": "success",
        "pr125_resulting_main_fia_tests": 443,
        "pr125_resulting_main_fia_assertions": 698,
        "pr125_resulting_main_fia_findings": 0,
        "pr126_base_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
        "pr126_reviewed_head_sha": "e7d5d3908bedf1a75c6627448c3ed0c067b076f8",
        "pr126_merge_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "pr126_reviewed_head_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_merge_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_merge_head_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_head_merge_tree_identity": "PASS",
        "pr126_exact_head_fia_run": 39141076412,
        "pr126_exact_head_fia_status": "completed",
        "pr126_exact_head_fia_conclusion": "success",
        "resulting_main_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "resulting_main_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "resulting_main_fia_run": 39143147487,
        "resulting_main_fia_status": "completed",
        "resulting_main_fia_conclusion": "success",
        "resulting_main_fia_tests": 455,
        "resulting_main_fia_assertions": 728,
        "resulting_main_fia_findings": 0,
        "fresh_resulting_main_verification": "PASS",
        "candidate_archive_path": candidate_archive_path,
        "candidate_archive_sha256": candidate_archive_sha256,
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_tracker_issue": 120,
        "phase_7b_tracker_state": "CLOSED / COMPLETED",
        "programme_router_issue": 111,
        "programme_router_state": "OPEN",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "contract_lifecycle": "COMPLETE / CERTIFIED / CURRENT",
        "proof_classification": "NEW_TRACER_BULLET",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        **({
            "classification_status": "COMPLETE / FINALISED",
            "current_route_status_successor_version": "1.2.77 / 0.4.19 / 0.1.21 / 0.5.21",
        } if phase8_candidate_current else {}),
        "current_paths": current_paths,
        "predecessor_archives_sha256": {
            **predecessor_archives,
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.73.md": "86b8a0b9d181ad6551b5174d3856a1d700209d583970dcc90a7aaa4b72ef8577",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.15.md": "a5b7e2d94b29e077adb6d85605f2cbbbf139dff4983711ee73bfedce2b9bba26",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.17.md": "99c72571ef4243e6d765c4d5dd4b0e5b3dce73d993662916d8bed839ebd2ad55",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.17.md": "a80c6870a6b86dc4e871d0357a11edc877379085b846a348e750ab037741e1d7",
        },
        "protected_current_artifacts_sha256": protected_current_artifacts,
    }
    rule = integrity_rules.get("fp001_phase7c_final_contract_current_promotion", {})
    issues: list[str] = []
    if not isinstance(rule, dict) or any(rule.get(key) != value for key, value in expected_rule.items()):
        issues.append("manifest does not pin PR #126 provenance, resulting-main evidence, closed tracker and current routes")

    for relative, expected_hash in predecessor_archives.items():
        archive = root / relative
        if not archive.is_file() or sha256_file(archive) != expected_hash:
            issues.append(f"direct predecessor archive is missing or changed: {relative}")
        retired_path = relative.replace("/archive/", "/working/")
        if retired_path.endswith("02_OPEN_WORK_v1.2.72.md"):
            retired_path = "docs/00_platform/02_OPEN_WORK_v1.2.72.md"
        elif retired_path.endswith("02_OPEN_WORK_v1.2.71.md"):
            retired_path = "docs/00_platform/02_OPEN_WORK_v1.2.71.md"
        elif retired_path.endswith("02_OPEN_WORK_v1.2.70.md"):
            retired_path = "docs/00_platform/02_OPEN_WORK_v1.2.70.md"
        if (root / retired_path).exists():
            issues.append(f"direct predecessor remains at its retired working path: {retired_path}")
    if isinstance(rule, dict):
        issues.extend(_fp001_protected_historical_evidence_issues(root, rule, integrity_rules))

    candidate = root / candidate_archive_path
    candidate_history = next(
        (entry for entry in _all_entries(manifest) if entry.get("document_id") == "FP001_PHASE_7C_CONTRACT_PR_125_CANDIDATE"),
        None,
    )
    if not candidate.is_file() or sha256_file(candidate) != candidate_archive_sha256:
        issues.append("immutable PR #125 candidate archive is missing or its SHA-256 changed")
    if (
        not isinstance(candidate_history, dict)
        or _relative_path(candidate_history) != candidate_archive_path
        or candidate_history.get("sha256") != candidate_archive_sha256
        or candidate_history.get("provenance_sha256") != candidate_archive_sha256
        or candidate_history.get("lifecycle") != "historical"
        or candidate_history.get("graph_policy") != "frozen_provenance"
        or candidate_history.get("authority_class") != "FP001_PHASE_7C_CONTRACT_CERTIFICATION_EVIDENCE"
    ):
        issues.append("manifest does not preserve PR #125 candidate bytes as pinned historical evidence")

    predecessor_entries = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.72.md": ("OPEN_WORK_V1_2_72", "1.2.72", "1.2.73"),
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.14.md": ("DELIVERY_ATLAS_V0_4_14", "0.4.14", "0.4.15"),
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md": ("FP001_SKELETON_V0_1_16", "0.1.16", "0.1.17"),
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.16.md": ("HARDEN_02_V0_5_16", "0.5.16", "0.5.17"),
    }
    for archived_path, digest in predecessor_archives.items():
        document_id, version, successor_version = predecessor_entries[archived_path]
        predecessor = next((entry for entry in _all_entries(manifest) if entry.get("document_id") == document_id), None)
        if (
            not isinstance(predecessor, dict)
            or _relative_path(predecessor) != archived_path
            or predecessor.get("semver") != version
            or predecessor.get("superseded_version") != successor_version
            or predecessor.get("sha256") != digest
            or predecessor.get("provenance_sha256") != digest
            or predecessor.get("lifecycle") != "historical"
            or predecessor.get("graph_policy") != "frozen_provenance"
        ):
            issues.append(f"manifest does not pin the archived direct predecessor {archived_path}")

    if _fp001_phase8_candidate_route_is_current(manifest):
        archived_status_paths = {
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.16.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        }
        for archive_relative in archived_status_paths:
            expected_hash = protected_current_artifacts.get(archive_relative)
            archived = root / archive_relative
            if not isinstance(expected_hash, str) or not archived.is_file() or sha256_file(archived) != expected_hash:
                issues.append(f"archived Phase 7C status snapshot is missing or changed: {archive_relative}")
            entry = next((item for item in _all_entries(manifest) if _relative_path(item) == archive_relative), None)
            if (
                not isinstance(entry, dict)
                or entry.get("lifecycle") != "historical"
                or entry.get("sha256") != expected_hash
                or entry.get("provenance_sha256") != expected_hash
            ):
                issues.append(f"manifest does not preserve the Phase 7C status snapshot as historical: {archive_relative}")
        for relative, expected_hash in protected_current_artifacts.items():
            if relative in archived_status_paths:
                continue
            path = root / relative
            if not path.is_file() or sha256_file(path) != expected_hash:
                issues.append(f"protected Phase 7C source artifact is missing or changed: {relative}")

        historical_open_work = next(
            (entry for entry in _all_entries(manifest) if _relative_path(entry) == "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md"),
            None,
        )
        if (
            not isinstance(historical_open_work, dict)
            or historical_open_work.get("document_id") != "OPEN_WORK_V1_2_74"
            or historical_open_work.get("semver") != "1.2.74"
            or historical_open_work.get("superseded_version") != "1.2.75"
            or historical_open_work.get("lifecycle") != "historical"
        ):
            issues.append("manifest does not preserve Open Work v1.2.74 as the historical Phase 8 route predecessor")
        _record_check(
            report,
            "fp001_phase7c_final_contract_current_promotion",
            not issues,
            "PR #126 certification evidence and the v1.2.74 Phase 7C status snapshot remain immutable under the TB-001 successor"
            if not issues
            else "; ".join(issues),
            path=candidate_archive_path,
        )
        return

    for relative in current_paths.values():
        if not (root / relative).is_file():
            issues.append(f"current status route is missing: {relative}")
    for relative, expected_hash in protected_current_artifacts.items():
        current = root / relative
        if not current.is_file() or (expected_hash != "PENDING" and sha256_file(current) != expected_hash):
            issues.append(f"protected current Phase 7C status artifact is missing or changed: {relative}")

    graph_rules = integrity_rules.get("graph_rules", {})
    navigation = graph_rules.get("navigation_document_paths", []) if isinstance(graph_rules, dict) else []
    for key, relative in current_paths.items():
        if key != "open_work" and relative not in navigation:
            issues.append(f"manifest navigation omits current status route {relative}")
    for archived_path in predecessor_archives:
        retired_path = archived_path.replace("/archive/", "/working/")
        if retired_path.endswith("02_OPEN_WORK_v1.2.72.md"):
            retired_path = "docs/00_platform/02_OPEN_WORK_v1.2.72.md"
        elif retired_path.endswith("02_OPEN_WORK_v1.2.71.md"):
            retired_path = "docs/00_platform/02_OPEN_WORK_v1.2.71.md"
        elif retired_path.endswith("02_OPEN_WORK_v1.2.70.md"):
            retired_path = "docs/00_platform/02_OPEN_WORK_v1.2.70.md"
        if retired_path in navigation:
            issues.append(f"manifest navigation still routes archived predecessor {retired_path}")
    open_work_entry = next((entry for entry in manifest.get("governing_documents", []) if entry.get("document_id") == "OPEN_WORK"), None)
    if (
        not isinstance(open_work_entry, dict)
        or _relative_path(open_work_entry) != current_paths["open_work"]
        or open_work_entry.get("semver") != "1.2.74"
        or open_work_entry.get("superseded_version") != "1.2.73"
    ):
        issues.append("manifest governing Open Work lineage is not v1.2.73 → v1.2.74")

    contract_path = current_paths["final_feature_pack_contract"]
    current_authorities = [
        entry for entry in _all_entries(manifest)
        if entry.get("lifecycle", "current") != "historical"
    ]
    if any(_relative_path(entry) == contract_path for entry in current_authorities):
        issues.append("Final Feature Pack Contract was incorrectly promoted into root authority")
    contract_file = root / contract_path
    contract = contract_file.read_text(encoding="utf-8") if contract_file.is_file() else ""
    promotion_match = re.search(
        r"<!-- FP001_PHASE7C_CURRENT_STATUS_START -->\s*```json\s*(.*?)\s*```\s*<!-- FP001_PHASE7C_CURRENT_STATUS_END -->",
        contract,
        re.DOTALL,
    )
    try:
        promotion = json.loads(promotion_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if promotion_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        promotion = {}
    expected_promotion = {
        "artifact_version": "v0.1.0",
        "promotion_state": "CURRENT / VERIFIED AFTER PR #126 RESULTING-MAIN PASS",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "contract_lifecycle": "COMPLETE / CERTIFIED / CURRENT",
        "candidate_pr": 125,
        "approved_candidate_head_sha": "bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5",
        "pr125_reviewed_head_sha": "bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5",
        "candidate_tree_sha": "8e5fc724b4c4f4a6a196d41e3beafc8e1384c2bf",
        "pr125_merge_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
        "pr125_merge_second_parent_sha": "bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5",
        "pr125_merge_tree_sha": "8e5fc724b4c4f4a6a196d41e3beafc8e1384c2bf",
        "pr125_resulting_main_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
        "pr125_resulting_main_tree_sha": "8e5fc724b4c4f4a6a196d41e3beafc8e1384c2bf",
        "pr125_candidate_resulting_main_tree_identity": "PASS",
        "independent_exact_head_review": "PASS",
        "pr125_exact_head_fia_run": 39121794222,
        "pr125_exact_head_fia_status": "completed",
        "pr125_exact_head_fia_conclusion": "success",
        "pr125_exact_head_fia_tests": 443,
        "pr125_exact_head_fia_assertions": 698,
        "pr125_exact_head_fia_findings": 0,
        "pr125_resulting_main_fia_run": 39126317950,
        "pr125_resulting_main_fia_status": "completed",
        "pr125_resulting_main_fia_conclusion": "success",
        "pr125_resulting_main_fia_tests": 443,
        "pr125_resulting_main_fia_assertions": 698,
        "pr125_resulting_main_fia_findings": 0,
        "pr126_base_sha": "cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5",
        "pr126_reviewed_head_sha": "e7d5d3908bedf1a75c6627448c3ed0c067b076f8",
        "pr126_merge_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "pr126_reviewed_head_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_merge_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_merge_head_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "pr126_head_merge_tree_identity": "PASS",
        "pr126_exact_head_fia_run": 39141076412,
        "pr126_exact_head_fia_status": "completed",
        "pr126_exact_head_fia_conclusion": "success",
        "resulting_main_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
        "resulting_main_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
        "resulting_main_fia_run": 39143147487,
        "resulting_main_fia_status": "completed",
        "resulting_main_fia_conclusion": "success",
        "resulting_main_fia_tests": 455,
        "resulting_main_fia_assertions": 728,
        "resulting_main_fia_findings": 0,
        "fresh_resulting_main_verification": "PASS",
        "candidate_archive_path": candidate_archive_path,
        "candidate_archive_sha256": candidate_archive_sha256,
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_tracker_issue": 120,
        "phase_7b_tracker_state": "CLOSED / COMPLETED",
        "programme_router_issue": 111,
        "programme_router_state": "OPEN",
        "proof_classification": "NEW_TRACER_BULLET",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "classification_authority_event": "SEPARATE OPEN WORK POST-PHASE-7C STATUS DECISION",
        "phase8": "AUTHORISED",
        "application_implementation": "AUTHORISED",
        "development_entry_hard_stop_condition_9": "SATISFIED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
    }
    if promotion != expected_promotion:
        issues.append("working contract status record is missing, altered or contains a premature lifecycle decision")
    if not contract.startswith(
        "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT\n"
        "COMPLETE\nCERTIFIED\nCURRENT\n\n"
        "NON-IMPLEMENTATION\n\nNOT PROOF CLASSIFICATION\n"
        "NOT PHASE 8 AUTHORITY\nNOT APPLICATION IMPLEMENTATION AUTHORITY\n"
    ):
        issues.append("working Final Feature Pack Contract is not marked COMPLETE / CERTIFIED / CURRENT")
    status_summary = contract.split("## A. Identity and provenance", 1)[0]
    for token in (
        "PHASE 7A: COMPLETE",
        "REQUIRED DOSSIER SET: DISPOSITION-COMPLETE",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "DEVELOPMENT ENTRY HARD STOP CONDITIONS 1–10: SATISFIED",
        "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
    ):
        if token not in status_summary:
            issues.append(f"working contract lifecycle summary omits or contradicts {token!r}")
    if "Closes #124" in contract or "closes #124" in contract:
        issues.append("working contract status record incorrectly tries to close an already closed issue")

    candidate_text = candidate.read_text(encoding="utf-8") if candidate.is_file() else ""
    body_start = "## B. Outcome and validation objective"
    old_end = "## Candidate lifecycle handoff"
    new_end = "## Certification and current-status promotion record"
    old_exit = "Phase 7C exit for this candidate means only that the contract is authored and ready for fresh independent exact-head review. Certification, current-status promotion, proof classification, and Phase 8 entry are separate later gates."
    new_exit = "Phase 7C contract delivery is COMPLETE / CERTIFIED / CURRENT under this separate status successor. The separate downstream classification status is COMPLETE / FINALISED as NEW_TRACER_BULLET; proof execution, Phase 8 entry and application implementation remain gated."
    try:
        candidate_body = candidate_text.split(body_start, 1)[1].split(old_end, 1)[0].replace(old_exit, "<PHASE_7C_EXIT_LIFECYCLE_STATUS>")
        current_body = contract.split(body_start, 1)[1].split(new_end, 1)[0].replace(new_exit, "<PHASE_7C_EXIT_LIFECYCLE_STATUS>")
        if candidate_body != current_body:
            issues.append("substantive Final Feature Pack Contract sections changed during the status-only promotion")
    except IndexError:
        issues.append("contract semantic comparison headings are missing or reordered")

    open_work_path = root / current_paths["open_work"]
    open_work = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() else ""
    state_match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work,
        re.DOTALL,
    )
    try:
        state = json.loads(state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        state = {}
    expected_state = {
        "status_successor_version": "1.2.74",
        "status_successor_base_sha": "675a8c50ac53a995a48e4d262df42065f8ccd412",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "current_stage": "FP-001 PHASE 8 ARCHITECTURAL PROOF (BOUNDED)",
        "next_stage": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "phase_7c_execution_tracker_issue": 124,
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
        "programme_router_issue_111_state": "OPEN",
        "proof_classification": "NEW_TRACER_BULLET",
        "application_implementation": "AUTHORISED",
        "phase8": "AUTHORISED",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
    }
    if any(state.get(key) != value for key, value in expected_state.items()):
        issues.append("Open Work current lifecycle state is missing or contradicts the closed-tracker route")
    contract_state = state.get("phase_7c_final_feature_pack_contract", {})
    if (
        not isinstance(contract_state, dict)
        or contract_state.get("version") != "0.1.0"
        or contract_state.get("lifecycle") != "COMPLETE / CERTIFIED / CURRENT"
        or contract_state.get("proof_classification") != "NEW_TRACER_BULLET"
        or contract_state.get("selected_proof_vehicle") != "NEW_TRACER_BULLET"
        or contract_state.get("reuse_existing_proof") != "NOT SELECTED"
        or contract_state.get("tracer_bullet_id") != "NONE / NOT CREATED"
        or contract_state.get("architectural_proof_execution") != "NOT STARTED"
        or contract_state.get("phase8") != ("AUTHORISED" if "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED" in open_work else "UNAUTHORISED")
        or contract_state.get("candidate_archive_sha256") != candidate_archive_sha256
        or contract_state.get("resulting_main_fia_run") != 39143147487
        or contract_state.get("resulting_main_fia_tests") != 455
        or contract_state.get("resulting_main_fia_assertions") != 728
        or contract_state.get("resulting_main_fia_findings") != 0
        or contract_state.get("fresh_resulting_main_verification") != "PASS"
    ):
        issues.append("Open Work does not route the current contract, hosted evidence and downstream gates")
    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    active_route = open_work[active_start:active_end] if active_start >= 0 and active_end > active_start else ""
    hard_stop_promoted = "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED" in open_work
    for token in (
        "PHASE 7A: COMPLETE",
        "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "#120 CLOSED / COMPLETED",
        "PROGRAMME ROUTER #111: OPEN",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        *(
            (
                "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
                "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
                "DEVELOPMENT ENTRY HARD STOP CONDITIONS 1–10: SATISFIED",
                "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
                "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
                "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET; PHASE 9 VERTICAL SLICES AND BROAD FP-001 IMPLEMENTATION REMAIN UNAUTHORISED",
            )
            if hard_stop_promoted
            else (
                "NEXT GOVERNANCE ACTION: DEVELOPMENT ENTRY HARD STOP EVALUATION",
                "DEVELOPMENT ENTRY HARD STOP CONDITION 9: SATISFIED",
                "REMAINING DEVELOPMENT ENTRY HARD STOP CONDITIONS: NOT EVALUATED / MUST PASS BEFORE PHASE 8",
                "EXECUTABLE DEVELOPMENT: UNAUTHORISED; CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9; ALL OTHER APPLICABLE CONDITIONS REQUIRE INDEPENDENT EVALUATION",
            )
        ),
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET: REQUIRED / NOT YET DEFINED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "39143147487",
        "455 TESTS / 728 ASSERTIONS / 0 FINDINGS",
    ):
        if token not in active_route:
            issues.append(f"Open Work current route omits {token!r}")
    if re.search(r"(?im)^.*#124[^\n]{0,120}\bOPEN\b.*$", active_route):
        issues.append("Open Work current route projects issue #124 as OPEN")
    if "PROOF CLASSIFICATION: NEW_TRACER_BULLET" not in active_route:
        issues.append("Open Work does not record its selected proof vehicle")
    if re.search(r"(?im)^\s*REUSE_EXISTING_PROOF\s*:\s*SELECTED\b", active_route):
        issues.append("Open Work selects REUSE_EXISTING_PROOF")
    if re.search(r"(?im)^\s*PHASE 8\s*:\s*AUTHORI[ZS]ED\s*$", active_route):
        issues.append("Open Work authorises Phase 8 without bounded architectural-proof scope")
    if re.search(r"(?im)^\s*APPLICATION IMPLEMENTATION\s*:\s*AUTHORI[ZS]ED\s*$", active_route):
        issues.append("Open Work authorises application implementation without bounded Phase 8 scope")

    readme_path = root / "docs/00_platform/README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    current_state = _markdown_h2_section(readme, "Current State") or ""
    for token in (
        "PHASE 7A: COMPLETE",
        "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "PROGRAMME ROUTER #111: OPEN",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "39143147487",
        "455 tests / 728 FIA assertions / 0 findings",
    ):
        if token not in current_state:
            issues.append(f"README current state omits {token!r}")
    for route_path in current_paths.values():
        if Path(route_path).name not in readme:
            issues.append(f"README does not route current artifact {route_path}")
    if re.search(r"(?im)^.*#124[^\n]{0,120}\bOPEN\b.*$", current_state):
        issues.append("README current state projects issue #124 as OPEN")
    if "PROOF CLASSIFICATION: NEW_TRACER_BULLET" not in current_state:
        issues.append("README current state does not record the selected proof vehicle")
    if re.search(r"(?im)^\s*REUSE_EXISTING_PROOF\s*:\s*SELECTED\b", current_state):
        issues.append("README current state selects REUSE_EXISTING_PROOF")
    if (
        re.search(r"(?im)^\s*PHASE 8\s*:\s*AUTHORI[ZS]ED\s*$", current_state)
        or re.search(r"(?im)^\s*APPLICATION IMPLEMENTATION\s*:\s*AUTHORI[ZS]ED\s*$", current_state)
    ):
        issues.append("README current state authorises Phase 8 or application implementation without bounded scope")

    active_artifacts = _markdown_h2_section(readme, "Active Working Artifacts") or ""
    current_route_sections = [("README current state", current_state), ("README active artifacts", active_artifacts), ("Open Work", active_route)]
    route_sections = {
        "delivery_atlas": "## 26.22 FP-001 Development Entry Hard Stop PASS current route",
        "fp001_skeleton": "## v0.1.18",
        "harden_02": "## 25. FP-001 architectural proof classification current status",
    }
    for key, heading in route_sections.items():
        path = root / current_paths[key]
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        if heading in text:
            route = text.split(heading, 1)[1].split("\n## ", 1)[0]
            current_route_sections.append((key, route))
    retired_paths = graph_rules.get("retired_current_predecessor_paths", []) if isinstance(graph_rules, dict) else []
    guard_note = graph_rules.get("stale_predecessor_current_path_guard_note", "") if isinstance(graph_rules, dict) else ""
    if (
        "The separate PR #119 Audit v0.1.0 current-status promotion" not in guard_note
        or "the exact PR #118 candidate is pinned as historical certification evidence" not in guard_note
    ):
        issues.append("manifest Audit promotion guard note must distinguish PR #119 promotion from PR #118 candidate")
    for relative in retired_paths:
        name = Path(relative).name
        unqualified = re.compile(r"(?<!archive/)" + re.escape(name))
        for label, route in current_route_sections:
            if unqualified.search(route):
                issues.append(f"{label} routes retired predecessor without archive qualification: {name}")

    for key in ("delivery_atlas", "fp001_skeleton", "harden_02"):
        path = root / current_paths[key]
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        if "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED" not in text:
            issues.append(f"current {key} does not state the closed Phase 7C tracker")
        if "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED" not in text:
            issues.append(f"current {key} omits the next governance action")
        if "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET" not in text:
            issues.append(f"current {key} omits the selected proof classification")
        if hard_stop_promoted:
            if "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)" not in text or "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)" not in text:
                issues.append(f"current {key} omits bounded Phase 8 authorisation")
        elif "PHASE 8: UNAUTHORISED" not in text or "APPLICATION IMPLEMENTATION: UNAUTHORISED" not in text:
            issues.append(f"current {key} authorises or omits the Phase 8 gate")
        if re.search(r"(?im)^.*#124[^\n]{0,120}\bOPEN\b.*$", text.split("\n## ", 1)[0]):
            issues.append(f"current {key} route projects issue #124 as OPEN")

    skeleton = root / current_paths["fp001_skeleton"]
    predecessor_skeleton = root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md"
    pmr_start = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:START -->"
    pmr_end = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:END -->"
    def marked_pmr(path: Path) -> str:
        if not path.is_file():
            return ""
        text = path.read_text(encoding="utf-8")
        if text.count(pmr_start) != 1 or text.count(pmr_end) != 1:
            return ""
        left, right = text.index(pmr_start), text.index(pmr_end)
        return text[left:right + len(pmr_end)] if left < right else ""
    if not marked_pmr(predecessor_skeleton) or marked_pmr(skeleton) != marked_pmr(predecessor_skeleton):
        issues.append("current skeleton changed or lost the certified PMR contract block")
    skeleton_text = skeleton.read_text(encoding="utf-8") if skeleton.is_file() else ""
    if "The six affected Domains and seven material capability relationships remain unchanged." not in skeleton_text:
        issues.append("current skeleton omits the preserved six-Domain and seven-capability scope")
    if "Phase 7B reconciliation v0.1.0 is COMPLETE / CERTIFIED / CURRENT" not in skeleton_text:
        issues.append("current skeleton does not preserve the certified Phase 7B route")

    open_work_text = open_work
    if "after this status successor merges" in active_route.casefold() or "after the separate status successor merges" in active_route.casefold():
        issues.append("Open Work current route retains stale status-successor transition wording")
    if "#124 OPEN through promotion merge" in current_state:
        issues.append("README current route retains stale tracker-open-through-verification wording")

    _record_check(
        report,
        "fp001_phase7c_final_contract_current_promotion",
        not issues,
        "PR #126 provenance, resulting-main counts, tracker closure, status routes and downstream gates are pinned"
        if not issues
        else "; ".join(issues),
        path=current_paths["final_feature_pack_contract"],
    )

def _check_fp001_phase7b_certification_current(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Pin the exact reviewed candidate and fail closed on the certified current route."""

    docs = root / "docs" / "00_platform"
    candidate_path = "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
    current_path = "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
    candidate = root / candidate_path
    current = root / current_path
    expected_hash = "274306e73e2450806516a5b76ca96f1a768af7824ba823cca6c9371c58e65401"
    archives = integrity_rules.get("fp001_phase7b_reconciliation_certification_archives", {})
    archive_issues: list[str] = []
    required_archives = {
        candidate_path: expected_hash,
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.66.md": "96a61dd94098f3c9fbb4ba1a6c683e9a3484b62ee15306d8dd5d884ad84f2133",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.8.md": "e92f94d390cbf58173231daaedea00a0fac2a6d67fb69a0a7f6edab0e487af4e",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md": "5d1332286bd8c9d7e86838f91b22edbf2e72afca1d8fb59edd28103e165c019b",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.10.md": "dad16d39906afede052e3cc94bb4c39568a1fe14215bb0b7b52e0e234b106f42",
    }
    if not isinstance(archives, dict) or archives != required_archives:
        archive_issues.append("manifest archive-integrity bundle does not pin exactly the candidate and four immediate predecessors")
    for relative, digest in required_archives.items():
        path = root / relative
        if not path.is_file():
            archive_issues.append(f"required Phase 7B certification archive is missing: {relative}")
        elif sha256_file(path) != digest:
            archive_issues.append(f"Phase 7B certification archive hash drifted: {relative}")
    candidate_rule = integrity_rules.get("fp001_phase7b_reconciliation_candidate", {})
    if not isinstance(candidate_rule, dict) or candidate_rule.get("path") != candidate_path:
        archive_issues.append("manifest candidate path no longer identifies the immutable archive")
    historical_candidate = next(
        (
            entry
            for entry in _all_entries(manifest)
            if entry.get("document_id") == "FP001_PHASE_7B_RECONCILIATION_PR_121_CANDIDATE"
        ),
        None,
    )
    if (
        not isinstance(historical_candidate, dict)
        or _relative_path(historical_candidate) != candidate_path
        or historical_candidate.get("sha256") != expected_hash
        or historical_candidate.get("provenance_sha256") != expected_hash
        or historical_candidate.get("lifecycle") != "historical"
    ):
        archive_issues.append("manifest historical PR #121 candidate evidence is missing or contradictory")
    _record_check(
        report,
        "fp001_phase7b_certification_archive_integrity",
        not archive_issues,
        "immutable PR #121 candidate and all four direct predecessors match their pinned bytes"
        if not archive_issues
        else "; ".join(archive_issues),
        path=candidate_path,
    )

    closure_archives = integrity_rules.get("fp001_phase7b_tracker_closure_sync_archives", {})
    expected_closure_archives = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.67.md": "23f1236ec32a59f740db751e4d2dbd5d10e92849ea2730b5b284a80b44a07bb0",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.9.md": "45382afcf906f1e63a4769d0a02726343df3128e868c5af859f91b9f05502a41",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.11.md": "8a9167326a6198d1820425cf7e2ebcf1f6cd851d3a31cb7d9291355274945089",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.11.md": "bd96505d4060ecc5d7e06bb033e527dd93114577ea4ac1de4051faeec50f395c",
    }
    closure_archive_issues: list[str] = []
    if closure_archives != expected_closure_archives:
        closure_archive_issues.append("manifest tracker-closure archive pins are missing, substituted or incorrect")
    for relative, digest in expected_closure_archives.items():
        archived = root / relative
        if not archived.is_file() or sha256_file(archived) != digest:
            closure_archive_issues.append(f"tracker-closure predecessor archive is missing or changed: {relative}")
    predecessor_open_work = next(
        (entry for entry in _all_entries(manifest) if entry.get("document_id") == "OPEN_WORK_V1_2_67"),
        None,
    )
    predecessor_digest = expected_closure_archives["docs/00_platform/archive/02_OPEN_WORK_v1.2.67.md"]
    if (
        not isinstance(predecessor_open_work, dict)
        or _relative_path(predecessor_open_work) != "docs/00_platform/archive/02_OPEN_WORK_v1.2.67.md"
        or predecessor_open_work.get("semver") != "1.2.67"
        or predecessor_open_work.get("authority_class") != "PLANNING_TRACKER_HISTORICAL"
        or predecessor_open_work.get("superseded_version") != "1.2.68"
        or predecessor_open_work.get("lifecycle") != "historical"
        or predecessor_open_work.get("sha256") != predecessor_digest
        or predecessor_open_work.get("provenance_sha256") != predecessor_digest
    ):
        closure_archive_issues.append("manifest does not correctly register archived Open Work v1.2.67")
    _record_check(
        report,
        "fp001_phase7b_tracker_closure_sync_archives",
        not closure_archive_issues,
        "four direct predecessors are archived byte-identically and Open Work v1.2.67 is manifest-pinned"
        if not closure_archive_issues
        else "; ".join(closure_archive_issues),
        path="docs/00_platform/archive/02_OPEN_WORK_v1.2.67.md",
    )

    issues: list[str] = []
    candidate_text = candidate.read_text(encoding="utf-8") if candidate.is_file() else ""
    current_text = current.read_text(encoding="utf-8") if current.is_file() else ""
    if not current_text:
        issues.append("current reconciliation status successor is missing")

    open_work_entry_early = next(
        (
            entry
            for entry in _all_entries(manifest)
            if entry.get("document_id") == "OPEN_WORK" and entry.get("lifecycle", "current") != "historical"
        ),
        None,
    )
    open_work_path_early = root / _relative_path(open_work_entry_early) if open_work_entry_early else None
    open_work = (
        open_work_path_early.read_text(encoding="utf-8")
        if open_work_path_early and open_work_path_early.is_file()
        else ""
    )
    hard_stop_promoted = "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED" in open_work
    if _fp001_phase8_candidate_route_is_current(manifest):
        issues = _check_fp001_pmr_reconciliation_after_phase7c_promotion(root, manifest, integrity_rules)
        _record_check(
            report,
            "fp001_phase7b_certification_current",
            not issues,
            "archived Phase 7B certification, its current reconciliation source and the Phase 8 TB-001 candidate route remain pinned"
            if not issues
            else "; ".join(issues),
            path=candidate_path,
        )
        return

    readme_path = docs / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    readme_current = _markdown_h2_section(readme_text, "Current State")
    if readme_current is None:
        issues.append("README current state section is missing")
        readme_current = ""
    else:
        readme_routes = (
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
            "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
            "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
            "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
            "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
            *(
                (
                    "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
                    "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
                    "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
                )
                if hard_stop_promoted
                else ("PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",)
            ),
        )
        for route in readme_routes:
            if route not in readme_current:
                issues.append(f"README current state omits required lifecycle route {route!r}")
        if TRACKER_120_OPEN_PROJECTION_PATTERN.search(readme_current):
            issues.append("README current/active routing still projects tracker #120 as open")
        if not re.search(r"(?i)#120[^\n]{0,100}CLOSED / COMPLETED", readme_current):
            issues.append("README current/active routing omits tracker #120 completion")

        blocked_phase7c = re.compile(
            r"\bphase\s+7c\b[^.!?\n]{0,100}\bblocked\b[^.!?\n]{0,40}\bnot[\s/_-]*started\b",
            re.IGNORECASE,
        )
        for paragraph in re.split(r"\n\s*\n", readme_current):
            for sentence in re.split(r"(?<=[.!?])\s+", paragraph):
                match = blocked_phase7c.search(sentence)
                if match is None:
                    continue
                issues.append(
                    "README current state contains a BLOCKED / NOT_STARTED Phase 7C statement"
                )
                break
    readme_active = _markdown_h2_section(readme_text, "Active Working Artifacts")
    if readme_active is None:
        issues.append("README active working artifacts section is missing")
    elif (
        TRACKER_120_OPEN_PROJECTION_PATTERN.search(readme_active)
        or "CLOSED / COMPLETED" not in readme_active
        or "tracker #120" not in readme_active
    ):
        issues.append("README active-artifact routing does not project tracker #120 as CLOSED / COMPLETED")
    required_status = (
        "FP-001 PHASE 7B RECONCILIATION\nCOMPLETE\nCERTIFIED\nCURRENT",
        "NON-IMPLEMENTATION",
        "NOT PHASE 7C",
        "NOT DEVELOPMENT-ENTRY AUTHORITY",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "RECONCILIATION v0.1.0: CERTIFIED / CURRENT",
        "PHASE 7C: NEXT / NOT_STARTED",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
        "Fresh independent post-merge review: PASS",
        "reviewer inspected and revalidated repository-hosted evidence",
        "did not claim to have executed CI personally",
    )
    for token in required_status:
        if token not in current_text:
            issues.append(f"current reconciliation successor omits required lifecycle/evidence token: {token}")
    current_header = current_text.split("## 1. Baseline and authority set", 1)[0]
    tracker_header_lines = re.findall(r"(?m)^\*\*Execution tracker:\*\*[^\n]*$", current_header)
    if (
        len(tracker_header_lines) != 1
        or "issue [#120]" not in tracker_header_lines[0]
        or "CLOSED / COMPLETED" not in tracker_header_lines[0]
        or "Phase 7B execution/control history" not in tracker_header_lines[0]
        or TRACKER_120_OPEN_PROJECTION_PATTERN.search(tracker_header_lines[0])
    ):
        issues.append("current reconciliation status header does not record issue #120 as CLOSED / COMPLETED")
    for token in (
        "b6f82218026f3372ccacc96ffdbb37430e8e503f",
        "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
        "f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3",
        "98e553d45006136277e4b2aa629c97c31f7742e2",
        expected_hash,
        "39035622705",
        "39041010709",
        "6235094794",
        "6235345322",
    ):
        if token not in current_text:
            issues.append(f"current reconciliation successor omits certification evidence {token}")
    section_start = "## 3. Reconciliation method and terms"
    section_end = "## 8. Candidate result and certification boundary"
    if not candidate_text or not current_text or section_start not in candidate_text or section_start not in current_text or section_end not in candidate_text or section_end not in current_text:
        issues.append("immutable candidate or current successor is missing substantive reconciliation sections")
    else:
        candidate_body = candidate_text.split(section_start, 1)[1].split(section_end, 1)[0]
        current_body = current_text.split(section_start, 1)[1].split(section_end, 1)[0]
        if candidate_body != current_body:
            issues.append("current successor changes the exact reviewed substantive reconciliation body")
    if _fp001_phase7b_candidate_text_issues(candidate_text, candidate_rule if isinstance(candidate_rule, dict) else {}):
        issues.append("archived candidate no longer passes the 15-pair seam matrix and zero-blocker checks")
    if current_text.count("BLOCKING_AUTHORITY_GAP: NONE") != 1 or current_text.count("BLOCKING_DOSSIER_CONTRADICTION: NONE") != 1:
        issues.append("current reconciliation does not preserve both zero-blocker conclusions exactly once")

    open_work_entry = next(
        (
            entry
            for entry in _all_entries(manifest)
            if entry.get("document_id") == "OPEN_WORK" and entry.get("lifecycle", "current") != "historical"
        ),
        None,
    )
    open_work_path = root / _relative_path(open_work_entry) if open_work_entry else None
    open_work = open_work_path.read_text(encoding="utf-8") if open_work_path and open_work_path.is_file() else ""
    match = re.search(
        r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
        open_work,
        re.DOTALL,
    )
    try:
        state = json.loads(match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        state = {}
    certification = state.get("phase_7b_reconciliation_certification", {})
    exact_certification = {
        "pr_121_url": "https://github.com/JCSchoeman96/NewYou/pull/121",
        "candidate_head": "b6f82218026f3372ccacc96ffdbb37430e8e503f",
        "pre_candidate_main": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
        "resulting_main": "f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3",
        "merge_parents": [
            "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
            "b6f82218026f3372ccacc96ffdbb37430e8e503f",
        ],
        "candidate_resulting_main_tree": "98e553d45006136277e4b2aa629c97c31f7742e2",
        "archived_candidate_path": candidate_path,
        "archived_candidate_sha256": expected_hash,
        "exact_head_run": "39035622705",
        "exact_head_result": "PASS",
        "resulting_main_run": "39041010709",
        "resulting_main_result": "PASS",
        "exact_head_tests": "397 PASS",
        "resulting_main_tests": "397 PASS",
        "exact_head_foundation_integrity": {"assertions": 646, "result": "PASS", "findings": 0},
        "resulting_main_foundation_integrity": {"assertions": 646, "result": "PASS", "findings": 0},
        "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/121#issuecomment-6235094794",
        "post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/121#issuecomment-6235345322",
        "post_merge_independent_review": "PASS",
        "reviewer": "ChatGPT / GPT-5.6 Sol",
        "poster": "JCSchoeman96",
        "reviewer_revalidated_repository_hosted_evidence": True,
        "reviewer_executed_ci_personally": False,
        "issue_120_state_while_status_successor_pr_unmerged": "OPEN",
        "issue_120_closure": "CLOSED / COMPLETED BY PR #122 STATUS-SUCCESSOR MERGE",
        "pr_122_status_successor": {
            "url": "https://github.com/JCSchoeman96/NewYou/pull/122",
            "reviewed_head": "5f0747b766b76df24d764f88774cf73315e61c01",
            "merge_commit": "3f4c9bf564b2b011e96171b8664428423eeba558",
            "merge_tree": "c7a505dbf05e707f1bf256394f59f27cc537d8ce",
            "merge_parents": [
                "f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3",
                "5f0747b766b76df24d764f88774cf73315e61c01",
            ],
            "issue_120_state_after_merge": "CLOSED / COMPLETED",
            "resulting_main_run": "39097918329",
            "resulting_main_result": "PASS",
            "resulting_main_tests": "406 PASS",
            "resulting_main_foundation_integrity": {"assertions": 660, "result": "PASS", "findings": 0},
            "exact_head_guard": "SKIPPED (resulting-main workflow)",
        },
    }
    if certification != exact_certification:
        issues.append("current Open Work is missing or contradicts exact PR #121 post-merge certification evidence")
    expected_state = (
        {
            "status_successor_version": "1.2.74",
            "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
            "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
            "current_stage": "FP-001 PHASE 8 ARCHITECTURAL PROOF (BOUNDED)",
            "phase_7c_execution_tracker_issue": 124,
            "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
            "programme_router_issue_111_state": "OPEN",
            "next_stage": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
            "proof_classification": "NEW_TRACER_BULLET",
            "architectural_proof_classification_status": "COMPLETE / FINALISED",
            "selected_proof_vehicle": "NEW_TRACER_BULLET",
            "reuse_existing_proof": "NOT SELECTED",
            "tracer_bullet": "REQUIRED / NOT YET DEFINED",
            "tracer_bullet_id": "NONE / NOT CREATED",
            "architectural_proof_execution": "NOT STARTED",
            "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
            "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
            "application_implementation": "AUTHORISED",
            "phase8": "AUTHORISED",
            "next_governance_action": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
            "phase_7b_reconciliation_execution_tracker_issue": 120,
            "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
            "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
            "conditional_dossiers": {
                "privacy_consent": "NOT_REQUIRED",
                "content_media": "NOT_REQUIRED",
                "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
                "analytics": "NOT_REQUIRED",
            },
        }
        if hard_stop_promoted
        else {
            "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
            "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
            "phase_7c_execution_tracker_issue": 124,
            "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
            "programme_router_issue_111_state": "OPEN",
            "next_stage": "DEVELOPMENT ENTRY HARD STOP EVALUATION",
            "proof_classification": "NEW_TRACER_BULLET",
            "architectural_proof_classification_status": "COMPLETE / FINALISED",
            "selected_proof_vehicle": "NEW_TRACER_BULLET",
            "development_entry_hard_stop_condition_9": "SATISFIED",
            "remaining_development_entry_hard_stop_conditions": "NOT EVALUATED / MUST PASS BEFORE PHASE 8",
            "application_implementation": "UNAUTHORISED / BLOCKED UNTIL ALL DEVELOPMENT ENTRY HARD STOP CONDITIONS PASS",
            "phase_7b_reconciliation_execution_tracker_issue": 120,
            "phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED",
            "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
            "conditional_dossiers": {
                "privacy_consent": "NOT_REQUIRED",
                "content_media": "NOT_REQUIRED",
                "audit_evidence": "REQUIRED / COMPLETE / CERTIFIED / CURRENT",
                "analytics": "NOT_REQUIRED",
            },
        }
    )
    for key, expected in expected_state.items():
        if state.get(key) != expected:
            issues.append(f"current Open Work lifecycle state {key!r} is missing or contradictory")
    phase7c_state = state.get("phase_7c_final_feature_pack_contract", {})
    if not isinstance(phase7c_state, dict) or any(
        phase7c_state.get(key) != value
        for key, value in {
            "path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
            "version": "0.1.0",
            "lifecycle": "COMPLETE / CERTIFIED / CURRENT",
            "candidate_archive_sha256": "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19",
            "pr125_exact_head_fia_run": 39121794222,
            "pr125_resulting_main_fia_run": 39126317950,
            "pr126_reviewed_head_sha": "e7d5d3908bedf1a75c6627448c3ed0c067b076f8",
            "pr126_merge_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
            "pr126_merge_tree_sha": "f5586314db6c3addab6482e866b8d781faba75bc",
            "pr126_exact_head_fia_run": 39141076412,
            "resulting_main_sha": "69bef7bb2782cbff00a48505504ebd2686eb53d9",
            "resulting_main_fia_run": 39143147487,
            "resulting_main_fia_status": "completed",
            "resulting_main_fia_conclusion": "success",
            "resulting_main_fia_tests": 455,
            "resulting_main_fia_assertions": 728,
            "resulting_main_fia_findings": 0,
            "fresh_resulting_main_verification": "PASS",
            "tracker_124_state": "CLOSED / COMPLETED",
            "proof_classification": "NEW_TRACER_BULLET",
            "phase8": "AUTHORISED" if hard_stop_promoted else "UNAUTHORISED",
        }.items()
    ):
        issues.append("current Open Work Phase 7C contract provenance is missing or contradictory")
    expected_candidate_state = {
        "path": candidate_path,
        "current_status_successor_path": current_path,
        "version": "0.1.0",
        "result": "PASS / READY FOR INDEPENDENT REVIEW",
        "lifecycle": "CERTIFIED / CURRENT",
        "certification": "COMPLETE; EXACT CANDIDATE MERGED UNCHANGED; RESULTING-MAIN VERIFIED",
        "tracker_issue": 120,
    }
    if state.get("phase_7b_reconciliation_candidate") != expected_candidate_state:
        issues.append("Open Work does not separate the immutable candidate from its current status successor")
    if state.get("current_delivery_atlas") != "working/DELIVERY_ATLAS_WORKING_v0.4.16.md" or state.get("current_fp001_skeleton") != "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md" or state.get("current_harden_02") != "working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md":
        issues.append("Open Work current Atlas, Skeleton or HARDEN successor route is stale")
    if (
        not isinstance(open_work_entry, dict)
        or _relative_path(open_work_entry) != "docs/00_platform/02_OPEN_WORK_v1.2.74.md"
        or open_work_entry.get("semver") != "1.2.74"
        or open_work_entry.get("superseded_version") != "1.2.73"
    ):
        issues.append("Open Work current manifest lineage is not v1.2.73 → v1.2.74")
    predecessor = next(
        (entry for entry in _all_entries(manifest) if entry.get("document_id") == "OPEN_WORK_V1_2_67"),
        None,
    )
    predecessor_hash = expected_closure_archives["docs/00_platform/archive/02_OPEN_WORK_v1.2.67.md"]
    if (
        not isinstance(predecessor, dict)
        or _relative_path(predecessor) != "docs/00_platform/archive/02_OPEN_WORK_v1.2.67.md"
        or predecessor.get("semver") != "1.2.67"
        or predecessor.get("authority_class") != "PLANNING_TRACKER_HISTORICAL"
        or predecessor.get("superseded_version") != "1.2.68"
        or predecessor.get("lifecycle") != "historical"
        or predecessor.get("sha256") != predecessor_hash
        or predecessor.get("provenance_sha256") != predecessor_hash
    ):
        issues.append("historical Open Work v1.2.67 manifest lineage or archive hash is invalid")
    if hard_stop_promoted:
        if "PHASE 7C: COMPLETE / CERTIFIED / CURRENT" not in open_work or "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET" not in open_work:
            issues.append("current Open Work route loses Phase 7C completion or bounded Phase 8 authorisation")
    elif "PHASE 7C: COMPLETE / CERTIFIED / CURRENT" not in open_work or "EXECUTABLE DEVELOPMENT: UNAUTHORISED" not in open_work:
        issues.append("current Open Work route loses Phase 7C completion or implementation stop")
    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    active = open_work[active_start:active_end] if active_start >= 0 and active_end > active_start else ""
    active_summary = active.split("<!-- HARDEN_02_LIFECYCLE_STATE_START -->", 1)[0]
    required_active_routes = (
        "RECONCILIATION v0.1.0: CERTIFIED / CURRENT",
        "RECONCILIATION EXECUTION TRACKER: #120 CLOSED / COMPLETED",
        *(
            (
                "NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
                "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
                "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET; PHASE 9 VERTICAL SLICES AND BROAD FP-001 IMPLEMENTATION REMAIN UNAUTHORISED",
            )
            if hard_stop_promoted
            else (
                "NEXT GOVERNANCE ACTION: DEVELOPMENT ENTRY HARD STOP EVALUATION",
                "EXECUTABLE DEVELOPMENT: UNAUTHORISED; CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9; ALL OTHER APPLICABLE CONDITIONS REQUIRE INDEPENDENT EVALUATION",
            )
        ),
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "PHASE 7C FINAL FEATURE PACK CONTRACT: `working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md`; v0.1.0 COMPLETE / CERTIFIED / CURRENT",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
    )
    for route in required_active_routes:
        if active_summary.count(route) != 1:
            issues.append(f"current Open Work active route omits or duplicates {route!r}")
    if "PROGRAMME ROUTER #111: OPEN" not in active or TRACKER_120_OPEN_PROJECTION_PATTERN.search(active):
        issues.append("current Open Work active tracker routing is stale or contradicts issue #120 closure")
    if len(re.findall(r"(?m)^PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT\s*$", active)) != 1:
        issues.append("current Open Work active route omits or duplicates the completed Phase 7B reconciliation status")
    if re.search(r"(?im)^PHASE 7B RECONCILIATION\s*:\s*(?:IN PROGRESS|NEXT / NOT_STARTED|STARTED).*$", active):
        issues.append("current Open Work active route leaves completed Phase 7B incomplete")
    for route in (
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        *(
            (
                "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET; PHASE 9 VERTICAL SLICES AND BROAD FP-001 IMPLEMENTATION REMAIN UNAUTHORISED",
            )
            if hard_stop_promoted
            else (
                "EXECUTABLE DEVELOPMENT: UNAUTHORISED; CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9; ALL OTHER APPLICABLE CONDITIONS REQUIRE INDEPENDENT EVALUATION",
            )
        ),
    ):
        if len(re.findall(r"(?m)^" + re.escape(route) + r"\s*$", active_summary)) != 1:
            issues.append(f"current Open Work active route omits or duplicates {route!r}")
    if re.search(r"(?im)^.*PHASE 7C\s*:\s*AUTHORI[ZS]ED.*$", active):
        issues.append("current Open Work active route authorises Phase 7C")
    if "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED" not in active or "PROOF CLASSIFICATION: NEW_TRACER_BULLET" not in active:
        issues.append("current Open Work active route does not carry the finalised selected proof classification")
    if not hard_stop_promoted and re.search(
        r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$",
        active,
    ):
        issues.append("current Open Work active route authorises Phase 8 or application implementation")
    _record_check(
        report,
        "fp001_phase7b_certification_current",
        not issues,
        "exact PR #121 candidate evidence, certified Phase 7B current status and closed downstream gates are preserved"
        if not issues
        else "; ".join(issues),
        path=current_path,
    )


def _check_fp001_pmr_reconciliation_after_phase7c_promotion(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
) -> list[str]:
    """Preserve the certified PMR and Phase 7B evidence through tracker closure."""

    issues: list[str] = []
    promotion = integrity_rules.get("fp001_phase7c_final_contract_current_promotion", {})
    phase7b = integrity_rules.get("fp001_phase7b_reconciliation_candidate", {})
    if not isinstance(promotion, dict) or not isinstance(phase7b, dict):
        return ["manifest Phase 7C promotion or Phase 7B baseline rules are missing"]
    if _fp001_phase8_candidate_route_is_current(manifest):
        phase8 = integrity_rules.get("fp001_phase8_proof_contract_lifecycle", {})
        if not isinstance(phase8, dict):
            return ["manifest Phase 8 proof-contract lifecycle rule is missing"]
        previous_routes = {
            "open_work": "docs/00_platform/archive/02_OPEN_WORK_v1.2.74.md",
            "delivery_atlas": "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.16.md",
            "fp001_skeleton": "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
            "harden_02": "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        }
        previous_hashes = phase8.get("predecessor_archives_sha256", {})
        for relative, digest in previous_hashes.items() if isinstance(previous_hashes, dict) else ():
            path = root / relative
            if not path.is_file() or sha256_file(path) != digest:
                issues.append(f"Phase 8 predecessor archive is missing or changed: {relative}")
        for relative in previous_routes.values():
            if relative not in previous_hashes:
                issues.append(f"Phase 8 route does not pin its archived predecessor: {relative}")

        frozen_sources = phase8.get("frozen_source_sha256", {})
        if not isinstance(frozen_sources, dict):
            issues.append("Phase 8 frozen-source hash map is malformed")
            frozen_sources = {}
        for relative, digest in frozen_sources.items():
            path = root / relative
            if not path.is_file() or sha256_file(path) != digest:
                issues.append(f"certified Phase 7B source changed from the proof-contract baseline: {relative}")

        skeleton = root / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md"
        predecessor_skeleton = root / previous_routes["fp001_skeleton"]
        marker_start = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:START -->"
        marker_end = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:END -->"

        def marked_pmr(path: Path) -> str:
            if not path.is_file():
                return ""
            text = path.read_text(encoding="utf-8")
            if text.count(marker_start) != 1 or text.count(marker_end) != 1:
                return ""
            left, right = text.index(marker_start), text.index(marker_end)
            return text[left : right + len(marker_end)] if left < right else ""

        if not marked_pmr(predecessor_skeleton) or marked_pmr(skeleton) != marked_pmr(predecessor_skeleton):
            issues.append("current skeleton changed or lost the certified PR #67 PMR contract block")
        skeleton_text = skeleton.read_text(encoding="utf-8") if skeleton.is_file() else ""
        if "The six affected Domains and seven material capability relationships remain unchanged." not in skeleton_text:
            issues.append("current skeleton omits the preserved six-Domain and seven-capability scope")
        if "Phase 7B reconciliation v0.1.0 is COMPLETE / CERTIFIED / CURRENT" not in skeleton_text:
            issues.append("current skeleton does not preserve the certified Phase 7B route")
        active_skeletons = sorted(
            path
            for path in (root / "docs/00_platform/working").rglob("FP-001_FEATURE_PACK_SKELETON_WORKING_v*.md")
            if "archive" not in path.parts
        )
        if active_skeletons != [skeleton]:
            issues.append("exactly one current FP-001 skeleton v0.1.21 is required")

        current_open_work = root / "docs/00_platform/02_OPEN_WORK_v1.2.77.md"
        open_work = current_open_work.read_text(encoding="utf-8") if current_open_work.is_file() else ""
        if "working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md" not in open_work:
            issues.append("current Open Work does not route the TB-001 proof-contract candidate")
        for token in (
            "PROOF EXECUTION: NOT STARTED",
            "PROOF RESULT: NOT STARTED",
            "PROOF CERTIFICATION: NOT STARTED",
            "PHASE 9 / VERTICAL SLICES: NOT STARTED / NOT AUTHORISED",
        ):
            if token not in open_work:
                issues.append(f"current Open Work does not preserve {token!r}")

        # The Phase 8 route supersedes only the active task-definition/status route.
        # Keep earlier certified-source and historical-evidence checks in force.
        issues.extend(_fp001_protected_historical_evidence_issues(root, promotion, integrity_rules))
        dossier_files = {
            "Identity & Access": "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
            "Communications": "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
            "Audit & Evidence": "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        }
        dossier_hashes = phase7b.get("dossier_sha256", {})
        for name, relative in dossier_files.items():
            path = root / relative
            expected = dossier_hashes.get(name) if isinstance(dossier_hashes, dict) else None
            if not path.is_file() or not isinstance(expected, str) or sha256_file(path) != expected:
                issues.append(f"certified {name} dossier changed from its Phase 7B baseline")
                if name == "Identity & Access":
                    issues.append("Identity current lifecycle or semantic body changed from its certified Phase 7B baseline")

        identity_path = root / dossier_files["Identity & Access"]
        identity_text = identity_path.read_text(encoding="utf-8") if identity_path.is_file() else ""
        identity_headings = list(re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*#*\s*$", identity_text))
        history_headings = [
            heading for heading in identity_headings
            if heading.group(1) == "###" and heading.group(2) == "Inherited v0.1.3 certification evidence"
        ]
        baseline_headings = [
            heading for heading in identity_headings
            if heading.group(1) == "##" and heading.group(2) == "A. Baseline and scope"
        ]
        if (
            len(history_headings) != 1
            or len(baseline_headings) != 1
            or history_headings[0].start() >= baseline_headings[0].start()
        ):
            issues.append("active Identity lifecycle evidence boundaries are missing, duplicated or malformed")

        active_identity_dossiers = sorted(
            path
            for path in (root / "docs/00_platform/working").rglob("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v*.md")
            if "archive" not in path.parts
        )
        if active_identity_dossiers != [identity_path]:
            issues.append("exactly one active certified/current Identity dossier v0.1.4 is required; stale candidates or extra versions remain active")

        active_audit_dossiers = sorted(
            path
            for path in (root / "docs/00_platform").rglob("*.md")
            if "working" in path.parts
            and "archive" not in path.parts
            and path.name.upper().startswith("FP-001")
            and "AUDIT" in path.name.upper()
            and "DOSSIER" in path.name.upper()
        )
        if active_audit_dossiers != [root / dossier_files["Audit & Evidence"]]:
            issues.append("only the current FP-001 Audit dossier v0.1.0 status successor may exist outside archive")
        return issues

    current_paths = promotion.get("current_paths", {})
    expected_current_paths = {
        "open_work": "docs/00_platform/02_OPEN_WORK_v1.2.74.md",
        "delivery_atlas": "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
        "fp001_skeleton": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
        "harden_02": "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        "final_feature_pack_contract": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
    }
    if current_paths != expected_current_paths:
        issues.append("manifest current Phase 7C route omits or substitutes a status successor")
    current_documents = {key: root / path for key, path in expected_current_paths.items()}
    for key, path in current_documents.items():
        if not path.is_file():
            issues.append(f"current Phase 7C promotion artifact is missing: {expected_current_paths[key]}")

    protected_current = promotion.get("protected_current_artifacts_sha256", {})
    if not isinstance(protected_current, dict) or set(protected_current) != {
        *expected_current_paths.values(),
        "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
        "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
    }:
        issues.append("manifest current Phase 7C artifact hashes are missing or substituted")
        protected_current = protected_current if isinstance(protected_current, dict) else {}
    for relative, expected_hash in protected_current.items():
        path = root / relative
        if not path.is_file() or sha256_file(path) != expected_hash:
            issues.append(f"protected current Phase 7C artifact is missing or changed: {relative}")

    issues.extend(_fp001_protected_historical_evidence_issues(root, promotion, integrity_rules))
    predecessor_hashes = promotion.get("predecessor_archives_sha256", {})
    if not isinstance(predecessor_hashes, dict) or not predecessor_hashes:
        issues.append("manifest does not hash-pin Phase 7C / hard-stop predecessor archives")
        predecessor_hashes = {}
    for archived_path, digest in predecessor_hashes.items():
        archive = root / archived_path
        if not archive.is_file() or sha256_file(archive) != digest:
            issues.append(f"direct Phase 7C predecessor archive is missing or changed: {archived_path}")
        retired = archived_path.replace("/archive/", "/working/")
        if retired.endswith("02_OPEN_WORK_v1.2.72.md"):
            retired = "docs/00_platform/02_OPEN_WORK_v1.2.72.md"
        elif retired.endswith("02_OPEN_WORK_v1.2.71.md"):
            retired = "docs/00_platform/02_OPEN_WORK_v1.2.71.md"
        elif retired.endswith("02_OPEN_WORK_v1.2.70.md"):
            retired = "docs/00_platform/02_OPEN_WORK_v1.2.70.md"
        if (root / retired).exists():
            issues.append(f"direct Phase 7C predecessor remains at a retired working path: {retired}")

    candidate_path = "docs/00_platform/archive/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
    candidate_hash = "c4913808e7c403f223270599e6b3d2ec8f075dc8450a9271c3ebd7c97ab28a19"
    candidate = root / candidate_path
    if promotion.get("candidate_archive_path") != candidate_path or promotion.get("candidate_archive_sha256") != candidate_hash or not candidate.is_file() or sha256_file(candidate) != candidate_hash:
        issues.append("immutable PR #125 candidate evidence or its pinned SHA-256 changed")

    current_skeleton = current_documents["fp001_skeleton"]
    predecessor_skeleton = root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.16.md"
    marker_start = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:START -->"
    marker_end = "<!-- NEWYOU:FP001-PMR-RECONCILIATION-CONTRACT:END -->"
    def marked_pmr(path: Path) -> str:
        if not path.is_file():
            return ""
        text = path.read_text(encoding="utf-8")
        if text.count(marker_start) != 1 or text.count(marker_end) != 1:
            return ""
        left, right = text.index(marker_start), text.index(marker_end)
        return text[left:right + len(marker_end)] if left < right else ""
    if not marked_pmr(predecessor_skeleton) or marked_pmr(current_skeleton) != marked_pmr(predecessor_skeleton):
        issues.append("current skeleton changed or lost the certified PR #67 PMR contract block")
    skeleton_text = current_skeleton.read_text(encoding="utf-8") if current_skeleton.is_file() else ""
    if "The six affected Domains and seven material capability relationships remain unchanged." not in skeleton_text:
        issues.append("current skeleton omits the preserved six-Domain and seven-capability scope")
    if "Phase 7B reconciliation v0.1.0 is COMPLETE / CERTIFIED / CURRENT" not in skeleton_text:
        issues.append("current skeleton does not preserve the certified Phase 7B route")

    dossier_files = {
        "Identity & Access": "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
        "Communications": "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        "Audit & Evidence": "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
    }
    dossier_hashes = phase7b.get("dossier_sha256", {})
    for name, relative in dossier_files.items():
        path = root / relative
        expected = dossier_hashes.get(name) if isinstance(dossier_hashes, dict) else None
        if not path.is_file() or not isinstance(expected, str) or sha256_file(path) != expected:
            issues.append(f"certified {name} dossier changed from its Phase 7B baseline")
            if name == "Identity & Access":
                issues.append("Identity current lifecycle or semantic body changed from its certified Phase 7B baseline")
    identity_dossier_text = (root / dossier_files["Identity & Access"]).read_text(encoding="utf-8") if (root / dossier_files["Identity & Access"]).is_file() else ""
    identity_headings = list(re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*#*\s*$", identity_dossier_text))
    history_headings = [
        heading for heading in identity_headings
        if heading.group(1) == "###" and heading.group(2) == "Inherited v0.1.3 certification evidence"
    ]
    baseline_headings = [
        heading for heading in identity_headings
        if heading.group(1) == "##" and heading.group(2) == "A. Baseline and scope"
    ]
    if (
        len(history_headings) != 1
        or len(baseline_headings) != 1
        or history_headings[0].start() >= baseline_headings[0].start()
    ):
        issues.append("active Identity lifecycle evidence boundaries are missing, duplicated or malformed")

    active_identity_dossiers = sorted(
        path
        for path in (root / "docs/00_platform/working").rglob("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v*.md")
        if "archive" not in path.parts
    )
    expected_identity_dossier = root / dossier_files["Identity & Access"]
    if active_identity_dossiers != [expected_identity_dossier]:
        issues.append("exactly one active certified/current Identity dossier v0.1.4 is required; stale candidates or extra versions remain active")

    active_skeletons = sorted(
        path
        for path in (root / "docs/00_platform/working").rglob("FP-001_FEATURE_PACK_SKELETON_WORKING_v*.md")
        if "archive" not in path.parts
    )
    if active_skeletons != [current_skeleton]:
        issues.append("exactly one active certified/current FP-001 skeleton v0.1.18 is required; stale candidates or extra versions remain active")

    active_audit_dossiers = sorted(
        path
        for path in (root / "docs/00_platform").rglob("*.md")
        if "working" in path.parts
        and "archive" not in path.parts
        and path.name.upper().startswith("FP-001")
        and "AUDIT" in path.name.upper()
        and "DOSSIER" in path.name.upper()
    )
    expected_audit_dossier = root / dossier_files["Audit & Evidence"]
    if active_audit_dossiers != [expected_audit_dossier]:
        issues.append("only the current FP-001 Audit dossier v0.1.0 status successor may exist outside archive")

    open_work = current_documents["open_work"].read_text(encoding="utf-8") if current_documents["open_work"].is_file() else ""
    open_work_provenance_heading = "## 12.14 — PR #76 candidate certification and post-merge evidence; PR #77 current-status promotion"
    open_work_provenance = (
        "PR #76 certified the v0.1.4 candidate and supplied completed post-merge certification evidence. "
        "It did not make v0.1.4 current. This separate PR #77 status successor records the current-status "
        "promotion; the resulting Identity state is CERTIFIED / CURRENT."
    )
    open_work_sections = list(re.finditer(r"(?m)^## 12\.14[^\n]*$", open_work))
    if len(open_work_sections) == 1:
        section_start = open_work_sections[0].start()
        next_section = re.search(r"(?m)^##\s+", open_work[section_start + 1 :])
        section_end = section_start + 1 + next_section.start() if next_section is not None else len(open_work)
        section_text = open_work[section_start:section_end]
    else:
        section_text = ""
    if (
        len(open_work_sections) != 1
        or open_work_sections[0].group(0) != open_work_provenance_heading
        or section_text.count(open_work_provenance) != 1
        or "PR #76 certification/promotion" in section_text
    ):
        issues.append("Open Work §12.14 does not separate PR #76 candidate/post-merge certification evidence from the PR #77 current-status successor")

    state_match = re.search(r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->", open_work, re.DOTALL)
    try:
        state = json.loads(state_match.group(1), object_pairs_hook=_reject_duplicate_json_keys) if state_match else {}
    except (json.JSONDecodeError, TypeError, ValueError):
        state = {}
    required_state = {
        "status_successor_version": "1.2.74",
        "status_successor_base_sha": "675a8c50ac53a995a48e4d262df42065f8ccd412",
        "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c": "COMPLETE / CERTIFIED / CURRENT",
        "phase_7c_execution_tracker_state": "CLOSED / COMPLETED",
        "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.16.md",
        "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md",
        "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.18.md",
        "programme_router_issue_111_state": "OPEN",
        "proof_classification": "NEW_TRACER_BULLET",
        "architectural_proof_classification_status": "COMPLETE / FINALISED",
        "architectural_proof_requirement": "NEW_TRACER_BULLET",
        "selected_proof_vehicle": "NEW_TRACER_BULLET",
        "reuse_existing_proof": "NOT SELECTED",
        "tracer_bullet": "REQUIRED / NOT YET DEFINED",
        "tracer_bullet_id": "NONE / NOT CREATED",
        "architectural_proof_execution": "NOT STARTED",
        "development_entry_hard_stop_status": "PASS / ALL 10 CONDITIONS SATISFIED",
        "development_entry_hard_stop_conditions_1_through_10": "SATISFIED",
        "next_stage": "NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION",
        "application_implementation": "AUTHORISED",
        "phase8": "AUTHORISED",
    }
    if any(state.get(key) != value for key, value in required_state.items()):
        issues.append("Open Work current lifecycle state is missing or contradicts the closed-tracker route")
    expected_atlas_status = (
        "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.16.md`; "
        "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.15.md`; "
        "pinned v0.2.1 source-at-freeze artifacts remain preserved; DERIVED / NON-AUTHORITATIVE; "
        "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this successor does not create ATLAS-12"
    )
    if re.findall(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", open_work) != [expected_atlas_status]:
        issues.append("Open Work current Atlas route must name its byte-identical immediate predecessor in archive")
    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    active = open_work[active_start:active_end] if active_start >= 0 and active_end > active_start else ""
    required_active = (
        "PHASE 7A: COMPLETE",
        "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
        "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "PROGRAMME ROUTER #111: OPEN",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        "ARCHITECTURAL PROOF REQUIREMENT / SELECTED PROOF VEHICLE: NEW_TRACER_BULLET",
        "REUSE_EXISTING_PROOF: NOT SELECTED",
        "TRACER BULLET: REQUIRED / NOT YET DEFINED",
        "TRACER BULLET ID: NONE / NOT CREATED",
        "ARCHITECTURAL PROOF EXECUTION: NOT STARTED",
        "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED",
        "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
        "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET",
    )
    for token in required_active:
        if token not in active:
            issues.append(f"Open Work active current route omits {token!r}")
    if re.search(r"(?im)^.*#124[^\n]{0,120}\bOPEN\b.*$", active):
        issues.append("Open Work active route projects issue #124 as OPEN")
    contract_state = state.get("phase_7c_final_feature_pack_contract", {})
    if not isinstance(contract_state, dict) or contract_state.get("lifecycle") != "COMPLETE / CERTIFIED / CURRENT" or contract_state.get("resulting_main_fia_tests") != 455 or contract_state.get("resulting_main_fia_assertions") != 728 or contract_state.get("resulting_main_fia_findings") != 0:
        issues.append("Open Work current route omits current contract or resulting-main evidence")

    readme = root / "docs/00_platform/README.md"
    readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    readme_current = _markdown_h2_section(readme_text, "Current State") or ""
    hard_stop_readme = "DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED" in readme_current
    for token in (
        "PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT",
        "PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED",
        "PROGRAMME ROUTER #111: OPEN",
        "ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED",
        "PROOF CLASSIFICATION: NEW_TRACER_BULLET",
        *(
            (
                "PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)",
                "APPLICATION IMPLEMENTATION: AUTHORISED (BOUNDED PHASE 8 ARCHITECTURAL PROOF ONLY)",
            )
            if hard_stop_readme
            else (
                "PHASE 8: UNAUTHORISED",
                "APPLICATION IMPLEMENTATION: UNAUTHORISED",
            )
        ),
    ):
        if token not in readme_current:
            issues.append(f"README current state omits {token!r}")
    for path in expected_current_paths.values():
        if Path(path).name not in readme_text:
            issues.append(f"README does not route current artifact {path}")
    if "IDENTITY v0.1.4: CERTIFIED / CURRENT under the separate PR #77 status successor" not in readme_text:
        issues.append("README does not preserve the current Identity v0.1.4 status route")

    graph_rules = integrity_rules.get("graph_rules", {})
    guard_note = graph_rules.get("stale_predecessor_current_path_guard_note", "") if isinstance(graph_rules, dict) else ""
    if "The separate PR #119 Audit v0.1.0 current-status promotion" not in guard_note:
        issues.append("manifest Audit promotion guard note must distinguish PR #119 promotion from PR #118 candidate")

    atlas = current_documents["delivery_atlas"].read_text(encoding="utf-8") if current_documents["delivery_atlas"].is_file() else ""
    if hard_stop_readme:
        if "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.15.md`" not in atlas or "- **SemVer transition:** `v0.4.15 → v0.4.16`" not in atlas:
            issues.append("current Atlas artifact lineage or status-successor metadata is wrong")
        harden = current_documents["harden_02"].read_text(encoding="utf-8") if current_documents["harden_02"].is_file() else ""
        header = harden.split("### Revision log", 1)[0]
        if "- **Plan / contract version:** `v0.5.18`" not in header or "- **Immediate predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.17.md`" not in header or "- **v0.5.18 status successor base main SHA:** `675a8c50ac53a995a48e4d262df42065f8ccd412`" not in header:
            issues.append("current HARDEN-02 v0.5.18 successor metadata declaration is missing or incorrect")
        predecessor_fields = re.findall(
            r"(?im)^-\s*\*\*(?:current|direct|immediate) predecessor:\*\*\s*`([^`]+)`",
            header,
        )
        if predecessor_fields != ["archive/HARDEN-02_CONTRACT_WORKING_v0.5.17.md"]:
            issues.append("current HARDEN-02 v0.5.18 must identify only v0.5.17 as its direct predecessor")
        try:
            section_20 = harden.split("## 20. Contract-stage STOP", 1)[1].split("## 21.", 1)[0]
        except IndexError:
            section_20 = ""
        required_section_20_authority = (
            "No application implementation is authorised by HARDEN-02 itself.",
            "Current Open Work v1.2.74 separately records application implementation as AUTHORISED only inside the bounded Phase 8 / NEW_TRACER_BULLET architectural-proof stage.",
        )
        if any(statement not in section_20 for statement in required_section_20_authority) or re.search(
            r"(?i)\bNo application implementation is authorised\.(?:\s|$)", section_20
        ):
            issues.append("current HARDEN-02 section 20 must scope its implementation boundary to HARDEN-02 and Open Work")
    else:
        if "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.14.md`" not in atlas or "- **SemVer transition:** `v0.4.14 → v0.4.15`" not in atlas:
            issues.append("current Atlas artifact lineage or status-successor metadata is wrong")
        harden = current_documents["harden_02"].read_text(encoding="utf-8") if current_documents["harden_02"].is_file() else ""
        header = harden.split("### Revision log", 1)[0]
        if "- **Plan / contract version:** `v0.5.17`" not in header or "- **Immediate predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.16.md`" not in header or "- **v0.5.17 status successor base main SHA:** `24a9ad925ee1ab6d75ddb44bae6df0b4f3d09bca`" not in header:
            issues.append("current HARDEN-02 v0.5.18 successor metadata declaration is missing or incorrect")
    if "after this status successor merges" in active.casefold() or "OPEN through promotion merge" in active:
        issues.append("current Open Work route retains stale pre-closure wording")
    return issues

def _check_fp001_pmr_reconciliation(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    docs = root / "docs" / "00_platform"
    current_open_work_entries = [
        entry for entry in _all_entries(manifest)
        if entry.get("document_id") == "OPEN_WORK" and entry.get("lifecycle", "current") != "historical"
    ]
    if len(current_open_work_entries) == 1 and current_open_work_entries[0].get("semver") in {"1.2.73", "1.2.74", "1.2.77"}:
        promotion_issues = _check_fp001_pmr_reconciliation_after_phase7c_promotion(root, manifest, integrity_rules)
        _record_check(
            report,
            "fp001_pmr_reconciliation",
            not promotion_issues,
            "the certified PMR block, dossier baselines and Phase 7B scope remain intact through the FP-001 status successors"
            if not promotion_issues
            else "; ".join(promotion_issues),
            path=(
                "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.21.md"
                if current_open_work_entries[0].get("semver") == "1.2.77"
                else "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.18.md"
            ),
        )
        return

    skeleton = docs / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.13.md"
    communications_dossier = docs / "working" / "FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    communications_v010_candidate = docs / "archive" / "FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    dossier = docs / "working" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
    skeleton_candidate = docs / "archive" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"
    dossier_candidate = docs / "archive" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md"
    identity_predecessor = docs / "archive" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md"
    identity_promotion_candidate = docs / "archive" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
    superseded_identity_current = docs / "archive" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
    identity_v014_candidate = docs / "archive" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
    predecessor_skeleton = docs / "archive" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
    predecessor_dossier = docs / "archive" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    readme_path = docs / "README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    issues: list[str] = []

    current_entries = [
        entry
        for entry in _all_entries(manifest)
        if entry.get("document_id") == "OPEN_WORK"
        and entry.get("lifecycle", "current") != "historical"
    ]
    audit_promotion_current = False
    reconciliation_candidate_current = False
    reconciliation_certified_current = False
    tracker_closure_sync_current = False
    phase7c_candidate_current = False
    if len(current_entries) != 1:
        issues.append("manifest must identify exactly one current Open Work route")
        open_work = ""
    else:
        current_open_work = current_entries[0]
        open_work_path = root / _relative_path(current_open_work)
        open_work = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() else ""
        current_open_work_version = current_open_work.get("semver")
        audit_promotion_current = current_open_work_version in {"1.2.65", "1.2.66", "1.2.67", "1.2.68", "1.2.69"}
        reconciliation_candidate_current = current_open_work_version == "1.2.66"
        reconciliation_certified_current = current_open_work_version in {"1.2.67", "1.2.68", "1.2.69"}
        tracker_closure_sync_current = current_open_work_version == "1.2.68"
        phase7c_candidate_current = current_open_work_version == "1.2.69"
        expected_open_work_path = (
            "docs/00_platform/02_OPEN_WORK_v1.2.69.md"
            if phase7c_candidate_current
            else "docs/00_platform/02_OPEN_WORK_v1.2.68.md"
            if reconciliation_certified_current
            else
            "docs/00_platform/02_OPEN_WORK_v1.2.66.md"
            if reconciliation_candidate_current
            else "docs/00_platform/02_OPEN_WORK_v1.2.65.md"
            if audit_promotion_current
            else "docs/00_platform/02_OPEN_WORK_v1.2.64.md"
        )
        expected_open_work_filename = Path(expected_open_work_path).name
        if _relative_path(current_open_work) != expected_open_work_path:
            issues.append(f"manifest Open Work route is not {expected_open_work_filename}")
        if current_open_work.get("canonical_filename") != expected_open_work_filename:
            issues.append("manifest current Open Work filename is stale")
        if current_open_work_version not in {"1.2.64", "1.2.65", "1.2.66", "1.2.67", "1.2.68", "1.2.69"}:
            issues.append("manifest current Open Work version is stale")
    atlas_status_lines = re.findall(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", open_work)
    expected_atlas_status = (
        f"ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.{'4.11' if phase7c_candidate_current else '4.10' if tracker_closure_sync_current else '4.9' if reconciliation_certified_current else '4.8' if reconciliation_candidate_current else '4.7' if audit_promotion_current else '4.6'}.md`; "
        f"immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.{'4.10' if phase7c_candidate_current else '4.9' if tracker_closure_sync_current else '4.8' if reconciliation_certified_current else '4.7' if reconciliation_candidate_current else '4.6' if audit_promotion_current else '4.5'}.md`; "
        "pinned v0.2.1 source-at-freeze artifacts remain preserved; DERIVED / NON-AUTHORITATIVE; "
        "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this successor does not create ATLAS-12"
    )
    if atlas_status_lines != [expected_atlas_status]:
        issues.append(
            "Open Work current Atlas route must name its byte-identical immediate predecessor in archive"
        )

    expected_active_skeletons = [skeleton]
    expected_active_dossiers = [dossier]
    active_skeletons = sorted((docs / "working").glob("FP-001_FEATURE_PACK_SKELETON_WORKING_v*.md"))
    active_dossiers = sorted((docs / "working").glob("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v*.md"))
    if active_skeletons != expected_active_skeletons:
        issues.append("exactly one active certified/current FP-001 skeleton is required; stale candidates or extra versions remain active")
    if active_dossiers != expected_active_dossiers:
        issues.append("exactly one active certified/current Identity dossier v0.1.4 is required; stale candidates or extra versions remain active")
    for path, label in ((skeleton, "certified skeleton"), (dossier, "certified Identity dossier")):
        if not path.is_file():
            issues.append(f"{label} is missing")
    active_audit_candidates = sorted(
        path
        for path in docs.rglob("*.md")
        if path.name.upper().startswith("FP-001")
        and "AUDIT" in path.name.upper()
        and "DOSSIER" in path.name.upper()
        and "archive" not in path.parts
    )
    expected_audit_candidate = (
        docs / "working" / "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    )
    if audit_promotion_current:
        if active_audit_candidates != [expected_audit_candidate]:
            issues.append("only the current FP-001 Audit dossier v0.1.0 status successor may exist outside archive")
    elif active_audit_candidates:
        if active_audit_candidates != [expected_audit_candidate]:
            issues.append(
                "only the FP-001 Audit dossier v0.1.0 review candidate may exist outside the archive"
            )
        else:
            candidate_text = expected_audit_candidate.read_text(encoding="utf-8")
            header_boundary = "## 1. Baseline, purpose and scope"
            if header_boundary not in candidate_text:
                issues.append(
                    "the FP-001 Audit dossier candidate is missing its expected lifecycle header boundary"
                )
            candidate_header = candidate_text.split(header_boundary, 1)[0]
            required_candidate_header = (
                "PROPOSED PATH: docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
                "PROPOSED VERSION: v0.1.0",
                "PHASE: 7B implementation-grade planning",
                "FEATURE PACK: FP-001",
                "DOMAIN: AUDIT & EVIDENCE",
                "STATUS: CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT",
                "NON-EXECUTABLE",
                "NOT PHASE 7C DEVELOPMENT-ENTRY AUTHORITY",
                "DOES NOT AMEND PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW",
            )
            if any(candidate_header.count(line) != 1 for line in required_candidate_header):
                issues.append(
                    "the FP-001 Audit dossier candidate is missing its exact non-current review lifecycle header"
                )
            current_manifest_paths = {
                _relative_path(entry)
                for entry in _all_entries(manifest)
                if entry.get("lifecycle", "current") != "historical"
            }
            candidate_relative_path = (
                "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            )
            if candidate_relative_path in current_manifest_paths:
                issues.append(
                    "the FP-001 Audit review candidate must remain outside current authority manifest routing"
                )
            if expected_audit_candidate.name in readme and (
                "candidate v0.1.0 is authored and review-ready in PR #118" not in readme
                or "NOT CERTIFIED / NOT CURRENT" not in readme
                or "not current governing authority" not in readme
            ):
                issues.append("README candidate routing omits its review-only, non-current lifecycle boundary")

    required_archive_hashes = {
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md",
        "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
        "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md",
        "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
        "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md",
    }
    expected_archive_hashes = integrity_rules.get("fp001_pmr_predecessor_archives")
    if not isinstance(expected_archive_hashes, dict):
        issues.append("manifest does not pin predecessor and PR #67 / #70 candidate archive hashes")
        expected_archive_hashes = {}
    if set(expected_archive_hashes) != required_archive_hashes:
        issues.append("manifest FP-001 archive hash paths are missing, substituted or unexpected")
    for relative in sorted(required_archive_hashes):
        archive = root / relative
        expected_hash = expected_archive_hashes.get(relative)
        if not archive.is_file():
            issues.append(f"required FP-001 archive is missing: {relative}")
        if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            issues.append(f"manifest archive hash is missing or malformed: {relative}")
        elif archive.is_file() and sha256_file(archive) != expected_hash:
            issues.append(f"FP-001 archive bytes do not match the pinned hash: {relative}")

    required_identity_v014_archives = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.56.md": "c14474cd91a236eaa6df8509e3f21ab0a4d2236942e7930d2be19a74b68b0516",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.3.8.md": "c557741ff03707eb159a9daaf06aa23a05cc2c5c90f8a4c831caa82d0a50af12",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.0.md": "3397af97ebd5a1a7a7b5696ff9f8ab75c18f1befb9ad4808b7d0f0cc60234fef",
        "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md": "a88f993d92ea9ff0dc5652c284ccf4e2c17f4bb16b31759fb3417044d7f8e254",
        "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md": "1557a4bded20b94fc363d96dd5a601213de105e0daccfa1970b869a0e38f362f",
    }
    configured_identity_archives = integrity_rules.get("identity_v014_promotion_archives")
    if not isinstance(configured_identity_archives, dict) or set(configured_identity_archives) != set(required_identity_v014_archives):
        issues.append("manifest Identity v0.1.4 promotion archive paths are missing, substituted or unexpected")
        configured_identity_archives = configured_identity_archives if isinstance(configured_identity_archives, dict) else {}
    for relative, required_hash in required_identity_v014_archives.items():
        archive = root / relative
        if not archive.is_file():
            issues.append(f"Identity v0.1.4 promotion archive is missing: {relative}")
        if configured_identity_archives.get(relative) != required_hash:
            issues.append(f"manifest Identity v0.1.4 archive hash is wrong: {relative}")
        if archive.is_file() and sha256_file(archive) != required_hash:
            issues.append(f"Identity v0.1.4 promotion archive bytes changed: {relative}")
    required_communications_start_archives = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.57.md": "4c9098360dbc5b3d56cb0f8b1de97c42271d87f9895f0947363d7d35e01564c6",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.3.9.md": "1cdbb6e47bd307b78f53b6bddabbbaa7d8fcddf0fb6fabb5542a50fed674cb69",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.1.md": "098569e5a872a212a5c403104494668b566cd7173e95d4d6ce6ee5f7de4de36e",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md": "0a472eadd814591d8a98c20a163cfe5c9013e0dba297c78546163cb147d3dcb1",
    }
    configured_communications_archives = integrity_rules.get("communications_start_status_archives")
    if (
        not isinstance(configured_communications_archives, dict)
        or set(configured_communications_archives) != set(required_communications_start_archives)
    ):
        issues.append("manifest Communications-start status archive paths are missing, substituted or unexpected")
        configured_communications_archives = (
            configured_communications_archives
            if isinstance(configured_communications_archives, dict)
            else {}
        )
    for relative, required_hash in required_communications_start_archives.items():
        archive = root / relative
        if not archive.is_file():
            issues.append(f"Communications-start status archive is missing: {relative}")
        if configured_communications_archives.get(relative) != required_hash:
            issues.append(f"manifest Communications-start status archive hash is wrong: {relative}")
        if archive.is_file() and sha256_file(archive) != required_hash:
            issues.append(f"Communications-start predecessor bytes changed: {relative}")
    required_communications_v010_archives = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.58.md": "a05a502f00a374026d531a2c2f303ec2bc6129e7bbde508c7a29c601561a9da1",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.0.md": "e582ea9c83e096ef0f7489da27e057ae0de41e82810bf9820caaefa80cbc3209",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md": "68d807b2dd26962ffa44472fba483cc8f3e7baddeafe5af8a5492175b44e51e1",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.4.md": "5316d909bfacb3d3e0776cbbdd7636f09b40d0a9b4ce405841a7f6c8155c3e1d",
        "docs/00_platform/archive/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "039f1b0e249f62dfd606fc6484681d4e821077fb4c89eba65c4f33eb752277a9",
    }
    configured_communications_v010_archives = integrity_rules.get("communications_v010_promotion_archives")
    if (
        not isinstance(configured_communications_v010_archives, dict)
        or set(configured_communications_v010_archives) != set(required_communications_v010_archives)
    ):
        issues.append("manifest Communications v0.1.0 promotion archive paths are missing, substituted or unexpected")
        configured_communications_v010_archives = (
            configured_communications_v010_archives
            if isinstance(configured_communications_v010_archives, dict)
            else {}
        )
    for relative, required_hash in required_communications_v010_archives.items():
        archive = root / relative
        if not archive.is_file():
            issues.append(f"Communications v0.1.0 promotion archive is missing: {relative}")
        if configured_communications_v010_archives.get(relative) != required_hash:
            issues.append(f"manifest Communications v0.1.0 archive hash is wrong: {relative}")
        if archive.is_file() and sha256_file(archive) != required_hash:
            issues.append(f"Communications v0.1.0 promotion archive bytes changed: {relative}")
    if identity_promotion_candidate.is_file() and superseded_identity_current.is_file() and identity_promotion_candidate.read_bytes() == superseded_identity_current.read_bytes():
        issues.append("PR #70 candidate archive was confused with the promoted/current v0.1.3 snapshot")
    if (docs / "working" / "candidates" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").exists():
        issues.append("promoted Identity v0.1.4 remains in the candidate route")

    required_work_start_archives = {
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.62.md",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.4.md",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.6.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.6.md",
    }
    work_start_archives = integrity_rules.get("fp001_audit_dossier_work_start_predecessor_archives")
    if not isinstance(work_start_archives, dict) or set(work_start_archives) != required_work_start_archives:
        issues.append("manifest Audit work-start predecessor archive paths are missing, substituted or unexpected")
        work_start_archives = work_start_archives if isinstance(work_start_archives, dict) else {}
    for relative in sorted(required_work_start_archives):
        archive = root / relative
        expected_hash = work_start_archives.get(relative)
        if not archive.is_file():
            issues.append(f"Audit work-start predecessor archive is missing: {relative}")
        if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            issues.append(f"manifest Audit work-start archive hash is missing or malformed: {relative}")
        elif archive.is_file() and sha256_file(archive) != expected_hash:
            issues.append(f"Audit work-start predecessor bytes do not match their pinned hash: {relative}")

    navigation_paths = integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])
    expected_navigation_paths = {
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.11.md" if phase7c_candidate_current else "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.10.md" if reconciliation_certified_current else "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.8.md" if reconciliation_candidate_current else "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.7.md" if audit_promotion_current else "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.6.md",
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.13.md" if phase7c_candidate_current else "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.12.md" if reconciliation_certified_current else "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md" if reconciliation_candidate_current else "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.9.md" if audit_promotion_current else "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md",
        "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
        "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.13.md" if phase7c_candidate_current else "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.12.md" if reconciliation_certified_current else "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.10.md" if reconciliation_candidate_current else "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.9.md" if audit_promotion_current else "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.8.md",
    }
    if reconciliation_certified_current:
        expected_navigation_paths.add(
            "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
        )
    if phase7c_candidate_current:
        expected_navigation_paths.add(
            "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md"
        )
    if audit_promotion_current:
        expected_navigation_paths.add(
            "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        )
    if reconciliation_certified_current:
        expected_navigation_paths.add(
            "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
        )
    if not isinstance(navigation_paths, list) or set(navigation_paths) != expected_navigation_paths or len(navigation_paths) != len(expected_navigation_paths):
        issues.append("manifest navigation does not route exactly the current FP-001, Atlas and HARDEN successors")

    retired_working_predecessors = (
        (
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.8.md",
            "immediate Atlas predecessor remains in the working route",
        ),
        (
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md",
            "immediate Skeleton predecessor remains in the working route",
        ),
        (
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.10.md",
            "immediate HARDEN-02 predecessor remains in the working route",
        ),
        (
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.6.md",
            "immediate Atlas predecessor remains in the working route",
        ),
        (
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.8.md",
            "immediate Atlas predecessor remains in the working route",
        ),
        (
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md",
            "immediate Skeleton predecessor remains in the working route",
        ),
        (
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.8.md",
            "immediate HARDEN-02 predecessor remains in the working route",
        ),
        (
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.0.md",
            "immediate HARDEN-02 predecessor remains in the working route",
        ),
    )
    for relative_path, issue in retired_working_predecessors:
        if (root / relative_path).exists():
            issues.append(issue)

    skeleton_text = skeleton.read_text(encoding="utf-8") if skeleton.is_file() else ""
    reconciliation_path = docs / "working" / "FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
    reconciliation_text = reconciliation_path.read_text(encoding="utf-8") if reconciliation_path.is_file() else ""
    dossier_text = dossier.read_text(encoding="utf-8") if dossier.is_file() else ""
    skeleton_candidate_text = skeleton_candidate.read_text(encoding="utf-8") if skeleton_candidate.is_file() else ""
    dossier_candidate_text = dossier_candidate.read_text(encoding="utf-8") if dossier_candidate.is_file() else ""
    identity_promotion_candidate_text = identity_promotion_candidate.read_text(encoding="utf-8") if identity_promotion_candidate.is_file() else ""
    superseded_identity_current_text = superseded_identity_current.read_text(encoding="utf-8") if superseded_identity_current.is_file() else ""
    identity_v014_candidate_text = identity_v014_candidate.read_text(encoding="utf-8") if identity_v014_candidate.is_file() else ""
    communications_dossier_text = communications_dossier.read_text(encoding="utf-8") if communications_dossier.is_file() else ""
    communications_v010_candidate_text = (
        communications_v010_candidate.read_text(encoding="utf-8") if communications_v010_candidate.is_file() else ""
    )

    if not re.search(r"(?m)^\*\*Lifecycle status:\*\*\s+(?:`CERTIFIED / CURRENT`|CERTIFIED / CURRENT)\b", skeleton_text):
        issues.append("current FP-001 skeleton is not marked CERTIFIED / CURRENT")
    if "RECONCILIATION CANDIDATE / NOT CERTIFIED" in skeleton_text:
        issues.append("active skeleton remains a reconciliation candidate")
    if "RECONCILIATION CANDIDATE / NOT CERTIFIED" in dossier_text:
        issues.append("active Identity dossier remains a reconciliation candidate")
    if (
        "Communications remains " + chr(96) + "COMPLETE / CERTIFIED / CURRENT v0.1.0" + chr(96) not in dossier_text
        or "Communications finalisation remains " + chr(96) + "BLOCKED / STOP" + chr(96) not in dossier_text
        or "No Communications dossier, Phase 7C work or implementation starts here." not in dossier_text
    ):
        issues.append("certified Identity dossier does not preserve the Communications certification and finalisation stop boundary")

    headings = list(re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*#*\s*$", dossier_text))
    history_headings = [
        heading for heading in headings
        if heading.group(1) == "###" and heading.group(2) == "Inherited v0.1.3 certification evidence"
    ]
    baseline_headings = [
        heading for heading in headings
        if heading.group(1) == "##" and heading.group(2) == "A. Baseline and scope"
    ]
    historical_boundary_ok = len(history_headings) == 1 and len(baseline_headings) == 1
    if historical_boundary_ok:
        history_heading = history_headings[0]
        baseline_heading = baseline_headings[0]
        following_headings = [heading for heading in headings if heading.start() > history_heading.start()]
        historical_boundary_ok = (
            history_heading.start() < baseline_heading.start()
            and len(following_headings) > 0
            and following_headings[0] == baseline_heading
        )
    if not historical_boundary_ok:
        issues.append("active Identity lifecycle evidence boundaries are missing, duplicated or malformed")

    expected_identity_state = {
        "artifact_version": "v0.1.4",
        "identity_lifecycle": "CERTIFIED / CURRENT",
        "pr_76_candidate_certification": "COMPLETE",
        "pr_76_post_merge_certification_evidence": "COMPLETE",
        "current_status_promotion": "PR #77 STATUS SUCCESSOR",
        "communications": "COMPLETE / CERTIFIED / CURRENT v0.1.0",
        "communications_finalisation": "BLOCKED / STOP",
        "phase_7c": "BLOCKED / NOT_STARTED",
        "proof_classification": "NOT FINALISED",
        "phase_8_application_implementation": "UNAUTHORISED",
    }
    lifecycle_start_marker = "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_START -->"
    lifecycle_end_marker = "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_END -->"
    marker_like_lines = [
        line.strip()
        for line in dossier_text.splitlines()
        if line.lstrip().startswith("<!--") and "IDENTITY_V014_CURRENT_LIFECYCLE_STATE_" in line
    ]
    start_markers = list(re.finditer(r"(?m)^<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_START -->[ \t]*$", dossier_text))
    end_markers = list(re.finditer(r"(?m)^<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_END -->[ \t]*$", dossier_text))
    current_state: dict[str, Any] = {}
    lifecycle_block_valid = (
        marker_like_lines == [lifecycle_start_marker, lifecycle_end_marker]
        and len(start_markers) == 1
        and len(end_markers) == 1
        and start_markers[0].start() < end_markers[0].start()
        and historical_boundary_ok
    )
    status_mirrors = list(re.finditer(r"(?m)^\*\*Status:\*\*\s+`([^`]+)`[^\n]*$", dossier_text))
    status_provenance_mirrors = list(
        re.finditer(
            r"(?m)^\*\*Status:\*\*\s+`([^`]+)`; PR #76 candidate certification is `([^`]+)`; "
            r"PR #76 post-merge certification evidence is `([^`]+)`; current-status promotion is `([^`]+)`\.[^\n]*$",
            dossier_text,
        )
    )
    version_mirrors = list(re.finditer(r"(?m)^\*\*Artifact version:\*\*\s+(v\d+\.\d+\.\d+)\b[^\n]*$", dossier_text))
    if lifecycle_block_valid:
        status_line_end = status_mirrors[0].end() if len(status_mirrors) == 1 else -1
        history_start = history_headings[0].start()
        lifecycle_block_valid = (
            status_line_end >= 0
            and status_line_end < start_markers[0].start()
            and end_markers[0].start() < history_start
        )
    if lifecycle_block_valid:
        block_content = dossier_text[start_markers[0].end() : end_markers[0].start()]
        block_pattern = re.compile(
            r"\s*This structured block is the machine-authoritative lifecycle projection for this artifact\. "
            r"Historical narrative and explanatory prose do not independently redefine current lifecycle state\."
            r"\s*```json\s*(\{.*?\})\s*```\s*",
            re.DOTALL,
        )
        block_match = block_pattern.fullmatch(block_content)
        if block_match is None:
            lifecycle_block_valid = False
        else:
            try:
                parsed_state = json.loads(
                    block_match.group(1),
                    object_pairs_hook=_reject_duplicate_json_keys,
                )
            except (json.JSONDecodeError, TypeError, ValueError):
                lifecycle_block_valid = False
            else:
                if isinstance(parsed_state, dict):
                    current_state = parsed_state
                lifecycle_block_valid = parsed_state == expected_identity_state
    if not lifecycle_block_valid:
        issues.append(
            "Identity current lifecycle block is missing, duplicated, malformed, misplaced or inconsistent with governed state"
        )

    if len(status_mirrors) != 1 or status_mirrors[0].group(1) != current_state.get("identity_lifecycle"):
        issues.append("Identity current lifecycle header Status mirror disagrees with the structured state")
    if (
        len(status_provenance_mirrors) != 1
        or status_provenance_mirrors[0].group(1) != current_state.get("identity_lifecycle")
        or status_provenance_mirrors[0].group(2) != current_state.get("pr_76_candidate_certification")
        or status_provenance_mirrors[0].group(3) != current_state.get("pr_76_post_merge_certification_evidence")
        or status_provenance_mirrors[0].group(4) != current_state.get("current_status_promotion")
    ):
        issues.append("Identity current lifecycle header Status provenance mirror disagrees with the structured state")
    if len(version_mirrors) != 1 or version_mirrors[0].group(1) != current_state.get("artifact_version"):
        issues.append("Identity current lifecycle header artifact-version mirror disagrees with the structured state")

    phase7c_headers = list(re.finditer(r"(?m)^### `BLOCKS_PHASE7C`[ \t]*$", dossier_text))
    release_headers = list(re.finditer(r"(?m)^### `BLOCKS_RELEASE_ONLY`[ \t]*$", dossier_text))
    if (
        len(phase7c_headers) != 1
        or len(release_headers) != 1
        or phase7c_headers[0].start() >= release_headers[0].start()
    ):
        issues.append("active Identity BLOCKS_PHASE7C lifecycle section is missing, duplicated or malformed")
        phase7c_section = ""
    else:
        phase7c_section = dossier_text[phase7c_headers[0].start() : release_headers[0].start()]

    phase7c_mirror_patterns = {
        "pr_76_candidate_certification": r"(?m)^\* PR #76 candidate certification is `([^`]+)`[.;]$",
        "pr_76_post_merge_certification_evidence": r"(?m)^\* PR #76 post-merge certification evidence is `([^`]+)`\.",
        "current_status_promotion": r"(?m)^\* Current-status promotion is recorded by `([^`]+)`[.;]$",
        "identity_lifecycle": r"(?m)^\* Identity (v\d+\.\d+\.\d+) is `([^`]+)`\.",
        "communications": r"(?m)^\* Communications remains `([^`]+)`;",
        "communications_finalisation": r"(?m)^\* Communications remains `[^`]+`; Communications finalisation remains `([^`]+)` pending",
        "phase_7c": r"(?m)^\* Phase 7C remains `([^`]+)` while",
        "proof_classification": r"(?m)^\* Proof classification remains `([^`]+)`\.",
        "phase_8_application_implementation": r"(?m)^\* Phase 8/application implementation remains `([^`]+)`\.",
    }
    for field, pattern in phase7c_mirror_patterns.items():
        matches = list(re.finditer(pattern, phase7c_section))
        if field == "identity_lifecycle":
            agrees = (
                len(matches) == 1
                and matches[0].group(1) == current_state.get("artifact_version")
                and matches[0].group(2) == current_state.get(field)
            )
        else:
            agrees = len(matches) == 1 and matches[0].group(1) == current_state.get(field)
        if not agrees:
            issues.append(f"Identity current lifecycle BLOCKS_PHASE7C mirror disagrees with structured field {field}")

    required_phase7c_state = (
        "required Phase 7B work remains",
        "conditional dossiers remain subject to explicit adjudication",
        "applicable blocking gates must be resolved",
    )
    for token in required_phase7c_state:
        if token.casefold() not in phase7c_section.casefold():
            issues.append(f"active Identity BLOCKS_PHASE7C lifecycle omits current promotion/STOP state: {token}")

    evidence = (
        "PR #67",
        "79d0540c66f0224ece0330181e61dfef8ab4b458",
        "38022caea64cb2522ab8fc4db730099a94cd6600",
        "4000ae50660930114e3ad43108dc029fd0673d32",
        "a71dbeb2cca79bea0013f9997e40f34769f262f3",
        "36991113390",
        "37009244020",
        "5952693308",
        "5955641536",
        "Fresh independent post-merge review | " + chr(96) + "PASS" + chr(96),
    )
    for token in evidence:
        if token not in skeleton_text:
            issues.append(f"active certification provenance omits PR #67 evidence: {token}")

    lifecycle_start = open_work.find("<!-- HARDEN_02_LIFECYCLE_STATE_START -->")
    lifecycle_end = open_work.find("<!-- HARDEN_02_LIFECYCLE_STATE_END -->", lifecycle_start + 1)
    lifecycle_region = open_work[lifecycle_start:lifecycle_end] if lifecycle_start >= 0 and lifecycle_end > lifecycle_start else ""
    lifecycle_blocks = re.findall(r"```json\s*(\{.*?\})\s*```", lifecycle_region, re.DOTALL)
    try:
        lifecycle_state = (
            json.loads(lifecycle_blocks[0], object_pairs_hook=_reject_duplicate_json_keys)
            if len(lifecycle_blocks) == 1
            else {}
        )
    except (json.JSONDecodeError, TypeError, ValueError):
        lifecycle_state = {}
    expected_fp001_state = {
        "status_successor_base_sha": "3f09bc91199e74d27645ebbb37d45c4831340952",
        "current_stage": "COMMUNICATIONS v0.1.0 CURRENT-STATUS PROMOTION",
        "next_stage": "REMAINING REQUIRED / CONDITIONAL PHASE 7B",
        "status_successor_version": "0.5.5",
        "fp001_reconciliation": "COMPLETE / CERTIFIED",
        "identity_dossier": "CERTIFIED / CURRENT v0.1.4",
        "identity_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
        "communications_dossier": "CERTIFIED / CURRENT v0.1.0",
        "communications_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
        "communications_finalisation": "BLOCKED / STOP",
        "communications": "COMPLETE / CERTIFIED / CURRENT v0.1.0",
        "conditional_dossiers": {
            "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "analytics": "NOT REQUIRED",
        },
        "phase_7c": "BLOCKED / NOT_STARTED",
        "proof_classification": "NOT FINALISED",
        "application_implementation": "BLOCKED",
        "store_cer": "EXCLUDED",
        "completed_milestones": [
            "TARGETED PRODUCT AMENDMENT PROGRAMME",
            "FP-001 PHASE 7A",
            "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
            "HARDEN-02 EXECUTION",
            "ENGINEERING STANDARDS AUTHORITY PROMOTION",
            "FP-001 PMR RECONCILIATION",
            "FP-001 IDENTITY v0.1.3 DURABLE-DELIVERY PATCH PROMOTION",
            "FP-001 IDENTITY v0.1.4 GOVERNANCE-CORRECTION PATCH PROMOTION",
            "FP-001 COMMUNICATIONS v0.1.0 JIT DOMAIN DOSSIER PROMOTION",
        ],
    }
    reconciliation_candidate_current = lifecycle_state.get("status_successor_version") == "0.5.10"
    phase7c_candidate_current = lifecycle_state.get("status_successor_version") == "0.5.13"
    reconciliation_certified_current = lifecycle_state.get("status_successor_version") in {"0.5.11", "0.5.12", "0.5.13"}
    tracker_closure_sync_current = lifecycle_state.get("status_successor_version") == "0.5.12"
    audit_promotion_current = lifecycle_state.get("status_successor_version") in {"0.5.9", "0.5.10", "0.5.11", "0.5.12", "0.5.13"}
    adjudication_current = lifecycle_state.get("status_successor_version") in {"0.5.6", "0.5.7", "0.5.8", "0.5.9", "0.5.10", "0.5.11", "0.5.12", "0.5.13"}
    audit_work_start_current = lifecycle_state.get("status_successor_version") in {"0.5.7", "0.5.8", "0.5.9", "0.5.10", "0.5.11", "0.5.12", "0.5.13"}
    audit_candidate_review_current = lifecycle_state.get("status_successor_version") in {"0.5.8", "0.5.9", "0.5.10", "0.5.11", "0.5.12", "0.5.13"}
    if adjudication_current:
        expected_fp001_state.update(
            {
                "status_successor_base_sha": (
                    "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd"
                    if reconciliation_candidate_current
                    else "3566f1353ef34af58773aa13c6f5bd61d2613d96"
                    if audit_promotion_current
                    else
                    "5f5a994e48d9458aaa6397044b3af4d72c5d5e81"
                    if audit_candidate_review_current
                    else "332d51f19d77430fe4e95911920fe0c87cab524a"
                    if audit_work_start_current
                    else "6036491dfbda0a311b8fcd0ddcdc3af5c3f11ac3"
                ),
                "current_stage": (
                    (
                        "FP-001 PHASE 7B RECONCILIATION CANDIDATE REVIEW"
                        if reconciliation_candidate_current
                        else "FP-001 AUDIT & EVIDENCE DOSSIER CURRENT-STATUS PROMOTION"
                        if audit_promotion_current
                        else
                        "FP-001 PHASE 7B AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE REVIEW"
                        if audit_candidate_review_current
                        else "FP-001 PHASE 7B AUDIT & EVIDENCE JIT DOMAIN DOSSIER WORK START"
                    )
                    if audit_work_start_current
                    else "FP-001 PHASE 7A/7B CONDITIONAL-DOSSIER ADJUDICATION"
                ),
                "next_stage": (
                    (
                        "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
                        if reconciliation_candidate_current
                        else "FP-001 PHASE 7B RECONCILIATION"
                        if audit_promotion_current
                        else
                        "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
                        if audit_candidate_review_current
                        else "AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE"
                    )
                    if audit_work_start_current
                    else "FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER"
                ),
                "status_successor_version": (
                    "0.5.10" if reconciliation_candidate_current else
                    "0.5.9" if audit_promotion_current else
                    "0.5.8" if audit_candidate_review_current else "0.5.7"
                ) if audit_work_start_current else "0.5.6",
                "conditional_dossiers": {
                    "privacy_consent": "NOT_REQUIRED",
                    "content_media": "NOT_REQUIRED",
                    "audit_evidence": (
                        "REQUIRED / COMPLETE / CERTIFIED / CURRENT"
                        if audit_promotion_current
                        else
                        "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                        if audit_work_start_current
                        else "REQUIRED / NEXT / NOT_STARTED"
                    ),
                    "analytics": "NOT_REQUIRED",
                },
                "phase_7c_block_reason": (
                    "Successful Phase 7B reconciliation is required; Audit dossier authorship and current status are complete"
                    if audit_promotion_current
                    else "Audit & Evidence dossier must be COMPLETE / CERTIFIED / CURRENT and subsequent Phase 7B reconciliation must succeed"
                ),
                "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
                "completed_milestones": expected_fp001_state["completed_milestones"]
                + ["FP-001 PHASE 7A/7B CONDITIONAL-DOSSIER ADJUDICATION"]
                + (["FP-001 AUDIT & EVIDENCE v0.1.0 DOSSIER PROMOTION"] if audit_promotion_current else []),
            }
        )
        expected_fp001_state["audit_dossier"] = (
            "REQUIRED / COMPLETE / CERTIFIED / CURRENT"
            if audit_promotion_current
            else
            "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
            if audit_work_start_current
            else "REQUIRED / NEXT / NOT_STARTED"
        )
        if audit_work_start_current:
            expected_fp001_state.update(
                {
                    "audit_dossier_execution_tracker_issue": 116,
                    "audit_dossier_candidate": (
                        "COMPLETE / CERTIFIED / MERGED UNCHANGED"
                        if audit_promotion_current
                        else
                        "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
                        if audit_candidate_review_current
                        else "NOT_AUTHORED / NOT_CERTIFIED / NOT_CURRENT"
                    ),
                    "audit_dossier_work_start_baseline_main_sha": "332d51f19d77430fe4e95911920fe0c87cab524a",
                }
            )
            if audit_candidate_review_current:
                expected_fp001_state["audit_dossier_candidate_pr"] = 118
        if audit_promotion_current:
            expected_fp001_state.update(
                {
                    "phase_7b_reconciliation": (
                        "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
                        if reconciliation_candidate_current
                        else "NEXT / NOT_STARTED"
                    ),
                    "audit_certified_candidate_sha256": "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea",
                }
            )
            if reconciliation_candidate_current:
                expected_fp001_state.update(
                    {
                        "phase_7b_reconciliation_execution_tracker_issue": 120,
                        "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
                        "phase_7b_reconciliation_candidate": {
                            "path": "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
                            "version": "0.1.0",
                            "result": "PASS / READY FOR INDEPENDENT REVIEW",
                            "lifecycle": "NOT CERTIFIED / NOT CURRENT",
                            "certification": "PENDING FRESH INDEPENDENT EXACT-HEAD REVIEW",
                            "tracker_issue": 120,
                        },
                    }
                )
            if not re.fullmatch(
                r"PR #[1-9][0-9]* STATUS SUCCESSOR",
                str(lifecycle_state.get("audit_current_status_promotion", "")),
            ):
                issues.append("current Open Work does not bind Audit status promotion to an actual PR number")
    if reconciliation_certified_current:
        expected_fp001_state.update(
            {
                "status_successor_base_sha": "1a51755d505279821afe166b030be735fe0b6a1c" if phase7c_candidate_current else "3f4c9bf564b2b011e96171b8664428423eeba558" if tracker_closure_sync_current else "f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3",
                "current_stage": "FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
                "next_stage": "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE" if phase7c_candidate_current else "AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT",
                "status_successor_version": "0.5.13" if phase7c_candidate_current else "0.5.12" if tracker_closure_sync_current else "0.5.11",
                "phase_7b_reconciliation": "COMPLETE / CERTIFIED / CURRENT",
                "phase_7c": "IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING" if phase7c_candidate_current else "NEXT / NOT_STARTED",
                "application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
                "phase_7b_reconciliation_execution_tracker_issue": 120,
                **({"phase_7b_reconciliation_execution_tracker_state": "CLOSED / COMPLETED"} if tracker_closure_sync_current or phase7c_candidate_current else {}),
                "phase_7b_reconciliation_baseline_main_sha": "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
                "phase_7b_reconciliation_candidate": {
                    "path": "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
                    "current_status_successor_path": "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
                    "version": "0.1.0",
                    "result": "PASS / READY FOR INDEPENDENT REVIEW",
                    "lifecycle": "CERTIFIED / CURRENT",
                    "certification": "COMPLETE; EXACT CANDIDATE MERGED UNCHANGED; RESULTING-MAIN VERIFIED",
                    "tracker_issue": 120,
                },
                "audit_current_status_promotion": "PR #119 STATUS SUCCESSOR",
                "audit_certified_candidate_sha256": "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea",
                "current_delivery_atlas": "working/DELIVERY_ATLAS_WORKING_v0.4.11.md" if phase7c_candidate_current else "working/DELIVERY_ATLAS_WORKING_v0.4.10.md",
                "current_fp001_skeleton": "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.13.md" if phase7c_candidate_current else "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.12.md",
                "current_harden_02": "working/HARDEN-02_CONTRACT_WORKING_v0.5.13.md" if phase7c_candidate_current else "working/HARDEN-02_CONTRACT_WORKING_v0.5.12.md",
            }
        )
        if phase7c_candidate_current:
            expected_fp001_state.update(
                {
                    "phase_7c_execution_tracker_issue": 124,
                    "phase_7c_execution_tracker_state": "OPEN",
                    "phase_7c_contract_candidate": {
                        "path": "docs/00_platform/working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md",
                        "version": "0.1.0",
                        "lifecycle": "CANDIDATE / NOT CERTIFIED / NOT CURRENT",
                        "authored": True,
                        "certification": "PENDING",
                        "current_status_promotion": "PENDING",
                    },
                    "programme_router_issue_111_state": "OPEN",
                    "downstream_route": [
                        "FP-001 PHASE 7A: COMPLETE",
                        "REQUIRED JIT DOSSIER SET: DISPOSITION-COMPLETE",
                        "FP-001 PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
                        "PHASE 7C FINAL FEATURE PACK CONTRACT: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
                        "FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: CANDIDATE / NOT CERTIFIED / NOT CURRENT",
                        "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE",
                        "SEPARATE CERTIFICATION AND CURRENT-STATUS PROMOTION",
                        "PROOF CLASSIFICATION: NOT FINALISED",
                        "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
                    ],
                }
            )
        expected_fp001_state.pop("phase_7c_block_reason", None)
    if not isinstance(lifecycle_state, dict) or any(
        lifecycle_state.get(key) != value for key, value in expected_fp001_state.items()
    ):
        issues.append("current Open Work lifecycle state advances beyond certified FP-001 reconciliation or omits its exact stage/evidence boundaries")
    expected_fp001_evidence = {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/67",
        "candidate_sha": "79d0540c66f0224ece0330181e61dfef8ab4b458",
        "prior_main_sha": "38022caea64cb2522ab8fc4db730099a94cd6600",
        "resulting_main_sha": "4000ae50660930114e3ad43108dc029fd0673d32",
        "candidate_tree_sha": "a71dbeb2cca79bea0013f9997e40f34769f262f3",
        "exact_head_ci_run": "36991113390",
        "resulting_main_ci_run": "37009244020",
        "pre_merge_attestation_comment": "5952693308",
        "post_merge_attestation_comment": "5955641536",
        "post_merge_independent_review": "PASS",
    }
    if lifecycle_state.get("fp001_reconciliation_certification") != expected_fp001_evidence:
        issues.append("current Open Work does not bind the complete verified PR #67 reconciliation certification evidence")

    expected_identity_evidence = {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/70",
        "candidate_head_sha": "613ea1d52f6ffdadb3910cee3c62ea5dbd88f583",
        "candidate_tree_sha": "421b9c1670586699e12807bc28f01179ca755fa7",
        "prior_main_sha": "d9174de272ac7b98c5a14f0d55c60c80e15759fb",
        "resulting_main_sha": "df6190a06bdc8aa4b99f6ed3a18cb9e3e12e22fb",
        "resulting_main_tree_sha": "421b9c1670586699e12807bc28f01179ca755fa7",
        "candidate_merged_unchanged": True,
        "candidate_to_resulting_main_changed_files": 0,
        "exact_head_ci_run": "37198148095",
        "exact_head_ci_result": "PASS / 287 TESTS / 535 FIA ASSERTIONS / ZERO FINDINGS",
        "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/70#issuecomment-5980442552",
        "exact_head_independent_review": "PASS",
        "resulting_main_ci_run": "37205571249",
        "resulting_main_ci_result": "PASS / 287 TESTS / 535 FIA ASSERTIONS / ZERO FINDINGS",
        "post_merge_independent_review": "PASS",
        "post_merge_independent_review_actor": "ChatGPT / GPT-5.6 Sol",
        "post_merge_attestation_poster": "JCSchoeman96",
        "post_merge_poster_equals_pr_author_disclosed": True,
        "post_merge_review_actor_authored_or_modified_candidate": False,
        "post_merge_substantive_reviewer_is_review_actor_not_poster": True,
        "post_merge_attestation": "COMPLETE",
        "post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/70#issuecomment-5981764432",
    }
    expected_identity_v014_certification = {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/76",
        "candidate_head_sha": "b349202f79825b641bf73ffe943da497a247e120",
        "candidate_base_sha": "3f06eafe58c2cc441a090e804b4169c1c3c4ca2b",
        "resulting_main_sha": "90f96ba3452c95112bf6ec4ce5bb897676adbed4",
        "candidate_tree_sha": "44ad689e46e823e4f453b32edd39306d99c62015",
        "resulting_main_tree_sha": "44ad689e46e823e4f453b32edd39306d99c62015",
        "candidate_merged_unchanged": True,
        "candidate_to_resulting_main_changed_files": 0,
        "exact_head_ci_run": "37419452502",
        "exact_head_ci_result": "PASS / 291 TESTS / 541 FIA ASSERTIONS / ZERO FINDINGS",
        "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/76#issuecomment-6010805470",
        "pre_merge_independent_review": "PASS",
        "pre_merge_independent_review_actor": "ChatGPT / GPT-5.6 Sol",
        "pre_merge_attestation_poster": "JCSchoeman96",
        "pre_merge_poster_equals_pr_author_disclosed": True,
        "pre_merge_review_actor_authored_or_modified_candidate": False,
        "pre_merge_substantive_reviewer_is_review_actor_not_poster": True,
        "resulting_main_ci_run": "37425057900",
        "resulting_main_ci_result": "PASS / 291 TESTS / 541 FIA ASSERTIONS / ZERO FINDINGS",
        "post_merge_independent_review": "PASS",
        "post_merge_independent_review_actor": "ChatGPT / GPT-5.6 Sol",
        "post_merge_attestation_poster": "JCSchoeman96",
        "post_merge_poster_equals_pr_author_disclosed": True,
        "post_merge_review_actor_authored_or_modified_candidate": False,
        "post_merge_substantive_reviewer_is_review_actor_not_poster": True,
        "post_merge_attestation": "COMPLETE",
        "post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/76#issuecomment-6011044499",
    }
    if lifecycle_state.get("identity_v014_promotion_certification") != expected_identity_v014_certification:
        issues.append("current Open Work does not bind exact PR #76 CI, attestation and reviewer/poster evidence")
    expected_communications_v010_certification = {
        "pr_url": "https://github.com/JCSchoeman96/NewYou/pull/78",
        "candidate_head_sha": "8623fd622fb40e3fa1ec1c2540f1ad228dc57e65",
        "candidate_base_sha": "ff1ff5c64b764fc4229e4dccfc46e58482d2b3d0",
        "candidate_tree_sha": "a83cf3f939f72fc3e33c80db52986ef80fe76a35",
        "resulting_main_sha": "a062bd56e3ae94e815e2991ee00bf133ee9f3b56",
        "resulting_main_tree_sha": "a83cf3f939f72fc3e33c80db52986ef80fe76a35",
        "candidate_merged_unchanged": True,
        "candidate_to_resulting_main_changed_files": 0,
        "exact_head_ci_run": "37609981185",
        "exact_head_ci_result": "PASS",
        "pre_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/78#issuecomment-6036677517",
        "pre_merge_independent_review": "PASS",
        "resulting_main_ci_run": "37612931207",
        "resulting_main_ci_result": "PASS",
        "post_merge_independent_review": "PASS",
        "post_merge_attestation": "COMPLETE",
        "post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/78#issuecomment-6038969688",
    }
    if lifecycle_state.get("communications_v010_promotion_certification") != expected_communications_v010_certification:
        issues.append("current Open Work does not bind exact PR #78 CI, attestation and reviewer/poster evidence")
    identity_certification = lifecycle_state.get("identity_durable_delivery_certification")
    expected_identity_attestation_url = (
        "https://github.com/JCSchoeman96/NewYou/pull/70#issuecomment-5981764432"
    )
    if (
        not isinstance(identity_certification, dict)
        or identity_certification.get("post_merge_attestation_url")
        != expected_identity_attestation_url
    ):
        issues.append(
            "current Open Work must bind PR #70 durable post-merge attestation to its exact GitHub comment URL"
        )
    if identity_certification != expected_identity_evidence:
        issues.append("current Open Work does not bind the complete PR #70 durable-delivery certification evidence")

    if not identity_predecessor.is_file() or not identity_promotion_candidate.is_file():
        issues.append("Identity v0.1.2 predecessor and exact PR #70 candidate archives are required")
    if not superseded_identity_current.is_file() or not identity_v014_candidate.is_file():
        issues.append("superseded promoted/current v0.1.3 and exact PR #76 candidate archives are required")
    if (docs / "working" / "candidates" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md").exists() or (docs / "working" / "candidates" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").exists():
        issues.append("promoted Identity dossier remains in a candidate route")
    j1_heading = "### J.1 Narrow Identity/Communications durable-delivery correction"
    j1a_heading = "### J.1a Automated retrieval / scanner-safe proof consumption"
    j2_heading = "### J.2 Technical evidence and certification boundary"
    if j1_heading in dossier_text and j2_heading in dossier_text:
        active_j1 = dossier_text.split(j1_heading, 1)[1].split(j1a_heading if j1a_heading in dossier_text else j2_heading, 1)[0]
        candidate_j1 = identity_promotion_candidate_text.split(j1_heading, 1)[1].split(j2_heading, 1)[0] if j1_heading in identity_promotion_candidate_text and j2_heading in identity_promotion_candidate_text else ""
        snapshot_j1 = superseded_identity_current_text.split(j1_heading, 1)[1].split(j2_heading, 1)[0] if j1_heading in superseded_identity_current_text and j2_heading in superseded_identity_current_text else ""
        if not candidate_j1 or active_j1 != candidate_j1 or active_j1 != snapshot_j1:
            issues.append("active J.1 differs from exact PR #70 candidate or superseded promoted/current v0.1.3 snapshot")
    else:
        issues.append("active Identity dossier is missing the PR #70 durable-delivery correction")

    j1a_heading = "### J.1a Automated retrieval / scanner-safe proof consumption"
    if j1a_heading in dossier_text and "### J.2 Technical evidence and certification boundary" in dossier_text:
        active_j1a = dossier_text.split(j1a_heading, 1)[1].split("### J.2 Technical evidence and certification boundary", 1)[0]
        candidate_j1a = identity_v014_candidate_text.split(j1a_heading, 1)[1].split("### J.2 Technical evidence and certification boundary", 1)[0] if j1a_heading in identity_v014_candidate_text and "### J.2 Technical evidence and certification boundary" in identity_v014_candidate_text else ""
        if not candidate_j1a or active_j1a != candidate_j1a:
            issues.append("active scanner-safe proof-consumption correction differs from exact PR #76 candidate")
    else:
        issues.append("current Identity v0.1.4 dossier is missing J.1a")
    for token in (
        "Content & Media owns the governed message/template content versions",
        "publication/eligibility lifecycle",
        "Communications consumes the exact eligible content/locale version for delivery and owns the corresponding delivery binding/provenance",
        "automated retrieval is never sufficient authority to consume the Identity proof",
        "explicit participant confirmation/action",
        "Identity re-reads current proof + current source state",
        "existing single-use/conditional-update boundary",
        "MessageIntent",
        "DeliveryAttempt",
    ):
        if token.casefold() not in dossier_text.casefold():
            issues.append(f"Identity v0.1.4 correction meaning is missing: {token}")

    identity_evidence = (
        "613ea1d52f6ffdadb3910cee3c62ea5dbd88f583",
        "421b9c1670586699e12807bc28f01179ca755fa7",
        "d9174de272ac7b98c5a14f0d55c60c80e15759fb",
        "df6190a06bdc8aa4b99f6ed3a18cb9e3e12e22fb",
        "37198148095",
        "37205571249",
        "287 tests, 535 assertions, zero findings",
        "https://github.com/JCSchoeman96/NewYou/pull/70#issuecomment-5980442552",
        "CERTIFIED / CURRENT",
        "COMMUNICATIONS FINALISATION: BLOCKED / STOP",
        "b349202f79825b641bf73ffe943da497a247e120",
        "3f06eafe58c2cc441a090e804b4169c1c3c4ca2b",
        "90f96ba3452c95112bf6ec4ce5bb897676adbed4",
        "44ad689e46e823e4f453b32edd39306d99c62015",
        "37419452502",
        "37425057900",
        "291 tests, 541 assertions, zero findings",
        "https://github.com/JCSchoeman96/NewYou/pull/76#issuecomment-6010805470",
        "https://github.com/JCSchoeman96/NewYou/pull/76#issuecomment-6011044499",
    )
    for token in identity_evidence:
        if token not in dossier_text:
            issues.append(f"active Identity dossier omits required PR #70/#76 certification evidence: {token}")

    def marked_block(text: str, name: str) -> str:
        start_marker = "<!-- NEWYOU:" + name + ":START -->"
        end_marker = "<!-- NEWYOU:" + name + ":END -->"
        if text.count(start_marker) != 1 or text.count(end_marker) != 1:
            return ""
        return text.split(start_marker, 1)[1].split(end_marker, 1)[0]

    skeleton_pmr = marked_block(skeleton_text, "FP001-PMR-RECONCILIATION-CONTRACT")
    dossier_pmr = marked_block(dossier_text, "FP001-PMR-RECONCILIATION-CONTRACT")
    skeleton_candidate_pmr = marked_block(skeleton_candidate_text, "FP001-PMR-RECONCILIATION-CONTRACT")
    dossier_candidate_pmr = marked_block(dossier_candidate_text, "FP001-PMR-RECONCILIATION-CONTRACT")
    if not skeleton_pmr or not dossier_pmr:
        issues.append("each certified successor must contain exactly one marked PMR reconciliation contract")
    if skeleton_candidate.is_file() and skeleton_pmr != skeleton_candidate_pmr:
        issues.append("certified skeleton PMR normative contract differs from the PR #67 candidate")
    if dossier_candidate.is_file() and dossier_pmr != dossier_candidate_pmr:
        issues.append("certified Identity dossier PMR normative contract differs from the PR #67 candidate")

    required_skeleton = (
        "required human-facing Platform Member Reference (PMR)",
        "exactly one canonical active PMR under Identity & Access ownership",
        "not database identity",
        "not authentication",
        "not authorisation",
        "not verification assurance",
        "not paid Membership",
        "not subscription state",
        "not entitlement",
        "not payment authority",
        "not a voucher/coupon/discount authority",
        "not a bearer credential",
        "non-secret but private-by-default",
        "Possession proves none",
        "Active PMR uniqueness is preserved",
        "Ordinary PMR values are immutable",
        "Legitimate reactivation retains",
        "never reassigned or reused",
        "duplicate-account reconciliation",
        "collision-safe",
        "concurrency-correct",
        "retry-safe",
        "purpose-scoped",
        "minimum-disclosure",
        "non-authoritative",
        "beneficiary key",
        "ARQ-IAM-013",
        "representation remains unfrozen",
        "Failed, partial or ambiguous Account creation does not create an externally usable PMR",
    )
    required_dossier = (
        "Identity & Access Account truth",
        "only after successful individual Account creation",
        "one canonical active PMR per canonical individual Account",
        "A failed, partial or ambiguous Account creation does not assign an externally usable PMR",
        "retries converge on the one committed Account/reference result",
        "The PMR is stable and human-facing.",
        "not database identity",
        "not authentication",
        "not authorisation",
        "not verification assurance",
        "not paid Membership",
        "not subscription state",
        "not entitlement",
        "not payment authority",
        "not a voucher/coupon/discount authority",
        "not a bearer credential",
        "non-secret but private-by-default",
        "Possession of a PMR proves none",
        "Ordinary PMR values are immutable",
        "reactivation retains",
        "never reassign or reuse it",
        "Duplicate-account reconciliation",
        "collision-safe",
        "concurrency-correct",
        "idempotent",
        "purpose-scoped",
        "minimum-disclosure",
        "non-authoritative",
        "beneficiary key",
        "ARQ-IAM-013",
        "representation remains unfrozen",
    )
    for token in required_skeleton:
        source = skeleton_text if token in required_skeleton[:2] else skeleton_pmr
        if token.casefold() not in source.casefold():
            issues.append(f"skeleton PMR block omits required meaning: {token}")
    for token in required_dossier:
        if token.casefold() not in dossier_pmr.casefold():
            issues.append(f"Identity dossier PMR block omits required meaning: {token}")

    frozen_representation = re.compile(
        r"(?i)\b(?:prefix|alphabet|grouping|length|checksum|check\s+algorithm|generator|schema|index\s+strategy|database\s+representation|Ash\s+Resource|field\s+shape|implementation\s+package)\b\s*(?:is|are|=|:|set\s+to|fixed\s+to|selected\s+as)"
    )
    if frozen_representation.search(skeleton_pmr) or frozen_representation.search(dossier_pmr):
        issues.append("PMR reconciliation freezes an exact representation")
    lifecycle_dimensions = (
        "orthogonal account, verification and security dimensions",
        "Authentication credential",
        "Verification, reset, magic-link and recovery proof",
        "Application session",
        "Graduated recovery",
        "Platform Member Reference",
        "Duplicate reconciliation",
    )
    for token in lifecycle_dimensions:
        if token.casefold() not in dossier_text.casefold():
            issues.append(f"Identity lifecycle dimension is missing or collapsed: {token}")

    def oq_references(text: str) -> tuple[str, ...]:
        return tuple(re.findall(r"\bOQ-\d{3}\b", text))

    if oq_references(skeleton_text) != oq_references(skeleton_candidate_text):
        issues.append("OQ classifications or OQ references changed during status promotion")
    active_identity_semantics = dossier_text.split("## A. Baseline and scope", 1)
    candidate_identity_semantics = identity_v014_candidate_text.split("## A. Baseline and scope", 1)
    if len(active_identity_semantics) != 2 or len(candidate_identity_semantics) != 2 or oq_references(active_identity_semantics[-1]) != oq_references(candidate_identity_semantics[-1]):
        issues.append("Identity dossier OQ references changed during status promotion")
    if (
        "OQ-034" not in skeleton_text
        or "proof execution has not started" not in skeleton_text.casefold()
        or "classification is complete as new_tracer_bullet" not in skeleton_text.casefold()
    ):
        issues.append("OQ-034 architecture selection or incomplete Phase 8 proof boundary changed")
    for token in ("OQ-035", "BLOCKS_RELEASE_ONLY", "OQ-036", "OQ-038"):
        if token not in skeleton_text:
            issues.append(f"preserved OQ gate evidence is missing: {token}")
    for oq in ("OQ-035", "OQ-036"):
        if re.findall(rf"(?m)^\| `{oq}` \| `([^`]+)` \|", skeleton_text) != ["BLOCKS_RELEASE_ONLY"]:
            issues.append(f"{oq} must remain BLOCKS_RELEASE_ONLY in the current FP-001 gate manifest")
    if "| " + chr(96) + "OQ-038" + chr(96) + " | " + chr(96) + "FUTURE_ONLY" not in skeleton_text:
        issues.append("OQ-038 status changed")

    if not skeleton_candidate.is_file() or not dossier_candidate.is_file():
        issues.append("PR #67 candidate archives are required for byte preservation and provenance")

    stage = open_work.split("# 9. Immediate Next Action", 1)
    stage = stage[1].split("# 10. Minimal Tools", 1)[0] if len(stage) == 2 else ""
    next_routes = re.findall(r"(?m)^NEXT STAGE:\s*(.*?)\s*$", stage)
    expected_next_route = (
        "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE"
        if phase7c_candidate_current
        else "AUTHOR FP-001 PHASE 7C FINAL FEATURE PACK CONTRACT (NOT_STARTED)"
        if reconciliation_certified_current
        else
        "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
        if reconciliation_candidate_current
        else "FP-001 PHASE 7B RECONCILIATION"
        if audit_promotion_current
        else (
            "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"
            if audit_candidate_review_current
            else "AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE"
        )
        if audit_work_start_current
        else "FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER"
        if adjudication_current
        else "REMAINING REQUIRED / CONDITIONAL PHASE 7B"
    )
    if next_routes != [expected_next_route]:
        issues.append("current Open Work NEXT route does not name the single remaining required Phase 7B action")
    required_stage_tokens = [
        "CURRENT AUTHORITY-STAGE PROGRAMME: " + (
            lifecycle_state.get("current_stage")
            if adjudication_current
            else "COMMUNICATIONS v0.1.0 CURRENT-STATUS PROMOTION"
        ),
        "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
        "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
        "COMMUNICATIONS v0.1.0 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
        "COMMUNICATIONS v0.1.0 CURRENT-STATUS PROMOTION SOURCE: PR #81 STATUS SUCCESSOR; PR #78 CANDIDATE AND POST-MERGE CERTIFICATION EVIDENCE: COMPLETE",
        "COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0",
        "COMMUNICATIONS FINALISATION: BLOCKED / STOP",
        "- COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
        "OPEN GATES: OQ-035 SECURITY / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY; OQ-036 VENDOR / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
        "STORE / CER: EXCLUDED FROM HARDEN-02",
    ]
    if reconciliation_certified_current:
        required_stage_tokens.extend(
            [
                "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
                "RECONCILIATION v0.1.0: CERTIFIED / CURRENT",
                "RECONCILIATION v0.1.0: CERTIFIED / CURRENT — `working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md`; immutable candidate: `archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md`",
            ]
        )
        required_stage_tokens.extend(
            [
                "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
                "PHASE 7C TRACKER #124: OPEN",
                "PHASE 7C CONTRACT CANDIDATE: working/FP-001_FINAL_FEATURE_PACK_CONTRACT_WORKING_v0.1.0.md; CANDIDATE / NOT CERTIFIED / NOT CURRENT",
                "NEXT PHASE 7 ACTION: FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE; STATUS: PENDING",
            ] if phase7c_candidate_current else ["PHASE 7C: NEXT / NOT_STARTED"]
        )
    if reconciliation_candidate_current:
        required_stage_tokens.extend(
            [
                "PHASE 7B RECONCILIATION: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING",
                "RECONCILIATION CANDIDATE: NOT CERTIFIED / NOT CURRENT",
                "RECONCILIATION EXECUTION TRACKER: #120 OPEN — links #111, completed #114 and completed #116",
            ]
        )
    if adjudication_current:
        required_stage_tokens.extend(
            [
                "- PRIVACY & CONSENT: NOT_REQUIRED",
                "- CONTENT & MEDIA: NOT_REQUIRED",
                "- AUDIT & EVIDENCE: " + (
                    "REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0"
                    if audit_promotion_current
                    else
                    "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
                    if audit_work_start_current
                    else "REQUIRED / NEXT / NOT_STARTED"
                ),
                *(
                    (
                        "AUDIT DOSSIER CANDIDATE: " + (
                            "COMPLETE / CERTIFIED / MERGED UNCHANGED"
                            if audit_promotion_current
                            else
                            "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
                            if audit_candidate_review_current
                            else "NOT AUTHORED / NOT CERTIFIED / NOT CURRENT"
                        ),
                        "AUDIT DOSSIER EXECUTION TRACKER: #116",
                        "AUDIT DOSSIER WORK-START BASELINE MAIN SHA: `332d51f19d77430fe4e95911920fe0c87cab524a`",
                        *( ("AUDIT DOSSIER CANDIDATE PR: #118",) if audit_candidate_review_current else () ),
                    )
                    if audit_work_start_current
                    else ()
                ),
                "- ANALYTICS: NOT_REQUIRED",
                (
                    "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
                    if phase7c_candidate_current
                    else "PHASE 7C: NEXT / NOT_STARTED"
                )
                if reconciliation_certified_current
                else "PHASE 7C: BLOCKED / NOT_STARTED UNTIL SUCCESSFUL PHASE 7B RECONCILIATION"
                if audit_promotion_current
                else "PHASE 7C: BLOCKED / NOT_STARTED UNTIL AUDIT DOSSIER COMPLETE / CERTIFIED / CURRENT AND PHASE 7B RECONCILIATION SUCCEEDS",
            ]
        )
    else:
        required_stage_tokens.extend(
            [
                "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
                "PHASE 7C: BLOCKED / NOT_STARTED PENDING CONDITIONAL-DOSSIER DISPOSITIONS",
            ]
        )
    for token in required_stage_tokens:
        if token not in stage:
            issues.append(f"Open Work current status or later-gate boundary changed: {token}")
    expected_communications_dossier_status = "COMPLETE / CERTIFIED / CURRENT v0.1.0"
    if re.findall(r"(?m)^COMMUNICATIONS DOSSIER:\s*(.*?)\s*$", stage) != [expected_communications_dossier_status]:
        issues.append("Open Work Communications dossier current route is missing, duplicated or inconsistent with certified dossier work")
    if re.findall(r"(?m)^- COMMUNICATIONS:\s*(.*?)\s*$", stage) != ["REQUIRED / " + expected_communications_dossier_status]:
        issues.append("Open Work Communications required-dossier route is missing, duplicated or inconsistent with certified dossier work")
    forbidden_advancement = (
        ("Communications finalisation", r"(?im)^.*COMMUNICATIONS FINALISATION\s*:\s*(?:COMPLETE|CERTIFIED|UNBLOCKED|AUTHORI[ZS]ED).*$"),
        ("conditional dossiers", r"(?im)^.*CONDITIONAL DOSSIERS:.*\b(?:COMPLETE|CERTIFIED|ADJUDICATED)\b.*$"),
        ("Phase 7C", r"(?im)^.*PHASE 7C\s*:\s*(?:NEXT|READY|UNBLOCKED|COMPLETE|CERTIFIED|AUTHORI[ZS]ED).*$"),
        ("proof classification", r"(?im)^.*PROOF CLASSIFICATION\s*:\s*(?:FINAL|FINALI[ZS]ED|CERTIFIED).*$"),
        ("Phase 8/application implementation", r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$"),
        ("Store/CER", r"(?im)^.*STORE\s*/\s*CER\s*:\s*(?:INCLUDED|REQUIRED|AUTHORI[ZS]ED|COMPLETE).*$"),
    )
    for label, pattern in forbidden_advancement:
        if label == "Phase 7C" and reconciliation_certified_current:
            continue
        if re.search(pattern, stage):
            issues.append(f"{label} advanced during the FP-001 status successor")
    if "FP001_RECONCILIATION_REQUIRED: REQUIRED / NEXT / NOT PERFORMED" in stage:
        issues.append("certified reconciliation still says NOT PERFORMED")
    if re.search(r"(?im)^.*COMMUNICATIONS DOSSIER STARTED:\s*YES.*$", skeleton_text + dossier_text):
        issues.append("Communications dossier is marked started")
    if not communications_dossier.is_file():
        issues.append("certified Communications dossier is missing")
    elif "**Status:** `CERTIFIED / CURRENT`" not in communications_dossier_text:
        issues.append("Communications dossier is not marked CERTIFIED / CURRENT")
    comm_semantic_marker = "## 1. Authority, baseline and post-Identity delta"
    active_comm_semantics = communications_dossier_text.split(comm_semantic_marker, 1)
    candidate_comm_semantics = communications_v010_candidate_text.split(comm_semantic_marker, 1)
    if (
        len(active_comm_semantics) != 2
        or len(candidate_comm_semantics) != 2
        or active_comm_semantics[1] != candidate_comm_semantics[1]
    ):
        issues.append("Communications dossier semantic body changed during status promotion")

    readme_route = (
        "Current programme status is in Open Work v1.2.69."
        if phase7c_candidate_current
        else "Current programme status is in Open Work v1.2.68."
        if reconciliation_certified_current
        else "Current programme status is in Open Work v1.2.66."
        if reconciliation_candidate_current
        else "Current programme status is in Open Work v1.2.65."
        if audit_promotion_current
        else "Current programme status is in Open Work v1.2.64."
        if audit_candidate_review_current
        else "Current programme status is in Open Work v1.2.63."
        if audit_work_start_current
        else "Current programme status is in Open Work v1.2.62."
        if adjudication_current
        else "Current programme status is in Open Work v1.2.61.",
        "PR #67 PMR reconciliation is COMPLETE / CERTIFIED",
        "PR #76 candidate certification and completed post-merge certification evidence are COMPLETE / CERTIFIED",
        "The separate PR #77 status successor records Identity v0.1.4 as CERTIFIED / CURRENT",
        "- IDENTITY v0.1.4: CERTIFIED / CURRENT under the separate PR #77 status successor; PR #76 candidate and post-merge certification evidence are COMPLETE",
        "PR #78 candidate certification and post-merge certification evidence are COMPLETE / CERTIFIED",
        "separate PR #81 status successor records Communications dossier v0.1.0 as CERTIFIED / CURRENT",
    )
    for token in readme_route:
        if token not in readme:
            issues.append(f"README current route is missing or stale: {token}")
    if "PR #76 promotes Identity v0.1.4 to CURRENT" in readme:
        issues.append("README current route still attributes Identity current-status promotion to PR #76")

    open_work_provenance_heading = (
        "## 12.14 — PR #76 candidate certification and post-merge evidence; PR #77 current-status promotion"
    )
    open_work_provenance = (
        "PR #76 certified the v0.1.4 candidate and supplied completed post-merge certification evidence. "
        "It did not make v0.1.4 current. This separate PR #77 status successor records the current-status "
        "promotion; the resulting Identity state is CERTIFIED / CURRENT."
    )
    open_work_sections = list(re.finditer(r"(?m)^## 12\.14[^\n]*$", open_work))
    if len(open_work_sections) == 1:
        section_start = open_work_sections[0].start()
        next_section = re.search(r"(?m)^##\s+", open_work[section_start + 1 :])
        section_end = (
            section_start + 1 + next_section.start()
            if next_section is not None
            else len(open_work)
        )
        section_text = open_work[section_start:section_end]
    else:
        section_text = ""
    if (
        len(open_work_sections) != 1
        or open_work_sections[0].group(0) != open_work_provenance_heading
        or section_text.count(open_work_provenance) != 1
        or "PR #76 certification/promotion" in section_text
    ):
        issues.append(
            "Open Work §12.14 does not separate PR #76 candidate/post-merge certification evidence from the PR #77 current-status successor"
        )
    readme_active_routes = (
        "4. " + chr(96) + (
            "02_OPEN_WORK_v1.2.69.md" if phase7c_candidate_current else
            "02_OPEN_WORK_v1.2.68.md" if reconciliation_certified_current else
            "02_OPEN_WORK_v1.2.66.md" if reconciliation_candidate_current else
            "02_OPEN_WORK_v1.2.65.md" if audit_promotion_current else
            "02_OPEN_WORK_v1.2.64.md" if audit_candidate_review_current else
            "02_OPEN_WORK_v1.2.63.md" if audit_work_start_current else
            "02_OPEN_WORK_v1.2.62.md" if adjudication_current else "02_OPEN_WORK_v1.2.61.md"
        ) + chr(96),
        chr(96) + (
            "working/DELIVERY_ATLAS_WORKING_v0.4.11.md" if phase7c_candidate_current else
            "working/DELIVERY_ATLAS_WORKING_v0.4.10.md" if reconciliation_certified_current else
            "working/DELIVERY_ATLAS_WORKING_v0.4.8.md" if reconciliation_candidate_current else
            "working/DELIVERY_ATLAS_WORKING_v0.4.7.md" if audit_promotion_current else
            "working/DELIVERY_ATLAS_WORKING_v0.4.6.md" if audit_candidate_review_current else
            "working/DELIVERY_ATLAS_WORKING_v0.4.5.md" if audit_work_start_current else
            "working/DELIVERY_ATLAS_WORKING_v0.4.4.md" if adjudication_current else "working/DELIVERY_ATLAS_WORKING_v0.4.3.md"
        ) + chr(96) + " — derived Delivery Atlas",
        chr(96) + (
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.13.md" if phase7c_candidate_current else
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.12.md" if reconciliation_certified_current else
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.10.md" if reconciliation_candidate_current else
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.9.md" if audit_promotion_current else
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.8.md" if audit_candidate_review_current else
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.7.md" if audit_work_start_current else
            "working/HARDEN-02_CONTRACT_WORKING_v0.5.6.md" if adjudication_current else "working/HARDEN-02_CONTRACT_WORKING_v0.5.5.md"
        ) + chr(96) + " — preserves certified HARDEN-02",
        chr(96) + (
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.13.md" if phase7c_candidate_current else
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.12.md" if reconciliation_certified_current else
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md" if reconciliation_candidate_current else
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.9.md" if audit_promotion_current else
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md" if audit_candidate_review_current else
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.7.md" if audit_work_start_current else
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.6.md" if adjudication_current else "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md"
        ) + chr(96),
        chr(96) + "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md" + chr(96) + " — certified/current",
        chr(96) + "working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md" + chr(96),
        *( (chr(96) + "working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md" + chr(96)) if audit_promotion_current else () ),
    )
    for token in readme_active_routes:
        if token not in readme:
            issues.append(f"README active route is missing or stale: {token}")

    open_work_comm_provenance_heading = (
        "## 12.16 — PR #78 candidate certification and post-merge evidence; PR #81 current-status promotion"
    )
    open_work_comm_provenance = (
        "PR #78 certified the v0.1.0 candidate and supplied completed post-merge certification evidence. "
        "It did not make v0.1.0 current. This separate PR #81 status successor records the current-status "
        "promotion; the resulting Communications dossier state is CERTIFIED / CURRENT."
    )
    if open_work_comm_provenance not in open_work or open_work_comm_provenance_heading not in open_work:
        issues.append(
            "Open Work §12.16 does not separate PR #78 candidate/post-merge certification evidence from the PR #81 current-status successor"
        )
    if re.search(
        r"PR #78 certified candidate `8623fd622fb40e3fa1ec1c2540f1ad228dc57e65` based on `a062bd56e3ae94e815e2991ee00bf133ee9f3b56`",
        open_work,
    ):
        issues.append("Open Work §12.16 records PR #78 resulting main as the reviewed merge base")
    comm_cert = lifecycle_state.get("communications_v010_promotion_certification")
    if not isinstance(comm_cert, dict) or comm_cert.get("candidate_base_sha") != "ff1ff5c64b764fc4229e4dccfc46e58482d2b3d0":
        issues.append("Open Work does not bind PR #78 merge base separately from resulting main")
    open_work_section_matches = list(re.finditer(r"(?m)^## 12\.1[56][^\n]*$", open_work))
    if len(open_work_section_matches) < 2:
        issues.append("Open Work Communications lifecycle sections are missing or malformed")
    elif open_work_section_matches[0].group(0) != "## 12.15 — Communications JIT dossier work start (historical predecessor record)":
        issues.append("Open Work §12.15 must precede §12.16 and be labelled as historical predecessor evidence")
    elif open_work_section_matches[1].group(0) != open_work_comm_provenance_heading:
        issues.append("Open Work §12.16 must follow the historical §12.15 predecessor record")
    section_1215_start = open_work.find("## 12.15 — Communications JIT dossier work start")
    section_1216_start = open_work.find(open_work_comm_provenance_heading)
    if section_1215_start >= 0 and section_1216_start > section_1215_start:
        section_1215_text = open_work[section_1215_start:section_1216_start]
        if re.search(
            r"(?im)Its status is IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
            section_1215_text,
        ) or re.search(r"(?im)remains NOT CERTIFIED / NOT CURRENT until", section_1215_text):
            issues.append(
                "Open Work §12.15 still reads as live Communications IN PROGRESS / NOT CERTIFIED state"
            )
    if re.search(
        r"(?im)Communications Phase 7B work has begun with the FP-001 Communications JIT Domain Dossier candidate in PR #78\. Its status is",
        open_work,
    ):
        issues.append("Open Work retains a live Communications work-start state after promotion")

    atlas_version = "0.4.11" if phase7c_candidate_current else "0.4.10" if tracker_closure_sync_current else "0.4.9" if reconciliation_certified_current else "0.4.8" if reconciliation_candidate_current else "0.4.7" if audit_promotion_current else "0.4.6" if audit_candidate_review_current else "0.4.5" if audit_work_start_current else "0.4.4" if adjudication_current else "0.4.3"
    atlas_path = docs / "working" / f"DELIVERY_ATLAS_WORKING_v{atlas_version}.md"
    atlas = atlas_path.read_text(encoding="utf-8") if atlas_path.is_file() else ""
    atlas_header = _markdown_header_metadata(atlas, f"# Delivery Atlas working v{atlas_version}")
    atlas_predecessors = _metadata_values(atlas_header, "Predecessor")
    atlas_transitions = _metadata_values(atlas_header, "SemVer transition")
    all_atlas_predecessors = _metadata_declarations(atlas, "Predecessor")
    all_atlas_transitions = _metadata_declarations(atlas, "SemVer transition")
    if (
        len(all_atlas_predecessors) != 1
        or len(atlas_predecessors) != 1
        or all_atlas_predecessors != atlas_predecessors
        or not atlas_predecessors[0].startswith(
            ("`archive/DELIVERY_ATLAS_WORKING_v0.4.10.md`" if phase7c_candidate_current else "`archive/DELIVERY_ATLAS_WORKING_v0.4.9.md`" if tracker_closure_sync_current else "`archive/DELIVERY_ATLAS_WORKING_v0.4.8.md`" if reconciliation_certified_current else "`archive/DELIVERY_ATLAS_WORKING_v0.4.7.md`" if reconciliation_candidate_current else "`archive/DELIVERY_ATLAS_WORKING_v0.4.6.md`" if audit_promotion_current else "`archive/DELIVERY_ATLAS_WORKING_v0.4.5.md`" if audit_candidate_review_current else "`archive/DELIVERY_ATLAS_WORKING_v0.4.4.md`") if audit_work_start_current else
            "`archive/DELIVERY_ATLAS_WORKING_v0.4.3.md`" if adjudication_current else "`archive/DELIVERY_ATLAS_WORKING_v0.4.2.md`"
        )
    ):
        issues.append(
            "current Atlas artifact lineage has a missing, duplicate, misplaced or incorrect Atlas metadata declaration for Predecessor"
        )
    if (
        len(all_atlas_transitions) != 1
        or len(atlas_transitions) != 1
        or all_atlas_transitions != atlas_transitions
        or not atlas_transitions[0].startswith(
            ("`v0.4.10 → v0.4.11`" if phase7c_candidate_current else "`v0.4.9 → v0.4.10`" if tracker_closure_sync_current else "`v0.4.8 → v0.4.9`" if reconciliation_certified_current else "`v0.4.7 → v0.4.8`" if reconciliation_candidate_current else "`v0.4.6 → v0.4.7`" if audit_promotion_current else "`v0.4.5 → v0.4.6`" if audit_candidate_review_current else "`v0.4.4 → v0.4.5`") if audit_work_start_current else
            "`v0.4.3 → v0.4.4`" if adjudication_current else "`v0.4.2 → v0.4.3`"
        )
    ):
        issues.append(
            "current Atlas artifact lineage has a missing, duplicate, misplaced or incorrect Atlas metadata declaration for SemVer transition"
        )
    current_open_work_route = (
        "docs/00_platform/02_OPEN_WORK_v1.2.69.md" if phase7c_candidate_current else
        "docs/00_platform/02_OPEN_WORK_v1.2.68.md" if reconciliation_certified_current else
        "docs/00_platform/02_OPEN_WORK_v1.2.66.md" if reconciliation_candidate_current else
        "docs/00_platform/02_OPEN_WORK_v1.2.65.md" if audit_promotion_current else
        "docs/00_platform/02_OPEN_WORK_v1.2.64.md" if audit_candidate_review_current else
        "docs/00_platform/02_OPEN_WORK_v1.2.63.md" if audit_work_start_current else
        "docs/00_platform/02_OPEN_WORK_v1.2.62.md" if adjudication_current else "docs/00_platform/02_OPEN_WORK_v1.2.61.md"
    )
    if current_open_work_route not in atlas:
        issues.append(f"current Delivery Atlas does not point to {Path(current_open_work_route).name}")
    if (
        not any(
            marker in atlas
            for marker in (
                "FP-001 PMR reconciliation remains COMPLETE / CERTIFIED",
                "FP-001 PMR reconciliation is COMPLETE / CERTIFIED",
            )
        )
        or (
            "Identity dossier v0.1.4 is CERTIFIED / CURRENT" not in atlas
            and "Identity dossier v0.1.4 and Communications JIT Domain Dossier v0.1.0 are COMPLETE / CERTIFIED / CURRENT" not in atlas
        )
        or (
            "Communications dossier v0.1.0 is COMPLETE / CERTIFIED / CURRENT" not in atlas
            and "Communications JIT Domain Dossier v0.1.0 is COMPLETE / CERTIFIED / CURRENT" not in atlas
        )
        or "Identity dossier v0.1.3 is CERTIFIED / CURRENT" in atlas
    ):
        issues.append("current Delivery Atlas route is stale or omits the Identity or Communications promotion")

    harden_version = "0.5.13" if phase7c_candidate_current else "0.5.12" if tracker_closure_sync_current else "0.5.11" if reconciliation_certified_current else "0.5.10" if reconciliation_candidate_current else "0.5.9" if audit_promotion_current else "0.5.8" if audit_candidate_review_current else "0.5.7" if audit_work_start_current else "0.5.6" if adjudication_current else "0.5.5"
    harden_path = docs / "working" / f"HARDEN-02_CONTRACT_WORKING_v{harden_version}.md"
    harden = harden_path.read_text(encoding="utf-8") if harden_path.is_file() else ""
    harden_header = _markdown_header_metadata(harden, f"# HARDEN-02_CONTRACT_WORKING_v{harden_version}.md")
    harden_metadata_validators = {
        "Plan / contract version": lambda value: value == f"`v{harden_version}`",
        "Current predecessor": lambda value: value.startswith(
            ("`archive/HARDEN-02_CONTRACT_WORKING_v0.5.12.md`" if phase7c_candidate_current else "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.11.md`" if tracker_closure_sync_current else "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.10.md`" if reconciliation_certified_current else "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.9.md`" if reconciliation_candidate_current else "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.8.md`" if audit_promotion_current else "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.7.md`" if audit_candidate_review_current else "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.6.md`") if audit_work_start_current else
            "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.5.md`" if adjudication_current else "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.4.md`"
        ),
        "Earlier historical status predecessor": lambda value: value.startswith(
            "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md`"
        ),
        "Certified contract semantics": lambda value: value.startswith(
            "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md`"
        ) and f"this v{harden_version} successor" in value,
        "v0.5.0 status-successor base main SHA": lambda value: value
        == "`df6190a06bdc8aa4b99f6ed3a18cb9e3e12e22fb`",
        "v0.5.1 status-successor base main SHA": lambda value: value
        == "`90f96ba3452c95112bf6ec4ce5bb897676adbed4`",
        "v0.5.2 status-successor base main SHA": lambda value: value
        == "`0473cd69416f72fd94f2cee24a4d02c7f4fe0992`",
        ("v0.5.13 current-status successor base main SHA" if phase7c_candidate_current else "v0.5.12 current-status successor base main SHA" if tracker_closure_sync_current else "v0.5.11 current-status successor base main SHA" if reconciliation_certified_current else "v0.5.10 current-status successor base main SHA" if reconciliation_candidate_current else "v0.5.9 current-status successor base main SHA" if audit_promotion_current else "v0.5.8 routing-successor base main SHA" if audit_candidate_review_current else
         "v0.5.7 routing-successor base main SHA" if audit_work_start_current else
         "v0.5.6 routing-successor base main SHA" if adjudication_current else "v0.5.5 routing-successor base main SHA"): lambda value: value
        == ("`1a51755d505279821afe166b030be735fe0b6a1c`" if phase7c_candidate_current else "`3f4c9bf564b2b011e96171b8664428423eeba558`" if tracker_closure_sync_current else "`f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3`" if reconciliation_certified_current else "`5d282ecca4e13b621c7f96c05c47d6fac43ec1bd`" if reconciliation_candidate_current else "`3566f1353ef34af58773aa13c6f5bd61d2613d96`" if audit_promotion_current else "`5f5a994e48d9458aaa6397044b3af4d72c5d5e81`" if audit_candidate_review_current else
            "`332d51f19d77430fe4e95911920fe0c87cab524a`" if audit_work_start_current else
            "`6036491dfbda0a311b8fcd0ddcdc3af5c3f11ac3`" if adjudication_current else "`3f09bc91199e74d27645ebbb37d45c4831340952`"),
    }
    for label, valid_value in harden_metadata_validators.items():
        header_values = _metadata_values(harden_header, label)
        document_values = _metadata_declarations(harden, label)
        if (
            len(header_values) != 1
            or len(document_values) != 1
            or document_values != header_values
            or not valid_value(header_values[0])
        ):
            issues.append(
                f"current HARDEN-02 v{harden_version} successor metadata declaration for {label} must occur once in the canonical header and match its governed value"
            )
    harden_status_line = re.findall(r"(?m)^- \*\*Status:\*\*[^\n]*$", harden)
    harden_revision_text = harden.split("### Revision log", 1)
    harden_revision_text = harden_revision_text[1].split("\n---", 1)[0] if len(harden_revision_text) == 2 else ""
    if (
        len(harden_status_line) != 1
        or "Identity v0.1.4 **COMPLETE / CERTIFIED / CURRENT under the separate PR #77 status successor**" not in harden_status_line[0]
        or harden_revision_text.count(
            "Records PR #76 candidate certification and completed post-merge certification evidence; the separate PR #77 status successor records Identity v0.1.4 as CERTIFIED / CURRENT."
        ) != 1
        or harden_revision_text.count(
            "Records PR #78 Communications dossier certification and the separate PR #81 current-status promotion under Open Work v1.2.59."
        ) != 1
    ):
        issues.append(f"current HARDEN-02 v{harden_version} status header or revision log confuses certification with current-status promotion")
    harden_current = harden.split("## 21. Current execution certification and next stage", 1)
    harden_current = harden_current[1] if len(harden_current) == 2 else ""
    expected_harden_open_work = (
        "Open Work v1.2.69" if phase7c_candidate_current else
        "Open Work v1.2.68" if reconciliation_certified_current else
        "Open Work v1.2.66" if reconciliation_candidate_current else
        "Open Work v1.2.65" if audit_promotion_current else
        "Open Work v1.2.64" if audit_candidate_review_current else
        "Open Work v1.2.63" if audit_work_start_current else
        "Open Work v1.2.62" if adjudication_current else "Open Work v1.2.61"
    )
    if expected_harden_open_work not in harden_current or "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED" not in harden_current or "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT" not in harden_current or "IDENTITY v0.1.4 CURRENT-STATUS PROMOTION SOURCE: PR #77 STATUS SUCCESSOR; PR #76 CANDIDATE AND POST-MERGE CERTIFICATION EVIDENCE: COMPLETE" not in harden_current:
        issues.append(f"current HARDEN-02 v{harden_version} status route is stale or omits completed Identity promotion")
    if audit_promotion_current and (
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0" not in harden_current
        or (
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT"
            if reconciliation_certified_current
            else "Phase 7B reconciliation is IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING"
            if reconciliation_candidate_current
            else "Phase 7B reconciliation is NEXT / NOT_STARTED"
        ) not in harden_current
    ):
        issues.append("current HARDEN-02 route omits the completed Audit dossier or Phase 7B reconciliation state")
    if audit_work_start_current and not audit_promotion_current and (
        "AUDIT & EVIDENCE DOSSIER: REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING" not in harden_current
        or (
            "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION" if audit_candidate_review_current
            else "AUTHOR AND REVIEW THE FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE"
        ) not in harden_current
        or (
            "AUDIT DOSSIER CANDIDATE: CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
            if audit_candidate_review_current
            else "AUDIT DOSSIER CANDIDATE: NOT AUTHORED / NOT CERTIFIED / NOT CURRENT"
        ) not in harden_current
    ):
        issues.append("current HARDEN-02 route advances or omits the Audit dossier work-start state")
    if (
        "COMMUNICATIONS v0.1.0 PROMOTION: COMPLETE / CERTIFIED / CURRENT" not in harden_current
        or "COMMUNICATIONS DOSSIER: COMPLETE / CERTIFIED / CURRENT v0.1.0" not in harden_current
        or "COMMUNICATIONS FINALISATION: BLOCKED / STOP" not in harden_current
        or (
            (
                "PHASE 7C: IN PROGRESS / CANDIDATE AUTHORED / NOT COMPLETE / CERTIFICATION PENDING" not in harden_current
                or "FRESH INDEPENDENT EXACT-HEAD REVIEW OF THE PHASE 7C CONTRACT CANDIDATE" not in harden_current
                or "FINAL FEATURE PACK CONTRACT v0.1.0: CANDIDATE / NOT CERTIFIED / NOT CURRENT" not in harden_current
            ) if phase7c_candidate_current else
            "PHASE 7C: NEXT / NOT_STARTED" not in harden_current
            if reconciliation_certified_current else "PHASE 7C: BLOCKED / NOT_STARTED" not in harden_current
        )
        or "Identity dossier v0.1.3 are COMPLETE / CERTIFIED" in harden_current
    ):
        issues.append("current HARDEN-02 route does not record Communications promotion or advances a later gate")
    harden_before_history = harden.split("### 11.5 PR #40 lifecycle evidence", 1)[0]
    if re.search(
        r"(?im)Current Open Work v1\.2\.58 records Communications JIT Domain Dossier work as IN PROGRESS",
        harden_before_history,
    ):
        issues.append("current HARDEN-02 prose still treats Open Work v1.2.58 Communications as live IN PROGRESS state")
    i07_parts = harden.split("### I-07 — Phase 7C readiness fail-closed", 1)
    i07_section = i07_parts[1].split("### I-08 —", 1)[0] if len(i07_parts) == 2 else ""
    if "required Communications dossier and conditional dispositions remain unresolved" in i07_section:
        issues.append("HARDEN I-07 still blocks Phase 7C on the Communications dossier itself after promotion")
    if (
        "→ COMMUNICATIONS JIT DOMAIN DOSSIER\n→ REMAINING REQUIRED / CONDITIONAL PHASE 7B"
        in harden
        and "→ CERTIFIED FP-001 COMMUNICATIONS v0.1.0 DOSSIER PROMOTION\n→ REMAINING REQUIRED / CONDITIONAL PHASE 7B"
        not in harden
    ):
        issues.append("current HARDEN-02 route omits completed Communications dossier promotion before remaining Phase 7B")
    if "does not create or start the Communications dossier" in harden_before_history:
        issues.append("current HARDEN-02 §20 still denies Communications dossier promotion that is now recorded as complete")

    stale_predecessor_routes = (
        ("Open Work v1.2.67", r"(?<!archive/)02_OPEN_WORK_v1\.2\.67\.md"),
        ("Delivery Atlas v0.4.9", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.4\.9\.md"),
        ("FP-001 skeleton v0.1.11", r"(?<!archive/)FP-001_FEATURE_PACK_SKELETON_WORKING_v0\.1\.11\.md"),
        ("HARDEN-02 v0.5.11", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.5\.11\.md"),
        ("Open Work v1.2.66", r"(?<!archive/)02_OPEN_WORK_v1\.2\.66\.md"),
        ("Delivery Atlas v0.4.8", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.4\.8\.md"),
        ("FP-001 skeleton v0.1.10", r"(?<!archive/)FP-001_FEATURE_PACK_SKELETON_WORKING_v0\.1\.10\.md"),
        ("HARDEN-02 v0.5.10", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.5\.10\.md"),
        ("Open Work v1.2.59", r"(?<!archive/)02_OPEN_WORK_v1\.2\.58\.md"),
        ("Delivery Atlas v0.4.0", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.4\.0\.md"),
        ("HARDEN-02 v0.5.2", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.5\.2\.md"),
        ("Open Work v1.2.59", r"(?<!archive/)02_OPEN_WORK_v1\.2\.59\.md"),
        ("Delivery Atlas v0.4.1", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.4\.1\.md"),
        ("HARDEN-02 v0.5.3", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.5\.3\.md"),
        ("FP-001 skeleton v0.1.4", r"(?<!archive/)FP-001_FEATURE_PACK_SKELETON_WORKING_v0\.1\.4\.md"),
        ("Open Work v1.2.57", r"(?<!archive/)02_OPEN_WORK_v1\.2\.57\.md"),
        ("Delivery Atlas v0.3.9", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.9\.md"),
        ("HARDEN-02 v0.5.1", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.5\.1\.md"),
        ("FP-001 skeleton v0.1.3", r"(?<!archive/)FP-001_FEATURE_PACK_SKELETON_WORKING_v0\.1\.3\.md"),
        ("Open Work v1.2.54", r"(?<!archive/)02_OPEN_WORK_v1\.2\.54\.md"),
        ("Open Work v1.2.55", r"(?<!archive/)02_OPEN_WORK_v1\.2\.55\.md"),
        ("Delivery Atlas v0.3.6", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.6\.md"),
        ("Delivery Atlas v0.3.7", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.7\.md"),
        ("HARDEN-02 v0.4.8", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.4\.8\.md"),
        ("HARDEN-02 v0.4.9", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.4\.9\.md"),
        ("Identity dossier v0.1.2", r"(?<!archive/)FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0\.1\.2\.md"),
        ("Open Work v1.2.56", r"(?<!archive/)02_OPEN_WORK_v1\.2\.56\.md"),
        ("Delivery Atlas v0.3.8", r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.8\.md"),
        ("HARDEN-02 v0.5.0", r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.5\.0\.md"),
        ("Identity dossier v0.1.3", r"(?<!archive/)FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0\.1\.3\.md"),
    )
    graph_rules = integrity_rules.get("graph_rules", {})
    configured_stale_patterns = graph_rules.get("stale_reference_patterns", [])
    current_route_surfaces = (
        ("README", readme),
        ("Open Work", open_work),
        ("skeleton", skeleton_text),
        ("Identity dossier", dossier_text),
        ("Delivery Atlas", atlas),
        ("HARDEN-02 current route", harden_current),
        ("Phase 7B reconciliation current route", reconciliation_text),
    )
    for predecessor, stale_pattern in stale_predecessor_routes:
        if stale_pattern not in configured_stale_patterns:
            issues.append(f"manifest does not reject unarchived {predecessor} routes")
        pattern = re.compile(stale_pattern)
        for surface, text in current_route_surfaces:
            if pattern.search(text):
                issues.append(f"current {surface} route still references unarchived {predecessor}")

    if audit_promotion_current:
        _check_audit_v010_current_promotion(
            root,
            manifest,
            integrity_rules,
            readme,
            open_work,
            report,
        )

    _record_check(
        report,
        "fp001_pmr_reconciliation",
        not issues,
        "FP-001 PMR reconciliation and Identity v0.1.4 promotion status, PR #67/#70/#76 provenance, separate archives and downstream route are consistent"
        if not issues
        else "; ".join(issues),
        path="docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
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

    allowed_governing_filenames = {
        str(entry.get("canonical_filename"))
        for entry in governing_entries
        if entry.get("canonical_filename")
    }
    governing_root = root / roots["governing"]
    extra_governing_artifacts: list[str] = []
    if governing_root.is_dir():
        for path in sorted(governing_root.iterdir()):
            if not path.is_file():
                continue
            name = path.name
            if name == Path(roots["context_index"]).name:
                continue
            if name.startswith("CURRENT_AUTHORITY_MANIFEST") and name.endswith(".json"):
                continue
            if VERSION_PATTERN.search(name):
                if name not in allowed_governing_filenames:
                    extra_governing_artifacts.append(name)
    governing_root_ok = not extra_governing_artifacts
    _record_check(
        report,
        "governing_root_exclusivity",
        governing_root_ok,
        "governing root contains only manifest-listed current authority versioned documents"
        if governing_root_ok
        else f"unregistered versioned authority documents in governing root: {extra_governing_artifacts}",
        path=roots["governing"],
    )

    context_index = roots["context_index"]
    readme = root / context_index
    readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    expected_order = [str(entry.get("canonical_filename")) for entry in governing_entries]
    default_context = readme_text
    default_context_start = readme_text.find("## Default Agent Context")
    if default_context_start >= 0:
        default_context = readme_text[default_context_start:]
        next_section = re.search(r"^## ", default_context[len("## Default Agent Context"):], re.MULTILINE)
        if next_section:
            section_end = len("## Default Agent Context") + next_section.start()
            default_context = default_context[:section_end]
    expected_names = set(expected_order)
    readme_order = []
    for line in default_context.splitlines():
        if not re.match(r"^\s*\d+\.\s+", line):
            continue
        match = re.search(r"`([^`]+)`", line)
        if match and match.group(1) in expected_names:
            readme_order.append(match.group(1))
    _record_check(
        report,
        "readme_current_authority_order",
        readme.is_file() and readme_order == expected_order,
        "README lists every governing document in manifest order"
        if readme.is_file() and readme_order == expected_order
        else f"README authority order mismatch: {readme_order}",
        path=context_index,
    )

    graph_rules = integrity_rules["graph_rules"]
    stale_patterns = tuple(re.compile(pattern) for pattern in graph_rules["stale_reference_patterns"])
    navigation_document_ids = set(graph_rules["navigation_document_ids"])
    navigation_paths = [str(path) for path in graph_rules.get("navigation_document_paths", [])]
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
    ] + [
        (relative, _path_is_under(relative, roots["reference"]))
        for relative in navigation_paths
    ]
    source_at_freeze_exceptions = graph_rules.get("source_at_freeze_reference_exceptions", {})
    if not isinstance(source_at_freeze_exceptions, dict):
        stale_hits.append("graph rule source_at_freeze_reference_exceptions is not an object")
        source_at_freeze_exceptions = {}
    scan_paths = {relative for relative, _is_reference in scan_targets}
    approved_source_exceptions: dict[str, set[str]] = {}
    stale_pattern_sources = set(graph_rules.get("stale_reference_patterns", []))
    for relative, exception in source_at_freeze_exceptions.items():
        if not isinstance(relative, str) or relative not in scan_paths or not isinstance(exception, dict):
            stale_hits.append(f"invalid source-at-freeze exception route: {relative!r}")
            continue
        exception_patterns = exception.get("patterns")
        expected_hash = exception.get("sha256")
        reason = exception.get("reason")
        source = root / relative
        if (
            not isinstance(exception_patterns, list)
            or not exception_patterns
            or not all(isinstance(item, str) and item in stale_pattern_sources for item in exception_patterns)
            or not isinstance(expected_hash, str)
            or not isinstance(reason, str)
            or not reason.strip()
            or not source.is_file()
            or source.is_symlink()
            or sha256_file(source) != expected_hash
        ):
            stale_hits.append(f"invalid or changed source-at-freeze exception: {relative}")
            continue
        approved_source_exceptions[relative] = set(exception_patterns)
    for relative, is_reference in scan_targets:
        path = root / relative
        if not path.is_file():
            if relative in navigation_paths:
                stale_hits.append(f"{relative}: missing active navigation document")
            continue
        text = path.read_text(encoding="utf-8")
        if relative == "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md":
            authority_start = text.find("## 1. Authority")
            if authority_start >= 0:
                text = text[:authority_start]
        if relative == "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md":
            semantic_start = text.find("## 1. Baseline, purpose and scope")
            if semantic_start >= 0:
                # The certified body intentionally preserves its source-at-certification
                # versions; current route correctness is checked separately below.
                text = text[:semantic_start]
        if is_reference:
            text = "\n".join(text.splitlines()[: graph_rules["reference_header_lines"]])
            patterns = stale_patterns[:1] + stale_patterns[-1:]
        else:
            patterns = stale_patterns
        for pattern in patterns:
            if pattern.pattern in approved_source_exceptions.get(relative, set()):
                if not pattern.search(text):
                    stale_hits.append(
                        f"source-at-freeze exception no longer matches its declared reference: {relative}: {pattern.pattern}"
                    )
                continue
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
        and (
            "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS" in readiness_text
            or "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED" in readiness_text
            or "EXECUTABLE DEVELOPMENT: UNAUTHORISED; CLASSIFICATION SATISFIES ONLY DEVELOPMENT ENTRY HARD STOP CONDITION 9; ALL OTHER APPLICABLE CONDITIONS REQUIRE INDEPENDENT EVALUATION" in readiness_text
            or "EXECUTABLE DEVELOPMENT: AUTHORISED ONLY FOR BOUNDED PHASE 8 ARCHITECTURAL PROOF / NEW_TRACER_BULLET" in readiness_text
        )
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
    repository_root: Path | None = None,
) -> dict[str, Any]:
    """Run all foundation checks and return a JSON-serializable report.

    ``root`` selects the mutable content under audit. Immutable predecessor
    provenance comes from ``repository_root`` or this tool's canonical checkout.
    """

    root = Path(root)
    repository_root = Path(repository_root) if repository_root is not None else _default_root()
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
    by_id = {str(entry.get("document_id", "")): entry for entry in entries}
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
    _check_current_authority_self_versions(root, manifest, report)
    _check_current_authority_route_resolution(root, manifest, integrity_rules, report)
    _check_current_authority_delegated_routing(root, manifest, integrity_rules, report)
    docs = root / "docs" / "00_platform"
    standards_readme = (docs / "README.md").read_text(encoding="utf-8") if (docs / "README.md").is_file() else ""
    open_work_entry = by_id.get("OPEN_WORK", {})
    open_work_path = root / _relative_path(open_work_entry) if open_work_entry else None
    current_open_work = open_work_path.read_text(encoding="utf-8") if open_work_path and open_work_path.is_file() else ""
    harden_route = re.search(
        r"(?m)^CURRENT HARDEN-02 STATUS SUCCESSOR:\s*([^;\s]+)",
        current_open_work,
    )
    harden_path = docs / harden_route.group(1) if harden_route else None
    current_harden = harden_path.read_text(encoding="utf-8") if harden_path and harden_path.is_file() else ""
    if _engineering_standards_candidate_signal(root, manifest, standards_readme):
        standards_ok, standards_message = _engineering_standards_lifecycle_state(
            root,
            manifest,
            standards_readme,
            current_open_work,
            current_harden,
        )
        _record_check(
            report,
            "engineering_standards_lifecycle",
            standards_ok,
            standards_message,
            path="docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md",
        )
    if _production_mode(expected_counts):
        _check_production_graph(root, manifest, integrity_rules, report)
        _check_product_semantics(root, entries, integrity_rules, report)
        if (
            _fp001_phase8_approved_status_successor_is_current(manifest)
            or _fp001_phase8_execution_status_successor_is_current(manifest)
        ):
            # The predecessor-era suite runs against its pinned exact-SHA snapshot.
            # The successor receives explicit current-path, archive-provenance and
            # proof-stop checks so old status assertions do not masquerade as current.
            _check_phase8_approved_status_successor(
                root, repository_root, manifest, integrity_rules, report
            )
            _check_fp001_phase7c_candidate(root, manifest, integrity_rules, report)
        else:
            _check_roadmap_proof_classification_lifecycle(root, manifest, integrity_rules, report)
            _check_fp001_development_entry_hard_stop_lifecycle(root, manifest, integrity_rules, report)
            _check_fp001_phase8_proof_contract_lifecycle(root, manifest, integrity_rules, report)
            _check_fp001_pmr_reconciliation(root, manifest, integrity_rules, report)
            _check_fp001_phase7b_candidate(root, manifest, integrity_rules, report)
            _check_fp001_phase7b_certification_current(root, manifest, integrity_rules, report)
            _check_fp001_phase7c_candidate(root, manifest, integrity_rules, report)
            _check_fp001_phase7c_current_promotion(root, manifest, integrity_rules, report)
            _check_platform_readme_router_consistency(root, report)
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
    report = run_audit(root, manifest_path, repository_root=root)
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        _print_human_report(report)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
