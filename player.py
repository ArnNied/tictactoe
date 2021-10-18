from math import floor
from random import randrange

from utils import row_convert


class Player:
    name = "Player"

    def __init__(self, symbol: str, name: str = None):
        if name != None:
            self.name = name

        self.symbol = symbol
        self.slot = []


class Human(Player):
    def valid_slot(self, turn: int, board_size: int) -> bool:
        """Check if the chosen slot is our of range or not"""

        if turn < 0 or turn > board_size ** 2:
            print("Error: Out of range")

            return False

        return True

    def turn(self, board: list, board_size: int) -> int:
        while True:
            turn = int(input("> ")) - 1

            if self.valid_slot(turn, board_size):
                break

        return turn


class Computer(Player):
    def neighbour_of_filled(self, board: list, board_size: int) -> list:
        filled_slot = self.filled_slot(board, board_size)
        board_full_size = board_size * board_size

        neighbour = set()
        for filled in filled_slot:
            y_up = filled - board_size
            y_up_left = y_up - 1
            y_up_right = y_up + 1

            y_down = filled + board_size
            y_down_left = y_down - 1
            y_down_right = y_down + 1

            if y_up >= 0:
                neighbour.add(y_up)

            if y_up_left >= 0 and row_convert(y_up, board_size)[1] - 1 >= 0:
                neighbour.add(y_up_left)

            if y_up_right >= 0 and row_convert(y_up, board_size)[1] + 1 < board_size:
                neighbour.add(y_up_right)

            if y_down < board_full_size:
                neighbour.add(y_down)

            if (
                y_down_left < board_full_size
                and row_convert(y_down, board_size)[1] - 1 >= 0
            ):
                neighbour.add(y_down_left)

            if (
                y_down_right < board_full_size
                and row_convert(y_down, board_size)[1] + 1 < board_size
            ):
                neighbour.add(y_down_right)

            x = filled
            x_left = filled - 1
            x_right = filled + 1

            if x_left >= 0 and row_convert(x, board_size)[1] - 1 >= 0:
                neighbour.add(x_left)

            if (
                x_right < board_full_size
                and row_convert(x, board_size)[1] + 1 < board_size
            ):
                neighbour.add(x_left)

        collide = neighbour & set(filled_slot)
        for i in collide:
            neighbour.remove(i)

        return neighbour

    def filled_slot(self, board: list, board_size: int) -> list:
        """Return all filled slot on the board"""

        filled_slot = list()
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] != " ":
                    filled_slot.append(row * board_size + col)

        return filled_slot

    def empty_slot(self, board: list, board_size: int) -> list:
        """Return all empty slot on the board"""

        empty_slot = list()
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == " ":
                    empty_slot.append(row * board_size + col)

        return empty_slot

    def turn(self, board: list, board_size: int) -> int:
        empty_slot = self.empty_slot(board, board_size)

        random_choice = randrange(len(empty_slot))
        choice = empty_slot[random_choice]

        self.neighbour_of_filled(board, board_size)

        print(f"> {choice + 1}")

        return choice


class Weak(Computer):
    name = "Weak AI"


class Normal(Computer):
    name = "Normal AI"


class Strong(Computer):
    name = "Strong AI"
