import pygame
pygame.init() # will make this work

#create the screen
WIDTH = 1280
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#main game loop
while True:
    #closes the gam when we hit the x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update makes the code work
    # draw helps you make things appear