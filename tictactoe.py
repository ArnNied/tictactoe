from math import floor
from random import uniform

from exception import GameEnd, GameStalemate


class Tictactoe:
    board = []
    board_size = 0
    current_turn = 1

    players = ["player_one", "player_two"]
    player_one = None
    player_two = None

    def __init__(self, board_size: int, player_one: object, player_two: object):
        self.player_one = player_one
        self.player_two = player_two

        self.current_turn = 1
        self.max_turn = board_size * board_size

        self.board_size = board_size
        self.board_assemble()

    def board_assemble(self) -> None:
        """Assemble the board in x by x size with 'x' being self.board_size"""

        for i in range(self.board_size):
            self.board.append([" " for row in range(self.board_size)])

    def board_show(self) -> None:
        """Prints the board to the console"""

        for row in self.board:
            print("|".join(row))

    def slot_empty(self, data: int) -> bool:
        """Check if the chosen slot is occupied or not"""

        if data in self.player_one.slot or data in self.player_two.slot:
            print("Error: Slot is occupied")
            return False

        return True

    def row_convert(self, data: int) -> tuple:
        """Convert raw slot position to a value to access the board 2d array"""

        row, col = divmod(data, self.board_size)

        return row, col

    def line_check(self, line: set) -> bool:
        if len(line) == 1 and (
            self.player_one.symbol in line or self.player_two.symbol in line
        ):
            return True

    def row_win(self) -> bool:
        """Row win check"""

        for row in self.board:
            row = set(row)

            if self.line_check(row):
                return True

    def col_win(self) -> bool:
        """Column win check"""

        for i in range(self.board_size):
            col = set()
            for j in range(self.board_size):
                col.add(self.board[j][i])

            if self.line_check(col):
                return True

    def diagonal_win(self) -> bool:
        """Diagonal win check"""

        tl_br = set()
        for i in range(self.board_size):
            tl_br.add(self.board[i][i])

        tr_bl = set()
        for i in range(-1, -self.board_size - 1, -1):
            tr_bl.add(self.board[abs(i) - 1][i])

        return self.line_check(tl_br) or self.line_check(tr_bl)

    def win_check(self) -> None:
        """Check if win condition is met and end the game"""

        if self.row_win() or self.col_win() or self.diagonal_win():
            raise GameEnd

    def start(self) -> None:
        """Start the game"""

        while self.current_turn <= self.board_size * self.board_size:
            current_player = getattr(
                self, self.players[floor(self.current_turn % len(self.players) - 1)]
            )

            print("")
            self.board_show()
            while True:
                print(current_player.name)
                turn = current_player.turn(self.board, self.board_size)

                if self.slot_empty(turn):
                    current_player.slot.append(turn)

                    row, col = self.row_convert(turn)
                    self.board[row][col] = current_player.symbol

                    self.win_check()
                    break

            self.current_turn += 1

        raise GameStalemate
