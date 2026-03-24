from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    platform = TournamentPlatform()

    dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="legendary",
        attack=8,
        health=8,
    )

    wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="rare",
        attack=7,
        health=6,
    )

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon.wins}-{dragon.losses}\n")

    print(f"{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {wizard.wins}-{wizard.losses}\n")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for idx, card_info in enumerate(leaderboard, 1):
        print(
            f"{idx}. {card_info['name']} - Rating: {card_info['rating']}, "
            f"({card_info['wins']}-{card_info['losses']})"
        )

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")


if __name__ == "__main__":
    main()
