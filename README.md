# F65 Agentic Sleep Research

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed six-agent reference architecture for sleep research across study context, signal quality, sleep metric validation, confounder review, evidence appraisal, reproducibility, and qualified human scientific review.

F65 is designed for research and engineering workflows involving polysomnography, actigraphy, wearable sleep sensing, longitudinal sleep logs, circadian context, and derived sleep metrics. It organizes evidence and exposes uncertainty without crossing into autonomous diagnosis or treatment.

This repository does not diagnose sleep disorders, prescribe or change medication, authorize treatment, determine clinical fitness, independently interpret a sleep study for patient care, or replace a qualified sleep specialist, clinician, or scientist.

## Six-agent architecture

```text
research question / dataset
          |
          v
 Study Context Agent
          |
          v
 Signal Quality Agent
          |
          v
  Sleep Metric Agent
          |
          v
Confounder Review Agent
          |
          v
Evidence Quality Agent
          |
          v
 Qualified Human Review
```

| Agent | Responsibility | Core question |
|---|---|---|
| Study Context Agent | Research objective, cohort, protocol, modality and provenance | What exactly was measured, in whom, under which protocol and for what research question? |
| Signal Quality Agent | Signal inventory, missingness, artifact, synchronization and acquisition quality | Are the underlying signals sufficiently complete and trustworthy for the intended analysis? |
| Sleep Metric Agent | Derived sleep measures and metric traceability | Are reported sleep metrics defined, calculated and validated consistently with the available signals? |
| Confounder Review Agent | Behavioral, clinical, environmental and methodological confounders | What alternative explanations or measurement conditions could affect the observed result? |
| Evidence Quality Agent | Study-quality appraisal, uncertainty and claim discipline | How strong is the evidence, and are the conclusions proportional to it? |
| Human Review Agent | Qualified scientific or clinical authority boundary | Has an appropriately qualified human reviewed consequential or patient-specific interpretation? |

## Repository structure

```text
AGENTS/
├── study_context_agent.py
├── signal_quality_agent.py
├── sleep_metric_agent.py
├── confounder_review_agent.py
├── evidence_quality_agent.py
└── human_review_agent.py

SKILLS/
├── study_design_reasoning.py
├── signal_reasoning.py
├── metric_reasoning.py
├── confounder_reasoning.py
└── evidence_appraisal.py

TOOLS/
├── signal_inventory_tool.py
├── sleep_log_tool.py
├── metric_table_tool.py
├── confounder_tool.py
└── provenance_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/tests.yml
run.py
README.md
```

The architecture separates reasoning from deterministic evidence handling so research conclusions can be traced back to source signals, protocol context, metrics, and review state.

## Study context

The Study Context Agent establishes the research frame before metrics are interpreted.

A complete context can include:

- research question
- study design
- cohort definition
- inclusion and exclusion criteria
- participant characteristics
- acquisition modality
- recording environment
- protocol version
- recording duration
- time zone and clock alignment
- intervention or exposure status
- repeated-measure schedule
- outcome definitions
- source provenance
- ethics/privacy scope

Sleep data are highly context-sensitive. A metric should not be treated as interchangeable across laboratory PSG, home sleep testing, consumer wearables, research actigraphy, or self-reported sleep diaries.

## Sleep data modalities

F65 is modality-neutral, but common research inputs include:

- polysomnography
- EEG
- EOG
- chin or limb EMG
- ECG
- respiratory airflow
- respiratory effort
- pulse oximetry
- body position
- snoring channels
- actigraphy
- PPG
- accelerometry
- skin temperature
- environmental light
- heart-rate or HRV signals
- sleep diaries
- questionnaires
- wearable-derived sleep stages

Each modality has different accuracy, sampling, artifact, calibration, and interpretation limits. The workflow should preserve those limits explicitly.

## Signal quality

The Signal Quality Agent reviews whether the underlying data can support the intended metric or analysis.

`TOOLS/signal_inventory_tool.py` provides deterministic support for recording available signals and metadata.

Relevant checks can include:

- required signal presence
- sampling frequency
- channel labels
- sensor placement
- time synchronization
- signal dropout
- clipping
- saturation
- motion artifact
- electrode artifact
- missing epochs
- oximetry dropout
- clock drift
- device removal
- battery-related gaps
- recording start/stop anomalies

Poor-quality source data should propagate uncertainty downstream rather than being hidden by a polished summary.

## Polysomnography versus wearable data

PSG and wearable-derived sleep estimates should not be treated as equivalent evidence.

PSG can provide direct multi-channel physiological recordings appropriate for specialist scoring and research-grade staging when acquired and scored under a defined protocol. Wearables often estimate sleep and wake or sleep stages through indirect signals such as motion and PPG.

F65 therefore requires metric provenance to identify:

```text
source modality
sensor/device
algorithm or scoring method
software/model version
analysis window
quality exclusions
human review status
```

A wearable-derived stage estimate should not be represented as if it were manually scored PSG unless the study design and validation evidence justify that comparison.

## Sleep staging boundary

Sleep staging can involve wake, N1, N2, N3, and REM classifications, but the authority and validity of those labels depend on the source signals and scoring method.

F65 can organize stage labels, stage-duration summaries, transition matrices, and algorithm-validation evidence. It must not independently convert an unvalidated signal stream into a clinical sleep-stage interpretation or claim equivalence to specialist PSG scoring without evidence.

## Sleep metrics

The Sleep Metric Agent organizes derived measures through `TOOLS/metric_table_tool.py`.

Common research metrics can include:

- total sleep time
- time in bed
- sleep opportunity
- sleep onset latency
- wake after sleep onset
- sleep efficiency
- number of awakenings
- stage durations
- stage percentages
- REM latency
- arousal indices where appropriately scored
- movement indices
- nap duration
- sleep midpoint
- bedtime and wake-time variability
- interdaily stability or related circadian metrics

Every metric should have a clear definition, unit, source, calculation method, applicable exclusion rules, and provenance.

## Respiratory and oxygen-related metrics

Sleep research can also include respiratory measures such as event counts, oxygen saturation, desaturation indices, and apnea-hypopnea related metrics.

These measures are clinically consequential and protocol-dependent. F65 can preserve reported values and research definitions, but it must not autonomously diagnose obstructive sleep apnea, central sleep apnea, hypoventilation, or another sleep-related breathing disorder.

A possible sleep-apnea signal or abnormal respiratory pattern requires qualified sleep-specialist review before patient-specific interpretation.

## Circadian context

Sleep timing cannot always be understood without circadian and behavioral context.

Relevant variables can include:

- habitual bedtime
- wake time
- sleep midpoint
- shift-work schedule
- travel and jet lag
- time-zone changes
- light exposure
- daytime naps
- social schedule
- chronotype
- seasonal effects
- weekday/weekend differences

Research comparisons should distinguish sleep quantity, sleep timing, circadian phase, and sleep opportunity rather than collapsing them into one concept.

## Sleep logs and longitudinal context

`TOOLS/sleep_log_tool.py` supports structured longitudinal observations.

A sleep-log record can include:

```text
date
bedtime
lights_out
estimated_sleep_onset
awakenings
final_wake_time
out_of_bed_time
nap_periods
subjective_sleep_quality
caffeine_context
alcohol_context
exercise_context
medication_context
notes
```

Longitudinal data can reveal variability that a single-night study cannot. At the same time, self-reported sleep and sensor-derived sleep should remain distinguishable in the evidence model.

## Confounder review

The Confounder Review Agent uses `TOOLS/confounder_tool.py` to record factors that could influence sleep measurements or outcomes.

Common confounders include:

- age
- sex where scientifically relevant
- chronotype
- shift work
- caffeine
- alcohol
- nicotine
- exercise
- acute illness
- pain
- stress
- mood
- medication exposure
- sedating or stimulating substances
- travel
- environmental noise
- light exposure
- room temperature
- device adherence
- first-night effects
- comorbid conditions
- sleep opportunity

The system should not imply causality merely because a sleep metric changes alongside one of these variables.

## Excessive sleepiness and safety-sensitive contexts

Daytime sleepiness can become safety-sensitive when driving, operating machinery, working at height, or performing other hazardous tasks.

F65 can identify that a research record contains a safety-sensitive excessive-sleepiness concern and route it for qualified review. It must not independently determine fitness to drive, fitness for duty, or emergency status.

## Evidence appraisal

The Evidence Quality Agent evaluates whether conclusions are supported by the available design and data.

Relevant questions include:

- Is the study observational or interventional?
- Was the analysis prespecified?
- Was the sample adequate for the claim?
- Were repeated measures handled correctly?
- Were confounders considered?
- Were missing data and exclusions reported?
- Were metrics validated for the device and population?
- Was multiple testing addressed where relevant?
- Is the effect clinically or practically meaningful?
- Is the conclusion causal, associative, descriptive, or exploratory?

Unsupported causal language should fail closed.

## Wearables and algorithm validation

Wearable sleep algorithms may change across firmware, hardware, cloud-processing, or model versions.

A reproducible study should preserve:

- device model
- hardware revision where available
- firmware version
- app/software version
- algorithm/model version where available
- raw versus processed-data distinction
- epoch length
- validation reference
- population used for validation
- known limitations

An algorithm validated in one population or condition should not automatically be assumed valid in another.

## Statistical and ML considerations

Sleep research often uses repeated-night data, longitudinal observations, high-dimensional physiology, and machine learning.

Production research pipelines should guard against:

- participant leakage between train and test sets
- night-level splitting that leaks the same participant across partitions
- post-hoc outcome selection
- uncorrected multiple comparisons
- class imbalance
- site or device confounding
- medication-state confounding
- overfitting
- circular feature selection
- hidden preprocessing differences
- non-independent observations

The unit of independence should be chosen deliberately and documented.

## Provenance and reproducibility

`TOOLS/provenance_tool.py` and the repository memory layer preserve the link between data and conclusions.

Useful provenance includes:

```text
participant_or_dataset_id
source_file_or_record
acquisition_device
acquisition_time
protocol_version
processing_version
metric_definition
algorithm_version
quality_exclusions
analysis_version
review_state
```

A result that cannot be traced back to its source and processing history should not be treated as research-ready.

## Privacy and ethics

Sleep datasets can contain sensitive physiological, behavioral, location, schedule, and health information.

Production research use should define:

- consent or authorization scope
- ethics/IRB status where applicable
- de-identification strategy
- access control
- minimum-necessary data access
- retention policy
- linkage-key handling
- export controls
- wearable-account handling
- third-party cloud considerations

F65 does not substitute for institutional ethics, privacy, or legal review.

## Fail-closed governance

The workflow does not represent a case as research-ready when material evidence is missing.

Blockers can include:

- data provenance unverified
- study context incomplete
- signal inventory incomplete
- poor or unreviewed signal quality
- metric definition missing
- metric validation incomplete
- device or algorithm version unknown when relevant
- confounder review incomplete
- evidence-quality review incomplete
- privacy review missing
- unsupported causal claim
- possible sleep apnea without qualified review
- safety-sensitive excessive sleepiness without escalation review
- patient-specific diagnostic request
- medication recommendation request
- treatment decision request
- unresolved methodological conflict
- qualified human approval missing

Autonomous diagnosis authority: **false**.  
Autonomous medication authority: **false**.  
Autonomous treatment authority: **false**.

## Human authority boundary

F65 must not autonomously:

- diagnose insomnia
- diagnose sleep apnea
- diagnose narcolepsy
- diagnose parasomnias
- diagnose circadian-rhythm disorders
- interpret a patient PSG as a final clinical study
- prescribe or modify medication
- recommend PAP or another treatment as a patient-specific clinical order
- determine fitness to drive or fitness for duty
- provide clinical clearance
- replace specialist sleep-study interpretation

Qualified professionals retain all consequential scientific and clinical authority.

## End-to-end reference workflow

A typical F65 workflow follows this sequence:

1. Define the research question and protocol context.
2. Record cohort and acquisition modality.
3. Capture data provenance and device/software versions.
4. Inventory available signals.
5. Review signal quality and missingness.
6. Define sleep metrics and calculation methods.
7. Validate metric applicability to the source modality.
8. Review behavioral, environmental, medication, and clinical confounders.
9. Appraise the strength of the resulting evidence.
10. Flag possible respiratory or safety-sensitive concerns for qualified review.
11. Preserve uncertainty, provenance, and unresolved questions.
12. Require qualified human review before patient-specific or consequential use.

## Observability

The `observability/` layer supports traceability of the multi-agent workflow.

Useful workflow telemetry includes:

- signal-quality failures
- missing-signal counts
- metric-validation failures
- provenance gaps
- confounder-review status
- evidence-quality state
- escalation events
- unresolved questions
- human-review status

Observability measures workflow performance. They do not establish clinical accuracy by themselves.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/reference_case.json
evals/evaluate.py
evals/heldout_suite.py
```

Held-out evaluation should measure governance behavior rather than generic prose quality.

Useful evaluation dimensions include:

- provenance-gap detection
- poor-signal detection
- missing-signal handling
- invalid-metric detection
- modality-mismatch detection
- confounder-gap detection
- unsupported-causal-claim detection
- respiratory-concern escalation
- excessive-sleepiness escalation
- patient-specific diagnosis blocking
- medication/treatment blocking
- privacy-gate enforcement
- human-review enforcement

## Verification and CI

CI runs on Python 3.10, 3.11, and 3.12 and executes:

```bash
ruff check . --select F,E9
python -m pytest -q
python evals/heldout_suite.py
python examples/example.py
python run.py
```

For production research systems, additional validation should cover modality-specific fixtures, device-version changes, missing-data behavior, signal dropout, clock synchronization, metric regression, wearable algorithm changes, longitudinal participant splitting, privacy controls, and reproducibility across software versions.

## Explicit failure states

Useful states include:

```text
STUDY CONTEXT INCOMPLETE
PROVENANCE UNVERIFIED
SIGNAL INVENTORY INCOMPLETE
SIGNAL QUALITY FAILED
METRIC DEFINITION MISSING
METRIC VALIDATION INCOMPLETE
CONFOUNDER REVIEW REQUIRED
EVIDENCE QUALITY REVIEW REQUIRED
PRIVACY REVIEW REQUIRED
CAUSAL CLAIM UNSUPPORTED
SLEEP SPECIALIST REVIEW REQUIRED
SAFETY ESCALATION REQUIRED
PATIENT-SPECIFIC DIAGNOSIS BLOCKED
TREATMENT AUTHORITY BLOCKED
HUMAN REVIEW REQUIRED
```

The system should never fabricate signal quality, sleep stages, respiratory events, metrics, device validation, clinical interpretation, or human approval.

## L3 Gold Standard

F65 follows the library's L3 Gold Standard pattern through specialist-agent separation, deterministic tools, explicit governance gates, held-out evaluation, observability, CI, provenance controls, and mandatory human authority.

This designation describes repository engineering maturity. It is not clinical validation, diagnostic certification, regulatory authorization, or evidence that the system can replace professional sleep-study interpretation.

## Extending F65

Common extensions include:

- PSG data adapters
- EDF/EDF+ import
- BIDS-compatible sleep datasets
- actigraphy platforms
- wearable APIs
- PPG pipelines
- environmental light sensors
- circadian-analysis modules
- sleep-diary apps
- questionnaire systems
- research EDC platforms
- statistical-analysis pipelines
- device-validation registries
- reproducible notebook pipelines
- longitudinal dashboards

Extensions should preserve source provenance, modality boundaries, algorithm versioning, validation evidence, privacy, and human review.

## Design principles

1. Define study context before interpreting metrics.
2. Treat signal quality as a prerequisite, not an afterthought.
3. Keep PSG, wearable, actigraphy, and self-report evidence distinct.
4. Make every sleep metric traceable to a definition and source.
5. Review behavioral, environmental, medication, and methodological confounders.
6. Separate association from causation.
7. Preserve device and algorithm versions for reproducibility.
8. Escalate respiratory and safety-sensitive concerns without diagnosing them.
9. Fail closed when evidence or provenance is incomplete.
10. Keep consequential clinical and scientific authority with qualified humans.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

This repository is intended to function as a reusable technical reference for multi-agent sleep-research architecture. Cite the repository and its version when adapting its architecture, evaluation patterns, governance model, or implementation concepts.

## Responsible use

Use F65 as a research and engineering reference. Validate all signals, algorithms, derived metrics, statistical methods, device assumptions, privacy requirements, and scientific conclusions against the actual study protocol and population. Patient-specific diagnostic and treatment decisions remain exclusively with appropriately qualified healthcare professionals.