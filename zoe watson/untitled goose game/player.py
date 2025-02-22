import pygame

class Goose:

    # constructor function (creates a goose object)
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = pygame.Color(255, 255,255)
        self.size = 2

    # update the goose
    def update(self):
        pass

    # draw the goose
    def draw(self):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
