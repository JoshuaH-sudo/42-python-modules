def check_temperature(temp_str: str) -> int:
    """
    Check if the given temperature string is a valid temperature for plants.
    Valid temperature range for plants is 0°C to 40°C.
    :param temp_str: Temperature as a string
    :return: Temperature as an integer if valid
    """
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")
    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    """
    Test the check_temperature function with various inputs.
    """
    print("=== Garden Temperature Checker ===\n")
    test_values = ["25", "abc", "100", "-50"]
    for val in test_values:
        try:
            print("Testing temperature:", val)
            result = check_temperature(val)
            print(f"Temperature {result}°C is perfect for plants!")
        except ValueError as e:
            print(e)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
