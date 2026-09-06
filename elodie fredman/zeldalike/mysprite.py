import pygame
from common import *
from convenience import load_sprite

class MySprite:
    _spr: pygame.sprite.Sprite
    _draw_offset: pygame.math.Vector2
    _hitbox: pygame.Rect
    _hurtbox: pygame.Rect


    def __init__(self, path, offset: pygame.math.Vector2, hitbox: pygame.Rect | None = None, hurtbox: pygame.Rect | None = None):
        self._spr = pygame.sprite.Sprite()
        self._spr.image = load_sprite(path=path)
        self._spr.rect = self._spr.image.get_rect()

        self._draw_offset = offset

    def draw(self, screen, draw_pos) -> None:
        self._spr.rect.topleft = draw_pos + self._draw_offset
        screen.blit(self._spr.image, self._spr.rect)
