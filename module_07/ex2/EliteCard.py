from typing import Dict, List
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
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack_power if attack_power >= 0 else 1
        self.health = health if health >= 0 else 1
        self.mana_pool = mana_pool if mana_pool >= 0 else 0
        self.defense = 3

    def play(self, game_state: Dict) -> Dict:
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {"error": "Not enough mana to play this card."}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters the battlefield",
        }

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> Dict:
        if incoming_damage < 0:
            raise ValueError("incoming_damage must be non-negative.")

        blocked_damaged = incoming_damage - self.defense
        if blocked_damaged < 0:
            blocked_damaged = 0
        self.health -= blocked_damaged
        if self.health < 0:
            self.health = 0
        return {
            "defender": self.name,
            "damage_taken": blocked_damaged,
            "damage_blocked": incoming_damage - blocked_damaged,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> Dict:
        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        spell_cost = targets.__len__() * 2

        if self.mana_pool < spell_cost:
            return {"error": "Not enough mana to cast spell."}
        self.mana_pool -= spell_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": spell_cost,
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana_pool += amount
        return {
            "card": self.name,
            "channeled": amount,
            "current_mana": self.mana_pool,
        }

    def get_magic_stats(self) -> Dict:
        return {
            "name": self.name,
            "mana_pool": self.mana_pool,
        }
