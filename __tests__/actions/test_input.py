from actions.input import get_computer_input
from models.entity import EntityEnum


def test_get_computer_input():
    computer_input = get_computer_input()
    assert isinstance(computer_input, EntityEnum)
