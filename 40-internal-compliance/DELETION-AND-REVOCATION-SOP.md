# Deletion and Revocation SOP

Status: **Draft operational procedure - implementation BLOCKED**

Public contact: `hello@agentkip.ai`

## Scope

Use this procedure for account deletion, data deletion, integration disconnect,
credential revocation, provider-consent revocation, and diagnostics deletion.
Deleting the AgentKip account is not the same as deleting user-controlled GitHub
repositories, apps, phones, devices, model-provider accounts, or self-hosted data.

## Intake and verification

1. Accept authenticated in-app requests. Support intake may help a user regain
   access but must not become the only deletion path.
2. Create a request ID and record the requested scope, time, authenticated
   subject, and communication channel without copying unnecessary user content.
3. Reauthenticate or use a proportionate identity check. Never request a password,
   recovery key, provider API key, or repository secret.
4. Show the user affected systems, expected timing, billing implications,
   external-data boundaries, and known retention exceptions before confirmation.
5. On confirmation, prevent new sessions and new covered processing as early as
   safely possible.

## Execution order

1. Revoke AgentKip sessions and authentication credentials.
2. Revoke or delete AgentKip-held integration tokens and pending invitations.
3. Stop background jobs, diagnostics uploads, provider transfers, and queued
   actions for the subject.
4. Delete active records from each AgentKip-controlled production store.
5. Invoke provider deletion/revocation APIs and record redacted outcomes.
6. Send a signed instruction to self-hosted Noggin only when the user requests it
   and the service supports a verifiable deletion operation.
7. Mark backup deletion/expiry according to the approved schedule.
8. Preserve only approved exception records, minimized and access-restricted.
9. Return completed, pending, partially completed, or failed status with the
   remaining system and next action.

## System checklist

- [ ] Clerk account, sessions, factors, invitations, and tokens.
- [ ] Neon/AgentKip account, consent, entitlement, and operational records.
- [ ] Stripe customer/entitlement references and legally/contractually retained
      transaction records; do not claim processor-held records were erased unless
      confirmed.
- [ ] Vercel or other logs to the extent controlled and covered by the approved
      retention/request process.
- [ ] GitHub tokens, installations, webhooks, cached repository data, and pending
      actions; do not delete repositories or GitHub accounts.
- [ ] AI-provider credentials, stored history, and provider-side deletion where
      AgentKip controls the relevant account/path.
- [ ] Self-hosted Noggin stores, checkpoints, logs, caches, and credentials when
      expressly requested and verifiably supported.
- [ ] Diagnostics, support records, device identifiers, push tokens, and local
      app data.
- [ ] Backups and incident/legal-hold exceptions.

## Revocation-specific behavior

- Legal/provider consent revocation blocks future covered processing; it does not
  retroactively invalidate a completed action.
- Integration disconnect revokes credentials before clearing local display state.
- Permission-mode downgrade takes effect server-side and client-side before the
  UI reports success.
- Push-token and device-identifier revocation must not depend on reinstalling the
  app.
- Revocation failure stays visible and retryable; never report success based only
  on a local flag.

## Completion evidence

Store only request ID, subject reference, systems attempted, timestamps, redacted
results, retained categories/reasons, backup-expiry status, and user notification.
Never place raw provider responses, secrets, repository content, or residential
information in the record.

## Release blockers

1. In-app deletion and authoritative deletion API are absent.
2. The production store/provider inventory is incomplete.
3. Retention exceptions and backup propagation are not approved.
4. Provider and self-hosted Noggin deletion/revocation are not end-to-end tested.
5. Partial-failure retry and user notification are not implemented.
