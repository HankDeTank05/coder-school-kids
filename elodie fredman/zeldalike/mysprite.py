import pygame
from common import *
from convenience import load_sprite

class MySprite(pygame.sprite.Sprite):
    _position: pygame.math.Vector2
    _draw_offset: pygame.math.Vector2
    _hitbox: pygame.Rect
    _hurtbox: pygame.Rect


    def __init__(self, path, offset: pygame.math.Vector2, hitbox: pygame.Rect | None = None, hurtbox: pygame.Rect | None = None):
        self.image = load_sprite(path=path)
        self.rect = self.image.get_rect()

        self._position = pygame.math.Vector2(0, 0)
        self._draw_offset = offset

        self.rect.topleft = self._position + self._draw_offset

        self._hitbox = hitbox
        self._hurtbox = hurtbox

    def draw(self, screen) -> None:
        # draws the sprite
        screen.blit(self.image, self.rect)

        # draws the hitbox
        pygame.draw.rect(screen, COLOR_RED, self._hitbox, width = 1)

        # draws the hurtbox
        if self._hurtbox is not None:
            pygame.draw.rect(screen, COLOR_BLUE, self._hurtbox, width = 1)

        # draws the corner position before applying offset
        pygame.draw.circle(screen, 'gray', self._position, 5)

    def _move_by(self, delta: pygame.math.Vector2):
        self._position += delta
        self.rect.topleft = self._position + self._draw_offset
        self._hitbox.move_ip(delta)

        if self._hurtbox is not None:
            self._hurtbox.move_ip(delta)



    
