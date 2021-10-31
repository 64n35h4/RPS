from actions.exceptions import InvalidException, GracefulExit
from actions.game import Game
from models.entity import EntityEnum


def main():
    print("enter [q]uit/[e]xit to leave")

    game = Game()
    while True:
        game.print_help()
        try:
            user = game.get_user_input()
        except InvalidException:
            print("Wrong Input, please follow instructions")
            continue
        except GracefulExit:
            print("Good-bye")
            break
        if not isinstance(user, EntityEnum):
            continue

        com = game.get_computer_input()
        winner = game.calculate_winner(user, com)
        game.add_game()
        print(f"Game No. {game.game_number} \nUser: {user.name}, Computer: {com.name} \n-> Winner: {winner.name}")


if __name__ == '__main__':
    main()
