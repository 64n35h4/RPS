import pytest
from actions.exceptions import GracefulExit
from actions.game import Game, get_action
from models.commands import CommandEnum


def test_actions_enum():
    actions = CommandEnum
    assert actions.QUIT.value == 'q'
    assert actions.STATISTICS.value == 's'


def test_get_action():
    quit_input = 'q'
    stat_input = 's'
    assert get_action(quit_input) == Game.action_quit
    assert get_action(stat_input) == Game.action_statistics


def test_action_quit():
    with pytest.raises(GracefulExit):
        Game.action_quit()


def test_action_statistics(capsys):
    Game.action_statistics()
    out, err = capsys.readouterr()
    out = list(
        filter(
            lambda f: f, map(
                lambda m: m.strip(), out.split("\n")
            )
        )
    )
    assert out == [
        'Total Games: 0',
        'User Wins: 0',
        'Computer Wins: 0',
        'Tie Wins: 0'
    ]

