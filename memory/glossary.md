# Glossary

| Term | Meaning |
|------|---------|
| PB | Prime brokerage |
| GS | Goldman Sachs |
| Break | A reconciliation discrepancy between two sources that must be researched and resolved |
| Cost basis | Original value of an asset for tax purposes; central to tax-lot and gain/loss reporting |
| 1099 (DIV/B/INT) | US information returns for dividends, broker proceeds, interest |
| 1042-S | US information return for income paid to foreign persons (NRA withholding) |
| FATCA | Foreign Account Tax Compliance Act; drives account classification and reporting |
| CRS | Common Reporting Standard; OECD analog to FATCA |
| NAV | Net asset value |
| Tie-out | Reconciling a statement or report against an authoritative source until they agree |
| Remediation path | How a break gets fixed: UI, XML update, SQL query, or plugin |
| Reader-critic-resolver | Anthropic GL Reconciler agent decomposition: one worker reads/extracts, one critiques, one resolves/routes |

## Asset-strategy terms
| Term | Meaning |
|------|---------|
| Three tests | Understand it / decompose it / adapt it; the filter for adopting any asset |
| Specs not software | Treat credible repos as design specifications to harvest, not code to run |
| Domain-knowledge gap | The tax/withholding/break-taxonomy knowledge the user pours into a generic skill to make it role-fit |
| Execution layer | The tool that actually runs the content (GS assistant, Copilot, Claude); swappable |

## Build terms
| Term | Meaning |
|------|---------|
| Three-layer build | Content (YAML) separated from presentation (HTML template), assembled by a Python build script |
| Four hard rules | The build's gating checks: required fields present, core_function tool-agnostic, domain_gap substantive, workflow remediation carries a sign-off gate |
| Section 8 bar | The quality standard set by the worked exemplar in SKILLS_LIBRARY_SPEC.md; every entry matches its shape and depth |
| Stage | The primary navigation axis: intake-classify, research, remediate, communicate |
| Offline check | The build step that aborts if the compiled HTML references anything external |
| dist | The generated-output directory; holds the compiled skills-library.html, gitignored |
