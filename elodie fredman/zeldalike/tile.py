import pygame
from common import *

class Tile:

    def __init__(self, pos: pygame.math.Vector2, color: pygame.Color, is_solid: bool, transition_to = None):
        self._rect = pygame.Rect(pos, pygame.math.Vector2(TILE_WIDTH_PX, TILE_HEIGHT_PX))
        self._color = color
        self._is_solid = is_solid
        self._transition_to = transition_to

    def draw(self, screen):
        pygame.draw.rect(surface=screen, color=self._color, rect=self._rect)

class TileFloor(Tile):

    def __init__(self, pos: pygame.math.Vector2, color: pygame.Color):
        super().__init__(pos=pos, color=color, is_solid=False, transition_to=None)

    def __repr__(self) -> str:
        return '/'

class TileFloorGrass(TileFloor):

    def __init__(self, pos: pygame.math.Vector2):
        super().__init__(pos=pos, color=COLOR_GREEN)

class TileWall(Tile):

    def __init__(self, pos: pygame.math.Vector2, color: pygame.Color):
        super().__init__(pos=pos, color=color, is_solid=True, transition_to=None)

    def __repr__(self) -> str:
        return '#'

class TileWallDirt(TileWall):
    
    def __init__(self, pos: pygame.math.Vector2):
        super().__init__(pos=pos, color=COLOR_BROWN)