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
# One earlier scratch generator emits a single trailing space in a current-route
# test line. Normalize that exact generated line; do not strip historical files.
text += '''\n# Diff-hygiene repair for exact generated current-route test line.\np = ROOT / "tests" / "test_authority_routing_successors.py"\ns = read(p)\ns = s.replace(\n    '        for filename in ("00_PLATFORM_v1.6.0.md", "01_DECISIONS_v1.6.0.md", "02_OPEN_WORK_v1.2.60.md", "04_DOMAIN_MAP_v1.2.0.md"): \\n',\n    '        for filename in ("00_PLATFORM_v1.6.0.md", "01_DECISIONS_v1.6.0.md", "02_OPEN_WORK_v1.2.60.md", "04_DOMAIN_MAP_v1.2.0.md"):\\n',\n    1,\n)\nwrite(p, s)\n'''
path.write_text(text, encoding="utf-8")
print("PASS9_DYNAMIC_CURRENT_ROUTES_FIX_APPLIED")
