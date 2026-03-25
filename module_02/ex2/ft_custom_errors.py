class GardenError(Exception):
    """Base class for all garden-related errors."""

    def __init__(self, message: str = "An error occurred in the garden."):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """Exception raised for errors related to plants."""

    def __init__(self, message: str = "An error occurred with the plants."):
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for errors related to watering."""

    def __init__(self, message: str = "An error occurred with watering."):
        super().__init__(message)


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as pe:
        print(f"Caught PlantError: {pe}")

    print()

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as we:
        print(f"Caught WaterError: {we}")

    print()

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as ge:
        print(f"Caught a garden error: {ge}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as ge:
        print(f"Caught a garden error: {ge}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
