from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "docs"
    / "00_platform"
    / "working"
    / "TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md"
)
STAGE_3B_ARTIFACT = (
    ROOT
    / "docs"
    / "00_platform"
    / "working"
    / "TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md"
)
STAGE_4A_ARTIFACT = (
    ROOT
    / "docs"
    / "00_platform"
    / "working"
    / "TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md"
)
OPEN_WORK = ROOT / "docs" / "00_platform" / "archive" / "02_OPEN_WORK_v1.2.35.md"
README = ROOT / "docs" / "00_platform" / "README.md"
MANIFEST = ROOT / "docs" / "00_platform" / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

POLICY_KEYS = ("A-08", "B-09", "D-02", "D-03", "D-04", "D-05", "D-07")
EXPECTED_CLUSTERS = {
    "A-08": "EP-Q2",
    "B-09": "EP-Q3",
    "D-02": "EP-Q4",
    "D-03": "EP-Q4",
    "D-07": "EP-Q4",
    "D-04": "EP-Q5",
    "D-05": "EP-Q5",
}
DEFERRED_KEYS = ("A-06", "A-09", "C-03", "C-04", "C-07")
REJECTED_KEYS = ("A-10", "B-08", "B-10", "C-06", "C-08", "D-08", "D-09")
HUMAN_QUESTIONS = ("EP-Q1", "EP-Q2", "EP-Q3", "EP-Q4", "EP-Q5")

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


def _coverage_rows(text: str) -> list[dict[str, str]]:
    start = text.index("## Seven-proposition coverage matrix")
    end = text.index("##", start + len("## Seven-proposition coverage matrix"))
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []
    for line in text[start:end].splitlines():
        if line.startswith("| Stage 3B key |"):
            headers = _cells(line)
            continue
        if headers is None or not line.startswith("|"):
            continue
        if re.match(r"^\|\s*-+", line):
            continue
        values = _cells(line)
        if len(values) != len(headers):
            raise AssertionError(f"coverage row width mismatch: {line}")
        rows.append(dict(zip(headers, values)))
    return rows


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Stage4BEngineeringPolicyGrillIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.rows = _coverage_rows(cls.text)
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = MANIFEST.read_text(encoding="utf-8")
        cls.stage_3b = STAGE_3B_ARTIFACT.read_text(encoding="utf-8")
        cls.stage_4a = STAGE_4A_ARTIFACT.read_text(encoding="utf-8")

    def test_artifact_banners_and_stop_boundary(self):
        self.assertIn(
            "NON-AUTHORITATIVE / STAGE 4B ENGINEERING-POLICY GRILL EVIDENCE",
            self.text,
        )
        self.assertIn("DOES NOT AMEND PRODUCT LAW", self.text)
        self.assertIn("DOES NOT AMEND AR-000", self.text)
        self.assertIn("DOES NOT AMEND ARCHITECTURE LAW", self.text)
        self.assertIn("DOES NOT CREATE ENGINEERING STANDARDS", self.text)
        self.assertIn("DOES NOT INSTALL OR SELECT DEPENDENCIES", self.text)
        self.assertIn("NO GOVERNED IDENTIFIERS CREATED", self.text)
        self.assertIn("NO IMPLEMENTATION AUTHORISED", self.text)
        self.assertIn("d2477e2d3d49187610fdee6b5aedb799df8bfe02", self.text)
        self.assertNotIn("PENDING HUMAN ACCEPTANCE", self.text)

    def test_seven_stage_3b_policy_propositions_are_covered(self):
        self.assertEqual(7, len(self.rows))
        by_key = {row["Stage 3B key"].strip("`"): row for row in self.rows}
        self.assertEqual(set(POLICY_KEYS), set(by_key))
        for key, question in EXPECTED_CLUSTERS.items():
            self.assertEqual(question, by_key[key]["Human question"].strip("`"), key)
            self.assertIn("ACCEPTED", by_key[key]["Accepted human answer"].upper(), key)
            self.assertTrue(by_key[key]["Accepted policy direction"], key)

    def test_every_material_question_has_explicit_human_acceptance(self):
        self.assertEqual(5, len(HUMAN_QUESTIONS))
        for question in HUMAN_QUESTIONS:
            self.assertIn(f"### {question} —", self.text)
        self.assertEqual(5, self.text.count("ACCEPTED WITH REFINEMENT"))
        self.assertIn("`LOW`", self.text)
        self.assertIn("`STANDARD`", self.text)
        self.assertIn("`HIGH`", self.text)
        self.assertIn("`financial`", self.text)
        self.assertIn("`entitlement`", self.text)
        self.assertIn("`safety`", self.text)
        self.assertIn("`privacy_deletion`", self.text)
        self.assertIn("`privileged_security`", self.text)
        self.assertIn("`irreversible`", self.text)
        self.assertIn("Do not introduce a fourth `CRITICAL` tier", self.text)

    def test_deferred_and_rejected_stage_3b_items_remain_closed(self):
        deferred = self.text[
            self.text.index("## Deferred and rejected Stage 3B items remain closed") :
        ]
        for key in DEFERRED_KEYS:
            self.assertIn(f"`{key}`", deferred)
            self.assertIn("DEFER_NO_CURRENT_EVIDENCE", self.stage_3b)
        for key in REJECTED_KEYS:
            self.assertIn(f"`{key}`", deferred)
        self.assertIn("A Stage 4B preference is not evidence sufficient to reopen", self.text)

    def test_no_architecture_proposition_or_engineering_standard_is_created(self):
        self.assertIn("Independent Stage 3B Architecture Grill propositions reintroduced: **0**", self.text)
        self.assertIn("Architecture changes: **0**", self.text)
        self.assertIn("Domain changes: **0**", self.text)
        self.assertIn("Engineering Standards created: **none**", self.text)
        self.assertIn("Architecture amendment begun: **no**", self.text)
        self.assertIsNone(
            re.search(
                r"^#{1,6} (?:DEC|OQ|ARC|ARQ|CAP|FP|TB|VS|HH)-",
                self.text,
                re.MULTILINE,
            )
        )
        self.assertIsNone(
            re.search(r"\bARC-(?:32[8-9]|3[3-9]\d|[4-9]\d{2})\b", self.text)
        )
        self.assertFalse((ROOT / "mix.exs").exists())
        self.assertFalse((ROOT / ".formatter.exs").exists())
        self.assertFalse((ROOT / ".credo.exs").exists())
        workflow_dir = ROOT / ".github" / "workflows"
        self.assertEqual(
            ["foundation-integrity.yml"],
            sorted(path.name for path in workflow_dir.glob("*")),
        )

    def test_planning_routes_architecture_amendment_next_after_stage_4b(self):
        self.assertIn("ARCHITECTURE GRILL: COMPLETE", self.open_work)
        self.assertIn("ENGINEERING-POLICY GRILL: COMPLETE", self.open_work)
        self.assertIn("ARCHITECTURE AMENDMENT: NOT_STARTED / NEXT", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.open_work)
        self.assertIn("ARCHITECTURE GRILL: COMPLETE", self.readme)
        self.assertIn("ENGINEERING-POLICY GRILL: COMPLETE", self.readme)
        self.assertIn("ARCHITECTURE AMENDMENT: COMPLETE", self.readme)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.readme)
        self.assertIn("TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md", self.readme)
        self.assertIn('"semver": "1.2.36"', self.manifest)
        self.assertNotIn("TARGETED_ENGINEERING_POLICY_GRILL", self.manifest)
        self.assertIn("Engineering Standards remain downstream", self.text)

    def test_protected_authority_and_stage_4a_evidence_remain_unchanged(self):
        for relative_path, expected_hash in PROTECTED_HASHES.items():
            if expected_hash is None:
                continue
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)
        self.assertEqual(
            "87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b",
            _sha256(ROOT / "docs/00_platform/archive/03_ARCHITECTURE_v1.0.0.md"),
        )
        self.assertIn("Engineering-Policy Grill begun: **no**", self.stage_4a)
        queue_c = self.stage_3b[
            self.stage_3b.index("### Queue C: Engineering-Policy Grill") : self.stage_3b.index(
                "### Queue D: Deferred / rejected"
            )
        ]
        self.assertEqual(
            set(POLICY_KEYS),
            set(re.findall(r"\*\*([A-D]-\d{2})\*\*", queue_c)),
        )


if __name__ == "__main__":
    unittest.main()
