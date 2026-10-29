#!/usr/bin/env bash
# Publish only verified assets; a matching unpublished draft can be resumed.
set -euo pipefail
: "${RELEASE_TAG:?}" "${GITHUB_REPOSITORY:?}" "${RUNNER_TEMP:?}"
python -c 'import sys; from scripts.check_content import version_from_tag; version_from_tag(sys.argv[1])' "$RELEASE_TAG"
head=$(git rev-parse HEAD)

find_release() {
  gh api --paginate "repos/$GITHUB_REPOSITORY/releases" \
    --jq ".[] | select(.tag_name == \"$RELEASE_TAG\") | .id" > "$RUNNER_TEMP/release-ids.txt"
  mapfile -t release_ids < "$RUNNER_TEMP/release-ids.txt"
  test "${#release_ids[@]}" -le 1
}

ensure_tag() {
  if git ls-remote --exit-code origin "refs/tags/$RELEASE_TAG" > "$RUNNER_TEMP/release-tag.txt"; then
    git fetch origin "refs/tags/$RELEASE_TAG"
    test "$(git rev-parse 'FETCH_HEAD^{commit}')" = "$head"
  else
    status=$?
    test "$status" -eq 2 || return "$status"
    git tag "$RELEASE_TAG" "$head"
    git push origin "refs/tags/$RELEASE_TAG"
  fi
}

find_release
if [[ ${#release_ids[@]} -eq 0 ]]; then
  ensure_tag
  flags=()
  if [[ "$RELEASE_TAG" == *-* ]]; then flags+=(--prerelease); fi
  gh release create "$RELEASE_TAG" \
    "$RUNNER_TEMP/release/custom-instructions-compact.txt" \
    "$RUNNER_TEMP/release/custom-instructions-extended.txt" \
    --draft --verify-tag --fail-on-no-commits --target "$head" \
    --title "$RELEASE_TAG - ChatGPT Custom Instructions" \
    --notes-file "$RUNNER_TEMP/release/release-notes.md" "${flags[@]}"
  find_release
fi
test "${#release_ids[@]}" -eq 1
[[ "${release_ids[0]}" =~ ^[0-9]+$ ]]
gh api "repos/$GITHUB_REPOSITORY/releases/${release_ids[0]}" > "$RUNNER_TEMP/release-metadata.json"
python - <<'PY'
import json
import os
from pathlib import Path
import re
import subprocess

root = Path(os.environ["RUNNER_TEMP"])
release = json.loads((root / "release-metadata.json").read_text())
tag = os.environ["RELEASE_TAG"]
if release["tag_name"] != tag or not release["draft"]:
    raise SystemExit("Existing published releases are not changed")
if release["name"] != f"{tag} - ChatGPT Custom Instructions":
    raise SystemExit("Draft title differs from the requested release")
target = release["target_commitish"]
if not re.fullmatch(r"[0-9a-f]{40}", target):
    raise SystemExit("Draft target must be an exact commit")
subprocess.run(["git", "merge-base", "--is-ancestor", target, "HEAD"], check=True)
if release["body"] != (root / "release" / "release-notes.md").read_text():
    raise SystemExit("Draft notes differ from the validated release notes")
expected = {"custom-instructions-compact.txt", "custom-instructions-extended.txt"}
assets = release["assets"]
if len(assets) != 2 or {a["name"] for a in assets} != expected:
    raise SystemExit("Draft must contain exactly the two expected TXT assets")
for asset in assets:
    if asset["state"] != "uploaded" or asset["size"] != (root / "release" / asset["name"]).stat().st_size:
        raise SystemExit("Draft attachment is incomplete or has a different size")
PY

gh release download "$RELEASE_TAG" --dir "$RUNNER_TEMP/release-check" --pattern 'custom-instructions-*.txt'
cmp "$RUNNER_TEMP/release/custom-instructions-compact.txt" "$RUNNER_TEMP/release-check/custom-instructions-compact.txt"
cmp "$RUNNER_TEMP/release/custom-instructions-extended.txt" "$RUNNER_TEMP/release-check/custom-instructions-extended.txt"
# Draft creation does not guarantee that GitHub has materialized the tag.
ensure_tag
latest=true
if [[ "$RELEASE_TAG" == *-* ]]; then latest=false; fi
gh release edit "$RELEASE_TAG" --target "$head" --verify-tag --draft=false --latest="$latest"
git fetch origin "refs/tags/$RELEASE_TAG"
test "$(git rev-parse 'FETCH_HEAD^{commit}')" = "$head"
