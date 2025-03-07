
import pgzrun
import pygame

SQUARE_SIZE = 10

TILE_WIDTH = 30
TILE_HEIGHT = 40

WIDTH = TILE_WIDTH * SQUARE_SIZE
HEIGHT = TILE_HEIGHT * SQUARE_SIZE

PURPLE = (255, 0, 255)

grid = []

for y in range(TILE_HEIGHT):
    grid.append([])
    for x in range(TILE_WIDTH):
        grid[y].append(None)

print(len(grid))
print(len(grid[0]))

t = [None, None, None, None]
tpos = pygame.math.Vector2(15,0)
rot = 0

down_held = False

def make_t():
    global t, tpos, rot
    t[0] = Rect((150, 0), (SQUARE_SIZE, SQUARE_SIZE))
    t[1] = Rect((150, 10), (SQUARE_SIZE, SQUARE_SIZE))
    t[2] = Rect((140, 0), (SQUARE_SIZE, SQUARE_SIZE))
    t[3] = Rect((160, 0), (SQUARE_SIZE, SQUARE_SIZE))
    tpos = pygame.math.Vector2(15,0)
    rot = 0


"""
BLOCK MOVEMENT FUNCTIONS
"""

def place_on_board():

    for i in range(4):
        pos = pygame.math.Vector2(t[i].x / SQUARE_SIZE, t[i].y / SQUARE_SIZE)
        grid[int(pos.y)][int(pos.x)] = t[i]

def block_fall(schedule = True):
    canfall = True
    for i in range(4):
        x_index = t[i].x//SQUARE_SIZE
        y_index = t[i].y//SQUARE_SIZE
        if t[i].y >= HEIGHT-SQUARE_SIZE or grid[y_index+1][x_index] is not None:
            canfall = False
            break
    if canfall == False: #check if t2 can move down
        # don't fall
        place_on_board()
        make_t()
    else:
        # fall
        tpos.y += 1
        for i in range(4):
            t[i].move_ip(0, SQUARE_SIZE)
    if schedule == True:
        clock.schedule(block_fall, 0.5)

def block_move_left():
    can_move_left = True
    for i in range(4):
        if t[i].x <= 0:
            can_move_left = False
            break
    if can_move_left == False:
        # don't move left
        pass
    else:
        # move left
        tpos.x -= 1
        for i in range(4):
            t[i].move_ip(-SQUARE_SIZE, 0)

def block_move_right():
    can_move_right = True
    for i in range(4):
        if t[i].x >= WIDTH - SQUARE_SIZE:
            can_move_right = False
            break
    if can_move_right == False:
        # don't move right
        pass
    else:
        #move right
        tpos.x += 1
        for i in range(4):
            t[i].move_ip(SQUARE_SIZE, 0)

def block_rotate_left():
    global rot
    for i in range(4):
        #step 1: convert to local coordinates
        coords = pygame.math.Vector2(t[i].left // SQUARE_SIZE, t[i].top // SQUARE_SIZE)
        coords -= tpos
        if coords != pygame.math.Vector2(0,0):
            #step 2: rotate
            if rot == 0 or rot == 180:
                coords *= -1 #negate
            print(coords)
            # swap x/y
            temp = coords.x
            coords.x = coords.y
            coords.y = temp
            print(coords)
            #step 3: convert back to screen pixels
            coords += tpos
            coords *= SQUARE_SIZE
            t[i].update(coords, (SQUARE_SIZE, SQUARE_SIZE))
    rot -= 90
    if rot < 0:
        rot = 270

def block_rotate_right():
    global rot
    
        
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

def on_key_up(key):
    if key == keys.DOWN:
        global down_held
        down_held = False

# start the game
make_t()
clock.schedule(block_fall, 0.5)

def update():
    if down_held == True:
        block_fall(False)

def draw():
    screen.fill((1, 1, 1))

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
                screen.draw.filled_rect(grid[y_index][x_index], PURPLE)

    #draws the tetromino
    for i in range(4):
        screen.draw.filled_rect(t[i], PURPLE)
    

pgzrun.go()
