# library imports 
import pygame

# game imports
from common import *
import player
import map

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
frame_time = 0


# game variables
p1 = player.Player()
map_screen = map.MapScreen()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    ##################
    # part 1: update #
    ##################
    keys = pygame.key.get_pressed()
    p1.update(frame_time, keys, current_map_screen=map_screen)
    map_screen.update(frame_time)

    ################
    # part 2: draw #
    ################
    map_screen.draw(screen)
    p1.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    frame_time = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()