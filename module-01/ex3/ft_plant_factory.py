#! /usr/bin/env python3


class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height_cm}cm, "
            f"{self.age_days} days old"
        )

    def grow(self, cm: int):
        self.height_cm += cm

    def age(self, days: int):
        self.age_days += days


def ft_plant_factory() -> None:
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
