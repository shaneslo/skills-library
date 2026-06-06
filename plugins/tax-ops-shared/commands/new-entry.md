---
description: Scaffold a new content entry with every schema field pre-filled and commented.
argument-hint: "<slug> \"<name>\""
# skills-library metadata (ignored by Claude Code)
source: ".claude/commands/new-entry.md"
---

Create a new asset entry. Use $ARGUMENTS, the first argument as the id slug and the filename, and the second as the name when given.

Write a new file at `content/entries/<slug>.yaml` from the scaffold below. Fill what the request gives you and leave the rest as the prompts shown. Match the depth of the exemplar in `SKILLS_LIBRARY_SPEC.md` section 8. An entry that cannot pass the three tests visibly is not ready, so do not scaffold and walk away; load the tax-ops-domain skill and write a real `domain_gap`.

For a prompt, skill, or agent, use this scaffold:

```yaml
id: <slug>                   # stable slug, lowercase-with-hyphens, matches the filename
name: "REPLACE"              # human-readable title, sentence case
type: skill                  # one of: prompt, skill, agent, workflow
stage: research              # one of: intake-classify, research, remediate, communicate
tier: 1                      # credibility tier 1 to 4, from the research inventory
source: "REPLACE, origin plus link"   # where it came from
core_function: >             # one sentence, tool-agnostic. Name no database, runtime, or connector.
  REPLACE with the decomposed core, stripped of any tooling.
domain_fit: >                # which domain priority it serves and how directly
  REPLACE with the priority it serves and how directly.
adaptation: author-from-spec # one of: use-as-is, adapt, author-from-spec
maturity: >                  # trust signal: stars, vendor backing, last updated, author standing
  REPLACE with the maturity signal from the inventory.
body: |                      # the copy-pasteable asset text, the expandable payload
  REPLACE with the full prompt or skill text. Keep it tool-agnostic.
  Put firm specifics in bracketed inserts and pull them from the domain skill.
  [INSERT: the domain reference this body needs]
domain_gap: >                # what the analyst supplies to make it role-fit. Never blank for a finance asset.
  REPLACE. Name the exact domain knowledge the source cannot provide: the
  break-cause taxonomy, the remediation routing rules, the income-type to
  tax-form mapping, or whatever this asset needs. A one-line gap is a failure.
  Say what gets poured in and what changes once it is filled, to the section 8 standard.
notes: >                     # optional: caveats, licensing, prerequisites
  REPLACE or delete this field.
```

For a workflow, swap to these fields instead:

```yaml
id: <slug>
name: "REPLACE"
type: workflow
tier: 1
source: "REPLACE, origin plus link"
domain_fit: >
  REPLACE.
maturity: >
  REPLACE.
trigger: >                   # what starts the workflow: an inbound issue, a period close, a flagged break
  REPLACE.
steps:                       # ordered. Each step: title, optional asset reference, prompt, output.
  - title: "REPLACE"
    asset: optional-entry-id # optional reference to another entry's id
    prompt: |
      REPLACE with the step prompt.
    output: "REPLACE with what the step produces"
gates:                       # explicit human-sign-off points. A remediation step with no gate is a defect.
  - "REPLACE with the sign-off required before a change is made"
output: >                    # the end artifact: a break table, a status note, a corrected log
  REPLACE.
```

After writing the file, run `/validate` and clear every failure before `/build`.
