import sys
import math


def calculate_distance(
    start: tuple[int, int, int], end: tuple[int, int, int]
) -> float:
    x1, y1, z1 = map(float, start)
    x2, y2, z2 = map(float, end)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    try:
        x_str, y_str, z_str = coord_str.split(",")
        return int(x_str), int(y_str), int(z_str)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        raise e


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    received_arguments = sys.argv[1:]

    try:
        player_position = parse_coordinates(received_arguments[0])
        coordinates = parse_coordinates(received_arguments[1])
    except Exception as e:
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
        return None
    print(f"Position created: {player_position}")
    distance_from_origin = calculate_distance((0, 0, 0), player_position)
    print(
        f"Distance between (0, 0, 0) and {player_position}:",
        f"{distance_from_origin:.2f}\n",
    )

    print(f'Position coordinates: "{received_arguments[1]}"')
    print(f"Parsed position: {coordinates}")
    position_from_origin = calculate_distance((0, 0, 0), coordinates)
    print(
        f"Distance between (0, 0, 0) and {coordinates}:",
        f"{position_from_origin:.1f}",
    )

    print("\nUnpacking demonstration:")
    x, y, z = player_position
    print(f"Player at x={x}, y={y}, z={z}")
    x, y, z = coordinates
    print(f"Coordinates at X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
