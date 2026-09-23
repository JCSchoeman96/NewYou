from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
DOMAIN_MAP = DOCS / "04_DOMAIN_MAP_v1.1.0.md"
DOMAIN_MAP_PREDECESSOR = DOCS / "archive" / "04_DOMAIN_MAP_v1.0.0.md"
EVIDENCE = DOCS / "working" / "TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md"
OPEN_WORK = DOCS / "archive" / "02_OPEN_WORK_v1.2.37.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.36.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

HISTORICAL_DOMAINS = (
    "Identity & Access",
    "Privacy & Consent",
    "Temperament",
    "Health Records",
    "Safety & Eligibility",
    "Plans & Nutrition",
    "Content & Media",
    "Programmes & Challenges",
    "Habits, Journals & Progress",
    "Commerce",
    "Entitlements",
    "Community",
    "Events & Live",
    "Professional Care",
    "Communications",
    "Experimentation",
    "Analytics",
    "Audit & Evidence",
)

REJECTED_DOMAIN_NAMES = (
    "Interactive Tools",
    "Interactive Evidence",
    "Engagement",
    "Platform Member Reference",
    "Competitions",
)

PROTECTED_HASHES = {
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/03_ARCHITECTURE_v1.1.0.md": "d44615f0db3f5f0b38bb68a2904db6066d23e1f82c55da134745c4f6d70b6852",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": "caadd2dfc3c7ed872fda5806efdba467d753b9662e1ff47af16b6303d90b9fa3",
    "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md": "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
    "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md": "26ff1e7a7e40945e501793c2bfb2ede9c01ae03f7949383ae724e3b031fa4faa",
    "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md": "0d8e25170ae692df39f7f771189f95ab76ab64f2701823fb2cde214946650d3f",
    "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.1.0.md": "8cb7769018c21b09c91208c5991b1b9bca09141c5fa0ef74cd577946d76377f1",
    "docs/00_platform/working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md": "27bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017",
    ".github/workflows/foundation-integrity.yml": "2c718457456c71ad8d7fc416a6e0a646792271b9341e4a14fedda6ddb02bcdb8",
}

REQUIRED_SUCCESSOR_PATHS = (
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.37.md",
    "docs/00_platform/04_DOMAIN_MAP_v1.1.0.md",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.36.md",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md",
    "docs/00_platform/working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md",
)

PROHIBITED_PRESENT_PATHS = (
    "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.36.md",
    "mix.exs",
    "docs/00_platform/ENGINEERING_STANDARDS_v1.0.0.md",
    "docs/00_platform/reference/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    "docs/00_platform/working/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
)

OWNERSHIP_EXPECTATIONS = {
    "Research/feedback campaign, instrument and published version": "Research & Feedback",
    "Participant Research/feedback response": "Research & Feedback",
    "Research correction, withdrawal and de-link lifecycle": "Research & Feedback",
    "Staff Research annotation/classification": "Research & Feedback",
    "Governed vote/poll rules": "Voting & Balloting",
    "Vote submission and integrity disposition evidence": "Voting & Balloting",
    "Accepted vote tally": "Voting & Balloting",
    "Governed vote finalisation": "Voting & Balloting",
    "Official voting result": "Voting & Balloting",
    "Vote exception, adjudication, correction and rerun": "Voting & Balloting",
    "Platform Member Reference lifecycle": "Identity & Access",
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _table_rows(text: str, heading: str, next_heading: str) -> list[dict[str, str]]:
    start = text.index(heading)
    end = text.index(next_heading, start)
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []
    for line in text[start:end].splitlines():
        if line.startswith("|") and headers is None:
            headers = [cell.strip() for cell in line.strip("|").split("|")]
            continue
        if headers is None or not line.startswith("|") or re.match(r"^\|\s*-+", line):
            continue
        values = [cell.strip() for cell in line.strip("|").split("|")]
        if len(values) == len(headers):
            rows.append(dict(zip(headers, values)))
    return rows


class DomainAmendmentIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.domain_map = DOMAIN_MAP.read_text(encoding="utf-8")
        cls.predecessor = DOMAIN_MAP_PREDECESSOR.read_text(encoding="utf-8")
        cls.evidence = EVIDENCE.read_text(encoding="utf-8")
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.domain_rows = _table_rows(
            cls.domain_map,
            "## 3. Approved domain set",
            "## 4. Platform-wide business-truth ownership matrix",
        )
        cls.ownership_rows = _table_rows(
            cls.domain_map,
            "## 4. Platform-wide business-truth ownership matrix",
            "### 4.1 Ownership interpretation",
        )

    def test_predecessor_is_byte_identical_and_successor_uses_explicit_semver(self):
        self.assertEqual(
            "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
            _sha256(DOMAIN_MAP_PREDECESSOR),
        )
        self.assertEqual(
            "69b7c00a6b134cdfe80ecb8e2cb5b10350159c95bdbb79067bcb3225dbb3d34c",
            _sha256(OPEN_WORK_PREDECESSOR),
        )
        self.assertIn("v1.0.0 → v1.1.0", self.domain_map)
        self.assertIn("v1.2.36 → v1.2.37", self.open_work)
        self.assertIn("archive/04_DOMAIN_MAP_v1.0.0.md", self.domain_map)
        self.assertFalse((DOCS / "04_DOMAIN_MAP_v1.0.0.md").exists())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.36.md").exists())

    def test_approved_domain_set_is_20_with_historical_1_to_18_unchanged(self):
        numbered = [row for row in self.domain_rows if row["#"].isdigit()]
        self.assertEqual(20, len(numbered))
        self.assertEqual([str(number) for number in range(1, 21)], [row["#"] for row in numbered])
        self.assertEqual(list(HISTORICAL_DOMAINS), [row["Domain"].strip("*") for row in numbered[:18]])
        self.assertEqual("Research & Feedback", numbered[18]["Domain"].strip("*"))
        self.assertEqual("Voting & Balloting", numbered[19]["Domain"].strip("*"))
        self.assertEqual(20, len({row["Domain"].strip("*") for row in numbered}))
        predecessor_numbered = [
            row for row in _table_rows(
                self.predecessor,
                "## 3. Approved domain set",
                "## 4. Platform-wide business-truth ownership matrix",
            )
            if row["#"].isdigit()
        ]
        self.assertEqual(18, len(predecessor_numbered))
        self.assertEqual(
            [(row["#"], row["Domain"]) for row in predecessor_numbered],
            [(row["#"], row["Domain"]) for row in numbered[:18]],
        )

    def test_new_ownership_rows_have_exactly_one_approved_owner(self):
        domains = {row["Domain"].strip("*") for row in self.domain_rows if row["#"].isdigit()}
        by_truth = {row["Business truth"]: row for row in self.ownership_rows}
        self.assertEqual(61, len(self.ownership_rows))
        for truth, owner in OWNERSHIP_EXPECTATIONS.items():
            self.assertIn(truth, by_truth, truth)
            owners = re.findall(r"\*\*(.+?)\*\*", by_truth[truth]["Authoritative domain"])
            self.assertEqual([owner], owners, truth)
            self.assertIn(owner, domains)
        findings = by_truth.get("Governed content/translation/publication version")
        self.assertIsNotNone(findings)
        self.assertIn("Content & Media", findings["Authoritative domain"])

    def test_rejected_pseudo_domains_are_not_approved(self):
        approved = "\n".join(row["Domain"] for row in self.domain_rows if row["#"].isdigit())
        for name in REJECTED_DOMAIN_NAMES:
            self.assertNotIn(f"**{name}**", approved)
            self.assertNotIn(f"| {name} |", approved)
        self.assertNotIn("### 6.21", self.domain_map)
        self.assertNotIn("Voting / Balloting / Competitions", self.domain_map.split("## 14.")[0])
        self.assertIn("Voting & Balloting", self.domain_map)
        self.assertIn("Research & Feedback", self.domain_map)

    def test_tools_boundary_is_purpose_distributed_not_generic(self):
        content = self.domain_map[self.domain_map.index("### 6.7 — Content & Media") : self.domain_map.index("### 6.8 —")]
        habits = self.domain_map[self.domain_map.index("### 6.9 — Habits, Journals & Progress") : self.domain_map.index("### 6.10 —")]
        self.assertIn("published Interactive Tool editorial/presentation artifacts", content)
        self.assertIn("calculation algorithms", content)
        self.assertNotIn("owns all Interactive Tool calculations", content.lower())
        self.assertIn("Account-linked Interactive Tool results only when", habits)
        self.assertIn("generic persisted Interactive Tool results", habits)
        self.assertNotIn("any persisted tool result", habits)
        self.assertIn("Purpose-distributed among existing owners; **not** a Domain", self.domain_map)
        self.assertIn("calculation is not authority", self.domain_map.lower())

    def test_handoffs_keep_rewards_analytics_and_audit_non_source(self):
        self.assertIn("Research & Feedback | Commerce", self.domain_map.replace("`", ""))
        self.assertIn("Research & Feedback | Entitlements", self.domain_map.replace("`", ""))
        self.assertIn("Voting & Balloting | Commerce", self.domain_map.replace("`", ""))
        self.assertIn("Voting & Balloting | Entitlements", self.domain_map.replace("`", ""))
        analytics = self.domain_map[self.domain_map.index("### 6.17 — Analytics") : self.domain_map.index("### 6.18 —")]
        audit = self.domain_map[self.domain_map.index("### 6.18 — Audit & Evidence") : self.domain_map.index("## 7.")]
        self.assertIn("Research responses, accepted vote tally, official voting result", analytics)
        self.assertIn("Research responses, official voting results or Platform Member Reference as business truth", audit)
        self.assertIn("reward/entitlement is a separately owned consequence", self.domain_map)

    def test_identity_owns_pmr_without_freezing_representation(self):
        identity = self.domain_map[self.domain_map.index("### 6.1 — Identity & Access") : self.domain_map.index("### 6.2 —")]
        self.assertIn("Platform Member Reference assignment after successful individual Account creation", identity)
        self.assertIn("minimum-disclosure PMR lookup", identity)
        self.assertIn("never proves Account control", identity)
        self.assertIn("ARQ-IAM-013", identity)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", identity)
        for frozen in ("alphabet", "grouping", "checksum", "generator"):
            self.assertIn(frozen, identity)
        self.assertIn("Exact prefix", identity)

    def test_research_and_voting_profiles_exist_and_exclude_foreign_authority(self):
        research = self.domain_map[self.domain_map.index("### 6.19 — Research & Feedback") : self.domain_map.index("### 6.20 —")]
        voting = self.domain_map[self.domain_map.index("### 6.20 — Voting & Balloting") : self.domain_map.index("## 7.")]
        self.assertIn("DEC-294", research)
        self.assertIn("ARC-331", research)
        self.assertIn("participant Research/feedback submission", research)
        self.assertIn("staff annotation/classification", research)
        self.assertIn("do not directly mutate Health, Safety, Plans, Temperament, Commerce or Entitlements", research)
        self.assertIn("generic survey-builder", research)
        self.assertIn("DEC-295", voting)
        self.assertIn("ARC-332", voting)
        self.assertIn("official result", voting)
        self.assertIn("not a mandate for seven Resources", voting)
        self.assertIn("Research polls", voting)
        self.assertIn("does not own competitions as a whole", voting.lower())
        self.assertIn("Authority ≠ acceleration", research + voting)

    def test_pressure_test_evidence_is_non_authoritative_and_records_human_decisions(self):
        self.assertIn("NON-AUTHORITATIVE / DOMAIN PRESSURE-TEST EVIDENCE", self.evidence)
        self.assertIn("Domain Law is created only by the versioned Domain Map successor", self.evidence)
        self.assertIn("f5170caeb09dcffe80c20fbc7d251c854a422a66", self.evidence)
        self.assertIn("47", self.evidence)
        self.assertIn("DQ-1", self.evidence)
        self.assertIn("ACCEPT", self.evidence)
        self.assertIn("ACCEPT WITH NAMING REFINEMENT", self.evidence)
        self.assertIn("Research & Feedback", self.evidence)
        self.assertIn("Voting & Balloting", self.evidence)
        self.assertIn("Contradiction count:", self.evidence)
        self.assertIn("`0`", self.evidence)

    def test_open_work_readme_and_manifest_route_the_successor(self):
        self.assertIn("DOMAIN AMENDMENT: COMPLETE", self.open_work)
        self.assertIn("DOMAIN PRESSURE TEST: COMPLETE", self.open_work)
        self.assertIn("ROADMAP SEQUENCING GRILL: NEXT / NOT STARTED", self.open_work)
        self.assertIn("ROADMAP_REVIEW_REQUIRED", self.open_work)
        self.assertIn("FP001_RECONCILIATION_REQUIRED", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.open_work)
        self.assertIn("ENGINEERING STANDARDS: DOWNSTREAM", self.open_work)
        self.assertIn("04_DOMAIN_MAP_v1.1.0.md", self.readme)
        self.assertIn("archive/02_OPEN_WORK_v1.2.37.md", self.readme)
        self.assertIn("DOMAIN AMENDMENT: COMPLETE", self.readme)
        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        self.assertEqual("1.2.42", current["OPEN_WORK"]["semver"])
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.42.md", current["OPEN_WORK"]["repository_path"])
        self.assertEqual(_sha256(ROOT / current["OPEN_WORK"]["repository_path"]), current["OPEN_WORK"]["sha256"])
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_37"]["lifecycle"])
        self.assertEqual(_sha256(OPEN_WORK), historical["OPEN_WORK_V1_2_37"]["sha256"])
        self.assertEqual("1.1.0", current["DOMAIN_MAP"]["semver"])
        self.assertEqual("docs/00_platform/04_DOMAIN_MAP_v1.1.0.md", current["DOMAIN_MAP"]["repository_path"])
        self.assertEqual(_sha256(DOMAIN_MAP), current["DOMAIN_MAP"]["sha256"])
        self.assertEqual(20, self.manifest["integrity_rules"]["expected_counts"]["domains"])
        self.assertEqual(61, self.manifest["integrity_rules"]["expected_counts"]["ownership_rows"])
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_36"]["lifecycle"])
        self.assertEqual("historical", historical["DOMAIN_MAP_V1_0_0"]["lifecycle"])
        self.assertEqual(
            "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
            historical["DOMAIN_MAP_V1_0_0"]["sha256"],
        )

    def test_protected_upstream_and_downstream_artifacts_keep_exact_hashes(self):
        for relative_path, expected_hash in PROTECTED_HASHES.items():
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)

    def test_scope_has_no_implementation_or_prohibited_artifact_changes(self):
        for relative_path in REQUIRED_SUCCESSOR_PATHS:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)
        for relative_path in PROHIBITED_PRESENT_PATHS:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)
        self.assertFalse((ROOT / ".formatter.exs").exists())
        self.assertFalse((ROOT / ".credo.exs").exists())
        workflow_dir = ROOT / ".github" / "workflows"
        self.assertEqual(
            ["foundation-integrity.yml"],
            sorted(path.name for path in workflow_dir.glob("*")),
        )
        self.assertEqual(
            PROTECTED_HASHES[".github/workflows/foundation-integrity.yml"],
            _sha256(workflow_dir / "foundation-integrity.yml"),
        )
        for forbidden in ("LOW/STANDARD/HIGH", "typespec", "Dialyzer", "Credo", "Splode"):
            self.assertNotIn(forbidden, self.domain_map)


if __name__ == "__main__":
    unittest.main()
