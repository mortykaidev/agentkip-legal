# Publication and Integration Brief

## Objective

Publish only reviewed, hash-locked legal content from this private repository while keeping the
website, iOS app, Noggin, App Store records, and retained acceptance artifacts on the same versions.

## Authority and artifact flow

```text
canonical private markdown
        ↓
DOCUMENTATION-MANIFEST.yaml + claim/source/release review
        ↓  validate + hash + Brandon approval + source commit
approved deterministic export
        ├── website content + website legal-documents.json
        └── app copy + app legal-documents.json
                    ↓
consumer-repository integration PRs and runtime receipts
```

Canonical markdown is never imported from the website or app. Generated copies are never edited.
If a consumer needs different wording, edit the canonical source, assign a new version/hash, review
materiality, approve, export, and integrate again.

## Manifest lifecycle

1. Draft entries use `status: draft`, `sha256: GENERATED`, and
   `publication_commit: UNPUBLISHED`.
2. `python3 scripts/legal_docs.py validate` reports missing/generated draft sources as warnings but
   fails schema, path, link, placeholder, address, stale-law/age, and false review-claim checks.
3. After every source exists, run `python3 scripts/legal_docs.py hashes --write`; review the entire
   manifest diff and commit sources plus hashes.
4. Brandon records approval, changes the approved entries to `approved`, and sets
   `publication_commit` to the full 40-character source commit. This metadata change is a separate
   auditable commit.
5. Run `python3 scripts/legal_docs.py validate --release` and then
   `python3 scripts/legal_docs.py export --output build/approved-exports`.
6. Consumer PRs copy outputs without modification and verify their bytes against the export
   registry. Website publication changes manifest status to `published` in a follow-up record.

`DOCUMENTATION-MANIFEST.yaml` is JSON-compatible YAML 1.2 so all commands use only Python's
standard library.

## Export contract

The export command fails unless every selected artifact is approved/published, present, hash
correct, and tied to a source commit. It writes deterministic output beneath the caller-supplied
directory:

```text
approved-exports/
  website/
    legal-documents.json
    privacy/content.md
    terms/content.md
    ...
  app/
    legal-documents.json
    copy/age-and-terms-assent.md
    ...
  export-manifest.json
```

Registries expose only integration metadata: ID, title, category, version, effective date, status,
region, URL, source hash, material-change flag, acceptance mode, publication commit, and exported
file when applicable. Internal source paths, evidence notes, inactive regions, and internal
compliance documents are excluded.

The app registry includes public legal metadata even when the full public markdown is website-only,
so the app can display the exact URL/version/hash and compare it with retained receipts. In-app
copy is bundled as markdown resources. Canonical in-app templates may contain only runtime tokens
explicitly declared on that manifest entry; undeclared tokens fail package validation. Before a
rendered string is displayed or retained, the consumer must substitute every declared value and
run the equivalent of `legal_docs.py validate-rendered <document-id> <rendered-file>`—rendered copy
with any token remaining fails. A material version change triggers the product acceptance
coordinator; changing only a remote page cannot silently alter an accepted artifact.

## Website integration

- Resolve website PR #3 ownership before touching overlapping legal pages.
- Preserve `/privacy`, `/terms`, `/security`, and every other route in the manifest.
- Render exported content through a shared legal layout; do not duplicate legal prose in TSX.
- Footer, sitemap, account/deletion, provider-consent, and support surfaces link to canonical routes.
- CI compares imported file hashes and registry metadata with the legal export, rejects local edits,
  and runs build, links, accessibility, and responsive tests.
- Do not publish user guides until their procedures match the live product.

## App integration

- Bundle `app/legal-documents.json` and `app/copy/*` as resources generated from an approved export.
- Model legal documents and consent receipts with explicit IDs/versions/hashes; never key acceptance
  only by a Boolean.
- Route every fresh-install/signup/invite/pair/deep-link entry through one acceptance coordinator.
- Keep provider consent, target authority, Auto Apply acknowledgment, and per-action approval as
  independent decisions.
- Retain/display/export the accepted version and, where required, a readable copy; a user must be
  able to review what they accepted.
- Settings links, App Store metadata, App Privacy answers, and deletion UX use registry URLs and
  versions.

## Noggin and cross-repository integration

Noggin consumes typed authorization contracts, not legal markdown. Extend its existing approval and
checkpoint machinery with exact request/decision IDs, scopes, risk, side effects, timeout, receipts,
and rollback references. Unknown/mismatched/lost approval fails closed. Backend changes remain in
the Noggin repository and receive their own PR/tests.

Each consumer repository performs its own preflight and opens a draft PR before edits. Do not merge,
rebase, cherry-pick, or overwrite another agent's in-flight claim. Apple product targets use
separate product-scoped PRs and a single serialized Xcode build/test lane.

## Verification handoff

Attach to every publication PR:

- `validate --release` output;
- `export-manifest.json` and consumer hash-parity result;
- manifest/changelog entry and source publication commit;
- closed applicable release blockers;
- website build/link/accessibility evidence or app build/test/manual-run evidence;
- independent review findings and resolutions;
- explicit Brandon publication approval.
