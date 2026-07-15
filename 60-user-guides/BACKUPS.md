# Back Up Before You Let AI Change Anything

Status: **Draft - verify product labels and recovery controls before publication**

AI can make a technically valid change that is still wrong for your project. It
can also misunderstand an instruction, overwrite data, expose a secret, or be
influenced by malicious text in a repository, file, webpage, or message. A model
approval or AgentKip checkpoint is not a substitute for a backup you control.

## Before connecting a system

1. Confirm you own the repository, device, app, account, data, or deployment, or
   have authority from the owner to connect and change it.
2. Back up important data to a separate, access-controlled location.
3. Test that you can restore the backup. A backup that has never been restored is
   only an assumption.
4. Protect default and release branches. Work on a new non-protected branch.
5. Remove secrets from files and logs. Use the provider's secret-management tools.
6. Limit the integration to only the repositories, devices, and capabilities
   needed for the current task.
7. Start in **Read Only**, then move to **Ask First** only when you are ready to
   review exact changes.

## Before approving a consequential action

- Read the exact target, files/resources, external side effects, and cost.
- Verify the branch, environment, device, account, and repository yourself.
- Review the complete diff or action preview, including deletions and permission
  changes.
- Confirm a current backup and a tested recovery path exist.
- Stop if the action is broader than your request or the preview is incomplete.
- Treat production deployment, publication, payment, external messages, access
  changes, credential changes, remote pushes, and device configuration as
  separate decisions.

## What a checkpoint can and cannot do

A checkpoint may help restore files or state captured by Noggin. It may not cover
remote systems, deleted repositories, messages already sent, published content,
payments, deployments, provider-side changes, credential exposure, device state,
or work created after the checkpoint. Review its exact scope before relying on it.

## Keep your recovery materials separate

Do not store your only backup, recovery code, signing key, password, or provider
token in the same repository, device, or account that an automated action can
change. Keep recovery access offline or in an independent protected account.

If an action goes wrong, stop new actions and follow the [recovery guide](/guides/recovery).
