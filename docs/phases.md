# Delivery plan and evidence gates

## Phase 0 — architecture skeleton (this commit)
- [x] Project layout, registry, read-only AgentScope toolkit, optional voice adapter, fixed Docker lab and unit policy tests.
- [ ] Verify AgentScope/OpenRouter live tool-call compatibility (requires a user key).
- [ ] Execute Docker lab integration and negative egress tests on an actual Docker host.
- [ ] Configure OpenRouter key-level hard spending limit.

**Gate:** all three tests above documented, no unauthorised execution, no exposed secrets.

## Phase 1 — governed execution
- Implement tool schema validation, identity, explicit scopes and deny-by-default policy.
- Build an MCP client/registry gateway. ToolHive is a candidate; evaluate against simpler local MCP before selecting.
- Add execution-bound, single-use, expiring approvals; no agent self-approval.
- Build provider-independent request limits, token/cost ledger and timeout enforcement.
- Add trace identifiers, evidence hashes and structured outcomes.

**Gate:** adversarial tests for scope bypass, replay, tool-output injection, malformed schemas and budget exhaustion.

## Phase 2 — useful security workflows
- One orchestrator, security analyst and independent verifier; avoid unbounded agent spawning.
- Read-only GitHub PR review; Trivy/Checkov/Prowler via reviewed adapters.
- Local lab findings with evidence references, confidence and reproducible test fixtures.
- Compare single-agent vs delegated workflow on quality, cost and latency.

**Gate:** benchmark demonstrates a reason to use multiple agents rather than a single agent plus deterministic tools.

## Phase 3 — assistant experience
- Push-to-talk via local Whisper, optional TTS, desktop/web command centre.
- Scheduled personal briefings, repository triage and research summaries.
- Explicit approvals for outbound writes; separate personal and organisational environments.

**Gate:** authenticated multi-user design and bounded unattended execution before any externally reachable service.

## Deliberately postponed
Kubernetes, multi-region message buses, broad MCP auto-discovery, general-purpose shell agents, production cloud write access and self-modifying agents. Add only in response to validated requirements.
