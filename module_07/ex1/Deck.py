import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from typing import List


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.insert(0, card)

    def remove_card(self, card_name: str) -> Card | None:
        index = 0
        for card in self.cards:
            if card.name == card_name:
                return self.cards.pop(index)
            index += 1
        return None

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card | None:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = 0
        total_cost = 0
        creature_cards = 0
        spell_cards = 0
        artifact_cards = 0

        for card in self.cards:
            total_cards += 1
            total_cost += card.cost
            if card.__class__ == CreatureCard:
                creature_cards += 1
            if card.__class__ == SpellCard:
                spell_cards += 1
            if card.__class__ == ArtifactCard:
                artifact_cards += 1

        if total_cards == 0:
            return {
                "total_cards": 0,
                "average_cost": 0,
                "rarity_distribution": {},
            }

        average_cost = total_cost / total_cards
        return {
            "total_cards": total_cards,
            "creature_cards": creature_cards,
            "spell_cards": spell_cards,
            "artifact_cards": artifact_cards,
            "avg_cost": f"{average_cost:.1f}",
        }
