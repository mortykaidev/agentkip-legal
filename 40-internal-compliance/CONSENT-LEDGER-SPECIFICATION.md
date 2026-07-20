# Consent Ledger Specification

Status: **Approved interface baseline; storage and implementation BLOCKED**

## Purpose

The consent ledger proves what a user saw and decided without storing prompts,
repository content, diagnostics, credentials, or other unrelated personal data.
It supports display, export, revocation, re-consent, deletion, and release audits.

## Record types

### Legal acceptance receipt

- Receipt ID and account-scoped subject identifier.
- Event: accepted, declined, revoked, superseded, or migrated.
- Terms, Acceptable Use, and incorporated AI-notice identifiers, versions,
  effective dates, public URLs, locales, and SHA-256 hashes of the exact
  displayed documents.
- Terms/Acceptable Use agreement decision and the AI notice state recorded as
  `presentedIncorporated`, never as provider-transfer consent.
- Privacy Policy acknowledgment decision, labeled as acknowledgment rather than
  consent to all processing.
- Neutral 18+ attestation.
- Client app version/build and receipt-schema version.
- UTC server timestamp and client timestamp with trust/source indicator.

### AI-provider consent receipt

- Provider identifier and disclosure version.
- Categories of data disclosed to the user.
- Purpose, provider policy URL, routing boundary, and material retention/data-use
  summary shown at the time.
- Decision: allowed, denied, or revoked.
- Scope: account, provider, model/configuration, and optional target integration.
- UTC timestamp, app version/build, and disclosure hash.

### Authorization and risk acknowledgment

- Permission mode: read only, ask first, or auto apply.
- Target type and stable target reference, without credentials.
- Capabilities granted and prohibited.
- Recipient/provider, disclosed data categories, purpose, relevant policy URL,
  and a distinct data-transfer permission decision or verified no-transfer state.
- Auto-apply risk acknowledgment version and decision.
- Material permission changes, revocation, and reconnect events.
- Link to a separate action authorization receipt where a consequential action is
  individually approved.

## Shared interface contracts

These contracts are language-neutral. Consumer repositories may use native
types, but field meaning, enum values, identifiers, and fail-closed behavior must
remain compatible. Unknown required enum values or missing required fields do
not grant acceptance, consent, or authority.

### `LegalDocumentVersion`

- `identifier`: stable manifest document ID.
- `version`: stable document version.
- `effectiveDate`: ISO 8601 calendar date.
- `url`: canonical HTTPS URL when public; otherwise absent.
- `sha256`: lowercase SHA-256 of the exact canonical bytes.
- `locale`: BCP 47 locale of the displayed copy.
- `materialChange`: Boolean controlling re-acceptance review.

### `ConsentReceipt`

- `receiptId`, account-scoped `subjectId`, `schemaVersion`, and `event`.
- Accepted `LegalDocumentVersion` values for Terms and Acceptable Use, plus the
  AI-notice `LegalDocumentVersion` with state `presentedIncorporated`.
- `ageAttestation`, separate `privacyAcknowledgment`, and provider consent
  decisions; absence is not acceptance.
- UTC server timestamp, client timestamp plus trust indicator, locale, and app
  version/build.
- Integrity/delivery status and superseded/revoked receipt references.

### `AIProviderDisclosure`

- Stable provider identifier and legal/display names.
- Specific transmitted data-category identifiers.
- Specific purpose identifier and user-readable purpose.
- Canonical provider privacy-policy URL and verified policy/version metadata.
- Consent/disclosure version and SHA-256 hash.
- Material retention, training/data-use, routing, and refusal-effect summary.

### `AuthorizationScope`

- Stable target type and canonical target identifier.
- Granted and prohibited capability identifiers.
- Approval mode: `readOnly`, `askFirst`, or `autoApply`.
- Repository/branch/resource boundary and expiry where applicable.
- Recipient, disclosed data categories, purpose, and transfer-permission receipt
  when personal information leaves the controlled boundary.
- Revocation state: `active`, `revoked`, `expired`, or `unknown`; `unknown`
  grants no capability.

### `ActionAuthorizationRequest`

- Unique action ID and immutable request/preview hash.
- Exact target/account, requested capability, and effects.
- Risk tier/reasons, external side effects, and cost representation.
- Checkpoint/backup reference and reversibility/manual-recovery description.
- Permission mode, required legal-copy version, expiry, and transport-integrity
  state.

### `ActionAuthorizationReceipt`

- The complete `ActionAuthorizationRequest` or immutable reference and hash.
- Exact displayed preview/hash and user decision: `approved`, `denied`,
  `canceled`, or `expired`.
- Permission mode, decision timestamp, delivery/match status, and governing
  Terms/AUP versions.
- Result: `notRun`, `completed`, `partiallyCompleted`, `failed`, or `unknown`.
- Safe result summary, verification state, and rollback reference; no raw secret
  or unnecessary User Content.

### `AccountDeletionStatus`

- Stable request ID and account-scoped subject identifier.
- State: `requested`, `pending`, `completed`, `partiallyCompleted`, or `failed`.
- Requested/completed timestamps and per-controlled-store outcome.
- Retained-data categories with purpose/legal explanation and planned deletion
  or review date where applicable.
- Integration revocation outcomes and explicit independently controlled systems
  excluded from the deletion request.

## Integrity and privacy requirements

- Generate immutable, unique receipts; corrections create a new event rather
  than silently rewriting history.
- Hash the canonical source shown to the user and verify it at acceptance time.
- Use server-assigned time when online; mark queued/offline events and reconcile
  them without fabricating chronology.
- Encrypt in transit and at rest, restrict access, and audit administrative reads.
- Never store raw credentials, prompts, repository contents, device hardware IDs,
  or diagnostic payloads in a consent receipt.
- Make records idempotent across retries and resistant to replay.
- Store only the minimum identity needed to associate the receipt with the user's
  account and honor export/deletion requests.
- Do not use consent as a blanket legal basis for unrelated processing.

## Lifecycle

1. Fetch the current signed/hashed document registry.
2. Block gated product paths when a required material version is absent.
3. Display complete documents through readable, retainable links; checkboxes
   remain unchecked.
4. Write a receipt only after the explicit decision.
5. Confirm persistence before granting gated capabilities; otherwise fail closed.
6. Display the receipt in Legal & Privacy and include it in account export.
7. On material document/provider/permission change, retain the historical event
   and request a new decision.
8. On revocation, prevent new covered processing while preserving only the
   minimal approved evidence required by the retention decision.
9. On account deletion, delete or minimize the receipt according to the approved
   retention rule and return an accurate retained-data status.

## Version and material-change rules

Material changes include new data categories or recipients, broader AI-provider
use, new autonomous capabilities, weaker user controls, new paid obligations,
new liability/indemnity terms, or a changed dispute forum. Formatting, typo, or
non-substantive clarity edits may keep acceptance valid only when documented as
non-material in the legal changelog.

## Required tests

- Fresh install and every signup/invite/pair/deep-link route is gated.
- Decline does not produce an acceptance receipt or grant capability.
- Receipt hash matches the exact canonical content.
- Offline/retry creates one correctly ordered event.
- Material version causes re-consent without deleting user data.
- Provider transfer does not occur before provider-specific consent.
- Revocation immediately blocks new covered transfers/actions.
- Export is readable and deletion returns accurate status.
- Tampering, unknown version, unavailable registry, or persistence failure fails
  closed.

## Release blockers

1. Authoritative store, API, migration, and access model are not implemented.
2. Retention/deletion treatment is not approved.
3. Offline behavior and server-time trust are not implemented.
4. The app does not yet enforce acceptance on every entry path.
5. Provider-specific consent is not yet proven before transfer.
