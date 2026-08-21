# Agentic Sleep Research

F65 in the Agentic AI Library.

A standalone multi-agent research workflow for sleep study planning, signal and metadata review, sleep metric synthesis, confounder review, evidence appraisal, and human scientific review.

This system supports research only and does not diagnose sleep disorders or provide treatment decisions.

## Core agents

- [`study_context_agent.py`](AGENTS/study_context_agent.py)
- [`signal_quality_agent.py`](AGENTS/signal_quality_agent.py)
- [`sleep_metric_agent.py`](AGENTS/sleep_metric_agent.py)
- [`confounder_review_agent.py`](AGENTS/confounder_review_agent.py)
- [`evidence_quality_agent.py`](AGENTS/evidence_quality_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Architecture

[`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Run

```bash
python run.py
```
