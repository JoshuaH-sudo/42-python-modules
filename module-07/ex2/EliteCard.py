from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    type = "elite"

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana_pool: int,
    ):
        super().__init__(name, cost, rarity)
        if attack_power < 0 or health < 0 or mana_pool < 0:
            raise ValueError(
                "attack_power, health, and mana_pool must be non-negative."
            )
        self.attack_power = attack_power
        self.health = health
        self.mana_pool = mana_pool

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {"error": "Not enough mana to play this card."}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters the battlefield",
        }

    def attack(self, target) -> dict:
        target_name = getattr(target, "name", "unknown target")
        damage_result = None
        if hasattr(target, "defend"):
            damage_result = target.defend(self.attack_power)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack_power,
            "target_result": damage_result,
        }

    def defend(self, incoming_damage: int) -> dict:
        if incoming_damage < 0:
            raise ValueError("incoming_damage must be non-negative.")
        self.health -= incoming_damage
        if self.health < 0:
            self.health = 0
        return {
            "card": self.name,
            "damage_taken": incoming_damage,
            "remaining_health": self.health,
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell_cost = len(targets)
        if self.mana_pool < spell_cost:
            return {"error": "Not enough mana to cast spell."}
        self.mana_pool -= spell_cost
        target_names = [
            getattr(target, "name", str(target)) for target in targets
        ]
        return {
            "caster": self.name,
            "spell_name": spell_name,
            "targets": target_names,
            "mana_spent": spell_cost,
            "remaining_mana": self.mana_pool,
        }

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            raise ValueError("amount must be non-negative.")
        self.mana_pool += amount
        return {
            "card": self.name,
            "mana_gained": amount,
            "current_mana": self.mana_pool,
        }

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "mana_pool": self.mana_pool,
        }
