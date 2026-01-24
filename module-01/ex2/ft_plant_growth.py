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


def ft_plant_growth():
    """
    This function simulates the growth of a plant over a period of days.
    """
    rose = Plant("Rose", 25, 30)
    start_size = rose.height_cm

    print("=== Day 1 ===")
    rose.get_info()

    for _ in range(6):
        rose.grow(1)
        rose.age(1)

    print("=== Day 7 ===")
    rose.get_info()

    end_size = rose.height_cm
    difference = end_size - start_size
    print(f"Growth this week: +{difference}cm")


if __name__ == "__main__":
    ft_plant_growth()
