import pygame
from pygame.locals import *
from TetrisSemiBoard import TetrisBoard
from TetrisController import TetrisController
from view import TetrisView


def main():
    i = 0
    pygame.init()

    board = TetrisBoard()
    controller = TetrisController(board)
    view = TetrisView(board)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                controller.control_piece()

        if board._active_piece is None:
            board.add_rel_piece()  # Check and add a new piece if none exists
            i += 1

        board.drop_active_piece()
        # if i % 3 == 0:
        #     board.move_active_piece_left()
        # if i % 3 == 1:
        #     board.move_active_piece_right()
        view.draw_board()

        clock.tick(2)

    pygame.quit()


if __name__ == "__main__":
    main()
