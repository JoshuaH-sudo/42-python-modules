import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    capitalized_players = [name.capitalize() for name in players]
    initially_capitalized = [name for name in players if name[0].isupper()]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {initially_capitalized}")

    score_dict = {
        name: random.randint(50, 999) for name in capitalized_players
    }
    score_average = round(sum(score_dict.values()) / len(score_dict), 2)
    high_scores = {
        name: score
        for name, score in score_dict.items()
        if score > score_average
    }

    print(f"Score dict: {score_dict}")
    print(f"Score average is {score_average}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
