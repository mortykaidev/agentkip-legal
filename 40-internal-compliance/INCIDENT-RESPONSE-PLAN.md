# Privacy and Security Incident Response Plan

Status: **Internal baseline - exercise and contacts BLOCKED**

Public intake: `hello@agentkip.ai`

## Goals

- Protect affected people and stop unauthorized access or harmful actions.
- Preserve trustworthy evidence without collecting unnecessary user content.
- Revoke exposed credentials and contain autonomous capabilities quickly.
- Assess notification duties by affected person and jurisdiction.
- Communicate accurately; never minimize or speculate.

## Roles

| Role | Responsibility | Named backup/contact |
|---|---|---|
| Incident commander | Severity, containment, decisions, closure | BLOCKED |
| Security/engineering lead | Technical triage, evidence, remediation | BLOCKED |
| Privacy lead | Data/jurisdiction assessment and notifications | BLOCKED |
| Communications lead | User, provider, Apple, and public messaging | BLOCKED |
| Service owners | Clerk, Neon, Stripe, Vercel, GitHub, AI providers, Noggin | BLOCKED |

Do not launch until an out-of-band contact path and backup are stored in an
approved private operations system. Do not put phone numbers, secrets, or home
addresses in this repository.

## Severity

- **SEV-1:** Active credential compromise, destructive/unauthorized tool actions,
  broad personal-data exposure, production takeover, or credible ongoing harm.
- **SEV-2:** Confirmed limited unauthorized access/disclosure, approval bypass,
  provider misrouting, or sensitive diagnostics exposure without broad takeover.
- **SEV-3:** Contained suspected event, control failure without confirmed exposure,
  or low-impact data integrity/availability event.
- **SEV-4:** Security/privacy defect or near miss with no incident evidence.

Severity can rise as evidence develops. Uncertainty is not a reason to delay
containment.

## First response

1. Open an incident ID, establish an incident commander, and restrict access to
   the working record.
2. Preserve timestamps, versions, configurations, audit events, and minimal
   relevant logs. Do not copy whole user repositories or conversations by default.
3. Contain: disable affected routes, stop queued actions, revoke tokens, rotate
   company credentials, and isolate compromised providers/hosts.
4. Protect user-controlled systems: tell affected users what credentials or
   integrations to revoke without claiming control over their repositories,
   apps, phones, devices, or provider accounts.
5. Identify data categories, people, jurisdictions, recipients, encryption,
   persistence, actor, time window, and likely consequences.
6. Contact affected providers through verified security channels and preserve
   case identifiers.
7. Determine regulator, Apple, contractual, law-enforcement, and affected-user
   notification duties using current rules; record the decision and deadline.
8. Issue accurate updates with known facts, protective actions, uncertainty, and
   next-update timing.

## AI and automation incident checks

- Was an approval required, displayed accurately, and matched to the executed
  action/target?
- Did read-only or ask-first mode fail open?
- Did prompt injection from a repository, file, webpage, message, or tool output
  influence the action?
- Did the model/provider receive data outside the disclosed scope?
- Did a checkpoint exist, and can rollback reduce harm without overwriting later
  user work?
- Did the action affect a protected branch, deployment, publication, external
  message, purchase, permission, credential, or device?
- Are similar queued or scheduled actions still capable of execution?

## Notification record

For each jurisdiction/provider, record the applicable rule, decision maker,
awareness time, deadline, threshold analysis, recipient, delivery proof, and final
notice. Never invent a universal deadline: notification triggers and time limits
vary, and inactive regional checklists must be consulted if affected people are
present there.

## Recovery and closure

- Remove persistence, patch the root cause, rotate affected credentials, and
  validate least privilege.
- Test the fix, approval gates, deletion/revocation, and monitoring in a safe
  environment.
- Restore service gradually with explicit owner approval.
- Provide affected-user remediation where appropriate.
- Write a blameless post-incident review covering timeline, impact, controls that
  failed, corrective owners/dates, and evidence of completion.
- Update the claim matrix, provider register, retention schedule, public notices,
  App Privacy answers, and future-review triggers when facts changed.

## Release blockers

1. Operational roles and out-of-band contacts are not assigned.
2. Provider escalation paths and log-preservation capabilities are incomplete.
3. No tabletop exercise has validated this plan.
4. Notification-decision support has not been prepared for the launch footprint.
5. Approval-bypass and provider-misrouting detection are not demonstrated.
