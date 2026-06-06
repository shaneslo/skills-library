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

### Decided (resolves the three 2026-05-31 design calls)
- Workflow stage handling: resolved on `main` by PR #9, which made `stage` a
  required field for every entry and added a Type-axis filter carrying a
  "Workflows" control (`data-type="workflow"`). That surfaces all workflow
  assets regardless of stage and removes the orphaned `data-stage="workflow"`
  value the review flagged. No template change ships in this changelog entry.
- Spec criterion 8 no longer ties `tier` to an uncommitted "research inventory".
  Tier is an integer 1 to 4 set from source provenance, with the rationale
  carried in each entry's `source` and `maturity` fields. The deep-research
  inventory is a research-phase artifact, not a build input. (`SKILLS_LIBRARY_SPEC.md`)
- Exemplar terminal form: bracketed `[INSERT: …]` placeholders are the intended
  terminal state for `adapt` and `author-from-spec` entries, not an incomplete
  one. They mark the adaptation surface where firm-specific domain knowledge is
  supplied at use time. The spec's acceptance criteria now state this, so open
  inserts pass rather than read as unfinished. (`SKILLS_LIBRARY_SPEC.md`)

## [0.1.0] - 2026-05-31

### Added
- Initial scaffold: build pipeline, offline HTML template, spec, domain skills.
- First exemplar entry: `gl-reconciler-break-triage`.
