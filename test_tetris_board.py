from tetris_board import TetrisBoard
import pytest


@pytest.fixture
def board():
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return TetrisBoard()


# check that an empty row is considered empty
def test_check_row(board):
    """
    Checks that the check_row method of the TetrisBoard class
    """

    assert board.check_row(4) is False


# def test__repr__(capsys, board):

#     print(board)
#     captured = capsys.readouterr()

#     assert (
#         captured.out
