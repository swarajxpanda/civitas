from __future__ import annotations

from typing import Iterable, List, Tuple

from .clock import SimulationClock
from .civilization import Civilization, ACTION_ATTACK, ACTION_EXPAND, ACTION_GATHER, ACTION_TRADE
from .event import Event
from .logger import HistoryLogger
from systems.economy import apply_economic_growth, resolve_trade
from systems.survival import apply_survival_step, is_collapsed
from systems.warfare import resolve_attack


class World:
    def __init__(self, civilizations: Iterable[Civilization]):
        self.civilizations: List[Civilization] = list(civilizations)
        self.clock = SimulationClock()
        self.logger = HistoryLogger()
        self.dead_archive: List[dict] = []

    def living_civilizations(self) -> List[Civilization]:
        return [civilization for civilization in self.civilizations if civilization.alive]

    def choose_pair(self) -> Tuple[Civilization | None, Civilization | None]:
        living = self.living_civilizations()
        if len(living) < 2:
            return (living[0], None) if living else (None, None)
        return living[0], living[1]

    def step(self) -> list[Event]:
        turn = self.clock.tick()
        turn_events: list[Event] = []

        actor_a, actor_b = self.choose_pair()
        if actor_a is None:
            self.logger.extend(turn_events)
            return turn_events

        if actor_b is None:
            action_a, scores_a = actor_a.choose_action(None)
            turn_events.extend(self.resolve_action(turn, actor_a, None, action_a, scores_a))
            turn_events.extend(self.finish_turn(turn))
            self.logger.extend(turn_events)
            return turn_events

        action_a, scores_a = actor_a.choose_action(actor_b)
        action_b, scores_b = actor_b.choose_action(actor_a)

        turn_events.extend(self.resolve_action(turn, actor_a, actor_b, action_a, scores_a))
        turn_events.extend(self.resolve_action(turn, actor_b, actor_a, action_b, scores_b))
        turn_events.extend(self.finish_turn(turn))
        self.logger.extend(turn_events)
        return turn_events

    def resolve_action(
        self,
        turn: int,
        actor: Civilization,
        target: Civilization | None,
        action: str,
        scores: dict,
    ) -> list[Event]:
        events: list[Event] = []
        events.append(
            Event(
                turn=turn,
                kind="action_selected",
                source=actor.name,
                target=target.name if target is not None else None,
                details={"action": action, "scores": scores},
            )
        )

        if not actor.alive:
            return events

        if action == ACTION_GATHER:
            actor.resources += 20
            actor.food += 15
            events.append(Event(turn, "gather", actor.name, details={"resources": 20, "food": 15}))
        elif action == ACTION_EXPAND:
            actor.resources -= 15
            actor.population += 5
            actor.territory += 1
            actor.stability += 2
            events.append(Event(turn, "expand", actor.name, details={"territory": 1, "population": 5}))
        elif action == ACTION_TRADE and target is not None and target.alive:
            resolve_trade(actor, target)
            events.append(Event(turn, "trade", actor.name, target.name, {"resources": 10}))
        elif action == ACTION_ATTACK and target is not None and target.alive:
            outcome = resolve_attack(actor, target)
            events.append(
                Event(
                    turn=turn,
                    kind="attack",
                    source=actor.name,
                    target=target.name,
                    details=outcome,
                )
            )

        apply_economic_growth(actor, events, turn)
        return events

    def finish_turn(self, turn: int) -> list[Event]:
        events: list[Event] = []
        for civilization in self.civilizations:
            if not civilization.alive:
                continue
            events.extend(apply_survival_step(civilization, turn))
            if is_collapsed(civilization):
                civilization.mark_dead()
                self.dead_archive.append(civilization.to_dict())
                event = Event(turn, "civilization_dead", civilization.name, details=civilization.to_dict())
                events.append(event)
        return events

    def is_over(self) -> bool:
        return sum(1 for civilization in self.civilizations if civilization.alive) <= 1

    def snapshot(self) -> dict:
        return {
            "turn": self.clock.turn,
            "civilizations": [civilization.to_dict() for civilization in self.civilizations],
            "history": self.logger.to_list(),
            "dead_archive": list(self.dead_archive),
        }
