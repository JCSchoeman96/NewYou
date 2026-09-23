from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
ROADMAP = DOCS / "05_ROADMAP_v1.1.0.md"
ROADMAP_PREDECESSOR = DOCS / "archive" / "05_ROADMAP_v1.0.0.md"
EVIDENCE = DOCS / "working" / "TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md"
OPEN_WORK = DOCS / "archive" / "02_OPEN_WORK_v1.2.38.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.37.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
DOMAIN_MAP = DOCS / "04_DOMAIN_MAP_v1.1.0.md"

PROTECTED_HASHES = {
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/03_ARCHITECTURE_v1.1.0.md": "d44615f0db3f5f0b38bb68a2904db6066d23e1f82c55da134745c4f6d70b6852",
    "docs/00_platform/04_DOMAIN_MAP_v1.1.0.md": "2c66142e624ccd626727ae36511121fcb64333ca774986ab97ce31eebe5c5ef2",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.37.md": "09d59d615a9aab0d85b590747c932098a1b1164a45ece3a69659d5d49d49ee42",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": "caadd2dfc3c7ed872fda5806efdba467d753b9662e1ff47af16b6303d90b9fa3",
    "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md": "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
    "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md": "26ff1e7a7e40945e501793c2bfb2ede9c01ae03f7949383ae724e3b031fa4faa",
    "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md": "0d8e25170ae692df39f7f771189f95ab76ab64f2701823fb2cde214946650d3f",
    "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md": "8cb7769018c21b09c91208c5991b1b9bca09141c5fa0ef74cd577946d76377f1",
    "docs/00_platform/working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md": "6a4efe4ad4625e2278321d4ae6a4c9147ec3d35d8d80a41e2638a4bee02bb582",
    ".github/workflows/foundation-integrity.yml": "2c718457456c71ad8d7fc416a6e0a646792271b9341e4a14fedda6ddb02bcdb8",
}

REQUIRED_SUCCESSOR_PATHS = (
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.38.md",
    "docs/00_platform/05_ROADMAP_v1.1.0.md",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.37.md",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md",
    "docs/00_platform/working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md",
)

PROHIBITED_PRESENT_PATHS = (
    "docs/00_platform/05_ROADMAP_v1.0.0.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.37.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.38.md",
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


class RoadmapAmendmentIntegrityTests(unittest.TestCase):
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
        self.assertEqual(
            "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
            _sha256(ROADMAP_PREDECESSOR),
        )
        self.assertEqual(
            "09d59d615a9aab0d85b590747c932098a1b1164a45ece3a69659d5d49d49ee42",
            _sha256(OPEN_WORK_PREDECESSOR),
        )
        self.assertIn("v1.0.0 → v1.1.0", self.roadmap)
        self.assertIn("v1.2.37 → v1.2.38", self.open_work)
        self.assertIn("archive/05_ROADMAP_v1.0.0.md", self.roadmap)
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
        self.assertIn("00_PLATFORM_v1.3.0.md", header)
        self.assertIn("01_DECISIONS_v1.3.0.md", header)
        self.assertIn("03_ARCHITECTURE_v1.1.0.md", header)
        self.assertIn("04_DOMAIN_MAP_v1.1.0.md", header)
        self.assertIn("02_OPEN_WORK_v1.2.38.md", header)
        self.assertNotIn("00_PLATFORM_v1.2.1.md", header)
        self.assertNotIn("03_ARCHITECTURE_v1.0.0.md", header)
        self.assertNotIn("04_DOMAIN_MAP_v1.0.0.md", header)
        self.assertIn("`00_PLATFORM_v1.3.0.md", self.fp_sections["FP-001"])
        self.assertIn("`03_ARCHITECTURE_v1.1.0.md", self.fp_sections["FP-001"])

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
        self.assertIn("05_ROADMAP_v1.1.0.md", self.readme)
        self.assertIn("archive/02_OPEN_WORK_v1.2.38.md", self.readme)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE", self.readme)
        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertEqual("1.2.41", current["OPEN_WORK"]["semver"])
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.41.md", current["OPEN_WORK"]["repository_path"])
        self.assertEqual(_sha256(ROOT / current["OPEN_WORK"]["repository_path"]), current["OPEN_WORK"]["sha256"])
        self.assertEqual("historical", {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}["OPEN_WORK_V1_2_38"]["lifecycle"])
        self.assertEqual(_sha256(OPEN_WORK), {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}["OPEN_WORK_V1_2_38"]["sha256"])
        self.assertEqual("1.1.0", current["ROADMAP"]["semver"])
        self.assertEqual("docs/00_platform/05_ROADMAP_v1.1.0.md", current["ROADMAP"]["repository_path"])
        self.assertEqual(_sha256(ROADMAP), current["ROADMAP"]["sha256"])
        self.assertEqual(17, self.manifest["integrity_rules"]["expected_counts"]["feature_packs"])
        self.assertEqual(20, self.manifest["integrity_rules"]["expected_counts"]["domains"])
        self.assertEqual(61, self.manifest["integrity_rules"]["expected_counts"]["ownership_rows"])
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_37"]["lifecycle"])
        self.assertEqual("historical", historical["ROADMAP_V1_0_0"]["lifecycle"])
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
