from __future__ import annotations

import random

from core.civilization import Civilization


def mutate_traits(civilization: Civilization, rate: float = 0.05) -> Civilization:
    civilization.aggression = min(1.0, max(0.0, civilization.aggression + random.uniform(-rate, rate)))
    civilization.trade_preference = min(
        1.0, max(0.0, civilization.trade_preference + random.uniform(-rate, rate))
    )
    civilization.expansionism = min(1.0, max(0.0, civilization.expansionism + random.uniform(-rate, rate)))
    return civilization
