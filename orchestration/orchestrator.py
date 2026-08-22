from AGENTS.confounder_review_agent import ConfounderReviewAgent
from AGENTS.evidence_quality_agent import EvidenceQualityAgent
from AGENTS.human_review_agent import HumanReviewAgent
from AGENTS.signal_quality_agent import SignalQualityAgent
from AGENTS.sleep_metric_agent import SleepMetricAgent
from AGENTS.study_context_agent import StudyContextAgent
from safety.clinical_gate import clinical_gate

AGENTS = [
    StudyContextAgent(),
    SignalQualityAgent(),
    SleepMetricAgent(),
    ConfounderReviewAgent(),
    EvidenceQualityAgent(),
    HumanReviewAgent(),
]


def orchestrate(context: dict) -> dict:
    """Run the F65 research workflow and enforce fail-closed governance."""
    outputs = [agent.run(context) for agent in AGENTS]
    gate = clinical_gate(context)
    return {
        "system": "F65",
        "workflow": [output["agent"] for output in outputs],
        "agent_outputs": outputs,
        "governance": gate,
        "approved": gate["allowed"],
        "status": "approved_for_research_use" if gate["allowed"] else "review_required",
    }
