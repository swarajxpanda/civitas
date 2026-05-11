from __future__ import annotations


class ShortTermMemory:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.items: list = []

    def add(self, item) -> None:
        self.items.append(item)
        if len(self.items) > self.capacity:
            self.items.pop(0)

