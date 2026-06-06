# tax-data-analytics

Diagnostics and reporting over tax-ops data. This plugin holds the assets that explain why a metric moved, profile data quality, and turn findings into a readout, a brief, or a written report. One command stitches the skills into an end-to-end break diagnostic.

## What it holds

One command and five skills.

Command:
- `tax-break-diagnostic-workflow` — runs the full diagnostic, from metric movement to a written conclusion, with a human sign-off gate before any remediation.

Skills:
- `tax-metric-movement-diagnostics` — explains a period-over-period metric change and isolates the driver.
- `tax-data-quality-profiler` — profiles a dataset for completeness, validity, and anomalies.
- `break-backlog-kpi-readout` — reads the break-backlog KPIs and calls out what changed and why.
- `tax-ops-dashboard-brief` — turns a dashboard into a short brief for leadership.
- `tax-ops-report-writer` — writes the formal report from the analysis.

## How the bodies read

Every body is tool-agnostic prose that works pasted into an API call. Firm specifics live in bracketed `[INSERT: ...]` placeholders an analyst fills at use time. The placeholders are the intended terminal form, not an unfinished draft. Domain rules come from the `tax-ops-domain` skill in the `tax-ops-shared` plugin.
