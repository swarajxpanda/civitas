from __future__ import annotations

from core.civilization import Civilization
from core.event import Event


def resolve_trade(a: Civilization, b: Civilization) -> None:
    a.resources += 10
    b.resources += 10
    a.food += 5
    b.food += 5
    a.stability += 1
    b.stability += 1


def apply_economic_growth(civilization: Civilization, events: list[Event], turn: int) -> None:
    prosperity = max(0.0, civilization.resources - 100.0) + max(0.0, civilization.food - 100.0)
    if prosperity <= 0:
        return

    growth = min(5.0, prosperity / 50.0)
    civilization.population += growth
    civilization.resources += growth * 0.5
    civilization.stability += growth * 0.25
    events.append(
        Event(
            turn=turn,
            kind="prosperity",
            source=civilization.name,
            details={"growth": growth},
        )
    )
