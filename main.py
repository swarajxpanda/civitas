from civilization import Civilization

civ1 = Civilization("Aether")
civ2 = Civilization("Norvik")

for turn in range(1, 21):
    print(f"\n~~~~~~ TURN {turn} ~~~~~~")

    # Decision Phase
    action1, scores1 = civ1.choose_action(civ2)
    action2, scores2 = civ2.choose_action(civ1)

    print(f"{civ1.name} chose: {action1}")
    print(scores1)

    print()

    print(f"{civ2.name} chose: {action2}")
    print(scores2)

    print()

    # Resolve Actions for Civilization 1
    if action1 == "GATHER":
        civ1.resources += 20
        print(f"{civ1.name} gathered resources.")

    elif action1 == "EXPAND":
        civ1.resources -= 15
        civ1.territory += 1
        civ1.population += 5

        print(f"{civ1.name} expanded territory.")

    elif action1 == "TRADE":
        civ1.resources += 10
        civ2.resources += 10

        print(f"{civ1.name} traded with {civ2.name}.")

    elif action1 == "ATTACK":
        print(f"{civ1.name} attacked {civ2.name}!")

        if civ1.military > civ2.military:
            civ1.resources += 30
            civ2.resources -= 30

            civ2.population -= 10
            civ2.military -= 5

            print(f"{civ1.name} won the battle.")

        else:
            civ1.resources -= 20
            civ1.population -= 10
            civ1.military -= 5

            print(f"{civ1.name} lost the battle.")

    # Resolve Actions for Civilization 2
    if action2 == "GATHER":
        civ2.resources += 20
        print(f"{civ2.name} gathered resources.")

    elif action2 == "EXPAND":
        civ2.resources -= 15
        civ2.territory += 1
        civ2.population += 5

        print(f"{civ2.name} expanded territory.")

    elif action2 == "TRADE":
        civ2.resources += 10
        civ1.resources += 10

        print(f"{civ2.name} traded with {civ1.name}.")

    elif action2 == "ATTACK":
        print(f"{civ2.name} attacked {civ1.name}!")

        if civ2.military > civ1.military:
            civ2.resources += 30
            civ1.resources -= 30

            civ1.population -= 10
            civ1.military -= 5

            print(f"{civ2.name} won the battle.")

        else:
            civ2.resources -= 20
            civ2.population -= 10
            civ2.military -= 5

            print(f"{civ2.name} lost the battle.")

    # Resource Consumption: population consumes resources
    civ1.resources -= civ1.population * 0.1
    civ2.resources -= civ2.population * 0.1

    # Military Upkeep: military consumes resources
    civ1.resources -= civ1.military * 0.05
    civ2.resources -= civ2.military * 0.05

    # Population Effects: if healthy, population grows; if unhealthy, population shrinks
    if civ1.resources > 100:
        civ1.population += 2

    else:
        civ1.population -= 2

    if civ2.resources > 100:
        civ2.population += 2

    else:
        civ2.population -= 2

    # Civilization Collapse Check
    if civ1.population <= 0:
        print(f"\n{civ1.name} has collapsed.")
        break

    if civ2.population <= 0:
        print(f"\n{civ2.name} has collapsed.")
        break

    # Prevent Negative Values
    civ1.resources = max(civ1.resources, 0)
    civ2.resources = max(civ2.resources, 0)

    civ1.military = max(civ1.military, 0)
    civ2.military = max(civ2.military, 0)

    # World State
    print("\n~~~~~~ WORLD STATE ~~~~~~")

    print()
    print(vars(civ1))

    print()
    print(vars(civ2))
