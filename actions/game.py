import random

from actions.exceptions import InvalidException
from actions.rules import Rules
from models.actions import ActionEnum, Actions
from models.entity import EntityEnum
from models.player import PlayerEnum


class Game:
    game_number: int = 0

    def __init__(self):
        print()
        print("Starting new game")
        self.print_help()
        self.add_game()

    @staticmethod
    def print_help():
        print(f"{ActionEnum.QUIT.value} - Quit")
        print(f"{ActionEnum.STATISTICS.value} - Statistics")
        print("Please enter your value:")
        print(f"{EntityEnum.ROCK.value} - Rock")
        print(f"{EntityEnum.PAPER.value} - Paper")
        print(f"{EntityEnum.SCISSORS.value} - Scissors")

    @classmethod
    def add_game(cls):
        cls.game_number += 1

    @staticmethod
    def get_user_input():
        user_in = input("> ")
        if user_in in EntityEnum.get_values():
            return Game.validate_user_input(user_in)
        if user_in in ActionEnum.get_values():
            Actions.get_action(user_in)()

    @staticmethod
    def get_computer_input():
        return random.choices(list(EntityEnum), k=1)[0]

    @staticmethod
    def validate_user_input(user_input: str) -> bool:
        if int(user_input) in EntityEnum.get_values():
            return EntityEnum(user_input)
        else:
            raise InvalidException()

    @staticmethod
    def calculate_winner(user_input, computer_input) -> PlayerEnum:
        winning_matrix = Rules.build_winning_matrix()

        def calculate_winner_player(index: int) -> PlayerEnum:
            inputs = {
                PlayerEnum.USER: user_input,
                PlayerEnum.COMPUTER: computer_input
            }
            for k, v in inputs.items():
                if v.value == index:
                    return k
            return PlayerEnum.TIE

        winning_index = winning_matrix[computer_input.value][user_input.value]
        winner = calculate_winner_player(winning_index)
        return winner
