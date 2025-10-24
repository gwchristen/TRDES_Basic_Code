
from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json

@dataclass
class AppConfig:
    default_encoding: str = "utf-8"
    ignore_case: bool = True
    last_root: str | None = None

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")

    @staticmethod
    def load(path: Path) -> "AppConfig":
        if not path.exists():
            return AppConfig()
        data = json.loads(path.read_text(encoding="utf-8"))
        return AppConfig(**data)
