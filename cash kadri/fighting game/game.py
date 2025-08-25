# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

##################################################
# CONSTANT VARIABLES (these should never change) #
##################################################

FLOOR_HEIGHT = 690

################
# GAME CLASSES #
################

class Fighter:

    # constructor
    def __init__(self, starting_pstn: pygame.math.Vector2, speed: float):
        self._max_hp = 300
        self._current_hp = self._max_hp
        self._max_meter = 100
        self._current_meter = self._max_meter
        self._current_pstn = starting_pstn
        self._speed = speed
        
    def update(self):
        self._current_pstn.y += 10
        # TODO: next time, we need to make sure we don't fall through the floor
    
    def draw(self):
        size = pygame.math.Vector2(50, 100)
        rect = pygame.Rect(self._current_pstn, size)
        pygame.draw.rect(SCREEN, (255, 255, 255), rect)

##################
# GAME VARIABLES #
##################

p1 = Fighter(starting_pstn=pygame.math.Vector2(x = 50, y = 100), speed=100)
p2 = Fighter(starting_pstn=pygame.math.Vector2(x = SCREEN_WIDTH - 100, y = 100), speed=250)

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

    p1.update()
    p2.update()

    ################
    # STEP 2: DRAW #
    ################

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill("purple")

    p1.draw()
    p2.draw()

    # TEMPORARILY draw a line for where the floor is
    floor_line_start = pygame.math.Vector2(0, FLOOR_HEIGHT)
    floor_line_end = pygame.math.Vector2(SCREEN_WIDTH, FLOOR_HEIGHT)
    pygame.draw.line(SCREEN, (255, 255, 255), floor_line_start, floor_line_end)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()
