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

        print(board._active_piece)
        if board._active_piece is None:
            board.add_rel_piece()  # Check and add a new piece if none exists

        controller.control_piece()
        board.drop_active_piece()
        board.move_active_piece_left()
        view.draw_board()

        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    main()
