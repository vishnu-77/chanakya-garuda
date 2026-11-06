# ADR 0001: Separate reasoning from privileged execution

**Status:** accepted for scaffold (2026-11-06)

## Context
AgentScope can select and invoke tools, but an LLM instruction is not a reliable authorisation mechanism. Security-assessment operations can affect networked targets and may consume resources or expose credentials.

## Decision
Expose only deterministic low-risk functions to the model in Phase 0. Put active lab scanning behind a separate local CLI path with fixed target/arguments, an explicit operator confirmation and audit events. Later replace this limited CLI gate with authenticated, execution-bound authorisation in a gateway independent of AgentScope.

## Consequences
The initial system is intentionally less autonomous. Tool discovery cannot trigger execution. The CLI confirmation is not sufficient for production security; do not make the lab-scanning command remotely callable without redesign.

## Revisit when
Adding remote users, write-capable tools, arbitrary MCP providers, scheduled scans or cloud credentials.
