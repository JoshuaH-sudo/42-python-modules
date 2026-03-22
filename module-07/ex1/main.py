from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from .Deck import Deck


def main():
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard("Goblin Warrior", 4, "Common", 3, 2))
    deck.add_card(
        ArtifactCard(
            "Ancient Relic", 4, "Rare", 5, "Grants +2 attack to all creatures"
        )
    )
    deck.add_card(SpellCard("Fireball", 4, "Uncommon", "damage"))
    print(f"Deck stats: {deck.get_deck_stats()}")


if __name__ == "__main__":
    main()
