from Display_Game import DisplayGame
from Take_Turn import take_turn


def main():
    game = DisplayGame()
    take_turn(game)
    take_turn(game)
    take_turn(game)
    take_turn(game)


if __name__ == '__main__':
    main()
