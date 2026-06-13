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

## Build methodology: thin vertical slice first
Prove one asset all the way up before going wide. From the first five minutes, take a single skill through the whole stack: author the entry, run `/validate`, run `/build`, then open `dist/skills-library.html` and confirm it renders and presents well. A working slice of one beats a broad pack that has never compiled. Widen only after the slice holds, adding entries and rebuilding with a render check each pass. A change that spans the stack (schema, build, or template) rides through one entry end to end before it touches the rest. Full rationale in `memory/projects/skills-library.md`.

## Domain terminology
Break: a reconciliation discrepancy to research and resolve. Tie-out: reconcile a statement against an authoritative source. Cost basis: original asset value for tax gain and loss. Remediation path: UI, XML, SQL, or plugin. 1099-DIV/B/INT, 1042-S, FATCA, CRS: the reporting forms and regimes. Full definitions live in `memory/glossary.md`. Full break taxonomy, routing rules, and tax-form mappings live in the domain skill below.

## Where things live
- `content/entries/*.yaml` — one asset per file, 14 today across two packs. A Data Analytics pack covers metric-movement diagnostics, data-quality profiling, the break-backlog KPI readout, the dashboard brief, the report writer, and an end-to-end diagnostic workflow. A Gainskeeper operations pack covers exception research, gain/loss tie-out, email intake triage, field-status replies, KB review, the break tracker, and work-item routing. `gl-reconciler-break-triage.yaml` is the exemplar every entry matches for shape and depth. Schema in `SKILLS_LIBRARY_SPEC.md` section 4 (assets) and section 5 (workflows).
- `build/build.py` — validates content, renders each entry, runs the offline check, compiles the HTML. The build reads `content/entries/` and nothing else.
- `build/template.html` — the offline shell. Inlined CSS and JS, no external dependencies. The build injects entries at the `<!--ENTRIES-->` marker.
- `dist/skills-library.html` — generated output, gitignored. Do not hand-edit; the next build overwrites it.
- `tests/test_validate.py` — pytest contract tests, one per validation rule, with a regression case behind each past fix. Run `python -m pytest`.
- `requirements.txt` (pyyaml, markdown) and `requirements-dev.txt` (adds pytest) — the pinned dependencies.
- `.claude/skills/tax-ops-domain.md` — break taxonomy, routing rules, tax-form mappings, three-test framework. Load it when authoring or adapting an entry.
- `.claude/skills/build-pipeline.md` — the content-layer model, the build steps, the ten acceptance criteria.
- `.claude/commands/*.md` — the `/validate`, `/build`, and `/new-entry` slash commands.
- `.claude/agents/repo-review-orchestrator.md` — the multi-angle review agent. It keeps its own `memory: project` store under `.claude/`, owned by the agent and separate from the operator memory layer below.
- `SKILLS_LIBRARY_SPEC.md` — the contract. Section 8 is the quality bar, section 10 the acceptance criteria.
- `CHANGELOG.md` — what changed, newest first. `TASKS.md` — active work, waiting-on items, someday, and done.
- `memory/` — operator context, the cold store this file defers to. `memory/README.md` defines the layer and its boundary with the build. `memory/glossary.md` holds full term definitions, `memory/company.md` the environment, `memory/projects/skills-library.md` this repo's dossier. None of it compiles into `dist/`.

## Build commands
The slash commands wrap the script. The script is the source of truth, so either form works.
- `/validate` or `python build/build.py --check` — check every entry against the schema and the hard rules. No build. A non-zero exit names the file, the field, and the rule.
- `/build` or `python build/build.py` — validate, compile, run the offline check, write `dist/skills-library.html`. A failed offline check aborts before any file is written.
- `/new-entry <slug> "<name>"` — scaffold a content entry with every schema field pre-filled.
- `python -m pytest` — run the validator contract tests. Install deps first with `pip install -r requirements-dev.txt`.

## Keep the productivity suite current
Whenever you change code, a document, or the environment, move the bookkeeping in the same pass, before push: TASKS.md shows what is now active, waiting, or done, and CHANGELOG.md gets a line under `[Unreleased]`. The same trigger drives both files; a doc-only or environment-only change still earns a changelog line. This is the interim rule while a better mechanism is chosen against the wshobson/agents patterns; it is guidance the assistant follows, not an enforced hook.

## Adding or changing an entry
1. Scaffold with `/new-entry`, or copy the exemplar.
2. Write a tool-agnostic body. Put firm specifics in bracketed `[INSERT: …]` placeholders and pull the real content from `.claude/skills/tax-ops-domain.md`. Open inserts are the intended terminal form for `adapt` and `author-from-spec` entries, not an unfinished state.
3. Write a substantive `domain_gap` to the section 8 standard: name what the analyst supplies and what changes once it is filled. A one-line gap fails.
4. Run `/validate`, clear every failure, then `/build`.
5. Match the exemplar. An entry that cannot pass the three tests visibly is not ready.

## What validation enforces
- Every required field is present for the entry type. Assets carry the section 4 fields, workflows the section 5 fields.
- `id` is a stable slug that matches the filename stem and is unique across the library.
- `tier` is an integer 1 to 4. `stage`, `type`, and `adaptation` hold allowed values only.
- `core_function` names no tool. A match on sql, xml, plugin, database, connector, runtime, sdk, mcp, api, rest, graphql, endpoint, or cron fails the entry, since the core has not been decomposed.
- `domain_gap` is present and substantive for every asset.
- A workflow carries at least one explicit human-sign-off gate, and any workflow with a remediation step must gate it.
- The compiled HTML loads nothing external and uses no browser storage. The offline scan catches external `src` and `href`, `<link>`, external `<script src>`, `@import`, remote `url()`, and any `localStorage`, `sessionStorage`, `indexedDB`, or cookie use in the page chrome.

## Writing preferences
BLUF. Specific over general, decisive. No em dashes. Avoid "not X but Y" constructions. Sentence-case headings. Vary sentence length. End on a fact or a next step, not a summary. Output reads as if a polished professional assembled it.

Banned vocabulary: leverage, utilize, robust, seamless, streamline, empower, foster, paradigm, landscape, journey, pivotal, cutting-edge, holistic, demonstrate, facilitate, ensure, endeavor, game-changer, state-of-the-art.

Banned transitions: Moreover, Furthermore, Additionally, Notably, Importantly, It is worth noting that.

Banned constructions: the single-caveat reveal, where one item gets teed up as specially significant. No "one X remains, and it's the Y", no "one X, and it's the Y", no "this one's load-bearing", no "the load-bearing X". Drop the faux-candor framing ("one honest thing", "to be honest, the real issue is"). State the point plainly without the buildup. The word "load-bearing" as a descriptor is banned.

Honor these in every non-code string: skill bodies, domain-gap notes, comments, prompt text, setup instructions. Code is exempt.
