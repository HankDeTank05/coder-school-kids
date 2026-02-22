import pygame
from constants import *
import random

class MovingObject:

    def __init__(self, rect, speed, color):
        self._rect = rect
        self._speed = speed
        self._colot = color

    def _set_start_pos(self):
        x = random.randint(0, WIDTH - self._rect.width)
        y = -self._rect.height
        self._rect.update(x, y, self._rect.width, self._rect.height)