import pygame
import TetrisSemiBoard
import TetrisView

pygame.init()

game_board = TetrisSemiBoard.TetrisBoard()
game_board.add_rel_piece()
print(game_board)
game_board.rotate_active_piece_cw()
print(game_board)
# game_board.drop_active_piece()
# print(game_board)
# for i in range(30):
#     game_board.drop_active_piece()

# print(game_board)
# game_board.add_rel_piece()
# print(game_board)
# for _ in range(30):
#     game_board.drop_active_piece()
# print(game_board)
# game_board.drop_active_piece()
# game_board.move_active_piece_right()
# game_board.move_active_piece_right()
# game_board.move_active_piece_right()
# print(game_board)

# TetrisView.TetrisView(game_board)
