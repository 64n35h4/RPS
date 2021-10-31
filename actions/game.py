import random

from actions.exceptions import InvalidException, GracefulExit
from actions.rules import build_winning_matrix
from actions.utils import print_help, get_winner_player, get_inputs
from models.commands import CommandEnum
from models.entity import EntityEnum
from models.player import PlayerEnum


def get_action(value):
    mapper = {
        CommandEnum.QUIT.value: Game.action_quit,
        CommandEnum.STATISTICS.value: Game.action_statistics
    }
    return mapper.get(value)


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
        if user_in in CommandEnum.get_values():
            return get_action(user_in)
        if int(user_in) in EntityEnum.get_values():
            return EntityEnum(int(user_in))
        raise InvalidException()

    @staticmethod
    def get_computer_input():
        return random.choices(list(EntityEnum), k=1)[0]

    @staticmethod
    def calculate_winner(user_input: EntityEnum, computer_input: EntityEnum) -> PlayerEnum:
        winning_matrix = build_winning_matrix()
        inputs = get_inputs(user_input, computer_input)
        winning_index = winning_matrix[computer_input.value][user_input.value]
        winner = get_winner_player(winning_index, inputs)
        Game.update_winner(winner)
        return winner

    @classmethod
    def update_winner(cls, winner: PlayerEnum):
        mapper = {
            PlayerEnum.TIE: "tie_winning",
            PlayerEnum.USER: "user_winning",
            PlayerEnum.COMPUTER: "computer_winning"
        }
        player = mapper.get(winner)
        if player:
            setattr(cls, player, getattr(cls, player) + 1)

    @classmethod
    def action_statistics(cls):
        print(f"""Total Games: {cls.game_number}
        User Wins: {cls.user_winning}
        Computer Wins: {cls.computer_winning}
        Tie Wins: {cls.tie_winning}""")

    @staticmethod
    def action_quit():
        raise GracefulExit()
