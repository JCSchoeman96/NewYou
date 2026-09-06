from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
LAW = DOCS / "reference" / "ARCHITECTURE_LAW_WORKING_v0.36.0.md"
LAW_PREDECESSOR = DOCS / "archive" / "ARCHITECTURE_LAW_WORKING_v0.35.0.md"
SYNTHESIS = DOCS / "03_ARCHITECTURE_v1.1.0.md"
SYNTHESIS_PREDECESSOR = DOCS / "archive" / "03_ARCHITECTURE_v1.0.0.md"
FLOW = DOCS / "reference" / "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md"
FLOW_PREDECESSOR = DOCS / "archive" / "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md"
OPEN_WORK = DOCS / "archive" / "02_OPEN_WORK_v1.2.36.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.35.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
STAGE_3B = DOCS / "working" / "TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md"

PRODUCT_DERIVED_ARQS = {
    "ARQ-SYS-007", "ARQ-SYS-008", "ARQ-SYS-009", "ARQ-SYS-010",
    "ARQ-IAM-009", "ARQ-IAM-010", "ARQ-IAM-011", "ARQ-IAM-012", "ARQ-IAM-013",
    "ARQ-STATE-008", "ARQ-STATE-009", "ARQ-STATE-010", "ARQ-STATE-011",
    "ARQ-STATE-012", "ARQ-STATE-013", "ARQ-ASYNC-004",
}

NEW_ARC_ARQS = {
    "ARC-328": {"ARQ-SYS-007", "ARQ-SYS-008", "ARQ-SYS-009"},
    "ARC-329": {"ARQ-IAM-009"},
    "ARC-330": {"ARQ-IAM-011", "ARQ-IAM-012"},
    "ARC-331": {"ARQ-STATE-008", "ARQ-STATE-013"},
    "ARC-332": {"ARQ-STATE-009", "ARQ-STATE-010", "ARQ-STATE-011"},
}

CLOSURE_EXPECTATIONS = {
    "ARQ-SYS-007": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-328", "NEW ARC"),
    "ARQ-SYS-008": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-328", "NEW ARC"),
    "ARQ-SYS-009": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-328", "NEW ARC"),
    "ARQ-SYS-010": ("EXISTING_ARCHITECTURE_SUFFICIENT", "ARC-046, ARC-047, ARC-049, ARC-055, ARC-061, ARC-152, ARC-168, ARC-231", "EXISTING ARC ONLY"),
    "ARQ-IAM-009": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-329", "NEW ARC"),
    "ARQ-IAM-010": ("EXISTING_ARCHITECTURE_SUFFICIENT", "ARC-038, ARC-039, ARC-042, ARC-118, ARC-123, ARC-126, ARC-203", "EXISTING ARC ONLY"),
    "ARQ-IAM-011": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-330", "NEW ARC"),
    "ARQ-IAM-012": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-330", "NEW ARC"),
    "ARQ-IAM-013": ("DOWNSTREAM_DETAIL_ONLY", "ARC-098, ARC-330", "DOWNSTREAM-ONLY REPRESENTATION DETAIL"),
    "ARQ-STATE-008": ("EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION", "ARC-065, ARC-191, ARC-192, ARC-197, ARC-331", "EXISTING + NEW ARC"),
    "ARQ-STATE-009": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-061, ARC-068, ARC-124, ARC-144, ARC-332", "EXISTING + NEW ARC"),
    "ARQ-STATE-010": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-046, ARC-061, ARC-168, ARC-231, ARC-332", "EXISTING + NEW ARC"),
    "ARQ-STATE-011": ("NEW_ARCHITECTURE_DECISION_REQUIRED", "ARC-041, ARC-124, ARC-129, ARC-130, ARC-332", "EXISTING + NEW ARC"),
    "ARQ-STATE-012": ("EXISTING_ARCHITECTURE_SUFFICIENT", "ARC-066, ARC-233, ARC-237, ARC-238, ARC-240, ARC-241, ARC-242", "EXISTING ARC ONLY"),
    "ARQ-STATE-013": ("EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION", "ARC-044, ARC-046, ARC-061, ARC-065, ARC-331", "EXISTING + NEW ARC"),
    "ARQ-ASYNC-004": ("EXISTING_ARCHITECTURE_SUFFICIENT", "ARC-146, ARC-155, ARC-170, ARC-171", "EXISTING ARC ONLY"),
}

TARGETED_FLOWS = {
    "FLOW-01": "ARC-329`, `ARC-330",
    "FLOW-02": "ARC-330`, `ARC-332",
    "FLOW-03": "ARC-331",
    "FLOW-06": "ARC-332",
    "FLOW-08": "ARC-329`, `ARC-330`, `ARC-331`, `ARC-332",
    "FLOW-10": "ARC-330",
    "FLOW-11": "ARC-331`, `ARC-332",
}

PROTECTED_HASHES = {
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md": "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md": "971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91",
    "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
    "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.1.0.md": "8cb7769018c21b09c91208c5991b1b9bca09141c5fa0ef74cd577946d76377f1",
    "docs/00_platform/working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md": "c986c11811100b72ba083f9a6ad057b33abffbd4800159f6de502b3097cc94f4",
    "docs/00_platform/working/TARGETED_ARCHITECTURE_GRILL_WORKING_v0.1.0.md": "d25b6b7232f05859f3b19d8cf48f4a2648095830b27dcbca3676209a2a1af5c8",
    "docs/00_platform/working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md": "27bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017",
    ".github/workflows/foundation-integrity.yml": "2c718457456c71ad8d7fc416a6e0a646792271b9341e4a14fedda6ddb02bcdb8",
}

REQUIRED_SUCCESSOR_PATHS = (
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.36.md",
    "docs/00_platform/03_ARCHITECTURE_v1.1.0.md",
    "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md",
    "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.35.md",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.0.0.md",
    "docs/00_platform/archive/ARCHITECTURE_LAW_WORKING_v0.35.0.md",
    "docs/00_platform/archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md",
)

PROHIBITED_PRESENT_PATHS = (
    "mix.exs",
    "docs/00_platform/ENGINEERING_STANDARDS_v1.0.0.md",
    "docs/00_platform/reference/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    "docs/00_platform/working/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(text: str, heading_pattern: str, next_pattern: str) -> str:
    start_match = re.search(heading_pattern, text, re.MULTILINE)
    if start_match is None:
        raise AssertionError(f"missing heading: {heading_pattern}")
    end_match = re.search(next_pattern, text[start_match.end() :], re.MULTILINE)
    end = start_match.end() + end_match.start() if end_match else len(text)
    return text[start_match.start() : end].rstrip()


def _arc_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## (ARC-\d{3}) —", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        search_region = text[match.end() :]
        boundary_offsets: list[int] = []
        if index + 1 < len(matches):
            boundary_offsets.append(matches[index + 1].start() - match.end())
        other_heading = re.search(r"^#{1,2} (?!ARC-\d{3} —)", search_region, re.MULTILINE)
        if other_heading is not None:
            boundary_offsets.append(other_heading.start())
        end = match.end() + (min(boundary_offsets) if boundary_offsets else len(search_region))
        sections[match.group(1)] = text[match.start() : end].rstrip()
    return sections


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


class ArchitectureAmendmentIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.law = LAW.read_text(encoding="utf-8")
        cls.law_predecessor = LAW_PREDECESSOR.read_text(encoding="utf-8")
        cls.synthesis = SYNTHESIS.read_text(encoding="utf-8")
        cls.flow = FLOW.read_text(encoding="utf-8")
        cls.flow_predecessor = FLOW_PREDECESSOR.read_text(encoding="utf-8")
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = (DOCS / "README.md").read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_predecessors_are_immutable_and_successors_use_explicit_semver(self):
        self.assertEqual("a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639", _sha256(LAW_PREDECESSOR))
        self.assertEqual("87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b", _sha256(SYNTHESIS_PREDECESSOR))
        self.assertEqual("f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20", _sha256(FLOW_PREDECESSOR))
        self.assertEqual("772ec84d590e73b0963e798ac5ea30fa77bbf98d5ec3685bde69474367c70ff1", _sha256(OPEN_WORK_PREDECESSOR))
        self.assertIn("v0.35.0 → v0.36.0", self.law)
        self.assertIn("v0.2.0 → v0.3.0", self.flow)
        self.assertIn("v1.2.35 → v1.2.36", self.open_work)
        self.assertIn("Predecessor frozen version", self.synthesis)

    def test_arc_history_is_unchanged_and_new_range_is_contiguous(self):
        predecessor = _arc_sections(self.law_predecessor)
        successor = _arc_sections(self.law)
        self.assertEqual(list(range(1, 328)), [int(key[4:]) for key in predecessor])
        self.assertEqual(list(range(1, 333)), [int(key[4:]) for key in successor])
        for arc_id in predecessor:
            self.assertEqual(predecessor[arc_id], successor[arc_id], arc_id)
        self.assertEqual([f"ARC-{number:03d}" for number in range(328, 333)], list(successor)[-5:])
        self.assertEqual(332, len(set(successor)))

    def test_new_arc_records_have_valid_sources_and_map_to_all_five_questions(self):
        predecessor = _arc_sections(self.law_predecessor)
        sections = _arc_sections(self.law)
        self.assertEqual(set(NEW_ARC_ARQS), set(sections) - set(predecessor))
        for arc_id, expected_arqs in NEW_ARC_ARQS.items():
            section = sections[arc_id]
            for required_field in ("Decision source", "Status", "Source ARQs", "Decision", "Rationale", "Rules", "Failure behaviour", "Security/privacy", "Performance/scaling", "Enforcement/downstream", "Amendment/interaction effect"):
                self.assertIn(f"- **{required_field}:**", section, arc_id)
            source_line = re.search(r"- \*\*Source ARQs:\*\* (.+)", section)
            self.assertIsNotNone(source_line, arc_id)
            actual_arqs = set(re.findall(r"ARQ-[A-Z]+-\d{3}", source_line.group(1)))
            self.assertEqual(expected_arqs, actual_arqs, arc_id)
            self.assertTrue(actual_arqs <= PRODUCT_DERIVED_ARQS)
        for question in ("Q1", "Q2", "Q3", "Q4", "Q5"):
            self.assertRegex(self.law, rf"\| `ARC-3\d{{2}}` \| {question} \|")

    def test_closure_matrix_covers_exactly_the_sixteen_product_arqs(self):
        rows = _table_rows(self.law, "## 6.2 Sixteen-ARQ Architecture closure matrix", "## 6.3 Existing-Architecture closure record")
        self.assertEqual(16, len(rows))
        by_arq = {row["ARQ"].strip("`"): row for row in rows}
        self.assertEqual(PRODUCT_DERIVED_ARQS, set(by_arq))
        for arq, (disposition, arcs, basis) in CLOSURE_EXPECTATIONS.items():
            row = by_arq[arq]
            self.assertEqual(disposition, row["Stage 4A disposition"].strip("`"), arq)
            self.assertEqual(arcs, row["Governing ARC(s)"].replace("`", ""), arq)
            self.assertEqual(basis, row["Closure basis"].replace("`", ""), arq)
            self.assertTrue(row["Short closure rationale"])
            self.assertTrue(row["Downstream gate/detail"])
            self.assertTrue(row["Targeted flow impact"])
        self.assertIn("No AR-000 amendment is made", self.law)

    def test_existing_only_and_downstream_only_closures_remain_explicit(self):
        matrix = self.law[self.law.index("## 6.2") : self.law.index("## 6.3")]
        for arq in ("ARQ-SYS-010", "ARQ-IAM-010", "ARQ-STATE-012", "ARQ-ASYNC-004"):
            row = next(line for line in matrix.splitlines() if line.startswith("|") and f"`{arq}`" in line)
            self.assertIn("EXISTING ARC ONLY", row)
        pmr_row = next(line for line in matrix.splitlines() if line.startswith("|") and "`ARQ-IAM-013`" in line)
        self.assertIn("DOWNSTREAM-ONLY REPRESENTATION DETAIL", pmr_row)
        pmr_arc = _arc_sections(self.law)["ARC-330"]
        self.assertIn("`ARQ-IAM-013` constrains", pmr_arc)
        self.assertIn("exact representation remains unfrozen", pmr_arc)
        self.assertNotIn("Source ARQs:** `ARQ-IAM-013`", pmr_arc)
        for representation in ("prefix", "alphabet", "grouping", "length", "check", "generator", "database representation"):
            self.assertIn(representation, pmr_arc)
        self.assertIn("VG", pmr_arc)

    def test_stage_3b_and_stage_4b_do_not_become_arc_sources(self):
        supplement = self.law[self.law.index("# 6. Architecture amendment supplement") :]
        for key in ("A-08", "B-09", "D-02", "D-03", "D-04", "D-05", "D-07"):
            self.assertNotIn(f"`{key}`", supplement)
        self.assertNotIn("TARGETED_ENGINEERING_POLICY_GRILL", supplement)
        stage_3b = STAGE_3B.read_text(encoding="utf-8")
        queue_b = stage_3b[stage_3b.index("### Queue B: Architecture Grill") : stage_3b.index("### Queue C: Engineering-Policy Grill")]
        self.assertEqual([], re.findall(r"\*\*([A-D]-\d{2}(?:-[AP])?)\*\*", queue_b))
        for arc_id in NEW_ARC_ARQS:
            section = _arc_sections(self.law)[arc_id]
            self.assertNotIn("Engineering-Policy", section)
            self.assertNotIn("Engineering Standards", section)

    def test_product_identity_and_domain_guardrails_remain_unassigned(self):
        supplement = self.law[self.law.index("# 6. Architecture amendment supplement") :]
        for forbidden in ("Research Domain", "Voting Domain", "Interactive Tools Domain", "Engagement Domain", "Interactive Evidence Domain", "Platform Member Reference Domain", "Domain owner:"):
            self.assertNotIn(forbidden, supplement)
        self.assertIn("No new Domain, Domain owner", supplement)
        self.assertIn("Genuine anonymous", supplement)
        self.assertIn("one-human-one-vote", supplement)
        self.assertIn("not authority", supplement)
        self.assertIn("not a bearer credential", supplement)
        self.assertIn("no new mechanism is required", supplement.lower())

    def test_targeted_flow_review_covers_exactly_the_required_set(self):
        rows = _table_rows(self.flow, "## 2.1 Targeted Architecture-amendment review", "# 3. FLOW-01")
        self.assertEqual(8, len(rows))
        by_flow = {row["Flow"]: row for row in rows}
        self.assertEqual(set(TARGETED_FLOWS) | {"FLOW-09"}, set(by_flow))
        for flow_id, arc_text in TARGETED_FLOWS.items():
            self.assertEqual("TARGETED_FLOW_AMENDMENT_REQUIRED", by_flow[flow_id]["Targeted pressure result"].replace("`", ""))
            self.assertIn(arc_text, by_flow[flow_id]["New/extended ARC touchpoints"])
        self.assertIn("NOT_INCLUDED / CONDITIONAL_REVIEW_NOT_TRIGGERED", by_flow["FLOW-09"]["Targeted pressure result"])
        self.assertIn("no new unproven burst/concurrency event-hold assumption", self.flow)
        flow_ids = re.findall(r"^# \d+\. FLOW-(\d{2})", self.flow, re.MULTILINE)
        self.assertEqual([f"{number:02d}" for number in range(1, 13)], flow_ids)
        for flow_id in ("FLOW-04", "FLOW-05", "FLOW-07", "FLOW-09", "FLOW-12"):
            self.assertEqual(
                _section(self.flow_predecessor, rf"^# \d+\. {flow_id} —", r"^# \d+\. "),
                _section(self.flow, rf"^# \d+\. {flow_id} —", r"^# \d+\. "),
            )

    def test_synthesis_open_work_and_manifest_route_successors(self):
        self.assertIn("ARC-001...ARC-332", self.synthesis)
        self.assertIn("433/433", self.synthesis)
        for section in ("## 4.4 Bounded capability modes", "## 6.5 Participation identity contract", "## 6.6 Platform Member Reference contract", "## 7.5 Versioned Research and Tool evidence", "## 7.6 Layered governed voting authority"):
            self.assertIn(section, self.synthesis)
        self.assertIn("ARCHITECTURE AMENDMENT COMPLETE", self.synthesis)
        self.assertIn("16/16 Stage 4A Product-derived ARQs", self.open_work)
        self.assertIn("exactly the 16 Product-derived ARQs", self.open_work)
        self.assertIn("ENGINEERING STANDARDS: DOWNSTREAM", self.open_work)
        self.assertIn("DOMAIN PRESSURE TEST / AMENDMENT: DOWNSTREAM", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: BLOCKED", self.open_work)
        current = {entry["document_id"]: entry for section in ("governing_documents", "reference_documents") for entry in self.manifest[section]}
        expected = {
            "OPEN_WORK": ("1.2.38", "docs/00_platform/02_OPEN_WORK_v1.2.38.md"),
            "ARCHITECTURE_SYNTHESIS": ("1.1.0", "docs/00_platform/03_ARCHITECTURE_v1.1.0.md"),
            "DOMAIN_MAP": ("1.1.0", "docs/00_platform/04_DOMAIN_MAP_v1.1.0.md"),
            "ARCHITECTURE_LAW": ("0.36.0", "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md"),
            "REFERENCE_FLOW_PRESSURE_TESTS": ("0.3.0", "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md"),
        }
        for document_id, (version, path) in expected.items():
            self.assertEqual(version, current[document_id]["semver"], document_id)
            self.assertEqual(path, current[document_id]["repository_path"], document_id)
            self.assertEqual(_sha256(ROOT / path), current[document_id]["sha256"], document_id)
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        for document_id in ("OPEN_WORK_V1_2_35", "OPEN_WORK_V1_2_36", "ARCHITECTURE_SYNTHESIS_V1_0_0", "ARCHITECTURE_LAW_V0_35_0", "REFERENCE_FLOW_PRESSURE_TESTS_V0_2_0", "DOMAIN_MAP_V1_0_0"):
            self.assertEqual("historical", historical[document_id]["lifecycle"])

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
        supplement = self.law[self.law.index("# 6. Architecture amendment supplement") :]
        self.assertNotIn("TARGETED_ENGINEERING_POLICY_GRILL", supplement)
        for key in ("A-08", "B-09", "D-02", "D-03", "D-04", "D-05", "D-07"):
            self.assertNotIn(f"`{key}`", supplement)
        for arc_id in NEW_ARC_ARQS:
            section = _arc_sections(self.law)[arc_id]
            self.assertNotIn("Engineering-Policy", section)
            self.assertNotIn("Engineering Standards", section)
            self.assertNotIn("LOW/STANDARD/HIGH", section)
            self.assertNotIn("typespec", section.lower())
            self.assertNotIn("static analysis", section.lower())
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md"],
            _sha256(ROOT / "docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md"),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/archive/05_ROADMAP_v1.0.0.md"],
            _sha256(ROOT / "docs/00_platform/archive/05_ROADMAP_v1.0.0.md"),
        )
        self.assertEqual(
            PROTECTED_HASHES["docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md"],
            _sha256(ROOT / "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md"),
        )


if __name__ == "__main__":
    unittest.main()
