from models.commands import CommandEnum
from models.entity import EntityEnum
from models.player import PlayerEnum


def print_help():
    print(f"{CommandEnum.QUIT.value} - Quit")
    print(f"{CommandEnum.STATISTICS.value} - Statistics")
    print("Please enter your value:")
    print(f"{EntityEnum.ROCK.value} - Rock")
    print(f"{EntityEnum.PAPER.value} - Paper")
    print(f"{EntityEnum.SCISSORS.value} - Scissors")


def get_winner_player(index: int, inputs: dict) -> PlayerEnum:
    for player_type, entity_type in inputs.items():
        if entity_type.value == index:
            return player_type
    return PlayerEnum.TIE


def get_inputs(user_input: EntityEnum, computer_input: EntityEnum) -> dict:
    return {
        PlayerEnum.USER: user_input,
        PlayerEnum.COMPUTER: computer_input
    }
