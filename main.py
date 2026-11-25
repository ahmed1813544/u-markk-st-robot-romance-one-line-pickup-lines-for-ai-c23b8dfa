"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line to entry.txt in the output directory
given by MAKEFUN_OUTPUT_DIR, or /output/entry.txt by default.
Stdlib only, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

LINE = "Are you a CAPTCHA? Because every time I try to prove I'm human, I keep picking you."


def main() -> None:
    # The gate allows 1-200 characters; keep the line a single line.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
