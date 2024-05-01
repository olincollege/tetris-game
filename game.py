import pygame
from pygame.locals import *
from TetrisSemiBoard import TetrisBoard
from TetrisController import TetrisController
from TetrisPressedController import TetrisPressedController
from view import TetrisView


def main():
    i = 0
    pygame.init()

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

        if board._active_piece is None:
            board.add_rel_piece()  # Check and add a new piece if none exists
            i += 1

        board.drop_active_piece()
        # if i % 3 == 0:
        #     board.move_active_piece_left()
        # if i % 3 == 1:
        #     board.move_active_piece_right()
        for i in range(10):
            controller.control_piece()
            clock.tick(20 + 2 * board.level)
            if i % 1 == 0:
                view.draw_board()
        print(board.points)

    pygame.quit()


if __name__ == "__main__":
    main()
