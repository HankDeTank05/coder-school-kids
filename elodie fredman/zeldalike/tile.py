import pygame
from common import *

# NOTE: this is probably not the right way to avoid a circular import ("from map import Map" is causing the circular import)
# NOTE: until a better solution can be found, this will stay here so the program can run
# NOTE: ^^from Henry^^^
class Map:
    pass
        
class Tile:

    _rect: pygame.Rect
    _color: pygame.Color
    _is_solid: bool
    _transition_to: Map

    def __init__(self, pos: pygame.math.Vector2, color: pygame.Color, is_solid: bool, transition_to: Map | None = None):
        self._rect = pygame.Rect(pos, pygame.math.Vector2(TILE_WIDTH_PX, TILE_HEIGHT_PX))
        self._color = color
        self._is_solid = is_solid
        self._transition_to = transition_to

    def draw(self, screen):
        pygame.draw.rect(surface=screen, color=self._color, rect=self._rect)

    # accessors:

    @property
    def rect(self) -> pygame.Rect:
        return self._rect
    
    @property
    def is_solid(self) -> bool:
        return self._is_solid

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

class TileDoor(Tile):

    def __init__(self, pos: pygame.math.Vector2, transition_to: Map):
        assert(transition_to is not None)
        super().__init__(pos=pos, color=COLOR_BLUE, is_solid=False, transition_to=transition_to)

    def __repr__(self) -> str:
        return 'D'