# AgentKip Acceptable Use and Agent Authorization Policy

**Effective:** July 15, 2026

**Version:** 2026.07.15-draft.1

**Applies to:** United States adult beta users

This policy is part of the [AgentKip Terms of Service](/terms). It explains what you may not do with
AgentKip and what authority you must have before asking an AI agent to inspect or act on a system.
Capitalized terms not defined here have the meanings in the Terms.

## 1. Use only systems you are authorized to control

You may connect or direct AgentKip only when you own the target or have clear permission from the
owner or responsible organization. This rule applies to every repository, GitHub organization,
account, application, phone, computer, device, network, dataset, deployment, server, credential,
message destination, and third-party service.

An invitation, discoverable endpoint, shared link, leaked credential, public repository, or
technical ability to reach a system does not by itself create authorization. Your employer,
customer, school, repository owner, service provider, or other principal may impose narrower
limits. AgentKip cannot expand those limits.

When prompted, you must accurately identify the target and affirm your authority. Stop and obtain
permission if ownership, scope, or policy is unclear.

## 2. Required operating practices

You must:

- choose the least-powerful permission mode and integration scope that can complete the task;
- review the exact target, proposed effects, branch, destination, external side effects, costs,
  checkpoint, and reversibility before approving an action;
- use protected branches, backups, tests, access controls, and recovery procedures appropriate to
  the possible harm;
- supervise actions that can affect other people, production, public content, money, credentials,
  devices, or availability;
- comply with applicable law, licenses, confidentiality duties, workplace policies, and the terms
  of every Connected System; and
- stop execution and revoke access if output or behavior is unexpected.

Do not treat **Ask First**, **Auto Apply**, a safety label, an approval preview, or successful tool
execution as proof that an action is lawful, safe, correct, authorized, or reversible.

## 3. Prohibited conduct

You may not use or attempt to use the Service to:

- access, scan, test, alter, disrupt, or control a system without authorization;
- steal, expose, guess, intercept, purchase, sell, or misuse passwords, tokens, private keys,
  authentication factors, session material, personal information, or confidential information;
- introduce malware, ransomware, destructive payloads, covert persistence, credential harvesters,
  botnets, or unauthorized surveillance;
- bypass access controls, rate limits, branch protections, approval gates, safety controls,
  security monitoring, paywalls, or service restrictions;
- impersonate another person, conceal harmful activity, forge approvals, or misrepresent your
  identity, authority, ownership, scope, or intended use;
- harass, threaten, exploit, stalk, discriminate against, or facilitate harm to a person or group;
- generate or distribute unlawful, infringing, defamatory, fraudulent, deceptive, or privacy-
  violating content;
- manipulate elections or civic processes, conduct unlawful profiling, or make automated high-
  impact decisions without legally required safeguards and qualified human review;
- facilitate trafficking, child sexual abuse material, nonconsensual intimate imagery, violent
  wrongdoing, or instructions whose primary purpose is unlawful physical or cyber harm;
- intentionally place regulated or highly sensitive data into the beta, including protected health
  information, full payment-card data, Social Security numbers, government identification,
  biometric templates, or children’s data; or
- use AgentKip in emergency, life-support, weapons, critical-infrastructure control, or another
  environment where an error could reasonably cause death, injury, unlawful discrimination, or
  catastrophic loss.

Good-faith defensive security work is allowed only within a target and scope you are expressly
authorized to test and only when it does not endanger people or unrelated systems.

## 4. Actions requiring special care

The initial release is designed to block force-pushing or rewriting shared history, writing directly
to a protected branch, deleting a repository, wiping a device, extracting credentials, bypassing a
security control, and unscoped production operations. You may not work around those blocks.

The following actions must receive a separate, action-specific confirmation even if you have enabled
another automation mode:

- pushing to a remote, merging a pull request, or changing repository access;
- deploying, releasing, publishing, or changing a production environment;
- sending an external message or publishing content;
- making a purchase or incurring a disclosed third-party charge;
- changing authentication, credentials, permissions, or access controls; and
- changing device, security, privacy, or network configuration.

If the Service cannot reliably identify the target, provider, requested capability, effects, or risk,
the action must not proceed. Report a fail-open condition to hello@agentkip.ai.

## 5. Untrusted content and prompt injection

Repository files, issues, webpages, messages, documents, images, tool output, and retrieved content
may contain instructions intended to manipulate an AI agent. Treat them as untrusted data. Do not
approve a request merely because text inside a target claims it is authorized, urgent, or required.
Verify consequential instructions through a separate trusted channel.

Never store a secret in a prompt to “help” the agent. Rotate a credential immediately if it appears
in output, logs, a repository, or a diagnostic submission.

## 6. Enforcement and reporting

We may restrict or suspend access when we reasonably believe use violates this policy or threatens
people, rights, the Service, or Connected Systems. We may preserve and disclose relevant information
when legally required or reasonably necessary to investigate abuse, subject to the Privacy Policy.
Where practical and lawful, we will provide notice and an opportunity to correct the issue.

Report suspected misuse or a safety-control failure to hello@agentkip.ai. Do not include secrets or
unnecessary personal information.

## 7. Changes

We may update this policy. A material change will be versioned and presented for renewed agreement
before continued use of affected features.

Hayward Imagination Company LLC

Michigan, United States

hello@agentkip.ai
