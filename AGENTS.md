# AgentKip Legal Repository Rules

This private repository is the authoritative source for AgentKip legal, privacy, AI-safety,
compliance, in-app consent, and App Store submission documentation.

## Safety

- Keep the repository private. Never publish internal compliance records or source-ledger notes.
- Never commit residential addresses, secrets, credentials, raw user content, or personal logs.
- Public claims must be supported by `00-control/CLAIM-TO-CODE-MATRIX.md`.
- Generated exports are never edited independently of their canonical source documents.
- Do not state or imply that these documents were reviewed by an attorney.
- Do not activate regional supplements until their release gates are satisfied.

## Workflow

- Work on `codex/*` or `claude/*` branches and use pull requests; never push directly to `main`.
- Re-run link, manifest, hash, placeholder, and sensitive-data checks before every merge.
- Record material document changes in `00-control/LEGAL-CHANGELOG.md`.
- Brandon retains publication and merge authority.

