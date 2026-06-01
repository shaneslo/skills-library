# Changelog

All notable changes to the Skills Library. Newest first. Dates are YYYY-MM-DD.

## [Unreleased]

### Fixed
- Validation: remediation detection in workflows now scans each step's `output`,
  not just `title` and `prompt`. A remediation described only in the output no
  longer slips past the human-sign-off-gate rule. (`build/build.py`)
- Validation: a YAML-quoted `tier` (for example `"2"`) is accepted instead of
  hard-failing. The validator now coerces with `int()`, matching the renderer.
- Validation: the tool-agnostic scan on `core_function` catches plural tokens.
  "calls external APIs" now trips the rule, where only "API" did before.
- Offline check: patterns catch protocol-relative references (`//cdn…`), not just
  `https?:`. A protocol-relative external src, href, or `url()` is now flagged.
- `.gitignore`: secret coverage widened to `.env*`, `credentials.json`,
  `token.json`, `oauth_creds.json`, `client_secret*.json`, `.ssh/`, `.mcp-auth/`.

### Added
- `tests/test_validate.py`: contract tests for `validate_entries`, one per rule,
  with regression cases for each fix above. Run with `python -m pytest`.
- `requirements-dev.txt` and `requirements.txt` to pin the build and test deps.
- Tracked `.claude/agents/repo-review-orchestrator.md` (was untracked).

### Known, deferred to a design decision
- Workflow stage filtering: a workflow with no `stage` renders with
  `data-stage="workflow"`, a value no filter button selects. It stays visible
  under "All" and tier filters, grouped under "cross-stage workflows". Decide
  whether workflows get a real stage or the filter gains a "workflow" control.
- Spec criterion 8 ties `tier` to a "research inventory" that is not a checked-in
  file. Either commit the inventory or drop the criterion.
- The exemplar entry names its `[INSERT: …]` gaps but never fills one. Decide
  whether to ship a fully-assembled sibling or to document open brackets as the
  intended terminal state.

## [0.1.0] - 2026-05-31

### Added
- Initial scaffold: build pipeline, offline HTML template, spec, domain skills.
- First exemplar entry: `gl-reconciler-break-triage`.
