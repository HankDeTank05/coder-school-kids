# python import #
import math
import copy

# other people's code
import pygame

# my code
import common as c

# setup stuff
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
delta_time = 0 # time it takes to render a frame

# game variables
P_WIDTH = SCREEN_WIDTH * 0.05 #5% OF SCREEN WIDTH
P_HEIGHT = SCREEN_HEIGHT * 0.25 #25% OF SCREEN HEIGHT
P_EDGE_DISTANCE = 10 # NUMBER OF PIXELS BACK EDGE OF PADDLE IS AWAY FROM EDGE OF SCREEN
p1_paddle = pygame.Rect(P_EDGE_DISTANCE, 0, P_WIDTH, P_HEIGHT)
p2_paddle = pygame.Rect(SCREEN_WIDTH - (P_WIDTH + P_EDGE_DISTANCE), 0, P_WIDTH, P_HEIGHT)
paddle_speed = 1000
paddle_bounds_top = 0
paddle_bounds_bottom = SCREEN_HEIGHT - P_HEIGHT

# score variables #
p1_score = 0
p2_score = 0

# ball variables #
ball_center = pygame.math.Vector2()
ball_radius = 20
ball_speed = 50
ball_dir = pygame.math.Vector2(ball_speed, ball_speed)
# Ball boundries variables #
ball_bounds_top = 0 + ball_radius
ball_bounds_bottum = SCREEN_HEIGHT - ball_radius
ball_bounds_left = SCREEN_WIDTH - ball_radius
ball_bounds_right = 0 + ball_radius

def put_ball_in_center():
    global ball_center
    ball_center = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def set_ball_dir(dir_x, dir_y):
    global ball_dir
    ball_dir = pygame.math.Vector2(dir_x, dir_y) # resets the speed and direction of the ball #

def reset_ball(dir_x, dir_y):
    put_ball_in_center()
    set_ball_dir(dir_x, dir_y)
    

def move_paddle(keys, paddle, up_key, down_key):
    # read keys #
    if keys[up_key] == True:
        paddle.move_ip(0, -paddle_speed * delta_time)
    if keys[down_key] == True:
        paddle.move_ip (0, paddle_speed * delta_time)

    # boundry check #
    # prevent the paddle from going offscreen #
    if paddle.y < paddle_bounds_top:
        paddle.y = paddle_bounds_top
    elif paddle.y > paddle_bounds_bottom:
        paddle.y = paddle_bounds_bottom

def ball_collision(circle_center, circle_radius, rect):
    clamped_center = copy.deepcopy(circle_center)
    # clamp circle center inside of rect #
    if clamped_center.x < rect.x:
        clamped_center.x = rect.x
    elif clamped_center.x > rect.x + rect.width:
        clamped_center.x = rect.x + rect.width
    if clamped_center.y < rect.y:
        clamped_center.y = rect.y
    elif clamped_center.y > rect.y + rect.height:
        clamped_center.y = rect.y + rect.height

    x_dist = circle_center.x - clamped_center.x
    y_dist = circle_center.y - clamped_center.y

    distance = math.sqrt((x_dist ** 2) + (y_dist ** 2))
    return distance <= circle_radius

def move_ball():
    global ball_center
    #makes the ball move#
    ball_center = ball_center + (ball_dir * delta_time)

    # boundary check x #

    if ball_center.x < ball_bounds_right: # this code code checks if the ball has hit the right of the screen
        # ball_center.x = ball_bounds_right # this code doesn't let it go off of the screen (right)
        # ball_dir.x = ball_dir.x * (-1) # this code makes it bounce off the right of the screen
        reset_ball(ball_speed, ball_speed)
        # TODO: eventually we need to give player 1 a point (code goes here)
    elif ball_center.x > ball_bounds_left: # this code checks if the ball has hit the left of the screen
        # ball_center.x = ball_bounds_left # this code doesn't let it go off of the screen (left)
        # ball_dir.x = ball_dir.x * (-1) # this code makes it bounce off the left of the screen
        reset_ball(ball_speed, ball_speed)
        # TODO: eventually we need to give player 2 a point (code goes here)
    
    # boundry check y #
    if ball_center.y < ball_bounds_top: # this code code checks if the ball has hit the top of the screen
        ball_center.y = ball_bounds_top # this code doesn't let it go off of the screen (top)
        ball_dir.y = ball_dir.y * (-1) # this code makes it bounce off the top of the screen
    elif ball_center.y > ball_bounds_bottum: # this code checks if the ball has hit the bottom of the screen
        ball_center.y = ball_bounds_bottum # this code doesn't let it go off of the screen (bottom)
        ball_dir.y = ball_dir.y * (-1) # this code makes it bounce off the bottom of the screen

# center the ball before the game starts
put_ball_in_center()

# main game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(c.BLACK)
    ##################
    # step 1: update #
    ##################

    keys = pygame.key.get_pressed()
    move_paddle(keys, p1_paddle, pygame.K_w, pygame.K_s)
    move_paddle(keys, p2_paddle, pygame.K_UP, pygame.K_DOWN)
    move_ball()

    # check if the ball collided with paddle 1
    if ball_collision(ball_center, ball_radius, p1_paddle) == True:
        ball_center.x = p1_paddle.x + p1_paddle.width + ball_radius
        set_ball_dir(ball_dir.x * -1.1, ball_dir.y * 1.1)
        #ball_dir.x = ball_dir.x * -1.1
        # TODO: increase ball speed

    # otherwise, check if the ball collided with paddle 2
    elif ball_collision(ball_center, ball_radius, p2_paddle) == True:
        ball_center.x = p2_paddle.x - ball_radius
        set_ball_dir(ball_dir.x * -1.1, ball_dir.y * 1.1)
        #ball_dir.x = ball_dir.x * -1.1
        # TODO: increase ball speed

    ################
    # step 2: draw #
    ################
    
    # draw p1's paddle
    pygame.draw.rect(SCREEN, c.WHITE, p1_paddle)

    # draw p2's paddle
    pygame.draw.rect(SCREEN, c.WHITE, p2_paddle)

    pygame.draw.circle(SCREEN, c.WHITE, ball_center, ball_radius)

    pygame.display.flip()

    delta_time = clock.tick() / 1000

pygame.quit()
