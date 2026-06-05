# Tasks

## Active

- [ ] **Reconcile assistant session logs for missing skills** - review Codex CLI, Claude Code, and clod.ai sessions that discussed new assets; for each, ensure there is either a `content/entries/*.yaml` entry or a tracking issue with the intended entry id
- [ ] **Get the Skills Library spec reviewed by the evaluator agent** - hand off `SKILLS_LIBRARY_SPEC.md`; incorporate feedback before build
- [ ] **Review the Data Analytics v1 pack for desk fit** - confirm which metrics, break cuts, and status-note shapes match the real operating cadence
- [ ] **Review the Gainskeeper operations pack for desk fit** - confirm exception fields, gain/loss tie-out shape, email buckets, tracker statuses, and work-item priority rules
- [ ] **Decide the next source family to harvest** - likely GitHub agent patterns, financial-services examples, or document-review workflows

## Waiting On

- [ ] **Group input on which skill to pilot first after the Data Analytics seed** - since 06-03-2026
- [ ] **Evaluator agent feedback on the spec** - since 05-31-2026

## Review follow-ups (from 05-31-2026 repo review, design calls)

All three resolved 06-03-2026. See the "Decided" block in CHANGELOG.md.

## Someday

- [ ] **Add tool-specific execution notes per asset** - GS internal assistant, Copilot, then Claude when provisioned
- [ ] **Re-target the content layer when Claude access lands** - upgrade execution layer without rewriting content
- [ ] **Author the full set of skill/prompt/agent bodies** - beyond the v1 subset, work through remaining inventory entries

## Done

- [x] ~~Resolve the three 05-31 review design calls~~ (06-03-2026) - workflow stage handling (resolved on main by PR #9's Type-axis "Workflows" filter; `stage` is now required, removing the orphaned `data-stage` value), research-inventory criterion (tier now reads from source/maturity, no external file), exemplar terminal form (bracketed inserts are the intended end state, documented in the spec). Bracketed-insert fill task closed by that last call.
- [x] ~~Initialize Data Analytics v1 pack~~ (06-03-2026) - added six tax-ops-adapted entries from the Data Analytics plugin: metric diagnostics, data quality profiling, break backlog KPI readout, dashboard brief, report writer, and an end-to-end diagnostic workflow
- [x] ~~Initialize Gainskeeper operations pack~~ (06-03-2026) - added seven entries for exception research, gain/loss tie-out, email intake, field replies, KB review, break trackers, and work-item routing
- [x] ~~Build the first Skills Library artifact~~ (06-03-2026) - generated `dist/skills-library.html` from seven entries; validation passed and the offline check was clean
- [x] ~~Formalize the memory layer~~ (06-02-2026) - documented the layer and its boundary with the build in `memory/README.md`, wired CLAUDE.md and the build-pipeline skill to it, and fixed the absolute-path and duplicate-scheme seams in the repo-review agent's memory section
- [x] ~~Run deep research and build the credibility-tier-ranked inventory~~ (05-31-2026)
- [x] ~~Establish the core value-generation principle (specs not software; three tests)~~ (05-31-2026)
- [x] ~~Decide to split build and strategy into separate chats for context optimization~~ (05-31-2026)
- [x] ~~Multi-agent repo review with evaluator checkpoint; fix the verified findings~~ (05-31-2026)
