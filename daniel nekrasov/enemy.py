import pygame
import common as c

class Frank:

    #constructor
    def __init__(self, speed, pos):
        self.color = c.DARK_GREEN
        self.speed = speed
        self.dir = pygame.math.Vector2(-1,0)
        self.health = c.FRANK_BASE_HEALTH
        self.pos = pos
        self.flash_timer = 0
        self.SIZE = 100

    def update(self, dt, target: pygame.math.Vector2):
        if self.flash_timer > 0:
            self.flash_timer -= dt
        pos_delta = target - self.pos
        pos_delta.normalize_ip()
        pos_delta *= self.speed

        pos_delta *= dt
        self.pos += pos_delta
        if self.flash_timer <= 0:
            self.color = c.DARK_GREEN

    def hit(self, damage):
        self.health -= damage
        self.color = c.RED
        self.flash_timer = 0.1

    def draw(self):
        pygame.draw.circle(c.screen, self.color, self.pos, self.SIZE) #drawing frank
        