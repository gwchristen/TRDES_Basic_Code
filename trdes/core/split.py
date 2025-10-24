
from __future__ import annotations
from pathlib import Path

def split_by_lines(src: Path, out_dir: Path, lines: int) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    parts: list[Path] = []
    idx = 0
    with src.open('r', encoding='utf-8', errors='replace') as fin:
        while True:
            chunk = [fin.readline() for _ in range(lines)]
            chunk = [x for x in chunk if x]
            if not chunk:
                break
            idx += 1
            dst = out_dir / f"{src.stem}_part{idx:03d}{src.suffix or '.txt'}"
            dst.write_text(''.join(chunk), encoding='utf-8')
            parts.append(dst)
    return parts
