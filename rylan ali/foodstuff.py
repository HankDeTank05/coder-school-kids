import pygame
import random
import common as c
import snake as s


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
        self.max_food = 7

    def create_food(self):
        if len(self.food) < self.max_food:
            start_x = random.randrange(c.GRID_WIDTH)
            start_y = random.randrange(c.GRID_HEIGHT)
            temp_food = Food(start_x, start_y)
            self.food.append(temp_food)
        else:
            print("List is full")
   
    def update(self, other_rect: pygame.Rect):
        # TODO: come back here and rewrite this code
        food_2_remove = []
        for i in range(len(self.food)):
            if self.food[i].rect.colliderect(other_rect) == True:
                food_2_remove.append(i)
        while len(food_2_remove) > 0:
            pass

    def draw(self, screen):
        for i in range(len(self.food)):
            self.food[i].draw(screen)