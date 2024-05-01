import pygame
from pygame.locals import QUIT
from TetrisSemiBoard import TetrisBoard
from TetrisController import TetrisController
from view import TetrisView


def main():
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

        board.add_new_piece_if_none()  # Check and add a new piece if none exists

        controller.control_piece()
        board.drop_active_piece()
        board.move_active_piece_right()
        view.draw_board()

        clock.tick(1)

    pygame.quit()


if __name__ == "__main__":
    main()
