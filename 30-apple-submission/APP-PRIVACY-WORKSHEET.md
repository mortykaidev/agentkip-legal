# App Privacy Worksheet

Status: **BLOCKED - release-build evidence incomplete**

Applies to: AgentKip and every bundled extension or companion submitted with it

Snapshot date: 2026-07-15

## How to use this worksheet

Apple requires declarations for data collected by the app and by third-party
partners whose code is integrated into it. Data processed only on-device is not
treated the same as data transmitted off-device. Free-form text and recordings
must be evaluated as `Other User Content` and `Audio Data`; do not infer every
possible sensitive category a user might voluntarily include.

Complete the worksheet from an archived release build and production traffic
trace. Reconcile it with the public Privacy Policy and provider register before
submission.

## Current known behavior

- Account creation exists. The exact account fields, authentication identifiers,
  and server-side records require release-build and production-schema evidence.
- Metadata flight recording currently defaults on, and metadata segments may be
  uploaded automatically when a gateway is configured.
- Full-content capture and content-segment upload currently default off, but
  metadata events can include software-redacted snippets of up to 80 characters
  from prompts and replies. Those snippets may upload automatically because the
  app marks the events as metadata. Redaction may not remove every sensitive
  value. This is a release blocker that must be reconciled with the final binary.
- Device context currently defaults on and can include a stable identifier, raw
  hardware identifier, device name, OS/app/build versions, capability flags,
  locale, and time zone.
- AgentKip can transmit user instructions and selected context to a self-hosted
  Noggin and user-selected AI providers. Exact routing and retention vary by the
  user's configuration.
- The website uses Clerk authentication/cookies, Neon/Drizzle data storage,
  Stripe billing or entitlement records, Vercel hosting, and local storage for
  theme preference. Website collection must not be confused with app collection,
  but the public Privacy Policy must cover both.
- No ads, data sale, cross-app tracking, or company model training is intended.
  Each claim remains blocked until production SDK/configuration and contract
  evidence confirms it.

## Candidate data-type decisions

| Apple data type | Candidate status | Possible source or use | Release evidence required |
|---|---|---|---|
| Name | Possible | Account profile or authentication | Account schema, Clerk configuration, API trace |
| Email address | Likely collected | Account authentication and support | Account schema, authentication flow, support flow |
| Phone number | Unknown | Authentication may expose it if enabled | Clerk factors and production settings |
| Physical address | Not intended | No product purpose identified | UI/schema scan and provider field inventory |
| Payment information | Provider-handled; verify | Stripe-hosted billing may keep payment data outside AgentKip | Checkout implementation and Stripe data-access evidence |
| Purchase history | Possible | Billing or entitlement status | Stripe/Apple purchase integration and entitlement schema |
| Photos or videos | Possible | User-selected context or attachment | Permission flow, upload trace, retention path |
| Audio data | Possible | Speech input or user recording | Speech pipeline trace, provider routing, retention behavior |
| Emails or text messages | Possible | User-selected content supplied to an agent | Integration inventory and transfer trace |
| Other user content | Likely collected | Prompts, conversations, files, repository content, support text | End-to-end data-flow trace and retention evidence |
| Browsing history | Unknown | Web or repository research tools | Tool-capability inventory and server trace |
| Search history | Possible | Search prompts or queries | Client/server logs and retention evidence |
| User ID | Likely collected | Account, consent, entitlement, or session identity | Account schema and API trace |
| Device ID | Likely collected under current behavior | Stable and raw hardware identifiers in device context | Exact fields, destinations, retention, reset behavior |
| Product interaction | Possible | Flight-recorder metadata | Event schema, defaults, destination, retention |
| Crash data | Unknown | OS or SDK crash reporting | Dependency/entitlement audit and App Store settings |
| Performance data | Possible | Flight-recorder or diagnostics metadata | Event schema, defaults, destination, retention |
| Other diagnostic data | Likely collected under current behavior | Device context and metadata uploads | Payload capture and server retention evidence |
| Coarse location | Possible inference | IP address, locale, or time zone can imply location | Server log fields and provider documentation |
| Precise location | Not intended | No product purpose identified | Entitlement/permission scan and traffic evidence |
| Contacts | Not intended | No product purpose identified | Entitlement/permission and code-path scan |
| Sensitive information | Not specifically solicited; verify | Users may place sensitive material in free-form content | UX prompts, model routing, and policy review |

This table is deliberately conservative. `Likely collected` is not a final App
Store answer; it signals that evidence must support classification, linkage, and
purpose.

## Purpose, linkage, and tracking questions

For every data type marked collected, record:

- Purpose: app functionality, analytics, developer advertising/marketing,
  third-party advertising, product personalization, or other purpose.
- Whether Hayward Imagination Company LLC or a partner links it to an account,
  device, or other identity.
- Whether it is combined with third-party data for targeted advertising,
  advertising measurement, or a data broker. The intended answer is no, but it
  requires SDK, provider-contract, and production-configuration evidence.
- Whether collection is optional and infrequent enough to satisfy every element
  of Apple's optional-disclosure criteria. Do not assume a user-triggered report
  qualifies without checking all criteria.
- Whether the data is merely transmitted to service a request and immediately
  discarded, or retained in readable form by AgentKip or a partner.

## Required release evidence

- [ ] Archived build dependency list and SDK privacy manifests.
- [ ] Runtime traffic capture for fresh install, signed-in idle state, chat,
      voice, photo/file attachment, GitHub, diagnostics, and deletion.
- [ ] Client payload schemas and server log/database schemas.
- [ ] Production retention configuration and deletion verification.
- [ ] AI-provider routing matrix, policies, and data-use settings.
- [ ] Clerk, Neon, Stripe, Vercel, Apple-service, and GitHub data-flow evidence.
- [ ] Confirmation that metadata and device context are default-off until a
      documented opt-in or user-triggered submission.
- [ ] Confirmation that no advertising/tracking SDK or configuration is present.
- [ ] Final answers exported from App Store Connect and diffed against this file.

## Release blockers

1. **Automatic metadata path:** metadata recording/upload is broader than the
   intended user-triggered diagnostics promise.
2. **Device-context path:** device context defaults on and includes persistent or
   identifying fields; consent, minimization, and classification are unresolved.
3. **Provider evidence:** exact AI-provider, self-hosted Noggin, and third-party
   retention behavior is not yet evidenced.
4. **SDK evidence:** the release archive and integrated SDK manifests have not
   been inventoried.
5. **Deletion evidence:** account and associated-data deletion is not implemented
   or demonstrated.

Source: [Apple App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)
