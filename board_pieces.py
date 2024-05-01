"""
Tetris Pieces using relative Coordinates
"""

from abc import ABC, abstractmethod


class TetrisPieces(ABC):
    """
    Abstract class for tetris pieces

    Attributes:
        RED: tuple representing RGB values for red
        GREEN: tuple representing RGB values for green
        BLUE: tuple representing RGB values for blue
        CYAN: tuple representing RGB values for cyan
        YELLOW: tuple representing RGB values for yellow
        MAGENTA: tuple representing RGB values for magenta
        ORANGE: tuple representing RGB values for orange
    """

    # Colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (128, 0, 128)
    ORANGE = (255, 127, 0)

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self._orientation = 0

    def fall(self):
        """
        Method to handle the pieces falling
        """
        self.coordinates[0] += 1

    def move_left(self):
        """
        Method to move the piece to the left
        """
        try:
            self.coordinates[1] -= 1
        except IndexError:
            pass

    def move_right(self):
        """
        Method to move the piece to the right
        """
        try:
            self.coordinates[1] += 1
        except IndexError:
            pass

    @property
    def dict_3x3(self):
        """Defines a name for all possible coordinates in a 3x3 square

        Return:
            A dictionary mapping names of each square to their coordinates
        """
        return {
            "top_left": [self.coordinates[0] - 1, self.coordinates[1] - 1],
            "top_middle": [self.coordinates[0] - 1, self.coordinates[1]],
            "top_right": [self.coordinates[0] - 1, self.coordinates[1] + 1],
            "middle_left": [self.coordinates[0], self.coordinates[1] - 1],
            "middle_middle": [self.coordinates[0], self.coordinates[1]],
            "middle_right": [self.coordinates[0], self.coordinates[1] + 1],
            "bottom_left": [self.coordinates[0] + 1, self.coordinates[1] - 1],
            "bottom_middle": [self.coordinates[0] + 1, self.coordinates[1]],
            "bottom_right": [self.coordinates[0] + 1, self.coordinates[1] + 1],
        }

    @abstractmethod
    def full_piece(self):
        """
        Abstract method to set coordinates of full piece
        """
        pass  # pylint: disable=unnecessary-pass

    def rotate_cw(self):
        """
        Abstract method to rotate pieces clockwise
        """
        self._orientation = (self._orientation + 1) % 4

    def rotate_ccw(self):
        """
        Abstract method to rotate pieces counter-clockwise
        """
        self._orientation = (self._orientation - 1) % 4

    @abstractmethod
    def color(self):
        """
        Abstract method to set the piece color
        """
        pass  # pylint: disable=unnecessary-pass


# subclasses below
class OPiece(TetrisPieces):
    """
    Subclass of the Tetris Pieces class. Makes an O shaped piece.
    """

    def color(self):
        """
        Sets color of piece to yellow.

        Returns:
            a tuple representing the RBG color value
        """
        return TetrisPieces.YELLOW

    def full_piece(self):
        """
        Sets the coordinate of each block in the piece.

        Returns:
            a list of 4 lists, containing the coordinates of each block
            in the piece
        """
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
        ]


class IPiece(TetrisPieces):
    """
    Subclass of the Tetris Pieces class. Makes an I shaped piece.
    """

    def color(self):
        """
        Method that sets color of piece to cyan.

        Returns:
            a tuple representing the RBG color value
        """
        return TetrisPieces.CYAN

    def full_piece(self):
        """
        Method that sets the coordinate of each block in the piece based
        relative to the block at coordinates self.coordinates.

        Returns:
            a list of 4 lists, containing the coordinates of each block
            in the piece
        """
        if self._orientation == 0:
            return [
                [self.coordinates[0] - 1, self.coordinates[1] - 1],
                [self.coordinates[0] - 1, self.coordinates[1]],
                [self.coordinates[0] - 1, self.coordinates[1] + 1],
                [self.coordinates[0] - 1, self.coordinates[1] + 2],
            ]
        if self._orientation == 1:
            return [
                [self.coordinates[0] - 2, self.coordinates[1] - 1],
                [self.coordinates[0] - 1, self.coordinates[1] - 1],
                [self.coordinates[0], self.coordinates[1] - 1],
                [self.coordinates[0] + 1, self.coordinates[1] - 1],
            ]
        if self._orientation == 2:
            return [
                [self.coordinates[0] + 1, self.coordinates[1] + 1],
                [self.coordinates[0] + 1, self.coordinates[1]],
                [self.coordinates[0] + 1, self.coordinates[1] - 1],
                [self.coordinates[0] + 1, self.coordinates[1] - 2],
            ]
        return [
            [self.coordinates[0] - 1, self.coordinates[1] + 1],
            [self.coordinates[0], self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0] + 2, self.coordinates[1] + 1],
        ]


class JPiece(TetrisPieces):
    """
    Subclass of the Tetris Pieces class. Makes an J shaped piece.
    """

    def color(self):
        """
        Method that sets color of piece to orange.

        Returns:
            a tuple representing the RBG color value
        """
        return TetrisPieces.ORANGE

    def full_piece(self):
        """
        Method that sets the coordinate of each block in the piece based
        relative to the block at coordinates self.coordinates.

        Returns:
            a list of 4 lists, containing the coordinates of each block
            in the piece
        """

        if self._orientation == 0:
            return [
                self.dict_3x3["top_left"],
                self.dict_3x3["middle_left"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_right"],
            ]
        if self._orientation == 1:
            return [
                self.dict_3x3["top_right"],
                self.dict_3x3["top_middle"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["bottom_middle"],
            ]
        if self._orientation == 2:
            return [
                self.dict_3x3["bottom_right"],
                self.dict_3x3["middle_right"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_left"],
            ]
        return [
            self.dict_3x3["bottom_left"],
            self.dict_3x3["bottom_middle"],
            self.dict_3x3["middle_middle"],
            self.dict_3x3["top_middle"],
        ]


class LPiece(TetrisPieces):
    """
    Subclass of the Tetris Pieces class. Makes an L shaped piece.
    """

    def color(self):
        """
        Method that sets color of piece to blue.

        Returns:
            a tuple representing the RBG color value
        """
        return TetrisPieces.BLUE

    def full_piece(self):
        """
        Method that sets the coordinate of each block in the piece based
        relative to the block at coordinates self.coordinates.

        Returns:
            a list of 4 lists, containing the coordinates of each block
            in the piece
        """
        if self._orientation == 0:
            return [
                self.dict_3x3["top_right"],
                self.dict_3x3["middle_right"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_left"],
            ]
        if self._orientation == 1:
            return [
                self.dict_3x3["bottom_right"],
                self.dict_3x3["bottom_middle"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["top_middle"],
            ]
        if self._orientation == 2:
            return [
                self.dict_3x3["bottom_left"],
                self.dict_3x3["middle_left"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_right"],
            ]
        return [
            self.dict_3x3["top_left"],
            self.dict_3x3["top_middle"],
            self.dict_3x3["middle_middle"],
            self.dict_3x3["bottom_middle"],
        ]


class SPiece(TetrisPieces):
    """
    Subclass of the Tetris Pieces class. Makes an S shaped piece.
    """

    def color(self):
        """
        Method that sets color of piece to green.

        Returns:
            a tuple representing the RBG color value
        """
        return TetrisPieces.GREEN

    def full_piece(self):
        """
        Method that sets the coordinate of each block in the piece based
        relative to the block at coordinates self.coordinates.

        Returns:
            a list of 4 lists, containing the coordinates of each block
            in the piece
        """
        if self._orientation == 0:
            return [
                self.dict_3x3["top_right"],
                self.dict_3x3["top_middle"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_left"],
            ]
        if self._orientation == 1:
            return [
                self.dict_3x3["bottom_right"],
                self.dict_3x3["middle_right"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["top_middle"],
            ]
        if self._orientation == 2:
            return [
                self.dict_3x3["bottom_left"],
                self.dict_3x3["bottom_middle"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_right"],
            ]
        return [
            self.dict_3x3["top_left"],
            self.dict_3x3["middle_left"],
            self.dict_3x3["middle_middle"],
            self.dict_3x3["bottom_middle"],
        ]


class ZPiece(TetrisPieces):
    """
    Subclass of the Tetris Pieces class. Makes an Z shaped piece.
    """

    def color(self):
        """
        Method that sets color of piece to red.

        Returns:
            a tuple representing the RBG color value
        """
        return TetrisPieces.RED

    def full_piece(self):
        """
        Method that sets the coordinate of each block in the piece based
        relative to the block at coordinates self.coordinates.

        Returns:
            a list of 4 lists, containing the coordinates of each block
            in the piece
        """
        if self._orientation == 0:
            return [
                self.dict_3x3["top_left"],
                self.dict_3x3["top_middle"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_right"],
            ]
        if self._orientation == 1:
            return [
                self.dict_3x3["top_right"],
                self.dict_3x3["middle_right"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["bottom_middle"],
            ]
        if self._orientation == 2:
            return [
                self.dict_3x3["bottom_right"],
                self.dict_3x3["bottom_middle"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_left"],
            ]
        return [
            self.dict_3x3["bottom_left"],
            self.dict_3x3["middle_left"],
            self.dict_3x3["middle_middle"],
            self.dict_3x3["top_middle"],
        ]


class TPiece(TetrisPieces):
    """
    Subclass of the Tetris Pieces class. Makes an Z shaped piece.
    """

    def color(self):
        """
        Method that sets color of piece to magenta.

        Returns:
            a tuple representing the RBG color value
        """
        return TetrisPieces.MAGENTA

    def full_piece(self):
        """
        Method that sets the coordinate of each block in the piece based
        relative to the block at coordinates self.coordinates.

        Returns:
            a list of 4 lists, containing the coordinates of each block
            in the piece
        """
        if self._orientation == 0:
            return [
                self.dict_3x3["middle_left"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_right"],
                self.dict_3x3["top_middle"],
            ]
        if self._orientation == 1:
            return [
                self.dict_3x3["top_middle"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["bottom_middle"],
                self.dict_3x3["middle_right"],
            ]
        if self._orientation == 2:
            return [
                self.dict_3x3["middle_left"],
                self.dict_3x3["middle_middle"],
                self.dict_3x3["middle_right"],
                self.dict_3x3["bottom_middle"],
            ]
        return [
            self.dict_3x3["top_middle"],
            self.dict_3x3["middle_middle"],
            self.dict_3x3["bottom_middle"],
            self.dict_3x3["middle_left"],
        ]
