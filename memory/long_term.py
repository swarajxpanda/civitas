from __future__ import annotations


class LongTermMemory:
    def __init__(self) -> None:
        self.relations: dict = {}

    def update(self, key, value) -> None:
        self.relations[key] = value

