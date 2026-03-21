from .Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ):
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be non-negative.")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        print(
            f"Playing creature card: {self.name} with {self.attack} attack",
            f"and {self.health} health.",
        )
        return game_state

    def attack_target(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack} damage.")
        target.health -= self.attack
        if target.health <= 0:
            print(f"{target.name} has been defeated.")
