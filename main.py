from actions.exceptions import InvalidException, GracefulExit
from actions.game import Game
from models.entity import EntityEnum


def main():
    print("enter [q]uit/[e]xit to leave")

    while True:
        game = Game()
        try:
            user = game.get_user_input()
        except InvalidException:
            print("wrong")
            continue
        except GracefulExit:
            print("bye")
            break
        if user is not EntityEnum:
            continue

        com = game.get_computer_input()
        winner = game.calculate_winner(user, com)
        print(f"Game No. {game.game_number} \nUser: {user.name}, Computer: {com.name} \n-> Winner: {winner.name}")


if __name__ == '__main__':
    main()
