"""
Tetris Pieces using relative Coordinates
"""

from abc import ABC, abstractmethod


class TetrisPieces(ABC):
    """
    Abstract class for e=tetris pieces

    Attributes:
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

    def __init__(self, board, coordinates):
        self._tetris_board = board
        self.coordinates = coordinates

    @property
    def board(self):
        """
        Docstring here.
        """
        return self._tetris_board

    def fall(self):
        for square in self.coordinates:
            square[0] -= 1

    def move_left(self):
        for square in self.coordinates:
            square[1] -= 1

    def move_right(self):
        for square in self.coordinates:
            square[1] += 1

    @abstractmethod
    def full_piece(self):
        pass

    @abstractmethod
    def rotate_cw(self, orientation):
        pass

    @abstractmethod
    def rotate_ccw(self, orientation):
        pass


# subclasses below
class OPiece(TetrisPieces):
    """
    Docstring here.
    """

    def full_piece(self):
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
        ]


class IPiece(TetrisPieces):
    """
    Docstring here.
    """

    def full_piece(self):
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 2, self.coordinates[1]],
            [self.coordinates[0] + 3, self.coordinates[1]],
        ]

    def rotate_cw(self, orientation):
        if orientation % 2 == 1:
            for i in range(4):
                self.coordinates[i][0] += i
                self.coordinates[i][1] += i

        if orientation % 2 == 0:
            for i in range(4):
                self.coordinates[i][0] -= i
                self.coordinates[i][1] -= i


class JPiece(TetrisPieces):
    """
    Docstring here.
    """

    def full_piece(self):
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1] + 1],
            [self.coordinates[0], self.coordinates[1] + 2],
        ]

    def rotate_cw(self, orientation):
        if orientation == 1:
            self.coordinates[0][0] += 1

            self.coordinates[1][1] -= 1

            self.coordinates[2][0] -= 1

            self.coordinates[3][0] -= 2
            self.coordinates[3][1] += 1

        elif orientation == 2:
            self.coordinates[0][0] += 1
            self.coordinates[0][1] += 1

            self.coordinates[1][0] += 2

            self.coordinates[2][0] += 1
            self.coordinates[2][1] -= 1

            self.coordinates[3][1] -= 2

        elif orientation == 3:
            self.coordinates[0][0] -= 1
            self.coordinates[0][1] += 1

            self.coordinates[1][1] += 2

            self.coordinates[2][0] += 1
            self.coordinates[2][1] += 1

            self.coordinates[3][0] += 2

        elif orientation == 0:
            self.coordinates[0][0] -= 1
            self.coordinates[0][1] -= 2

            self.coordinates[1][0] -= 2
            self.coordinates[1][1] -= 1

            self.coordinates[2][0] -= 1

            self.coordinates[3][1] += 1

    def rotate_ccw(self, orientation):
        if orientation == 3:
            self.coordinates[0][0] += 1
            self.coordinates[0][1] += 2

            self.coordinates[1][0] += 2
            self.coordinates[1][1] += 1

            self.coordinates[2][0] += 1

            self.coordinates[3][1] -= 1

        elif orientation == 2:
            self.coordinates[0][0] += 1
            self.coordinates[0][1] -= 1

            self.coordinates[1][1] -= 2

            self.coordinates[2][0] -= 1
            self.coordinates[2][1] -= 1

            self.coordinates[3][0] -= 2

        elif orientation == 1:
            self.coordinates[0][0] -= 1
            self.coordinates[0][1] -= 1

            self.coordinates[1][0] -= 2

            self.coordinates[2][0] -= 1
            self.coordinates[2][1] += 1

            self.coordinates[3][1] += 2

        elif orientation == 0:
            self.coordinates[0][0] -= 1

            self.coordinates[1][1] += 1

            self.coordinates[2][0] += 1

            self.coordinates[3][0] += 2
            self.coordinates[3][1] -= 1


class LPiece(TetrisPieces):
    """
    Docstring here.
    """

    def full_piece(self):
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 2],
        ]

    def rotate_cw(self, orientation):
        if orientation == 1:
            self.coordinates[0][0] += 1
            self.coordinates[0][1] += 1

            self.coordinates[2][0] -= 1
            self.coordinates[2][1] -= 1

            self.coordinates[3][1] -= 2

        elif orientation == 2:
            self.coordinates[0][0] += 1

            self.coordinates[1][1] += 1

            self.coordinates[2][0] -= 1
            self.coordinates[2][1] += 2

            self.coordinates[3][0] -= 2
            self.coordinates[3][1] += 1

        elif orientation == 3:
            self.coordinates[0][1] -= 2

            self.coordinates[1][0] += 1
            self.coordinates[1][1] -= 1

            self.coordinates[2][0] += 2

            self.coordinates[3][0] += 1
            self.coordinates[3][1] += 1

        elif orientation == 0:
            self.coordinates[0][0] -= 2
            self.coordinates[0][1] += 1

            self.coordinates[1][0] -= 1

            self.coordinates[2][1] -= 1

            self.coordinates[3][0] += 1

    def rotate_ccw(self, orientation):
        if orientation == 3:
            self.coordinates[0][0] += 2
            self.coordinates[0][1] -= 1

            self.coordinates[1][0] += 1

            self.coordinates[2][1] += 1

            self.coordinates[3][0] -= 1

        if orientation == 2:
            self.coordinates[0][1] += 2

            self.coordinates[1][0] -= 1
            self.coordinates[1][1] += 1

            self.coordinates[2][0] -= 2

            self.coordinates[3][0] -= 1
            self.coordinates[3][1] -= 1

        if orientation == 1:
            self.coordinates[0][0] -= 1

            self.coordinates[1][1] -= 1

            self.coordinates[2][0] += 1
            self.coordinates[2][1] -= 2

            self.coordinates[3][0] += 2
            self.coordinates[3][1] -= 1

        if orientation == 0:
            self.coordinates[0][0] -= 1
            self.coordinates[0][1] -= 1

            self.coordinates[2][0] += 1
            self.coordinates[2][1] += 1

            self.coordinates[3][1] += 2


class SPiece(TetrisPieces):
    """
    Docstring here.
    """

    def full_piece(self):
        return [
            self.coordinates,
            [self.coordinates[0], self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 2],
        ]

    def rotate_cw(self, orientation):
        if orientation == 1:
            self.coordinates[0][0] += 2

            self.coordinates[1][0] += 1
            self.coordinates[1][1] += 1

            self.coordinates[3][0] -= 1
            self.coordinates[3][1] += 1

        if orientation == 0:
            self.coordinates[0][0] -= 2

            self.coordinates[1][0] -= 1
            self.coordinates[1][1] -= 1

            self.coordinates[3][0] += 1
            self.coordinates[3][1] -= 1


class ZPiece(TetrisPieces):
    """
    Docstring here
    """

    def full_piece(self):
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0] + 2, self.coordinates[1] + 1],
        ]

    def rotate_cw(self, orientation):
        if orientation == 1:
            self.coordinates[0][1] += 2

            self.coordinates[1][0] += 1

            self.coordinates[2][1] += 1

            self.coordinates[3][0] += 1
            self.coordinates[3][1] -= 1

        if orientation == 0:
            self.coordinates[0][1] -= 2

            self.coordinates[1][0] -= 1

            self.coordinates[2][1] -= 1

            self.coordinates[3][0] -= 1
            self.coordinates[3][1] += 1


class TPiece(TetrisPieces):
    """
    Docstring here.
    """

    def full_piece(self):
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 2, self.coordinates[1]],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
        ]

    def rotate_cw(self, orientation):
        if orientation == 1:
            self.coordinates[0][1] += 2

            self.coordinates[1][0] += 1
            self.coordinates[1][1] += 1

            self.coordinates[2][0] += 2

        if orientation == 2:
            self.coordinates[0][0] += 2

            self.coordinates[1][0] += 1
            self.coordinates[1][1] -= 1

            self.coordinates[2][1] -= 2

        if orientation == 3:
            self.coordinates[0][1] -= 2

            self.coordinates[1][0] -= 1
            self.coordinates[1][1] -= 1

            self.coordinates[2][0] -= 2

        if orientation == 0:
            self.coordinates[0][0] -= 2

            self.coordinates[1][0] -= 1
            self.coordinates[1][1] += 1

            self.coordinates[2][1] += 2

    def rotate_ccw(self, orientation):
        if orientation == 3:
            self.coordinates[0][0] += 2

            self.coordinates[1][0] += 1
            self.coordinates[1][1] -= 1

            self.coordinates[2][1] -= 2

        if orientation == 2:
            self.coordinates[0][1] += 2

            self.coordinates[1][0] += 1
            self.coordinates[1][1] += 1

            self.coordinates[2][0] += 2

        if orientation == 1:
            self.coordinates[0][0] -= 2

            self.coordinates[1][0] -= 1
            self.coordinates[1][1] += 1

            self.coordinates[2][1] += 2

        if orientation == 0:
            self.coordinates[0][1] -= 2

            self.coordinates[1][0] -= 1
            self.coordinates[1][1] -= 1

            self.coordinates[2][0] -= 2
