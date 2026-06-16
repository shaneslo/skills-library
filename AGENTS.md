# AGENTS.md

Guidance for Codex (and any non-Claude agent) in this repo. The project files are the source of truth. Read them before acting.

## Dual-agent repo
Two agents work here, and the split is deliberate. It is not a migration in progress.
- Codex harvests and adapts content. Most `content/entries/*.yaml` were decomposed from first-party OpenAI plugin skills and re-expressed as tool-agnostic prose.
- Claude Code owns the build pipeline, scaffolding, tests, and frontend.

Both share the same domain skills under `.claude/skills/` and the same `memory/` cold store. Neither tool is the sole agent. Do not strip the other's work.

`CLAUDE.md` is the canonical, fuller contract. Read it. Everything in it applies to Codex too. This file covers only the Codex-specific deltas.

## What this repo is
A copy-and-adapt library of AI assets (prompts, skills, agents, workflows) for Goldman Sachs prime brokerage tax-reporting operations. Content is tool-agnostic and compiles to one offline HTML file. The execution layer can change without rewriting content.

## Core principle
The question is never which tools we have, but what exists that works. Three tests for any asset: understand it, decompose it to its core function and rebuild it, adapt it to the domain now. Treat credible repos as specifications, not software: harvest the decomposition, drop code that will not run, re-express the rest as prompts the available assistant runs. The edge is the domain knowledge poured into the gap the repo cannot fill.

## Where Codex things live
- `.claude/skills/tax-ops-domain.md` — break taxonomy, routing rules, tax-form mappings, the three-test framework. Shared, not Claude-only. Load it when authoring or adapting an entry. (This pointer previously read `.Codex/skills/`, a path that never existed; the skills live under `.claude/skills/`.)
- `.claude/skills/build-pipeline.md` — the content-layer model, the build steps, the acceptance criteria.
- `.codex/` — Codex local scaffolding (agent and environment). Gitignored, not part of the build. `.codex/agents/repo-review-orchestrator.toml` mirrors `.claude/agents/repo-review-orchestrator.md`; keep the two in step if you change one.

## Build commands
Same as in `CLAUDE.md`. The script is the source of truth.
- `python build/build.py --check` — validate every entry against the schema and the hard rules. No build.
- `python build/build.py` — validate, compile, run the offline check, write `dist/skills-library.html`.
- `python -m pytest` — run the validator contract tests. Install deps first with `pip install -r requirements-dev.txt`.

## Keep the bookkeeping current
Whenever you change code, a document, or the environment, update `TASKS.md` and add a line to `CHANGELOG.md` under `[Unreleased]` in the same pass, before push. A doc-only or environment-only change still earns a changelog line.

## Writing preferences
BLUF. Specific over general, decisive. No em dashes. Avoid "not X but Y" constructions. Sentence-case headings. Vary sentence length. End on a fact or a next step, not a summary.

Banned vocabulary: leverage, utilize, robust, seamless, streamline, empower, foster, paradigm, landscape, journey, pivotal, cutting-edge, holistic, demonstrate, facilitate, ensure, endeavor, game-changer, state-of-the-art.

Banned transitions: Moreover, Furthermore, Additionally, Notably, Importantly, It is worth noting that.

Banned constructions: the single-caveat reveal, where one item gets teed up as specially significant. No "one X remains, and it's the Y", no "this one's load-bearing", no "the load-bearing X". Drop the faux-candor framing. State the point plainly. The word "load-bearing" as a descriptor is banned.

Honor these in every non-code string: skill bodies, domain-gap notes, comments, prompt text, setup instructions. Code is exempt.
