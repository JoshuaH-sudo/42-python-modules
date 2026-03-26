from typing import Dict, List
from ex0.Card import Card
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    deck: Dict
    hand: List[Card] = []
    total_damage: int = 0
    cards_created: int = 0
    turn_count: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.deck = self.factory.create_themed_deck(30)

    def simulate_turn(self) -> Dict:
        if self.hand.__len__() == 0:
            self.hand = (
                self.deck["creature"][:1]
                + self.deck["spell"][:1]
                + self.deck["artifact"][:1]
            )
            self.cards_created += self.hand.__len__()
            current_hand = ", ".join(
                f"{card.name} ({card.cost})" for card in self.hand
            )
            return {
                "current_hand": current_hand,
            }
        self.turn_count += 1
        battlefield = ["Enemy Player"]
        turn_result = self.strategy.execute_turn(self.hand, battlefield)
        damage_dealt = turn_result.get("damage_dealt", 0)
        self.total_damage += damage_dealt

        return turn_result

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turn_count,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
