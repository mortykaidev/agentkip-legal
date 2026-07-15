# Age and Terms Assent Copy

**Copy version:** 2026.07.15-draft.1

**Effective:** July 15, 2026

**Region:** United States

**Receipt event:** `legal_assent_accepted`

This file defines exact launch copy. Bracketed fields are runtime values and must never appear
unresolved in the app.

## Initial onboarding screen

**Navigation title:** Before you continue

**Heading:** AgentKip is an adult AI beta

**Body:**

> AgentKip can connect AI to repositories, apps, devices, accounts, and services you control. AI can
> be wrong, insecure, or destructive. Review important actions, use backups, and connect only systems
> you own or are authorized to manage.

**Age checkbox, unchecked by default:**

> I confirm that I am at least 18 years old and located in the United States.

**Agreement checkbox, unchecked by default:**

> I agree to the AgentKip Terms of Service (version [TERMS_VERSION]), including its incorporated AI
> Transparency and Safety Notice (version [AI_NOTICE_VERSION]), and the Acceptable Use and Agent
> Authorization Policy (version [AUP_VERSION]). This is not consent to send data to an AI provider.

**Links:**

- `Read Terms of Service` → `[TERMS_URL]`
- `Read Acceptable Use Policy` → `[AUP_URL]`
- `Read AI Transparency and Safety Notice` → `[AI_NOTICE_URL]`

**Primary button:** Agree and continue

**Secondary button:** Exit setup

**Footer:**

> The AgentKip iOS app is also licensed under Apple’s Standard EULA. Accepting these terms does not
> authorize access to a repository, device, account, or other system; you will confirm that authority
> when you connect each target.

## Interaction rules

- Do not pre-check either checkbox.
- Keep **Agree and continue** disabled until both boxes are checked and all three document links can
  be opened or a verified, hash-matching cached copy is available.
- Do not combine the Privacy Policy acknowledgment or AI-provider permission with this agreement.
- Exiting setup leaves the Service unavailable except for viewing legal/support information.
- Signup, invitation, pairing, restore, and deep-link routes must return here when current assent is
  missing.

## Material update screen

**Heading:** AgentKip’s terms have changed

**Body:**

> Please review and agree to the updated Terms of Service (version [TERMS_VERSION]) and Acceptable
> Use Policy (version [AUP_VERSION]), including the incorporated AI Transparency and Safety Notice
> (version [AI_NOTICE_VERSION]), before continuing. Your existing data will not be deleted if you
> choose not to agree, but affected AgentKip features will remain unavailable. This agreement is not
> consent to an AI-provider data transfer.

**Links:** Current Terms, Acceptable Use Policy, and AI Transparency and Safety Notice URLs from the
verified document registry.

**Agreement checkbox, unchecked:**

> I have reviewed and agree to these updated terms.

**Primary button:** Agree and continue

**Secondary button:** Not now

A material AI-notice change triggers this screen and a new acceptance receipt even if the parent
Terms text did not otherwise change. The receipt records the updated notice as
`presentedIncorporated`, not as provider consent.

## Error and integrity copy

**Documents unavailable:**

> We can’t verify the current legal documents. Check your connection and try again. AgentKip will not
> continue with an unknown or mismatched version.

**Receipt save failed:**

> Your agreement could not be recorded. Nothing was accepted. Try again before continuing.

**Version changed during review:**

> This document changed while you were reviewing it. Please review the current version before
> agreeing.

## Receipt requirements

Record the account identifier, event name, age attestation, region, locale, timestamp, Terms/AUP/AI
document identifiers, versions, URLs, SHA-256 hashes, displayed-copy version, and acceptance result.
Record the AI notice as presented and incorporated into the accepted Terms—not as AI-provider
consent. Never record User Content in this receipt. Make the receipt viewable and exportable in
Legal & Privacy settings.
