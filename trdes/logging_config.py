
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def configure_logging(verbosity: int = 0, log_dir: Path | None = None) -> None:
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG

    log_dir = log_dir or Path.cwd() / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    logfile = log_dir / "trdes.log"

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    handler = RotatingFileHandler(logfile, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    handler.setFormatter(fmt)

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()
    root.addHandler(handler)

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    ch.setLevel(level)
    root.addHandler(ch)
