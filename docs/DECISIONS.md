# Architecture decision register

**Source of truth:** individual [ADRs](adr/README.md). This is an index, not a replacement for their rationale.

| ID | Atomic decision | Decision state | Delivery maturity | Phase | Review trigger |
|---|---|---|---|---|---|
| [0001](adr/0001-controlled-tool-execution.md) | Model reasoning cannot authorise active execution | Accepted | Partial scaffold | 0/1 | Remote/writable tools |
| [0002](adr/0002-agentscope-runtime.md) | Use AgentScope as MVP runtime, behind an adapter | Accepted for MVP | Adapter exists; live unverified | 0 | SDK instability/failed tool calls |
| [0003](adr/0003-openrouter-model-boundary.md) | Route LLM inference through OpenRouter | Accepted for MVP | Adapter exists; guardrails incomplete | 0/1 | Privacy, price, outage, routing mismatch |
| [0004](adr/0004-tool-registry-vs-authority.md) | Separate catalogue, connection broker and policy | Accepted | Catalogue only | 0/1 | Tool activation requirements |
| [0005](adr/0005-lab-execution-isolation.md) | Use fixed-target isolated Docker lab initially | Accepted | Compose exists; egress unverified | 0/1 | Arbitrary tests or cloud targets |
| [0006](adr/0006-evidence-provenance.md) | Introduce trace/evidence provenance contract | Proposed | JSON evidence only | 1 | Research reproducibility needs |
| [0007](adr/0007-evaluated-multiagent-expansion.md) | Require baseline evaluation before swarm expansion | Accepted | Not implemented | 2 | Evidence of useful delegation |
| [0008](adr/0008-local-first-data-and-budget.md) | Local-first interaction with explicit data routing and budgets | Accepted | Partial; no local budget enforcement | 0/1/3 | Multi-user or confidential data |
| [0009](adr/0009-approval-capabilities.md) | Bind approval to exact execution and prevent replay | Proposed | CLI consent only | 1 | Gateway implementation |

## Change discipline

- **One ADR, one decision**. Do not combine unrelated choices to make the count smaller.
- Distinguish **decision state** from **implementation maturity**.
- Never mark an ADR Verified merely because code was committed.
- An accepted decision that changes materially gets a new ADR with `Supersedes: 000N`; the old ADR becomes Superseded with a backlink.
- ADR authors should include alternatives, trade-offs, security consequences, verification and falsification conditions.
- Update this register and affected phase gates in the same PR as an ADR change.
- Log experiment evidence in PRs/issues; don't fabricate benchmark results.

## Status vocabulary

**Proposed:** being evaluated. **Accepted:** chosen design, not necessarily coded. **Rejected:** ruled out with rationale. **Superseded:** replaced by a later ADR. Implementation maturity separately uses **Unstarted**, **Scaffold**, **Implemented (untested)**, **Integration tested** or **Verified against gate**.
