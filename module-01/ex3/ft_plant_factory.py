#! /usr/bin/env python3

class Plant:
    """
    A class to represent a plant in the garden.
    Attributes:
        name (str): The name of the plant.
        height_cm (int): The height of the plant in centimeters.
        age_days (int): The age of the plant in days.
    """
    def __init__(self, name: str, height_cm: int, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def get_info(self):
        """
        Displays the plant's information in a formatted string.
        """
        print(
            f"{self.name.capitalize()}: "
            f"{self.height_cm}cm, "
            f"{self.age_days} days old"
        )

    def grow(self, cm: int):
        """
        Increases the height of the plant by a specified number of centimeters.
        Args:
            cm (int): The number of centimeters to grow the plant.
        """
        self.height_cm += cm

    def age(self, days: int):
        """
        Increases the age of the plant by a specified number of days.
        Args:
            days (int): The number of days to age the plant.
        """
        self.age_days += days


def ft_plant_factory():
    names = ["rose", "oak", "cactus", "sunflower", "fern"]
    heights = [25, 200, 5, 80, 15]
    ages = [30, 365, 90, 45, 120]

    print("=== Plant Factory Output ===")
    for i in range(len(names)):
        plant = Plant(names[i], heights[i], ages[i])
        print(
            f"Created: {plant.name.capitalize()} "
            f"({plant.height_cm}cm, {plant.age_days} days)"
        )
    print("\n")
    print(f"Total plants created: {len(names)}")


if __name__ == "__main__":
    ft_plant_factory()
