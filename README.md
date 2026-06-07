# tax-ops skills library

A copy-and-adapt marketplace of AI assets for Goldman Sachs prime-brokerage tax-reporting operations. Each asset is self-contained, tool-agnostic prose built to run through an API call on a firm gateway or Cloud SDK. The Claude Code desktop app is one way to browse and author the assets. It is not where they run. Read [docs/north-star.md](docs/north-star.md) first.

## The three plugins

- gainskeeper-operations: exception research, gain/loss tie-out, transaction-log break triage, email and work-item intake routing, and field-status communication.
- tax-data-analytics: metric-movement diagnostics, data-quality profiling, KPI readouts, dashboard briefs, report writing, and the end-to-end break diagnostic workflow.
- tax-ops-shared: shared domain knowledge (break taxonomy, routing rules, tax-form mappings) plus the validate, build, and new-entry authoring commands.

## Docs

- [docs/north-star.md](docs/north-star.md) — the purpose, the three-test framework, and the most valued asset shape.
- [docs/architecture.md](docs/architecture.md) — the marketplace layout and how it maps from the old content model.
- [docs/authoring-plugins.md](docs/authoring-plugins.md) — how to add a skill, agent, or command, with the frontmatter contract.

## Install via Claude Code

Add the marketplace, then install the plugins you want.

```
/plugin marketplace add shaneslo/skills-library
/plugin install gainskeeper-operations
/plugin install tax-data-analytics
/plugin install tax-ops-shared
```

## Build the offline catalog

The offline HTML build still reads `content/entries/` until the follow-up re-point lands. Install the dev dependencies, validate, then build.

```
pip install -r requirements-dev.txt
python build/build.py --check
python build/build.py
```

The output writes to `dist/skills-library.html`, loads nothing external, and uses no browser storage.
