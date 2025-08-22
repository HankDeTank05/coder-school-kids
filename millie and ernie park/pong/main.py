# Example file showing a basic pygame "game loop"
import pygame

import common as c
import paddle as p

# pygame setup
pygame.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
frame_time = 0

paddle_start_height = c.SCREEN_HEIGHT/2 - c.PADDLE_HEIGHT/2

p1_paddle = p.Paddle(pygame.math.Vector2(0, paddle_start_height), c.RED, pygame.K_w, pygame.K_s)
p2_paddle = p.Paddle(pygame.math.Vector2(c.SCREEN_WIDTH - c.PADDLE_WIDTH, paddle_start_height), c.BLUE, pygame.K_UP, pygame.K_DOWN)
# p2_paddle = pygame.Rect(c.SCREEN_WIDTH - c.PADDLE_WIDTH, paddle_start_height, c.PADDLE_WIDTH, c.PADDLE_HEIGHT)

ball_center = pygame.math.Vector2(c.SCREEN_WIDTH/2, c.SCREEN_HEIGHT/2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(c.BLACK)

    # RENDER YOUR GAME HERE

    # pygame.draw.rect(screen, c.RED, p1_paddle)
    p1_paddle.draw(screen)
    p2_paddle.draw(screen)
    # pygame.draw.rect(screen, c.BLUE, p2_paddle)

    pygame.draw.circle(screen, c.WHITE, ball_center, c.BALL_RADIUS)


    # flip() the display to put your work on screen
    pygame.display.flip()

    frame_time = clock.tick(60)  # limits FPS to 60

pygame.quit()