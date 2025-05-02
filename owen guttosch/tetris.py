import pgzrun
import pygame
import random

SQUARE_SIZE = 20

TILE_WIDTH = 20
TILE_HEIGHT = 40

WIDTH = TILE_WIDTH * SQUARE_SIZE
HEIGHT = TILE_HEIGHT * SQUARE_SIZE

BACKGROUND_COLOR = (10, 115, 2)

GRAY = (128, 128, 128)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (97, 95, 18)
BLUE = (0, 0, 128)
LIGHT_BROWN = (182, 145, 131)
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

"""
DEBUG FUNCTIONS
"""

def print_2d_list(list_2d):
    for y in range(len(list_2d)):
        print(f"row {y} = ", end=' ')
        for x in range(len(list_2d[y])):
            if list_2d[y][x] is None:
                print("*", end=' ')
            else:
                print("X", end=' ')
        print()

"""
TETRIS FUNCTIONS
"""

def make_tetro():
    #              0    1    2    3    4    5    6
    tetrominos = ['t', 'o', 's', 'z', 'l', 'j', 'i']
    choice = random.randint(0, len(tetrominos) - 1)
    print(choice)
    global tetro, tetro_pos, tetro_rot, tetro_color
    center_x = TILE_WIDTH // 2
    tetro[0] = Rect((center_x * SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE))
    tetro_pos = pygame.math.Vector2(15,0)
    if tetrominos[choice] == 't':
        tetro[1] = Rect((center_x * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect(((center_x - 1) * SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect(((center_x + 1) * SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = PURPLE
    elif tetrominos[choice] == 'o':
        tetro[1] = Rect(((center_x + 1) * SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((center_x * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect(((center_x + 1) * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = BLACK
    elif tetrominos[choice] == 's':
        tetro[1] = Rect(((center_x + 1) * SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((center_x * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect(((center_x - 1) * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = YELLOW
    elif tetrominos[choice] == 'z':
        tetro[1] = Rect(((center_x - 1) * SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((center_x * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect(((center_x + 1) * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_color = LIGHT_BLUE
    elif tetrominos[choice] == 'l':
        tetro[1] = Rect((center_x * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((center_x * SQUARE_SIZE, 2 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect(((center_x + 1) * SQUARE_SIZE, 2 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_pos = pygame.math.Vector2(15,1)
        tetro_color = BLUE
    elif tetrominos[choice] == 'j':
        tetro[1] = Rect((center_x * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((center_x * SQUARE_SIZE, 2 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect(((center_x - 1) * SQUARE_SIZE, 2 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_pos = pygame.math.Vector2(15,1)
        tetro_color = DARK_YELLOW
    elif tetrominos[choice] == 'i':
        tetro[1] = Rect((center_x * SQUARE_SIZE, 1 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[2] = Rect((center_x * SQUARE_SIZE, 2 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro[3] = Rect((center_x * SQUARE_SIZE, 3 * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
        tetro_pos = pygame.math.Vector2(15,1)
        tetro_color = LIGHT_BROWN
    tetro_rot = 0


"""
BLOCK MOVEMENT FUNCTIONS
"""

def place_on_board():
    # place the tetromino on the board
    for i in range(4):
        pos = pygame.math.Vector2(tetro[i].x / SQUARE_SIZE, tetro[i].y / SQUARE_SIZE)
        grid[int(pos.y)][int(pos.x)] = tetro[i]
    # check if it's time to clear a line
    lines_to_clear = []
    for row in range(len(grid)):
        tiles_filled = 0
        for col in range(len(grid[row])):
            if grid[row][col] is not None: # if the current cell is not empty, increase the counter
                tiles_filled += 1
        if tiles_filled == len(grid[row]): # if the current row is completely filled, add the row index to the list of lines to clear
            lines_to_clear.append(row)
    
    while len(lines_to_clear) > 0:
        current_row = lines_to_clear[0]
        lines_to_clear.pop(0)
        # step 1: clear the line
        for x in range(len(grid[current_row])):
            grid[current_row][x] = None
        # step 2: bring all the above lines down by one row
        for y in range(current_row - 1, -1, -1):
            grid[y+1] = grid[y]
            # TODO: come back and move the rectangles down so that it draws properly (code)

    print_2d_list(grid)

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
        grid_x = tetro[i].x // SQUARE_SIZE
        grid_y = tetro[i].y // SQUARE_SIZE
        # check if on left edge of screen or if grid space to the left is not empty
        if tetro[i].x <= 0 or grid[grid_y][grid_x - 1] is not None:
            can_move_left = False
            break            
    if can_move_left == True:
        # move left
        tetro_pos.x -= 1
        for i in range(4):
            tetro[i].move_ip(-SQUARE_SIZE, 0)

def block_move_right():
    can_move_right = True
    for i in range(4):
        grid_x = tetro[i].x // SQUARE_SIZE
        grid_y = tetro[i].y // SQUARE_SIZE
        # check if on right edge of screen or if grid space to the right is not empty
        if tetro[i].x >= WIDTH - SQUARE_SIZE or grid[grid_y][grid_x + 1] is not None:
            can_move_right = False
            break
    if can_move_right == True:
        #move right
        tetro_pos.x += 1
        for i in range(4):
            tetro[i].move_ip(SQUARE_SIZE, 0)

def block_rotate_left():
    global tetro_rot
    for i in range(4):
        #step 1: convert to local coordinates
        coords = pygame.math.Vector2(tetro[i].x // SQUARE_SIZE, tetro[i].y // SQUARE_SIZE)
        print(coords)
        coords -= tetro_pos
        print(coords)
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
            print(coords)
            tetro[i].update(coords, (SQUARE_SIZE, SQUARE_SIZE))
    tetro_rot -= 90
    if tetro_rot < 0:
        tetro_rot = 270

def block_rotate_right():
    global tetro_rot
    for i in range(4):
        #step 1: convert to local coordinates
        coords = pygame.math.Vector2(tetro[i].x // SQUARE_SIZE, tetro[i].y // SQUARE_SIZE)
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
            print(coords)
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
    #make sure that it's impossible to go off screen (left side)
    for i in range(4):
        while tetro[i].x < 0:
            block_move_right()
    #make sure that it's impossible to go off screen (right side)
    for i in range(4):
        while tetro[i].x >= WIDTH:
            block_move_left()

def draw():
    screen.fill(BACKGROUND_COLOR)

    #draws the grid
    for y in range(0, HEIGHT, SQUARE_SIZE):
        # draws the row of squares
        for x in range(0, WIDTH, SQUARE_SIZE):
            x_index = x//SQUARE_SIZE
            y_index = y//SQUARE_SIZE
            square = Rect((x, y), (SQUARE_SIZE, SQUARE_SIZE))
            if grid[y_index][x_index] is None:
                screen.draw.rect(square, (255, 255, 255))
            else:
                #screen.draw.filled_rect(grid[y_index][x_index], GRAY) # TODO: come back and make the grid remember the color of the
                screen.draw.filled_rect(square, GRAY)

    #draws the tetromino
    for i in range(4):
        screen.draw.filled_rect(tetro[i], tetro_color)
    

pgzrun.go()
