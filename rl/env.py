from __future__ import annotations


class CivitasEnv:
    def __init__(self, world) -> None:
        self.world = world

    def reset(self):
        raise NotImplementedError("Gym wrapper is planned for Phase 2.")

    def step(self, action):
        raise NotImplementedError("Gym wrapper is planned for Phase 2.")

