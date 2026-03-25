from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        raise NotImplementedError(
            "Subclasses must implement cast_spell method"
        )

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        raise NotImplementedError(
            "Subclasses must implement channel_mana method"
        )

    @abstractmethod
    def get_magic_stats(self) -> dict:
        raise NotImplementedError(
            "Subclasses must implement get_magic_stats method"
        )
