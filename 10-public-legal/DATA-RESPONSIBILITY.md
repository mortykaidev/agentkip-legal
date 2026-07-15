# AgentKip Data and Connected-System Responsibility Guide

**Effective:** July 15, 2026

**Version:** 2026.07.15-draft.1

**Applies to:** United States adult beta users

AgentKip can interact with data and systems that Hayward does not own or administer. This guide
explains the practical boundary between your responsibilities, Hayward’s responsibilities, and the
responsibilities of independent providers. It supplements the [Terms](/terms) and does not remove a
right or duty that cannot lawfully be changed.

## 1. Systems you control

You are responsible for your repositories, organizations, branches, accounts, apps, phones,
computers, devices, networks, credentials, data, deployments, servers, self-hosted Noggin instance,
and third-party subscriptions. Before connecting one, confirm you own it or have permission to
control it.

You decide what to connect, what information to provide, what provider to use, which permission mode
to enable, and which displayed actions to approve. You are responsible for keeping appropriate
backups, access controls, protected branches, recovery procedures, tests, and human review.

## 2. Systems Hayward controls

Hayward is responsible for the AgentKip software and Hayward-operated account, website, and service
components, including:

- describing material data uses and provider disclosures accurately;
- requesting consent and authorization where required;
- applying reasonable safeguards to information Hayward controls;
- honoring the permission and deletion behavior the product promises;
- not materially exceeding the target and scope presented for approval; and
- correcting or disclosing verified product defects and security issues as appropriate.

An approval does not excuse a hidden action outside the displayed scope, and a disclaimer does not
eliminate Hayward’s non-waivable privacy, security, consumer-protection, or product obligations.

## 3. Independent and user-directed services

Hayward-selected service providers, including Clerk, Neon, Vercel, and Stripe if activated, operate
under their own service terms but remain part of Hayward’s vendor-management and privacy
responsibility for information Hayward controls. Hayward must verify and disclose their roles and
cannot shift those obligations to you.

GitHub, user-selected AI providers, Apple services, a self-hosted Noggin instance, and other systems
you independently select or operate have their own terms and privacy practices. Hayward cannot
secure, update, back up, restore, or delete information inside an independently controlled system
merely because AgentKip can connect to it.

Review each service’s pricing, retention, model-training settings, security, data location, license,
and deletion controls. Your choice of provider can materially change risk.

## 4. Minimum data practices

- Do not paste passwords, access tokens, private keys, recovery codes, or authentication cookies
  into prompts. Use designated secure authorization flows.
- Grant the fewest repositories and capabilities required and revoke them when finished.
- Keep confidential or personal information out of prompts and diagnostics unless it is necessary,
  authorized, disclosed, and appropriate for every receiving provider.
- Do not use this beta for protected health information, full payment-card data, Social Security
  numbers, government identification, biometric templates, children’s data, or another regulated
  workload.
- Inspect repository history, generated files, logs, screenshots, output, and action receipts for
  accidentally exposed secrets.
- Rotate a credential immediately if it is revealed to an unintended person, provider, log, output,
  repository, or support submission.

## 5. Repositories and software

Use a non-protected branch and a clean working tree when possible. Preserve an independent backup or
remote recovery point. Review diffs for security, licenses, tests, generated files, build settings,
secrets, migrations, and destructive changes before merging or deploying.

An agent may write syntactically valid code that is insecure, incompatible, unlicensed, or wrong.
Passing tests are evidence only for what those tests cover. You decide whether to ship or rely on
the result.

## 6. Phones, devices, and local networks

Connect only devices you own or are authorized to administer. Device names, hardware identifiers,
capabilities, locale, and network context can be identifying. Review device-context and diagnostic
settings, limit local-network exposure, protect the gateway, and do not approve a configuration
change you cannot reverse.

Never use AgentKip to wipe a device, weaken device security, disable monitoring, expose a network,
or alter a device belonging to someone else. Initial-release safeguards blocking these actions must
not be bypassed.

## 7. Backups and recovery

A checkpoint or rollback reference is helpful but is not a complete backup. External services may
have already received a message, accepted a payment, changed access, deployed code, invalidated a
credential, or triggered an irreversible process.

Before consequential work, maintain a recovery method that does not depend on AgentKip, test it,
and know who can restore service. After an action, verify state in the target system itself.

## 8. Costs and external effects

AI providers, hosting platforms, GitHub products, cloud tools, cellular data, and other services may
charge you. Review displayed cost information, but do not assume it captures every downstream fee.
Set provider budgets and alerts where available. You are responsible for charges you knowingly
incur or authorize, except charges caused by hidden or materially out-of-scope product conduct.

## 9. Deletion boundaries

Deleting an AgentKip account or local app data does not automatically delete a repository, branch,
deployment, message, file, provider record, self-hosted database, device backup, or other copy
controlled elsewhere. Disconnect and delete data separately in each relevant system. See
[Data Deletion](/data-deletion).

## 10. If something goes wrong

Stop pending actions, disconnect affected integrations, preserve non-sensitive evidence, rotate
credentials, restore from a trusted backup, and contact the relevant provider or administrator.
Report an AgentKip security or authorization failure to hello@agentkip.ai without including secrets.
