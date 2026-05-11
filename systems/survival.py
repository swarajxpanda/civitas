from __future__ import annotations

from core.civilization import Civilization
from core.event import Event


def apply_survival_step(civilization: Civilization, turn: int) -> list[Event]:
    events: list[Event] = []

    food_need = civilization.population * 0.15
    upkeep_need = civilization.military * 0.08
    total_need = food_need + upkeep_need

    if civilization.food >= food_need:
        civilization.food -= food_need
    else:
        deficit = food_need - civilization.food
        civilization.food = 0.0
        starvation_loss = min(civilization.population, deficit * 0.5)
        civilization.population = max(0.0, civilization.population - starvation_loss)
        civilization.stability -= 6
        events.append(
            Event(
                turn=turn,
                kind="starvation",
                source=civilization.name,
                details={"population_loss": starvation_loss, "deficit": deficit},
            )
        )

    if civilization.resources >= upkeep_need:
        civilization.resources -= upkeep_need
    else:
        deficit = upkeep_need - civilization.resources
        civilization.resources = 0.0
        military_loss = min(civilization.military, deficit * 0.4)
        civilization.military = max(0.0, civilization.military - military_loss)
        civilization.stability -= 4
        events.append(
            Event(
                turn=turn,
                kind="upkeep_failure",
                source=civilization.name,
                details={"military_loss": military_loss, "deficit": deficit},
            )
        )

    if civilization.food > 120 and civilization.resources > 120 and civilization.stability > 60:
        growth = 2.0
        civilization.population += growth
        civilization.stability += 1
        events.append(Event(turn, "population_growth", civilization.name, details={"growth": growth}))

    if civilization.resources < 25 or civilization.food < 15:
        civilization.stability -= 5
        events.append(
            Event(
                turn=turn,
                kind="scarcity",
                source=civilization.name,
                details={"resources": civilization.resources, "food": civilization.food},
            )
        )

    civilization.population = max(0.0, civilization.population)
    civilization.resources = max(0.0, civilization.resources)
    civilization.food = max(0.0, civilization.food)
    civilization.military = max(0.0, civilization.military)
    civilization.stability = min(100.0, max(0.0, civilization.stability))

    return events


def is_collapsed(civilization: Civilization) -> bool:
    return civilization.population <= 0 or civilization.stability <= 0
