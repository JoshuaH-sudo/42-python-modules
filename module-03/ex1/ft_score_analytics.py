import sys


def ft_score_analytics() -> None:
    print("=== Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            "No scores provided.",
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...",
        )
        return

    received_scores = sys.argv[1:]
    scores = []
    for score in received_scores:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
            continue

    if len(scores) == 0:
        print(
            "No scores provided.",
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...",
        )
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    score_range = max_score - min_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"Maximum score: {max_score}")
    print(f"Minimum score: {min_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
