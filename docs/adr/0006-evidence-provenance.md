# ADR 0006: Establish a structured evidence provenance contract

- Date: 2026-11-06
- Status: Proposed
- Delivery maturity: Unstarted; mutable local JSON only
- Phase: 1
- Supersedes: none

## Context
Tool output alone is insufficient to reproduce security findings, and LLM summaries can introduce unsupported interpretations.

## Proposed decision
Record a run ID, actor/delegation chain, tool identity and digest, immutable arguments hash, target, policy decision, timestamps, exit code, bounded stdout/stderr, redaction result, source references and evidence hash for every execution. Separate observations from model interpretations.

## Alternatives considered
| Option | Benefit | Risk |
|---|---|---|
| JSONL + content-addressed artefacts | Simple and inspectable | Local tamper risk and rotation complexity |
| SQLite events + immutable artefacts | Transactionality | Schema/operational complexity |
| Full event-sourced backend | Audit/replay potential | Overengineering for single user |

## Consequences
Evidence retention, encryption, secrets redaction and event schema migration must be defined. No claim of cryptographic immutability until an actual integrity design is verified.

## Verification and falsification
Reconstruct a report from stored runs; detect changed evidence; reliably redact known secret fixtures; report missing evidence rather than assert certainty.

## Revisit triggers
Multi-host execution, retention requirements, independent forensic audit or benchmark reproducibility needs.
