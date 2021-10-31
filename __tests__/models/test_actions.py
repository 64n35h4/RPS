import pytest
from actions.exceptions import GracefulExit
from models.actions import ActionEnum, Actions


def test_actions_enum():
    actions = ActionEnum
    assert actions.QUIT.value == 'q'
    assert actions.STATISTICS.value == 's'


def test_get_action():
    quit_input = 'q'
    stat_input = 's'
    assert Actions.get_action(quit_input) == Actions.action_quit
    assert Actions.get_action(stat_input) == Actions.action_statistics


def test_action_quit():
    with pytest.raises(GracefulExit):
        Actions.action_quit()


def test_action_statistics(capsys):
    Actions.action_statistics()
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

