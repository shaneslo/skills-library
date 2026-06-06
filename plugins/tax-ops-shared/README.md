# tax-ops-shared

Shared knowledge and authoring tooling the other two plugins depend on. The domain skill is the single source for break taxonomy, routing rules, and tax-form mappings. The commands validate, build, and scaffold library content.

## What it holds

One skill and three commands.

Skill:
- `tax-ops-domain` — break taxonomy, routing rules, tax-form mappings, and the three-test framework. Load it when authoring or adapting any entry.

Commands:
- `validate` — check every entry against the schema and the hard rules. No build.
- `build` — validate, compile the offline HTML, run the offline check, write the catalog.
- `new-entry` — scaffold a content entry with every schema field pre-filled.

## How the bodies read

The domain skill body is tool-agnostic prose with bracketed `[INSERT: ...]` placeholders for firm specifics. The commands wrap `build/build.py`, which stays the source of truth for validation and the offline build.
