import pygame

class Player:

    def __init__(self):
        self._pos = pygame.math.Vector2(0,0)
        self._speed = 100
        self._size = 10

    def update(self, frame_time, keys):
        if keys[pygame.K_UP]:
            self._pos.y -= self._speed * frame_time
        if keys[pygame.K_DOWN]:
            self._pos.y += self._speed * frame_time
        if keys[pygame.K_RIGHT]:
            self._pos.x += self._speed * frame_time
        if keys[pygame.K_LEFT]:
            self._pos.x -= self._speed * frame_time

    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(self._pos, (self._size, self._size)))