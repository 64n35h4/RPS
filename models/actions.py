from actions.exceptions import GracefulExit
from models import TEntity


class ActionEnum(TEntity):
    QUIT = 'q'
    STATISTICS = 's'


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
        from actions.game import Game
        print(f"""
        Total Games: {Game.game_number}\n
        User Wins: {Game.user_winning}\n
        Computer Wins: {Game.computer_winning}\n
        Tie Wins: {Game.tie_winning}\n
        """)
