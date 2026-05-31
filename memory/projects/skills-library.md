# Project: Skills Library

## What
A curated, credibility-tier-ranked, copy-and-adapt repository of AI assets (prompts, skills, agents, workflows) for the GS prime brokerage tax-ops role. Tool-agnostic content compiles to one offline HTML file. The execution layer can change without rewriting content.

## Why
Decouple AI capability from tool procurement. Capture working patterns as tool-agnostic content now, and upgrade the execution layer (GS assistant, Copilot, Claude) over time without rewriting content.

## Status (current)
Built. The project is now a Claude Code repo. The single hand-authored HTML file is gone; the repo compiles the output instead. v1 ships the scaffold, the build pipeline, and one fully worked exemplar entry (gl-reconciler-break-triage). The pipeline runs clean end to end: validate passes, build compiles, the offline check finds no external references.

## Repo
Lives at `/Users/shaneslo/projects/skills-library/`, initialized from `gs_projectfiles`. Shape:
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
Four hard rules, all script-checked: every required schema field present per type; `core_function` names no tool; `domain_gap` present and substantive for every finance asset; any workflow with a remediation step carries a human-sign-off gate. An offline check aborts the build if the output references anything external. Navigation is by workflow stage (intake-classify, research, remediate, communicate). Tier 1 to 4 is a tag and a filter, not the grouping axis.

## Open items
- Run the init script. Confirm `python build/build.py --check` returns `PASS. 1 entries`, then build and open `dist/skills-library.html` offline.
- Second entry is the real test of the section 8 bar. Pick one from the inventory, run `/new-entry`, and see whether the bar holds when the exemplar was not written to fit it.
- Tax figures in `tax-ops-domain.md` (24% backup withholding, 30% NRA default, 1099-DIV box numbers, 1042-S income codes 06/01/51) are as of training. Confirm against current-year IRS instructions each filing season.
- GL Reconciler maturity stats (roughly 29k stars, 4.1k forks, 2026-05-05 release) came from the research pass and were not re-verified. Spot-check before the library goes wider than you.

## Source material
Research report artifact: credibility-tier-ranked inventory across four tiers (Anthropic financial-services repo, Microsoft 365 Copilot Finance, Atlassian Rovo, ServiceNow, wshobson/agents, OpenAI Academy, Nate B. Jones). Inventory holds names, one-liners, sources, fit notes. Most full runnable bodies must be authored, not copied.

## Versioning roadmap
- v1: tool-agnostic content. Runs on whatever assistant is in hand, including the GS internal assistant and Copilot.
- v2: add per-asset execution notes per tool as access is confirmed.
- v3: when Claude or an internal Goldman tool lands, add execution notes and link runnable skills alongside the prompt bodies. The content layer carries forward unchanged.
