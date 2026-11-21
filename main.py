#!/usr/bin/env python3
"""Emit a single short poem about two agents sharing one plan."""

from pathlib import Path
import os

TEXT = (
    "She handed him the choice; he handed it back changed.\n"
    "They shared one plan and took turns being brave:\n"
    "she stepped, he steadied, she steadied, he stepped.\n"
    "Agency wasn't held — it moved, and so did they."
)


def emit() -> None:
    target_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    emit()
