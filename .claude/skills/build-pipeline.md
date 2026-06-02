---
name: build-pipeline
description: How to validate content and build the offline Skills Library HTML. Load when running a build, debugging a validation failure, adding or editing a content entry, or checking the output against the spec's acceptance criteria. Covers the content-layer model, the build script, template injection, the offline check, and all ten acceptance criteria from SKILLS_LIBRARY_SPEC.md section 10.
---

# Build pipeline

Content and presentation are separate. Author the content as YAML, run one script, get one self-contained HTML file. The model spends its output budget on the asset bodies, and a loop in the script generates the repetitive markup for free. A one-line fix to a single asset means editing one small file and re-running. The template is never re-emitted by hand.

The build reads `content/entries/` and nothing else. `memory/` is operator context that feeds the assistant, never the output; see `memory/README.md` for the boundary. Do not point the build at it.

## The three layers

1. **Content.** `content/entries/*.yaml`, one asset per file. Each file carries the schema fields. The prompt body and the prose notes are the value; everything else is metadata.
2. **Template.** `build/template.html`, written once. Inlined CSS and JS, the expandable card, the copy button, the stage and tier filters, the search box. The build injects entries at the `<!--ENTRIES-->` marker.
3. **Build.** `build/build.py`, run on every change. It reads content, validates it, renders each entry, injects the markup into the template, runs the offline check, and writes `dist/skills-library.html`.

## Running it

```
pip install pyyaml markdown        # once
python build/build.py --check      # validate only, no output written
python build/build.py              # validate, then build dist/skills-library.html
```

`--check` exits non-zero on any validation failure and names the file, the field, and the rule. The full build validates again, and if validation passes it renders, runs the offline check, and writes the file. A failed offline check aborts the build before anything is written.

## What the script enforces

The script validates so the rules cannot drift between a reviewer's head and the output:

- Every required field is present per entry type. Assets need the section 4 fields; workflows need the section 5 fields.
- `id` matches the filename stem and is unique across the library.
- `tier` is an integer 1 to 4. `stage`, `type`, and `adaptation` use their allowed values.
- `core_function` names no tool. A match on sql, xml, plugin, database, connector, runtime, sdk, mcp, api, rest, graphql, endpoint, or cron fails the entry.
- `domain_gap` is present and substantive for every asset. A blank or near-blank note fails.
- A workflow with a remediation step carries at least one explicit sign-off gate. A workflow with no gate at all fails.
- The compiled HTML loads nothing external. The offline check scans for external `src` and `href`, `<link>`, external `<script src>`, `@import`, and `url()` to a remote resource.

## Acceptance criteria checklist

Spec section 10, as a runnable checklist. The script covers most; the rest are a quick manual read of the output.

1. **Every entry carries all required schema fields.** Script-enforced. `--check` lists any missing field by file.
2. **Every `core_function` is tool-agnostic.** Script-enforced by the tool-token scan.
3. **Every finance asset has a substantive `domain_gap`.** Script-enforced by presence and a minimum-length check. Read the note to confirm it names real domain knowledge, not filler.
4. **Every workflow with a remediation step has an explicit sign-off gate.** Script-enforced.
5. **The output runs offline from `file://`.** Script-enforced by the offline scan. Confirm by opening the file with the network off.
6. **Copy buttons yield clean plain text.** Manual. The copy source is the raw `body` held verbatim in a `<pre>`; the JS copies its `textContent` with no transform and no smart-quote substitution. Open the file, copy a prompt, paste into a plain editor, confirm it matches the YAML body byte for byte.
7. **Content and presentation are separable.** Structural. Editing an entry never touches the template or the script.
8. **Tier tags are present and match the inventory.** Manual. Each card shows its tier tag; confirm the value against the research inventory.
9. **Primary navigation is by workflow stage; tier is a tag.** Structural. The output groups by stage and offers a tier filter, not a tier grouping.
10. **At least one entry meets the section 8 depth, and the rest match its shape.** Manual. The `gl-reconciler-break-triage` entry is the anchor. Hold every new entry to it.

## Adding or editing an asset

1. Run `/new-entry <slug> "<name>"` to scaffold a file, or copy an existing entry.
2. Write the body. Keep it tool-agnostic. Put firm specifics in bracketed inserts and pull them from the tax-ops-domain skill.
3. Write the `domain_gap` to the section 8 standard: name exactly what the analyst supplies and what changes once it is filled.
4. Run `/validate`. Clear every failure.
5. Run `/build`. Confirm the offline check is clean and note the output path.

If validation fails, the message gives the file, the field, and the broken rule. Fix the content and re-run. Do not edit the generated HTML to paper over a content failure; the next build overwrites it.
