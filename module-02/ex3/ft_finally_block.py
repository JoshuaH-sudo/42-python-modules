def water_plants(plant_list: list[str]):
    """
    Simulates watering plants, demonstrating the use of a finally block for cleanup.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Invalid plant: None")
            print(f"Watering {plant}")
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant")
    finally:
        print("Closing water system (cleanup)")
        return
    print("Watering completed successfully!")


def test_watering_system():
    """
    Tests the watering system with both normal and error scenarios.
    """
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")
    print("\n", end="")

    print("Testing with error...")
    plants_with_error = ["tomato", None]
    water_plants(plants_with_error)
    print("\n", end="")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
