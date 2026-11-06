# ADR 0004: Separate tool inventory, connectivity and authorisation

- Date: 2026-11-06
- Status: Accepted
- Delivery maturity: Local catalogue only
- Phase: 0–1
- Supersedes: none

## Context
MCP capabilities can be discovered dynamically, but existence of a tool does not establish permission to run it. Self-installation also creates a supply-chain boundary.

## Decision
Maintain separate responsibilities: **catalogue** describes versioned capabilities; **MCP broker** connects only to reviewed servers; **policy gateway** checks actor, capability, resource, scope and approval; **runner** executes limited operations. Never infer authority from tool discovery.

## Alternatives considered
| Option | Benefit | Risk |
|---|---|---|
| Registry + broker + policy | Explicit trust boundaries | More plumbing |
| Direct agent-to-MCP | Quick development | Confused deputy and tool privilege expansion |
| ToolHive as sole security solution | Operational convenience | Insufficient until concrete policy guarantees are verified |

## Consequences
A typed manifest needs identity, schema, digest, data sensitivity, network requirements, versions and audit fields. No unreviewed auto-installation. Decide whether ToolHive is warranted through a small connector comparison.

## Verification and falsification
Unknown tool, wrong scope, schema mutation, untrusted MCP server and inactive version must fail closed. A tool returned by discovery cannot be executed without a separate policy decision.

## Revisit triggers
Multi-user deployment, remote MCP transport, tool registry scaling and operational evidence.
