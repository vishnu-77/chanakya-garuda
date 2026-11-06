# Chanakya Garuda — Project context

**Version:** 0.1 | **Date:** 2026-11-06 | **Status:** living architecture context | **Source of truth:** this repository.

## 1. Problem and intent

Build a **local-first hybrid AI engineering assistant** that supports daily engineering tasks and controlled cybersecurity research. The system should interpret user intent, discover reviewed capabilities, route requests to models, execute *authorised* operations through a deterministic gateway, preserve evidence, and report uncertainty. It is **not** an unrestricted offensive swarm or a production-ready security control.

The product is called **Chanakya Garuda**. JARVIS is the interaction concept, not a dependency.

### Measurable success
- An approved read-only workflow can retrieve registered tools/evidence and answer with source references.
- An unauthorised active operation is denied without model cooperation.
- The lab cannot access arbitrary external targets (demonstrated by negative integration tests).
- Every executed tool call is attributable to a run, identity, target/scope, policy decision and evidence record (Phase 1).
- Delegated agents outperform an appropriate single-agent baseline on at least one measurable, defined task family before expansion (Phase 2).

## 2. Stakeholders and operating model

| Role | Responsibility | Trust |
|---|---|---|
| Local operator | Specifies intent and explicitly approves sensitive actions | Authenticated operator in future; CLI terminal consent only in v0.1 |
| Orchestrator | Plans and selects eligible tools | Untrusted decision maker |
| Specialist agent | Performs bounded analysis | Untrusted decision maker |
| Verification agent | Independently tests claims | Untrusted decision maker; not final authoriser |
| Policy/authorisation gateway | Enforces scope, identity, approvals and budgets | Trusted service with narrow privileges |
| Tool runner | Executes vetted code inside limits | Privileged boundary; restrict aggressively |
| Model provider | Generates reasoning/tool proposals | External processor; never handles secrets by default |

## 3. Invariants (MUST)

| ID | Invariant | Enforcement locus | Evidence |
|---|---|---|---|
| INV-01 | Model output never grants execution rights | Policy gateway, not prompt | Denial tests |
| INV-02 | Every active tool invocation has explicit allowed scope and target | Gateway + runner | Argument/scope mismatch tests |
| INV-03 | Discovery and installation/activation are separate privileges | Registry admin boundary | Unregistered-tool rejection |
| INV-04 | Child delegation cannot broaden authority | Delegation validator | Multi-hop attenuation tests |
| INV-05 | Expired/replayed/modified approval cannot execute | Authorisation service | Replay and tamper tests |
| INV-06 | No production credentials or third-party data egress by default | Secrets broker and routing policy | DLP/redaction tests |
| INV-07 | Task and provider budgets halt execution before exhaustion | Model proxy + task runner | Cost/call exhaustion tests |
| INV-08 | Security findings record source, observation and uncertainty | Evidence service and verifier | Blind labelled evaluation |
| INV-09 | Docker access is never exposed to agent tools | Host architecture | Integration inspection |
| INV-10 | Every failure and denial produces inspectable telemetry | Audit service | Failure injection tests |

These are **target invariants**. Phase 0 implements only narrow portions of INV-01/02/03/09. A design claim is not an implementation claim.

## 4. Current system and future architecture

```text
Phase 0 — implemented scaffold (integration unverified)
operator CLI --ask--> AgentScope --> OpenRouter
                      |--> catalogue reader / prior evidence reader
operator CLI --confirm--> fixed Docker runner --> internal target

Phase 1+ — proposed boundary
UI/CLI/voice --> API/auth --> task orchestrator --> model adapter
                                    |
                               tool request
                                    v
                          policy + scoped approval
                                    |
                             execution gateway
                              /      |      \
                          MCP       jobs    lab runner
                                    |
                            evidence + audit + budgets
```

## 5. Data classification and handling

| Class | Examples | Default allowed destination |
|---|---|---|
| Public | Published CVEs, public open-source documentation | Approved model provider |
| Local research | Synthetic lab traces, fixtures | Local store; external model only with operator configuration |
| Confidential | Private repository source, company logs | Local authorised boundary only until policy exists |
| Secret | API keys, tokens, private keys | Secret broker only; never prompt/evidence/log |

Voice transcription is local, but **its transcript is not local-only** when passed to OpenRouter. Images/video generation is optional and out of MVP runtime scope; no OpenArt dependency is required in Phase 0.

## 6. Working surfaces

| Surface | Phase | Interface | Write permission |
|---|---|---|---|
| Tool inventory | 0 | Local JSON read-only | Operator-controlled git changes |
| Evidence reader | 0 | AgentScope function tool | None |
| Isolated lab | 0 | Fixed CLI operation | Active scan behind local consent |
| MCP gateway | 1 | Reviewed explicit tool registration | Admin-only install/activate |
| GitHub PR review | 2 | Read-only API adapter | None |
| Scheduled briefings | 3 | Background runner | Local report only initially |
| Dashboard/voice | 3 | Local authenticated UI | Scoped approval required |

## 7. Decision governance

ADRs in [adr/README.md](adr/README.md) define the *why*. [DECISIONS.md](DECISIONS.md) is the register; [PHASE-MATRIX.md](PHASE-MATRIX.md) tracks delivery and acceptance. [phases.md](phases.md) is the initial historical roadmap and must not be interpreted as evidence of completion.

Decision states: **Proposed → Accepted → Implemented → Verified**, with **Rejected** and **Superseded** as terminal dispositions. Implementation maturity is a separate axis from decision status. Every ADR should have one decision, trade-offs, alternatives, falsifiers, and a review trigger.

## 8. Out-of-scope and non-goals

No self-installing tools, arbitrary shell agents, arbitrary network recon, production cloud write permissions, unsupervised external publication, multi-tenant SaaS, Kubernetes, distributed consensus, or claims of formally verified policy in initial phases.

## 9. Research hypothesis (not established fact)

Testing authority attenuation, evidence provenance and bounded autonomous execution may yield useful results. Existing frameworks already provide agent collaboration and tool integrations; novelty must be demonstrated through prior-art comparison, baseline evaluation and reproducible security experiments.

## 10. Open decisions

- Whether ToolHive offers measurable value over a simple local MCP connector for this single-user MVP.
- Which model routing/provider fallback policies satisfy cost, privacy and function-calling reliability.
- What durable event/evidence store is justified after local SQLite.
- What precisely qualifies as an independently verified vulnerability.
- What additional threat controls are needed before unattended scheduling.

Resolve these through explicit ADR amendments or new ADRs after experimentation; do not silently turn proposals into accepted architecture.
