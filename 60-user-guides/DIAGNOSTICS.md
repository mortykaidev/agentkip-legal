# Diagnostics and Support Reports

Status: **BLOCKED - current defaults do not match this intended user control**

Diagnostics can reveal more than an error message. Device identifiers, device
name, OS/app/build versions, locale, time zone, capability flags, product events,
repository names, prompts, file paths, logs, or content may identify you or expose
private work.

## Intended release behavior

- Diagnostic and device-context transmission is off by default.
- A report is sent only when you explicitly submit it or enable a clear,
  revocable diagnostic opt-in.
- Before submission, AgentKip shows the exact encoded payload, destination,
  purpose, and whether content is included.
- Content capture and upload remain off unless you deliberately select specific
  content for that report.
- You can remove optional fields, cancel before sending, clear local diagnostic
  history, and revoke ongoing diagnostic consent.
- The report never includes passwords, API keys, full tokens, recovery keys, or
  unrelated repository/file content.

## Before you send

1. Read every field in the preview.
2. Remove names, repository paths, issue text, prompts, or device details that are
   unnecessary for the problem.
3. Never paste credentials or secret values into the description.
4. Confirm the displayed destination is `hello@agentkip.ai` or another verified
   AgentKip support endpoint.
5. Save your own non-sensitive copy if you need a record.

## Current release blocker

The audited build currently has flight-recorder metadata enabled by default, may
auto-upload metadata segments when a gateway is configured, and has device
context enabled by default. Current metadata events can include
software-redacted snippets of up to 80 characters from prompts and replies;
because the app marks them as metadata, those snippets may upload
automatically. Redaction may not catch every sensitive value. Device context can
include a stable identifier, raw hardware identifier, device name, OS/app/build,
capabilities, locale, and time zone. Full-content capture and content-segment
upload default off, but that setting does not exclude the current snippets.

That current behavior must be changed and tested before this guide or a
user-triggered-only diagnostics promise is published.

## Verification required before publication

- Fresh install sends no diagnostic or device-context payload before user action.
- Preview bytes exactly match transmitted bytes.
- Opt-out stops future transmission on client and server.
- Local clear and server deletion/retention behavior are accurate.
- Offline, retry, cancellation, and partial failure do not send hidden payloads.
- The Privacy Policy, App Privacy answers, privacy manifest, and retention
  schedule match the verified behavior.
