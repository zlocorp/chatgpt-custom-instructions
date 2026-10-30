#!/usr/bin/env python3
"""Validate versioned Markdown prompts and build ephemeral release assets."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TAG_PATTERN = re.compile(
    r"v(?P<version>[1-9][0-9]*(?:\.(?:0|[1-9][0-9]*)){0,2})"
    r"(?:-(?:alpha|beta|rc)\.(?:0|[1-9][0-9]*))?\Z"
)
CHANGELOG_VERSION = re.compile(r"^## (v[^ \n]+)(?: - [^\n]+)?$", re.MULTILINE)
PROMPT_BLOCK = re.compile(r"^```text[ \t]*\n(.*?)\n```[ \t]*$", re.MULTILINE | re.DOTALL)
DECLARED_COUNT = re.compile(r"The prompt (?:contains|is) \*\*([0-9,]+) characters\*\*", re.IGNORECASE)
DECLARED_CRLF_COUNT = re.compile(
    r"\*\*([0-9,]+)(?: characters)?\*\* with CRLF(?: line breaks| endings)", re.IGNORECASE
)
VARIANTS = {"compact": ("free", 1500), "extended": ("5000", 5000)}


def version_from_tag(tag: str) -> str:
    if not TAG_PATTERN.fullmatch(tag):
        raise ValueError(f"Invalid release tag {tag!r}; expected v5, v5.1, v5.1.2, or v5.1-rc.1")
    return tag


def source_version(tag: str) -> str:
    """Minor and prerelease tags reuse the current major-version Markdown files."""
    match = TAG_PATTERN.fullmatch(tag)
    if not match:
        raise ValueError(f"Invalid release tag {tag!r}")
    return f"v{match.group('version').split('.')[0]}"


def latest_version(root: Path) -> str:
    """Use the newest released version in CHANGELOG, not the major source filename."""
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    for match in CHANGELOG_VERSION.finditer(changelog):
        return version_from_tag(match.group(1))
    raise ValueError("CHANGELOG.md: no valid version heading found")


def extract_prompt(markdown: str, path: Path, limit: int) -> str:
    markdown = markdown.replace("\r\n", "\n")
    matches = list(PROMPT_BLOCK.finditer(markdown))
    if len(matches) != 1:
        raise ValueError(f"{path}: expected exactly one fenced ```text block; found {len(matches)}")
    prompt = matches[0].group(1) + "\n"
    declared = DECLARED_COUNT.search(markdown)
    if not declared:
        raise ValueError(f"{path}: missing declared character count")
    expected = int(declared.group(1).replace(",", ""))
    if len(prompt) != expected:
        raise ValueError(f"{path}: {len(prompt)} characters, but document declares {expected}")
    if len(prompt) > limit:
        raise ValueError(f"{path}: {len(prompt)} characters, exceeds {limit} limit")
    crlf_count = len(prompt.replace("\n", "\r\n"))
    if crlf_count > limit:
        raise ValueError(f"{path}: {crlf_count} characters with CRLF, exceeds {limit} limit")
    declared_crlf = DECLARED_CRLF_COUNT.search(markdown)
    if declared_crlf:
        expected_crlf = int(declared_crlf.group(1).replace(",", ""))
        if crlf_count != expected_crlf:
            raise ValueError(f"{path}: {crlf_count} characters with CRLF, but document declares {expected_crlf}")
    return prompt


def validate_local_links(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        relative = target.split("#", 1)[0]
        if relative and not (path.parent / relative).exists():
            raise ValueError(f"{path}: missing local Markdown target {target}")


def load_validated_prompts(root: Path, version: str) -> dict[str, str]:
    prompts: dict[str, str] = {}
    readme = (root / "README.md").read_text(encoding="utf-8")
    for variant, (suffix, limit) in VARIANTS.items():
        path = root / "prompts" / f"{source_version(version)}-{suffix}.md"
        markdown = path.read_text(encoding="utf-8")
        prompt = extract_prompt(markdown, path, limit)
        declared_in_readme = f"| **{version} {variant.title()}** | {len(prompt):,} characters"
        if declared_in_readme not in readme:
            raise ValueError(f"README.md: missing or stale character count for {version} {variant}")
        prompts[variant] = prompt
        crlf_count = len(prompt.replace("\n", "\r\n"))
        print(f"PASS {path.name}: {len(prompt)}/{limit} LF, {crlf_count}/{limit} CRLF characters")
    for page in sorted((root / "prompts").glob("*.md")):
        validate_local_links(page)
    validate_local_links(root / "README.md")
    print("PASS local Markdown links and README counts")
    return prompts


def render_release_notes(tag: str, prompts: dict[str, str]) -> str:
    return (
        f"# {tag} — ChatGPT Custom Instructions\n\n"
        "Two independently maintained general-purpose Custom Instructions variants:\n\n"
        f"- **Compact:** {len(prompts['compact']):,} / 1,500 characters (Free and Go).\n"
        f"- **Extended:** {len(prompts['extended']):,} / 5,000 characters (larger Custom Instructions field).\n\n"
        "Copy one TXT attachment into ChatGPT Custom Instructions, replacing previous general-purpose instructions.\n\n"
        "Performance improvements have not yet been established in controlled tests. "
        "See the repository README for setup and attribution.\n"
    )


def export_assets(output_dir: Path, tag: str, prompts: dict[str, str]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for variant, prompt in prompts.items():
        path = output_dir / f"custom-instructions-{variant}.txt"
        path.write_bytes(prompt.encode("utf-8"))
        if path.read_bytes() != prompt.encode("utf-8"):
            raise ValueError(f"Failed to verify generated {path}")
        print(f"BUILT {path.name}")
    (output_dir / "release-notes.md").write_text(render_release_notes(tag, prompts), encoding="utf-8")
    print("BUILT release-notes.md")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-tag", help="Validate prompts for this exact release version tag")
    parser.add_argument("--export-dir", type=Path, help="Generate release assets into this external directory")
    args = parser.parse_args(argv)

    version = version_from_tag(args.release_tag) if args.release_tag else latest_version(ROOT)
    prompts = load_validated_prompts(ROOT, version)
    if args.export_dir:
        export_assets(args.export_dir, args.release_tag or version, prompts)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        sys.exit(1)
