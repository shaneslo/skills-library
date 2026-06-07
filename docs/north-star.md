# North star

Read this first.

## The purpose

Every asset in this library is a business-critical, portable tool consumed through an API call. The target runtime is a Goldman Sachs gateway or Cloud SDK, not the Claude Code desktop app. The desktop app is a convenient authoring and browsing surface. It is not where the work runs. An asset earns its place only if it works when pasted into an API call as self-contained, tool-agnostic prose.

That constraint drives every design choice. No asset may depend on a connector, a plugin runtime, a database handle, or any host-specific capability to do its core job. The body carries everything the model needs: the task, the method, the guardrails, and bracketed `[INSERT: ...]` placeholders for the firm specifics an analyst supplies at call time.

## What we harvest

We pull the best skills, agents, and commands from many sources: Anthropic knowledge-work plugins, Codex and OpenAI plugins, and enterprise tools such as Linear and Notion and their search patterns. We treat each source as a specification, not as software to install.

## The three-test framework

Every candidate asset passes three tests before it ships.

1. Understand it. Read the source and state plainly what it does and why it works.
2. Decompose to core function and rebuild. Strip the tool-specific scaffolding. Name the one job the asset performs. Rebuild that job as prompt-only prose that runs anywhere a model runs.
3. Adapt to the domain now. Re-express the rebuilt function for prime-brokerage tax-reporting operations: reconciliation, exception research, cost-basis and transaction analysis, tax and regulatory reporting, trade support, and issue routing.

The edge is the domain knowledge poured into the gap the source could not fill. A generic reconciliation prompt is common. A reconciliation prompt that knows the break taxonomy, the routing rules, and the 1099 and 1042-S form mappings is the asset.

## The most valued shape

A command that drives an agent or a skill. The command is the entry point an operator triggers. It carries the workflow, names its sign-off gates, and calls the skills that do the focused work. This shape ports cleanly to an API call: one prompt orchestrates, the others execute.

## The standing rule

The question is never which tools we have. The question is what exists that works. Harvest the decomposition, drop the code that will not run, re-express the rest as prompts the available assistant runs, and fill the domain gap.
