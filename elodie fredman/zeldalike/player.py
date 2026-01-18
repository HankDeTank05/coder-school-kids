import pygame
from common import *

class Player:

    def __init__(self):
        self._pos = pygame.math.Vector2(0,0)
        self._speed = 1000
        self._size = 10

    def update(self, frame_time, keys):
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
        elif self._pos.x > WIDTH - 1 - self._size:
            self._pos.x = WIDTH - 1 - self._size
        
        if self._pos.y < 0:
            self._pos.y = 0
        elif self._pos.y > HEIGHT - 1 - self._size:
            self._pos.y = HEIGHT - 1 - self._size 

    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(self._pos, (self._size, self._size)))