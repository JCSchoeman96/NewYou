from __future__ import annotations

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUCCESSOR = ROOT / "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md"
ARQ_HISTORY = ROOT / "docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md"
ANALYSIS_ARCHIVE = (
    ROOT
    / "docs/00_platform/archive/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md"
)
ANALYSIS_WORKING = (
    ROOT
    / "docs/00_platform/working/TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md"
)
MANIFEST = ROOT / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

ARQ_HEADING = re.compile(r"^#{1,6} (ARQ-[A-Z]+-\d{3}) — (.+)$", re.MULTILINE)
ARQ_TOKEN = re.compile(r"ARQ-[A-Z]+-\d{3}\b")

EXPECTED_NEW_ARQS = {
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
}

EXPECTED_CLUSTERS = {
    "Bounded Research and Feedback capability modes",
    "Research identity, uniqueness and anonymous-linkage truth",
    "Research response lifecycle, including anonymous withdrawal limits",
    "Research follow-up and monitoring-promise boundary",
    "Bounded voting modes and purpose classification",
    "Vote lifecycle and integrity-evidence states",
    "Tally, official result and reward boundary",
    "Voting finalisation and exception outcomes",
    "Bounded interactive-tool capability and administrator configuration",
    "Platform Member Reference assignment and identity meaning",
    "Platform Member Reference human-usable representation",
    "Historical Research and Voting truth after Account deletion",
}

EXPECTED_LINKED_THEMES = {
    "Research authority and downstream handoff",
    "Governed research instrument provenance and lifecycle",
    "Sensitive Research visibility, targeting and publication",
    "Research incentives and annotation provenance",
    "Voting participation identity and eligibility",
    "Voting visibility and integrity",
    "Voting integrity, status and anti-abuse",
    "Voting visibility, adjudication and safety",
    "Non-authoritative tool result and downstream handoff",
    "Tool persistence, version and history",
    "Tool health, safety, access and minimisation",
    "Tool explainability, configuration and correction",
    "Derived presentation and ownership boundary",
    "Platform Member Reference security and non-authority",
    "Platform Member Reference security and lifecycle",
    "Platform Member Reference lookup and beneficiary boundaries",
    "Cross-capability purpose and authority boundary",
    "Shared interaction and ownership boundary",
}


def _definitions(text: str) -> list[tuple[str, str]]:
    return ARQ_HEADING.findall(text)


def _table_rows(text: str, heading: str, end_heading: str) -> list[dict[str, str]]:
    section = text[text.index(heading) : text.index(end_heading, text.index(heading))]
    lines = [line for line in section.splitlines() if line.startswith("|")]
    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]
    rows = []
    for line in lines[2:]:
        rows.append(dict(zip(headers, [cell.strip() for cell in line.strip("|").split("|")])))
    return rows


class Stage3A2AmendmentIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.successor_text = SUCCESSOR.read_text(encoding="utf-8")
        cls.history_text = ARQ_HISTORY.read_text(encoding="utf-8")

    def test_v1_0_history_is_byte_preserved_and_no_longer_active(self):
        self.assertFalse(ANALYSIS_WORKING.exists())
        self.assertEqual(
            "cdf09ecced658635572a20e4f2feb04120b4f856e81762ef5af9ba179a11c40e",
            hashlib.sha256(ARQ_HISTORY.read_bytes()).hexdigest(),
        )

        marker = "# 1. Permanent Maintenance Rule"
        historical_body = self.history_text[self.history_text.index(marker) :].rstrip()
        successor_body = self.successor_text[self.successor_text.index(marker) :]
        self.assertTrue(
            successor_body.startswith(historical_body + "\n\n# 10. Post-freeze governed amendment"),
            "the v1.0.0 ARQ body must remain unchanged before the appended amendment",
        )

    def test_cumulative_identifiers_and_monotonic_allocations(self):
        historical_ids = [identifier for identifier, _ in _definitions(self.history_text)]
        successor_ids = [identifier for identifier, _ in _definitions(self.successor_text)]

        self.assertEqual(417, len(historical_ids))
        self.assertEqual(433, len(successor_ids))
        self.assertEqual(len(historical_ids), len(set(historical_ids)))
        self.assertEqual(len(successor_ids), len(set(successor_ids)))
        self.assertTrue(set(historical_ids) <= set(successor_ids))
        self.assertEqual(EXPECTED_NEW_ARQS, set(successor_ids) - set(historical_ids))

        expected_ranges = {
            "ARQ-PERF": (1, 166),
            "ARQ-AN": (1, 216),
            "ARQ-PAY": (1, 1),
            "ARQ-SYS": (1, 10),
            "ARQ-IAM": (1, 13),
            "ARQ-STATE": (1, 13),
            "ARQ-ASYNC": (1, 4),
            "ARQ-CONTENT": (1, 6),
            "ARQ-SEC": (1, 2),
            "ARQ-OPS": (1, 2),
        }
        for family, (start, end) in expected_ranges.items():
            actual = sorted(
                int(identifier.rsplit("-", 1)[1])
                for identifier in successor_ids
                if identifier.startswith(f"{family}-")
            )
            self.assertEqual(list(range(start, end + 1)), actual, family)

    def test_new_arqs_have_product_sources_and_exclude_stage_3b_inputs(self):
        matches = list(ARQ_HEADING.finditer(self.successor_text))
        blocks = {}
        amendment_end = self.successor_text.index("## 10.5 Identifier allocation proof")
        for index, match in enumerate(matches):
            identifier = match.group(1)
            later_matches = [item.start() for item in matches[index + 1 :] if item.start() < amendment_end]
            end = later_matches[0] if later_matches else amendment_end
            blocks[identifier] = self.successor_text[match.start() : end]

        for identifier in EXPECTED_NEW_ARQS:
            block = blocks[identifier]
            self.assertIn("**Exact Product Law source:**", block)
            self.assertRegex(block, r"§§?21[M-NO-PQ]")
            self.assertRegex(block, r"DEC-(294|295|296|297|298)")
            self.assertIn("**Status:** ACCEPTED", block)
            self.assertIn("**Architecture status:** ARQ_LOCKED / ARC_PENDING", block)
            for excluded in ("Errors & Diagnostics", "Observability refinement", "Native Compute", "Rustler", "Engineering Quality"):
                self.assertNotIn(excluded, block)

    def test_member_reference_arqs_preserve_qualified_product_meaning(self):
        iam_011_start = self.successor_text.index("### ARQ-IAM-011")
        iam_012_start = self.successor_text.index("### ARQ-IAM-012", iam_011_start)
        iam_011 = self.successor_text[iam_011_start:iam_012_start]

        for reason in ("security", "privacy", "integrity", "reconciliation", "equivalent operational-correctness"):
            self.assertIn(reason, iam_011)
        self.assertIn("legitimately reactivated", iam_011)
        self.assertIn("new Platform Member Reference", iam_011)
        self.assertIn("old reference remains permanently non-reusable", iam_011)
        self.assertIn("routine vanity changes are not a Product requirement", iam_011)

        iam_013_start = self.successor_text.index("### ARQ-IAM-013")
        iam_013_end = self.successor_text.index("### ARQ-STATE-008", iam_013_start)
        iam_013 = self.successor_text[iam_013_start:iam_013_end]

        self.assertIn(
            "not obviously sequential in a way that unnecessarily exposes Account growth or materially simplifies enumeration",
            iam_013,
        )
        self.assertIn("compatible with an error-detection/check mechanism", iam_013)
        self.assertNotRegex(iam_013, r"must be[^.]*error-detectable")
        self.assertIn("exact representation", iam_013)
        self.assertIn("`VG`", iam_013)

    def test_all_descriptive_clusters_and_linked_themes_are_mapped(self):
        cluster_rows = _table_rows(
            self.successor_text,
            "### 12 new descriptive cluster coverage",
            "### 18 linked additive theme coverage",
        )
        linked_rows = _table_rows(
            self.successor_text,
            "### 18 linked additive theme coverage",
            "### Product-source coverage check",
        )
        self.assertEqual(12, len(cluster_rows))
        self.assertEqual(18, len(linked_rows))
        self.assertEqual(
            EXPECTED_CLUSTERS,
            {row["Stage 3A.1 descriptive cluster"] for row in cluster_rows},
        )
        self.assertEqual(
            EXPECTED_LINKED_THEMES,
            {row["Stage 3A.1 linked additive theme"] for row in linked_rows},
        )
        all_ids = set(identifier for identifier, _ in _definitions(self.successor_text))
        for row in [*cluster_rows, *linked_rows]:
            destinations = set(ARQ_TOKEN.findall(row["Resulting governed ARQ(s)"]))
            self.assertTrue(destinations, row)
            self.assertTrue(destinations <= all_ids, row)

    def test_source_propagation_matches_approved_exact_targets(self):
        rows = _table_rows(
            self.successor_text,
            "### Valid source-propagation mappings",
            "### Source-propagation exclusions and related evidence only",
        )
        self.assertEqual(17, len(rows))
        self.assertTrue(all(row["Date"] == "2026-09-03" for row in rows))
        self.assertTrue(
            all(
                row["Historical wording/status"]
                == "Unchanged; historical text and status remain intact."
                for row in rows
            )
        )
        self.assertTrue(
            all("TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md" in row["Stage 3A.1 provenance reference"] for row in rows)
        )

        expected = Counter()

        def add(evidence: str, targets: list[str], source: str) -> None:
            for target in targets:
                expected[(evidence, f"`{target}`", source)] += 1

        add(
            "Vote limits and retried/concurrent submissions",
            ["ARQ-PERF-025", "ARQ-PERF-026", "ARQ-PERF-027", "ARQ-PERF-041"],
            "`00_PLATFORM_v1.3.0.md §21N.3`; `DEC-295`",
        )
        add(
            "Proportionate voting anti-abuse controls",
            ["ARQ-SEC-001"],
            "`00_PLATFORM_v1.3.0.md §21N.3`; `DEC-295`",
        )
        add(
            "Governed research publication and lifecycle",
            ["ARQ-STATE-002"],
            "`00_PLATFORM_v1.3.0.md §21M.4`; `DEC-294`",
        )
        add(
            "Material calculation changes create governed versions",
            ["ARQ-STATE-002"],
            "`00_PLATFORM_v1.3.0.md §21O.3`; `DEC-296`",
        )
        add(
            "Persisted interactive-result version provenance",
            ["ARQ-STATE-002"],
            "`00_PLATFORM_v1.3.0.md §21O.3`; `DEC-296`",
        )
        add(
            "Interactive correction and recalculation preserve history",
            ["ARQ-STATE-002"],
            "`00_PLATFORM_v1.3.0.md §21O.5`; `DEC-296`",
        )
        add(
            "Dashboards and visualisations remain derived",
            ["ARQ-AN-001", "ARQ-AN-022", "ARQ-AN-127", "ARQ-AN-161"],
            "`00_PLATFORM_v1.3.0.md §21O.5`; `DEC-296`",
        )
        add(
            "Analytics, dashboards, leaderboards and reports remain derived",
            ["ARQ-AN-001", "ARQ-AN-022", "ARQ-AN-127", "ARQ-AN-161"],
            "`00_PLATFORM_v1.3.0.md §21Q.8`; `DEC-298`",
        )
        actual = Counter(
            (row["Stage 3A.1 evidence row"], row["Existing ARQ"], row["New Product source"])
            for row in rows
        )
        self.assertEqual(expected, actual)
        self.assertEqual(
            {
                "ARQ-PERF-025",
                "ARQ-PERF-026",
                "ARQ-PERF-027",
                "ARQ-PERF-041",
                "ARQ-SEC-001",
                "ARQ-STATE-002",
                "ARQ-AN-001",
                "ARQ-AN-022",
                "ARQ-AN-127",
                "ARQ-AN-161",
            },
            {row["Existing ARQ"].strip("`") for row in rows},
        )

        forbidden_by_evidence = {
            "Vote limits and retried/concurrent submissions": {"ARQ-PERF-032", "ARQ-PERF-037"},
            "Proportionate voting anti-abuse controls": {"ARQ-PERF-025", "ARQ-PERF-049"},
            "Material calculation changes create governed versions": {"ARQ-AN-014", "ARQ-AN-141"},
            "Persisted interactive-result version provenance": {
                "ARQ-AN-014",
                "ARQ-AN-141",
                "ARQ-CONTENT-003",
            },
            "Dashboards and visualisations remain derived": {"ARQ-PERF-114"},
            "Analytics, dashboards, leaderboards and reports remain derived": {"ARQ-AN-180"},
            "Interactive correction and recalculation preserve history": {
                "ARQ-AN-015",
                "ARQ-AN-142",
                "ARQ-AN-144",
                "ARQ-PERF-033",
            },
            "Governed research publication and lifecycle": {"ARQ-CONTENT-003", "ARQ-ASYNC-002"},
        }
        for row in rows:
            self.assertNotIn(
                row["Existing ARQ"].strip("`"),
                forbidden_by_evidence[row["Stage 3A.1 evidence row"]],
            )

    def test_product_sources_and_closure_arithmetic_reconcile(self):
        rows = _table_rows(
            self.successor_text,
            "### Product-source coverage check — §§21M–21Q / DEC-294–DEC-298",
            "## 10.4 New governed ARQs",
        )
        self.assertEqual(5, len(rows))
        self.assertEqual(
            {"DEC-294", "DEC-295", "DEC-296", "DEC-297", "DEC-298"},
            {row["Decision"].strip("`") for row in rows},
        )
        self.assertTrue(all(row["Result"] == "COVERED" for row in rows))
        self.assertIn("The complete Product-obligation arithmetic is `5 + 44 + 15 + 2 + 0 = 66`", self.successor_text)
        self.assertIn("the ARQ arithmetic is `417 + 16 = 433`", self.successor_text)
        self.assertIn("| Stage 3A.1 `NO_ARQ_REQUIRED` rows | 2, explicitly listed in §10.6 |", self.successor_text)

    def test_manifest_routes_current_and_historical_artifacts(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in manifest[section]
        }
        historical = {entry["document_id"]: entry for entry in manifest["historical_documents"]}

        self.assertEqual(
            "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md",
            current["ARCHITECTURE_REQUIREMENTS"]["repository_path"],
        )
        self.assertEqual("1.1.0", current["ARCHITECTURE_REQUIREMENTS"]["semver"])
        self.assertEqual("1.0.0", current["ARCHITECTURE_REQUIREMENTS"]["superseded_version"])
        self.assertEqual("1.2.45", current["OPEN_WORK"]["semver"])
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.45.md", current["OPEN_WORK"]["repository_path"])
        self.assertEqual(
            hashlib.sha256((ROOT / current["OPEN_WORK"]["repository_path"]).read_bytes()).hexdigest(),
            current["OPEN_WORK"]["sha256"],
        )
        self.assertIn("ARCHITECTURE_REQUIREMENTS_V1_0_0", historical)
        self.assertIn("TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS", historical)
        self.assertEqual("historical", historical["ARCHITECTURE_REQUIREMENTS_V1_0_0"]["lifecycle"])
        self.assertEqual("historical", historical["TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS"]["lifecycle"])


if __name__ == "__main__":
    unittest.main()
