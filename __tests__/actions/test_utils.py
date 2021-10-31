from actions.utils import print_help, get_inputs, get_winner_player
from models.entity import EntityEnum
from models.player import PlayerEnum


def test_print_help(capsys):
    print_help()
    out, err = capsys.readouterr()
    out = list(
        filter(
            lambda f: f, map(
                lambda m: m.strip(), out.split("\n")
            )
        )
    )
    assert out == [
        'q - Quit',
        's - Statistics',
        'Please enter your value:',
        '0 - Rock',
        '1 - Paper',
        '2 - Scissors'
    ]


def test_winner_player():
    user_input = EntityEnum.PAPER
    computer_input = EntityEnum.SCISSORS
    inputs = get_inputs(user_input, computer_input)
    winner = get_winner_player(EntityEnum.SCISSORS.value, inputs)
    assert winner == PlayerEnum.COMPUTER
