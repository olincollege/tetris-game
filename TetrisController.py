# importing all the required libraries
import pygame
from pygame.locals import *
import sys

# initiating pygame library to use it's
# functions
pygame.init()


class TetrisController:

    def __init__(self, board):

        self.board = board

    def control_piece(self):

        orientation = 0
        while True == True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        return self.board.move_active_piece_left()

                    elif event.key == K_RIGHT:
                        return self.board.move_active_piece_right()

                    elif event.key == K_UP:
                        orientation += 1
                        return self.board.rotate_active_piece_cw()

                    elif event.key == K_DOWN:
                        orientation -= 1
                        return self.board.rotate_active_piece_cw()

                    elif event.key == K_SPACE:
                        return self.board.drop_active_piece()

            # elif event.key == K_z:
            #     return self.piece.fall_faster()
