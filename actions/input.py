import random

from actions.exceptions import InvalidException
from actions.game import get_action
from models.commands import CommandEnum
from models.entity import EntityEnum


def get_user_input():
    user_in = input("> ")
    if not user_in:
        raise InvalidException()

    if user_in in CommandEnum.get_values():
        return get_action(user_in)
    try:
        user_in = int(user_in)
    except ValueError:
        raise InvalidException()
    if int(user_in) in EntityEnum.get_values():
        return EntityEnum(int(user_in))
    raise InvalidException()


def get_computer_input():
    return random.choices(list(EntityEnum), k=1)[0]
