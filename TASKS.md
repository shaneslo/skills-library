# Tasks

## Active

- [ ] **Get the Skills Library spec reviewed by the evaluator agent** - hand off `SKILLS_LIBRARY_SPEC.md`; incorporate feedback before build
- [ ] **Review the Data Analytics v1 pack for desk fit** - confirm which metrics, break cuts, and status-note shapes match the real operating cadence
- [ ] **Review the Gainskeeper operations pack for desk fit** - confirm exception fields, gain/loss tie-out shape, email buckets, tracker statuses, and work-item priority rules
- [ ] **Fill bracketed domain inserts into terminal-form variants** - decide whether v1 keeps reusable inserts or ships assembled sibling entries with taxonomy, routing, and form mappings embedded
- [ ] **Decide the next source family to harvest** - likely GitHub agent patterns, financial-services examples, or document-review workflows
- [ ] **Prototype the workflow map (Track B, issue #8)** - draw an inline SVG or small-script map from the workflow YAML for v2 using `tax-break-diagnostic-workflow`; hold React Flow for v3 behind the offline and browser-storage scan over every emitted file. Write `docs/react-flow-pro-license-note.md` before any Pro-informed code

## Waiting On

- [ ] **Group input on which skill to pilot first after the Data Analytics seed** - since 06-03-2026
- [ ] **Evaluator agent feedback on the spec** - since 05-31-2026

## Review follow-ups (from 05-31-2026 repo review, design calls)

- [ ] **Resolve the research-inventory criterion** - spec criterion 8 ties `tier` to an inventory that is not a checked-in file. Commit the inventory or drop the criterion
- [ ] **Decide the exemplar's terminal form** - ship a fully-assembled sibling entry with `[INSERT: …]` gaps filled, or document open brackets as the intended terminal state
- [ ] **Frontend polish from the #9 review** - cards use `min-height` not `aspect-ratio: 1/1` and the grid packs more than three columns at 1280px; the `<dialog>` has no `aria-labelledby` to the title and the copy "Copied" status is not in an `aria-live` region; the validator does not constrain a workflow's `stage` to the four stages, so a typo would render it in no group. Decide which to tighten

## Someday

- [ ] **Add tool-specific execution notes per asset** - GS internal assistant, Copilot, then Claude when provisioned
- [ ] **Re-target the content layer when Claude access lands** - upgrade execution layer without rewriting content
- [ ] **Author the full set of skill/prompt/agent bodies** - beyond the v1 subset, work through remaining inventory entries

## Done

- [x] ~~Review and merge the v2 frontend build (#9)~~ (06-03-2026) - light square-card UI, a Type filter, native `<dialog>` detail views, an offline scan widened with browser-storage patterns and scoped away from entry prose, and a stage-count summary. Reviewed against the #8 plan: validate clean on 14 entries, 20 tests pass, build and offline check clean. Merged to main
- [x] ~~Resolve workflow stage handling (issue #2)~~ (06-03-2026) - workflows keep their starting stage and are found through the new Type filter; `stage` is now required for every entry type and the synthetic "workflow" group is gone. Closed #2
- [x] ~~Review the v2 frontend build plan (issue #8)~~ (06-03-2026) - checked the plan against the live repo and handed five edits to codex: scanner scope, `data-type` attribute, issue #2 handling, native `<dialog>` drawer, stage-count token; promoted Track B path 1 (inline map, no Node) to the v2 decision with React Flow held to v3
- [x] ~~Initialize Data Analytics v1 pack~~ (06-03-2026) - added six tax-ops-adapted entries from the Data Analytics plugin: metric diagnostics, data quality profiling, break backlog KPI readout, dashboard brief, report writer, and an end-to-end diagnostic workflow
- [x] ~~Initialize Gainskeeper operations pack~~ (06-03-2026) - added seven entries for exception research, gain/loss tie-out, email intake, field replies, KB review, break trackers, and work-item routing
- [x] ~~Build the first Skills Library artifact~~ (06-03-2026) - generated `dist/skills-library.html` from seven entries; validation passed and the offline check was clean
- [x] ~~Formalize the memory layer~~ (06-02-2026) - documented the layer and its boundary with the build in `memory/README.md`, wired CLAUDE.md and the build-pipeline skill to it, and fixed the absolute-path and duplicate-scheme seams in the repo-review agent's memory section
- [x] ~~Run deep research and build the credibility-tier-ranked inventory~~ (05-31-2026)
- [x] ~~Establish the core value-generation principle (specs not software; three tests)~~ (05-31-2026)
- [x] ~~Decide to split build and strategy into separate chats for context optimization~~ (05-31-2026)
- [x] ~~Multi-agent repo review with evaluator checkpoint; fix the verified findings~~ (05-31-2026)
