from random import random


def row_convert(data: int, board_size: int) -> tuple:
    """Convert raw slot position to a value to access the board 2d array"""

    row, col = divmod(data, board_size)

    return row, col


def rng(data: float = None) -> float:
    if data != None:
        return data >= random()

    return random()
