# Chanakya Garuda

Local-first, security-first AI engineering assistant built incrementally on AgentScope, OpenRouter and governed tools.

**Status: Phase 0 / experimental scaffold.** No production credentials, unrestricted shell access, autonomous external scanning or self-authorised tool calls.

## Architecture

See [system architecture](docs/architecture.md), [threat model](docs/threat-model.md), [delivery phases](docs/phases.md), and [ADR 0001](docs/adr/0001-controlled-tool-execution.md).

## Local quickstart

Python 3.11+ and Docker Compose are required for the optional lab.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
pytest -q
chanakya tools
# Set OPENROUTER_API_KEY in .env before invoking:
chanakya ask 'Describe your available tools'
```

The lab uses a fixed Docker-internal target and an explicit confirmation: `chanakya lab-up`, `chanakya lab-scan`, `chanakya lab-down`.

**Security caveat:** CLI consent is a local demonstration, not authenticated, replay-safe authorisation. The model cannot invoke active scans. Container images and dependencies require supply-chain review before any hardened use.

## Roadmap

Phase 0: trusted skeleton and testable policies. Phase 1: OpenRouter limits, evidenced execution, MCP registry. Phase 2: verifier agent and workflows. Phase 3: voice, UI and scheduled personal workflows. See `docs/phases.md` for gates.

## Licence

No licence has been selected yet; the code is publicly visible, but no open-source reuse permission is granted by default.
