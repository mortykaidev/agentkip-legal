# Claim-to-Code Matrix

Audit date: **2026-07-15**

Evidence snapshots:

- iOS repository `mortykaidev/agentkip` at `abf2a399225e5c8b5811b911b8cfe8193dbd7445`
- Website repository `mortykaidev/agentkip-site` at `b9f8395551b16d9aab895282281b5028ffbe5af3`
- Noggin repository (`kai-core` checkout) at `99a877a411b47bced10c33cf35468b36710b801d`

Line numbers are audit aids, not durable identifiers. Re-run the cited search and update the commit
before approval. `Blocked` means the public claim is not currently safe; it does not mean the
feature can never ship.

## Current data and provider facts

| ID | Candidate claim or disclosure | Evidence | Status | Publication rule |
|---|---|---|---|---|
| `DATA-001` | Website authentication uses Clerk. | `agentkip-site/package.json:20`; `src/lib/auth.ts`; `src/lib/w1/auth.ts` | Supported | Disclose Clerk categories/purposes and cookies; do not claim the site sees no account data. |
| `DATA-002` | Website production storage can use Neon Postgres through Drizzle. | `agentkip-site/package.json:21,23`; `src/lib/store.ts:16-24`; `src/lib/w1/db.ts` | Supported | Disclose stored categories and retention only after the live schema/config is verified. |
| `DATA-003` | Billing code stores Clerk subjects plus Stripe customer, Checkout, subscription, event, and entitlement identifiers. | `agentkip-site/src/db/schema.ts:54-140`; `src/lib/w1/services.ts`; `src/app/api/stripe/webhook/route.ts` | Supported | Disclose Stripe/billing records whenever the flow is enabled. Code presence does not prove production billing is live. |
| `DATA-004` | Website theme preference is stored in browser local storage under `kip-theme`. | `agentkip-site/src/components/theme-toggle.ts:35`; `src/app/layout.tsx:97` | Supported | Include browser storage in the Privacy Policy/cookie-storage notice. |
| `DATA-005` | Website includes Vercel Blob and is designed for Vercel-hosted operation. | `agentkip-site/package.json:22`; `src/lib/store.ts:16-18`; `src/lib/actions.ts` | Partially supported | Disclose Vercel only after confirming the live production deployment and enabled services. |
| `DATA-006` | iOS flight-recorder metadata capture defaults on; metadata segments auto-upload after a gateway is configured. | `agentkip/AgentKip/Core/Persistence/AppSettingsStore.swift:905-938,1969`; `AgentKip/Core/FlightRecorder/FlightLogShipper.swift:140-149,235` | Supported; not policy-compliant | Release blocker until default/consent changes or the approved policy and App Privacy answers truthfully describe the behavior. |
| `DATA-007` | Full-content mode defaults off, but user messages and completed replies are software-redacted and truncated to as many as 80 characters, stored on events marked `containsContent: false`, and therefore may travel in metadata segments that auto-upload after a gateway is configured. | `agentkip/AgentKip/Core/Persistence/AppSettingsStore.swift:919-939,1970-1975`; `AgentKip/Features/Chat/ChatViewModel.swift:1914-1926,1937-1949,1962-1977`; `AgentKip/Core/FlightRecorder/FlightLogShipper.swift:140-149` | Supported; not policy-compliant | Do not describe content upload as wholly off. Remove this default snippet path or require explicit content consent, then prove the encoded payload and segment classification in tests. |
| `DATA-008` | Device-context sharing defaults on and can send a stable device ID, marketing model, raw hardware ID, OS/app/build, device name, capability flags, locale, and time zone to the configured gateway. | `agentkip/AgentKip/Core/Persistence/AppSettingsStore.swift:954-971,1977`; `AgentKip/Core/Models/KipDeviceContext.swift:22-57,118-149`; `AgentKip/Core/Services/KipDeviceRegistrar.swift:102-111` | Supported; not policy-compliant | Release blocker until default/consent changes or disclosure and App Privacy answers are reconciled. |
| `DATA-009` | “AgentKip never receives or can access app data” is not established. | Diagnostics/device transport above; website pages currently assert broad no-access/no-middle claims at `src/app/privacy/page.tsx:16-20,61-70` and `src/app/security/page.tsx:96-114,153-155` | Blocked | Replace absolutes with actor/data-path-specific statements backed by deployment evidence. |
| `DATA-010` | No ads, sale, cross-context tracking, or company model training. | Policy decision only; no complete runtime/vendor audit artifact yet | Unverified policy commitment | Do not publish until dependency, network, provider-contract, and production-configuration review is complete. |

## Authorization and agent-action facts

| ID | Candidate claim or disclosure | Evidence | Status | Publication rule |
|---|---|---|---|---|
| `AUTH-001` | `Read Only`, `Ask First`, and `Auto Apply` are enforced product capabilities. | `agentkip/AgentKip/Core/Persistence/AppSettingsStore.swift:516-540,1723-1726`; `AgentKip/Core/GitHub/GitHubClient.swift:80-92` injects the choice into prompt text | Blocked | Do not claim enforcement until iOS and Noggin tests prove server-side capability denial and fail-closed approval. |
| `AUTH-002` | Ask First is the default selection. | `agentkip/AgentKip/Core/Persistence/AppSettingsStore.swift` initializes `repoEditApproval` to `.askFirst` | Supported as a UI/default fact | Must be paired with the `AUTH-001` warning until enforcement ships. |
| `AUTH-003` | The phone presents and can resolve durable approval requests. | `agentkip/AgentKip/Core/NogginClient/NogginSSEParser.swift:252-253` downgrades `approval.request` to generic `toolStarted` | Blocked | Typed request, exact preview, approve/deny transport, timeout/mismatch behavior, and visible receipt are release gates. |
| `AUTH-004` | GitHub installation is least privilege. | `agentkip/AgentKip/Core/GitHub/GitHubAppSetup.swift:80-85` requests contents, pull requests, and issues write by default | Blocked | Minimize repositories/scopes or disclose each required permission and require explicit reconnect for expansion. |
| `AUTH-005` | Noggin already contains approval and filesystem-checkpoint primitives that should be extended. | `kai-core/tools/approval.py`; `acp_adapter/edit_approval.py`; `acp_adapter/permissions.py`; `tools/checkpoint_manager.py` | Supported internal architecture fact | Reuse the existing pipeline; do not represent it as an end-to-end iOS safety control until integration tests pass. |
| `AUTH-006` | Checkpoint rollback makes every action reversible. | `kai-core/tools/checkpoint_manager.py` covers filesystem checkpoints; external services and destructive actions are not inherently reversible | Blocked | Display action-specific reversibility and external side effects; never make a universal rollback claim. |

## App Store and user-control facts

| ID | Candidate claim or disclosure | Evidence | Status | Publication rule |
|---|---|---|---|---|
| `APP-001` | Every distributed Apple bundle has an accurate privacy manifest. | Audit command `rg --files -g 'PrivacyInfo.xcprivacy'` returned no file in the iOS snapshot | Blocked | Inventory required-reason APIs/SDK manifests and embed the correct file in each distributed bundle before submission. |
| `APP-002` | Fresh install, signup, invitation, pairing, and deep-link entry cannot bypass current legal acceptance. | No versioned legal gate or receipt model found in `AgentKip/Features/Onboarding` or connection entry points at the audited commit | Blocked | Add and test a single fail-closed acceptance coordinator used by every entry path. |
| `APP-003` | Settings provides Legal & Privacy, consent history, provider controls, export, disconnect, and account deletion. | No matching legal center or account-deletion implementation found at the audited commit | Blocked | Build and exercise the surfaces; distinguish account deletion from disconnect and self-hosted/third-party deletion. |
| `APP-004` | Users can delete an AgentKip-created account in the app. | Website has `src/app/account/page.tsx`; no verified iOS deletion flow or complete deletion API/receipt was found | Blocked if account creation ships | Implement end-to-end deletion and App Review demonstration, or remove account creation from the submitted experience. |
| `APP-005` | Privacy/App Store disclosures match all shipped data flows. | `30-apple-submission` worksheets and bundle manifests are not yet approved | Blocked | Reconcile after final binary/SDK inspection, then record the build and submission answers. |

## Existing public-page contradictions

| ID | Existing statement | Evidence/risk | Required disposition |
|---|---|---|---|
| `WEB-001` | App conversations/files “never touch anything we run” and the project has no access. | `agentkip-site/src/app/privacy/page.tsx:16-20,61-70`; conflicts with configured diagnostics/device paths and lacks actor-specific qualification | Replace before legal publication. |
| `WEB-002` | Website hosting/processors are only Vercel and Clerk. | `agentkip-site/src/app/privacy/page.tsx:50-55`; omits Neon/Drizzle and conditional Stripe/billing records | Replace with verified data-path/provider disclosure. |
| `WEB-003` | Product is not directed at and does not knowingly collect from people below age 13. | `agentkip-site/src/app/privacy/page.tsx:88-93`; conflicts with locked adults-only launch | Replace with 18+ eligibility and handling of suspected ineligible accounts. |
| `WEB-004` | App has no analytics/tracking/telemetry and holds only a pairing token as sensitive data. | `agentkip-site/src/app/security/page.tsx:94-114`; conflicts with diagnostics, GitHub credentials/settings, device context, and caches | Replace with scoped, verified claims. |
| `WEB-005` | Nothing passes through AgentKip infrastructure. | `agentkip-site/src/app/security/page.tsx:148-155`; live architecture/deployment not established and service website stores account/billing data | Remove absolute; describe the precise phone-to-Noggin path and exceptions. |

## Required refresh procedure

Before approval, update all three commit IDs, re-run each negative search, and turn every public
claim's row to `Supported`. A policy choice without code evidence may remain in Terms as a promise
only if the release owner accepts it as an enforceable operating commitment and the applicable
release blocker is closed.
