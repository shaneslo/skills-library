# Architecture

How the marketplace is laid out and how it maps from the old content model.

## The layout

The repo is a Claude Code plugin marketplace. One registry at the root lists the plugins. Each plugin is a self-contained tree.

```
.claude-plugin/marketplace.json     registry: lists the three plugins
plugins/
  gainskeeper-operations/
    .claude-plugin/plugin.json       manifest
    agents/                          driving agents
    skills/                          focused skills
    README.md
  tax-data-analytics/
    .claude-plugin/plugin.json
    commands/                        driving commands
    skills/
    README.md
  tax-ops-shared/
    .claude-plugin/plugin.json
    skills/                          shared domain knowledge
    commands/                        authoring commands
    README.md
docs/                                north-star, architecture, authoring
```

`marketplace.json` carries a `plugins` array. Each entry names a plugin, points `source` at its directory, and gives a one-line description. The three plugins are `gainskeeper-operations`, `tax-data-analytics`, and `tax-ops-shared`.

Each `plugin.json` carries `name`, `version`, `description`, and `author`. Claude Code reads `agents/`, `commands/`, and `skills/` by convention. Unknown JSON and frontmatter keys are ignored, which is what lets each asset keep its rich library metadata.

## The three plugins

- `gainskeeper-operations` holds the exception-handling work: one agent and seven skills for research, tie-out, intake, routing, tracking, and field replies.
- `tax-data-analytics` holds the diagnostics and reporting work: one command and five skills, with the command driving the end-to-end break diagnostic.
- `tax-ops-shared` holds the shared `tax-ops-domain` skill and the `validate`, `build`, and `new-entry` authoring commands.

## The mapping from the old model

The library used to live as one YAML file per asset under `content/entries/*.yaml`. Each file carried both native fields (a name, a type, a body) and library metadata (tier, stage, source, core function, domain fit, domain gap, maturity).

In the plugin layout each entry becomes a native Claude Code asset: a skill, an agent, or a command. The native fields move into standard frontmatter (`name`, `description`) and the asset body. The library metadata moves into extended frontmatter keys on the same file. Claude Code ignores the extra keys; the offline build reads them. Nothing is lost in translation.

## The offline build

`build/build.py` still compiles the browsable offline HTML catalog. In a follow-up step it will be re-pointed to read `plugins/**` so the catalog reflects the plugin layout. Until that consolidation lands, `content/entries/` stays the live source the build reads, and the build stays green.

This batch is additive. It adds the marketplace scaffolding, the plugin manifests, the READMEs, and these docs. It changes nothing under `content/entries/`, `build/`, or `tests/`. The two source layouts coexist until the build re-point retires the old one.
