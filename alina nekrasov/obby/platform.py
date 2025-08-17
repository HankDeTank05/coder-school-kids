import pygame

class Platform:

    # constructor
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def update(self, delta_time):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
 
# plat = Platform(????)

class PlatManager:

    # constructor
    def __init__(self):
        self.platforms: list[Platform] = []

    def update(self, delta_time):
        for platform in self.platforms:
            platform.update(delta_time)
    
    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)

# plat_man = PlatManager()