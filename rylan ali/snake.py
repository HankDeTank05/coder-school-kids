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
        
snake_head = pygame.math.Vector2(GRID_WIDTH //2,GRID_HEIGHT //2)
grid[int(snake_head.y)][int(snake_head.x)] = "s0"
snake_dir=pygame.math.Vector2(0,-1)

def snake_update():
    global snake_head
    global snake_dir
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s] == True:
        snake_dir=pygame.math.Vector2(0,1)
    grid[int(snake_head.y)][int(snake_head.x)] =None
    snake_head=snake_head+snake_dir
    grid[int(snake_head.y)][int(snake_head.x)] = "s0"
    
def draw_snake():
	pygame.draw.rect(surface=screen,color=COLOR_RED,rect=pygame.Rect(snake_head.x * TILE_SIZE,snake_head.y * TILE_SIZE,TILE_SIZE,TILE_SIZE))

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

    clock.tick(1)  # limits FPS to 60

pygame.quit()