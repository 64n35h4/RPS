import random

from actions.rules import Rules
from actions.utils import print_help, get_winner_player
from models.actions import ActionEnum, Actions
from models.entity import EntityEnum
from models.player import PlayerEnum


class Game:
    game_number: int = 0
    user_winning: int = 0
    computer_winning: int = 0
    tie_winning: int = 0

    def __init__(self):
        print()
        print("Starting new game")

    @staticmethod
    def print_help():
        print()
        print_help()

    @classmethod
    def add_game(cls):
        cls.game_number += 1

    @staticmethod
    def get_user_input():
        user_in = input("> ")
        if user_in in ActionEnum.get_values():
            Actions.get_action(user_in)()
        elif int(user_in) in EntityEnum.get_values():
            return EntityEnum(int(user_in))

    @staticmethod
    def get_computer_input():
        return random.choices(list(EntityEnum), k=1)[0]

    @staticmethod
    def calculate_winner(user_input, computer_input) -> PlayerEnum:
        winning_matrix = Rules.build_winning_matrix()
        inputs = {
            PlayerEnum.USER: user_input,
            PlayerEnum.COMPUTER: computer_input
        }
        winning_index = winning_matrix[computer_input.value][user_input.value]
        winner = get_winner_player(winning_index, inputs)
        Game.update_winner(winner)
        return winner

    @classmethod
    def update_winner(cls, winner):
        mapper = {
            PlayerEnum.TIE: "tie_winning",
            PlayerEnum.USER: "user_winning",
            PlayerEnum.COMPUTER: "computer_winning"
        }
        player = mapper.get(winner)
        if player:
            setattr(cls, player, getattr(cls, player) + 1)
