from .CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    goblin_card = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
    dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreateCard Info:")
    print(dragon_card.get_card_info())

    print(f"Playing {dragon_card.name} with 6 mana available:")
    print(f"Playable: {dragon_card.is_playable(6)}")
    print(f"Play result: {dragon_card.play({})}")
    print("")

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon_card.attack_target(goblin_card)}")
    print("")

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon_card.is_playable(3)}")
    print("")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
