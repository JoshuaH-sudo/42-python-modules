from .CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing AbstractBase Class Design:\n")

    dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreateCard Info:")
    print(dragon_card.get_card_info())


if __name__ == "__main__":
    main()
