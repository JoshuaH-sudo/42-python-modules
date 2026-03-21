def validate_ingredients(ingredients: str) -> str:
    normalized_ingredients = ingredients.lower()
    valid_ingredients = ("fire", "water", "earth", "air")

    for ingredient in valid_ingredients:
        if ingredient in normalized_ingredients:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"