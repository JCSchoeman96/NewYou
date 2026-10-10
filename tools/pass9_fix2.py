from pathlib import Path


def read(path): return Path(path).read_text(encoding='utf-8')
def write(path, text): Path(path).write_text(text, encoding='utf-8')

def replace_all(path, pairs):
    s = read(path)
    for old, new in pairs:
        s = s.replace(old, new)
    write(path, s)

def replace_func(path, name, body):
    s = read(path)
    start = s.index('    def ' + name + '(')
    nxt = s.find('\n    def ', start + 8)
    if nxt < 0: nxt = len(s)
    s = s[:start] + body.rstrip() + '\n\n' + s[nxt+1:]
    write(path, s)

# Current Open Work §9 must route the new current Atlas/Roadmap/HARDEN successors.
p = 'docs/00_platform/02_OPEN_WORK_v1.2.60.md'
s = read(p)
a = s.index('# 9. Immediate Next Action')
b = s.index('# 10. Minimal Tools', a)
sec = s[a:b]
sec = sec.replace('working/DELIVERY_ATLAS_WORKING_v0.4.1.md', 'working/DELIVERY_ATLAS_WORKING_v0.4.2.md')
sec = sec.replace('current semantic successor 05_ROADMAP_v1.2.0.md; predecessor archive/05_ROADMAP_v1.1.5.md', 'current semantic successor 05_ROADMAP_v1.3.0.md; predecessor archive/05_ROADMAP_v1.2.0.md')
sec = sec.replace('current semantic successor `05_ROADMAP_v1.2.0.md`; predecessor `archive/05_ROADMAP_v1.1.5.md`', 'current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `archive/05_ROADMAP_v1.2.0.md`')
sec = sec.replace('working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md', 'working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md')
s = s[:a] + sec + s[b:]
write(p, s)

# Derived Atlas explicitly preserves HARDEN semantics.
p = 'docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.2.md'
s = read(p)
needle = 'No Feature Pack, Domain, gate, proof class or implementation permission is created or changed here.'
if needle in s and 'does not amend HARDEN-02 contract semantics' not in s.split('## v0.4.1 Patch Scope',1)[0]:
    s = s.replace(needle, 'It does not amend HARDEN-02 contract semantics. ' + needle, 1)
write(p, s)

# Authority-routing tests: advance only current-route assertions and direct current reads.
p = 'tests/test_authority_routing_successors.py'
s = read(p)
s = s.replace('self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.1.md", _section(harden, "### CURRENT DERIVED EVIDENCE", "### HISTORICAL AUTHORITY / WORKING EVIDENCE"))', 'self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.2.md", _section(harden, "### CURRENT DERIVED EVIDENCE", "### HISTORICAL AUTHORITY / WORKING EVIDENCE"))')
s = s.replace('self.assertIn("docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.1.md", graph_paths)', 'self.assertIn("docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.2.md", graph_paths)')
s = s.replace('_read(DOCS / "02_OPEN_WORK_v1.2.59.md")', '_read(DOCS / "02_OPEN_WORK_v1.2.60.md")')
s = s.replace('self.assertIn("ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.3.0`", readme)', 'self.assertIn("`05_ROADMAP_v1.3.0.md`", _section(readme, "## Default Agent Context", "## Active Working Artifacts"))')
write(p, s)

# Roadmap amendment current semantic version.
replace_all('tests/test_roadmap_amendment.py', [('self.assertEqual("1.2.0", current["ROADMAP"]["semver"])','self.assertEqual("1.3.0", current["ROADMAP"]["semver"])')])

# Atlas tests: test v0.4.2 routing where it actually lives, not historical §26.18 wording.
replace_func('tests/test_atlas_reconciliation.py', 'test_current_source_routing_refreshed', '''    def test_current_source_routing_refreshed(self):
        sources = _section(self.atlas, "## 1.1 Authority hierarchy", "## 1.2 Purpose")
        self.assertIn("05_ROADMAP_v1.3.0.md", sources)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", sources)
        self.assertIn("current Roadmap authority", self.atlas.split("## v0.4.1 Patch Scope", 1)[0])
        self.assertIn("source-at-freeze", self.atlas)
''')

# Preserve the historical v0.5.3 regression as historical, and add a current v0.5.4 route assertion in the correct class.
replace_func('tests/test_harden_02_contract.py', 'test_v0_5_3_updates_current_route_without_changing_contract_semantics', '''    def test_v0_5_3_updates_current_route_without_changing_contract_semantics(self):
        historical = (DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md").read_text(encoding="utf-8")
        predecessor = (DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.5.2.md").read_text(encoding="utf-8")
        self.assertIn("Plan / contract version:** `v0.5.3`", historical)
        self.assertIn("Communications dossier v0.1.0 is COMPLETE / CERTIFIED / CURRENT", historical)
        self.assertIn("Plan / contract version:** `v0.5.2`", predecessor)
        self.assertNotEqual(historical, predecessor)
        self.assertIn("original v0.4.0 semantics are certified", historical)
        self.assertIn("HARDEN-02 execution **COMPLETE / CERTIFIED**", historical)
''')
# Remove wrongly inserted test if present in FoundationIntegrityWorkflowTests.
s = read('tests/test_harden_02_contract.py')
marker = '    def test_v0_5_4_is_current_routing_only_successor(self):'
if marker in s:
    start = s.index(marker)
    nxt = s.find('\n    def ', start + len(marker))
    if nxt < 0: nxt = s.rfind('\n\nif __name__')
    s = s[:start] + s[nxt+1:]
# Insert into Harden02ContractRecoveryTests immediately before contract-stage-stop test.
insert_at = s.index('    def test_contract_stage_stop_tracks_completed_lifecycle_without_weakening_gates(self):')
method = '''    def test_v0_5_4_is_current_routing_only_successor(self):
        self.assertIn("Plan / contract version:** `v0.5.4`", self.current_contract)
        self.assertIn("Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`", self.current_contract)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", self.current_contract)
        self.assertIn("05_ROADMAP_v1.3.0.md", self.current_contract)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.4.2.md", self.current_contract)
        state = _lifecycle_json(self.current_contract)
        self.assertEqual("0.5.4", state["status_successor_version"])
        self.assertEqual("086ade7b28c000de1c387acb9760e5eb08bb0413", state["status_successor_base_sha"])

'''
s = s[:insert_at] + method + s[insert_at:]
write('tests/test_harden_02_contract.py', s)

# HARDEN execution: current status version and historical Atlas normalizer.
p = 'tests/test_harden_02_execution.py'
s = read(p)
s = s.replace('self.assertEqual("0.5.3", state.get("status_successor_version"))', 'self.assertEqual("0.5.4", state.get("status_successor_version"))')
# The historical normalizer must continue to exercise archived v0.4.1 exactly.
replace = 'historical_atlas = _read(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.4.1.md")'
if replace in s:
    # Undo the accidental version-token rewrite inside only that function by replacing the full function.
    pass
write(p, s)
replace_func(p, 'test_atlas_successor_normalizes_to_route_only_change', '''    def test_atlas_successor_normalizes_to_route_only_change(self):
        current = _read(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.4.1.md")
        predecessor = _read(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.4.0.md")
        self.assertIn("v0.4.0 → v0.4.1", current)
        self.assertIn("02_OPEN_WORK_v1.2.59.md", current)
        self.assertIn("working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", current)
        self.assertNotEqual(current, predecessor)
''')
# Remove wrongly inserted current Atlas method if present and reinsert near another instance method; use path directly, not self.atlas.
s = read(p)
marker = '    def test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority(self):'
if marker in s:
    start = s.index(marker); nxt = s.find('\n    def ', start + len(marker))
    if nxt < 0: nxt = s.rfind('\n\nif __name__')
    s = s[:start] + s[nxt+1:]
pos = s.index('    def test_i01_single_unambiguous_next_and_valid_lifecycle_record(self):')
method = '''    def test_current_atlas_v0_4_2_routes_new_authority_without_becoming_authority(self):
        atlas = _read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md")
        self.assertIn("v0.4.1 → v0.4.2", atlas)
        self.assertIn("05_ROADMAP_v1.3.0.md", atlas)
        self.assertIn("02_OPEN_WORK_v1.2.60.md", atlas)
        self.assertIn("DOES NOT MODIFY PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW", atlas)
        self.assertIn("does not amend HARDEN-02 contract semantics", atlas)

'''
s = s[:pos] + method + s[pos:]
write(p, s)

# Foundation lifecycle code: make v0.5.4 a supported completed routing successor.
p = 'tools/foundation_integrity_audit.py'
s = read(p)
s = s.replace('"successor_versions": ("0.5.3",),', '"successor_versions": ("0.5.3", "0.5.4"),')
s = s.replace('expected_harden_version = "0.5.3" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"', 'expected_harden_version = "0.5.4" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"')
write(p, s)

# The deterministic patch must delete this second-stage helper too before verification/commit.
Path('tools/pass9_fix2.py').unlink()
