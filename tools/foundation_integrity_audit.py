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
    fp001_path = root / "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
    fp001 = fp001_path.read_text(encoding="utf-8") if fp001_path.is_file() else ""

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
    no_blocking_reference = all(
        not any("OQ-034" in line and "BLOCKS_THIS_FP" in line for line in document.splitlines())
        for document in (roadmap, fp001)
    )
    proof_is_downstream = all(
        "phase 8" in document.lower()
        and "proof" in document.lower()
        and re.search(r"proof[^\n]{0,100}(not complete|not finalised|not finalized|incomplete)", document.lower())
        for document in (roadmap, fp001)
    )
    oq_ok = bool(
        decision_match
        and "RESOLVED / ARCHITECTURE SELECTION" in decision_match.group(1)
        and no_blocking_reference
        and proof_is_downstream
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

    h02_rows = _marked_matrix_rows(open_work, "HARDEN-02-LIFECYCLE")
    h02 = {row.get("gate", ""): row.get("status", "") for row in h02_rows}
    required_h02 = {
        "PRE_MERGE_CERTIFICATION": "COMPLETE",
        "CERTIFIED_HEAD_MERGED_UNCHANGED": "COMPLETE",
        "RESULTING_MAIN_CI": "PASS",
        "POST_MERGE_INDEPENDENT_INSPECTION": "PENDING",
        "POST_MERGE_ATTESTATION": "PENDING",
        "EXECUTION": "NOT_STARTED_NOT_AUTHORISED",
    }
    h02_ok = h02 == required_h02 and "POST-MERGE CERTIFICATION: PENDING" in readme and (
        "NOT STARTED / NOT AUTHORISED" in readme
    ) and "PENDING INDEPENDENT PRE-MERGE CERTIFICATION" not in readme
    _record_check(
        report,
        "harden_02_lifecycle_state",
        h02_ok,
        "HARDEN-02 records completed pre-merge/merge/CI steps and pending post-merge certification without authorising execution"
        if h02_ok
        else "HARDEN-02 lifecycle facts, post-merge pending state or execution stop are inconsistent",
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
    readme_order = [
        str(entry.get("canonical_filename"))
        for entry in governing_entries
        if f"`{entry.get('canonical_filename')}`" in readme_text
    ]
    expected_order = [str(entry.get("canonical_filename")) for entry in governing_entries]
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
        _check_product_semantics(root, entries, integrity_rules, report)
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
