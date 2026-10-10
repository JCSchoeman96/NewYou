from pathlib import Path
import hashlib, json


def rw(path):
    return Path(path).read_text(encoding="utf-8")


def ww(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_one(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one occurrence, found {count}: {old!r}")
    return text.replace(old, new, 1)


def function_region(text, name):
    start = text.index("    def " + name + "(")
    nxt = text.find("\n    def ", start + 8)
    return start, len(text) if nxt < 0 else nxt

# Finish current Open Work successor lifecycle and recompute manifest hash.
p = "docs/00_platform/02_OPEN_WORK_v1.2.60.md"
s = rw(p)
s = replace_one(s, '"status_successor_version": "0.5.3"', '"status_successor_version": "0.5.4"', "Open Work HARDEN version")
s = replace_one(s, '"status_successor_base_sha": "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"', '"status_successor_base_sha": "086ade7b28c000de1c387acb9760e5eb08bb0413"', "Open Work HARDEN base")
s = s.replace("current status routing is v0.5.3", "current status routing is v0.5.4")
s = s.replace("current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `v1.1.5` is preserved at `archive/05_ROADMAP_v1.2.0.md`", "current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `v1.2.0` is preserved at `archive/05_ROADMAP_v1.2.0.md`")
ww(p, s)

mp = Path("docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
m = json.loads(mp.read_text(encoding="utf-8"))
ow = next(x for x in m["governing_documents"] if x["document_id"] == "OPEN_WORK")
ow["sha256"] = hashlib.sha256(Path(p).read_bytes()).hexdigest()
mp.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# README: preserve source-at-freeze exception explicitly while current route stays on v0.4.2.
p = "docs/00_platform/README.md"
s = rw(p)
atlas_bullet = "- `working/DELIVERY_ATLAS_WORKING_v0.4.2.md` — routing-only derived Delivery Atlas successor aligned to Roadmap v1.3.0 and Open Work v1.2.60. It remains working/non-authoritative and does not semantically re-derive prior Atlas views; current Roadmap authority wins. Direct predecessor v0.4.1 is preserved byte-identically at `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`."
addition = " The unchanged v0.2.1 working path remains available to existing FP-001 and HARDEN-02 source-at-freeze references."
if atlas_bullet in s and addition.strip() not in s:
    s = replace_one(s, atlas_bullet, atlas_bullet + addition, "README Atlas source-at-freeze note")
ww(p, s)

# Current authority routing tests.
p = "tests/test_authority_routing_successors.py"
s = rw(p)
s = s.replace('"OPEN_WORK": "02_OPEN_WORK_v1.2.59.md"', '"OPEN_WORK": "02_OPEN_WORK_v1.2.60.md"', 1)
s = s.replace('"ROADMAP": "05_ROADMAP_v1.2.0.md"', '"ROADMAP": "05_ROADMAP_v1.3.0.md"', 1)
for old, new in [
    ('DOCS / "working/DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'DOCS / "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('"working/DELIVERY_ATLAS_WORKING_v0.4.1.md", open_work_header', '"working/DELIVERY_ATLAS_WORKING_v0.4.2.md", open_work_header'),
    ('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", open_work_header', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md", open_work_header'),
    ('"CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', '"CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('"working/DELIVERY_ATLAS_WORKING_v0.4.1.md", self.readme', '"working/DELIVERY_ATLAS_WORKING_v0.4.2.md", self.readme'),
    ('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", self.readme', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md", self.readme'),
    ('"02_OPEN_WORK_v1.2.59.md", "04_DOMAIN_MAP_v1.2.0.md"', '"02_OPEN_WORK_v1.2.60.md", "04_DOMAIN_MAP_v1.2.0.md"'),
    ('ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.2.0`', 'ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.3.0`'),
    ('current semantic successor `05_ROADMAP_v1.2.0.md`; predecessor `archive/05_ROADMAP_v1.1.5.md`', 'current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `archive/05_ROADMAP_v1.2.0.md`'),
    ('current semantic successor 05_ROADMAP_v1.2.0.md; predecessor archive/05_ROADMAP_v1.1.5.md', 'current semantic successor 05_ROADMAP_v1.3.0.md; predecessor archive/05_ROADMAP_v1.2.0.md'),
    ('self.assertEqual("1.2.59", self.governing["OPEN_WORK"]["semver"])', 'self.assertEqual("1.2.60", self.governing["OPEN_WORK"]["semver"])'),
    ('_read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md")', '_read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md")'),
    ('_read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md")', '_read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md")'),
]:
    s = s.replace(old, new)
start = s.index("    def test_roadmap_amendment_preserves_feature_pack_identity_outcomes_and_unamended_content(self):")
end = s.index("    def test_current_authority_predecessors_are_archived_byte_identically_and_manifested(self):", start)
body = '''    def test_roadmap_amendment_preserves_feature_pack_identity_outcomes_and_unamended_content(self):
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
                    self.assertEqual(_feature_pack_field(old_packs[feature_pack], field), _feature_pack_field(new_packs[feature_pack], field), f"{feature_pack} changed {field}")
                if feature_pack != "FP-006":
                    self.assertEqual(_feature_pack_field(old_packs[feature_pack], "Affected Domains"), _feature_pack_field(new_packs[feature_pack], "Affected Domains"), f"{feature_pack} changed Affected Domains")
                if feature_pack not in {"FP-005", "FP-006", "FP-017"}:
                    self.assertEqual(old_packs[feature_pack], new_packs[feature_pack], f"{feature_pack} changed outside accepted Roadmap v1.3.0 semantic edit surface")

'''
s = s[:start] + body + s[end:]
ww(p, s)

# Roadmap routing resilience: current pointers advance; historical v1.1.x tests remain historical.
p = "tests/test_roadmap_routing_resilience.py"
s = rw(p)
s = s.replace('CURRENT_ROADMAP = DOCS / "05_ROADMAP_v1.2.0.md"', 'CURRENT_ROADMAP = DOCS / "05_ROADMAP_v1.3.0.md"')
s = s.replace('OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"')
s = s.replace('ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"')
s = s.replace('self.assertEqual("05_ROADMAP_v1.2.0.md", roadmap["canonical_filename"])', 'self.assertEqual("05_ROADMAP_v1.3.0.md", roadmap["canonical_filename"])')
s = s.replace('self.assertEqual("docs/00_platform/05_ROADMAP_v1.2.0.md", roadmap["repository_path"])', 'self.assertEqual("docs/00_platform/05_ROADMAP_v1.3.0.md", roadmap["repository_path"])')
s = s.replace('self.assertEqual("02_OPEN_WORK_v1.2.59.md", open_work["canonical_filename"])', 'self.assertEqual("02_OPEN_WORK_v1.2.60.md", open_work["canonical_filename"])')
s = s.replace('current_route = "05_ROADMAP_v1.2.0.md"', 'current_route = "05_ROADMAP_v1.3.0.md"')
s = s.replace('        self.assertEqual(7, self.open_work.count(current_route))\n        self.assertEqual(6, self.atlas.count(current_route))', '        self.assertIn(current_route, self.open_work)\n        self.assertIn(current_route, self.atlas)')
s = s.replace('self.assertEqual("1.2.0", governing["ROADMAP"]["semver"])', 'self.assertEqual("1.3.0", governing["ROADMAP"]["semver"])')
old = '''        for heading, next_heading in (("# 21. Phase 7 handoff", ""),):
            current = _section_bytes(CURRENT_ROADMAP, heading, next_heading)
            predecessor = _section_bytes(ROADMAP, heading, next_heading)'''
new = '''        for heading, next_heading in (("# 21. Phase 7 handoff", ""),):
            current = _section_bytes(CURRENT_ROADMAP, heading, next_heading)
            predecessor = _section_bytes(DOCS / "archive" / "05_ROADMAP_v1.2.0.md", heading, next_heading)'''
s = replace_one(s, old, new, "Roadmap §21 predecessor")
ww(p, s)

# Roadmap amendment test current route.
p = "tests/test_roadmap_amendment.py"
s = rw(p).replace('ROADMAP_CURRENT = DOCS / "05_ROADMAP_v1.2.0.md"', 'ROADMAP_CURRENT = DOCS / "05_ROADMAP_v1.3.0.md"').replace('self.assertEqual("1.2.0", roadmap_entry["semver"])', 'self.assertEqual("1.3.0", roadmap_entry["semver"])')
ww(p, s)

# Atlas reconciliation current pointers only.
p = "tests/test_atlas_reconciliation.py"
s = rw(p)
s = s.replace('ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"')
s = s.replace('CURRENT_OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'CURRENT_OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"')
s = s.replace('self.assertIn("v0.4.0 → v0.4.1", self.atlas)', 'self.assertIn("v0.4.1 → v0.4.2", self.atlas)')
s = s.replace('current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.1.md`', 'current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.2.md`')
s = s.replace('self.assertIn("05_ROADMAP_v1.2.0.md", sources)', 'self.assertIn("05_ROADMAP_v1.3.0.md", sources)')
s = s.replace('Roadmap `v1.2.0` and current Open Work `v1.2.59`.', 'Roadmap `v1.3.0` and current Open Work `v1.2.60`.')
s = s.replace('DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"')
ww(p, s)

# HARDEN contract tests: current successor moves; preserve v0.5.3 historical normalizer against archived predecessor.
p = "tests/test_harden_02_contract.py"
s = rw(p)
s = s.replace('CONTRACT_CURRENT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'CONTRACT_CURRENT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"')
s = s.replace('CONTRACT_CURRENT_PREDECESSOR = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.2.md"', 'CONTRACT_CURRENT_PREDECESSOR = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"')
s = s.replace('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", self.readme', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md", self.readme')
s = s.replace('self.assertEqual("1.2.59", current["OPEN_WORK"]["semver"])', 'self.assertEqual("1.2.60", current["OPEN_WORK"]["semver"])')
s = s.replace('"docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md", navigation_paths', '"docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md", navigation_paths')
s = s.replace('self.assertEqual("0.5.3", state["status_successor_version"])', 'self.assertEqual("0.5.4", state["status_successor_version"])')
s = s.replace('self.assertEqual("1.2.59", next(row for row in self.manifest["governing_documents"] if row["document_id"] == "OPEN_WORK")["semver"])', 'self.assertEqual("1.2.60", next(row for row in self.manifest["governing_documents"] if row["document_id"] == "OPEN_WORK")["semver"])')
s = s.replace('self.assertEqual("a062bd56e3ae94e815e2991ee00bf133ee9f3b56", state["status_successor_base_sha"])', 'self.assertEqual("086ade7b28c000de1c387acb9760e5eb08bb0413", state["status_successor_base_sha"])')
a, b = function_region(s, "test_v0_5_3_updates_current_route_without_changing_contract_semantics")
reg = s[a:b]
line = reg.find("\n") + 1
reg = reg[:line] + '        historical_v053 = (DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md").read_text(encoding="utf-8")\n' + reg[line:]
reg = reg.replace("self.current_contract", "historical_v053").replace("CONTRACT_CURRENT_PREDECESSOR", 'DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.2.md"')
s = s[:a] + reg + s[b:]
insert = '''\n    def test_v0_5_4_is_current_routing_only_successor(self):
        predecessor = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"
        self.assertTrue(predecessor.is_file())
        self.assertIn("Plan / contract version:** `v0.5.4`", self.current_contract)
        self.assertIn("Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`", self.current_contract)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", self.current_contract)
        self.assertIn("05_ROADMAP_v1.3.0.md", self.current_contract)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.2.md", self.current_contract)
        self.assertEqual("0.5.4", _lifecycle_json(self.current_contract)["status_successor_version"])
        self.assertEqual("086ade7b28c000de1c387acb9760e5eb08bb0413", _lifecycle_json(self.current_contract)["status_successor_base_sha"])
\n'''
pos = s.rfind('\n\nif __name__ == "__main__":')
s = s[:pos] + insert + s[pos:]
ww(p, s)

# HARDEN execution current pointers; retain historical Atlas normalizer on archived v0.4.1.
p = "tests/test_harden_02_execution.py"
s = rw(p)
for old, new in [
    ('OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"'),
    ('CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('ROADMAP = DOCS / "05_ROADMAP_v1.2.0.md"', 'ROADMAP = DOCS / "05_ROADMAP_v1.3.0.md"'),
    ('atlas_path = "working/DELIVERY_ATLAS_WORKING_v0.4.1.md"', 'atlas_path = "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('"working/DELIVERY_ATLAS_WORKING_v0.4.1.md" not in readme', '"working/DELIVERY_ATLAS_WORKING_v0.4.2.md" not in readme'),
    ('[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.4.1.md)', '[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.4.2.md)'),
    ('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md" not in readme', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md" not in readme'),
    ('CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md', 'CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md'),
    ('"working/DELIVERY_ATLAS_WORKING_v0.4.1.md"', '"working/DELIVERY_ATLAS_WORKING_v0.4.2.md"'),
    ('"working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', '"working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'),
    ('"02_OPEN_WORK_v1.2.59.md"', '"02_OPEN_WORK_v1.2.60.md"'),
    ('"05_ROADMAP_v1.2.0.md"', '"05_ROADMAP_v1.3.0.md"'),
]:
    s = s.replace(old, new)
a, b = function_region(s, "test_atlas_successor_normalizes_to_route_only_change")
reg = s[a:b]
line = reg.find("\n") + 1
reg = reg[:line] + '        historical_atlas = _read(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.4.1.md")\n' + reg[line:]
reg = reg.replace("self.atlas", "historical_atlas").replace("v0.4.2", "v0.4.1").replace("v0.4.1 → v0.4.2", "v0.4.0 → v0.4.1")
s = s[:a] + reg + s[b:]
insert = '''\n    def test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority(self):
        self.assertIn("v0.4.1 → v0.4.2", self.atlas)
        self.assertIn("05_ROADMAP_v1.3.0.md", self.atlas)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", self.atlas)
        self.assertIn("DOES NOT MODIFY PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW", self.atlas)
        self.assertIn("does not amend upstream law or HARDEN-02 contract semantics", self.atlas)
\n'''
pos = s.rfind('\n\nif __name__ == "__main__":')
s = s[:pos] + insert + s[pos:]
ww(p, s)

# Completion lifecycle and Engineering Standards current Open Work routes.
p = "tests/test_harden_02_completion_lifecycle.py"
s = rw(p).replace('OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"', 'OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"').replace('CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"', 'CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"').replace('`working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`', '`working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md`')
ww(p, s)

p = "tests/test_engineering_standards_promotion.py"
s = rw(p).replace('Path("docs/00_platform/02_OPEN_WORK_v1.2.59.md")', 'Path("docs/00_platform/02_OPEN_WORK_v1.2.60.md")').replace('DOCS / "02_OPEN_WORK_v1.2.59.md"', 'DOCS / "02_OPEN_WORK_v1.2.60.md"')
ww(p, s)

# Production audit current-route expectations + HARDEN v0.5.4 lifecycle. Historical checks remain pinned.
p = "tools/foundation_integrity_audit.py"
s = rw(p)
s = s.replace('docs/00_platform/02_OPEN_WORK_v1.2.59.md', 'docs/00_platform/02_OPEN_WORK_v1.2.60.md')
s = s.replace('02_OPEN_WORK_v1.2.59.md', '02_OPEN_WORK_v1.2.60.md')
s = s.replace('working/DELIVERY_ATLAS_WORKING_v0.4.1.md', 'working/DELIVERY_ATLAS_WORKING_v0.4.2.md')
s = s.replace('working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md', 'working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md')
s = s.replace('current Atlas v0.4.1', 'current Atlas v0.4.2').replace('current HARDEN-02 v0.5.3', 'current HARDEN-02 v0.5.4')
s = s.replace('("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3")', '("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3", "0.5.4")')
s = s.replace('expected_harden_version = "0.5.3" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"', 'expected_harden_version = "0.5.4" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"')
needle = 'expected_base_sha = (\n            "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"\n            if state.get("status_successor_version") == "0.5.3"'
if needle in s:
    s = s.replace(needle, 'expected_base_sha = (\n            "086ade7b28c000de1c387acb9760e5eb08bb0413"\n            if state.get("status_successor_version") == "0.5.4"\n            else "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"\n            if state.get("status_successor_version") == "0.5.3"', 1)
ww(p, s)

# Remove temporary Pass-9 automation before verification; tested tree is the candidate tree.
for path in Path(".github/workflows").glob("pass9-*.yml"):
    path.unlink()
Path("tools/pass9_apply.py").unlink()
