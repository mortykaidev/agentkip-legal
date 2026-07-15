# Encryption and Export Compliance Checklist

Status: **BLOCKED - engineering inventory and classification incomplete**

Scope: Each Apple-platform binary and each submitted version

This checklist gathers evidence; it does not make an export-control legal
determination. App Store Connect answers must reflect the exact binary and current
rules on the submission date.

## Cryptography inventory

- [ ] Enumerate Apple networking/security frameworks used by each target.
- [ ] Enumerate TLS/HTTPS, certificate handling, Keychain, CryptoKit,
      CommonCrypto, local encryption, VPN, SSH, end-to-end encryption, custom
      algorithms, and bundled cryptographic libraries.
- [ ] Enumerate cryptography supplied by every embedded third-party SDK.
- [ ] Identify whether the app implements, calls, exposes, or merely relies on
      operating-system cryptography.
- [ ] Confirm whether users can configure or supply cryptographic functions.
- [ ] Confirm intended distribution countries and any region-specific limits.
- [ ] Record library names, versions, purposes, targets, and source evidence.

## App Store Connect decision record

Complete only after the inventory:

| Question | Answer | Evidence/owner |
|---|---|---|
| Does the binary use encryption? | BLOCKED | Engineering inventory required |
| Is use limited to encryption within Apple's operating system? | BLOCKED | Architecture evidence required |
| Does it contain proprietary or non-standard algorithms? | BLOCKED | Source/dependency scan required |
| Is it eligible for an exemption? | BLOCKED | Classification review required |
| Is documentation or a CCATS required? | BLOCKED | Classification and distribution review required |
| `ITSAppUsesNonExemptEncryption` value | BLOCKED | Set only after answers above |
| App Store Connect documentation uploaded | Not started | Submission owner |
| Annual or version-specific reporting required | BLOCKED | Current-rule verification required |

Do not assume ordinary HTTPS, authentication, or Keychain use automatically
answers every App Store Connect question. Conversely, do not characterize a
binary as using non-exempt encryption without an evidence-backed classification.

## Verification

- [ ] Diff the inventory against the final dependency lockfiles and archive.
- [ ] Search source and linked binaries for cryptographic libraries/symbols.
- [ ] Confirm the Info.plist value is embedded in every submitted target.
- [ ] Confirm App Store Connect answers match the embedded value.
- [ ] Store non-secret classification evidence in this private package.
- [ ] Re-run after any networking, authentication, security, VPN, SSH, or SDK
      change.

## Release blockers

1. No per-target cryptography inventory exists.
2. The final dependency/archive evidence is missing.
3. Exemption and documentation requirements have not been classified.
4. The embedded Info.plist value and App Store Connect answers are not reconciled.

Sources:

- [Overview of export compliance](https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance)
- [Complying with encryption export regulations](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations)
