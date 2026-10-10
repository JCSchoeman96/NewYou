from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def one(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one occurrence, found {count}: {old[:140]!r}")
    return text.replace(old, new, 1)


def replace_section(text: str, start: str, end: str, replacements: tuple[tuple[str, str], ...]) -> str:
    a = text.index(start)
    b = text.index(end, a + len(start))
    body = text[a:b]
    for old, new in replacements:
        body = body.replace(old, new)
    return text[:a] + body + text[b:]


# ---------------------------------------------------------------------------
# A. Retained documents: update only live/current routing surfaces.
# ---------------------------------------------------------------------------
readme_path = DOCS / "README.md"
readme = read(readme_path)
readme = readme.replace("4. `02_OPEN_WORK_v1.2.59.md`", "4. `02_OPEN_WORK_v1.2.60.md`", 1)
readme = readme.replace("7. `05_ROADMAP_v1.2.0.md`", "7. `05_ROADMAP_v1.3.0.md`", 1)

old_atlas_bullet = next(line for line in readme.splitlines() if line.startswith("- `working/DELIVERY_ATLAS_WORKING_v0.4.1.md`"))
new_atlas_bullet = (
    "- `working/DELIVERY_ATLAS_WORKING_v0.4.2.md` — routing-only derived Delivery Atlas successor aligned to "
    "Roadmap v1.3.0 and Open Work v1.2.60. It remains working/non-authoritative, outside authority-document "
    "records, and is listed only under graph/navigation paths. It does not semantically re-derive prior Atlas views; "
    "current Roadmap authority wins. Direct predecessor v0.4.1 is preserved byte-identically at "
    "`archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`. The unchanged v0.2.1 working path remains available to existing "
    "FP-001 and HARDEN-02 source-at-freeze references."
)
readme = one(readme, old_atlas_bullet, new_atlas_bullet, "README current Atlas bullet")
old_harden_bullet = next(line for line in readme.splitlines() if line.startswith("- `working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`"))
new_harden_bullet = (
    "- `working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md` — routing-only current-status successor preserving certified "
    "HARDEN-02 semantics and execution evidence while following Roadmap v1.3.0 / Open Work v1.2.60. Engineering "
    "Standards Authority Promotion, FP-001 PMR reconciliation, Identity v0.1.4 promotion and Communications dossier "
    "v0.1.0 promotion remain COMPLETE / CERTIFIED. Communications finalisation remains BLOCKED / STOP; later gates "
    "remain downstream or blocked. Direct predecessor v0.5.3 is preserved byte-identically at "
    "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`."
)
readme = one(readme, old_harden_bullet, new_harden_bullet, "README current HARDEN bullet")
readme = readme.replace(
    "[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.4.1.md)",
    "[Delivery Atlas](working/DELIVERY_ATLAS_WORKING_v0.4.2.md)",
    1,
)
readme = readme.replace(
    "Current programme status is in Open Work v1.2.59.",
    "Current programme status is in Open Work v1.2.60.",
    1,
)

archive_replacements = (
    (
        "- `archive/02_OPEN_WORK_v1.2.58.md` — byte-identical direct predecessor to current Open Work v1.2.59; its hash is pinned in the manifest. Communications IN PROGRESS / CERTIFICATION PENDING is preserved as historical state.",
        "- `archive/02_OPEN_WORK_v1.2.59.md` — byte-identical direct predecessor to current Open Work v1.2.60; its hash is pinned in the manifest.\n"
        "- `archive/02_OPEN_WORK_v1.2.58.md` — byte-identical predecessor to archived Open Work v1.2.59; its hash is pinned in the manifest. Communications IN PROGRESS / CERTIFICATION PENDING remains historical state.",
    ),
    (
        "- `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md` — byte-identical direct predecessor to current Atlas v0.4.1; its hash is pinned in the manifest.",
        "- `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md` — byte-identical direct predecessor to current Atlas v0.4.2; its hash is pinned in the manifest.\n"
        "- `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md` — byte-identical predecessor to archived Atlas v0.4.1; its hash is pinned in the manifest.",
    ),
    (
        "- `archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md` — byte-identical direct predecessor to current HARDEN-02 v0.5.3; its hash is pinned in the manifest.",
        "- `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md` — byte-identical direct predecessor to current HARDEN-02 v0.5.4; its hash is pinned in the manifest.\n"
        "- `archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md` — byte-identical predecessor to archived HARDEN-02 v0.5.3; its hash is pinned in the manifest.",
    ),
)
for old, new in archive_replacements:
    if old in readme:
        readme = one(readme, old, new, "README archive lineage")
write(readme_path, readme)

harden_path = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"
harden = read(harden_path)
harden = replace_section(
    harden,
    "### CURRENT AUTHORITY",
    "### CURRENT DERIVED EVIDENCE",
    (("02_OPEN_WORK_v1.2.59.md", "02_OPEN_WORK_v1.2.60.md"), ("05_ROADMAP_v1.2.0.md", "05_ROADMAP_v1.3.0.md")),
)
harden = replace_section(
    harden,
    "### CURRENT DERIVED EVIDENCE",
    "### HISTORICAL AUTHORITY / WORKING EVIDENCE",
    (("working/DELIVERY_ATLAS_WORKING_v0.4.1.md", "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"),),
)
harden = replace_section(
    harden,
    "## 21. Current execution certification and next stage",
    "## 22.",
    (
        ("Open Work v1.2.59", "Open Work v1.2.60"),
        ("02_OPEN_WORK_v1.2.59.md", "02_OPEN_WORK_v1.2.60.md"),
        ("05_ROADMAP_v1.2.0.md", "05_ROADMAP_v1.3.0.md"),
        ("working/DELIVERY_ATLAS_WORKING_v0.4.1.md", "working/DELIVERY_ATLAS_WORKING_v0.4.2.md"),
    ),
)
write(harden_path, harden)

# ---------------------------------------------------------------------------
# B. Production FIA: current routes are derived from manifest/navigation.
# Historical evidence remains literal.
# ---------------------------------------------------------------------------
p = ROOT / "tools" / "foundation_integrity_audit.py"
s = read(p)

anchor = '    issues: list[str] = []\n\n    current_entries = ['
insert = '''    issues: list[str] = []\n\n    graph_rules = integrity_rules.get("graph_rules", {})\n    navigation_paths = graph_rules.get("navigation_document_paths", [])\n    if not isinstance(navigation_paths, list):\n        issues.append("manifest graph navigation paths must be a list")\n        navigation_paths = []\n\n    def current_navigation_route(prefix: str) -> str:\n        matches = [\n            path for path in navigation_paths\n            if isinstance(path, str)\n            and Path(path).parent.as_posix() == "docs/00_platform/working"\n            and Path(path).name.startswith(prefix)\n        ]\n        if len(matches) != 1:\n            issues.append(f"manifest must identify exactly one current navigation route for {prefix}")\n            return ""\n        return matches[0]\n\n    def version_from_route(route: str, prefix: str) -> str:\n        match = re.fullmatch(re.escape(prefix) + r"(\\d+\\.\\d+\\.\\d+)\\.md", Path(route).name)\n        if match is None:\n            issues.append(f"current route has malformed SemVer filename: {route}")\n            return ""\n        return match.group(1)\n\n    def latest_archived_route(prefix: str, current_version: str) -> str:\n        if not current_version:\n            return ""\n        current = tuple(int(part) for part in current_version.split("."))\n        candidates: list[tuple[tuple[int, int, int], Path]] = []\n        pattern = re.compile(re.escape(prefix) + r"(\\d+\\.\\d+\\.\\d+)\\.md$")\n        for candidate in (docs / "archive").glob(prefix + "*.md"):\n            match = pattern.fullmatch(candidate.name)\n            if match is None:\n                continue\n            version = tuple(int(part) for part in match.group(1).split("."))\n            if version < current:\n                candidates.append((version, candidate))\n        if not candidates:\n            issues.append(f"no archived predecessor exists for current route {prefix}{current_version}.md")\n            return ""\n        predecessor = max(candidates, key=lambda item: item[0])[1]\n        return "archive/" + predecessor.name\n\n    current_atlas_route = current_navigation_route("DELIVERY_ATLAS_WORKING_v")\n    current_harden_route = current_navigation_route("HARDEN-02_CONTRACT_WORKING_v")\n    atlas_version = version_from_route(current_atlas_route, "DELIVERY_ATLAS_WORKING_v") if current_atlas_route else ""\n    harden_version = version_from_route(current_harden_route, "HARDEN-02_CONTRACT_WORKING_v") if current_harden_route else ""\n    expected_atlas_predecessor = latest_archived_route("DELIVERY_ATLAS_WORKING_v", atlas_version) if atlas_version else ""\n    expected_harden_predecessor = latest_archived_route("HARDEN-02_CONTRACT_WORKING_v", harden_version) if harden_version else ""\n    atlas_working_ref = current_atlas_route.removeprefix("docs/00_platform/")\n    harden_working_ref = current_harden_route.removeprefix("docs/00_platform/")\n\n    current_entries = ['''
s = one(s, anchor, insert, "FIA current-route derivation insertion")

old = '''        if _relative_path(current_open_work) != "docs/00_platform/02_OPEN_WORK_v1.2.60.md":\n            issues.append("manifest Open Work route is not v1.2.60")\n        if current_open_work.get("canonical_filename") != "02_OPEN_WORK_v1.2.60.md":\n            issues.append("manifest current Open Work filename is stale")\n        if current_open_work.get("semver") != "1.2.60":\n            issues.append("manifest current Open Work version is stale")\n'''
new = '''        current_open_work_filename = current_open_work.get("canonical_filename")\n        current_open_work_semver = current_open_work.get("semver")\n        if not isinstance(current_open_work_filename, str) or not isinstance(current_open_work_semver, str):\n            issues.append("manifest current Open Work filename/SemVer metadata is missing")\n        else:\n            if _relative_path(current_open_work) != f"docs/00_platform/{current_open_work_filename}":\n                issues.append("manifest current Open Work repository path disagrees with its canonical filename")\n            if current_open_work_filename != f"02_OPEN_WORK_v{current_open_work_semver}.md":\n                issues.append("manifest current Open Work filename disagrees with its SemVer")\n'''
s = one(s, old, new, "FIA Open Work dynamic route")

old = '''    atlas_status_lines = re.findall(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", open_work)\n    expected_atlas_status = (\n        "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.2.md`; "\n        "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`; "\n        "pinned v0.2.1 source-at-freeze artifacts remain preserved; DERIVED / NON-AUTHORITATIVE; "\n        "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"\n    )\n    if atlas_status_lines != [expected_atlas_status]:\n        issues.append(\n            "Open Work v1.2.60 Atlas route must name archived Atlas v0.4.1 as its immediate routing predecessor"\n        )\n'''
new = '''    atlas_status_lines = re.findall(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", open_work)\n    expected_atlas_status = (\n        f"ATLAS RECONCILIATION: COMPLETE — current Atlas `{atlas_working_ref}`; "\n        f"immediate routing predecessor `{expected_atlas_predecessor}`; "\n        "pinned v0.2.1 source-at-freeze artifacts remain preserved; DERIVED / NON-AUTHORITATIVE; "\n        "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"\n    )\n    if atlas_status_lines != [expected_atlas_status]:\n        issues.append("current Open Work Atlas route does not match the manifest-selected Atlas and its immediate archived predecessor")\n'''
s = one(s, old, new, "FIA dynamic Atlas Open Work route")

old = '''    navigation_paths = integrity_rules.get("graph_rules", {}).get("navigation_document_paths", [])\n    expected_navigation_paths = {\n        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.2.md",\n        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md",\n        "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",\n        "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",\n        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md",\n    }\n'''
new = '''    expected_navigation_paths = {\n        current_atlas_route,\n        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md",\n        "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",\n        "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",\n        current_harden_route,\n    }\n'''
s = one(s, old, new, "FIA dynamic graph routes")

start = s.index('    atlas_path = docs / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"')
end = s.index('\n    harden_path = docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"', start)
atlas_block = '''    atlas_path = root / current_atlas_route if current_atlas_route else docs / "working" / "__missing_atlas__.md"\n    atlas = atlas_path.read_text(encoding="utf-8") if atlas_path.is_file() else ""\n    atlas_header = _markdown_header_metadata(atlas, f"# Delivery Atlas working v{atlas_version}") if atlas_version else ""\n    atlas_predecessors = _metadata_values(atlas_header, "Predecessor")\n    atlas_transitions = _metadata_values(atlas_header, "SemVer transition")\n    all_atlas_predecessors = _metadata_declarations(atlas, "Predecessor")\n    all_atlas_transitions = _metadata_declarations(atlas, "SemVer transition")\n    predecessor_version_match = re.search(r"DELIVERY_ATLAS_WORKING_v(\\d+\\.\\d+\\.\\d+)\\.md", expected_atlas_predecessor)\n    predecessor_version = predecessor_version_match.group(1) if predecessor_version_match else ""\n    if (\n        len(all_atlas_predecessors) != 1\n        or len(atlas_predecessors) != 1\n        or all_atlas_predecessors != atlas_predecessors\n        or not atlas_predecessors[0].startswith(f"`{expected_atlas_predecessor}`")\n    ):\n        issues.append(\n            "current Atlas artifact lineage has a missing, duplicate, misplaced or incorrect Atlas metadata declaration for Predecessor"\n        )\n    if (\n        len(all_atlas_transitions) != 1\n        or len(atlas_transitions) != 1\n        or all_atlas_transitions != atlas_transitions\n        or not atlas_transitions[0].startswith(f"`v{predecessor_version} → v{atlas_version}`")\n    ):\n        issues.append(\n            "current Atlas artifact lineage has a missing, duplicate, misplaced or incorrect Atlas metadata declaration for SemVer transition"\n        )\n    if isinstance(current_open_work, dict) and _relative_path(current_open_work) not in atlas:\n        issues.append("current Delivery Atlas does not point to the manifest-selected Open Work route")\n    roadmap_entries = [\n        entry for entry in _all_entries(manifest)\n        if entry.get("document_id") == "ROADMAP" and entry.get("lifecycle", "current") != "historical"\n    ]\n    if len(roadmap_entries) != 1 or _relative_path(roadmap_entries[0]) not in atlas:\n        issues.append("current Delivery Atlas does not point to the manifest-selected Roadmap route")\n    atlas_content_state = _metadata_values(atlas_header, "Current content state")\n    current_atlas_state = atlas_content_state[0] if len(atlas_content_state) == 1 else ""\n    if (\n        "FP-001 PMR reconciliation remains COMPLETE / CERTIFIED" not in current_atlas_state\n        or "Identity dossier v0.1.4 is CERTIFIED / CURRENT" not in current_atlas_state\n        or "Communications finalisation remains BLOCKED / STOP" not in current_atlas_state\n    ):\n        issues.append("current Delivery Atlas header is stale or omits the certified FP-001 status boundary")\n'''
s = s[:start] + atlas_block + s[end:]

old_harden_start = '    harden_path = docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"'
start = s.index(old_harden_start)
metadata_start = s.index('    harden_status_line = re.findall', start)
old_block = s[start:metadata_start]
harden_block = '''    harden_path = root / current_harden_route if current_harden_route else docs / "working" / "__missing_harden__.md"\n    harden = harden_path.read_text(encoding="utf-8") if harden_path.is_file() else ""\n    harden_header = _markdown_header_metadata(harden, f"# HARDEN-02_CONTRACT_WORKING_v{harden_version}.md") if harden_version else ""\n    harden_metadata_validators = {\n        "Plan / contract version": lambda value: value == f"`v{harden_version}`",\n        "Current predecessor": lambda value: value.startswith(f"`{expected_harden_predecessor}`"),\n        "Earlier historical status predecessor": lambda value: value.startswith(\n            "`archive/HARDEN-02_CONTRACT_WORKING_v0.5.1.md`"\n        ),\n        "Certified contract semantics": lambda value: value.startswith(\n            "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md`"\n        ) and f"this v{harden_version} successor" in value,\n        "v0.5.0 status-successor base main SHA": lambda value: value\n        == "`df6190a06bdc8aa4b99f6ed3a18cb9e3e12e22fb`",\n        "v0.5.1 status-successor base main SHA": lambda value: value\n        == "`90f96ba3452c95112bf6ec4ce5bb897676adbed4`",\n        "v0.5.2 status-successor base main SHA": lambda value: value\n        == "`0473cd69416f72fd94f2cee24a4d02c7f4fe0992`",\n        "v0.5.3 status-successor base main SHA": lambda value: value\n        == "`a062bd56e3ae94e815e2991ee00bf133ee9f3b56`",\n        f"v{harden_version} status-successor base main SHA": lambda value: value\n        == "`086ade7b28c000de1c387acb9760e5eb08bb0413`",\n    }\n    for label, valid_value in harden_metadata_validators.items():\n        header_values = _metadata_values(harden_header, label)\n        document_values = _metadata_declarations(harden, label)\n        if (\n            len(header_values) != 1\n            or len(document_values) != 1\n            or document_values != header_values\n            or not valid_value(header_values[0])\n        ):\n            issues.append(\n                f"current HARDEN-02 v{harden_version} successor metadata declaration for {label} must occur once in the canonical header and match its governed value"\n            )\n'''
s = s[:start] + harden_block + s[metadata_start:]

s = s.replace(
    'if "Open Work v1.2.59" not in harden_current or "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED" not in harden_current',
    'if f"Open Work v{current_open_work_semver}" not in harden_current or "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED" not in harden_current',
    1,
)

old = '''    readme_active_routes = (\n        "4. " + chr(96) + "02_OPEN_WORK_v1.2.60.md" + chr(96),\n        chr(96) + "working/DELIVERY_ATLAS_WORKING_v0.4.2.md" + chr(96) + " — derived Delivery Atlas",\n        chr(96) + "working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md" + chr(96) + " — preserves certified HARDEN-02",\n        chr(96) + "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md" + chr(96) + " — certified/current",\n        chr(96) + "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md" + chr(96) + " — certified/current",\n        chr(96) + "working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md" + chr(96),\n    )\n'''
new = '''    readme_active_routes = (\n        "4. " + chr(96) + str(current_open_work_filename) + chr(96),\n        chr(96) + atlas_working_ref + chr(96),\n        chr(96) + harden_working_ref + chr(96),\n        chr(96) + "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md" + chr(96),\n        chr(96) + "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md" + chr(96),\n        chr(96) + "working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md" + chr(96),\n    )\n'''
s = one(s, old, new, "FIA dynamic README active routes")
write(p, s)

# ---------------------------------------------------------------------------
# C. Current-route regression tests. Historical/source-at-freeze fixtures stay literal.
# ---------------------------------------------------------------------------
p = ROOT / "tests" / "test_product_law_hardening.py"
s = read(p)
helper_anchor = '''def current_document(document_id: str) -> str:\n    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))\n    entry = next(item for item in manifest["governing_documents"] if item["document_id"] == document_id)\n    return (ROOT / entry["repository_path"]).read_text(encoding="utf-8")\n\n\n'''
helper_new = helper_anchor + '''def current_navigation_document(prefix: str) -> str:\n    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))\n    paths = manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]\n    matches = [path for path in paths if Path(path).name.startswith(prefix)]\n    if len(matches) != 1:\n        raise AssertionError(f"expected one current navigation path for {prefix}, found {matches}")\n    return (ROOT / matches[0]).read_text(encoding="utf-8")\n\n\n'''
s = one(s, helper_anchor, helper_new, "product test navigation helper")
s = s.replace('cls.atlas = (DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md").read_text(encoding="utf-8")', 'cls.atlas = current_navigation_document("DELIVERY_ATLAS_WORKING_v")', 1)
s = s.replace('cls.harden02 = (DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md").read_text(\n            encoding="utf-8"\n        )', 'cls.harden02 = current_navigation_document("HARDEN-02_CONTRACT_WORKING_v")', 1)
s = s.replace('self.assertIn("05_ROADMAP_v1.2.0.md", self.open_work)', 'self.assertIn("05_ROADMAP_v1.3.0.md", self.open_work)', 1)
s = s.replace('            "02_OPEN_WORK_v1.2.59.md",\n            "04_DOMAIN_MAP_v1.2.0.md",\n            "05_ROADMAP_v1.2.0.md",', '            "02_OPEN_WORK_v1.2.60.md",\n            "04_DOMAIN_MAP_v1.2.0.md",\n            "05_ROADMAP_v1.3.0.md",', 1)
s = s.replace('            "docs/00_platform/02_OPEN_WORK_v1.2.59.md",\n            "docs/00_platform/05_ROADMAP_v1.2.0.md",', '            "docs/00_platform/02_OPEN_WORK_v1.2.60.md",\n            "docs/00_platform/05_ROADMAP_v1.3.0.md",', 1)
s = s.replace('            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.1.md",\n            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.3.md",', '            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.2.md",\n            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.4.md",', 1)
write(p, s)

p = ROOT / "tests" / "test_atlas_authority_boundary.py"
s = read(p)
s = s.replace('            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.1.md",\n            graph["navigation_document_paths"],', '            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.2.md",\n            graph["navigation_document_paths"],', 1)
s = s.replace('self.assertEqual("02_OPEN_WORK_v1.2.59.md", open_work_entry["canonical_filename"])', 'self.assertEqual(CURRENT_OPEN_WORK.name, open_work_entry["canonical_filename"])', 1)
write(p, s)

p = ROOT / "tests" / "test_dol_01_marketing_unsubscribe_authority.py"
s = read(p)
s = s.replace('"OPEN_WORK": ("02_OPEN_WORK_v1.2.60.md", "1.2.59")', '"OPEN_WORK": ("02_OPEN_WORK_v1.2.60.md", "1.2.60")', 1)
s = s.replace('"ROADMAP": ("05_ROADMAP_v1.3.0.md", "1.2.0")', '"ROADMAP": ("05_ROADMAP_v1.3.0.md", "1.3.0")', 1)
write(p, s)

p = ROOT / "tests" / "test_foundation_integrity_audit.py"
s = read(p)
replacements = (
    ('"- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`",\n                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.9.md`"', '"- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`",\n                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`"'),
    ('"- **SemVer transition:** `v0.4.0 → v0.4.1`",\n                "- **SemVer transition:** `v0.3.9 → v0.4.0`"', '"- **SemVer transition:** `v0.4.1 → v0.4.2`",\n                "- **SemVer transition:** `v0.4.0 → v0.4.1`"'),
    ('"- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md` (routing predecessor; preserved byte-identically). Earlier predecessors remain preserved at their archive paths.\\n"', '"- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md` (routing predecessor; preserved byte-identically). Earlier predecessors remain preserved at their archive paths.\\n"'),
    ('"- **SemVer transition:** `v0.4.0 → v0.4.1`",\n                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md` (duplicate)\\n"\n                "- **SemVer transition:** `v0.4.0 → v0.4.1`"', '"- **SemVer transition:** `v0.4.1 → v0.4.2`",\n                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md` (duplicate)\\n"\n                "- **SemVer transition:** `v0.4.1 → v0.4.2`"'),
    ('self.assertIn("- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`", header)', 'self.assertIn("- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`", header)'),
    ('self.assertIn("current HARDEN-02 v0.5.3 successor metadata declaration",', 'self.assertIn("current HARDEN-02 v0.5.4 successor metadata declaration",'),
)
for old, new in replacements:
    s = s.replace(old, new)
write(p, s)

print("PASS9_DYNAMIC_CURRENT_ROUTES_APPLIED")
