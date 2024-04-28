import pygame
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode([500, 1000])

running = True

T = [[0, 0], [1, 0], [2, 0], [1, 1]]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))

    surf = pygame.Surface((50, 50))
    surf.fill((255, 0, 0))

    for coordinate in T:

        column = coordinate[0] * 50
        row = coordinate[1] * 50
        screen.blit(surf, (column, row))

    pygame.display.flip()
