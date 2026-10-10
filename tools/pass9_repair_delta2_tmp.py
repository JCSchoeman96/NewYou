from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MAIN='086ade7b28c000de1c387acb9760e5eb08bb0413'

def r(p): return Path(p).read_text(encoding='utf-8')
def w(p,s): Path(p).write_text(s,encoding='utf-8')
def replace_func(s,name,body):
    a=s.find(f'    def {name}(')
    if a<0: raise AssertionError(name)
    b=s.find('\n    def ',a+8)
    if b<0: b=s.find('\n\nif __name__',a)
    if b<0: b=len(s)
    return s[:a]+body.rstrip()+'\n'+s[b:]

def ensure_transition(s,old,new,label):
    old_count=s.count(old)
    new_count=s.count(new)
    if old_count == 1 and new_count == 0:
        return s.replace(old,new,1)
    if old_count == 0 and new_count == 1:
        return s
    raise AssertionError(f'{label}: expected one old→new transition or one already-new marker; old={old_count}, new={new_count}')

# 1. Anchor CURRENT_AUTHORITY itself, while accepting a prior repair layer that already advanced it.
p=ROOT/'tests/test_authority_routing_successors.py'; s=r(p)
s=ensure_transition(s,
    '    "OPEN_WORK": "02_OPEN_WORK_v1.2.59.md",\n    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",',
    '    "OPEN_WORK": "02_OPEN_WORK_v1.2.60.md",\n    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",',
    'CURRENT_AUTHORITY OPEN_WORK')
s=ensure_transition(s,
    '    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.2.0.md",\n    "ROADMAP": "05_ROADMAP_v1.2.0.md",',
    '    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.2.0.md",\n    "ROADMAP": "05_ROADMAP_v1.3.0.md",',
    'CURRENT_AUTHORITY ROADMAP')
w(p,s)

# 2. HARDEN v0.5.4 must carry its own current lifecycle successor metadata, not only a new header.
p=ROOT/'docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md'; s=r(p)
s=ensure_transition(s,'"status_successor_version": "0.5.3"','"status_successor_version": "0.5.4"','HARDEN lifecycle version')
s=ensure_transition(s,
    '"status_successor_base_sha": "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"',
    f'"status_successor_base_sha": "{MAIN}"',
    'HARDEN lifecycle base SHA')
s=s.replace('The governing route is recorded in Open Work v1.2.59.','The governing route is recorded in Open Work v1.2.60.',1)
s=s.replace('Current Open Work v1.2.59 records Communications dossier v0.1.0','Current Open Work v1.2.60 records Communications dossier v0.1.0',1)
w(p,s)

# 3. New HARDEN current-successor test checks the actual v0.5.4 file.
p=ROOT/'tests/test_harden_02_contract.py'; s=r(p)
body=f'''    def test_v0_5_4_is_current_routing_only_successor(self):
        current = (DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md").read_text(encoding="utf-8")
        predecessor = DOCS / "archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"
        self.assertTrue(predecessor.is_file())
        self.assertIn("Plan / contract version:** `v0.5.4`", current)
        self.assertIn("Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`", current)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", current)
        self.assertIn("05_ROADMAP_v1.3.0.md", current)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.2.md", current)
        self.assertIn('"status_successor_version": "0.5.4"', current)
        self.assertIn('"status_successor_base_sha": "{MAIN}"', current)
'''
s=replace_func(s,'test_v0_5_4_is_current_routing_only_successor',body)
w(p,s)

# 4. Production audit accepts exactly one additional completed routing successor: v0.5.4.
p=ROOT/'tools/foundation_integrity_audit.py'; s=r(p)
old='        "successor_versions": ("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3"),'
new='        "successor_versions": ("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3", "0.5.4"),'
s=ensure_transition(s,old,new,'H02 complete successor_versions')
old_version='expected_harden_version = "0.5.3" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"'
new_version='expected_harden_version = "0.5.4" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"'
s=ensure_transition(s,old_version,new_version,'expected HARDEN version')
old_base='''        expected_base_sha = (
            "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"'''
new_base=f'''        expected_base_sha = (
            "{MAIN}"
            if state.get("status_successor_version") == "0.5.4"
            else "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"'''
s=ensure_transition(s,old_base,new_base,'HARDEN base SHA routing')
w(p,s)
print('PASS9_DELTA2_APPLIED')
