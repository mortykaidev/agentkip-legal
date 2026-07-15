# Permission Modes and Confirmations

Status: **Draft - publication blocked until client and Noggin enforcement tests pass**

Permission modes set the maximum authority AgentKip may use. They do not prove
that a suggested action is correct, safe, lawful, or authorized by another person.

## Modes

### Read Only

AgentKip may inspect only the resources you selected. It must not write files,
push changes, deploy, publish, send messages, make purchases, change access, or
configure a device.

Use Read Only for unfamiliar repositories, audits, research, and any target where
you are unsure of your authority.

### Ask First

Ask First is the default. Before every mutation, AgentKip must show a durable
preview with the exact target, intended effects, important external side effects,
cost where known, checkpoint/backup information, and whether the action is
reversible. Nothing should run unless the matching request is approved.

If the request changes, expires, cannot be delivered, or no longer matches the
target, AgentKip must ask again or stop.

### Auto Apply

Auto Apply is limited to reversible edits inside an explicitly selected
repository on a non-protected branch. Enabling it requires a separate risk
acknowledgment. It is not blanket permission over your GitHub account, devices,
applications, deployments, or other services.

Do not use Auto Apply without a current backup, protected default branch, narrow
repository scope, and a plan to review every result before merge or release.

## Actions that always require a separate confirmation

- Remote push or pull-request merge.
- Deployment, release, publication, or external message.
- Purchase, paid resource, or other financial effect.
- Access-control, membership, credential, or secret change.
- Device, security, privacy, network, or account configuration.

## Actions blocked in the initial release

- Force-push or shared-history rewrite.
- Direct write to a protected/default branch.
- Repository deletion.
- Device wipe.
- Credential extraction.
- Security-control bypass.
- Unscoped production operation.

AgentKip must fail closed when the target, provider, permission, risk, or approval
cannot be identified. A model prompt saying `ask first` is not enforcement.

## Change or revoke access

Use **Legal & Privacy > Integrations and Permissions** to review and reduce access
after that screen ships. Also revoke access in the connected provider. A local
disconnect is not complete until the provider confirms token or installation
revocation.

## Release gate

The current permission mode must not be described publicly as enforced until
client and Noggin tests prove every write path follows these rules.
