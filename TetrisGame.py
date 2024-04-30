import TetrisBoard
import TetrisView
import pygame

pygame.init()

game_board = TetrisBoard.TetrisBoard()
print(game_board)
game_board.add_rel_piece()
print(game_board)
game_board.drop_active_piece()
print(game_board)

for i in range(30):
    game_board.drop_active_piece()
    print(game_board)

game_board.add_rel_piece()
print(game_board)
game_board.drop_active_piece()
game_board.move_active_piece_right()
game_board.move_active_piece_right()
game_board.move_active_piece_right()
print(game_board)

TetrisView.TetrisView(game_board)
