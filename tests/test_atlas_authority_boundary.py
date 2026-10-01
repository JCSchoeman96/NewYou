from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.3.5.md"
ATLAS_SUCCESSOR = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.3.0.md"
ATLAS_PREDECESSOR = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.3.md"
OPEN_WORK = DOCS / "archive" / "02_OPEN_WORK_v1.2.48.md"
CURRENT_OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.53.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.47.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
POM = DOCS / "PLATFORM_OPERATING_MODEL_v1.0.1.md"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(text: str, start_heading: str, end_heading: str) -> str:
    start_matches = list(re.finditer(rf"(?m)^{re.escape(start_heading)}.*$", text))
    end_matches = list(re.finditer(rf"(?m)^{re.escape(end_heading)}.*$", text))
    if len(start_matches) != 1 or len(end_matches) != 1:
        raise ValueError(
            f"expected one {start_heading!r} and {end_heading!r} heading, "
            f"found {len(start_matches)} and {len(end_matches)}"
        )
    start, end = start_matches[0].start(), end_matches[0].start()
    if start >= end:
        raise ValueError(f"{start_heading!r} must precede {end_heading!r}")
    return text[start:end]


def _source_owned_block(*, required_evidence_missing: bool, stronger_source_stop: bool) -> bool:
    """An Atlas-only recommendation has no authority to block work or closure."""
    return stronger_source_stop or required_evidence_missing


AUTHORITY_BOUNDARY_BLOCKS = (
    ("# Delivery Atlas working", "# 1. Authority, purpose and boundaries"),
    ("## 1.1 Authority hierarchy", "## 1.2 Purpose"),
    ("# Delivery Lifecycle Governance", "# 2. Atlas terminology and classification system"),
    ("## 6.3 Derivation procedure", "## 6.4 Domain relationship exception register"),
    ("## 6.5 JIT projection contract", "## 6.6 Coverage audit and STOP rule"),
    ("## 7.1 Purpose and permanent boundary", "## 7.2 State-machine rule"),
    ("## 7.3 Canonical inputs and authority boundary", "## 7.4 Derivation path and procedure"),
    ("## 7.4 Derivation path and procedure", "## 7.5 Capability != lifecycle concept"),
    ("## 7.7 Lifecycle coverage vocabulary", "## 7.8 Coverage status versus risk flags"),
    ("## 7.10 JIT Domain Dossier gate and proof boundary", "## 7.11 Feature Pack Grill-Me role"),
    ("## 7.11 Feature Pack Grill-Me role", "## 7.12 Projection review triggers"),
    ("## 7.12 Projection review triggers", "## 7.13 Selective context rule"),
    ("## 7.15 ATLAS-06 closure audit", "# 8. Cross-Domain Dependency Derivation & JIT Projection Contract"),
    ("## 8.6 Active-Feature-Pack derivation path", "## 8.7 Temporary active-FP dependency projection"),
    ("## 8.21 ATLAS-07 closure audit", "# 9. Participant Journey Boundaries & JIT Projection Contract"),
    ("## 9.3 Canonical inputs and authority precedence", "## 9.4 Permanent participant boundary register"),
    ("## 9.5 Active-Feature-Pack derivation path", "## 9.7 Frontend/JIT rule"),
    ("## 10.1 Purpose and permanence rule", "## 10.2 Authority sources and precedence"),
    ("## 10.2 Authority sources and precedence", "## 10.3 Operating Model reference boundary"),
    ("## 11.1 Purpose and permanence rule", "## 11.2 Authority sources and precedence"),
    ("## 11.2 Authority sources and precedence", "## 11.3 Frontend Experience System reference boundary"),
    ("## 11.9 Active-Feature-Pack derivation path", "## 11.10 Temporary active-FP frontend projection"),
    ("## 12.2 Existing authority and precedence", "## 12.3 Authority boundaries"),
    ("## 12.4 Active-Feature-Pack derivation", "## 12.5 Temporary active-FP data projection"),
    ("## 9.9 Selective context and JIT boundary", "# 10. Staff / Operator JIT Derivation Contract"),
    ("## 10.7 Active-Feature-Pack derivation path", "## 10.8 Temporary active-FP operator projection"),
    ("## 10.9 Review, approval and escalation boundary", "## 10.10 Evidence, scheduling and analytics boundary"),
    ("# 23. Development navigation rules", "# 24. Atlas governance/change policy"),
    ("# 24. Atlas governance/change policy", "# 25. Global STOP conditions"),
    ("# 25. Global STOP conditions", "# 26. Closure/readiness audit"),
    ("# 26. Closure/readiness audit", None),
)


def _normalise_atlas_successor(successor: str, predecessor: str) -> str:
    route_marker = "02_OPEN_WORK_v1.2.48.md"
    if successor.count(route_marker) != 2:
        raise ValueError(f"expected 2 current Open Work route markers, found {successor.count(route_marker)}")
    successor = successor.replace(route_marker, "02_OPEN_WORK_v1.2.47.md")
    roadmap_route_marker = "05_ROADMAP_v1.1.4.md"
    if successor.count(roadmap_route_marker) != 6:
        raise ValueError(
            f"expected 6 current Roadmap route markers, found {successor.count(roadmap_route_marker)}"
        )
    successor = successor.replace(roadmap_route_marker, "05_ROADMAP_v1.1.3.md")
    roadmap_version_marker = "Roadmap `v1.1.4`"
    if successor.count(roadmap_version_marker) != 1:
        raise ValueError(
            f"expected 1 current Roadmap version marker, found {successor.count(roadmap_version_marker)}"
        )
    successor = successor.replace(roadmap_version_marker, "Roadmap `v1.1.3`", 1)
    for start_heading, end_heading in AUTHORITY_BOUNDARY_BLOCKS:
        if end_heading is None:
            start_matches = list(re.finditer(rf"(?m)^{re.escape(start_heading)}.*$", successor))
            old_start_matches = list(re.finditer(rf"(?m)^{re.escape(start_heading)}.*$", predecessor))
            if len(start_matches) != 1 or len(old_start_matches) != 1:
                raise ValueError(f"expected one terminal section marker: {start_heading}")
            successor = successor[: start_matches[0].start()] + predecessor[old_start_matches[0].start() :]
            continue
        current = _section(successor, start_heading, end_heading)
        old = _section(predecessor, start_heading, end_heading)
        if successor.count(current) != 1 or predecessor.count(old) != 1:
            raise ValueError(f"authority-boundary block is duplicated or relocated: {start_heading}")
        successor = successor.replace(current, old, 1)
    return successor


OPEN_WORK_HISTORICAL_ATLAS_BLOCK = (
    "## 12.7 — Historical Delivery Atlas reconciliation\n\n"
    "**Status:** HISTORICAL COMPLETION RECORD — the then-current derived / non-authoritative navigation successor was "
    "`working/DELIVERY_ATLAS_WORKING_v0.2.1.md` (predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`; "
    "earlier predecessor `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`). This subsection records that historical "
    "reconciliation and is not the current Atlas route.\n\n"
)
OPEN_WORK_HISTORICAL_ATLAS_BLOCK_PREDECESSOR = (
    "## 12.7 — Delivery Atlas reconciliation\n\n"
    "**Status:** COMPLETE as derived / non-authoritative navigation successor `working/DELIVERY_ATLAS_WORKING_v0.2.1.md` "
    "(predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`; earlier predecessor "
    "`archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`).\n\n"
)


OPEN_WORK_ATLAS_CURRENT_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.0.md`; "
    "immediate predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.3.md`; pinned v0.2.1 source-at-freeze artifacts remain preserved; "
    "DERIVED / NON-AUTHORITATIVE; ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)
OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE = OPEN_WORK_ATLAS_CURRENT_STATUS_LINE.replace(
    "working/DELIVERY_ATLAS_WORKING_v0.3.0.md",
    "working/DELIVERY_ATLAS_WORKING_v0.2.3.md",
)
OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.2.3.md`; "
    "predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md`; DERIVED / NON-AUTHORITATIVE; "
    "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)


def _validate_open_work_atlas_status_line(text: str, expected: str) -> None:
    matches = list(re.finditer(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", text))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one Open Work Atlas reconciliation status line, found {len(matches)}")
    start_positions = [
        match.start() for match in re.finditer(r"(?m)^# 9\. Immediate Next Action\r?$", text)
    ]
    end_positions = [
        match.start() for match in re.finditer(r"(?m)^# 10\. Minimal Tools\r?$", text)
    ]
    if (
        len(start_positions) != 1
        or len(end_positions) != 1
        or not start_positions[0] < matches[0].start() < end_positions[0]
    ):
        raise ValueError("Open Work Atlas reconciliation status line is missing from or relocated outside §9")
    if matches[0].group(0) != expected:
        raise ValueError("Open Work §9 Atlas reconciliation status line differs outside declared lineage clarification")


def _normalise_open_work_successor(successor: str, predecessor: str) -> str:
    _validate_open_work_atlas_status_line(successor, OPEN_WORK_ATLAS_CURRENT_STATUS_LINE)
    if successor.count(OPEN_WORK_HISTORICAL_ATLAS_BLOCK) != 1:
        raise ValueError("expected exactly one historical Atlas clarification block in Open Work successor")
    replacements = (
        ("# 02_OPEN_WORK_v1.2.48.md", "# 02_OPEN_WORK_v1.2.47.md", 1),
        ("OPEN-WORK SUCCESSOR v1.2.48", "OPEN-WORK SUCCESSOR v1.2.47", 1),
        ("Document version:** v1.2.48", "Document version:** v1.2.47", 1),
        ("archive/02_OPEN_WORK_v1.2.47.md", "archive/02_OPEN_WORK_v1.2.46.md", 1),
        ("v1.2.47 → v1.2.48", "v1.2.46 → v1.2.47", 1),
        ("working/DELIVERY_ATLAS_WORKING_v0.3.0.md", "working/DELIVERY_ATLAS_WORKING_v0.2.3.md", 5),
        ("05_ROADMAP_v1.1.4.md", "05_ROADMAP_v1.1.3.md", 6),
    )
    for current, old, expected_count in replacements:
        actual_count = successor.count(current)
        if actual_count != expected_count:
            raise ValueError(
                f"expected {expected_count} routing/version marker(s) for {current}, found {actual_count}"
            )
        successor = successor.replace(current, old)
    _validate_open_work_atlas_status_line(successor, OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE)
    successor = successor.replace(
        OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE,
        OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE,
        1,
    )
    _validate_open_work_atlas_status_line(successor, OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE)
    if successor.count(OPEN_WORK_HISTORICAL_ATLAS_BLOCK) != 1:
        raise ValueError("historical Atlas clarification block is missing, duplicate, or relocated")
    successor = successor.replace(
        OPEN_WORK_HISTORICAL_ATLAS_BLOCK,
        OPEN_WORK_HISTORICAL_ATLAS_BLOCK_PREDECESSOR,
        1,
    )
    if successor != predecessor:
        raise ValueError("Open Work successor differs outside declared routing/version, §9 lineage, and historical clarification markers")
    return successor


class AtlasAuthorityBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.atlas = ATLAS.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.pom = POM.read_text(encoding="utf-8")

    def test_successor_normalises_to_the_predecessor_outside_declared_change_blocks(self):
        self.assertTrue(ATLAS_SUCCESSOR.is_file(), ATLAS_SUCCESSOR)
        self.assertTrue(ATLAS_PREDECESSOR.is_file(), ATLAS_PREDECESSOR)
        if not ATLAS_SUCCESSOR.is_file() or not ATLAS_PREDECESSOR.is_file():
            return
        successor = ATLAS_SUCCESSOR.read_text(encoding="utf-8")
        predecessor = ATLAS_PREDECESSOR.read_text(encoding="utf-8")
        self.assertEqual(predecessor, _normalise_atlas_successor(successor, predecessor))

    def test_normalizers_fail_closed_on_missing_duplicate_or_relocated_markers(self):
        successor = ATLAS_SUCCESSOR.read_text(encoding="utf-8")
        predecessor = ATLAS_PREDECESSOR.read_text(encoding="utf-8")
        current_route = "02_OPEN_WORK_v1.2.48.md"
        missing_route = successor.replace(current_route, "02_OPEN_WORK_v1.2.47.md", 1)
        duplicate_route = successor.replace(current_route, current_route + " " + current_route, 1)
        duplicated_heading = successor.replace(
            "## 7.11 Feature Pack Grill-Me role",
            "## 7.11 Feature Pack Grill-Me role\n## 7.11 Feature Pack Grill-Me role",
            1,
        )
        relocated = successor.replace("## 7.10 JIT Domain Dossier gate and proof boundary", "__ATLAS_SECTION_7_10__", 1)
        relocated = relocated.replace("## 7.11 Feature Pack Grill-Me role", "## 7.10 JIT Domain Dossier gate and proof boundary", 1)
        relocated = relocated.replace("__ATLAS_SECTION_7_10__", "## 7.11 Feature Pack Grill-Me role", 1)
        for malformed in (missing_route, duplicate_route, duplicated_heading, relocated):
            with self.subTest(malformed=malformed[:120]):
                with self.assertRaises(ValueError):
                    _normalise_atlas_successor(malformed, predecessor)

        open_work = OPEN_WORK.read_text(encoding="utf-8")
        open_work_predecessor = OPEN_WORK_PREDECESSOR.read_text(encoding="utf-8")
        atlas_route = "working/DELIVERY_ATLAS_WORKING_v0.3.0.md"
        missing_open_route = open_work.replace(atlas_route, "working/DELIVERY_ATLAS_WORKING_v0.2.3.md", 1)
        duplicate_open_route = open_work.replace(atlas_route, atlas_route + " " + atlas_route, 1)
        for malformed in (missing_open_route, duplicate_open_route):
            with self.subTest(malformed=malformed[:120]):
                with self.assertRaises(ValueError):
                    _normalise_open_work_successor(malformed, open_work_predecessor)

        lineage_line = OPEN_WORK_ATLAS_CURRENT_STATUS_LINE
        missing_lineage = open_work.replace(lineage_line + "\n", "", 1)
        duplicate_lineage = open_work.replace(lineage_line, lineage_line + "\n" + lineage_line, 1)
        relocated_lineage = open_work.replace(lineage_line + "\n", "", 1).replace(
            "# 10. Minimal Tools", "# 10. Minimal Tools\n" + lineage_line, 1
        )
        changed_lineage = open_work.replace(
            "immediate predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.3.md`",
            "predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md`",
            1,
        )
        for malformed in (missing_lineage, duplicate_lineage, relocated_lineage, changed_lineage):
            with self.subTest(malformed=malformed[:120]):
                with self.assertRaises(ValueError):
                    _normalise_open_work_successor(malformed, open_work_predecessor)

    def test_grill_me_keeps_its_questions_without_becoming_a_gate(self):
        grill = _section(self.atlas, "## Grill-Me", "## Implementation handoff")
        for question in (
            "What assumptions exist?",
            "What dependencies exist?",
            "What could invalidate the approach?",
            "What future capability could be blocked?",
            "What domains are affected?",
            "What policies/lifecycles are involved?",
            "Are acceptance criteria clear?",
            "Are failure modes understood?",
            "Are security/privacy/performance requirements identified?",
        ):
            self.assertIn(question, grill)
        self.assertNotRegex(grill, r"(?i)reviews are required before")
        self.assertNotRegex(grill, r"(?i)review is a .*gate")
        self.assertRegex(grill, r"(?i)advisory|recommended")
        self.assertRegex(grill, r"(?i)approved (?:feature pack )?contract|upstream source")
        self.assertRegex(grill, r"(?i)positive review.{0,100}(?:does not|cannot).{0,60}permission")
        self.assertRegex(grill, r"(?i)mandatory because that source owns the requirement")

    def test_handoff_fields_remain_useful_without_a_named_artifact_requirement(self):
        handoff = _section(self.atlas, "## Implementation handoff", "## Continuation review")
        for field in (
            "what was implemented",
            "final architecture impact",
            "domain impact",
            "lifecycle changes",
            "state machine changes",
            "database changes",
            "performance characteristics",
            "security/privacy changes",
            "tests/evidence",
            "operational requirements",
            "known limitations",
            "unlocked future work",
        ):
            self.assertIn(field, handoff)
        self.assertNotRegex(handoff, r"(?i)must produce an Implementation Handoff")
        self.assertRegex(handoff, r"(?i)recommended|useful|optional")
        self.assertRegex(handoff, r"(?i)unless|when.{0,80}(?:contract|upstream source).{0,40}requires")

    def test_continuation_revalidation_does_not_require_a_named_review_artifact(self):
        continuation = _section(self.atlas, "## Continuation review", "## Evidence and closure requirements")
        for evidence in (
            "previous handoff documentation",
            "current repository state",
            "current tests",
            "current authority documents",
        ):
            self.assertIn(evidence, continuation)
        self.assertNotRegex(continuation, r"(?i)continuation review must")
        self.assertRegex(continuation, r"(?i)recommend|revalidation")
        self.assertRegex(continuation, r"(?i)authority.{0,100}(?:changed|conflict).{0,100}(?:stop|stops)")
        self.assertRegex(continuation, r"(?i)(?:missing|absence).{0,80}(?:named|continuation review).{0,80}(?:not|does not).{0,60}block")

    def test_closure_follows_upstream_contract_evidence_and_not_atlas_only_checklists(self):
        closure = _section(self.atlas, "## Evidence and closure requirements", "## Decision Escalation Matrix")
        for source_requirement in (
            "approved Feature Pack",
            "JIT",
            "acceptance criteria",
            "proof",
            "security",
            "privacy",
            "performance",
            "operational",
            "recovery",
        ):
            self.assertIn(source_requirement.lower(), closure.lower())
        self.assertNotIn("Closure requires all of the following", closure)
        self.assertNotRegex(closure, r"(?i)required Grill-Me reviews")
        self.assertNotRegex(closure, r"(?i)Implementation Handoff is complete")
        self.assertNotRegex(closure, r"(?i)Continuation Review confirms")
        self.assertRegex(closure, r"(?i)required by.{0,100}(?:authority|contract|source)")
        self.assertRegex(closure, r"(?i)missing.{0,100}(?:required|upstream).{0,100}(?:stop|gate|open|block)")

    def test_pressure_cases_block_only_for_source_owned_requirements_or_stops(self):
        cases = (
            ("optional Grill-Me skipped", False, False, False),
            ("approved contract review missing", True, False, True),
            ("evidence exists without a named Handoff", False, False, False),
            ("resume after a gap with unchanged authority", False, False, False),
            ("current authority changed materially", False, True, True),
            ("contract-required security evidence missing", True, False, True),
            ("Atlas says proceed while upstream says STOP", False, True, True),
        )
        for name, missing_source_evidence, stronger_stop, expected_block in cases:
            with self.subTest(name=name):
                self.assertEqual(
                    expected_block,
                    _source_owned_block(
                        required_evidence_missing=missing_source_evidence,
                        stronger_source_stop=stronger_stop,
                    ),
                )
        self.assertIn("current upstream authority", self.atlas.lower())
        self.assertRegex(self.atlas, r"(?i)Atlas.{0,100}(?:cannot|does not).{0,80}override")

    def test_phase_7_sequence_matches_the_unchanged_operating_model(self):
        canonical = "Feature Pack Skeleton + Gate Manifest → required JIT Domain Dossiers → Final Feature Pack Contract"
        self.assertIn(canonical, self.pom)
        self.assertIn("This document creates no additional Phase 7 artifact types.", self.pom)
        self.assertEqual(
            "7cb725adcdb796ba112d39c4be6fd09c90026b49e772b61f0867db62828b9d12",
            _sha256(POM),
        )
        lifecycle = _section(self.atlas, "## Lifecycle purpose and operating flow", "## Feature Pack lifecycle")
        ordered_stages = (
            "Roadmap approved outcome",
            "Phase 7A Feature Pack Skeleton + preliminary Gate Manifest",
            "Phase 7B required JIT Domain Dossiers",
            "Phase 7C Final Feature Pack Contract",
            "explicit proof classification",
            "proof / Tracer Bullet only when required by the approved contract",
            "Vertical Slices",
            "Horizontal Hardening",
            "Release / Readiness",
        )
        positions = [lifecycle.find(stage) for stage in ordered_stages]
        self.assertTrue(all(position >= 0 for position in positions), positions)
        self.assertEqual(sorted(positions), positions)
        self.assertRegex(lifecycle, r"(?i)Atlas.{0,160}(?:does not|cannot).{0,120}(?:create|add).{0,60}(?:gate|prerequisite|artifact)")

    def test_advisory_reviews_are_not_inserted_as_delivery_lifecycle_stages(self):
        self.assertNotRegex(
            self.atlas,
            r"(?m)^\s*→\s*Optional advisory review prompts",
        )
        self.assertRegex(self.atlas, r"(?i)optional Grill-Me prompts may (?:help|inform)")

    def test_stop_conditions_remain_fail_closed_without_an_atlas_only_record_gate(self):
        stop_rules = _section(self.atlas, "# 25. Global STOP conditions", "# 26. Closure/readiness audit")
        self.assertIn("Product Law conflicts", stop_rules)
        self.assertIn("Architecture Law conflicts", stop_rules)
        self.assertIn("Roadmap sequencing conflicts", stop_rules)
        self.assertIn("Do not STOP solely because an Atlas-only", stop_rules)
        self.assertNotRegex(self.atlas, r"(?i)STOP record must")
        self.assertIn("When STOP occurs, report:", stop_rules)
        for stop_field in (
            "the exact source path and section or identifier",
            "the finding and the evidence that produced it",
            "the authority level that must decide or correct it",
            "the affected Atlas view and Feature Pack relationship",
            "the safe downstream action after resolution",
            "the fact that no Atlas-level guess was made",
        ):
            self.assertIn(stop_field, stop_rules)

    def test_full_spec_completion_and_review_preserve_source_owned_gate_boundary(self):
        coverage = _section(self.atlas, "## 7.7 Lifecycle coverage vocabulary", "## 7.8 Coverage status versus risk flags")
        dossier_boundary = _section(
            self.atlas,
            "## 7.10 JIT Domain Dossier gate and proof boundary",
            "## 7.11 Feature Pack Grill-Me role",
        )
        completion = _section(self.atlas, "## 26.6 ATLAS-06 completion standard", "## 26.7 ATLAS-06 review protocol")
        review = _section(self.atlas, "## 26.7 ATLAS-06 review protocol", "## 26.8 ATLAS-07 completion standard")

        for source_owner in (
            "current authority",
            "preliminary Gate Manifest",
            "approved Feature Pack contract",
        ):
            with self.subTest(source_owner=source_owner):
                self.assertIn(source_owner, coverage)

        self.assertRegex(
            coverage,
            r"(?is)`FULL_SPEC_REQUIRED`.*source-owned requirement.*does not create one",
        )
        self.assertRegex(
            coverage,
            r"(?is)Use this status only when current authority, the preliminary Gate Manifest or an approved Feature Pack contract requires full lifecycle specification",
        )
        self.assertRegex(
            dossier_boundary,
            r"(?i)(?:makes complete lifecycle specification a prerequisite|cannot independently impose this prerequisite)",
        )

        completion_row = re.search(
            r"(?im)^\|\s*[^|]*(?:gate|requirement)[^|]*\|.*`FULL_SPEC_REQUIRED`.*$",
            completion,
        )
        self.assertIsNotNone(completion_row)
        if completion_row is None:
            return
        self.assertRegex(
            completion_row.group(0),
            r"(?i)`FULL_SPEC_REQUIRED` records a source-owned requirement for complete implementation-grade lifecycle semantics in the affected JIT Domain Dossier before governed implementation proceeds; the Atlas does not create that gate\."
        )
        self.assertNotRegex(completion_row.group(0), r"(?i)`FULL_SPEC_REQUIRED` explicitly gates")
        self.assertRegex(
            review,
            r"(?i)source-owned `FULL_SPEC_REQUIRED` requirement.{0,100}JIT Domain Dossier obligation",
        )
        self.assertNotRegex(review, r"(?i)`FULL_SPEC_REQUIRED` Dossier gate")
        for section_name, section in (("completion", completion), ("review", review)):
            mandatory_references = [
                line
                for line in section.splitlines()
                if "`FULL_SPEC_REQUIRED`" in line
                and re.search(
                    r"(?i)must|mandatory|requirement|obligation|gate|prerequisite|before governed implementation",
                    line,
                )
            ]
            self.assertTrue(mandatory_references, section_name)
            for line in mandatory_references:
                with self.subTest(section=section_name, line=line):
                    self.assertRegex(line, r"(?i)source-owned")

    def test_manifest_keeps_atlas_out_of_authority_records_but_in_navigation(self):
        authority_records = self.manifest["governing_documents"] + self.manifest["reference_documents"]
        self.assertFalse(any("ATLAS" in entry["document_id"] for entry in authority_records))
        self.assertFalse(any("DELIVERY_ATLAS" in entry["repository_path"] for entry in authority_records))
        self.assertFalse(
            any("ATLAS" in entry["document_id"] for entry in self.manifest["historical_documents"])
        )
        graph = self.manifest["integrity_rules"]["graph_rules"]
        self.assertIn(
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.5.md",
            graph["navigation_document_paths"],
        )
        stale_patterns = [re.compile(pattern) for pattern in graph["stale_reference_patterns"]]
        self.assertTrue(any(pattern.search("working/DELIVERY_ATLAS_WORKING_v0.2.3.md") for pattern in stale_patterns))
        self.assertFalse(any(pattern.search("archive/DELIVERY_ATLAS_WORKING_v0.2.3.md") for pattern in stale_patterns))
        open_work_entry = next(entry for entry in self.manifest["governing_documents"] if entry["document_id"] == "OPEN_WORK")
        self.assertEqual("02_OPEN_WORK_v1.2.53.md", open_work_entry["canonical_filename"])
        self.assertEqual(_sha256(CURRENT_OPEN_WORK), open_work_entry["sha256"])
        self.assertTrue(any(entry["document_id"] == "OPEN_WORK_V1_2_48" for entry in self.manifest["historical_documents"]))
        old_open_work = next(
            entry for entry in self.manifest["historical_documents"] if entry["document_id"] == "OPEN_WORK_V1_2_47"
        )
        self.assertEqual(_sha256(OPEN_WORK_PREDECESSOR), old_open_work["sha256"])
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.2.1.md", (DOCS / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md").read_text(encoding="utf-8"))
        self.assertFalse(any(pattern.search("working/DELIVERY_ATLAS_WORKING_v0.2.1.md") for pattern in stale_patterns))
        self.assertEqual(
            _sha256(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"),
            _sha256(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"),
        )

    def test_open_work_successor_is_routing_only_and_preserves_programme_state(self):
        self.assertTrue(OPEN_WORK.is_file())
        self.assertTrue(OPEN_WORK_PREDECESSOR.is_file())
        self.assertEqual(
            "71d6f4641cdc70aaa57c8630887d4b24d1a971d34e390c607dda7dbcc8c05118",
            _sha256(OPEN_WORK_PREDECESSOR),
        )
        predecessor = OPEN_WORK_PREDECESSOR.read_text(encoding="utf-8")
        successor = OPEN_WORK.read_text(encoding="utf-8")
        self.assertEqual(predecessor, _normalise_open_work_successor(successor, predecessor))
        for preserved_state in (
            "HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED",
            "Engineering Standards Authority Promotion remains downstream",
            "FP-001 reconciliation remains downstream",
            "COMMUNICATIONS: REQUIRED / NOT_STARTED",
            "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "PHASE 7C: BLOCKED / NOT_STARTED",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
            "Feature Pack count remains **17**",
            "Domain count remains **20**",
        ):
            self.assertIn(preserved_state, successor)


if __name__ == "__main__":
    unittest.main()
