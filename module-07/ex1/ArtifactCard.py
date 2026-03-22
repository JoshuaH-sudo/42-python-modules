from ex0.Card import Card


class ArtifactCard(Card):
    type = "artifact"

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state) -> dict:
        if not self.is_playable(game_state["available_mana"]):
            return {"error": "Not enough mana to play this card."}
        self.durability -= 1
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def activate_ability(self) -> dict:
        return {
            "name": self.name,
        }
