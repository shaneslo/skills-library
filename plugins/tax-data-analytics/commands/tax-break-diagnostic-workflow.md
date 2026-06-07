---
name: tax-break-diagnostic-workflow
description: Run an end-to-end tax break diagnosis from intake through remediation staging and report, producing a source-checked break table, staged remediation recommendation, KPI status note, and durable analytical report.
argument-hint: the inbound issue or export to diagnose
# skills-library metadata (ignored by Claude Code; read by the catalog build)
type: workflow
stage: research
tier: 1
source: "OpenAI Data Analytics plugin skills, adapted workflow pack"
domain_fit: >
  Priority 1, directly. This combines data quality, metric diagnostics,
  break triage, KPI readout, and report writing into one analyst workflow for
  inbound tax-reporting issues.
maturity: >
  Author-from-spec workflow assembled from first-party OpenAI Data Analytics
  plugin skills and the repo's tax-ops domain layer. It is prompt-only and
  does not depend on any particular assistant runtime.
trigger: >
  An inbound issue, close checkpoint, client escalation, or workflow item shows
  a break spike, aged backlog, withholding variance, cost-basis discrepancy,
  corrected-form risk, or unexplained tie-out gap.
steps:
  - title: Intake the issue
    asset: tax-metric-movement-diagnostics
    prompt: |
      Restate the issue as a diagnostic question. Identify the metric or discrepancy, time window, comparison period, affected population, suspected source, and the decision needed.
    output: >
      A scoped diagnostic question with assumptions and missing evidence.
  - title: Check source fitness
    asset: tax-data-quality-profiler
    prompt: |
      Profile the provided extract or source summary against its intended grain. Flag freshness, duplicate, missing-field, identifier, date, account-documentation, income-classification, withholding, and cost-basis issues that could change the conclusion.
    output: >
      A dataset fitness finding with severity and source caveats.
  - title: Triage the breaks
    asset: gl-reconciler-break-triage
    prompt: |
      Compare the transaction log and authoritative source. Classify every discrepancy against the break taxonomy. Propose a remediation path for analyst review.
    output: >
      A break table with cause, evidence, confidence, proposed path, and analyst sign-off column.
  - title: Diagnose movement and drivers
    asset: tax-metric-movement-diagnostics
    prompt: |
      Quantify the movement, decompose it by tax form, break cause, income type, account documentation status, security, client, age bucket, and remediation path. Separate verified drivers from hypotheses.
    output: >
      Driver table with contribution, evidence, confidence, caveat, and next validation step.
  - title: Stage remediation recommendation
    asset: gl-reconciler-break-triage
    prompt: |
      For each verified or likely break group, choose UI, XML update, plugin, or write query path under the routing rules. State blast radius, control need, rollback consideration, and whether the recommendation is ready for execution.
    output: >
      Remediation staging table for human approval.
  - title: Prepare status communication
    asset: break-backlog-kpi-readout
    prompt: |
      Convert the findings into a field or leadership status note. Include current status, drivers, risk, caveats, owner action, and next checkpoint.
    output: >
      A polished status note and KPI scorecard.
  - title: Write the durable report
    asset: tax-ops-report-writer
    prompt: |
      Build an answer-first report with evidence, caveats, and next action. Keep it concise, source-backed, and suitable for an operating review.
    output: >
      A finished analytical report with source notes.
gates:
  - >
    Analyst signs off before any remediation path is treated as executable.
  - >
    Change-control owner signs off before any write query, bulk message, or
    recurring tool run.
  - >
    Communication owner approves client-facing or leadership-facing language
    when corrected-form, withholding, or regulatory risk is mentioned.
output: >
  A source-checked break diagnosis, staged remediation table, KPI status note,
  and durable report ready for analyst review.
---

You are running a structured tax break diagnostic workflow. The inbound issue or export is: $ARGUMENTS

Work through each step below in order. At each step, apply the named asset's approach to the available evidence. Do not skip a step and do not treat any remediation path as executable until the human sign-off gates are cleared.

## Step 1: Intake the issue
Asset: tax-metric-movement-diagnostics

Restate the issue as a diagnostic question. Identify the metric or discrepancy, time window, comparison period, affected population, suspected source, and the decision needed.

Deliver: a scoped diagnostic question with assumptions and missing evidence.

## Step 2: Check source fitness
Asset: tax-data-quality-profiler

Profile the provided extract or source summary against its intended grain. Flag freshness, duplicate, missing-field, identifier, date, account-documentation, income-classification, withholding, and cost-basis issues that could change the conclusion.

Deliver: a dataset fitness finding with severity and source caveats.

## Step 3: Triage the breaks
Asset: gl-reconciler-break-triage

Compare the transaction log and authoritative source. Classify every discrepancy against the break taxonomy. Propose a remediation path for analyst review.

Deliver: a break table with cause, evidence, confidence, proposed path, and analyst sign-off column.

## Step 4: Diagnose movement and drivers
Asset: tax-metric-movement-diagnostics

Quantify the movement, decompose it by tax form, break cause, income type, account documentation status, security, client, age bucket, and remediation path. Separate verified drivers from hypotheses.

Deliver: driver table with contribution, evidence, confidence, caveat, and next validation step.

## Step 5: Stage remediation recommendation
Asset: gl-reconciler-break-triage

For each verified or likely break group, choose UI, XML update, plugin, or write query path under the routing rules. State blast radius, control need, rollback consideration, and whether the recommendation is ready for execution.

Deliver: remediation staging table for human approval.

## Step 6: Prepare status communication
Asset: break-backlog-kpi-readout

Convert the findings into a field or leadership status note. Include current status, drivers, risk, caveats, owner action, and next checkpoint.

Deliver: a polished status note and KPI scorecard.

## Step 7: Write the durable report
Asset: tax-ops-report-writer

Build an answer-first report with evidence, caveats, and next action. Keep it concise, source-backed, and suitable for an operating review.

Deliver: a finished analytical report with source notes.

## Human sign-off gates

These gates are mandatory. Do not treat any output as approved or executable until the appropriate owner has signed off.

1. Analyst signs off before any remediation path is treated as executable.
2. Change-control owner signs off before any write query, bulk message, or recurring tool run.
3. Communication owner approves client-facing or leadership-facing language when corrected-form, withholding, or regulatory risk is mentioned.

## Output

A source-checked break diagnosis, staged remediation table, KPI status note, and durable report ready for analyst review.
