# AI Provider Consent Copy

**Copy version:** 2026.07.15-draft.1

**Effective:** July 15, 2026

**Region:** United States

**Receipt event:** `ai_provider_consent_decided`

This is a just-in-time, provider-specific permission. Bracketed fields must be replaced with verified
values before presentation.

## First-use consent sheet

**Navigation title:** AI provider permission

**Heading:** Send selected data to [PROVIDER_NAME]?

**Provider:** [PROVIDER_LEGAL_NAME]

**Feature:** [FEATURE_NAME]

**Data sent:**

> [SPECIFIC_DATA_CATEGORIES]

Use concrete categories—for example: “your prompt, the selected repository files and filenames,
conversation context, tool results, and device locale.” Never substitute “necessary data” or “some
information.”

**Purpose:**

> [SPECIFIC_PURPOSE]

**Provider handling:**

> [PROVIDER_NAME] processes this information under its terms, privacy policy, account tier, and
> settings. [VERIFIED_RETENTION_AND_TRAINING_SUMMARY]

**Links:**

- `Provider privacy information` → `[PROVIDER_PRIVACY_URL]`
- `AgentKip Privacy Policy` → `[PRIVACY_URL]`

**Consent checkbox, unchecked by default:**

> I allow AgentKip to send the data listed above to [PROVIDER_NAME] for [SHORT_PURPOSE].

**Primary button:** Allow [PROVIDER_NAME]

**Secondary button:** Don’t allow

**Decline explanation:**

> If you don’t allow this, [FEATURE_NAME] will not use [PROVIDER_NAME]. Other AgentKip features that
> do not require this transfer will remain available.

## Interaction rules

- Present this before the first transfer, not after a request has already been sent.
- Consent to one provider does not cover another provider.
- Consent to one category or purpose does not cover a materially broader category or purpose.
- Do not make refusal cancel the user’s account or block unrelated functionality.
- Keep the provider name and data categories visible without opening another page.
- Re-consent when the provider, material category, purpose, training/retention representation, or
  recipient role changes.
- Revocation prevents future transfers through AgentKip; it does not delete data already controlled
  by the provider. Link to the provider’s deletion controls where available.

## Scope-expansion copy

**Heading:** [PROVIDER_NAME] needs additional data

> You previously allowed [PREVIOUS_CATEGORIES]. To use [FEATURE_NAME], AgentKip would also send
> [NEW_CATEGORIES] for [NEW_PURPOSE]. Review the updated provider information before deciding.

**Checkbox:** I allow this additional transfer.

**Primary button:** Allow additional data

**Secondary button:** Keep current permission

## Errors

**Disclosure incomplete:**

> AgentKip can’t verify the provider, data categories, or purpose, so nothing was sent.

**Receipt failure:**

> Your choice could not be recorded. Nothing was sent. Try again.

## Receipt requirements

Record account identifier, event/action ID, provider legal name and identifier, feature, exact data-
category identifiers, purpose identifier, provider-policy URL/version where available, disclosure
version/hash, decision, locale, and timestamp. Do not copy the prompt or User Content into the
consent receipt.
