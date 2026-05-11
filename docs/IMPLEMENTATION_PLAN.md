## Phases

### Phase 0 — Foundational Architecture

Transform the current procedural script into a scalable simulation engine.

**World Controller** (`world.py`) — owns all civilizations, advances turns, resolves actions, stores history, manages the simulation clock.

**Civilization Class** (`civilization.py`) — each civilization holds its own state, personality traits, memory, relationships, and learning variables.

**Event System** (`event.py`) — all meaningful interactions become structured events. Events form the world history, training data, replay system, and analytics layer.

**History Logger** (`logger.py`) — appends events, saves timelines, generates historical archives.

**Save/Load System** (`storage.py`) — starts with JSON, later moves to SQLite and compressed saves.

---

### Phase 1 — Survival Systems

Introduce scarcity and collapse. Civilizations must struggle to survive.

- Population consumes food and resources
- Military consumes upkeep and equipment
- Prosperity drives population growth and economic expansion
- Scarcity causes starvation, instability, and collapse
- Civilizations can permanently die — dead civilizations remain in the history archive

---

### Phase 2 — Feature Engineering and RL Loop (Early Training)

This is the earliest point at which training is viable. The world exists, rewards exist, and state is meaningful — so training starts here.

Each turn is structured as a standard RL transition:

```
state -> action -> outcome -> reward
```

World state is encoded as a flat feature vector per civilization:

```
[resources, military, population, territory, food_level,
 economic_stability, enemy_strength, trust_scores, aggression_index]
```

Training uses `stable-baselines3` with a simple MLP policy. The simulation runs as a Gym-compatible environment. No handwriting networks, no reinventing infrastructure — get signal fast and iterate.

The agent learns from this environment directly. Everything added in later phases enriches the state space and improves the policy automatically.

---

### Phase 3 — Adaptive Agents (Rule-Based Baseline)

While RL trains in the background, rule-based agents serve as a baseline and opponent pool.

Each action type is tracked. Successful actions increase preference; failed actions decrease it. Over time, rule-based agents drift toward militarism, trade, expansion, or isolationism — without explicit scripting. These agents generate experience data and act as opponents during early RL training.

---

### Phase 4 — Memory and Relationships

Civilizations remember history across three layers.

- **Short-term memory** — recent interactions and events
- **Long-term memory** — per-civilization relationship tracking (trust, wars, trades)
- **Historical archive** — a permanent, immutable global timeline

Memory values are added directly to the feature vector, enriching what the RL policy can observe and reason over.

---

### Phase 5 — Economic Specialization

Replace generic resources with real economies: food, gold, industry, energy, technology.

Civilizations develop shortages, dependencies, and trade identities. Emergent outcomes include trade empires, industrial powers, starving militarists, and technological civilizations. Each new resource dimension extends the feature vector and expands the action space the policy must learn.

---

### Phase 6 — World Generation

Introduce geography through procedural map generation — continents, terrain, climates, resource zones. Civilizations occupy tiles. Terrain shapes economy, warfare, expansion, and trade routes.

Geographic features are encoded and appended to the state vector, giving the policy spatial context for decision-making.

---

### Phase 7 — Evolutionary Systems

Strategies evolve genetically over time.

- Traits drift through random mutation
- New civilizations inherit strategies, personalities, and tendencies from predecessors
- Successful strategies survive longer; weak ones disappear naturally

Evolutionary pressure acts as a second optimization loop running alongside RL — policies that win produce more offspring.

---

### Phase 8 — Advanced RL and Self-Play

With a rich state space now in place, move to more powerful training regimes.

- Self-play: RL agents compete against past versions of themselves
- Population-based training: multiple policies evolve in parallel
- Curriculum learning: agents face progressively harder opponents and scenarios

Policy architecture can be upgraded here — from MLP to recurrent (LSTM) if memory-dependent behavior improves performance.

---

### Phase 9 — Emergent Civilization Ecosystem

Scale into a living world with many civilizations, alliances, coalitions, migrations, collapses, and historical eras. History becomes emergent narrative — timelines, empires, dynasties, wars, economic collapses — generated entirely from agent behavior.

---

## Directory Structure

```
civitas/
│
├── main.py                   # Entry point
│
├── core/                     # Simulation engine
│   ├── world.py
│   ├── civilization.py
│   ├── event.py
│   ├── clock.py
│   └── storage.py
│
├── systems/                  # Game systems
│   ├── economy.py
│   ├── warfare.py
│   ├── survival.py
│   ├── relationships.py
│   └── geography.py
│
├── agents/                   # Decision-making
│   ├── rule_based.py
│   ├── rl_agent.py
│   └── evolution.py
│
├── rl/                       # Reinforcement learning
│   ├── env.py                # Gym environment wrapper
│   ├── features.py           # Feature engineering
│   ├── rewards.py            # Reward functions
│   └── trainer.py
│
├── memory/                   # Memory systems
│   ├── short_term.py
│   ├── long_term.py
│   └── archive.py
│
├── data/                     # Persistence
│   ├── world.json
│   ├── history.json
│   └── civilizations.json
│
├── logs/
│   └── simulation.log
│
└── visualizer/
    ├── map_renderer.py
    └── timeline_viewer.py
```
