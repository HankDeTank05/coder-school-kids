# language imports (these are built in to python)
# DONT HOLD TAB
# library imports (this is stuff that's not ours, but not built in to python)
import pygame

# project imports (this is our stuff we created)
from constants import *
from gamestate import GameState, StartState


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()



clock = pygame.time.Clock()

frame_time = 0
running = True
current_state: GameState = StartState()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


    ##################
    # PART 1: UPDATE #
    ##################
    keys = pygame.key.get_pressed()
    current_state.update(frame_time, events, keys)

    ################
    # PART 2: DRAW #
    ################

    screen.fill(WHITE) # fill the screen with a color to wipe away anything from last frame

    current_state.draw(screen)

    pygame.display.flip() # flip() the display to put your work on screen

    ##########################
    # PART 3: GET NEXT STATE #
    ##########################

    current_state = current_state.get_next_state()

    frame_time = clock.tick(FPS) / 1000  # limits FPS to 60

pygame.quit()