class Achievement:
    def __init__(self, name: str, is_rare: bool = False) -> None:
        self.name = name
        self.is_rare = is_rare


allowed_achievements = {
    Achievement("boss_slayer"),
    Achievement("first_kill"),
    Achievement("level_10"),
    Achievement("speed_demon"),
    Achievement("treasure_hunter"),
    Achievement("collector", True),
    Achievement("perfectionist", True),
}


class Player:
    def __init__(self, name: str, achievements: list[str]) -> None:
        self.name = name
        for achievement in achievements:
            if achievement not in [a.name for a in allowed_achievements]:
                raise ValueError(f"Invalid achievement: {achievement}")
        self.achievements = set(achievements)

    def display_info(self) -> None:
        print(f"Player: {self.name} achievements: {self.achievements}")


class AchievementAnalyzer:
    players: list[Player]

    def __init__(self, players: list[Player]) -> None:
        self.players = players

    @staticmethod
    def common_achievements(player1: Player, player2: Player) -> set[str]:
        return player1.achievements.intersection(player2.achievements)

    def common_achievements_all(self) -> set[str]:
        common = self.players[0].achievements
        for player in self.players[1:]:
            common = common.intersection(player.achievements)
        return common

    def players_with_rare_achievements(self) -> list[str]:
        rare_achievements = {a.name for a in allowed_achievements if a.is_rare}
        players_with_rare = []
        for player in self.players:
            if player.achievements.intersection(rare_achievements):
                players_with_rare.append(player.name)
        return players_with_rare


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker ===\n")

    alice = Player(
        "Alice", {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    )
    bob = Player("Bob", {"first_kill", "level_10", "boss_slayer", "collector"})
    charlie = Player(
        "Charlie",
        {
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        },
    )
    players = [alice, bob, charlie]
    for player in players:
        player.display_info()

    print("\n=== Achievement Analytics ===")
    analyzer = AchievementAnalyzer(players)

    common = analyzer.common_achievements_all()
    achievement_names = {a.name for a in allowed_achievements}
    rare_achievements = {a.name for a in allowed_achievements if a.is_rare}
    players_with_rare = analyzer.players_with_rare_achievements()

    print(f"All unique achievements: {achievement_names}")
    print(f"Total unique achievements: {len(allowed_achievements)}")
    print()

    print(f"Common to all players: {common}")
    print(
        f"Rare achievements: ({len(players_with_rare)} player)",
        f"{rare_achievements}",
    )
    print()

    print("Alice vs Bob common:", analyzer.common_achievements(alice, bob))
    print("Alice unique:", alice.achievements - bob.achievements)
    print("Bob unique:", bob.achievements - alice.achievements)


if __name__ == "__main__":
    ft_achievement_tracker()
