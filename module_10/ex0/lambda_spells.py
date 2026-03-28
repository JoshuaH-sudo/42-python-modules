from typing import List, Dict


# ’name’: str, ’power’: int, ’type’: str}
def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda spell: f"*{spell}*", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = sum(map(lambda mage: mage["power"], mages)) / mages.__len__()

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": f"{avg_power:.2f}",
    }


def lambda_spells() -> None:
    artifacts = [
        {"name": "Earth Shield", "power": 112, "type": "armor"},
        {"name": "Earth Shield", "power": 72, "type": "focus"},
        {"name": "Lightning Rod", "power": 66, "type": "focus"},
        {"name": "Wind Cloak", "power": 98, "type": "relic"},
    ]
    mages = [
        {"name": "Luna", "power": 10, "element": "shadow"},
        {"name": "Ember", "power": 15, "element": "water"},
        {"name": "Ash", "power": 69, "element": "light"},
        {"name": "Morgan", "power": 81, "element": "lightning"},
        {"name": "Kai", "power": 66, "element": "fire"},
    ]
    spells = ["shield", "heal", "fireball", "meteor"]
    print("Original Artifacts:")
    print(artifacts)
    print("\nOriginal Mages:")
    print(mages)
    print("\nOriginal Spells:")
    print(spells)

    print("\n========================================")

    print("\nSorted Artifacts by Power:")
    print(artifact_sorter(artifacts))
    print("\nMages with Power >= 60:")
    print(power_filter(mages, 60))
    print("\nTransformed Spells:")
    print(spell_transformer(spells))
    print("\nMage Stats:")
    print(mage_stats(mages))
    pass


if __name__ == "__main__":
    lambda_spells()
