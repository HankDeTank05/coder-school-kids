import pygame
import random
import common as c
import snake as s

class Food:

    # constuctor 
    def __init__(self, start_grid_x, start_grid_y):
        assert(0<= start_grid_x)
        assert(start_grid_x  < c.GRID_WIDTH)
        assert(0<= start_grid_y)
        assert(start_grid_y < c.GRID_HEIGHT)
        start_screen_x = start_grid_x * c.TILE_SIZE
        start_screen_y = start_grid_y * c.TILE_SIZE
        self.grid_pos = pygame.math.Vector2(start_grid_x, start_grid_y)
        self.rect = pygame.Rect(start_screen_x, start_screen_y, c.TILE_SIZE, c.TILE_SIZE)
    
    def update(self): 
        pass 

    def draw(self, screen):
        pygame.draw.rect(surface=screen,
                         color = c.COLOR_FOOD,
                         rect=self.rect)
        
    def get_screen_pos(self):
        return self.rect.topleft
    
    def get_grid_pos(self):
        return self.grid_pos
        
        
class FoodManager:
    
    # constuctor
    def __init__(self, sp_max_food):
        self.food: list[Food] = []
        self.max_food = sp_max_food
        for i in range(self.max_food):
            self.create_food()

    def create_food(self):
        # checks length because we need to know if we can add more food
        if len(self.food) < self.max_food:
            # radomizes the places the food can spawn
            temp_grid_x = random.randrange(c.GRID_WIDTH)
            temp_grid_y = random.randrange(c.GRID_HEIGHT)
            if len(self.food) > 0:
                # 1. check if if any other food object hass the same pos as the newly created food (which is located at index len(self.food)-1)
                unique_pos: bool = True
                for food in self.food:
                    if temp_grid_x == food.get_grid_pos().x and temp_grid_y == food.get_grid_pos().y:
                        unique_pos = False
                # 1.1. if (1) is true rerandomize pos of new food object
                # 2. sort list by calling .sort()
                pass
            temp_food = Food(temp_grid_x, temp_grid_y)
            self.food.append(temp_food)
        else:
            print("List is full")
   
    def update(self, snake):

        # generating a list of indices at which to remove Food objects

        # this just means the variable is a list of ints
        #            vvvvvvvvvvv
        food_2_remove: list[int] = []

        # this for loop iterates over self.food in forward order 
        # when a food object collides with snake_rect it adds an index to food_2_remove
        for i in range(len(self.food)):
            food_item = self.food[i]
            food_rect = food_item.rect
            # if the food item collides with the snake then....
            if food_rect.colliderect(snake.get_head_rect()) == True:
                # ... queues the food to be destroyed...
                food_2_remove.append(i)
                # ...and add a segment to the snake 
                snake.add_tile()

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

        for food in range(len(food_2_remove)):
            self.create_food()

    def draw(self, screen):
        for i in range(len(self.food)):
            self.food[i].draw(screen)