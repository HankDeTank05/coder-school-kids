import pygame


from constants import *
from pieces import Pieces
from board import Board



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()


running = True
clock = pygame.time.Clock()
frame_time = 0

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        


    screen.fill(COLOR_BLUE)
    Board(screen, COLUMN, ROW, X, Y)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
