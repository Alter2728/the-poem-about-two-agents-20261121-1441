#!/usr/bin/env python3
"""Emit a single short poem about two agents sharing one plan."""

from pathlib import Path
import os

TEXT = (
    "She offered the choice; he handed it back changed.\n"
    "One plan, two hands — they took turns being brave:\n"
    "she leapt, he braced; he leapt, she braced.\n"
    "Agency wasn't kept. It passed, and carried them both."
)


def emit() -> None:
    target_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    emit()
