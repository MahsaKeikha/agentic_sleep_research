CLINICAL_AUTHORITY_KEYS = {
    "diagnosis",
    "prescription",
    "medication_recommendation",
    "treatment_decision",
    "treatment_authorization",
}

REQUIRED_RESEARCH_GATES = {
    "data_provenance_verified": "data provenance must be verified",
    "signal_quality_reviewed": "signal quality must be reviewed",
    "sleep_metrics_validated": "sleep metrics must be validated",
    "confounders_reviewed": "confounders must be reviewed",
    "evidence_reviewed": "evidence quality must be reviewed",
    "privacy_reviewed": "privacy and data handling must be reviewed",
    "human_approval": "qualified human scientific review is required",
}


def clinical_gate(context: dict) -> dict:
    """Fail closed when research quality or clinical authority boundaries are unmet."""
    reasons: list[str] = []

    for key, message in REQUIRED_RESEARCH_GATES.items():
        if context.get(key) is not True:
            reasons.append(message)

    if any(key in context for key in CLINICAL_AUTHORITY_KEYS):
        reasons.append("patient-specific diagnosis or treatment authority is prohibited")

    if context.get("patient_specific_use") is True:
        reasons.append("patient-specific use requires qualified clinical review outside this system")

    if context.get("possible_sleep_apnea") is True and context.get("sleep_specialist_reviewed") is not True:
        reasons.append("possible sleep apnea requires qualified sleep-specialist review")

    if context.get("safety_sensitive_sleepiness") is True and context.get("clinical_escalation_reviewed") is not True:
        reasons.append("safety-sensitive excessive sleepiness requires clinical escalation review")

    if context.get("signal_quality") == "poor":
        reasons.append("poor signal quality prevents reliable sleep research interpretation")

    if context.get("unsupported_causal_claim") is True:
        reasons.append("unsupported causal claims are prohibited")

    allowed = not reasons
    return {
        "allowed": allowed,
        "requires_human_review": True,
        "reasons": reasons,
        "autonomous_diagnosis_authority": False,
        "autonomous_treatment_authority": False,
    }
