# language imports
import random
import math

# Example file showing a basic pygame "game loop"
import pygame

import paddle as p

######################
# CONSTANT VARIABLES #
######################

# screen variables
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# paddle variables
PADDLE_WIDTH = 30
PADDLE_HEIGHT = SCREEN_HEIGHT * 0.25
PADDLE_SPEED = 300

# ball variables
BALL_RADIUS = 15
BALL_SPEED = 409

# colors
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

##################
# math functions #
##################

def clamp(value_to_clamp, range_min, range_max):
    if value_to_clamp > range_max:
        return range_max
    elif value_to_clamp < range_min:
        return range_min
    else :
        return value_to_clamp
    
def collide_circle_rect(rect: pygame.Rect, circle_center: pygame.math.Vector2, circle_radius: int|float) -> bool:
    clamp_x = clamp(circle_center.x, rect.left, rect.right)
    clamp_y = clamp(circle_center.y, rect.top, rect.bottom)
    clamp_point = pygame.math.Vector2(clamp_x, clamp_y)
    a = circle_center.x - clamp_point.x
    b = circle_center.y - clamp_point.y
    distance = math.sqrt(a**2 + b**2)
    overlap = distance <= circle_radius
    return overlap


################
# game classes #
################

class Paddle:

    # constructor
    def __init__(self, start_pos: pygame.math.Vector2, color: pygame.Color, up_key: int, down_key: int):
        self.rect = pygame.Rect(start_pos, pygame.math.Vector2(PADDLE_WIDTH, PADDLE_HEIGHT))
        self.color = color
        self.upkey = up_key
        self.downkey = down_key

    def update(self, frame_time, keys):
        
        # movement
        if keys[self.upkey] == True:
            self.rect.y -= PADDLE_SPEED * frame_time
        if keys[self.downkey] == True:
            self.rect.y += PADDLE_SPEED * frame_time

        # boundaries
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT-1:
            self.rect.bottom = SCREEN_HEIGHT -1

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Ball:

    # constructor
    def __init__(self):
        self.pos = None
        self.dir = None
        self.reset()
        self.radius = BALL_RADIUS
        self.speed = BALL_SPEED
        self.color = WHITE

    def update(self, frame_time, left_paddle: pygame.Rect, right_paddle: pygame.Rect):
        # check if ball needs to bounce

        # check is at top of screen    check if it is at bottom of screen
        #  vvvvvvvvvvvvvvvvvvvvvvvv    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        if self.pos.y < self.radius or self.pos.y > SCREEN_HEIGHT - 1 - self.radius:
            self.dir.y *= -1

        # check if collided with p1 paddle                            check if collide with p2 paddle
        #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        if collide_circle_rect(left_paddle, self.pos, self.radius) or collide_circle_rect(right_paddle, self.pos, self.radius):
            self.dir.x *= -1

        # move the ball
        self.pos += self.dir * self.speed * frame_time

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def reset(self):
        #puts the ball in the middle of the screen
        self.pos = pygame.math.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        #picks a random direction
        random_x = random.choice([-1, 1])
        random_y = random.choice([-1, 1])
        self.dir = pygame.math.Vector2(random_x, random_y)
        self.dir.normalize_ip()



################
# pygame setup #
################

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
frame_time = 0

##################
# game variables #
##################

# paddle vars
paddle_start_height = SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2
p1_paddle = Paddle(pygame.math.Vector2(0, paddle_start_height), RED, pygame.K_w, pygame.K_s)
p2_paddle = Paddle(pygame.math.Vector2(SCREEN_WIDTH - PADDLE_WIDTH, paddle_start_height), BLUE, pygame.K_UP, pygame.K_DOWN)

# ball vars
ball = Ball()

#screen vars
screen_rect = pygame.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

#################
# the game code #
#################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)

    # RENDER YOUR GAME HERE

    ##################
    # STEP 1: UPDATE #
    ##################

    keys = pygame.key.get_pressed()
    p1_paddle.update(frame_time, keys)
    p2_paddle.update(frame_time, keys)
    ball.update(frame_time, p1_paddle.rect, p2_paddle.rect)
    if collide_circle_rect(screen_rect,ball.pos,ball.radius) == False:
        ball.reset()

    ################
    # STEP 2: DRAW #
    ################

    p1_paddle.draw()
    p2_paddle.draw()
    ball.draw()


    # flip() the display to put your work on screen
    pygame.display.flip()

    frame_time = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()