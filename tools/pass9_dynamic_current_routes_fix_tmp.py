from pathlib import Path

# Scratch-only verifier transformation; deleted before retained-tree tests run.
path = Path(__file__).with_name("pass9_dynamic_current_routes_tmp.py")
text = path.read_text(encoding="utf-8")
text = text.replace(
    'old_atlas_bullet = next(line for line in readme.splitlines() if line.startswith("- `working/DELIVERY_ATLAS_WORKING_v0.4.1.md`"))',
    'old_atlas_bullet = next(line for line in readme.splitlines() if line.startswith("- `working/DELIVERY_ATLAS_WORKING_v0.4."))',
    1,
)
text = text.replace(
    'old_harden_bullet = next(line for line in readme.splitlines() if line.startswith("- `working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`"))',
    'old_harden_bullet = next(line for line in readme.splitlines() if line.startswith("- `working/HARDEN-02_CONTRACT_WORKING_v0.5."))',
    1,
)
text = text.replace(
    '    "## 22.",\n    (\n        ("Open Work v1.2.59", "Open Work v1.2.60"),',
    '    "PR #67 lifecycle evidence:",\n    (\n        ("Open Work v1.2.59", "Open Work v1.2.60"),',
    1,
)

# Append only evidence-backed root corrections discovered by the first meaningful RED run.
text += r'''

# ---------------------------------------------------------------------------
# D. RED-run root corrections: preserve history, retain explicit FP-001 status,
# make synthetic FIA fixtures fail closed rather than crash, and advance only
# tests that mean "current".
# ---------------------------------------------------------------------------

# D1. Atlas v0.4.2 is routing-only. Preserve the historical v0.3.0 reconciliation
# snapshot, while carrying the explicit current FP-001 status semantics forward.
atlas_path = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"
atlas = read(atlas_path)
lines = atlas.splitlines()
for index, line in enumerate(lines):
    if line.startswith("- **Current content state:**"):
        lines[index] = (
            "- **Current content state:** ATLAS-01 through ATLAS-11 remain complete at their recorded "
            "source-at-freeze scope as derived navigation. This `v0.4.2` successor routes current authority "
            "to Roadmap v1.3.0 and Open Work v1.2.60 only. It does not semantically re-derive capability, "
            "Domain or Feature Pack views. Where an older Atlas view differs from the bounded FP-006 Research "
            "& Feedback activation in Roadmap v1.3.0, the current Roadmap wins. FP-001 PMR reconciliation "
            "remains COMPLETE / CERTIFIED; Identity dossier v0.1.4 is CERTIFIED / CURRENT; Communications JIT "
            "Domain Dossier v0.1.0 remains COMPLETE / CERTIFIED / CURRENT; Communications finalisation remains "
            "BLOCKED / STOP. This successor does not amend upstream law or HARDEN-02 contract semantics, "
            "authorise Phase 7C, finalise proof classification or authorise implementation."
        )
        break
else:
    raise AssertionError("Atlas current-content-state header missing")
atlas = "\n".join(lines) + ("\n" if atlas.endswith("\n") else "")

hist_start = atlas.index("## 26.18 ATLAS reconciliation (`v0.3.0`) completion standard")
hist_end = atlas.index("## 26.19 ATLAS reconciliation review protocol", hist_start)
hist = atlas[hist_start:hist_end]
hist = hist.replace(
    "Roadmap `v1.3.0` and current Open Work `v1.2.60`",
    "Roadmap `v1.2.0` and current Open Work `v1.2.59`",
)
atlas = atlas[:hist_start] + hist + atlas[hist_end:]
write(atlas_path, atlas)

# D2. FIA synthetic manifests may intentionally omit current Open Work. Defaults
# convert that condition into findings rather than an UnboundLocalError.
p = ROOT / "tools" / "foundation_integrity_audit.py"
s = read(p)
route_anchor = (
    '    atlas_working_ref = current_atlas_route.removeprefix("docs/00_platform/")\n'
    '    harden_working_ref = current_harden_route.removeprefix("docs/00_platform/")\n\n'
    '    current_entries = ['
)
route_replacement = (
    '    atlas_working_ref = current_atlas_route.removeprefix("docs/00_platform/")\n'
    '    harden_working_ref = current_harden_route.removeprefix("docs/00_platform/")\n'
    '    current_open_work_filename = ""\n'
    '    current_open_work_semver = ""\n\n'
    '    current_entries = ['
)
if route_anchor not in s:
    raise AssertionError("FIA current-route default anchor missing")
s = s.replace(route_anchor, route_replacement, 1)

old_routes = '''    readme_active_routes = (
        "4. " + chr(96) + str(current_open_work_filename) + chr(96),
        chr(96) + atlas_working_ref + chr(96),
        chr(96) + harden_working_ref + chr(96),
        chr(96) + "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md" + chr(96),
        chr(96) + "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md" + chr(96),
        chr(96) + "working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md" + chr(96),
    )
'''
new_routes = '''    readme_active_routes = [
        chr(96) + atlas_working_ref + chr(96),
        chr(96) + harden_working_ref + chr(96),
        chr(96) + "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md" + chr(96),
        chr(96) + "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md" + chr(96),
        chr(96) + "working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md" + chr(96),
    ]
    if current_open_work_filename:
        readme_active_routes.insert(0, "4. " + chr(96) + current_open_work_filename + chr(96))
'''
if old_routes not in s:
    raise AssertionError("FIA README-route tuple anchor missing")
s = s.replace(old_routes, new_routes, 1)
write(p, s)

# D3. Product-law tests: advance only current-source expectations. Keep the
# historical §26.18 v0.3.0 reconciliation assertion pinned to v1.2.0/v1.2.59.
p = ROOT / "tests" / "test_product_law_hardening.py"
s = read(p)
old_current_table = '''        for current_name in (
            "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
            "00_PLATFORM_v1.6.0.md",
            "01_DECISIONS_v1.6.0.md",
            "02_OPEN_WORK_v1.2.59.md",
            "04_DOMAIN_MAP_v1.2.0.md",
            "05_ROADMAP_v1.2.0.md",
        ):
'''
new_current_table = old_current_table.replace("02_OPEN_WORK_v1.2.59.md", "02_OPEN_WORK_v1.2.60.md").replace(
    "05_ROADMAP_v1.2.0.md", "05_ROADMAP_v1.3.0.md"
)
if old_current_table not in s:
    raise AssertionError("Product current-source table expectation anchor missing")
s = s.replace(old_current_table, new_current_table, 1)
old_sources = '''        current_sources = (
            "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
            "00_PLATFORM_v1.6.0.md",
            "01_DECISIONS_v1.6.0.md",
            "03_ARCHITECTURE_v1.1.1.md",
            "04_DOMAIN_MAP_v1.2.0.md",
            "05_ROADMAP_v1.2.0.md",
            "02_OPEN_WORK_v1.2.59.md",
            "FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
        )
'''
new_sources = old_sources.replace("05_ROADMAP_v1.2.0.md", "05_ROADMAP_v1.3.0.md").replace(
    "02_OPEN_WORK_v1.2.59.md", "02_OPEN_WORK_v1.2.60.md"
)
if old_sources not in s:
    raise AssertionError("Product current Atlas source tuple anchor missing")
s = s.replace(old_sources, new_sources, 1)
write(p, s)

# D4. Current-route diagnostic message assertions follow the relational validator.
p = ROOT / "tests" / "test_foundation_integrity_audit.py"
s = read(p)
s = s.replace(
    "Open Work v1.2.60 Atlas route must name archived Atlas v0.4.1 as its immediate routing predecessor",
    "current Open Work Atlas route does not match the manifest-selected Atlas and its immediate archived predecessor",
)
s = s.replace(
    "current HARDEN-02 v0.5.3 successor metadata declaration",
    "current HARDEN-02 v0.5.4 successor metadata declaration",
)
write(p, s)

# Diff-hygiene repair for one exact generated current-route test line.
p = ROOT / "tests" / "test_authority_routing_successors.py"
s = read(p)
s = s.replace(
    '        for filename in ("00_PLATFORM_v1.6.0.md", "01_DECISIONS_v1.6.0.md", "02_OPEN_WORK_v1.2.60.md", "04_DOMAIN_MAP_v1.2.0.md"): \n',
    '        for filename in ("00_PLATFORM_v1.6.0.md", "01_DECISIONS_v1.6.0.md", "02_OPEN_WORK_v1.2.60.md", "04_DOMAIN_MAP_v1.2.0.md"):\n',
    1,
)
write(p, s)
'''

path.write_text(text, encoding="utf-8")
print("PASS9_DYNAMIC_CURRENT_ROUTES_FIX_APPLIED")
