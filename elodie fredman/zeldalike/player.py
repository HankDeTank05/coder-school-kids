import pygame
from common import *
from gamemath import tiles_to_pixels

class Player:

    def __init__(self):
        self._pos = pygame.math.Vector2(0,0) # this is in px, not tiles
        self._speed = 250 #pps (pixels per second)
        self._size = pygame.math.Vector2(TILE_WIDTH_PX, TILE_HEIGHT_PX)

    def update(self, frame_time, keys, current_map_screen):
        pos_delta = pygame.math.Vector2(0,0)

        #calculate movement
        if keys[pygame.K_UP]:
            pos_delta.y -= 1
        if keys[pygame.K_DOWN]:
            pos_delta.y += 1
        if keys[pygame.K_RIGHT]:
            pos_delta.x += 1
        if keys[pygame.K_LEFT]:
            pos_delta.x -= 1

        # fix diagonal movement
        if pos_delta.x != 0 and pos_delta.y != 0:
            pos_delta = pos_delta.normalize()
        
        #move player 
        self._pos += pos_delta * self._speed * frame_time

        # stay on screen
        if self._pos.x < 0:
            self._pos.x = 0
        elif self._pos.x > WIDTH - 1 - self._size.x:
            self._pos.x = WIDTH - 1 - self._size.x
        
        if self._pos.y < 0:
            self._pos.y = 0
        elif self._pos.y > HEIGHT - 1 - self._size.y:
            self._pos.y = HEIGHT - 1 - self._size.y 

        # TODO: check for collision w/ map screen
        my_rect = pygame.Rect(self._pos, self._size)
        for y in range(SCREEN_TILE_HEIGHT):
            for x in range(SCREEN_TILE_WIDTH):
                if my_rect.colliderect()
        
    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(self._pos, self._size))

    def spawn_at_tile(self, tile_pos: pygame.math.Vector2):
        self._pos = tiles_to_pixels(tile_pos)