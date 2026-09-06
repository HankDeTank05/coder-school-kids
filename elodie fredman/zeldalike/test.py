# Example file showing a basic pygame "game loop"
import pygame
import os
from mysprite import MySprite
from common import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


# load stuff to see here
spr = MySprite(
    path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_up_1.png'),
    offset=pygame.math.Vector2(0,-12 * SCALE_FACTOR),
    hitbox=pygame.Rect(0,0,16*SCALE_FACTOR,16*SCALE_FACTOR)
)
test_pos = pygame.math.Vector2(245,167)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # RENDER YOUR GAME HERE

    spr.draw(screen=screen, draw_pos=test_pos)
    pygame.draw.circle(screen, 'gray', test_pos, 2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()