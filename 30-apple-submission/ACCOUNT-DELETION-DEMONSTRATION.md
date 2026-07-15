# Account Deletion Demonstration

Status: **BLOCKED - account creation exists; no in-app deletion flow or route was found**

## Required user outcome

A user must be able to find and initiate deletion from AgentKip without emailing,
calling, or searching support documentation. The flow must offer deletion of the
entire AgentKip account and associated personal data, subject only to disclosed
legal retention. Deactivation or disconnect alone is insufficient.

Deleting an AgentKip account must clearly distinguish:

- AgentKip-controlled account, consent, entitlement, and service records that
  will be deleted or retained for a stated reason.
- Credentials or tokens that AgentKip or Noggin will revoke or erase.
- Self-hosted Noggin data and logs requiring a separate, clearly linked action.
- GitHub repositories, apps, phones, devices, provider accounts, and other
  external resources that remain controlled by the user and are not deleted.
- Apple subscriptions or purchases, if enabled, and their separate management.

## Demonstration script

1. Start from a fresh install and create a seeded review account.
2. Accept the current legal versions and create representative, non-personal
   records: consent receipt, conversation, provider choice, integration, and
   diagnostic submission.
3. Open **Settings > Legal & Privacy > Delete Account**.
4. Verify the screen identifies what will be deleted, what will remain, expected
   timing, subscription impact, and how completion will be communicated.
5. Reauthenticate if required and confirm the destructive action.
6. Capture the returned deletion request/status identifier without exposing a
   secret or raw personal identifier.
7. Verify the user is signed out and cannot continue using a deleted session.
8. Verify deletion or documented retention in every AgentKip-controlled store.
9. Verify linked tokens are revoked and provider/integration access is removed.
10. Verify external repositories/devices are unchanged unless the user separately
    requested an action supported by that external service.
11. Verify the user receives an accurate completion or partial-completion status.
12. Attempt login again and confirm the result matches the documented lifecycle.

## Evidence record

| Evidence | Required artifact |
|---|---|
| Discoverability | Screen recording from signed-in Settings |
| Intentional confirmation | Screenshots and UI test |
| API behavior | Redacted request/response and integration test |
| Store deletion | Before/after queries for each production-equivalent store |
| Token revocation | Provider-specific redacted verification |
| Retained records | Field, legal/business reason, access, and purge date |
| Completion | User-visible status and notification |
| External-data boundary | Test proving repository/device/provider data is not implied deleted |

## Failure cases

- Offline or unavailable backend: retain a visible pending state; do not claim
  completion.
- Partial provider failure: show partial status, retry safely, and identify the
  remaining system without exposing credentials.
- Already-deleted account: return an idempotent result that reveals no additional
  personal data.
- Active subscription: explain billing management while preserving an immediate
  account-deletion option where required.
- Sign in with Apple: if used, verify token revocation and credential lifecycle.

## Release blockers

1. No deletion UI/route was found.
2. The authoritative inventory of AgentKip-controlled stores is incomplete.
3. Retention exceptions and deletion service levels are not approved.
4. Revocation behavior for each authentication/integration provider is not proven.
5. Partial-failure and completion-notification behavior is not implemented.

Source: [Offering account deletion in your app](https://developer.apple.com/support/offering-account-deletion-in-your-app)
