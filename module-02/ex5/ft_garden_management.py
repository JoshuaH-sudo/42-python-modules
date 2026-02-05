class GardenError(Exception):
    """Custom exception for garden management errors."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        try:
            if plant_name is None or plant_name.strip() == "":
                raise ValueError("Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering plant: {plant} - success")
        except Exception as e:
            print(f"Error watering plants: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            # check plant name is not empty
            if not plant_name:
                raise ValueError("Plant name cannot be empty!")
            # check water level is within acceptable range 1 - 10
            if water_level > 10:
                raise GardenError(
                    f"Water level {water_level} is too high (max 10)"
                )
            if water_level < 1:
                raise GardenError(
                    f"Water level {water_level} is too low (min 1)"
                )
            # check sunlight hours is within acceptable range 2 - 12
            if sunlight_hours > 12:
                raise GardenError(
                    f"Sunlight hours {sunlight_hours}",
                    "is too high (max 12)",
                )
            if sunlight_hours < 2:
                raise GardenError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)"
                )
            print(
                f"{plant_name}: healthy",
                f"(water: {water_level}, sun: {sunlight_hours})",
            )
        except ValueError as e:
            print(f"Error checking plant health: {e}")
        except GardenError as e:
            print(f"Error checking {plant_name}: {e.message}")


def test_garden_management():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant(None)  # should trigger error
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 6)
    manager.check_plant_health("lettuce", 15, 6)  # should trigger error

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
