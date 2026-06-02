# CLAUDE.md

Guidance for Claude Code in this repo. The project files are the source of truth. Read them before acting. The move to Claude Code is settled; do not re-open it.

## What this repo is
A copy-and-adapt library of AI assets (prompts, skills, agents, workflows) for Goldman Sachs prime brokerage tax-reporting operations. Content is tool-agnostic and compiles to one offline HTML file. The execution layer can change without rewriting content.

## Me
Finance operations on GS prime brokerage client tax reporting.

## Workflow spine
1. Receive issues by email or workflow that need research.
2. Open the client account and the back-office transaction log, review it.
3. Decide whether a manual update is needed and how: UI, XML, SQL, or plugin.
4. Communicate status to the field and to leadership.
5. Analyze internal KB articles, client statements, and tax documents.

## Domain weighting
Reconciliation, exception research and handling, cost-basis and transaction analysis, tax and regulatory reporting, trade support, issue classification and routing.

## Core principle
The question is never which tools we have, but what exists that works. Three tests for any asset: understand it, decompose it to its core function and rebuild it, adapt it to the domain now. Treat credible repos as specifications, not software: harvest the decomposition, drop code that will not run, re-express the rest as prompts the available assistant runs. The edge is the domain knowledge poured into the gap the repo cannot fill.

## Domain terminology
Break: a reconciliation discrepancy to research and resolve. Tie-out: reconcile a statement against an authoritative source. Cost basis: original asset value for tax gain and loss. Remediation path: UI, XML, SQL, or plugin. 1099-DIV/B/INT, 1042-S, FATCA, CRS: the reporting forms and regimes. Full definitions live in `memory/glossary.md`. Full break taxonomy, routing rules, and tax-form mappings live in the domain skill below.

## Where things live
- `content/entries/*.yaml` — one asset per file. Schema in `SKILLS_LIBRARY_SPEC.md` section 4 (assets) and section 5 (workflows).
- `build/build.py` — validates content and compiles the HTML.
- `build/template.html` — the offline shell. No external dependencies.
- `dist/skills-library.html` — generated output. Do not hand-edit.
- `.claude/skills/tax-ops-domain.md` — break taxonomy, routing rules, tax-form mappings, three-test framework. Load it when authoring or adapting an entry.
- `.claude/skills/build-pipeline.md` — how to validate and build.
- `SKILLS_LIBRARY_SPEC.md` — the contract. Section 8 is the quality bar.
- `memory/` — operator context, the cold store this file defers to. `memory/README.md` defines the layer and its boundary with the build. `memory/glossary.md` holds full term definitions, `memory/company.md` the environment, `memory/projects/skills-library.md` this repo's dossier. None of it compiles into `dist/`.

## Build commands
- `/validate` — check every entry against the schema and the four hard rules. No build.
- `/build` — validate, compile, confirm the output loads nothing external, report the path.
- `/new-entry` — scaffold a content entry with every schema field pre-filled.

## Writing preferences
BLUF. Specific over general, decisive. No em dashes. Avoid "not X but Y" constructions. Sentence-case headings. Vary sentence length. End on a fact or a next step, not a summary. Output reads as if a polished professional assembled it.

Banned vocabulary: leverage, utilize, robust, seamless, streamline, empower, foster, paradigm, landscape, journey, pivotal, cutting-edge, holistic, demonstrate, facilitate, ensure, endeavor, game-changer, state-of-the-art.

Banned transitions: Moreover, Furthermore, Additionally, Notably, Importantly, It is worth noting that.

Honor these in every non-code string: skill bodies, domain-gap notes, comments, prompt text, setup instructions. Code is exempt.
