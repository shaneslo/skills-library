# Authoring plugins

How to add a skill, an agent, or a command to a plugin.

## Pick the shape

- Skill: a focused job a model does well in one pass. Most assets are skills.
- Agent: drives a multi-step task to a documented disposition.
- Command: the operator entry point that orchestrates skills and agents and names the sign-off gates. The most valued shape.

## Pick the path

Drop the file under the right plugin and the directory its kind belongs to.

```
plugins/<plugin>/skills/<id>/SKILL.md
plugins/<plugin>/agents/<id>.md
plugins/<plugin>/commands/<id>.md
```

The file stem (or skill directory name) is the asset `id`. Keep it a stable slug, unique across the library.

## Native frontmatter

Every asset carries the two fields Claude Code reads natively:

```yaml
---
name: <human-readable name>
description: <one line on when to reach for this asset>
---
```

The body follows the frontmatter. Write it tool-agnostic, BLUF, with firm specifics in bracketed `[INSERT: ...]` placeholders. Open placeholders are the intended terminal form for adapted and author-from-spec assets, not an unfinished state. The body must work pasted into an API call with no host capability assumed.

## Extended library metadata

Add the library metadata as extra frontmatter keys on the same file. Claude Code ignores them; the offline build reads them.

```yaml
type: skill | agent | workflow
stage: <where it sits in the workflow spine>
tier: 1 | 2 | 3 | 4
adaptation: use-as-is | adapt | author-from-spec
source: <repo or origin, with license>
core_function: <the one job, naming no tool>
domain_fit: <which priority it serves and how directly>
domain_gap: <what the analyst supplies and what changes once filled>
maturity: <provenance and readiness of the source>
notes: <anything a future author needs>
```

A command that orchestrates an end-to-end workflow carries `type: workflow`. A native helper command such as `/validate` or `/build` is tooling, not a catalog asset, so it carries no library `type`.

Two keys carry the weight of review.

- `core_function` must name no tool. A match on sql, xml, plugin, database, connector, runtime, sdk, mcp, api, rest, graphql, endpoint, or cron means the core has not been decomposed.
- `domain_gap` must be substantive. Name what the analyst supplies and what changes once it is filled. A one-line gap fails the quality bar.

## Before you ship

Run `validate` to check every entry against the schema and the hard rules. Then `build` to compile the offline catalog and confirm it loads nothing external. Match the exemplar `gl-reconciler-break-triage` for shape and depth. An asset that cannot pass the three tests visibly is not ready.
