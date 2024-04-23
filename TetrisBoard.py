# Currently, this code only creates a list of lists and checks to see if
# rows are full. It checks that by seeing if each pixel in a row is a space.
# If at least one square is a space then it is not full.
import TetrisListPiece


class TetrisBoard:
    def __init__(self):
        rows = []
        for _ in range(12):
            rows.append(" ")
        board = []
        for _ in range(24):
            board.append(rows)
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

    def add_piece(self):
        ActivePiece = TetrisListPiece.TetrisPiece()
        print(ActivePiece.piece[0])
        square_dim = len(ActivePiece.piece[0])
        for i in range(square_dim):
            base = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            base[4 : 4 + square_dim] = ActivePiece.piece[0][i]
            self._board[i] = base

    def __repr__(self):
        return str(self._board)
