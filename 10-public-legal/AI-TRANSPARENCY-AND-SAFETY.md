# AgentKip AI Transparency and Safety Notice

**Effective:** July 15, 2026

**Version:** 2026.07.15-draft.1

**Applies to:** United States adult beta users

AgentKip uses artificial intelligence to interpret requests, generate content, inspect information,
and coordinate tools. This notice describes what that means and how to use those capabilities
responsibly. It supplements the [Terms](/terms), [Acceptable Use Policy](/acceptable-use),
[Privacy Policy](/privacy), and [Data Responsibility Guide](/data-responsibility).

## 1. AI is not a person or professional

AI responses are generated from patterns in data and context. They are not statements from a human
employee and do not show consciousness, intent, professional judgment, or guaranteed understanding.
AgentKip may sound confident while being wrong.

Do not rely on AgentKip as a medical, legal, financial, tax, employment, housing, insurance, credit,
emergency, or safety professional. Qualified human review is required before using output for a
high-impact decision or any decision affecting another person’s rights or opportunities.

## 2. Providers and data flow

AgentKip may use an AI provider selected by you or configured through your self-hosted Noggin
environment. Before personal information is first sent from the app to a third-party AI provider,
the app will show:

- the provider’s name;
- the categories of information to be transmitted;
- why the information is needed;
- a link to relevant provider privacy information; and
- whether declining disables the requested feature.

That provider-specific permission is separate from accepting the Terms. You can decline or later
revoke it. A provider may store, review, or use information according to its own terms, account
settings, and contract. Hayward does not use User Content to train or improve a Hayward model, but
that promise does not rewrite an independent provider’s terms.

That no-company-training statement is a launch commitment. Publication remains blocked until the
release’s dependencies, provider settings and contracts, data routes, and operations verify it.

## 3. Known limitations

AI output may be:

- inaccurate, outdated, incomplete, inconsistent, or fabricated;
- insecure, vulnerable, destructive, or incompatible with your environment;
- biased or inappropriate;
- substantially similar to protected or third-party material;
- based on misunderstood context, permissions, costs, or intent; or
- manipulated by hidden or visible instructions in files, repositories, webpages, messages, images,
  retrieved results, or tool output.

Memory and context can be missing, truncated, stale, or associated with the wrong task. A preview
can omit downstream behavior. A reversible-looking action may have irreversible external effects.

## 4. Permission modes are risk controls, not guarantees

**Read Only** is intended to prevent mutations. **Ask First** requires approval before a proposed
mutation. **Auto Apply** is limited to a separately acknowledged class of reversible repository-
local edits. Certain consequential actions always require confirmation, and certain destructive
actions are blocked.

These controls reduce risk but cannot prove correctness, legality, ownership, authority, or complete
reversibility. You remain responsible for selecting the mode, reviewing what is shown, maintaining
backups, testing results, and supervising use within your authority. AgentKip remains responsible for
its own product behavior and legal obligations; it cannot hide an undisclosed or materially broader
action behind your approval.

## 5. A safe operating routine

Before an agent acts:

1. Confirm that you own or are authorized to control the exact target.
2. Remove secrets and unnecessary personal or regulated information.
3. Use Read Only first and grant the smallest repository and capability scope.
4. Treat repository, web, message, file, and tool content as potentially hostile.
5. Read the proposed effects, destination, cost, external side effects, checkpoint, and rollback
   information.
6. Deny ambiguous, unexpected, unscoped, or high-impact requests.
7. Back up important data, work on a non-protected branch, test in a non-production environment,
   and review the resulting diff or action log.

After an action, verify the target directly. An “action complete” message is not independent proof
that the desired state is correct.

## 6. Stop conditions

Stop the agent, deny pending requests, disconnect integrations, and rotate affected credentials if:

- the target or scope changes unexpectedly;
- the agent requests a secret or broader permission without a clear need;
- a file or webpage instructs the agent to ignore you or bypass safeguards;
- a preview does not match the proposed effect;
- an approval appears after you canceled or for a different action;
- the agent attempts a protected, destructive, financial, public, or production action without the
  required confirmation; or
- output exposes confidential or personal information.

Preserve non-sensitive evidence and report a safety-control or security failure to
hello@agentkip.ai.

## 7. Beta status

AgentKip is experimental software. Safety controls, provider behavior, and model capabilities may
change. A material change to provider data sharing or authorization behavior will require an updated
disclosure and, where appropriate, renewed consent or agreement.

Hayward Imagination Company LLC

Michigan, United States

hello@agentkip.ai
