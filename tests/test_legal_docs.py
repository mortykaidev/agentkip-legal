from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import legal_docs as legal


class LegalDocsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "00-control").mkdir()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @property
    def manifest_path(self) -> Path:
        return self.root / "00-control" / "DOCUMENTATION-MANIFEST.yaml"

    def public_document(
        self,
        content: str = "# Test Policy\n\n**Effective:** July 15, 2026\n**Version:** 2026.07.15-test.1\n\nSafe policy text.\n",
        *,
        status: str = "approved",
        digest: str | None = None,
    ) -> dict[str, object]:
        source = self.root / "10-public-legal" / "TEST-POLICY.md"
        source.parent.mkdir(exist_ok=True)
        source.write_text(content, encoding="utf-8")
        return {
            "id": "test-policy",
            "title": "Test Policy",
            "category": "public-legal",
            "version": "2026.07.15-test.1",
            "effective_date": "2026-07-15",
            "status": status,
            "region": "US",
            "source": "10-public-legal/TEST-POLICY.md",
            "public_url": "https://agentkip.ai/test-policy",
            "sha256": digest if digest is not None else legal.sha256_file(source),
            "material_change": True,
            "acceptance": "none",
            "approver": "Brandon",
            "publication_commit": "a" * 40 if status in legal.RELEASE_STATUSES else "UNPUBLISHED",
            "exports": {"website": "test-policy/content.md"},
            "registry_targets": ["website", "app"],
        }

    def in_app_document(
        self,
        content: str = "# Test Copy\n\n**Copy version:** 2026.07.15-test.1\n**Effective:** July 15, 2026\n\nApprove [TARGET_NAME]?\n",
    ) -> dict[str, object]:
        source = self.root / "20-in-app-copy" / "TEST-COPY.md"
        source.parent.mkdir(exist_ok=True)
        source.write_text(content, encoding="utf-8")
        return {
            "id": "test-copy",
            "title": "Test Copy",
            "category": "in-app-copy",
            "version": "2026.07.15-test.1",
            "effective_date": "2026-07-15",
            "status": "approved",
            "region": "US",
            "source": "20-in-app-copy/TEST-COPY.md",
            "public_url": None,
            "sha256": legal.sha256_file(source),
            "material_change": True,
            "acceptance": "per-action",
            "approver": "Brandon",
            "publication_commit": "b" * 40,
            "exports": {"app": "copy/test-copy.md"},
            "registry_targets": ["app"],
            "runtime_tokens": ["TARGET_NAME"],
        }

    def write_manifest(self, documents: list[dict[str, object]]) -> None:
        manifest = {
            "schema_version": 1,
            "product": "AgentKip",
            "canonical_base_url": "https://agentkip.ai",
            "allowed_internal_routes": ["/", "/support"],
            "export_targets": {
                "website": {"registry": "legal-documents.json"},
                "app": {"registry": "legal-documents.json"},
            },
            "documents": documents,
        }
        self.manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    def error_codes(self, issues: list[legal.Issue]) -> set[str]:
        return {issue.code for issue in issues if issue.severity == "error"}

    def test_valid_release_manifest(self) -> None:
        self.write_manifest([self.public_document()])
        issues = legal.validate_manifest(self.root, self.manifest_path, release=True)
        self.assertEqual([], [issue for issue in issues if issue.severity == "error"])

    def test_draft_generated_hash_is_warning_but_release_error(self) -> None:
        document = self.public_document(status="draft", digest="GENERATED")
        self.write_manifest([document])
        draft_issues = legal.validate_manifest(self.root, self.manifest_path)
        self.assertIn("generated-hash", {issue.code for issue in draft_issues if issue.severity == "warning"})
        release_codes = self.error_codes(legal.validate_manifest(self.root, self.manifest_path, release=True))
        self.assertTrue({"generated-hash", "release-status", "release-commit"}.issubset(release_codes))

    def test_hash_mismatch_is_rejected(self) -> None:
        self.write_manifest([self.public_document(digest="0" * 64)])
        self.assertIn("hash-mismatch", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_public_source_version_must_match_manifest(self) -> None:
        content = "# Test Policy\n\n**Effective:** July 15, 2026\n**Version:** 1.0\n\nSafe policy text.\n"
        self.write_manifest([self.public_document(content)])
        self.assertIn("version-mismatch", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_in_app_copy_version_must_match_manifest(self) -> None:
        content = "# Test Copy\n\n**Copy version:** 1.0\n**Effective:** July 15, 2026\n\nApprove [TARGET_NAME]?\n"
        self.write_manifest([self.in_app_document(content)])
        self.assertIn("copy-version-mismatch", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_effective_date_must_match_manifest(self) -> None:
        content = "# Test Policy\n\n**Updated:** July 14, 2026\n**Version:** 2026.07.15-test.1\n\nSafe policy text.\n"
        self.write_manifest([self.public_document(content)])
        self.assertIn("effective-date-mismatch", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_hash_update_fills_generated_value(self) -> None:
        document = self.public_document(status="draft", digest="GENERATED")
        self.write_manifest([document])
        hashes, missing = legal.update_hashes(self.root, self.manifest_path, write=True)
        self.assertEqual([], missing)
        updated = legal.load_manifest(self.manifest_path)
        self.assertEqual(hashes["test-policy"], updated["documents"][0]["sha256"])

    def test_source_path_escape_is_rejected(self) -> None:
        document = self.public_document()
        document["source"] = "../escape.md"
        self.write_manifest([document])
        self.assertIn("source-path", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_missing_local_link_is_rejected(self) -> None:
        self.write_manifest([self.public_document("# Test\n\n**Effective:** July 15, 2026\n**Version:** 2026.07.15-test.1\n\n[Missing](NOPE.md)\n")])
        self.assertIn("missing-local-link", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_forbidden_consumer_language_and_placeholders(self) -> None:
        samples = {
            "placeholder-word": "TODO replace this",
            "template-braces": "Hello {{NAME}}",
            "example-domain": "Visit example.com",
            "stale-governing-law": "These terms are governed by the laws of New York.",
            "under-13-launch-language": "We do not knowingly serve anyone under 13.",
            "professional-review-claim": "These terms were reviewed by an attorney.",
        }
        for expected, content in samples.items():
            with self.subTest(expected=expected):
                self.write_manifest([self.public_document(f"# Test\n\n**Effective:** July 15, 2026\n**Version:** 2026.07.15-test.1\n\n{content}\n")])
                self.assertIn(expected, self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_negated_professional_review_statement_is_allowed(self) -> None:
        content = "# Test\n\n**Effective:** July 15, 2026\n**Version:** 2026.07.15-test.1\n\nThis package is not represented as attorney-reviewed.\n"
        self.write_manifest([self.public_document(content)])
        self.assertNotIn("professional-review-claim", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_possible_street_address_is_rejected_repository_wide(self) -> None:
        self.write_manifest([self.public_document()])
        control = self.root / "00-control" / "PRIVATE.md"
        control.write_text("Send mail to 123 Sample Street.\n", encoding="utf-8")
        self.assertIn("possible-residential-address", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_non_readme_package_markdown_requires_manifest_entry(self) -> None:
        self.write_manifest([self.public_document()])
        (self.root / "10-public-legal" / "ORPHAN.md").write_text("# Orphan\n", encoding="utf-8")
        (self.root / "10-public-legal" / "README.md").write_text("# Index\n", encoding="utf-8")
        issues = legal.validate_manifest(self.root, self.manifest_path)
        unmanifested = [issue.path for issue in issues if issue.code == "unmanifested-source"]
        self.assertEqual(["10-public-legal/ORPHAN.md"], unmanifested)

    def test_declared_runtime_tokens_are_allowed_in_template(self) -> None:
        self.write_manifest([self.in_app_document()])
        issues = legal.validate_manifest(self.root, self.manifest_path, release=True)
        self.assertNotIn("runtime-token", self.error_codes(issues))

    def test_undeclared_runtime_token_is_rejected(self) -> None:
        document = self.in_app_document(
            "# Test Copy\n\n**Copy version:** 2026.07.15-test.1\n**Effective:** July 15, 2026\n\nApprove [TARGET_NAME] for [UNKNOWN_SCOPE]?\n"
        )
        self.write_manifest([document])
        self.assertIn("runtime-token", self.error_codes(legal.validate_manifest(self.root, self.manifest_path)))

    def test_rendered_copy_rejects_remaining_runtime_token(self) -> None:
        self.write_manifest([self.in_app_document()])
        rendered = self.root / "rendered.md"
        rendered.write_text("Approve [TARGET_NAME]?\n", encoding="utf-8")
        self.assertIn("runtime-token", self.error_codes(legal.validate_rendered(self.root, self.manifest_path, "test-copy", rendered)))

    def test_export_copies_exact_bytes_and_writes_registries(self) -> None:
        public = self.public_document()
        app = self.in_app_document()
        self.write_manifest([public, app])
        output = self.root / "out"
        written = legal.export_approved(self.root, self.manifest_path, output)
        output = output.resolve()
        self.assertIn(output / "website" / "test-policy" / "content.md", written)
        self.assertEqual(
            (self.root / public["source"]).read_bytes(),
            (output / "website" / "test-policy" / "content.md").read_bytes(),
        )
        app_registry = json.loads((output / "app" / "legal-documents.json").read_text(encoding="utf-8"))
        self.assertEqual(["test-copy", "test-policy"], [item["id"] for item in app_registry["documents"]])
        template = next(item for item in app_registry["documents"] if item["id"] == "test-copy")
        self.assertEqual(["TARGET_NAME"], template["runtimeTokens"])
        with self.assertRaises(legal.ManifestError):
            legal.export_approved(self.root, self.manifest_path, output)


if __name__ == "__main__":
    unittest.main()
