from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self, name="AggressiveStrategy"):
        super().__init__(name)

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 10
        mana_used = 0
        cards_played = []
        for card in sorted(hand, key=lambda c: c.cost):
            if card.cost <= 3 and mana_used + card.cost <= available_mana:
                cards_played.append(card)
                mana_used += card.cost
        targets = self.prioritize_targets(battlefield)
        damage_dealt = mana_used + 3
        return {
            "cards_played": [c.name for c in cards_played],
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return self.name

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
