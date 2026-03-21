from ex0 import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state) -> dict:
        self.durability -= 1
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "effect": self.effect,
            "durability": self.durability,
        }

    def activate_ability(self) -> dict:
        return {
            "name": self.name,
        }
