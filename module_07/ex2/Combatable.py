from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> Dict:
        raise NotImplementedError("Subclasses must implement attack method")

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        raise NotImplementedError("Subclasses must implement defend method")

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        raise NotImplementedError(
            "Subclasses must implement get_combat_stats method"
        )
