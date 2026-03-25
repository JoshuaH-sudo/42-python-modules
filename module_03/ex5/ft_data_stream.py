import random
import typing


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "move",
    "grab",
    "release",
    "eat",
    "sleep",
    "climb",
    "run",
    "swim",
    "use",
]


def gen_event() -> typing.Generator[typing.Tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events: list[typing.Tuple[str, str]],
) -> typing.Generator[typing.Tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def ft_data_stream() -> None:
    stream = gen_event()
    for index in range(1000):
        player, action = next(stream)
        print(f"Event {index + 1}: Player {player} did action {action}")

    ten_events: list[typing.Tuple[str, str]] = list()
    for _ in range(10):
        ten_events.append(next(stream))
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    ft_data_stream()
