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
    total_power = sum(map(lambda mage: mage["power"], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def lambda_spells():
    artifacts = [
        {"name": "Orb", "power": 1},
        {"name": "staff", "power": 10},
        {"name": "sword", "power": 3},
    ]
    print(artifact_sorter(artifacts))
    mages = [
        {"name": "gandalf", "power": 3, "element": "Fire"},
        {"name": "avatar", "power": 12, "element": "Wind"},
        {"name": "harry", "power": 7, "element": "Dark"},
    ]
    print(power_filter(mages, 7))
    spells = ["fireball", "lighting bolt", "abrakadabra"]
    print(spell_transformer(spells))
    print(mage_stats(mages))
    pass


if __name__ == "__main__":
    lambda_spells()
