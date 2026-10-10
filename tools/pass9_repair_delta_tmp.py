from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs' / '00_platform'
MAIN = '086ade7b28c000de1c387acb9760e5eb08bb0413'

def r(p): return Path(p).read_text(encoding='utf-8')
def w(p,s): Path(p).write_text(s,encoding='utf-8')

def replace_func(s,name,body):
    a=s.find(f'    def {name}(')
    if a<0: raise AssertionError(name)
    b=s.find('\n    def ',a+8)
    if b<0: b=s.find('\n\nif __name__',a)
    if b<0: b=len(s)
    return s[:a]+body.rstrip()+'\n'+s[b:]

# Roadmap amendment suite: current successor expectations only.
p=ROOT/'tests/test_roadmap_amendment.py'; s=r(p)
s=s.replace('self.assertTrue("05_ROADMAP_v1.2.0.md" in self.readme, "README current Roadmap")','self.assertTrue("05_ROADMAP_v1.3.0.md" in self.readme, "README current Roadmap")')
s=s.replace('self.assertEqual("1.2.0", current["ROADMAP"]["semver"])','self.assertEqual("1.3.0", current["ROADMAP"]["semver"])')
s=s.replace('self.assertEqual("docs/00_platform/05_ROADMAP_v1.2.0.md", current["ROADMAP"]["repository_path"])','self.assertEqual("docs/00_platform/05_ROADMAP_v1.3.0.md", current["ROADMAP"]["repository_path"])')
w(p,s)

# Authority routing suite: move only active/current expectations and bound Roadmap v1.3.0 semantics.
p=ROOT/'tests/test_authority_routing_successors.py'; s=r(p)
s=s.replace('"OPEN_WORK": "02_OPEN_WORK_v1.2.59.md"','"OPEN_WORK": "02_OPEN_WORK_v1.2.60.md"')
s=s.replace('"ROADMAP": "05_ROADMAP_v1.2.0.md"','"ROADMAP": "05_ROADMAP_v1.3.0.md"')
s=s.replace('current = _read(DOCS / "02_OPEN_WORK_v1.2.59.md")','current = _read(DOCS / "02_OPEN_WORK_v1.2.60.md")')
s=s.replace('Current Atlas is derived / non-authoritative at working/DELIVERY_ATLAS_WORKING_v0.4.1.md','Current Atlas is derived / non-authoritative at working/DELIVERY_ATLAS_WORKING_v0.4.2.md')
s=s.replace('"CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"','"CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md"')
# Current Atlas lineage test: preserve pinned v0.2.1 evidence, advance immediate routing predecessor only.
old='''    def test_current_open_work_atlas_lineage_distinguishes_current_predecessor_and_pinned_source(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.60.md")
        expected = OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE.replace(
            "working/DELIVERY_ATLAS_WORKING_v0.3.1.md", "working/DELIVERY_ATLAS_WORKING_v0.4.1.md"
        ).replace(
            "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.4.0.md"
        )
        _validate_open_work_atlas_status_line(current, expected)
        self.assertIn("current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.1.md`", expected)
        self.assertIn("immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`", expected)
        self.assertIn("pinned v0.2.1 source-at-freeze artifacts remain preserved", expected)
        self.assertNotRegex(
            expected,
            r"current Atlas `working/DELIVERY_ATLAS_WORKING_v0\\.3\\.4\\.md`; predecessor `archive/DELIVERY_ATLAS_WORKING_v0\\.2\\.1\\.md`",
        )
        pinned_working = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        pinned_archive = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        self.assertTrue(pinned_working.is_file())
        self.assertTrue(pinned_archive.is_file())
        self.assertEqual(_sha256(pinned_working), _sha256(pinned_archive))
'''
new='''    def test_current_open_work_atlas_lineage_distinguishes_current_predecessor_and_pinned_source(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.60.md")
        expected = OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE.replace(
            "working/DELIVERY_ATLAS_WORKING_v0.3.1.md", "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"
        ).replace(
            "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.4.1.md"
        )
        _validate_open_work_atlas_status_line(current, expected)
        self.assertIn("current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.2.md`", expected)
        self.assertIn("immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`", expected)
        self.assertIn("pinned v0.2.1 source-at-freeze artifacts remain preserved", expected)
        pinned_working = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        pinned_archive = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        self.assertTrue(pinned_working.is_file())
        self.assertTrue(pinned_archive.is_file())
        self.assertEqual(_sha256(pinned_working), _sha256(pinned_archive))
'''
if old in s: s=s.replace(old,new,1)
else: s=replace_func(s,'test_current_open_work_atlas_lineage_distinguishes_current_predecessor_and_pinned_source',new)
# Its malformed-line companion must use the same current lineage.
s=s.replace('"working/DELIVERY_ATLAS_WORKING_v0.3.1.md", "working/DELIVERY_ATLAS_WORKING_v0.4.1.md"','"working/DELIVERY_ATLAS_WORKING_v0.3.1.md", "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"')
s=s.replace('"archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.4.0.md"','"archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.4.1.md"')
s=s.replace('immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`','immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`')
# Replace the pre-v1.3 preservation method with an immediate-predecessor guard matching accepted edit surface.
body='''    def test_roadmap_amendment_preserves_feature_pack_identity_outcomes_and_unamended_content(self):
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
s=replace_func(s,'test_roadmap_amendment_preserves_feature_pack_identity_outcomes_and_unamended_content',body)
w(p,s)

# HARDEN contract current expectations; direct file reads avoid class-fixture coupling.
p=ROOT/'tests/test_harden_02_contract.py'; s=r(p)
s=s.replace('self.assertEqual("1.2.59", next(row for row in self.manifest["governing_documents"] if row["document_id"] == "OPEN_WORK")["semver"])','self.assertEqual("1.2.60", next(row for row in self.manifest["governing_documents"] if row["document_id"] == "OPEN_WORK")["semver"])')
body=f'''    def test_v0_5_4_is_current_routing_only_successor(self):
        current = (DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md").read_text(encoding="utf-8")
        predecessor = DOCS / "archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"
        self.assertTrue(predecessor.is_file())
        self.assertIn("Plan / contract version:** `v0.5.4`", current)
        self.assertIn("Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`", current)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", current)
        self.assertIn("05_ROADMAP_v1.3.0.md", current)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.2.md", current)
        state = _lifecycle_json(current)
        self.assertEqual("0.5.4", state["status_successor_version"])
        self.assertEqual("{MAIN}", state["status_successor_base_sha"])
'''
if 'def test_v0_5_4_is_current_routing_only_successor' in s: s=replace_func(s,'test_v0_5_4_is_current_routing_only_successor',body)
w(p,s)

# HARDEN execution current literals + direct Atlas read for the new current test.
p=ROOT/'tests/test_harden_02_execution.py'; s=r(p)
s=s.replace('self.assertEqual("0.5.3", state.get("status_successor_version"))','self.assertEqual("0.5.4", state.get("status_successor_version"))')
s=s.replace('current semantic successor 05_ROADMAP_v1.2.0.md','current semantic successor 05_ROADMAP_v1.3.0.md')
body='''    def test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority(self):
        atlas = _read(DOCS / "working/DELIVERY_ATLAS_WORKING_v0.4.2.md")
        self.assertIn("v0.4.1 → v0.4.2", atlas)
        self.assertIn("05_ROADMAP_v1.3.0.md", atlas)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", atlas)
        self.assertIn("DOES NOT MODIFY PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW", atlas)
        self.assertIn("does not amend upstream law or HARDEN-02 contract semantics", atlas)
'''
if 'def test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority' in s: s=replace_func(s,'test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority',body)
w(p,s)

# Production audit: robustly add v0.5.4 to completed HARDEN successor set and base SHA map.
p=ROOT/'tools/foundation_integrity_audit.py'; s=r(p)
s=s.replace('"successor_versions": ("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3"),','"successor_versions": ("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3", "0.5.4"),')
s=s.replace('expected_harden_version = "0.5.3" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"','expected_harden_version = "0.5.4" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"')
needle='''        expected_base_sha = (
            "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"'''
repl=f'''        expected_base_sha = (
            "{MAIN}"
            if state.get("status_successor_version") == "0.5.4"
            else "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"'''
if needle in s: s=s.replace(needle,repl,1)
w(p,s)

print('PASS9_DELTA_APPLIED')
