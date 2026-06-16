# Project: Skills Library

## What
A curated, credibility-tier-ranked, copy-and-adapt repository of AI assets (prompts, skills, agents, workflows) for the GS prime brokerage tax-ops role. Tool-agnostic content compiles to one offline HTML file. The execution layer can change without rewriting content.

## Why
Decouple AI capability from tool procurement. Capture working patterns as tool-agnostic content now, and upgrade the execution layer (GS assistant, Copilot, Claude) over time without rewriting content.

## Status (current)
Built. The project is now a Claude Code repo. The single hand-authored HTML file is gone; the repo compiles the output instead. v1 ships the scaffold, the build pipeline, one fully worked exemplar entry, a Data Analytics seed pack, and a wider operations pack for Gainskeeper exception research, gain and loss tie-outs, email intake, status replies, KB review, tracker maintenance, and work-item routing. The pipeline runs clean end to end: validate passes, tests pass, build compiles, and the offline check finds no external references.

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

## Build methodology: vertical slice first
The working unit is a thin vertical slice, not a wide layer. Build one skill all the way up before adding a second: author the YAML entry, run `/validate`, run `/build`, then open `dist/skills-library.html` and confirm the entry renders correctly and presents well. Only once that slice is clean do we widen the library, adding entries and rebuilding with a render check each pass. The same rule governs cross-cutting work: a schema, build, or template change rides through one entry end to end before it touches the rest. Why this order holds: a broad pack that has never compiled hides its failures until late, and a render that reads wrong is cheapest to catch on a single card. The payoff is a repo that is demonstrably working at every step, presentable to the group from minute one. The 14 entries already shipped were authored before this rule; it governs the next pack, the frontend v2 map, and any schema change from here.

## What the build enforces
Four hard rules, all script-checked: every required schema field present per type; `core_function` names no tool; `domain_gap` present and substantive for every finance asset; any workflow with a remediation step carries a human-sign-off gate. An offline check aborts the build if the output references anything external. Navigation is by workflow stage (intake-classify, research, remediate, communicate). Tier 1 to 4 is a tag and a filter, not the grouping axis.

## Open items
- Review the 14-entry pack for desk fit. Confirm whether the asset names, fields, and issue types match the real Gainskeeper operating cadence.
- Decide whether bracketed inserts remain reusable or terminal-form siblings should embed the routing rules and form mappings directly. The GL Reconciler exemplar now embeds the first real cause-taxonomy insert, based on the tax-agent correction-loop research note and the shared tax-ops domain skill.
- Reconstruct or commit the missing research inventory if tier tags need audit support beyond the source notes in each entry.
- Tax figures in `tax-ops-domain.md` (24% backup withholding, 30% NRA default, 1099-DIV box numbers, 1042-S income codes 06/01/51) are as of training. Confirm against current-year IRS instructions each filing season.
- GL Reconciler maturity stats (roughly 29k stars, 4.1k forks, 2026-05-05 release) came from the research pass and were not re-verified. Spot-check before the library goes wider than you.

## Source material
Research report artifact: credibility-tier-ranked inventory across four tiers (Anthropic financial-services repo, Microsoft 365 Copilot Finance, Atlassian Rovo, ServiceNow, wshobson/agents, OpenAI Academy, Nate B. Jones). Inventory holds names, one-liners, sources, fit notes. Most full runnable bodies must be authored, not copied.

The checked-in project currently references that inventory only in this dossier. The itemized inventory file was not found in the repo during the 2026-06-03 initialization pass.

`content/harvest/writing-skills/` holds three generic writing source packs: `content-strategy`, `copywriting`, and `deep-write`. Treat them as candidate source material for SLO-76 or a later source-family pass. They should become entries or plugin assets only after a tax-ops use case passes the three-test framework.

## Versioning roadmap
- v1: tool-agnostic content. Runs on whatever assistant is in hand, including the GS internal assistant and Copilot.
- v2: add per-asset execution notes per tool as access is confirmed.
- v3: when Claude or an internal Goldman tool lands, add execution notes and link runnable skills alongside the prompt bodies. The content layer carries forward unchanged.
