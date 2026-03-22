from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        raise NotImplementedError("Subclasses must implement attack method")

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        raise NotImplementedError("Subclasses must implement defend method")

    @abstractmethod
    def get_combat_stats(self) -> dict:
        raise NotImplementedError(
            "Subclasses must implement get_combat_stats method"
        )
