from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registered_cards = []
        self.card_ids = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = (
            card.name.lower().replace(" ", "_")
            + f"_{len(self.registered_cards) + 1:03d}"
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

        card1_wins = 0
        card2_wins = 0

        for _ in range(100):
            if card1.attack > card2.health:
                card1_wins += 1
            elif card2.attack > card1.health:
                card2_wins += 1

        card1.update_wins(card1_wins)
        card1.update_losses(card2_wins)
        card2.update_wins(card2_wins)
        card2.update_losses(card1_wins)
        self.matches_played += 1

        winner_id = card1_id if card1_wins > card2_wins else card2_id
        loser_id = card2_id if card1_wins > card2_wins else card1_id
        winner_card = card1 if card1_wins > card2_wins else card2
        loser_card = card2 if card1_wins > card2_wins else card1

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
        total_rating = sum(
            card.calculate_rating() for card in self.registered_cards
        )
        avg_rating = (
            total_rating // len(self.registered_cards)
            if self.registered_cards
            else 0
        )
        return {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": (
                "active" if self.registered_cards else "inactive"
            ),
        }
