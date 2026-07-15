# Privacy Acknowledgment Copy

**Copy version:** 2026.07.15-draft.1

**Effective:** July 15, 2026

**Region:** United States

**Receipt event:** `privacy_notice_acknowledged`

## Screen copy

**Navigation title:** Privacy

**Heading:** Understand where your data can go

**Body:**

> AgentKip can process information on this iPhone, through your configured gateway and self-hosted
> Noggin service, through an AI provider you choose, and through connected services such as GitHub.
> Hayward-operated account, website, billing, support, security, and diagnostic systems may also
> receive the information described in the Privacy Policy.

**Current beta behavior callout:**

> When a gateway is configured, flight-recorder metadata uploads automatically. Full-content capture
> and content-segment upload are off by default, but metadata events can include software-redacted
> snippets of up to 80 characters from prompts and replies, and those snippets may upload
> automatically. Redaction may not catch every sensitive value. Device-context sharing is on by
> default and can include a stable device identifier, raw hardware identifier, device name, hardware
> and capabilities, OS and AgentKip versions, locale, and time zone. These are current beta behaviors
> and release blockers, not the intended public-release defaults.

**Provider callout:**

> Before personal information is sent to a third-party AI provider, AgentKip will identify the
> provider, categories, purpose, and policy and ask for separate permission. You can decline.

**Acknowledgment checkbox, unchecked by default:**

> I have read and acknowledge the AgentKip Privacy Policy (version [PRIVACY_VERSION]).

**Link:** `Read Privacy Policy` → `[PRIVACY_URL]`

**Primary button:** Acknowledge and continue

**Secondary button:** Exit setup

**Footer:**

> This acknowledges receipt of the Privacy Policy. It is not consent to every optional data use.
> Optional AI-provider and integration permissions are requested separately.

## Interaction rules

- Never label this checkbox “I agree to the Privacy Policy.”
- Do not pre-check it or bundle it with Terms assent, marketing, analytics, or provider consent.
- Disable the primary button until the box is checked and the current document is available with a
  matching version and hash.
- If product defaults change before publication, replace the current-behavior callout and increment
  this copy version before shipping.

## Material update copy

**Heading:** Our privacy practices have changed

> Please review the updated Privacy Policy (version [PRIVACY_VERSION]). Where a change requires your
> permission, AgentKip will ask separately before using the affected feature.

**Checkbox:** I have read and acknowledge the updated Privacy Policy.

**Primary button:** Acknowledge

**Secondary button:** Not now

## Error copy

**Policy unavailable:**

> We can’t verify the current Privacy Policy. Try again before continuing.

**Receipt save failed:**

> Your acknowledgment could not be recorded. Nothing was accepted. Try again.

## Receipt requirements

Record account identifier, event name, Privacy Policy identifier/version/URL/SHA-256 hash, displayed-
copy version, locale, timestamp, and decision. Do not store User Content in the receipt.
