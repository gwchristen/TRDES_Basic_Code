
from __future__ import annotations
from pathlib import Path

def file_exists(p: Path) -> bool:
    return p.is_file()

def dir_exists(p: Path) -> bool:
    return p.is_dir()
