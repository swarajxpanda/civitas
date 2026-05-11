from __future__ import annotations

from core.civilization import Civilization


def choose_rule_based_action(civilization: Civilization, enemy: Civilization | None = None):
    return civilization.choose_action(enemy)
