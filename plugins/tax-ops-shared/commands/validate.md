---
description: Validate every content entry against the schema and the four hard rules. No build.
# skills-library metadata (ignored by Claude Code)
source: ".claude/commands/validate.md"
---

Validate the content library and report. Do not build.

Steps:

1. Run `python build/build.py --check` from the repo root.
2. Read `content/entries/` so you can point to the exact file and field for any failure the script reports.
3. Confirm the four hard rules hold for every entry:
   - All required schema fields are present for the entry type. Assets follow `SKILLS_LIBRARY_SPEC.md` section 4; workflows follow section 5.
   - `core_function` names no tool. A database, a language runtime, or a connector in `core_function` is a failure; the core has not been decomposed.
   - `domain_gap` is present and substantive for every finance asset. A blank or one-line note is a failure.
   - Every workflow with a remediation step carries an explicit human-sign-off gate.
4. Output a pass or fail report. Open with one line: PASS, or FAIL with the issue count. For each failure give the file, the field, and the rule it broke. State passes as a count.
5. Fail loudly. If anything fails, say so first, in plain words, before the detail. Do not soften it and do not bury it.

A non-zero exit blocks the build until every failure clears. If the report is clean, say the library is ready to build.
