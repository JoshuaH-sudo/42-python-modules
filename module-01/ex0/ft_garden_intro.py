#!/usr/bin/env python3


def ft_garden_intro() -> None:
    """
    This function introduces a simple garden with one plant.
    It prints the plant's name, height, and age.
    """
    plant_name = "rose"
    plant_height = 25
    plant_age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name.capitalize()}")
    print(f"Height: {plant_height} cm")
    print(f"Age: {plant_age} days")
    print("\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
