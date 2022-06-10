import copy
import utils
from history import History

from exception import GameEnd, GameStalemate
from queue import Queue


class Board:
    def __init__(self, size):
        self.value = []
        self.size = size

        for i in range(self.size):
            self.value.append([" " for row in range(self.size)])

    def show(self):
        for row in self.value:
            print("|".join(row))


class Tictactoe:
    def __init__(self, board_size, *players):
        self.current_turn = 1
        self.board = Board(board_size)

        self.history = History(board_size**2)

        self.players = Queue(len(players))
        self.players.enqueue(*players)

    def valid_slot(self, slot):
        """Check if the chosen slot is occupied or not and if slot not out of bound"""

        if slot < 0 or slot >= self.board.size**2:
            print("Error: Invalid slot")
            return False

        row, col = divmod(slot, self.board.size)

        if self.board.value[row][col] != " ":
            print("Error: Slot is occupied")
            return False

        return True

    def line_check(self, line, symbol):
        """Check if only one symbol exist on a given line."""

        if len(line) == 1 and symbol in line:
            return True

    def row_win(self, symbol):
        """Row win check."""

        for row in self.board.value:
            row = set(row)

            return self.line_check(row, symbol)

    def col_win(self, symbol):
        """Column win check."""

        for i in range(self.board.size):
            col = set()
            for j in range(self.board.size):
                col.add(self.board.value[j][i])

            return self.line_check(col, symbol)

    def diagonal_win(self, symbol):
        """Diagonal win check."""

        tl_br = set()
        tr_bl = set()
        for i in range(self.board.size):
            tl_br.add(self.board.value[i][i])
            tr_bl.add(self.board.value[i][0 - 1 - i])

        return self.line_check(tl_br, symbol) or self.line_check(tr_bl, symbol)

    def win_check(self, symbol):
        """Check if win condition is met and end the game."""

        if self.row_win(symbol) or self.col_win(symbol) or self.diagonal_win(symbol):
            raise GameEnd

    def start(self):
        """Start the game."""

        while self.current_turn <= self.board.size**2:
            utils.clear_stdout()

            current_player = self.players.dequeue()
            self.players.enqueue(current_player)

            self.board.show()
            print(f"Turn: {self.current_turn}")

            valid_turn = False
            while not valid_turn:
                while True:
                    try:
                        chosen_slot = (
                            int(input(f"{current_player.name}({current_player.symbol}): ")) - 1
                        )
                    except ValueError:
                        print("Error: Invalid slot")
                    else:
                        break

                valid_turn = self.valid_slot(chosen_slot)

            row, col = divmod(chosen_slot, self.board.size)
            self.board.value[row][col] = current_player.symbol

            self.history.do(
                {
                    "board": copy.deepcopy(self.board),
                    "turn": self.current_turn,
                    "slot": chosen_slot + 1,
                    "player": current_player,
                }
            )

            self.win_check(current_player.symbol)
            self.current_turn += 1

        raise GameStalemate
