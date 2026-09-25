"""Validate formal Phase 7 and Phase 8 entry implications from Open Work state."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
from typing import Any


PHASE_7C_STATES = frozenset({"BLOCKED / NOT_STARTED", "READY", "STARTED", "COMPLETE"})
ACTIVE_PHASE_7C_STATES = frozenset({"READY", "STARTED", "COMPLETE"})
ARTIFACT_STATUSES = frozenset({"NOT_STARTED", "IN_PROGRESS", "COMPLETE", "APPROVED"})
COMPLETE_ARTIFACT_STATUSES = frozenset({"COMPLETE", "APPROVED"})
FORMAL_ARTIFACT_TYPES = frozenset(
    {
        "FEATURE_PACK_SKELETON_GATE_MANIFEST",
        "JIT_DOMAIN_DOSSIER",
        "FINAL_FEATURE_PACK_CONTRACT",
        "ARCHITECTURAL_PROOF",
        "TRACER_BULLET",
        "PRE_JIT_CONTRACT",
    }
)
REQUIRED_ARTIFACT_TYPES = {
    "FP001_SKELETON_GATE_MANIFEST": "FEATURE_PACK_SKELETON_GATE_MANIFEST",
    "FP001_IDENTITY_ACCESS_JIT": "JIT_DOMAIN_DOSSIER",
    "FP001_COMMUNICATIONS_JIT": "JIT_DOMAIN_DOSSIER",
    "FP001_FINAL_CONTRACT": "FINAL_FEATURE_PACK_CONTRACT",
}
CONDITIONAL_DOSSIER_ARTIFACT_IDS = {
    "privacy_consent": "FP001_PRIVACY_CONSENT_JIT",
    "content_media": "FP001_CONTENT_MEDIA_JIT",
    "audit_evidence": "FP001_AUDIT_EVIDENCE_JIT",
}
CONDITIONAL_DOSSIER_STATES = frozenset(
    {
        "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "NOT REQUIRED",
        "REQUIRED / NOT_STARTED",
        "REQUIRED / IN_PROGRESS",
        "REQUIRED / COMPLETE",
        "REQUIRED / APPROVED",
    }
)
FINAL_PROOF_CLASSIFICATIONS = frozenset({"REUSE_EXISTING_PROOF", "NEW_TRACER_BULLET"})


def _registered_artifacts(
    state: dict[str, Any], root: Path
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    raw_artifacts = state.get("formal_artifacts")
    if not isinstance(raw_artifacts, list):
        return {}, ["formal_artifacts must be an array"]

    artifacts: dict[str, dict[str, Any]] = {}
    issues: list[str] = []
    for index, artifact in enumerate(raw_artifacts):
        if not isinstance(artifact, dict):
            issues.append(f"formal_artifacts[{index}] must be an object")
            continue
        registry_id = artifact.get("registry_id")
        formal_type = artifact.get("formal_type")
        path_value = artifact.get("path")
        status = artifact.get("status")
        requirement = artifact.get("requirement")
        if not isinstance(registry_id, str) or not registry_id:
            issues.append(f"formal_artifacts[{index}].registry_id must be a non-empty string")
            continue
        if registry_id in artifacts:
            issues.append(f"formal artifact identity {registry_id} is duplicated")
        else:
            artifacts[registry_id] = artifact
        if not isinstance(formal_type, str) or formal_type not in FORMAL_ARTIFACT_TYPES:
            issues.append(f"{registry_id}: invalid formal_type {formal_type!r}")
        if not isinstance(status, str) or status not in ARTIFACT_STATUSES:
            issues.append(f"{registry_id}: invalid status {status!r}")
        if not isinstance(requirement, str) or requirement not in {"REQUIRED", "CONDITIONAL", "OPTIONAL"}:
            issues.append(f"{registry_id}: invalid requirement {requirement!r}")
        if path_value is not None and not isinstance(path_value, str):
            issues.append(f"{registry_id}: path must be a repository-relative string or null")
        elif isinstance(path_value, str):
            safe_path = _safe_registered_path(path_value)
            if safe_path is None:
                issues.append(f"{registry_id}: path {path_value!r} is not normalized and repository-relative")
            else:
                try:
                    resolved_root = root.resolve()
                    resolved_path = root.joinpath(*safe_path.parts).resolve(strict=False)
                    resolved_path.relative_to(resolved_root)
                    if status in COMPLETE_ARTIFACT_STATUSES and not resolved_path.is_file():
                        issues.append(f"{registry_id}: completed artifact path does not identify a repository file")
                except (OSError, RuntimeError, ValueError):
                    issues.append(f"{registry_id}: path {path_value!r} resolves outside the repository")
        if status == "NOT_STARTED" and path_value is not None:
            issues.append(f"{registry_id}: NOT_STARTED artifact must not declare a path")

    for registry_id, expected_type in REQUIRED_ARTIFACT_TYPES.items():
        artifact = artifacts.get(registry_id)
        if artifact is None:
            issues.append(f"required formal artifact {registry_id} is not registered")
        elif artifact.get("formal_type") != expected_type:
            issues.append(
                f"{registry_id}: expected formal_type {expected_type!r}, got {artifact.get('formal_type')!r}"
            )
        elif artifact.get("requirement") != "REQUIRED":
            issues.append(f"{registry_id}: requirement must remain REQUIRED")

    return artifacts, issues


def _safe_registered_path(relative: str) -> Path | None:
    if not relative or "\\" in relative:
        return None
    path = PurePosixPath(relative)
    if path.is_absolute() or path.as_posix() != relative or any(part in {".", ".."} for part in path.parts):
        return None
    return Path(relative)


def _artifact_is_complete(
    artifacts: dict[str, dict[str, Any]],
    registry_id: str,
    formal_type: str,
    root: Path,
) -> bool:
    artifact = artifacts.get(registry_id)
    if artifact is None or artifact.get("formal_type") != formal_type:
        return False
    status = artifact.get("status")
    if not isinstance(status, str) or status not in COMPLETE_ARTIFACT_STATUSES:
        return False
    path_value = artifact.get("path")
    safe_path = _safe_registered_path(path_value) if isinstance(path_value, str) else None
    if safe_path is None:
        return False
    try:
        resolved_root = root.resolve()
        resolved_path = root.joinpath(*safe_path.parts).resolve(strict=False)
        resolved_path.relative_to(resolved_root)
    except (OSError, RuntimeError, ValueError):
        return False
    return resolved_path.is_file()


def validate_phase_7_state(state: dict[str, Any], root: Path) -> dict[str, Any]:
    """Check registered artifact identity and Phase 7/8 transition implications."""

    root = Path(root)
    checks: list[dict[str, str]] = []
    findings: list[dict[str, str]] = []

    def record(name: str, passed: bool, message: str) -> None:
        status = "PASS" if passed else "FAIL"
        checks.append({"name": name, "status": status, "message": message})
        if not passed:
            findings.append({"check": name, "message": message})

    artifacts, registry_issues = _registered_artifacts(state, root)
    record(
        "phase_7_formal_artifact_registry",
        not registry_issues,
        "formal artifact registry has unique identities and required formal types"
        if not registry_issues
        else "; ".join(registry_issues),
    )

    phase_7c = state.get("phase_7c")
    phase_state_valid = isinstance(phase_7c, str) and phase_7c in PHASE_7C_STATES
    record(
        "phase_7c_state",
        phase_state_valid,
        "Phase 7C state uses a supported lifecycle value"
        if phase_state_valid
        else f"unsupported Phase 7C state {phase_7c!r}",
    )
    phase_7c_active = phase_state_valid and phase_7c in ACTIVE_PHASE_7C_STATES

    communications_state = state.get("communications")
    communications_state_valid = isinstance(communications_state, str) and communications_state in {
        "REQUIRED / NOT_STARTED",
        "REQUIRED / IN_PROGRESS",
        "REQUIRED / COMPLETE",
        "REQUIRED / APPROVED",
    }
    communications_state_complete = isinstance(communications_state, str) and communications_state in {
        "REQUIRED / COMPLETE",
        "REQUIRED / APPROVED",
    }
    communications_artifact_complete = _artifact_is_complete(
        artifacts,
        "FP001_COMMUNICATIONS_JIT",
        "JIT_DOMAIN_DOSSIER",
        root,
    )
    communications_ready = communications_state_complete and communications_artifact_complete
    record(
        "phase_7c_communications_gate",
        communications_state_valid and (not phase_7c_active or communications_ready),
        "required Communications JIT dossier is complete before Phase 7C"
        if communications_ready
        else f"unsupported Communications state {communications_state!r}"
        if not communications_state_valid
        else "Phase 7C requires Communications state and a registered complete JIT Domain Dossier"
        if phase_7c_active
        else "Phase 7C remains blocked while required Communications work is incomplete",
    )

    conditional = state.get("conditional_dossiers")
    conditional_issues: list[str] = []
    conditional_structure_valid = True
    conditional_ready = isinstance(conditional, dict)
    if not isinstance(conditional, dict):
        conditional_structure_valid = False
        conditional_issues.append("conditional_dossiers must be an object")
    else:
        expected_keys = set(CONDITIONAL_DOSSIER_ARTIFACT_IDS) | {"analytics"}
        missing = sorted(expected_keys - set(conditional))
        extra = sorted(set(conditional) - expected_keys)
        if missing or extra:
            conditional_structure_valid = False
            conditional_ready = False
            conditional_issues.append(f"conditional dossier keys differ; missing={missing}, extra={extra}")
        for dossier_id in expected_keys:
            disposition = conditional.get(dossier_id)
            if not isinstance(disposition, str) or disposition not in CONDITIONAL_DOSSIER_STATES:
                conditional_structure_valid = False
                conditional_ready = False
                conditional_issues.append(f"{dossier_id}: unsupported disposition {disposition!r}")
                continue
            if disposition == "CONDITIONAL / PENDING EXPLICIT ADJUDICATION":
                conditional_ready = False
                conditional_issues.append(f"{dossier_id}: explicit adjudication is pending")
            elif dossier_id == "analytics" and disposition != "NOT REQUIRED":
                conditional_structure_valid = False
                conditional_ready = False
                conditional_issues.append("analytics remains NO DOSSIER under the current Phase 7A selection")
            elif disposition.startswith("REQUIRED /"):
                artifact_id = CONDITIONAL_DOSSIER_ARTIFACT_IDS.get(dossier_id)
                complete = artifact_id is not None and _artifact_is_complete(
                    artifacts,
                    artifact_id,
                    "JIT_DOMAIN_DOSSIER",
                    root,
                )
                if disposition not in {"REQUIRED / COMPLETE", "REQUIRED / APPROVED"} or not complete:
                    conditional_ready = False
                    conditional_issues.append(
                        f"{dossier_id}: required conditional JIT dossier must be registered and complete"
                    )
    record(
        "phase_7c_conditional_dossiers_gate",
        conditional_structure_valid and (not phase_7c_active or conditional_ready),
        "conditional dossiers have explicit dispositions and required dossiers are complete"
        if conditional_ready
        else "; ".join(conditional_issues)
        if phase_7c_active
        else "Phase 7C remains blocked while conditional dispositions await adjudication",
    )

    proof_classification = state.get("proof_classification")
    proof_unfinalised = proof_classification == "NOT FINALISED"
    proof_final = isinstance(proof_classification, str) and proof_classification in FINAL_PROOF_CLASSIFICATIONS
    contract_approved = _artifact_is_complete(
        artifacts,
        "FP001_FINAL_CONTRACT",
        "FINAL_FEATURE_PACK_CONTRACT",
        root,
    ) and artifacts.get("FP001_FINAL_CONTRACT", {}).get("status") == "APPROVED"
    proof_ready = proof_unfinalised or (
        proof_final and phase_7c == "COMPLETE" and contract_approved
    )
    record(
        "phase_8_proof_classification_gate",
        proof_ready,
        "proof classification follows an approved Final Feature Pack Contract"
        if proof_ready
        else f"proof classification {proof_classification!r} requires completed Phase 7C and an approved registered Final Feature Pack Contract",
    )

    application_state = state.get("application_implementation")
    application_blocked = application_state == "BLOCKED"
    application_authorised = application_state == "AUTHORISED"
    skeleton_complete = _artifact_is_complete(
        artifacts,
        "FP001_SKELETON_GATE_MANIFEST",
        "FEATURE_PACK_SKELETON_GATE_MANIFEST",
        root,
    )
    identity_complete = _artifact_is_complete(
        artifacts,
        "FP001_IDENTITY_ACCESS_JIT",
        "JIT_DOMAIN_DOSSIER",
        root,
    )
    entry_ready = (
        phase_7c == "COMPLETE"
        and communications_ready
        and conditional_ready
        and skeleton_complete
        and identity_complete
        and contract_approved
        and proof_final
    )
    record(
        "development_entry_formal_gate",
        application_blocked or (application_authorised and entry_ready),
        "application implementation remains blocked until formal Phase 7 and Phase 8 entry state is present"
        if application_blocked
        else "formal Phase 7 and Phase 8 entry requirements are present"
        if application_authorised and entry_ready
        else f"application implementation state {application_state!r} is invalid or lacks complete formal Phase 7 and Phase 8 entry state",
    )

    return {
        "status": "PASS" if not findings else "FAIL",
        "assertion_count": len(checks),
        "checks": checks,
        "findings": findings,
    }
