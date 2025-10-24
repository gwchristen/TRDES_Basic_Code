
        from __future__ import annotations
        from pathlib import Path
        from typing import Iterable
        import itertools

        def combine_files(root: Path, patterns: Iterable[str], out_path: Path, add_headers: bool = False) -> int:
            count = 0
            with out_path.open('w', encoding='utf-8', newline='') as fout:
                for pat in patterns:
                    for p in root.rglob(pat):
                        if not p.is_file():
                            continue
                        if add_headers:
                            fout.write(f"===== BEGIN {p} =====
")
                        with p.open('r', encoding='utf-8', errors='replace') as fin:
                            for line in fin:
                                fout.write(line)
                                count += 1
                        if add_headers:
                            fout.write(f"===== END {p} =====
")
            return count
