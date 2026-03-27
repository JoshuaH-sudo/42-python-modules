from typing import Callable


# LEGB rule: Local, Enclosing, Global, Built-in
def mage_counter() -> Callable:
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def inner(spell_power: int):
        nonlocal total_power
        total_power += spell_power
        return total_power

    return inner


def enchantment_Factory(enchantment_type: str) -> Callable:
    def add_enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"

    return add_enchantment


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: str | None = None):
        if value is not None:
            vault[key] = value
            return f"Stored: {key} -> {value}"
        return vault.get(key, "Key not found.")

    def recall(key: str):
        return vault.get(key, "Key not found.")

    return {"store": store, "recall": recall}


def scope_mysteries():
    counter = mage_counter()
    print("Mage Counter:")
    print(f"Call 1: {counter()}")  # Output: 1
    print(f"Call 2: {counter()}")  # Output: 2
    print(f"Call 3: {counter()}")  # Output: 3

    print("\nSpell Accumulator:")
    spell = spell_accumulator(10)
    print(f"Call 1: {spell(5)}")  # Output: 15
    print(f"Call 2: {spell(3)}")  # Output: 18

    print("\nEnchantment Factory:")
    fire_enchant = enchantment_Factory("Fire")
    frozen_enchant = enchantment_Factory("Frozen")
    print(fire_enchant("Sword"))  # Output: "Fire Sword"
    print(frozen_enchant("Shield"))  # Output: "Frozen Shield"

    print("\nMemory Vault:")
    store, recall = memory_vault().values()
    print(store("spell1", "Fireball"))  # Output: "Stored: spell1 -> Fireball"
    print(store("spell2", "Heal"))  # Output: "Stored: spell2 -> Heal"
    print(recall("spell1"))  # Output: "Fireball"
    print(recall("spell2"))  # Output: "Heal"
    print(recall("spell3"))  # Output: "Key not found."


if __name__ == "__main__":
    scope_mysteries()
