from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from .Deck import Deck


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    game_state = {"available_mana": 20}

    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Common", 3, 2))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal", 2, "Rare", 2, "Permanent +1 mana per turn"
        )
    )
    deck.add_card(SpellCard("Lightning Bolt", 3, "Uncommon", "damage"))
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")

    card = deck.draw_card()
    print(f"Draw: {card.name} ({card.type.capitalize()})")
    print(f"Play: {card.play(game_state)}\n")

    card = deck.draw_card()
    print(f"Draw: {card.name} ({card.type.capitalize()})")
    print(f"Play: {card.play(game_state)}\n")

    card = deck.draw_card()
    print(f"Draw: {card.name} ({card.type.capitalize()})")
    print(f"Play: {card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
