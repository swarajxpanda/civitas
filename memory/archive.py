from __future__ import annotations


class HistoricalArchive:
    def __init__(self) -> None:
        self.events: list = []

    def add(self, event) -> None:
        self.events.append(event)

