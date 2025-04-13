import pygame
import random
import common as c

class Food:
    def __init__(self, start_x, start_y):
        self.pos = pygame.math.Vector2(start_x, start_y)
        self.rect = pygame.Rect(start_x, start_y,c.TILE_SIZE,c.TILE_SIZE)
    
    def update(self): 
        pass 

    def draw(self, screen):
        pygame.draw.rect(surface=screen,
                         color = c.COLOR_GREEN,
                         rect=self.rect)
        
class FoodManager:
    
    def __init__(self):
        self.food = []
        self.max_food = 1

    def create_food(self):
        start_x = random.randrange(c.GRID_WIDTH)
        start_y = random.randrange(c.GRID_HEIGHT)
        self.food.append(Food(start_x, start_y))

    def update(self, other_rect):
        pass