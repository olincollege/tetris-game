import pygame
from pygame.locals import QUIT

pygame.init()


class TetrisView:

    def __init__(self, board):
        self._board = board

    def draw_board(self):

        screen = pygame.display.set_mode([500, 1000])
        # this might have to be moved to the main file

        screen.fill((0, 0, 0))

        for i, row in enumerate(self._board):
            for j, square in enumerate(row):
                if square != " ":
                    surf = pygame.Surface((50, 50))
                    surf.fill(square[1])
                    screen.blit(surf, (j * 50, i * 50))

        pygame.display.flip()
