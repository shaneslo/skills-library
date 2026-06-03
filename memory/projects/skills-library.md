# Project: Skills Library

## What
A curated, credibility-tier-ranked, copy-and-adapt repository of AI assets (prompts, skills, agents, workflows) for the GS prime brokerage tax-ops role. Tool-agnostic content compiles to one offline HTML file. The execution layer can change without rewriting content.

## Why
Decouple AI capability from tool procurement. Capture working patterns as tool-agnostic content now, and upgrade the execution layer (GS assistant, Copilot, Claude) over time without rewriting content.

## Status (current)
Built. The project is now a Claude Code repo. The single hand-authored HTML file is gone; the repo compiles the output instead. v1 ships the scaffold, the build pipeline, one fully worked exemplar entry, a Data Analytics seed pack, and a wider operations pack for Gainskeeper exception research, gain and loss tie-outs, email intake, status replies, KB review, tracker maintenance, and work-item routing. The pipeline runs clean end to end: validate passes, tests pass, build compiles, and the offline check finds no external references.

The frontend redesign shipped in PR #9 (merged 2026-06-03): a light square-card library grouped by stage, a Type filter, native `<dialog>` detail views, an offline scan widened to catch browser-storage APIs and scoped away from entry prose, and a stage-count summary. The 14-entry pack is in place. Reviewed against the issue #8 plan with validate, 20 tests, build, and offline check all clean. The next frontend step is the Track B workflow map; see Open items. The build plan and its review live in issue #8.

## Repo
The repo root, initialized from `gs_projectfiles`. Shape:
- `content/entries/*.yaml`: one asset per file, the value layer.
- `build/build.py`: validates content and compiles the HTML.
- `build/template.html`: the offline shell, no external dependencies.
- `dist/skills-library.html`: generated output, gitignored.
- `.claude/skills/tax-ops-domain.md`: break taxonomy, remediation routing, tax-form mappings, three-test framework.
- `.claude/skills/build-pipeline.md`: how to validate and build.
- `.claude/commands/`: `/validate`, `/build`, `/new-entry`.
- `CLAUDE.md`: repo guidance and hot-cache memory.
- `SKILLS_LIBRARY_SPEC.md`: the contract. Section 8 is the quality bar.

## How it works
Three layers: content (YAML), template (HTML, written once), build (a Python loop that injects content into the template). Output tokens go to asset bodies; the script generates the repetitive markup. Edit one small YAML file and re-run. The template is never re-emitted by hand.

## What the build enforces
Four hard rules, all script-checked: every required schema field present per type; `core_function` names no tool; `domain_gap` present and substantive for every finance asset; any workflow with a remediation step carries a human-sign-off gate. An offline check aborts the build if the output references anything external, and a browser-storage scan (localStorage, sessionStorage, indexedDB, document.cookie) runs over the executable chrome only, so prompt prose that names those tokens does not trip it. Navigation is by workflow stage (intake-classify, research, remediate, communicate), with a Type filter that isolates prompts, skills, agents, and workflows. Workflows keep their starting stage, and `stage` is now required for every type, which resolved issue #2. Tier 1 to 4 is a tag and a filter, not the grouping axis.

## Open items
- Prototype the Track B workflow map (issue #8): inline SVG or a small inline script drawn from the workflow YAML for v2, starting with `tax-break-diagnostic-workflow`; React Flow deferred to v3 behind the offline and storage scan over every emitted file. Add `docs/react-flow-pro-license-note.md` before any Pro-informed code.
- Frontend polish from the #9 review: cards use `min-height` rather than `aspect-ratio: 1/1` and the grid packs more than three columns at 1280px; the `<dialog>` has no `aria-labelledby` to the title and the copy status is not in an `aria-live` region; the validator does not constrain a workflow `stage` to the four stages, so a typo would render it in no group.
- Review the 14-entry pack for desk fit. Confirm whether the asset names, fields, and issue types match the real Gainskeeper operating cadence.
- Decide whether bracketed inserts remain reusable or terminal-form siblings should embed the taxonomy, routing rules, and form mappings directly.
- Reconstruct or commit the missing research inventory if tier tags need audit support beyond the source notes in each entry.
- Tax figures in `tax-ops-domain.md` (24% backup withholding, 30% NRA default, 1099-DIV box numbers, 1042-S income codes 06/01/51) are as of training. Confirm against current-year IRS instructions each filing season.
- GL Reconciler maturity stats (roughly 29k stars, 4.1k forks, 2026-05-05 release) came from the research pass and were not re-verified. Spot-check before the library goes wider than you.

## Source material
Research report artifact: credibility-tier-ranked inventory across four tiers (Anthropic financial-services repo, Microsoft 365 Copilot Finance, Atlassian Rovo, ServiceNow, wshobson/agents, OpenAI Academy, Nate B. Jones). Inventory holds names, one-liners, sources, fit notes. Most full runnable bodies must be authored, not copied.

The checked-in project currently references that inventory only in this dossier. The itemized inventory file was not found in the repo during the 2026-06-03 initialization pass.

## Versioning roadmap
- v1: tool-agnostic content. Runs on whatever assistant is in hand, including the GS internal assistant and Copilot.
- v2: add per-asset execution notes per tool as access is confirmed.
- v3: when Claude or an internal Goldman tool lands, add execution notes and link runnable skills alongside the prompt bodies. The content layer carries forward unchanged.
