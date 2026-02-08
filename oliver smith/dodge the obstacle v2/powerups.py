import pygame
from constants import *


class Powerup:

    def __init__(self, rect: pygame.Rect, color):
        self._speed = OBSTACLE_SPEED_BIG
        self._rect: pygame.Rect = rect
        self._color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self._rect)



class Invincibility(Powerup):

    def __init__(self):
        temp_rect = pygame.Rect(0, 0, OBSTACLE_NORMAL_WIDTH, OBSTACLE_NORMAL_HEIGHT)
        super().__init__(temp_rect, MIDNIGHT_BLUE)
