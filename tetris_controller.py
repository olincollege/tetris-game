"""This file is used to control the active piece in Tetris"""

# importing all the required libraries
import pygame

# initiating pygame library to use it's
# functions
pygame.init()


class TetrisPressedController:
    """
    The controller class to move active pieces
    """

    def __init__(self, board):
        """
        Constructs the controller class

        Args:
            board: (board class): the board to control
        """
        self.board = board
        self._left_thresh = 0
        self._right_thresh = 0
        self._z_thresh = 0
        self._up_lock = False
        self._down_lock = False
        self._drop_lock = False

    def control_piece(self):
        """
        A function to control the piece based on buttons pressed
        """
        presses = pygame.key.get_pressed()
        if presses[pygame.K_LEFT]:
            if self._left_thresh == 0 or (
                self._left_thresh > 5 and self._left_thresh % 2 == 1
            ):
                self.board.move_active_piece_left()
            self._left_thresh += 1
        if presses[pygame.K_RIGHT]:
            if self._right_thresh == 0 or (
                self._right_thresh > 5 and self._right_thresh % 2 == 1
            ):
                self.board.move_active_piece_right()
            self._right_thresh += 1
        if presses[pygame.K_z]:
            if self._z_thresh == 0 or self._z_thresh > 5:
                self.board.drop_active_piece()
                self.board.add_z_points()
            self._z_thresh += 1
        if presses[pygame.K_UP] and self._up_lock is False:
            self.board.rotate_active_piece_cw()
            self._up_lock = True
        if presses[pygame.K_DOWN] and self._down_lock is False:
            self.board.rotate_active_piece_ccw()
            self._down_lock = True
        if presses[pygame.K_SPACE] and self._drop_lock is False:
            self.board.full_drop()
            self._drop_lock = True
        if not presses[pygame.K_LEFT]:
            self._left_thresh = 0
        if not presses[pygame.K_RIGHT]:
            self._right_thresh = 0
        if not presses[pygame.K_z]:
            self._z_thresh = 0
        if not presses[pygame.K_UP]:
            self._up_lock = False
        if not presses[pygame.K_DOWN]:
            self._down_lock = False
        if not presses[pygame.K_SPACE]:
            self._drop_lock = False
