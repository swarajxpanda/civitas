# CIVITAS
Adaptive Civilization Intelligence Simulator

CIVITAS is a pure Python simulation project for exploring how civilizations behave under pressure, adapt over time, and collapse when survival conditions fail.

The current engine models a small world of autonomous civilizations that choose actions, consume resources, manage military upkeep, and respond to scarcity. The longer-term goal is to grow this into a full agent-driven ecosystem with memory, history, evolution, and reinforcement learning.

## What the simulation does

Each turn, every civilization:
- evaluates its current state
- scores possible actions
- chooses an action
- pays the consequences
- updates its survival outlook

The current action set includes:
- `ATTACK`
- `TRADE`
- `EXPAND`
- `GATHER`

The survival layer adds:
- food consumption
- resource consumption
- military upkeep
- prosperity-based growth
- scarcity penalties
- permanent collapse

## Current focus

The project is still early, but the foundation is real now:
- Phase 0: core world engine, events, history, and storage scaffolding
- Phase 1: survival systems, starvation, upkeep, prosperity, and death handling

That means the simulation now produces a readable turn-by-turn event stream and a live world state that can be extended into future agents and training loops.

## Project structure

```text
.
├── main.py
├── core/
│   ├── world.py
│   ├── civilization.py
│   ├── event.py
│   ├── clock.py
│   ├── logger.py
│   └── storage.py
├── systems/
│   ├── economy.py
│   ├── warfare.py
│   └── survival.py
├── agents/
│   ├── rule_based.py
│   ├── rl_agent.py
│   └── evolution.py
├── rl/
│   ├── env.py
│   ├── features.py
│   ├── rewards.py
│   └── trainer.py
├── memory/
│   ├── short_term.py
│   ├── long_term.py
│   └── archive.py
├── data/
└── logs/
```

## Tech stack

- Python 3
- Standard library only
- No external ML dependencies yet
- Designed to support later RL and agent integration

## How to run

```bash
python main.py
```

That will run a short two-civilization simulation and print each turn's events followed by the resulting world state.

## Roadmap

- Phase 0: world controller, civilization model, event logging, persistence scaffolding
- Phase 1: survival systems and collapse behavior
- Phase 2: feature engineering and RL environment
- Phase 3: adaptive rule-based agents
- Phase 4: memory and relationships
- Phase 5: economic specialization
- Phase 6: world generation
- Phase 7: evolutionary systems
- Phase 8: advanced RL and self-play
- Phase 9: emergent civilization ecosystem

## Status

Early architectural foundation complete. The simulation now runs through a structured engine instead of a single procedural script.
