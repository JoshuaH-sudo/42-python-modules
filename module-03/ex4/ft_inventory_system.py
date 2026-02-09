def pluralize(unit: int, singular: str, plural: str) -> str:
    return singular if unit == 1 else plural


class Inventory:
    items = dict()

    def __init__(self, items: dict):
        self.items = items

    def get_unique_items(self):
        return set(self.items.keys())

    def get_total_items(self):
        total = 0
        for quantity in self.items.values():
            total += quantity
        return total

    def print_inventory(self):
        print("=== Current Inventory ===")
        for item, quantity in self.items.items():
            percentage = (quantity / self.get_total_items()) * 100
            print(
                f"{item}: {quantity}",
                f"{pluralize(quantity, 'unit', 'units')} ({percentage:.1f}%)",
            )

    def inventory_statistics(self):
        most_abundant: dict[str, int] | None = None
        least_abundant: dict[str, int] | None = None
        for item, quantity in self.items.items():
            if most_abundant is None or quantity > self.items[most_abundant]:
                most_abundant = item
            if least_abundant is None or quantity < self.items[least_abundant]:
                least_abundant = item

        print("=== Inventory Statistics ===")
        print(
            f"Most abundant: {most_abundant}",
            f"({self.items[most_abundant]}",
            f"{pluralize(self.items[most_abundant], 'unit', 'units')})",
        )
        print(
            f"Least abundant: {least_abundant}",
            f"({self.items[least_abundant]}",
            f"{pluralize(self.items[least_abundant], 'unit', 'units')})",
        )

    def print_categories(self):
        moderate_items = {}
        scarce_items = {}

        # if units is greater than 5, it's moderate, otherwise it's scarce
        for item, quantity in self.items.items():
            if quantity >= 5:
                moderate_items[item] = quantity
            else:
                scarce_items[item] = quantity

        print("=== Item Categories ===")
        print(f"Moderate Items: {moderate_items}")
        print(f"Scarce Items: {scarce_items}")

    def management_suggestions(self):
        # if units equals to 1, suggest to restock
        restock_suggestions = []
        for item, quantity in self.items.items():
            if quantity == 1:
                restock_suggestions.append(item)
        if restock_suggestions:
            print("=== Management Suggestions ===")
            print(f"Restock needed: {restock_suggestions}")


def ft_inventory_system():
    inventory = Inventory(
        {"potion": 5, "armor": 3, "shield": 2, "sword": 1, "helmet": 1}
    )
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {inventory.get_total_items()}")
    print(f"Unique items types: {inventory.get_unique_items()}")
    print()

    inventory.print_inventory()
    print()
    inventory.inventory_statistics()
    print()
    inventory.print_categories()
    print()
    inventory.management_suggestions()
    print()

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.items.keys()}")
    print(f"Dictionary values: {inventory.items.values()}")
    print(
        f"Sample lookup - 'sword' in inventory: {'sword' in inventory.items}"
    )


if __name__ == "__main__":
    ft_inventory_system()
