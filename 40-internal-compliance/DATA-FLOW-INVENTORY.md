# Data-Flow Inventory

Status: **BLOCKED - production trace and store inventory incomplete**

Snapshot date: 2026-07-15

## System boundary

AgentKip spans more than the iOS binary. The audited boundary includes:

1. AgentKip and any distributed Apple-platform extensions or companion apps.
2. The AgentKip website and its authentication, database, billing, and hosting.
3. The user's self-hosted Noggin service.
4. User-selected AI providers and integrations.
5. GitHub and any repositories or organizations authorized by the user.
6. Apple services used by the distributed build.
7. Support, diagnostics, and incident-handling systems.

## Known and candidate flows

| Flow | Data classes | From -> to | Trigger/default | Current evidence status |
|---|---|---|---|---|
| Account authentication | Account identifiers, contact information, session data | Website/app -> Clerk and AgentKip stores | Account creation/sign-in | Provider confirmed; exact fields and stores BLOCKED |
| Website operation | IP/server logs, auth cookies, theme preference, account/entitlement data | Browser -> Vercel, Clerk, Neon/Drizzle | Site visit/account use | Providers confirmed; field/retention trace BLOCKED |
| Billing | Account/entitlement and payment-related records | Website -> Stripe and AgentKip stores | Billing flow if enabled | Integration exists; launch state and accessible fields BLOCKED |
| Conversation request | Prompt, selected context, attachments, account/session identifiers | AgentKip -> self-hosted Noggin | User request | Content/path/retention trace BLOCKED |
| AI inference | Prompt and selected context, provider credentials/metadata | Noggin or client -> user-selected AI provider | Provider-specific request | Provider list, routing, and provider terms BLOCKED |
| GitHub access | Installation/repository IDs, metadata, files, diffs, issues/PRs, credentials | AgentKip/Noggin <-> GitHub | User connects and requests action | Scope/action trace BLOCKED |
| Device context | Stable ID, raw hardware ID, device name, OS/app/build, capabilities, locale, time zone | AgentKip -> configured gateway | Currently defaults on | Known current behavior; minimization/consent BLOCKED |
| Flight-recorder metadata | Product interaction/performance/diagnostic metadata, including software-redacted prompt/reply snippets of up to 80 characters | AgentKip -> configured gateway | Recording defaults on; segments may auto-upload | Snippets are currently marked as metadata; redaction is not guaranteed; removal or explicit content opt-in, payload proof, and retention BLOCKED |
| Flight-recorder content | Potential conversation or content payload beyond the snippets carried in metadata | AgentKip -> configured gateway | Full-content capture/content-segment upload currently default off | Must remain off absent explicit user action; runtime proof BLOCKED |
| User-triggered support | User-entered report, selected diagnostics, contact details | App/site -> support destination | Intended affirmative submission | Exact preview/payload/destination BLOCKED |
| Apple platform services | Push, speech/audio, photos/files, purchases, crash/analytics data as enabled | Device/app <-> Apple | Permission or platform configuration | Exact services/configuration BLOCKED |
| Consent records | Document versions/hashes, decisions, time, locale, account identifier | AgentKip -> authoritative consent store | Legal/provider acceptance | Interface approved; storage not implemented/evidenced |
| Account deletion | Account ID, status, retained-record reasons, revocation results | AgentKip -> all controlled stores/providers | User request | No UI/route found; BLOCKED |

## Data-flow rules approved for implementation

- Legal acceptance does not itself authorize an AI-provider transfer.
- Provider consent must identify the provider, data categories, purpose, and
  policy before personal data is sent.
- Diagnostics and device-context transmission must be default-off and either
  user-triggered or covered by a clear, revocable opt-in.
- Permission modes must be enforced in capability code and Noggin, not merely in
  model prompts.
- Unknown destination, provider, permission, risk, or approval state fails closed.
- Credentials must be transmitted only where necessary for the authorized
  integration and must never enter logs or this repository.

## Evidence required for each flow

- Exact fields and classification.
- Purpose and lawful/business basis.
- User control, default, and trigger.
- Transport, encryption, and credential boundary.
- Controller/processor/independent-controller role.
- Storage location, access, retention, deletion, and backup behavior.
- Recipient/provider contract and data-use settings.
- Release-build traffic trace and matching server/store evidence.
- Public notice, App Privacy, privacy-manifest, and consent mapping.

## Release blockers

1. No complete runtime traffic capture exists for a production-equivalent build.
2. Metadata/device-context defaults conflict with the intended privacy posture.
3. AI-provider and Apple-service paths are not fully enumerated.
4. Store, log, backup, and deletion coverage is incomplete.
5. Provider roles, locations, subprocessors, and contract controls are unresolved.
