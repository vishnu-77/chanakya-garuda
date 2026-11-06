# ADR 0005: Start with a fixed-target Docker security lab

- Date: 2026-11-06
- Status: Accepted
- Delivery maturity: Compose scaffold, isolation unverified
- Phase: 0–1
- Supersedes: none

## Context
Security experiments may produce network traffic, resource pressure or malicious test content. Arbitrary hosts and arguments would make early autonomy unsafe.

## Decision
Initial lab operations use a fixed Docker-internal HTTP target and a predefined TCP connect scan. Operator approval occurs in a local CLI. No host ports or Docker socket are presented to the agent. Add more targets only through reviewed fixtures.

## Alternatives considered
| Option | Benefit | Risk |
|---|---|---|
| Isolated Docker lab | Cheap, reproducible | Docker daemon/rootless isolation limitations |
| VM/microVM lab | Stronger containment | More CPU and setup |
| Cloud lab | Realism and scale | Cost, egress and identity risk |

## Consequences
The current Compose network is a design intention, not proof of isolation. Pin image digests; run negative egress tests and confirm scanner limits. Do not treat Docker as hostile-code containment without a stronger isolation assessment.

## Verification and falsification
Validate fixed target, denied arbitrary domain, no external egress, no port exposure, no Docker socket and bounded CPU/memory/timeout. Move to VM/microVM where stronger isolation is required.

## Revisit triggers
Unknown code execution, adversarial payloads, dynamic targets, multi-user runtime or network realism needs.
