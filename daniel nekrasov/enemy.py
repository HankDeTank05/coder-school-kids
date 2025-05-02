import pygame
import common as c

class Frank:

    #constructor
    def __init__(self, speed, pos, width, height):
        self.color = c.DARK_GREEN
        self.speed = speed
        self.dir = 
        self.health = 
        self.rect = pygame.Rect(pos, pygame.math.Vector2(width, height))

    def update(self, dt):
        pass

    def draw(self):
        pygame.draw.rect(c.screen, self.color, self.rect)