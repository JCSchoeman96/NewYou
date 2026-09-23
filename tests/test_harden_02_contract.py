from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.2.0.md"
CONTRACT_PREDECESSOR = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.1.0.md"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.41.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.40.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

PROTECTED_UPSTREAM_HASHES = {
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/03_ARCHITECTURE_v1.1.0.md": "d44615f0db3f5f0b38bb68a2904db6066d23e1f82c55da134745c4f6d70b6852",
    "docs/00_platform/04_DOMAIN_MAP_v1.1.0.md": "2c66142e624ccd626727ae36511121fcb64333ca774986ab97ce31eebe5c5ef2",
    "docs/00_platform/05_ROADMAP_v1.1.0.md": "eaeaf6031e47653777caf5885ad9eb0ceba58783c99d7d6d255acfbca53fa613",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": "caadd2dfc3c7ed872fda5806efdba467d753b9662e1ff47af16b6303d90b9fa3",
    "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.39.md": "5af9c6965d214bb0dd46cd3215a2e23ed1a17d546ef53ccd4de31be346d11e21",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.40.md": "e53d416efe2b859053e4d2167b36065383f4f67603db56d833f20247d5120b3e",
    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.1.0.md": "71615d3363a91a7e6002d907c6edd474fbd87f77bdfc6a38f5b11afd240a5626",
}

# Superseded active routing paths only. Do not permanently forbid later Engineering
# Standards or application bootstrap artifacts.
PROHIBITED_PRESENT_PATHS = (
    "docs/00_platform/02_OPEN_WORK_v1.2.39.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.40.md",
    "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.1.0.md",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Harden02ContractDraftingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = CONTRACT.read_text(encoding="utf-8")
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_contract_artifact_identity_and_authority_class(self):
        self.assertTrue(CONTRACT.is_file())
        self.assertIn("Contract ID:** `HARDEN-02`", self.contract)
        self.assertIn("WORKING GOVERNANCE CONTRACT", self.contract)
        self.assertIn("OPEN / PENDING INDEPENDENT CERTIFICATION", self.contract)
        self.assertIn("execution **NOT AUTHORISED**", self.contract)
        self.assertNotIn("CURRENT_AUTHORITY_MANIFEST", self.contract.split("Authority class")[0])
        self.assertNotIn("ee3f9d2", self.contract)
        self.assertNotIn("6e9ab62", self.contract)
        self.assertNotIn("REUSE_HARDENING", self.contract)

    def test_objective_and_governance_boundary(self):
        self.assertIn(
            "Phase-7 delivery-pipeline governance integrity",
            self.contract,
        )
        self.assertIn("FP001_RECONCILIATION_REQUIRED", self.contract)
        self.assertIn("not an FP-001 dependency, Roadmap gate, Product requirement or blocking OQ", self.contract)
        for forbidden_label in (
            "Store Blueprint / CER reuse",
            "Commerce/Entitlements",
            "subscription-engine",
        ):
            self.assertIn(forbidden_label, self.contract)
        self.assertIn("Store Blueprint / CER: **EXCLUDED**", self.contract)
        self.assertIn("Commerce / Entitlements hardening: **EXCLUDED**", self.contract)
        self.assertIn("H02-1", self.contract)
        self.assertIn("H02-2", self.contract)
        self.assertIn("H02-3", self.contract)
        self.assertIn("H02-3R", self.contract)
        self.assertIn("I-01", self.contract)
        self.assertIn("I-13", self.contract)

    def test_store_cer_explicitly_excluded(self):
        self.assertIn("Store Blueprint / CER is OUT OF SCOPE", self.contract)
        self.assertIn("working/commerce_entitlements/*", self.contract)
        self.assertIn("I-13 — Store/CER exclusion", self.contract)
        self.assertIsNone(re.search(r"Store default branch `main`: `[0-9a-f]{40}`", self.contract))
        self.assertNotIn("486a1c74f5b738d488fdd54118002e90ec67bd49", self.contract)
        self.assertNotIn("77a272c3887a7ab46e84a7fed02163d964e37b9b", self.contract)

    def test_downstream_resume_order(self):
        self.assertIn("HARDEN-02_EXECUTION_REQUIRED", self.open_work)
        self.assertIn("ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED", self.open_work)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", self.open_work)
        self.assertIn(
            "Engineering Standards Authority Promotion → narrow FP-001 PMR reconciliation → Communications JIT",
            self.contract,
        )
        self.assertIn("NEXT = ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED", self.contract)
        self.assertIn(
            "After independently certified Engineering Standards Authority Promotion",
            self.contract,
        )
        self.assertIn(
            "After independently certified narrow FP-001 PMR reconciliation",
            self.contract,
        )
        self.assertIn("Communications JIT Domain Dossier", self.contract)

    def test_execution_requires_merge_and_post_merge_certification(self):
        self.assertIn("HARDEN-02 EXECUTION: NOT STARTED", self.open_work)
        self.assertIn("REQUIRES MERGE + POST-MERGE CERTIFICATION OF MAIN", self.open_work)
        self.assertIn("pre-merge exact-head review is not execution authority", self.open_work)
        self.assertIn("merged unchanged", self.open_work)
        self.assertIn("post-merge certified", self.open_work)
        self.assertIn("REQUIRES MERGE + POST-MERGE CERTIFICATION OF MAIN", self.readme)
        self.assertIn("merged unchanged", self.readme)
        self.assertIn("post-merge certified", self.readme)
        self.assertIn(
            "merged unchanged and the resulting `main` is independently post-merge certified",
            self.contract,
        )
        self.assertIn(
            "pre-merge exact-head certification of this PR is **not** sufficient",
            self.contract,
        )
        self.assertNotIn("HARDEN-02 EXECUTION: COMPLETE", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.readme)

    def test_engineering_standards_promotion_is_routed_but_not_started(self):
        marker = (
            "ENGINEERING STANDARDS AUTHORITY PROMOTION: "
            "DOWNSTREAM AFTER CERTIFIED HARDEN-02 EXECUTION / NOT STARTED"
        )
        self.assertIn(marker, self.open_work)
        self.assertIn(marker, self.readme)
        self.assertIn("Engineering Standards: **NOT STARTED by HARDEN-02**", self.contract)
        self.assertIn(
            "Engineering Standards Authority Promotion: **NOT EXECUTED by HARDEN-02**",
            self.contract,
        )
        self.assertIn("Application code: **UNCHANGED by this contract stage**", self.contract)
        self.assertIn("application source code", self.contract)

    def test_counts_and_fp001_state_unchanged(self):
        self.assertIn("Domain count is **20**", self.open_work)
        self.assertIn("Feature Pack count remains **17**", self.open_work)
        self.assertIn("IDENTITY & ACCESS: COMPLETE / MERGED", self.open_work)
        self.assertIn("COMMUNICATIONS: REQUIRED / NOT_STARTED", self.open_work)
        self.assertIn("PHASE 7C: BLOCKED / NOT_STARTED", self.open_work)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", self.open_work)

    def test_open_work_readme_manifest_coherent(self):
        self.assertTrue(OPEN_WORK.is_file())
        self.assertTrue(OPEN_WORK_PREDECESSOR.is_file())
        self.assertTrue(CONTRACT_PREDECESSOR.is_file())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.40.md").exists())
        self.assertFalse((DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.1.0.md").exists())
        self.assertIn("v1.2.40 → v1.2.41", self.open_work)
        self.assertIn("02_OPEN_WORK_v1.2.41.md", self.readme)
        self.assertIn("HARDEN-02_CONTRACT_WORKING_v0.2.0.md", self.readme)
        self.assertIn("HARDEN-02_EXECUTION_REQUIRED", self.readme)
        self.assertIn("ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED", self.readme)
        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertEqual("1.2.41", current["OPEN_WORK"]["semver"])
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.41.md", current["OPEN_WORK"]["repository_path"])
        self.assertEqual(_sha256(OPEN_WORK), current["OPEN_WORK"]["sha256"])
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_40"]["lifecycle"])
        self.assertEqual(_sha256(OPEN_WORK_PREDECESSOR), historical["OPEN_WORK_V1_2_40"]["sha256"])

    def test_upstream_authority_and_fp001_hashes_unchanged(self):
        for relative_path, expected_hash in PROTECTED_UPSTREAM_HASHES.items():
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)
        for relative_path in PROHIBITED_PRESENT_PATHS:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)

    def test_contract_not_in_authority_manifest(self):
        paths = [
            entry.get("repository_path", "")
            for section in ("governing_documents", "reference_documents", "historical_documents")
            for entry in self.manifest[section]
        ]
        self.assertTrue(all("HARDEN-02" not in path for path in paths))


if __name__ == "__main__":
    unittest.main()
