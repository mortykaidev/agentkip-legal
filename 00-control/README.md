# Control Layer

This directory records the facts, versions, evidence, placement, and release gates that keep
AgentKip's legal copy synchronized with the product. Public documents live in
`10-public-legal/`; approved exports are generated from the manifest and are never hand-edited.

## Read order

1. `FACTS-AND-DECISIONS.md` — locked launch facts and policy choices.
2. `DOCUMENTATION-MANIFEST.yaml` — machine-readable inventory, versions, hashes, and exports.
3. `CLAIM-TO-CODE-MATRIX.md` — evidence for technical statements and known contradictions.
4. `SOURCE-LEDGER.md` — primary official legal, platform, and vendor sources.
5. `PLACEMENT-MATRIX.md` — where each approved artifact is presented or retained.
6. `RELEASE-BLOCKERS.md` — fail-closed publication, TestFlight, and App Store gates.
7. `PUBLICATION-AND-INTEGRATION-BRIEF.md` — deterministic export and consumer-repository flow.
8. `LEGAL-CHANGELOG.md` — material-change and acceptance history.
9. `INDEPENDENT-REVIEW-2026-07-15.md` — adversarial findings, resolutions, and remaining gates.

## Manifest format

`DOCUMENTATION-MANIFEST.yaml` is JSON-compatible YAML 1.2. That deliberate restriction lets the
repository validate and update it with Python's standard library instead of installing a YAML
parser. Every controlled document is listed; package `README.md` files are navigation aids and are
not controlled artifacts.

## Commands

```bash
python3 scripts/legal_docs.py validate
python3 scripts/legal_docs.py hashes
python3 scripts/legal_docs.py hashes --write
python3 scripts/legal_docs.py export --output build/approved-exports
python3 -m unittest discover -s tests -v
```

Draft validation allows a missing canonical source only when its manifest hash is `GENERATED` and
reports that state as a warning. Approved export is fail-closed: every exported source must exist,
have an exact SHA-256 hash, be `approved` or `published`, and identify the source publication
commit.
