# CIVITAS Implementation Plan

This document tracks the build-out of the simulation from the current engine foundation toward agent-driven civilization behavior.

## Completed Phases

- [x] Phase 0 - Foundational Architecture
- [x] Phase 1 - Survival Systems

These are the milestones already implemented in the codebase.

## Phase 0 - Foundational Architecture

Status: complete

Goal: turn the original procedural script into a maintainable simulation engine.

Completed work:
- world controller that owns civilizations and advances turns
- civilization model with state and decision weights
- structured event objects for all meaningful outcomes
- history logging for turn-by-turn simulation output
- JSON storage scaffolding for future persistence
- project layout split into `core/`, `systems/`, `agents/`, `memory/`, `rl/`, `data/`, and `logs/`

## Phase 1 - Survival Systems

Status: complete

Goal: introduce scarcity, pressure, and collapse so civilizations can actually fail.

Completed work:
- population consumes food and resources over time
- military consumes upkeep
- prosperity can support population growth
- scarcity creates starvation and instability
- civilizations can collapse permanently
- dead civilizations remain in the history archive

## Phase 2 - Feature Engineering and RL Loop

Status: planned

Goal: turn the simulation into a Gym-compatible environment where each turn becomes a standard RL transition:

```text
state -> action -> outcome -> reward
```

Planned work:
- encode each civilization as a flat feature vector
- define reward signals for survival, growth, and strategic success
- wrap the world as an environment for training
- integrate `stable-baselines3` or an equivalent RL pipeline

## Phase 3 - Adaptive Agents

Status: planned

Goal: keep rule-based agents competitive while RL matures.

Planned work:
- track action outcomes per civilization
- tune preferences based on success and failure
- let agents drift toward militarism, trade, expansion, or isolationism

## Phase 4 - Memory and Relationships

Status: planned

Goal: give civilizations memory across multiple timescales.

Planned work:
- short-term memory for recent events
- long-term relationship tracking
- permanent historical archive
- memory features exposed to the policy/state vector

## Phase 5 - Economic Specialization

Status: planned

Goal: replace generic resources with a richer economy.

Planned work:
- food, gold, industry, energy, technology
- shortages and dependencies
- trade identities and specialization

## Phase 6 - World Generation

Status: planned

Goal: add geography and terrain.

Planned work:
- procedural maps
- continents, climates, terrain, and resource zones
- spatial constraints on economy and warfare

## Phase 7 - Evolutionary Systems

Status: planned

Goal: let strategies survive, mutate, and inherit over time.

Planned work:
- mutation of behavioral traits
- inheritance from successful civilizations
- survival-based selection pressure

## Phase 8 - Advanced RL and Self-Play

Status: planned

Goal: improve training once the state space is rich enough.

Planned work:
- self-play against past policies
- population-based training
- curriculum learning
- possible recurrent policies for memory-heavy behavior

## Phase 9 - Emergent Civilization Ecosystem

Status: planned

Goal: scale into a living world of alliances, migrations, collapses, and historical eras.

Planned work:
- many civilizations
- coalitions and rival blocs
- large-scale historical timelines
- emergent narrative over long simulation runs

## Notes

- The repository is intentionally kept pure Python for now.
- Persistence, agents, and RL scaffolding exist so later phases can grow without another rewrite.
- The implementation plan should stay aligned with the current engine rather than the original one-file prototype.
