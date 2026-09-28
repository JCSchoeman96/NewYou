from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

PREDECESSORS = {
    "PROJECT_NORTH_STAR_AND_MVP": (
        "PROJECT_NORTH_STAR_AND_MVP_v1.2.2.md",
        "1.2.2",
        "1.2.3",
        "296b01a3da81e079bd33aab7a59dd23390946baf0b6daa3deae9d71f3971531d",
    ),
    "PLATFORM_BASELINE": (
        "00_PLATFORM_v1.4.1.md",
        "1.4.1",
        "1.5.0",
        "868b6a6ca81df7d4322dd534cb4387c051748cd49cdc3834e53626b49040c8ec",
    ),
    "DECISION_REGISTER": (
        "01_DECISIONS_v1.4.1.md",
        "1.4.1",
        "1.5.0",
        "e92564c16c9ad15e8b7558ff76a509efad4310aa786c697b09b0ce2723ec4701",
    ),
    "OPEN_WORK": (
        "02_OPEN_WORK_v1.2.48.md",
        "1.2.48",
        "1.2.49",
        "270172784629197f2bb6faa60dbe6d4184bd9d04d878876f6877c98390fd8d17",
    ),
    "ROADMAP": (
        "05_ROADMAP_v1.1.3.md",
        "1.1.3",
        "1.1.4",
        "9cba581592ebc43ec3e39debce82a8e86ac0b3132962d7be12d377706e5e0126",
    ),
}

CURRENT_AUTHORITY = {
    "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md",
    "PLATFORM_BASELINE": "00_PLATFORM_v1.5.0.md",
    "DECISION_REGISTER": "01_DECISIONS_v1.5.0.md",
    "OPEN_WORK": "02_OPEN_WORK_v1.2.49.md",
    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",
    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.2.0.md",
    "ROADMAP": "05_ROADMAP_v1.1.4.md",
    "PLATFORM_OPERATING_MODEL": "PLATFORM_OPERATING_MODEL_v1.0.1.md",
    "FRONTEND_EXPERIENCE_SYSTEM": "FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
}

PRODUCT_BODY_START = "# 1. Platform Purpose"
PRODUCT_BODY_END = "# 24. Current Planning Stop Condition"
PRODUCT_INSERTION_START = "# 21S. Marketing Permission and Communication Preferences"
PRODUCT_INSERTION_END = "# 22. Explicitly Not Yet Decided"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def _line_marker_positions(text: str, marker: str) -> list[int]:
    pattern = rf"(?m)^{re.escape(marker)}\r?$"
    return [match.start() for match in re.finditer(pattern, text)]


def _product_body(text: str) -> str:
    start_positions = _line_marker_positions(text, PRODUCT_BODY_START)
    if len(start_positions) != 1:
        raise ValueError(f"expected exactly one Product body start marker: {PRODUCT_BODY_START}")
    end_positions = _line_marker_positions(text, PRODUCT_BODY_END)
    if len(end_positions) != 1:
        raise ValueError(f"expected exactly one Product body end marker: {PRODUCT_BODY_END}")

    start = start_positions[0]
    end = end_positions[0]
    if start >= end:
        raise ValueError("Product body start marker must precede its end marker")
    return text[start:end]


def _successor_product_body_without_authorized_insertion(text: str) -> str:
    body = _product_body(text)
    insertion_start_positions = _line_marker_positions(text, PRODUCT_INSERTION_START)
    if len(insertion_start_positions) != 1:
        raise ValueError(f"expected exactly one authorized Product insertion start marker: {PRODUCT_INSERTION_START}")
    insertion_end_positions = _line_marker_positions(text, PRODUCT_INSERTION_END)
    if len(insertion_end_positions) != 1:
        raise ValueError(f"expected exactly one authorized Product insertion end marker: {PRODUCT_INSERTION_END}")

    body_start = _line_marker_positions(text, PRODUCT_BODY_START)[0]
    body_end = _line_marker_positions(text, PRODUCT_BODY_END)[0]
    insertion_start = insertion_start_positions[0]
    insertion_end = insertion_end_positions[0]
    if not (body_start < insertion_start < body_end):
        raise ValueError("Product insertion start marker must be inside the Product body")
    if not (body_start < insertion_end < body_end):
        raise ValueError("Product insertion end marker must be inside the Product body")
    if insertion_end <= insertion_start:
        raise ValueError("Product insertion end marker must follow its start marker")
    return body[: insertion_start - body_start] + body[insertion_end - body_start :]


def _feature_pack_sections(text: str) -> dict[str, str]:
    starts = list(re.finditer(r"^## (FP-\d{3}) — .+$", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else text.index("# 7. MVP", match.end())
        sections[match.group(1)] = text[match.start() : end]
    return sections


OPEN_WORK_HISTORICAL_ATLAS_BLOCK = (
    "## 12.7 — Historical Delivery Atlas reconciliation\n\n"
    "**Status:** HISTORICAL COMPLETION RECORD — the then-current derived / non-authoritative navigation successor was "
    "`working/DELIVERY_ATLAS_WORKING_v0.2.1.md` (predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`; "
    "earlier predecessor `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`). This subsection records that historical "
    "reconciliation and is not the current Atlas route.\n\n"
)
OPEN_WORK_HISTORICAL_ATLAS_BLOCK_PREDECESSOR = (
    "## 12.7 — Delivery Atlas reconciliation\n\n"
    "**Status:** COMPLETE as derived / non-authoritative navigation successor `working/DELIVERY_ATLAS_WORKING_v0.2.1.md` "
    "(predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`; earlier predecessor "
    "`archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`).\n\n"
)


OPEN_WORK_ATLAS_CURRENT_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.0.md`; "
    "immediate predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.3.md`; pinned v0.2.1 source-at-freeze artifacts remain preserved; "
    "DERIVED / NON-AUTHORITATIVE; ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)
OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.1.md`; "
    "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.0.md`; pinned v0.2.1 source-at-freeze artifacts remain preserved; "
    "DERIVED / NON-AUTHORITATIVE; ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)
OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE = OPEN_WORK_ATLAS_CURRENT_STATUS_LINE.replace(
    "working/DELIVERY_ATLAS_WORKING_v0.3.0.md",
    "working/DELIVERY_ATLAS_WORKING_v0.2.3.md",
)
OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.2.3.md`; "
    "predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md`; DERIVED / NON-AUTHORITATIVE; "
    "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)


def _validate_open_work_atlas_status_line(text: str, expected: str) -> None:
    matches = list(re.finditer(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", text))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one Open Work Atlas reconciliation status line, found {len(matches)}")
    start_positions = _line_marker_positions(text, "# 9. Immediate Next Action")
    end_positions = _line_marker_positions(text, "# 10. Minimal Tools")
    if (
        len(start_positions) != 1
        or len(end_positions) != 1
        or not start_positions[0] < matches[0].start() < end_positions[0]
    ):
        raise ValueError("Open Work Atlas reconciliation status line is missing from or relocated outside §9")
    if matches[0].group(0) != expected:
        raise ValueError("Open Work §9 Atlas reconciliation status line differs outside declared lineage clarification")


def _normalise_open_work_successor(text: str, canonical_predecessor: str) -> str:
    _validate_open_work_atlas_status_line(text, OPEN_WORK_ATLAS_CURRENT_STATUS_LINE)
    if text.count(OPEN_WORK_HISTORICAL_ATLAS_BLOCK) != 1:
        raise ValueError("expected exactly one historical Atlas clarification block in Open Work successor")
    if text.count("## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt") != 1:
        raise ValueError("expected exactly one historical Atlas clarification end marker")

    replacements = (
        ("# 02_OPEN_WORK_v1.2.48.md", "# 02_OPEN_WORK_v1.2.47.md", 1),
        ("OPEN-WORK SUCCESSOR v1.2.48", "OPEN-WORK SUCCESSOR v1.2.47", 1),
        ("Document version:** v1.2.48", "Document version:** v1.2.47", 1),
        ("archive/02_OPEN_WORK_v1.2.47.md", "archive/02_OPEN_WORK_v1.2.46.md", 1),
        ("v1.2.47 → v1.2.48", "v1.2.46 → v1.2.47", 1),
        ("DELIVERY_ATLAS_WORKING_v0.3.0.md", "DELIVERY_ATLAS_WORKING_v0.2.3.md", 5),
        ("05_ROADMAP_v1.1.4.md", "05_ROADMAP_v1.1.3.md", 6),
    )
    for current, previous, expected_count in replacements:
        actual_count = text.count(current)
        if actual_count != expected_count:
            raise AssertionError(f"expected {expected_count} Open Work routing replacements for {current!r}, found {actual_count}")
        text = text.replace(current, previous)
    _validate_open_work_atlas_status_line(text, OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE)
    text = text.replace(
        OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE,
        OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE,
        1,
    )
    _validate_open_work_atlas_status_line(text, OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE)
    if text.count(OPEN_WORK_HISTORICAL_ATLAS_BLOCK) != 1:
        raise ValueError("historical Atlas clarification block is missing, duplicate, or relocated")
    text = text.replace(
        OPEN_WORK_HISTORICAL_ATLAS_BLOCK,
        OPEN_WORK_HISTORICAL_ATLAS_BLOCK_PREDECESSOR,
        1,
    )
    if text != canonical_predecessor:
        raise ValueError("Open Work successor differs outside declared routing/version, §9 lineage, and historical clarification markers")
    return text


class AuthorityRoutingSuccessorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.governing = {entry["document_id"]: entry for entry in cls.manifest["governing_documents"]}
        cls.historical = {entry["document_id"]: entry for entry in cls.manifest["historical_documents"]}
        cls.readme = _read(DOCS / "README.md")

    def test_readme_and_manifest_resolve_the_expected_current_authority_set(self):
        self.assertEqual(
            CURRENT_AUTHORITY,
            {document_id: self.governing[document_id]["canonical_filename"] for document_id in CURRENT_AUTHORITY},
        )
        context = _section(self.readme, "## Default Agent Context", "## Active Working Artifacts")
        listed = re.findall(r"^\d+\. `([^`]+)`$", context, re.MULTILINE)
        expected = list(CURRENT_AUTHORITY.values())
        self.assertEqual(expected, listed)
        for document_id, filename in CURRENT_AUTHORITY.items():
            entry = self.governing[document_id]
            self.assertEqual(filename, entry["canonical_filename"])
            self.assertEqual(f"docs/00_platform/{filename}", entry["repository_path"])
            self.assertEqual(_sha256(ROOT / entry["repository_path"]), entry["sha256"])
        self.assertEqual(
            _sha256(ROOT / self.governing["OPEN_WORK"]["repository_path"]),
            self.governing["OPEN_WORK"]["provenance_sha256"],
        )

    def test_current_authority_predecessors_are_archived_byte_identically_and_manifested(self):
        historical_ids = {
            "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_V1_2_2",
            "PLATFORM_BASELINE": "PLATFORM_BASELINE_V1_4_1",
            "DECISION_REGISTER": "DECISION_REGISTER_V1_4_1",
            "OPEN_WORK": "OPEN_WORK_V1_2_48",
            "ROADMAP": "ROADMAP_V1_1_3",
        }
        for document_id, (filename, old_version, new_version, expected_hash) in PREDECESSORS.items():
            with self.subTest(document_id=document_id):
                path = DOCS / "archive" / filename
                self.assertTrue(path.is_file(), path)
                if not path.is_file():
                    continue
                self.assertEqual(expected_hash, _sha256(path))
                entry = self.historical[historical_ids[document_id]]
                self.assertEqual("historical", entry["lifecycle"])
                self.assertEqual(filename, entry["canonical_filename"])
                self.assertEqual(f"docs/00_platform/archive/{filename}", entry["repository_path"])
                self.assertEqual(old_version, entry["semver"])
                self.assertEqual(new_version, entry["superseded_version"])
                self.assertEqual(expected_hash, entry["sha256"])
                current = self.governing[document_id]
                self.assertEqual(new_version, current["semver"])
                self.assertEqual(old_version, current["superseded_version"])
                self.assertIn(f"archive/{filename}", self.readme)

    def test_product_north_star_decisions_and_roadmap_meaning_is_preserved(self):
        old_north_star = _read(DOCS / "archive" / PREDECESSORS["PROJECT_NORTH_STAR_AND_MVP"][0])
        new_north_star = _read(DOCS / CURRENT_AUTHORITY["PROJECT_NORTH_STAR_AND_MVP"])
        self.assertEqual(
            _section(old_north_star, "# 1. Read This Document First", "# 23. Current Planning Position"),
            _section(new_north_star, "# 1. Read This Document First", "# 23. Current Planning Position"),
        )

        old_product = _read(DOCS / "archive" / PREDECESSORS["PLATFORM_BASELINE"][0])
        new_product = _read(DOCS / CURRENT_AUTHORITY["PLATFORM_BASELINE"])
        old_product_body = _product_body(old_product)
        new_product_body = _successor_product_body_without_authorized_insertion(new_product)
        self.assertEqual(old_product_body, new_product_body)

        old_decisions = _read(DOCS / "archive" / PREDECESSORS["DECISION_REGISTER"][0])
        new_decisions = _read(DOCS / CURRENT_AUTHORITY["DECISION_REGISTER"])
        old_decision_body = old_decisions[old_decisions.index("# GQ-001"):]
        new_decision_body = new_decisions[new_decisions.index("# GQ-001"):]
        old_before_gates, old_gates = old_decision_body.split("# Open Gates", 1)
        new_before_decision, new_tail = new_decision_body.split("## DEC-304 —", 1)
        new_decision, new_gates = new_tail.split("# Open Gates", 1)
        self.assertEqual(old_before_gates, new_before_decision)
        self.assertEqual(old_gates, new_gates)
        old_identifiers = re.findall(r"^## (?:DEC|OQ)-\d{3}", old_decisions, re.MULTILINE)
        new_identifiers = re.findall(r"^## (?:DEC|OQ)-\d{3}", new_decisions, re.MULTILINE)
        self.assertEqual(old_identifiers, [identifier for identifier in new_identifiers if identifier != "## DEC-304"])

        old_roadmap = _read(DOCS / "archive" / PREDECESSORS["ROADMAP"][0])
        new_roadmap = _read(DOCS / CURRENT_AUTHORITY["ROADMAP"])
        old_packs = _feature_pack_sections(old_roadmap)
        new_packs = _feature_pack_sections(new_roadmap)
        self.assertEqual([f"FP-{number:03d}" for number in range(1, 18)], list(old_packs))
        self.assertEqual(list(old_packs), list(new_packs))
        for pack_id in old_packs:
            prior, current = old_packs[pack_id], new_packs[pack_id]
            self.assertEqual(prior, current, pack_id)

    def test_product_successor_exclusion_is_exact_and_fails_closed(self):
        successor = (
            "# 1. Platform Purpose\n\n"
            "Product purpose text.\n\n"
            "# 21S. Marketing Permission and Communication Preferences\n\n"
            "Authorized insertion text.\n\n"
            "# 22. Explicitly Not Yet Decided\n\n"
            "Section 22 text.\n\n"
            "# 23. Current Constraints\n\n"
            "Section 23 text.\n\n"
            "# 24. Current Planning Stop Condition\n\n"
        )
        expected = (
            "# 1. Platform Purpose\n\n"
            "Product purpose text.\n\n"
            "# 22. Explicitly Not Yet Decided\n\n"
            "Section 22 text.\n\n"
            "# 23. Current Constraints\n\n"
            "Section 23 text.\n\n"
        )
        self.assertEqual(expected, _successor_product_body_without_authorized_insertion(successor))

        changed_section_22 = successor.replace("Section 22 text.", "Changed section 22 text.", 1)
        changed_section_23 = successor.replace("Section 23 text.", "Changed section 23 text.", 1)
        self.assertNotEqual(expected, _successor_product_body_without_authorized_insertion(changed_section_22))
        self.assertNotEqual(expected, _successor_product_body_without_authorized_insertion(changed_section_23))

        out_of_order = successor.replace(
            "# 21S. Marketing Permission and Communication Preferences\n\n"
            "Authorized insertion text.\n\n"
            "# 22. Explicitly Not Yet Decided",
            "# 22. Explicitly Not Yet Decided\n\n"
            "# 21S. Marketing Permission and Communication Preferences\n\n"
            "Authorized insertion text.",
            1,
        )
        invalid_successors = (
            successor.replace("# 21S. Marketing Permission and Communication Preferences\n", "", 1),
            successor.replace(
                "# 21S. Marketing Permission and Communication Preferences",
                "# 21S. Marketing Permission and Communication Preferences\n\n"
                "# 21S. Marketing Permission and Communication Preferences",
                1,
            ),
            successor.replace("# 22. Explicitly Not Yet Decided\n", "", 1),
            out_of_order,
            successor.replace(
                "# 22. Explicitly Not Yet Decided",
                "# 22. Explicitly Not Yet Decided\n\n# 22. Explicitly Not Yet Decided",
                1,
            ),
            successor.replace("# 1. Platform Purpose\n", "", 1),
            successor.replace("# 24. Current Planning Stop Condition\n", "", 1),
            successor.replace(
                "# 21S. Marketing Permission and Communication Preferences\n",
                "Prose mentions # 21S. Marketing Permission and Communication Preferences\n",
                1,
            ),
            successor + "# 21S. Marketing Permission and Communication Preferences\n",
            successor.replace(
                "# 22. Explicitly Not Yet Decided\n",
                "Prose mentions # 22. Explicitly Not Yet Decided\n",
                1,
            ),
            successor + "# 22. Explicitly Not Yet Decided\n",
        )
        for invalid_successor in invalid_successors:
            with self.subTest(invalid_successor=invalid_successor):
                with self.assertRaises(ValueError):
                    _successor_product_body_without_authorized_insertion(invalid_successor)

    def test_current_route_and_lifecycle_are_consistent(self):
        readme = self.readme
        north_star = _read(DOCS / CURRENT_AUTHORITY["PROJECT_NORTH_STAR_AND_MVP"])
        product = _read(DOCS / CURRENT_AUTHORITY["PLATFORM_BASELINE"])
        decisions = _read(DOCS / CURRENT_AUTHORITY["DECISION_REGISTER"])
        roadmap = _read(DOCS / CURRENT_AUTHORITY["ROADMAP"])
        open_work = _read(DOCS / CURRENT_AUTHORITY["OPEN_WORK"])
        for filename in (
            "00_PLATFORM_v1.4.1.md",
            "01_DECISIONS_v1.4.1.md",
            "02_OPEN_WORK_v1.2.45.md",
            "05_ROADMAP_v1.1.2.md",
        ):
            self.assertIn(filename, north_star)
        self.assertIn("02_OPEN_WORK_v1.2.46.md", decisions)
        roadmap_header_marker = "## Amendment summary"
        self.assertEqual(1, roadmap.count(roadmap_header_marker))
        roadmap_header = roadmap.split(roadmap_header_marker, 1)[0]
        for authority_id in (
            "PROJECT_NORTH_STAR_AND_MVP",
            "PLATFORM_BASELINE",
            "DECISION_REGISTER",
            "ARCHITECTURE_SYNTHESIS",
            "DOMAIN_MAP",
        ):
            self.assertIn(self.governing[authority_id]["canonical_filename"], roadmap_header)
        route_match = re.search(r"(?m)^- \*\*Current programme routing:\*\* (.+)$", roadmap_header)
        self.assertIsNotNone(route_match)
        route = route_match.group(1) if route_match else ""
        self.assertIn("README.md", route)
        self.assertIn("current Open Work path it identifies", route)
        self.assertNotRegex(route, r"02_OPEN_WORK_v\d+\.\d+\.\d+\.md")

        self.assertIn("HARDEN-02 execution as NEXT / AUTHORISED / NOT STARTED", product)
        self.assertIn("FP001_RECONCILIATION_REQUIRED` remains downstream and not performed", product)
        self.assertIn("archive/02_OPEN_WORK_v1.2.45.md", roadmap)
        self.assertNotIn("current tracker `02_OPEN_WORK_v1.2.45.md`", roadmap)
        self.assertNotIn("Current Open Work v1.2.45 records", roadmap)
        fp006 = _feature_pack_sections(roadmap)["FP-006"]
        self.assertIn("PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", fp006)
        self.assertIn("00_PLATFORM_v1.4.1.md", fp006)
        self.assertIn("source-at-freeze tracker `archive/02_OPEN_WORK_v1.2.45.md §§8, 11`", fp006)
        section_21 = roadmap.split("# 21. Phase 7 handoff", 1)[1]
        self.assertIn("README and current Open Work own programme routing", section_21)
        self.assertNotIn("HARDEN-02", section_21)
        self.assertNotIn("NEXT / AUTHORISED / NOT STARTED", section_21)
        self.assertIn("HARDEN-02 v0.4.0 CONTRACT LIFECYCLE: COMPLETE / CERTIFIED", open_work)
        self.assertIn("HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING", open_work)
        current_context = _section(readme, "## Default Agent Context", "## Active Working Artifacts")
        for filename in ("00_PLATFORM_v1.5.0.md", "01_DECISIONS_v1.5.0.md", "02_OPEN_WORK_v1.2.49.md", "04_DOMAIN_MAP_v1.2.0.md"):
            self.assertIn(filename, current_context)
        for stale_name in ("00_PLATFORM_v1.4.1.md", "01_DECISIONS_v1.4.1.md", "02_OPEN_WORK_v1.2.45.md", "04_DOMAIN_MAP_v1.1.1.md"):
            self.assertNotIn(stale_name, current_context)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.1.4`", readme)
        self.assertEqual("1.2.49", self.governing["OPEN_WORK"]["semver"])

        active_paths = [
            self.readme,
            *(_read(ROOT / entry["repository_path"]) for entry in self.governing.values()),
            _read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.3.1.md"),
            _read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.3.md"),
        ]
        stale_patterns = (
            re.compile(r"(?<!archive/)02_OPEN_WORK_v1\.2\.44\.md"),
            re.compile(r"(?<!archive/)02_OPEN_WORK_v1\.2\.48\.md"),
            re.compile(r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.0\.md"),
            re.compile(r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.4\.2\.md"),
        )
        for stale in stale_patterns:
            self.assertFalse(any(stale.search(text) for text in active_paths), stale.pattern)
        guards = self.manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"]
        for guard_text, active, archived in (
            (r"(?<!archive/)02_OPEN_WORK_v1\.2\.48\.md", "02_OPEN_WORK_v1.2.48.md", "archive/02_OPEN_WORK_v1.2.48.md"),
            (r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.0\.md", "DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md"),
            (r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.4\.2\.md", "HARDEN-02_CONTRACT_WORKING_v0.4.2.md", "archive/HARDEN-02_CONTRACT_WORKING_v0.4.2.md"),
        ):
            self.assertIn(guard_text, guards)
            guard = re.compile(guard_text)
            self.assertIsNotNone(guard.search(active))
            self.assertIsNone(guard.search(archived))
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.2.1.md", _read(DOCS / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"))

    def test_current_open_work_marks_the_v0_2_1_reconciliation_as_historical(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.49.md")
        historical_heading = "## 12.7 — Historical Delivery Atlas reconciliation"
        self.assertEqual(1, current.count(historical_heading))
        if current.count(historical_heading) != 1:
            return

        history = _section(
            current,
            historical_heading,
            "## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt",
        )
        self.assertIn("HISTORICAL COMPLETION RECORD", history)
        self.assertIn(
            "then-current derived / non-authoritative navigation successor was `working/DELIVERY_ATLAS_WORKING_v0.2.1.md`",
            history,
        )
        self.assertIn("not the current Atlas route", history)
        self.assertIn("current Delivery Atlas remains derived and non-authoritative at `working/DELIVERY_ATLAS_WORKING_v0.3.1.md`", current)

    def test_current_open_work_atlas_lineage_distinguishes_current_predecessor_and_pinned_source(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.49.md")
        _validate_open_work_atlas_status_line(current, OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE)
        self.assertIn("current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.1.md`", OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE)
        self.assertIn("immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.0.md`", OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE)
        self.assertIn("pinned v0.2.1 source-at-freeze artifacts remain preserved", OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE)
        self.assertNotRegex(
            OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE,
            r"current Atlas `working/DELIVERY_ATLAS_WORKING_v0\.3\.1\.md`; predecessor `archive/DELIVERY_ATLAS_WORKING_v0\.2\.1\.md`",
        )
        pinned_working = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        pinned_archive = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        self.assertTrue(pinned_working.is_file())
        self.assertTrue(pinned_archive.is_file())
        self.assertEqual(_sha256(pinned_working), _sha256(pinned_archive))

    def test_open_work_normalizer_rejects_invalid_or_relocated_current_atlas_lineage(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.49.md")
        line = OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE
        malformed = (
            current.replace(line + "\n", "", 1),
            current.replace(line, line + "\n" + line, 1),
            current.replace(line + "\n", "", 1).replace(
                "# 10. Minimal Tools", "# 10. Minimal Tools\n" + line, 1
            ),
            current.replace(
                "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.0.md`",
                "predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md`",
                1,
            ),
        )
        for sample in malformed:
            with self.subTest(sample=sample[:160]):
                with self.assertRaises(ValueError):
                    _validate_open_work_atlas_status_line(sample, line)

    def test_open_work_normalizer_rejects_missing_duplicate_or_relocated_historical_clarification(self):
        current = _read(DOCS / "archive" / "02_OPEN_WORK_v1.2.48.md")
        predecessor = _read(DOCS / "archive" / "02_OPEN_WORK_v1.2.47.md")
        block = OPEN_WORK_HISTORICAL_ATLAS_BLOCK
        missing = current.replace(block, "", 1)
        duplicate = current.replace(block, block + block, 1)
        relocated = current.replace(block, "", 1).replace(
            "## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt",
            block + "## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt",
            1,
        )
        for malformed in (missing, duplicate, relocated):
            with self.subTest(sample=malformed[:160]):
                with self.assertRaises(ValueError):
                    _normalise_open_work_successor(malformed, predecessor)

    def test_open_work_successor_changes_only_routing_metadata_and_preserves_all_gate_state(self):
        predecessor = DOCS / "archive" / "02_OPEN_WORK_v1.2.47.md"
        successor = DOCS / "archive" / "02_OPEN_WORK_v1.2.48.md"
        self.assertTrue(predecessor.is_file(), predecessor)
        self.assertTrue(successor.is_file(), successor)
        if not predecessor.is_file() or not successor.is_file():
            return

        predecessor_text = _read(predecessor)
        successor_text = _read(successor)
        self.assertEqual(
            "71d6f4641cdc70aaa57c8630887d4b24d1a971d34e390c607dda7dbcc8c05118",
            _sha256(predecessor),
        )
        self.assertEqual(predecessor_text, _normalise_open_work_successor(successor_text, predecessor_text))
        for preserved_state in (
            "HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED",
            "Engineering Standards Authority Promotion remains downstream after certified execution",
            "FP-001 reconciliation remains downstream after certified Standards Promotion",
            "Communications follows FP-001 reconciliation",
            "Privacy & Consent, Content & Media, and Audit & Evidence remain conditional / pending explicit adjudication",
            "Analytics remains not required",
            "Phase 7C remains blocked / not started",
            "proof classification remains not finalised",
            "executable development remains blocked until Phase 8 entry conditions pass",
            "Feature Pack count remains **17**",
            "Domain count remains **20**",
        ):
            self.assertIn(preserved_state, successor_text)


if __name__ == "__main__":
    unittest.main()
