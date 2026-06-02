# Tasks

## Active

- [ ] **Get the Skills Library spec reviewed by the evaluator agent** - hand off `SKILLS_LIBRARY_SPEC.md`; incorporate feedback before build
- [ ] **Build the Skills Library artifact** - in a dedicated build chat within this project; self-contained offline HTML, one entry per skill/prompt/agent/workflow in expandable blocks with copy buttons
- [ ] **Decide the v1 starting subset with the group** - which assets to author first; pick the highest-fit slice rather than all 40+
- [ ] **Run the first chosen asset through the three tests** - understand / decompose / adapt; produce a worked template the rest follow

## Waiting On

- [ ] **Group input on which skill to pilot first** - since since 05-31-2026
- [ ] **Evaluator agent feedback on the spec** - since 05-31-2026

## Review follow-ups (from 05-31-2026 repo review, design calls)

- [ ] **Decide workflow stage handling** - a stage-less workflow renders `data-stage="workflow"`, which no filter button selects. Give workflows a real stage or add a "workflow" filter control
- [ ] **Resolve the research-inventory criterion** - spec criterion 8 ties `tier` to an inventory that is not a checked-in file. Commit the inventory or drop the criterion
- [ ] **Decide the exemplar's terminal form** - ship a fully-assembled sibling entry with `[INSERT: …]` gaps filled, or document open brackets as the intended end state

## Someday

- [ ] **Add tool-specific execution notes per asset** - GS internal assistant, Copilot, then Claude when provisioned
- [ ] **Re-target the content layer when Claude access lands** - upgrade execution layer without rewriting content
- [ ] **Author the full set of skill/prompt/agent bodies** - beyond the v1 subset, work through remaining inventory entries

## Done

- [x] ~~Formalize the memory layer~~ (06-02-2026) — documented the layer and its boundary with the build in `memory/README.md`, wired CLAUDE.md and the build-pipeline skill to it, and fixed the absolute-path and duplicate-scheme seams in the repo-review agent's memory section
- [x] ~~Run deep research and build the credibility-tier-ranked inventory~~ (05-31-2026)
- [x] ~~Establish the core value-generation principle (specs not software; three tests)~~ (05-31-2026)
- [x] ~~Decide to split build and strategy into separate chats for context optimization~~ (05-31-2026)
- [x] ~~Multi-agent repo review with evaluator checkpoint; fix the verified findings~~ (05-31-2026)
