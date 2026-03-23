from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self, name="AggressiveStrategy"):
        super().__init__(name)

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return self.name

    def prioritize_targets(self, available_targets: list) -> list:
        pass
