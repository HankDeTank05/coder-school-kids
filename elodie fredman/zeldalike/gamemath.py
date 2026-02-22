import pygame
from common import *

def tiles_to_pixels(tile_pos: pygame.math.Vector2) -> pygame.math.Vector2:
    return pygame.math.Vector2(TILE_WIDTH_PX * tile_pos.x, TILE_HEIGHT_PX * tile_pos.y)
def pixels_to_tiles():
    pass