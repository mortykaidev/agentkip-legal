# Independent Adversarial Review — 2026-07-15

Review status: **Passed for a blocked internal draft; not approved for publication, TestFlight, or
App Store submission**

This record summarizes two independent read-only AI review lanes plus the final targeted reread.
It is an internal product/compliance review, not attorney, lawyer, or counsel review.

## Scope reviewed

- All public legal documents and in-app assent, consent, authority, and action copy.
- Facts/decisions, claim-to-code evidence, manifest acceptance semantics, placement, provider and
  retention records, shared interfaces, Apple worksheets, and release blockers.
- Responsibility allocation, non-waivable carveouts, AI/provider consent, processor boundaries,
  age/account-deletion claims, diagnostics, approval failure states, and export/link behavior.

## Material findings resolved in the draft

- Replaced passive continued-use assent with explicit unchecked clickwrap and incorporated the AI
  notice without treating it as provider-transfer consent.
- Added separate provider-specific AI consent and recipient/data/purpose/policy permission for
  other connected-service transfers, including scope expansion.
- Prevented the User Content license and user instructions from bypassing required disclosures,
  provider consent, target authority, or action authorization.
- Distinguished Hayward-engaged service providers from user-selected or self-hosted systems and
  preserved Hayward's vendor-management, privacy, product, and non-waivable duties.
- Conditionalized unverified production processor/payment claims and added explicit publication
  gates for equal protection, contracts/configuration, retention, and no-ad/sale/tracking/training
  commitments.
- Disclosed default-on device context and automatic metadata uploads containing software-redacted
  prompt/reply snippets of up to 80 characters; added a dedicated P0 blocker.
- Clarified that the current build does not prove an age gate, account deletion, enforced permission
  modes, typed approvals, or blocked actions.
- Added consumer-protection/forum carveouts, deterministic approval-not-delivered versus
  execution-unknown states, the seven shared interfaces, and export-safe guide links.
- Aligned website-visitor privacy/provider scope separately from the United States adult product
  eligibility rule.

## Findings intentionally left open

The review did not close product or production-evidence blockers. Public drafts describe the
required release behavior, while `CLAIM-TO-CODE-MATRIX.md` and `RELEASE-BLOCKERS.md` show that the
current app/site/backend do not yet implement or prove it. In particular:

- assent/provider consent/target permission cannot yet be enforced or retained;
- Read Only, Ask First, Auto Apply, always-confirm, and blocked actions are not proven capabilities;
- account deletion and privacy manifests do not exist;
- diagnostics/device context and the 80-character snippet path violate the locked launch default;
- production providers, contracts, locations, exact fields, retention, and deletion are unverified;
- the site, App Store records, final binary, and backend have not consumed an approved export.

These are release blockers, not drafting defects. Draft or `UNPUBLISHED` status must remain until
implementation and evidence close the applicable gates.

## Verification evidence

At the final draft snapshot:

- all 40 controlled sources are manifest-covered, version/date matched, and SHA-256 locked;
- draft validation returns zero errors and zero warnings;
- 17 validator/export tests pass;
- release validation and approved export correctly fail closed because consumer artifacts remain
  `draft` with `UNPUBLISHED` publication commits;
- no residential address, unresolved editorial placeholder, New York governing-law clause,
  launch-under-13 language, secret pattern, or completed professional-review claim was found.

## Release-review requirement

After product and production-evidence changes, run a new independent review against the exact
commits and binary. Do not treat this report as approval of a later document version, consumer
export, website deployment, or app build. Brandon remains the publication and merge approver.
