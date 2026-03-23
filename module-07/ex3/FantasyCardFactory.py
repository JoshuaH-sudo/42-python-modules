from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
from random import choice


class FantasyCardFactory(CardFactory):
    supported_types = {
        "creature": ["dragon", "goblin"],
        "spell": ["fireball"],
        "artifact": ["mana_ring"],
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = choice(self.supported_types["creature"])
        if name_or_power.__class__ == int:
            creature_name = choice(self.supported_types["creature"])
            return CreatureCard(
                name=creature_name,
                cost=2 if name_or_power < 5 else 5,
                rarity="common" if name_or_power < 5 else "rare",
                attack=name_or_power,
                health=name_or_power + 1,
            )
        if name_or_power.__class__ == str:
            if name_or_power == "dragon":
                return CreatureCard(
                    name="Dragon",
                    cost=5,
                    rarity="legendary",
                    attack=8,
                    health=8,
                )
            elif name_or_power == "goblin":
                return CreatureCard(
                    name="Goblin", cost=2, rarity="common", attack=2, health=1
                )
            else:
                raise ValueError(f"Unsupported creature type: {name_or_power}")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = choice(self.supported_types["spell"])
        if name_or_power.__class__ == int:
            spell_name = choice(self.supported_types["spell"])
            return SpellCard(
                name=spell_name,
                cost=2 if name_or_power < 5 else 5,
                rarity="common" if name_or_power < 5 else "rare",
                effect_type="damage",
            )
        if name_or_power.__class__ == str:
            if name_or_power == "fireball":
                return SpellCard(
                    name="Fireball",
                    cost=4,
                    rarity="rare",
                    effect_type="damage",
                )
            else:
                raise ValueError(f"Unsupported spell type: {name_or_power}")
        raise TypeError("name_or_power must be str, int, or None")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = choice(self.supported_types["artifact"])
        if name_or_power.__class__ == int:
            artifact_name = choice(self.supported_types["artifact"])
            return ArtifactCard(
                name=artifact_name,
                cost=2 if name_or_power < 5 else 5,
                rarity="common" if name_or_power < 5 else "rare",
                durability=2 if name_or_power < 5 else 4,
                effect="Gain 1 mana" if name_or_power < 5 else "Gain 2 mana",
            )
        if name_or_power.__class__ == str:
            if name_or_power == "mana_ring":
                return ArtifactCard(
                    name="Mana Ring",
                    cost=2,
                    rarity="rare",
                    durability=3,
                    effect="Permanent +1 mana per turn",
                )
            else:
                raise ValueError(f"Unsupported artifact type: {name_or_power}")
        raise TypeError("name_or_power must be str, int, or None")

    def create_themed_deck(self, size: int) -> dict:
        deck = {"creature": [], "spell": [], "artifact": []}
        for _ in range(size):
            card_type = choice(list(self.supported_types.keys()))
            if card_type == "creature":
                deck["creature"].append(self.create_creature())
            elif card_type == "spell":
                deck["spell"].append(self.create_spell())
            elif card_type == "artifact":
                deck["artifact"].append(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        return self.supported_types
