# Threat model v0.1

## Protected assets
Model API credentials, authorised target inventory, host runtime, lab execution boundary, evidence integrity, user data, provider budget and future organisational source data.

## Adversaries and untrusted inputs
Prompt-injected evidence; compromised dependencies/container images; malicious MCP servers (not yet enabled); adversarial target output; an agent that tries to reinterpret its own authority; careless operator consent.

## Threats, controls and gaps

| Threat | Phase-0 control | Residual gap |
|---|---|---|
| Prompt injection triggers active scan | Active scan absent from model toolkit | CLI operator could be misled |
| Scan goes outside authorised lab | Fixed service alias, Docker internal network | Docker/network config changes require integration validation |
| Arbitrary shell execution | No shell tool exposed to model | Host CLI and package installs remain privileged |
| Token/cost runaway | Provider-side spending cap (operator configured) | No local per-task metering or hard request cap |
| Credential exfiltration | No secrets tool; .env ignored | Prompt and tool output still sent to provider |
| False security conclusions | Evidence-reading tool and system-level caution | No independent evaluator yet |
| Evidence tampering | Local JSON + audit events | No signatures or write-once store |
| Compromised images/dependencies | Pinned AgentScope version | Docker base images not digest-pinned |
| Consent replay or impersonation | Interactive local terminal phrase | Not suitable for remote use |

## Invariants to test before Phase 1 exit
- An unknown tool is denied.
- A registered read-only tool cannot be invoked through the active-execution path.
- Active lab operations fail without approval.
- Tool APIs do not accept caller-controlled scan host/flags.
- Scanner network has no unintended outbound route (validate using Docker integration tests).
- No scanner or Docker socket is visible to model tools.
- Redacted traces never contain credentials.
