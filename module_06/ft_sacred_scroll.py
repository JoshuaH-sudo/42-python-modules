import alchemy
import alchemy.elements


def ft_sacred_scroll() -> None:
    print("=== Sacred Scroll Mastery ===")
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}"
    )
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}"
    )
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
    print("")

    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        earth_value = alchemy.create_earth()  # type: ignore[attr-defined]
        print(f"alchemy.create_earth(): {earth_value}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        air_value = alchemy.create_air()  # type: ignore[attr-defined]
        print(f"alchemy.create_air(): {air_value}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print("")

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    ft_sacred_scroll()
