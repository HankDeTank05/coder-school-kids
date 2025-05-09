# language imports
import copy

# library imports
import pygame

# game imports
import common as c
import player as p
import bullet as b

clock = pygame.time.Clock()
running = True
dt=0

player = p.Player(c.GREEN, 500)

#main game loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    c.screen.fill(c.BLACK)

    # step 1: update stuff
    #character.player_update(dt)
    player.update(dt)
    b.bullet_update(dt)

    # step 2: draw stuff
    #character.player_draw()
    player.draw()
    b.bullet_draw()
    pygame.display.flip()

    dt=clock.tick(60)/1000

pygame.quit()
