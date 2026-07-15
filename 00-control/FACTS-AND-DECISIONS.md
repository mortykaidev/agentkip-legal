# Facts and Decisions

Baseline frozen: **2026-07-15**

Decision owner and publication approver: **Brandon**

Package status: **internal draft; not attorney-reviewed**

This file separates decisions from current implementation facts. A decision is not a shipped
technical control. Any public statement about product behavior must also have supported evidence
in `CLAIM-TO-CODE-MATRIX.md` and pass the release gates.

## Identity and launch

| Topic | Locked decision |
|---|---|
| Legal entity | Hayward Imagination Company LLC, a Michigan limited liability company |
| Products | AgentKip (iOS client), Kip (assistant identity), and Noggin (self-hosted agent/backend) |
| Public contact | `hello@agentkip.ai` |
| Public address | No residential address may be stored or published. Use entity + Michigan + email until a non-residential business address is approved. |
| Initial audience | Adults age 18 or older with legal capacity |
| Initial region | United States only |
| Later regions | New Zealand, UK/Ireland, EEA, and additional US-state modules remain inactive until their activation checklists pass |
| Distribution | TestFlight/App Store candidate using Apple's Standard EULA plus AgentKip service Terms |
| Governing law | Michigan law and Michigan courts, without mandatory arbitration, subject to non-waivable law |
| Launch review | Internally reviewed indie-launch baseline. Do not state or imply attorney, lawyer, or counsel review. |

## Product and responsibility model

- AgentKip is an AI-enabled client for a user-controlled or user-authorized Noggin environment and
  user-selected external services.
- The user must own or have authority to control every repository, organization, account, app,
  phone, device, credential, dataset, deployment, server, and third-party service they connect.
- The user is responsible for prompts, instructions, permission choices, backups, testing,
  credentials, provider charges, third-party terms, applicable law, and actions they initiate,
  approve, or explicitly enable.
- AI output may be inaccurate, insecure, incomplete, destructive, biased, or manipulated by
  untrusted content. AgentKip is not for emergency, safety-critical, medical, legal, financial, or
  unsupervised production reliance.
- Terms may allocate risk, disclaim warranties, exclude categories of damages, and cap direct
  liability to the extent permitted by law. They do not waive AgentKip's own non-waivable privacy,
  security, consumer-protection, fraud, willful-misconduct, or gross-negligence obligations.
- The baseline aggregate direct-liability cap is the greater of fees paid during the preceding 12
  months or USD $100, subject to applicable-law carveouts.

## Acceptance and authorization

| Surface | Decision |
|---|---|
| Eligibility | Neutral 18+ attestation before product use |
| Terms | Unchecked, explicit agreement to versioned Terms and Acceptable Use |
| Privacy | Separate acknowledgment; a privacy policy is not described as blanket consent |
| AI providers | Separate, just-in-time consent identifying provider, data categories, purpose, and policy before personal data is sent |
| Connected targets | Target-specific authority attestation when connecting repositories, devices, accounts, or services |
| Auto Apply | Separate risk acknowledgment before activation |
| Material changes | Re-acceptance required without deleting user data |
| Receipts | Retain document IDs, versions, SHA-256 hashes, timestamp, locale, age attestation, consent decisions, and event type; make them displayable and exportable |

Authorization is enforced as a product capability, not only prompt text:

- **Read Only:** no write, push, deploy, publish, message, purchase, or device-change capability.
- **Ask First (default):** every mutation receives an exact preview and approve/deny decision.
- **Auto Apply:** only reversible edits inside an explicitly selected repository on a non-protected
  branch; never a substitute for always-confirm actions.
- **Always confirm:** remote push, pull-request merge, deploy/release, publication, external
  message, purchase, access-control change, credential rotation, and device configuration.
- **Blocked for initial release:** force-push/history rewrite, protected-branch direct write,
  repository deletion, device wipe, credential extraction, security-control bypass, and unscoped
  production operations.
- Missing target, provider, scope, risk, approval response, or transport integrity fails closed.

Action confirmations identify the target, effect, risk, reversibility/checkpoint, external side
effects, and cost before the decision. They are separate from Terms acceptance.

## Privacy and data commitments

These are policy commitments, not pre-approved factual claims:

- No advertising, sale of personal information, or cross-context behavioral tracking.
- No company training of models on user content.
- Collect and retain only data needed for the disclosed feature, security, support, or legal
  purpose, with a documented deletion or revocation path.
- Diagnostics and device context must be off by default or separately, explicitly enabled before
  transmission. User-triggered submission must show the exact encoded payload.
- Provider/API disclosures must cover Clerk, Neon/Drizzle, Stripe when enabled, Vercel, Apple
  services, GitHub, Noggin, user-selected model providers, and any shipped SDK that receives data.
- Deleting AgentKip-controlled account data does not delete independently controlled repositories,
  apps, phones, devices, provider accounts, or self-hosted Noggin data.

The current iOS and website implementations do not yet satisfy every commitment. In particular,
metadata diagnostics and device context default on in the audited iOS revision; the website uses
Clerk, Neon/Drizzle, Stripe-related records, Vercel dependencies, and browser storage. Those facts
must be disclosed or the implementation must change before publication.

## Commercial and regional decisions

- Paid-service, subscription, promotion, refund, and cancellation language remains inactive until
  the corresponding production payment flow and policy are explicitly enabled and verified.
- Existing Stripe test-mode or entitlement code does not prove that paid production service is
  live.
- Regional supplements are not public merely because files exist. `inactive` means excluded from
  approved exports.
- A non-residential business address, representative requirements, international transfer facts,
  and region-specific rights are activation gates where applicable.

## Governance

- This private repository is the authoritative legal/compliance source.
- Brandon approves publication and merge. No model or agent is an approver.
- Generated website and app copies are immutable outputs of the manifest workflow.
- A document is publishable only when its manifest entry is `approved` or `published`, the exact
  hash matches, its source commit is recorded, its claims have evidence, and all applicable
  blockers are closed.
- Future professional legal review is recommended, but not a day-one gate. Reconsider it before
  minors, regulated health/financial data, enterprise contracts, UK/EEA distribution, materially
  broader autonomous authority, or a material dispute.

## Explicitly unresolved or non-facts

- No public street address is approved.
- No production launch date is approved by this package.
- No claim that the system is risk-free, fully private, anonymous, zero telemetry, incapable of
  data loss, or inaccessible to AgentKip is approved.
- No production processor location, retention duration, deletion SLA, or payment state should be
  inferred from dependency names alone; those require environment evidence and provider records.
- No legal document is represented as attorney-reviewed, legally certified, or guaranteed
  enforceable.
