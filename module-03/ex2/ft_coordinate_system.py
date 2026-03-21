import math


def calculate_distance(
    start: tuple[int, int, int], end: tuple[int, int, int]
) -> float:
    x1, y1, z1 = map(float, start)
    x2, y2, z2 = map(float, end)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple[float, float, float] | None:
    try:
        x_str, y_str, z_str = coord_str.split(",")
        return float(x_str.strip()), float(y_str.strip()), float(z_str.strip())
    except ValueError as e:
        return None


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    while True:
        player_position_str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        player_position = parse_coordinates(player_position_str)
        if player_position is not None:
            break
        print("Invalid syntax")
    distance_from_origin = calculate_distance((0, 0, 0), player_position)
    print(
        "Distance between (0, 0, 0) and",
        f"{player_position}: {distance_from_origin:.2f}",
    )
    print("")

    coordinates_str = "3,4,0"
    print(f'Parsing coordinates: "{coordinates_str}"')
    coordinates = parse_coordinates(coordinates_str)
    print(f"Parsed position: {coordinates}")
    position_from_origin = calculate_distance((0, 0, 0), coordinates)
    print(
        "Distance between (0, 0, 0) and",
        f"{coordinates}: {position_from_origin:.1f}",
    )
    print("")

    invalid_coordinates_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_coordinates_str}"')
    try:
        parse_coordinates(invalid_coordinates_str)
    except Exception as e:
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
    print("")

    print("Unpacking demonstration:")
    x, y, z = coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
