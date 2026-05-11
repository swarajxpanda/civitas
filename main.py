from core.civilization import Civilization
from core.world import World


def main() -> None:
    world = World([Civilization("Aether"), Civilization("Norvik")])

    for _ in range(20):
        events = world.step()
        current_turn = world.clock.turn

        print(f"\n~~~~~~ TURN {current_turn} ~~~~~~")
        for event in events:
            print(event.to_dict())

        print("\n~~~~~~ WORLD STATE ~~~~~~")
        for civilization in world.civilizations:
            print(civilization.to_dict())

        if world.is_over():
            break


if __name__ == "__main__":
    main()
