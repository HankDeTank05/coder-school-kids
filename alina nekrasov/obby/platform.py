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
        self._platforms: list[Platform] = []

    def update(self, delta_time):
        for platform in self._platforms:
            platform.update(delta_time)
    
    def draw(self, screen):
        for platform in self._platforms:
            platform.draw(screen)

    def add_plat(self, x, y, width, height, color):
        plat = Platform(x, y, width, height, color)
        self._platforms.append(plat)

    def add_plat_relative(self, x, y, width, height, color):
        last_x = self._platforms[-1].rect.x
        last_y = self._platforms[-1].rect.y
        plat = Platform(last_x + x, last_y + y, width, height, color)
        self._platforms.append(plat)

    def get_rects(self) -> list[pygame.Rect]:
        rects: list[pygame.Rect] = []
        # populate the list
        for plat_index in range(len(self._platforms)):
            plat = self._platforms[plat_index]
            plat_rect =plat.rect
            rects.append(plat_rect)
        return rects

# plat_man = PlatManager()