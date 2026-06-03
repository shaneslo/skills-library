# Tasks

## Active

- [ ] **Get the Skills Library spec reviewed by the evaluator agent** - hand off `SKILLS_LIBRARY_SPEC.md`; incorporate feedback before build
- [ ] **Review the Data Analytics v1 pack for desk fit** - confirm which metrics, break cuts, and status-note shapes match the real operating cadence
- [ ] **Review the Gainskeeper operations pack for desk fit** - confirm exception fields, gain/loss tie-out shape, email buckets, tracker statuses, and work-item priority rules
- [ ] **Fill bracketed domain inserts into terminal-form variants** - decide whether v1 keeps reusable inserts or ships assembled sibling entries with taxonomy, routing, and form mappings embedded
- [ ] **Decide the next source family to harvest** - likely GitHub agent patterns, financial-services examples, or document-review workflows

## Waiting On

- [ ] **codex to fold the five review edits into the issue #8 build plan** - since 06-03-2026; then build Track A
- [ ] **Group input on which skill to pilot first after the Data Analytics seed** - since 06-03-2026
- [ ] **Evaluator agent feedback on the spec** - since 05-31-2026

## Review follow-ups (from 05-31-2026 repo review, design calls)

- [ ] **Decide workflow stage handling** - a stage-less workflow renders `data-stage="workflow"`, which no filter button selects. Give workflows a real stage or add a "workflow" filter control. Slated for resolution through the issue #8 plan: workflows keep their starting stage and a type filter is added; close #2 against that plan
- [ ] **Resolve the research-inventory criterion** - spec criterion 8 ties `tier` to an inventory that is not a checked-in file. Commit the inventory or drop the criterion
- [ ] **Decide the exemplar's terminal form** - ship a fully-assembled sibling entry with `[INSERT: …]` gaps filled, or document open brackets as the intended end state

## Someday

- [ ] **Add tool-specific execution notes per asset** - GS internal assistant, Copilot, then Claude when provisioned
- [ ] **Re-target the content layer when Claude access lands** - upgrade execution layer without rewriting content
- [ ] **Author the full set of skill/prompt/agent bodies** - beyond the v1 subset, work through remaining inventory entries

## Done

- [x] ~~Review the v2 frontend build plan (issue #8)~~ (06-03-2026) - checked the plan against the live repo and posted a review; handed five edits to codex through the issue: scope the offline and storage scanner away from entry prose, emit a `data-type` attribute for the workflow type filter, resolve issue #2's stage handling, use a native `<dialog>` drawer, and add a stage-count summary token; promoted Track B path 1 (inline map, no Node) to the v2 decision with React Flow held to v3
- [x] ~~Initialize Data Analytics v1 pack~~ (06-03-2026) - added six tax-ops-adapted entries from the Data Analytics plugin: metric diagnostics, data quality profiling, break backlog KPI readout, dashboard brief, report writer, and an end-to-end diagnostic workflow
- [x] ~~Initialize Gainskeeper operations pack~~ (06-03-2026) - added seven entries for exception research, gain/loss tie-out, email intake, field replies, KB review, break trackers, and work-item routing
- [x] ~~Build the first Skills Library artifact~~ (06-03-2026) - generated `dist/skills-library.html` from seven entries; validation passed and the offline check was clean
- [x] ~~Formalize the memory layer~~ (06-02-2026) - documented the layer and its boundary with the build in `memory/README.md`, wired CLAUDE.md and the build-pipeline skill to it, and fixed the absolute-path and duplicate-scheme seams in the repo-review agent's memory section
- [x] ~~Run deep research and build the credibility-tier-ranked inventory~~ (05-31-2026)
- [x] ~~Establish the core value-generation principle (specs not software; three tests)~~ (05-31-2026)
- [x] ~~Decide to split build and strategy into separate chats for context optimization~~ (05-31-2026)
- [x] ~~Multi-agent repo review with evaluator checkpoint; fix the verified findings~~ (05-31-2026)
