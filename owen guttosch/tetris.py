import pgzrun
import pygame
import random

SQUARE_SIZE = 10

TILE_WIDTH = 30
TILE_HEIGHT = 40

WIDTH = TILE_WIDTH * SQUARE_SIZE
HEIGHT = TILE_HEIGHT * SQUARE_SIZE

BACKGROUND_COLOR = (10, 115, 2)

GRAY = (128, 128, 128)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 128)
LIGHT_BLUE = (135, 206, 250)

grid = []

for y in range(TILE_HEIGHT):
    grid.append([])
    for x in range(TILE_WIDTH):
        grid[y].append(None)

print(len(grid))
print(len(grid[0]))

tetro = [None, None, None, None]
tetro_pos = pygame.math.Vector2(15,0)
tetro_rot = 0
tetro_color = None

down_held = False

def make_tetro():
    #              0    1    2    3    4    5    6
    tetrominos = ['t', 'o', 's', 'z', 'l', 'j', 'i']
    choice = random.randint(0, len(tetrominos) - 1)
    print(choice)
    global tetro, tetro_pos, tetro_rot, tetro_color
    tetro[0] = Rect((150, 0), (SQUARE_SIZE, SQUARE_SIZE))
    if tetrominos[choice] == 't':
        tetro[1] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((140, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((160, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = PURPLE
    elif tetrominos[choice] == 'o':
        tetro[1] = Rect((160, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((160, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = BLACK
    elif tetrominos[choice] == 's':
        tetro[1] = Rect((160, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((140, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = BLACK
    elif tetrominos[choice] == 'z':
        tetro[1] = Rect((140, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((160, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = BLACK
    elif tetrominos[choice] == 'l':
        tetro[0] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[1] = Rect((150, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((150, 20), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((160, 20), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = BLACK
    elif tetrominos[choice] == 'j':
        tetro[0] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[1] = Rect((150, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((150, 20), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((140, 20), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = BLACK
    elif tetrominos[choice] == 'i':
        tetro[0] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[1] = Rect((150, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((150, 20), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((150, 30), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = BLACK
    tetro_pos = pygame.math.Vector2(15,0)
    tetro_rot = 0


"""
BLOCK MOVEMENT FUNCTIONS
"""

def place_on_board():

    for i in range(4):
        pos = pygame.math.Vector2(tetro[i].x / SQUARE_SIZE, tetro[i].y / SQUARE_SIZE)
        grid[int(pos.y)][int(pos.x)] = tetro[i]

def block_fall(schedule = True):
    canfall = True
    for i in range(4):
        x_index = tetro[i].x//SQUARE_SIZE
        y_index = tetro[i].y//SQUARE_SIZE
        if tetro[i].y >= HEIGHT-SQUARE_SIZE or grid[y_index+1][x_index] is not None:
            canfall = False
            break
    if canfall == False: #check if t2 can move down
        # don't fall
        place_on_board()
        make_tetro()
    else:
        # fall
        tetro_pos.y += 1
        for i in range(4):
            tetro[i].move_ip(0, SQUARE_SIZE)
    if schedule == True:
        clock.schedule(block_fall, 0.5)

def block_move_left():
    can_move_left = True
    for i in range(4):
        if tetro[i].x <= 0:
            can_move_left = False
            break
    if can_move_left == False:
        # don'tetro move left
        pass
    else:
        # move left
        tetro_pos.x -= 1
        for i in range(4):
            tetro[i].move_ip(-SQUARE_SIZE, 0)

def block_move_right():
    can_move_right = True
    for i in range(4):
        if tetro[i].x >= WIDTH - SQUARE_SIZE:
            can_move_right = False
            break
    if can_move_right == False:
        # don'tetro move right
        pass
    else:
        #move right
        tetro_pos.x += 1
        for i in range(4):
            tetro[i].move_ip(SQUARE_SIZE, 0)

def block_rotate_left():
    global tetro_rot
    for i in range(4):
        #step 1: convert to local coordinates
        coords = pygame.math.Vector2(tetro[i].left // SQUARE_SIZE, tetro[i].top // SQUARE_SIZE)
        coords -= tetro_pos
        if coords != pygame.math.Vector2(0,0):
            #step 2: rotate
            coords.x *= -1 #negate
            print(coords)
            # swap x/y
            temp = coords.x
            coords.x = coords.y
            coords.y = temp
            print(coords)
            #step 3: convert back to screen pixels
            coords += tetro_pos
            coords *= SQUARE_SIZE
            tetro[i].update(coords, (SQUARE_SIZE, SQUARE_SIZE))
    tetro_rot -= 90
    if tetro_rot < 0:
        tetro_rot = 270

def block_rotate_right():
    global tetro_rot
    for i in range(4):
        #step 1: convert to local coordinates
        coords = pygame.math.Vector2(tetro[i].left // SQUARE_SIZE, tetro[i].top // SQUARE_SIZE)
        coords -= tetro_pos
        if coords != pygame.math.Vector2(0,0):
            # step 2: rotate
            coords.y *= -1 #n-e-g-a-tetro-e
            print(coords)
            # swap x/y
            temp = coords.x
            coords.x = coords.y
            coords.y = temp
            print(coords)
            #step 3: convert back to screen pixels
            coords += tetro_pos
            coords *= SQUARE_SIZE
            tetro[i].update(coords, (SQUARE_SIZE, SQUARE_SIZE))
    tetro_rot += 90
    if tetro_rot > 270:
        tetro_rot = 0
            
            
    
        
"""
EVENT HOOKS
"""

def on_key_down(key):
    if key == keys.LEFT:
        block_move_left()
    elif key == keys.RIGHT:
        block_move_right()
    elif key == keys.DOWN:
        global down_held
        down_held = True
    elif key == keys.Z:
        block_rotate_left()
    elif key == keys.X:
        block_rotate_right()

def on_key_up(key):
    if key == keys.DOWN:
        global down_held
        down_held = False

# start the game
make_tetro()
clock.schedule(block_fall, 0.5)

def update():
    if down_held == True:
        block_fall(False)

def draw():
    screen.fill(BACKGROUND_COLOR)

    #draws the grid
    for y in range(0, HEIGHT, SQUARE_SIZE):
        # draws the row of squares
        for x in range(0, WIDTH, SQUARE_SIZE):
            x_index = x//SQUARE_SIZE
            y_index = y//SQUARE_SIZE
            if grid[y_index][x_index] is None:
                square = Rect((x, y), (SQUARE_SIZE, SQUARE_SIZE))
                screen.draw.rect(square, (255, 255, 255))
            else:
                screen.draw.filled_rect(grid[y_index][x_index], GRAY) # TODO: come back and make the grid remember the color of the tetrominos

    #draws the tetromino
    for i in range(4):
        screen.draw.filled_rect(tetro[i], tetro_color)
    

pgzrun.go()
