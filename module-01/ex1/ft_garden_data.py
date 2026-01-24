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


def ft_garden_data():
    """
    This function creates a list of plants and displays their information.
    """
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.get_info()


if __name__ == "__main__":
    ft_garden_data()
