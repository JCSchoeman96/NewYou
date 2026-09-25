import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS_PATH = ROOT / "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.2.2.md"

CAP_IDS = [f"CAP-{number:03d}" for number in range(1, 34)]
FP_IDS = [f"FP-{number:03d}" for number in range(1, 18)]
SYMBOLS = ("I", "R", "E", "S")
ALL_SYMBOLS = (*SYMBOLS, "—")
VIEW_LABELS = {
    "I": "Introduced",
    "R": "Later Reuse",
    "E": "Extensions",
    "S": "Specialisations",
}
ZERO_INTRODUCTION_CAPS = ["CAP-007", "CAP-032", "CAP-033"]
DEFERRED_LINEAGE = {
    "CAP-007": "— (Roadmap-deferred)",
    "CAP-032": "— (FUTURE-GATED / FEATURE-PACK-UNASSIGNED)",
    "CAP-033": "— (FUTURE-GATED / FEATURE-PACK-UNASSIGNED)",
}


def _section(text, start_heading, end_heading):
    start = text.index(start_heading)
    end = text.index(end_heading, start)
    return text[start:end]


def _cells(line):
    stripped = line.strip()
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def _table_rows(block, first_cell_pattern):
    pattern = re.compile(first_cell_pattern)
    rows = []
    for line in block.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = _cells(line)
        if cells and pattern.fullmatch(cells[0]):
            rows.append(cells)
    return rows


def _parse_ids(value):
    if value == "—" or value.startswith("— ") or not value:
        return set()
    return {item.strip() for item in value.split(",")}


def _parse_atlas():
    text = ATLAS_PATH.read_text(encoding="utf-8")

    matrix_block = _section(
        text,
        "### Main matrix",
        "### Feature Pack capability summary",
    )
    matrix_lines = [
        line for line in matrix_block.splitlines() if line.lstrip().startswith("|")
    ]
    matrix_header = _cells(matrix_lines[0])
    matrix_rows = _table_rows(matrix_block, r"CAP-\d{3}")
    matrix = {
        row[0]: dict(zip(matrix_header[2:], row[2:])) for row in matrix_rows
    }

    summary_block = _section(
        text,
        "### Feature Pack capability summary",
        "### Capability lineage view",
    )
    summary_rows = _table_rows(summary_block, r"FP-\d{3}")
    summary = {}
    for row in summary_rows:
        summary[row[0]] = {
            symbol: _parse_ids(value)
            for symbol, value in zip(SYMBOLS, row[1:])
        }

    lineage_block = _section(
        text,
        "### Capability lineage view",
        "### Exception / interpretation notes",
    )
    lineage_rows = _table_rows(lineage_block, r"CAP-\d{3}")
    lineage = {}
    lineage_raw = {}
    for row in lineage_rows:
        lineage_raw[row[0]] = row[1:]
        lineage[row[0]] = {
            symbol: _parse_ids(value)
            for symbol, value in zip(SYMBOLS, row[1:])
        }

    return text, matrix_header[2:], matrix, summary, lineage, lineage_raw


class DeliveryAtlasConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (
            cls.atlas_text,
            cls.feature_ids,
            cls.matrix,
            cls.summary,
            cls.lineage,
            cls.lineage_raw,
        ) = _parse_atlas()

    def test_matrix_structure_and_symbols(self):
        self.assertEqual(CAP_IDS, list(self.matrix))
        self.assertEqual(FP_IDS, self.feature_ids)
        self.assertEqual(33, len(self.matrix))
        self.assertEqual(17, len(self.feature_ids))

        cells = []
        for cap in CAP_IDS:
            self.assertEqual(17, len(self.matrix[cap]))
            cells.extend(self.matrix[cap][fp] for fp in FP_IDS)

        self.assertEqual(561, len(cells))
        self.assertTrue(
            all(cell in ALL_SYMBOLS for cell in cells),
            "matrix contains a symbol outside I/R/E/S/—",
        )

    def test_certified_matrix_counts(self):
        counts = Counter(
            self.matrix[cap][fp] for cap in CAP_IDS for fp in FP_IDS
        )
        self.assertEqual(
            {symbol: counts.get(symbol, 0) for symbol in ALL_SYMBOLS},
            {"I": 30, "R": 156, "E": 1, "S": 0, "—": 374},
        )
        self.assertEqual(187, sum(counts[symbol] for symbol in SYMBOLS))

    def test_feature_pack_summary_matches_matrix(self):
        self.assertEqual(FP_IDS, list(self.summary))
        for fp in FP_IDS:
            for symbol in ALL_SYMBOLS[:-1]:
                expected = {
                    cap
                    for cap in CAP_IDS
                    if self.matrix[cap][fp] == symbol
                }
                actual = self.summary[fp][symbol]
                self.assertEqual(
                    expected,
                    actual,
                    f"{fp}: matrix {symbol} IDs do not match Feature Pack summary",
                )

            listed = set().union(*(self.summary[fp][symbol] for symbol in SYMBOLS))
            expected_material = {
                cap
                for cap in CAP_IDS
                if self.matrix[cap][fp] != "—"
            }
            self.assertEqual(expected_material, listed, f"{fp}: summary has a non-matrix relationship")

    def test_capability_lineage_matches_matrix(self):
        self.assertEqual(CAP_IDS, list(self.lineage))
        for cap in CAP_IDS:
            for fp in FP_IDS:
                matrix_symbol = self.matrix[cap][fp]
                for symbol, label in VIEW_LABELS.items():
                    listed = fp in self.lineage[cap][symbol]
                    expected = matrix_symbol == symbol
                    if listed != expected:
                        presence = "contains" if listed else "omits"
                        self.fail(
                            f"{cap} / {fp}: matrix = {matrix_symbol}; "
                            f"lineage {label} {presence} {fp}"
                        )

            for symbol, label in VIEW_LABELS.items():
                expected = {
                    fp
                    for fp in FP_IDS
                    if self.matrix[cap][fp] == symbol
                }
                self.assertEqual(
                    expected,
                    self.lineage[cap][symbol],
                    f"{cap}: lineage {label} does not reverse the matrix",
                )

    def test_deferred_and_unassigned_caps(self):
        for cap, label in DEFERRED_LINEAGE.items():
            self.assertTrue(all(self.matrix[cap][fp] == "—" for fp in FP_IDS), cap)
            self.assertEqual(label, self.lineage_raw[cap][0], cap)
            self.assertEqual(
                {symbol: set() for symbol in SYMBOLS},
                self.lineage[cap],
                cap,
            )

    def test_introduction_ordering(self):
        zero_introduction_caps = []
        for cap in CAP_IDS:
            row = self.matrix[cap]
            introductions = [fp for fp in FP_IDS if row[fp] == "I"]
            if not introductions:
                zero_introduction_caps.append(cap)
                continue

            self.assertEqual(1, len(introductions), f"{cap}: introduction count")
            introduction_index = FP_IDS.index(introductions[0])
            for fp in FP_IDS:
                if row[fp] in {"R", "E", "S"}:
                    self.assertGreaterEqual(
                        FP_IDS.index(fp),
                        introduction_index,
                        f"{cap} / {fp}: material relationship precedes introduction",
                    )

        self.assertEqual(ZERO_INTRODUCTION_CAPS, zero_introduction_caps)

    def test_atlas07_has_five_classes_and_seven_seams(self):
        classes_block = _section(
            self.atlas_text,
            "## 8.4 Conceptual dependency classes",
            "## 8.5 Runtime interaction boundary",
        )
        classes = re.findall(r"^### `([^`]+)`$", classes_block, re.MULTILINE)
        self.assertEqual(
            [
                "AUTHORITATIVE_READ",
                "OWNER_CONTROLLED_CONSEQUENCE",
                "DERIVED_PROJECTION",
                "ORCHESTRATION_WITHOUT_OWNERSHIP",
                "EVIDENCE_OBSERVATION",
            ],
            classes,
        )
        self.assertNotIn("CONDITIONAL_GATED_SEAM", classes)

        seam_block = _section(
            self.atlas_text,
            "## 8.13 Permanent dependency invariant and exception register",
            "## 8.14 Provider evidence rule",
        )
        seam_rows = _table_rows(seam_block, r"(?!Seam$)(?!-+$).+")
        self.assertEqual(7, len(seam_rows))


if __name__ == "__main__":
    unittest.main()
