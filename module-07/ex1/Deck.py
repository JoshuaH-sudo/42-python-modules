import random
from collections import Counter
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card):
        if not isinstance(card, Card):
            raise TypeError("card must be an instance of Card")
        self.cards.append(card)

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
        total_cards = len(self.cards)
        if total_cards == 0:
            return {
                "total_cards": 0,
                "average_cost": 0,
                "rarity_distribution": {},
            }

        average_cost = sum(card.cost for card in self.cards) / total_cards
        rarity_distribution = dict(Counter(card.rarity for card in self.cards))

        return {
            "total_cards": total_cards,
            "average_cost": average_cost,
            "rarity_distribution": rarity_distribution,
        }
