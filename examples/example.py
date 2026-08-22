from orchestration.orchestrator import orchestrate


print(
    orchestrate(
        {
            "study_question": "review sleep continuity metrics",
            "data_provenance_verified": True,
            "signal_quality_reviewed": True,
            "sleep_metrics_validated": True,
            "confounders_reviewed": True,
            "evidence_reviewed": True,
            "privacy_reviewed": True,
            "human_approval": True,
        }
    )
)
