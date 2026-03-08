import pygame
from common import *
from gamemath import tiles_to_pixels

class Player:

    def __init__(self):
        self._rect = pygame.Rect(
            pygame.math.Vector2(0,0), # this is in px, not tiles
            pygame.math.Vector2(TILE_WIDTH_PX, TILE_HEIGHT_PX)
        )
        
        self._speed = 250 #pps (pixels per second)

    # game functions

    def update(self, frame_time, keys, current_map_screen):
        # note: delta means change
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
        # self._pos += pos_delta * self._speed * frame_time
        self._rect.move_ip(pos_delta * self._speed * frame_time)

        # stay on screen
        # if self._pos.x < 0:
        #     self._pos.x = 0
        # elif self._pos.x > WIDTH - 1 - self._size.x:
        #     self._pos.x = WIDTH - 1 - self._size.x
        if self._rect.left < SCREEN_RECT.left:
            self._rect.left = SCREEN_RECT.left
        elif self._rect.right > SCREEN_RECT.right:
            self._rect.right = SCREEN_RECT.right
        
        # if self._pos.y < 0:
        #     self._pos.y = 0
        # elif self._pos.y > SCREEN_HEIGHT - 1 - self._size.y:
        #     self._pos.y = SCREEN_HEIGHT - 1 - self._size.y 
        if self._rect.top < SCREEN_RECT.top:
            self._rect.top = SCREEN_RECT.top
        elif self._rect.bottom > SCREEN_RECT.bottom:
            self._rect.bottom = SCREEN_RECT.bottom
                    
    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), self._rect)

    # accessors

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    # mutators

    def spawn_at_tile(self, tile_pos: pygame.math.Vector2):
        self._rect.topleft = tiles_to_pixels(tile_pos)
    