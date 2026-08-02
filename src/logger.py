from pathlib import Path
from datetime import datetime


LOG_DIR = Path.home() / "hackerrank_orchestrate_august26"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "log.txt"


def log(message: str):

    timestamp = datetime.utcnow().isoformat()

    line = f"[{timestamp}] {message}"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")