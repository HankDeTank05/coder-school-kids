import pygame
from common import *


class Map:
    
    def __init__(self):
        self._screens: list[list[MapScreen]]

class MapScreen:
    
    def __init__(self):
        self._tiles = []
        for y in range(SCREEN_TILE_HEIGHT):
            self._tiles.append([])
            for x in range(SCREEN_TILE_WIDTH):
                self._tiles[y].append(None)
                if x == 0 or x == SCREEN_TILE_WIDTH - 1 or y == 0 or y == SCREEN_TILE_HEIGHT - 1:
                    self._tiles[y][x] = '#'
                else:
                    self._tiles[y][x] = ' '
            print(self._tiles[y])

    def update(self, frame_time):
        pass

    def draw(self, screen):
        # draw map tiles
        for y in range(len(self._tiles)): # for every row in the grid
            for x in range(len(self._tiles[y])): #for every tile in the row 
                tile_rect = pygame.Rect(x * TILE_WIDTH, y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                if self._tiles[y][x]== '#':
                    pygame.draw.rect(screen, TILE_WALL_COLOR, tile_rect)
                elif self._tiles[y][x] == ' ':
                    pygame.draw.rect(screen, TILE_FLOOR_COLOR, tile_rect)
        # makes grid lines for the map
        for x in range(0,WIDTH - 1, TILE_WIDTH):
            pygame.draw.line(screen, COLOR_BLACK, (x,0), (x,HEIGHT-1))
        for y in range(0, HEIGHT - 1, TILE_HEIGHT):
            pygame.draw.line(screen, COLOR_BLACK, (0,y), (WIDTH - 1, y))