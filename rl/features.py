from __future__ import annotations

from core.civilization import Civilization


def encode_civilization(civilization: Civilization) -> list[float]:
    return [
        float(civilization.resources),
        float(civilization.military),
        float(civilization.population),
        float(civilization.territory),
        float(civilization.food),
        float(civilization.stability),
    ]
