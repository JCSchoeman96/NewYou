from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
ROADMAP = DOCS / "05_ROADMAP_v1.1.5.md"
ROOT_ROADMAP_PREDECESSOR = DOCS / "05_ROADMAP_v1.1.4.md"
ROADMAP_PREDECESSOR = DOCS / "archive" / "05_ROADMAP_v1.1.4.md"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.50.md"
ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.3.2.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
ROADMAP_V1_1_4_SHA256 = "251f6d174c35de1d227be3b27f6cf812d5dce79ca3efe6c2370564eb170b04c9"

PATCH_SCOPE = (
    "## v1.1.5 Patch Scope\n\n"
    "This routing-only PATCH updates the explicit current Product-authority route. It preserves all 17 Feature Packs, outcomes, sequencing, dependencies, gates, proof semantics, implementation STOP and programme lifecycle state. README and current Open Work retain programme routing responsibility.\n\n"
)
PATCH_SCOPE_INSERTION = (
    "---\n\n"
    + PATCH_SCOPE
    + "# 1. Authority, purpose and boundaries"
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
        raise ValueError(f"expected one v1.1.5 Patch Scope, found {scope_count}")

    replacements = (
        ("# 05_ROADMAP_v1.1.5.md", "# 05_ROADMAP_v1.1.4.md"),
        ("**Document version:** v1.1.5", "**Document version:** v1.1.4"),
        ("**Last updated:** 2026-09-29", "**Last updated:** 2026-09-26"),
        ("`archive/05_ROADMAP_v1.1.4.md`", "`archive/05_ROADMAP_v1.1.3.md`"),
        ("`v1.1.4 → v1.1.5`", "`v1.1.3 → v1.1.4`"),
        (
            "- **Current Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md`, `00_PLATFORM_v1.5.1.md`, `01_DECISIONS_v1.5.0.md`",
            "- **Current Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`, `00_PLATFORM_v1.5.0.md`, `01_DECISIONS_v1.5.0.md`",
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
            f"expected one v1.1.5 Patch Scope at its declared insertion point, found {insertion_count}"
        )
    normalised = normalised.replace(
        PATCH_SCOPE_INSERTION,
        "---\n\n# 1. Authority, purpose and boundaries",
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


class RoadmapRoutingResilienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.roadmap = ROADMAP.read_text(encoding="utf-8") if ROADMAP.is_file() else ""
        cls.predecessor = ROADMAP_PREDECESSOR.read_text(encoding="utf-8") if ROADMAP_PREDECESSOR.is_file() else ""
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.atlas = ATLAS.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_roadmap_successor_preserves_everything_outside_declared_routing_patch(self):
        self.assertTrue(ROADMAP.is_file(), ROADMAP)
        self.assertFalse(ROOT_ROADMAP_PREDECESSOR.exists(), ROOT_ROADMAP_PREDECESSOR)
        self.assertTrue(ROADMAP_PREDECESSOR.is_file(), ROADMAP_PREDECESSOR)
        if not ROADMAP.is_file() or not ROADMAP_PREDECESSOR.is_file():
            return
        self.assertEqual(ROADMAP_V1_1_4_SHA256, _sha256(ROADMAP_PREDECESSOR))
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
        self.assertTrue(self.roadmap, "current Roadmap v1.1.5 must exist")
        manifest_current = {
            item["document_id"]: item
            for item in self.manifest["governing_documents"]
        }
        roadmap = manifest_current["ROADMAP"]
        open_work = manifest_current["OPEN_WORK"]
        self.assertEqual("05_ROADMAP_v1.1.5.md", roadmap["canonical_filename"])
        self.assertEqual("docs/00_platform/05_ROADMAP_v1.1.5.md", roadmap["repository_path"])
        self.assertEqual(_sha256(ROADMAP), roadmap["sha256"])
        self.assertEqual("02_OPEN_WORK_v1.2.50.md", open_work["canonical_filename"])

        header = self.roadmap.split("## Amendment summary", 1)[0]
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
        current_route = "05_ROADMAP_v1.1.5.md"
        self.assertIn(f"`{current_route}`", self.readme)
        self.assertEqual(6, self.open_work.count(current_route))
        self.assertEqual(6, self.atlas.count(current_route))

        stale_current = re.compile(r"(?<!archive/)05_ROADMAP_v1\.1\.4\.md")
        for label, text in (
            ("README", self.readme),
            ("current Open Work", self.open_work),
            ("current Atlas", self.atlas),
            ("current Roadmap", self.roadmap),
        ):
            with self.subTest(source=label):
                self.assertIsNone(stale_current.search(text), f"stale active Roadmap route in {label}")

        governing = {entry["document_id"]: entry for entry in self.manifest["governing_documents"]}
        self.assertEqual(current_route, governing["ROADMAP"]["canonical_filename"])
        self.assertEqual("1.1.5", governing["ROADMAP"]["semver"])
        history = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
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

    def test_all_feature_pack_sections_and_section_21_are_exactly_preserved(self):
        old_packs = _feature_pack_sections(self.predecessor)
        new_packs = _feature_pack_sections(self.roadmap)
        expected = [f"FP-{number:03d}" for number in range(1, 18)]
        self.assertEqual(expected, list(old_packs))
        self.assertEqual(expected, list(new_packs))
        self.assertEqual(old_packs, new_packs)

        marker = "# 21. Phase 7 handoff\n"
        old_section = self.predecessor.split(marker, 1)[1].split("\n# 22.", 1)[0]
        new_section = self.roadmap.split(marker, 1)[1].split("\n# 22.", 1)[0]
        self.assertEqual(old_section, new_section)

    def test_patch_scope_is_narrow_and_stage_neutral(self):
        self.assertIn(PATCH_SCOPE.strip(), self.roadmap)
        scope = self.roadmap.split("## v1.1.5 Patch Scope\n\n", 1)[1].split("\n\n", 1)[0]
        self.assertIn("routing-only PATCH", scope)
        self.assertIn("preserves all 17 Feature Packs", scope)


if __name__ == "__main__":
    unittest.main()
