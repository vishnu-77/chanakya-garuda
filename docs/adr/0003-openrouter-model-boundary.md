# ADR 0003: Use OpenRouter for MVP model inference

- Date: 2026-11-06
- Status: Accepted for MVP
- Delivery maturity: Scaffold; live and spend limits unverified
- Phase: 0–1
- Supersedes: none

## Context
A hybrid assistant benefits from comparing models without binding the orchestration layer to one provider.

## Decision
Call OpenRouter through a replaceable model adapter. Use a dedicated key with a provider-side hard limit; add local task budgets, request ceilings, retries and usage reconciliation before unattended operation.

## Alternatives considered
| Option | Benefit | Drawback |
|---|---|---|
| OpenRouter | Multi-provider model catalogue | External routing, availability, privacy and pricing dependencies |
| Direct provider API | Potentially clearer single-provider controls | Vendor coupling |
| Local inference | Data locality and predictable API spend | Hardware and capability constraints |

## Consequences
Provider routing, data retention/processing requirements and model tool-call compatibility need explicit configuration. Do not send confidential corporate data or credentials by default. A hard provider cap is a prerequisite, not a property of the starter code.

## Verification and falsification
Integration test response schema, tool calling, error handling, failover and token accounting. Test concurrent budget exhaustion before background automation. Reconsider if cost, reliability, privacy or model quality miss thresholds.

## Revisit triggers
Data residency restrictions, provider routing changes, unacceptable cost or new local models.
