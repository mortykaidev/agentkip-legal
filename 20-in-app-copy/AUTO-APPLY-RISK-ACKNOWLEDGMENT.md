# Auto Apply Risk Acknowledgment Copy

**Copy version:** 2026.07.15-draft.1

**Effective:** July 15, 2026

**Region:** United States

**Receipt event:** `auto_apply_risk_acknowledged`

## Enablement sheet

**Navigation title:** Auto Apply

**Heading:** Allow limited edits without asking each time?

**Scope:** [REPOSITORY] · [BRANCH]

**Allowed capability:** Reversible, repository-local file edits

**Duration:** [SESSION_OR_AUTHORIZATION_DURATION]

**Warning:**

> Auto Apply can change code and files without showing an approval for every edit. AI can introduce
> bugs, security issues, data loss, license problems, or changes you did not intend. A checkpoint is
> helpful but is not a complete backup.

**What Auto Apply does not authorize:**

**Always requires a separate action confirmation:**

- pushing to a remote, merging, deploying, releasing, or publishing;
- sending an external message or making a purchase;
- changing credentials, access controls, device settings, privacy settings, or network security.

**Remains blocked in the initial release:**

- writing directly to a protected branch;
- force-pushing, rewriting shared history, deleting a repository, wiping a device, extracting a
  credential, bypassing a security control, or performing an unscoped production operation.

Auto Apply never converts an always-confirm or blocked action into an unattended action.

**Acknowledgment checkbox, unchecked by default:**

> I understand the risks and authorize only reversible, repository-local edits in [REPOSITORY] on
> [BRANCH]. I have authority over this target, an independent recovery method, and responsibility for
> reviewing and testing changes before I merge, deploy, publish, or rely on them.

**Primary button:** Enable Auto Apply for this scope

**Secondary button:** Keep Ask First

**Footer:**

> Auto Apply does not waive AgentKip’s responsibility to stay within the displayed scope or its
> non-waivable product, privacy, and security obligations.

## Interaction rules

- Keep Ask First as the default.
- Never pre-check the acknowledgment.
- Do not permit Auto Apply without an explicit repository, non-protected branch, capability list,
  duration, and successful checkpoint/recovery check.
- Enabling Auto Apply for one repository or branch does not enable it elsewhere.
- Re-acknowledge when the repository, branch, capabilities, duration, risk policy, or legal-copy
  version changes.
- Automatically return to Ask First if scope cannot be verified, the branch becomes protected, the
  connection changes, authorization is revoked, or approval transport fails.

## Runtime status copy

**Active banner:** Auto Apply is active for [REPOSITORY] on [BRANCH].

**Action:** Turn off Auto Apply

**Scope blocked:**

> Auto Apply stopped because the target or branch is no longer within the approved scope. Ask First
> is now active.

**Recovery unavailable:**

> Auto Apply can’t start because AgentKip could not verify a checkpoint or recovery method.

## Receipt requirements

Record account identifier, repository canonical identifier, branch, protected-branch result,
capabilities, duration/expiry, checkpoint reference, authority receipt reference, Terms/AUP versions,
displayed-copy version, decision, locale, and timestamp. Do not record repository contents.
