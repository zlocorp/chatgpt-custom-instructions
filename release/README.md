# Publishing releases

Versioned Markdown files in the repository root are the source of truth. GitHub Actions generates the two downloadable TXT attachments when a new version tag is pushed.

## Publish a new version

1. Add the version's Markdown files, for example `v5.1-free.md` and `v5.1-5000.md`. Update their declared character counts and the README version table. Keep earlier versions intact.
2. Push the changes to `main` and verify that **Content checks** passes.
3. Create a tag for that version on the tested commit and push it. The **Publish release** workflow validates the prompts, generates both TXT files and release notes, and publishes the new GitHub Release.

Tag `v6` uses `v6-free.md` and `v6-5000.md`. Prerelease tag `v6-rc.1` uses those same files and marks the release as a prerelease.

Only new tags trigger publication. Ordinary commits to `main` do not create releases, and existing releases are not overwritten.

## Local validation

```bash
python -m unittest discover -s tests -v
python scripts/check_content.py --release-tag v5 --export-dir release-preview
```

Replace `v5` with the version being prepared and choose any local output directory. This creates preview assets without publishing anything.

## Checks

- One fenced `text` block per Markdown variant, accurate declared character counts, valid local links, and adherence to the 1,500/5,000-character limits.
- Generated TXT files must match the source prompts.
- Release publication requires an existing tag and uses scoped GitHub Actions permissions.
