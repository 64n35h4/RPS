from actions.exceptions import GracefulExit
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

    @staticmethod
    def action_statistics():
        print(f"""
        Total Games: {Game.game_number}
        User Wins: {Game.user_winning}
        Computer Wins: {Game.computer_winning}
        Tie Wins: {Game.tie_winning}""")

    @staticmethod
    def action_quit():
        raise GracefulExit()
