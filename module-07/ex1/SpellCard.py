from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    type = "spell"

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        for effect in EffectType:
            if effect.value == effect_type:
                break
        else:
            raise ValueError(f"Invalid effect_type: {effect_type}")
        self.effect_type = effect_type

    def play(self, game_state) -> dict:
        if not self.is_playable(game_state["available_mana"]):
            return {"error": "Not enough mana to play this card."}

        if self.effect_type == EffectType.DAMAGE.value:
            effect = "Deal 3 damage to target"
        elif self.effect_type == EffectType.HEAL.value:
            effect = "Heal 3 health to target"
        elif self.effect_type == EffectType.BUFF.value:
            effect = "Buff target creature with +2/+2 until end of turn"
        elif self.effect_type == EffectType.DEBUFF.value:
            effect = "Debuff target creature with -2/-2 until end of turn"

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect,
        }

    def resolve_effect(self) -> dict:
        return {
            "name": self.name,
        }
