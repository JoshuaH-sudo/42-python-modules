import math


def calculate_distance(
    start: tuple[int, int, int], end: tuple[int, int, int]
) -> float:
    x1, y1, z1 = map(float, start)
    x2, y2, z2 = map(float, end)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple[float, float, float] | None:
    try:
        x_str, y_str, z_str = (
            coord_str.strip().strip("'").strip('"').split(",")
        )
    except ValueError:
        print("Invalid syntax")
        return None
    try:
        for coord in (x_str, y_str, z_str):
            float(coord)
        return float(x_str), float(y_str), float(z_str)
    except ValueError as e:
        print(f"Error on parameter: '{coord}': {e}")
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
    print(f"Get a first tuple: {player_position}")
    print(
        f"It includes: X={player_position[0]},"
        f" Y={player_position[1]},"
        f" Z={player_position[2]}"
    )
    distance_from_origin = calculate_distance((0, 0, 0), player_position)
    print(f"Distance to center: {distance_from_origin:.4f}\n")

    print("Get a second set of coordinates")
    while True:
        coordinates_str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        coordinates = parse_coordinates(coordinates_str)
        if coordinates is not None:
            break
    coordinates = parse_coordinates(coordinates_str)
    position_from_origin = calculate_distance(player_position, coordinates)
    print(
        f"Distance between 2 sets of coordinates: {position_from_origin:.4f}",
    )


if __name__ == "__main__":
    ft_coordinate_system()
