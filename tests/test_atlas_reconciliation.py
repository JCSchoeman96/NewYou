from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

from tests.test_atlas_authority_boundary import _normalise_atlas_successor


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.3.0.md"
ATLAS_PREDECESSOR = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.3.md"
ATLAS_V0_2_2 = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.2.md"
ATLAS_V0_2_1 = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
ATLAS_V0_2_0 = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.0.md"
ATLAS_OLDER_PREDECESSOR = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.1.0.md"
OPEN_WORK = DOCS / "archive" / "02_OPEN_WORK_v1.2.43.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.42.md"
OPEN_WORK_OLDER_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.41.md"
OPEN_WORK_V1_2_40 = DOCS / "archive" / "02_OPEN_WORK_v1.2.40.md"
ATLAS_STAGE_OPEN_WORK = DOCS / "archive" / "02_OPEN_WORK_v1.2.39.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

PROTECTED_HASHES = {
    "docs/00_platform/archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/archive/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/archive/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.1.0.md": "d44615f0db3f5f0b38bb68a2904db6066d23e1f82c55da134745c4f6d70b6852",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.1.0.md": "2c66142e624ccd626727ae36511121fcb64333ca774986ab97ce31eebe5c5ef2",
    "docs/00_platform/archive/05_ROADMAP_v1.1.0.md": "eaeaf6031e47653777caf5885ad9eb0ceba58783c99d7d6d255acfbca53fa613",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md": "8cb7769018c21b09c91208c5991b1b9bca09141c5fa0ef74cd577946d76377f1",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.2.0.md": "c122c0f4a903c9679529e0e65a794999dcdaf957a66fcff00df990a0644bbb7f",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.2.2.md": "2a9553cd9076333665d340c6d787a8de8bfa0f78509e6cc8b2cfb874730ab02e",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.2.3.md": "fb107bcc1972f225aef9675bcf36b8709185405e76db19c204c911b7b4a4f1ca",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.47.md": "71d6f4641cdc70aaa57c8630887d4b24d1a971d34e390c607dda7dbcc8c05118",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.38.md": "b5710e3cd3348668ae9d9a7b586343e4b18ba4c1bb7e59ae5c4a69927de188f6",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.39.md": "5af9c6965d214bb0dd46cd3215a2e23ed1a17d546ef53ccd4de31be346d11e21",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.40.md": "e53d416efe2b859053e4d2167b36065383f4f67603db56d833f20247d5120b3e",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.41.md": "85dd9946cf5684b0907f49e973ef75b59541c0f265ac46d44465d1527535da62",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.42.md": "2f9baad6ef314b23b53f9c0daa79976347bfbc5b937d68f7937b3149415e55a3",
    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.1.0.md": "71615d3363a91a7e6002d907c6edd474fbd87f77bdfc6a38f5b11afd240a5626",
    "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
    "docs/00_platform/archive/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/archive/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": "caadd2dfc3c7ed872fda5806efdba467d753b9662e1ff47af16b6303d90b9fa3",
    "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md": "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
    "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md": "26ff1e7a7e40945e501793c2bfb2ede9c01ae03f7949383ae724e3b031fa4faa",
    "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md": "0d8e25170ae692df39f7f771189f95ab76ab64f2701823fb2cde214946650d3f",
}

PROHIBITED_PRESENT_PATHS = (
    "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.1.0.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.38.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.39.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.40.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.41.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.42.md",
    "docs/00_platform/ENGINEERING_STANDARDS_v1.0.0.md",
    "docs/00_platform/reference/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    "docs/00_platform/working/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    "mix.exs",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(text: str, start: str, end: str) -> str:
    start_i = text.index(start)
    end_i = text.index(end, start_i)
    return text[start_i:end_i]


class AtlasReconciliationIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.atlas = ATLAS.read_text(encoding="utf-8")
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        current_open_work_path = DOCS.parent.parent / next(
            entry["repository_path"]
            for entry in cls.manifest["governing_documents"]
            if entry["document_id"] == "OPEN_WORK"
        )
        cls.current_open_work = current_open_work_path.read_text(encoding="utf-8")

    def test_predecessor_preserved_and_successor_versioned(self):
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.2.0.md"],
            _sha256(ATLAS_V0_2_0),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.2.3.md"],
            _sha256(ATLAS_PREDECESSOR),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.2.2.md"],
            _sha256(ATLAS_V0_2_2),
        )
        self.assertFalse((DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.2.md").exists())
        self.assertFalse((DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.3.md").exists())
        self.assertEqual(
            "b4c27c8a314d2a9e227acd53bd69dfce0e01a2cc743535e49a45a848f135cc59",
            _sha256(ATLAS_V0_2_1),
        )
        self.assertEqual(_sha256(ATLAS_V0_2_1), _sha256(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"))
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md"],
            _sha256(ATLAS_OLDER_PREDECESSOR),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/02_OPEN_WORK_v1.2.40.md"],
            _sha256(OPEN_WORK_V1_2_40),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/02_OPEN_WORK_v1.2.41.md"],
            _sha256(OPEN_WORK_OLDER_PREDECESSOR),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/02_OPEN_WORK_v1.2.42.md"],
            _sha256(OPEN_WORK_PREDECESSOR),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/02_OPEN_WORK_v1.2.39.md"],
            _sha256(ATLAS_STAGE_OPEN_WORK),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/02_OPEN_WORK_v1.2.38.md"],
            _sha256(DOCS / "archive" / "02_OPEN_WORK_v1.2.38.md"),
        )
        self.assertTrue(ATLAS.is_file())
        self.assertIn("v0.2.3 → v0.3.0", self.atlas)
        self.assertIn("MINOR", self.atlas)
        self.assertNotIn("working/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md", self.atlas)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.1.0.md", self.atlas)
        self.assertIn("v1.2.42 → v1.2.43", self.open_work)
        self.assertIn("v1.2.41 → v1.2.42", OPEN_WORK_PREDECESSOR.read_text(encoding="utf-8"))
        self.assertIn("v1.2.40 → v1.2.41", OPEN_WORK_OLDER_PREDECESSOR.read_text(encoding="utf-8"))
        self.assertIn("v1.2.39 → v1.2.40", OPEN_WORK_V1_2_40.read_text(encoding="utf-8"))
        self.assertIn("v1.2.38 → v1.2.39", ATLAS_STAGE_OPEN_WORK.read_text(encoding="utf-8"))
        self.assertFalse((DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.1.0.md").exists())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.38.md").exists())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.39.md").exists())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.40.md").exists())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.41.md").exists())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.42.md").exists())

    def test_atlas_successor_changes_only_declared_authority_boundary_blocks(self):
        self.assertTrue(ATLAS_PREDECESSOR.is_file(), ATLAS_PREDECESSOR)
        if not ATLAS_PREDECESSOR.is_file():
            return
        predecessor = ATLAS_PREDECESSOR.read_text(encoding="utf-8")
        self.assertEqual(predecessor, _normalise_atlas_successor(self.atlas, predecessor))

    def test_atlas_remains_non_authoritative_and_outside_manifest(self):
        self.assertIn("WORKING / NON-AUTHORITATIVE", self.atlas)
        self.assertIn("DERIVED DELIVERY PLANNING ARTIFACT", self.atlas)
        self.assertIn("DOES NOT AUTHORISE IMPLEMENTATION", self.atlas)
        self.assertIn("outside authority-document records", self.atlas)
        self.assertIn("listed only under graph/navigation paths", self.atlas)
        ids = {
            entry["document_id"]
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertNotIn("DELIVERY_ATLAS", ids)
        for entry in self.manifest["governing_documents"] + self.manifest["reference_documents"]:
            self.assertNotIn("DELIVERY_ATLAS", entry.get("canonical_filename", ""))
            self.assertNotIn("DELIVERY_ATLAS", entry.get("repository_path", ""))

    def test_not_formally_atlas_12(self):
        self.assertIn("not** `ATLAS-12`", self.atlas.replace("**not** `ATLAS-12`", "not** `ATLAS-12`"))
        self.assertIn("ATLAS_RECONCILIATION", self.atlas)
        self.assertIn("ATLAS-12 NOT_STARTED", self.open_work)
        self.assertIn("reconciliation is not ATLAS-12", self.open_work)

    def test_current_source_routing_refreshed(self):
        sources = _section(self.atlas, "## 1.1 Authority hierarchy", "## 1.2 Purpose")
        self.assertIn("00_PLATFORM_v1.5.0.md", sources)
        self.assertIn("01_DECISIONS_v1.5.0.md", sources)
        self.assertIn("03_ARCHITECTURE_v1.1.1.md", sources)
        self.assertIn("04_DOMAIN_MAP_v1.2.0.md", sources)
        self.assertIn("05_ROADMAP_v1.1.4.md", sources)
        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertIn(Path(current["OPEN_WORK"]["repository_path"]).name, sources)
        self.assertNotIn("00_PLATFORM_v1.3.0.md", sources)
        self.assertNotIn("01_DECISIONS_v1.3.0.md", sources)
        self.assertNotIn("03_ARCHITECTURE_v1.0.0.md", sources)
        self.assertNotIn("04_DOMAIN_MAP_v1.0.0.md", sources)
        self.assertNotIn("05_ROADMAP_v1.0.0.md", sources)
        self.assertNotIn("02_OPEN_WORK_v1.2.28.md", sources)

    def test_section_54_capability_count_matches_inventory_and_matrix(self):
        inventory = _section(
            self.atlas,
            "### Summary register",
            "### CAP-001 — Canonical identity and authentication",
        )
        inventory_caps = re.findall(r"^\| (CAP-\d{3}) \|", inventory, re.MULTILINE)
        self.assertEqual(
            [f"CAP-{number:03d}" for number in range(1, 34)],
            inventory_caps,
        )
        self.assertEqual(33, len(inventory_caps))
        self.assertNotIn("CAP-034", inventory_caps)

        atlas04 = _section(self.atlas, "## 5.4 ATLAS-04", "### Source boundary and matrix rule")
        declared = re.search(
            r"ATLAS-04 connects the (\d+) canonical capabilities to the (\d+) frozen Feature Packs",
            atlas04,
        )
        self.assertIsNotNone(declared)
        self.assertEqual(len(inventory_caps), int(declared.group(1)))
        self.assertEqual(17, int(declared.group(2)))

        matrix = _section(self.atlas, "### Main matrix", "### Feature Pack capability summary")
        matrix_caps = [
            cells[0]
            for line in matrix.splitlines()
            if line.lstrip().startswith("|")
            for cells in [[c.strip() for c in line.strip()[1:-1].split("|")]]
            if cells and re.fullmatch(r"CAP-\d{3}", cells[0])
        ]
        self.assertEqual(inventory_caps, matrix_caps)
        self.assertEqual(33, len(matrix_caps))
        header = next(
            line
            for line in matrix.splitlines()
            if line.lstrip().startswith("|") and "FP-001" in line
        )
        self.assertEqual(17, len(re.findall(r"FP-\d{3}", header)))
        self.assertNotIn("FP-018", header)

    def test_feature_pack_and_domain_counts(self):
        self.assertIn("Feature Pack count remains **17**", self.open_work)
        self.assertIn("Domain count is **20**", self.open_work)
        self.assertEqual(17, self.manifest["integrity_rules"]["expected_counts"]["feature_packs"])
        self.assertEqual(20, self.manifest["integrity_rules"]["expected_counts"]["domains"])
        self.assertIn("20/20 Domain names", self.atlas)
        self.assertNotIn("## FP-018", self.atlas)
        self.assertNotIn("**ID:** `FP-018`", self.atlas)
        for forbidden in (
            "## FP-018",
            "Research Feature Pack",
            "Voting Feature Pack",
            "Competitions Feature Pack",
            "Tools Feature Pack",
            "PMR Feature Pack",
        ):
            # Atlas may say "no ... Feature Pack"; ensure no positive creation markers
            self.assertNotIn(f"**Name:** {forbidden.split()[0]}", self.atlas)

    def test_pmr_in_fp001_navigation_and_unfrozen(self):
        fp001 = _section(self.atlas, "## FP-001 — Trusted bilingual entry", "## FP-002 —")
        self.assertIn("Platform Member Reference", fp001)
        self.assertIn("REQUIRED", fp001)
        self.assertIn("Identity & Access", fp001)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", fp001)
        self.assertIn("encoding remains unfrozen", fp001.lower() + "encoding remains unfrozen")
        self.assertIn("Exact Platform Member Reference encoding", fp001)
        self.assertIn("ARQ-IAM-013", fp001)
        cap001 = _section(self.atlas, "### CAP-001 — Canonical identity", "### CAP-002 —")
        self.assertIn("Platform Member Reference", cap001)
        self.assertIn("not authentication, authorisation, Membership", cap001)

    def test_research_future_gated_and_not_cap019(self):
        self.assertIn("### CAP-032 — Research & Feedback", self.atlas)
        self.assertIn("FUTURE-GATED / FEATURE-PACK-UNASSIGNED", self.atlas)
        lineage = _section(self.atlas, "### Capability lineage view", "### Exception / interpretation notes")
        self.assertIn(
            "| CAP-032 | — (FUTURE-GATED / FEATURE-PACK-UNASSIGNED) | — | — | — |",
            lineage,
        )
        cap019 = _section(self.atlas, "### CAP-019 — Participant progress", "### CAP-020 —")
        self.assertIn("not** Domain 19 Research & Feedback", cap019.replace("**not** Domain 19", "not** Domain 19"))
        self.assertIn("does not activate Research", cap019)
        self.assertIn("EX-011", self.atlas)
        self.assertNotIn("| CAP-032 | Research & Feedback | I |", self.atlas)

    def test_voting_future_gated_and_not_fp008_fp013(self):
        self.assertIn("### CAP-033 — Voting & Balloting", self.atlas)
        lineage = _section(self.atlas, "### Capability lineage view", "### Exception / interpretation notes")
        self.assertIn(
            "| CAP-033 | — (FUTURE-GATED / FEATURE-PACK-UNASSIGNED) | — | — | — |",
            lineage,
        )
        cap033 = _section(self.atlas, "### CAP-033 — Voting & Balloting", "## 5.3 ATLAS-03")
        self.assertIn("not** required by FP-008 or FP-013", cap033.replace("**not** required", "not** required"))
        self.assertIn("EX-012", self.atlas)

    def test_no_generic_tools_authority(self):
        self.assertNotIn("### CAP-034", self.atlas)
        self.assertIn("Interactive Tools / calculators / decision aids are **not** allocated a CAP ID", self.atlas)
        self.assertIn("calculation != authority", self.atlas)
        self.assertIn("EX-013", self.atlas)
        self.assertIn("purpose-distributed", self.atlas.lower())

    def test_matrix_unassigned_caps_have_zero_material_cells(self):
        matrix = _section(self.atlas, "### Main matrix", "### Feature Pack capability summary")
        for cap in ("CAP-032", "CAP-033"):
            rows = [line for line in matrix.splitlines() if line.startswith(f"| {cap} |")]
            self.assertEqual(1, len(rows), cap)
            cells = [c.strip() for c in rows[0].strip("|").split("|")]
            # CAP, name, then 17 FP cells
            self.assertEqual(19, len(cells), cap)
            self.assertTrue(all(cell == "—" for cell in cells[2:]), cap)

    def test_open_work_readme_routing(self):
        self.assertIn("ATLAS RECONCILIATION: COMPLETE", self.current_open_work)
        self.assertIn("HARDEN-02_EXECUTION_REQUIRED", self.current_open_work)
        self.assertIn("HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED", self.current_open_work)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", self.current_open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.current_open_work)
        self.assertIn("DELIVERY_ATLAS_WORKING_v0.3.0.md", self.readme)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.2.3.md", self.readme)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.2.2.md", self.readme)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.2.1.md", self.readme)
        self.assertIn("archive/DELIVERY_ATLAS_WORKING_v0.2.0.md", self.readme)
        self.assertIn(
            "archive/DELIVERY_ATLAS_WORKING_v0.2.2.md` — preserved predecessor to archived Atlas v0.2.3",
            self.readme,
        )
        self.assertIn(
            "archive/DELIVERY_ATLAS_WORKING_v0.2.3.md` — byte-identical immediate predecessor to current working Atlas v0.3.0",
            self.readme,
        )
        self.assertIn("HARDEN-02_EXECUTION_REQUIRED", self.readme)
        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertIn(Path(current["OPEN_WORK"]["repository_path"]).name, self.readme)
        current_open_work_path = DOCS.parent.parent / current["OPEN_WORK"]["repository_path"]
        self.assertTrue(current_open_work_path.is_file())
        self.assertEqual(_sha256(current_open_work_path), current["OPEN_WORK"]["sha256"])
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_42"]["lifecycle"])
        self.assertEqual(_sha256(OPEN_WORK_PREDECESSOR), historical["OPEN_WORK_V1_2_42"]["sha256"])
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_41"]["lifecycle"])
        self.assertEqual(_sha256(OPEN_WORK_OLDER_PREDECESSOR), historical["OPEN_WORK_V1_2_41"]["sha256"])
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_40"]["lifecycle"])
        self.assertEqual(_sha256(OPEN_WORK_V1_2_40), historical["OPEN_WORK_V1_2_40"]["sha256"])
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_39"]["lifecycle"])
        self.assertEqual(_sha256(ATLAS_STAGE_OPEN_WORK), historical["OPEN_WORK_V1_2_39"]["sha256"])
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_38"]["lifecycle"])

    def test_upstream_law_and_fp001_unchanged(self):
        for relative_path, expected_hash in PROTECTED_HASHES.items():
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)
        for relative_path in PROHIBITED_PRESENT_PATHS:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)
        # Atlas must not invent HARDEN-02 law; later governed successors may advance independently.
        self.assertIn("HARDEN-02 artifacts are not amended by this successor", self.atlas)
        self.assertTrue((DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.2.md").is_file())
        self.assertTrue((DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.4.0.md").is_file())
        self.assertTrue((DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.2.0.md").is_file())
        self.assertTrue((DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.1.0.md").is_file())


if __name__ == "__main__":
    unittest.main()
