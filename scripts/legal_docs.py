#!/usr/bin/env python3
"""Validate, hash, and export the AgentKip legal documentation package.

The manifest is intentionally JSON-compatible YAML 1.2, so this tool has no
third-party dependencies. Approved export is fail-closed; draft validation is
useful while source documents are still being assembled.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import ssl
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Sequence
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = Path("00-control") / "DOCUMENTATION-MANIFEST.yaml"

REQUIRED_DOCUMENT_FIELDS = {
    "id",
    "title",
    "category",
    "version",
    "effective_date",
    "status",
    "region",
    "source",
    "public_url",
    "sha256",
    "material_change",
    "acceptance",
    "approver",
    "publication_commit",
    "exports",
    "registry_targets",
}

CATEGORY_PREFIXES = {
    "public-legal": "10-public-legal",
    "in-app-copy": "20-in-app-copy",
    "apple-submission": "30-apple-submission",
    "internal-compliance": "40-internal-compliance",
    "regional": "50-regional",
    "user-guide": "60-user-guides",
    "future-review": "90-future-review",
}
PUBLIC_CATEGORIES = {"public-legal", "user-guide"}
CONSUMER_CATEGORIES = {"public-legal", "in-app-copy", "user-guide"}
ALLOWED_STATUSES = {"draft", "approved", "published", "inactive", "retired"}
RELEASE_STATUSES = {"approved", "published"}
ALLOWED_ACCEPTANCE = {
    "none",
    "acknowledgment",
    "explicit",
    "provider-specific",
    "per-action",
}
ALLOWED_EXPORT_TARGETS = {"website", "app"}
CONTROLLED_SUFFIXES = {".md", ".json", ".yaml", ".yml"}

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
REGION_RE = re.compile(r"^[A-Z][A-Z0-9-]{1,31}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
RUNTIME_TOKEN_RE = re.compile(r"\[([A-Z][A-Z0-9_]+)\](?!\()")
PUBLIC_VERSION_RE = re.compile(r"^\*\*Version:\*\*\s*(.+?)\s*$", re.MULTILINE)
COPY_VERSION_RE = re.compile(r"^\*\*Copy version:\*\*\s*(.+?)\s*$", re.MULTILINE)
PUBLIC_DATE_RE = re.compile(r"^\*\*(?:Effective|Updated):\*\*\s*(.+?)\s*$", re.MULTILINE)
IN_APP_DATE_RE = re.compile(r"^\*\*Effective:\*\*\s*(.+?)\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
AUTOLINK_RE = re.compile(r"<((?:https://|http://|mailto:)[^>]+)>")

PLACEHOLDER_PATTERNS = (
    ("placeholder-word", re.compile(r"\b(?:TODO|TBD|TBC|CHANGEME|FIXME)\b", re.IGNORECASE)),
    ("template-braces", re.compile(r"\{\{[^{}\n]+\}\}")),
    ("example-domain", re.compile(r"\bexample\.(?:com|org|net)\b", re.IGNORECASE)),
    (
        "editorial-placeholder",
        re.compile(r"\[(?:DATE|ADDRESS|COMPANY|EMAIL|NAME|URL|INSERT[^\]]*)\]", re.IGNORECASE),
    ),
)

CONSUMER_FORBIDDEN_PATTERNS = (
    (
        "stale-governing-law",
        re.compile(
            r"(?:governed\s+by|laws?\s+of|exclusive\s+venue|courts?\s+(?:in|of))"
            r"[^\n.]{0,80}\bNew\s+York\b",
            re.IGNORECASE,
        ),
    ),
    (
        "under-13-launch-language",
        re.compile(r"\b(?:under\s+(?:the\s+age\s+of\s+)?13|13\s+years?\s+old)\b", re.IGNORECASE),
    ),
)

PROFESSIONAL_REVIEW_RE = re.compile(
    r"\b(?:attorney|lawyer|counsel)[ -](?:reviewed|approved|certified)\b"
    r"|\b(?:reviewed|approved|certified)\s+by\s+(?:an?\s+)?(?:attorney|lawyer|counsel)\b",
    re.IGNORECASE,
)

STREET_ADDRESS_RE = re.compile(
    r"\b\d{1,6}\s+(?:[A-Za-z0-9.'-]+\s+){0,5}"
    r"(?:Street|St\.?|Road|Rd\.?|Avenue|Ave\.?|Boulevard|Blvd\.?|Drive|Dr\.?|"
    r"Lane|Ln\.?|Court|Ct\.?|Way|Circle|Terrace|Trail|Parkway|Place|Highway|Hwy\.?)\b",
    re.IGNORECASE,
)

SECRET_PATTERNS = (
    ("private-key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("stripe-live-secret", re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
)


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str
    document_id: str | None = None
    path: str | None = None
    line: int | None = None

    def __str__(self) -> str:
        location = self.path or self.document_id or "manifest"
        if self.line is not None:
            location = f"{location}:{self.line}"
        return f"{self.severity.upper()} [{self.code}] {location}: {self.message}"


class ManifestError(ValueError):
    """Raised when the manifest cannot be loaded or an export cannot proceed."""


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ManifestError(f"manifest does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ManifestError(
            f"manifest must be JSON-compatible YAML 1.2: {path}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(value, dict):
        raise ManifestError("manifest root must be an object")
    return value


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _safe_relative(value: Any) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in {"", ".", ".."} for part in path.parts)


def _repo_path(root: Path, value: str) -> Path:
    candidate = (root / PurePosixPath(value)).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ManifestError(f"path escapes repository root: {value}") from exc
    return candidate


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _parse_display_date(value: str) -> str | None:
    cleaned = value.strip()
    for format_string in ("%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(cleaned, format_string).date().isoformat()
        except ValueError:
            continue
    return None


def _validate_single_header(
    text: str,
    *,
    pattern: re.Pattern[str],
    expected: str,
    missing_code: str,
    duplicate_code: str,
    mismatch_code: str,
    label: str,
    document_id: str,
    source: str,
    transform: Any | None = None,
) -> list[Issue]:
    values = [match.group(1).strip() for match in pattern.finditer(text)]
    if not values:
        return [Issue("error", missing_code, f"source requires exactly one {label} header", document_id, source)]
    if len(values) != 1:
        return [Issue("error", duplicate_code, f"source must contain exactly one {label} header", document_id, source)]
    actual = transform(values[0]) if transform else values[0]
    if actual is None:
        return [Issue("error", mismatch_code, f"source {label} is not a supported date: {values[0]!r}", document_id, source)]
    if actual != expected:
        return [Issue("error", mismatch_code, f"source declares {values[0]!r}; manifest declares {expected!r}", document_id, source)]
    return []


def _is_negated_review_claim(text: str, start: int) -> bool:
    prefix = text[max(0, start - 32) : start].lower()
    return bool(re.search(r"\b(?:not|never|no)\s+(?:represented\s+as\s+)?$", prefix))


def scan_text(
    text: str,
    *,
    document_id: str,
    path: str,
    consumer_facing: bool,
    allowed_runtime_tokens: Iterable[str] = (),
    rendered: bool = False,
) -> list[Issue]:
    issues: list[Issue] = []
    allowed = set(allowed_runtime_tokens)

    for code, pattern in PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(text):
            token_match = RUNTIME_TOKEN_RE.fullmatch(match.group(0))
            if token_match and token_match.group(1) in allowed and not rendered:
                continue
            issues.append(
                Issue("error", code, f"forbidden unresolved placeholder {match.group(0)!r}", document_id, path, _line_for_offset(text, match.start()))
            )

    found_runtime_tokens: set[str] = set()
    for match in RUNTIME_TOKEN_RE.finditer(text):
        token = match.group(1)
        found_runtime_tokens.add(token)
        if rendered or token not in allowed:
            detail = "runtime-rendered copy contains an unresolved token" if rendered else "runtime token is not declared in the manifest"
            issues.append(
                Issue("error", "runtime-token", f"{detail}: [{token}]", document_id, path, _line_for_offset(text, match.start()))
            )

    for token in sorted(allowed - found_runtime_tokens):
        issues.append(
            Issue("warning", "unused-runtime-token", f"manifest declares unused runtime token [{token}]", document_id, path)
        )

    if consumer_facing:
        for code, pattern in CONSUMER_FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                issues.append(
                    Issue("error", code, f"forbidden launch language {match.group(0)!r}", document_id, path, _line_for_offset(text, match.start()))
                )

    for match in PROFESSIONAL_REVIEW_RE.finditer(text):
        if _is_negated_review_claim(text, match.start()):
            continue
        issues.append(
            Issue(
                "error",
                "professional-review-claim",
                f"do not state or imply professional legal review: {match.group(0)!r}",
                document_id,
                path,
                _line_for_offset(text, match.start()),
            )
        )

    return issues


def _validate_url(value: str, *, allow_mailto: bool = False) -> bool:
    parsed = urlparse(value)
    if allow_mailto and parsed.scheme == "mailto":
        return bool(parsed.path and "@" in parsed.path and not parsed.query and not parsed.fragment)
    return parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username and not parsed.password


def validate_links(
    text: str,
    *,
    root: Path,
    source_path: Path,
    document_id: str,
    public_routes: set[str],
    allowed_routes: set[str],
) -> tuple[list[Issue], set[str]]:
    issues: list[Issue] = []
    external: set[str] = set()
    candidates = [match.group(1) for match in MARKDOWN_LINK_RE.finditer(text)]
    candidates.extend(match.group(1) for match in AUTOLINK_RE.finditer(text))

    for raw in candidates:
        target = raw.strip().strip("<>")
        if not target or target.startswith("#"):
            continue
        if target.startswith("https://"):
            if not _validate_url(target):
                issues.append(Issue("error", "invalid-link", f"invalid HTTPS URL: {target}", document_id, str(source_path.relative_to(root))))
            else:
                external.add(target)
            continue
        if target.startswith("mailto:"):
            if not _validate_url(target, allow_mailto=True):
                issues.append(Issue("error", "invalid-mailto", f"invalid mail link: {target}", document_id, str(source_path.relative_to(root))))
            continue
        if target.startswith("http://"):
            issues.append(Issue("error", "insecure-link", f"external link must use HTTPS: {target}", document_id, str(source_path.relative_to(root))))
            continue
        if target.startswith("/"):
            parsed = urlparse(target)
            route = parsed.path.rstrip("/") or "/"
            allowed = route in public_routes or any(
                route == prefix or route.startswith(prefix.rstrip("/") + "/") for prefix in allowed_routes
            )
            if not allowed:
                issues.append(Issue("error", "unknown-internal-route", f"route is not declared by the manifest: {target}", document_id, str(source_path.relative_to(root))))
            continue

        relative_target = target.split("#", 1)[0].split("?", 1)[0]
        if not relative_target:
            continue
        candidate = (source_path.parent / relative_target).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError:
            issues.append(Issue("error", "link-path-escape", f"local link escapes repository: {target}", document_id, str(source_path.relative_to(root))))
            continue
        if not candidate.exists():
            issues.append(Issue("error", "missing-local-link", f"local link target does not exist: {target}", document_id, str(source_path.relative_to(root))))

    return issues, external


def _check_external_url(url: str, timeout: float = 8.0) -> str | None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "AgentKip-Legal-LinkCheck/1.0"})
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
            if response.status < 400:
                return None
            return f"HTTP {response.status}"
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 405}:
            return None
        return f"HTTP {exc.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return str(exc)


def _repo_sensitive_scan(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    excluded_parts = {".git", "build", "scripts", "tests", "__pycache__"}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in CONTROLLED_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if any(part in excluded_parts for part in relative.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in STREET_ADDRESS_RE.finditer(text):
            issues.append(
                Issue(
                    "error",
                    "possible-residential-address",
                    f"street-address pattern requires removal or explicit non-residential review: {match.group(0)!r}",
                    path=str(relative),
                    line=_line_for_offset(text, match.start()),
                )
            )
        for code, pattern in SECRET_PATTERNS:
            for match in pattern.finditer(text):
                issues.append(
                    Issue("error", code, "possible secret or credential is forbidden", path=str(relative), line=_line_for_offset(text, match.start()))
                )
    return issues


def validate_manifest(
    root: Path,
    manifest_path: Path,
    *,
    release: bool = False,
    check_external: bool = False,
) -> list[Issue]:
    root = root.resolve()
    manifest = load_manifest(manifest_path)
    issues: list[Issue] = []

    if manifest.get("schema_version") != 1:
        issues.append(Issue("error", "schema-version", "schema_version must equal 1"))
    if not isinstance(manifest.get("product"), str) or not manifest.get("product"):
        issues.append(Issue("error", "product", "product must be a non-empty string"))

    base_url = manifest.get("canonical_base_url")
    if not isinstance(base_url, str) or not _validate_url(base_url):
        issues.append(Issue("error", "base-url", "canonical_base_url must be an HTTPS URL"))
        base_url = ""
    base_parsed = urlparse(base_url) if base_url else None

    allowed_routes_raw = manifest.get("allowed_internal_routes", [])
    allowed_routes: set[str] = set()
    if not isinstance(allowed_routes_raw, list) or not all(isinstance(item, str) and item.startswith("/") for item in allowed_routes_raw):
        issues.append(Issue("error", "allowed-routes", "allowed_internal_routes must be a list of absolute paths"))
    else:
        allowed_routes = {item.rstrip("/") or "/" for item in allowed_routes_raw}

    export_targets = manifest.get("export_targets")
    if not isinstance(export_targets, dict) or set(export_targets) != ALLOWED_EXPORT_TARGETS:
        issues.append(Issue("error", "export-targets", "export_targets must define exactly website and app"))
        export_targets = {}
    else:
        for target, settings in export_targets.items():
            registry = settings.get("registry") if isinstance(settings, dict) else None
            if not _safe_relative(registry):
                issues.append(Issue("error", "registry-path", f"{target} registry must be a safe relative path"))

    documents = manifest.get("documents")
    if not isinstance(documents, list) or not documents:
        issues.append(Issue("error", "documents", "documents must be a non-empty list"))
        return issues + _repo_sensitive_scan(root)

    document_ids: set[str] = set()
    source_paths: set[str] = set()
    public_urls: set[str] = set()
    public_routes: set[str] = set()
    export_paths: dict[str, set[str]] = {target: set() for target in ALLOWED_EXPORT_TARGETS}
    external_urls: set[str] = set()
    declared_public_routes = {
        urlparse(item["public_url"]).path.rstrip("/") or "/"
        for item in documents
        if isinstance(item, dict)
        and item.get("category") in PUBLIC_CATEGORIES
        and isinstance(item.get("public_url"), str)
        and _validate_url(item["public_url"])
    }

    for index, raw_document in enumerate(documents):
        if not isinstance(raw_document, dict):
            issues.append(Issue("error", "document-shape", f"documents[{index}] must be an object"))
            continue
        document = raw_document
        document_id = document.get("id") if isinstance(document.get("id"), str) else f"documents[{index}]"
        missing = REQUIRED_DOCUMENT_FIELDS - set(document)
        if missing:
            issues.append(Issue("error", "required-fields", f"missing fields: {', '.join(sorted(missing))}", document_id))

        if not ID_RE.fullmatch(str(document.get("id", ""))):
            issues.append(Issue("error", "document-id", "id must be lowercase hyphenated ASCII", document_id))
        elif document_id in document_ids:
            issues.append(Issue("error", "duplicate-id", "document id is duplicated", document_id))
        else:
            document_ids.add(document_id)

        if not isinstance(document.get("title"), str) or not document.get("title", "").strip():
            issues.append(Issue("error", "title", "title must be a non-empty string", document_id))

        category = document.get("category")
        if category not in CATEGORY_PREFIXES:
            issues.append(Issue("error", "category", f"unknown category: {category!r}", document_id))

        if not isinstance(document.get("version"), str) or not VERSION_RE.fullmatch(document.get("version", "")):
            issues.append(Issue("error", "version", "version must be a stable ASCII identifier", document_id))

        try:
            date.fromisoformat(document.get("effective_date", ""))
        except (TypeError, ValueError):
            issues.append(Issue("error", "effective-date", "effective_date must be YYYY-MM-DD", document_id))

        status = document.get("status")
        if status not in ALLOWED_STATUSES:
            issues.append(Issue("error", "status", f"unknown status: {status!r}", document_id))

        if not isinstance(document.get("region"), str) or not REGION_RE.fullmatch(document.get("region", "")):
            issues.append(Issue("error", "region", "region must be an uppercase stable identifier", document_id))

        source = document.get("source")
        source_path: Path | None = None
        if not _safe_relative(source):
            issues.append(Issue("error", "source-path", "source must be a safe repository-relative path", document_id))
        else:
            if source in source_paths:
                issues.append(Issue("error", "duplicate-source", f"source is reused: {source}", document_id))
            source_paths.add(source)
            expected_prefix = CATEGORY_PREFIXES.get(category)
            if expected_prefix and PurePosixPath(source).parts[0] != expected_prefix:
                issues.append(Issue("error", "source-category", f"{category} source must live under {expected_prefix}/", document_id, source))
            if not source.endswith(".md"):
                issues.append(Issue("error", "source-extension", "controlled source must be Markdown", document_id, source))
            try:
                source_path = _repo_path(root, source)
            except ManifestError as exc:
                issues.append(Issue("error", "source-path", str(exc), document_id, source))

        public_url = document.get("public_url")
        if category in PUBLIC_CATEGORIES:
            if not isinstance(public_url, str) or not _validate_url(public_url):
                issues.append(Issue("error", "public-url", "public document requires an HTTPS public_url", document_id))
            else:
                parsed = urlparse(public_url)
                if base_parsed and (parsed.scheme, parsed.netloc) != (base_parsed.scheme, base_parsed.netloc):
                    issues.append(Issue("error", "public-origin", "public_url must use canonical_base_url origin", document_id))
                if parsed.query or parsed.fragment:
                    issues.append(Issue("error", "public-url-shape", "public_url cannot contain query or fragment", document_id))
                if public_url in public_urls:
                    issues.append(Issue("error", "duplicate-public-url", f"public_url is duplicated: {public_url}", document_id))
                public_urls.add(public_url)
                public_routes.add(parsed.path.rstrip("/") or "/")
        elif public_url is not None:
            issues.append(Issue("error", "private-public-url", "non-public category must use null public_url", document_id))

        digest = document.get("sha256")
        if digest != "GENERATED" and (not isinstance(digest, str) or not SHA256_RE.fullmatch(digest)):
            issues.append(Issue("error", "sha256", "sha256 must be GENERATED or 64 lowercase hex characters", document_id))

        if not isinstance(document.get("material_change"), bool):
            issues.append(Issue("error", "material-change", "material_change must be Boolean", document_id))
        if document.get("acceptance") not in ALLOWED_ACCEPTANCE:
            issues.append(Issue("error", "acceptance", f"unknown acceptance mode: {document.get('acceptance')!r}", document_id))
        if not isinstance(document.get("approver"), str) or not document.get("approver", "").strip():
            issues.append(Issue("error", "approver", "approver must be a non-empty owner name", document_id))

        publication_commit = document.get("publication_commit")
        if publication_commit != "UNPUBLISHED" and (not isinstance(publication_commit, str) or not COMMIT_RE.fullmatch(publication_commit)):
            issues.append(Issue("error", "publication-commit", "publication_commit must be UNPUBLISHED or a full 40-character commit", document_id))

        exports = document.get("exports")
        if not isinstance(exports, dict):
            issues.append(Issue("error", "exports", "exports must be an object", document_id))
            exports = {}
        else:
            unknown_targets = set(exports) - ALLOWED_EXPORT_TARGETS
            if unknown_targets:
                issues.append(Issue("error", "export-target", f"unknown export targets: {', '.join(sorted(unknown_targets))}", document_id))
            for target, target_path in exports.items():
                if target not in ALLOWED_EXPORT_TARGETS:
                    continue
                if not _safe_relative(target_path):
                    issues.append(Issue("error", "export-path", f"{target} export path must be safe and relative", document_id))
                elif target_path in export_paths[target]:
                    issues.append(Issue("error", "duplicate-export", f"{target} export path is duplicated: {target_path}", document_id))
                else:
                    export_paths[target].add(target_path)

        registry_targets = document.get("registry_targets")
        if not isinstance(registry_targets, list) or not all(item in ALLOWED_EXPORT_TARGETS for item in registry_targets):
            issues.append(Issue("error", "registry-targets", "registry_targets must contain only website/app", document_id))
            registry_targets = []
        elif len(registry_targets) != len(set(registry_targets)):
            issues.append(Issue("error", "registry-targets", "registry_targets cannot contain duplicates", document_id))

        if status == "inactive" and (exports or registry_targets):
            issues.append(Issue("error", "inactive-export", "inactive documents cannot export or enter a consumer registry", document_id))
        if category == "public-legal" and "website" not in exports:
            issues.append(Issue("error", "public-export", "public legal document requires a website export", document_id))
        if category == "in-app-copy" and "app" not in exports:
            issues.append(Issue("error", "app-export", "in-app copy requires an app export", document_id))
        if category not in PUBLIC_CATEGORIES | {"in-app-copy"} and exports:
            issues.append(Issue("error", "private-export", f"{category} cannot have a consumer export", document_id))

        runtime_tokens_raw = document.get("runtime_tokens", [])
        runtime_tokens: list[str] = []
        if not isinstance(runtime_tokens_raw, list) or not all(
            isinstance(token, str) and re.fullmatch(r"[A-Z][A-Z0-9_]+", token) for token in runtime_tokens_raw
        ):
            issues.append(Issue("error", "runtime-tokens", "runtime_tokens must be uppercase token names", document_id))
        else:
            runtime_tokens = runtime_tokens_raw
            if len(runtime_tokens) != len(set(runtime_tokens)):
                issues.append(Issue("error", "runtime-tokens", "runtime_tokens cannot contain duplicates", document_id))
            if runtime_tokens and category != "in-app-copy":
                issues.append(Issue("error", "runtime-token-category", "only in-app templates may declare runtime tokens", document_id))

        is_exportable = bool(exports or registry_targets) and status != "inactive"
        if release and is_exportable and status not in RELEASE_STATUSES:
            issues.append(Issue("error", "release-status", "consumer artifact must be approved or published", document_id, source if isinstance(source, str) else None))
        if release and is_exportable and publication_commit == "UNPUBLISHED":
            issues.append(Issue("error", "release-commit", "consumer artifact requires a source publication commit", document_id, source if isinstance(source, str) else None))

        if source_path is None:
            continue
        if not source_path.exists():
            severity = "error" if release or digest != "GENERATED" else "warning"
            issues.append(Issue(severity, "missing-source", "canonical source does not exist", document_id, source))
            continue

        actual_digest = sha256_file(source_path)
        if digest == "GENERATED":
            severity = "error" if release else "warning"
            issues.append(Issue(severity, "generated-hash", f"replace GENERATED with {actual_digest}", document_id, source))
        elif digest != actual_digest:
            issues.append(Issue("error", "hash-mismatch", f"manifest {digest}; actual {actual_digest}", document_id, source))

        text = source_path.read_text(encoding="utf-8")
        if category == "public-legal":
            issues.extend(
                _validate_single_header(
                    text,
                    pattern=PUBLIC_VERSION_RE,
                    expected=document.get("version", ""),
                    missing_code="missing-version-header",
                    duplicate_code="duplicate-version-header",
                    mismatch_code="version-mismatch",
                    label="**Version:**",
                    document_id=document_id,
                    source=source,
                )
            )
            issues.extend(
                _validate_single_header(
                    text,
                    pattern=PUBLIC_DATE_RE,
                    expected=document.get("effective_date", ""),
                    missing_code="missing-effective-header",
                    duplicate_code="duplicate-effective-header",
                    mismatch_code="effective-date-mismatch",
                    label="**Effective:** or **Updated:**",
                    document_id=document_id,
                    source=source,
                    transform=_parse_display_date,
                )
            )
        elif category == "in-app-copy":
            issues.extend(
                _validate_single_header(
                    text,
                    pattern=COPY_VERSION_RE,
                    expected=document.get("version", ""),
                    missing_code="missing-copy-version-header",
                    duplicate_code="duplicate-copy-version-header",
                    mismatch_code="copy-version-mismatch",
                    label="**Copy version:**",
                    document_id=document_id,
                    source=source,
                )
            )
            issues.extend(
                _validate_single_header(
                    text,
                    pattern=IN_APP_DATE_RE,
                    expected=document.get("effective_date", ""),
                    missing_code="missing-effective-header",
                    duplicate_code="duplicate-effective-header",
                    mismatch_code="effective-date-mismatch",
                    label="**Effective:**",
                    document_id=document_id,
                    source=source,
                    transform=_parse_display_date,
                )
            )
        issues.extend(
            scan_text(
                text,
                document_id=document_id,
                path=source,
                consumer_facing=category in CONSUMER_CATEGORIES,
                allowed_runtime_tokens=runtime_tokens,
            )
        )
        link_issues, found_external = validate_links(
            text,
            root=root,
            source_path=source_path,
            document_id=document_id,
            public_routes=declared_public_routes,
            allowed_routes=allowed_routes,
        )
        issues.extend(link_issues)
        external_urls.update(found_external)

    for prefix in sorted(set(CATEGORY_PREFIXES.values())):
        package_root = root / prefix
        if not package_root.exists():
            continue
        for markdown_path in sorted(package_root.rglob("*.md")):
            if markdown_path.name == "README.md":
                continue
            relative = markdown_path.relative_to(root).as_posix()
            if relative not in source_paths:
                issues.append(
                    Issue(
                        "error",
                        "unmanifested-source",
                        "every non-README package Markdown file must be listed in the manifest",
                        path=relative,
                    )
                )

    issues.extend(_repo_sensitive_scan(root))

    if check_external:
        for url in sorted(external_urls):
            failure = _check_external_url(url)
            if failure:
                issues.append(Issue("error", "external-link", f"{url} is not reachable: {failure}"))

    return issues


def update_hashes(root: Path, manifest_path: Path, *, write: bool) -> tuple[dict[str, str], list[str]]:
    manifest = load_manifest(manifest_path)
    documents = manifest.get("documents")
    if not isinstance(documents, list):
        raise ManifestError("documents must be a list")

    hashes: dict[str, str] = {}
    missing: list[str] = []
    for document in documents:
        if not isinstance(document, dict) or not isinstance(document.get("id"), str) or not _safe_relative(document.get("source")):
            continue
        source = _repo_path(root, document["source"])
        if not source.exists():
            missing.append(document["source"])
            continue
        digest = sha256_file(source)
        hashes[document["id"]] = digest
        if write:
            document["sha256"] = digest

    if write:
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return hashes, missing


def _registry_entry(document: dict[str, Any], target: str) -> dict[str, Any]:
    exports = document.get("exports", {})
    return {
        "id": document["id"],
        "title": document["title"],
        "category": document["category"],
        "version": document["version"],
        "effectiveDate": document["effective_date"],
        "status": document["status"],
        "region": document["region"],
        "url": document["public_url"],
        "sha256": document["sha256"],
        "materialChange": document["material_change"],
        "acceptance": document["acceptance"],
        "publicationCommit": document["publication_commit"],
        "file": exports.get(target),
        "runtimeTokens": document.get("runtime_tokens", []) if target == "app" else [],
    }


def _safe_export_root(root: Path, output: Path) -> Path:
    resolved = output.resolve()
    if resolved == root.resolve():
        raise ManifestError("output cannot be the repository root")
    try:
        relative = resolved.relative_to(root.resolve())
    except ValueError:
        return resolved
    if relative.parts and relative.parts[0] in {
        ".git",
        "00-control",
        "10-public-legal",
        "20-in-app-copy",
        "30-apple-submission",
        "40-internal-compliance",
        "50-regional",
        "60-user-guides",
        "90-future-review",
        "scripts",
        "tests",
    }:
        raise ManifestError(f"output cannot overwrite a source/tooling directory: {relative}")
    return resolved


def export_approved(
    root: Path,
    manifest_path: Path,
    output: Path,
    *,
    replace: bool = False,
) -> list[Path]:
    issues = validate_manifest(root, manifest_path, release=True)
    errors = [issue for issue in issues if issue.severity == "error"]
    if errors:
        rendered = "\n".join(str(issue) for issue in errors[:20])
        suffix = "" if len(errors) <= 20 else f"\n... and {len(errors) - 20} more error(s)"
        raise ManifestError(f"release validation failed:\n{rendered}{suffix}")

    manifest = load_manifest(manifest_path)
    output = _safe_export_root(root, output)
    if output.exists():
        if not replace:
            raise ManifestError(f"output already exists; pass --replace to replace it: {output}")
        shutil.rmtree(output)
    output.mkdir(parents=True)

    written: list[Path] = []
    registries: dict[str, list[dict[str, Any]]] = {target: [] for target in ALLOWED_EXPORT_TARGETS}
    selected = [document for document in manifest["documents"] if document.get("status") in RELEASE_STATUSES]

    for document in selected:
        source = _repo_path(root, document["source"])
        for target, relative in sorted(document.get("exports", {}).items()):
            destination = output / target / PurePosixPath(relative)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(source.read_bytes())
            written.append(destination)
        for target in document.get("registry_targets", []):
            registries[target].append(_registry_entry(document, target))

    targets_summary: dict[str, Any] = {}
    for target in sorted(ALLOWED_EXPORT_TARGETS):
        registry_name = manifest["export_targets"][target]["registry"]
        registry_path = output / target / PurePosixPath(registry_name)
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        registry = {
            "schemaVersion": manifest["schema_version"],
            "product": manifest["product"],
            "target": target,
            "documents": sorted(registries[target], key=lambda item: item["id"]),
        }
        registry_path.write_text(json.dumps(registry, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        written.append(registry_path)
        targets_summary[target] = {
            "registry": str(PurePosixPath(target) / registry_name),
            "documentIds": [item["id"] for item in registry["documents"]],
        }

    export_manifest = {
        "schemaVersion": 1,
        "product": manifest["product"],
        "sourceManifestSha256": sha256_file(manifest_path),
        "targets": targets_summary,
    }
    export_manifest_path = output / "export-manifest.json"
    export_manifest_path.write_text(json.dumps(export_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    written.append(export_manifest_path)
    return written


def validate_rendered(root: Path, manifest_path: Path, document_id: str, rendered_path: Path) -> list[Issue]:
    manifest = load_manifest(manifest_path)
    document = next((item for item in manifest.get("documents", []) if item.get("id") == document_id), None)
    if not isinstance(document, dict):
        raise ManifestError(f"unknown document id: {document_id}")
    if document.get("category") != "in-app-copy":
        raise ManifestError("validate-rendered accepts only in-app-copy document IDs")
    text = rendered_path.read_text(encoding="utf-8")
    return scan_text(
        text,
        document_id=document_id,
        path=str(rendered_path),
        consumer_facing=True,
        rendered=True,
    )


def _print_issues(issues: Sequence[Issue]) -> int:
    for issue in sorted(issues, key=lambda item: (item.severity != "error", item.path or "", item.line or 0, item.code)):
        print(issue)
    errors = sum(issue.severity == "error" for issue in issues)
    warnings = sum(issue.severity == "warning" for issue in issues)
    print(f"Result: {errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="manifest path")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="validate schema, sources, hashes, links, and forbidden content")
    validate_parser.add_argument("--release", action="store_true", help="enforce approved-export release gates")
    validate_parser.add_argument("--check-external", action="store_true", help="perform live external HTTPS checks")

    hashes_parser = subparsers.add_parser("hashes", help="calculate canonical source SHA-256 values")
    hashes_parser.add_argument("--write", action="store_true", help="write calculated values to the manifest")

    export_parser = subparsers.add_parser("export", help="generate fail-closed approved website/app exports")
    export_parser.add_argument("--output", type=Path, required=True, help="output directory")
    export_parser.add_argument("--replace", action="store_true", help="replace an existing output directory")

    rendered_parser = subparsers.add_parser("validate-rendered", help="verify fully rendered in-app copy has no unresolved runtime tokens")
    rendered_parser.add_argument("document_id", help="in-app manifest document ID")
    rendered_parser.add_argument("path", type=Path, help="rendered copy file")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()
    manifest_path = args.manifest
    if not manifest_path.is_absolute():
        manifest_path = root / manifest_path

    try:
        if args.command == "validate":
            return _print_issues(validate_manifest(root, manifest_path, release=args.release, check_external=args.check_external))
        if args.command == "hashes":
            hashes, missing = update_hashes(root, manifest_path, write=args.write)
            for document_id, digest in sorted(hashes.items()):
                print(f"{document_id} {digest}")
            for source in missing:
                print(f"MISSING {source}", file=sys.stderr)
            if args.write:
                print(f"Updated {len(hashes)} manifest hash(es).")
            return 1 if missing else 0
        if args.command == "export":
            output = args.output if args.output.is_absolute() else root / args.output
            written = export_approved(root, manifest_path, output, replace=args.replace)
            for path in sorted(written):
                print(path)
            print(f"Exported {len(written)} file(s).")
            return 0
        if args.command == "validate-rendered":
            rendered_path = args.path if args.path.is_absolute() else root / args.path
            return _print_issues(validate_rendered(root, manifest_path, args.document_id, rendered_path))
    except (ManifestError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
