# Legal Changelog

This is the human review record. The machine version/hash/source-commit record lives in
`DOCUMENTATION-MANIFEST.yaml`. Add one entry per approved batch; do not rewrite past entries.

## 2026-07-15 — Draft baseline package

- **Status:** Draft; not published
- **Material change:** Yes — establishes the initial legal, privacy, AI, authorization, and user
  responsibility baseline.
- **Documents:** All manifest entries at `2026.07.15-draft.1`.
- **Acceptance impact:** Planned fresh acceptance for Terms/AUP, separate privacy acknowledgment,
  provider-specific AI consent, target authority attestations, Auto Apply acknowledgment, and
  per-action confirmations.
- **Code impact:** Identifies unresolved diagnostics/device defaults, prompt-only approval modes,
  generic approval event parsing, GitHub scopes, legal-gate absence, account deletion, and privacy
  manifests.
- **Review:** Two independent adversarial lanes completed; drafting findings were resolved and
  technical/production-evidence blockers remain open.
- **Publication:** None. All 40 source hashes are recorded; publication commits remain
  `UNPUBLISHED` pending product evidence and Brandon approval.
- **Approver:** Pending Brandon approval.

## Entry template

```text
## YYYY-MM-DD — Short change name

- Status:
- Material change: Yes/No and why
- Documents and old/new versions:
- Plain-language changes:
- Acceptance or re-consent impact:
- Product/operational dependencies:
- Publication routes and commit:
- Approver and approval record:
- Rollback/supersession note:
```

Versioning rules:

- Use a new version whenever user-visible meaning, rights, duties, recipients, purposes, retention,
  authorization, liability, or dispute terms change.
- Mark `material_change: true` when a reasonable user's decision or expectations could change.
- Typographic corrections may retain acceptance only when they do not change meaning; still update
  the hash and changelog.
- Never edit a published version in place. Supersede it, retain the accepted artifact, and update
  the publication commit.
