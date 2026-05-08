# CIVITAS
### Adaptive Civilization Intelligence Simulator

> Build a fully self-contained civilization ecosystem from scratch — no frameworks, no shortcuts.
> Intelligence emerges through feedback loops, memory, and evolution.

---

## The Arc

```
Static Simulation
    ↓
Survival Pressure
    ↓
Adaptive Learning
    ↓
Probabilistic Decisions
    ↓
Persistent Memory
    ↓
Relationship Systems
    ↓
Advanced Economics
    ↓
Territory & Geography
    ↓
Evolutionary Intelligence
    ↓
Handwritten Neural Networks
    ↓
Living Civilization Ecosystem
```

---

## Phases

---

### Phase 0 — Core Simulation

A minimal working simulation. Two civilizations interact across turns — gathering resources, attacking, trading, expanding. Everything is deterministic. This is your foundation.

**Build:**
- `Civilization` class with resources, military, population, territory, personality weights
- 4 actions: `ATTACK`, `TRADE`, `EXPAND`, `GATHER`
- Turn loop: observe → choose → resolve → update → print

**AI type:** Static utility scoring — calculate action scores, pick the highest.

**Files:** `civilization.py`, `main.py`

✅ **Done when:** Two civilizations survive and interact for multiple turns without crashing.

---

### Phase 1 — Resource Pressure & Survival

Remove infinite growth. Add upkeep, starvation, and collapse. Civilizations can now die — and the simulation starts to feel alive.

**Build:**
- Population consumes resources every turn
- Armies require maintenance costs
- Population grows under prosperity, shrinks under scarcity
- Civilizations can collapse and die permanently

**Emergent behaviors to watch for:** Overexpansion collapse, militaristic bankruptcy, sustainable growth patterns.

✅ **Done when:** Civilizations naturally rise and fall through system interaction alone.

---

### Phase 2 — Adaptive Learning

Civilizations start remembering what worked. Successful wars raise aggression; failed ones lower it. Strategies shift over time without you writing new rules.

**Build:**
- Track outcomes per action
- Reward signals: successful action → increase that preference weight
- Penalty signals: failed action → decrease that preference weight
- Personality traits (`aggression`, `trade_preference`, `expansionism`) evolve over time

**AI type:** Adaptive weighted utility — civilizations now remember and change.

✅ **Done when:** Civilizations visibly change their strategy across a long run.

---

### Phase 3 — Probabilistic Decisions

Replace "always pick the highest score" with probability-weighted choices. Add occasional exploration of suboptimal options. Behavior becomes unpredictable in interesting ways.

**Build:**
- Convert utility scores into normalized probabilities
- Weighted random action selection
- Exploration logic: occasionally try a suboptimal action to discover new strategies

**Example:** `ATTACK → 50%`, `TRADE → 30%`, `EXPAND → 20%`

**AI type:** Probabilistic adaptive — less predictable, more alive.

✅ **Done when:** Civilizations become less predictable and start finding unexpected strategies.

---

### Phase 4 — Persistent World State

Save everything to disk. Closing the terminal no longer erases what civilizations have learned. The world continues from where it left off.

**Build:**
- `save_world()` → serializes all civilization state to `world.json`
- `load_world()` → resumes simulation from saved state
- Persist: stats, personality weights, history, simulation year

✅ **Done when:** Intelligence survives program restarts.

---

### Phase 5 — Memory & Relationships

Civilizations remember past wars, alliances, and betrayals. Trust scores shape diplomacy. Decisions are no longer just about the present — they're shaped by history.

**Build:**
- Relationship matrix: each civilization stores trust values toward every other
- Positive trade history increases trust; repeated attacks decrease it
- Historical event log: record wars, alliances, betrayals
- Decisions become contextual, not purely statistical

✅ **Done when:** Civilizations treat historical allies and enemies differently.

---

### Phase 6 — Advanced Economics

Replace the single "resources" number with food, gold, industry, energy, and technology. Civilizations develop economic identities and trade specific goods.

**Build:**
- Split generic resources into: `food`, `gold`, `industry`, `energy`, `technology`
- Civilizations exchange specific goods in trades
- Add shortages, production imbalances, and economic dependencies

✅ **Done when:** Each civilization develops a distinct economic character.

---

### Phase 7 — Territory & World Generation

Add a real map. Generate continents, terrain types, and distributed resources. Civilizations physically occupy tiles — and geography starts shaping behavior.

**Build:**
- Procedural world generator: continents, terrain, climate zones, resource distribution
- Civilizations occupy and expand across map tiles
- Terrain modifiers affect economy, military, and expansion

✅ **Done when:** Geography meaningfully influences how civilizations grow and fight.

---

### Phase 8 — Evolutionary Intelligence

Behavioral traits mutate and inherit across generations. Successful strategies survive. Distinct archetypes — aggressive warlords, peaceful traders — emerge without being programmed.

**Build:**
- Trait mutation: personality weights drift slightly over time
- Inheritance: successor civilizations carry traits from predecessors
- Selection pressure: successful strategies persist longer

**AI type:** Evolutionary adaptive intelligence.

✅ **Done when:** Distinct civilization archetypes emerge entirely on their own.

---

### Phase 9 — Handwritten Neural Networks

Replace hardcoded formulas with trainable networks built by hand. Forward propagation, gradient descent, weight updates — written in pure Python, no libraries.

**Build:**
- Input layer: resources, military, enemy strength, population, territory, trust values
- Hidden layer(s) + output layer: action probabilities
- Training loop: weights update through reward feedback
- Constraints: pure Python only, no NumPy, no ML frameworks

✅ **Done when:** Civilizations learn strategy without a single hardcoded rule.

---

### Phase 10 — Living Civilization Ecosystem

Scale up. Many civilizations, dynamic alliances, thousands of simulated years. Empires rise and collapse. Migrations happen. History writes itself.

**Build:**
- Large numbers of civilizations running simultaneously
- Dynamic coalitions and geopolitical systems
- Long-term historical archive: empires, collapses, migrations, ideological shifts
- Continuous autonomous adaptation without manual tuning

✅ **Done when:** The simulation generates believable historical narratives through pure system interaction.

---

## The Goal

CIVITAS isn't a game engine. It's a laboratory for understanding:

- How intelligence emerges from simple rules
- How adaptation and optimization work at a fundamental level
- How evolutionary pressure shapes behavior
- How neural networks learn — implemented by hand, from scratch

Everything is built in **pure Python**. No external ML frameworks. No shortcuts.

The complexity earns itself, one phase at a time.
