#!/usr/bin/env python3
class SecurePlant:
    """
    A class to represent a plant in the garden.
    Attributes:
        name (str): The name of the plant.
        height_cm (int): The height of the plant in centimeters.
        age_days (int): The age of the plant in days.
    """

    def __init__(self, name: str, height_cm: int, age_days: int):
        self._name = name
        print(f"Plant created: {self._name.capitalize()}")
        self.set_height(height_cm)
        self.set_age(age_days)

    def get_height(self) -> int:
        """
        Returns the height of the plant.
        """
        return self._height_cm

    def set_height(self, height_cm: int):
        """
        Sets the height of the plant, ensuring it is not negative.
        Args:
            height_cm (int): The new height of the plant in centimeters.
        """
        if height_cm < 0:
            print(
                "Invalid operation attempted:",
                f"height {height_cm}cm (REJECTED)",
            )
            print("Security: Negative height rejected")
            return
        self._height_cm = height_cm
        print(f"Height updated: {self._height_cm}cm [OK]")

    def get_age(self) -> int:
        """
        Returns the age of the plant.
        """
        return self._age_days

    def set_age(self, age_days: int):
        """
        Sets the age of the plant, ensuring it is not negative.
        Args:
            age_days (int): The new age of the plant in days.
        """
        if age_days < 0:
            print(
                "Invalid operation attempted:",
                f"age {age_days} days (REJECTED)",
            )
            print("Security: Negative age rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days [OK]")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("rose", 25, 30)
    print("\n")
    rose.set_height(-5)
    print("\n")
    print(
        f"Current plant: {rose._name.capitalize()} ",
        f"({rose.get_height()}cm, {rose.get_age()} days)",
    )


if __name__ == "__main__":
    ft_garden_security()
