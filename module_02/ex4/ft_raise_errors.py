def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> None:
    # check plant name is not empty
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    # check water level is within acceptable range 1 - 10
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    # check sunlight hours is within acceptable range 2 - 12
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    print(
        f"Plant '{plant_name}' is healthy!",
    )


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    # Test with valid inputs
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n", end="")

    # Test with empty plant name
    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n", end="")

    # Test with invalid water level
    try:
        print("Testing bad water level...")
        check_plant_health("lettuce", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n", end="")

    # Test with invalid sunlight hours
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("carrot", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n", end="")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
