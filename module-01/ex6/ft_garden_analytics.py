class Plant:
    """
    A class to represent a plant in the garden.
    Attributes:
        name (str): The name of the plant.
        height_cm (int): The height of the plant in centimeters.
        age_days (int): The age of the plant in days.
    """

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        score: int = 10,
        plant_type: str = "regular",
    ):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days
        self.score = score
        self.type = plant_type

    def get_info(self) -> str:
        """
        Displays the plant's information in a formatted string.
        Args:
            extra_info (str): Additional information to display.
        """
        return f"{self.name.capitalize()}: {self.height_cm}cm"

    def grow(self, cm: int):
        """
        Grows the plant by a specified number of centimeters.
        Args:
            cm (int): The number of centimeters to grow.
        """
        self.height_cm += cm
        print(f"{self.name.capitalize()} grew {cm}cm")


class Flowering(Plant):
    """
    A class to represent a flower, inheriting from Plant.
    """

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        color: str,
        points: int = 50,
        plant_type: str = "flowering",
    ):
        super().__init__(name, height_cm, age_days, points, plant_type)
        self.color = color

    def get_info(self) -> str:
        """
        Displays the flower's information including its color.
        """
        return (
            f"{self.name.capitalize()}: {self.height_cm}cm, "
            f"{self.color} flowers (blooming)"
        )

    def bloom(self) -> None:
        """
        Simulates the blooming of the flower.
        """
        print(f"{self.name.capitalize()} is blooming beautifully!")


class prizeFlower(Flowering):
    """
    A class to represent a prize flower, inheriting from Flower.
    """

    def __init__(
        self, name: str, height_cm: int, age_days: int, color: str, points: int
    ):
        super().__init__(
            name, height_cm, age_days, color, points, "prize flowers"
        )
        self.points = points

    def get_info(self) -> str:
        """
        Displays the prize flower's information including its award.
        """
        return (
            f"{self.name.capitalize()}: {self.height_cm}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.points}"
        )


class Garden:
    """
    A class to represent a garden containing multiple plants.
    """

    owner: str
    plants: list[Plant] = []
    total_growth: int = 0
    total_points: int = 0
    regular_plants: int = 0
    flowering_plants: int = 0
    prize_flowers: int = 0

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant):
        """
        Adds a plant to the garden.
        Args:
            plant (Plant): The plant to add.
        """
        self.plants.append(plant)
        self.total_points += plant.score
        if plant.type == "prize flowers":
            self.prize_flowers += 1
        elif plant.type == "flowering":
            self.flowering_plants += 1
        else:
            self.regular_plants += 1
        print(
            f"Added {plant.name.capitalize()} to",
            f"{self.owner.capitalize()}'s garden.",
        )

    def get_plant_count(self) -> int:
        """
        Returns the number of plants in the garden.
        Returns:
            int: The number of plants.
        """
        count = 0
        for _ in self.plants:
            count += 1
        return count

    def grow_all(self, cm: int):
        """
        Grows all plants in the garden by a specified number of centimeters.
        Args:
            cm (int): The number of centimeters to grow each plant.
        """

        print(
            f"{self.owner.capitalize()} is helping all plants grow...",
        )
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth += cm
        print("")


class GardenManager:
    """
    A class to manage multiple gardens.
    """

    gardens = dict[Garden]()

    def __init__(self, gardens: dict):
        self.gardens = gardens

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        """
        Creates a new garden for the specified owner.
        Args:
            owners (list[str]): List of garden owners.
        """
        new_gardens = dict()
        for owner in owners:
            new_gardens[owner] = Garden(owner)
        return cls(new_gardens)

    def get_garden(self, owner: str) -> Garden:
        """
        Retrieves a garden by owner name.
        Args:
            owner (str): The owner's name.
        Returns:
            Garden: The garden belonging to the owner.
        """
        return self.gardens.get(owner)

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        """
        Adds a plant to a specific garden.
        Args:
            owner (str): The owner's name.
            plant (Plant): The plant to add.
        """
        garden = self.get_garden(owner)
        stats = self.get_garden_stats(owner)
        if garden:
            garden.add_plant(plant)
            stats.record_plant(plant)

    def garden_report(self, owner: str):
        """
        Reports the statistics of a specific garden.
        Args:
            owner (str): The owner's name.
        """
        garden = self.get_garden(owner)
        if garden:
            self.GardenStats.print_garden_stats(garden)

    def manager_report(self) -> None:
        """
        Reports the overall statistics of all managed gardens.
        """
        self.GardenStats.print_manager_stats(self.gardens)

    class GardenStats:
        @staticmethod
        def print_garden_stats(garden: Garden):
            print(f"=== {garden.owner.capitalize()}'s Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                print(f"- {plant.get_info()}")
            print("")
            print(
                f"Plants added: {garden.get_plant_count()}",
                f"total growth: {garden.total_growth}cm",
            )
            print(
                f"Plant types: {garden.regular_plants} regular,",
                f"{garden.flowering_plants} flowering,",
                f"{garden.prize_flowers} prize flowers",
            )
            print("")

        @staticmethod
        def print_manager_stats(gardens: dict) -> None:
            garden_count = 0
            height_validated = True
            for owner in gardens:
                garden = gardens[owner]
                for plant in garden.plants:
                    if plant.height_cm < 0:
                        height_validated = False
                garden_count += 1
            print(f"Height validation test: {height_validated}")
            print("Garden scores: - ", end="")
            index = 0
            for owner in gardens:
                garden = gardens[owner]
                print(
                    f"{garden.owner.capitalize()}:",
                    f"{garden.total_points} points",
                    end="",
                )
                if index < garden_count - 1:
                    print(", ", end="")
                else:
                    print("")
                index += 1
            print(f"Total gardens managed: {garden_count}")


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    gardenManager = GardenManager.create_garden_network(["Alice", "Bob"])
    aliceGarden = gardenManager.get_garden("Alice")

    aliceGarden.add_plant(Plant("Oak Tree", 100, 120))
    aliceGarden.add_plant(Flowering("Rose", 25, 15, "Red"))
    aliceGarden.add_plant(prizeFlower("Sunflower", 50, 15, "Yellow", 50))
    print("\n")

    aliceGarden.grow_all(1)

    gardenManager.garden_report("Alice")

    gardenManager.manager_report()


if __name__ == "__main__":
    ft_garden_analytics()
