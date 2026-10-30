# Publishing releases

Versioned Markdown files in `prompts/` are the source of truth. GitHub Actions generates the two TXT attachments; do not maintain separate copies in Git.

## Prepare a version

1. For a minor release such as `v5.2`, update `prompts/v5-free.md` and `prompts/v5-5000.md` in place; for a new major version such as `v6`, create `prompts/v6-free.md` and `prompts/v6-5000.md`. Previous releases are preserved by their tags and attachments.
2. Update declared LF/CRLF counts, the README table, feedback-form options, and `CHANGELOG.md`. Use a changelog heading such as `## v5.2 - YYYY-MM-DD`.
3. Merge the changes into `main` and verify that **Content checks** passes.

## Publish

Create and push the version tag on the tested commit. Alternatively, create a branch named `release/v5.2` at that exact commit. Creating or updating this branch is an explicit publication request: the workflow creates the corresponding tag and release after validation, then removes the request branch after success.

Both routes run the tests, validate the major-version source files at the requested tag's commit, generate TXT and notes, and include the exact release tag's changelog entry. The workflow verifies the uploaded files before publishing the draft release. A tag or release that already points to different content is never overwritten.

Only release-tag pushes or creation/update of a `release/v...` branch can publish. Ordinary commits to `main` and unrelated branches do not publish releases. The source commit must already belong to `main`.

Prerelease tags such as `v6-rc.1` use the same `prompts/v6-free.md` and `prompts/v6-5000.md` sources and need an exact `v6-rc.1` changelog entry. Prereleases are not marked as latest.

## Local validation

```bash
python -m unittest discover -s tests -v
python scripts/check_content.py --release-tag v5.1 --export-dir release-preview
```

Replace `v5.1` with the version being prepared. This creates preview assets without publishing anything. Counts include the final newline; exported TXT uses LF and both LF/CRLF variants must fit the limit.

If publication fails after creating a draft, inspect that draft and its tag before retrying. A matching unpublished draft can be resumed only when its notes, exact asset names and bytes match the validated output, and its target is an ancestor of the tested commit. Existing published releases are never changed. Tags are created explicitly before publication and are never moved.
