# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 12) # credit: https://www.geeksforgeeks.org/python/python-display-text-to-pygame-window/

corner_points = [
    pygame.math.Vector2(0, 0),
    pygame.math.Vector2(SCREEN_WIDTH - 1, 0),
    pygame.math.Vector2(0, SCREEN_HEIGHT - 1),
    pygame.math.Vector2(SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)
]

def draw_point(pos: pygame.math.Vector2):
    # draw a little red dot at the chosen point
    pygame.draw.circle(SCREEN, RED, mouse_pos, 1)
    # draw a red circle around the point for visibility
    pygame.draw.circle(SCREEN, RED, mouse_pos, 10, width=1)

    # create the text
    text = font.render(f"({pos.x}, {pos.y})", True, RED, BLACK)
    text_rect = text.get_rect()
    text_rect.center = pos + pygame.math.Vector2(0, -15)
    
    # prevent the text from going off screen
    while text_rect.left < 0:
        text_rect.left += 1
    while text_rect.right >= SCREEN_WIDTH:
        text_rect.right -= 1
    while text_rect.top < 0:
        text_rect.top += 1
    while text_rect.bottom >= SCREEN_HEIGHT:
        text_rect.bottom -= 1
    
    # draw text on screen
    SCREEN.blit(text, text_rect)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill(BLACK)    

    ##########
    # UPDATE #
    ##########

    # get mouse position
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())

    ########
    # DRAW #
    ########

    for point in corner_points:
        draw_point(point)
    draw_point(mouse_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()