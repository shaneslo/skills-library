"""Contract tests for validate_entries, the function the whole quality bar rests on.

Run from the repo root:
    pip install pyyaml markdown pytest
    python -m pytest

Each test crafts entry dicts and asserts which (file, field, message) tuples come
back. The fields named in the assertions are the rule under test.
"""

import sys
from pathlib import Path

# build.py lives in build/; add it to the path so we can import the validator.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "build"))

from build import validate_entries  # noqa: E402


def asset(**over):
    # A minimal asset entry that passes every rule. Override one field per test.
    e = {
        "_file": "demo-entry.yaml",
        "id": "demo-entry",
        "name": "Demo entry",
        "type": "prompt",
        "tier": 2,
        "source": "example/repo",
        "domain_fit": "Reconciliation, directly.",
        "maturity": "vendor-backed, active",
        "stage": "research",
        "core_function": "Compare two records and surface the differences.",
        "adaptation": "adapt",
        "body": "Do the thing.",
        "domain_gap": "Insert the break taxonomy, the routing rules, and the form mappings the analyst supplies.",
    }
    e.update(over)
    return e


def workflow(**over):
    e = {
        "_file": "demo-flow.yaml",
        "id": "demo-flow",
        "name": "Demo flow",
        "type": "workflow",
        "tier": 1,
        "source": "example/repo",
        "domain_fit": "Reconciliation, directly.",
        "maturity": "vendor-backed, active",
        "trigger": "An inbound break lands in the queue.",
        "steps": [{"title": "Read the log", "prompt": "Read it."}],
        "gates": ["Analyst confirms the classification."],
        "output": "A classified break.",
    }
    e.update(over)
    return e


def fields(errors):
    return {field for _f, field, _m in errors}


def test_valid_asset_passes():
    assert validate_entries([asset()]) == []


def test_valid_workflow_passes():
    assert validate_entries([workflow()]) == []


def test_missing_required_field_is_flagged():
    e = asset()
    del e["domain_fit"]
    assert "domain_fit" in fields(validate_entries([e]))


def test_unknown_type_is_flagged():
    assert "type" in fields(validate_entries([asset(type="macro")]))


def test_id_must_match_filename_stem():
    assert "id" in fields(validate_entries([asset(id="something-else")]))


def test_duplicate_id_is_flagged():
    errors = validate_entries([asset(), asset()])
    assert any("duplicate id" in m for _f, field, m in errors if field == "id")


def test_tier_out_of_range_is_flagged():
    assert "tier" in fields(validate_entries([asset(tier=9)]))


def test_quoted_tier_string_is_accepted():
    # Regression: a YAML-quoted tier ("2") must pass, matching the renderer's int().
    assert "tier" not in fields(validate_entries([asset(tier="2")]))


def test_tool_token_in_core_function_is_flagged():
    assert "core_function" in fields(
        validate_entries([asset(core_function="Query the SQL database for breaks.")])
    )


def test_plural_tool_token_is_flagged():
    # Regression: "APIs" must trip the scan, not just "API".
    assert "core_function" in fields(
        validate_entries([asset(core_function="Calls external APIs to fetch data.")])
    )


def test_thin_domain_gap_is_flagged():
    assert "domain_gap" in fields(validate_entries([asset(domain_gap="ask someone")]))


def test_remediation_without_gate_is_flagged():
    e = workflow(
        steps=[{"title": "Correct the cost basis", "prompt": "Apply the fix."}],
        gates=[],
    )
    assert "gates" in fields(validate_entries([e]))


def test_remediation_described_only_in_output_still_needs_a_gate():
    # Regression: remediation in the step output, not the title/prompt, must still
    # require a sign-off gate.
    e = workflow(
        steps=[{"title": "Step one", "prompt": "Look at it.",
                "output": "The corrected cost-basis record is posted."}],
        gates=[],
    )
    assert "gates" in fields(validate_entries([e]))
