# Chanakya Garuda

Architecture-first, local-first AI engineering assistant for authorised security research and everyday engineering work.

**Phase 0 — experimental scaffold, not a production security boundary.**

## Quickstart

Python 3.11+; Docker Compose is optional for the local lab.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
pytest -q
chanakya tools
# Set OPENROUTER_API_KEY in .env before using the model
chanakya ask "Explain what tools you have"
# Optional, isolated lab:
chanakya lab-up
chanakya lab-scan
chanakya lab-down
```

## Design

- [Architecture](docs/architecture.md)
- [Threat model](docs/threat-model.md)
- [Phased delivery and acceptance gates](docs/phases.md)
- [ADR: Separate execution from reasoning](docs/adr/0001-controlled-tool-execution.md)

Only catalogue discovery and evidence reading are exposed as model-callable tools. Active lab scanning is available **only** from the local CLI with explicit terminal confirmation. The scan's target and flags are fixed. The repository has no production cloud integrations or arbitrary shell agent.

**Not implemented:** hard local model spend caps, signed execution approvals, independent verifier, ToolHive connection, persistent task orchestration or a GUI. A provider-side OpenRouter spending limit is mandatory for initial experimentation. Never connect organisational secrets or production assets without independent authorisation.

**Licence:** none selected yet; public visibility is not an open-source licence.
