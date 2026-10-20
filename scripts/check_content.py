#!/usr/bin/env python3
"""Check prompt character limits, release exports, and local Markdown links."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = {
    "v5-free.md": (1500, 1394, "compact"),
    "v5-5000.md": (5000, 4949, "extended"),
}

def check():
    for filename, (limit, expected, variant) in PROMPTS.items():
        source = (ROOT / filename).read_text(encoding="utf-8")
        blocks = re.findall(r"```text\n(.*?)\n```", source, re.S)
        if len(blocks) != 1:
            raise ValueError(f"{filename}: expected exactly one text block")
        prompt = blocks[0] + "\n"
        if len(prompt) != expected or len(prompt) > limit:
            raise ValueError(f"{filename}: {len(prompt)} characters (expected {expected}, limit {limit})")
        export = ROOT / "release" / f"custom-instructions-{variant}.txt"
        if export.read_bytes() != prompt.encode("utf-8"):
            raise ValueError(f"{export}: does not match prompt")
        print(f"PASS {filename}: {len(prompt)}/{limit}, export matches")

    for path in [ROOT / "README.md", *ROOT.glob("v5-*.md")]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (path.parent / relative).exists():
                raise ValueError(f"{path.name}: missing link {target}")
    print("PASS local Markdown links")

if __name__ == "__main__":
    try:
        check()
    except (OSError, ValueError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        sys.exit(1)
