from typing import Callable
from time import time
from functools import wraps
import random


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        begin = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - begin} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator_factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", 0)
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell."

        return wrapper

    return decorator_factory


def retry_spell(max_attempts: int) -> Callable:
    def decorator_factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, Retrying...",
                        f"({attempts + 1}/{max_attempts})",
                    )
                    attempts += 1
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator_factory


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}!"


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@power_validator(min_power=50)
def ice_shard(power: int) -> str:
    return f"Ice Shard cast with power {power}!"


@retry_spell(max_attempts=3)
def lightning_bolt() -> str:
    if random.random() < 0.5:
        raise Exception("Lightning Bolt failed!")
    return "Lightning Bolt cast successfully!"


def decorator_mastery() -> None:
    # print(fireball.__name__) # test by removing the @wraps decorator
    print("Testing spell timer...")
    print(f"Results: {fireball()}\n")

    print("Testing power validator...")
    print(f"Results: {ice_shard(power=30)}")
    print(f"Results: {ice_shard(power=60)}\n")

    print("Testing retry spell...")
    print(f"Results: {lightning_bolt()}\n")

    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf the Grey"))
    print(guild.validate_mage_name("Al"))
    print(guild.cast_spell(spell_name="Arcane Blast", power=15))
    print(guild.cast_spell(spell_name="Arcane Blast", power=5))


if __name__ == "__main__":
    decorator_mastery()
