import pygame

class Circle:

    def __init__(self, center: pygame.math.Vector2, radius: int | float) -> None:
        self.center = center
        self.radius = radius