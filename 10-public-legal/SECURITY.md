# AgentKip Security

**Updated:** July 15, 2026

**Version:** 2026.07.15-draft.1

**Service status:** United States adult beta

AgentKip connects an iPhone to systems and AI providers that can inspect information and take
actions. Security depends on the AgentKip app, Hayward-operated services, your configured gateway
and self-hosted Noggin environment, your providers, your devices, and the choices you make. No
single control makes that chain perfectly secure.

## Security model

AgentKip follows these security principles for the public-release baseline:

- **Minimum scope:** integrations should request only the repositories and capabilities needed.
- **Explicit authority:** you must attest that you own or are authorized to control a target.
- **Layered approvals:** mutations receive a durable preview; consequential actions receive a
  separate confirmation; prohibited actions fail closed.
- **Credential separation:** supported GitHub tokens and credentials are stored in the iOS Keychain,
  not ordinary app preferences. Some connection flows copy a token from a configured host to the
  phone’s Keychain; both endpoints must be trusted and secured.
- **Local and self-hosted boundaries:** data may remain on your device or self-hosted environment,
  but information you direct to an AI provider or Connected System follows that service’s path.
- **Recovery evidence:** action receipts and checkpoints are intended to support investigation and
  rollback where the target operation is actually reversible.
- **Fail safely:** a mutation should not proceed when the target, provider, capability, effects,
  risk, or approval cannot be reliably identified.

The beta is still being hardened. A listed design principle must not be treated as proof that every
current route, provider, or tool implements it. Before relying on a control, verify what the app
actually displays and what the target system records.

## Current diagnostic and device context behavior

In the July 15, 2026 beta baseline, configuring a gateway enables automatic flight-recorder metadata
upload. Full-content capture and content-segment upload are off by default, but current metadata
events can include software-redacted snippets of up to 80 characters from prompts and replies. The
app marks those events as metadata, so it may upload the snippets automatically. Software redaction
of recognized secret patterns is not a guarantee that every sensitive value will be removed.
Device-context sharing is on by default and may include a stable device identifier, raw hardware
identifier, device name, hardware and capabilities, OS and app/build versions, locale, and time
zone. The automatic snippet path and these defaults are release blockers planned to be removed or
placed behind explicit user controls before public release. Until a verified build changes them,
treat this paragraph as the current behavior. See the [Privacy Policy](/privacy).

## What you should do

- Connect only a gateway, Noggin host, repository, account, and device you own or trust and are
  authorized to control.
- Keep iOS, AgentKip, your host, Noggin, dependencies, and provider software updated.
- Use strong authentication, protected branches, minimum permissions, provider budgets, and
  independent backups.
- Never paste passwords, tokens, private keys, recovery codes, or session cookies into prompts.
- Start in Read Only, test in a non-production target, inspect diffs and receipts, and verify results
  directly in the target system.
- Revoke installations and tokens, remove host copies, and rotate credentials when a connection is
  no longer needed or may have been exposed.
- Treat files, webpages, messages, issues, images, retrieved content, and tool output as possible
  prompt-injection sources.

## What AgentKip is not designed for

The beta is not designed for minors; protected health information; full payment-card data; Social
Security numbers; government identification; biometric templates; life-safety, emergency, weapons,
or critical-infrastructure control; or unsupervised production changes. It is not a compliance
certification, managed security service, penetration-testing authorization, or guaranteed secure
execution environment.

## Reporting a vulnerability

Email hello@agentkip.ai with the subject **“Security report.”** Include:

- the affected AgentKip version, component, and feature;
- clear reproduction steps and expected versus observed behavior;
- the security impact and whether the issue is still active; and
- a safe proof of concept with secrets and personal information removed.

Do not access another person’s data, degrade service, run destructive tests, persist after proving
the issue, publish a live exploit, or demand payment. We do not promise a bug bounty. We will
acknowledge and investigate good-faith reports as resources permit and coordinate disclosure where
appropriate.

For an active account or credential compromise, stop pending actions, disconnect affected
integrations, rotate credentials through the relevant provider, preserve non-sensitive evidence,
and contact the provider or system owner as well as us.

## Security and privacy questions

Hayward Imagination Company LLC

Michigan, United States

hello@agentkip.ai
