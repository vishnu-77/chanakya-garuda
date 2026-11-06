# ADR 0002: Use AgentScope as the MVP agent runtime

- Date: 2026-11-06
- Status: Accepted for MVP
- Delivery maturity: Scaffold; integration unverified
- Phase: 0
- Supersedes: none

## Context
The assistant needs tool calling, agent context and later delegation, but writing an orchestration engine now would add complexity with little research value.

## Decision
Use AgentScope 2.x behind a narrow internal adapter for model calls, tool registration and future task delegation. Keep policy decisions outside the framework. Pin a version and verify actual runtime behaviour.

## Alternatives considered
| Option | Advantage | Drawback |
|---|---|---|
| AgentScope | Agent/team APIs with integrated tool surface | SDK volatility and adaptation cost |
| Pydantic AI | Typed Python tool/response contracts | Requires separate orchestration integration |
| LangGraph | Explicit durable graphs and checkpoints | Heavier state-machine setup for v0.1 |
| Custom runtime | Full control | High maintenance and low differentiation |

## Consequences
The adapter is replaceable; tool and approval contracts must be framework-neutral. A lockfile, SDK smoke tests and breakage handling are required. Framework convenience APIs must never become execution authority.

## Verification and falsification
Run clean install, direct model response, read-only tool invocation and malformed tool-call tests. Reconsider if the SDK cannot satisfy these reliably or requires bypassing security constraints.

## Revisit triggers
API incompatibility, need for durable recovery, unacceptable latency or operational fragility.
