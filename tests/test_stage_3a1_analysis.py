from __future__ import annotations

import re
import unittest
from collections import Counter
from pathlib import Path


ARTIFACT = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "00_platform"
    / "archive"
    / "TARGETED_PRODUCT_AMENDMENT_AR000_DELTA_ANALYSIS_WORKING_v0.1.0.md"
)

CAPABILITY_HEADINGS = (
    "Research and Feedback",
    "Voting, Balloting and Competitions",
    "Interactive Tools, Calculators and Decision Aids",
    "Platform Member Reference",
    "Cross-capability interaction rules",
)

CLASSIFICATIONS = (
    "EXISTING_ARQ_SUFFICIENT",
    "EXISTING_ARQ_SOURCE_REFRESH_REQUIRED",
    "EXISTING_ARQ_AMENDMENT_REQUIRED",
    "NEW_ARQ_REQUIRED",
    "NO_ARQ_REQUIRED",
    "UPSTREAM_PRODUCT_CONTRADICTION",
)

EXPECTED_CLASSIFICATIONS = {
    "EXISTING_ARQ_SUFFICIENT": 0,
    "EXISTING_ARQ_SOURCE_REFRESH_REQUIRED": 5,
    "EXISTING_ARQ_AMENDMENT_REQUIRED": 44,
    "NEW_ARQ_REQUIRED": 15,
    "NO_ARQ_REQUIRED": 2,
    "UPSTREAM_PRODUCT_CONTRADICTION": 0,
}

EXPECTED_CAPABILITY_COUNTS = {
    "Research and Feedback": 15,
    "Voting, Balloting and Competitions": 17,
    "Interactive Tools, Calculators and Decision Aids": 14,
    "Platform Member Reference": 10,
    "Cross-capability interaction rules": 10,
}

EXPECTED_NEW_CLUSTERS = (
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
)

TREATMENT_PREFIXES = (
    "AMEND_EXACT_ARQ: ",
    "PRESERVE_EXISTING_ARQS_AND_ADD_LINKED_COVERAGE",
    "CONSOLIDATE_WITH_CANDIDATE_CLUSTER: ",
    "SOURCE_REFRESH_PLUS_ADDITIVE_COVERAGE",
)


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _evidence_rows(text: str) -> tuple[list[dict[str, str]], dict[str, int]]:
    lines = text.splitlines()
    rows: list[dict[str, str]] = []
    header_widths: dict[str, int] = {}

    for heading in CAPABILITY_HEADINGS:
        heading_index = lines.index(f"### {heading}")
        table_index = next(
            index
            for index in range(heading_index + 1, len(lines))
            if lines[index].startswith("| Product source |")
        )
        headers = _cells(lines[table_index])
        header_widths[heading] = len(headers)
        for line in lines[table_index + 2 :]:
            if not line.startswith("|"):
                break
            if line.startswith("|---"):
                continue
            fields = _cells(line)
            if len(fields) != len(headers):
                raise AssertionError(
                    f"{heading}: expected {len(headers)} cells, got {len(fields)}: {line}"
                )
            row = {
                "capability": heading,
                **dict(zip(headers, fields)),
            }
            row["Primary classification"] = row["Primary classification"].strip("`")
            rows.append(row)

    return rows, header_widths


def _table_rows_in_section(
    text: str,
    heading: str,
    next_heading: str,
) -> list[dict[str, str]]:
    section = text[text.index(heading) : text.index(next_heading)]
    lines = section.splitlines()
    table_index = next(index for index, line in enumerate(lines) if line.startswith("| "))
    headers = _cells(lines[table_index])
    rows = []
    for line in lines[table_index + 2 :]:
        if not line.startswith("|"):
            break
        if line.startswith("|---"):
            continue
        fields = _cells(line)
        if len(fields) != len(headers):
            raise AssertionError(
                f"{heading}: expected {len(headers)} cells, got {len(fields)}: {line}"
            )
        rows.append(dict(zip(headers, fields)))
    return rows


class Stage3A1AnalysisIntegrityTests(unittest.TestCase):
    def test_register_counts_and_treatments_reconcile(self):
        text = ARTIFACT.read_text(encoding="utf-8")
        rows, header_widths = _evidence_rows(text)

        self.assertEqual(
            {heading: 10 for heading in CAPABILITY_HEADINGS},
            header_widths,
        )
        self.assertEqual(66, len(rows))
        actual_classifications = Counter(row["Primary classification"] for row in rows)
        for classification, expected in EXPECTED_CLASSIFICATIONS.items():
            self.assertEqual(expected, actual_classifications[classification])
        self.assertEqual(
            EXPECTED_CAPABILITY_COUNTS,
            Counter(row["capability"] for row in rows),
        )

        amendment_rows = [
            row
            for row in rows
            if row["Primary classification"] == "EXISTING_ARQ_AMENDMENT_REQUIRED"
        ]
        for row in amendment_rows:
            treatment = row["Stage 3A.2 proposed treatment"].strip("`")
            matching_treatments = [
                prefix
                for prefix in TREATMENT_PREFIXES
                if treatment.startswith(prefix)
            ]
            self.assertEqual(
                1,
                len(matching_treatments),
                msg=row["Exact Product obligation"],
            )

    def test_decision_coverage_matches_register(self):
        text = ARTIFACT.read_text(encoding="utf-8")
        rows, _ = _evidence_rows(text)
        actual = Counter()
        for row in rows:
            decision = re.search(r"DEC-(294|295|296|297|298)", row["Product source"])
            self.assertIsNotNone(decision, msg=row["Product source"])
            actual[decision.group(1)] += 1

        lines = text.splitlines()
        start = lines.index("### Decision coverage")
        summaries: dict[str, int] = {}
        for line in lines[start + 3 :]:
            if not line.startswith("|"):
                break
            fields = _cells(line)
            if not fields or not fields[0].startswith("`DEC-"):
                continue
            decision = fields[0].strip("`").removeprefix("DEC-")
            source_count = re.search(r"(\d+) source refresh(?:es)?", fields[3])
            amendment_count = re.search(r"(\d+) amendments?", fields[3])
            new_count = re.search(r"(\d+) new row(?:s)?", fields[3])
            product_only_count = re.search(
                r"(\d+) Product(?:/implementation)?-only row",
                fields[3],
            )
            self.assertIsNotNone(amendment_count, msg=fields[3])
            self.assertIsNotNone(new_count, msg=fields[3])
            summaries[decision] = sum(
                int(match.group(1))
                for match in (
                    source_count,
                    amendment_count,
                    new_count,
                    product_only_count,
                )
                if match is not None
            )

        self.assertEqual(
            {decision: actual[decision] for decision in ("294", "295", "296", "297", "298")},
            summaries,
        )
        self.assertEqual(66, sum(summaries.values()))

    def test_source_provenance_targets_match_exact_product_semantics(self):
        text = ARTIFACT.read_text(encoding="utf-8")
        source_rows = _table_rows_in_section(
            text,
            "### Source propagation only",
            "### Existing ARQs genuinely requiring semantic amendment",
        )
        source_targets = {
            row["Evidence row"]: set(re.findall(r"ARQ-[A-Z]+-\d{3}\b", row["Exact existing ARQ(s)"]))
            for row in source_rows
        }
        self.assertEqual(
            {
                "Vote limits and retried/concurrent submissions": {
                    "ARQ-PERF-025",
                    "ARQ-PERF-026",
                    "ARQ-PERF-027",
                    "ARQ-PERF-041",
                },
                "Proportionate voting anti-abuse controls": {"ARQ-SEC-001"},
                "Material calculation changes create governed versions": {"ARQ-STATE-002"},
                "Dashboards and visualisations remain derived": {
                    "ARQ-AN-001",
                    "ARQ-AN-022",
                    "ARQ-AN-127",
                    "ARQ-AN-161",
                },
                "Analytics, dashboards, leaderboards and reports remain derived": {
                    "ARQ-AN-001",
                    "ARQ-AN-022",
                    "ARQ-AN-127",
                    "ARQ-AN-161",
                },
            },
            source_targets,
        )

        additive_source_rows = _table_rows_in_section(
            text,
            "### Valid source propagation attached to reclassified additive rows",
            "### Existing ARQs preserved unchanged as related evidence",
        )
        self.assertEqual(
            {
                "Governed research publication and lifecycle (reclassified)": {
                    "ARQ-STATE-002"
                },
                "Persisted interactive-result version provenance (reclassified)": {
                    "ARQ-STATE-002"
                },
                "Interactive correction and recalculation preserve history (reclassified)": {
                    "ARQ-STATE-002"
                },
            },
            {
                row["Evidence row"]: set(
                    re.findall(r"ARQ-[A-Z]+-\d{3}\b", row["Exact existing ARQ(s)"])
                )
                for row in additive_source_rows
            },
        )

        source_scope = text[
            text.index("### Source propagation only") : text.index(
                "### Existing ARQs preserved unchanged as related evidence"
            )
        ]
        for forbidden in (
            "ARQ-ASYNC-002",
            "ARQ-CONTENT-003",
            "ARQ-PERF-032",
            "ARQ-PERF-037",
            "ARQ-PERF-049",
            "ARQ-AN-014",
            "ARQ-AN-141",
            "ARQ-PERF-114",
            "ARQ-AN-015",
            "ARQ-AN-142",
            "ARQ-AN-144",
            "ARQ-PERF-033",
            "ARQ-AN-180",
        ):
            self.assertNotIn(forbidden, source_scope)

    def test_all_candidate_clusters_reach_stage_3a2_handoff(self):
        text = ARTIFACT.read_text(encoding="utf-8")
        rows, _ = _evidence_rows(text)
        handoff = text[text.index("## Consolidated Stage 3A.2 treatment register") :]

        clusters = {
            row["Candidate cluster, if needed"]
            for row in rows
            if row["Candidate cluster, if needed"] not in {"Not applicable", "—", ""}
        }
        for cluster in clusters:
            self.assertIn(cluster, handoff)

        for cluster in EXPECTED_NEW_CLUSTERS:
            self.assertIn(cluster, text)
            self.assertIn(cluster, handoff)

    def test_every_cited_arq_token_is_backtick_delimited_and_well_formed(self):
        text = ARTIFACT.read_text(encoding="utf-8")
        token_pattern = re.compile(r"ARQ-[A-Z]+-\d{3}\b")
        for occurrence in re.finditer(r"ARQ-", text):
            if text.startswith("ARQ-000", occurrence.start()):
                continue
            token = token_pattern.match(text, occurrence.start())
            self.assertIsNotNone(token, msg=text[occurrence.start() : occurrence.start() + 30])
            assert token is not None
            self.assertEqual("`", text[token.start() - 1], msg=token.group())
            self.assertEqual("`", text[token.end()], msg=token.group())


if __name__ == "__main__":
    unittest.main()
