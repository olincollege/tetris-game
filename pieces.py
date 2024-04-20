"""
Tetris Pieces
"""

import random
import pygame


class TetrisPiece:
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

    # Pieces and their rotations
    O = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]

    I = [
        # vertical
        [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
        # horizontal
        [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    ]

    J = [
        # start
        [[0, 1, 0], [0, 1, 0], [1, 1, 0]],
        # rot 1 cw
        [[0, 0, 0], [1, 0, 0], [1, 1, 1]],
        # rot 2 cw
        [[1, 1, 0], [1, 0, 0], [1, 0, 0]],
        # rot 3 cw
        [[1, 1, 1], [0, 0, 1], [0, 0, 0]],
    ]

    L = [  # start
        [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
        # rot 1 cw
        [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
        # rot 2 cw
        [[0, 1, 1], [0, 0, 1], [0, 0, 1]],
        # rot 3 cw
        [[0, 0, 0], [0, 0, 1], [1, 1, 1]],
    ]

    S = [  # start
        [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
        # rot 1 cw
        [[0, 1, 0], [0, 1, 1], [0, 0, 1]],
    ]

    Z = [  # start
        [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
        # rot 1 cw
        [[0, 0, 1], [0, 1, 1], [0, 1, 0]],
    ]

    T = [  # start
        [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
        # rot 1 cw
        [[0, 0, 1], [0, 1, 1], [0, 0, 1]],
        # rot 2 cw
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
        # rot 3 cw
        [[1, 0, 0], [1, 1, 0], [1, 0, 0]],
    ]

    pieces = [O, I, S, Z, L, J, T]

    def __init__(self):
        self.color = random.choice(TetrisPiece.colors)
        self.piece = random.choice(TetrisPiece.pieces)
