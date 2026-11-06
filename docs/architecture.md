# Architecture — Phase 0

## Boundaries

```text
User (local CLI)
  |-- ask --> AgentScope runtime --> OpenRouter (external model API)
  |                 |
  |                 +--> typed read-only tools
  |                           |--> registry manifests
  |                           +--> previously captured lab evidence
  |
  +-- lab-scan --> human terminal confirmation --> fixed Docker Compose scanner
                                                 |
                                                 +--> isolated HTTP target
```

The model is **not an enforcement point** and cannot invoke the Docker runner. The registry is inventory, not permission: discovery never grants execution. The CLI is an operator entry point, not a remote trust boundary.

## Components

1. **Agent adapter:** AgentScope with OpenRouter's OpenAI-compatible endpoint. AgentScope APIs are pinned; verify with a real integration smoke test before upgrades.
2. **Tool catalogue:** local JSON allowlist, no dynamic installation or auto-loading.
3. **Deterministic policy:** refuses unknown tools; allows active actions only for registered lab-only capabilities plus explicit local consent.
4. **Evidence:** JSON scan result, append-only-style local JSONL event log. Files are mutable; neither cryptographic integrity nor immutability is claimed.
5. **Lab:** Docker internal-only network, non-root scanner and target, limited resource/capability settings; no exposed ports.
6. **Voice:** optional file-based local transcription (separate dependency group); resulting text is sent to the selected remote model.

## Data flows and security boundaries

- Transcribed instructions, prompts and model-callable tool output may leave the machine via OpenRouter.
- Scanner execution stays outside model-exposed tools. The host Docker daemon remains privileged and is not exposed to the agent.
- The model may *read* prior evidence. Treat model-produced conclusions as hypotheses unless corroborated by evidence.
- Lab input is not an arbitrary domain: target/port are constants owned by the application.
- Multiple users, scheduled unattended jobs, production credentials, arbitrary MCP servers and browser automation are out of scope.

## Next target architecture

Introduce a gateway between orchestration and *all* tool execution. Bind execution permits to actor, tool digest, target, argument hash, expiry and single use. Separate the MCP registry, MCP connection broker and authorisation engine. Implement durable run IDs, redacted traces, per-run budgets and evaluation fixtures before adding more autonomous agents.
