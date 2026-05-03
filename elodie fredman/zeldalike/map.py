import pygame
from common import *
from tile import Tile, TileWallDirt, TileFloorGrass
from settings import *
from enum import Enum

class Edge(Enum):
    Top = 1
    Bottom = 57
    Left = 932
    Right = 35



class MapScreen:
    _spawn_tile_pos: pygame.math.Vector2
    _tiles: list[list[Tile]]
    
    def __init__(self, spawn_tile_pos: pygame.math.Vector2 = pygame.math.Vector2(SCREEN_TILE_WIDTH // 2, SCREEN_TILE_HEIGHT // 2)):
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

    def draw(self, screen: pygame.Surface)-> None:
        # draw map tiles
        for y in range(len(self._tiles)): # for every row in the grid
            for x in range(len(self._tiles[y])): #for every tile in the row 
                self._tiles[y][x].draw(screen)
        if SHOW_GRIDLINES:

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
    
    # mutators

    def set_tile_grass_floor(self, x: int, y: int) -> None:
        self._tiles[y][x] = TileFloorGrass(pygame.math.Vector2(TILE_WIDTH_PX * x, TILE_HEIGHT_PX * y))

    def set_tile_dirt_wall(self, x: int, y: int) -> None:
        pass

class Map:
    _screens: list[list[MapScreen]]
    _current_screen: pygame.math.Vector2
    _start_screen: pygame.math.Vector2
    _go_down_box: pygame.Rect
    _go_up_box: pygame.Rect
    _go_right_box: pygame.Rect
    _go_left_box: pygame.Rect

    def __init__(self, map_screen_width:int, map_screen_height:int, start_screen_x: int, start_screen_y: int):
        assert(map_screen_width>0)
        assert(map_screen_height>0)
        self._screens = []
        for y in range(map_screen_height):
            self._screens.append([])
            for x in range(map_screen_width):
                self._screens[y].append(MapScreen())
        assert(0<=start_screen_x<map_screen_width)
        assert(0<=start_screen_y<map_screen_height)
        self._current_screen = pygame.math.Vector2(start_screen_x, start_screen_y)
        self._start_screen = pygame.math.Vector2(start_screen_x, start_screen_y)
        self._go_down_box = pygame.Rect(0, SCREEN_HEIGHT - SCREEN_TRANS_BOX_SIZE, SCREEN_WIDTH, SCREEN_TRANS_BOX_SIZE)
        self._go_up_box = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_TRANS_BOX_SIZE)
        self._go_right_box = pygame.Rect(SCREEN_WIDTH - SCREEN_TRANS_BOX_SIZE, 00, SCREEN_TRANS_BOX_SIZE, SCREEN_HEIGHT)
        self._go_left_box = pygame.Rect(0, 0, SCREEN_TRANS_BOX_SIZE, SCREEN_HEIGHT)

    # game functions

    def update(self, frame_time: float) -> None:
        pass

    def draw(self, screen: pygame.Surface)-> None:
        # assert(False)
        # map_screen: MapScreen=self._screens[1][1]
        # map_screen.draw(screen=screen)
        pygame.draw.rect(screen, COLOR_RED, self._go_down_box, width=1)
        pygame.draw.rect(screen, COLOR_RED, self._go_up_box, width=1)
        pygame.draw.rect(screen, COLOR_RED, self._go_right_box, width=1)
        pygame.draw.rect(screen, COLOR_RED, self._go_left_box, width=1)
        

    # accessors

    def get_start_screen(self) -> MapScreen:
        return self._screens[int(self._start_screen.y)][int(self._start_screen.x)]
    
    def get_current_screen(self) -> MapScreen:
        return self._screens[int(self._current_screen.x)][int(self._current_screen.y)]

    def get_map_screen(self, map_screen_x: int, map_screen_y: int)-> MapScreen:
        return self._screens[map_screen_y][map_screen_x]
    
    def get_trans_box(self, edge: Edge) -> pygame.Rect:

        if edge == Edge.Top:
            return self._go_up_box
        elif edge == Edge.Bottom:
            return self._go_down_box
        elif edge == Edge.Right:
            return self._go_right_box
        elif edge == Edge.Left:
            return self._go_left_box
        else:
            assert(False)

    # mutators

    def go_down(self) -> None:
        self._current_screen.y += 1