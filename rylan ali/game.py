# Example file showing a basic pygame "game loop"
import pygame
import common as c 
import snake 
import random
import foodstuff



# pygame setup
pygame.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

grid = []

for y in range(c.GRID_HEIGHT):
    grid.append([])
    for x in range(c.GRID_WIDTH):
        grid[y].append(None)
        
'''
segments = 5
snake_start = pygame.math.Vector2(c.GRID_WIDTH //2,c.GRID_HEIGHT //2)
snake_pos = []
for i in range(segments):
    snake_pos.append(snake_start + pygame.math.Vector2(0, i))
    print(snake_pos[i])

# grid[int(snake_head.y)][int(snake_head.x)] = "s0"


snake_dir = pygame.math.Vector2(0,-1)

move_queue = []
'''

'''
def snake_update():
    global snake_head
    global snake_dir

    if len(move_queue) == 0: #if there is nothing left in the move_queue
        # read for input
        keys=pygame.key.get_pressed()
        # TODO: come back next time and prevent 180 deg turns (or find a way to allow it without snake overlapping itself)
        if keys[pygame.K_w] == True:
            if snake_dir != dir_down:
                # no 180
                snake_dir = dir_up 
            else:
                #do 180 turn
                move_queue.append(dir_left)
                move_queue.append(dir_up)
        if keys[pygame.K_s] == True:
            if snake_dir != dir_up:
                # no 180
                snake_dir = dir_down
            else:
                #do 180 turn
                move_queue.append(dir_right)
                move_queue.append(dir_down)
        if keys[pygame.K_a] == True:  
            if snake_dir != dir_right:
                #no 180
                snake_dir =  dir_left
            else:
                #do 180 turn
                move_queue.append(dir_down)
                move_queue.append(dir_left)
        if keys[pygame.K_d] == True:
            if snake_dir != dir_left:
                # no 180
                snake_dir = dir_right
            else:
                # do 180 turn
                move_queue.append(dir_up)
                move_queue.append(dir_right)   
    else:# there is somthing left in move_queue
        snake_dir = move_queue[0]
        move_queue.pop(0)

    # grid[int(snake_head.y)][int(snake_head.x)] = None

    # snake_head = snake_head + snake_dir
    snake_head = snake_pos[0] + snake_dir # calculate new head pos
    snake_pos.insert(0, snake_head)
    snake_pos.pop()

    # grid[int(snake_head.y)][int(snake_head.x)] = "s0"
'''

'''
def draw_snake():
    for i in range(segments):
        pygame.draw.rect(surface=screen,
                    color=COLOR_RED,
                    rect=pygame.Rect(snake_pos[i].x * TILE_SIZE,
                                    snake_pos[i].y * TILE_SIZE,
                                    TILE_SIZE,
                                    TILE_SIZE))
'''

def draw_gridlines():
    
    for pixel_x in range(0, c.SCREEN_WIDTH, c.TILE_SIZE):
        pygame.draw.line(surface = screen,color = c.COLOR_BLACK,start_pos=(pixel_x,0),end_pos=(pixel_x, c.SCREEN_HEIGHT))
        
    for pixel_y in range(0,c.SCREEN_HEIGHT, c.TILE_SIZE):
        pygame.draw.line(surface = screen, color = c.COLOR_BLACK, start_pos = (0, pixel_y), end_pos=(c.SCREEN_WIDTH, pixel_y))

# TODO randomize start position
start_x = random.randrange(c.GRID_WIDTH)
start_y = random.randrange(c.GRID_HEIGHT)

# randomize start direction
left_max = c.EDGE_ZONE
right_min = c.GRID_WIDTH - c.EDGE_ZONE
top_max = c.EDGE_ZONE
bottom_min = c.GRID_HEIGHT - c.EDGE_ZONE
dir_all =[c.DIR_DOWN, c.DIR_LEFT, c.DIR_RIGHT, c.DIR_UP]

while True:
    start_dir = dir_all[random.randrange(len(dir_all))] 

    # if we start in the left edge zone and we start facing left...
    if start_x <= left_max and start_dir == c.DIR_LEFT:
        continue # ...Repick starting dir
    # otherwise, if we start in the right edge zone and we start facing right...
    elif start_x >= right_min and start_dir == c.DIR_RIGHT:
        continue 
    # if we start in the top edge zone and we start facing up...
    if start_y <= top_max and start_dir == c.DIR_UP:
        continue
    #otherwise, if we start in the bottom edge zone and we start facing down...
    elif start_y >= bottom_min and start_dir == c.DIR_DOWN:
        continue 

    break

# create snake
player_snake = snake.Snake(start_x, start_y, start_dir)
all_pos_in_list = player_snake.pos

foodmanager = foodstuff.FoodManager()
foodmanager.create_food()

#Maiin game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #part 1: update
    player_snake.update()
    
	#part 2: draw
    draw_gridlines()
    player_snake.draw(screen)
    foodmanager.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(15)  # limits FPS to 60

pygame.quit()