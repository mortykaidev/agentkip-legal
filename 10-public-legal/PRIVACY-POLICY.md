# AgentKip Privacy Policy

**Effective:** July 15, 2026

**Version:** 2026.07.15-draft.1

**Applies to:** AgentKip website visitors and United States adult beta users

This Privacy Policy explains how Hayward Imagination Company LLC (**“Hayward,” “AgentKip,” “we,”
“us,”** or **“our”**) handles personal information in connection with the AgentKip iOS application,
agentkip.ai, account services, support, and related beta features (collectively, the **“Service”**).

AgentKip can connect to a self-hosted Noggin service, AI providers, GitHub, Apple services, and
other systems you choose. Where information goes depends on the feature, provider, and deployment
you select. We do not make the blanket claim that information never reaches us. This policy
describes the circumstances in which it may.

## 1. Scope and roles

This policy applies when Hayward determines why and how personal information is processed—for
example, on our website, in our account system, or when you contact support. A self-hosted Noggin
instance and third-party services you direct may process information outside our control under
their own terms and privacy policies.

This policy applies to information Hayward processes from visitors to its public website regardless
of where they access it; that coverage does not make the product available in another region. The
AgentKip beta itself is only for adults age 18 or older in the United States. It is not offered for
children or for workloads that require a regulated-data agreement. Non-waivable law may provide a
website visitor additional rights.

## 2. Information we may process

The categories below depend on the features you use.

### Account, website, and relationship information

- name, email address, account identifier, authentication status, and profile information;
- acceptance and consent records, including document versions, timestamps, locale, and decisions;
- connected-service identifiers, configuration choices, permission modes, and revocation status; and
- communications, feedback, support requests, and deletion requests.

The audited AgentKip website code is configured to use Clerk for authentication and session
management, including authentication and session cookies. Clerk may process login credentials and
authentication factors; the integration is designed so Hayward does not receive the raw Clerk
password. The audited code is also configured for Neon and Drizzle account, service, and entitlement
records and for Vercel hosting. A theme preference may be stored in your browser’s local storage.
The production deployment, enabled routes, provider settings, and exact record fields remain a
release-verification gate; this draft must be updated if the verified deployment differs.

### User Content and agent activity

User Content may include prompts, chat messages, repository content, filenames, code, documents,
images, audio or speech you choose to submit, tool requests, previews, approvals, outputs, and action
results. Depending on your configuration, this information may be processed on your device, by your
self-hosted Noggin instance, by an AI provider you select, by a Connected System, or by Hayward
systems needed to provide an account, relay, support, or other disclosed feature.

Before the app sends personal information to a third-party AI provider, it will identify that
provider, the categories to be sent, the purpose, and a link to relevant provider information, and
request separate permission. Declining may disable that provider-dependent feature.

### Connected Systems and credentials

When you connect GitHub or another service, we may process account and repository identifiers,
selected installation scope, authorization status, and the information necessary to request the
action you direct. The iOS app stores supported GitHub tokens and credentials in the iOS Keychain.
Some connection flows copy a token from the configured host to the phone and store it in the iOS
Keychain so the requested integration can operate. That transfer must be treated as credential
access: connect only a host you control and trust, protect both the host and phone, and revoke tokens
when access is no longer needed. Other authentication
tokens or credentials may be handled by your self-hosted environment, the connected service, or an
authorized service component, depending on the integration. Do not paste secrets into prompts. Use
designated authorization flows and grant only the minimum repositories and permissions required.

### Device permissions and media

If you choose a feature that needs it, the app may request access to microphone or speech input,
camera, photos, notifications, local-network discovery, or similar iOS capabilities. Apple controls
the system permission prompt. We use the resulting data for the feature you requested and do not
claim access merely because a permission exists. You can change permissions in iOS Settings.

### Diagnostics, device context, support, and security data

The Service creates flight-recorder and device-context information. In the July 15, 2026 beta
baseline, configuring a gateway enables automatic upload of flight-recorder metadata. Full-content
capture and content-segment upload are off by default, but that does **not** mean prompt and reply
content is absent from the metadata path. Current metadata events can include software-redacted
snippets of up to 80 characters from prompts and replies. Because the app marks those events as
metadata, it may upload the snippets automatically when a gateway is configured. The software
attempts to replace recognized secret patterns before truncating a snippet, but that process is not
a guarantee that every sensitive value will be removed. Other operational metadata can include
timestamps, event types, app and operating-system versions, error states, connection status,
feature state, and security-relevant events.

Device-context sharing is also on by default in this baseline. Shared fields can include a stable
device identifier, raw hardware identifier, user-assigned device name, hardware and capability
information, operating-system version, AgentKip app/build version, locale, and time zone. These
fields can identify or distinguish a device even when they do not name a person. They are provided
to the configured gateway to support device-aware behavior, compatibility, troubleshooting, and
service operation.

A user-initiated support or diagnostic submission may include additional context shown in its
preview. Review the preview and remove sensitive information before sending. The automatic
metadata snippet path, automatic/default-on diagnostics, and default-on device-context sharing are
release blockers. We plan to remove them or place them behind explicit, accurately labeled user
controls before public release; until those product changes are shipped and verified, the behavior
described in the preceding paragraphs is the current behavior.

Our website and service infrastructure may receive ordinary network and security information such
as IP address, request time, browser or device type, route requested, and abuse-prevention events.

### Transaction and entitlement information

The audited website code includes a Stripe billing and entitlement integration that may be enabled
where a paid offering is available. When enabled, Stripe processes payment credentials under its own
policy. The integration is designed to provide Hayward transaction and entitlement records such as
customer and subscription identifiers, product, price, status, amount, and relevant dates rather
than full payment-card numbers. Apple may process App Store or in-app transactions under Apple’s
policies. Production payment status, accessible fields, and retention remain release-verification
gates. If a specific beta tier is free, enabled systems may still keep the account or entitlement
state needed to determine access.

## 3. How we use information

We may use personal information to:

- provide, authenticate, configure, and secure the Service;
- carry out the provider connection, tool request, or action you direct;
- record and enforce consent, permissions, approvals, revocations, and legal-document versions;
- provide support and user-requested diagnostics;
- detect abuse, protect accounts and Connected Systems, and investigate security incidents;
- maintain, debug, and improve product reliability using information appropriate for that purpose;
- communicate service, security, legal, billing, or support information; and
- comply with law and establish, exercise, or defend legal claims.

We do not sell personal information. We do not use personal information for targeted or cross-
context behavioral advertising. We do not use User Content to train or improve a Hayward model. An
AI provider you choose may process information under its own terms, settings, and privacy policy;
review those materials before consenting.

These are launch commitments, not conclusions inferred from a dependency list. Publication remains
blocked until dependency, network, provider-contract, configuration, and operational review verifies
that the release actually satisfies them.

## 4. When information is disclosed

We may disclose information:

- **At your direction:** to an AI provider, GitHub, Apple service, self-hosted Noggin instance, or
  other Connected System you select;
- **To service providers:** that host, authenticate, store, bill, secure, or support components of
  the Service under contractual restrictions appropriate to their role;
- **For safety and law:** where reasonably necessary to comply with valid legal process, protect
  rights or safety, investigate abuse, or secure the Service; and
- **For a business transaction:** in connection with a merger, financing, acquisition,
  reorganization, bankruptcy, or sale of assets, subject to appropriate confidentiality and notice
  where required.

The current categories of service providers and user-directed integrations are described on the
[Subprocessors and Connected Services page](/subprocessors).

For public release, a service provider processing personal information for Hayward must use it only
for the services it provides to us and protect it to the same or an equivalent standard promised by
this policy and applicable law. Provider contracts and production configurations are not yet fully
verified, so this policy cannot be approved or published until that evidence is complete. A service
you independently direct may instead act under its own terms; the app must identify the recipient,
information, and purpose and request any required permission before transfer.

We do not disclose personal information to data brokers or advertising networks for their own
targeted advertising.

## 5. Storage and retention

Information may be stored on your device, in your self-hosted environment, by a provider or
Connected System you choose, and in our account or service systems where necessary for the feature.
Do not assume that deleting one copy deletes every independently controlled copy.

We retain information according to its purpose:

- account, configuration, billing, and entitlement information while the account or transaction is
  active and for the period reasonably needed to complete deletion, prevent fraud, resolve
  disputes, maintain financial records, and meet legal obligations;
- acceptance, consent, authorization, and transaction records for as long as reasonably necessary
  to demonstrate the choices and transactions they document;
- flight-recorder metadata, device context, support records, and user-submitted diagnostics for the
  operational periods configured by the receiving gateway and, where Hayward controls the
  destination, only as reasonably necessary for service operation, security, support,
  recordkeeping, or legal needs; and
- website and security logs for a limited period appropriate to reliability, fraud prevention,
  incident investigation, and legal compliance.

Exact default and maximum periods, deletion triggers, backup expiration, and approved exceptions
have not yet been verified for every controlled system and provider. This policy cannot be approved
or published until those periods are added from production configuration and contractual evidence;
“reasonably necessary” is not a substitute for that release record.

Content stored by your device, self-hosted Noggin instance, AI provider, GitHub, Apple, or another
Connected System follows that system’s retention controls. Our [Data Deletion Notice](/data-deletion)
explains scope and requests.

## 6. Your choices and rights

Depending on where you live and subject to legal exceptions, you may request access to, correction
of, deletion of, or a portable copy of personal information Hayward controls. You may also revoke
an optional consent, disconnect an integration, change an iOS permission, or object to or restrict
certain processing where applicable.

Use the controls in AgentKip or email hello@agentkip.ai. We may verify your identity and authority
before completing a request. You may use an authorized agent where state law permits; we may request
proof of authority and identity. We will respond within the time required by applicable law and will
explain a denial or available appeal process when required.

Because we do not sell personal information or use it for targeted advertising, there is no sale or
targeted-advertising opt-out to exercise. If that practice changes, we will update this policy and
provide required controls before the change.

## 7. Account deletion, disconnection, and local data

Deleting an AgentKip account is different from disconnecting a provider or deleting data elsewhere.
An account-deletion request covers account data Hayward controls, subject to lawful retention. It
does not delete repositories, branches, deployments, apps, files, device data, self-hosted Noggin
data, AI-provider records, GitHub data, or other content controlled independently by you or another
service. You must use those systems’ deletion and retention controls separately.

The app will present deletion status and any category retained with an explanation. See
[Data Deletion](/data-deletion) for the full process.

## 8. Security

We use administrative, technical, and organizational safeguards designed for the nature of the
Service and information. No system is perfectly secure, and beta software carries additional risk.
Use strong device and account security, minimum integration permissions, protected branches,
backups, and human review. See [Security](/security) for our security model and reporting process.

## 9. Children and regulated information

The Service is not directed to anyone under 18, and the Terms prohibit minors from creating beta
accounts. The required neutral age gate and bypass tests are not yet implemented, so this draft does
not claim that the current build prevents minor accounts. Publication remains blocked until that
control is implemented and verified. If you believe a minor provided personal information, contact
hello@agentkip.ai.

The beta is not designed for protected health information, payment-card data, Social Security
numbers, government identification, biometric templates, children’s data, or other regulated or
highly sensitive workloads. Do not intentionally submit such information. Use designated secure
authentication flows rather than placing credentials or private keys in User Content.

## 10. Processing locations

Hayward is based in the United States. Our providers and user-directed services may process
information in the United States or other locations described in their documentation. This beta is
not offered as a solution for international data-transfer compliance and is not currently launched
outside the United States.

## 11. Changes to this policy

We may update this policy to reflect product, provider, legal, or operational changes. We will post
the version and effective date. If a change materially affects how we use personal information, we
will provide reasonable notice and obtain renewed consent where required before applying the new
practice.

## 12. Contact

Hayward Imagination Company LLC

Michigan, United States

hello@agentkip.ai
