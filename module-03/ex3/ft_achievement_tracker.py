import random

ACHIEVEMENTS = [
    "Boss Slayer",
    "Collector Supreme",
    "Crafting Genius",
    "First Steps",
    "Hidden Path Finder",
    "Master Explorer",
    "Sharp Mind",
    "Speed Runner",
    "Strategist",
    "Survivor",
    "Treasure Hunter",
    "Untouchable",
    "Unstoppable",
    "World Savior",
]


def gen_player_achievements() -> set:
    count = random.randint(4, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print("")

    all_achievements = set(ACHIEVEMENTS)
    player_sets = list(players.values())

    distinct = player_sets[0].union(*player_sets[1:])
    print(f"All distinct achievements: {distinct}\n")

    common = player_sets[0]
    for achievements in player_sets[1:]:
        common = common.intersection(achievements)
    print(f"Common achievements: {common}\n")

    for name, achievements in players.items():
        others = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others = others.union(other_achievements)
        unique = achievements.difference(others)
        print(f"Only {name} has: {unique}")
    print("")

    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
