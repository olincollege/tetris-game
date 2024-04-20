# importing all the required libraries
import pygame
from pygame.locals import *
from sys import exit

# initiating pygame library to use it's
# functions
pygame.init()


class TetrisController:

    def __init__(self, piece):

        self.piece = piece

    def control_piece(self):

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.piece.move_left()
            elif event.key == K_RIGHT:
                self.piece.move_right()
            elif event.key == K_UP:
                self.piece.rotate_cw()
            elif event.key == K_DOWN:
                self.piece.rotate_ccw()
            elif event.key == K_SPACE:
                self.piece.drop()
            elif event.key == K_z:
                self.piece.fall_faster()
