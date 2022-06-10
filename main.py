import utils

from exception import GameEnd, GameStalemate
from tictactoe import Tictactoe
from player import Player

if __name__ == "__main__":
    while True:
        try:
            board_size = int(input("Board size? "))
        except ValueError:
            print("ValueError: Invalid board size")
        else:
            break

    game = Tictactoe(board_size, Player("X", "Player 1"), Player("O", "Player 2"))

    try:
        game.start()
    except GameEnd:
        print("\nGame finished")
    except GameStalemate:
        print("\nGame stalemate")
    finally:
        utils.clear_stdout()
        game.board.show()
        print("FINAL BOARD STATE")

    game.history.start()
