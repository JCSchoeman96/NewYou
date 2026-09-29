from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

from tests.test_harden_02_execution import (
    _normalise_atlas_successor as _normalise_current_atlas_successor,
    _normalise_contract_successor as _normalise_current_harden_successor,
    _normalise_open_work_successor as _normalise_current_open_work_successor,
)
from tests.test_roadmap_routing_resilience import (
    _normalise_roadmap_successor as _normalise_current_roadmap_successor,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

PREDECESSORS = {
    "PROJECT_NORTH_STAR_AND_MVP": (
        "PROJECT_NORTH_STAR_AND_MVP_v1.2.2.md",
        "1.2.2",
        "1.2.3",
        "296b01a3da81e079bd33aab7a59dd23390946baf0b6daa3deae9d71f3971531d",
    ),
    "PLATFORM_BASELINE": (
        "00_PLATFORM_v1.4.1.md",
        "1.4.1",
        "1.5.0",
        "868b6a6ca81df7d4322dd534cb4387c051748cd49cdc3834e53626b49040c8ec",
    ),
    "DECISION_REGISTER": (
        "01_DECISIONS_v1.4.1.md",
        "1.4.1",
        "1.5.0",
        "e92564c16c9ad15e8b7558ff76a509efad4310aa786c697b09b0ce2723ec4701",
    ),
    "OPEN_WORK": (
        "02_OPEN_WORK_v1.2.48.md",
        "1.2.48",
        "1.2.49",
        "270172784629197f2bb6faa60dbe6d4184bd9d04d878876f6877c98390fd8d17",
    ),
    "ROADMAP": (
        "05_ROADMAP_v1.1.3.md",
        "1.1.3",
        "1.1.4",
        "9cba581592ebc43ec3e39debce82a8e86ac0b3132962d7be12d377706e5e0126",
    ),
}

CURRENT_AUTHORITY = {
    "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md",
    "PLATFORM_BASELINE": "00_PLATFORM_v1.5.2.md",
    "DECISION_REGISTER": "01_DECISIONS_v1.5.0.md",
    "OPEN_WORK": "02_OPEN_WORK_v1.2.51.md",
    "ARCHITECTURE_SYNTHESIS": "03_ARCHITECTURE_v1.1.1.md",
    "DOMAIN_MAP": "04_DOMAIN_MAP_v1.2.0.md",
    "ROADMAP": "05_ROADMAP_v1.1.6.md",
    "PLATFORM_OPERATING_MODEL": "PLATFORM_OPERATING_MODEL_v1.0.1.md",
    "FRONTEND_EXPERIENCE_SYSTEM": "FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
}

STARTING_MAIN_SHA = "6fea69eadf18f2fb79d78c2a94ab035b10abe31f"

ARCHIVED_STARTING_MAIN_BLOBS = {
    "PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md": (
        "41b6aab9d6061715dea2012c450f449a15a52300",
        "a3ff58a26d1ec13173b31c9e7994b427be5fcf644d344b3106894b0026272cd6",
    ),
    "00_PLATFORM_v1.5.1.md": (
        "b762afb4008770a1ef067a846d8b20adb85d0434",
        "70e57a6771c3b7cecadcad41d9c97f3dc8ac61d753591200fd1ed855b2417afe",
    ),
    "05_ROADMAP_v1.1.5.md": (
        "958aba14ded0bc0bd9a45ad0f9b6f18ff32d87b1",
        "5e5e938343d3ff7210515011b0bc9e11900553bcde24a552ef61cd2c85e7c5fb",
    ),
    "02_OPEN_WORK_v1.2.50.md": (
        "85395ec8861a3f0aee4a5845290a361e0940581f",
        "ea99015d5fca34211e9c85e9f6575e8ad69df2cf9a39da3b255f2e9d3a5abcb7",
    ),
    "DELIVERY_ATLAS_WORKING_v0.3.2.md": (
        "ea3328f397e1cda3e4cb1553e9c7c590b894b2cd",
        "b24bcaaac4f82617a766f1602418e8301a5076594d9ac8f90afb302174bf706e",
    ),
    "HARDEN-02_CONTRACT_WORKING_v0.4.4.md": (
        "216d5a175fb8c9cfa5c4745869b47294164d732a",
        "496df83ba06d3e3ad1e871b8415a5352147662ae694005d945359f7b1f7976da",
    ),
}

CURRENT_SUCCESSOR_PREDECESSORS = {
    "PROJECT_NORTH_STAR_AND_MVP": (
        "PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md", "1.2.4", "1.2.5",
        "PROJECT_NORTH_STAR_AND_MVP_V1_2_4",
    ),
    "PLATFORM_BASELINE": (
        "00_PLATFORM_v1.5.1.md", "1.5.1", "1.5.2", "PLATFORM_BASELINE_V1_5_1",
    ),
    "OPEN_WORK": (
        "02_OPEN_WORK_v1.2.50.md", "1.2.50", "1.2.51", "OPEN_WORK_V1_2_50",
    ),
    "ROADMAP": (
        "05_ROADMAP_v1.1.5.md", "1.1.5", "1.1.6", "ROADMAP_V1_1_5",
    ),
}

NORTH_STAR_PATCH_SCOPE = (
    "## v1.2.4 Patch Scope\n\n"
    "This non-semantic PATCH repairs current-authority routing and North Star self-state. It preserves the v1.2.3 "
    "North Star, MVP, catalogue, journeys, pricing, product boundaries and Phase 7/8 meaning.\n\n"
)
PRODUCT_PATCH_SCOPE = (
    "## v1.5.1 Patch Scope\n\n"
    "This non-semantic PATCH corrects Product self-version and delegates current programme routing and lifecycle "
    "status. Product semantics, including §21S and DEC-304 composition, remain unchanged; the Development Entry "
    "stop condition remains in force.\n\n"
)
ROADMAP_PATCH_SCOPE = (
    "## v1.1.5 Patch Scope\n\n"
    "This routing-only PATCH updates the explicit current Product-authority route. It preserves all 17 Feature Packs, "
    "outcomes, sequencing, dependencies, gates, proof semantics, implementation STOP and programme lifecycle state. "
    "README and current Open Work retain programme routing responsibility.\n\n"
)
OPEN_WORK_PATCH_SCOPE = "- **Patch scope:** PATCH / current-authority and derived-navigation route substitutions only.\n"
OPEN_WORK_CHANGELOG = (
    "- Planning-state SemVer transition: `v1.2.49 → v1.2.50`.\n"
    "- Archives Open Work v1.2.49 byte-identically and updates current authority and derived-navigation routes; "
    "all programme lifecycle states remain unchanged.\n"
)
ATLAS_PATCH_SCOPE = "- **Patch scope:** PATCH / current-source routing and provenance only; Atlas authority and delivery content are unchanged.\n"
HARDEN_V044_REVISION = (
    "- `v0.4.4` — PATCH current-authority/current-derived routing and provenance only. HARDEN execution and every "
    "v0.4.0 invariant remain unchanged.\n"
)

SUCCESSOR_FILES = {
    "north_star": (
        "PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md",
        "archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md",
    ),
    "product": ("00_PLATFORM_v1.5.2.md", "archive/00_PLATFORM_v1.5.1.md"),
    "roadmap": ("05_ROADMAP_v1.1.6.md", "archive/05_ROADMAP_v1.1.5.md"),
    "open_work": ("02_OPEN_WORK_v1.2.51.md", "archive/02_OPEN_WORK_v1.2.50.md"),
    "atlas": (
        "working/DELIVERY_ATLAS_WORKING_v0.3.3.md",
        "archive/DELIVERY_ATLAS_WORKING_v0.3.2.md",
    ),
    "harden": (
        "working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md",
        "archive/HARDEN-02_CONTRACT_WORKING_v0.4.4.md",
    ),
}

PRODUCT_BODY_START =PRODUCT_BODY_START = "# 1. Platform Purpose"
PRODUCT_BODY_END = "# 24. Current Planning Stop Condition"
PRODUCT_INSERTION_START = "# 21S. Marketing Permission and Communication Preferences"
PRODUCT_INSERTION_END = "# 22. Explicitly Not Yet Decided"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_blob_oid(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def _section(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def _line_marker_positions(text: str, marker: str) -> list[int]:
    pattern = rf"(?m)^{re.escape(marker)}\r?$"
    return [match.start() for match in re.finditer(pattern, text)]


def _product_body(text: str) -> str:
    start_positions = _line_marker_positions(text, PRODUCT_BODY_START)
    if len(start_positions) != 1:
        raise ValueError(f"expected exactly one Product body start marker: {PRODUCT_BODY_START}")
    end_positions = _line_marker_positions(text, PRODUCT_BODY_END)
    if len(end_positions) != 1:
        raise ValueError(f"expected exactly one Product body end marker: {PRODUCT_BODY_END}")

    start = start_positions[0]
    end = end_positions[0]
    if start >= end:
        raise ValueError("Product body start marker must precede its end marker")
    return text[start:end]


def _successor_product_body_without_authorized_insertion(text: str) -> str:
    body = _product_body(text)
    insertion_start_positions = _line_marker_positions(text, PRODUCT_INSERTION_START)
    if len(insertion_start_positions) != 1:
        raise ValueError(f"expected exactly one authorized Product insertion start marker: {PRODUCT_INSERTION_START}")
    insertion_end_positions = _line_marker_positions(text, PRODUCT_INSERTION_END)
    if len(insertion_end_positions) != 1:
        raise ValueError(f"expected exactly one authorized Product insertion end marker: {PRODUCT_INSERTION_END}")

    body_start = _line_marker_positions(text, PRODUCT_BODY_START)[0]
    body_end = _line_marker_positions(text, PRODUCT_BODY_END)[0]
    insertion_start = insertion_start_positions[0]
    insertion_end = insertion_end_positions[0]
    if not (body_start < insertion_start < body_end):
        raise ValueError("Product insertion start marker must be inside the Product body")
    if not (body_start < insertion_end < body_end):
        raise ValueError("Product insertion end marker must be inside the Product body")
    if insertion_end <= insertion_start:
        raise ValueError("Product insertion end marker must follow its start marker")
    return body[: insertion_start - body_start] + body[insertion_end - body_start :]


def _feature_pack_sections(text: str) -> dict[str, str]:
    starts = list(re.finditer(r"^## (FP-\d{3}) — .+$", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else text.index("# 7. MVP", match.end())
        sections[match.group(1)] = text[match.start() : end]
    return sections


SUCCESSOR_NORMALIZATION = {
    "north_star": {
        "patch": NORTH_STAR_PATCH_SCOPE,
        "before": "- **Decision coverage:** GQ-001 through GQ-012 plus GQ-NY-001 and approved post-freeze DEC-292–DEC-303 amendments\n",
        "after": "## v1.2.3 Patch Scope\n",
        "replacements": (
            ("# PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md", "# PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", 1),
            ("- **Document status:** FROZEN PRODUCT NORTH STAR / MVP BASELINE v1.2.4", "- **Document status:** FROZEN PRODUCT NORTH STAR / MVP BASELINE v1.2.3", 1),
            ("- **Document version:** v1.2.4", "- **Document version:** v1.2.3", 1),
            ("- **Predecessor:** `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`", "- **Predecessor:** `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.2.md`", 1),
            ("- **SemVer transition:** `v1.2.3 → v1.2.4`", "- **SemVer transition:** `v1.2.2 → v1.2.3`", 1),
            ("  - `00_PLATFORM_v1.5.1.md`", "  - `00_PLATFORM_v1.4.1.md`", 1),
            ("  - `01_DECISIONS_v1.5.0.md`", "  - `01_DECISIONS_v1.4.1.md`", 1),
            ("  - `02_OPEN_WORK_v1.2.50.md`", "  - `02_OPEN_WORK_v1.2.45.md`", 1),
            ("  - `05_ROADMAP_v1.1.5.md`", "  - `05_ROADMAP_v1.1.2.md`", 1),
            ("- **Last updated:** 2026-09-29", "- **Last updated:** 2026-09-26", 1),
            (
                "Current Product/Decision/Roadmap authority is routed by README and CURRENT_AUTHORITY_MANIFEST. README and current Open Work own the active programme stage and NEXT route. This North Star does not authorise HARDEN-02 execution, implementation or Phase 8 proof.",
                "Current routing is `00_PLATFORM_v1.4.1.md`, `01_DECISIONS_v1.4.1.md`, `02_OPEN_WORK_v1.2.45.md` and `05_ROADMAP_v1.1.2.md`. README and current Open Work own the active programme stage and NEXT route. This North Star path patch does not authorise HARDEN-02 execution, advance implementation or Phase 8 proof.",
                1,
            ),
            ("**Current Product Law / governance-alignment condition: MET (v1.2.4).**", "**Current Product Law / governance-alignment condition: MET (v1.2.2).**", 1),
        ),
    },
    "product": {
        "patch": PRODUCT_PATCH_SCOPE,
        "before": "- **Related documents:** `01_DECISIONS_v1.5.0.md`, `02_OPEN_WORK_v1.2.50.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md`\n",
        "after": "## v1.3.0 Amendment Scope\n",
        "replacements": (
            ("# 00_PLATFORM_v1.5.1.md", "# 00_PLATFORM_v1.5.0.md", 1),
            ("- **Document status:** FROZEN PRODUCT BASELINE v1.5.1", "- **Document status:** FROZEN PRODUCT BASELINE v1.5.0", 1),
            ("- **Document version:** v1.5.1", "- **Document version:** v1.5.0", 1),
            ("- **Predecessor:** `archive/00_PLATFORM_v1.5.0.md`", "- **Predecessor:** `archive/00_PLATFORM_v1.4.1.md`", 1),
            ("- **SemVer transition:** `v1.5.0 → v1.5.1`", "- **SemVer transition:** `v1.4.1 → v1.5.0`", 1),
            ("- **Last updated:** 2026-09-29", "- **Last updated:** 2026-09-26", 1),
            (
                "- **Related documents:** `01_DECISIONS_v1.5.0.md`, `02_OPEN_WORK_v1.2.50.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md`",
                "- **Related documents:** `01_DECISIONS_v1.5.0.md`, `02_OPEN_WORK_v1.2.46.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`",
                1,
            ),
            (
                "Current Product Law is v1.5.1. This Product Law successor does not execute HARDEN-02 or authorise implementation. README and current Open Work own current programme routing and lifecycle status. The Product Law Development Entry and executable-development stop conditions remain in force. Phase 8 and executable development remain blocked until the Development Entry conditions pass. Historical amendment text above remains preserved.",
                "Current Product Law is v1.4.1. This Product Law successor does not execute HARDEN-02 or authorise implementation. README and current Open Work own current programme routing; current Open Work records HARDEN-02 execution as NEXT / AUTHORISED / NOT STARTED. `FP001_RECONCILIATION_REQUIRED` remains downstream and not performed. Phase 8 and executable development remain blocked until the Development Entry conditions pass. Historical amendment text above remains preserved.",
                1,
            ),
        ),
    },
    "roadmap": {
        "patch": ROADMAP_PATCH_SCOPE,
        "before": "## v1.1.4 Patch Scope\n",
        "after": "# 1. Authority, purpose and boundaries\n",
        "replacements": (
            ("# 05_ROADMAP_v1.1.5.md", "# 05_ROADMAP_v1.1.4.md", 1),
            ("- **Document version:** v1.1.5", "- **Document version:** v1.1.4", 1),
            ("- **Predecessor frozen version:** `archive/05_ROADMAP_v1.1.4.md`", "- **Predecessor frozen version:** `archive/05_ROADMAP_v1.1.3.md`", 1),
            ("- **SemVer transition:** `v1.1.4 → v1.1.5`", "- **SemVer transition:** `v1.1.3 → v1.1.4`", 1),
            ("- **Last updated:** 2026-09-29", "- **Last updated:** 2026-09-26", 1),
            (
                "- **Current Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md`, `00_PLATFORM_v1.5.1.md`, `01_DECISIONS_v1.5.0.md`",
                "- **Current Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`, `00_PLATFORM_v1.5.0.md`, `01_DECISIONS_v1.5.0.md`",
                1,
            ),
        ),
    },
    "open_work": {
        "patch": OPEN_WORK_PATCH_SCOPE,
        "before": "- **Planning-state SemVer transition:** `v1.2.49 → v1.2.50`",
        "after": "- **Related documents:**",
        "changelog": OPEN_WORK_CHANGELOG,
        "changelog_before": "## Historical changelog\n\n",
        "changelog_after": "- Planning-state SemVer transition: `v1.2.48 → v1.2.49`.\n",
        "replacements": (
            ("# 02_OPEN_WORK_v1.2.50.md", "# 02_OPEN_WORK_v1.2.49.md", 1),
            ("- **Document status:** PRODUCT LAW AND GOVERNANCE HARDENING OPEN-WORK SUCCESSOR v1.2.50", "- **Document status:** PRODUCT LAW AND GOVERNANCE HARDENING OPEN-WORK SUCCESSOR v1.2.49", 1),
            ("- **Document version:** v1.2.50", "- **Document version:** v1.2.49", 1),
            ("- **Predecessor:** `archive/02_OPEN_WORK_v1.2.49.md`", "- **Predecessor:** `archive/02_OPEN_WORK_v1.2.48.md`", 1),
            ("- **Planning-state SemVer transition:** `v1.2.49 → v1.2.50` — current-authority routing only; no downstream gate advances.", "- **Planning-state SemVer transition:** `v1.2.48 → v1.2.49` — execution-status/routing update only; no downstream gate advances.", 1),
            ("- **Last updated:** 2026-09-29", "- **Last updated:** 2026-09-28", 1),
            ("PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md", "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", 1),
            ("00_PLATFORM_v1.5.1.md", "00_PLATFORM_v1.5.0.md", 4),
            ("05_ROADMAP_v1.1.5.md", "05_ROADMAP_v1.1.4.md", 6),
            ("working/DELIVERY_ATLAS_WORKING_v0.3.2.md", "working/DELIVERY_ATLAS_WORKING_v0.3.1.md", 5),
            ("archive/DELIVERY_ATLAS_WORKING_v0.3.1.md", "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", 1),
            ("working/HARDEN-02_CONTRACT_WORKING_v0.4.4.md", "working/HARDEN-02_CONTRACT_WORKING_v0.4.3.md", 4),
            ("current v0.4.4", "current v0.4.3", 1),
            ("Status successor v0.4.4", "Status successor v0.4.3", 1),
            ("current status recorded by working v0.4.4", "current status recorded by working v0.4.3", 1),
            ("current North Star v1.2.4:", "current North Star v1.2.3:", 1),
        ),
    },
    "atlas": {
        "patch": ATLAS_PATCH_SCOPE,
        "before": "- **Current content state:**",
        "after": "This document is the current Delivery Atlas working artifact.",
        "replacements": (
            ("# Delivery Atlas working v0.3.2", "# Delivery Atlas working v0.3.1", 1),
            ("archive/DELIVERY_ATLAS_WORKING_v0.3.1.md", "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", 2),
            ("- **SemVer transition:** `v0.3.1 → v0.3.2` (PATCH: current-source routing and provenance only; Atlas authority and delivery content are unchanged).", "- **SemVer transition:** `v0.3.0 → v0.3.1` (PATCH: current Open Work routing update only; Atlas authority and delivery content are unchanged).", 1),
            (
                "- **Current content state:** ATLAS-01 through ATLAS-11 remain complete at their recorded scope as derived navigation. This `v0.3.2` current-source-routing successor updates current Product, Decision, Open Work and Roadmap source references only; the v0.3.1 authority-boundary and delivery content remain unchanged. It preserves the existing Feature Pack relationships, FP-001/PMR routing, capability rows, Domain participation derivation and all upstream meanings. Grill-Me prompts, handoff summaries and revalidation guidance are advisory unless a current upstream source or approved contract owns a requirement. This successor does **not** populate a new ATLAS-12 view, amend FP-001 Skeleton/dossiers, HARDEN-02 or Engineering Standards, authorise implementation, or advance any stage. HARDEN-02 artifacts are not amended by this successor. `FP001_RECONCILIATION_REQUIRED` remains downstream.",
                "- **Current content state:** ATLAS-01 through ATLAS-11 remain complete at their recorded scope as derived navigation. This `v0.3.1` routing successor updates current Open Work routing only; the v0.3.0 authority-boundary and delivery content remain unchanged. It preserves the existing Feature Pack relationships, FP-001/PMR routing, capability rows, Domain participation derivation and all upstream meanings. Grill-Me prompts, handoff summaries and revalidation guidance are advisory unless a current upstream source or approved contract owns a requirement. This successor does **not** populate a new ATLAS-12 view, amend FP-001 Skeleton/dossiers, HARDEN-02 or Engineering Standards, authorise implementation, or advance any stage. HARDEN-02 artifacts are not amended by this successor. `FP001_RECONCILIATION_REQUIRED` remains downstream.",
                1,
            ),
            ("PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md", "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", 5),
            ("00_PLATFORM_v1.5.1.md", "00_PLATFORM_v1.5.0.md", 6),
            ("02_OPEN_WORK_v1.2.50.md", "02_OPEN_WORK_v1.2.49.md", 2),
            ("05_ROADMAP_v1.1.5.md", "05_ROADMAP_v1.1.4.md", 6),
            (
                "| Current-source routing | §1.1 points to Product `v1.5.1`, Decisions `v1.5.0`, Architecture `v1.1.1`, Domain Map `v1.2.0`, Roadmap `v1.1.5` and current Open Work `v1.2.50`. |",
                "| Current-source routing | §1.1 points to Product `v1.5.0`, Decisions `v1.5.0`, Architecture `v1.1.1`, Domain Map `v1.2.0`, Roadmap `v1.1.4` and current Open Work `v1.2.49`. |",
                1,
            ),
        ),
    },
    "harden": {
        "patch": HARDEN_V044_REVISION,
        "before": "- `v0.4.3` — PATCH status + current-source-routing/provenance successor",
        "after": "## 1. Objective\n",
        "replacements": (
            ("# HARDEN-02_CONTRACT_WORKING_v0.4.4.md", "# HARDEN-02_CONTRACT_WORKING_v0.4.3.md", 1),
            ("- **Plan / contract version:** `v0.4.4`", "- **Plan / contract version:** `v0.4.3`", 1),
            ("- **Predecessor v0.4.3 routing-successor base main SHA:** `4efdac4fe3c79b96b18a243800e47c71e7d369b8`", "- **Predecessor v0.4.2 status-successor base main SHA:** `9411b34b646d7752d2942afca1363830d3b25f10`", 1),
            ("- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.3.md`", "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.2.md`", 1),
            ("this v0.4.4 successor", "this v0.4.3 successor", 1),
            ("- **Last updated:** 2026-09-29", "- **Last updated:** 2026-09-28", 1),
            ("PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md", "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", 1),
            ("00_PLATFORM_v1.5.1.md", "00_PLATFORM_v1.5.0.md", 1),
            ("02_OPEN_WORK_v1.2.50.md", "02_OPEN_WORK_v1.2.49.md", 1),
            ("05_ROADMAP_v1.1.5.md", "05_ROADMAP_v1.1.4.md", 1),
            ("working/DELIVERY_ATLAS_WORKING_v0.3.2.md", "working/DELIVERY_ATLAS_WORKING_v0.3.1.md", 1),
            (
                "The v0.4.0 contract lifecycle remains COMPLETE / CERTIFIED. The original status-successor base main SHA is `9411b34b646d7752d2942afca1363830d3b25f10`. The v0.4.3 execution-status successor records that HARDEN-02 execution started from exact current main SHA `1c8fc94058176795d88cb82e08857e3d30c553e9`. This v0.4.4 current-source-routing/provenance successor is based on exact current main SHA `4efdac4fe3c79b96b18a243800e47c71e7d369b8`. Execution remains IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING; execution certification remains pending until the governed post-merge lifecycle is complete. This successor does not revise or recertify v0.4.0 semantics, alter any invariant or scope boundary, or advance a downstream stage.",
                "The v0.4.0 contract lifecycle remains COMPLETE / CERTIFIED. The original status-successor base main SHA is `9411b34b646d7752d2942afca1363830d3b25f10`. This v0.4.3 status + current-source-routing/provenance successor starts HARDEN-02 execution from exact current main SHA `1c8fc94058176795d88cb82e08857e3d30c553e9`. Execution is IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING; execution certification remains pending until the governed post-merge lifecycle is complete. This successor does not revise or recertify v0.4.0 semantics, alter any invariant or scope boundary, or advance a downstream stage.",
                1,
            ),
        ),
    },
}


def _remove_normalization_block(text: str, block: str, before: str, after: str) -> str:
    if text.count(block) != 1:
        raise ValueError("declared successor-only block is missing or duplicated")
    block_start = text.index(block)
    before_positions = [match.start() for match in re.finditer(re.escape(before), text)]
    after_positions = [match.start() for match in re.finditer(re.escape(after), text)]
    if len(before_positions) != 1 or len(after_positions) != 1:
        raise ValueError("normalization boundary marker is missing or duplicated")
    if not before_positions[0] < block_start < after_positions[0]:
        raise ValueError("declared successor-only block is relocated")
    return text.replace(block, "", 1)


def _validate_north_star_current_state(text: str, expected_version: str) -> None:
    routing = _section(
        text,
        "# 23. Current Planning Position",
        "# 24. Document Stop Condition",
    )
    pinned_route = re.compile(
        r"(?:PROJECT_NORTH_STAR_AND_MVP|00_PLATFORM|01_DECISIONS|02_OPEN_WORK|05_ROADMAP)_v\d+\.\d+\.\d+\.md"
    )
    if pinned_route.search(routing):
        raise ValueError("North Star §23 pins versioned current routes")
    if "README" not in routing or "CURRENT_AUTHORITY_MANIFEST" not in routing:
        raise ValueError("North Star §23 does not delegate current authority routing")
    if "current Open Work own the active programme stage and NEXT route" not in routing:
        raise ValueError("North Star §23 does not delegate current programme routing")
    stop_condition = _section(text, "# 24. Document Stop Condition", "**Implementation STOP:**")
    state_versions = re.findall(
        r"Current Product Law / governance-alignment condition:\s+MET\s+\(v(\d+\.\d+\.\d+)\)",
        stop_condition,
    )
    if state_versions != [expected_version]:
        raise ValueError(f"North Star §24 self-state {state_versions!r} does not match {expected_version!r}")


def _validate_product_current_state(text: str, expected_version: str) -> None:
    stop_condition = text.split("# 24. Current Planning Stop Condition", 1)[1]
    product_versions = re.findall(
        r"Current Product Law is v(\d+\.\d+\.\d+)",
        stop_condition,
    )
    if product_versions != [expected_version]:
        raise ValueError(f"Product §24 self-state {product_versions!r} does not match {expected_version!r}")
    if "README and current Open Work own current programme routing and lifecycle status" not in stop_condition:
        raise ValueError("Product §24 does not delegate programme routing and lifecycle status")
    if "Development Entry" not in stop_condition or "Implementation hard stop" not in stop_condition:
        raise ValueError("Product §24 no longer retains its durable development stop condition")
    volatile_states = (
        "NEXT / AUTHORISED / NOT STARTED",
        "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
        "COMPLETE / CERTIFIED",
    )
    if any(state in stop_condition for state in volatile_states):
        raise ValueError("Product §24 mirrors volatile HARDEN lifecycle state")


CURRENT_PATCH_MARKERS = {
    "north_star": (
        "## v1.2.5 Patch Scope\n\n"
        "This non-semantic PATCH refreshes current-authority routing after certified HARDEN-02 execution. "
        "It preserves the v1.2.4 North Star, MVP, catalogue, journeys, pricing, product boundaries and Phase 7/8 meaning. "
        "README and current Open Work remain the sole current programme/status route. This patch does not create "
        "Engineering Standards authority, perform its promotion, reconcile FP-001, advance Phase 7C/proof classification, "
        "or authorise Phase 8/implementation.\n\n"
    ),
    "product": (
        "## v1.5.2 Patch Scope\n\n"
        "This non-semantic PATCH refreshes current-authority routing after certified HARDEN-02 execution. "
        "Product semantics, including §21S and DEC-304 composition, remain unchanged. README and current Open Work "
        "continue to own volatile programme/status routing. This patch does not create or approve Engineering Standards, "
        "perform FP-001 reconciliation, advance Phase 7C/proof classification, or authorise Phase 8/implementation.\n\n"
    ),
    "roadmap": (
        "## v1.1.6 Patch Scope\n\n"
        "This routing-only PATCH refreshes the explicit current Product-authority route after certified HARDEN-02 execution. "
        "It preserves all 17 Feature Packs, outcomes, sequencing, dependencies, gates, §21 task-contract/proof semantics, "
        "and the implementation STOP. README and current Open Work retain programme routing responsibility. "
        "No downstream stage is completed by this Roadmap patch.\n\n"
    ),
    "open_work": "- **Patch scope:** PATCH / certified HARDEN-02 execution status + immediate H02-3R route transition + current-source routing only.\n",
    "atlas": "- **SemVer transition:** `v0.3.2 → v0.3.3` (PATCH: current-source routing and provenance only; Atlas authority and delivery content are unchanged).\n",
    "harden": (
        "- `v0.4.5` — PATCH execution-certification status successor. Records I-01…I-13 PASS and the prospective "
        "PR #57/#59 recovery certification culminating in resulting main `6fea69eadf18f2fb79d78c2a94ab035b10abe31f`; "
        "routes NEXT exclusively to `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`. It preserves H02-1/H02-2/H02-3R, "
        "every v0.4.0 scope/invariant, and all later gates. The PR #59 direct phase-diagram-body helper mutation-test note "
        "remains non-blocking evidence-led hardening.\n"
    ),
}

CURRENT_ROUTE_MUTATIONS = {
    "north_star": "# PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md",
    "product": "# 00_PLATFORM_v1.5.2.md",
    "roadmap": "# 05_ROADMAP_v1.1.6.md",
    "open_work": "# 02_OPEN_WORK_v1.2.51.md",
    "atlas": "# Delivery Atlas working v0.3.3",
    "harden": "# HARDEN-02_CONTRACT_WORKING_v0.4.5.md",
}


def _normalise_current_north_star(successor: str, predecessor: str) -> str:
    marker = CURRENT_PATCH_MARKERS["north_star"]
    if successor.count(marker) != 1:
        raise ValueError("North Star v1.2.5 Patch Scope is missing, duplicated, or altered")
    restored = successor.replace(marker, "", 1)
    replacements = (
        ("# PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md", "# PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md"),
        ("FROZEN PRODUCT NORTH STAR / MVP BASELINE v1.2.5", "FROZEN PRODUCT NORTH STAR / MVP BASELINE v1.2.4"),
        ("- **Document version:** v1.2.5", "- **Document version:** v1.2.4"),
        ("- **Predecessor:** `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md`", "- **Predecessor:** `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`"),
        ("- **SemVer transition:** `v1.2.4 → v1.2.5`", "- **SemVer transition:** `v1.2.3 → v1.2.4`"),
        ("  - `00_PLATFORM_v1.5.2.md`", "  - `00_PLATFORM_v1.5.1.md`"),
        ("  - `02_OPEN_WORK_v1.2.51.md`", "  - `02_OPEN_WORK_v1.2.50.md`"),
        ("  - `05_ROADMAP_v1.1.6.md`", "  - `05_ROADMAP_v1.1.5.md`"),
        ("**Current Product Law / governance-alignment condition: MET (v1.2.5).**", "**Current Product Law / governance-alignment condition: MET (v1.2.4).**"),
    )
    for current, previous in replacements:
        if restored.count(current) != 1:
            raise ValueError(f"North Star current-route marker is missing or duplicated: {current}")
        restored = restored.replace(current, previous, 1)
    if restored != predecessor:
        raise ValueError("North Star v1.2.5 differs from v1.2.4 outside the declared route/self-state patch")
    return predecessor


def _normalise_current_product(successor: str, predecessor: str) -> str:
    marker = CURRENT_PATCH_MARKERS["product"]
    if successor.count(marker) != 1:
        raise ValueError("Product v1.5.2 Patch Scope is missing, duplicated, or altered")
    restored = successor.replace(marker, "", 1)
    replacements = (
        ("# 00_PLATFORM_v1.5.2.md", "# 00_PLATFORM_v1.5.1.md"),
        ("FROZEN PRODUCT BASELINE v1.5.2", "FROZEN PRODUCT BASELINE v1.5.1"),
        ("- **Document version:** v1.5.2", "- **Document version:** v1.5.1"),
        ("- **Predecessor:** `archive/00_PLATFORM_v1.5.1.md`", "- **Predecessor:** `archive/00_PLATFORM_v1.5.0.md`"),
        ("- **SemVer transition:** `v1.5.1 → v1.5.2`", "- **SemVer transition:** `v1.5.0 → v1.5.1`"),
        (
            "- **Related documents:** `01_DECISIONS_v1.5.0.md`, `02_OPEN_WORK_v1.2.51.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.2.5.md`",
            "- **Related documents:** `01_DECISIONS_v1.5.0.md`, `02_OPEN_WORK_v1.2.50.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md`",
        ),
        (
            "Current Product Law is v1.5.2. HARDEN-02 execution status is delegated to README and current Open Work; "
            "this Product Law successor does not execute Engineering Standards Authority Promotion or authorise implementation.",
            "Current Product Law is v1.5.1. This Product Law successor does not execute HARDEN-02 or authorise implementation.",
        ),
    )
    for current, previous in replacements:
        if restored.count(current) != 1:
            raise ValueError(f"Product current-route marker is missing or duplicated: {current[:80]}")
        restored = restored.replace(current, previous, 1)
    if restored != predecessor:
        raise ValueError("Product v1.5.2 differs from v1.5.1 outside the declared route/self-state patch")
    return predecessor


def _normalise_successor(kind: str, successor: str, predecessor: str) -> str:
    normalizers = {
        "north_star": _normalise_current_north_star,
        "product": _normalise_current_product,
        "roadmap": _normalise_current_roadmap_successor,
        "open_work": _normalise_current_open_work_successor,
        "atlas": _normalise_current_atlas_successor,
        "harden": _normalise_current_harden_successor,
    }
    try:
        normalizer = normalizers[kind]
    except KeyError as exc:
        raise ValueError(f"unknown current successor kind: {kind}") from exc
    return normalizer(successor, predecessor)


OPEN_WORK_HISTORICAL_ATLAS_BLOCK =OPEN_WORK_HISTORICAL_ATLAS_BLOCK = (
    "## 12.7 — Historical Delivery Atlas reconciliation\n\n"
    "**Status:** HISTORICAL COMPLETION RECORD — the then-current derived / non-authoritative navigation successor was "
    "`working/DELIVERY_ATLAS_WORKING_v0.2.1.md` (predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`; "
    "earlier predecessor `archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`). This subsection records that historical "
    "reconciliation and is not the current Atlas route.\n\n"
)
OPEN_WORK_HISTORICAL_ATLAS_BLOCK_PREDECESSOR = (
    "## 12.7 — Delivery Atlas reconciliation\n\n"
    "**Status:** COMPLETE as derived / non-authoritative navigation successor `working/DELIVERY_ATLAS_WORKING_v0.2.1.md` "
    "(predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.0.md`; earlier predecessor "
    "`archive/DELIVERY_ATLAS_WORKING_v0.1.0.md`).\n\n"
)


OPEN_WORK_ATLAS_CURRENT_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.0.md`; "
    "immediate predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.3.md`; pinned v0.2.1 source-at-freeze artifacts remain preserved; "
    "DERIVED / NON-AUTHORITATIVE; ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)
OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.1.md`; "
    "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.0.md`; pinned v0.2.1 source-at-freeze artifacts remain preserved; "
    "DERIVED / NON-AUTHORITATIVE; ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)
OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE = OPEN_WORK_ATLAS_CURRENT_STATUS_LINE.replace(
    "working/DELIVERY_ATLAS_WORKING_v0.3.0.md",
    "working/DELIVERY_ATLAS_WORKING_v0.2.3.md",
)
OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE = (
    "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.2.3.md`; "
    "predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md`; DERIVED / NON-AUTHORITATIVE; "
    "ATLAS-12 NOT_STARTED; this reconciliation is not ATLAS-12 and this recovery does not create ATLAS-12"
)


def _validate_open_work_atlas_status_line(text: str, expected: str) -> None:
    matches = list(re.finditer(r"(?m)^ATLAS RECONCILIATION: COMPLETE.*$", text))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one Open Work Atlas reconciliation status line, found {len(matches)}")
    start_positions = _line_marker_positions(text, "# 9. Immediate Next Action")
    end_positions = _line_marker_positions(text, "# 10. Minimal Tools")
    if (
        len(start_positions) != 1
        or len(end_positions) != 1
        or not start_positions[0] < matches[0].start() < end_positions[0]
    ):
        raise ValueError("Open Work Atlas reconciliation status line is missing from or relocated outside §9")
    if matches[0].group(0) != expected:
        raise ValueError("Open Work §9 Atlas reconciliation status line differs outside declared lineage clarification")


def _normalise_open_work_successor(text: str, canonical_predecessor: str) -> str:
    _validate_open_work_atlas_status_line(text, OPEN_WORK_ATLAS_CURRENT_STATUS_LINE)
    if text.count(OPEN_WORK_HISTORICAL_ATLAS_BLOCK) != 1:
        raise ValueError("expected exactly one historical Atlas clarification block in Open Work successor")
    if text.count("## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt") != 1:
        raise ValueError("expected exactly one historical Atlas clarification end marker")

    replacements = (
        ("# 02_OPEN_WORK_v1.2.48.md", "# 02_OPEN_WORK_v1.2.47.md", 1),
        ("OPEN-WORK SUCCESSOR v1.2.48", "OPEN-WORK SUCCESSOR v1.2.47", 1),
        ("Document version:** v1.2.48", "Document version:** v1.2.47", 1),
        ("archive/02_OPEN_WORK_v1.2.47.md", "archive/02_OPEN_WORK_v1.2.46.md", 1),
        ("v1.2.47 → v1.2.48", "v1.2.46 → v1.2.47", 1),
        ("DELIVERY_ATLAS_WORKING_v0.3.0.md", "DELIVERY_ATLAS_WORKING_v0.2.3.md", 5),
        ("05_ROADMAP_v1.1.4.md", "05_ROADMAP_v1.1.3.md", 6),
    )
    for current, previous, expected_count in replacements:
        actual_count = text.count(current)
        if actual_count != expected_count:
            raise AssertionError(f"expected {expected_count} Open Work routing replacements for {current!r}, found {actual_count}")
        text = text.replace(current, previous)
    _validate_open_work_atlas_status_line(text, OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE)
    text = text.replace(
        OPEN_WORK_ATLAS_ROUTE_NORMALISED_STATUS_LINE,
        OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE,
        1,
    )
    _validate_open_work_atlas_status_line(text, OPEN_WORK_ATLAS_PREDECESSOR_STATUS_LINE)
    if text.count(OPEN_WORK_HISTORICAL_ATLAS_BLOCK) != 1:
        raise ValueError("historical Atlas clarification block is missing, duplicate, or relocated")
    text = text.replace(
        OPEN_WORK_HISTORICAL_ATLAS_BLOCK,
        OPEN_WORK_HISTORICAL_ATLAS_BLOCK_PREDECESSOR,
        1,
    )
    if text != canonical_predecessor:
        raise ValueError("Open Work successor differs outside declared routing/version, §9 lineage, and historical clarification markers")
    return text


class AuthorityRoutingSuccessorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.governing = {entry["document_id"]: entry for entry in cls.manifest["governing_documents"]}
        cls.historical = {entry["document_id"]: entry for entry in cls.manifest["historical_documents"]}
        cls.readme = _read(DOCS / "README.md")

    def test_current_routing_fields_resolve_to_manifest_and_readme(self):
        current = {doc_id: entry["canonical_filename"] for doc_id, entry in self.governing.items()}
        north_star = _read(DOCS / current["PROJECT_NORTH_STAR_AND_MVP"])
        product = _read(DOCS / current["PLATFORM_BASELINE"])
        roadmap = _read(DOCS / current["ROADMAP"])
        open_work = _read(DOCS / current["OPEN_WORK"])
        atlas = _read(DOCS / "working/DELIVERY_ATLAS_WORKING_v0.3.3.md")
        harden = _read(DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md")

        _validate_north_star_current_state(north_star, self.governing["PROJECT_NORTH_STAR_AND_MVP"]["semver"])
        _validate_product_current_state(product, self.governing["PLATFORM_BASELINE"]["semver"])
        roadmap_header = roadmap.split("## Amendment summary", 1)[0]
        current_product_route = re.search(r"(?m)^- \*\*Current Product authority:\*\* (.+)$", roadmap_header)
        self.assertIsNotNone(current_product_route)
        self.assertEqual(
            [current["PROJECT_NORTH_STAR_AND_MVP"], current["PLATFORM_BASELINE"], current["DECISION_REGISTER"]],
            re.findall(r"[A-Za-z0-9_.-]+_v\d+\.\d+\.\d+\.md", current_product_route.group(1) if current_product_route else ""),
        )
        self.assertIn("01_DECISIONS_v1.5.0.md", product.split("- **Related documents:**", 1)[1].splitlines()[0])
        self.assertIn(current["OPEN_WORK"], product.split("- **Related documents:**", 1)[1].splitlines()[0])
        self.assertIn(current["PROJECT_NORTH_STAR_AND_MVP"], product.split("- **Related documents:**", 1)[1].splitlines()[0])

        atlas_sources = _section(atlas, "# 1. Authority, purpose and boundaries", "## 1.2 Purpose")
        current_rows = {
            line.split("|", 2)[1].strip(): re.findall(r"[A-Za-z0-9_.-]+_v\d+\.\d+\.\d+\.md", line)
            for line in atlas_sources.splitlines()
            if line.startswith("|") and len(line.split("|")) > 2
        }
        self.assertEqual(
            [current["PROJECT_NORTH_STAR_AND_MVP"], current["PLATFORM_BASELINE"], current["DECISION_REGISTER"]],
            current_rows["Product Law"],
        )
        self.assertEqual([current["ROADMAP"]], current_rows["Roadmap"])
        self.assertEqual([current["OPEN_WORK"]], current_rows["Planning tracker"])

        harden_current = _section(harden, "### CURRENT AUTHORITY", "### CURRENT DERIVED EVIDENCE")
        for document_id in (
            "PROJECT_NORTH_STAR_AND_MVP", "PLATFORM_BASELINE", "DECISION_REGISTER",
            "OPEN_WORK", "ROADMAP",
        ):
            self.assertIn(f"`{current[document_id]}`", harden_current)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.3.3.md", _section(harden, "### CURRENT DERIVED EVIDENCE", "### HISTORICAL AUTHORITY / WORKING EVIDENCE"))
        open_work_header = open_work.split("---", 1)[0]
        for document_id in ("PROJECT_NORTH_STAR_AND_MVP", "PLATFORM_BASELINE", "DECISION_REGISTER", "OPEN_WORK", "ROADMAP"):
            if document_id == "OPEN_WORK":
                continue
            self.assertIn(current[document_id], open_work_header)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.3.3.md", open_work_header)
        self.assertIn("working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md", open_work_header)
        active_status = _section(open_work, "# 9. Immediate Next Action", "# 10. Minimal Tools")
        self.assertIn("CURRENT HARDEN-02 STATUS SUCCESSOR: working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md", active_status)
        for filename in (current["PROJECT_NORTH_STAR_AND_MVP"], current["PLATFORM_BASELINE"], current["OPEN_WORK"], current["ROADMAP"]):
            self.assertIn(filename, self.readme)
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.3.3.md", self.readme)
        self.assertIn("working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md", self.readme)

        # These are labelled source-at-freeze provenance, not current routing fields.
        decision_header = _read(DOCS / current["DECISION_REGISTER"]).split("# GQ-001", 1)[0]
        self.assertIn("02_OPEN_WORK_v1.2.46.md", decision_header)
        domain = _read(DOCS / current["DOMAIN_MAP"])
        self.assertIn("Primary inputs — current semantic authority for the v1.2.0 DOL-01 amendment", domain)
        self.assertIn("Product Law `00_PLATFORM_v1.5.0.md` §21S", domain)

        stale_north_star = north_star.replace(
            "Current Product/Decision/Roadmap authority is routed by README and CURRENT_AUTHORITY_MANIFEST.",
            "Current routing is `00_PLATFORM_v1.4.1.md`, `01_DECISIONS_v1.4.1.md`, `02_OPEN_WORK_v1.2.45.md` and `05_ROADMAP_v1.1.2.md`.",
            1,
        )
        with self.assertRaises(ValueError):
            _validate_north_star_current_state(stale_north_star, self.governing["PROJECT_NORTH_STAR_AND_MVP"]["semver"])
        stale_north_star_self_state = north_star.replace("MET (v1.2.5)", "MET (v1.2.2)", 1)
        with self.assertRaises(ValueError):
            _validate_north_star_current_state(stale_north_star_self_state, self.governing["PROJECT_NORTH_STAR_AND_MVP"]["semver"])
        stale_product = product.replace("Current Product Law is v1.5.2", "Current Product Law is v1.4.1", 1)
        with self.assertRaises(ValueError):
            _validate_product_current_state(stale_product, self.governing["PLATFORM_BASELINE"]["semver"])
        stale_roadmap_route = roadmap.replace(
            "00_PLATFORM_v1.5.2.md", "00_PLATFORM_v1.4.1.md", 1
        )
        stale_roadmap_header = stale_roadmap_route.split("## Amendment summary", 1)[0]
        stale_roadmap_match = re.search(r"(?m)^- \*\*Current Product authority:\*\* (.+)$", stale_roadmap_header)
        self.assertNotEqual(
            [current["PROJECT_NORTH_STAR_AND_MVP"], current["PLATFORM_BASELINE"], current["DECISION_REGISTER"]],
            re.findall(r"[A-Za-z0-9_.-]+_v\d+\.\d+\.\d+\.md", stale_roadmap_match.group(1) if stale_roadmap_match else ""),
        )
        stale_open_work = open_work.replace("00_PLATFORM_v1.5.2.md", "00_PLATFORM_v1.4.1.md", 1)
        self.assertNotEqual(open_work_header, stale_open_work.split("---", 1)[0])
        product_lifecycle_mirror = product.replace(
            "Current Product Law is v1.5.2.",
            "Current Product Law is v1.5.2. HARDEN-02 execution is COMPLETE / CERTIFIED.",
            1,
        )
        with self.assertRaises(ValueError):
            _validate_product_current_state(product_lifecycle_mirror, self.governing["PLATFORM_BASELINE"]["semver"])

    def test_readme_and_manifest_resolve_the_expected_current_authority_set(self):
        self.assertEqual(
            CURRENT_AUTHORITY,
            {document_id: self.governing[document_id]["canonical_filename"] for document_id in CURRENT_AUTHORITY},
        )
        context = _section(self.readme, "## Default Agent Context", "## Active Working Artifacts")
        listed = re.findall(r"^\d+\. `([^`]+)`$", context, re.MULTILINE)
        expected = list(CURRENT_AUTHORITY.values())
        self.assertEqual(expected, listed)
        for document_id, filename in CURRENT_AUTHORITY.items():
            entry = self.governing[document_id]
            self.assertEqual(filename, entry["canonical_filename"])
            self.assertEqual(f"docs/00_platform/{filename}", entry["repository_path"])
            self.assertEqual(_sha256(ROOT / entry["repository_path"]), entry["sha256"])
        self.assertEqual(
            _sha256(ROOT / self.governing["OPEN_WORK"]["repository_path"]),
            self.governing["OPEN_WORK"]["provenance_sha256"],
        )

    def test_current_authority_predecessors_are_archived_byte_identically_and_manifested(self):
        historical_ids = {
            "PROJECT_NORTH_STAR_AND_MVP": "PROJECT_NORTH_STAR_AND_MVP_V1_2_2",
            "PLATFORM_BASELINE": "PLATFORM_BASELINE_V1_4_1",
            "DECISION_REGISTER": "DECISION_REGISTER_V1_4_1",
            "OPEN_WORK": "OPEN_WORK_V1_2_48",
            "ROADMAP": "ROADMAP_V1_1_3",
        }
        for document_id, (filename, old_version, new_version, expected_hash) in PREDECESSORS.items():
            with self.subTest(document_id=document_id):
                path = DOCS / "archive" / filename
                self.assertTrue(path.is_file(), path)
                if not path.is_file():
                    continue
                self.assertEqual(expected_hash, _sha256(path))
                entry = self.historical[historical_ids[document_id]]
                self.assertEqual("historical", entry["lifecycle"])
                self.assertEqual(filename, entry["canonical_filename"])
                self.assertEqual(f"docs/00_platform/archive/{filename}", entry["repository_path"])
                self.assertEqual(old_version, entry["semver"])
                self.assertEqual(new_version, entry["superseded_version"])
                self.assertEqual(expected_hash, entry["sha256"])
                self.assertIn(f"archive/{filename}", self.readme)

    def test_six_current_predecessors_match_the_starting_main_git_blobs(self):
        for filename, (expected_blob, expected_sha256) in ARCHIVED_STARTING_MAIN_BLOBS.items():
            with self.subTest(filename=filename):
                archived = DOCS / "archive" / filename
                self.assertTrue(archived.is_file(), archived)
                if not archived.is_file():
                    continue
                self.assertEqual(expected_blob, _git_blob_oid(archived))
                self.assertEqual(expected_sha256, _sha256(archived))

    def test_successor_archives_are_manifested_and_each_successor_normalizes_exactly(self):
        for kind, (successor_name, archive_name) in SUCCESSOR_FILES.items():
            with self.subTest(kind=kind):
                successor_path = DOCS / successor_name
                predecessor_path = DOCS / archive_name
                self.assertTrue(successor_path.is_file(), successor_path)
                self.assertTrue(predecessor_path.is_file(), predecessor_path)
                if not successor_path.is_file() or not predecessor_path.is_file():
                    continue
                predecessor = _read(predecessor_path)
                successor = _read(successor_path)
                self.assertEqual(predecessor, _normalise_successor(kind, successor, predecessor))

        for document_id, (filename, predecessor_version, successor_version, history_id) in CURRENT_SUCCESSOR_PREDECESSORS.items():
            with self.subTest(document_id=document_id):
                entry = self.historical[history_id]
                expected_sha = ARCHIVED_STARTING_MAIN_BLOBS[filename][1]
                self.assertEqual("historical", entry["lifecycle"])
                self.assertEqual(filename, entry["canonical_filename"])
                self.assertEqual(f"docs/00_platform/archive/{filename}", entry["repository_path"])
                self.assertEqual(predecessor_version, entry["semver"])
                self.assertEqual(successor_version, entry["superseded_version"])
                self.assertEqual(expected_sha, entry["sha256"])
                self.assertEqual(expected_sha, entry["provenance_sha256"])

    def test_successor_normalizers_reject_missing_duplicate_relocated_and_unexpected_changes(self):
        for kind, (successor_name, archive_name) in SUCCESSOR_FILES.items():
            successor = _read(DOCS / successor_name)
            predecessor = _read(DOCS / archive_name)
            marker = CURRENT_PATCH_MARKERS[kind]
            malformed = (
                successor.replace(marker, "", 1),
                successor.replace(marker, marker + marker, 1),
                successor.replace(marker, "", 1) + "\n" + marker,
                successor + "\nUNDECLARED CHANGE\n",
            )
            for sample in malformed:
                with self.subTest(kind=kind, sample=sample[:100]):
                    with self.assertRaises(ValueError):
                        _normalise_successor(kind, sample, predecessor)

            route_marker = CURRENT_ROUTE_MUTATIONS[kind]
            changed_route = successor.replace(route_marker, "BROKEN_CURRENT_ROUTE", 1)
            with self.subTest(kind=kind, mutation="current-route"):
                with self.assertRaises(ValueError):
                    _normalise_successor(kind, changed_route, predecessor)

    def test_protected_authorities_and_working_artifacts_match_starting_main(self):
        protected = {
            "01_DECISIONS_v1.5.0.md": "00c046646ff2ef5d6ac3591b4b3392ca63923fb75b986005d9a58c39a2c4c0d2",
            "03_ARCHITECTURE_v1.1.1.md": "342d02a7946f99aca9e6683647fc3a2505901b3d0cc2d13c21d807442025f0b3",
            "04_DOMAIN_MAP_v1.2.0.md": "e09e14ee0a773c5855257c48685cf3a75d413c983a98d22a56b42af57dc2c078",
            "PLATFORM_OPERATING_MODEL_v1.0.1.md": "7cb725adcdb796ba112d39c4be6fd09c90026b49e772b61f0867db62828b9d12",
            "FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md": "58c733e8e0cc73c72b102b623cb756b60cbadb084f8cc710051be42d0877fdb4",
            "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md": "7038f1634677f129ba44230b1f104198a7ab3b4a33e68af5e8cffd5bb87b06dd",
            "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
        }
        for relative_path, expected_sha in protected.items():
            with self.subTest(relative_path=relative_path):
                self.assertEqual(expected_sha, _sha256(DOCS / relative_path))

        for entries in (self.manifest["governing_documents"], self.manifest["reference_documents"], self.manifest["historical_documents"]):
            paths = {entry["repository_path"] for entry in entries}
            self.assertNotIn("docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.3.md", paths)
            self.assertNotIn("docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md", paths)

        graph_paths = self.manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]
        self.assertIn("docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.3.md", graph_paths)
        self.assertIn("docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.5.md", graph_paths)

    def test_product_north_star_decisions_and_roadmap_meaning_is_preserved(self):
        old_north_star = _read(DOCS / "archive" / PREDECESSORS["PROJECT_NORTH_STAR_AND_MVP"][0])
        new_north_star = _read(DOCS / CURRENT_AUTHORITY["PROJECT_NORTH_STAR_AND_MVP"])
        self.assertEqual(
            _section(old_north_star, "# 1. Read This Document First", "# 23. Current Planning Position"),
            _section(new_north_star, "# 1. Read This Document First", "# 23. Current Planning Position"),
        )

        old_product = _read(DOCS / "archive" / PREDECESSORS["PLATFORM_BASELINE"][0])
        new_product = _read(DOCS / CURRENT_AUTHORITY["PLATFORM_BASELINE"])
        old_product_body = _product_body(old_product)
        new_product_body = _successor_product_body_without_authorized_insertion(new_product)
        self.assertEqual(old_product_body, new_product_body)

        old_decisions = _read(DOCS / "archive" / PREDECESSORS["DECISION_REGISTER"][0])
        new_decisions = _read(DOCS / CURRENT_AUTHORITY["DECISION_REGISTER"])
        old_decision_body = old_decisions[old_decisions.index("# GQ-001"):]
        new_decision_body = new_decisions[new_decisions.index("# GQ-001"):]
        old_before_gates, old_gates = old_decision_body.split("# Open Gates", 1)
        new_before_decision, new_tail = new_decision_body.split("## DEC-304 —", 1)
        new_decision, new_gates = new_tail.split("# Open Gates", 1)
        self.assertEqual(old_before_gates, new_before_decision)
        self.assertEqual(old_gates, new_gates)
        old_identifiers = re.findall(r"^## (?:DEC|OQ)-\d{3}", old_decisions, re.MULTILINE)
        new_identifiers = re.findall(r"^## (?:DEC|OQ)-\d{3}", new_decisions, re.MULTILINE)
        self.assertEqual(old_identifiers, [identifier for identifier in new_identifiers if identifier != "## DEC-304"])

        old_roadmap = _read(DOCS / "archive" / PREDECESSORS["ROADMAP"][0])
        new_roadmap = _read(DOCS / CURRENT_AUTHORITY["ROADMAP"])
        old_packs = _feature_pack_sections(old_roadmap)
        new_packs = _feature_pack_sections(new_roadmap)
        self.assertEqual([f"FP-{number:03d}" for number in range(1, 18)], list(old_packs))
        self.assertEqual(list(old_packs), list(new_packs))
        for pack_id in old_packs:
            prior, current = old_packs[pack_id], new_packs[pack_id]
            self.assertEqual(prior, current, pack_id)

    def test_product_successor_exclusion_is_exact_and_fails_closed(self):
        successor = (
            "# 1. Platform Purpose\n\n"
            "Product purpose text.\n\n"
            "# 21S. Marketing Permission and Communication Preferences\n\n"
            "Authorized insertion text.\n\n"
            "# 22. Explicitly Not Yet Decided\n\n"
            "Section 22 text.\n\n"
            "# 23. Current Constraints\n\n"
            "Section 23 text.\n\n"
            "# 24. Current Planning Stop Condition\n\n"
        )
        expected = (
            "# 1. Platform Purpose\n\n"
            "Product purpose text.\n\n"
            "# 22. Explicitly Not Yet Decided\n\n"
            "Section 22 text.\n\n"
            "# 23. Current Constraints\n\n"
            "Section 23 text.\n\n"
        )
        self.assertEqual(expected, _successor_product_body_without_authorized_insertion(successor))

        changed_section_22 = successor.replace("Section 22 text.", "Changed section 22 text.", 1)
        changed_section_23 = successor.replace("Section 23 text.", "Changed section 23 text.", 1)
        self.assertNotEqual(expected, _successor_product_body_without_authorized_insertion(changed_section_22))
        self.assertNotEqual(expected, _successor_product_body_without_authorized_insertion(changed_section_23))

        out_of_order = successor.replace(
            "# 21S. Marketing Permission and Communication Preferences\n\n"
            "Authorized insertion text.\n\n"
            "# 22. Explicitly Not Yet Decided",
            "# 22. Explicitly Not Yet Decided\n\n"
            "# 21S. Marketing Permission and Communication Preferences\n\n"
            "Authorized insertion text.",
            1,
        )
        invalid_successors = (
            successor.replace("# 21S. Marketing Permission and Communication Preferences\n", "", 1),
            successor.replace(
                "# 21S. Marketing Permission and Communication Preferences",
                "# 21S. Marketing Permission and Communication Preferences\n\n"
                "# 21S. Marketing Permission and Communication Preferences",
                1,
            ),
            successor.replace("# 22. Explicitly Not Yet Decided\n", "", 1),
            out_of_order,
            successor.replace(
                "# 22. Explicitly Not Yet Decided",
                "# 22. Explicitly Not Yet Decided\n\n# 22. Explicitly Not Yet Decided",
                1,
            ),
            successor.replace("# 1. Platform Purpose\n", "", 1),
            successor.replace("# 24. Current Planning Stop Condition\n", "", 1),
            successor.replace(
                "# 21S. Marketing Permission and Communication Preferences\n",
                "Prose mentions # 21S. Marketing Permission and Communication Preferences\n",
                1,
            ),
            successor + "# 21S. Marketing Permission and Communication Preferences\n",
            successor.replace(
                "# 22. Explicitly Not Yet Decided\n",
                "Prose mentions # 22. Explicitly Not Yet Decided\n",
                1,
            ),
            successor + "# 22. Explicitly Not Yet Decided\n",
        )
        for invalid_successor in invalid_successors:
            with self.subTest(invalid_successor=invalid_successor):
                with self.assertRaises(ValueError):
                    _successor_product_body_without_authorized_insertion(invalid_successor)

    def test_current_route_and_lifecycle_are_consistent(self):
        readme = self.readme
        north_star = _read(DOCS / CURRENT_AUTHORITY["PROJECT_NORTH_STAR_AND_MVP"])
        product = _read(DOCS / CURRENT_AUTHORITY["PLATFORM_BASELINE"])
        decisions = _read(DOCS / CURRENT_AUTHORITY["DECISION_REGISTER"])
        roadmap = _read(DOCS / CURRENT_AUTHORITY["ROADMAP"])
        open_work = _read(DOCS / CURRENT_AUTHORITY["OPEN_WORK"])
        north_star_current_routing = _section(
            north_star,
            "# 23. Current Planning Position",
            "# 24. Document Stop Condition",
        )
        self.assertIn("README and CURRENT_AUTHORITY_MANIFEST", north_star_current_routing)
        self.assertIn("current Open Work own the active programme stage and NEXT route", north_star_current_routing)
        for stale_filename in (
            "00_PLATFORM_v1.4.1.md",
            "01_DECISIONS_v1.4.1.md",
            "02_OPEN_WORK_v1.2.45.md",
            "05_ROADMAP_v1.1.2.md",
        ):
            self.assertNotIn(stale_filename, north_star_current_routing)
        self.assertIn("README and current Open Work own the active programme stage and NEXT route", north_star_current_routing)
        self.assertIn("MET (v1.2.5)", _section(north_star, "# 24. Document Stop Condition", "**Implementation STOP:**"))
        self.assertIn("02_OPEN_WORK_v1.2.46.md", decisions)
        roadmap_header_marker = "## Amendment summary"
        self.assertEqual(1, roadmap.count(roadmap_header_marker))
        roadmap_header = roadmap.split(roadmap_header_marker, 1)[0]
        for authority_id in (
            "PROJECT_NORTH_STAR_AND_MVP",
            "PLATFORM_BASELINE",
            "DECISION_REGISTER",
            "ARCHITECTURE_SYNTHESIS",
            "DOMAIN_MAP",
        ):
            self.assertIn(self.governing[authority_id]["canonical_filename"], roadmap_header)
        route_match = re.search(r"(?m)^- \*\*Current programme routing:\*\* (.+)$", roadmap_header)
        self.assertIsNotNone(route_match)
        route = route_match.group(1) if route_match else ""
        self.assertIn("README.md", route)
        self.assertIn("current Open Work path it identifies", route)
        self.assertNotRegex(route, r"02_OPEN_WORK_v\d+\.\d+\.\d+\.md")

        product_stop_condition = product.split("# 24. Current Planning Stop Condition", 1)[1]
        self.assertIn("Current Product Law is v1.5.2", product_stop_condition)
        self.assertIn("HARDEN-02 execution status is delegated to README and current Open Work", product_stop_condition)
        self.assertNotIn("ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED", product_stop_condition)
        self.assertIn("Implementation hard stop", product_stop_condition)
        self.assertIn("archive/02_OPEN_WORK_v1.2.45.md", roadmap)
        self.assertNotIn("current tracker `02_OPEN_WORK_v1.2.45.md`", roadmap)
        self.assertNotIn("Current Open Work v1.2.45 records", roadmap)
        fp006 = _feature_pack_sections(roadmap)["FP-006"]
        self.assertIn("PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md", fp006)
        self.assertIn("00_PLATFORM_v1.4.1.md", fp006)
        self.assertIn("source-at-freeze tracker `archive/02_OPEN_WORK_v1.2.45.md §§8, 11`", fp006)
        section_21 = roadmap.split("# 21. Phase 7 handoff", 1)[1]
        self.assertIn("README and current Open Work own programme routing", section_21)
        self.assertNotIn("HARDEN-02", section_21)
        self.assertNotIn("NEXT / AUTHORISED / NOT STARTED", section_21)
        self.assertIn("HARDEN-02 v0.4.0 CONTRACT LIFECYCLE: COMPLETE / CERTIFIED", open_work)
        self.assertIn("HARDEN-02 EXECUTION: COMPLETE / CERTIFIED", open_work)
        self.assertIn("ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED", open_work)
        current_context = _section(readme, "## Default Agent Context", "## Active Working Artifacts")
        for filename in ("00_PLATFORM_v1.5.2.md", "01_DECISIONS_v1.5.0.md", "02_OPEN_WORK_v1.2.51.md", "04_DOMAIN_MAP_v1.2.0.md"):
            self.assertIn(filename, current_context)
        for stale_name in ("00_PLATFORM_v1.5.0.md", "01_DECISIONS_v1.4.1.md", "02_OPEN_WORK_v1.2.49.md", "04_DOMAIN_MAP_v1.1.1.md"):
            self.assertNotIn(stale_name, current_context)
        self.assertIn("ROADMAP AMENDMENT: COMPLETE — current Roadmap `v1.1.6`", readme)
        self.assertEqual("1.2.51", self.governing["OPEN_WORK"]["semver"])

        active_paths = [
            self.readme,
            *(_read(ROOT / entry["repository_path"]) for entry in self.governing.values()),
            _read(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.3.2.md"),
            _read(DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.4.4.md"),
        ]
        stale_patterns = (
            re.compile(r"(?<!archive/)02_OPEN_WORK_v1\.2\.44\.md"),
            re.compile(r"(?<!archive/)02_OPEN_WORK_v1\.2\.48\.md"),
            re.compile(r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.0\.md"),
            re.compile(r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.4\.2\.md"),
        )
        for stale in stale_patterns:
            self.assertFalse(any(stale.search(text) for text in active_paths), stale.pattern)
        guards = self.manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"]
        for guard_text, active, archived in (
            (r"(?<!archive/)02_OPEN_WORK_v1\.2\.48\.md", "02_OPEN_WORK_v1.2.48.md", "archive/02_OPEN_WORK_v1.2.48.md"),
            (r"(?<!archive/)DELIVERY_ATLAS_WORKING_v0\.3\.0\.md", "DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md"),
            (r"(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\.4\.2\.md", "HARDEN-02_CONTRACT_WORKING_v0.4.2.md", "archive/HARDEN-02_CONTRACT_WORKING_v0.4.2.md"),
        ):
            self.assertIn(guard_text, guards)
            guard = re.compile(guard_text)
            self.assertIsNotNone(guard.search(active))
            self.assertIsNone(guard.search(archived))
        self.assertIn("working/DELIVERY_ATLAS_WORKING_v0.2.1.md", _read(DOCS / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"))

    def test_current_open_work_marks_the_v0_2_1_reconciliation_as_historical(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.51.md")
        historical_heading = "## 12.7 — Historical Delivery Atlas reconciliation"
        self.assertEqual(1, current.count(historical_heading))
        if current.count(historical_heading) != 1:
            return

        history = _section(
            current,
            historical_heading,
            "## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt",
        )
        self.assertIn("HISTORICAL COMPLETION RECORD", history)
        self.assertIn(
            "then-current derived / non-authoritative navigation successor was `working/DELIVERY_ATLAS_WORKING_v0.2.1.md`",
            history,
        )
        self.assertIn("not the current Atlas route", history)
        self.assertIn("current Delivery Atlas remains derived/non-authoritative at `working/DELIVERY_ATLAS_WORKING_v0.3.3.md`", current)

    def test_current_open_work_atlas_lineage_distinguishes_current_predecessor_and_pinned_source(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.51.md")
        expected = OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE.replace(
            "working/DELIVERY_ATLAS_WORKING_v0.3.1.md", "working/DELIVERY_ATLAS_WORKING_v0.3.3.md"
        ).replace(
            "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.3.2.md"
        )
        _validate_open_work_atlas_status_line(current, expected)
        self.assertIn("current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.3.md`", expected)
        self.assertIn("immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.2.md`", expected)
        self.assertIn("pinned v0.2.1 source-at-freeze artifacts remain preserved", expected)
        self.assertNotRegex(
            expected,
            r"current Atlas `working/DELIVERY_ATLAS_WORKING_v0\.3\.2\.md`; predecessor `archive/DELIVERY_ATLAS_WORKING_v0\.2\.1\.md`",
        )
        pinned_working = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        pinned_archive = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        self.assertTrue(pinned_working.is_file())
        self.assertTrue(pinned_archive.is_file())
        self.assertEqual(_sha256(pinned_working), _sha256(pinned_archive))

    def test_open_work_normalizer_rejects_invalid_or_relocated_current_atlas_lineage(self):
        current = _read(DOCS / "02_OPEN_WORK_v1.2.51.md")
        line = OPEN_WORK_ATLAS_CURRENT_V031_STATUS_LINE.replace(
            "working/DELIVERY_ATLAS_WORKING_v0.3.1.md", "working/DELIVERY_ATLAS_WORKING_v0.3.3.md"
        ).replace(
            "archive/DELIVERY_ATLAS_WORKING_v0.3.0.md", "archive/DELIVERY_ATLAS_WORKING_v0.3.2.md"
        )
        malformed = (
            current.replace(line + "\n", "", 1),
            current.replace(line, line + "\n" + line, 1),
            current.replace(line + "\n", "", 1).replace(
                "# 10. Minimal Tools", "# 10. Minimal Tools\n" + line, 1
            ),
            current.replace(
                "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.2.md`",
                "predecessor `archive/DELIVERY_ATLAS_WORKING_v0.2.1.md`",
                1,
            ),
        )
        for sample in malformed:
            with self.subTest(sample=sample[:160]):
                with self.assertRaises(ValueError):
                    _validate_open_work_atlas_status_line(sample, line)

    def test_open_work_normalizer_rejects_missing_duplicate_or_relocated_historical_clarification(self):
        current = _read(DOCS / "archive" / "02_OPEN_WORK_v1.2.48.md")
        predecessor = _read(DOCS / "archive" / "02_OPEN_WORK_v1.2.47.md")
        block = OPEN_WORK_HISTORICAL_ATLAS_BLOCK
        missing = current.replace(block, "", 1)
        duplicate = current.replace(block, block + block, 1)
        relocated = current.replace(block, "", 1).replace(
            "## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt",
            block + "## 12.8 — Historical HARDEN-02 contract v0.2.0 attempt",
            1,
        )
        for malformed in (missing, duplicate, relocated):
            with self.subTest(sample=malformed[:160]):
                with self.assertRaises(ValueError):
                    _normalise_open_work_successor(malformed, predecessor)

    def test_open_work_successor_changes_only_routing_metadata_and_preserves_all_gate_state(self):
        predecessor = DOCS / "archive" / "02_OPEN_WORK_v1.2.47.md"
        successor = DOCS / "archive" / "02_OPEN_WORK_v1.2.48.md"
        self.assertTrue(predecessor.is_file(), predecessor)
        self.assertTrue(successor.is_file(), successor)
        if not predecessor.is_file() or not successor.is_file():
            return

        predecessor_text = _read(predecessor)
        successor_text = _read(successor)
        self.assertEqual(
            "71d6f4641cdc70aaa57c8630887d4b24d1a971d34e390c607dda7dbcc8c05118",
            _sha256(predecessor),
        )
        self.assertEqual(predecessor_text, _normalise_open_work_successor(successor_text, predecessor_text))
        for preserved_state in (
            "HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED",
            "Engineering Standards Authority Promotion remains downstream after certified execution",
            "FP-001 reconciliation remains downstream after certified Standards Promotion",
            "Communications follows FP-001 reconciliation",
            "Privacy & Consent, Content & Media, and Audit & Evidence remain conditional / pending explicit adjudication",
            "Analytics remains not required",
            "Phase 7C remains blocked / not started",
            "proof classification remains not finalised",
            "executable development remains blocked until Phase 8 entry conditions pass",
            "Feature Pack count remains **17**",
            "Domain count remains **20**",
        ):
            self.assertIn(preserved_state, successor_text)


if __name__ == "__main__":
    unittest.main()
