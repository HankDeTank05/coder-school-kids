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

ball_center = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
ball_radius = 20


def move_paddle(keys, paddle, up_key, down_key):
    # read keys #
    if keys[up_key] == True:
        paddle.move_ip(0, -paddle_speed * delta_time)
    if keys[down_key] == True:
        paddle.move_ip (0, paddle_speed * delta_time)

    # boundries #
    if paddle.y < paddle_bounds_top:
        paddle.y = paddle_bounds_top
    elif paddle.y > paddle_bounds_bottom:
        paddle.y = paddle_bounds_bottom


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
