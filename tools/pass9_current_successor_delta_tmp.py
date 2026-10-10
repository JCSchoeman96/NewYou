from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN = "086ade7b28c000de1c387acb9760e5eb08bb0413"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def one(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected exactly one old marker, found {count}: {old!r}")
    return text.replace(old, new, 1)


def function_block(text: str, name: str) -> tuple[int, int, str]:
    start = text.find(f"def {name}(")
    if start < 0:
        raise AssertionError(f"function not found: {name}")
    nxt = text.find("\ndef ", start + 4)
    end = len(text) if nxt < 0 else nxt
    return start, end, text[start:end]


def replace_function_block(text: str, name: str, mutate) -> str:
    start, end, block = function_block(text, name)
    updated = mutate(block)
    return text[:start] + updated + text[end:]


def active_route_replace(text: str, old: str, new: str, archived_old: str | None = None) -> str:
    text = text.replace(old, new)
    if archived_old is not None:
        text = text.replace("archive/" + new, "archive/" + archived_old)
    return text


# ---------------------------------------------------------------------------
# 1. Production audit: advance only the current FP-001 routing/integrity view.
# Historical archive hashes and source-at-freeze evidence stay untouched.
# ---------------------------------------------------------------------------
p = ROOT / "tools" / "foundation_integrity_audit.py"
s = read(p)


def mutate_pmr(block: str) -> str:
    # Current Open Work route/version.
    block = block.replace("docs/00_platform/02_OPEN_WORK_v1.2.59.md", "docs/00_platform/02_OPEN_WORK_v1.2.60.md")
    block = block.replace('"02_OPEN_WORK_v1.2.59.md"', '"02_OPEN_WORK_v1.2.60.md"')
    block = block.replace('"1.2.59"', '"1.2.60"', 1)
    block = block.replace("manifest Open Work route is not v1.2.59", "manifest Open Work route is not v1.2.60")

    # Current Atlas route and exact immediate predecessor.
    block = block.replace(
        "current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.1.md`; immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`",
        "current Atlas `working/DELIVERY_ATLAS_WORKING_v0.4.2.md`; immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`",
    )
    block = block.replace(
        "Open Work v1.2.59 Atlas route must name archived Atlas v0.4.0 as its immediate routing predecessor",
        "Open Work v1.2.60 Atlas route must name archived Atlas v0.4.1 as its immediate routing predecessor",
    )
    block = block.replace(
        'atlas_path = docs / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"',
        'atlas_path = docs / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"',
    )
    block = block.replace(
        '_markdown_header_metadata(atlas, "# Delivery Atlas working v0.4.1")',
        '_markdown_header_metadata(atlas, "# Delivery Atlas working v0.4.2")',
    )
    block = block.replace(
        'not atlas_predecessors[0].startswith("`archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`")',
        'not atlas_predecessors[0].startswith("`archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`")',
    )
    block = block.replace(
        'not atlas_transitions[0].startswith("`v0.4.0 → v0.4.1`")',
        'not atlas_transitions[0].startswith("`v0.4.1 → v0.4.2`")',
    )
    block = block.replace(
        'if "docs/00_platform/02_OPEN_WORK_v1.2.59.md" not in atlas:',
        'if "docs/00_platform/02_OPEN_WORK_v1.2.60.md" not in atlas:',
    )
    block = block.replace(
        'issues.append("current Delivery Atlas does not point to Open Work v1.2.59")',
        'issues.append("current Delivery Atlas does not point to Open Work v1.2.60")',
    )

    # Current HARDEN route and metadata. Prior base-SHA declarations remain required.
    block = block.replace(
        'harden_path = docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"',
        'harden_path = docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"',
    )
    block = block.replace(
        '_markdown_header_metadata(harden, "# HARDEN-02_CONTRACT_WORKING_v0.5.3.md")',
        '_markdown_header_metadata(harden, "# HARDEN-02_CONTRACT_WORKING_v0.5.4.md")',
    )
    block = block.replace(
        '"Plan / contract version": lambda value: value == "`v0.5.3`",',
        '"Plan / contract version": lambda value: value == "`v0.5.4`",',
    )
    block = block.replace(
        '"Current predecessor": lambda value: value.startswith("`archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md`"),',
        '"Current predecessor": lambda value: value.startswith("`archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`"),',
    )
    block = block.replace(
        ') and "this v0.5.3 successor" in value,',
        ') and "this v0.5.4 successor" in value,',
    )
    sha_v053 = (
        '        "v0.5.3 status-successor base main SHA": lambda value: value\n'
        '        == "`a062bd56e3ae94e815e2991ee00bf133ee9f3b56`",\n'
    )
    if '"v0.5.4 status-successor base main SHA"' not in block:
        if sha_v053 not in block:
            raise AssertionError("HARDEN v0.5.3 metadata validator anchor missing")
        block = block.replace(
            sha_v053,
            sha_v053
            + '        "v0.5.4 status-successor base main SHA": lambda value: value\n'
            + f'        == "`{MAIN}`",\n',
            1,
        )
    block = block.replace(
        "current HARDEN-02 v0.5.3 successor metadata declaration",
        "current HARDEN-02 v0.5.4 successor metadata declaration",
    )

    # Current lifecycle projection moved by routing only; business/gate state is unchanged.
    block = block.replace(
        '"status_successor_base_sha": "a062bd56e3ae94e815e2991ee00bf133ee9f3b56",',
        f'"status_successor_base_sha": "{MAIN}",',
        1,
    )
    block = block.replace('"status_successor_version": "0.5.3",', '"status_successor_version": "0.5.4",', 1)
    block = block.replace("Current programme status is in Open Work v1.2.59.", "Current programme status is in Open Work v1.2.60.")

    return block


s = replace_function_block(s, "_check_fp001_pmr_reconciliation", mutate_pmr)
write(p, s)

# Candidate HARDEN header must identify itself, not the superseded status successor.
p = ROOT / "docs" / "00_platform" / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"
s = read(p)
s = one(
    s,
    "this v0.5.3 successor preserves them and records current status plus source routing/provenance",
    "this v0.5.4 successor preserves them and records current status plus source routing/provenance",
    "HARDEN certified-semantics successor self-reference",
)
write(p, s)

# ---------------------------------------------------------------------------
# 2. Tests that intentionally follow current authority/current navigation.
# Historical archive routes are restored after each active-path replacement.
# ---------------------------------------------------------------------------

# Atlas authority boundary: current Atlas/Open Work only; historical normalizers remain pinned.
p = ROOT / "tests" / "test_atlas_authority_boundary.py"
s = read(p)
s = s.replace(
    'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"',
    'ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"',
)
s = s.replace(
    'CURRENT_OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.59.md"',
    'CURRENT_OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.60.md"',
)
write(p, s)

# Product-law hardening consumes current derived Atlas navigation.
p = ROOT / "tests" / "test_product_law_hardening.py"
s = read(p)
s = s.replace(
    '"working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md"',
    '"working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"',
)
write(p, s)

# DOL-01 route test: advance current expectations, restore archived predecessor expectations.
p = ROOT / "tests" / "test_dol_01_marketing_unsubscribe_authority.py"
s = read(p)
for old, new, archive_old in (
    ("02_OPEN_WORK_v1.2.59.md", "02_OPEN_WORK_v1.2.60.md", "02_OPEN_WORK_v1.2.59.md"),
    ("05_ROADMAP_v1.2.0.md", "05_ROADMAP_v1.3.0.md", "05_ROADMAP_v1.2.0.md"),
    ("DELIVERY_ATLAS_WORKING_v0.4.1.md", "DELIVERY_ATLAS_WORKING_v0.4.2.md", "DELIVERY_ATLAS_WORKING_v0.4.1.md"),
    ("HARDEN-02_CONTRACT_WORKING_v0.5.3.md", "HARDEN-02_CONTRACT_WORKING_v0.5.4.md", "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"),
):
    s = s.replace(old, new)
    s = s.replace("archive/" + new, "archive/" + archive_old)
write(p, s)

# Foundation-audit tests: current active paths advance; archive/source-at-freeze paths stay pinned.
p = ROOT / "tests" / "test_foundation_integrity_audit.py"
s = read(p)
for old, new, archive_old in (
    ("02_OPEN_WORK_v1.2.59.md", "02_OPEN_WORK_v1.2.60.md", "02_OPEN_WORK_v1.2.59.md"),
    ("05_ROADMAP_v1.2.0.md", "05_ROADMAP_v1.3.0.md", "05_ROADMAP_v1.2.0.md"),
    ("DELIVERY_ATLAS_WORKING_v0.4.1.md", "DELIVERY_ATLAS_WORKING_v0.4.2.md", "DELIVERY_ATLAS_WORKING_v0.4.1.md"),
    ("HARDEN-02_CONTRACT_WORKING_v0.5.3.md", "HARDEN-02_CONTRACT_WORKING_v0.5.4.md", "HARDEN-02_CONTRACT_WORKING_v0.5.3.md"),
):
    s = s.replace(old, new)
    s = s.replace("archive/" + new, "archive/" + archive_old)

# Current Atlas metadata mutation tests now target v0.4.2 and its direct predecessor.
s = s.replace("## v0.4.1 Patch Scope", "## v0.4.2 Patch Scope")
s = s.replace(
    "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md` (routing predecessor; preserved byte-identically). Earlier predecessors remain preserved at their archive paths.",
    "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md` (routing predecessor; preserved byte-identically). Earlier predecessors remain preserved at their archive paths.",
)
s = s.replace("- **SemVer transition:** `v0.4.0 → v0.4.1`", "- **SemVer transition:** `v0.4.1 → v0.4.2`")
s = s.replace(
    'current_predecessor = "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`"',
    'current_predecessor = "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`"',
)
s = s.replace(
    'stale_predecessor = "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.9.md`"',
    'stale_predecessor = "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.4.0.md`"',
)
s = s.replace(
    "Open Work v1.2.59 Atlas route must name archived Atlas v0.4.0 as its immediate routing predecessor",
    "Open Work v1.2.60 Atlas route must name archived Atlas v0.4.1 as its immediate routing predecessor",
)

# Current HARDEN metadata mutation tests now target v0.5.4 and v0.5.3 predecessor.
s = s.replace("test_fp001_pmr_validates_harden_v053_successor_metadata", "test_fp001_pmr_validates_harden_v054_successor_metadata")
s = s.replace(
    'predecessor = "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.2.md` — byte-identical prior current-status snapshot\\n"',
    'predecessor = "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md` — byte-identical prior current-status snapshot\\n"',
)
s = s.replace("this v0.5.3 successor preserves them", "this v0.5.4 successor preserves them")
s = s.replace("this v0.5.2 successor preserves them", "this v0.5.3 successor preserves them")
s = s.replace(
    '- **v0.5.3 status-successor base main SHA:** `a062bd56e3ae94e815e2991ee00bf133ee9f3b56`\\n",\n                "",',
    f'- **v0.5.4 status-successor base main SHA:** `{MAIN}`\\n",\n                "",',
)
s = s.replace(
    '- **v0.5.3 status-successor base main SHA:** `a062bd56e3ae94e815e2991ee00bf133ee9f3b56`",\n                "- **v0.5.3 status-successor base main SHA:** `0000000000000000000000000000000000000000`",',
    f'- **v0.5.4 status-successor base main SHA:** `{MAIN}`",\n                "- **v0.5.4 status-successor base main SHA:** `0000000000000000000000000000000000000000`",',
)
s = s.replace(
    'self.assertIn("- **Plan / contract version:** `v0.5.3`", harden.split("### Revision log", 1)[0])',
    'self.assertIn("- **Plan / contract version:** `v0.5.4`", harden.split("### Revision log", 1)[0])',
)
s = s.replace(
    'self.assertIn("current HARDEN-02 v0.5.3 successor metadata", promotion_check["message"])',
    'self.assertIn("current HARDEN-02 v0.5.4 successor metadata", promotion_check["message"])',
)
s = s.replace(
    '"HARDEN-02 v0.5.3 successor metadata declaration",',
    '"HARDEN-02 v0.5.4 successor metadata declaration",',
)
s = s.replace(
    '("v0.5.3 status-successor base main SHA", "`0000000000000000000000000000000000000000`"),',
    '("v0.5.4 status-successor base main SHA", "`0000000000000000000000000000000000000000`"),',
)

write(p, s)

# ---------------------------------------------------------------------------
# 3. Sanity checks: prove current routes moved while direct predecessors remain archived.
# ---------------------------------------------------------------------------
audit = read(ROOT / "tools" / "foundation_integrity_audit.py")
assert 'docs/00_platform/02_OPEN_WORK_v1.2.60.md' in audit
assert 'atlas_path = docs / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md"' in audit
assert 'harden_path = docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md"' in audit
assert '`archive/DELIVERY_ATLAS_WORKING_v0.4.1.md`' in audit
assert '`archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md`' in audit
assert '"v0.5.4 status-successor base main SHA"' in audit

assert (ROOT / "docs/00_platform/archive/05_ROADMAP_v1.2.0.md").is_file()
assert (ROOT / "docs/00_platform/archive/02_OPEN_WORK_v1.2.59.md").is_file()
assert (ROOT / "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.1.md").is_file()
assert (ROOT / "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.3.md").is_file()

print("PASS9_CURRENT_SUCCESSOR_DELTA_APPLIED")
