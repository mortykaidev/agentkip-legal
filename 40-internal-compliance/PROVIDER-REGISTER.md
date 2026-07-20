# Provider Register

Status: **BLOCKED - contracts, locations, and configurations incomplete**

Snapshot date: 2026-07-15

`Confirmed` below means the service is present in the audited product surface; it
does not mean every data use, role, or contract has been verified.

| Provider/category | Role and candidate data | Activation evidence | Entity/location | Privacy, retention, and deletion evidence | Last production verification | Required closure evidence |
|---|---|---|---|---|---|---|
| Clerk | Website authentication; contact info, account ID, session/device/security data | Confirmed in audited website code | Contracting entity and locations unverified | Official privacy/DPA sources recorded; active terms, retention, and deletion API unverified | Not completed | Production fields, cookies, factors, DPA, subprocessors, locations, retention, deletion API |
| Neon/Drizzle | Website database/data access; account, entitlement, consent, operational records | Confirmed in audited website code | Contracting entity and region unverified | Official privacy/DPA sources recorded; backup, retention, and deletion configuration unverified | Not completed | Production schema, region, backups, access, retention, deletion, DPA/subprocessors |
| Stripe | Billing/entitlements; account, transaction, entitlement, provider-held payment data | Integration present; inactive for approved launch baseline | Contracting entity and locations unverified | Official privacy/services sources recorded; active account terms and deletion limits unverified | Not completed | Enabled products, accessible fields, webhooks/logs, retention, DPA/subprocessors, deletion limits |
| Vercel | Website hosting; request/IP logs, cookies, page/form data, operational metadata | Confirmed in audited website code | Contracting entity and regions unverified | Official privacy/DPA sources recorded; logging/retention/deletion configuration unverified | Not completed | Production deployment, regions, logs, analytics, retention, DPA/subprocessors, deletion path |
| GitHub | User-selected repository integration; account/org/repo IDs, code/files, diffs, issues/PRs, credentials | Confirmed product capability | Independent service entity/location treatment unverified | Official permissions/authorization/Terms sources recorded; token/log retention unverified | Not completed | App permissions, selected repos, token stores, webhook logs, retention, revocation, terms |
| User-selected AI providers | Independent model inference; prompts, selected context, attachments, metadata | Provider category confirmed; exact providers unresolved | Provider entities and processing locations unresolved | Provider-specific policy, contract, training, retention, and deletion evidence unresolved | Not completed | Provider list, routing, policy URL, training/data-use settings, retention, region, credential model |
| Self-hosted Noggin | User/host-controlled gateway, tools, approvals, checkpoints; conversations, actions, credentials, diagnostics | Architecture confirmed | User-selected host/operator and location | Host-specific terms, logs, backups, retention, and deletion are user/operator controlled and unresolved | Not completed | Controller boundary, stores, retention, deletion, version support, secure defaults |
| Apple platform services | Distribution, purchases, push, speech/audio, photos/files, crash/analytics; service-specific data | App Store/TestFlight expected; exact services unresolved | Apple entity/location treatment unverified | Apple primary sources recorded; enabled services and app-specific retention unresolved | Not completed | Archive, entitlements, App Store settings, payload traces, agreements, deletion/user controls |
| Support destination | User support; contact information, report text, selected diagnostics | Destination unresolved | Entity and locations unresolved | Policy, retention, access, and deletion unresolved | Not completed | Vendor/system, exact payload preview, access, retention, deletion, incident handling |

## Required provider decision record

For each active provider, document:

- Contracting entity and service/product name.
- Controller, processor, subprocessor, or independent-controller role by flow.
- Data categories, purpose, user trigger, and default.
- Hosting/processing locations and cross-border transfer mechanism where relevant.
- Retention/deletion, backups, access, security, and breach-notification terms.
- AI training/model-improvement defaults and account-level controls where relevant.
- Current DPA, privacy notice, terms, subprocessor list, and effective dates.
- API/token scopes, secret owner, rotation, revocation, and least-privilege evidence.
- Product owner, review date, approved configuration, and exit/deletion plan.

## Release blockers

1. The exact AI-provider list and routing behavior are not frozen.
2. Provider contracts, DPAs, subprocessors, locations, and retention are not
   recorded.
3. Apple-service and support-provider use is incomplete.
4. Production configurations have not been captured and compared with public
   claims.
5. A provider cannot be described as preventing training, tracking, or retention
   without provider-specific evidence.
