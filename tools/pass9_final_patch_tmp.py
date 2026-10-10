from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN = "086ade7b28c000de1c387acb9760e5eb08bb0413"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def transition(text: str, old: str, new: str, label: str) -> str:
    old_count = text.count(old)
    new_count = text.count(new)
    if old_count == 1 and new_count == 0:
        return text.replace(old, new, 1)
    if old_count == 0 and new_count == 1:
        return text
    raise AssertionError(
        f"{label}: expected one old→new transition or one already-new marker; "
        f"old={old_count}, new={new_count}"
    )


# 1. CURRENT_AUTHORITY and the one current-route test method must match the
# promoted README/manifest route. Historical fixtures elsewhere remain pinned.
p = ROOT / "tests" / "test_authority_routing_successors.py"
s = read(p)
s = transition(
    s,
    '    "OPEN_WORK": "02_OPEN_WORK_v1.2.59.md",\n    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",',
    '    "OPEN_WORK": "02_OPEN_WORK_v1.2.60.md",\n    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",',
    "CURRENT_AUTHORITY Open Work",
)
s = transition(
    s,
    '    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.2.0.md",\n    "ROADMAP": "05_ROADMAP_v1.2.0.md",',
    '    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.2.0.md",\n    "ROADMAP": "05_ROADMAP_v1.3.0.md",',
    "CURRENT_AUTHORITY Roadmap",
)
method_updates = [
    (
        'for filename in ("00_PLATFORM_v1.6.0.md", "01_DECISIONS_v1.6.0.md", "02_OPEN_WORK_v1.2.59.md", "04_DOMAIN_MAP_v1.2.0.md"):',
        'for filename in ("00_PLATFORM_v1.6.0.md", "01_DECISIONS_v1.6.0.md", "02_OPEN_WORK_v1.2.60.md", "04_DOMAIN_MAP_v1.2.0.md"): ',
    ),
    (
        'self.assertIn("ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.2.0`", readme)',
        'self.assertIn("ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.3.0`", readme)',
    ),
    (
        'self.assertIn("current semantic successor `05_ROADMAP_v1.2.0.md`; predecessor `archive/05_ROADMAP_v1.1.5.md`", readme)',
        'self.assertIn("current semantic successor `05_ROADMAP_v1.3.0.md`; predecessor `archive/05_ROADMAP_v1.2.0.md`", readme)',
    ),
    (
        'self.assertIn("current semantic successor 05_ROADMAP_v1.2.0.md; predecessor archive/05_ROADMAP_v1.1.5.md", open_work)',
        'self.assertIn("current semantic successor 05_ROADMAP_v1.3.0.md; predecessor archive/05_ROADMAP_v1.2.0.md", open_work)',
    ),
    (
        'self.assertEqual("1.2.59", self.governing["OPEN_WORK"]["semver"])',
        'self.assertEqual("1.2.60", self.governing["OPEN_WORK"]["semver"])',
    ),
    (
        '_read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.1.md")',
        '_read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.4.2.md")',
    ),
    (
        '_read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.3.md")',
        '_read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.4.md")',
    ),
]
for old, new in method_updates:
    if old in s:
        s = s.replace(old, new, 1)
write(p, s)

# 2. Production HARDEN lifecycle accepts the routing-only v0.5.4 successor while
# preserving every prior certified/historical version. The promotion-complete
# branch also has its own exact-current override and must advance in lockstep.
p = ROOT / "tools" / "foundation_integrity_audit.py"
s = read(p)
s = transition(
    s,
    '        "successor_versions": ("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3"),',
    '        "successor_versions": ("0.4.7", "0.4.8", "0.4.9", "0.5.0", "0.5.1", "0.5.2", "0.5.3", "0.5.4"),',
    "HARDEN completed successor versions",
)
s = transition(
    s,
    '                    "successor_versions": ("0.5.3",),',
    '                    "successor_versions": ("0.5.4",),',
    "promotion-complete current HARDEN successor",
)
s = transition(
    s,
    'expected_harden_version = "0.5.3" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"',
    'expected_harden_version = "0.5.4" if promotion_status == "COMPLETE / CERTIFIED" else "0.4.7"',
    "current HARDEN version",
)
old_base = '''        expected_base_sha = (
            "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"'''
new_base = f'''        expected_base_sha = (
            "{MAIN}"
            if state.get("status_successor_version") == "0.5.4"
            else "a062bd56e3ae94e815e2991ee00bf133ee9f3b56"
            if state.get("status_successor_version") == "0.5.3"'''
s = transition(s, old_base, new_base, "HARDEN v0.5.4 base SHA")
write(p, s)

# 3. Runtime assertions: prove the exact execution paths changed before tests.
fixture = read(ROOT / "tests" / "test_authority_routing_successors.py")
fixture_head = fixture.split("STARTING_MAIN_SHA", 1)[0]
assert '"OPEN_WORK": "02_OPEN_WORK_v1.2.60.md"' in fixture_head
assert '"ROADMAP": "05_ROADMAP_v1.3.0.md"' in fixture_head
assert '"02_OPEN_WORK_v1.2.60.md", "04_DOMAIN_MAP_v1.2.0.md"' in fixture
assert 'ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.3.0`' in fixture
assert 'self.assertEqual("1.2.60", self.governing["OPEN_WORK"]["semver"])' in fixture

audit = read(ROOT / "tools" / "foundation_integrity_audit.py")
complete_start = audit.index('    "COMPLETE / CERTIFIED": {', audit.index("H02_EXECUTION_STATES"))
complete_end = audit.index("    },", complete_start)
complete_block = audit[complete_start:complete_end]
assert '"0.5.4"' in complete_block
assert '"successor_versions": ("0.5.4",)' in audit
assert 'expected_harden_version = "0.5.4"' in audit
assert f'"{MAIN}"\n            if state.get("status_successor_version") == "0.5.4"' in audit

open_work = read(ROOT / "docs" / "00_platform" / "02_OPEN_WORK_v1.2.60.md")
match = re.search(
    r'<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(\{.*?\})\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->',
    open_work,
    re.DOTALL,
)
assert match is not None
state = json.loads(match.group(1))
assert state["status_successor_version"] == "0.5.4", state["status_successor_version"]
assert state["status_successor_base_sha"] == MAIN, state["status_successor_base_sha"]

print("PASS9_FINAL_PATCH_APPLIED")
print("CURRENT_AUTHORITY_OPEN_WORK=02_OPEN_WORK_v1.2.60.md")
print("CURRENT_AUTHORITY_ROADMAP=05_ROADMAP_v1.3.0.md")
print("HARDEN_COMPLETE_SUCCESSOR_INCLUDES=0.5.4")
print("HARDEN_CURRENT_OVERRIDE=0.5.4")
print("OPEN_WORK_STATUS_SUCCESSOR_VERSION=0.5.4")
