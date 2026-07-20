# Recover After an Unexpected AI Action

Status: **Draft - verify product labels and rollback behavior before publication**

Move quickly, but do not let an automatic rollback erase newer work or create a
second incident. Check what actually happened before restoring anything.

## Immediate containment

1. Stop the current run and any queued or scheduled actions.
2. Switch the integration to **Read Only** if the control is available.
3. Disconnect the affected integration in AgentKip, then revoke its token,
   installation, or session in the provider itself.
4. Protect affected branches, deployments, accounts, and devices from further
   changes.
5. If a credential may be exposed, rotate it from a trusted device and review
   recent provider activity.
6. Preserve minimal timestamps, action IDs, diffs, and provider audit events. Do
   not copy unrelated user content or secrets into a report.

## Assess the effect

- What exact repository, branch, environment, device, account, or provider changed?
- Was anything pushed, merged, deployed, published, messaged, purchased, deleted,
  or made public?
- Were permissions, workflows, secrets, signing settings, or security controls
  changed?
- Did an untrusted file, issue, webpage, message, or tool output influence the AI?
- Did the approval preview match the action that ran?
- Has anyone created legitimate work after the affected checkpoint?

## Restore safely

1. Prefer a new reviewed repair commit or provider-supported reversal over a
   history rewrite.
2. Compare the checkpoint/backup scope with the actual affected systems.
3. Restore in a non-production environment where possible.
4. Review the full repair, run the project's tests/build, and exercise the
   behavior before deployment.
5. Obtain required human/organization approvals before merging or publishing.
6. Monitor for recurrence and remove any persistence or queued action.

Checkpoints may not reverse remote pushes, merges, messages, publications,
payments, provider-side actions, credential exposure, device changes, or data
created after the checkpoint.

## Lost or compromised device/account

- Revoke AgentKip, Clerk, GitHub, AI-provider, and Noggin sessions/tokens from a
  trusted device.
- Rotate affected secrets and recovery codes.
- Review provider security/audit logs and account membership.
- Disable the self-hosted Noggin endpoint if its credentials or host are affected.
- Do not rely on deleting the AgentKip app to revoke server/provider access.

## Report an AgentKip issue

Contact `hello@agentkip.ai` with a non-sensitive summary, approximate time, app
version/build, and action/request ID if available. Do not send passwords, API
keys, recovery codes, full tokens, or unrelated repository content.

If the event involves immediate physical danger, financial theft, or another
emergency, contact the appropriate emergency, financial, provider, or law-
enforcement channel. AgentKip is not an emergency service.
