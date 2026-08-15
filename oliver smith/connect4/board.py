import pygame
from pieces import Pieces
from constants import *


class Board:


    def __init__(self, screen, column, row, x, y):
        self._column = column
        self._row = row
        self._x = x
        self._y = y
        self.draw(screen)


    def draw(self, screen):
        x = self._x
        self._y = 10
        for row in range(self._row):
            for col in range(self._column):
                circle = Pieces(COLOR_WHITE, self._x, self._y)
                circle.click_event()
                circle.draw(screen)
                self._x += 160
            self._y += 160
            self._x = x