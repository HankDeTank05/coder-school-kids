import pygame

class Platform:

    # constructor
    def __init__(self, _x, _y, _width, _height, _color):
        self.x=_x
        self.y=_y
        self.width=_width
        self.height=_height
        self.color=_color


    def update(self, _dt):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
