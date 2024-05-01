# Currently, this code only creates a list of lists and checks to see if
# rows are full. It checks that by seeing if each pixel in a row is a space.
# If at least one square is a space then it is not full.
# import TetrisListPiece
# import TetrisRelativePieces
import SemiRelativePiecesForBoard
import random


class TetrisBoard:
    piece_types = [
        SemiRelativePiecesForBoard.LPiece([2, 3]),
        SemiRelativePiecesForBoard.IPiece([2, 3]),
        SemiRelativePiecesForBoard.SPiece([2, 3]),
        SemiRelativePiecesForBoard.ZPiece([2, 3]),
        SemiRelativePiecesForBoard.TPiece([2, 3]),
        SemiRelativePiecesForBoard.OPiece([2, 3]),
        SemiRelativePiecesForBoard.JPiece([2, 3]),
    ]

    def __init__(self):
        rows = []
        for _ in range(10):
            rows.append(" ")
        board = []
        for _ in range(24):
            board.append(rows[:])  # rows is sliced so that a change to one row
            # ...only affects one row
        self._board = board
        self._active_piece = None
        self._unseen_row = 4

    def check_all_rows(self):
        """
        Checks all rows to see if they are full, and clears them if they are
        """
        # The tetris board list may be modifed as this runs due to rows
        # clearing, but since rows can not go "up" in the board, this
        # should be fine and there should be no index errors or skips
        for i in range(len(self._board)):
            self.check_row(i)

    def check_row(self, row_num):
        """
        Checks a specific row to see if it is full, and clears it if it is
        """
        row_is_full = True
        for i, pixel in enumerate(self._board[row_num]):
            if pixel == " " and i != 0 and i != 11:
                row_is_full = False
        if row_is_full is True:
            self.row_clear(row_num)

    def row_clear(self, row_num):
        """
        deletes a row from the tetris board then adds another row to the top.
        """
        del self._board[row_num]
        self._board.insert(0, self._board[0])  ###This may make each row equal
        ###...to each other later on which could cause issues

    def add_rel_piece(self):
        rando_int = random.randint(0, 6)
        #        self._active_piece = random.choice(TetrisBoard.piece_types)
        self._active_piece = self.piece_types[rando_int]
        # print(rando_int)
        for i in self._active_piece.full_piece():
            self._board[i[0]][i[1]] = ["Active", self._active_piece.color()]

    def update_piece(self):
        # function uses indices because I had trouble replacing active
        # pieces with spaces only iterating through each value
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

    def has_active_piece(self):
        """
        Check if there is an active piece on the board.
        Returns:
            bool: True if there is an active piece, False otherwise.
        """
        return self._active_piece is not None

    def add_new_piece_if_none(self):
        """
        Add a new active piece to the board if there is no active piece.
        """
        if not self.has_active_piece():
            self.add_rel_piece()

    def place_piece(self):
        for i in self._board:
            for j in i:
                if "Active" in j:
                    j[0] = "Inactive"

    def drop_active_piece(self):
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
        except IndexError:
            self.place_piece()

    def move_active_piece_left(self):
        piece_to_left = False
        try:
            for i in self._active_piece.full_piece():
                if self._board[i[0]][i[1] - 1][0] == "Inactive" or i[1] == 0:
                    piece_to_left = True
            if piece_to_left is False:
                print(self._active_piece.full_piece())
                self._active_piece.move_left()
                print(self._active_piece.full_piece())
                self.update_piece()
        except IndexError:
            pass

    def move_active_piece_right(self):
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
        return self._board

    def __repr__(self):
        repr_str = ""
        for i in self._board:
            repr_str = repr_str + str(i) + "\n"
        return repr_str
