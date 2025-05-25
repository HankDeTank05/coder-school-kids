import pygame
import random
import common as c
import snake as s


class Food:

    # constuctor 
    def __init__(self, start_x, start_y):
        self.pos = pygame.math.Vector2(start_x, start_y)
        self.rect = pygame.Rect(start_x, start_y,c.TILE_SIZE,c.TILE_SIZE)
    
    def update(self): 
        pass 

    def draw(self, screen):
        pygame.draw.rect(surface=screen,
                         color = c.COLOR_GREEN,
                         rect=self.rect)
        
    def get_pos(self):
        return self.pos
        
class FoodManager:
    
    # constuctor
    def __init__(self):
        self.food = []
        self.max_food = 100

    def create_food(self):
        # checks length because we need to know if we can add more food
        if len(self.food) < self.max_food:
            # radomizes the places the food can spawn
            temp_x = random.randrange(c.GRID_WIDTH)
            temp_y = random.randrange(c.GRID_HEIGHT)
            found = False 
            can_insert = False
            current_index = 0
            while found == False:
                # gets the current pos of the indexed food object in self.food
                current_pos = self.food[current_index].get_pos()
                if temp_x == current_pos.x:
                    if temp_y == current_pos.y:
                        # reramdomize temp_pos
                        temp_x = random.randrange(c.GRID_WIDTH)
                        temp_y = random.randrange(c.GRID_HEIGHT)
                        current_index = 0
                        continue # continue  restarts the loop without running any code inside the loop below it 
                    elif temp_y < current_pos.y: 
                        temp_food = Food(temp_x, temp_y)
                        self.food.insert(current_index, temp_food)
                    elif temp_y > current_pos.y:
                        next_pos = self.food[current_index + 1].get_pos()
                        if temp_x < next_pos.x or (temp_x == next_pos.x and temp_y < next_pos.y):
                            temp_food = Food(temp_x, temp_y)
                            self.food.insert(current_index + 1,temp_food)
                else:
                    current_index = current_index + 1 # increase index by 1 
            temp_food = Food(temp_x, temp_y)
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
        #                                                 this is the end of the range - 1 (it will always stops at 0)
        #                         the start of the range  ||   this means to count down by 1
        #                         vvvvvvvvvvvvvvvvvvvvvv  vv  vv
        for remove_index in range(len(food_2_remove) - 1, -1, -1):
            # remove_index = the index of food_2_remove
            # food_index = the index at which to remove a Food object (from self.food)
            food_index = food_2_remove[remove_index]
            self.food.pop(food_index)

    def draw(self, screen):
        for i in range(len(self.food)):
            self.food[i].draw(screen)