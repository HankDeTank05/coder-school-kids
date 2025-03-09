# Example file showing a basic pygame "game loop"
import pygame

GRID_WIDTH = 160
GRID_HEIGHT = 90
TILE_SIZE = 5
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE

COLOR_BLACK = (0,0,0)
COLOR_RED = (155,0,0)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

snake = list()
grid = []

for y in range(GRID_HEIGHT):
    grid.append([])
    for x in range(GRID_WIDTH):
        grid[y].append(None)
        
segments = 5
snake_start = pygame.math.Vector2(GRID_WIDTH //2,GRID_HEIGHT //2)
snake_pos = []
for i in range(segments):
    snake_pos.append(snake_start + pygame.math.Vector2(0, i))
    print(snake_pos[i])

# grid[int(snake_head.y)][int(snake_head.x)] = "s0"
dir_up = pygame.math.Vector2(0, -1)
dir_down = pygame.math.Vector2(0, 1)
dir_left = pygame.math.Vector2(-1, 0)
dir_right = pygame.math.Vector2(1, 0)

snake_dir = pygame.math.Vector2(0,-1)

move_queue = []

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
        if keys[pygame.K_d] == True and snake_dir != dir_left:
            snake_dir = dir_right
    else:# there is somthing left in move_queue
        snake_dir = move_queue[0]
        move_queue.pop(0)

    # grid[int(snake_head.y)][int(snake_head.x)] = None

    # snake_head = snake_head + snake_dir
    snake_head = snake_pos[0] + snake_dir # calculate new head pos
    snake_pos.insert(0, snake_head)
    snake_pos.pop()

    # grid[int(snake_head.y)][int(snake_head.x)] = "s0"
    
def draw_snake():
    for i in range(segments):
        pygame.draw.rect(surface=screen,
                    color=COLOR_RED,
                    rect=pygame.Rect(snake_pos[i].x * TILE_SIZE,
                                    snake_pos[i].y * TILE_SIZE,
                                    TILE_SIZE,
                                    TILE_SIZE))

def draw_gridlines():
    
    for pixel_x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(surface = screen,color = COLOR_BLACK,start_pos=(pixel_x,0),end_pos=(pixel_x,SCREEN_HEIGHT))
        
    for pixel_y in range(0,SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(surface = screen, color = COLOR_BLACK, start_pos = (0, pixel_y), end_pos=(SCREEN_WIDTH,pixel_y))

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
    snake_update()
    
	#part 2: draw
    draw_gridlines()
    draw_snake()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(15)  # limits FPS to 60

pygame.quit()