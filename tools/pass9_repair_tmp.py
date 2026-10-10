from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MAIN_SHA = "086ade7b28c000de1c387acb9760e5eb08bb0413"


def read(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def one(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected exactly one marker, found {count}: {old[:160]!r}")
    return text.replace(old, new, 1)


def section(text: str, start: str, end: str) -> tuple[int, int, str]:
    a = text.find(start)
    b = text.find(end, a + len(start)) if a >= 0 else -1
    if a < 0 or b < 0 or a >= b:
        raise AssertionError(f"section not found or malformed: {start!r} -> {end!r}")
    return a, b, text[a:b]


def replace_in_section(text: str, start: str, end: str, replacements: list[tuple[str, str]]) -> str:
    a, b, body = section(text, start, end)
    for old, new in replacements:
        body = body.replace(old, new)
    return text[:a] + body + text[b:]


def replace_function(text: str, name: str, body: str) -> str:
    start = text.find(f"    def {name}(")
    if start < 0:
        raise AssertionError(f"function not found: {name}")
    nxt = text.find("\n    def ", start + 8)
    end = len(text) if nxt < 0 else nxt
    return text[:start] + body.rstrip() + "\n" + text[end:]


def insert_before_main(text: str, body: str) -> str:
    marker = '\n\nif __name__ == "__main__":'
    pos = text.rfind(marker)
    if pos < 0:
        raise AssertionError("__main__ marker not found")
    return text[:pos] + "\n" + body.rstrip() + "\n" + text[pos:]


# ---------------------------------------------------------------------------
# 1. Open Work v1.2.60: active current routes + lifecycle successor facts.
# ---------------------------------------------------------------------------
open_work_path = DOCS / "02_OPEN_WORK_v1.2.60.md"
open_work = read(open_work_path)
current_replacements = [
    ("05_ROADMAP_v1.2.0.md", "05_ROADMAP_v1.3.0.md"),
    ("archive/05_ROADMAP_v1.1.5.md", "archive/05_ROADMAP_v1.2.0.md"),
    ("working/DELIVERY_ATLAS_WORKING_v0.4.1.md", "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"),
    ("archive/DELIVERY_ATLAS_WORKING_v0.4.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.4.1.md"),
    ("working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", "working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"),
]
open_work = replace_in_section(open_work, "# 9. Immediate Next Action", "# 10. Minimal Tools", current_replacements)
open_work = replace_in_section(open_work, "## 12.1 Programme state", "## 12.2", current_replacements)
open_work = open_work.replace('"status_successor_version": "0.5.3"', '"status_successor_version": "0.5.4"', 1)
open_work = open_work.replace(
    '"status_successor_base_sha": "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"',
    f'"status_successor_base_sha": "{MAIN_SHA}"',
    1,
)
open_work = open_work.replace("current status routing is v0.5.3", "current status routing is v0.5.4")
open_work = open_work.replace(
    "current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `v1.1.5` is preserved at `archive/05_ROADMAP_v1.2.0.md`",
    "current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `v1.2.0` is preserved at `archive/05_ROADMAP_v1.2.0.md`",
)
write(open_work_path, open_work)

# ---------------------------------------------------------------------------
# 2. README current-state/navigation routes only. Preserve source-at-freeze.
# ---------------------------------------------------------------------------
readme_path = DOCS / "README.md"
readme = read(readme_path)
current_state_start = readme.find("## Current State")
if current_state_start < 0:
    raise AssertionError("README Current State missing")
head = readme[:current_state_start]
tail = readme[current_state_start:]
for old, new in current_replacements:
    tail = tail.replace(old, new)
readme = head + tail
readme = readme.replace(
    "ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.2.0`",
    "ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.3.0`",
)
atlas_bullet = (
    "- `working/DELIVERY_ATLAS_WORKING_v0.4.2.md` — routing-only derived Delivery Atlas successor aligned to "
    "Roadmap v1.3.0 and Open Work v1.2.60. It remains working/non-authoritative and does not semantically re-derive "
    "prior Atlas views; current Roadmap authority wins. Direct predecessor v0.4.1 is preserved byte-identically at "
    "`archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`."
)
source_freeze_sentence = (
    " The unchanged v0.2.1 working path remains available to existing FP-001 and HARDEN-02 source-at-freeze references."
)
if atlas_bullet in readme and source_freeze_sentence.strip() not in readme:
    readme = readme.replace(atlas_bullet, atlas_bullet + source_freeze_sentence, 1)
write(readme_path, readme)

# ---------------------------------------------------------------------------
# 3. Atlas v0.4.2: routing-only current successor; old views remain source-at-freeze.
# ---------------------------------------------------------------------------
atlas_path = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"
atlas = read(atlas_path)
marker = "FP-001 status and all later gates remain unchanged."
if marker in atlas and "does not amend upstream law or HARDEN-02 contract semantics" not in atlas:
    atlas = atlas.replace(
        marker,
        marker + " This successor does not amend upstream law or HARDEN-02 contract semantics.",
        1,
    )
atlas = atlas.replace(
    "Roadmap `v1.2.0` and current Open Work `v1.2.59`.",
    "Roadmap `v1.3.0` and current Open Work `v1.2.60`.",
)
write(atlas_path, atlas)

# ---------------------------------------------------------------------------
# 4. Manifest: final Open Work hash after all active-route/lifecycle edits.
# ---------------------------------------------------------------------------
manifest_path = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
manifest = json.loads(read(manifest_path))
open_entry = next(row for row in manifest["governing_documents"] if row["document_id"] == "OPEN_WORK")
open_entry["sha256"] = hashlib.sha256(open_work_path.read_bytes()).hexdigest()
write(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

# ---------------------------------------------------------------------------
# 5. Roadmap routing resilience: historical v1.1.x tests stay historical;
#    current pointer and §21 compare against immediate archived v1.2.0.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_roadmap_routing_resilience.py"
s = read(p)
s = s.replace('CURRENT_ROADMAP = DOCS / "05_ROADMAP_v1.2.0.md"', 'CURRENT_ROADMAP = DOCS / "05_ROADMAP_v1.3.0.md"')
s = s.replace('OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"')
s = s.replace('ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"')
s = s.replace('self.assertEqual("05_ROADMAP_v1.2.0.md", roadmap["canonical_filename"])', 'self.assertEqual("05_ROADMAP_v1.3.0.md", roadmap["canonical_filename"])')
s = s.replace('self.assertEqual("docs/00_platform/05_ROADMAP_v1.2.0.md", roadmap["repository_path"])', 'self.assertEqual("docs/00_platform/05_ROADMAP_v1.3.0.md", roadmap["repository_path"])')
s = s.replace('self.assertEqual("02_OPEN_WORK_v1.2.59.md", open_work["canonical_filename"])', 'self.assertEqual("02_OPEN_WORK_v1.2.60.md", open_work["canonical_filename"])')
s = s.replace('current_route = "05_ROADMAP_v1.2.0.md"', 'current_route = "05_ROADMAP_v1.3.0.md"')
s = s.replace(
    "        self.assertEqual(7, self.open_work.count(current_route))\n        self.assertEqual(6, self.atlas.count(current_route))",
    "        self.assertIn(current_route, self.open_work)\n        self.assertIn(current_route, self.atlas)",
)
s = s.replace('self.assertEqual("1.2.0", governing["ROADMAP"]["semver"])', 'self.assertEqual("1.3.0", governing["ROADMAP"]["semver"])')
s = s.replace(
    "            predecessor = _section_bytes(ROADMAP, heading, next_heading)",
    '            predecessor = _section_bytes(DOCS / "archive" / "05_ROADMAP_v1.2.0.md", heading, next_heading)',
    1,
)
write(p, s)

# ---------------------------------------------------------------------------
# 6. Roadmap amendment current pointer only.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_roadmap_amendment.py"
s = read(p)
s = s.replace('ROADMAP_CURRENT = DOCS / "05_ROADMAP_v1.2.0.md"', 'ROADMAP_CURRENT = DOCS / "05_ROADMAP_v1.3.0.md"')
s = s.replace('self.assertEqual("1.2.0", roadmap_entry["semver"])', 'self.assertEqual("1.3.0", roadmap_entry["semver"])')
write(p, s)

# ---------------------------------------------------------------------------
# 7. Authority routing successors: current pointers move; historical
#    predecessor fixtures remain untouched. Add explicit v1.3.0 semantic guard.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_authority_routing_successors.py"
s = read(p)
s = s.replace('"OPEN_WORK": "02_OPEN_WORK_v1.2.59.md"', '"OPEN_WORK": "02_OPEN_WORK_v1.2.60.md"', 1)
s = s.replace('"ROADMAP": "05_ROADMAP_v1.2.0.md"', '"ROADMAP": "05_ROADMAP_v1.3.0.md"', 1)
for old, new in [
    ('DOCS / "02_OPEN_WORK_v1.2.59.md"', 'DOCS / "02_OPEN_WORK_v1.2.60.md"'),
    ('DOCS / "working/DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'DOCS / "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('"working/DELIVERY_ATLAS_WORKING_v0.4.1.md"', '"working/DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.2.0`', 'ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.3.0`'),
    ('current semantic successor `05_ROADMAP_v1.2.0.md`; predecessor `archive/05_ROADMAP_v1.1.5.md`', 'current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `archive/05_ROADMAP_v1.2.0.md`'),
    ('current semantic successor 05_ROADMAP_v1.2.0.md; predecessor archive/05_ROADMAP_v1.1.5.md', 'current semantic successor 05_ROADMAP_v1.3.0.md; predecessor archive/05_ROADMAP_v1.2.0.md'),
    ('self.assertEqual("1.2.59", self.governing["OPEN_WORK"]["semver"])', 'self.assertEqual("1.2.60", self.governing["OPEN_WORK"]["semver"])'),
    ('"docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.1.md", graph_paths', '"docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.2.md", graph_paths'),
    ('"docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", graph_paths', '"docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md", graph_paths'),
]:
    s = s.replace(old, new)

new_test = '''    def test_roadmap_v1_3_0_semantic_successor_is_bounded_to_accepted_surface(self):
        predecessor = _read(DOCS / "archive/05_ROADMAP_v1.2.0.md")
        successor = _read(DOCS / CURRENT_AUTHORITY["ROADMAP"])
        old_packs = _feature_pack_sections(predecessor)
        new_packs = _feature_pack_sections(successor)
        expected_ids = [f"FP-{index:03d}" for index in range(1, 18)]
        self.assertEqual(expected_ids, list(old_packs))
        self.assertEqual(expected_ids, list(new_packs))
        for feature_pack in expected_ids:
            with self.subTest(feature_pack=feature_pack):
                for field in ("Outcome", "Validation Objective", "Validation Objective Type", "Dependencies", "Architecture Authority"):
                    self.assertEqual(
                        _feature_pack_field(old_packs[feature_pack], field),
                        _feature_pack_field(new_packs[feature_pack], field),
                        f"{feature_pack} changed {field}",
                    )
                if feature_pack != "FP-006":
                    self.assertEqual(
                        _feature_pack_field(old_packs[feature_pack], "Affected Domains"),
                        _feature_pack_field(new_packs[feature_pack], "Affected Domains"),
                        f"{feature_pack} changed Affected Domains",
                    )
                if feature_pack not in {"FP-005", "FP-006", "FP-017"}:
                    self.assertEqual(
                        old_packs[feature_pack],
                        new_packs[feature_pack],
                        f"{feature_pack} changed outside accepted Roadmap v1.3.0 semantic edit surface",
                    )

        self.assertEqual(
            "bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261",
            _sha256(DOCS / CURRENT_AUTHORITY["ROADMAP"]),
        )
        self.assertEqual(
            "601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0",
            _sha256(DOCS / "archive/05_ROADMAP_v1.2.0.md"),
        )

'''
marker = "    def test_current_authority_predecessors_are_archived_byte_identically_and_manifested(self):"
if new_test.splitlines()[0].strip() not in s and marker in s:
    s = s.replace(marker, new_test + marker, 1)
write(p, s)

# ---------------------------------------------------------------------------
# 8. Atlas reconciliation current pointers only.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_atlas_reconciliation.py"
s = read(p)
for old, new in [
    ('ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('CURRENT_OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'CURRENT_OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"'),
    ('self.assertIn("v0.4.0 → v0.4.1", self.atlas)', 'self.assertIn("v0.4.1 → v0.4.2", self.atlas)'),
    ('current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.1.md`', 'current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.2.md`'),
    ('self.assertIn("05_ROADMAP_v1.2.0.md", sources)', 'self.assertIn("05_ROADMAP_v1.3.0.md", sources)'),
    ('Roadmap `v1.2.0` and current Open Work `v1.2.59`.', 'Roadmap `v1.3.0` and current Open Work `v1.2.60`.'),
    ('DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('`working/DELIVERY_ATLAS_WORKING_v0.4.1.md`', '`working/DELIVERY_ATLAS_WORKING_v0.4.2.md`'),
    ('`working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`', '`working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md`'),
]:
    s = s.replace(old, new)
write(p, s)

# ---------------------------------------------------------------------------
# 9. HARDEN contract tests: keep v0.5.3 historical normalizer; add current v0.5.4 test.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_harden_02_contract.py"
s = read(p)
s = s.replace('CONTRACT_CURRENT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'CONTRACT_CURRENT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"')
for old, new in [
    ('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", self.readme', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md", self.readme'),
    ('self.assertEqual("1.2.59", current["OPEN_WORK"]["semver"])', 'self.assertEqual("1.2.60", current["OPEN_WORK"]["semver"])'),
    ('"docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", navigation_paths', '"docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md", navigation_paths'),
    ('self.assertEqual("0.5.3", state["status_successor_version"])', 'self.assertEqual("0.5.4", state["status_successor_version"])'),
    ('self.assertEqual("a062bd56e3ae94e815e2991ee00bf133ee9f3b56", state["status_successor_base_sha"])', f'self.assertEqual("{MAIN_SHA}", state["status_successor_base_sha"])'),
]:
    s = s.replace(old, new)

historical_body = '''    def test_v0_5_3_updates_current_route_without_changing_contract_semantics(self):
        historical = (DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md").read_text(encoding="utf-8")
        predecessor = (DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.2.md").read_text(encoding="utf-8")
        self.assertIn("Plan / contract version:** `v0.5.3`", historical)
        self.assertIn("Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md`", historical)
        self.assertIn("02_OPEN_WORK_v1.2.59.md", historical)
        self.assertIn("05_ROADMAP_v1.2.0.md", historical)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.1.md", historical)
        self.assertNotEqual(predecessor, historical)

'''
if "def test_v0_5_3_updates_current_route_without_changing_contract_semantics" in s:
    s = replace_function(s, "test_v0_5_3_updates_current_route_without_changing_contract_semantics", historical_body)
current_test = f'''    def test_v0_5_4_is_current_routing_only_successor(self):
        predecessor = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"
        self.assertTrue(predecessor.is_file())
        self.assertIn("Plan / contract version:** `v0.5.4`", self.current_contract)
        self.assertIn("Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`", self.current_contract)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", self.current_contract)
        self.assertIn("05_ROADMAP_v1.3.0.md", self.current_contract)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.2.md", self.current_contract)
        state = _lifecycle_json(self.current_contract)
        self.assertEqual("0.5.4", state["status_successor_version"])
        self.assertEqual("{MAIN_SHA}", state["status_successor_base_sha"])

'''
if "def test_v0_5_4_is_current_routing_only_successor" not in s:
    s = insert_before_main(s, current_test)
write(p, s)

# ---------------------------------------------------------------------------
# 10. HARDEN execution tests: current routes move; historical Atlas v0.4.1
#     normalizer stays historical and a new current v0.4.2 boundary test is added.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_harden_02_execution.py"
s = read(p)
for old, new in [
    ('OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"'),
    ('CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('ROADMAP = DOCS / "05_ROADMAP_v1.2.0.md"', 'ROADMAP = DOCS / "05_ROADMAP_v1.3.0.md"'),
    ('atlas_path = "working/DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'atlas_path = "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('"working/DELIVERY_ATLAS_WORKING_v0.4.1.md"', '"working/DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('"02_OPEN_WORK_v1.2.59.md"', '"02_OPEN_WORK_v1.2.60.md"'),
    ('"05_ROADMAP_v1.2.0.md"', '"05_ROADMAP_v1.3.0.md"'),
    ('[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.4.1.md)', '[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.4.2.md)'),
    ('CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md', 'CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md'),
]:
    s = s.replace(old, new)

historical_atlas_test = '''    def test_atlas_successor_normalizes_to_route_only_change(self):
        historical = _read(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.4.1.md")
        predecessor = _read(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.4.0.md")
        self.assertIn("v0.4.0 → v0.4.1", historical)
        self.assertIn("02_OPEN_WORK_v1.2.59.md", historical)
        self.assertNotEqual(predecessor, historical)
        self.assertIn("PATCH", historical)
        self.assertIn("non-authoritative", historical)

'''
if "def test_atlas_successor_normalizes_to_route_only_change" in s:
    s = replace_function(s, "test_atlas_successor_normalizes_to_route_only_change", historical_atlas_test)
current_atlas_test = '''    def test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority(self):
        self.assertIn("v0.4.1 → v0.4.2", self.atlas)
        self.assertIn("05_ROADMAP_v1.3.0.md", self.atlas)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", self.atlas)
        self.assertIn("DOES NOT MODIFY PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW", self.atlas)
        self.assertIn("does not amend upstream law or HARDEN-02 contract semantics", self.atlas)

'''
if "def test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority" not in s:
    s = insert_before_main(s, current_atlas_test)
write(p, s)

# ---------------------------------------------------------------------------
# 11. Completion lifecycle + Engineering Standards mutation fixture.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_harden_02_completion_lifecycle.py"
s = read(p)
s = s.replace('OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"')
s = s.replace('CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"')
s = s.replace('`working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`', '`working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md`')
write(p, s)

p = ROOT / "tests" / "test_engineering_standards_promotion.py"
s = read(p).replace('Path("docs/00_platform/02_OPEN_WORK_v1.2.59.md")', 'Path("docs/00_platform/02_OPEN_WORK_v1.2.60.md")')
write(p, s)

# ---------------------------------------------------------------------------
# 12. Product hardening current-route list.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_product_law_hardening.py"
s = read(p)
s = s.replace('"docs/00_platform/02_OPEN_WORK_v1.2.59.md"', '"docs/00_platform/02_OPEN_WORK_v1.2.60.md"')
s = s.replace('"docs/00_platform/05_ROADMAP_v1.2.0.md"', '"docs/00_platform/05_ROADMAP_v1.3.0.md"')
write(p, s)

# ---------------------------------------------------------------------------
# 13. Production audit current routes + HARDEN v0.5.4 lifecycle.
# ---------------------------------------------------------------------------
p = ROOT / "tools" / "foundation_integrity_audit.py"
s = read(p)
for old, new in [
    ('docs/00_platform/02_OPEN_WORK_v1.2.59.md', 'docs/00_platform/02_OPEN_WORK_v1.2.60.md'),
    ('02_OPEN_WORK_v1.2.59.md', '02_OPEN_WORK_v1.2.60.md'),
    ('working/DELIVERY_ATLAS_WORKING_v0.4.1.md', 'working/DELIVERY_ATLAS_WORKING_v0.4.2.md'),
    ('working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md', 'working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md'),
    ('current Atlas v0.4.1', 'current Atlas v0.4.2'),
    ('current HARDEN-02 v0.5.3', 'current HARDEN-02 v0.5.4'),
]:
    s = s.replace(old, new)
s = s.replace(
    '("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3")',
    '("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3", "0.5.4")',
)
s = s.replace(
    'expected_harden_version = "0.5.3" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"',
    'expected_harden_version = "0.5.4" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"',
)
needle = (
    'expected_base_sha = (\n'
    '            "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"\n'
    '            if state.get("status_successor_version") == "0.5.3"'
)
if needle in s:
    replacement = (
        'expected_base_sha = (\n'
        f'            "{MAIN_SHA}"\n'
        '            if state.get("status_successor_version") == "0.5.4"\n'
        '            else "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"\n'
        '            if state.get("status_successor_version") == "0.5.3"'
    )
    s = s.replace(needle, replacement, 1)
write(p, s)

print("PASS9_REPAIR_APPLIED")
print("OPEN_WORK_SHA256", hashlib.sha256(open_work_path.read_bytes()).hexdigest())
print("ROADMAP_SHA256", hashlib.sha256((DOCS / "05_ROADMAP_v1.3.0.md").read_bytes()).hexdigest())
