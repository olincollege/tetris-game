import pygame


class TetrisView:
    def __init__(self, board):
        self._board = board  # Store the TetrisBoard object

    def draw_board(self):
        screen = pygame.display.set_mode([400, 800])
        screen.fill((0, 0, 0))

        # Get the screen height
        screen_height = screen.get_height()

        # Determine the number of rows to display based on screen height
        rows_to_display = min(len(self._board._board), screen_height // 40)
        # print(rows_to_display, "ROWSROWS")
        # print(self._board._board)

        for i, row in enumerate(self._board._board[4:]):
            for j, square in enumerate(row):
                if square != " ":
                    surf = pygame.Surface((38, 38))
                    surf.fill(square[1])
                    screen.blit(surf, (j * 40 + 1, i * 40 + 1))

        pygame.display.flip()
