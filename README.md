# tax-ops-skills library

A copy-and-adapt marketplace of AI assets for enterprise financial services reporting operations. Each asset is self-contained, tool-agnostic prose built to run through an API call on an ingernal AI gateway or Cloud SDK. The Claude Code desktop app is one way to browse and author the assets. It is not where they run. Read [docs/context.md](docs/context.md) first.

## The three plugins

- gainskeeper-operations: exception research, gain/loss tie-out, transaction-log break triage, email and work-item intake routing, and field-status communication.
- tax-data-analytics: metric-movement diagnostics, data-quality profiling, KPI readouts, dashboard briefs, report writing, and the end-to-end break diagnostic workflow.
- tax-ops-shared: shared domain knowledge (break taxonomy, routing rules, tax-form mappings) plus the validate, build, and new-entry authoring commands.

## Docs

- [docs/context.md](docs/context.md) — who/what/when/where/why
- [docs/architecture.md](docs/architecture.md) — the marketplace layout and how it maps from the old content model.


## DRAFT - `tree` patth

## Build the offline catalog

The offline HTML build still reads `[DEPRECTAED]` until the follow-up re-point lands. Install the dev dependencies, validate, then build.

```
pip install -r requirements-dev.txt
python build/build.py --check
python build/build.py
```

The output writes to `[DEPRECATED]`, loads nothing external, and uses no browser storage.
