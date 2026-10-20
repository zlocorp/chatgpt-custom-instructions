# Automated releases

The versioned Markdown instruction files in the repository root are the **single source of truth**. The two `.txt` downloads attached to each GitHub Release are generated when a new version tag is pushed. They are not maintained or committed independently.

The existing [v5 release](https://github.com/zlocorp/chatgpt-custom-instructions/releases/tag/v5) is already published and must not be re-created. Its original attachments remain available even after older committed TXT copies are removed from `main`.

## Publishing a future version

1. Update the instruction blocks in the versioned Markdown files and their stated character counts. Update the README comparison table accordingly.
2. Open a pull request or push the changes to `main`. The **Content checks** workflow validates counts, local links, tests, and generated TXT files without publishing a release.
3. When the changes are ready, create **a new tag**, such as `v5.1`, from the final tested commit on `main`, then push that tag.
4. **Publish release** runs on the tag, verifies the correct version's prompts, generates TXT downloads and version-aware introductory notes, and creates the GitHub Release with automatically generated changelog notes. It does not edit existing releases.

The workflow derives Markdown filenames from the **version tag**: `v5.1` requires new `v5.1-free.md` and `v5.1-5000.md`, and `v6` requires `v6-free.md` and `v6-5000.md`. A prerelease tag such as `v6-rc.1` uses the `v6-*` files. Earlier Markdown versions are preserved unchanged. Only explicit new Git tags trigger publication. A normal push to `main` cannot publish a release.

To preview the exact generated files locally without creating a release:

```bash
python -m unittest discover -s tests -v
python scripts/check_content.py --release-tag v5 --export-dir /tmp/ci-release-preview
```

For a future release, replace `v5` with its new tag after creating the matching Markdown source files. On Windows, replace the output directory with a suitable local path. This preview is read-only with respect to the repository and writes only generated files to the requested directory.

## Guardrails

- The existing release tag must be present; the release command uses `--verify-tag`.
- Existing releases are not overwritten or recreated.
- The release job runs the same tests and validation as the content checks.
- Every prompt must have one `text` code block, accurate stated character count, valid local links, and fit its plan's character limit.
- Release notes describe the tagged variant and are prefixed to GitHub's generated changelog, so they do not carry a stale hard-coded version number.
- Only the release workflow uses the narrowly scoped `contents: write` permission; validation workflows are read-only.
