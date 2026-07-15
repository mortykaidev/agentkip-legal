# AgentKip Legal and Compliance

Private source of truth for AgentKip legal copy, privacy disclosures, AI-safety notices,
in-product consent language, Apple submission material, and operational compliance evidence.

This repository contains an internally reviewed indie-launch baseline. It is not represented as
attorney-reviewed, certified, or guaranteed to satisfy every law in every jurisdiction.

## Package map

- `00-control/` — facts, versions, evidence, placement, changes, and release blockers
- `10-public-legal/` — canonical public policies and notices
- `20-in-app-copy/` — versioned assent, consent, authority, and action-confirmation copy
- `30-apple-submission/` — App Store privacy, rating, review, deletion, and export worksheets
- `40-internal-compliance/` — data-flow, retention, provider, deletion, consent, and incident records
- `50-regional/` — inactive regional supplements and activation gates
- `60-user-guides/` — operational guidance for backups, permissions, self-hosting, and recovery
- `90-future-review/` — triggers and questions for optional future professional review

## Publication rule

Canonical sources are versioned in `00-control/DOCUMENTATION-MANIFEST.yaml`. Website and app
copies are generated exports: do not edit them independently. A document may be published only
when its hash, evidence, placement, approval, and applicable release gates all pass validation.

No residential address, secret, credential, raw user content, or personal diagnostic log belongs
in this repository.
