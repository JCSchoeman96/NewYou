import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLATFORM = ROOT / "docs" / "00_platform"
MANIFEST_PATH = PLATFORM / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
README_PATH = PLATFORM / "README.md"


def read_current(document_id):
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    item = next(
        entry
        for entry in manifest["governing_documents"]
        if entry["document_id"] == document_id and entry["lifecycle"] == "current"
    )
    return (ROOT / item["repository_path"]).read_text(encoding="utf-8")


def compact(text):
    return re.sub(r"\s+", " ", text).casefold()


class UnsubscribeIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.current = {
            item["document_id"]: item
            for item in cls.manifest["governing_documents"]
            if item["lifecycle"] == "current"
        }
        cls.historical = {
            item["document_id"]: item for item in cls.manifest["historical_documents"]
        }
        cls.product = compact(read_current("PLATFORM_BASELINE"))
        cls.product_unsubscribe = (
            cls.product.split("# 21s.", 1)[1].split("# 22.", 1)[0]
            if "# 21s." in cls.product and "# 22." in cls.product
            else ""
        )
        cls.decisions = compact(read_current("DECISION_REGISTER"))
        cls.domain_map = compact(read_current("DOMAIN_MAP"))
        cls.open_work = compact(read_current("OPEN_WORK"))
        cls.readme = README_PATH.read_text(encoding="utf-8")
        atlas_path = PLATFORM / "working" / "DELIVERY_ATLAS_WORKING_v0.2.2.md"
        cls.atlas = compact(atlas_path.read_text(encoding="utf-8")) if atlas_path.is_file() else ""

    def test_reconciled_authority_uses_successor_ids_and_paths(self):
        expected_current = {
            "PLATFORM_BASELINE": ("1.4.1", "00_PLATFORM_v1.4.1.md"),
            "DECISION_REGISTER": ("1.4.1", "01_DECISIONS_v1.4.1.md"),
            "DOMAIN_MAP": ("1.1.2", "04_DOMAIN_MAP_v1.1.2.md"),
            "OPEN_WORK": ("1.2.45", "02_OPEN_WORK_v1.2.45.md"),
        }
        for document_id, (version, filename) in expected_current.items():
            with self.subTest(document=document_id):
                entry = self.current[document_id]
                self.assertEqual(version, entry["semver"])
                self.assertEqual(filename, entry["canonical_filename"])
                self.assertTrue((ROOT / entry["repository_path"]).is_file())

        for document_id, version, path in (
            ("PLATFORM_BASELINE_V1_4_0", "1.4.0", "archive/00_PLATFORM_v1.4.0.md"),
            ("DECISION_REGISTER_V1_4_0", "1.4.0", "archive/01_DECISIONS_v1.4.0.md"),
            ("DOMAIN_MAP_V1_1_1", "1.1.1", "archive/04_DOMAIN_MAP_v1.1.1.md"),
            ("OPEN_WORK_V1_2_44", "1.2.44", "archive/02_OPEN_WORK_v1.2.44.md"),
        ):
            with self.subTest(predecessor=document_id):
                entry = self.historical.get(document_id)
                self.assertIsNotNone(entry, f"missing archived predecessor {document_id}")
                if entry is None:
                    continue
                self.assertEqual(version, entry["semver"])
                self.assertEqual(f"docs/00_platform/{path}", entry["repository_path"])
                self.assertTrue((PLATFORM / path).is_file())

    def test_decision_304_narrows_and_coexists_with_decision_301(self):
        self.assertIsNotNone(
            re.search(r"dec-304\s+—\s+marketing unsubscribe semantics", self.decisions),
            "DEC-304 must record marketing unsubscribe semantics",
        )
        self.assertIn("dec-301", self.decisions)
        self.assertTrue(self.product_unsubscribe, "Product Law needs a §21S successor")
        self.assertIn("dec-301 remains the general consent-withdrawal rule", self.product_unsubscribe)
        self.assertIn("dec-304 applies that rule specifically to marketing permission", self.product_unsubscribe)

    def test_domain_map_routes_privacy_withdrawal_without_shared_writes(self):
        for phrase in (
            "communications | privacy & consent |",
            "communications requests withdrawal through privacy & consent's owning interface",
            "privacy & consent validates and commits its own withdrawal",
            "communications never directly writes or mutates privacy-owned consent state",
            "marketing delivery revalidates current privacy consent and communications preference",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.domain_map, f"missing ownership route: {phrase}")

    def test_dol02_stays_gated_and_pr42_authorities_remain_current(self):
        self.assertEqual("1.2.2", self.current["PROJECT_NORTH_STAR_AND_MVP"]["semver"])
        self.assertEqual("1.1.1", self.current["ROADMAP"]["semver"])
        self.assertIn("harden-02_contract_working_v0.4.1.md", self.readme.casefold())
        gate = "required / downstream after certified engineering standards authority promotion / not performed"
        self.assertTrue(gate in self.readme.casefold(), "README must keep DOL-02 gated")
        self.assertTrue(gate in self.open_work, "Open Work must keep DOL-02 gated")
        self.assertTrue(self.atlas, "the Atlas needs a versioned routing successor")
        self.assertIn("fp001_reconciliation_required", self.atlas)
        for path in (
            "current-source routing",
            "00_platform_v1.4.1.md",
            "01_decisions_v1.4.1.md",
            "04_domain_map_v1.1.2.md",
            "02_open_work_v1.2.45.md",
        ):
            with self.subTest(atlas_anchor=path):
                self.assertTrue(path in self.atlas, f"Atlas routing is missing {path}")

        graph_rules = self.manifest["integrity_rules"]["graph_rules"]
        self.assertEqual(
            ["PLATFORM_BASELINE", "DECISION_REGISTER", "OPEN_WORK", "DOMAIN_MAP"],
            graph_rules["navigation_document_ids"],
        )
        self.assertEqual(
            ["docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.2.2.md"],
            graph_rules["navigation_document_paths"],
        )


if __name__ == "__main__":
    unittest.main()
