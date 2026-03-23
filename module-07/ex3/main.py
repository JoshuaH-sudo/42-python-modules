from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game \n")
    print("Configuring Fantasy Card Game...\n")
    card_factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game_engine = GameEngine()
    game_engine.configure_engine(card_factory, strategy)
    print(f"Factory: {game_engine.factory.__class__.__name__}")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print(f"Available types: {card_factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    game_engine.simulate_turn()


if __name__ == "__main__":
    main()
