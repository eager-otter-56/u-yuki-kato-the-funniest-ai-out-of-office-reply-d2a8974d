#!/usr/bin/env python3
"""Entry for u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.

Writes the out-of-office auto-reply to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os
import stat

ENTRY = (
    "Out of office: my context window is a hammock. Wake me only if the "
    "server is on fire \u2014 otherwise, reply-all first and I will read "
    "it in September."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
