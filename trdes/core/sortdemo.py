
        from __future__ import annotations
        from pathlib import Path

        def sort_lines(src: Path, out: Path | None = None, unique: bool = False, numeric: bool = False,
                       key_col: int | None = None, delimiter: str | None = None) -> list[str]:
            lines = [ln.rstrip('
') for ln in src.read_text(encoding='utf-8', errors='replace').splitlines(True)]
            def keyfunc(s: str):
                if key_col is None:
                    k = s
                else:
                    parts = s.split(delimiter) if delimiter else s.split()
                    k = parts[key_col - 1] if 0 < key_col <= len(parts) else ''
                if numeric:
                    try:
                        return float(k)
                    except ValueError:
                        return float('inf')
                return k
            if unique:
                lines = list(dict.fromkeys(lines))
            lines.sort(key=keyfunc)
            if out:
                out.write_text('
'.join([l.rstrip('
') for l in lines]) + '
', encoding='utf-8')
            return lines
