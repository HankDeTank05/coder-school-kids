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
   
    def update(self, snake_rect: pygame.Rect):

        # generating a list of indices at which to remove Food objects

        # this just means the variable is a list of ints
        #            vvvvvvvvvvv
        food_2_remove: list[int] = []

        # this for loop iterates over self.food in forward order 
        # when a food object collides with snake_rect it adds an index to food_2_remove
        for i in range(len(self.food)):
            food_item = self.food[i]
            food_rect = food_item.rect
            if food_rect.colliderect(snake_rect) == True:
                food_2_remove.append(i)

        # removes Food items that the player has collided with

        food_2_remove = sorted(food_2_remove)

        # this for loop iterates over food_2_remove in end-to-start order (aka, reverse order)
        # it iterates in reverse order so it doesen't affect the other indices so we won't remove the wrong items
        for remove_index in range(start=len(food_2_remove) - 1, stop=-1, step=-1):
            # remove_index = the index of food_2_remove
            # food_index = the index at which to remove a Food object (from self.food)
            food_index = food_2_remove[remove_index]
            self.food.pop(food_index)

    def draw(self, screen):
        for i in range(len(self.food)):
            self.food[i].draw(screen)