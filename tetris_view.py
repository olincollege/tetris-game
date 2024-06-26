import pygame


class TetrisView:
    """
    A class that represents the user view of the tetris game
    """

    def __init__(self, board):
        self._board = board  # Store the TetrisBoard object

    def draw_board(self):
        """
        Method to visually represent the tetris board and player's score
        """
        # Create game window
        screen = pygame.display.set_mode([700, 800])
        screen.fill((0, 0, 0))

        # Line separating game fron score and controls info
        pygame.draw.line(screen, (255, 0, 0), (401, 0), (401, 800))

        # Score info
        score_font = pygame.font.SysFont("Arial", 36)
        score_label = score_font.render("Score:", True, (255, 255, 255))
        screen.blit(score_label, (500, 400))
        score_num = score_font.render(
            f"{self._board.points}", True, (255, 255, 255)
        )
        screen.blit(score_num, (550, 450))

        # Get the screen height

        # Determine the number of rows to display based on screen height
        # print(rows_to_display, "ROWSROWS")
        # print(self._board._board)

        for i, row in enumerate(self._board.board[4:]):
            for j, square in enumerate(row):
                if square != " ":
                    surf = pygame.Surface((38, 38))
                    surf.fill(square[1])
                    screen.blit(surf, (j * 40 + 1, i * 40 + 1))

        # Game Over Screen
        if self._board.loss is True:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 400, 800))
            game_over_font = pygame.font.SysFont("Arial", 100)
            game_over = game_over_font.render(
                "GAME OVER", True, (255, 255, 255)
            )
            screen.blit(game_over, (110, 200))

        pygame.display.flip()
