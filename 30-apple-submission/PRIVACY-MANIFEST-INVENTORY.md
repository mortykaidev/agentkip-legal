# Privacy Manifest Inventory

Status: **BLOCKED - no `PrivacyInfo.xcprivacy` found in the audited repository**

Snapshot date: 2026-07-15

Privacy manifests must describe the shipping target and its bundled third-party
SDKs. This inventory must be regenerated from the archived build after each SDK,
target, or required-reason API change.

## Target inventory

| Candidate target | Product area | Distribution status | App-owned manifest | SDK manifests | Gate |
|---|---|---|---|---|---|
| AgentKip | Main iOS app | Verify | Missing | Unknown | BLOCKED |
| KipShare | Share extension | Verify | Missing | Unknown | BLOCKED if distributed |
| KipWidgets | Widgets and Live Activities | Verify | Missing | Unknown | BLOCKED if distributed |
| Kip26 | Showcase target | Verify | Missing | Unknown | BLOCKED if distributed |
| KipPairMenu | macOS pairing app | Verify separately | Missing | Unknown | BLOCKED if distributed |

Targets not included in the submitted archive do not require claims for that
archive, but their distribution status must be documented rather than assumed.

## Required manifest fields

For each distributed bundle, verify and record:

- `NSPrivacyTracking` and, if applicable, tracking domains.
- `NSPrivacyCollectedDataTypes`, purposes, linkage, and tracking flags.
- `NSPrivacyAccessedAPITypes` and approved reasons for each required-reason API.
- Every third-party SDK's manifest, signature status where applicable, and
  consistency with actual configuration.

## Required-reason API audit

Search first-party source and binary dependencies for current Apple-listed API
categories, including file timestamp, system boot time, disk space, active
keyboard, and user defaults APIs. This list is only a starting point; the audit
must use Apple's current required-reason API list on the submission date.

For every finding, record:

| Field | Required value |
|---|---|
| Target and binary | Exact bundle and dependency |
| API category | Apple's current category identifier |
| Call site | File/symbol or dependency version |
| Product purpose | Actual shipping behavior |
| Approved reason | Current Apple reason code and rationale |
| Evidence | Static scan plus runtime/build evidence |
| Disposition | Declare, remove, replace, or obtain SDK update |

Do not select a reason merely because it permits submission. The reason must
describe the shipping use, and the API may not be used for tracking or another
undeclared purpose.

## Build verification

- [ ] Run the current privacy report/static analysis for the archive.
- [ ] Inspect the built `.app` and each `.appex`, not only source directories.
- [ ] Enumerate package-manager and embedded-framework privacy manifests.
- [ ] Resolve missing or invalid SDK manifests/signatures.
- [ ] Compare manifest data types with the App Privacy worksheet.
- [ ] Compare reasons with current Apple documentation on submission day.
- [ ] Archive the final manifests and report with version/build evidence.
- [ ] Add a CI gate that fails when a distributed target lacks its required
      manifest or introduces an unreviewed API category.

## Release blockers

1. No app-owned privacy manifest was found.
2. Distributed-target scope has not been frozen.
3. The release dependency graph and third-party manifests are not inventoried.
4. Required-reason API use has not been scanned and justified.
5. App Privacy answers cannot be reconciled until the manifest is complete.

Sources:

- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files)
- [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests)
- [Describing use of required-reason APIs](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api)
