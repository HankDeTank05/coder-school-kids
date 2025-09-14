import random
import common as c
import pygame
import snake as s
class Trap:

    def __init__(self, start_grid_x, start_grid_y):
        assert(0<= start_grid_x)# checking if 0 is equal to or less than start_grid_x
        assert(start_grid_x < c.GRID_WIDTH)# shows that start_grid_x is less than 160
        assert(0<= start_grid_y)#
        assert(start_grid_y < c.GRID_HEIGHT)# 
        self.color = (10, 64, 12) # dark green
        self.size = random.randint(2, 4)
        self.grid_pos = pygame.math.Vector2(start_grid_x, start_grid_y)
        start_screen_x = start_grid_x * c.TILE_SIZE
        start_screen_y = start_grid_y * c.TILE_SIZE
        self.rect = pygame.Rect(start_screen_x, start_screen_y, c.TILE_SIZE * self.size, c.TILE_SIZE * self.size)

        self.act_rate = None # activation rate (aka, the percent chance the trap will trigger)
        if self.size == 2:
            self.act_rate = 40
        elif self.size == 3:
            self.act_rate = 30
        elif self.size == 4:
            self.act_rate = 20
        else:
            assert(False)

        self.touch_snake_prev = False 
        self.trap_bool = False
            
    def update(self, snake):
        touch_snake_curr = snake.get_head_rect().colliderect(self.rect)
        # more code goes here

        if self.touch_snake_prev == False and touch_snake_curr == True:
            number = random.randrange(1, 101)
            if number <= self.act_rate:
                self.trap_bool = True # trigger the trap

        # vvv this is to prepare for the next frame vvv
        self.touch_snake_prev = touch_snake_curr

    def draw(self, screen):
        pygame.draw.rect(surface=screen,color =self.color, rect=self.rect)

    def check_trap_act(self) -> bool:
        return self.trap_bool


class TrapManager:
    def __init__(self, sp_max_traps):
        self.traps: list[Trap] = []
        self.max_traps = sp_max_traps
        for i in range(self.max_traps):
            self.create_trap()

    def create_trap(self):
        # checks length to know if we need to add more traps 
        if len(self.traps) < self.max_traps:
            temp_grid_x = random.randrange(c.GRID_WIDTH)
            temp_grid_y = random.randrange(c.GRID_HEIGHT)
            temp_trap = Trap(temp_grid_x,temp_grid_y)
            self.traps.append(temp_trap)
           
    def update(self):
        pass

    def draw(self, screen):
        for i in range(len(self.traps)):
            self.traps[i].draw(screen)
     