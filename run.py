from orchestration.orchestrator import orchestrate


if __name__ == "__main__":
    print(
        orchestrate(
            {
                "goal": "sleep research support",
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
