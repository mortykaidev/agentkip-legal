# AgentKip Service Providers and Connected Services

**Updated:** July 15, 2026

**Version:** 2026.07.15-draft.1

**Applies to:** AgentKip website visitors and United States adult beta users

This draft identifies service providers present in audited AgentKip code and important services you
may direct AgentKip to use. It supplements the [Privacy Policy](/privacy). Production enablement,
configuration, contracts, record fields, and retention remain release-verification gates. A
company’s role can differ by feature: some vendors process information for Hayward, while others
independently provide a service you choose.

## Hayward service providers

### Clerk

**Code/configuration purpose:** Website authentication, account identity, and session management.

**Information:** Account identifiers, email/profile information, authentication events, session
cookies, device/network information, and security events as described by Clerk.

**Control:** Use available account and session controls; contact us for an AgentKip account request.

### Neon

**Code/configuration purpose:** Hosted database infrastructure used with Drizzle for account, service, consent,
configuration, billing-status, and entitlement records.

**Information:** Records the Service writes to the database, which may include account identifiers,
document/consent versions, settings, entitlement state, and information submitted through an enabled
service route. Do not assume that all User Content remains on the phone or self-hosted environment.

**Control:** Account and deletion requests are handled through AgentKip or hello@agentkip.ai.

### Vercel

**Code/configuration purpose:** Hosting and delivery of agentkip.ai and related web functions.

**Information:** Web requests, IP address, browser/device information, timestamps, routes, cookies
or headers used by the site, security events, and data processed by deployed web functions.

**Control:** Browser cookie controls and applicable AgentKip privacy requests.

### Stripe

**Code/configuration purpose:** Billing, payment processing, subscription status, and entitlement management where a
paid offering is available.

**Activation status:** Inactive for the approved launch baseline; production use remains unverified.

**Information:** Stripe receives payment and billing details under its policy. Hayward may receive
customer, subscription, product, price, amount, status, and transaction identifiers and dates, but
not full payment-card numbers.

**Control:** Use the billing portal where available or contact us. Stripe may retain transaction
records under financial, fraud-prevention, and legal requirements.

## Platform and user-directed services

### Apple

Apple provides iOS, App Store and TestFlight distribution, device permissions, Keychain, push or
system services used by enabled features, and purchase services where applicable. Apple processes
information independently under its terms and privacy policy. Your Apple ID, device, purchase,
backup, notification, and platform settings are controlled through Apple.

### GitHub

If you connect GitHub, AgentKip processes selected account, organization, repository, issue, pull-
request, commit, branch, installation, and authorization information needed for the action you
request. GitHub independently controls its platform records. Select the fewest repositories and
permissions, and revoke the GitHub App installation or token in GitHub when finished.

### AI providers

AgentKip may transmit prompts, selected context, files or repository content, images, audio,
instructions, and related metadata to the AI provider you select. The exact provider can vary by
account and self-hosted configuration. Before the app first sends personal information to a third-
party AI provider, it will identify the provider, categories, purpose, and relevant policy and ask
for separate permission.

An AI provider may retain, review, or use information according to its contract, account tier,
settings, and policy. Review those terms and model-training controls. Hayward’s promise not to use
User Content to train or improve a Hayward model does not change an independent provider’s terms.

### Self-hosted Noggin and configured gateways

A self-hosted Noggin service or configured gateway is operated by you or the host owner, not by
Hayward merely because AgentKip connects to it. That operator controls hosting, network exposure,
logs, databases, models, checkpoints, backups, retention, credentials, and deletion. Device context
and flight-recorder metadata may be transmitted to the configured gateway as described in the
Privacy Policy.

### Other integrations

The Service may add another provider or integration. The connection or consent surface must identify
the service and requested capabilities before use. That service’s terms and privacy policy govern
its independent processing.

## Locations and changes

These companies and user-directed services may process information in the United States and other
locations described in their documentation. AgentKip’s beta is currently limited to United States
adult users and is not offered as an international-transfer compliance solution.

Before this page is approved for publication, every active Hayward service provider must be verified
against the production deployment and required to use personal information only for its assigned
services with protection equivalent to the commitments in the Privacy Policy and applicable law.
We will update this page before adding a service provider that materially changes how Hayward
processes personal information. A user-directed integration may become available through a product
update; the app will identify the recipient, information, purpose, and relevant privacy terms and
request any required permission before transfer.

Questions: hello@agentkip.ai
