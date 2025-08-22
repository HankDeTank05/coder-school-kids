import pygame

import common as c

class Paddle:

    # constructor
    def __init__(self, start_pos: pygame.math.Vector2, color: pygame.Color, up_key: int, down_key: int):
        self.rect = pygame.Rect(start_pos, pygame.math.Vector2(c.PADDLE_WIDTH, c.PADDLE_HEIGHT))
        self.color = color
        self.upkey = up_key
        self.downkey = down_key

    def update(self, frame_time):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)