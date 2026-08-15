import pygame

from constants import *





class Pieces:


    def __init__(self, color,x,y):
        self._rect = pygame.Rect(x,y, PIECES_SIZE, PIECES_SIZE)
        self._circle_center = self._rect.center
        self._circle_radius = self._rect.width / 2
        self._color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, self._circle_center, self._circle_radius)

    def click_event(self):
        mouse_pos = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            print(f"holding left click at {mouse_pos}")