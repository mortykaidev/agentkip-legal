# Connected Target Authority Attestation Copy

**Copy version:** 2026.07.15-draft.1

**Effective:** July 15, 2026

**Region:** United States

**Receipt event:** `target_authority_attested`

Use this copy before connecting a repository, organization, account, app, phone, device, server,
deployment, gateway, dataset, or third-party service.

## Connection sheet

**Navigation title:** Confirm your authority

**Heading:** You’re connecting [TARGET_DISPLAY_NAME]

**Target:** [TARGET_TYPE] · [TARGET_CANONICAL_IDENTIFIER]

**Owner/account:** [OWNER_OR_ACCOUNT]

**Requested access:** [SPECIFIC_CAPABILITIES]

**Requested scope:** [REPOSITORIES_DEVICES_OR_RESOURCES]

**Recipient/service:** [RECIPIENT_LEGAL_NAME]

**Information shared:** [SPECIFIC_DATA_CATEGORIES_OR_NONE]

**Purpose:** [SPECIFIC_TRANSFER_PURPOSE_OR_NONE]

**Privacy information:** [RECIPIENT_PRIVACY_URL]

**Body:**

> Connect this target only if you own it or have clear permission from its owner or responsible
> organization. Technical access, a shared link, a public repository, an invitation, or a credential
> does not by itself grant authority. Your employer, customer, repository owner, or provider may set
> narrower limits.

**Authority checkbox, unchecked by default:**

> I confirm that I own or am authorized to access and direct AgentKip to use this exact target within
> the access and scope shown above.

**Responsibility checkbox, unchecked by default:**

> I will follow applicable law, contracts, workplace policies, licenses, and provider terms; use the
> least access needed; and revoke access when it is no longer needed.

**Data-transfer permission checkbox, unchecked when personal information will be shared:**

> I allow AgentKip to send the information listed above to [RECIPIENT_LEGAL_NAME] for
> [SPECIFIC_TRANSFER_PURPOSE]. I understand that the recipient handles that information under its
> own terms and privacy practices.

Do not show the data-transfer checkbox when the verified connection transfers no personal
information. Provider-specific AI consent remains a separate screen and cannot be replaced by this
connection permission.

**Primary button:** Confirm and connect

**Secondary button:** Cancel

**Footer:**

> This confirmation records your representation of authority. It does not create authority you do
> not already have, and it does not excuse AgentKip from staying within the scope shown.

## Scope expansion sheet

**Heading:** Approve broader access?

> [TARGET_DISPLAY_NAME] is currently authorized for [CURRENT_SCOPE]. The requested feature would add
> [NEW_CAPABILITIES_OR_SCOPE]. Confirm that you have authority for the additional access.

**Recipient/service:** [RECIPIENT_LEGAL_NAME]

**New or changed information shared:** [NEW_OR_CHANGED_DATA_CATEGORIES_OR_NONE]

**New or changed purpose:** [NEW_OR_CHANGED_TRANSFER_PURPOSE_OR_NONE]

**Privacy information:** [RECIPIENT_PRIVACY_URL]

**Checkbox:** I confirm my authority for this additional access.

**Transfer checkbox, unchecked when the recipient, data categories, or purpose changes:** I allow
AgentKip to make the new or changed transfer described above.

**Primary button:** Approve broader access

**Secondary button:** Keep current access

If the scope expansion changes no recipient, personal-data category, or purpose, show the verified
no-transfer-change state instead of a transfer checkbox. Any AI-provider change still uses the
separate AI-provider consent screen.

## Integrity and error copy

**Target changed:**

> The target or requested scope changed while you were reviewing it. Nothing was connected. Review
> the current target and scope.

**Target unknown:**

> AgentKip can’t verify the target, owner, or requested access, so it will not connect.

**Receipt failure:**

> Your authority confirmation could not be recorded. Nothing was connected.

## Receipt requirements

Record account identifier, connection/action ID, target type and canonical identifier, owner/account
identifier, exact capability and resource scopes, recipient/provider identifier, disclosed data-
category and purpose identifiers, recipient-policy URL/version when available, authority decision,
data-transfer decision or verified no-transfer state, displayed-copy version/hash, locale, and
timestamp. Never store a secret, credential value, or transferred content in the receipt.
