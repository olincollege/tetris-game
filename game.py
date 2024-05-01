"""A file that combines the tetris board and controller to run Tetris"""

import pygame
from pygame.locals import QUIT, KEYDOWN
from tetris_board import TetrisBoard
from tetris_controller import TetrisPressedController
from view import TetrisView


def main():
    """
    A function to run the game Tetris when the file is run
    """
    i = 0
    pygame.init()
    pygame.display.set_caption("Tetris")
    board = TetrisBoard()
    controller = TetrisPressedController(board)
    view = TetrisView(board)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.control_piece()

        if board.active_piece is None:
            board.add_rel_piece()  # Check and add a new piece if none exists
            i += 1

        board.drop_active_piece()

        for i in range(10):
            controller.control_piece()
            clock.tick(20 + 2 * board.level)
            if i % 1 == 0:
                view.draw_board()

    pygame.quit()


if __name__ == "__main__":
    main()
