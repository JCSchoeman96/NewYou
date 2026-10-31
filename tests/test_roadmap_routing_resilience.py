from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

from foundation_test_support import current_document_path, current_working_path, historical_platform_readme_path, historical_platform_readme_text


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
ROADMAP = DOCS / "archive" / "05_ROADMAP_v1.2.3.md"
ROOT_ROADMAP_PREDECESSOR = DOCS / "05_ROADMAP_v1.2.2.md"
ROADMAP_PREDECESSOR = DOCS / "archive" / "05_ROADMAP_v1.2.2.md"
CURRENT_ROADMAP = current_document_path(ROOT, "ROADMAP")
README = historical_platform_readme_path(ROOT)
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
ROADMAP_V1_1_4_SHA256 = "251f6d174c35de1d227be3b27f6cf812d5dce79ca3efe6c2370564eb170b04c9"
ROADMAP_V1_2_0_SHA256 = "601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0"
ROADMAP_V1_2_2_SHA256 = "4225fad688589d3c66733527303cbda39ef3c8bf52b78c4cc372c0736d202cdc"

PATCH_SCOPE = (
    "## v1.2.3 Patch Scope\n\n"
    "This PATCH corrects proof-classification lifecycle timing and ownership, aligning Roadmap with the governed sequence of Phase 7C, the separate architectural proof classification gate, then Phase 8 executable proof. It preserves all 17 Feature Packs, their outcomes, order, dependencies, affected Domains, gates, exit conditions and anticipated proof directions. It does not select FP-001 proof classification, create a Tracer Bullet, authorise Phase 8 or authorise application implementation.\n\n"
)
PATCH_SCOPE_INSERTION = (
    "\n\n"
    + PATCH_SCOPE
    + "## v1.2.2 Patch Scope"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _normalise_roadmap_successor(successor: str, predecessor: str) -> str:
    route_marker = "- **Current programme routing:** `README.md` and the current Open Work path it identifies."
    route_count = successor.count(route_marker)
    if route_count != 1:
        raise ValueError(f"expected one dynamic Roadmap routing marker, found {route_count}")
    scope_count = successor.count(PATCH_SCOPE)
    if scope_count != 1:
        raise ValueError(f"expected one v1.2.3 Patch Scope, found {scope_count}")

    replacements = (
        ("# 05_ROADMAP_v1.2.3.md", "# 05_ROADMAP_v1.2.2.md"),
        ("FROZEN / AMENDED ROADMAP v1.2.3", "FROZEN / AMENDED ROADMAP v1.2.2"),
        ("**Document version:** v1.2.3", "**Document version:** v1.2.2"),
        ("**Last updated:** 2026-10-18", "**Last updated:** 2026-10-13"),
        ("`archive/05_ROADMAP_v1.2.2.md`", "`archive/05_ROADMAP_v1.2.1.md`"),
        ("`v1.2.2 → v1.2.3`", "`v1.2.1 → v1.2.2`"),
        (
            "Anticipated proof labels are provisional. An anticipated Roadmap proof label is not a proof classification. Phase 7C and the Final Feature Pack Contract freeze the architectural proof requirement and applicable proof obligations. The separate architectural proof classification gate runs after Phase 7C and before Phase 8 executable proof. The gate selects either `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`. This classification is a Development Entry Hard Stop requirement and does not itself prove the architecture. Phase 8 remains the first executable architectural-proof stage.",
            "Anticipated proof labels are deliberately provisional. Phase 7 Final Feature Pack Contracts own the final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` decision.",
        ),
        (
            "**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET`. This direction is provisional. Phase 7C freezes the architectural proof requirement and applicable obligations. The separate architectural proof classification gate after Phase 7C and before Phase 8 selects the final proof vehicle.",
            "**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — the first real authentication/session/recovery path materially exercises the accepted identity boundary; Phase 7 decides whether one proof can cover the complete path.",
        ),
        (
            "No Tracer Bullet is created by this Roadmap. Final proof classification occurs at the separate architectural proof classification gate after Phase 7C and before Phase 8.",
            "No Tracer Bullet is created by this Roadmap. Final proof classification belongs to Phase 7.",
        ),
        (
            "- freeze the architectural proof requirement and applicable obligations; leave the `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET` choice to the separate architectural proof classification gate after Phase 7C and before Phase 8;",
            "- make the final proof choice `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`;",
        ),
    )
    normalised = successor
    for current, previous in replacements:
        count = normalised.count(current)
        if count != 1:
            raise ValueError(f"expected one Roadmap successor marker {current!r}, found {count}")
        normalised = normalised.replace(current, previous, 1)
    insertion_count = normalised.count(PATCH_SCOPE_INSERTION)
    if insertion_count != 1:
        raise ValueError(
        f"expected one v1.2.3 Patch Scope at its declared insertion point, found {insertion_count}"
        )
    normalised = normalised.replace(
        PATCH_SCOPE_INSERTION,
        "\n\n## v1.2.2 Patch Scope",
        1,
    )
    if normalised != predecessor:
        raise ValueError("Roadmap successor differs outside the declared routing patch")
    return normalised


def _feature_pack_sections(text: str) -> dict[str, str]:
    starts = list(re.finditer(r"^## (FP-\d{3}) — .+$", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else text.index("# 7. MVP", match.end())
        sections[match.group(1)] = text[match.start() : end]
    return sections


def _section_bytes(path: Path, heading: str, next_heading_prefix: str) -> bytes:
    lines = path.read_bytes().splitlines(keepends=True)
    start = next(
        index for index, line in enumerate(lines)
        if heading.encode("utf-8") in line
    )
    end = len(lines)
    if next_heading_prefix:
        end = next(
            index for index in range(start + 1, len(lines))
            if lines[index].lstrip().startswith(next_heading_prefix.encode("utf-8"))
        )
    return b"".join(lines[start:end])


class RoadmapRoutingResilienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.roadmap = ROADMAP.read_text(encoding="utf-8") if ROADMAP.is_file() else ""
        cls.current_roadmap = CURRENT_ROADMAP.read_text(encoding="utf-8") if CURRENT_ROADMAP.is_file() else ""
        cls.predecessor = ROADMAP_PREDECESSOR.read_text(encoding="utf-8") if ROADMAP_PREDECESSOR.is_file() else ""
        cls.open_work = current_document_path(ROOT, "OPEN_WORK").read_text(encoding="utf-8")
        cls.atlas = current_working_path(ROOT, "DELIVERY_ATLAS_WORKING_").read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_roadmap_successor_preserves_everything_outside_declared_routing_patch(self):
        self.assertTrue(ROADMAP.is_file(), ROADMAP)
        self.assertFalse(ROOT_ROADMAP_PREDECESSOR.exists(), ROOT_ROADMAP_PREDECESSOR)
        self.assertTrue(ROADMAP_PREDECESSOR.is_file(), ROADMAP_PREDECESSOR)
        if not ROADMAP.is_file() or not ROADMAP_PREDECESSOR.is_file():
            return
        self.assertEqual(ROADMAP_V1_2_2_SHA256, _sha256(ROADMAP_PREDECESSOR))
        self.assertEqual(self.predecessor, _normalise_roadmap_successor(self.roadmap, self.predecessor))

    def test_normalizer_fails_closed_on_missing_duplicate_or_relocated_markers(self):
        self.assertTrue(ROADMAP.is_file(), ROADMAP)
        if not ROADMAP.is_file():
            return
        missing_route = self.roadmap.replace(
            "- **Current programme routing:** `README.md` and the current Open Work path it identifies.",
            "- **Current programme routing:** `README.md`.",
            1,
        )
        duplicate_scope = self.roadmap + "\n" + PATCH_SCOPE
        duplicate_route = self.roadmap.replace(
            "- **Current programme routing:** `README.md` and the current Open Work path it identifies.",
            "- **Current programme routing:** `README.md` and the current Open Work path it identifies.\n"
            "- **Current programme routing:** duplicate",
            1,
        )
        relocated_scope = self.roadmap.replace(
            "\n\n" + PATCH_SCOPE + "---\n\n# 1. Authority, purpose and boundaries",
            "\n\n---\n\n# 1. Authority, purpose and boundaries",
            1,
        ) + "\n" + PATCH_SCOPE
        for malformed in (missing_route, duplicate_scope, duplicate_route, relocated_scope):
            with self.subTest(sample=malformed[:160]):
                with self.assertRaises(ValueError):
                    _normalise_roadmap_successor(malformed, self.predecessor)

    def test_roadmap_dynamic_routing_resolves_through_readme_and_manifest(self):
        self.assertTrue(self.current_roadmap, "current Roadmap v1.2.4 must exist")
        manifest_current = {
            item["document_id"]: item
            for item in self.manifest["governing_documents"]
        }
        roadmap = manifest_current["ROADMAP"]
        open_work = manifest_current["OPEN_WORK"]
        self.assertEqual(CURRENT_ROADMAP.name, roadmap["canonical_filename"])
        self.assertEqual(CURRENT_ROADMAP.relative_to(ROOT).as_posix(), roadmap["repository_path"])
        self.assertEqual(_sha256(CURRENT_ROADMAP), roadmap["sha256"])
        self.assertEqual(Path(open_work["repository_path"]).name, open_work["canonical_filename"])

        header = self.current_roadmap.split("## Amendment summary", 1)[0]
        route_lines = re.findall(r"(?m)^- \*\*Current programme routing:\*\* (.+)$", header)
        self.assertEqual(1, len(route_lines))
        route = route_lines[0]
        self.assertIn("README.md", route)
        self.assertIn("current Open Work path it identifies", route)
        self.assertNotRegex(route, r"02_OPEN_WORK_v\d+\.\d+\.\d+\.md")

        default_context = self.readme.split("## Default Agent Context", 1)[1].split("## Current Authority", 1)[0]
        self.assertIn(f"`{roadmap['canonical_filename']}`", default_context)
        self.assertIn(f"`{open_work['canonical_filename']}`", default_context)

    def test_readme_manifest_open_work_and_atlas_agree_on_current_roadmap(self):
        current_route = CURRENT_ROADMAP.name
        self.assertIn(f"`{current_route}`", self.readme)
        self.assertGreaterEqual(self.open_work.count(current_route), 1)
        self.assertGreaterEqual(self.atlas.count(current_route), 1)

        stale_current = re.compile(r"(?<!archive/)05_ROADMAP_v1\.1\.4\.md")
        for label, text in (
            ("README", self.readme),
            ("current Open Work", self.open_work),
            ("current Atlas", self.atlas),
            ("current Roadmap", self.current_roadmap),
        ):
            with self.subTest(source=label):
                self.assertIsNone(stale_current.search(text), f"stale active Roadmap route in {label}")

        governing = {entry["document_id"]: entry for entry in self.manifest["governing_documents"]}
        self.assertEqual(current_route, governing["ROADMAP"]["canonical_filename"])
        self.assertEqual("1.2.4", governing["ROADMAP"]["semver"])
        history = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        predecessor_roadmap = history["ROADMAP_V1_2_3"]
        self.assertEqual("05_ROADMAP_v1.2.3.md", predecessor_roadmap["canonical_filename"])
        self.assertEqual("docs/00_platform/archive/05_ROADMAP_v1.2.3.md", predecessor_roadmap["repository_path"])
        self.assertEqual("1.2.4", predecessor_roadmap["superseded_version"])
        self.assertEqual("044b5c6308d59253cb0e5ae86d53e13611fb84dec04135b1175880d7881593c2", predecessor_roadmap["sha256"])
        old_roadmap = history["ROADMAP_V1_1_4"]
        self.assertEqual("05_ROADMAP_v1.1.4.md", old_roadmap["canonical_filename"])
        self.assertEqual(
            "docs/00_platform/archive/05_ROADMAP_v1.1.4.md",
            old_roadmap["repository_path"],
        )
        self.assertEqual("1.1.5", old_roadmap["superseded_version"])
        self.assertEqual(ROADMAP_V1_1_4_SHA256, old_roadmap["sha256"])

        patterns = self.manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"]
        stale_route_guards = [pattern for pattern in patterns if "05_ROADMAP_v1\\.1\\.4\\.md" in pattern]
        self.assertEqual([r"(?<!archive/)05_ROADMAP_v1\.1\.4\.md"], stale_route_guards)
        guard = re.compile(stale_route_guards[0])
        self.assertIsNotNone(guard.search("05_ROADMAP_v1.1.4.md"))
        self.assertIsNone(guard.search("archive/05_ROADMAP_v1.1.4.md"))

    def test_current_roadmap_keeps_the_same_feature_pack_inventory(self):
        old_packs = _feature_pack_sections(self.predecessor)
        new_packs = _feature_pack_sections(self.current_roadmap)
        expected = [f"FP-{number:03d}" for number in range(1, 18)]
        self.assertEqual(expected, list(old_packs))
        self.assertEqual(expected, list(new_packs))
        self.assertNotIn("FP-018", self.current_roadmap)

    def test_feature_pack_outcomes_and_unrelated_section_21_content_are_preserved(self):
        self.assertTrue(CURRENT_ROADMAP.is_file(), CURRENT_ROADMAP)
        self.assertTrue(ROADMAP.is_file(), ROADMAP)
        old_packs = _feature_pack_sections(self.roadmap)
        new_packs = _feature_pack_sections(self.current_roadmap)
        self.assertEqual(old_packs.keys(), new_packs.keys())
        for pack_id in old_packs:
            expected = old_packs[pack_id]
            if pack_id in {"FP-002", "FP-003"}:
                expected = expected.replace("00_PLATFORM_v1.8.0.md", "00_PLATFORM_v1.9.0.md", 1)
            if pack_id == "FP-009":
                expected = expected.replace(
                    "`00_PLATFORM_v1.6.0.md §§8, 21G, 21L.8, 21L.11–21L.18, 21T.9`; `DEC-039...DEC-043`, `DEC-170...DEC-190`, `DEC-275`, `DEC-278`, `DEC-283...DEC-285`, `DEC-312`.",
                    "`00_PLATFORM_v1.9.0.md §§8, 21A.6, 21G, 21L.8, 21L.11–21L.18, 21T.9`; `DEC-039...DEC-043`, `DEC-045`, `DEC-170...DEC-190`, `DEC-275`, `DEC-278`, `DEC-283...DEC-285`, `DEC-312`, `DEC-315`.",
                    1,
                )
            self.assertEqual(expected, new_packs[pack_id], pack_id)
        for heading, next_heading in (("# 21. Phase 7 handoff", ""),):
            current = _section_bytes(CURRENT_ROADMAP, heading, next_heading)
            predecessor = _section_bytes(ROADMAP_PREDECESSOR, heading, next_heading)
            self.assertEqual(
                predecessor,
                current.replace(
                    b"- freeze the architectural proof requirement and applicable obligations; leave the `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET` choice to the separate architectural proof classification gate after Phase 7C and before Phase 8;",
                    b"- make the final proof choice `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`;",
                    1,
                ),
                heading,
            )

    def test_patch_scope_is_narrow_and_stage_neutral(self):
        self.assertIn(PATCH_SCOPE.strip(), self.roadmap)
        scope = self.roadmap.split("## v1.2.3 Patch Scope\n\n", 1)[1].split("\n\n", 1)[0]
        self.assertIn("corrects proof-classification lifecycle timing and ownership", scope)
        self.assertIn("preserves all 17 Feature Packs", scope)
        self.assertIn("does not select FP-001 proof classification", scope)
        self.assertIn("create a Tracer Bullet", scope)
        self.assertIn("authorise Phase 8", scope)

    def test_pass2_gates_and_stage_neutrality_are_carried_into_current_roadmap(self):
        fp003 = _feature_pack_sections(self.current_roadmap)["FP-003"]
        fp006 = _feature_pack_sections(self.current_roadmap)["FP-006"]
        fp009 = _feature_pack_sections(self.current_roadmap)["FP-009"]
        fp012 = _feature_pack_sections(self.current_roadmap)["FP-012"]
        self.assertIn("production-intended proprietary assessment encoding", fp003)
        self.assertIn("mask", fp003.lower())
        self.assertIn("first 10", fp006.lower())
        self.assertIn("day 90", fp006.lower())
        self.assertIn("limited public", fp006.lower())
        self.assertIn("recurring contribution", fp009.lower())
        self.assertIn("practitioner", fp012.lower())
        self.assertIn("does not authorize Feature Pack preparation, Phase 7C, Architectural Proof, Phase 8 or implementation", self.current_roadmap)
        self.assertIn("Feature Pack count remains **17**", self.current_roadmap)

    def test_phase7c_freezes_proof_obligations_and_routes_classification_before_phase8(self):
        successor = CURRENT_ROADMAP
        roadmap = successor.read_text(encoding="utf-8") if successor.is_file() else ""
        self.assertTrue(successor.is_file(), "current Roadmap successor must exist")

        self.assertIn(
            "Phase 7C and the Final Feature Pack Contract freeze the architectural proof requirement and applicable proof obligations.",
            roadmap,
        )
        self.assertIn(
            "The separate architectural proof classification gate runs after Phase 7C and before Phase 8 executable proof.",
            roadmap,
        )
        self.assertIn(
            "This classification is a Development Entry Hard Stop requirement and does not itself prove the architecture.",
            roadmap,
        )
        self.assertIn("Phase 8 remains the first executable architectural-proof stage.", roadmap)
        self.assertIn("An anticipated Roadmap proof label is not a proof classification.", roadmap)
        self.assertNotIn(
            "Phase 7 Final Feature Pack Contracts own the final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` decision.",
            roadmap,
        )
        self.assertNotIn(
            "Phase 7 decides whether one proof can cover the complete path.",
            roadmap,
        )
        self.assertNotIn("make the final proof choice", roadmap)
        self.assertIn(
            "leave the `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET` choice to the separate architectural proof classification gate after Phase 7C and before Phase 8",
            roadmap,
        )

        fp001 = re.search(
            r"(?ms)^## FP-001 — .*?(?=^## FP-002 — )",
            roadmap,
        )
        self.assertIsNotNone(fp001, "current FP-001 Roadmap section must exist")
        if fp001:
            self.assertIn("`PROBABLY_NEW_TRACER_BULLET`", fp001.group(0))
            self.assertNotRegex(
                fp001.group(0),
                r"(?m)^\*\*Anticipated Architectural Proof:\*\* `(?:REUSE_EXISTING_PROOF|NEW_TRACER_BULLET)`",
            )
            self.assertNotIn("Phase 7 decides", fp001.group(0))

    def test_current_atlas_routes_the_separate_post_7c_classification_gate(self):
        self.assertIn(
            "Phase 7C resolves blocking gates and produces the Final Feature Pack Contract, which owns development-entry scope and freezes the architectural proof requirement and applicable proof obligations.",
            self.atlas,
        )
        self.assertIn(
            "After Phase 7C and before Phase 8 executable proof, the separate architectural proof classification gate selects `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`.",
            self.atlas,
        )
        self.assertIn(
            "This classification is a Development Entry Hard Stop requirement and does not itself prove the architecture.",
            self.atlas,
        )
        self.assertIn(
            "Phase 8 remains the first executable architectural-proof stage.",
            self.atlas,
        )
        for outdated_claim in (
            "The approved contract records `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`",
            "The Feature Pack contract must still decide `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`",
            "The later Feature Pack contract owns the decision between `REUSE_EXISTING_PROOF` and `NEW_TRACER_BULLET`",
            "The affected Feature Pack later decides whether its requirement is `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`",
        ):
            self.assertNotIn(outdated_claim, self.atlas)

    def test_roadmap_v1_2_2_is_preserved_byte_identically_in_archive(self):
        archived = DOCS / "archive" / "05_ROADMAP_v1.2.2.md"
        working_predecessor = DOCS / "05_ROADMAP_v1.2.2.md"
        self.assertTrue(archived.is_file(), "Roadmap v1.2.2 must be archived")
        self.assertFalse(working_predecessor.exists(), "Roadmap v1.2.2 must leave the current path")
        if archived.is_file():
            self.assertEqual(
                "4225fad688589d3c66733527303cbda39ef3c8bf52b78c4cc372c0736d202cdc",
                hashlib.sha256(archived.read_bytes()).hexdigest(),
            )


if __name__ == "__main__":
    unittest.main()
