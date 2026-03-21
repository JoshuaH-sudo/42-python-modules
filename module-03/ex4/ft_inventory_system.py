import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory = {}
    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, quantity_str = arg.split(":", 1)
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        inventory[item] = quantity
    return inventory


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print(
            "Usage: ft_inventory_system.py <item_name>:<quantity> <item_name>:<quantity> ..."
        )
        return
    inventory = parse_inventory(sys.argv[1:])

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item in inventory.keys():
        percentage = round(inventory[item] / total * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant = None
    least_abundant = None
    for item in inventory.keys():
        if most_abundant is None or inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if (
            least_abundant is None
            or inventory[item] < inventory[least_abundant]
        ):
            least_abundant = item

    print(
        f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}"
    )
    print(
        f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
