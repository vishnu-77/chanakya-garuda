# ADR 0009: Bind approvals to individual executions

- Date: 2026-11-06
- Status: Proposed
- Delivery maturity: Unstarted; CLI phrase is a demonstration
- Phase: 1
- Supersedes: none

## Context
A typed terminal confirmation is unsuitable for delegated, remote, concurrent or unattended tools. An agent may alter arguments after approval or replay a prior approval.

## Proposed decision
Issue a short-lived, one-time execution permit bound to subject, parent authority, tool digest, canonical argument hash, resource/target, policy version, expiry and nonce. The gateway revalidates context at execution time and atomically consumes the nonce.

## Alternatives considered
| Option | Benefit | Risk |
|---|---|---|
| Single-use bound permit | Explicit replay defence and scoped delegation | Nonce store, signing and canonicalisation burden |
| User prompt per tool call | Simple in local CLI | Approval fatigue and replay ambiguity |
| Broad standing permissions | Efficient | Excessive authority |

## Consequences
Define identity assurance, approval UX, revocation, issuer key rotation, clock skew, atomic issuance/consumption, cancellation and audit. Permit is necessary but does not replace runner/network controls.

## Verification and falsification
Reject argument/target mutation, expired permits, replay, different actor, widened child scope, revoked authority and concurrent double-use.

## Revisit triggers
Remote UI, agents with write access, delegation and scheduled jobs.
