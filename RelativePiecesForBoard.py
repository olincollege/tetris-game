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

    @abstractmethod
    def full_piece(self):
        """
        Abstract method to set coordinates of full piece
        """
        pass

    @abstractmethod
    def rotate_cw(self, orientation):
        """
        Abstract method to rotate pieces clockwise
        """
        pass

    @abstractmethod
    def rotate_ccw(self, orientation):
        """
        Abstract method to rotate pieces counter-clockwise
        """
        pass

    @abstractmethod
    def color(self):
        """
        Abstract method to set the piece color
        """
        pass


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

    def rotate_cw(self, orientation):
        pass

    def rotate_ccw(self, orientation):
        pass


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
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 2, self.coordinates[1]],
            [self.coordinates[0] + 3, self.coordinates[1]],
        ]

    def rotate_cw(self, orientation):
        """
        Method to rotate piece clockwise.
        """
        if orientation % 2 == 1:
            for i in range(4):
                self.coordinates[i][0] += i
                self.coordinates[i][1] += i

        if orientation % 2 == 0:
            for i in range(4):
                self.coordinates[i][0] -= i
                self.coordinates[i][1] -= i

    def rotate_ccw(self, orientation):
        self.rotate_cw(orientation)


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
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1] + 1],
            [self.coordinates[0], self.coordinates[1] + 2],
        ]

    def rotate_cw(self, orientation):
        """
        Method to rotate piece clockwise.
        """
        if orientation % 4 == 1:
            self.coordinates[0][1] += 1

            self.coordinates[1][0] -= 1

            self.coordinates[2][1] -= 1

            self.coordinates[3][1] -= 2
            self.coordinates[3][0] += 1

        elif orientation % 4 == 2:
            self.coordinates[0][1] += 1
            self.coordinates[0][0] += 1

            self.coordinates[1][1] += 2

            self.coordinates[2][1] += 1
            self.coordinates[2][0] -= 1

            self.coordinates[3][0] -= 2

        elif orientation % 4 == 3:
            self.coordinates[0][1] -= 1
            self.coordinates[0][0] += 1

            self.coordinates[1][0] += 2

            self.coordinates[2][1] += 1
            self.coordinates[2][0] += 1

            self.coordinates[3][1] += 2

        elif orientation % 4 == 0:
            self.coordinates[0][1] -= 1
            self.coordinates[0][0] -= 2

            self.coordinates[1][1] -= 2
            self.coordinates[1][0] -= 1

            self.coordinates[2][1] -= 1

            self.coordinates[3][0] += 1

    def rotate_ccw(self, orientation):
        """
        Method to rotate piece counter-clockwise.
        """
        if orientation % 4 == 3:
            self.coordinates[0][1] += 1
            self.coordinates[0][0] += 2

            self.coordinates[1][1] += 2
            self.coordinates[1][0] += 1

            self.coordinates[2][1] += 1

            self.coordinates[3][0] -= 1

        elif orientation % 4 == 2:
            self.coordinates[0][1] += 1
            self.coordinates[0][0] -= 1

            self.coordinates[1][0] -= 2

            self.coordinates[2][1] -= 1
            self.coordinates[2][0] -= 1

            self.coordinates[3][1] -= 2

        elif orientation % 4 == 1:
            self.coordinates[0][1] -= 1
            self.coordinates[0][0] -= 1

            self.coordinates[1][1] -= 2

            self.coordinates[2][1] -= 1
            self.coordinates[2][0] += 1

            self.coordinates[3][0] += 2

        elif orientation % 4 == 0:
            self.coordinates[0][1] -= 1

            self.coordinates[1][0] += 1

            self.coordinates[2][1] += 1

            self.coordinates[3][1] += 2
            self.coordinates[3][0] -= 1


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
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 2],
        ]

    def rotate_cw(self, orientation):
        """
        Method to rotate piece clockwise.
        """
        if orientation % 4 == 1:
            self.coordinates[0][1] += 1
            self.coordinates[0][0] += 1

            self.coordinates[2][1] -= 1
            self.coordinates[2][0] -= 1

            self.coordinates[3][0] -= 2

        elif orientation % 4 == 2:
            self.coordinates[0][1] += 1

            self.coordinates[1][0] += 1

            self.coordinates[2][1] -= 1
            self.coordinates[2][0] += 2

            self.coordinates[3][1] -= 2
            self.coordinates[3][0] += 1

        elif orientation % 4 == 3:
            self.coordinates[0][0] -= 2

            self.coordinates[1][1] += 1
            self.coordinates[1][0] -= 1

            self.coordinates[2][1] += 2

            self.coordinates[3][1] += 1
            self.coordinates[3][0] += 1

        elif orientation % 4 == 0:
            self.coordinates[0][1] -= 2
            self.coordinates[0][0] += 1

            self.coordinates[1][1] -= 1

            self.coordinates[2][0] -= 1

            self.coordinates[3][1] += 1

    def rotate_ccw(self, orientation):
        """
        Method to rotate piece counter-clockwise.
        """
        if orientation % 4 == 3:
            self.coordinates[0][1] += 2
            self.coordinates[0][0] -= 1

            self.coordinates[1][1] += 1

            self.coordinates[2][0] += 1

            self.coordinates[3][1] -= 1

        if orientation % 4 == 2:
            self.coordinates[0][0] += 2

            self.coordinates[1][1] -= 1
            self.coordinates[1][0] += 1

            self.coordinates[2][1] -= 2

            self.coordinates[3][1] -= 1
            self.coordinates[3][0] -= 1

        if orientation % 4 == 1:
            self.coordinates[0][1] -= 1

            self.coordinates[1][0] -= 1

            self.coordinates[2][1] += 1
            self.coordinates[2][0] -= 2

            self.coordinates[3][1] += 2
            self.coordinates[3][0] -= 1

        if orientation % 4 == 0:
            self.coordinates[0][1] -= 1
            self.coordinates[0][0] -= 1

            self.coordinates[2][1] += 1
            self.coordinates[2][0] += 1

            self.coordinates[3][0] += 2


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
        return [
            self.coordinates,
            [self.coordinates[0], self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0] + 1, self.coordinates[1] + 2],
        ]

    def rotate_cw(self, orientation):
        """
        Method to rotate piece clockwise.
        """
        if orientation % 2 == 1:
            self.coordinates[0][1] += 2

            self.coordinates[1][1] += 1
            self.coordinates[1][0] += 1

            self.coordinates[3][1] -= 1
            self.coordinates[3][0] += 1

        if orientation % 2 == 0:
            self.coordinates[0][1] -= 2

            self.coordinates[1][1] -= 1
            self.coordinates[1][0] -= 1

            self.coordinates[3][1] += 1
            self.coordinates[3][0] -= 1

    def rotate_ccw(self, orientation):
        self.rotate_cw(orientation)


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
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0] + 2, self.coordinates[1] + 1],
        ]

    def rotate_cw(self, orientation):
        """
        Method to rotate piece clockwise.
        """
        if orientation % 2 == 1:
            self.coordinates[0][0] += 2

            self.coordinates[1][1] += 1

            self.coordinates[2][0] += 1

            self.coordinates[3][1] += 1
            self.coordinates[3][0] -= 1

        if orientation % 2 == 0:
            self.coordinates[0][0] -= 2

            self.coordinates[1][1] -= 1

            self.coordinates[2][0] -= 1

            self.coordinates[3][1] -= 1
            self.coordinates[3][0] += 1

    def rotate_ccw(self, orientation):
        self.rotate_cw(orientation)


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
        return [
            self.coordinates,
            [self.coordinates[0] + 1, self.coordinates[1]],
            [self.coordinates[0] + 2, self.coordinates[1]],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
        ]

    def rotate_cw(self, orientation):
        """
        Method to rotate piece clockwise.
        """
        if orientation % 4 == 1:
            self.coordinates[0][0] += 2

            self.coordinates[1][1] += 1
            self.coordinates[1][0] += 1

            self.coordinates[2][1] += 2

        if orientation % 4 == 2:
            self.coordinates[0][1] += 2

            self.coordinates[1][1] += 1
            self.coordinates[1][0] -= 1

            self.coordinates[2][0] -= 2

        if orientation % 4 == 3:
            self.coordinates[0][0] -= 2

            self.coordinates[1][1] -= 1
            self.coordinates[1][0] -= 1

            self.coordinates[2][1] -= 2

        if orientation % 4 == 0:
            self.coordinates[0][1] -= 2

            self.coordinates[1][1] -= 1
            self.coordinates[1][0] += 1

            self.coordinates[2][0] += 2

    def rotate_ccw(self, orientation):
        """
        Method to rotate piece counter-clockwise.
        """
        if orientation % 4 == 3:
            self.coordinates[0][1] += 2

            self.coordinates[1][1] += 1
            self.coordinates[1][0] -= 1

            self.coordinates[2][0] -= 2

        if orientation % 4 == 2:
            self.coordinates[0][0] += 2

            self.coordinates[1][1] += 1
            self.coordinates[1][0] += 1

            self.coordinates[2][1] += 2

        if orientation % 4 == 1:
            self.coordinates[0][1] -= 2

            self.coordinates[1][1] -= 1
            self.coordinates[1][0] += 1

            self.coordinates[2][0] += 2

        if orientation % 4 == 0:
            self.coordinates[0][0] -= 2

            self.coordinates[1][1] -= 1
            self.coordinates[1][0] -= 1

            self.coordinates[2][1] -= 2
