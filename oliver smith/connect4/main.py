import pygame


from constants import *
from pieces import Pieces
from board import Board



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()


running = True
clock = pygame.time.Clock()
frame_time = 0

m1_prev = False
m1_curr = False

board = Board(COLUMN_COUNT, ROW_COUNT, player_count=10)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # part 1 - update

    # 1.1 - process input
    mx, my = pygame.mouse.get_pos()
    m1_curr = pygame.mouse.get_pressed()[0]

    # 1.2 - actual update
    board.update(frame_time, mx, my, m1_prev == True and m1_curr == False)

    # 1.3 - prep for next frame
    m1_prev = m1_curr


    # part 2 - draw

    screen.fill(COLOR_BLUE)

    board.draw(screen)

    pygame.display.flip()
    frame_time = clock.tick(FPS) / 1000

pygame.quit()
