# type: ignore
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any, Callable, Dict, List

import time


def spell_reducer(spells: List[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "mul":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    else:
        return -1


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lighting_enchant": partial(
            base_enchantment, power=50, element="lighting"
        ),
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(arg: Any) -> Callable:
    return spell_dispatcher


@spell_dispatcher.register
def _(enchantment: str) -> Callable:
    def apply_enchantment(target: str) -> Dict:
        return {"enchantment": enchantment, "target": target}

    return apply_enchantment


@spell_dispatcher.register
def _(damage: int) -> Dict:
    return {"damage": damage}


@spell_dispatcher.register
def _(multi_cast: list) -> Dict:
    return {"multi_cast": multi_cast}


def base_enchantment(power: int, element: str, target: str) -> Dict:
    return {"power": power, "element": element, "target": target}


def functools_artifacts():
    spell_powers = [10, 20, 5, 15]
    print("Spell Powers:", spell_powers)
    print("Sum of Spell Powers:", spell_reducer(spell_powers, "add"))
    print("Product of Spell Powers:", spell_reducer(spell_powers, "mul"))
    print("Max Spell Power:", spell_reducer(spell_powers, "max"))
    print("Min Spell Power:", spell_reducer(spell_powers, "min"))
    print("")

    print("Partial Enchanter:")
    (fire_enchantment, ice_enchantment, lighting_enchantment) = (
        partial_enchanter(base_enchantment).values()
    )
    print(fire_enchantment(target="sword"))
    print(ice_enchantment(target="shield"))
    print(lighting_enchantment(target="armor"))
    print("")

    print("Memoized Fibonacci:")
    begin = time.time()
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(20):", memoized_fibonacci(20))
    print("Fib(30):", memoized_fibonacci(30))
    end = time.time()
    print(f"Execution Time: {end - begin:.10f} seconds\n")

    print("Spell Dispatcher:")
    damage_spell = spell_dispatcher(25)
    enchantment_spell = spell_dispatcher("flame")
    multi_cast_spell = spell_dispatcher([10, 20, 30])
    print("Damage Spell:", damage_spell)
    print("Enchantment Spell:", enchantment_spell("sword"))
    print("Multi-Cast Spell:", multi_cast_spell)


if __name__ == "__main__":
    functools_artifacts()
