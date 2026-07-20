# Legal and Compliance Review Triggers

Status: **Active internal control**

Owner: Brandon

## Trigger workflow

When a trigger occurs:

1. Pause the affected release, region, provider, or capability; unaffected work
   may continue.
2. Record the proposed change, users, systems, data, providers, regions, revenue,
   and risk in the facts-and-decisions record.
3. Update the data flow, provider register, retention, consent, deletion,
   authorization, incident, App Privacy, manifest, and public-copy impact.
4. Identify current official rules and the appropriate reviewer: product,
   security, privacy, tax/accounting, accessibility, App Store, insurance, or
   qualified legal review.
5. Record Brandon's decision, mitigations, evidence, and approval before enabling
   the change.

## High-priority triggers

The approved plan recommends qualified review, but does not automatically require
outside counsel, before:

- Admitting or knowingly serving anyone under 18.
- Soliciting, inferring, or routinely processing health, medical, financial,
  credit, insurance, biometric, genetic, precise-location, education, employment,
  government-ID, or similarly regulated/sensitive data.
- Entering enterprise, business-associate, data-processing, SLA, indemnity,
  security-addendum, procurement, public-sector, school, healthcare, or financial-
  institution agreements.
- Enabling distribution in the EEA, United Kingdom, Ireland, New Zealand, or a new
  country not covered by an activated checklist.
- Allowing materially broader autonomous authority over repositories, production,
  devices, money, communications, publication, access controls, credentials,
  physical systems, or safety-relevant decisions.
- Receiving a credible demand letter, lawsuit, regulator inquiry, App Store legal
  escalation, major consumer complaint, or insurance notice.

## Product and data triggers

- Company-hosted Noggin or company retention of conversations/repository content.
- New AI/model provider, routing model, training/model-improvement use, fine-
  tuning, evaluation corpus, or human review of user content.
- Advertising, tracking, targeted marketing, sale/share of data, data-broker
  activity, affiliate attribution, or third-party analytics.
- Public profiles, user-to-user communication, shared/public content, moderation,
  marketplace, discovery/search, or creator monetization.
- Voiceprint, face/hand/body, camera/environment scanning, contacts, location,
  background recording, or persistent device fingerprinting.
- Automated decisions with legal, financial, employment, housing, education,
  healthcare, insurance, access, or similarly significant effects.
- API, SDK, plugin marketplace, third-party developer access, delegated agents,
  or external action webhooks.
- Material retention increase, new data recipient/location, new backup/logging
  system, or weaker deletion/revocation path.

## Commercial and corporate triggers

- Paid App Store subscription, direct web billing, credits/tokens, metered model
  charges, marketplace payments, refund-policy change, or pricing outside the US.
- Business/entity name, ownership, merger, acquisition, investment, asset sale,
  insolvency, or assignment of user agreements/data.
- New trademark/brand, open-source licensing model, commercial model weights, or
  third-party content licensing.
- Warranty, uptime, support, professional-service, custom-development, reseller,
  or partner commitments.
- Material revenue/user-count/data-volume thresholds relevant to state, federal,
  or regional obligations.

## Security and incident triggers

- Confirmed personal-data breach, credential exposure, provider compromise,
  unauthorized tool action, approval bypass, destructive action, or prompt-
  injection incident with external effect.
- A new privileged permission, broad organization installation, protected-branch
  access, device administration, code signing, deployment, or payment capability.
- Removal or weakening of ask-first, checkpoint, least-privilege, audit, backup,
  revocation, or fail-closed controls.
- A material public security/privacy claim can no longer be proven.
- A provider changes its terms, subprocessors, training use, retention, location,
  breach obligations, or deletion behavior.

## Legal-document triggers

Require a material-change assessment when a document adds or changes:

- Data categories, purposes, recipients, transfers, or retention.
- Provider-specific consent or user-control consequences.
- Eligibility, payment, cancellation, ownership, license, warranty, liability,
  indemnity, governing law, forum, or dispute rights.
- Autonomous capabilities, prohibited uses, or responsibility allocation.
- Account deletion, export, diagnostics, or security promises.

Material changes require a new version/hash, changelog entry, publication sync,
and re-acceptance where the changed obligation or risk warrants it.

## Evidence of closure

A trigger closes only when the decision record names the scope, current sources,
reviewer, implementation changes, tests, public documents, regional/Apple impact,
remaining risk, and Brandon's dated approval.
