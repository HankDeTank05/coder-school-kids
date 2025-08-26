import pgzrun

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOR_SKY_DAY = (173,216,230)
COLOR_SKY_NIGHT = (0,33,71)

cybertruck = Actor('cybertruck_25_left')
cybertruck.pos = SCREEN_WIDTH/2, SCREEN_HEIGHT/2

background_move = 0
building = Rect((SCREEN_WIDTH/2, 125), (50, 175))

window_spacing = 2
window_width = 4

'''
IDEAS
- make a road for it to drive on
- have it pass villages every so often
- it's an uber, so it stops to pick up people
- put music in
'''

def on_key_down(key):
    global background_move
    if key == keys.LEFT:
        cybertruck.image = 'cybertruck_25_left'
        background_move = 1
    if key == keys.RIGHT:
        cybertruck.image = 'cybertruck_25_right'
        background_move = -1

def on_key_up(key):
    global background_move
    if key == keys.LEFT:
        background_move = 0
    if key == keys.RIGHT:
        background_move = 0

def update():
    building.move_ip(background_move, 0)
    # TODO: make the buildings in the background loop
    if building.right < 0:
        building.left = SCREEN_WIDTH - 1
    elif building.left > SCREEN_WIDTH - 1:
        building.right = 0

def draw():
    screen.fill(COLOR_SKY_DAY)

    # draw the building
    screen.draw.filled_rect(building, (128, 128, 128))
    # draw one row of windows
    # TODO: fix the windows going off the right edge of the building
    for x in range(0, 50, window_spacing + window_width):
        window_rect = Rect((building.x + x, building.y), (window_width, window_width))
        screen.draw.filled_rect(window_rect, (0, 0, 0))
    # TODO: draw multiple rows of windows

    # draw the cybertruck
    cybertruck.draw()

pgzrun.go()