
from __future__ import annotations
from pathlib import Path
from typing import Iterable
import shutil

def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def atomic_write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    ensure_parent(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding=encoding)
    shutil.move(tmp, path)

def iter_paths(root: Path, patterns: Iterable[str] | None = None) -> Iterable[Path]:
    if patterns:
        for pat in patterns:
            yield from root.rglob(pat)
    else:
        yield from root.rglob("*")
