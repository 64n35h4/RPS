from actions.exceptions import GracefulExit
from actions.game import Game
from models import TEntity


class ActionEnum(TEntity):
    QUIT = 'q'
    STATISTICS = 's'

    @staticmethod
    def get_values():
        return [x.value for x in ActionEnum]


class Actions:
    @staticmethod
    def get_action(value):
        mapper = {
            ActionEnum.QUIT.value: Actions.action_quit,
            ActionEnum.STATISTICS.value: Actions.action_statistics
        }
        return mapper.get(value)

    @staticmethod
    def action_quit():
        raise GracefulExit()

    @staticmethod
    def action_statistics():
        print(Game.game_number)
