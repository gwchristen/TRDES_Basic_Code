
from __future__ import annotations
from pathlib import Path
from collections import defaultdict

def accumulate(path: Path, value_col: int, group_col: int | None = None, delimiter: str = ',') -> list[tuple[str, float]]:
    totals: dict[str, float] = defaultdict(float)
    for i, line in enumerate(path.read_text(encoding='utf-8', errors='replace').splitlines(), start=1):
        if not line.strip():
            continue
        parts = line.split(delimiter)
        try:
            val = float(parts[value_col - 1])
        except Exception:
            # Skip header or invalid
            continue
        key = parts[group_col - 1] if group_col else "__total__"
        totals[key] += val
    return sorted(totals.items(), key=lambda kv: kv[0])
