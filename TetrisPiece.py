"""
Tetris Pieces
"""

import random
import pygame


class TetrisPiece(ABC):
    """
    Class representing pieces in a tetris game

    Pieces are O, I, J, L, Z, S, T

    The color of each piece is randomly chosen to be red, green,
    blue, cyan, magenta, or yellow
    """

    # Colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (128, 0, 128)
    ORANGE = (255, 127, 0)

    colors = [RED, GREEN, BLUE, CYAN, YELLOW, MAGENTA, ORANGE]

    # Pieces by Relative Coordinates
    O = [[0, 0], [1, 0], [0, 1], [1, 1]]
    I = [[0, 0], [1, 0], [2, 0], [3, 0]]
    J = [[0, 0], [1, 0], [0, 1], [0, 2]]
    L = [[0, 0], [1, 0], [1, 1], [1, 2]]
    S = [[0, 0], [0, 1], [1, 1], [1, 2]]
    Z = [[0, 0], [1, 0], [1, 1], [2, 1]]
    T = [[0, 0], [1, 0], [2, 0], [1, 1]]

    pieces = [O, I, S, Z, L, J, T]

    def __init__(self):
        random_index = random.randint(0, 6)
        self.color = TetrisPiece.colors[random_index]
        self.piece = TetrisPiece.pieces[random_index]
