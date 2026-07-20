# Unresolved Questions and Release Decisions

Status: **Open control register**

Snapshot date: 2026-07-15

Unknowns are blockers, not blank spaces to fill with favorable assumptions.
Close each item with a dated answer, owner, source/evidence, affected documents,
and implementation/test reference.

## P0 - blocks baseline release

| ID | Question/decision | Evidence required |
|---|---|---|
| P0-01 | Which exact iOS/macOS targets and extensions are distributed in the first release? | Archived build and App Store Connect target list |
| P0-02 | What exact fields, destinations, defaults, and retention apply to flight-recorder metadata and device context? | Payload schemas, fresh-install trace, server stores, tests |
| P0-03 | When will diagnostics/device-context transmission become default-off and user-triggered or explicitly opted in? | Implementation PR and client/server tests |
| P0-04 | What AgentKip-controlled accounts and stores exist across Clerk, Neon, Stripe, Vercel, app services, support, and Noggin? | Production schema/provider inventory |
| P0-05 | How does in-app account deletion reach every controlled store, revoke credentials, handle backups, and report partial failure? | UI/API implementation and deletion demonstration |
| P0-06 | Which AI providers/models can receive data, by what route, with what training, retention, location, and deletion settings? | Provider register, contracts/settings, runtime traces |
| P0-07 | Which app data types are collected, linked, or used for tracking under Apple's definitions? | Release archive, SDK inventory, traffic/store evidence |
| P0-08 | Which targets need privacy manifests, which required-reason APIs are present, and which reasons describe actual use? | Built-app scan and current Apple reason mapping |
| P0-09 | What cryptography does each submitted binary contain/use, and what export classification/Info.plist answer applies? | Engineering inventory and App Store record |
| P0-10 | How are Read Only, Ask First, Auto Apply, always-confirm, and blocked actions enforced client-side and in Noggin? | Capability tests and end-to-end failure tests |
| P0-11 | Where are legal/provider/authorization receipts stored, protected, exported, retained, and deleted? | Interface/API/store implementation and threat review |
| P0-12 | Can signup, invite, pairing, restore, or deep links bypass current legal acceptance? | Route inventory and UI/integration tests |
| P0-13 | What non-personal reviewer environment and seeded account let Apple exercise every primary capability? | Review runbook and live dry run |
| P0-14 | What exact retention/expiry rule applies to every record and backup class? | Approved schedule and technical enforcement evidence |
| P0-15 | Who owns incident roles, out-of-band contacts, and each provider escalation? | Private operations roster and tabletop evidence |

## P1 - blocks a claim or capability

| ID | Question/decision | Evidence required |
|---|---|---|
| P1-01 | Can the company prove no ads, tracking, sale/share, or company model training across all SDKs/providers/configurations? | Dependency/configuration/contracts and runtime evidence |
| P1-02 | Which GitHub permissions are truly necessary for each mode, and how are repository selection and scope increases controlled? | GitHub App config, capability map, reconnect tests |
| P1-03 | What data remains entirely on device, what reaches self-hosted Noggin, and what reaches AgentKip or a provider? | End-to-end trace per feature/configuration |
| P1-04 | Does support-report preview exactly match encoded/transmitted bytes, including retry and failure? | Golden payload and transport tests |
| P1-05 | Which Apple services are enabled for push, speech, files/photos, purchases, crash data, and analytics? | Entitlements, config, archive, runtime trace |
| P1-06 | Is Stripe billing active at launch, and what cancellation/refund/subscription copy is required? | Product decision, App Store/billing configuration |
| P1-07 | Which website cookies/local-storage entries are essential, optional, analytical, or marketing? | Browser storage/network audit and provider settings |
| P1-08 | What public vulnerability-reporting path and incident service level can be sustained? | Operational owner, intake, escalation, response tests |
| P1-09 | What is the current age-rating questionnaire result after all AI/content/tool capabilities are included? | Saved App Store Connect questionnaire |
| P1-10 | What is the supported Noggin version/deployment matrix and secure update path? | Tested deployment documentation and compatibility CI |

## P2 - blocks regional or expanded release

| ID | Question/decision | Evidence required |
|---|---|---|
| P2-01 | What non-residential business-address/representative solution will be used where publication is required? | Approved service/entity record; never store a home address here |
| P2-02 | Which US state privacy, health, biometric, AI, breach, subscription, and consumer rules apply at launch metrics? | Dated 51-jurisdiction matrix and company metrics |
| P2-03 | What provider transfer safeguards support New Zealand, UK, Ireland, and EEA users? | Contract/location/transfer assessment per flow |
| P2-04 | Are UK/EEA representatives, DPO, DPIA, ROPA, transfer assessments, and authority routing required? | Territorial-scope and governance assessment |
| P2-05 | What EU AI Act role/use classification and applicable dates govern each capability? | Role/use-case inventory and current-source assessment |
| P2-06 | What accessibility, consumer, tax/VAT, trader, subscription, and ePrivacy/cookie obligations apply in each enabled country? | Country activation record and implementation tests |
| P2-07 | Will minors, regulated data, enterprise terms, public content, or broader autonomy enter scope? | Explicit product decision and future-review closure |

## Closed baseline facts

- Entity: Hayward Imagination Company LLC, Michigan.
- Products: AgentKip, Kip, and self-hosted Noggin.
- Initial posture: United States, adults-only beta, self-hosted Noggin.
- Contract approach: Apple's Standard EULA plus AgentKip service Terms.
- Disputes: Michigan law/courts, no mandatory arbitration, subject to mandatory
  consumer rights.
- Public contact: `hello@agentkip.ai`.
- Residential addresses are prohibited from tracked/public documents.
- The baseline is internally reviewed and is not represented as attorney-reviewed.
- Brandon retains publication and merge authority.

These facts remain subject to a material-change review; `closed` does not mean
they may be silently changed elsewhere.
