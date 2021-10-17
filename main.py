from exception import GameEnd, GameStalemate
from menu import Menu
from tictactoe import Tictactoe


if __name__ == "__main__":
    board_size, player_one, player_two = Menu().start()
    game = Tictactoe(board_size, player_one, player_two)
    try:
        game.start()
    except GameEnd:
        print("\nGame finished")
    except GameStalemate:
        print("\nGame stalemate")
    finally:
        game.board_show()
        print("FINAL BOARD STATE")
