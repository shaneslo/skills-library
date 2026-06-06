# gainskeeper-operations

Day-to-day exception handling for prime-brokerage tax operations. This plugin holds the assets an analyst reaches for when a break lands in the queue: research it, tie it out, route it, track it, and reply to the field.

## What it holds

One agent and seven skills.

Agent:
- `gainskeeper-exception-research-agent` — drives an exception from intake to a documented disposition.

Skills:
- `gl-reconciler-break-triage` — the exemplar entry; classifies a transaction-log break and names the remediation path.
- `gain-loss-tieout-analyst` — reconciles realized gain/loss against an authoritative source.
- `tax-document-kb-reviewer` — reviews KB articles, client statements, and tax documents for the answer.
- `ops-email-intake-triage` — turns an inbound email into a typed, routable work item.
- `work-item-routing-control` — applies routing rules and the control gate before work moves.
- `break-tracker-sheet-maintainer` — keeps the break tracker current and consistent.
- `field-status-reply-drafter` — drafts the status reply to the field and to leadership.

## How the bodies read

Every body is tool-agnostic prose that works pasted into an API call. Firm specifics live in bracketed `[INSERT: ...]` placeholders an analyst fills at use time. The placeholders are the intended terminal form, not an unfinished draft. Real break taxonomy, routing rules, and form mappings come from the `tax-ops-domain` skill in the `tax-ops-shared` plugin.
