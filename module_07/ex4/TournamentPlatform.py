from typing import Dict, List

from .TournamentCard import TournamentCard
import statistics


class TournamentPlatform:
    def __init__(self) -> None:
        self.registered_cards: List[TournamentCard] = []
        self.card_ids: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = (
            card.name.lower().replace(" ", "_")
            + f"_{self.registered_cards.__len__() + 1:03d}"
        )
        self.registered_cards.append(card)
        self.card_ids[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.card_ids or card2_id not in self.card_ids:
            raise ValueError(
                "Both card IDs must be registered on the platform."
            )

        card1 = self.card_ids[card1_id]
        card2 = self.card_ids[card2_id]

        if card1.damage >= card2.damage:
            winner_card, loser_card = card1, card2
            winner_id, loser_id = card1_id, card2_id
        elif card2.damage > card1.damage:
            winner_card, loser_card = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner_card.update_wins(1)
        loser_card.update_losses(1)
        self.matches_played += 1
        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner_card.calculate_rating(),
            "loser_rating": loser_card.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            [(cid, card) for cid, card in self.card_ids.items()],
            key=lambda x: x[1].calculate_rating(),
            reverse=True,
        )
        return [
            {
                "id": card_id,
                "name": card.name,
                "rating": card.calculate_rating(),
                "wins": card.wins,
                "losses": card.losses,
            }
            for card_id, card in sorted_cards
        ]

    def generate_tournament_report(self) -> dict:
        avg_rating = (
            statistics.mean(
                [card.calculate_rating() for card in self.registered_cards]
            )
            if self.registered_cards
            else 0
        )
        return {
            "total_cards": self.registered_cards.__len__(),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": (
                "active" if self.registered_cards else "inactive"
            ),
        }
