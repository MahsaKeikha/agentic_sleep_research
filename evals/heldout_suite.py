from safety.clinical_gate import clinical_gate

BASE = {
    "data_provenance_verified": True,
    "signal_quality_reviewed": True,
    "sleep_metrics_validated": True,
    "confounders_reviewed": True,
    "evidence_reviewed": True,
    "privacy_reviewed": True,
    "human_approval": True,
}

CASES = [
    ("valid", {}, True),
    ("missing_provenance", {"data_provenance_verified": False}, False),
    ("poor_signal", {"signal_quality": "poor"}, False),
    ("unvalidated_metrics", {"sleep_metrics_validated": False}, False),
    ("confounders_missing", {"confounders_reviewed": False}, False),
    ("possible_apnea", {"possible_sleep_apnea": True}, False),
    ("safety_sleepiness", {"safety_sensitive_sleepiness": True}, False),
    ("patient_specific", {"patient_specific_use": True}, False),
    ("treatment_request", {"treatment_decision": "change treatment"}, False),
    ("unsupported_causality", {"unsupported_causal_claim": True}, False),
]


def run() -> None:
    passed = 0
    for name, changes, expected in CASES:
        context = {**BASE, **changes}
        actual = clinical_gate(context)["allowed"]
        if actual != expected:
            raise AssertionError(f"{name}: expected {expected}, got {actual}")
        passed += 1
    print(f"held-out governance: {passed}/{len(CASES)} passed")


if __name__ == "__main__":
    run()
