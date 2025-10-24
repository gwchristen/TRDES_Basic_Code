
from __future__ import annotations
from datetime import date

def weekday_of(iso_date: str) -> str:
    y, m, d = map(int, iso_date.split('-'))
    wd = date(y, m, d).strftime('%A')
    return wd
