
from __future__ import annotations
from datetime import date, timedelta

def add_days(iso_date: str, days: int) -> str:
    y, m, d = map(int, iso_date.split('-'))
    return (date(y, m, d) + timedelta(days=days)).isoformat()

def range_days(start_iso: str, end_iso: str) -> list[str]:
    y1, m1, d1 = map(int, start_iso.split('-'))
    y2, m2, d2 = map(int, end_iso.split('-'))
    cur = date(y1, m1, d1)
    end = date(y2, m2, d2)
    out = []
    step = 1 if cur <= end else -1
    while True:
        out.append(cur.isoformat())
        if cur == end:
            break
        cur += timedelta(days=step)
    return out
