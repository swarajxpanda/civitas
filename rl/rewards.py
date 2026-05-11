from __future__ import annotations

from core.civilization import Civilization


def compute_reward(civilization: Civilization) -> float:
    return civilization.population * 0.2 + civilization.resources * 0.1 + civilization.stability * 0.5
