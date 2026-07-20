# Release Blockers

Baseline status: **blocked for legal publication, external TestFlight, and App Store submission**

`P0` blocks every external release. `P1` blocks the affected feature or public claim. An owner
closes a blocker only with linked code/document PRs and verification evidence; prose alone cannot
close a technical control.

| ID | Priority | Gate | Closure evidence | Status |
|---|---:|---|---|---|
| `RB-001` | P0 | Canonical launch sources exist, have no forbidden content, and have verified hashes/versions/publication commits. | `validate --release` and approved manifest diff | Open |
| `RB-002` | P0 | Existing website Privacy, Terms, and Security contradictions are replaced; all ten stable legal routes, footer, and sitemap work. | Website PR, build, link/accessibility/responsive tests, export hash parity | Open |
| `RB-003` | P0 | Website draft PR #3 overlap is resolved before legal-page editing. | PR #3 merged/closed or owner-approved claim handoff | Open |
| `RB-004` | P0 | Fresh-install, signup, invitation, pairing, and deep-link paths require current 18+/Terms/AUP/privacy assent before use. | Acceptance coordinator unit/UI tests and manual fresh-install run | Open |
| `RB-005` | P0 | Provider-specific disclosure and explicit consent occur before personal data is sent to any third-party AI provider. | Network/provider tests for consent, decline, revoke, version change, and fail-closed states | Open |
| `RB-006` | P0 | Diagnostics and device-context defaults/consents match the approved Privacy Policy, App Privacy answers, and exact payload preview. | Code change or explicit approved disclosure, clean-install settings test, encoded-payload parity test | Open |
| `RB-006A` | P0 | Redacted message/reply prefixes of up to 80 characters are not silently classified and uploaded as metadata; transmission requires explicit content opt-in. | Unit/integration tests for truncation, redaction, `containsContent`, segment classification, clean-install defaults, and exact uploaded bytes | Open |
| `RB-007` | P0 | `Read Only`, `Ask First`, and `Auto Apply` are enforced by capability and Noggin authorization, not prompt text. | End-to-end denial/approval tests across iOS and `kai-core` | Open |
| `RB-008` | P0 | Typed approval requests show target/effect/risk/reversibility/cost, remain visible, and support matching approve/deny with fail-closed timeout/mismatch/loss. | UI and transport integration tests plus manual run | Open |
| `RB-009` | P0 | Account creation, if shipped, has in-app deletion distinct from disconnect and documents third-party/self-hosted exclusions. | Deletion API/UI test, retained-data status, App Review demonstration | Open |
| `RB-010` | P0 | Privacy manifests exist for every distributed Apple bundle and match required-reason API/SDK inventory. | Built-product inspection and `PRIVACY-MANIFEST-INVENTORY.md` approval | Open |
| `RB-011` | P0 | App Store Privacy, age rating, review notes, encryption/export answers, and public policies match the final binary and live services. | Approved Apple submission package tied to build number | Open |
| `RB-012` | P1 | GitHub repositories and permissions are minimized; scope expansion requires explicit reconnect. | Installation/scopes tests and user-visible disclosure | Open |
| `RB-013` | P1 | Production website processors, data categories, retention/deletion, locations, and contracts are verified. | Provider register plus live configuration evidence with secrets redacted | Open |
| `RB-014` | P1 | No ad/sale/tracking/company-training claim is published until dependency, network, contract, and operational review supports it. | Updated claim matrix and independent review | Open |
| `RB-015` | P1 | Paid-service/refund/cancellation language remains inactive until production payment facts and policy are approved. | Explicit owner decision, production flow evidence, updated Terms/Privacy/App Store records | Open |
| `RB-016` | P1 | All regional modules remain inactive; storefront availability is US-only. | App Store territory evidence and inactive manifest status | Open |
| `RB-017` | P1 | No residential address, placeholder, prohibited launch-age wording, stale governing-law reference, or professional-review claim is present. | Validator output plus manual review | Open |
| `RB-018` | P1 | Fresh independent adversarial review finds no unsupported claim, approval bypass, excessive permission, or unsafe failure mode. | Review report with resolved findings | Open |

## Fail-closed rules

- A missing or `GENERATED` hash is not a release waiver.
- A draft/inactive document is never an approved export.
- A passed document validator does not waive a product blocker.
- A test passing establishes only what the test exercised; manual build-and-run evidence remains
  required for the acceptance, approval, deletion, and Settings flows.
- A regional file's existence does not activate that region.
- An unresolved ownership overlap stops the affected lane rather than silently choosing one branch.

## Release decision record

When all applicable blockers close, record the final decision here with date, build/website
commits, manifest version, validator output, review report, and Brandon's approval. Until then,
public draft pages must not be represented as the approved AgentKip legal baseline.
