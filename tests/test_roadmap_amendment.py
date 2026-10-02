from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
ROADMAP = DOCS / "archive" / "05_ROADMAP_v1.1.3.md"
ROADMAP_CURRENT = DOCS / "05_ROADMAP_v1.2.0.md"
ROADMAP_PREDECESSOR = DOCS / "archive" / "05_ROADMAP_v1.1.2.md"
ROADMAP_V1_0_0_PREDECESSOR = DOCS / "archive" / "05_ROADMAP_v1.0.0.md"
ROADMAP_V1_1_0_PREDECESSOR = DOCS / "archive" / "05_ROADMAP_v1.1.0.md"
ROADMAP_V1_1_1_PREDECESSOR = DOCS / "archive" / "05_ROADMAP_v1.1.1.md"
EVIDENCE = DOCS / "working" / "TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md"
OPEN_WORK = DOCS / "archive" / "02_OPEN_WORK_v1.2.38.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.37.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
DOMAIN_MAP = DOCS / "archive" / "04_DOMAIN_MAP_v1.1.0.md"

ROADMAP_V1_1_2_SHA256 = "e22b76eb27a3d0c6c9d8e3af9486b34c0187dd3426a12de42895743a2efb4ab2"
ROADMAP_V1_1_3_SHA256 = "9cba581592ebc43ec3e39debce82a8e86ac0b3132962d7be12d377706e5e0126"
FP006_OLD_TRACKER_CITATION = "current tracker `02_OPEN_WORK_v1.2.45.md §§8, 11`"
FP006_SOURCE_AT_FREEZE_CITATION = "source-at-freeze tracker `archive/02_OPEN_WORK_v1.2.45.md §§8, 11`"

PROTECTED_HASHES = {
    "docs/00_platform/archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/archive/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/archive/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.1.0.md": "d44615f0db3f5f0b38bb68a2904db6066d23e1f82c55da134745c4f6d70b6852",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.1.0.md": "2c66142e624ccd626727ae36511121fcb64333ca774986ab97ce31eebe5c5ef2",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/archive/05_ROADMAP_v1.1.0.md": "eaeaf6031e47653777caf5885ad9eb0ceba58783c99d7d6d255acfbca53fa613",
    "docs/00_platform/archive/05_ROADMAP_v1.1.1.md": "db2f17ba41d1a5aea63f46c94e8c0f5950030872a5ef6b07d53c5e1ea3ca3e4c",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.37.md": "09d59d615a9aab0d85b590747c932098a1b1164a45ece3a69659d5d49d49ee42",
    "docs/00_platform/archive/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/archive/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": "caadd2dfc3c7ed872fda5806efdba467d753b9662e1ff47af16b6303d90b9fa3",
    "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md": "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
    "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md": "26ff1e7a7e40945e501793c2bfb2ede9c01ae03f7949383ae724e3b031fa4faa",
    "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md": "0d8e25170ae692df39f7f771189f95ab76ab64f2701823fb2cde214946650d3f",
    "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be",
    "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md": "8cb7769018c21b09c91208c5991b1b9bca09141c5fa0ef74cd577946d76377f1",
    "docs/00_platform/working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md": "af35b9cd6159f8f1b5154bc5df8baa2c0547e7f0f94b8b8b37dbc182846a18cb",
    ".github/workflows/foundation-integrity.yml": "1e9161e066465d93ba9b2a74ae103accfd0d732393aff2e797f16fb1d27c6091",
}

REQUIRED_SUCCESSOR_PATHS = (
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.38.md",
    "docs/00_platform/archive/05_ROADMAP_v1.1.0.md",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.37.md",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md",
    "docs/00_platform/archive/05_ROADMAP_v1.1.2.md",
    "docs/00_platform/archive/05_ROADMAP_v1.1.3.md",
    "docs/00_platform/working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md",
)

PROHIBITED_PRESENT_PATHS = (
    "docs/00_platform/05_ROADMAP_v1.0.0.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.37.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.38.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.46.md",
    "docs/00_platform/05_ROADMAP_v1.1.2.md",
    "mix.exs",
    "docs/00_platform/ENGINEERING_STANDARDS_v1.0.0.md",
    "docs/00_platform/reference/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    "docs/00_platform/working/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
)

FORBIDDEN_NEW_FP_MARKERS = (
    "**ID:** `FP-018`",
    "## FP-018",
    "**Name:** Research",
    "**Name:** Voting",
    "**Name:** Interactive Tools",
    "**Name:** Platform Member Reference",
    "**Name:** Competitions",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _fp_sections(text: str) -> dict[str, str]:
    pattern = re.compile(r"^## (FP-\d{3}) — .+$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else text.find("\n# 7. MVP", match.end())
        if end < 0:
            end = len(text)
        sections[match.group(1)] = text[match.start() : end]
    return sections


def _normalise_roadmap_routing_successor(current: str, predecessor: str) -> str:
    replacements = (
        ("# 05_ROADMAP_v1.1.3.md", "# 05_ROADMAP_v1.1.2.md"),
        ("**Document version:** v1.1.3", "**Document version:** v1.1.2"),
        ("`archive/05_ROADMAP_v1.1.2.md`", "`archive/05_ROADMAP_v1.1.1.md`"),
        ("`v1.1.2 → v1.1.3`", "`v1.1.1 → v1.1.2`"),
        (
            "- **Current Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`, `00_PLATFORM_v1.5.0.md`, `01_DECISIONS_v1.5.0.md`",
            "- **Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`, `00_PLATFORM_v1.4.1.md`, `01_DECISIONS_v1.4.1.md`",
        ),
        (
            "- **Current Architecture authority:** `03_ARCHITECTURE_v1.1.1.md` and accepted Architecture Law (`reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` where exact legislative evidence is required)",
            "- **Architecture authority:** `03_ARCHITECTURE_v1.1.1.md` and accepted Architecture Law (`reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` where exact legislative evidence is required)",
        ),
        (
            "- **Current Domain authority:** `04_DOMAIN_MAP_v1.2.0.md`",
            "- **Domain authority:** `04_DOMAIN_MAP_v1.1.1.md`",
        ),
        (
            "- **Current programme routing:** `README.md` and the current Open Work path it identifies (`02_OPEN_WORK_v1.2.47.md`)",
            "- **Planning tracker:** `02_OPEN_WORK_v1.2.45.md`",
        ),
        (
            "source-at-freeze tracker `archive/02_OPEN_WORK_v1.2.45.md §§8, 11`",
            "current tracker `02_OPEN_WORK_v1.2.45.md §§8, 11`",
        ),
    )
    normalised = current
    for successor, prior in replacements:
        if normalised.count(successor) != 1:
            raise AssertionError(f"expected one Roadmap routing replacement target: {successor}")
        normalised = normalised.replace(successor, prior)

    for inserted in (
        "- **Roadmap-freeze provenance (v1.1.2 source-at-freeze):** `archive/00_PLATFORM_v1.4.1.md`, `archive/01_DECISIONS_v1.4.1.md`, `archive/04_DOMAIN_MAP_v1.1.1.md`, `archive/02_OPEN_WORK_v1.2.45.md`\n",
        "## v1.1.3 Patch Scope\n\nThis routing/provenance-only successor separates current authority from Roadmap-freeze provenance, corrects the FP-006 source-at-freeze tracker label and defers current task/stage selection to README and current Open Work. It preserves Roadmap semantics, all 17 Feature Pack definitions, sequence, affected Domains, gates, dependencies, proof directions, critical path, future-gated Research/Voting treatment and Interactive Tools doctrine. It does not advance any task or stage.\n\n",
        "Current Product, Decision, Architecture and Domain authority is identified in the versioned authority fields above and routed by README. The Roadmap-freeze provenance field records the sources used when v1.1.2 was frozen. Older version citations retained in Feature Pack sections, including Product `v1.4.1`, are source-at-freeze evidence for those frozen definitions; they do not claim current authority and are not replaced merely because newer authority exists. This v1.1.3 clarification does not re-derive any Feature Pack.\n\n",
    ):
        if normalised.count(inserted) != 1:
            raise AssertionError("expected exactly one inserted routing/provenance block")
        normalised = normalised.replace(inserted, "")

    marker = "# 21. Phase 7 handoff\n\n"
    current_section = normalised.split(marker, 1)[1]
    prior_section = predecessor.split(marker, 1)[1]
    current_opening = current_section.split("\n\n", 1)[0]
    prior_opening = prior_section.split("\n\n", 1)[0]
    if current_opening.count("This Roadmap defines the approved outcome sequence") != 1:
        raise AssertionError("unexpected current §21 opening")
    normalised = normalised.replace(current_opening, prior_opening, 1)
    return normalised


class RoadmapAmendmentIntegrityTests(unittest.TestCase):
    maxDiff = 0

    @classmethod
    def setUpClass(cls) -> None:
        cls.roadmap = ROADMAP.read_text(encoding="utf-8")
        cls.predecessor = ROADMAP_PREDECESSOR.read_text(encoding="utf-8")
        cls.evidence = EVIDENCE.read_text(encoding="utf-8")
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.domain_map = DOMAIN_MAP.read_text(encoding="utf-8")
        cls.fp_sections = _fp_sections(cls.roadmap)

    def test_predecessor_is_byte_identical_and_successor_uses_explicit_semver(self):
        self.assertTrue(ROADMAP.is_file(), ROADMAP)
        self.assertTrue(ROADMAP_PREDECESSOR.is_file(), ROADMAP_PREDECESSOR)
        self.assertEqual(ROADMAP_V1_1_2_SHA256, _sha256(ROADMAP_PREDECESSOR))
        self.assertEqual(
            "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
            _sha256(ROADMAP_V1_0_0_PREDECESSOR),
        )
        self.assertEqual(
            "eaeaf6031e47653777caf5885ad9eb0ceba58783c99d7d6d255acfbca53fa613",
            _sha256(ROADMAP_V1_1_0_PREDECESSOR),
        )
        self.assertEqual(
            "db2f17ba41d1a5aea63f46c94e8c0f5950030872a5ef6b07d53c5e1ea3ca3e4c",
            _sha256(ROADMAP_V1_1_1_PREDECESSOR),
        )
        self.assertEqual(
            "09d59d615a9aab0d85b590747c932098a1b1164a45ece3a69659d5d49d49ee42",
            _sha256(OPEN_WORK_PREDECESSOR),
        )
        self.assertIn("v1.0.0 → v1.1.0", ROADMAP_V1_1_0_PREDECESSOR.read_text(encoding="utf-8"))
        self.assertIn("v1.1.2 → v1.1.3", self.roadmap)
        self.assertIn(
            "**Predecessor frozen version:** `archive/05_ROADMAP_v1.1.2.md`",
            self.roadmap,
        )
        self.assertIn("v1.2.37 → v1.2.38", self.open_work)
        self.assertIn("archive/05_ROADMAP_v1.0.0.md", self.roadmap)
        roadmap_grill = (DOCS / "working" / "TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md").read_text(encoding="utf-8")
        self.assertIn("`docs/00_platform/archive/05_ROADMAP_v1.1.0.md`", roadmap_grill)
        self.assertNotIn("`05_ROADMAP_v1.1.0.md`", roadmap_grill)
        self.assertFalse((DOCS / "05_ROADMAP_v1.0.0.md").exists())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.37.md").exists())

    def test_feature_pack_set_remains_exactly_seventeen(self):
        ids = re.findall(r"\*\*ID:\*\* `(FP-\d{3})`", self.roadmap)
        self.assertEqual(17, len(ids))
        self.assertEqual([f"FP-{number:03d}" for number in range(1, 18)], ids)
        self.assertEqual(17, len(self.fp_sections))
        for marker in FORBIDDEN_NEW_FP_MARKERS:
            self.assertNotIn(marker, self.roadmap)
        self.assertIn("no Research Feature Pack", self.roadmap)
        self.assertIn("no Voting or Competitions Feature Pack", self.roadmap)
        self.assertIn("No Tools Feature Pack", self.roadmap)
        self.assertIn("Feature Pack count remains **17**", self.roadmap)

    def test_only_routing_and_provenance_regions_differ_from_archived_roadmap(self):
        self.assertEqual(self.predecessor, _normalise_roadmap_routing_successor(self.roadmap, self.predecessor))

    def test_feature_pack_sections_match_archived_roadmap_except_fp006_tracker_provenance(self):
        expected_ids = [f"FP-{number:03d}" for number in range(1, 18)]
        predecessor_sections = _fp_sections(self.predecessor)
        self.assertEqual(expected_ids, list(predecessor_sections))
        self.assertEqual(expected_ids, list(self.fp_sections))

        for feature_pack_id in expected_ids:
            expected = predecessor_sections[feature_pack_id]
            if feature_pack_id == "FP-006":
                self.assertIn(FP006_OLD_TRACKER_CITATION, expected)
                expected = expected.replace(FP006_OLD_TRACKER_CITATION, FP006_SOURCE_AT_FREEZE_CITATION)
            self.assertEqual(expected, self.fp_sections[feature_pack_id], feature_pack_id)

    def test_fp001_requires_pmr_without_freezing_representation(self):
        fp001 = self.fp_sections["FP-001"]
        self.assertIn("required human-facing Platform Member Reference", fp001)
        self.assertIn("DEC-297", fp001)
        self.assertIn("ARC-330", fp001)
        self.assertIn("Identity & Access", fp001)
        self.assertIn("non-secret but private-by-default", fp001)
        self.assertIn("ARQ-IAM-013", fp001)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", fp001)
        for frozen in ("prefix", "alphabet", "grouping", "checksum", "generator"):
            self.assertIn(frozen, fp001)
        self.assertNotIn("VG", fp001)

    def test_research_is_future_gated_and_not_fp005(self):
        self.assertIn("FUTURE-GATED / FEATURE-PACK-UNASSIGNED", self.roadmap)
        self.assertIn("Domain 19 — Research & Feedback", self.roadmap)
        self.assertIn("Not MVP", self.roadmap)
        self.assertIn("not FP-005", self.roadmap)
        self.assertIn("not automatically FP-006, FP-008 or FP-009", self.roadmap)
        fp005 = self.fp_sections["FP-005"]
        self.assertIn("do **not** activate Domain 19 Research & Feedback", fp005)
        self.assertIn("Habits, Journals & Progress", fp005)
        self.assertNotIn("Domain 19", fp005.split("**Feedback classification guardrail:**")[0])

    def test_voting_is_future_gated_and_not_required_by_fp008_or_fp013(self):
        self.assertIn("Domain 20 — Voting & Balloting", self.roadmap)
        fp008 = self.fp_sections["FP-008"]
        fp013 = self.fp_sections["FP-013"]
        self.assertIn("does **not** require Voting & Balloting", fp008)
        self.assertIn("does **not** require Voting & Balloting", fp013)
        self.assertIn("FUTURE-GATED / FEATURE-PACK-UNASSIGNED", fp008)
        self.assertIn("FUTURE-GATED / FEATURE-PACK-UNASSIGNED", fp013)
        self.assertNotIn("OPTIONAL Voting", fp008)
        self.assertNotIn("OPTIONAL Voting", fp013)

    def test_interactive_tools_are_purpose_distributed_without_feature_pack(self):
        self.assertIn("purpose-distributed delivery mechanisms, not an independent Feature Pack family", self.roadmap)
        self.assertIn("No Tools Feature Pack", self.roadmap)
        self.assertIn("calculation != authority", self.roadmap)
        fp005 = self.fp_sections["FP-005"]
        fp010 = self.fp_sections["FP-010"]
        self.assertIn("Plans & Nutrition", fp005)
        self.assertIn("Plans & Nutrition authority", fp010)
        self.assertNotIn("## FP-018", self.roadmap)

    def test_dependency_graph_has_no_research_or_voting_nodes(self):
        graph = self.roadmap[self.roadmap.index("## 3.2 Dependency graph") : self.roadmap.index("## 3.3")]
        self.assertNotIn("Research", graph)
        self.assertNotIn("Voting", graph)
        self.assertNotIn("Interactive Tools", graph)
        self.assertIn("FP-001 Trusted bilingual entry and verified identity", graph)
        self.assertIn("FP-017", graph)
        critical = self.roadmap[self.roadmap.index("# 7. MVP / FIRST-PAID CRITICAL PATH") : self.roadmap.index("# 8. Pilot progression")]
        self.assertIn("required Platform Member Reference", critical)
        self.assertNotIn("Research", critical)
        self.assertNotIn("Voting", critical)

    def test_authority_references_use_current_successors(self):
        header = "\n".join(self.roadmap.splitlines()[:35])
        self.assertTrue("PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md" in header, "current North Star")
        self.assertTrue("00_PLATFORM_v1.5.0.md" in header, "current Product")
        self.assertTrue("01_DECISIONS_v1.5.0.md" in header, "current Decisions")
        self.assertTrue("03_ARCHITECTURE_v1.1.1.md" in header, "current Architecture")
        self.assertTrue("04_DOMAIN_MAP_v1.2.0.md" in header, "current Domain Map")
        self.assertNotIn("00_PLATFORM_v1.3.0.md", header)
        self.assertNotIn("03_ARCHITECTURE_v1.0.0.md", header)
        self.assertNotIn("04_DOMAIN_MAP_v1.0.0.md", header)
        for archived_path in (
            "archive/00_PLATFORM_v1.4.1.md",
            "archive/01_DECISIONS_v1.4.1.md",
            "archive/04_DOMAIN_MAP_v1.1.1.md",
            "archive/02_OPEN_WORK_v1.2.45.md",
        ):
            self.assertTrue(
                any(
                    archived_path in line and re.search(r"source[- ]at[- ]freeze", line, re.IGNORECASE)
                    for line in self.roadmap.splitlines()
                ),
                archived_path,
            )
        self.assertIn("`00_PLATFORM_v1.4.1.md", self.fp_sections["FP-001"])
        self.assertIn("`03_ARCHITECTURE_v1.1.1.md", self.fp_sections["FP-001"])

    def test_fp006_uses_archived_source_at_freeze_tracker(self):
        fp006 = self.fp_sections["FP-006"]
        self.assertTrue(FP006_SOURCE_AT_FREEZE_CITATION in fp006, "FP-006 source-at-freeze citation")
        self.assertFalse(FP006_OLD_TRACKER_CITATION in fp006, "FP-006 current-tracker citation")

    def test_historical_handoff_and_freeze_stop_are_absent(self):
        self.assertFalse("NEXT: FOUNDATION READINESS AUDIT" in self.roadmap)
        self.assertFalse(
            "The next allowed action after this Roadmap is frozen is the **Foundation Readiness Audit**"
            in self.roadmap,
        )
        self.assertFalse("STOP. Do not begin Phase 7 in this task." in self.roadmap)

    def test_section_21_defers_current_routing_without_snapshotting_active_task(self):
        section_21 = self.roadmap[self.roadmap.index("# 21. Phase 7 handoff") :]
        self.assertIn("README and current Open Work own programme routing", section_21)
        self.assertRegex(section_21.lower(), r"current (?:task|stage)")
        self.assertFalse("HARDEN-02" in section_21, "Section 21 active-task snapshot")
        self.assertFalse("NEXT / AUTHORISED / NOT STARTED" in section_21, "Section 21 active-task status")
        self.assertFalse("Current Open Work v1.2.45 records" in section_21, "Section 21 versioned tracker snapshot")

    def test_grill_evidence_records_locked_human_decisions(self):
        self.assertIn("NON-AUTHORITATIVE / ROADMAP SEQUENCING GRILL EVIDENCE", self.evidence)
        self.assertIn("522eab3d5efd367044f2bb0459730b200523071f", self.evidence)
        self.assertIn("Contradiction count:", self.evidence)
        self.assertIn("`0`", self.evidence)
        self.assertIn("Decision 1 — Platform Member Reference", self.evidence)
        self.assertIn("REQUIRED within FP-001", self.evidence)
        self.assertIn("Decision 2 — Research & Feedback", self.evidence)
        self.assertIn("FUTURE-GATED / FEATURE-PACK-UNASSIGNED", self.evidence)
        self.assertIn("Decision 3 — Voting & Balloting", self.evidence)
        self.assertIn("Decision 4 — Interactive Tools", self.evidence)
        self.assertIn("purpose-distributed", self.evidence.lower())

    def test_open_work_readme_and_manifest_route_the_successor(self):
        self.assertIn("ROADMAP SEQUENCING GRILL: COMPLETE", self.open_work)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE", self.open_work)
        self.assertIn("ATLAS_RECONCILIATION_REQUIRED", self.open_work)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.open_work)
        self.assertIn("ENGINEERING STANDARDS: DOWNSTREAM", self.open_work)
        self.assertIn("## 12.4 ", self.open_work)
        self.assertIn("## 12.5 ", self.open_work)
        self.assertIn("## 12.6 ", self.open_work)
        self.assertLess(self.open_work.index("## 12.4 "), self.open_work.index("## 12.5 "))
        self.assertLess(self.open_work.index("## 12.5 "), self.open_work.index("## 12.6 "))
        self.assertTrue("05_ROADMAP_v1.2.0.md" in self.readme, "README current Roadmap")
        self.assertIn("archive/02_OPEN_WORK_v1.2.38.md", self.readme)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE", self.readme)
        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertEqual(_sha256(ROOT / current["OPEN_WORK"]["repository_path"]), current["OPEN_WORK"]["sha256"])
        self.assertEqual("historical", {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}["OPEN_WORK_V1_2_38"]["lifecycle"])
        self.assertEqual(_sha256(OPEN_WORK), {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}["OPEN_WORK_V1_2_38"]["sha256"])
        self.assertEqual("1.2.0", current["ROADMAP"]["semver"])
        self.assertEqual("docs/00_platform/05_ROADMAP_v1.2.0.md", current["ROADMAP"]["repository_path"])
        self.assertEqual(_sha256(ROADMAP_CURRENT), current["ROADMAP"]["sha256"])
        self.assertEqual(17, self.manifest["integrity_rules"]["expected_counts"]["feature_packs"])
        self.assertEqual(20, self.manifest["integrity_rules"]["expected_counts"]["domains"])
        self.assertEqual(61, self.manifest["integrity_rules"]["expected_counts"]["ownership_rows"])
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_37"]["lifecycle"])
        self.assertEqual("historical", historical["ROADMAP_V1_0_0"]["lifecycle"])
        self.assertEqual("historical", historical["ROADMAP_V1_1_1"]["lifecycle"])
        self.assertEqual("1.1.2", historical["ROADMAP_V1_1_1"]["superseded_version"])
        self.assertEqual(_sha256(ROADMAP_V1_1_1_PREDECESSOR), historical["ROADMAP_V1_1_1"]["sha256"])
        self.assertIn("ROADMAP_V1_1_2", historical)
        self.assertEqual("historical", historical["ROADMAP_V1_1_2"]["lifecycle"])
        self.assertEqual("1.1.3", historical["ROADMAP_V1_1_2"]["superseded_version"])
        self.assertEqual(_sha256(ROADMAP_PREDECESSOR), historical["ROADMAP_V1_1_2"]["sha256"])
        self.assertEqual("historical", historical["ROADMAP_V1_1_3"]["lifecycle"])
        self.assertEqual("1.1.4", historical["ROADMAP_V1_1_3"]["superseded_version"])
        self.assertEqual(ROADMAP_V1_1_3_SHA256, historical["ROADMAP_V1_1_3"]["sha256"])
        self.assertEqual(
            "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
            historical["ROADMAP_V1_0_0"]["sha256"],
        )

    def test_domain_and_upstream_law_unchanged(self):
        self.assertEqual(
            "2c66142e624ccd626727ae36511121fcb64333ca774986ab97ce31eebe5c5ef2",
            _sha256(DOMAIN_MAP),
        )
        self.assertIn("20 approved ownership domains", self.domain_map)
        for relative_path, expected_hash in PROTECTED_HASHES.items():
            if expected_hash is None:
                continue
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)

    def test_scope_has_no_implementation_or_prohibited_artifact_changes(self):
        for relative_path in REQUIRED_SUCCESSOR_PATHS:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)
        for relative_path in PROHIBITED_PRESENT_PATHS:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)
        self.assertFalse((ROOT / ".formatter.exs").exists())
        self.assertFalse((ROOT / ".credo.exs").exists())
        atlas = (DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.1.0.md").read_bytes()
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md"],
            hashlib.sha256(atlas).hexdigest(),
        )
        workflow_dir = ROOT / ".github" / "workflows"
        self.assertEqual(
            ["foundation-integrity.yml"],
            sorted(path.name for path in workflow_dir.glob("*")),
        )
        for forbidden in ("LOW/STANDARD/HIGH", "typespec", "Dialyzer", "Credo", "Splode"):
            self.assertNotIn(forbidden, self.roadmap)
            self.assertNotIn(forbidden, self.open_work)


if __name__ == "__main__":
    unittest.main()
