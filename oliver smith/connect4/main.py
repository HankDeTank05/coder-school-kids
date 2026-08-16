import pygame


from constants import *
from pieces import Pieces
from board import Board



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()


running = True
clock = pygame.time.Clock()
frame_time = 0

board = Board(COLUMN_COUNT, ROW_COUNT, X_CIRCLE_SPACING, Y_CIRCLE_SPACING)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # part 1 - update

    board.update(frame_time)
        

    # part 2 - draw

    screen.fill(COLOR_BLUE)

    board.draw(screen)

    pygame.display.flip()
    frame_time = clock.tick(FPS) / 1000

pygame.quit()
