from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    card_factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game_engine = GameEngine()
    game_engine.configure_engine(card_factory, strategy)
    print(f"Factory: {game_engine.factory.__class__.__name__}")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print(f"Available types: {card_factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    turn_result = game_engine.simulate_turn()
    print(f"Hand: [{turn_result['current_hand']}]\n")

    print("Turn execution:")
    turn_result = game_engine.simulate_turn()
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print(f"Actions: {turn_result}")

    print("\nGame Report:")
    print(game_engine.get_engine_status())
    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
