# Consequential Action Confirmation Copy

**Copy version:** 2026.07.15-draft.1

**Effective:** July 15, 2026

**Region:** United States

**Receipt event:** `consequential_action_decided`

Use this sheet for every action that requires confirmation regardless of permission mode: remote
push, pull-request merge, deployment, release, publication, external message, purchase, access-
control change, credential rotation, or device/security/network configuration.

## Confirmation sheet

**Navigation title:** Review action

**Heading:** Approve [ACTION_SHORT_NAME]?

**Requested by:** [AGENT_OR_MODEL] via [PROVIDER]

**Target:** [TARGET_TYPE] · [TARGET_CANONICAL_IDENTIFIER]

**Account/owner:** [OWNER_OR_ACCOUNT]

**Exact action:** [ACTION_DESCRIPTION]

**Expected effects:** [EXPECTED_EFFECTS]

**External side effects:** [EXTERNAL_SIDE_EFFECTS_OR_NONE]

**Estimated cost:** [COST_OR_NO_KNOWN_DIRECT_COST]

**Checkpoint/backup:** [CHECKPOINT_STATUS_AND_REFERENCE]

**Reversibility:** [REVERSIBILITY_AND_MANUAL_RECOVERY]

**Risk:** [RISK_TIER] · [RISK_REASONS]

**Warning:**

> AI can be wrong or manipulated by untrusted content. Approval authorizes only the exact target and
> effects shown here. Verify the target, authority, scope, cost, and recovery plan. Deny this request
> if anything is missing, unexpected, or unclear.

**Authority checkbox for a new or materially changed target, unchecked:**

> I confirm that I own or am authorized to direct this exact action on this target.

**Primary button:** Approve this action once

**Destructive-position secondary button:** Deny action

Do not use ambiguous labels such as **Yes**, **Continue**, or **OK**.

## Category-specific warning lines

- **Remote push or merge:** “This changes shared repository state and may trigger automation.”
- **Deploy or release:** “This can affect production users, availability, data, and provider cost.”
- **Publication or message:** “People outside AgentKip may receive this content. Sending may not be
  reversible.”
- **Purchase:** “Approving may create the displayed charge and related taxes or recurring terms.”
- **Access or credential change:** “This changes who or what can access the target and may invalidate
  existing sessions.”
- **Device/security/network change:** “This may affect privacy, connectivity, monitoring, or device
  recovery.”

## Blocked-action copy

**Heading:** AgentKip won’t perform this action

> [ACTION_SHORT_NAME] is blocked in this release because it involves [BLOCK_REASON]. Perform it
> manually outside AgentKip only if you have authority and understand the risk.

Blocked reasons include force-push/history rewrite, direct protected-branch write, repository
deletion, device wipe, credential extraction, security-control bypass, and unscoped production
operation. Do not offer an in-app bypass.

## Failure and race-condition copy

**Unknown scope:**

> AgentKip can’t verify the target, provider, requested capability, effects, or risk. Nothing ran.

**Action changed:**

> The action changed while you were reviewing it. Your prior decision does not apply. Review the new
> request.

**Approval expired:**

> This approval expired. Nothing ran. Request a new preview to continue.

**Approval not delivered:**

> Approval was not delivered, so AgentKip did not authorize the action.

**Execution state unknown:**

> AgentKip cannot verify whether the action ran. Check the target and do not retry until its state is
> known.

**Canceled:** Action canceled. No approval was sent.

**Denied:** Action denied.

**Approved:** Approved once. Verifying the result…

## Result and receipt copy

**Completed:**

> AgentKip reports that [ACTION_SHORT_NAME] completed. Verify the result in [TARGET_DISPLAY_NAME].

**Partially completed:**

> The action completed only in part: [COMPLETED_EFFECTS]. [FAILED_OR_UNKNOWN_EFFECTS]. Review the
> target before retrying or rolling back.

**Failed:**

> The action failed: [SAFE_ERROR_SUMMARY]. The target may still have changed. Verify it directly.

**Receipt action:** View action receipt

**Recovery action when available:** Review rollback steps

The receipt must include action ID, model/provider, exact target and account, requested effects,
external effects, cost representation, risk tier/reasons, permission mode, displayed-preview hash,
decision and timestamp, Terms/AUP versions, checkpoint/rollback reference, delivery status, result,
and verification status. Never store a secret value in a receipt.
