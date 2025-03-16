import pygame

class Platform:

    def __init__(self, x, y, width, height, color):
        self.platform = pygame.Rect(x, y, width, height)
        self.color = color

    def update(self, delta_time):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.platform)