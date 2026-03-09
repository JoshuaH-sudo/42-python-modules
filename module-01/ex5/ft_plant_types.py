class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def get_info(self, plant_type: str, extra_info: str = "") -> None:
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
    def __init__(self, name: str, height_cm: int, age_days: int, color: str):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def get_info(self) -> None:
        super().get_info("Flower", f"{self.color} color")

    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        trunk_diameter: int,
    ):
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        super().get_info("Tree", f"{self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name.capitalize()} provides 78 square meters of shade")


class Vegetable(Plant):
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

    def get_info(self) -> None:
        super().get_info("Vegetable", f"{self.harvest_season} harvest")
        print(f"{self.name.capitalize()} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
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
