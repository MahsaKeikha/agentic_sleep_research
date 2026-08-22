from orchestration.orchestrator import orchestrate
from safety.clinical_gate import clinical_gate


def valid_context():
    return {
        "data_provenance_verified": True,
        "signal_quality_reviewed": True,
        "sleep_metrics_validated": True,
        "confounders_reviewed": True,
        "evidence_reviewed": True,
        "privacy_reviewed": True,
        "human_approval": True,
    }


def test_valid_research_context_can_pass():
    result = orchestrate(valid_context())
    assert result["approved"] is True
    assert len(result["workflow"]) == 6


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert clinical_gate(context)["allowed"] is False


def test_poor_signal_quality_fails_closed():
    context = valid_context()
    context["signal_quality"] = "poor"
    assert clinical_gate(context)["allowed"] is False


def test_possible_sleep_apnea_requires_specialist_review():
    context = valid_context()
    context["possible_sleep_apnea"] = True
    result = clinical_gate(context)
    assert result["allowed"] is False
    assert any("sleep-specialist" in reason for reason in result["reasons"])


def test_safety_sensitive_sleepiness_requires_escalation():
    context = valid_context()
    context["safety_sensitive_sleepiness"] = True
    assert clinical_gate(context)["allowed"] is False


def test_clinical_authority_is_prohibited():
    context = valid_context()
    context["treatment_decision"] = "start therapy"
    result = clinical_gate(context)
    assert result["allowed"] is False
    assert result["autonomous_treatment_authority"] is False


def test_patient_specific_use_fails_closed():
    context = valid_context()
    context["patient_specific_use"] = True
    assert clinical_gate(context)["allowed"] is False


def test_unsupported_causal_claim_fails_closed():
    context = valid_context()
    context["unsupported_causal_claim"] = True
    assert clinical_gate(context)["allowed"] is False
