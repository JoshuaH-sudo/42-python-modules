#!/usr/bin/env python3

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

    def get_info(self, plant_type: str, extra_info: str = ""):
        """
        Displays the plant's information in a formatted string.
        Args:
            extra_info (str): Additional information to display.
        """
        info = (
            f"{self.name.capitalize()} "
            f"({plant_type.capitalize()}): "
            f"{self.height_cm}cm, "
            f"{self.age_days} days old"
        )
        if extra_info:
            info += f", {extra_info}"
        print(info)


class Flower(Plant):
    """
    A class to represent a flower, inheriting from Plant.
    """

    def __init__(self, name: str, height_cm: int, age_days: int, color: str):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def get_info(self):
        """
        Displays the flower's information including its color.
        """
        super().get_info("Flower", f"{self.color} color")

    def bloom(self):
        """
        Simulates the blooming of the flower.
        """
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    """
    A class to represent a tree, inheriting from Plant.
    """

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        trunk_diameter: int,
    ):
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        """
        Displays the tree's information including its trunk diameter.
        """
        super().get_info("Tree", f"{self.trunk_diameter}cm diameter")

    def produce_shade(self):
        """
        Simulates the tree producing shade.
        """
        print(f"{self.name.capitalize()} provides 78 square meters of shade")


class Vegetable(Plant):
    """
    A class to represent a vegetable, inheriting from Plant.
    """

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        harvest_season: str,
        nutritional_value: str,
    ):
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        """
        Displays the vegetable's information including its harvest season
        and nutritional value.
        """
        super().get_info("Vegetable", f"{self.harvest_season} harvest")
        print(f"{self.name.capitalize()} is rich in {self.nutritional_value}")


def ft_plant_types():
    """
    Function to create multiple Plant instances of different types and
    display their information.
    """
    flower = Flower("rose", 25, 30, "red")
    tree = Tree("oak", 500, 1825, 50)
    vegetable = Vegetable("tomato", 80, 90, "summer", "Vitamin C")

    print("=== Garden Plant Types ===")
    print("\n")

    flower.get_info()
    flower.bloom()
    print("\n")

    tree.get_info()
    tree.produce_shade()
    print("\n")

    vegetable.get_info()
    print("\n")


if __name__ == "__main__":
    ft_plant_types()
