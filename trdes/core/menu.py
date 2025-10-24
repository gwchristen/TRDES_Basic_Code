
# Optional textual menu for nostalgia; not used by default CLI
from __future__ import annotations
from pathlib import Path
from .weekday import weekday_of

def run_menu() -> None:
    while True:
        print("TRDES Menu")
        print("1) Weekday of a date")
        print("Q) Quit")
        choice = input("> ").strip().lower()
        if choice == '1':
            d = input("Enter date (YYYY-MM-DD): ").strip()
            print(weekday_of(d))
        elif choice in {'q', 'quit', 'exit'}:
            break
