from .EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    for base in EliteCard.__mro__:
        if (
            base.__name__ == "object"
            or base.__name__ == "EliteCard"
            or base.__name__ == "ABC"
        ):
            continue

        print(f"- {base.__name__}", end=": ")
        methods = [
            name
            for name, value in base.__dict__.items()
            if value.__class__.__name__ == "function"
            and not name.startswith("__")
        ]
        print(methods)

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="legendary",
        attack_power=5,
        health=5,
        mana_pool=8,
    )
    print("Combat phase:")
    combat_result = arcane_warrior.attack(target="Enemy")
    print(f"Attack result: {combat_result}")
    defend_result = arcane_warrior.defend(incoming_damage=5)
    print(f"Defend result: {defend_result}")

    print("\nMagic phase:")
    spell_result = arcane_warrior.cast_spell(
        spell_name="Fireball", targets=["Enemy1", "Enemy2"]
    )
    print(f"Spell result: {spell_result}")
    mana_channel_result = arcane_warrior.channel_mana(amount=3)
    print(f"Mana channel: {mana_channel_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
