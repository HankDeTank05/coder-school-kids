import pgzrun
import random

# TODO make more buildings and windows
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FLORR_HEIGT = 275
ROAD_HEIRGHT = FLORR_HEIGT + 100
ROAD_WIDTH = 40

COLOR_SKY_DAY = (173,216,230)
COLOR_SKY_NIGHT = (16,12,8)

BUILDING_COUNT = 175
MIN_BUILD_H = 40
MAX_BUILD_H = 170
MIN_WIN_SPACE = 1
MAX_WIN_SPACE = 6

cybertruck = Actor('cybertruck_25_left')
cybertruck.pos = SCREEN_WIDTH/2, SCREEN_HEIGHT/2

background_move = 0

BLACK = (0, 0, 0)
YELLOW = (255,216,0)
OFF_BLACK = (51,51,51)
ROAD_BLACK = (35,43,43)
class Building:

    # constructor
    def __init__(self, x_pos, width, height, win_space):
        self.width = width
        self.height = height
        self.color = OFF_BLACK
        self.border = 3
        self.rect = Rect((x_pos, FLORR_HEIGT - self.height), (self.width, self.height))
        self.win_space = win_space
        self.win_width = 4
        self.win_height = 4
        self.win_color = YELLOW

    def update(self, _background_move):
        self.rect.move_ip(_background_move, 0)
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH - 1
        elif self.rect.left > SCREEN_WIDTH - 1:
            self.rect.right = 0

    def draw(self):
        # draw the building
        screen.draw.filled_rect(self.rect, self.color)

        for y in range(self.border, self.height - self.border, self.win_space + self.win_height):
            # draw one row of windows
            for x in range(self.border, self.width - self.border, self.win_space + self.win_width):
                # this draws a single window
                window_rect = Rect((self.rect.x + x, self.rect.y + y), (self.win_width, self.win_height))
                screen.draw.filled_rect(window_rect, self.win_color)

building_width = 50
building_height = 175
building_color = OFF_BLACK
building_border = 3
window_spacing = 4
window_width = 4
window_height = 4
window_color = YELLOW
key_building = Rect((SCREEN_WIDTH/2, 125), (building_width, building_height))

#building2 = Building(width = 50, height  = 175)
buildigds = []
for b in range(BUILDING_COUNT):
    building_x = random.randrange(0,SCREEN_WIDTH)
    building_width = 50
    building_height = random.randrange(MIN_BUILD_H, MAX_BUILD_H)
    win_space = random.randrange(MIN_WIN_SPACE, MAX_WIN_SPACE)
    building = Building(x_pos = building_x, width = building_width, height = building_height, win_space = win_space)
    buildigds.append(building)

'''
IDEAS
- make a road for it to drive on
- have it pass villages every so often
- it's an uber, so it stops to pick up people
- put music in
- make nighttime a thing
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
    #building2.update(background_move)
    for build in buildigds:
        build.update(background_move)

def draw():
    screen.fill(COLOR_SKY_NIGHT)

    #building2.draw()
    for build in buildigds:
        build.draw()

    # draw the road
    road = Rect(0, ROAD_HEIRGHT - ROAD_WIDTH/2, SCREEN_WIDTH, ROAD_WIDTH)
    screen.draw.filled_rect(road, ROAD_BLACK)

    # draw the cybertruck
    cybertruck.draw()

pgzrun.go()