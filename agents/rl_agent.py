from __future__ import annotations


class RLAgent:
    def __init__(self, name: str = "rl-agent") -> None:
        self.name = name

    def act(self, state):
        raise NotImplementedError("RL support is planned for Phase 2.")

