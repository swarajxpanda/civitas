from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SimulationClock:
    turn: int = 0

    def tick(self) -> int:
        self.turn += 1
        return self.turn

