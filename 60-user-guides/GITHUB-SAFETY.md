# Use AgentKip Safely with GitHub

Status: **Draft - verify installation scopes and enforced actions before publication**

Only connect repositories and organizations you own or are authorized to access.
Your employer, client, open-source project, or organization may require approval
before code or metadata is sent to an AI provider.

## Safer setup

1. Install the GitHub App only on the repositories needed for the task. Prefer
   selected repositories over organization-wide access.
2. Review every requested permission. Do not grant write access for a read-only
   task.
3. Protect default, release, and production branches. Require pull requests,
   review, status checks, and appropriate approval rules.
4. Create a dedicated non-protected working branch.
5. Back up important work and verify restore access outside the connected account.
6. Keep secrets out of repositories, issue text, pull-request text, diffs, and
   diagnostic reports.
7. Begin in **Read Only** or **Ask First**.

## Review every change

- Check the repository, organization, branch, base branch, and commit range.
- Read additions and deletions, generated files, dependency changes, workflows,
  permissions, and configuration.
- Run the project's own tests and build. Passing tests do not prove the behavior
  is correct; exercise the changed feature.
- Review security-sensitive files such as CI workflows, package scripts,
  entitlements, infrastructure, deployment configuration, and agent instructions.
- Never approve a remote push or merge because an AI says its own work is safe.

## Treat repository content as untrusted

Issues, comments, READMEs, source files, web pages, test fixtures, and tool output
can contain instructions designed to manipulate an AI. AgentKip should not treat
that content as higher-priority authorization. Stop if a proposed action asks for
secrets, broader access, disabled protections, hidden output, or an unrelated
external action.

## Token and installation hygiene

- Use least privilege and the shortest practical token lifetime.
- Do not paste GitHub tokens into chat, source, logs, support reports, or this
  documentation repository.
- Reconnect explicitly if additional scope is genuinely required.
- Remove unused installations and tokens in GitHub, not just in AgentKip.
- Review GitHub security logs after an unexpected action.

## If something goes wrong

1. Stop AgentKip/Noggin actions and queued work.
2. Revoke the GitHub App installation or token in GitHub.
3. Protect affected branches and rotate any exposed secret.
4. Preserve the relevant audit trail without copying unrelated repository content.
5. Restore through a new reviewed change; do not overwrite other people's later
   work with an unexamined rollback.
6. Follow the [recovery guide](/guides/recovery) and contact `hello@agentkip.ai` for an
   AgentKip security or privacy issue.

GitHub's permissions and terms still apply independently of AgentKip.
