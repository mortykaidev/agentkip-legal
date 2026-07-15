# Placement Matrix

This matrix defines source ownership and consumer placement. Canonical files remain private;
consumer repositories receive only validated exports. A link or copied file is not authoritative.

## Public legal set

| Manifest ID | Canonical source | Website route | In-app placement | Acceptance |
|---|---|---|---|---|
| `privacy-policy` | `10-public-legal/PRIVACY-POLICY.md` | `/privacy` | Onboarding link; Settings → Legal & Privacy | Separate acknowledgment |
| `terms-of-service` | `10-public-legal/TERMS-OF-SERVICE.md` | `/terms` | Onboarding link; Settings → Legal & Privacy; receipt history | Explicit unchecked agreement |
| `acceptable-use-policy` | `10-public-legal/ACCEPTABLE-USE-POLICY.md` | `/acceptable-use` | Terms acceptance disclosure; Settings | Explicit with Terms |
| `ai-transparency-and-safety` | `10-public-legal/AI-TRANSPARENCY-AND-SAFETY.md` | `/ai` | Onboarding summary; provider-consent sheet; Settings | Explicit acceptance incorporated with Terms; provider transfer consent remains separate |
| `data-responsibility` | `10-public-legal/DATA-RESPONSIBILITY.md` | `/data-responsibility` | Authority and Auto Apply disclosures; Settings | None; target authority and Auto Apply decisions remain separate |
| `data-deletion` | `10-public-legal/DATA-DELETION.md` | `/data-deletion` | Settings → Legal & Privacy → Delete account/data | None; action confirmation is separate |
| `security` | `10-public-legal/SECURITY.md` | `/security` | Settings link | None |
| `subprocessors` | `10-public-legal/SUBPROCESSORS.md` | `/subprocessors` | Privacy and provider-consent links | None |
| `accessibility` | `10-public-legal/ACCESSIBILITY.md` | `/accessibility` | Settings link | None |
| `legal-notice` | `10-public-legal/LEGAL-NOTICE.md` | `/legal-notice` | Settings link | None |

Every route belongs in the website footer, sitemap, and legal registry. Privacy and Terms URLs also
belong in App Store Connect metadata. The app registry includes IDs, versions, URLs, hashes,
material-change flags, and acceptance modes; the app may cache an accepted version for retention,
but it may not silently substitute a newer web page for the version the user accepted.

## In-app consent and authorization copy

| Manifest ID | Canonical source | Required surface | Receipt/event |
|---|---|---|---|
| `age-and-terms-assent` | `20-in-app-copy/AGE-AND-TERMS-ASSENT.md` | Every fresh-install, signup, invitation, pairing, and acceptance-required deep link before use | Age attestation + exact Terms/AUP/incorporated AI-notice IDs, versions, hashes + decision |
| `privacy-acknowledgment` | `20-in-app-copy/PRIVACY-ACKNOWLEDGMENT.md` | Same gate, separately selectable from Terms | Privacy version/hash + acknowledgment |
| `ai-provider-consent` | `20-in-app-copy/AI-PROVIDER-CONSENT.md` | Just before first transfer to each provider and after material disclosure change | Provider, categories, purpose, policy, consent version, decision |
| `authority-attestation` | `20-in-app-copy/AUTHORITY-ATTESTATION.md` | Before connecting each repository, account, device, app, deployment, or service class | Target type/ID, scopes, recipient/provider, data categories, purpose, privacy-policy URL, copy version, authority decision, and separate transfer-permission decision (or verified no transfer) |
| `auto-apply-risk-acknowledgment` | `20-in-app-copy/AUTO-APPLY-RISK-ACKNOWLEDGMENT.md` | Before Auto Apply can be enabled and after material permission-policy change | Target scope, policy version, decision |
| `action-confirmation` | `20-in-app-copy/ACTION-CONFIRMATION.md` | Every always-confirm or consequential action | Action ID, target, effect, risk, cost/side effects, checkpoint, decision, result |

Consent copy is an app resource export, not a website page. Provider consent and per-action
authorization remain separate from Terms acceptance.

## Apple submission and internal evidence

| Package | Placement | Publication rule |
|---|---|---|
| `30-apple-submission` | App Store Connect worksheets, review notes, privacy-manifest inventory, deletion demonstration, encryption/export record | Private; manually transpose only after code and manifest reconciliation |
| `40-internal-compliance` | Operational record for data flow, retention, providers, consent receipts, deletion/revocation, and incidents | Private only; never copied to the public website or app |
| `50-regional` | Region activation checklists | Private and `inactive` until every region gate is approved |
| `60-user-guides` | `/guides/*`, support links, and contextual Settings help | Export after claims and procedures are verified; no legal acceptance |
| `90-future-review` | Review triggers and unresolved owner decisions | Private only |

## Consumer integration ownership

| Consumer | Integration contract | Required verification |
|---|---|---|
| `mortykaidev/agentkip-site` | Import website export content and `legal-documents.json`; keep routes stable | Build, link, sitemap/footer, accessibility, responsive, hash-parity tests |
| `mortykaidev/kai` AgentKip target | Bundle app registry and approved in-app copy; implement versioned receipt and legal center | Unit/UI tests plus build-and-run on the required iOS 27 simulator |
| Other Apple targets | Consume only documents relevant to their bundle; maintain independent privacy-manifest inventory | Separate product PR and bundle inspection |
| Noggin / `kai-core` | Consume authorization and consent contracts, not public markdown | Approval/deny, timeout, mismatch, revocation, receipt, and rollback integration tests |

Website legal-page work must not begin on top of an overlapping in-flight PR. At baseline, website
draft PR #3 claims the existing Privacy, Terms, and Security page files; resolve that ownership gate
before integration.
