import pygame

# directions
DIR_UP = pygame.math.Vector2(0, -1)
DIR_DOWN = pygame.math.Vector2(0, 1)
DIR_LEFT = pygame.math.Vector2(-1, 0)
DIR_RIGHT = pygame.math.Vector2(1, 0)

#colors
COLOR_BLACK = (0,0,0)
COLOR_RED = (155,0,0)

# display
GRID_WIDTH = 160
GRID_HEIGHT = 90
TILE_SIZE = 5
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE