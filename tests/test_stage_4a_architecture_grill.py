from __future__ import annotations

import hashlib
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "docs"
    / "00_platform"
    / "working"
    / "TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md"
)
STAGE_3B_ARTIFACT = (
    ROOT
    / "docs"
    / "00_platform"
    / "working"
    / "TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md"
)
OPEN_WORK = ROOT / "docs" / "00_platform" / "archive" / "02_OPEN_WORK_v1.2.34.md"
README = ROOT / "docs" / "00_platform" / "README.md"
MANIFEST = ROOT / "docs" / "00_platform" / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

EXPECTED_ARQS = [
    "ARQ-SYS-007",
    "ARQ-SYS-008",
    "ARQ-SYS-009",
    "ARQ-SYS-010",
    "ARQ-IAM-009",
    "ARQ-IAM-010",
    "ARQ-IAM-011",
    "ARQ-IAM-012",
    "ARQ-IAM-013",
    "ARQ-STATE-008",
    "ARQ-STATE-009",
    "ARQ-STATE-010",
    "ARQ-STATE-011",
    "ARQ-STATE-012",
    "ARQ-STATE-013",
    "ARQ-ASYNC-004",
]

EXPECTED_DISPOSITIONS = {
    "ARQ-SYS-007": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-SYS-008": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-SYS-009": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-SYS-010": "EXISTING_ARCHITECTURE_SUFFICIENT",
    "ARQ-IAM-009": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-IAM-010": "EXISTING_ARCHITECTURE_SUFFICIENT",
    "ARQ-IAM-011": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-IAM-012": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-IAM-013": "DOWNSTREAM_DETAIL_ONLY",
    "ARQ-STATE-008": "EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION",
    "ARQ-STATE-009": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-STATE-010": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-STATE-011": "NEW_ARCHITECTURE_DECISION_REQUIRED",
    "ARQ-STATE-012": "EXISTING_ARCHITECTURE_SUFFICIENT",
    "ARQ-STATE-013": "EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION",
    "ARQ-ASYNC-004": "EXISTING_ARCHITECTURE_SUFFICIENT",
}

EXPECTED_QUESTIONS = {
    "ARQ-SYS-007": "Q1",
    "ARQ-SYS-008": "Q1",
    "ARQ-SYS-009": "Q1",
    "ARQ-SYS-010": "None",
    "ARQ-IAM-009": "Q2",
    "ARQ-IAM-010": "None",
    "ARQ-IAM-011": "Q3",
    "ARQ-IAM-012": "Q3",
    "ARQ-IAM-013": "None",
    "ARQ-STATE-008": "Q4",
    "ARQ-STATE-009": "Q5",
    "ARQ-STATE-010": "Q5",
    "ARQ-STATE-011": "Q5",
    "ARQ-STATE-012": "None",
    "ARQ-STATE-013": "Q4",
    "ARQ-ASYNC-004": "None",
}

EXPECTED_DISPOSITION_COUNTS = {
    "NEW_ARCHITECTURE_DECISION_REQUIRED": 9,
    "EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION": 2,
    "EXISTING_ARCHITECTURE_SUFFICIENT": 4,
    "DOWNSTREAM_DETAIL_ONLY": 1,
    "UPSTREAM_CONTRADICTION_STOP": 0,
}

PROTECTED_HASHES = {
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.0.0.md": "87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b",
    "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md": "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
    "docs/00_platform/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md": "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
    "docs/00_platform/archive/ARCHITECTURE_LAW_WORKING_v0.35.0.md": "a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639",
    "docs/00_platform/archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20",
}


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _closure_rows(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    start = text.index("## 16-ARQ closure matrix")
    end = text.index("### Disposition counts", start)
    section_lines = text[start:end].splitlines()
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for line in section_lines:
        if line.startswith("| ARQ |"):
            headers = _cells(line)
            continue
        if headers is None or not line.startswith("|"):
            continue
        if re.match(r"^\|\s*-+", line):
            continue
        values = _cells(line)
        if len(values) != len(headers):
            raise AssertionError(f"closure row width mismatch: {line}")
        rows.append(dict(zip(headers, values)))
    return rows


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Stage4AArchitectureGrillIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.rows = _closure_rows(cls.text)
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.stage_3b = STAGE_3B_ARTIFACT.read_text(encoding="utf-8")

    def test_artifact_banners_and_stop_boundary(self):
        self.assertIn("NON-AUTHORITATIVE / STAGE 4A ARCHITECTURE GRILL EVIDENCE", self.text)
        self.assertIn("DOES NOT AMEND PRODUCT LAW", self.text)
        self.assertIn("DOES NOT AMEND AR-000", self.text)
        self.assertIn("DOES NOT AMEND ARCHITECTURE LAW", self.text)
        self.assertIn("NO ARC IDENTIFIERS CREATED", self.text)
        self.assertIn("NO DOMAIN OWNERSHIP CREATED", self.text)
        self.assertIn("NO IMPLEMENTATION AUTHORISED", self.text)
        self.assertIn("a7cd4279cfddc67bb816f512231c3f7bfc8482c2", self.text)
        self.assertIn("ZERO CURRENT INDEPENDENT ARCHITECTURE GRILL PROPOSITIONS", self.text)

    def test_closure_matrix_covers_all_sixteen_arqs_with_expected_dispositions(self):
        self.assertEqual(16, len(self.rows))
        by_arq = {row["ARQ"].strip("`"): row for row in self.rows}
        self.assertEqual(set(EXPECTED_ARQS), set(by_arq))
        for arq, disposition in EXPECTED_DISPOSITIONS.items():
            self.assertEqual(disposition, by_arq[arq]["Coverage disposition"].strip("`"), arq)
            self.assertEqual(EXPECTED_QUESTIONS[arq], by_arq[arq]["Human question"].strip("`"), arq)
            self.assertTrue(by_arq[arq]["Relevant existing ARCs / Architecture"], arq)
            self.assertTrue(by_arq[arq]["Downstream-only detail"], arq)
            self.assertTrue(by_arq[arq]["Flow-impact flag"], arq)

        counts = Counter(
            row["Coverage disposition"].strip("`") for row in self.rows
        )
        for disposition, expected in EXPECTED_DISPOSITION_COUNTS.items():
            self.assertEqual(expected, counts[disposition], disposition)

    def test_material_human_decisions_are_explicitly_accepted(self):
        for question in ("Q1", "Q2", "Q3", "Q4", "Q5"):
            self.assertIn(
                f"**Human decision:** `ACCEPT OPTION 1 WITH REFINEMENT`",
                self.text,
            )
            self.assertIn(f"### {question} —", self.text)
        self.assertEqual(5, self.text.count("ACCEPT OPTION 1 WITH REFINEMENT"))
        self.assertNotIn("PENDING HUMAN ACCEPTANCE", self.text)

    def test_no_arc_identifiers_created_and_architecture_amendment_not_begun(self):
        self.assertIsNone(
            re.search(
                r"^#{1,6} (?:DEC|OQ|ARC|ARQ|CAP|FP|TB|VS|HH)-",
                self.text,
                re.MULTILINE,
            )
        )
        # Existing ARC-001…ARC-327 may be cited as evidence; no ARC-328+ may be allocated.
        self.assertIsNone(
            re.search(r"\bARC-(?:32[8-9]|3[3-9]\d|[4-9]\d{2})\b", self.text)
        )
        self.assertIn("No `ARC-*` identifier is allocated in Stage 4A.", self.text)
        self.assertIn("Architecture amendment begun: **no**", self.text)
        self.assertIn("Engineering-Policy Grill begun: **no**", self.text)
        self.assertIn("ARCHITECTURE AMENDMENT: NOT_STARTED", self.open_work)
        self.assertIn("ARCHITECTURE AMENDMENT: COMPLETE", self.readme)

    def test_stage_3b_independent_architecture_queue_remains_zero(self):
        self.assertIn("### Queue B: Architecture Grill", self.stage_3b)
        queue_b = self.stage_3b[
            self.stage_3b.index("### Queue B: Architecture Grill") : self.stage_3b.index(
                "### Queue C: Engineering-Policy Grill"
            )
        ]
        self.assertEqual(set(), set(re.findall(r"\*\*([A-D]-\d{2}(?:-[AP])?)\*\*", queue_b)))
        self.assertIn("ZERO CURRENT INDEPENDENT ARCHITECTURE GRILL PROPOSITIONS", self.text)

    def test_planning_state_advances_to_engineering_policy_grill_next(self):
        self.assertIn("ARCHITECTURE GRILL: COMPLETE", self.open_work)
        self.assertIn("ENGINEERING-POLICY GRILL: NOT_STARTED / NEXT", self.open_work)
        self.assertIn("ARCHITECTURE AMENDMENT: COMPLETE", self.readme)
        self.assertIn("ARCHITECTURE GRILL: COMPLETE", self.readme)
        self.assertIn("TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md", self.readme)
        self.assertTrue(
            (ROOT / "docs" / "00_platform" / "archive" / "02_OPEN_WORK_v1.2.34.md").is_file()
        )
        self.assertNotIn("TARGETED_ARCHITECTURE_GRILL", MANIFEST.read_text(encoding="utf-8"))

    def test_protected_authority_and_evidence_hashes_remain_unchanged(self):
        for relative_path, expected_hash in PROTECTED_HASHES.items():
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)


if __name__ == "__main__":
    unittest.main()
