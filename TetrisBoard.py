# Currently, this code only creates a list of lists and checks to see if
# rows are full. It checks that by seeing if each pixel in a row is a space.
# If at least one square is a space then it is not full.
# import TetrisListPiece
# import TetrisRelativePieces
import TetrisRelativePiecesCopy
import random


class TetrisBoard:
    piece_types = [
        TetrisRelativePiecesCopy.JPiece([3, 2]),
        TetrisRelativePiecesCopy.LPiece([3, 2]),
        TetrisRelativePiecesCopy.TPiece([3, 2]),
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
        active_piece = random.choice(TetrisBoard.piece_types)
        for i in active_piece.full_piece():
            print(i)
            print(self._board[i[1]][i[0]])
            self._board[i[1]][i[0]] = "X"

    #    def add_piece(self):
    #        ActivePiece = random.choice(TetrisBoard.piece_types)

    # def add_piece(self):
    #        ActivePiece = TetrisListPiece.TetrisPiece()
    #        square_dim = len(ActivePiece.piece[0])
    #        for i in range(square_dim):
    #            base = [" " for j in range(10)]
    #            for
    #            base[3 : 3 + square_dim] = (
    #                ActivePiece.piece[0][i],
    #                ActivePiece.color,
    #                "active",
    #            )
    #            self._board[i] = base

    # def check_fallen_piece(self):
    # Should run before a piece falls a space

    def __repr__(self):
        return str(self._board)
