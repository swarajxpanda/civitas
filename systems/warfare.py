from __future__ import annotations

from core.civilization import Civilization


def resolve_attack(attacker: Civilization, defender: Civilization) -> dict:
    outcome = {
        "attacker": attacker.name,
        "defender": defender.name,
        "winner": None,
        "resources_shift": 0,
        "population_loss": 0,
    }

    attack_power = attacker.military + attacker.population * 0.2 + attacker.aggression * 10
    defense_power = defender.military + defender.population * 0.2 + defender.stability * 0.1

    if attack_power > defense_power:
        attacker.resources += 30
        defender.resources = max(0.0, defender.resources - 30)
        defender.population = max(0.0, defender.population - 10)
        defender.military = max(0.0, defender.military - 5)
        defender.stability -= 10
        attacker.stability += 2
        outcome["winner"] = attacker.name
        outcome["resources_shift"] = 30
        outcome["population_loss"] = 10
    else:
        attacker.resources = max(0.0, attacker.resources - 20)
        attacker.population = max(0.0, attacker.population - 10)
        attacker.military = max(0.0, attacker.military - 5)
        attacker.stability -= 8
        defender.stability += 1
        outcome["winner"] = defender.name
        outcome["resources_shift"] = -20
        outcome["population_loss"] = 10

    return outcome
