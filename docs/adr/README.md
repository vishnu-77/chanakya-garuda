# Architecture Decision Records

ADRs capture decisions and their trade-offs, *not* project progress. The high-level index is [../DECISIONS.md](../DECISIONS.md) and phase delivery is [../PHASE-MATRIX.md](../PHASE-MATRIX.md).

## Rules
1. Use a monotonically increasing identifier: `NNNN-kebab-case-title.md`.
2. Decide exactly one architectural question per ADR.
3. State date, status, affected phase, context, decision, alternatives, security/operational consequences, validation and revisit triggers.
4. Do not retroactively change rationale to pretend future evidence was known. Correct editorial errors in place; supersede substantive changes with a new ADR.
5. A decision can be Accepted while implementation is entirely absent. Never conflate these statuses.
6. New PR changing an architectural boundary must update the register and phase acceptance gates.

## Index
- [0001 — Separate reasoning from privileged execution](0001-controlled-tool-execution.md)
- [0002 — AgentScope runtime](0002-agentscope-runtime.md)
- [0003 — OpenRouter model boundary](0003-openrouter-model-boundary.md)
- [0004 — Tool registry versus authority](0004-tool-registry-vs-authority.md)
- [0005 — Lab execution isolation](0005-lab-execution-isolation.md)
- [0006 — Evidence provenance](0006-evidence-provenance.md)
- [0007 — Evaluated multi-agent expansion](0007-evaluated-multiagent-expansion.md)
- [0008 — Local-first data and budget](0008-local-first-data-and-budget.md)
- [0009 — Execution-bound approval capabilities](0009-approval-capabilities.md)

Use [TEMPLATE.md](TEMPLATE.md) for new decisions.
