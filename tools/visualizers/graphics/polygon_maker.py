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

# TODO: make it so that points can be added and removed from the polygon while the program is running

point_dist = 15

polygon_pts = [
    pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 0.1 * SCREEN_HEIGHT),
    pygame.math.Vector2(SCREEN_WIDTH / 2 - 0.1 * SCREEN_WIDTH, SCREEN_HEIGHT / 2 + 0.1 * SCREEN_HEIGHT),
    pygame.math.Vector2(SCREEN_WIDTH / 2 + 0.1 * SCREEN_WIDTH, SCREEN_HEIGHT / 2 + 0.1 * SCREEN_HEIGHT)
]

font = pygame.font.Font('freesansbold.ttf', 32) # credit: https://www.geeksforgeeks.org/python/python-display-text-to-pygame-window/

editing_point_index = None

m1_prev = False
m1_curr = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill(BLACK)

    # RENDER YOUR GAME HERE
    pygame.draw.polygon(SCREEN, WHITE, polygon_pts, width=1)

    # get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # read the state of the left mouse button
    m1_curr = pygame.mouse.get_pressed()[0]

    # for each point...
    for i in range(len(polygon_pts)):
        point = polygon_pts[i]
        point_to_cursor = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(point)

        # get the distance from the point to the cursor
        point_to_cursor_dist = point_to_cursor.length_squared()
        text = None

        # if the cursor is close to the point...
        if point_to_cursor_dist <= point_dist**2:
            # ...draw the point number in white text
            text = font.render(f"{i}", True, WHITE, BLACK)

            # if LMB is pressed but no point has been chosen to be edited, then set the point to be edited
            if m1_curr == True and editing_point_index is None:
                editing_point_index = i
        
        # otherwise (if the cursor is not close to the point)...
        else:
            # ...draw the point number in gray
            text = font.render(f"{i}", True, GRAY, BLACK)

        # if a point is still chosen to be edited, but LMB has been released, then stop editing that point
        if editing_point_index is not None and m1_curr == False:
            editing_point_index = None
        
        text_rect = text.get_rect()

        # position the point number over its corresponding point
        if editing_point_index is not None and editing_point_index == i:
            text_rect.center = mouse_pos
            polygon_pts[i] = mouse_pos
        else:
            text_rect.center = point
            polygon_pts[i] = point

        # draw the point number
        SCREEN.blit(text, text_rect)

        # draw a bounding circle around the point
        pygame.draw.circle(SCREEN, GRAY, point, point_dist, width=1)

    # propogate mouse state back for next frame
    m1_prev = m1_curr

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()