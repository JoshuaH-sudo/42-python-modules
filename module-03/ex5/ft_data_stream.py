# import time

import typing


events = ["level_up", "found_treasure", "killed_monster"]
players = ["Alice", "Bob", "Charlie"]

class DataProcessor:
    event_processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    def process_data(self, data_stream: typing.Generator[typing.Tuple[str, str, int], None, None]) -> None:
        for event, player, level in data_stream:
            self.event_processed += 1
            print(
                f"Event {self.event_processed}: Player {player}",
                f"(level {level}) {event}",
            )
            if level >= 10:
                self.high_level_players += 1
            if event == "found_treasure":
                self.treasure_events += 1
            if event == "level_up":
                self.level_up_events += 1


def event_stream(n: int) -> typing.Generator[typing.Tuple[str, str, int], None, None]:
    for i in range(n):
        event = events[i % len(events)]
        player = players[i % len(players)]
        level = (i // len(players)) + 1
        yield (event, player, level)


def fibonacci(n: int) -> typing.Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n: int) -> typing.Generator[int, None, None]:
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===\n")
    processor = DataProcessor()
    data_stream = event_stream(1000)

    # start_time = time.perf_counter()
    processor.process_data(data_stream)
    # end_time = time.perf_counter()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {processor.event_processed}")
    print(f"High-level players: {processor.high_level_players}")
    print(f"Treasure events: {processor.treasure_events}")
    print(f"Level up events: {processor.level_up_events}")
    # print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fib_stream = fibonacci(10)
    fib_values = [str(next(fib_stream)) for _ in range(10)]
    separator = ", "
    print("Fibonacci sequence (first 10):", f"{separator.join(fib_values)}")

    prime_stream = primes(5)
    prime_values = [str(next(prime_stream)) for _ in range(5)]
    print("Prime numbers (first 5):", f"{separator.join(prime_values)}")


if __name__ == "__main__":
    ft_data_stream()
