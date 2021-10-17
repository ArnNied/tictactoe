from math import floor
from random import uniform

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
    # def opponent_sibling_filled()
    # def sibling_filled(self, board: list, board_size: int) -> list:
    
    def filled_slot(self, board:list, board_size: int) -> list:
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

        random_choice = floor(uniform(0, len(empty_slot)))
        choice = empty_slot[random_choice]

        print(f"> {choice + 1}")

        return choice


class Weak(Computer):
    name = "Weak AI"


class Normal(Computer):
    name = "Normal AI"


class Strong(Computer):
    name = "Strong AI"
