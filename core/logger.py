from __future__ import annotations

from pathlib import Path
from typing import Iterable, List
import json

from .event import Event


class HistoryLogger:
    def __init__(self) -> None:
        self.events: List[Event] = []

    def append(self, event: Event) -> None:
        self.events.append(event)

    def extend(self, events: Iterable[Event]) -> None:
        self.events.extend(events)

    def to_list(self) -> list:
        return [event.to_dict() for event in self.events]

    def save_json(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_list(), indent=2), encoding="utf-8")

