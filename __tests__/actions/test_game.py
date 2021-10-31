from actions.game import Game
from models.entity import EntityEnum


def test_get_computer_input():
    computer_input = Game.get_computer_input()
    assert isinstance(computer_input, EntityEnum)