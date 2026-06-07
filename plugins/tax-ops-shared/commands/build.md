---
description: Validate, compile the offline HTML, confirm it loads nothing external, report the output path.
# skills-library metadata (ignored by Claude Code)
source: ".claude/commands/build.md"
---

Build the library. Stop at the first failure and say why.

Steps:

1. Validate first. Run `python build/build.py --check`. If it exits non-zero, stop. Report the failing file, field, and rule. Do not build on top of invalid content.
2. Build. Run `python build/build.py`. The script validates again, renders every entry, runs the offline check, and writes `dist/skills-library.html`.
3. Confirm offline compliance. The script scans the output for external `src` and `href` attributes, `<link>` elements, external `<script src>`, `@import`, and `url()` to a remote resource. If it finds any, the build aborts before writing. Confirm the scan reported clean.
4. Report the absolute path to `dist/skills-library.html` and the entry count.
5. Note that the file is meant to open from `file://` with no network.

One failure stops the sequence. Name the failing step, the reason, and the fix. Do not continue past a failure to report a partial result.
