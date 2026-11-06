# ADR 0007: Expand agent teams only when a baseline justifies them

- Date: 2026-11-06
- Status: Accepted
- Delivery maturity: Unstarted
- Phase: 2
- Supersedes: none

## Context
Specialist agents increase coordination cost, latency, authority complexity and failure propagation; a larger swarm is not inherently better.

## Decision
Begin with one orchestrator. Add analyst and independent verifier only after defining task fixtures and a single-agent/deterministic baseline. Keep task budgets and delegation depth bounded.

## Alternatives considered
| Option | Benefit | Risk |
|---|---|---|
| Fixed three-agent workflow | Easy to reason about and measure | Potentially slower |
| Dynamic swarm | Flexible specialisation | Unbounded cost and ambiguous accountability |
| One agent + deterministic tools | Cheapest baseline | May miss independent checking |

## Consequences
All agents are non-authoritative principals; verifier recommendations do not grant tool permissions. Track per-task success, security finding precision/recall, reproducibility, cost, latency and variance across multiple fixtures.

## Verification and falsification
Demonstrate a reproducible improvement against the same tool budget and dataset. If gains do not justify expense/complexity, retain single-agent design.

## Revisit triggers
Large task benchmark results or robust evidence that collaboration materially improves verified outcomes.
