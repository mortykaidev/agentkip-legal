# Age Rating and App Review Notes

Status: **BLOCKED - questionnaire and review environment not verified**

Release posture: United States, adults-only beta

## Age rating

AgentKip's Terms require users to be at least 18. App Store Connect must therefore
use an age-rating override that does not conflict with that contractual minimum,
even if Apple's questionnaire calculates a lower rating. Apple currently provides
an `Override to Higher Age Rating` path and directs developers whose EULA has a
higher minimum age to use an appropriate override.

Candidate submission choice: **18+ override**, subject to the region-specific
result displayed by App Store Connect.

Do not select Kids Category. Do not describe the app as suitable for children.

### Questionnaire evidence checklist

- [ ] Inventory unrestricted web access, links, and browsing tools.
- [ ] Inventory messaging, user-generated content, and public-sharing features.
- [ ] Assess whether open-ended AI output can expose mature, violent, sexual,
      profane, medical, substance-related, or other rated content.
- [ ] Record implemented parental, content-filtering, reporting, and blocking
      controls; do not claim controls that exist only in prompts.
- [ ] Inventory gambling, contest, loot-box, advertising, and purchase features.
- [ ] Save the completed questionnaire and region-specific ratings as evidence.
- [ ] Verify the Terms, onboarding age gate, metadata, and product page all agree.

## App Review notes template

Replace every bracketed item with verified release information. Bracketed text
must never be submitted.

> AgentKip is an adults-only AI client that connects to a user-controlled Noggin
> service and user-selected integrations. Reviewers can use [review account or
> approved no-account flow] and [review Noggin endpoint/environment].
>
> To reach the primary experience: [exact steps]. To review AI-provider consent:
> [exact steps]. To review GitHub permission modes and an approval card: [exact
> steps]. To initiate account deletion: Settings > Legal & Privacy > Delete
> Account, then [verified completion behavior].
>
> The app does not require access to the reviewer's personal GitHub repositories,
> devices, or paid AI-provider credentials. [Describe seeded review data and
> credentials supplied through App Store Connect.]
>
> AgentKip requires users to be at least 18 and uses Apple's Standard EULA plus
> AgentKip service Terms. The age rating is overridden accordingly.

## Review-environment gates

- [ ] Stable reviewer account or account-free review path.
- [ ] Stable Noggin endpoint with non-personal seeded data.
- [ ] No dependency on Brandon's home network, personal devices, repositories,
      credentials, or residential address.
- [ ] Every primary feature works without requiring a reviewer to spend money.
- [ ] Permission denials and unavailable integrations fail with useful UI.
- [ ] Legal acceptance, provider consent, action approval, diagnostics controls,
      and account deletion are demonstrable.
- [ ] Backend and website remain available throughout expected review.

## Release blockers

1. The age questionnaire has not been completed from the release feature set.
2. A reproducible non-personal review environment is not evidenced.
3. Onboarding does not yet enforce the 18+ and versioned legal gates.
4. Account deletion cannot yet be demonstrated.
5. Approval behavior is not yet proven as enforced rather than prompt-only.

Source: [Set an app age rating](https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating)
