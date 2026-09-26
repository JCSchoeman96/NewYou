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
        "00_PLATFORM_v1.4.0.md",
        "1.4.0",
        "1.4.1",
        "34d1fa2dc3c12248b9fc0f850e25a0964083dc6d4ebe7b9f6f30dc4347cc0b29",
    ),
    "DECISION_REGISTER": (
        "01_DECISIONS_v1.4.0.md",
        "1.4.0",
        "1.4.1",
        "6058a81e5c3f7864c4587d5fb2e714efc1067abc694d9a0279ebccdd2b28ed14",
    ),
    "ROADMAP": (
        "05_ROADMAP_v1.1.1.md",
        "1.1.1",
        "1.1.2",
        "db2f17ba41d1a5aea63f46c94e8c0f5950030872a5ef6b07d53c5e1ea3ca3e4c",
    ),
}

CURRENT_AUTHORITY = {
    "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md",
    "PLATFORM_BASELINE": "00_PLATFORM_v1.4.1.md",
    "DECISION_REGISTER": "01_DECISIONS_v1.4.1.md",
    "OPEN_WORK": "02_OPEN_WORK_v1.2.45.md",
    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",
    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.1.1.md",
    "ROADMAP": "05_ROADMAP_v1.1.2.md",
    "PLATFORM_OPERATING_MODEL": "PLATFORM_OPERATING_MODEL_v1.0.1.md",
    "FRONTEND_EXPERIENCE_SYSTEM": "FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def _feature_pack_sections(text: str) -> dict[str, str]:
    starts = list(re.finditer(r"^## (FP-\d{3}) — .+$", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else text.index("# 7. MVP", match.end())
        sections[match.group(1)] = text[match.start() : end]
    return sections


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

    def test_four_predecessors_are_archived_byte_identically_and_manifested(self):
        historical_ids = {
            "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_V1_2_2",
            "PLATFORM_BASELINE": "PLATFORM_BASELINE_V1_4_0",
            "DECISION_REGISTER": "DECISION_REGISTER_V1_4_0",
            "ROADMAP": "ROADMAP_V1_1_1",
        }
        for document_id, (filename, old_version, new_version, expected_hash) in PREDECESSORS.items():
            with self.subTest(document_id=document_id):
                path = DOCS / "archive" / filename
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
        self.assertEqual(
            _section(old_product, "# 1. Platform Purpose", "# 24. Current Planning Stop Condition"),
            _section(new_product, "# 1. Platform Purpose", "# 24. Current Planning Stop Condition"),
        )

        old_decisions = _read(DOCS / "archive" / PREDECESSORS["DECISION_REGISTER"][0])
        new_decisions = _read(DOCS / CURRENT_AUTHORITY["DECISION_REGISTER"])
        self.assertEqual(old_decisions[old_decisions.index("# GQ-001"):], new_decisions[new_decisions.index("# GQ-001"):])
        self.assertEqual(
            re.findall(r"^## (?:DEC|OQ)-\d{3}", old_decisions, re.MULTILINE),
            re.findall(r"^## (?:DEC|OQ)-\d{3}", new_decisions, re.MULTILINE),
        )

        old_roadmap = _read(DOCS / "archive" / PREDECESSORS["ROADMAP"][0])
        new_roadmap = _read(DOCS / CURRENT_AUTHORITY["ROADMAP"])
        old_packs = _feature_pack_sections(old_roadmap)
        new_packs = _feature_pack_sections(new_roadmap)
        self.assertEqual([f"FP-{number:03d}" for number in range(1, 18)], list(old_packs))
        self.assertEqual(list(old_packs), list(new_packs))
        for pack_id in old_packs:
            prior, current = old_packs[pack_id], new_packs[pack_id]
            current = current.replace(
                "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", "PROJECT_NORTH_STAR_AND_MVP_v1.2.2.md"
            ).replace("00_PLATFORM_v1.4.1.md", "00_PLATFORM_v1.4.0.md")
            if pack_id == "FP-006":
                current = current.replace(
                    "current tracker `02_OPEN_WORK_v1.2.45.md §§8, 11`",
                    "`02_OPEN_WORK_v1.2.44.md §§8, 11`",
                )
            self.assertEqual(prior, current, pack_id)

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
        self.assertIn("HARDEN-02 execution as NEXT / AUTHORISED / NOT STARTED", product)
        self.assertIn("FP001_RECONCILIATION_REQUIRED` remains downstream and not performed", product)
        self.assertIn("02_OPEN_WORK_v1.2.45.md", decisions)
        self.assertIn("02_OPEN_WORK_v1.2.45.md", roadmap)
        self.assertIn("HARDEN-02 execution as NEXT / AUTHORISED / NOT STARTED", roadmap)
        fp006 = _feature_pack_sections(roadmap)["FP-006"]
        self.assertIn("PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", fp006)
        self.assertIn("00_PLATFORM_v1.4.1.md", fp006)
        self.assertIn("02_OPEN_WORK_v1.2.45.md", fp006)
        self.assertIn("Engineering Standards Authority Promotion", roadmap)
        self.assertIn("FP-001 reconciliation", roadmap)
        self.assertIn("Communications", roadmap)
        self.assertIn("Phase 7C", roadmap)
        self.assertIn("Phase 8 only after the Development Entry Hard Stop passes", roadmap)
        self.assertIn("HARDEN-02 v0.4.0 CONTRACT LIFECYCLE: COMPLETE / CERTIFIED", open_work)
        self.assertIn("HARDEN-02 EXECUTION: NEXT / AUTHORISED / NOT STARTED", open_work)
        self.assertIn("00_PLATFORM_v1.4.1.md", readme)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.1.2`", readme)

        active_paths = [
            self.readme,
            *(_read(ROOT / entry["repository_path"]) for entry in self.governing.values()),
            _read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"),
            _read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.2.md"),
        ]
        stale = re.compile(r"(?<!archive/)02_OPEN_WORK_v1\.2\.44\.md")
        self.assertFalse(any(stale.search(text) for text in active_paths))


if __name__ == "__main__":
    unittest.main()
