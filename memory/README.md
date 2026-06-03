# Memory

This directory is the operator's persistent context for the tax-ops AI work. It feeds the assistant, not the compiled HTML. The Skills Library product is `content/`, `build/`, and `SKILLS_LIBRARY_SPEC.md`; this layer sits beside it and answers a different question: not what the library ships, but what the assistant should already know before it starts.

## The boundary with the build

`build/build.py` reads only `content/entries/`. It never reads `memory/`, so nothing here reaches `dist/skills-library.html`. The two layers are version-controlled differently on purpose: `memory/` is tracked, `dist/` is gitignored. Tracked context that never compiles is the signal that this layer is deliberate operator memory, not stray content that lost its way to the build.

If you are looking for what the user can copy and paste into an assistant, that is `content/`. If you are looking for the background the assistant carries into every task, that is here.

## The context model

Two surfaces hold the operator's curated context.

- **CLAUDE.md, the hot cache.** Always loaded. Short forms only: the workflow spine, domain weighting, the core principle, terse term definitions. It defers the full definitions to this directory, for example "Full definitions live in `memory/glossary.md`."
- **`memory/`, the cold store.** Loaded when a task needs it. Full glossary definitions, company and environment context, one dossier per project. CLAUDE.md points here; this is where the detail lives.

The split keeps the always-loaded file small while the full record stays one hop away.

## File roles

- `company.md` - the team, the tools in hand, the constraints, and relevant external developments such as the GS/Anthropic partnership. The environment the work runs in.
- `glossary.md` - the authoritative term definitions. CLAUDE.md carries the short forms and defers here for the full ones. Edit a definition here, not in CLAUDE.md.
- `projects/<slug>.md` - one dossier per project: what it is, why, current status, repo shape, open items, roadmap. `projects/skills-library.md` is this repo's own dossier.

## The projects/ convention

`projects/` is the operator's workspace memory and may hold a dossier for each project the operator runs, not only this one. Today it holds a single file, `skills-library.md`, because this is the project in front of us. The plural directory is the convention, the lone file is the current state. A second project earns a second dossier here, with no change to this repo's build.

## Agent memory is separate

`.claude/agent-memory/` is not part of this layer. It is agent-owned, self-maintained, durable memory that a specific agent writes for itself across conversations. The repo-review-orchestrator agent uses it, provisioned by the `memory: project` declaration in that agent's frontmatter and created on first write. It lives under `.claude/` because it belongs to the agent, not to the operator. Related to this layer, governed by a different owner and lifecycle.
