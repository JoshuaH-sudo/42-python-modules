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
    plants_data = [
        {"name": "rose", "height_cm": 25, "age_days": 30},
        {"name": "oak", "height_cm": 200, "age_days": 365},
        {"name": "cactus", "height_cm": 5, "age_days": 90},
        {"name": "sunflower", "height_cm": 80, "age_days": 45},
        {"name": "fern", "height_cm": 15, "age_days": 120},
    ]

    print("=== Plant Factory Output ===")
    for plant_data in plants_data:
        plant = Plant(
            plant_data["name"],
            plant_data["height_cm"],
            plant_data["age_days"],
        )
        print(
            f"Created: {plant.name.capitalize()} "
            f"({plant.height_cm}cm, {plant.age_days} days)"
        )
    print("\n")
    print(f"Total plants created: {len(plants_data)}")


if __name__ == "__main__":
    ft_plant_factory()
