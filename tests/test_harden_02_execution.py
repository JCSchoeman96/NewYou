from __future__ import annotations

import difflib
import hashlib
import json
import re
import unittest
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.51.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.50.md"
CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.5.md"
CONTRACT_PREDECESSOR = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.4.4.md"
ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.3.3.md"
ATLAS_PREDECESSOR = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.3.2.md"

POM = DOCS / "PLATFORM_OPERATING_MODEL_v1.0.1.md"
ROADMAP = DOCS / "05_ROADMAP_v1.1.6.md"
SKELETON = DOCS / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"

MATRIX_START = "<!-- NEWYOU:PRODUCT-MATRIX:HARDEN-02-LIFECYCLE:START -->"
MATRIX_END = "<!-- NEWYOU:PRODUCT-MATRIX:HARDEN-02-LIFECYCLE:END -->"
JSON_START = "<!-- HARDEN_02_LIFECYCLE_STATE_START -->"
JSON_END = "<!-- HARDEN_02_LIFECYCLE_STATE_END -->"

CURRENT_STAGE = "ENGINEERING STANDARDS AUTHORITY PROMOTION"
NEXT_STAGE = "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED"
EXECUTION_STATUS = "COMPLETE / CERTIFIED"
EXECUTION_MATRIX_STATUS = "COMPLETE_CERTIFIED"
EXECUTION_MATRIX_EVIDENCE = "`I-01…I-13 PASS on resulting main 6fea69eadf18f2fb79d78c2a94ab035b10abe31f; run 36567933267; PR #59 durable post-merge attestation 5890574449`"
CONTRACT_STATUS = "COMPLETE / CERTIFIED"

EXPECTED_ARCHIVE_SHA256 = {
    OPEN_WORK_PREDECESSOR: "ea99015d5fca34211e9c85e9f6575e8ad69df2cf9a39da3b255f2e9d3a5abcb7",
    CONTRACT_PREDECESSOR: "496df83ba06d3e3ad1e871b8415a5352147662ae694005d945359f7b1f7976da",
    ATLAS_PREDECESSOR: "b24bcaaac4f82617a766f1602418e8301a5076594d9ac8f90afb302174bf706e",
}

EXPECTED_DOWNSTREAM_ROUTE = [
    "CERTIFIED HARDEN-02 EXECUTION",
    "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
    "CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
    "FP001_RECONCILIATION_REQUIRED",
    "COMMUNICATIONS JIT DOMAIN DOSSIER",
    "REMAINING REQUIRED / CONDITIONAL PHASE 7B",
    "PHASE 7C",
    "PROOF CLASSIFICATION",
    "PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
]

EXPECTED_MATRIX_GATES = (
    "CONTRACT_LIFECYCLE",
    "PRE_MERGE_CERTIFICATION",
    "EXACT_HEAD_CI",
    "CERTIFIED_HEAD_MERGE",
    "RESULTING_MAIN_CI",
    "POST_MERGE_INDEPENDENT_REVIEW",
    "POST_MERGE_ATTESTATION",
    "EXECUTION",
)

CURRENT_AUTHORITY_DOCUMENT_IDS = (
    "PROJECT_NORTH_STAR_AND_MVP",
    "PLATFORM_BASELINE",
    "DECISION_REGISTER",
    "OPEN_WORK",
    "ARCHITECTURE_SYNTHESIS",
    "DOMAIN_MAP",
    "ROADMAP",
    "PLATFORM_OPERATING_MODEL",
    "FRONTEND_EXPERIENCE_SYSTEM",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def _heading_positions(text: str) -> dict[str, list[int]]:
    positions: dict[str, list[int]] = {}
    for match in re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*$", text):
        heading = f"{match.group(1)} {match.group(2)}"
        positions.setdefault(heading, []).append(match.start())
    return positions


def _section(text: str, start_heading: str, end_heading: str | None) -> str:
    start_matches = list(re.finditer(rf"(?m)^{re.escape(start_heading)}\s*$", text))
    if len(start_matches) != 1:
        raise ValueError(f"expected one {start_heading!r}, found {len(start_matches)}")
    start = start_matches[0].start()
    if end_heading is None:
        return text[start:]
    end_matches = list(
        re.finditer(rf"(?m)^{re.escape(end_heading)}\s*$", text[start:])
    )
    if len(end_matches) != 1:
        raise ValueError(f"expected one {end_heading!r} after {start_heading!r}")
    end = start + end_matches[0].start()
    if start >= end:
        raise ValueError(f"section order is invalid for {start_heading!r}")
    return text[start:end]


def _assert_unique_headings(text: str) -> None:
    duplicates = {
        heading: positions
        for heading, positions in _heading_positions(text).items()
        if len(positions) > 1
    }
    if duplicates:
        raise ValueError(f"duplicate section marker(s): {sorted(duplicates)}")


def _marked_region(text: str, start_marker: str, end_marker: str) -> str:
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise ValueError(f"expected exactly one {start_marker} and {end_marker}")
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    if start >= end:
        raise ValueError(f"markers are out of order: {start_marker}")
    return text[start:end]


def _assert_lifecycle_markers_in_active_section(text: str) -> None:
    active_start = text.index("# 9. Immediate Next Action")
    active_end = text.index("# 10. Minimal Tools", active_start)
    for marker in (MATRIX_START, MATRIX_END, JSON_START, JSON_END):
        marker_position = text.index(marker)
        if not active_start < marker_position < active_end:
            raise ValueError(f"lifecycle marker is outside the active section: {marker}")
    marker_names = re.findall(
        r"<!--\s*([^>]*(?:HARDEN_02|HARDEN-02|PRODUCT-MATRIX)[^>]*)\s*-->",
        text,
    )
    marker_names = [name.strip() for name in marker_names]
    allowed = {
        "NEWYOU:PRODUCT-MATRIX:HARDEN-02-LIFECYCLE:START",
        "NEWYOU:PRODUCT-MATRIX:HARDEN-02-LIFECYCLE:END",
        "HARDEN_02_LIFECYCLE_STATE_START",
        "HARDEN_02_LIFECYCLE_STATE_END",
    }
    unexpected = [name for name in marker_names if name not in allowed]
    if unexpected:
        raise ValueError(f"unexpected lifecycle marker(s): {unexpected}")


def _reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _lifecycle_json(text: str) -> dict[str, object]:
    _assert_lifecycle_markers_in_active_section(text)
    region = _marked_region(text, JSON_START, JSON_END)
    matches = re.findall(r"```json\s*(\{.*?\})\s*```", region, re.DOTALL)
    if len(matches) != 1:
        raise ValueError(f"expected one fenced lifecycle JSON object, found {len(matches)}")
    try:
        value = json.loads(matches[0], object_pairs_hook=_reject_duplicate_json_keys)
    except (TypeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("malformed lifecycle JSON") from exc
    if not isinstance(value, dict):
        raise ValueError("lifecycle JSON must be an object")
    return value


def _table_cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def _table_rows_in_section(text: str, start_heading: str, end_heading: str) -> list[list[str]]:
    section = _section(text, start_heading, end_heading)
    rows = [_table_cells(line) for line in section.splitlines()]
    rows = [row for row in rows if row]
    if rows.count(["Source", "Use"]) != 1:
        raise ValueError(f"expected one source table under {start_heading}")
    return [
        row
        for row in rows
        if row != ["Source", "Use"]
        and not all(re.fullmatch(r":?-+", cell) for cell in row)
    ]


def _manifest_authority_filenames() -> dict[str, str]:
    try:
        manifest = json.loads(_read(MANIFEST))
        governing = {
            entry["document_id"]: entry
            for entry in manifest["governing_documents"]
        }
        filenames: dict[str, str] = {}
        for document_id in CURRENT_AUTHORITY_DOCUMENT_IDS:
            entry = governing[document_id]
            filename = entry["canonical_filename"]
            if entry["repository_path"] != f"docs/00_platform/{filename}":
                raise ValueError(f"manifest path is inconsistent for {document_id}")
            filenames[document_id] = filename
        return filenames
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ValueError("current authority manifest cannot resolve all required sources") from exc


def _validate_contract_source_routing(text: str) -> None:
    _assert_unique_headings(text)
    authority_rows = _table_rows_in_section(
        text,
        "### CURRENT AUTHORITY",
        "### CURRENT DERIVED EVIDENCE",
    )
    if len(authority_rows) != len(CURRENT_AUTHORITY_DOCUMENT_IDS):
        raise ValueError("CURRENT AUTHORITY source table has missing or unexpected rows")
    if any(len(row) != 2 for row in authority_rows):
        raise ValueError("CURRENT AUTHORITY source table has a malformed row")
    actual = [row[0].strip("`") for row in authority_rows]
    current = _manifest_authority_filenames()
    expected = [current[document_id] for document_id in CURRENT_AUTHORITY_DOCUMENT_IDS]
    if actual != expected:
        raise ValueError("CURRENT AUTHORITY rows do not match the current manifest routes")

    readme_context = _section(_read(README), "## Default Agent Context", "## Active Working Artifacts")
    readme_paths = re.findall(r"`([^`]+\.md)`", readme_context)
    if any(filename not in readme_paths for filename in expected):
        raise ValueError("CURRENT AUTHORITY rows do not match the README current routes")

    derived_rows = _table_rows_in_section(
        text,
        "### CURRENT DERIVED EVIDENCE",
        "### HISTORICAL AUTHORITY / WORKING EVIDENCE",
    )
    if len(derived_rows) != 3 or any(len(row) != 2 for row in derived_rows):
        raise ValueError("current derived/source-at-freeze table has missing or unexpected rows")
    derived = {row[0].strip("`"): row[1] for row in derived_rows}
    atlas_path = "working/DELIVERY_ATLAS_WORKING_v0.3.3.md"
    skeleton_path = "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
    identity_path = "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
    if set(derived) != {atlas_path, skeleton_path, identity_path}:
        raise ValueError("derived/source-at-freeze rows do not identify the current artifacts")
    atlas_use = derived[atlas_path].casefold()
    if "derived" not in atlas_use or "non-authoritative" not in atlas_use:
        raise ValueError("current Atlas must remain derived and non-authoritative")
    if "working/delivery_atlas_working_v0.2.1.md" not in atlas_use:
        raise ValueError("pinned Atlas v0.2.1 source-at-freeze evidence is not identified")
    if "source-at-freeze" not in atlas_use or "not current navigation" not in atlas_use:
        raise ValueError("pinned Atlas v0.2.1 must be classified as source-at-freeze only")
    if "phase 7a" not in derived[skeleton_path].casefold():
        raise ValueError("current FP-001 Skeleton is not identified as the Phase 7A artifact")
    identity_use = derived[identity_path].casefold()
    for required in (
        "source-at-freeze / reconciliation evidence",
        "not current lifecycle authority",
        "later fp-001 reconciliation",
        "current open work",
    ):
        if required not in identity_use:
            raise ValueError("Identity dossier is not classified as source-at-freeze evidence")

    readme = _read(README)
    if "working/DELIVERY_ATLAS_WORKING_v0.3.3.md" not in readme:
        raise ValueError("README does not route current Atlas to v0.3.3")
    if "The unchanged v0.2.1 working path remains available to existing FP-001 and HARDEN-02 source-at-freeze references." not in readme:
        raise ValueError("README does not preserve Atlas v0.2.1 as source-at-freeze evidence")
    atlas_routing = _section(readme, "## Delivery Atlas routing", "## Machine-readable inventory")
    if "[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.3.3.md)" not in atlas_routing:
        raise ValueError("README Delivery Atlas navigation does not target v0.3.3")
    if "working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md" not in readme:
        raise ValueError("README does not route the current HARDEN status successor")
    active = _active_window(_read(OPEN_WORK))
    if "- IDENTITY & ACCESS: COMPLETE / MERGED" not in active:
        raise ValueError("current Identity lifecycle status is not sourced from Open Work")
    if "CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md" not in active:
        raise ValueError("Open Work does not route the current HARDEN status successor")


def _lifecycle_matrix(text: str) -> dict[str, dict[str, str]]:
    _assert_lifecycle_markers_in_active_section(text)
    region = _marked_region(text, MATRIX_START, MATRIX_END)
    rows = [_table_cells(line) for line in region.splitlines()]
    rows = [row for row in rows if row]
    if rows.count(["gate", "status", "evidence"]) != 1:
        raise ValueError("lifecycle matrix must have one exact header")
    data = [row for row in rows if row != ["gate", "status", "evidence"]]
    data = [row for row in data if not all(re.fullmatch(r":?-+", cell) for cell in row)]
    if len(data) != len(EXPECTED_MATRIX_GATES):
        raise ValueError(f"expected {len(EXPECTED_MATRIX_GATES)} lifecycle rows, found {len(data)}")
    if any(len(row) != 3 or not all(row) for row in data):
        raise ValueError("lifecycle matrix contains a malformed row")
    gates = [row[0].strip("`") for row in data]
    if tuple(gates) != EXPECTED_MATRIX_GATES:
        raise ValueError(f"unexpected lifecycle matrix gate order: {gates}")
    return {
        gate: {"status": row[1].strip("`"), "evidence": row[2]}
        for gate, row in zip(gates, data)
    }


def _active_window(text: str) -> str:
    return _section(text, "# 9. Immediate Next Action", "# 10. Minimal Tools")


def _inject_active_statement(text: str, statement: str) -> str:
    active = _active_window(text)
    anchor = "H02-3R POST-EXECUTION ROUTE:"
    if active.count(anchor) != 1:
        raise ValueError("active execution section is missing its unique route anchor")
    contaminated = active.replace(anchor, f"{statement}\n{anchor}", 1)
    return text.replace(active, contaminated, 1)


def _route_declarations(text: str, label: str) -> list[str]:
    return re.findall(rf"(?m)^{re.escape(label)}:\s*(.+?)\s*$", text)


def _route_state(text: str, state: dict[str, object]) -> bool:
    try:
        _assert_lifecycle_markers_in_active_section(text)
    except ValueError:
        return False
    current = _route_declarations(text, "CURRENT AUTHORITY-STAGE PROGRAMME")
    next_stage = _route_declarations(text, "NEXT STAGE")
    if len(current) != 1 or len(next_stage) != 1:
        return False
    active = _active_window(text)
    if active.count(f"CURRENT AUTHORITY-STAGE PROGRAMME: {current[0]}") != 1:
        return False
    if active.count(f"NEXT STAGE: {next_stage[0]}") != 1:
        return False
    return (
        current[0] == CURRENT_STAGE
        and next_stage == [NEXT_STAGE]
        and state.get("current_stage") == current[0]
        and state.get("next_stage") == NEXT_STAGE
    )


def _roadmap_phase7_section(text: str) -> tuple[str, int]:
    heading = "# 21. Phase 7 handoff"
    starts = list(re.finditer(rf"(?m)^{re.escape(heading)}\s*$", text))
    if len(starts) != 1:
        raise ValueError(f"expected one Roadmap {heading!r}, found {len(starts)}")
    start = starts[0].start()
    next_headings = list(re.finditer(r"(?m)^#\s+.+?\s*$", text[start + len(heading):]))
    if next_headings:
        end = start + len(heading) + next_headings[0].start()
    else:
        end = len(text)
    if start >= end:
        raise ValueError("Roadmap Phase 7 handoff section has invalid boundaries")
    return text[start:end], start


def _markdown_bullet_items(text: str, *, offset: int = 0) -> list[tuple[int, str]]:
    items: list[tuple[int, str]] = []
    active_start: int | None = None
    active_parts: list[str] = []
    fence_char: str | None = None
    fence_length = 0

    def finish() -> None:
        nonlocal active_start, active_parts
        if active_start is not None:
            items.append((offset + active_start, " ".join(active_parts)))
        active_start = None
        active_parts = []

    line_offset = 0
    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        if fence_char is not None:
            closing_fence = re.fullmatch(
                rf" {{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*",
                content,
            )
            if closing_fence is not None:
                finish()
                fence_char = None
                fence_length = 0
            line_offset += len(line)
            continue

        opening_fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", content)
        if opening_fence is not None:
            marker = opening_fence.group(1)
            suffix = opening_fence.group(2)
            if marker[0] != "`" or "`" not in suffix:
                finish()
                fence_char = marker[0]
                fence_length = len(marker)
                line_offset += len(line)
                continue

        bullet = re.match(r"^[ \t]*[-*+][ \t]+(.*)$", content)
        if bullet:
            finish()
            active_start = line_offset + bullet.start()
            active_parts = [bullet.group(1).strip()]
        elif active_start is not None and content.strip() and re.match(r"^[ \t]{2,}\S", content):
            active_parts.append(content.strip())
        elif content.strip():
            finish()
        line_offset += len(line)
    finish()
    return items

def _roadmap_phase7_handoff_requirements(text: str) -> list[int]:
    """Validate Roadmap §21's state boundary and ordered Phase 7 task contract."""
    handoff, section_offset = _roadmap_phase7_section(text)
    anchor = "When current Open Work authorises a Phase 7 task, that task must:"
    anchor_matches = list(re.finditer(rf"(?m)^{re.escape(anchor)}\s*$", handoff))
    document_anchors = list(re.finditer(rf"(?m)^{re.escape(anchor)}\s*$", text))
    if len(anchor_matches) != 1 or len(document_anchors) != 1:
        raise ValueError("Roadmap §21 must contain one Phase 7 task-contract anchor")
    if document_anchors[0].start() != section_offset + anchor_matches[0].start():
        raise ValueError("Roadmap Phase 7 task-contract anchor is outside §21")

    summary_block = handoff[len("# 21. Phase 7 handoff") : anchor_matches[0].start()].strip()
    summary_paragraphs = [
        re.sub(r"\s+", " ", paragraph.replace("`", "")).strip().casefold()
        for paragraph in re.split(r"\n\s*\n", summary_block)
        if paragraph.strip()
    ]
    # Integrity witness for the current authoritative Roadmap §21 summary, not a new authority.
    # Any summary prose change must fail closed until this witness is deliberately reviewed and updated.
    expected_summary_paragraphs = (
        (
            "This Roadmap defines the approved outcome sequence, dependencies and gates. "
            "It does not select or own the active task or stage, grant execution authorisation, "
            "or record current programme status. README and current Open Work own programme routing "
            "and current task/stage selection; use those current sources for operational status. "
            "This Roadmap records the approved sequence and gate boundaries only."
        ),
        (
            "FP-001 has existing Phase 7A work and an Identity & Access dossier. "
            "The narrow PMR artifact reconciliation remains required after certified Engineering "
            "Standards Authority Promotion and has not been performed. Phase 7C remains gated, "
            "proof classification is not finalised, and executable authentication proof is incomplete."
        ),
    )
    expected_summary_paragraphs = tuple(
        re.sub(r"\s+", " ", paragraph).strip().casefold()
        for paragraph in expected_summary_paragraphs
    )
    if tuple(summary_paragraphs) != expected_summary_paragraphs:
        raise ValueError(
            "Roadmap §21 summary must exactly preserve the reviewed two-paragraph Phase 7 boundary"
        )

    anchor_end = anchor_matches[0].end()
    tail = handoff[anchor_end:]
    diagram_matches = list(re.finditer(r"(?m)^```text[ \t]*$", tail))
    if len(diagram_matches) != 1:
        raise ValueError("Roadmap §21 task contract must transition once into the text phase diagram")

    task_block = tail[: diagram_matches[0].start()]
    nonblank_task_lines = [
        line.rstrip("\r\n")
        for line in task_block.splitlines(keepends=True)
        if line.strip()
    ]
    if any(
        re.match(r"^[-*+][ \t]+\S", line) is None
        for line in nonblank_task_lines
    ):
        raise ValueError(
            "Roadmap §21 task block may contain only top-level unordered task bullets"
        )

    task_bullets = _markdown_bullet_items(task_block, offset=anchor_end)
    if len(task_bullets) != 7:
        raise ValueError(
            f"Roadmap §21 task contract must contain exactly seven bullets, found {len(task_bullets)}"
        )

    post_task = tail[diagram_matches[0].start():]
    post_task_lines = post_task.splitlines(keepends=True)
    if not post_task_lines or re.fullmatch(
        r"```text[ \t]*(?:\r?\n)?",
        post_task_lines[0],
    ) is None:
        raise ValueError("Roadmap §21 phase diagram must begin with a text fence")

    closing_fence_index = next(
        (
            index
            for index, line in enumerate(post_task_lines[1:], start=1)
            if re.fullmatch(r"```[ \t]*(?:\r?\n)?", line)
        ),
        None,
    )
    if closing_fence_index is None:
        raise ValueError("Roadmap §21 phase diagram is missing its closing fence")

    post_diagram = "".join(post_task_lines[closing_fence_index + 1 :])
    if post_diagram.strip() != "Do not advance the current stage from this Roadmap patch.":
        raise ValueError(
            "Roadmap §21 task contract must transition directly to the phase diagram "
            "and the fail-closed stage-advance sentence"
        )

    def normalized(item: str) -> str:
        return re.sub(r"\s+", " ", item.replace("`", "")).casefold()

    requirement_rules = (
        (
            "Roadmap FP-001 outcome and dependencies",
            re.compile(r"use this roadmap['’]s fp-001 outcome and dependencies[.;]?"),
        ),
        (
            "upstream Product, Architecture and Domain authority",
            re.compile(r"preserve upstream product, architecture and domain authority[.;]?"),
        ),
        (
            "required JIT Domain Dossiers",
            re.compile(r"create only the jit domain dossiers required by the selected pack[.;]?"),
        ),
        (
            "OQ-034/OQ-035/OQ-036 Phase 7 and Phase 8 boundary",
            re.compile(
                r"use the resolved oq-034 architecture selection and "
                r"preserve its incomplete phase 8 proof obligation; "
                r"resolve oq-035\s*/\s*oq-036 only at the affected depth[.;]?"
            ),
        ),
        (
            "affected-depth OQ-039 mapping",
            re.compile(
                r"perform implementation[- ]grade oq-039 mapping only for affected domains/actions[.;]?"
            ),
        ),
        (
            "final proof vehicle choice",
            re.compile(
                r"make the final proof choice reuse_existing_proof or new_tracer_bullet[.;]?"
            ),
        ),
        (
            "fail-closed invention STOP condition",
            re.compile(
                r"stop if a task would need to invent product policy, clinical thresholds, "
                r"ownership, provider semantics, retention, security exceptions,? or "
                r"implementation[- ]grade domain semantics[.;]?"
            ),
        ),
    )
    document_requirement_rules = (
        re.compile(r"\buse this roadmap['’]s fp-001 outcome and dependencies\b"),
        re.compile(r"\bpreserve upstream product, architecture and domain authority\b"),
        re.compile(r"\bcreate only the jit domain dossiers required by the selected pack\b"),
        re.compile(
            r"\buse the resolved oq-034 architecture selection\b"
            r".*\bpreserve its incomplete phase 8 proof obligation\b"
            r".*\bresolve oq-035\s*/\s*oq-036 only at the affected depth\b"
        ),
        re.compile(
            r"\bperform implementation[- ]grade oq-039 mapping only for affected domains/actions\b"
        ),
        re.compile(
            r"\bmake the final proof choice reuse_existing_proof or new_tracer_bullet\b"
        ),
        re.compile(
            r"(?=.*\bstop if\b)(?=.*\btask\b)(?=.*\binvent\b)"
            r"(?=.*\bproduct policy\b)(?=.*\bclinical thresholds\b)"
            r"(?=.*\bownership\b)(?=.*\bprovider semantics\b)"
            r"(?=.*\bretention\b)(?=.*\bsecurity exceptions\b)"
            r"(?=.*\bimplementation[- ]grade domain semantics\b)"
        ),
    )

    block_matches: list[tuple[int, str]] = []
    for index, ((label, pattern), (position, item)) in enumerate(
        zip(requirement_rules, task_bullets),
        start=1,
    ):
        if pattern.fullmatch(normalized(item)) is None:
            raise ValueError(
                f"Roadmap §21 task-contract bullet {index} does not exactly match {label}"
            )
        block_matches.append((position, item))

    if len({position for position, _ in block_matches}) != 7:
        raise ValueError("Roadmap §21 Phase 7 requirements must use seven distinct bullets")

    if any(
        earlier[0] >= later[0]
        for earlier, later in zip(block_matches, block_matches[1:])
    ):
        raise ValueError("Roadmap §21 Phase 7 task requirements are out of order")

    document_bullets = _markdown_bullet_items(text)
    expected_positions = [section_offset + position for position, _ in block_matches]
    for (label, _), pattern, expected_position in zip(
        requirement_rules,
        document_requirement_rules,
        expected_positions,
    ):
        matches = [
            position
            for position, item in document_bullets
            if pattern.search(normalized(item))
        ]
        if matches != [expected_position]:
            raise ValueError(f"Roadmap §21 {label} must occur once and only inside §21")

    return [position for position, _ in block_matches]


def _phase_order(text: str, *, source: str) -> list[int]:
    if source == "pom":
        handoff = _section(text, "# 25. Phase 7 / JIT handoff", "# 26. Development boundary")
        canonical = "Feature Pack Skeleton + Gate Manifest → required JIT Domain Dossiers → Final Feature Pack Contract"
        if handoff.count(canonical) != 1:
            raise ValueError("Operating Model Phase 7 handoff is missing or duplicated")
        return [handoff.index(phrase) for phrase in (
            "Feature Pack Skeleton + Gate Manifest",
            "required JIT Domain Dossiers",
            "Final Feature Pack Contract",
        )]
    if source == "skeleton":
        handoff = _section(text, "# FP-001 Feature Pack Skeleton and Preliminary Gate Manifest", "## 1. Identity")
        return [handoff.index(phrase) for phrase in (
            "Phase 7A Skeleton",
            "Phase 7B required JIT Domain Dossiers",
            "Phase 7C Final Feature Pack Contract",
        )]
    if source == "roadmap":
        handoff, _ = _roadmap_phase7_section(text)
        required = (
            "FP-001 has existing Phase 7A work",
            "Phase 7C remains gated",
            "proof classification",
            "executable authentication proof is incomplete",
        )
        summary_positions = [handoff.casefold().index(phrase.casefold()) for phrase in required]
        return summary_positions + _roadmap_phase7_handoff_requirements(text)
    if source == "open_work":
        handoff = _section(text, "## Phase 7 — Feature Pack Preparation + JIT Domain Dossiers", "# 8. Product Planning Stop Condition")
        required = (
            "### 7A",
            "### 7B",
            "### 7C",
            "## Phase 8",
        )
        return [handoff.casefold().index(phrase.casefold()) for phrase in required]
    raise ValueError(f"unknown Phase 7 source: {source}")


def _line_in_span(text: str, line_number: int, start: str, end: str | None) -> bool:
    starts = [match.start() for match in re.finditer(rf"(?m)^{re.escape(start)}.*$", text)]
    if len(starts) != 1:
        return False
    start_line = text[: starts[0]].count("\n")
    if end is None:
        end_line = len(text.splitlines())
    else:
        ends = [match.start() for match in re.finditer(rf"(?m)^{re.escape(end)}.*$", text)]
        if len(ends) != 1:
            return False
        end_line = text[: ends[0]].count("\n")
    return start_line <= line_number < end_line


def _line_in_marked_region(text: str, line_number: int, start_marker: str, end_marker: str) -> bool:
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        return False
    start_line = text[: text.index(start_marker)].count("\n")
    end_line = text[: text.index(end_marker)].count("\n")
    return start_line <= line_number <= end_line


def _normalise_document_diff(
    successor: str,
    predecessor: str,
    reverse_line: Callable[[str], str | None],
    *,
    allowed_insertions: tuple[str, ...] = (),
    check_unique_headings: bool = True,
) -> str:
    if not successor or not predecessor:
        raise ValueError("successor and predecessor are required")
    if check_unique_headings:
        _assert_unique_headings(successor)
        _assert_unique_headings(predecessor)
    successor_lines = successor.splitlines(keepends=True)
    predecessor_lines = predecessor.splitlines(keepends=True)
    matcher = difflib.SequenceMatcher(
        None,
        predecessor_lines,
        successor_lines,
        autojunk=False,
    )
    normalised: list[str] = []
    for tag, old_start, old_end, new_start, new_end in matcher.get_opcodes():
        old_lines = predecessor_lines[old_start:old_end]
        new_lines = successor_lines[new_start:new_end]
        if tag == "equal":
            normalised.extend(new_lines)
            continue
        if tag == "delete":
            raise ValueError("successor removes predecessor content")

        restored: list[str] = []
        for line in new_lines:
            if line.rstrip("\r\n") in allowed_insertions:
                continue
            reversed_line = reverse_line(line)
            if reversed_line is not None:
                restored.append(reversed_line)
                continue
            raise ValueError(f"successor line changed outside declared normalization: {line.strip()[:180]}")
        if restored != old_lines:
            raise ValueError(
                "successor hunk does not normalize exactly to its predecessor: "
                f"old={old_lines[:2]!r}, normalized={restored[:2]!r}"
            )
        normalised.extend(restored)

    result = "".join(normalised)
    if result != predecessor:
        raise ValueError("successor normalization does not reproduce predecessor bytes")
    return result


def _reverse_line_with_pairs(line: str, pairs: tuple[tuple[str, str], ...]) -> str | None:
    body = line.rstrip("\r\n")
    ending = line[len(body) :]
    restored = body
    for current, previous in sorted(pairs, key=lambda item: len(item[0]), reverse=True):
        restored = restored.replace(current, previous)
    if restored == body:
        return None
    return restored + ending


def _replace_exact(text: str, current: str, previous: str) -> str:
    if text.count(current) != 1:
        raise ValueError(f"expected one declared successor delta: {current[:80]!r}")
    return text.replace(current, previous, 1)


def _line_with_prefix(text: str, prefix: str) -> str:
    matches = [line for line in text.splitlines() if line.startswith(prefix)]
    if len(matches) != 1:
        raise ValueError(f"expected one line starting {prefix!r}, found {len(matches)}")
    return matches[0]


def _normalise_open_work_successor(successor: str, predecessor: str) -> str:
    _assert_lifecycle_markers_in_active_section(successor)
    _assert_lifecycle_markers_in_active_section(predecessor)
    successor_state = _lifecycle_json(successor)
    if successor_state.get("harden_02_execution") != EXECUTION_STATUS:
        raise ValueError("lifecycle JSON execution status is not certified")
    if successor_state.get("current_stage") != CURRENT_STAGE or successor_state.get("next_stage") != NEXT_STAGE:
        raise ValueError("certified execution does not route exclusively to Engineering Standards promotion")
    if successor_state.get("engineering_standards_authority_promotion") != "NEXT / AUTHORISED / NOT STARTED":
        raise ValueError("Engineering Standards promotion is not the sole immediate NEXT stage")
    try:
        _assert_downstream_state(successor_state)
    except AssertionError as exc:
        raise ValueError(str(exc)) from exc
    matrix = _lifecycle_matrix(successor)
    if matrix["EXECUTION"] != {"status": EXECUTION_MATRIX_STATUS, "evidence": EXECUTION_MATRIX_EVIDENCE}:
        raise ValueError("execution matrix does not bind the certified resulting-main evidence")

    restored = successor
    route_pairs = (
        ("PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md", "PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md"),
        ("00_PLATFORM_v1.5.2.md", "00_PLATFORM_v1.5.1.md"),
        ("05_ROADMAP_v1.1.6.md", "05_ROADMAP_v1.1.5.md"),
        ("working/DELIVERY_ATLAS_WORKING_v0.3.3.md", "working/DELIVERY_ATLAS_WORKING_v0.3.2.md"),
        ("working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md", "working/HARDEN-02_CONTRACT_WORKING_v0.4.4.md"),
    )
    for current, previous in route_pairs:
        restored = restored.replace(current, previous)
    restored = _replace_exact(restored, "# 02_OPEN_WORK_v1.2.51.md", "# 02_OPEN_WORK_v1.2.50.md")
    restored = _replace_exact(
        restored,
        "PRODUCT LAW AND GOVERNANCE HARDENING OPEN-WORK SUCCESSOR v1.2.51",
        "PRODUCT LAW AND GOVERNANCE HARDENING OPEN-WORK SUCCESSOR v1.2.50",
    )
    restored = _replace_exact(restored, "Document version:** v1.2.51", "Document version:** v1.2.50")
    restored = _replace_exact(restored, "`archive/02_OPEN_WORK_v1.2.50.md`", "`archive/02_OPEN_WORK_v1.2.49.md`")
    restored = _replace_exact(
        restored,
        "`v1.2.50 → v1.2.51` — certified HARDEN-02 execution status transition; only Engineering Standards Authority Promotion becomes NEXT.",
        "`v1.2.49 → v1.2.50` — current-authority routing only; no downstream gate advances.",
    )
    restored = _replace_exact(
        restored,
        "- **Patch scope:** PATCH / certified HARDEN-02 execution status + immediate H02-3R route transition + current-source routing only.",
        "- **Patch scope:** PATCH / current-authority and derived-navigation route substitutions only.",
    )
    restored = _replace_exact(
        restored,
        "lifecycle completion is recorded in current v0.4.5",
        "lifecycle completion is recorded in current v0.4.4",
    )
    restored = _replace_exact(
        restored,
        "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.2.md`",
        "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.1.md`",
    )
    restored = _replace_exact(
        restored,
        "current status recorded by working v0.4.5",
        "current status recorded by working v0.4.4",
    )

    changelog = """- Planning-state SemVer transition: `v1.2.50 → v1.2.51`.
- Records certified HARDEN-02 execution after I-01…I-13 PASS on final resulting main, exact recovery CI/review/attestation evidence, and routes NEXT exclusively to `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`.
- Preserves FP-001 reconciliation as downstream until certified Engineering Standards Authority Promotion; Communications, conditional dossiers, Phase 7C, proof classification and Phase 8 remain at their existing downstream/blocked states.
- Archives Open Work v1.2.50 byte-identically; refreshes current Product/Roadmap/Atlas/HARDEN successor routes only.
- Retains the PR #59 reviewer’s phase-diagram-body helper-test note as a non-blocking hardening observation; it creates no new gate.

"""
    if restored.count(changelog) != 1:
        raise ValueError("certification changelog is missing, duplicated, or altered")
    restored = restored.replace(changelog, "", 1)

    restored = restored.replace(
        _line_with_prefix(restored, "- **Current planning position:**"),
        _line_with_prefix(predecessor, "- **Current planning position:**"),
        1,
    )
    restored = _replace_exact(
        restored,
        "CURRENT AUTHORITY-STAGE PROGRAMME: ENGINEERING STANDARDS AUTHORITY PROMOTION\nNEXT STAGE: ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
        "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING\nNEXT STAGE: HARDEN-02_EXECUTION_REQUIRED",
    )
    restored = _replace_exact(
        restored,
        "HARDEN-02 EXECUTION: COMPLETE / CERTIFIED\nENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
        "HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING\nENGINEERING STANDARDS AUTHORITY PROMOTION: DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED",
    )
    restored = _replace_exact(
        restored,
        "| `EXECUTION` | `COMPLETE_CERTIFIED` | `I-01…I-13 PASS on resulting main 6fea69eadf18f2fb79d78c2a94ab035b10abe31f; run 36567933267; PR #59 durable post-merge attestation 5890574449` |",
        "| `EXECUTION` | `IN_PROGRESS_NOT_COMPLETE_CERTIFICATION_PENDING` | `I-01…I-13 execution proofs in progress; certification remains pending` |",
    )

    successor_region = _marked_region(restored, JSON_START, JSON_END)
    predecessor_region = _marked_region(predecessor, JSON_START, JSON_END)
    restored = restored.replace(successor_region, predecessor_region, 1)

    evidence_start = restored.find("HARDEN-02 execution certification evidence:")
    if evidence_start < 0:
        raise ValueError("certified execution evidence paragraph is missing")
    evidence_end = restored.find(MATRIX_START, evidence_start)
    if evidence_end < 0:
        raise ValueError("certified execution evidence is not adjacent to the lifecycle matrix")
    restored = restored[:evidence_start] + restored[evidence_end:]

    if restored != predecessor:
        diff = "\n".join(difflib.unified_diff(predecessor.splitlines(), restored.splitlines(), lineterm=""))
        raise ValueError(f"Open Work successor contains undeclared changes:\n{diff[:4000]}")
    return predecessor


def _normalise_contract_successor(successor: str, predecessor: str) -> str:
    _validate_contract_source_routing(successor)
    if "HARDEN-02 execution **COMPLETE / CERTIFIED**" not in "\n".join(successor.splitlines()[:25]):
        raise ValueError("contract successor does not record certified HARDEN execution")
    if "Engineering Standards Authority Promotion **NEXT / AUTHORISED / NOT STARTED**" not in "\n".join(successor.splitlines()[:25]):
        raise ValueError("contract successor does not expose only the next promotion stage")
    restored = successor
    for current, previous in (
        ("PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md", "PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md"),
        ("00_PLATFORM_v1.5.2.md", "00_PLATFORM_v1.5.1.md"),
        ("02_OPEN_WORK_v1.2.51.md", "02_OPEN_WORK_v1.2.50.md"),
        ("05_ROADMAP_v1.1.6.md", "05_ROADMAP_v1.1.5.md"),
        ("working/DELIVERY_ATLAS_WORKING_v0.3.3.md", "working/DELIVERY_ATLAS_WORKING_v0.3.2.md"),
    ):
        restored = restored.replace(current, previous)
    restored = _replace_exact(restored, "# HARDEN-02_CONTRACT_WORKING_v0.4.5.md", "# HARDEN-02_CONTRACT_WORKING_v0.4.4.md")
    restored = _replace_exact(restored, "- **Plan / contract version:** `v0.4.5`", "- **Plan / contract version:** `v0.4.4`")
    restored = _replace_exact(
        restored,
        "- **Status:** Original v0.4.0 contract lifecycle **COMPLETE / CERTIFIED** — HARDEN-02 execution **COMPLETE / CERTIFIED** — Engineering Standards Authority Promotion **NEXT / AUTHORISED / NOT STARTED**",
        "- **Status:** Original v0.4.0 contract lifecycle **COMPLETE / CERTIFIED** — HARDEN-02 execution **IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING**",
    )
    restored = _replace_exact(
        restored,
        "- **Predecessor v0.4.4 routing-successor base main SHA:** `4efdac4fe3c79b96b18a243800e47c71e7d369b8`\n- **Execution-certification resulting main SHA:** `6fea69eadf18f2fb79d78c2a94ab035b10abe31f`",
        "- **Predecessor v0.4.3 routing-successor base main SHA:** `4efdac4fe3c79b96b18a243800e47c71e7d369b8`",
    )
    restored = _replace_exact(
        restored,
        "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.4.md` — preserved byte-identically as the prior in-progress/current-routing status snapshot",
        "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.3.md` — preserved byte-identically as the prior completed-contract status snapshot",
    )
    restored = _replace_exact(
        restored,
        "- **Certified contract semantics:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md` — the original v0.4.0 semantics are certified; this v0.4.5 successor preserves them and records certified execution status plus current-source routing/provenance",
        "- **Certified contract semantics:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md` — the original v0.4.0 semantics are certified; this v0.4.4 successor preserves them and records execution status plus current-source routing/provenance",
    )
    revision = "- `v0.4.5` — PATCH execution-certification status successor. Records I-01…I-13 PASS and the prospective PR #57/#59 recovery certification culminating in resulting main `6fea69eadf18f2fb79d78c2a94ab035b10abe31f`; routes NEXT exclusively to `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`. It preserves H02-1/H02-2/H02-3R, every v0.4.0 scope/invariant, and all later gates. The PR #59 direct phase-diagram-body helper mutation-test note remains non-blocking evidence-led hardening.\n"
    if restored.count(revision) != 1:
        raise ValueError("v0.4.5 revision entry is missing or duplicated")
    restored = restored.replace(revision, "", 1)

    evidence_start = restored.find("### 11.6 HARDEN-02 execution certification evidence")
    evidence_end = restored.find("HARDEN-02 remains governance sequencing.", evidence_start)
    if evidence_start < 0 or evidence_end < 0:
        raise ValueError("execution certification evidence section is missing or relocated")
    restored = restored[:evidence_start] + restored[evidence_end:]

    restored = _replace_exact(
        restored,
        "This status-sync artifact records already-certified HARDEN-02 execution; it does not execute Engineering Standards Authority Promotion.",
        "This status-sync artifact itself does not execute HARDEN-02.",
    )
    restored = _replace_exact(
        restored,
        "HARDEN-02 execution is COMPLETE / CERTIFIED. I-01…I-13 pass on resulting main `6fea69eadf18f2fb79d78c2a94ab035b10abe31f`, and the applicable prospective recovery lifecycle is complete through resulting-main CI, fresh independent post-merge review and durable post-merge attestation. Engineering Standards Authority Promotion is NEXT / AUTHORISED / NOT STARTED; this status successor does not perform or certify that promotion.",
        "Current HARDEN-02 execution is IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING, begun from execution-start baseline main SHA `1c8fc94058176795d88cb82e08857e3d30c553e9`. Do not mark execution COMPLETE / CERTIFIED until I-01…I-13 execution proofs PASS and the applicable unchanged-merge, resulting-main CI, fresh post-merge review and durable post-merge certification lifecycle is complete.",
    )
    if restored != predecessor:
        diff = "\n".join(difflib.unified_diff(predecessor.splitlines(), restored.splitlines(), lineterm=""))
        raise ValueError(f"HARDEN status successor contains undeclared changes:\n{diff[:4000]}")
    return predecessor


def _normalise_atlas_successor(successor: str, predecessor: str) -> str:
    restored = successor
    restored = _replace_exact(restored, "# Delivery Atlas working v0.3.3", "# Delivery Atlas working v0.3.2")
    restored = _replace_exact(
        restored,
        "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.2.md` (routing predecessor; preserved byte-identically). Earlier v0.2.0, v0.2.1, v0.2.2, v0.2.3, v0.3.0 and v0.3.1 predecessors remain preserved.",
        "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.1.md` (routing predecessor; preserved byte-identically). Earlier v0.2.0, v0.2.1, v0.2.2 and v0.2.3 predecessors remain preserved.",
    )
    restored = _replace_exact(
        restored,
        "- **SemVer transition:** `v0.3.2 → v0.3.3` (PATCH: current-source routing and provenance only; Atlas authority and delivery content are unchanged).",
        "- **SemVer transition:** `v0.3.1 → v0.3.2` (PATCH: current-source routing and provenance only; Atlas authority and delivery content are unchanged).",
    )
    restored = restored.replace(
        _line_with_prefix(restored, "- **Current content state:**"),
        _line_with_prefix(predecessor, "- **Current content state:**"),
        1,
    )
    for current, previous in (
        ("docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md", "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md"),
        ("docs/00_platform/00_PLATFORM_v1.5.2.md", "docs/00_platform/00_PLATFORM_v1.5.1.md"),
        ("docs/00_platform/02_OPEN_WORK_v1.2.51.md", "docs/00_platform/02_OPEN_WORK_v1.2.50.md"),
        ("docs/00_platform/05_ROADMAP_v1.1.6.md", "docs/00_platform/05_ROADMAP_v1.1.5.md"),
        ("current Open Work `v1.2.51`", "current Open Work `v1.2.50`"),
        ("Product `v1.5.2`", "Product `v1.5.1`"),
        ("Roadmap `v1.1.6`", "Roadmap `v1.1.5`"),
    ):
        restored = restored.replace(current, previous)
    restored = _replace_exact(
        restored,
        "`05_ROADMAP_v1.1.6.md §6 FP-001`, with dependency and phase context in §§3.2, 5 and 14; `04_DOMAIN_MAP_v1.2.0.md §§3–5 and §6.1`; Product PMR law in `00_PLATFORM_v1.5.2.md §21P` / `DEC-297`; current gate and planning routing in `02_OPEN_WORK_v1.2.51.md`.",
        "`05_ROADMAP_v1.1.5.md §6 FP-001`, with dependency and phase context in §§3.2, 5 and 14; `04_DOMAIN_MAP_v1.2.0.md §§3–5 and §6.1`; Product PMR law in `00_PLATFORM_v1.5.1.md §21P` / `DEC-297`; current gate and planning routing in `02_OPEN_WORK_v1.2.50.md`.",
    )
    if restored != predecessor:
        diff = "\n".join(difflib.unified_diff(predecessor.splitlines(), restored.splitlines(), lineterm=""))
        raise ValueError(f"Atlas successor contains undeclared changes:\n{diff[:4000]}")
    return predecessor


def _assert_downstream_state(state: dict[str, object]) -> None:
    expected = {
        "engineering_standards_authority_promotion": "NEXT / AUTHORISED / NOT STARTED",
        "fp001_reconciliation": "REQUIRED / DOWNSTREAM / NOT PERFORMED",
        "communications": "REQUIRED / NOT_STARTED",
        "phase_7c": "BLOCKED / NOT_STARTED",
        "proof_classification": "NOT FINALISED",
        "application_implementation": "BLOCKED",
        "store_cer": "EXCLUDED",
    }
    for key, value in expected.items():
        if state.get(key) != value:
            raise AssertionError(f"unexpected lifecycle state for {key}: {state.get(key)!r}")
    conditional = state.get("conditional_dossiers")
    if conditional != {
        "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "analytics": "NOT REQUIRED",
    }:
        raise AssertionError(f"unexpected conditional-dossier state: {conditional!r}")


def _execution_state_is_valid(text: str, state: dict[str, object]) -> bool:
    try:
        if not _route_state(text, state):
            return False
        _assert_downstream_state(state)
        matrix = _lifecycle_matrix(text)
    except (AssertionError, ValueError):
        return False
    expected_statuses = {
        "CONTRACT_LIFECYCLE": "COMPLETE / CERTIFIED",
        "PRE_MERGE_CERTIFICATION": "COMPLETE",
        "EXACT_HEAD_CI": "PASS",
        "CERTIFIED_HEAD_MERGE": "COMPLETE_UNCHANGED",
        "RESULTING_MAIN_CI": "PASS",
        "POST_MERGE_INDEPENDENT_REVIEW": "PASS",
        "POST_MERGE_ATTESTATION": "COMPLETE",
        "EXECUTION": EXECUTION_MATRIX_STATUS,
    }
    if {gate: row["status"] for gate, row in matrix.items()} != expected_statuses:
        return False
    if matrix["EXECUTION"]["evidence"] != EXECUTION_MATRIX_EVIDENCE:
        return False
    if state.get("contract_status") != CONTRACT_STATUS:
        return False
    if state.get("certified_contract_version") != "0.4.0":
        return False
    if state.get("harden_02_execution") != EXECUTION_STATUS:
        return False
    if state.get("harden_02_scope") != "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY":
        return False
    if state.get("store_cer") != "EXCLUDED":
        return False
    if state.get("completed_milestones") != [
        "TARGETED PRODUCT AMENDMENT PROGRAMME",
        "FP-001 PHASE 7A",
        "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
        "HARDEN-02 EXECUTION",
    ]:
        return False
    if state.get("conditional_dossiers") != {
        "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "analytics": "NOT REQUIRED",
    }:
        return False
    expected_route = EXPECTED_DOWNSTREAM_ROUTE
    if state.get("downstream_route") != expected_route:
        return False
    active = _active_window(text)
    required_active = (
        "HARDEN-02 v0.4.0 CONTRACT LIFECYCLE: COMPLETE / CERTIFIED",
        f"HARDEN-02 EXECUTION: {EXECUTION_STATUS}",
        "ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
        "FP001_RECONCILIATION_REQUIRED: REQUIRED / DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION / NOT PERFORMED",
        "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION",
        "- IDENTITY & ACCESS: COMPLETE / MERGED",
        "- COMMUNICATIONS: REQUIRED / NOT_STARTED",
        "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED",
        "PHASE 7C: BLOCKED / NOT_STARTED PENDING COMMUNICATIONS AND CONDITIONAL-DOSSIER DISPOSITIONS",
        "PROOF CLASSIFICATION: NOT FINALISED",
        "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
        "STORE / CER: EXCLUDED FROM HARDEN-02",
    )
    if any(active.count(line) != 1 for line in required_active):
        return False
    route_lines = [line.strip("→ ") for line in active.splitlines() if line.lstrip().startswith("→")]
    if active.count("H02-3R POST-EXECUTION ROUTE:") != 1 or route_lines != expected_route[1:]:
        return False
    if _affirmative_prohibited_scope(active):
        return False
    return True


def _affirmative_prohibited_scope(text: str) -> list[str]:
    patterns = (
        r"(?im)^\s*(?:HARDEN-02|H02-1).*\b(?:Product Law|Architecture Law|Domain Law|Roadmap Law|Feature Pack|Horizontal Hardening)\b.*\b(?:is|becomes|owns|requires)\b",
        r"(?im)^\s*HARDEN-02\s+(?:is|becomes|acts as|constitutes)\s+(?:a\s+|an\s+)?(?:Product requirement|Roadmap gate|blocking OQ|Feature Pack|Horizontal Hardening|Store hardening|Commerce/Entitlements hardening)\b",
        r"(?im)^\s*(?:STORE\s*/\s*CER|Store Blueprint|\bCER\b).*\b(?:IN SCOPE|REQUIRED|AUTHORISED|AUTHORIZED|COMPLETE)\b",
        r"(?im)^\s*(?:FP001_RECONCILIATION_REQUIRED|COMMUNICATIONS).*\b(?:COMPLETE|STARTED|AUTHORISED|AUTHORIZED)\b",
        r"(?im)^\s*(?:ENGINEERING STANDARDS AUTHORITY PROMOTION).*\b(?:COMPLETE|EXECUTED|FROZEN|APPROVED)\b",
        r"(?im)^\s*(?:PHASE 7C|PROOF CLASSIFICATION|PHASE 8|EXECUTABLE DEVELOPMENT|APPLICATION IMPLEMENTATION).*\b(?:COMPLETE|APPROVED|PASSED|AUTHORISED|AUTHORIZED|READY)\b",
        r"(?im)^\s*(?:APPLICATION IMPLEMENTATION|EXECUTABLE DEVELOPMENT|TB|VS|HH|PACKAGE INSTALLS?|MIGRATIONS?|PROVIDER CHANGES?)\s*:\s*(?:AUTHORISED|AUTHORIZED|ENABLED|APPROVED|STARTED|IN PROGRESS|COMPLETE|ALLOWED)\b",
        r"(?im)\bStore repository SHA\b",
        r"(?im)\bCER proof obligation\b",
        r"(?im)\bCER exit condition\b",
        r"(?im)\bStore/CER implementation path\b",
    )
    return [
        match.group(0).strip()
        for pattern in patterns
        for match in re.finditer(pattern, text)
    ]


class Harden02ExecutionInvariantTests(unittest.TestCase):
    def _required(self, path: Path) -> str:
        self.assertTrue(path.is_file(), f"missing current successor: {path}")
        return _read(path)

    def _open_work(self) -> str:
        return self._required(OPEN_WORK)

    def _state_and_matrix(self) -> tuple[str, dict[str, object], dict[str, dict[str, str]]]:
        text = self._open_work()
        try:
            return text, _lifecycle_json(text), _lifecycle_matrix(text)
        except ValueError as exc:
            self.fail(str(exc))
            raise AssertionError("unreachable")

    def test_i01_single_unambiguous_next_and_valid_lifecycle_record(self):
        text, state, matrix = self._state_and_matrix()
        self.assertTrue(_execution_state_is_valid(text, state))
        self.assertTrue(_route_state(text, state))
        self.assertEqual(EXECUTION_STATUS, state.get("harden_02_execution"))
        self.assertEqual(EXECUTION_MATRIX_STATUS, matrix["EXECUTION"]["status"])
        self.assertEqual(CONTRACT_STATUS, state.get("contract_status"))
        contract = self._required(CONTRACT)
        self.assertRegex(contract[:2000], r"(?is)status:.*COMPLETE / CERTIFIED")
        self.assertIn("I-01", matrix["EXECUTION"]["evidence"])
        self.assertIn("I-13", matrix["EXECUTION"]["evidence"])
        contradictory = (
            text
            + "\nCURRENT AUTHORITY-STAGE PROGRAMME: FP-001 RECONCILIATION\n"
            + "NEXT STAGE: FP001_RECONCILIATION_REQUIRED\n"
        )
        self.assertFalse(_route_state(contradictory, state))
        self.assertFalse(_execution_state_is_valid(contradictory, state))

    def test_i02_completed_stages_stay_completed(self):
        text, state, _ = self._state_and_matrix()
        self.assertIn("STAGE 1 — TARGETED PRODUCT AMENDMENT GRILL: COMPLETE", text)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE", text)
        self.assertIn("PHASE 7A COMPLETE", text)
        self.assertIn("IDENTITY & ACCESS JIT DOMAIN DOSSIER COMPLETE / MERGED", text)
        self.assertIn("OQ-034 ARCHITECTURE SELECTION RESOLVED", text)
        self.assertIn("TARGETED PRODUCT AMENDMENT PROGRAMME", state.get("completed_milestones", []))
        self.assertIn("FP-001 PHASE 7A", state.get("completed_milestones", []))
        self.assertNotIn("STAGE 1 — TARGETED PRODUCT AMENDMENT GRILL: NEXT", text)
        self.assertNotIn("PHASE 7A: NOT_STARTED", text)
        for milestone in state["completed_milestones"]:
            reopened_state = dict(state)
            reopened_state["completed_milestones"] = [
                value for value in state["completed_milestones"] if value != milestone
            ]
            with self.subTest(reopened=milestone):
                self.assertFalse(_execution_state_is_valid(text, reopened_state))

    def test_i03_only_immediate_downstream_stage_can_be_next(self):
        text, state, _ = self._state_and_matrix()
        _assert_downstream_state(state)
        active = _active_window(text)
        self.assertRegex(
            active,
            r"(?m)^HARDEN-02 EXECUTION:\s*COMPLETE / CERTIFIED\s*$",
        )
        self.assertRegex(
            active,
            r"(?m)^ENGINEERING STANDARDS AUTHORITY PROMOTION:\s*NEXT / AUTHORISED / NOT STARTED\s*$",
        )
        self.assertRegex(
            active,
            r"(?m)^FP001_RECONCILIATION_REQUIRED:\s*REQUIRED / DOWNSTREAM.*NOT PERFORMED\s*$",
        )
        self.assertNotRegex(active, r"(?m)^COMMUNICATIONS:\s*(?:COMPLETE|IN_PROGRESS)")
        self.assertNotRegex(active, r"(?m)^FP001_RECONCILIATION_REQUIRED:\s*(?:COMPLETE|NEXT)")
        premature = text.replace(
            '"engineering_standards_authority_promotion": "NEXT / AUTHORISED / NOT STARTED"',
            '"engineering_standards_authority_promotion": "COMPLETE / CERTIFIED"',
            1,
        )
        self.assertFalse(_execution_state_is_valid(premature, _lifecycle_json(premature)))

    def test_i04_phase7_order_matches_all_current_sources_and_preserves_oq034_proof(self):
        open_work, _, _ = self._state_and_matrix()
        roadmap = _read(ROADMAP)
        self.assertEqual(7, len(_roadmap_phase7_handoff_requirements(roadmap)))
        sources = {
            "pom": _read(POM),
            "roadmap": roadmap,
            "open_work": open_work,
            "skeleton": _read(SKELETON),
        }
        for name, source in sources.items():
            with self.subTest(source=name):
                self.assertTrue(source, f"missing current source for {name}")
                positions = _phase_order(source, source=name)
                self.assertEqual(sorted(positions), positions)
        skeleton_manifest = _section(_read(SKELETON), "## 10. Preliminary Gate Manifest", "## 11. Preliminary performance and scaling review")
        self.assertEqual(1, _read(SKELETON).count("## 10. Preliminary Gate Manifest"))
        self.assertIn("OQ-034", skeleton_manifest)
        self.assertRegex(skeleton_manifest, r"(?i)phase 8 proof required")
        self.assertNotRegex(skeleton_manifest, r"(?i)proof (?:complete|finalised|finalized)")
        self.assertIn("executable authentication proof is incomplete", _read(ROADMAP).casefold())
        self.assertIn("OQ-034", open_work)
        self.assertIn(
            "OQ-034 resolves architecture selection only. Its executable proof remains a Phase 8 obligation",
            open_work,
        )
        self.assertIn("PHASE 8", open_work)
        skeleton_entry_stop = _section(
            _read(SKELETON),
            "### 10.7 Entry STOP condition",
            "## 11. Preliminary performance and scaling review",
        )
        phase7c_contract = skeleton_entry_stop.index("approved Phase 7C contract")
        development_hard_stop = skeleton_entry_stop.index("Development Entry Hard Stop")
        proof_classification = skeleton_entry_stop.index("the proof vehicle must be classified")
        phase8_proof = skeleton_entry_stop.index("Phase 8 proof boundary")
        self.assertEqual(
            sorted((phase7c_contract, development_hard_stop, proof_classification, phase8_proof)),
            [phase7c_contract, development_hard_stop, proof_classification, phase8_proof],
        )

    def test_i04_roadmap_phase7_task_contract_fails_closed_on_mutations(self):
        roadmap = _read(ROADMAP)

        def bullet_containing(text: str, phrase: str) -> str:
            matches = [
                line
                for line in text.splitlines(keepends=True)
                if line.startswith("- ") and phrase.casefold() in line.casefold()
            ]
            if len(matches) != 1:
                raise ValueError(f"expected one Roadmap bullet containing {phrase!r}")
            return matches[0]

        def remove_bullet(text: str, phrase: str) -> str:
            line = bullet_containing(text, phrase)
            return text.replace(line, "", 1)

        def append_to_bullet(text: str, phrase: str, addition: str) -> str:
            line = bullet_containing(text, phrase)
            newline = "\n" if line.endswith("\n") else ""
            content = line.rstrip("\r\n")
            return text.replace(line, f"{content}{addition}{newline}", 1)

        required_jit = "create only the JIT Domain Dossiers required by the selected pack"
        oq034 = "use the resolved `OQ-034` architecture selection"
        oq039 = "perform implementation-grade `OQ-039` mapping only for affected domains/actions"
        proof_choice = "make the final proof choice `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`"
        stop_condition = "stop if a task would need to invent product policy"

        fenced_nonsemantic_duplicate = (
            "```text\n"
            "- create only the JIT Domain Dossiers required by the selected pack;\n"
            "```\n\n"
            + roadmap
        )
        self.assertEqual(
            len(_roadmap_phase7_handoff_requirements(fenced_nonsemantic_duplicate)),
            7,
        )

        weakened_oq034 = roadmap.replace(
            bullet_containing(roadmap, oq034),
            "- resolve OQ-034 and OQ-035/OQ-036.\n",
            1,
        )
        duplicate_jit = roadmap.replace(
            bullet_containing(roadmap, required_jit),
            bullet_containing(roadmap, required_jit) * 2,
            1,
        )
        proof_line = bullet_containing(roadmap, proof_choice)
        jit_line = bullet_containing(roadmap, required_jit)
        lines = roadmap.splitlines(keepends=True)
        proof_index = lines.index(proof_line)
        lines.pop(proof_index)
        jit_index = lines.index(jit_line)
        lines.insert(jit_index, proof_line)
        reordered_proof_before_jit = "".join(lines)
        oq039_line = bullet_containing(roadmap, oq039)
        relocated_oq039 = roadmap.replace(oq039_line, "", 1).replace(
            "# 21. Phase 7 handoff\n",
            oq039_line + "\n# 21. Phase 7 handoff\n",
            1,
        )
        relocated_oq039_with_appended_clause = roadmap.replace(
            "# 21. Phase 7 handoff\n",
            oq039_line.rstrip("\r\n")
            + "; implementation may begin immediately\n# 21. Phase 7 handoff\n",
            1,
        )
        invalid_backtick_info_cannot_hide_relocated_requirement = roadmap.replace(
            "# 21. Phase 7 handoff\n",
            "```invalid`info\n" + oq039_line + "```\n\n# 21. Phase 7 handoff\n",
            1,
        )
        four_space_pseudo_fence_cannot_hide_relocated_requirement = roadmap.replace(
            "# 21. Phase 7 handoff\n",
            "    ```text\n" + oq039_line + "```\n\n# 21. Phase 7 handoff\n",
            1,
        )
        extra_task_bullet = roadmap.replace(
            jit_line,
            jit_line + "- implementation may begin once these planning tasks are complete.\n",
            1,
        )
        extra_star_task_bullet = roadmap.replace(
            jit_line,
            jit_line + "* implementation may begin once these planning tasks are complete.\n",
            1,
        )
        extra_plus_task_bullet = roadmap.replace(
            jit_line,
            jit_line + "+ implementation may begin once these planning tasks are complete.\n",
            1,
        )

        task_anchor = "When current Open Work authorises a Phase 7 task, that task must:"
        task_region = roadmap.split(task_anchor, 1)[1].split("```text", 1)[0]
        task_lines = [
            line
            for line in task_region.splitlines(keepends=True)
            if line.startswith("- ")
        ]
        if len(task_lines) != 7:
            raise ValueError(f"expected seven canonical Roadmap task lines, found {len(task_lines)}")
        canonical_task_block = "".join(task_lines)
        fenced_remaining_tasks = roadmap.replace(
            canonical_task_block,
            task_lines[0] + "```markdown\n" + "".join(task_lines[1:]) + "```\n",
            1,
        )
        stop_line = bullet_containing(roadmap, stop_condition)
        ordered_eighth_task = roadmap.replace(
            stop_line,
            stop_line + "8. implementation may begin once these planning tasks are complete.\n",
            1,
        )
        contradictory_prose_after_list = roadmap.replace(
            stop_line,
            stop_line + "Implementation may begin immediately after these planning tasks.\n",
            1,
        )
        contradictory_prose_after_diagram = roadmap.replace(
            "Do not advance the current stage from this Roadmap patch.",
            "Do not advance the current stage from this Roadmap patch.\n\n"
            "Implementation may begin immediately after these planning tasks.",
            1,
        )
        prose_between_first_and_late_closing_fence = roadmap.replace(
            "```\n\nDo not advance the current stage from this Roadmap patch.",
            "```\nImplementation may begin immediately after these planning tasks.\n"
            "```\n\nDo not advance the current stage from this Roadmap patch.",
            1,
        )

        mutants = {
            "required JIT dossier bullet removed": remove_bullet(roadmap, required_jit),
            "OQ-034/OQ-035/OQ-036 requirement weakened": weakened_oq034,
            "OQ-039 mapping bullet removed": remove_bullet(roadmap, oq039),
            "final proof choice removed": remove_bullet(roadmap, proof_choice),
            "STOP condition removed": remove_bullet(roadmap, stop_condition),
            "final proof choice moved before JIT dossiers": reordered_proof_before_jit,
            "required JIT bullet duplicated": duplicate_jit,
            "OQ-039 bullet relocated outside section 21": relocated_oq039,
            "OQ-039 outside §21 has an appended clause": relocated_oq039_with_appended_clause,
            "invalid backtick-info pseudo-fence cannot hide relocated OQ-039": invalid_backtick_info_cannot_hide_relocated_requirement,
            "four-space pseudo-fence cannot hide relocated OQ-039": four_space_pseudo_fence_cannot_hide_relocated_requirement,
            "unrecognised eighth task bullet": extra_task_bullet,
            "eighth star task bullet": extra_star_task_bullet,
            "eighth plus task bullet": extra_plus_task_bullet,
            "remaining task requirements moved into fenced code": fenced_remaining_tasks,
            "ordered eighth task item": ordered_eighth_task,
            "contradictory prose after task list": contradictory_prose_after_list,
            "contradictory prose after phase diagram": contradictory_prose_after_diagram,
            "prose cannot hide behind a later closing fence": prose_between_first_and_late_closing_fence,
            "JIT requirement repeated inside one bullet": append_to_bullet(
                roadmap,
                required_jit,
                "; create only the JIT Domain Dossiers required by the selected pack",
            ),
            "OQ-039 requirement repeated inside one bullet": append_to_bullet(
                roadmap,
                oq039,
                "; perform implementation-grade OQ-039 mapping only for affected domains/actions",
            ),
            "JIT bullet permits required dossiers to be skipped": append_to_bullet(
                roadmap,
                required_jit,
                "; however those dossiers may be skipped",
            ),
            "OQ-034 bullet claims executable proof is complete": append_to_bullet(
                roadmap,
                oq034,
                "; executable proof is already complete",
            ),
            "STOP bullet permits invention of provider semantics": append_to_bullet(
                roadmap,
                stop_condition,
                "; a task may invent provider semantics",
            ),
            "valid bullet has an unrelated appended clause": append_to_bullet(
                roadmap,
                "preserve upstream product, architecture and domain authority",
                "; implementation may begin immediately",
            ),
        }
        for label, mutant in mutants.items():
            with self.subTest(mutation=label):
                with self.assertRaises(ValueError):
                    _roadmap_phase7_handoff_requirements(mutant)

    def test_i04_roadmap_parser_rejects_malformed_section_and_summary_state(self):
        roadmap = _read(ROADMAP)
        heading = "# 21. Phase 7 handoff"
        anchor = "When current Open Work authorises a Phase 7 task, that task must:"
        malformed = {
            "missing section heading": roadmap.replace(heading, "", 1),
            "duplicated section heading": roadmap + f"\n{heading}\n",
            "duplicated task-contract anchor": roadmap.replace(anchor, f"{anchor}\n{anchor}", 1),
            "contradictory Phase 7C summary": roadmap.replace(
                anchor,
                f"Phase 7C is READY.\n{anchor}",
                1,
            ),
            "summary permits implementation while Phase 8 proof remains incomplete": roadmap.replace(
                "executable authentication proof is incomplete.",
                "executable authentication proof is incomplete. "
                "Implementation may begin immediately while the Phase 8 proof remains incomplete.",
                1,
            ),
            "summary says not to wait for Phase 8 proof": roadmap.replace(
                "executable authentication proof is incomplete.",
                "executable authentication proof is incomplete. "
                "Do not wait for the Phase 8 proof before implementation.",
                1,
            ),
            "unreviewed summary prose added before task anchor": roadmap.replace(
                anchor,
                f"Additional unreviewed Phase 7 boundary prose.\n\n{anchor}",
                1,
            ),
        }
        summary_facts = (
            "FP-001 has existing Phase 7A work and an Identity & Access dossier.",
            "The narrow PMR artifact reconciliation remains required after certified Engineering Standards Authority Promotion and has not been performed.",
            "Phase 7C remains gated",
            "proof classification is not finalised",
            "executable authentication proof is incomplete",
        )
        for fact in summary_facts:
            malformed[f"summary fact removed: {fact}"] = roadmap.replace(fact, "", 1)

        for label, mutant in malformed.items():
            with self.subTest(mutation=label):
                with self.assertRaises(ValueError):
                    _roadmap_phase7_handoff_requirements(mutant)

    def test_i05_required_dossiers_cannot_be_skipped(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual("REQUIRED / NOT_STARTED", state.get("communications"))
        self.assertIn("COMMUNICATIONS: REQUIRED / NOT_STARTED", _active_window(text))
        self.assertIn("Communications", _read(SKELETON))
        self.assertIn("Required dossiers", _read(SKELETON))
        self.assertNotRegex(_active_window(text), r"(?i)communications.*(?:COMPLETE|MERGED|OPTIONAL)")
        skipped = text.replace(
            '"communications": "REQUIRED / NOT_STARTED"',
            '"communications": "OPTIONAL / COMPLETE"',
            1,
        )
        self.assertFalse(_execution_state_is_valid(skipped, _lifecycle_json(skipped)))

    def test_i06_conditional_dossiers_need_explicit_disposition(self):
        text, state, _ = self._state_and_matrix()
        conditional = state["conditional_dossiers"]
        self.assertEqual(
            {
                "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
                "analytics": "NOT REQUIRED",
            },
            conditional,
        )
        active = _active_window(text)
        self.assertIn("CONDITIONAL DOSSIERS:", active)
        self.assertIn("PENDING EXPLICIT ADJUDICATION", active)
        self.assertNotRegex(active, r"(?i)CONDITIONAL DOSSIERS:.*\b(?:COMPLETE|APPROVED)\b")
        adjudicated = text.replace(
            '"privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION"',
            '"privacy_consent": "COMPLETE / APPROVED"',
            1,
        )
        self.assertFalse(_execution_state_is_valid(adjudicated, _lifecycle_json(adjudicated)))

    def test_i07_phase7c_remains_blocked_until_required_work_is_done(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual("BLOCKED / NOT_STARTED", state.get("phase_7c"))
        self.assertRegex(_active_window(text), r"(?m)^PHASE 7C:\s*BLOCKED / NOT_STARTED\b")
        self.assertNotRegex(_active_window(text), r"(?m)^PHASE 7C:\s*(?:READY|COMPLETE|APPROVED)")
        advanced = text.replace(
            '"phase_7c": "BLOCKED / NOT_STARTED"',
            '"phase_7c": "READY / COMPLETE"',
            1,
        )
        self.assertFalse(_execution_state_is_valid(advanced, _lifecycle_json(advanced)))

    def test_i08_proof_classification_is_not_final_before_final_contract(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual("BLOCKED / NOT_STARTED", state.get("phase_7c"))
        self.assertEqual("NOT FINALISED", state.get("proof_classification"))
        self.assertRegex(_active_window(text), r"(?m)^PROOF CLASSIFICATION:\s*NOT FINALISED\s*$")
        skeleton = _read(SKELETON)
        self.assertIn(
            "Only the approved Phase 7C Final Feature Pack Contract may become development-entry authority",
            skeleton,
        )
        self.assertIn("OQ-034", _read(ROADMAP))
        self.assertRegex(_read(ROADMAP), r"(?i)executable authentication proof (?:is incomplete|remains (?:incomplete|a phase 8 obligation))")
        self.assertNotRegex(_active_window(text), r"(?i)PROOF CLASSIFICATION:\s*(?:REUSE_EXISTING_PROOF|NEW_TRACER_BULLET|COMPLETE)")
        finalised = text.replace(
            '"proof_classification": "NOT FINALISED"',
            '"proof_classification": "REUSE_EXISTING_PROOF"',
            1,
        )
        self.assertFalse(_execution_state_is_valid(finalised, _lifecycle_json(finalised)))

    def test_i09_harden02_authority_and_scope_remain_separate(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual("PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY", state.get("harden_02_scope"))
        self.assertEqual([], _affirmative_prohibited_scope(_active_window(text)))
        contract = self._required(CONTRACT)
        self.assertIn("HARDEN-02 is not authority for Product, Architecture, Domain or Roadmap law", contract)
        self.assertIn("Engineering Standards Authority Promotion: **NOT EXECUTED by HARDEN-02**", contract)
        self.assertIn("FP-001 reconciliation: **NOT PERFORMED by HARDEN-02**", contract)
        expanded = text.replace(
            '"harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY"',
            '"harden_02_scope": "PRODUCT LAW / IMPLEMENTATION"',
            1,
        )
        self.assertFalse(_execution_state_is_valid(expanded, _lifecycle_json(expanded)))
        prohibited_classifications = (
            "HARDEN-02 is a Product requirement",
            "HARDEN-02 is a Roadmap gate",
            "HARDEN-02 is a blocking OQ",
            "HARDEN-02 is a Feature Pack",
            "HARDEN-02 is Horizontal Hardening",
            "HARDEN-02 is Store hardening",
            "HARDEN-02 is Commerce/Entitlements hardening",
        )
        for statement in prohibited_classifications:
            with self.subTest(statement=statement):
                contaminated = _inject_active_statement(text, statement)
                self.assertTrue(_affirmative_prohibited_scope(_active_window(contaminated)))
                self.assertFalse(_execution_state_is_valid(contaminated, _lifecycle_json(contaminated)))

    def test_i10_fp001_reconciliation_is_recognised_without_false_completion(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual("REQUIRED / DOWNSTREAM / NOT PERFORMED", state.get("fp001_reconciliation"))
        self.assertIn("FP001_RECONCILIATION_REQUIRED", text)
        self.assertRegex(
            _active_window(text),
            r"(?m)^FP001_RECONCILIATION_REQUIRED:\s*REQUIRED / DOWNSTREAM.*NOT PERFORMED\s*$",
        )
        self.assertNotRegex(_active_window(text), r"(?i)FP001_RECONCILIATION_REQUIRED:\s*(?:COMPLETE|DONE|PASSED)")
        false_complete = re.sub(
            r'("fp001_reconciliation"\s*:\s*)"[^"]+"',
            r'\1"COMPLETE"',
            text,
            count=1,
        )
        self.assertNotEqual(text, false_complete)
        self.assertEqual("COMPLETE", _lifecycle_json(false_complete).get("fp001_reconciliation"))
        self.assertFalse(_execution_state_is_valid(false_complete, _lifecycle_json(false_complete)))

    def test_i11_implementation_remains_blocked(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual("BLOCKED", state.get("application_implementation"))
        active = _active_window(text)
        self.assertRegex(active, r"(?m)^EXECUTABLE DEVELOPMENT:\s*BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS\s*$")
        self.assertNotRegex(active, r"(?i)(?:TB|VS|HH|application implementation).*\b(?:AUTHORISED|AUTHORIZED|STARTED|COMPLETE)\b")
        self.assertNotIn("APPLICATION IMPLEMENTATION: AUTHORISED", text)
        implementation = text.replace(
            '"application_implementation": "BLOCKED"',
            '"application_implementation": "AUTHORISED"',
            1,
        )
        self.assertFalse(_execution_state_is_valid(implementation, _lifecycle_json(implementation)))
        prohibited_authorities = (
            "APPLICATION IMPLEMENTATION: AUTHORISED",
            "TB: AUTHORISED",
            "VS: AUTHORISED",
            "HH: AUTHORISED",
            "PACKAGE INSTALLS: AUTHORISED",
            "MIGRATIONS: AUTHORISED",
            "PROVIDER CHANGES: AUTHORISED",
        )
        for statement in prohibited_authorities:
            with self.subTest(statement=statement):
                contaminated = _inject_active_statement(text, statement)
                self.assertTrue(_affirmative_prohibited_scope(_active_window(contaminated)))
                self.assertFalse(_execution_state_is_valid(contaminated, _lifecycle_json(contaminated)))

    def test_i12_post_execution_resume_order_has_no_skipped_predecessor(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual(NEXT_STAGE, state.get("next_stage"))
        self.assertEqual(EXPECTED_DOWNSTREAM_ROUTE, state.get("downstream_route"))
        route_text = _active_window(text)
        route_lines = [line.strip("→ ") for line in route_text.splitlines() if line.lstrip().startswith("→")]
        for required in EXPECTED_DOWNSTREAM_ROUTE[1:]:
            self.assertIn(required, route_lines)
        positions = [route_lines.index(required) for required in EXPECTED_DOWNSTREAM_ROUTE[1:]]
        self.assertEqual(sorted(positions), positions)
        self.assertEqual(1, len(_route_declarations(text, "NEXT STAGE")))
        self.assertNotRegex(route_text, r"(?m)^NEXT STAGE:\s*(?:FP001_RECONCILIATION_REQUIRED|COMMUNICATIONS)")
        json_region = _marked_region(text, JSON_START, JSON_END)
        for index, predecessor in enumerate(EXPECTED_DOWNSTREAM_ROUTE[1:], start=1):
            ending = ",\n" if index < len(EXPECTED_DOWNSTREAM_ROUTE) - 1 else "\n"
            route_entry = f'    "{predecessor}"{ending}'
            skipped = json_region.replace(route_entry, "", 1)
            self.assertNotEqual(json_region, skipped, predecessor)
            mutant = text.replace(json_region, skipped, 1)
            with self.subTest(skipped=predecessor):
                try:
                    mutant_state = _lifecycle_json(mutant)
                except ValueError:
                    continue
                self.assertFalse(_execution_state_is_valid(mutant, mutant_state))

    def test_i13_store_and_cer_are_excluded(self):
        text, state, _ = self._state_and_matrix()
        self.assertEqual("EXCLUDED", state.get("store_cer"))
        self.assertRegex(_active_window(text), r"(?m)^STORE / CER:\s*EXCLUDED(?: FROM HARDEN-02)?\s*$")
        contract = self._required(CONTRACT)
        self.assertRegex(contract, r"(?i)Store Blueprint / CER:\s*\*\*EXCLUDED\*\*")
        self.assertEqual([], _affirmative_prohibited_scope(_active_window(text)))
        included = text.replace('"store_cer": "EXCLUDED"', '"store_cer": "IN SCOPE"', 1)
        self.assertFalse(_execution_state_is_valid(included, _lifecycle_json(included)))
        forbidden_evidence = (
            "Store repository SHA: deadbeef",
            "CER proof obligation: required",
            "CER exit condition: passed",
            "Store/CER implementation path: docs/store/implementation",
        )
        current_evidence = EXECUTION_MATRIX_EVIDENCE.strip("`")
        for forbidden in forbidden_evidence:
            with self.subTest(forbidden=forbidden):
                contaminated = text.replace(
                    current_evidence,
                    f"{current_evidence}; {forbidden}",
                    1,
                )
                self.assertNotEqual(text, contaminated)
                self.assertFalse(
                    _execution_state_is_valid(contaminated, _lifecycle_json(contaminated))
                )
                in_active_state = _inject_active_statement(text, forbidden)
                self.assertTrue(_affirmative_prohibited_scope(_active_window(in_active_state)))
                self.assertFalse(
                    _execution_state_is_valid(in_active_state, _lifecycle_json(in_active_state))
                )

    def test_current_authority_and_derived_source_tables_match_live_routing(self):
        contract = self._required(CONTRACT)
        _validate_contract_source_routing(contract)
        current = _manifest_authority_filenames()
        rows = _table_rows_in_section(
            contract,
            "### CURRENT AUTHORITY",
            "### CURRENT DERIVED EVIDENCE",
        )
        self.assertEqual(
            [current[document_id] for document_id in CURRENT_AUTHORITY_DOCUMENT_IDS],
            [row[0].strip("`") for row in rows],
        )
        stale_mutants = (
            contract.replace("00_PLATFORM_v1.5.2.md", "00_PLATFORM_v1.4.1.md", 1),
            contract.replace("02_OPEN_WORK_v1.2.51.md", "02_OPEN_WORK_v1.2.45.md", 1),
            contract.replace(
                "working/DELIVERY_ATLAS_WORKING_v0.3.3.md",
                "working/DELIVERY_ATLAS_WORKING_v0.2.1.md",
                1,
            ),
        )
        for mutant in stale_mutants:
            with self.subTest(mutant=mutant[:100]):
                with self.assertRaises(ValueError):
                    _validate_contract_source_routing(mutant)

    def test_lifecycle_markers_json_and_matrix_fail_closed(self):
        text = self._open_work()
        malformed_json = (
            text.replace(JSON_START, "", 1),
            text.replace(JSON_START, JSON_START + "\n" + JSON_START, 1),
            text.replace(JSON_END, "", 1),
            re.sub(
                r'("harden_02_execution"\s*:\s*)"[^"]+"',
                r"\1BROKEN",
                text,
                count=1,
            ),
            text.replace(
                f'"harden_02_execution": "{EXECUTION_STATUS}"',
                f'"harden_02_execution": "{EXECUTION_STATUS}", "harden_02_execution": "BROKEN"',
                1,
            ),
        )
        for sample in malformed_json:
            with self.subTest(sample=sample[:120]):
                with self.assertRaises(ValueError):
                    _lifecycle_json(sample)

        malformed_matrix = (
            text.replace(MATRIX_START, "", 1),
            text.replace(MATRIX_START, MATRIX_START + "\n" + MATRIX_START, 1),
            text.replace(MATRIX_END, "", 1),
            text.replace(
                f"| `EXECUTION` | `{EXECUTION_MATRIX_STATUS}` |",
                f"| `EXECUTION` | |",
                1,
            ),
            text.replace(MATRIX_END, "<!-- UNEXPECTED HARDEN_02 MATRIX -->" + MATRIX_END, 1),
        )
        for sample in malformed_matrix:
            with self.subTest(sample=sample[:120]):
                with self.assertRaises(ValueError):
                    _lifecycle_matrix(sample)

        relocated = text.replace(MATRIX_START, "", 1).replace(
            "# 10. Minimal Tools",
            "# 10. Minimal Tools\n" + MATRIX_START,
            1,
        )
        with self.assertRaises(ValueError):
            _lifecycle_json(relocated)

    def test_successor_predecessor_archives_are_exact_and_open_work_normalizer_is_fail_closed(self):
        successor = self._open_work()
        predecessor = self._required(OPEN_WORK_PREDECESSOR)
        self.assertEqual(EXPECTED_ARCHIVE_SHA256[OPEN_WORK_PREDECESSOR], _sha256(OPEN_WORK_PREDECESSOR))
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.48.md").exists())
        self.assertEqual(predecessor, _normalise_open_work_successor(successor, predecessor))
        missing = successor.replace(MATRIX_START, "", 1)
        duplicate = successor + "\n" + MATRIX_START
        relocated = successor.replace(
            MATRIX_START,
            "",
            1,
        ).replace("# 10. Minimal Tools", MATRIX_START + "\n# 10. Minimal Tools", 1)
        unexpected = successor + "\n## 99. Unexpected lifecycle section\n"
        downstream_mutation = successor.replace(
            '"phase_7c": "BLOCKED / NOT_STARTED"',
            '"phase_7c": "COMPLETE / CERTIFIED"',
            1,
        )
        for sample in (missing, duplicate, relocated, unexpected, downstream_mutation):
            with self.subTest(sample=sample[:100]):
                with self.assertRaises(ValueError):
                    _normalise_open_work_successor(sample, predecessor)

    def test_contract_successor_normalizes_only_declared_status_and_source_routing_provenance(self):
        successor = self._required(CONTRACT)
        predecessor = self._required(CONTRACT_PREDECESSOR)
        self.assertEqual(EXPECTED_ARCHIVE_SHA256[CONTRACT_PREDECESSOR], _sha256(CONTRACT_PREDECESSOR))
        self.assertFalse((DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.4.md").exists())
        self.assertEqual(predecessor, _normalise_contract_successor(successor, predecessor))
        self.assertRegex(
            successor[:2000],
            r"(?is)status:.*HARDEN-02 execution.*COMPLETE / CERTIFIED.*Engineering Standards Authority Promotion.*NEXT / AUTHORISED / NOT STARTED",
        )
        unexpected = successor.replace(
            "## 1. Objective",
            "## 1. Objective\n\nUnexpected execution-law mutation.",
            1,
        )
        product_row = next(
            line
            for line in successor.splitlines(keepends=True)
            if "| `00_PLATFORM_v1.5.2.md` |" in line
        )
        missing_row = successor.replace(product_row, "", 1)
        duplicated_row = successor.replace(product_row, product_row + product_row, 1)
        relocated_row = successor.replace(product_row, "", 1).replace(
            "### CURRENT DERIVED EVIDENCE\n",
            "### CURRENT DERIVED EVIDENCE\n" + product_row,
            1,
        )
        stale_route = successor.replace("00_PLATFORM_v1.5.2.md", "00_PLATFORM_v1.4.1.md", 1)
        for sample in (unexpected, missing_row, duplicated_row, relocated_row, stale_route):
            with self.subTest(sample=sample[:120]):
                with self.assertRaises(ValueError):
                    _normalise_contract_successor(sample, predecessor)

    def test_atlas_successor_normalizes_only_declared_routing_substitutions(self):
        successor = self._required(ATLAS)
        predecessor = self._required(ATLAS_PREDECESSOR)
        self.assertEqual(EXPECTED_ARCHIVE_SHA256[ATLAS_PREDECESSOR], _sha256(ATLAS_PREDECESSOR))
        self.assertFalse((DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.3.2.md").exists())
        self.assertEqual(predecessor, _normalise_atlas_successor(successor, predecessor))
        unexpected = successor.replace(
            "# 1. Authority, purpose and boundaries",
            "# 1. Authority, purpose and boundaries\n\nUnexpected Atlas gate.",
            1,
        )
        with self.assertRaises(ValueError):
            _normalise_atlas_successor(unexpected, predecessor)

if __name__ == "__main__":
    unittest.main()
