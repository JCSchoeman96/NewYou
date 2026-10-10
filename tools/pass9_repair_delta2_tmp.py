from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

def r(p): return Path(p).read_text(encoding='utf-8')
def w(p,s): Path(p).write_text(s,encoding='utf-8')
def replace_func(s,name,body):
    a=s.find(f'    def {name}(')
    if a<0: raise AssertionError(name)
    b=s.find('\n    def ',a+8)
    if b<0: b=s.find('\n\nif __name__',a)
    if b<0: b=len(s)
    return s[:a]+body.rstrip()+'\n'+s[b:]

# 1. Force current authority mapping to the promoted routes.
p=ROOT/'tests/test_authority_routing_successors.py'; s=r(p)
s,n=re.subn(r'(?m)^(\s*"OPEN_WORK":\s*)"02_OPEN_WORK_v1\.2\.59\.md"',r'\1"02_OPEN_WORK_v1.2.60.md"',s)
if n<1: raise AssertionError('CURRENT_AUTHORITY OPEN_WORK route not found')
s,n2=re.subn(r'(?m)^(\s*"ROADMAP":\s*)"05_ROADMAP_v1\.2\.0\.md"',r'\1"05_ROADMAP_v1.3.0.md"',s)
if n2<1: raise AssertionError('CURRENT_AUTHORITY ROADMAP route not found')
w(p,s)

# 2. New HARDEN current-successor test uses content assertions only; lifecycle coherence is covered by dedicated suites.
p=ROOT/'tests/test_harden_02_contract.py'; s=r(p)
body='''    def test_v0_5_4_is_current_routing_only_successor(self):
        current = (DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md").read_text(encoding="utf-8")
        predecessor = DOCS / "archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md"
        self.assertTrue(predecessor.is_file())
        self.assertIn("Plan / contract version:** `v0.5.4`", current)
        self.assertIn("Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`", current)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", current)
        self.assertIn("05_ROADMAP_v1.3.0.md", current)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.2.md", current)
        self.assertIn('"status_successor_version": "0.5.4"', current)
        self.assertIn('"status_successor_base_sha": "086ade7b28c000de1c387acb9760e5eb08bb0413"', current)
'''
s=replace_func(s,'test_v0_5_4_is_current_routing_only_successor',body)
w(p,s)

# 3. Production audit: structurally extend only the COMPLETE/CERTIFIED successor versions.
p=ROOT/'tools/foundation_integrity_audit.py'; s=r(p)
pattern=(r'("COMPLETE / CERTIFIED":\s*\{\s*\n\s*"matrix":\s*"COMPLETE_CERTIFIED",\s*\n\s*'
         r'"successor_versions":\s*\()([^\)]*)(\),)')
m=re.search(pattern,s)
if not m: raise AssertionError('complete successor_versions tuple not found')
versions=m.group(2)
if '"0.5.4"' not in versions:
    versions=versions.rstrip()+', "0.5.4"'
s=s[:m.start(2)]+versions+s[m.end(2):]
# Ensure current certified contract metadata check follows v0.5.4.
s=s.replace('expected_harden_version = "0.5.3" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"','expected_harden_version = "0.5.4" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"')
# Ensure v0.5.4 base SHA is recognized before the historical v0.5.3 branch.
needle='''        expected_base_sha = (
            "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"'''
if needle in s:
    s=s.replace(needle,'''        expected_base_sha = (
            "086ade7b28c000de1c387acb9760e5eb08bb0413"
            if state.get("status_successor_version") == "0.5.4"
            else "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"''',1)
w(p,s)
print('PASS9_DELTA2_APPLIED')
