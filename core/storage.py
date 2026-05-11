from __future__ import annotations

from pathlib import Path
import json


class WorldStorage:
    @staticmethod
    def save_json(path: str | Path, payload: dict) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @staticmethod
    def load_json(path: str | Path) -> dict:
        path = Path(path)
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))

