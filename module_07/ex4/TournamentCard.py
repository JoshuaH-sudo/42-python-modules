from random import randint

from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.damage = randint(1, 10)
        self.health = randint(1, 10)
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {"error": "Not enough mana to play this card."}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the battlefield",
        }

    def calculate_rating(self) -> int:
        win_loss_ratio = (
            self.wins / (self.losses + 1) + self.damage + self.health * 100
        )
        return int(win_loss_ratio)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.damage,
            "health": self.health,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.damage,
        }

    def defend(self, incoming_damage: int) -> dict:
        actual_damage = incoming_damage - (self.health // 2)
        self.health -= actual_damage
        return {
            "defender": self.name,
            "incoming_damage": incoming_damage,
            "actual_damage_taken": actual_damage,
            "health_remaining": self.health,
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.damage,
            "health": self.health,
            "rating": self.calculate_rating(),
        }
