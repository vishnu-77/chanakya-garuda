# Phase execution matrix

**Review date:** 2026-11-06. Status is evidence-driven, not aspiration. Gate owners are role labels until assigned.

| Phase | Goal | Dependency | Work packages | Minimum acceptance evidence | Status |
|---|---|---|---|---|---|
| 0 | Establish a constrained local scaffold | None | AgentScope adapter; OpenRouter config; read-only tools; fixed Docker lab; policy tests | Python tests + live tool-call smoke test + lab negative egress and deny tests | **Scaffold committed; gate open** |
| 1 | Govern all tool calls | Phase 0 gate | Tool schema contracts; tool registry+MCP broker; policy engine; signed/nonce-bound approvals; task budget proxy; structured traces | Attack tests for scope, delegation, replay, provider overrun and untrusted tool content | Planned |
| 2 | Deliver useful security workflows | Phase 1 gate | GitHub read-only PR review; Trivy/Checkov adapters; analyst & independent verifier; fixtures | Baseline comparison with measured quality, cost, latency and failure rate | Planned |
| 3 | Add assistant experience | Phase 2 service reliability | Voice push-to-talk; UI; scheduler; notifications; personal integrations | Authenticated operations, safe cancellations, idempotent jobs, no unintended external writes | Planned |
| 4 | Test research claims | Phases 1–3 traces | Controlled red-team evaluation; multi-agent ablations; replication harness | Public methodology, raw traces or redacted dataset, statistics, clearly stated limits | Research proposal |

## Phase 0 checklist

| ID | Task | Current evidence | Blocker | Gate |
|---|---|---|---|---|
| P0-01 | Repository and structure | Git commit exists | None | Done |
| P0-02 | Unit policy tests | Test files committed | Must run on clean machine | Open |
| P0-03 | AgentScope ↔ OpenRouter compatibility | Adapter committed | Live API key and SDK integration run | Open |
| P0-04 | Fixed lab executes | Compose + runner committed | Docker host run | Open |
| P0-05 | Prove network isolation | Internal Docker network configured | Negative egress testing | Open |
| P0-06 | Provider spending cap | Documented operational prerequisite | Configure dedicated API key externally | Open |
| P0-07 | Secret/supply-chain scan | .gitignore committed | Scan actual public repository and dependencies | Open |

## Phase 1 atomic increments

| ID | Increment | Required invariant | Acceptance test |
|---|---|---|---|
| P1-01 | Typed capability/tool manifest and parser | INV-03 | Reject malformed/unknown/duplicate tool |
| P1-02 | Policy API with explicit actor, action, resource and context | INV-01/02 | Deny on missing/forged scope |
| P1-03 | Approval with nonce, digest, expiry and one-time use | INV-05 | Replay/mutation rejected |
| P1-04 | MCP gateway with reviewed server allowlist | INV-03 | Unregistered server denied |
| P1-05 | Sandbox wrapper with network/resource constraints | INV-02/09 | Negative egress and timeout tests |
| P1-06 | Provider budget preflight and reconciliation | INV-07 | Hard stop before limit; concurrent reservation test |
| P1-07 | Run ledger with evidence hashes and redaction | INV-08/10 | Deterministic audit and failure trace |
| P1-08 | Attenuated delegation tokens | INV-04 | Grandchild cannot widen ancestor authority |

## Phase 2 workflow increments

| ID | Workflow | Baseline | Result schema |
|---|---|---|---|
| P2-01 | PR security review | Deterministic scanners + single agent | File/line, finding, reproduction, confidence, evidence |
| P2-02 | Cloud/IaC posture | Checkov/Trivy without LLM | Resource, control, impact, remediation, evidence |
| P2-03 | Local lab inspection | Fixed scanner only | Scope, observation, hypotheses, next validations |
| P2-04 | Verifier assessment | Analyst without verifier | Confirmed/refuted/unresolved + reproducibility |
| P2-05 | Agent collaboration ablation | Single agent same tool budget | Precision/recall, verified findings/£, wall time, failure rate |

## Phase 3 workflow increments

| ID | Experience | Constraint | Acceptance |
|---|---|---|---|
| P3-01 | Local push-to-talk | No always-on recording | Audio stays local until transcript deliberately sent |
| P3-02 | Command centre | Authenticated operator | Tool call and approval history visible |
| P3-03 | Threat-intel briefing | Source freshness and dedup | Evidence links and no fabricated incidents |
| P3-04 | Scheduling | Idempotent jobs and cancellation | Crash/retry tests, budget ceilings |
| P3-05 | Personal tools | Consent per integration | No unintended send/delete/write |

## Gate procedure

1. Record the command, environment, versions, test fixture and date.
2. Attach machine-readable outputs, negative tests and known failure modes.
3. Compare against the phase gate, not the existence of source files.
4. Mark **Verified** only after independent execution or reproducible CI.
5. If a gate fails, keep the phase open and create the smallest corrective issue.

No arbitrary calendar deadline replaces a failed security gate.
