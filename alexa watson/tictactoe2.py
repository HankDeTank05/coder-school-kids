# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# colors
LIGHT_SKY_BLUE = (135, 206, 250)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pygame.draw.line(screen, LIGHT_SKY_BLUE, (SCREEN_WIDTH/3, 0), (SCREEN_WIDTH/3, 300))
    pygame.draw.line(screen, LIGHT_SKY_BLUE, (SCREEN_WIDTH/3, 0), (SCREEN_WIDTH/3, 300))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()