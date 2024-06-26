"""
This is the board class which handles the board and anything within it
(such as movement, dropping, placing pieces, points, the level, etc.)
"""

import random
from tetris_pieces import (
    OPiece,
    IPiece,
    SPiece,
    ZPiece,
    LPiece,
    JPiece,
    TPiece,
)


# pylint: disable-next=consider-using-enumerate
class TetrisBoard:  # pylint: disable=too-many-instance-attributes
    """
    A board for use in the game tetris

    Attributes:
        piece_types: (list) a list of all 7 Tetris piece types as classes
    """

    piece_types = [
        LPiece,
        IPiece,
        SPiece,
        ZPiece,
        TPiece,
        OPiece,
        JPiece,
    ]

    def __init__(self):
        """
        Constructor for TetrisBoard class

        Attributes:
            self._board: (list) a list representing every square in the board
            self._active_piece: (None) if there is an active piece, represents
            it in this attribute as a piece type
        """
        rows = []
        for _ in range(10):
            rows.append(" ")
        board = []
        for _ in range(24):
            board.append(rows[:])  # rows is sliced so that a change to one row
            # ...only affects one row (removes aliasing between rows)
        self._board = board
        self._active_piece = None
        self._loss_row = 4
        self._loss = False
        self._bag = []
        self._points = 0
        self._clears = 0
        self._level = 0

    def add_z_points(self):
        """
        Adds points based on z presses
        """
        self._points = self._points + (2 + self._level / 2)

    def check_all_rows(self):
        """
        Checks all rows to see if they are full, and clears them if they are
        """
        # The tetris board list may be modifed as this runs due to rows
        # clearing, but since rows can not go "up" in the board, this
        # should be fine and there should be no index errors or skips
        clears = 0
        for i in range(len(self._board)):
            if self.check_row(i):
                clears += 1
        if clears == 4:
            self._points = self._points + (600 + self._level * 500)

    def check_row(self, row_num):
        """
        Checks a specific row to see if it is full, and clears it if it is

        Args:
            row_num: (int) the row to check
        Returns:
            True if a row is cleared, false otherwise
        """
        row_is_full = True
        for i in self._board[row_num]:
            if i[0] != "Inactive":
                row_is_full = False
        if row_is_full:
            self.row_clear(row_num)
            return True
        return False

    def row_clear(self, row_num):
        """
        deletes a row from the tetris board then adds another row to the top.

        Args:
            row_num: (int) the row to clear
        """
        del self._board[row_num]
        new_row = []
        for _ in range(10):
            new_row.append(" ")
        self._board.insert(0, new_row)
        self._clears += 1
        self._level = self._clears // 10
        self._points += 100 * (1 + self._level / 10)

    def check_loss(self):
        """
        Checks if the game is lost or not
        """
        for i in self._board[self._loss_row]:
            if i[0] == "Inactive":
                self._loss = True

    def fill_bag(self):
        """
        Fills the board's piece bag with each tetris piece twice
        """
        for _ in range(2):
            for i in self.piece_types:
                self._bag.append(i([2, 5]))

    def add_rel_piece(self):
        """
        Adds a randomly-shaped active piece to the game
        """
        if not self._bag:
            self.fill_bag()
        rando_int = random.randint(0, len(self._bag) - 1)
        self._active_piece = self._bag.pop(rando_int)
        for i in self._active_piece.full_piece():
            self._board[i[0]][i[1]] = ["Active", self._active_piece.color()]

    def update_piece(self):
        """
        Updates the position of an active piece given new coordinates
        """
        # function uses indices because I had trouble replacing active
        # pieces with spaces only iterating through each value
        self.check_loss()
        if self._active_piece is None:
            return
        # pylint: disable-next=consider-using-enumerate
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j][0] == "Active":
                    self._board[i][j] = " "
        for i in self._active_piece.full_piece():
            self._board[i[0]][i[1]] = [
                "Active",
                self._active_piece.color(),
                "Updated",
            ]

    def place_piece(self):
        """
        Places a piece by making all "Active" squares "Inactive"
        """
        for i in self._board:
            for j in i:
                if "Active" in j:
                    j[0] = "Inactive"
        self._active_piece = None
        self.check_all_rows()

    def drop_active_piece(self):
        """
        Lowers an active piece's vertical position by one square
        """
        if self._active_piece is None:
            return
        piece_under_active = False
        try:
            for i in self._active_piece.full_piece():
                if self._board[i[0] + 1][i[1]][0] == "Inactive":
                    piece_under_active = True
            if piece_under_active is False:
                self._active_piece.fall()
                self.update_piece()
            else:
                self.place_piece()
                self.update_piece()
        except IndexError:
            self.place_piece()
            self.update_piece()

    def full_drop(self):
        """
        Fully drops pieces and awards points based on number of squares dropped
        """
        while self._active_piece is not None:
            self.drop_active_piece()
            self._points = self._points + (5 + self._level * 2.5)

    def move_active_piece_left(self):
        """
        Moves an active piece to the left unless it cannot move more left
        """
        if self._active_piece is None:
            return
        piece_to_left = False
        try:
            for i in self._active_piece.full_piece():
                if self._board[i[0]][i[1] - 1][0] == "Inactive" or i[1] == 0:
                    piece_to_left = True
            if piece_to_left is False:
                self._active_piece.move_left()
                self.update_piece()
        except IndexError:
            pass

    def move_active_piece_right(self):
        """
        Moves an active piece to the right unless it cannot move more right
        """
        if self._active_piece is None:
            return
        piece_to_right = False
        try:
            for i in self._active_piece.full_piece():
                if self._board[i[0]][i[1] + 1][0] == "Inactive" or i[1] == 9:
                    piece_to_right = True
            if piece_to_right is False:
                self._active_piece.move_right()
                self.update_piece()
        except IndexError:
            pass

    def rotate_active_piece_cw(self):
        """
        Rotates the active piece clockwise unless it cannot rotate
        """
        if self._active_piece is None:
            return
        can_rotate = True
        self._active_piece.rotate_cw()
        for i in self._active_piece.full_piece():
            if i[0] >= 0 and i[0] < 24 and i[1] >= 0 and i[1] < 10:
                if self._board[i[0]][i[1]][0] != "Inactive":
                    pass
                else:
                    can_rotate = False
            else:
                can_rotate = False
        if can_rotate is False:
            self._active_piece.rotate_ccw()
        self.update_piece()

    def rotate_active_piece_ccw(self):
        """
        Rotates the active piece counterclockwise unless it cannot rotate
        """
        if self._active_piece is None:
            return
        can_rotate = True
        self._active_piece.rotate_ccw()
        for i in self._active_piece.full_piece():
            if i[0] >= 0 and i[0] < 24 and i[1] >= 0 and i[1] < 10:
                if self._board[i[0]][i[1]][0] != "Inactive":
                    pass
                else:
                    can_rotate = False
            else:
                can_rotate = False
        if can_rotate is False:
            self._active_piece.rotate_cw()
        self.update_piece()

    @property
    def board(self):
        """
        property for self._board

        Returns:
            self._board: (list) a list representing the board
        """
        return self._board

    @property
    def points(self):
        """
        property for self._points

        Returns:
            self._points: (int) an int representing points
        """
        return int(self._points)

    @property
    def level(self):
        """
        property for self._level

        Returns:
            self._level: (int) an int representing level
        """
        return self._level

    @property
    def loss(self):
        """
        property for self._loss

        Returns:
            self._loss: (bool) a bool representing if the game is lost
        """
        return self._loss

    @property
    def active_piece(self):
        """
        property for self._active_piece

        Returns:
            self._active_piece: (active piece type) the currently active piece
        """
        return self._active_piece

    def __repr__(self):
        """
        Prints the state of the board

        Return:
            repr_str: (str) a string representation of the board.
        """
        repr_str = ""
        for i in self._board:
            repr_str = repr_str + str(i) + "\n"
        return repr_str
