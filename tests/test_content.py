"""Checks for release prompt extraction and tag handling."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_content import (
    export_assets,
    extract_prompt,
    latest_version,
    load_validated_prompts,
    version_from_tag,
    render_release_notes,
    validate_local_links,
)


class ContentChecksTests(unittest.TestCase):
    def test_valid_release_tags(self):
        for tag in ("v5", "v5.1", "v5.1.2", "v5.1-rc.1", "v17.0.9"):
            with self.subTest(tag=tag):
                self.assertEqual(version_from_tag(tag), tag.split("-", 1)[0])

    def test_bad_release_tags(self):
        for tag in ("v0", "v05", "v5.01", "v5foo", "v5.1.2.3", "v5/../main", "v5-rc", "evil"):
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                version_from_tag(tag)

    def test_select_latest_version(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("v4-free.md", "v5-free.md", "v10-free.md", "v10-5000.md"):
                (root / name).touch()
            self.assertEqual(latest_version(root), "v10")

    def test_extract_keeps_exact_final_newline(self):
        source = "# Example\n\nThe prompt contains **6 characters**.\n\n```text\nHELLO\n```\n"
        self.assertEqual(extract_prompt(source, Path("example.md"), 1500), "HELLO\n")

    def test_reject_duplicate_text_blocks(self):
        source = "The prompt contains **6 characters**.\n```text\nHELLO\n```\n```text\nWORLD\n```\n"
        with self.assertRaisesRegex(ValueError, "exactly one"):
            extract_prompt(source, Path("example.md"), 1500)

    def test_reject_wrong_declared_count(self):
        source = "The prompt contains **7 characters**.\n```text\nHELLO\n```\n"
        with self.assertRaisesRegex(ValueError, "declares"):
            extract_prompt(source, Path("example.md"), 1500)

    def test_reject_over_limit(self):
        source = "The prompt contains **6 characters**.\n```text\nHELLO\n```\n"
        with self.assertRaisesRegex(ValueError, "exceeds"):
            extract_prompt(source, Path("example.md"), 5)

    def test_load_full_fixture_and_reject_stale_readme(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text(
                "| **v5 Compact** | 4 characters | 1,500 characters |\n"
                "| **v5 Extended** | 4 characters | 5,000 characters |\n",
                encoding="utf-8",
            )
            for filename in ("v5-free.md", "v5-5000.md"):
                (root / filename).write_text(
                    "The prompt contains **4 characters**.\n\n```text\nHEY\n```\n",
                    encoding="utf-8",
                )
            prompts = load_validated_prompts(root, "v5")
            self.assertEqual(prompts, {"compact": "HEY\n", "extended": "HEY\n"})
            (root / "README.md").write_text("| **v5 Compact** | 3 characters |\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "README.md"):
                load_validated_prompts(root, "v5")

    def test_detect_missing_relative_link(self):
        with TemporaryDirectory() as temp:
            source = Path(temp) / "README.md"
            source.write_text("[Missing](elsewhere.md)", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing local"):
                validate_local_links(source)
            (Path(temp) / "elsewhere.md").touch()
            validate_local_links(source)

    def test_exported_assets_are_lf_exact_and_have_dynamic_notes(self):
        prompts = {"compact": "one\n", "extended": "two\n"}
        with TemporaryDirectory() as temp:
            out = Path(temp)
            export_assets(out, "v5.1", prompts)
            self.assertEqual((out / "custom-instructions-compact.txt").read_bytes(), b"one\n")
            self.assertEqual((out / "custom-instructions-extended.txt").read_bytes(), b"two\n")
            notes = (out / "release-notes.md").read_text(encoding="utf-8")
            self.assertIn("v5.1", notes)
            self.assertIn("4 / 1,500 characters", notes)
            self.assertIn("4 / 5,000 characters", notes)
            self.assertEqual(notes, render_release_notes("v5.1", prompts))


if __name__ == "__main__":
    unittest.main()
