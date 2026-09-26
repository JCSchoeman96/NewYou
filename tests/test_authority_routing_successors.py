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
        "02_OPEN_WORK_v1.2.46.md",
        "1.2.46",
        "1.2.47",
        "d19ba98b486478ff8fea36b74a72b4102e8fe192a797af919318a1fc31c8c870",
    ),
    "ROADMAP": (
        "05_ROADMAP_v1.1.2.md",
        "1.1.2",
        "1.1.3",
        "e22b76eb27a3d0c6c9d8e3af9486b34c0187dd3426a12de42895743a2efb4ab2",
    ),
}

CURRENT_AUTHORITY = {
    "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md",
    "PLATFORM_BASELINE": "00_PLATFORM_v1.5.0.md",
    "DECISION_REGISTER": "01_DECISIONS_v1.5.0.md",
    "OPEN_WORK": "02_OPEN_WORK_v1.2.47.md",
    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",
    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.2.0.md",
    "ROADMAP": "05_ROADMAP_v1.1.3.md",
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


def _normalise_open_work_successor(text: str) -> str:
    replacements = (
        ("# 02_OPEN_WORK_v1.2.47.md", "# 02_OPEN_WORK_v1.2.46.md"),
        ("OPEN-WORK SUCCESSOR v1.2.47", "OPEN-WORK SUCCESSOR v1.2.46"),
        ("Document version:** v1.2.47", "Document version:** v1.2.46"),
        ("archive/02_OPEN_WORK_v1.2.46.md", "archive/02_OPEN_WORK_v1.2.45.md"),
        ("v1.2.46 → v1.2.47", "v1.2.45 → v1.2.46"),
        ("05_ROADMAP_v1.1.3.md", "05_ROADMAP_v1.1.2.md"),
        ("DELIVERY_ATLAS_WORKING_v0.2.3.md", "DELIVERY_ATLAS_WORKING_v0.2.2.md"),
    )
    for current, predecessor in replacements:
        text = text.replace(current, predecessor)
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

    def test_current_authority_predecessors_are_archived_byte_identically_and_manifested(self):
        historical_ids = {
            "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_V1_2_2",
            "PLATFORM_BASELINE": "PLATFORM_BASELINE_V1_4_1",
            "DECISION_REGISTER": "DECISION_REGISTER_V1_4_1",
            "OPEN_WORK": "OPEN_WORK_V1_2_46",
            "ROADMAP": "ROADMAP_V1_1_2",
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
            if pack_id == "FP-006":
                current = current.replace(
                    "source-at-freeze tracker `archive/02_OPEN_WORK_v1.2.45.md §§8, 11`",
                    "current tracker `02_OPEN_WORK_v1.2.45.md §§8, 11`",
                )
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
        product = _read(DOCS / CURRENT_AUTHORITY["PLATFORM_BASELINE"])
        roadmap = _read(DOCS / CURRENT_AUTHORITY["ROADMAP"])
        open_work = _read(DOCS / CURRENT_AUTHORITY["OPEN_WORK"])
        roadmap_header = roadmap.split("## Amendment summary", 1)[0]
        for authority_id in (
            "PROJECT_NORTH_STAR_AND_MVP",
            "PLATFORM_BASELINE",
            "DECISION_REGISTER",
            "ARCHITECTURE_SYNTHESIS",
            "DOMAIN_MAP",
            "OPEN_WORK",
        ):
            self.assertIn(self.governing[authority_id]["canonical_filename"], roadmap_header)

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
        self.assertIn("HARDEN-02 EXECUTION: NEXT / AUTHORISED / NOT STARTED", open_work)
        current_context = _section(readme, "## Default Agent Context", "## Active Working Artifacts")
        for filename in ("00_PLATFORM_v1.5.0.md", "01_DECISIONS_v1.5.0.md", "02_OPEN_WORK_v1.2.47.md", "04_DOMAIN_MAP_v1.2.0.md"):
            self.assertIn(filename, current_context)
        for stale_name in ("00_PLATFORM_v1.4.1.md", "01_DECISIONS_v1.4.1.md", "02_OPEN_WORK_v1.2.45.md", "04_DOMAIN_MAP_v1.1.1.md"):
            self.assertNotIn(stale_name, current_context)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.1.3`", readme)

        active_paths = [
            self.readme,
            *(_read(ROOT / entry["repository_path"]) for entry in self.governing.values()),
            _read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.3.md"),
            _read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.2.md"),
        ]
        stale = re.compile(r"(?<!archive/)02_OPEN_WORK_v1\.2\.44\.md")
        self.assertFalse(any(stale.search(text) for text in active_paths))

    def test_open_work_successor_changes_only_routing_metadata_and_preserves_all_gate_state(self):
        predecessor = DOCS / "archive" / "02_OPEN_WORK_v1.2.46.md"
        successor = DOCS / "02_OPEN_WORK_v1.2.47.md"
        self.assertTrue(predecessor.is_file(), predecessor)
        self.assertTrue(successor.is_file(), successor)
        if not predecessor.is_file() or not successor.is_file():
            return

        predecessor_text = _read(predecessor)
        successor_text = _read(successor)
        self.assertEqual(
            "d19ba98b486478ff8fea36b74a72b4102e8fe192a797af919318a1fc31c8c870",
            _sha256(predecessor),
        )
        self.assertEqual(predecessor_text, _normalise_open_work_successor(successor_text))
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
