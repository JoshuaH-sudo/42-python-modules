from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        for effect in EffectType:
            if effect.value == effect_type:
                break
        else:
            raise ValueError(f"Invalid effect_type: {effect_type}")
        self.effect_type = effect_type

    def play(self, game_state) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "effect_type": self.effect_type,
        }

    def resolve_effect(self) -> dict:
        return {
            "name": self.name,
        }
