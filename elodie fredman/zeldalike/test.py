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
    hitbox=pygame.Rect(0,0,16*SCALE_FACTOR,16*SCALE_FACTOR),
    hurtbox=pygame.Rect(0, -12*SCALE_FACTOR, 16*SCALE_FACTOR, 11*SCALE_FACTOR)
)
test_pos = pygame.math.Vector2(245,167)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE
    
    pos_delta = pygame.math.Vector2(0, 0)
    keys = pygame.key.get_pressed()
    #calculate movement
    if keys[pygame.K_UP]:
        pos_delta.y -= 1
    if keys[pygame.K_DOWN]:
        pos_delta.y += 1      
    if keys[pygame.K_LEFT]:
        pos_delta.x -= 1
    if keys[pygame.K_RIGHT]:
        pos_delta.x += 1
    spr._move_by(pos_delta * 5)


    # DRAW

    screen.fill('black')
    spr.draw(screen=screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()