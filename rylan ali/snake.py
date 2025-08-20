import pygame
import common as c

class Snake:
    
    # constructor
    def __init__(self, start_x, start_y, start_dir_move):
        self.pos = []
        self.dir = start_dir_move
        # dir segments build in after the head(multipling a  Vector2 by a negative number  makes it invert dir).
        build_segments_dir = start_dir_move * -1
        snake_start = pygame.math.Vector2(start_x, start_y)
        for i in range(5):
            self.pos.append(snake_start + build_segments_dir * i)
            print(self.pos[i])
        self.move_queue = []
        self.base_wait = c.SNAKE_WAIT
        self.wait_time = self.base_wait 

    def update(self, frame_time):
        self.wait_time -= frame_time
        if self.wait_time <= 0:
            self.wait_time = self.base_wait
            if len(self.move_queue) == 0: #if there is nothing left in the move_queue
                # read for input
                keys=pygame.key.get_pressed()
                # come back next time and prevent 180 deg turns (or find a way to allow it without snake overlapping itself)
                if keys[pygame.K_w] == True:
                    if self.dir != c.DIR_DOWN:
                        # no 180
                        self.dir = c.DIR_UP 
                    else:
                        #do 180 turn
                        self.move_queue.append(c.DIR_LEFT)
                        self.move_queue.append(c.DIR_UP)
                if keys[pygame.K_s] == True:
                    if self.dir != c.DIR_UP:
                        # no 180
                        self.dir = c.DIR_DOWN
                    else:
                        #do 180 turn
                        self.move_queue.append(c.DIR_RIGHT)
                        self.move_queue.append(c.DIR_DOWN)
                if keys[pygame.K_a] == True:  
                    if self.dir != c.DIR_RIGHT:
                        #no 180
                        self.dir =  c.DIR_LEFT
                    else:
                        #do 180 turn
                        self.move_queue.append(c.DIR_DOWN)
                        self.move_queue.append(c.DIR_LEFT)
                if keys[pygame.K_d] == True:
                    if self.dir != c.DIR_LEFT:
                        # no 180
                        self.dir = c.DIR_RIGHT
                    else:
                        # do 180 turn
                        self.move_queue.append(c.DIR_UP)
                        self.move_queue.append(c.DIR_RIGHT)   
            else:# there is somthing left in move_queue
                self.dir = self.move_queue[0]
                self.move_queue.pop(0)

            # snake_head = snake_head + snake_dir
            snake_head = self.pos[0] + self.dir # calculate new head pos
            if snake_head.x < 0:
                snake_head.x = c.GRID_WIDTH - 1
            elif snake_head.x > c.GRID_WIDTH - 1:
                snake_head.x = 0
            if snake_head.y < 0:
                snake_head.y = c.GRID_HEIGHT - 1 
            elif snake_head.y > c.GRID_HEIGHT - 1:
                snake_head.y = 0 
                
            
            self.pos.insert(0, snake_head)
            self.pos.pop()

            # check if the snake ran into itself
            for i in range(1, len(self.pos)):
                if snake_head == self.pos[i]:
                    pass # restart the game

    def draw(self, screen):
        for i in range(len(self.pos)):
            pygame.draw.rect(surface=screen, 
                                color=c.COLOR_RED,
                                rect=pygame.Rect(self.pos[i].x * c.TILE_SIZE,
                                                 self.pos[i].y * c.TILE_SIZE,
                                                 c.TILE_SIZE,
                                                 c.TILE_SIZE))
            
    def get_head_rect(self):
        return pygame.Rect(self.pos[0].x * c.TILE_SIZE,
                           self.pos[0].y * c.TILE_SIZE,
                           c.TILE_SIZE,
                           c.TILE_SIZE)
    
    def add_tile(self):
        #old_tail_pos = self.pos[len(self.pos)-1]
        old_tail_pos = self.pos[-1] # this is the same as the commented code above
        last_bod_seg = self.pos[-2]
        dir_2_add = old_tail_pos - last_bod_seg
        new_tail_pos = old_tail_pos + dir_2_add
        self.pos.append(new_tail_pos)
        self.base_wait -= 0.001

