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
- Memory layer: hardcoded absolute paths made portable. The repo-review agent's
  persistent-memory section dropped `/Users/shaneslo/...agent-memory/...` and now
  defers to the `memory: project` managed store, created on first write, removing
  the false "this directory already exists" claim. `memory/projects/skills-library.md`
  no longer pins the repo to an absolute path.

### Added
- `content/entries/period-close-reconciliation-workflow.yaml`: a period-close
  tie-out runbook. It chains existing single-task assets (data-quality profiler,
  GL reconciler break triage, metric-movement diagnostics, KPI readout) into one
  ordered close, with a filing-readiness step and four human sign-off gates. Sits
  in the `research` stage beside the break-diagnostic workflow without overlapping
  it: this one reconciles a whole period, that one diagnoses a single break.
- `tests/test_validate.py`: contract tests for `validate_entries`, one per rule,
  with regression cases for each fix above. Run with `python -m pytest`.
- `requirements-dev.txt` and `requirements.txt` to pin the build and test deps.
- Tracked `.claude/agents/repo-review-orchestrator.md` (was untracked).
- `memory/README.md`: defines the memory layer, its boundary with the build
  (`build/build.py` reads only `content/entries/`, never `memory/`), the
  hot-cache/cold-store context model, the per-file roles, the `projects/`
  convention, and how agent memory under `.claude/` differs. CLAUDE.md "Where
  things live" and the build-pipeline skill now point at the layer, and a comment
  at `CONTENT_DIR` in `build/build.py` records that memory never compiles.

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
