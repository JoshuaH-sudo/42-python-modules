def ft_analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===\n")
    game_data = [
        {
            "player": "alice",
            "score": 2300,
            "achievements": [
                "first_blood",
                "sharp_shooter",
                "smith_expert",
                "mage",
                "speedster",
            ],
            "isActive": True,
            "region": "north",
        },
        {
            "player": "bob",
            "score": 1800,
            "achievements": ["veteran", "banana", "level_10"],
            "isActive": True,
            "region": "central",
        },
        {
            "player": "charlie",
            "score": 2150,
            "achievements": [
                "first_blood",
                "sharp_shooter",
                "treasure_hunter",
                "mage",
                "speedster",
                "loot",
                "epic_gamer",
            ],
            "isActive": True,
            "region": "east",
        },
        {
            "player": "diana",
            "score": 700,
            "achievements": ["rookie"],
            "isActive": False,
            "region": "north",
        },
    ]

    print("=== List Comprehension Examples ===")
    high_scores = [
        entry["player"] for entry in game_data if entry["score"] > 2000
    ]
    doubled_scores = [entry["score"] * 2 for entry in game_data]
    active_players = [
        entry["player"] for entry in game_data if entry["isActive"]
    ]

    print(f"High scores (>2000): {high_scores}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")

    print("\n=== Dictionary Comprehension Example ===")
    players = {entry["player"]: entry for entry in game_data}
    player_scores = {player: info["score"] for player, info in players.items()}
    score_categories = {
        player: (
            "high"
            if info["score"] >= 2000
            else "medium" if info["score"] >= 1000 else "low"
        )
        for player, info in players.items()
    }
    achievement_counts = {
        player: len(info["achievements"]) for player, info in players.items()
    }
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Example ===")
    unique_players = {entry["player"] for entry in game_data}
    unique_achievements = {
        achievement
        for entry in game_data
        for achievement in entry["achievements"]
    }
    active_regions = {entry["region"] for entry in game_data}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(unique_players)
    total_achievements = len(unique_achievements)
    average_score = sum(player_scores.values()) / total_players
    top_performer = max(player_scores, key=player_scores.get)

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_achievements}")
    print(f"Average score: {average_score:.2f}")
    print(
        f"Top performer: {top_performer}",
        f"({player_scores[top_performer]} points,",
        f"{achievement_counts[top_performer]} achievements)",
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
