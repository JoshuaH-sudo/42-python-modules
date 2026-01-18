def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        message = f"{quantity} packets available"
    elif (unit == "grams"):
        message = f"{quantity} grams total"
    elif (unit == "area"):
        message = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: {message}")
