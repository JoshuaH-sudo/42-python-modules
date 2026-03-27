from typing import Callable


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target: [spell(target) for spell in spells]


def fireball(target):
    return f"Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def lightning(target):
    return f"Lightning strikes {target}"


def fireball_power(power):
    return power


def is_enemy(target):
    return target in ["Goblin", "Orc"]


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target: (spell1(target), spell2(target))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda power: base_spell(power) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target: (
        spell(target) if condition(target) else "Spell fizzled"
    )


def higher_magic():
    combined = spell_combiner(fireball, heal)
    print("Testing spell combiner:")
    print(f"Combined Spell Result: {combined('Dragon')}\n")

    mega_fireball = power_amplifier(fireball_power, 3)
    print("Testing power amplifier:")
    print(f"Original: {fireball_power(10)} Amplified: {mega_fireball(10)}\n")

    conditional_attack = conditional_caster(is_enemy, fireball)
    print("Testing conditional caster:")
    print(f"Enemy Target: {conditional_attack('Goblin')}")
    print(f"Friendly Target: {conditional_attack('Knight')}\n")

    spells = [fireball, heal, lightning]
    sequence = spell_sequence(spells)
    print("Testing spell sequence:")
    print(f"Spell Sequence Result: {sequence('Troll')}\n")


if __name__ == "__main__":
    higher_magic()
