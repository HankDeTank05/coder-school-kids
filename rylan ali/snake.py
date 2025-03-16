import pygame
import common as c

class Snake:
    
    # constructor
    def __init__(self, start_x, start_y, start_dir_move):
        self.pos = []
        self.dir = start_dir_move
        build_segments = start_dir_move * -1
        snake_start = pygame.math.Vector2(start_x, start_y)
        for i in range(5):
            self.pos.append(snake_start + build_segments)
            print(self.pos[i])
        self.move_queue

    def update(self):

            if len(self.move_queue) == 0: #if there is nothing left in the move_queue
                # read for input
                keys=pygame.key.get_pressed()
                # TODO: come back next time and prevent 180 deg turns (or find a way to allow it without snake overlapping itself)
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
            self.pos.insert(0, snake_head)
            self.pos.pop()