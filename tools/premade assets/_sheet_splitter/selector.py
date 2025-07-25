# language imports
import os.path

# package imports
import pygame

def select_color(image_path):
    assert(os.path.exists(image_path))
    assert(os.path.isabs(image_path))
    assert(os.path.isfile(image_path) == True)

    image = pygame.image.load(image_path)

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((image.get_width(), image.get_height()))
    clock = pygame.time.Clock()
    running = True

    # left mouse button states
    m1_prev = False # current frame
    m1_curr = False # previous frame

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ##########
        # UPDATE #
        ##########
        m1_curr = pygame.mouse.get_pressed()[0] # get the current state of the left mouse button
        if m1_curr == True and m1_prev == False:
            selected_color = image.get_at(pygame.mouse.get_pos())
            print(selected_color)
            running = False

        ########
        # DRAW #
        ########
        screen.blit(image, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

        # prep for next frame
        m1_prev = m1_curr

    pygame.quit()

    return selected_color
