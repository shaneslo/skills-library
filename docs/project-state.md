# Project state, 2026-06-14

A snapshot of what the repo actually contains against what the standing docs claim. Captured to surface drift before the next pack or the build re-point lands. The build is green at capture time: `validate` passes on 20 entries, `build` compiles `dist/skills-library.html`, offline check clean.

## Headline

Two facts moved and the prose did not follow. The content layer grew from 14 to 20 entries, and the repo gained a Claude Code plugin marketplace beside the YAML layer. CLAUDE.md and the project dossier still describe the 14-entry, single-source repo.

## Entry count drift

CLAUDE.md "Where things live" says `content/entries/*.yaml` holds "14 today across two packs." The directory holds 20 YAML files. Six landed since that line was written:

- `build-pipeline-knowledge` (skill, tier 1)
- `claude-build-command` (skill, tier 1)
- `claude-validate-command` (skill, tier 1)
- `claude-new-entry-command` (skill, tier 1)
- `tax-ops-domain-knowledge` (skill, tier 1)
- `period-close-reconciliation-workflow` (workflow, tier 1)

CLAUDE.md is also internally inconsistent: it says "14" then enumerates the two packs as six Data Analytics entries plus seven Gainskeeper entries, which is 13. `memory/projects/skills-library.md` repeats "14 entries" and "14-entry pack" three times.

## Two source layouts coexist

The docs split on what the repo is.

- CLAUDE.md and `memory/projects/skills-library.md` describe one source: `content/entries/*.yaml` compiled by `build/build.py`.
- README.md, `docs/architecture.md`, `docs/north-star.md`, and `docs/authoring-plugins.md` describe a Claude Code plugin marketplace: `.claude-plugin/marketplace.json` plus `plugins/{gainskeeper-operations, tax-data-analytics, tax-ops-shared}`.

Both are present. The build still reads `content/entries/` only; `docs/architecture.md` states the re-point to `plugins/**` is a pending follow-up and the two layouts coexist until it lands. So the marketplace is real scaffolding, not yet the build input.

## New top-level directories CLAUDE.md does not list

CLAUDE.md "Where things live" predates four directories now in the tree:

- `docs/` — `architecture.md`, `north-star.md`, `authoring-plugins.md`
- `plugins/` — the three-plugin marketplace
- `.claude-plugin/` — `marketplace.json` registry
- `mocks/` — `skills-library-linear.html`, the Linear-style interface mock (CHANGELOG records it; CLAUDE.md does not)

## Plugin tree does not mirror all 20 entries

The marketplace carries 18 of the 20 entries as native assets:

- `gainskeeper-operations`: 7 skills plus 1 agent (`gainskeeper-exception-research-agent`)
- `tax-data-analytics`: 5 skills plus 1 command (`tax-break-diagnostic-workflow`)
- `tax-ops-shared`: the `tax-ops-domain` skill plus `build`, `validate`, `new-entry` commands

Two content entries have no plugin counterpart:

- `period-close-reconciliation-workflow` — a `type: workflow` entry with no home in any plugin
- `build-pipeline-knowledge` — a catalog skill not represented in the marketplace

The `build`/`validate`/`new-entry` commands appear in `tax-ops-shared/commands/` and as separate `claude-*-command` catalog entries under `content/entries/`, so the same three commands exist in both layouts under different names.

## Helper-command classification contradicts the authoring doc

`docs/authoring-plugins.md` says: "A native helper command such as `/validate` or `/build` is tooling, not a catalog asset, so it carries no library `type`." Yet `content/entries/` carries `claude-build-command`, `claude-validate-command`, and `claude-new-entry-command` as `type: skill`, tier 1, stage `communicate` catalog entries. The same `/build` and `/validate` are catalog assets in the YAML layer and explicitly not catalog assets in the marketplace doc.

## Marketplace naming

`marketplace.json` sets `name: tax-ops-skills-library` and `owner.name: skills-library`, while README install instructions reference `shaneslo/skills-library`. Worth a glance before publishing the marketplace, since the registry name and the repo slug differ.

## Dossier staleness

`memory/projects/skills-library.md` "Status (current)" and "Repo" sections predate the marketplace. They list `content/entries/*.yaml` as the only source, cite 14 entries, and name no `plugins/`, `docs/`, or `mocks/` directory. The dossier is the cold store CLAUDE.md defers to, so it should track the same reality.

## Recommended follow-ups

Capture only; nothing below is changed in this pass.

1. Update CLAUDE.md "Where things live" to 20 entries and add `docs/`, `plugins/`, `.claude-plugin/`, `mocks/`. Fix the 14-versus-13 count.
2. Refresh `memory/projects/skills-library.md` to the marketplace reality and the current entry count.
3. Decide the home for `period-close-reconciliation-workflow` and `build-pipeline-knowledge` in the plugin tree, or document why they stay YAML-only.
4. Resolve the helper-command classification: either retire the `claude-*-command` catalog entries or amend the authoring doc.
5. Reconcile the marketplace `name` with the repo slug before publishing.
