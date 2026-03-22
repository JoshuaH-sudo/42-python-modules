import random
from collections import Counter
from statistics import mean
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from typing import List


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card):
        if not card.__class__.__bases__[0] == Card:
            raise TypeError("card must be an instance of Card")
        self.cards.insert(0, card)

    def remove_card(self, card_name: str):
        for index, card in enumerate(self.cards):
            if card.name == card_name:
                return self.cards.pop(index)
        return None

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self):
        total_cards = Counter(self.cards).total()
        if total_cards == 0:
            return {
                "total_cards": 0,
                "average_cost": 0,
                "rarity_distribution": {},
            }

        average_cost = mean(card.cost for card in self.cards)
        creature_cards = Counter(
            [card for card in self.cards if card.__class__ == CreatureCard]
        ).total()
        spell_cards = Counter(
            [card for card in self.cards if card.__class__ == SpellCard]
        ).total()
        artifact_cards = Counter(
            [card for card in self.cards if card.__class__ == ArtifactCard]
        ).total()

        return {
            "total_cards": total_cards,
            "creature_cards": creature_cards,
            "spell_cards": spell_cards,
            "artifact_cards": artifact_cards,
            "avg_cost": f"{average_cost:.1f}",
        }
