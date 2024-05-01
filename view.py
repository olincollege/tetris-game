import pygame


class TetrisView:
    def __init__(self, board):
        self._board = board  # Store the TetrisBoard object

    def draw_board(self):
        # Create game window
        screen = pygame.display.set_mode([700, 800])
        screen.fill((0, 0, 0))

        # Line separating game fron score and controls info
        pygame.draw.line(screen, (255, 0, 0), (401, 0), (401, 800))

        # Score info
        font = pygame.font.SysFont("Arial", 36)
        txtsurf = font.render("Score:", True, (255, 255, 255))
        screen.blit(txtsurf, (500, 400))
        score_num = font.render(f"{self._board.points}", True, (255, 255, 255))
        screen.blit(score_num, (550, 450))

        # Get the screen height
        screen_height = screen.get_height()

        # Determine the number of rows to display based on screen height
        rows_to_display = min(len(self._board.board), screen_height // 40)
        # print(rows_to_display, "ROWSROWS")
        # print(self._board._board)

        for i, row in enumerate(self._board.board[4:]):
            for j, square in enumerate(row):
                if square != " ":
                    surf = pygame.Surface((38, 38))
                    surf.fill(square[1])
                    screen.blit(surf, (j * 40 + 1, i * 40 + 1))

        pygame.display.flip()
