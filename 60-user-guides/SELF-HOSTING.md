# Self-Hosting Noggin Safely

Status: **Draft - deployment-specific instructions require verification**

Self-hosting gives you control, but it also gives you operational responsibility.
Hayward Imagination Company LLC does not administer a Noggin server, network,
model-provider account, repository, device, or credential merely because you
connect it to AgentKip.

AgentKip remains responsible for accurately describing its client behavior and
for controls inside the AgentKip service. You remain responsible for systems and
accounts you operate or authorize.

## Minimum operating checklist

- Run a supported Noggin version and apply security updates promptly.
- Expose the service only through an authenticated, encrypted path. Do not place
  an unauthenticated gateway on the public internet.
- Use unique, revocable credentials and least-privilege service accounts.
- Keep model-provider, GitHub, signing, deployment, and device credentials out of
  source control and logs.
- Restrict administrative access and review it regularly.
- Define log, checkpoint, cache, conversation, diagnostic, and backup retention.
- Encrypt and test backups; keep recovery access separate from the server.
- Protect default branches, production deployments, devices, and external actions
  independently of model instructions.
- Monitor failed authentication, new integrations, approval bypasses, unusual
  tool actions, and unexpected outbound traffic.
- Maintain a shutdown/revocation path that works even if AgentKip is unavailable.

## AI providers

You choose provider accounts and models. Review each provider's privacy policy,
terms, data-use controls, retention, location, cost, and credential model before
use. A local Noggin does not make a request local if Noggin sends it to a remote
model provider.

Do not send data you are not authorized to disclose. Free-form prompts,
repositories, attachments, voice, and tool output can contain personal,
confidential, regulated, or third-party information.

## Updates and compatibility

- Read release notes and back up configuration before updating.
- Test permission modes, approval requests, checkpoints, revocation, deletion,
  and provider routing in a non-production environment.
- Confirm the AgentKip and Noggin versions are supported together.
- Do not weaken authentication or expose secrets to work around a version error.

## When to stop the service

Stop Noggin and revoke affected credentials if you see an unknown approval,
unexpected target, unauthorized action, lost device, leaked token, unexplained
outbound request, or provider/account compromise. Preserve minimal audit evidence,
then follow the [recovery guide](/guides/recovery).

## Release gate

The public guide must link to tested deployment documentation for supported
configurations. It must not promise that self-hosted data never reaches AgentKip
or a provider until runtime traces prove every path and optional feature.
