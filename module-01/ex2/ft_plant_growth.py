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


def ft_plant_growth() -> None:
    rose = Plant("rose", 25, 30)
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
