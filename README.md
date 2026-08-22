# Agentic Sleep Research

**F65 | L3 Gold Standard | v1.0**

A governed multi-agent research workflow for sleep study context, signal and metadata quality, sleep metric validation, confounder review, evidence appraisal, and qualified human scientific review.

This system supports research and engineering workflows only. It does not diagnose sleep disorders, prescribe medication, authorize treatment, or replace qualified clinical judgment.

## Core agents

- [`study_context_agent.py`](AGENTS/study_context_agent.py)
- [`signal_quality_agent.py`](AGENTS/signal_quality_agent.py)
- [`sleep_metric_agent.py`](AGENTS/sleep_metric_agent.py)
- [`confounder_review_agent.py`](AGENTS/confounder_review_agent.py)
- [`evidence_quality_agent.py`](AGENTS/evidence_quality_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Gold-standard governance

The workflow fails closed when required research gates are incomplete. Required controls include data provenance, signal-quality review, validated sleep metrics, confounder review, evidence review, privacy review, and qualified human approval.

Additional escalation gates cover poor signal quality, possible sleep apnea without sleep-specialist review, safety-sensitive excessive sleepiness without clinical escalation review, unsupported causal claims, patient-specific use, and requests for diagnosis, medication recommendations, or treatment decisions.

Autonomous diagnosis authority: **false**. Autonomous treatment authority: **false**.

## Architecture

[`AGENTS/`](AGENTS/) | [`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and executes correctness linting, pytest, the held-out governance suite, the example workflow, and the smoke run.

```bash
ruff check . --select F,E9
python -m pytest -q
python evals/heldout_suite.py
python examples/example.py
python run.py
```
