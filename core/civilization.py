from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import Dict, Tuple


ACTION_ATTACK = "ATTACK"
ACTION_TRADE = "TRADE"
ACTION_EXPAND = "EXPAND"
ACTION_GATHER = "GATHER"

ACTION_ORDER = (ACTION_ATTACK, ACTION_TRADE, ACTION_EXPAND, ACTION_GATHER)


@dataclass
class Civilization:
    name: str
    resources: float = 100.0
    food: float = 100.0
    military: float = 50.0
    population: float = 100.0
    territory: int = 1
    stability: float = 100.0
    alive: bool = True
    aggression: float = field(default_factory=lambda: random.uniform(0.0, 1.0))
    trade_preference: float = field(default_factory=lambda: random.uniform(0.0, 1.0))
    expansionism: float = field(default_factory=lambda: random.uniform(0.0, 1.0))
    memory: list = field(default_factory=list)

    def calculate_scores(self, enemy: Civilization | None = None) -> Dict[str, float]:
        enemy_military = enemy.military if enemy is not None else 0.0
        enemy_population = enemy.population if enemy is not None else 0.0

        attack_score = self.aggression * 100 + (self.military - enemy_military)
        trade_score = self.trade_preference * 100 + self.resources * 0.2 + self.food * 0.1
        expand_score = self.expansionism * 100 + self.resources * 0.15 + self.population * 0.05
        gather_score = 50 + max(0.0, 100.0 - self.resources) * 0.25 + max(0.0, 100.0 - self.food) * 0.15

        if enemy is not None:
            attack_score += max(0.0, self.population - enemy_population) * 0.1

        if self.stability < 40:
            attack_score -= 15
            expand_score -= 10
            trade_score += 5

        if self.food < 50:
            gather_score += 20

        return {
            ACTION_ATTACK: attack_score,
            ACTION_TRADE: trade_score,
            ACTION_EXPAND: expand_score,
            ACTION_GATHER: gather_score,
        }

    def choose_action(self, enemy: Civilization | None = None) -> Tuple[str, Dict[str, float]]:
        scores = self.calculate_scores(enemy)
        action = max(scores, key=scores.get)
        return action, scores

    def mark_dead(self) -> None:
        self.alive = False
        self.population = max(0.0, self.population)
        self.resources = max(0.0, self.resources)
        self.food = max(0.0, self.food)
        self.military = max(0.0, self.military)
        self.stability = max(0.0, self.stability)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "resources": self.resources,
            "food": self.food,
            "military": self.military,
            "population": self.population,
            "territory": self.territory,
            "stability": self.stability,
            "alive": self.alive,
            "aggression": self.aggression,
            "trade_preference": self.trade_preference,
            "expansionism": self.expansionism,
            "memory": list(self.memory),
        }
