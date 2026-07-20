# Retention Schedule

Status: **BLOCKED - periods are not approved or technically evidenced**

Rule: Do not publish a retention promise until the production systems enforce it.

## Retention principles

- Keep personal data only for a documented purpose and no longer than necessary.
- Prefer local or user-controlled storage where the product can operate without
  company retention.
- Separate active data, backups, security logs, billing records, consent evidence,
  and legal holds; one deletion claim cannot silently cover all of them.
- Start expiry from a defined event, such as account deletion, token revocation,
  conversation deletion, submission closure, or incident closure.
- Make backup expiry and deletion lag explicit.
- Never retain credentials, raw user content, or diagnostics merely because a
  deletion path has not been built.

## Schedule requiring approval and enforcement

| Record class | Purpose | Current behavior | Required retention decision | Deletion trigger | Status |
|---|---|---|---|---|---|
| Account/profile | Authentication and service delivery | Unknown across Clerk/AgentKip stores | Define active-account period and post-deletion exceptions | Verified account deletion | BLOCKED |
| Session/auth tokens | Authentication | Exact storage/expiry unknown | Shortest provider-supported lifetime; revoke on deletion/disconnect | Logout, rotation, revocation, deletion | BLOCKED |
| Consent receipts | Prove versioned decisions | Not implemented/evidenced | Define evidentiary period and minimization; preserve document hash, not document copy unless required | Account deletion plus approved exception | BLOCKED |
| Conversation content | User-requested AI service | User/self-hosted and provider behavior varies | Document each store/provider; company retention should be none unless needed and disclosed | User deletion/account deletion/provider control | BLOCKED |
| Attachments/repository content | Perform user-requested action | Exact caching/logging unknown | Ephemeral processing where feasible; define cache expiry | Request completion, cache expiry, deletion | BLOCKED |
| GitHub metadata/diffs | Integration and action history | Exact stores unknown | Separate operational cache from action receipt | Disconnect, repository removal, expiry, deletion | BLOCKED |
| Credentials/secrets | Authenticate integrations | Exact stores/partitioning require evidence | Retain only while integration is active; never log; revoke/erase promptly | Disconnect, rotation, deletion | BLOCKED |
| Action authorization receipts | Safety, accountability, dispute handling | Interface approved; store unknown | Define minimal fields and evidence period; exclude raw secrets/content | Account deletion plus approved exception | BLOCKED |
| Device context | Compatibility/diagnostics | Defaults on; destination/retention unknown | Default-off; collect minimal fields only for explicit purpose; define short expiry | Opt-out, submission deletion, account deletion | BLOCKED |
| Flight-recorder metadata | Troubleshooting | Recording defaults on; may auto-upload; includes software-redacted prompt/reply snippets of up to 80 characters | Remove snippets or require explicit content opt-in; default-off transmission; define local ring size and server expiry | Clear diagnostics, expiry, deletion | BLOCKED |
| Flight-recorder content | Troubleshooting | Full-content capture/content-segment upload defaults off, excluding snippets currently misclassified as metadata | Preserve default off; if submitted, define explicit preview and short expiry | Submission deletion/closure and expiry | BLOCKED |
| Support tickets | Resolve user request | Destination/retention unknown | Define closure-based period and deletion/escalation exceptions | Ticket closure, account deletion | BLOCKED |
| Billing/entitlements | Transactions and access | Stripe/AgentKip records exist or are planned | Distinguish processor records from company-accessible records and legal retention | Account deletion, transaction/legal requirement | BLOCKED |
| Website/server logs | Security and operations | Vercel/provider logging unknown | Define fields, access, rolling expiry, and IP handling | Automatic expiry, verified request where applicable | BLOCKED |
| Security/incident records | Protect systems and investigate incidents | Process not yet evidenced | Define severity-based period and strict access; redact user content | Incident closure plus approved period | BLOCKED |
| Backups | Resilience | Scope/expiry unknown | Define encrypted backup scope, restore access, rotation, and deletion propagation | Rotation and deletion propagation | BLOCKED |

## Approval record required per row

Before a row can change from `BLOCKED`, record:

- Data/system owner.
- Exact production stores and backup copies.
- Approved period or objective criterion; avoid vague `as long as necessary`.
- Starting event and deletion service level.
- Access roles and audit controls.
- Technical enforcement and monitoring evidence.
- Legal or contractual exception, if any.
- Public-policy language and App Privacy impact.

## Release blockers

Every row above is blocked until the named decisions and enforcement evidence
exist. The public Privacy Policy must use candid system-specific language rather
than inventing a universal number.
