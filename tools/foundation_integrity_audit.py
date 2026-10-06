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
CURRENT_ROUTE_FILENAME_PATTERN = re.compile(
    r"(?<![\w/.-])(?:[\w.-]+/)*[\w.-]+_v\d+\.\d+\.\d+\.md"
)
CURRENT_ROUTE_VERSION_PATTERN = re.compile(r"\bv(\d+\.\d+\.\d+)\b")

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
        "successor_versions": ("0.4.7", "0.4.8"),
        "current_stage": "ENGINEERING STANDARDS AUTHORITY PROMOTION",
        "next_stage": "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
        "readme": "HARDEN-02 EXECUTION: COMPLETE / CERTIFIED",
        "programme_status": "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION NEXT / AUTHORISED / NOT STARTED",
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

    execution = state.get("harden_02_execution")
    if execution not in H02_EXECUTION_STATES:
        return False, "HARDEN execution status is not one of the permitted lifecycle states"
    expected = dict(H02_EXECUTION_STATES[execution])
    promotion_status = state.get("engineering_standards_authority_promotion")
    if execution == "COMPLETE / CERTIFIED":
        if promotion_status == "COMPLETE / CERTIFIED":
            expected.update(
                {
                    "successor_versions": ("0.5.1",),
                    "current_stage": "CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
                    "next_stage": "COMMUNICATIONS JIT DOMAIN DOSSIER",
                    "programme_status": "HARDEN-02 EXECUTION COMPLETE / CERTIFIED; ENGINEERING STANDARDS AUTHORITY PROMOTION COMPLETE / CERTIFIED; FP-001 RECONCILIATION COMPLETE / CERTIFIED; IDENTITY v0.1.4 COMPLETE / CERTIFIED / CURRENT",
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
            ]
            expected_downstream.update({
                "engineering_standards_authority_promotion": "COMPLETE / CERTIFIED",
                "fp001_reconciliation": "COMPLETE / CERTIFIED",
                "communications": "REQUIRED / NEXT / NOT_STARTED",
                "pr_60": "STALE HISTORICAL CANDIDATE / SUPERSEDED BY THIS SUCCESSOR / NOT MERGED / NOT AUTHORITY",
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
    expected_conditionals = {
        "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "analytics": "NOT REQUIRED",
    }
    if state.get("conditional_dossiers") != expected_conditionals:
        return False, "conditional dossier or Analytics state changed"

    expected_route = [
        "CERTIFIED HARDEN-02 EXECUTION",
        "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
        "CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
        "FP001_RECONCILIATION_REQUIRED",
        "CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
        "COMMUNICATIONS JIT DOMAIN DOSSIER",
        "REMAINING REQUIRED / CONDITIONAL PHASE 7B",
        "PHASE 7C",
        "PROOF CLASSIFICATION",
        "PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
    ]
    if state.get("downstream_route") != expected_route:
        return False, "the governed post-execution route changed"
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
            "90f96ba3452c95112bf6ec4ce5bb897676adbed4"
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
            )
            if promotion_status == "COMPLETE / CERTIFIED"
            else (
                "ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
                "FP001_RECONCILIATION_REQUIRED: REQUIRED / DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION / NOT PERFORMED",
            )
        )
        communications_route = (
            "COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION"
        )
        required_active = promotion_route + (
            "PR #38: STALE / BLOCKED / NOT AUTHORITY",
            "PR #60: STALE HISTORICAL CANDIDATE / SUPERSEDED BY THIS SUCCESSOR / NOT MERGED / NOT AUTHORITY",
            "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
            "PHASE 7C: BLOCKED / NOT_STARTED",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
            "STORE / CER: EXCLUDED FROM HARDEN-02",
        )
        if any(active.count(line) != 1 for line in required_active):
            return False, "Open Work omits a required completion or downstream boundary"
        if active.count(communications_route) != 2:
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
            "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
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
    required_readme = (
        "- CURRENT AUTHORITY-STAGE PROGRAMME: " + expected["current_stage"],
        "- NEXT STAGE: " + expected["next_stage"],
        "- IDENTITY v0.1.4: CERTIFIED / CURRENT under PR #76",
        "- COMMUNICATIONS FINALISATION: BLOCKED / STOP",
        "- ENGINEERING STANDARDS AUTHORITY PROMOTION: " + (
            "COMPLETE / CERTIFIED"
            if promotion_status == "COMPLETE / CERTIFIED"
            else "NEXT / AUTHORISED / NOT STARTED"
            if execution == "COMPLETE / CERTIFIED"
            else "DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED"
        ),
        "- PRIVACY & CONSENT DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "- CONTENT & MEDIA DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "- AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "- ANALYTICS DOSSIER: NOT REQUIRED",
        "- PHASE 7C: BLOCKED / NOT_STARTED pending the required Communications dossier and explicit conditional-dossier dispositions.",
        "- PROOF CLASSIFICATION: NOT FINALISED",
        "- EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
    )
    if any(readme_current.count(line) != 1 for line in required_readme):
        return False, "README current route or downstream status is missing or contradictory"
    communications_status = (
        "- COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED"
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
        expected_harden_version = "0.5.1" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"
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
                "immediate next task is `COMMUNICATIONS JIT DOMAIN DOSSIER`",
                "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
                "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
                "COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED",
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

    active_start = open_work.find("# 9. Immediate Next Action")
    active_end = open_work.find("# 10. Minimal Tools", active_start + 1)
    if active_start < 0 or active_end < 0 or active_start >= active_end:
        return False, "current Open Work programme-state section is missing"
    active = open_work[active_start:active_end]
    required_route = (
        "ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED",
        "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
        "PR #38: STALE / BLOCKED / NOT AUTHORITY",
        "PR #60: STALE HISTORICAL CANDIDATE / SUPERSEDED BY THIS SUCCESSOR / NOT MERGED / NOT AUTHORITY",
        "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
        "PHASE 7C: BLOCKED / NOT_STARTED",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
        "STORE / CER: EXCLUDED FROM HARDEN-02",
    )
    if any(active.count(line) != 1 for line in required_route):
        return False, "Open Work current route omits or duplicates the certified stage or a downstream boundary"
    if active.count("COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED") != 2:
        return False, "Open Work Communications summary and required-dossier route disagree or are duplicated"
    if "NEXT STAGE: COMMUNICATIONS JIT DOMAIN DOSSIER" not in active:
        return False, "Open Work does not route NEXT to Communications after certified FP-001 reconciliation"
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
    if re.search(r"(?im)^.*COMMUNICATIONS\s*:\s*(?:STARTED|COMPLETE|AUTHORI[ZS]ED).*$", active):
        return False, "Communications has advanced before FP-001 reconciliation"
    if re.search(r"(?im)^.*PHASE 7C\s*:\s*(?:NEXT|UNBLOCKED|COMPLETE|AUTHORI[ZS]ED).*$", active):
        return False, "Phase 7C has been unblocked prematurely"
    if re.search(r"(?im)^.*PROOF CLASSIFICATION\s*:\s*FINALI[ZS]ED.*$", active):
        return False, "proof classification has been finalised prematurely"
    if re.search(r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$", active):
        return False, "Phase 8 or application implementation has been authorised prematurely"
    if re.search(r"(?im)^.*STORE\s*/\s*CER\s*:\s*IN SCOPE.*$", active):
        return False, "Store/CER has been included in scope"

    harden_section_start = open_work.find("## 12.9 — HARDEN-02 contract lifecycle completion")
    harden_section_end = open_work.find("## 12.10", harden_section_start + 1)
    if harden_section_start < 0 or harden_section_end < 0 or harden_section_start >= harden_section_end:
        return False, "Open Work current HARDEN lifecycle status section is missing or malformed"
    harden_section = open_work[harden_section_start:harden_section_end]
    required_harden_status = (
        "Engineering Standards Authority Promotion is COMPLETE / CERTIFIED under `reference/ENGINEERING_STANDARDS_v1.0.1.md`",
        "FP-001 PMR reconciliation is COMPLETE / CERTIFIED under PR #67",
        "Identity v0.1.3 is COMPLETE / CERTIFIED / CURRENT under PR #70",
        "NEXT is `COMMUNICATIONS JIT DOMAIN DOSSIER`, REQUIRED / NEXT / NOT_STARTED",
        "Phase 7C remains blocked / not started",
        "proof classification remains not finalised",
        "executable development remains blocked until Phase 8 entry conditions pass",
    )
    if any(harden_section.count(line) != 1 for line in required_harden_status):
        return False, "Open Work current HARDEN status section has stale promotion status or altered downstream gates"
    if "Engineering Standards Authority Promotion is NEXT / AUTHORISED / NOT STARTED" in harden_section:
        return False, "Open Work current HARDEN status section retains the pre-certification Standards route"

    if not harden:
        return False, "current HARDEN status successor is missing"
    harden_route_start = harden.rfind("## 21. Current execution certification and next stage")
    if harden_route_start < 0:
        return False, "current HARDEN successor has no current route section"
    harden_route = harden[harden_route_start:]
    required_harden_route = (
        "Engineering Standards Authority Promotion, FP-001 PMR reconciliation and Identity dossier v0.1.4 are COMPLETE / CERTIFIED",
        "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
        "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
        "COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED",
    )
    if any(value not in harden_route for value in required_harden_route):
        return False, "current HARDEN successor does not route the certified promotion to FP-001"
    if "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION" in harden_route:
        return False, "current HARDEN successor starts or misroutes Communications"
    if "PHASE 7C: BLOCKED / NOT_STARTED" not in harden_route:
        return False, "current HARDEN successor unblocks Phase 7C"
    if "PROOF CLASSIFICATION: NOT FINALISED" not in harden_route:
        return False, "current HARDEN successor finalises proof classification"
    if "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS" not in harden_route:
        return False, "current HARDEN successor authorises Phase 8 or implementation"
    if "STORE / CER: EXCLUDED FROM HARDEN-02" not in harden_route:
        return False, "current HARDEN successor includes Store/CER"

    return True, "certified Engineering Standards, FP-001 reconciliation and Identity promotion route NEXT to the Communications JIT Domain Dossier"


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
    fp001_candidates = (
        root / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md",
        root / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
    )
    fp001_path = next((path for path in fp001_candidates if path.is_file()), fp001_candidates[-1])
    fp001 = fp001_path.read_text(encoding="utf-8") if fp001_path.is_file() else ""
    atlas_relative_path = next(
        (
            str(path)
            for path in integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])
            if Path(str(path)).name.startswith("DELIVERY_ATLAS_WORKING_")
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
        route_filenames = [
            Path(value).name for value in CURRENT_ROUTE_FILENAME_PATTERN.findall(route_line)
        ]
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

        for filename in route_filenames:
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

    def record_current_routes(
        document_id: str,
        relative: str,
        routed_names: list[str],
        expected_names: list[str],
    ) -> None:
        if routed_names != expected_names:
            issues.append(
                f"{document_id}: explicitly current routes {routed_names!r} do not match manifest routes {expected_names!r}"
            )
            issue_paths.append(relative)
        for filename in routed_names:
            if filename not in by_filename:
                issues.append(f"{document_id}: active route {filename!r} is not a current manifest route")
                issue_paths.append(relative)
            elif filename not in readme_filenames:
                issues.append(f"{document_id}: active route {filename!r} is absent from README current authority")
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
        route_names = [
            Path(filename).name
            for filename in CURRENT_ROUTE_FILENAME_PATTERN.findall(current_authority_lines[0])
        ] if len(current_authority_lines) == 1 else []
        if len(current_authority_lines) == 1 or complete_authority_inventory:
            record_current_routes("ROADMAP", relative, route_names, expected_product_authority)

    graph_rules = integrity_rules.get("graph_rules", {})
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
                source_rows[cells[0]] = [
                    Path(filename).name
                    for filename in CURRENT_ROUTE_FILENAME_PATTERN.findall(cells[1])
                ]
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
                source_rows.get(label, []),
                expected_names,
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
                    authority_sources.extend(
                        Path(filename).name
                        for filename in CURRENT_ROUTE_FILENAME_PATTERN.findall(cells[0])
                    )
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
            authority_sources,
            expected_harden_authority,
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


def _check_fp001_pmr_reconciliation(
    root: Path,
    manifest: dict[str, Any],
    integrity_rules: dict[str, Any],
    report: dict[str, Any],
) -> None:
    docs = root / "docs" / "00_platform"
    skeleton = docs / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md"
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
    if len(current_entries) != 1:
        issues.append("manifest must identify exactly one current Open Work route")
        open_work = ""
    else:
        current_open_work = current_entries[0]
        open_work_path = root / _relative_path(current_open_work)
        open_work = open_work_path.read_text(encoding="utf-8") if open_work_path.is_file() else ""
        if _relative_path(current_open_work) != "docs/00_platform/02_OPEN_WORK_v1.2.57.md":
            issues.append("manifest Open Work route is not v1.2.57")
        if current_open_work.get("canonical_filename") != "02_OPEN_WORK_v1.2.57.md":
            issues.append("manifest current Open Work filename is stale")
        if current_open_work.get("semver") != "1.2.57":
            issues.append("manifest current Open Work version is stale")

    atlas_status_lines = re.findall(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", open_work)
    expected_atlas_status = (
        "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.9.md`; "
        "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md`; "
        "pinned v0.2.1 source-at-freeze artifacts remain preserved; DERIVED / NON-AUTHORITATIVE; "
        "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
    )
    if atlas_status_lines != [expected_atlas_status]:
        issues.append(
            "Open Work v1.2.57 Atlas route must name archived Atlas v0.3.8 as its immediate routing predecessor"
        )

    expected_active_skeletons = [skeleton]
    expected_active_dossiers = [dossier]
    active_skeletons = sorted((docs / "working").glob("FP-001_FEATURE_PACK_SKELETON_WORKING_v*.md"))
    active_dossiers = sorted((docs / "working").glob("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v*.md"))
    if active_skeletons != expected_active_skeletons:
        issues.append("exactly one active certified/current skeleton v0.1.3 is required; stale candidates or extra versions remain active")
    if active_dossiers != expected_active_dossiers:
        issues.append("exactly one active certified/current Identity dossier v0.1.4 is required; stale candidates or extra versions remain active")
    for path, label in ((skeleton, "certified skeleton"), (dossier, "certified Identity dossier")):
        if not path.is_file():
            issues.append(f"{label} is missing")

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
    if identity_promotion_candidate.is_file() and superseded_identity_current.is_file() and identity_promotion_candidate.read_bytes() == superseded_identity_current.read_bytes():
        issues.append("PR #70 candidate archive was confused with the promoted/current v0.1.3 snapshot")
    if (docs / "working" / "candidates" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").exists():
        issues.append("promoted Identity v0.1.4 remains in the candidate route")

    navigation_paths = integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])
    expected_navigation_paths = {
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.9.md",
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md",
        "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md",
    }
    if not isinstance(navigation_paths, list) or set(navigation_paths) != expected_navigation_paths or len(navigation_paths) != len(expected_navigation_paths):
        issues.append("manifest navigation does not route exactly the current FP-001, Atlas and HARDEN successors")

    skeleton_text = skeleton.read_text(encoding="utf-8") if skeleton.is_file() else ""
    dossier_text = dossier.read_text(encoding="utf-8") if dossier.is_file() else ""
    skeleton_candidate_text = skeleton_candidate.read_text(encoding="utf-8") if skeleton_candidate.is_file() else ""
    dossier_candidate_text = dossier_candidate.read_text(encoding="utf-8") if dossier_candidate.is_file() else ""
    identity_promotion_candidate_text = identity_promotion_candidate.read_text(encoding="utf-8") if identity_promotion_candidate.is_file() else ""
    superseded_identity_current_text = superseded_identity_current.read_text(encoding="utf-8") if superseded_identity_current.is_file() else ""
    identity_v014_candidate_text = identity_v014_candidate.read_text(encoding="utf-8") if identity_v014_candidate.is_file() else ""

    if "**Lifecycle status:** " + chr(96) + "CERTIFIED / CURRENT" + chr(96) not in skeleton_text:
        issues.append("skeleton v0.1.3 is not marked CERTIFIED / CURRENT")
    if "**Status:** " + chr(96) + "CERTIFIED / CURRENT" + chr(96) not in dossier_text:
        issues.append("Identity dossier v0.1.4 is not marked CERTIFIED / CURRENT")
    if "**Artifact version:** v0.1.4" not in dossier_text.split("## A. Baseline and scope", 1)[0]:
        issues.append("active Identity dossier metadata does not match the routed v0.1.4 version")
    if "RECONCILIATION CANDIDATE / NOT CERTIFIED" in skeleton_text:
        issues.append("active skeleton remains a reconciliation candidate")
    if "RECONCILIATION CANDIDATE / NOT CERTIFIED" in dossier_text:
        issues.append("active Identity dossier remains a reconciliation candidate")
    if (
        "Communications remains " + chr(96) + "REQUIRED / NEXT / NOT_STARTED" + chr(96) not in dossier_text
        or "finalisation remains " + chr(96) + "BLOCKED / STOP" + chr(96) not in dossier_text
        or "No Communications dossier, Phase 7C work or implementation starts here." not in dossier_text
    ):
        issues.append("certified Identity dossier does not preserve the Communications NEXT and finalisation stop boundary")

    phase7c_start = dossier_text.find("### `BLOCKS_PHASE7C`")
    phase7c_end = dossier_text.find("### `BLOCKS_RELEASE_ONLY`", phase7c_start + 1)
    if phase7c_start < 0 or phase7c_end <= phase7c_start:
        issues.append("active Identity BLOCKS_PHASE7C lifecycle section is missing or malformed")
    else:
        phase7c_section = dossier_text[phase7c_start:phase7c_end]
        pending_lifecycle_patterns = (
            r"\bNOT\s+CURRENT\b",
            r"\bCERTIFICATION\s+PENDING\b",
            r"\b(?:await(?:s|ed|ing)?|pending)\b.{0,100}\b(?:certification|promotion)\b",
            r"\b(?:certification|promotion)\b.{0,100}\b(?:pending|awaiting)\b",
            r"\bthis\b.{0,40}\b(?:v0\.1\.4\s+)?candidate\b",
            r"\bIdentity(?:\s+&\s+Access)?(?:\s+dossier)?\s+v0\.1\.[0-3]\b.{0,80}\b(?:current|certified)\b",
            r"\b(?:current|certified)\b.{0,80}\bIdentity(?:\s+&\s+Access)?(?:\s+dossier)?\s+v0\.1\.[0-3]\b",
        )
        if any(re.search(pattern, phase7c_section, flags=re.IGNORECASE | re.DOTALL) for pattern in pending_lifecycle_patterns):
            issues.append("active Identity BLOCKS_PHASE7C lifecycle contradicts CERTIFIED / CURRENT")
        required_phase7c_state = (
            "PR #76 certification/promotion is `COMPLETE`",
            "Identity v0.1.4 is `CERTIFIED / CURRENT`",
            "Communications remains `REQUIRED / NEXT / NOT_STARTED`",
            "Communications finalisation remains `BLOCKED / STOP` pending its own dossier and applicable gates",
            "Phase 7C remains `BLOCKED / NOT_STARTED`",
            "required Phase 7B work remains",
            "separately authorised Communications dossier is not started",
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
        "status_successor_base_sha": "90f96ba3452c95112bf6ec4ce5bb897676adbed4",
        "current_stage": "CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
        "next_stage": "COMMUNICATIONS JIT DOMAIN DOSSIER",
        "status_successor_version": "0.5.1",
        "fp001_reconciliation": "COMPLETE / CERTIFIED",
        "identity_dossier": "CERTIFIED / CURRENT v0.1.4",
        "identity_dossier_promotion": "COMPLETE / CERTIFIED / CURRENT",
        "communications_finalisation": "BLOCKED / STOP",
        "communications": "REQUIRED / NEXT / NOT_STARTED",
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
        ],
    }
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
    if "OQ-034" not in skeleton_text or "executable proof is not complete" not in skeleton_text.casefold() or "proof classification is not finalised" not in skeleton_text.casefold():
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
    if next_routes != ["COMMUNICATIONS JIT DOMAIN DOSSIER"]:
        issues.append("current Open Work NEXT route is not the existing Communications JIT Domain Dossier task")
    for token in (
        "CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
        "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED",
        "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT",
        "COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED",
        "COMMUNICATIONS FINALISATION: BLOCKED / STOP",
        "- COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED",
        "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
        "OPEN GATES: OQ-035 SECURITY / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY; OQ-036 VENDOR / OPERATIONS REVIEW UNRESOLVED / RELEASE-ONLY",
        "PHASE 7C: BLOCKED / NOT_STARTED PENDING COMMUNICATIONS AND CONDITIONAL-DOSSIER DISPOSITIONS",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
        "STORE / CER: EXCLUDED FROM HARDEN-02",
    ):
        if token not in stage:
            issues.append(f"Open Work current status or later-gate boundary changed: {token}")
    if re.findall(r"(?m)^COMMUNICATIONS:\s*(.*?)\s*$", stage) != ["REQUIRED / NEXT / NOT_STARTED"]:
        issues.append("Open Work Communications current route is missing, duplicated, started or completed")
    if re.findall(r"(?m)^- COMMUNICATIONS:\s*(.*?)\s*$", stage) != ["REQUIRED / NEXT / NOT_STARTED"]:
        issues.append("Open Work Communications required-dossier route is missing, duplicated, started or completed")
    forbidden_advancement = (
        ("Communications", r"(?im)^.*COMMUNICATIONS\s*:\s*(?:STARTED|COMPLETE|CERTIFIED|AUTHORI[ZS]ED).*$"),
        ("conditional dossiers", r"(?im)^.*CONDITIONAL DOSSIERS:.*\b(?:COMPLETE|CERTIFIED|ADJUDICATED)\b.*$"),
        ("Phase 7C", r"(?im)^.*PHASE 7C\s*:\s*(?:NEXT|READY|UNBLOCKED|COMPLETE|CERTIFIED|AUTHORI[ZS]ED).*$"),
        ("proof classification", r"(?im)^.*PROOF CLASSIFICATION\s*:\s*(?:FINAL|FINALI[ZS]ED|CERTIFIED).*$"),
        ("Phase 8/application implementation", r"(?im)^.*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT)\s*:\s*(?:AUTHORI[ZS]ED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE).*$"),
        ("Store/CER", r"(?im)^.*STORE\s*/\s*CER\s*:\s*(?:INCLUDED|REQUIRED|AUTHORI[ZS]ED|COMPLETE).*$"),
    )
    for label, pattern in forbidden_advancement:
        if re.search(pattern, stage):
            issues.append(f"{label} advanced during the FP-001 status successor")
    if "FP001_RECONCILIATION_REQUIRED: REQUIRED / NEXT / NOT PERFORMED" in stage:
        issues.append("certified reconciliation still says NOT PERFORMED")
    if re.search(r"(?im)^.*COMMUNICATIONS DOSSIER STARTED:\s*YES.*$", skeleton_text + dossier_text):
        issues.append("Communications dossier is marked started")
    communications_dossiers = [
        candidate
        for candidate in (docs / "working").rglob("*.md")
        if candidate.is_file()
        and "COMMUNICATIONS" in candidate.name.upper()
        and "DOSSIER" in candidate.name.upper()
        and candidate.name.upper().startswith("FP-001")
    ]
    if communications_dossiers:
        issues.append("Communications JIT Domain Dossier was created in the status-only successor")

    readme_route = (
        "Current programme status is in Open Work v1.2.57.",
        "PR #67 PMR reconciliation is COMPLETE / CERTIFIED",
        "PR #76 Identity v0.1.4 promotion is COMPLETE / CERTIFIED",
        "- IDENTITY v0.1.4: CERTIFIED / CURRENT under PR #76",
        "NEXT is " + chr(96) + "COMMUNICATIONS JIT DOMAIN DOSSIER" + chr(96),
        "Communications dossier has not started",
    )
    for token in readme_route:
        if token not in readme:
            issues.append(f"README current route is missing or stale: {token}")
    readme_active_routes = (
        "4. " + chr(96) + "02_OPEN_WORK_v1.2.57.md" + chr(96),
        chr(96) + "working/DELIVERY_ATLAS_WORKING_v0.3.9.md" + chr(96) + " — derived Delivery Atlas",
        chr(96) + "working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md" + chr(96) + " — preserves certified HARDEN-02",
        chr(96) + "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md" + chr(96) + " — certified/current",
        chr(96) + "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md" + chr(96) + " — certified/current",
    )
    for token in readme_active_routes:
        if token not in readme:
            issues.append(f"README active route is missing or stale: {token}")

    atlas_path = docs / "working" / "DELIVERY_ATLAS_WORKING_v0.3.9.md"
    atlas = atlas_path.read_text(encoding="utf-8") if atlas_path.is_file() else ""
    if "docs/00_platform/02_OPEN_WORK_v1.2.57.md" not in atlas:
        issues.append("current Delivery Atlas does not point to Open Work v1.2.57")
    if "FP-001 PMR reconciliation remains COMPLETE / CERTIFIED" not in atlas or "Identity dossier v0.1.4 is CERTIFIED / CURRENT" not in atlas or "COMMUNICATIONS JIT DOMAIN DOSSIER" not in atlas or "Identity dossier v0.1.3 is CERTIFIED / CURRENT" in atlas:
        issues.append("current Delivery Atlas route is stale or omits the Identity promotion or Communications task")

    harden_path = docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.1.md"
    harden = harden_path.read_text(encoding="utf-8") if harden_path.is_file() else ""
    harden_current = harden.split("## 21. Current execution certification and next stage", 1)
    harden_current = harden_current[1] if len(harden_current) == 2 else ""
    if "Open Work v1.2.57" not in harden_current or "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED" not in harden_current or "IDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT" not in harden_current:
        issues.append("current HARDEN-02 status route is stale or omits completed Identity promotion")
    if "COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED" not in harden_current or "COMMUNICATIONS FINALISATION: BLOCKED / STOP" not in harden_current or "PHASE 7C: BLOCKED / NOT_STARTED" not in harden_current or "Identity dossier v0.1.3 are COMPLETE / CERTIFIED" in harden_current:
        issues.append("current HARDEN-02 route starts Communications or advances a later gate")

    stale_predecessor_routes = (
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
    )
    for predecessor, stale_pattern in stale_predecessor_routes:
        if stale_pattern not in configured_stale_patterns:
            issues.append(f"manifest does not reject unarchived {predecessor} routes")
        pattern = re.compile(stale_pattern)
        for surface, text in current_route_surfaces:
            if pattern.search(text):
                issues.append(f"current {surface} route still references unarchived {predecessor}")

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
    for relative, is_reference in scan_targets:
        path = root / relative
        if not path.is_file():
            if relative in navigation_paths:
                stale_hits.append(f"{relative}: missing active navigation document")
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
        _check_fp001_pmr_reconciliation(root, manifest, integrity_rules, report)
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
