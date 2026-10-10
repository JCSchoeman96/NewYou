from pathlib import Path

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
path.write_text(text, encoding="utf-8")
print("PASS9_DYNAMIC_CURRENT_ROUTES_FIX_APPLIED")
