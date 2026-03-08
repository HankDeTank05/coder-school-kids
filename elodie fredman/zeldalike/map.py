import pygame
from common import *
from tile import Tile, TileWallDirt, TileFloorGrass


class Map:
    
    def __init__(self):
        self._screens: list[list[MapScreen]]
        for y in range(3):
            self._screens.append([])
            for x in range(3):
                self._screens[y].append(MapScreen())

class MapScreen:
    _spawn_tile_pos: pygame.math.Vector2
    _tiles: list[list[Tile]]
    
    def __init__(self, spawn_tile_pos: pygame.math.Vector2):
        self._spawn_tile_pos = spawn_tile_pos
        self._tiles = []
        for tile_y in range(SCREEN_TILE_HEIGHT):
            self._tiles.append([])
            for tile_x in range(SCREEN_TILE_WIDTH):
                tile_pos = pygame.math.Vector2(tile_x * TILE_WIDTH_PX, tile_y * TILE_HEIGHT_PX)
                if tile_x == 0 or tile_x == SCREEN_TILE_WIDTH - 1 or tile_y == 0 or tile_y == SCREEN_TILE_HEIGHT - 1:
                    self._tiles[tile_y].append(TileWallDirt(pos=tile_pos))
                else:
                    self._tiles[tile_y].append(TileFloorGrass(pos=tile_pos))
            print(self._tiles[tile_y])

    # game functions

    def update(self, frame_time):
        pass

    def draw(self, screen):
        # draw map tiles
        for y in range(len(self._tiles)): # for every row in the grid
            for x in range(len(self._tiles[y])): #for every tile in the row 
                self._tiles[y][x].draw(screen)
        # makes grid lines for the map
        for x in range(0,SCREEN_WIDTH - 1, TILE_WIDTH_PX):
            pygame.draw.line(screen, COLOR_BLACK, (x,0), (x,SCREEN_HEIGHT-1))
        for y in range(0, SCREEN_HEIGHT - 1, TILE_HEIGHT_PX):
            pygame.draw.line(screen, COLOR_BLACK, (0,y), (SCREEN_WIDTH - 1, y))

    # accessors

    def get_spawn_tile_pos(self) -> pygame.math.Vector2:
        return self._spawn_tile_pos
    
    def get_tile_at(self, x: int, y: int) -> Tile:
        return self._tiles[y][x]