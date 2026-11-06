# ADR 0008: Keep interaction local-first and bound external data and spend

- Date: 2026-11-06
- Status: Accepted
- Delivery maturity: Partial scaffold
- Phase: 0–1, 3
- Supersedes: none

## Context
A voice-enabled assistant handling security context can leak confidential content via provider calls and create uncontrolled recurring inference charges.

## Decision
Use a local CLI and optional local Whisper transcription initially. Explicitly classify data before model egress; use dedicated credentials and both provider-side hard spending caps and local per-task preflight budgets. No unattended workflows until those controls are tested.

## Alternatives considered
| Option | Benefit | Risk |
|---|---|---|
| Local STT + remote model | Fast MVP, local audio processing | Transcript leaves device |
| Fully local models | Stronger data locality | Quality, resource and model management cost |
| Hosted end-to-end voice | Easy UX | Larger privacy/trust boundary |

## Consequences
Voice recording and transcript handling must be disclosed. A local transcription engine does not guarantee local inference. Missing or exhausted budget must stop the run rather than silently switch providers.

## Verification and falsification
Test no unintended audio upload, outbound prompt classification, preflight budget rejection and concurrent requests under the same cap.

## Revisit triggers
Corporate data use, always-listening UX, distributed scheduling and provider changes.
