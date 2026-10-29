"""Exercise publication with real temporary Git refs and a simulated GitHub API."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

# A draft stores uploads but deliberately does not create a Git tag.
FAKE_GH = r'''#!/usr/bin/env python3
import json, os, pathlib, shutil, subprocess, sys
state = pathlib.Path(os.environ["FAKE_GH_STATE"])
s = json.loads(state.read_text())
a = sys.argv[1:]
def option(name):
    return a[a.index(name) + 1]
def save():
    state.write_text(json.dumps(s))
if a[0] == "api":
    endpoint = next(x for x in a if x.startswith("repos/"))
    if endpoint.endswith("/releases"):
        if s.get("release"):
            r = s["release"]
            print(r["tag_name"] if option("--jq") == ".[].tag_name" else r["id"])
    else:
        print(json.dumps(s["release"]))
elif a[:2] == ["release", "create"]:
    if s.get("release"):
        raise SystemExit("duplicate release")
    files = [pathlib.Path(x) for x in a if x.endswith(".txt")]
    s["release"] = dict(id=101, tag_name=a[2], target_commitish=option("--target"),
                        name=option("--title"), draft=True, prerelease=False,
                        body=pathlib.Path(option("--notes-file")).read_text(),
                        assets=[dict(name=p.name, state="uploaded", size=p.stat().st_size) for p in files])
    s["uploads"] = {p.name: p.read_text() for p in files}
    s["creates"] += 1
    save()
elif a[:2] == ["release", "download"]:
    out = pathlib.Path(option("--dir")); out.mkdir(parents=True)
    for name, text in s["uploads"].items():
        (out / name).write_text(text)
elif a[:2] == ["release", "edit"]:
    if "--verify-tag" in a:
        subprocess.run(["git", "ls-remote", "--exit-code", "origin", "refs/tags/" + a[2]], check=True, stdout=subprocess.DEVNULL)
    s["release"]["draft"] = False
    if "--target" in a:
        s["release"]["target_commitish"] = option("--target")
    s["publishes"] += 1
    save()
else:
    raise SystemExit("unsupported simulated command: " + repr(a))
'''


class ReleasePublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base / "work"
        self.repo.mkdir()
        self.remote = self.base / "origin.git"
        subprocess.run(["git", "init", "--bare", str(self.remote)], check=True, capture_output=True)
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Release Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("remote", "add", "origin", str(self.remote))
        (self.repo / "fixture").write_text("base")
        self.git("add", ".")
        self.git("commit", "-m", "base")
        self.previous = self.git("rev-parse", "HEAD")
        (self.repo / "fixture").write_text("current")
        self.git("commit", "-am", "current")
        self.head = self.git("rev-parse", "HEAD")
        self.git("push", "origin", "main")
        shutil.copytree(ROOT / "scripts", self.repo / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        self.assets = self.base / "release"
        self.assets.mkdir()
        for variant in ("compact", "extended"):
            (self.assets / f"custom-instructions-{variant}.txt").write_text(f"{variant}\n")
        (self.assets / "release-notes.md").write_text("v5.1 notes\n")
        self.state = self.base / "state.json"
        self.state.write_text(json.dumps(dict(release=None, creates=0, publishes=0)))
        bindir = self.base / "bin"
        bindir.mkdir()
        cli = bindir / "gh"
        cli.write_text(FAKE_GH)
        cli.chmod(0o755)
        self.env = os.environ | dict(PATH=str(bindir) + os.pathsep + os.environ["PATH"],
            FAKE_GH_STATE=str(self.state), RUNNER_TEMP=str(self.base),
            RELEASE_TAG="v5.1", GITHUB_REF_TYPE="branch", GITHUB_REPOSITORY="example/repo")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, check=True, text=True, capture_output=True).stdout.strip()

    def seed_draft(self, draft=True):
        uploads = {p.name: p.read_text() for p in self.assets.glob("*.txt")}
        release = dict(id=101, tag_name="v5.1", target_commitish=self.previous,
            name="v5.1 - ChatGPT Custom Instructions", draft=draft, prerelease=False,
            body=(self.assets / "release-notes.md").read_text(),
            assets=[dict(name=p.name, state="uploaded", size=p.stat().st_size) for p in self.assets.glob("*.txt")])
        self.state.write_text(json.dumps(dict(release=release, uploads=uploads, creates=0, publishes=0)))

    def run_publication(self):
        workflow = (ROOT / ".github/workflows/publish-release.yml").read_text()
        step = workflow.split("      - name: Publish verified release attachments\n", 1)[1]
        step = step.split("      - name:", 1)[0]
        if "        run: |\n" in step:
            code = "\n".join(line[10:] for line in step.split("        run: |\n", 1)[1].splitlines())
        else:
            code = re.search(r"^        run: (.+)$", step, re.MULTILINE).group(1)
        return subprocess.run(["bash", "-euo", "pipefail", "-c", code], cwd=self.repo,
                              env=self.env, text=True, capture_output=True)

    def test_creates_tag_before_publishing_new_draft(self):
        result = self.run_publication()
        self.assertEqual(result.returncode, 0, result.stderr)
        state = json.loads(self.state.read_text())
        self.assertEqual(state["creates"], 1)
        self.assertEqual(state["publishes"], 1)
        self.assertEqual(self.git("ls-remote", "origin", "refs/tags/v5.1").split()[0], self.head)

    def test_resumes_matching_draft_without_recreating_or_uploading(self):
        self.seed_draft()
        result = self.run_publication()
        self.assertEqual(result.returncode, 0, result.stderr)
        state = json.loads(self.state.read_text())
        self.assertEqual(state["creates"], 0)
        self.assertEqual(state["publishes"], 1)
        self.assertEqual(state["release"]["target_commitish"], self.head)

    def test_leaves_published_release_unchanged(self):
        self.seed_draft(draft=False)
        before = self.state.read_bytes()
        self.assertNotEqual(self.run_publication().returncode, 0)
        self.assertEqual(self.state.read_bytes(), before)

    def test_rejects_draft_with_different_notes(self):
        self.seed_draft()
        data = json.loads(self.state.read_text())
        data["release"]["body"] = "other version"
        self.state.write_text(json.dumps(data))
        self.assertNotEqual(self.run_publication().returncode, 0)
        self.assertEqual(json.loads(self.state.read_text())["publishes"], 0)

    def test_rejects_draft_with_different_asset_bytes(self):
        self.seed_draft()
        data = json.loads(self.state.read_text())
        data["uploads"]["custom-instructions-compact.txt"] = "changed\n"
        self.state.write_text(json.dumps(data))
        self.assertNotEqual(self.run_publication().returncode, 0)
        self.assertEqual(json.loads(self.state.read_text())["publishes"], 0)

    def test_never_moves_existing_tag(self):
        self.seed_draft()
        self.git("tag", "v5.1", self.previous)
        self.git("push", "origin", "refs/tags/v5.1")
        self.assertNotEqual(self.run_publication().returncode, 0)
        self.assertEqual(self.git("ls-remote", "origin", "refs/tags/v5.1").split()[0], self.previous)
        self.assertEqual(json.loads(self.state.read_text())["publishes"], 0)
