from models.actions import ActionEnum
from models.entity import EntityEnum
from models.player import PlayerEnum


def print_help():
    print(f"{ActionEnum.QUIT.value} - Quit")
    print(f"{ActionEnum.STATISTICS.value} - Statistics")
    print("Please enter your value:")
    print(f"{EntityEnum.ROCK.value} - Rock")
    print(f"{EntityEnum.PAPER.value} - Paper")
    print(f"{EntityEnum.SCISSORS.value} - Scissors")


def get_winner_player(index: int, inputs) -> PlayerEnum:
    for k, v in inputs.items():
        if v.value == index:
            return k
    return PlayerEnum.TIE
