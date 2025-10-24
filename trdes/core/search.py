
        from __future__ import annotations
        from pathlib import Path
        from typing import Iterable
        import fnmatch

        def search_tokens(root: Path, patterns: Iterable[str], tokens: list[str], mode: str = 'all', ignore_case: bool = True) -> list[str]:
            results: list[str] = []
            tokens_cmp = [t.lower() for t in tokens] if ignore_case else tokens
            for pat in patterns:
                for p in root.rglob(pat):
                    if not p.is_file():
                        continue
                    try:
                        with p.open('r', encoding='utf-8', errors='replace') as f:
                            for i, line in enumerate(f, start=1):
                                hay = line.lower() if ignore_case else line
                                checks = [(t in hay) for t in tokens_cmp]
                                ok = all(checks) if mode == 'all' else any(checks)
                                if ok:
                                    results.append(f"{p}:{i}: {line.rstrip()}
")
                    except Exception as ex:
                        results.append(f"ERROR reading {p}: {ex}
")
            return results
