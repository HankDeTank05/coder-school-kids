import pygame

#screen stuff
pygame.init()
SCREEN_WIDTH=1280
SCREEN_HEIGHT=720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (170, 0, 0)
VERY_DARK_RED = (85, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 170, 0)
VERY_DARK_GREEN = (0, 85, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 170)
VERY_DARK_BLUE = (0, 0, 85)

#collision stuff
PLAYER_BASE_HEALTH = 100
FRANK_BASE_HEALTH = 1000

# player stuff
NORMAL_TIMESCALE = 1
SLOMO_TIMESCALE = 0.1

