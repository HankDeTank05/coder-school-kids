# Example file showing a basic pygame "game loop"
import pygame

##################################################
# CONSTANT VARIABLES (these should never change) #
##################################################

# game constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# stage constants
FLOOR_HEIGHT = 690

# player constants
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100

# color constants
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

################
# pygame setup #
################

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

################
# GAME CLASSES #
################

class Fighter:

    # constructor
    def __init__(self, starting_pstn: pygame.math.Vector2, speed: float, left_key, right_key):
        self._max_hp = 300
        self._current_hp = self._max_hp

        self._max_meter = 100
        self._current_meter = self._max_meter

        self._current_pstn = starting_pstn
        self._speed = speed
        size = pygame.math.Vector2(PLAYER_WIDTH, PLAYER_HEIGHT)
        self._rect = pygame.Rect(self._current_pstn, size)

        self._left_key = left_key
        self._right_key = right_key
        
    def update(self, _keys):
        self._current_pstn.y += 10
        
        # this code helps them stand on the floor
        if self._current_pstn.y > FLOOR_HEIGHT:
            self._current_pstn.y = FLOOR_HEIGHT

        # this code reads input
        if _keys[self._left_key]:
            self._current_pstn.x -= self._speed #  go left
        if _keys[self._right_key]:
            self._current_pstn.x += self._speed # go right

        self._rect.midbottom = self._current_pstn

        # this code makes sure they don't go off screen
        if self._rect.left < 0:
            self._rect.left = 0
        
        if self._rect.right > SCREEN_WIDTH - 1:
            self._rect.right =  SCREEN_WIDTH - 1

        self._current_pstn = pygame.math.Vector2(self._rect.midbottom)

    
    def draw(self):
        pygame.draw.rect(SCREEN, WHITE, self._rect)

        pygame.draw.circle(SCREEN, RED, self._current_pstn, 7, 1)
        pygame.draw.circle(SCREEN, RED, self._current_pstn, 3)

##################
# GAME VARIABLES #
##################

p1 = Fighter(starting_pstn=pygame.math.Vector2(x = 50, y = 100),                    speed=50,   left_key=pygame.K_a,    right_key= pygame.K_d)
p2 = Fighter(starting_pstn=pygame.math.Vector2(x = SCREEN_WIDTH - 100, y = 100),    speed=50,   left_key = pygame.K_LEFT,   right_key=pygame.K_RIGHT)

##################
# MAIN GAME LOOP #
##################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ##################
    # STEP 1: UPDATE #
    ##################

    keys = pygame.key.get_pressed()
    p1.update(keys)
    p2.update(keys)

    ################
    # STEP 2: DRAW #
    ################

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill(BLACK)

    p1.draw()
    p2.draw()

    # TEMPORARILY draw a line for where the floor is
    floor_line_start = pygame.math.Vector2(0, FLOOR_HEIGHT)
    floor_line_end = pygame.math.Vector2(SCREEN_WIDTH, FLOOR_HEIGHT)
    pygame.draw.line(SCREEN, (255, 255, 255), floor_line_start, floor_line_end)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
