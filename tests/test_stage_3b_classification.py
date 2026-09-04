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
    / "TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md"
)

CLASSIFICATIONS = {
    "ALREADY_GOVERNED_NO_CHANGE",
    "ARCHITECTURE_GRILL_REQUIRED",
    "ENGINEERING_POLICY_GRILL_REQUIRED",
    "SPLIT_ARCHITECTURE_AND_ENGINEERING_POLICY",
    "DEFER_NO_CURRENT_EVIDENCE",
    "REJECT_UNNECESSARY_COMPLEXITY",
    "UPSTREAM_CONTRADICTION_STOP",
}

EXPECTED_COUNTS = {
    "ALREADY_GOVERNED_NO_CHANGE": 18,
    "ARCHITECTURE_GRILL_REQUIRED": 2,
    "ENGINEERING_POLICY_GRILL_REQUIRED": 6,
    "SPLIT_ARCHITECTURE_AND_ENGINEERING_POLICY": 2,
    "DEFER_NO_CURRENT_EVIDENCE": 3,
    "REJECT_UNNECESSARY_COMPLEXITY": 7,
    "UPSTREAM_CONTRADICTION_STOP": 0,
}

EXPECTED_QUEUES = {
    "Queue A: Already governed": {
        "A-01",
        "A-02",
        "A-04",
        "A-05",
        "A-07",
        "A-11",
        "B-01",
        "B-02",
        "B-03",
        "B-04",
        "B-05",
        "B-06",
        "B-07",
        "C-01",
        "C-02",
        "C-05",
        "D-01",
        "D-06",
    },
    "Queue B: Architecture Grill": {"A-03", "C-03", "C-04-A", "D-07-A"},
    "Queue C: Engineering-Policy Grill": {
        "A-08",
        "B-09",
        "D-02",
        "D-03",
        "D-04",
        "D-05",
        "C-04-P",
        "D-07-P",
    },
    "Queue D: Deferred / rejected": {
        "A-06",
        "A-09",
        "C-07",
        "A-10",
        "B-08",
        "B-10",
        "C-06",
        "C-08",
        "D-08",
        "D-09",
    },
}

PROTECTED_HASHES = {
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/03_ARCHITECTURE_v1.0.0.md": "87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b",
    "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md": "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
    "docs/00_platform/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md": "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
    "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md": "a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639",
    "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20",
}


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _register_rows(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    rows: list[dict[str, str]] = []
    for index, line in enumerate(lines):
        if not re.match(r"^\| [A-D]-\d{2} \|", line):
            continue
        header_index = next(
            candidate
            for candidate in range(index - 1, -1, -1)
            if lines[candidate].startswith("| Key |")
        )
        headers = _cells(lines[header_index])
        values = _cells(line)
        if len(headers) != len(values):
            raise AssertionError(f"register row width mismatch: {line}")
        rows.append(dict(zip(headers, values)))
    return rows


def _queue_keys(text: str, heading: str, next_heading: str) -> set[str]:
    section = text[text.index(heading) : text.index(next_heading, text.index(heading))]
    return set(re.findall(r"\*\*([A-D]-\d{2}(?:-[AP])?)\*\*", section))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Stage3BClassificationIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.rows = _register_rows(cls.text)

    def test_register_counts_and_primary_classifications_reconcile(self):
        self.assertEqual(38, len(self.rows))
        self.assertEqual(38, len({row["Key"] for row in self.rows}))
        classifications = Counter(
            row["Primary classification"].strip("`") for row in self.rows
        )
        for classification, expected in EXPECTED_COUNTS.items():
            self.assertEqual(expected, classifications[classification], classification)
        for row in self.rows:
            self.assertIn(row["Primary classification"].strip("`"), CLASSIFICATIONS)
            for field in (
                "Proposition and requirement",
                "Proposal provenance",
                "Current evidence",
                "Gap analysis and rationale",
                "Routing, rejected mechanism, revisit and STOP",
            ):
                self.assertTrue(row[field], f"{row['Key']} missing {field}")

    def test_queues_cover_register_without_architecture_policy_duplication(self):
        queue_a = _queue_keys(
            self.text,
            "### Queue A: Already governed",
            "### Queue B: Architecture Grill",
        )
        queue_b = _queue_keys(
            self.text,
            "### Queue B: Architecture Grill",
            "### Queue C: Engineering-Policy Grill",
        )
        queue_c = _queue_keys(
            self.text,
            "### Queue C: Engineering-Policy Grill",
            "### Queue D: Deferred / rejected",
        )
        queue_d = _queue_keys(self.text, "### Queue D: Deferred / rejected", "## Contradiction")

        self.assertEqual(EXPECTED_QUEUES["Queue A: Already governed"], queue_a)
        self.assertEqual(EXPECTED_QUEUES["Queue B: Architecture Grill"], queue_b)
        self.assertEqual(EXPECTED_QUEUES["Queue C: Engineering-Policy Grill"], queue_c)
        self.assertEqual(EXPECTED_QUEUES["Queue D: Deferred / rejected"], queue_d)
        self.assertTrue(queue_b.isdisjoint(queue_c))
        self.assertTrue(queue_b.isdisjoint(queue_d))
        self.assertTrue(queue_c.isdisjoint(queue_d))

    def test_stage_3b_is_independent_and_creates_no_governed_identifiers_or_domains(self):
        self.assertIn("They are not Product-derived", self.text)
        self.assertIn(
            "does not answer an Architecture Grill, write an Engineering Standard, select packages, create a Domain, create a Feature Pack, or authorise implementation.",
            self.text,
        )
        for row in self.rows:
            self.assertIn("Independent", row["Proposal provenance"])
            self.assertNotIn("Product-derived", row["Proposal provenance"])
        self.assertIsNone(
            re.search(
                r"^#{1,6} (?:DEC|OQ|ARC|ARQ|CAP|FP|TB|VS|HH)-",
                self.text,
                re.MULTILINE,
            )
        )
        self.assertIn("**New Domains:** none created.", self.text)
        self.assertIn("**Governed identifiers:** none created.", self.text)

    def test_protected_authority_and_evidence_hashes_remain_unchanged(self):
        for relative_path, expected_hash in PROTECTED_HASHES.items():
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)


if __name__ == "__main__":
    unittest.main()
